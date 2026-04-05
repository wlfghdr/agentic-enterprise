# AIMS Internal Audit Programme

> **Template version:** 1.0
> **Last updated:** 2026-04-05
> **Standard:** ISO/IEC 42001:2023 — Clauses 9.2.1, 9.2.2
> **Purpose:** Establish a systematic internal audit programme for the AI Management System

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | AIMS-AUDIT-001 |
| Version | {{VERSION}} |
| Classification | Confidential |
| Owner | {{AUDIT_PROGRAMME_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual |
| Related | [AIMS Scope](_TEMPLATE-aims-scope.md), [AIMS SoA](_TEMPLATE-aims-soa.md), [AIMS Management Review](_TEMPLATE-aims-management-review.md) |

---

## Part A: Audit Programme (per Clause 9.2.2)

### 1. Audit Programme Overview

#### 1a. Frequency

| Audit type | Frequency | Trigger |
|-----------|-----------|---------|
| Full AIMS audit cycle | Annual (all clauses and controls covered within 12 months) | Planned schedule |
| Focused / thematic audit | As needed | Significant change, incident, management request |
| Pre-certification audit | Prior to external audit | Certification timeline |

#### 1b. Scope

The audit programme covers the full AIMS scope as defined in the [AIMS Scope Statement](_TEMPLATE-aims-scope.md), including:

- All ISO 42001 clauses (4--10)
- All applicable Annex A controls (per [AIMS SoA](_TEMPLATE-aims-soa.md) — 39 AI-specific controls)
- AI system lifecycle processes
- AI risk assessment and impact assessment processes
- AI data governance processes

#### 1c. Methods

| Method | Description | When used |
|--------|-------------|-----------|
| Document review | Examine policies, templates, records, evidence | All audits |
| Interviews | Structured discussions with process owners and operators | Clause audits, control verification |
| Observation | Observe processes in operation | Operational control audits |
| Sampling | Select representative samples of records, decisions, outputs | High-volume processes |
| Technical testing | Verify technical controls (observability, access controls) | Technical control audits |

#### 1d. Responsibilities

| Role | Responsibility |
|------|----------------|
| Audit programme manager | Plan, maintain, and report on the audit programme; ensure auditor competence and independence |
| Lead auditor | Plan and conduct individual audits; produce audit reports |
| Auditor(s) | Collect evidence, assess conformity, document findings |
| Auditee | Provide access to evidence, cooperate with auditors, implement corrective actions |
| Top management | Receive audit results, approve corrective actions, ensure resources |

#### 1e. Planning Requirements

| Requirement | Detail |
|-------------|--------|
| Lead time | Minimum {{LEAD_TIME}} weeks notice to auditees |
| Pre-audit documentation | Auditors receive: AIMS scope, SoA, relevant policies, previous audit reports, corrective action status |
| Audit plan distribution | Distributed to all auditees at least {{DISTRIBUTION_LEAD}} days before audit |
| Resource allocation | {{RESOURCE_NOTES}} |

#### 1f. Reporting

| Report type | Audience | Timing |
|-------------|----------|--------|
| Individual audit report | Auditees, process owners, audit programme manager | Within {{REPORT_DAYS}} days of audit completion |
| Audit programme summary | Top management, AIMS management representative | Annual (input to management review per 9.3.2 d.3) |
| Corrective action tracking | Audit programme manager, relevant process owners | Ongoing |

---

## Part B: Individual Audit Plan (per Clause 9.2.2 a--c)

### 2. Audit Objectives (9.2.2 a)

| Objective | Description |
|-----------|-------------|
| Conformity — organizational | Verify the AIMS conforms to the organization's own AI management requirements |
| Conformity — ISO 42001 | Verify the AIMS conforms to all applicable requirements of ISO/IEC 42001:2023 |
| Effectiveness | Assess whether the AIMS is effectively implemented and maintained |
| Specific objective | {{SPECIFIC_OBJECTIVE}} |

### 3. Audit Criteria and Scope (9.2.2 a)

| Field | Value |
|-------|-------|
| Standard clauses in scope | {{CLAUSES_IN_SCOPE}} |
| Annex A controls in scope | {{CONTROLS_IN_SCOPE}} |
| Organizational requirements | {{ORG_REQUIREMENTS}} |
| Timeframe under review | {{REVIEW_PERIOD}} |
| Systems / locations in scope | {{SYSTEMS_IN_SCOPE}} |

### 4. Auditor Selection (9.2.2 b)

| Field | Value |
|-------|-------|
| Lead auditor | {{LEAD_AUDITOR}} |
| Auditor(s) | {{AUDITORS}} |
| Independence verification | Auditors shall not audit their own work — no auditor may audit processes or controls for which they are directly responsible |
| Impartiality statement | {{IMPARTIALITY_NOTES}} |
| Competence requirements | Knowledge of ISO 42001, AI systems, audit methodology |

### 5. Audit Schedule

| Date | Time | Activity | Auditee(s) | Auditor(s) |
|------|------|----------|------------|------------|
| {{DATE}} | {{TIME}} | Opening meeting | All | All |
| {{DATE}} | {{TIME}} | {{AUDIT_ACTIVITY}} | {{AUDITEE}} | {{AUDITOR}} |
| {{DATE}} | {{TIME}} | Closing meeting | All | All |

---

## Part C: AIMS-Specific Audit Checklist

This checklist is specific to ISO/IEC 42001:2023. It is NOT a copy of the ISO 27001 ISMS audit checklist.

### 6. Clauses 4--10 Conformity Checks

#### Clause 4 — Context of the Organization

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 4.1 | Are external and internal issues relevant to the AIMS determined? | {{C}} | {{E}} | |
| 4.2 | Are interested parties and their requirements identified? | {{C}} | {{E}} | |
| 4.3 | Is the AIMS scope defined and documented? | {{C}} | {{E}} | |
| 4.4 | Is the AIMS established, implemented, maintained, and continually improved? | {{C}} | {{E}} | |

#### Clause 5 — Leadership

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 5.1 | Does top management demonstrate leadership and commitment to the AIMS? | {{C}} | {{E}} | |
| 5.2 | Is an AI policy established, communicated, and available? | {{C}} | {{E}} | |
| 5.3 | Are AIMS roles, responsibilities, and authorities assigned? | {{C}} | {{E}} | |

#### Clause 6 — Planning

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 6.1.1 | Are risks and opportunities for the AIMS addressed? | {{C}} | {{E}} | |
| 6.1.2 | Is an AI risk assessment process defined and performed? | {{C}} | {{E}} | |
| 6.1.3 | Is an AI risk treatment process defined? Is the SoA produced? | {{C}} | {{E}} | |
| 6.1.4 | Is an AI system impact assessment process defined and performed? | {{C}} | {{E}} | |
| 6.2 | Are AI objectives established and plans to achieve them defined? | {{C}} | {{E}} | |

#### Clause 7 — Support

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 7.1 | Are resources for the AIMS determined and provided? | {{C}} | {{E}} | |
| 7.2 | Is competence of persons doing AI-related work determined and ensured? | {{C}} | {{E}} | |
| 7.3 | Are persons aware of the AI policy, their contribution, and implications of nonconformity? | {{C}} | {{E}} | |
| 7.4 | Are internal and external communications for the AIMS determined? | {{C}} | {{E}} | |
| 7.5 | Is documented information controlled (creation, updating, retention)? | {{C}} | {{E}} | |

#### Clause 8 — Operation

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 8.1 | Are operational processes planned, implemented, and controlled? | {{C}} | {{E}} | |
| 8.2 | Is the AI risk assessment performed at planned intervals? | {{C}} | {{E}} | |
| 8.3 | Is the AI risk treatment plan implemented? | {{C}} | {{E}} | |
| 8.4 | Are AI system impact assessments performed at planned intervals? | {{C}} | {{E}} | |

#### Clause 9 — Performance Evaluation

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 9.1 | Are monitoring, measurement, analysis, and evaluation performed? | {{C}} | {{E}} | |
| 9.2 | Are internal audits conducted at planned intervals? | {{C}} | {{E}} | |
| 9.3 | Does top management review the AIMS at planned intervals? | {{C}} | {{E}} | |

#### Clause 10 — Improvement

| Ref | Check | Conformity | Evidence | Notes |
|-----|-------|:----------:|----------|-------|
| 10.1 | Are nonconformities addressed and corrective actions taken? | {{C}} | {{E}} | |
| 10.2 | Is the AIMS continually improved? | {{C}} | {{E}} | |

### 7. Annex A Control Implementation Verification (39 AI-specific controls)

| Control | Title | Applicable (per SoA) | Implemented | Evidence | Finding |
|---------|-------|:--------------------:|:-----------:|----------|---------|
| A.2.2 | AI policy | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.2.3 | Roles and responsibilities | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.2.4 | Resources for AI | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.3.2 | AI system life cycle | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.3.3 | Responsible AI — due diligence | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.4.2 | AI risk assessment | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.4.3 | Approaches for addressing risks | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.4.4 | Documentation of risk assessment | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.4.5 | AI risk treatment | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.4.6 | AI risk communication | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.5.2 | AI impact assessment process | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.5.3 | Documentation of impact assessment | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.5.4 | Impact to individuals | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.5.5 | Impact to societies | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.1.2 | Objectives for responsible AI | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.1.3 | Organizational compliance with AI | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.2 | AI system design and development | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.3 | Verification and validation | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.4 | AI system operation and monitoring | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.5 | AI system documentation | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.6 | Responsible use of AI | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.7 | Third-party and customer relationships | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.6.2.8 | Log management | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.7.2 | Data management processes | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.7.3 | Data acquisition | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.7.4 | Data quality | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.7.5 | Data provenance | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.7.6 | Data preparation | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.8.2 | Conformity with legislation and regulation | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.8.3 | External reporting | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.8.4 | Use of specific technical tools | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.8.5 | Reporting obligations | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.9.2 | System log monitoring | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.9.3 | Performance monitoring | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.9.4 | AI system change management | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.10.2 | AI-specific awareness training | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.10.3 | AI literacy and fluency | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |
| A.10.4 | Customer AI requirements | {{Y/N}} | {{Y/N}} | {{E}} | {{F}} |

### 8. AI-Specific Audit Questions

| Question | Response | Evidence |
|----------|----------|----------|
| Is the AI risk assessment aligned with the AI policy and AI objectives? | {{RESPONSE}} | {{EVIDENCE}} |
| Are AI system impact assessments performed at planned intervals per 8.4? | {{RESPONSE}} | {{EVIDENCE}} |
| Is the Statement of Applicability for Annex A complete and current? | {{RESPONSE}} | {{EVIDENCE}} |
| Are AI data governance processes defined and followed per A.7.2--A.7.6? | {{RESPONSE}} | {{EVIDENCE}} |
| Is the AI system inventory current and complete? | {{RESPONSE}} | {{EVIDENCE}} |
| Are model cards maintained and current for all AI systems? | {{RESPONSE}} | {{EVIDENCE}} |
| Are fairness audits performed for high-risk AI systems? | {{RESPONSE}} | {{EVIDENCE}} |
| Is human oversight implemented for high-risk AI decisions? | {{RESPONSE}} | {{EVIDENCE}} |

---

## Part D: Audit Report Template

### 9. Audit Summary

| Field | Value |
|-------|-------|
| Audit ID | {{AUDIT_ID}} |
| Audit date(s) | {{AUDIT_DATES}} |
| Lead auditor | {{LEAD_AUDITOR}} |
| Audit scope | {{SCOPE_SUMMARY}} |
| Overall conclusion | {{CONCLUSION}} |

### 10. Findings

| Finding ID | Clause / Control | Classification | Description | Evidence | Corrective action | Owner | Deadline |
|-----------|-----------------|----------------|-------------|----------|-------------------|-------|----------|
| {{F_ID}} | {{REF}} | Major NC / Minor NC / Observation / OFI | {{DESC}} | {{EVIDENCE}} | {{ACTION}} | {{OWNER}} | {{DEADLINE}} |

**Classification guide:**
- **Major nonconformity**: Absence or total failure of a required process or control; systematic failure affecting AIMS effectiveness
- **Minor nonconformity**: Single instance of non-fulfilment; isolated failure that does not affect overall AIMS effectiveness
- **Observation**: Issue identified that could become a nonconformity if not addressed
- **Opportunity for improvement (OFI)**: Good practice suggestion beyond conformity requirements

### 11. Management Reporting (per 9.2.2 c)

| Recipient | Role | Report distributed | Date |
|-----------|------|--------------------|------|
| {{NAME}} | {{ROLE}} | Yes / No | {{DATE}} |

---

## Part E: Audit Evidence Requirements (per Clause 9.2.2)

Documented information must be available as evidence of:

| Evidence type | Description | Retention |
|---------------|-------------|-----------|
| Audit programme | Annual audit plan, schedule, scope, methods | Duration of certification cycle |
| Individual audit plans | Objectives, criteria, scope, auditor selection | Minimum {{RETENTION}} years |
| Audit reports | Findings, evidence, corrective actions | Minimum {{RETENTION}} years |
| Corrective action records | Actions taken, verification of effectiveness | Minimum {{RETENTION}} years |
| Auditor competence records | Qualifications, training, independence declarations | Current plus {{RETENTION}} years |

---

## Compliance Mapping

| Standard clause | Section in this template |
|----------------|------------------------|
| Clause 9.2.1 — Internal audit purpose | §2 (objectives) |
| Clause 9.2.2 — Audit programme (frequency, methods, responsibilities, planning, reporting) | Part A: §1a--1f |
| Clause 9.2.2(a) — Audit objectives, criteria, scope | Part B: §2--3 |
| Clause 9.2.2(b) — Auditor selection, objectivity, impartiality | Part B: §4 |
| Clause 9.2.2(c) — Results reporting to management | Part D: §11 |
| Clause 9.2.2 — Evidence of audit programme and results | Part E |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-05 | Initial template covering Clauses 9.2.1, 9.2.2. ISO 42001-specific checklist (Clauses 4--10 + 39 Annex A controls). Closes #248. |
