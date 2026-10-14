# Division: Knowledge & Enablement

> **Owner:** <!-- Division lead name -->
> **Type:** GTM
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns documentation, tutorials, training content, battlecards, demo environments, POC configurations, and release notes. This division ensures customers and internal teams have the knowledge and tools to succeed.

## Scope

### In Scope
- Technical documentation and API docs generation
- Training content, certification modules, and interactive labs
- Competitive battlecards and RFP/RFI response management
- Demo environment maintenance and customization
- POC environment configuration per customer profile
- Release notes generation and content-product sync

### Out of Scope
- Product positioning and competitive strategy (→ Product Marketing)
- Customer support and health management (→ Customer Experience)
- CI/CD and developer tooling (→ Engineering Foundation)

## Key Responsibilities

1. **Documentation** — Generate and maintain technical docs, API references, and tutorials
2. **Training & Enablement** — Create training content, labs, and certification materials
3. **Sales Tools** — Maintain battlecards, RFP answer libraries, and demo environments
4. **POC Management** — Configure proof-of-concept environments per customer requirements
5. **Release Communication** — Generate release notes and maintain content-product consistency

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Product Marketing, Customer Experience | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/content.md` — For all documentation and training content

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
