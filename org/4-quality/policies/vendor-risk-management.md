<!-- placeholder-ok -->
# Vendor & Third-Party Risk Management Policy

> **Applies to:** All third-party vendors, suppliers, service providers, subprocessors, and external integrations used by the organization or its agents
> **Enforced by:** Quality Layer eval agents, Procurement Division
> **Authority:** Security & Compliance team, Procurement leadership
> **Version:** 1.1 | **Last updated:** 2026-03-16

---

## Principles

1. **Vendors extend your attack surface** — Every third-party relationship introduces risk. A vendor's security failure is your incident. Governance must match the risk the vendor introduces.
2. **Assess before you integrate** — No vendor gains access to organizational systems, data, or agent workflows without a completed security assessment. The assessment gate applies equally to human-selected and agent-selected integrations.
3. **Proportional governance** — Not every vendor needs the same scrutiny. Criticality tiers scale assessment depth, monitoring frequency, and contractual requirements to the actual risk each vendor introduces.
4. **Continuous, not one-time** — Vendor risk is not static. Attestations expire, security postures change, services evolve. Ongoing monitoring is a requirement, not a stretch goal.
5. **Independence and resilience** — Vendor concentration is a risk. Over-reliance on a single provider for critical capabilities creates a single point of failure that must be identified, scored, and mitigated.
6. **Conformity matters too** — External providers affect product and service quality, not just security. Evaluation must include delivery quality, defect escape, change discipline, and corrective-action responsiveness when the vendor materially influences customer outcomes.

---

## Why This Policy Exists

The Integration Registry (AGENTS.md Rule 8) governs how external tools connect to the operating model, but does not assess whether the vendor behind the tool is trustworthy, financially viable, or compliant with the organization's security and privacy standards. Without vendor risk management:

- **ISO 27001 assessors** cannot verify supplier relationship controls (A.5.19–A.5.23)
- **ISO 9001 auditors** cannot verify external provider evaluation and monitoring criteria (8.4.1)
- **SOC 2 auditors** cannot confirm vendor risk mitigation (CC9.1, CC9.2)
- **Privacy regulators** cannot verify subprocessor oversight (GDPR Art. 28)
- **EU AI Act** deployer obligations for third-party AI systems go unaddressed (Art. 26–28)
- **Supply chain attacks** (SE-5 in risk-management.md) have no pre-integration detection gate
- **Enterprise procurement teams** lack the vendor risk documentation they require

This policy closes those gaps by defining how vendors are assessed, monitored, and governed across their full lifecycle.

---

## 1. Vendor Criticality Tiers

Every vendor relationship is assigned a criticality tier based on the risk it introduces. The tier determines assessment depth, monitoring frequency, and contractual requirements.

### 1.1 Tier Definitions

| Tier | Label | Criteria | Examples |
|------|-------|----------|----------|
| **1** | **Critical** | Vendor processes RESTRICTED or CONFIDENTIAL data, provides infrastructure or security services, or a failure would cause SEV1/SEV2 impact. No ready alternative exists. | Cloud infrastructure (AWS, Azure, GCP), primary LLM provider, identity provider, KMS, SIEM/observability platform |
| **2** | **Significant** | Vendor processes INTERNAL data, provides important business services, or a failure would cause SEV3 impact. Alternatives exist but switching has material cost. | CI/CD platform, collaboration tools, secondary AI providers, HR/payroll systems, CRM |
| **3** | **Standard** | Vendor provides commodity services, processes only PUBLIC data, or a failure has limited operational impact. Easy to replace. | CDN, email marketing, design tools, analytics, development utilities |
| **4** | **Low** | Vendor provides non-critical ancillary services with no data access and minimal operational dependency. | Office supplies, non-technical SaaS, informational subscriptions |

### 1.2 Tier Assignment Rules

