# docs/ — Operator Guides & Reference Documentation
<!-- placeholder-ok -->

> This folder contains operator guides and reference documentation for the Agentic Enterprise framework.
> For the framework overview, start with [`OPERATING-MODEL.md`](../OPERATING-MODEL.md) at the root.
> For initial setup, start with [`CUSTOMIZATION-GUIDE.md`](../CUSTOMIZATION-GUIDE.md) at the root.

---

## Start Here

Pick the shortest path that matches what you are trying to do:

| If you need to... | Read this first | Then read |
|---|---|---|
| Understand what belongs where in the repo | [`FILE-GUIDE.md`](FILE-GUIDE.md) | [`mission-lifecycle.md`](mission-lifecycle.md) if you are working on missions |
| Choose or configure a work backend | [`WORK-BACKENDS.md`](WORK-BACKENDS.md) | [`GITHUB-ISSUES.md`](GITHUB-ISSUES.md) for the GitHub issue backend |
| Make GitHub governance enforceable | [`REQUIRED-GITHUB-SETTINGS.md`](REQUIRED-GITHUB-SETTINGS.md) | [`github/README.md`](github/README.md) |
| Understand mission flow and status gates | [`mission-lifecycle.md`](mission-lifecycle.md) | [`WORK-BACKENDS.md`](WORK-BACKENDS.md) for backend differences |
| Work on CI or policy gates | One of the CI feature guides below | [`AUTOMATION-PATTERNS.md`](AUTOMATION-PATTERNS.md) for script-vs-agent guidance |
| Implement telemetry or observability | [`OTEL-CONTRACT.md`](OTEL-CONTRACT.md) | [`../examples/observability/agent-span-example.md`](../examples/observability/agent-span-example.md) |

---

## Template vs. Company Fork

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
| [`GITHUB-ISSUES.md`](GITHUB-ISSUES.md) | Setup reference | ✅ Framework doc | **Keep** — concrete GitHub issue-backend implementation guide |
| [`WORK-BACKENDS.md`](WORK-BACKENDS.md) | Setup reference | ✅ Framework doc | **Keep** — guide to work backend choice (git-files vs. issue tracker) |

---

## Core Guides

These are the primary docs most operators need.

| Guide | Purpose |
|---|---|
| [`FILE-GUIDE.md`](FILE-GUIDE.md) | Maps every root file to a category (OSS infrastructure, company content, or agent bootstrap). Answers "what do I keep, what do I delete?" for every file including `.github/` configs. |
| [`REQUIRED-GITHUB-SETTINGS.md`](REQUIRED-GITHUB-SETTINGS.md) | Checklist for GitHub branch protection, CODEOWNERS enforcement, and required status checks. Without this, PRs are advisory — not binding. |
| [`WORK-BACKENDS.md`](WORK-BACKENDS.md) | Canonical backend guide: backend choice, `CONFIG.yaml` structure, artifact placement, migration paths, and backend-specific behavior. |
| [`GITHUB-ISSUES.md`](GITHUB-ISSUES.md) | GitHub issue-backend operations guide: project setup, labels, issue forms, handoff rules, and human approval flow. |
| [`mission-lifecycle.md`](mission-lifecycle.md) | End-to-end mission lifecycle: status transitions, Divide & Conquer decomposition, gate requirements, anti-patterns. Required reading for Orchestration and Execution agents. |

---

## Platform Implementation

Guides for implementing the framework on specific platforms (GitHub, GitLab, etc.).

| Guide | Purpose |
|---|---|
| [`github/README.md`](github/README.md) | GitHub instance kit: platform overview, Projects guidance, reference workflows, and the colocated issue-template assets used by company forks. |
| [`AUTOMATION-PATTERNS.md`](AUTOMATION-PATTERNS.md) | Script-first, LLM-second principle. Classification of what to automate via scripts vs. what needs LLM agents. |

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

## Compliance Reference Docs

Per-standard compliance reference documents with article-level mappings, observability evidence sources, and external references.

| Guide | Standard |
|---|---|
| [`compliance/README.md`](compliance/README.md) | Index and overview of all compliance references |
| [`compliance/iso-27001.md`](compliance/iso-27001.md) | ISO/IEC 27001:2022 — Information Security Management |
| [`compliance/soc2.md`](compliance/soc2.md) | SOC 2 Type II — Trust Service Criteria |
| [`compliance/gdpr.md`](compliance/gdpr.md) | GDPR — EU Data Protection Regulation |
| [`compliance/iso-42001.md`](compliance/iso-42001.md) | ISO/IEC 42001:2023 — AI Management Systems |
| [`compliance/nist-ai-rmf.md`](compliance/nist-ai-rmf.md) | NIST AI RMF — AI Risk Management Framework |
| [`compliance/eu-ai-act.md`](compliance/eu-ai-act.md) | EU AI Act — European AI Regulation |

---

## Consistency Rules

The docs folder now follows a simple split:

- `WORK-BACKENDS.md` is the single source of truth for backend selection and configuration.
- `GITHUB-ISSUES.md` is the single source of truth for GitHub issue-backend operations.
- `OTEL-CONTRACT.md` is the single source of truth for telemetry naming, attributes, and metrics.
- `README.md` is only a navigation layer and should stay short.

---

## Adding a Runtime Guide

To document a new agent runtime, see [`runtimes/README.md`](runtimes/README.md).
