# Example: HR Recruiting — From Observability Alert to Hired Engineer

> **Purpose:** Walkthrough of how an operational metric anomaly detected by the observability platform triggers a full People division recruiting mission, showing that the signal→mission→fleet loop is not limited to engineering — it spans corporate functions including HR, Legal, and Finance.
>
> **Scenario:** The observability platform detects that PR review cycle time has been degrading for 21 days, exceeding SLA by 310%. Root cause analysis traces the bottleneck to two senior engineering positions that were vacated in Q4 and never backfilled. The Steering Layer authorizes a recruiting mission. The People division — using the Workforce Planner Agent, Recruiting Coordinator Agent, and HR Generalist Agent — executes the hiring pipeline under human oversight at every consequential decision point.

---

## Why This Example Is Different

The [feature lifecycle example](generic-feature-lifecycle.md) traces external demand into product code. The [company optimization example](company-optimization-lifecycle.md) shows internal metrics triggering policy changes. This example shows a third path:

- **Origin:** Observability platform auto-files the signal — no human noticed first
- **Primary division:** People — a corporate function, not an engineering division
- **Supporting divisions:** Legal & Compliance (jurisdiction + offer review), Finance & Procurement (budget confirmation)
- **Challenge:** The binding constraint is human capacity, not technical debt
- **Unique mechanism:** The outcome is measured back in the observability platform — the same metric that triggered the mission validates its success

This exercises the **corporate function layer** of the operating model: People, Legal, and Finance divisions working together with human-gated checkpoints at every consequential decision.

---

## Phase 1: Automated Signal Detection

**Layer:** Observability Platform (automated) · **Loop:** Operate · **Source:** Observability anomaly detector

The observability platform, continuously monitoring DORA metrics across all divisions, detects a sustained anomaly. It automatically files a signal to `work/signals/` — no human agent is involved:

**Artifact created:** `work/signals/2026-02-20-pr-review-cycle-time-bottleneck.md`

```markdown
# Signal: PR Review Cycle Time Exceeding SLA — Engineering Capacity Gap

## Source
- Category: internal
- Source system: Observability Platform — DORA Metrics Dashboard
- Source URL/reference: CONFIG.yaml → integrations.observability (primary-observability)
- Confidence: high
- Author: observability-platform (automated signal via anomaly detection)

## Observation
The observability platform detected a sustained degradation in PR review cycle time
across the Engineering Foundation and AI & Intelligence divisions over the past 21 days.

Metrics (P95, rolling 7-day):
| Week    | Cycle Time P95 | SLA Target | Variance |
|---------|----------------|------------|---------- |
| 2026-W05| 3.2 days       | ≤ 1 day    | +220%    |
| 2026-W06| 3.8 days       | ≤ 1 day    | +280%    |
| 2026-W07| 4.1 days       | ≤ 1 day    | +310%    |

Additional signals from the same query window:
- PR queue depth: 47 open PRs awaiting first review (baseline: 12)
- Reviewer utilization: 3 active senior reviewers handling load for 5–7
- Downstream impact: 6 security patches in Automated Security Response mission
  blocked pending review

Root cause hypothesis (from platform anomaly classifier):
Insufficient senior engineering reviewer capacity. Two senior engineers left
in Q4 2025 and have not been backfilled.

## Initial Assessment
- Urgency: immediate
- Strategic alignment: autonomy-maturity (review loops are throughput constraints);
  trust-is-product (blocked security patches erode trust posture)
- Potential impact: high
- Affected divisions: Engineering Foundation, AI & Intelligence, People (action required)

## Recommended Disposition
- [x] Proceed to opportunity validation
```

> **Key principle in action (Rule 9b — consume from observability before acting):** The signal is grounded entirely in live metric data — three weeks of P95 cycle time, queue depth, and downstream impact — not in human anecdote. The anomaly classifier's root cause hypothesis ("two unfilled seats") is labeled as hypothesis, not conclusion. The Workforce Planner Agent will verify it before any action is taken.

