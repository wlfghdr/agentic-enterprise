<!-- placeholder-ok -->
# HIPAA — Workforce Training Programme

> **Implements:** HIPAA-specific workforce training with documented completion records
> **Regulation:** HIPAA (45 CFR §164.530(b), §164.308(a)(5))
> **Severity:** High — training is mandatory for all workforce members with PHI access; training failures are a common OCR enforcement finding
> **Related issue:** [#147](https://github.com/wlfghdr/agentic-enterprise/issues/147)
> **Related compliance doc:** [HIPAA Compliance Reference](../hipaa.md)

---

## 1. Purpose

HIPAA requires Covered Entities and Business Associates to train all workforce members on policies and procedures related to PHI. The Privacy Rule (§164.530(b)) mandates training on privacy policies for all workforce members, and the Security Rule (§164.308(a)(5)) requires a security awareness and training programme for all workforce members (including management).

The Agentic Enterprise framework provides agent instructions (`AGENT.md` hierarchy) that serve as "training" for AI agents and defines security awareness requirements in the [Security Policy](../../../org/4-quality/policies/security.md). This guide extends that foundation with a formal training programme for the human workforce covering HIPAA-specific topics, training frequency requirements (new hire, periodic refresher, material change), and AI-specific training topics such as PHI handling in AI prompts, agent boundary controls, and automated PHI processing risks.

This guide establishes a complete HIPAA workforce training programme covering training requirements, content, frequency, AI-specific topics, documentation, and a verification checklist.

---

## 2. Training Requirements

### 2a. Who Must Be Trained

HIPAA defines "workforce" broadly to include employees, volunteers, trainees, and other persons whose conduct is under the direct control of the Covered Entity or Business Associate, whether or not they are paid. All workforce members with access to PHI must be trained.

| Workforce Category | Training Required | Scope |
|-------------------|------------------|-------|
| **All workforce members** | Privacy Rule training (§164.530(b)(1)) | Policies and procedures relevant to their job functions |
| **All workforce members** | Security awareness training (§164.308(a)(5)) | Security awareness programme including periodic reminders |
| **New workforce members** | Initial training | Within a reasonable period after joining |
| **Existing workforce members** | Refresher training | Periodically (recommended: annually) |
| **All workforce members** | Material change training | When functions are affected by a material change in policies or procedures |
| **Workforce with agent/AI system access** | AI-specific HIPAA training | PHI risks in AI/agent systems |
| **Management** | Management-specific training | Oversight responsibilities, sanctions policy, incident reporting |

### 2b. Training Timing Requirements

| Trigger | Timeline | CFR Reference |
|---------|----------|---------------|
| **New hire / new role with PHI access** | Within a reasonable period after joining (recommended: within 30 days, before PHI access is granted) | §164.530(b)(1) |
| **Material change in policies or procedures** | Within a reasonable period after the change becomes effective | §164.530(b)(2)(i) |
| **Periodic refresher** | At least annually (recommended; not explicitly mandated but expected by OCR in enforcement actions) | §164.308(a)(5)(ii)(A) — security reminders |
| **Post-incident** | After a privacy or security incident involving the workforce member's area | Best practice |
| **Role change** | When a workforce member's role changes to include new PHI access or responsibilities | §164.530(b)(1) — "relevant to their job functions" |

---

## 3. Training Content

### 3a. Privacy Rule Training (§164.530(b))

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **What is PHI** | Definition, 18 identifiers, PHI vs. de-identified data, examples in the organization's context | 20 min |
| **Permitted uses and disclosures** | Treatment, payment, operations; minimum necessary standard; authorizations; when authorization is not required | 30 min |
| **Patient rights** | Access, amendment, accounting of disclosures, restriction requests, confidential communications, complaint right; how to handle patient requests | 30 min |
| **Notice of Privacy Practices** | Content, distribution requirements, acknowledgment process | 10 min |
| **Minimum necessary standard** | How to determine minimum necessary for specific job functions; role-based access; practical examples | 20 min |
| **Authorizations** | When required, valid authorization elements, revocation | 15 min |
| **Incidental disclosures** | What qualifies as incidental (permitted) vs. impermissible disclosure | 10 min |
| **Organization-specific policies** | Internal privacy policies, PHI handling procedures specific to the workforce member's role | 20 min |
| **Sanctions for violations** | Sanctions policy, examples of violations and consequences | 10 min |

### 3b. Security Rule Training (§164.308(a)(5))

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **Security awareness fundamentals** | Why ePHI security matters, threat landscape, social engineering, phishing | 20 min |
| **Password management** | Strong passwords, multi-factor authentication, password sharing prohibition | 10 min |
| **Workstation security** | Screen lock, clean desk, physical security, remote work requirements | 10 min |
| **Malicious software protection** | Malware recognition, safe browsing, software installation policies | 10 min |
| **Log-in monitoring** | Recognizing unauthorized access attempts, reporting suspicious activity | 10 min |
| **Access controls** | Role-based access, least privilege, access request and revocation procedures | 15 min |
| **Encryption** | When and how to encrypt ePHI (at rest, in transit), encrypted email, encrypted storage | 10 min |
| **Mobile device security** | BYOD policies, mobile device management, remote wipe, secure messaging | 10 min |
| **Incident reporting** | How to recognize and report security incidents, internal reporting channels | 15 min |
| **Physical safeguards** | Facility access, visitor management, device disposal, media sanitization | 10 min |

### 3c. Breach Notification Rule Training

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **What constitutes a breach** | Definition, presumption of breach, risk assessment to determine if notification is required | 15 min |
| **Exceptions to breach definition** | Unintentional acquisition by workforce member, inadvertent disclosure within CE/BA, good-faith belief of no retention | 10 min |
| **Reporting obligations** | Internal reporting procedure, 60-day individual notification, HHS notification (500+ threshold), media notification | 15 min |
| **BA breach reporting** | BA obligations to notify CE, 60-day timeline, required information | 10 min |
| **Breach documentation** | What to document, retention requirements (6 years) | 10 min |

### 3d. Organization-Specific Policy Training

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **PHI locations in the organization** | Where PHI is stored, processed, transmitted — systems inventory | 15 min |
| **Role-specific PHI access** | What PHI the workforce member can access and why (minimum necessary per role) | 15 min |
| **Internal procedures** | PHI request handling, disclosure logging, authorization processing, patient rights request routing | 20 min |
| **Vendor/BA management** | How to handle PHI sharing with Business Associates, BAA requirements | 10 min |
| **Documentation requirements** | What must be documented, where, and how long retained | 10 min |

---

## 4. AI-Specific Training Topics

When the organization uses AI or agent systems that process, access, or interact with PHI, additional training is required.

### 4a. PHI in AI Prompts

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **PHI risk in AI inputs** | How including PHI in prompts, queries, or context windows can create unauthorized disclosure | 15 min |
| **Minimum necessary for AI** | Include only the PHI elements essential for the AI task — never dump full records into prompts | 10 min |
| **Approved AI systems** | Which AI systems are approved for PHI processing (covered by BAAs), which are prohibited | 10 min |
| **Prohibited practices** | Never enter PHI into consumer AI tools (ChatGPT, Gemini, etc.) without organizational approval and BAA; never copy-paste PHI into unauthorized systems | 10 min |
| **De-identification before AI processing** | When and how to de-identify data before using AI tools for analysis | 15 min |

### 4b. Agent Boundary Controls

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **Agent access boundaries** | How agent systems are configured to limit PHI access (tool permissions, CODEOWNERS, AGENT.md hierarchy) | 15 min |
| **Human oversight of agents** | When and how humans must review agent actions involving PHI (AGENTS.md Rule 2) | 10 min |
| **Agent output review** | Verifying agent outputs do not contain unauthorized PHI disclosure before forwarding or publishing | 10 min |
| **Agent audit trail** | How to review agent actions in OTel telemetry, what to look for in agent PHI access logs | 15 min |

### 4c. Automated PHI Processing Risks

| Topic | Content | Duration (est.) |
|-------|---------|----------------|
| **PHI in agent logs and telemetry** | How agent systems may inadvertently capture PHI in logs, traces, and telemetry — and how redaction controls work | 15 min |
| **Agent data retention** | How agent memory, context, and cache handling interacts with PHI retention requirements | 10 min |
| **Hallucinated PHI** | Risk of AI systems generating fabricated patient information that appears real | 10 min |
| **Cross-contamination** | Risk of PHI from one patient appearing in responses about another patient via shared context or model behaviour | 10 min |
| **Breach scenarios involving AI** | Specific breach scenarios involving agent systems: prompt injection leading to PHI extraction, context leakage, unauthorized model training on PHI | 15 min |

---

## 5. Training Frequency and Schedule

| Training Type | Frequency | Audience | Delivery Method |
|--------------|-----------|----------|-----------------|
| **Initial HIPAA training** | Once — within 30 days of hire / before PHI access | All new workforce members | Instructor-led or online course with assessment |
| **Annual refresher — Privacy** | Annually | All workforce members with PHI access | Online course with assessment |
| **Annual refresher — Security** | Annually | All workforce members with PHI access | Online course with assessment |
| **Material change update** | Within reasonable period of change | Affected workforce members | Targeted briefing (email, meeting, or short module) |
| **AI-specific HIPAA training** | Initially + annually | Workforce members using AI/agent systems with PHI | Online course with assessment |
| **Post-incident training** | After relevant incident | Affected team(s) | Targeted briefing based on incident findings |
| **Security reminders** | Periodically (recommended: monthly or quarterly) | All workforce members | Email bulletins, intranet posts, short tips |
| **Management training** | Initially + annually | Management / supervisors | Instructor-led or online with management-specific content |

### 5a. Annual Training Calendar (Recommended)

| Month | Activity |
|-------|---------|
| January | Annual training plan approval by Privacy/Security Officer |
| February-March | Annual refresher training — Privacy Rule |
| April-May | Annual refresher training — Security Rule |
| June | AI-specific HIPAA training (for applicable workforce) |
| July | Mid-year compliance assessment — training completion rates |
| August | Breach Notification Rule refresher |
| September-October | Security awareness month activities, phishing simulation |
| November | Year-end training compliance review |
| December | Training programme evaluation and next-year planning |
| Ongoing | Monthly/quarterly security reminders, new-hire training within 30 days |

---

## 6. Documentation and Evidence Requirements

### 6a. What Must Be Documented (§164.530(b)(2)(ii), §164.530(j))

| Documentation Element | Content | Retention Period |
|----------------------|---------|-----------------|
| **Training policy** | Written training policy describing programme, audience, content, frequency | 6 years from date of creation or last effective date |
| **Training materials** | Copies of all training content (slides, videos, assessments) | 6 years from last use |
| **Completion records** | Per-individual records: name, date, course completed, assessment score, trainer | 6 years from date of training |
| **Assessment results** | Quiz/test scores demonstrating comprehension | 6 years from date of assessment |
| **Acknowledgment forms** | Signed acknowledgments that workforce members received and understand training | 6 years from date of signature |
| **Non-compliance records** | Documentation of workforce members who failed to complete training and remediation actions taken | 6 years from date of record |
| **Training updates** | Records of material changes that triggered additional training, including what changed and when training was delivered | 6 years from date of training |

### 6b. Evidence Collection for OCR Audits

OCR expects the following evidence during audits and enforcement investigations:

| Evidence Type | What OCR Looks For | How to Produce |
|--------------|-------------------|----------------|
| **Training programme documentation** | Written policy, content outline, frequency schedule | Policy document + training plan |
| **Individual completion records** | Proof that each workforce member completed required training | LMS records, sign-in sheets, completion certificates |
| **Timeliness evidence** | Training within required timeframes (new hire, material change, periodic) | Dated completion records correlated with hire dates / change dates |
| **Content adequacy** | Training covers required topics (Privacy, Security, Breach Notification) | Training materials, curriculum outline |
| **Assessment evidence** | Proof of comprehension, not just attendance | Quiz/test scores, practical exercises |
| **Sanctions enforcement** | Evidence that non-compliance with training has consequences | Sanctions policy, records of sanctions applied |
| **Continuous improvement** | Evidence that training is updated based on incidents, audits, and regulatory changes | Training update records, post-incident training evidence |

### 6c. Framework Integration for Documentation

| Framework Component | Training Documentation Use |
|--------------------|---------------------------|
| Git repository | Store training policies, curricula, and material change records as version-controlled files |
| [Observability Policy](../../../org/4-quality/policies/observability.md) | Emit OTel events for training completion (`hipaa.training.completed`) with workforce member ID, course, date, score |
| [Log Retention Policy](../../../org/4-quality/policies/log-retention.md) | Configure 6-year minimum retention for training records |
| Work signals (`work/signals/`) | File signals for training gaps discovered during audits or incidents |
| [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) | Include training gap assessment in incident postmortem template |

---

## 7. Verification Checklist

### Training Programme Structure
- [ ] Written training policy documented and version-controlled
- [ ] Training programme approved by Privacy Officer and Security Officer
- [ ] Training content covers Privacy Rule, Security Rule, and Breach Notification Rule
- [ ] Organization-specific policies included in training content
- [ ] AI-specific HIPAA training module developed (if AI/agent systems process PHI)
- [ ] Assessment/quiz component included to verify comprehension
- [ ] Training delivery method established (instructor-led, online, or hybrid)

### Training Frequency
- [ ] Initial training within 30 days of hire / before PHI access
- [ ] Annual refresher training scheduled and calendared
- [ ] Material change training procedure documented
- [ ] Post-incident training procedure documented
- [ ] Security reminders distributed periodically (monthly or quarterly)
- [ ] Management-specific training scheduled

### Training Content — Privacy Rule
- [ ] PHI definition and 18 identifiers covered
- [ ] Permitted uses and disclosures covered
- [ ] Minimum necessary standard covered
- [ ] Patient rights covered (access, amendment, accounting, restrictions, confidential communications, complaints)
- [ ] Authorization requirements covered
- [ ] NPP content and distribution covered
- [ ] Sanctions policy covered

### Training Content — Security Rule
- [ ] Security awareness fundamentals covered
- [ ] Password management and MFA covered
- [ ] Workstation and physical security covered
- [ ] Malicious software protection covered
- [ ] Access controls and least privilege covered
- [ ] Encryption requirements covered
- [ ] Incident reporting procedures covered

### Training Content — AI-Specific
- [ ] PHI in AI prompts — risks and prohibitions covered
- [ ] Approved vs. prohibited AI systems for PHI processing covered
- [ ] Agent boundary controls and human oversight covered
- [ ] Agent output review procedures covered
- [ ] Automated PHI processing risks (hallucination, cross-contamination, prompt injection) covered
- [ ] De-identification before AI processing covered

### Documentation and Evidence
- [ ] Training completion records maintained per individual
- [ ] Assessment scores recorded and retained
- [ ] Signed acknowledgment forms collected
- [ ] Non-compliance records and remediation actions documented
- [ ] All training documentation retained for minimum 6 years
- [ ] Training records producible for OCR audit within reasonable timeframe
- [ ] Training programme reviewed and updated annually
