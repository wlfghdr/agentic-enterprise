<!-- placeholder-ok -->
# ISO 22301 — BCMS Internal Audit Programme

> **Implements:** BCMS internal audit programme (clause 9.2)
> **Standard:** ISO 22301:2019 — Business Continuity Management Systems
> **Severity:** High — required for certification
> **Related issue:** [#141](https://github.com/wlfghdr/agentic-enterprise/issues/141)
> **Related compliance doc:** [ISO 22301 Compliance Reference](../iso-22301.md)

---

## 1. Purpose

ISO 22301 clause 9.2 requires organizations to conduct internal audits at planned intervals to provide information on whether the BCMS conforms to the organization's own requirements and the requirements of the standard, and whether it is effectively implemented and maintained. The audit programme must define frequency, methods, responsibilities, planning requirements, and reporting.

The Agentic Enterprise framework provides foundational coverage through the Quality Layer (Layer 4) evaluation mechanisms, which assess agent outputs and policy compliance. The framework also includes an ISO 27001 ISMS internal audit programme (if implemented per the [ISO 27001 implementation guides](../iso-27001.md)). This guide builds on those foundations to implement a formal BCMS-specific audit programme that systematically verifies BC arrangements — BIA currency, BC plan adequacy, exercise programme effectiveness, and overall BCMS performance against ISO 22301 requirements.

This guide provides the BCMS audit requirements, an audit programme template (scope, frequency, methodology, auditor competence, audit criteria), mapping to the framework's quality evaluations, integration with any existing ISO 27001 ISMS audit programme, and a verification checklist.

---

## 2. Audit Requirements (Clause 9.2)

ISO 22301 clause 9.2 specifies the following requirements:

| Requirement | Clause Reference | Description |
|-------------|-----------------|-------------|
| Planned intervals | 9.2 a) | Audits must be conducted at planned intervals — not ad-hoc |
| Conformity assessment | 9.2 a) 1) | Verify conformity with the organization's own BCMS requirements |
| Standard conformity | 9.2 a) 2) | Verify conformity with ISO 22301 requirements |
| Effective implementation | 9.2 a) | Verify the BCMS is effectively implemented and maintained |
| Audit programme planning | 9.2 b) | Plan, establish, implement, and maintain an audit programme including frequency, methods, responsibilities, planning requirements, and reporting |
| Risk-based frequency | 9.2 b) | Take into consideration the importance of the processes concerned and the results of previous audits |
| Audit criteria and scope | 9.2 c) | Define audit criteria and scope for each audit |
| Auditor independence | 9.2 d) | Select auditors and conduct audits to ensure objectivity and impartiality — auditors must not audit their own work |
| Results reporting | 9.2 e) | Ensure audit results are reported to relevant management |
| Documented information | 9.2 f) | Retain documented information as evidence of the audit programme and audit results |
| Corrective action | 9.2, 10.1 | Take necessary corrections and corrective actions without undue delay |

---

## 3. Audit Programme Template

The following template should be instantiated as a governed artifact (e.g., `docs/compliance/bcms-audit-programme.md`).

