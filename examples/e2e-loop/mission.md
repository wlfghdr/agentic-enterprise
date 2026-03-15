# Mission Brief: Fix Onboarding Step 3 Drop-Off

> **Mission ID:** MISSION-2026-008
> **Status:** completed
> **Created:** 2026-03-03
> **Revision:** 2 | **Last updated:** 2026-03-18
> **Author:** Strategy Layer
> **Design required:** false

---

## Origin

- **Signal(s):** `work/signals/2026-03-01-onboarding-step3-dropoff.md`
- **Strategic alignment:** "Reduce time-to-value for new customers"
- **Sponsor:** Sarah Chen (VP Product)

## Objective

Reduce the Step 3 (workspace configuration) drop-off rate from 34% back to ≤20% by simplifying the workspace setup flow, restoring onboarding completion rates to pre-redesign levels.

## Scope

### In Scope
- UX audit of the current workspace configuration step
- Simplify the workspace settings to essential fields only
- Add progress indicator and contextual help
- A/B test simplified flow vs. current flow

### Out of Scope
- Full onboarding redesign (other steps are performing well)
- Backend workspace architecture changes
- Mobile onboarding flow (desktop only for now)

### Constraints
- Must not break existing workspace configurations
- A/B test must run for at least 7 days before deciding

## Divisions Involved

| Division | Role | Contribution |
|----------|------|-------------|
| core-applications | Primary | Implement UI changes |
| customer-experience | Supporting | UX audit and design review |
| quality-security-engineering | Supporting | A/B test setup and analysis |

## Outcome Contract

| Metric | Target | Measurement Method | Deadline |
|--------|--------|-------------------|----------|
| Step 3 drop-off rate | ≤20% | Product analytics funnel | 2026-03-21 |
| Overall onboarding completion | ≥80% | Product analytics funnel | 2026-03-21 |
| Workspace config time | <2 minutes median | Session timing | 2026-03-21 |

## Human Checkpoints

1. **UX design review** — Before implementation begins → VP Product
2. **A/B test results review** — After 7-day test completes → VP Product

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Simplified flow loses power-user features | medium | medium | Add "Advanced settings" expandable section |
| A/B test inconclusive | low | medium | Extend test duration to 14 days |

## Estimated Effort

- **Size:** small (< 2 weeks)
- **Agent fleet size:** 2 concurrent agent streams
- **Human touchpoints:** 2 (UX review, A/B results review)

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | 2026-03-03 | Strategy Layer | Initial draft |
| 2 | 2026-03-18 | Strategy Layer | Status updated to completed |
