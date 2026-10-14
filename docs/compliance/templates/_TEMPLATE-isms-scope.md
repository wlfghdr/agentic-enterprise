# ISMS Scope Statement

> **Standard:** ISO/IEC 27001:2022 — Clause 4.3
> **Purpose:** Define the boundaries and applicability of the Information Security Management System

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ISMS-SCOPE-001 |
| Version | {{VERSION}} |
| Classification | {{CLASSIFICATION}} |
| Owner | {{ISMS_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual (or upon significant change) |

## 1. Organization Context (Clause 4.1)

### 1a. Organization Overview

[Brief description of the organization, its mission, and its operating model. Reference COMPANY.md for the Agentic Enterprise framework context.]

- Legal entity: {{LEGAL_ENTITY_NAME}}
- Industry: {{INDUSTRY}}
- Primary business: {{PRIMARY_BUSINESS}}
- Operating model: Agentic Enterprise (multi-agent AI governance)

### 1b. Internal Context

[Key internal factors relevant to the ISMS:]

- Organizational structure (reference the 5-layer model if using the framework)
- Technology stack and infrastructure
- AI/agent workloads and their classification
- Existing governance processes

### 1c. External Context

[Key external factors:]

- Regulatory environment (GDPR, EU AI Act, sector-specific)
- Customer and partner requirements
- Threat landscape
- Market expectations for security certifications

## 2. Interested Parties (Clause 4.2)

| Interested Party | Requirements | Relevance to ISMS |
|-----------------|-------------|-------------------|
| Customers | Data protection, service availability, compliance attestations | Direct — their data is processed within ISMS scope |
| Regulators | Legal compliance (GDPR, EU AI Act, sector-specific) | Direct — audit/inspection rights |
| Employees | Privacy, safe working environment | Direct — process personal data |
| Partners/vendors | Secure data exchange, contractual obligations | Direct — supply chain risk |
| Shareholders/board | Risk management, business continuity | Indirect — governance expectations |
| AI system users | Transparency, fairness, data rights | Direct — AI-specific obligations |

## 3. ISMS Scope Definition (Clause 4.3)

### 3a. Included in Scope

#### Organizational Units

[List all organizational units covered by the ISMS:]

- {{ORG_UNIT_1}}
- {{ORG_UNIT_2}}

#### Locations

| Location | Type | In Scope |
|----------|------|----------|
| {{LOCATION_1}} | {{TYPE}} (HQ/office/data center/cloud region) | Yes |

#### Information Systems and Services

| System/Service | Description | Classification | In Scope |
|---------------|-------------|----------------|----------|
| Agent execution platform | Multi-agent AI workloads | {{CLASSIFICATION}} | Yes |
| Orchestration layer | Fleet management, mission dispatch | {{CLASSIFICATION}} | Yes |
| Observability platform | OTel telemetry, SIEM | {{CLASSIFICATION}} | Yes |
| Git repository | Governance backbone, code, policies | {{CLASSIFICATION}} | Yes |
| CI/CD pipeline | Automated testing and deployment | {{CLASSIFICATION}} | Yes |
| {{ADDITIONAL_SYSTEM}} | {{DESCRIPTION}} | {{CLASSIFICATION}} | Yes/No |

#### Processes

[List key processes in scope:]

- Information security risk management
- Agent governance and quality assurance
- Change management (PR-based)
- Incident response and management
- Access control and identity management
- Vendor/supplier management
- Business continuity management
- Data classification and protection
- Cryptographic key management
- Monitoring, logging, and audit

#### Data Types

| Data Type | Classification | Processing Activities |
|-----------|---------------|---------------------|
| Customer data | Confidential | Processing by agent workloads |
| Agent telemetry | Internal | Observability and audit |
| Business strategy | Restricted | Strategy layer decisions |
| Source code | Internal | Development and deployment |
| Personnel data | Confidential | HR processes |
| AI training data | {{CLASSIFICATION}} | Model training/fine-tuning |

### 3b. Excluded from Scope

| Exclusion | Justification |
|-----------|--------------|
| {{EXCLUSION_1}} | {{JUSTIFICATION_1}} |
| Physical security of third-party data centers | Covered by cloud provider's SOC 2/ISO 27001 (shared responsibility model) |

### 3c. Interfaces and Dependencies

[Systems and parties outside the ISMS scope that interact with in-scope systems:]

| Interface | Direction | Controls Applied |
|-----------|-----------|-----------------|
| Cloud provider (AWS/Azure/GCP) | Bidirectional | Vendor risk management, SLA monitoring, cloud provider SOC 2 reliance |
| External AI model providers | Outbound (API calls) | Vendor assessment, data classification controls, encryption in transit |
| Customer-facing APIs | Inbound | WAF, authentication, rate limiting, input validation |
| Third-party integrations | Bidirectional | Integration registry governance, MCP server controls |

## 4. ISMS Boundaries

### 4a. Logical Boundaries

- All systems deployed in {{CLOUD_PROVIDER}} region(s): {{REGIONS}}
- All agent workloads managed by the orchestration layer
- All data classified as Internal, Confidential, or Restricted per the Data Classification Policy
- All governance processes managed through the Git-based operating model

### 4b. Physical Boundaries

- {{PHYSICAL_BOUNDARY_DESCRIPTION}}

### 4c. Network Boundaries

- VPC/VNet: {{NETWORK_IDENTIFIER}}
- IP ranges: {{IP_RANGES}}
- DNS domains: {{DOMAINS}}

## 5. Applicability of Annex A Controls

The detailed applicability of all 93 Annex A controls is documented in the **Statement of Applicability (SoA)** — see [Statement of Applicability](_TEMPLATE-soa.md).

Summary:

- **Applicable:** {{N}} controls
- **Not applicable:** {{M}} controls (with justification in SoA)
- **Partially applicable:** {{P}} controls (deployment-specific completion required)

## 6. Review and Maintenance

This scope statement is reviewed:

- **Annually** as part of the management review cycle
- **Upon significant change** to the organization, technology, threats, or regulatory environment
- **After major incidents** that reveal scope inadequacy

| Trigger | Action | Owner |
|---------|--------|-------|
| Annual review | Full scope reassessment | ISMS Owner |
| New regulation | Evaluate impact on scope | Legal/Compliance |
| New system/service | Evaluate inclusion/exclusion | IT Security |
| Organizational restructure | Reassess organizational units | ISMS Owner |
| Major security incident | Evaluate scope adequacy | Incident Commander + ISMS Owner |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial scope statement |
