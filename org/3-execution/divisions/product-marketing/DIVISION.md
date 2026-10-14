# Division: Product Marketing

> **Owner:** <!-- Division lead name -->
> **Type:** GTM
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns go-to-market execution, product launches, press and analyst relations, competitive positioning, and marketing content. This division ensures new capabilities reach the market effectively and the company maintains competitive positioning.

## Scope

### In Scope
- Product launch coordination and multi-channel execution
- Competitive positioning, battlecard updates, and market intelligence
- Marketing content — blog posts, press releases, social media
- Sales proposal generation and business case development
- Win story creation and customer evidence packaging
- Analyst briefing preparation and competitive wave analysis

### Out of Scope
- Technical documentation and tutorials (→ Knowledge & Enablement)
- Customer success and support (→ Customer Experience)
- Product strategy and venture charters (→ Strategy Layer)

## Key Responsibilities

1. **Product Launches** — Coordinate multi-channel launch activities with timeline and asset management
2. **Competitive Intelligence** — Monitor competitors and maintain current positioning materials
3. **Content Production** — Generate marketing content at product velocity
4. **Sales Enablement Content** — Create proposals, win stories, and business cases
5. **Analyst Relations** — Prepare analyst briefing materials and competitive analysis

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Knowledge & Enablement, Customer Experience | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/content.md` — For all customer-facing content
- `policies/customer.md` — For customer-facing claims

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
