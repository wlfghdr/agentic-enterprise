<p align="center">
  <img src="https://img.shields.io/badge/model-Agentic%20Enterprise-blueviolet" alt="Agentic Enterprise">
  <img src="https://img.shields.io/badge/version-3.0.0-brightgreen" alt="Version">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/badge/runtime-bring%20your%20own-orange" alt="Runtime">
  <a href="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml">
    <img src="https://github.com/wlfghdr/agentic-enterprise/actions/workflows/validate.yml/badge.svg" alt="Validate Framework">
  </a>
  <br>
  <img src="https://img.shields.io/badge/policies-14_mandatory_domains-0e8a16" alt="14 policy domains">
  <img src="https://img.shields.io/badge/trust-privacy_|_incident_|_availability-1d76db" alt="Trust surfaces">
  <img src="https://img.shields.io/badge/evidence-telemetry_backed-5319e7" alt="Telemetry backed evidence">
</p>

<h1 align="center">Agentic Enterprise</h1>

<p align="center">
  <strong>Run your entire company as a Git repository.<br>5 layers. 4 loops. Integrate everything. Zero legacy ceremony.</strong>
</p>

<p align="center">
  <a href="https://wlfghdr.github.io/agentic-enterprise/"><strong>🌐 Website & Interactive Demo →</strong></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#the-model">The Model</a> •
  <a href="#agent-bootstrap">Agent Bootstrap</a> •
  <a href="#repository-structure">Repo Structure</a> •
  <a href="#ecosystem--integrations">Ecosystem</a> •
  <a href="#known-limitations--roadmap">Roadmap</a> •
  <a href="#enterprise-trust--audit-readiness">Trust</a> •
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

## What Is This?

**Agentic Enterprise** is a complete, open-source operating model for running an organization with AI agents — expressed entirely as a Git repository. It's built for the post-ticket, post-countless-meetings, post-endless-human-discussions enterprise era: a unified, version-controlled, agent-native operating system with two native communication channels — the **repo itself** (agents read instructions as natural language files, produce artifacts, and file signals — all versioned in Git) and the **observability platform** (real-time telemetry and event exchange that feeds automated signals back into governance).

This is **not** a strategy deck. It's a **live, forkable framework** — with org structure, process definitions, agent instructions, quality policies, work artifacts, and templates — all in Markdown and YAML.

It also treats trust as an operating concern, not a brochure claim: the framework now includes explicit privacy, incident response, and availability / continuity policy surfaces so teams can define how agentic systems are governed **and** how those commitments are proven in runtime evidence.

### How to Read This Project

To avoid confusion, there are **three distinct layers** in the broader story:

1. **Agentic Enterprise** = the **public, open-source operating model** in this repository  
   The product here is the governance model: org structure, process loops, policies, repo conventions, and integration patterns.
2. **Your runtime + toolchain** = the **execution layer you bring**  
   OpenClaw, LangGraph, custom MCP servers, CI/CD, observability vendors, chat systems — this repo is designed to plug into them, not replace them.
3. **Reference implementations / proving grounds** = **evidence that the model can run**  
   Real teams need proof, not just theory. Proving grounds show the model running with actual missions, artifacts, policy checks, and feedback loops. They are proof surfaces for the framework — not the framework itself.

**In short:** Agentic Enterprise is the **operating model for agent-governed work**. Your runtime executes it. A proving ground demonstrates that it actually works.

### The Proof Model

If you need the shortest possible framing, use this:

- **Framework:** Agentic Enterprise defines how agent-governed work is structured and governed.
- **Runtime:** A concrete runtime executes the agents, tools, and automations.
- **Proof surface:** A proving ground shows the model producing visible work, evidence, and improvement loops.

What should count as proof?

- missions with clear inputs and outputs
- artifacts created through the defined layer and loop structure
- quality gates and review checkpoints that can be inspected
- feedback from operation back into new work
- reusable learnings that improve the framework itself

That distinction matters because this repository is intentionally **not** selling a closed runtime, a dashboard, or a hidden internal system. It is publishing the **operating model** that those systems can run.

### Why?

