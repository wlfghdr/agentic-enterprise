# Division: Legal & Compliance

> **Owner:** <!-- Division lead name -->
> **Type:** Corporate Function
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns legal advisory, contract management, regulatory compliance, intellectual property protection, and privacy law. This division ensures the company operates within legal boundaries, manages legal risk proactively, and maintains the contractual and regulatory foundation the business requires.

## Scope

### In Scope
- Contract drafting, review, redlining, and lifecycle management (vendor, customer, partner, employment)
- Regulatory compliance research and advisory (GDPR, CCPA, SOC 2, industry-specific)
- Intellectual property management: patents, trademarks, copyrights, trade secrets
- Privacy law compliance and data processing agreements (DPAs)
- Employment law advisory (not day-to-day HR operations)
- Litigation support and legal risk management
- Terms of service and privacy policy drafting and maintenance
- Legal review of marketing claims and product feature representations
- Corporate governance documentation
- Export control and sanctions compliance

### Out of Scope
- Day-to-day HR operations (→ People)
- Financial reporting and tax filings (→ Finance & Procurement)
- Security policy enforcement (→ Quality & Security Engineering)
- Procurement decisions and purchase orders (→ Finance & Procurement)

## Key Responsibilities

1. **Contract Management** — Draft, review, and track contracts through signature; maintain executed contract repository; alert on renewal and expiry dates
2. **Regulatory Advisory** — Monitor regulatory landscape; advise on compliance obligations; produce compliance guidance documents for execution divisions
3. **Privacy Compliance** — Maintain records of processing activities; review data handling practices; draft and maintain DPAs; advise on user consent mechanisms
4. **IP Protection** — Identify and file IP protections; advise on freedom-to-operate; review content for third-party IP risk
5. **Legal Risk Monitoring** — Track legal signals across the business; surface legal risk to Steering Layer before it becomes litigation
6. **Policy & Terms Maintenance** — Keep Terms of Service, Privacy Policy, and acceptable-use policies current and compliant with applicable law

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | All Divisions | Contract requests, compliance questions, IP review requests via signals |
| Receives from | People | Employment contract needs, HR compliance questions |
| Receives from | Finance & Procurement | Vendor contract review requests |
| Receives from | Quality & Security Engineering | Regulatory requirements for security policies |
| Delivers to | Quality Layer | Legal compliance evaluations (privacy, regulatory) |
| Delivers to | Steering Layer | Legal risk assessments, regulatory change signals |
| Delivers to | All Divisions | Compliance guidance, contract templates, legal advisory |
| Collaborates with | Finance & Procurement | Joint vendor negotiation; contract-to-purchase alignment |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always (legal documents contain confidential business information)
- `policies/content.md` — For all public-facing legal documents (ToS, Privacy Policy)
- `policies/customer.md` — For all customer-facing legal representations and commitments

## Human Checkpoints

These decisions require human division lead (or above) involvement:

- Any contract above the defined financial threshold — human legal lead mandatory
- New regulatory compliance determinations — require human legal lead review
- IP filing decisions — require human legal lead and executive approval
- Litigation decisions (pursue, settle, defend) — Steering executive required
- Privacy policy changes affecting user rights — human legal lead + Steering
- Export control classifications — human legal lead mandatory

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Legal outputs are advisory only — no agent may represent that a contract is final or binding without human legal lead sign-off
3. All contract drafts must clearly be marked "DRAFT — Pending Legal Review" until approved
4. Privacy-sensitive data in legal documents must be handled per `policies/security.md`
5. When in doubt about legal interpretation, escalate — legal errors compound quickly
6. Maintain version history on all contract drafts; never overwrite a prior version

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Contract repository | <!-- secure repo URL --> | Executed contracts with metadata |
| Contract templates | <!-- repo URL --> | Approved contract templates by type |
| Compliance matrix | <!-- repo URL --> | Regulatory requirements by jurisdiction/framework |
| IP registry | <!-- repo URL --> | Patent, trademark, and IP asset register |
