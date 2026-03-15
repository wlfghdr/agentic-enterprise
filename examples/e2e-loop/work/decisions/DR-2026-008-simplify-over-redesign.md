# Decision Record: Simplify Step 3 via Progressive Disclosure (Not Full Redesign)

> **Decision ID:** DR-2026-008
> **Status:** accepted
> **Created:** 2026-03-04
> **Revision:** 1 | **Last updated:** 2026-03-05
> **Author:** Strategy Layer + Technical Design Agent
> **Reviewers:** Sarah Chen (VP Product), eng-lead

---

## Context

The onboarding Step 3 (workspace configuration) drop-off rate increased from 18% to 34% after a UI redesign on 2026-01-15 that consolidated 12 workspace settings into a single form. The mission (MISSION-2026-008) requires reducing drop-off back to ≤20%. Three approaches were considered.

## Decision

Use progressive disclosure: show only 3 essential fields (name, timezone, language) by default, with remaining 9 fields in a collapsible "Advanced settings" section. Validate improvement via A/B test before full rollout.

## Alternatives Considered

### Alternative 1: Multi-Step Wizard
- **Description:** Split the 12 fields across 3 sub-steps within Step 3 (basic → team → advanced)
- **Pros:** Guided experience, each sub-step feels lightweight
- **Cons:** Adds navigation complexity, longer total time, harder to A/B test, higher implementation effort
- **Why rejected:** Adds complexity rather than reducing it; product analytics show users don't need most fields

### Alternative 2: Full Onboarding Redesign
- **Description:** Redesign the entire 4-step onboarding flow with a wizard-based approach
- **Pros:** Addresses all steps, future-proof
- **Cons:** 3-4x scope, 6+ weeks effort, high risk of regression in working steps
- **Why rejected:** Out of scope — Steps 1, 2, and 4 are performing well; violates constraint to fix Step 3 specifically

### Alternative 3: Remove Advanced Fields Entirely
- **Description:** Permanently remove the 9 non-essential fields from onboarding; users configure later in settings
- **Pros:** Simplest implementation, fastest to ship
- **Cons:** Breaks existing onboarding flows for power users, may increase support tickets from users who expect workspace settings during setup
- **Why rejected:** Too aggressive — analytics needed on actual advanced settings usage before considering removal

## Consequences

### Positive
- Minimal implementation effort (< 2 weeks)
- Preserves all existing functionality for power users
- A/B testable — data-driven rollout decision
- Reversible if metrics don't improve

### Negative
- Advanced settings usage will drop (expected: from 100% forced to ~23% opt-in)
- Some power users may be confused by the collapsed section initially

### Neutral
- No backend changes required — risk profile is very low
- A/B test infrastructure (feature flags) can be reused for future experiments

## Affected Components

- Frontend: `src/onboarding/WorkspaceConfigStep.tsx`
- Frontend: `src/components/ProgressIndicator.tsx` (new)
- Feature flag service: `onboarding-v2-simplified` flag

## Related Decisions

- None — first decision record for this mission

## Review Schedule

This decision should be reviewed: after A/B test results are available (2026-03-14)

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | 2026-03-04 | Strategy Layer + Technical Design Agent | Initial draft — accepted after VP Product review |
