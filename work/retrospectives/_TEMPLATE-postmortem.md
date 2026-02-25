# Postmortem: [Incident Name]

> **Template version:** 1.1 | **Last updated:** 2026-02-25  
> **Incident ID:** INC-YYYY-NNN  
> **Severity:** SEV1 (Critical) | SEV2 (Major) | SEV3 (Minor) | SEV4 (Low)  
> **Status:** draft | reviewed | accepted  
> **Date of incident:** YYYY-MM-DD HH:MM UTC  
> **Date of resolution:** YYYY-MM-DD HH:MM UTC  
> **Author:** [Operate Loop agent + on-call engineer]  
> **Storage:** `work/retrospectives/YYYY-MM-DD-<incident-name>.md`

---

## Incident Summary

[One paragraph: what happened, who was affected, how it was resolved]

## Timeline

| Time (UTC) | Event |
|-----------|-------|
| HH:MM | [First anomaly detected — how and by whom/what] |
| HH:MM | [Alert fired — which alert, which system] |
| HH:MM | [Triage began — who was involved] |
| HH:MM | [Root cause identified] |
| HH:MM | [Remediation action taken] |
| HH:MM | [Service restored / incident resolved] |
| HH:MM | [Post-resolution validation complete] |

## Impact

### Blast Radius
- **Services affected:** [list of impacted services/components]
- **Customers affected:** [number or percentage of impacted users]
- **Duration:** [total time from first impact to full resolution]
- **Service impact:** [which health targets were breached, by how much]
- **Impact on service health targets:** [percentage of error budget consumed by this incident]

### Business Impact
- **Revenue impact:** [estimated, if applicable]
- **Customer trust impact:** [churn risk, escalations, complaints]
- **Data impact:** [any data loss or corruption]

## Detection

- **How was it detected?** [monitoring alert / customer report / agent detection / manual observation]
- **Time to detect (TTD):** [minutes from first impact to detection]
- **Was the detection method adequate?** [yes / no — if no, what should change]

## Root Cause Analysis

### Root Cause
[Clear, specific description of the root cause]

### 5 Whys
1. **Why** did the incident occur? → [answer]
2. **Why** did that happen? → [answer]
3. **Why** did that happen? → [answer]
4. **Why** did that happen? → [answer]
5. **Why** did that happen? → [root cause]

### Contributing Factors
- [Factor 1 — e.g., missing test coverage for edge case]
- [Factor 2 — e.g., gap in the affected pathway's monitoring coverage]

## Remediation

### Immediate Actions Taken
- [Action 1 — e.g., rolled back deployment v2.3.1 → v2.3.0]
- [Action 2 — e.g., scaled up replicas to handle backlog]

### Was a Runbook Used?
- [ ] **Yes** — Runbook: [link] — Was it adequate? [yes / no — if no, what was missing]
- [ ] **No** — No runbook existed for this scenario

## Policy Gap Analysis

| Policy | Gap Identified? | Description |
|--------|----------------|-------------|
| Security | yes / no | [description of gap, if any] |
| Observability | yes / no | [e.g., "missing coverage for this failure mode"] |
| Delivery | yes / no | [e.g., "rollback procedure was unclear"] |
| Architecture | yes / no | [e.g., "single point of failure not documented"] |

## Follow-Up Items

### Immediate (This Week)

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Fix the immediate bug/config] | [name/team] | YYYY-MM-DD | open / done |
| [Update runbook] | [name/team] | YYYY-MM-DD | open / done |

### Short-Term (This Month)

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Add missing test or monitoring coverage] | [name/team] | YYYY-MM-DD | open / done |
| [Improve test coverage] | [name/team] | YYYY-MM-DD | open / done |

### Long-Term (Requires Mission)

| Action | Signal Filed? | Signal Link |
|--------|--------------|-------------|
| [Architectural rework to eliminate SPOF] | yes / no | [link to `work/signals/`] |
| [Policy update to prevent recurrence] | yes / no | [link to `work/signals/`] |

## Signals Filed

> **Every postmortem must produce at least one signal.** Insights from incidents feed back into the Discover loop via `work/signals/`. This section is the explicit link between retrospectives and the signal lifecycle — it ensures no insight is lost.

| Signal ID | Description | Category | Link |
|-----------|-------------|----------|------|
| YYYY-MM-DD-<slug> | [What this signal captures from the incident] | technical / process / policy / architecture | [`work/signals/YYYY-MM-DD-<slug>.md`](../../signals/YYYY-MM-DD-<slug>.md) |
| | | | |

**Filing guidance:**
- File at least one signal per postmortem — even if the lesson is "our monitoring worked correctly"
- For policy gaps identified in the Policy Gap Analysis above, file a separate signal per gap
- For long-term architectural issues, file a signal that may become a mission

## Lessons Learned

### What went well
- [e.g., "Detection was fast due to automated health monitoring"]

### What could be improved
- [e.g., "Runbook was outdated, added 10 minutes to resolution"]

### Systemic observations
- [e.g., "This is the 2nd incident this quarter related to database connection pooling — may need an architecture mission"]

## Approval

- [ ] On-call engineer reviewed and validated timeline
- [ ] Operations Policy Author reviewed policy gap analysis
- [ ] All follow-up items assigned and tracked
- [ ] Improvement signals filed in `work/signals/`
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-02-25 | Renamed "Generated Signals" to "Signals Filed" with explicit signal IDs, file links, filing guidance, and Discover loop feedback requirement |
| 1.0 | 2026-02-19 | Initial version |
