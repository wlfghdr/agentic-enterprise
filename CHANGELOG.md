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

- New ISO 42001 certification-readiness assets: `docs/compliance/remediation/iso-42001-aims-scope.md`, `docs/compliance/templates/_TEMPLATE-aims-scope.md`, and `docs/compliance/templates/_TEMPLATE-ai-system-inventory.md` — AIMS scope guidance plus reusable scope and AI system inventory templates aligned to ISO/IEC 42001 clause 4 and the framework's AI risk-tier model. Closes #126.
- New SOC 2 audit-readiness assets: `docs/compliance/remediation/soc2-control-testing.md`, `docs/compliance/templates/_TEMPLATE-soc2-control-testing-matrix.md`, and `docs/compliance/templates/_TEMPLATE-soc2-control-test-result.md` — formal control testing guidance, pre-seeded TSC-to-procedure matrix, CI/CD validation-to-control-test mapping, and reusable result records for documenting control effectiveness. Closes #124.
- New CI validation: `scripts/validate_cross_references.py` — semantic cross-reference integrity checks for work artifacts, signal supersession chains, governance exception references, and quality-policy file references including bare `.md` mentions. Runs as blocking `validate-cross-references` job in `validate.yml`. Closes #114.
- New CI validation: `scripts/validate_otel_contract.py` — OTel contract compliance checks for agent type telemetry sections, skill manifest telemetry declarations, observability integration documentation examples, and telemetry-aware policy references to `docs/otel-contract.md`. Runs as blocking `validate-otel-contract` job in `validate.yml`. Closes #115.
- New CI validation: `scripts/validate_compliance_mapping.py` — compliance mapping validation for quality policies, including framework normalization, control identifier format checks, compliance reference document presence, and reused-control consistency warnings. Runs as blocking `validate-compliance-mapping` job in `validate.yml`. Closes #116.
- New CI validation: `scripts/validate_integration_registry.py` — integration registry consistency checks for `CONFIG.yaml`, category docs in `org/integrations/categories/`, observability integration presence, and integration-spec metadata. Runs as blocking `validate-integration-registry` job in `validate.yml`. Closes #117.
- New CI validation: `scripts/validate_content_security.py` — content security scanner that detects prompt injection patterns, instruction override attempts, role impersonation, hierarchy violations, unsafe code patterns, encoded payloads, trust boundary violations, social engineering in work artifacts, policy bypass attempts, CI pipeline integrity violations, and Rego policy tampering across all governed files including workflow YAML and policy-as-code. Runs as blocking `validate-content-security` job in `validate.yml`. Supports inline suppression via `<!-- content-security:allow -->` for legitimate references. Policy reference: agent-security.md §4.3.
- New OPA/Rego rule: `policy/workflows/security_integrity.rego` — enforces CI pipeline integrity by blocking `continue-on-error` on security/validation jobs, `if: false` disabling of security jobs, unquoted `${{ github.event.* }}` shell injection vectors, and remote script fetch-and-execute patterns. Runs via Conftest in `policy.yml`.
- New quality policy: `org/4-quality/policies/ai-governance.md` — AI governance & responsible AI covering 4-tier risk classification (Prohibited / High-Risk / Limited-Risk / Minimal-Risk aligned to EU AI Act), model card requirements (scaled by risk tier), fairness audit process (demographic parity, equalized odds, error rate parity), adversarial robustness testing (beyond prompt injection), explainability levels (Traceable / Justifiable / Auditable), token usage accountability (budget enforcement, cost attribution), and compliance mapping (ISO 42001 / EU AI Act / NIST AI RMF). Closes #91.
- New quality policy: `org/4-quality/policies/data-classification.md` — 4-level data classification scheme (PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED) with handling requirements matrix (encryption, access control, retention, deletion, audit logging per level), PII inventory requirements, asset registry integration, agent workflow classification rules, cross-policy alignment (security, privacy, cryptography, observability, risk management, content), and compliance mapping (ISO 27001 A.8 / SOC 2 C1 / GDPR Art. 5, 9, 30 / NIST SP 800-53, 800-60). Closes #93.
- New template: `work/assets/_TEMPLATE-pii-inventory.md` — PII inventory entry template for tracking personal data categories, classification, processing purposes, storage locations, access controls, and compliance cross-references (DPIA, DPA, asset registry).
- New quality policy: `org/4-quality/policies/vendor-risk-management.md` — Vendor & Third-Party Risk Management covering 4-tier vendor criticality model (Critical / Significant / Standard / Low), full lifecycle governance (identification → assessment → onboarding → monitoring → offboarding), security assessment framework with 7 domains (security posture, attestations, data handling, privacy/subprocessor, operational resilience, AI-specific, financial viability), SLA and contract requirements, attestation verification (SOC 2 Type II / ISO 27001), concentration risk tracking, integration registry connection, and compliance mapping (ISO 27001 A.5.19–A.5.23 / SOC 2 CC9 / GDPR Art. 28 / EU AI Act Art. 26–28 / NIST SP 800-53 SA-9, SR / NIST AI RMF). Closes #92.
- New template: `work/assets/_TEMPLATE-vendor-security-assessment.md` — Vendor security assessment questionnaire with 7 assessment domains, attestation verification checklist, AI-specific assessment section, concentration risk evaluation, and risk findings tracker.
- New quality policy: `org/4-quality/policies/log-retention.md` — Log Retention & Immutability covering 5-category retention schedule (audit / security / access / operational / debug), WORM and tamper-evidence requirements for audit and security logs, legal hold capability, verified deletion with confirmation records, log access controls, agent telemetry classification, and compliance mapping (ISO 27001 A.12.4 / SOC 2 CC7 / GDPR Art. 5(1)(e), 17, 30 / EU AI Act Art. 12 / NIST SP 800-53 AU-9, AU-10, AU-11). Closes #94.
- New quality policy: `org/4-quality/policies/agent-security.md` — covers prompt injection mitigations, tool abuse prevention, insecure output handling, and security testing requirements. Maps to OWASP LLM Top 10. Closes #69.
- New quality policy: `org/4-quality/policies/risk-management.md` — formal risk management framework with 5×5 scoring methodology, AI risk taxonomy (22 canonical risks across 5 dimensions), agent autonomy tiers, observability-driven KRIs, and regulatory crosswalk (ISO 31000 / NIST RMF / NIST AI RMF / ISO 27001 / SOC 2 / EU AI Act). Closes #86.
- New template: `work/decisions/_TEMPLATE-risk-register.md` — risk register entry template with mandatory fields per ISO 27001 §6.1.2 and SOC 2 CC3.
- New CONFIG.yaml section: `risk_appetite` (§11) — configurable risk tolerance thresholds referenced by risk-management.md.
- New quality policy: `org/4-quality/policies/cryptography.md` — encryption & key management covering approved algorithms (AES-256-GCM, TLS 1.3, post-quantum readiness), key lifecycle (NIST SP 800-57), AI/agent-specific encryption (model protection, credential isolation, inter-agent mTLS), certificate management, KMS infrastructure, and compliance mapping (ISO 27001 A.8.24 / SOC 2 CC6.1 / NIST SP 800-57 / PCI DSS / GDPR / EU AI Act). Closes #88.
- New CONFIG.yaml section: `encryption` (§12) — configurable key rotation schedules, certificate lifetimes, and crypto infrastructure referenced by cryptography.md.

