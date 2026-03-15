# NIST AI Risk Management Framework — Compliance Reference

> **Framework:** NIST AI 100-1 — Artificial Intelligence Risk Management Framework (AI RMF 1.0)
> **Companion:** NIST AI 600-1 — Generative AI Profile
> **Scope:** Voluntary framework for managing risks in AI system design, development, deployment, and use
> **Official source:** [NIST AI RMF](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework)

## 1. What NIST AI RMF Requires

The AI RMF organizes risk management into four core functions:

### GOVERN — Establish AI governance

| Subcategory | Focus |
|-------------|-------|
| GOVERN 1 | Policies, processes, procedures, and practices for AI risk management |
| GOVERN 2 | Accountability structures and risk management roles |
| GOVERN 3 | Workforce diversity, equity, inclusion |
| GOVERN 4 | Organizational risk culture |
| GOVERN 5 | Stakeholder engagement processes |
| GOVERN 6 | Policies addressing third-party AI risks |

### MAP — Contextualize AI risks

| Subcategory | Focus |
|-------------|-------|
| MAP 1 | Context (intended purpose, users, affected parties) |
| MAP 2 | Interdependencies and broader context |
| MAP 3 | AI-specific risks mapped and categorized |
| MAP 4 | Risks and benefits across affected groups |
| MAP 5 | AI impacts likelihood and severity |

### MEASURE — Quantify AI risks

| Subcategory | Focus |
|-------------|-------|
| MEASURE 1 | Metrics to assess AI risks |
| MEASURE 2 | AI system evaluated for trustworthiness characteristics |
| MEASURE 3 | Mechanisms for tracking emergent risks |
| MEASURE 4 | Feedback mechanisms for continuous evaluation |

### MANAGE — Treat AI risks

| Subcategory | Focus |
|-------------|-------|
| MANAGE 1 | AI risks prioritized and responded to |
| MANAGE 2 | AI risk response strategies implemented |
| MANAGE 3 | Post-deployment AI risks monitored |
| MANAGE 4 | Risk management documented and reported |

## 2. How This Framework Addresses It

### Function-Level Mapping

