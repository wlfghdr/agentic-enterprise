# Division: Customer Experience

> **Owner:** <!-- Division lead name -->
> **Type:** Customer
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns customer success, support, onboarding, health monitoring, renewals, expansion, and advocacy. This division ensures customers derive maximum value and the enterprise maintains strong, growing customer relationships.

## Scope

### In Scope
- Support ticket triage, diagnosis, response, and resolution
- Customer health analysis and proactive monitoring
- Onboarding journey management and milestone tracking
- Renewal preparation and churn risk assessment
- Expansion and upsell opportunity identification
- SLA compliance tracking and performance reporting
- Knowledge base maintenance from resolved cases
- Customer signal detection for product improvement
- Escalation packaging for engineering teams
- Customer advocacy and reference management

### Out of Scope
- Product marketing and positioning (→ Product Marketing)
- Technical documentation and training (→ Knowledge & Enablement)
- Product strategy and roadmap (→ Strategy Layer)

## Key Responsibilities

1. **Support Operations** — Triage, diagnose, and resolve customer issues at scale
2. **Customer Health** — Monitor health metrics, detect churn signals, and drive proactive intervention
3. **Onboarding** — Accelerate time-to-first-value with structured onboarding journeys
4. **Revenue Protection** — Manage renewals with evidence-backed value realization reports
5. **Growth** — Identify and pursue expansion opportunities from usage patterns
6. **Voice of Customer** — Surface product improvement signals from support interactions
7. **Advocacy** — Identify reference candidates and assemble case study evidence

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Knowledge & Enablement, Product Marketing | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/customer.md` — For all customer-facing interactions
- `policies/content.md` — For customer-facing materials

## Human Checkpoints

These decisions require human division lead involvement:

- Architecture-changing proposals
- New external integrations
- Customer-impacting schema changes
- Work that crosses division boundaries

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Check the Software Catalog for existing services before creating new ones
3. Follow established code patterns in this division's codebase
4. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
5. Register new components via `org/3-execution/divisions/_TEMPLATE/_TEMPLATE-component-onboarding.md`

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Source code | <!-- repo URL --> | Main repository |
| Documentation | <!-- doc URL --> | User-facing docs |
| API specs | <!-- API spec URL --> | OpenAPI specs |
