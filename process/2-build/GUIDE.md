# Build Loop — Guide

> **What this covers:** How approved missions get executed. The complete Build loop workflow.

---

## Workflow

### Step 1: Mission Decomposition (Orchestration Layer)

Once a mission brief is approved:
1. Orchestration Layer breaks the mission into work streams
2. Each stream is assigned to a division
3. Fleet configuration created (`org/2-orchestration/fleet-configs/<mission>.yaml`)
4. Dependencies between streams mapped
5. Human checkpoints identified

### Step 2: Stream Execution (Execution Layer)

For each work stream:
1. Agent reads fleet configuration to understand scope, constraints, and policies
2. Agent reads ALL applicable quality policies
3. Agent produces outputs (code, docs, content, etc.)
4. Agent self-evaluates against quality policies
5. Agent submits outputs as Pull Request

### Step 3: Quality Evaluation (Quality Layer)

For each submitted output:
1. Quality eval agent reviews against all applicable policies
2. Produces evaluation verdict: PASS | PASS WITH NOTES | FAIL | ESCALATE
3. For FAIL: specific feedback provided, output returned to Execution
4. For ESCALATE: flagged for human review

### Step 4: Iteration

- FAIL outputs are revised and resubmitted
- ESCALATE outputs wait for human decision
- PASS outputs proceed to Ship loop

### Step 5: Decision Recording

Novel patterns, architecture choices, and strategy decisions discovered during Build are captured:
1. Use `templates/decision-record.md`
2. Submit as PR to `work/decisions/`
3. Architecture Governor reviews and approves

---

## Build Quality Checklist

Before submitting any output:
- [ ] Read all applicable quality policies
- [ ] Self-evaluated against each policy criterion
- [ ] Automated checks pass (lint, test, security scan)
- [ ] Acceptance criteria from outcome contract addressed
- [ ] Any novel patterns documented in decision record
- [ ] Dependencies logged
- [ ] Conventional commit messages used

## Work Stream Types

| Type | Typical Outputs | Key Policies |
|------|----------------|--------------|
| Engineering | Code, tests, API specs | security, architecture, performance |
| Documentation | User docs, API docs, guides | content, experience |
| Content | Blog posts, release notes | content |
| Sales | Proposals, battlecards | customer, content |
| Customer Success | QBR packages, health reports | customer |
| Operations | Runbooks, dashboards, alerts | performance, security |

## Anti-Patterns

- ❌ Starting execution without reading quality policies
- ❌ Large PRs (break into smaller, reviewable chunks)
- ❌ Ignoring evaluation feedback
- ❌ Making architecture decisions without decision records
- ❌ Working outside assigned stream paths
- ❌ Skipping self-evaluation before submission
