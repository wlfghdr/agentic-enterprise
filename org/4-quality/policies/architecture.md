# Architecture Policy

> **Applies to:** All code changes, new services, API designs, data models, system integrations
> **Enforced by:** Quality Layer eval agents
> **Authority:** Architecture Governors (Steering Layer delegates)
> **Version:** 1.2 | **Last updated:** 2026-02-25

---

## Principles

1. **Consistency over creativity** — Use established patterns before inventing new ones.
2. **API-first** — Design the contract before the implementation.
3. **Loose coupling** — Services communicate through well-defined interfaces, not shared state.
4. **Observable by default** — Every service must emit structured telemetry (logs, metrics, traces). See [observability.md](observability.md) for full requirements — **nothing ships without observability**.

## Mandatory Requirements

### Service Design
- [ ] New services registered in the Software Catalog before development begins, with at minimum: **name**, **type** (service, library, website), **owner** (team/division), **lifecycle status** (experimental, production, deprecated), and links to health dashboard and API contract
- [ ] Service boundaries aligned with division boundaries
- [ ] API contracts defined in OpenAPI 3.x (REST) or Protocol Buffers (gRPC)
- [ ] Breaking API changes follow deprecation policy (minimum 2 release cycles)
- [ ] No direct database access across service boundaries

### Technical Design
- [ ] **Multi-stream missions** (2+ streams with dependencies) must have a Technical Design document (`_TEMPLATE-technical-design.md`) approved before execution begins
- [ ] Technical Design includes: API contracts, data model changes, interface contracts between streams, behavioral specifications, security threat model, performance budgets, and **observability design** (instrumentation plan, metrics, SLOs, dashboards, alerting — per [observability.md](observability.md))
- [ ] Technical Design reviewed by Architecture Governor (and Security Lead if security-sensitive)
- [ ] All inter-stream interface contracts from the fleet config are defined in the Technical Design — no implicit interfaces
- [ ] Behavioral specifications map to acceptance criteria in the Outcome Contract
- [ ] For single-stream or low-complexity missions: design step may be skipped if the Orchestration Layer marks `design-required: false`

### Code Quality
- [ ] Code coverage ≥ {{MIN_CODE_COVERAGE}} for new code
- [ ] No code duplication above threshold (DRY)
- [ ] Functions/methods within complexity limits
- [ ] Consistent naming conventions (per language style guide)
- [ ] Error handling: no swallowed exceptions, structured error responses

### Design System (UI)
- [ ] UI components use the company design system components exclusively
- [ ] No custom CSS that overrides design system tokens
- [ ] Accessibility: WCAG 2.1 AA minimum
- [ ] Responsive design for supported viewport sizes
- [ ] Dark mode support if applicable

### Data Architecture
- [ ] Data models documented
- [ ] Schema changes backward-compatible or versioned
- [ ] Data pipelines idempotent
- [ ] Query performance validated (no unbounded queries)

### Architecture Decision Records
- [ ] Novel patterns justified in an Architecture Decision Record (ADR)
- [ ] ADR follows template: `work/decisions/_TEMPLATE-decision-record.md`
- [ ] ADR reviewed by at least one Architecture Governor

### Observability (cross-reference: [observability.md](observability.md))
- [ ] Every new service has at least one instrumentation source active (OTel SDK, APM agent, or API ingest)
- [ ] All service endpoints expose RED metrics (Rate, Errors, Duration)
- [ ] Distributed traces propagate context across all service boundaries (W3C Trace Context)
- [ ] Structured logging (JSON) with trace ID correlation on every log entry
- [ ] Health target defined for every production service
- [ ] Service health dashboard created and linked in Software Catalog
- [ ] Alerting configured with documented runbooks
- [ ] **No component progresses to production without verified observability**

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Uses existing patterns | Follows established conventions | Introduces novel pattern without ADR |
| API contract | Defined before implementation | Implementation without contract |
| Code coverage | ≥ {{MIN_CODE_COVERAGE}} | Below threshold |
| Design system | Uses standard components | Custom components without approval |
| Service boundary | Aligned with division | Cross-division data sharing |
| Observability | Instrumented with traces, metrics, logs, health targets; observability designed in Technical Design with production baselines consulted | Missing instrumentation, no health targets, or no observability design in Technical Design |
| Technical design | Design document exists and approved for multi-stream missions | Multi-stream mission executing without reviewed design |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
| 1.2 | 2026-02-25 | Added observability design to Technical Design checklist; updated evaluation criteria to include design-time observability |
| 1.1 | 2026-02-23 | Replace {{DESIGN_SYSTEM_NAME}} placeholder with generic "company design system" language |
