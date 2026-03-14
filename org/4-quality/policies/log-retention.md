<!-- placeholder-ok -->
# Log Retention & Immutability Policy

> **Applies to:** All log data, telemetry, audit trails, and observability records produced by services, agents, pipelines, and infrastructure
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team, Operations leadership
> **Version:** 1.0 | **Last updated:** 2026-03-14

---

## Principles

1. **Logs are evidence** — Every log record, trace, and metric is potential evidence for compliance, incident investigation, and audit. Retention is not optional storage management — it is a governance obligation.
2. **Immutability protects trust** — Audit logs that can be modified after the fact have no evidentiary value. Tamper-evidence is a hard requirement for compliance-critical records.
3. **Retention is bounded** — Logs must be retained long enough to satisfy regulatory, contractual, and operational obligations — and deleted when those obligations expire. Indefinite retention without justification violates storage limitation principles.
4. **Classification drives retention** — The retention period for a log record is determined by its data classification level (per [data-classification.md](data-classification.md)) and its log category, not by ad-hoc decisions.
5. **Deletion is a positive act** — Deleting logs at retention expiry is as important as retaining them. Deletion must be verified, logged, and auditable.

---

## Why This Policy Exists

The framework mandates comprehensive observability (AGENTS.md Rule 9a) and defines telemetry as "the system of truth for what agents actually did." But without defined retention periods, immutability requirements, and deletion procedures:

- **SOC 2 auditors** cannot verify that audit trails are durable and tamper-evident (CC7.1)
- **ISO 27001 assessors** cannot confirm "appropriate retention periods" or "protection of log information" (A.12.4)
- **GDPR controllers** cannot demonstrate storage limitation compliance (Art. 5(1)(e)) or produce records of processing activities (Art. 30)
- **Incident investigators** cannot rely on logs existing when needed for postmortem analysis
- **Legal counsel** cannot place litigation holds on evidence that may have been auto-deleted

This policy closes those gaps by defining what is retained, for how long, how it is protected, and when it is deleted.

---

## 1. Log Categories & Retention Schedule

All log data falls into one of five categories. Each category has a default retention period that adopters must configure for their deployment.

### 1.1 Retention Schedule

| Category | Description | Default Retention | Online Availability | Examples |
|----------|-------------|-------------------|--------------------:|---------|
| **Audit logs** | Records of governance decisions, access control changes, policy evaluations, approval events, agent autonomous decisions | {{RETENTION_AUDIT_YEARS}} years (recommended: 7) | 1 year | `governance.decision` span events, PR approvals, permission changes, data access authorizations, classification changes |
| **Security logs** | Authentication events, authorization failures, policy violations, intrusion detection, vulnerability scan results | {{RETENTION_SECURITY_YEARS}} years (recommended: 7) | 6 months | Failed logins, MFA events, firewall logs, WAF events, secret rotation records, agent policy violations |
| **Access logs** | Records of who accessed what data, when, and from where. Includes agent data access spans | {{RETENTION_ACCESS_YEARS}} years (recommended: 3) | 6 months | API access logs, database query logs (sanitized), file access records, `tool.execute` spans with `data.classification` attribute |
| **Operational logs** | Application behavior, performance metrics, health checks, agent task execution, non-security telemetry | {{RETENTION_OPERATIONAL_DAYS}} days (recommended: 90) | Full period | Application stdout/stderr, health check results, `agent.run` spans, `inference.chat` spans, deployment logs |
| **Debug logs** | Verbose diagnostic output enabled for troubleshooting. May contain transient sensitive data. | {{RETENTION_DEBUG_DAYS}} days (recommended: 30) | Full period | Stack traces, request/response bodies (sanitized), verbose agent reasoning traces |

### 1.2 Retention Rules

- [ ] Every log source is assigned to exactly one category in the deployment's log inventory
- [ ] Retention periods are configured per deployment in CONFIG.yaml (see §6)
- [ ] Logs containing personal data (CONFIDENTIAL+ per data-classification.md) follow the shorter of: the category retention period or the data subject's retention window from the PII inventory
- [ ] Legal holds (§4) override normal retention — held logs are not deleted until the hold is released
- [ ] Retention clocks start from the timestamp of the log record, not the date of ingestion

