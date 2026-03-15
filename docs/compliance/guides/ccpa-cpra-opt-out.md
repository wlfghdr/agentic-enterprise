<!-- placeholder-ok -->
# CCPA/CPRA — "Do Not Sell or Share" Opt-Out Mechanism Guide

> **Implements:** "Do Not Sell or Share" opt-out mechanism
> **Regulation:** California Consumer Privacy Act / California Privacy Rights Act (Cal. Civ. Code §1798.120, §1798.135)
> **Severity:** High — statutory requirement with private right of action exposure and CPPA enforcement
> **Related issue:** [#142](https://github.com/wlfghdr/agentic-enterprise/issues/142)
> **Related compliance doc:** [CCPA/CPRA Compliance Reference](../ccpa-cpra.md)

---

## 1. Purpose

CCPA §1798.120 grants consumers the right to direct a business not to sell or share their personal information. CPRA broadened this right significantly by expanding the definition of "sharing" to include cross-context behavioral advertising — even when no monetary exchange occurs. §1798.135 mandates specific mechanisms businesses must provide, including a conspicuous homepage link and recognition of opt-out preference signals.

The Agentic Enterprise framework provides strong data classification, privacy governance, and agent security controls. This guide extends those controls with:

- A runtime opt-out mechanism and UI component ("Do Not Sell or Share My Personal Information" link)
- Recognition and enforcement of Global Privacy Control (GPC) or other opt-out preference signals
- Backend state management to track and enforce consumer opt-out preferences across agent data flows
- Classification guidance for distinguishing "service provider" processing from "third-party" processing under CPRA's definitions
- Guidance on which agent data flows may constitute "sharing" under CPRA's broad definition

This guide provides the requirements, design patterns, and verification steps to implement these controls.

---

## 2. CCPA/CPRA Opt-Out Requirements

### 2a. Statutory Rights

| Right | Section | Description |
|-------|---------|-------------|
| Right to opt out of sale | §1798.120(a) | Consumer may direct a business that sells their PI to stop selling it |
| Right to opt out of sharing | §1798.120(a) | Consumer may direct a business that shares their PI to stop sharing it (CPRA addition) |
| No sale/sharing of minors' PI without opt-in | §1798.120(c)–(d) | Children under 16 require opt-in consent; children under 13 require parental/guardian consent |
| Opt-out must be honored for 12 months minimum | §1798.135(a)(6) | Business may request opt-in again no sooner than 12 months after opt-out |
| No account required to opt out | §1798.135(a)(1) | Business cannot require consumers to create an account to exercise opt-out |

### 2b. Definitions — Sale vs. Sharing

Understanding the distinction is critical for determining which data flows require an opt-out mechanism:

| Term | Definition | Key Nuance |
|------|-----------|------------|
| **Sale** (§1798.140(ad)) | Selling, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating PI for monetary or other valuable consideration | "Other valuable consideration" is broad — includes barter, reciprocal data exchanges, and indirect benefits |
| **Sharing** (§1798.140(ah)) | Sharing, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating PI for cross-context behavioral advertising | No monetary exchange required — if a third party uses the PI for behavioral advertising, it is "sharing" |
| **Cross-context behavioral advertising** (§1798.140(k)) | Targeting advertising to a consumer based on PI obtained from the consumer's activity across businesses, distinctly-branded websites, applications, or services | Includes tracking pixels, analytics SDKs, and advertising network integrations |

### 2c. Exceptions to Opt-Out

Certain disclosures are exempt from the opt-out requirement:

| Exception | Condition |
|-----------|-----------|
| Service provider processing | PI disclosed to a service provider under a CCPA-compliant contract for a business purpose (§1798.140(ag)) |
| Contractor processing | PI disclosed to a contractor under a CCPA-compliant contract (§1798.140(j)) |
| Consumer-directed disclosure | Consumer intentionally directs disclosure to a third party and uses the third party's service |
| Intentional public disclosure | Consumer intentionally makes PI publicly available |
| Deidentified or aggregate data | Data that meets CCPA deidentification or aggregation standards (§1798.140(m), (a)) |

---

## 3. Opt-Out Mechanism Design

### 3a. Homepage Link Requirements (§1798.135)

CCPA/CPRA mandates specific, conspicuous consumer-facing mechanisms:

| Requirement | Section | Implementation Detail |
|-------------|---------|----------------------|
| **"Do Not Sell or Share My Personal Information" link** | §1798.135(a)(1) | Clear, conspicuous link on homepage; must be titled using this exact phrase (or "Do Not Sell My Personal Information" if business does not share PI) |
| **Alternative: single "Your Privacy Choices" link** | §1798.135(a)(2) | A single link titled "Your Privacy Choices" or "Your California Privacy Choices" may replace the above, provided it is accompanied by an opt-out icon specified by the CPPA |
| **Opt-out page design** | §1798.135(a)(1) | Link leads to a page where consumers can opt out; must not require account creation |
| **"Limit the Use of My Sensitive Personal Information" link** | §1798.135(a)(3) | If the business uses or discloses sensitive PI beyond the listed purposes, a second link is required (see [Sensitive PI Guide](ccpa-cpra-sensitive-pi.md)) |
| **Privacy policy disclosure** | §1798.135(a)(5) | Privacy policy must include: whether the business sells or shares PI, consumer rights, and how to submit opt-out requests |

### 3b. Global Privacy Control (GPC) Signal Support

CPRA and CPPA regulations require businesses to treat user-enabled opt-out preference signals as valid opt-out requests:

| Requirement | Detail |
|-------------|--------|
| **Signal recognition** | Business must treat an opt-out preference signal (e.g., GPC) as a valid request to opt out of sale and sharing (§1798.135(e)) |
| **GPC specification** | Global Privacy Control (Sec-GPC HTTP header, `globalPrivacyControl` JS API) — see [GPC specification](https://globalprivacycontrol.github.io/gpc-spec/) |
| **No conflicting instructions** | If a consumer has both a GPC signal and an account-level "opt-in," the business must resolve the conflict; CPPA guidance favors the most privacy-protective interpretation |
| **No friction or penalty** | Business cannot display pop-ups, charge fees, or degrade service in response to a GPC signal |
| **Scope** | GPC signal applies to the browser or device from which it is sent; if the business can associate the signal with a consumer account, it should apply account-wide |

**Detection implementation:**

| Signal Type | Detection Method | Header/API |
|-------------|-----------------|------------|
| GPC HTTP header | Check for `Sec-GPC: 1` header on incoming requests | `Sec-GPC` |
| GPC JavaScript API | Check `navigator.globalPrivacyControl === true` on page load | `navigator.globalPrivacyControl` |
| Other opt-out preference signals | Monitor CPPA rulemaking for additional recognized signals | TBD per CPPA regulations |

### 3c. Opt-Out State Management

Once a consumer opts out, the business must maintain and enforce that preference:

| Requirement | Implementation Guidance |
|-------------|------------------------|
| **Persistent storage** | Store opt-out state per consumer (by account, device, or cookie identifier) in a dedicated consent/preference datastore |
| **12-month minimum** | Do not prompt the consumer to opt back in for at least 12 months |
| **Downstream propagation** | Notify all third parties to whom PI was sold/shared in the 90 days prior to opt-out (§1798.115(d)) |
| **Real-time enforcement** | All data flows classified as "sale" or "sharing" must check opt-out state before transmitting PI |
| **Agent enforcement** | Agents must query opt-out state before any data flow that could constitute sale or sharing (see Section 4) |

---

## 4. Implementation Guidance for Agentic Systems

### 4a. Agent Data Flows That May Constitute "Sharing"

Under CPRA's broad definition, agent data flows should be evaluated for sale/sharing classification:

| Agent Data Flow | Potential Classification | Analysis |
|----------------|------------------------|----------|
| Agent sends PI to an external LLM API | **May be sharing** if the LLM provider uses the data for model training or other purposes beyond the service contract; **service provider processing** if contract restricts use to performing services for the business | Review LLM provider terms — many providers retain rights to use inputs for improvement |
| Agent sends PI to an analytics or observability platform | **Service provider processing** if the platform contract restricts data use; **sharing** if the platform uses data for its own advertising or profiling purposes | Verify contract terms; see Vendor Risk Management Policy |
| Agent enriches PI with data from a third-party data broker | **May constitute sale** if the data broker receives PI as part of the enrichment exchange | Evaluate whether PI flows bidirectionally |
| Agent generates content that includes PI and publishes externally | **May be sale or sharing** depending on the recipient and their use of the PI | Assess recipient classification and contractual restrictions |
| Agent logs PI to a third-party logging service | **Service provider processing** under proper contract; otherwise may be sharing | Ensure DPA/service-provider contract in place |

### 4b. Service Provider vs. Third-Party Classification

Proper classification determines whether opt-out applies:

| Classification | Criteria (§1798.140) | Opt-Out Required? |
|---------------|----------------------|-------------------|
| **Service provider** | (1) Processes PI on behalf of the business; (2) written contract prohibits selling/sharing, retaining, using, or disclosing PI for any purpose other than performing services; (3) contract includes CCPA-required terms | No — exempt from opt-out |
| **Contractor** | (1) Written contract with CCPA-required terms; (2) business makes PI available for a business purpose; (3) contract certifies understanding and compliance with CCPA restrictions | No — exempt from opt-out |
| **Third party** | Any entity that is not the business, a service provider, or a contractor | **Yes** — PI transfers to third parties are sale or sharing and subject to opt-out |

**Framework action:** Review every external integration in `org/integrations/` and classify each as service provider, contractor, or third party. Document the classification and contractual basis in the integration definition file.

### 4c. Agent Opt-Out Enforcement Pattern

Agents processing PI must enforce opt-out state. The recommended pattern:

1. **Before any external data transmission**, the agent queries the consumer's opt-out state
2. **If opt-out is active** and the transmission would constitute sale or sharing, the agent blocks the transmission and logs the blocked action with reason `ccpa.opt_out.enforced`
3. **If opt-out is not active** or the transmission is exempt (service provider processing), the agent proceeds and logs the classification decision
4. **OTel instrumentation**: all opt-out checks emit a span event:

| Span Event | Attributes | Values |
|------------|-----------|--------|
| `privacy.opt_out.check` | `privacy.opt_out.status` | `opted_out`, `opted_in`, `unknown` |
| | `privacy.opt_out.signal_source` | `gpc`, `manual`, `account`, `cookie` |
| | `privacy.data_flow.classification` | `sale`, `sharing`, `service_provider`, `contractor`, `exempt` |
| | `privacy.opt_out.action` | `blocked`, `permitted`, `escalated` |

---

## 5. Privacy Policy and Notice Requirements

The following disclosures must appear in the business's privacy policy:

| Disclosure | Section | Content Requirement |
|-----------|---------|-------------------|
| Whether business sells or shares PI | §1798.130(a)(5)(B) | Explicit statement; if yes, categories of PI sold/shared and categories of third parties |
| Right to opt out | §1798.135(a)(5) | Description of the right and how to exercise it |
| "Do Not Sell or Share" link | §1798.135(a)(1) | Link to opt-out mechanism |
| Opt-out preference signal recognition | §1798.135(e) | Statement that business honors GPC or other recognized signals |
| Categories of PI sold/shared in past 12 months | §1798.130(a)(5)(C) | Updated annually; if none, state "none" |

---

## 6. Verification Checklist

### Opt-Out Mechanism
- [ ] "Do Not Sell or Share My Personal Information" link (or "Your Privacy Choices" with CPPA-specified icon) is displayed on the homepage
- [ ] Link leads to a functional opt-out page that does not require account creation
- [ ] Opt-out page clearly describes what sale/sharing means and what the opt-out covers
- [ ] Opt-out can be exercised with a single, simple step (no unnecessary friction)
- [ ] Opt-out preference is stored persistently per consumer (account, device, or identifier)
- [ ] 12-month minimum opt-out period is enforced before re-prompting for opt-in

### Global Privacy Control (GPC)
- [ ] `Sec-GPC: 1` HTTP header is detected on incoming requests
- [ ] `navigator.globalPrivacyControl` JavaScript API is checked on page load
- [ ] GPC signal is treated as a valid opt-out request for sale and sharing
- [ ] No friction, pop-ups, or service degradation in response to GPC signal
- [ ] GPC-triggered opt-out is applied to the associated consumer account (if identifiable)

### Data Flow Classification
- [ ] All external integrations in `org/integrations/` are classified as service provider, contractor, or third party
- [ ] Classification is documented with contractual basis for each integration
- [ ] Contracts with service providers and contractors include CCPA-required terms (§1798.140(ag), (j))
- [ ] Third-party data flows are identified and subject to opt-out enforcement

### Agent Enforcement
- [ ] Agents query consumer opt-out state before external PI transmissions that constitute sale or sharing
- [ ] Opt-out state check blocks sale/sharing transmissions when opt-out is active
- [ ] Blocked transmissions are logged with `privacy.opt_out.enforced` reason
- [ ] OTel span events are emitted for all opt-out checks with required attributes
- [ ] Service provider and contractor transmissions proceed with classification logged

### Downstream Notification
- [ ] Third parties that received PI via sale/sharing in the 90 days prior to opt-out are notified of the opt-out (§1798.115(d))
- [ ] Notification process is documented and tracked

### Privacy Policy Disclosure
- [ ] Privacy policy states whether the business sells or shares PI
- [ ] Privacy policy describes the right to opt out and how to exercise it
- [ ] Privacy policy identifies categories of PI sold/shared in the past 12 months
- [ ] Privacy policy states that the business recognizes GPC and other opt-out preference signals
- [ ] Privacy policy is updated at least annually

### Minors
- [ ] If business has actual knowledge that a consumer is under 16, PI is not sold or shared without opt-in consent
- [ ] If business has actual knowledge that a consumer is under 13, parental/guardian opt-in consent is obtained before sale or sharing
