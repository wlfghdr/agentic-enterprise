# docs/ — Operator Guides & Reference Documentation
<!-- placeholder-ok -->

> This folder contains operator guides and reference documentation for the Agentic Enterprise framework.
> For the framework overview, start with [`OPERATING-MODEL.md`](../OPERATING-MODEL.md) at the root.
> For initial setup, start with [`CUSTOMIZATION-GUIDE.md`](../CUSTOMIZATION-GUIDE.md) at the root.

---

## Template vs. Company Fork — Which Docs Apply to You?

Each document falls into one of three categories:

| Document | Category | Template repo | Company fork |
|---|---|---|---|
| [`FILE-GUIDE.md`](FILE-GUIDE.md) | Setup reference | ✅ Framework doc | **Keep** — read once during fork setup to understand what each root file does |
| [`REQUIRED-GITHUB-SETTINGS.md`](REQUIRED-GITHUB-SETTINGS.md) | Setup reference | ✅ Applies to both | **Apply** — configure branch protection and CODEOWNERS before going live |
| [`runtimes/README.md`](runtimes/README.md) | Runtime reference | ✅ Framework doc | **Keep** as runtime guide index |
| [`runtimes/openclaw.md`](runtimes/openclaw.md) | Runtime reference | ✅ Framework doc | **Keep** if using OpenClaw; ignore otherwise |
| [`POLICY-AS-CODE.md`](POLICY-AS-CODE.md) | CI feature | ✅ Template CI gate | **Keep** if using OPA/Conftest gate; delete otherwise |
| [`SECURITY-SCANNING.md`](SECURITY-SCANNING.md) | CI feature | ✅ Template CI gate | **Keep** if using Gitleaks/Dependency Review; delete otherwise |
| [`LOCK-ENFORCEMENT.md`](LOCK-ENFORCEMENT.md) | CI feature | ✅ Template CI gate | **Keep** if using lock enforcement; delete otherwise |
| [`PLACEHOLDER-CHECK.md`](PLACEHOLDER-CHECK.md) | CI feature | ✅ Template CI gate | **Keep** if using placeholder CI gate; delete otherwise |
| [`SCHEMA-GUIDE.md`](SCHEMA-GUIDE.md) | CI feature | ✅ Template CI gate | **Keep** if using schema validation; delete otherwise |
| [`mission-lifecycle.md`](mission-lifecycle.md) | Process reference | ✅ Framework doc | **Keep** — mission lifecycle, status transitions, Divide & Conquer pattern |

---

## Setup Reference Guides

Guides that help you bootstrap a new fork or understand the framework structure.

| Guide | Purpose |
|---|---|
| [`FILE-GUIDE.md`](FILE-GUIDE.md) | Maps every root file to a category (OSS infrastructure, company content, or agent bootstrap). Answers "what do I keep, what do I delete?" for every file including `.github/` configs. |
| [`REQUIRED-GITHUB-SETTINGS.md`](REQUIRED-GITHUB-SETTINGS.md) | Checklist for GitHub branch protection, CODEOWNERS enforcement, and required status checks. Without this, PRs are advisory — not binding. |
| [`mission-lifecycle.md`](mission-lifecycle.md) | End-to-end mission lifecycle: status transitions, Divide & Conquer decomposition, gate requirements, anti-patterns. Required reading for Orchestration and Execution agents. |

---

## Runtime Implementation Guides

Guides for connecting specific agent runtimes and platforms to the framework. The framework core is runtime-agnostic — these guides cover runtime-specific configuration only.

| Guide | Purpose |
|---|---|
| [`runtimes/README.md`](runtimes/README.md) | Index of available runtime guides. Explains the runtime-agnostic principle and how to contribute a new runtime guide. |
| [`runtimes/openclaw.md`](runtimes/openclaw.md) | Complete OpenClaw setup: fleet sizing, model tier strategy, heartbeat scheduling, auto-merge gates, cost and reliability controls. |

---

## CI Feature Guides

Reference documentation for the CI/automation gates that ship with the template. Each gate enforces a specific aspect of framework governance. These guides explain how to run the checks locally, interpret results, and extend or disable a gate.

| Guide | CI gate it documents |
|---|---|
| [`POLICY-AS-CODE.md`](POLICY-AS-CODE.md) | OPA/Rego + Conftest enforcement (workflow permissions, pinned action refs) |
| [`SECURITY-SCANNING.md`](SECURITY-SCANNING.md) | Gitleaks secret scanning + GitHub Dependency Review |
| [`LOCK-ENFORCEMENT.md`](LOCK-ENFORCEMENT.md) | Lock files for protected paths (prevents concurrent edits to critical docs) |
| [`PLACEHOLDER-CHECK.md`](PLACEHOLDER-CHECK.md) | Blocks PRs with unfilled `{{VAR}}`, `[TODO]`, `[TBD]` placeholders |
| [`SCHEMA-GUIDE.md`](SCHEMA-GUIDE.md) | JSON Schema validation for `CONFIG.yaml` and work artifact markdown |

---

## Adding a Runtime Guide

To document a new agent runtime, see [`runtimes/README.md`](runtimes/README.md).
