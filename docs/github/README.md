# GitHub Implementation Guide

> How to implement the agentic-enterprise operating model using GitHub as your platform.

This guide covers the GitHub-specific implementation details: Issues as work backend, Projects for visibility, Actions workflows for CI/CD and DORA metrics.

This folder is the GitHub instance kit for company forks:

- `README.md` explains the GitHub operating model.
- `setup-checklist.md` is the one-pass setup sequence for the GitHub issue backend.
- `issue-templates/` contains copyable files for `.github/ISSUE_TEMPLATE/`.
- `labels/` contains a copyable label bootstrap sample.
- `workflows/` contains reference workflows you can copy into `.github/workflows/`.

The preferred installation path is scripted:

```bash
python3 scripts/instantiate_instance.py install-github-work-repo \
  --main-repo your-org/your-instance \
  --target-dir ../your-instance-work

python3 scripts/instantiate_instance.py install-pr-automation
```

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

See [`docs/work-backends.md`](../work-backends.md) for the full backend configuration guide.

### Required Labels

When using `use_label_prefixes: true`, create these labels:

| Prefix | Values |
|--------|--------|
| `artifact:` | `signal`, `mission`, `task`, `decision`, `release`, `retrospective` |
| `layer:` | `steering`, `strategy`, `orchestration`, `execution`, `quality` |
| `loop:` | `discover`, `build`, `ship`, `operate` |
| `priority:` | `critical`, `high`, `medium`, `low` |
| `category:` | `market`, `customer`, `technical`, `internal`, `competitive`, `financial` |
| `confidence:` | `high`, `medium`, `low` |
| `urgency:` | `immediate`, `next-cycle`, `monitor` |

> **Status tracking:** Do not create `status:*` labels. Use the GitHub Project (v2) **Status** field instead. See [docs/github-issues.md](../github-issues.md).

Use [`labels/labels.sample.yml`](labels/labels.sample.yml) as the bootstrap source of truth.

### Issue Templates

Consider creating `.github/ISSUE_TEMPLATE/` templates for:
- Signal (observation filed by agent or human)
- Mission (strategic intent with outcomes)
- Task (concrete work item)

Copy the samples from `issue-templates/` in this folder into your instance repository when you enable the issue backend, or use the scripted install step above.

Important limitation:
- Issue Forms can set only static base labels directly.
- Dynamic labels such as `priority:*`, `category:*`, `confidence:*`, and `urgency:*` need either human discipline or automation.

Use [`workflows/sync-issue-form-labels.yml`](workflows/sync-issue-form-labels.yml) if you want those labels synchronized from form answers automatically.

---

## 2. GitHub Projects

Create a GitHub Project board for operational visibility:

**Recommended views:**

| View | Type | Group by | Filter |
|------|------|----------|--------|
| **Kanban** | Board | Project Status field | Open issues |
| **By Layer** | Table | `layer:` label | Open issues |
| **By Priority** | Table | Sort by `priority:` | Open issues |
| **Recently Updated** | Table | Sort by updated | Last 14 days |

---

## 3. GitHub Actions Workflows

### Active in template (`.github/workflows/`)

These workflows are live in the template and run on push/PR:

| Workflow | Purpose | Docs |
|----------|---------|------|
| `validate.yml` | YAML validation, schema checks, placeholder detection, OPA/Conftest policy enforcement | [`schema-guide.md`](../schema-guide.md), [`policy-as-code.md`](../policy-as-code.md) |
| `security.yml` | Gitleaks + dependency review | [`security-scanning.md`](../security-scanning.md) |

### Reference implementations (not active — copy to `.github/workflows/` when ready)

These workflow files are provided as **reference implementations**. They are NOT active in the template to avoid triggering on repos that don't have deployment targets configured.

**Copy them to `.github/workflows/` in your company fork when you're ready to use them.**

| Workflow | Purpose | File |
|----------|---------|------|
| `deploy.yml` | Deployment pipeline with DORA frequency telemetry | [`workflows/deploy.yml`](workflows/deploy.yml) |
| `dora-lead-time.yml` | PR lead time measurement (DORA) | [`workflows/dora-lead-time.yml`](workflows/dora-lead-time.yml) |
| `change-failure-rate.yml` | Deployment failure rate tracking (DORA) | [`workflows/change-failure-rate.yml`](workflows/change-failure-rate.yml) |
| `mttr.yml` | Mean time to recovery tracking (DORA) | [`workflows/mttr.yml`](workflows/mttr.yml) |
| `validate-issue-templates.yml` | Slim CI for a dedicated issue/work repo | [`workflows/validate-issue-templates.yml`](workflows/validate-issue-templates.yml) |
| `sync-issue-form-labels.yml` | Optional automation to translate issue-form answers into labels | [`workflows/sync-issue-form-labels.yml`](workflows/sync-issue-form-labels.yml) |

---

## 4. GitHub Settings

See [`required-github-settings.md`](../required-github-settings.md) for branch protection, CODEOWNERS, and required status checks.

For the fastest clean setup path, use [`setup-checklist.md`](setup-checklist.md).

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
