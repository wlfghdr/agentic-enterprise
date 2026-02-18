# Example: Agent Fleet Change — New Agent Type & Deprecation

> **Purpose:** Walkthrough of the agent type lifecycle: proposing a new agent type, deprecating an underperforming one, managing the transition, and measuring results. Shows how the agent registry at `org/agents/` governs fleet composition.
>
> **Scenario:** API integration failures are the leading cause of quality evaluation failures. A new "API contract testing agent" is proposed while an underperforming legacy integration test agent is deprecated. This exercises the **agent lifecycle governance** system.

---

## Why This Example Is Different

The [feature lifecycle](generic-feature-lifecycle.md) produces **product deliverables**. The [company optimization](company-optimization-lifecycle.md) updates **policies and processes**. This example changes the **agent fleet itself** — the workforce that does the work.

- **Origin:** Quality pattern analysis across multiple missions
- **Output:** New agent type definition, fleet composition changes, agent retirement
- **Governance:** Agent Type Registry at `org/agents/`, lifecycle: proposed → active → deprecated → retired
- **Challenge:** Parallel operation during transition, performance comparison, graceful deprecation

---

## Phase 1: Signal Detection from Multiple Sources

**Layer:** Quality + Orchestration + Execution · **Loop:** Operate · **Agent types:** Various

Three categories of agents independently surface the same underlying problem:

### Signal A: Quality Pattern

The `delivery-evaluator` agent, analyzing quality evaluation results across Q1 2026, detects a pattern:

**Artifact created:** `work/signals/2026-05-20-api-contract-failures-leading-cause.md`

```markdown
# Signal: API Contract Failures Are #1 Cause of Quality FAIL Verdicts

## Source
- Category: internal
- Source system: Quality evaluation report analysis
- Confidence: high

## Observation
Across 47 quality evaluations in Q1 2026:
- 14 FAIL verdicts (30% failure rate)
- 9 of 14 FAILs (64%) were caused by API contract violations:
  - Request/response schema mismatches: 4
  - Missing required fields in API responses: 3
  - Breaking changes to existing endpoints: 2
- The existing `integration-test-agent` caught only 3 of 9 contract issues 
  during self-evaluation (33% detection rate)

## Initial Assessment
- Urgency: next-cycle
- Potential impact: high (affects quality of every API-producing mission)
- Affected divisions: Core Services, Data Foundation, Customer Experience
```

### Signal B: Execution Friction

A `coding-agent` files a frustration signal:

**Artifact created:** `work/signals/2026-05-21-manual-contract-validation-time.md`

```markdown
# Signal: 30% of Coding Agent Time Spent on Manual API Contract Validation

## Observation
In the last 3 missions involving API work, coding agents spent an estimated 
30% of implementation time manually checking API contracts:
- Comparing implementation against OpenAPI specs
- Verifying backward compatibility with existing consumers
- Testing response schemas against documented contracts

This is repetitive, automatable work that should be handled by a specialized agent.
The existing `integration-test-agent` does not validate API contracts — it runs 
integration tests that only catch runtime errors, not contract drift.
```

### Signal C: Production Incidents

The `incident-response-agent` flags a recurring pattern:

**Artifact created:** `work/signals/2026-05-22-api-contract-drift-incidents.md`

```markdown
# Signal: 4 Production Incidents in Q1 Caused by API Contract Drift

## Observation
4 SEV2/SEV3 incidents in Q1 2026 traced to API contract drift:
1. INC-2026-014: Mobile app crash — API removed a field without deprecation notice
2. INC-2026-019: Partner integration failure — response type changed from array to object
3. INC-2026-023: Webhook delivery failures — payload schema silently changed
4. INC-2026-027: Data pipeline failure — API pagination response format changed

All 4 were caught in production, not pre-production. The existing integration test 
suite did not catch any of them because tests only validated "happy path" responses.
```

---

## Phase 2: Signal Aggregation & Pattern Alert

**Layer:** Steering · **Loop:** Continuous Sensing · **Agent type:** `signal-aggregation`

**Artifact created:** `work/signals/digests/2026-W21-digest.md`

