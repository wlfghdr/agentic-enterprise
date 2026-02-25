# Ship Loop — Guide

> **What this covers:** How quality-approved outputs get safely deployed to production. The complete Ship loop workflow.

---

## Workflow

### Step 1: Release Contract

When outputs from the Build loop have received PASS verdicts:

1. Compile a release contract using `work/releases/_TEMPLATE-release-contract.md`
2. List all changes included in this release
3. Define progressive rollout stages
4. Document rollback procedures and triggers
5. Prepare customer-facing release notes
6. Submit release contract for human approval

### Step 2: Pre-Deployment Checks

Before deployment begins:
- [ ] All quality evaluations passed
- [ ] Release contract approved by human
- [ ] Rollback plan documented and tested
- [ ] Feature flags configured and tested in staging
- [ ] Database migrations backward-compatible
- [ ] Monitoring dashboards ready
- [ ] On-call team notified

### Step 3: Progressive Deployment

Execute the rollout plan:

```
Stage 1: Internal / Canary ({{CANARY_PERCENTAGE}})
  → Monitor for {{CANARY_DURATION}}
  → Health check: error rate, latency, resource usage
  
Stage 2: Early Adopters ({{EARLY_ADOPTER_PERCENTAGE}})
  → Monitor for {{EARLY_ADOPTER_DURATION}}
  → Health check: + user feedback, feature adoption
  
Stage 3: General Availability ({{GA_PERCENTAGE}})
  → Monitor for {{GA_DURATION}}
  → Health check: + business metrics, customer impact

Stage 4: Full Rollout (100%)
  → Continue monitoring
  → Feature flag cleanup scheduled
```

### Step 4: Post-Deployment Validation

Within the validation window:
- [ ] Error rates within normal bounds
- [ ] Latency within target
- [ ] No critical alerts triggered
- [ ] Smoke tests passing
- [ ] User-facing functionality verified
- [ ] Resource consumption within expected bounds

### Step 5: Outcome Measurement

After the defined measurement period:
1. Collect metrics defined in the outcome contract
2. Compare actuals vs. targets
3. Document what worked and what didn't
4. Generate outcome report

### Step 6: Feedback Loop

Production observations become new signals:
1. Performance improvements needed → signal to `work/signals/`
2. Customer feedback patterns → signal to `work/signals/`
3. Process friction points → signal to `work/signals/`
4. Unexpected behavior → incident signal

---

## Rollback Criteria

Automatic rollback triggers:
- Error rate increases > {{MAX_ERROR_RATE_INCREASE}} above baseline
- p99 latency exceeds 2x target
- Health check failures in > {{MAX_HEALTH_CHECK_FAILURE_RATE}} of instances
- Critical security alert
- Data integrity issue detected

Manual rollback triggers:
- Customer reports of broken functionality
- Business metric degradation
- Regulatory compliance concern

## Emergency / Hotfix Process

For critical production issues:
1. **Assess** — Is this a P1 (customer-impacting) or P0 (service down)?
2. **Fix** — Create hotfix branch, minimal change
3. **Test** — Abbreviated testing (security checks still mandatory)
4. **Deploy** — Expedited deployment (skip non-essential stages)
5. **Validate** — Post-deployment health check (15 min window)
6. **Document** — Post-incident signal in `work/signals/`

## Exit Criteria / Handoff to Operate

Before a release transitions from Ship to Operate, **all** of the following must be true:

### Required Artifacts
- [ ] Release contract exists and is approved (`work/releases/YYYY-MM-DD-<release>.md`)
- [ ] Progressive deployment completed through all stages (canary → GA → full rollout)
- [ ] Post-deployment validation passed (error rates, latency, smoke tests)
- [ ] Outcome contract has `measurement_schedule` dates filled in (`work/missions/<name>/OUTCOME-CONTRACT.md`)
- [ ] Runbook exists for the deployed service/feature (if applicable)

### Quality Gates Passed
- [ ] Error rates within normal bounds after full rollout
- [ ] No critical alerts triggered during validation window
- [ ] Latency within target for all affected endpoints
- [ ] Smoke tests and user-facing functionality verified

### Ownership Transfer
- [ ] **Ship owner:** Orchestration Layer (release complete from their perspective)
- [ ] **Operate owner:** Quality Layer (takes over for outcome measurement, production signaling, and stall detection)
- [ ] Quality Layer has the `measurement_schedule` dates and will trigger outcome reports at each checkpoint
- [ ] On-call team is aware of the new deployment and has access to rollback procedures
- [ ] `STATUS.md` updated to reflect that the mission is in the Operate/measurement phase

> **Gate enforcer:** The Orchestration Layer verifies this checklist before declaring the release complete. The Quality Layer begins the Operate loop once the handoff is confirmed.

## Anti-Patterns

- ❌ Big-bang deployments (no progressive rollout)
- ❌ Deployments without rollback capability
- ❌ Skipping post-deployment validation
- ❌ Not measuring outcomes (deploy and forget)
- ❌ Emergency deploys without post-incident signals
- ❌ Feature flags left forever (schedule cleanup)
