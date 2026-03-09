# Archive Policy (Work Artifact Lifecycle)

> **Version:** 1.1 | **Last updated:** 2026-03-07

All work artifacts follow the same lifecycle: **active → done → archived**.

Archiving keeps active views clean and scannable while preserving full history. The mechanics depend on your configured work backend (see `CONFIG.yaml → work_backend` and [WORK-BACKENDS.md](WORK-BACKENDS.md)).

---

## Git-Files Backend

### Archive Mechanics

Every `work/<area>/` directory may contain an `archive/` subfolder. When items reach a terminal state, they move there.

```
work/
  signals/
    archive/          ← closed/actioned signals
  signals/triage/
    archive/          ← triage records for archived signals
  missions/
    archive/          ← closed/completed/consolidated missions (entire folder)
  reports/
    archive/          ← old daily/weekly reports
  research/
    archive/          ← superseded research digests
  retrospectives/
    archive/          ← past retros (keep recent 2)
  decisions/
    archive/          ← implemented/superseded decisions
  designs/
    archive/          ← superseded design docs
```

### When to Archive

| Area | Archive trigger |
|------|----------------|
| **signals** | Signal status = `done` or `upstream-issued` + action confirmed |
| **signals/triage** | Corresponding signal archived |
| **missions** | STATUS.md says `closed`, `completed`, or `consolidated` |
| **reports** | Older than 30 days (configurable) |
| **research** | Digest superseded by newer cycle |
| **retrospectives** | Keep only most recent 2 |
| **decisions** | Decision implemented + referenced in mission/PR |
| **designs** | Design superseded by newer version or implementation complete |

### How to Archive

**Option A: git mv** (preferred — preserves blame)
```bash
git mv work/signals/my-signal.md work/signals/archive/
git mv work/missions/old-mission/ work/missions/archive/
```

**Option B: automation script** (if provided by your instance)
```bash
./scripts/archive_work.sh          # archives all eligible items
./scripts/archive_work.sh --dry-run  # preview only
```

### Rules

1. **Never delete** work artifacts from the repo — always archive (git history = audit trail)
2. **Archive entire mission folders** (not individual files inside a mission)
3. **Templates** (`_TEMPLATE-*`) are never archived
4. **Active/parked items** stay in place — only done/closed/completed items move
5. **README.md** files in each directory stay (never archived)
6. **Agents ignore `archive/`** — when scanning active work, skip the archive subfolder

---

## Issue Backend (GitHub Issues)

When `work_backend.type` is `"github-issues"`, archiving is equivalent to **closing** issues. Closed issues remain searchable and serve as the historical record — no data is lost.

### When to Close

The same triggers from the git-files table apply. When an artifact reaches a terminal state, close its corresponding issue.

### How to Close

1. **Set project status to `Done`** before closing — this enables filtering and reporting
2. **Add a closing comment** summarizing the outcome or linking to the follow-up work
3. **Close the issue** (not delete) — use close reason `completed` or `not planned` as appropriate

For missions tracked as issue hierarchies:
- Close child task issues first
- Close the parent mission issue last
- The parent issue's closing comment should summarize the mission outcome

### Rules

1. **Never delete** issues — close them with a resolution note
2. **Always set project status to `Done` before closing** (enables filtering and reporting)
3. **Closed issues remain searchable** — they are the audit trail equivalent of `archive/` subfolders
4. **Templates** (issues with `template:*` labels, if any) are not closed
5. **Agents filter by open status** — when scanning active work, query only open issues

---

## Agent Integration

This policy is referenced in AGENTS.md Rule 14. All agents should:

**Git-files backend:**
- Archive items they close (in the same commit/PR)
- Orchestration agents: periodically scan for archivable items
- Never scan `archive/` subfolders when looking for active work

**Issue backend:**
- Close issues they complete (apply final status label + closing comment)
- Orchestration agents: periodically scan for closable issues
- Filter by open status when looking for active work
