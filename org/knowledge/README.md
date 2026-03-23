# Knowledge Manifests Registry

> **Last updated:** 2026-03-23

This directory is the governed registry of **what agents know**.

Skill manifests govern reusable process instructions. MCP profiles govern tool access. **Knowledge manifests govern the sources, freshness, and ownership of context agents may rely on.**

## Schema

All manifests must conform to [`schemas/knowledge-manifest.schema.json`](../../schemas/knowledge-manifest.schema.json).

## Naming Convention

```
<knowledge-id>.knowledge.json
```

Example: `org-governance.knowledge.json`

## Layer Model

| Layer | Scope | Typical examples |
|---|---|---|
| **1** | org-wide | standards, security baselines, shared vocabulary |
| **2** | capability/domain | platform engineering playbooks, sales domain guidance |
| **3** | product | product workflows, troubleshooting surfaces, integration behavior |
| **4** | repo | AGENTS.md, ADRs, build/deploy specifics |

## Lifecycle

1. Propose or update a manifest via PR.
2. Name the source paths, owners, and freshness expectations explicitly.
3. Reference the manifest from capability contracts when an agent type depends on that knowledge.
4. Review and refresh on the declared cadence.

## Index

| Knowledge ID | Layer | Version | Purpose |
|---|---:|---|---|
| `org-governance` | 1 | 1.0.0 | Shared governance, process, and policy knowledge shipped with the framework |
