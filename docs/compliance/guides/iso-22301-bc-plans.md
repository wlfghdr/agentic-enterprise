<!-- placeholder-ok -->
# ISO 22301 — Business Continuity Plans

> **Implements:** Documented BC plans per critical process (clause 8.4)
> **Standard:** ISO 22301:2019 — Business Continuity Management Systems
> **Severity:** High — core deliverable of the standard
> **Related issue:** [#140](https://github.com/wlfghdr/agentic-enterprise/issues/140)
> **Related compliance doc:** [ISO 22301 Compliance Reference](../iso-22301.md)

---

## 1. Purpose

ISO 22301 clause 8.4 requires organizations to establish and maintain documented BC plans and procedures to manage disruptions and continue or recover activities within the prioritized timeframes established in the BIA. The plans must define a response structure, activation criteria, communication procedures, roles and responsibilities, resource requirements, and step-by-step recovery procedures.

The Agentic Enterprise framework provides strong incident response capabilities through the [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) with SEV1–4 classification, auto-escalation timers, and structured postmortems. The [Availability Policy](../../../org/4-quality/policies/availability.md) defines DR strategies per availability tier (active-active, active-passive, backup-restore, rebuild). This guide extends those foundations into full BC plans per ISO 22301 — covering the broader scope of business continuity planning: process-level activation criteria, non-technical resource mobilization, stakeholder communication plans, and structured procedures for restoring business operations beyond technology recovery.

This guide provides the BC plan requirements, a BC plan template per critical process, mapping to availability policy tiers and RTO/RPO targets, and a verification checklist.

---

## 2. BC Plan Requirements (Clause 8.4)

ISO 22301 clause 8.4 specifies the following requirements for BC plans and procedures:

| Requirement | Clause Reference | Description |
|-------------|-----------------|-------------|
| Response structure | 8.4.1 | Defined structure for responding to and managing a disruptive incident — roles, authorities, and communication flows |
| Activation criteria | 8.4.2 | Conditions under which the BC plan is activated — thresholds, decision authority, activation procedures |
| Warning and communication | 8.4.3 | Procedures for internal and external communication — who to notify, when, by what means, what information |
| Roles and responsibilities | 8.4.1, 8.4.4 | Named roles for plan execution with clear responsibilities and authorities, including alternates |
| Stabilization procedures | 8.4.4 a) | Immediate actions to stabilize the situation and prevent further escalation |
| Continuity procedures | 8.4.4 b) | Procedures to continue critical activities at an acceptable level during disruption |
| Recovery procedures | 8.4.4 c) | Step-by-step procedures to recover disrupted activities within the RTO |
| Resource requirements | 8.4.4 d) | Resources needed to execute the plan — aligned with BIA minimum resource requirements |
| Stand-down procedures | 8.4.4 | Criteria and procedures for deactivating the BC plan and returning to normal operations |

---

## 3. Response Structure (Clause 8.4.1)

Before individual BC plans, the organization must define an overarching response structure. This integrates with the framework's existing 5-layer model and incident response structure.

### Response Team Structure

| Role | Responsibility | Framework Mapping | Authority |
|------|---------------|-------------------|-----------|
| BC Coordinator | Overall coordination of BC response; decision to activate/deactivate plans | Steering Layer (Layer 0) — human executive | Activate/deactivate BC plans, authorize resource deployment |
| Incident Commander | Technical incident management per Incident Response Policy | Quality Layer (Layer 4) — as defined in Incident Response Policy | Technical decisions within incident scope |
| Communications Lead | Execute communication plan — internal and external stakeholders | Designated human role | Authorize external communications |
| Process Owners | Execute process-specific BC plans for their critical processes | Execution Layer (Layer 3) — division leads or designated owners | Process-level recovery decisions |
| Technology Recovery Lead | Execute technical recovery procedures per availability tier DR strategy | Execution Layer (Layer 3) — SRE / infrastructure | Technical recovery execution |
| Agent Fleet Manager | Manage agent operations during disruption — graceful degradation, failover, restart | Orchestration Layer (Layer 2) | Agent fleet decisions |

### Escalation from Incident Response to BC Plan Activation

Not every incident triggers BC plan activation. The following criteria distinguish normal incident response from BC plan activation:

| Condition | Response | Authority |
|-----------|----------|-----------|
| Incident within single service, RTO achievable via standard IR procedures | Normal incident response per Incident Response Policy | Incident Commander |
| Incident affects multiple critical processes, or RTO at risk of breach | Escalate to BC Coordinator; assess BC plan activation | BC Coordinator |
| Disruption exceeds or is projected to exceed MTPD for any Tier 1 or Tier 2 process | Mandatory BC plan activation | BC Coordinator (mandatory) |
| External event (facility loss, major provider outage, force majeure) | Immediate BC plan activation | BC Coordinator |

