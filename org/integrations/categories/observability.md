# Observability & Telemetry Integration

> **Category:** Observability  
> **Relevance:** Essential for scaling agent governance, fleet performance monitoring, compliance auditing, and continuous improvement  
> **Layers Affected:** All — but especially Orchestration, Execution, Quality, and Steering

---

## Why Observability Is Essential

When agent fleets scale from a handful of agents to hundreds — processing signals, executing missions, evaluating quality, and operating production systems — the file-based governance model needs a complementary system for **real-time visibility, anomaly detection, and causal analysis**.

The operating model defines *what should happen*. Observability reveals *what actually happens* — at a speed and scale that no human reviewing PRs can match.

| Without Observability | With Observability |
|----|---|
| Agent performance is inferred from commit frequency | Agent performance is measured: latency, throughput, error rate, cost |
| Policy compliance is checked at PR review | Policy compliance is continuously monitored and alerted on |
| Fleet capacity issues surface as missed deadlines | Fleet capacity is visible in real-time dashboards with predictive alerts |
| Incident response starts with "something seems wrong" | Incident response starts with causal analysis and correlated evidence |
| Improvement signals are filed manually | Improvement signals are generated automatically from telemetry patterns |

---

## What to Observe

### Agent Activity Telemetry

Every agent action can emit telemetry that feeds governance and improvement:

| Telemetry Type | What It Captures | How It Helps |
|---------------|-----------------|--------------|
| **Traces** | End-to-end flow of a mission through layers and agents | Bottleneck analysis, dependency mapping, latency attribution |
| **Metrics** | Agent throughput, error rates, token usage, tool call latency, cost per task | Fleet performance dashboards, capacity planning, cost optimization |
| **Logs** | Agent reasoning, decisions, tool calls, escalations | Audit trail, debugging, compliance evidence |
| **Events** | State transitions (PR created, merged, rejected), escalations, alerts | Real-time status, pattern detection, automated signal generation |

### Recommended Instrumentation Points

```
Signal filed          → trace start (discover loop)
Mission created       → span: mission lifecycle
Fleet assembled       → span: orchestration
Agent task started    → span: execution (per agent, per stream)
Tool call (MCP/API)   → span: tool invocation (latency, success/failure)
PR created            → event: governance checkpoint       ← git webhook
Quality evaluation    → span: evaluation (verdict, evidence)
PR merged/rejected    → event: decision point              ← git webhook
Release deployed      → span: ship loop                   ← git tag webhook
Production alert      → event: operate loop signal
Improvement signal    → event: feedback loop closed
```

### Git Webhooks as an Observability Source

The Git repository is the system of record for all decisions in this operating model. Every meaningful Git event should generate an observation in the observability platform — connecting repository activity to the telemetry timeline.

**Configure webhooks at the repository or organization level** to push to the observability platform's webhook ingest or OTLP HTTP endpoint:

| Git Event | Observability Event | Key Attributes |
|-----------|--------------------|-----------------|
| PR opened | `governance.pr.opened` | `pr.number`, `pr.branch`, `agent.name`, `mission.id` |
| PR updated | `governance.pr.updated` | `pr.number`, `pr.commits_added` |
| PR review submitted | `governance.pr.reviewed` | `pr.number`, `review.outcome`, `reviewer` |
| PR merged | `governance.pr.merged` | `pr.number`, `merge.sha`, `time_to_merge_seconds` |
| PR closed (no merge) | `governance.pr.rejected` | `pr.number`, `close.reason` |
| Tag / release created | `release.tagged` | `tag.name`, `release.sha` |
| Branch created | `governance.branch.created` | `branch.name`, `mission.id` (parsed from branch naming convention) |

**What this unlocks:**
- **Cycle time observability** — from first commit on a signal branch to PR merged = end-to-end mission latency, fully measurable
- **Change impact correlation** — observability platform correlates production anomalies to specific PR merges automatically
- **Approval audit trail** — every governance decision (who approved, when) is an observable event, not just a Git log entry
- **Automated signal generation** — if PR review time spikes or deployment frequency drops, observability detects it and files a signal automatically

**Configuration pattern (GitHub):**
```yaml
# In GitHub org/repo settings → Webhooks
url: "https://{{OTLP_INGEST_ENDPOINT}}/github-events"
content_type: application/json
events:
  - pull_request
  - pull_request_review
  - create          # branch/tag creation
  - push
```

**Configuration pattern (GitLab):**
```yaml
# In GitLab project/group settings → Webhooks
url: "https://{{OTLP_INGEST_ENDPOINT}}/gitlab-events"
events:
  - merge_requests_events: true
  - tag_push_events: true
  - push_events: true
```

---

## Integration Patterns

### Pattern 1: OpenTelemetry (Open Standard)