| Problem | This Framework's Answer |
|---------|------------------------|
| AI agents need governance, not just prompts | 5-layer organizational model with explicit boundaries, RACI via CODEOWNERS, and policy enforcement |
| Legacy processes (tickets, wikis, standups, endless meetings) don't work for agent fleets | Git-native governance: PRs = decisions, branches = workflow states, CI/CD = quality gates |
| No standard way to structure human + agent collaboration | Clear separation: humans steer and decide, agents execute and evaluate, Git is the system of record |
| Enterprise AI adoption stalls at "cool demo" stage | Production-grade org template with 12 divisions, 14 quality policy domains, 4 process loops |
| Agent instructions are scattered and inconsistent | Hierarchical `AGENT.md` files: global → layer → division, all version-controlled |
| Enterprises run dozens of tools that agents need to use | Integration Registry with governed connections to observability, ITSM, CI/CD, business systems |

---

## The Model

### 5 Organizational Layers

Every function in the company — engineering, marketing, sales, customer success, support — operates within the same 5-layer architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│  STEERING          Executives + agents evolve the company       │
│  org/0-steering/   C-Suite, Org Architects                      │
├─────────────────────────────────────────────────────────────────┤
│  STRATEGY          Humans define WHY + WHAT + CONSTRAINTS       │
│  org/1-strategy/   Venture Leads, Outcome Owners                │
├─────────────────────────────────────────────────────────────────┤
│  ORCHESTRATION     Translate strategy → executable work         │
│  org/2-orchestration/  Mission Leads, Fleet Managers            │
├─────────────────────────────────────────────────────────────────┤
│  EXECUTION         Agents do the work, humans own hard parts    │
│  org/3-execution/  12 divisions across eng, GTM, customer       │
├─────────────────────────────────────────────────────────────────┤
│  QUALITY           Agents evaluate, humans author policies      │
│  org/4-quality/    14 policy domains, eval agent fleets         │
└─────────────────────────────────────────────────────────────────┘
```

### 4 Process Loops

Legacy phase-gates are replaced with continuous loops:

| Loop | Purpose | Duration | Human Touch |
|------|---------|----------|-------------|
| **1. Discover & Decide** | Signal → Mission Brief | Hours–Days | 1 Go/No-Go |
| **2. Design & Build** | Mission → Working Software | Days–Weeks | By exception |
| **3. Validate & Ship** | Staging → GA | Days | 1 Go/No-Go |
| **4. Operate & Evolve** | GA → Continuous health | 24/7 | By escalation |

Loop 4 feeds signals back into Loop 1 via two channels: telemetry from the observability platform surfaces anomalies and files automated signals into `work/signals/`; agents in Discover pick them up as natural language files and initiate the next mission. A continuous organizational metabolism.

### The GitOps Revolution

| Legacy | Agentic Enterprise | Why Better |
|--------|-------------------|------------|
| Ticket system | Work artifacts in `work/` or issue tracker | Version-controlled, diffable, agent-readable; or native issue UI for human triage |
| Sprint planning | Mission briefs | Goal-oriented, not time-boxed |
| Daily standup | `git log` + dashboards | Always current, no meetings |
| Wiki / knowledge base | This repository | Single source of truth |
| RACI matrix | `CODEOWNERS` | Executable, enforced by Git |
| Status meetings | `git diff` + mission status | Self-updating, always accurate |
| Phase gates | CI/CD checks | Automated, consistent |
| Org restructuring | Evolution PRs | Transparent, reversible, evidence-based |
| Siloed tool configs | Integration Registry | Governed, auditable, agent-accessible |
| Manual monitoring setup | Observability-as-config | Declared in CONFIG.yaml, auto-wired |

### The Autonomy Curve

Every process in the enterprise follows the same maturity trajectory:

```
Manual → Recommendations → Supervised Autonomy → Full Autonomy
   │           │                    │                    │
   ▼           ▼                    ▼                    ▼
 Humans    Agents suggest,     Agents act,          Agents act,
 do all    humans decide       humans review        humans audit
