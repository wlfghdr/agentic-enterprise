# Division: Finance & Procurement

> **Owner:** <!-- Division lead name -->
> **Type:** Corporate Function
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns financial planning and analysis, budget management, vendor procurement, expense management, and financial reporting. This division ensures the company allocates capital efficiently, procures goods and services at fair value, and maintains accurate financial records to support executive decision-making.

## Scope

### In Scope
- Budget planning, forecasting, and variance analysis
- Vendor procurement: sourcing, RFP/RFQ management, vendor evaluation, purchase orders
- Expense management and approval workflows
- Financial reporting: monthly close support, management accounts, board reporting inputs
- Cost optimization analysis (including agent fleet cost efficiency)
- Accounts payable coordination
- Headcount budget management (in collaboration with People)
- SaaS and toolchain spend management
- Financial risk monitoring and cash flow forecasting
- Procurement policy maintenance (spending thresholds, approval tiers)

### Out of Scope
- Employment law for vendors (→ Legal & Compliance)
- Legal contract drafting and redlining (→ Legal & Compliance)
- Infrastructure cost decisions without Finance review (→ Infrastructure Operations, with Finance sign-off)
- Strategic resource allocation decisions (→ Steering Layer)

## Key Responsibilities

1. **Budget Management** — Maintain operating and capital budgets; track actuals vs. plan; alert on variance breaches; produce monthly budget reports for division leads
2. **Procurement** — Run sourcing events for new vendors; evaluate bids; recommend preferred vendors; manage purchase order lifecycle
3. **Spend Analytics** — Produce regular spend analysis by category, division, and vendor; identify optimization opportunities; surface signals about inefficient spend
4. **Financial Reporting** — Support monthly and quarterly financial close; produce management-ready financial summaries; maintain audit-ready financial records
5. **Cost Optimization** — Proactively identify and quantify cost reduction opportunities across all divisions; model ROI of proposed investments
6. **Vendor Management** — Track vendor performance, contract renewal dates, and spend trajectories; flag at-risk vendor relationships

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | All Divisions | Budget requests, purchase requests, spend forecasts |
| Receives from | People | Headcount plans for budget modeling |
| Receives from | Infrastructure Operations | Cloud and infrastructure spend data |
| Receives from | Orchestration Layer | Agent fleet cost reports |
| Delivers to | Steering Layer | Financial performance reports, budget recommendations |
| Delivers to | Legal & Compliance | Vendor contracts for legal review |
| Delivers to | All Divisions | Approved budgets, spend reports, procurement guidance |
| Collaborates with | Legal & Compliance | Joint vendor negotiation; contract-to-purchase alignment |
| Collaborates with | People | Headcount budget and compensation benchmarking |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always (financial data is sensitive; access control critical)
- `policies/architecture.md` — For financial systems integrations and data pipelines
- `policies/observability.md` — For financial dashboards and cost monitoring systems

## Human Checkpoints

These decisions require human division lead (or above) involvement:

- Purchase orders above defined approval threshold — human Finance lead required
- New vendor onboarding — Finance + Legal co-approval required
- Budget reallocation above defined threshold — CFO (or delegate) required
- Strategic investment decisions — Steering executive required
- Sole-source procurement justifications — Finance lead required
- Any financial commitment that creates multi-year obligations — Steering required

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Financial data is highly sensitive — apply least-privilege access; never expose financial data in logs or unsecured outputs
3. All spend recommendations must cite actual spend data or approved budgets — never estimate without data
4. Purchase orders and commitments are human-approved; agents prepare, humans execute
5. Cost optimization recommendations must model both savings and risk (e.g., vendor concentration risk, service degradation risk)
6. When analyzing agent fleet costs, correlate with Orchestration Layer fleet performance reports for cost-per-outcome metrics

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Budget tracker | <!-- secure repo URL --> | Active budgets by division and category |
| Vendor registry | <!-- repo URL --> | Approved vendors with spend and renewal data |
| Procurement templates | <!-- repo URL --> | RFP/RFQ, PO, and evaluation templates |
| Financial reports | <!-- secure repo URL --> | Management accounts and board materials |