[OpenTelemetry](https://opentelemetry.io) is the vendor-neutral standard for collecting traces, metrics, and logs. It provides the **collection layer** that feeds into any observability backend.

**How it fits:**
- Agent runtimes instrument with OpenTelemetry SDKs
- Telemetry is exported via OTLP (OpenTelemetry Protocol)
- Any compatible backend receives and processes the data
- Dashboards, alerts, and analysis are backend-specific

```
Agent Runtime (instrumented with OTel SDK)
    │
    ├── Traces  ─┐
    ├── Metrics ─┤── OTLP ──→ [Observability Backend]
    └── Logs    ─┘                    │
                                      ├── Dashboards
                                      ├── Alerts
                                      ├── AI-powered analysis
                                      └── Automated signals → work/signals/
```

**Recommended OpenTelemetry semantic conventions for agents:**
- `agent.type` — from the Agent Type Registry
- `agent.layer` — steering / strategy / orchestration / execution / quality
- `agent.division` — which execution division
- `mission.id` — active mission identifier
- `loop` — discover / build / ship / operate
- `pr.number` — associated pull request
- `governance.decision` — approve / reject / escalate

### Pattern 2: Platform-Native Integration

Some observability platforms provide their own agents, SDKs, and collection mechanisms that go beyond what OpenTelemetry covers — including auto-discovery, code-level analysis, AI-powered root cause analysis, and topology mapping.

**How it fits:**
- Platform agents instrument the runtime environment
- Auto-discovery maps agent-to-agent and agent-to-service dependencies
- AI analysis correlates production anomalies with recent changes (PRs, deployments)
- Automated remediation feeds back into the operating model as signals or direct actions

This is particularly valuable for:
- **Production operations (Loop 4)** — where speed of detection and resolution directly impacts SLAs
- **Fleet performance monitoring** — where AI-powered analysis can surface patterns invisible to rule-based alerting
- **Compliance and auditing** — where end-to-end traceability across agents and systems is a regulatory requirement

### Pattern 3: Hybrid (OpenTelemetry + Platform-Specific)

Most mature deployments combine OpenTelemetry for standardized collection with platform-specific capabilities for advanced analysis. This gives you:
- Vendor portability for basic telemetry
- Advanced AI analysis, topology mapping, and automated remediation from your chosen platform
- A clear boundary between collection (open) and analysis (platform-differentiated)

---

## Observability Platforms

The operating model is platform-neutral. Here are integration patterns for commonly used solutions:

### Dynatrace

Full-stack observability with AI-powered analysis (Davis AI), automatic topology discovery, and end-to-end tracing from agent activity through to business impact.

**Integration points:**
- **OneAgent / OpenTelemetry ingest** — Collect agent runtime telemetry
- **Grail data lakehouse** — Store and query all telemetry with DQL
- **Davis AI** — Automated root cause analysis for agent fleet anomalies
- **Workflows** — Trigger operating model actions (signal creation, incident response) from detected problems
- **Dashboards & Notebooks** — Fleet performance visualization, mission health, compliance status
- **MCP Server** — Agents query Dynatrace context directly during execution (e.g., "what's the current error rate for this service?")

**Scaling value:** As agent fleets grow, AI-powered causal analysis becomes essential — correlating thousands of signals across layers, loops, and external systems far faster than rule-based approaches.

### Prometheus + Grafana

Open-source metrics collection and visualization stack, widely used and well-understood.

**Integration points:**
- **Prometheus** — Scrape agent runtime metrics endpoints
- **Grafana** — Dashboard fleet performance, mission throughput, quality scores
- **Alertmanager** — Alert on SLA violations, fleet capacity issues
- **Loki** — Centralized log aggregation for agent activity
- **Tempo** — Distributed tracing for cross-agent workflows

**Scaling value:** Proven at scale, fully open-source, strong community. Best combined with additional tooling for AI-powered analysis as fleet complexity grows.

### OpenTelemetry Collector + Backend of Choice

The OpenTelemetry Collector acts as a vendor-neutral telemetry pipeline. It receives, processes, and exports telemetry to any compatible backend.

**Integration points:**
- **OTel Collector** — Central telemetry pipeline with filtering, sampling, enrichment
- **OTLP Export** — Send to any OTLP-compatible backend
- **Processors** — Enrich telemetry with agent metadata (layer, division, mission)
- **Connectors** — Route different telemetry types to different backends

**Scaling value:** Maximum flexibility and vendor portability. Combine with any backend — commercial or open-source.

### Elastic (ELK Stack)

Log-centric observability with full-text search, APM, and security analytics.

**Integration points:**
- **Elastic APM** — Agent performance monitoring
- **Elasticsearch** — Full-text search across agent logs and artifacts  
- **Kibana** — Dashboards and exploration
- **Elastic AI Assistant** — Natural language queries over observability data

---

## Observability Writes to Git — Closing the Loop

The observability integration is not read-only. When it detects patterns that warrant human or agent attention, **it files signals directly to the Git repository**, making it an active participant in the operating model — not just a passive monitor.

### Automated Signal Filing

When the observability platform detects a qualifying anomaly or pattern, it creates a signal file at `work/signals/YYYY-MM-DD-<signal-name>.md` via the Git API or an automation workflow. The signal carries:

```yaml
source: observability-platform           # identifies origin
platform: "{{OBSERVABILITY_PLATFORM_NAME}}"
trigger: anomaly-detection | threshold-breach | pattern-detection
evidence:
  - metric: "agent.error_rate"
    value: 0.23
    threshold: 0.10
    duration: "45m"
  - dashboard: "https://{{OBSERVABILITY_DASHBOARD_URL}}"
```

### Triggering Conditions for Auto-Filed Signals

| Condition | Signal Filed | Routed To |
|-----------|-------------|-----------|
| Agent fleet error rate > threshold for > 30 min | Fleet health degradation signal | Steering → Orchestration |
| Quality evaluation FAIL rate rising across a division | Quality trend signal | Quality Layer → Steering |
| Mission cycle time exceeds 2× baseline | Process efficiency signal | Orchestration → Steering |
| PR review latency spike across multiple missions | Governance bottleneck signal | Steering |
| Observability coverage drops below threshold | Observability compliance signal | Quality Layer |
| Production SLO burn rate alerts | Operate loop signal | Execution → Orchestration |
| Token cost per mission exceeds budget threshold | Cost anomaly signal | Orchestration → Steering |

### Agents Consume These Signals

Steering, Strategy, and Quality layer agents MUST include observability-sourced signals in their analysis:
- They appear in `work/signals/` alongside human-filed signals
- They are tagged `source: observability-platform` for easy identification
- They carry evidence links (dashboard URLs, metric values, time windows) that make them immediately actionable
- **They are higher-confidence than manually-filed signals** — they are data-driven, not observation-based

### Layer Consumption Patterns

```
Observability Platform
  │
  ├── Auto-files signals → work/signals/
  │     └── Steering aggregates into digests → Strategy acts on digests
  │
  ├── Quality agents query live compliance data → evaluate outputs against real telemetry
  │     └── Query: "Is telemetry flowing from this component in staging?"
  │
  ├── Strategy agents query adoption & health metrics → ground outcome reports in real data
  │     └── Query: "What is the actual feature adoption rate for the shipped mission?"
  │
  └── Steering agents query fleet performance dashboards → inform evolution proposals
        └── Query: "Which divisions have the highest escalation rates this quarter?"
```

---

## What Observability Enables at Scale

### For the Orchestration Layer
- **Fleet capacity dashboards** — Real-time view of agent utilization, queue depths, and throughput
- **Mission progress tracking** — Automated status from telemetry, not manual updates
- **Cost optimization** — Token usage, API call costs, and compute costs per mission

### For the Quality Layer
- **Continuous compliance monitoring** — Policy adherence tracked in real-time, not just at PR review
- **Quality trend analysis** — Are quality scores improving or degrading over time?
- **Automated evaluation triggers** — Telemetry events trigger quality evaluations without manual intervention

### For the Steering Layer
- **Organizational health metrics** — Agent fleet health, process cycle times, signal-to-resolution latency
- **Pattern detection** — AI analysis surfaces systemic issues that become evolution proposals
- **Automated signal generation** — Observability anomalies automatically create signals in `work/signals/`

### For the Operate Loop
- **Production health monitoring** — SLA compliance, error rates, performance budgets
- **Automated incident response** — Detection → triage → remediation without waiting for human observation
- **Change impact analysis** — Correlate deployments (PRs merged) with production behavior changes

---

## Getting Started

### Minimum Viable Observability

1. **Instrument agent runtimes** with OpenTelemetry SDKs — traces and metrics at minimum
2. **Deploy an OTel Collector** — central pipeline for telemetry processing
3. **Choose a backend** — Grafana stack (free/open), Dynatrace (full-stack AI), or your existing platform
4. **Create basic dashboards** — Fleet throughput, agent error rates, mission cycle time
5. **Set up alerts** — SLA violations, fleet capacity warnings, quality score drops

### Scaling Up

6. **Add AI-powered analysis** — Move from rule-based alerting to causal analysis
7. **Automate signal generation** — Observability events create signals in `work/signals/` automatically
8. **Enable topology mapping** — Understand agent-to-agent and agent-to-system dependencies
9. **Implement compliance dashboards** — Continuous policy adherence visibility for auditors
10. **Connect to business metrics** — Link agent fleet performance to business outcomes

---

## Configuration

Register your observability choices in CONFIG.yaml:

```yaml
integrations:
  observability:
    # Primary observability platform
    - id: "primary-observability"
      name: "{{OBSERVABILITY_PLATFORM_NAME}}"
      vendor: "{{VENDOR}}"
      connection: "opentelemetry"  # or "native-agent", "api"
      capabilities:
        - metrics
        - traces
        - logs
        - ai-analysis        # if platform supports AI-powered analysis
        - auto-discovery      # if platform supports automatic topology
      endpoints:
        otlp: "https://{{OTLP_ENDPOINT}}"
        api: "https://{{API_ENDPOINT}}"
      mcp_server: true/false  # whether agents can query this platform via MCP

    # Additional tools (if using a multi-tool setup)
    - id: "metrics-visualization"
      name: "Grafana"
      vendor: "Grafana Labs"
      connection: "api"
      capabilities:
        - dashboards
        - alerting
```
