# Operating Model: The Agentic Enterprise GitOps Model

> **What this document is:** The meta-description of how this entire system works — the replacement of legacy ticket-based, ceremony-driven, phase-gated product development with a Git-native, agent-driven, outcome-governed operating model.  
> **Audience:** Humans and agents who need to understand the big picture.

> **⚠️ POC / Demo Disclaimer**  
> This is a proof-of-concept demonstrating the *structure and shape* of an agentic enterprise operating model. Key simplifications:
> - **Mono-repo:** Production would use multiple repositories (operating model, per-product code, GTM content, customer playbooks, etc.) with cross-repo orchestration.
> - **Policies are stubs:** Quality policies need extensive real-world calibration — false positive rates, threshold tuning, domain-specific edge cases, legal and compliance review.
> - **Agent runtime not included:** The repo defines *what* agents do and *how* work flows, but does not include the actual LLM orchestration, tool bindings, or agent runtime that would execute this in production.
> - **AGENT.md files only:** Agents exist here solely as instruction files. In production, agents would be full implementations with **skills** (composable expertise), connected to business systems via **MCP servers, APIs, and tool integrations**.
> - **PR-centric interaction:** All decisions flow through Git PRs in this POC. In production, most humans would interact via **chat/messaging**, **purpose-built dashboards and web UIs**, or **within their existing tools** — with Git as the system of record underneath.
> - **Governance is described, not wired:** CODEOWNERS, branch protection, CI/CD checks are documented as the target state but not implemented as live infrastructure.
> - **Integrations are templated, not connected:** The Integration Registry (`org/integrations/`) defines *how* external tools connect, but does not include live MCP servers, webhooks, or API clients. Production would wire these to your actual observability platform, ITSM, CI/CD, and business systems.

---

## The Pitch

A fully working operating model for running {{COMPANY_SHORT}} as an agentic enterprise. Not a strategy deck — a **live Git repo** with org structure, process, agent instructions, quality policies, and active work artifacts. Everything versioned, auditable, executable.

- **5 layers** — Steering → Strategy → Orchestration → Execution → Quality — covering the entire company (eng, delivery, GTM, sales, CS, support), not just R&D
- **4 loops** — Discover → Build → Ship → Operate — replacing legacy phase-gate processes. Idea-to-GA in 2–4 weeks. Continuous production operations feed signals back into Discover.
- **Git is the system of record** — PRs = decisions. CODEOWNERS = RACI. CI/CD = quality gates. Agents are native Git citizens. Enterprise tools connect through governed integrations.
- **Integration-ready** — Observability platforms, ITSM, CI/CD, business systems, and communication channels plug in through a governed Integration Registry (`org/integrations/`). The model works with your existing tools, not against them.
- **Self-evolving** — Every agent surfaces improvement signals → Steering Layer aggregates → proposes org/process changes as PRs → execs approve by merging. Continuous organizational metabolism, not annual reorgs

---

## The Core Idea

**The operating model lives in the filesystem — versioned, auditable, executable. Git is the system of record. The enterprise ecosystem of tools, platforms, and observability extends its reach.**

This is not an incremental improvement over legacy processes. It is a structural reinvention based on four observations:

1. **AI agents are native Git citizens.** They create branches, write files, submit PRs, respond to reviews. Git is their natural medium for governance — the canonical source of truth for structure, process, policy, and decisions.

2. **Git provides the governance backbone.** Branching = workflow states. PRs = decisions and approvals. CODEOWNERS = RACI. CI/CD = quality gates. History = audit trail. All of this is built-in, version-controlled, and free.

3. **The bottleneck in agentic enterprise work is not execution — it's governance.** When agent fleets can write code 100x faster than humans, the question is not "how do we produce more code?" but "how do we ensure quality, alignment, and trust at scale?" Git's PR-based governance is the foundation — but scaling it requires observability, enterprise tool integration, and real-time telemetry.

4. **Enterprises run on ecosystems, not single tools.** Real organizations use CI/CD pipelines, ITSM platforms, observability tools, CRMs, and communication channels. The operating model connects to all of them through a governed integration registry — keeping Git as the system of record while agents operate across the full enterprise toolscape.

---

## Two Halves of the Model

### Organizational Structure → `org/`

The **static structure** of the organization: who exists, where they sit, what they own, how they relate to each other. This covers the **entire company** — engineering, delivery, go-to-market, sales, customer success, and support — not just R&D.

