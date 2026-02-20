# Agent Type Definition: Procurement Agent

> **Status:** proposed | **Proposed date:** 2026-02-20
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | `exec-procurement-agent` |
| **Name** | Procurement Agent |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | execution |
| **Division** | `finance-procurement` |
| **Category** | procurement |

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
Manages the vendor sourcing and procurement lifecycle: issues RFPs/RFQs, evaluates vendor responses against defined criteria, produces vendor comparison matrices, prepares purchase order drafts, tracks vendor delivery against commitments, and monitors SaaS and toolchain spend. Routes all purchase decisions to appropriate human approvers.

**Problem solved:**
Procurement is operationally intensive — sourcing events, RFP management, vendor evaluation, PO creation. Without structured support, purchasing decisions are made ad-hoc, creating vendor sprawl, inconsistent pricing, and compliance gaps. This agent brings discipline and efficiency to the procurement process.

**Value proposition:**
Consistent, policy-compliant procurement across all divisions. Faster sourcing cycles. Better vendor visibility. Integration with registration workflows in the Integration Registry.

## Capabilities

### Skills
- rfp-drafting
- vendor-evaluation
- purchase-order-drafting
- vendor-spend-tracking
- integration-registry-coordination

### MCP Servers
- <!-- Procurement platform MCP -->
- <!-- ERP / AP MCP for PO creation -->
- <!-- Vendor portal MCP -->

### Tool Access
- Read: procurement policies, approved vendor list, spending thresholds, integration registry
- Write: RFP/RFQ documents (draft), vendor evaluation matrices, PO drafts (human-approved before submission), vendor registry updates (draft)

### Languages
- <!-- configure per implementation -->

### Data Access
- Procurement platform: active sourcing events, vendor submissions
- ERP: approved budgets, existing POs
- Integration registry (`org/integrations/`): registered tools and their status

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | `org/3-execution/AGENT.md` |
| **Division DIVISION.md** | `org/3-execution/divisions/finance-procurement/DIVISION.md` |

### Additional Context
- `AGENTS.md` — Rule 8 (integrations through governed channels): when a new tool is being procured, check `org/integrations/` and ensure registration follows the Integration Registry process
- `org/4-quality/policies/security.md` — Vendor security assessment required before procurement approval

## Interactions

### Produces
- RFP/RFQ documents (draft — human approval before sending)
- Vendor evaluation matrices with scoring rationale
- Purchase order drafts (human-approved before submission)
- Vendor performance reports
- New integration registration PRs (when procuring new tooling)

### Consumes
- Purchase requests from divisions
- Procurement policy and spending thresholds
- Integration registry (to check if a tool is already registered/approved)
- Security assessment outputs (from Quality & Security Engineering)
- Budget availability confirmation (from Budget Analyst Agent)

### Collaborates With
- Budget Analyst Agent — budget availability check before sourcing events
- Contract Review Agent — vendor contract review coordination
- Legal & Compliance — vendor terms and regulatory compliance
- Quality & Security Engineering — vendor security assessments

### Escalates To
- Finance & Procurement Division Lead — all PO approvals above threshold
- Legal & Compliance — non-standard vendor contract terms
- Steering Layer — strategic vendor relationships and sole-source justifications

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 |
| **Max instances** | <!-- scale with procurement volume --> |
| **Scaling trigger** | purchase-request-queue |
| **Cost class** | medium |

## Quality

### Applicable Policies
- `policies/security.md` — Vendor security assessment integration
- `policies/content.md` — RFP/RFQ document quality

### Evaluation Frequency
quarterly

### Performance Metrics
- Procurement cycle time (request to PO)
- Vendor evaluation completeness score
- Policy compliance rate (% of purchases with required approvals)
- Cost savings vs. benchmark pricing

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial proposal | System |
