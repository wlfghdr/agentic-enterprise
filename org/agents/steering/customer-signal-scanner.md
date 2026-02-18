# Agent Type Definition: Customer Signal Scanner

> **Status:** proposed | **Proposed date:** 2026-02-18
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `steering-customer-signal-scanner` |
| **Name** | Customer Signal Scanner |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | steering |
| **Division** | `—` |
| **Category** | signal-processing |

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
Continuously monitors CRM data, support tickets, customer meetings, and market feedback to detect emerging patterns and converging demand signals.

**Problem solved:**
Without systematic signal detection, strategic opportunities are missed or noticed too late. This is the enterprise's early warning system.

**Value proposition:**
Every enterprise following the agentic operating model benefits from this agent because it addresses a universal organizational need that scales with agent fleet adoption.

## Capabilities

### Skills
- signal-processing

### MCP Servers
- <!-- configure per enterprise toolchain -->

### Tool Access
- <!-- configure per enterprise toolchain -->

### Languages
- <!-- configure per implementation -->

### Data Access
- crm
- support-tickets
- market-data

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/0-steering/AGENT.md` |
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
