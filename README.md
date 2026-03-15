<p align="center">
  <img src="https://img.shields.io/badge/model-Agentic%20Enterprise-blueviolet" alt="Agentic Enterprise">
  <img src="https://img.shields.io/badge/version-4.0.0-brightgreen" alt="Version">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/badge/runtime-bring%20your%20own-orange" alt="Runtime">
  <a href="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml">
    <img src="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml/badge.svg" alt="Validate Framework">
  </a>
  <br>
  <img src="https://img.shields.io/badge/ISO_27001-~90%25_covered-0e8a16" alt="ISO 27001">
  <img src="https://img.shields.io/badge/SOC_2-~90%25_covered-1d76db" alt="SOC 2">
  <img src="https://img.shields.io/badge/GDPR-~75%25_covered-d93f0b" alt="GDPR">
  <img src="https://img.shields.io/badge/ISO_42001-~85%25_covered-5319e7" alt="ISO 42001">
  <img src="https://img.shields.io/badge/NIST_AI_RMF-~90%25_covered-fbca04" alt="NIST AI RMF">
  <img src="https://img.shields.io/badge/EU_AI_Act-~85%25_covered-0e8a16" alt="EU AI Act">
  <img src="https://img.shields.io/badge/NIST_CSF_2.0-~95%25_covered-0e8a16" alt="NIST CSF 2.0">
  <img src="https://img.shields.io/badge/ISO_9001-~85%25_covered-0e8a16" alt="ISO 9001">
  <img src="https://img.shields.io/badge/ISO_22301-~70%25_covered-fbca04" alt="ISO 22301">
  <img src="https://img.shields.io/badge/CCPA%2FCPRA-~75%25_covered-d93f0b" alt="CCPA/CPRA">
  <img src="https://img.shields.io/badge/HIPAA-~70%25_covered-b60205" alt="HIPAA">
</p>

<h1 align="center">Agentic Enterprise</h1>

<p align="center">
  <strong>Govern AI-assisted work through a repository-backed operating model.<br>5 layers. 4 loops. Explicit accountability.</strong>
</p>

<p align="center">
  <a href="https://wlfghdr.github.io/agentic-enterprise/"><strong>Live Demo</strong></a> ·
  <a href="https://wlfghdr.github.io/agentic-enterprise/concept-visualization.html"><strong>Reference Scenario</strong></a> ·
  <a href="docs/adoption/minimal-adoption.md"><strong>Minimal Adoption</strong></a>
</p>

<p align="center">
  <a href="#choose-your-path">Choose a Path</a> ·
  <a href="#executive-reality-check">Reality Check</a> ·
  <a href="#see-it-in-motion">See It In Motion</a> ·
  <a href="#start-minimal-adoption">Start Minimal Adoption</a> ·
  <a href="#the-operating-loop">Operating Loop</a> ·
  <a href="#public-proof">Proof</a> ·
  <a href="#runtimes--integrations">Runtimes</a> ·
  <a href="#enterprise-compliance-readiness">Compliance</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

## Choose Your Path

