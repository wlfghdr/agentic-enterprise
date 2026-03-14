<!-- placeholder-ok -->
# AI Governance & Responsible AI Policy

> **Applies to:** All AI/ML models, agent types, LLM-powered workflows, automated decision systems, and AI-generated outputs
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team, Steering Layer
> **Version:** 1.0 | **Last updated:** 2026-03-14

---

## Principles

1. **Transparent by default** — Every AI system documents what it does, how it works, what data it uses, and what its known limitations are. Opacity is a governance failure, not a design choice.
2. **Fair and non-discriminatory** — AI outputs must not systematically disadvantage individuals or groups based on protected characteristics. Fairness is measured, not assumed.
3. **Accountable to humans** — AI systems recommend; humans decide on high-impact matters. Every AI-assisted decision has a traceable chain: model → output → review → decision → outcome.
4. **Proportional governance** — Governance rigor scales with the impact and autonomy level of the AI system. A code formatting agent needs less governance than an agent that influences hiring or financial decisions.
5. **Continuously validated** — AI systems degrade over time (data drift, model drift, context drift). Governance is not a one-time certification but a continuous evaluation loop.

---

## 1. AI System Risk Classification

All AI systems must be classified by risk level. This classification determines governance requirements throughout this policy. The classification aligns with EU AI Act risk tiers and maps to the agent autonomy tiers defined in [risk-management.md](risk-management.md) Section 6.1.

### 1.1 Risk Tiers

| Tier | Label | Definition | Examples | Governance Level |
|------|-------|-----------|----------|-----------------|
| **0** | **Prohibited** | AI uses that are fundamentally incompatible with organizational values and applicable law | Social scoring, real-time biometric identification (unless legally mandated), manipulative AI, exploitation of vulnerabilities | **Blocked** — must not be built or deployed |
| **1** | **High-Risk** | AI that materially affects individuals' rights, opportunities, safety, or financial outcomes | Hiring/screening decisions, credit/insurance scoring, medical triage, legal analysis, safety-critical systems | **Full governance** — model card, fairness audit, DPIA, human oversight, explainability |
| **2** | **Limited-Risk** | AI that interacts with people or generates content that could be mistaken for human-created | Customer-facing chatbots, content generation, summarization for external use, automated email drafting | **Transparency** — model card, output labeling, human review for sensitive content |
| **3** | **Minimal-Risk** | AI used for internal tooling, code assistance, or operational automation with low external impact | Code generation, internal search, log analysis, test generation, internal summarization | **Standard** — model card (lightweight), token budget, standard observability |

### 1.2 Classification Rules

- [ ] Every agent type in the Agent Type Registry documents its AI risk tier in the Model Governance section
- [ ] Risk tier classification is reviewed when the agent's scope, autonomy level, or data access changes
- [ ] Tier 0 (Prohibited) uses are blocked at design time — no mission brief may authorize prohibited AI uses
- [ ] When classification is uncertain, apply the higher tier until the data owner and security team confirm
- [ ] Risk tier classification is documented in the agent type definition and cross-referenced in the model card

---

## 2. Model Cards

Every AI system that uses an LLM or ML model must maintain a model card. Model cards are the transparency artifact that makes AI systems inspectable, comparable, and auditable. The depth of the model card scales with the risk tier.

### 2.1 Model Card Requirements by Risk Tier

| Section | Tier 3 (Minimal) | Tier 2 (Limited) | Tier 1 (High) |
|---------|-----------------|-----------------|----------------|
| Model identity | Required | Required | Required |
| Intended use & scope | Required | Required | Required |
| Model selection rationale | Recommended | Required | Required |
| Training data summary | Not required | Recommended | Required |
| Performance & accuracy | Recommended | Required | Required |
| Known limitations & failure modes | Required | Required | Required |
| Fairness evaluation | Not required | Recommended | **Required** |
| Explainability approach | Not required | Recommended | **Required** |
| Adversarial robustness | Not required | Recommended | **Required** |
| Token budget & cost | Required | Required | Required |