| Function | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| **GOVERN 1** | Policies | 19 quality policies, AI Governance Policy, agent instruction hierarchy | Policy version history in Git |
| **GOVERN 1.7** | AI security policies | [Agent Security Policy](../../org/4-quality/policies/agent-security.md) — OWASP LLM Top 10 coverage | Security test results, CI/CD gates |
| **GOVERN 2** | Accountability | 5-layer model with explicit authority, CODEOWNERS RACI, agent type declarations | PR approvals, `governance.decision` events |
| **GOVERN 4** | Risk culture | [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — risk appetite statement, escalation culture | Risk register, escalation frequency metrics |
| **GOVERN 5** | Stakeholder engagement | Human-in-the-loop governance, PR-based review | PR comments, approval records |
| **GOVERN 6** | Third-party AI risk | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — AI vendor extended assessment | Vendor assessment records |
| **MAP 1** | Context | Agent type definitions with intended use, model cards | Agent type registry |
| **MAP 2** | Interdependencies | Architecture policy (dependency mapping), vendor risk (concentration risk tracking) | Dependency diagrams, vendor register |
| **MAP 3** | AI risk mapping | AI risk taxonomy — 22 canonical risks across 5 dimensions (OP/SE/CO/RE/FI) | Risk register artifacts |
| **MAP 5** | Impact assessment | [AI Governance Policy](../../org/4-quality/policies/ai-governance.md) — 4-tier risk classification, DPIA template | Risk tier assignments, DPIA records |
| **MEASURE 1** | Risk metrics | Risk Management Policy — 7 KRIs with thresholds and automated monitoring | KRI dashboards, OTel `risk.threshold.breach` events |
| **MEASURE 2** | Trustworthiness | Fairness audit (four-fifths rule), adversarial robustness testing, explainability levels | Fairness dashboards, test results |
| **MEASURE 3** | Emergent risks | Observability anomaly detection, improvement signals, behavioral drift monitoring | Automated signals, anomaly alerts |
| **MEASURE 4** | Feedback | 4-loop process (Loop 4 feeds signals back to Loop 1), retrospectives | Signal artifacts, retrospective records |
| **MANAGE 1** | Risk prioritization | Risk scoring (5x5 matrix), risk appetite alignment | Risk register with scores |
| **MANAGE 2** | Risk response | Treatment strategies (avoid/mitigate/transfer/accept), cascade failure prevention, circuit breakers | Treatment records, `risk.treatment.applied` events |
| **MANAGE 3** | Post-deployment monitoring | [Observability Policy](../../org/4-quality/policies/observability.md) — continuous agent monitoring, SLO tracking | OTel pipeline, SLO dashboards |
| **MANAGE 4** | Reporting | Risk register review cadence, monthly posture summaries, annual assessment | Reports, risk register updates |

### NIST AI 600-1 (Generative AI Profile) Additions

| GenAI Risk | Framework Coverage |
|------------|-------------------|
| **CBRN information** | Content Policy — accuracy requirements, AI governance — Tier 0 prohibitions |
| **Confabulation** | AI Governance — RE-1 hallucinated content risk, explainability requirements |
| **Data privacy** | Privacy Policy — full GDPR coverage, data classification |
| **Environmental impact** | Token budget tracking (partial — energy consumption not directly measured) |
| **Homogenization** | Vendor concentration risk tracking, model diversity in fleet configs |
| **Intellectual property** | Content Policy — license compliance, vendor assessment — training data provenance |
| **Obscene content** | AI Governance — RE-3 harmful content risk, content filtering |
| **Value chain risks** | Vendor Risk Management — supply chain assessment, AI vendor extended questions |

## 3. Where Observability Provides Evidence

NIST AI RMF emphasizes **continuous monitoring** (MANAGE 3) and **quantitative measurement** (MEASURE). The observability platform is the implementation mechanism:

| RMF Function | Observability Source | Why It Matters |
|-------------|---------------------|----------------|
| GOVERN — Policy enforcement | CI/CD quality gate traces, `governance.decision` events | Proves policies are enforced at runtime, not just documented |
| MAP — Risk identification | Anomaly detection alerts, automated risk signals | Proves risks are continuously identified, not just mapped once |
| MEASURE — Risk quantification | KRI dashboards (prompt injection rate, tool call failure rate, escalation frequency, hallucination rate) | Proves risks are measured with real data |
| MEASURE — Trustworthiness | Fairness metric dashboards, adversarial test results, explainability traces | Proves trustworthiness characteristics are validated |
| MANAGE — Risk response | `risk.treatment.applied` events, `agent.emergency_halt` events, circuit breaker metrics | Proves risk responses activate when needed |
| MANAGE — Post-deployment | Agent fleet dashboards, SLO burn rates, behavioral drift alerts | Proves AI systems are monitored after deployment |

## 4. Remaining Gaps

| Gap | NIST AI RMF Requirement | What's Needed | Severity |
|-----|------------------------|---------------|----------|
| **Organizational AI risk profile** | MAP 3 | Formal document consolidating all AI risks with organizational context | Medium |
| **Third-party evaluation** | MEASURE 2 | Independent evaluation of AI system trustworthiness | Medium |
| **Stakeholder impact assessment** | MAP 4 | Formal assessment of impacts across affected groups (beyond DPIA) | Medium |
| **Environmental impact tracking** | GOVERN 1 (GenAI Profile) | Energy consumption metrics for AI workloads | Low |
| **Workforce AI competence** | GOVERN 3 | Formal AI competence programme and diversity considerations | Low |

**Addressed by framework:** Quantitative MEASURE scaffolding — see the [quantitative measurement guide](remediation/nist-ai-rmf-measure-metrics.md), [dashboard template](templates/_TEMPLATE-nist-ai-rmf-measure-dashboard.md), and [measurement report template](templates/_TEMPLATE-nist-ai-rmf-measure-report.md). These standardize metric definitions, baseline establishment, dashboard structure, and reporting format; adopters still need live telemetry and completed reports from their running deployment.

## 5. External References

- [NIST AI 100-1 — AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) — The framework itself
- [NIST AI 600-1 — Generative AI Profile](https://airc.nist.gov/Docs/1) — GenAI-specific risks and actions
- [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Playbook) — Suggested actions for each subcategory
- [NIST AI 100-2e2023 — Adversarial Machine Learning Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) — Attack taxonomy
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Security and privacy controls (crosswalk)
- [NIST AI RMF Crosswalk to ISO 42001](https://airc.nist.gov/Docs/Crosswalks) — Official mapping
- [NIST AI RMF Crosswalk to EU AI Act](https://airc.nist.gov/Docs/Crosswalks) — Official mapping
