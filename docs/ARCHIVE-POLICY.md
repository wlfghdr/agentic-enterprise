# Archive Policy (Work Artifact Lifecycle)

All `work/` directories follow the same lifecycle: **active → done → archived**.

Archiving keeps active directories clean and scannable while preserving full history in git.

## Archive Mechanics

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

## When to Archive

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

## How to Archive

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

## Rules

1. **Never delete** work artifacts from the repo — always archive (git history = audit trail)
2. **Archive entire mission folders** (not individual files inside a mission)
3. **Templates** (`_TEMPLATE-*`) are never archived
4. **Active/parked items** stay in place — only done/closed/completed items move
5. **README.md** files in each directory stay (never archived)
6. **Agents ignore `archive/`** — when scanning active work, skip the archive subfolder

## Agent Integration

This policy is referenced in AGENTS.md Rule 14. All agents should:
- Archive items they close (in the same commit/PR)
- Orchestration agents: periodically scan for archivable items
- Never scan `archive/` subfolders when looking for active work
