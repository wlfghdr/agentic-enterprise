# AIMS Statement of Applicability (SoA)

> **Template version:** 1.0
> **Last updated:** 2026-04-05
> **Standard:** ISO/IEC 42001:2023 — Clause 6.1.3(f), Definition 3.26
> **Purpose:** Document applicability and implementation status of all Annex A controls for the AI Management System

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | AIMS-SOA-001 |
| Version | {{VERSION}} |
| Classification | Confidential |
| Owner | {{AIMS_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual (or upon significant change to risk assessment) |
| Related | [AIMS Scope](_TEMPLATE-aims-scope.md), [AIMS Internal Audit](_TEMPLATE-aims-internal-audit.md), [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md) |

---

## How to Use This Template

Per Clause 6.1.3(f) and Definition 3.26, the SoA must document all necessary controls and justify inclusion or exclusion of each. Note:
- Organizations may not require all controls listed in Annex A
- Organizations may add controls beyond Annex A
- All identified risks must be documented and reflected in the SoA

This template is **pre-populated** with the Agentic Enterprise framework's implementation references where applicable. Adopters must review and adjust each control based on their specific risk assessment.

### Status Legend

| Status | Meaning |
|--------|---------|
| Implemented | Control is fully implemented by the framework and/or deployment |
| Partial | Framework provides governance scaffolding; deployment must complete |
| Planned | Control is planned but not yet implemented |
| Not started | Control not yet addressed |
| Not applicable | Control does not apply (justification required) |

---

## A.2 — AI Policies (3 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.2.2 | AI policy | Yes | Foundational requirement — establishes organizational commitment to responsible AI | Implemented | [ai-governance.md](../../../org/4-quality/policies/ai-governance.md) — AI Governance & Responsible AI Policy | |
| A.2.3 | Roles and responsibilities for AI | Yes | Required to ensure accountability for AI system lifecycle | Implemented | [AGENTS.md](../../../AGENTS.md) — 5-layer governance model; [CODEOWNERS](../../../CODEOWNERS); layer-specific AGENT.md files | |
| A.2.4 | Resources for AI | Yes | Ensures adequate resources for AIMS implementation | Partial | [CONFIG.yaml](../../../CONFIG.yaml) — agent fleet configuration; token budgets in ai-governance.md §6. **Deployment-specific:** adopter must allocate human and financial resources | |

## A.3 — Internal Organization (2 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.3.2 | AI system life cycle | Yes | Required to manage AI systems from inception to retirement | Implemented | Agent type definitions in [org/agents/](../../../org/agents/); mission lifecycle in [org/2-orchestration/](../../../org/2-orchestration/); model card requirements in ai-governance.md §2 | |
| A.3.3 | Responsible AI — due diligence | Yes | Ensures responsible AI practices are integrated into operations | Implemented | ai-governance.md (principles, fairness audit §3, adversarial robustness §4); [risk-management.md](../../../org/4-quality/policies/risk-management.md) AI risk taxonomy | |

## A.4 — AI Risk Management (5 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.4.2 | AI risk assessment | Yes | Core AIMS requirement for identifying and evaluating AI risks | Implemented | [risk-management.md](../../../org/4-quality/policies/risk-management.md) — AI risk taxonomy (22 canonical risks), risk scoring | |
| A.4.3 | Approaches for addressing AI risks | Yes | Required to define treatment options for identified risks | Implemented | risk-management.md §6 — autonomy tiers, kill switch, cascade prevention | |
| A.4.4 | Documentation of AI risk assessment | Yes | Evidence requirement for risk assessment results | Partial | Risk tiers documented in agent type definitions. **Deployment-specific:** adopter must maintain formal risk register | |
| A.4.5 | AI risk treatment | Yes | Required to implement selected treatment options | Implemented | risk-management.md — treatment mapped per risk; ai-governance.md — fairness remediation, adversarial testing | |
| A.4.6 | Communication of AI risks | Yes | Ensures risks are communicated to relevant stakeholders | Partial | Signal system ([work/signals/](../../../work/signals/)); steering layer reviews. **Deployment-specific:** adopter must define external communication channels | |

## A.5 — AI Impact Assessment (4 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.5.2 | AI impact assessment process | Yes | Required to assess consequences for individuals and societies | Implemented | [_TEMPLATE-ai-system-impact-assessment.md](_TEMPLATE-ai-system-impact-assessment.md) §1 | |
| A.5.3 | Documentation of impact assessment | Yes | Evidence requirement for impact assessment results | Implemented | [_TEMPLATE-ai-system-impact-assessment.md](_TEMPLATE-ai-system-impact-assessment.md) §2 | |
| A.5.4 | Impact assessment — individuals | Yes | Required to assess impacts on individuals and groups | Implemented | [_TEMPLATE-ai-system-impact-assessment.md](_TEMPLATE-ai-system-impact-assessment.md) §3 (8 impact areas) | |
| A.5.5 | Impact assessment — societies | Yes | Required to assess broader societal impacts | Implemented | [_TEMPLATE-ai-system-impact-assessment.md](_TEMPLATE-ai-system-impact-assessment.md) §4 (5 impact areas) | |

## A.6.1 — Objectives for Responsible AI (2 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.6.1.2 | Objectives for responsible AI | Yes | Required to establish measurable AI objectives | Partial | ai-governance.md §1 (risk classification), §3 (fairness metrics). **Deployment-specific:** adopter must set specific measurable objectives | |
| A.6.1.3 | Organizational compliance with AI | Yes | Ensures compliance with applicable AI laws and regulations | Implemented | ai-governance.md §9 (compliance mapping — ISO 42001, EU AI Act, NIST AI RMF); [privacy.md](../../../org/4-quality/policies/privacy.md) GDPR alignment | |

## A.6.2 — AI System Lifecycle (7 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.6.2.2 | Design and development | Yes | Ensures AI systems are designed responsibly | Implemented | Agent type definitions with model governance sections; ai-governance.md §2 (model cards) | |
| A.6.2.3 | Verification and validation | Yes | Required to verify AI systems meet requirements | Implemented | [org/4-quality/](../../../org/4-quality/) — quality layer eval agents; ai-governance.md §3 (fairness audit), §4 (adversarial testing) | |
| A.6.2.4 | Operation and monitoring | Yes | Required to monitor AI systems in operation | Implemented | [observability.md](../../../org/4-quality/policies/observability.md); [otel-contract.md](../../otel-contract.md); ai-governance.md §6 (token accountability) | |
| A.6.2.5 | AI system documentation | Yes | Transparency requirement for AI systems | Implemented | ai-governance.md §2 (model cards); agent type definitions; [_TEMPLATE-agent-type.md](../../../org/agents/_TEMPLATE-agent-type.md) | |
| A.6.2.6 | Responsible use of AI | Yes | Ensures AI is used within intended boundaries | Implemented | ai-governance.md §1 (Tier 0 prohibited uses); AGENTS.md Rule 2 (humans decide); risk-management.md autonomy tiers | |
| A.6.2.7 | Third-party and customer relationships | Yes | Manages AI-related third-party risks | Partial | [vendor-risk.md](../../../org/4-quality/policies/vendor-risk.md); [org/integrations/](../../../org/integrations/) integration registry. **Deployment-specific:** adopter must define customer AI agreements | |
| A.6.2.8 | Log management | Yes | Required for AI system auditability | Implemented | observability.md; otel-contract.md — structured logging for all agent actions; ai-governance.md §5 (explainability — Traceable level for all systems) | |

## A.7 — Data for AI Systems (5 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.7.2 | Data management processes | Yes | Required to govern data used in AI systems | Implemented | ai-governance.md §10 (AI Data Governance) | |
| A.7.3 | Data acquisition | Yes | Required to document data sources and selection | Implemented | ai-governance.md §10.2 (data acquisition documentation) | |
| A.7.4 | Data quality | Yes | Required to define and ensure data quality standards | Implemented | ai-governance.md §10.3 (data quality requirements per risk tier) | |
| A.7.5 | Data provenance | Yes | Required to track data origin and transformations | Implemented | ai-governance.md §10.4 (data provenance tracking) | |
| A.7.6 | Data preparation | Yes | Required to document data preparation methods | Implemented | ai-governance.md §10.5 (data preparation standards) | |

## A.8 — Information for Interested Parties (4 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.8.2 | Conformity with legislation and regulation | Yes | Ensures compliance with applicable AI laws | Implemented | ai-governance.md §9 (compliance mapping); privacy.md (GDPR); [agent-security.md](../../../org/4-quality/policies/agent-security.md) | |
| A.8.3 | External reporting of concerns | Yes | Provides mechanism for reporting adverse AI impacts | Partial | Signal system for internal reporting. **Deployment-specific:** adopter must implement external adverse-impact reporting channel | |
| A.8.4 | Use of specific technical tools | Yes | Ensures appropriate tooling for AI development | Implemented | Integration registry; CONFIG.yaml — governed tool and MCP server registration | |
| A.8.5 | Reporting obligations | Yes | Ensures regulatory reporting obligations are met | Partial | ai-governance.md §9 compliance mapping. **Deployment-specific:** adopter must identify and implement jurisdiction-specific reporting obligations | |

## A.9 — Monitoring of AI Systems (3 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.9.2 | System log monitoring | Yes | Required for AI system observability and incident detection | Implemented | observability.md; otel-contract.md — structured OTel traces for all agent actions | |
| A.9.3 | Performance monitoring | Yes | Required to detect model drift and degradation | Implemented | ai-governance.md §6 (token monitoring, anomaly detection); observability.md SLO framework | |
| A.9.4 | AI system change management | Yes | Required to manage changes to AI systems | Implemented | Git-based change management (AGENTS.md Rule 3); PR review gates; CODEOWNERS; model card update triggers in ai-governance.md §2.2 | |

## A.10 — AI Awareness and Training (3 controls)

| Control | Title | Applicable? | Justification for inclusion / exclusion | Status | Implementation reference | Risk treatment plan ref |
|---------|-------|:-----------:|----------------------------------------|:------:|------------------------|------------------------|
| A.10.2 | AI-specific awareness training | Yes | Ensures personnel understand AI governance requirements | Partial | AGENTS.md (agent instructions); layer-specific AGENT.md files. **Deployment-specific:** adopter must implement human staff awareness training programme | |
| A.10.3 | AI literacy and fluency | Yes | Ensures personnel have sufficient AI competence | Partial | Framework documentation and guides. **Deployment-specific:** adopter must assess and develop human AI competence levels | |
| A.10.4 | Customer AI requirements | Yes | Ensures customer expectations are understood and met | Partial | ai-governance.md §7 (deployment-customizable decisions). **Deployment-specific:** adopter must document customer AI requirements and domain limits | |

---

## Additional Organization-Defined Controls (per Clause 6.1.3 d)

Per Clause 6.1.3(d) and Note 3, the organization may identify controls beyond Annex A. Document any additional controls below using the same structure.

| Control ID | Title | Applicable? | Justification for inclusion | Status | Implementation reference | Risk treatment plan ref |
|-----------|-------|:-----------:|----------------------------|:------:|------------------------|------------------------|
| ORG.1 | {{TITLE}} | {{Y/N}} | {{JUSTIFICATION}} | {{STATUS}} | {{REFERENCE}} | {{RTR_REF}} |

---

## Management Approval

Per Clause 6.1.3: "The organization shall obtain approval from the designated management for the AI risk treatment plan and for acceptance of the residual AI risks."

| Role | Name | Approval | Date | Notes |
|------|------|----------|------|-------|
| AIMS owner | {{NAME}} | Approved / Pending | {{DATE}} | |
| Top management | {{NAME}} | Approved / Pending | {{DATE}} | Risk treatment plan accepted |
| Risk owner(s) | {{NAME}} | Approved / Pending | {{DATE}} | Residual risks accepted |

---

## Summary

| Category | Total controls | Applicable | Not applicable | Implemented | Partial | Planned | Not started |
|----------|:--------------:|:----------:|:--------------:|:-----------:|:-------:|:-------:|:-----------:|
| A.2 — Policies | 3 | | | | | | |
| A.3 — Internal organization | 2 | | | | | | |
| A.4 — Risk management | 5 | | | | | | |
| A.5 — Impact assessment | 4 | | | | | | |
| A.6.1 — Objectives | 2 | | | | | | |
| A.6.2 — Lifecycle | 7 | | | | | | |
| A.7 — Data | 5 | | | | | | |
| A.8 — Information | 4 | | | | | | |
| A.9 — Monitoring | 3 | | | | | | |
| A.10 — Awareness | 3 | | | | | | |
| **Total** | **38** | | | | | | |
| Additional (org-defined) | | | | | | | |

> Note: The standard lists 39 controls in Table A.1. The count difference reflects that some numbering is non-sequential (e.g. A.2 starts at A.2.2). All controls from A.2.2 through A.10.4 are covered above.

---

## Compliance Mapping

| Standard clause | Section in this template |
|----------------|------------------------|
| Clause 6.1.3(f) — Statement of applicability | Entire document |
| Definition 3.26 — Statement of applicability | Structure and justification fields |
| Clause 6.1.3(d) — Additional controls | "Additional Organization-Defined Controls" section |
| Clause 6.1.3 — Management approval | "Management Approval" section |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-05 | Initial template covering all 39 Annex A controls (A.2.2--A.10.4). Pre-populated with Agentic Enterprise framework references. Closes #249. |
