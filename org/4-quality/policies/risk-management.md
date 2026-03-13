# Risk Management Policy

> **Applies to:** All organizational layers, agent types, missions, integrations, and operational processes
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team, Steering Layer
> **Version:** 1.1 | **Last updated:** 2026-03-13

---

## Principles

1. **Risk-aware by design** — Risk assessment is a design-time discipline, not a post-incident afterthought. Every mission, technical design, and agent deployment must identify and score risks before execution begins.
2. **Continuous, not periodic** — Risk posture is monitored in real-time via the observability platform. Static risk registers are insufficient — risks must be observable, measurable, and re-evaluated at defined triggers.
3. **Humans own risk decisions** — Agents identify, score, and monitor risks. Humans define risk appetite, accept residual risk, and authorize risk treatments. No agent may unilaterally accept risk above the defined tolerance.
4. **Proportional controls** — Control rigor scales with agent autonomy level and risk impact. Higher autonomy demands tighter tolerances, more frequent reassessment, and more granular observability.
5. **Traceable end-to-end** — Every risk has an owner, a score, a treatment, a residual assessment, and a link to the controls that mitigate it. The chain from risk → control → evidence must be auditable.

---

## 1. Regulatory & Standards Alignment

This policy is designed to satisfy the risk management requirements of the following frameworks:

| Standard | Requirement | How this policy addresses it |
|----------|-------------|------------------------------|
| **ISO 31000:2018** | Documented risk management process (Establish Context → Identify → Analyze → Evaluate → Treat → Monitor) | §3 defines the full process aligned to ISO 31000 |
| **ISO 27001:2022 §6.1** | Documented risk assessment methodology, risk acceptance criteria, risk owners | §3, §4 (risk register with mandatory owner field), §2 (risk appetite) |
| **SOC 2 CC3.1** | Risk identification with clear threat descriptions | §3.1 + §5 (AI-specific risk taxonomy) |
| **SOC 2 CC3.2** | Likelihood and impact scoring using documented methodology | §3.2 (5×5 matrix with AI-calibrated scales) |
| **SOC 2 CC3.3** | Fraud risk consideration | §5.5 (financial risks including unauthorized transactions) |
| **SOC 2 CC3.4** | Stakeholder involvement in risk assessment | §3.1 (cross-layer participation requirement) |
| **NIST RMF (SP 800-37)** | Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor | §7 (NIST RMF crosswalk) |
| **NIST AI RMF (AI 100-1)** | Govern, Map, Measure, Manage functions for AI risk | §6 (AI-specific controls mapped to NIST AI RMF functions) |
| **EU AI Act** | Risk classification, human oversight for high-risk AI | §6.1 (agent autonomy tiers), §6.3 (human override procedures) |

---

## 2. Risk Appetite

### 2.1 Organizational Risk Appetite Statement

Risk appetite is defined per risk dimension. Adopters must configure these thresholds in `CONFIG.yaml → risk_appetite` and review them at least annually (or after any significant incident).

| Risk Dimension | Appetite | Tolerance Threshold | Escalation |
|---------------|----------|---------------------|------------|
| **Safety / Human Impact** | Zero | No agent action may cause physical harm or safety-critical system failure | Immediate halt + Steering Layer notification |
| **Compliance / Regulatory** | Zero | No known regulatory violation may persist | Immediate remediation + legal notification |
| **Security** | Very Low | Prompt injection, data breach, unauthorized access: zero tolerance for unmitigated known vulnerabilities | Immediate remediation per `agent-security.md` |
| **Operational** | Low | Service disruption: maximum {{RISK_MAX_DOWNTIME_MINUTES}} minutes unplanned downtime per month | Escalate to mission sponsor when >50% of budget consumed |
| **Reputational** | Low | No agent-generated content published externally without human review | Escalate any public-facing content incident to Steering Layer |
| **Financial** | Moderate | No unauthorized transactions; cost overruns flagged at {{RISK_COST_OVERRUN_THRESHOLD}}% of mission budget | Escalate to mission sponsor at threshold |
| **Innovation / Experimentation** | Higher | Sandboxed environments may accept higher risk with documented rationale | Risk owner documents and accepts per §3.4 |

### 2.2 Agent Autonomy Tiers and Risk Tolerance

Risk tolerance tightens as agent autonomy increases:

