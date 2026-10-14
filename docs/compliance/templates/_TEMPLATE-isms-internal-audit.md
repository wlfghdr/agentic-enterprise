# ISMS Internal Audit Programme

> **Standard:** ISO/IEC 27001:2022 — Clause 9.2
> **Purpose:** Establish a systematic internal audit programme for the ISMS

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ISMS-AUDIT-001 |
| Version | {{VERSION}} |
| Classification | Confidential |
| Owner | {{AUDIT_PROGRAMME_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual |
| Related | [ISMS Scope](_TEMPLATE-isms-scope.md), [SoA](_TEMPLATE-soa.md) |

## 1. Audit Programme Overview

### 1a. Objectives

- Verify ISMS conformity with ISO 27001:2022 requirements
- Verify ISMS conformity with the organization's own information security requirements
- Assess effective implementation and maintenance of the ISMS
- Provide input for continual improvement
- Prepare for external certification/surveillance audits

### 1b. Scope

The audit programme covers the full ISMS scope as defined in the [ISMS Scope Statement](_TEMPLATE-isms-scope.md), including:

- All ISO 27001 clauses (4-10)
- All applicable Annex A controls (per [SoA](_TEMPLATE-soa.md))
- The Agentic Enterprise operating model processes
- Agent governance and quality controls

### 1c. Authority

The audit programme is authorized by {{MANAGEMENT_AUTHORITY}} and operates independently of the functions being audited.

## 2. Audit Schedule

### 2a. Annual Audit Cycle

Full ISMS cycle over 12 months — each clause and control group audited at least once per year:

| Quarter | Audit Focus | ISO 27001 Clauses/Controls | Duration |
|---------|-------------|---------------------------|----------|
| Q1 | Governance & Risk | Clauses 4-6, A.5.1-A.5.10 | {{DAYS}} days |
| Q2 | Operations & Access | Clauses 7-8, A.5.11-A.5.23, A.6, A.8.1-A.8.10 | {{DAYS}} days |
| Q3 | Monitoring & Incident | Clause 9, A.5.24-A.5.37, A.8.11-A.8.23 | {{DAYS}} days |
| Q4 | Technology & Improvement | Clause 10, A.7, A.8.24-A.8.34 | {{DAYS}} days |

### 2b. Risk-Based Audit Planning

Priority adjustments based on:

- Previous audit findings (non-conformities increase audit attention)
- Changes to the ISMS scope, technology, or organization
- Incident history (areas with recent incidents get more scrutiny)
- External threat intelligence
- Results from agent-driven continuous quality reviews

### 2c. Special Audits

Triggered by:

- Major security incidents
- Significant organizational changes
- Regulatory requirement changes
- Pre-certification preparation

## 3. Auditor Requirements

### 3a. Independence (Clause 9.2b)

- Auditors must NOT audit their own work or area of responsibility
- In the Agentic Enterprise model:
  - Quality Layer agents provide continuous monitoring (this is NOT the internal audit)
  - Internal auditors must be independent of the layer/division being audited
  - A Strategy Layer agent cannot audit strategy decisions
  - An Execution Layer agent cannot audit execution quality
- **Recommended:** Engage a mix of internal staff and external consultants
- **Minimum:** Ensure no auditor has operational responsibility for the area being audited

### 3b. Competence

Internal auditors must have:

- Knowledge of ISO 27001:2022 requirements
- Understanding of the Agentic Enterprise operating model
- Audit methodology training (ISO 19011 recommended)
- Understanding of information security risks and controls
- Familiarity with the organization's ISMS

### 3c. Auditor Register

| Auditor | Role | Qualifications | Independence Status | Areas Qualified |
|---------|------|---------------|--------------------|-----------------|
| {{AUDITOR_1}} | {{ROLE}} | {{QUALIFICATIONS}} | Independent of {{AREAS}} | {{AREAS}} |

## 4. Audit Methodology

### 4a. Audit Types

| Type | Purpose | When |
|------|---------|------|
| Document review | Verify policies, procedures, records are current and complete | Every audit |
| Interview | Assess understanding and implementation by personnel | Quarterly audits |
| Technical testing | Verify control effectiveness through testing | Annual per control |
| Observation | Watch processes in operation | On-site/during operations |
| Agent telemetry review | Analyze OTel data for control effectiveness evidence | Continuous (feed into quarterly) |

### 4b. Audit Process

1. **Planning** — Select scope, assign auditors, create audit checklist
2. **Opening meeting** — Communicate objectives and schedule to auditees
3. **Evidence collection** — Documents, interviews, observations, technical tests, telemetry review
4. **Analysis** — Evaluate evidence against criteria (ISO 27001 + SoA + policies)
5. **Findings** — Document conformities, non-conformities, observations, opportunities for improvement
6. **Closing meeting** — Present findings to auditees, agree corrective actions
7. **Reporting** — Formal audit report
8. **Follow-up** — Verify corrective actions are implemented and effective

### 4c. How Agent-Driven Quality Reviews Feed Into Audits

The Quality Layer (org/4-quality/) provides continuous automated evaluation. This is complementary to — but does NOT replace — the internal audit programme:

| Quality Layer Output | Audit Input |
|---------------------|-------------|
| Policy compliance evaluations | Evidence of control operation (CC5) |
| Agent evaluation results (agent-eval policy) | Evidence of agent governance effectiveness |
| Delivery quality gates | Evidence of change management effectiveness |
| Observability dashboards | Evidence of monitoring effectiveness |
| Incident response metrics | Evidence of incident management effectiveness |

The auditor uses these as **evidence sources**, not as audit conclusions. The auditor independently evaluates whether the evidence demonstrates effective control operation.

## 5. Non-Conformity Management

### 5a. Classification

| Classification | Definition | Response Timeline |
|---------------|-----------|-------------------|
| Major non-conformity | Absence or total failure of a required control, or systemic failure | Corrective action plan within 5 business days |
| Minor non-conformity | Partial implementation or isolated failure of a control | Corrective action plan within 20 business days |
| Observation | Area for improvement, not a failure | Address in next audit cycle |
| Opportunity for improvement | Suggestion for enhancement beyond requirements | Consider in management review |

### 5b. Corrective Action Process

1. **Root cause analysis** — determine why the non-conformity occurred
2. **Corrective action plan** — define actions to address root cause
3. **Implementation** — execute corrective actions
4. **Verification** — auditor verifies effectiveness of corrective action
5. **Closure** — non-conformity closed when verified effective

### 5c. Tracking

- Non-conformities tracked in {{TRACKING_SYSTEM}} (e.g., GitHub Issues with `audit:non-conformity` label, or `work/decisions/` artifacts)
- Status reviewed in every management review meeting
- Open non-conformities reported to management monthly

## 6. Audit Report Template

Each audit produces a formal report containing:

1. **Audit metadata** — date, scope, auditor(s), auditee(s)
2. **Executive summary** — overall assessment, key findings
3. **Detailed findings** — per clause/control assessed:
   - Evidence examined
   - Conformity status (conforming / non-conforming / observation)
   - Non-conformity details (if any)
   - Recommended corrective actions
4. **Statistics** — findings by classification and area
5. **Previous audit follow-up** — status of open corrective actions from prior audits
6. **Auditor opinion** — overall ISMS effectiveness assessment
7. **Distribution** — to ISMS Owner, management, auditees

## 7. Management Review Integration (Clause 9.3)

Internal audit results are a required input to management review. The audit programme provides:

- Summary of audit findings across the year
- Status of non-conformities and corrective actions
- Trends in ISMS effectiveness
- Areas requiring management attention or resources
- Recommendations for ISMS scope or control changes

## 8. Continuous Improvement

The audit programme itself is subject to improvement:

- Post-audit lessons learned
- Audit methodology effectiveness review
- Auditor feedback
- Alignment with external certification body expectations
- Adjustment based on organization and threat landscape changes

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial audit programme |
