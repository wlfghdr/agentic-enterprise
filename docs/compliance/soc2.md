# SOC 2 Type II — Compliance Reference

> **Standard:** AICPA SOC 2 — Trust Service Criteria (TSC)
> **Scope:** Controls relevant to Security, Availability, Processing Integrity, Confidentiality, and Privacy
> **Official source:** [AICPA SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)

## 1. What SOC 2 Requires

SOC 2 evaluates an organization's controls against five Trust Service Criteria (TSC):

| Category | Focus | Key Criteria |
|----------|-------|-------------|
| **Security** (CC1–CC9) | Protection against unauthorized access | CC1 Control environment, CC2 Communication, CC3 Risk assessment, CC5 Control activities, CC6 Logical/physical access, CC7 System operations, CC8 Change management, CC9 Risk mitigation |
| **Availability** (A1) | System availability commitments | A1.1 Capacity planning, A1.2 Recovery objectives, A1.3 Backup/recovery testing |
| **Processing Integrity** (PI1) | System processing accuracy | PI1.1–PI1.5 Completeness, accuracy, timeliness |
| **Confidentiality** (C1) | Protection of confidential information | C1.1–C1.2 Identification, protection, disposal |
| **Privacy** (P1–P8) | Personal information handling | Notice, choice, collection, use, disclosure, access, quality, monitoring |

**Type II distinction:** SOC 2 Type II evaluates **operating effectiveness over a period** (typically 6–12 months), not just control design. This means runtime evidence is essential.

## 2. How This Framework Addresses It

### Trust Service Criteria Mapping

| Criterion | Requirement | Framework Implementation | Runtime Evidence |
|-----------|-------------|-------------------------|------------------|
| **CC1.1–CC1.5** | Control environment | 5-layer governance model, CODEOWNERS RACI, agent instruction hierarchy | Git history showing governance enforcement |
| **CC2.1–CC2.3** | Communication & information | Versioned policies, PR-based decisions, signal system | Policy change PRs, signal artifacts |
| **CC3.1–CC3.4** | Risk assessment | [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — 5x5 matrix, AI risk taxonomy, KRIs | `risk.assessment.complete` OTel events, KRI dashboards |
| **CC5.1–CC5.3** | Control activities | 19 quality policies with PASS/FAIL evaluation criteria | Quality eval results, CI/CD gate logs |
| **CC6.1–CC6.8** | Logical/physical access | Least-privilege tooling, mTLS, short-lived tokens, data classification | `tool.execute` spans, authentication events |
| **CC7.1–CC7.5** | System operations | [Observability Policy](../../org/4-quality/policies/observability.md), [Log Retention Policy](../../org/4-quality/policies/log-retention.md) — WORM for audit/security logs | Full OTel pipeline, WORM verification, integrity checks |
| **CC8.1** | Change management | PR-based governance, CI/CD gates, progressive rollout | PR history, deployment traces |
| **CC9.1–CC9.2** | Risk mitigation (vendors) | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — 4-tier model, SOC 2/ISO 27001 attestation for Tier 1–2 | Vendor assessment records, SLA dashboards |
| **A1.1–A1.3** | Availability | [Availability Policy](../../org/4-quality/policies/availability.md) — tiered RTO/RPO, DR drills | Recovery dashboards, drill evidence |
| **PI1.1–PI1.5** | Processing integrity | Quality gates, automated testing, progressive rollout with health checks | Test results, deployment health metrics |
| **C1.1–C1.2** | Confidentiality | [Data Classification Policy](../../org/4-quality/policies/data-classification.md), [Cryptography Policy](../../org/4-quality/policies/cryptography.md) | `data.classification` attributes, encryption verification |
| **P1–P8** | Privacy | [Privacy Policy](../../org/4-quality/policies/privacy.md) — lawful basis, DPA, DSAR, breach handling | DSAR OTel events, breach timeline spans |

## 3. Where Observability Provides Evidence

SOC 2 Type II is uniquely dependent on **runtime evidence** — the auditor needs proof that controls operated effectively over the audit period. This is where the observability platform is indispensable:

| SOC 2 Evidence Need | Observability Source | Why It Matters |
|--------------------|---------------------|----------------|
| Audit trail completeness (CC7.1) | Agent spans with `governance.decision` events, WORM-stored logs | Proves every action was logged and logs weren't tampered with |
| Change management effectiveness (CC8.1) | Git PR traces, CI/CD pipeline spans, deployment rollout metrics | Proves changes followed the governed process |
| Access control operation (CC6.1) | `tool.execute` spans with tool scope verification | Proves least-privilege was enforced at runtime |
| Incident detection & response (CC7.2–CC7.4) | Incident timeline spans with SLA measurements | Proves response times met commitments |
| Availability commitments (A1) | SLO burn rate dashboards, uptime metrics, DR drill records | Proves availability targets were maintained |
| Risk monitoring (CC3.1) | KRI dashboards, automated risk signals | Proves risks were actively monitored |
| Vendor oversight (CC9) | Vendor SLA dashboards, attestation tracking | Proves vendor risk was managed continuously |
| Log retention & integrity (CC7.1) | WORM verification alerts, hash chain validation | Proves logs are immutable and retained per schedule |

## 4. Remaining Gaps

| Gap | SOC 2 Requirement | What's Needed | Severity |
|-----|-------------------|---------------|----------|
| **Formal control testing** | All criteria | Documented testing of each control's effectiveness | High — auditor expectation |
| **Independent audit** | SOC 2 engagement | CPA firm engagement, management assertion letter | High — cannot self-certify |
| **Complementary User Entity Controls (CUECs)** | Common | Documentation of what the adopter's customers must do | Medium |
| **Subservice organization management** | CC9 | Formal subservice organization identification and monitoring | Medium — if using SaaS dependencies |
| **Physical access controls** | CC6 | Deployment-specific physical security | Low — often inherited from cloud provider SOC 2 |

**Addressed by framework:** Operating effectiveness evidence collection — see [evidence guide](remediation/soc2-operating-effectiveness.md) for TSC-to-OTel mapping, sample evidence packages, and auditor engagement preparation.

## 5. External References

- [AICPA Trust Service Criteria (2017, updated 2022)](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) — Criteria definitions
- [AICPA SOC 2 Guide](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/sorhome) — Engagement guidance
- [SOC 2 Trust Service Criteria Points of Focus](https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf) — Detailed control points
- [Cloud Security Alliance CCM to SOC 2 Mapping](https://cloudsecurityalliance.org/research/cloud-controls-matrix) — Cross-framework mapping
