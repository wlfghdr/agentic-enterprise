<!-- placeholder-ok -->
# ISO 42001 — AIMS Scope Statement and AI System Inventory

> **Closes gap:** Formal AIMS scope statement and AI system inventory
> **Standard:** ISO/IEC 42001:2023 — Artificial Intelligence Management Systems
> **Severity:** High — required for certification readiness
> **Related issue:** [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126)
> **Related compliance doc:** [ISO 42001 Compliance Reference](../iso-42001.md)

---

## 1. Gap Summary

ISO/IEC 42001 clause 4 requires an organization to define the scope of its AI Management System (AIMS) and to understand which AI systems fall within that boundary. The Agentic Enterprise framework already provides much of the governance foundation:

- a 5-layer operating model with defined authorities
- an agent type registry
- an AI governance policy with risk tiers
- observability requirements for AI behavior
- vendor governance for external AI providers

What was missing was the **formal certification artifact layer**:

1. a dedicated AIMS scope statement
2. a governed inventory of all AI systems in scope with risk classification

Without those artifacts, an adopter can have strong AI governance and still be unable to show an auditor exactly which systems, processes, organizational units, and dependencies are inside the AIMS boundary.

This guide closes that framework gap by introducing:

- an [AIMS scope statement template](../templates/_TEMPLATE-aims-scope.md)
- an [AI system inventory template](../templates/_TEMPLATE-ai-system-inventory.md)

Use these together. The scope statement defines the AIMS boundary; the inventory provides the detailed list of AI systems that live inside that boundary.

---

## 2. What ISO 42001 Requires for Scope and Inventory

The AIMS scope must be grounded in clauses 4.1, 4.2, and 4.3.

| Requirement | Clause Reference | What Must Be Documented |
|-------------|------------------|-------------------------|
| Context of the organization | 4.1 | Internal and external issues that affect the AI management system |
| Interested parties | 4.2 | Relevant stakeholders and their AI-related expectations |
| Boundaries and applicability of the AIMS | 4.3 | Organizational units, services, AI systems, locations, interfaces, and exclusions |
| AI system inventory | Clause 4 foundation | Complete list of AI systems in scope with risk classification and ownership |

In practice, auditors typically want to see:

- which AI systems are in scope
- which systems are explicitly out of scope
- who owns each AI system
- what models or providers are used
- what risk tier applies to each AI system
- how human oversight is achieved
- which external interfaces or providers affect the AIMS boundary

---

## 3. How to Use the New Templates

### 3.1 AIMS Scope Statement

Instantiate the [AIMS scope statement template](../templates/_TEMPLATE-aims-scope.md) into a governed document such as:

- `docs/compliance/aims-scope.md`
- `docs/compliance/iso-42001/aims-scope.md`

That document should answer:

- What parts of the organization are governed by the AIMS?
- Which AI-enabled services, agent types, workflows, and decision processes are in scope?
- Which locations, environments, and third-party providers are inside or outside the boundary?
- Which exclusions exist, and why are they legitimate?

### 3.2 AI System Inventory

Instantiate the [AI system inventory template](../templates/_TEMPLATE-ai-system-inventory.md) into a governed document such as:

- `docs/compliance/ai-system-inventory.md`
- `docs/compliance/iso-42001/ai-system-inventory.md`

The inventory should list every AI system in scope and capture, at minimum:

- system identity
- intended use
- business and technical owners
- AI risk tier
- autonomy level
- model/provider/version
- data categories
- human oversight mode
- key monitoring metrics
- related governance artifacts

The inventory should be referenced by the scope statement, and the scope statement should be referenced by the inventory.

---

## 4. Mapping Framework Artifacts to the AIMS Boundary

The new templates should not be filled from scratch. The framework already contains many of the inputs.

