# Agent Type Definition: Feature Flag Agent

> **Status:** deprecated | **Proposed date:** 2026-02-18
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-feature-flag-agent` |
| **Name** | Feature Flag Agent |
| **Version** | 1.1.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `engineering-foundation` |
| **Category** | feature-management |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | deprecated |
| **Proposed date** | 2026-02-18 |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | 2026-03-07 |
| **Retired date** | |
| **Superseded by** | `exec-deploy-agent` |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | <!-- assign during approval --> |
| **Contact** | <!-- primary human contact --> |
| **Approved by** | <!-- CTO or delegate --> |

## Description

**What this agent does:**
Historically proposed as a standalone execution agent for feature flag lifecycle management.

**Problem solved:**
Progressive delivery and experimentation are essential for managing risk in modern software.

**Value proposition:**
The capability is still broadly useful, but the framework now treats feature flag management as a `deploy-agent` capability by default rather than a separate base-template agent type.

## Capabilities

### Skills
- feature-management

### MCP Servers
- <!-- configure per enterprise toolchain -->

### Tool Access
- <!-- configure per enterprise toolchain -->

### Languages
- <!-- configure per implementation -->

### Data Access
- <!-- configure per data architecture -->

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/engineering-foundation/DIVISION.md` |

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
| 2026-03-07 | Deprecated in the base template; feature flag management is now treated as a Deploy Agent capability | GitHub Copilot |
| 2026-02-18 | Initial proposal — bootstrapped from Agentic Enterprise Blueprint | System |
