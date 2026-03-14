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
| Understand what belongs where in the repo | [`file-guide.md`](file-guide.md) | [`mission-lifecycle.md`](mission-lifecycle.md) if you are working on missions |
| Choose or configure a work backend | [`work-backends.md`](work-backends.md) | [`github-issues.md`](github-issues.md) for the GitHub issue backend |
| Make GitHub governance enforceable | [`required-github-settings.md`](required-github-settings.md) | [`github/README.md`](github/README.md) |
| Understand mission flow and status gates | [`mission-lifecycle.md`](mission-lifecycle.md) | [`work-backends.md`](work-backends.md) for backend differences |
| Work on CI or policy gates | One of the CI feature guides below | [`automation-patterns.md`](automation-patterns.md) for script-vs-agent guidance |
| Implement telemetry or observability | [`otel-contract.md`](otel-contract.md) | [`../examples/observability/agent-span-example.md`](../examples/observability/agent-span-example.md) |

---

## Template vs. Company Fork

Each document falls into one of three categories:

| Document | Category | Template repo | Company fork |
|---|---|---|---|
| [`file-guide.md`](file-guide.md) | Setup reference | ✅ Framework doc | **Keep** — read once during fork setup to understand what each root file does |
| [`required-github-settings.md`](required-github-settings.md) | Setup reference | ✅ Applies to both | **Apply** — configure branch protection and CODEOWNERS before going live |
| [`runtimes/README.md`](runtimes/README.md) | Runtime reference | ✅ Framework doc | **Keep** as runtime guide index |
| [`runtimes/openclaw.md`](runtimes/openclaw.md) | Runtime reference | ✅ Framework doc | **Keep** if using OpenClaw; ignore otherwise |
| [`policy-as-code.md`](policy-as-code.md) | CI feature | ✅ Template CI gate | **Keep** if using OPA/Conftest gate; delete otherwise |
| [`security-scanning.md`](security-scanning.md) | CI feature | ✅ Template CI gate | **Keep** if using Gitleaks/Dependency Review; delete otherwise |
| [`lock-enforcement.md`](lock-enforcement.md) | CI feature | ✅ Template CI gate | **Keep** if using lock enforcement; delete otherwise |
| [`placeholder-check.md`](placeholder-check.md) | CI feature | ✅ Template CI gate | **Keep** if using placeholder CI gate; delete otherwise |
| [`schema-guide.md`](schema-guide.md) | CI feature | ✅ Template CI gate | **Keep** if using schema validation; delete otherwise |
| [`mission-lifecycle.md`](mission-lifecycle.md) | Process reference | ✅ Framework doc | **Keep** — mission lifecycle, status transitions, Divide & Conquer pattern |
| [`github-issues.md`](github-issues.md) | Setup reference | ✅ Framework doc | **Keep** — concrete GitHub issue-backend implementation guide |
| [`work-backends.md`](work-backends.md) | Setup reference | ✅ Framework doc | **Keep** — guide to work backend choice (git-files vs. issue tracker) |

---

## Core Guides

These are the primary docs most operators need.

| Guide | Purpose |
|---|---|
| [`file-guide.md`](file-guide.md) | Maps every root file to a category (OSS infrastructure, company content, or agent bootstrap). Answers "what do I keep, what do I delete?" for every file including `.github/` configs. |
| [`required-github-settings.md`](required-github-settings.md) | Checklist for GitHub branch protection, CODEOWNERS enforcement, and required status checks. Without this, PRs are advisory — not binding. |
| [`work-backends.md`](work-backends.md) | Canonical backend guide: backend choice, `CONFIG.yaml` structure, artifact placement, migration paths, and backend-specific behavior. |
| [`github-issues.md`](github-issues.md) | GitHub issue-backend operations guide: project setup, labels, issue forms, handoff rules, and human approval flow. |
| [`mission-lifecycle.md`](mission-lifecycle.md) | End-to-end mission lifecycle: status transitions, Divide & Conquer decomposition, gate requirements, anti-patterns. Required reading for Orchestration and Execution agents. |

---

## Platform Implementation

Guides for implementing the framework on specific platforms (GitHub, GitLab, etc.).

| Guide | Purpose |
|---|---|
| [`github/README.md`](github/README.md) | GitHub instance kit: platform overview, Projects guidance, reference workflows, and the colocated issue-template assets used by company forks. |
| [`automation-patterns.md`](automation-patterns.md) | Script-first, LLM-second principle. Classification of what to automate via scripts vs. what needs LLM agents. |

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
| [`policy-as-code.md`](policy-as-code.md) | OPA/Rego + Conftest enforcement (workflow permissions, pinned action refs) |
| [`security-scanning.md`](security-scanning.md) | Gitleaks secret scanning + GitHub Dependency Review |
| [`lock-enforcement.md`](lock-enforcement.md) | Lock files for protected paths (prevents concurrent edits to critical docs) |
| [`placeholder-check.md`](placeholder-check.md) | Blocks PRs with unfilled `{{VAR}}`, `[TODO]`, `[TBD]` placeholders |
| [`schema-guide.md`](schema-guide.md) | JSON Schema validation for `CONFIG.yaml` and work artifact markdown |

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

- `work-backends.md` is the single source of truth for backend selection and configuration.
- `github-issues.md` is the single source of truth for GitHub issue-backend operations.
- `otel-contract.md` is the single source of truth for telemetry naming, attributes, and metrics.
- `README.md` is only a navigation layer and should stay short.

---

## Adding a Runtime Guide

To document a new agent runtime, see [`runtimes/README.md`](runtimes/README.md).
