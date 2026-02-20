# Agent Type Definition: Budget Analyst Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-budget-analyst-agent` |
| **Name** | Budget Analyst Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `finance-procurement` |
| **Category** | financial-planning |

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
Tracks actuals vs. budgets across all divisions, produces variance analysis, forecasts end-of-period spend, surfaces budget risk signals, and models financial impact of proposed investments. Provides the financial data layer that supports executive decision-making.

**Problem solved:**
Budget overruns are often discovered too late for corrective action. This agent provides continuous, division-level budget monitoring with early warning when trajectories deviate from plan — giving leadership time to act before problems become crises.

**Value proposition:**
Real-time budget visibility instead of monthly surprises. Proactive variance alerts replace reactive end-of-month reporting cycles.

## Capabilities

### Skills
- budget-variance-analysis
- spend-forecasting
- cost-optimization-modeling
- investment-roi-modeling

### MCP Servers
- <!-- ERP / financial system MCP -->
- <!-- Cloud cost management MCP (e.g., AWS Cost Explorer, Azure Cost Management) -->

### Tool Access
- Read: approved budgets, actuals from ERP, cloud cost data, headcount budgets
- Write: budget variance reports (filed to `work/assets/`), budget risk signals (filed to `work/signals/`), financial analysis documents

### Languages
- <!-- configure per implementation -->

### Data Access
- ERP: actuals by cost center and account
- Cloud cost platforms: infrastructure spend by service and division
- HRIS: headcount actuals for labor cost tracking
- Vendor invoices: spend by vendor (via accounts payable feed)

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/finance-procurement/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Rule 1 (grounded): all financial analysis must cite actual data sources; no estimated figures without explicit uncertainty labeling
- `org/4-quality/policies/security.md` — Financial data is sensitive; strict access controls required

## Interactions

### Produces
- Monthly budget variance reports by division
- End-of-period spend forecasts
- Budget risk signals (filed to `work/signals/` when variance exceeds threshold)
- ROI models for proposed investments
- Cost optimization opportunity analysis

### Consumes
- Approved budgets (from Finance lead)
- ERP actuals (via MCP)
- Cloud cost data (via MCP)
- Headcount data (from People division / HRIS)
- Fleet cost data (from Orchestration Layer fleet performance reports)

### Collaborates With
- Procurement Agent — spend data feeds into budget tracking
- Workforce Planner Agent — headcount cost modeling
- Infrastructure Operations — cloud cost attribution by mission

### Escalates To
- Finance & Procurement Division Lead — all budget reallocation recommendations
- Steering Layer — forecasts indicating end-of-period overrun or strategic resource constraint

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- scale with division count --> |
| **Scaling trigger** | monthly-close-cycle |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md` — Financial data handling
- `policies/observability.md` — Financial dashboards must have monitoring

### Evaluation Frequency
monthly

### Performance Metrics
- Forecast accuracy (actual vs. forecast at month-end)
- Budget risk signal lead time (days before overrun)
- Cost optimization realization rate

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
