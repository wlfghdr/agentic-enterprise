# Changelog

All notable changes to the **Agentic Enterprise Operating Model** framework are documented here.

This file follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) convention.
The framework uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html): `MAJOR.MINOR.PATCH`.

## Versioning Conventions

| Bump | When to use |
|------|-------------|
| **PATCH** | Prose edits, typos, clarifications that don't change meaning or structure |
| **MINOR** | New sections, field additions, structural additions (non-breaking) |
| **MAJOR** | Breaking changes to template structure or policy that invalidate existing instances |

**Document-level versioning** (AGENT.md, policies, templates) uses `MAJOR.MINOR` and is tracked independently inside each file's changelog section. The framework-level version here tracks the overall system.

---

## [Unreleased]

_Changes merged to `main` but not yet tagged as a release go here. Move to a new version section when cutting a release._

### Added

**Corporate function divisions — People, Legal & Compliance, Finance & Procurement (PR #TBD)**
- `org/3-execution/divisions/people/DIVISION.md` — People division: recruiting, workforce planning, HR operations, onboarding, performance, L&D
- `org/3-execution/divisions/legal/DIVISION.md` — Legal & Compliance division: contract management, regulatory advisory, IP, privacy law
- `org/3-execution/divisions/finance-procurement/DIVISION.md` — Finance & Procurement division: budget management, vendor procurement, financial reporting
- `org/agents/execution/workforce-planner-agent.md` — Workforce Planner Agent: translates operational capacity signals into headcount recommendations
- `org/agents/execution/recruiting-coordinator-agent.md` — Recruiting Coordinator Agent: end-to-end talent acquisition pipeline execution
- `org/agents/execution/hr-generalist-agent.md` — HR Generalist Agent: HR operations, onboarding, performance review facilitation, culture signal analysis
- `org/agents/execution/contract-review-agent.md` — Contract Review Agent: first-pass contract review, redlining, template drafting, lifecycle tracking
- `org/agents/execution/compliance-advisor-agent.md` — Compliance Advisor Agent: regulatory monitoring, compliance guidance, privacy advisory
- `org/agents/execution/budget-analyst-agent.md` — Budget Analyst Agent: continuous budget tracking, variance analysis, spend forecasting
- `org/agents/execution/procurement-agent.md` — Procurement Agent: vendor sourcing, RFP/RFQ management, PO drafting, spend tracking
- `CONFIG.yaml` — added `corporate` division category with people, legal, finance-procurement divisions

**HR Recruiting full lifecycle example**
- `examples/hr-recruiting-lifecycle.md` — End-to-end walkthrough: observability platform auto-files PR review latency signal → Steering authorizes recruiting mission → 3-stream People division fleet (Workforce Analysis, Recruiting Pipeline, Interview & Offer Management) with blocking cross-division gates (Legal + Finance) → outcome measured back in the observability platform; shows corporate functions as first-class divisions
- `examples/README.md` — Added HR Recruiting to Available Examples table, Coverage Matrix (new column), and recommended reading order

**PR consistency fixes — lock and governance exception integration (follow-up to PRs #38, #39)**
- `AGENTS.md` Rule 4 — added governance exception process guidance: when, how, and who must approve exceptions; references `_TEMPLATE-governance-exception.md`
- `AGENTS.md` Rule 11 — fixed template classification to include `_TEMPLATE-*.md` files anywhere in the repo (including `work/locks/` and `work/decisions/`), not just `org/`
- `AGENTS.md` repo structure — added `work/locks/` to the structure diagram
- `CLAUDE.md` — synced with all `AGENTS.md` changes above
- `CODEOWNERS` — added `work/locks/ @orchestration-fleet-manager`; added template overrides for `work/decisions/_TEMPLATE-governance-exception.md` (`@steering-executive @quality-policy-author`) and `work/locks/_TEMPLATE-lock.md` (`@steering-executive`)
- `work/decisions/_TEMPLATE-governance-exception.md` — v1.0 → v1.1: added instance metadata block (Revision, Last updated, Status fields) and Revision History section for instance tracking
- `work/README.md` — added `locks/` to the folder structure diagram and How It Works table; added governance exception row to the table; added naming conventions for governance exceptions (`EXC-YYYY-NNN-...`) and locks (path-derived slug)
- `org/4-quality/AGENT.md` — v1.1 → v1.2: updated "What You Never Do" to reference the Governance Exception process; clarified that a merged, unexpired exception record is required to unlock a policy bypass
- `CHANGELOG.md` — added retroactive entries for PRs #38 and #39 (previously unlogged)

**Retroactive entries for previously merged PRs:**

_PR #39 (2026-02-20) — Add governance exception template_
- `work/decisions/_TEMPLATE-governance-exception.md` — new template for time-bounded policy exceptions with risk documentation and required approvers

_PR #38 (2026-02-20) — Define work lock convention_
- `work/locks/README.md` — lock convention: when to lock, lock file format, acquire/release protocol, stale lock handling
- `work/locks/_TEMPLATE-lock.md` — lock file template

**Template/instance distinction and `/deploy` skill**
- `AGENTS.md` Rule 11 — distinguishes template/framework files from work artifact instances; defines completion criteria for each (framework changes require commit + push + green CI before done)
- `.claude/skills/deploy/SKILL.md` — Claude Code `/deploy` slash command: 5-step template release checklist (verify version fields, add changelog entry, commit, push, watch CI)
- `.github/prompts/deploy.prompt.md` — GitHub Copilot `/deploy` prompt: same 5-step checklist for Copilot Chat
- `.github/copilot-instructions.md` — added template vs. instance classification section and reference to `/deploy`

---

## [1.1.0] — 2026-02-19

### Added

**Versioning system**
- `CHANGELOG.md` — this file; framework-level version history
- `CONFIG.yaml` — added `framework_version: "1.0.0"` field
- All 5 layer `AGENT.md` files — added `Version` and `Last updated` metadata; added `## Changelog` section; added `## Versioning Your Outputs` section with artifact-specific guidance
- All 4 process loop `AGENT.md` files (`process/*/AGENT.md`) — added `Version` and `Last updated` metadata; added `## Changelog` section; added `## Versioning Your Outputs` section
- All 8 quality policy files — added `Version` and `Last updated` metadata; added `## Changelog` section
- All 23 `_TEMPLATE-*.md` files — added `Last updated` to `Template version` field; added `## Changelog` section
- Work artifact templates — added `Revision` metadata field and `## Revision History` section
- `AGENTS.md` Rule 10 — global versioning mandate with bump rules and per-artifact guidance
- `validate-versioning` CI job — existence check for version fields + PR enforcement that changed governed files have updated `Last updated` date

### Changed

- `org/2-orchestration/AGENT.md` — clarified that `STATUS.md` is a running log exempt from Revision tracking (resolved conflict with Rule 10)

---

## [1.0.0] — 2026-02-19

### Added

**Framework foundation**
- `AGENTS.md` — Global agent instruction hierarchy (Rules 1–10)
- `COMPANY.md` — Vision, mission, and strategic beliefs
- `OPERATING-MODEL.md` — 5-layer model overview
- `CONFIG.yaml` — Central configuration with `framework_version` field
- `CHANGELOG.md` — This file; project-level version history (you are here)
- `CODEOWNERS` — Git-native RACI for approval routing
- `FILE-GUIDE.md` — Orientation guide for repo structure

**Organizational structure**
- `org/0-steering/AGENT.md` — Steering Layer instructions (v1.0)
- `org/1-strategy/AGENT.md` — Strategy Layer instructions (v1.0)
- `org/2-orchestration/AGENT.md` — Orchestration Layer instructions (v1.0)
- `org/3-execution/AGENT.md` — Execution Layer instructions (v1.0)
- `org/4-quality/AGENT.md` — Quality Layer instructions (v1.0)
- `org/README.md` — 5-layer model overview
- Agent Type Registry (`org/agents/`) with templates for all five layers

**Quality policies** (all at v1.0)
- `org/4-quality/policies/architecture.md`
- `org/4-quality/policies/content.md`
- `org/4-quality/policies/customer.md`
- `org/4-quality/policies/delivery.md`
- `org/4-quality/policies/experience.md`
- `org/4-quality/policies/observability.md`
- `org/4-quality/policies/performance.md`
- `org/4-quality/policies/security.md`

**Process loops**
- 4-loop lifecycle: Discover, Build, Ship, Operate
- AGENT.md and GUIDE.md for each loop

**Work artifact templates** (all at v1.0)
- Mission Brief, Outcome Contract, Outcome Report, Mission Status, Technical Design
- Fleet Performance Report, Quality Evaluation Report
- Release Contract, Decision Record
- Signal, Signal Digest
- Postmortem, Asset Registry Entry
- Venture Charter, Venture Health Report
- Agent Type definition and proposal templates
- Evolution Proposal, Fleet Config, Runbook, Component Onboarding, Integration

**CI / Validation**
- `validate.yml` — YAML validation, Markdown link checks, placeholder checks, structure checks, version field enforcement
- `stale.yml` — Stale issue/PR management

**Integrations**
- Integration Registry (`org/integrations/`) with category structure
- `_TEMPLATE-integration.md`

**Examples**
- Reference examples in `examples/`
