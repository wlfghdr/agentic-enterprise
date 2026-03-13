# Policy Source Notes — Privacy, Incident Response, Availability

> **Purpose:** Concise research notes that shaped the framework policies added in March 2026.
> **Scope:** GDPR privacy controls, incident response SLAs, and disaster recovery / business continuity.

---

## Privacy / GDPR

### Primary sources

- **GDPR official text (EUR-Lex):** <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679>
  - Shaped the policy structure around Articles **28** (processor terms / DPA), **12 + 15–22** (data subject rights), **33–34** (breach notification), **35** (DPIA), and **44–46** (international transfers).
- **ICO — Data processing agreements:** <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/data-sharing-a-code-of-practice/data-processing-agreements/>
  - Reinforced the minimum operational content of a DPA and controller/processor allocation.
- **ICO — Right of access:** <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/right-of-access/>
  - Helped frame the DSAR runbook around identity verification, search scope, deadlines, and exceptions.
- **ICO — Personal data breaches guide:** <https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/>
  - Shaped the requirement to distinguish general incidents from personal-data breaches and to operate against the 72-hour supervisory-authority clock.

### Synthesis used in this repo

- The framework should not pretend every deployment has the same lawful basis, DPO requirement, or transfer pattern.
- Therefore the policy separates **non-negotiable legal control categories** from **deployment-specific legal configuration**.
- Observability is used as evidence for DSAR and breach workflows, but the policy explicitly keeps telemetry sanitized and subordinate to privacy law.

## Incident Response SLAs

### Primary sources

- **NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide:** <https://csrc.nist.gov/pubs/sp/800/61/r2/final>
  - Anchored the incident lifecycle logic: preparation, detection, analysis, containment, eradication, and recovery.
- **Google SRE Book — Managing Incidents:** <https://sre.google/sre-book/managing-incidents/>
  - Shaped the emphasis on incident command, early ownership, communication, and avoiding unmanaged incident chaos.
- **CISA Ransomware Guide:** <https://www.cisa.gov/stopransomware/ransomware-guide>
  - Reinforced the need for prepared operational playbooks, escalation readiness, and evidence-driven response in serious incidents.

### Synthesis used in this repo

- Standards strongly support disciplined incident handling, but they generally do **not** prescribe universal SEV1–SEV4 minute/hour targets.
- Therefore the framework adopts a pragmatic enterprise baseline matrix and makes stricter contractual targets override it.
- Observability is treated as part of the SLA mechanism itself: it supplies detection time, verifies mitigation, and proves whether recovery actually occurred.

## Availability / Disaster Recovery / Business Continuity

### Primary sources

- **NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems:** <https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final>
  - Anchored contingency planning, dependency-aware recovery design, and recovery testing expectations.
- **AWS whitepaper — Disaster Recovery of Workloads on AWS:** <https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/>
  - Reinforced the use of RTO/RPO as architecture-level choices tied to recovery strategy and investment.

### Synthesis used in this repo

- The policy treats RTO/RPO as **tiered defaults**, not magical promises.
- Service tiering, runbooks, backup/replication health, and drill evidence are all required before targets are credible.
- Observability is explicitly tied to failover confidence, replication/backup readiness, verification of restore success, and drill evidence.

---

## Why the policies are concise

This repo is a framework / operating model, not a legal handbook or 50-page enterprise manual. The implementation deliberately keeps the policy layer compact and pushes deployment-specific detail into templates, runbooks, and local customization.