In this model, it's a **5-layer architecture**:

| Layer | Purpose | Human Density | Agent Density |
|-------|---------|--------------|---------------|
| **Steering** | Evolve the company itself — structure, model, portfolio | Very High (C-Suite) | Medium (evolution agents) |
| **Strategy** | Define WHY + WHAT + CONSTRAINTS | High | Low (support agents) |
| **Orchestration** | Translate strategy → executable work | Medium | Medium (coordination agents) |
| **Execution** | Do the work across all functions | Mixed (varies by division) | High (agent fleets) |
| **Quality** | Evaluate outputs against policies | Low (policy authors) | High (eval agents) |

Each layer has:
- A folder in `org/<layer>/`
- An `AGENT.md` with layer-specific agent instructions
- Artifacts that layer owns
- A **continuous improvement responsibility**: every agent in every layer surfaces improvement signals to `work/signals/`

Loops 1–3 are **mission-driven** (time-bounded, goal-oriented). Loop 4 is **continuous** — it runs 24/7, keeping shipped software healthy with operations agents, remediation agents, feature flag agents, incident response agents, and capacity agents. Loop 4 generates the production signals that feed back into Loop 1 (Discover), making the entire model circular.

### Process Organization → `process/`

The **dynamic processes** of the organization: how work flows, what steps are followed, what handoffs happen.

In this model, it's a **4-loop lifecycle**:

| Loop | Purpose | Duration | Human Touchpoints |
|------|---------|----------|-------------------|
| **Discover & Decide** | Signal → Mission Brief | Hours-Days | 1 (Go/No-Go) |
| **Design & Build** | Mission → Working Software | Days-Weeks | By exception only |
| **Validate & Ship** | Staging → GA | Days | 1 (Go/No-Go) |
| **Operate & Evolve** | GA → Continuous production health, remediation, signals | Continuous (24/7) | By escalation only |

### Templates (co-located with artifacts)

Reusable templates that standardize how work is created and tracked. Templates are co-located with their artifacts as `_TEMPLATE-*` files:

| Category | Templates | Location |
|----------|-----------|----------|
| **Discover** | `_TEMPLATE-signal.md`, `_TEMPLATE-signal-digest.md`, `_TEMPLATE-mission-brief.md` | `work/signals/`, `work/signals/digests/`, `work/missions/` |
| **Build** | `_TEMPLATE-outcome-contract.md`, `_TEMPLATE-technical-design.md`, `_TEMPLATE-decision-record.md`, `_TEMPLATE-mission-status.md`, `_TEMPLATE-quality-evaluation-report.md`, `_TEMPLATE-component-onboarding.md` | `work/missions/`, `work/decisions/`, `org/3-execution/divisions/_TEMPLATE/` |
| **Ship** | `_TEMPLATE-release-contract.md`, `_TEMPLATE-outcome-report.md`, `_TEMPLATE-asset-registry-entry.md` | `work/releases/`, `work/missions/`, `work/assets/` |
| **Operate** | `_TEMPLATE-runbook.md`, `_TEMPLATE-postmortem.md` | `org/3-execution/divisions/_TEMPLATE/`, `work/retrospectives/` |
| **Strategy** | `_TEMPLATE-venture-health-report.md`, `_TEMPLATE-fleet-performance-report.md` | `org/1-strategy/ventures/`, `work/missions/` |
| **Evolution** | `_TEMPLATE-evolution-proposal.md`, `_TEMPLATE-agent-type-proposal.md` | `org/0-steering/`, `org/agents/` |

### Key Terminology: Fleets and Crews

| Term | Definition |
|------|-----------|
| **Division** | A persistent group of agents organized by expertise — the agentic equivalent of a department (e.g., Core API, Frontend, Documentation). Divisions own skills, standards, and institutional knowledge. |
| **Fleet** | The full pool of agents available to the Orchestration Layer. A fleet is the total capacity — all agents across all divisions that can be assigned to work. |
| **Crew** | A subset of agents drawn from the fleet and assigned to a specific mission. A crew is assembled when a mission starts and disbanded when it ends. One agent can serve on multiple crews. |

**How they relate:** Divisions define *what agents know*. The fleet is *who is available*. A crew is *who is working on this mission right now*. The Orchestration Layer assembles crews from the fleet based on the divisions a mission requires.

---

