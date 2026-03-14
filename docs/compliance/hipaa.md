# HIPAA — Compliance Reference

> **Regulation:** Health Insurance Portability and Accountability Act (Public Law 104-191, 1996), as amended by the HITECH Act (Public Law 111-5, 2009)
> **Scope:** Covered Entities (healthcare providers, health plans, healthcare clearinghouses) and their Business Associates that create, receive, maintain, or transmit Protected Health Information (PHI)
> **Official source:** [HHS HIPAA Home](https://www.hhs.gov/hipaa/index.html)
> **Enforcement authority:** HHS Office for Civil Rights (OCR)

## 1. What HIPAA Requires

HIPAA establishes national standards to protect individuals' medical records and other personal health information. The law is organized into three main rules:

| Rule | Focus | Key Sections |
|------|-------|-------------|
| **Privacy Rule** (45 CFR Part 160, 164 Subpart E) | Governs use and disclosure of PHI, establishes patient rights, requires minimum necessary standard | §164.502 (uses/disclosures), §164.508 (authorizations), §164.520 (NPP), §164.524 (access), §164.526 (amendment), §164.528 (accounting of disclosures), §164.530 (administrative requirements) |
| **Security Rule** (45 CFR Part 160, 164 Subpart C) | Administrative, physical, and technical safeguards to ensure confidentiality, integrity, and availability of ePHI | §164.308 (administrative), §164.310 (physical), §164.312 (technical), §164.314 (organizational), §164.316 (policies/documentation) |
| **Breach Notification Rule** (45 CFR Part 164 Subpart D) | Requirements for notification following a breach of unsecured PHI | §164.404 (individual notice), §164.406 (media notice), §164.408 (HHS notice), §164.410 (BA notification to CE), §164.414 (administrative requirements) |

**Penalties:** Tiered penalty structure from $100 per violation (no knowledge) to $1.9M+ per violation category per year, plus potential criminal penalties under 42 USC §1320d-6.

## 2. How This Framework Addresses It

### Security Rule — Administrative Safeguards (§164.308)

| Standard | Requirement | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **§164.308(a)(1)** | Security management process — risk analysis, risk management, sanctions policy, information system activity review | [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — ISO 31000-aligned methodology, risk register, risk treatment plans | Risk register artifacts, OTel `risk.assessment.complete` events |
| **§164.308(a)(2)** | Assigned security responsibility | `CODEOWNERS` as RACI for security artifacts; [Security Policy](../../org/4-quality/policies/security.md) defines security role ownership | CODEOWNERS file, PR review assignments |
| **§164.308(a)(3)** | Workforce security — authorization, supervision, termination | Agent instructions (`AGENT.md` hierarchy) define boundaries per layer; Rule 5 ("Stay in your lane"); least-privilege agent tooling | Agent span telemetry showing boundary enforcement |
| **§164.308(a)(4)** | Information access management — access authorization, establishment, modification | `CODEOWNERS` for repository access; [Agent Security Policy](../../org/4-quality/policies/agent-security.md) — tool-level access controls | `tool.execute` spans with access verification |
| **§164.308(a)(5)** | Security awareness and training | Agent instructions serve as "training" for agents; security policy defines awareness requirements | **Partial** — human workforce training is a gap |
| **§164.308(a)(6)** | Security incident procedures | [Incident Response Policy](../../org/4-quality/policies/incident-response.md) — SEV1-4 targets, detection, triage, containment, notification, auto-escalation | Incident timeline OTel spans, postmortem records |
| **§164.308(a)(7)** | Contingency plan — backup, DR, emergency mode | [Availability Policy](../../org/4-quality/policies/availability.md) — tiered RTO/RPO, DR drills, backup requirements | DR drill evidence dashboards, recovery time measurements |
| **§164.308(a)(8)** | Evaluation | Quality Layer (`org/4-quality/`) — policy evaluation, quality gates, continuous compliance monitoring | Quality evaluation reports, CI/CD checks |
| **§164.308(b)** | Business associate contracts and arrangements | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — 4-tier model, assessment, contractual controls; [Privacy Policy](../../org/4-quality/policies/privacy.md) §2 — DPA template | Vendor assessment records, DPA artifacts |

### Security Rule — Physical Safeguards (§164.310)

| Standard | Requirement | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **§164.310(a)** | Facility access controls | **Out of scope** — framework-level, not facility management | N/A |
| **§164.310(b)** | Workstation use | **Out of scope** — deployment-specific | N/A |
| **§164.310(c)** | Workstation security | **Out of scope** — deployment-specific | N/A |
| **§164.310(d)** | Device and media controls | **Out of scope** — deployment-specific; data classification policy provides handling rules per classification level | N/A |

### Security Rule — Technical Safeguards (§164.312)

| Standard | Requirement | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **§164.312(a)** | Access control — unique user ID, emergency access, auto-logoff, encryption | Security Policy — authentication requirements, short-lived tokens; `CODEOWNERS` — access scoping; [Cryptography Policy](../../org/4-quality/policies/cryptography.md) — encryption at rest | Authentication OTel spans, KMS audit logs |
| **§164.312(b)** | Audit controls | [Observability Policy](../../org/4-quality/policies/observability.md) — every agent action emits OTel spans; [Log Retention Policy](../../org/4-quality/policies/log-retention.md) — bounded retention with integrity guarantees; [OTel Contract](../otel-contract.md) — canonical telemetry specification | Full OTel telemetry pipeline, WORM storage verification |
| **§164.312(c)** | Integrity — ePHI alteration/destruction protection | Git-based governance — immutable history, PR-based changes with review; cryptographic hashing | Git history, PR approval records |
| **§164.312(d)** | Person or entity authentication | Security Policy — mTLS, short-lived tokens, identity verification | Authentication event logs |
| **§164.312(e)** | Transmission security — integrity controls, encryption | Cryptography Policy — TLS 1.3 minimum, mTLS for service-to-service; encryption in transit mandatory | Certificate monitoring, TLS verification spans |

### Security Rule — Organizational Requirements (§164.314)

| Standard | Requirement | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **§164.314(a)** | Business associate contracts | Vendor Risk Management Policy — contractual requirements, ongoing monitoring; Privacy Policy §2 — DPA template covers BA obligations | DPA artifacts, vendor assessment records |
| **§164.314(b)** | Group health plan requirements | **Out of scope** — domain-specific organizational requirement | N/A |

### Security Rule — Policies, Procedures, and Documentation (§164.316)

| Standard | Requirement | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **§164.316(a)** | Policies and procedures | 19 quality policies in `org/4-quality/policies/`, version-controlled in Git | Policy version history, Git blame |
| **§164.316(b)** | Documentation — retain for 6 years, keep current, make available | Log Retention Policy — bounded retention; Git history provides indefinite policy version retention; Rule 10 (version everything) | Git history, retention dashboards |

### Privacy Rule Mapping

| Section | Requirement | Framework Implementation | Evidence Source |
|---------|-------------|-------------------------|-----------------|
| **§164.502(a)** | Permitted uses and disclosures | Privacy Policy §1 — lawful basis documentation per processing activity | Processing records in Git |
| **§164.502(b)** | Minimum necessary standard | Privacy Policy — data minimization principles; [Data Classification Policy](../../org/4-quality/policies/data-classification.md) — classification drives handling, least-privilege access | `data.classification` span attributes |
| **§164.508** | Authorizations for uses/disclosures | **Partial** — Privacy Policy covers consent/lawful basis documentation; HIPAA-specific authorization form is a gap | Processing register |
| **§164.520** | Notice of Privacy Practices | **Gap** — framework does not provide NPP template | N/A |
| **§164.524** | Individual access to PHI | Privacy Policy §3 — DSAR runbook with access request workflow, identity verification, search, export | DSAR OTel events |
| **§164.526** | Amendment of PHI | Privacy Policy §3 — DSAR runbook includes correction pathway with accuracy verification | Correction workflow OTel spans |
| **§164.528** | Accounting of disclosures | **Partial** — OTel audit trail tracks agent data access; formal accounting of disclosures report template is a gap | OTel `tool.execute` spans |
| **§164.530(a)(1)** | Privacy Officer designation | **Gap** — framework defines role-based responsibility via CODEOWNERS but does not designate a Privacy Officer | N/A |

### Breach Notification Rule Mapping

| Section | Requirement | Framework Implementation | Evidence Source |
|---------|-------------|-------------------------|-----------------|
| **§164.404** | Individual notification (without unreasonable delay, no later than 60 days) | Incident Response Policy — breach detection, triage, notification workflow; Privacy Policy §4 — notification timelines | Breach timeline OTel spans |
| **§164.406** | Media notification (breaches > 500 residents in a state) | **Partial** — incident response covers communication; media-specific notification process is a gap | Incident records |
| **§164.408** | HHS notification (annual for < 500, immediate for >= 500) | **Partial** — incident response covers regulatory notification; HHS-specific reporting cadence needs configuration | Breach notification records |
| **§164.410** | BA notification to CE | Vendor Risk Management Policy — incident notification requirements in contracts | Vendor incident records |

## 3. Where Observability Provides Evidence

HIPAA's Security Rule explicitly requires audit controls (§164.312(b)) and information system activity review (§164.308(a)(1)(ii)(D)). The framework's observability architecture provides comprehensive evidence:

| HIPAA Evidence Need | Observability Source | Relevant Section |
|---------------------|---------------------|------------------|
| Information system activity review | Agent spans with full action telemetry — every agent action emits OTel spans per AGENTS.md Rule 9 | §164.308(a)(1)(ii)(D) |
| Access control verification | `tool.execute` spans showing least-privilege enforcement, authentication event logs | §164.312(a) |
| Audit trail / audit controls | Full OTel telemetry pipeline — traces, spans, events with [canonical attributes](../otel-contract.md); WORM storage for immutability | §164.312(b) |
| Integrity verification | Git commit hashes, PR approval records, cryptographic verification spans | §164.312(c) |
| Transmission security evidence | TLS verification spans, certificate monitoring alerts, mTLS handshake logs | §164.312(e) |
| ePHI access logging | `data.classification` attributes on tool calls accessing data, purpose-tagged spans | §164.308(a)(1), §164.312(a) |
| Incident detection and response timeline | Incident OTel spans: detection→awareness→triage→containment→eradication→recovery with timestamps | §164.308(a)(6), §164.404 |
| Contingency plan testing evidence | DR drill dashboards, recovery time measurements, backup verification logs | §164.308(a)(7) |
| Risk assessment evidence | `risk.assessment.complete` events, KRI dashboards, `risk.threshold.breach` span events | §164.308(a)(1)(ii)(A) |
| BA/vendor monitoring | Vendor SLA monitoring dashboards, assessment records, contractual compliance tracking | §164.308(b), §164.314 |
| Security awareness verification | Agent instruction version history, policy acknowledgment records | §164.308(a)(5) |

## 4. Remaining Gaps

| Gap | HIPAA Requirement | What's Needed | Criticality |
|-----|------------------|---------------|-------------|
| **Business Associate Agreement (BAA) template** | §164.308(b), §164.314(a) | HIPAA-specific BAA template covering required provisions (permitted uses, safeguards, breach notification, termination, return/destruction of PHI) — the existing DPA template covers some but not all BAA-required terms | **High** |
| **PHI-specific data classification** | §164.502, §164.514 | Extend Data Classification Policy with explicit PHI and ePHI categories, de-identification standards (Safe Harbor and Expert Determination methods per §164.514), and PHI-specific handling rules | **High** |
| **Notice of Privacy Practices (NPP) template** | §164.520 | NPP document template covering required content: uses/disclosures, individual rights, CE duties, complaint process, effective date | **High** |
| **Designated Privacy and Security Officers** | §164.530(a)(1), §164.308(a)(2) | Named Privacy Officer and Security Officer designations — framework defines role-based responsibility but does not mandate specific officer appointments; organizational decision required | **High** |
| **Patient rights implementation** | §164.524, §164.526, §164.528 | Full implementation of access, amendment, and accounting of disclosures workflows with HIPAA-specific timelines (30 days for access, 60 days for amendment, accounting going back 6 years) — DSAR runbook covers the pattern but needs HIPAA-specific timeline configuration | **High** |
| **HIPAA-specific workforce training programme** | §164.308(a)(5), §164.530(b) | Formal security awareness and privacy training for human workforce (not just agent instructions) with documented completion records and periodic refresher schedule | **High** |
| **60-day breach notification timeline enforcement** | §164.404 | Incident Response Policy SLAs partially cover this but need explicit 60-day outer bound with countdown tracking; distinguish between 500+ breaches (immediate HHS notification) and smaller breaches (annual log to HHS) | **Medium** |
| **HIPAA-specific risk assessment methodology** | §164.308(a)(1)(ii)(A) | OCR expects risk assessment methodology aligned with NIST SP 800-30 or equivalent, covering all ePHI — the Risk Management Policy covers general risk assessment but needs HIPAA-specific scope (all systems creating, receiving, maintaining, or transmitting ePHI) | **Medium** |
| **Sanctions policy for workforce violations** | §164.308(a)(1)(ii)(C) | Documented sanctions for workforce members who violate security policies — partially covered by agent boundary enforcement but needs explicit human workforce sanctions | **Medium** |
| **Physical safeguards** | §164.310 | Facility access controls, workstation use/security, device and media controls — out of scope for a software framework; deployment-specific | **Medium** |
| **6-year document retention requirement** | §164.316(b)(2), §164.530(j) | HIPAA requires 6-year retention of policies, procedures, and certain records — Log Retention Policy covers the retention pattern but needs explicit 6-year floor for HIPAA-governed documents | **Low** |

See also: [GDPR compliance reference](gdpr.md) — significant overlap in privacy controls, data subject/patient rights workflows, breach notification requirements, and security safeguards.

## 5. External References

- [HHS HIPAA Home Page](https://www.hhs.gov/hipaa/index.html) — Official HIPAA information and guidance
- [HIPAA Privacy Rule (45 CFR Part 164, Subpart E)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E) — Full regulatory text
- [HIPAA Security Rule (45 CFR Part 164, Subpart C)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C) — Full regulatory text
- [HIPAA Breach Notification Rule (45 CFR Part 164, Subpart D)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D) — Full regulatory text
- [HITECH Act (Public Law 111-5, Title XIII)](https://www.congress.gov/bill/111th-congress/house-bill/1/text) — HITECH amendments to HIPAA
- [NIST SP 800-66 Rev. 2 — Implementing the HIPAA Security Rule](https://csrc.nist.gov/publications/detail/sp/800-66/rev-2/final) — NIST guide for HIPAA Security Rule implementation
- [HHS Security Risk Assessment Tool](https://www.healthit.gov/topic/privacy-security-and-hipaa/security-risk-assessment-tool) — OCR-recommended risk assessment methodology
- [HHS Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) — Public breach reporting database
- [OCR Enforcement Actions](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html) — Resolution agreements and civil money penalties
- [GDPR Compliance Reference](gdpr.md) — Cross-reference for overlapping privacy and security controls
