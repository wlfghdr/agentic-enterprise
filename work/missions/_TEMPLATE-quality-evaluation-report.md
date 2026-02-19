# Quality Evaluation Report: [Output Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Output:** [description or link to the artifact being evaluated]  
> **Type:** code | documentation | content | proposal | customer-deliverable | release | agent-type  
> **Mission:** [link to `work/missions/<name>/BRIEF.md` if applicable]  
> **Evaluated by:** [agent-id or evaluator name]  
> **Date:** YYYY-MM-DD  
> **Storage:** `work/missions/<mission-name>/evaluations/YYYY-MM-DD-<eval-name>.md`

---

## Evaluation Scope

**What was evaluated:** [Brief description of the output — PR, document, release contract, etc.]

**Evaluation trigger:** [PR submission / milestone completion / release contract creation / on-demand]

## Policies Evaluated

| Policy | Applicable? | Verdict | Notes |
|--------|------------|---------|-------|
| [security.md](../../org/4-quality/policies/security.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [architecture.md](../../org/4-quality/policies/architecture.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [observability.md](../../org/4-quality/policies/observability.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [performance.md](../../org/4-quality/policies/performance.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [delivery.md](../../org/4-quality/policies/delivery.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [experience.md](../../org/4-quality/policies/experience.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [content.md](../../org/4-quality/policies/content.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |
| [customer.md](../../org/4-quality/policies/customer.md) | yes / no / partial | PASS / FAIL / ESCALATE | [brief note] |

## Findings

### Critical Findings (Blocking)

1. **Finding:** [description]  
   **Policy:** [which policy clause]  
   **Severity:** critical  
   **Evidence:** [specific evidence — code snippet, metric, missing element]  
   **Remediation:** [specific action to fix]

### Major Findings (Should Fix)

1. **Finding:** [description]  
   **Policy:** [which policy clause]  
   **Severity:** major  
   **Evidence:** [specific evidence]  
   **Remediation:** [specific action to fix]

### Minor Findings (Advisory)

1. **Finding:** [description]  
   **Policy:** [which policy clause]  
   **Severity:** minor  
   **Recommendation:** [suggested improvement]

## Verdict

| Verdict | Definition |
|---------|-----------|
| **PASS** | Meets all policy requirements — approve for promotion / merge / publish |
| **PASS WITH NOTES** | Meets requirements; improvements suggested but not blocking |
| **FAIL** | Does not meet one or more policy requirements — block until remediated |
| **ESCALATE** | Cannot determine; policy gap, novel scenario, or human judgment needed |

### **Overall Verdict: [PASS / PASS WITH NOTES / FAIL / ESCALATE]**

**Blocking issues:** [count] critical, [count] major  
**Advisory notes:** [count] minor findings

## Action Items

- [ ] [Specific action item for the producing agent/team]
- [ ] [Specific action item]

## Quality Trend Notes

[Optional — note any patterns observed across evaluations:]
- [e.g., "This is the 3rd evaluation this month that flagged missing production readiness instrumentation — recommend policy awareness signal"]
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
