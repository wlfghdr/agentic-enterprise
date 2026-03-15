# Compliance Reference Index

> **Purpose:** Central mapping of external standards to framework policies, controls, and remaining gaps.
> **Audience:** Auditors, compliance officers, adopters assessing certification readiness.

This directory contains one reference document per external standard or regulation that the Agentic Enterprise framework maps to. Each document explains:

1. **What the standard requires** — key clauses and control objectives
2. **How this framework addresses it** — specific policies, controls, and mechanisms
3. **Where observability fits** — how telemetry provides runtime evidence
4. **What remains open** — honest assessment of gaps that require deployment-specific work

## Standards Covered

| Standard | Document | Framework Coverage | Key Gaps |
|----------|----------|-------------------|----------|
| [ISO/IEC 27001:2022](iso-27001.md) | Information Security Management | ~90% | Management review records, competence records |
| [SOC 2 Type II](soc2.md) | Trust Service Criteria | ~90% | Independent audit |
| [GDPR](gdpr.md) | EU Data Protection | ~75% | Consent management UX, DPO appointment, supervisory authority registration, cookie/tracking compliance |
| [ISO/IEC 42001:2023](iso-42001.md) | AI Management Systems | ~85% | Conformity assessment, management review, internal audit programme |
| [NIST AI RMF](nist-ai-rmf.md) | AI Risk Management Framework | ~90% | Third-party evaluation, organizational AI risk profile document, stakeholder impact assessment |
| [EU AI Act](eu-ai-act.md) | European AI Regulation | ~85% | Post-market monitoring system, serious incident reporting |
| [NIST CSF 2.0](nist-csf.md) | Cybersecurity Framework | ~95% | IdP integration, physical security controls |
| [ISO 9001:2015](iso-9001.md) | Quality Management Systems | ~85% | Formal QMS scope statement, customer satisfaction measurement, external provider evaluation |
| [ISO 22301:2019](iso-22301.md) | Business Continuity Management | ~70% | BIA template, documented BC plans, BCMS scope statement, exercise programme |
| [CCPA/CPRA](ccpa-cpra.md) | California Consumer Privacy | ~75% | "Do Not Sell/Share" opt-out, sensitive PI handling, annual cybersecurity audit |
| [HIPAA](hipaa.md) | US Health Information Privacy & Security | ~70% | BAA template, PHI classification, NPP template, Privacy/Security Officer designation, workforce training |

## Important Disclaimer

**These documents describe governance scaffolding, not certification status.** The framework provides policy surfaces, control structures, and observability patterns. Actual certification requires:

- A running deployment with real operational evidence
- Independent third-party audit (ISO/SOC 2) or self-assessment with documentation (GDPR/EU AI Act)
- Deployment-specific configuration (retention periods, encryption keys, access controls, DPO appointment, etc.)
- Continuous evidence collection via the observability platform

## How Observability Closes the Evidence Gap

A recurring theme across all standards: **governance documents alone are insufficient — auditors need runtime evidence.** The framework's observability architecture (see [otel-contract.md](../otel-contract.md) and [observability policy](../../org/4-quality/policies/observability.md)) is designed to produce this evidence:

- **Audit trails** — Every agent action produces an OpenTelemetry span with governance decision events
- **Access logs** — Tool calls, data access, and authentication events are traced
- **Change evidence** — Git history + PR-based governance provides tamper-evident change records
- **SLA/SLO proof** — Health targets, error budgets, and incident response times are measured and dashboarded
- **Compliance dashboards** — Observability platform surfaces policy compliance metrics in real time

Without a configured observability platform, the framework's compliance claims remain theoretical. With one, they become provable.

## Remediation Guides

For **P0-critical gaps** that block certification audits, actionable remediation guides are available in the [remediation/](remediation/) directory. These guides provide step-by-step instructions for adopters deploying the framework in real environments.

## Related Resources

- [Quality Policies](../../org/4-quality/policies/) — The 19 policy domains that implement these controls
- [otel-contract.md](../otel-contract.md) — Canonical telemetry contract for agent spans and events
- [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — Framework crosswalk to all standards
- [CONFIG.yaml](../../CONFIG.yaml) — Central configuration including observability integration
