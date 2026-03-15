<!-- placeholder-ok -->
# SOC 2 Type II — Operating Effectiveness Evidence Guide

> **Closes gap:** Operating effectiveness evidence (runtime data)
> **Standard:** SOC 2 Type II — All Trust Service Criteria
> **Severity:** Critical — blocks Type II certification
> **Related issue:** [#123](https://github.com/wlfghdr/agentic-enterprise/issues/123)
> **Related compliance doc:** [SOC 2 Compliance Reference](../soc2.md)

---

## 1. Gap Summary

SOC 2 Type I evaluates whether controls are **designed** appropriately at a single point in time. Type II goes further: it evaluates whether those controls **operated effectively** over a continuous observation period of 6 to 12 months. The distinction is the difference between "you wrote a policy" and "you enforced that policy every day for a year."

The Agentic Enterprise framework provides the **control design layer** — governance hierarchies, quality policies, change management via PRs, observability contracts, and agent instruction boundaries. This design layer satisfies the Type I requirement. However, adopters must independently collect and retain **runtime evidence** proving that these controls were active and effective throughout the audit period. Without this evidence, a Type II audit cannot proceed.

This guide specifies exactly what evidence is required, how to collect it using the framework's built-in observability and governance mechanisms, and how to package it for an auditor.

---

## 2. Evidence Collection Requirements by TSC

Each Trust Service Criterion requires specific types of runtime evidence. The table below maps criteria to concrete evidence, collection methods available within the framework, and the required retention period.

| Criterion | Evidence Required | Collection Method | Retention |
|-----------|-------------------|-------------------|-----------|
| **CC1** Control environment | Governance enforcement logs — proof that the 5-layer model, CODEOWNERS, and agent instruction hierarchy were actively enforced | OTel `agent.run` spans with `governance.decision` events; CODEOWNERS bypass attempts (should be zero) | 12 months |
| **CC2** Communication & information | Policy change records, signal artifacts, decision records proving information flowed through governed channels | Git PR history for policy changes; `work/signals/` artifacts; `work/decisions/` records | 12 months |
| **CC3** Risk assessment | Evidence that risk assessments were performed on schedule and findings were acted upon | `risk.assessment.complete` OTel events; KRI dashboard snapshots; risk register updates in `work/` | 12 months |
| **CC5** Control activities | Quality evaluation results proving that every deliverable was evaluated against policy | `quality.evaluate` spans with `quality.verdict` attribute; CI/CD gate pass/fail logs | 12 months |
| **CC6** Logical & physical access | Authentication and authorization logs proving least-privilege enforcement | `tool.execute` spans with scope verification attributes; failed auth attempts; token lifecycle logs | 12 months |
| **CC7** System operations | Monitoring, alerting, and incident response evidence proving operational vigilance | Full OTel pipeline data; WORM-stored audit and security logs; alerting rule configurations and firing history | 12 months |
| **CC8** Change management | Change approval and deployment records proving every change followed the governed PR process | Git PR merge history with reviewer approvals; CI/CD pipeline spans; deployment rollout metrics; rollback evidence | 12 months |
| **CC9** Vendor risk mitigation | Vendor assessment and ongoing monitoring records for all Tier 1-2 vendors | Vendor review artifacts in `work/`; SLA dashboard data; SOC 2/ISO 27001 attestation collection logs | 12 months |
| **A1** Availability | Uptime metrics, DR drill records, capacity planning evidence | SLO burn rate dashboards; recovery test evidence; capacity planning documents and threshold alerts | 12 months |
| **PI1** Processing integrity | Test results, deployment health checks, data accuracy validations | Quality gate results from `quality.evaluate` spans; canary deployment metrics; data reconciliation reports | 12 months |
| **C1** Confidentiality | Data classification enforcement, encryption status, disposal records | `data.classification` span attributes; encryption audit results per [Cryptography Policy](../../../org/4-quality/policies/cryptography.md); secure disposal logs | 12 months |
| **P1-P8** Privacy | DSAR processing records, consent management, breach response timelines | DSAR OTel events; consent state tracking; breach timeline spans per [Privacy Policy](../../../org/4-quality/policies/privacy.md) | 12 months |

---

## 3. OTel Telemetry to SOC 2 Evidence Mapping

The framework's [OTel Telemetry Contract](../../otel-contract.md) defines canonical span types and events. Each maps directly to SOC 2 evidence needs. This section provides the mapping so adopters can verify their instrumentation covers all audit requirements.

### 3a. Key Span Types

| Span Name | SOC 2 Criteria Served | Evidence Provided |
|-----------|----------------------|-------------------|
| `agent.run` | CC1, CC5 | Proves governance enforcement — every agent invocation is traceable, with layer identity and instruction compliance |
| `tool.execute` | CC6, CC7 | Proves access control enforcement (tool scoping, authentication) and operational activity logging |
| `git.operation` | CC8 | Proves change management — every Git action (commit, push, PR open/merge) is instrumented with author, reviewer, and outcome |
| `quality.evaluate` | CC5, PI1 | Proves control activities — every deliverable was evaluated against quality policies with a recorded PASS/FAIL verdict |
| `mission.transition` | CC1, CC2 | Proves control environment and communication — mission state changes flow through governed channels with approval records |
| `agent.subagent.invoke` | CC1, CC7 | Proves orchestration governance — delegation between agents is explicit, traceable, and within defined boundaries |

### 3b. Key Span Events

| Event Name | SOC 2 Criteria Served | Evidence Provided |
|------------|----------------------|-------------------|
| `governance.decision` | CC1, CC8 | Records every approve/reject/escalate decision with reason and PR number — direct audit evidence of control enforcement |
| `policy.violation` | CC5 | Records control activity failures — **critical evidence** for Type II because auditors verify that violations were detected and remediated |
| `agent.escalation` | CC1 | Proves escalation paths function — agents escalate rather than proceeding beyond their authority |
| `risk.assessment.complete` | CC3 | Proves risk assessments were executed on schedule |

### 3c. Coverage Verification

Before beginning the observation period, verify that your instrumentation covers all required spans and events. Use the OTel compliance check described in [otel-contract.md Section 11](../../otel-contract.md) to validate that:

1. All six canonical span types are being emitted
2. All required attributes for each span type are populated (not null/empty)
3. `governance.decision` events fire for every approval workflow
4. `policy.violation` events fire when quality evaluations return FAIL
5. WORM storage receives audit and security log categories

---

## 4. Evidence Collection Architecture

Adopters must build an evidence collection pipeline that captures, stores, and makes auditable the telemetry and artifacts produced by the framework.

### 4a. Telemetry Pipeline

The recommended architecture:

```
Agent workloads (instrumented per otel-contract.md)
    │
    ▼
OTel SDK (in each agent process)
    │
    ▼
OTel Collector (centralized, with processors for sampling/filtering)
    │
    ├──▶ SIEM / Observability backend (queryable dashboards)
    │
    └──▶ WORM storage (tamper-proof archive for audit/security logs)
```

Key requirements:

- **No sampling for audit-relevant spans.** Governance decisions, policy violations, and access control events must be captured at 100% — never sampled. Configure the OTel Collector to route these to WORM storage unconditionally.
- **WORM storage** (Write Once, Read Many) is required for audit and security log categories per the [Log Retention Policy](../../../org/4-quality/policies/log-retention.md). This proves logs were not tampered with post-facto.
- **Dashboard snapshots** should be automated monthly and stored alongside the WORM archive. These provide point-in-time evidence that dashboards were actively monitored.
- **Clock synchronization** across all agent hosts (NTP or equivalent) — auditors will check timestamp consistency.

### 4b. CONFIG.yaml Integration Setup

Add SOC 2 evidence collection configuration to your `CONFIG.yaml` observability integration:

```yaml
integrations:
  observability:
    provider: "{{OBSERVABILITY_PROVIDER}}"
    capabilities: [metrics, traces, logs]
    endpoints:
      otlp: "https://{{OTLP_ENDPOINT}}"
    soc2_evidence:
      retention_days: 365
      worm_enabled: true
      worm_backend: "{{WORM_STORAGE_PROVIDER}}"
      snapshot_interval: "monthly"
      snapshot_storage: "{{SNAPSHOT_ARCHIVE_PATH}}"
      no_sampling_span_events:
        - "governance.decision"
        - "policy.violation"
        - "agent.escalation"
        - "risk.assessment.complete"
```

See [CONFIG.yaml](../../../CONFIG.yaml) for the full configuration reference and [Integration Registry](../../../org/integrations/README.md) for available observability providers.

### 4c. Git-Based Evidence

The framework's Git-native governance model produces significant audit evidence without additional instrumentation:

| Git Artifact | SOC 2 Criterion | What It Proves |
|-------------|-----------------|----------------|
| PR merge history | CC8 | Every change went through a review-and-approve process |
| CODEOWNERS enforcement | CC1 | Designated owners reviewed changes to governed files |
| Branch protection rules | CC6 | Direct pushes to protected branches were blocked |
| CI/CD pipeline logs | CC5 | Automated quality gates ran on every change |
| Commit signatures (if enabled) | CC6 | Committer identity was cryptographically verified |
| `work/decisions/` records | CC1, CC2 | Governance decisions were documented with DACI accountability |
| `work/signals/` artifacts | CC2, CC3 | Risk signals were captured and triaged through governed channels |

**Export recommendation:** At the start of the audit engagement, export the full Git log for the observation period (`git log --since="YYYY-MM-DD" --until="YYYY-MM-DD" --all --format=fuller`) and PR metadata via the GitHub API. Store this export in the evidence archive.

---

## 5. Sample Evidence Package

This section provides a concrete example of what an auditor expects to see for a single criterion. Use this as a template for assembling evidence packages for all criteria.

### Example: CC8.1 — Change Management Evidence Package

**Control statement:** All changes to information systems follow a governed PR-based process with mandatory human approval, automated quality gates, and traceable deployment.

**Policy reference:** [Delivery Policy](../../../org/4-quality/policies/delivery.md)

**Evidence items:**

1. **Policy document with version history**
   - Current version of `org/4-quality/policies/delivery.md`
   - Git log showing the file was actively maintained during the audit period
   - Proof that agents were instructed to follow it (link to `AGENTS.md` Rule 4)

2. **Population evidence (all changes)**
   - Export of all merged PRs during the audit period
   - For each PR: author, reviewer(s), approval status, CI gate results, merge timestamp
   - Total count and any PRs merged without approval (should be zero)

3. **Sample evidence (detailed review)**
   - 25 randomly selected PRs (auditor may select these) with:
     - Full review conversation trail
     - CI/CD pipeline results (all checks green before merge)
     - Deployment traces showing progressive rollout
     - Any rollback evidence if applicable

4. **Exception evidence**
   - All governance exceptions filed during the period (`work/decisions/EXC-*.md`)
   - Each exception must show: justification, approver, time-bound scope, and remediation
   - If no exceptions were filed, document that fact explicitly

5. **Metrics dashboard**
   - Monthly snapshots showing:
     - PR approval rate (target: 100%)
     - Mean time from PR open to review
     - CI pass rate on first attempt
     - Deployment success rate
     - Rollback frequency

6. **Incident correlation**
   - Any incidents caused by changes during the audit period
   - For each: root cause analysis, corrective action, and link to the change that caused it
   - If no change-related incidents occurred, document that fact with supporting evidence

---

## 6. Minimum Observation Period

### Timeline Requirements

- **SOC 2 Type II minimum observation period:** 6 months
- **Recommended observation period:** 12 months (preferred by most auditors and provides stronger assurance)
- **Evidence retention beyond audit:** Minimum 12 months after the audit period ends (some industries require longer)

### Recommended Timeline

| Phase | Duration | Activities |
|-------|----------|------------|
| **Instrumentation setup** | Month 0 | Deploy OTel pipeline, configure WORM storage, verify all span types are emitting |
| **Burn-in period** | Months 1-2 | Validate evidence completeness, fix instrumentation gaps, begin dashboard snapshots |
| **Observation period start** | Month 3 | Formally begin the observation window; all evidence from this point is audit-relevant |
| **Readiness assessment** | Month 6 | Optional pre-audit with the CPA firm to identify gaps while evidence collection continues |
| **Observation period end** | Month 9-15 | End the window (6-12 months after start, depending on auditor preference) |
| **Audit fieldwork** | Month 10-16 | Auditor examines evidence, conducts walkthroughs, tests samples |
| **Report issuance** | Month 12-18 | Final SOC 2 Type II report issued |

### Pre-Engagement Readiness Checklist

Before the observation period begins, verify all evidence collection mechanisms are operational:

- [ ] OTel pipeline operational and exporting to WORM-capable backend
- [ ] All agent workloads instrumented per [otel-contract.md](../../otel-contract.md)
- [ ] 100% capture (no sampling) configured for governance and security events
- [ ] Dashboard snapshots automated on a monthly schedule
- [ ] Git branch protection enforced on all governed branches
- [ ] CODEOWNERS file active and enforced (no bypass)
- [ ] Quality policy evaluations running and recording PASS/FAIL results
- [ ] Vendor assessments documented for all Tier 1-2 vendors per [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md)
- [ ] Incident response runbooks documented (even if no incidents have occurred)
- [ ] Clock synchronization verified across all agent hosts
- [ ] Evidence archive storage provisioned with sufficient capacity for 12+ months

---

## 7. Auditor Engagement Preparation

### Selecting a CPA Firm

This section is a high-level overview. For the step-by-step engagement workflow, management assertion template, auditor access model, and preparation timeline, see the [SOC 2 CPA audit engagement guide](soc2-cpa-engagement.md).

- The SOC 2 audit must be performed by a **licensed CPA firm** (AICPA member or equivalent in your jurisdiction)
- Look for firms with specific experience in:
  - Technology and SaaS companies
  - AI/ML systems (relevant given the agentic architecture)
  - Automated governance and DevOps-driven control environments
- Request references from companies with similar operating models

### Pre-Audit Deliverables

| Deliverable | Owner | Description |
|-------------|-------|-------------|
| **Management assertion letter** | Executive sponsor | Formal statement that controls are designed and operating effectively; required by AICPA standards |
| **System description** | Architecture team | Narrative describing the system's boundaries, components, data flows, and control environment — this becomes Section 3 of the SOC 2 report |
| **Control matrix** | Compliance team | Mapping of each control to its TSC criterion, with cross-references to framework policies and evidence sources — use [soc2.md Section 2](../soc2.md) as the starting point |
| **Evidence index** | Compliance team | Organized inventory of all evidence artifacts with storage locations, date ranges, and responsible parties |

### Readiness Assessment (Recommended)

Engage the auditor 3-6 months before the formal audit for a **readiness assessment**:

- The auditor reviews your control design and evidence collection mechanisms
- They identify gaps while you still have time to remediate
- This is advisory (no opinion issued) and does not count as the formal audit
- Cost is typically 30-50% of the full audit fee but prevents costly surprises

### Scoping Discussion

Work with the auditor to determine which TSC categories are **in scope** based on your services:

- **Security (CC1-CC9):** Always in scope — mandatory for every SOC 2 report
- **Availability (A1):** In scope if you make uptime commitments to customers
- **Processing Integrity (PI1):** In scope if you process transactions or data where accuracy matters
- **Confidentiality (C1):** In scope if you handle confidential customer data
- **Privacy (P1-P8):** In scope if you handle personal information (consider using SOC 2+ Privacy or pairing with a separate privacy assessment)

### Complementary User Entity Controls (CUECs)

Document controls that **your customers** must implement for the overall control environment to be effective. Common CUECs for an agentic platform include:

- Customer responsibility for managing their own API credentials and access tokens
- Customer responsibility for configuring their own data classification labels
- Customer responsibility for monitoring their own usage dashboards
- Customer responsibility for reporting security incidents on their side

CUECs are listed in the SOC 2 report and shift specific control responsibilities to the customer. Identify these early — auditors will ask.

---

## 8. Verification Checklist

Use this checklist as a final gate before entering the formal audit window. Every item must be confirmed.

### Evidence Completeness

- [ ] OTel pipeline collecting all six canonical span types defined in [otel-contract.md](../../otel-contract.md)
- [ ] `governance.decision` events recorded for every approval workflow (PR merges, mission approvals, policy exceptions)
- [ ] `policy.violation` events recorded for every quality evaluation failure
- [ ] `agent.escalation` events recorded for every escalation
- [ ] WORM storage configured and verified for audit and security log categories
- [ ] WORM integrity verification running on schedule (per [Log Retention Policy](../../../org/4-quality/policies/log-retention.md))

### Observation Period

- [ ] Evidence covers minimum 6-month continuous observation period (12 months preferred)
- [ ] No gaps in telemetry collection during the observation period (verify with pipeline uptime metrics)
- [ ] Dashboard snapshots archived monthly for the full observation period

### Governance Evidence

- [ ] PR-based change management enforced with no bypass during the observation period
- [ ] CODEOWNERS reviews required and enforced — no overrides
- [ ] Branch protection rules active — no direct pushes to governed branches
- [ ] All governance exceptions formally documented in `work/decisions/EXC-*.md`

### Quality and Operations Evidence

- [ ] Quality evaluation results recorded for every deliverable during the observation period
- [ ] Incident response evidence documented (even if no incidents occurred — document the readiness drills)
- [ ] DR drills executed and documented per [Availability Policy](../../../org/4-quality/policies/availability.md) schedule
- [ ] Vendor assessments current for all Tier 1-2 vendors

### Audit Preparation

- [ ] Management assertion letter drafted and reviewed by legal counsel
- [ ] System description written and reviewed for accuracy
- [ ] Control matrix complete with cross-references to evidence
- [ ] Evidence index organized and accessible to the audit team
- [ ] CPA firm engaged with confirmed audit timeline
- [ ] CUECs identified and documented

---

## References

- [SOC 2 Compliance Reference](../soc2.md) — framework-level control design mapping
- [OTel Telemetry Contract](../../otel-contract.md) — canonical span types, attributes, and events
- [Observability Policy](../../../org/4-quality/policies/observability.md) — observability requirements for all agents
- [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) — WORM storage and retention requirements
- [Delivery Policy](../../../org/4-quality/policies/delivery.md) — change management and deployment governance
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md) — risk assessment framework
- [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md) — vendor tiering and assessment
- [Privacy Policy](../../../org/4-quality/policies/privacy.md) — DSAR and breach handling
- [Data Classification Policy](../../../org/4-quality/policies/data-classification.md) — data handling and classification
- [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) — encryption requirements
- [Availability Policy](../../../org/4-quality/policies/availability.md) — RTO/RPO and DR drill requirements