### Changed

- Refined validation ownership boundaries so OTel contract checks focus on contract-linked telemetry artifacts and observability documentation, integration registry checks own `CONFIG.yaml` registry validation, `validate_agent_instructions.py` focuses on structural hierarchy checks, and `validate_cross_references.py` no longer requires `pyyaml` for registry-category validation.
- Hardened workflow validation consistency: `validate.yml` now resolves diff SHAs through `env:` variables instead of direct `github.event.*` interpolation inside shell, `policy.yml` documents the active security-integrity Rego coverage, and `validate_content_security.py` scopes the GitHub expression warning to executable workflow `run:` blocks to avoid comment/env false positives.
- Updated `scripts/validate_cross_references.py` to downgrade case-only filename mismatches to warnings while still resolving them and reporting the exact filename discrepancy; corrected `org/4-quality/policies/ai-governance.md` prose references to use the canonical lowercase `agent-security.md` filename.
- Reworked the public onboarding flow across `README.md`, `index.html`, and `concept-visualization.html` so the README acts as a router for three first actions: understand the operating model, see the demo/reference scenario, and start minimal adoption. Promoted the HTML demo assets as first-class proof surfaces, aligned terminology around operating model / demo / reference scenario / runtime / observability / adoption, made the no-agents-required path more prominent, shortened duplicated landing-page explanation, and set the visualization's default scenario to the real `examples/e2e-loop/` artifact chain.
- Updated `org/4-quality/policies/agent-security.md` (v1.0.1 → v1.1) — added §4.3 CI Content Security Scanning with automated enforcement via `validate_content_security.py`; added content security CI evaluation criterion; updated OWASP LLM01 coverage map.
- Updated `docs/security-scanning.md` — added Content Security Scanning section documenting pattern categories, local usage, finding handling, and policy alignment.
- Updated `org/integrations/_TEMPLATE-integration.md` (v1.1 → v1.2) — added vendor assessment reference, criticality tier, attestation status fields, and vendor-risk-management.md to policy references and validation checklist.
- Updated `org/4-quality/policies/risk-management.md` (v1.1 → v1.2) — extended §6.4 to reference vendor-risk-management.md for general vendor governance; added vendor concentration risk requirement.
- Updated `org/4-quality/policies/security.md` (v1.2 → v1.3) — renamed Dependency Security to Dependency & Vendor Security; added vendor assessment and attestation requirements.
- Updated `org/4-quality/AGENT.md` (v1.12 → v1.13) — added vendor & third-party risk to quality dimensions.
- Updated `CUSTOMIZATION-GUIDE.md` (v3.5 → v3.6) with vendor risk management policy customization guidance and vendor risk management note.
- Updated `README.md` and `index.html` to reflect 19 quality policy domains (was 17); updated ISO 27001 (~85% → ~90%) compliance badge; vendor risk badges now green.
- Updated `org/4-quality/policies/observability.md` (v1.3 → v1.4) — added Log Retention & Immutability section cross-referencing log-retention.md; added telemetry retention evaluation criterion.
- Updated `org/4-quality/policies/security.md` (v1.1 → v1.2) — data retention requirement now references log-retention.md.
- Updated `org/4-quality/AGENT.md` (v1.11 → v1.12) — added log retention & immutability to quality dimensions.
- Updated `CUSTOMIZATION-GUIDE.md` (v3.4 → v3.5) with log retention policy customization guidance and log retention note.
- Updated `README.md` and `index.html` to reflect 17 quality policy domains (was 16); updated ISO 27001 (~80% → ~85%) and SOC 2 (~90% → ~95%) compliance badges.
- Updated `org/agents/_TEMPLATE-agent-type.md` (v1.0 → v1.1) — added Model Governance section with AI risk tier, model identity, intended use & scope, known limitations, training data & context, fairness considerations, and token budget fields.
- Updated `org/4-quality/AGENT.md` (v1.10 → v1.11) — added AI governance & responsible AI to quality dimensions.
- Updated `CUSTOMIZATION-GUIDE.md` (v3.3 → v3.4) with AI governance policy customization guidance and AI governance note.
- Updated `README.md` and `index.html` to reflect 16 quality policy domains (was 15).
- Updated `org/4-quality/policies/security.md` (v1.0 → v1.1) — Data Protection section now references data-classification.md for classification taxonomy and handling requirements; evaluation criterion updated.
- Updated `work/assets/_TEMPLATE-asset-registry-entry.md` (v1.0 → v1.1) — added Classification section with Data Classification, Contains PII, and Handling notes fields.
- Updated `CUSTOMIZATION-GUIDE.md` (v3.2 → v3.3) with data classification policy customization guidance and data classification note.
- Updated `README.md` and `index.html` to reflect 15 quality policy domains (was 14).
- Updated `org/4-quality/AGENT.md` (v1.9) to include encryption & key management in quality dimensions.
- Updated `org/4-quality/policies/risk-management.md` §10 to include cryptography.md in the policy-to-risk-control mapping.
- Updated `CUSTOMIZATION-GUIDE.md` (v3.2) with cryptography policy customization guidance, encryption note, and `{{CRYPTO_*}}` placeholder reference.
- Updated `README.md` and `index.html` to reflect 11 quality policy domains (was 10).
- Documentation cleanup in `docs/`: removed the duplicate backend config guide `WORK-BACKEND.md` in favor of `work-backends.md`, removed the duplicate observability quick-reference `observability-genai.md` in favor of `otel-contract.md`, and rewrote `docs/README.md` as a shorter navigation index with clearer reading paths.
- Consolidated GitHub instance assets under `docs/github/`: moved the former `docs/github-implementation/` guide and `docs/github-issues/` samples into one GitHub-focused folder with `issue-templates/` and `workflows/` subfolders, and updated references accordingly.
- Clarified agent observability correlation guidance: `org/integrations/categories/observability.md` now uses canonical `git.*` and `agentic.*` field names in Git-derived event examples and explicitly distinguishes native spans from derived UI events.
- Expanded `docs/otel-contract.md` to define how downstream UIs correlate flattened activity records to traces using canonical `trace.id`, `span.id`, and `parent.span.id` identifiers, closing a gap for command-center trace linking.
- Tightened `org/4-quality/policies/observability.md` so trace-linkability of derived activity records is now a policy-level requirement, not just a contract detail.

