<!-- placeholder-ok -->
# ISO 9001 — Formal QMS Scope Statement Guide

> **Implements:** Formal QMS scope statement (clause 4.3)
> **Standard:** ISO 9001:2015 — Quality Management Systems
> **Severity:** High — required for certification; auditors check this first
> **Related issue:** [#137](https://github.com/wlfghdr/agentic-enterprise/issues/137)
> **Related compliance doc:** [ISO 9001 Compliance Reference](../iso-9001.md)

---

## 1. Purpose

The Agentic Enterprise framework provides a comprehensive quality management foundation: 19 quality policies in `org/4-quality/policies/`, a 4-loop process lifecycle (`process/`), CODEOWNERS-based roles and responsibilities, version-controlled documented information, and continuous improvement through the signals system. These artifacts collectively satisfy the substance of most ISO 9001 clauses.

This guide implements the **formal QMS scope statement** as required by ISO 9001:2015 clause 4.3. Adopters use this guide to demonstrate that they have:

- Considered the internal and external issues relevant to their purpose and strategic direction (clause 4.1)
- Considered the requirements of relevant interested parties (clause 4.2)
- Defined the boundaries and applicability of the QMS
- Determined which products and services are covered
- Justified any clauses determined to be not applicable

The scope statement is the first document auditors request during an ISO 9001 certification audit. It frames the entire QMS boundary and determines what is in and out of scope for assessment.

This guide provides a fill-in scope statement template, maps existing framework artifacts to ISO 9001 QMS elements, and gives guidance on documenting the context of the organization.

---

## 2. QMS Scope Statement Requirements (ISO 9001:2015 Clause 4.3)

Clause 4.3 requires the organization to determine the boundaries and applicability of the QMS to establish its scope. When determining scope, the organization must consider:

| Input | Clause Reference | What Must Be Considered |
|-------|-----------------|------------------------|
| External and internal issues | 4.1 | Issues that are relevant to the organization's purpose, strategic direction, and ability to achieve intended results of the QMS |
| Requirements of interested parties | 4.2 | Relevant requirements of relevant interested parties (customers, regulators, employees, suppliers, shareholders) |
| Products and services | 4.3 | The products and services of the organization that fall within the QMS boundary |
| Applicability of requirements | 4.3 | All requirements of ISO 9001 apply unless the organization determines that a requirement cannot be applied — with justification |

### Mandatory Content of the Scope Statement

The scope statement must:

1. **State the types of products and services covered** — what the organization delivers within the QMS boundary
2. **Justify any non-applicable requirements** — if any clause of ISO 9001 (4 through 10) is determined not applicable, provide justification that demonstrates the exclusion does not affect the organization's ability or responsibility to ensure conformity of its products and services
3. **Be available as documented information** — maintained, version-controlled, and available to interested parties upon request
4. **Reflect the actual activities of the organization** — the scope must be honest about what is and is not covered; auditors will verify through sampling

### Common Pitfalls

- **Scope too narrow:** Excluding processes that directly affect product/service quality to avoid audit scrutiny — auditors will challenge this
- **Scope too broad:** Including activities the organization does not actually perform, leading to nonconformities during audit
- **Missing exclusion justification:** Claiming a clause is not applicable without demonstrating why
- **Static scope:** Failing to update the scope when the organization's products, services, or context change

---

## 3. QMS Scope Statement Template

The following template is designed for organizations adopting the Agentic Enterprise framework. It is pre-populated with framework artifacts as the foundation. Adopters must replace all `{{PLACEHOLDER}}` values with organization-specific information.

```markdown
# Quality Management System — Scope Statement

> **Organization:** {{COMPANY_LEGAL_NAME}}
> **Standard:** ISO 9001:2015
> **Version:** 1.0
> **Effective date:** {{YYYY-MM-DD}}
> **Approved by:** {{APPROVER_NAME_AND_ROLE}}
> **Next review:** {{YYYY-MM-DD}} (at least annually)

## 1. Organization Identity

| Field | Value |
|-------|-------|
| Legal name | {{COMPANY_LEGAL_NAME}} |
| Trading name(s) | {{TRADING_NAMES}} |
| Primary location(s) | {{LOCATIONS}} |
| Industry / sector | {{INDUSTRY_SECTOR}} |
| Number of employees | {{HEADCOUNT}} |

## 2. Context of the Organization (Clause 4.1)

### Internal Issues

| Issue | Relevance to QMS |
|-------|-------------------|
| Agentic operating model (multi-agent, multi-layer governance) | Defines how work is planned, executed, and evaluated — the QMS must account for agent-based execution alongside human oversight |
| {{INTERNAL_ISSUE_2}} | {{RELEVANCE}} |
| {{INTERNAL_ISSUE_3}} | {{RELEVANCE}} |

### External Issues

| Issue | Relevance to QMS |
|-------|-------------------|
| {{REGULATORY_ENVIRONMENT}} | {{RELEVANCE}} |
| {{MARKET_CONDITIONS}} | {{RELEVANCE}} |
| {{TECHNOLOGY_LANDSCAPE}} | {{RELEVANCE}} |

## 3. Interested Parties and Their Requirements (Clause 4.2)

| Interested Party | Relevant Requirements | How Monitored |
|-----------------|----------------------|---------------|
| Customers | {{CUSTOMER_REQUIREMENTS}} | Customer Policy, venture charters, customer satisfaction measurement |
| Regulatory authorities | {{APPLICABLE_REGULATIONS}} | Compliance reference documents (`docs/compliance/`), quality policies |
| Employees / operators | {{EMPLOYEE_REQUIREMENTS}} | CODEOWNERS, role definitions, agent type registry |
| Suppliers / vendors | {{VENDOR_REQUIREMENTS}} | Vendor Risk Management Policy |
| Shareholders / owners | {{SHAREHOLDER_REQUIREMENTS}} | Steering Layer governance, COMPANY.md strategic direction |
| {{ADDITIONAL_PARTY}} | {{REQUIREMENTS}} | {{MONITORING_METHOD}} |

## 4. Scope of the QMS

### 4.1 Scope Statement

{{COMPANY_LEGAL_NAME}} has established and maintains a quality management
system in accordance with ISO 9001:2015 for the following scope:

> **{{SCOPE_STATEMENT}}**
>
> Example: "Design, development, and operation of AI-assisted
> {{products/services}} delivered through an agentic enterprise
> operating model, including agent governance, quality assurance,
> and continuous improvement processes."

### 4.2 Products and Services Covered

| Product / Service | Description | Customer Segment |
|-------------------|-------------|-----------------|
| {{PRODUCT_1}} | {{DESCRIPTION}} | {{SEGMENT}} |
| {{PRODUCT_2}} | {{DESCRIPTION}} | {{SEGMENT}} |

### 4.3 Organizational Functions Covered

| Function / Layer | In Scope | Justification |
|-----------------|----------|---------------|
| Steering Layer (`org/0-steering/`) | Yes | Strategic direction and management review |
| Strategy Layer (`org/1-strategy/`) | Yes | Planning and objective setting |
| Orchestration Layer (`org/2-orchestration/`) | Yes | Resource allocation and work coordination |
| Execution Layer (`org/3-execution/`) | Yes | Product and service realization |
| Quality Layer (`org/4-quality/`) | Yes | Monitoring, measurement, and improvement |

### 4.4 Locations Covered

| Location | Activities Performed | In Scope |
|----------|---------------------|----------|
| {{LOCATION_1}} | {{ACTIVITIES}} | Yes / No |

### 4.5 Processes Covered

| Process Loop | Activities | Reference |
|-------------|------------|-----------|
| Discover & Decide | Signal intake, triage, prioritization, mission chartering | `process/1-discover/` |
| Design & Build | Technical design, implementation, peer review | `process/2-build/` |
| Validate & Ship | Quality evaluation, release management, deployment | `process/3-ship/` |
| Operate & Evolve | Monitoring, incident response, improvement, evolution | `process/4-operate/` |

## 5. Applicability of ISO 9001 Requirements

All clauses of ISO 9001:2015 (4 through 10) are applicable to this QMS,
with the following exception(s):

| Clause | Requirement | Applicable? | Justification |
|--------|-------------|-------------|---------------|
| 7.1.5 | Monitoring and measuring resources — calibration | No | The organization's products and services are software-based. No physical measurement equipment is used in the realization of products or services. Monitoring is performed through software observability tooling (OpenTelemetry) which is validated through automated testing, not physical calibration. |
| {{CLAUSE}} | {{REQUIREMENT}} | No | {{JUSTIFICATION}} |

> **Note:** If all clauses are applicable, state: "All clauses of
> ISO 9001:2015 (4 through 10) are applicable to this QMS.
> No exclusions have been determined."

## 6. Document Control

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{YYYY-MM-DD}} | {{AUTHOR}} | Initial scope statement |
```

---

## 4. Mapping Framework Artifacts to ISO 9001 QMS Elements

This section maps existing Agentic Enterprise framework artifacts to the QMS elements required by ISO 9001. Adopters can use this mapping to demonstrate that the framework provides the structural foundation of their QMS.

### Documented Information (Clause 7.5)

ISO 9001 requires the QMS to include documented information required by the standard and determined by the organization as necessary for QMS effectiveness.

| ISO 9001 Document Type | Framework Artifact | Path |
|------------------------|--------------------|------|
| Quality policy | 19 quality policies (mandatory per AGENTS.md Rule 4) | `org/4-quality/policies/` |
| Quality manual (optional but recommended) | OPERATING-MODEL.md + AGENTS.md + layer AGENT.md files | Root and `org/*/AGENT.md` |
| Documented procedures | Quality policies define procedural requirements; process loop documentation defines workflows | `org/4-quality/policies/`, `process/` |
| Records (evidence of conformity) | Git history, OTel traces, PR review records, quality evaluations | Git log, observability platform |
| Document control | Git version control with CI-enforced versioning (AGENTS.md Rule 10) | `.github/workflows/validate.yml` |

### Plan-Do-Check-Act (Clause 4.4, General)

The framework's 4-loop process lifecycle maps directly to the PDCA cycle:

| PDCA Phase | Framework Process Loop | Key Activities |
|------------|----------------------|----------------|
| **Plan** | Discover & Decide (`process/1-discover/`) | Signal triage, mission chartering, objective setting, risk assessment |
| **Do** | Design & Build (`process/2-build/`) | Technical design, implementation, execution of plans |
| **Check** | Validate & Ship (`process/3-ship/`) | Quality evaluation, testing, release criteria verification |
| **Act** | Operate & Evolve (`process/4-operate/`) | Post-deployment monitoring, incident response, corrective action, improvement signals |

### Continual Improvement (Clause 10)

| ISO 9001 Mechanism | Framework Implementation | Evidence |
|--------------------|-------------------------|----------|
| Nonconformity identification | Quality evaluations (PASS/FAIL), automated CI checks, incident detection | Quality eval artifacts, CI logs |
| Root cause analysis | Retrospectives (`work/retrospectives/`) with structured analysis | Retrospective records |
| Corrective action | Improvement signals trigger new missions; missions track corrective actions to closure | `work/signals/`, `work/missions/` |
| Preventive improvement | AGENTS.md Rule 7 — every agent is a sensor for improvement; signals capture observations continuously | Signal artifacts |
| Management review of improvement | Steering Layer reviews signal digests, evaluates organizational performance | Signal digests in `work/signals/digests/` |

### Monitoring, Measurement, Analysis, and Evaluation (Clause 9.1)

| ISO 9001 Requirement | Framework Mechanism | Reference |
|----------------------|---------------------|-----------|
| Process performance metrics | OTel traces with latency, throughput, error rate (RED metrics) | `docs/otel-contract.md` |
| Product/service conformity | Quality gate enforcement in CI/CD, release criteria in release contracts | Delivery Policy, `work/releases/` |
| Customer satisfaction | Customer Policy, experience metrics | `org/4-quality/policies/customer.md` |
| QMS effectiveness | SLO dashboards, error budget burn rates, mission outcome tracking | Performance Policy, Observability Policy |

### Management Responsibility (Clause 5)

| ISO 9001 Requirement | Framework Mechanism | Reference |
|----------------------|---------------------|-----------|
| Top management commitment | Steering Layer provides strategic direction; executive approval gates on all strategic decisions | `org/0-steering/AGENT.md` |
| Quality policy communication | AGENTS.md Rule 4 mandates policy compliance; instruction hierarchy ensures propagation | `AGENTS.md`, `CLAUDE.md` |
| Roles, responsibilities, authorities | CODEOWNERS defines approval authorities; AGENT.md hierarchy defines boundaries; Agent Type Registry defines capabilities | `CODEOWNERS`, `org/agents/` |
| Management review | Steering Layer reviews signals, missions, and organizational performance in evolution cycles | `org/0-steering/EVOLUTION.md` |

---

## 5. Context of the Organization (Clauses 4.1 and 4.2)

ISO 9001 requires organizations to understand their context before defining QMS scope. For organizations operating with the Agentic Enterprise model, the context has unique characteristics that must be explicitly documented.

### 5a. Documenting Internal Issues (Clause 4.1)

Internal issues are factors within the organization that affect its ability to achieve the intended results of the QMS. For an agentic enterprise, consider:

| Category | Example Issues to Document |
|----------|---------------------------|
| **Governance model** | Multi-agent execution with human oversight; 5-layer organizational model; PR-based approval governance |
| **Technology stack** | AI/ML capabilities and limitations; agent reliability and behavioral consistency; observability infrastructure maturity |
| **Organizational knowledge** | Agent instruction quality; policy completeness; template coverage; institutional knowledge captured in Git |
| **Culture and values** | "Humans decide, agents recommend" principle; evidence-based decision making; transparency and auditability |
| **Process maturity** | Process loop maturity levels; automation coverage; manual intervention points |
| **Resource constraints** | Agent compute capacity; human reviewer bandwidth; integration availability |

### 5b. Documenting External Issues (Clause 4.1)

External issues are factors outside the organization that affect the QMS:

| Category | Example Issues to Document |
|----------|---------------------------|
| **Regulatory environment** | AI-specific regulations (EU AI Act, local AI governance requirements); industry-specific regulations; data protection laws |
| **Market conditions** | Customer expectations around AI transparency; competitive landscape; market trust in AI-assisted delivery |
| **Technology trends** | LLM capability evolution; AI safety developments; observability standards maturation |
| **Standards landscape** | ISO/IEC 42001 (AI management systems); ISO/IEC 23894 (AI risk management); sector-specific standards |
| **Supply chain** | AI model provider reliability; cloud infrastructure dependencies; third-party integration stability |

### 5c. Documenting Interested Parties (Clause 4.2)

For each interested party, document: (a) who they are, (b) what their relevant requirements are, and (c) which of those requirements are applicable to the QMS.

**Interested parties typical for an agentic enterprise:**

| Interested Party | Relevant Requirements | QMS Implication |
|-----------------|----------------------|-----------------|
| **Customers** | Product/service quality; transparency about AI involvement; data handling; SLA compliance | Customer Policy, SLOs, release criteria, instructions for use |
| **Regulators** | Compliance with applicable law; auditability; incident reporting; human accountability | Compliance reference docs, audit trails, incident response policy |
| **Employees / human operators** | Clear roles and authorities; manageable oversight burden; training on AI systems | CODEOWNERS, AGENT.md hierarchy, agent type definitions |
| **AI model providers** | Acceptable use policies; usage reporting; API terms of service | Vendor Risk Management Policy, integration registry |
| **Certification bodies** | Conformity with ISO 9001; objective evidence; access during audits | QMS documentation, observability evidence, Git history |
| **End users** | Usability; reliability; privacy; transparency about AI-generated outputs | Experience Policy, Privacy Policy, transparency mechanisms |

### 5d. Maintaining Context Documentation

Clause 4.1 and 4.2 are not one-time exercises. The organization must:

- **Review context at planned intervals** — at minimum during management review (clause 9.3) and when significant changes occur
- **Update the scope statement** if changes to context affect QMS boundaries
- **Record context reviews** as documented information — a dated record of what was reviewed, what changed, and what actions were taken
- **Use the signal system** — agents observing changes in context (new regulations, market shifts, technology changes) should file improvement signals per AGENTS.md Rule 7

---

## 6. Verification Checklist

Use this checklist to verify that the QMS scope statement and supporting context documentation are complete and audit-ready.

### Scope Statement Completeness
- [ ] QMS scope statement is documented and version-controlled
- [ ] Scope statement defines the products and services covered
- [ ] Scope statement defines the organizational functions and locations covered
- [ ] Scope statement defines the processes covered
- [ ] All non-applicable clauses are identified with documented justification
- [ ] Justification demonstrates that exclusions do not affect product/service conformity
- [ ] Scope statement is approved by top management (or equivalent authority)
- [ ] Scope statement is available to interested parties upon request

### Context of the Organization (4.1)
- [ ] Internal issues relevant to the QMS are identified and documented
- [ ] External issues relevant to the QMS are identified and documented
- [ ] Issues specifically related to the agentic operating model are addressed
- [ ] A review schedule for context monitoring is defined

### Interested Parties (4.2)
- [ ] Relevant interested parties are identified
- [ ] Relevant requirements of each interested party are documented
- [ ] Requirements applicable to the QMS are distinguished from general requirements
- [ ] A review schedule for interested party requirements is defined

### Framework Artifact Mapping
- [ ] Quality policies in `org/4-quality/policies/` are referenced as documented procedures
- [ ] 4-loop process lifecycle is mapped to PDCA
- [ ] CODEOWNERS is referenced as the roles and responsibilities matrix
- [ ] Observability infrastructure is documented as the monitoring and measurement system
- [ ] Signal system and retrospectives are documented as the continual improvement mechanism
- [ ] Git version control is documented as the document control system

### Integration with Existing QMS Elements
- [ ] Scope statement references the quality policies as the quality policy documentation
- [ ] Scope statement is consistent with `COMPANY.md` (vision, mission, strategic direction)
- [ ] Scope statement is consistent with `CONFIG.yaml` (organizational configuration)
- [ ] Scope statement is consistent with `OPERATING-MODEL.md` (system description)

### Ongoing Maintenance
- [ ] Review frequency is defined (minimum annually, plus triggered reviews)
- [ ] Responsibility for scope statement maintenance is assigned
- [ ] Change triggers are documented (new products, organizational changes, regulatory changes)
- [ ] Scope statement version history is maintained
