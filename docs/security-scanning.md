# Security Scanning
<!-- placeholder-ok -->

This document describes the security tooling integrated into CI, how to run
scans locally, and how to handle findings — including the allowlist strategy
for unavoidable false positives.

**Policy reference:** [`org/4-quality/policies/security.md`](../org/4-quality/policies/security.md)

---

## Overview

Three scans run on every PR targeting `main` (and on pushes to `main`):

| Scan | Tool | Trigger | Blocking? |
|------|------|---------|-----------|
| Secret scanning | [Gitleaks](https://github.com/gitleaks/gitleaks) | push + PR | **Yes** — any finding fails CI |
| Dependency vulnerability scan | [GitHub Dependency Review](https://github.com/actions/dependency-review-action) | PR only | **Yes** — HIGH/CRITICAL CVEs fail CI |
| Content security scanning | [`validate_content_security.py`](../scripts/validate_content_security.py) | push + PR | **Yes** — error-severity findings fail CI |

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

## Content Security Scanning

The content security scanner detects prompt injection patterns, instruction
override attempts, hierarchy violations, and other content-level security risks
in governed files (agent instructions, policies, work artifacts, templates).

**Policy reference:** [`org/4-quality/policies/agent-security.md` §4.3](../org/4-quality/policies/agent-security.md)

### What it detects

| Pattern ID | Category | Applies to | Description |
|------------|----------|------------|-------------|
| INJ-001–003 | Instruction Override | All governed files | "Ignore previous instructions", system prompt extraction, new instruction injection |
| INJ-004–005 | Role Impersonation | Work artifacts, templates | "You are now a…" role reassignment, privilege escalation phrases |
| HIE-001–002 | Hierarchy Violation | Instructions, work | Lower-level files attempting to override parent rules, Non-Negotiable Rules redefinition |
| CODE-001–002 | Unsafe Code Pattern | Instructions, work, templates | `eval()`/`exec()` in markdown, shell injection risk in code blocks |
| ENC-001 | Encoded Payload | All governed files | Suspicious base64-encoded blocks (>100 chars) in governed files |
| TRUST-001–002 | Trust Boundary | All governed files | Directives to concatenate external content into prompts, skip input validation |
| SOC-001 | Social Engineering | Work artifacts | "Approve immediately", "skip review", urgency manipulation in work artifacts |
| POL-001–002 | Policy Bypass | All governed files / work | Directives to ignore policies, self-authorized governance exceptions |
| CI-001 | Pipeline Integrity | Workflow YAML | `continue-on-error: true` could silently suppress security failures |
| CI-002 | Pipeline Integrity | Workflow YAML | `if: false` permanently disables a workflow job or step |
| CI-003 | Pipeline Integrity | Workflow YAML | Unquoted `${{ github.event.* }}` in `run:` blocks (shell injection) |
| CI-004 | Pipeline Integrity | Workflow YAML | `curl`/`wget` piped to `sh`/`bash` (remote code execution) |
| CI-005 | Pipeline Integrity | Workflow YAML | Comments indicating a validation/security step was disabled or removed |
| REGO-001 | Policy-as-Code Integrity | Rego files | OPA `deny` rule commented out or permanently disabled |

### Running locally

```bash
# Scan the full repository
python3 scripts/validate_content_security.py

# Verbose mode (shows each file)
python3 scripts/validate_content_security.py --verbose

# Scan an alternate root (e.g., examples)
python3 scripts/validate_content_security.py --root examples/e2e-loop
```

### Handling findings

1. **Is it a real injection attempt?**
   - If yes: remove the offending content. Investigate the source (which PR
     introduced it, which agent or human authored it). File a security signal.
   - If no (legitimate reference): add `<!-- content-security:allow -->` as an
     inline HTML comment on the flagged line.

2. **Suppression review:** Suppression markers are visible in PR diffs. Reviewers
   must verify that each suppression is justified — a suppressed injection pattern
   in a work artifact is suspicious; in a security policy document explaining
   what to detect, it is expected.

3. **Adding new patterns:** When new injection vectors are discovered, add them
   to the `PATTERNS` list in `scripts/validate_content_security.py`. This is a
   living regression suite (per agent-security.md §4.2).

---

## Workflow & Pipeline Integrity (Policy-as-Code)

In addition to the content security scanner's CI-* patterns, the
**Conftest/OPA policy layer** (`policy.yml` + Rego rules) enforces structural
security invariants on workflow files:

| Rule | File | What it enforces |
|------|------|-----------------|
| `permissions.rego` | Workflow top-level `permissions` | Prevents over-broad `GITHUB_TOKEN` scope (privilege escalation) |
| `pinned_actions.rego` | External action refs | Blocks floating refs (`@main`, `@latest`) — supply chain protection |
| `security_integrity.rego` | Security job integrity | Blocks `continue-on-error` on security jobs, `if: false` disabling, shell injection via `${{ github.event.* }}`, remote script execution |

The content security scanner and Rego policies are complementary:
- **Content scanner** (Python, `validate.yml`): pattern-matches across all
  governed files including workflows — catches text-level injection
- **Conftest/OPA** (Rego, `validate.yml` conftest job): structurally parses YAML and
  evaluates security invariants — catches semantic workflow tampering

Both must pass for a PR to merge when branch protection is enabled.

---

## Policy Alignment

| Policy requirement | Implementation |
|---|---|
| No secrets in source code | Gitleaks blocks any push/PR containing a detected secret |
| Dependencies scanned for known vulnerabilities | Dependency Review blocks PRs introducing HIGH/CRITICAL CVEs |
| No critical or high vulnerabilities in production dependencies | `fail-on-severity: high` in Dependency Review |
| Dependency update cadence | Dependabot or manual triage; risk-accepted findings tracked in issues |
| No prompt injection patterns in governed files | Content security scanner blocks PRs with error-severity injection findings |
| Agent instruction hierarchy integrity | Content security scanner detects hierarchy override attempts in lower-level files |
| Trust boundary enforcement | Content security scanner detects directives to concatenate untrusted content into prompts |

---

## Related Files

- `.gitleaks.toml` — Gitleaks configuration and allowlist
- `.github/workflows/security.yml` — CI workflow for secret & dependency scanning
- `.github/workflows/validate.yml` — CI workflow for content security scanning (and other validators)
- `scripts/validate_content_security.py` — Content security scanner source
- `org/4-quality/policies/security.md` — Security policy (authoritative)
- `org/4-quality/policies/agent-security.md` — Agent security policy (prompt injection, tool abuse, §4.3 CI enforcement)
- `SECURITY.md` — Vulnerability reporting instructions