```markdown
# BCMS Internal Audit Programme

> **Version:** {{VERSION}}
> **Last updated:** {{YYYY-MM-DD}}
> **Programme owner:** {{AUDIT_PROGRAMME_OWNER — must be independent of BCMS
>   operations}}
> **Approved by:** {{APPROVER — top management per clause 5.1}}
> **BCMS scope reference:** {{LINK_TO_BCMS_SCOPE_STATEMENT}}
> **Review frequency:** Annual (audit programme itself is reviewed annually)

## 1. Programme Objectives

This audit programme ensures the BCMS:
- Conforms to the organization's own BCMS requirements and policies
- Conforms to ISO 22301:2019 requirements
- Is effectively implemented and maintained
- Delivers continual improvement in business continuity capability

## 2. Audit Scope

### 2a. BCMS Elements in Scope

The audit programme covers all elements of the BCMS as defined in the
BCMS scope statement:

| BCMS Element | ISO 22301 Clause | Audit Frequency | Priority |
|-------------|-----------------|-----------------|----------|
| BCMS scope and context | 4.1–4.4 | Annual | Medium |
| Leadership and BC policy | 5.1–5.3 | Annual | Medium |
| Risk and opportunity management | 6.1–6.2 | Annual | High |
| BC objectives and planning | 6.2–6.3 | Annual | Medium |
| Support (resources, competence, communication, documented info) | 7.1–7.5 | Annual | Medium |
| Business Impact Analysis | 8.2.2 | Annual | High |
| Risk assessment for BC | 8.2.3 | Annual | High |
| BC strategies and solutions | 8.3 | Annual | High |
| BC plans and procedures | 8.4 | Semi-annual | Critical |
| Exercise programme and results | 8.5 | Semi-annual | Critical |
| Monitoring, measurement, analysis | 9.1 | Annual | Medium |
| Management review | 9.3 | Annual | Medium |
| Improvement and corrective actions | 10.1–10.2 | Annual | Medium |

### 2b. Risk-Based Frequency Adjustment

Audit frequency may be increased for elements that:
- Had nonconformities in the previous audit cycle
- Support Tier 1 or Tier 2 critical processes
- Have undergone significant change since the last audit
- Are subject to regulatory scrutiny

| Condition | Frequency Adjustment |
|-----------|---------------------|
| Nonconformity found in previous audit | Next audit within 6 months (regardless of normal cycle) |
| Major nonconformity or systemic failure | Next audit within 3 months |
| Significant organizational or process change | Audit affected elements within current cycle |
| Post-incident (BC plan was activated) | Audit the activated plan and related elements within 30 days |
| No issues for 2 consecutive cycles | May extend to 18-month cycle (maximum) with management approval |

## 3. Audit Methodology

### 3a. Audit Types

| Type | Description | When Used |
|------|-------------|-----------|
| Full BCMS audit | Comprehensive audit of all BCMS elements | At least once per annual cycle |
| Focused audit | Audit of specific BCMS elements or clauses | Between full audits; risk-driven or follow-up |
| Post-incident audit | Audit triggered by BC plan activation | Within 30 days of any BC plan activation |
| Follow-up audit | Verify corrective actions from previous findings | As scheduled per corrective action timelines |

### 3b. Audit Techniques

| Technique | Description | Evidence Produced |
|-----------|-------------|-------------------|
| Document review | Review BCMS documentation for completeness and currency | Document checklist, gap notes |
| Record examination | Examine evidence of BCMS operation — exercise records, incident logs, management review minutes | Evidence log |
| Interview | Interview process owners, BC team members, management | Interview notes |
| Observation | Observe exercises, drills, or operational procedures | Observation notes |
| Observability data review | Query the observability platform for operational evidence — SLO compliance, DR drill metrics, incident timelines | Dashboard screenshots, query results |
| Technical verification | Verify technical controls — backup integrity, failover capability, replication status | Test results |

### 3c. Audit Criteria

Each audit finding is assessed against:
1. ISO 22301:2019 clause requirements
2. Organization's BCMS policies and procedures
3. BCMS scope statement commitments
4. BC plan documented procedures vs. actual practice
5. BIA currency and accuracy
6. Exercise programme execution and results

### 3d. Finding Classification

| Classification | Definition | Required Response |
|---------------|------------|-------------------|
| Major nonconformity | Absence or total failure of a required BCMS element; systemic breakdown of a process | Corrective action plan within 5 business days; resolution within 30 days; follow-up audit within 3 months |
| Minor nonconformity | Partial implementation or isolated failure of a required element | Corrective action plan within 10 business days; resolution within 60 days |
| Observation | Area for improvement that does not constitute nonconformity | Noted for management review; no mandatory timeline |
| Good practice | Effective implementation beyond minimum requirements | Documented for knowledge sharing |

## 4. Auditor Requirements

### 4a. Competence

| Competence Area | Requirement | Evidence |
|-----------------|-------------|---------|
| ISO 22301 knowledge | Understanding of all clauses and their intent | Training certificate, demonstrated experience |
| Audit methodology | Proficiency in ISO 19011 audit principles and techniques | ISO 19011 training, audit experience log |
| Business continuity domain | Understanding of BIA, BC planning, exercise design, and BC strategies | Professional experience or BC certification (e.g., CBCI, MBCI) |
| Organization knowledge | Familiarity with the organization's products, services, and operating model | Organizational briefing prior to audit |
| Agentic systems (recommended) | Understanding of multi-agent systems, AI governance, and the agentic operating model | Framework familiarization |

### 4b. Independence

| Rule | Requirement |
|------|-------------|
| No self-audit | Auditors must not audit processes they are responsible for operating or managing |
| Organizational independence | The audit function must report independently of BCMS operations — not to the BC Coordinator |
| Conflict of interest | Auditors must declare any conflicts; conflicted auditors are excluded from the affected audit scope |
| Rotation | Lead auditor should rotate at least every 3 years for a given audit area (recommended) |

### 4c. Audit Team

| Role | Responsibility | Independence Requirement |
|------|---------------|------------------------|
| Lead Auditor | Plan and conduct the audit, produce audit report, manage audit team | Must not be involved in BCMS operations |
| Auditor(s) | Conduct assigned audit activities, document findings | Must not audit their own work area |
| Technical Expert (optional) | Provide domain expertise (e.g., DR technology, agent architecture) | Advisory role — does not make audit judgments |

## 5. Audit Schedule

### 5a. Annual Audit Calendar

| Quarter | Audit Activity | BCMS Elements | Type |
|---------|---------------|---------------|------|
| Q1 | Full BCMS audit | All clauses (4–10) | Full |
| Q2 | BC plans and exercise review | 8.4, 8.5 | Focused |
| Q3 | BIA and risk assessment review | 8.2, 6.1 | Focused |
| Q4 | Pre-management-review audit | 9.1, 9.3, 10 | Focused |

### 5b. Audit Planning (Per Audit)

Each individual audit must have a documented audit plan:

| Element | Content |
|---------|---------|
| Audit objectives | What the audit aims to verify |
| Audit scope | Which BCMS elements, processes, locations, and time period |
| Audit criteria | Standards, policies, and procedures against which conformity is assessed |
| Audit team | Named auditors with roles and independence confirmation |
| Audit schedule | Dates, times, and sequence of audit activities |
| Auditee notification | Minimum 2 weeks advance notice (except post-incident audits) |
| Resources required | Access to documents, systems, observability data, personnel |

## 6. Audit Reporting

### 6a. Audit Report Template

Each audit produces a formal report:

| Section | Content |
|---------|---------|
| Executive summary | Overall conformity status, number and severity of findings |
| Audit details | Scope, criteria, team, dates, methodology |
| Findings | Each finding with: classification, clause reference, evidence, description, risk |
| Corrective action requirements | Required actions, responsible parties, deadlines |
| Good practices identified | Effective implementations worth preserving or sharing |
| Auditor conclusion | Overall assessment of BCMS effectiveness |
| Distribution | Management recipients of the report |

### 6b. Reporting and Follow-Up

| Activity | Timeline | Responsible |
|----------|----------|------------|
| Draft audit report | Within 5 business days of audit completion | Lead Auditor |
| Report distributed to management | Within 10 business days of audit completion | Audit Programme Owner |
| Corrective action plans submitted | Per finding classification timelines | Process owners |
| Corrective action verification | Per finding classification timelines | Lead Auditor |
| Audit results input to management review | Next scheduled management review | Audit Programme Owner |

## 7. Records and Retention

| Record | Retention Period | Storage |
|--------|-----------------|---------|
| Audit programme (this document) | Current version plus previous 3 versions | Version-controlled in repository |
| Individual audit plans | 3 years | Repository or document management |
| Audit reports | 3 years (minimum) | Repository or document management |
| Corrective action records | 3 years after closure | Repository or document management |
| Auditor competence records | Duration of auditor role plus 2 years | HR or audit records |
```

