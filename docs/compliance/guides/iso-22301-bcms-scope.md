<!-- placeholder-ok -->
# ISO 22301 — BCMS Scope Statement

> **Implements:** Formal BCMS scope statement (clause 4.3)
> **Standard:** ISO 22301:2019 — Business Continuity Management Systems
> **Severity:** High — required for certification
> **Related issue:** [#138](https://github.com/wlfghdr/agentic-enterprise/issues/138)
> **Related compliance doc:** [ISO 22301 Compliance Reference](../iso-22301.md)

---

## 1. Purpose

ISO 22301 clause 4.3 requires organizations to define the scope of the BCMS — identifying which products, services, activities, and locations are covered, including any exclusions and their justification. The scope must consider internal and external issues (clause 4.1) and the requirements of interested parties (clause 4.2).

The Agentic Enterprise framework provides the structural foundation for a BCMS — the 5-layer organizational model, 4-loop process lifecycle, availability policy with RTO/RPO tiers, and incident response procedures. This guide implements the formal BCMS scope statement that defines the boundaries of the business continuity management system — the governed artifact establishing which processes, services, and organizational units fall within the BCMS boundary, a mandatory prerequisite for ISO 22301 certification.

This guide provides the requirements, a scope statement template tailored to the agentic enterprise context, and a mapping of existing framework artifacts to BCMS elements.

---

## 2. BCMS Scope Requirements (Clause 4.3)

The BCMS scope statement must address all of the following elements per ISO 22301:

| Requirement | Clause Reference | Description |
|-------------|-----------------|-------------|
| Internal and external issues | 4.1 | Issues relevant to the organization's purpose that affect the BCMS — regulatory environment, market conditions, technology dependencies, organizational structure |
| Interested party requirements | 4.2 | Needs and expectations of parties with a stake in business continuity — customers, regulators, employees, suppliers, shareholders |
| Products and services in scope | 4.3 a) | Which products, services, and service types are covered by the BCMS |
| Activities in scope | 4.3 a) | Which organizational activities support the in-scope products and services |
| Locations in scope | 4.3 a) | Physical and logical locations where in-scope activities are performed |
| Exclusions and justification | 4.3 note | Any elements deliberately excluded from the BCMS scope with rationale for exclusion |
| Dependencies | 4.3, 8.2 | Internal and external dependencies that could affect in-scope products and services |
| Risk appetite for disruption | 4.1, 6.1 | Organizational tolerance for disruption to in-scope activities |

---

## 3. BCMS Scope Statement Template

The following template should be instantiated as a governed artifact (e.g., `docs/compliance/bcms-scope.md` or within a dedicated BCMS documentation area). It is subject to PR review and CODEOWNERS approval.

