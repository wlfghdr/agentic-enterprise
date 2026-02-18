# Agent Type Definition: Customer Material Evaluator

> **Status:** proposed | **Proposed date:** 2026-02-18
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `quality-customer-material-evaluator` |
| **Name** | Customer Material Evaluator |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | quality |
| **Division** | `—` |
| **Category** | material-evaluation |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | proposed |
| **Proposed date** | 2026-02-18 |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | |
| **Retired date** | |
| **Superseded by** | |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | <!-- assign during approval --> |
| **Contact** | <!-- primary human contact --> |
| **Approved by** | <!-- CTO or delegate --> |

## Description

**What this agent does:**
Evaluates customer-facing materials for SLA compliance, data accuracy, and defensible claims.

**Problem solved:**
Customer-facing claims must be accurate and defensible. Automated review prevents embarrassment and liability.

**Value proposition:**
Every enterprise following the agentic operating model benefits from this agent because it addresses a universal organizational need that scales with agent fleet adoption.

## Capabilities

### Skills
- material-evaluation

### MCP Servers
- <!-- configure per enterprise toolchain -->

### Tool Access
- <!-- configure per enterprise toolchain -->

### Languages
- <!-- configure per implementation -->

### Data Access
- customer-materials
- sla-data
- compliance-requirements

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/4-quality/AGENT.md` |
| **Division DIVISION.md** | `—` |

### Additional Context
- `AGENTS.md` — Global agent rules
- Relevant quality policies in `org/4-quality/policies/`

## Interactions

### Produces
- <!-- define based on mission assignment -->

### Consumes
- <!-- define based on mission assignment -->

### Collaborates With
- <!-- varies by mission -->

### Escalates To
- Human division lead
- Layer escalation path

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- configure per workload --> |
| **Scaling trigger** | mission-assignment |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md`
- `policies/architecture.md`

### Evaluation Frequency
per-mission

### Performance Metrics
- Task completion rate
- Quality evaluation pass rate
- Escalation frequency

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-18 | Initial proposal — bootstrapped from Agentic Enterprise Blueprint | System |
