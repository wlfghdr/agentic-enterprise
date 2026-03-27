# Compliance Reference Index

> **Purpose:** Central mapping of external standards to framework policies, controls, and adopter responsibilities.
> **Audience:** Auditors, compliance officers, adopters assessing certification readiness.

This directory contains one reference document per external standard or regulation that the Agentic Enterprise framework maps to. Each document explains:

1. **What the standard requires** — key clauses and control objectives
2. **How this framework addresses it** — specific policies, controls, and mechanisms
3. **Where observability fits** — how telemetry provides runtime evidence
4. **What adopters must provide** — deployment-specific requirements beyond the framework's scope

## Standards Covered

| Standard | Document | Self-Assessed Template Posture | Adopter Responsibilities |
|----------|----------|-------------------|----------|
| [ISO/IEC 27001:2022](iso-27001.md) | Information Security Management | ~90% | Management review records, competence records |
| [SOC 2 Type II](soc2.md) | Trust Service Criteria | ~90% | Independent audit |
| [GDPR](gdpr.md) | EU Data Protection | ~75% | Consent management UX, DPO appointment, supervisory authority registration, cookie/tracking compliance |
| [ISO/IEC 42001:2023](iso-42001.md) | AI Management Systems | ~85% | Conformity assessment, management review, internal audit programme |
| [NIST AI RMF](nist-ai-rmf.md) | AI Risk Management Framework | ~90% | Third-party evaluation, organizational AI risk profile document, stakeholder impact assessment |
| [EU AI Act](eu-ai-act.md) | European AI Regulation | ~85% | Post-market monitoring system, serious incident reporting |
| [NIST CSF 2.0](nist-csf.md) | Cybersecurity Framework | ~95% | IdP integration, physical security controls |
| [ISO 9001:2015](iso-9001.md) | Quality Management Systems | ~85% | Populate QMS reviews, customer measurement, and supplier quality scorecards |
| [ISO 22301:2019](iso-22301.md) | Business Continuity Management | ~70% | BIA template, documented BC plans, BCMS scope statement, exercise programme |
| [CCPA/CPRA](ccpa-cpra.md) | California Consumer Privacy | ~75% | "Do Not Sell/Share" opt-out, sensitive PI handling, annual cybersecurity audit |
| [HIPAA](hipaa.md) | US Health Information Privacy & Security | ~70% | BAA template, PHI classification, NPP template, Privacy/Security Officer designation, workforce training |

## Important Disclaimer

**These documents describe governance scaffolding, not certification status.** The framework provides policy surfaces, control structures, and observability patterns. Actual certification requires:

- A running deployment with real operational evidence
- Independent third-party audit (ISO/SOC 2) or self-assessment with documentation (GDPR/EU AI Act)
- Deployment-specific configuration (retention periods, encryption keys, access controls, DPO appointment, etc.)
- Continuous evidence collection via the observability platform

**Method note:** the percentages in this index, `README.md`, and `index.html` are editorial posture markers for the template. They are not produced by `scripts/validate_compliance_coverage.py`. That validator currently measures a narrower and stricter signal: how completely the policy Compliance Mapping tables link back to the documented clauses/articles/controls in these reference docs. Today, that validator reports materially lower machine-verifiable coverage than the top-level posture snapshot, so leadership should treat the validator output as the better source for concrete gap-closing work.

## How Observability Provides Audit Evidence

A recurring theme across all standards: **governance documents alone are insufficient — auditors need runtime evidence.** The framework's observability architecture (see [otel-contract.md](../otel-contract.md) and [observability policy](../../org/4-quality/policies/observability.md)) is designed to produce this evidence:

- **Audit trails** — Every agent action produces an OpenTelemetry span with governance decision events
- **Access logs** — Tool calls, data access, and authentication events are traced
- **Change evidence** — Git history + PR-based governance provides tamper-evident change records
- **SLA/SLO proof** — Health targets, error budgets, and incident response times are measured and dashboarded
- **Compliance dashboards** — Observability platform surfaces policy compliance metrics in real time

Without a configured observability platform, the framework's compliance claims remain theoretical. With one, they become provable.

## Implementation Guides

For certification-critical requirements that need deployment-specific implementation, actionable guides are available in the [guides/](guides/) directory. These guides provide step-by-step instructions for adopters deploying the framework in real environments. For template hardening, prefer shipping one more concrete guide or template over inflating the posture percentages.

## Related Resources

- [Quality Policies](../../org/4-quality/policies/) — The 19 policy domains that implement these controls
- [otel-contract.md](../otel-contract.md) — Canonical telemetry contract for agent spans and events
- [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — Framework crosswalk to all standards
- [Autonomy Tier Rollout Checklist](templates/_TEMPLATE-autonomy-tier-rollout-checklist.md) — adopter-facing checklist for ownership, readiness, monitoring, rollback, and communication before raising autonomy
- [CONFIG.yaml](../../CONFIG.yaml) — Central configuration including observability integration
