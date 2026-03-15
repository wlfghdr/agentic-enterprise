# Postmortem: Onboarding Step 3 UX Regression

> **Incident ID:** INC-2026-003
> **Severity:** SEV3 (Minor)
> **Status:** accepted
> **Date of incident:** 2026-01-15 14:00 UTC
> **Date of resolution:** 2026-03-15 10:00 UTC
> **Author:** Operate Loop agent + Sarah Chen (VP Product)

---

## Incident Summary

A UI redesign of the onboarding workspace configuration step (Step 3), shipped on 2026-01-15, caused the drop-off rate to increase from 18% to 34% over 6 weeks. The regression was not detected for 4 weeks because onboarding funnel monitoring had a 30-day smoothing window that masked the gradual increase. Once detected via a customer-experience agent signal on 2026-03-01, a mission (MISSION-2026-008) was launched to fix the issue. The simplified flow was rolled out on 2026-03-15, reducing drop-off to 16%.

## Timeline

| Time (UTC) | Event |
|-----------|-------|
| 2026-01-15 14:00 | Workspace settings UI redesign deployed (consolidated 12 fields into single form) |
| 2026-01-22 | Drop-off rate begins trending upward — not detected due to 30-day smoothing |
| 2026-02-15 | Drop-off rate reaches 28% — still within smoothed threshold |
| 2026-03-01 09:00 | Customer-experience agent detects 34% drop-off anomaly on daily funnel report |
| 2026-03-01 10:00 | Signal filed: `work/signals/2026-03-01-onboarding-step3-dropoff.md` |
| 2026-03-03 | Mission MISSION-2026-008 created and approved |
| 2026-03-07 | Simplified form + A/B test shipped (PR #89, #91) |
| 2026-03-14 | A/B test results confirm improvement — VP Product approves rollout |
| 2026-03-15 10:00 | Simplified variant rolled out to 100% (PR #95) — drop-off at 16% |

## Impact

### Blast Radius
- **Services affected:** Customer onboarding flow (desktop web)
- **Customers affected:** Estimated 1,200 new customers experienced the degraded Step 3 over 8 weeks
- **Duration:** 59 days (2026-01-15 to 2026-03-15)
- **Service impact:** Step 3 completion rate degraded from 82% to 66%
- **Impact on service health targets:** Onboarding completion SLO (≥75%) was not breached but was trending toward breach

### Business Impact
- **Revenue impact:** Estimated 180 customers did not complete onboarding who otherwise would have (~15% of 1,200)
- **Customer trust impact:** No direct customer complaints — users simply abandoned the flow
- **Data impact:** None — no data loss or corruption

## Detection

- **How was it detected?** Agent detection — customer-experience division agent identified anomaly on daily funnel report
- **Time to detect (TTD):** 28 days from first impact to detection
- **Was the detection method adequate?** No — the 30-day smoothing window on the funnel dashboard masked the gradual regression. A 7-day rolling window or absolute threshold alert would have detected it within 1 week.

## Root Cause Analysis

### Root Cause
The workspace settings UI redesign (PR #67, merged 2026-01-14) consolidated 12 configuration fields into a single form without progressive disclosure. The redesign was focused on visual consistency with the new design system but did not include UX research or A/B testing. The result was a cognitively overwhelming form that caused 16% more users to abandon the step.

### 5 Whys
1. **Why** did the drop-off rate increase? → The new form presented too many fields at once
2. **Why** were too many fields shown? → The redesign was scoped as a visual refresh, not a UX optimization
3. **Why** wasn't UX impact considered? → No UX review checkpoint existed for "visual refresh" PRs
4. **Why** wasn't it detected sooner? → Funnel monitoring used 30-day smoothing that masked gradual changes
5. **Why** was 30-day smoothing used? → It was the default when the dashboard was created; no one had reviewed the alerting thresholds for the onboarding funnel

### Contributing Factors
- No A/B testing requirement for UX changes to onboarding flow
- Missing UX review checkpoint for changes classified as "visual refresh"
- Funnel dashboard smoothing window too long for detecting gradual regressions

## Remediation

### Immediate Actions Taken
- Launched mission MISSION-2026-008 to simplify the form
- Shipped simplified variant with A/B test (PR #89, #91)
- After A/B test validation, rolled out to 100% (PR #95)

### Was a Runbook Used?
- [x] **No** — No runbook existed for UX regression scenarios (onboarding funnel degradation)

## Policy Gap Analysis

| Policy | Gap Identified? | Description |
|--------|----------------|-------------|
| Security | no | No security gap |
| Observability | yes | Funnel dashboard smoothing window was too long; no absolute threshold alert for step completion rate |
| Delivery | yes | "Visual refresh" changes bypass UX review checkpoint; no A/B testing requirement for onboarding UX changes |
| Architecture | no | No architecture gap |

## Follow-Up Items

### Immediate (This Week)

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Reduce funnel dashboard smoothing to 7-day rolling window | SRE team | 2026-03-22 | done |
| Add absolute threshold alert: Step 3 completion < 70% | SRE team | 2026-03-22 | done |

### Short-Term (This Month)

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Add UX review checkpoint for all onboarding flow changes | VP Product | 2026-04-01 | open |
| Require A/B testing for UX changes to onboarding | VP Product | 2026-04-01 | open |

### Long-Term (Requires Mission)

| Action | Signal Filed? | Signal Link |
|--------|--------------|-------------|
| Investigate mobile onboarding drop-off (42% at Step 3) | yes | `work/signals/2026-03-15-mobile-onboarding-dropoff.md` |

## Signals Filed

| Signal ID | Description | Category | Link |
|-----------|-------------|----------|------|
| 2026-03-15-mobile-onboarding-dropoff | Mobile Step 3 has same 42% drop-off pattern | customer | `work/signals/2026-03-15-mobile-onboarding-dropoff.md` |
| 2026-03-20-funnel-alerting-gap | Onboarding funnel monitoring needs shorter windows and absolute thresholds | technical | `work/signals/2026-03-20-funnel-alerting-gap.md` |

## Lessons Learned

### What went well
- Once detected, the signal-to-fix cycle was fast (14 days from signal to full rollout)
- A/B testing validated the fix before full rollout — data-driven decision
- The operating model worked as designed: observe → signal → mission → execute → ship

### What could be improved
- Detection was too slow — 28 days to notice a 16pp regression
- "Visual refresh" changes should not bypass UX review for critical flows
- Funnel dashboards need alerting, not just visualization

### Systemic observations
- This incident demonstrates the value of shifting observability left (Rule 9c). If the original redesign PR had included an observability design section with funnel impact assessment, the risk might have been caught at design time.

## Approval

- [x] On-call engineer reviewed and validated timeline
- [x] Operations Policy Author reviewed policy gap analysis
- [x] All follow-up items assigned and tracked
- [x] Improvement signals filed in `work/signals/`

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | 2026-03-20 | Operate Loop agent | Initial draft |
| 2 | 2026-03-21 | Sarah Chen (VP Product) | Reviewed and accepted |
