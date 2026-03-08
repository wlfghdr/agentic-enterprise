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