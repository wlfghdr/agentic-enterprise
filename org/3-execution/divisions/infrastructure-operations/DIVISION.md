# Division: Infrastructure Operations

> **Owner:** <!-- Division lead name -->
> **Type:** Operations
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns cloud accounts, infrastructure-as-code, container orchestration, production operations, incident management, capacity planning, and cost management. This division keeps the production environment healthy, efficient, and reliable.

## Scope

### In Scope
- Cloud infrastructure provisioning and IaC management
- Container orchestration (Kubernetes) monitoring and management
- Production health monitoring — hosts, networks, processes
- Incident detection, response, and auto-remediation
- Capacity planning and demand forecasting
- Cloud cost management and FinOps optimization
- Backup, disaster recovery, and data restoration
- Performance monitoring and baseline management
- Resilience testing and failure injection

### Out of Scope
- CI/CD pipeline management (→ Engineering Foundation)
- Security vulnerability scanning (→ Quality & Security Engineering)
- Application-level code changes (→ domain-specific divisions)

## Key Responsibilities

1. **Infrastructure Provisioning** — Manage IaC and container orchestration with policy compliance
2. **Production Health** — Monitor service, host, network, and process health across all environments
3. **Incident Management** — Detect, triage, respond to, and auto-remediate production incidents
4. **Cost Optimization** — Track cloud spend, identify waste, and implement rightsizing recommendations
5. **Capacity & Resilience** — Forecast demand, plan capacity, and conduct resilience testing
6. **Disaster Recovery** — Maintain backup procedures and ensure data restoration capabilities

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Engineering Foundation, Quality & Security Engineering | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/observability.md` — For all monitoring and alerting
- `policies/performance.md` — For performance baselines and budgets

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
