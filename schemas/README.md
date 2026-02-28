# Schemas

This directory contains schema definitions for core Agentic Enterprise framework artifacts.

| File | Target | Validator |
|---|---|---|
| `config.schema.json` | `CONFIG.yaml` | JSON Schema (draft-07) via `jsonschema` |
| `work/signal.schema.json` | `work/signals/*.md` | Custom markdown rules |
| `work/mission-brief.schema.json` | `work/missions/**/BRIEF.md` | Custom markdown rules |
| `work/release-contract.schema.json` | `work/releases/*release-contract*.md` | Custom markdown rules |

## How Validation Works

`scripts/validate_schema.py` runs during CI (`validate-schema` job in `.github/workflows/validate.yml`) and locally:

```bash
pip install pyyaml jsonschema
python3 scripts/validate_schema.py
```

## Adding a New Schema

See [docs/SCHEMA-GUIDE.md](../docs/SCHEMA-GUIDE.md) for the full contribution workflow.

## Capability Contract Schemas (Issue #5)

Three new schemas support the skills/tools/MCP profiles system:

| File | Target | Description |
|---|---|---|
| `skill-manifest.schema.json` | `org/skills/*.skill.json` | Declarative skill manifests |
| `mcp-profile.schema.json` | `org/mcp-profiles/*.mcp-profile.json` | MCP server permission matrices |
| `capability-contract.schema.json` | `org/capability-contracts/*.contract.json` | Versioned capability contracts per agent type |

See [docs/CAPABILITY-CONTRACTS.md](../docs/CAPABILITY-CONTRACTS.md) for the full design.
