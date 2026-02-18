# Division: {{DIVISION_NAME}}

> **Owner:** {{DIVISION_LEAD}}  
> **Type:** Core | Domain | Operations | GTM | Customer  
> **Layer:** Execution  
> **Status:** Active | Proposed | Deprecated

---

## Purpose

One-paragraph description of what this division does and why it exists.

## Scope

### In Scope
- What this division owns and is responsible for

### Out of Scope
- What explicitly does NOT belong to this division
- Where the boundary lies with adjacent divisions

## Key Responsibilities

1. **Responsibility 1** — Description
2. **Responsibility 2** — Description
3. **Responsibility 3** — Description

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | {{ADJACENT_DIVISION}} | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- Add other relevant policies

## Human Checkpoints

These decisions require human division lead involvement:

- Architecture-changing proposals
- New external integrations
- Customer-impacting schema changes
- Work that crosses division boundaries

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Check the Software Catalog for existing services before creating new ones
3. Follow established code patterns in this division's codebase
4. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
5. Register new components via `process/templates/component-onboarding.md`

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Source code | `{{REPO_URL}}` | Main repository |
| Documentation | `{{DOC_URL}}` | User-facing docs |
| API specs | `{{API_SPEC_URL}}` | OpenAPI specs |