| If you want to... | Start here | What you get |
|---------|------------------------|-------------|
| **Understand the operating model** | [10-Minute Walkthrough](docs/quickstart/10-minute-agentic-enterprise.md) · [org/README.md](org/README.md) | The 5 layers, 4 loops, and core artifact flow in the shortest useful path |
| **Stress-test the concept** | [Executive Reality Check](docs/executive-reality-check.md) | Candid answers to the objections a CTO, CEO, COO, or CFO should raise before adopting the framework |
| **See it in motion** | [Live demo](https://wlfghdr.github.io/agentic-enterprise/) · [Reference scenario](https://wlfghdr.github.io/agentic-enterprise/concept-visualization.html) | The public proof layer, driven by [`index.html`](index.html) and [`concept-visualization.html`](concept-visualization.html) |
| **Start minimal adoption** | [Minimal Adoption Guide](docs/adoption/minimal-adoption.md) | A no-agents-required path: fork, configure, use signals + missions + PRs |

## What Is Agentic Enterprise?

**Agentic Enterprise** is an open-source operating model for running work through a governed Git repository. Humans decide. Agents execute and evaluate. Git history becomes the audit trail.

Keep these terms separate:

- **Operating model:** this repo's templates, policies, process loops, and agent instructions
- **Demo / reference scenario:** the public proof assets in [`index.html`](index.html) and [`concept-visualization.html`](concept-visualization.html)
- **Runtime:** your agent platform of choice
- **Observability:** your OpenTelemetry-native evidence layer
- **Adoption:** start with Git, CODEOWNERS, signals, missions, and PRs; add agents later if you want

The repo is the governance backbone. You bring the runtime, observability platform, and domain systems that actually execute business operations. The framework stays runtime-agnostic.

---

## Executive Reality Check

Before you buy the story, challenge these points directly:

| Challenge | Honest answer |
|-----------|---------------|
| **Is this a replacement for Jira, ERP, CRM, ITSM, or observability?** | No. It governs decisions, approvals, work artifacts, and audit trails. Domain systems still do domain work. |
| **Do the 5 layers imply a heavy org chart?** | No. They are decision roles, not mandatory headcount. Small teams can collapse multiple layers into the same people. |
| **Is the public proof already enterprise-scale?** | Not yet. The public reference organization proves internal consistency and repeatability, not Fortune 500 operating scale. |
| **Do the compliance percentages mean certification or operating effectiveness?** | No. They measure framework scaffolding coverage. Real controls, evidence, and audits remain adopter work. |
| **Can agents run the company unattended?** | No. Humans stay accountable for scope, policy, risk, and releases. The framework reduces toil; it does not eliminate executive responsibility. |

**[Full executive diligence notes →](docs/executive-reality-check.md)**

---

## See It In Motion

The demo is a first-class onboarding asset, not side material:

- **[Live demo](https://wlfghdr.github.io/agentic-enterprise/)** shows the operating model as the public product surface
- **[Reference scenario](https://wlfghdr.github.io/agentic-enterprise/concept-visualization.html)** replays representative lifecycle patterns step by step
- **[`index.html`](index.html)** and **[`concept-visualization.html`](concept-visualization.html)** are the source files for those two proof assets
- **[Reference organization details](docs/reference-organization/sandboxcorp.md)** and the **[end-to-end example](examples/e2e-loop/)** connect the demo back to repo artifacts

---

## Start Minimal Adoption

**[Minimal Adoption Guide →](docs/adoption/minimal-adoption.md)** keeps the first real trial short and concrete.

1. Fork or clone the repo.
2. Fill in `CONFIG.yaml` and set up `CODEOWNERS`.
3. Start with signals, missions, and PRs.

**No agents required.** The operating model is useful before you add a runtime or observability platform.

---

## The Operating Loop

Every piece of work follows one loop:

```
Observe  →  Decide  →  Execute  →  Ship  →  Learn  →  Repeat
(Signal)   (Mission)    (PR)     (Release)  (Signal)
```

Git history becomes the organizational audit trail. Every decision is a PR merge. Every change is diffable, reversible, and attributable.

| Loop | Purpose | Duration | Human Touch |
|------|---------|----------|-------------|
| **1. Discover** | Signal → Mission Brief | Hours–Days | 1 Go/No-Go |
| **2. Build** | Mission → Working Software | Days–Weeks | By exception |
| **3. Ship** | Staging → GA | Days | 1 Go/No-Go |
| **4. Operate** | GA → Continuous health | 24/7 | By escalation |

Loop 4 feeds signals back into Loop 1 via telemetry — a continuous organizational metabolism.

**5 organizational layers:**

```
STEERING (0)        Executives evolve the company
STRATEGY (1)        Humans define WHY + WHAT
ORCHESTRATION (2)   Translate strategy → executable work
EXECUTION (3)       Agents do the work
QUALITY (4)         Agents evaluate against 19 policies
```

---

## Public Proof

As of **2026-03-16**, the directly inspectable public proof in [`wlfghdr/agentic-enterprise`](https://github.com/wlfghdr/agentic-enterprise) is:

| Metric | Count | What you can verify |
|--------|------:|---------------------|
| **Issues** | 88 | Repository issue history, including roadmap, compliance, and framework work |
| **Pull Requests** | 80 total / 75 merged | Governed change history with review and merge records |
| **Commits** | 239 | Auditable Git history in this repository |
| **Quality policies** | 19 | Enforceable policy domains under [`org/4-quality/policies/`](org/4-quality/policies/) |

Counts change daily. The reference-organization narrative below is intentionally scoped to what is public and verifiable from this repository, rather than cross-repo totals that readers cannot inspect from one page.

**[Full reference org details →](docs/reference-organization/sandboxcorp.md)** · **[Executive reality check →](docs/executive-reality-check.md)** · **[End-to-end example →](examples/e2e-loop/)** · **[Architecture overview →](docs/architecture/agentic-enterprise-architecture.md)**

---

## Runtimes & Integrations

Runtime-agnostic, integration-ready. The **Integration Registry** (`org/integrations/`) governs all external tool connections.

**Agent runtimes:** [Claude Code](https://claude.ai) · [OpenClaw](https://openclaw.ai) · [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) · [CrewAI](https://github.com/crewai-inc/crewAI) · [LangGraph](https://github.com/langchain-ai/langgraph) — load `AGENT.md` hierarchy as instructions.

**Protocols:** Git + Markdown (primary) · OpenTelemetry (real-time) · [MCP](https://github.com/modelcontextprotocol/specification) (tool connection) · [A2A](https://github.com/google/A2A) (cross-agent)

<details>
<summary><strong>Agent bootstrap prompt</strong></summary>

```
Read these files in order:
1. AGENTS.md — Global rules for every agent
2. org/<your-layer>/AGENT.md — Your layer's instructions
3. org/4-quality/policies/ — Mandatory quality policies
4. work/missions/ — Current mission context
```

See [docs/runtimes/](docs/runtimes/) for platform-specific setup guides.

</details>

---

## Enterprise Compliance Readiness

Built-in governance controls mapped to 11 certification frameworks. Honest self-assessments, not certification stamps.

| Framework | Coverage | | Framework | Coverage |
|-----------|----------|-|-----------|----------|
| **NIST CSF 2.0** | ~95% | | **ISO 42001** | ~85% |
| **ISO 27001** | ~90% | | **GDPR** | ~75% |
| **SOC 2 Type II** | ~90% | | **EU AI Act** | ~85% |
| **NIST AI RMF** | ~90% | | **CCPA/CPRA** | ~75% |
| **ISO 9001** | ~85% | | **ISO 22301** | ~70% |
|  |  | | **HIPAA** | ~70% |

> Certification requires an independent audit of your running system. This repo provides the **governance scaffolding**. Adopter responsibilities tracked as [open issues](https://github.com/wlfghdr/agentic-enterprise/issues?q=label%3Acompliance). Per-standard reference docs in [`docs/compliance/`](docs/compliance/).

---

## Repository Structure

```
agentic-enterprise/
├── CONFIG.yaml              ← Central config (fill FIRST)
├── AGENTS.md                ← Global agent instructions
├── CODEOWNERS               ← RACI — who approves what
├── org/                     ← 5-layer org structure + 17 divisions + 19 policies
├── process/                 ← 4-loop lifecycle definitions
├── work/                    ← Active signals, missions, decisions, releases
├── docs/                    ← Quickstart, architecture, adoption, observability, compliance
└── examples/                ← End-to-end lifecycle example
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome framework improvements, runtime integrations, tooling, and documentation.

---

## License

[Apache License 2.0](LICENSE) — Enterprise-friendly. Use it, fork it, build on it.

---

<p align="center">
  <strong>The future of enterprise is not more meetings. It's explicit governance for AI-assisted work.</strong>
</p>

<p align="center">
  <a href="https://github.com/wlfghdr/agentic-enterprise">Star this repo</a> ·
  <a href="https://github.com/wlfghdr/agentic-enterprise/fork">Fork it</a> ·
  <a href="https://github.com/wlfghdr/agentic-enterprise/discussions">Join the discussion</a>
</p>
