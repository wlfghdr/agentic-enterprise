# Policy-as-Code (OPA/Rego + Conftest)

Policy-as-Code (PaC) turns governance rules into machine-readable, version-controlled
checks that run automatically in CI. This framework uses [Conftest](https://www.conftest.dev/)
with [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) Rego policies to enforce
repo-level standards on every pull request.

---

## Table of Contents

1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Running Locally](#running-locally)
4. [Current Policies](#current-policies)
5. [Adding a New Policy](#adding-a-new-policy)
6. [Approving an Exception / Waiver](#approving-an-exception--waiver)
7. [CI Integration](#ci-integration)
8. [Extending to Other Targets](#extending-to-other-targets)

---

## Overview

| Tool       | Role                                                              |
|------------|-------------------------------------------------------------------|
| OPA        | Open Policy Agent — evaluates Rego rules against structured data  |
| Rego       | Policy language used to write rules                               |
| Conftest   | CLI that parses files (YAML, JSON, …) and runs Rego against them  |

Policies are **blocking by default**: a `deny` rule causes a CI failure. Use `warn`
rules for advisory signals that don't block merges.

---

## Folder Structure

```
policy/
  workflows/
    permissions.rego      # Enforce top-level permissions on workflow files
    pinned_actions.rego   # Enforce pinned action refs (no @main/@latest)
  exceptions.yaml         # Approved waivers / allowlist

conftest.toml             # Conftest configuration (points at policy/)
docs/POLICY-AS-CODE.md    # This file
.github/workflows/
  policy.yml              # CI job that runs conftest
```

---

## Running Locally

### Prerequisites

Install Conftest (macOS/Linux):

```bash
# macOS
brew install conftest

# Linux (manual)
VERSION=0.51.0
curl -sL "https://github.com/open-policy-agent/conftest/releases/download/v${VERSION}/conftest_${VERSION}_Linux_x86_64.tar.gz" \
  | tar xz conftest
sudo mv conftest /usr/local/bin/
```

### Run all workflow policies

```bash
conftest test .github/workflows/ \
  --policy policy/ \
  --data policy/ \
  --namespace workflows \
  --output table
```

### Run against a single file

```bash
conftest test .github/workflows/validate.yml \
  --policy policy/ \
  --data policy/ \
  --namespace workflows
```

### Check output format options

```bash
conftest test ... --output [table|json|tap|github]
```

Use `--output github` in CI for native GitHub Actions annotations.

---

## Current Policies

### `workflows/permissions` — Top-level permissions block required

**File:** `policy/workflows/permissions.rego`
**Severity:** Blocking (deny)

All GitHub Actions workflow files must declare a top-level `permissions` block.
This limits what the `GITHUB_TOKEN` can do, reducing blast radius from a compromised
step or dependency.

```yaml
# Good
permissions:
  contents: read

# Also good (explicitly no permissions)
permissions: {}
```

### `workflows/pinned_actions` — External actions must be pinned

**File:** `policy/workflows/pinned_actions.rego`
**Severity:** Blocking (deny)

External action references must be pinned to a specific version tag or commit SHA.
Floating refs (`@main`, `@master`, `@latest`) allow arbitrary code changes to be
silently pulled into CI — a supply-chain attack vector.

```yaml
# Good
- uses: actions/checkout@v4
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683

# Bad — will fail the check
- uses: myorg/myaction@main
- uses: myorg/myaction@latest
```

Local composite actions (`uses: ./...`) are exempt.

---

## Adding a New Policy

1. **Create a `.rego` file** in the appropriate subdirectory under `policy/`:

   ```
   policy/workflows/my_rule.rego    # for workflow checks
   policy/config/my_rule.rego       # for config file checks (future)
   ```

2. **Use the correct package name** matching the namespace for the target:

   ```rego
   package workflows   # for .github/workflows/*.yml

   import rego.v1

   deny contains msg if {
       # your condition here
       msg := "Human-readable violation message"
   }

   # Advisory-only (non-blocking):
   warn contains msg if {
       # your condition here
       msg := "Advisory: ..."
   }
   ```

3. **Test locally** before opening a PR:

   ```bash
   conftest test .github/workflows/ \
     --policy policy/ --data policy/ --namespace workflows
   ```

4. **Add a comment block** at the top of the file explaining:
   - What the policy enforces
   - Why it matters (rationale)
   - How to add an exception

### Policy guidelines

- Prefer `deny` for clear security or correctness violations.
- Use `warn` for style, best-practices, or advisory checks.
- Keep rules small and focused — one concern per file.
- Reference the relevant standard or doc link in the comment header.
- Load exceptions via `data.exceptions.*` (see below).

---

## Approving an Exception / Waiver

Sometimes a legitimate use case conflicts with a policy. The process:

1. **Edit `policy/exceptions.yaml`** and add the exception under the appropriate key.
2. **Document the exception inline** with `reason`, `approved-by`, and `expires` fields.
3. **Open a PR** — the exception entry is itself reviewed and version-controlled.
4. **Revisit before the expiry date** and remove the exception if no longer needed.

```yaml
# policy/exceptions.yaml

workflows:
  allow_missing_permissions:
    - "Legacy Workflow"  # reason: pre-dates PaC, approved: 2025-01-15, expires: 2025-06-01

  allow_unpinned_actions:
    - "myorg/internal-action@main"  # reason: internal repo, approved: 2025-02-01, expires: 2025-08-01
```

Exceptions without documented reasons will be rejected in code review.

---

## CI Integration

The policy checks run in `.github/workflows/policy.yml` on every push to `main`
and every pull request. The job is **blocking** — CI fails if any `deny` rule fires.

To see which files triggered a violation, check the CI step output. The `table`
output format lists each file, the rule that fired, and the denial message.

---

## Extending to Other Targets

Conftest can parse and check any structured file format (YAML, JSON, TOML, HCL, …).
To add checks for a new target:

1. Create a new package (e.g., `package config`) in `policy/config/`.
2. Add a new `conftest test` invocation in `.github/workflows/policy.yml`:

   ```yaml
   - name: Check config policies
     run: |
       conftest test CONFIG.yaml \
         --policy policy/ \
         --data policy/ \
         --namespace config
   ```

3. Write Rego rules that reference `input` (the parsed file content).

---

*See [Conftest docs](https://www.conftest.dev/) and [OPA docs](https://www.openpolicyagent.org/docs/latest/) for further reference.*
