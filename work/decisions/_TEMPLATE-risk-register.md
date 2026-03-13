# Risk Register Entry: <short title>

> **Template version:** 1.0 | **Last updated:** 2026-03-13

> **Instance metadata** (fill in when creating a risk entry from this template):
> **Revision:** 1 | **Last updated:** YYYY-MM-DD | **Status:** open | mitigated | accepted | closed

## Risk Summary

- **Risk ID:** RISK-YYYY-NNN
- **Title:** <descriptive name>
- **Category:** <from risk taxonomy — e.g., SE-1 Prompt Injection, OP-1 Cascade Failure>
- **Risk Owner:** @<named individual — not a team>
- **Related Mission(s):** <link to mission brief, or "organizational" if not mission-specific>
- **Related Issue(s):** <links>

## Risk Description

### What can go wrong

<Describe the risk scenario: what event or condition could occur, and what would the consequences be?>

### Threat source

<Where does this risk originate? External attacker, system failure, process gap, third-party dependency, agent behavior, etc.>

### Affected assets

<What is at risk? Data, services, customers, reputation, compliance status, financial position, etc.>

### Existing controls

<What controls are already in place that partially mitigate this risk? Reference specific policies, procedures, or technical controls.>

## Risk Scoring

### Inherent Risk (before treatment)

| Factor | Score (1–5) | Rationale |
|--------|-------------|-----------|
| **Likelihood** | | <Why this score? Reference evidence, comparable incidents, or observability data> |
| **Impact** | | <Why this score? Reference affected scope, data sensitivity, customer impact> |
| **Inherent Risk Score** | | Likelihood × Impact |

### Risk Rating

_Per `org/4-quality/policies/risk-management.md` §3.2:_

| Score Range | Rating | This risk |
|------------|--------|-----------|
| 1–4 | Low | |
| 5–9 | Medium | |
| 10–15 | High | |
| 16–25 | Critical | |

## Treatment

### Strategy

<Avoid | Mitigate | Transfer | Accept — choose one>

### Treatment Plan

<If Mitigate: What specific controls will be applied? Link to policies, procedures, or technical implementations.>
<If Avoid: What activity or scope is being eliminated?>
<If Transfer: What mechanism (insurance, vendor SLA, contract clause)? What is covered?>
<If Accept: Why is the residual risk within appetite? Who accepts it?>

### Controls Applied

| Control | Type | Source | Status |
|---------|------|--------|--------|
| <control description> | Preventive / Detective / Corrective | <policy or procedure reference> | Implemented / Planned |

## Residual Risk (after treatment)

| Factor | Score (1–5) | Rationale |
|--------|-------------|-----------|
| **Residual Likelihood** | | <How do applied controls reduce likelihood?> |
| **Residual Impact** | | <How do applied controls reduce impact?> |
| **Residual Risk Score** | | Residual Likelihood × Residual Impact |

### Human Acceptance (required if strategy = Accept or residual risk > 0)

- **Accepted by:** @<named individual>
- **Date:** YYYY-MM-DD
- **Rationale:** <Why is this residual risk acceptable?>
- **Monitoring plan:** <How will this risk be monitored going forward?>

## Review Schedule

- **Next review date:** YYYY-MM-DD
- **Review frequency:** <per risk rating: Low=quarterly, Medium=monthly, High=weekly, Critical=daily>
- **Reassessment triggers:** <What events would force an earlier review? Reference §4.3 of risk-management.md>

## Revision History

_Add a row each time this risk register entry is modified._

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial risk assessment |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial template — aligned with risk-management.md §4.1 mandatory fields, ISO 27001 §6.1.2, SOC 2 CC3 |
