# Example: Company Optimization — Reducing Deployment Cycle Time

> **Purpose:** Walkthrough of an internally-driven optimization that changes the operating model itself, showing how the Steering Layer drives evolution, policies are updated as code, and the company improves through its own feedback loops.
>
> **Scenario:** Internal metrics show deployments take 3× longer than industry benchmarks. This is not a customer feature request — it's a systemic inefficiency detected by the company's own agents. The fix involves policy updates, process changes, and new automation — not product code.

---

## Why This Example Is Different

The [feature lifecycle example](generic-feature-lifecycle.md) follows the most common path: external demand → product delivery. This example follows a different path:

- **Origin:** Internal signals, not customer requests
- **Protagonist:** Steering Layer, not Strategy Layer
- **Output:** Policy and process changes, not product code
- **Challenge:** Meta-quality — evaluating changes to the quality system itself

This exercises the **evolution mechanisms** of the operating model: Evolution Proposals, policy-as-code updates, and the Steering Layer's three loops (Continuous Sensing, Structural Proposals, Strategic Recalibration).

---

## Phase 1: Internal Signal Detection

**Layer:** Orchestration + Quality · **Loop:** Operate · **Agent types:** `fleet-performance-monitor`, `delivery-evaluator`

Two agents independently detect the same problem from different angles:

### Signal A: Fleet Performance Anomaly

The `fleet-performance-monitor` agent, tracking fleet-wide metrics across all active missions, notices a pattern:

**Artifact created:** `work/signals/2026-05-02-deployment-cycle-time-anomaly.md`

```markdown
# Signal: Deployment Cycle Time 3× Above Benchmark

## Source
- Category: internal
- Source system: Fleet performance analytics
- Confidence: high

## Observation
Across 12 missions completed in Q1 2026, the average time from "all quality evals 
passed" to "deployed in production" is 4.2 days. Industry benchmark for comparable 
organizations is 1.2 days. The gap has widened from 2.1× in Q4 2025 to 3.5× in Q1 2026.

Breakdown:
- Quality eval turnaround: 1.8 days avg (was 0.8 days in Q4)
- Human approval wait time: 1.4 days avg (was 0.6 days)
- Deploy pipeline execution: 0.7 days avg (stable)
- Post-deploy validation: 0.3 days avg (stable)

## Initial Assessment
- Urgency: next-cycle
- Strategic alignment: "Engineering velocity enables market speed"
- Potential impact: high (compound effect on all missions)
- Affected divisions: All (systemic issue)

## Recommended Disposition
- [x] Proceed to opportunity validation
```

### Signal B: Quality Gate Bottleneck

The `delivery-evaluator` agent, analyzing quality evaluation patterns, independently flags:

**Artifact created:** `work/signals/2026-05-03-quality-eval-queue-backlog.md`

```markdown
# Signal: Quality Evaluation Queue Backlog Growing

## Observation
Quality evaluation turnaround has increased 125% quarter-over-quarter. Root causes:
1. Number of active missions increased 40% but eval agent capacity unchanged
2. 23% of evaluations require ESCALATE → human review (up from 8%)
3. No automated pre-screening to filter trivial vs. complex evals

The ESCALATE rate increase correlates with 3 new agent types onboarded in Q1 that 
produce more architecturally novel output.
```

### Signal C: Process Signal from Execution

A `coding-agent` files a signal after waiting 3 days for a release approval:

**Artifact created:** `work/signals/2026-05-05-release-approval-wait-time.md`

```markdown
# Signal: Release Approval Wait Time Blocking Delivery

## Observation
Mission MISSION-2026-018 had all quality evaluations passed on Monday. Release 
contract submitted Monday afternoon. Human approval received Thursday morning. 
The approver (Engineering Manager) was the single approval point for 4 concurrent 
missions. No backup approver configured.
```

> **Key principle in action:** Every agent is a sensor. The operating model states: "You don't need permission to observe and signal." Three agents across three layers independently surfaced the same underlying problem.

---

## Phase 2: Signal Aggregation & Pattern Alert

**Layer:** Steering · **Loop:** Continuous Sensing · **Agent type:** `signal-aggregation`

The `signal-aggregation` agent compiles the weekly digest and immediately identifies a converging pattern:

**Artifact created:** `work/signals/digests/2026-W19-digest.md`

