# Data Classification & Handling Policy

> **Applies to:** All organizational data assets, storage systems, processing pipelines, agent workflows, integrations, and outputs
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team
> **Version:** 1.0.1 | **Last updated:** 2026-03-14

---

## Principles

1. **Classify before you process** — No data is stored, transmitted, or processed without a classification. Unclassified data is treated as a gap, not as low-risk.
2. **Handling follows classification** — Encryption, access controls, retention, and deletion requirements are determined by the classification level, not by ad-hoc decisions.
3. **Least privilege by default** — When classification is uncertain, apply the higher level until the data owner confirms. Downgrading requires documented justification.
4. **Inventory is continuous** — Data classification is not a one-time exercise. New data sources, integrations, and agent workflows trigger classification review.
5. **Separation of concerns** — The person or agent that classifies data is not the sole authority on handling exceptions. Exceptions require governance approval.

---

## 1. Classification Scheme

All organizational data must be assigned one of the following four levels. Adopters may add intermediate levels but must not remove these four.

| Level | Label | Definition | Examples |
|-------|-------|-----------|----------|
| **1** | **PUBLIC** | Information intended for or safe for unrestricted disclosure. No confidentiality requirement. | Published docs, open-source code, marketing materials, public API specs |
| **2** | **INTERNAL** | Information for organizational use only. Disclosure would not cause significant harm but is not intended for external audiences. | Internal process docs, non-sensitive meeting notes, internal tooling configs, org charts |
| **3** | **CONFIDENTIAL** | Sensitive information whose disclosure could cause material harm to the organization, its customers, or individuals. Includes all personal data (PII) by default. | Customer PII, financial records, contracts, credentials, security configurations, audit logs, employee data, health data |
| **4** | **RESTRICTED** | Highest-sensitivity information whose disclosure could cause severe harm. Access limited to named individuals or roles. | Cryptographic key material, root credentials, board-level strategy, legal hold data, security incident forensics, special-category personal data (GDPR Art. 9) |

### 1.1 Classification Rules

- [ ] Every data store, dataset, API response, agent output, and integration payload has an assigned classification level
- [ ] Classification is assigned by the data owner (team or division responsible for the data source)
- [ ] Default classification for new, unreviewed data is **CONFIDENTIAL** until reviewed and downgraded with documented justification
- [ ] Personal data (PII) is classified at minimum **CONFIDENTIAL**; special-category data (GDPR Art. 9) is **RESTRICTED**
- [ ] Classification decisions are recorded in the asset registry (for registered assets) or the PII inventory (for personal data)

### 1.2 Reclassification

- [ ] Reclassification requests are documented with: current level, proposed level, justification, and approver
- [ ] Downgrading (e.g., CONFIDENTIAL to INTERNAL) requires written approval from the data owner and security review
- [ ] Upgrading (e.g., INTERNAL to CONFIDENTIAL) can be done immediately by any agent or team member — no approval needed
- [ ] Reclassification events are logged in the asset's revision history

---

## 2. Handling Requirements by Classification

Each classification level maps to specific handling controls. These requirements are cumulative — higher levels inherit all controls from lower levels.

### 2.1 Summary Matrix

| Control | PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED |
|---------|--------|----------|-------------|------------|
| **Encryption at rest** | Not required | Recommended | **Required** (AES-256) | **Required** (AES-256 + KMS isolation) |
| **Encryption in transit** | TLS recommended | **Required** (TLS 1.2+) | **Required** (TLS 1.2+) | **Required** (TLS 1.3 + mTLS) |
| **Access control** | None | Role-based | Role-based + need-to-know | Named individuals + MFA + audit |
| **Authentication** | None | Standard auth | Standard auth + session limits | MFA required + short-lived tokens |
| **Audit logging** | Not required | Recommended | **Required** | **Required** + tamper-evident |
| **Retention limit** | None | Per policy | **Required** — defined per data category | **Required** — minimum necessary |
| **Deletion/destruction** | Standard | Standard | Verified deletion + confirmation | Cryptographic erasure + dual confirmation |
| **Backup encryption** | Not required | Recommended | **Required** — separate key hierarchy | **Required** — separate key hierarchy + access audit |
| **Sharing / export** | Unrestricted | Internal only | Approval required + DPA if external | Named-recipient only + legal review |
| **Agent access** | Unrestricted | Any authenticated agent | Scoped agents with documented purpose | Named agent types + per-access justification |

### 2.2 Observability & Logging Constraints

- [ ] **PUBLIC / INTERNAL:** May appear in logs and telemetry without redaction
- [ ] **CONFIDENTIAL:** Must be redacted or masked in logs, telemetry, and error messages. Access events must be logged. See `observability.md` and `security.md` sanitization requirements.
- [ ] **RESTRICTED:** Must never appear in logs, telemetry, traces, or error messages. All access logged with actor identity, timestamp, and justification. See `docs/otel-contract.md` Section 8 for privacy defaults.

---

## 3. Data Inventory & Mapping

### 3.1 PII Inventory

Organizations processing personal data must maintain a PII inventory. The inventory is the operational companion to the GDPR Record of Processing Activities required by `privacy.md`.

- [ ] A PII inventory exists and is maintained as instances of `work/assets/_TEMPLATE-pii-inventory.md`
- [ ] The inventory covers: data category, classification level, source, processing purpose, lawful basis (per `privacy.md`), storage location, retention window, and responsible team
- [ ] The inventory is reviewed at minimum quarterly or when new data sources, integrations, or agent workflows are introduced
- [ ] Each PII inventory entry cross-references the relevant privacy impact assessment (DPIA) where applicable

### 3.2 Asset Registry Integration

