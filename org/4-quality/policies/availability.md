# Availability & Continuity Policy

> **Applies to:** Production services, supporting infrastructure, operational dependencies, and business-critical internal systems
> **Enforced by:** Quality Layer eval agents
> **Authority:** Operations / Platform / Security leadership
> **Version:** 1.0 | **Last updated:** 2026-03-13

---

## Principles

1. **Recovery targets are design inputs** — RTO and RPO shape architecture, not just incident paperwork.
2. **Tiered resilience** — not every system deserves the same recovery spend; every system does need an explicit tier.
3. **Continuity is broader than failover** — people, dependencies, communications, and decision paths matter too.
4. **Recovery claims require evidence** — drills, failovers, backups, and telemetry must prove that targets are believable.

## What This Policy Requires

This policy establishes minimum disaster recovery (DR) and business continuity expectations for every running instance.

It requires:

- Service tiering based on business criticality
- Defined **RTO** (Recovery Time Objective) and **RPO** (Recovery Point Objective) per tier
- Recovery runbooks and failover procedures for critical systems
- Backup, restore, and dependency recovery planning aligned to targets
- Regular recovery tests and evidence retention
- Observability that proves detection, failover behavior, restore success, and drill outcomes

## Deployment-Customizable Decisions

### Must Be Customized Per Instance / Deployment

- Service inventory and tier classification
- Which components are in scope for cross-region, warm standby, hot standby, or backup/restore recovery patterns
- Named recovery owners and business continuity contacts
- Dependency map for identity, secrets, CI/CD, storage, messaging, and external SaaS
- Exact backup frequency, retention, encryption, and restore tooling
- Communication plan for internal stakeholders, customers, and regulators where relevant

### Baseline Tier Targets Defined by This Framework

| Tier | Typical Use | RTO | RPO |
|---|---|---:|---:|
| **Tier 1** | Revenue-critical, customer-facing, or trust-critical services | 15 min | 5 min |
| **Tier 2** | Important but tolerable short interruption | 1 hour | 1 hour |
| **Tier 3** | Internal, batch, or non-critical supporting capability | 24 hours | 24 hours |

These are baseline defaults. A deployment may choose stricter targets but must not claim these targets without evidence.

## Mandatory Requirements

### 1. Tiering and Scope

- [ ] Every production system and critical dependency has an assigned service tier
- [ ] Tiering reflects business impact, customer trust impact, regulatory impact, and dependency centrality
- [ ] Shared dependencies (identity, secrets, control plane, telemetry pipeline, backups) are tiered explicitly, not assumed

### 2. Recovery Design

- [ ] Tier 1 and Tier 2 systems have documented failover and recovery procedures
- [ ] Recovery design identifies primary site/region, recovery site/region, data replication method, and activation criteria
- [ ] Backup and restore strategy is documented for each data store
- [ ] Recovery dependencies and prerequisites are explicit (DNS, secrets, certificates, network routes, CI/CD access, staff access)
- [ ] Recovery designs identify which controls are automated vs. manual

### 3. Recovery Runbooks and Procedures

- [ ] Critical services have a recovery runbook using `process/4-operate/_TEMPLATE-recovery-runbook.md`
- [ ] Failover-capable systems have a procedure using `process/4-operate/_TEMPLATE-failover-procedure.md`
- [ ] Runbooks define decision triggers, step order, validation checks, rollback / failback conditions, and communications
- [ ] Runbooks identify where observability evidence must be captured before, during, and after recovery

### 4. Testing and Drill Cadence

- [ ] Tier 1 services: DR exercise at least annually, plus material-change revalidation
- [ ] Tier 2 services: recovery validation at least annually
- [ ] Backup restore tests are performed regularly enough to support claimed RPO/RTO
- [ ] Test evidence is stored and reviewable: scope, date, participants, outcome, gaps, follow-up actions
- [ ] Failed or partial drills create signals, not quiet exceptions

### 5. Business Continuity

- [ ] Human decision-makers and alternates are named for incident command, platform recovery, communications, privacy/security review, and customer updates
- [ ] Continuity plans include loss of region, loss of core SaaS dependency, and loss of a key operator path (for example identity or secrets outage)
- [ ] Critical knowledge is in runbooks, not only in individuals' heads

## How Compliance Is Ensured in a Running Instance

A running instance is considered compliant only when recovery objectives are wired into operations.

Minimum implementation pattern:

1. **Service tiers are published** and linked to architecture and runbooks.
2. **Backups/replication run continuously** and produce health signals.
3. **Recovery procedures are executable** by the on-call/operations team without rediscovery.
4. **Tests happen on cadence** and produce evidence.
5. **Claims are verified** — if a service claims Tier 1 targets, the drill data must show it can realistically achieve them.

## Observability Requirements

Observability is what turns DR/BCP from a confidence story into a measurable operating capability.

- [ ] Dashboards show replication lag, backup freshness, restore status, dependency health, and recovery-region readiness
- [ ] Failover procedures include telemetry checkpoints for traffic shift, error rate, saturation, latency, queue drain, and data consistency
- [ ] Restore procedures include verification checkpoints for data completeness and application readiness
- [ ] Drill dashboards and event logs retain timestamps for declaration, failover start, failover complete, restore verified, and failback complete where used
- [ ] Alerting exists for backup failure, replication lag beyond RPO tolerance, degraded standby, and unresolved recovery drift

### Why Observability Matters Materially

For availability and continuity, observability is how the framework proves recovery confidence:

- **Detection:** shows when continuity risk starts (replication lag, standby drift, backup failure)
- **Response:** tells operators which dependencies are actually broken and whether recovery prerequisites are met
- **Verification:** confirms that failover/restore produced a healthy and data-consistent system
- **Drills:** produces objective drill timing against RTO/RPO rather than anecdotal “it seemed fine”
- **Evidence:** gives auditors, customers, and leadership a defensible record of readiness and actual recovery performance

## Evaluation Criteria

| Criterion | PASS | FAIL |
|---|---|---|
| Tiering | All critical systems and dependencies have a service tier | Recovery priorities are implicit or ad hoc |
| RTO/RPO targets | Each tier in scope has explicit objectives | Availability language exists without recovery objectives |
| Runbooks | Failover/recovery procedures exist for critical systems | No executable recovery path |
| Test evidence | Drills/restores are performed and evidenced | Targets claimed without testing |
| Observability linkage | Recovery readiness and verification telemetry exist | Recovery confidence depends on manual intuition |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial availability and continuity policy covering service tiers, RTO/RPO, failover/recovery runbooks, annual testing, and observability-backed recovery evidence |
