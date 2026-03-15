# SOC 2 — CPA Audit Engagement Guide

> **Implements:** Independent CPA audit engagement and management assertion preparation
> **Standard:** SOC 2 Type II — engagement requirement
> **Severity:** High — a licensed external CPA firm is still required for report issuance
> **Related issue:** [#125](https://github.com/wlfghdr/agentic-enterprise/issues/125)
> **Related compliance doc:** [SOC 2 Compliance Reference](../soc2.md)
> **Companion resources:** [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md), [SOC 2 Formal Control Testing Documentation](soc2-control-testing.md), and the [SOC 2 Management Assertion Letter Template](../templates/_TEMPLATE-soc2-management-assertion-letter.md)

---

## 1. Purpose

The Agentic Enterprise framework helps adopters prepare for SOC 2 by providing:

- control design mappings in [soc2.md](../soc2.md)
- runtime evidence guidance in [soc2-operating-effectiveness.md](soc2-operating-effectiveness.md)
- formal control testing guidance in [soc2-control-testing.md](soc2-control-testing.md)

This guide provides the final preparation layer between "we have evidence" and "we are ready to engage a licensed CPA firm." It covers:

1. how to select and engage the audit firm
2. how to prepare management's assertion package
3. how to coordinate auditor access without breaking least-privilege or audit-trail controls
4. how to stage the engagement timeline 3 to 6 months before fieldwork

This guide does **not** replace the external audit itself.

---

## 2. What Should Exist Before Formal Engagement

Before the organization signs an audit engagement letter, it should already be able to show the following:

| Readiness Item | Why It Matters | Framework Starting Point |
|----------------|----------------|--------------------------|
| Defined SOC 2 scope and in-scope Trust Service Criteria | The CPA firm must know what system and which criteria are being examined | [SOC 2 Compliance Reference](../soc2.md) |
| Operating-effectiveness evidence pipeline | Fieldwork depends on real evidence for the observation period | [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md) |
| Control testing matrix and sample result records | Auditors expect a documented testing programme before heavy sampling begins | [SOC 2 Formal Control Testing Documentation](soc2-control-testing.md) |
| Draft system description | The report needs a management-owned description of the system boundary and control environment | Deployment-specific artifact built from the framework mappings |
| Vendor and subservice inventory | The auditor needs to understand carve-outs, inherited controls, and third-party dependencies | [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md) |
| Named executive sponsor and audit coordinator | The engagement stalls quickly without clear ownership for requests and sign-off | Adopter-defined local ownership |

If several of these are missing, start with a readiness assessment rather than formal fieldwork.

---

## 3. CPA Firm Selection and Engagement Workflow

Treat auditor selection as a governed vendor decision, not a last-minute procurement step.

| Phase | Goal | Practical Output |
|-------|------|------------------|
| Internal scope alignment | Confirm report type, in-scope criteria, observation period, and known open areas | Internal readiness memo or checklist |
| CPA firm shortlist | Identify firms with SaaS, cloud, and AI-governance familiarity | Shortlist with evaluation notes |
| Capability and independence review | Confirm the firm can perform the engagement and is independent | Selection record and conflict check |
| Readiness assessment or scoping call | Validate whether the organization is truly fieldwork-ready | Findings list, expected PBC list, timeline assumptions |
| Engagement letter negotiation | Lock scope, period, deliverables, timeline, and responsibilities | Signed engagement letter |
| Kickoff and request intake setup | Establish the request process before fieldwork begins | Audit tracker, owners, evidence-room structure |

### 3.1 Questions to Ask Prospective CPA Firms

- Have you performed SOC 2 examinations for SaaS or AI-heavy environments?
- How do you approach automated control environments with Git-based approvals and CI/CD evidence?
- Do you recommend a readiness assessment before fieldwork for this maturity level?
- What evidence format do you prefer for telemetry, Git history, and control testing results?
- How do you want subservice organizations, hosted dependencies, and inherited cloud controls presented?
- What is your expected timeline from kickoff to draft report for a Type II engagement?

### 3.2 Engagement Outputs to Lock Early

Before fieldwork starts, confirm:

- report type and audit period
- in-scope Trust Service Criteria categories
- system boundary and subservice organization treatment
- request list format and response cadence
- management assertion timing and signatories
- rules for auditor access, evidence handling, and confidentiality

---

## 4. Internal Ownership Model

The framework can organize evidence, but the adopter still needs named humans for the engagement.

| Role | Typical Owner | Responsibility |
|------|---------------|----------------|
| Executive sponsor | CEO, COO, CFO, or equivalent | Owns overall readiness, approves scope, signs the management assertion |
| Audit coordinator | Compliance, GRC, or security lead | Owns the request tracker, evidence room, and weekly coordination with the CPA firm |
| Technical owner | Platform, engineering, or security lead | Explains system architecture, access controls, telemetry, and change management evidence |
| Legal or privacy reviewer | Internal counsel or outside counsel | Reviews assertion wording, customer commitments, and confidentiality handling |
| Control owners | Named owners from the control matrix | Provide explanations, evidence, and remediation status for sampled controls |

One named audit coordinator matters more than a large committee. Auditors prefer one accountable intake path.

---

## 5. Management Assertion Preparation

The management assertion is management's statement to the CPA firm. It is not a marketing artifact and it is not boilerplate to sign blindly.

Use the [SOC 2 management assertion letter template](../templates/_TEMPLATE-soc2-management-assertion-letter.md) as the starting point, then finalize the wording with:

- the engaged CPA firm
- legal counsel
- the executive who will sign the document

### 5.1 Inputs Needed Before Drafting

| Input | Why It Is Needed |
|-------|------------------|
| Final audit period | The assertion must match the actual examination window |
| Final system description title and scope | The assertion refers to the exact description under examination |
| In-scope TSC categories | Security is mandatory; other categories must match the engagement letter |
| Control testing summary | Management needs a factual basis for its assertion |
| Exception list and remediation status | Known exceptions must be understood before sign-off |
| Subservice organization treatment | Carve-out versus inclusive treatment affects the wording and description |
| Signatory authority | The signer must have appropriate management authority |

### 5.2 Practical Drafting Rules

- Do not finalize the letter before the system description and scope are stable.
- Do not claim operating effectiveness unless management has actually reviewed evidence supporting that claim.
- Keep the audit period, system name, and TSC scope identical across the engagement letter, assertion, and system description.
- Record who reviewed the draft and when.
- Treat last-minute scope changes as a reason to refresh the assertion draft, not as a cosmetic edit.

### 5.3 Important Limitation

The template in this repository is a reusable starting point. CPA firms often want small wording adjustments, and legal counsel may require jurisdiction-specific changes. That review is part of the normal process, not a sign that the template failed.

---

## 6. Auditor Access and Cooperation Model

The goal is to make evidence easy to review without weakening security controls.

### 6.1 Core Principles

- **Single intake path:** All auditor requests go through the audit coordinator or a tracked request register.
- **Read-only first:** Prefer exports, dashboards, screenshots, signed reports, and immutable logs before considering live system access.
- **Least privilege:** If live access is unavoidable, provide the minimum scope needed for the specific request.
- **Time-bounded access:** Access should expire automatically after the agreed review window.
- **Traceable fulfillment:** Every request should show who fulfilled it, when, and from which source artifact.

### 6.2 Preferred Fulfillment Model by Request Type

| Auditor Request | Preferred Response | Primary Owner |
|-----------------|-------------------|---------------|
| PR approval and change-management evidence | Export PR metadata, review history, and CI results | Audit coordinator + engineering |
| Runtime evidence and monitoring proof | Provide dashboard snapshots, retained reports, or targeted exports from the observability platform | Technical owner |
| Access-control evidence | Provide access roster, branch protection exports, KMS or IAM evidence, and reviewer assignment history | Security or platform owner |
| Incident or alerting evidence | Provide redacted incident timelines, alert history, and follow-up records | Security or operations owner |
| Vendor oversight evidence | Provide current assessments, attestations, and review dates | Vendor-risk owner |

### 6.3 If Live Access Is Unavoidable

Require all of the following:

- named auditor account or supervised session
- MFA and time-bound access window
- read-only permissions unless a stronger justification is approved
- session logging or equivalent access record
- explicit revocation after the review window closes

Direct production mutation rights for an auditor are almost never appropriate.

---

## 7. Evidence Room and Request Tracker Structure

Keep the evidence room simple and predictable. A practical structure is:

```text
01-engagement-admin/
02-management-assertion/
03-system-description/
04-control-matrix-and-test-results/
05-evidence-by-tsc/
06-exceptions-and-remediation/
07-pbc-request-tracker/
```

Recommended rules:

- number folders so both the internal team and the auditor see a stable order
- keep one request tracker with request ID, owner, due date, status, and evidence link
- freeze delivered evidence versions instead of overwriting files in place
- store final exports and signed documents with clear dates in the filename or document control block

---

## 8. Practical Timeline

Start the engagement preparation **3 to 6 months before formal fieldwork**. A shorter window is possible, but it increases scramble risk.

| Timing | Activity | Target Outcome |
|--------|----------|----------------|
| T-24 to T-20 weeks | Internal readiness review, scope confirmation, evidence-gap check | Decision on whether to pursue readiness assessment or formal fieldwork |
| T-20 to T-16 weeks | CPA firm shortlist and evaluation | Preferred firm selected |
| T-16 to T-12 weeks | Scoping call or readiness assessment | Initial request list and engagement assumptions |
| T-12 to T-8 weeks | Engagement letter, system-description drafting, assertion-template preparation | Audit logistics locked |
| T-8 to T-4 weeks | Evidence-room setup, control-testing refresh, exception cleanup | Fieldwork-ready evidence package |
| T-4 to T-0 weeks | Finalize management assertion draft, confirm signatories, rehearse walkthroughs | Clean kickoff |
| T0 onward | Fieldwork, sample response, exception follow-up | Timely auditor response and report progression |

If the organization is still discovering major scope or control deficiencies at T-8 weeks, delay fieldwork rather than forcing a weak start.

---

## 9. Verification Checklist

Use this checklist before declaring the engagement ready.

- [ ] Executive sponsor and audit coordinator are named
- [ ] In-scope TSC categories and audit period are confirmed
- [ ] System description draft exists and matches the proposed audit scope
- [ ] Control testing matrix and sample results exist for in-scope controls
- [ ] CPA firm is selected and the engagement scope is documented
- [ ] Management assertion draft exists and has been reviewed by legal counsel
- [ ] Auditor request tracker exists with named owners and due dates
- [ ] Evidence room structure is defined and populated
- [ ] Auditor access model is documented and follows least privilege
- [ ] Known exceptions and remediation items are tracked before fieldwork
- [ ] Access granted for the engagement has an explicit revocation path

---

## References

- [SOC 2 Compliance Reference](../soc2.md)
- [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md)
- [SOC 2 Formal Control Testing Documentation](soc2-control-testing.md)
- [SOC 2 Management Assertion Letter Template](../templates/_TEMPLATE-soc2-management-assertion-letter.md)
- [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md)
- [Delivery Policy](../../../org/4-quality/policies/delivery.md)
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
