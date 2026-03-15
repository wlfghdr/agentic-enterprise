# SOC 2 Management Assertion Letter

> **Template version:** 1.0.1
> **Last updated:** 2026-03-15
> **Standard:** SOC 2 Type II — management assertion
> **Purpose:** Provide a reusable starting point for the management assertion letter included in a SOC 2 examination package
> **Important:** Final wording must be confirmed with the engaged CPA firm and legal counsel before signature

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | SOC2-ASSERT-001 |
| Version | {{VERSION}} |
| Organization | {{ORGANIZATION_NAME}} |
| Audit period | {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}} |
| Report type | SOC 2 Type II |
| In-scope TSC categories | {{TSC_SCOPE}} |
| Prepared by | {{PREPARER}} |
| Reviewed by | {{LEGAL_REVIEWER}} / {{AUDIT_COORDINATOR}} |
| Signatory | {{EXECUTIVE_SIGNATORY}} |
| Related | [SOC 2 CPA Audit Engagement Guide](../guides/soc2-cpa-engagement.md) |

## Preparation Checklist

- [ ] Audit period matches the engagement letter and system description
- [ ] System description title is final
- [ ] In-scope Trust Service Criteria categories are final
- [ ] Known exceptions and remediation status were reviewed by management
- [ ] Legal counsel reviewed the wording
- [ ] CPA firm confirmed any required wording adjustments
- [ ] Signatory authority is confirmed

## Template

{{ORGANIZATION_LETTERHEAD}}

{{DATE}}

{{CPA_FIRM_NAME}}
{{CPA_FIRM_CONTACT}}
{{CPA_FIRM_ADDRESS}}

**Subject:** Management Assertion Regarding the Description of {{SYSTEM_NAME}} for the Period {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}}

To {{CPA_FIRM_CONTACT_NAME_OR_TEAM}},

We are responsible for preparing the accompanying description of {{SYSTEM_NAME}} titled "{{SYSTEM_DESCRIPTION_TITLE}}" for the period {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}}. We are also responsible for designing, implementing, operating, monitoring, and maintaining effective controls within that system to provide reasonable assurance that {{ORGANIZATION_NAME}}'s service commitments and system requirements relevant to the applicable Trust Services Criteria were achieved.

We assert that:

1. the accompanying description fairly presents the boundaries of {{SYSTEM_NAME}}, the services provided, the relevant infrastructure, software, people, procedures, data, and the complementary subservice organization and complementary user entity control considerations applicable to the system during the period {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}};
2. the controls stated in the description were suitably designed throughout the period {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}} to provide reasonable assurance that {{SERVICE_COMMITMENTS_AND_SYSTEM_REQUIREMENTS}} were achieved based on the applicable Trust Services Criteria for {{TSC_SCOPE}}; and
3. the controls operated effectively throughout the period {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}} to provide reasonable assurance that {{SERVICE_COMMITMENTS_AND_SYSTEM_REQUIREMENTS}} were achieved based on the applicable Trust Services Criteria for {{TSC_SCOPE}}.

This assertion is based on the criteria established in the applicable AICPA Trust Services Criteria and on management's review of the system description, control testing results, operating-effectiveness evidence, and known exceptions documented during the examination period.

Because of inherent limitations in any system of internal control, errors or irregularities may occur and not be detected. In addition, projections of any evaluation of controls to future periods are subject to the risk that controls may become inadequate because of changes in conditions, or that the degree of compliance with policies or procedures may deteriorate.

{{OPTIONAL_EXCEPTION_OR_SCOPE_NOTE}}

Sincerely,

{{EXECUTIVE_SIGNATORY}}
{{EXECUTIVE_TITLE}}
{{ORGANIZATION_NAME}}

## Notes for Adaptation

- If the CPA firm wants specific wording for subservice organizations, CUECs, or service commitments, update the numbered assertions instead of appending conflicting language elsewhere.
- If the examination scope changes late, refresh the period, system description title, and TSC scope together.
- If you are pursuing a Type I report instead of Type II, replace the period-based design and operating-effectiveness language with the point-in-time wording required by the CPA firm.

## Supporting Inputs

| Input | Source / Reference |
|-------|--------------------|
| Audit period | {{ENGAGEMENT_LETTER_REF}} |
| System description title | {{SYSTEM_DESCRIPTION_REF}} |
| TSC scope | {{SCOPE_DECISION_REF}} |
| Control testing summary | {{CONTROL_TESTING_REF}} |
| Exception summary | {{EXCEPTION_TRACKER_REF}} |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial management assertion letter draft |

## Changelog

| Version | Date | Change |
|---------|------|--------|
| Template 1.0 | 2026-03-15 | Initial SOC 2 management assertion letter template for CPA-audit engagement packages |
