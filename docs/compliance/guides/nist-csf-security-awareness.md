<!-- placeholder-ok -->
# NIST CSF 2.0 — Security Awareness Programme Guide

> **Implements:** Formal human security awareness training programme
> **Standard:** NIST Cybersecurity Framework (CSF) 2.0
> **Severity:** High — agent instructions are not a human training programme
> **Related issue:** [#136](https://github.com/wlfghdr/agentic-enterprise/issues/136)
> **Related compliance doc:** [NIST CSF 2.0 Compliance Reference](../nist-csf.md)

---

## 1. Purpose

The Agentic Enterprise framework uses agent instructions (`AGENT.md` hierarchy, AGENTS.md Rule 4 "Policies are law") as the mechanism for ensuring agents operate within security boundaries. For agents, this is effective — instructions are deterministically loaded before every task, version-controlled, and auditable via Git history.

NIST CSF 2.0 subcategories PR.AT-01 and PR.AT-02 require security awareness and training for *human* personnel, not just machine agents. Humans interact with the framework as PR reviewers, policy authors, executive approvers, and system operators. They face human-targeted threats (phishing, social engineering, credential theft) that agent instructions do not address, and they must understand AI-specific risks (prompt injection, data leakage through AI systems, over-reliance on AI recommendations) that are unique to operating an agentic enterprise.

This guide defines the security awareness programme design for PR.AT-01 and PR.AT-02 compliance — covering training topics, delivery methods, role-based curricula, and measurable outcomes.

---

## 2. Security Awareness Requirements per NIST CSF

| Subcategory | Requirement | What's Needed Beyond Framework |
|-------------|-------------|-------------------------------|
| PR.AT-01 | Awareness and training provided to all users | Formal security awareness programme for all humans who interact with the framework — developers, operators, reviewers, executives |
| PR.AT-02 | Privileged users understand roles and responsibilities | Enhanced training for users with elevated access: Steering Layer approvers, CODEOWNERS, infrastructure operators, IdP administrators |

### Supporting NIST SP 800-53 Controls

The CSF subcategories map to detailed controls in NIST SP 800-53 Rev. 5:

| SP 800-53 Control | Description | Programme Requirement |
|-------------------|-------------|----------------------|
| AT-1 | Policy and procedures for awareness and training | Documented programme charter with scope, roles, and review cadence |
| AT-2 | Literacy training and awareness | Baseline security awareness for all personnel, delivered annually |
| AT-2(2) | Insider threat awareness | Training on recognizing and reporting insider threats, including misuse of AI agent capabilities |
| AT-2(3) | Social engineering and mining | Phishing simulations, pretexting scenarios, AI-enhanced social engineering awareness |
| AT-3 | Role-based training | Differentiated curricula for developers, operators, executives, and privileged users |
| AT-4 | Training records | Completion tracking, assessment scores, compliance evidence |

---

## 3. Security Awareness Programme Design

### 3a. Training Topics

The programme covers both traditional cybersecurity topics and AI-specific risks unique to operating an agentic enterprise.

**Core Topics (All Personnel):**

| Topic | Content Areas | Relevance to Agentic Enterprise |
|-------|---------------|--------------------------------|
| **Phishing and social engineering** | Email phishing, spear phishing, pretexting, vishing, AI-generated deepfakes | Attackers may impersonate agent communications or use AI to craft convincing phishing |
| **Credential security** | Strong passwords, MFA usage, credential sharing prohibition, phishing-resistant auth | IdP credentials control access to Git governance, observability, and agent configurations |
| **Data handling** | Data classification levels, handling rules per classification, data loss prevention | Framework processes classified data (data-classification policy defines 4 levels) |
| **Incident reporting** | How to report suspected incidents, reporting channels, no-blame culture | Humans are sensors — early reporting enables the incident response policy to activate |
| **Acceptable use** | Authorized use of framework tools, AI systems, and organizational data | Operators must understand boundaries of agent autonomy and their oversight role |
| **Physical security basics** | Clean desk, screen lock, visitor management, device security | Applies to on-premise deployments and developer workstations |
| **Removable media and BYOD** | USB device risks, personal device policies, mobile security | Relevant for developers with repository access on personal devices |

**AI-Specific Topics (All Personnel):**

| Topic | Content Areas | Relevance to Agentic Enterprise |
|-------|---------------|--------------------------------|
| **Prompt injection risks** | Direct and indirect prompt injection, jailbreaking, instruction hijacking | Agents process external inputs — humans must recognize when outputs may be manipulated |
| **Agent boundary violations** | Recognizing when agents operate outside their defined lane, unauthorized scope expansion | AGENTS.md Rule 5 "Stay in your lane" — humans must verify agent compliance |
| **Data leakage through AI** | Sensitive data in prompts, training data extraction, context window risks | Agents handle classified data — humans must understand leakage vectors |
| **Over-reliance on AI** | Automation bias, uncritical acceptance of agent recommendations, verification responsibility | AGENTS.md Rule 2 "Humans decide, agents recommend" — training reinforces this principle |
| **AI-generated content risks** | Hallucinations, fabricated evidence, plausible but incorrect outputs | AGENTS.md Rule 1 "Grounded, not speculative" — humans must verify agent claims |
| **Supply chain AI risks** | Compromised models, poisoned training data, adversarial inputs to vendor AI | Vendor risk management extends to AI components in the supply chain |

### 3b. Delivery Methods

| Method | Frequency | Audience | Purpose |
|--------|-----------|----------|---------|
| **Annual baseline training** | Once per year (mandatory) | All personnel | Comprehensive programme covering all core and AI-specific topics |
| **Quarterly micro-learning** | Every 3 months | All personnel | Short (10-15 min) focused modules on seasonal or emerging threats |
| **Phishing simulations** | Monthly | All personnel | Simulated phishing emails to measure and improve detection capability |
| **Event-triggered training** | As needed | Affected personnel | After a real incident, policy change, new threat landscape, or framework update |
| **Onboarding training** | First week of employment/engagement | New personnel | Security awareness as part of onboarding, before granting framework access |
| **Tabletop exercises** | Semi-annually | Incident responders, operators | Scenario-based exercises using framework-specific incidents (agent compromise, data breach) |
| **Lunch-and-learn sessions** | Monthly (optional) | Interested personnel | Deep dives on emerging topics (new AI threats, regulatory changes, framework updates) |

### 3c. Role-Based Curricula

Beyond the baseline programme, specific roles receive additional training aligned with their access and responsibilities:

**Developers (Execution Layer operators):**

| Topic | Content |
|-------|---------|
| Secure coding with AI assistance | Reviewing AI-generated code for vulnerabilities, injection flaws, insecure defaults |
| Agent security policy | OWASP LLM Top 10 threats, input validation, output sanitization |
| Secret management | No static credentials, using IdP tokens, secret scanning in CI/CD |
| Supply chain security | Dependency scanning, SBOM verification, signed commits |

**Operators (Orchestration Layer, Infrastructure):**

| Topic | Content |
|-------|---------|
| IdP administration | Identity lifecycle management, access reviews, privilege escalation detection |
| Observability security | Securing telemetry data, preventing log injection, protecting dashboards |
| Incident response | SEV1-4 procedures, escalation paths, evidence preservation |
| Agent fleet security | Monitoring agent behavior, detecting boundary violations, credential rotation |

**Executives and Steering Layer:**

| Topic | Content |
|-------|---------|
| Risk governance | Understanding risk appetite, KRI dashboards, accepting vs. mitigating risks |
| Regulatory landscape | AI regulations (EU AI Act, NIST AI RMF), compliance obligations |
| Business email compromise | Executive-targeted attacks, wire fraud, impersonation via AI deepfakes |
| Approval responsibilities | Understanding what they are approving in PRs, governance decisions, exception requests |

**Privileged Users (CODEOWNERS, IdP admins, infrastructure admins):**

| Topic | Content |
|-------|---------|
| Privileged access management | Just-in-time access, session recording, privilege escalation procedures |
| Insider threat awareness | Recognizing indicators of compromise in privileged accounts |
| Change management security | Verifying PR integrity, detecting unauthorized modifications, CODEOWNERS governance |
| Cryptographic key management | CA administration, certificate lifecycle, key ceremony procedures |

---

## 4. AI-Specific Security Awareness

The Agentic Enterprise model introduces security risks that traditional awareness programmes do not cover. This section details the AI-specific training that must supplement conventional cybersecurity awareness.

### 4a. Prompt Injection Risks

| Threat | Description | What Humans Must Do |
|--------|-------------|---------------------|
| **Direct prompt injection** | Attacker crafts input that overrides agent instructions | Review agent outputs for instruction-following anomalies; report suspicious behavior |
| **Indirect prompt injection** | Malicious content in data sources (documents, web pages) that agents process | Verify data source integrity before feeding to agents; monitor for unexpected agent actions |
| **Instruction hijacking** | Attempts to make agents ignore their AGENT.md rules | Audit agent actions against their defined boundaries; verify agents cite evidence (Rule 1) |
| **Context window poisoning** | Flooding agent context with misleading information to bias outputs | Review agent reasoning chains; cross-check agent claims against primary sources |

### 4b. Agent Boundary Violations

| Violation Type | Indicators | Human Response |
|---------------|------------|----------------|
| **Cross-layer action** | Strategy agent making code changes; execution agent modifying policy | Report as security incident; review agent instruction compliance |
| **Unauthorized tool use** | Agent calling unregistered integrations (Rule 8) | Block the integration; file a signal; review integration registry |
| **Self-authorization** | Agent approving its own work or bypassing governance exceptions | Reject the PR/artifact; escalate to Steering Layer |
| **Scope expansion** | Agent taking actions beyond its mission brief or fleet configuration | Review mission scope; restrict agent permissions if needed |

### 4c. Data Leakage Through AI Systems

| Leakage Vector | Risk | Mitigation Training |
|---------------|------|---------------------|
| **Sensitive data in prompts** | Classified data sent to external AI APIs | Train on data classification; verify data handling rules before providing data to agents |
| **Agent output contains secrets** | Agents may surface credentials, PII, or classified data in responses | Review agent outputs before publishing; use automated secret scanning |
| **Telemetry data exposure** | OTel spans may contain sensitive business data | Understand privacy defaults in OTel contract; review telemetry configurations |
| **Cross-tenant data mixing** | In multi-tenant deployments, agent context may leak between tenants | Verify tenant isolation; report any cross-tenant data in agent outputs |

### 4d. Over-Reliance on AI Recommendations

| Bias | Description | Countermeasure |
|------|-------------|----------------|
| **Automation bias** | Accepting agent recommendations without critical evaluation | Training on verification responsibility; "trust but verify" culture |
| **Authority bias** | Treating agent outputs as authoritative because they appear confident | Understanding that agents hallucinate; demanding evidence citations (Rule 1) |
| **Anchoring** | Over-weighting the first agent recommendation without exploring alternatives | Encouraging humans to ask for alternatives; independent verification of key decisions |
| **Diffusion of responsibility** | Assuming "the agent checked it" without personal verification | Clear accountability: human approver is responsible for outcomes of approved work |

---

## 5. Metrics and Evidence

### 5a. Programme Metrics

| Metric | Target | Measurement Method | Reporting Cadence |
|--------|--------|-------------------|-------------------|
| **Training completion rate** | ≥ 95% within 30 days of assignment | LMS completion records | Monthly |
| **Phishing simulation click rate** | ≤ 5% (industry benchmark: 10-15%) | Phishing platform reports | Monthly |
| **Phishing reporting rate** | ≥ 70% of simulations reported | Phishing platform reports | Monthly |
| **Knowledge assessment score** | ≥ 80% pass rate on post-training assessment | LMS assessment records | After each training module |
| **Time to complete onboarding training** | ≤ 5 business days from start date | LMS + HR system correlation | Monthly |
| **Repeat clicker rate** | ≤ 2% click on ≥ 2 consecutive simulations | Phishing platform reports | Quarterly |
| **AI-specific assessment score** | ≥ 80% on AI threat awareness modules | LMS assessment records | After each AI training module |
| **Event-triggered training deployment time** | ≤ 48 hours from incident to training assignment | LMS + incident system correlation | Per event |

### 5b. Evidence for Compliance

| Evidence Type | NIST CSF Link | Storage Location |
|--------------|---------------|-----------------|
| Programme charter and policy | PR.AT-01 | `org/4-quality/policies/` or policy management system |
| Training completion records (per person, per module) | PR.AT-01, PR.AT-02 | LMS export; retained per log retention policy |
| Phishing simulation results (aggregate, not individual shaming) | PR.AT-01 | Phishing platform; quarterly summary reports |
| Knowledge assessment scores | PR.AT-01, PR.AT-02 | LMS export |
| Role-based curriculum assignments | PR.AT-02 | LMS configuration; linked to HR role data |
| Programme review minutes (annual review) | PR.AT-01 | Meeting records; retained per log retention policy |
| Incident-triggered training records | PR.AT-01 | LMS + incident management system cross-reference |

---

## 6. Integration with Framework

### 6a. Agent Security Policy Alignment

The [Agent Security Policy](../../../org/4-quality/policies/agent-security.md) addresses OWASP LLM Top 10 threats at the agent instruction level. The human awareness programme complements this by training humans to:

| Agent Security Policy Area | Human Awareness Complement |
|---------------------------|---------------------------|
| Prompt injection defences (LLM01) | Humans recognize when agent outputs suggest injection; report anomalies |
| Insecure output handling (LLM02) | Humans review agent outputs before publishing or acting on them |
| Training data poisoning (LLM03) | Humans verify data source integrity; report suspicious data quality changes |
| Sensitive information disclosure (LLM06) | Humans check agent outputs for secrets/PII before sharing externally |
| Excessive agency (LLM08) | Humans monitor agent scope; enforce "stay in your lane" principle |
| Overreliance (LLM09) | Humans maintain critical evaluation; demand evidence; verify independently |

### 6b. Security Policy Alignment

The [Security Policy](../../../org/4-quality/policies/security.md) defines technical controls. The awareness programme trains humans to operate within these controls:

| Security Policy Requirement | Awareness Training Link |
|----------------------------|------------------------|
| mTLS for agent communication | Operators trained on certificate management and rotation |
| Short-lived tokens, no static credentials | All users trained on credential hygiene; developers on secret management |
| Shift-left security scanning | Developers trained on interpreting and acting on CI/CD security findings |
| Vulnerability disclosure | All users know how to report vulnerabilities; incident reporting channels |

### 6c. Governance Integration

| Framework Governance Mechanism | Awareness Programme Connection |
|-------------------------------|-------------------------------|
| PR-based approvals | Reviewers trained on what to look for (security implications, data classification, agent boundary compliance) |
| `CODEOWNERS` | Owners understand their approval authority carries security responsibility |
| Governance exceptions (`work/decisions/EXC-*`) | Approvers trained on exception risk assessment; time-bounded exceptions |
| Quality policies (Rule 4) | All personnel understand policies are mandatory, not advisory |
| Signal system (Rule 7) | All personnel trained to file security signals when they observe issues |

### 6d. CONFIG.yaml Integration

```yaml
# Add to CONFIG.yaml under integrations
integrations:
  security_awareness:
    type: training
    provider: "{{LMS_PROVIDER}}"  # knowbe4 | proofpoint | cofense | custom
    phishing_simulation:
      enabled: true
      frequency: monthly
      provider: "{{PHISHING_PROVIDER}}"
    training_cadence:
      baseline: annual
      micro_learning: quarterly
      phishing_simulation: monthly
      privileged_user: semi-annual
    completion_target: 95
    assessment_pass_threshold: 80
```

---

## 7. Verification Checklist

### Programme Establishment
- [ ] Security awareness programme charter documented with scope, roles, and objectives
- [ ] Programme owner assigned (human — not an agent)
- [ ] Budget allocated for LMS platform, phishing simulation tool, and content development
- [ ] Training content developed or procured for all core topics (Section 3a)
- [ ] AI-specific training modules developed covering prompt injection, boundary violations, data leakage, and over-reliance (Section 4)
- [ ] Role-based curricula defined for developers, operators, executives, and privileged users (Section 3c)

### Delivery Infrastructure
- [ ] Learning management system (LMS) deployed and configured
- [ ] LMS integrated with IdP for SSO and automated role assignment
- [ ] Phishing simulation platform deployed and configured
- [ ] Email templates for phishing simulations reviewed and approved (not too easy, not too cruel)
- [ ] Onboarding workflow includes mandatory security training before framework access is granted
- [ ] Event-triggered training workflow documented (incident → training assignment within 48 hours)

### Content and Curriculum
- [ ] Annual baseline training covers all core topics and AI-specific topics
- [ ] Quarterly micro-learning modules scheduled for the next 12 months
- [ ] Phishing simulation campaign calendar defined (monthly, varied difficulty)
- [ ] Knowledge assessments created for each training module (≥ 80% pass threshold)
- [ ] Training content reviewed by security team and updated for current threat landscape
- [ ] AI-specific scenarios include framework-relevant examples (agent boundary violation, prompt injection in PR review)

### Metrics and Reporting
- [ ] LMS configured to track completion rates per person, per module
- [ ] Phishing simulation platform configured to track click rates and reporting rates
- [ ] Monthly metrics report automated (completion, click rate, reporting rate)
- [ ] Quarterly executive summary report defined (aggregate metrics, trend analysis, risk areas)
- [ ] Compliance evidence export configured for NIST CSF PR.AT-01 and PR.AT-02 audit support
- [ ] Annual programme review scheduled with documented improvement actions

### Compliance Integration
- [ ] Training records retained per [Log Retention Policy](../../../org/4-quality/policies/log-retention.md)
- [ ] Programme mapped to NIST CSF subcategories PR.AT-01 and PR.AT-02 with evidence cross-references
- [ ] Programme mapped to NIST SP 800-53 controls AT-1 through AT-4
- [ ] CONFIG.yaml updated with security awareness integration details
- [ ] Signal filed for any programme areas requiring attention identified during initial deployment
