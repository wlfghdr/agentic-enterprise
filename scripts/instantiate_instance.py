#!/usr/bin/env python3
"""Bootstrap helpers for turning the framework template into a live instance.

Four high-friction tasks are intentionally automated here:

1. ``cleanup-instance`` removes template-only assets and rewrites the top-level
   instance-facing docs after ``CONFIG.yaml`` has been filled in.
2. ``install-github-work-repo`` copies the GitHub issue-backend kit into the
   repo that will host operational issues.
3. ``prune-agents`` removes unused divisions and agent type definitions
   based on CONFIG.yaml and a keep-list, reducing template bloat.
4. ``install-pr-automation`` adds auto-merge and issue-linking workflows
   for governed PR lifecycle.

Recommended order:
1. Fill in ``CONFIG.yaml``
2. Run ``prune-agents`` to reduce to your actual org structure
3. Run ``install-pr-automation`` for PR governance
4. Run ``install-github-work-repo`` if the issue backend will be used
5. Run ``cleanup-instance`` to strip remaining template-facing assets
"""

from __future__ import annotations

import argparse
import shutil
import sys
import textwrap
from pathlib import Path
from typing import Any

import yaml

from work_backend import ISSUE_BACKEND, load_work_backend

DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_REPO_URL = "https://github.com/wlfghdr/agentic-enterprise"

TEMPLATE_ONLY_PATHS = [
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "index.html",
    "concept-visualization.html",
    "docs/customization-guide.md",
    "docs/file-guide.md",
    "docs/adoption",
    "docs/reference-organization",
    "docs/github",
    "docs/compliance",
    "docs/runtimes",
    "docs/quickstart",
    "examples/generic-feature-lifecycle.md",
    "examples/company-optimization-lifecycle.md",
    "examples/agent-fleet-change-lifecycle.md",
    "examples/hr-recruiting-lifecycle.md",
]

ISSUE_FORM_SAMPLES = {
    "config.yml": "docs/github/issue-templates/config.sample.yml",
    "signal.yml": "docs/github/issue-templates/forms/signal.sample.yml",
    "mission.yml": "docs/github/issue-templates/forms/mission.sample.yml",
    "task.yml": "docs/github/issue-templates/forms/task.sample.yml",
    "decision.yml": "docs/github/issue-templates/forms/decision.sample.yml",
    "release.yml": "docs/github/issue-templates/forms/release.sample.yml",
    "retrospective.yml": "docs/github/issue-templates/forms/retrospective.sample.yml",
}

WORKFLOW_SAMPLES = {
    "validate-issue-templates.yml": "docs/github/workflows/validate-issue-templates.yml",
    "sync-issue-form-labels.yml": "docs/github/workflows/sync-issue-form-labels.yml",
}

LABELS_SAMPLE = "docs/github/labels/labels.sample.yml"


