# Agent Type Definition: Cross-Mission Coordinator

> **Status:** proposed | **Proposed date:** 2026-02-18
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `orch-cross-mission-coordinator` |
| **Name** | Cross-Mission Coordinator |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | orchestration |
| **Division** | `—` |
| **Category** | dependency-management |

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
Detects dependency conflicts across concurrent initiatives, proposes sequencing strategies, and manages shared resource contention.

**Problem solved:**
Organizations run many things in parallel. Without coordination, they collide.

**Value proposition:**
Every enterprise following the agentic operating model benefits from this agent because it addresses a universal organizational need that scales with agent fleet adoption.

## Capabilities

### Skills
- dependency-management

### MCP Servers
- <!-- configure per enterprise toolchain -->

### Tool Access
- <!-- configure per enterprise toolchain -->

### Languages
- <!-- configure per implementation -->

### Data Access
- mission-data
- dependency-graphs
- resource-utilization

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/2-orchestration/AGENT.md` |
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
