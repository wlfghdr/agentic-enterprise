# Quality Policy: Observability

> **Applies to:** All services, apps, components, agents, and pipelines — nothing ships without proper observability
> **Enforced by:** Quality Layer eval agents, including the dedicated [Observability Compliance Agent](../../agents/quality/observability-compliance-agent.md)
> **Authority:** Operations leads + Architecture Governors
> **Principle:** If it runs, it must be observable. If it's not observable, it doesn't ship.
> **Version:** 1.0 | **Last updated:** 2026-02-19

---

## Observable by Default — The Prime Directive

**Observability is not a feature you add later. It is the first thing you build.**

Before any component, agent, workflow, or pipeline is considered "done" — before it enters PR review, before quality evaluation, before any merge — its instrumentation must be complete and telemetry must be verified flowing to the registered observability integration.

This policy establishes observability as a **hard gate**, not a checklist item:

| Stage | Gate |
|-------|------|
| PR opened | Instrumentation code present (static check) |
| PR review | Telemetry verified in staging (evidence required) |
| Quality evaluation | Observability Compliance Agent issues PASS verdict |
| Release contract | SLOs configured, dashboards linked, alerts active |
| Production deploy | Post-deploy monitoring plan active |

**No exception exists for shipping without any observability.** The Observability Compliance Agent will BLOCK any output that lacks verified instrumentation.

---

## Why This Policy Exists

Observability is not optional. Every service, app, agent, and pipeline must be instrumented so that:

1. **Problems are detected before customers notice** — proactive, not reactive
2. **Issues are diagnosed in minutes, not hours** — distributed traces, correlated logs, precise metrics
3. **Health targets are provably met** — data-driven, not anecdotal
4. **Agents can self-monitor and self-correct** — autonomous operations require observability as a prerequisite

---

## Mandatory Requirements (All Components)

### Instrumentation — Non-Negotiable

Every deployed component MUST have at least one instrumentation source active. The method depends on component type, but the outcome is the same: full observability.

| Component Type | Primary Instrumentation | Acceptable Alternatives |
|----------------|------------------------|------------------------|
| Backend service | OpenTelemetry SDK (auto + manual) | APM agent, API ingest |
| Frontend app | RUM / browser instrumentation | OTel JS SDK |
| Agent / AI workflow | OTel SDK (manual spans for tool calls, LLM invocations) | API ingest (metrics + logs) |
| Data pipeline / batch job | OTel SDK or API ingest | Process monitoring agent |
| Infrastructure component | Infrastructure monitoring agent | OTel Collector |
| Third-party integration | OTel Collector as proxy | API ingest (push) |

- [ ] **At least one instrumentation method is active and verified** before first production deployment
- [ ] **Instrumentation verified in staging** — telemetry data appears in {{OBSERVABILITY_TOOL}} within 5 minutes of deployment
- [ ] **No blind spots:** every service-to-service call is traceable end-to-end

### The Three Pillars — Minimum Coverage

#### 1. Distributed Traces

- [ ] All inbound requests produce a trace (HTTP, gRPC, messaging)
- [ ] Trace context is propagated across all service boundaries (W3C Trace Context)
- [ ] Custom spans added for business-critical operations (not just framework-level spans)
- [ ] Span attributes include: service name, version, environment, division owner
- [ ] Agent operations produce spans: tool calls, LLM invocations, decision points, handoffs
- [ ] Database queries are captured as child spans with query text (sanitized — no PII)
- [ ] External API calls are captured as spans with endpoint, method, status code, and duration

#### 2. Metrics

- [ ] **RED metrics** exposed for every service endpoint:
  - **R**ate — requests per second
  - **E**rrors — error rate (4xx, 5xx, or domain-specific errors)
  - **D**uration — latency percentiles (p50, p95, p99)
- [ ] **USE metrics** exposed for infrastructure-level components:
  - **U**tilization — CPU, memory, disk, network
  - **S**aturation — queue depths, thread pool usage, connection pool usage
  - **E**rrors — hardware/OS-level errors