```markdown
# BCMS Scope Statement

> **Version:** {{VERSION}}
> **Last updated:** {{YYYY-MM-DD}}
> **Approved by:** {{APPROVER_NAME_AND_ROLE}}
> **Review frequency:** Annual (minimum) or upon significant organizational change

## 1. Organization Context (Clause 4.1)

### Internal Issues
- Organizational structure: {{DESCRIBE — e.g., "5-layer agentic operating model
  with N divisions"}}
- Technology landscape: {{DESCRIBE — e.g., "Cloud-native SaaS platform hosted
  on {{PROVIDER}}, multi-agent system with autonomous and human-supervised
  operations"}}
- Operational model: {{DESCRIBE — e.g., "4-loop process lifecycle (Discover,
  Build, Ship, Operate) with GitOps governance"}}
- Key constraints: {{LIST — e.g., "Single cloud provider dependency, agent
  availability requirements, data residency obligations"}}

### External Issues
- Regulatory environment: {{LIST — e.g., "EU AI Act, GDPR, SOC 2, ISO 27001"}}
- Market conditions: {{DESCRIBE}}
- Technology dependencies: {{LIST — e.g., "LLM API providers, cloud
  infrastructure, MCP server ecosystem"}}
- Threat landscape: {{DESCRIBE — e.g., "Cyber threats, supply chain disruption,
  AI model provider outages"}}

## 2. Interested Parties (Clause 4.2)

| Interested Party | BC Requirements | Communication Needs |
|-----------------|-----------------|---------------------|
| Customers | {{e.g., "Service availability per SLA, data protection during disruptions"}} | {{e.g., "Status page updates, contractual notification within N hours"}} |
| Regulators | {{e.g., "Continued compliance during disruptions, incident reporting per regulatory timelines"}} | {{e.g., "Formal notification per regulatory requirements"}} |
| Employees / agents | {{e.g., "Clear roles and procedures during disruptions, safe working conditions"}} | {{e.g., "Internal communication channels, agent instruction updates"}} |
| Suppliers / vendors | {{e.g., "Coordinated response to shared disruptions, SLA enforcement"}} | {{e.g., "Vendor communication per contracts"}} |
| Shareholders / investors | {{e.g., "Financial impact minimization, transparent risk communication"}} | {{e.g., "Board-level reporting"}} |

## 3. Scope Definition

### 3a. Products and Services In Scope

| Product / Service | Availability Tier | Criticality | Justification |
|------------------|-------------------|-------------|---------------|
| {{PRODUCT_1}} | {{Tier 1/2/3/4 per Availability Policy}} | {{Critical/High/Medium/Low}} | {{Why this is in BCMS scope}} |
| {{PRODUCT_2}} | {{Tier}} | {{Criticality}} | {{Justification}} |

### 3b. Activities In Scope

| Activity | Supporting Layer | Process Loop | Related Policy |
|----------|-----------------|-------------|----------------|
| {{e.g., "Customer-facing API operations"}} | Execution (Layer 3) | Operate (Loop 4) | Availability Policy |
| {{e.g., "Agent orchestration and fleet management"}} | Orchestration (Layer 2) | Build/Operate (Loop 2/4) | Availability Policy |
| {{e.g., "Data processing and storage"}} | Execution (Layer 3) | Operate (Loop 4) | Data Classification Policy |
| {{e.g., "Incident detection and response"}} | Quality (Layer 4) | Operate (Loop 4) | Incident Response Policy |
| {{e.g., "Governance and compliance operations"}} | Steering (Layer 0) | Discover/Operate (Loop 1/4) | All quality policies |

### 3c. Locations In Scope

| Location | Type | Activities Performed |
|----------|------|---------------------|
| {{e.g., "AWS eu-west-1"}} | Cloud region — primary | Production workloads, data storage |
| {{e.g., "AWS eu-central-1"}} | Cloud region — DR | Failover target, replicated data |
| {{e.g., "GitHub (SaaS)"}} | Code and governance platform | Source control, CI/CD, PR governance |
| {{e.g., "Corporate office, {{CITY}}"}} | Physical | Human oversight, management review |

### 3d. Exclusions

| Excluded Element | Justification |
|-----------------|---------------|
| {{e.g., "Development and staging environments"}} | {{e.g., "Non-production; disruption does not impact customers or revenue"}} |
| {{e.g., "Marketing website"}} | {{e.g., "Static content; no business continuity impact; separate hosting with independent recovery"}} |

## 4. Dependencies

| Dependency | Type | Impact if Unavailable | Mitigation |
|-----------|------|----------------------|------------|
| {{e.g., "LLM API provider"}} | External — critical | Agent operations degraded or halted | {{e.g., "Multi-provider strategy, graceful degradation"}} |
| {{e.g., "Cloud infrastructure provider"}} | External — critical | Full service outage | {{e.g., "Multi-region deployment, DR procedures"}} |
| {{e.g., "Git platform"}} | External — high | Governance and deployment halted | {{e.g., "Local repository copies, manual procedures"}} |
| {{e.g., "Observability platform"}} | External — medium | Reduced visibility, manual monitoring required | {{e.g., "Local logging fallback"}} |

## 5. Review and Approval

| Action | Responsible | Date |
|--------|------------|------|
| Drafted | {{AUTHOR}} | {{DATE}} |
| Reviewed | {{REVIEWER}} | {{DATE}} |
| Approved | {{APPROVER — must be top management per clause 5.1}} | {{DATE}} |
| Next review due | — | {{DATE + 1 year}} |
```

