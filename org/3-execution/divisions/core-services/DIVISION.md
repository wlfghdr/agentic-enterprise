# Division: Core Services

> **Owner:** <!-- Division lead name -->
> **Type:** Core
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns identity, authentication, authorization, RBAC, API lifecycle management, and core platform services. This division provides the foundational service layer that all other divisions depend on.

## Scope

### In Scope
- Identity and access management (IAM)
- RBAC policy enforcement and governance
- API lifecycle management and versioning
- Token management and authentication services
- Core platform APIs and service contracts

### Out of Scope
- UI layer and dashboards (→ Core Applications)
- Infrastructure provisioning (→ Infrastructure Operations)
- Security scanning and vulnerability management (→ Quality & Security Engineering)

## Key Responsibilities

1. **Identity & Access** — Manage IAM, authentication, and authorization across the platform
2. **Policy Enforcement** — Ensure RBAC policies are enforced consistently across all services
3. **API Management** — Maintain API standards, versioning, and backward compatibility
4. **Service Contracts** — Define and enforce service-level contracts between divisions

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Data Foundation, Core Applications | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/security.md` — For all IAM and access control changes

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