---

## 4. Mapping to Framework Quality Evaluations

The BCMS audit programme leverages and extends the framework's existing quality mechanisms:

| Framework Mechanism | BCMS Audit Integration | Relationship |
|--------------------|-----------------------|--------------|
| Quality Layer evaluations (Layer 4) | BCMS audits are a specialized evaluation type; findings feed into the Quality Layer signal pipeline | Complementary — quality evals cover agent output quality; BCMS audits cover continuity readiness |
| Policy compliance checks (CI) | Automated policy validation provides baseline evidence for BCMS document control audits (clause 7.5) | BCMS audit verifies the policies themselves are adequate, not just that documents are formatted correctly |
| Improvement signals (`work/signals/`) | BCMS audit findings that require structural changes are filed as improvement signals | Audit findings flow into the normal signal-to-mission governance cycle |
| Retrospectives (`work/retrospectives/`) | Post-incident retrospectives provide evidence for BCMS audits (clause 10.1) and are inputs to post-incident audits | Retrospectives are consumed by audits; audit findings may trigger new retrospectives |
| Observability platform | Auditors query the observability platform for operational evidence — SLO compliance, incident response times, DR drill results | Observability data is primary evidence for BCMS effectiveness (not just documentation review) |

---

## 5. Integration with ISO 27001 ISMS Audit Programme