---

## 4. BC Plan Template (Per Critical Process)

Create one BC plan per critical process identified in the BIA. Store as governed artifacts (e.g., `docs/compliance/bc-plans/bc-plan-{{PROCESS_ID}}.md`).

```markdown
# Business Continuity Plan — {{PROCESS_NAME}}

> **Process ID:** {{PROCESS_ID — from BIA}}
> **Version:** {{VERSION}}
> **Last updated:** {{YYYY-MM-DD}}
> **Plan owner:** {{PROCESS_OWNER_NAME_AND_ROLE}}
> **Availability tier:** {{Tier 1/2/3/4}}
> **MTPD:** {{From BIA}}
> **RTO:** {{From BIA}}
> **RPO:** {{From BIA}}
> **BIA reference:** {{LINK_TO_BIA}}
> **Review frequency:** Annual (minimum) or after exercise/incident

## 1. Plan Purpose and Scope

This plan covers the continuity and recovery of {{PROCESS_NAME}} in the
event of a disruption. It applies to all scenarios that could prevent
this process from operating within its normal parameters.

### In Scope
- {{List specific components, services, and activities covered}}

### Out of Scope
- {{List items explicitly excluded — reference other BC plans if applicable}}

## 2. Activation Criteria

### Activation Triggers

| Trigger Condition | Detection Method | Activation Decision |
|------------------|-----------------|---------------------|
| {{e.g., "Process unavailable for >15 minutes"}} | {{e.g., "Automated alert from observability platform"}} | {{e.g., "Automatic — Incident Commander activates"}} |
| {{e.g., "Primary infrastructure provider reports major outage"}} | {{e.g., "Provider status page, vendor notification"}} | {{e.g., "BC Coordinator assesses and decides"}} |
| {{e.g., "Dependent process P-04 BC plan activated"}} | {{e.g., "Internal notification from P-04 plan owner"}} | {{e.g., "Automatic — cascade activation"}} |
| {{e.g., "Facility loss affecting operations personnel"}} | {{e.g., "Physical security, management report"}} | {{e.g., "BC Coordinator activates"}} |

### Activation Procedure

1. **Assess:** Incident Commander or BC Coordinator confirms the trigger
   condition is met and normal incident response is insufficient
2. **Decide:** BC Coordinator authorizes plan activation (or activation
   is automatic per trigger criteria above)
3. **Notify:** Communications Lead executes notification procedures
   (Section 4 below)
4. **Mobilize:** Process Owner mobilizes resources per Section 5
5. **Log:** Record activation time, trigger condition, and decision
   rationale in the incident timeline

### Activation Authority

| Authority Level | Who | When |
|----------------|-----|------|
| Primary | {{BC Coordinator name/role}} | Normal business hours |
| Alternate 1 | {{Alternate name/role}} | Outside hours or if primary unavailable |
| Alternate 2 | {{Second alternate name/role}} | If both above unavailable |

## 3. Roles and Responsibilities

| Role | Named Person | Alternate | Responsibilities |
|------|-------------|-----------|-----------------|
| Process Owner | {{Name}} | {{Alternate}} | Overall plan execution, recovery decisions, status reporting |
| Technology Recovery | {{Name}} | {{Alternate}} | Execute technical recovery procedures per availability tier |
| Agent Fleet Manager | {{Name}} | {{Alternate}} | Manage agent degradation/failover/restart for this process |
| Data Recovery | {{Name}} | {{Alternate}} | Restore data to RPO, validate data integrity |
| Stakeholder Liaison | {{Name}} | {{Alternate}} | Coordinate with customers, vendors, regulators as applicable |

## 4. Communication Plan

### Internal Notifications

| When | Who to Notify | Method | Message Content |
|------|--------------|--------|-----------------|
| Plan activated | BC Coordinator, all process team members | {{e.g., "PagerDuty, Slack #bc-incidents"}} | Plan activation notice, trigger condition, initial assessment |
| Every {{N}} hours during disruption | Executive sponsor, dependent process owners | {{e.g., "Email, status call"}} | Status update, estimated recovery time, escalations needed |
| Recovery complete | All notified parties | {{e.g., "Email, Slack"}} | Recovery confirmation, any residual impacts, stand-down notice |

### External Notifications

| When | Who to Notify | Method | Message Content | Authority to Send |
|------|--------------|--------|-----------------|-------------------|
| If SLA breach likely | Affected customers | {{e.g., "Status page, email"}} | Service impact notice, expected resolution | Communications Lead |
| If regulatory threshold met | {{Relevant regulator}} | {{e.g., "Formal notification per regulatory timeline"}} | Incident report per regulatory requirements | BC Coordinator |
| If vendor coordination needed | {{Vendor name}} | {{e.g., "Vendor support channel"}} | Support request, impact details | Technology Recovery |

## 5. Resource Requirements

Minimum resources to resume this process within the RTO (from BIA):

| Resource Category | Minimum Requirement | Source / Location | Pre-positioned? |
|------------------|--------------------|--------------------|----------------|
| Compute infrastructure | {{e.g., "2 instances in DR region"}} | {{e.g., "AWS eu-central-1"}} | {{Yes — warm standby / No — provision on activation}} |
| Data | {{e.g., "Database replica current within RPO"}} | {{e.g., "Cross-region replication"}} | {{Yes / No}} |
| Agent fleet | {{e.g., "Minimum 2 orchestration agents, 4 execution agents"}} | {{e.g., "DR fleet configuration"}} | {{Yes / No}} |
| Credentials and secrets | {{e.g., "DR region secrets store populated"}} | {{e.g., "AWS Secrets Manager (DR region)"}} | {{Yes}} |
| People | {{e.g., "1 SRE, 1 process owner"}} | {{e.g., "On-call rotation"}} | {{N/A}} |
| External services | {{e.g., "LLM API — failover provider"}} | {{e.g., "Provider B API credentials"}} | {{Yes / No}} |
| Documentation | {{e.g., "This BC plan, runbooks, architecture diagrams"}} | {{e.g., "Git repository (mirrored)"}} | {{Yes}} |

## 6. Recovery Procedures

### Phase 1 — Stabilize (Target: within {{N}} minutes of activation)

| Step | Action | Responsible | Verification |
|------|--------|------------|--------------|
| 1.1 | {{e.g., "Confirm scope of disruption — which components are affected"}} | Process Owner | {{e.g., "Component status matrix completed"}} |
| 1.2 | {{e.g., "Isolate affected components to prevent cascading failure"}} | Technology Recovery | {{e.g., "Traffic diverted, affected nodes cordoned"}} |
| 1.3 | {{e.g., "Activate graceful degradation for agent fleet"}} | Agent Fleet Manager | {{e.g., "Agents operating in reduced mode, queue depth stable"}} |
| 1.4 | {{e.g., "Confirm data protection — last backup, replication status"}} | Data Recovery | {{e.g., "RPO confirmed, replication lag documented"}} |

### Phase 2 — Continue at minimum acceptable level (Target: within RTO)

| Step | Action | Responsible | Verification |
|------|--------|------------|--------------|
| 2.1 | {{e.g., "Provision DR infrastructure per resource requirements"}} | Technology Recovery | {{e.g., "DR instances running, health checks passing"}} |
| 2.2 | {{e.g., "Restore data to DR environment from most recent backup/replica"}} | Data Recovery | {{e.g., "Data integrity checks passed, RPO met"}} |
| 2.3 | {{e.g., "Deploy application to DR environment"}} | Technology Recovery | {{e.g., "Application running, smoke tests passed"}} |
| 2.4 | {{e.g., "Redirect traffic to DR environment"}} | Technology Recovery | {{e.g., "DNS updated, traffic flowing, latency acceptable"}} |
| 2.5 | {{e.g., "Restart agent fleet against DR environment"}} | Agent Fleet Manager | {{e.g., "Agents connected, processing requests"}} |
| 2.6 | {{e.g., "Validate minimum acceptable service level"}} | Process Owner | {{e.g., "Core functionality confirmed, SLO metrics within threshold"}} |

### Phase 3 — Recover to normal operations

| Step | Action | Responsible | Verification |
|------|--------|------------|--------------|
| 3.1 | {{e.g., "Root cause analysis of original disruption"}} | Technology Recovery | {{e.g., "RCA documented in retrospective"}} |
| 3.2 | {{e.g., "Restore primary environment"}} | Technology Recovery | {{e.g., "Primary infrastructure healthy"}} |
| 3.3 | {{e.g., "Synchronize data from DR back to primary"}} | Data Recovery | {{e.g., "Data synchronized, consistency verified"}} |
| 3.4 | {{e.g., "Migrate traffic back to primary"}} | Technology Recovery | {{e.g., "Traffic on primary, DR in standby"}} |
| 3.5 | {{e.g., "Restore full agent fleet capacity"}} | Agent Fleet Manager | {{e.g., "Full fleet operational"}} |
| 3.6 | {{e.g., "Confirm normal operations restored"}} | Process Owner | {{e.g., "All SLOs met, no degradation"}} |

## 7. Dependencies on Other BC Plans

| Dependent BC Plan | Process ID | Dependency Type | Coordination Required |
|------------------|-----------|----------------|----------------------|
| {{e.g., "BC Plan — Authentication"}} | P-04 | Hard — this plan cannot succeed without P-04 recovery | {{e.g., "P-04 must reach Phase 2 before this plan can begin Phase 2"}} |
| {{e.g., "BC Plan — Monitoring"}} | P-05 | Soft — degraded execution possible | {{e.g., "Manual monitoring procedures if P-05 not recovered"}} |

## 8. Stand-Down Procedures

### Stand-Down Criteria

- [ ] Process is operating at normal capacity
- [ ] All SLOs are being met
- [ ] Primary environment is restored and verified
- [ ] Data integrity is confirmed with no gaps
- [ ] Root cause is identified and mitigated (or risk accepted)
- [ ] BC Coordinator authorizes stand-down

### Stand-Down Steps

1. BC Coordinator formally deactivates the BC plan
2. Communications Lead sends stand-down notification to all parties
   notified at activation
3. Process Owner confirms handover from DR to normal operations
4. All BC plan activity is logged for the post-incident review
5. Schedule retrospective within {{N}} business days

## 9. Plan Maintenance

| Activity | Frequency | Responsible |
|----------|-----------|------------|
| Review and update plan content | Annual or after exercise/incident | Process Owner |
| Validate contact details and alternates | Quarterly | Process Owner |
| Validate resource availability (DR infrastructure, credentials) | Quarterly | Technology Recovery |
| Exercise this plan (per exercise programme) | Per exercise schedule | BC Coordinator |
| Update after BIA refresh | When BIA is updated | Process Owner |
```