- [ ] **Business metrics** for user-facing features:
  - Feature adoption (usage count, unique users)
  - Conversion/completion rates for workflows
  - Data volume processed (for pipeline components)
- [ ] **Agent-specific metrics:**
  - Token consumption per task
  - Tool call success/failure rates
  - Decision latency (time from signal to action)
  - Autonomous vs. escalated resolution ratio
- [ ] Metrics use standard naming conventions (dot-separated, lowercase)
- [ ] Metric dimensions include: `service.name`, `service.version`, `division`

#### 3. Logs

- [ ] Structured logging (JSON) with consistent field names across all services
- [ ] Every log entry includes: timestamp, severity, service name, trace ID, span ID
- [ ] Log levels used correctly:
  - `ERROR` — actionable failures requiring investigation
  - `WARN` — degraded operation, potential issue
  - `INFO` — significant business events (not noise)
  - `DEBUG` — diagnostic detail (disabled in production by default)
- [ ] **No PII in logs** (cross-reference: [security.md](security.md))
- [ ] Log volume is proportional to activity (no excessive logging that drowns signal in noise)
- [ ] Error logs include: error type, stack trace (or error code), originating request context

---

## Service Health Target Requirements

Every production service MUST define and track at least one health target:

- [ ] **Availability target** defined (target ≥ 99.5% unless explicitly justified lower)
- [ ] **Latency target** defined (aligned with [performance.md](performance.md) budgets)
- [ ] Health targets configured in {{OBSERVABILITY_TOOL}} with:
  - Appropriate burn rate alerts
  - Error budget tracking visible on a dashboard
  - Error budget depletion alerts at configurable thresholds
- [ ] Health targets reviewed quarterly with evidence (→ tighten if consistently exceeded, investigate if breached)

---

## Dashboards & Visualization

- [ ] **Service health dashboard** created for every production service:
  - Key metrics for all endpoints
  - Health target status and error budget
  - Dependency health (downstream services, databases, external APIs)
  - Recent deployments overlaid on metrics timeline
- [ ] Dashboard URL registered in Software Catalog entity metadata
- [ ] **On-call dashboard** for services with incident response requirements:
  - Current alert status
  - Runbook links for each alert
  - Escalation contacts

---

## Alerting & Anomaly Detection

- [ ] **Anomaly detection** enabled for all instrumented services
- [ ] **Custom alerts** configured for:
  - Health target burn rate thresholds
  - Error rate exceeding baseline by > 2x
  - Latency exceeding target by > 50%
  - Resource saturation > 80% (CPU, memory, disk, connections)
  - Data pipeline lag exceeding threshold (for pipeline components)
  - Agent task failure rate exceeding 10%
- [ ] Alert routing configured:
  - P1/P2: Alerting/paging system → on-call engineer
  - P3/P4: Team chat channel
  - Agent-resolvable issues: routed to remediation agent
- [ ] **No alert fatigue:** every alert must have a documented runbook action. Alerts that fire > 5x/week without action must be tuned or removed.
- [ ] Alert definitions stored as code (GitOps)

---

## Agent Observability — Special Requirements

AI agents are first-class citizens that require purpose-built observability:

- [ ] **Every agent action produces a span** with:
  - `agent.name`, `agent.role`, `agent.layer` (steering/strategy/orchestration/execution/quality)
  - `agent.mission_id` — links to the mission being executed
  - `agent.tool` — the tool being invoked
  - `agent.model` — LLM model used (if applicable)
  - `agent.token_usage.input`, `agent.token_usage.output` — token counts
  - `agent.decision` — the decision made (summarized)
