# Incident Response Policy

> **Applies to:** All production incidents, security incidents, service degradations, customer-visible failures, and operational anomalies
> **Enforced by:** Quality Layer eval agents
> **Authority:** Operations / Security leadership
> **Version:** 1.0.1 | **Last updated:** 2026-03-15

---

## Principles

1. **Fast acknowledgement beats silent analysis** — ownership must be visible early.
2. **Severity drives behavior** — the same incident framework applies everywhere, but targets scale with impact.
3. **Observability is part of response, not a side system** — telemetry proves detection, escalation, mitigation, recovery, and follow-through.
4. **Escalate on evidence, not optimism** — missed targets auto-escalate.

## What This Policy Requires

This policy converts the framework's existing SEV1-SEV4 incident model into time-bound operational commitments.

It requires every running instance to have:

- A common severity model for all production incidents
- Explicit acknowledge / mitigation / resolution targets by severity
- Auto-escalation rules when timing or impact thresholds are breached
- A single incident record with timestamps and evidence
- Observability dashboards and alerts that let operators prove whether targets were met
- Post-incident review for SEV1 and SEV2, and for repeated SEV3 classes

## Deployment-Customizable Decisions

### Must Be Customized Per Instance / Deployment

- On-call rota, paging tool, and escalation contacts
- Service-specific severity criteria (for example: what counts as Tier 1 customer impact)
- Exact communication channels and customer-notification workflow
- Which mitigations may run automatically vs. require human approval
- Any stricter targets required by contract or regulated deployment

### Baseline Targets Defined by This Framework

These are the default enterprise commitments unless a deployment adopts stricter ones.

| Severity | Typical Impact | Acknowledge | Mitigate | Resolve / Stable Service Restored |
|---|---|---:|---:|---:|
| **SEV1** | Broad outage, data integrity/security risk, or major customer/business impact | 15 min | 1 hour | 4 hours |
| **SEV2** | Material degradation with contained blast radius or major feature impaired | 1 hour | 4 hours | 8 hours |
| **SEV3** | Limited degradation, workaround exists, low blast radius | 4 hours | 24 hours | 72 hours |
| **SEV4** | Low-impact defect, informational issue, or non-urgent operational follow-up | 24 hours | 3 business days | 1 week |

If contractual SLAs are stricter than the matrix above, the stricter commitment wins.

## Severity Definitions

### SEV1 — Critical

Use when one or more of the following is true:
- Multi-customer or business-critical outage
- Data loss, corruption, privacy breach, or confirmed active security incident
- Core workflow unavailable with no workaround
- Recovery requires executive coordination, legal/privacy involvement, or emergency change

### SEV2 — Major

Use when one or more of the following is true:
- Significant customer-visible degradation
- Major feature unavailable but business can partially operate
- Single-region or contained outage with meaningful customer impact
- Error budget burn or dependency failure indicates imminent SEV1 risk without intervention

### SEV3 — Minor

Use when:
- Degradation is real but limited in blast radius
- A workaround exists
- Customer impact is measurable but not business-critical
- Action is needed to prevent repeat degradation

### SEV4 — Low

Use when:
- No significant customer impact exists
- Issue is informational, cosmetic, low-frequency, or preventive
- Work can be scheduled through normal operations without elevated coordination

## Mandatory Requirements

### 1. Response Ownership

- [ ] Every incident has an incident lead within the acknowledge window
- [ ] SEV1 and SEV2 incidents open a shared incident record and active coordination channel
- [ ] Incident role assignment is explicit: incident lead, communications owner, technical lead, and scribe/evidence owner where applicable

### 2. SLA Tracking

- [ ] Acknowledge, mitigate, and resolve clocks start from first credible detection or internal awareness, whichever comes first
- [ ] Clock timestamps are recorded automatically where tooling allows
- [ ] Breached clocks auto-escalate to the next leadership level and on-call tier
- [ ] Reclassification is allowed only with explicit rationale captured in the incident record

### 3. Escalation Rules

- [ ] **SEV1:** page primary + secondary on-call immediately; executive, security, or privacy escalation engaged as relevant
- [ ] **SEV2:** page primary on-call immediately; secondary escalation if acknowledge or mitigation targets are missed
- [ ] **SEV3:** create tracked response item; escalate if impact expands, workaround fails, or 24h mitigation target is missed
- [ ] **SEV4:** track in backlog/operations queue; escalate if repeated pattern indicates systemic issue

