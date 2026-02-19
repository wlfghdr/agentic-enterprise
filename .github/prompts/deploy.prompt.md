---
name: deploy
description: Release template or framework file changes — commit with a meaningful message, push to remote, and verify all GitHub Actions CI checks are green before considering done
agent: agent
tools: []
---

You are executing the template release workflow for the agentic-enterprise repository.

## Step 0 — Scope check

Confirm the changed files are **template or framework files** (not instances):

- `_TEMPLATE-*.md` files anywhere in `org/`
- `AGENT.md` files at each layer (`org/*/AGENT.md`)
- `AGENTS.md` / `CLAUDE.md`
- Quality policies in `org/4-quality/policies/`
- `CONFIG.yaml`, `OPERATING-MODEL.md`, integration definitions in `org/integrations/`


---

## Step 1 — Verify version and date fields

List all changed files (`git diff --stat`). For each, confirm version/date fields are updated:

| File type | What to update |
|---|---|
| `AGENT.md` files | `Version` (minor or major bump) + `Last updated` date |
| `_TEMPLATE-*.md` files | `Template version` + `Last updated` date + new row in `## Changelog` |
| Quality policies | `Version` + `Last updated` date |
| `CONFIG.yaml` | `framework_version` |
| `AGENTS.md` / `CLAUDE.md` | `Last updated` date (if field present) |

Fix any missing fields before continuing.

---

## Step 2 — Add changelog entry

For each changed file:
- File has `## Changelog` section → add row: `| <date> | <version> | <what changed and why> |`
- File has no changelog → add entry to root `CHANGELOG.md`

Entry must explain **what** changed and **why**.

---

## Step 3 — Commit

Stage only the files you intentionally changed. Do not use `git add -A` or `git add .`.

```
<type>: <short summary (≤72 chars)>

<body: what problem this solves / what decision was made>
```

Types: `feat` · `fix` · `docs` · `refactor`

---

## Step 4 — Push

```bash
git push
```

Confirm the push succeeded. Set upstream if needed: `git push -u origin <branch>`.

---

## Step 5 — Watch CI and verify green

```bash
gh run list --limit 3
gh run view <run-id>
```

**All checks green → done.**

**Any check red:** read `gh run view <run-id> --log-failed`, fix the root cause, commit the fix (return to Step 3), re-push, re-verify. Do **not** mark done while any check is red.
