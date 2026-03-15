# Artificial Intelligence Management System — Scope Statement

> **Template version:** 1.0
> **Last updated:** 2026-03-15
> **Standard:** ISO/IEC 42001:2023 — Clause 4.3
> **Purpose:** Define the boundaries and applicability of the Artificial Intelligence Management System (AIMS)

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | AIMS-SCOPE-001 |
| Version | {{VERSION}} |
| Classification | {{CLASSIFICATION}} |
| Owner | {{AIMS_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual (or upon significant change) |
| Related | [AI System Inventory](_TEMPLATE-ai-system-inventory.md) |

## 1. Organization Context (Clauses 4.1 and 4.2)

### 1a. Organization Overview

- Legal entity: {{LEGAL_ENTITY_NAME}}
- Industry: {{INDUSTRY}}
- Primary business: {{PRIMARY_BUSINESS}}
- Operating model: Agentic Enterprise (multi-agent AI governance)

### 1b. Internal Issues Relevant to the AIMS

- Organizational structure: {{ORG_STRUCTURE_DESCRIPTION}}
- AI operating model: {{AI_OPERATING_MODEL}}
- Key AI use cases: {{AI_USE_CASES}}
- Existing governance mechanisms: {{GOVERNANCE_MECHANISMS}}
- Resource or capability constraints: {{CONSTRAINTS}}

### 1c. External Issues Relevant to the AIMS

- Regulatory environment: {{REGULATORY_ENVIRONMENT}}
- Customer and partner expectations: {{CUSTOMER_PARTNER_EXPECTATIONS}}
- External AI provider dependencies: {{AI_PROVIDER_DEPENDENCIES}}
- Threat landscape: {{THREAT_LANDSCAPE}}
- Market expectations for AI assurance: {{MARKET_EXPECTATIONS}}

### 1d. Interested Parties

| Interested Party | AI-Related Requirements | Relevance to the AIMS |
|-----------------|-------------------------|-----------------------|
| Customers | {{CUSTOMER_REQUIREMENTS}} | {{RELEVANCE}} |
| Regulators | {{REGULATORY_REQUIREMENTS}} | {{RELEVANCE}} |
| Employees / operators | {{EMPLOYEE_REQUIREMENTS}} | {{RELEVANCE}} |
| Partners / vendors | {{VENDOR_REQUIREMENTS}} | {{RELEVANCE}} |
| Board / shareholders | {{BOARD_REQUIREMENTS}} | {{RELEVANCE}} |
| Affected individuals / AI system users | {{USER_REQUIREMENTS}} | {{RELEVANCE}} |

## 2. AIMS Scope Definition (Clause 4.3)

### 2a. Scope Statement

{{ORGANIZATION_NAME}} has established and maintains an Artificial Intelligence
Management System in accordance with ISO/IEC 42001:2023 for the following scope:

> **{{AIMS_SCOPE_STATEMENT}}**

### 2b. Organizational Units in Scope

- {{ORG_UNIT_1}}
- {{ORG_UNIT_2}}

### 2c. AI Systems and Services in Scope

| AI System / Service | Purpose | Risk Tier | Lifecycle Stage | In Scope |
|---------------------|---------|-----------|-----------------|----------|
| {{AI_SYSTEM_1}} | {{PURPOSE}} | {{TIER_0_1_2_3}} | {{DESIGN / PILOT / PRODUCTION / RETIRED}} | Yes |
| {{AI_SYSTEM_2}} | {{PURPOSE}} | {{TIER_0_1_2_3}} | {{STAGE}} | Yes / No |

> Maintain the full system list in the related [AI System Inventory](_TEMPLATE-ai-system-inventory.md).

### 2d. Activities and Processes in Scope

| Activity | Supporting Layer | In Scope |
|----------|------------------|----------|
| AI system design and approval | {{LAYER}} | Yes |
| Model/provider selection and change management | {{LAYER}} | Yes |
| Prompt, workflow, and orchestration management | {{LAYER}} | Yes |
| Inference operations and human review | {{LAYER}} | Yes |
| Monitoring, evaluation, and incident response for AI systems | {{LAYER}} | Yes |
| {{ADDITIONAL_ACTIVITY}} | {{LAYER}} | Yes / No |

### 2e. Locations and Environments in Scope

| Location / Environment | Type | Activities Performed | In Scope |
|------------------------|------|----------------------|----------|
| {{LOCATION_1}} | {{CLOUD_REGION / OFFICE / SAAS}} | {{ACTIVITIES}} | Yes |
| {{LOCATION_2}} | {{TYPE}} | {{ACTIVITIES}} | Yes / No |

### 2f. Data Categories in Scope

| Data Category | Classification | AI Processing Activity |
|---------------|----------------|------------------------|
| {{DATA_CATEGORY_1}} | {{PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED}} | {{ACTIVITY}} |
| {{DATA_CATEGORY_2}} | {{CLASSIFICATION}} | {{ACTIVITY}} |

### 2g. Interfaces and Dependencies

| Interface / Dependency | Direction | AI Relevance | Controls Applied |
|------------------------|-----------|--------------|-----------------|
| {{AI_PROVIDER}} | {{INBOUND / OUTBOUND / BIDIRECTIONAL}} | {{WHY_RELEVANT}} | {{CONTROLS}} |
| {{INTEGRATION_2}} | {{DIRECTION}} | {{WHY_RELEVANT}} | {{CONTROLS}} |

### 2h. Exclusions from Scope

| Exclusion | Justification |
|-----------|--------------|
| {{EXCLUSION_1}} | {{JUSTIFICATION_1}} |
| {{EXCLUSION_2}} | {{JUSTIFICATION_2}} |

## 3. AIMS Boundaries

### 3a. Logical Boundaries

- {{LOGICAL_BOUNDARY_1}}
- {{LOGICAL_BOUNDARY_2}}

### 3b. Physical / Hosting Boundaries

- {{PHYSICAL_BOUNDARY_DESCRIPTION}}

### 3c. Legal / Regulatory Boundaries

- {{LEGAL_BOUNDARY_DESCRIPTION}}

## 4. AI Risk Profile Summary

| Risk Tier | Count of In-Scope Systems | Notes |
|-----------|---------------------------|-------|
| Tier 0 — Prohibited | {{N}} | {{NOTES}} |
| Tier 1 — High-Risk | {{N}} | {{NOTES}} |
| Tier 2 — Limited-Risk | {{N}} | {{NOTES}} |
| Tier 3 — Minimal-Risk | {{N}} | {{NOTES}} |

## 5. Review and Maintenance

This scope statement is reviewed:

- annually as part of the AIMS management review cycle
- upon significant change to AI use cases, models, providers, or organizational structure
- after major incidents, nonconformities, or regulatory changes affecting AI systems

| Trigger | Action | Owner |
|---------|--------|-------|
| Annual review | Full scope reassessment | AIMS Owner |
| New AI system or provider | Evaluate inclusion and update inventory | AIMS Owner + System Owner |
| Material model / provider change | Reassess boundaries and dependencies | AIMS Owner |
| Regulatory change | Evaluate scope impact | Legal / Compliance |
| Major AI incident | Evaluate scope adequacy | Incident Commander + AIMS Owner |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial AIMS scope statement |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-15 | Initial AIMS scope statement template aligned to ISO/IEC 42001 clause 4.3 |
