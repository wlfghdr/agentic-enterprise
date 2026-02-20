# Agent Type Definition: Recruiting Coordinator Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-recruiting-coordinator-agent` |
| **Name** | Recruiting Coordinator Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `people` |
| **Category** | talent-acquisition |

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
Executes the talent acquisition pipeline for approved roles. Drafts job descriptions, prepares sourcing strategies, screens inbound applications against role criteria, coordinates interview scheduling logistics, and prepares candidate shortlists and interview packets for human hiring teams.

**Problem solved:**
Recruiting pipelines involve high volumes of repetitive coordination work (drafting JDs, screening CVs, scheduling interviews, tracking candidate status). This agent handles the coordination layer so human recruiters and hiring managers focus on high-judgment decisions (final interviews, offers, culture fit).

**Value proposition:**
Compresses time-to-first-shortlist from weeks to days. Ensures consistent screening criteria are applied across all candidates, reducing bias from inconsistent human review patterns.

## Capabilities

### Skills
- job-description-drafting
- candidate-screening
- interview-coordination
- pipeline-status-tracking

### MCP Servers
- <!-- ATS (Applicant Tracking System) MCP for pipeline management -->
- <!-- Calendar MCP for interview scheduling -->
- <!-- Job board MCP for posting -->

### Tool Access
- Read: approved job description templates, role leveling frameworks, interview guides
- Write: job postings (draft only — human approval before publishing), candidate evaluation summaries, interview schedules

### Languages
- <!-- configure per implementation -->

### Data Access
- ATS: candidate pipeline, application data, interview feedback
- Calendar system: interviewer availability
- HRIS: approved role requisitions and headcount budget

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/people/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Global agent rules, especially Rule 1 (grounded, not speculative — no fabricated candidate data)
- `org/4-quality/policies/security.md` — Candidate data is PII; handle with strict access controls

## Interactions

### Produces
- Draft job descriptions (for human approval before posting)
- Candidate screening summaries (structured, criteria-based)
- Interview schedules and logistics coordination
- Weekly pipeline status reports
- Candidate shortlists with evaluation rationale

### Consumes
- Approved role requisitions from HRIS
- Interview guides and evaluation rubrics
- Workforce planning report (from Workforce Planner Agent)
- Hiring manager preferences and must-have criteria

### Collaborates With
- Workforce Planner Agent — receives approved hiring plan
- HR Generalist Agent — role definition, interview process design, offer preparation
- Hiring managers (human) — shortlist review, final selection

### Escalates To
- People Division Lead — offer terms, candidate rejections requiring sensitivity
- Legal & Compliance — any compliance question about candidate assessment or background checks

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- scale with open requisition volume --> |
| **Scaling trigger** | requisition-count |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md` — PII handling mandatory
- `policies/content.md` — Job postings are public-facing content

### Evaluation Frequency
per-role-close

### Performance Metrics
- Time-to-shortlist (from requisition approval)
- Screening accuracy (% of shortlisted candidates who pass hiring manager review)
- Offer acceptance rate
- Candidate experience rating (where measurable)

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
