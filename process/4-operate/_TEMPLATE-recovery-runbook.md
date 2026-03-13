# Recovery Runbook: [Service / System]

> **Template version:** 1.0 | **Last updated:** 2026-03-13
> **Owner:** [team / role]
> **Service tier:** Tier 1 | Tier 2 | Tier 3
> **Target RTO / RPO:** [time] / [time]
> **Dependencies:** [identity, secrets, network, storage, messaging, external SaaS]

---

## Purpose

Document the steps required to restore service and data to an acceptable operating state after outage, corruption, region loss, or dependency failure.

## Recovery Triggers

- Service unavailable beyond tolerance
- Data corruption or failed migration
- Backup restore required
- Failover unsuccessful or not possible
- Declared DR exercise

## Inputs

- Incident / drill ID:
- Last known good backup / snapshot:
- Replication status:
- Latest architecture / dependency map:
- Customer communication state:

## Procedure

### 1. Assess and Declare
- Confirm scope, severity, and affected systems
- Determine whether recovery is restore-in-place, failover, rebuild, or partial service restoration
- Assign incident lead, technical lead, and evidence owner

### 2. Recover Core Dependencies
- Restore access to identity, secrets, certificates, networking, and control-plane prerequisites
- Confirm operators can reach required tooling

### 3. Recover Data
- Restore from backup / snapshot / journal / replica as applicable
- Record chosen restore point and expected data loss window
- Prevent new writes until integrity checks pass where required

### 4. Recover Application / Service Plane
- Deploy or activate known-good service version
- Restore queues, workers, schedulers, and integrations in controlled order
- Re-enable writes and downstream flows only after validation checkpoints pass

### 5. Validate and Return to Service
- Verify customer-critical journeys
- Verify data completeness, latency, saturation, and error rate
- Confirm recovery met or missed RTO / RPO and capture why

## Validation Checklist

- [ ] Backup / restore source documented
- [ ] Data integrity checks passed
- [ ] Critical user journeys passed
- [ ] Health signals stable
- [ ] Communications updated
- [ ] Incident timeline complete

## Observability Evidence

Link the telemetry used to prove recovery:
- Alert/detection view
- Backup freshness / replication status
- Restore job logs or metrics
- Application health dashboard
- Data consistency check results
- Customer-journey synthetic checks

## Escalate If

- Restore point exceeds allowed RPO
- Recovery steps require undocumented tribal knowledge
- Standby or backup media are unhealthy
- Dependency restoration blocks service recovery
- Recovered system is up but not trustworthy

## Follow-Up

- Needed architecture or resilience changes:
- Needed policy changes:
- Drill / incident lessons:

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial recovery runbook template |
