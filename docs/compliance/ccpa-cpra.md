# CCPA/CPRA — Compliance Reference

> **Regulation:** California Consumer Privacy Act (Cal. Civ. Code §§ 1798.100–1798.199.100), as amended by the California Privacy Rights Act (Proposition 24, 2020)
> **Scope:** Businesses meeting revenue/data thresholds that collect or process personal information of California residents
> **Official source:** [California Legislative Information — CCPA/CPRA](https://leginfo.legislature.ca.gov/faces/codes_displayexpandedbranch.xhtml?tocCode=CIV&division=3.&title=1.81.5.&part=4.)
> **Enforcement authority:** California Privacy Protection Agency (CPPA); California Attorney General

## 1. What CCPA/CPRA Requires

CCPA (effective January 2020) established baseline consumer privacy rights for California residents. CPRA (effective January 2023) significantly expanded those rights, created a dedicated enforcement agency, and introduced new obligations for businesses handling sensitive personal information.

| Area | Focus | Key Sections |
|------|-------|-------------|
| **Consumer right to know** | Consumers can request categories and specific pieces of PI collected about them | §1798.100, §1798.110 |
| **Right to delete** | Consumers can request deletion of PI, with defined exceptions | §1798.105 |
| **Right to correct** | Consumers can request correction of inaccurate PI (CPRA addition) | §1798.106 |
| **Right to opt-out of sale/sharing** | Consumers can direct a business not to sell or share their PI; "Do Not Sell or Share My Personal Information" link required | §1798.120, §1798.135 |
| **Right to limit use of sensitive PI** | Consumers can limit use and disclosure of sensitive PI to specified purposes | §1798.121 |
| **Non-discrimination** | Businesses cannot discriminate against consumers who exercise their rights | §1798.125 |
| **Financial incentive disclosure** | Businesses offering financial incentives for data collection must disclose terms and obtain opt-in | §1798.125(b) |
| **Service provider / contractor obligations** | Contractual requirements for entities processing PI on behalf of a business | §1798.100(d), §1798.140(ag), (j) |
| **Reasonable security** | Businesses must implement reasonable security procedures and practices | §1798.100(e), §1798.150 (private right of action for breaches from inadequate security) |
| **Privacy risk assessments** | Required for processing that presents significant risk to consumer privacy (CPRA addition) | §1798.185(a)(15) |
| **Automated decision-making** | Consumers' right to opt out of automated decision-making technology and right to information about its use (CPRA addition) | §1798.185(a)(16) |
| **Annual cybersecurity audits** | Required for businesses whose processing presents significant risk (CPRA addition) | §1798.185(a)(15) |

## 2. How This Framework Addresses It

### Section-Level Mapping

| Section | Requirement | Framework Implementation | Evidence Source |
|---------|-------------|-------------------------|-----------------|
| **§1798.100** | Right to know / disclosure at collection | [Privacy Policy](../../org/4-quality/policies/privacy.md) §1 — purpose documentation per data processing activity; notice-at-collection requirements | Processing records in Git |
| **§1798.105** | Right to delete | Privacy Policy §3 — DSAR runbook with deletion workflow including identity verification, search, deletion, and confirmation | DSAR OTel events (intake→verification→fulfillment→closure) |
| **§1798.106** | Right to correct | Privacy Policy §3 — DSAR runbook includes correction pathway with accuracy verification | Correction workflow OTel spans |
| **§1798.110** | Right to know (categories and specific pieces) | Privacy Policy §3 — DSAR access request workflow; [Data Classification Policy](../../org/4-quality/policies/data-classification.md) — PI categorization | DSAR response audit logs |
| **§1798.120** | Right to opt-out of sale/sharing | **Gap — deployment-specific** — framework does not implement opt-out mechanism (see §4 below) | N/A |
| **§1798.121** | Right to limit use of sensitive PI | Data Classification — RESTRICTED level for sensitive PI; [Agent Security Policy](../../org/4-quality/policies/agent-security.md) — access controls | `data.classification` span attributes |
| **§1798.125** | Non-discrimination + financial incentives | Privacy Policy §1 — principle of non-discrimination documented; financial incentive disclosure is **gap** | Policy artifacts |
| **§1798.135** | "Do Not Sell or Share" link requirement | **Gap — deployment-specific** — framework does not implement UI elements | N/A |
| **§1798.100(d)** | Service provider contracts | Privacy Policy §2 — DPA template with processing restrictions; [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — subprocessor controls and contractual requirements | DPA artifacts, vendor assessment records |
| **§1798.100(e)** | Reasonable security measures | [Security Policy](../../org/4-quality/policies/security.md) — access controls, authentication, secure development; [Cryptography Policy](../../org/4-quality/policies/cryptography.md) — encryption at rest/transit | Security audit trails, KMS logs |
| **§1798.150** | Private right of action (breach from inadequate security) | [Incident Response Policy](../../org/4-quality/policies/incident-response.md) — breach detection, triage, notification; Security Policy — preventive controls | Breach timeline OTel spans |
| **§1798.185(a)(15)** | Privacy risk assessments | Privacy Policy §5 — DPIA required before high-risk processing; partially covers CPRA risk assessment mandate | DPIA decision records |
| **§1798.185(a)(16)** | Automated decision-making transparency + opt-out | Agent Security Policy — automated decision safeguards; [AI Governance Policy](../../org/4-quality/policies/ai-governance.md) — explainability requirements; `governance.decision` OTel events document reasoning | `governance.decision` span events |
| **§1798.185(a)(15)** | Annual cybersecurity audit (high-risk processing) | **Gap** — framework provides security controls but not a formal annual audit programme | N/A |

### Cross-Cutting Framework Controls

| CCPA/CPRA Theme | Framework Mechanisms |
|-----------------|---------------------|
| **Accountability & auditability** | Git-based governance (PR approval trail), OTel telemetry for every agent action, `governance.decision` events |
| **Data inventory** | Data Classification Policy — classification levels (PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED) with handling rules per level |
| **Data minimization** | Data Classification Policy — least-privilege data access; [Log Retention Policy](../../org/4-quality/policies/log-retention.md) — bounded retention with verified deletion |
| **Breach response** | Incident Response Policy — detection→triage→containment→notification; Privacy Policy §4 — notification timelines and communication |
| **Vendor oversight** | Vendor Risk Management Policy — risk-tiered assessments, contractual controls, ongoing monitoring |
| **Automated decision safeguards** | Agent Security Policy — human-in-the-loop requirements; AI Governance Policy — explainability, fairness evaluation; AGENTS.md Rule 2 ("Humans decide, agents recommend") |

## 3. Where Observability Provides Evidence

CCPA/CPRA enforcement increasingly requires demonstrable compliance — the ability to show what data was accessed, when, by whom, and for what purpose. The framework's observability architecture provides this evidence:

| CCPA/CPRA Evidence Need | Observability Source | Relevant Section |
|-------------------------|---------------------|------------------|
| PI access logging | Agent spans with `data.classification` attributes on every tool call accessing data | §1798.100 |
| DSAR response tracking and SLA compliance | DSAR workflow OTel events with timestamps: intake→identity verification→search→fulfillment→closure (45-day deadline tracking) | §1798.105, §1798.106, §1798.110 |
| Deletion verification | Deletion confirmation audit logs with `data.action: delete` spans | §1798.105 |
| Purpose limitation enforcement | Agent spans showing documented purpose for each data processing activity | §1798.100 |
| Security measure effectiveness | Encryption verification spans, access control audit trails, authentication event logs | §1798.100(e), §1798.150 |
| Breach detection and response timeline | Incident OTel spans: detection→awareness→triage→containment→notification (timeline reconstruction) | §1798.150 |
| Automated decision-making transparency | `governance.decision` span events recording decision rationale, inputs, and outcome | §1798.185(a)(16) |
| Vendor data processing oversight | Vendor assessment records, DPA monitoring, subprocessor audit trails | §1798.100(d) |
| Risk assessment evidence | `governance.decision` events for high-risk processing gates, DPIA decision records | §1798.185(a)(15) |

## 4. Adopter Responsibilities

| Requirement | CCPA/CPRA Requirement | What's Needed | Criticality |
|-----|----------------------|---------------|-------------|
| **"Do Not Sell or Share" opt-out mechanism** | §1798.120, §1798.135 | Runtime opt-out UI ("Do Not Sell or Share My Personal Information" link), opt-out signal recognition (GPC), backend enforcement of opt-out state per consumer — entirely deployment-specific | **High** |
| **Sensitive Personal Information handling controls** | §1798.121 | Explicit SPI categorization (SSN, financial accounts, precise geolocation, racial/ethnic origin, etc.) mapped to CCPA/CPRA definition; consumer-facing "Limit Use" mechanism — partially covered by Data Classification Policy's RESTRICTED level but needs CCPA-specific SPI taxonomy | **High** |
| **Privacy risk assessment (California-style)** | §1798.185(a)(15) | CPPA-defined risk assessment format when final regulations are issued; DPIA process in Privacy Policy partially covers this but may need California-specific adaptations | **Medium** |
| **Annual cybersecurity audit** | §1798.185(a)(15) | Formal annual audit programme for businesses engaged in high-risk processing; framework provides controls but not audit scheduling, scope definition, or independent review | **Medium** |
| **Financial incentive disclosure** | §1798.125(b) | Terms disclosure and opt-in mechanism for loyalty programmes or other financial incentives offered in exchange for PI — deployment-specific, rarely applicable | **Low** |

**Addressed by framework:** "Do Not Sell or Share" opt-out mechanism ([guide](guides/ccpa-cpra-opt-out.md)), Sensitive Personal Information handling controls ([guide](guides/ccpa-cpra-sensitive-pi.md)).

## 5. External References

- [CCPA/CPRA Full Text (California Legislative Information)](https://leginfo.legislature.ca.gov/faces/codes_displayexpandedbranch.xhtml?tocCode=CIV&division=3.&title=1.81.5.&part=4.) — Official statute text
- [California Privacy Protection Agency (CPPA)](https://cppa.ca.gov/) — Enforcement authority and rulemaking
- [CPPA Final Regulations](https://cppa.ca.gov/regulations/) — Implementing regulations (ongoing rulemaking)
- [California AG — CCPA Resources](https://oag.ca.gov/privacy/ccpa) — Attorney General guidance and enforcement actions
- [GDPR Compliance Reference](gdpr.md) — Significant overlap; many GDPR controls satisfy CCPA/CPRA equivalents
- [IAPP CCPA/CPRA Resource Center](https://iapp.org/resources/topics/ccpa-and-cpra/) — Practitioner guidance and analysis