```markdown
# Signal Digest: Week 2026-W19

## Pattern Alerts

### Pattern Alert: Deployment Pipeline Systemic Bottleneck
- Signals involved: 5 (3 this week + 2 from prior weeks)
- First signal: 2026-04-08 (quality eval turnaround from feature lifecycle mission)
- Latest signal: 2026-05-05
- Pattern description: Deployment cycle time degrading across all missions. 
  Multiple independent indicators: fleet metrics, quality queue analysis, 
  and direct execution agent observations all converge.
- Root cause hypothesis: Quality eval capacity hasn't scaled with mission volume; 
  human approval bottleneck has single-point-of-failure; no automated pre-screening.
- Recommended action: Evolution Proposal — process improvement
- Urgency: high — affects every active and future mission

## Recommended Actions for Strategy Layer
| Priority | Action | Related Signals |
|----------|--------|----------------|
| P1 | Evolution proposal for deployment pipeline optimization | 5 converging signals |
```

**Handover:** The Steering Layer's `org-evolution-proposer` agent picks up the P1 recommendation from the digest.

---

## Phase 3: Evolution Proposal

**Layer:** Steering · **Loop:** Structural Proposals · **Agent type:** `org-evolution-proposer`

Unlike a feature mission (which starts with a Mission Brief from Strategy), this is a **structural change to the operating model itself**. It requires an Evolution Proposal — the Steering Layer's mechanism for proposing organizational changes.

**Artifact created:** Submitted as PR `evolution/EVO-2026-008-deployment-pipeline-optimization`  
**Template:** `org/0-steering/_TEMPLATE-evolution-proposal.md`

```markdown
# Evolution Proposal: Deployment Pipeline Optimization

## Proposal ID: EVO-2026-008
## Category: Process improvement
## Status: draft
## Trigger: work/signals/digests/2026-W19-digest.md (Pattern Alert: Deployment Pipeline)

## Summary
Deployment cycle time has degraded to 3.5× industry benchmark, primarily due to 
quality eval bottleneck and single-point-of-failure human approval. This proposal 
recommends three changes: automated quality pre-screening, backup approver policy, 
and quality eval agent scaling.

## Current State
- Quality eval turnaround: 1.8 days (target: < 0.5 days)
- Human approval wait: 1.4 days (target: < 0.5 days)
- ESCALATE rate: 23% (target: < 10%)
- Single approver per release contract, no backup configured

## Proposed Changes

### Change 1: Automated Quality Pre-Screening
Add an automated pre-screening step before full quality evaluation. PRs that pass 
all automated checks (tests, linting, security scanning, policy compliance checklist) 
get a "pre-screened" label. Pre-screened PRs get priority in the eval queue and 
can use a streamlined evaluation (skip policies already verified by automation).

Requires update to: `org/4-quality/policies/delivery.md`

### Change 2: Backup Approver Policy
Require all release contracts to have a primary AND backup approver. If the primary 
doesn't respond within 4 hours during business hours, the backup is automatically 
notified. After 8 hours, the backup can approve.

Requires update to: `org/4-quality/policies/delivery.md`, CODEOWNERS

### Change 3: Quality Eval Agent Scaling
Increase quality eval agent pool capacity by 50% to match the 40% increase in 
active missions. Add auto-scaling trigger: if eval queue depth > 5 for > 2 hours, 
spin up additional eval agents.

Requires update to: Fleet configs for active missions, Orchestration AGENT.md

### What Stays the Same
- Quality policies themselves (security, architecture, etc.) — unchanged
- Progressive rollout requirements — unchanged
- Human approval requirement for releases — unchanged (but adds backup path)
- Quality evaluation rigor — unchanged (pre-screening supplements, doesn't replace)

## Evidence
### Signal Pattern
- 5 converging signals from 3 layers over 4 weeks
- Deployment cycle time: 4.2 days avg (industry benchmark: 1.2 days)
- Quality eval turnaround: 1.8 days (was 0.8 days one quarter ago)
- ESCALATE rate: 23% (was 8% before new agent types onboarded)

### Data
- 12 missions analyzed in Q1 2026
- Bottleneck accounts for 76% of total cycle time (3.2 of 4.2 days)
- Estimated improvement: 60-70% reduction in cycle time

## Impact Assessment
| Layer | Impact | Description |
|-------|--------|-------------|
| Steering | low | No structural change to steering process |
| Strategy | low | Faster outcomes; no process change for strategy |
| Orchestration | medium | Fleet configs updated; new scaling triggers |
| Execution | low | Faster feedback loops; no change to execution process |
| Quality | high | New pre-screening step; policy updates; agent scaling |

## Rollback Plan
- Reversible? yes
- Mechanism: Revert the policy PR + fleet config PR
- Timeline: Within 1 hour
- Risks: Temporary queue backlog during rollback, but no data loss

## Success Metrics
| Metric | Baseline | Target | Method | Timeline |
|--------|---------|--------|--------|----------|
| Deployment cycle time | 4.2 days | < 1.5 days | Fleet performance analytics | 4 weeks |
| Quality eval turnaround | 1.8 days | < 0.5 days | Eval queue metrics | 2 weeks |
| Human approval wait | 1.4 days | < 0.5 days | PR approval analytics | 2 weeks |
| ESCALATE rate | 23% | < 12% | Quality eval reports | 4 weeks |

## Implementation Plan
| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Update delivery.md policy (pre-screening + backup approver) | Quality agent | Week 1 |
| 2 | Implement pre-screening automation | Execution agent | Week 1-2 |
| 3 | Update CODEOWNERS for backup approver support | Orchestration | Week 1 |
| 4 | Scale quality eval agent pool | Orchestration | Week 1 |
| 5 | Roll out to 1 division (pilot) | Orchestration | Week 2 |
| 6 | Measure pilot results | Fleet performance monitor | Week 3 |
| 7 | Roll out to all divisions | Orchestration | Week 4 |

## Alternatives Considered
| Alternative | Pros | Cons | Why Not Chosen |
|------------|------|------|----------------|
| Remove human approval for small releases | Fastest improvement | Unacceptable risk reduction | Policy requires human judgment for production |
| Hire more human reviewers | Addresses approval bottleneck | Doesn't fix eval bottleneck; slow to implement | Agents can scale faster |
| **Do nothing** | No effort | Problem compounds as missions increase | Unacceptable — all missions affected |
```

