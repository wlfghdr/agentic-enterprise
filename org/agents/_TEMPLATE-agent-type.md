# Agent Type Definition: [Agent Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Governed registry entry for a single agent type.**  
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | _(unique identifier, e.g., "steering-signal-scanner")_ |
| **Name** | _(human-readable name, e.g., "Customer Signal Scanner")_ |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | _(steering / strategy / orchestration / execution / quality)_ |
| **Division** | _(division ID — required for execution agents, optional otherwise)_ |
| **Category** | _(e.g., "signal-processing", "code-generation", "evaluation")_ |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | proposed _(proposed / approved / implementing / active / deprecated / retired)_ |
| **Proposed date** | YYYY-MM-DD |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | |
| **Retired date** | |
| **Superseded by** | _(agent type ID that replaces this one, if deprecated)_ |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | |
| **Contact** | _(primary human contact)_ |
| **Approved by** | _(e.g., "CTO")_ |

## Description

**What this agent does:**  
_(one-paragraph description)_

**Problem solved:**  
_(what capability gap or problem this agent addresses)_

**Value proposition:**  
_(why the enterprise needs this agent type)_

## Capabilities

### Skills
- _(e.g., "code-review", "test-generation")_

### MCP Servers
- _(e.g., "github", "jira", "slack")_

### Tool Access
- _(e.g., "git", "ci-cd-pipeline", "observability-api")_

### Languages
- _(programming languages for code agents, e.g., "python", "typescript")_

### Data Access
- _(e.g., "crm", "support-tickets", "telemetry")_

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | _(e.g., "org/0-steering/AGENT.md")_ |
| **Division DIVISION.md** | _(e.g., "org/3-execution/divisions/core-api/DIVISION.md")_ |

### Additional Context
- _(additional instruction files this agent must read)_

## Interactions

### Produces
- _(artifact types this agent produces, e.g., "signal", "quality-evaluation-report")_

### Consumes
- _(artifact types this agent consumes, e.g., "mission-brief", "fleet-config")_

### Collaborates With
- _(other agent type IDs this agent frequently interacts with)_

### Escalates To
- _(human roles or agent types for escalation)_

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 _(0 = on-demand only)_ |
| **Max instances** | 1 |
| **Scaling trigger** | _(e.g., "mission-assignment", "signal-volume > 50/day")_ |
| **Cost class** | _(light / medium / heavy)_ |

## Quality

### Applicable Policies
- _(e.g., "security", "architecture")_

### Evaluation Frequency
_(e.g., "per-PR", "weekly")_

### Performance Metrics
- _(e.g., "pr-acceptance-rate", "eval-accuracy")_

## Changelog

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | | |
---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