| Tier | Description | Risk Tolerance | Required Controls |
|------|-------------|---------------|-------------------|
| **Tier 1 — Human-directed** | Agent drafts, human executes | Standard | Policy compliance, telemetry |
| **Tier 2 — Supervised autonomy** | Agent executes, human approves before external effect | Moderate | All Tier 1 + approval gates for high-impact actions |
| **Tier 3 — Monitored autonomy** | Agent executes autonomously, human monitors | Low | All Tier 2 + real-time anomaly detection, circuit breakers, kill switch |
| **Tier 4 — Full autonomy** | Agent executes without real-time human oversight | Very Low | All Tier 3 + formal risk assessment per mission, enhanced telemetry, automatic rollback |

---

## 3. Risk Assessment Methodology

The risk assessment process follows ISO 31000:2018 and is mandatory for all missions, agent deployments, and integration registrations.

### 3.1 Risk Identification

**Who participates:** Risk identification is cross-layer. The mission sponsor, executing agents, quality agents, and subject-matter humans all contribute. No single-perspective risk assessment is sufficient (SOC 2 CC3.4).

**How to identify risks:**
- [ ] Review the AI risk taxonomy (§5) — assess each category for applicability
- [ ] Consult the observability platform for production baselines and existing failure patterns
- [ ] Review prior incident retrospectives (`work/retrospectives/`) for recurring themes
- [ ] Assess third-party dependencies (model providers, external APIs, MCP servers)
- [ ] Consider cascade failure paths — how does a failure in this component propagate?
- [ ] Consider fraud and abuse scenarios (SOC 2 CC3.3) — could this system be exploited for unauthorized financial actions, data exfiltration, or agent impersonation?
- [ ] Document each risk with: description, threat source, affected assets, existing controls

### 3.2 Risk Analysis — Likelihood × Impact Scoring

Use a **5×5 matrix** with AI-calibrated scales.

#### Likelihood Scale

| Score | Label | AI Calibration |
|-------|-------|---------------|
| 1 | **Rare** | Requires sophisticated adversarial attack + multiple independent control failures |
| 2 | **Unlikely** | Known attack vector exists but strong mitigations are deployed and tested |
| 3 | **Possible** | Attack vector or failure mode exists; mitigations are partial or untested |
| 4 | **Likely** | Known vulnerability; exploits demonstrated in comparable systems |
| 5 | **Almost Certain** | Active exploitation observed in the wild; no effective mitigation deployed |

#### Impact Scale

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | **Negligible** | No customer impact, internal only, self-correcting within minutes |
| 2 | **Minor** | Limited customer impact, recoverable within 1 hour, no data exposure |
| 3 | **Moderate** | Customer-facing disruption, recoverable within hours, limited data exposure possible |
| 4 | **Major** | Significant disruption, data breach requiring notification, regulatory reporting triggered |
| 5 | **Critical** | Safety impact, systemic data breach, regulatory enforcement action, existential reputational damage |

#### Risk Score Calculation

**Risk Score = Likelihood × Impact** (range 1–25)

| Score Range | Rating | Required Action | Review Frequency |
|------------|--------|-----------------|------------------|
| 1–4 | **Low** | Accept or monitor; document rationale | Quarterly |
| 5–9 | **Medium** | Treat; assign risk owner; implement controls | Monthly |
| 10–15 | **High** | Treat urgently; escalate to Steering Layer; implement controls before proceeding | Weekly |
| 16–25 | **Critical** | Immediate action required; suspend affected operations until mitigated; Steering Layer notification | Daily until mitigated |

### 3.3 Risk Evaluation

- [ ] Score each identified risk using the 5×5 matrix
- [ ] Compare scores against risk appetite thresholds (§2)
- [ ] Risks scoring above appetite require treatment before the mission proceeds
- [ ] Risks at or below appetite may be accepted with documented rationale and risk owner sign-off
- [ ] Aggregate risk scores to assess overall mission risk profile

### 3.4 Risk Treatment

For each risk above the acceptance threshold, select a treatment strategy:

| Strategy | When to use | Documentation required |
|----------|-------------|----------------------|
| **Avoid** | Eliminate the risk by not performing the activity | Document what was descoped and why |
| **Mitigate** | Reduce likelihood or impact through controls | Document controls, expected residual risk, and verification method |
| **Transfer** | Shift risk to a third party (insurance, vendor SLA) | Document transfer mechanism and coverage scope |
| **Accept** | Consciously accept the risk (only within appetite) | Risk owner signs off; document rationale and monitoring plan |

