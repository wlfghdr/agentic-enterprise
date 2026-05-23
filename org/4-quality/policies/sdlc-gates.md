# SDLC Governance Gates

> **Applies to:** All software, AI system, agent, integration, and operational changes that progress through the delivery lifecycle
> **Enforced by:** Quality Layer eval agents, release coordinators, and human approvers for mandatory gates
> **Authority:** Release Management / DevOps leads, Security & Compliance team
> **Version:** 1.0 | **Last updated:** 2026-05-23

---

## Purpose

This policy provides the single-view SDLC stage-gate map for the governance controls already defined across the quality policy set. It clarifies **which existing requirements become blocking gates at which SDLC phase** so teams can demonstrate delivery readiness against ISO 42001, NIST AI RMF, and internal release governance expectations.

A gate is **blocking** unless the referenced policy explicitly defines an emergency exception path. Referenced policies remain authoritative for detailed control language.

## SDLC Stage-Gate Map

| SDLC Phase | Required blocking gates | Primary evidence / artifacts | Governing policies |
|---|---|---|---|
| **PLAN** | Mission scope defined, autonomy tier identified, initial risk assessment completed, applicable regulatory/compliance obligations identified | Mission brief, technical design draft, initial risk register entries, autonomy classification | [risk-management.md](risk-management.md), [ai-governance.md](ai-governance.md), [architecture.md](architecture.md) |
| **CODE** | Agent/tool scope declared, trust boundaries documented, secure coding and data-handling controls applied, governed integrations registered before use | Agent type definitions, capability contracts, integration registry entries, design notes | [agent-security.md](agent-security.md), [security.md](security.md), [data-classification.md](data-classification.md), [vendor-risk-management.md](vendor-risk-management.md) |
| **BUILD** | CI checks pass, dependency/security scanning passes, governed artifacts pass content security validation, release contract prepared when change is release-bound | CI results, scanner output, release contract draft | [security.md](security.md), [agent-security.md](agent-security.md), [delivery.md](delivery.md) |
| **TEST** | Quality policy evaluations pass, regression/security/eval coverage complete, AI-specific penetration testing completed for applicable AI/agentic changes, observability validation prepared | Test results, eval reports, red-team / penetration test evidence, staging dashboards and alerts | [agent-security.md](agent-security.md), [performance.md](performance.md), [observability.md](observability.md), [experience.md](experience.md), [delivery.md](delivery.md) |
| **DEPLOY** | Release contract complete, rollback plan tested, feature flags configured where applicable, **AI system impact assessment complete for Tier 1/Tier 2 systems before initial production deployment**, **pre-deploy readiness checklist completed**, progressive rollout plan approved, deployment security gates satisfied | Release contract, rollback evidence, feature-flag plan, impact assessment, pre-deploy readiness checklist | [delivery.md](delivery.md), [ai-governance.md](ai-governance.md), [agent-security.md](agent-security.md), [risk-management.md](risk-management.md) |
| **RELEASE** | Customer-facing release notes complete, stakeholder communication complete, approval gates for externally visible or high-impact changes satisfied | Release notes, approvals, communications record | [delivery.md](delivery.md), [customer.md](customer.md), [content.md](content.md) |
| **OPERATE** | Post-deploy validation complete, telemetry flowing, rollback triggers active, incident and support ownership in place | Post-deploy health evidence, dashboards, alerts, runbooks, on-call ownership | [delivery.md](delivery.md), [observability.md](observability.md), [security.md](security.md) |
| **MONITOR** | KRIs/SLOs monitored, incidents and near-misses fed back into risk and governance processes, reassessment triggers honored | Observability evidence, risk signals, retrospectives, updated risk register | [risk-management.md](risk-management.md), [observability.md](observability.md), [ai-governance.md](ai-governance.md) |

## Named Deploy Gates

The following are explicit blocking gates for production deployment unless a referenced policy defines a limited emergency exception:

- **Quality policy pass gate** — Required evaluations for security, architecture, performance, observability, and other applicable policy domains must pass.
- **AI system impact assessment gate** — Tier 1 and Tier 2 AI systems must complete the required impact assessment before initial production deployment.
- **AI-specific penetration testing gate** — Applicable AI and agentic systems must complete prompt injection, tool abuse, output-handling, and related adversarial testing before production deployment.
- **Pre-deploy readiness checklist gate** — A documented readiness review must confirm release contract completion, rollback readiness, observability readiness, security readiness, deployment communication, and ownership for rollback/incident response.
- **Progressive rollout gate** — Production changes must ship through an approved staged rollout with health checks and rollback triggers.

## Minimum Pre-Deploy Readiness Checklist Content

A pre-deploy readiness checklist must confirm at minimum:

- [ ] Release contract is complete and current
- [ ] Required quality policy evaluations passed
- [ ] Security validation and AI-specific penetration testing passed
- [ ] AI system impact assessment completed when required by [ai-governance.md](ai-governance.md)
- [ ] Rollback plan documented and tested
- [ ] Observability ready: instrumentation, SLOs, dashboards, alerts, runbooks
- [ ] Feature flags and blast-radius controls configured where applicable
- [ ] Deployment window and stakeholder communications prepared
- [ ] Named owners available for deployment, rollback, and incident escalation

## Related Policies

- **[delivery.md](delivery.md)** — Detailed deployment and release controls
- **[agent-security.md](agent-security.md)** — Declared tool scope, trust boundaries, AI-specific security testing
- **[ai-governance.md](ai-governance.md)** — AI system impact assessment requirements
- **[risk-management.md](risk-management.md)** — Risk identification, treatment, and reassessment triggers
- **[vendor-risk-management.md](vendor-risk-management.md)** — Third-party and integration assessment requirements

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-05-23 | Initial version. Added explicit SDLC stage-gate mapping, named deploy gates, AI impact assessment deploy gate, AI-specific penetration testing gate, and minimum pre-deploy readiness checklist requirements. |