---

## 5. Mapping to Availability Policy Tiers

Each BC plan must align with the availability tier assigned by the BIA. The tier determines the recovery strategy and constrains the plan's recovery procedures:

| Availability Tier | DR Strategy | BC Plan Implications |
|------------------|------------|---------------------|
| Tier 1 — Critical (RTO <1h) | Active-active | Failover is automated; BC plan focuses on validation, communication, and root cause — not manual recovery steps. Phase 2 may be pre-activated (always-on DR). |
| Tier 2 — High (RTO <4h) | Active-passive | Warm standby exists; BC plan includes activation of standby, data synchronization verification, and traffic redirection. |
| Tier 3 — Medium (RTO <24h) | Backup-restore | BC plan includes full provisioning, restore from backup, application deployment, and validation. More detailed recovery steps required. |
| Tier 4 — Low (RTO <72h) | Rebuild | BC plan may include building infrastructure from scratch using infrastructure-as-code. Extended timeline allows for more deliberate recovery. |

---

## 6. Integration with Incident Response Policy

The BC plans extend (not replace) the [Incident Response Policy](../../../org/4-quality/policies/incident-response.md):

| Aspect | Incident Response Policy | BC Plan | Relationship |
|--------|-------------------------|---------|--------------|
| Scope | Individual service incidents (SEV1–4) | Process-level disruption beyond normal IR | BC plan activates when IR is insufficient |
| Activation | Automatic (alert-driven) | Decision-based (BC Coordinator) or automatic (trigger criteria) | IR activates first; escalation to BC if needed |
| Duration | Hours (target: resolve within SLA) | Hours to days (target: recover within RTO) | BC plan governs when disruption exceeds IR timelines |
| Communication | Internal escalation paths | Internal and external stakeholder communication | BC plan adds external communication |
| Recovery | Service restoration | Business process restoration | BC plan is broader — includes non-technical recovery |
| Post-event | Blameless retrospective | Retrospective plus BC plan review and update | Both apply; BC plan review feeds into plan maintenance |