### 1.3 Online vs. Archive Availability

- [ ] Logs within the **online availability** window must be queryable in the observability platform with sub-minute response times
- [ ] Logs past the online window but within retention period may be moved to cold/archive storage, but must be retrievable within 24 hours upon request
- [ ] Archive storage must maintain the same immutability and access controls as online storage

---

## 2. Immutability & Tamper-Evidence

### 2.1 Immutability Requirements by Log Category

| Category | Immutability Requirement |
|----------|------------------------|
| **Audit logs** | **WORM required** — Write-Once Read-Many. No modification or deletion before retention expiry (except legal hold extension). |
| **Security logs** | **WORM required** — Same as audit logs. Security events must be tamper-proof for forensic investigations. |
| **Access logs** | **Tamper-evident required** — Integrity verification must detect any modification. WORM recommended but not mandatory. |
| **Operational logs** | **Tamper-evident recommended** — Integrity checksums should be maintained. |
| **Debug logs** | **No immutability requirement** — May be truncated or compressed during retention period. |

### 2.2 Tamper-Evidence Mechanisms

At least one of the following mechanisms must be active for log categories that require tamper-evidence:

- [ ] **Cryptographic checksums** — Each log batch or log file has a SHA-256 (or stronger) hash stored separately from the log data
- [ ] **Hash chains** — Sequential log records are chained so that modification of any record invalidates all subsequent hashes
- [ ] **WORM storage** — Storage backend enforces write-once semantics at the infrastructure level (e.g., S3 Object Lock, Azure Immutable Blob, GCS Bucket Lock)
- [ ] **Third-party attestation** — An independent service or timestamping authority periodically attests to log integrity

### 2.3 Integrity Verification

- [ ] Integrity verification runs automatically on a scheduled basis (recommended: daily for audit/security logs, weekly for access logs)
- [ ] Verification failures generate a **SEV2 security incident** (per [incident-response.md](incident-response.md)) — log tampering is a security event
- [ ] Verification results are themselves logged and retained as audit records
- [ ] The verification mechanism is independent of the system that produced the logs (separation of duties)

---

## 3. Access Control for Log Data

Log data itself requires classification and access control — logs about sensitive operations are sensitive data.

### 3.1 Log Data Classification

| Log Category | Minimum Classification | Rationale |
|--------------|----------------------|-----------|
| Audit logs | **CONFIDENTIAL** | Contains governance decisions, access patterns, and organizational behavior |
| Security logs | **CONFIDENTIAL** | Reveals security posture, attack patterns, and defensive capabilities |
| Access logs | **CONFIDENTIAL** | Contains who-accessed-what patterns; PII if user identifiers present |
| Operational logs | **INTERNAL** | Application behavior; no inherent sensitivity unless containing classified data |
| Debug logs | **CONFIDENTIAL** | May contain transient sensitive data (request bodies, stack traces with data) |

### 3.2 Access Requirements

- [ ] Access to audit and security logs is restricted to named security/compliance roles
- [ ] Access to log data follows the handling requirements of its classification level (per data-classification.md §2.1)
- [ ] All access to CONFIDENTIAL+ log data is itself logged (creating a meta-audit trail)
- [ ] Bulk log exports (for legal discovery, compliance review, or analytics) require documented approval
- [ ] Agents accessing log data must have documented purpose and scoped permissions (per data-classification.md §3.3)

---

## 4. Legal Hold & Compliance Preservation

### 4.1 Legal Hold Process

A legal hold suspends normal retention and deletion for logs relevant to an active or anticipated legal matter, regulatory investigation, or compliance audit.

