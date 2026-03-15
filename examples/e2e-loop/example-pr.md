# Example Pull Request: PR #89

> This file shows what a governed PR looks like in the Agentic Enterprise workflow. In practice, this would be a real GitHub PR — this file documents the pattern.

---

## PR Title

`fix(onboarding): simplify workspace config step to reduce drop-off`

## PR Description

### Summary

- Reduce workspace config from 12 fields to 3 essential fields (name, timezone, language)
- Move 9 non-essential fields to expandable "Advanced settings" section
- Add step progress indicator showing "Step 3 of 4"
- Add contextual help tooltips for each field

### Context

- **Mission:** MISSION-2026-008 — Fix Onboarding Step 3 Drop-Off
- **Signal:** `work/signals/2026-03-01-onboarding-step3-dropoff.md`
- **Tasks:** T3, T4

### Why

Step 3 drop-off increased from 18% to 34% after the workspace settings UI redesign on 2026-01-15. This PR simplifies the flow back to essential fields while preserving power-user access via an expandable section.

### Test Plan

- [ ] Unit tests pass for new form component
- [ ] Integration test: complete onboarding with minimal fields
- [ ] Integration test: complete onboarding with all advanced fields
- [ ] Visual regression test: progress indicator renders correctly
- [ ] A/B test flag correctly splits traffic

### Quality Policy Checklist

- [x] Code meets `org/4-quality/policies/code-quality.md` standards
- [x] Accessibility requirements met (keyboard navigation, screen reader labels)
- [x] No new security vulnerabilities introduced
- [x] Observability: new spans added for step completion tracking

---

## PR Metadata

| Field | Value |
|-------|-------|
| **Author** | Agent (core-applications) |
| **Reviewers** | @sarah-chen (VP Product), @eng-lead |
| **Labels** | `mission/2026-008`, `division/core-applications` |
| **Branch** | `mission/2026-008-onboarding-step3` |
| **CI Status** | All checks passing |
| **CODEOWNERS match** | `src/onboarding/` → @eng-lead |

## Review Flow

```
1. Agent opens PR, assigns to self, requests review from CODEOWNERS
2. CI runs: lint, test, security scan, policy check → all pass
3. @eng-lead reviews code → approves
4. @sarah-chen reviews UX changes → approves
5. Agent merges PR
6. Agent updates mission status and task list
```

## What Makes This a Good PR

1. **Linked to mission and signal** — Traceability from observation to change
2. **Clear scope** — Does exactly what the tasks specify, nothing more
3. **Quality gate compliance** — Explicitly checks against quality policies
4. **Reviewers from CODEOWNERS** — Governance is enforced, not optional
5. **Observability included** — New telemetry spans added as part of the change
