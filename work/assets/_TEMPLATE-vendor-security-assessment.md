# Vendor Security Assessment: {{VENDOR_NAME}}

> **Vendor:** {{VENDOR_NAME}}
> **Service:** {{SERVICE_DESCRIPTION}}
> **Criticality Tier:** {{1 / 2 / 3 / 4}} _(per vendor-risk-management.md §1)_
> **Assessor:** {{ASSESSOR_NAME_OR_AGENT}}
> **Assessment Date:** {{YYYY-MM-DD}}
> **Next Reassessment:** {{YYYY-MM-DD}}
> **Overall Rating:** {{PASS / CONDITIONAL / FAIL}}

---

## 1. Vendor Information

| Field | Value |
|-------|-------|
| **Legal entity name** | |
| **Headquarters location** | |
| **Service(s) in scope** | |
| **Data classification of shared data** | _(PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED — per data-classification.md)_ |
| **Contains PII** | _(yes / no — if yes, DPA required per privacy.md §2)_ |
| **Integration Registry ID** | _(link to integration registration, if applicable)_ |
| **Contract reference** | _(link to vendor agreement)_ |
| **AI/ML vendor** | _(yes / no — if yes, complete §7 AI-Specific Assessment)_ |

---

## 2. Attestations & Certifications

| Certification | Status | Scope Covers Our Use? | Expiry Date | Notes |
|--------------|--------|----------------------|-------------|-------|
| SOC 2 Type II | _(current / expired / not held)_ | _(yes / partial / no)_ | | |
| SOC 2 Type I | _(current / expired / not held)_ | _(yes / partial / no)_ | | |
| ISO 27001 | _(current / expired / not held)_ | _(yes / partial / no)_ | | |
| ISO 42001 (AI) | _(current / expired / not held / N/A)_ | _(yes / partial / no)_ | | |
| FedRAMP | _(current / expired / not held / N/A)_ | _(yes / partial / no)_ | | |
| HIPAA / HITRUST | _(current / expired / not held / N/A)_ | _(yes / partial / no)_ | | |
| PCI DSS | _(current / expired / not held / N/A)_ | _(yes / partial / no)_ | | |
| Other: _________ | | | | |

**Attestation review notes:** _(qualified opinions, exceptions, control deficiencies from SOC 2 report, bridge letter status)_

---

## 3. Security Posture _(Tier 1–3)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 3.1 | Does the vendor encrypt data at rest using AES-256 or equivalent? | | | |
| 3.2 | Does the vendor enforce TLS 1.2+ (TLS 1.3 preferred) for all data in transit? | | | |
| 3.3 | Does the vendor implement role-based access control (RBAC) with least privilege? | | | |
| 3.4 | Does the vendor require MFA for administrative access? | | | |
| 3.5 | Does the vendor conduct regular penetration testing (at least annually)? | | | |
| 3.6 | Does the vendor have a vulnerability management program with defined SLAs for patching (critical: ≤72h)? | | | |
| 3.7 | Does the vendor have a documented incident response plan with defined notification timelines? | | | |
| 3.8 | Does the vendor maintain security logging and monitoring (audit trails, SIEM, anomaly detection)? | | | |
| 3.9 | Does the vendor perform background checks on personnel with access to customer data? | | | |
| 3.10 | Does the vendor have a secure software development lifecycle (SDLC) with code review and testing? | | | |

---

## 4. Data Handling _(Tier 1–3)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 4.1 | Where is data stored geographically? Does the vendor support data residency requirements? | | | |
| 4.2 | Does data cross international borders? If so, what transfer mechanisms are used (SCCs, adequacy decisions, BCRs)? | | | |
| 4.3 | Can the vendor classify and handle data at the classification level required by our data-classification.md? | | | |
| 4.4 | Does the vendor have defined data retention and deletion procedures? | | | |
| 4.5 | Can the vendor provide verified data deletion (cryptographic erasure or certified destruction) on contract termination? | | | |
| 4.6 | Does the vendor maintain backups? Are backups encrypted with separate key management? | | | |
| 4.7 | Can the vendor export all organizational data in a standard format on request? | | | |

---

## 5. Privacy & Subprocessor Management _(Tier 1–3 if PII involved)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 5.1 | Does the vendor maintain a current list of subprocessors and provide advance notice of changes? | | | |
| 5.2 | Is the vendor willing to sign our DPA (or does their DPA meet our requirements per privacy.md §2)? | | | |
| 5.3 | Can the vendor support DSAR fulfillment (access, correction, deletion, portability) within required timelines? | | | |
| 5.4 | Does the vendor have a personal data breach notification process with defined timelines? | | | |
| 5.5 | Does the vendor use customer data for purposes beyond the contracted service (analytics, training, marketing)? | | | |

---

## 6. Operational Resilience _(Tier 1–2)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 6.1 | What is the vendor's uptime SLA? | | | |
| 6.2 | Does the vendor have a documented DR/BCP plan with defined RTO and RPO? | | | |
| 6.3 | When was the vendor's DR plan last tested? | | | |
| 6.4 | Does the vendor provide advance notification of planned maintenance and breaking changes? | | | |
| 6.5 | What is the vendor's support model (24/7, business hours, tiered)? | | | |
| 6.6 | What is the vendor's escalation path for critical issues? | | | |

---

## 7. AI-Specific Assessment _(if AI/ML vendor)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 7.1 | Does the vendor have documented model governance (lifecycle management, validation, monitoring, retirement)? | | | |
| 7.2 | Can the vendor describe training data sources and consent mechanisms? Is customer data used for training? | | | |
| 7.3 | Does the vendor test for and report on model bias and fairness? What metrics are used? | | | |
| 7.4 | Has the vendor tested for adversarial attacks (prompt injection, data poisoning, model extraction)? | | | |
| 7.5 | Can the vendor provide explanations for model decisions at a level appropriate to the use case? | | | |
| 7.6 | Does the vendor use upstream model providers (fourth parties)? If so, which? | | | |
| 7.7 | Does the vendor pin model versions? What is the notification period for model changes or deprecations? | | | |
| 7.8 | Where does inference processing occur? Does input/output data leave the contracted region? | | | |
| 7.9 | Does the vendor hold or pursue ISO 42001 (AI Management System) certification? | | | |

---

## 8. Financial Viability _(Tier 1–2)_

| # | Question | Response | Evidence | Rating |
|---|----------|----------|----------|--------|
| 8.1 | Is the vendor publicly traded or independently audited? | | | |
| 8.2 | Are there going-concern indicators (layoffs, funding issues, pending litigation, acquisition rumors)? | | | |
| 8.3 | Does the vendor offer source code escrow or data escrow arrangements? | | | |

---

## 9. Assessment Summary

### Risk Findings

| # | Finding | Severity | Domain | Mitigation / Remediation | Status |
|---|---------|----------|--------|--------------------------|--------|
| 1 | | _(critical / high / medium / low)_ | | | _(open / mitigated / accepted)_ |
| 2 | | | | | |

### Concentration Risk

| Field | Value |
|-------|-------|
| **Capability provided** | |
| **Alternative vendors available** | _(count + names)_ |
| **Estimated switching cost** | _(low / medium / high)_ |
| **Concentration risk level** | _(low / medium / high — high if sole provider of critical capability)_ |
| **Mitigation plan** | _(if concentration risk is medium or high)_ |

### Overall Assessment

| Field | Value |
|-------|-------|
| **Overall rating** | _(PASS / CONDITIONAL / FAIL)_ |
| **Conditions** | _(if CONDITIONAL: list required mitigations and deadlines)_ |
| **Approved by** | |
| **Approval date** | |