---

## [3.1.0] — 2026-03-08

> **Status tracking moves from labels to GitHub Project Status fields.** This release replaces `status:*` labels with the GitHub Projects v2 native Status field for issue-backend state tracking. Labels remain for categorization (`artifact:`, `layer:`, `loop:`, `priority:`, `category:`, `urgency:`). Status transitions happen via a single-select Project Status field with values: Backlog, Triage, Approved, Planning, In Progress, Blocked, Done. Terminal states use GitHub's native close mechanism (completed / not planned).

### Changed

**Status tracking: labels → GitHub Project Status field (MINOR)**

_Core configuration:_
- `CONFIG.yaml` — added `project_owner` and `project_number` under `work_backend.github_issues`; bumped `framework_version` from `3.0.0` to `3.1.0`
- `schemas/config.schema.json` — added `project_owner` (string) and `project_number` (integer) properties; updated `use_label_prefixes` description to remove `status:`

_Primary documentation:_
- `docs/github-issues.md` — **major rewrite (v1.1 → v2.0)**: removed ~20 `status:*` labels; added "Status Tracking via GitHub Project" section with Project Status Field Options, Terminal States, "Why Not Labels?" rationale, Status Mapping by Artifact Type; updated setup checklist, label bootstrap, human approval table, handoff mechanics
- `docs/work-backends.md` — replaced "Status Labels" section with "Status Tracking (GitHub Project Status Field)"; updated handoff protocol, approval mechanisms, audit trail; version bumped to v1.3
- `docs/WORK-BACKEND.md` — updated config sample and label table to remove `status:` row
- `docs/mission-lifecycle.md` — added Project Status field column to Mission Statuses table; updated gate transitions from `status:` labels to Project Status transitions
- `docs/archive-policy.md` — updated close guidance from "apply final status labels" to "set project status to Done"
- `docs/required-github-settings.md` — updated required label families and human approval examples
- `docs/github-implementation/README.md` — updated label table (removed `status:` row, added note about Project Status field); board view grouping changed from `status:` label to Project Status field

