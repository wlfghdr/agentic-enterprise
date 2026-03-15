<!-- placeholder-ok -->
# HIPAA — PHI-Specific Data Classification Mapping

> **Implements:** PHI-specific data classification with de-identification standards
> **Regulation:** HIPAA (45 CFR §160.103, §164.502, §164.514)
> **Severity:** High — correct PHI identification and classification is foundational to all HIPAA compliance
> **Related issue:** [#145](https://github.com/wlfghdr/agentic-enterprise/issues/145)
> **Related compliance doc:** [HIPAA Compliance Reference](../hipaa.md)

---

## 1. Purpose

HIPAA defines Protected Health Information (PHI) broadly and establishes specific handling requirements based on the form of PHI (oral, written, electronic). This guide extends the framework's [Data Classification Policy](../../../org/4-quality/policies/data-classification.md) with explicit PHI and ePHI categories, enumerates the 18 HIPAA identifiers, and addresses the two permitted de-identification methods (Safe Harbor and Expert Determination).

This guide provides PHI-to-classification-level mappings, de-identification standards, and agent-specific PHI handling requirements including prompt sanitization, response filtering, and log redaction.

---

## 2. PHI Definition and the 18 HIPAA Identifiers

### 2a. What Constitutes PHI

Protected Health Information (PHI) is individually identifiable health information that is created, received, maintained, or transmitted by a Covered Entity or Business Associate. PHI includes information that:

1. Relates to the past, present, or future physical or mental health or condition of an individual;
2. Relates to the provision of health care to an individual; or
3. Relates to the past, present, or future payment for the provision of health care to an individual;

AND identifies the individual or provides a reasonable basis to believe the individual can be identified.

| PHI Form | Definition | HIPAA Term |
|----------|-----------|------------|
| **Written PHI** | PHI in paper or documentary form | PHI |
| **Oral PHI** | PHI communicated verbally | PHI |
| **Electronic PHI (ePHI)** | PHI created, received, maintained, or transmitted in electronic form | ePHI — subject to Security Rule (45 CFR Part 164, Subpart C) |

### 2b. The 18 HIPAA Identifiers (§164.514(b)(2))

The following 18 identifiers, when associated with health information, create PHI. Under the Safe Harbor de-identification method, all 18 must be removed.

| # | Identifier | Examples | Sensitivity |
|---|-----------|----------|-------------|
| 1 | **Names** | Full name, maiden name, alias | High |
| 2 | **Geographic data** (smaller than state) | Street address, city, county, ZIP code (first 3 digits may be retained if population > 20,000) | High |
| 3 | **Dates** (except year) related to an individual | Birth date, admission date, discharge date, date of death; all ages over 89 | High |
| 4 | **Telephone numbers** | Home, mobile, work phone numbers | High |
| 5 | **Fax numbers** | Fax machine numbers | High |
| 6 | **Email addresses** | Personal or work email | High |
| 7 | **Social Security Numbers** | SSN | Critical |
| 8 | **Medical record numbers** | MRN, chart numbers | High |
| 9 | **Health plan beneficiary numbers** | Insurance member ID, group numbers | High |
| 10 | **Account numbers** | Financial account numbers | High |
| 11 | **Certificate/license numbers** | Driver's license, professional license | High |
| 12 | **Vehicle identifiers and serial numbers** | VIN, license plate numbers | Medium |
| 13 | **Device identifiers and serial numbers** | Medical device UDIs, serial numbers | Medium |
| 14 | **Web URLs** | Personal web pages, patient portal URLs | Medium |
| 15 | **IP addresses** | Network addresses associated with individuals | Medium |
| 16 | **Biometric identifiers** | Fingerprints, voiceprints, retinal scans | Critical |
| 17 | **Full-face photographs** | Photos and comparable images | High |
| 18 | **Any other unique identifying number, characteristic, or code** | Catch-all for other identifiers not listed above | Varies |

---

## 3. Mapping PHI to Framework Data Classification Levels

The framework's Data Classification Policy defines classification levels. PHI maps to these levels as follows:

| Framework Classification Level | PHI Category | Examples | Handling Requirements |
|-------------------------------|-------------|----------|----------------------|
| **CRITICAL** | PHI with SSN, biometric identifiers, or genetic information | SSN + diagnosis, biometric data + treatment record | Encryption at rest and in transit (AES-256 / TLS 1.3), access logging, no agent processing without explicit authorization, immediate breach notification |
| **CONFIDENTIAL** | Standard PHI — health information with any of the 18 identifiers | Patient name + diagnosis, MRN + treatment plan, email + prescription | Encryption at rest and in transit, role-based access control, minimum necessary enforcement, 60-day breach notification |
| **CONFIDENTIAL** | ePHI — electronic PHI subject to Security Rule | Any PHI in electronic form | All CONFIDENTIAL handling plus Security Rule administrative, physical, and technical safeguards |
| **INTERNAL** | De-identified health information (Safe Harbor or Expert Determination) | Aggregate health statistics, de-identified datasets | Standard internal handling — no longer PHI under HIPAA, but re-identification risk must be monitored |
| **INTERNAL** | Limited Data Set (§164.514(e)) | Health information with direct identifiers removed but retaining dates, ZIP codes, ages | Requires Data Use Agreement (DUA); not fully de-identified |

### 3a. Classification Decision Tree

```
Does the data relate to health, healthcare, or payment for healthcare?
├── No  → Not health information → classify per standard Data Classification Policy
└── Yes → Is the data individually identifiable?
    ├── No  → Not PHI → classify as INTERNAL (de-identified health data)
    └── Yes → PHI detected
        ├── Contains SSN, biometric, or genetic data?
        │   ├── Yes → classify as CRITICAL
        │   └── No  → classify as CONFIDENTIAL
        └── Is the PHI in electronic form?
            └── Yes → also subject to Security Rule (ePHI)
```

---

## 4. ePHI Handling Requirements

Electronic PHI triggers the full HIPAA Security Rule. The following requirements apply in addition to the framework's standard CONFIDENTIAL-level handling.

| Safeguard Category | Requirement | Framework Implementation |
|-------------------|-------------|-------------------------|
| **Administrative** | Risk analysis covering all ePHI systems | [Risk Management Policy](../../../org/4-quality/policies/risk-management.md) — scope to all ePHI repositories |
| **Administrative** | Workforce access authorization | `CODEOWNERS` + [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) tool-level access controls |
| **Administrative** | Security incident procedures | [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) with HIPAA-specific escalation |
| **Administrative** | Contingency plan (backup, DR, emergency mode) | [Availability Policy](../../../org/4-quality/policies/availability.md) with ePHI-specific RTO/RPO |
| **Technical** | Access control — unique user ID | [Security Policy](../../../org/4-quality/policies/security.md) — identity verification, short-lived tokens |
| **Technical** | Audit controls | [Observability Policy](../../../org/4-quality/policies/observability.md) — OTel spans for all ePHI access |
| **Technical** | Integrity controls | Git-based governance, cryptographic hashing |
| **Technical** | Transmission security — encryption | [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) — TLS 1.3, mTLS for service-to-service |
| **Technical** | Encryption at rest | Cryptography Policy — AES-256 for ePHI at rest |
| **Physical** | Facility access controls | Deployment-specific — document in deployment runbook |
| **Physical** | Device and media controls | Deployment-specific — document disposal and reuse procedures |

---

## 5. De-identification Standards

HIPAA provides two methods for de-identifying PHI. Once properly de-identified, data is no longer PHI and is not subject to HIPAA requirements.

### 5a. Safe Harbor Method (§164.514(b))

Remove all 18 identifiers listed in Section 2b from the data and ensure the Covered Entity has no actual knowledge that the remaining information could identify an individual.

| Requirement | Detail |
|-------------|--------|
| **Remove all 18 identifiers** | Every instance of every identifier must be removed or generalized |
| **No actual knowledge** | CE/BA must not have actual knowledge that remaining data could identify an individual |
| **ZIP code exception** | First 3 digits of ZIP may be retained if the geographic unit contains > 20,000 persons; otherwise replace with 000 |
| **Age exception** | Ages over 89 must be aggregated into a single "90+" category |
| **Re-identification code** | A code may be assigned for re-identification purposes, but: (a) the code must not be derived from the individual's information, (b) the code must not be translatable back to the individual, and (c) the CE/BA must not use or disclose the code for other purposes or disclose the re-identification mechanism |

### 5b. Expert Determination Method (§164.514(a))

A qualified statistical or scientific expert determines that the risk of identifying an individual from the data is very small.

| Requirement | Detail |
|-------------|--------|
| **Qualified expert** | Person with appropriate knowledge of accepted statistical and scientific principles and methods for rendering information not individually identifiable |
| **Expert determination** | Expert applies principles and methods and determines risk is very small that the data could be used, alone or in combination with other reasonably available information, to identify an individual |
| **Documentation** | Expert documents methods and results of the analysis |
| **Accepted methods** | K-anonymity, l-diversity, t-closeness, differential privacy, and other statistical disclosure limitation techniques |

### 5c. De-identification Verification

| Check | Safe Harbor | Expert Determination |
|-------|------------|---------------------|
| All 18 identifiers removed/generalized | Required | N/A — expert determines scope |
| No actual knowledge of re-identification | Required | N/A — expert assesses risk |
| Expert qualification documented | N/A | Required |
| Statistical methodology documented | N/A | Required |
| Re-identification risk assessment | Implicit (18 identifiers removed) | Explicit (very small risk) |
| Periodic re-assessment | Recommended | Required (as data environment changes) |

---

## 6. Agent-Specific PHI Handling

AI and agent systems present unique risks for PHI exposure. The following controls must be implemented when agents process, access, or generate content involving PHI.

### 6a. Prompt Sanitization

| Control | Implementation | Verification |
|---------|---------------|-------------|
| **PHI detection in prompts** | Scan all prompts and context inputs for the 18 HIPAA identifiers before processing | Automated regex/NLP scanning with logging |
| **Minimum necessary enforcement** | Include only the PHI elements essential to the task — strip unnecessary identifiers | Task-specific PHI allowlists |
| **Prompt logging redaction** | If prompts are logged for debugging or telemetry, redact PHI before storage | OTel span attribute filtering with `privacy.redact_by_default: true` |
| **Context window limits** | Limit the volume of PHI in a single prompt/context window to the minimum necessary | Configuration-enforced context size limits for PHI-containing requests |

### 6b. Response Filtering

| Control | Implementation | Verification |
|---------|---------------|-------------|
| **PHI in outputs** | Scan agent outputs for unintended PHI disclosure before returning to the requester | Post-processing filter for 18 identifiers |
| **Output audience verification** | Verify the requester is authorized to receive the PHI in the output | Role-based access control check before output delivery |
| **Output logging** | Log outputs containing PHI with the same protections as input PHI | Encrypted log storage, access-controlled |
| **Hallucinated PHI** | Monitor for agent outputs that fabricate PHI-like data (false patient information) | Output validation against source records |

### 6c. Log Redaction

| Log Type | PHI Risk | Redaction Requirement |
|----------|---------|----------------------|
| **OTel spans/traces** | Span attributes may contain PHI from prompts, tool calls, or outputs | Redact all 18 identifiers from span attributes; use `data.classification: phi` tag without including actual PHI values |
| **Application logs** | Error messages, debug output may echo PHI | Structured logging with PHI-aware formatters that mask identifiers |
| **Audit logs** | Access logs should record who accessed what PHI, not the PHI itself | Log access events with record IDs, not record contents |
| **Model interaction logs** | Full prompt/response logs for AI systems | Store in ePHI-classified storage with encryption and access controls, or redact before storage |

### 6d. Minimum Necessary Standard for Agents

The minimum necessary standard (§164.502(b)) requires that PHI use and disclosure be limited to the minimum necessary to accomplish the intended purpose. For agent systems:

| Principle | Agent Implementation |
|-----------|---------------------|
| **Role-based PHI access** | Configure agent tool permissions to restrict PHI access to only the data elements needed for the specific task |
| **Task-scoped PHI retrieval** | When agents query PHI data stores, queries must be scoped to the specific records needed — no broad PHI dumps |
| **Ephemeral PHI processing** | PHI should not persist in agent memory, context, or cache beyond the duration of the specific task |
| **PHI access justification** | Every agent access to PHI should include a purpose code in the OTel span (`phi.access.purpose`) |

---

## 7. Verification Checklist

### PHI Identification and Classification
- [ ] All systems creating, receiving, maintaining, or transmitting PHI are inventoried
- [ ] PHI data flows mapped across all systems (including agent systems)
- [ ] All 18 HIPAA identifiers recognized in classification rules
- [ ] PHI mapped to CRITICAL or CONFIDENTIAL classification levels
- [ ] ePHI systems identified and subject to Security Rule safeguards
- [ ] Limited Data Sets identified and governed by Data Use Agreements

### De-identification
- [ ] De-identification method selected (Safe Harbor or Expert Determination)
- [ ] Safe Harbor: all 18 identifiers removed and no actual knowledge of re-identification
- [ ] Expert Determination: qualified expert engaged, methodology documented, risk assessed as very small
- [ ] De-identified datasets classified as INTERNAL (no longer PHI)
- [ ] Re-identification risk monitoring established
- [ ] Re-identification codes (if used) protected per §164.514(c)

### Agent-Specific Controls
- [ ] Prompt sanitization implemented — PHI detection before processing
- [ ] Minimum necessary standard enforced in agent PHI access
- [ ] Response filtering implemented — PHI detection in outputs
- [ ] Log redaction configured — PHI stripped from OTel spans, application logs, and debug output
- [ ] `privacy.redact_by_default: true` configured for PHI-related telemetry
- [ ] PHI access purpose codes included in OTel spans (`phi.access.purpose`)
- [ ] Ephemeral PHI processing verified — no PHI persistence beyond task scope
- [ ] Agent tool permissions scoped to minimum necessary PHI elements
- [ ] Hallucinated PHI detection controls in place

### Operational
- [ ] Data Classification Policy updated with PHI and ePHI categories
- [ ] Classification decision tree documented and accessible to all agents and workforce
- [ ] PHI handling training completed for workforce (see [Workforce Training Guide](hipaa-workforce-training.md))
- [ ] Periodic PHI classification review scheduled (at least annually)
- [ ] PHI inventory reconciled with BAA inventory (all BA PHI access covered by BAA)
