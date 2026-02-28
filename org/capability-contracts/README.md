# Capability Contracts Registry

A **capability contract** is a versioned, approved record binding an agent type to specific skills and MCP profiles.

## Schema

All contracts must conform to [`schemas/capability-contract.schema.json`](../../schemas/capability-contract.schema.json).

## Naming Convention

```
<agent-type-id>.contract.json
```

Example: `execution-builder.contract.json`

## Lifecycle

1. Propose a new or updated contract via PR.
2. Changes to any `mcp_profiles` entry or permission upgrade require **human approval** before merge.
3. On approval and merge, the contract becomes active.
4. Previous contract versions are preserved in `changelog`.
5. Contracts must be reviewed on expiry or when the agent type's scope changes.

## Index

| Agent Type | Contract Version | Status | Effective |
|---|---|---|---|
| `execution-builder` | 1.0.0 | active | 2026-02-28 |
| `quality-pr-reviewer` | 1.0.0 | active | 2026-02-28 |
