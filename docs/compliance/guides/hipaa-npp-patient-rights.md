<!-- placeholder-ok -->
# HIPAA — Notice of Privacy Practices and Patient Rights

> **Implements:** Notice of Privacy Practices (NPP) template and patient rights implementation
> **Regulation:** HIPAA (45 CFR §164.520, §164.524, §164.526, §164.528)
> **Severity:** High — NPP is mandatory for all Covered Entities; patient rights are enforceable by HHS OCR
> **Related issue:** [#146](https://github.com/wlfghdr/agentic-enterprise/issues/146)
> **Related compliance doc:** [HIPAA Compliance Reference](../hipaa.md)

---

## 1. Purpose

HIPAA requires every Covered Entity to provide individuals with a Notice of Privacy Practices (NPP) that describes how their PHI may be used and disclosed, their rights regarding their PHI, and the Covered Entity's legal duties. The Privacy Rule also establishes six individual rights that Covered Entities must implement and support.

The Agentic Enterprise framework provides a DSAR (Data Subject Access Request) runbook via the [Privacy Policy](../../../org/4-quality/policies/privacy.md) that covers the general pattern for access and correction requests. This guide extends that foundation with a HIPAA-specific NPP template, HIPAA-specific timelines (30 days for access, 60 days for amendment, 6-year accounting window), and guidance for how AI/agent systems should interact with patient data access requests.

This guide provides the complete NPP requirements, a content template, implementation guidance for all six patient rights, agent-specific considerations, and a verification checklist.

---

## 2. Notice of Privacy Practices Requirements

### 2a. NPP Content Requirements (§164.520(b))

The NPP must contain all of the following elements:

| Required Element | Description | CFR Reference |
|-----------------|-------------|---------------|
| **Header** | Statement that the notice describes how medical information may be used and disclosed and how the individual can access it; statement to review carefully | §164.520(b)(1)(i) |
| **Uses and disclosures** | Description of each purpose for which the CE is permitted or required to use or disclose PHI without individual authorization | §164.520(b)(1)(ii) |
| **Authorization-required uses** | Description of uses/disclosures requiring individual authorization (marketing, sale of PHI, psychotherapy notes) | §164.520(b)(1)(ii)(E) |
| **Individual rights** | Statement of each right and how to exercise it (access, amendment, accounting, restriction, confidential communications, complaint) | §164.520(b)(1)(iv) |
| **CE duties** | Statement that the CE is required by law to maintain privacy of PHI, provide the NPP, and abide by its terms | §164.520(b)(1)(v) |
| **Complaint process** | Description of how to file a complaint with the CE and with the HHS Secretary | §164.520(b)(1)(vi) |
| **Contact information** | Name and contact of the person or office to contact for further information | §164.520(b)(1)(vii) |
| **Effective date** | Date the NPP is effective | §164.520(b)(1)(viii) |
| **Right to change terms** | Statement that the CE reserves the right to change NPP terms and make the new provisions effective for all PHI maintained | §164.520(b)(1)(v)(C) |

### 2b. NPP Distribution Requirements (§164.520(c))

| Distribution Requirement | Detail | Applies To |
|-------------------------|--------|-----------|
| **Provide at first service delivery** | NPP must be provided no later than the date of first service delivery | Direct treatment providers |
| **Make available on request** | NPP must be available to any person who requests it | All Covered Entities |
| **Post prominently** | Post the NPP in a clear and prominent location at the service delivery site | Providers with physical locations |
| **Post on website** | If the CE maintains a website with information about its services, post the NPP prominently on the website | All CEs with websites |
| **Good faith acknowledgment** | Obtain written acknowledgment of receipt of the NPP from individuals; document good-faith efforts if acknowledgment cannot be obtained | Direct treatment providers |
| **Health plan enrollment** | Provide NPP at enrollment and within 60 days of material revision | Health plans |
| **Material revision notification** | Provide revised NPP (or information about material change and how to obtain the revised NPP) to individuals for whom the CE has contact information | All Covered Entities |

### 2c. NPP Content Template

The following template covers all required NPP elements. Customize the `{{PLACEHOLDER}}` fields for the specific Covered Entity.

```
NOTICE OF PRIVACY PRACTICES

Effective Date: {{EFFECTIVE_DATE}}

THIS NOTICE DESCRIBES HOW MEDICAL INFORMATION ABOUT YOU MAY BE USED AND
DISCLOSED AND HOW YOU CAN GET ACCESS TO THIS INFORMATION.
PLEASE REVIEW IT CAREFULLY.

1. OUR PLEDGE REGARDING YOUR MEDICAL INFORMATION

   {{CE_NAME}} ("we," "us," or "our") is required by law to maintain the
   privacy of your Protected Health Information (PHI), provide you with
   this Notice of our legal duties and privacy practices, and follow the
   terms of the Notice currently in effect.

2. HOW WE MAY USE AND DISCLOSE YOUR MEDICAL INFORMATION

   We may use and disclose your PHI without your authorization for the
   following purposes:

   a. TREATMENT — To provide, coordinate, or manage your health care.
      Example: {{TREATMENT_EXAMPLE}}

   b. PAYMENT — To obtain payment for health care services provided to
      you. Example: {{PAYMENT_EXAMPLE}}

   c. HEALTH CARE OPERATIONS — To support our business activities,
      including quality assessment, training, accreditation, and
      business planning. Example: {{OPERATIONS_EXAMPLE}}

   d. AS REQUIRED BY LAW — When federal, state, or local law requires
      disclosure.

   e. PUBLIC HEALTH ACTIVITIES — For public health purposes such as
      disease prevention, reporting adverse events, and tracking FDA-
      regulated products.

   f. HEALTH OVERSIGHT — To a health oversight agency for authorized
      activities such as audits, investigations, and inspections.

   g. JUDICIAL AND ADMINISTRATIVE PROCEEDINGS — In response to court
      orders or subpoenas.

   h. LAW ENFORCEMENT — For law enforcement purposes as permitted by law.

   i. DECEDENTS — To coroners, medical examiners, and funeral directors.

   j. ORGAN AND TISSUE DONATION — To organ procurement organizations.

   k. RESEARCH — For research purposes subject to an approved waiver
      of authorization.

   l. SERIOUS THREAT TO HEALTH OR SAFETY — To prevent or lessen a
      serious and imminent threat to health or safety.

   m. SPECIALIZED GOVERNMENT FUNCTIONS — For military, veterans, national
      security, and intelligence activities as required by law.

   n. WORKERS' COMPENSATION — As authorized by workers' compensation laws.

3. USES AND DISCLOSURES REQUIRING YOUR AUTHORIZATION

   We will obtain your written authorization before using or disclosing
   your PHI for:
   - Marketing purposes
   - Sale of your PHI
   - Most uses and disclosures of psychotherapy notes
   - Any purpose not described in this Notice

   You may revoke your authorization in writing at any time.

4. YOUR RIGHTS REGARDING YOUR MEDICAL INFORMATION

   a. RIGHT TO ACCESS — You have the right to inspect and obtain a copy
      of your PHI maintained in a Designated Record Set. We will respond
      within 30 days of your request (one 30-day extension permitted
      with written notice). Submit requests in writing to {{CONTACT}}.

   b. RIGHT TO AMEND — You have the right to request amendment of your
      PHI in a Designated Record Set. We will respond within 60 days.
      We may deny your request if the PHI was not created by us, is not
      part of a Designated Record Set, is not available for inspection,
      or is accurate and complete.

   c. RIGHT TO ACCOUNTING OF DISCLOSURES — You have the right to receive
      an accounting of certain disclosures of your PHI made in the six
      years prior to your request. This does not include disclosures
      for treatment, payment, or health care operations, disclosures
      you authorized, or certain other disclosures.

   d. RIGHT TO REQUEST RESTRICTIONS — You have the right to request that
      we restrict use or disclosure of your PHI for treatment, payment,
      or health care operations. We are not required to agree, except
      that we must agree to restrict disclosures to a health plan for
      payment or health care operations when you have paid for the
      service in full out of pocket.

   e. RIGHT TO CONFIDENTIAL COMMUNICATIONS — You have the right to
      request that we communicate with you about your health information
      by alternative means or at alternative locations.

   f. RIGHT TO A PAPER COPY — You have the right to obtain a paper copy
      of this Notice upon request.

   g. RIGHT TO BE NOTIFIED OF A BREACH — You have the right to be
      notified if a breach of your unsecured PHI occurs.

5. CHANGES TO THIS NOTICE

   We reserve the right to change this Notice and make the new provisions
   effective for all PHI we maintain. A revised Notice will be posted at
   {{POSTING_LOCATION}} and on our website at {{WEBSITE_URL}}.

6. COMPLAINTS

   If you believe your privacy rights have been violated, you may file a
   complaint with us or with the U.S. Department of Health and Human
   Services. You will not be penalized for filing a complaint.

   File with us:
      {{PRIVACY_OFFICER_NAME}}
      {{PRIVACY_OFFICER_CONTACT}}

   File with HHS:
      Office for Civil Rights
      U.S. Department of Health and Human Services
      200 Independence Avenue, S.W.
      Washington, D.C. 20201
      1-877-696-6775
      https://www.hhs.gov/hipaa/filing-a-complaint/

CONTACT INFORMATION

   For questions about this Notice or to exercise your rights:
      {{CONTACT_NAME}}
      {{CONTACT_TITLE}}
      {{CONTACT_ADDRESS}}
      {{CONTACT_PHONE}}
      {{CONTACT_EMAIL}}
```

---

## 3. Patient Rights Implementation

### 3a. Right to Access (§164.524)

| Requirement | Detail | Timeline |
|------------|--------|----------|
| **Scope** | PHI maintained in a Designated Record Set (medical records, billing records, enrollment records, and other records used to make decisions about individuals) | N/A |
| **Response time** | 30 calendar days from receipt of request; one 30-day extension with written notice | 30 + 30 days max |
| **Format** | In the form and format requested by the individual if readily producible (including electronic copy if ePHI is maintained electronically) | Per request |
| **Fees** | Reasonable, cost-based fee (labor for copying, supplies, postage); cannot charge for retrieval or maintaining systems | Cost-based only |
| **Denial** | May deny in limited circumstances (psychotherapy notes, compiled for legal proceedings, inmates, research with ongoing participation); some denials are reviewable | Written denial with reason |
| **Third-party direction** | Individual may direct CE to transmit a copy to a designated third party in writing | Signed, written direction |

**Implementation workflow:**

```
Request received → Identity verification → Locate PHI in Designated Record Set
→ Determine format (electronic/paper per request) → Review for denial grounds
→ Produce copy within 30 days → Calculate cost-based fee → Deliver to individual
→ Log in access request register → Report to Privacy Officer
```

### 3b. Right to Amendment (§164.526)

| Requirement | Detail | Timeline |
|------------|--------|----------|
| **Scope** | PHI in a Designated Record Set | N/A |
| **Response time** | 60 calendar days from receipt of request; one 30-day extension with written notice | 60 + 30 days max |
| **Acceptance** | If accepted, amend the PHI, inform the individual, and make reasonable efforts to inform others who received the PHI and who may rely on it | Ongoing |
| **Denial grounds** | PHI not created by CE, not part of Designated Record Set, not available for inspection, or already accurate and complete | Written denial |
| **Denial process** | Written denial with basis, right to submit disagreement statement, right to file complaint | Included in denial |

### 3c. Right to Accounting of Disclosures (§164.528)

| Requirement | Detail | Timeline |
|------------|--------|----------|
| **Scope** | Disclosures made in the 6 years prior to the request (or since compliance date if shorter) | 6-year window |
| **Excluded disclosures** | Treatment, payment, health care operations; disclosures authorized by individual; disclosures to the individual; incidental disclosures; national security/intelligence; correctional institution disclosures; limited data set disclosures | N/A |
| **Content per entry** | Date of disclosure, name and address of recipient (if known), brief description of PHI disclosed, brief statement of purpose (or copy of authorization/request) | Per entry |
| **Response time** | 60 calendar days from receipt of request; one 30-day extension with written notice | 60 + 30 days max |
| **Fees** | Free for first request in 12-month period; reasonable cost-based fee for subsequent requests (individual must be informed of fee in advance) | First free per year |

### 3d. Right to Request Restrictions (§164.522(a))

| Requirement | Detail |
|------------|--------|
| **Scope** | Individual may request restriction on uses/disclosures for treatment, payment, or health care operations |
| **CE obligation** | Not required to agree to a restriction, except for the out-of-pocket payment exception |
| **Out-of-pocket exception** | CE MUST agree to restrict disclosures to a health plan for payment or health care operations if the individual has paid for the item or service in full out of pocket (HITECH §13405(a)) |
| **If agreed** | CE must comply with the agreed restriction except in emergencies |
| **Termination** | Either party may terminate an agreed restriction; CE must agree in writing; termination only applies to PHI created or received after termination notice |

### 3e. Right to Confidential Communications (§164.522(b))

| Requirement | Detail |
|------------|--------|
| **Scope** | Individual may request communications about PHI by alternative means or at alternative locations |
| **CE obligation** | Health care providers must accommodate reasonable requests; health plans must accommodate if individual states disclosure could endanger them |
| **No reason required** | Individual is not required to explain the reason for the request |
| **Examples** | Contact at work instead of home; use email instead of mail; send to alternate address |

### 3f. Right to File a Complaint (§164.530(d))

| Requirement | Detail |
|------------|--------|
| **Internal complaint process** | CE must have a process to receive complaints about privacy practices |
| **HHS complaint** | Individual may file with HHS OCR; CE must inform individuals of this right |
| **Non-retaliation** | CE may not retaliate against individual for filing a complaint |
| **Documentation** | CE must document complaints received and their disposition |

---

## 4. Implementation Guidance for AI/Agent Systems

When AI or agent systems interact with patient data or handle patient rights requests, additional controls are needed.

### 4a. Agent Handling of Access Requests

| Consideration | Guidance |
|--------------|---------|
| **Identity verification** | Agents must not process access requests without verified identity — route to human-supervised identity verification workflow |
| **Designated Record Set scope** | Agents must query only Designated Record Set repositories — not operational logs, draft notes, or working files |
| **Format determination** | If individual requests electronic format, agent may assist in data export; final review of exported data should be human-supervised |
| **Denial assessment** | Agents must not autonomously deny access requests — denial grounds require Privacy Officer review |
| **PHI in agent memory** | If agent context/memory contains PHI from the requesting individual, this may be part of the Designated Record Set if used for decisions — assess and include |
| **Audit trail** | Log all access request processing steps in OTel spans with `hipaa.right: access` attribute |

### 4b. Agent Handling of Amendment Requests

| Consideration | Guidance |
|--------------|---------|
| **Scope verification** | Agent may assist in locating PHI in Designated Record Sets for amendment review |
| **Amendment decision** | Accept/deny decisions must be made by a human (Privacy Officer or designee) — agents recommend, humans decide |
| **Propagation** | If amendment is accepted, agent may assist in propagating the amendment to downstream systems and notifying recipients |
| **Agent-generated PHI** | If an agent generated or contributed to the PHI being amended, document the agent's role in the amendment record |

### 4c. Agent Handling of Accounting Requests

| Consideration | Guidance |
|--------------|---------|
| **Disclosure logging** | Agents must log all PHI disclosures in a format that supports accounting — OTel spans with `hipaa.disclosure.recipient`, `hipaa.disclosure.purpose`, `hipaa.disclosure.date` attributes |
| **6-year window** | Disclosure logs must be retained for at least 6 years to support accounting requests |
| **Agent-initiated disclosures** | When agents disclose PHI (e.g., sending PHI to a downstream system or subprocessor), this must be logged as a disclosure |
| **Excluded disclosures** | Agent must correctly categorize disclosures as excluded (treatment, payment, operations) or accountable |

### 4d. Automated Processing Transparency

| Principle | Implementation |
|-----------|---------------|
| **No invisible PHI processing** | All agent processing of PHI must be traceable via OTel spans — Rule 9 applies doubly for PHI |
| **Purpose limitation** | Agent PHI access must include a purpose code matching a permitted use/disclosure category |
| **Human oversight** | Patient rights requests involving agent-processed PHI require human review before response — agents assist but do not autonomously fulfill |

---

## 5. Verification Checklist

### Notice of Privacy Practices
- [ ] NPP drafted with all required elements per §164.520(b)
- [ ] Header statement present ("THIS NOTICE DESCRIBES...")
- [ ] All permitted uses and disclosures described
- [ ] Authorization-required uses identified (marketing, sale, psychotherapy notes)
- [ ] All six individual rights described with instructions for exercising
- [ ] CE duties statement included
- [ ] Complaint process described (internal and HHS OCR)
- [ ] Contact information provided
- [ ] Effective date stated
- [ ] Right to change terms stated
- [ ] NPP posted at service delivery site (if applicable)
- [ ] NPP posted on website
- [ ] NPP provided at first service delivery
- [ ] Written acknowledgment of receipt obtained (or good-faith efforts documented)
- [ ] Material revision process established

### Right to Access (§164.524)
- [ ] Written request process established
- [ ] Identity verification procedure documented
- [ ] 30-day response timeline with extension tracking implemented
- [ ] Electronic format capability for ePHI
- [ ] Cost-based fee schedule documented
- [ ] Denial grounds and process documented
- [ ] Third-party direction process established
- [ ] Access request register maintained

### Right to Amendment (§164.526)
- [ ] Amendment request process established
- [ ] 60-day response timeline with extension tracking implemented
- [ ] Acceptance workflow (amend, notify individual, notify recipients) documented
- [ ] Denial process with required elements (basis, disagreement statement right, complaint right)
- [ ] Amendment propagation procedure documented

### Right to Accounting of Disclosures (§164.528)
- [ ] Disclosure logging system operational
- [ ] 6-year disclosure history maintained
- [ ] Excluded disclosures correctly categorized
- [ ] 60-day response timeline implemented
- [ ] First-free-per-year fee policy documented
- [ ] Required content per entry (date, recipient, PHI description, purpose) captured

### Right to Request Restrictions (§164.522(a))
- [ ] Restriction request process established
- [ ] Out-of-pocket payment exception implemented (mandatory restriction)
- [ ] Restriction agreement documentation maintained
- [ ] Emergency exception procedure documented
- [ ] Restriction termination process established

### Right to Confidential Communications (§164.522(b))
- [ ] Alternative communication request process established
- [ ] Accommodation of reasonable requests documented
- [ ] Communication preferences stored and enforced

### Agent-Specific Controls
- [ ] Agent identity verification routing to human-supervised workflow
- [ ] Agent Designated Record Set query scope limited
- [ ] Agent denial decisions routed to Privacy Officer
- [ ] Agent disclosure logging with HIPAA-specific OTel attributes
- [ ] Agent amendment propagation capability verified
- [ ] 6-year disclosure log retention for agent-initiated disclosures
- [ ] Human oversight for patient rights request fulfillment
