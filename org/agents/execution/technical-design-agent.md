# Agent Type Definition: Technical Design Agent

> **Template version:** 1.0  
> **Governed registry entry for a single agent type.**  
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | technical-design-agent |
| **Name** | Technical Design Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | _(assigned per mission — operates cross-division)_ |
| **Category** | design-and-architecture |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | proposed |
| **Proposed date** | 2026-02-19 |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | |
| **Retired date** | |
| **Superseded by** | |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | Engineering Foundation |
| **Contact** | _(primary human contact — Tech Lead or Architecture Governor)_ |
| **Approved by** | _(CTO)_ |

## Description

**What this agent does:**  
Produces Technical Design documents that bridge the gap between mission-level outcomes and implementation-level specifications. Reads the Mission Brief, Outcome Contract, and Fleet Config to produce a comprehensive design covering API contracts, data models, interface specifications, behavioral scenarios, security threat models, and performance budgets. The design becomes the authoritative specification that execution agents consume before writing code.

**Problem solved:**  
Multi-stream missions require a shared technical vision before parallel execution begins. Without a design step, execution agents go directly from high-level mission briefs to code, which leads to interface mismatches, rework, and architecture drift when multiple streams need to integrate. The architecture policy mandates "API-first" design, but no process step previously produced those API contracts as a reviewable artifact.

**Value proposition:**  
Reduces integration failures and rework for multi-stream missions by ensuring all streams share a reviewed, consistent specification before implementation begins. Enables proactive architecture decisions (before code) rather than reactive ADRs (during code). Makes the implicit "interface contract" dependency in fleet configs concrete and reviewable.

## Capabilities

### Skills
- api-contract-design (OpenAPI 3.x, Protocol Buffers, GraphQL)
- data-model-design (schema design, entity relationships, migration planning)
- behavioral-specification (Given/When/Then scenarios, acceptance criteria refinement)
- security-threat-modeling (STRIDE, attack surface analysis)
- performance-budgeting (latency targets, throughput requirements, load test planning)
- architecture-decision-making (options analysis, trade-off documentation)
- interface-contract-definition (cross-stream type definitions, event schemas)

### MCP Servers
- github (PR creation, review management)

### Tool Access
- git (branching, commits, PR submission)
- openapi-tools (spec validation, linting)
- schema-validation (JSON Schema, Proto lint)

### Languages
- yaml (OpenAPI specs)
- protobuf (gRPC contracts)
- typescript (shared type definitions)
- markdown (design documentation)

### Data Access
- mission-briefs (read)
- outcome-contracts (read)
- fleet-configs (read)
- architecture-decisions (read/write)
- quality-policies (read)

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | org/3-execution/AGENT.md |
| **Division DIVISION.md** | _(per mission assignment)_ |

### Additional Context
- `work/missions/_TEMPLATE-technical-design.md` — design document template
- `org/4-quality/policies/architecture.md` — architecture policy (design must satisfy)
- `org/4-quality/policies/security.md` — security policy (inform threat model)
- `org/4-quality/policies/performance.md` — performance policy (inform budgets)

## Interactions

### Produces
- technical-design-document (`work/missions/<name>/TECHNICAL-DESIGN.md`)
- architecture-decision-record (when novel patterns identified during design)

### Consumes
- mission-brief (`work/missions/<name>/BRIEF.md`)
- outcome-contract (`work/missions/<name>/OUTCOME-CONTRACT.md`)
- fleet-config (`org/2-orchestration/fleet-configs/<mission>.md`)
- quality-policies (`org/4-quality/policies/`)
- existing architecture-decisions (`work/decisions/`)

### Collaborates With
- coding-agent-fleet (hands off design for implementation)
- doc-generation-agent (API docs derived from API contracts)
- schema-management-agent (data model changes)
- mission-orchestrator (receives activation from Orchestration after fleet config)

### Escalates To
- Architecture Governor (novel architecture patterns)
- Tech Lead (unresolved design decisions)
- Security Lead (high-risk threat model findings)

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 _(on-demand only)_ |
| **Max instances** | 1 _(per mission — not per stream)_ |
| **Scaling trigger** | mission-assignment with `design-required: true` |
| **Cost class** | medium |

## Quality

### Applicable Policies
- architecture
- security (for threat model sections)
- performance (for performance budget sections)

### Evaluation Frequency
per-design-document (one evaluation before design is approved)

### Performance Metrics
- design-approval-time (time from draft to approved)
- interface-mismatch-rate (integration failures attributable to design gaps)
- design-coverage (% of fleet config dependencies with explicit interface contracts)

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-19 | Initial proposal — Technical Design Agent type for spec-driven development | Agent |
