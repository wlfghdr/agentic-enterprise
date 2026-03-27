# Agent Type Registry

> **Version:** 1.2 | **Last updated:** 2026-03-27

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

## What Belongs In The Base Template

Base-template agent types should pass all of these checks:

1. **Universal enough** — most adopting companies will plausibly need this capability.
2. **Stable boundary** — the agent owns a durable workflow boundary, not a single step inside another agent's workflow.
3. **More than a tool wrapper** — the capability is not just one feature flag system, one rollout mode, or one API binding.
4. **More than a task name** — names like "blog", "rollback", or "battlecard" are often outputs or skills, not durable agent types.
5. **Configuration is insufficient** — if an existing agent can handle the work with a division profile, tool profile, or skill set, prefer configuration over a new registry entry.

## Use Configuration Instead Of New Types When

- The difference is only environment-specific, such as one cloud provider, one monitoring backend, or one feature flag platform.
- The difference is only a delivery step inside a broader workflow, such as canary analysis or rollback inside deployment.
- The difference is only channel or artifact format, such as blog vs battlecard vs release notes inside content production.
- The difference is only team specialization, such as frontend vs backend coding profiles inside one coding fleet.

## Common Anti-Patterns

- **Task-level agent types** — one agent for onboarding, another for renewal, another for advocacy, even though one cleaner domain boundary would suffice.
- **Tool-level agent types** — one agent exists mainly because a feature flag, canary, or rollback tool exists.
- **Monitor explosion** — separate host, process, network, and container monitors when one infrastructure-health monitor with pluggable scopes would do.
- **Governance leakage** — execution-layer agent types quietly take on policy ownership that belongs in the Quality Layer.

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

## Agent Identity & Access Governance

Agent types are not just capability bundles. They are also **governed non-human identities** with explicit operational boundaries.

Every agent type definition should answer these questions in a reviewable way:

1. **Who is this agent in the enterprise?**
   - Stable agent type ID and human owner
   - Layer and division placement
   - Intended operating boundary
2. **What credentials or execution identity does it use?**
   - Named runtime principal, service account, workload identity, or equivalent
   - Whether credentials are shared, per-agent-type, or ephemeral per mission
3. **What may it touch?**
   - Declared tools, MCP profiles, data classes, and environments
   - Explicit write/delete authority where applicable
4. **What constrains blast radius?**
   - Approval gates for high-impact actions
   - Environment restrictions (for example: read-only prod, write in staging only)
   - Escalation path when the requested action exceeds scope
5. **How is it audited?**
   - Telemetry linked to agent identity
   - Traceable commits, tool calls, approvals, and secret access

### Minimum Identity Questions For New Agent Types

Before approving a new agent type, reviewers should be able to verify:

- Which **runtime identity** the agent operates as
- Which **credential source** issues that identity (for example KMS-backed secret, OAuth client, workload identity)
- Whether credentials are **scoped per agent type** or reused across types
- Which **environments** the agent may read, write, or administer
- Which **data classifications** the agent may access
- Which actions require **per-mission human approval**
- How the enterprise will detect **privilege escalation or scope drift** via telemetry

### Relationship To MCP Profiles And Capability Contracts

- **MCP profiles** govern what an external tool integration can do in principle.
- **Capability contracts** bind a specific agent type to approved skills, MCP profiles, and knowledge scope.
- **Agent type definitions** declare the identity, ownership, access boundary, and escalation model for the non-human actor itself.

These are complementary controls. A tool profile alone does **not** answer which identity an agent runs as or how its credentials are bounded.

## Relationship to Other Artifacts

| Artifact | Relationship |
|----------|-------------|
| **Fleet configs** (`org/2-orchestration/fleet-configs/`) | Fleet configs reference agent types from this registry by `id`. Only `active` agent types may be assigned to crews. |
| **Capability contracts** (`org/capability-contracts/`) | Capability contracts approve the specific skills, MCP profiles, and knowledge sources an agent type may use. They do not replace identity ownership or runtime-boundary documentation in the registry. |
| **MCP profiles** (`org/mcp-profiles/`) | MCP profiles define tool-side permissions. Agent type definitions define the non-human identity that receives and uses those permissions. |
| **org/README.md** | Documents the design principles and organizational structure that inform agent type design. |
| **Division definitions** (`org/3-execution/divisions/`) | Divisions define domain context. Agent types define capabilities. An agent type belongs to a division (for Execution agents) or to a layer. |
| **AGENT.md files** (`org/<layer>/AGENT.md`) | Layer instructions define behavioral rules. Agent type definitions specify capabilities, identity boundaries, and scaling. Both are needed for a complete agent specification. |

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-03-27 | Added agent identity & access governance guidance clarifying that agent type definitions must document runtime identity, credential boundaries, environments, data access, approval gates, and auditability. |
| 1.1 | 2026-03-07 | Added base-template fit criteria, configuration-vs-type guidance, and anti-patterns to reduce micro-specialized agent definitions |
| 1.0 | 2026-02-23 | Initial version |