### 4. Communications

- [ ] SEV1 and SEV2 incidents produce internal status updates at a defined cadence
- [ ] Customer-facing communication thresholds are documented per deployment
- [ ] Privacy/security incidents follow any additional legal or contractual notice obligations

### 5. Post-Incident Review

- [ ] SEV1 and SEV2 incidents require a postmortem using `work/retrospectives/_TEMPLATE-postmortem.md`
- [ ] Repeated SEV3 incidents require postmortem or signal review
- [ ] Follow-up actions must be assigned, dated, and linked to signals or missions where systemic work is required

## How Compliance Is Ensured in a Running Instance

A running instance is compliant only if the targets are operationalized, not merely documented.

Minimum implementation pattern:

1. **Detection path exists** — alerts, anomaly detection, or customer-facing health checks surface credible incidents quickly.
2. **Routing exists** — alerts page the right humans/agents with service ownership, runbook link, and severity hint.
3. **Evidence path exists** — timestamps for detect, acknowledge, mitigate, and resolve are durable.
4. **Escalation exists** — missed targets create a new alert, not a forgotten note.
5. **Verification exists** — mitigation is not accepted until telemetry shows service health stabilizing.

## Observability Requirements

Observability is a hard dependency for incident SLA credibility.

- [ ] Alerts include service, environment, severity hint, runbook, and owning team
- [ ] Incident dashboards show blast radius, active alerts, recent deploys, dependency health, and user impact signals
- [ ] Detection timestamp is captured from monitoring, not reconstructed manually when possible
- [ ] Mitigation timestamp is linked to the first action that measurably improved service health
- [ ] Resolution timestamp requires verified recovery in telemetry, not just “engineer believes it is fixed”
- [ ] Auto-escalation rules are implemented in alerting/incident tooling
- [ ] Observability data supports drills, postmortems, and external evidence requests

### Why Observability Matters Materially

For incident response, observability is how the framework proves reality:

- **Detection:** identifies the earliest trustworthy signal of failure
- **Response:** routes the alert and gives responders shared context fast
- **Verification:** confirms whether rollback, failover, or patching actually worked
- **Evidence:** preserves a defensible timeline for auditors, customers, and retrospectives
- **Learning:** shows repeat patterns, slow handoffs, noisy alerts, and blind spots that policy authors must tighten

## Evaluation Criteria

| Criterion | PASS | FAIL |
|---|---|---|
| Time-bound SLAs | Severity matrix with acknowledge / mitigate / resolve targets is active | Severity language exists but no timings |
| Auto-escalation | Missed targets trigger defined escalation | SLA breach depends on manual noticing |
| Evidence trail | Incident record contains durable timestamps and ownership | Timeline reconstructed ad hoc |
| Observability linkage | Alerts, dashboards, and verification telemetry exist | Incident workflow not materially connected to telemetry |
| Postmortem discipline | High-severity incidents produce review and follow-up | Incidents close without learning loop |

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **SOC 2** | CC7.3 Security incident response | §1 (Response Ownership), §3 (Escalation Rules) |
| **SOC 2** | CC7.4 Incident recovery | §2 (SLA Tracking), Baseline Targets |
| **SOC 2** | CC7.5 Incident identification and analysis | Severity Definitions, §5 (Post-Incident Review) |
| **ISO 27001:2022** | A.16.1 Management of information security incidents | §1 (Response Ownership), §2 (SLA Tracking) |
| **ISO 27001:2022** | A.16.1.2 Reporting information security events | §4 (Communications) |
| **ISO 27001:2022** | A.16.1.5 Response to information security incidents | §3 (Escalation Rules), §1 (Response Ownership) |
| **ISO 27001:2022** | A.16.1.6 Learning from information security incidents | §5 (Post-Incident Review) |
| **NIST AI RMF** | GOVERN 1.5 Ongoing monitoring of AI risks | Observability Requirements, §2 (SLA Tracking) |
| **GDPR** | Art. 33 Notification of data breach to supervisory authority | §4 (Communications), Severity Definitions (SEV1) |
| **GDPR** | Art. 34 Communication of data breach to data subject | §4 (Communications) |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.1 | 2026-03-15 | Add Compliance Mapping section with SOC 2, ISO 27001, NIST AI RMF, and GDPR control references |
| 1.0 | 2026-03-13 | Initial incident response policy with SEV1-SEV4 response targets, auto-escalation, and observability-backed evidence requirements |
