# Tasks: [Mission Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-24
> **Mission:** [link to BRIEF.md]
> **Mission ID:** MISSION-YYYY-NNN
> **Revision:** 1 | **Last updated:** YYYY-MM-DD
> **Author:** Orchestration Layer — Agent Fleet Manager
> **Storage:** `work/missions/<mission-name>/TASKS.md`

<!-- placeholder-ok -->

> **This file is required for missions with `Status: active`.** A mission cannot transition from `planning` to `active` without at least one decomposed task in this file. See [docs/mission-lifecycle.md](../../docs/mission-lifecycle.md) for the full status transition rules.
>
> **Exception:** Missions scoped entirely to Strategy or Steering considerations (no Execution Layer work) may use `Status: active` without a TASKS.md. In that case, document the rationale in the Mission Brief under Scope.

---

## How to Use This File

The **Orchestrator** creates this file by decomposing the Mission Brief and Outcome Contract into concrete, assignable work items. **Execution Agents** pick up tasks from this file, execute them, update their status, and generate asset entries upon completion.

**Task granularity:** Each task should be small enough to be independently deliverable by a single agent or agent pool within one work cycle. If a task requires coordination across multiple divisions, split it into division-aligned subtasks.

**Task assignment criteria:**

- **Division alignment** — the owning division determines which agents are eligible
- **Agent capability matching** — tasks route to agents with the right skills
- **Capacity and parallelization** — independent tasks can run in parallel
- **Dependency ordering** — dependent tasks must declare blockers explicitly

---

## Tasks

### TASK-001: [Task title]

| Field | Value |
|-------|-------|
| **Status** | `pending` / `in-progress` / `completed` / `blocked` / `cancelled` |
| **Assigned to** | [Division] — [Agent type or human role] |
| **Depends on** | None / TASK-NNN |
| **Priority** | critical / high / medium / low |
| **Target date** | YYYY-MM-DD |

**Description:**
[What needs to be done. Be specific enough that the assigned agent can start without further clarification.]

**Acceptance criteria:**
- [ ] [Criterion 1 — measurable or verifiable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Assets generated:**
- [Link to asset registry entry or PR, filled upon completion]

---

### TASK-002: [Task title]

| Field | Value |
|-------|-------|
| **Status** | `pending` / `in-progress` / `completed` / `blocked` / `cancelled` |
| **Assigned to** | [Division] — [Agent type or human role] |
| **Depends on** | TASK-001 |
| **Priority** | critical / high / medium / low |
| **Target date** | YYYY-MM-DD |

**Description:**
[What needs to be done.]

**Acceptance criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Assets generated:**
- [Link to asset registry entry or PR, filled upon completion]

---

## Task Summary

| Task | Title | Division | Status | Depends on | Priority |
|------|-------|----------|--------|------------|----------|
| TASK-001 | [Title] | [Division] | pending | — | high |
| TASK-002 | [Title] | [Division] | pending | TASK-001 | medium |

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial task decomposition |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-24 | Initial version |
