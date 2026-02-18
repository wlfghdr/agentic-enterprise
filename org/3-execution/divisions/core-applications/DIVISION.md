# Division: Core Applications

> **Owner:** <!-- Division lead name -->
> **Type:** Core
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns the UI layer, dashboards, search, navigation, analytics interfaces, and user-facing application experiences. This division translates platform capabilities into usable products.

## Scope

### In Scope
- UI layer, dashboards, and visualization components
- Search, navigation, and information architecture
- Analytics and insights interfaces
- User experience monitoring and optimization
- Design system implementation and compliance

### Out of Scope
- Core APIs and authentication (→ Core Services)
- AI reasoning and NL interfaces (→ AI & Intelligence)
- Data storage and query engines (→ Data Foundation)

## Key Responsibilities

1. **User Interfaces** — Build and maintain all user-facing application experiences
2. **Analytics Dashboards** — Deliver actionable business intelligence through visual interfaces
3. **User Experience** — Monitor real user behavior and optimize conversion funnels and journeys
4. **Design System** — Implement and maintain design system compliance across all UIs

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Core Services, AI & Intelligence | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/experience.md` — For all UI changes
- `policies/performance.md` — For dashboard load time budgets

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
