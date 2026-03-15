# Technical Design: Onboarding Step 3 Simplification

> **Produced by:** Execution Layer (Technical Design Agent)
> **Reviewed at:** UX design review checkpoint (Sarah Chen, VP Product)

---

## Metadata

| Field | Value |
|-------|-------|
| **Mission ID** | MISSION-2026-008 |
| **Mission brief** | [BRIEF.md](./BRIEF.md) |
| **Outcome contract** | See Mission Brief — Outcome Contract section |
| **Fleet config** | 2 concurrent agent streams (core-applications, quality-security-engineering) |
| **Status** | approved |
| **Author** | Technical Design Agent (core-applications) |
| **Reviewers** | Sarah Chen (VP Product), eng-lead |
| **Created** | 2026-03-04 |
| **Approved** | 2026-03-05 |

---

## Context & Goals

The workspace configuration step (Step 3) in the customer onboarding flow currently presents 12 fields simultaneously, with no progress indicator and technical error messages. Since the UI redesign on 2026-01-15, the drop-off rate increased from 18% to 34%.

This design addresses the problem by reducing the initial form to 3 essential fields, adding progressive disclosure for advanced settings, and including a progress indicator. The design must be A/B testable to validate improvement before full rollout.

---

## API Contracts

No new API endpoints required. Existing workspace creation endpoint (`POST /api/v1/workspaces`) continues to accept the same payload — the change is purely in the frontend form that constructs the request.

---

## Data Model

No schema changes required. The existing workspace entity supports all fields as optional except `name`, `timezone`, and `language`, which align with the 3 essential fields in the simplified form.

---

## Interface Contracts Between Streams

| From Stream | To Stream | Interface | Contract |
|-------------|-----------|-----------|----------|
| core-applications | quality-security-engineering | A/B test flag | Feature flag `onboarding-v2-simplified` (boolean), managed via feature flag service |
| quality-security-engineering | core-applications | Test results | A/B test report with metrics: completion rate, median config time, advanced settings usage |

---

## Behavioral Specifications

### Behavior 1: Essential Fields Only

**Relates to:** Outcome Contract — workspace config time < 2 minutes

```gherkin
Scenario: New user sees only essential fields
  Given a new customer is on onboarding Step 3
  And the feature flag "onboarding-v2-simplified" is enabled
  When the workspace configuration form loads
  Then only 3 fields are visible: name, timezone, language
  And an "Advanced settings" expandable section is collapsed
  And a progress indicator shows "Step 3 of 4"
```

### Behavior 2: Advanced Settings Access

```gherkin
Scenario: Power user accesses advanced settings
  Given a new customer is on the simplified Step 3 form
  When the user clicks "Advanced settings"
  Then 9 additional fields become visible
  And all fields retain their default values
```

### Error & Edge Case Scenarios

```gherkin
Scenario: Form validation with clear error messages
  Given a new customer is on Step 3
  When the user submits the form with an empty workspace name
  Then a plain-language error appears: "Give your workspace a name to continue"
  And the error is not a technical validation message
```

---

## Security Threat Model

No new attack surfaces introduced. The change is a frontend-only form simplification. Existing input validation, CSRF protection, and rate limiting on the workspace creation endpoint remain unchanged.

---

## Performance Budgets

| Component | Metric | Budget | Measurement Method |
|-----------|--------|--------|--------------------|
| Onboarding Step 3 form | Time to interactive | < 500ms | Lighthouse CI |
| Form submission | Round-trip time | < 1s p95 | APM traces |
| A/B test flag evaluation | Latency overhead | < 10ms | Feature flag service metrics |

---

## Observability Design

### Production Baseline (Existing Components)

| Component | Metric | Current Value | Source Dashboard | Risk if Degraded |
|-----------|--------|---------------|------------------|------------------|
| Onboarding flow | Step 3 completion rate | 66% | Product analytics funnel | Direct mission KPI |
| Workspace API | p95 latency | 180ms | API health dashboard | Low risk — well within budget |
| Workspace API | Error rate | 0.2% | API health dashboard | Low risk — 95% error budget remaining |

- [x] Production baselines queried from observability platform for all modified components
- [x] Error budget status reviewed — workspace API has ample headroom
- [x] Dependency map reviewed — no downstream impact from frontend-only changes

### Instrumentation Plan