```

This framework gives you the **governance infrastructure** to move right on this curve — safely, measurably, and reversibly.

### Trust, Proven Operationally

The goal is not to sound compliant. The goal is to make enterprise trust claims inspectable.

Recent policy additions make that explicit:

- **Privacy** — lawful basis, DPA, DSAR, breach handling, DPIA, consent, and transfer controls are first-class operating requirements, not side notes.
- **Incident response** — SEV1–SEV4 response targets define acknowledge / mitigate / resolve expectations with auto-escalation when reality drifts.
- **Availability & continuity** — service tiers, RTO/RPO expectations, failover and recovery runbooks, and annual drills make resilience a designed capability.
- **Observability as proof** — dashboards, traces, events, and audit evidence are part of the model so teams can verify what actually happened at runtime.

That matters because an agentic enterprise does not earn trust through policy PDFs alone. It earns trust when governance, operations, and telemetry line up.

---

## Quick Start

> **Before you start:** [docs/FILE-GUIDE.md](docs/FILE-GUIDE.md) maps every file in this repo to one of three categories — OSS infrastructure (delete in a private fork), company operating model content (fill in and own), or agent bootstrap helpers. Read it to avoid editing files you should delete, or deleting files you should fill in.

### 1. Fork & Clone

```bash
git clone https://github.com/wlfghdr/agentic-enterprise.git
cd agentic-enterprise
```

### 2. Configure Your Identity

Open `CONFIG.yaml` and fill in your company details:

```yaml
company:
  name: "Your Company"
  short_name: "YourCo"
  repo_slug: "yourco-enterprise"
  domain: "yourco.com"

vision:
  north_star: "Your aspirational sentence here."
  mission: "What you do, for whom."
```

### 3. Search & Replace Placeholders

```bash
# Replace all {{PLACEHOLDER}} variables across the repo
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_NAME}}/Your Company/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_SHORT}}/YourCo/g'
# ... see CUSTOMIZATION-GUIDE.md for the full list
```

### 4. Customize Your Divisions

Review `org/3-execution/divisions/` — keep what fits, rename or remove what doesn't. Each division has a `DIVISION.md` with agent instructions and a `README.md` with scope.

### 5. Point Your Agents

See the [Agent Bootstrap](#agent-bootstrap) section below. For runtime-specific fleet setup, see [docs/runtimes/](docs/runtimes/).

> **Detailed guide:** [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) walks through every customization step.

---

## Agent Bootstrap

Any AI agent can work within this framework. Point it at the repo and give it context about the instruction hierarchy.

### Universal Bootstrap Prompt

```
You are an agent working within the Agentic Enterprise Operating Model.

Before doing anything, read these files in order:
1. AGENTS.md — Global rules that apply to every agent
2. org/<your-layer>/AGENT.md — Your layer's specific instructions
3. The relevant quality policies in org/4-quality/policies/
4. The mission brief or task context in work/missions/

Key principles:
- Two native communication channels: the **repo** (natural language files — read instructions, produce artifacts, file signals) and the **observability platform** (real-time telemetry — emit spans as you act, consume operational data before deciding).
- Git is the governance backbone. PRs = decisions. CODEOWNERS = RACI.
- Work tracking is configurable: Markdown files in work/ or issues in an issue tracker (see CONFIG.yaml → work_backend).
- You recommend; humans decide (via PR merge or label transition).
- Every claim must be grounded in evidence.
- Stay in your lane — read your layer's boundaries.
- Surface improvement signals (to work/signals/ or as issues with artifact:signal label).

Repository structure:
- org/ — Organizational structure (5 layers)
- process/ — Process definitions (4 loops)
- work/ — Active work artifacts (missions, signals, decisions, releases)
- org/4-quality/policies/ — Quality policies (mandatory, not advisory)
```

### Platform-Specific Prompts

<details>
<summary><strong>Claude Code / Claude Projects</strong></summary>

Add this to your Claude Code `CLAUDE.md` or project system prompt:

```
Read AGENTS.md first — it is the top of the instruction hierarchy for this
agentic enterprise operating model. Then read org/<layer>/AGENT.md for your
layer and follow the process in process/<loop>/GUIDE.md for your current task.
All work artifacts go in work/. All changes via PR. CODEOWNERS is the RACI.
```

</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

Create a `.github/copilot-instructions.md`:

```
This repository is an Agentic Enterprise Operating Model. Read AGENTS.md for
global agent rules. The org/ folder contains the 5-layer organizational
structure. The process/ folder contains the 4-loop lifecycle. The work/ folder
contains active missions, signals, and decisions. Quality policies in
org/4-quality/policies/ are mandatory. All changes go through PRs.
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

Add to `.cursorrules`:

```
This is an Agentic Enterprise Operating Model repo — a framework for running
a company with AI agents via Git. Start by reading AGENTS.md (global rules),
then the layer-specific AGENT.md in org/. Quality policies in
org/4-quality/policies/ are mandatory. Work artifacts go in work/.
Changes via PR. CODEOWNERS enforces RACI.
```