_Agent instructions:_
- `AGENTS.md` (v3.1 → v3.2) — updated 5 references from status labels to project status transitions; CLAUDE.md updated via symlink
- `org/4-quality/AGENT.md` — stall detection now references project status `In Progress` instead of `status:active` label

_Work artifact references:_
- `work/README.md` — issue backend table updated from `status:*` labels to Project Status transitions
- `CUSTOMIZATION-GUIDE.md` — signal creation updated from `status:new` label to Project Status default
- `process/README.md` — approval row changed from "Label change" to "Project status transition"

_Issue form templates (removed default `status:*` labels):_
- `docs/github-issues/forms/signal.sample.yml`, `mission.sample.yml`, `task.sample.yml`, `decision.sample.yml`, `release.sample.yml`, `retrospective.sample.yml`

_Automation scripts:_
- `scripts/work_backend.py` — added `project_owner` and `project_number` to WorkBackend dataclass; added GraphQL helpers: `_graphql_cmd()`, `get_project_statuses()`, `set_project_status()`, `_find_project_item()`, `_get_issue_node_id()`
- `scripts/find_pending_work.py` — `issue_backend_report()` now uses `get_project_statuses()` batch query instead of `prefixed_label(issue, "status:")`
- `scripts/approval_queue.py` — `build()` now uses `get_project_statuses()` batch query instead of `prefixed_label(issue, "status:")`
- `scripts/triage_signals.py` — `handle_issue_backend()` now uses `get_project_statuses()` for reading and `set_project_status()` for writing, replacing `gh issue edit --add-label/--remove-label` commands

