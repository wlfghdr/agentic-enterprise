# Delivery Policy

> **Applies to:** All deployments, releases, rollouts, and operational changes  
> **Enforced by:** Quality Layer eval agents  
> **Authority:** Release Management / DevOps leads

---

## Principles

1. **Progressive delivery** — Never ship everything at once. Roll out incrementally.
2. **Reversible** — Every deployment must be rollback-capable.
3. **Evidence-based promotion** — Promotion decisions based on data, not hope.
4. **Minimal blast radius** — Limit impact of any single change.

## Mandatory Requirements

### Environment Progression
All changes must progress through isolated environments before reaching production. Each environment serves a distinct validation purpose:

- **Development** — Where code is first deployed and tested by the authoring team
- **Staging** — Pre-production validation under production-like conditions
- **Production** — Customer-facing, reached only after successful staging validation

Promotion between environments requires evidence of health at the current stage. No environment may be skipped except during emergency deployments (see Emergency / Hotfix below).

### Pre-Deployment
- [ ] All quality policy evaluations passed (security, architecture, performance, **observability**)
- [ ] Release contract completed (`work/releases/_TEMPLATE-release-contract.md`)
- [ ] Observability verified: instrumentation active, SLOs configured, dashboard created, alerting with runbooks (see `policies/observability.md`)
- [ ] Rollback plan documented and tested
- [ ] Feature flags configured for new features
- [ ] Database migrations backward-compatible

### Deployment Process
- [ ] Progressive rollout plan defined (e.g., 5% → 25% → 50% → 100%)
- [ ] Health checks defined and monitored at each stage
- [ ] Automatic rollback triggers configured
- [ ] Deployment window communicated to stakeholders
- [ ] No manual steps in the deployment pipeline (fully automated)

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
