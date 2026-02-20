# Fleet Configuration: Engineering Reviewer Capacity Expansion

> **Template version:** 1.0 | **Last updated:** 2026-02-19
> **Configuration for agent fleet deployment on a specific mission.**
> **Created by:** Orchestration Layer (Mission Lead + Agent Fleet Manager)

---

## Mission

| Field | Value |
|-------|-------|
| **Mission ID** | MISSION-2026-010 |
| **Mission brief** | [BRIEF.md](../../../work/missions/engineering-reviewer-capacity/BRIEF.md) |
| **Status** | proposed |

## Orchestration

| Role | Person |
|------|--------|
| **Mission Lead** | <!-- assign: orchestration fleet manager --> |
| **Fleet Manager** | <!-- assign: orchestration fleet manager --> |

---

## Streams

### Stream 1: Workforce Capacity Analysis

| Field | Value |
|-------|-------|
| **Agent pool** | people-workforce-planning |
| **Division** | `people` |
| **Exclusive** | no _(analysis is read-only; no exclusive file access needed)_ |

**Working paths:**
- `work/signals/2026-02-20-pr-review-cycle-time-bottleneck.md` (read)
- `work/missions/engineering-reviewer-capacity/` (read/write for analysis artifacts)
- Observability platform (via MCP — read-only queries)

**Agent type:** `exec-workforce-planner-agent`

**Instructions for this stream:**

1. Query the observability platform for the full 21-day PR review cycle time trend (use the metrics cited in the originating signal as the starting point; verify with live data)
2. Cross-reference with HRIS for current Engineering Foundation and AI & Intelligence headcount vs. authorized headcount
3. Model the capacity gap: how many additional senior reviewers are needed to bring the P95 cycle time to ≤ 1 day at current mission load?
4. Assess whether agent-assisted first-pass review (proposed bridge measure) would materially reduce the gap — quantify the estimate
5. Produce a **Workforce Capacity Analysis** document filed to `work/missions/engineering-reviewer-capacity/WORKFORCE-ANALYSIS.md`
6. File the analysis as a PR. Human checkpoint 1 applies: People Division Lead and Sponsor must approve before Stream 2 activates.

**Quality policies:**
- security (PII handling for employee data)
- observability (all conclusions must cite observed metrics, not estimates)

**Human checkpoints:**

| Trigger | Who | Action |
|---------|-----|--------|
| Workforce analysis draft complete | People Division Lead + Sponsor | Review and approve headcount recommendation; confirm budget envelope with Finance |

**Success metrics:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| Analysis delivered | Within 5 business days of mission activation | Date of PR open |
| Metric citation accuracy | 100% of claims backed by observability data | Human review |

---

### Stream 2: Recruiting Pipeline Execution

| Field | Value |
|-------|-------|
| **Agent pool** | people-recruiting |
| **Division** | `people` |
| **Exclusive** | no |

**Working paths:**
- `work/missions/engineering-reviewer-capacity/` (read/write for JD drafts and pipeline reports)
- ATS system (via MCP — read/write for candidate pipeline)
- Job board integrations (via MCP — write for posting, pending human approval)

**Agent type:** `exec-recruiting-coordinator-agent`

**Gate:** Stream 2 does NOT activate until Stream 1 (Workforce Capacity Analysis) is human-approved.

**Instructions for this stream:**

1. Read the approved workforce analysis from Stream 1
2. Draft a job description for "Senior Engineer — Platform & Code Review" using the approved JD template and the technical criteria provided by Engineering Foundation lead
3. Submit JD draft as PR for human approval (Human checkpoint 2)
4. On JD approval: activate sourcing on approved channels (referral program, approved job boards, targeted outreach — per procurement-approved channels only; do not use unapproved sourcing tools)
5. Screen inbound applications against the role scorecard (technical depth, code review experience, communication quality based on written materials)
6. Schedule technical phone screens with Engineering Foundation lead interviewers
7. Produce a **candidate shortlist** of ≥ 4 qualified candidates with structured evaluation rationale for each
8. Submit shortlist as PR for human checkpoint 3 (hiring manager review)
9. Coordinate logistics for final-round interviews (calendar scheduling, interview packet distribution)
10. Track pipeline weekly; file a pipeline status update to `work/missions/engineering-reviewer-capacity/PIPELINE-STATUS.md` every 5 business days

**Quality policies:**
- security (candidate data is PII — never log in plaintext; use ATS system as system of record)
- content (job posting is public-facing; apply content policy)

**Human checkpoints:**

