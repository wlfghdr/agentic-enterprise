# Agent Type Definition: Observability Compliance Agent

> **Status:** proposed | **Proposed date:** 2026-02-19
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `quality-observability-compliance-agent` |
| **Name** | Observability Compliance Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | quality |
| **Division** | `—` |
| **Category** | observability-compliance |

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
| **Owning team** | <!-- assign during approval --> |
| **Contact** | <!-- primary human contact --> |
| **Approved by** | <!-- CTO or delegate --> |

## Description

**What this agent does:**
Evaluates every outcome — code, agent, workflow, pipeline, service, or artifact — against the observability policy. Issues PASS or FAIL verdicts. Blocks promotion of any output that lacks verified instrumentation. Acts as the automated enforcement layer for the [Observable by Default](../../4-quality/policies/observability.md) mandate.

**Problem solved:**
Observability compliance has historically been a manual checklist item, reviewed inconsistently at PR review. At agent fleet scale, with hundreds of agents producing outputs continuously, manual compliance checking is impractical. Uninstrumented components reach production undetected, creating blind spots in incident response, audit trails, and organizational health monitoring.

**Value proposition:**
- Every output that passes this agent is guaranteed to have verified telemetry flowing before it ships
- Continuous evaluation (not just at PR time) catches observability regressions as fleets evolve
- Generates improvement signals when systemic observability gaps are detected across divisions
- Closes the feedback loop: agent activity data feeds the observability platform, which feeds this agent's evaluation context

## Capabilities

### Skills
- observability-compliance-evaluation
- telemetry-verification
- otel-instrumentation-review
- git-webhook-coverage-check

### MCP Servers
- Observability platform MCP server (query telemetry data to verify instrumentation is active)
- Git host MCP server (verify webhook configuration)

### Tool Access
- Read access to all component code (instrumentation verification)
- Read access to observability platform dashboards and telemetry data (via MCP)
- Read access to CONFIG.yaml (verify registered observability integrations)
- Read access to all quality policies

### Languages
- <!-- configure per implementation -->

### Data Access
- all-component-outputs
- observability-platform-telemetry
- git-webhook-config
- release-contracts
- fleet-configs

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/4-quality/AGENT.md` |
| **Division DIVISION.md** | `—` |

### Additional Context
- `AGENTS.md` — Global agent rules, Rule 9 (emit activity telemetry)
- `org/4-quality/policies/observability.md` — The policy this agent enforces
- `org/integrations/categories/observability.md` — Integration patterns and configuration

## Evaluation Protocol

For every output under evaluation, this agent performs the following checks in order:

### 1. Instrumentation Presence (Static)
- Verify instrumentation code exists for the component type (OTel SDK, APM agent, or API ingest)
- Verify span attributes include mandatory fields: `agent.name`, `agent.layer`, `agent.mission_id`, `agent.tool`
- Verify structured logging with trace ID correlation is present
- Verify external calls are wrapped in spans
- **FAIL immediately** if no instrumentation code is present

### 2. Telemetry Flow Verification (Dynamic)
- Query the registered observability integration (via MCP) to verify telemetry is actively flowing from the component in staging
- Verify traces are present for at least one representative operation
- Verify RED metrics are exposed for all endpoints
- Verify logs contain trace IDs and are structured JSON
- **FAIL** if telemetry is not confirmed flowing within 5 minutes of staging deployment

### 3. Git Webhook Coverage
- Verify git webhooks are configured for the repository (query git host MCP)
- Verify PR lifecycle events are reaching the observability integration
- **FAIL** if webhooks are missing or events are not flowing

### 4. SLO and Alerting Readiness (for Ship-time evaluation)
- Verify SLOs are defined and configured in the observability platform
- Verify at least one burn rate alert is active
- Verify a service health dashboard exists and is linked in the catalog
- **FAIL** if SLOs or dashboards are absent at ship time

### 5. Agent Fleet Observability (for agent components)
- Verify every agent action produces spans with mandatory attributes (per AGENTS.md Rule 9)
- Verify error traces capture tool failures, policy violations, and escalation triggers
- Verify token usage is attributed to mission and division
- **FAIL** if agent actions are untraced

## Interactions

### Produces
- Quality evaluation reports: `work/missions/<mission-name>/evaluations/YYYY-MM-DD-observability-compliance.md`
- BLOCK signals to PR review queue (FAIL verdicts)
- Improvement signals when systemic observability gaps detected: `work/signals/`

### Consumes
- Component code and configuration (instrumentation check)
- Observability platform telemetry data (via MCP)
- Release contracts (ship-time evaluation context)
- Fleet configs (agent type verification context)
- CONFIG.yaml (registered integration endpoints)

### Collaborates With
- Architecture Review Agent (observability as architectural concern)
- Delivery Evaluator (observability as release gate)
- Production Readiness Evaluator (observability as production prerequisite)
- Orchestration Layer (fleet dashboards, telemetry routing)

### Escalates To
- Human Architecture Governor (novel instrumentation patterns with no established approach)
- Operations lead (observability platform connectivity issues)
- Layer escalation path

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 1 (always-on for continuous compliance monitoring) |
| **Max instances** | <!-- configure per workload --> |
| **Scaling trigger** | mission-assignment, PR-opened, scheduled (daily fleet scan) |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/observability.md` — Primary enforcement target
- `policies/architecture.md` — Architecture compliance cross-check
- `policies/security.md` — No PII in telemetry
- `policies/delivery.md` — Observability as a release gate

### Evaluation Frequency
- per-PR (triggered on every PR that contains code or configuration changes)
- per-release (ship-time gate)
- daily (fleet-wide scan for regressions)

### Performance Metrics
- Observability coverage rate (% of components with verified telemetry)
- Mean time to detect observability regression (from regression introduced to FAIL verdict)
- False positive rate (FAIL verdicts overturned by human review)
- Escalation frequency

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-19 | Initial proposal — observability as a first-class quality gate | System |
