# Division: Engineering Foundation

> **Owner:** <!-- Division lead name -->
> **Type:** Operations
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns the developer portal, build infrastructure, CI/CD pipelines, golden paths, and release engineering. This division provides the engineering platform that all development teams depend on for productivity and delivery.

## Scope

### In Scope
- CI/CD pipeline infrastructure and optimization
- Build systems, artifact management, and dependency updates
- Developer portal and service catalog maintenance
- Deployment automation — blue-green, canary, rolling strategies
- Release engineering — canary analysis, rollback procedures, feature flag infrastructure
- Code quality gates and static analysis integration
- Integration connectors for development tools (Git, CI/CD, project management)

### Out of Scope
- Cloud infrastructure provisioning (→ Infrastructure Operations)
- Security scanning and vulnerability triage (→ Quality & Security Engineering)
- Application code implementation (→ domain-specific divisions)

## Key Responsibilities

1. **CI/CD Pipeline** — Maintain and optimize build and deployment pipelines for all teams
2. **Release Engineering** — Ensure safe, progressive delivery with canary analysis and rollback
3. **Developer Experience** — Provide golden paths, service catalog, and self-service tooling
4. **Quality Gates** — Enforce automated quality checks on every pull request
5. **Tool Integration** — Maintain connectors between development tools and workflows

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Infrastructure Operations, Quality & Security Engineering | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/delivery.md` — For all deployment and release changes
- `policies/architecture.md` — For pipeline architecture decisions

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
