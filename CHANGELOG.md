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