### 2.2 Mandatory Requirements

- [ ] Every agent type that uses an LLM or ML model includes a Model Governance section in its agent type definition (see updated `org/agents/_TEMPLATE-agent-type.md`)
- [ ] Model cards are reviewed when the model version changes, the agent scope changes, or at minimum annually
- [ ] Model cards for Tier 1 (High-Risk) systems are reviewed and approved by the security team before deployment
- [ ] Model selection rationale documents why this model was chosen over alternatives (capability, cost, safety, licensing)

### 2.3 Model Card Template Structure

Model cards are embedded in agent type definitions (not standalone files) to keep governance co-located with the system it governs. The Model Governance section in `org/agents/_TEMPLATE-agent-type.md` provides the governed structure.

---

## 3. Fairness Audit

AI systems classified as Tier 1 (High-Risk) or Tier 2 (Limited-Risk) must undergo fairness evaluation. The goal is to detect and mitigate systematic bias before it affects individuals.

### 3.1 What to Evaluate

- [ ] **Output consistency** — Does the system produce materially different outputs for inputs that differ only in protected characteristics (gender, race, age, disability, religion, nationality)?
- [ ] **Demographic parity** — Are outcomes distributed proportionally across demographic groups where proportional outcomes are expected?
- [ ] **Error rate parity** — Are false positive and false negative rates comparable across demographic groups?
- [ ] **Representation bias** — Does the system's training data or prompt context systematically underrepresent or misrepresent groups?
- [ ] **Feedback loop risk** — Could the system's outputs reinforce existing biases through data feedback loops?

### 3.2 Audit Process

- [ ] **Tier 1 (High-Risk):** Fairness audit before initial deployment and after every model change. Quarterly re-evaluation using production data. Results documented in quality evaluation report.
- [ ] **Tier 2 (Limited-Risk):** Fairness review before initial deployment. Annual re-evaluation. Results documented.
- [ ] **Tier 3 (Minimal-Risk):** No formal fairness audit required. Standard quality evaluation applies.
- [ ] Fairness audits use representative test datasets that cover relevant demographic dimensions
- [ ] Audit results that show material bias trigger a mandatory remediation cycle before deployment or continued operation
- [ ] Remediation may include: prompt engineering, guardrails, output filtering, model switching, scope restriction, or human-in-the-loop override

### 3.3 Fairness Metrics

Adopters should select metrics appropriate to their use case. Common metrics include:

- **Demographic parity ratio** — ratio of positive outcomes between groups (target: 0.8–1.25 per EEOC four-fifths rule where applicable)
- **Equalized odds difference** — difference in true positive and false positive rates between groups
- **Predictive parity** — equal precision across groups
- **Individual fairness** — similar inputs produce similar outputs regardless of group membership

The specific thresholds are deployment-customizable (see Section 7).

---

## 4. Adversarial Robustness

AI systems must be tested for robustness against adversarial inputs beyond prompt injection (which is covered by [agent-security.md](agent-security.md)). This section covers behavioral robustness — ensuring the system behaves correctly under stress, manipulation, and distribution shift.

### 4.1 Testing Requirements by Risk Tier

| Test Category | Tier 3 | Tier 2 | Tier 1 |
|--------------|--------|--------|--------|
| Prompt injection & jailbreak | Per [agent-security.md](agent-security.md) | Per agent-security.md | Per agent-security.md |
| Role-play / persona manipulation | Not required | **Required** | **Required** |
| Instruction override attempts | Per agent-security.md | Per agent-security.md | Per agent-security.md |
| Output consistency under paraphrase | Not required | Recommended | **Required** |
| Boundary probing (scope escape) | Recommended | **Required** | **Required** |
| Multi-turn manipulation | Not required | Recommended | **Required** |
| Adversarial examples in structured data | Not required | Not required | **Required** |

### 4.2 Mandatory Requirements

