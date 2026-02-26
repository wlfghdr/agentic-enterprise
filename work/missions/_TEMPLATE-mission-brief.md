# Mission Brief: [Mission Name]

> **Template version:** 1.3 | **Last updated:** 2026-02-25
> **Mission ID:** MISSION-YYYY-NNN
> **Status:** proposed | approved | planning | active | paused | completed | cancelled
> **Created:** YYYY-MM-DD
> **Revision:** 1 | **Last updated:** YYYY-MM-DD
> **Author:** [Strategy Layer agent or human]
> **Design required:** true | false _(Set to `true` for multi-stream missions, novel architecture patterns, new external APIs, data model changes, or regulated features. The Orchestration Layer will gate execution on a reviewed Technical Design document.)_
> **Blocked by:** _(optional — comma-separated Mission IDs that must complete before this mission can start, e.g., `MISSION-2026-040, MISSION-2026-041`)_
> **Blocks:** _(optional — comma-separated Mission IDs that depend on this mission's completion)_

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

## Observability Requirements

> **Requirement:** Per AGENTS.md Rule 9c — observability must be considered from mission inception, not deferred to implementation. For missions marked `design-required: true`, the full Observability Design lives in the Technical Design document. This section captures the high-level requirements that inform that design.

### Key Metrics

> What must be measurable for this mission to demonstrate success? These should align with the Outcome Contract metrics.

| Metric | Measurement Approach | Existing or New | Notes |
|--------|---------------------|-----------------|-------|
| [Outcome metric 1] | [How it will be observed — dashboard, query, etc.] | existing | new | [Notes] |

### Production Baselines at Risk

> For missions that touch existing production components, identify what must not degrade. Query the observability platform for current baselines.

| Component | Current SLO Status | Error Budget Remaining | Risk Level |
|-----------|--------------------|----------------------|------------|
| [Existing component 1] | [e.g., 99.95% availability] | [e.g., 62%] | low / medium / high |

> _Skip this section for entirely greenfield missions with no production dependencies._

### Observability Dependencies

- [ ] New dashboards required: yes / no — _(describe if yes)_
- [ ] New SLOs / health targets required: yes / no — _(describe if yes)_
- [ ] New alerting required: yes / no — _(describe if yes)_
- [ ] Existing monitoring must be updated: yes / no — _(describe if yes)_

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
| 1.3 | 2026-02-25 | Added Observability Requirements section (key metrics, production baselines at risk, observability dependencies) per AGENTS.md Rule 9c |
| 1.2 | 2026-02-25 | Added optional `blocked_by` and `blocks` fields for cross-mission dependency declaration |
| 1.1 | 2026-02-24 | Added `planning` and `cancelled` statuses; added Status Transition Rules section with gates; documented TASKS.md requirement for `active` status and exception for non-execution missions |
| 1.0 | 2026-02-19 | Initial version |