---

## Phase 4: Executive Review

**Layer:** Steering · **Loop:** Structural Proposals · **Human checkpoint**

The Evolution Proposal lands as a PR. Per the evolution proposal template, "Process improvement" category requires **COO + CTO** approval.

**Review process:**
1. **CTO** reviews the technical aspects: pre-screening approach, agent scaling, automation feasibility. Approves with one condition: "Add a metric for false-negative pre-screening (PRs that pass pre-screen but fail full eval) — we need to ensure rigor isn't silently degraded."
2. **COO** reviews the process aspects: backup approver policy, rollout plan, rollback plan. Approves as-is.

The `org-evolution-proposer` agent adds the false-negative metric to the success metrics table and the proposal is merged. ✅

**Status change:** EVO-2026-008 moves from `draft` → `approved`.

> **This is the key difference from a feature mission:** The approval came from the Steering Layer (CxO level), not the Strategy Layer (VP level). Evolution proposals change the operating model — they require higher authority.

---

## Phase 5: Implementation Mission

**Layer:** Strategy → Orchestration → Execution · **Loop:** Build

The approved evolution proposal is now translated into a standard mission for execution. The `product-strategy` agent creates a mission brief — but this mission produces **policy documents and automation**, not product code.

### 5a. Mission Brief

**Artifact created:** `work/missions/deployment-pipeline-optimization/BRIEF.md`

```markdown
# Mission Brief: Deployment Pipeline Optimization

## Mission ID: MISSION-2026-024
## Status: approved

## Origin
- Signal(s): 5 converging signals (deployment cycle time, quality eval queue, approval wait)
- Evolution Proposal: EVO-2026-008 (approved by CTO + COO)
- Strategic alignment: "Engineering velocity enables market speed"

## Objective
Reduce deployment cycle time from 4.2 days to < 1.5 days by implementing automated 
quality pre-screening, backup approver policy, and quality eval agent scaling.

## Scope
### In Scope
- Update delivery.md policy with pre-screening rules and backup approver requirement
- Implement automated pre-screening workflow
- Update CODEOWNERS for backup approver support
- Scale quality eval agent pool (+50% capacity)
- Pilot rollout to one division, then all

### Out of Scope
- Changes to quality standards themselves (rigor maintained)
- Changes to security or architecture policies
- Removal of human approval requirement

## Divisions Involved
| Division | Role | Contribution |
|----------|------|-------------|
| Engineering Foundation | Primary | Pre-screening automation, CODEOWNERS updates |
| Quality & Security Engineering | Supporting | Policy updates, eval agent scaling |

## Outcome Contract
Reference: work/missions/deployment-pipeline-optimization/OUTCOME-CONTRACT.md
```

