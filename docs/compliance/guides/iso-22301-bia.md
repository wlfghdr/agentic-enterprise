<!-- placeholder-ok -->
# ISO 22301 — Business Impact Analysis

> **Implements:** Business Impact Analysis template (clause 8.2.2)
> **Standard:** ISO 22301:2019 — Business Continuity Management Systems
> **Severity:** High — central to ISO 22301
> **Related issue:** [#139](https://github.com/wlfghdr/agentic-enterprise/issues/139)
> **Related compliance doc:** [ISO 22301 Compliance Reference](../iso-22301.md)

---

## 1. Purpose

ISO 22301 clause 8.2.2 requires organizations to implement and maintain a formal Business Impact Analysis (BIA) process. The BIA must identify activities that support the delivery of products and services, assess the impacts over time of not performing those activities, set prioritized timeframes and levels for resuming them, and identify dependencies and supporting resources.

The Agentic Enterprise framework provides foundational coverage through the [Availability Policy](../../../org/4-quality/policies/availability.md), which defines four availability tiers with associated RTO/RPO targets, and the [Risk Management Policy](../../../org/4-quality/policies/risk-management.md), which provides ISO 31000-aligned risk assessment methodology. This guide implements the formal BIA methodology and template that connects these policies into a structured impact analysis process — identifying critical processes, determining Maximum Tolerable Period of Disruption (MTPD), documenting impact categories, mapping dependencies, and establishing minimum resource requirements.

This guide provides the BIA requirements, a BIA template tailored to the agentic enterprise context, integration with the framework's availability tiers and risk management policy, and a verification checklist.

---

## 2. BIA Requirements (Clause 8.2.2)

The BIA must address all of the following elements per ISO 22301:

| Requirement | Clause Reference | Description |
|-------------|-----------------|-------------|
| Activity identification | 8.2.2 a) | Identify activities that support the provision of products and services within the BCMS scope |
| Impact assessment over time | 8.2.2 b) | Assess the impacts over time of not performing each activity — impacts must be evaluated across multiple categories and at multiple time intervals |
| MTPD determination | 8.2.2 c) | Set the Maximum Tolerable Period of Disruption for each activity — the point at which impact becomes unacceptable to the organization |
| Prioritized timeframes | 8.2.2 c) | Set prioritized timeframes for resuming each activity at a specified minimum acceptable level — this becomes the RTO |
| Resource identification | 8.2.2 d) | Identify resources required to support each activity — people, technology, information, facilities, supplies, partners |
| Dependency mapping | 8.2.2, 8.2.3 | Identify dependencies between activities, and between activities and external parties, suppliers, and outsourced functions |
| RPO determination | 8.2.2 | Determine the point to which information used by an activity must be restored to enable the activity to operate on resumption (Recovery Point Objective) |

---

## 3. BIA Template

The following template should be instantiated as a governed artifact (e.g., `docs/compliance/bia.md`). It covers the full BIA methodology and results for an agentic enterprise deployment.

