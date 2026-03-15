# Observability Architecture

> How OpenTelemetry integrates with the Agentic Enterprise operating model.

## The Role of Observability

Observability is not just monitoring — it is the **second communication channel** in the operating model. While the Git repository captures decisions and governance, the observability platform captures what actually happened at runtime.

```
        Git Repository                  Observability Platform
        ──────────────                  ──────────────────────
        What was decided                What actually happened
        Governance trail                Execution trail
        Asynchronous                    Real-time
        Agent instructions IN           Telemetry OUT
        Artifacts OUT                   Signals IN (automated)
```

Together, they close the loop: agents read instructions from Git, execute work, emit telemetry to the observability platform, and the platform feeds anomalies back as signals into `work/signals/`.

## How Telemetry Integrates

```
┌──────────────┐    emit spans     ┌──────────────────────┐
│              │ ─────────────────▶│                      │
│   Agent      │                   │   Observability      │
│   Runtime    │    query data     │   Platform           │
│              │ ◀─────────────────│   (OTel-compatible)  │
└──────────────┘                   └──────────┬───────────┘
                                              │
                                   detect anomalies
                                              │
                                              ▼
                                   ┌──────────────────────┐
                                   │  Automated Signal    │
                                   │  → work/signals/     │
                                   │  → New Mission       │
                                   │  → Improvement       │
                                   └──────────────────────┘
```

### What Agents Emit

Every agent action produces an OpenTelemetry span. The telemetry contract is defined in [docs/otel-contract.md](../otel-contract.md).

| Span Type | What It Captures | Example |
|-----------|-----------------|---------|
| `agent.execute` | Agent task execution | "Execute mission task: update API docs" |
| `governance.decision` | Approve/reject/escalate | "PR #47 approved by Engineering Lead" |
| `tool.execute` | External tool calls | "GitHub API: create pull request" |
| `quality.evaluate` | Policy evaluation | "Privacy policy check: PASS" |
| `mission.lifecycle` | Mission state transitions | "MISSION-2026-012: approved → active" |

### What Agents Consume

Before acting, agents query the observability platform for operational context:

| Query | Purpose | Example |
|-------|---------|---------|
| Current SLO status | Don't ship if error budget is exhausted | "API availability: 99.92% (budget: 38% remaining)" |
| Error rate trends | Assess risk before changes | "Error rate trending up 12% over 7 days" |
| Mission cycle times | Inform planning and staffing | "Average mission completion: 4.2 days" |
| Agent performance | Identify bottlenecks | "Agent retry rate: 8% (above 5% threshold)" |

## Key Metrics

These metrics track the health of the operating model itself:

### Mission Lifecycle

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| `mission.completion_time` | Time from approved → completed | Depends on size (small: <2 weeks) |
| `mission.cycle_time` | Time from signal → release | Trending down over time |
| `mission.success_rate` | Missions completed vs. cancelled | >80% |
| `mission.blocked_time` | Time spent in paused/blocked state | <10% of total lifecycle |

### Agent Performance

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| `agent.task_success_rate` | Tasks completed without human intervention | Trending up |
| `agent.escalation_rate` | Tasks escalated to humans | Trending down |
| `agent.retry_rate` | Failed actions retried | <5% |
| `agent.latency_p95` | 95th percentile task duration | Within SLO |

### PR Flow

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| `pr.merge_latency` | Time from PR open → merge | <24 hours for standard PRs |
| `pr.review_turnaround` | Time from review request → review | <8 hours |
| `pr.ci_pass_rate` | PRs that pass CI on first attempt | >90% |
| `pr.revision_count` | Number of revision cycles per PR | <3 |

### Policy Compliance

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| `policy.pass_rate` | Quality evaluations that pass | >95% |
| `policy.violation_rate` | Policy violations detected at runtime | <2% |
| `policy.remediation_time` | Time to fix a policy violation | <48 hours |
| `human.intervention_rate` | Decisions requiring human override | Trending down |

## Implementation Approach

### OTel-First

The framework standardizes on OpenTelemetry as the telemetry protocol. This is vendor-neutral — you can send data to any compatible backend:

```
Agent Runtime
    │
    │  OTLP (OpenTelemetry Protocol)
    ▼
OTel Collector
    │
    ├──▶ Grafana / Prometheus  (open source)
    ├──▶ Any enterprise APM     (enterprise)
    ├──▶ Elastic               (log-centric)
    └──▶ Any OTLP backend      (your choice)
```

### Minimum Viable Observability

You don't need a full observability stack to start. The minimum is:

1. **Structured JSON logs to stdout** — Every agent action logged with span context
2. **Git history as audit trail** — Commit messages and PR descriptions capture decisions
3. **Manual dashboards** — Periodically review metrics from Git data (PR merge times, mission durations)

As your deployment matures, add:

4. **OTel Collector** — Centralized telemetry collection
5. **Dashboards** — Real-time visibility into agent fleet health
6. **Automated signals** — Anomaly detection that files signals back into `work/signals/`

## The Feedback Loop

The observability platform doesn't just watch — it participates in governance:

```
1. Agent executes task
       │
2. Emits OTel spans (traces, metrics, events)
       │
3. Platform detects anomaly (e.g., error rate spike)
       │
4. Platform files automated signal
   → work/signals/auto-2026-03-14-error-rate-spike.md
   → source: observability-platform
       │
5. Steering/Strategy Layer triages signal
       │
6. New mission created to address root cause
       │
7. Agent executes fix, emits telemetry
       │
8. Platform confirms anomaly resolved
```

This is how the operating model evolves itself: runtime telemetry creates organizational improvement.

## Reference

- [OTel Contract](../otel-contract.md) — Canonical attribute names, span types, and privacy defaults
- [Observability Integration Category](../../org/integrations/categories/observability.md) — Platform connection patterns
- [AGENTS.md Rule 9](../../AGENTS.md) — Observability requirements for all agents
