# Agent Type Registry

> **What this is:** The governed, versioned registry of all agent types in the {{COMPANY_SHORT}} agentic enterprise. Each agent type has a YAML definition file that describes its capabilities, lifecycle status, scaling parameters, and ownership.  
> **Governance:** New agent types require Steering Layer evaluation and CTO approval via PR. This registry is the operational source of truth for all agent types.

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

| Status | Meaning | Operational Rules |
|--------|---------|-------------------|
| **proposed** | Agent type proposal submitted, awaiting Steering review | Cannot be referenced in fleet configs. No instances may be provisioned. |
| **approved** | CTO approved, awaiting implementation | Cannot be referenced in fleet configs. Implementation work may begin. |
| **implementing** | Skills, tools, and instructions being built | Cannot be referenced in fleet configs. Test instances allowed in non-production environments only. |
| **active** | Deployed and available for fleet assignment | **Only `active` agent types may be assigned to crews in fleet configs.** Production instances allowed. |
| **deprecated** | Still running but superseded; no new assignments | **Fleet configs must NOT reference deprecated types.** Existing running instances may continue until their current mission completes, but no new assignments are permitted. Orchestration Layer must migrate to the replacement type. |
| **retired** | Decommissioned, definition kept for audit | No instances may run. Definition file remains in the registry for audit trail. Fleet configs referencing retired types will fail CI validation. |

### Lifecycle Transition Approvals

| Transition | Who Approves | Required Evidence |
|------------|-------------|-------------------|
| proposed → approved | CTO (via PR merge) | Quality Layer evaluation of proposal boundaries and safety constraints |
| approved → implementing | Automatic (on PR merge of approved status) | — |
| implementing → active | CTO (via PR merge) | Quality validation report confirming capabilities, safety constraints, and policy compliance |
| active → deprecated | CTO (via PR merge) | Evolution proposal documenting replacement type and migration plan |
| deprecated → retired | CTO (via PR merge) | Confirmation that no fleet configs reference this type and no instances are running |

### Deprecation Rules

- A deprecated agent type **must** have a `superseded_by` field pointing to the replacement agent type ID
- The Orchestration Layer is responsible for migrating fleet configs from the deprecated type to the replacement type
- Deprecation does not mean immediate shutdown — existing missions using the deprecated type may complete their current work
- The Steering Layer sets the **migration deadline** (typically 30-90 days) in the evolution proposal
- After the migration deadline, the type transitions to `retired`

### Retirement Process

- **When to retire (vs. keep deprecated):** Retire when all fleet configs have been migrated and no instances are running. Deprecation is a transition state, not a permanent one.
- **Retirement does not delete the file.** The definition file stays in the registry with `status: retired` for audit trail and historical reference.
- **Archived definitions** may be moved to a `retired/` subdirectory within the layer folder if the active registry becomes cluttered — this is optional and at Steering Layer discretion.

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
| **OPERATING-MODEL.md** | Documents the design principles and organizational structure that inform agent type design. |
| **Division definitions** (`org/3-execution/divisions/`) | Divisions define domain context. Agent types define capabilities. An agent type belongs to a division (for Execution agents) or to a layer. |
| **AGENT.md files** (`org/<layer>/AGENT.md`) | Layer instructions define behavioral rules. Agent type definitions specify capabilities & scaling. Both are needed for a complete agent specification. |
