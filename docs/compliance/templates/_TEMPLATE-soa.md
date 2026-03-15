# Statement of Applicability (SoA)

> **Template version:** 1.0
> **Last updated:** 2026-03-15
> **Standard:** ISO/IEC 27001:2022 — Clause 6.1.3d
> **Purpose:** Document applicability and implementation status of all 93 Annex A controls

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ISMS-SOA-001 |
| Version | {{VERSION}} |
| Classification | Confidential |
| Owner | {{ISMS_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Annual (or upon significant change) |
| Related | [ISMS Scope Statement](_TEMPLATE-isms-scope.md) |

## How to Use This Template

This SoA template is **pre-populated** with the Agentic Enterprise framework's coverage:
- **Framework-addressed** controls show the implementing policy or mechanism
- **Deployment-specific** controls require the adopter to fill in their implementation
- **Not applicable** is pre-suggested for controls unlikely to apply to a software framework — **review and adjust** based on your actual deployment

### Status Legend

| Status | Meaning |
|--------|---------|
| Implemented | Control is fully implemented by the framework and/or deployment |
| Partial | Framework provides governance scaffolding; deployment must complete |
| Planned | Control is planned but not yet implemented |
| Not applicable | Control does not apply (justification required) |
| To be assessed | Adopter must evaluate applicability |

---

## A.5 Organizational Controls (37 controls)

| # | Control | Applicable | Status | Implementation / Justification |
|---|---------|:----------:|:------:|-------------------------------|
| A.5.1 | Policies for information security | Yes | Implemented | 19 quality policies in [`org/4-quality/policies/`](../../../org/4-quality/policies/), version-controlled in Git with PR-based review cycle. Policies cover security, privacy, cryptography, data classification, incident response, vendor risk, availability, observability, and more. Annual review enforced by steering layer. |
| A.5.2 | Information security roles and responsibilities | Yes | Implemented | [`CODEOWNERS`](../../../CODEOWNERS) defines RACI for all governed artifacts. Layer-specific [`AGENT.md`](../../../AGENTS.md) files define agent boundaries. 5-layer governance model (`org/0-steering/` through `org/4-quality/`) assigns clear responsibilities. Human approval gates on all governance decisions. |
| A.5.3 | Segregation of duties | Yes | Implemented | Layer separation enforces segregation: strategy agents do not write code, execution agents do not make strategy decisions, quality agents do not implement features. [`CODEOWNERS`](../../../CODEOWNERS) prevents self-approval of PRs. Separate agent types per layer with distinct permissions. |
| A.5.4 | Management responsibilities | Yes | Implemented | Steering layer ([`org/0-steering/AGENT.md`](../../../org/0-steering/AGENT.md)) defines management oversight. Human approval gates on all governance decisions (AGENTS.md Rule 2). Executive sponsors required for missions and strategic changes. |
| A.5.5 | Contact with authorities | Yes | Partial | [`CONFIG.yaml`](../../../CONFIG.yaml) defines organizational contacts. Integration registry ([`org/integrations/`](../../../org/integrations/)) supports authority notification channels. **Deployment-specific:** adopter must configure actual regulatory authority contacts, reporting obligations, and notification workflows. |
| A.5.6 | Contact with special interest groups | Yes | Partial | [`work/signals/`](../../../work/signals/) system ingests external intelligence. Steering layer produces weekly digests ([`work/signals/digests/`](../../../work/signals/digests/)). Framework participation via Rule 13 (upstream contribution). **Deployment-specific:** adopter must establish relationships with ISACs, CERTs, and industry groups. |
| A.5.7 | Threat intelligence | Yes | Partial | Observability platform provides anomaly detection ([`org/4-quality/policies/observability.md`](../../../org/4-quality/policies/observability.md)). Signal system ([`work/signals/`](../../../work/signals/)) captures threat observations. AGENTS.md Rule 9b requires agents to consume observability data before acting. **Deployment-specific:** adopter must configure threat intelligence feeds and integrate with SIEM. |
| A.5.8 | Information security in project management | Yes | Implemented | Technical design template ([`work/missions/_TEMPLATE-technical-design.md`](../../../work/missions/_TEMPLATE-technical-design.md)) includes security section. Quality layer reviews security aspects of all designs. AGENTS.md Rule 9c requires observability and security planning before building. Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) mandates security gates. |
| A.5.9 | Inventory of information and other associated assets | Yes | Partial | [`CONFIG.yaml`](../../../CONFIG.yaml) and [`org/`](../../../org/) structure define framework assets. Asset registry ([`work/assets/`](../../../work/assets/)) tracks non-code deliverables. Integration registry ([`org/integrations/`](../../../org/integrations/)) catalogs third-party tools. **Deployment-specific:** adopter must maintain a complete asset inventory including infrastructure, data stores, and endpoints. |
| A.5.10 | Acceptable use of information and other associated assets | Yes | Implemented | Data classification policy ([`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md)) defines handling rules per classification level. AGENTS.md rules constrain agent behavior. Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) defines acceptable use for AI agents. |
| A.5.11 | Return of assets | Yes | To be assessed | **Deployment-specific:** adopter must define asset return procedures for personnel offboarding. Framework provides [`work/decisions/`](../../../work/decisions/) for documenting access grants and revocations. |
| A.5.12 | Classification of information | Yes | Implemented | Data classification policy ([`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md)) defines classification levels (Public, Internal, Confidential, Restricted). [`CODEOWNERS`](../../../CODEOWNERS) enforces access control aligned with classification. |
| A.5.13 | Labelling of information | Yes | Partial | Data classification policy defines labelling requirements. Document control sections in templates include Classification field. **Deployment-specific:** adopter must implement automated labelling in email, file systems, and data stores. |
| A.5.14 | Information transfer | Yes | Partial | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) governs artifact transfer through CI/CD. Integration registry ([`org/integrations/`](../../../org/integrations/)) governs external data flows. Cryptography policy ([`org/4-quality/policies/cryptography.md`](../../../org/4-quality/policies/cryptography.md)) mandates TLS 1.3 for data in transit. **Deployment-specific:** adopter must define transfer agreements and procedures for non-automated channels. |
| A.5.15 | Access control | Yes | Implemented | Agent least-privilege principle (AGENTS.md Rule 5 — stay in your lane). [`CODEOWNERS`](../../../CODEOWNERS) enforces repository access control. Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) defines agent permission boundaries. Layer separation prevents cross-layer access. |
| A.5.16 | Identity management | Yes | Partial | Framework uses Git identities and bot accounts for agents. AGENTS.md assignment discipline (Rule 3) requires every artifact to have an assignee. **Deployment-specific:** adopter must implement an Identity Provider (IdP) with lifecycle management, MFA, and federation. |
| A.5.17 | Authentication information | Yes | Partial | Cryptography policy ([`org/4-quality/policies/cryptography.md`](../../../org/4-quality/policies/cryptography.md)) defines authentication standards. Agent security policy requires secure credential management. **Deployment-specific:** adopter must implement credential vaulting, rotation schedules, and MFA enforcement. |
| A.5.18 | Access rights | Yes | Implemented | Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) enforces least-privilege tooling for agents. [`CODEOWNERS`](../../../CODEOWNERS) defines who can approve changes to what. PR-based access control changes are auditable in Git history. |
| A.5.19 | Information security in supplier relationships | Yes | Implemented | Vendor risk management policy ([`org/4-quality/policies/vendor-risk-management.md`](../../../org/4-quality/policies/vendor-risk-management.md)) defines 4-tier vendor classification and assessment requirements. Integration registry tracks all third-party connections. |
| A.5.20 | Addressing information security within supplier agreements | Yes | Implemented | Vendor risk management policy defines contractual security requirements per vendor tier. Includes data processing agreements, audit rights, incident notification SLAs, and sub-processor controls. |
| A.5.21 | Managing information security in the ICT supply chain | Yes | Implemented | Vendor risk management policy addresses supply chain risk with specific controls for open-source dependencies, AI model providers, and cloud infrastructure. Delivery policy includes dependency scanning requirements. |
| A.5.22 | Monitoring, review and change management of supplier services | Yes | Implemented | Vendor risk management policy defines monitoring cadence and SLA review per vendor tier. Integration registry tracks supplier service configurations. Observability platform monitors supplier API health. |
| A.5.23 | Information security for use of cloud services | Yes | Partial | Vendor risk management policy includes cloud-specific assessment criteria and shared responsibility model documentation. **Deployment-specific:** adopter must configure cloud-native security controls (IAM, network policies, encryption, logging) per their cloud provider. |
| A.5.24 | Information security incident management planning and preparation | Yes | Implemented | Incident response policy ([`org/4-quality/policies/incident-response.md`](../../../org/4-quality/policies/incident-response.md)) defines incident management framework, roles, communication channels, and escalation procedures. Retrospective template ensures post-incident learning. |
| A.5.25 | Assessment and decision on information security events | Yes | Implemented | Incident response policy defines event classification criteria (severity levels), triage procedures, and assessment workflows. Observability platform provides event detection and correlation. Signal system captures security events. |
| A.5.26 | Response to information security incidents | Yes | Implemented | Incident response policy defines response procedures per severity level, containment strategies, eradication steps, and recovery processes. [`work/retrospectives/`](../../../work/retrospectives/) captures incident retrospectives with root cause analysis. |
| A.5.27 | Learning from information security incidents | Yes | Implemented | [`work/retrospectives/`](../../../work/retrospectives/) stores post-incident reviews with lessons learned, timeline reconstruction, and improvement actions. AGENTS.md Rule 7 requires agents to file improvement signals based on incident observations. Steering layer aggregates patterns. |
| A.5.28 | Collection of evidence | Yes | Implemented | Log retention policy ([`org/4-quality/policies/log-retention.md`](../../../org/4-quality/policies/log-retention.md)) defines evidence preservation requirements. Observability policy ([`org/4-quality/policies/observability.md`](../../../org/4-quality/policies/observability.md)) mandates comprehensive telemetry. Git history provides immutable audit trail. All agent actions produce OpenTelemetry spans (AGENTS.md Rule 9a). |
| A.5.29 | Information security during disruption | Yes | Implemented | Availability policy ([`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md)) defines business continuity requirements, RTO/RPO targets, and failover procedures. Incident response policy covers disruption scenarios. |
| A.5.30 | ICT readiness for business continuity | Yes | Implemented | Availability policy defines ICT readiness requirements including redundancy, backup, disaster recovery testing, and capacity planning. Performance policy ([`org/4-quality/policies/performance.md`](../../../org/4-quality/policies/performance.md)) ensures infrastructure capacity. |
| A.5.31 | Legal, statutory, regulatory and contractual requirements | Yes | Partial | Privacy policy ([`org/4-quality/policies/privacy.md`](../../../org/4-quality/policies/privacy.md)) addresses GDPR, EU AI Act, and data protection regulations. Data classification policy covers regulatory handling requirements. **Deployment-specific:** adopter must identify and document all applicable legal, regulatory, and contractual requirements for their jurisdiction and industry. |
| A.5.32 | Intellectual property rights | Yes | Partial | Privacy policy includes intellectual property considerations. Framework is open-source (MIT/Apache). **Deployment-specific:** adopter must document IP ownership for AI-generated outputs, training data licensing, and third-party code attribution. |
| A.5.33 | Protection of records | Yes | Implemented | Privacy policy defines records protection requirements. Log retention policy specifies retention periods and immutability controls. Git history provides tamper-evident record of all governance decisions. Data classification policy defines handling per classification level. |
| A.5.34 | Privacy and protection of PII | Yes | Partial | Privacy policy ([`org/4-quality/policies/privacy.md`](../../../org/4-quality/policies/privacy.md)) defines PII handling, data subject rights, consent management, and privacy-by-design principles. Data classification policy identifies PII classification. **Deployment-specific:** adopter must implement DPIA processes, data subject request workflows, and consent management systems. |
| A.5.35 | Independent review of information security | Yes | Partial | Quality layer ([`org/4-quality/AGENT.md`](../../../org/4-quality/AGENT.md)) provides independent review of all deliverables. Quality agents evaluate compliance with policies. **Deployment-specific:** adopter must arrange external independent audits (e.g., ISO 27001 certification audit, penetration testing by third parties). |
| A.5.36 | Compliance with policies, rules and standards | Yes | Implemented | Quality policies ([`org/4-quality/policies/`](../../../org/4-quality/policies/)) define compliance requirements. Quality layer agents verify compliance. CI/CD pipelines enforce policy checks. AGENTS.md Rule 4 makes policies mandatory ("Policies are law"). Governance exceptions require formal documentation and approval. |
| A.5.37 | Documented operating procedures | Yes | Implemented | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) documents development and deployment procedures. [`AGENTS.md`](../../../AGENTS.md) documents agent operating procedures. [`org/README.md`](../../../org/README.md) and [`process/README.md`](../../../process/README.md) document the overall operating model. Layer-specific AGENT.md files document layer procedures. Process documentation in [`process/`](../../../process/). |

---

## A.6 People Controls (8 controls)

| # | Control | Applicable | Status | Implementation / Justification |
|---|---------|:----------:|:------:|-------------------------------|
| A.6.1 | Screening | Yes | To be assessed | **Deployment-specific:** adopter must implement pre-employment screening (background checks, reference verification) appropriate to the role and information access level. Framework does not address human HR processes. |
| A.6.2 | Terms and conditions of employment | Yes | To be assessed | **Deployment-specific:** adopter must include information security responsibilities in employment contracts, NDAs, and acceptable use agreements. Framework does not address employment terms. |
| A.6.3 | Information security awareness, education and training | Yes | Partial | Agent instructions ([`AGENTS.md`](../../../AGENTS.md), layer-specific `AGENT.md` files) serve as "training" for AI agents — read before every task (AGENTS.md "Before Starting Any Task"). **Deployment-specific:** adopter must implement security awareness training for human staff, including phishing simulations, policy acknowledgment, and role-specific training. |
| A.6.4 | Disciplinary process | Yes | To be assessed | **Deployment-specific:** adopter must define a disciplinary process for information security policy violations by human personnel. For agents, non-compliance is addressed through policy enforcement (AGENTS.md Rule 4) and quality layer review. |
| A.6.5 | Responsibilities after termination or change of employment | Yes | To be assessed | **Deployment-specific:** adopter must define offboarding procedures including access revocation, asset return, and ongoing confidentiality obligations. For agents, decommissioning includes revoking API keys, bot accounts, and integration credentials. |
| A.6.6 | Confidentiality or non-disclosure agreements | Yes | Partial | Vendor risk management policy ([`org/4-quality/policies/vendor-risk-management.md`](../../../org/4-quality/policies/vendor-risk-management.md)) requires NDAs with suppliers per vendor tier. **Deployment-specific:** adopter must implement NDAs for employees, contractors, and third parties with access to classified information. |
| A.6.7 | Remote working | Yes | Partial | Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) addresses agent execution security — agents inherently operate remotely (cloud-based execution). Cryptography policy mandates encryption for all communications. **Deployment-specific:** adopter must define remote working security controls for human staff (VPN, endpoint security, secure workspace requirements). |
| A.6.8 | Information security event reporting | Yes | Implemented | [`work/signals/`](../../../work/signals/) system enables security event reporting by any agent or human. AGENTS.md Rule 7 requires every agent to be a "sensor" and file improvement signals. Incident response policy defines escalation paths. Observability platform detects and surfaces anomalies automatically. |

---

## A.7 Physical Controls (14 controls)

| # | Control | Applicable | Status | Implementation / Justification |
|---|---------|:----------:|:------:|-------------------------------|
| A.7.1 | Physical security perimeters | Yes | To be assessed | **Deployment-specific:** adopter must define physical security perimeters for offices and on-premises infrastructure. For cloud-native deployments, this is typically addressed by the cloud provider's SOC 2/ISO 27001 certification under the shared responsibility model. |
| A.7.2 | Physical entry | Yes | To be assessed | **Deployment-specific:** adopter must implement physical access controls (badge readers, visitor logs, escort policies). For cloud-native deployments, cloud provider manages data center physical access. |
| A.7.3 | Securing offices, rooms and facilities | Yes | To be assessed | **Deployment-specific:** adopter must secure office spaces containing sensitive information processing. For cloud-native deployments, cloud provider manages facility security. |
| A.7.4 | Physical security monitoring | Yes | To be assessed | **Deployment-specific:** adopter must implement physical monitoring (CCTV, intrusion detection) for applicable premises. For cloud-native deployments, cloud provider manages physical surveillance. |
| A.7.5 | Protecting against physical and environmental threats | Yes | To be assessed | **Deployment-specific:** adopter must address fire, flood, earthquake, and environmental risks for applicable premises. Availability policy ([`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md)) addresses disaster recovery at the logical level. |
| A.7.6 | Working in secure areas | Yes | To be assessed | **Deployment-specific:** adopter must define controls for working in secure areas (clean desk, restricted photography, visitor supervision). |
| A.7.7 | Clear desk and clear screen | Yes | To be assessed | **Deployment-specific:** adopter must implement clear desk and clear screen policies for human workstations. Agents do not have physical workstations — their execution environment security is covered by agent security policy. |
| A.7.8 | Equipment siting and protection | Yes | To be assessed | **Deployment-specific:** adopter must protect IT equipment from environmental threats and unauthorized access. For cloud-native deployments, cloud provider manages equipment siting. |
| A.7.9 | Security of assets off-premises | Yes | To be assessed | **Deployment-specific:** adopter must define controls for assets used outside organizational premises (laptops, mobile devices). Agent security policy covers agent execution in cloud environments. |
| A.7.10 | Storage media | Yes | Partial | Data classification policy ([`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md)) defines handling and disposal requirements per classification level. Cryptography policy mandates encryption for data at rest. **Deployment-specific:** adopter must implement media sanitization and disposal procedures for physical storage devices. |
| A.7.11 | Supporting utilities | Yes | To be assessed | **Deployment-specific:** adopter must protect supporting utilities (power, telecommunications, water). For cloud-native deployments, cloud provider manages utility infrastructure and redundancy. |
| A.7.12 | Cabling security | Yes | To be assessed | **Deployment-specific:** adopter must protect cabling from interception and damage. For cloud-native deployments, cloud provider manages data center cabling security. |
| A.7.13 | Equipment maintenance | Yes | To be assessed | **Deployment-specific:** adopter must implement equipment maintenance schedules. For cloud-native deployments, cloud provider manages hardware maintenance. Availability policy addresses logical system maintenance windows. |
| A.7.14 | Secure disposal or re-use of equipment | Yes | To be assessed | **Deployment-specific:** adopter must implement secure disposal/re-use procedures with certified data sanitization. Data classification policy defines disposal requirements. Log retention policy defines retention before disposal is permitted. |

---

## A.8 Technological Controls (34 controls)

| # | Control | Applicable | Status | Implementation / Justification |
|---|---------|:----------:|:------:|-------------------------------|
| A.8.1 | User endpoint devices | Yes | To be assessed | **Deployment-specific:** adopter must implement endpoint device management (MDM, disk encryption, patching, endpoint detection and response). Agents operate in managed cloud environments — their "endpoints" are governed by agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)). |
| A.8.2 | Privileged access rights | Yes | Implemented | Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) enforces least-privilege for agent access. [`CODEOWNERS`](../../../CODEOWNERS) restricts who can approve changes to governance artifacts. AGENTS.md Rule 5 (stay in your lane) prevents privilege escalation across layers. PR-based changes to access rights provide audit trail. |
| A.8.3 | Information access restriction | Yes | Implemented | Data classification policy ([`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md)) defines access restrictions per classification level. Agent security policy enforces information access boundaries for agents. Layer separation restricts strategy information from execution agents and vice versa. |
| A.8.4 | Access to source code | Yes | Implemented | Git-based repository with branch protection rules. [`CODEOWNERS`](../../../CODEOWNERS) controls merge permissions per path. PR reviews required for all changes. Agent access scoped to specific repositories/paths via bot account permissions. **Deployment-specific:** adopter must configure repository access controls in their Git hosting platform. |
| A.8.5 | Secure authentication | Yes | Partial | Cryptography policy ([`org/4-quality/policies/cryptography.md`](../../../org/4-quality/policies/cryptography.md)) defines authentication standards (mTLS, TLS 1.3). Security policy ([`org/4-quality/policies/security.md`](../../../org/4-quality/policies/security.md)) mandates strong authentication. **Deployment-specific:** adopter must implement MFA, SSO, certificate-based auth, and credential rotation per the policy requirements. |
| A.8.6 | Capacity management | Yes | Partial | Performance policy ([`org/4-quality/policies/performance.md`](../../../org/4-quality/policies/performance.md)) defines capacity management requirements including monitoring, scaling thresholds, and resource planning. Observability platform tracks resource utilization. **Deployment-specific:** adopter must configure auto-scaling, capacity alerts, and resource quotas. |
| A.8.7 | Protection against malware | Yes | Partial | Agent security policy addresses agent execution sandboxing and input validation. Delivery policy mandates dependency scanning and SAST/DAST in CI/CD. **Deployment-specific:** adopter must implement endpoint anti-malware, container image scanning, and runtime protection. |
| A.8.8 | Management of technical vulnerabilities | Yes | Partial | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) requires dependency scanning in CI/CD. Agent security policy addresses vulnerability remediation for agent components. **Deployment-specific:** adopter must implement vulnerability scanning, patch management, CVE tracking, and remediation SLAs. |
| A.8.9 | Configuration management | Yes | Implemented | [`CONFIG.yaml`](../../../CONFIG.yaml) is the central configuration file, version-controlled in Git. All infrastructure-as-code and configuration changes go through PR review. AGENTS.md Rule 10 requires version bumps on every change. Git history provides complete configuration change audit trail. |
| A.8.10 | Information deletion | Yes | Partial | Data classification policy ([`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md)) defines retention and deletion requirements per classification level. Log retention policy defines log lifecycle. AGENTS.md Rule 14 governs work artifact archiving (never delete, archive). **Deployment-specific:** adopter must implement automated data deletion workflows for expired data, GDPR right-to-erasure requests, and decommissioned systems. |
| A.8.11 | Data masking | Yes | Partial | Data classification policy addresses data handling by classification level. Privacy policy ([`org/4-quality/policies/privacy.md`](../../../org/4-quality/policies/privacy.md)) requires data minimization. **Deployment-specific:** adopter must implement data masking, pseudonymization, and tokenization for sensitive data in non-production environments and analytics. |
| A.8.12 | Data leakage prevention | Yes | Partial | Privacy policy defines data leakage prevention principles. Data classification policy restricts data handling. Agent security policy constrains agent data exfiltration paths. AGENTS.md rules prevent agents from committing secrets (.env, credentials). **Deployment-specific:** adopter must implement DLP tools, egress filtering, and data loss monitoring. |
| A.8.13 | Information backup | Yes | Partial | Availability policy ([`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md)) defines backup requirements including RPO targets, backup frequency, and encryption. Git repository provides inherent backup for governance artifacts. **Deployment-specific:** adopter must implement automated backups for databases, object storage, and infrastructure state, with regular restore testing. |
| A.8.14 | Redundancy of information processing facilities | Yes | Partial | Availability policy defines redundancy requirements including multi-AZ deployment, failover mechanisms, and RTO targets. **Deployment-specific:** adopter must implement infrastructure redundancy (multi-region, load balancing, database replication) per availability tier. |
| A.8.15 | Logging | Yes | Implemented | Observability policy ([`org/4-quality/policies/observability.md`](../../../org/4-quality/policies/observability.md)) mandates comprehensive logging. Log retention policy ([`org/4-quality/policies/log-retention.md`](../../../org/4-quality/policies/log-retention.md)) defines retention periods and immutability. AGENTS.md Rule 9a requires every agent action to produce OpenTelemetry spans. OTel contract ([`docs/otel-contract.md`](../otel-contract.md)) defines canonical attribute names. Git history provides governance audit log. |
| A.8.16 | Monitoring activities | Yes | Implemented | Observability policy defines monitoring requirements. AGENTS.md Rule 9b requires agents to consume observability data. Anomaly detection from observability platform generates automated signals. Performance policy defines alerting thresholds. Integration registry governs monitoring tool connections. |
| A.8.17 | Clock synchronization | Yes | To be assessed | **Deployment-specific:** adopter must configure NTP/PTP time synchronization across all information processing systems. OTel spans require accurate timestamps for trace correlation. Cloud providers typically provide synchronized clocks — adopter must verify and document. |
| A.8.18 | Use of privileged utility programs | Yes | Partial | Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) restricts agent access to privileged utilities. AGENTS.md Rule 8 requires all integrations to go through governed channels. **Deployment-specific:** adopter must restrict and audit use of privileged system utilities (database admin tools, infrastructure CLIs, debug tools). |
| A.8.19 | Installation of software on operational systems | Yes | To be assessed | **Deployment-specific:** adopter must control software installation on operational systems through approved package registries, container image policies, and change management. Delivery policy governs deployment pipelines. |
| A.8.20 | Networks security | Yes | Partial | Security policy ([`org/4-quality/policies/security.md`](../../../org/4-quality/policies/security.md)) defines network security requirements. Cryptography policy mandates TLS 1.3 for all network communications. **Deployment-specific:** adopter must implement network security controls (firewalls, WAF, IDS/IPS, network monitoring) per security policy requirements. |
| A.8.21 | Security of network services | Yes | Partial | Security policy defines web service security requirements. Cryptography policy mandates mTLS for service-to-service communication. Integration registry tracks all external network service dependencies. **Deployment-specific:** adopter must implement API gateway security, rate limiting, and network service SLAs. |
| A.8.22 | Segregation of networks | Yes | To be assessed | **Deployment-specific:** adopter must implement network segmentation (VPCs/VNets, subnets, security groups, network policies) to isolate environments and workloads. Security policy provides architectural guidance. |
| A.8.23 | Web filtering | Yes | To be assessed | **Deployment-specific:** adopter must implement web filtering for user internet access and agent outbound communications. Agent security policy restricts agent network access to approved integrations. |
| A.8.24 | Use of cryptography | Yes | Implemented | Cryptography policy ([`org/4-quality/policies/cryptography.md`](../../../org/4-quality/policies/cryptography.md)) defines approved algorithms, key lengths, protocols (TLS 1.3, mTLS), key management practices, and certificate lifecycle. Covers encryption at rest, in transit, and for backups. |
| A.8.25 | Secure development life cycle | Yes | Implemented | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) defines the secure SDLC including threat modeling in design, SAST/DAST in CI/CD, dependency scanning, code review, and security testing. Agent security policy adds AI-specific secure development requirements. 4-loop process (`process/`) embeds security at every stage. |
| A.8.26 | Application security requirements | Yes | Implemented | Delivery policy defines application security requirements including input validation, authentication, authorization, error handling, and logging. Technical design template mandates security requirements section. Quality layer validates security requirements in design reviews. |
| A.8.27 | Secure system architecture and engineering principles | Yes | Implemented | Architecture policy ([`org/4-quality/policies/architecture.md`](../../../org/4-quality/policies/architecture.md)) defines architectural principles. Delivery policy mandates defense-in-depth, least privilege, fail-secure, and zero-trust principles. Technical design template requires architecture review. AGENTS.md Rule 9c requires security consideration in design phase. |
| A.8.28 | Secure coding | Yes | Implemented | Agent security policy ([`org/4-quality/policies/agent-security.md`](../../../org/4-quality/policies/agent-security.md)) defines secure coding requirements for agent development. Delivery policy mandates code review, static analysis, and secure coding standards. PR-based workflow ensures all code is reviewed before merge. |
| A.8.29 | Security testing in development and acceptance | Yes | Implemented | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) mandates shift-left security testing: SAST in CI, DAST in staging, dependency vulnerability scanning, and penetration testing before production release. Agent evaluation policy ([`org/4-quality/policies/agent-eval.md`](../../../org/4-quality/policies/agent-eval.md)) adds AI-specific testing. |
| A.8.30 | Outsourced development | Yes | Partial | Delivery policy addresses outsourced development security requirements. Vendor risk management policy defines supplier assessment for development partners. **Deployment-specific:** adopter must implement contractual security requirements, code escrow, and IP protection for outsourced development. |
| A.8.31 | Separation of development, test and production environments | Yes | Implemented | Delivery policy ([`org/4-quality/policies/delivery.md`](../../../org/4-quality/policies/delivery.md)) mandates environment separation (development, staging, production). CI/CD pipeline enforces promotion gates between environments. Configuration management via `CONFIG.yaml` supports environment-specific settings. |
| A.8.32 | Change management | Yes | Implemented | PR-based change management for all governed artifacts. [`CODEOWNERS`](../../../CODEOWNERS) enforces approval requirements. AGENTS.md Rule 3 mandates PR workflow. Delivery policy defines change management procedures including rollback plans. CI/CD validates changes before deployment. Git history provides complete change audit trail. |
| A.8.33 | Test information | Yes | Partial | Delivery policy addresses test data management. Data classification policy applies to test environments. **Deployment-specific:** adopter must ensure production data is not used in test environments without anonymization/masking, and that test data is classified and protected appropriately. |
| A.8.34 | Protection of information systems during audit testing | Yes | Partial | Availability policy ([`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md)) defines audit log protection with WORM (Write Once Read Many) requirements. Log retention policy ensures audit data integrity. **Deployment-specific:** adopter must plan and control audit testing activities to minimize operational impact, restrict audit tool access, and protect audit evidence. |

---

## Summary Statistics

| Theme | Total | Applicable | Implemented | Partial | Planned | N/A | To be assessed |
|-------|------:|----------:|------------:|--------:|--------:|----:|---------------:|
| A.5 Organizational | 37 | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| A.6 People | 8 | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| A.7 Physical | 14 | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| A.8 Technological | 34 | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **Total** | **93** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** |

> **Instructions:** After reviewing all controls and finalizing applicability decisions, compute the totals per theme and overall. Remove this note in the final document.

---

## Risk Treatment Cross-Reference

Each applicable control should map to one or more risks in the risk assessment. Document the cross-reference below or in a separate risk treatment plan.

| Control | Risk ID | Risk Description | Treatment Option |
|---------|---------|-----------------|-----------------|
| {{CONTROL}} | {{RISK_ID}} | {{RISK_DESCRIPTION}} | Mitigate / Transfer / Accept / Avoid |

> **Instructions:** Populate this table after completing the risk assessment (ISO 27001 Clause 6.1.2). Every applicable control must trace to at least one identified risk. Remove this note in the final document.

---

## Justification for Non-Applicable Controls

Any control marked as "Not applicable" must have a documented justification per ISO 27001 Clause 6.1.3d. Review the table above — justifications are included in the Implementation / Justification column for each control.

> **Auditor note:** If your deployment has no physical premises (fully cloud-native, fully remote), certain A.7 physical controls may be marked "Not applicable" with justification referencing the cloud provider's certifications and the shared responsibility model. Always verify with your certification body before excluding controls.

---

## Review and Maintenance

This Statement of Applicability is reviewed:

- **Annually** as part of the ISMS management review cycle
- **Upon significant change** to the organization, technology, threat landscape, or regulatory environment
- **After major security incidents** that reveal control gaps
- **When the risk assessment is updated** (controls must align with current risk treatment plan)

| Trigger | Action | Owner |
|---------|--------|-------|
| Annual review | Full SoA reassessment against current risk register | ISMS Owner |
| New regulation or standard | Evaluate impact on control applicability | Legal/Compliance |
| New system or service | Evaluate control coverage for new assets | IT Security |
| Risk assessment update | Align controls with updated risk treatment | Risk Owner |
| Major security incident | Evaluate control effectiveness gaps | Incident Commander + ISMS Owner |
| Framework version upgrade | Review pre-populated mappings against new framework version | ISMS Owner |

---

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial Statement of Applicability |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-14 | Initial SoA template with all 93 ISO/IEC 27001:2022 Annex A controls pre-mapped to Agentic Enterprise framework |
