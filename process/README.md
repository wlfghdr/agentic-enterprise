# Process Lifecycle — The Four Loops

> **What this is:** The universal lifecycle that every piece of work follows — from initial signal to shipped outcome to continuous production operations.  
> **The model:** Four interconnected loops:
> 1. **Discover** — Detect signals, validate opportunities, create mission briefs  
> 2. **Build** — Execute missions, produce outputs, evaluate quality  
> 3. **Ship** — Release, deploy, validate, go live  
> 4. **Operate** — Monitor production health, remediate, manage rollouts, feed signals back into Discover  
>
> Loops 1–3 are **mission-driven** (time-bounded). Loop 4 is **continuous** (event-driven, 24/7).

---

## Overview

```
┌─────────────────────────────────────────────────────────┐
│                    DISCOVER                              │
│   Signals → Analysis → Opportunity → Mission Brief       │
│                                                          │
│        ┌──────────────────────────────────────┐          │
│        │             BUILD                     │          │
│        │   Mission → Tasks → Outputs → Eval    │          │
│        │                                       │          │
│        │      ┌──────────────────────┐         │          │
│        │      │       SHIP           │         │          │
│        │      │  Release → Deploy →  │         │          │
│        │      │  Measure → Learn     │         │          │
│        │      └──────────┬───────────┘         │          │
│        │                 │                     │          │
│        └─────────────────┼─────────────────────┘          │
│                          │                                │
│              Feedback loops (continuous)                   │
└──────────────────────────┼────────────────────────────────┘
                           │
                    work/signals/ ← new signals from production
```

## The Three Loops in Detail

### Loop 1: Discover
**Purpose:** Turn signals (market, customer, technical, internal) into validated mission briefs.

| Phase | Input | Output | Owner |
|-------|-------|--------|-------|
| Signal capture | Raw signal | `work/signals/<signal>.md` | Anyone (human or agent) |
| Signal triage | Signal file | Prioritized, categorized signal | Strategy Layer |
| Opportunity validation | Prioritized signal | Validated opportunity | Strategy Layer + Steering Layer |
| Mission brief | Validated opportunity | `work/missions/<name>/BRIEF.md` | Strategy Layer |

**Loop details:** [1-discover/GUIDE.md](1-discover/GUIDE.md)  
**Agent instructions:** [1-discover/AGENT.md](1-discover/AGENT.md)

### Loop 2: Build
**Purpose:** Execute mission briefs and produce quality-evaluated outputs.

| Phase | Input | Output | Owner |
|-------|-------|--------|-------|
| Mission decomposition | Mission brief | Fleet configuration, work streams | Orchestration Layer |
| Execution | Work streams | Code, docs, content, deliverables | Execution Layer |
| Quality evaluation | Outputs | Evaluation verdicts | Quality Layer |
| Iteration | Evaluation feedback | Improved outputs | Execution Layer |

**Loop details:** [2-build/GUIDE.md](2-build/GUIDE.md)  
**Agent instructions:** [2-build/AGENT.md](2-build/AGENT.md)

### Loop 3: Ship
**Purpose:** Release outputs to production, measure outcomes, and feed learnings back.

| Phase | Input | Output | Owner |
|-------|-------|--------|-------|
| Release preparation | Quality-approved outputs | Release contract | Orchestration Layer |
| Deployment | Release contract | Deployed changes | Execution Layer |
| Measurement | Deployed changes | Outcome data | Quality Layer |
| Learning | Outcome data | New signals, updated policies | All Layers |

**Loop details:** [3-ship/GUIDE.md](3-ship/GUIDE.md)  
**Agent instructions:** [3-ship/AGENT.md](3-ship/AGENT.md)

### Loop 4: Operate & Evolve
**Purpose:** Keep shipped software healthy in production. Monitor, remediate, manage rollouts, and feed production signals back into Discover.

Like Loops 1–3, the Operate loop **spans all 5 layers** — it is not confined to Execution:

| Phase | Input | Output | Owner (Layer) |
|-------|-------|--------|-------|
| Policy definition | Issue learnings, health target data | Health targets, remediation boundaries, alerting standards | Operations Policy Authors (**Quality**) |
| Production monitoring | Deployed software, health targets | Health signals, anomaly alerts | Operations agents (**Execution**) |
| Automated remediation | Anomaly alerts | Rollbacks, restarts, scaling actions | Remediation agents (**Execution**) |
| Progressive rollout | Feature flags, health signals | Rollout advancement, hold, or rollback | Feature flag agents (**Execution**) + Outcome Owners (**Strategy**) |
| Incident coordination | SEV1-2 alerts | War room, responder assembly, timeline | Agent Fleet Managers (**Orchestration**) |
| Incident response | SEV1-4 alerts | Resolution, postmortem, policy updates | Incident agents + on-call engineers (**Execution**) |
| Capacity & performance | Resource metrics, traffic patterns | Optimization actions, forecasts | Capacity agents (**Execution**) |
| Signal interpretation | Production observations | New missions, strategic pivots | Outcome Owners (**Strategy**) |
| Signal generation | All production observations | `work/signals/` entries → Loop 1 | All operations agents (**Execution → Strategy**) |
| Systemic signal aggregation | Operational trends, maturity metrics | Company-level evolution proposals | Steering agents (**Steering**) |

