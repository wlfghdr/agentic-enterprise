# Work Backend Configuration

> How operational artifacts are stored and managed.

## Overview

The agentic-enterprise framework supports two storage backends for operational artifacts:

- **`git-files`** — Markdown files in `work/` directories (default)
- **`github-issues`** — GitHub Issues with structured labels

The backend is configured in `CONFIG.yaml` under `work_backend`. Scripts use `scripts/work_backend.py` to abstract backend access.

## Configuration

```yaml
work_backend:
  type: "github-issues"          # or "git-files"

  github_issues:
    repo: "your-org/your-repo"   # GitHub repo for issues
    use_projects: true            # use GitHub Projects for boards + status tracking
    project_owner: "your-org"    # GitHub org or user owning the project
    project_number: 2             # GitHub Project v2 number
    use_label_prefixes: true      # structured labels (artifact:, layer:, loop:, etc.)

  overrides:
    # These artifact types always stay in git (documents, not workflow)
    technical-design: "git-files"
    decision: "git-files"
    quality-eval: "git-files"
    outcome-report: "git-files"
    fleet-report: "git-files"
    governance-exception: "git-files"
    asset-registry: "git-files"
    signal-digest: "git-files"
    lock: "git-files"
```

## What Goes Where

The split follows a simple principle:

**GitHub Issues** = workflow items (status changes, assignments, comments)
- Signals — observations that need triage
- Signal triage records — triage outcomes
- Missions — mission tracking with status transitions
- Tasks — concrete work items with assignments

**Git files** = documents/deliverables (written, reviewed, versioned)
- Technical designs — architecture docs
- Decisions — ADRs (Architecture Decision Records)
- Quality evaluations — review reports
- Outcome reports — mission closure reports
- Fleet reports — fleet performance data
- Governance exceptions — exception records
- Asset registry entries — delivered artifact metadata
- Signal digests — research summaries
- Locks — file lock records

## Label Structure (when using github-issues)

Issues use prefixed labels for structured filtering:

| Prefix | Values | Example |
|--------|--------|---------|
| `artifact:` | signal, signal-triage, mission, task | `artifact:task` |
| _(Status)_ | Tracked via GitHub Project Status field, not labels | _(see GITHUB-ISSUES.md)_ |
| `layer:` | steering, strategy, orchestration, execution, quality | `layer:execution` |
| `loop:` | discover, build, ship, operate | `loop:build` |
| `priority:` | critical, high, medium, low | `priority:high` |
| `category:` | market, customer, technical, internal | `category:technical` |

## Scripts

All automation scripts use `work_backend.py` to read from the correct backend:

```python
from work_backend import load_work_backend

wb = load_work_backend()
if wb.uses_issues_for("signal"):
    # read signals from GitHub Issues
else:
    # read signals from work/signals/*.md
```

## Migration

When switching from `git-files` to `github-issues`:

1. Update `CONFIG.yaml` → `work_backend.type: "github-issues"`
2. Create issues for active work items (signals, missions, tasks)
3. Archive git-file versions of migrated items
4. Keep overrides for document-type artifacts

The dual-backend pattern in `work_backend.py` ensures scripts work correctly during and after migration.
