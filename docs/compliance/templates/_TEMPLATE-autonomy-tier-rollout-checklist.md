# Autonomy Tier Rollout Checklist

> **Template version:** 1.0
> **Last updated:** 2026-03-27
> **Purpose:** Provide a concrete governance record before moving an agent, workflow, or team to a higher autonomy tier
> **Related policy:** [`org/4-quality/policies/risk-management.md`](../../../org/4-quality/policies/risk-management.md) §2.3 Workforce Readiness by Autonomy Tier

---

## Document Control

| Field | Value |
|-------|-------|
| Rollout ID | ATR-YYYY-NNN |
| Version | {{VERSION}} |
| Owner | {{OWNER}} |
| Requested by | {{REQUESTOR}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review date | {{REVIEW_DATE}} |
| Related artifacts | {{RISK_REGISTER / AI_SYSTEM_INVENTORY / RELEASE_CONTRACT / RUNBOOK / DASHBOARD}} |

## How to Use This Template

1. Complete this checklist before raising the autonomy tier of an existing agent, workflow, or operating team.
2. Use one checklist per autonomy change request. Do not combine unrelated systems into a single approval record.
3. Treat unchecked items as blockers unless a documented exception exists.
4. Keep links to the observability dashboard, override path, and communication record current.

## 1. Requested Autonomy-Tier Change

| Field | Value |
|-------|-------|
| System / workflow / team name | {{NAME}} |
| Current autonomy tier | {{1 / 2 / 3 / 4}} |
| Requested autonomy tier | {{1 / 2 / 3 / 4}} |
| Scope of change | {{WHAT IS MOVING TO HIGHER AUTONOMY}} |
| Business reason | {{WHY THIS CHANGE IS REQUESTED}} |
| Expected benefits | {{SPEED / COST / QUALITY / COVERAGE}} |
| Key risks introduced by the change | {{OVERSIGHT / QUALITY / SECURITY / COMPLIANCE / CUSTOMER IMPACT}} |
| Planned start date | {{DATE}} |
| Planned review checkpoint | {{DATE}} |

## 2. Named Human Roles

| Responsibility | Named role / person | Confirmed? | Notes |
|----------------|---------------------|------------|-------|
| Business owner | {{NAME}} | yes / no | |
| Approver for tier change | {{NAME}} | yes / no | |
| Day-to-day supervisor / monitor | {{NAME}} | yes / no | |
| Override / kill-switch owner | {{NAME}} | yes / no | |
| Incident / post-incident reviewer | {{NAME}} | yes / no | |
| Observability / monitoring owner | {{NAME}} | yes / no | |
| Training / readiness signoff owner | {{NAME}} | yes / no | |
| Communications / change-management owner | {{NAME}} | yes / no | |

## 3. Readiness and Training Signoff

| Check | Status | Evidence / link |
|------|--------|-----------------|
| Affected approvers, supervisors, or operators know the new autonomy scope and limits | [ ] | {{LINK}} |
| Failure modes, escalation triggers, and override paths were reviewed with the human roles above | [ ] | {{LINK}} |
| Required dashboards, alerts, or queues were demonstrated to the monitoring team | [ ] | {{LINK}} |
| Training or enablement for the new operating mode is complete | [ ] | {{LINK}} |
| Readiness signoff recorded by the named training / readiness owner | [ ] | {{LINK}} |

## 4. Observability and Monitoring Readiness

| Check | Status | Evidence / link |
|------|--------|-----------------|
| Monitoring owner is named and reachable during the rollout window | [ ] | {{NAME / LINK}} |
| Dashboard for the autonomy change exists and is linked | [ ] | {{DASHBOARD_LINK}} |
| Alerts cover the main failure or drift conditions for this higher tier | [ ] | {{ALERT_LINK}} |
| Human override, escalation, and anomaly signals are visible in telemetry | [ ] | {{QUERY / DASHBOARD}} |
| Review cadence for the rollout period is defined | [ ] | {{CADENCE}} |

## 5. Rollback and Override Path

| Field | Value |
|-------|-------|
| Primary rollback / downgrade mechanism | {{KILL SWITCH / FEATURE FLAG / PROCESS REVERSION / TIER RESET}} |
| Expected rollback time | {{TIME}} |
| Manual override path | {{HOW A HUMAN STOPS OR OVERRIDES THE SYSTEM}} |
| Trigger conditions for rollback or downgrade | {{HEALTH / QUALITY / COMPLIANCE / HUMAN BURDEN THRESHOLDS}} |
| Runbook link | {{RUNBOOK_LINK}} |
| Rollback owner on duty | {{NAME}} |
| Rollback / override drill completed | yes / no |

## 6. Communication and Change Management

| Check | Status | Evidence / link |
|------|--------|-----------------|
| Affected teams were told what is changing and when | [ ] | {{LINK}} |
| Teams know who supervises, approves, and overrides the higher-autonomy workflow | [ ] | {{LINK}} |
| Customer, partner, or compliance stakeholders were notified if required | [ ] | {{LINK}} |
| Change-management owner confirms communication is complete | [ ] | {{LINK}} |

## 7. Approval Decision

### Recommendation

- [ ] Approve the autonomy-tier increase as proposed
- [ ] Approve with conditions listed below
- [ ] Reject until blockers are resolved

### Conditions / Blockers

- [Condition or blocker]
- [Condition or blocker]

### Signoff

| Role | Name | Decision / date |
|------|------|------------------|
| Owner | {{NAME}} | {{APPROVED / REJECTED — DATE}} |
| Approver | {{NAME}} | {{APPROVED / REJECTED — DATE}} |
| Supervisor / monitoring owner | {{NAME}} | {{APPROVED / REJECTED — DATE}} |

## 8. Post-Rollout Review

| Check | Status | Notes |
|------|--------|-------|
| First review checkpoint completed | [ ] | |
| Monitoring burden remained operationally realistic | [ ] | |
| Override / escalation path worked as expected | [ ] | |
| Unexpected workforce or customer impact captured | [ ] | |
| Follow-up actions recorded | [ ] | |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial autonomy-tier rollout checklist |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-27 | Initial adopter-facing checklist for autonomy-tier increases, including ownership, readiness, monitoring, rollback, and communication controls |
