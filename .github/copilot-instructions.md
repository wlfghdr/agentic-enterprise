# Copilot Instructions — Agentic Enterprise

This repository is an operating model for running organizations with
AI agents. Work tracking is configurable — see `CONFIG.yaml → work_backend`.

## Read First

1. `AGENTS.md` — Global non-negotiable agent rules
2. `org/<layer>/AGENT.md` — Layer-specific instructions
3. `org/4-quality/policies/` — Mandatory quality policies
4. Mission context in `work/missions/`

## Mental Model

- 5 layers: Steering → Strategy → Orchestration → Execution → Quality
- 4 loops: Discover → Build → Ship → Operate
- Git is the governance backbone:
  - PRs = governance decisions (org structure, policies, templates)
  - CODEOWNERS = RACI
  - CI/CD = quality gates
- Work tracking adapts to configured backend:
  - Git files (`work/`) or issue tracker (GitHub Issues)
  - See `CONFIG.yaml → work_backend` and `docs/work-backends.md`

## Required Behaviors

- Ground recommendations in evidence
- Do not silently make strategic decisions for humans
- Stay in your layer boundaries
- Surface improvement signals (to `work/signals/` or as issues with `artifact:signal` label)
- Prefer minimal, focused changes over broad rewrites

## Template vs. Instance — Know Which You Are Touching

The repo contains two fundamentally different kinds of files. Identify the type before starting work — the completion criteria differ.

**Template / framework files** (the OSS framework itself):
- `_TEMPLATE-*.md` files anywhere in `org/`
- `AGENT.md` files at each layer
- `AGENTS.md` / `CLAUDE.md`
- Quality policies in `org/4-quality/policies/`
- `CONFIG.yaml`, `OPERATING-MODEL.md`, integration definitions in `org/integrations/`

**Instances** (work artifacts created during operations):
- Everything under `work/` — signals, missions, decisions, releases, retrospectives
- Or: issues in the configured issue tracker with `artifact:*` labels
- Division-specific files created during execution

## Releasing Template Changes

When you have finished changing a template or framework file, use `/deploy` to complete the release. The `/deploy` prompt walks through the full checklist: version fields, changelog entry, commit, push, and CI verification.

For instances (files under `work/`): create/update the file, increment `Revision`, open a PR — human approval via merge is the gate.
For instances (issue backend): create/update the issue with appropriate labels — human approval via label change is the gate.

## Key Paths

- `org/` — Organizational structure and agent roles
- `process/` — Loop-by-loop process guides
- `work/` — Active work artifacts
- `CONFIG.yaml` — Customization source of truth
