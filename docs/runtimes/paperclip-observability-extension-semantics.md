# Paperclip-backed Agentic Enterprise: observability extension semantics

> **Status:** Draft operating contract
> **Purpose:** Define what the Agentic Enterprise overlay must preserve when Paperclip is the runtime substrate and observability signals need to become governed work.
> **Scope:** This document does not redefine the canonical telemetry schema in [docs/otel-contract.md](../otel-contract.md) or the observability policy in [org/4-quality/policies/observability.md](../../org/4-quality/policies/observability.md). It defines the **extension-layer semantics** that turn telemetry into enterprise actions.

---

## 1. Why this layer exists

If Paperclip owns runtime execution, task orchestration, approvals, plugin attachment, and company isolation, Agentic Enterprise should not duplicate that machinery.

The remaining enterprise value is semantic and governance-heavy:

- signals become governed work
- actions map to enterprise roles and escalation paths
- evidence is preserved for delivery, security, compliance, and quality review
- feedback loops determine whether runtime anomalies are actually resolved

This document defines that contract.

---

## 2. Operating principle

**Paperclip may observe and route. Agentic Enterprise decides what the signal means in enterprise terms.**

A Paperclip-backed deployment is conformant only if an observability signal can be answered with all of the following:

1. What happened
2. How severe and credible it is
3. Which role owns the response
4. Whether it creates governed work, only informs, or requires human approval
5. What evidence must exist before the signal can be considered resolved

If a plugin preserves raw telemetry but drops those semantics, the integration is incomplete.

---

## 3. Minimum signal model

Every observability-derived signal entering Agentic Enterprise MUST carry these fields, regardless of source system.

| Field | Requirement | Meaning |
|---|---|---|
| `signal.id` | Required | Stable identifier for dedupe and audit |
| `signal.type` | Required | One of: `delivery`, `reliability`, `security`, `quality`, `cost`, `compliance` |
| `signal.source` | Required | Tool, plugin, collector, SIEM, APM, CI, runtime, or derived governance pipeline |
| `signal.summary` | Required | Human-readable statement of the condition |
| `signal.severity` | Required | `low`, `medium`, `high`, `critical` |
| `signal.confidence` | Required | `low`, `medium`, `high` or numeric equivalent |
| `signal.detected_at` | Required | Detection timestamp |
| `signal.target.role` | Required | Owning enterprise role or division |
| `signal.expected_action` | Required | Inform, investigate, remediate, approve, escalate, or block |
| `signal.evidence` | Required | Links or references to trace/log/metric/PR/policy evidence |
| `signal.related.resource` | Recommended | Service, workflow, agent, repo, mission, or control |
| `signal.related.mission` | Recommended | Existing mission if already known |
| `signal.requires_human` | Required | Boolean flag derived from mapping rules |

### 3.1 Signal type requirements

| Type | Typical source | Target role | Expected action | Required evidence |
|---|---|---|---|---|
| `delivery` | CI/CD, deploy telemetry, PR flow analytics | delivery owner, release health agent, engineering lead | unblock, rollback, repair, or re-sequence release work | failed run, deployment event, impacted change set, recovery evidence |
| `reliability` | SLO burn, incident tooling, APM, OTel traces | service owner, incident response, platform ops | investigate, mitigate, open incident or follow-up mission | trace/metric evidence, user impact, time window, service scope |
| `security` | SIEM, runtime security, dependency/vuln scanning, IAM events | security lead, devsecops, incident commander | contain, escalate, request approval, or block release | detection evidence, asset scope, exploitability, remediation record |
| `quality` | eval pipelines, regression telemetry, customer-impact metrics | quality layer, product owner, engineering lead | diagnose, create correction work, or gate release | eval result, failing criteria, artifact version, before/after evidence |
| `cost` | billing telemetry, token spend, capacity metrics | budget owner, capacity-cost agent, platform owner | optimize, throttle, approve spend, or re-plan workload | cost delta, baseline, contributing component, expected savings |
| `compliance` | policy engines, audit checks, evidence-chain validation | compliance owner, quality lead, human approver | gather evidence, block release, approve exception, or remediate | violated control, missing evidence, retention/audit references |

### 3.2 Severity and confidence semantics

- **Severity** measures business or operational impact if the signal is true.
- **Confidence** measures how trustworthy the detection is.
- High severity with low confidence defaults to **human review or corroboration**, not blind automation.
- Low severity with high confidence may remain informational if no policy threshold is crossed.

---

## 4. Signal to mission/work mapping

This layer defines when observability becomes work.

| Condition | Required outcome |
|---|---|
| Repeated or threshold-breaching signal with clear owner | Create or update a mission/task |
| Security, compliance, or production reliability signal with material risk | Escalate to the owning role immediately |
| Action would change customer-facing behavior, spend, policy posture, or access | Request human approval before remediation |
| Signal is below threshold, transient, or already covered by active work | Attach evidence to the existing mission or keep informational |
| Signal cannot be attributed, deduped, or evidenced | Keep informational until enriched; do not auto-remediate |