```markdown
# Business Impact Analysis

> **Version:** {{VERSION}}
> **Last updated:** {{YYYY-MM-DD}}
> **Approved by:** {{APPROVER_NAME_AND_ROLE}}
> **BCMS scope reference:** {{LINK_TO_BCMS_SCOPE_STATEMENT}}
> **Review frequency:** Annual (minimum) or upon significant change to
>   products, services, or organizational structure

## 1. Methodology

### 1a. Impact Categories

Impacts of disruption are assessed across the following categories:

| Category | Description | Measurement |
|----------|-------------|-------------|
| Financial | Direct revenue loss, contractual penalties, remediation costs | Currency ({{CURRENCY}}) per time period |
| Regulatory / legal | Regulatory non-compliance, legal liability, enforcement action | Severity scale: Low / Medium / High / Critical |
| Reputational | Customer confidence, market perception, brand damage | Severity scale: Low / Medium / High / Critical |
| Operational | Cascading impact on other processes, backlog accumulation | Severity scale: Low / Medium / High / Critical |
| Contractual / SLA | SLA breaches, service credits, customer contract violations | Number of affected SLAs, financial exposure |
| Safety / welfare | Impact on health, safety, or welfare of persons | Severity scale: Low / Medium / High / Critical |

### 1b. Time Intervals

Impact is assessed at the following intervals after disruption onset:

| Interval | Label | Rationale |
|----------|-------|-----------|
| 0–1 hour | Immediate | Within incident detection and initial response window |
| 1–4 hours | Short-term | Within Tier 1 RTO target |
| 4–24 hours | Medium-term | Within Tier 2 RTO target |
| 1–3 days | Extended | Within Tier 3 RTO target |
| 3–7 days | Prolonged | Beyond standard recovery targets |
| >7 days | Severe | Potentially unrecoverable without intervention |

### 1c. Availability Tier Mapping

The BIA results directly inform availability tier assignment per the
[Availability Policy](../../../org/4-quality/policies/availability.md):

| Availability Tier | MTPD Range | RTO Target | RPO Target | DR Strategy |
|------------------|------------|------------|------------|-------------|
| Tier 1 — Critical | <4 hours | <1 hour | Near-zero | Active-active |
| Tier 2 — High | <24 hours | <4 hours | <1 hour | Active-passive |
| Tier 3 — Medium | <72 hours | <24 hours | <24 hours | Backup-restore |
| Tier 4 — Low | >72 hours | <72 hours | <72 hours | Rebuild |

## 2. Critical Process Identification

### 2a. Process Inventory

| ID | Process | Description | Supporting Layer | Process Loop | Product/Service Supported |
|----|---------|-------------|-----------------|-------------|--------------------------|
| P-01 | {{e.g., "Customer API request processing"}} | {{Description}} | Execution (Layer 3) | Operate (Loop 4) | {{Product name}} |
| P-02 | {{e.g., "Agent orchestration"}} | {{Description}} | Orchestration (Layer 2) | Build/Operate | {{Product name}} |
| P-03 | {{e.g., "Data ingestion pipeline"}} | {{Description}} | Execution (Layer 3) | Operate (Loop 4) | {{Product name}} |
| P-04 | {{e.g., "Authentication and authorization"}} | {{Description}} | Execution (Layer 3) | Operate (Loop 4) | All products |
| P-05 | {{e.g., "Monitoring and alerting"}} | {{Description}} | Quality (Layer 4) | Operate (Loop 4) | All products |
| P-06 | {{e.g., "CI/CD pipeline"}} | {{Description}} | Execution (Layer 3) | Ship (Loop 3) | All products |
| P-07 | {{e.g., "Governance and compliance"}} | {{Description}} | Steering (Layer 0) | Discover (Loop 1) | All products |

### 2b. Impact Assessment

For each process, assess impact at each time interval across all impact
categories. Use the following scale: None (0), Low (1), Medium (2),
High (3), Critical (4).

| Process ID | Impact Category | 0–1h | 1–4h | 4–24h | 1–3d | 3–7d | >7d |
|-----------|-----------------|------|------|-------|------|------|-----|
| P-01 | Financial | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| P-01 | Regulatory | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| P-01 | Reputational | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| P-01 | Operational | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| P-01 | Contractual/SLA | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| P-01 | Safety | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| | | | | | | | |
| P-02 | Financial | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} | {{0–4}} |
| ... | ... | ... | ... | ... | ... | ... | ... |

### 2c. MTPD, RTO, and RPO Determination

| Process ID | Process Name | MTPD | RTO | RPO | Availability Tier | Justification |
|-----------|-------------|------|-----|-----|-------------------|---------------|
| P-01 | {{Name}} | {{e.g., "2 hours"}} | {{e.g., "1 hour"}} | {{e.g., "Near-zero"}} | Tier 1 | {{e.g., "Revenue impact exceeds threshold at 2h; SLA breach at 4h"}} |
| P-02 | {{Name}} | {{MTPD}} | {{RTO}} | {{RPO}} | {{Tier}} | {{Justification}} |
| P-03 | {{Name}} | {{MTPD}} | {{RTO}} | {{RPO}} | {{Tier}} | {{Justification}} |

**Rule:** RTO must be less than MTPD. RPO must be achievable with the
DR strategy defined for the assigned availability tier.

## 3. Dependency Mapping

### 3a. Internal Dependencies

| Process ID | Depends On (Process ID) | Dependency Type | Impact if Dependency Fails |
|-----------|------------------------|----------------|---------------------------|
| P-01 | P-04 | Hard — cannot operate without | API requests fail authentication |
| P-01 | P-05 | Soft — degraded operation | Reduced visibility but service continues |
| P-02 | P-04 | Hard | Agent operations cannot authenticate |
| {{...}} | {{...}} | {{Hard/Soft}} | {{Description}} |

### 3b. External Dependencies

| Process ID | External Dependency | Provider | Dependency Type | Alternative Available | Impact if Unavailable |
|-----------|-------------------|----------|----------------|----------------------|----------------------|
| P-01 | LLM API | {{Provider}} | Hard | {{Yes/No — describe}} | {{Impact description}} |
| P-01 | Cloud compute | {{Provider}} | Hard | {{Multi-region/No}} | {{Impact description}} |
| P-06 | Git platform | {{Provider}} | Hard | {{Local copies}} | {{Impact description}} |
| P-05 | Observability platform | {{Provider}} | Soft | {{Local logging}} | {{Impact description}} |

### 3c. Dependency Diagram

{{Include or reference an architecture diagram showing process
dependencies. Store as a governed artifact in the repository.}}

## 4. Minimum Resource Requirements

For each critical process, identify the minimum resources required
to resume at the minimum acceptable level within the RTO.

| Process ID | Resource Category | Minimum Requirement | Normal Capacity | Notes |
|-----------|------------------|--------------------|-----------------|----|
| P-01 | Compute | {{e.g., "2 application instances, 1 database replica"}} | {{e.g., "6 instances, 3 replicas"}} | {{Degraded performance acceptable}} |
| P-01 | People | {{e.g., "1 SRE on-call, 1 incident commander"}} | {{e.g., "3 SREs, 1 team lead"}} | {{Minimum for incident response}} |
| P-01 | Information | {{e.g., "Customer database, API keys, TLS certificates"}} | — | {{Must be recoverable within RPO}} |
| P-01 | External services | {{e.g., "LLM API access, DNS"}} | — | {{Minimum viable provider set}} |
| {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

## 5. BIA Summary and Recommendations

### 5a. Prioritized Process List

| Priority | Process ID | Process Name | Availability Tier | MTPD | RTO |
|----------|-----------|-------------|-------------------|------|-----|
| 1 | {{ID}} | {{Name}} | Tier 1 | {{MTPD}} | {{RTO}} |
| 2 | {{ID}} | {{Name}} | {{Tier}} | {{MTPD}} | {{RTO}} |
| 3 | {{ID}} | {{Name}} | {{Tier}} | {{MTPD}} | {{RTO}} |

### 5b. Key Findings and Recommendations

- {{Finding 1 — e.g., "Single points of failure identified in process P-03"}}
- {{Finding 2 — e.g., "Current DR strategy for P-02 does not meet the
  determined RTO"}}
- {{Recommendation 1 — e.g., "Upgrade P-03 from Tier 3 to Tier 2 based on
  impact assessment results"}}

## 6. Review and Approval

| Action | Responsible | Date |
|--------|------------|------|
| BIA conducted | {{ANALYST}} | {{DATE}} |
| Results reviewed | {{REVIEWER}} | {{DATE}} |
| Approved by management | {{APPROVER}} | {{DATE}} |
| Next review due | — | {{DATE + 1 year}} |
```