**Residual risk:** After treatment, re-score the risk. The residual score is the risk that remains after controls are applied. Residual risk above appetite requires human acceptance (documented in the risk register).

---

## 4. Risk Register Requirements

Every organization maintains a risk register. Individual missions maintain mission-level risk entries that roll up to the organizational register.

### 4.1 Mandatory Fields

Each risk register entry must include:

| Field | Description | Required |
|-------|-------------|----------|
| **Risk ID** | Unique identifier (e.g., `RISK-2026-001`) | Yes |
| **Title** | Short descriptive name | Yes |
| **Category** | From the AI risk taxonomy (§5) | Yes |
| **Description** | What can go wrong, threat source, affected assets | Yes |
| **Risk Owner** | Named individual (not a team) — per ISO 27001 §6.1.2 | Yes |
| **Likelihood** | Score 1–5 with rationale | Yes |
| **Impact** | Score 1–5 with rationale | Yes |
| **Inherent Risk Score** | Likelihood × Impact before treatment | Yes |
| **Treatment Strategy** | Avoid / Mitigate / Transfer / Accept | Yes |
| **Controls** | Specific controls applied (link to policies, procedures) | Yes (if Mitigate) |
| **Residual Likelihood** | Score 1–5 after treatment | Yes |
| **Residual Impact** | Score 1–5 after treatment | Yes |
| **Residual Risk Score** | Residual Likelihood × Residual Impact | Yes |
| **Human Acceptance** | Sign-off by risk owner if residual risk accepted | Yes (if Accept) |
| **Review Date** | Next mandatory reassessment date | Yes |
| **Status** | `open` / `mitigated` / `accepted` / `closed` | Yes |
| **Related Mission(s)** | Link to mission brief or task | If applicable |
| **Last Updated** | Date of last assessment | Yes |

### 4.2 Risk Register Location

- **Git-files backend:** `work/decisions/RISK-YYYY-NNN-<description>.md` (use the risk register template `work/decisions/_TEMPLATE-risk-register.md`)
- **Issue backend:** Issues with `artifact:risk` label, structured body per template

### 4.3 Update Cadence and Reassessment Triggers

Risk registers must be reassessed:
- [ ] At the scheduled review date (based on risk rating per §3.2)
- [ ] When a new agent type is deployed
- [ ] When a new tool integration is registered
- [ ] When a security incident or near-miss occurs
- [ ] When the observability platform detects anomalous risk indicators (§8)
- [ ] When a significant architecture change is proposed
- [ ] When external threat landscape changes (new OWASP entries, CVEs, regulatory updates)
- [ ] At minimum annually for all registered risks

---

## 5. AI Risk Taxonomy

The following risk categories are canonical for agentic enterprise systems. Every organizational risk assessment must evaluate each category for applicability.

### 5.1 Operational Risks

| ID | Risk | Description |
|----|------|-------------|
| OP-1 | **Cascade failure** | Corrupted output from one agent propagates through the multi-agent system at machine speed |
| OP-2 | **Agent deadlock** | Multiple agents waiting on each other, blocking mission progress |
| OP-3 | **Resource exhaustion** | Runaway agent consuming excessive compute, API calls, or storage |
| OP-4 | **Incorrect automated decision** | Agent makes a decision outside its competence that causes operational harm |
| OP-5 | **Stale context** | Agent operates on outdated information, producing incorrect outputs |
| OP-6 | **Emergent behavior** | Unexpected behaviors arising from multi-agent interaction patterns not observed in isolation |

### 5.2 Security Risks

| ID | Risk | Description |
|----|------|-------------|
| SE-1 | **Prompt injection** | External content overrides agent instructions (direct or indirect) |
| SE-2 | **Tool misuse** | Agent uses tools beyond intended scope or is tricked into tool abuse |
| SE-3 | **Privilege escalation** | Agent obtains or exercises permissions beyond its declared scope |
| SE-4 | **Data exfiltration** | Sensitive information exposed through agent outputs or tool calls |
| SE-5 | **Supply chain compromise** | Compromised upstream model, tool, or dependency |
| SE-6 | **Memory/context poisoning** | Corrupting agent persistent memory to influence future decisions |
| SE-7 | **Inter-agent impersonation** | Agent-to-agent message tampering or unauthorized delegation |