### 4.1 Required mapping rules

An observability integration is conformant only if it can express these outcomes:

1. **Create issue/task** when the signal implies discrete follow-up work that can be owned and verified.
2. **Escalate to a role** when response time or authority matters more than task creation.
3. **Request human approval** when the action crosses governance boundaries.
4. **Remain informational only** when the signal adds context but should not create work by itself.

### 4.2 Governance triggers

Human approval is required when any of the following is true:

- production mitigation changes access, data handling, or policy enforcement
- a cost-control action materially degrades service or user experience
- a compliance signal implies an exception, waiver, or missing audit evidence
- a security action could disrupt customer operations or destroy evidence
- confidence is too low for safe autonomous remediation

---

## 5. Feedback semantics after agent action

Resolving a signal is not the same as acting on it. The extension layer MUST preserve the post-action feedback loop.

Every action taken from an observability signal MUST record:

1. **What changed**
   - code, config, workflow, threshold, routing, rollback, or exception state
2. **Did the signal clear**
   - fully cleared, partially improved, unchanged, or regressed
3. **Did risk go up or down**
   - explicit risk delta with rationale
4. **What evidence was produced**
   - traces, dashboards, PRs, approvals, test results, policy verdicts, or incident notes

### 5.1 Closure contract

A signal is only eligible for closure when:

- the implemented change is linked to the originating signal or mission
- post-change evidence exists
- the resulting risk posture is stated
- the responsible role or policy gate accepts the outcome

If the signal did not clear, the feedback loop MUST create follow-on work or escalate instead of silently resolving.

---

## 6. Plugin boundary

This is the practical boundary between Paperclip, plugins, and the Agentic Enterprise overlay.

| Layer | Owns | Must not own |
|---|---|---|
| **Paperclip core** | runtime execution, task state, approvals plumbing, company isolation, event transport, extension loading | enterprise-specific policy meaning of observability signals |
| **Plugin integrations** | source-specific ingestion, enrichment, normalization, dedupe hints, transport into runtime hooks or work queues | repository-specific governance policy or enterprise role semantics |
| **Agentic Enterprise extension semantics** | signal taxonomy, severity/confidence interpretation, role ownership, work-creation rules, approval triggers, feedback/closure semantics, evidence expectations | low-level telemetry collection or backend-specific ingest details |

### 6.1 Practical test

A future plugin author should be able to answer:

- Which fields must I provide so AE can classify the signal?
- Which thresholds or categories must preserve security, compliance, quality, cost, delivery, and reliability meaning?
- How does my plugin indicate whether the signal should create work, escalate, or stay informational?
- What evidence links must survive so AE can verify closure?

If those answers are missing, the plugin boundary is underspecified.

---

## 7. Relationship to existing Agentic Enterprise work

This contract intentionally builds on existing AE documents instead of restating them:

- [docs/otel-contract.md](../otel-contract.md) defines canonical telemetry shape
- [docs/observability/otel-architecture.md](../observability/otel-architecture.md) defines the telemetry feedback loop
- [org/4-quality/policies/observability.md](../../org/4-quality/policies/observability.md) defines observability as a ship gate
- issue [#170](https://github.com/wlfghdr/agentic-enterprise/issues/170) covers evidence-chain validation
- issue [#188](https://github.com/wlfghdr/agentic-enterprise/issues/188) covers outcome-oriented observability quality metrics
- issue [#233](https://github.com/wlfghdr/agentic-enterprise/issues/233) covers delivery governance and stage gates
- issue [#243](https://github.com/wlfghdr/agentic-enterprise/issues/243) scopes AE as the semantic and governance overlay over Paperclip runtime capabilities

This document adds the missing piece: **how a Paperclip-backed runtime must preserve observability meaning when signals become enterprise work.**

---

## 8. Conformance checklist for a Paperclip observability extension

A Paperclip observability extension is conformant only if it preserves all of the following:

- [ ] supports the six required signal types
- [ ] captures source, severity, confidence, target role, expected action, and evidence
- [ ] can distinguish informational signals from work-creating signals
- [ ] can trigger escalation and human approval paths when governance rules require them
- [ ] can attach post-action evidence and risk-change outcomes
- [ ] can keep closure state tied to the original signal rather than only the remediation action
- [ ] does not move enterprise governance meaning into Paperclip core or hide it inside source-specific plugin logic

---

## 9. Long-term implication

If Paperclip matures into the runtime substrate, Agentic Enterprise should remain the **enterprise semantics and governance overlay** for observability, not a competing runtime.

That means the durability requirement is not "can Paperclip ingest telemetry?"

It is: **can a Paperclip-backed system preserve the meaning, ownership, evidence, and closure semantics of enterprise observability signals?**
