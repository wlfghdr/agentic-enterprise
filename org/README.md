# Organizational Structure

> **What this is:** The static structure of the agentic enterprise {{COMPANY_SHORT}} organization — who exists, where they sit, what they own, how they relate. This covers the **entire company**, not just R&D: engineering, delivery, go-to-market, sales, customer success, and support all operate within the same 5-layer model.  
> **What it replaces:** Legacy role hierarchies, ticket-based coordination, manual phase gates, and siloed functional departments.  
> **Governance:** Changes via Pull Request → Steering Layer (structural) or Strategy Layer (operational) approval

---

## The 5-Layer Model

The organization is structured in five layers. Each layer has a distinct purpose, a distinct mix of humans and agents, and distinct agent instructions. **The same 5-layer pattern applies across all company functions** — because the principle is universal: executives steer the system, humans set direction, agents and humans orchestrate, agents and humans execute, agents and humans evaluate.

The critical addition — Layer 0: Steering — embeds what was historically invisible C-level work directly into the operating model. The company doesn't just operate through this system; it **evolves itself** through this system.

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   STEERING LAYER        Executives + Agents evolve the company      │
│   org/0-steering/       ~{{STEERING_SIZE}} people (C-Suite + Org Architects)  │
│                         CEO, CTO, CPO, CFO, COO/CRO, CHRO,         │
│                         Organization Architects, Board Advisors     │
│                         Agents: evolution, portfolio, model health   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   STRATEGY LAYER        Humans define WHY + WHAT + CONSTRAINTS      │
│   org/1-strategy/       ~{{STRATEGY_SIZE}} people                   │
│                         Venture Leads, Outcome Owners,             │
│                         GTM Strategists, Sales Strategists,         │
│                         Customer Strategists                        │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ORCHESTRATION LAYER   Humans + Agents translate strategy → work   │
│   org/2-orchestration/  ~{{ORCHESTRATION_SIZE}} people              │
│                         Mission Leads, Agent Fleet Managers,        │
│                         Release Coordinators, Campaign Leads        │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   EXECUTION LAYER       Agents do the work, humans own hard parts   │
│   org/3-execution/      ~{{EXECUTION_SIZE}} people + agent fleets   │
│                         Tech Leads, Sales Engineers,                │
│                         Content Producers, CSMs, Support Engineers  │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   QUALITY LAYER         Agents evaluate, humans author policies     │
│   org/4-quality/        ~{{QUALITY_SIZE}} people + eval agent fleets│
│                         Policy Authors across all domains           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Key principle:** Information and artifacts flow DOWN (steering → strategy → missions → work → evaluation). Insights and improvement signals flow UP (quality metrics → fleet performance → mission outcomes → strategic decisions → evolution proposals). **The company is its own first customer: it observes itself and uses that intelligence to continuously evolve.**

---

## Layer Details

### Steering Layer → [0-steering/](0-steering/)

**Purpose:** Evolve the company itself — its organizational structure, operating model, venture portfolio, division map, processes, and strategic direction.

**Humans:** CEO, CTO, CPO, CFO, COO/CRO, CHRO, Organization Architects, Board Advisors

**Agent support:** Company evolution agents, portfolio agents, operating model agents, investment modeling agents, transformation health agents, competitive intelligence agents.

**Key distinction from Strategy Layer:** Strategy works *within* the current structure. Steering *reshapes* the structure.

### Strategy Layer → [1-strategy/](1-strategy/)

**Purpose:** Define the WHY and WHAT across the entire company. Set missions, constraints, and outcome criteria.

**Humans:** Venture Leads, Outcome Owners, Experience Directors, Architecture Governors, Growth Analysts, Market Strategists, GTM Campaign Strategists, Sales Strategy Leads, Customer Strategy Leads

**Agent support:** Discovery agents, GTM agents, analytics agents, sales intelligence agents, customer health agents.

### Orchestration Layer → [2-orchestration/](2-orchestration/)

**Purpose:** Translate strategy into executable agent fleet configurations. Monitor fleet performance. Escalate exceptions.