### 5.3 Compliance Risks

| ID | Risk | Description |
|----|------|-------------|
| CO-1 | **Regulatory violation** | Agent action violates applicable law or regulation (GDPR, EU AI Act, sector-specific) |
| CO-2 | **Audit trail gap** | Agent action not recorded in telemetry, breaking traceability |
| CO-3 | **Data residency violation** | Data processed or stored outside permitted jurisdictions |
| CO-4 | **Missing human oversight** | High-risk decision made without required human approval |
| CO-5 | **Unlicensed data use** | Training data, retrieved content, or tool outputs used without proper licensing |

### 5.4 Reputational Risks

| ID | Risk | Description |
|----|------|-------------|
| RE-1 | **Hallucinated public content** | Agent generates and publishes fabricated claims, metrics, or sources |
| RE-2 | **Biased output** | Agent produces discriminatory or unfair outputs affecting customers or public perception |
| RE-3 | **Harmful content** | Agent generates offensive, dangerous, or legally problematic content |
| RE-4 | **Human trust exploitation** | Agent output manipulates human decision-makers through social engineering patterns |

### 5.5 Financial Risks

| ID | Risk | Description |
|----|------|-------------|
| FI-1 | **Unauthorized transaction** | Agent processes payment, modifies billing, or creates financial commitment without authorization |
| FI-2 | **Cost overrun** | Runaway agent activity causes uncontrolled cloud/API spend |
| FI-3 | **Liability from AI decision** | Incorrect AI-generated advice or action creates legal liability |
| FI-4 | **Fraud via agent** | Agent exploited to conduct fraudulent activity (SOC 2 CC3.3) |

---

## 6. AI-Specific Risk Controls

### 6.1 Agent Autonomy Tier Classification

Every agent type in the Agent Type Registry (`org/agents/`) must be classified into an autonomy tier (§2.2). The classification determines:
- Which risk tolerance thresholds apply
- Which mandatory controls must be in place
- What level of human oversight is required
- How frequently associated risks must be reassessed

### 6.2 Cascade Failure Prevention

- [ ] Multi-agent workflows must define circuit breakers — automatic halt when error rate exceeds threshold
- [ ] Cross-agent output validation — receiving agents must validate inputs from upstream agents
- [ ] Blast radius containment — failures in one division's agents must not propagate to other divisions
- [ ] Maximum chain depth — agent delegation chains must not exceed the configured maximum depth without human checkpoint

### 6.3 Human Override & Emergency Procedures

- [ ] Every agent deployment must have a documented kill switch procedure
- [ ] Kill switch must be executable by any authorized human within {{RISK_KILL_SWITCH_TARGET_SECONDS}} seconds
- [ ] Emergency halt must be observable in the telemetry platform (span event: `agent.emergency_halt`)
- [ ] Post-halt recovery procedure must be documented in the mission's technical design
- [ ] Kill switch procedures must be tested at least quarterly

### 6.4 Third-Party AI / Model Risk

- [ ] Upstream model providers must be assessed for: reliability, data handling, change notification, deprecation policy
- [ ] Model version pinning — agent deployments must pin to specific model versions; automatic upgrades require risk assessment
- [ ] Fallback procedures for model provider outage or degradation
- [ ] Monitor for model behavior drift via the observability platform (output quality metrics over time)

---

## 7. Framework Crosswalk

This table maps internal controls to external framework requirements, enabling compliance teams to trace coverage.

