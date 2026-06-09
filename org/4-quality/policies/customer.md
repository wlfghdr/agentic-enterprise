# Customer Policy

> **Applies to:** All customer-facing interactions — proposals, QBRs, support responses, onboarding, renewals, escalations
> **Enforced by:** Quality Layer eval agents
> **Authority:** Customer Success & Sales leadership
> **Version:** 1.2 | **Last updated:** 2026-06-09

---

## Principles

1. **Customer-centric** — Every interaction should deliver value to the customer.
2. **Honest** — Never overcommit. Under-promise and over-deliver.
3. **Responsive** — Acknowledge quickly, resolve thoroughly.
4. **Personalized** — Context-aware interactions, not generic templates.

## Mandatory Requirements

### Proposals & Sales Materials
- [ ] Tailored to customer's industry, use case, and current state
- [ ] Technical claims accurate and achievable
- [ ] Pricing aligned with approved pricing models
- [ ] Competitive positioning factual (no FUD)
- [ ] Timeline commitments realistic and approved by delivery
- [ ] All proposals marked "pending human review" before sending

### Customer Success Interactions
- [ ] QBR data current and verified
- [ ] Health scores based on actual usage data, not assumptions
- [ ] Recommendations actionable and specific
- [ ] Renewal risk assessment evidence-based
- [ ] Success metrics mapped to customer's stated objectives

### Support Interactions
- [ ] Response within SLA timeframe
- [ ] Root cause analysis for severity 1-2 incidents
- [ ] Knowledge base article created for novel issues
- [ ] Customer communication clear, empathetic, and solution-oriented
- [ ] Escalation procedures followed for unresolved issues

### Onboarding
- [ ] Onboarding plan customized to customer's environment
- [ ] Success criteria defined and agreed with customer
- [ ] Technical prerequisites documented
- [ ] Training materials appropriate for customer's skill level
- [ ] Go-live criteria clear and measurable

### Data & Privacy
- [ ] Customer data handled per data processing agreement
- [ ] No customer data shared across accounts
- [ ] Demo environments use synthetic data only
- [ ] Customer-specific configurations documented and secured

### AI System Customer Requirements (A.10.4, B.10.4)
- [ ] Capture AI-specific customer expectations during discovery, sales, onboarding, renewal, major change, and material incident review, including intended outcomes, prohibited uses, assurance needs, and required human-review points
- [ ] Document what the customer is told about each relevant AI-enabled feature: intended use, supported domain of use, known limitations, confidence or review caveats where applicable, and when human escalation is required
- [ ] Confirm whether the customer expects contract terms, usage restrictions, data-location commitments, model/provider restrictions, audit evidence, or opt-out controls related to AI use
- [ ] Route material AI-specific customer requirements into product, delivery, security, legal, and governance backlogs so they influence system design and operation instead of staying in account notes alone
- [ ] Re-confirm AI-related customer expectations when the system purpose, model provider, autonomy level, or data-handling pattern changes materially

### Responsibility Allocation for AI-Enabled Services (B.10.4)
- [ ] Customer-facing documentation and contracts define which responsibilities remain with the provider and which are assigned to the customer for each AI-enabled workflow
- [ ] Provider responsibilities cover at minimum: service operation, model and prompt governance, baseline safety controls, incident handling, and the accuracy of published product information
- [ ] Customer responsibilities cover at minimum: lawful use, user authorization, input-data quality where customer-supplied data is used, review of high-impact outputs where the workflow requires it, and compliance with communicated domain-of-use limits
- [ ] Shared-responsibility boundaries are reviewed by Legal or the accountable business owner before external commitment
- [ ] Where an AI system is valid only for a specific domain, industry context, geography, or user population, those limits are communicated before or at onboarding and whenever materially changed

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Personalization | Tailored to customer context | Generic template sent |
| Accuracy | All claims verifiable | Unverifiable commitments |
| SLA compliance | Within response window | SLA breach |
| Data privacy | Fully compliant | Customer data mishandled |
| Human review | All external comms reviewed | Sent without approval |
| AI expectations captured | AI-specific expectations and obligations documented for relevant customer interactions | AI requirements left implicit or undocumented |
| Domain-of-use disclosure | Customer receives clear AI intended-use boundaries and limitations | AI limitations or use boundaries not communicated |
| Responsibility allocation | Provider/customer AI responsibilities documented and reviewable | No clear shared-responsibility statement for AI-enabled service |

---

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|----------------|
| **ISO 9001:2015** | 4.2 Needs and expectations of interested parties | Proposals & Sales Materials; Customer Success Interactions |
| **ISO 9001:2015** | 8.2 Requirements for products and services | Proposals & Sales Materials; AI System Customer Requirements |
| **ISO 9001:2015** | 9.1 Monitoring, measurement, analysis, and evaluation | Customer Success Interactions; Support Interactions |
| **ISO 42001:2023** | A.10.4 Customer requirements | AI System Customer Requirements |
| **GDPR** | Art. 12 Transparent information and communication | Proposals & Sales Materials; Data & Privacy |
| **GDPR** | Art. 13 Information provided when personal data are collected | Data & Privacy |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-06-09 | Added structured compliance mappings for customer requirements, AI responsibility allocation, and privacy transparency. |
| 1.1 | 2026-05-23 | Added AI-specific customer requirements, domain-of-use communication expectations, and provider/customer responsibility allocation guidance for ISO 42001 A.10.4. Closes #254. |
| 1.0 | 2026-02-19 | Initial version |