### 5b. Fleet Configuration

**Artifact created:** `org/2-orchestration/fleet-configs/deployment-pipeline-optimization.md`

```markdown
## Streams

### Stream: policy-updates
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Quality & Security Engineering |
| Exclusive | yes |

Working paths:
- org/4-quality/policies/delivery.md
- CODEOWNERS

Quality policies:
- delivery (meta: policy updating itself)
- architecture (for automation design)

### Stream: pre-screening-automation
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Engineering Foundation |
| Exclusive | yes |

Working paths:
- .github/workflows/pre-screening.yml
- src/automation/quality-prescreening/

Quality policies:
- architecture
- security
- delivery

### Stream: agent-scaling-config
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Engineering Foundation |
| Exclusive | yes |

Working paths:
- org/2-orchestration/AGENT.md (scaling trigger section)
- org/2-orchestration/fleet-configs/ (active configs)

Quality policies:
- delivery
- architecture
```

---

## Phase 6: Execution — Policy & Process Changes

**Layer:** Execution · **Loop:** Build · **Agent types:** `coding-agent`

### Stream 1: Policy Updates

The `coding-agent` updates `org/4-quality/policies/delivery.md`:

```markdown
## Additions to delivery.md

### Pre-Screening (New Section)
Before full quality evaluation, all PRs undergo automated pre-screening:
1. All tests pass (unit, integration)
2. Linting and formatting clean
3. Security scanning clean (no new vulnerabilities)
4. Policy compliance checklist auto-verified where possible

PRs that pass pre-screening receive the `pre-screened` label and enter 
the priority eval queue. Pre-screened PRs may use streamlined evaluation 
for policies already verified by automation.

Pre-screening does NOT replace full evaluation. It prioritizes the queue 
and eliminates repeated checking of automatable criteria.

### Backup Approver Requirement (New Section)
All release contracts must designate:
- Primary approver (CODEOWNERS-defined role)
- Backup approver (must be a different individual with equivalent authority)

Escalation timeline:
- T+0: Primary approver notified
- T+4h (business hours): Backup approver notified
- T+8h (business hours): Backup approver may approve independently
```

The agent also updates `CODEOWNERS` to support backup approver designations.

### Stream 2: Pre-Screening Automation

The `coding-agent` implements the automated pre-screening workflow:
- GitHub Actions workflow triggered on PR creation
- Runs test suite, linting, security scan, and policy checklist
- Applies `pre-screened` label on pass
- Applies `needs-attention` label on fail with detailed report
- Integrates with the quality eval queue (pre-screened PRs get priority)

### Stream 3: Agent Scaling Configuration

The `coding-agent` updates orchestration configuration:
- Quality eval agent pool capacity increased from 4 to 6
- Auto-scaling trigger added: if eval queue depth > 5 for > 2 hours, scale to 8
- Auto-scale-down: if queue depth < 2 for > 4 hours, return to baseline

---

## Phase 7: Meta-Quality Evaluation

**Layer:** Quality · **Loop:** Build · **Agent types:** `delivery-evaluator`, `architecture-review`

This is the most interesting quality evaluation in this example: **evaluating changes to the quality system itself.**

### The Meta-Quality Challenge

When a `coding-agent` updates `delivery.md`, the `delivery-evaluator` — which enforces delivery policy — is being asked to evaluate changes to its own policy. The framework handles this through cross-policy evaluation:

1. **The `delivery-evaluator`** cannot evaluate changes to its own policy (conflict of interest). Instead, the `architecture-review` agent evaluates the delivery policy changes for structural consistency and coherence.

2. **Cross-policy consistency check:** The `architecture-review` agent verifies that the new pre-screening rules don't contradict any other quality policy. For example: does the "streamlined evaluation" clause risk bypassing security checks? The agent confirms that pre-screening explicitly states it "does NOT replace full evaluation" — PASS.