### Added
- **Assignment discipline for all GitHub artifacts** (AGENTS.md Rule 3, work-backends.md, github-issues.md): Every issue, PR, and review request must have an assignee at all times. Mandatory handoff protocols for both issues and PRs. Comment-based human approval model — humans comment and re-assign, agents handle all label management. PR handoff protocol covers review requests, feedback cycles, and merge handoffs. Orchestration agents must sweep for unassigned items. Agent identity via dedicated bot accounts required.
- **Canonical OTel Telemetry Contract** (`docs/otel-contract.md`): Single source of truth for all agent telemetry. OTel-first design — standard OTel/GenAI semantic conventions (`gen_ai.*`) take precedence; custom `agentic.*` and `governance.*` attributes used only where OTel has no equivalent. Includes: canonical span names (`agent.run`, `agent.subagent.invoke`, `tool.execute`, `quality.evaluate`, `git.operation`, `mission.transition`, `inference.chat`, `inference.generate`), resource attribute requirements, native vs derived event contract, privacy defaults (content capture off by default), canonical deprecation table for all legacy field names, semconv stability and migration policy, machine-readable YAML schema appendix. Closes #77, supersedes inline attribute lists in AGENTS.md, observability policy, and integration docs.
- **Instrumented workflow example** (`examples/observability/agent-span-example.md`): Concrete end-to-end trace example covering agent run, inference, tool calls, git operations, quality evaluation, governance decision events, and error scenarios.

### Changed
- **AGENTS.md Rule 9a** (version 3.1 → 3.2): Replaced inline attribute list with reference to `docs/otel-contract.md`. Updated span event and tool span naming to use canonical names.
- **`org/4-quality/policies/observability.md`** (version 1.1 → 1.2): Replaced Agent Observability attribute list with reference to `docs/otel-contract.md`.
- **`org/integrations/categories/observability.md`**: Replaced "Recommended OpenTelemetry semantic conventions" section with reference to `docs/otel-contract.md`; documents deprecated field names.
- **`org/agents/quality/observability-compliance-agent.md`**: Updated Instrumentation Presence check to reference canonical contract and flag deprecated attribute names.

