# Failover Procedure: [Service / System]

> **Template version:** 1.0 | **Last updated:** 2026-03-13
> **Owner:** [team / role]
> **Service tier:** Tier 1 | Tier 2 | Tier 3
> **Primary environment:** [region / site]
> **Recovery environment:** [region / site]
> **Target RTO / RPO:** [time] / [time]

---

## Preconditions

- Current incident / drill ID:
- Declaration authority:
- Latest known replication or backup status:
- Known customer impact:

## Trigger Criteria

List the conditions that justify failover:
- [ ] Primary environment unavailable beyond tolerance
- [ ] Data-plane or control-plane dependency unavailable
- [ ] Security / integrity event requires isolation
- [ ] Planned resilience drill

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Incident lead | | Declares failover and coordinates response |
| Technical lead | | Executes traffic/data recovery steps |
| Communications owner | | Internal/customer updates |
| Evidence owner | | Captures timing and telemetry proof |

## Procedure

### 1. Confirm Preconditions
- Validate blast radius and current severity
- Confirm that failover is safer than continued primary recovery
- Freeze risky changes and confirm change window ownership

### 2. Activate Recovery Environment
- Enable or scale standby resources
- Confirm secrets, certificates, connectivity, and dependencies
- Verify data replication status against RPO target

### 3. Shift Traffic / Workload
- Update routing, DNS, load balancer, queue consumers, or scheduler controls
- Record exact start/end times for the traffic shift
- Prevent split-brain or double writers where relevant

### 4. Verify Service Health
- Confirm request success, latency, saturation, queue depth, and dependency health
- Confirm user-facing critical paths work end to end
- Confirm data consistency / write safety

### 5. Communicate and Stabilize
- Publish status update
- Continue monitoring until service is stable within target
- Decide whether to remain on recovery environment or plan failback

## Observability Checkpoints

Capture links or screenshots for:
- Detection timeline
- Replication lag / backup freshness before failover
- Traffic shift success
- Error rate + latency before and after failover
- Data consistency verification
- RTO / RPO actuals

## Failback Conditions

- Primary environment restored and validated
- Data consistency confirmed
- Failback approved by named authority
- Customer communication ready if impact is visible

## Follow-Up

- Postmortem required? yes / no
- Signals to file:
- Runbook updates needed:

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial failover procedure template |