3. **The `delivery-evaluator`** evaluates the pre-screening automation code (stream 2) against the existing delivery policy — the automation must correctly implement the policy it's designed to enforce.

**Evaluation results:**

| Stream | Evaluator | Verdict | Notes |
|--------|-----------|---------|-------|
| Policy updates | `architecture-review` | PASS WITH NOTES | Suggest adding examples to backup approver section |
| Pre-screening automation | `delivery-evaluator` | PASS | Automation correctly implements policy clauses |
| Agent scaling config | `architecture-review` | PASS | Scaling triggers are reasonable |

> **Improvement signal:** The `architecture-review` agent files a signal: "There is no formal process for cross-policy consistency checks when policies are updated. This was handled ad-hoc. Recommend adding a 'policy update' evaluation protocol." Signal: `work/signals/2026-05-12-policy-update-evaluation-protocol.md`

---

## Phase 8: Pilot Rollout

**Layer:** Orchestration → Execution · **Loop:** Ship · **Agent types:** `release-coordinator`, `fleet-performance-monitor`

Unlike a feature release with progressive percentage rollout, this is a **process change rollout by division**. The `release-coordinator` creates a release contract with a division-based progressive rollout:

**Artifact created:** `work/releases/2026-05-14-deployment-pipeline-optimization.md`

```markdown
# Release Contract: Deployment Pipeline Optimization v1.0

## Progressive Rollout Plan
| Stage | Target | Duration | Health Criteria | Rollback Trigger |
|-------|--------|----------|-----------------|-----------------|
| Pilot | Engineering Foundation division only | 2 weeks | Cycle time < 2 days; no quality regressions | Quality eval false-negative rate > 5% |
| Expansion | All divisions | Ongoing | Cycle time < 1.5 days | Quality eval false-negative rate > 3% |

## Pre-Deployment Checklist
- [x] Policy updates reviewed and merged
- [x] Pre-screening automation tested in staging
- [x] Backup approvers designated for all active missions
- [x] Quality eval agent pool scaled
- [x] Monitoring dashboard updated with new metrics:
  - Pre-screening pass/fail rates
  - Quality eval queue depth
  - False-negative rate (pre-screen pass → eval fail)
  - Backup approver activation rate
- [ ] Release contract reviewed by COO + CTO
```

**Human checkpoint:** COO + CTO approve the release contract (consistent with the evolution proposal approval authority). ✅

### Pilot Execution

The changes are applied to the Engineering Foundation division first:
- Pre-screening automation activated for their PRs
- Backup approvers configured for their release contracts
- Quality eval agents prioritize pre-screened PRs from this division

**Pilot results (2 weeks):**

| Metric | Baseline | Pilot Result | Target |
|--------|---------|--------------|--------|
| Deployment cycle time | 4.2 days | 1.8 days | < 1.5 days |
| Quality eval turnaround | 1.8 days | 0.6 days | < 0.5 days |
| Human approval wait | 1.4 days | 0.4 days | < 0.5 days |
| Pre-screening pass rate | N/A | 78% | — |
| False-negative rate | N/A | 2.1% | < 5% (pilot) / < 3% (expansion) |
| Quality eval ESCALATE rate | 23% | 14% | < 12% |

**Assessment:** Cycle time improved 57% (4.2 → 1.8 days). Not yet at the 1.5-day target, but significant improvement. The remaining gap is in eval turnaround (0.6 vs. 0.5 target). The ESCALATE rate decreased but is still above target — expected to improve as eval agents learn the new patterns.

**Decision:** Proceed to full rollout with monitoring.

---

## Phase 9: Full Rollout & Measurement

**Layer:** Orchestration · **Loop:** Ship → Operate · **Agent types:** `fleet-performance-monitor`, `release-coordinator`

The changes are rolled out to all divisions. The `fleet-performance-monitor` tracks metrics across the entire fleet for 4 weeks.

**Artifact created:** `work/missions/deployment-pipeline-optimization/OUTCOME-REPORT.md`

