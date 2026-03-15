# NIST AI RMF — Quantitative Measurement Guide

> **Closes gap:** Standardized quantitative measurement scaffolding for NIST AI RMF MEASURE 1-4
> **Framework:** NIST AI 100-1 — AI RMF 1.0
> **Severity:** High — the framework now defines the measurement model, but adopters still need live telemetry and completed reports
> **Related issue:** [#128](https://github.com/wlfghdr/agentic-enterprise/issues/128)
> **Related compliance doc:** [NIST AI RMF Compliance Reference](../nist-ai-rmf.md)
> **Companion resources:** [NIST AI RMF MEASURE Dashboard Template](../templates/_TEMPLATE-nist-ai-rmf-measure-dashboard.md) and [NIST AI RMF Measurement Report Template](../templates/_TEMPLATE-nist-ai-rmf-measure-report.md)

---

## 1. Gap Summary

The Agentic Enterprise framework already had the policy ingredients needed for NIST AI RMF measurement:

- observability requirements in the [Observability Policy](../../../org/4-quality/policies/observability.md)
- AI-specific trustworthiness and fairness expectations in the [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md)
- continuous risk indicators in the [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
- behavioral evaluation metrics in the [Agent Eval Policy](../../../org/4-quality/policies/agent-eval.md)
- canonical telemetry fields in the [OTel Telemetry Contract](../../otel-contract.md)

What was missing was the **operational wrapper** that turns those ingredients into a repeatable NIST AI RMF MEASURE programme:

1. a standard metric catalog aligned to MEASURE 1-4
2. a baseline-establishment method
3. a reusable dashboard structure for AI risk quantification
4. a reusable report structure showing expected measurement outputs

This guide closes that framework gap. It does **not** create real measurements by itself. Adopters still need live telemetry, evaluation data, and operational ownership.

---

## 2. What the Framework Standardizes vs. What Adopters Must Populate

| Topic | Framework Now Provides | Adopter Must Still Provide |
|-------|------------------------|----------------------------|
| MEASURE metric structure | Standard metric families, formulas, ownership guidance, baseline method | Actual metric values from the live deployment |
| Dashboard design | Reusable panel structure, filters, threshold fields, review workflow | Real dashboard implementation in the chosen observability platform |
| Measurement reports | Standard reporting sections and output expectations | Completed periodic reports with real results and actions |
| Telemetry mapping | Mapping from OTel spans/metrics/events to NIST AI RMF MEASURE categories | Instrumented systems that actually emit the required data |
| Trustworthiness evaluation inputs | Hooks to fairness, eval, robustness, and override metrics | Deployment-specific datasets, thresholds, and quality-review decisions |

This division matters. The framework can make measurement **structured** and **consistent**. Only a running deployment can make it **populated**.

---

## 3. Standard Metric Catalog by NIST AI RMF MEASURE Category

Use the metric families below as the default starting set for AI systems deployed on this framework. If a deployment needs more metrics, extend this set. Do not reduce it without documented rationale.

### 3.1 MEASURE 1 — Metrics to Assess AI Risks

| Metric | Why It Matters | Primary Source | Baseline Method | Typical Threshold |
|--------|----------------|----------------|-----------------|------------------|
| **Agent escalation rate** | Rising escalations can indicate poor scope fit, uncertainty, or control weakness | `governance.decision` events where decision=`escalate` | 30-day rolling baseline by agent type and mission type | Investigate if rate rises above baseline by >25% |
| **Tool call failure rate** | Quantifies operational fragility and integration reliability | `tool.execute` spans with error status | 30-day rolling baseline by tool and environment | Alert if failure rate exceeds configured KRI threshold |
| **Human override / rejection rate** | Measures whether human oversight is catching too many unsafe or poor decisions | `governance.decision` events where decision=`reject` | Weekly trend plus 30-day baseline | Investigate sustained upward trend over 4 weeks |
| **Hallucination / correction rate** | Measures output reliability and factual-quality failures | `quality.evaluate` results, accuracy-focused eval findings, corrective-action records | Baseline by agent type and evaluation category | Escalate when rate breaches the configured hallucination threshold or local threshold |
| **Token cost variance** | Quantifies efficiency drift and runaway cost patterns | `gen_ai.client.token.usage` histograms aggregated by mission, agent, model | 30-day rolling baseline by mission type | Alert if variance exceeds budget or >3x expected range |

### 3.2 MEASURE 2 — Trustworthiness Evaluation

| Metric | Why It Matters | Primary Source | Baseline Method | Typical Threshold |
|--------|----------------|----------------|-----------------|------------------|
| **Eval pass rate** | Quantifies behavioral correctness and policy compliance | `eval.suite.run` results or equivalent structured eval output | Baseline by agent type and eval category | Alert if pass rate drops below 95% or local threshold |
| **Regression count** | Quantifies trustworthiness degradation over time | `eval.regression.detected` events | Rolling weekly and monthly count | Any new regression is high signal; repeated regressions require root-cause review |
| **Fairness ratio / bias metric** | Quantifies disparate impact or group skew where applicable | Fairness audit outputs referenced by the AI Governance Policy | Baseline per system and affected group | Use deployment-approved fairness thresholds; four-fifths rule is a common starting point |
| **Adversarial robustness pass rate** | Quantifies resistance to manipulative or hostile inputs | Adversarial eval results and red-team outputs | Baseline by system and test suite version | Tier 1 systems should treat failed core cases as blocking |
| **Explanation coverage rate** | Measures whether required justifications and traceability are actually present | `governance.decision` events, trace coverage audits, report sampling | Monthly percentage of reviewed outputs with required rationale | Alert if coverage falls below local minimum |

### 3.3 MEASURE 3 — Tracking Emergent Risks

| Metric | Why It Matters | Primary Source | Baseline Method | Typical Threshold |
|--------|----------------|----------------|-----------------|------------------|
| **Anomaly alert rate** | Detects unusual runtime behavior before incidents scale | Observability anomaly detection and automated signals | 30-day rolling baseline by agent or workflow | Investigate spikes above seasonal baseline |
| **Drift signal count** | Tracks behavior or outcome drift that may not appear as outright failure yet | Scheduled eval deltas, quality trends, output-distribution monitoring | Weekly trend versus prior quarter | Investigate any sustained upward trend |
| **Risk threshold breach count** | Quantifies how often AI risk is crossing defined tolerances | `risk.threshold.breach` events | Monthly trend and threshold-breach history | Repeated breaches trigger risk register review |
| **Prompt-injection detection rate** | Measures hostile input pressure and defense effectiveness | Agent security telemetry and policy violation events | Rolling baseline by external surface | Any increase merits review; sustained attempts may require stronger controls |
| **Model or provider incident correlation** | Tracks whether changes in provider/model behavior align with measurement degradation | Change records, model-version tags, eval and runtime metrics | Compare pre/post-change windows | Any material post-change drop should trigger change review |

### 3.4 MEASURE 4 — Feedback and Continuous Evaluation

| Metric | Why It Matters | Primary Source | Baseline Method | Typical Threshold |
|--------|----------------|----------------|-----------------|------------------|
| **Signal closure latency** | Measures whether feedback actually turns into action | `work/signals/` lifecycle or issue cycle-time data | 90-day median by signal type | Escalate long-lived open signals affecting AI risk |
| **Corrective-action completion rate** | Measures remediation follow-through | Report action trackers, issue status, retest status | Monthly completion rate by owner/team | Alert if overdue actions accumulate |
| **Incident recurrence rate** | Measures whether lessons learned are sticking | Retrospectives, incident taxonomy, signal links | Quarterly trend by root-cause category | Repeated recurrence indicates weak risk treatment |
| **User or operator feedback volume** | Quantifies real-world feedback intake and detects silent failure modes | Support, review queues, feedback forms, quality-review notes | Baseline by channel and AI system | Investigate both sharp spikes and suspicious drops |
| **Measurement data completeness** | Ensures the dashboard and report are trustworthy | Dashboard data-quality checks, missing telemetry counts, stale panel detection | Daily completeness check | Treat stale or missing data as a measurement failure |

---

## 4. OTel and Framework Mapping

This table provides the canonical mapping from framework telemetry and governed artifacts into the NIST AI RMF MEASURE function.

| NIST AI RMF Area | Metric / Signal | OTel / Framework Source | Primary Artifact |
|------------------|-----------------|-------------------------|------------------|
| **MEASURE 1** | Token cost variance | `gen_ai.client.token.usage` metric | Dashboard panel + periodic report |
| **MEASURE 1** | Inference latency trend | `gen_ai.client.operation.duration` metric | Dashboard panel + SLO review |
| **MEASURE 1** | Tool call failure rate | `tool.execute` spans with `error.type` | Dashboard panel + incident review |
| **MEASURE 1** | Escalation / override rate | `governance.decision` span events | Dashboard panel + measurement report |
| **MEASURE 2** | Eval pass rate | `eval.suite.run` and `eval.case.run` spans or equivalent eval output | Trustworthiness section of the report |
| **MEASURE 2** | Regression count | `eval.regression.detected` events | Trustworthiness section + action tracker |
| **MEASURE 2** | Fairness and robustness results | AI governance audit outputs and red-team results | Measurement report appendix |
| **MEASURE 3** | Risk threshold breach count | `risk.threshold.breach` span events | Emergent-risk panel and report |
| **MEASURE 3** | Anomaly and drift signals | Observability anomaly alerts, scheduled eval deltas, automated signals | Emergent-risk section |
| **MEASURE 4** | Signal closure latency | Signal issue/file lifecycle data | Feedback section + operational review |
| **MEASURE 4** | Corrective-action completion rate | Report follow-up tracker, issues, retests | Feedback section + action register |

### 4.1 Important Constraint

Not every MEASURE metric is a native OTel metric today. Some are derived from:

- structured eval outputs
- governed Git artifacts such as signals, issues, and remediation trackers
- deployment-specific fairness or robustness datasets

That is acceptable. NIST AI RMF cares that measurement is **defined, repeatable, and actionable**, not that every value originates from the same telemetry primitive.

---

## 5. Baseline Establishment Method

Measurement without baseline quickly becomes anecdotal. Use this baseline process for every in-scope AI system or agent type.

### 5.1 Step 1 — Define the Measurement Scope

For each dashboard or report, explicitly record:

- which AI systems, agent types, or workflows are in scope
- which NIST AI RMF MEASURE subcategories the metric set supports
- which environments are included (`production`, `staging`, or both)
- which segmentation dimensions matter (`agent type`, `model`, `provider`, `mission type`, `risk tier`)

### 5.2 Step 2 — Select the Initial Metric Set

At minimum include:

- one operational-risk metric
- one trustworthiness metric
- one emergent-risk metric
- one feedback / continuous-evaluation metric

High-risk deployments should include multiple metrics in each category.

### 5.3 Step 3 — Capture the Initial Baseline Window

Recommended default:

- **30 days** of production data for always-on systems
- **10 completed cycles** for lower-volume workflows
- **three scheduled eval runs** for systems where trustworthiness is measured mainly through evaluations

If a deployment does not yet have enough data, mark the baseline as provisional and refresh it at the next reporting cycle.

### 5.4 Step 4 — Set Thresholds and Owners

For every metric, define:

- named owner
- baseline window
- alert threshold or trend trigger
- expected review cadence
- required action when breached

Where a policy already defines a threshold or KRI, use that as the starting point before inventing a new number.

### 5.5 Step 5 — Rebaseline Carefully

Rebaseline when:

- model/provider changes materially affect behavior
- mission mix changes enough to invalidate the old comparison
- the system moves from pilot to production
- a measurement definition or query changes

Do not silently overwrite baselines. Record why the baseline changed and when.

---

## 6. Dashboard Design Guidance

Use the [dashboard template](../templates/_TEMPLATE-nist-ai-rmf-measure-dashboard.md) to define the measurement surface before building it in the observability tool.

The default dashboard should include four zones:

1. **Operational risk** — latency, token usage, tool failure rate, escalation/override rate
2. **Trustworthiness** — eval pass rate, regression count, fairness or robustness results
3. **Emergent risk** — anomalies, drift signals, threshold breaches, provider/model change overlays
4. **Feedback and remediation** — signal backlog, corrective-action closure, incident recurrence, data completeness

### 6.1 Minimum Dashboard Filters

- environment
- AI system or agent type
- model / provider
- mission type or workflow
- reporting period

### 6.2 Minimum Dashboard Behaviors

- show current value **and** baseline
- highlight threshold breaches visibly
- link each alert or breach to an owner and next action
- indicate data freshness and completeness

If a panel cannot answer "what do we do when this moves?", it is not a good MEASURE panel yet.

---

## 7. Measurement Reports

Use the [measurement report template](../templates/_TEMPLATE-nist-ai-rmf-measure-report.md) for monthly or quarterly reporting. The report turns dashboards into governance action.

### 7.1 Minimum Report Sections

- scope and systems covered
- baseline period and methodology
- metric results with comparisons to baseline
- trustworthiness findings
- emergent risk findings
- corrective actions and ownership
- next-cycle changes

### 7.2 Example Output Excerpt

The example below illustrates the level of specificity the report should reach:

| Metric | Current Period | Baseline | Change | Interpretation | Action |
|--------|----------------|----------|--------|----------------|--------|
| Escalation rate | 18% | 11% | +7pp | Significant rise after model change for two execution agents | Review prompts and recent model/version change |
| Eval pass rate | 93% | 97% | -4pp | Drift concentrated in adversarial and decision-quality suites | Open corrective action, expand regression set |
| Tool failure rate | 2.3% | 0.7% | +1.6pp | Mostly isolated to one vendor API | Investigate provider health and fallback behavior |
| Corrective-action completion | 62% | 85% | -23pp | Remediation backlog growing | Reassign overdue actions and escalate in risk review |

Good MEASURE reports explain both the number **and** the governance consequence.

---

## 8. Verification Checklist

- [ ] A defined metric catalog exists for each in-scope AI system or agent family
- [ ] Every metric maps to at least one NIST AI RMF MEASURE subcategory
- [ ] Dashboard panels record source, baseline, threshold, owner, and review cadence
- [ ] Measurement reports compare current values to a documented baseline
- [ ] Data completeness and freshness are reviewed alongside the metrics themselves
- [ ] Trustworthiness metrics include eval, fairness, robustness, or explanation evidence where applicable
- [ ] Emergent-risk metrics include anomaly, drift, or threshold-breach tracking
- [ ] Feedback metrics include remediation or corrective-action follow-through
- [ ] Baseline changes are documented rather than silently overwritten

---

## References

- [NIST AI RMF Compliance Reference](../nist-ai-rmf.md)
- [OTel Telemetry Contract](../../otel-contract.md)
- [Observability Policy](../../../org/4-quality/policies/observability.md)
- [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md)
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
- [Agent Eval Policy](../../../org/4-quality/policies/agent-eval.md)
