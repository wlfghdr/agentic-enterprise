<!-- placeholder-ok -->
# ISO 9001 — Customer Satisfaction Measurement Guide

> **Implements:** Monitoring customer perceptions (clause 9.1.2)
> **Standard:** ISO 9001:2015 — Quality Management Systems
> **Severity:** Medium — required where products or services reach real customers
> **Related compliance doc:** [ISO 9001 Compliance Reference](../iso-9001.md)

---

## 1. Purpose

ISO 9001 requires the organization to monitor customer perceptions of whether
customer requirements have been fulfilled. In the framework, telemetry and
outcome reports provide useful signals, but they are not enough on their own.
This guide defines a practical customer-satisfaction measurement system that
combines direct feedback with operational evidence.

---

## 2. Measurement Principles

Use a blend of direct and indirect signals.

| Signal Type | Examples | Why it matters |
|-------------|----------|----------------|
| Direct perception | CSAT, NPS, interviews, complaint themes, customer review notes | Best evidence of customer perception |
| Indirect experience | Renewal/churn, support escalation rate, onboarding friction, SLA misses | Useful operational context |
| Product behavior | Feature adoption, failed workflow rate, latency or reliability issues | Shows service quality, but not sentiment by itself |

Do not treat product telemetry alone as customer satisfaction. It is supporting
evidence, not the full control.

---

## 3. Measurement System Template

Instantiate a controlled record such as `docs/compliance/customer-satisfaction-programme.md`.

```markdown
# Customer Satisfaction Measurement Programme

> **Owner:** {{CUSTOMER_OR_QUALITY_OWNER}}
> **In-scope products/services:** {{LIST}}
> **Review cadence:** {{monthly / quarterly}}

| Channel | Audience | Metric | Collection method | Cadence | Owner | Escalation trigger | Evidence retained |
|---------|----------|--------|-------------------|---------|-------|--------------------|------------------|
| Post-support CSAT | Active customers | CSAT % | Survey after ticket closure | Continuous | {{OWNER}} | < {{THRESHOLD}} | Survey export |
| Executive review | Strategic accounts | Relationship health | QBR notes / interviews | Quarterly | {{OWNER}} | Repeated negative theme | Review notes |
| Complaint analysis | All customers | Complaint recurrence | Support categorization | Monthly | {{OWNER}} | Trend up > {{THRESHOLD}} | Complaint log |
```

---

## 4. Recommended Minimum Signals

For most adopters, the minimum credible set is:

- one direct post-interaction satisfaction channel
- one periodic relationship or account-health review
- one complaint / escalation trend review
- one operational quality dashboard used as supporting context

If there are no real customers yet, document that explicitly and define the trigger
for introducing live customer-perception measurement.

---

## 5. Closed-Loop Expectations

Customer satisfaction data should feed:

- management review inputs
- quality objectives
- corrective actions and improvement missions
- supplier review when vendor performance contributes to customer harm

This is where customer satisfaction becomes a QMS control rather than a vanity metric.

---

## 6. Verification Checklist

- [ ] At least one direct customer-perception mechanism exists for each in-scope service
- [ ] Complaint themes are reviewed, not just logged
- [ ] Supporting operational metrics are linked but not used as the sole proxy
- [ ] Escalation thresholds are defined
- [ ] Results feed management review and improvement work
- [ ] If no live customer base exists yet, that temporary condition is explicitly documented