- [ ] Every vendor with an active contract or integration is assigned a criticality tier
- [ ] Tier assignment is documented in the vendor's assessment record (see §3)
- [ ] Tier is reassessed when: the vendor's scope changes, data classification of shared data changes, or the organization's dependency on the vendor increases
- [ ] When tier assignment is uncertain, apply the higher tier until review confirms otherwise (same principle as data classification)
- [ ] AI/ML model providers are assessed at minimum Tier 2; providers of models used in High-Risk AI systems (per ai-governance.md Tier 1) are Tier 1

---

## 2. Vendor Lifecycle

Vendor governance spans five phases. Each phase has mandatory activities that scale by criticality tier.

### 2.1 Lifecycle Overview

```
IDENTIFICATION → ASSESSMENT → ONBOARDING → MONITORING → OFFBOARDING
     ↑                                          |
     └──────────── REASSESSMENT ←───────────────┘
```

### 2.2 Phase Requirements by Tier

| Phase | Tier 1 (Critical) | Tier 2 (Significant) | Tier 3 (Standard) | Tier 4 (Low) |
|-------|-------------------|---------------------|-------------------|-------------|
| **Assessment** | Full security + quality assessment questionnaire + attestation review + AI-specific assessment (if applicable) | Security + quality assessment questionnaire + attestation review | Lightweight assessment (attestation check + key questions) | Self-declaration |
| **Attestation** | SOC 2 Type II or ISO 27001 **required**; additional certifications as relevant (FedRAMP, HIPAA, PCI DSS) | SOC 2 Type II or ISO 27001 **required**; SOC 2 Type I accepted with remediation plan | SOC 2 Type I or equivalent **recommended** | Not required |
| **Contract** | Full vendor agreement with SLA, right-to-audit, breach notification (≤24h), subprocessor controls, data return/deletion, and quality/corrective-action clauses | Vendor agreement with SLA, breach notification (≤48h), data handling terms, and quality expectations | Standard terms with data handling addendum | Standard terms |
| **DPA** | Required if processing personal data (per privacy.md §2) | Required if processing personal data | Required if processing personal data | N/A |
| **Monitoring** | Continuous: attestation tracking, SLA + quality monitoring, quarterly review, annual reassessment | Attestation tracking, SLA + quality monitoring, semi-annual review, annual reassessment | Annual attestation check, annual reassessment | Reassess on renewal |
| **Offboarding** | Data return/deletion verification, credential revocation, integration deregistration, 30-day transition plan | Data deletion verification, credential revocation, integration deregistration | Credential revocation, integration deregistration | Account closure |

---

## 3. Vendor Security Assessment

### 3.1 Assessment Process

- [ ] Before a new vendor is onboarded or an existing vendor's scope is expanded, a security assessment is completed
- [ ] Assessment records are created using `work/assets/_TEMPLATE-vendor-security-assessment.md`
- [ ] Assessment results are reviewed by the Security & Compliance team (Tier 1–2) or the responsible division lead (Tier 3–4)
- [ ] Assessment findings are documented with risk ratings: PASS (acceptable), CONDITIONAL (acceptable with mitigations), FAIL (unacceptable — do not onboard)
- [ ] CONDITIONAL assessments require a remediation plan with timeline; unresolved findings trigger reassessment

### 3.2 Assessment Domains

The assessment questionnaire covers the following domains, scaled by criticality tier:

| Domain | What to Assess | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|--------|---------------|--------|--------|--------|--------|
| **Security posture** | Encryption (at rest + in transit), access controls, vulnerability management, penetration testing, incident response | Full | Full | Key questions | — |
| **Attestations & certifications** | SOC 2 Type II, ISO 27001, industry-specific (FedRAMP, HIPAA, PCI DSS) | Required | Required | Recommended | — |
| **Data handling** | Data classification support, residency/sovereignty, retention, deletion capability, backup, cross-border transfers | Full | Full | Key questions | — |
| **Privacy & subprocessor** | DPA readiness, subprocessor list, GDPR compliance, DSAR support, breach notification SLA | Full | Full | If PII involved | — |
| **Operational resilience** | Uptime SLA, RTO/RPO, disaster recovery, change management, notification procedures | Full | Full | SLA only | — |
| **Quality & conformity** | Delivery quality, defect rates, service/process conformity, acceptance criteria, corrective-action responsiveness, change notification discipline | Full | Full | Key questions | — |
| **Financial viability** | Financial health, market position, funding, acquisition risk, going-concern indicators | Full | Simplified | — | — |
| **AI-specific** (if vendor provides AI/ML services) | Model governance, training data provenance, bias/fairness, adversarial robustness, explainability, fourth-party model dependencies | Full | Full | Key questions | — |

### 3.3 AI Vendor Assessment — Extended Requirements

When a vendor provides AI or ML capabilities (LLM providers, AI SaaS, model hosting, AI-powered analytics), the assessment must additionally cover:

- [ ] **Model governance** — Does the vendor have documented model lifecycle management (training, validation, deployment, monitoring, retirement)?
- [ ] **Training data** — Can the vendor describe training data sources, consent, and opt-out mechanisms? Is customer data used for training (opt-in/opt-out)?
- [ ] **Bias and fairness** — Does the vendor test for and report on model bias? What fairness metrics are used?
- [ ] **Adversarial robustness** — Has the vendor tested for prompt injection, data poisoning, model extraction, and evasion attacks?
- [ ] **Explainability** — Can the vendor provide explanations for model decisions at a level appropriate to the use case?
- [ ] **Fourth-party dependencies** — Does the vendor use upstream model providers (e.g., OpenAI, Anthropic, Google)? If so, the assessment extends to those providers.
- [ ] **Model versioning and change notification** — Does the vendor pin model versions? What is the notification period for model changes, deprecations, or behavior shifts?
- [ ] **Data residency** — Where does inference happen? Where is input/output data stored? Does data leave the contracted region?

### 3.4 Attestation Verification

- [ ] Attestation documents (SOC 2 reports, ISO 27001 certificates) are collected and stored securely
- [ ] Attestation scope is verified — the attested services must cover the services the organization actually uses
- [ ] Attestation currency is verified — expired attestations trigger reassessment
- [ ] SOC 2 Type II reports are reviewed for qualified opinions, exceptions, and control deficiencies
- [ ] Bridge letters are requested if there is a gap between attestation periods

---

## 4. Vendor SLA & Contract Requirements

### 4.1 Mandatory Contract Clauses (Tier 1–2)

- [ ] **Service Level Agreement** — uptime targets, response time targets, support hours, escalation path, and credit/remedy for SLA breaches
- [ ] **Security requirements** — encryption standards, access controls, vulnerability management, penetration testing cadence
- [ ] **Data handling** — data classification acknowledgment, processing limitations, residency constraints, retention, return/deletion on termination
- [ ] **Breach notification** — timeline for notifying the organization of security incidents (Tier 1: ≤24 hours; Tier 2: ≤48 hours; Tier 3: ≤72 hours)
- [ ] **Right to audit** — the organization's right to audit or request evidence of vendor compliance (directly or via independent assessor)
- [ ] **Subprocessor controls** — advance notification of subprocessor changes, right to object, flow-down of security and privacy obligations
- [ ] **Business continuity** — vendor's DR/BCP capabilities, RTO/RPO commitments, and notification procedures for service disruptions
- [ ] **Quality criteria** — service acceptance criteria, defect or nonconformance thresholds, corrective-action expectations, and change notification duties for externally provided processes or services that affect customer outcomes
- [ ] **Termination assistance** — data export format, transition timeline, continued access during transition period
- [ ] **Insurance** — cyber liability insurance appropriate to the services and data handled

### 4.2 SLA Monitoring

