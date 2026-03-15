<p align="center">
  <img src="https://img.shields.io/badge/model-Agentic%20Enterprise-blueviolet" alt="Agentic Enterprise">
  <img src="https://img.shields.io/badge/version-3.0.0-brightgreen" alt="Version">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/badge/runtime-bring%20your%20own-orange" alt="Runtime">
  <a href="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml">
    <img src="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml/badge.svg" alt="Validate Framework">
  </a>
  <br>
  <img src="https://img.shields.io/badge/ISO_27001-~90%25_covered-0e8a16" alt="ISO 27001">
  <img src="https://img.shields.io/badge/SOC_2-~90%25_covered-1d76db" alt="SOC 2">
  <img src="https://img.shields.io/badge/GDPR-~75%25_covered-d93f0b" alt="GDPR">
  <img src="https://img.shields.io/badge/ISO_42001-~80%25_covered-5319e7" alt="ISO 42001">
  <img src="https://img.shields.io/badge/NIST_AI_RMF-~85%25_covered-fbca04" alt="NIST AI RMF">
  <img src="https://img.shields.io/badge/EU_AI_Act-~85%25_covered-0e8a16" alt="EU AI Act">
  <img src="https://img.shields.io/badge/NIST_CSF_2.0-~95%25_covered-0e8a16" alt="NIST CSF 2.0">
  <img src="https://img.shields.io/badge/ISO_9001-~85%25_covered-0e8a16" alt="ISO 9001">
  <img src="https://img.shields.io/badge/ISO_22301-~70%25_covered-fbca04" alt="ISO 22301">
  <img src="https://img.shields.io/badge/CCPA%2FCPRA-~75%25_covered-d93f0b" alt="CCPA/CPRA">
  <img src="https://img.shields.io/badge/HIPAA-~70%25_covered-b60205" alt="HIPAA">
</p>

<h1 align="center">Agentic Enterprise</h1>

<p align="center">
  <strong>Run your entire company as a Git repository.<br>5 layers. 4 loops. Zero legacy ceremony.</strong>
</p>

<p align="center">
  <a href="https://wlfghdr.github.io/agentic-enterprise/"><strong>Website & Interactive Demo</strong></a>
</p>

<p align="center">
  <a href="#what-is-agentic-enterprise">What Is This</a> ·
  <a href="#the-operating-loop">Operating Loop</a> ·
  <a href="#operational-proof">Proof</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#ecosystem--integrations">Ecosystem</a> ·
  <a href="#enterprise-compliance-readiness">Compliance</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

## What Is Agentic Enterprise?

**Agentic Enterprise** is a complete, open-source operating model for running an organization with AI agents — expressed entirely as a Git repository. A [reference organization](#operational-proof) runs it end-to-end: **440+ commits, 108 PRs, 99 work items** — all governed through this framework.

| Problem | This Framework's Answer |
|---------|------------------------|
| AI agents need governance, not just prompts | 5-layer model with boundaries, CODEOWNERS RACI, policy enforcement |
| Legacy processes don't work for agent fleets | Git-native: PRs = decisions, CI/CD = quality gates |
| No standard for human + agent collaboration | Humans steer and decide, agents execute and evaluate |
| Enterprise AI stalls at "cool demo" | 15 divisions, 19 quality policies, 4 process loops, 11 compliance frameworks |

**Three layers, clearly separated:** This repo is the **framework** (templates, policies, processes). You bring the **runtime** (Claude, OpenAI, CrewAI, LangGraph — any agent platform). You connect **observability** (OpenTelemetry-native). The framework is runtime-agnostic.

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

## Operational Proof

The framework is exercised by a **reference organization** that runs the operating model end-to-end — maintaining both the framework itself (self-improving) and a fully functional application.

| Metric | Count |
|--------|------:|
| **Work items** (signals, missions, tasks) | 99 |
| **Pull Requests** (governed, reviewed, merged) | 108 |
| **Commits** (auditable change trail) | 440+ |

Every artifact traces: Signal → Mission → PR → Release → New Signal. The Git history is the proof.

**[Full reference org details →](docs/reference-organization/sandboxcorp.md)** · **[End-to-end example →](examples/e2e-loop/)** · **[Architecture overview →](docs/architecture/agentic-enterprise-architecture.md)**

---

## Quickstart

**[10-Minute Walkthrough →](docs/quickstart/10-minute-agentic-enterprise.md)** — Understand the full workflow in 10 minutes.

**[Minimal Adoption Guide →](docs/adoption/minimal-adoption.md)** — Start today, no agents required.

```bash
git clone https://github.com/wlfghdr/agentic-enterprise.git
cd agentic-enterprise
```

1. Fill in `CONFIG.yaml` · 2. Replace `{{PLACEHOLDER}}` variables ([guide](CUSTOMIZATION-GUIDE.md)) · 3. Customize divisions · 4. Set up `CODEOWNERS` · 5. File your first signal

> [docs/file-guide.md](docs/file-guide.md) maps every file to one of three categories — read it before editing.

---

## Ecosystem & Integrations

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
| **NIST CSF 2.0** | ~95% | | **ISO 42001** | ~80% |
| **ISO 27001** | ~90% | | **GDPR** | ~75% |
| **SOC 2 Type II** | ~90% | | **EU AI Act** | ~75% |
| **NIST AI RMF** | ~85% | | **CCPA/CPRA** | ~75% |
| **ISO 9001** | ~85% | | **ISO 22301** | ~70% |
|  |  | | **HIPAA** | ~70% |

> Certification requires an independent audit of your running system. This repo provides the **governance scaffolding**. Gaps tracked as [open issues](https://github.com/wlfghdr/agentic-enterprise/issues?q=label%3Agap). Per-standard reference docs in [`docs/compliance/`](docs/compliance/).

---

## Repository Structure

```
agentic-enterprise/
├── CONFIG.yaml              ← Central config (fill FIRST)
├── AGENTS.md                ← Global agent instructions
├── CODEOWNERS               ← RACI — who approves what
├── org/                     ← 5-layer org structure + 15 divisions + 19 policies
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
  <strong>The future of enterprise is not more meetings. It's a Git repository that runs itself.</strong>
</p>

<p align="center">
  <a href="https://github.com/wlfghdr/agentic-enterprise">Star this repo</a> ·
  <a href="https://github.com/wlfghdr/agentic-enterprise/fork">Fork it</a> ·
  <a href="https://github.com/wlfghdr/agentic-enterprise/discussions">Join the discussion</a>
</p>