## How the Model Relates to Existing Tools

The agentic enterprise model does not require replacing every tool in your organization. It introduces a **governance backbone** (Git-based) and a **governed integration layer** that connects to existing enterprise systems. Here's how concepts map:

| Traditional Concept | Agentic Enterprise Equivalent | Relationship |
|---------------|----------------------|-----------------|
| **Ticket (Jira/Linear)** | Markdown file in `work/` | System of record moves to Git; existing tools can sync via Integration Registry |
| **Ticket workflow** | Git branch → PR → merge | Governance is Git-native; status can be projected to existing tools |
| **Board/Kanban** | Auto-generated dashboards from `work/` | Visualization is decoupled from data — use existing dashboards or build new ones |
| **Sprint planning** | Mission brief creation | Goal-oriented, not time-boxed |
| **Sprint review** | PR review with embedded evidence | Continuous, not biweekly |
| **Daily standup** | Git log + fleet observability dashboards | Always current, no meetings; observability provides real-time fleet health |
| **Story points** | Fleet throughput metrics (from observability) | Measured from telemetry, not estimated |
| **Wiki** | This repository | Single source of truth, version-controlled |
| **Chat discussions** | PR comments + chat integration | Auditable via Git; chat is the human interaction surface |
| **RACI matrix** | CODEOWNERS file | Executable, enforced by the Git host |
| **Phase gates** | CI/CD pipeline checks | Automated, consistent, no human bottleneck |
| **Status meeting** | `git diff` + mission status + observability | Self-updating, always accurate |
| **Monitoring/alerting** | Observability integration (org/integrations/) | Production telemetry feeds signals back into governance |
| **Retrospective** | Policy evolution PRs + improvement signals | Continuous improvement, not periodic |
| **Role descriptions** | Agent instruction files | Executable, testable, versionable |
| **Executive strategy offsite** | Steering Layer evolution process | Continuous, evidence-based, agent-assisted |
| **Org restructuring** | Evolution proposals via PR | Transparent, reversible, grounded in signals |

---

## The Collaboration Pattern

```
                    Executives evolve the system
                         │
                         ▼
              ┌─────────────────────┐
              │   STEERING LAYER    │  Agents analyze the company itself
              │ (org/0-steering/)   │  Executives approve evolution
              └──────────┬──────────┘
                         │ Evolution PRs (structure, model, portfolio)
                         ▼
              ┌─────────────────────┐
              │   STRATEGY LAYER    │  Humans define missions
              │  (org/1-strategy/)  │  Agents discover & recommend
              └──────────┬──────────┘
                         │ Mission Brief (PR)
                         ▼
              ┌─────────────────────┐
              │  ORCHESTRATION      │  Humans configure fleets
              │(org/2-orchestration)│  Agents decompose & coordinate
              └──────────┬──────────┘
                         │ Fleet Config (YAML)
                         ▼
              ┌─────────────────────┐
              │   EXECUTION LAYER   │  Agents build, write, prepare, support
              │ (org/3-execution/)  │  Humans own decisions & relationships
              └──────────┬──────────┘
                         │ Code PRs / Content / Materials / Responses
                         ▼
              ┌─────────────────────┐
              │   QUALITY LAYER     │  Agents evaluate against policies
              │  (org/4-quality/)   │  Humans author & evolve policies
              └──────────┬──────────┘
                         │ Evaluation verdicts
                         ▼
                    Merge or iterate
                         │
                         │ ┌──────────────────────────────────┐
                         └→│  IMPROVEMENT SIGNALS flow UP     │
                           │  from ALL layers to Steering     │
                           │  → The company evolves itself    │
                           └──────────────────────────────────┘
```

Every arrow in this diagram is a **Git operation** (commit, branch, PR, merge, review comment) — the system of record. In practice, agents also interact with enterprise tools (observability platforms, ITSM, CI/CD, communication channels) through governed integrations. Git remains the canonical record; external tools extend the operating model's reach.

---

## Artifact Flow: The Complete Chain

Every handoff between layers and loops is mediated by a concrete artifact stored in the repository. No implicit handoffs.

