<!-- placeholder-ok -->
# EU AI Act — CE Marking & EU Database Registration Guide

> **Implements:** CE marking (Art. 48) and EU database registration (Art. 49, 71)
> **Regulation:** EU AI Act (Regulation 2024/1689)
> **Severity:** Critical — mandatory prerequisites for EU market entry
> **Related issue:** [#130](https://github.com/wlfghdr/agentic-enterprise/issues/130)
> **Related compliance doc:** [EU AI Act Compliance Reference](../eu-ai-act.md)
> **Companion guide:** [Conformity Assessment](eu-ai-act-conformity-assessment.md) — must be completed first

---

## 1. Purpose

CE marking is the visible declaration that a high-risk AI system conforms with all applicable requirements of the EU AI Act. EU database registration makes the system discoverable by market surveillance authorities and the public. Both are mandatory before placing a high-risk AI system on the EU market or putting it into service.

The Agentic Enterprise framework provides the governance design and operational controls that satisfy the substantive requirements of the EU AI Act (risk management, data governance, human oversight, logging, transparency — see the [article-level mapping](../eu-ai-act.md)). This guide covers the final steps of the compliance journey: issuing the declaration of conformity, affixing the CE marking, registering in the EU AI database, and maintaining these obligations post-market.

Adopters use this guide to complete the CE marking and registration process — from issuing the declaration of conformity through post-market maintenance — bridging the framework's control implementation and the EU AI Act's market-entry requirements.

---

## 2. Prerequisites

All of the following must be completed before beginning the CE marking and registration process:

| Prerequisite | Reference | Status Check |
|-------------|-----------|-------------|
| Conformity assessment completed | [Conformity Assessment Guide](eu-ai-act-conformity-assessment.md), Art. 43 | Internal (Annex VI) or third-party (Annex VII) assessment passed with no unresolved findings |
| Technical documentation package complete | Annex IV, [Conformity Assessment Guide Section 3c](eu-ai-act-conformity-assessment.md#3c-technical-documentation-package-annex-iv) | All 8 sections of Annex IV documentation are present, current, and reviewed |
| Quality management system in place | Art. 17, [Conformity Assessment Guide Section 6](eu-ai-act-conformity-assessment.md#6-quality-management-system-evidence-art-17) | QMS is documented AND operational with evidence of execution |
| Risk management system operational | Art. 9, [Risk Management Policy](../../../org/4-quality/policies/risk-management.md) | Continuous risk management producing evidence (KRI dashboards, risk register updates) |
| Human oversight mechanisms designed | Art. 14, `AGENTS.md` Rule 2 ("Humans decide, agents recommend") | Oversight architecture documented for the specific AI system |
| Logging capability verified | Art. 12, [OTel contract](../../otel-contract.md), [Observability Policy](../../../org/4-quality/policies/observability.md) | Automatic event recording operational throughout system lifetime |
| All Chapter III Section 2 requirements verified | Arts. 9-15 | Each requirement has been assessed and documented in the conformity assessment report |

**Critical sequencing:** The declaration of conformity, CE marking, and EU database registration must all be completed BEFORE placing the AI system on the market or putting it into service. There is no grace period — market entry without these elements is a regulatory violation.

---

## 3. Declaration of Conformity (Art. 47)

The EU declaration of conformity is the formal legal instrument by which the provider takes sole responsibility for asserting that the AI system complies with the EU AI Act.

### 3a. Required Content

Art. 47 and Annex V specify the content requirements. The declaration must contain all of the following:

| Element | Description | Example |
|---------|-------------|---------|
| AI system identification | Name, type, and any additional unambiguous reference allowing identification (hardware/software version, batch/serial number if applicable) | "Agentic Hiring Assistant v2.1.0, build 2026-05-15-a3f2" |
| Provider identification | Name and address of the provider (and EU authorized representative, if applicable) | Legal entity name, registered office address, contact details |
| Sole responsibility statement | Explicit statement that the declaration is issued under the sole responsibility of the provider | Fixed text — see template below |
| Conformity statement | Statement that the AI system is in conformity with the EU AI Act and, where applicable, other relevant Union harmonization legislation | Reference specific chapters and articles |
| Harmonized standards / common specifications | References to relevant harmonized standards applied, or common specifications in relation to which conformity is declared | "ISO/IEC 42001:2023, ISO/IEC 23894:2023" |
| Notified body (if applicable) | Name and identification number of the notified body, description of the assessment performed, and reference to the certificate issued | Required only for Annex III point 1 systems (biometric identification) |
| Place and date | Location and date of issuance | City, country, and full date |
| Signatory | Name and function of the person who signs on behalf of the provider | Must be a person authorized to represent the provider |
| Signature | Handwritten or qualified electronic signature | For software-only systems, a qualified electronic signature is appropriate |

### 3b. Declaration Template

```
EU DECLARATION OF CONFORMITY
pursuant to Article 47 of Regulation (EU) 2024/1689

1. AI SYSTEM IDENTIFICATION
   Name:           {{AI_SYSTEM_NAME}}
   Type:           {{AI_SYSTEM_TYPE}}
   Version:        {{VERSION}}
   Unique ID:      {{UNIQUE_IDENTIFIER}}

2. PROVIDER
   Legal name:     {{COMPANY_LEGAL_NAME}}
   Address:        {{REGISTERED_ADDRESS}}
   Contact:        {{CONTACT_EMAIL}}

3. EU AUTHORIZED REPRESENTATIVE (if provider outside EU)
   Legal name:     {{EU_REP_NAME}}
   Address:        {{EU_REP_ADDRESS}}

4. RESPONSIBILITY STATEMENT
   This declaration of conformity is issued under the sole
   responsibility of the provider named in point 2.

5. CONFORMITY STATEMENT
   The AI system described in point 1 is in conformity with
   Regulation (EU) 2024/1689 of the European Parliament and
   of the Council (EU Artificial Intelligence Act).

   [Where applicable: The AI system is also in conformity with
   the following Union harmonization legislation:
   - {{LIST_OTHER_APPLICABLE_REGULATIONS}}]

6. STANDARDS AND SPECIFICATIONS APPLIED
   The following harmonized standards and/or common specifications
   were applied:
   - {{HARMONIZED_STANDARD_1}} (e.g., ISO/IEC 42001:2023)
   - {{HARMONIZED_STANDARD_2}} (e.g., ISO/IEC 23894:2023)
   - {{ADDITIONAL_STANDARDS_AS_APPLICABLE}}

7. CONFORMITY ASSESSMENT
   Type:           Internal (Annex VI) / Third-party (Annex VII)
   Notified body:  {{NAME_AND_NUMBER}} (if applicable)
   Certificate:    {{CERTIFICATE_REFERENCE}} (if applicable)

   [If no notified body was involved: "Not applicable —
   internal conformity assessment performed pursuant to
   Article 43(2) and Annex VI."]

8. ADDITIONAL INFORMATION
   Risk classification: High-risk (Art. 6, Annex III area {{AREA_NUMBER}})
   Intended purpose:    {{INTENDED_PURPOSE_SUMMARY}}

Signed at {{PLACE}} on {{DATE}}

{{SIGNATORY_NAME}}
{{SIGNATORY_FUNCTION}}
{{SIGNATURE}}
```

### 3c. Maintenance Obligations

The declaration of conformity is not a one-time document. It carries ongoing obligations:

- **10-year retention:** The declaration must be kept for 10 years after the AI system is placed on the market or put into service (Art. 47(2))
- **Available on request:** National competent authorities may request the declaration at any time; it must be provided without undue delay
- **Update on substantial modification:** When the AI system undergoes a substantial modification (Art. 3(23)), the conformity assessment must be repeated and a new declaration issued
- **Language:** Must be translated into the language(s) required by the member state(s) where the AI system is made available
- **Machine-readable copy:** Recommended practice — maintain a machine-readable version (e.g., JSON or XML) alongside the signed document for automated compliance verification

---

## 4. CE Marking (Art. 48)

The CE marking is the visible, physical (or digital) indicator that the AI system has undergone conformity assessment and complies with the EU AI Act.

### 4a. General Requirements

CE marking for AI systems follows the general principles established by Regulation (EC) No 765/2008, Article 30:

- **Affixed by the provider only** — no other party may affix the CE marking
- **Affixed BEFORE the AI system is placed on the market** — not after
- **Visible, legible, and indelible** — must be clearly readable and resistant to wear or removal
- **Minimum height: 5mm** — unless impracticable due to the nature of the AI system
- **Proportions must be maintained** — the CE marking has a defined geometric ratio that must be preserved when scaling
- **No misleading marks** — no other marks that could be confused with the CE marking or impair its visibility or legibility

### 4b. CE Marking for Physical Products with AI Components

For AI systems embedded in physical products (Annex I path):

- CE marking is affixed **visibly, legibly, and indelibly** to the product
- If affixing to the product is not possible, affix to the packaging or accompanying documentation
- Must follow the general principles of Regulation (EC) No 765/2008, Art. 30
- The CE marking for the AI Act may appear alongside other CE markings required by product-specific legislation (e.g., Machinery Regulation, MDR)

### 4c. CE Marking for Software-Only AI Systems

For standalone software AI systems — the typical case for systems built with the Agentic Enterprise framework — the CE marking must be applied digitally.

**Mandatory placement locations (at least one):**

| Location | Implementation | When Required |
|----------|---------------|---------------|
| Application UI | Visible CE mark on startup screen, about page, settings/system information panel, or equivalent | If the system has a user interface |
| API documentation | CE marking section in API reference documentation | If the system is accessed via API |
| System documentation | Dedicated section in technical/deployment documentation delivered to deployers | Always required |

**Recommended additional placements:**

- Machine-readable metadata in the software distribution package
- Digital certificate or manifest file shipped with the software
- Health/status endpoint response (for API-based systems)
- Release notes for each version

**Machine-readable CE marking metadata:**

Embed the following metadata in a standardized location within the software distribution. This enables automated compliance verification by deployers and market surveillance authorities.

```json
{
  "eu_ai_act_compliance": {
    "ce_marking": true,
    "regulation": "Regulation (EU) 2024/1689",
    "provider": {
      "name": "{{COMPANY_LEGAL_NAME}}",
      "address": "{{REGISTERED_ADDRESS}}",
      "eu_representative": null
    },
    "ai_system": {
      "name": "{{AI_SYSTEM_NAME}}",
      "version": "{{VERSION}}",
      "risk_classification": "high-risk",
      "annex_reference": "Annex III, point {{AREA_NUMBER}}"
    },
    "conformity_assessment": {
      "type": "internal",
      "annex": "VI",
      "date": "{{YYYY-MM-DD}}",
      "notified_body": null
    },
    "declaration_of_conformity_ref": "DoC-{{YEAR}}-{{NUMBER}}",
    "eu_database_registration_id": "{{REGISTRATION_ID}}",
    "standards_applied": [
      "ISO/IEC 42001:2023",
      "ISO/IEC 23894:2023"
    ],
    "marking_date": "{{YYYY-MM-DD}}"
  }
}
```

**Framework integration:**

For systems built and deployed using the Agentic Enterprise framework, the CE marking metadata should be:

1. **Stored as a governed file** (e.g., `ce-declaration.json` in the repository root or a dedicated compliance directory) subject to PR review and CODEOWNERS approval
2. **Included in the build/deployment pipeline** so it is embedded in every release artifact — reference the [Delivery Policy](../../../org/4-quality/policies/delivery.md) for CI/CD integration patterns
3. **Exposed via a system information endpoint** or health check response for runtime verification
4. **Referenced in the system's instructions for use** (Art. 13) and release contracts in `work/releases/`

**CONFIG.yaml integration:**

```yaml
# Add to CONFIG.yaml under a new eu_ai_act section
eu_ai_act:
  risk_classification: high-risk
  annex_iii_area: "{{AREA_NUMBER}}"
  ce_marking:
    enabled: true
    conformity_date: "{{YYYY-MM-DD}}"
    declaration_ref: "DoC-{{YEAR}}-{{NUMBER}}"
  eu_database:
    registration_id: "{{REGISTRATION_ID}}"
    registration_date: "{{YYYY-MM-DD}}"
  eu_representative:
    required: false  # set to true if provider is outside EU
    name: null
    address: null
```

### 4d. What CE Marking Legally Means

- The provider takes **sole legal responsibility** for the AI system's conformity
- CE marking is **not** an endorsement, quality mark, or certification of excellence — it is a declaration of regulatory compliance
- CE marking does **not** replace product-specific markings required by other EU legislation
- **Misuse carries penalties:** Affixing the CE marking without completing the conformity assessment, or affixing a misleading mark, constitutes an infringement subject to administrative fines:
  - **Affixing CE marking without conformity assessment:** Up to EUR 15 million or 3% of worldwide annual turnover (Art. 99(4)(b))
  - **Misleading CE marking:** Up to EUR 7.5 million or 1% of worldwide annual turnover (Art. 99(4)(c))
  - Member states may impose additional penalties under national law

---

## 5. EU AI Database Registration (Art. 49, 71)

The EU AI database is a publicly accessible database established and maintained by the European Commission (through the AI Office). Registration provides market surveillance authorities and the public with information about high-risk AI systems available in the EU.

### 5a. Who Must Register

| Actor | Registration Requirement | Legal Basis |
|-------|------------------------|-------------|
| **Providers of high-risk AI systems** | Must register each high-risk AI system BEFORE placing it on the market or putting it into service | Art. 49(1) |
| **Deployers that are public authorities** (or act on behalf of public authorities) | Must register their use of high-risk AI systems | Art. 49(3) |
| **Providers of AI systems with transparency obligations** (Art. 50) | Must register in a separate, non-public section of the database BEFORE placing on market | Art. 49(2) |

**Exception:** High-risk AI systems related to law enforcement, migration, and asylum (Annex III, points 1(a) regarding real-time remote biometric identification, 6, 7, and 8) are registered in a restricted-access section of the database, accessible only to market surveillance authorities (Art. 49(4)).

### 5b. Registration Data Requirements (Annex VIII)

The following data must be provided at registration. Prepare this information in advance to avoid delays at market entry.

**Provider information:**

| Data Field | Description | Source within Framework |
|-----------|-------------|----------------------|
| Provider identity | Legal name, address, contact details | Company registration, `CONFIG.yaml` |
| EU authorized representative | Name and contact (if provider outside EU) | Legal arrangements |
| Trade name(s) | Commercial name(s) of the AI system | Product naming |

**AI system information:**

| Data Field | Description | Source within Framework |
|-----------|-------------|----------------------|
| AI system name and version | Official name and version identifier | Release artifacts in `work/releases/` |
| Unique identifier | System-level unique reference | Build/deployment pipeline |
| AI system status | On the market / withdrawn / recalled | Managed post-registration |
| Member states | EU member states where the system is or will be available | Commercial deployment plan |
| Annex III classification | Which area(s) of Annex III apply | Risk classification from [Conformity Assessment Guide Section 2](eu-ai-act-conformity-assessment.md#2-risk-classification-decision-tree) |
| Intended purpose | Clear description of what the AI system does and for whom | Technical documentation (Annex IV, Section 1) |
| Categories of affected persons | Natural persons and groups likely to be affected | Risk assessment, intended purpose documentation |
| Special category data | Whether the system processes Art. 9 GDPR data | [Privacy Policy](../../../org/4-quality/policies/privacy.md), data classification records |
| Plain language description | Accessible description of the AI system | Instructions for use |

**Conformity information:**

| Data Field | Description | Source within Framework |
|-----------|-------------|----------------------|
| Conformity assessment type | Internal (Annex VI) or third-party (Annex VII) | Conformity assessment report |
| Harmonized standards applied | List of standards used | Declaration of conformity |
| Notified body | Name and number (if applicable) | Third-party assessment records |
| URL for instructions for use | Publicly accessible link to deployer instructions | System documentation |
| URL for declaration of conformity | Publicly accessible or authority-accessible link | Declaration storage |

### 5c. Registration Process

The EU AI database is being established by the AI Office (Art. 71). The expected process:

1. **Access the database portal** — the AI Office will publish the URL and access procedures before the August 2026 deadline for high-risk obligations
2. **Create provider account** — register the legal entity, verify identity through electronic identification means, appoint database administrator
3. **Submit system registration** — enter all Annex VIII data for each high-risk AI system
4. **Receive confirmation** — obtain a unique registration number for each system
5. **Include registration number** in:
   - The AI system's documentation and instructions for use
   - The CE marking metadata (recommended)
   - Internal compliance records
   - The declaration of conformity (as additional information)
6. **Verify public listing** — confirm the registration is visible in the public section of the database (except for restricted-access systems under Art. 49(4))

**Important timing:** Registration must happen BEFORE market entry. If the database is not yet fully operational when you are ready to deploy, monitor the AI Office communications for interim registration procedures. The AI Office website and official EU channels will publish guidance as the August 2026 deadline approaches.

### 5d. Update Obligations

Registration is not a one-time event. Providers must keep registration data current:

| Trigger | Action Required | Timeline |
|---------|----------------|----------|
| Any registered information changes | Update the registration entry | Without undue delay |
| Substantial modification to the AI system | Re-assess conformity, update registration with new version/modification details | Before placing modified system on market |
| System withdrawal from the market | Update status to "withdrawn" | Without undue delay |
| System recall | Update status to "recalled" and provide recall details | Immediately upon recall decision |
| Declaration of conformity updated | Update corresponding registration fields | Without undue delay |
| Provider ceases to exist | EU authorized representative (or last responsible entity) ensures registration is updated | Within timeline set by national law |

---

## 6. Timeline Relative to Market Entry

The following timeline shows the sequencing of CE marking and registration activities relative to the conformity assessment and market entry. All activities must be completed before the system is placed on the market.

```
Month   Action                                          Article
-----   ------                                          -------
-12     Begin conformity assessment                     Art. 43
 -9     Engage notified body (if biometric ID system)   Art. 43(1)
 -6     Complete technical documentation package         Art. 11
 -4     Complete quality management system evidence      Art. 17
 -3     Complete conformity assessment                   Art. 43
 -2     Issue declaration of conformity                  Art. 47
 -1     Affix CE marking (digital)                      Art. 48
 -1     Submit EU database registration                 Art. 49
  0     == MARKET ENTRY ==
 +0     Post-market monitoring system operational        Art. 72
 +0     Serious incident reporting procedure active      Art. 62
+120    Ongoing: update registration as needed           Art. 49
```

**Critical path dependencies:**

1. Conformity assessment must complete before the declaration of conformity can be issued
2. The declaration of conformity must be issued before the CE marking can be affixed
3. Both CE marking and EU database registration must be completed before market entry
4. Post-market monitoring must be operational from the moment of market entry

**Key deadline:** High-risk AI system obligations apply from **August 2, 2026**.

---

## 7. Post-Market Obligations

Placing the CE marking and registering in the EU database marks the beginning, not the end, of compliance obligations. Providers must maintain the following on an ongoing basis.

### 7a. Document Retention (Art. 18)

| Document | Retention Period | Storage Requirements |
|----------|-----------------|---------------------|
| Declaration of conformity | 10 years after AI system placed on market | Accessible on request by national competent authorities |
| Technical documentation (Annex IV) | 10 years after AI system placed on market | Complete, current, and available for inspection |
| QMS documentation | 10 years after AI system placed on market | Demonstrating ongoing operational effectiveness |
| Conformity assessment records | 10 years after AI system placed on market | Including any notified body certificates and correspondence |
| EU database registration records | 10 years after AI system placed on market | Including all updates and version history |

**Framework implementation:** Use the existing [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) as the baseline, but extend retention periods to 10 years for all conformity-related documentation. Store conformity documents in a dedicated, access-controlled location within the repository or document management system. Git history provides immutable version tracking, but ensure that 10-year availability is guaranteed by your hosting and backup infrastructure.

### 7b. Post-Market Monitoring (Art. 72)

Providers must establish and document a post-market monitoring system proportionate to the nature and risks of the AI system:

- **Active collection** of data on AI system performance throughout its lifetime
- **Evaluation** of the continuous compliance with requirements in Chapter III, Section 2
- **Integration with risk management** — post-market data feeds back into the Art. 9 risk management system
- **Plan documentation** — the post-market monitoring plan must be part of the technical documentation (Annex IV)

The framework's Operate loop ([`process/4-operate/`](../../../process/4-operate/)) and [Observability Policy](../../../org/4-quality/policies/observability.md) provide the monitoring infrastructure. Adopters must configure monitoring to capture AI-specific performance indicators:

- **Accuracy drift** — tracking model performance degradation over time
- **Bias drift** — monitoring for emergent discriminatory patterns in outputs
- **Usage pattern changes** — detecting deployment in unintended contexts
- **Incident patterns** — correlating operational incidents with AI system behavior
- **User feedback** — collecting and analyzing deployer and end-user reports

### 7c. Serious Incident Reporting (Art. 62)

A "serious incident" means an incident or malfunctioning that directly or indirectly leads to, or is realistically likely to lead to:

- Death or serious damage to health of a person
- Serious and irreversible disruption of the management or operation of critical infrastructure
- Breach of obligations under Union law intended to protect fundamental rights
- Serious damage to property or the environment

| Incident Type | Reporting Timeline | Report To |
|--------------|-------------------|-----------|
| Serious incident (death, serious harm) | Within 15 days of becoming aware | Market surveillance authority of the member state where incident occurred |
| Widespread infringement or breach of fundamental rights | Within 2 days of becoming aware | Same as above |
| Follow-up report | As requested by the authority, or when new information becomes available | Same as above |

The framework's [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) provides the incident management structure. Adopters must add an EU AI Act incident classification step to the response procedure, with escalation paths to the provider's regulatory affairs function for incidents that meet the Art. 62 threshold.

### 7d. Cooperation with Authorities (Art. 21)

Providers must cooperate with national competent authorities on request, including:

- Providing access to technical documentation
- Providing access to training, validation, and testing datasets (where necessary and technically feasible)
- Providing access to the AI system's source code (where necessary to assess compliance)
- Granting access to automatically generated logs (Art. 12)
- Taking corrective actions when required by the authority

---

## 8. If the Provider Is Outside the EU

Providers not established in the EU but placing AI systems on the EU market must appoint an **EU authorized representative** (Art. 22).

### Authorized Representative Requirements

| Requirement | Detail |
|-------------|--------|
| Establishment | Must be established in one of the EU member states where the system is available |
| Written mandate | Must have a written mandate from the provider specifying the tasks and scope |
| Authority to act | Must be empowered to: keep documentation available, provide information to national authorities, cooperate with competent authorities |
| Registration | Representative's name and contact details appear in the EU database registration alongside the provider's |
| Liability | If no authorized representative is appointed, the importer (Art. 23) assumes certain provider obligations |

### Tasks of the Authorized Representative

1. Verify that the declaration of conformity and technical documentation have been drawn up
2. Keep a copy of the declaration of conformity and technical documentation available for 10 years
3. Provide national competent authorities with all information and documentation necessary to demonstrate conformity
4. Cooperate with competent authorities on any corrective or preventive action
5. Terminate the mandate if the provider acts contrary to its obligations under the EU AI Act

### Provider Obligations Toward the Representative

- Provide the representative with all necessary documentation and resources
- Keep the representative informed of changes to the AI system, its documentation, or its market status
- Ensure the representative can fulfill their tasks effectively
- The provider remains fully responsible — appointing a representative does not transfer legal liability

---

## 9. Framework Artifacts Supporting CE Marking and Registration

Existing Agentic Enterprise framework artifacts that provide evidence for CE marking and registration:

| EU AI Act Requirement | Framework Artifact | Path |
|----------------------|-------------------|------|
| Risk management (Art. 9) | Risk Management Policy | [`org/4-quality/policies/risk-management.md`](../../../org/4-quality/policies/risk-management.md) |
| Data governance (Art. 10) | Data Classification Policy, Privacy Policy | [`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md), [`org/4-quality/policies/privacy.md`](../../../org/4-quality/policies/privacy.md) |
| Technical documentation (Art. 11) | Technical design templates, mission briefs | `work/missions/*/technical-design.md`, agent type definitions in `org/agents/` |
| Logging (Art. 12) | OTel Contract, Observability Policy, Log Retention Policy | [`docs/otel-contract.md`](../../otel-contract.md), [`org/4-quality/policies/observability.md`](../../../org/4-quality/policies/observability.md), [`org/4-quality/policies/log-retention.md`](../../../org/4-quality/policies/log-retention.md) |
| Transparency (Art. 13) | Agent instruction hierarchy, org/README.md | [`org/README.md`](../../../org/README.md), [`AGENTS.md`](../../../AGENTS.md) |
| Human oversight (Art. 14) | AGENTS.md Rule 2, PR-based governance, CODEOWNERS | [`AGENTS.md`](../../../AGENTS.md), [`CODEOWNERS`](../../../CODEOWNERS) |
| Accuracy/robustness (Art. 15) | Quality policies, Agent Security Policy, Agent Eval Policy | [`org/4-quality/policies/security.md`](../../../org/4-quality/policies/security.md), [`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md), [`org/4-quality/policies/agent-eval.md`](../../../org/4-quality/policies/agent-eval.md) |
| QMS (Art. 17) | 19 quality policies, 4-loop process model | [`org/4-quality/policies/`](../../../org/4-quality/policies/), [`process/`](../../../process/) |
| Change management | PR-based governance, Delivery Policy | [`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md) |
| Incident response (Art. 62) | Incident Response Policy, retrospectives | [`org/4-quality/policies/incident-response.md`](../../../org/4-quality/policies/incident-response.md) |
| AI governance | AI Governance Policy | [`org/4-quality/policies/ai-governance.md`](../../../org/4-quality/policies/ai-governance.md) |

---

## 10. Verification Checklist

Use this checklist to confirm that CE marking and EU database registration are complete and that post-market obligations are established.

### Declaration of Conformity
- [ ] Declaration drafted with all required content per Art. 47 and Annex V
- [ ] AI system name, version, and unique identifier are accurate
- [ ] Provider identity and address match business registration
- [ ] EU authorized representative named (if provider outside EU)
- [ ] Sole responsibility statement included
- [ ] Conformity statement references EU AI Act and any other applicable legislation
- [ ] Harmonized standards and common specifications listed
- [ ] Notified body details included (if third-party assessment performed)
- [ ] Place and date of issuance recorded
- [ ] Signed by authorized person with name and function stated
- [ ] Translated into required member state language(s)
- [ ] Machine-readable version prepared (recommended)
- [ ] 10-year retention plan in place

### CE Marking
- [ ] CE marking prepared in appropriate format (digital for software-only systems)
- [ ] CE marking placed in at least one mandatory location (UI, API docs, or system docs)
- [ ] CE marking is visible, legible, and indelible (or persistent in digital form)
- [ ] Minimum height of 5mm maintained (or digital equivalent)
- [ ] Machine-readable CE marking metadata embedded in software distribution
- [ ] CE marking references the declaration of conformity
- [ ] No misleading marks or symbols that could be confused with CE marking
- [ ] CE marking affixed BEFORE market entry (verified by dated evidence)

### EU Database Registration
- [ ] All Annex VIII data fields prepared and verified
- [ ] Provider account created in EU AI database (when available)
- [ ] Registration submitted for each high-risk AI system
- [ ] Registration confirmation and unique identifier received
- [ ] Registration number included in system documentation
- [ ] Public listing verified in the database (except restricted-access systems)
- [ ] Registration completed BEFORE market entry (verified by dated evidence)
- [ ] Update procedure documented for ongoing registration maintenance

### Post-Market Obligations
- [ ] Post-market monitoring system operational (Art. 72)
- [ ] Post-market monitoring plan included in technical documentation
- [ ] Serious incident reporting procedure established per Art. 62 timelines
- [ ] 15-day and 2-day reporting paths tested and documented
- [ ] National competent authority contact details identified for each member state of deployment
- [ ] Cooperation procedure documented for authority requests (Art. 21)
- [ ] Document retention system configured for 10-year compliance
- [ ] Registration update procedure documented and assigned to responsible team

### If Provider Outside EU
- [ ] EU authorized representative appointed (Art. 22)
- [ ] Written mandate formalized specifying tasks and scope
- [ ] Representative details included in all registrations and declarations
- [ ] Representative has access to all required documentation
