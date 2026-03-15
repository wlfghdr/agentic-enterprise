<!-- placeholder-ok -->
# HIPAA — Business Associate Agreement Template

> **Implements:** Business Associate Agreement (BAA) template with required provisions
> **Regulation:** HIPAA (45 CFR §164.502(e), §164.504(e)), as amended by HITECH Act
> **Severity:** High — BAAs are mandatory before any Business Associate creates, receives, maintains, or transmits PHI on behalf of a Covered Entity
> **Related issue:** [#144](https://github.com/wlfghdr/agentic-enterprise/issues/144)
> **Related compliance doc:** [HIPAA Compliance Reference](../hipaa.md)

---

## 1. Purpose

HIPAA requires Covered Entities to enter into a Business Associate Agreement (BAA) with every Business Associate before allowing them to create, receive, maintain, or transmit Protected Health Information (PHI). The HITECH Act extended direct liability to Business Associates and strengthened BAA requirements.

The Agentic Enterprise framework provides a Data Processing Agreement (DPA) template via the [Privacy Policy](../../../org/4-quality/policies/privacy.md) and contractual controls via the [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md). This guide extends those controls with HIPAA-specific BAA provisions — particularly the required clauses around permitted uses and disclosures of PHI, return or destruction of PHI at termination, subcontractor flow-down requirements, and the specific breach notification obligations under the Breach Notification Rule.

This guide provides the complete BAA template with all required clauses, agent-specific considerations for AI/agent systems acting as Business Associates, and a verification checklist for confirming BAA compliance.

---

## 2. BAA Requirements Under HIPAA

### 2a. When a BAA Is Required

A BAA must be in place whenever a Covered Entity engages a Business Associate to perform a function or activity involving PHI. The HITECH Act also requires BAAs between Business Associates and their subcontractors.

| Relationship | BAA Required | Legal Basis |
|-------------|-------------|-------------|
| Covered Entity to Business Associate | Yes — before PHI access begins | §164.502(e)(1), §164.504(e)(1) |
| Business Associate to Subcontractor | Yes — same terms as CE-BA agreement | §164.502(e)(1)(ii), HITECH §13401 |
| Covered Entity to Covered Entity | No — but data use agreements may apply | §164.502(e)(1) exception |
| Covered Entity to workforce members | No — workforce is not a Business Associate | §160.103 definition |

### 2b. What Constitutes a Business Associate

| Category | Examples | BAA Needed |
|----------|----------|-----------|
| **Claims processing / administration** | Billing services, claims clearinghouses | Yes |
| **Data analysis / processing** | Analytics vendors, AI/ML service providers, agent systems processing PHI | Yes |
| **Utilization review** | Care management platforms | Yes |
| **Quality assurance** | External audit firms reviewing PHI | Yes |
| **Legal / actuarial / accounting** | Law firms, actuaries, accountants with PHI access | Yes |
| **Management / administration** | Practice management systems, EHR vendors | Yes |
| **Cloud / hosting services** | Cloud providers storing ePHI, SaaS platforms | Yes |
| **Health Information Exchange** | HIE organizations, data intermediaries | Yes |

### 2c. Required BAA Provisions (§164.504(e)(2))

The following provisions are mandatory in every BAA:

| Required Provision | CFR Reference | Purpose |
|-------------------|---------------|---------|
| Permitted and required uses/disclosures | §164.504(e)(2)(i) | Limits BA's use of PHI to contract performance, BA's own obligations, and as required by law |
| Prohibition on unauthorized use/disclosure | §164.504(e)(2)(ii)(A) | BA may not use or disclose PHI except as permitted by BAA or required by law |
| Appropriate safeguards | §164.504(e)(2)(ii)(B) | BA must use appropriate safeguards to prevent unauthorized use/disclosure |
| Breach reporting | §164.504(e)(2)(ii)(C) | BA must report any use or disclosure not provided for by the BAA, including breaches of unsecured PHI |
| Subcontractor requirements | §164.504(e)(2)(ii)(D) | BA must ensure subcontractors agree to the same restrictions and conditions |
| Access to PHI | §164.504(e)(2)(ii)(E) | BA must make PHI available to individuals to satisfy CE's access obligations (§164.524) |
| Amendment of PHI | §164.504(e)(2)(ii)(F) | BA must make PHI available for amendment and incorporate amendments (§164.526) |
| Accounting of disclosures | §164.504(e)(2)(ii)(G) | BA must make information available for accounting of disclosures (§164.528) |
| HHS access | §164.504(e)(2)(ii)(H) | BA must make internal practices, books, and records available to HHS |
| Return or destruction of PHI | §164.504(e)(2)(ii)(I) | BA must return or destroy all PHI at termination, if feasible |
| Termination for material breach | §164.504(e)(2)(iii) | CE may terminate BAA if BA violates a material term |

---

## 3. BAA Template

The following template contains all required and recommended clauses. Replace `{{PLACEHOLDER}}` values with organization-specific information.

```
BUSINESS ASSOCIATE AGREEMENT

This Business Associate Agreement ("Agreement") is entered into as of
{{EFFECTIVE_DATE}} ("Effective Date") by and between:

    Covered Entity:     {{CE_LEGAL_NAME}}
    Address:            {{CE_ADDRESS}}
    ("Covered Entity" or "CE")

    Business Associate: {{BA_LEGAL_NAME}}
    Address:            {{BA_ADDRESS}}
    ("Business Associate" or "BA")

collectively referred to as the "Parties."

RECITALS

WHEREAS, Covered Entity and Business Associate have entered into or intend
to enter into an arrangement ("Underlying Agreement") pursuant to which
Business Associate may create, receive, maintain, or transmit Protected
Health Information on behalf of Covered Entity; and

WHEREAS, the Parties intend to comply with the requirements of the Health
Insurance Portability and Accountability Act of 1996, as amended by the
Health Information Technology for Economic and Clinical Health Act
(collectively, "HIPAA"), and the regulations promulgated thereunder at
45 CFR Parts 160 and 164 (the "HIPAA Rules");

NOW, THEREFORE, in consideration of the mutual promises and covenants
contained herein, the Parties agree as follows:

ARTICLE 1 — DEFINITIONS

1.1  Terms used but not otherwise defined in this Agreement shall have
     the same meaning as those terms in the HIPAA Rules, including but
     not limited to: Breach, Business Associate, Covered Entity,
     Designated Record Set, Electronic Protected Health Information
     (ePHI), Individual, Minimum Necessary, Protected Health
     Information (PHI), Required by Law, Security Incident,
     Subcontractor, and Unsecured Protected Health Information.

1.2  "Services" means the functions, activities, or services performed
     by Business Associate on behalf of Covered Entity under the
     Underlying Agreement that involve the use or disclosure of PHI.

ARTICLE 2 — PERMITTED USES AND DISCLOSURES OF PHI

2.1  Business Associate may use or disclose PHI solely:
     (a) As necessary to perform the Services under the Underlying
         Agreement;
     (b) As Required by Law;
     (c) For the proper management and administration of Business
         Associate, provided that:
         (i)   the disclosure is Required by Law; or
         (ii)  Business Associate obtains reasonable assurances from the
               recipient that the PHI will be held confidentially, used
               or further disclosed only as Required by Law or for the
               purposes for which it was disclosed, and the recipient
               will notify Business Associate of any instances of which
               it becomes aware in which the confidentiality of the
               information has been breached;
     (d) To provide Data Aggregation services relating to the health
         care operations of Covered Entity, if permitted under the
         Underlying Agreement.

2.2  Business Associate shall not use or disclose PHI in a manner that
     would violate Subpart E of 45 CFR Part 164 if done by Covered
     Entity, except as permitted under Sections 2.1(c) and 2.1(d).

2.3  Business Associate shall comply with the Minimum Necessary standard
     (§164.502(b)) when using or disclosing PHI. Business Associate
     shall limit its use, disclosure, or request of PHI to the minimum
     necessary to accomplish the intended purpose.

ARTICLE 3 — SAFEGUARDS

3.1  Business Associate shall implement administrative, physical, and
     technical safeguards that reasonably and appropriately protect the
     confidentiality, integrity, and availability of ePHI that it
     creates, receives, maintains, or transmits on behalf of Covered
     Entity, as required by the Security Rule (45 CFR Part 164,
     Subpart C).

3.2  Business Associate shall comply with the Security Rule requirements
     applicable to Business Associates, including but not limited to:
     (a) Conducting a risk analysis (§164.308(a)(1)(ii)(A));
     (b) Implementing risk management measures (§164.308(a)(1)(ii)(B));
     (c) Implementing access controls (§164.312(a));
     (d) Implementing audit controls (§164.312(b));
     (e) Implementing integrity controls (§164.312(c));
     (f) Implementing transmission security (§164.312(e)).

3.3  Business Associate shall document and keep current its security
     policies and procedures as required by §164.316.

ARTICLE 4 — BREACH REPORTING AND SECURITY INCIDENTS

4.1  Business Associate shall report to Covered Entity any use or
     disclosure of PHI not permitted by this Agreement of which it
     becomes aware, including any Breach of Unsecured PHI, without
     unreasonable delay and in no case later than sixty (60) calendar
     days after discovery of the Breach.

4.2  A Breach is considered "discovered" as of the first day on which
     the Breach is known to Business Associate or, by exercising
     reasonable diligence, would have been known to Business Associate.

4.3  Business Associate's Breach notification to Covered Entity shall
     include, to the extent available:
     (a) Identification of each individual whose Unsecured PHI has been,
         or is reasonably believed to have been, accessed, acquired,
         used, or disclosed;
     (b) A description of what happened, including the date of the
         Breach and the date of discovery;
     (c) A description of the types of Unsecured PHI involved;
     (d) Steps Business Associate recommends that affected individuals
         take to protect themselves;
     (e) A description of what Business Associate is doing to
         investigate, mitigate, and prevent future Breaches.

4.4  Business Associate shall report to Covered Entity any Security
     Incident (as defined in §164.304) of which it becomes aware. The
     Parties acknowledge that unsuccessful Security Incidents (e.g.,
     pings, port scans, unsuccessful log-on attempts, denied access)
     occur routinely and that notice of such unsuccessful attempts shall
     be provided via aggregate reporting on a {{REPORTING_FREQUENCY}}
     basis.

ARTICLE 5 — SUBCONTRACTORS

5.1  Business Associate shall ensure that any Subcontractor that creates,
     receives, maintains, or transmits PHI on behalf of Business
     Associate agrees in writing to the same restrictions, conditions,
     and requirements that apply to Business Associate under this
     Agreement with respect to such PHI.

5.2  Business Associate shall remain responsible for any acts or
     omissions of its Subcontractors that cause Business Associate to
     violate the terms of this Agreement.

5.3  Business Associate shall maintain an up-to-date list of all
     Subcontractors with access to PHI and make this list available to
     Covered Entity upon request.

ARTICLE 6 — INDIVIDUAL RIGHTS — ACCESS, AMENDMENT, ACCOUNTING

6.1  ACCESS. Business Associate shall make PHI maintained in a
     Designated Record Set available to Covered Entity (or, at Covered
     Entity's direction, to an Individual) within {{ACCESS_DAYS}}
     calendar days of a request, in the form and format requested if
     readily producible, to enable Covered Entity to fulfill its
     obligations under §164.524.

6.2  AMENDMENT. Business Associate shall, within {{AMENDMENT_DAYS}}
     calendar days of receiving a request from Covered Entity, make PHI
     available for amendment and incorporate any amendments to PHI in a
     Designated Record Set, as directed by Covered Entity, to enable
     Covered Entity to fulfill its obligations under §164.526.

6.3  ACCOUNTING OF DISCLOSURES. Business Associate shall maintain a log
     of disclosures of PHI made by Business Associate as would be
     required for Covered Entity to respond to a request for an
     accounting of disclosures under §164.528. Business Associate shall
     make such information available to Covered Entity within
     {{ACCOUNTING_DAYS}} calendar days of a request. The accounting
     shall cover disclosures made during the six (6) years prior to
     the request (or since the Agreement's Effective Date if less than
     six years).

ARTICLE 7 — HHS ACCESS

7.1  Business Associate shall make its internal practices, books, and
     records relating to the use and disclosure of PHI available to the
     Secretary of the U.S. Department of Health and Human Services
     for purposes of determining compliance with the HIPAA Rules.

ARTICLE 8 — RETURN OR DESTRUCTION OF PHI

8.1  Upon termination of this Agreement or the Underlying Agreement, for
     whatever reason, Business Associate shall:
     (a) Return to Covered Entity or destroy all PHI received from
         Covered Entity, or created, received, maintained, or
         transmitted on behalf of Covered Entity, in all forms
         (electronic, paper, oral records of PHI);
     (b) Retain no copies of such PHI in any form; and
     (c) Certify in writing to Covered Entity that all PHI has been
         returned or destroyed within {{DESTRUCTION_DAYS}} calendar days
         of termination.

8.2  If return or destruction of PHI is not feasible, Business Associate
     shall:
     (a) Notify Covered Entity in writing of the conditions that make
         return or destruction infeasible;
     (b) Extend the protections of this Agreement to any retained PHI;
     (c) Limit further uses and disclosures of the retained PHI to
         those purposes that make return or destruction infeasible; and
     (d) Return or destroy the PHI when it becomes feasible to do so.

ARTICLE 9 — TERM AND TERMINATION

9.1  This Agreement shall be effective as of the Effective Date and
     shall terminate when all PHI provided by Covered Entity to Business
     Associate, or created, received, maintained, or transmitted by
     Business Associate on behalf of Covered Entity, is destroyed or
     returned to Covered Entity.

9.2  Covered Entity may terminate this Agreement and the Underlying
     Agreement if Covered Entity determines that Business Associate has
     violated a material term of this Agreement and Business Associate
     has not cured the breach within {{CURE_PERIOD_DAYS}} calendar days
     of receiving written notice of the breach from Covered Entity.

9.3  If cure is not possible, Covered Entity may immediately terminate
     this Agreement.

9.4  The obligations of Business Associate under Articles 3, 4, 7, and
     8 shall survive termination of this Agreement.

ARTICLE 10 — MISCELLANEOUS

10.1 AMENDMENT. This Agreement may not be modified or amended except by
     a written instrument signed by both Parties. The Parties agree
     to amend this Agreement as necessary to comply with changes to
     the HIPAA Rules.

10.2 INTERPRETATION. Any ambiguity in this Agreement shall be resolved
     in favor of a meaning that permits the Parties to comply with the
     HIPAA Rules.

10.3 GOVERNING LAW. This Agreement shall be governed by federal law
     (HIPAA and HITECH) and, to the extent not preempted, the laws of
     {{GOVERNING_STATE}}.

10.4 NOTICES. All notices under this Agreement shall be in writing and
     sent to the addresses listed above or such other address as either
     Party may designate in writing.

IN WITNESS WHEREOF, the Parties have executed this Business Associate
Agreement as of the Effective Date.

COVERED ENTITY:

{{CE_SIGNATORY_NAME}}
{{CE_SIGNATORY_TITLE}}
Date: {{CE_SIGNATURE_DATE}}

BUSINESS ASSOCIATE:

{{BA_SIGNATORY_NAME}}
{{BA_SIGNATORY_TITLE}}
Date: {{BA_SIGNATURE_DATE}}
```

---

## 4. Agent-Specific BAA Considerations

When AI or agent systems function as Business Associates — creating, receiving, maintaining, or transmitting PHI — the BAA must address additional considerations beyond traditional vendor relationships.

### 4a. AI/Agent Systems as Business Associates

| Scenario | BAA Implication | Additional Clause Needed |
|----------|----------------|-------------------------|
| Agent processes PHI in prompts or context | Agent vendor is a Business Associate | Specify that PHI in AI prompts is PHI under the BAA |
| Agent stores PHI in logs, traces, or telemetry | Logs containing PHI are subject to BAA protections | Require log redaction or PHI-aware logging configuration |
| Agent generates outputs containing PHI | Generated content inherits PHI classification | Specify output handling and downstream disclosure rules |
| Agent training on PHI | Use of PHI for model training is a disclosure | Explicitly prohibit or separately authorize PHI use for training |
| Agent subprocessors (model providers, cloud infra) | Each subprocessor with PHI access needs a subcontractor BAA | Require disclosure of all AI subprocessors |

### 4b. Recommended Additional Clauses for Agent BAAs

Add the following clauses to the BAA template when the Business Associate operates AI/agent systems:

```
ARTICLE 11 — AI AND AGENT SYSTEM PROVISIONS

11.1 PROHIBITION ON TRAINING. Business Associate shall not use PHI
     received from or on behalf of Covered Entity to train, fine-tune,
     or improve any machine learning model, artificial intelligence
     system, or algorithm, unless explicitly authorized in writing by
     Covered Entity.

11.2 PROMPT AND CONTEXT HANDLING. Business Associate acknowledges that
     PHI included in prompts, queries, context windows, or other inputs
     to AI or agent systems is PHI subject to all protections of this
     Agreement. Business Associate shall implement technical controls
     to prevent PHI in prompts from being retained beyond the duration
     of the specific transaction or session.

11.3 OUTPUT CONTROLS. Business Associate shall implement controls to
     prevent AI or agent systems from including PHI in outputs
     (responses, logs, reports, telemetry) except as necessary to
     perform the permitted Services. Any PHI in outputs shall be
     subject to the same safeguard requirements as PHI in inputs.

11.4 AUTOMATED PROCESSING TRANSPARENCY. Business Associate shall,
     upon request, provide Covered Entity with:
     (a) A description of the types of automated processing performed
         on PHI;
     (b) The categories of PHI processed;
     (c) The AI or agent systems and subprocessors involved;
     (d) The safeguards applied to PHI during automated processing.

11.5 AI SUBPROCESSOR DISCLOSURE. Business Associate shall maintain and
     provide to Covered Entity a list of all AI model providers,
     cloud infrastructure providers, and other technology subprocessors
     that may have access to PHI during automated processing. This
     list shall be updated at least {{SUBPROCESSOR_UPDATE_FREQUENCY}}
     and whenever a new subprocessor is engaged.
```

### 4c. Framework Integration

| Framework Component | BAA Relevance | Action Required |
|--------------------|---------------|-----------------|
| [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md) | Tier classification of BA vendors | Classify all BAs as Tier 1 (Critical) or Tier 2 (Material) — PHI access makes a vendor at least Tier 2 |
| [Privacy Policy](../../../org/4-quality/policies/privacy.md) | DPA template overlap | Use BAA for HIPAA-governed relationships; DPA for GDPR-governed relationships; combine if both apply |
| [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) | Agent tool access controls | Ensure agent tool permissions enforce minimum necessary PHI access |
| [OTel Contract](../../otel-contract.md) | Telemetry containing PHI | Configure `privacy.redact_by_default: true` for PHI-related spans; ensure PHI is not leaked into telemetry attributes |
| `CONFIG.yaml` | BA registry | Maintain a list of active BAAs with effective dates, renewal dates, and scope descriptions |

---

## 5. Verification Checklist

### BAA Existence and Coverage
- [ ] All Business Associates identified and inventoried
- [ ] BAA executed with every Business Associate before PHI access
- [ ] BAAs executed between Business Associates and their subcontractors
- [ ] BAA inventory maintained with effective dates, renewal dates, and scope
- [ ] Annual review of BAA inventory for completeness

### Required Provisions Present
- [ ] Permitted and required uses/disclosures defined (§164.504(e)(2)(i))
- [ ] Prohibition on unauthorized use/disclosure included (§164.504(e)(2)(ii)(A))
- [ ] Appropriate safeguards requirement included (§164.504(e)(2)(ii)(B))
- [ ] Breach reporting obligation with 60-day outer limit (§164.504(e)(2)(ii)(C))
- [ ] Subcontractor flow-down requirement included (§164.504(e)(2)(ii)(D))
- [ ] Individual access rights provision included (§164.504(e)(2)(ii)(E))
- [ ] Amendment rights provision included (§164.504(e)(2)(ii)(F))
- [ ] Accounting of disclosures provision included (§164.504(e)(2)(ii)(G))
- [ ] HHS access provision included (§164.504(e)(2)(ii)(H))
- [ ] Return or destruction of PHI at termination (§164.504(e)(2)(ii)(I))
- [ ] Termination for material breach provision included (§164.504(e)(2)(iii))

### Agent-Specific Provisions (if applicable)
- [ ] Prohibition on PHI use for AI model training included
- [ ] Prompt and context window PHI handling addressed
- [ ] Output controls for PHI in AI-generated responses specified
- [ ] Automated processing transparency requirements included
- [ ] AI subprocessor list maintained and shared with Covered Entity
- [ ] Telemetry and logging PHI redaction requirements specified

### Operational Compliance
- [ ] BAA terms reflected in operational controls (access controls, logging, encryption)
- [ ] Breach notification procedure tested and documented
- [ ] Subcontractor BAA compliance verified
- [ ] PHI return/destruction procedure documented and tested
- [ ] Annual BAA compliance review scheduled