- [ ] **Agent error traces** capture:
  - Tool call failures (with error details)
  - Policy violations detected
  - Escalation triggers (why the agent couldn't proceed autonomously)
  - Retry attempts and outcomes
- [ ] **Agent fleet dashboard** exists per division showing:
  - Active agents and their current missions
  - Success/failure rates by agent type
  - Token consumption trends
  - Mean time to complete missions
  - Escalation frequency and reasons
- [ ] **Cost attribution:** agent token/compute costs are attributable to specific missions and divisions

---

## Git Events as Observability Source

Every Git operation in this repository is a significant lifecycle event. The observability integration MUST receive events for every meaningful Git change via webhooks.

### Required Git Event Coverage

- [ ] **PR created** → event: `governance.pr.opened` with branch name, author agent, mission ID
- [ ] **PR updated** (new commits pushed) → event: `governance.pr.updated`
- [ ] **PR review requested / completed** → event: `governance.pr.review`
- [ ] **PR merged** → event: `governance.pr.merged` with merge SHA, approver(s), time-to-merge
- [ ] **PR rejected / closed without merge** → event: `governance.pr.rejected` with reason (if documented)
- [ ] **Tag / release created** → event: `release.tagged`
- [ ] **Branch created** → event: `governance.branch.created` (correlate to fleet config or mission)

### What Git Webhooks Enable

| Capability | Explanation |
|-----------|-------------|
| **Cycle time tracking** | Time from signal filed (first commit on branch) to PR merged = end-to-end mission latency |
| **Compliance evidence** | Every approval in Git is an observable event with timestamp and approver identity |
| **Change impact correlation** | Observability platform correlates production behavior changes to specific PR merges |
| **Automated signal generation** | Deployment frequency drops, review time spikes → auto-filed signals in `work/signals/` |
| **Audit trail completeness** | Git + telemetry together provide the full audit trail: what was decided (Git) + what actually happened (telemetry) |

### Configuration

Git webhooks are configured at the repository or organization level to push events to the OTLP endpoint or webhook ingest of the registered observability integration. See `org/integrations/categories/observability.md` for configuration patterns.

---

## Verification Gates

Observability is checked at multiple points in the lifecycle:

### At Component Onboarding
- All observability items in the component onboarding checklist completed
- Telemetry data visible in {{OBSERVABILITY_TOOL}} within 5 minutes of first deployment

### At Build Time (PR Review)
- New endpoints have instrumentation (traces + RED metrics)
- New error paths produce structured logs with trace correlation
- New external calls are wrapped in spans
- Agent workflows include observability spans for tool calls and decisions

### At Ship Time (Release Contract)
- SLOs defined and configured
- Dashboard created and linked in catalog
- Alerting configured with runbooks
- Post-deployment monitoring plan in the release contract
- Observability section in release contract is fully populated

### At Operate Time (Ongoing)
- Health target compliance reviewed weekly
- Alert quality reviewed monthly (tune or remove noisy alerts)
- Dashboard accuracy verified after every deployment
- Observability coverage gaps surfaced as signals in `work/signals/`

---

## Exceptions

- **Prototype/experimental components** may defer SLO definition and alerting, but MUST have basic instrumentation (traces + logs) from day one
- **Batch jobs running < 1x/day** may use simplified metrics (success/failure + duration only)
- **Libraries** (non-deployed code) are exempt from runtime observability but must support instrumentation when consumed by services
- **Third-party components** where instrumentation is not possible must have synthetic monitoring configured as a substitute

**No exception exists for shipping without any observability.** If a component cannot be instrumented, it cannot go to production.

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Instrumentation | At least one source active, telemetry verified | No instrumentation or telemetry not flowing |
| Traces | End-to-end traces with W3C context propagation | Missing traces or broken context propagation |
| Metrics | RED metrics on all endpoints | Missing rate, error, or duration metrics |
| Logs | Structured JSON logs with trace ID correlation | Unstructured logs or missing trace correlation |
| SLOs | Defined, configured, burn rate alerts active | No SLOs or no alerting |
| Dashboards | Service health dashboard created and linked | No dashboard or not linked in catalog |
| Alerting | All alerts have documented runbook actions | Alerts without runbooks or no alerting |
| Agent observability | Spans for tool calls, decisions, token usage | Agent actions not traced (if agent component) |
| Git event coverage | Webhook configured, PR lifecycle events flowing | No git webhooks or events not reaching observability integration |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