```
Signal (work/signals/)
  │
  ├─ Steering: Signal Digest (work/signals/digests/)
  │
  ▼
Mission Brief (work/missions/<name>/BRIEF.md)
  + Outcome Contract (work/missions/<name>/OUTCOME-CONTRACT.md)
  │
  ├─ Orchestration: Fleet Config (org/2-orchestration/fleet-configs/<mission>.md)
  │                  Mission Status (work/missions/<name>/STATUS.md)
  │                  Fleet Performance Report
  │
  ├─ Technical Design (work/missions/<name>/TECHNICAL-DESIGN.md)
  │  (for design-required missions: API contracts, data models,
  │   interface specs, behavioral specs, threat model, perf budgets)
  │
  ▼
Execution Outputs (code PRs, docs, content, assets)
  + Asset Registry (work/assets/<asset>.md)
  + Runbooks (per service)
  │
  ├─ Quality: Evaluation Reports (work/missions/<name>/evaluations/)
  │
  ▼
Release Contract (work/releases/YYYY-MM-DD-<release>.md)
  │
  ▼
Production (deployed)
  │
  ├─ Outcome Report (work/missions/<name>/OUTCOME-REPORT.md)
  ├─ Venture Health Report (Strategy → Steering)
  ├─ Postmortem (work/retrospectives/) — if incident
  │
  ▼
New Signals (work/signals/) ← completes the loop
```

---

## Agent Lifecycle Governance

Agent types are governed as first-class organizational assets in the **Agent Type Registry** (`org/agents/`).

| Concept | Location | Owner |
|---------|----------|-------|
| **Agent type definition** | `org/agents/<layer>/<type-id>.md` | Steering Layer (CTO approval) |
| **Agent type proposal** | PR using `org/agents/_TEMPLATE-agent-type-proposal.md` | Any layer can propose |
| **Agent type lifecycle** | `proposed → active → deprecated → retired` | Steering Layer governs transitions |
| **Agent instances** | Fleet configs referencing active types | Orchestration Layer provisions |

**Key separation:** The registry defines *what agent types exist* (their capabilities, boundaries, and quality gates). Fleet configs determine *how many instances run* and *on which missions*. Execution divisions *use* agents within their defined capabilities.

See [org/agents/README.md](org/agents/README.md) for the full lifecycle documentation.

---

## Human Interaction Model

### Layer 1: Git + PR Interface (The Foundation)

Every human interaction ultimately maps to a Git operation. But the *surface* varies by role:

| Interaction Surface | Who Uses It | What They Do |
|---|---|---|
| **{{GIT_HOST}} Web UI** | Everyone | Review PRs, approve merges, browse structure |
| **IDE (VS Code + Copilot)** | Tech Leads, Policy Authors | Edit policies, review code, write decision records |
| **Git CLI** | Agent Fleet Managers, advanced users | Scripted operations, bulk changes |
| **Chat / Messaging Interface** | Outcome Owners, Executives, all layers | Natural-language commands → agent actions → PRs |
| **Dashboard / Web App** | Executives, Mission Leads, Fleet Managers | Real-time mission status, fleet health, quality metrics |
| **Mobile notifications** | Outcome Owners, on-call | Approve/reject decisions, escalation alerts |

### Layer 2: Chat & Messaging (The Primary Human-Agent Channel)

In practice, **most human-agent interaction happens through chat/messaging interfaces** — not through raw Git commands:

```
Human (in chat):  "What's the status of the authentication mission?"
Agent:            "Mission AUTH-UPGRADE is in Loop 2 (Build). 3 of 5 streams 
                   complete. Blocked on: security policy review for OAuth provider 
                   trust. PR #247 awaits your approval."
Human:            "Approve it. And start the enablement stream."
Agent:            [merges PR #247, creates enablement branch, notifies 
                   Knowledge & Enablement division lead]
                  "Done. PR #247 merged. Enablement stream initiated."
```

**Key design principle:** Every chat action that changes state produces a Git commit. Chat is the *input surface*, Git is the *state machine*. Conversations are ephemeral; Git is permanent.

### Layer 3: Web UIs & Dashboards (The Visual Layer)

| UI | Purpose | Data Source |
|---|---|---|
| **Mission Control Dashboard** | Kanban-style view of all active missions | `work/missions/` + Git activity |
| **Signal Triage Board** | Incoming signals ranked by urgency/impact | `work/signals/` + agent analysis |
| **Fleet Performance Dashboard** | Agent throughput, error rates, cost per task | {{OBSERVABILITY_TOOL}} metrics |
| **Quality Scorecard** | Per-division quality grades, compliance rates | `org/4-quality/` evaluation results |
| **Org Health Visualizer** | Interactive 5-layer org chart | `org/` folder structure |
| **PR Review Queue** | Prioritized list of PRs needing human attention | {{GIT_HOST}} API |

