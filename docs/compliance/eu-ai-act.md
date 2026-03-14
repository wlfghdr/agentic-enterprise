# EU AI Act — Compliance Reference

> **Regulation:** Regulation (EU) 2024/1689 — Artificial Intelligence Act
> **Scope:** AI systems placed on the market or put into service in the EU
> **Official source:** [EUR-Lex — EU AI Act Full Text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
> **Application timeline:** Prohibitions from Feb 2025, high-risk obligations from Aug 2026, full application from Aug 2027

## 1. What the EU AI Act Requires

The EU AI Act establishes a risk-based regulatory framework:

### Risk Categories

| Category | Examples | Key Obligations |
|----------|----------|-----------------|
| **Prohibited** (Art. 5) | Social scoring, real-time biometric identification (exceptions), subliminal manipulation, exploitation of vulnerabilities | Must not be developed, placed on market, or used |
| **High-risk** (Art. 6, Annex III) | Hiring/recruitment, credit scoring, law enforcement, migration, critical infrastructure, education | Full compliance: risk management, data governance, transparency, human oversight, accuracy/robustness, logging, conformity assessment |
| **Limited-risk** (Art. 50) | Chatbots, deepfakes, emotion recognition | Transparency obligations (disclosure of AI interaction) |
| **Minimal-risk** (Art. 52) | Spam filters, AI-enabled games | No specific obligations (voluntary codes of conduct encouraged) |

### Key Obligations for High-Risk AI Systems

| Article | Obligation | Detail |
|---------|-----------|--------|
| Art. 9 | Risk management system | Continuous, iterative risk management throughout AI lifecycle |
| Art. 10 | Data governance | Training/validation/test data quality, relevance, representativeness, bias examination |
| Art. 11 | Technical documentation | Before placing on market — purpose, design, development, testing, performance |
| Art. 12 | Record-keeping (logging) | Automatic recording of events throughout lifecycle, traceability |
| Art. 13 | Transparency | Understandable instructions for use, limitations, intended purpose |
| Art. 14 | Human oversight | Designed for effective human oversight, ability to override/interrupt |
| Art. 15 | Accuracy, robustness, cybersecurity | Appropriate levels throughout lifecycle, resilience to errors/attacks |
| Art. 16–22 | Provider obligations | Conformity assessment, CE marking, EU database registration, post-market monitoring |
| Art. 26–28 | Deployer obligations | Use in accordance with instructions, monitor, inform provider of risks |

### General-Purpose AI (GPAI) Models (Art. 51–56)

| Obligation | Applies to |
|-----------|-----------|
| Technical documentation | All GPAI models |
| Transparency (copyright compliance, model capabilities) | All GPAI models |
| Systemic risk evaluation | GPAI with systemic risk (>10^25 FLOPs or equivalent) |
| Adversarial testing | GPAI with systemic risk |
| Incident reporting | GPAI with systemic risk |

## 2. How This Framework Addresses It

### Article-Level Mapping

| Article | Requirement | Framework Implementation | Evidence Source |
|---------|-------------|-------------------------|-----------------|
| **Art. 5** | Prohibited practices | [AI Governance Policy](../../org/4-quality/policies/ai-governance.md) §1 — Tier 0 prohibited (social scoring, real-time biometrics, manipulative AI) | Risk tier assignments in agent type registry |
| **Art. 6** | High-risk classification | AI Governance Policy §1 — 4-tier risk classification aligned to EU AI Act, every agent type documents risk tier | Agent type definitions |
| **Art. 9** | Risk management | [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — continuous risk management, AI risk taxonomy, 7 KRIs, circuit breakers | Risk register, KRI dashboards, `risk.assessment.complete` events |
| **Art. 10** | Data governance | [Data Classification Policy](../../org/4-quality/policies/data-classification.md), [Privacy Policy](../../org/4-quality/policies/privacy.md), AI vendor assessment — training data provenance | PII inventory, data classification records |
| **Art. 11** | Technical documentation | Model cards in agent type definitions (purpose, model selection, performance, limitations, fairness, adversarial robustness) | Model card artifacts in `org/agents/` |
| **Art. 12** | Record-keeping | [Log Retention Policy](../../org/4-quality/policies/log-retention.md), [Observability Policy](../../org/4-quality/policies/observability.md) — all agent actions produce OTel spans, WORM for audit logs | Full OTel telemetry pipeline, WORM verification |
| **Art. 13** | Transparency | Versioned agent instructions (AGENT.md), explainability levels (Traceable/Justifiable/Auditable), model cards | Agent instruction history, explainability traces |
| **Art. 14** | Human oversight | AGENTS.md Rule 2 ("Humans decide, agents recommend"), human approval gates, kill switch, escalation mechanisms | `governance.decision` events, human override logs, escalation metrics |
| **Art. 15** | Accuracy, robustness | AI Governance Policy §4 — adversarial testing (prompt injection, persona manipulation, boundary probing), [Agent Security Policy](../../org/4-quality/policies/agent-security.md) — OWASP LLM Top 10 | Test results, prompt injection rate metrics |
| **Art. 26–28** | Deployer obligations | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — AI vendor extended assessment, model version tracking, use-in-accordance monitoring | Vendor assessment records, usage monitoring |
| **Art. 50** | Transparency (limited-risk) | AI Governance §1 Tier 2 — output labeling ("generated by AI"), model card | Disclosure records |

## 3. Where Observability Provides Evidence

The EU AI Act explicitly requires **logging** (Art. 12) and **post-market monitoring** (Art. 72). The observability platform directly fulfills these:

| EU AI Act Requirement | Observability Source | Why It Matters |
|----------------------|---------------------|----------------|
| Record-keeping (Art. 12) | All agent actions as OTel spans — `agent.run`, `inference.*`, `tool.execute`, `governance.decision` | Direct fulfillment of automatic logging obligation |
| Post-market monitoring (Art. 72) | Continuous agent fleet dashboards, SLO monitoring, anomaly detection | Proves ongoing monitoring after deployment |
| Risk management (Art. 9) | KRI dashboards, `risk.threshold.breach` events, automated risk signals | Proves risk management is continuous, not point-in-time |
| Human oversight (Art. 14) | Human override rate metrics, escalation frequency dashboards | Proves human oversight is meaningful, not rubber-stamp |
| Accuracy monitoring (Art. 15) | Error rate metrics, hallucination/correction rate, fairness dashboards | Proves accuracy is maintained post-deployment |
| Incident detection | Anomaly detection alerts, security test results | Supports incident reporting obligations (Art. 62) |

## 4. Remaining Gaps

| Gap | EU AI Act Requirement | What's Needed | Severity |
|-----|----------------------|---------------|----------|
| **Conformity assessment** | Art. 43 | Third-party conformity assessment for high-risk AI in Annex III areas | Critical — legal requirement before placing on EU market |
| **CE marking** | Art. 48 | Affixed after successful conformity assessment | Critical — cannot market without it |
| **EU database registration** | Art. 49, 71 | Registration in EU AI database before placing on market | Critical — legal requirement |
| **Post-market monitoring system** | Art. 72 | Formal, documented system (partially addressed by observability) | High — requires specific procedures beyond monitoring |
| **Serious incident reporting** | Art. 62 | Reporting to national market surveillance authorities | High — must be operational |
| **Quality management system** | Art. 17 | Formal QMS documentation (partially addressed by quality policies) | Medium — may need ISO 9001-style documentation |
| **Instructions for use** | Art. 13(3) | Formal user-facing documentation for deployers | Medium |
| **Fundamental rights impact assessment** | Art. 27 | Required for deployers of certain high-risk systems (public bodies, private entities in specific sectors) | Medium — deployer obligation |
| **EU representative** | Art. 22 | If provider is outside EU | Low — context-dependent |

## 5. External References

- [EU AI Act Full Text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — Official regulation
- [EU AI Act Corrigendum](https://eur-lex.europa.eu/eli/reg/2024/1689/corr/2024-08-01) — Corrections
- [European Commission AI Act Q&A](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — Official guidance
- [EU AI Act Explorer](https://artificialintelligenceact.eu/) — Navigable text with annotations
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office) — Enforcement body
- [Harmonised Standards under EU AI Act](https://single-market-economy.ec.europa.eu/single-market/european-standards_en) — Technical standards (in development)
- [NIST AI RMF Crosswalk to EU AI Act](https://airc.nist.gov/Docs/Crosswalks) — Official crosswalk
- [ISO/IEC 42001 to EU AI Act Mapping](https://www.iso.org/standard/81230.html) — Standard alignment
- [High-Level Expert Group Ethics Guidelines for Trustworthy AI](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-artificial-intelligence) — Foundational principles
