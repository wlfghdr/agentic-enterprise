<!-- placeholder-ok -->
# ISO 42001 — Conformity Assessment Preparation Guide

> **Closes gap:** Guidance for third-party ISO 42001 certification process
> **Standard:** ISO/IEC 42001:2023 — Artificial Intelligence Management Systems
> **Severity:** High — certification still requires an external body
> **Related issue:** [#127](https://github.com/wlfghdr/agentic-enterprise/issues/127)
> **Related compliance doc:** [ISO 42001 Compliance Reference](../iso-42001.md)

---

## 1. Gap Summary

The Agentic Enterprise framework provides much of the governance structure an ISO 42001 auditor will expect to see:

- AI governance rules
- risk classification and risk management
- observability and logging requirements
- versioned governance and approval records
- agent type definitions and model governance surfaces

What it does **not** do is replace the external certification process. ISO 42001 certification still requires an accredited certification body to review the organization's documentation and implementation.

That means the framework can close the **guidance gap**, but not the **external assessment dependency**.

This guide explains:

1. how ISO 42001 certification typically works
2. what to prepare for Stage 1 and Stage 2 audits
3. what evidence the framework already provides
4. what adopters still must implement or demonstrate themselves
5. how to stay ready for surveillance audits after certification

---

## 2. How ISO 42001 Certification Typically Works

ISO 42001 certification usually follows the standard management-system certification pattern:

| Phase | Purpose | Typical Output |
|-------|---------|----------------|
| **Readiness / pre-assessment** | Internal gap analysis before formal certification | Action list and remediation plan |
| **Stage 1 audit** | Documentation review and scope readiness check | Stage 1 findings, readiness decision for Stage 2 |
| **Stage 2 audit** | Implementation and operating-effectiveness review | Certification recommendation or nonconformities |
| **Certification decision** | Certification body decision based on audit evidence | Certificate issued or deferred |
| **Surveillance audits** | Ongoing verification that the AIMS is maintained | Annual surveillance findings |
| **Recertification** | Full reassessment at the end of the cycle | Renewed certificate or recertification findings |

### 2.1 Stage 1 Audit

Stage 1 is mainly a **documentation and readiness** audit. The certification body usually checks:

- whether the AIMS scope is defined
- whether the AI system inventory exists
- whether key policies and responsibilities are documented
- whether the organization understands its AI-related risks and obligations
- whether the organization is ready to proceed to implementation testing

### 2.2 Stage 2 Audit

Stage 2 tests whether the AIMS is actually **implemented and operating**. The certification body typically looks for:

- evidence that the documented processes are in use
- ownership and accountability in practice
- monitoring and review records
- risk treatment in action
- evidence of human oversight and AI governance controls for in-scope systems
- nonconformity handling and improvement cycles

### 2.3 Surveillance Audits

After certification, surveillance audits usually verify that:

- the AIMS remains in use
- the scope is still accurate
- in-scope AI systems and providers are kept current
- management review and internal audit continue
- nonconformities and incidents are being handled through the improvement process

---

## 3. Choosing a Certification Body

Selecting the certification body is not a procurement afterthought. The wrong auditor can slow the process or misread an AI-heavy operating model.

### 3.1 Selection Criteria

Prefer certification bodies that can demonstrate experience with:

- ISO 27001 or other Annex SL management-system audits
- AI/ML systems, not just general software
- cloud-native and API-driven environments
- third-party AI providers and model governance
- regulated or high-trust software environments

### 3.2 Questions to Ask During Selection

- Have you already certified organizations against ISO 42001?
- How do you evaluate AI systems that depend on third-party model providers?
- How do you expect the AI system inventory to be structured?
- What evidence do you typically want for human oversight, monitoring, and model/provider governance?
- How do you scope multi-agent or AI-assisted workflows that are partly internal and partly customer-facing?

### 3.3 Practical Selection Guidance

- Request a sample document request list or Stage 1 preparation list.
- Ask whether the audit team includes AI-specific domain expertise.
- Confirm expected timelines, document submission windows, and surveillance cadence.
- Make sure the certification body can audit the jurisdictions relevant to your deployment and customers.

---

## 4. What the Framework Already Provides vs. What Adopters Must Supply

The framework provides strong scaffolding, but certification bodies certify an implemented AIMS, not a template repository.

| Topic | Framework Provides | Adopter Must Still Provide |
|-------|--------------------|----------------------------|
| AIMS structure | Layer model, policies, approval model, improvement loop | Actual organizational ownership, scope approval, and operating records |
| AIMS scope | Organizational model, agent registry, and AI governance context | Completed scope statement for the real deployment |
| AI system inventory | AI risk-tier model and agent governance surfaces | Filled inventory for all deployed AI systems |
| AI governance | Risk tiers, model governance, fairness and explainability policy | System-specific evidence that those controls are implemented |
| Observability | Telemetry contract and observability policy | A live observability stack with actual traces, metrics, logs, and review evidence |
| Vendor governance | Vendor-risk policy and AI vendor assessment approach | Real vendor assessments, current attestations, and provider-specific controls |
| Risk management | Risk scoring methodology and governance model | Real risk entries, treatment actions, and review records |
| Continuous improvement | Signal and retrospective loops | Evidence that nonconformities and incidents are actually handled through those loops |
| Certification | Preparation guidance | Selection and engagement of the external certification body |

This division is important: the framework can make the audit **prepared**, but only a real deployment can make it **certifiable**.

---

## 5. Stage 1 Readiness Checklist

Use this checklist before engaging the certification body for Stage 1.

- [ ] The AIMS scope statement exists and is approved
- [ ] The AI system inventory exists and is current
- [ ] AI governance responsibilities are assigned and documented
- [ ] In-scope AI systems have documented risk tiers
- [ ] Relevant policies are approved and current
- [ ] External AI providers and dependencies are identified
- [ ] The organization can explain which AI systems are in scope and why
- [ ] Known exclusions are explicitly documented with justification
- [ ] The organization can describe how AI risk, oversight, and monitoring are governed
- [ ] Management can explain the purpose of the AIMS and who owns it

### 5.1 Documents Commonly Needed for Stage 1

- AIMS scope statement
- AI system inventory
- AI governance policy and related quality policies
- risk management methodology
- organizational roles and approval structure
- relevant technical and operational documentation for in-scope AI systems

If these artifacts are incomplete, Stage 1 often ends with a readiness gap rather than a clean move to Stage 2.

---

## 6. Stage 2 Readiness Checklist

Use this checklist before the implementation audit.

- [ ] Scope and inventory documents are not just present but actively maintained
- [ ] In-scope AI systems have owners who can explain intended use and controls
- [ ] Human oversight mechanisms exist in practice, not only in policy
- [ ] Monitoring and logging are active for in-scope AI systems
- [ ] Risk assessments exist for relevant AI systems and are current
- [ ] Vendor and provider governance exists for external AI dependencies
- [ ] Review and approval evidence exists for relevant AI changes
- [ ] Nonconformities, incidents, or exceptions are tracked and acted upon
- [ ] The organization can show examples of the improvement loop operating
- [ ] Staff responsible for the AIMS understand their roles during the audit

### 6.1 Evidence the Auditor Will Likely Sample

- approved policies and their version history
- examples of AI system risk classification
- records of governance decisions and human approvals
- monitoring or dashboard evidence for AI systems
- vendor/provider review records
- evidence of issue handling, corrective action, or improvement signals

---

## 7. Surveillance Audit Readiness

Certification is not the end state. Surveillance audits test whether the AIMS remains alive.

Keep the following continuously current:

- AIMS scope statement
- AI system inventory
- provider and dependency list
- management review inputs and outputs
- internal audit outputs
- risk reviews and treatment updates
- records of significant AI system changes

### 7.1 Triggers That Should Force AIMS Review

- onboarding a new AI system or agent type
- switching model provider or major model version
- changing the intended use of an AI system
- moving from internal-only to customer-facing AI use
- incidents, regulatory changes, or material audit findings

If the scope changes and the documentation does not, surveillance findings are likely.

---

## 8. Suggested Certification Timeline

| Phase | Typical Duration | Notes |
|-------|------------------|-------|
| Internal readiness and gap closure | 1-3 months | Longer if inventory, scope, or monitoring are immature |
| Certification body selection and scheduling | 1-2 months | Start early; specialist capacity may be limited |
| Stage 1 preparation and audit | 2-6 weeks | Depends on document maturity |
| Stage 1 remediation | 2-6 weeks | Close documentation findings before Stage 2 |
| Stage 2 preparation and audit | 1-2 months | Requires implemented and evidenced controls |
| Post-audit remediation and certification decision | 2-8 weeks | Depends on nonconformity severity |

Treat these as planning ranges, not guarantees.

---

## 9. Final Readiness Questions

Before you call the organization ready for ISO 42001 certification, be able to answer:

- Can we show exactly which AI systems are in scope?
- Can we explain why each one has its assigned risk tier?
- Can we show how human oversight works in practice?
- Can we show monitoring evidence for in-scope AI systems?
- Can we show how third-party AI providers are governed?
- Can we show how findings, incidents, and changes feed back into improvement?

If any of those answers is weak, fix that before formal audit scheduling.

---

## References

- [ISO 42001 Compliance Reference](../iso-42001.md)
- [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md)
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
- [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md)
- [Observability Policy](../../../org/4-quality/policies/observability.md)
