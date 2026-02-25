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

**Observability-driven design: shift observability left into design and discovery phases**

> Observability-driven AI development shifts software engineering from reactive fixes to predictive prevention by using real production data during design. Agents evaluate architecture, performance, and resilience upfront — flagging risky assumptions before coding begins.

_Global agent rules:_
- `AGENTS.md` — v2.0 → v2.1: added Rule 9c "Design with observability — before building" mandating that agents define what to observe before building, consult production baselines, assess impact predictively, surface contradictions, ensure observability coverage from design through production, and evaluate observability design at quality review

_Templates:_
- `work/missions/_TEMPLATE-technical-design.md` — v1.0 → v1.1: added Observability Design section (production baseline, instrumentation plan, metrics design, health targets/SLOs, dashboard specification, alerting plan, observability coverage checklist); updated Design Review Checklist with observability, production baselines, and impact assessment items
- `work/missions/_TEMPLATE-mission-brief.md` — v1.2 → v1.3: added Observability Requirements section (key metrics, production baselines at risk, observability dependencies)

_Quality policies:_
- `org/4-quality/policies/observability.md` — v1.0 → v1.1: added Design-Time Observability section; added design-time stage gate (Technical Design approved → observability design complete); added "At Design Time" verification gate; added design-time observability evaluation criterion
- `org/4-quality/policies/architecture.md` — v1.1 → v1.2: added observability design to Technical Design checklist; updated evaluation criteria to include design-time observability

_Process guides:_
- `process/1-discover/GUIDE.md` — added observability requirements step to Mission Brief Creation
- `process/1-discover/AGENT.md` — v1.1 → v1.2: added observability-driven signal detection and Observability Requirements to Mission Brief Drafting
- `process/2-build/GUIDE.md` — added observability design to Technical Design step; added observability to Work Stream Types key policies (Design/Spec, Engineering); added observability to Build Quality Checklist and Exit Criteria
- `process/2-build/AGENT.md` — v1.2 → v1.3: added observability design to Technical Design production; expanded Maintain Quality with observability coverage verification

_Layer agent instructions:_
- `org/2-orchestration/AGENT.md` — v1.3 → v1.4: added observability design verification to Technical Design Gate; added observability policy assignment to Fleet Configuration
- `org/3-execution/AGENT.md` — v1.2 → v1.3: added observability design to Technical Design Production; added production baseline consultation and impact assessment
- `org/4-quality/AGENT.md` — v1.4 → v1.5: added design-time observability evaluation to Evaluation Protocol (step 6)

_Configuration:_
- `CONFIG.yaml` — bumped `framework_version` from `2.1.0` to `2.2.0`

