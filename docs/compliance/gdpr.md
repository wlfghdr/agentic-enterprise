# GDPR — Compliance Reference

> **Regulation:** General Data Protection Regulation (EU) 2016/679
> **Scope:** Processing of personal data of individuals in the EU/EEA
> **Official source:** [EUR-Lex — GDPR Full Text](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
> **Supervisory authorities:** National DPAs (e.g., BfDI (DE), CNIL (FR), ICO (UK-equivalent))

## 1. What GDPR Requires

GDPR establishes rights for data subjects and obligations for controllers/processors across these key areas:

| Chapter | Focus | Key Articles |
|---------|-------|-------------|
| **Principles** (Art. 5) | Lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, accountability | Art. 5(1)(a)–(f), 5(2) |
| **Lawful basis** (Art. 6) | At least one legal basis required for processing | Art. 6(1)(a)–(f) |
| **Special categories** (Art. 9) | Stricter rules for health, biometric, political, religious data | Art. 9(1)–(2) |
| **Data subject rights** (Art. 12–22) | Access, rectification, erasure, portability, objection, automated decision-making | Art. 15–22 |
| **Controller/processor** (Art. 24–31) | Responsibility, DPA, records of processing | Art. 26, 28, 30 |
| **Security** (Art. 32) | Appropriate technical and organizational measures | Art. 32(1)(a)–(d) |
| **Breach notification** (Art. 33–34) | 72-hour notification to authority, communication to data subjects | Art. 33(1), 34(1) |
| **DPIA** (Art. 35) | Impact assessment before high-risk processing | Art. 35(1), 35(3) |
| **International transfers** (Art. 44–49) | Adequate safeguards for transfers outside EU/EEA | Art. 46 (SCCs), 47 (BCRs) |
| **DPO** (Art. 37–39) | Data Protection Officer appointment for certain organizations | Art. 37(1) |

## 2. How This Framework Addresses It

### Article-Level Mapping

| Article | Requirement | Framework Implementation | Evidence Source |
|---------|-------------|-------------------------|-----------------|
| **Art. 5(1)(a)** | Lawfulness, fairness, transparency | [Privacy Policy](../../org/4-quality/policies/privacy.md) §1 — lawful basis documentation per feature/workflow | Processing records in Git |
| **Art. 5(1)(b)** | Purpose limitation | Privacy Policy §1 — purpose documented per data processing activity | Purpose declarations in processing records |
| **Art. 5(1)(c)** | Data minimization | [Data Classification Policy](../../org/4-quality/policies/data-classification.md) — classification drives handling, least-privilege data access | `data.classification` span attributes |
| **Art. 5(1)(e)** | Storage limitation | [Log Retention Policy](../../org/4-quality/policies/log-retention.md) — bounded retention, verified deletion | Deletion confirmation audit logs |
| **Art. 5(1)(f)** | Integrity and confidentiality | [Security Policy](../../org/4-quality/policies/security.md), [Cryptography Policy](../../org/4-quality/policies/cryptography.md) — encryption, access controls | KMS audit trails, access logs |
| **Art. 5(2)** | Accountability | Git history as audit trail, OTel telemetry, PR-based governance | Full observability pipeline |
| **Art. 6** | Lawful basis | Privacy Policy §1 — documented per feature, AI features include prompts/outputs/traces | Processing register |
| **Art. 9** | Special categories | Data Classification — RESTRICTED level for Art. 9 data | Classification enforcement spans |
| **Art. 12–22** | Data subject rights | Privacy Policy §3 — DSAR runbook with identity verification, search, export, correction, deletion | DSAR OTel events (intake→verification→fulfillment→closure) |
| **Art. 28** | Processor obligations | Privacy Policy §2 — DPA template, subprocessor controls | DPA artifacts, [Vendor Risk Management](../../org/4-quality/policies/vendor-risk-management.md) records |
| **Art. 30** | Records of processing | Privacy Policy §1 — RoPA requirement per deployment | Processing register artifacts |
| **Art. 32** | Security of processing | Security Policy + Cryptography Policy — encryption at rest/transit, access controls, pseudonymization | Security audit trails |
| **Art. 33** | Breach notification (authority) | Privacy Policy §4 — 72-hour clock, triage process | Breach timeline OTel spans |
| **Art. 34** | Breach notification (data subjects) | Privacy Policy §4 — communication to affected individuals | Breach notification records |
| **Art. 35** | DPIA | Privacy Policy §5 — required before high-risk processing, AI profiling requires DPIA | DPIA decision records |
| **Art. 44–49** | International transfers | Privacy Policy §7 — transfer mapping, SCCs, transfer risk assessment | Transfer mechanism records |

## 3. Where Observability Provides Evidence

GDPR accountability (Art. 5(2)) requires demonstrable compliance — not just policies on paper. The observability platform provides this evidence:

| GDPR Evidence Need | Observability Source | Relevant Article |
|--------------------|---------------------|------------------|
| Processing lawfulness proof | Agent spans showing data access with documented purpose | Art. 5(1)(a), 6 |
| Data minimization verification | `data.classification` attributes on tool calls, access scoping | Art. 5(1)(c) |
| Storage limitation enforcement | Log retention dashboards, deletion confirmation logs | Art. 5(1)(e) |
| DSAR response tracking | DSAR workflow OTel events with SLA measurements | Art. 12–22 |
| Breach response timeline | Breach OTel spans: detection→awareness→triage→notification | Art. 33–34 |
| Security measure effectiveness | Encryption verification, access control audit trails | Art. 32 |
| DPIA decision trail | `governance.decision` events for high-risk processing gates | Art. 35 |
| Transfer mechanism verification | Vendor assessment records, SCC documentation | Art. 44–49 |

## 4. Remaining Gaps

| Gap | GDPR Requirement | What's Needed | Severity |
|-----|-----------------|---------------|----------|
| **Consent management UX** | Art. 6(1)(a), 7 | Runtime consent collection, storage, withdrawal UI — deployment-specific | High — if consent is the lawful basis |
| **DPO appointment** | Art. 37 | Named DPO with independence guarantees — organizational decision | High — if required (public authority, large-scale monitoring, special categories) |
| **Supervisory authority registration** | Art. 37(7) | DPO contact details communicated to SA | Medium — organizational |
| **Cookie/tracking compliance** | ePrivacy Directive | Cookie consent, tracking transparency — deployment-specific | Medium — if web-facing |
| **Records of Processing (RoPA)** | Art. 30 | Populated inventory — framework provides template, deployment must populate | Medium |
| **Right to explanation** | Art. 22 | Meaningful information about automated decision-making logic | Medium — addressed partially by AI governance explainability |
| **Age verification** | Art. 8 | Child data protections if processing children's data | Low — context-dependent |

## 5. External References

- [GDPR Full Text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — Official regulation text
- [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en) — European Data Protection Board guidance documents
- [WP29 Guidelines on DPIAs](https://ec.europa.eu/newsroom/article29/items/611236) — DPIA methodology guidance
- [SCCs for International Transfers (2021)](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en) — Standard Contractual Clauses
- [ICO Guide to GDPR](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/) — UK supervisory authority practical guide
- [BfDI GDPR Guidance](https://www.bfdi.bund.de/EN/Home/home_node.html) — German federal DPA
- [CNIL GDPR Guidance](https://www.cnil.fr/en/gdpr-developers-guide) — French DPA guide for developers
