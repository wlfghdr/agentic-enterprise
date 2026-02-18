# Loop 4: Operate & Evolve — Human Guide

> **For:** Operations Policy Authors, Operations Leads, On-Call Engineers, Outcome Owners, Agent Fleet Managers  
> **Your role:** You define operational policies, respond to escalations, lead issue resolution, and make judgment calls that go beyond automated remediation. You also interpret operational signals that inform product strategy.  
> **Key difference from Loops 1–3:** This loop never ends. It runs continuously, 24/7. Your engagement is primarily event-driven (issues, escalations, policy reviews) rather than mission-driven.

---

## Which Layers Are Involved

Loop 4 is **not an Execution-only concern**. Like Loops 1–3, it spans all 5 organizational layers:

| Layer | Role in Operate | Who |
|-------|-----------------|-----|
| **Steering** | Receives systemic operational signals (cost trends, auto-remediation maturity, production health posture) that inform company-level evolution | Executives, Organization Architects |
| **Strategy** | Interprets production signals → decides which warrant new missions. Owns the Operate → Discover feedback loop | Outcome Owners, Venture Leads |
| **Orchestration** | Coordinates operations agent fleets. Creates missions from production signals. Leads incident coordination (SEV1/2 war rooms) | Agent Fleet Managers, Mission Leads |
| **Execution** | Runs the agents: operations, remediation, feature flags, incidents, resilience, capacity, performance. Human on-call handles escalations | Tech Leads, On-Call Engineers, Operations Teams |
| **Quality** | Defines the policies that operations agents enforce: health targets, issue severity, remediation boundaries, rollback criteria, alerting standards | Operations Policy Authors, Security Policy Authors |

The sections below are organized by **your role**, not by layer. Most humans in Loop 4 belong to one layer but interact with adjacent layers regularly.

---

## What This Loop Covers

After software ships (Loop 3), it enters the Operate loop. This is where the software **lives** — where real customers use it, where reliability matters, and where production signals generate the richest input for future product decisions.

```
Loop 3 (Ship) completes → Feature is GA → Loop 4 begins (and never ends)

  ┌────────────────────────────────────────────────────────────────────┐
  │                    OPERATE & EVOLVE (Continuous)                   │
  │                                                                    │
  │  Health Agents ──► Monitor service health, error budgets, deployment health  │
  │       │                                                            │
  │       ▼                                                            │
  │  Anomaly Detected?                                                 │
  │       │                                                            │
  │       ├─ No ──► Continue monitoring                                │
  │       │                                                            │
  │       └─ Yes ──► Classify severity                                 │
  │                    │                                                │
  │           ┌────────┼────────┐                                      │
  │           ▼        ▼        ▼                                      │
  │        SEV3-4   SEV2     SEV1                                      │
  │        Auto-    Auto-    HUMAN                                     │
  │        remediate remediate ESCALATION                              │
  │        + log    + notify  + War Room                               │
  │           │        │        │                                      │
  │           ▼        ▼        ▼                                      │
  │        Verify   Verify   Resolve                                   │
  │        outcome  outcome  + Postmortem                              │
  │           │        │        │                                      │
  │           └────────┴────────┘                                      │
  │                    │                                                │
  │                    ▼                                                │
  │        File improvement signal → work/signals/ → Loop 1 (Discover)│
  │                                                                    │
  │  In parallel (always running):                                     │
  │  • Feature flag agents manage progressive rollouts                 │
  │  • Capacity agents forecast and optimize resources                 │
  │  • Performance agents monitor baselines and detect regression      │
  │  • Resilience agents run chaos experiments                         │
  │  • Cost agents track and optimize cloud spend                     │
  │                                                                    │
  └────────────────────────────────────────────────────────────────────┘
```

---

## What You Do

### 1. Define & Evolve Operational Policies (Operations Policy Authors)

You author the policies that operations agents enforce autonomously:

| Policy Area | What You Define |
|---|---|
| **Health target standards** | Which indicators to measure, target thresholds, error budget windows |
| **Issue severity** | Blast radius thresholds, customer impact tiers, escalation triggers |
| **Remediation boundaries** | What agents can auto-remediate vs. what requires human approval |
| **Rollback criteria** | Health signal thresholds that trigger automatic rollback |
| **Alert quality** | Actionability requirements — no alert without clear action |
| **Capacity thresholds** | When to auto-scale, when to alert, when to escalate |

### 2. Respond to Escalations (On-Call Engineers)

When operations agents escalate, you investigate and resolve:

| Escalation Type | Your Response |
|---|---|
| **Novel failure pattern** | Investigate root cause → diagnose → fix → update runbook |
| **Remediation scope exceeded** | Review proposed action → approve, modify, or reject |
| **Health target breach with customer impact** | Lead issue response: war room, communication, resolution |
| **Security vulnerability** | Assess severity → coordinate emergency patch → verify fix |
| **Cost anomaly** | Investigate cause → approve remediation → file signal if structural |

### 3. Manage Progressive Rollout Decisions (Outcome Owners, AFMs)

Feature flag agents manage ongoing rollouts, but key decisions are yours:

| Decision | When You're Involved |
|---|---|
| **Advance rollout** | Agent recommends widening → you approve |
| **Hold rollout** | Agent detects marginal signals → you decide |
| **Kill a feature** | Agent triggers kill switch → you decide if temporary or needs rework |
| **Interpret experiments** | A/B test results are ambiguous → you interpret business context |
| **Clean up stale flags** | Agent alerts on old flags → you decide whether to remove |

### 4. Interpret Operational Signals for Strategy

The most valuable output of Loop 4 is the **feedback loop to Loop 1**:

- Operations agents file signals in `work/signals/` based on production observations
- You interpret whether these signals warrant new missions
- **This is the loop that closes the entire model.** Without Operate → Discover feedback, the model is linear. With it, the model is circular.

---

## What You DON'T Do Anymore

- **Don't manually check health metrics** — agents monitor continuously
- **Don't manually write postmortems** — agents draft them, you review
- **Don't manually track feature flag status** — agents manage progression
- **Don't manually forecast capacity** — agents project trends, you validate
- **Don't manually investigate every alert** — agents auto-remediate within policy

---

## Cadence

| Activity | Frequency | Who |
|---|---|---|
| **Health target review** | Weekly (automated) | Operations Policy Authors |
| **Incident response** | Event-driven (24/7) | On-Call Engineers |
| **Rollout decisions** | As-needed | Outcome Owners, AFMs |
| **Operational signal triage** | Weekly | Outcome Owners |
| **Policy evolution** | Monthly or post-incident | Operations Policy Authors |
| **Cost review** | Monthly | Operations Leads |

---

## The Feedback Loop — Why This Loop Matters Most

```
 Loop 4 (Operate) generates signals:
   "Feature X adoption is <2% after 6 weeks"
   "Service Y had 3 incidents from the same subsystem"
   "Query Z degrades 5% per month at current data growth"
         │
         ▼
 Signals filed in work/signals/
         │
         ▼
 Loop 1 (Discover) picks them up:
   Strategy Layer triages, prioritizes, creates missions
         │
         ▼
 Loop 2 (Build) → Loop 3 (Ship) → Loop 4 (Operate)
         │
         ▼
 The cycle continues — the company continuously improves
```

**Without Loop 4, the model is a factory (idea → product). With Loop 4, the model is a living system (idea → product → evidence → better idea).**
