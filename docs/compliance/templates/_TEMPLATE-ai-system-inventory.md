# AI System Inventory

> **Template version:** 1.0
> **Last updated:** 2026-03-15
> **Standard:** ISO/IEC 42001:2023 — Clause 4 foundation
> **Purpose:** Maintain the authoritative inventory of AI systems in scope for the Artificial Intelligence Management System (AIMS)

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | AIMS-AI-INV-001 |
| Version | {{VERSION}} |
| Owner | {{AIMS_OWNER}} |
| Approved by | {{APPROVER}} |
| Effective date | {{EFFECTIVE_DATE}} |
| Review cycle | Quarterly (minimum) and upon material AI system change |
| Related | [AIMS Scope Statement](_TEMPLATE-aims-scope.md) |

## How to Use This Template

1. Create one row per coherent AI system or AI-enabled workflow in scope.
2. Use the AI risk tiers from `org/4-quality/policies/ai-governance.md`.
3. Keep ownership, provider, model, and governance references current.
4. Do not omit internal AI systems just because they are not customer-facing if they materially influence decisions or process sensitive data.

## Inventory

| System ID | AI System Name | Intended Use | Business Owner | Technical Owner | Risk Tier | Autonomy Tier | Lifecycle Stage | Model / Provider / Version | Data Categories | Human Oversight | Key Monitoring Metrics | External Dependencies | Related Governance Artifacts | In Scope |
|-----------|----------------|--------------|----------------|-----------------|-----------|---------------|-----------------|----------------------------|----------------|-----------------|------------------------|----------------------|-----------------------------|----------|
| {{AI_SYS_001}} | {{SYSTEM_NAME}} | {{INTENDED_USE}} | {{BUSINESS_OWNER}} | {{TECHNICAL_OWNER}} | {{0 / 1 / 2 / 3}} | {{1 / 2 / 3 / 4}} | {{DESIGN / PILOT / PRODUCTION / RETIRED}} | {{MODEL_PROVIDER_VERSION}} | {{DATA_CATEGORIES}} | {{OVERSIGHT_MODE}} | {{METRICS}} | {{DEPENDENCIES}} | {{MODEL_CARD / DPIA / RISK_REGISTER / VENDOR_ASSESSMENT}} | Yes |
| {{AI_SYS_002}} | {{SYSTEM_NAME}} | {{INTENDED_USE}} | {{BUSINESS_OWNER}} | {{TECHNICAL_OWNER}} | {{0 / 1 / 2 / 3}} | {{1 / 2 / 3 / 4}} | {{STAGE}} | {{MODEL_PROVIDER_VERSION}} | {{DATA_CATEGORIES}} | {{OVERSIGHT_MODE}} | {{METRICS}} | {{DEPENDENCIES}} | {{ARTIFACTS}} | Yes / No |

## Inventory Summary

| Dimension | Count | Notes |
|-----------|------:|-------|
| Total AI systems listed | {{N}} | |
| In-scope AI systems | {{N}} | |
| Tier 1 — High-Risk | {{N}} | |
| Tier 2 — Limited-Risk | {{N}} | |
| Tier 3 — Minimal-Risk | {{N}} | |
| External AI providers used | {{N}} | |

## Change Triggers

Update this inventory when any of the following occur:

- a new AI system or AI-enabled workflow is introduced
- an existing system changes model, provider, intended use, or autonomy level
- data categories processed by the system change
- the system's risk tier changes
- a material incident or audit finding changes the governance posture of the system

## Review Checklist

- [ ] Every in-scope AI system has a unique `System ID`
- [ ] Every in-scope AI system has named business and technical owners
- [ ] Every in-scope AI system has a risk tier aligned to the AI Governance Policy
- [ ] Every higher-risk system links to its supporting governance artifacts
- [ ] External AI providers listed here are also covered in vendor assessment records
- [ ] Systems marked `No` under `In Scope` are intentionally excluded and documented in the AIMS scope statement

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial AI system inventory |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-15 | Initial AI system inventory template with risk tier, ownership, provider, and governance linkage fields |
