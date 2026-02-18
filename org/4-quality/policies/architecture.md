# Architecture Policy

> **Applies to:** All code changes, new services, API designs, data models, system integrations  
> **Enforced by:** Quality Layer eval agents  
> **Authority:** Architecture Governors (Steering Layer delegates)

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

### Code Quality
- [ ] Code coverage ≥ {{MIN_CODE_COVERAGE}} for new code
- [ ] No code duplication above threshold (DRY)
- [ ] Functions/methods within complexity limits
- [ ] Consistent naming conventions (per language style guide)
- [ ] Error handling: no swallowed exceptions, structured error responses

### Design System (UI)
- [ ] UI components use {{DESIGN_SYSTEM_NAME}} components exclusively
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
- [ ] ADR follows template: `process/templates/decision-record.md`
- [ ] ADR reviewed by at least one Architecture Governor

### Observability (cross-reference: [observability.md](observability.md))
- [ ] Every new service has at least one instrumentation source active (OTel SDK, APM agent, or API ingest)
- [ ] All service endpoints expose RED metrics (Rate, Errors, Duration)
- [ ] Distributed traces propagate context across all service boundaries (W3C Trace Context)
- [ ] Structured logging (JSON) with trace ID correlation on every log entry
- [ ] SLO defined for every production service
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
| Observability | Instrumented with traces, metrics, logs, SLOs | Missing instrumentation or no SLOs |