| Internal Control | ISO 31000 | NIST RMF (800-37) | NIST AI RMF | ISO 27001 | SOC 2 | EU AI Act |
|-----------------|-----------|-------------------|-------------|-----------|-------|-----------|
| Risk appetite definition (§2) | Clause 6.4 | Prepare | GOVERN 1.1, 1.2 | §6.1.2 | CC3.1 | Art. 9 |
| Risk identification (§3.1) | Clause 6.4.2 | Categorize | MAP 1.1, 1.5 | §6.1.2 | CC3.1, CC3.4 | Art. 9.2 |
| Risk scoring (§3.2) | Clause 6.4.3 | Categorize | MEASURE 1.1 | §6.1.2 | CC3.2 | Art. 9.2 |
| Risk treatment (§3.4) | Clause 6.4.5 | Select, Implement | MANAGE 1.1, 2.1 | §6.1.3 | CC3.1 | Art. 9.4 |
| Risk register (§4) | Clause 6.7 | Assess | GOVERN 1.5 | §6.1.2, §8.2 | CC3.1 | Art. 11 |
| Fraud risk (§5.5) | — | — | — | — | CC3.3 | — |
| Agent autonomy tiers (§6.1) | — | Categorize | GOVERN 1.3, MAP 3.1 | — | — | Art. 14 |
| Cascade failure prevention (§6.2) | — | — | MANAGE 2.3 | — | — | Art. 15 |
| Human override (§6.3) | — | — | GOVERN 1.4, MANAGE 4.1 | — | — | Art. 14.4 |
| Third-party model risk (§6.4) | Clause 6.4.2 | Prepare | MAP 5.1, MANAGE 3.1 | §A.15 | CC9.2 | Art. 28 |
| Continuous monitoring (§8) | Clause 6.6 | Monitor | MEASURE 2.1, 4.1 | §9.1 | CC4.1 | Art. 9.4 |
| Reassessment triggers (§4.3) | Clause 6.6 | Monitor | MEASURE 3.1 | §8.2 | CC3.1 | Art. 9.9 |

---

## 8. Risk Monitoring & Observability Integration

### 8.1 Key Risk Indicators (KRIs)

The following KRIs must be sourced from the observability platform and monitored continuously:

| KRI | Source | Threshold | Action when breached |
|-----|--------|-----------|---------------------|
| Prompt injection detection rate | `agent-security.md` telemetry | Any detected attempt | Log, investigate, update risk score |
| Unauthorized tool calls | `tool.execute` spans with undeclared tools | >0 | Immediate halt + investigation |
| Agent escalation frequency | `governance.decision` span events | >{{RISK_ESCALATION_RATE_THRESHOLD}}% of decisions | Review agent instructions and scope |
| Tool call failure rate | `tool.execute` spans with error | >{{RISK_TOOL_FAILURE_THRESHOLD}}% | Investigate tool integration health |
| Human override frequency | `governance.decision` where decision=`reject` | Trending upward over 4 weeks | Review agent quality and scope |
| Mission cycle time variance | Mission status transitions | >{{RISK_CYCLE_TIME_VARIANCE}}% deviation from baseline | Investigate bottlenecks |
| Hallucination/correction rate | Quality evaluation verdicts (FAIL on accuracy) | >{{RISK_HALLUCINATION_THRESHOLD}}% | Review agent instructions, model, context |

### 8.2 Automated Risk Signals

When a KRI breaches its threshold, the observability platform (or monitoring agent) files an automated signal:
- **Git-files backend:** `work/signals/YYYY-MM-DD-risk-<kri-name>.md` with `source: observability-platform`
- **Issue backend:** Issue with `artifact:signal` + `source:observability` labels

The Steering Layer's weekly sensing loop aggregates risk signals alongside other signals (AGENTS.md Rule 7).

### 8.3 Risk Telemetry Requirements

Risk-related events must produce OTel spans per `docs/OTEL-CONTRACT.md`:
- Risk assessment completion → span event `risk.assessment.complete` with attributes: `risk.id`, `risk.score`, `risk.rating`
- Risk treatment applied → span event `risk.treatment.applied` with attributes: `risk.id`, `risk.treatment.strategy`
- Risk threshold breach → span event `risk.threshold.breach` with attributes: `risk.kri`, `risk.threshold`, `risk.actual_value`
- Emergency halt → span event `agent.emergency_halt` with attributes: `risk.id`, `risk.reason`

---

## 9. Reporting & Review

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Risk register review | Per risk rating (§3.2) | Risk owners + Steering Layer | Updated scores, treatment status, new risks |
| Risk posture summary | Monthly | Steering Layer | Aggregate risk profile, KRI trends, top risks |
| Annual risk assessment | Annually | Executive team | Full reassessment of all registered risks, appetite review |
| Post-incident risk update | After every SEV1/SEV2 | Steering Layer + affected teams | Updated risk scores, new risks identified, control gaps |

---

## 10. Existing Quality Policy → Risk Control Mapping

