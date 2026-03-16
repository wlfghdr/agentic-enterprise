<!-- placeholder-ok -->
# ISO 9001 — Internal Audit Programme Guide

> **Implements:** Internal audit programme (clause 9.2)
> **Standard:** ISO 9001:2015 — Quality Management Systems
> **Severity:** Medium — required for certification and systematic self-checking
> **Related compliance doc:** [ISO 9001 Compliance Reference](../iso-9001.md)

---

## 1. Purpose

The framework's Quality Layer performs continuous evaluation, but ISO 9001 still
expects a formal internal audit programme with scope, frequency, methods,
independence, reporting, and follow-up. This guide provides that wrapper so
adopters can convert continuous quality signals into an auditable QMS programme.

---

## 2. What The Audit Programme Must Define

| Requirement | ISO 9001 Ref | Meaning |
|-------------|--------------|---------|
| Planned intervals | 9.2.2 a) | Audit cadence is defined in advance |
| Importance of processes | 9.2.2 a) | Higher-risk or customer-critical processes receive more attention |
| Changes affecting the organization | 9.2.2 a) | Audit focus updates when context changes |
| Previous audit results | 9.2.2 a) | Recurring issues increase scrutiny |
| Criteria and scope | 9.2.2 b) | Each audit defines what is being tested |
| Auditor objectivity | 9.2.2 c) | Auditors do not audit their own work |
| Reporting | 9.2.2 d) | Results go to relevant management |
| Evidence retention | 9.2.2 e) | Programme and results are retained as documented information |

---

## 3. Audit Programme Template

Instantiate a controlled record such as `docs/compliance/qms-internal-audit-programme.md`.

```markdown
# QMS Internal Audit Programme

> **Owner:** {{AUDIT_PROGRAMME_OWNER}}
> **Effective date:** {{YYYY-MM-DD}}
> **Review cycle:** Annual
> **Linked scope:** {{LINK_TO_QMS_SCOPE}}

## 1. Objectives

- Verify conformity with the organization's QMS requirements
- Verify conformity with ISO 9001:2015
- Assess effective implementation and maintenance
- Provide input for improvement and management review

## 2. Annual Audit Plan

| Period | Focus area | Scope | Lead auditor | Method | Output |
|--------|------------|-------|--------------|--------|--------|
| {{Q1}} | {{PROCESS / FUNCTION}} | {{SCOPE}} | {{AUDITOR}} | Interview / document / sample / telemetry | Audit report |

## 3. Independence Rules

- Auditors do not audit their own operational area
- Quality Layer continuous evaluation informs but does not replace the audit
- External support may be used where independence is weak internally

## 4. Reporting and Follow-up

| Finding ID | Severity | Owner | Due date | Corrective action | Verified closed |
|------------|----------|-------|----------|-------------------|-----------------|
```

---

## 4. Suggested Audit Domains For This Framework

| Domain | Example Scope |
|--------|---------------|
| Governance and documented information | AGENTS, policies, CODEOWNERS, versioning discipline |
| Process performance | Discover/Build/Ship/Operate controls and handoffs |
| Customer and complaint handling | Feedback channels, escalation handling, customer evidence |
| Supplier / external provider control | Vendor assessment, monitoring, quality criteria |
| Improvement and corrective action | Signals, postmortems, action closure discipline |
| Measurement and monitoring | Observability evidence, dashboards, KPI/SLO reporting |

---

## 5. Relationship To Continuous Quality Evaluation

Quality evaluations are a valuable input to the audit programme because they show
ongoing policy conformance. They are not sufficient on their own, because ISO 9001
expects a planned programme with explicit scope, independence, and reporting.

The practical model is:

- continuous quality evaluation feeds the audit plan
- internal audit samples the system more formally
- management review consumes both

---

## 6. Verification Checklist

- [ ] The audit cadence is planned rather than ad hoc
- [ ] Audit scope and criteria are defined for each audit
- [ ] Independence is documented
- [ ] Results are reported to management
- [ ] Corrective actions are tracked to closure
- [ ] Audit outputs feed management review
