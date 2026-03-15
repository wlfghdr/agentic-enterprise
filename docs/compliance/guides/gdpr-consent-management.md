<!-- placeholder-ok -->
# GDPR — Consent Management UX and DPO Appointment Guide

> **Implements:** Consent management UX (Art. 6–7) and DPO appointment (Art. 37–39)
> **Regulation:** General Data Protection Regulation (EU) 2016/679
> **Severity:** High — consent management is mandatory when consent is the lawful basis; DPO appointment is mandatory for qualifying organizations
> **Related issue:** [#132](https://github.com/wlfghdr/agentic-enterprise/issues/132)
> **Related compliance doc:** [GDPR Compliance Reference](../gdpr.md)

---

## 1. Purpose

The Agentic Enterprise framework provides comprehensive privacy governance — lawful basis documentation, DSAR handling, breach notification procedures, DPIA processes, and international transfer controls (see the [article-level mapping](../gdpr.md)). This guide extends that foundation with two areas:

1. **Consent management UX guidance.** This guide provides patterns for implementing runtime consent collection, storage, withdrawal, and age verification in a way that satisfies GDPR Arts. 6–8. Adopters use this guide when consent is the chosen lawful basis.

2. **DPO appointment guidance.** This guide provides guidance on when DPO appointment is mandatory, what qualifications are needed, how to ensure DPO independence, and how to integrate the DPO role into the framework's governance structure.

This guide provides actionable implementation patterns for consent management and a complete DPO appointment and integration guide.

---

## 2. Consent Management Requirements (GDPR Arts. 6–7)

### 2a. Lawful Bases for Processing (Art. 6)

GDPR requires at least one lawful basis for every processing activity. Consent is one of six options — and not always the most appropriate one.

| Lawful Basis | Article | When Appropriate | Key Consideration |
|-------------|---------|-----------------|-------------------|
| **Consent** | Art. 6(1)(a) | Data subject freely chooses to allow processing for specified purposes | Must meet Art. 7 conditions; can be withdrawn at any time |
| **Contract** | Art. 6(1)(b) | Processing necessary for contract performance or pre-contractual steps | Cannot be stretched to cover unrelated processing |
| **Legal obligation** | Art. 6(1)(c) | Processing required by EU or member state law | Must identify the specific legal provision |
| **Vital interests** | Art. 6(1)(d) | Life-or-death situations | Narrow scope — not for routine processing |
| **Public interest** | Art. 6(1)(e) | Task in the public interest or official authority | Requires legal basis in EU or member state law |
| **Legitimate interests** | Art. 6(1)(f) | Controller or third-party interests, balanced against data subject rights | Requires documented balancing test (LIA); not available for public authorities |

**Decision guidance:** Before implementing consent flows, verify that consent is genuinely the correct lawful basis. If the processing is necessary to fulfill a contract, use Art. 6(1)(b). If the data subject has no genuine choice (e.g., employee data processing required by the employer), consent is unlikely to be freely given and another basis should be used. Document the lawful basis decision in the Records of Processing Activities (RoPA) as required by the [Privacy Policy](../../../org/4-quality/policies/privacy.md).

### 2b. Consent Requirements (Art. 7)

When consent is the chosen lawful basis, it must satisfy all four conditions simultaneously:

| Condition | GDPR Source | Requirement | Implementation Implication |
|-----------|-------------|-------------|---------------------------|
| **Freely given** | Art. 4(11), Recital 42–43 | No imbalance of power; service not conditional on consent to unnecessary processing; no detriment for refusal | Unbundle consent from service access; no "consent walls" for unrelated processing |
| **Specific** | Art. 4(11), Recital 32 | Given for one or more specific purposes; clearly distinguishable from other matters | Separate consent per purpose; no blanket "I agree to everything" |
| **Informed** | Art. 4(11), Recital 42 | Data subject knows at minimum: controller identity, purposes, data types, right to withdraw | Plain language; accessible before consent is given |
| **Unambiguous** | Art. 4(11), Recital 32 | Clear affirmative act; silence, pre-ticked boxes, or inactivity do not constitute consent | Opt-in only; no default-on toggles |

**Special category data (Art. 9):** Processing of health, biometric, political, religious, or other special category data requires **explicit** consent — a higher bar than standard consent. Explicit consent should use a distinct, prominent mechanism (e.g., typed confirmation, separate signature) rather than a simple checkbox.

### 2c. Consent Withdrawal (Art. 7(3))

> "The data subject shall have the right to withdraw his or her consent at any time. [...] It shall be as easy to withdraw as to give consent."

| Requirement | Detail |
|-------------|--------|
| Right to withdraw | Must exist for every consent-based processing activity |
| Ease of withdrawal | Withdrawal mechanism must be no more burdensome than the original consent mechanism |
| Prior information | Data subjects must be informed of the right to withdraw BEFORE giving consent |
| Effect of withdrawal | Does not affect lawfulness of processing based on consent before withdrawal |
| Cessation of processing | Controller must stop the specific processing activity upon withdrawal without undue delay |

### 2d. Consent Records

GDPR places the burden of proof on the controller (Art. 7(1)): "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented."

| Record Element | Purpose | Retention |
|---------------|---------|-----------|
| **Who** consented | Identity of the data subject (or pseudonymized reference) | Duration of processing + legal retention period |
| **When** consent was given | Timestamp of the affirmative act | Same as above |
| **What** was consented to | Specific purposes, data types, and scope at the time of consent | Same as above |
| **How** consent was given | The mechanism used (UI version, form version, verbatim consent text presented) | Same as above |
| **Withdrawal record** | If and when consent was withdrawn | Same as above |

**Framework integration:** Store consent records as structured data (e.g., JSON events) in the observability pipeline. Use `governance.decision` span events (as defined in [`docs/otel-contract.md`](../../otel-contract.md)) to capture consent grant and withdrawal events, enabling auditability through the existing telemetry infrastructure.

### 2e. Age Verification (Art. 8)

When offering information society services directly to a child, consent must be given or authorized by the holder of parental responsibility if the child is below the age threshold.

| Aspect | Requirement |
|--------|-------------|
| **Default age threshold** | 16 years (member states may lower to 13 — check applicable national law) |
| **Parental consent** | Must make reasonable efforts to verify parental consent, taking into account available technology |
| **Age gate** | Implement an age verification mechanism before collecting consent from potential minors |
| **National variation** | DE: 16, FR: 15, UK: 13, IE: 16, NL: 16, ES: 14, BE: 13 — check all jurisdictions where the service operates |

---

## 3. Consent Management UX Patterns

### 3a. Consent Collection Design

The following patterns satisfy GDPR requirements while maintaining usable design:

**Granular per-purpose consent:**

```
┌─────────────────────────────────────────────────────┐
│  We'd like your permission for the following:       │
│                                                     │
│  □  Analytics — understand how you use the service  │
│     Data: page views, feature usage, session length │
│                                                     │
│  □  Personalization — tailor content to your needs  │
│     Data: preferences, interaction history          │
│                                                     │
│  □  Marketing emails — product updates and offers   │
│     Data: email address, name                       │
│                                                     │
│  ℹ️  You can change these choices at any time in    │
│     your privacy settings. Refusing does not        │
│     affect your access to the core service.         │
│                                                     │
│  [Save choices]           [Refuse all optional]     │
│                                                     │
│  Privacy Policy · Contact DPO                       │
└─────────────────────────────────────────────────────┘
```

**Design principles:**

| Principle | Requirement | Anti-Pattern to Avoid |
|-----------|-------------|----------------------|
| All checkboxes unchecked by default | Art. 4(11), Recital 32 | Pre-ticked boxes |
| Equal visual weight for accept/refuse | Freely given (Recital 42) | Large "Accept" button vs. tiny "Refuse" link |
| No consent wall for core service | Freely given (Recital 43) | "Accept all or leave" |
| Plain language, no legal jargon | Informed (Art. 12) | Dense legalese requiring legal training |
| Purpose-specific toggles | Specific (Art. 4(11)) | Single "I agree to everything" checkbox |
| Data types listed per purpose | Informed (Recital 42) | Vague "we process your data" |
| No dark patterns | Freely given + EDPB Guidelines 05/2020 | Confusing double negatives, guilt-tripping, visual manipulation |

### 3b. Consent Dashboard for Data Subjects

Provide a self-service dashboard where data subjects can view and manage their consent choices at any time:

**Required dashboard elements:**

| Element | Purpose | GDPR Basis |
|---------|---------|------------|
| Current consent status | Show which purposes are active (consented) and which are inactive | Art. 7(3) — informed withdrawal |
| Consent history | When each consent was given or withdrawn | Art. 7(1) — demonstrability |
| Per-purpose toggle | Enable withdrawal of specific consents without affecting others | Art. 7(3) — granular withdrawal |
| Withdraw all | One-click withdrawal of all optional consents | Art. 7(3) — ease of withdrawal |
| Contact DPO | Link to DPO or privacy team contact | Art. 38(4) |
| Privacy policy link | Current version of the privacy policy | Art. 13–14 |

**Accessibility:** The dashboard must be accessible from the same interface where consent was originally given. If consent was collected via web UI, the dashboard must be reachable via web UI — not hidden behind a support ticket or email request.

### 3c. Withdrawal Mechanism

| Requirement | Implementation |
|-------------|---------------|
| Same channel | If consent was given via web UI, withdrawal must be possible via web UI |
| No more steps | Withdrawal must require no more clicks/steps than the original consent |
| No confirmation barriers | Do not add "Are you sure?" friction that was not present when giving consent |
| Immediate effect | Processing based on the withdrawn consent must stop without undue delay |
| Confirmation | Provide confirmation that withdrawal was processed |
| No penalty | No degradation of core service functionality as a result of withdrawal |

### 3d. Cookie Consent (ePrivacy Alignment)

Cookie consent overlaps with GDPR consent requirements but is technically governed by the ePrivacy Directive (2002/58/EC) and national implementations. For web-facing deployments:

| Cookie Category | Consent Required | Rationale |
|----------------|-----------------|-----------|
| **Strictly necessary** | No | Required for the service to function (Art. 5(3) ePrivacy exemption) |
| **Analytics** | Yes | Not strictly necessary; tracks user behavior |
| **Functionality** | Depends | Consent required if not strictly necessary for requested service |
| **Marketing/advertising** | Yes | Always requires consent |
| **Third-party tracking** | Yes | Always requires consent; additional transparency about third parties |

**Implementation requirements:**

- No non-essential cookies set before consent is obtained
- Cookie banner must not block content access (no "cookie wall" for consent-exempt content)
- Cookie preferences must be as easy to change as they were to set initially
- Cookie consent records must be stored and auditable
- Re-consent must be requested if processing purposes change

---

## 4. Data Protection Officer (Art. 37–39)

### 4a. When DPO Appointment Is Mandatory

DPO appointment is mandatory in three cases (Art. 37(1)):

| Trigger | Article | Description | Examples |
|---------|---------|-------------|---------|
| **Public authority or body** | Art. 37(1)(a) | Processing carried out by a public authority or body (except courts acting in judicial capacity) | Government agencies, public universities, public healthcare providers |
| **Large-scale systematic monitoring** | Art. 37(1)(b) | Core activities require regular and systematic monitoring of data subjects on a large scale | Behavioral advertising networks, location tracking services, loyalty programs with profiling, insurance risk scoring |
| **Large-scale special category data** | Art. 37(1)(c) | Core activities consist of large-scale processing of special categories of data (Art. 9) or personal data relating to criminal convictions (Art. 10) | Hospitals, genetic testing services, large HR operations processing health data, political organizations |

**"Large scale" factors** (EDPB/WP29 Guidelines on DPOs, WP 243):
- Number of data subjects (absolute or as a proportion of the population)
- Volume or range of data items being processed
- Duration or permanence of the processing
- Geographical extent of the processing

**"Core activities"** means the key operations necessary to achieve the controller's or processor's objectives — not ancillary functions like payroll or IT support (Recital 97).

**Even when not mandatory**, GDPR encourages voluntary DPO appointment as a governance best practice (Art. 37(4)). National law may also impose additional DPO requirements beyond Art. 37(1).

### 4b. DPO Qualifications and Independence

| Requirement | Article | Detail |
|-------------|---------|--------|
| **Professional qualities** | Art. 37(5) | Expert knowledge of data protection law and practices; level of expertise proportionate to the complexity and sensitivity of processing |
| **Internal or external** | Art. 37(6) | May be a staff member or engaged via a service contract; group of undertakings may appoint a single DPO if each establishment can access the DPO |
| **No conflict of interest** | Art. 38(6) | May perform other tasks and duties, but none that result in a conflict of interest; DPO cannot be a person who determines purposes and means of processing (e.g., not the CEO, CTO, CISO, or head of HR/marketing) |
| **No instructions** | Art. 38(3) | Controller/processor must not instruct the DPO regarding the exercise of their tasks; DPO acts independently |
| **No dismissal or penalty** | Art. 38(3) | DPO must not be dismissed or penalized for performing their tasks; reports directly to the highest management level |
| **Resources** | Art. 38(2) | Controller/processor must provide resources necessary to carry out tasks, maintain expert knowledge, and access personal data and processing operations |

**Roles incompatible with DPO** (EDPB guidance): CEO, COO, CFO, CTO, CISO, head of HR, head of marketing, head of IT — any role that determines purposes and means of data processing.

### 4c. DPO Tasks and Responsibilities

The DPO has the following minimum tasks under Art. 39:

| Task | Article | Description |
|------|---------|-------------|
| **Inform and advise** | Art. 39(1)(a) | Inform and advise the controller/processor and their employees of their GDPR obligations |
| **Monitor compliance** | Art. 39(1)(b) | Monitor compliance with GDPR, other data protection provisions, and internal policies — including assignment of responsibilities, awareness-raising, training, and audits |
| **DPIA advice** | Art. 39(1)(c) | Provide advice on Data Protection Impact Assessments and monitor their performance (Art. 35) |
| **Cooperate with SA** | Art. 39(1)(d) | Cooperate with the supervisory authority |
| **Contact point for SA** | Art. 39(1)(e) | Act as the contact point for the supervisory authority on processing issues, including prior consultation (Art. 36) |
| **Risk-based prioritization** | Art. 39(2) | Have due regard to the risk associated with processing operations, taking into account nature, scope, context, and purposes |

### 4d. DPO Contact and Accessibility

| Requirement | Article | Implementation |
|-------------|---------|---------------|
| **Published contact details** | Art. 37(7) | Controller/processor must publish the DPO's contact details (not necessarily name — contact point suffices) |
| **Communicated to SA** | Art. 37(7) | DPO contact details must be communicated to the competent supervisory authority |
| **Accessible to data subjects** | Art. 38(4) | Data subjects may contact the DPO with regard to all issues related to processing of their data and exercise of their rights |
| **Confidentiality** | Art. 38(5) | DPO is bound by secrecy or confidentiality concerning the performance of their tasks |

**Framework integration:** Add DPO contact details to `CONFIG.yaml` under a `gdpr` section and reference them in the consent collection UI (Section 3a), the consent dashboard (Section 3b), and the organization's public privacy policy.

```yaml
# Add to CONFIG.yaml
gdpr:
  dpo:
    appointed: true  # or false — document reasoning if not required
    name: "{{DPO_NAME}}"
    email: "{{DPO_EMAIL}}"
    phone: "{{DPO_PHONE}}"  # optional
    external: false  # true if engaged via service contract
    supervisory_authority_notified: false  # set true after Art. 37(7) communication
    supervisory_authority: "{{SA_NAME}}"  # e.g., "BfDI", "CNIL", "ICO"
  consent_management:
    enabled: false  # set true when consent UX is deployed
    lawful_bases_documented: false  # set true when RoPA is populated
```

---

## 5. Integration with Framework

### 5a. Privacy Policy Mapping

The existing [Privacy Policy](../../../org/4-quality/policies/privacy.md) provides the governance foundation. This guide extends it with operational patterns:

| Privacy Policy Section | This Guide Extension | Action Required |
|-----------------------|---------------------|-----------------|
| §1 — Lawful basis documentation | Section 2a — lawful basis selection guidance | Document chosen lawful basis per processing activity in RoPA |
| §1 — Processing records | Section 2d — consent records | Implement consent event logging via OTel pipeline |
| §3 — DSAR runbook | Section 3b — consent dashboard | Integrate consent status into DSAR responses |
| §4 — Breach notification | N/A — already covered | Ensure consent records are included in breach scope assessment |
| §5 — DPIA | Section 4c — DPO DPIA advice | Involve DPO in DPIA reviews |

### 5b. Data Classification Policy Mapping

The [Data Classification Policy](../../../org/4-quality/policies/data-classification.md) defines data handling tiers:

| Classification Level | Consent Relevance |
|---------------------|-------------------|
| **PUBLIC** | No consent needed for processing already-public data (but consent may still be the lawful basis for collection) |
| **INTERNAL** | Consent required if personal data is processed under Art. 6(1)(a); other bases may apply |
| **CONFIDENTIAL** | Likely personal data — verify lawful basis; if consent, implement full consent flow |
| **RESTRICTED** | Likely special category (Art. 9) — requires explicit consent if consent is the lawful basis; heightened UX requirements |

### 5c. Observability Integration

| Consent Event | OTel Span/Event | Attributes |
|--------------|-----------------|------------|
| Consent granted | `governance.decision` event | `governance.decision: consent_granted`, `consent.purpose: <purpose>`, `consent.mechanism: <ui_version>` |
| Consent withdrawn | `governance.decision` event | `governance.decision: consent_withdrawn`, `consent.purpose: <purpose>` |
| Consent record queried | `tool.execute` span | `tool.name: consent_lookup`, `data_subject.ref: <pseudonymized_id>` |
| Age verification | `governance.decision` event | `governance.decision: age_verified`, `age_verification.method: <method>` |

---

## 6. Verification Checklist

### Consent Management
- [ ] Lawful basis documented for every processing activity in the Records of Processing Activities
- [ ] Where consent is the lawful basis, consent collection UI implements all four conditions (freely given, specific, informed, unambiguous)
- [ ] All consent checkboxes/toggles are unchecked/off by default
- [ ] Accept and refuse options have equal visual prominence — no dark patterns
- [ ] Core service access is not conditional on consent to non-essential processing
- [ ] Plain language descriptions provided for each consent purpose, including data types
- [ ] Consent withdrawal mechanism is accessible and no more burdensome than consent collection
- [ ] Data subjects are informed of the right to withdraw BEFORE giving consent
- [ ] Consent records capture who, when, what, and how for every consent event
- [ ] Consent records are stored in the observability pipeline with appropriate retention
- [ ] Consent dashboard is available for data subjects to view and manage their choices
- [ ] Cookie consent implemented for web-facing deployments (no non-essential cookies before consent)
- [ ] Cookie preferences are as easy to change as they were to set
- [ ] Age verification mechanism implemented if the service may be used by children
- [ ] National age threshold variations are accounted for across all deployment jurisdictions
- [ ] Special category data processing uses explicit consent mechanism (higher bar than standard consent)

### DPO Appointment
- [ ] Assessment completed: does Art. 37(1)(a), (b), or (c) apply to this organization?
- [ ] If DPO required: appointed individual or external service with documented qualifications
- [ ] DPO has no conflict of interest (does not determine purposes/means of processing)
- [ ] DPO independence guaranteed — no instructions on task exercise, no dismissal for performing duties
- [ ] DPO reports directly to highest management level
- [ ] Adequate resources provided for DPO function (budget, tools, access, training)
- [ ] DPO contact details published (privacy policy, consent UI, website)
- [ ] DPO contact details communicated to the competent supervisory authority (Art. 37(7))
- [ ] DPO accessible to data subjects for all processing-related inquiries (Art. 38(4))
- [ ] DPO integrated into DPIA process as advisor (Art. 39(1)(c))
- [ ] DPO contact information added to `CONFIG.yaml` under `gdpr.dpo`

### Framework Integration
- [ ] Privacy Policy cross-referenced with consent management patterns in this guide
- [ ] Data Classification Policy levels mapped to consent requirements
- [ ] Consent events emitted as `governance.decision` OTel events
- [ ] Consent records included in DSAR response scope
- [ ] DPO role documented in organizational governance structure
