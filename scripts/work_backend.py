#!/usr/bin/env python3
"""Shared work-backend helpers for agentic-enterprise automation.

Operational artifacts can live either in Git files or GitHub Issues. This
module centralizes backend lookup so individual scripts don't hardcode
`work/`-only assumptions.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent
ISSUE_BACKEND = "github-issues"
GIT_BACKEND = "git-files"


@dataclass(frozen=True)
class WorkBackend:
    repo_root: Path
    type: str = GIT_BACKEND
    github_repo: str = ""
    use_projects: bool = True
    project_owner: str = ""
    project_number: int = 0
    use_label_prefixes: bool = True
    overrides: dict[str, str] = field(default_factory=dict)

    def backend_for(self, artifact_type: str) -> str:
        if artifact_type == "lock":
            return GIT_BACKEND
        return self.overrides.get(artifact_type, self.type)

    def uses_issues_for(self, artifact_type: str) -> bool:
        return self.backend_for(artifact_type) == ISSUE_BACKEND

    def configured_issue_repo(self) -> str:
        return self.github_repo.strip()

    def to_dict(self) -> dict[str, Any]:
        return {
            "type": self.type,
            "github_repo": self.github_repo,
            "use_projects": self.use_projects,
            "project_owner": self.project_owner,
            "project_number": self.project_number,
            "use_label_prefixes": self.use_label_prefixes,
            "overrides": dict(self.overrides),
        }


def load_work_backend(repo_root: Path | None = None) -> WorkBackend:
    root = (repo_root or DEFAULT_REPO_ROOT).resolve()
    config_path = root / "CONFIG.yaml"
    config: dict[str, Any] = {}
    if config_path.exists():
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            config = loaded

    backend_cfg = config.get("work_backend") or {}
    github_cfg = backend_cfg.get("github_issues") or {}
    overrides = backend_cfg.get("overrides") or {}

    return WorkBackend(
        repo_root=root,
        type=backend_cfg.get("type", GIT_BACKEND),
        github_repo=github_cfg.get("repo", ""),
        use_projects=bool(github_cfg.get("use_projects", True)),
        project_owner=github_cfg.get("project_owner", ""),
        project_number=int(github_cfg.get("project_number", 0)),
        use_label_prefixes=bool(github_cfg.get("use_label_prefixes", True)),
        overrides=dict(overrides),
    )


def label_names(issue: dict[str, Any]) -> list[str]:
    names: list[str] = []
    for label in issue.get("labels") or []:
        if isinstance(label, dict):
            name = label.get("name")
            if name:
                names.append(name)
        elif isinstance(label, str):
            names.append(label)
    return names


def prefixed_label(issue: dict[str, Any], prefix: str) -> str | None:
    for label in label_names(issue):
        if label.startswith(prefix):
            return label
    return None


def strip_prefix(label: str | None, prefix: str) -> str | None:
    if not label or not label.startswith(prefix):
        return None
    return label[len(prefix):]


def issue_reference_from_body(body: str, *field_names: str) -> int | None:
    if not body or not field_names:
        return None
    joined = "|".join(re.escape(name) for name in field_names)
    pattern = re.compile(
        rf"(?im)^(?:[-*]\s*)?(?:\*\*)?(?:{joined})(?:\*\*)?:\s*#(\d+)\b"
    )
    match = pattern.search(body)
    return int(match.group(1)) if match else None


def gh_json(args: list[str], repo: str = "", cwd: Path | None = None) -> Any:
    command = ["gh", *args]
    if repo:
        command.extend(["--repo", repo])

    result = subprocess.run(
        command,
        cwd=str(cwd or DEFAULT_REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "gh command failed")
    return json.loads(result.stdout or "null")


def _graphql_cmd(query: str, variables: dict[str, Any], cwd: Path | None = None) -> Any:
    """Execute a GraphQL query via ``gh api graphql``.

    Each variable is passed as a separate flag (``-f`` for strings, ``-F``
    for integers/booleans) because ``gh`` does **not** support a single
    ``-f variables=...`` blob.
    """
    command: list[str] = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        if isinstance(value, (int, bool)):
            command.extend(["-F", f"{key}={json.dumps(value)}"])
        else:
            command.extend(["-f", f"{key}={value}"])

    result = subprocess.run(
        command,
        cwd=str(cwd or DEFAULT_REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "graphql query failed")
    return json.loads(result.stdout or "null")


def get_project_statuses(
    backend: WorkBackend,
    issue_numbers: list[int] | None = None,
) -> dict[int, str | None]:
    """Return ``{issue_number: project_status}`` for issues in the project.

    Paginates through all project items.  If *issue_numbers* is given,
    only those issues are included in the result.
    """
    owner = backend.project_owner
    number = backend.project_number
    if not owner or not number:
        return {}

    statuses: dict[int, str | None] = {}
    cursor: str | None = None

    while True:
        after_clause = f', after: "{cursor}"' if cursor else ""
        query = """
        query($owner: String!, $number: Int!) {
          organization(login: $owner) {
            projectV2(number: $number) {
              items(first: 100%s) {
                pageInfo { hasNextPage endCursor }
                nodes {
                  fieldValueByName(name: "Status") {
                    ... on ProjectV2ItemFieldSingleSelectValue { name }
                  }
                  content {
                    ... on Issue { number }
                  }
                }
              }
            }
          }
        }
        """ % after_clause

        data = _graphql_cmd(query, {"owner": owner, "number": number}, cwd=backend.repo_root)
        project = (data.get("data") or {}).get("organization", {}).get("projectV2")
        if not project:
            # Try user-owned project as fallback
            query_user = query.replace("organization(login: $owner)", "user(login: $owner)")
            data = _graphql_cmd(query_user, {"owner": owner, "number": number}, cwd=backend.repo_root)
            project = (data.get("data") or {}).get("user", {}).get("projectV2")
            if not project:
                break

        items = project.get("items", {})
        for node in items.get("nodes", []):
            content = node.get("content") or {}
            issue_num = content.get("number")
            if issue_num is None:
                continue
            field_val = node.get("fieldValueByName") or {}
            status = field_val.get("name")
            statuses[issue_num] = status

        page_info = items.get("pageInfo", {})
        if page_info.get("hasNextPage"):
            cursor = page_info.get("endCursor")
        else:
            break

    if issue_numbers is not None:
        return {n: statuses.get(n) for n in issue_numbers}
    return statuses


def set_project_status(
    backend: WorkBackend,
    issue_number: int,
    status: str,
    repo: str = "",
) -> None:
    """Set the Project Status field for an issue.

    If the issue is not yet in the project, it is added first.
    """
    owner = backend.project_owner
    number = backend.project_number
    if not owner or not number:
        raise RuntimeError("project_owner and project_number must be set in CONFIG.yaml")

    # 1. Get project ID, status field ID, and option ID
    meta_query = """
    query($owner: String!, $number: Int!) {
      organization(login: $owner) {
        projectV2(number: $number) {
          id
          field(name: "Status") {
            ... on ProjectV2SingleSelectField {
              id
              options { id name }
            }
          }
        }
      }
    }
    """
    data = _graphql_cmd(meta_query, {"owner": owner, "number": number}, cwd=backend.repo_root)
    project_data = (data.get("data") or {}).get("organization", {}).get("projectV2")
    if not project_data:
        meta_user = meta_query.replace("organization(login: $owner)", "user(login: $owner)")
        data = _graphql_cmd(meta_user, {"owner": owner, "number": number}, cwd=backend.repo_root)
        project_data = (data.get("data") or {}).get("user", {}).get("projectV2")
        if not project_data:
            raise RuntimeError(f"Project {owner}/{number} not found")

    project_id = project_data["id"]
    field_data = project_data.get("field") or {}
    field_id = field_data.get("id")
    if not field_id:
        raise RuntimeError("Status field not found in project")

    option_id = None
    for opt in field_data.get("options", []):
        if opt.get("name") == status:
            option_id = opt["id"]
            break
    if not option_id:
        valid = [o["name"] for o in field_data.get("options", [])]
        raise RuntimeError(f"Status option '{status}' not found. Valid: {valid}")

    # 2. Find the item ID for this issue in the project (paginated)
    item_id = _find_project_item(project_data["id"], issue_number, owner, number, backend.repo_root)

    # 3. If not in project, add it
    if not item_id:
        issue_node_id = _get_issue_node_id(issue_number, repo or backend.github_repo, backend.repo_root)
        add_mutation = """
        mutation($projectId: ID!, $contentId: ID!) {
          addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
            item { id }
          }
        }
        """
        result = _graphql_cmd(add_mutation, {"projectId": project_id, "contentId": issue_node_id}, cwd=backend.repo_root)
        item_id = (result.get("data") or {}).get("addProjectV2ItemById", {}).get("item", {}).get("id")
        if not item_id:
            raise RuntimeError(f"Failed to add issue #{issue_number} to project")

    # 4. Set the status field
    update_mutation = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId,
        itemId: $itemId,
        fieldId: $fieldId,
        value: {singleSelectOptionId: $optionId}
      }) {
        projectV2Item { id }
      }
    }
    """
    _graphql_cmd(update_mutation, {
        "projectId": project_id,
        "itemId": item_id,
        "fieldId": field_id,
        "optionId": option_id,
    }, cwd=backend.repo_root)


