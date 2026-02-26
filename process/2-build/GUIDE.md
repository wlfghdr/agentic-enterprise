# Build Loop — Guide

> **What this covers:** How approved missions get executed. The complete Build loop workflow.

---

## Workflow

### Step 1: Mission Decomposition (Orchestration Layer)

Once a mission brief is approved:
1. Orchestration Layer breaks the mission into work streams
2. Each stream is assigned to a division
3. Fleet configuration created (`org/2-orchestration/fleet-configs/<mission>.md`)
4. Dependencies between streams mapped
5. Human checkpoints identified

### Step 2: Technical Design (Execution Layer)

For missions marked `design-required: true` in the Mission Brief, a Technical Design document must be produced and approved **before** stream execution begins.

**When required:**
- Multi-stream missions (2+ execution streams with dependencies)
- Novel architecture patterns not covered by existing ADRs
- Missions involving new external APIs, data model changes, or security-sensitive flows
- Regulated features requiring specification traceability

**Process:**
1. Technical Design Agent (or Tech Lead) reads Mission Brief, Outcome Contract, and Fleet Config
2. Produces Technical Design document (`work/missions/<name>/TECHNICAL-DESIGN.md`)
3. Design covers: API contracts, data models, interface contracts between streams, behavioral specifications, security threat model, performance budgets, **observability design** (instrumentation plan, metrics, SLOs, dashboards, alerting, production baselines for modified components — per AGENTS.md Rule 9c and `org/4-quality/policies/observability.md`), and key architecture decisions
4. Design submitted as PR for architecture review at the human checkpoint
5. Execution streams begin only after design is approved (or marked N/A for single-stream missions)

**Template:** `work/missions/_TEMPLATE-technical-design.md`

> **Note:** For simple, single-stream missions without novel patterns, this step can be skipped — the Mission Brief + Fleet Config provide sufficient context. The Orchestration Layer determines whether design is required based on mission complexity.

### Step 3: Stream Execution (Execution Layer)

For each work stream:
1. Agent reads fleet configuration to understand scope, constraints, and policies
2. Agent reads Technical Design document (if one exists for this mission)
3. Agent reads ALL applicable quality policies
4. Agent produces outputs (code, docs, content, etc.)
5. Agent self-evaluates against quality policies
6. Agent submits outputs as Pull Request

### Step 4: Quality Evaluation (Quality Layer)

For each submitted output:
1. Quality eval agent reviews against all applicable policies
2. Produces evaluation verdict: PASS | PASS WITH NOTES | FAIL | ESCALATE
3. For FAIL: specific feedback provided, output returned to Execution
4. For ESCALATE: flagged for human review

### Step 5: Iteration

- FAIL outputs are revised and resubmitted
- ESCALATE outputs wait for human decision
- PASS outputs proceed to Ship loop

### Step 6: Decision Recording

Novel patterns, architecture choices, and strategy decisions discovered during Build are captured:
1. Use `work/decisions/_TEMPLATE-decision-record.md`
2. Submit as PR to `work/decisions/`
3. Architecture Governor reviews and approves

---

## Build Quality Checklist

Before submitting any output:
- [ ] Read all applicable quality policies
- [ ] Self-evaluated against each policy criterion
- [ ] Automated checks pass (lint, test, security scan)
- [ ] Acceptance criteria from outcome contract addressed
- [ ] **Observability designed** (if new components) or **baseline impact assessed** (if modifying existing) — per `org/4-quality/policies/observability.md` and AGENTS.md Rule 9c
- [ ] Any novel patterns documented in decision record
- [ ] Dependencies logged
- [ ] Conventional commit messages used

## Work Stream Types

| Type | Typical Outputs | Key Policies |
|------|----------------|--------------|
| Design/Spec | API contracts, data models, interface specs, threat models, behavioral specs, observability design | architecture, observability |
| Engineering | Code, tests, API specs | security, architecture, performance, observability |
| Documentation | User docs, API docs, guides | content, experience |
| Content | Blog posts, release notes | content |
| Sales | Proposals, battlecards | customer, content |
| Customer Success | QBR packages, health reports | customer |
| Operations | Runbooks, dashboards, alerts | performance, security |

## Exit Criteria / Handoff to Ship

Before a mission's outputs can proceed from Build to Ship, **all** of the following must be true:

### Required Artifacts
- [ ] All tasks in `TASKS.md` are marked `done` (or explicitly descoped with rationale)
- [ ] All PRs for in-scope deliverables are merged to `main`
- [ ] Quality evaluation reports exist for every output (`work/missions/<name>/evaluations/`)
- [ ] All evaluation verdicts are **PASS** or **PASS WITH NOTES** — no open FAILs or ESCALATEs
- [ ] Decision records filed for all novel patterns or architecture choices (`work/decisions/`)

### Quality Gates Passed
- [ ] All applicable quality policies evaluated (security, architecture, performance, observability)
- [ ] Automated checks pass (lint, test, security scan) for all code outputs
- [ ] Task acceptance criteria verified by Quality Layer

### Ownership Transfer
- [ ] **Build owner:** Execution Layer agents (mission complete from their perspective)
- [ ] **Ship owner:** Orchestration Layer (takes over for release preparation)
- [ ] Orchestration Layer notified that Build is complete and release preparation can begin
- [ ] `STATUS.md` updated to reflect readiness for Ship loop

> **Gate enforcer:** The Quality Layer verifies this checklist before approving the Build→Ship transition. The Orchestration Layer cannot create a release contract until all items are checked.

## Anti-Patterns

- ❌ Starting execution without reading the Technical Design (when one exists)
- ❌ Starting execution without reading quality policies
- ❌ Large PRs (break into smaller, reviewable chunks)
- ❌ Ignoring evaluation feedback
- ❌ Making architecture decisions without decision records
- ❌ Working outside assigned stream paths
- ❌ Skipping self-evaluation before submission