### Layer 4: Human Escalation Patterns

```
┌─ ROUTINE ──────────────────────────────────────────────────────────┐
│  Agent completes work → submits PR → human reviews at leisure     │
└───────────────────────────────────────────────────────────────────┘
┌─ ATTENTION NEEDED ─────────────────────────────────────────────────┐
│  Agent encounters ambiguity or policy conflict → flags in PR      │
└───────────────────────────────────────────────────────────────────┘
┌─ DECISION REQUIRED ────────────────────────────────────────────────┐
│  Agent needs Go/No-Go or strategic choice → blocks and waits      │
└───────────────────────────────────────────────────────────────────┘
┌─ ESCALATION ───────────────────────────────────────────────────────┐
│  Agent detects policy violation, security risk, or blocked path   │
└───────────────────────────────────────────────────────────────────┘
```

---

## Multi-Agent Concurrency & Git Coordination

### The Concurrency Model

```
                    ┌─────────────────────────────────┐
                    │         main branch              │
                    │    (protected, merge-only)        │
                    └───────┬───────┬───────┬──────────┘
                            │       │       │
                    ┌───────┴──┐ ┌──┴───────┐ ┌──┴──────┐
                    │ Agent A  │ │ Agent B  │ │ Agent C │
                    │ branch:  │ │ branch:  │ │ branch: │
                    │ build/   │ │ build/   │ │ signal/ │
                    │ auth/api │ │ auth/docs│ │ new-sig │
                    └──────────┘ └──────────┘ └─────────┘
```

### Rule 1: One Branch Per Agent Per Task
Every agent creates a dedicated branch. No two agents commit to the same branch simultaneously.

### Rule 2: File Ownership via Folder Structure
The folder structure minimizes file contention — different agents work in different folders.

### Rule 3: Git-Native Conflict Resolution
When agents touch the same files, Git's standard merge conflict resolution applies. On conflict, agents attempt automatic resolution or escalate to humans.

### Rule 4: Pessimistic Locking for Critical Shared Files
Certain files (COMPANY.md, OPERATING-MODEL.md, quality policies) should not be concurrently modified. Use lock files or branch protection.

### Rule 5: Workstream Isolation for Missions
The Orchestration Layer pre-assigns file ownership via fleet configs with `exclusive: true` paths.

### Rule 6: Conflict Prevention > Conflict Resolution
1. **Additive-only patterns:** Signals, missions, decisions are new files
2. **Folder-per-entity:** Each mission gets its own folder
3. **Status files are append-only**
4. **Index files are auto-generated**
5. **PR serialization on main**

---

## Integration & Observability: Scaling Governance Beyond Git

The operating model's definitions, decisions, and governance live in the filesystem — versioned in Git. But as agent fleets scale, two additional capabilities become essential:

### The Integration Registry → `org/integrations/`

Enterprises operate with rich ecosystems of tools. The **Integration Registry** provides a governed catalog of external connections:

| Category | What Connects | Examples |
|----------|--------------|----------|
| **Observability & Telemetry** | Agent fleet monitoring, governance visibility, anomaly detection | Dynatrace, Prometheus + Grafana, OpenTelemetry, Elastic |
| **Enterprise Toolchain** | CI/CD, ITSM, security scanning, service catalogs | GitHub Actions, ServiceNow, Snyk, Backstage |
| **Business Systems** | CRM, ERP, support, analytics | Salesforce, Zendesk, Mixpanel |
| **Communication** | Human-agent interaction surfaces | Slack, Teams, PagerDuty |

Each integration is registered in `CONFIG.yaml` and governed through the same PR-based process as everything else. No shadow integrations, no untracked data flows.

Connection patterns:
- **MCP Servers** — Agents call external tools via Model Context Protocol
- **Webhooks** — External events flow into the operating model as signals
- **API Integration** — Agents take actions in external systems
- **OpenTelemetry** — Standardized telemetry collection across agent activity

### Observability for Agent Governance at Scale

When agent fleets grow from a handful to hundreds, the file-based governance model needs a complementary layer for **real-time visibility, anomaly detection, and causal analysis**. The operating model defines *what should happen*. Observability reveals *what actually happens* — at a speed and scale that no human reviewing PRs can match.