</details>

<details>
<summary><strong>OpenClaw (openclaw.ai)</strong></summary>

OpenClaw is a self-hosted AI gateway that connects chat interfaces (WhatsApp, Telegram, Discord, iMessage) to AI agents. To use it with this framework:

```yaml
# In your OpenClaw skill configuration
name: agentic-enterprise
description: "Agentic Enterprise Operating Model agent"
instructions: |
  You operate within the Agentic Enterprise Operating Model.
  Read AGENTS.md for global rules. The instruction hierarchy is:
  AGENTS.md → org/<layer>/AGENT.md → division DIVISION.md → mission brief.
  All work goes in work/. All changes via Git PR. CODEOWNERS = RACI.
  Surface improvement signals to work/signals/.
tools:
  - github  # OpenClaw's built-in GitHub integration
```

OpenClaw's persistent memory, multi-channel routing, and 50+ integrations make it an excellent companion for operationalizing this framework beyond the Git interface. See [openclaw.ai](https://openclaw.ai) and [docs.openclaw.ai](https://docs.openclaw.ai).

> **Operational guide available:** For a complete setup reference — agent fleet sizing, model tier assignment, heartbeat strategy, auto-merge gates, and self-organizing artifact loops — see [`docs/runtimes/openclaw.md`](docs/runtimes/openclaw.md).

</details>

<details>
<summary><strong>OpenAI Agents SDK / CrewAI / LangGraph</strong></summary>

```python
# OpenAI Agents SDK
from agents import Agent

enterprise_agent = Agent(
    name="Enterprise Agent",
    instructions="""You operate within the Agentic Enterprise Operating Model.
    Read AGENTS.md for global rules. Follow the instruction hierarchy:
    AGENTS.md → org/<layer>/AGENT.md → DIVISION.md → mission brief.
    All changes via Git PR. CODEOWNERS = RACI. Surface signals to work/signals/.""",
    tools=[github_tool, file_tool],
)

# CrewAI
from crewai import Agent as CrewAgent

enterprise_agent = CrewAgent(
    role="Execution Agent",
    goal="Complete missions within the Agentic Enterprise framework",
    backstory="Read AGENTS.md and org/3-execution/AGENT.md for your instructions.",
)

# LangGraph — use the instruction files as state context
# Load AGENTS.md → layer AGENT.md → division DIVISION.md into agent state
```

</details>

> **Full setup guide:** [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) — including agent bootstrap steps and minimal fleet configuration.

---

## Repository Structure

