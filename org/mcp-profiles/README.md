# MCP Tool Profiles Registry

Each file in this directory is an **MCP profile** — a declarative definition of a Model Context Protocol server, including its permission matrix per agent layer.

## Schema

All profiles must conform to [`schemas/mcp-profile.schema.json`](../../schemas/mcp-profile.schema.json).

## Naming Convention

```
<profile-id>.mcp-profile.json
```

Example: `github.mcp-profile.json`

## Lifecycle

1. Propose a new MCP profile via PR.
2. Security review required for any `risk_level: high` or `critical` tools.
3. Steering Layer approves permission matrix.
4. Once merged, the profile can be referenced in skill manifests and capability contracts.

## Permission Matrix Rules

- **allowed_layers**: Agent layers that may invoke the tool by default.
- **denied_layers**: Explicit deny overrides — always wins over `allowed_layers`.
- **requires_approval**: Human must approve before the tool can be invoked.

Principle of least privilege: default to the narrowest `allowed_layers` that enables the use case.

## Index

| Profile ID | Type | Description |
|---|---|---|
| `github` | npm/stdio | GitHub MCP server — repository, PR, and issue operations |
