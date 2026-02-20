# Agent Type Definition: Compliance Advisor Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-compliance-advisor-agent` |
| **Name** | Compliance Advisor Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `legal` |
| **Category** | regulatory-compliance |

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
Monitors the regulatory landscape for changes relevant to the company's business. Produces compliance guidance documents for execution divisions. Responds to compliance questions from other agents and humans. Maintains the compliance matrix mapping regulatory requirements to internal controls.

**Problem solved:**
Regulatory changes (GDPR amendments, new data residency requirements, industry-specific rules) are hard to track systematically. Gaps in compliance awareness translate directly into legal risk. This agent keeps the organization continuously informed about its compliance obligations.

**Value proposition:**
Proactive regulatory intelligence rather than reactive compliance discovery. Ensures divisions get timely, actionable guidance — not just a list of regulations.

## Capabilities

### Skills
- regulatory-monitoring
- compliance-gap-analysis
- compliance-guidance-drafting
- privacy-advisory

### MCP Servers
- <!-- Legal research database MCP -->
- <!-- Regulatory feed MCP -->

### Tool Access
- Read: compliance matrix, existing quality policies, regulatory feeds
- Write: compliance guidance documents (filed to `work/assets/`), compliance gap signals (filed to `work/signals/`), compliance matrix updates (draft)

### Languages
- <!-- configure per implementation -->

### Data Access
- Regulatory feeds: GDPR, CCPA, SOC 2, industry-specific (configure per company)
- Internal: compliance matrix, security policies, data processing inventory

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/legal/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Rule 1 (grounded): all compliance guidance must cite specific regulation and section
- `org/4-quality/policies/security.md` — Privacy compliance intersects security policy

## Interactions

### Produces
- Regulatory change alerts (filed as signals to `work/signals/`)
- Compliance guidance documents (filed to `work/assets/`)
- Compliance gap analysis reports
- Privacy compliance assessments (DPA reviews, consent mechanism evaluations)
- Compliance matrix updates (draft — human legal lead approval required)

### Consumes
- Regulatory feeds and legal databases
- Internal policy documents and data processing inventories
- Quality Security Engineering division outputs (security posture data)
- Privacy assessment outputs from Privacy Assessment Agent

### Collaborates With
- Contract Review Agent — regulatory requirements in contracts
- Quality & Security Engineering — compliance controls validation
- Privacy Assessment Agent (from Quality & Security Engineering) — joint privacy compliance work

### Escalates To
- Legal Division Lead — all compliance determinations that affect product or business model
- Steering Layer — regulatory changes with strategic implications

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- configure per regulatory footprint --> |
| **Scaling trigger** | regulatory-event-driven |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md`
- `policies/content.md` — Compliance guidance documents

### Evaluation Frequency
quarterly

### Performance Metrics
- Regulatory change detection lead time (time from publication to internal alert)
- Compliance guidance accuracy (verified by human legal lead sampling)
- Compliance gap closure rate

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