def _find_project_item(project_id: str, issue_number: int, owner: str, number: int, cwd: Path) -> str | None:
    """Find the project item ID for a given issue number (paginated)."""
    cursor: str | None = None
    while True:
        after_clause = f', after: "{cursor}"' if cursor else ""
        query = """
        query($owner: String!, $number: Int!) {
          organization(login: $owner) {
            projectV2(number: $number) {
              items(first: 100%s) {
                pageInfo { hasNextPage endCursor }
                nodes {
                  id
                  content { ... on Issue { number } }
                }
              }
            }
          }
        }
        """ % after_clause
        data = _graphql_cmd(query, {"owner": owner, "number": number}, cwd=cwd)
        project = (data.get("data") or {}).get("organization", {}).get("projectV2")
        if not project:
            query_user = query.replace("organization(login: $owner)", "user(login: $owner)")
            data = _graphql_cmd(query_user, {"owner": owner, "number": number}, cwd=cwd)
            project = (data.get("data") or {}).get("user", {}).get("projectV2")
            if not project:
                return None

        for node in project.get("items", {}).get("nodes", []):
            content = node.get("content") or {}
            if content.get("number") == issue_number:
                return node["id"]

        page_info = project.get("items", {}).get("pageInfo", {})
        if page_info.get("hasNextPage"):
            cursor = page_info.get("endCursor")
        else:
            return None


def _get_issue_node_id(issue_number: int, repo: str, cwd: Path) -> str:
    """Get the GraphQL node ID for a GitHub issue."""
    args = ["issue", "view", str(issue_number), "--json", "id"]
    result = gh_json(args, repo=repo, cwd=cwd)
    node_id = result.get("id") if isinstance(result, dict) else None
    if not node_id:
        raise RuntimeError(f"Could not resolve node ID for issue #{issue_number}")
    return node_id


def _main(argv: list[str]) -> int:
    backend = load_work_backend()
    if len(argv) < 2:
        print(json.dumps(backend.to_dict(), indent=2, ensure_ascii=False))
        return 0

    command = argv[1]
    if command == "type":
        print(backend.type)
        return 0
    if command == "repo":
        print(backend.configured_issue_repo())
        return 0
    if command == "backend" and len(argv) >= 3:
        print(backend.backend_for(argv[2]))
        return 0
    if command == "summary":
        print(json.dumps(backend.to_dict(), indent=2, ensure_ascii=False))
        return 0

    print(f"Unknown command: {' '.join(argv[1:])}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))