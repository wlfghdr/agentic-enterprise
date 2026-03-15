# NIST AI RMF MEASURE Dashboard Specification

> **Template version:** 1.0
> **Last updated:** 2026-03-15
> **Framework:** NIST AI 100-1 — AI RMF 1.0
> **Purpose:** Define a reusable dashboard specification for quantitative AI-risk measurement aligned to NIST AI RMF MEASURE 1-4

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | NIST-AIRMF-DASH-001 |
| Version | {{VERSION}} |
| Dashboard Name | {{DASHBOARD_NAME}} |
| Organization | {{ORGANIZATION_NAME}} |
| Owner | {{OWNER}} |
| Review Cadence | Monthly / Quarterly |
| Reporting Period Default | {{REPORTING_PERIOD_DEFAULT}} |
| Related | [NIST AI RMF Measurement Report Template](_TEMPLATE-nist-ai-rmf-measure-report.md) |

## 1. Scope

### 1.1 AI Systems / Agent Types in Scope

- {{SYSTEM_OR_AGENT_1}}
- {{SYSTEM_OR_AGENT_2}}

### 1.2 NIST AI RMF MEASURE Coverage

- [ ] MEASURE 1 — metrics to assess AI risks
- [ ] MEASURE 2 — trustworthiness evaluation
- [ ] MEASURE 3 — emergent risk tracking
- [ ] MEASURE 4 — feedback and continuous evaluation

### 1.3 Environments Included

- {{ENVIRONMENT_1}}
- {{ENVIRONMENT_2}}

## 2. Baseline Definition

| Field | Value |
|-------|-------|
| Baseline window | {{BASELINE_WINDOW}} |
| Baseline start | {{BASELINE_START}} |
| Baseline end | {{BASELINE_END}} |
| Baseline rationale | {{BASELINE_RATIONALE}} |
| Rebaseline trigger | {{REBASELINE_TRIGGER}} |

## 3. Required Filters

| Filter | Values / Notes |
|--------|----------------|
| Environment | {{ENV_FILTER_VALUES}} |
| AI system / agent type | {{SYSTEM_FILTER_VALUES}} |
| Model / provider | {{MODEL_FILTER_VALUES}} |
| Mission / workflow | {{MISSION_FILTER_VALUES}} |
| Time period | {{TIME_FILTER_VALUES}} |

## 4. Dashboard Panels

| Panel ID | MEASURE Category | Metric / Question | Source Query or Telemetry | Baseline | Threshold / Trigger | Visualization | Owner |
|----------|------------------|-------------------|---------------------------|----------|---------------------|--------------|-------|
| P-01 | MEASURE 1 | Escalation rate by agent type | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-02 | MEASURE 1 | Tool failure rate by tool and environment | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-03 | MEASURE 1 | Token usage / cost variance by mission type | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-04 | MEASURE 2 | Eval pass rate trend | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-05 | MEASURE 2 | Regression count and category breakdown | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-06 | MEASURE 2 | Fairness / robustness result summary | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-07 | MEASURE 3 | Risk threshold breaches over time | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-08 | MEASURE 3 | Anomaly / drift signal trend | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-09 | MEASURE 4 | Corrective-action completion rate | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |
| P-10 | MEASURE 4 | Measurement data completeness / freshness | {{QUERY_OR_REF}} | {{BASELINE}} | {{THRESHOLD}} | {{CHART_TYPE}} | {{OWNER}} |

## 5. Alert and Review Rules

| Rule ID | Trigger | Severity | Notification Path | Required Action | Runbook / Tracking Reference |
|---------|---------|----------|-------------------|-----------------|------------------------------|
| A-01 | {{TRIGGER}} | {{SEVERITY}} | {{ROUTE}} | {{ACTION}} | {{RUNBOOK_OR_ISSUE}} |
| A-02 | {{TRIGGER}} | {{SEVERITY}} | {{ROUTE}} | {{ACTION}} | {{RUNBOOK_OR_ISSUE}} |

## 6. Data Quality Checks

| Check | Method | Frequency | Owner |
|-------|--------|-----------|-------|
| Panel freshness | {{METHOD}} | {{FREQUENCY}} | {{OWNER}} |
| Missing telemetry | {{METHOD}} | {{FREQUENCY}} | {{OWNER}} |
| Baseline integrity | {{METHOD}} | {{FREQUENCY}} | {{OWNER}} |
| Segmentation correctness | {{METHOD}} | {{FREQUENCY}} | {{OWNER}} |

## 7. Access and Governance

| Topic | Requirement |
|-------|-------------|
| Dashboard viewers | {{VIEWER_GROUPS}} |
| Editors | {{EDITOR_GROUPS}} |
| Sensitive content handling | {{SENSITIVE_DATA_RULES}} |
| Review meeting cadence | {{MEETING_CADENCE}} |
| Escalation owner | {{ESCALATION_OWNER}} |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial MEASURE dashboard specification |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-15 | Initial dashboard specification template for NIST AI RMF MEASURE quantitative metrics, thresholds, and review workflow |