def load_config(repo_root: Path) -> dict[str, Any]:
    config_path = repo_root / "CONFIG.yaml"
    try:
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError as exc:
        raise SystemExit(f"CONFIG.yaml not found at {config_path}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit("CONFIG.yaml must parse to a mapping")
    return loaded


def company_value(config: dict[str, Any], key: str, default: str) -> str:
    company = config.get("company") or {}
    value = company.get(key)
    if not isinstance(value, str):
        return default
    stripped = value.strip()
    return stripped or default


def write_text(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        print(f"WOULD WRITE {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"WROTE {path}")


def remove_path(path: Path, dry_run: bool) -> None:
    if not path.exists():
        return
    if dry_run:
        print(f"WOULD REMOVE {path}")
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()
    print(f"REMOVED {path}")


def render_readme(company_name: str, instance_repo: str, backend_type: str, issue_repo: str) -> str:
    backend_note = "Operational work lives directly in `work/`." if backend_type != ISSUE_BACKEND else (
        f"Day-to-day issue tracking lives in `{issue_repo}`."
        if issue_repo and issue_repo != instance_repo
        else "Day-to-day issue tracking lives in GitHub Issues in this repository."
    )
    repo_boundary = (
        f"- `{issue_repo}` is the issue frontend: issue forms, labels, Project status tracking, and work board views.\n"
        if backend_type == ISSUE_BACKEND and issue_repo and issue_repo != instance_repo
        else ""
    )
    return textwrap.dedent(
        f"""
        # {company_name} Operating Model

        This repository is the live `{company_name}` instance of the Agentic Enterprise operating model. It holds the governed backbone for roles, policies, decision records, durable work evidence, and validation.

        This is not the public framework template. Generic instantiation guidance belongs upstream in [`wlfghdr/agentic-enterprise`]({TEMPLATE_REPO_URL}).

        ## Start Here

        - [`docs/repo-scope.md`](docs/repo-scope.md) explains what belongs in this repo versus upstream template or work repo.
        - [`docs/work-tracking.md`](docs/work-tracking.md) explains how work is tracked in this instance.
        - [`docs/github-issues.md`](docs/github-issues.md) defines the live GitHub issue-backend operating rules.
        - [`docs/required-github-settings.md`](docs/required-github-settings.md) lists the GitHub governance settings that must remain enforced.
        - [`org/README.md`](org/README.md) is the organizational backbone for layers, roles, and ownership.

        ## Repository Boundaries

        - `{instance_repo}` is the governance backbone: org model, policies, process rules, durable evidence, and validation.
        {repo_boundary}- `agentic-enterprise` is the upstream template: reusable framework guidance, instantiation assets, and generic setup tooling.

        ## Operating Notes

        - {backend_note}
        - Git-backed companion artifacts still stay here: technical designs, quality evaluations, fleet reports, outcome reports, governance exceptions, locks, and asset registry entries.
        - Generic framework improvements should go upstream first and then be pulled back into this instance deliberately.
        """
    ).strip()


def render_docs_readme() -> str:
    return textwrap.dedent(
        """
        # docs/ — Instance Operator Guides
        <!-- placeholder-ok -->

        This folder contains the instance-specific operating notes that sit on top of the upstream Agentic Enterprise framework.

        ## Start Here

        | If you need to... | Read this first |
        |---|---|
        | Understand what this repo is responsible for | [`repo-scope.md`](repo-scope.md) |
        | Understand where work lives | [`work-tracking.md`](work-tracking.md) |
        | Run the issue backend day to day | [`github-issues.md`](github-issues.md) |
        | Verify GitHub governance settings | [`required-github-settings.md`](required-github-settings.md) |
        | Understand backend behavior and artifact placement | [`work-backends.md`](work-backends.md) |

        ## Core Instance Docs

        - [`repo-scope.md`](repo-scope.md)
        - [`work-tracking.md`](work-tracking.md)
        - [`github-issues.md`](github-issues.md)
        - [`required-github-settings.md`](required-github-settings.md)
        - [`automation-and-work-continuity.md`](automation-and-work-continuity.md)

        ## Upstream-Only Concerns

        Generic fork cleanup, reusable GitHub kits, and template-facing onboarding belong upstream in [`wlfghdr/agentic-enterprise`](https://github.com/wlfghdr/agentic-enterprise).
        """
    ).strip()


def render_repo_scope(instance_repo: str, backend_type: str, issue_repo: str) -> str:
    extra = (
        f"- operational issue frontend in `{issue_repo}`\n"
        if backend_type == ISSUE_BACKEND and issue_repo and issue_repo != instance_repo
        else ""
    )
    return textwrap.dedent(
        f"""
        # Repository Scope

        This repository is the operating-model backbone for `{instance_repo}`. It is intentionally narrower than the upstream template and intentionally different from any dedicated issue frontend.

        ## What belongs here

        - organizational structure under `org/`
        - global agent instructions and governance rules
        - quality policies and validation scripts
        - process definitions and reference guides
        - durable Git-backed work evidence such as technical designs, fleet reports, outcome reports, governance exceptions, locks, and asset registry entries
        - instance-specific operator documentation in `docs/`

        ## What does not belong here

        - template marketing/demo assets
        - generic fork or instantiation walkthroughs
        - GitHub asset sample kits meant to be copied into other repos
        - a second copy of upstream framework adoption material unless this instance has explicitly customized it

        ## Where those things live instead

        - upstream template and reusable instantiation assets: [`wlfghdr/agentic-enterprise`]({TEMPLATE_REPO_URL})
        {extra}- separate product repos stay separate from the governance backbone

        ## Rule of Thumb

        If the artifact is reusable across many companies, it belongs upstream.
        If the artifact defines or records how this organization is governed, it belongs here.
        """
    ).strip()


def render_work_tracking(instance_repo: str, backend_type: str, issue_repo: str) -> str:
    if backend_type == ISSUE_BACKEND:
        topology_lines = [
            f"- `{instance_repo}` is the governed operating-model repository.",
            (
                f"- `{issue_repo}` is the GitHub issue frontend configured in `CONFIG.yaml`."
                if issue_repo and issue_repo != instance_repo
                else "- GitHub Issues in this repository are the operational work frontend."
            ),
        ]
        active_backend = textwrap.dedent(
            f"""
            `CONFIG.yaml` currently declares:

            - `work_backend.type: "github-issues"`
            - `work_backend.github_issues.repo: "{issue_repo if issue_repo else ''}"`
            - `work_backend.github_issues.use_projects: true`

            That means day-to-day signals, missions, tasks, releases, and retrospectives are tracked as issues, while durable companion artifacts remain in Git here.
            """
        ).strip()
    else:
        topology_lines = [f"- `{instance_repo}` is both the governance backbone and the work-tracking repository."]
        active_backend = textwrap.dedent(
            """
            `CONFIG.yaml` currently declares:

            - `work_backend.type: "git-files"`

            That means operational work artifacts are tracked directly under `work/`.
            """
        ).strip()

    topology_block = "\n".join(topology_lines)

    return textwrap.dedent(
        f"""
        # Work Tracking

        {topology_block}

        ## Active Backend Configuration

        {active_backend}

        ## What stays in this repo

        - mission-adjacent technical designs, fleet reports, and outcome reports
        - governance exceptions and decision records that must stay durable in Git
        - asset registry entries
        - locks and validation scripts
        - the organization model, policies, and operating instructions

        ## Operator Shortcut

        Use [`github-issues.md`](github-issues.md) for the live issue workflow and [`work-backends.md`](work-backends.md) for the backend contract underneath it.
        """
    ).strip()


def cmd_cleanup_instance(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    config = load_config(repo_root)
    backend = load_work_backend(repo_root)
    company_name = company_value(config, "name", repo_root.name)
    repo_slug = company_value(config, "repo_slug", repo_root.name)
    issue_repo = backend.configured_issue_repo() or repo_slug

    for rel_path in TEMPLATE_ONLY_PATHS:
        remove_path(repo_root / rel_path, args.dry_run)

    generated_docs = {
        repo_root / "README.md": render_readme(company_name, repo_slug, backend.type, issue_repo),
        repo_root / "docs/README.md": render_docs_readme(),
        repo_root / "docs/repo-scope.md": render_repo_scope(repo_slug, backend.type, issue_repo),
        repo_root / "docs/work-tracking.md": render_work_tracking(repo_slug, backend.type, issue_repo),
    }

    for path, content in generated_docs.items():
        write_text(path, content, args.dry_run)

    return 0


def read_asset(repo_root: Path, relative_path: str) -> str:
    asset_path = repo_root / relative_path
    if not asset_path.exists():
        raise SystemExit(
            f"Required asset not found: {asset_path}\n"
            "Run this command from a fresh template checkout or before cleanup-instance removes docs/github."
        )
    return asset_path.read_text(encoding="utf-8")


def write_yaml(path: Path, data: Any, dry_run: bool) -> None:
    if dry_run:
        print(f"WOULD WRITE {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    print(f"WROTE {path}")


def cmd_install_github_work_repo(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    load_config(repo_root)  # fail fast if CONFIG.yaml is missing/broken
    target_dir = Path(args.target_dir).resolve()

    config_template = yaml.safe_load(read_asset(repo_root, ISSUE_FORM_SAMPLES["config.yml"]))
    contact_links = config_template.get("contact_links") or []
    if contact_links:
        contact_links[0]["url"] = f"https://github.com/{args.main_repo}/blob/main/docs/github-issues.md"
    if len(contact_links) > 1:
        contact_links[1]["url"] = args.discussion_url or f"https://github.com/{args.main_repo}/discussions"

    write_yaml(target_dir / ".github/ISSUE_TEMPLATE/config.yml", config_template, args.dry_run)

    for target_name, source_rel in ISSUE_FORM_SAMPLES.items():
        if target_name == "config.yml":
            continue
        content = read_asset(repo_root, source_rel)
        write_text(target_dir / ".github/ISSUE_TEMPLATE" / target_name, content, args.dry_run)

    labels_content = read_asset(repo_root, LABELS_SAMPLE)
    write_text(target_dir / ".github/labels.sample.yml", labels_content, args.dry_run)

    validate_workflow = read_asset(repo_root, WORKFLOW_SAMPLES["validate-issue-templates.yml"])
    write_text(
        target_dir / ".github/workflows/validate-issue-templates.yml",
        validate_workflow,
        args.dry_run,
    )

    if args.include_label_sync:
        sync_workflow = read_asset(repo_root, WORKFLOW_SAMPLES["sync-issue-form-labels.yml"])
        write_text(
            target_dir / ".github/workflows/sync-issue-form-labels.yml",
            sync_workflow,
            args.dry_run,
        )

    return 0


def extract_division_ids(config: dict[str, Any]) -> set[str]:
    """Return all division ``id`` values from every category under the ``divisions`` key."""
    ids: set[str] = set()
    divisions = config.get("divisions")
    if not divisions:
        return ids
    if isinstance(divisions, list):
        # flat list of division dicts
        for entry in divisions:
            if isinstance(entry, dict) and "id" in entry:
                ids.add(entry["id"])
    elif isinstance(divisions, dict):
        # mapping of category -> list of division dicts
        for category_entries in divisions.values():
            if not isinstance(category_entries, list):
                continue
            for entry in category_entries:
                if isinstance(entry, dict) and "id" in entry:
                    ids.add(entry["id"])
    return ids


def cmd_prune_agents(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    config = load_config(repo_root)

    # --- Prune divisions ---
    division_ids = extract_division_ids(config)
    divisions_dir = repo_root / "org" / "3-execution" / "divisions"

    removed_divisions: list[str] = []
    kept_divisions: list[str] = []

    if divisions_dir.is_dir():
        for child in sorted(divisions_dir.iterdir()):
            if not child.is_dir():
                continue
            if child.name.startswith("_TEMPLATE"):
                kept_divisions.append(child.name)
                continue
            if child.name in division_ids:
                kept_divisions.append(child.name)
            else:
                remove_path(child, args.dry_run)
                removed_divisions.append(child.name)

    # --- Prune agent types ---
    keep_agents_raw = args.keep_agents or ""
    keep_set = {a.strip() for a in keep_agents_raw.split(",") if a.strip()}

    agents_dir = repo_root / "org" / "agents"

    removed_agents: list[str] = []
    kept_agents: list[str] = []

    if agents_dir.is_dir():
        for child in sorted(agents_dir.iterdir()):
            if not child.is_file() or child.suffix != ".md":
                continue
            # Always keep README.md and _TEMPLATE files
            if child.name == "README.md" or child.name.startswith("_TEMPLATE"):
                kept_agents.append(child.name)
                continue
            stem = child.stem
            if stem in keep_set:
                kept_agents.append(child.name)
            else:
                remove_path(child, args.dry_run)
                removed_agents.append(child.name)

    # --- Summary ---
    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}=== Prune Summary ===")
    print(f"Divisions kept  ({len(kept_divisions)}): {', '.join(kept_divisions) or '(none)'}")
    print(f"Divisions removed ({len(removed_divisions)}): {', '.join(removed_divisions) or '(none)'}")
    print(f"Agent files kept  ({len(kept_agents)}): {', '.join(kept_agents) or '(none)'}")
    print(f"Agent files removed ({len(removed_agents)}): {', '.join(removed_agents) or '(none)'}")

    return 0


AUTO_MERGE_WORKFLOW = """\
name: Auto-merge on approval
on:
  pull_request_review:
    types: [submitted]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    if: github.event.review.state == 'approved'
    runs-on: ubuntu-latest
    steps:
      - name: Enable auto-merge
        run: gh pr merge --auto --squash "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""

CHECK_ISSUE_LINK_WORKFLOW = """\
name: Check issue link
on:
  pull_request:
    types: [opened, edited]

jobs:
  check-link:
    runs-on: ubuntu-latest
    steps:
      - name: Check for issue reference
        env:
          PR_BODY: ${{ github.event.pull_request.body }}
        run: |
          if echo "$PR_BODY" | grep -qiE '(closes|fixes|resolves)\\s+#[0-9]+'; then
            echo "Issue reference found"
          else
            echo "::error::PR must link to an originating issue using 'closes #NNN', 'fixes #NNN', or 'resolves #NNN'"
            exit 1
          fi
"""

PR_TEMPLATE = """\
## Summary

<!-- Describe the change and its purpose. -->

## Linked Issues

closes #

## Test Plan

<!-- How was this tested? What should reviewers verify? -->
"""


def cmd_install_pr_automation(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()

    workflows_dir = repo_root / ".github" / "workflows"

    write_text(workflows_dir / "auto-merge.yml", AUTO_MERGE_WORKFLOW, args.dry_run)
    write_text(workflows_dir / "check-issue-link.yml", CHECK_ISSUE_LINK_WORKFLOW, args.dry_run)

    pr_template_path = repo_root / ".github" / "PULL_REQUEST_TEMPLATE.md"
    if pr_template_path.exists():
        existing = pr_template_path.read_text(encoding="utf-8")
        if "Linked Issues" not in existing:
            updated = existing.rstrip() + "\n\n## Linked Issues\n\ncloses #\n"
            write_text(pr_template_path, updated, args.dry_run)
        else:
            print(f"SKIPPED {pr_template_path} (already contains Linked Issues section)")
    else:
        write_text(pr_template_path, PR_TEMPLATE, args.dry_run)

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=str(DEFAULT_REPO_ROOT),
        help="Path to the framework checkout or freshly forked instance repo",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files")

    subparsers = parser.add_subparsers(dest="command", required=True)

    cleanup = subparsers.add_parser(
        "cleanup-instance",
        help="Remove template-only assets and rewrite top-level instance docs",
    )
    cleanup.set_defaults(func=cmd_cleanup_instance)

    install = subparsers.add_parser(
        "install-github-work-repo",
        help="Copy issue-backend assets into the repo that will host operational issues",
    )
    install.add_argument(
        "--target-dir",
        required=True,
        help="Path to the repo that should receive the GitHub issue-backend assets",
    )
    install.add_argument(
        "--main-repo",
        required=True,
        help="owner/name of the main operating-model repo whose docs the forms should link to",
    )
    install.add_argument(
        "--discussion-url",
        default="",
        help="Optional GitHub Discussions URL for the issue-template config",
    )
    install.add_argument(
        "--include-label-sync",
        action="store_true",
        help="Also install the optional workflow that maps issue-form answers to labels",
    )
    install.set_defaults(func=cmd_install_github_work_repo)

    prune = subparsers.add_parser(
        "prune-agents",
        help="Remove unused divisions and agent type definitions based on CONFIG.yaml and a keep-list",
    )
    prune.add_argument(
        "--keep-agents",
        default="",
        help="Comma-separated list of agent filenames (without .md) to keep, e.g. 'signal-aggregation-agent,coding-agent-fleet'",
    )
    prune.set_defaults(func=cmd_prune_agents)

    pr_auto = subparsers.add_parser(
        "install-pr-automation",
        help="Add auto-merge and issue-linking workflows for governed PR lifecycle",
    )
    pr_auto.set_defaults(func=cmd_install_pr_automation)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
