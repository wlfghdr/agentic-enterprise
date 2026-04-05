# AI System Impact Assessment

> **Template version:** 1.0
> **Last updated:** 2026-04-05
> **Standard:** ISO/IEC 42001:2023 — Clauses 6.1.4, 8.4, Annex A.5.2--A.5.5
> **Purpose:** Assess and document potential consequences of AI systems on individuals, groups, and societies

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | AIMS-IMPACT-001 |
| Version | {{VERSION}} |
| Classification | {{CLASSIFICATION}} |
| Owner | {{ASSESSMENT_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | At planned intervals or when significant changes occur (per Clause 8.4) |
| Retention period | {{RETENTION_PERIOD}} |
| Related | [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md), [AIMS Scope](_TEMPLATE-aims-scope.md) |

---

## 1. Assessment Process Definition (per A.5.2 / B.5.2)

### 1a. Trigger Criteria

An AI system impact assessment must be performed when any of the following apply:

- [ ] New AI system deployment or significant change to an existing system
- [ ] Criticality of the intended purpose or context changes
- [ ] Complexity of the AI technology or automation level changes
- [ ] Sensitivity of data types or data sources changes
- [ ] Planned interval review is due (per Clause 8.4)
- [ ] Regulatory or legal requirement changes affecting the AI system
- [ ] Incident or adverse impact report received for the AI system

### 1b. Assessment Elements

| Element | Description |
|---------|-------------|
| **Identification** | Identify sources, events, and potential outcomes — both positive and negative — arising from the AI system's deployment, intended use, and foreseeable misuse |
| **Analysis** | Analyze consequences (severity) and likelihood for each identified outcome |
| **Evaluation** | Determine acceptance decisions and prioritize risks based on organizational risk criteria |
| **Treatment** | Define mitigation measures for unacceptable impacts; link to the AI risk treatment plan |
| **Documentation and reporting** | Record all findings; make available to relevant interested parties where appropriate |

### 1c. Assessor Role

| Field | Value |
|-------|-------|
| Lead assessor | {{LEAD_ASSESSOR}} |
| Assessment team | {{TEAM_MEMBERS}} |
| Independence requirement | Assessors must not be solely responsible for the AI system under assessment |
| Competence requirements | Familiarity with ISO 42001, AI risk assessment, and the domain of the AI system |

### 1d. Utilization of Results

- Results inform design, deployment, and operational decisions for the AI system
- Results exceeding organizational risk appetite trigger formal review and approval before proceeding
- Results are input to the AIMS management review (Clause 9.3)
- Results feed into the AI risk treatment plan and Statement of Applicability

### 1e. Scope

| Field | Value |
|-------|-------|
| AI system name | {{AI_SYSTEM_NAME}} |
| System purpose | {{SYSTEM_PURPOSE}} |
| Risk tier (per ai-governance.md) | {{RISK_TIER}} |
| Individuals potentially impacted | {{INDIVIDUALS_IN_SCOPE}} |
| Groups potentially impacted | {{GROUPS_IN_SCOPE}} |
| Societies potentially impacted | {{SOCIETIES_IN_SCOPE}} |

---

## 2. Assessment Documentation (per A.5.3 / B.5.3)

### 2a. Intended Use and Foreseeable Misuse

| Category | Description |
|----------|-------------|
| Intended use | {{INTENDED_USE}} |
| Reasonable foreseeable misuse | {{FORESEEABLE_MISUSE}} |
| Out-of-scope uses | {{OUT_OF_SCOPE_USES}} |

### 2b. Positive and Negative Impacts

| Impact | Affected party | Positive / Negative | Severity | Likelihood | Risk level |
|--------|---------------|---------------------|----------|------------|------------|
| {{IMPACT_1}} | {{PARTY}} | {{P_OR_N}} | {{SEV}} | {{LIKE}} | {{RISK}} |

### 2c. Predictable Failures

| Failure mode | Potential impact | Severity | Mitigation measure | Residual risk |
|-------------|-----------------|----------|-------------------|---------------|
| {{FAILURE_1}} | {{IMPACT}} | {{SEV}} | {{MITIGATION}} | {{RESIDUAL}} |

### 2d. Relevant Demographic Groups

| Demographic dimension | Applicable? | Notes |
|----------------------|:-----------:|-------|
| Age | {{Y/N}} | {{NOTES}} |
| Gender | {{Y/N}} | {{NOTES}} |
| Race / ethnicity | {{Y/N}} | {{NOTES}} |
| Disability | {{Y/N}} | {{NOTES}} |
| Socioeconomic status | {{Y/N}} | {{NOTES}} |
| Geographic location | {{Y/N}} | {{NOTES}} |
| Language | {{Y/N}} | {{NOTES}} |
| Other: {{DIMENSION}} | {{Y/N}} | {{NOTES}} |

### 2e. System Complexity

| Factor | Description |
|--------|-------------|
| AI technology type | {{TECHNOLOGY_TYPE}} |
| Automation level | {{AUTOMATION_LEVEL}} |
| Number of models / components | {{COMPONENT_COUNT}} |
| Data dependencies | {{DATA_DEPENDENCIES}} |
| Integration complexity | {{INTEGRATION_COMPLEXITY}} |

### 2f. Human Role and Oversight

| Factor | Description |
|--------|-------------|
| Human oversight model | {{OVERSIGHT_MODEL}} |
| Human-in-the-loop capabilities | {{HITL_CAPABILITIES}} |
| Override processes | {{OVERRIDE_PROCESSES}} |
| Override tools | {{OVERRIDE_TOOLS}} |
| Escalation path | {{ESCALATION_PATH}} |

### 2g. Employment and Staff Skilling Impacts

| Impact area | Assessment |
|-------------|------------|
| Job displacement risk | {{DISPLACEMENT_ASSESSMENT}} |
| New skills required | {{SKILLS_REQUIRED}} |
| Training / reskilling plan | {{TRAINING_PLAN}} |
| Workforce transition support | {{TRANSITION_SUPPORT}} |

---

## 3. Individual and Group Impact Assessment (per A.5.4 / B.5.4)

Assess each area for impacts to individuals or groups of individuals throughout the AI system's life cycle.

| Impact area | Affected individuals / groups | Impact description | Severity (1-5) | Likelihood (1-5) | Risk rating | Mitigation |
|-------------|------------------------------|-------------------|:--------------:|:----------------:|:-----------:|------------|
| **Fairness** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Accountability** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Transparency and explainability** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Security and privacy** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Safety and health** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Financial consequences** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Accessibility** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |
| **Human rights** | {{PARTIES}} | {{DESCRIPTION}} | {{SEV}} | {{LIKE}} | {{RATING}} | {{MITIGATION}} |

---

## 4. Societal Impact Assessment (per A.5.5 / B.5.5)

Assess each area for impacts to societies throughout the AI system's life cycle.

### 4a. Environmental Sustainability

| Factor | Assessment |
|--------|------------|
| GHG emissions (training + inference) | {{GHG_ASSESSMENT}} |
| Natural resource consumption | {{RESOURCE_ASSESSMENT}} |
| Energy efficiency measures | {{EFFICIENCY_MEASURES}} |
| Environmental mitigation | {{ENV_MITIGATION}} |

### 4b. Economic Impact

| Factor | Assessment |
|--------|------------|
| Financial services access | {{FINANCIAL_ACCESS}} |
| Employment impact | {{EMPLOYMENT_IMPACT}} |
| Tax and fiscal implications | {{TAX_IMPLICATIONS}} |
| Trade and market effects | {{TRADE_EFFECTS}} |

### 4c. Government and Democratic Impact

| Factor | Assessment |
|--------|------------|
| Legislative process implications | {{LEGISLATIVE}} |
| Misinformation risk | {{MISINFO_RISK}} |
| National security considerations | {{NATIONAL_SECURITY}} |
| Criminal justice implications | {{CRIMINAL_JUSTICE}} |

### 4d. Health and Safety Impact

| Factor | Assessment |
|--------|------------|
| Healthcare access effects | {{HEALTHCARE_ACCESS}} |
| Diagnostic implications | {{DIAGNOSTIC}} |
| Physical harm potential | {{PHYSICAL_HARM}} |
| Psychological harm potential | {{PSYCHOLOGICAL_HARM}} |

### 4e. Norms, Traditions, Culture, and Values

| Factor | Assessment |
|--------|------------|
| Cultural impact | {{CULTURAL_IMPACT}} |
| Social norms effects | {{SOCIAL_NORMS}} |
| Value alignment | {{VALUE_ALIGNMENT}} |
| Tradition preservation | {{TRADITION}} |

---

## 5. Risk Treatment Summary

| Risk ID | Description | Treatment option | Treatment detail | Owner | Deadline | Status |
|---------|-------------|-----------------|-----------------|-------|----------|--------|
| {{ID}} | {{DESC}} | Mitigate / Accept / Transfer / Avoid | {{DETAIL}} | {{OWNER}} | {{DEADLINE}} | {{STATUS}} |

---

## 6. Retention and Review

| Field | Value |
|-------|-------|
| Retention period | {{RETENTION_PERIOD}} (per A.5.3: results retained for a defined period) |
| Next scheduled review | {{NEXT_REVIEW_DATE}} |
| Review trigger conditions | Significant system change, incident, regulatory change, planned interval |

---

## 7. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead assessor | {{NAME}} | {{SIGNATURE}} | {{DATE}} |
| AI system owner | {{NAME}} | {{SIGNATURE}} | {{DATE}} |
| AIMS management representative | {{NAME}} | {{SIGNATURE}} | {{DATE}} |

---

## Compliance Mapping

| Standard clause | Section in this template |
|----------------|------------------------|
| Clause 6.1.4 — AI system impact assessment process | §1 (process definition), §2--4 (assessment), §5 (treatment) |
| Clause 8.4 — Perform impact assessments at planned intervals | §1a (trigger criteria), §6 (review schedule) |
| A.5.2 — Process for assessing consequences | §1 (full process definition) |
| A.5.3 — Document and retain results | §2 (documentation), §6 (retention) |
| A.5.4 — Individual / group impact assessment | §3 (8 impact areas) |
| A.5.5 — Societal impact assessment | §4 (5 impact areas) |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-05 | Initial template covering Clauses 6.1.4, 8.4, A.5.2--A.5.5. Closes #245. |