- [ ] Tier 1 and Tier 2 systems maintain an adversarial test suite with documented test cases
- [ ] Test suites are run before deployment, after model changes, and on a quarterly cadence
- [ ] Test results are documented in quality evaluation reports
- [ ] Failed adversarial tests block deployment for Tier 1 systems; trigger review for Tier 2
- [ ] Adversarial test cases cover the categories required for the system's risk tier (per table above)

### 4.3 Relationship to Agent Security

This section extends — not replaces — [agent-security.md](agent-security.md). Agent-security.md covers security-specific threats (prompt injection, tool abuse, privilege escalation). This section covers behavioral robustness (consistency, manipulation resistance, scope adherence). Both apply. When in doubt, apply both sets of requirements.

---

## 5. Explainability

AI systems that influence decisions affecting individuals, finances, or organizational strategy must provide appropriate explainability. The goal is not to explain every token but to make the decision rationale inspectable when it matters.

### 5.1 Explainability Levels

| Level | When Required | What It Means |
|-------|--------------|---------------|
| **Traceable** | All AI systems (Tier 1–3) | The inputs, model version, and outputs are logged and correlatable via observability (OTel traces). The "what happened" is always answerable. |
| **Justifiable** | Tier 1 and Tier 2 systems | The system can produce a human-readable rationale for its output — why it recommended this action, flagged this risk, or generated this content. Rationale is logged alongside the output. |
| **Auditable** | Tier 1 systems | The full decision chain is reconstructable: input → model reasoning → output → human review → final decision → outcome. Sufficient for regulatory inquiry or legal discovery. |

### 5.2 Mandatory Requirements

- [ ] All AI systems meet the **Traceable** level — inputs, model version, and outputs logged per `docs/OTEL-CONTRACT.md`
- [ ] Tier 1 and Tier 2 systems meet the **Justifiable** level — outputs include or can produce a human-readable rationale
- [ ] Tier 1 systems meet the **Auditable** level — full decision chain reconstructable from observability data and work artifacts
- [ ] High-impact automated decisions (per [risk-management.md](risk-management.md) §6.1 autonomy tiers) include a `governance.decision` span event with `governance.reason` attribute documenting the rationale
- [ ] When a human overrides an AI recommendation, both the original recommendation and the override rationale are logged

### 5.3 What Does NOT Require Explainability Beyond Traceability

- Code formatting, linting, and style suggestions (Tier 3)
- Internal log summarization (Tier 3)
- Test case generation (Tier 3)
- Build/CI automation decisions (Tier 3, unless safety-critical)

---

## 6. Token Usage Accountability

AI compute costs must be attributable, budgeted, and monitored. Uncontrolled token consumption is both a financial risk (FI-2 in [risk-management.md](risk-management.md)) and a governance gap.

### 6.1 Mandatory Requirements

- [ ] Token usage is tracked per inference call via `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` attributes on `inference.*` spans (per `docs/OTEL-CONTRACT.md`)
- [ ] Token costs are attributable to specific missions, agent types, and divisions (per [observability.md](observability.md) agent fleet dashboard requirements)
- [ ] Each mission type has a token budget ceiling defined in the mission brief or fleet configuration — exceeding the ceiling triggers escalation, not automatic halt (unless `{{RISK_KILL_SWITCH_TARGET_SECONDS}}` applies)
- [ ] Agent types document their expected token consumption range in the Model Governance section of their agent type definition
- [ ] Token consumption trends are monitored via the observability platform — anomalous spikes (> 3x baseline) trigger automated alerts
- [ ] Cost attribution dashboards are available to mission sponsors and division leads

### 6.2 Budget Enforcement

Token budgets are advisory guardrails, not hard kill switches (unless the risk management kill switch is triggered). The enforcement model:

1. **Monitoring** — observability platform tracks token consumption per agent, mission, and division in real-time
2. **Warning** — at 80% of mission token budget, the orchestration agent is notified
3. **Escalation** — at 100% of budget, the mission sponsor is notified and must approve continuation
4. **Emergency halt** — only when token consumption indicates a runaway loop (per [risk-management.md](risk-management.md) §6.3 cascade failure prevention)