**Humans:** Mission Leads, Agent Fleet Managers, Cross-Mission Coordinators, Release Coordinators, Campaign Orchestrators, Deal Desk Leads, Customer Journey Coordinators

**Agent support:** Coordination agents, fleet monitoring agents, release orchestration agents, campaign scheduling agents, deal support agents.

### Execution Layer → [3-execution/](3-execution/)

**Purpose:** Do the work. Agent fleets handle 80%+ of implementation across all disciplines. Humans own architecture decisions, critical path resolution, key customer relationships, and novel problem solving.

**Humans:** Tech Leads / System Architects, Release Engineers, Senior Technical Writers, Product Marketing Managers, Sales Engineers, Customer Success Managers, Support Engineers

**Agent support:** Implementation agent swarms, release automation agents, content generation agents, GTM agents, sales agents, CS agents, support agents.

### Quality Layer → [4-quality/](4-quality/)

**Purpose:** Evaluate all outputs against defined policies. Enforce quality gates automatically. Escalate anomalies. Author and evolve policies.

**Humans:** Security Policy Authors, Reliability Policy Authors, Performance Engineers, UX Standards Authors, Content Quality Authors, SLA Policy Authors

**Agent support:** Security eval agents, architecture eval agents, UX eval agents, performance eval agents, delivery readiness eval agents, content quality eval agents, customer interaction quality eval agents.

---

## Divisions: The Full Company

Divisions are the **execution units** of the organization — each owns a domain of work, has a team of humans + agents, and produces artifacts. Each division groups agents by expert knowledge, specialized tools, and domain-specific goals.

### Engineering Divisions — Core

| Division | What It Owns |
|-----------|-------------|
| **Data Foundation** | Core data storage, query engine ({{QUERY_LANGUAGE}}), data governance, enrichment, semantic normalization |
| **Core Services** | IAM, RBAC, tokens, lifecycle management, serverless runtime, APIs |
| **Core Applications** | Dashboards, notebooks, search, navigation, {{ASSISTANT_NAME}} UI |
| **AI & Intelligence** | {{AI_INTELLIGENCE_NAME}}, {{ASSISTANT_NAME}} backend, agent reasoning, NL↔{{QUERY_LANGUAGE}}, AI safety |

### Engineering Divisions — Domain

> **Customize this section.** Add divisions specific to your product domain. Examples:

| Division | What It Owns |
|-----------|-------------|
| **{{DOMAIN_CAP_1_NAME}}** | {{DOMAIN_CAP_1_DESCRIPTION}} |
| **{{DOMAIN_CAP_2_NAME}}** | {{DOMAIN_CAP_2_DESCRIPTION}} |

### Engineering Divisions — Operational Excellence

| Division | What It Owns |
|-----------|-------------|
| **Engineering Foundation** | Golden paths, developer portal, build infra, CI/CD, release engineering, feature flags, deployment pipelines |
| **Infrastructure Operations** | Cloud accounts, IaC, cost management, K8s runtime, networking, SLOs, incident management, on-call |
| **Quality & Security Engineering** | Security testing, privacy, compliance, quality gates, supply chain |

### Go-to-Market Divisions

| Division | What It Owns |
|-----------|-------------|
| **Product Marketing** | GTM strategy execution, launch orchestration, press releases, analyst relations, competitive positioning |
| **Knowledge & Enablement** | Product docs, API docs, tutorials, release notes, knowledge base, demos, battlecards, training, certifications |

### Customer Divisions

| Division | What It Owns |
|-----------|-------------|
| **Customer Experience** | Onboarding, adoption tracking, health scores, QBRs, renewal management, support, incident resolution, knowledge base, SLA management |

---

## How Legacy Roles Map to the Agentic Enterprise Model