```
agentic-enterprise/
├── README.md                        ← You are here
├── AGENTS.md                        ← Global agent instruction hierarchy
├── CLAUDE.md                        ← Mirrors AGENTS.md (keep in sync)
├── COMPANY.md                       ← Vision, mission, strategic beliefs
├── CONFIG.yaml                      ← Central configuration (fill FIRST)
├── CUSTOMIZATION-GUIDE.md           ← Step-by-step onboarding (start here)
├── OPERATING-MODEL.md               ← How the whole system works
├── CODEOWNERS                       ← RACI — who approves what
├── CONTRIBUTING.md                  ← How to contribute
├── CHANGELOG.md                     ← Framework version history
├── locks.yaml                       ← Protected path definitions for lock enforcement
├── docs/                            ← Operator guides and reference documentation
│   ├── README.md                    ← docs/ index with template vs. company guide
│   ├── FILE-GUIDE.md                ← What each file is and what to do in a fork
│   ├── runtimes/                    ← Runtime-specific implementation guides
│   │   ├── README.md               ← Runtime guide index
│   │   └── openclaw.md             ← OpenClaw fleet setup guide
├── schemas/                         ← JSON schemas for CONFIG.yaml validation
├── scripts/                         ← Automation scripts (validation, checks)
│
├── org/                             ← ORGANIZATIONAL STRUCTURE
│   ├── 0-steering/                  ← Evolve the company itself
│   ├── 1-strategy/                  ← Define WHY + WHAT
│   │   └── ventures/                ← Market-facing venture charters
│   ├── 2-orchestration/             ← Translate strategy → work
│   │   └── fleet-configs/           ← Agent fleet configurations
│   ├── 3-execution/                 ← Do the work
│   │   └── divisions/               ← 15 specialized divisions
│   │       ├── ai-intelligence/
│   │       ├── core-applications/
│   │       ├── core-services/
│   │       ├── data-foundation/
│   │       ├── engineering-foundation/
│   │       ├── infrastructure-operations/
│   │       ├── quality-security-engineering/
│   │       ├── product-marketing/
│   │       ├── knowledge-enablement/
│   │       ├── customer-experience/
│   │       ├── finance-procurement/
│   │       ├── legal/
│   │       ├── people/
│   │       └── ... (+ domain placeholders)
│   ├── 4-quality/                   ← Evaluate against policies
│   │   └── policies/                ← 14 mandatory policy domains, including privacy, incident response, and availability
│   ├── agents/                      ← Agent Type Registry
│   └── integrations/                ← Integration Registry (3rd-party tools)
│       ├── categories/              ← Observability, toolchain, business, comms
│       └── _TEMPLATE-integration.md ← Template for new integrations
│
├── process/                         ← PROCESS DEFINITIONS
│   ├── 1-discover/                  ← Loop 1: Signal → Mission
│   ├── 2-build/                     ← Loop 2: Mission → Software
│   ├── 3-ship/                      ← Loop 3: Staging → GA
│   └── 4-operate/                   ← Loop 4: GA → Health (24/7)
│
├── work/                            ← ACTIVE WORK (GitOps PM)
│   ├── signals/                     ← Incoming opportunities/problems
│   ├── missions/                    ← Active missions with contracts
│   ├── decisions/                   ← Decision Records (DACI)
│   ├── releases/                    ← Release contracts
│   ├── assets/                      ← Non-code deliverable registry
│   ├── retrospectives/              ← Postmortems
│   └── locks/                       ← Concurrency locks for shared files
│
└── examples/                        ← Reference implementation examples
```

---

## Ecosystem & Integrations

This framework is **runtime-agnostic** and **integration-ready**. It defines the organizational structure, processes, and governance — you bring the agent runtime and connect your enterprise tools. The **Integration Registry** (`org/integrations/`) provides governed connection patterns for every category of external tool.

### Integration Registry

The operating model lives in the filesystem. But enterprises run on ecosystems. The Integration Registry makes external tool connections explicit, governed, and auditable:

| Category | What Connects | Registry Guide |
|----------|--------------|----------------|
| **Observability & Telemetry** | Agent fleet monitoring, governance visibility, anomaly detection, compliance auditing | `org/integrations/categories/observability.md` |
| **Enterprise Toolchain** | CI/CD pipelines, ITSM, security scanners, service catalogs, developer portals | `org/integrations/categories/enterprise-toolchain.md` |
| **Business Systems** | CRM, ERP, customer support, analytics, marketing automation | `org/integrations/categories/business-systems.md` |
| **Communication** | Chat (Slack/Teams), messaging, email, notifications, escalation | `org/integrations/categories/communication.md` |

**Connection patterns:** MCP Servers (agent-callable tools), Webhooks (inbound events), API Integration (outbound actions), OpenTelemetry (standardized telemetry).

All integrations are declared in `CONFIG.yaml → integrations` and governed through the same PR-based process as everything else.

### Observability for Agent Governance at Scale

As agent fleets grow, observability becomes the **second native communication channel** alongside the repo — agents emit OpenTelemetry spans and events as they act, the platform surfaces patterns, and automated signals flow back into `work/signals/` to feed the governance loop. It is not just monitoring — it is a bidirectional coordination layer: agents consume operational data from it *before* deciding, and emit telemetry to it *after* acting.

The framework supports any observability platform through OpenTelemetry and platform-native integration patterns:

| Approach | Tools | Best For |
|----------|-------|----------|
| **Open standard** | OpenTelemetry + Prometheus + Grafana | Vendor-neutral collection, proven at scale, free |
| **Full-stack AI-powered** | Dynatrace | Automatic topology, AI root cause analysis, end-to-end tracing |
| **Log-centric** | Elastic (ELK Stack) | Full-text search, security analytics, APM |
| **Hybrid** | OpenTelemetry collection + any backend | Maximum flexibility, open collection, differentiated analysis |

See `org/integrations/categories/observability.md` for detailed patterns.

### Agent Runtimes (Bring Your Own)

