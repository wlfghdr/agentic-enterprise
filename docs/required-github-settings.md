# Required GitHub Settings (Governance Enforcement)

This framework assumes **GitHub enforces governance**. The repository can document roles (via `CODEOWNERS`) and quality gates (via Actions), but **only GitHub branch protection** makes these rules binding.

> **Applies to:** Both the OSS template repo and company forks.
> For the OSS template repo: these settings are what the public repo itself should have configured.
> For your company fork: these settings are what **your fork must configure** before agents operate in it.
> Either way, do this before going live — without branch protection, PRs are advisory, not binding.

Use this checklist when you fork/customize the framework.

---

## 1) Enable Issues

Repo → **Settings → General → Features**
- ✅ Issues

> **Company fork note:** If `CONFIG.yaml → work_backend.type` is `github-issues`, this is required, not optional. If you stay on `git-files`, Issues can remain disabled for internal operations.

---

## 2) If using the issue backend, enable issue forms and labels before going live

Repo → **Settings → General → Features**
- ✅ Issues
- ✅ Issue forms

Prefer the scripted install path from `scripts/instantiate_instance.py install-github-work-repo`.
If you need the manual path, copy the sample files from `docs/github/issue-templates/` into `.github/ISSUE_TEMPLATE/` in your instance repository and customize them.
Use `docs/github/labels/labels.sample.yml` for label bootstrap and `docs/github/setup-checklist.md` for the full GitHub issue-backend setup sequence.

Minimum required label families for a usable GitHub issue backend:
- `artifact:` labels for each issue-backed artifact type
- A GitHub Project (v2) with a **Status** field for state transitions
- `layer:` labels for ownership
- `loop:` labels for lifecycle stage
- `priority:` labels for triage

Use [docs/github-issues.md](github-issues.md) for the exact label set, human approval transitions, and setup checklist.

---

## 3) Protect the default branch (`main`)

Repo → **Settings → Branches → Branch protection rules**

Recommended minimum rule for `main`:

### Required
- ✅ **Require a pull request before merging**
- ✅ **Require approvals** (recommend: 1–2)
- ✅ **Require review from Code Owners**
- ✅ **Require status checks to pass before merging**
  - Select the workflow checks from `.github/workflows/validate.yml` (e.g., "Validate Framework")
- ✅ **Require branches to be up to date before merging** (optional but recommended)

### Strongly recommended
- ✅ **Restrict who can push to matching branches** (admins/maintainers only)
- ✅ **Do not allow bypassing the above settings** (or restrict bypass to a very small set)

### Optional hardening
- ✅ Require signed commits
- ✅ Require linear history
- ✅ Require conversation resolution

---


## 3b) PR governance defaults

For repos where agents are expected to operate continuously:

- enable GitHub Auto-merge if your plan supports it
- require PR-based changes to protected branches
- treat issue-linking as a governed requirement, not a nice-to-have
- treat PR assignees and reviewer requests as required operating metadata, not optional hygiene

Minimum PR discipline:
- every open PR has a named assignee who owns the next step
- every PR that needs human approval has explicit reviewer request(s)
- the PR body tells reviewers what to focus on and what actions they can take
- PRs waiting on a human should be visible in that human's queue via review requests and/or assignee handoff

PR descriptions should use real closing keywords when work is meant to auto-close issues:
- `closes #123`
- `fixes owner/repo#123`
- `resolves owner/repo#123`

`Addresses` is useful as context, but it is not sufficient for automatic closure.

## 4) CODEOWNERS must exist and be meaningful

- Keep `CODEOWNERS` current.
- Treat it as **executable RACI**: sensitive paths (policies, operating model, agent instructions) must have explicit owners.

---

## 5) Required checks: keep the gate list small and non-controversial

Start with the repo’s built-in validation workflow:
- YAML parse checks
- Markdown internal link checks
- Structure checks
- Versioning/metadata checks

Then add stronger gates (security scans, policy-as-code) as you adopt them.

If you split work into a **dedicated GitHub issue repo**:

- keep the full validation/security gates on the main operating-model repo
- use only slim checks on the work repo for the files that repo actually stores (for example issue-template YAML)
- do not require framework checks on the work repo if it does not contain the framework files those checks validate

The template includes a reference workflow for this pattern at `docs/github/workflows/validate-issue-templates.yml`, and the scripted installer can copy it into the work repo for you.

---

## 6) Operating model note

The model’s rule of thumb:
- **PRs = decisions**
- **CODEOWNERS = RACI**
- **CI = quality gates**

Without branch protection, these become advisory.

If you use the issue backend, add one more operating rule for humans:
- **Approval = explicit Project Status transition by an authorized human**

Examples:
- Mission approval: set Project Status from `Backlog` to `Approved`
- Release approval: set Project Status from `Backlog` to `Approved`
- Signal triage: set Project Status from `Backlog`/`Triage` to `Approved`, `Done`, etc.
