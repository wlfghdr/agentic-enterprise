# Division: {{DOMAIN_CAP_2_NAME}}

> **Owner:** <!-- Division lead name -->
> **Type:** Domain
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Domain-specific capability division. Customize this division to own a specific product domain in your organization. See CONFIG.yaml to set the name and description.

## Scope

### In Scope
- <!-- Define domain-specific scope items here -->

### Out of Scope
- <!-- Define explicit boundaries here -->

## Key Responsibilities

1. **Domain Delivery** — Own end-to-end delivery of domain-specific capabilities
2. **Domain Expertise** — Maintain deep domain knowledge and best practices
3. **Domain Integration** — Ensure domain capabilities integrate cleanly with core platform

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Core Services, Core Applications | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes


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