---

## 7. Deployment-Customizable Decisions

The framework defines the governance structure. Each adopter must configure the instance-specific details.

### Must Be Customized Per Instance / Deployment

- **Risk tier classification** for each agent type — the framework provides the tier definitions; adopters assign their agents to tiers based on their specific use cases and regulatory context
- **Fairness metrics and thresholds** — which metrics apply to each Tier 1/2 system, what thresholds constitute acceptable bias, and what demographic dimensions to evaluate
- **Token budget ceilings** — per mission type, agent type, and division; depends on model pricing and organizational cost tolerance
- **Adversarial test suites** — specific test cases relevant to the organization's agent portfolio and threat model
- **Explainability implementation** — how Justifiable and Auditable levels are technically achieved (chain-of-thought logging, retrieval attribution, decision tree export, etc.)
- **Model allowed list** — which LLM/ML models are approved for which risk tiers and use cases
- **Fairness audit cadence** — quarterly is the minimum for Tier 1; adopters may increase frequency based on regulatory requirements or risk appetite
- **EU AI Act applicability** — whether the organization's AI systems fall under EU AI Act scope and which specific obligations apply

### Must Not Be Customized Away

- The 4-tier risk classification structure (tiers may be subdivided but not collapsed)
- The model card requirement for all AI-using agent types
- The fairness audit requirement for Tier 1 (High-Risk) systems
- The Traceable explainability level for all AI systems
- The token usage tracking requirement
- The prohibition on Tier 0 (Prohibited) uses

---

## 8. Cross-Policy Alignment

| Policy | What This Policy Provides |
|--------|--------------------------|
| **[Agent Security Policy](agent-security.md)** | This policy extends agent-security.md with behavioral robustness testing (§4). Agent-security.md covers security threats (prompt injection, tool abuse); this policy covers fairness, transparency, and adversarial robustness. Both apply to all AI systems. |
| **[Risk Management Policy](risk-management.md)** | Risk tier classification (§1) maps to autonomy tiers in risk-management.md §6.1. AI risk taxonomy risks RE-2 (biased output), FI-2 (cost overrun), and CO-1 (regulatory violation) are operationalized by this policy's fairness audit, token accountability, and EU AI Act alignment. |
| **[Data Classification Policy](data-classification.md)** | AI systems processing CONFIDENTIAL or RESTRICTED data require higher governance rigor. Model cards document data classification of training data and inference inputs. PII in AI pipelines triggers privacy.md requirements. |
| **[Privacy Policy](privacy.md)** | AI features that process personal data must document this in the model card. DPIA is required for high-risk AI processing (per privacy.md §5). Consent and lawful basis requirements apply to AI training data and inference. |
| **[Observability Policy](observability.md)** | Token tracking, agent telemetry, and decision event spans are the technical foundation for explainability (§5) and token accountability (§6). This policy defines what must be observable; observability.md defines how. |
| **[Encryption & Key Management Policy](cryptography.md)** | AI model artifacts, training data, and inference I/O follow encryption requirements per data classification level. Model weights are encrypted at rest per cryptography.md §4.1. |

---

