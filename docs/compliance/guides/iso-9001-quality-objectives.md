<!-- placeholder-ok -->
# ISO 9001 — Quality Objectives Guide

> **Implements:** Documented quality objectives at relevant functions and levels (clause 6.2)
> **Standard:** ISO 9001:2015 — Quality Management Systems
> **Severity:** Medium — required for certification and operational focus
> **Related compliance doc:** [ISO 9001 Compliance Reference](../iso-9001.md)

---

## 1. Purpose

ISO 9001 requires quality objectives to be established at relevant functions,
levels, and processes. In the framework, many objectives already exist implicitly
inside mission briefs, venture metrics, SLOs, and quality thresholds. This guide
turns those distributed goals into an explicit QMS objectives register.

The register is the control that proves quality intent is measurable, owned,
reviewed, and updated.

---

## 2. What ISO 9001 Requires

Quality objectives must be:

- consistent with the quality policy
- measurable where practicable
- monitored
- communicated
- updated as appropriate
- supported by plans describing what will be done, by whom, by when, and how results are evaluated

---

## 3. Objective Register Pattern

Instantiate a controlled register such as `docs/compliance/qms-quality-objectives.md`.

```markdown
# QMS Quality Objectives Register

> **Effective date:** {{YYYY-MM-DD}}
> **Owner:** {{QMS_OWNER}}
> **Review cadence:** {{monthly / quarterly}}
> **Linked scope:** {{LINK_TO_QMS_SCOPE}}

| Objective ID | Level | Objective | Metric / method | Baseline | Target | Owner | Review cadence | Evidence source | Status |
|--------------|-------|-----------|-----------------|----------|--------|-------|----------------|-----------------|--------|
| QO-001 | Company | {{OBJECTIVE}} | {{METRIC}} | {{BASELINE}} | {{TARGET}} | {{OWNER}} | Quarterly | {{DASHBOARD / REPORT}} | Active |
```

Suggested `Level` values:

- Company
- Layer
- Division
- Process
- Product / service

---

## 4. Good Objective Categories For This Framework

| Category | Example Objective | Typical Evidence |
|----------|-------------------|------------------|
| Delivery quality | Reduce failed quality evaluations on shipped outputs | Quality evaluation trend reports |
| Process performance | Improve signal-to-mission and mission-to-ship cycle time | Workflow and mission dashboards |
| Customer outcomes | Increase customer satisfaction or reduce complaint recurrence | Survey results, support analytics |
| Reliability | Maintain service within SLO and incident targets | Observability dashboards, incident metrics |
| Supplier quality | Reduce vendor-caused quality escapes or SLA/quality exceptions | Vendor review scorecards |
| Improvement discipline | Close corrective actions within agreed SLA | Postmortem and action tracker |

Avoid objectives that are only activity counts with no quality meaning.

---

## 5. Planning Each Objective

For every objective, document:

| Planning Element | Example |
|------------------|---------|
| What will be done | Introduce release checklist for customer-facing docs |
| Resources required | Quality reviewer time, CI checks, dashboard support |
| Owner | Named function or individual |
| Due / review date | End of quarter |
| Evaluation method | Dashboard threshold, audit sample, survey result |

If an objective has no owner or evidence source, it is a slogan, not a control.

---

## 6. Recommended Minimum Starter Set

For a serious template adopter, a useful starting register usually includes at least:

- one customer-perception objective
- one delivery/process objective
- one reliability or nonconformity objective
- one supplier/external-provider objective if suppliers affect outcomes
- one continual-improvement objective tied to corrective-action closure

---

## 7. Verification Checklist

- [ ] Objectives exist at the functions and levels that matter to the deployment
- [ ] Each objective is measurable or has a defined evaluation method
- [ ] Each objective has a named owner and review cadence
- [ ] Evidence sources are identified up front
- [ ] Customer and supplier quality are not omitted where they materially matter
- [ ] Objectives are revisited during management review and updated when context changes