```markdown
# Signal Digest: Week 2026-W21

## Pattern Alerts

### Pattern Alert: API Contract Testing Gap
- Signals involved: 6 (3 this week + 3 from prior weeks on related topics)
- First signal: 2026-04-08 (quality eval turnaround — partial overlap)
- Latest signal: 2026-05-22
- Pattern description: API contract validation is a systemic gap across the 
  agent fleet. Quality evaluators catch contract issues post-hoc (64% of FAIL verdicts), 
  coding agents spend 30% of time on manual contract checks, and production incidents 
  keep recurring. The existing `integration-test-agent` has a 33% detection rate 
  for contract issues — it was designed for integration testing, not contract testing.
- Recommended action: Two-part evolution — propose new agent type + assess existing agent
- Urgency: high

## Cross-Layer Observations
| Source Layer | Observation | Implication |
|-------------|-------------|-------------|
| Quality | 64% of FAILs are contract-related | Quality eval agents are catching what execution should prevent |
| Execution | 30% time on manual contract work | Specialized agent would reclaim capacity |
| Operate | 4 production incidents from contract drift | Prevention > detection > remediation |
```

---

## Phase 3: Agent Type Proposal

**Layer:** Steering · **Loop:** Structural Proposals · **Agent type:** `org-evolution-proposer`

The `org-evolution-proposer` agent creates two linked proposals:

### 3a. New Agent Type Proposal

**Artifact created:** PR `evolution/new-agent-type/api-contract-testing-agent`  
**Template:** `org/agents/_TEMPLATE-agent-type-proposal.md`

```markdown
# Agent Type Proposal: API Contract Testing Agent

## Metadata
| Field | Value |
|-------|-------|
| Proposed ID | execution/api-contract-testing-agent |
| Layer | Execution |
| Status | proposed |
| Proposer | org-evolution-proposer (Steering) |
| Trigger | Signal digest 2026-W21: API Contract Testing Gap |

## Purpose
Automated validation of API contracts before, during, and after code changes. 
This agent ensures that API implementations match their contracts (OpenAPI specs), 
that changes are backward-compatible, and that contract drift is caught before 
production.

## Capabilities
1. **Pre-implementation:** Parse OpenAPI specs and generate contract test scaffolding
2. **During implementation:** Validate that implementation matches the contract as 
   code is written (schema validation, required fields, type checking)
3. **Pre-merge:** Run backward-compatibility checks against existing consumers
4. **Post-deploy:** Validate production API responses against published contracts

## Quality Policies Enforced
- `architecture.md` — API design standards, backward compatibility rules
- `security.md` — API authentication contract, input validation schemas
- `delivery.md` — Breaking change detection and migration path requirements

## Integration Points
- Triggered by: PRs that touch API-related files (routes, controllers, schemas)
- Reads: OpenAPI specs, existing consumer contracts, API test results
- Produces: Contract validation reports, breaking change alerts
- Interacts with: `coding-agent` (provides feedback during build), 
  `architecture-review` (shares contract analysis), `deploy-agent` (post-deploy validation)

## Resource Requirements
| Resource | Estimate |
|----------|----------|
| Instances (baseline) | 2 |
| Instances (peak) | 4 |
| Scaling trigger | > 3 API PRs in queue |
| Compute profile | Light (schema validation, no compilation) |

## Expected Impact
| Metric | Current | Expected | Method |
|--------|---------|----------|--------|
| API contract FAIL rate | 64% of all FAILs | < 10% | Quality eval reports |
| Manual contract validation time | 30% of coding agent time | < 5% | Agent time tracking |
| Production API contract incidents | 4 per quarter | < 1 per quarter | Incident tracking |
| Integration test agent FAIL rate | 40% on contract checks | N/A (deprecated) | — |

## Relationship to Existing Agent Types
- **Replaces (partially):** `integration-test-agent` — contract-specific checks move to this new agent
- **Complements:** `coding-agent` — provides real-time contract feedback during implementation
- **Complements:** `architecture-review` — shares contract analysis for architectural evaluation
- **Does not replace:** `integration-test-agent` runtime integration testing (non-contract)

## Risks
| Risk | Mitigation |
|------|-----------|
| False positives on contract violations | Configurable strictness levels; human override |
| Overlap with integration-test-agent during transition | Clear scope boundary; parallel operation with comparison metrics |
| OpenAPI spec quality varies by division | Agent reports spec quality issues as improvement signals |
```

### 3b. Deprecation Assessment

The `org-evolution-proposer` also requests a formal assessment of the existing `integration-test-agent`:

**Artifact created:** `work/signals/2026-05-23-integration-test-agent-assessment-request.md`

