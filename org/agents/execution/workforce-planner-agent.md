# Agent Type Definition: Workforce Planner Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-workforce-planner-agent` |
| **Name** | Workforce Planner Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `people` |
| **Category** | workforce-planning |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | proposed |
| **Proposed date** | 2026-02-20 |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | |
| **Retired date** | |
| **Superseded by** | |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | <!-- assign during approval --> |
| **Contact** | <!-- primary human contact --> |
| **Approved by** | <!-- CTO or delegate --> |

## Description

**What this agent does:**
Analyzes capacity signals from the observability platform and work artifacts to identify human workforce gaps. Translates operational bottlenecks (e.g., PR review latency, mission throughput degradation, SLA breaches) into headcount recommendations. Produces workforce planning reports and draft hiring plans for human review.

**Problem solved:**
Capacity problems in engineering and other functions often go undetected until they cause significant delivery impact. This agent connects observability data (cycle times, review latency, queue depths) to human capacity decisions, closing the loop between operational signals and People team action.

**Value proposition:**
Enables data-driven headcount decisions instead of reactive gut-feel hiring. Particularly critical in an agentic operating model where human reviewers are a key throughput constraint.

## Capabilities

### Skills
- workforce-capacity-analysis
- headcount-modeling
- signal-to-hiring-plan

### MCP Servers
- <!-- observability platform MCP for metric queries -->
- <!-- HRIS MCP for existing headcount data -->

### Tool Access
- Read: `work/signals/`, `work/missions/*/STATUS.md`, fleet performance reports
- Write: `work/signals/` (new capacity signals), workforce planning reports

### Languages
- <!-- configure per implementation -->

### Data Access
- Observability platform: throughput metrics, cycle time trends, queue depth histograms
- HRIS: current headcount by role and division
- Mission status: active missions and their resource demands

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/people/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Global agent rules, especially Rule 9b (consume observability before recommending)
- `org/4-quality/policies/security.md` — PII handling for employee data

## Interactions

### Produces
- Workforce capacity analysis reports (filed to `work/assets/`)
- Improvement signals for capacity gaps (filed to `work/signals/`)
- Draft hiring plan sections for mission briefs

### Consumes
- Observability platform metrics (via MCP): cycle time P95, review latency, queue depth
- Fleet performance reports from Orchestration Layer
- Active mission briefs and status updates
- Existing headcount data from HRIS

### Collaborates With
- Recruiting Coordinator Agent — hands off hiring plan for execution
- HR Generalist Agent — role definition and leveling
- Orchestration Layer Mission Lead — confirms whether agent fleet scaling can absorb the gap before recommending human hires

### Escalates To
- People Division Lead — all headcount recommendations require human approval
- Steering Layer — headcount plans with budget implications above threshold

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- configure per workload --> |
| **Scaling trigger** | signal-driven or quarterly-cycle |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md`
- `policies/observability.md`

### Evaluation Frequency
per-report

### Performance Metrics
- Accuracy of capacity predictions vs. actual bottleneck resolution
- Time from signal detection to hiring plan draft
- Quality evaluation pass rate

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
