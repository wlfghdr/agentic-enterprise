# Fleet Performance Report: [Mission Name or Period]

> **Template version:** 1.0  
> **Scope:** [mission-specific or monthly fleet-wide]  
> **Mission:** [link to `work/missions/<name>/BRIEF.md` — if mission-specific]  
> **Fleet Config:** [link to fleet config YAML — if mission-specific]  
> **Reporting period:** YYYY-MM-DD → YYYY-MM-DD  
> **Author:** [Orchestration Layer — Agent Fleet Manager]  
> **Date:** YYYY-MM-DD  
> **Storage:** `work/missions/<mission-name>/FLEET-REPORT.md` (mission-specific) or as appendix to mission status

---

## Fleet Composition

| Agent Pool | Agent Type | Division | Instances | Status |
|-----------|-----------|----------|-----------|--------|
| [pool name from fleet config] | [agent type ID from registry] | [division] | [count] | active / scaled-up / scaled-down |

## Throughput Metrics

| Metric | This Period | Previous Period | Trend |
|--------|------------|-----------------|-------|
| PRs generated | [count] | [count] | ↑ / → / ↓ |
| PRs merged | [count] | [count] | ↑ / → / ↓ |
| PRs rejected / needs-revision | [count] | [count] | ↑ / → / ↓ |
| PR acceptance rate | [%] | [%] | ↑ / → / ↓ |
| Average cycle time (open → merge) | [hours] | [hours] | ↑ / → / ↓ |
| Signals generated | [count] | [count] | ↑ / → / ↓ |
| Escalations to humans | [count] | [count] | ↑ / → / ↓ |

## Quality Scores

| Quality Dimension | Pass Rate | Trend | Notes |
|------------------|-----------|-------|-------|
| Security | [%] | ↑ / → / ↓ | [notable observations] |
| Architecture | [%] | ↑ / → / ↓ | |
| Observability | [%] | ↑ / → / ↓ | |
| Performance | [%] | ↑ / → / ↓ | |
| Content | [%] | ↑ / → / ↓ | |
| Overall | [%] | ↑ / → / ↓ | |

## Cost Indicators

| Metric | Value | Budget | Variance |
|--------|-------|--------|----------|
| Total agent compute cost | [amount] | [budget] | [+/- %] |
| Cost per merged PR | [amount] | [target] | [+/- %] |
| Cost per mission stream | [amount] | [target] | [+/- %] |

## Bottleneck Analysis

| Bottleneck | Location | Impact | Root Cause | Recommendation |
|-----------|----------|--------|-----------|----------------|
| [e.g., "Quality eval queue backlog"] | [stream/division] | [delay in hours/days] | [e.g., "eval agent capacity insufficient"] | [e.g., "Scale eval agents from 2→4"] |

## Agent Utilization

| Agent Pool | Capacity | Utilization | Idle Time | Recommendation |
|-----------|----------|-------------|-----------|----------------|
| [pool name] | [max instances] | [%] | [%] | [right-size / scale-up / scale-down / no change] |

## Recommendations

### Fleet Tuning
1. [e.g., "Increase implementation-agents pool from 3 to 5 — throughput bottleneck identified"]
2. [e.g., "Reduce content-agents pool from 4 to 2 — underutilized this mission"]

### Instruction Improvements
1. [e.g., "Coding agents frequently fail architecture policy — recommend instruction clarification on API patterns"]

### Process Improvements
1. [e.g., "Quality eval turnaround is the biggest bottleneck — recommend parallel evaluation streams"]

## Generated Signals

| Signal | Category | Link |
|--------|----------|------|
| [Signal description] | fleet / process / cost | [link to `work/signals/<signal>.md`] |