| AIMS Element | Framework Artifact | Path | How It Supports the AIMS |
|--------------|--------------------|------|--------------------------|
| Organizational context | Company strategy and identity | [`COMPANY.md`](../../../COMPANY.md), [`CONFIG.yaml`](../../../CONFIG.yaml) | Defines mission, operating context, and organizational structure |
| Organizational roles | Layer model and approval model | [`org/README.md`](../../../org/README.md), [`CODEOWNERS`](../../../CODEOWNERS) | Identifies who governs, executes, and reviews AI systems |
| AI governance rules | AI Governance Policy | [`org/4-quality/policies/ai-governance.md`](../../../org/4-quality/policies/ai-governance.md) | Provides the 4-tier AI risk classification and model governance requirements |
| AI risk register context | Risk Management Policy | [`org/4-quality/policies/risk-management.md`](../../../org/4-quality/policies/risk-management.md) | Supplies risk taxonomy, scoring, and treatment expectations |
| AI system candidates | Agent Type Registry | [`org/agents/`](../../../org/agents/) | Lists agent types, capabilities, and model governance sections |
| External AI dependencies | Vendor Risk Management Policy + Integration Registry | [`org/4-quality/policies/vendor-risk-management.md`](../../../org/4-quality/policies/vendor-risk-management.md), [`org/integrations/`](../../../org/integrations/) | Identifies AI providers, fourth parties, and interface boundaries |
| Monitoring evidence | Observability Policy + OTel contract | [`org/4-quality/policies/observability.md`](../../../org/4-quality/policies/observability.md), [`docs/otel-contract.md`](../../otel-contract.md) | Defines what AI behavior must be observable once in scope |
| Data governance | Data Classification and Privacy policies | [`org/4-quality/policies/data-classification.md`](../../../org/4-quality/policies/data-classification.md), [`org/4-quality/policies/privacy.md`](../../../org/4-quality/policies/privacy.md) | Defines data categories and privacy obligations for listed AI systems |

---

## 5. Scoping Guidance for Agentic Enterprises

AI system scope can be unintuitive in a multi-agent environment. Use the following decisions consistently.

### 5.1 What Usually Belongs In Scope

- agent types that use LLMs or ML models
- customer-facing AI features
- internal AI systems that materially influence business decisions
- AI-assisted workflows that process personal, confidential, or restricted data
- supporting model providers, orchestration logic, prompt management, and monitoring functions where they are necessary for the AI system to operate safely

### 5.2 What May Be Out of Scope

- non-AI infrastructure that does not materially influence AI behavior
- static documentation systems with no AI capability
- sandbox experiments that are isolated from production and do not affect customers or business decisions

If an excluded component can change AI behavior, supply AI outputs, or compromise AI governance outcomes, it is usually safer to keep it in scope.

### 5.3 Scope Boundary Questions to Answer Explicitly

- Does this system generate, rank, classify, summarize, or recommend using an AI model?
- Could its output materially affect customers, employees, finances, safety, or compliance?
- Does it depend on third-party AI models or AI-enabled SaaS?
- Does it process sensitive data or feed downstream decisions?
- Does human oversight exist, and where does it occur?

If the answer to one or more is yes, the system probably belongs in the inventory and should be evaluated for inclusion in the AIMS scope.

---

## 6. Aligning the Inventory with AI Risk Classification

The AI system inventory should use the same risk tiers defined in [ai-governance.md](../../../org/4-quality/policies/ai-governance.md):

| Tier | Meaning | Inventory Expectation |
|------|---------|-----------------------|
| **0** | Prohibited | Should not appear as an active in-scope deployed system; if discovered, escalate immediately |
| **1** | High-Risk | Requires full governance references: model card, fairness evidence, DPIA or equivalent, human oversight |
| **2** | Limited-Risk | Requires transparency, output labeling where applicable, and documented review controls |
| **3** | Minimal-Risk | Requires standard governance, model governance, and observability |

The inventory is not just a list of models. It is the authoritative roll-up of AI systems as governed business systems.

That means one row should represent a coherent AI system or AI-enabled workflow, not every individual prompt or every ephemeral experiment.

---

## 7. Verification Checklist

### AIMS Scope Statement

- [ ] Internal and external issues are documented for the AI context
- [ ] Interested parties with AI-related requirements are identified
- [ ] Organizational units and AI-enabled functions in scope are listed
- [ ] Exclusions are documented with justification
- [ ] External AI providers and interfaces are explicitly named
- [ ] The scope statement references the AI system inventory

### AI System Inventory

- [ ] Every in-scope AI system has a unique identifier and owner
- [ ] Every in-scope AI system has a risk tier
- [ ] Model/provider/version or equivalent AI dependency is documented
- [ ] Data categories and human oversight mode are documented
- [ ] Related governance artifacts are linked for higher-risk systems
- [ ] Inventory review cadence is defined and followed

### Cross-Consistency

- [ ] Systems listed as in scope appear in the inventory
- [ ] Systems excluded from scope are not silently present in the inventory as active in-scope systems
- [ ] Inventory risk tiers align with the AI Governance Policy
- [ ] External providers in the inventory align with the Integration Registry and Vendor Risk Management records

---

## References

- [ISO 42001 Compliance Reference](../iso-42001.md)
- [AIMS Scope Statement Template](../templates/_TEMPLATE-aims-scope.md)
- [AI System Inventory Template](../templates/_TEMPLATE-ai-system-inventory.md)
- [AI Governance Policy](../../../org/4-quality/policies/ai-governance.md)
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
- [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md)
- [Observability Policy](../../../org/4-quality/policies/observability.md)
