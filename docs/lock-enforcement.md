# Lock Enforcement CI Gate

> **Version:** 1.1 | **Last updated:** 2026-02-25

## Overview

A CI job (`validate-locks`) can block PRs that modify **protected paths** without a corresponding active lock file in `work/locks/`.

> **Template vs. Instance:** Lock enforcement CI is **disabled by default** in the upstream template repository — template development doesn't need concurrency locks. When you deploy this framework as a company instance, **uncomment the `validate-locks` job** in `.github/workflows/validate.yml` to activate enforcement. Everything else (scripts, lock files, `locks.yaml`) ships ready to use.

## How It Works

1. The job diffs the PR against the base branch to find changed files.
2. Each changed file is matched against glob patterns in **`locks.yaml`** (repo root).
3. If a file matches a protected pattern, the job checks `work/locks/*.md` for an active (non-expired) lock whose **Target** covers the file.
4. If no lock is found, the job fails with an actionable error message.

## Protected Paths (default)

Defined in `locks.yaml`:

| Pattern | What it protects |
|---|---|
| `COMPANY.md` | Company identity |
| `OPERATING-MODEL.md` | Operating model |
| `AGENTS.md` | Agent framework |
| `CONFIG.yaml` | Global configuration |
| `org/4-quality/policies/*.md` | Quality policies |
| `**/[_]TEMPLATE-*.md` | Global templates |
| `locks.yaml` | The lock config itself |

To add a new protected path, edit `locks.yaml` and open a PR (which itself requires a lock on `locks.yaml`).

## Creating a Lock

1. Copy `work/locks/_TEMPLATE-lock.md` to `work/locks/<lock-id>.md`
2. Fill in **Target**, **Owner**, **Reason**, **Expires**
3. The **Target** field must be an exact path or glob matching the file(s) you plan to change
4. Merge the lock (or include it in the first commit of your PR)

See `work/locks/README.md` for the full protocol.

## Exceptions

Add `ci:lock-exempt` anywhere in a commit message to bypass enforcement for that PR. Use sparingly — this is for emergencies.

## Extending

- Edit `locks.yaml` to add/remove protected patterns
- The script (`scripts/check_locks.py`) uses only Python stdlib — no extra dependencies

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-02-25 | Clarified lock enforcement as an instance concern; CI job disabled by default in the upstream template, with instructions to enable |
| 1.0 | 2025-07-22 | Initial CI gate |
