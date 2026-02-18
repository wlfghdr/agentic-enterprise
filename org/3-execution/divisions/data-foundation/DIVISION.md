# Division: Data Foundation

> **Owner:** <!-- Division lead name -->
> **Type:** Core
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns core data storage, query engines, data governance, schema management, and data pipeline infrastructure. This division ensures data is reliably ingested, stored, queryable, and governed across the enterprise.

## Scope

### In Scope
- Data storage engines and query infrastructure
- Schema management and backward-compatible migrations
- Data governance — classification, retention, residency policies
- Signal routing and data pipeline management
- Data cost optimization and storage lifecycle management

### Out of Scope
- Application-level analytics dashboards (→ Core Applications)
- AI/ML model training and inference (→ AI & Intelligence)
- Business intelligence reporting (→ Core Applications)

## Key Responsibilities

1. **Data Storage & Query** — Maintain and optimize core data storage and query engines
2. **Schema Governance** — Ensure backward-compatible schema evolution across all data stores
3. **Data Pipeline Management** — Route signals to appropriate data stores with reliability guarantees
4. **Cost Optimization** — Manage storage tiering, retention policies, and data cost controls
5. **Data Compliance** — Enforce data residency, retention, and access control policies

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
- `policies/performance.md` — For query performance budgets
- `policies/observability.md` — For data pipeline observability

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
