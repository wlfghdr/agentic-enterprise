# EU AI Act — Conformity Assessment Preparation Guide

> **Implements:** Conformity assessment preparation for high-risk AI (Art. 43)
> **Regulation:** EU AI Act (Regulation 2024/1689)
> **Severity:** Critical — legal requirement before placing high-risk AI on EU market
> **Related issue:** [#129](https://github.com/wlfghdr/agentic-enterprise/issues/129)
> **Related compliance doc:** [EU AI Act Compliance Reference](../eu-ai-act.md)
> **Enforcement date:** August 2026 for high-risk obligations

---

## 1. Purpose

The EU AI Act (Art. 43) requires providers of high-risk AI systems to complete a conformity assessment before placing any such system on the EU market or putting it into service. This assessment verifies that the system meets all applicable requirements in Chapter III, Section 2 of the regulation — covering risk management, data governance, technical documentation, transparency, human oversight, accuracy, robustness, and cybersecurity.

The Agentic Enterprise framework provides the **governance design and operational structure** that maps to many of these requirements (see the [article-level mapping in the compliance reference](../eu-ai-act.md)). This guide provides the conformity assessment procedure, decision tree for risk classification, and documentation package template aligned to Annex IV and Annex VI that adopters need to demonstrate compliance when deploying high-risk AI systems in the EU.

Specifically, this guide provides the risk classification decision tree, step-by-step internal conformity assessment procedure, and mappings from framework artifacts to the required documentation — connecting the framework's control design to the EU AI Act's pre-market obligations.

---

## 2. Risk Classification Decision Tree

Before any conformity assessment, adopters must determine which risk category applies to each AI system. The EU AI Act uses a layered classification that determines the scope of obligations.

### Step 1: Is it prohibited? (Art. 5)

Check whether the AI system falls under any prohibited practice:

- **Social scoring** by public authorities based on social behavior or personal characteristics
- **Subliminal manipulation** beyond a person's consciousness causing harm
- **Exploitation of vulnerabilities** of specific groups (age, disability, social/economic situation)
- **Real-time remote biometric identification** in publicly accessible spaces for law enforcement (with narrow exceptions for missing children, imminent threats, and serious criminal suspects)
- **Biometric categorization** using sensitive characteristics (race, political opinions, sexual orientation)
- **Untargeted scraping** of facial images for facial recognition databases
- **Emotion recognition** in workplace and educational institutions (with medical/safety exceptions)
- **Predictive policing** based solely on profiling or personality traits

**If prohibited:** STOP. The system cannot be developed, placed on the market, or put into service in the EU. No conformity assessment path exists — redesign or abandon the use case.

### Step 2: Is it high-risk? (Art. 6)

High-risk classification occurs through two independent paths:

**Annex I path — Safety component of regulated products:**

If the AI system is intended to be used as a safety component of a product, or is itself a product, covered by EU harmonization legislation listed in Annex I, and that product is required to undergo a third-party conformity assessment under that legislation, the AI system is high-risk. Examples include:

- Machinery (Regulation 2023/1230)
- Medical devices (Regulation 2017/745)
- In vitro diagnostic medical devices (Regulation 2017/746)
- Toys (Directive 2009/48/EC)
- Lifts (Directive 2014/33/EU)
- Radio equipment (Directive 2014/53/EU)
- Motor vehicles (various type-approval regulations)

**Annex III path — Standalone high-risk AI in specified areas:**

| Annex III Area | Examples |
|----------------|----------|
| 1. Biometric identification and categorization | Remote biometric identification (not real-time for law enforcement, which is prohibited), biometric categorization by sensitive attributes |
| 2. Critical infrastructure management | AI managing safety of road traffic, water/gas/heating/electricity supply, digital infrastructure |
| 3. Education and vocational training | AI determining access to education, evaluating learning outcomes, monitoring prohibited behavior during tests |
| 4. Employment and worker management | AI for recruitment, screening, hiring decisions, task allocation, performance monitoring, promotion/termination |
| 5. Essential private and public services | AI for credit scoring, insurance risk assessment, emergency service dispatch, benefits eligibility |
| 6. Law enforcement | AI for individual risk assessment (recidivism), polygraphs, evidence reliability assessment, profiling |
| 7. Migration, asylum, border control | AI for risk assessment (security, irregular migration, health), verification of travel document authenticity |
| 8. Justice and democratic processes | AI assisting judicial authorities in researching/interpreting facts and law, applying law to facts |

**Exception (Art. 6(3)):** An Annex III system is NOT high-risk if it does not pose a significant risk of harm to health, safety, or fundamental rights — specifically if the AI system is intended to:
- Perform a narrow procedural task
- Improve the result of a previously completed human activity
- Detect decision-making patterns without replacing human assessment
- Perform a preparatory task for an assessment relevant to Annex III use cases

Providers relying on this exception must document their reasoning and notify the relevant national authority before placing the system on the market.

### Step 3: If high-risk, which conformity assessment path?

| System Type | Assessment Path | Legal Basis |
|-------------|----------------|-------------|
| **Annex I systems** (safety component of regulated product) | Follow the conformity assessment required by the relevant product-specific EU legislation (e.g., MDR for medical devices, Machinery Regulation for industrial equipment) | Art. 43(3) |
| **Annex III systems — general** | Internal conformity assessment (self-assessment by provider following Annex VI) | Art. 43(2) |
| **Annex III, point 1 — biometric identification** | Third-party conformity assessment by a notified body (following Annex VII) | Art. 43(1) |

### Step 4: If limited-risk (Art. 50)

Systems with transparency obligations only:
- **AI systems interacting with natural persons** (chatbots) — must disclose that the person is interacting with AI
- **Emotion recognition / biometric categorization** (non-prohibited uses) — must inform persons being exposed
- **AI-generated content** (deepfakes, synthetic text/audio/image/video) — must label content as AI-generated

No conformity assessment required. Transparency obligations apply from August 2025.

### Step 5: If minimal-risk

No mandatory obligations. Providers are encouraged to voluntarily adhere to codes of conduct (Art. 95). No conformity assessment or transparency obligations apply.

---

## 3. Internal Conformity Assessment (Annex VI)

This section provides the step-by-step procedure for the internal conformity assessment, which is the default path for most Annex III high-risk AI systems.

### 3a. Prerequisites

Before beginning the assessment, the following must be in place:

| Prerequisite | EU AI Act Article | Framework Artifact |
|-------------|-------------------|-------------------|
| Quality management system | Art. 17 | Quality policies in [`org/4-quality/policies/`](../../../org/4-quality/policies/), process loops in [`process/`](../../../process/), CODEOWNERS |
| Technical documentation | Art. 11, Annex IV | Technical designs, mission briefs, agent type definitions, model cards — see Section 3c below |
| Risk management system | Art. 9 | [Risk Management Policy](../../../org/4-quality/policies/risk-management.md), risk register, KRI dashboards |
| Data governance measures | Art. 10 | [Data Classification Policy](../../../org/4-quality/policies/data-classification.md), [Privacy Policy](../../../org/4-quality/policies/privacy.md) |

### 3b. Assessment Steps

Execute each step sequentially. Document results in a conformity assessment report. For each step, record: what was assessed, evidence reviewed, findings, and pass/fail determination.

**Step 1 — Verify QMS compliance (Art. 17)**

Review the quality management system documentation against Art. 17 requirements:

- [ ] Regulatory compliance strategy documented
- [ ] Design and development procedures described (map to framework process loops)
- [ ] Design verification and validation procedures in place
- [ ] Testing and validation procedures documented
- [ ] Technical standards and specifications identified and applied
- [ ] Systems and procedures for data management (collection, analysis, labelling, storage, aggregation, retention, deletion)
- [ ] Risk management system documented (see Step 3)
- [ ] Post-market monitoring system planned (Art. 72)
- [ ] Procedures for reporting serious incidents (Art. 62) and malfunctions
- [ ] Communication with competent authorities, notified bodies, users, and other stakeholders
- [ ] Record-keeping system operational
- [ ] Resource management (human, technical, financial) documented
- [ ] Accountability framework established (CODEOWNERS, instruction hierarchy, approval gates)
- [ ] Corrective action procedures defined

**Step 2 — Review technical documentation (Annex IV completeness)**

Verify all elements listed in Annex IV are present and current. See Section 3c for the detailed checklist.

**Step 3 — Assess risk management system (Art. 9)**

Verify the risk management system is:

- [ ] Continuous and iterative throughout the AI system lifecycle
- [ ] Planned, implemented, documented, and maintained as a systematic process
- [ ] Updated when substantial modifications occur
- [ ] Identifying and analyzing known and reasonably foreseeable risks
- [ ] Estimating and evaluating risks from intended use and reasonably foreseeable misuse
- [ ] Adopting risk management measures (elimination, mitigation, information/training)
- [ ] Testing to identify the most appropriate risk management measures
- [ ] Considering combined effects of risks
- [ ] Addressing risks specific to the persons or groups likely to be affected

The framework's [Risk Management Policy](../../../org/4-quality/policies/risk-management.md) provides the structural foundation. Adopters must verify that the AI-specific risk taxonomy, KRI thresholds, and circuit breaker mechanisms are configured for the specific AI system under assessment.

**Step 4 — Verify data governance (Art. 10)**

For any AI system trained, validated, or tested using data:

- [ ] Training, validation, and testing datasets are subject to data governance practices
- [ ] Data collection processes are documented (sources, original purpose, scope)
- [ ] Data preparation operations are documented (annotation, labelling, cleaning, enrichment)
- [ ] Relevant assumptions about information the data measures/represents are documented
- [ ] Assessment of data availability, quantity, and suitability is performed
- [ ] Bias examination and appropriate mitigation measures are implemented
- [ ] Relevant data gaps or shortcomings are identified and documented
- [ ] Appropriate statistical properties (including representativeness) are verified per the geographic, contextual, behavioral, or functional setting

**Step 5 — Test accuracy, robustness, and cybersecurity (Art. 15)**

- [ ] Accuracy levels are determined and stated in instructions for use
- [ ] Accuracy metrics are appropriate to the intended purpose
- [ ] Resilience to errors, faults, and inconsistencies is tested
- [ ] Technical redundancy solutions (including backup/fail-safe plans) are in place where appropriate
- [ ] AI system is resilient to attempts by unauthorized third parties to exploit vulnerabilities
- [ ] Cybersecurity measures are appropriate to circumstances and risks
- [ ] Testing includes adversarial scenarios as documented in the [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) (OWASP LLM Top 10 coverage)

**Step 6 — Verify human oversight design (Art. 14)**

- [ ] AI system is designed for effective human oversight during the period it is in use
- [ ] Human oversight measures are identified and built into the system by the provider, or identified as appropriate for implementation by the deployer
- [ ] Persons exercising oversight can: understand the system's capabilities and limitations, remain aware of automation bias, correctly interpret output, decide not to use or override the system, and intervene or interrupt the system
- [ ] For Annex III point 1(a) systems (biometric identification): at least two natural persons verify each identification before acting on the result

The framework's human oversight architecture — the instruction hierarchy in `AGENTS.md` Rule 2 ("Humans decide, agents recommend"), PR approval gates, and `governance.decision` telemetry events — provides the structural foundation. Document how these mechanisms apply to the specific AI system.

**Step 7 — Verify logging capability (Art. 12)**

- [ ] AI system permits automatic recording of events (logs) throughout its lifetime
- [ ] Logging enables monitoring of system operation (as described in Art. 26(5))
- [ ] Logging capability conforms to recognized standards or common specifications
- [ ] Logs record: periods of use, reference database used, input data, identification of natural persons involved in verification

The framework's [OTel contract](../../../docs/otel-contract.md) and [Observability Policy](../../../org/4-quality/policies/observability.md) define the logging architecture. Verify that the spans, attributes, and retention periods satisfy Art. 12 requirements for the specific AI system.

**Step 8 — Verify transparency and instructions for use (Art. 13)**

- [ ] AI system is designed to operate with sufficient transparency for deployers to interpret output and use it appropriately
- [ ] Instructions for use are provided in an appropriate digital or non-digital format
- [ ] Instructions include: provider identity and contact, AI system characteristics/capabilities/limitations, intended purpose, level of accuracy/robustness/cybersecurity (Art. 15), known foreseeable circumstances that may lead to risks, specifications for input data, and information enabling deployers to interpret AI system output

**Step 9 — Issue declaration of conformity (Art. 47)**

Upon successful completion of Steps 1-8 with no unresolved findings:

- Draft the EU declaration of conformity (see [companion guide on CE marking](eu-ai-act-ce-marking.md), Section 3)
- The declaration is issued under the sole responsibility of the provider
- It states that the AI system complies with the requirements of Chapter III, Section 2
- Keep the declaration up to date and available for 10 years

**Step 10 — Affix CE marking (Art. 48)**

- Apply the CE marking to the AI system following the [CE Marking & EU Database Registration Guide](eu-ai-act-ce-marking.md)
- For software-only systems, the CE marking appears in digital form

### 3c. Technical Documentation Package (Annex IV)

The following checklist enumerates every element required by Annex IV. For each item, identify the source artifact within the framework and produce a consolidated documentation package.

**Section 1 — General description of the AI system:**

- [ ] Intended purpose of the AI system
- [ ] Provider name and contact information
- [ ] Version or date of the AI system and any previous versions
- [ ] How the AI system interacts with hardware or software that is not part of the AI system itself (where applicable)
- [ ] Versions of relevant software or firmware, and any dependency requirements
- [ ] Description of all forms of output (text, speech, visual, numerical, etc.)
- [ ] Instructions for use

**Section 2 — Detailed description of system elements and development process:**

- [ ] Methods and steps for development, including use of pre-trained systems or third-party tools and how these were obtained
- [ ] Design specifications: general logic of the AI system, principal design choices including rationale and assumptions, classification choices, optimization targets and metrics
- [ ] System architecture: dependencies between software components, computational resources used (development and deployment), data flows, and audit mechanisms
- [ ] Where applicable: computational and hardware requirements, model description (type, training methodology), and training choices (techniques, hyperparameters, architecture decisions)
- [ ] Data requirements: datasheets for training/validation/test datasets, data sources, scope and characteristics, labelling methodology, data cleaning methodology, and data gaps analysis
- [ ] Assessment of human oversight measures (Art. 14) including technical measures for deployers

**Section 3 — Monitoring, functioning, and control:**

- [ ] Description of the AI system's capabilities and limitations in performance (accuracy, robustness, cybersecurity — Art. 15)
- [ ] Degrees of accuracy and relevant metrics for the specific intended purpose, known foreseeable circumstances of misuse
- [ ] Possible unintended outcomes and sources of risk to health, safety, and fundamental rights
- [ ] Human interface tools for deployers

**Section 4 — Risk management system:**

- [ ] Full description of the risk management system per Art. 9
- [ ] Description of residual acceptable risks with justification

**Section 5 — Data governance:**

- [ ] Training methodologies and techniques, datasets used
- [ ] Description of data provenance, scope, characteristics
- [ ] Explanation of how data was obtained and selected
- [ ] Labelling procedures, data cleaning methods
- [ ] Information about data gaps and how they were addressed

**Section 6 — Testing and validation:**

- [ ] Validation and testing procedures used, including information about validation/testing data, metrics, and test logs
- [ ] Specific testing conditions under which the AI system was tested and validated
- [ ] Information about actual testing results and whether the system met the initial requirements

**Section 7 — Cybersecurity:**

- [ ] Technical solutions to address cybersecurity threats (Art. 15) — specific to the AI system and its environment of use

**Section 8 — Lifecycle changes:**

- [ ] Description of all changes made to the system through its lifecycle
- [ ] Version history and change management documentation

---

## 4. Third-Party Conformity Assessment

This section applies when a notified body must be involved — specifically for biometric identification systems under Annex III, point 1, or when a provider voluntarily opts for third-party assessment.

### When Required

- **Mandatory:** Remote biometric identification systems (Annex III, point 1) — Art. 43(1) requires assessment by a notified body following Annex VII
- **Voluntary:** Any provider of a high-risk AI system may choose to involve a notified body even when internal assessment is sufficient
- **Annex I systems:** Follow the product-specific assessment procedure, which may or may not involve a notified body depending on the relevant harmonization legislation

### Notified Body Selection

- The notified body must be designated by an EU member state under Art. 28-39
- It must be accredited and competent for the specific category of AI system
- Check the EU NANDO database (New Approach Notified and Designated Organisations) for designated bodies once they become available
- Ensure the notified body has no conflicts of interest (Art. 31)

### Assessment Procedure (Annex VII)

The Annex VII procedure requires the notified body to:

1. **Examine the application** including the technical documentation
2. **Assess the quality management system** (Art. 17) to determine if it ensures conformity
3. **Examine the technical documentation** to assess whether the AI system meets the applicable requirements
4. **Verify that the design and development** of the AI system and the QMS satisfy the requirements
5. **Issue an EU-type examination certificate** if the system and QMS are in conformity, or refuse with detailed explanation if not

### Timeline and Cost

| Planning Factor | Estimate |
|----------------|----------|
| Notified body selection and contracting | 1-3 months |
| Pre-assessment preparation (documentation, QMS readiness) | 2-4 months |
| Formal assessment by notified body | 3-6 months |
| Remediation of findings (if any) | 1-3 months |
| **Total end-to-end** | **6-12 months** |
| Cost (varies by complexity, system scope, and member state) | EUR 50,000 - 200,000+ |

Plan for the longer end of these estimates if the AI system is complex or if the provider has not previously undergone a comparable assessment (e.g., ISO 42001 certification or MDR assessment).

---

## 5. Framework Artifacts Mapping to Art. 11 Technical Documentation

The Agentic Enterprise framework produces governance and operational artifacts that can serve as building blocks for the Annex IV technical documentation package. This mapping shows where existing framework artifacts satisfy (or partially satisfy) each documentation requirement, and what additional work is needed.

| Annex IV Requirement | Framework Artifact | Coverage | Action Needed |
|---------------------|-------------------|----------|---------------|
| General AI system description | Mission briefs (`work/missions/`), technical designs (`work/missions/*/technical-design.md`) | Partial | Consolidate into a single Annex IV Section 1 document; add provider identity, intended purpose statement, and version history |
| Design specifications and architecture | Technical design documents, agent type definitions (`org/agents/`) | Partial | Add model architecture details, optimization targets, and classification rationale |
| Development process | Git history, PR trail, CI/CD pipeline records | Good | Export and structure as chronological development lifecycle evidence |
| Risk management system | [Risk Management Policy](../../../org/4-quality/policies/risk-management.md), risk register, KRI dashboards | Good | Map to Art. 9 continuous risk management format; ensure AI-specific risk taxonomy is complete |
| Data governance | [Data Classification Policy](../../../org/4-quality/policies/data-classification.md), [Privacy Policy](../../../org/4-quality/policies/privacy.md) | Partial | Extend with training data documentation: datasheets, provenance, cleaning methodology, bias analysis |
| Testing procedures and results | Quality evaluations, CI/CD test results, [Agent Eval Policy](../../../org/4-quality/policies/agent-eval.md) | Partial | Package as structured validation evidence with specific metrics and test conditions |
| Human oversight design | Agent instruction hierarchy (`AGENTS.md` Rule 2), approval gates, `governance.decision` events | Good | Document as Art. 14 human oversight mechanisms specific to the AI system |
| Logging capability | [OTel contract](../../../docs/otel-contract.md), [Observability Policy](../../../org/4-quality/policies/observability.md), [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) | Good | Map OTel span types and retention periods to Art. 12 record-keeping requirements |
| Cybersecurity measures | [Security Policy](../../../org/4-quality/policies/security.md), [Agent Security Policy](../../../org/4-quality/policies/agent-security.md), [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) | Good | Consolidate security documentation and add AI-specific threat model |
| Lifecycle changes | Git version history, CHANGELOG, PR descriptions | Good | Structure as Annex IV Section 8 change documentation |

---

## 6. Quality Management System Evidence (Art. 17)

Art. 17 requires providers to put in place and document a quality management system. The following table maps each Art. 17 requirement to the framework's existing governance structure, identifying what is already in place and what adopters must supplement.

| Art. 17 Requirement | Framework Implementation | Supplementary Action |
|---------------------|-------------------------|---------------------|
| Compliance strategy and regulatory adherence | Quality policies in [`org/4-quality/policies/`](../../../org/4-quality/policies/), [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md) | Document regulatory mapping specific to AI systems being deployed |
| Design and development procedures | Process loops in [`process/`](../../../process/) — Discover, Build, Ship, Operate | Map process steps to AI system development lifecycle |
| Design verification and validation | Quality layer evaluations, [Agent Eval Policy](../../../org/4-quality/policies/agent-eval.md), CI/CD gates | Add AI-specific validation procedures (accuracy benchmarks, fairness tests, robustness tests) |
| Testing and validation procedures | Quality evaluations, test automation in CI/CD | Document test methodologies, acceptance criteria, and evidence of test execution |
| Technical standards and specifications | Compliance reference documents in [`docs/compliance/`](../), framework policies | Identify and list all harmonized standards and common specifications applied |
| Data management systems and procedures | [Data Classification Policy](../../../org/4-quality/policies/data-classification.md), [Privacy Policy](../../../org/4-quality/policies/privacy.md) | Add training data lifecycle management: collection, annotation, storage, versioning, deletion |
| Risk management system | [Risk Management Policy](../../../org/4-quality/policies/risk-management.md), risk register, KRI dashboards, circuit breakers | Ensure risk management covers AI-specific risks (bias, drift, adversarial attacks) and operates continuously |
| Post-market monitoring | Operate loop in [`process/4-operate/`](../../../process/4-operate/), [Observability Policy](../../../org/4-quality/policies/observability.md) | Establish Art. 72 post-market monitoring plan specific to the AI system |
| Serious incident reporting | [Incident Response Policy](../../../org/4-quality/policies/incident-response.md), retrospectives in `work/retrospectives/` | Add EU AI Act Art. 62 reporting procedure (15-day / 2-day timelines, national authority notification) |
| Communication with authorities | Not currently in framework | Establish points of contact and procedures for communicating with national competent authorities and notified bodies |
| Record-keeping | Git history, OTel telemetry, [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) | Verify 10-year retention capability for conformity documentation |
| Resource management | Fleet configurations in [`org/2-orchestration/fleet-configs/`](../../../org/2-orchestration/fleet-configs/), instruction hierarchy | Document human, technical, and financial resources allocated to AI system compliance |
| Accountability framework | `CODEOWNERS`, RACI model, instruction hierarchy, approval gates | Map accountability structure to EU AI Act roles (provider, deployer, authorized representative) |
| Corrective action procedures | Improvement signals in `work/signals/`, retrospective process | Add formal corrective action and preventive action (CAPA) procedures for AI compliance findings |

---

## 7. Timeline for Compliance

The following timeline works backward from the August 2026 enforcement date for high-risk AI system obligations. Adjust dates based on your specific market entry plans — the deadline below represents the **latest possible** compliance date.

| Milestone | Target Date | Action | Responsible |
|-----------|------------|--------|-------------|
| Risk classification | Immediately | Determine if each AI system is prohibited, high-risk, limited-risk, or minimal-risk using the decision tree in Section 2 | Legal, AI/ML team leads |
| Gap analysis | Q2 2025 | Map current documentation and processes against Annex IV and Art. 17 requirements using Section 5 and Section 6 of this guide | Compliance, Engineering |
| QMS documentation | Q3-Q4 2025 | Build or supplement quality management system documentation to satisfy Art. 17 | Quality team, Compliance |
| Technical documentation | Q3-Q4 2025 | Compile Annex IV documentation package using Section 3c checklist | Engineering, AI/ML leads |
| Risk management system maturity | Q4 2025 | Ensure Art. 9 continuous risk management is operational and producing evidence | Risk management, Engineering |
| Data governance maturity | Q4 2025 | Complete training data documentation, bias analysis, data quality procedures per Art. 10 | Data team, AI/ML leads |
| Internal conformity assessment | Q1 2026 | Execute the Annex VI procedure per Section 3b of this guide | Cross-functional assessment team |
| Notified body engagement (if needed) | Q3 2025 | Select and contract notified body; begin pre-assessment preparation | Legal, Compliance |
| Remediation of findings | Q1-Q2 2026 | Address any gaps identified during internal or third-party assessment | Engineering, Quality |
| Declaration of conformity | Q2 2026 | Issue Art. 47 declaration (see [CE marking guide](eu-ai-act-ce-marking.md)) | Legal, Provider management |
| CE marking | Q2 2026 | Affix CE marking per Art. 48 (see [CE marking guide](eu-ai-act-ce-marking.md)) | Engineering, Legal |
| EU database registration | Q2 2026 | Register in the EU AI database per Art. 49 (see [CE marking guide](eu-ai-act-ce-marking.md)) | Compliance |
| Post-market monitoring | Before market entry | Establish Art. 72 post-market monitoring plan | Operations, Quality |
| **High-risk enforcement deadline** | **August 2026** | **Full compliance required for high-risk AI systems** | **All** |

---

## 8. Verification Checklist

Use this checklist to confirm that conformity assessment preparation is complete. Every item must be checked before issuing the declaration of conformity.

### Risk Classification
- [ ] Each AI system is classified (prohibited / high-risk / limited-risk / minimal-risk)
- [ ] Classification rationale is documented with reference to Art. 5, 6, and Annex I/III
- [ ] Art. 6(3) exception analysis documented (if claiming non-high-risk for Annex III system)

### Conformity Assessment Path
- [ ] Assessment path determined (internal Annex VI / third-party Annex VII / product-specific)
- [ ] Notified body engaged and contracted (if third-party assessment required)

### Technical Documentation (Annex IV)
- [ ] General AI system description complete (Section 1)
- [ ] Detailed system elements and development process documented (Section 2)
- [ ] Monitoring, functioning, and control described (Section 3)
- [ ] Risk management system documented (Section 4)
- [ ] Data governance documented (Section 5)
- [ ] Testing and validation documented (Section 6)
- [ ] Cybersecurity measures documented (Section 7)
- [ ] Lifecycle changes documented (Section 8)

### Quality Management System (Art. 17)
- [ ] QMS documentation complete per Art. 17 requirements
- [ ] All 14 QMS elements addressed (see Section 6 mapping)
- [ ] QMS is operational (not just documented — evidence of execution exists)

### Requirements Verification
- [ ] Risk management system operational and documented (Art. 9)
- [ ] Data governance measures documented and implemented (Art. 10)
- [ ] Human oversight mechanisms documented and designed into the system (Art. 14)
- [ ] Logging capability verified and operational (Art. 12)
- [ ] Transparency and instructions for use complete (Art. 13)
- [ ] Accuracy, robustness, and cybersecurity testing completed with documented results (Art. 15)

### Completion
- [ ] All assessment findings resolved or documented with justification
- [ ] Declaration of conformity prepared with all required content (Art. 47)
- [ ] CE marking prepared for affixing (Art. 48)
- [ ] EU database registration data prepared (Art. 49)
- [ ] 10-year document retention plan established
- [ ] Post-market monitoring system operational (Art. 72)
- [ ] Serious incident reporting procedure established (Art. 62)
