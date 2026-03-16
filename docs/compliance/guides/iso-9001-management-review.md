<!-- placeholder-ok -->
# ISO 9001 — Management Review Guide

> **Implements:** Management review records and cadence (clause 9.3)
> **Standard:** ISO 9001:2015 — Quality Management Systems
> **Severity:** Medium — required for certification and recurring executive control
> **Related compliance doc:** [ISO 9001 Compliance Reference](../iso-9001.md)

---

## 1. Purpose

ISO 9001 clause 9.3 requires top management to review the QMS at planned intervals.
The framework already produces many of the needed inputs through signals, outcome
reports, policy evaluations, incident reviews, and observability dashboards. This
guide turns those existing artifacts into a formal management review record that an
auditor can inspect.

Use this guide when you need to prove that leadership is not only receiving signals,
but also reviewing QMS performance, deciding actions, and tracking follow-through.

---

## 2. Required Inputs (Clause 9.3.2)

Every management review should explicitly cover:

| Input | ISO 9001 Ref | Typical Framework Sources |
|-------|--------------|---------------------------|
| Status of prior actions | 9.3.2 a) | Previous management review action log, mission follow-ups |
| Changes in internal/external issues | 9.3.2 b) | Steering digests, risk signals, compliance updates |
| Information on QMS performance | 9.3.2 c) | Outcome reports, incident metrics, quality evaluations, SLO dashboards |
| Adequacy of resources | 9.3.2 d) | Fleet performance, staffing plans, budget/risk reviews |
| Effectiveness of actions for risks/opportunities | 9.3.2 e) | Risk register updates, mitigation evidence, retrospectives |
| Opportunities for improvement | 9.3.2 f) | Signals, postmortems, customer feedback themes |

For software and agentic operating models, the following sub-inputs usually need
explicit treatment inside the performance section:

- customer satisfaction and complaint themes
- process performance and cycle time
- conformity / nonconformity trends
- audit results
- supplier and external provider performance

---

## 3. Recommended Cadence

Recommended baseline for adopters:

| Deployment Maturity | Cadence | Notes |
|---------------------|---------|-------|
| Early adoption / pre-certification | Monthly | Faster loop while processes are still stabilizing |
| Operating production deployment | Quarterly | Common default for management-system governance |
| Heavily regulated or high-change environment | Monthly + ad hoc | Add triggered reviews after major incidents or audit findings |

The important control is not the exact interval. It is that the cadence is defined,
followed, and evidenced.

---

## 4. Management Review Record Template

Instantiate this as a governed artifact such as
`docs/compliance/qms-management-review-2026-q2.md` or an equivalent controlled record.

```markdown
# QMS Management Review

> **Review period:** {{YYYY-QX or date range}}
> **Review date:** {{YYYY-MM-DD}}
> **Review chair:** {{TOP_MANAGEMENT_ROLE}}
> **Recorder:** {{OWNER}}
> **Scope reference:** {{LINK_TO_QMS_SCOPE}}

## 1. Attendees

| Name | Role | Function represented |
|------|------|----------------------|
| {{NAME}} | {{ROLE}} | {{FUNCTION}} |

## 2. Status of Prior Actions

| Action ID | Prior decision | Owner | Due date | Current status | Evidence |
|-----------|----------------|-------|----------|----------------|----------|

## 3. Changes in Context

### External issues
- {{Regulatory, customer, supplier, market, technology changes}}

### Internal issues
- {{Org changes, tooling changes, operating model changes, incident trends}}

## 4. QMS Performance Review

### Customer satisfaction
- {{Survey trends, complaint themes, renewal/retention signals, escalations}}

### Process performance and conformity
- {{Cycle time, delivery quality, nonconformities, quality verdict trends}}

### Audit and evaluation results
- {{Internal audits, external audits, policy evaluation trends}}

### Supplier / external provider performance
- {{Vendor scorecards, SLA and quality exceptions, reassessment triggers}}

## 5. Resource Adequacy

- {{People, budget, platform, observability, training, supplier capacity}}

## 6. Risks, Opportunities, and Corrective Actions

- {{Effectiveness of actions taken}}
- {{New risks or opportunities}}

## 7. Decisions and Actions

| ID | Decision / action | Owner | Due date | Type |
|----|-------------------|-------|----------|------|
| {{MR-001}} | {{ACTION}} | {{OWNER}} | {{DATE}} | improvement / resource / policy / risk |

## 8. Outputs Summary

- Improvement opportunities:
- Required QMS changes:
- Resource needs:
- Escalations / exceptions:
```

---

## 5. Evidence Mapping

| Review Topic | Preferred Evidence |
|--------------|--------------------|
| Customer satisfaction | Survey summaries, complaint logs, support metrics, renewal insights |
| Process performance | Outcome reports, cycle-time dashboards, quality verdict trends |
| Nonconformities | Postmortems, incident records, audit findings, corrective-action tracker |
| Supplier performance | Vendor review notes, SLA data, supplier-quality scorecards |
| Resource adequacy | Headcount plans, fleet dashboards, platform capacity reviews |
| Risk effectiveness | Risk register deltas, mitigation evidence, governance decisions |

---

## 6. Verification Checklist

- [ ] Review cadence is defined and actually followed
- [ ] Required clause 9.3.2 inputs are visible in the record
- [ ] Decisions and actions have named owners and due dates
- [ ] Prior actions are explicitly revisited in the next review
- [ ] Customer and supplier performance are treated as distinct inputs, not implied
- [ ] The record is version-controlled or otherwise controlled as documented information