---

## [3.0.0] — 2026-03-07

> **Agentic Enterprise goes multi-backend.** This is a major release that decouples work tracking from Git files, introduces GitHub Issues as a first-class work backend, and brings sweeping consistency improvements across all five layers of the operating model.

### Added

**Work Backend Abstraction — configurable work tracking (MAJOR)**

> Operational work artifacts (signals, missions, tasks, decisions, releases, retrospectives) can now be tracked in either Git files (the original model) or an issue tracker (GitHub Issues). The choice is made at instance configuration time via `CONFIG.yaml → work_backend`. This is a breaking conceptual change — the framework no longer assumes Git-only work tracking.

_Core concept:_
- `docs/work-backends.md` — new comprehensive guide: three file categories (governance backbone, persistent docs, configurable work artifacts), label taxonomy for issue backends, structural conventions, agent behavior differences, migration paths
- `CONFIG.yaml` — new section 8 `work_backend` with `type` (`git-files` | `github-issues`), `github_issues` configuration, and per-artifact `overrides`; bumped `framework_version` from `2.3.0` to `3.0.0`

_Agent rules updated:_
- `AGENTS.md` — Rule 3 renamed from "Process is the repo" to "Process is governed"; now describes both git-files and issue backends; Rule 2 updated approval mechanism; Rule 7 updated signal filing; Rule 11 updated instance definition for issue backend; Rule 12 updated deduplication for both backends; Rule 14 renamed from "keep active directories clean" to "keep active views clean" with issue-backend archiving (close issues); version bumped to 3.0
- `.github/copilot-instructions.md` — updated to reflect configurable work backend

_Documentation updated:_
- `OPERATING-MODEL.md` — softened "git is the only way" language; now describes Git as governance backbone with configurable work tracking; updated artifact flow, collaboration pattern, human interaction model, and mapping table; version bumped to 3.0
- `work/README.md` — added dual-backend structure, issue backend artifact/label table
- `CUSTOMIZATION-GUIDE.md` — new Step 4 "Choose Your Work Backend"; updated "What You Don't Need" section; updated initialization sequence for both backends; version bumped to 3.0
- `docs/github-issues.md` — new GitHub implementation guide with exact setup checklist, label bootstrap samples, issue form guidance, and explicit human approval transitions
- `docs/work-backends.md` — clarified which companion artifacts remain in Git, added human approval cheat sheet, and linked the GitHub implementation guide; version bumped to 1.1
- `docs/github-issues/` — added GitHub issue-form and config samples for signal, mission, task, decision, release, and retrospective workflows; kept them out of the live `.github/ISSUE_TEMPLATE/` path so the template repo itself does not behave like an instance repo
- `docs/mission-lifecycle.md`, `docs/required-github-settings.md`, `docs/file-guide.md` — corrected remaining git-only assumptions and made issue-backend human steps explicit

_Layer agent instructions updated:_
- `org/0-steering/AGENT.md` — updated sensing loop input, signal references, and interaction diagram for dual backend; version bumped to 1.3
- `org/1-strategy/AGENT.md` — updated signal triage input/output, mission brief creation, versioning table, approval mechanism, and continuous improvement signals for dual backend; version bumped to 1.3
- `org/2-orchestration/AGENT.md` — updated active missions context, work deduplication, task decomposition, status tracking, release preparation, and fleet reporting for dual backend; version bumped to 1.6
- `org/3-execution/AGENT.md` — updated task pickup, mission brief context, task status updates, improvement signals, and deduplication for dual backend; version bumped to 1.5
- `org/4-quality/AGENT.md` — updated evaluation context, report storage, versioning table, quality trend analysis, outcome measurement, stall detection, and production signaling for dual backend; version bumped to 1.6

