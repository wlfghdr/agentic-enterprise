# Connector Pattern — MCP/A2A/Business Systems

> **Version:** 1.0 | **Last updated:** 2026-03-07
> **Scope:** External system integrations for agentic-enterprise adopters

## Purpose

This pattern defines a safe, auditable way to connect agents to real enterprise systems
(Jira, ServiceNow, CRM, CI/CD, observability, communication platforms) using open protocols
and governed activation.

## Design Principles

1. **Registry-first, never ad-hoc**
   - Every connector must be registered in `org/integrations/` and `CONFIG.yaml`.
2. **Read-only first**
   - New connectors begin in read-only mode before any side effects are allowed.
3. **Policy-gated side effects**
   - Write/update/delete actions require explicit policy mapping and approval mode.
4. **Observable by default**
   - Every connector call emits telemetry with actor, target system, operation, and outcome.
5. **Human escalation path**
   - High-impact actions must support approve/reject/escalate decisions.

## Reference Architecture

```text
Agent Runtime
  ├─ Connector Adapter (MCP or A2A client/server)
  ├─ Policy Guard (allow/deny/escalate)
  ├─ Secret Provider (token retrieval only, no inline secrets)
  └─ Telemetry Emitter (OTel spans/events)
         │
         ▼
External Systems (Jira / ServiceNow / CRM / CI/CD / Messaging / etc.)
```

## Pattern Selection

| Pattern | Best for | Notes |
|---|---|---|
| MCP | Tool-like access from agents to external systems | Preferred default for agent tool interfaces |
| A2A | Agent-to-agent delegation between systems | Use when responsibility crosses system boundaries |
| Native API/Webhook | Legacy systems without MCP/A2A support | Wrap behind connector adapter + policy guard |

## Connector Capability Levels

| Level | Capability | Allowed operations | Approval |
|---|---|---|---|
| L1 | Observe | Read/list/query only | Not required |
| L2 | Assist | Draft/propose actions, no execution | Optional |
| L3 | Act (bounded) | Approved writes in scoped resources | Required |
| L4 | Act (privileged) | Cross-system or destructive actions | Mandatory human approval |

## Security & Governance Requirements

A connector is eligible for activation only if it defines:

- authentication model (OAuth/service account/API key + rotation owner)
- data classification for payloads and responses
- side-effect level (`none`, `low`, `high`)
- failure behavior (fail-closed vs degraded read-only)
- audit trail fields (who/what/when/result)
- quality policy mapping in `org/4-quality/policies/`

## Minimal Delivery Sequence (recommended)

1. **Foundation:** register connector + architecture/security metadata
2. **Read-only rollout:** enable L1/L2 capabilities and validate observability
3. **Controlled writes:** enable selected L3 actions with explicit approvals
4. **Privileged actions:** enable L4 only after policy and risk review

## Starter Connector Backlog (read-only)

- Jira: issue read/search
- ServiceNow: incident read/search
- GitHub: issue/PR read
- CRM: account/opportunity read
- Observability: dashboards/query read

These can be implemented incrementally without introducing external side effects.