- [ ] SLA metrics are tracked automatically where possible (uptime, response time, resolution time)
- [ ] SLA breaches are logged and trigger the escalation defined in the contract
- [ ] Service quality indicators are tracked for vendors that materially affect product or service quality (for example: defect escape, repeated nonconformance, missed acceptance criteria, chronic support-quality issues)
- [ ] SLA performance is reviewed at the cadence defined by the vendor's criticality tier (§2.2)
- [ ] Persistent SLA underperformance triggers vendor reassessment or replacement planning

---

## 5. Ongoing Monitoring & Review

### 5.1 Monitoring Activities

| Activity | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|----------|--------|--------|--------|--------|
| Attestation expiry tracking | Continuous | Continuous | Annual | On renewal |
| SLA / service quality monitoring | Continuous | Monthly | Quarterly | — |
| Security incident monitoring (vendor-side) | Continuous (via vendor status page, threat intel) | Monthly review | Annual review | — |
| Vendor financial health check | Semi-annual | Annual | — | — |
| Full reassessment | Annual | Annual | Biennial | On renewal |
| Vendor review meeting | Quarterly | Semi-annual | — | — |

### 5.2 Reassessment Triggers

Beyond scheduled reassessments, a vendor must be reassessed when:

- [ ] The vendor experiences a publicly disclosed security breach
- [ ] The vendor's attestation (SOC 2, ISO 27001) expires or is withdrawn
- [ ] The organization expands the vendor's scope (new data types, new integrations, higher-sensitivity use cases)
- [ ] The vendor undergoes a material change (acquisition, merger, leadership change, financial distress)
- [ ] The vendor changes its subprocessors or infrastructure providers
- [ ] The vendor shows repeated quality nonconformance, chronic delivery failure, or misses agreed acceptance criteria
- [ ] A risk management signal (work/signals/) identifies emerging vendor risk
- [ ] The vendor's AI model undergoes a major version change (for AI vendors)

### 5.3 Vendor Concentration Risk

- [ ] No single vendor provides more than one critical capability without a documented fallback or alternative
- [ ] Vendor concentration is tracked: for each critical capability, the number of available alternatives and switching cost is documented
- [ ] When concentration risk is identified (single vendor, no alternative, high switching cost), a mitigation plan is required — either contractual protections, escrow arrangements, or alternative vendor qualification

---

## 6. Vendor Offboarding

When a vendor relationship ends (contract termination, service migration, or vendor exit):

- [ ] All organizational data held by the vendor is returned or verifiably deleted (per data-classification.md deletion requirements)
- [ ] All credentials, API keys, and access tokens for the vendor are revoked
- [ ] The vendor's integration is deregistered from the Integration Registry and CONFIG.yaml
- [ ] The vendor's assessment record is updated with offboarding date and outcome
- [ ] For Tier 1 vendors: a 30-day transition plan is executed before final cutover
- [ ] For vendors processing personal data: deletion confirmation is obtained and retained as audit evidence (per log-retention.md audit log retention)

---

## 7. Integration with Existing Framework

### 7.1 Integration Registry Connection

The Integration Registry (org/integrations/) governs tool connections. This policy adds a vendor assessment layer:

- [ ] Before an integration is registered as `active`, the vendor behind it must have a completed security assessment at the appropriate tier
- [ ] The integration template includes a vendor assessment reference field (see updated `_TEMPLATE-integration.md`)
- [ ] Integration activation requires both technical validation (per existing checklist) and vendor risk approval

### 7.2 Agent-Specific Vendor Governance

Agents interact with vendors through integrations. Additional requirements:

- [ ] Agents must not activate or use unregistered integrations (AGENTS.md Rule 8) — this inherently prevents unassessed vendor usage
- [ ] When agents discover a need for a new integration, they file a signal — the signal triggers vendor assessment before integration registration
- [ ] Agent telemetry (`tool.execute` spans) for vendor API calls is retained per log-retention.md access log retention period and follows the canonical attribute contract in [`docs/otel-contract.md`](../../../docs/otel-contract.md)
- [ ] AI model provider changes (switching LLM, upgrading model version) require vendor reassessment if the new model or provider was not previously assessed

