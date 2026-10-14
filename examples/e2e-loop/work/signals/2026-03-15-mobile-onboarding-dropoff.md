# Signal: Mobile Onboarding Step 3 Drop-Off

> **Created:** 2026-03-15
> **Author:** Agent (operate-loop)

---

## Source

- **Category:** customer
- **Source system:** Product analytics dashboard (mobile segment)
- **Source URL/reference:** Observability platform — onboarding funnel dashboard (mobile filter)
- **Confidence:** high

## Observation

During the postmortem for the desktop onboarding regression (INC-2026-003), mobile onboarding data was reviewed. Mobile Step 3 (workspace configuration) shows a 42% drop-off rate — even higher than the desktop regression peak of 34%. This has been stable at ~42% since the mobile app launch (2025-11-01) and was never addressed because desktop metrics were the primary focus.

Supporting data:
- Mobile Step 1 (account creation): 91% completion
- Mobile Step 2 (profile setup): 84% completion
- Mobile Step 3 (workspace config): 49% completion — 42% drop-off
- Mobile Step 4 (first project): 44% completion

The mobile form presents the same 12-field layout as the pre-fix desktop version, but on a smaller screen where the cognitive load is even higher.

## Initial Assessment

- **Urgency:** next-cycle
- **Strategic alignment:** "Reduce time-to-value for new customers"
- **Potential impact:** high
- **Affected divisions:** core-applications, customer-experience, mobile-engineering

## Related Signals

- Related to: `work/signals/2026-03-01-onboarding-step3-dropoff.md` (desktop variant — now resolved)

## Recommended Disposition

- [x] Proceed to opportunity validation
- [ ] Defer to next planning cycle
- [ ] Monitor
- [ ] Archive

## Notes

The desktop fix (progressive disclosure) should be directly applicable to mobile. However, mobile may need additional UX considerations (e.g., native form components, smaller field set). Filed from retrospective INC-2026-003 follow-up items.
