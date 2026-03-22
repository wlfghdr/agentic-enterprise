# OpenClaw Onboarding for an Instance

## Goal

Reduce the amount of manual work required after instantiating an enterprise repo.

This guide focuses on the runtime/bootstrap steps that frequently remain outside the raw repo clone:
- minimum fleet definition
- agent workspace/agentDir expectations
- Discord channel topology
- routing policy
- work/dispatch labels

## Minimum fleet recommendation

A practical default fleet for an instance is:
- steering
- strategy
- orchestration
- execution
- quality
- internal auditor

Optional early additions when workload justifies them:
- research
- content / GTM

## Role split

- **Steering** detects and aggregates signals
- **Strategy** turns qualified signals into mission candidates
- **Orchestration** decomposes approved missions and keeps work moving
- **Execution** implements changes
- **Quality** checks quality/policy/genericity boundaries
- **Auditor** checks work-flow integrity, repo hygiene, ownership discipline, automation pickup, and upstream-adoption quality
- **Research** gathers evidence when the main gap is understanding
- **Content / GTM** supports messaging, enablement, and output communication

## Routing policy

For instance agents, prefer:
1. subscription-backed primary model
2. other-provider subscription fallback
3. API-token fallback only after that

## Workspace rule

Instance agents should use the **instance repo** as their workspace.
Do not leave them pointed at a generic catch-all shared workspace by default.

## Agent directories

Each running OpenClaw agent should have its own `agentDir` with the credentials/config it actually needs.
At minimum:
- `models.json`
- `auth-profiles.json`
- agent-local `AGENTS.md`

## Discord topology

Prefer role-first human channels, not model-first channels.

Example minimal channel set:
- `<instance>-main` (optional)
- `<instance>-steering`
- `<instance>-strategy`
- `<instance>-orchestration`
- `<instance>-execution`
- `<instance>-quality`
- `<instance>-auditor`
- optional: `<instance>-research`, `<instance>-content`

## Discord admin / provisioning path

Treat Discord provisioning as a first-class onboarding step, not an undocumented manual side quest.

The runtime/bootstrap path should support at least:
- create category
- create channel
- list existing channels
- return resulting channel IDs for runtime bindings
- optionally apply permission overwrites

Operational rules:
- keep the provisioning path auditable
- store environment-specific channel IDs in the runtime binding artifact, not buried in prose
- separate generic topology guidance from instance-specific IDs
- if channel creation still requires a human, make that handoff explicit with the exact channels/categories to create

## Labels

Install a practical minimum label baseline in the work repo.
Use labels for:
- artifact type
- best-fit agent/dispatch role
- scope/product boundary
- approval-required semantics

Do **not** use labels to duplicate native GitHub state or assignee ownership.
Ownership belongs in assignees and review requests.

## Cleanup caution

Do not remove CI-critical shared reference material during instance cleanup.
Before deleting or pruning scaffolded content, verify that validation workflows still have what they expect.
Typical examples include:
- compliance reference docs
- policy-linked docs
- workflow/policy scaffolding

If cleanup rules are scripted, prefer allowlists/preservation rules for known CI-critical assets over broad destructive pruning.
