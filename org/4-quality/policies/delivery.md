# Delivery Policy

> **Applies to:** All deployments, releases, rollouts, and operational changes
> **Enforced by:** Quality Layer eval agents
> **Authority:** Release Management / DevOps leads
> **Version:** 1.2 | **Last updated:** 2026-06-09

---

## Principles

1. **Progressive delivery** — Never ship everything at once. Roll out incrementally.
2. **Reversible** — Every deployment must be rollback-capable.
3. **Evidence-based promotion** — Promotion decisions based on data, not hope.
4. **Minimal blast radius** — Limit impact of any single change.

## Mandatory Requirements

For the cross-policy stage view of blocking governance requirements, see [sdlc-gates.md](sdlc-gates.md). This policy defines the deployment and release-specific gates within that SDLC map.

### Environment Progression
All changes must progress through isolated environments before reaching production. Each environment serves a distinct validation purpose:

- **Development** — Where code is first deployed and tested by the authoring team
- **Staging** — Pre-production validation under production-like conditions
- **Production** — Customer-facing, reached only after successful staging validation

Promotion between environments requires evidence of health at the current stage. No environment may be skipped except during emergency deployments (see Emergency / Hotfix below).

### Pre-Deployment
- [ ] All quality policy evaluations passed (security, architecture, performance, **observability**, and other applicable quality domains)
- [ ] Release contract completed (`work/releases/_TEMPLATE-release-contract.md`)
- [ ] Pre-deploy readiness checklist completed and approved
- [ ] Observability verified: instrumentation active, SLOs configured, dashboard created, alerting with runbooks (see `policies/observability.md`)
- [ ] Rollback plan documented and tested
- [ ] Feature flags configured for new features
- [ ] Database migrations backward-compatible
- [ ] AI system impact assessment completed before initial production deployment for Tier 1 and Tier 2 systems, per `ai-governance.md`
- [ ] AI-specific penetration testing completed for applicable AI and agentic systems (prompt injection, tool abuse, output-handling, and related adversarial scenarios), per `agent-security.md`

### Deployment Process
- [ ] Progressive rollout plan defined (e.g., 5% → 25% → 50% → 100%)
- [ ] Health checks defined and monitored at each stage
- [ ] Automatic rollback triggers configured
- [ ] Deployment window communicated to stakeholders
- [ ] No manual steps in the deployment pipeline (fully automated)

### Pre-Deploy Readiness Checklist
A documented pre-deploy readiness checklist is a **blocking deploy gate** for production changes. At minimum, it must confirm:

- [ ] Release contract is complete and current
- [ ] Required quality policy evaluations passed
- [ ] Security validation and AI-specific penetration testing passed
- [ ] AI system impact assessment completed when required by `ai-governance.md`
- [ ] Rollback plan documented and tested
- [ ] Observability ready: instrumentation, SLOs, dashboards, alerts, runbooks
- [ ] Feature flags and blast-radius controls configured where applicable
- [ ] Deployment window and stakeholder communications prepared
- [ ] Named owners available for deployment, rollback, and incident escalation

### Post-Deployment
- [ ] Health metrics validated within {{POST_DEPLOY_VALIDATION_WINDOW}} of deployment
- [ ] Error rate within acceptable bounds
- [ ] Performance metrics within target
- [ ] Telemetry verified: traces, metrics, and logs flowing correctly after deployment
- [ ] Health target burn rate monitored during rollout
- [ ] Customer-facing functionality verified (smoke tests)
- [ ] Deployment recorded in change log

### Rollback Criteria
Automatic rollback if any of:
- Error rate increases > {{MAX_ERROR_RATE_INCREASE}} above baseline
- p99 latency exceeds target
- Health check failures
- Critical alert triggered

### Release Notes
- [ ] Customer-facing release notes written
- [ ] Changes categorized (new feature, improvement, fix, deprecation)
- [ ] Breaking changes clearly highlighted
- [ ] Migration instructions provided if applicable

### Emergency / Hotfix Deployments
When an active production incident requires an immediate fix:

- Non-critical validation stages may be compressed or skipped (direct to target environment)
- **Security checks are never skippable** — all security policy requirements remain mandatory
- A rollback plan must be documented before deploying the fix
- Post-deployment health evidence must be provided within {{POST_DEPLOY_VALIDATION_WINDOW}}
- A post-incident signal must be filed in `work/signals/` after resolution
- Follow-up work to backfill any skipped validation must be tracked as a new mission
- Any temporarily compressed pre-deploy readiness evidence, impact assessment updates, or penetration-testing follow-up must be explicitly tracked and completed after incident stabilization

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Environment progression | Changes validated in each environment before promotion | Environments skipped without emergency justification |
| Progressive rollout | Defined plan with stages | Big-bang deployment |
| Rollback plan | Documented and tested | No rollback capability |
| Feature flags | New features flagged | Hard-coded feature delivery |
| Post-deploy validation | Evidence within window | No validation evidence |
| Release notes | Customer-ready | Missing or internal-only |
| Emergency deployment | Security checks maintained, post-incident signal filed | Security bypassed or no follow-up |
| AI impact assessment gate | Required Tier 1/Tier 2 impact assessment completed before initial production deployment | Required impact assessment missing or deferred without policy-defined exception |
| AI penetration testing gate | Applicable AI and agentic systems completed adversarial / penetration testing before production deployment | No named AI-specific penetration-testing evidence |
| Pre-deploy readiness checklist | Documented checklist completed with named owners and rollback/observability readiness | No readiness checklist or incomplete blocking evidence |

---

## Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|----------------|
| **SOC 2** | CC8.1 Change management | Environment Progression; Pre-Deployment; Deployment Process |
| **SOC 2** | A1.3 Recovery testing | Rollback Criteria; Post-Deployment |
| **ISO 22301:2019** | 8.3 Business continuity strategies and solutions | Deployment Process; Rollback Criteria |
| **ISO 22301:2019** | 8.4 Business continuity plans and procedures | Pre-Deploy Readiness Checklist; Rollback Criteria |
| **ISO 22301:2019** | 8.5 Exercise programme | Environment Progression; Post-Deployment |
| **ISO 9001:2015** | 8.5 Production and service provision | Deployment Process |
| **ISO 9001:2015** | 8.6 Release of products and services | Pre-Deployment; Pre-Deploy Readiness Checklist |
| **ISO 9001:2015** | 8.7 Control of nonconforming outputs | Rollback Criteria; Emergency / Hotfix Deployments |
| **NIST CSF 2.0** | PR.IR-03 Mechanisms are implemented to achieve resilience requirements | Progressive rollout; Rollback Criteria |
| **NIST CSF 2.0** | RC.RP-03 Recovery actions and restoration are verified | Post-Deployment; Rollback Criteria |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-06-09 | Added structured compliance mappings for governed change, continuity, release control, and recovery verification. |
| 1.1 | 2026-05-23 | Added SDLC gate cross-reference, formal AI impact assessment deploy gate, AI-specific penetration-testing deploy gate, and pre-deploy readiness checklist as a blocking production gate. |
| 1.0 | 2026-02-19 | Initial version |
