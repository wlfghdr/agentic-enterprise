# Tasks: MISSION-2026-008 — Fix Onboarding Step 3 Drop-Off

> Tracks execution work for this mission.

## Tasks

| ID | Task | Assignee | Status | PR |
|----|------|----------|--------|----|
| T1 | UX audit of current workspace config step | Agent (customer-experience) | done | — |
| T2 | Design simplified workspace setup flow | Agent (core-applications) | done | — |
| T3 | Implement simplified flow with progress indicator | Agent (core-applications) | done | PR #89 |
| T4 | Add contextual help tooltips | Agent (core-applications) | done | PR #89 |
| T5 | Set up A/B test infrastructure | Agent (quality-security-engineering) | done | PR #91 |
| T6 | Run A/B test (7 days minimum) | Agent (quality-security-engineering) | done | — |
| T7 | Analyze A/B test results and produce report | Agent (quality-security-engineering) | done | — |
| T8 | Roll out winning variant to 100% | Agent (core-applications) | done | PR #95 |

## Task Details

### T1: UX Audit

**Findings:**
- Workspace config presents 12 fields, only 3 are required
- No progress indicator — users don't know how many steps remain
- Error messages are technical, not user-friendly
- "Advanced settings" mixed with essential settings

### T3-T4: Implementation (PR #89)

**Changes:**
- Reduced initial form to 3 essential fields (name, timezone, default language)
- Added "Advanced settings" expandable section for remaining 9 fields
- Added step progress indicator (Step 3 of 4)
- Added contextual help tooltips on each field
- Improved error messages with plain-language explanations

### T7: A/B Test Results

| Metric | Control (current) | Variant (simplified) | Change |
|--------|-------------------|---------------------|--------|
| Step 3 completion | 66% | 84% | +18pp |
| Median config time | 4.2 min | 1.4 min | -67% |
| Overall onboarding completion | 71% | 86% | +15pp |
| Advanced settings usage | 100% (forced) | 23% (opt-in) | Expected |

**Decision:** VP Product approved rollout of simplified variant on 2026-03-14.