This table maps the organization's existing quality policies to the risk categories they mitigate, providing the traceability chain required by ISO 27001 §6.1.3.

| Quality Policy | Risks Mitigated | Control Type |
|---------------|----------------|--------------|
| **[security.md](security.md)** | SE-1 through SE-7 (partial), CO-3 | Preventive |
| **[agent-security.md](agent-security.md)** | SE-1 through SE-7, OP-4, CO-4 | Preventive, Detective |
| **[cryptography.md](cryptography.md)** | SE-4, SE-5, SE-7, CO-3, FI-4 | Preventive |
| **[observability.md](observability.md)** | CO-2, OP-1 through OP-6 (detection) | Detective, Corrective |
| **[architecture.md](architecture.md)** | OP-1, OP-2, OP-6, SE-5 | Preventive |
| **[delivery.md](delivery.md)** | OP-1, OP-3, FI-2 | Preventive, Corrective |
| **[performance.md](performance.md)** | OP-3, OP-5, FI-2 | Preventive, Detective |
| **[experience.md](experience.md)** | RE-2, RE-3 | Preventive |
| **[content.md](content.md)** | RE-1, RE-2, RE-3, CO-5 | Preventive |
| **[customer.md](customer.md)** | RE-1, RE-4, FI-3 | Preventive |
| **This policy (risk-management.md)** | All categories — governance framework | Directive |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Risk appetite defined | Risk appetite statement configured with thresholds per dimension | No risk appetite defined or thresholds missing |
| Agent autonomy classified | All agent types classified into autonomy tiers with corresponding controls | Agent types deployed without tier classification |
| Mission risk assessment | Mission brief includes risk assessment with scored entries from the taxonomy | Mission launched without risk assessment |
| Risk register maintained | All identified risks registered with mandatory fields, assigned owner, and review date | Missing risks, unassigned owners, or expired review dates |
| Risk scoring methodology | 5×5 matrix applied with documented rationale for scores | Unscored risks or scores without rationale |
| Residual risk documented | Treatment applied risks have residual scores; acceptances have human sign-off | Residual risk not assessed after treatment |
| Reassessment compliance | Risks reassessed per schedule and at defined triggers | Overdue reassessments or missed trigger-based reviews |
| KRI monitoring active | Key risk indicators sourced from observability platform and monitored | KRIs defined but not connected to live telemetry |
| Cascade failure controls | Circuit breakers and blast radius containment documented and tested | No cascade prevention for multi-agent workflows |
| Kill switch tested | Emergency halt procedures documented, tested quarterly, executable within target time | No kill switch or untested procedures |
| Fraud risk assessed | Financial and abuse scenarios explicitly evaluated (SOC 2 CC3.3) | No fraud risk consideration in assessment |
| Framework crosswalk current | Controls mapped to applicable regulatory requirements | No traceability from controls to standards |

---

## Related Policies

- **[Agent Security Policy](agent-security.md)** — Prompt injection and tool abuse prevention controls (SE-1 through SE-7)
- **[Security Policy](security.md)** — Infrastructure and code security controls
- **[Observability Policy](observability.md)** — Telemetry requirements that enable risk monitoring (§8)
- **[Delivery Policy](delivery.md)** — Deployment risk controls (rollback, progressive rollout)
- **[Architecture Policy](architecture.md)** — Structural controls for cascade prevention

## References

- [ISO 31000:2018 — Risk Management Guidelines](https://www.iso.org/standard/65694.html)
- [NIST SP 800-37 Rev 2 — Risk Management Framework](https://csrc.nist.gov/pubs/sp/800/37/r2/final)
- [NIST AI 100-1 — AI Risk Management Framework](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [NIST AI 600-1 — Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [EU AI Act — Risk Classification](https://artificialintelligenceact.eu/high-level-summary/)
- [SOC 2 CC3 — Risk Assessment Criteria](https://www.isms.online/soc-2/controls/risk-assessment-cc3-2-explained/)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial version — risk appetite framework, 5×5 scoring methodology, AI risk taxonomy (22 canonical risks across 5 dimensions), agent autonomy tiers, observability-driven KRIs, regulatory crosswalk (ISO 31000 / NIST RMF / NIST AI RMF / ISO 27001 / SOC 2 / EU AI Act), policy-to-risk control mapping |
