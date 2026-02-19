---
name: deploy
description: Release template or framework file changes — commit with a meaningful message, push to remote, and verify all GitHub Actions CI checks are green before considering done
argument-hint: "[optional: description of what changed]"
disable-model-invocation: true
allowed-tools: Bash(git *), Bash(gh *)
---

You are executing the template release workflow for the agentic-enterprise repository.

$ARGUMENTS

## Step 0 — Scope check

Confirm the changed files are **template or framework files** (not instances):

- `_TEMPLATE-*.md` files anywhere in `org/`
- `AGENT.md` files at each layer (`org/*/AGENT.md`)
- `AGENTS.md` / `CLAUDE.md`
- Quality policies in `org/4-quality/policies/`
- `CONFIG.yaml`, `OPERATING-MODEL.md`, integration definitions in `org/integrations/`


---

## Step 1 — Verify version and date fields

Run `git diff --stat` to list all changed files.

For each changed file, confirm its version/date fields are updated per Rule 10 in `AGENTS.md`:

| File type | What to update |
|---|---|
| `AGENT.md` files | `Version` (minor or major bump) + `Last updated` date |
| `_TEMPLATE-*.md` files | `Template version` + `Last updated` date + new row in `## Changelog` |
| Quality policies | `Version` + `Last updated` date |
| `CONFIG.yaml` | `framework_version` |
| `AGENTS.md` / `CLAUDE.md` | `Last updated` date (if field present) |

Fix any missing fields before proceeding.

---

## Step 2 — Add changelog entry

For each changed file:
- If the file has a `## Changelog` section → add a row: `| <date> | <version> | <what changed and why> |`
- If not → add an entry to root `CHANGELOG.md` under the correct version section

The entry must explain **what** changed and **why** — not just "updated file".

---

## Step 3 — Commit

Stage only the files you intentionally changed — do not use `git add -A` or `git add .` blindly.

Commit message format:
```
<type>: <short summary (≤72 chars)>

<body: what problem does this solve / what decision was made>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Allowed types: `feat` (new content), `fix` (correction), `docs` (prose only), `refactor` (restructure without meaning change).

Confirm the commit was created successfully.

---

## Step 4 — Push

```bash
git push
```

If the branch has no upstream yet: `git push -u origin <branch>`.

Confirm the push succeeded.

---

## Step 5 — Watch CI

```bash
gh run list --limit 3
```

Wait for all checks to complete, then inspect:

```bash
gh run view <run-id>
```

**All checks green → done.** Report success with the run URL.

**Any check red:**
1. Read the failure log: `gh run view <run-id> --log-failed`
2. Diagnose the root cause — read the actual output, do not guess
3. Fix the issue; if the fix touches governed files, update their version/date fields
4. Return to Step 3 and repeat
5. Do **not** mark the task complete while any check is red