- [ ] Legal holds can be initiated by: legal counsel, compliance officer, or security leadership
- [ ] A legal hold specifies: scope (which log categories, time range, and systems), reason, initiator, and expected duration
- [ ] Legal hold records are stored as governance exceptions (per AGENTS.md Rule 4) using `work/decisions/_TEMPLATE-governance-exception.md`
- [ ] Held logs are segregated or flagged so that automated retention deletion skips them
- [ ] Legal holds are reviewed at least quarterly — holds without active justification must be released

### 4.2 Compliance Archival

- [ ] When an external audit is announced, all relevant log categories are placed under preservation notice until the audit concludes
- [ ] Compliance archival follows the same immutability requirements as the log category's normal operations
- [ ] Archived logs for compliance must be exportable in a standard format (JSON, CSV, or the observability platform's native export format) within 24 hours of request

---

## 5. Deletion & Lifecycle

### 5.1 Retention Expiry Deletion

- [ ] Automated deletion jobs run on a defined schedule (recommended: daily) to remove logs past their retention period
- [ ] Deletion jobs check for active legal holds before deleting — held logs are skipped
- [ ] Deletion is verified: after a deletion run, a confirmation record is produced showing what was deleted (log category, time range, volume) and what was retained (due to legal hold or other exception)
- [ ] Deletion confirmation records are retained as audit logs (subject to audit log retention period)
- [ ] For logs containing personal data: deletion follows the verified deletion or cryptographic erasure requirements of data-classification.md §2.1

### 5.2 Log Lifecycle States

```
ACTIVE (online, queryable, within online availability window)
  → ARCHIVED (cold storage, retrievable within 24h, still within retention period)
    → DELETION PENDING (retention expired, queued for deletion, legal hold check)
      → DELETED (verified deletion, confirmation record produced)
         or
      → HELD (legal hold active, deletion suspended)
```

---

## 6. Deployment-Customizable Decisions

### Must Be Customized Per Instance / Deployment

- **Retention periods** — Each log category's retention period must be set based on the deployment's regulatory, contractual, and operational requirements. The defaults in §1.1 are recommendations; adjust based on jurisdiction (e.g., HIPAA requires 6 years for certain records, financial regulations may require 7-10 years)
- **WORM implementation** — The specific storage backend and WORM mechanism (S3 Object Lock, Azure Immutable Blob, dedicated WORM appliance, etc.)
- **Online availability windows** — How long logs remain in hot/warm storage depends on query volume and cost constraints
- **Legal hold workflow** — Who can initiate and release holds, and through what tooling
- **Deletion automation** — Scheduling and tooling for automated retention expiry deletion
- **Log classification overrides** — Some deployments may classify operational logs as CONFIDENTIAL if they contain regulated data

### Must Not Be Customized Away

- The five log categories (categories may be extended but not reduced)
- WORM requirement for audit and security logs
- Tamper-evidence requirement for access logs
- Legal hold capability
- Verified deletion with confirmation records
- The principle that retention periods are finite (no indefinite retention without explicit legal hold)

---

## 7. Agent-Specific Log Retention

Agents produce telemetry per AGENTS.md Rule 9a and the [OTEL-CONTRACT.md](../../../docs/OTEL-CONTRACT.md). Agent telemetry falls into the log categories as follows:

| Agent Telemetry Type | Log Category | Retention Rationale |
|---------------------|-------------|-------------------|
| `governance.decision` span events | **Audit** | Every autonomous decision must be auditable for the full audit retention period |
| `agent.run` spans | **Operational** | Task execution traces support operational debugging |
| `inference.chat` / `inference.generate` spans | **Operational** | LLM invocation records; upgrade to **Access** if processing CONFIDENTIAL+ data |
| `tool.execute` spans | **Access** (if `data.classification` is CONFIDENTIAL+) or **Operational** | Data access by agents must be as auditable as human data access |
| Policy violation events | **Security** | Agent policy violations are security-relevant |
| Token usage metrics | **Operational** | Cost attribution and budget enforcement (per ai-governance.md §6) |

- [ ] Agent telemetry is classified into log categories based on the mapping above
- [ ] `governance.decision` events are always treated as audit logs regardless of the agent's risk tier
- [ ] Agent spans that access RESTRICTED data are retained for the full audit log retention period

---

## 8. Cross-Policy Alignment

| Policy | What This Policy Provides |
|--------|--------------------------|
| **[Observability Policy](observability.md)** | Extends observability by defining how long telemetry is retained and how it is protected. Observability defines what is collected; this policy defines how long it lives. |
| **[Data Classification Policy](data-classification.md)** | Operationalizes the "retention limit" row in the handling requirements matrix. Log data is itself classified and handled per classification level. |
| **[Security Policy](security.md)** | Fulfills the "data retention policies defined and enforced" requirement (§Data Protection). Security logs are protected as CONFIDENTIAL data. |
| **[Privacy Policy](privacy.md)** | Connects log retention to GDPR storage limitation (Art. 5(1)(e)). Logs containing PII follow the stricter of: category retention or PII retention window. |
| **[Incident Response Policy](incident-response.md)** | Ensures logs exist for postmortem analysis. Evidence preservation (§Observability Requirements) depends on defined retention. |
| **[Cryptography Policy](cryptography.md)** | Immutability mechanisms (checksums, hash chains) use cryptographic primitives governed by cryptography.md. KMS audit logs follow audit log retention. |
| **[AI Governance Policy](ai-governance.md)** | Agent telemetry retention supports fairness audit, explainability, and token usage accountability requirements. |
| **[Risk Management Policy](risk-management.md)** | Risk telemetry events and KRI data are retained as operational logs. Risk register audit trail follows audit log retention. |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Retention schedule | All log sources assigned to categories with configured retention periods | Log sources without assigned category or retention period |
| Audit log immutability | WORM storage active for audit and security logs; integrity verification running | Audit or security logs modifiable after write, or no integrity verification |
| Tamper-evidence | Access logs have at least one tamper-evidence mechanism active | No tamper-evidence for access logs |
| Legal hold capability | Process exists; at least one legal hold can be demonstrated | No legal hold process or untested capability |
| Deletion verification | Automated deletion runs with confirmation records produced | No verified deletion, or logs retained indefinitely without justification |
| Log access control | CONFIDENTIAL+ log data access restricted and itself logged | Unrestricted access to sensitive log data |
| Agent telemetry classification | Agent spans and events mapped to log categories per §7 | Agent telemetry not classified or retained without category assignment |
| Online availability | Logs queryable within defined online window with sub-minute response | Logs unavailable or query latency exceeds acceptable thresholds during online window |

---

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **ISO 27001:2022** | A.12.4.1 Event logging — appropriate retention periods | §1 |
| **ISO 27001:2022** | A.12.4.2 Protection of log information — tamper-evidence | §2 |
| **ISO 27001:2022** | A.12.4.3 Administrator and operator logs — access control | §3 |
| **SOC 2** | CC7.1 System monitoring — audit trail durability | §1, §2 |
| **SOC 2** | CC7.2 System monitoring — analysis capability | §1.3 (online availability) |
| **GDPR** | Art. 5(1)(e) Storage limitation | §1.2, §5 |
| **GDPR** | Art. 30 Records of processing activities | §1 (retention supports RoPA evidence) |
| **GDPR** | Art. 17 Right to erasure — deletion verification | §5.1 |
| **EU AI Act** | Art. 12 Record-keeping for high-risk AI systems | §7 (agent telemetry retention) |
| **NIST SP 800-53** | AU-11 Audit record retention | §1 |
| **NIST SP 800-53** | AU-9 Protection of audit information | §2, §3 |
| **NIST SP 800-53** | AU-10 Non-repudiation | §2.2 (hash chains, WORM) |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-14 | Initial version — 5-category retention schedule (audit / security / access / operational / debug), WORM and tamper-evidence requirements, legal hold capability, verified deletion, agent telemetry classification, compliance mapping (ISO 27001 A.12.4 / SOC 2 CC7 / GDPR Art. 5/17/30 / EU AI Act Art. 12 / NIST AU). Closes #94. |
