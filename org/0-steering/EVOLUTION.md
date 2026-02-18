# Steering Layer — Evolution Process

> **What this is:** The continuous process by which the company evolves itself — its structure, operating model, processes, venture portfolio, division map, and agent instructions.  
> **Scope:** This process is unique to Layer 0. It governs how all other processes, structures, and models change.  
> **Governance:** Changes to this evolution process itself require CEO + CTO approval via PR.

---

## The Three Evolution Loops

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│   LOOP 1: CONTINUOUS SENSING           (Always Running)              │
│   Cadence: Real-time / Daily                                         │
│   Agents aggregate improvement signals from all layers.              │
│   Pattern detection. Anomaly flagging. No human approval needed.     │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   LOOP 2: STRUCTURAL PROPOSALS         (Weekly / Bi-Weekly)          │
│   Agents draft evolution proposals from accumulated evidence.        │
│   Impact assessments, rollback plans, success metrics.               │
│   Proposals become PRs for executive review.                         │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   LOOP 3: STRATEGIC RECALIBRATION      (Monthly / Quarterly)         │
│   Executives review company trajectory against vision.               │
│   Portfolio-level rebalancing. Operating model assessment.           │
│   Big bets: new ventures, market pivots, org restructuring.         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Loop 1: Continuous Sensing

**Purpose:** Gather, aggregate, and pattern-match improvement signals from every part of the company.

### Signal Sources

| Source | Signal Type | Where It Lands |
|--------|------------|----------------|
| Execution Layer agents | Friction signals (blocked by unclear instructions, policy conflicts) | `work/signals/` |
| Quality Layer agents | Policy violation patterns, evaluation bottlenecks | `work/signals/` |
| Orchestration Layer agents | Fleet performance anomalies, cross-mission conflicts | `work/signals/` |
| Strategy Layer agents | Market shifts, competitive moves that challenge strategy | `work/signals/` |
| Steering Layer agents | Cross-layer pattern analysis, model health metrics | Internal analysis |
| {{OBSERVABILITY_TOOL}} telemetry | Agent fleet performance, development velocity, deployment safety | Operational data |

### Sensing Outputs
- **Signal digest:** Weekly summary of all incoming signals, grouped by theme (template: `process/templates/signal-digest.md`, stored in `work/signals/digests/`)
- **Pattern alerts:** When 3+ related signals suggest a systemic issue
- **Anomaly flags:** When a metric deviates significantly from baseline

---

## Loop 2: Structural Proposals

**Purpose:** Convert evidence into concrete, executable proposals for organizational or process change.

### Proposal Process

```
Signal Pattern Detected → Analysis → Draft Proposal → Peer Review → Executive Review → Implementation → Measure & Iterate
```

**Template:** `process/templates/evolution-proposal.md` — all proposals follow this standardized format.

### Proposal Categories

| Category | Examples | Approval Required |
|----------|----------|-------------------|
| **Division merge/split** | Merge two divisions, split a large one | CPO + CTO |
| **New venture** | Add a new venture to the portfolio | CEO + CPO |
| **Venture sunset** | Remove or merge a venture | CEO + CPO |
| **Process improvement** | Change how work flows between layers | COO + CTO |
| **Operating model update** | Change how the model itself works | CEO + CTO |
| **Agent instruction update** | Update global AGENTS.md or layer instructions | CTO |
| **New agent type** | Propose a new agent type for the registry (`org/agents/`) | CTO |
| **Agent type deprecation** | Retire an agent type from the registry | CTO |
| **Agent scaling policy change** | Change scaling parameters for agent types | CTO + CFO |
| **Policy evolution** | Propose new policies or major policy changes | CTO + relevant Policy Author |
| **Investment rebalancing** | Shift resources between ventures/divisions | CEO + CFO |
| **Vision/mission update** | Revise COMPANY.md beliefs or direction | CEO + Board |

---

## Loop 3: Strategic Recalibration

### Scheduled Reviews

| Review | Cadence | Focus | Participants |
|--------|---------|-------|-------------|
| **Operating Model Health** | Monthly | Is the 5-layer model working? Process efficiency? | CTO + COO |
| **Venture Portfolio** | Quarterly | Are we in the right markets? Portfolio balance? | CEO + CPO + CFO |
| **Technology Direction** | Quarterly | Are our technology bets paying off? | CTO + Architecture Governors |
| **GTM Effectiveness** | Quarterly | Is our go-to-market working? | CRO + CPO |
| **People & Transformation** | Quarterly | How are humans experiencing the transformation? | CHRO + Layer Leads |
| **Company Direction** | Semi-annual | Is our vision still right? | CEO + Full C-Suite + Board |

---

## Evolution Types Reference

### Division Merges
**When to merge:** Two divisions have >50% scope overlap and separation creates coordination overhead without clear benefits.

### Division Splits
**When to split:** A division has grown to serve 3+ distinct domains and a single Tech Lead cannot effectively govern the full scope.

### Venture Portfolio Changes
**When to add:** Market evidence shows a gap that aligns with divisions and strategic beliefs.
**When to sunset:** Market relevance has declined or the venture has been absorbed by a broader offering.

### Anti-Patterns
- **Restructuring addiction** — Every change must have evidence and measured outcomes.
- **Ivory tower syndrome** — Always incorporate signals from Execution Layer.
- **Analysis paralysis** — Act on directional evidence with reversible changes.
- **Ignoring human impact** — CHRO perspective must be present in every proposal.
- **Model worship** — The model serves the company, not the other way around.
