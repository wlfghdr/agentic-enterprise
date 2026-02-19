# Release Contract: [Release Name / Version]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Release ID:** REL-YYYY-NNN  
> **Status:** draft | approved | deploying | deployed | rolled-back  
> **Created:** YYYY-MM-DD  
> **Revision:** 1 | **Last updated:** YYYY-MM-DD
> **Release Manager:** [name]  
> **Storage:** `work/releases/YYYY-MM-DD-<release-name>.md`

---

## Release Summary

[One paragraph: what is being released and why]

## Changes Included

| Change | Type | Mission | Quality Verdict |
|--------|------|---------|----------------|
| [Change description] | feature / fix / improvement / deprecation | [Mission ID] | PASS |
| [Change description] | feature / fix / improvement / deprecation | [Mission ID] | PASS |

## Breaking Changes

- [ ] **No breaking changes** in this release
- [ ] Breaking changes listed below:
  - [Description of breaking change + migration instructions]

## Progressive Rollout Plan

| Stage | Target | Duration | Health Criteria | Rollback Trigger |
|-------|--------|----------|-----------------|-----------------|
| Canary | {{CANARY_PERCENTAGE}} | {{CANARY_DURATION}} | Error rate < baseline + {{MAX_ERROR_RATE_INCREASE}} | Auto-rollback on any critical alert |
| Early Adopters | {{EARLY_ADOPTER_PERCENTAGE}} | {{EARLY_ADOPTER_DURATION}} | Error rate stable, latency within target | Auto-rollback on health target breach |
| General | {{GA_PERCENTAGE}} | {{GA_DURATION}} | All metrics stable | Manual rollback available |
| Full | 100% | Ongoing | Standard monitoring | Standard incident process |

## Rollback Plan

- **Rollback mechanism:** [e.g., deployment tool rollback, feature flag disable]
- **Rollback tested:** yes / no
- **Estimated rollback time:** [e.g., < 5 minutes]
- **Data rollback needed:** yes / no — [if yes, describe procedure]

## Pre-Deployment Checklist

- [ ] All quality evaluations passed
- [ ] **Production readiness verified** — see `org/4-quality/policies/observability.md`:
  - [ ] Instrumentation active and telemetry flowing
  - [ ] Distributed traces verified (end-to-end, W3C context)
  - [ ] Key metrics on all endpoints
  - [ ] Structured logs with trace ID correlation
  - [ ] Health targets defined and alerting active
  - [ ] Service health dashboard created and linked in catalog
  - [ ] Alerting configured with runbooks
  - [ ] Agent observability verified (if agent component)
- [ ] Release contract reviewed by human
- [ ] Rollback plan documented and tested
- [ ] Feature flags configured
- [ ] Database migrations backward-compatible
- [ ] Monitoring dashboards updated
- [ ] On-call team notified
- [ ] Release notes prepared

## Release Notes

### Customer-Facing

#### New Features
- [Feature description — user benefit]

#### Improvements
- [Improvement description]

#### Bug Fixes
- [Fix description]

#### Deprecations
- [Deprecated feature — migration path — removal timeline]

### Internal Notes
- [Internal-only information about this release]

## Post-Deployment Validation

- [ ] Error rates within normal bounds
- [ ] Latency within target
- [ ] No critical alerts triggered
- [ ] Smoke tests passing
- [ ] Feature flag behavior verified
- [ ] Resource consumption within expected bounds

## Approval

- [ ] Release Manager approval
- [ ] On-call acknowledgment
- [ ] Stakeholder notification sent
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
