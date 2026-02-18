# Copilot Instructions — Agentic Enterprise

This repository is a Git-native operating model for running organizations with
AI agents.

## Read First

1. `AGENTS.md` — Global non-negotiable agent rules
2. `org/<layer>/AGENT.md` — Layer-specific instructions
3. `org/4-quality/policies/` — Mandatory quality policies
4. Mission context in `work/missions/`

## Mental Model

- 5 layers: Steering → Strategy → Orchestration → Execution → Quality
- 4 loops: Discover → Build → Ship → Operate
- Git is the operating system:
  - PRs = decisions
  - CODEOWNERS = RACI
  - CI/CD = quality gates

## Required Behaviors

- Ground recommendations in evidence
- Do not silently make strategic decisions for humans
- Stay in your layer boundaries
- Surface improvement signals to `work/signals/`
- Prefer minimal, focused changes over broad rewrites

## Key Paths

- `org/` — Organizational structure and agent roles
- `process/` — Loop-by-loop process guides
- `work/` — Active work artifacts
- `CONFIG.yaml` — Customization source of truth
