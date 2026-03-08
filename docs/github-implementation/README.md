# GitHub Implementation Guide

> How to implement the agentic-enterprise operating model using GitHub as your platform.

This guide covers the GitHub-specific implementation details: Issues as work backend, Projects for visibility, Actions workflows for CI/CD and DORA metrics.

---

## 1. GitHub Issues as Work Backend

The agentic-enterprise model can use GitHub Issues to track workflow items (signals, missions, tasks) instead of git-file Markdown. Configure in `CONFIG.yaml`:

```yaml
work_backend:
  type: "github-issues"
  github_issues:
    repo: "your-org/your-repo"
    use_projects: true
    use_label_prefixes: true
```

See [`docs/WORK-BACKEND.md`](../WORK-BACKEND.md) for the full backend configuration guide.

### Required Labels

When using `use_label_prefixes: true`, create these labels:

| Prefix | Values |
|--------|--------|
| `artifact:` | `signal`, `signal-triage`, `mission`, `task` |
| `status:` | `open`, `pending`, `proposed`, `active`, `in-progress`, `done`, `closed`, `proceed`, `defer`, `monitor` |
| `layer:` | `steering`, `strategy`, `orchestration`, `execution`, `quality` |
| `loop:` | `discover`, `build`, `ship`, `operate` |
| `priority:` | `critical`, `high`, `medium`, `low` |
| `category:` | `market`, `customer`, `technical`, `internal` |
| `urgency:` | `immediate`, `next-cycle`, `monitor` |

### Issue Templates

Consider creating `.github/ISSUE_TEMPLATE/` templates for:
- Signal (observation filed by agent or human)
- Mission (strategic intent with outcomes)
- Task (concrete work item)

---

## 2. GitHub Projects

Create a GitHub Project board for operational visibility:

**Recommended views:**

| View | Type | Group by | Filter |
|------|------|----------|--------|
| **Kanban** | Board | `status:` label | Open issues |
| **By Layer** | Table | `layer:` label | Open issues |
| **By Priority** | Table | Sort by `priority:` | Open issues |
| **Recently Updated** | Table | Sort by updated | Last 14 days |

---

## 3. GitHub Actions Workflows

### Active in template (`.github/workflows/`)

These workflows are live in the template and run on push/PR:

| Workflow | Purpose | Docs |
|----------|---------|------|
| `validate.yml` | YAML validation, schema checks, placeholder detection | [`SCHEMA-GUIDE.md`](../SCHEMA-GUIDE.md) |
| `policy.yml` | OPA/Conftest policy enforcement | [`POLICY-AS-CODE.md`](../POLICY-AS-CODE.md) |
| `security.yml` | Gitleaks + dependency review | [`SECURITY-SCANNING.md`](../SECURITY-SCANNING.md) |
| `stale.yml` | Close stale issues (weekly) | — |

### Reference implementations (not active — copy to `.github/workflows/` when ready)

These workflow files are provided as **reference implementations**. They are NOT active in the template to avoid triggering on repos that don't have deployment targets configured.

**Copy them to `.github/workflows/` in your company fork when you're ready to use them.**

| Workflow | Purpose | File |
|----------|---------|------|
| `deploy.yml` | Deployment pipeline with DORA frequency telemetry | [`workflows/deploy.yml`](workflows/deploy.yml) |
| `dora-lead-time.yml` | PR lead time measurement (DORA) | [`workflows/dora-lead-time.yml`](workflows/dora-lead-time.yml) |
| `change-failure-rate.yml` | Deployment failure rate tracking (DORA) | [`workflows/change-failure-rate.yml`](workflows/change-failure-rate.yml) |
| `mttr.yml` | Mean time to recovery tracking (DORA) | [`workflows/mttr.yml`](workflows/mttr.yml) |

---

## 4. GitHub Settings

See [`REQUIRED-GITHUB-SETTINGS.md`](../REQUIRED-GITHUB-SETTINGS.md) for branch protection, CODEOWNERS, and required status checks.

---

## 5. Automation Scripts

Scripts in `scripts/` work with both git-files and github-issues backends:

| Script | Purpose | Backend-aware? |
|--------|---------|---------------|
| `work_backend.py` | Backend abstraction layer | Core |
| `triage_signals.py` | Rule-based signal triage | ✅ |
| `find_pending_work.py` | Find actionable work items | ✅ |
| `approval_queue.py` | Build human approval queue | ✅ |
| `archive_work.sh` | Archive completed artifacts | git-files only |
| `archive_runs.sh` | Monthly run log rotation | git-files only |

Scripts that are backend-aware use `work_backend.py` to read from the correct source (Issues or git files) based on `CONFIG.yaml`.

