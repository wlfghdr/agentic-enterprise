# Privacy Policy

> **Applies to:** All personal-data processing, product features, AI workflows, support operations, integrations, and customer environments
> **Enforced by:** Quality Layer eval agents
> **Authority:** Privacy / Legal / Security leadership
> **Version:** 1.0 | **Last updated:** 2026-03-13

---

## Principles

1. **Lawful before useful** — if the processing purpose, lawful basis, or controller/processor role is unclear, the work is not ready.
2. **Purpose-bound and minimal** — collect, store, and use only the personal data required for the documented purpose.
3. **Deployment-aware compliance** — privacy obligations are partly fixed by law and partly configurable per deployment; both must be explicit.
4. **Evidence over assertion** — runtime controls, logs, and approvals must prove that privacy commitments are actually being followed.

## What This Policy Requires

This policy makes GDPR-relevant privacy controls explicit for running instances of the framework.

It requires every deployment to define and maintain:

- A documented **controller / processor role model** for each product surface and integration
- A documented **lawful basis** for each personal-data processing purpose
- A signed or approved **Data Processing Agreement (DPA)** whenever the organization acts as processor for customer data
- A runnable **data subject rights process** covering access, rectification, erasure, restriction, objection, and portability where applicable
- A **personal data breach workflow** that supports assessment, containment, evidence capture, and supervisory-authority notification within 72 hours when required
- A **DPIA gate** for high-risk processing, especially profiling, large-scale monitoring, special-category data, or novel AI use cases
- A documented **international transfer mechanism** for transfers outside the EEA/UK/adequate jurisdictions
- **Consent requirements** where consent is the chosen lawful basis, including withdrawal handling and evidence retention

## Deployment-Customizable Decisions

The framework defines the control categories. Each company fork or production deployment must configure the instance-specific details.

### Must Be Customized Per Instance / Deployment

- **Controller / processor allocation** by product, workflow, and region
- **Record of processing activities** and system inventory
- **Lawful basis mapping** by purpose
- **DPA commercial terms** and subprocessors
- **DSAR intake channels**, approvers, identity-verification method, and fulfillment tooling
- **Breach notification contacts** (privacy lead, legal, security, supervisory authority path, customer contacts)
- **Retention schedules** and deletion windows
- **Cross-border transfer mechanism** (e.g. adequacy decision, SCCs, UK IDTA/addendum, equivalent local mechanism)
- **DPO designation** or explicit rationale if not legally required
- **Consent UX and records** if consent is used

### Must Not Be Customized Away

- The need to document lawful basis before launch
- The need for a DPA when acting as processor
- The need to support DSAR handling
- The 72-hour supervisory-authority notification clock when GDPR Art. 33 applies
- The requirement to run a DPIA for high-risk processing
- The requirement to have a lawful transfer mechanism for cross-border transfers

## Mandatory Requirements

### 1. Role, Purpose, and Lawful Basis

- [ ] Every feature, workflow, and integration that processes personal data documents: purpose, data categories, role (controller / processor / joint controller), lawful basis, retention rule, and transfer path
- [ ] Processing without a documented lawful basis is blocked
- [ ] Sensitive or high-risk processing is flagged for DPIA review before build or rollout
- [ ] AI features document whether prompts, outputs, traces, or feedback may contain personal data

### 2. Data Processing Agreements (DPA)

- [ ] A DPA is executed before customer personal data is processed on the customer's behalf
- [ ] The DPA identifies subject matter, duration, nature and purpose of processing, categories of data, and categories of data subjects
- [ ] Security, confidentiality, subprocessors, audit support, deletion/return, and breach-notification duties are covered
- [ ] Subprocessor changes follow the DPA notice/objection mechanism
- [ ] The active DPA template originates from `work/decisions/_TEMPLATE-data-processing-agreement.md` or an approved legal equivalent

### 3. Data Subject Access Requests (DSAR)

- [ ] A DSAR runbook exists and is operationally owned (`process/4-operate/dsar-runbook.md`)
- [ ] Intake channels are published and monitored
- [ ] Identity verification is proportionate to request sensitivity
- [ ] Search, review, export, correction, deletion, and exception handling steps are defined
- [ ] Response deadlines are configured per jurisdiction; GDPR default: respond without undue delay and within one month unless validly extended
- [ ] All DSAR actions produce an audit trail: request time, verifier, systems searched, decision, fulfillment date, and exception rationale

