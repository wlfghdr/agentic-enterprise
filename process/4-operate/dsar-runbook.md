# DSAR Runbook

> **Applies to:** Data subject rights requests involving personal data processed by the organization
> **Owner:** Privacy lead / support operations
> **Triggered by:** Access, rectification, erasure, portability, restriction, objection, or related privacy requests
> **Source policy:** [`../../org/4-quality/policies/privacy.md`](../../org/4-quality/policies/privacy.md)
> **Version:** 1.0 | **Last updated:** 2026-03-13

---

## Purpose

Provide a repeatable operating procedure for handling privacy requests without relying on ad hoc judgment.

## Request Types Covered

- Access
- Rectification
- Erasure
- Restriction
- Objection
- Portability
- Consent withdrawal / preference correction

## Instance-Specific Inputs To Configure

Before using this runbook, each deployment must define:

- DSAR intake channels (email, portal, support queue)
- Identity-verification method
- Systems of record to search
- Standard response templates and approvers
- Jurisdiction-specific deadlines and escalation contacts

## Operating Procedure

### 1. Intake and Classification

- Log the request with timestamp, requester identity, jurisdiction if known, and request type
- Confirm whether the request is from the data subject, an authorized agent, or an internal proxy
- Determine whether the organization is controller, processor, or both for the requested data
- If acting only as processor, route per the customer contract/DPA and notify the controller contact without undue delay

### 2. Identity Verification

- Verify identity proportionately to the request sensitivity
- Do not request more personal data than necessary to verify the requester
- If identity cannot be verified, pause fulfillment and document what is missing

### 3. Scope the Search

- Identify systems likely to contain the subject's data: app database, CRM, support tooling, analytics, logs, backups, and third-party processors as applicable
- Capture search owners for each system
- Define exclusions or legal exceptions up front and have them reviewed where required

### 4. Fulfill the Request

#### Access / Portability
- Collect relevant records in a structured, intelligible form
- Exclude data that would unlawfully disclose another person's data or protected security material
- Record the export package checksum or inventory for auditability

#### Rectification
- Correct inaccurate data at the source of truth
- Propagate the correction to downstream systems where required
- Record which systems were updated and when

#### Erasure / Restriction / Objection
- Determine whether legal, contractual, security, or audit-retention exceptions apply
- If deletion is approved, execute deletion or suppression across systems in scope
- Record any deferred deletion path (for example: backup expiry window)

### 5. Response and Closure

- Provide the response within the applicable legal deadline
- Include outcome, scope fulfilled, any exceptions applied, and follow-up path
- Close the request only after fulfillment evidence is attached

## Evidence Required

- Intake timestamp
- Identity-verification outcome
- Systems searched and search owners
- Decision and legal/privacy reviewer if applicable
- Fulfillment timestamp
- Exceptions or partial denial rationale
- Customer/controller notification if processor-led

## Observability Hooks

A mature deployment should emit events for:
- `privacy.dsar.received`
- `privacy.dsar.identity_verified`
- `privacy.dsar.search_completed`
- `privacy.dsar.fulfilled`
- `privacy.dsar.closed`
- `privacy.dsar.overdue`

## Escalate Immediately If

- The request involves high-risk data or a vulnerable individual
- Identity is disputed
- The request spans multiple jurisdictions with conflicting rules
- The request intersects an active incident, litigation hold, fraud investigation, or security event
- The organization is unsure whether it is controller or processor for the data in question

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial DSAR operating runbook |