```markdown
# Outcome Report: Deployment Pipeline Optimization

## Targets vs. Actuals (4 weeks post full rollout)

| Metric | Baseline | Target | Actual | Verdict |
|--------|---------|--------|--------|---------|
| Deployment cycle time | 4.2 days | < 1.5 days | 1.3 days | met |
| Quality eval turnaround | 1.8 days | < 0.5 days | 0.4 days | met |
| Human approval wait | 1.4 days | < 0.5 days | 0.3 days | met |
| ESCALATE rate | 23% | < 12% | 11% | met |
| False-negative rate | N/A | < 3% | 1.8% | met |

## Overall improvement: 69% reduction in deployment cycle time (4.2 → 1.3 days)

## Lessons Learned

### What worked well
- Pre-screening eliminated 78% of redundant checks in full evaluations
- Backup approver policy resolved the single-point-of-failure immediately
- Division-based pilot rollout caught tuning needs before full deployment

### What didn't work as expected
- ESCALATE rate only dropped to 11% (target: < 12%) — the new agent types still 
  produce novel patterns. This is a feature, not a bug — novel patterns SHOULD be 
  escalated. Consider adjusting the target.
- Pre-screening false-negative rate varies by division (0.5% to 3.2%) — divisions 
  with more complex architectures have higher false-negative rates

### Policy Observations
- Pre-screening concept should be considered for addition to other policies 
  (e.g., security pre-screening before full security eval)
- Backup approver policy is working well — consider making it a universal requirement 
  (not just release contracts)
```

---

## Phase 10: Evolution Closure & New Signals

**Layer:** Steering · **Loop:** Strategic Recalibration · **Agent type:** `org-evolution-proposer`, `transformation-health`

### Evolution Proposal Closure

The `org-evolution-proposer` updates EVO-2026-008 status to `implemented` and records the results:

```markdown
## Implementation Status: IMPLEMENTED
- All success metrics met
- Changes permanent (integrated into standard operating procedures)
- Monitoring continues via fleet performance dashboards
```

### Transformation Health Assessment

The `transformation-health` agent evaluates the broader health of this transformation:

- **Adoption:** 100% of divisions using pre-screening within 4 weeks ✅
- **Sustainability:** Metrics stable in weeks 3–4, no regression ✅
- **Side effects:** Two positive side effects discovered:
  1. Pre-screening CI pipeline also catches dependency vulnerabilities earlier
  2. Backup approver conversations led to better knowledge sharing between leads

### New Signals Generated

| Signal | Category | Description |
|--------|----------|-------------|
| Pre-screening concept for security policy | process | Extend pre-screening approach to security evaluations |
| Backup approver as universal policy | process | Expand beyond release contracts to all human approval points |
| Policy update evaluation protocol needed | process | Formalize cross-policy consistency checks |
| Division-specific false-negative calibration | technical | Pre-screening thresholds may need per-division tuning |
| ESCALATE target may need revisiting | process | 12% target may be too aggressive for organizations with rapid agent onboarding |

These signals enter the next weekly digest, potentially triggering further evolution proposals. The company improves itself through its own mechanisms.

---

## How This Example Differs from Feature Lifecycle

| Dimension | Feature Lifecycle | Company Optimization |
|-----------|------------------|---------------------|
| **Origin** | External (customer demand) | Internal (agent-detected metrics) |
| **Steering involvement** | Aggregation only | Full: sensing, proposal, executive review |
| **Key artifact** | Mission Brief | Evolution Proposal |
| **Approval authority** | VP Product | COO + CTO |
| **Output** | Product code + docs | Policies + automation + config |
| **Quality challenge** | Standard eval | Meta-quality (evaluating quality system changes) |
| **Rollout** | Percentage-based (canary → GA) | Division-based (pilot → all) |
| **Success measure** | Customer outcomes | Operational metrics |
| **Evolution mechanism** | Improvement signals | Evolution Proposal lifecycle |

---

## Key Takeaways

- **The operating model improves itself.** Agents detect systemic problems through their normal work. Signals converge. The Steering Layer proposes structural changes. Executives approve. The same build/ship/operate machinery executes the improvements.
- **Evolution Proposals are the mechanism for structural change.** They require higher approval authority than feature missions because they change the rules everyone operates under.
- **Meta-quality is a real challenge.** When the quality system evaluates changes to itself, you need cross-policy evaluation and clear conflict-of-interest rules.
- **Every agent is a sensor.** The deployment bottleneck was detected by three different agent types across three different layers — none of them were looking for it. They observed it in the course of their normal work.
- **Policies are code.** Updating a policy is the same workflow as updating product code: branch, implement, evaluate, PR, approve, merge, deploy. The delivery policy was versioned, reviewed, and progressively rolled out just like any software release.