### 4. Personal Data Breach Handling

- [ ] Personal-data breaches are triaged separately from general incidents when personal data may be involved
- [ ] The incident process determines whether the event constitutes a personal-data breach, affected data categories, affected jurisdictions, and likely risk to individuals
- [ ] If GDPR Art. 33 applies, supervisory-authority notification must be prepared without undue delay and within 72 hours after awareness
- [ ] If notification is delayed, reasons are recorded
- [ ] Customer / controller notification duties are contractually and operationally mapped
- [ ] If GDPR Art. 34 applies, communication to affected individuals must be prepared using approved legal/privacy review

### 5. DPIA and High-Risk Processing

- [ ] A DPIA is required before deploying processing likely to result in high risk to rights and freedoms
- [ ] DPIA outcomes must be tracked to mitigation actions, design changes, or a launch block
- [ ] AI features using profiling, automated decision support, large-scale monitoring, or special-category data require explicit DPIA review
- [ ] The approved template is `work/decisions/_TEMPLATE-data-protection-impact-assessment.md`

### 6. Consent and Preference Management

- [ ] Consent is used only where it is the correct lawful basis
- [ ] Consent capture records what the user agreed to, when, how, and from which surface
- [ ] Withdrawal of consent is as easy as giving consent
- [ ] Runtime systems propagate consent changes to downstream processors without undue delay

### 7. International Transfers

- [ ] Transfers outside covered jurisdictions are mapped and justified
- [ ] Each non-adequacy transfer uses an approved mechanism (for example SCCs) plus any required transfer-risk assessment or addendum
- [ ] Subprocessors and storage locations are current and reviewable by customers or auditors

## How Compliance Is Ensured in a Running Instance

Privacy compliance is not just a document set. In a running instance, the minimum enforceable pattern is:

1. **Design-time metadata** — each feature records purpose, lawful basis, role, retention, and transfer path.
2. **Contract gate** — a customer environment cannot move to live personal-data processing without an executed DPA or approved equivalent.
3. **Runtime controls** — retention jobs, access controls, deletion tooling, consent propagation, and export paths are implemented in the execution layer.
4. **Operational runbooks** — DSAR, breach handling, and DPIA review are routinized in Loop 4, not reinvented per incident.
5. **Audit evidence** — tickets, approvals, access logs, deletion logs, and observability events prove what happened.

## Observability Requirements for Privacy Evidence

Observability does not replace legal judgment, but it materially improves provability and response quality.

- [ ] DSAR workflows emit events for intake, verification, search completion, decision, fulfillment, and closure
- [ ] Breach workflows emit timestamps for detection, awareness, triage, notification decision, notification sent, and containment verified
- [ ] Privacy-relevant admin actions (export, delete, restore, retention override) are logged with actor, reason, scope, and trace correlation where possible
- [ ] Telemetry used for evidence must avoid unnecessary personal data; logs and traces must be sanitized per `security.md` and `observability.md`
- [ ] Dashboards exist for DSAR aging, breach clock status, and overdue privacy actions

## Evaluation Criteria

| Criterion | PASS | FAIL |
|---|---|---|
| Lawful basis coverage | Every personal-data use has role + lawful basis documented | Processing purpose exists without lawful basis or role clarity |
| DPA readiness | Processor relationships covered by signed DPA or approved equivalent | Customer personal data processed without DPA |
| DSAR operability | Intake, identity verification, search, fulfillment, and evidence path defined | Rights requests handled ad hoc |
| Breach handling | 72-hour workflow, customer notice path, and evidence capture defined | No breach-notification path or unclear ownership |
| DPIA gate | High-risk processing blocked pending DPIA | High-risk processing can launch without review |
| Transfer controls | Cross-border transfer mechanism documented | International transfers occur without lawful mechanism |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial privacy policy covering GDPR role/lawful-basis mapping, DPA, DSAR, breach notification, DPIA, consent, and transfer controls |
