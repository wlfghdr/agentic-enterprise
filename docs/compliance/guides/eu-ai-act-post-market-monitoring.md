<!-- placeholder-ok -->
# EU AI Act — Post-Market Monitoring & Serious Incident Reporting Guide

> **Implements:** Post-market monitoring system (Art. 72) and serious incident reporting (Art. 62)
> **Regulation:** EU AI Act (Regulation 2024/1689)
> **Severity:** Critical — mandatory obligations from the moment a high-risk AI system is placed on the EU market
> **Related issue:** [#131](https://github.com/wlfghdr/agentic-enterprise/issues/131)
> **Related compliance doc:** [EU AI Act Compliance Reference](../eu-ai-act.md)
> **Companion guides:** [Conformity Assessment](eu-ai-act-conformity-assessment.md), [CE Marking & Registration](eu-ai-act-ce-marking.md)

---

## 1. Purpose

The EU AI Act imposes two distinct post-market obligations on providers of high-risk AI systems:

1. **Post-market monitoring system (Art. 72):** Providers must establish and document a post-market monitoring (PMS) system that actively and systematically collects, analyses, and evaluates data on the AI system's performance throughout its lifetime. The PMS plan must be part of the technical documentation (Annex IV) and must feed data back into the risk management system (Art. 9). The PMS system must be proportionate to the nature of the AI technologies and the risks of the high-risk AI system.

2. **Serious incident reporting (Art. 62):** Providers must report serious incidents — those that directly or indirectly lead to, or are realistically likely to lead to, death, serious damage to health, serious disruption of critical infrastructure, breach of fundamental rights obligations, or serious damage to property or the environment — to the market surveillance authority of the member state where the incident occurred. Initial reports must be filed within 15 days of becoming aware of the incident, or within 2 days for widespread infringements.

The Agentic Enterprise framework provides strong **observability infrastructure** (OTel-based telemetry, the [Observability Policy](../../../org/4-quality/policies/observability.md), and the [OTel contract](../../otel-contract.md)) and a mature **incident response process** (the [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) with SEV1-4 classification and retrospectives). This guide extends those capabilities with:

- A **formal PMS plan** aligned to Art. 72 requirements
- A mapping from framework observability data to EU AI Act PMS data collection obligations
- An **Art. 62 serious incident classification** step in the incident response workflow
- **Regulatory reporting timelines and procedures** for notifying national market surveillance authorities
- Templates for the PMS plan and serious incident reports

This guide maps the framework's existing capabilities to the EU AI Act's post-market obligations and provides the additional procedures, templates, and checklists adopters need.

---

## 2. Post-Market Monitoring System (Art. 72)

### 2a. Regulatory Requirements

Art. 72 requires providers of high-risk AI systems to establish a post-market monitoring system that is:

| Requirement | Description | Art. 72 Reference |
|-------------|-------------|-------------------|
| **Documented** | A PMS plan must exist as part of the technical documentation (Annex IV) | Art. 72(1) |
| **Active and systematic** | The system must actively collect, document, and analyse relevant data — not merely react to complaints | Art. 72(1) |
| **Proportionate** | The scope and depth of monitoring must be proportionate to the nature of the AI technologies and the risks | Art. 72(1) |
| **Continuous** | Monitoring must cover the entire lifetime of the AI system, not just an initial period | Art. 72(1) |
| **Performance-focused** | Data collection must allow evaluation of the AI system's continuous compliance with Chapter III, Section 2 requirements | Art. 72(2) |
| **Risk-feeding** | PMS data must feed back into the risk management system (Art. 9) to update risk assessments | Art. 72(3) |
| **Corrective-action-triggering** | The PMS system must trigger corrective or preventive actions when non-compliance or risks are identified | Art. 72(4) |

### 2b. Mapping Framework Observability to PMS Requirements

The framework's OTel-based observability platform provides the data collection infrastructure for Art. 72 compliance. The following table maps PMS data requirements to existing framework capabilities.

| PMS Data Requirement | Framework Capability | Source Artifact | Action Needed |
|---------------------|---------------------|-----------------|-------------------|
| AI system performance metrics | OTel spans with `gen_ai.*` attributes (latency, token usage, model ID) | [OTel contract](../../otel-contract.md) Section 3 | Add AI-specific accuracy and drift metrics as custom OTel attributes |
| Error and failure rates | OTel span status codes, `otel.status_code`, `error.type` attributes | [OTel contract](../../otel-contract.md) Section 3 | Configure alerting thresholds specific to the AI system's risk profile |
| Governance decisions | `governance.decision` span events with `governance.decision`, `governance.reason` attributes | [OTel contract](../../otel-contract.md) Section 6.1 | Already captured — include in PMS periodic reports |
| User interactions and feedback | Application-layer telemetry, deployer feedback channels | [Observability Policy](../../../org/4-quality/policies/observability.md) | Establish structured deployer feedback collection mechanism |
| Incident data | Incident response records, retrospectives | [Incident Response Policy](../../../org/4-quality/policies/incident-response.md), `work/retrospectives/` | Add Art. 62 classification step (see Section 3) |
| Bias and fairness indicators | Not currently instrumented | — | Implement fairness metrics as custom OTel metrics; define acceptable thresholds |
| Accuracy drift detection | Not currently instrumented | — | Implement periodic accuracy evaluation against baseline; emit as OTel gauge metric |
| Usage pattern analysis | OTel span attributes: `ae.layer`, `ae.agent.type`, `ae.mission.id` | [OTel contract](../../otel-contract.md) Section 4 | Aggregate to detect deployment in unintended contexts |
| Corrective action records | Improvement signals, retrospective action items | `work/signals/`, `work/retrospectives/` | Link PMS findings to corrective action tracking |

### 2c. What Adopters Must Add

Beyond the existing framework capabilities, adopters must implement the following to satisfy Art. 72:

1. **Documented PMS plan** — Use the template in Section 5 of this guide to create a PMS plan specific to each high-risk AI system. The plan becomes part of the Annex IV technical documentation.

2. **Periodic evaluation triggers** — Define evaluation frequency based on risk level:

   | Risk Level | Evaluation Frequency | Trigger Conditions |
   |-----------|---------------------|--------------------|
   | High (Annex III areas 1, 6, 7, 8) | Monthly | Any SEV1/SEV2 incident, accuracy drop > 5%, bias metric breach |
   | Standard high-risk (other Annex III areas) | Quarterly | Any SEV1/SEV2 incident, accuracy drop > 10%, bias metric breach |
   | Post-substantial-modification | Immediately | Any change classified as substantial modification per Art. 3(23) |

3. **Data collection procedures** — For each data type in the mapping table above, document: what is collected, how it is collected, where it is stored, who is responsible for analysis, and what retention period applies (minimum: AI system lifetime + 10 years).

4. **Corrective action links** — Establish a formal process linking PMS findings to the framework's improvement signal mechanism:
   - PMS finding identified → file improvement signal in `work/signals/` with source `pms-art72`
   - Signal triaged by Steering Layer → mission created if remediation required
   - Corrective action implemented → PMS finding closed with reference to the implementing PR or mission
   - If the finding indicates non-compliance with Chapter III, Section 2 → trigger re-evaluation of conformity assessment

5. **Reporting to market surveillance authorities** — Art. 72(4) requires providers to make PMS data available to market surveillance authorities on request. Establish a process for:
   - Responding to authority data requests within the timelines set by national law
   - Producing PMS summary reports on demand
   - Granting access to relevant OTel dashboards or data exports (where the authority requests real-time or near-real-time access)

---

## 3. Serious Incident Reporting (Art. 62)

### 3a. What Constitutes a "Serious Incident"

Art. 3(49) defines a "serious incident" as an incident or malfunctioning of a high-risk AI system that directly or indirectly leads to, or is realistically likely to lead to, any of the following:

| Category | Description | Examples |
|----------|-------------|---------|
| **Death or serious damage to health** | The AI system's output, failure, or malfunction causes or is realistically likely to cause death or serious physical/mental health damage to a person | An AI triage system misclassifies a critical patient; an AI-controlled industrial system causes physical injury |
| **Serious disruption of critical infrastructure** | Serious and irreversible disruption of the management or operation of critical infrastructure | An AI managing electricity grid operations causes a widespread outage; an AI traffic management system causes a major transport disruption |
| **Breach of fundamental rights obligations** | Breach of obligations under Union law intended to protect fundamental rights | An AI recruitment system systematically discriminates on a protected characteristic; an AI benefits system denies eligible persons access to essential services |
| **Serious damage to property or environment** | Significant property damage or environmental harm caused by the AI system | An AI-controlled process causes a chemical spill; an AI system causes significant financial loss through erroneous automated decisions |

**Important:** The threshold is "realistically likely to lead to" — not only incidents where harm has already materialized. Near-misses that could realistically have caused serious harm are reportable.

### 3b. Mapping Framework Incident Severity to Art. 62 Classification

The framework's [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) uses a SEV1-4 classification. Adopters must add an Art. 62 classification step to determine whether an incident also meets the "serious incident" threshold under the EU AI Act.

| Framework Severity | Description | Art. 62 Classification | Action |
|-------------------|-------------|----------------------|--------|
| **SEV1** — Critical | Service down, data breach, safety risk | **Likely serious incident** — assess against Art. 3(49) categories immediately | Initiate Art. 62 reporting in parallel with incident response |
| **SEV2** — Major | Major feature degraded, significant user impact | **Possible serious incident** — assess within 24 hours | Evaluate against Art. 3(49); escalate to regulatory affairs if threshold met |
| **SEV3** — Minor | Minor feature degraded, workaround available | **Unlikely serious incident** — document assessment | Record Art. 62 classification rationale in incident record |
| **SEV4** — Low | Cosmetic, minimal impact | **Not a serious incident** — no Art. 62 action | No additional action required |

**Critical addition to incident response procedure:** Every SEV1 and SEV2 incident involving a high-risk AI system must include an explicit Art. 62 classification step. This classification must be documented in the incident record and, if the incident meets the serious incident threshold, immediately escalated to the provider's regulatory affairs function.

### 3c. Reporting Timelines

| Incident Type | Initial Report Deadline | Report To | Follow-up |
|--------------|------------------------|-----------|-----------|
| **Serious incident** (death, serious harm to health/safety, fundamental rights breach, property/environment damage) | **Within 15 days** of becoming aware that the incident is a serious incident | Market surveillance authority of the member state where the incident occurred | As requested by the authority, or when new material information becomes available |
| **Widespread infringement** (serious incident indicating a breach affecting or likely to affect more than one member state) | **Within 2 days** of becoming aware | Market surveillance authority of the member state where the incident occurred, plus notification to authorities in all affected member states | Immediate follow-up as requested |
| **Death or serious damage to health** | **Within 10 days** of becoming aware (stricter subset of the 15-day rule) | Market surveillance authority of the member state where the incident occurred | Immediate follow-up with investigation results |

**"Becoming aware"** means the moment the provider (or any person acting on the provider's behalf) first learns that a serious incident has occurred that may reasonably be linked to the AI system — not the moment of root cause confirmation.

### 3d. Required Information in a Serious Incident Report

Each report must contain, at minimum:

| Information Element | Description |
|--------------------|-------------|
| Provider identification | Legal name, address, contact details, EU authorized representative (if applicable) |
| AI system identification | Name, version, unique identifier, EU database registration number |
| Incident description | What happened, when, where, and how the AI system was involved |
| Serious incident classification | Which Art. 3(49) category applies, with rationale |
| Persons affected | Number and categories of persons affected or potentially affected |
| Impact assessment | Severity, scope, and reversibility of the harm caused or likely to be caused |
| Corrective actions taken | Immediate actions to contain the incident, mitigate harm, and prevent recurrence |
| Root cause analysis | Preliminary or final determination of why the incident occurred (if known at time of report) |
| Corrective actions planned | Long-term remediation measures, timeline for implementation |
| Previous incidents | Any related previous incidents involving the same AI system |

### 3e. National Authority Contacts Process

Adopters must establish a process for identifying and maintaining contact details for market surveillance authorities in each EU member state where their high-risk AI system is deployed:

1. **Pre-deployment:** Before placing the AI system on the market in any member state, identify the designated market surveillance authority for AI in that member state. The European Commission maintains a list of national competent authorities.

2. **Contact registry:** Maintain an internal registry of national authority contact details, including:
   - Authority name and department responsible for AI
   - Postal address, email, phone number
   - Preferred reporting format (if specified by the member state)
   - Language requirements for reports

3. **Periodic verification:** Review and update the contact registry at least annually, or whenever deploying in a new member state.

4. **Reporting channel:** Establish an internal escalation path from incident response to regulatory affairs that can execute a report submission within the required timelines:

   ```
   Incident detected
     → SEV classification (Incident Response Policy)
     → Art. 62 classification (this guide, Section 3b)
     → If serious incident: escalate to regulatory affairs within 24 hours
     → Regulatory affairs drafts report (Section 6 template)
     → Report submitted to national authority within 15 days (or 2 days)
     → Follow-up reports as required
   ```

---

## 4. Integration with Framework

### 4a. OTel Observability Data → PMS Requirements

The framework's [OTel contract](../../otel-contract.md) defines the telemetry architecture. The following table maps specific OTel data to Art. 72 PMS requirements.

| Art. 72 PMS Requirement | OTel Data Source | Implementation |
|------------------------|-----------------|----------------|
| Continuous performance monitoring | `gen_ai.*` span attributes (latency, token counts, model) | Configure dashboards tracking performance trends over time; set anomaly detection alerts |
| Compliance verification | `governance.decision` span events | Aggregate governance decisions to verify human oversight is functioning; flag periods without human review |
| Error tracking | `otel.status_code = ERROR`, `error.type` attributes | Track error rates by AI system component; alert on threshold breaches |
| Usage pattern analysis | `ae.layer`, `ae.agent.type`, `ae.mission.id` resource attributes | Build usage heatmaps; detect deployment outside intended purpose |
| Security event monitoring | `tool.execute` spans for security-relevant operations | Correlate with [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) threat model |
| Data quality indicators | Custom metrics (to be implemented) | Instrument input data quality checks as OTel metrics; alert on degradation |

### 4b. Incident Response Policy → Art. 62 Classification

The framework's [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) provides the operational incident management structure. To integrate Art. 62:

| Incident Response Phase | Art. 62 Integration |
|------------------------|-------------------|
| **Detection** | All alerts from AI system monitoring are tagged with `ai_system: true` and the EU database registration ID |
| **Triage (SEV classification)** | Add Art. 62 classification step immediately after SEV determination for all AI-system-related incidents |
| **Response** | If Art. 62 threshold met: activate regulatory reporting path in parallel with technical response |
| **Communication** | Add national market surveillance authority to stakeholder notification matrix for serious incidents |
| **Retrospective** | Include Art. 62 reporting compliance in retrospective scope; verify reporting timelines were met |

### 4c. Retrospectives Process → PMS Feedback Loop

The framework's retrospective process (`work/retrospectives/`) already captures structured lessons learned from incidents. To satisfy Art. 72's requirement that PMS data feeds back into the risk management system:

1. **Tag retrospectives** involving high-risk AI systems with `pms-relevant: true`
2. **Extract PMS-relevant findings** from each tagged retrospective and include in the next PMS periodic evaluation
3. **Update the risk register** with any new or changed risks identified through the retrospective
4. **Verify corrective actions** from retrospectives are tracked to completion and their effectiveness is measured in subsequent PMS evaluations

---

## 5. Post-Market Monitoring Plan Template

Adopters should complete one PMS plan per high-risk AI system. The completed plan becomes part of the Annex IV technical documentation.

```
POST-MARKET MONITORING PLAN
pursuant to Article 72 of Regulation (EU) 2024/1689

1. AI SYSTEM IDENTIFICATION
   Name:                    {{AI_SYSTEM_NAME}}
   Version:                 {{VERSION}}
   EU database reg. ID:     {{REGISTRATION_ID}}
   Risk classification:     High-risk (Annex III, area {{AREA_NUMBER}})
   Intended purpose:        {{INTENDED_PURPOSE}}
   Date of market entry:    {{YYYY-MM-DD}}
   PMS plan version:        {{PMS_PLAN_VERSION}}
   PMS plan date:           {{YYYY-MM-DD}}

2. MONITORING OBJECTIVES
   - [ ] Verify continuous compliance with Art. 9 (risk management)
   - [ ] Verify continuous compliance with Art. 10 (data governance)
   - [ ] Verify continuous compliance with Art. 12 (logging)
   - [ ] Verify continuous compliance with Art. 13 (transparency)
   - [ ] Verify continuous compliance with Art. 14 (human oversight)
   - [ ] Verify continuous compliance with Art. 15 (accuracy, robustness, cybersecurity)
   - [ ] Detect accuracy drift and performance degradation
   - [ ] Detect bias drift and emergent discriminatory patterns
   - [ ] Detect deployment in unintended contexts
   - [ ] Identify new or changed risks
   - [ ] Collect and analyse deployer and end-user feedback
   - [ ] Additional objectives: {{SYSTEM_SPECIFIC_OBJECTIVES}}

3. DATA COLLECTION METHODS
   | Data Category            | Collection Method       | Frequency    | Responsible    | Storage Location       |
   |--------------------------|-------------------------|-------------|----------------|------------------------|
   | Performance metrics      | OTel spans/metrics      | Continuous  | {{TEAM}}       | {{OBSERVABILITY_PLATFORM}} |
   | Error and failure data   | OTel error spans        | Continuous  | {{TEAM}}       | {{OBSERVABILITY_PLATFORM}} |
   | Accuracy benchmarks      | Periodic evaluation     | {{FREQ}}    | {{TEAM}}       | {{LOCATION}}           |
   | Bias/fairness metrics    | Periodic evaluation     | {{FREQ}}    | {{TEAM}}       | {{LOCATION}}           |
   | Usage pattern data       | OTel span aggregation   | Continuous  | {{TEAM}}       | {{OBSERVABILITY_PLATFORM}} |
   | Deployer feedback        | {{METHOD}}              | {{FREQ}}    | {{TEAM}}       | {{LOCATION}}           |
   | End-user feedback        | {{METHOD}}              | {{FREQ}}    | {{TEAM}}       | {{LOCATION}}           |
   | Incident data            | Incident response system| Continuous  | {{TEAM}}       | {{LOCATION}}           |
   | Security events          | OTel + SIEM             | Continuous  | {{TEAM}}       | {{LOCATION}}           |

4. ANALYSIS METHODOLOGY
   - Performance trend analysis:     {{DESCRIBE_METHOD}}
   - Accuracy drift detection:       {{DESCRIBE_METHOD}}
   - Bias drift detection:           {{DESCRIBE_METHOD}}
   - Usage pattern anomaly detection: {{DESCRIBE_METHOD}}
   - Root cause analysis:            {{DESCRIBE_METHOD}}
   - Statistical methods used:       {{LIST_METHODS}}

5. EVALUATION FREQUENCY
   | Evaluation Type          | Frequency   | Scope                                   |
   |--------------------------|-------------|------------------------------------------|
   | Automated monitoring     | Continuous  | All OTel-instrumented metrics and traces |
   | Performance review       | {{FREQ}}    | Accuracy, latency, error rates           |
   | Bias/fairness audit      | {{FREQ}}    | All protected characteristics             |
   | Comprehensive PMS review | {{FREQ}}    | All monitoring objectives (Section 2)    |
   | Ad hoc review            | On trigger  | Triggered by incident, complaint, or alert|

6. CORRECTIVE ACTION TRIGGERS
   | Trigger Condition                              | Action                                              |
   |------------------------------------------------|------------------------------------------------------|
   | Accuracy drops below {{THRESHOLD}}             | Initiate investigation; file improvement signal       |
   | Bias metric exceeds {{THRESHOLD}}              | Halt affected decision path; investigate; remediate   |
   | SEV1/SEV2 incident involving AI system         | Art. 62 classification; PMS ad hoc review             |
   | Deployment detected outside intended purpose   | Notify deployer; assess risk; escalate if necessary   |
   | Deployer reports unexpected behavior           | Investigate; assess against Art. 3(49) categories     |
   | Market surveillance authority request          | Produce PMS summary report within requested timeline  |
   | Substantial modification planned               | Trigger pre-modification PMS review and re-assessment |

7. RESPONSIBLE PERSONS
   | Role                           | Name / Team  | Responsibilities                           |
   |--------------------------------|--------------|--------------------------------------------|
   | PMS plan owner                 | {{NAME}}     | Maintain and update the PMS plan            |
   | Data collection lead           | {{NAME}}     | Ensure all data collection is operational   |
   | Analysis lead                  | {{NAME}}     | Perform periodic evaluations and analysis   |
   | Corrective action lead         | {{NAME}}     | Manage corrective action implementation     |
   | Regulatory affairs contact     | {{NAME}}     | Interface with market surveillance authorities |
   | Risk management liaison        | {{NAME}}     | Feed PMS findings into Art. 9 risk management |

8. RETENTION
   - PMS plan and all revisions: AI system lifetime + 10 years
   - PMS evaluation reports: AI system lifetime + 10 years
   - Raw monitoring data: per Log Retention Policy, minimum {{PERIOD}}
   - Corrective action records: AI system lifetime + 10 years
```

---

## 6. Serious Incident Report Template

Use this template when an incident has been classified as a serious incident under Art. 62. Complete and submit to the relevant national market surveillance authority within the required timeline.

```
SERIOUS INCIDENT REPORT
pursuant to Article 62 of Regulation (EU) 2024/1689

REPORT METADATA
   Report type:          Initial / Follow-up / Final
   Report date:          {{YYYY-MM-DD}}
   Report reference:     SIR-{{YEAR}}-{{NUMBER}}
   Previous report ref:  {{PREVIOUS_REF}} (if follow-up/final)

1. PROVIDER INFORMATION
   Legal name:           {{COMPANY_LEGAL_NAME}}
   Registered address:   {{REGISTERED_ADDRESS}}
   Contact person:       {{NAME}}, {{TITLE}}
   Contact email:        {{EMAIL}}
   Contact phone:        {{PHONE}}
   EU authorized rep:    {{EU_REP_NAME}} (if applicable)
   EU rep address:       {{EU_REP_ADDRESS}} (if applicable)

2. AI SYSTEM IDENTIFICATION
   System name:          {{AI_SYSTEM_NAME}}
   Version:              {{VERSION}}
   EU database reg. ID:  {{REGISTRATION_ID}}
   Risk classification:  High-risk (Annex III, area {{AREA_NUMBER}})
   Intended purpose:     {{INTENDED_PURPOSE}}
   Date of market entry: {{YYYY-MM-DD}}
   Deployer(s) involved: {{DEPLOYER_NAMES}}

3. INCIDENT DESCRIPTION
   Date of incident:     {{YYYY-MM-DD}}
   Date provider became aware: {{YYYY-MM-DD}}
   Location:             {{CITY, MEMBER_STATE}}
   Description:
     {{DETAILED_DESCRIPTION_OF_WHAT_HAPPENED}}

   AI system involvement:
     {{HOW_THE_AI_SYSTEM_WAS_INVOLVED_IN_THE_INCIDENT}}

   Operating conditions at time of incident:
     {{SYSTEM_STATE_INPUTS_CONFIGURATION}}

4. SERIOUS INCIDENT CLASSIFICATION
   Category (check all that apply):
   - [ ] Death of a person
   - [ ] Serious damage to health of a person
   - [ ] Serious and irreversible disruption of critical infrastructure
   - [ ] Breach of obligations under Union law protecting fundamental rights
   - [ ] Serious damage to property
   - [ ] Serious damage to the environment

   Classification rationale:
     {{WHY_THIS_INCIDENT_MEETS_THE_SERIOUS_INCIDENT_THRESHOLD}}

   Widespread infringement (Art. 62 accelerated reporting):
   - [ ] Yes — incident affects or is likely to affect more than one member state
   - [ ] No

5. IMPACT ASSESSMENT
   Number of persons affected:       {{NUMBER}}
   Categories of persons affected:   {{CATEGORIES}}
   Severity of harm:                 {{DESCRIPTION}}
   Reversibility of harm:            Reversible / Partially reversible / Irreversible
   Geographic scope:                 {{MEMBER_STATES_AFFECTED}}
   Ongoing risk:                     Yes / No
   If ongoing, containment status:   {{DESCRIPTION}}

6. CORRECTIVE ACTIONS TAKEN
   Immediate actions:
     {{ACTIONS_TAKEN_TO_CONTAIN_INCIDENT_AND_MITIGATE_HARM}}

   System status:
   - [ ] AI system remains operational (with modifications)
   - [ ] AI system temporarily suspended
   - [ ] AI system permanently withdrawn
   - [ ] AI system recalled

   Deployer notification:
   - [ ] Deployer(s) notified on {{DATE}}
   - [ ] Instructions provided to deployer(s): {{SUMMARY}}

7. ROOT CAUSE ANALYSIS
   Status: Preliminary / In progress / Complete
   Findings:
     {{ROOT_CAUSE_DESCRIPTION_OR_PRELIMINARY_ASSESSMENT}}

   Contributing factors:
     {{LIST_CONTRIBUTING_FACTORS}}

8. CORRECTIVE ACTIONS PLANNED
   | Action                    | Timeline    | Responsible  | Status      |
   |---------------------------|-------------|-------------|-------------|
   | {{ACTION_1}}              | {{DATE}}    | {{NAME}}    | {{STATUS}}  |
   | {{ACTION_2}}              | {{DATE}}    | {{NAME}}    | {{STATUS}}  |

9. PREVIOUS RELATED INCIDENTS
   - [ ] No previous related incidents
   - [ ] Previous incidents: {{LIST_WITH_REFERENCES}}

10. AUTHORITY NOTIFICATION
    Submitted to:           {{AUTHORITY_NAME}}
    Member state:           {{MEMBER_STATE}}
    Submission method:      {{METHOD}}
    Submission date:        {{YYYY-MM-DD}}
    Acknowledgement ref:    {{REF}} (if received)
    Other authorities notified: {{LIST}} (if widespread infringement)

PREPARED BY
    Name:                   {{NAME}}
    Function:               {{TITLE}}
    Date:                   {{YYYY-MM-DD}}

APPROVED BY
    Name:                   {{NAME}}
    Function:               {{TITLE}}
    Date:                   {{YYYY-MM-DD}}
```

---

## 7. Verification Checklist

Use this checklist to confirm that all Art. 72 (post-market monitoring) and Art. 62 (serious incident reporting) requirements are met before and after placing a high-risk AI system on the EU market.

### Post-Market Monitoring System (Art. 72)

- [ ] PMS plan documented using Section 5 template (or equivalent)
- [ ] PMS plan is included in the Annex IV technical documentation package
- [ ] PMS plan is proportionate to the nature and risks of the AI system
- [ ] All monitoring objectives defined and mapped to Chapter III, Section 2 requirements
- [ ] Data collection methods specified for each data category
- [ ] Data collection is active and systematic (not merely reactive)
- [ ] OTel observability platform configured to capture AI-system-specific metrics
- [ ] Accuracy drift detection implemented with defined thresholds
- [ ] Bias/fairness monitoring implemented with defined thresholds
- [ ] Usage pattern analysis configured to detect deployment outside intended purpose
- [ ] Evaluation frequency defined and scheduled (continuous, periodic, and ad hoc)
- [ ] Corrective action triggers defined with clear escalation paths
- [ ] PMS findings feed back into Art. 9 risk management system (documented link)
- [ ] Responsible persons assigned for all PMS roles
- [ ] Deployer and end-user feedback collection mechanisms established
- [ ] PMS data available to market surveillance authorities on request
- [ ] Retention periods comply with minimum requirements (AI system lifetime + 10 years)
- [ ] PMS system operational BEFORE or AT the moment of market entry

### Serious Incident Reporting (Art. 62)

- [ ] Art. 3(49) serious incident categories documented and understood by incident response team
- [ ] Art. 62 classification step added to incident response procedure (for all SEV1/SEV2 AI system incidents)
- [ ] Mapping from framework SEV levels to Art. 62 classification documented (Section 3b of this guide)
- [ ] 15-day reporting timeline documented and achievable (process tested)
- [ ] 2-day accelerated reporting timeline documented and achievable for widespread infringements (process tested)
- [ ] 10-day reporting timeline documented for incidents involving death or serious health damage
- [ ] Serious incident report template available (Section 6 of this guide or equivalent)
- [ ] National market surveillance authority contact details identified for each member state of deployment
- [ ] Authority contact registry is maintained and reviewed at least annually
- [ ] Internal escalation path from incident response to regulatory affairs is documented and tested
- [ ] Regulatory affairs function (or designated person) is identified and empowered to submit reports
- [ ] Follow-up reporting procedure documented (triggered by new information or authority request)
- [ ] Serious incident reporting procedure covers near-misses ("realistically likely to lead to" harm)
- [ ] All serious incident reports are retained for AI system lifetime + 10 years

### Integration with Framework

- [ ] OTel observability data mapped to Art. 72 PMS requirements (Section 4a of this guide)
- [ ] Incident Response Policy extended with Art. 62 classification step (Section 4b of this guide)
- [ ] Retrospectives process linked to PMS feedback loop (Section 4c of this guide)
- [ ] Improvement signals from PMS findings use source tag `pms-art72`
- [ ] Risk management system receives PMS data inputs (documented data flow)
- [ ] Conformity assessment re-evaluation triggered when PMS identifies non-compliance