> **Key principle in action (Rule 7 — file signals):** Agents treated as sensors. Here, the observability platform itself is the sensor. Automated signals filed at `work/signals/` carry the same authority as human-filed signals — `source: observability-platform` identifies their origin.

---

## Phase 2: Signal Aggregation & Authorization

**Layer:** Steering · **Loop:** Continuous Sensing · **Agent type:** `signal-aggregation`, `org-evolution-proposer`

The weekly Steering signal digest picks up the observability signal. Because the impact is immediate (security patches blocked), the Steering Layer fast-tracks authorization rather than deferring to the next planning cycle:

**Artifact created:** `work/signals/digests/2026-W08-digest.md` _(excerpt)_

```markdown
# Signal Digest: Week 2026-W08

## Pattern Alerts

### Immediate: Engineering Reviewer Capacity Bottleneck
- Signal: work/signals/2026-02-20-pr-review-cycle-time-bottleneck.md
- Pattern: Single signal, but immediate downstream impact (6 security patches blocked)
- Root cause hypothesis: 2 unfilled senior engineer seats (observability-platform)
- Recommended action: Authorize People division recruiting mission
- Urgency: immediate — security patch backlog is an active trust risk
- Note: Short-term bridge measure for Orchestration Layer to evaluate:
  can agent-assisted first-pass review reduce human reviewer load while hiring proceeds?

## Recommended Actions for Strategy Layer
| Priority | Action                                          |
|----------|-------------------------------------------------|
| P0       | Authorize MISSION: engineering-reviewer-capacity |
| P1       | Orchestration: assess agent bridge measure      |
```

**Human checkpoint — Steering executive reviews and authorizes.** The authorization to open a recruiting mission is a human decision; the Steering Layer agent prepares the recommendation, the executive approves it.

---

## Phase 3: Mission Brief

**Layer:** Strategy · **Loop:** Discover · **Agent type:** `discovery-agent`

The Discovery Agent translates the authorized signal into a mission brief. Note that **People is the primary division** — this is not an engineering mission:

**Artifact created:** `work/missions/engineering-reviewer-capacity/BRIEF.md`

```markdown
# Mission Brief: Engineering Reviewer Capacity Expansion

## Mission ID: MISSION-2026-010
## Status: proposed
## Design required: false (recruiting mission — no novel architecture patterns)

## Origin
- Signal(s): work/signals/2026-02-20-pr-review-cycle-time-bottleneck.md
- Strategic alignment: autonomy-maturity; trust-is-product
- Sponsor: Head of Engineering (or CTO)

## Objective
Hire 2 senior engineers with strong code review expertise within 60 days,
restoring PR review cycle time to ≤ 1 day P95 and unblocking the 6 security
patches currently queued in the Automated Security Response mission.

## Scope
### In Scope
- Workforce capacity analysis validating the headcount gap and business case
- Job description drafting for "Senior Engineer — Platform Review"
- Sourcing strategy and outreach plan
- Candidate screening and interview pipeline coordination
- Interview process design for the code review competency
- Shortlist preparation and offer material drafts (offers require human approval)
- Onboarding plan for new hires

### Out of Scope
- Compensation decisions (Finance & Procurement + People Division Lead)
- Employment contracts (Legal & Compliance reviews all offer letters)
- Architecture changes to the review process (separate mission if needed)
- Agent fleet changes to compensate for the gap (Orchestration Layer decision)

## Divisions Involved
| Division             | Role       | Contribution                                    |
|----------------------|------------|-------------------------------------------------|
| People               | Primary    | Workforce analysis, recruiting, offer prep      |
| Engineering Foundation | Consulting | Technical criteria, technical interviewers     |
| Finance & Procurement| Supporting | Budget confirmation, compensation benchmarks    |
| Legal & Compliance   | Supporting | Jurisdiction compliance, offer letter review    |

## Outcome Contract
| Metric                      | Target  | Measurement                        | Deadline   |
|-----------------------------|---------|-------------------------------------|------------|
| Senior engineers hired      | 2       | Signed offer letters                | 2026-04-21 |
| Time-to-first-shortlist     | ≤ 14 d  | Date of shortlist PR                | 2026-03-06 |
| PR review cycle time P95    | ≤ 1 day | Observability platform DORA dashboard | 2026-05-05 |
| Blocked security patches    | 6/6     | Automated Security Response STATUS.md | 2026-04-28 |

## Human Checkpoints
1. Workforce analysis approval — headcount confirmed before sourcing begins
2. Job description approval — JD approved before posting
3. Shortlist review — hiring manager selects candidates for final round
4. Offer approval — People Division Lead + Finance + Legal approve before extending
5. Onboarding activation — People Division Lead activates onboarding for each hire
```