---

## 4. Integration with Framework Policies

### Availability Policy Integration

The BIA results feed directly into the [Availability Policy](../../../org/4-quality/policies/availability.md) tier assignments:

| BIA Output | Availability Policy Input | Action Required |
|-----------|--------------------------|-----------------|
| MTPD per process | Tier assignment criteria | Map each process to the tier whose RTO is less than its MTPD |
| RPO per process | Tier RPO validation | Confirm that the tier's DR strategy can achieve the required RPO |
| Dependencies | DR architecture design | Ensure DR strategies account for dependency chains — a Tier 1 process cannot depend on a Tier 3 process without mitigation |
| Minimum resources | Capacity planning | DR environments must be provisioned to meet minimum resource requirements |

### Risk Management Policy Integration

The BIA complements but does not replace the risk assessment required by the [Risk Management Policy](../../../org/4-quality/policies/risk-management.md):

| BIA | Risk Assessment | Relationship |
|-----|----------------|--------------|
| Identifies critical processes and their impact if disrupted | Identifies threats and vulnerabilities that could cause disruption | BIA determines WHAT matters; risk assessment determines HOW LIKELY disruption is |
| Sets recovery priorities (MTPD, RTO, RPO) | Sets risk treatment priorities (risk appetite, KRI thresholds) | Both inform BC strategy selection |
| Maps dependencies | Maps threat vectors | Combined view reveals cascading failure scenarios |