```markdown
# Signal: Integration Test Agent Performance Assessment Requested

## Observation
The `integration-test-agent` (execution/integration-test-agent) has a 40% FAIL rate 
on contract-specific checks and only 33% detection rate for API contract issues that 
later cause quality evaluation failures. The new `api-contract-testing-agent` proposal 
would absorb the contract-testing responsibilities.

## Recommended Disposition
- [x] Assess integration-test-agent for partial deprecation (contract scope)
```

---

## Phase 4: Existing Agent Assessment

**Layer:** Steering · **Loop:** Structural Proposals · **Agent type:** `transformation-health`

The `transformation-health` agent performs a formal assessment of the `integration-test-agent`:

```markdown
# Agent Type Assessment: integration-test-agent

## Performance Analysis
| Metric | Value | Benchmark | Verdict |
|--------|-------|-----------|---------|
| Overall FAIL rate | 22% | < 15% | Below benchmark |
| Contract check FAIL rate | 40% | < 10% | Significantly below |
| Detection rate (contract issues) | 33% | > 80% | Critical gap |
| Compute cost per run | $0.12 | $0.08 | 50% above benchmark |
| False positive rate | 8% | < 5% | Above benchmark |

## Scope Analysis
The agent currently handles two distinct responsibilities:
1. **Runtime integration testing** — end-to-end test execution, service health checks, 
   dependency validation. Performance: adequate (85% detection rate).
2. **Contract testing** — schema validation, backward compatibility, field checking. 
   Performance: inadequate (33% detection rate).

## Recommendation
**Partial deprecation.** Transfer contract testing responsibilities to the proposed 
`api-contract-testing-agent`. Retain runtime integration testing responsibilities. 
Rename to clarify scope: `runtime-integration-test-agent`.

Alternatively: if the new agent demonstrates it can also handle runtime integration 
tests, consider full deprecation and replacement.

## Transition Risk Assessment
- **Parallel operation period:** Recommended 4 weeks
- **Comparison metrics:** Both agents evaluate the same PRs; compare detection rates
- **Rollback path:** If new agent underperforms, retain old agent at full scope
- **Knowledge transfer:** Contract-related test patterns should be migrated to new agent's instructions
```

---

## Phase 5: Human CTO Review

**Layer:** Steering · **Human checkpoint**

Per the agent type governance rules in `org/agents/README.md`, new agent types and agent deprecations both require **CTO approval**.

Two PRs are submitted:
1. **PR #1:** New agent type definition — `org/agents/execution/api-contract-testing-agent.md`
2. **PR #2:** Deprecation notice — Update to `org/agents/execution/integration-test-agent.md` with `status: deprecated` and scope reduction

**CTO review:**
- Reviews the new agent type proposal: capabilities, integration points, resource requirements
- Reviews the deprecation assessment: performance data, scope analysis, transition plan
- Asks one question: "What happens during the parallel operation if the agents disagree on a contract verdict?"
- The `org-evolution-proposer` responds: "During parallel operation, if agents disagree, the stricter verdict applies (union of findings). Disagreements are logged for analysis. After parallel period, the agent with higher detection rate and lower false-positive rate becomes authoritative."
- CTO approves both PRs. ✅

---

## Phase 6: Build & Deploy New Agent Type

**Layer:** Strategy → Orchestration → Execution · **Loop:** Build

A standard mission is created (abbreviated — follows the same pattern as the feature lifecycle):

**Mission:** `work/missions/api-contract-testing-agent/BRIEF.md` — MISSION-2026-028

### Execution Streams

| Stream | Division | Description |
|--------|----------|-------------|
| agent-definition | Engineering Foundation | Agent type definition, instructions, capabilities |
| agent-skills | Engineering Foundation | MCP server connections, API spec parsers, schema validators |
| agent-testing | Quality & Security Engineering | Sandbox testing, benchmark scenarios, comparison framework |
| agent-docs | Knowledge Enablement | Agent type documentation, integration guides |

### Key Deliverables

1. **Agent Type Definition** (`org/agents/execution/api-contract-testing-agent.md`)
   - Full agent type file following `_TEMPLATE-agent-type.md`
   - Status: `proposed` (will move to `active` after validation)

2. **Agent Instructions**
   - How to read OpenAPI specs
   - How to validate request/response schemas
   - How to check backward compatibility
   - How to report findings using the Quality Evaluation Report template
   - Escalation rules: when to flag for human review