| Legacy Role | New Role | Layer | Key Shift |
|------------|---------|-------|-----------|
| CEO | CEO (explicit in model) | Steering | From implicit direction-setting to agent-assisted company evolution |
| CTO | CTO (explicit in model) | Steering | From implicit tech direction to agent-assisted operating model stewardship |
| CPO | CPO (explicit in model) | Steering | From implicit portfolio to agent-assisted venture-market fit evolution |
| PM | Outcome Owner | Strategy | From spec-writing to goal-setting + outcome validation |
| UX Lead | Experience Director | Strategy | From design execution to experience policy + system-level decisions |
| Architect | Architecture Governor | Strategy | From review meetings to policy authoring + novel pattern decisions |
| Engineering Manager | Agent Fleet Manager | Orchestration | From delivery management to fleet orchestration |
| Senior Developer | Tech Lead / System Architect | Execution | From coding to architecture + agent direction + critical path |
| Developer | Agent Operator | Execution | From writing code to steering agents that write code |
| QA Engineer | Security Policy Author | Quality | From manual testing to policy authoring + anomaly investigation |
| SRE | Reliability Policy Author | Quality | From manual ops to policy authoring + incident leadership |
| Technical Writer | Documentation Division Lead | Execution | From writing all docs to directing doc agent fleets |
| Product Marketing Manager | Product Marketing Lead | Execution | From creating all materials to directing GTM agent fleets |
| Account Executive | Account Executive (enhanced) | Execution | Relationship owner — every interaction agent-prepared |
| CSM | Customer Success Manager (enhanced) | Execution | From manual health checks to agent-surfaced insights + human relationships |
| Support Engineer | Support Engineer (enhanced) | Execution | From manual triage to agent-assisted resolution |
| Manager | Organization Architect | Steering | Org design for human-agent collaboration |

---

## Folder Structure

```
org/
├── README.md                    ← You are here
├── agents/                      ← Agent type registry (governed source of truth)
│   ├── README.md                ← Registry overview and lifecycle documentation
│   ├── _TEMPLATE.yaml           ← Template for defining new agent types
│   ├── steering/                ← Steering layer agent type definitions
│   ├── strategy/                ← Strategy layer agent type definitions
│   ├── orchestration/           ← Orchestration layer agent type definitions
│   ├── execution/               ← Execution layer agent type definitions
│   └── quality/                 ← Quality layer agent type definitions
├── 0-steering/
│   ├── AGENT.md                 ← Instructions for steering-layer agents
│   └── EVOLUTION.md             ← How the company continuously evolves itself
├── 1-strategy/
│   ├── AGENT.md                 ← Instructions for strategy-layer agents
│   └── ventures/               ← Venture charters (customize per your market)
│       └── _TEMPLATE.md         ← Template for creating venture charters
├── 2-orchestration/
│   ├── AGENT.md                 ← Instructions for orchestration-layer agents
│   └── fleet-configs/
│       └── _TEMPLATE.yaml       ← Standard fleet configuration format
├── 3-execution/
│   ├── AGENT.md                 ← Instructions for execution-layer agents
│   └── divisions/            ← One folder per division (customize)
│       └── _TEMPLATE/
│           └── DIVISION.md    ← Template for creating division definitions
└── 4-quality/
    ├── AGENT.md                 ← Instructions for quality-layer agents
    └── policies/                ← Machine-readable quality policies
        ├── security.md
        ├── architecture.md
        ├── experience.md
        ├── performance.md
        ├── delivery.md
        ├── content.md
        └── customer.md
```

---

## Governance

- **Company evolution** (operating model, vision/mission, layer structure) requires Steering Layer C-level PR approval
- **Structural changes** (new ventures, new divisions, merges, splits) require Steering Layer CPO + CTO PR approval
- **Agent type changes** (new types, deprecations, scaling policy) require Steering Layer + CTO PR approval — see [agents/README.md](agents/README.md)
- **Policy changes** require the relevant Policy Author + Architecture Governor approval
- **Fleet configuration changes** require the Mission Lead + AFM approval
- **Division changes** require the Division Tech Lead approval
- All changes are version-controlled, auditable, and reversible via git history
- See [../CODEOWNERS](../CODEOWNERS) for the complete approval mapping