---

## 8. Deployment-Customizable Decisions

### Must Be Customized Per Instance / Deployment

- **Attestation requirements** — which certifications are required vs. recommended for each tier, based on industry (healthcare: HIPAA/HITRUST; government: FedRAMP; finance: PCI DSS/SOX)
- **Breach notification timelines** — the ≤24h/≤48h/≤72h defaults may need tightening based on contractual or regulatory obligations
- **Financial viability thresholds** — what constitutes acceptable financial health varies by organization size and risk appetite
- **Review cadence** — quarterly/semi-annual/annual defaults may need adjustment based on vendor volume and team capacity
- **Assessment questionnaire** — the template provides a baseline; adopters should extend with industry-specific questions (e.g., HIPAA security rule, PCI DSS requirements)
- **Vendor register tooling** — where vendor records are maintained (asset registry, dedicated GRC platform, or spreadsheet for smaller organizations)
- **AI vendor assessment depth** — how thoroughly fourth-party model providers are assessed depends on the organization's AI risk tier assignments (per ai-governance.md)

### Must Not Be Customized Away

- The four criticality tiers (tiers may be extended but not reduced)
- The requirement for security assessment before vendor onboarding
- Attestation requirement for Tier 1 and Tier 2 vendors (SOC 2 Type II or ISO 27001)
- Right-to-audit clause for Tier 1 and Tier 2 vendors
- Breach notification SLA in contracts
- Annual reassessment for Tier 1 and Tier 2 vendors
- Vendor offboarding data deletion verification
- AI vendor extended assessment when vendor provides AI/ML services

---

## 9. Cross-Policy Alignment

| Policy | What This Policy Provides |
|--------|--------------------------|
| **[Security Policy](security.md)** | Extends dependency security (§Data Protection) from code dependencies to vendor/supplier security assessment. Vendors must meet the same security standards applied internally. |
| **[Risk Management Policy](risk-management.md)** | Operationalizes SE-5 (supply chain compromise) prevention and extends §6.4 (Third-Party AI / Model Risk) to all vendor types. Vendor risks feed the risk register. |
| **[Privacy Policy](privacy.md)** | Connects vendor assessment to DPA requirements (§2). Subprocessor management operationalized through vendor lifecycle. |
| **[Data Classification Policy](data-classification.md)** | Vendor criticality tier is informed by the classification level of shared data. Vendor data handling capability is assessed against classification requirements. |
| **[Log Retention Policy](log-retention.md)** | Vendor assessment records and SLA monitoring data are retained as audit logs. Vendor API call telemetry follows access log retention. |
| **[Cryptography Policy](cryptography.md)** | Vendor encryption standards assessed against cryptography.md requirements. Vendor credential management follows key lifecycle policy. |
| **[AI Governance Policy](ai-governance.md)** | AI vendor assessment (§3.3) operationalizes model card, fairness, and explainability requirements for third-party AI systems. |
| **[Incident Response Policy](incident-response.md)** | Vendor breach notification SLAs feed incident detection and response. Vendor incidents are triaged per incident-response.md severity definitions. |
| **[Observability Policy](observability.md)** | Vendor SLA monitoring uses the observability platform. Integration health dashboards track vendor performance. |
| **[Delivery Policy](delivery.md)** | Vendor-provided services that affect shipped quality must have explicit acceptance criteria, release impact awareness, and corrective-action expectations. |
| **[Customer Policy](customer.md)** | Supplier performance is evaluated against the customer impact it creates, not just internal convenience or contract posture. |
| **Integration Registry** (`org/integrations/`) | Vendor assessment is a prerequisite for integration activation. Assessment reference field added to integration template. |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Vendor tier assignment | All active vendors assigned a criticality tier | Active vendors without tier assignment |
| Security assessment | All Tier 1–3 vendors have a current assessment record | Vendors onboarded without assessment, or assessments expired without reassessment |
| Attestation verification | Tier 1–2 vendors have current SOC 2 Type II or ISO 27001; scope covers services used | Tier 1–2 vendors without required attestation, or attestation scope mismatch |
| Contract coverage | Tier 1–2 vendor contracts include SLA, breach notification, right-to-audit, data handling | Missing mandatory contract clauses for Tier 1–2 vendors |
| Monitoring cadence | Vendors monitored at the cadence defined by their tier | Monitoring lapsed or never established |
| Quality performance | Vendors that materially affect product/service quality have defined quality criteria and are monitored against them | Supplier quality materially affects outcomes but no quality criteria or review evidence exists |
| AI vendor assessment | AI/ML vendors assessed with extended AI-specific questions (§3.3) | AI vendors assessed with standard-only questionnaire |
| Concentration risk | Critical capabilities have documented alternatives or mitigation plans | Single-vendor dependency for critical capability with no mitigation |
| Offboarding | Terminated vendors have data deletion verification and credential revocation | Vendor access persists after relationship ends |