| Trigger | Who | Action |
|---------|-----|--------|
| JD draft ready | People Division Lead + Engineering Foundation lead | Review and approve JD before posting |
| Candidate shortlist ready (≥ 4 candidates) | Hiring manager (Engineering Foundation lead) | Review shortlist; select candidates for final round |

**Success metrics:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| Time to shortlist (from sourcing activation) | ≤ 14 days | Date of shortlist PR |
| Shortlist acceptance rate | ≥ 50% advance to final round | Hiring manager decision |
| Pipeline health | ≥ 10 screened candidates in funnel | ATS tracking |

---

### Stream 3: Interview Process & Offer Management

| Field | Value |
|-------|-------|
| **Agent pool** | people-hr-operations |
| **Division** | `people` |
| **Exclusive** | no |

**Working paths:**
- `work/missions/engineering-reviewer-capacity/` (read/write for offer drafts and onboarding plan)
- HRIS (via MCP — read for role template; write for offer initiation)
- Legal & Compliance consultation channel

**Agent type:** `exec-hr-generalist-agent`

**Gate:** Stream 3 activates in parallel with Stream 2 (interview process design can happen while sourcing is underway).

**Instructions for this stream:**

1. Design the interview process for the "Senior Engineer — Platform & Code Review" role:
   - Define interview stages: recruiter screen → technical phone screen → code review live exercise → values interview
   - Draft structured interview guides for each stage with scoring rubrics for the code review competency
   - Submit interview process design for People Division Lead approval before interviews begin
2. Coordinate with Legal & Compliance to confirm jurisdiction eligibility for target candidate locations
3. Confirm budget envelope with Finance & Procurement before offer stage
4. When hiring manager selects finalists: draft offer materials (compensation package, role description, start date) using the approved template
5. Submit offer draft for human checkpoint 4 (People Division Lead + Finance + Legal approval)
6. On offer acceptance: draft onboarding plan specific to the Engineering Foundation context:
   - Days 1–5: system access, toolchain setup, pair review sessions with senior team members
   - Days 6–20: supervised review of real PRs with mentor feedback
   - Day 30: first independent review sign-off
7. Submit onboarding plan for People Division Lead activation (checkpoint 5)
8. On both hires completing Day 30: confirm review queue integration and file mission outcome data to `work/missions/engineering-reviewer-capacity/` for the outcome report

**Quality policies:**
- security (PII handling for candidates and employees; financial data in offer letters)
- content (interview guides and offer letters are formal documents)

**Human checkpoints:**

| Trigger | Who | Action |
|---------|-----|--------|
| Interview process design ready | People Division Lead | Approve before first interview |
| Offer materials drafted | People Division Lead + Finance + Legal | Approve before offer is extended |
| Onboarding plan ready | People Division Lead | Activate onboarding for each new hire |

**Success metrics:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| Offer-to-acceptance rate | ≥ 80% | Signed offer letters |
| Onboarding plan delivered | Before each hire's Day 1 | Date of plan approval |
| Day-30 review competency | Both hires cleared for independent review | Engineering Foundation lead sign-off |

---

## Dependencies

| From | To | Type |
|------|----|------|
| Stream 1 (Workforce Analysis) | Stream 2 (Recruiting) | blocks — sourcing must not begin before analysis is approved |
| Stream 2 (Recruiting) | Stream 3 (Offer Management) | informs — offer stage begins when shortlist is selected |
| Finance & Procurement | Stream 3 | blocks — budget confirmation required before offer stage |
| Legal & Compliance | Stream 3 | blocks — jurisdiction confirmation required before offers |

## Monitoring

| Parameter | Value |
|-----------|-------|
| **Quality threshold** | 0.85 minimum quality score before alert |
| **Throughput alert** | Alert if Stream 2 has < 5 screened candidates after 10 business days of sourcing |
| **Escalation policy** | People Division Lead → Steering Layer if hiring target is at risk at Day 30 |

---

## Context: Why This Demonstrates the Full Loop

This fleet config shows how the agentic operating model connects **observability → signal → mission → fleet → human outcomes**:

1. The observability platform detected a real metric anomaly (PR review latency)
2. It automatically filed a signal (`work/signals/`)
3. The Strategy Layer translated the signal into a mission brief
4. The Orchestration Layer decomposed the mission into a 3-stream fleet targeting the **People division** — a corporate function, not just engineering
5. Human checkpoints gate every consequential decision (headcount approval, JD posting, offer extension)
6. The outcome loops back to the observability platform: if the metric returns to SLA within 30 days of the hires onboarding, the mission is successful

This is the same pattern used for security incidents, product launches, and infrastructure capacity — the operating model is business-function-agnostic.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-20 | Initial configuration for MISSION-2026-010 |
