# Schema Validation Guide

This document describes the schema validation system for core Agentic Enterprise framework artifacts.

## Overview

Two categories of artifacts are validated:

| Artifact | Schema | Validator |
|---|---|---|
| `CONFIG.yaml` | `schemas/config.schema.json` | JSON Schema (jsonschema) |
| `work/signals/*.md` | `schemas/work/signal.schema.json` | Custom markdown rules |
| `work/missions/**/mission-brief.md` | `schemas/work/mission-brief.schema.json` | Custom markdown rules |
| `work/releases/*release-contract*.md` | `schemas/work/release-contract.schema.json` | Custom markdown rules |

Validation runs automatically on every `push` and `pull_request` to `main` via the **Validate Schemas** CI job (`.github/workflows/validate.yml`).

---

## Schema Locations

```
schemas/
├── config.schema.json            # JSON Schema for CONFIG.yaml
└── work/
    ├── signal.schema.json        # Markdown schema for signal artifacts
    ├── mission-brief.schema.json # Markdown schema for mission briefs
    └── release-contract.schema.json  # Markdown schema for release contracts
```

---

## CONFIG.yaml Schema

`schemas/config.schema.json` is a [JSON Schema (draft-07)](https://json-schema.org/draft-07/json-schema-release-notes) document. It enforces:

- **`framework_version`** — required, must match `MAJOR.MINOR.PATCH` semver.
- **`company`** — required fields: `name`, `short_name`, `repo_slug`, `domain`.
- **`vision`** — required fields: `north_star`, `mission`.
- **`strategic_beliefs`** — at least one belief, each with `id`, `title`, `summary`.
- **`ventures`** — at least one venture, each with `id`, `name`, `description`.
- **`divisions`** — object of division arrays, each division with `id`, `name`, `description`.
- **`toolchain`** — required: `git_host` (one of `GitHub`, `GitLab`, `Bitbucket`), `ci_cd`.
- **`quality`** — required: `code_coverage_minimum` (0-100), `api_response_p95_ms`.

Unknown top-level keys are permitted (`additionalProperties: true`) to allow future extension.

---

## Work Artifact Schemas

Work artifact schemas are custom JSON documents interpreted by `scripts/validate_schema.py`. They support two rule types:

### `required_sections`
A list of `## Heading` names that must appear in the markdown file.

### `required_fields`
A list of inline field definitions. Each field entry supports:

| Key | Description |
|---|---|
| `name` | Human-readable field name (used in error messages) |
| `inline_pattern` | Regex to extract the field value from the markdown text |
| `allowed_values` | Optional list of permitted values (case-insensitive) |
| `id_pattern` | Optional regex the extracted value must fully match |
| `required` | `true` (default) — field must be present |

---

## Running Validation Locally

```bash
pip install pyyaml jsonschema
python3 scripts/validate_schema.py
```

Exit code `0` = all checks passed. Exit code `1` = validation failures.

---

## Adding or Updating a Schema

### CONFIG.yaml Schema
Edit `schemas/config.schema.json` following JSON Schema draft-07 conventions. Test locally with `python3 scripts/validate_schema.py`.

### Work Artifact Schemas
Edit the relevant file under `schemas/work/`. The custom schema keys are:

```json
{
  "artifact_type": "markdown",
  "filename_pattern": "<regex for the filename>",
  "required_sections": ["Section Name", ...],
  "required_fields": [
    {
      "name": "Field Label",
      "inline_pattern": "\\*\\*Field Label:\\*\\*\\s*([^|\\n]+)",
      "allowed_values": ["value1", "value2"],
      "id_pattern": "^PREFIX-\\d{4}-\\d{3,}$",
      "required": true
    }
  ]
}
```

### Adding a New Artifact Type
1. Create `schemas/work/<artifact-type>.schema.json`.
2. Add a discovery function and validation call in `scripts/validate_schema.py`.
3. Update this document.

---

## CI Integration

The `validate-schema` job in `.github/workflows/validate.yml` installs `pyyaml` and `jsonschema`, then runs `python3 scripts/validate_schema.py`. The job fails if any schema violation is detected, blocking merge to `main`.

Template files (`_TEMPLATE-*.md`) and `README.md` files are automatically excluded from work-artifact validation.
