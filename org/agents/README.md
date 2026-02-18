# Agent Type Registry

> **What this is:** The governed, versioned registry of all agent types in the {{COMPANY_SHORT}} agentic enterprise. Each agent type has a YAML definition file that describes its capabilities, lifecycle status, scaling parameters, and ownership.  
> **Governance:** New agent types require Steering Layer evaluation and CTO approval via PR. The Agentic Enterprise Blueprint (`AGENTIC-ENTERPRISE-BLUEPRINT.md`) serves as the reference catalog; this registry is the operational source of truth.

---

## Structure

```
org/agents/
├── README.md                  ← You are here
├── _TEMPLATE-agent-type.md    ← Template for new agent type definitions
├── steering/                  ← Steering Layer agent types
├── strategy/                  ← Strategy Layer agent types
├── orchestration/             ← Orchestration Layer agent types
├── execution/                 ← Execution Layer agent types
└── quality/                   ← Quality Layer agent types
```

## Agent Type Lifecycle

```
proposed → approved → implementing → active → deprecated → retired
```

| Status | Meaning |
|--------|---------|
| **proposed** | Agent type proposal submitted, awaiting Steering review |
| **approved** | CTO approved, awaiting implementation |
| **implementing** | Skills, tools, and instructions being built |
| **active** | Deployed and available for fleet assignment |
| **deprecated** | Still running but superseded; no new assignments |
| **retired** | Decommissioned, definition kept for audit |

## How to Propose a New Agent Type

1. File a signal in `work/signals/` identifying the capability gap
2. Use the template: `org/agents/_TEMPLATE-agent-type-proposal.md`
3. Submit as a Pull Request — Steering Layer evaluates, Quality Layer reviews boundaries
4. On CTO approval: create the registry entry using `org/agents/_TEMPLATE-agent-type.md`
5. Implementation begins (skills, MCP connections, tool bindings, instructions)
6. Quality validation → status updated to `active`

## How to Deprecate an Agent Type

1. File an evolution proposal (see `org/0-steering/_TEMPLATE-evolution-proposal.md`)
2. Document the replacement agent type or capability that supersedes it
3. On CTO approval: update registry entry status to `deprecated`
4. After migration period: update to `retired`

## Who Does What

| Activity | Owner | Approver |
|----------|-------|----------|
| **Propose new agent type** | Any layer (typically Execution divisions) | Steering Layer (CTO) |
| **Design agent capabilities** | Execution divisions (domain experts) + Orchestration | Quality Layer (review) |
| **Approve agent type** | Steering Layer | CTO |
| **Provision instances** | Orchestration Layer (Agent Fleet Managers) | — |
| **Scale instances up/down** | Orchestration Layer | CTO + CFO (for cost-significant changes) |
| **Deprecate agent type** | Steering Layer | CTO |
| **Monitor agent performance** | Orchestration Layer (fleet metrics) + Steering (meta-optimization) | — |

## Relationship to Other Artifacts

| Artifact | Relationship |
|----------|-------------|
| **Fleet configs** (`org/2-orchestration/fleet-configs/`) | Fleet configs reference agent types from this registry by `id`. Only `active` agent types may be assigned to crews. |
| **Blueprint** (`AGENTIC-ENTERPRISE-BLUEPRINT.md`) | The Blueprint is the reference catalog of universal agent types. This registry is the governed, versioned source of truth for the deployed agent landscape. |
| **Division definitions** (`org/3-execution/divisions/`) | Divisions define domain context. Agent types define capabilities. An agent type belongs to a division (for Execution agents) or to a layer. |
| **AGENT.md files** (`org/<layer>/AGENT.md`) | Layer instructions define behavioral rules. Agent type definitions specify capabilities & scaling. Both are needed for a complete agent specification. |
