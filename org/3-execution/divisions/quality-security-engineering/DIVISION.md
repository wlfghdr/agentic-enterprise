# Division: Quality & Security Engineering

> **Owner:** <!-- Division lead name -->
> **Type:** Operations
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns security testing, privacy assessments, compliance evidence, vulnerability management, supply chain security, and quality engineering. This division provides the security and quality assurance capabilities that protect the enterprise.

## Scope

### In Scope
- SAST/DAST scanning and dependency vulnerability management
- Privacy impact assessments (GDPR/CCPA)
- Vulnerability triage, tracking, and prioritization
- Compliance evidence automation (SOC2, ISO 27001, FedRAMP)
- Software supply chain security and SBOM management
- Security incident resolution and patch coordination
- Attack detection, path analysis, and threat intelligence
- DevSecOps pipeline integration (SARIF reports, security gates)

### Out of Scope
- Infrastructure provisioning and operations (→ Infrastructure Operations)
- CI/CD pipeline management (→ Engineering Foundation)
- Quality policy authoring and evaluation (→ Quality Layer)

## Key Responsibilities

1. **Vulnerability Management** — Scan, triage, and resolve vulnerabilities with SLA compliance
2. **Privacy & Compliance** — Automate privacy assessments and compliance evidence collection
3. **Supply Chain Security** — Maintain SBOMs and audit third-party dependencies
4. **Threat Detection** — Detect attacks, map attack paths, and correlate security intelligence
5. **DevSecOps Integration** — Embed security findings into CI/CD pipelines as automated gates
6. **Security Incident Resolution** — Coordinate end-to-end patch generation and verification

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Engineering Foundation, Infrastructure Operations | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/security.md` — For all security-related work

## Human Checkpoints

These decisions require human division lead involvement:

- Architecture-changing proposals
- New external integrations
- Customer-impacting schema changes
- Work that crosses division boundaries

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Check the Software Catalog for existing services before creating new ones
3. Follow established code patterns in this division's codebase
4. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
5. Register new components via `org/3-execution/divisions/_TEMPLATE/_TEMPLATE-component-onboarding.md`

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Source code | <!-- repo URL --> | Main repository |
| Documentation | <!-- doc URL --> | User-facing docs |
| API specs | <!-- API spec URL --> | OpenAPI specs |