**Human checkpoint — Strategy Layer human reviews and approves the Mission Brief.** The scope, outcome contract, and division involvement must be human-approved before the Orchestration Layer builds the fleet config.

---

## Phase 4: Fleet Configuration

**Layer:** Orchestration · **Loop:** Build · **Agent type:** `mission-orchestrator`

The Mission Orchestrator decomposes the approved brief into three sequential/parallel agent streams. The key architectural decision: **Stream 2 cannot start until Stream 1 is human-approved** — sourcing must not begin before the headcount gap is validated with data.

**Artifact created:** `org/2-orchestration/fleet-configs/engineering-reviewer-capacity.md` _(excerpt)_

```markdown
## Streams

### Stream 1: Workforce Capacity Analysis
| Field       | Value                                |
|-------------|--------------------------------------|
| Agent pool  | people-workforce-planning            |
| Agent type  | exec-workforce-planner-agent         |
| Division    | people                               |
| Gate        | blocks Stream 2 until human-approved |

Working paths:
- work/signals/2026-02-20-pr-review-cycle-time-bottleneck.md (read)
- Observability platform (via MCP — live metric queries)
- work/missions/engineering-reviewer-capacity/ (write: WORKFORCE-ANALYSIS.md)

### Stream 2: Recruiting Pipeline
| Field       | Value                                    |
|-------------|------------------------------------------|
| Agent pool  | people-recruiting                        |
| Agent type  | exec-recruiting-coordinator-agent        |
| Division    | people                                   |
| Gate        | activates after Stream 1 human-approved  |

Working paths:
- ATS system (via MCP — candidate pipeline)
- Job board integrations (via MCP — posting, pending human JD approval)
- work/missions/engineering-reviewer-capacity/ (write: pipeline status)

### Stream 3: Interview Process & Offer Management
| Field       | Value                                              |
|-------------|----------------------------------------------------|
| Agent pool  | people-hr-operations                               |
| Agent type  | exec-hr-generalist-agent                           |
| Division    | people                                             |
| Gate        | activates in parallel with Stream 2 (design can   |
|             | proceed while sourcing runs); offer stage blocked  |
|             | on Finance budget confirmation + Legal clearance   |

## Dependencies
| From         | To           | Type    |
|--------------|--------------|---------|
| Stream 1     | Stream 2     | blocks  |
| Finance & Procurement | Stream 3 (offer) | blocks |
| Legal & Compliance    | Stream 3 (offer) | blocks |
```

---

## Phase 5: Stream 1 — Workforce Capacity Analysis

**Layer:** Execution · **Loop:** Build · **Agent type:** `exec-workforce-planner-agent`

The Workforce Planner Agent queries the observability platform directly (via MCP) rather than relying on the signal alone:

```markdown
## Workforce Capacity Analysis — MISSION-2026-010

### Step 1: Live Metric Verification
Query result — PR review cycle time P95 (last 28 days, Engineering Foundation + AI & Intelligence):

  2026-01-24: 1.1 days
  2026-01-31: 1.6 days  ← first breach
  2026-02-07: 2.9 days
  2026-02-14: 3.8 days
  2026-02-20: 4.1 days  ← current (signal date)

Signal hypothesis confirmed: degradation began ~2026-01-24.

### Step 2: Headcount Cross-Reference (HRIS)
Engineering Foundation authorized headcount: 7 senior engineers
Engineering Foundation current headcount: 5 senior engineers
Vacated: 2 (Q4 2025 departures, roles unfilled 63 days as of signal date)

### Step 3: Capacity Modeling
At 5 reviewers, throughput capacity = ~18 PR reviews/week.
Current PR arrival rate = ~27 reviews/week.
Queue growth rate = +9 reviews/week → explains the observed backlog trajectory.

At 7 reviewers: capacity = ~25 reviews/week.
Note: 7 reviewers would be near capacity at current load.
Recommendation: Hire 2 to restore to 7; monitor whether mission load continues
to grow (flag for next cycle if >30 PRs/week sustained).

### Step 4: Bridge Measure Assessment
Question: Can agent-assisted first-pass review reduce human load while hiring proceeds?
Assessment: Automated pre-screening (linting, test pass, policy checklist) could
eliminate human reviewer time on ~30% of PRs. At current load, this recovers
~8 reviews/week — not enough to close the 9/week gap alone, but meaningful
as a bridge measure.
Recommendation: Implement bridge measure in parallel with hiring (Orchestration
Layer to create separate task).

### Recommendation
Hire 2 senior engineers. Role: "Senior Engineer — Platform & Code Review."
Core competency: distributed systems experience + demonstrated code review depth.
Timeline: 60 days to offer acceptance.
```

**Human checkpoint 1 — People Division Lead + Sponsor review the analysis.** They confirm the headcount recommendation, direct Finance & Procurement to confirm budget, and direct Legal & Compliance to confirm jurisdiction availability. Only after this approval does the Recruiting Coordinator Agent begin sourcing.

---

## Phase 6: Stream 2 — Recruiting Pipeline

**Layer:** Execution · **Loop:** Build · **Agent type:** `exec-recruiting-coordinator-agent`

With the workforce analysis approved, the Recruiting Coordinator Agent activates:

### 6a. Job Description Draft

```markdown
# Job Description: Senior Engineer — Platform & Code Review (DRAFT — Pending Approval)

## About the Role
You will be a key reviewer and technical leader in our Engineering Foundation division,
responsible for maintaining the quality and velocity of our agent-driven development
pipeline. Your reviews are the human checkpoint that keeps our agentic operating model
safe, scalable, and trustworthy.

## What You'll Do
- Review 5–10 PRs per day across Engineering Foundation and AI & Intelligence divisions
- Establish and maintain code review standards for agent-generated code
- Mentor junior engineers and agents on review quality
- Identify patterns in agent output that indicate instruction or model issues
- Collaborate with Quality & Security Engineering on review criteria evolution

## What We're Looking For
- 6+ years of software engineering experience; 2+ years as a primary reviewer on a
  large codebase
- Experience reviewing agent-generated or auto-generated code (preferred)
- Distributed systems background; familiarity with event-driven architectures
- Strong written communication — your review comments are the primary feedback loop
  for agent improvement
- Track record of raising code quality across a team, not just blocking bad code
```

**Human checkpoint 2 — People Division Lead + Engineering Foundation lead approve the JD.** No posting until both sign off.

### 6b. Sourcing & Screening

The Recruiting Coordinator Agent executes the approved sourcing strategy across approved channels. Screening uses a structured rubric drawn from the JD:

```markdown
## Candidate Screening Rubric

| Criterion                        | Weight | Evaluation Method              |
|----------------------------------|--------|-------------------------------|
| Distributed systems depth        | 25%    | Technical phone screen          |
| Code review volume & scope       | 25%    | Portfolio / references          |
| Agent/generated code experience  | 20%    | Direct question                 |
| Written communication quality    | 20%    | CV + cover note analysis        |
| Culture and values alignment     | 10%    | Values interview                |

Agents never score candidates on subjective "culture fit" without a structured rubric.
Every evaluation criterion is explicit, weighted, and applied consistently.
```

After 11 business days, the Recruiting Coordinator Agent produces a shortlist:

```markdown
## Candidate Shortlist — MISSION-2026-010 (Revision 1)

| Candidate | Screening Score | Standout Evidence |
|-----------|-----------------|-------------------|
| A         | 87/100          | 4y reviewing ML pipeline outputs at scale |
| B         | 84/100          | Built internal code review tooling; 3 OSS projects |
| C         | 82/100          | Deep distributed systems; newer to review focus |
| D         | 79/100          | Strong comms; strong reviewer culture ref checks |

Recommendation: advance all 4 to final technical round.
```

**Human checkpoint 3 — Hiring manager (Engineering Foundation lead) reviews shortlist.** Selects candidates A, B, and C for final round. Recruiting Coordinator Agent coordinates final interview logistics.

---

## Phase 7: Stream 3 — Interview Process & Offer Management

**Layer:** Execution · **Loop:** Build · **Agent type:** `exec-hr-generalist-agent`

Running in parallel with Stream 2 (interview process design does not require shortlist completion), the HR Generalist Agent designs the evaluation rubric for final rounds:

```markdown
## Interview Process Design — Senior Engineer, Platform & Code Review

Stage 1: Recruiter Screen (30 min) — Recruiting Coordinator Agent coordinates
Stage 2: Technical Phone Screen (60 min) — Engineering Foundation senior engineer
Stage 3: Live Code Review Exercise (90 min) — Review an actual PR from our codebase
  Rubric: accuracy of issue identification, quality of written feedback, depth vs.
  breadth balance, handling of agent-specific patterns
Stage 4: Values Interview (45 min) — People Division Lead
  Rubric: collaboration, written communication, handling disagreement, feedback culture

Note: All interview guides submitted for People Division Lead approval before use.
```

**Legal & Compliance confirms jurisdiction** — both target candidates are in jurisdictions where employer-of-record is established. No new legal entity needed. ✅

**Finance & Procurement confirms budget** — headcount budget for 2 FTE at the specified band is available within Q1 allocation. Budget envelope confirmed. ✅

### 7a. Offer Drafting

Final round results: Candidates A and B receive offers. The HR Generalist Agent drafts offer materials using the approved template:

```markdown
## Offer Draft — Candidate A (DRAFT — Pending Approval)

Role: Senior Engineer — Platform & Code Review
Level: Senior II
Division: Engineering Foundation
Compensation: [per approved band — Finance confirmed]
Start date: 2026-03-17 (proposed)
Equity: [per approved plan]
Benefits: Standard package

Cover note to candidate:
"Your experience reviewing ML pipeline outputs at scale is directly relevant to
the work we're building here — you'd be reviewing agent-generated code at the
intersection of correctness and trust. We think you'd have real impact on how
this operating model evolves."

Legal review required before sending.
```

**Human checkpoint 4 — People Division Lead + Finance & Procurement + Legal & Compliance approve both offers.** All three functions must sign off. The HR Generalist Agent routes for approval; no offer is sent until all three approvals are in the PR.

---

## Phase 8: Onboarding Plan

**Layer:** Execution · **Loop:** Build · **Agent type:** `exec-hr-generalist-agent`

On acceptance, the HR Generalist Agent drafts role-specific onboarding:

```markdown
## Onboarding Plan — Senior Engineer, Platform & Code Review

### Days 1–5: Orientation
- System access provisioning (Infrastructure Operations)
- Toolchain setup (Engineering Foundation runbook)
- Read: AGENTS.md, org/3-execution/AGENT.md, divisions/engineering-foundation/DIVISION.md
- Pair sessions with 2 existing senior reviewers (shadowed reviews only)

### Days 6–20: Supervised Review
- Review 2–3 PRs per day with mentor feedback
- Attend weekly review calibration session with Engineering Foundation lead
- Flag any patterns in agent-generated code that differ from human-generated code
  (these are signals — file to work/signals/ if recurring)

### Day 30: Independent Review Clearance
- Engineering Foundation lead sign-off: cleared for independent review
- Metrics baseline established in observability platform

### Day 60: Integration Review
- Performance check-in with People Division Lead
- Observability review: is PR cycle time P95 trending toward SLA?
```