- [ ] The asset registry template includes a `Data Classification` field (see `work/assets/_TEMPLATE-asset-registry-entry.md`)
- [ ] Every registered asset has a classification level assigned
- [ ] Assets without a classification level are flagged as non-compliant during quality evaluation

### 3.3 Agent Workflow Classification

- [ ] Agent workflows that process, generate, or transmit data document the classification level of their inputs and outputs
- [ ] Agents must not write CONFIDENTIAL or RESTRICTED data to PUBLIC or INTERNAL destinations (e.g., public logs, unencrypted storage, unscoped telemetry)
- [ ] Agent tool calls that access RESTRICTED data produce a `tool.execute` span with `data.classification: restricted` attribute (see `docs/otel-contract.md`)

---

## 4. Deployment-Customizable Decisions

The framework defines the classification structure and handling baseline. Each adopter must configure:

### Must Be Customized Per Instance / Deployment

- **Classification taxonomy extensions** — additional levels or sub-labels (e.g., `CONFIDENTIAL-FINANCIAL`, `RESTRICTED-HEALTH`) if industry requires finer granularity
- **Data category inventory** — what specific data categories the organization processes (names, emails, payment data, health data, biometrics, etc.)
- **Retention schedules per classification** — specific retention windows aligned with legal, regulatory, and contractual requirements
- **Access control implementation** — how role-based and named-individual access maps to your IAM system
- **Encryption key hierarchy** — how classification levels map to your KMS key structure (per `cryptography.md`)
- **Responsible teams** — who owns classification decisions for each data domain

### Must Not Be Customized Away

- The four-level classification scheme (levels may be extended but not reduced)
- The default-to-CONFIDENTIAL rule for unclassified data
- The requirement to maintain a PII inventory when processing personal data
- The handling requirements matrix as a minimum baseline (may be tightened, not loosened)
- The audit logging requirement for CONFIDENTIAL and RESTRICTED data

---

## 5. Cross-Policy Alignment

This policy operationalizes data sensitivity concepts referenced across other policies:

| Policy | What This Policy Provides |
|--------|--------------------------|
| **[Security Policy](security.md)** | Fulfills the "PII identified and classified" requirement (§Data Protection). Classification levels define what "sensitive data" means for encryption and access controls. |
| **[Privacy Policy](privacy.md)** | Classification maps to GDPR data categories. PII inventory operationalizes the Record of Processing Activities. Special-category data maps to RESTRICTED level. |
| **[Encryption & Key Management Policy](cryptography.md)** | Classification determines encryption requirements per level. "High-sensitivity workloads" (§3.3) maps to CONFIDENTIAL and RESTRICTED. |
| **[Observability Policy](observability.md)** | Classification determines what must be redacted in telemetry. "No PII in logs" is operationalized by requiring CONFIDENTIAL+ data redaction. |
| **[Risk Management Policy](risk-management.md)** | Data classification informs risk severity scoring. Data exfiltration (SE-4) and data residency (CO-3) risks are assessed relative to classification level. |
| **[Content Policy](content.md)** | "No confidential information disclosed" maps to CONFIDENTIAL and RESTRICTED handling controls. |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Classification coverage | All data stores and assets have assigned classification levels | Unclassified data stores or assets exist |
| Handling compliance | Encryption, access, and logging controls match or exceed the handling matrix | Controls weaker than the classification level requires |
| PII inventory | Current PII inventory with all required fields; reviewed within last quarter | No PII inventory, or inventory not reviewed in 90+ days |
| Default classification | Unreviewed data defaults to CONFIDENTIAL | Unreviewed data treated as PUBLIC or INTERNAL |
| Agent data flow | Agent workflows document classification of inputs/outputs; no downward data leaks | Agents write CONFIDENTIAL+ data to lower-classification destinations |
| Reclassification governance | Downgrades documented with justification and approval | Downgrades without documentation or approval |
| Asset registry field | All asset registry entries have classification field populated | Asset entries missing classification |

---

## Related Policies

- **[Security Policy](security.md)** — General security controls. This policy provides the classification taxonomy that security.md references for data protection requirements.
- **[Privacy Policy](privacy.md)** — GDPR compliance. PII inventory and classification provide operational structure for privacy obligations.
- **[Encryption & Key Management Policy](cryptography.md)** — Cryptographic controls are applied based on classification level.
- **[Observability Policy](observability.md)** — Telemetry sanitization requirements are driven by classification level.
- **[Risk Management Policy](risk-management.md)** — Risk scoring considers data classification for impact assessment.
- **[Content Policy](content.md)** — Content disclosure controls align with classification levels.

---

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **ISO 27001:2022** | A.8.2 Information classification | §1 |
| **ISO 27001:2022** | A.8.3 Information labeling | §1, §3.2 |
| **ISO 27001:2022** | A.8.4 Information handling | §2 |
| **ISO 27001:2022** | A.8.10 Information deletion | §2.1 (deletion row) |
| **SOC 2** | C1 Confidentiality — classification | §1, §2 |
| **SOC 2** | CC6.1 Logical access — data-level | §2.1 (access control row) |
| **GDPR** | Art. 5(1)(c) Data minimization | §3.1 (PII inventory) |
| **GDPR** | Art. 5(1)(e) Storage limitation | §2.1 (retention row) |
| **GDPR** | Art. 30 Records of processing activities | §3.1 |
| **GDPR** | Art. 9 Special categories | §1 (RESTRICTED level) |
| **NIST SP 800-53** | RA-2 Security categorization | §1 |
| **NIST SP 800-60** | Information type categorization | §1 |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-14 | Initial version — 4-level classification scheme (PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED), handling requirements matrix, PII inventory requirements, asset registry integration, agent workflow classification, cross-policy alignment, compliance mapping (ISO 27001 / SOC 2 / GDPR / NIST). Closes #93. |
