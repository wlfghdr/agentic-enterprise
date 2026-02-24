# Outcome Report: [Mission Name]

> **Template version:** 1.1 | **Last updated:** 2026-02-24  
> **Mission:** [link to `work/missions/<name>/BRIEF.md`]  
> **Outcome Contract:** [link to `work/missions/<name>/OUTCOME-CONTRACT.md`]  
> **Status:** draft | reviewed | accepted  
> **Date:** YYYY-MM-DD  
> **Author:** [Ship Loop agent + Strategy Layer Outcome Owner]  
> **Storage:** `work/missions/<mission-name>/OUTCOME-REPORT.md`

---

## Mission Summary

[One paragraph: what this mission set out to achieve and what it delivered]

## Outcome Measurement

### Targets vs. Actuals

| Metric | Target | Actual | Variance | Verdict |
|--------|--------|--------|----------|---------|
| [Primary metric from outcome contract] | [target value] | [measured value] | [+/- %] | met / partially-met / not-met |
| [Secondary metric] | [target value] | [measured value] | [+/- %] | met / partially-met / not-met |
| [Guardrail metric] | [threshold] | [measured value] | [within / exceeded] | met / not-met |

### Measurement Methodology
- **Data sources:** [Where the measurements came from]
- **Measurement period:** [Start date → end date]
- **Confidence level:** [high / medium / low — and why]

### Overall Outcome Verdict

- [ ] **Met** — All primary metrics achieved, guardrails held
- [ ] **Partially Met** — Some metrics achieved, others missed
- [ ] **Not Met** — Primary metrics missed
- [ ] **Exceeded** — Metrics significantly surpassed targets

## Delivered Assets

| Asset | Type | Registry Entry | Status |
|-------|------|---------------|--------|
| [Asset name] | code / documentation / content / service | [link to `work/assets/<name>.md`] | deployed / published |
| [Asset name] | code / documentation / content / service | [link to `work/assets/<name>.md`] | deployed / published |

## Task Completion

> Source: `work/missions/<mission-name>/TASKS.md`

| Metric | Value |
|--------|-------|
| Total tasks | [count] |
| Completed | [count] |
| Descoped (with rationale) | [count] |
| Incomplete | [count] |

**Task completion verdict:**
- [ ] **All tasks completed** — every task in TASKS.md reached `completed` status
- [ ] **Completed with descoped tasks** — some tasks were explicitly descoped (rationale documented in TASKS.md)
- [ ] **Incomplete** — tasks remain open; document reason and follow-up plan below

**Incomplete/descoped task details (if any):**

| Task ID | Summary | Final Status | Rationale / Follow-up |
|---------|---------|-------------|----------------------|
| [TASK-NNN] | [brief] | descoped / incomplete | [why, and what happens next] |

## Quality Summary

| Evaluation | Date | Verdict | Link |
|-----------|------|---------|------|
| [Pre-ship quality eval] | YYYY-MM-DD | PASS / FAIL | [link to evaluation report] |
| [Post-deploy validation] | YYYY-MM-DD | PASS / FAIL | [link to evaluation report] |

## Variance Analysis

[For any metric where actual ≠ target, explain why:]

### What worked well
- [Factor that contributed to success]

### What didn't work as expected
- [Factor that caused variance — with evidence]

### External factors
- [Market changes, dependency delays, requirement shifts that affected outcomes]

## Lessons Learned

### Process Improvements
- [What would we do differently next time?]

### Policy Observations
- [Were any quality policies too tight/loose? Should they be updated?]

### Agent Fleet Observations
- [How did the agent fleet perform? Any capability gaps identified?]

## Generated Signals

| Signal | Category | Filed As |
|--------|----------|----------|
| [Signal description] | [technical / market / process / agent] | [link to `work/signals/<signal>.md`] |

## Venture Impact

| Venture | Success Metric Affected | Impact |
|---------|------------------------|--------|
| [Venture name] | [Which venture metric this mission moved] | [Quantified impact, e.g., "+5% to adoption target"] |

## Recommendation

- [ ] **Close mission** — Objectives achieved, no follow-up needed
- [ ] **Follow-up mission** — New mission recommended to address remaining gaps
- [ ] **Pivot** — Strategy adjustment recommended based on learnings
- [ ] **Extend** — Mission should continue with adjusted targets

## Approval

- [ ] Outcome Owner reviewed and accepted measurements
- [ ] Strategy Layer acknowledged venture impact
- [ ] Mission status updated to `completed` in `work/missions/`
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-02-24 | Added Task Completion section with completion metrics, verdict, and descoped/incomplete task detail |
| 1.0 | 2026-02-19 | Initial version |
