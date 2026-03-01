# Capability Contracts: Skills, MCP Profiles, and Permission Governance

> **Status:** Active — introduced in [#5](https://github.com/wlfghdr/agentic-enterprise/issues/5)  
> **Replaces:** ad-hoc Capabilities sections in agent type definitions (AGENT.md-only approach)

---

## Overview

The Agentic Enterprise framework moves beyond freeform `AGENT.md` markdown for capability definition. Instead, capabilities are declared in **three structured, versioned artifacts**:

| Artifact | Location | Purpose |
|---|---|---|
| **Skill manifest** | `org/skills/<id>.skill.json` | What an agent can *do* — inputs, outputs, permission level |
| **MCP profile** | `org/mcp-profiles/<id>.mcp-profile.json` | Tool-level permission matrix per MCP server, per agent layer |
| **Capability contract** | `org/capability-contracts/<id>.contract.json` | Binding record: agent type ↔ skills ↔ MCP profiles, versioned and approved |

All three artifact types are governed by JSON schemas in `schemas/`.

---

## Why This Matters

| Problem (AGENT.md only) | Solution |
|---|---|
| Capabilities are prose — no machine-readable enforcement | JSON schemas enable CI validation |
| No version history for what an agent was allowed to do | Contracts have `contract_version` and `changelog` |
| Permission drift — agents accumulate access over time | Explicit `tool_overrides` and `denied_layers` in contracts |
| No audit trail — who approved what, when? | `approved_by` field in contracts |
| MCP tool access undocumented | `permissions_matrix` in MCP profiles defines every tool |

---

## The Three Layers

### 1. Skill Manifests (`org/skills/`)

A skill is a named, versioned capability. It describes:

- **What the agent does** (description, category)
- **What it consumes and produces** (inputs, outputs)
- **Minimum permissions required** (permissions.level)
- **Which MCP servers are needed** (mcp_servers)
- **Hard constraints** — rules that must hold when the skill is active

Skills are **reusable**: multiple agent types can reference the same skill.

**Example: `github-pr-review`**
- Category: `code-review`
- Permissions: `read-write` (read diffs, post comments)
- Constraint: _"Must not approve PRs that modify policy/ without human approval."_

### 2. MCP Tool Profiles (`org/mcp-profiles/`)

An MCP profile captures everything about a single MCP server:

- **Server configuration** (type, transport, env vars)
- **Permissions matrix** — one entry per tool the server exposes:
  - `allowed_layers`: which agent layers may call this tool
  - `denied_layers`: explicit denies (wins over allowed)
  - `risk_level`: low / medium / high / critical
  - `requires_approval`: must a human approve before invocation?
  - `constraints`: invariants that apply at the tool level

The default stance is **least privilege**. If a tool isn't listed, it's denied.

**Example: `github` MCP profile (excerpts)**

| Tool | Allowed Layers | Risk | Approval? |
|---|---|---|---|
| `get_file_contents` | all | low | no |
| `create_pull_request` | execution | medium | no |
| `merge_pull_request` | _(none)_ | high | **yes** |
| `delete_file` | _(none)_ | critical | **yes** |
| `push_files` | execution | high | no |

### 3. Capability Contracts (`org/capability-contracts/`)

A contract is the final binding record. It:

- Names the **agent type** it applies to
- Lists the exact **skill versions** granted
- Lists the exact **MCP profile versions** granted
- May add **tool_overrides** to restrict further (never to expand)
- Records **approval**: who approved it and when
- Has a **version** — increment on any change

Contracts are the authoritative source of truth for what a running agent is allowed to do.

---

## Governance Flow

```
1. Developer proposes new skill or MCP profile → PR
2. Security review for high/critical risk tools
3. Steering Layer approves permission matrix
4. Capability contract updated to reference new skill/profile
5. Contract version incremented, approved_by updated
6. CI validates all JSON schemas pass
7. PR merged → contract active
```

**Golden rule:** Capability expansion always requires a PR and approval. Restriction can be done unilaterally.

---

## Integration with Agent Type Definitions

Existing agent type definition files (`org/agents/<layer>/<type>.md`) retain their `## Capabilities` section, but it now becomes a **reference** rather than the authoritative definition:

```markdown
## Capabilities

> Authoritative capability contract: [`org/capability-contracts/execution-builder.contract.json`](../org/capability-contracts/execution-builder.contract.json)

### Skills (summary)
- `github-code-implementation` v1.0.0

### MCP Profiles (summary)
- `github` v1.0.0

_For the full permission matrix, see the contract and MCP profile files._
```

---

## CI Validation

The existing `scripts/validate_schema.py` is extended to validate skill manifests, MCP profiles, and capability contracts against their schemas. CI will fail if any artifact violates its schema.

Add to `scripts/validate_schema.py` (see [SCHEMA-GUIDE.md](SCHEMA-GUIDE.md)):

```
org/skills/*.skill.json          → schemas/skill-manifest.schema.json
org/mcp-profiles/*.mcp-profile.json → schemas/mcp-profile.schema.json
org/capability-contracts/*.contract.json → schemas/capability-contract.schema.json
```

---

## Quick Reference

### Adding a New Skill

1. Copy `org/agents/_TEMPLATE-agent-type.md` pattern → create `org/skills/<id>.skill.json`
2. Validate: `python3 scripts/validate_schema.py`
3. Add to `org/skills/README.md` index
4. Open PR for approval

### Adding a New MCP Server

1. Create `org/mcp-profiles/<id>.mcp-profile.json`
2. List every tool the server exposes in `permissions_matrix`
3. Default all tools to `allowed_layers: []` + `requires_approval: true`, then relax deliberately
4. Open PR for security review

### Granting an Agent Type a New Capability

1. Update or create `org/capability-contracts/<agent-type-id>.contract.json`
2. Increment `contract_version`
3. Add entry to `changelog` with `approved_by`
4. Open PR — human approval required before merge

---

*See also:* [SCHEMA-GUIDE.md](SCHEMA-GUIDE.md) | [OPERATING-MODEL.md](../OPERATING-MODEL.md) | [MCP Specification](https://github.com/modelcontextprotocol/specification)
