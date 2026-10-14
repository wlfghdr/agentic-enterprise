# Division: People

> **Owner:** <!-- Division lead name -->
> **Type:** Corporate Function
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns the full human and agent talent lifecycle: recruiting, onboarding, performance management, learning and development, workforce planning, employee relations, and culture. This division ensures the organization has the right people and agents at the right time and that they are engaged, growing, and productive.

> **Note on scope:** In an agentic enterprise, "workforce planning" covers both human headcount and agent fleet capacity. People and Orchestration collaborate: People owns the human side (recruiting, roles, performance); Orchestration owns the agent side (fleet sizing, mission assignment). Signals about review bottlenecks, mission capacity, or throughput degradation may originate from either division.

## Scope

### In Scope
- Talent acquisition: job design, sourcing, screening, interviewing, offer management
- Employee onboarding and offboarding lifecycle management
- Performance management frameworks, review cycles, and improvement plans
- Learning and development programs, training content curation
- Workforce planning and headcount forecasting (human roles)
- Employee relations and culture programs
- HR compliance (labor law adherence, audit-ready records)
- Role and leveling framework maintenance
- Compensation benchmarking analysis (not final decisions — those require Finance)
- Diversity, equity, and inclusion program management

### Out of Scope
- Compensation approval and payroll execution (→ Finance & Procurement)
- Employment contracts and legal employment law advisory (→ Legal & Compliance)
- Agent fleet sizing and mission composition (→ Orchestration Layer)
- Office facilities and physical infrastructure (→ Infrastructure Operations)

## Key Responsibilities

1. **Recruiting** — Source, attract, screen, and present qualified candidates for open roles; coordinate interview pipelines; draft offer materials for human approval
2. **Workforce Planning** — Analyze capacity signals (e.g., PR review latency, mission throughput) and recommend headcount changes; translate operational signals into hiring plans
3. **Onboarding** — Ensure new hires are productive within defined ramp windows; maintain onboarding checklists and buddy programs
4. **Performance** — Run structured review cycles; surface performance risk early; coordinate improvement plans with managers
5. **Learning & Development** — Curate and deliver skill-building programs aligned to company strategic needs
6. **HR Compliance** — Maintain audit-ready employment records; track labor law requirements by jurisdiction
7. **Culture & Engagement** — Monitor engagement signals; design programs that strengthen culture and reduce attrition risk

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Steering Layer | Headcount budget signals, org evolution proposals |
| Receives from | All Divisions | Capacity and performance signals filed via `work/signals/` |
| Receives from | Orchestration Layer | Fleet performance reports indicating human capacity gaps |
| Delivers to | Quality Layer | HR artifacts (job descriptions, process documents) for policy evaluation |
| Delivers to | Legal & Compliance | Employment-related legal questions, contract needs |
| Delivers to | Finance & Procurement | Headcount forecast for budget planning; compensation benchmarks |
| Collaborates with | Engineering Foundation | Role definitions for engineering levels and recruiting pipelines |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always (candidate data is PII; privacy-first handling required)
- `policies/content.md` — For all job postings, offer letters, and employee-facing documents
- `policies/customer.md` — For external-facing employer brand content

## Human Checkpoints

These decisions require human division lead (or above) involvement:

- Offer extension — all offers require hiring manager and HR lead approval
- Headcount plan approval — workforce plans require Steering executive sign-off
- Performance improvement plans and terminations — human HR lead mandatory
- Changes to compensation frameworks — require Finance co-approval
- Jurisdictional HR compliance determinations — require Legal co-review

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Treat all candidate and employee data as PII — never log, store, or transmit it outside approved systems
3. Follow established templates for job descriptions and offer materials
4. Workforce planning recommendations must cite observability data (throughput metrics, cycle times) or signal files — not assumptions
5. Recruiting pipelines are human-decision-gated at offer stage; agents prepare, humans decide

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Job description library | <!-- repo URL --> | Approved JD templates by role family |
| Interview guide library | <!-- repo URL --> | Structured interview guides |
| HR policy documents | <!-- repo URL --> | Employee handbook and HR policies |
| Onboarding checklists | <!-- repo URL --> | Role-specific onboarding tracks |
