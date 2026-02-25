# Outcome Contract: [Mission Name]

> **Template version:** 1.1 | **Last updated:** 2026-02-25  
> **Defines measurable success criteria for a mission.**  
> **Lives alongside the mission brief in** `work/missions/<name>/`

---

## Mission

| Field | Value |
|-------|-------|
| **Mission ID** | _(e.g., MISSION-2026-042)_ |
| **Mission brief** | [BRIEF.md](./BRIEF.md) |

## Outcomes

### Outcome 1: [Name]

| Field | Value |
|-------|-------|
| **Description** | _(what this outcome measures)_ |
| **Metric** | _(e.g., "p95 API latency")_ |
| **Baseline** | _(current value before mission)_ |
| **Target** | _(target value)_ |
| **Measurement method** | _(how this is measured)_ |
| **Measurement source** | _(system/tool that provides the data)_ |
| **Deadline** | YYYY-MM-DD |
| **Status** | not-started _(not-started / in-progress / met / not-met)_ |

<!-- Copy the outcome section above for additional outcomes -->

## Acceptance Criteria

- [ ] _(e.g., "All API endpoints respond within target")_
- [ ] _(criterion 2)_

## Measurement Schedule

> **Purpose:** These dates trigger outcome measurement. The Quality Layer monitors these dates and produces outcome reports when each checkpoint arrives. The Strategy Layer uses `measurement_schedule` dates to trigger outcome report creation.

| Field | Value |
|-------|-------|
| **Measurement window start** | YYYY-MM-DD _(when to begin measuring outcomes — typically deployment date)_ |
| **Measurement window end** | YYYY-MM-DD _(when final measurement closes — typically 4-12 weeks post-deployment)_ |

| Checkpoint | Date | Status |
|------------|------|--------|
| **Initial check** | YYYY-MM-DD _(e.g., 1 week post-deployment)_ | pending _(pending / completed / skipped)_ |
| **Interim check** | YYYY-MM-DD _(e.g., 4 weeks post-deployment; add rows for additional interim checks if needed)_ | pending |
| **Final evaluation** | YYYY-MM-DD _(e.g., 8 weeks post-deployment)_ | pending |
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-02-25 | Enhanced Measurement Schedule with structured date fields (window start/end, interim checks with status tracking); added purpose note linking to Quality and Strategy Layer consumption |
| 1.0 | 2026-02-19 | Initial version |