If the organization also maintains an ISO 27001 ISMS, the BCMS and ISMS audit programmes should be coordinated to avoid duplication and ensure consistency:

| Integration Point | Approach |
|-------------------|----------|
| Shared Annex SL clauses | Clauses 4–7 and 9–10 share the same high-level structure in both standards. Conduct a single combined audit for these clauses, assessing conformity against both ISO 22301 and ISO 27001 requirements simultaneously. |
| Separate domain-specific clauses | ISO 22301 clause 8 (BIA, BC strategies, BC plans, exercises) and ISO 27001 Annex A controls require domain-specific audit expertise. Audit these separately with appropriate auditors. |
| Shared auditor pool | Maintain a combined auditor roster with competence profiles indicating which standards each auditor is qualified to assess. |
| Combined audit schedule | Align the BCMS and ISMS audit calendars to avoid audit fatigue — schedule combined audits for shared clauses, separate audits for domain-specific requirements. |
| Shared finding tracking | Use a single corrective action tracking system for findings from both programmes. Cross-reference findings that affect both systems. |
| Combined management review | Where practical, combine BCMS and ISMS management review inputs into a single review meeting (clause 9.3 requirements are compatible). |
| Information security and BC overlap | Specifically coordinate audits of: incident response (shared), risk assessment (shared methodology, different risk registers), business continuity controls in ISO 27001 Annex A (A.5.29, A.5.30), and DR/backup controls. |

### Combined Audit Calendar Example

| Quarter | BCMS Audit | ISMS Audit | Combined? |
|---------|-----------|-----------|-----------|
| Q1 | Full BCMS audit (clauses 4–10) | — | BCMS-only (ISMS full audit in Q2) |
| Q2 | — | Full ISMS audit (clauses 4–10, Annex A) | ISMS-only (clauses 4–7, 9–10 findings inform both) |
| Q3 | BC plans + exercises (8.4, 8.5) | Annex A technical controls | Separate — different domain expertise |
| Q4 | BIA + risk (8.2, 6.1) + pre-management-review | ISMS risk + pre-management-review | Combined management review inputs |

---

## 6. Verification Checklist

### Audit Programme Structure
- [ ] Audit programme is documented and approved by top management
- [ ] Audit programme defines frequency for all BCMS elements
- [ ] Frequency is risk-based — critical elements audited more frequently
- [ ] Audit methodology is defined (types, techniques, criteria, finding classification)
- [ ] Audit programme is reviewed and updated at least annually

### Auditor Competence and Independence
- [ ] Auditor competence requirements are defined
- [ ] Auditors have documented evidence of required competence (training, experience, certification)
- [ ] Auditor independence rules are defined and enforced — no self-auditing
- [ ] Audit function reports independently of BCMS operations
- [ ] Auditor rotation is practiced (recommended: lead auditor rotates every 3 years per area)

### Audit Execution
- [ ] Individual audit plans are prepared for each audit with scope, criteria, team, and schedule
- [ ] Auditees receive advance notification (minimum 2 weeks, except post-incident)
- [ ] Audits are conducted per the defined methodology
- [ ] Findings are classified per the defined classification scheme
- [ ] Audit reports are produced within the defined timeline

### Reporting and Follow-Up
- [ ] Audit results are reported to relevant management
- [ ] Corrective action plans are required for all nonconformities
- [ ] Corrective action timelines are defined and tracked
- [ ] Follow-up audits verify corrective action effectiveness
- [ ] Audit results are inputs to management review (clause 9.3)

### Integration
- [ ] BCMS audit programme is coordinated with ISMS audit programme (if applicable)
- [ ] Shared clauses are audited consistently across both programmes
- [ ] Audit findings are filed as improvement signals when structural changes are needed
- [ ] Observability platform data is used as audit evidence (not just documentation review)

### Records
- [ ] Audit programme, plans, reports, and corrective action records are retained per defined retention periods
- [ ] Audit records are version-controlled or stored in a governed document management system
- [ ] Historical audit results are accessible for trend analysis and risk-based planning
