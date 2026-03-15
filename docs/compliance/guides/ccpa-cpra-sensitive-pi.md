<!-- placeholder-ok -->
# CCPA/CPRA — Sensitive Personal Information Handling Controls Guide

> **Implements:** Sensitive Personal Information handling controls
> **Regulation:** California Consumer Privacy Act / California Privacy Rights Act (Cal. Civ. Code §1798.121, §1798.140(ae))
> **Severity:** High — CPRA-specific obligation with CPPA enforcement and significant penalty exposure
> **Related issue:** [#143](https://github.com/wlfghdr/agentic-enterprise/issues/143)
> **Related compliance doc:** [CCPA/CPRA Compliance Reference](../ccpa-cpra.md)
> **Companion guide:** [Opt-Out Mechanism Guide](ccpa-cpra-opt-out.md) — covers the related "Do Not Sell or Share" opt-out requirement

---

## 1. Purpose

CPRA introduced §1798.121, granting consumers the right to limit the use and disclosure of their sensitive personal information (SPI). This right goes beyond general PI protections — it restricts businesses to using SPI only for specified, narrowly defined purposes unless the consumer has not exercised the right to limit.

The Agentic Enterprise framework's [Data Classification Policy](../../../org/4-quality/policies/data-classification.md) provides a four-tier classification system (PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED) that partially addresses SPI through the RESTRICTED classification level. This guide extends that foundation with:

- An explicit CCPA/CPRA-specific SPI taxonomy mapping all 11 statutory categories to framework classification levels
- A consumer-facing "Limit the Use of My Sensitive Personal Information" mechanism
- Purpose limitation controls specific to SPI (distinguishing permitted from non-permitted uses under §1798.121)
- Agent-specific guidance on handling SPI in prompts, responses, logs, and telemetry
- Data minimization controls tailored to SPI processing within agentic workflows

This guide defines the SPI categories, establishes purpose limitation rules, provides agent-specific handling guidance, and maps controls to the framework's existing data classification infrastructure.

---

## 2. Sensitive Personal Information Categories Under CPRA

### 2a. Statutory Definition (§1798.140(ae))

CPRA defines sensitive personal information as PI that reveals or contains any of the following:

| # | SPI Category | §1798.140(ae) Ref | Examples |
|---|-------------|-------------------|----------|
| 1 | **Social Security number, driver's license, state ID, or passport number** | (ae)(1)(A) | SSN, driver's license number, state-issued ID number, passport number |
| 2 | **Account log-in credentials** | (ae)(1)(B) | Username/email combined with password, security question answers, or financial account number combined with access code |
| 3 | **Financial account information** | (ae)(1)(B) | Debit/credit card number combined with access code, password, or security credentials |
| 4 | **Precise geolocation** | (ae)(1)(C) | Any data derived from a device that locates a consumer within a geographic area equal to or less than the area of a circle with a 1,850-foot radius |
| 5 | **Racial or ethnic origin** | (ae)(1)(D) | Self-reported or inferred racial/ethnic information |
| 6 | **Religious or philosophical beliefs** | (ae)(1)(D) | Religious affiliation, philosophical convictions |
| 7 | **Union membership** | (ae)(1)(D) | Trade union membership status |
| 8 | **Contents of communications** | (ae)(1)(E) | Mail, email, and text message content (unless business is the intended recipient) |
| 9 | **Genetic data** | (ae)(1)(F) | Any data resulting from analysis of biological sample that identifies DNA characteristics |
| 10 | **Biometric data for unique identification** | (ae)(1)(F) | Fingerprints, face geometry, iris scans, voiceprints processed for identification purposes |
| 11 | **Health data** | (ae)(1)(G) | Health conditions, diagnoses, treatment information |
| 12 | **Sex life or sexual orientation** | (ae)(1)(H) | Information about sexual behavior, sexual orientation |

### 2b. Mapping SPI Categories to Framework Data Classification

Each SPI category must be mapped to the framework's data classification levels to ensure consistent handling:

| SPI Category | Framework Classification Level | Handling Rules Apply |
|-------------|-------------------------------|---------------------|
| Government IDs (SSN, license, passport) | **RESTRICTED** | Encryption at rest + in transit, access logging, no agent processing without explicit authorization |
| Account credentials | **RESTRICTED** | Never stored in plaintext, never logged, never included in agent prompts or responses |
| Financial account data | **RESTRICTED** | PCI DSS alignment, encryption required, masked in logs |
| Precise geolocation | **CONFIDENTIAL** (minimum) / **RESTRICTED** if combined with identity | Precision reduction where possible, purpose limitation enforced |
| Racial/ethnic origin | **RESTRICTED** | Never inferred by agents, collection only with explicit consent and purpose |
| Religious/philosophical beliefs | **RESTRICTED** | Same as racial/ethnic origin |
| Union membership | **RESTRICTED** | Same as racial/ethnic origin |
| Contents of communications | **CONFIDENTIAL** (minimum) / **RESTRICTED** if containing other SPI | Agent access restricted to intended-recipient scenarios |
| Genetic data | **RESTRICTED** | Maximum controls; rarely applicable to agentic enterprise systems |
| Biometric data | **RESTRICTED** | Never stored beyond active session unless explicitly authorized; deletion on request |
| Health data | **RESTRICTED** | HIPAA alignment where applicable; never inferred by agents without authorization |
| Sex life/sexual orientation | **RESTRICTED** | Never inferred by agents; collection only with explicit consent |

---

## 3. Right to Limit Use and Disclosure (§1798.121)

### 3a. Consumer Right

Consumers have the right to direct a business to limit the use and disclosure of their SPI to only those purposes that are necessary to perform the services or provide the goods reasonably expected by an average consumer.

| Aspect | Requirement | Section |
|--------|------------|---------|
| **Scope of right** | Applies to all SPI categories listed in §1798.140(ae) | §1798.121(a) |
| **"Limit Use" link** | Homepage link titled "Limit the Use of My Sensitive Personal Information" | §1798.135(a)(3) |
| **Alternative combined link** | May use a single "Your Privacy Choices" link that covers both opt-out and limit-use if accompanied by the CPPA-specified icon | §1798.135(a)(4) |
| **No account required** | Business cannot require account creation to exercise the right | §1798.135(a)(1) |
| **Service providers/contractors** | Business must notify service providers and contractors to also limit their use | §1798.121(b) |

### 3b. Permitted Uses After Limitation

When a consumer exercises the right to limit, the business may still use SPI for the following purposes only:

| Permitted Purpose | Description |
|------------------|-------------|
| Performing services or providing goods | Use reasonably necessary and proportionate to perform the services or provide the goods requested by the consumer |
| Security and integrity | Detecting security incidents, protecting against malicious or illegal activity, prosecuting those responsible |
| Safety | Protecting life and physical safety of consumers |
| Short-term transient use | Short-term, transient use where PI is not disclosed to another third party, not used to build a consumer profile, and not used to alter the consumer's experience outside the current interaction |
| Performing services on behalf of the business | Service provider/contractor performing services defined in the contract, including maintaining or servicing accounts, providing customer service, processing transactions, verifying customer information |
| Quality and safety maintenance | Verifying or maintaining the quality or safety of a product, service, or device owned or controlled by the business |
| Collecting or processing SPI where collection is not for inferring characteristics | Processing SPI when the purpose is not to infer characteristics about the consumer (e.g., reading an email to route it, not to profile the consumer) |

### 3c. Non-Permitted Uses After Limitation

If a consumer has exercised the right to limit, the following uses of SPI are prohibited:

| Prohibited Use | Why |
|---------------|-----|
| Profiling or behavioral advertising | Not among permitted purposes; SPI cannot be used to build consumer profiles for advertising |
| Selling or sharing SPI | §1798.121(a) prohibits sale/sharing after limitation |
| Inferring consumer characteristics | Using SPI to derive information about consumer preferences, behaviors, or attributes beyond the current service context |
| Secondary use beyond the original collection purpose | Any use not reasonably necessary to perform the service for which SPI was collected |
| Disclosure to third parties | Except to service providers/contractors under CCPA-compliant contracts for permitted purposes |

---

## 4. Data Minimization Requirements

### 4a. Statutory Minimization Standard

CPRA §1798.100(c) requires that a business's collection, use, retention, and sharing of PI (including SPI) be reasonably necessary and proportionate to the purposes for which it was collected or processed:

| Principle | Application to SPI |
|-----------|-------------------|
| **Collection limitation** | Collect SPI only when strictly necessary for the stated purpose; do not collect SPI speculatively |
| **Use limitation** | Use SPI only for the specific purpose disclosed at collection; do not repurpose without new consent |
| **Retention limitation** | Retain SPI only as long as reasonably necessary for the disclosed purpose; define and enforce retention periods |
| **Sharing limitation** | Disclose SPI to the fewest parties necessary; prefer aggregated or deidentified data when possible |

### 4b. Framework Alignment

| Minimization Requirement | Framework Control | Action Needed |
|-------------------------|-------------------|-----|
| Collection limitation | Data Classification Policy — least-privilege data access | Add SPI-specific collection justification requirements |
| Use limitation | Privacy Policy §1 — purpose documentation | Add SPI-specific purpose limitation enforcement at agent level |
| Retention limitation | [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) — bounded retention | Define SPI-specific retention periods (shorter than general PI) |
| Sharing limitation | [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md) — vendor controls | Add SPI-specific vendor disclosure controls |

---

## 5. Agent-Specific Guidance

### 5a. SPI in Agent Prompts

Agents must never include SPI in prompts unless strictly necessary for the immediate task:

| Rule | Implementation |
|------|---------------|
| **No SPI in system prompts** | System prompts, AGENT.md files, and fleet configurations must never contain SPI |
| **No SPI in few-shot examples** | Example prompts and responses must use synthetic data, never real SPI |
| **SPI in user-context prompts** | If an agent must process SPI to perform a consumer-requested service, include only the minimum SPI fields required; strip all non-essential SPI before prompt construction |
| **SPI classification check** | Before constructing a prompt containing data classified as RESTRICTED, the agent must verify: (1) the processing purpose is permitted, (2) the consumer has not exercised the right to limit (or the use falls within permitted purposes), (3) the SPI is minimized to the fields strictly required |

### 5b. SPI in Agent Responses

| Rule | Implementation |
|------|---------------|
| **No SPI in responses unless requested** | Agents must not include SPI in responses unless the consumer or authorized user explicitly requested the information |
| **Masking by default** | When SPI must be referenced in a response, use partial masking (e.g., `***-**-1234` for SSN, `****-****-****-5678` for card numbers) unless the full value is specifically requested and authorized |
| **No SPI in error messages** | Error messages, exception details, and diagnostic output must never contain SPI |
| **No SPI inference** | Agents must not infer SPI categories (race, religion, sexual orientation, health conditions) from non-SPI data; if an inference is made inadvertently, it must not be stored, logged, or acted upon |

### 5c. SPI in Logs and Telemetry

| Rule | Implementation |
|------|---------------|
| **Never log raw SPI** | OTel spans, structured logs, and telemetry must not contain raw SPI values |
| **Use classification markers** | Log that SPI was processed using `data.classification: RESTRICTED` and `data.spi_category: <category>` attributes, without logging the actual values |
| **Redaction in trace exports** | Configure OTel exporters to redact or drop span attributes that may contain SPI before export to observability platforms |
| **Log retention for SPI events** | SPI processing logs should follow the shorter of: the Log Retention Policy maximum or the SPI-specific retention period defined in this guide |

**Recommended OTel span attributes for SPI processing:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `data.classification` | string | `RESTRICTED` for all SPI |
| `data.spi_category` | string | One of: `government_id`, `account_credentials`, `financial_account`, `precise_geolocation`, `racial_ethnic_origin`, `religious_beliefs`, `union_membership`, `communication_contents`, `genetic_data`, `biometric_data`, `health_data`, `sex_life_orientation` |
| `data.spi_purpose` | string | The permitted purpose justifying processing |
| `data.spi_limit_status` | string | `limited`, `not_limited`, `unknown` |
| `data.spi_minimized` | boolean | Whether the SPI was minimized before processing |

### 5d. SPI in Agent Memory and Context

| Rule | Implementation |
|------|---------------|
| **No persistent SPI in agent memory** | Agents must not retain SPI in conversation history, memory stores, or context windows beyond the active session |
| **Session-scoped SPI** | SPI loaded for a specific task must be cleared from agent context when the task completes |
| **No SPI in training data** | Agent fine-tuning, evaluation datasets, and example stores must not contain real SPI |
| **Context window hygiene** | When agent context is passed to external LLMs, SPI must be stripped or replaced with tokens; the response is then re-mapped to actual values locally |

---

## 6. "Limit Use" Mechanism Design

### 6a. Consumer-Facing Requirements

| Requirement | Implementation |
|-------------|---------------|
| **Homepage link** | "Limit the Use of My Sensitive Personal Information" link on homepage (or combined "Your Privacy Choices" link with CPPA icon) |
| **Limit-use page** | Dedicated page explaining what SPI the business collects, how it is used, and the effect of exercising the right to limit |
| **No account required** | The limit mechanism must be usable without creating an account |
| **Confirmation** | Provide confirmation that the limitation has been applied |
| **Downstream notification** | Notify service providers and contractors to also limit their use of the consumer's SPI |

### 6b. Backend Enforcement

| Component | Design Guidance |
|-----------|----------------|
| **Limit-use state store** | Store per-consumer limit-use state (by account, device, or identifier) alongside opt-out state (see [Opt-Out Guide](ccpa-cpra-opt-out.md)) |
| **Purpose gate** | Before processing SPI, check: (1) is the consumer's limit-use active? (2) if yes, is the current processing purpose in the permitted-use list? (3) if not permitted, block and log |
| **Agent integration** | Agents must query limit-use state before processing SPI; blocked processing emits `privacy.spi_limit.enforced` span event |
| **Audit trail** | Every SPI processing action must be logged with purpose justification, limit-use status, and outcome |

---

## 7. Verification Checklist

### SPI Taxonomy and Classification
- [ ] All 12 CPRA SPI categories are documented and mapped to framework data classification levels
- [ ] Data Classification Policy references CPRA SPI taxonomy for RESTRICTED-level classification decisions
- [ ] Data inventory identifies all SPI categories collected, used, disclosed, or sold by the business
- [ ] Each SPI data flow has a documented lawful purpose that falls within permitted uses

### Right to Limit Mechanism
- [ ] "Limit the Use of My Sensitive Personal Information" link (or combined "Your Privacy Choices" link with CPPA icon) is displayed on the homepage
- [ ] Link leads to a functional limit-use page that does not require account creation
- [ ] Limit-use page explains what SPI is collected, how it is used, and the effect of exercising the right
- [ ] Consumer receives confirmation when the limitation is applied
- [ ] Limit-use state is stored persistently per consumer

### Purpose Limitation Enforcement
- [ ] All SPI processing activities are mapped to one of the permitted purposes listed in §1798.121
- [ ] Processing for non-permitted purposes is blocked when a consumer has exercised the right to limit
- [ ] Purpose gate checks are implemented before every SPI processing action
- [ ] Blocked processing actions are logged with `privacy.spi_limit.enforced` reason

### Data Minimization
- [ ] SPI collection is limited to data strictly necessary for the stated purpose
- [ ] SPI retention periods are defined and are shorter than or equal to general PI retention periods
- [ ] SPI is not repurposed beyond the original collection purpose without new consent
- [ ] Deidentification or aggregation is used in preference to raw SPI where feasible

### Agent SPI Handling
- [ ] System prompts and few-shot examples contain no real SPI
- [ ] Agent prompt construction strips non-essential SPI before including RESTRICTED data
- [ ] Agent responses mask SPI by default (partial values) unless full value is explicitly requested and authorized
- [ ] Agents do not infer SPI categories (race, religion, health, sexual orientation) from non-SPI data
- [ ] Error messages and diagnostic output contain no SPI
- [ ] SPI is cleared from agent context/memory when the task completes

### Logging and Telemetry
- [ ] OTel spans log SPI processing events with `data.classification: RESTRICTED` and `data.spi_category` attributes
- [ ] Raw SPI values are never present in logs, spans, or telemetry exports
- [ ] OTel exporters are configured to redact or drop attributes that may contain SPI
- [ ] SPI processing logs follow SPI-specific retention periods

### Service Provider and Contractor Controls
- [ ] Service providers and contractors processing SPI have CCPA-compliant contracts in place
- [ ] Contracts include SPI-specific restrictions matching permitted purposes
- [ ] Service providers and contractors are notified when a consumer exercises the right to limit
- [ ] Vendor Risk Management assessments include SPI handling evaluation

### Privacy Policy Disclosure
- [ ] Privacy policy identifies the categories of SPI collected
- [ ] Privacy policy discloses the purposes for which SPI is used
- [ ] Privacy policy describes the right to limit use and how to exercise it
- [ ] Privacy policy identifies whether SPI is sold or shared
- [ ] Privacy policy is updated at least annually with current SPI practices