---

## 7. Verification Checklist

### BC Plan Content (Per Plan)
- [ ] Plan is documented for each critical process identified in the BIA
- [ ] Activation criteria are defined with specific, measurable trigger conditions
- [ ] Activation authority and alternates are named
- [ ] Roles and responsibilities are assigned with named individuals and alternates
- [ ] Communication plan covers both internal and external stakeholders
- [ ] Resource requirements match the BIA minimum resource requirements
- [ ] Recovery procedures are step-by-step with responsible party and verification criteria for each step
- [ ] Recovery procedures are structured in phases (stabilize, continue, recover)
- [ ] Dependencies on other BC plans are identified and coordination procedures defined
- [ ] Stand-down criteria and procedures are documented
- [ ] Plan maintenance schedule is defined

### Alignment with Framework
- [ ] RTO and RPO in the BC plan match the BIA and Availability Policy
- [ ] DR strategy in recovery procedures matches the assigned availability tier
- [ ] Escalation from Incident Response Policy to BC plan activation is clearly defined
- [ ] Agent fleet management during disruption is addressed (graceful degradation, failover, restart)
- [ ] Observability and monitoring are maintained during recovery (or manual alternatives documented)

### Governance
- [ ] Each BC plan is version-controlled in the repository
- [ ] Each BC plan has a named owner and is reviewed at least annually
- [ ] BC plans are exercised per the exercise programme (clause 8.5)
- [ ] BC plans are updated after every exercise or real activation
- [ ] BC plan set covers all critical processes within the BCMS scope
- [ ] Contact details and alternates are validated quarterly
