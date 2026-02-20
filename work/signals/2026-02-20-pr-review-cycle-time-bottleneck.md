# Signal: PR Review Cycle Time Exceeding SLA — Engineering Capacity Gap

> **Template version:** 1.0 | **Last updated:** 2026-02-19
> **Created:** 2026-02-20
> **Revision:** 1 | **Last updated:** 2026-02-20
> **Author:** observability-platform (automated signal via anomaly detection)

---

## Source

- **Category:** internal
- **Source system:** Observability Platform — DORA Metrics Dashboard
- **Source URL/reference:** `CONFIG.yaml → integrations.observability` (primary-observability platform)
- **Confidence:** high

## Observation

The observability platform detected a sustained degradation in PR review cycle time across the Engineering Foundation and AI & Intelligence divisions over the past 21 days.

**Metrics (P95, rolling 7-day):**

| Week | PR Review Cycle Time P95 | SLA Target | Variance |
|------|--------------------------|------------|---------|
| 2026-W05 | 3.2 days | ≤ 1 day | +220% |
| 2026-W06 | 3.8 days | ≤ 1 day | +280% |
| 2026-W07 | 4.1 days | ≤ 1 day | +310% |

**Additional signals from the same query window:**
- PR queue depth: 47 open PRs awaiting first review (vs. historical baseline of 12)
- Reviewer utilization: 3 active senior reviewers handling a load designed for 5–7
- Mission throughput: the DORA Metrics Excellence mission (`work/missions/dora-metrics-excellence/`) reported a 34% reduction in deployment frequency, attributed to the review backlog
- Downstream impact: the Automated Security Response mission has 6 security patches queued and blocked pending review

**Root cause hypothesis (from platform anomaly classifier):**
Insufficient senior engineering reviewer capacity for current mission load. Not a process issue — reviewer availability is the binding constraint. Two senior engineers left in Q4 2025 and have not been backfilled.

## Initial Assessment

- **Urgency:** immediate
- **Strategic alignment:** `autonomy-maturity` — agentic workflows depend on fast human review loops to maintain the supervised autonomy tier; `trust-is-product` — security patches blocked by review backlog are a trust risk
- **Potential impact:** high — currently blocking security patches and degrading deployment frequency across two active missions
- **Affected divisions:** Engineering Foundation, AI & Intelligence, People (action required)

## Related Signals

- _(No prior signals on this topic — first detection)_

## Recommended Disposition

- [x] Proceed to opportunity validation
- [ ] Defer to next planning cycle
- [ ] Monitor (set follow-up date: YYYY-MM-DD)
- [ ] Archive (not actionable)

## Notes

**Recommended action path:**
1. Steering Layer triages this signal and authorizes a recruiting mission
2. People division (Workforce Planner Agent) validates the headcount gap and produces a hiring plan
3. Orchestration Layer creates a fleet config for the recruiting pipeline
4. Target: 2 senior engineers with strong code review credentials hired within 60 days

**Short-term mitigation (while hiring):**
Engineering Foundation should review whether agent-assisted PR review (Quality Layer eval agents doing a first-pass) can reduce the human review burden on straightforward changes. This would not eliminate the gap but could buy time.

**Note for People division:** This signal is the originating evidence for the headcount recommendation. The workforce planning analysis must cite these metrics when building the business case.

---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | 2026-02-20 | observability-platform | Initial automated signal from anomaly detection |