| Runtime | Stars | Best For | Integration Point |
|---------|-------|----------|-------------------|
| [OpenClaw](https://openclaw.ai) | — | Self-hosted AI gateway, multi-channel (WhatsApp/Telegram/Discord/iMessage), persistent memory, 50+ integrations | Skills + GitHub integration for Git-native workflow |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 19k+ | Production Python agents with tool use, handoffs, guardrails | Load AGENT.md hierarchy as agent instructions |
| [Microsoft AutoGen](https://github.com/microsoft/autogen) / [Agent Framework](https://github.com/microsoft/agents) | 54k+ / 7k+ | Multi-agent conversations, enterprise .NET/Python | Map 5-layer model to agent groups |
| [CrewAI](https://github.com/crewai-inc/crewAI) | 44k+ | Role-based agent crews with process orchestration | Natural fit: crews = missions, agents = division roles |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 24k+ | Stateful agent workflows with cycles and persistence | Model 4-loop lifecycle as graph states |

### Agent Protocols & Communication Paths

| Protocol / Channel | What It Does | How It Fits |
|----------|-------------|-------------|
| **Natural language in the repo** | Markdown and YAML files — `AGENT.md`, mission briefs, policies, signals — are the primary instruction and coordination medium between humans and agents | Asynchronous, versioned, diffable: agents read instructions, produce artifacts, and surface observations through structured natural language in Git |
| **Observability platform** | Event bus and telemetry backbone — agents emit OpenTelemetry spans and events; the platform detects patterns and feeds automated signals back into `work/signals/` | Real-time coordination layer: agents consume observability data *before* acting and emit telemetry *after* — closing the loop between execution and governance |
| [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol/specification) | Standardized tool/resource connection for agents | Connect agents to business systems (ITSM, Slack, DBs) beyond Git |
| [A2A (Agent2Agent)](https://github.com/google/A2A) | Cross-agent communication protocol (Google/Linux Foundation) | Enable cross-layer and cross-division agent collaboration |

### Governance & Platform Tools

| Tool | Purpose | Integration |
|------|---------|-------------|
| [Backstage](https://backstage.io) | Developer portal & service catalog | Division catalog, agent fleet dashboards |
| [OPA/Rego](https://www.openpolicyagent.org) | Policy-as-code enforcement | Enforce quality policies from `org/4-quality/policies/` |
| [Mergify](https://mergify.com) / [Prow](https://github.com/kubernetes-sigs/prow) | Automated PR management | Wire CODEOWNERS-based governance |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Agent output safety rails | Enforce agent instruction compliance |

---

## Known Limitations & Roadmap

> This is a proof-of-concept. The model is **structurally complete** but has deliberate simplifications. Each limitation links to a tracked issue with solution research.

| # | Limitation | Status | Discussion |
|---|-----------|--------|------------|
| 1 | **Mono-repo simplification** — Production would need multi-repo | [Issue #1](https://github.com/wlfghdr/agentic-enterprise/issues/1) | Backstage, Git submodules, Turborepo |
| 2 | **No agent runtime included** — Framework only, BYORT | [Issue #2](https://github.com/wlfghdr/agentic-enterprise/issues/2) | OpenClaw, OpenAI SDK, CrewAI, LangGraph |
| 3 | **Quality policies are now broad but still early-stage** — 14 domains exist, including privacy, incident response, and availability / continuity, but they still need domain-expert calibration, deployment-specific configuration, and runtime enforcement/evidence | [Issue #3](https://github.com/wlfghdr/agentic-enterprise/issues/3) | OWASP, CIS, NIST, OPA/Rego |
| 4 | **Governance not wired** — CODEOWNERS described, not enforced | [Issue #4](https://github.com/wlfghdr/agentic-enterprise/issues/4) | GitHub Branch Protection API, Mergify |
| 5 | **AGENT.md only — no skills/tools/MCP** | [Issue #5](https://github.com/wlfghdr/agentic-enterprise/issues/5) | MCP SDK, OpenClaw skills, A2A protocol |
| 6 | **PR-only interaction** — No chat/messaging interface | [Issue #6](https://github.com/wlfghdr/agentic-enterprise/issues/6) | OpenClaw gateway, Slack/Teams bots |
| 7 | **No dashboards or visualization** | [Issue #7](https://github.com/wlfghdr/agentic-enterprise/issues/7) | Backstage plugins, Grafana, GitHub Projects |
| 8 | **No cross-repo orchestration** | [Issue #8](https://github.com/wlfghdr/agentic-enterprise/issues/8) | repository_dispatch, ArgoCD, Flux, Nx |
| 9 | **Agent instructions not enforced** — Trust-based compliance | [Issue #9](https://github.com/wlfghdr/agentic-enterprise/issues/9) | MCP enforcement, NeMo Guardrails |
| 10 | **Integration Registry is templated, not wired** — Patterns defined, connections not live | [Issue #10](https://github.com/wlfghdr/agentic-enterprise/issues/10) | MCP servers, A2A, OpenTelemetry, vendor SDKs |

See [GitHub Discussions](https://github.com/wlfghdr/agentic-enterprise/discussions) for community conversation on each topic.

---

## Enterprise Trust & Audit Readiness

This repository now includes meaningful trust surfaces — not just placeholder policy names. In particular, the framework has explicit operating guidance for:

- **Privacy** — lawful basis, DPA / DPIA touchpoints, DSAR handling, breach response, and transfer controls
- **Incident response** — severity levels, response targets, escalation rules, and post-incident learning loops
- **Availability & continuity** — service tiers, RTO / RPO expectations, failover / recovery runbooks, and drill expectations
- **Observability & evidence** — telemetry, dashboards, traces, events, and audit artifacts that help prove what actually happened

That is the right framing for this repository: **it makes a team more audit-ready by giving them governance structure, policy surfaces, and evidence patterns**. It does **not** make a deployment compliant by itself. Certification, legal compliance, and control effectiveness still depend on the runtime you operate, the integrations you configure, the records you keep, and the evidence you can produce in the real environment.

If you want the short version:

- this repo is **strong on operating model and policy scaffolding**
- it is **honest about bring-your-own runtime and deployment controls**
- it is **designed to help teams move faster toward enterprise readiness without pretending the repo alone is the audit**

See the tracked roadmap items and discussions in GitHub Issues / Discussions for deployment-specific gaps, enforcement work, and certification-oriented follow-up.

---

## Who Is This For?

- **CTOs / VPs Engineering** — Exploring what an AI-native operating model looks like
- **Platform Engineers** — Building the governance layer for agent fleets
- **AI/ML Engineers** — Structuring multi-agent systems with clear boundaries
- **Consultants** — Need a reference architecture for agentic transformation
- **Open Source Contributors** — Want to help define the future of AI-native organizations

---

## Contributing

We welcome contributions! This is an early-stage project and there's a lot to build.

- **Framework improvements:** Better templates, policies, agent instructions
- **Runtime integrations:** Connect this framework to agent runtimes (OpenClaw, OpenAI SDK, CrewAI, etc.)
- **Tooling:** Build validators, dashboards, CLI tools
- **Documentation:** Tutorials, guides, case studies

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Related Projects

| Project | Relationship |
|---------|-------------|
| [OpenClaw](https://openclaw.ai) | Self-hosted AI gateway — operationalizes agents beyond Git with multi-channel support, persistent memory, and 50+ integrations |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Production agent runtime — use AGENT.md hierarchy as agent instructions |
| [Microsoft AutoGen](https://github.com/microsoft/autogen) | Multi-agent framework — map organizational layers to agent groups |
| [CrewAI](https://github.com/crewai-inc/crewAI) | Role-based agent crews — natural fit for mission-based execution |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful workflows — model process loops as graph states |
| [MCP Specification](https://github.com/modelcontextprotocol/specification) | Agent protocol — extend beyond Git to business systems |
| [Google A2A](https://github.com/google/A2A) | Agent-to-agent protocol — enable cross-layer communication |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Agent safety — enforce instruction compliance |

---

## License

[Apache License 2.0](LICENSE) — Enterprise-friendly. Use it, fork it, build on it. Patent protection included.

---

<p align="center">
  <strong>The future of enterprise is not more meetings.<br>It's a Git repository that runs itself.</strong>
</p>

<p align="center">
  <a href="https://github.com/wlfghdr/agentic-enterprise">⭐ Star this repo</a> •
  <a href="https://github.com/wlfghdr/agentic-enterprise/fork">🍴 Fork it</a> •
  <a href="https://github.com/wlfghdr/agentic-enterprise/discussions">💬 Join the discussion</a>
</p>