---

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **ISO 27001:2022** | A.5.19 Information security in supplier relationships | §1, §2, §3 |
| **ISO 27001:2022** | A.5.20 Addressing information security within supplier agreements | §4 |
| **ISO 27001:2022** | A.5.21 Managing information security in the ICT supply chain | §3.3 (AI/fourth-party), §5.3 (concentration) |
| **ISO 27001:2022** | A.5.22 Monitoring, review and change management of supplier services | §5 |
| **ISO 27001:2022** | A.5.23 Information security for use of cloud services | §3.2 (data handling domain), §4.1 (residency) |
| **SOC 2** | CC9.1 Risk mitigation — vendor risk identification | §1, §3 |
| **SOC 2** | CC9.2 Vendor and business partner risk management | §2, §5 |
| **SOC 2** | CC3.1 Risk identification — suppliers as threat source | §3.2 (security posture domain) |
| **ISO 9001:2015** | 8.4.1 Control of externally provided processes, products and services | §2.2, §3.2 (quality & conformity), §4, §5 |
| **GDPR** | Art. 28 Processor obligations and subprocessor controls | §2.2 (DPA row), §4.1 (subprocessor clause) |
| **GDPR** | Art. 44–49 International transfers | §3.2 (data handling — residency, cross-border) |
| **EU AI Act** | Art. 26–28 Deployer obligations for third-party AI | §3.3 (AI vendor assessment) |
| **NIST SP 800-53** | SA-9 External information system services | §2, §3 |
| **NIST SP 800-53** | SR-1 through SR-6 Supply chain risk management | §5.3 (concentration), §3 (assessment) |
| **NIST AI RMF** | MAP 5.1, MANAGE 3.1 Third-party AI risk | §3.3 (AI vendor assessment) |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-03-16 | Added supplier quality and conformity requirements alongside security/risk controls: quality assessment domain, contract quality criteria, service-quality monitoring, reassessment triggers for chronic nonconformance, delivery/customer cross-policy alignment, and ISO 9001 clause 8.4.1 mapping |
| 1.0.1 | 2026-03-15 | Added explicit docs/otel-contract.md reference for vendor API call telemetry requirements (#115) |
| 1.0 | 2026-03-14 | Initial version — 4-tier vendor criticality model, full lifecycle governance (identification → assessment → onboarding → monitoring → offboarding), security assessment framework with 7 domains, AI vendor extended assessment, SLA and contract requirements, attestation verification (SOC 2 Type II / ISO 27001), concentration risk tracking, integration registry connection, compliance mapping (ISO 27001 A.5.19–A.5.23 / SOC 2 CC9 / GDPR Art. 28 / EU AI Act Art. 26–28 / NIST SP 800-53 SA-9, SR / NIST AI RMF). Closes #92. |