_Process loop files updated:_
- `process/README.md` — updated "Process Governance" section from "Git-Native" to backend-aware; updated artifact output references in loop tables and feedback diagram
- `process/1-discover/AGENT.md` — updated signal drafting, mission brief creation, and versioning table for dual backend; version bumped to 1.3
- `process/1-discover/GUIDE.md` — added issue backend signal creation instructions alongside git-files; updated mission brief creation and submission for dual backend
- `process/2-build/AGENT.md` — updated task intake, decision records, and submission for dual backend; version bumped to 1.4
- `process/2-build/GUIDE.md` — updated decision recording, exit criteria, and status updates for dual backend
- `process/3-ship/AGENT.md` — updated release contract storage, task verification, outcome reports, feedback loop, versioning table, and open tasks rule for dual backend; version bumped to 1.3
- `process/3-ship/GUIDE.md` — updated signal references, release contract reference, and exit criteria for dual backend
- `process/4-operate/AGENT.md` — updated cross-layer interaction, signal filing, postmortem storage, signal generation, versioning table, and continuous improvement signals for dual backend; version bumped to 1.2
- `process/4-operate/GUIDE.md` — updated feedback loop diagram and signal filing references for dual backend

_Archive policy updated:_
- `docs/archive-policy.md` — restructured for dual backend: git-files mechanics (archive/ subfolders, git mv) and issue backend mechanics (close issues with final status labels); updated agent integration section; version bumped to 1.1

_Consistency fixes:_
- Updated regressed `Last updated` and changelog dates in the dual-backend rollout files so the framework metadata matches the current change date and remains auditable

---

### Added (previous)

