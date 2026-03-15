<!-- placeholder-ok -->
# HIPAA — Privacy Officer and Security Officer Designation

> **Implements:** Designated Privacy Officer and Security Officer with defined responsibilities
> **Regulation:** HIPAA (45 CFR §164.530(a)(1) — Privacy Officer; §164.308(a)(2) — Security Officer)
> **Severity:** High — officer designation is mandatory; absence is a common OCR enforcement finding
> **Related issue:** [#148](https://github.com/wlfghdr/agentic-enterprise/issues/148)
> **Related compliance doc:** [HIPAA Compliance Reference](../hipaa.md)

---

## 1. Purpose

HIPAA requires every Covered Entity and Business Associate to designate a Privacy Officer responsible for developing and implementing privacy policies and procedures, and a Security Officer responsible for developing and implementing security policies and procedures. These are mandatory designations, not optional roles.

The Agentic Enterprise framework defines role-based responsibility via `CODEOWNERS` and assigns security artifact ownership through the [Security Policy](../../../org/4-quality/policies/security.md). This guide extends that foundation with specific Privacy Officer and Security Officer appointment requirements, HIPAA-specific responsibilities for these officers, and officer responsibilities for AI/agent system oversight — including oversight of PHI processing by agents, agent security configuration review, and agent audit trail monitoring.

This guide defines the Privacy Officer and Security Officer requirements, responsibilities, AI/agent-specific oversight duties, reporting structure, and a verification checklist.

---

## 2. Privacy Officer Requirements

### 2a. Designation Requirement (§164.530(a)(1))

The Privacy Rule requires the Covered Entity to designate a Privacy Officer who is responsible for the development and implementation of the CE's privacy policies and procedures.

| Requirement | Detail | CFR Reference |
|------------|--------|---------------|
| **Mandatory designation** | Every CE must designate a Privacy Officer — this is not optional | §164.530(a)(1)(i) |
| **Named individual** | Must be a specific person, not a department or committee | §164.530(a)(1)(i) |
| **Contact point** | Must also designate a contact person or office for receiving complaints and providing information about the NPP | §164.530(a)(1)(ii) |
| **May be same as Security Officer** | In smaller organizations, the Privacy Officer and Security Officer may be the same person | HHS guidance |
| **Business Associates** | BAs are not required to designate a Privacy Officer by the Privacy Rule, but must designate a Security Officer; best practice is to designate both | §164.530 applies to CEs; §164.308(a)(2) applies to CEs and BAs |

### 2b. Privacy Officer Responsibilities

| Responsibility | Description | Evidence |
|---------------|-------------|---------|
| **Policy development** | Develop and maintain privacy policies and procedures compliant with the Privacy Rule | Version-controlled policies in `org/4-quality/policies/` |
| **Policy implementation** | Ensure privacy policies are implemented in practice across the organization | Implementation evidence, audit results |
| **NPP management** | Develop, distribute, and update the Notice of Privacy Practices | NPP document, distribution records, acknowledgment forms |
| **Training oversight** | Ensure all workforce members receive required privacy training | Training completion records, programme documentation |
| **Complaint handling** | Receive and investigate privacy complaints from individuals | Complaint register, investigation records |
| **Patient rights administration** | Oversee implementation of patient rights (access, amendment, accounting, restrictions, confidential communications) | Rights request logs, response records |
| **Authorization management** | Oversee the authorization process for uses and disclosures requiring individual authorization | Authorization forms, tracking records |
| **Minimum necessary oversight** | Define minimum necessary standards for each role and use case | Role-based access policies, minimum necessary determinations |
| **Sanctions administration** | Apply sanctions for workforce members who violate privacy policies | Sanctions policy, sanctions records |
| **Breach assessment** | Participate in breach risk assessments and notification decisions | Breach investigation records, notification records |
| **Regulatory liaison** | Serve as point of contact for HHS OCR inquiries and investigations | Correspondence records |
| **Documentation retention** | Ensure all required documentation is retained for 6 years | Retention schedule, storage verification |

---

## 3. Security Officer Requirements

### 3a. Designation Requirement (§164.308(a)(2))

The Security Rule requires the Covered Entity (and Business Associate, per HITECH) to designate a Security Officer who is responsible for the development and implementation of security policies and procedures.

| Requirement | Detail | CFR Reference |
|------------|--------|---------------|
| **Mandatory designation** | Every CE and BA must designate a Security Officer | §164.308(a)(2) |
| **Named individual** | Must be a specific person responsible for security | §164.308(a)(2) |
| **Scope** | Responsible for all aspects of the Security Rule — administrative, physical, and technical safeguards | §164.308(a)(2) |
| **May be same as Privacy Officer** | Permitted in smaller organizations; but consider separation of duties in larger organizations | HHS guidance |

### 3b. Security Officer Responsibilities

| Responsibility | Description | Evidence |
|---------------|-------------|---------|
| **Security policy development** | Develop and maintain security policies and procedures for administrative, physical, and technical safeguards | Version-controlled policies in `org/4-quality/policies/` |
| **Risk analysis** | Conduct and maintain an accurate and thorough risk analysis of ePHI (§164.308(a)(1)(ii)(A)) | Risk assessment reports, risk register |
| **Risk management** | Implement security measures sufficient to reduce risks to ePHI to a reasonable and appropriate level (§164.308(a)(1)(ii)(B)) | Risk treatment plans, remediation evidence |
| **Access management** | Implement policies and procedures for authorizing access to ePHI (§164.308(a)(4)) | Access control policies, access logs, provisioning/deprovisioning records |
| **Security awareness and training** | Implement a security awareness and training programme for all workforce members (§164.308(a)(5)) | Training programme, completion records, security reminders |
| **Security incident management** | Implement policies and procedures for identifying, responding to, and mitigating security incidents (§164.308(a)(6)) | Incident response policy, incident records, postmortems |
| **Contingency planning** | Establish policies and procedures for responding to an emergency or other occurrence that damages systems containing ePHI (§164.308(a)(7)) | Contingency plan, backup verification, DR drill records |
| **Evaluation** | Perform periodic technical and non-technical evaluations of security policies and procedures (§164.308(a)(8)) | Evaluation reports, audit results |
| **Business associate security** | Ensure BA contracts include appropriate security requirements (§164.308(b), §164.314(a)) | BAA records, BA security assessments |
| **Technical safeguard management** | Oversee access controls, audit controls, integrity controls, transmission security (§164.312) | Technical control configurations, audit logs |
| **Documentation management** | Maintain security documentation and retain for 6 years (§164.316) | Documentation inventory, retention verification |

---

## 4. Combined vs. Separate Officers

### 4a. When One Person May Serve Both Roles

| Factor | Combined (Same Person) | Separate (Different People) |
|--------|----------------------|---------------------------|
| **Organization size** | Small organizations with limited workforce | Larger organizations with dedicated compliance staff |
| **PHI volume** | Limited PHI processing | High-volume PHI processing |
| **Regulatory complexity** | Single state, straightforward operations | Multi-state, complex operations, research |
| **Risk profile** | Lower risk — limited systems, limited BA relationships | Higher risk — many systems, many BAs, complex data flows |
| **HIPAA text** | Permitted — neither rule prohibits combination | Not required — but recommended for separation of duties |

### 4b. Considerations for Combined Role

| Consideration | Guidance |
|--------------|---------|
| **Workload** | Ensure the combined officer has sufficient time and resources for both privacy and security responsibilities |
| **Expertise** | The combined officer must have competency in both privacy law/policy and information security |
| **Conflict of interest** | Monitor for situations where privacy and security interests conflict (e.g., security monitoring vs. privacy minimization) |
| **Backup** | Designate a backup officer to act in the primary officer's absence |
| **Documentation** | Clearly document that the same individual holds both designations |

---

## 5. Officer Responsibilities for AI/Agent Systems

When the organization uses AI or agent systems that process PHI, both the Privacy Officer and Security Officer have additional oversight responsibilities.

### 5a. Privacy Officer — AI/Agent Oversight

| Responsibility | Description | Framework Reference |
|---------------|-------------|-------------------|
| **PHI access review** | Review and approve agent system configurations that grant access to PHI | [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) — tool-level access controls |
| **Minimum necessary for agents** | Define minimum necessary PHI access for each agent role and task | `AGENT.md` hierarchy, agent tool permissions |
| **Prompt PHI monitoring** | Oversee controls that prevent unnecessary PHI inclusion in AI prompts and context windows | [PHI Classification Guide](hipaa-phi-classification.md) — Section 6a |
| **Output review policy** | Establish policy for reviewing agent outputs for unauthorized PHI disclosure | Output filtering controls |
| **Patient rights and agents** | Ensure agent-processed PHI is included in patient rights responses (access, amendment, accounting) | [NPP and Patient Rights Guide](hipaa-npp-patient-rights.md) — Section 4 |
| **Agent disclosure logging** | Verify that agent-initiated PHI disclosures are logged for accounting purposes | OTel telemetry with `hipaa.disclosure.*` attributes |
| **AI vendor BAA review** | Ensure BAAs are in place with all AI vendors/subprocessors that may access PHI | [BAA Template Guide](hipaa-baa-template.md) — Section 4 |
| **Training on AI PHI risks** | Include AI-specific PHI handling in workforce training programme | [Workforce Training Guide](hipaa-workforce-training.md) — Section 4 |

### 5b. Security Officer — AI/Agent Oversight

| Responsibility | Description | Framework Reference |
|---------------|-------------|-------------------|
| **Agent security configuration review** | Review and approve agent security configurations, including tool permissions, network access, and data access boundaries | [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) |
| **Agent risk assessment** | Include AI/agent systems in ePHI risk analysis — assess risks of PHI processing by agents, prompt injection, context leakage, model extraction | [Risk Management Policy](../../../org/4-quality/policies/risk-management.md) |
| **Agent audit trail review** | Periodically review agent OTel telemetry for unauthorized PHI access, anomalous data access patterns, and security incidents | [Observability Policy](../../../org/4-quality/policies/observability.md), [OTel Contract](../../otel-contract.md) |
| **Agent access controls** | Verify that agent systems implement access controls equivalent to human workforce requirements (unique identity, authentication, authorization, audit) | Security Policy — authentication requirements |
| **Agent incident response** | Include agent-related PHI security incidents in the incident response programme | [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) |
| **Agent encryption** | Verify that ePHI processed by agents is encrypted at rest and in transit | [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) |
| **Agent subprocessor security** | Assess security of AI model providers and infrastructure subprocessors handling ePHI | [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md) |
| **Agent log retention** | Ensure agent PHI access logs are retained for the required period (6 years for HIPAA, aligned with log retention policy) | [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) |

---

## 6. Reporting Structure

### 6a. Organizational Placement

| Principle | Guidance |
|-----------|---------|
| **Authority** | The Privacy Officer and Security Officer must have sufficient authority to implement and enforce policies — they should report to senior leadership, not to the teams they oversee |
| **Independence** | Officers should not be subordinate to the functions they are responsible for overseeing (e.g., the Security Officer should not report to IT operations if IT operations manages ePHI systems) |
| **Access** | Officers must have access to all relevant systems, documentation, workforce members, and leadership for carrying out their duties |
| **Budget** | Officers must have or be able to request adequate resources for compliance activities |
| **Board/executive reporting** | Privacy and security compliance status should be reported to the board or executive leadership at least quarterly |

### 6b. Framework Integration

| Framework Component | Officer Integration |
|--------------------|-------------------|
| **CODEOWNERS** | Privacy Officer and Security Officer should be listed as required reviewers for: privacy policies, security policies, data classification changes, BAA/DPA artifacts, agent security configurations |
| **CONFIG.yaml** | Add officer designations with name, title, contact, and effective date |
| **Incident Response Policy** | Officers are notified at SEV1-SEV2 incidents involving PHI; Privacy Officer participates in breach risk assessment |
| **Quality Layer (org/4-quality/)** | Officers review and approve quality policies related to privacy and security |
| **Agent instructions (AGENT.md)** | Reference officer authority in agent boundary definitions — agents escalate PHI decisions to designated officers |
| **Work signals (work/signals/)** | Officers review privacy and security signals for compliance implications |

### 6c. CONFIG.yaml Officer Designation

```yaml
# Add to CONFIG.yaml under a hipaa section
hipaa:
  privacy_officer:
    name: "{{PRIVACY_OFFICER_NAME}}"
    title: "{{PRIVACY_OFFICER_TITLE}}"
    email: "{{PRIVACY_OFFICER_EMAIL}}"
    effective_date: "{{YYYY-MM-DD}}"
    backup: "{{BACKUP_OFFICER_NAME}}"
  security_officer:
    name: "{{SECURITY_OFFICER_NAME}}"
    title: "{{SECURITY_OFFICER_TITLE}}"
    email: "{{SECURITY_OFFICER_EMAIL}}"
    effective_date: "{{YYYY-MM-DD}}"
    backup: "{{BACKUP_OFFICER_NAME}}"
  combined_role: false  # set to true if same person holds both roles
```

---

## 7. Verification Checklist

### Privacy Officer Designation
- [ ] Privacy Officer designated by name (§164.530(a)(1)(i))
- [ ] Contact person/office designated for complaints and NPP inquiries (§164.530(a)(1)(ii))
- [ ] Designation documented with effective date
- [ ] Privacy Officer has appropriate qualifications (privacy law, HIPAA knowledge)
- [ ] Privacy Officer has sufficient authority and organizational access
- [ ] Backup Privacy Officer designated for absence coverage
- [ ] Privacy Officer designation recorded in CONFIG.yaml or equivalent

### Security Officer Designation
- [ ] Security Officer designated by name (§164.308(a)(2))
- [ ] Designation documented with effective date
- [ ] Security Officer has appropriate qualifications (information security, HIPAA Security Rule knowledge)
- [ ] Security Officer has sufficient authority and organizational access
- [ ] Backup Security Officer designated for absence coverage
- [ ] Security Officer designation recorded in CONFIG.yaml or equivalent

### If Combined Role
- [ ] Combined designation documented and approved
- [ ] Combined officer has competency in both privacy and security domains
- [ ] Workload assessment confirms feasibility of combined role
- [ ] Separation of duties risk assessed and mitigated

### Privacy Officer Responsibilities Active
- [ ] Privacy policies developed and maintained
- [ ] NPP created, distributed, and maintained
- [ ] Privacy training programme operational
- [ ] Complaint handling process established
- [ ] Patient rights administration operational (access, amendment, accounting, restrictions, confidential communications)
- [ ] Authorization management process in place
- [ ] Minimum necessary standards defined per role
- [ ] Sanctions policy established and communicated
- [ ] Breach assessment participation documented
- [ ] 6-year documentation retention verified

### Security Officer Responsibilities Active
- [ ] Security policies developed and maintained
- [ ] Risk analysis completed and maintained
- [ ] Risk management measures implemented
- [ ] Access management policies and procedures operational
- [ ] Security awareness and training programme operational
- [ ] Security incident procedures established
- [ ] Contingency plan established and tested
- [ ] Periodic security evaluations conducted
- [ ] BA security requirements verified
- [ ] Technical safeguards operational (access, audit, integrity, transmission)
- [ ] 6-year documentation retention verified

### AI/Agent System Oversight
- [ ] Privacy Officer reviews agent PHI access configurations
- [ ] Privacy Officer defines minimum necessary PHI access for agent roles
- [ ] Privacy Officer oversees prompt sanitization and output filtering controls
- [ ] Privacy Officer verifies agent disclosure logging for accounting
- [ ] Privacy Officer reviews AI vendor BAAs
- [ ] Security Officer reviews agent security configurations
- [ ] Security Officer includes agents in ePHI risk analysis
- [ ] Security Officer periodically reviews agent audit trails
- [ ] Security Officer verifies agent access controls (identity, authentication, authorization, audit)
- [ ] Security Officer verifies agent ePHI encryption (at rest and in transit)
- [ ] Security Officer assesses AI subprocessor security
- [ ] Security Officer verifies agent PHI log retention compliance

### Reporting and Governance
- [ ] Officers report to senior leadership (not to functions they oversee)
- [ ] Quarterly compliance status reporting to board/executive leadership
- [ ] Officers listed as required reviewers in CODEOWNERS for relevant artifacts
- [ ] Officer authority referenced in agent instructions for PHI escalation
- [ ] Officer designations communicated to all workforce members