---

## 4. Mapping Framework Artifacts to BCMS Elements

Existing Agentic Enterprise framework artifacts that support the BCMS scope definition:

| BCMS Scope Element | Framework Artifact | Path | How It Supports Scoping |
|-------------------|-------------------|------|------------------------|
| Organization context | Company definition | [`COMPANY.md`](../../../COMPANY.md) | Vision, mission, strategic beliefs define what matters to the organization |
| Organization context | Configuration | [`CONFIG.yaml`](../../../CONFIG.yaml) | Organizational identity, integrations, and deployment context |
| Interested parties | Stakeholder references | [`CODEOWNERS`](../../../CODEOWNERS), `CONFIG.yaml` | Identifies responsible parties and approval authorities |
| Products and services | Availability tiers | [`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md) | Tier 1–4 classification maps directly to BCMS criticality levels |
| Activities | Process lifecycle | [`process/`](../../../process/) | 4-loop model (Discover, Build, Ship, Operate) identifies all organizational activities |
| Activities | Layer model | [`org/README.md`](../../../org/README.md) | 5-layer model identifies which organizational functions support which activities |
| Dependencies | Integration registry | [`org/integrations/`](../../../org/integrations/) | External tool dependencies are registered and governed |
| Dependencies | Vendor risk management | [`org/4-quality/policies/vendor-risk-management.md`](../../../org/4-quality/policies/vendor-risk-management.md) | Vendor tiers and exit planning identify critical supply chain dependencies |
| Risk context | Risk management | [`org/4-quality/policies/risk-management.md`](../../../org/4-quality/policies/risk-management.md) | Risk register and KRI monitoring inform disruption risk appetite |
| Recovery targets | Availability policy | [`org/4-quality/policies/availability.md`](../../../org/4-quality/policies/availability.md) | RTO/RPO per availability tier define recovery ambitions for scoped services |
| Incident handling | Incident response | [`org/4-quality/policies/incident-response.md`](../../../org/4-quality/policies/incident-response.md) | SEV1–4 classification and escalation paths inform response scope |

---

## 5. Verification Checklist

### Scope Statement Content
- [ ] Internal and external issues documented (clause 4.1)
- [ ] Interested parties and their BC requirements identified (clause 4.2)
- [ ] All in-scope products and services listed with availability tier assignments
- [ ] All in-scope activities listed and mapped to organizational layers and process loops
- [ ] All in-scope locations (physical and logical) identified
- [ ] Exclusions documented with justification for each exclusion
- [ ] Internal and external dependencies identified with impact assessment

### Alignment with Framework Artifacts
- [ ] Availability tier assignments in scope statement match the Availability Policy
- [ ] Dependencies in scope statement match the Integration Registry and Vendor Risk Management Policy
- [ ] Risk context references the Risk Management Policy risk register
- [ ] Process activities map correctly to the 4-loop process model

### Governance
- [ ] Scope statement is version-controlled in the repository
- [ ] Scope statement has been reviewed and approved by top management (clause 5.1)
- [ ] Scope statement is referenced from the BCMS policy (clause 5.2)
- [ ] Review frequency is defined (at least annual)
- [ ] Change triggers are defined — scope must be reviewed when products, services, locations, or dependencies change materially
- [ ] Scope statement is accessible to all interested parties who need it

### Integration with Other BCMS Artifacts
- [ ] Business Impact Analysis (clause 8.2) covers all activities listed in scope
- [ ] BC plans (clause 8.4) exist for all critical activities within scope
- [ ] Exercise programme (clause 8.5) tests plans for in-scope activities
- [ ] Internal audit programme (clause 9.2) covers the full BCMS scope
