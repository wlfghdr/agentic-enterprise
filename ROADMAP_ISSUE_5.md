# Issue #5: Skills, MCP Profiles & Capability Contracts

> Implemented in: `org/skills/`, `org/mcp-profiles/`, `org/capability-contracts/`, `schemas/`  
> Documentation: [docs/CAPABILITY-CONTRACTS.md](docs/CAPABILITY-CONTRACTS.md)

## What Was Built

This roadmap item moves the framework beyond AGENT.md-only capability definitions to a structured, machine-readable system of **skill manifests**, **MCP tool profiles**, and **versioned capability contracts**.

### New Schemas

| Schema | Purpose |
|---|---|
| `schemas/skill-manifest.schema.json` | Defines what a skill is: inputs, outputs, permissions, constraints |
| `schemas/mcp-profile.schema.json` | Defines an MCP server's per-tool permission matrix per agent layer |
| `schemas/capability-contract.schema.json` | Binds agent types to approved skills + MCP profiles, versioned |

### New Registries

| Directory | Contents |
|---|---|
| `org/skills/` | 5 core skill manifests (PR review, code implementation, signal triage, quality evaluation, mission orchestration) |
| `org/mcp-profiles/` | GitHub MCP profile with full `permissions_matrix` (17 tools, risk-rated, layer-gated) |
| `org/capability-contracts/` | Contracts for `execution-builder` and `quality-pr-reviewer` agent types |

## Design Principles

1. **Least privilege by default** — tools are denied unless explicitly allowed.
2. **Versioned** — contracts increment on every permission change.
3. **Auditable** — `approved_by` and `changelog` in every contract.
4. **Schema-enforced** — CI validates all artifacts against JSON schemas.
5. **Layered** — permissions_matrix operates per agent layer, not per agent instance.

## Next Steps

- Extend `scripts/validate_schema.py` to cover the new schema targets.
- Add contracts for remaining agent types (steering, orchestration, ops).
- Add MCP profiles for additional servers (Jira, Slack, observability).
- Wire capability contracts into agent dispatch logic as runtime guards.
