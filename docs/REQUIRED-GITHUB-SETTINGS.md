# Required GitHub Settings (Governance Enforcement)

This framework assumes **GitHub enforces governance**. The repository can document roles (via `CODEOWNERS`) and quality gates (via Actions), but **only GitHub branch protection** makes these rules binding.

Use this checklist when you fork/customize the framework.

---

## 1) Enable Issues (recommended)

Repo → **Settings → General → Features**
- ✅ Issues

---

## 2) Protect the default branch (`main`)

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

## 3) CODEOWNERS must exist and be meaningful

- Keep `CODEOWNERS` current.
- Treat it as **executable RACI**: sensitive paths (policies, operating model, agent instructions) must have explicit owners.

---

## 4) Required checks: keep the gate list small and non-controversial

Start with the repo’s built-in validation workflow:
- YAML parse checks
- Markdown internal link checks
- Structure checks
- Versioning/metadata checks

Then add stronger gates (security scans, policy-as-code) as you adopt them.

---

## 5) Operating model note

The model’s rule of thumb:
- **PRs = decisions**
- **CODEOWNERS = RACI**
- **CI = quality gates**

Without branch protection, these become advisory.