**Human checkpoint 5 — People Division Lead activates onboarding** for both hires on their respective Day 1.

---

## Phase 9: Outcome Measurement

**Layer:** Orchestration + Observability · **Loop:** Operate · **Agent type:** `fleet-performance-monitor`

The success metric from the Mission Brief was explicitly tied to the same observability query that generated the signal. Five weeks after both hires reach Day 30 independent review clearance:

**Artifact created:** `work/missions/engineering-reviewer-capacity/OUTCOME-REPORT.md` _(excerpt)_

```markdown
## Outcome Report — MISSION-2026-010

### Targets vs. Actuals

| Metric                      | Target    | Actual      | Verdict  |
|-----------------------------|-----------|-------------|----------|
| Senior engineers hired      | 2         | 2           | ✅ met    |
| Time-to-first-shortlist     | ≤ 14 days | 11 days     | ✅ met    |
| PR review cycle time P95    | ≤ 1 day   | 0.8 days    | ✅ met    |
| Blocked security patches    | 6/6       | 6/6 merged  | ✅ met    |

### Observability Confirmation
Query: PR review cycle time P95, rolling 7-day, post hire Day 30:

  2026-04-28: 1.6 days  ← both hires in onboarding
  2026-05-05: 1.2 days
  2026-05-12: 0.9 days  ← both cleared for independent review
  2026-05-19: 0.8 days  ← stable below SLA

The same metric that triggered the mission validates its success.
The loop is closed in the observability platform.

### New Signals Generated
- Bridge measure (agent-assisted first-pass review) was partially implemented
  during hiring window — reduced review load by ~22%. Signal filed to formalize
  this as a permanent capability.
- Reviewer utilization at 7 FTE is now 88% at current load — approaching capacity.
  File signal to monitor: if mission count grows by >20%, this bottleneck recurs.
```

---

## How the Divisions Collaborated

This mission is notable for how three corporate divisions coordinated with Engineering Foundation through a single fleet config:

```
People (primary)                Legal & Compliance          Finance & Procurement
├── Workforce Planner Agent     │                            │
│   └── validates gap w/ data  │                            │
├── Recruiting Coordinator      │                            │
│   ├── JD draft ──────────────┼────────────────────────────┤─── (budget confirm)
│   ├── sourcing & screening   │                            │
│   └── shortlist ─────────────┼─ (jurisdiction confirm) ───┤
└── HR Generalist Agent         │                            │
    ├── interview design        │                            │
    ├── offer draft ────────────┼─ (offer letter review) ────┼─── (comp approval)
    └── onboarding plan         │                            │
                                └────────────────────────────┘
```

Every cross-division touchpoint was a **blocking dependency** in the fleet config — not a "nice to have." Legal and Finance could not be skipped or bypassed. Their sign-off on offers was a PR gate.

---

## Key Takeaways

- **Observability triggers People decisions.** The operating model's signal loop is not only for technical incidents. An operational metric (PR latency) triggered a People division mission — automatically, without human observation first.
- **Corporate functions are first-class divisions.** People, Legal, and Finance are modeled with the same structure as engineering divisions: DIVISION.md, agent types, quality policies, human checkpoints. They participate in fleet configs as primary or supporting parties.
- **Agents prepare, humans decide — especially in HR.** No offer was sent without three human approvals (People Division Lead + Finance + Legal). No candidate advanced to final round without hiring manager review. The agents handled every coordination and preparation task; humans owned every consequential judgment.
- **The outcome metric closes the loop.** The mission's success criterion was the same observability query that generated the signal. This is intentional — the observability platform is both the sensor and the validator.
- **Recruiting missions have the same structure as engineering missions.** Signal → digest → mission brief → fleet config → streams → human checkpoints → outcome report. The 4-loop lifecycle and the 5-layer model apply regardless of whether the output is code, a policy change, or a hire.