**Framework taxonomy cleanup for generic adoption (Issue #concept-review)**

_Execution divisions:_
- `CONFIG.yaml` — bumped `framework_version` from `2.2.0` to `2.3.0`; removed `ai-intelligence` and `quality-security-engineering` from default division lists and kept them as commented optional extensions instead
- `org/README.md` — added version metadata and reframed execution divisions into core defaults, optional extensions, and company-specific product divisions; clarified that Quality & Security Engineering should not be implied as a default standalone split
- `CUSTOMIZATION-GUIDE.md` — updated division customization guidance so AI & Intelligence, GTM Web, and Quality & Security Engineering are treated as optional extensions rather than assumed defaults
- `org/3-execution/divisions/engineering-foundation/DIVISION.md`, `org/3-execution/divisions/core-services/DIVISION.md`, `org/3-execution/divisions/infrastructure-operations/DIVISION.md`, `org/3-execution/divisions/legal/DIVISION.md`, `org/3-execution/divisions/ai-intelligence/DIVISION.md` — removed stale assumptions that Quality & Security Engineering is a mandatory adjacent default and aligned interfaces with the new split between execution implementation and Quality-layer governance

_Agent registry guidance:_
- `org/agents/README.md` — added version metadata plus explicit criteria for what belongs in the base template, when to use configuration instead of new agent types, and common anti-patterns such as tool-level and task-level agent definitions
- `org/agents/execution/README.md` — added version metadata, a recommended execution starter set, and consolidation guidance for deploy, monitoring, coding, and customer-service agent boundaries

_Targeted execution-agent cleanup:_
- `org/agents/execution/feature-flag-agent.md` — deprecated in favor of `exec-deploy-agent`
- `org/agents/execution/canary-agent.md` — deprecated in favor of `exec-deploy-agent`
- `org/agents/execution/rollback-agent.md` — deprecated in favor of `exec-deploy-agent`
- `org/agents/execution/team-specific-coding-agents.md` — deprecated in favor of `exec-coding-agent-fleet`
- `examples/generic-feature-lifecycle.md` — updated rollout example to use `deploy-agent` for feature-flag management to match the cleaned execution taxonomy

**Connector pattern foundation for real system integrations (Issue #10)**

_Integration architecture and governance:_
- `docs/integrations/connector-pattern.md` — new reference pattern for MCP/A2A/business-system connectors with capability levels (L1–L4), read-only-first rollout, policy-gated side effects, and observability requirements
- `org/integrations/README.md` — added explicit side-effect gating model (`none`/`low`/`high`) and link to connector pattern guidance
- `org/integrations/_TEMPLATE-integration.md` — template v1.0 → v1.1: added `Access Mode`, `Side-Effect Level`, and `Approval Mode` fields; extended security/compliance and validation checklist; updated template changelog

**Work deduplication — Rule 12: Deduplicate before acting**

> Multi-agent systems are prone to duplicate work — multiple agents independently creating issues, PRs, or artifacts for the same problem. This rule makes deduplication a first-class obligation at every layer.

_Global agent rules:_
- `AGENTS.md` Rule 12 — new non-negotiable rule: search for existing work before creating PRs, issues, branches, or signals. Close duplicates immediately.

_Orchestration Layer:_
- `org/2-orchestration/AGENT.md` — new "Work Deduplication" section: mandatory overlap scan across active missions, open PRs, and TASKS.md before decomposing or dispatching work.

_Execution Layer:_
- `org/3-execution/AGENT.md` — new "Work Deduplication" section: mandatory duplicate check before creating PRs, issues, or branches. Check `Linked PRs/Issues` field on tasks.

_Templates:_
- `work/missions/_TEMPLATE-tasks.md` — added `Linked PRs/Issues` field per task to track active PRs/issues and prevent parallel work on the same task.

**Upstream contribution workflow — Rule 13a clarified: upstream-first for generic changes**

> Rule 13a (formerly 12a) now explicitly recommends upstream-first workflow for generic improvements. When a change is identified as non-company-specific during planning, open the PR against the upstream repo first, then adopt downstream. Local-first is acceptable for urgent or experimental changes, but must be followed by an upstream PR to prevent invisible drift.

_Note:_ Previous Rule 12 (framework ecosystem participation) is now Rule 13. References updated in `CUSTOMIZATION-GUIDE.md`.

---

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
- `docs/placeholder-check.md` — full guidance on what is detected, what is excluded, per-file opt-out (`<!-- placeholder-ok -->`), and how to fix violations
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
- `docs/file-guide.md` — moved from root `file-guide.md`; all cross-references updated
- `docs/runtimes/openclaw.md` — moved from `docs/OPENCLAW-SETUP.md` into new `docs/runtimes/` directory for runtime-specific guides
- `docs/runtimes/README.md` — new index for the runtimes directory
- `docs/README.md` — new index for the docs directory
- `AGENT-BOOTSTRAP-PROMPT.md` — deleted; bootstrap content consolidated into `CUSTOMIZATION-GUIDE.md` Step 6
- `docs/MINIMAL-STARTUP-LOOP.md` — deleted; minimal fleet content moved to new `CUSTOMIZATION-GUIDE.md` "Minimal Agent Fleet" section
- `CUSTOMIZATION-GUIDE.md` — added "Minimal Agent Fleet" section (3-agent starting point, self-sustaining loop, scaling guidance) and "Step 6 — Bootstrap Your Agents" section
- `.claude/skills/deploy/SKILL.md` — updated `/deploy` skill to full PR workflow: branch → commit → push → PR → CI watch → merge → return to main (previously stopped after push)
- `CODEOWNERS`, `CONTRIBUTING.md`, `OPERATING-MODEL.md`, `README.md`, `AGENTS.md` — updated all references from deleted/moved files to new paths
- `docs/placeholder-check.md` — removed `AGENT-BOOTSTRAP-PROMPT.md` from exclude list
- `docs/required-github-settings.md` — added context notes for OSS template vs. company fork
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
- `file-guide.md` — Orientation guide for repo structure

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
