# Security Scanning
<!-- placeholder-ok -->

This document describes the security tooling integrated into CI, how to run
scans locally, and how to handle findings — including the allowlist strategy
for unavoidable false positives.

**Policy reference:** [`org/4-quality/policies/security.md`](../org/4-quality/policies/security.md)

---

## Overview

Two scans run on every PR targeting `main` (and on pushes to `main`):

| Scan | Tool | Trigger | Blocking? |
|------|------|---------|-----------|
| Secret scanning | [Gitleaks](https://github.com/gitleaks/gitleaks) | push + PR | **Yes** — any finding fails CI |
| Dependency vulnerability scan | [GitHub Dependency Review](https://github.com/actions/dependency-review-action) | PR only | **Yes** — HIGH/CRITICAL CVEs fail CI |

---

## Running Locally

### Secret Scanning (Gitleaks)

**Install:**

```bash
# macOS
brew install gitleaks

# Linux (GitHub Releases)
VERSION=v8.21.2
curl -sSL "https://github.com/gitleaks/gitleaks/releases/download/${VERSION}/gitleaks_${VERSION#v}_linux_x64.tar.gz" | tar xz -C /usr/local/bin gitleaks
```

**Scan uncommitted changes:**

```bash
gitleaks detect --config .gitleaks.toml --source . -v
```

**Scan full git history (recommended before first push):**

```bash
gitleaks detect --config .gitleaks.toml --source . --log-opts="--all" -v
```

**Scan a specific commit range (e.g., a branch):**

```bash
gitleaks detect --config .gitleaks.toml --source . \
  --log-opts="origin/main..HEAD" -v
```

Results are printed to stdout. Exit code `1` = findings found, `0` = clean.

---

### Dependency Vulnerability Scanning

The GitHub Dependency Review Action runs only in CI because it compares the
dependency graph delta between the base and head of a PR via the GitHub API.

For local dependency scanning (if you add a package manifest in the future):

```bash
# Install osv-scanner
go install github.com/google/osv-scanner/cmd/osv-scanner@latest

# Scan current directory
osv-scanner -r .

# Scan a specific lockfile
osv-scanner --lockfile=requirements.txt
```

> **Note:** This repository currently has no package manifests (it is a
> Markdown/YAML framework). The Dependency Review step will pass silently
> until dependency files are added.

---

## Handling Findings

### Gitleaks — Secret Findings

1. **Is it a real secret?**
   - If yes: rotate the credential immediately. Remove it from history using
     `git filter-repo` or `BFG Repo Cleaner`. Contact the security team.
   - If no (false positive): follow the allowlist procedure below.

2. **Blocking CI with a false positive?**
   - You can use `# gitleaks:allow` as an inline comment on the line in
     question (for code files) to suppress a single-line finding without
     editing `.gitleaks.toml`:
     ```yaml
     example_token: "AAAA1234"  # gitleaks:allow
     ```
   - For broader suppression (entire file, path pattern, or commit), add an
     entry to `.gitleaks.toml` — see the [Allowlist Strategy](#allowlist-strategy)
     section below.

### Dependency Review — CVE Findings

1. **HIGH or CRITICAL CVE introduced in the PR (CI blocks):**
   - Update or replace the vulnerable dependency.
   - If the dependency cannot be updated (transitive, pinned), open a risk
     acceptance issue and add the GHSA ID to the `allow-ghsas` list in
     `.github/workflows/security.yml` with a comment linking the issue.

2. **MODERATE or LOW CVE (warning only, CI does not block):**
   - Document the risk in the PR description or a linked issue.
   - Schedule a follow-up patch in the next sprint.

---

## Allowlist Strategy

### Principle: narrow scope, documented reason

All allowlist entries must:
1. Be as narrow as possible (prefer per-path or per-regex over skip-commit).
2. Include a comment explaining _why_ the finding is safe to ignore.
3. Be reviewed during quarterly security audits.

### Gitleaks allowlist (`.gitleaks.toml`)

```toml
[allowlist]
  description = "Allowlisted patterns"

  # Path-based: ignore secrets in documentation examples
  paths = [
    '''(?i)examples/.*''',
    '''(?i)_TEMPLATE-.*\.md''',
  ]

  # Regex-based: ignore placeholder patterns like {{API_KEY}}
  regexes = [
    '''(?i)\{\{[A-Z_]+\}\}''',
  ]

  # Commit-based: skip a specific commit that cannot be rewritten
  commits = [
    "abc123def456",  # reason: example credentials in bootstrap commit, not real
  ]
```

Edit `.gitleaks.toml` in the repository root, commit, and push. CI will
pick up the updated allowlist immediately.

### Dependency Review allowlist (`.github/workflows/security.yml`)

Add accepted GHSA IDs to the `allow-ghsas` parameter:

```yaml
- name: Dependency Review
  uses: actions/dependency-review-action@v4
  with:
    fail-on-severity: high
    allow-ghsas: "GHSA-xxxx-yyyy-zzzz"  # link to risk acceptance issue #NNN
```

---

## Policy Alignment

| Policy requirement | Implementation |
|---|---|
| No secrets in source code | Gitleaks blocks any push/PR containing a detected secret |
| Dependencies scanned for known vulnerabilities | Dependency Review blocks PRs introducing HIGH/CRITICAL CVEs |
| No critical or high vulnerabilities in production dependencies | `fail-on-severity: high` in Dependency Review |
| Dependency update cadence | Dependabot or manual triage; risk-accepted findings tracked in issues |

---

## Related Files

- `.gitleaks.toml` — Gitleaks configuration and allowlist
- `.github/workflows/security.yml` — CI workflow definition
- `org/4-quality/policies/security.md` — Security policy (authoritative)
- `SECURITY.md` — Vulnerability reporting instructions