3. **Agent Skills & Integrations**
   - MCP server connection to API gateway
   - OpenAPI spec parser
   - JSON Schema validator
   - Backward compatibility checker (based on semantic versioning rules)
   - PR comment integration (inline contract feedback)

4. **Benchmark Test Suite**
   - 50 known contract violation scenarios (from the 9 historical FAILs + 4 incidents)
   - Expected detection rate: > 90% on known scenarios
   - Performance baseline for comparison during parallel operation

### Quality Evaluation

The `architecture-review` and `delivery-evaluator` agents evaluate the new agent type:

```markdown
# Quality Evaluation Report: API Contract Testing Agent Type Definition

## Policies Evaluated
| Policy | Verdict | Notes |
|--------|---------|-------|
| architecture.md | PASS | Clear layer placement, well-defined integration points |
| delivery.md | PASS | Includes scaling triggers and monitoring |
| security.md | PASS | Agent has read-only access to API specs; no write permissions to production |

## Agent Type-Specific Checks
| Check | Verdict |
|-------|---------|
| Purpose clearly defined | PASS |
| Non-overlapping with existing agents (post-deprecation) | PASS |
| Resource requirements justified | PASS |
| Rollback/deprecation path defined | PASS |
| Success metrics measurable | PASS |

## Overall Verdict: PASS
```

---

## Phase 7: Agent Type Activation & Fleet Update

**Layer:** Orchestration · **Loop:** Ship · **Agent types:** `release-coordinator`, `mission-orchestrator`

### Status Change: proposed → active

After quality evaluation passes and benchmark tests succeed (95% detection rate on known scenarios — above the 90% target), the agent type status is updated:

**Artifact updated:** `org/agents/execution/api-contract-testing-agent.md`
```markdown
status: active  # Changed from: proposed
activation-date: 2026-06-10
```

### Fleet Configuration Updates

The `mission-orchestrator` updates all active fleet configs that involve API work to include the new agent:

```markdown
# Addition to fleet configs with API streams

### Stream: api-contract-validation (NEW)
| Field | Value |
|-------|-------|
| Agent pool | api-contract-testing-agent |
| Division | (same as API implementation stream) |
| Exclusive | no (operates on same paths as coding-agent, read-only) |

Triggered by: PRs from api-implementation streams
Quality policies: architecture, security
```

### Deprecation Notice

The `integration-test-agent` definition is updated:

**Artifact updated:** `org/agents/execution/integration-test-agent.md`
```markdown
status: deprecated  # Changed from: active
deprecation-date: 2026-06-10
deprecation-reason: Contract testing responsibilities transferred to api-contract-testing-agent
remaining-scope: Runtime integration testing only
sunset-date: 2026-07-10 (after parallel operation period)
replacement: execution/api-contract-testing-agent (for contract testing)
```

---

## Phase 8: Parallel Operation & Comparison

**Layer:** Orchestration + Quality · **Loop:** Operate · **Agent types:** `fleet-performance-monitor`, both test agents

For 4 weeks, both agents operate on every API PR. This is the critical transition period.

### Parallel Operation Rules