**Expand Minimal Fleet to 5 agents and close structural gaps (Issue #58)**

_Fleet expansion:_
- `CUSTOMIZATION-GUIDE.md` — v2.0 → v2.1: replaced Minimal 3-Agent Fleet with Minimal 5-Agent Fleet (one agent per layer); added "Why 5 Agents, Not 3" rationale section; updated Day 0 → Day 1 initialization sequence to reference all 5 agents with explicit role assignments

_Layer AGENT.md wiring:_
- `org/1-strategy/AGENT.md` — v1.1 → v1.2: expanded "Signal Triage (via Digests)" into full "Signal Triage" workflow section with input/process/output, prioritization criteria, and disposition options
- `org/0-steering/AGENT.md` — v1.1 → v1.2: expanded "Signal Aggregation & Digests" into full "Continuous Sensing Loop" with input/process/output, pattern detection criteria (3+ signals in 4-week window), anomaly flagging, observability cross-reference, and weekly cadence
- `org/2-orchestration/AGENT.md` — v1.2 → v1.3: added "Release Preparation (Ship Loop)" section with input/process/output/handoff; added "Dependency Management" section with deadlock detection and escalation path
- `org/4-quality/AGENT.md` — v1.3 → v1.4: added "Operate Loop" section with outcome measurement (measurement_schedule monitoring), production signaling (reliability/adoption/performance anomalies), and stall detection (7-day threshold)

_Template enhancements:_
- `work/signals/_TEMPLATE-signal.md` — v1.0 → v1.1: added optional `supersedes` field in metadata and "Supersession" section with usage guidance (when to supersede vs. file new)
- `work/missions/_TEMPLATE-outcome-contract.md` — v1.0 → v1.1: enhanced Measurement Schedule with structured date fields (window start/end, interim checks with status tracking); added purpose note linking to Quality and Strategy Layer consumption
- `work/retrospectives/_TEMPLATE-postmortem.md` — v1.0 → v1.1: renamed "Generated Signals" to "Signals Filed" with explicit signal IDs, file links, filing guidance, and Discover loop feedback requirement
- `work/missions/_TEMPLATE-mission-brief.md` — v1.1 → v1.2: added optional `blocked_by` and `blocks` fields for cross-mission dependency declaration

_Governance and process:_
- `org/agents/README.md` — expanded Agent Type Lifecycle table with operational rules per state; added Lifecycle Transition Approvals table; added Deprecation Rules and Retirement Process sections
- `process/2-build/GUIDE.md` — added "Exit Criteria / Handoff to Ship" checklist (required artifacts, quality gates, ownership transfer)
- `process/3-ship/GUIDE.md` — added "Exit Criteria / Handoff to Operate" checklist (required artifacts, quality gates, ownership transfer)

_Configuration:_
- `CONFIG.yaml` — bumped `framework_version` from `2.0.0` to `2.1.0`

### Previously added

**Mission lifecycle: Divide & Conquer task decomposition and status gates (Issue #56)**
- `work/missions/_TEMPLATE-tasks.md` — new template for mission task decomposition; required for missions transitioning to `active` status; includes task structure with assignment, dependencies, acceptance criteria, and asset entry generation
- `docs/mission-lifecycle.md` — new Mission Lifecycle Guide documenting the full mission flow (Divide & Conquer pattern), all status transitions with gate requirements, task decomposition criteria, and 5 named anti-patterns from real operating instances
- `work/missions/_TEMPLATE-mission-brief.md` — v1.0 → v1.1: added `planning` and `cancelled` statuses; added Status Transition Rules section documenting gates for each transition; documented TASKS.md requirement for `active` status and exception for non-execution missions
- `org/2-orchestration/AGENT.md` — v1.1 → v1.2: added Task Decomposition section (TASKS.md as mandatory handoff interface); added `planning` and `cancelled` to status transitions; added TASKS.md to versioning table
- `work/missions/README.md` — updated mission folder structure to include TASKS.md, TECHNICAL-DESIGN.md, and FLEET-REPORT.md; added `planning` and `cancelled` statuses; added step 6 (task decomposition) to "How to Create a Mission"
- `docs/README.md` — added mission-lifecycle.md to setup reference guides and classification table
- `org/3-execution/AGENT.md` — v1.1 → v1.2: added Task Pickup section (TASKS.md as primary work intake for execution agents); added TASKS.md as first item in Context You Must Read
- `process/2-build/AGENT.md` — v1.1 → v1.2: added TASKS.md as primary work intake in Context and Execute Work Streams; added task status tracking to Track Progress
- `org/4-quality/AGENT.md` — v1.2 → v1.3: added TASKS.md to evaluation context; added task traceability (step 2) and acceptance criteria verification (step 5) to Evaluation Protocol
- `work/missions/_TEMPLATE-quality-evaluation-report.md` — v1.0 → v1.1: added Task reference field in metadata; added Task Acceptance Criteria section for traceability between tasks and quality evaluations
- `docs/mission-lifecycle.md` — added "Quality in the Task Lifecycle" section documenting the full task-output-evaluation-verdict cycle; added "The Untraceable Output" anti-pattern; updated Divide & Conquer diagram with quality feedback loop
- `work/missions/_TEMPLATE-mission-status.md` — v1.0 → v1.1: added Task Progress section with task completion metrics and blocked task detail table
- `work/missions/_TEMPLATE-outcome-report.md` — v1.0 → v1.1: added Task Completion section with completion metrics, verdict (all completed / descoped / incomplete), and detail table for incomplete/descoped tasks
- `process/3-ship/AGENT.md` — v1.1 → v1.2: added TASKS.md to context; added task completion verification as release gate; added "Never ship with open tasks" rule

---

## [2.0.0] — 2026-02-23

### Changed

**BREAKING: Simplify products section to single `product_name` field**
- `CONFIG.yaml` — replaced 7-field `products:` block (`core_product_name`, `ai_intelligence_name`, `assistant_name`, `agent_brand`, `data_store_name`, `query_language`, `design_system_name`) with a single top-level `product_name: ""` field; bumped `framework_version` from `1.0.0` to `2.0.0`
- `AGENTS.md` — removed "Product Naming (Mandatory)" section; the product-specific terminology table referenced variables that no longer exist
- `COMPANY.md` — replaced `{{DATA_STORE_NAME}}` with neutral prose; replaced `{{PRODUCT_NAME}}` dog-fooding reference with generic language
- `org/README.md` — replaced `{{QUERY_LANGUAGE}}`, `{{ASSISTANT_NAME}}`, and `{{AI_INTELLIGENCE_NAME}}` in division descriptions with generic capability descriptions
- `org/4-quality/policies/experience.md` — v1.0 → v1.1: replaced `{{DESIGN_SYSTEM_NAME}}` with "the company design system"
- `org/4-quality/policies/architecture.md` — v1.0 → v1.1: replaced `{{DESIGN_SYSTEM_NAME}}` with "the company design system"
- `CUSTOMIZATION-GUIDE.md` — updated Step 1 table, Step 2 sed block, and Placeholder Reference table to reflect single `product_name` field

**Version metadata for root governed files**
- `AGENTS.md`, `OPERATING-MODEL.md`, `CUSTOMIZATION-GUIDE.md`, `CONTRIBUTING.md` — added `> **Version:** 2.0 | **Last updated:** 2026-02-23` metadata line, aligning with the pattern already used by layer AGENT.md files

### Added

**Framework ecosystem participation — Rule 12 (PR #51)**
- `AGENTS.md` Rule 12 — new non-negotiable rule: participate in the framework ecosystem
  - 12a: Contribute generic improvements (bug fixes, patterns, policies) back to upstream template repo as issues/PRs
  - 12b: Periodically check for and propose adoption of upstream template updates (monthly cadence, via signals)
- `CUSTOMIZATION-GUIDE.md` — new "Staying in Sync with the Upstream Framework" section: practical git commands for fetching upstream, reviewing changes, selective merging, and contributing back
- `docs/runtimes/openclaw.md` — adaptive heartbeat backoff recommendation: exponential backoff from 10 min (high activity) to 1× daily (idle), with immediate reset on external events
- `docs/runtimes/README.md` — recommended runtimes overview and two-layer architecture pattern (Scheduling + Event Layer + Agent Runtime)

**Blocking CI check for unfilled placeholders in non-template docs (fix/issue-25)**
- `scripts/check_placeholders.py` — new script that detects unfilled placeholders (`{{VAR}}`, `[TODO]`, `[TBD]`, `T.B.D.`, `Coming Soon`, `__PLACEHOLDER__`, `<PLACEHOLDER>`, `<TODO>`, `_TO_BE_DEFINED_`) in non-template Markdown files; includes self-check mode (`--self-check`) for CI integrity verification
- `.github/workflows/validate.yml` — `validate-placeholders` job upgraded from warning-only to **blocking** (exit 1 on violations); self-check step added for script integrity
- `docs/PLACEHOLDER-CHECK.md` — full guidance on what is detected, what is excluded, per-file opt-out (`<!-- placeholder-ok -->`), and how to fix violations
- `.github/PULL_REQUEST_TEMPLATE.md` — updated checklist to list all detected patterns and reference the blocking CI check
- Framework files that ship with intentional `{{VAR}}` markers (AGENTS.md, COMPANY.md, policy files, process guides, etc.) annotated with `<!-- placeholder-ok -->` opt-out pragma

**Corporate function divisions — People, Legal & Compliance, Finance & Procurement**
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

**Docs reorganization and runtime-agnostic structure (2026-02-22)**
- `docs/FILE-GUIDE.md` — moved from root `FILE-GUIDE.md`; all cross-references updated
- `docs/runtimes/openclaw.md` — moved from `docs/OPENCLAW-SETUP.md` into new `docs/runtimes/` directory for runtime-specific guides
- `docs/runtimes/README.md` — new index for the runtimes directory
- `docs/README.md` — new index for the docs directory
- `AGENT-BOOTSTRAP-PROMPT.md` — deleted; bootstrap content consolidated into `CUSTOMIZATION-GUIDE.md` Step 6
- `docs/MINIMAL-STARTUP-LOOP.md` — deleted; minimal fleet content moved to new `CUSTOMIZATION-GUIDE.md` "Minimal Agent Fleet" section
- `CUSTOMIZATION-GUIDE.md` — added "Minimal Agent Fleet" section (3-agent starting point, self-sustaining loop, scaling guidance) and "Step 6 — Bootstrap Your Agents" section
- `.claude/skills/deploy/SKILL.md` — updated `/deploy` skill to full PR workflow: branch → commit → push → PR → CI watch → merge → return to main (previously stopped after push)
- `CODEOWNERS`, `CONTRIBUTING.md`, `OPERATING-MODEL.md`, `README.md`, `AGENTS.md` — updated all references from deleted/moved files to new paths
- `docs/PLACEHOLDER-CHECK.md` — removed `AGENT-BOOTSTRAP-PROMPT.md` from exclude list
- `docs/REQUIRED-GITHUB-SETTINGS.md` — added context notes for OSS template vs. company fork
- `index.html` — added executive section styles and hero outcomes; minor hero-desc tweak
- `scripts/check_placeholders.py` — removed `AGENT-BOOTSTRAP-PROMPT.md` from framework file exclusion list

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
