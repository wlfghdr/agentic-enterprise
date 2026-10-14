# Mission Brief: Fix Mobile Onboarding Step 3 Drop-Off

> **Mission ID:** MISSION-2026-009
> **Status:** proposed
> **Created:** 2026-03-16
> **Author:** Strategy Layer
> **Design required:** true

---

## Origin

- **Signal(s):** `work/signals/2026-03-15-mobile-onboarding-dropoff.md`
- **Strategic alignment:** "Reduce time-to-value for new customers"
- **Sponsor:** Sarah Chen (VP Product) — _awaiting approval_

## Objective

Reduce the mobile Step 3 (workspace configuration) drop-off rate from 42% to ≤20% by adapting the progressive disclosure pattern proven on desktop, with mobile-specific UX optimizations.

## Scope

### In Scope
- Adapt desktop progressive disclosure pattern to mobile form factors
- Mobile-native form components (platform-appropriate inputs)
- A/B test simplified mobile flow vs. current flow
- Review mobile-specific UX constraints (screen size, touch targets)

### Out of Scope
- Desktop onboarding changes (already resolved by MISSION-2026-008)
- Full mobile app redesign
- Backend workspace architecture changes

### Constraints
- Must reuse the same workspace creation API (no backend changes)
- A/B test must run for at least 7 days before deciding
- Must not regress desktop onboarding metrics

## Divisions Involved

| Division | Role | Contribution |
|----------|------|-------------|
| mobile-engineering | Primary | Implement mobile UI changes |
| core-applications | Supporting | API compatibility review |
| customer-experience | Supporting | Mobile UX audit and design review |

## Outcome Contract

| Metric | Target | Measurement Method | Deadline |
|--------|--------|-------------------|----------|
| Mobile Step 3 drop-off rate | ≤20% | Product analytics funnel (mobile segment) | 2026-04-15 |
| Mobile onboarding completion | ≥75% | Product analytics funnel (mobile segment) | 2026-04-15 |
| Mobile workspace config time | <90 seconds median | Session timing (mobile) | 2026-04-15 |

## Human Checkpoints

1. **Mission approval** — Before work begins → VP Product _(current stage)_
2. **Mobile UX design review** — Before implementation begins → VP Product
3. **A/B test results review** — After 7-day test completes → VP Product

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Mobile platform differences (iOS vs Android) require separate implementations | medium | medium | Start with shared React Native component; split only if needed |
| Desktop progressive disclosure doesn't translate to mobile UX | low | high | Mobile UX audit before implementation; consider mobile-first alternatives |

## Estimated Effort

- **Size:** small (< 2 weeks)
- **Agent fleet size:** 2 concurrent agent streams
- **Human touchpoints:** 3 (mission approval, UX review, A/B results review)