1. Both agents evaluate every API-related PR
2. The `api-contract-testing-agent` runs contract-specific checks
3. The `integration-test-agent` runs its full suite (including contract checks it's historically done)
4. If they disagree, the stricter verdict applies (during transition only)
5. All evaluations are logged and compared by the `fleet-performance-monitor`

### Week-by-Week Comparison

**Artifact created:** `work/missions/api-contract-testing-agent/FLEET-REPORT.md`

```markdown
# Fleet Performance Report: Agent Transition Comparison

## Throughput Metrics (4-week parallel period)

### API Contract Testing Agent (NEW)
| Week | PRs Evaluated | Contract Issues Found | False Positives | Detection Rate |
|------|--------------|----------------------|-----------------|---------------|
| 1 | 8 | 5 | 1 | 83% |
| 2 | 11 | 7 | 0 | 100% |
| 3 | 9 | 4 | 0 | 100% |
| 4 | 12 | 6 | 0 | 95% |
| **Total** | **40** | **22** | **1** | **95%** |

### Integration Test Agent (OLD — contract checks only)
| Week | PRs Evaluated | Contract Issues Found | False Positives | Detection Rate |
|------|--------------|----------------------|-----------------|---------------|
| 1 | 8 | 2 | 0 | 33% |
| 2 | 11 | 3 | 1 | 43% |
| 3 | 9 | 1 | 0 | 25% |
| 4 | 12 | 2 | 0 | 33% |
| **Total** | **40** | **8** | **1** | **35%** |

## Comparison Summary
| Metric | New Agent | Old Agent | Improvement |
|--------|----------|-----------|-------------|
| Contract issue detection rate | 95% | 35% | +171% |
| False positive rate | 2.5% (1/40) | 2.5% (1/40) | Same |
| Avg evaluation time | 45 seconds | 3.2 minutes | -77% |
| Compute cost per eval | $0.03 | $0.12 | -75% |

## Disagreement Log
| PR | New Agent | Old Agent | Actual Issue? | Correct Agent |
|----|----------|-----------|--------------|---------------|
| #1247 | FAIL (schema mismatch) | PASS | Yes — schema mismatch confirmed | New |
| #1263 | FAIL (breaking change) | PASS | Yes — field type changed | New |
| #1281 | PASS | FAIL (false positive) | No — valid implementation | New |
| #1295 | FAIL (missing field) | PASS | Yes — required field omitted | New |
(14 additional disagreements — new agent correct in 13/14 cases)

## Recommendation
New agent clearly outperforms old agent on contract testing:
- 95% vs. 35% detection rate
- 77% faster evaluation
- 75% lower cost
- Correct in 93% of disagreements (13/14)

Proceed with deprecation completion. Retain old agent for runtime integration testing only.
```

---

## Phase 9: Deprecation Completion

**Layer:** Steering · **Loop:** Structural Proposals · **Agent type:** `org-evolution-proposer`

### Retirement of Contract Testing Scope

After the parallel period confirms the new agent's superiority:

1. **Fleet configs updated:** Remove `integration-test-agent` from contract testing duties in all active fleet configs
2. **Agent type updated:** `integration-test-agent` scope formally reduced to runtime integration testing only. Renamed in documentation to `runtime-integration-test-agent` for clarity.
3. **Instructions updated:** Contract-testing instructions removed from the old agent, added to the new agent's instruction set

### Resource Reallocation

```markdown
## Resource Changes
| Resource | Before | After | Savings |
|----------|--------|-------|---------|
| integration-test-agent instances | 4 | 2 (reduced scope) | 2 instances freed |
| api-contract-testing-agent instances | 0 | 2 (new) | — |
| Net compute change | — | — | -$480/month (new agent 75% cheaper per eval) |
```

### Status Changes

**`org/agents/execution/integration-test-agent.md`:**
```markdown
status: active  # Remains active for runtime integration testing
scope: runtime-integration-testing-only  
note: Contract testing responsibilities retired 2026-07-10. 
      See api-contract-testing-agent for contract validation.
```

> **Note:** In this case, the agent isn't fully retired — just reduced in scope. If a future assessment shows its runtime testing capabilities can also be absorbed, it would move to `retired`. The agent type governance system supports graceful scope reduction, not just binary active/retired.

---

## Phase 10: Outcome Measurement & Generated Signals

**Layer:** Strategy + Steering · **Loop:** Ship → Discover · **Agent types:** `product-strategy`, `org-evolution-proposer`

### Outcome Report

**Artifact created:** `work/missions/api-contract-testing-agent/OUTCOME-REPORT.md`

```markdown
# Outcome Report: API Contract Testing Agent

## Targets vs. Actuals (8 weeks post-activation)

| Metric | Baseline | Target | Actual | Verdict |
|--------|---------|--------|--------|---------|
| API contract FAIL rate (% of all FAILs) | 64% | < 10% | 8% | met |
| Manual contract validation time | 30% of coding time | < 5% | 3% | met |
| Production API contract incidents | 4/quarter | < 1/quarter | 0 (8 weeks) | met |
| Agent detection rate (contract issues) | 33% (old) | > 80% | 95% | exceeded |
| Compute cost (contract validation) | $0.12/eval | < $0.10 | $0.03/eval | exceeded |

## Agent Fleet Impact
- **Coding agents** report 27% more productive time (reclaimed from manual contract validation)
- **Quality evaluators** report 40% fewer contract-related FAIL verdicts to process
- **Incident response** has had 0 API contract drift incidents since activation

## Venture Impact
| Venture | Metric | Impact |
|---------|--------|--------|
| Platform Product | API reliability | Contract coverage 95% (was ~35%) |
| Platform Product | Developer experience | Consumer SDKs auto-validated against contracts |

## Lessons Learned

### What worked well
- Parallel operation period provided irrefutable performance comparison data
- CTO's question about disagreement handling proved critical — the union-of-findings 
  rule during transition caught 14 issues the old agent missed
- Benchmark test suite (built from historical failures) gave immediate confidence

### What didn't work as expected
- Week 1 false positive (1 of 40) was caused by an outdated OpenAPI spec, not an 
  agent error. The agent correctly flagged a mismatch — the spec was wrong.
  This revealed a spec maintenance gap.
- Some divisions had incomplete or outdated OpenAPI specs, reducing the new agent's 
  effectiveness until specs were updated

### Agent Fleet Observations
- The parallel operation model should be the standard for all agent type transitions
- Agent type proposals should include a benchmark test suite requirement
```

### Generated Signals

| Signal | Category | Filed As |
|--------|----------|----------|
| OpenAPI spec maintenance gap across divisions | technical | `work/signals/2026-07-15-openapi-spec-maintenance.md` |
| Parallel operation should be standard for agent transitions | process | `work/signals/2026-07-15-agent-transition-parallel-standard.md` |
| Benchmark test suite should be required for agent proposals | process | `work/signals/2026-07-15-agent-benchmark-requirement.md` |
| New agent could also validate event schemas (scope expansion) | technical | `work/signals/2026-07-18-event-schema-validation-opportunity.md` |
| Runtime integration test agent may be further optimizable | internal | `work/signals/2026-07-20-runtime-test-agent-optimization.md` |

---

## Agent Type Lifecycle Summary

This example walked through the complete agent type lifecycle:

```
[Signals detected: capability gap]
        ↓
[Steering: signal aggregation + pattern alert]
        ↓
[Steering: agent type proposal (NEW) + deprecation assessment (OLD)]
        ↓
[CTO approval (both proposals)]
        ↓
[Build mission: agent definition, skills, testing, docs]
        ↓
[Quality evaluation: agent type-specific checks]
        ↓
[Activation: proposed → active in registry]
        ↓
[Fleet config updates: new agent added to relevant streams]
        ↓
[Deprecation notice: old agent marked deprecated]
        ↓
[Parallel operation: 4-week comparison period]
        ↓
[Comparison data: new agent outperforms]
        ↓
[Deprecation completion: old agent scope reduced/retired]
        ↓
[Outcome measurement + new signals → cycle continues]
```

---

## How This Example Differs from Feature and Optimization Lifecycles

| Dimension | Feature Lifecycle | Company Optimization | Agent Fleet Change |
|-----------|------------------|---------------------|-------------------|
| **Origin** | External customers | Internal metrics | Quality patterns + production incidents |
| **Key artifact** | Mission Brief | Evolution Proposal | Agent Type Proposal + Deprecation Assessment |
| **Approval** | VP Product | COO + CTO | CTO |
| **Output** | Product code | Policies + automation | Agent definitions + fleet configs |
| **Validation** | Progressive rollout % | Division-based pilot | Parallel operation comparison |
| **Success measure** | Customer outcomes | Operational metrics | Agent performance metrics |
| **Unique challenge** | Multi-stream coordination | Meta-quality evaluation | Graceful transition, disagreement handling |
| **Registry involved** | Asset registry | Policy registry | Agent Type Registry |

---

## Key Takeaways

- **The agent fleet is a managed, governed system.** Agent types have a lifecycle (proposed → active → deprecated → retired) managed through the registry at `org/agents/`. Changes require CTO approval via PR.
- **Parallel operation is the safe transition model.** Running both agents simultaneously with comparison metrics provides irrefutable data for the transition decision. The "union of findings" rule during overlap ensures nothing is missed.
- **Performance data drives decisions.** The 95% vs. 35% detection rate comparison left no ambiguity. Agent fleet changes should be data-driven, not opinion-driven.
- **Agents observe their own fleet.** The signals that started this lifecycle came from agents observing the fleet's weaknesses — quality evaluators seeing repeated FAIL patterns, coding agents noting wasted time, incident responders tracking preventable production issues.
- **Deprecation is graceful, not abrupt.** The old agent wasn't turned off — its scope was reduced. It still handles runtime integration testing. The registry tracks the full history: why it was deprecated, what replaced it, and what remains.
- **Every change generates new signals.** The new agent revealed an OpenAPI spec maintenance gap nobody knew about. The transition process itself generated process improvement signals (parallel operation standard, benchmark requirement). The cycle of improvement never stops.
