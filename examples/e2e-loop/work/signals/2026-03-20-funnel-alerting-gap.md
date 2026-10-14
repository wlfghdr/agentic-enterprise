# Signal: Onboarding Funnel Monitoring Needs Shorter Windows and Absolute Thresholds

> **Created:** 2026-03-20
> **Author:** Agent (operate-loop)

---

## Source

- **Category:** technical
- **Source system:** Postmortem analysis (INC-2026-003)
- **Source URL/reference:** `work/retrospectives/2026-03-20-onboarding-step3-regression.md`
- **Confidence:** high

## Observation

The onboarding Step 3 regression (INC-2026-003) went undetected for 28 days because the funnel monitoring dashboard used a 30-day smoothing window that masked the gradual increase in drop-off rate. The immediate fix (7-day rolling window + absolute threshold alert at 70%) has been applied to Step 3, but the same gap likely exists across all onboarding funnel steps and other critical user journey dashboards.

Key findings from the postmortem:
- 30-day smoothing was the default when the dashboard was created — never reviewed
- No absolute threshold alerts existed for any onboarding step completion rate
- The pattern may repeat for other critical funnels (activation, retention, upgrade)

## Initial Assessment

- **Urgency:** next-cycle
- **Strategic alignment:** "Observability is a design-time discipline" (AGENTS.md Rule 9c)
- **Potential impact:** medium
- **Affected divisions:** platform-infrastructure, quality-security-engineering

## Related Signals

- Root cause from: `work/signals/2026-03-01-onboarding-step3-dropoff.md`

## Recommended Disposition

- [ ] Proceed to opportunity validation
- [ ] Defer to next planning cycle
- [x] Monitor (set follow-up date: 2026-04-15)
- [ ] Archive

## Notes

The immediate fixes for Step 3 are done (retro follow-up items, status: done). This signal tracks the broader systemic issue: auditing all critical funnel dashboards for the same 30-day smoothing gap. Monitoring disposition because the SRE team is already aware and assessing scope — a mission may be proposed if the audit reveals widespread gaps.