| Component | Span Name | Type | Attributes | Notes |
|-----------|-----------|------|------------|-------|
| Onboarding UI | `onboarding.step3.view` | client span | `variant` (control/simplified), `user.is_new` | Track which variant is shown |
| Onboarding UI | `onboarding.step3.submit` | client span | `variant`, `fields_filled`, `advanced_expanded` | Track form submission behavior |
| Onboarding UI | `onboarding.step3.error` | client span | `variant`, `error_field`, `error_type` | Track validation errors |

- [x] All new UI interactions produce client-side spans
- [x] Custom spans defined for business-critical operations (step completion tracking)
- [x] A/B test variant recorded as span attribute for segmented analysis

### Metrics Design

| Metric Name | Type | Labels/Dimensions | Description |
|-------------|------|-------------------|-------------|
| `onboarding.step3.completion_rate` | gauge | variant, platform | Percentage of users completing Step 3 |
| `onboarding.step3.duration_seconds` | histogram | variant | Time from form load to successful submission |
| `onboarding.step3.advanced_usage` | counter | variant | Count of users who expand advanced settings |

- [x] RED metrics defined for workspace API endpoint (existing)
- [x] Business metrics defined: completion rate, duration, advanced usage
- [x] Metric naming follows dot-separated, lowercase conventions

### Health Targets / SLOs

| Component | SLO Type | Target | Error Budget | Burn Rate Alert Threshold |
|-----------|----------|--------|-------------|---------------------------|
| Onboarding Step 3 | Completion rate | ≥ 80% (post-rollout) | 20% may not complete | 2x burn rate for 1h window |
| Workspace API | Availability | 99.9% | 0.1% over 30d rolling | Existing alerting |

### Dashboard Specification

| Dashboard | Key Visualizations | Audience | Auto-Created |
|-----------|--------------------|----------|--------------|
| Onboarding A/B Test | Completion rate by variant, config time distribution, advanced settings usage, error rates | VP Product, eng-lead | yes |

### Alerting Plan

| Alert | Condition | Severity | Routing | Runbook |
|-------|-----------|----------|---------|---------|
| Step 3 completion drop | completion_rate < 50% for 1h (either variant) | P2 | eng-lead Slack | Disable A/B test, revert to control |

### Observability Coverage Checklist

- [x] Every new UI interaction has a corresponding instrumentation plan entry
- [x] A/B test variant is propagated as a span attribute for segmented analysis
- [x] Every error path produces structured client-side events
- [x] SLOs defined for post-rollout completion rate target
- [x] Dashboard planned for A/B test monitoring
- [x] Production baselines consulted for workspace API

---

## Architecture Decisions

### Decision 1: Progressive Disclosure Over Multi-Step Wizard

| Field | Value |
|-------|-------|
| **Context** | Need to reduce cognitive load of 12-field form |
| **Options considered** | (a) Multi-step wizard splitting fields across sub-steps, (b) Progressive disclosure with expandable advanced section, (c) Remove advanced fields entirely |
| **Decision** | Progressive disclosure (option b) |
| **Rationale** | Preserves power-user access without adding navigation complexity. Simpler to implement and A/B test than a wizard. |
| **Consequences** | Advanced settings usage will drop (expected and acceptable per product team) |
| **ADR** | See `work/decisions/DR-2026-008-simplify-over-redesign.md` |

---

## Open Questions

| # | Question | Impact if Unresolved | Owner | Target Date | Resolution |
|---|----------|---------------------|-------|-------------|------------|
| 1 | Should advanced settings default values be pre-populated from company profile? | Minor UX improvement | eng-lead | 2026-03-06 | Deferred to follow-up mission — not blocking |

---

## Design Review Checklist

- [x] API contracts defined (no changes needed — existing endpoint)
- [x] Data model changes documented (no changes needed)
- [x] All inter-stream interface contracts specified (A/B test flag, results report)
- [x] Behavioral specs cover key scenarios (essential fields, advanced access, errors)
- [x] Security threat model completed (no new attack surfaces)
- [x] Performance budgets set with measurement methods
- [x] Observability design completed: instrumentation plan, metrics, SLOs, dashboards, alerting
- [x] Production baselines queried for workspace API
- [x] Impact assessment: no proposed change degrades existing SLOs
- [x] Architecture decisions documented
- [x] Open questions have owners and target dates
- [x] Design is consistent with architecture policy requirements

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | 2026-03-04 | Technical Design Agent | Initial draft |
| 2 | 2026-03-05 | Technical Design Agent | Approved after UX review |