**Clause 8.2.3 requires a risk assessment that is consistent with the BIA.** The risk register maintained per the Risk Management Policy must reference BIA process IDs, and risk treatment decisions must account for BIA-determined recovery priorities.

---

## 5. Observability Evidence

The observability platform provides data to validate and maintain the BIA:

| BIA Element | Observability Source | How It Helps |
|------------|---------------------|--------------|
| Process criticality ranking | SLO dashboards, revenue attribution metrics | Validates whether impact assumptions match operational reality |
| MTPD / RTO targets | DR drill recovery time spans | Confirms whether current recovery capabilities meet BIA-determined targets |
| RPO targets | Backup completion timestamps, replication lag metrics | Validates whether data protection meets RPO requirements |
| Dependencies | Service dependency maps from distributed traces | Discovers dependencies not captured in manual BIA — automated validation |
| Impact assessment | Incident timeline spans, blast radius metrics | Historical incident data validates impact category scores |

---

## 6. Verification Checklist

### BIA Content
- [ ] All activities within BCMS scope are identified and documented
- [ ] Impact categories are defined and appropriate for the organization
- [ ] Impact is assessed at multiple time intervals for each activity
- [ ] MTPD is determined for each critical activity with documented rationale
- [ ] RTO is set for each activity and is less than its MTPD
- [ ] RPO is set for each activity that uses or produces information
- [ ] All activities are mapped to availability tiers per the Availability Policy

### Dependencies
- [ ] Internal dependencies between processes are mapped (hard and soft)
- [ ] External dependencies on suppliers, partners, and services are identified
- [ ] Dependency chains are validated — no Tier 1 hard dependency on lower-tier process without mitigation
- [ ] Single points of failure are identified and documented

### Resources
- [ ] Minimum resource requirements are documented for each critical process
- [ ] Resource requirements are categorized (people, technology, information, facilities, external services)
- [ ] Minimum requirements are validated as achievable with current DR provisioning

### Integration
- [ ] BIA results are consistent with the Risk Management Policy risk register
- [ ] Availability tier assignments match BIA-determined MTPD/RTO/RPO
- [ ] BIA process IDs are referenced in BC plans (clause 8.4)
- [ ] BIA informs the exercise programme — exercises test the most critical processes first

### Governance
- [ ] BIA is version-controlled in the repository
- [ ] BIA has been reviewed and approved by management
- [ ] BIA references the BCMS scope statement
- [ ] Review frequency is defined (at least annual or upon significant change)
- [ ] BIA methodology is documented and repeatable
