# Mission Brief: [Mission Name]

> **Template version:** 1.1 | **Last updated:** 2026-02-24
> **Mission ID:** MISSION-YYYY-NNN  
> **Status:** proposed | approved | planning | active | paused | completed | cancelled
> **Created:** YYYY-MM-DD  
> **Revision:** 1 | **Last updated:** YYYY-MM-DD
> **Author:** [Strategy Layer agent or human]  
> **Design required:** true | false _(Set to `true` for multi-stream missions, novel architecture patterns, new external APIs, data model changes, or regulated features. The Orchestration Layer will gate execution on a reviewed Technical Design document.)_

---

## Origin

- **Signal(s):** [link to originating signal(s) in `work/signals/`]
- **Strategic alignment:** [which strategic belief(s) does this mission serve?]
- **Sponsor:** [human sponsor name/role]

## Objective

[One paragraph: What does this mission accomplish and why does it matter? Write it so anyone in the company can understand.]

## Scope

### In Scope
- [Specific deliverable or outcome 1]
- [Specific deliverable or outcome 2]
- [Specific deliverable or outcome 3]

### Out of Scope
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

### Constraints
- [Time constraint, if any]
- [Technical constraint, if any]
- [Budget constraint, if any]

## Divisions Involved

| Division | Role | Contribution |
|----------|------|-------------|
| [Division 1] | Primary | [what they deliver] |
| [Division 2] | Supporting | [what they contribute] |

## Outcome Contract

> Reference: `work/missions/<name>/OUTCOME-CONTRACT.md`

| Metric | Target | Measurement Method | Deadline |
|--------|--------|-------------------|----------|
| [Metric 1] | [Target value] | [How measured] | YYYY-MM-DD |
| [Metric 2] | [Target value] | [How measured] | YYYY-MM-DD |

## Human Checkpoints

These moments require human review and approval:

1. **[Checkpoint name]** — [trigger condition] → [who reviews]
2. **[Checkpoint name]** — [trigger condition] → [who reviews]

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk 1] | high/med/low | high/med/low | [Mitigation strategy] |

## Estimated Effort

- **Size:** small (< 2 weeks) | medium (2-6 weeks) | large (6+ weeks)
- **Agent fleet size:** [estimated number of concurrent agent streams]
- **Human touchpoints:** [estimated number of human reviews needed]

## Status Transition Rules

Missions follow a governed lifecycle. Each transition has a gate that must be satisfied before the status can change. See [docs/mission-lifecycle.md](../../docs/mission-lifecycle.md) for the full lifecycle guide.

| From | To | Gate |
|------|----|------|
| `proposed` | `approved` | Strategy Layer human approves the Mission Brief via PR merge |
| `approved` | `planning` | Orchestrator creates Fleet Config; Technical Design started (if `design-required: true`) |
| `planning` | `active` | **TASKS.md must exist with at least one task** (unless mission has no Execution Layer scope — see exception below). Technical Design approved (if required). |
| `active` | `paused` | Human decision (resource conflict, external dependency, reprioritization) |
| `paused` | `active` | Human decision; original gate conditions still satisfied |
| `active` | `completed` | Outcome Report produced; outcomes measured against contract |
| any | `cancelled` | Human decision with documented rationale in STATUS.md |

> **Exception — missions without Execution tasks:** Some missions are scoped entirely to Strategy or Steering considerations (e.g., market analysis, policy evolution, organizational restructuring). These missions may transition to `active` without a TASKS.md. Document this explicitly in the Scope section with the rationale.

## Approval

- [ ] Strategy Layer human review
- [ ] Steering Layer review (for large missions)
- [ ] Affected division leads notified
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-02-24 | Added `planning` and `cancelled` statuses; added Status Transition Rules section with gates; documented TASKS.md requirement for `active` status and exception for non-execution missions |
| 1.0 | 2026-02-19 | Initial version |