**What to observe:**

| Telemetry | What It Captures | Governance Value |
|-----------|-----------------|------------------|
| **Traces** | End-to-end mission flow through layers and agents | Bottleneck analysis, latency attribution |
| **Metrics** | Agent throughput, error rates, cost per task | Fleet performance, capacity planning |
| **Logs** | Agent reasoning, decisions, tool calls | Audit trail, compliance evidence |
| **Events** | State transitions (PR created, merged, rejected) | Pattern detection, automated signal generation |

**How observability fits:**

```
Agent Activity → OpenTelemetry SDK → Telemetry Pipeline → Observability Platform
                                                                    │
                                              ┌─────────────────────┤
                                              │                     │
                                        Dashboards           AI Analysis
                                        & Alerts           & Anomaly Detection
                                              │                     │
                                              └──────────┬──────────┘
                                                         │
                                                    Automated Signals
                                                    → work/signals/
                                                         │
                                                    The governance loop
                                                    continues in Git
```

Observability platforms — whether open-source (Prometheus, Grafana, OpenTelemetry Collector) or commercial (Dynatrace, Datadog, Elastic) — become the **scaling layer** for governance. They process the telemetry that agents generate, surface patterns invisible to file-based inspection, and feed automated signals back into the operating model.

This is particularly critical for:
- **Fleet performance monitoring** — Are agents meeting throughput and quality targets?
- **Compliance auditing** — Continuous policy adherence, not just PR-time checks
- **Incident response** — Production anomalies detected and correlated in real-time
- **Cost governance** — Token usage, API costs, and compute spend tracked per mission

See `org/integrations/categories/observability.md` for detailed integration patterns.

---

## Design Principles

> Derived from empirical data across agentic enterprise deployments. These principles inform all architectural and operational decisions.

### 1. Specialization Over Generalization
Purpose-built agents outperform general-purpose ones by 3–5× on relevant metrics. Each agent should have a single, well-defined responsibility with clear inputs and outputs. The agent registry (`org/agents/`) enforces this by requiring explicit capability definitions.

### 2. Human-in-the-Loop Is a Feature, Not a Limitation
The highest-performing agentic systems maintain strategic human checkpoints. Humans handle judgment calls, ethical decisions, and novel situations. Agents handle volume, speed, and consistency. Every mission brief defines explicit human checkpoints.

### 3. Metrics-Driven Everything
Every agent, mission, and division must define measurable outcomes. Outcome contracts are not aspirational — they are the accountability mechanism. If you can't measure it, you can't manage it. Blueprint reference metrics provide baselines for what's achievable.

### 4. Layered Architecture Enables Scale
The 5-layer model (Steering → Strategy → Orchestration → Execution → Quality) creates clear separation of concerns. Each layer has distinct decision rights and feedback loops. This prevents the "agent soup" problem where responsibilities blur and accountability disappears.

### 5. Continuous Evolution Is Built In
The operating model evolves through the same mechanisms it uses for product work: signals surface observations, the steering layer evaluates patterns, and evolution proposals go through PR review. The company that observes itself through every agent improves exponentially faster than one relying on periodic top-down reviews.

---

## Getting Started

### For Humans
1. Read [CONFIG.yaml](CONFIG.yaml) — fill in your company configuration first
2. Read [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) — understand what to customize
3. Read [COMPANY.md](COMPANY.md) — understand the mission and beliefs
4. Read [org/README.md](org/README.md) — understand the 5-layer organizational structure
5. Read [process/README.md](process/README.md) — understand how work flows
6. Find your layer's GUIDE.md — understand your specific role
7. Look at [work/](work/) — see what's active

### For Agents
1. Read [AGENTS.md](AGENTS.md) — the non-negotiable rules
2. Read your layer's AGENT.md — your specific instructions
3. Read relevant quality policies — your guardrails
4. Read your task context (mission brief, fleet config, division charter)
5. If you are running this via OpenClaw, align your fleet config with [`docs/OPENCLAW-SETUP.md`](docs/OPENCLAW-SETUP.md)
6. Start working — submit PRs for review
7. Surface improvement signals — file signals in `work/signals/`

### For the Execution Example (Next Step)
The `examples/` folder contains worked-through examples of specific features going through the entire lifecycle — from signal to shipped feature — demonstrating how all the pieces fit together.
