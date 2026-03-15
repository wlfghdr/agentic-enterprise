# NIST AI RMF Measurement Report

> **Template version:** 1.0
> **Last updated:** 2026-03-15
> **Framework:** NIST AI 100-1 — AI RMF 1.0
> **Purpose:** Provide a reusable report structure for periodic quantitative AI-risk measurement aligned to NIST AI RMF MEASURE 1-4

---

## Report Metadata

| Field | Value |
|-------|-------|
| Report ID | NIST-AIRMF-MEASURE-REPORT-001 |
| Version | {{VERSION}} |
| Organization | {{ORGANIZATION_NAME}} |
| Reporting period | {{REPORTING_PERIOD}} |
| Prepared by | {{PREPARER}} |
| Reviewed by | {{REVIEWER}} |
| Approved by | {{APPROVER}} |
| Related dashboard | [NIST AI RMF MEASURE Dashboard Specification](_TEMPLATE-nist-ai-rmf-measure-dashboard.md) |

## 1. Scope

### 1.1 AI Systems / Agent Types Covered

- {{SYSTEM_OR_AGENT_1}}
- {{SYSTEM_OR_AGENT_2}}

### 1.2 Environments Covered

- {{ENVIRONMENT_1}}
- {{ENVIRONMENT_2}}

### 1.3 NIST AI RMF Coverage

- [ ] MEASURE 1
- [ ] MEASURE 2
- [ ] MEASURE 3
- [ ] MEASURE 4

## 2. Executive Summary

### Overall measurement posture

{{OVERALL_POSTURE_SUMMARY}}

### Top findings

1. {{TOP_FINDING_1}}
2. {{TOP_FINDING_2}}
3. {{TOP_FINDING_3}}

### Immediate actions

- {{IMMEDIATE_ACTION_1}}
- {{IMMEDIATE_ACTION_2}}

## 3. Baseline and Methodology

| Field | Value |
|-------|-------|
| Baseline window | {{BASELINE_WINDOW}} |
| Baseline source | {{BASELINE_SOURCE}} |
| Measurement method | {{MEASUREMENT_METHOD}} |
| Data completeness status | {{DATA_COMPLETENESS_STATUS}} |
| Known limitations | {{KNOWN_LIMITATIONS}} |

## 4. Quantitative Results

| Metric | MEASURE Category | Current Period | Baseline | Change | Status | Interpretation | Action Reference |
|--------|------------------|----------------|----------|--------|--------|----------------|------------------|
| {{METRIC_1}} | {{MEASURE_CATEGORY}} | {{CURRENT}} | {{BASELINE}} | {{DELTA}} | {{NORMAL / WATCH / BREACH}} | {{INTERPRETATION}} | {{ACTION_REF}} |
| {{METRIC_2}} | {{MEASURE_CATEGORY}} | {{CURRENT}} | {{BASELINE}} | {{DELTA}} | {{STATUS}} | {{INTERPRETATION}} | {{ACTION_REF}} |
| {{METRIC_3}} | {{MEASURE_CATEGORY}} | {{CURRENT}} | {{BASELINE}} | {{DELTA}} | {{STATUS}} | {{INTERPRETATION}} | {{ACTION_REF}} |

## 5. Trustworthiness Findings

### Eval and regression summary

{{EVAL_AND_REGRESSION_SUMMARY}}

### Fairness / robustness / explainability findings

{{TRUSTWORTHINESS_FINDINGS}}

## 6. Emergent Risk Findings

### Anomalies, drift, and threshold breaches

{{EMERGENT_RISK_SUMMARY}}

### Significant changes since the last report

- {{CHANGE_1}}
- {{CHANGE_2}}

## 7. Feedback and Remediation

| Action / Signal | Owner | Due Date | Status | Evidence / Tracking Reference |
|-----------------|-------|----------|--------|-------------------------------|
| {{ACTION_1}} | {{OWNER}} | {{DATE}} | {{STATUS}} | {{REF}} |
| {{ACTION_2}} | {{OWNER}} | {{DATE}} | {{STATUS}} | {{REF}} |

### Feedback themes

{{FEEDBACK_THEMES}}

## 8. Next-Cycle Changes

- {{NEXT_CYCLE_CHANGE_1}}
- {{NEXT_CYCLE_CHANGE_2}}

## 9. Appendix — Evidence and Data Quality

| Evidence Item | Location / Reference | Notes |
|---------------|----------------------|-------|
| {{EVIDENCE_1}} | {{LOCATION}} | {{NOTES}} |
| {{EVIDENCE_2}} | {{LOCATION}} | {{NOTES}} |

| Data Quality Check | Result | Notes |
|--------------------|--------|-------|
| {{CHECK_1}} | {{PASS_FAIL}} | {{NOTES}} |
| {{CHECK_2}} | {{PASS_FAIL}} | {{NOTES}} |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial measurement report |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-15 | Initial reporting template for periodic NIST AI RMF MEASURE metrics, findings, and corrective actions |
