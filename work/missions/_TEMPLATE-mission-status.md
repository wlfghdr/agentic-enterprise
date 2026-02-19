# Mission Status: [Mission Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Mission:** [link to `work/missions/<name>/BRIEF.md`]  
> **Fleet Config:** [link to `org/2-orchestration/fleet-configs/<config>.md`]  
> **Author:** [Orchestration Layer — Agent Fleet Manager]  
> **Storage:** `work/missions/<mission-name>/STATUS.md` (append-only, latest entry first)

---

<!-- 
  INSTRUCTIONS: Add new status entries at the TOP of this file (below this comment).
  Each entry is a snapshot of mission progress at a point in time.
  Never delete or modify previous entries — this file is an append-only log.
-->

## Status Update: YYYY-MM-DD

**Overall status:** on-track | at-risk | blocked | ahead  
**Mission phase:** proposed | approved | active | paused | completing  
**Reporting period:** YYYY-MM-DD → YYYY-MM-DD

### Stream Progress

| Stream | Division | Status | Progress | Notes |
|--------|----------|--------|----------|-------|
| [Stream 1 from fleet config] | [division] | active / completed / blocked | [% or checklist summary] | [brief note] |
| [Stream 2] | [division] | active / completed / blocked | [% or checklist summary] | [brief note] |

### Blockers

| Blocker | Severity | Blocking Stream(s) | Escalated To | Status |
|---------|----------|-------------------|-------------|--------|
| [Description] | critical / major / minor | [stream name(s)] | [human role] | open / resolving / resolved |

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [Description] | high / medium / low | high / medium / low | [planned mitigation] |

### Key Decisions Made This Period

| Decision | Date | Decided By | Link |
|----------|------|-----------|------|
| [Decision summary] | YYYY-MM-DD | [who] | [link to decision record, if any] |

### Next Milestones

| Milestone | Target Date | Status |
|-----------|------------|--------|
| [Next milestone] | YYYY-MM-DD | on-track / at-risk |

### Fleet Performance (This Period)

| Metric | Value |
|--------|-------|
| PRs generated | [count] |
| PRs merged | [count] |
| PRs rejected / needs-revision | [count] |
| Quality eval pass rate | [%] |
| Average cycle time (PR open → merge) | [hours/days] |

---

<!-- Previous status entries appear below, newest first -->
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