## 9. Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **ISO 42001:2023** | 6.1 AI risk management | §1 (risk classification) |
| **ISO 42001:2023** | 6.2 AI system lifecycle | §2 (model cards), §3 (fairness audit lifecycle) |
| **ISO 42001:2023** | 7.2 AI system transparency | §2 (model cards), §5 (explainability) |
| **ISO 42001:2023** | 8.4 Data for AI systems | §2.1 (training data summary), §8 cross-ref to data-classification.md |
| **ISO 42001:2023** | 9.1 Monitoring & measurement | §6 (token accountability), §3.2 (audit cadence) |
| **EU AI Act** | Art. 6 Classification of high-risk AI | §1 (risk tiers) |
| **EU AI Act** | Art. 9 Risk management system | §1, §4 (adversarial robustness) |
| **EU AI Act** | Art. 10 Data governance | §2.1 (training data), cross-ref to data-classification.md |
| **EU AI Act** | Art. 11 Technical documentation | §2 (model cards) |
| **EU AI Act** | Art. 13 Transparency | §5 (explainability) |
| **EU AI Act** | Art. 14 Human oversight | §5.2 (human override logging), cross-ref to risk-management.md §6.1 |
| **EU AI Act** | Art. 15 Accuracy, robustness, cybersecurity | §4 (adversarial robustness), §3 (fairness/accuracy) |
| **NIST AI RMF** | GOVERN — Governance structures | §1 (risk classification), §7 (customization) |
| **NIST AI RMF** | MAP — Context and risk identification | §1 (risk tiers), §2 (model cards) |
| **NIST AI RMF** | MEASURE — Quantify risks and impacts | §3 (fairness metrics), §6 (token metrics) |
| **NIST AI RMF** | MANAGE — Prioritize and respond | §3.2 (remediation), §6.2 (budget enforcement) |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Risk tier classification | All AI-using agent types have documented risk tier | Agent types using AI without risk tier classification |
| Model card completeness | Model card present with all sections required for the system's risk tier | Missing model card or incomplete for risk tier |
| Fairness audit (Tier 1) | Current fairness audit with documented metrics and no unmitigated material bias | No fairness audit, or audit shows unmitigated material bias |
| Fairness review (Tier 2) | Fairness review completed before deployment | Deployed without fairness review |
| Adversarial testing | Test suite exists and passes for required categories per risk tier | Missing test suite or failing tests for required categories |
| Explainability level | System meets the explainability level required for its risk tier | Explainability below required level for risk tier |
| Token tracking | Token usage tracked per inference call; attributable to mission and agent type | Token usage not tracked or not attributable |
| Token budget | Mission token budgets defined; escalation at ceiling | No budgets defined or uncontrolled consumption |
| Prohibited uses | No Tier 0 uses built or deployed | Prohibited AI use detected |
| Human oversight (Tier 1) | Human review documented for high-impact decisions | Automated high-impact decisions without human review |

---

## Related Policies

- **[Agent Security Policy](agent-security.md)** — Security-specific AI threats (prompt injection, tool abuse, OWASP LLM Top 10). This policy covers governance and responsible AI; agent-security.md covers security. Both apply.
- **[Risk Management Policy](risk-management.md)** — AI risk taxonomy (22 canonical risks), autonomy tiers, risk scoring, KRI monitoring. This policy operationalizes fairness (RE-2), cost control (FI-2), and regulatory compliance (CO-1).
- **[Data Classification & Handling Policy](data-classification.md)** — Data sensitivity classification. AI systems inherit handling requirements based on the classification of data they process.
- **[Privacy Policy](privacy.md)** — GDPR compliance. AI features processing personal data must comply with privacy.md in addition to this policy.
- **[Observability Policy](observability.md)** — Technical foundation for token tracking, decision tracing, and explainability evidence.
- **[Encryption & Key Management Policy](cryptography.md)** — Model artifact and inference data encryption requirements.

## References

- [ISO/IEC 42001:2023 — AI Management Systems](https://www.iso.org/standard/81230.html)
- [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 600-1 — Generative AI Profile](https://airc.nist.gov/Docs/1)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [IEEE 7010-2020 — Wellbeing Impact Assessment for AI](https://standards.ieee.org/ieee/7010/6573/)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-14 | Initial version — AI risk classification (4 tiers aligned to EU AI Act), model card requirements, fairness audit process (demographic parity, equalized odds, error rate parity), adversarial robustness testing, explainability levels (Traceable / Justifiable / Auditable), token usage accountability, compliance mapping (ISO 42001 / EU AI Act / NIST AI RMF). Closes #91. |
