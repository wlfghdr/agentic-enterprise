# Policy-as-Code (OPA/Rego + Conftest)

Policy-as-Code (PaC) turns governance rules into machine-readable, version-controlled
checks that run automatically in CI. This framework uses [Conftest](https://www.conftest.dev/)
with [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) Rego policies to enforce
repo-level standards on every pull request.

The template uses OPA for **structured invariants**: workflow YAML, `CONFIG.yaml`,
and other machine-readable governance surfaces. Markdown-heavy semantics, Git-diff-aware
version checks, placeholder scanning, and content-security heuristics stay in the
dedicated Python validators where that logic is easier to express and review.

---

## Table of Contents

1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Running Locally](#running-locally)
4. [Current Policies](#current-policies)
5. [What Belongs In OPA](#what-belongs-in-opa)
6. [Adding a New Policy](#adding-a-new-policy)
7. [Approving an Exception - Waiver](#approving-an-exception---waiver)
8. [CI Integration](#ci-integration)
9. [Extending to Other Targets](#extending-to-other-targets)

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
  config/
    framework_governance.rego   # Enforce template config invariants
    observability_registry.rego # Enforce observability registry structure
  workflows/
    permissions.rego      # Enforce top-level permissions on workflow files
    pinned_actions.rego   # Enforce pinned action refs (no @main/@latest)
  exceptions.yaml         # Approved waivers / allowlist

conftest.toml             # Conftest configuration (points at policy/)
docs/policy-as-code.md    # This file
.github/workflows/
  validate.yml            # CI job that runs conftest (conftest job)
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

### Run workflow policies

```bash
conftest test .github/workflows/ \
  --policy policy/ \
  --data policy/ \
  --namespace workflows \
  --output table
```

### Run config policies

```bash
conftest test CONFIG.yaml \
  --policy policy/ \
  --data policy/ \
  --namespace config \
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

### `config/framework_governance` — Template config governance invariants

**File:** `policy/config/framework_governance.rego`
**Severity:** Blocking (deny)

These rules enforce template-level invariants that should hold across both the
public framework and downstream forks:

- `framework_version` must use semantic versioning
- `work_backend.type` must be one of the supported backend modes
- governance-critical artifact overrides such as `technical-design` and
  `governance-exception` must stay in Git

This is a good OPA target because the logic is structural and expressed entirely
against `CONFIG.yaml`.

### `config/observability_registry` — Observability registry structure

**File:** `policy/config/observability_registry.rego`
**Severity:** Blocking (deny)

These rules enforce the minimum structure of the observability integration registry:

- at least one observability integration entry exists
- IDs are unique
- connection type is supported
- OpenTelemetry-backed entries declare the core capabilities needed by the framework

This keeps the template's "observability is mandatory" stance grounded in a
machine-checked registry shape without pretending that runtime evidence can be
verified from static YAML alone.

---

## What Belongs In OPA

OPA is strongest when the input is structured and the rule is deterministic.

**Good OPA candidates**

- Enumerations and required fields in `CONFIG.yaml`
- Cross-field invariants in YAML or JSON
- Workflow permission, action pinning, and structural CI hardening
- Exception-list shape and expiry metadata in machine-readable files

**Keep in dedicated scripts instead**

- Markdown link integrity and prose cross-references
- Version bumps that depend on Git diffs
- Placeholder scanning across mixed template/doc files
- Content-security heuristics, prompt-injection patterns, and other fuzzy checks

The practical rule: keep the Markdown policy docs as the normative source, then
move the **structured subset** of those rules into Rego where CI can enforce them.

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

## Approving an Exception - Waiver

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

The policy checks run as the `conftest` job in `.github/workflows/validate.yml` on every push to `main`
and every pull request. The job is **blocking** — CI fails if any `deny` rule fires.

The template currently runs Conftest against:

- `.github/workflows/` with namespace `workflows`
- `CONFIG.yaml` with namespace `config`

To see which files triggered a violation, check the CI step output. The `table`
output format lists each file, the rule that fired, and the denial message.

---

## Extending to Other Targets

Conftest can parse and check any structured file format (YAML, JSON, TOML, HCL, …).
To add checks for a new target:

1. Create a new package (e.g., `package config`) in `policy/config/`.
2. Add a new `conftest test` invocation in the `conftest` job in `.github/workflows/validate.yml`:

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