**Key distinction:** Loops 1–3 are mission-driven (time-bounded). Loop 4 is continuous (event-driven, 24/7).

**Loop details:** [4-operate/GUIDE.md](4-operate/GUIDE.md)  
**Agent instructions:** [4-operate/AGENT.md](4-operate/AGENT.md)

---

## Process Governance: Git-Native

This is a **Git-native** company. Git is the system of record, not a side channel.

| Concept | Git Mechanism |
|---------|---------------|
| **Decision** | Pull Request merged to `work/decisions/` |
| **Approval** | PR review approval |
| **RACI** | CODEOWNERS file — see [../../CODEOWNERS](../../CODEOWNERS) |
| **Audit trail** | Git history |
| **Policy change** | PR to `org/4-quality/policies/` |
| **Strategy change** | PR to `org/1-strategy/` |
| **Escalation** | PR with `escalation` label |

### CODEOWNERS Structure

> **Customize** this to match your organization's team structure.

```
# Steering Layer — full repo oversight
*                                           @{{COMPANY_SHORT}}/steering

# Strategy
/org/1-strategy/                            @{{COMPANY_SHORT}}/strategy-leads
/work/missions/                             @{{COMPANY_SHORT}}/strategy-leads

# Orchestration
/org/2-orchestration/                       @{{COMPANY_SHORT}}/orchestration-leads
/org/2-orchestration/fleet-configs/         @{{COMPANY_SHORT}}/fleet-managers

# Quality policies
/org/4-quality/policies/                    @{{COMPANY_SHORT}}/quality-governors

# Process
/process/                                   @{{COMPANY_SHORT}}/process-owners

# Divisions (add one line per division)
# /org/3-execution/divisions/<div-name>/ @{{COMPANY_SHORT}}/<div-team>
```

---

## Templates

All process artifacts use standardized templates. See [templates/](templates/) for the full set:

| Template | Purpose | Used In |
|----------|---------|---------|
| `signal.md` | Capture a signal (market, customer, technical) | Discover loop |
| `signal-digest.md` | Weekly aggregated signal summary with patterns and themes | Discover loop (Steering → Strategy) |
| `mission-brief.md` | Define a mission with scope, constraints, outcomes | Discover → Build |
| `outcome-contract.yaml` | Define measurable success criteria | Build loop |
| `mission-status.md` | Append-only mission progress tracking | Build loop (Orchestration) |
| `decision-record.md` | Document an architecture or strategy decision | Build loop |
| `quality-evaluation-report.md` | Standardized quality evaluation verdict | Build loop (Quality) |
| `release-contract.md` | Define release scope, rollout plan, and rollback | Ship loop |
| `outcome-report.md` | Mission closure: targets vs. actuals, lessons learned | Ship loop → Strategy |
| `component-onboarding.md` | Checklist for onboarding new components | Build loop |
| `asset-registry-entry.yaml` | Register non-code deliverables | Any loop |
| `runbook.md` | Operational runbook for services and workflows | Build → Operate |
| `postmortem.md` | Blameless incident retrospective | Operate loop |
| `venture-health-report.md` | Venture-level metrics rollup | Strategy (periodic) |
| `fleet-performance-report.md` | Fleet throughput, quality, and cost metrics | Orchestration (periodic) |
| `agent-type-proposal.md` | Proposal for new agent types | Any layer → Steering |
| `evolution-proposal.md` | Steering Layer change proposal (structure, process, agents) | Steering loop |

---

## Two-World Model: Human + Agent

Every process step has both a human and an agent dimension:

| Phase | Agent Does | Human Does |
|-------|-----------|------------|
| Signal capture | Monitors data sources, drafts signals | Validates signal importance |
| Mission brief | Drafts brief, estimates scope | Approves brief, sets priorities |
| Execution | Writes code, content, docs | Reviews architecture, key decisions |
| Quality eval | Runs automated checks | Resolves ESCALATE verdicts |
| Deployment | Executes deployment pipeline | Approves production promotion |
| Measurement | Collects metrics, generates reports | Interprets, decides next actions |
| Production ops | Monitors health targets, auto-remediates, manages rollouts | Defines health targets, handles escalations |
| Incident response | Triages, diagnoses, coordinates remediation | Approves postmortems, updates policies |

**Rule:** Agents propose, humans approve. For anything customer-facing, security-critical, or architecture-changing, a human must be in the loop.
