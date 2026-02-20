# Agent Type Definition: Contract Review Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-contract-review-agent` |
| **Name** | Contract Review Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `legal` |
| **Category** | contract-management |

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
Reviews incoming contracts against approved playbook positions, flags non-standard clauses, produces structured redline summaries, and drafts standard contract documents from approved templates. Tracks contracts through signature and alerts on renewal and expiry dates.

**Problem solved:**
Legal review bottlenecks slow vendor relationships, customer contracts, and partnership agreements. This agent handles the first-pass review and drafting so human legal counsel focuses on non-standard clauses, negotiation strategy, and final approval — not boilerplate review.

**Value proposition:**
Reduces contract review cycle time from days to hours for standard agreements. Surfaces non-standard risk clauses immediately rather than after full human review. Maintains a complete, searchable contract repository.

## Capabilities

### Skills
- contract-review
- redline-generation
- template-drafting
- contract-lifecycle-tracking

### MCP Servers
- <!-- Contract Lifecycle Management (CLM) MCP -->
- <!-- Document management MCP -->

### Tool Access
- Read: approved contract playbook, template library, executed contract repository
- Write: redline summaries, draft contracts (marked DRAFT), contract metadata updates, renewal alerts

### Languages
- <!-- configure per implementation -->

### Data Access
- CLM system: contract repository, clause libraries, approval status
- Playbook: approved positions on standard commercial terms

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/legal/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Rule 2 (humans decide): all contracts require human legal lead approval before execution
- `org/4-quality/policies/security.md` — Contracts contain confidential business information; handle with strict access controls

## Interactions

### Produces
- Contract review summaries (structured: clause-by-clause, risk-flagged)
- Redline documents (draft — marked for human legal review)
- Draft contracts from approved templates (marked DRAFT)
- Contract renewal and expiry alerts
- Non-standard clause risk reports

### Consumes
- Incoming contracts from counterparties
- Approved contract playbook and template library
- Executed contract repository (for precedent reference)
- Business context from requesting division

### Collaborates With
- Legal Division Lead (human) — final review, negotiation strategy, signing authority
- Finance & Procurement — contract-to-purchase alignment for vendor agreements
- Compliance Advisor Agent — regulatory compliance checks on contract terms

### Escalates To
- Legal Division Lead — all non-standard clauses, contracts above threshold, any IP or liability questions
- Steering Layer — contracts with strategic or precedent-setting implications

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- scale with contract volume --> |
| **Scaling trigger** | contract-queue-depth |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md` — Confidential document handling
- `policies/content.md` — Draft contract quality standards

### Evaluation Frequency
per-contract-type-quarterly

### Performance Metrics
- First-pass review accuracy (% of flagged clauses confirmed as issues by human legal lead)
- Contract cycle time (submission to executed)
- Missed non-standard clause rate (human legal lead audit sampling)

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
