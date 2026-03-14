# NIST Cybersecurity Framework (CSF) 2.0 — Compliance Reference

> **Standard:** NIST Cybersecurity Framework (CSF) 2.0
> **Scope:** Voluntary framework for managing and reducing cybersecurity risk, applicable to organizations of all sizes and sectors
> **Official source:** [NIST CSF 2.0](https://www.nist.gov/cyberframework)

## 1. What NIST CSF 2.0 Requires

NIST CSF 2.0, released in February 2024, replaces CSF 1.1 and organizes cybersecurity outcomes around **6 core functions**, each containing categories and subcategories:

**GOVERN (GV)** — Establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy:
- Organizational context (GV.OC)
- Risk management strategy (GV.RM)
- Roles, responsibilities, and authorities (GV.RR)
- Policy (GV.PO)
- Oversight (GV.OV)
- Cybersecurity supply chain risk management (GV.SC)

**IDENTIFY (ID)** — Understand the organization's current cybersecurity risks:
- Asset management (ID.AM)
- Risk assessment (ID.RA)
- Improvement (ID.IM)

**PROTECT (PR)** — Use safeguards to manage cybersecurity risks:
- Identity management, authentication, and access control (PR.AA)
- Awareness and training (PR.AT)
- Data security (PR.DS)
- Platform security (PR.PS)
- Technology infrastructure resilience (PR.IR)

**DETECT (DE)** — Find and analyze possible cybersecurity attacks and compromises:
- Continuous monitoring (DE.CM)
- Adverse event analysis (DE.AE)

**RESPOND (RS)** — Take action regarding a detected cybersecurity incident:
- Incident management (RS.MA)
- Incident analysis (RS.AN)
- Incident response reporting and communication (RS.CO)
- Incident mitigation (RS.MI)

**RECOVER (RC)** — Restore assets and operations affected by a cybersecurity incident:
- Incident recovery plan execution (RC.RP)
- Incident recovery communication (RC.CO)

## 2. How This Framework Addresses It

### GOVERN Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| GV.OC-01 | Organizational context is understood | `COMPANY.md` (vision/mission/beliefs), `CONFIG.yaml` (org identity, stakeholders) | Git history |
| GV.OC-02 | Internal and external stakeholders are understood | 5-layer model (`org/README.md`), division structure, `CODEOWNERS` | PR review assignments |
| GV.OC-03 | Legal, regulatory requirements understood | Compliance reference docs (`docs/compliance/`), quality policies | Compliance mapping artifacts |
| GV.OC-04 | Critical objectives, capabilities understood | Venture charters (`org/1-strategy/ventures/`), mission briefs | Mission artifacts |
| GV.OC-05 | Outcomes used to inform risk management | Signals → missions cycle, retrospectives, risk register | `work/signals/`, `work/retrospectives/` |
| GV.RM-01 | Risk management objectives established | [Risk Management Policy](../../org/4-quality/policies/risk-management.md) — ISO 31000-aligned methodology | Policy version history |
| GV.RM-02 | Risk appetite and tolerance established | Risk management policy — risk appetite definitions, KRI thresholds | Risk register artifacts, KRI dashboards |
| GV.RM-03 | Risk activities integrated into enterprise risk | Risk register linked to mission execution, quality gates | OTel `risk.assessment.complete` events |
| GV.RM-04 | Strategic direction informs risk decisions | Steering Layer evolution cycle, strategy → orchestration flow | Evolution records, mission briefs |
| GV.RM-05 | Supply chain risks managed | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — 4-tier model | Vendor assessment records, SLA dashboards |
| GV.RM-06 | Risk management effectiveness assessed | Quality evaluations, observability platform metrics | Eval reports, OTel telemetry |
| GV.RM-07 | Strategic opportunities from risk management | Signals system surfaces improvement opportunities from risk assessments | `work/signals/` |
| GV.RR-01 | Organizational leadership accountable | Steering Layer with executive authority, `CODEOWNERS` as RACI | PR approvals |
| GV.RR-02 | Roles and responsibilities established | Layer-specific `AGENT.md` instructions, division `DIVISION.md` files | Agent instruction version history |
| GV.RR-03 | Resources adequate for cybersecurity | Fleet configs (`org/2-orchestration/fleet-configs/`), resource allocation in missions | Mission resource artifacts |
| GV.RR-04 | Cybersecurity in human resource practices | Agent competence requirements in `AGENT.md`, agent type registry (`org/agents/`) | Agent type definitions |
| GV.PO-01 | Cybersecurity policy established | 19 quality policies in `org/4-quality/policies/`, "Policies are law" (AGENTS.md Rule 4) | Policy Git history, CI validation |
| GV.PO-02 | Policy reviewed and updated | Version control on all policies (Rule 10), changelog requirements | Git diff history, version fields |
| GV.OV-01 | Cybersecurity risk management overseen | Quality Layer evaluations, steering oversight, PR governance | Eval reports, PR history |
| GV.OV-02 | Risk management performance reviewed | Observability dashboards, quality metrics, retrospectives | OTel dashboards, retrospective records |
| GV.OV-03 | Adjustments made based on review | Signals → steering → evolution cycle, policy updates | Evolution records, policy PRs |
| GV.SC-01 | Supply chain risk management program | [Vendor Risk Management Policy](../../org/4-quality/policies/vendor-risk-management.md) — lifecycle from onboarding to offboarding | Vendor registry, assessment records |
| GV.SC-02 | Supply chain cybersecurity roles defined | Vendor risk tiers with per-tier requirements, review cadences | Tier classification records |
| GV.SC-03–SC-10 | Supply chain due diligence, contracts, monitoring | Vendor assessment methodology, SLA monitoring, incident notification requirements | Vendor SLA dashboards, assessment artifacts |

### IDENTIFY Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| ID.AM-01 | Hardware assets inventoried | Asset registry (`work/assets/`) with asset type classification | Asset registry entries |
| ID.AM-02 | Software assets inventoried | Asset registry, `CONFIG.yaml` integrations list, dependency tracking | Asset registry, integration registry |
| ID.AM-03 | Data assets mapped | [Data Classification Policy](../../org/4-quality/policies/data-classification.md) — 4-level scheme | `data.classification` span attributes |
| ID.AM-04 | External information systems catalogued | Integration registry (`org/integrations/`), vendor risk assessments | Integration definitions, vendor records |
| ID.AM-05 | Assets prioritized by criticality | Availability tiers (Tier 1–4 in availability policy), data classification levels | Tier assignments, classification labels |
| ID.AM-07 | Resource classification and management | [Data Classification Policy](../../org/4-quality/policies/data-classification.md), asset registry taxonomy | Classification metadata |
| ID.AM-08 | Systems, services mapped | Integration registry with dependency mapping, `CONFIG.yaml` | Integration topology |
| ID.RA-01 | Vulnerabilities identified | [Security Policy](../../org/4-quality/policies/security.md) — shift-left scanning, CI/CD security gates | CI/CD scan results, vulnerability OTel spans |
| ID.RA-02 | Threat intelligence received | Signals system (`work/signals/`), observability anomaly detection | Automated signals from observability platform |
| ID.RA-03 | Threats assessed | [Agent Security Policy](../../org/4-quality/policies/agent-security.md) — OWASP LLM Top 10 threat model | Threat model artifacts |
| ID.RA-04 | Potential impacts assessed | Risk management policy — impact/likelihood matrix, risk register | Risk register entries |
| ID.RA-05 | Risks prioritized | Risk register with scoring methodology, KRI thresholds | Risk dashboards |
| ID.RA-06 | Risk responses selected | Risk treatment in mission briefs, governance decisions (`work/decisions/`) | Decision records |
| ID.RA-07 | Changes and exceptions managed | Governance exception process (`work/decisions/EXC-*`), change via PRs | Exception records, PR history |
| ID.IM-01 | Improvements identified | Signals system (AGENTS.md Rule 7), retrospective action items | `work/signals/`, retrospective records |
| ID.IM-02 | Improvements prioritized and tracked | Steering Layer triage, mission prioritization | Signal triage records, mission STATUS.md |
| ID.IM-03 | Improvements implemented | Missions → execution → quality gate cycle | Mission completion evidence |

### PROTECT Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| PR.AA-01 | Identities managed | Agent identity via `CODEOWNERS`, bot accounts, layer assignments | CODEOWNERS file, agent configurations |
| PR.AA-02 | Identities correlated | Activity telemetry links `agent.id` to all spans (OTel contract) | `agent.id` span attributes |
| PR.AA-03 | Authentication mechanisms | [Security Policy](../../org/4-quality/policies/security.md) — mTLS, short-lived tokens, no static credentials | Authentication OTel spans |
| PR.AA-04 | Access permissions managed | `CODEOWNERS` as access matrix, least-privilege agent tooling, PR approval gates | `tool.execute` spans with access verification |
| PR.AA-05 | Access policies enforced | PR merge requirements, CI checks, policy-as-code validation | CI pipeline results |
| PR.AA-06 | Physical access managed | Out of scope (framework-level, not physical infrastructure) | — |
| PR.AT-01 | Awareness and training provided | Agent instructions (`AGENT.md` hierarchy), "read before starting" rule (AGENTS.md) | Instruction version history |
| PR.AT-02 | Privileged users trained | Steering/quality layer agent instructions with elevated governance requirements | Layer-specific AGENT.md |
| PR.DS-01 | Data-at-rest protected | [Cryptography Policy](../../org/4-quality/policies/cryptography.md) — AES-256 encryption requirements | KMS audit logs |
| PR.DS-02 | Data-in-transit protected | Cryptography policy — TLS 1.3, mTLS for agent-to-agent | Certificate monitoring, TLS OTel spans |
| PR.DS-10 | Data-in-use protected | Agent security policy — prompt injection defences, output validation | Agent execution OTel spans |
| PR.DS-11 | Data backups performed | [Availability Policy](../../org/4-quality/policies/availability.md) — tiered RPO targets | Backup verification dashboards |
| PR.PS-01 | Configuration management | `CONFIG.yaml` version-controlled, Git as single source of truth | Git history |
| PR.PS-02 | Software maintained | Dependency management, CI/CD pipeline security scanning | CI pipeline OTel spans |
| PR.PS-03 | Hardware maintained | Out of scope (framework-level, not hardware management) | — |
| PR.PS-04 | Log records generated | [Observability Policy](../../org/4-quality/policies/observability.md) — every agent action produces a span | Full OTel telemetry pipeline |
| PR.PS-05 | Installation and execution policies enforced | Agent security policy — tool allowlisting, sandbox boundaries | `tool.execute` spans |
| PR.PS-06 | Secure software development practices | Security policy — shift-left, OWASP LLM Top 10, CI/CD security gates | CI/CD scan results, code review PRs |
| PR.IR-01 | Networks protected | Security policy — network segmentation requirements, mTLS | Network monitoring dashboards |
| PR.IR-02 | Technology resilience | Availability policy — tiered SLOs, redundancy, geographic distribution | Availability dashboards, SLO tracking |

### DETECT Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| DE.CM-01 | Networks monitored | [Observability Policy](../../org/4-quality/policies/observability.md) — continuous monitoring requirements | OTel network spans, anomaly alerts |
| DE.CM-02 | Physical environment monitored | Out of scope (framework-level) | — |
| DE.CM-03 | Personnel activity monitored | All agent actions produce OTel spans (Rule 9a — "agents do not self-censor telemetry") | Full agent telemetry |
| DE.CM-06 | External service provider activity monitored | Vendor SLA monitoring, integration telemetry | Vendor SLA dashboards, `tool.execute` spans |
| DE.CM-09 | Computing hardware and software monitored | Observability platform with anomaly detection, [OTel contract](../otel-contract.md) | OTel dashboards, automated alerts |
| DE.AE-01 | Baseline of expected activity established | Observability baselines, SLO targets, KRI thresholds | Baseline dashboards |
| DE.AE-02 | Anomalies detected and analysed | Observability anomaly detection → automated signals, `risk.threshold.breach` events | Automated `work/signals/` entries |
| DE.AE-03 | Events correlated from multiple sources | OTel distributed tracing with trace propagation across agents | Correlated trace views |
| DE.AE-04 | Impact of events estimated | Incident severity classification (SEV1–4), risk impact matrix | Incident timeline spans |
| DE.AE-06 | Information shared on events | Incident communication requirements, stakeholder notification | Incident OTel spans, notification records |
| DE.AE-07 | Cyber threat intelligence integrated | Signals from observability anomaly detection, external threat feeds via integrations | Signal records with `source: observability-platform` |
| DE.AE-08 | Incidents declared when warranted | [Incident Response Policy](../../org/4-quality/policies/incident-response.md) — severity-based declaration criteria | Incident declaration OTel events |

### RESPOND Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| RS.MA-01 | Incident response plan executed | [Incident Response Policy](../../org/4-quality/policies/incident-response.md) — structured response with SEV1-4 targets | Incident timeline OTel spans |
| RS.MA-02 | Incident reports completed | Retrospectives (`work/retrospectives/`), postmortem templates | Retrospective records |
| RS.MA-03 | Incidents tracked and documented | Incident artifacts with full timeline, OTel spans for all response actions | Incident trace data, retrospective records |
| RS.MA-04 | Incidents escalated as needed | Auto-escalation rules (SEV1: 15 min, SEV2: 30 min), stakeholder matrix | Escalation OTel events, `governance.decision` spans |
| RS.MA-05 | Criteria for incident closure defined | Incident response policy — resolution verification, retrospective completion | Incident close events |
| RS.AN-01 | Investigations performed | Incident response policy — root cause analysis requirement | RCA artifacts |
| RS.AN-03 | Analysis performed to determine actions | Retrospective action items, corrective action tracking | Retrospective records |
| RS.AN-06 | Actions are performed to contain | Incident mitigation steps in response plan, rollback procedures | Mitigation OTel spans |
| RS.AN-07 | Log integrity ensured | [Log Retention Policy](../../org/4-quality/policies/log-retention.md) — WORM storage, hash chain validation | WORM verification alerts, hash chain logs |
| RS.AN-08 | Incident magnitude estimated | SEV1-4 classification with defined impact criteria | Severity assignment records |
| RS.CO-02 | Internal stakeholders notified | Incident response policy — stakeholder notification matrix, escalation paths | Notification OTel events |
| RS.CO-03 | Information shared with stakeholders | Incident communication plan, status updates | Communication records |
| RS.MI-01 | Incidents contained | Incident response policy — containment actions by severity | Containment OTel spans |
| RS.MI-02 | Incidents eradicated | Root cause elimination, corrective actions from retrospectives | Action item tracking |

### RECOVER Function Mapping

| Category | Subcategory | Framework Implementation | Evidence Source |
|----------|-------------|-------------------------|-----------------|
| RC.RP-01 | Recovery plan executed | [Availability Policy](../../org/4-quality/policies/availability.md) — tiered RTO/RPO targets, DR procedures | Recovery timeline OTel spans |
| RC.RP-02 | Recovery actions selected and performed | Availability policy — failover procedures, backup restoration | Recovery action dashboards |
| RC.RP-03 | Recovery verified | Availability policy — DR drill requirements, recovery validation | Drill evidence, recovery verification records |
| RC.RP-04 | Critical functions restored | Tiered recovery (Tier 1 first: RTO ≤ 1h), service restoration order | Service restoration dashboards |
| RC.RP-05 | Service restoration communicated | Incident communication plan, stakeholder notification on recovery | Recovery notification records |
| RC.CO-03 | Recovery activities communicated | Incident response + availability policies — post-incident communication | Retrospective records, status pages |
| RC.CO-04 | Public updates on recovery shared | Communication plan for external stakeholders | External communication records |

## 3. Where Observability Provides Evidence

NIST CSF 2.0 emphasizes continuous improvement and measurable outcomes. The observability platform provides the evidence backbone:

| CSF Function | Evidence Need | Observability Source |
|-------------|---------------|---------------------|
| GOVERN | Policy enforcement effectiveness | Policy compliance dashboards, `governance.decision` span events |
| GOVERN | Supply chain risk monitoring | Vendor SLA dashboards, integration telemetry |
| IDENTIFY | Asset inventory accuracy | Asset registry cross-referenced with `tool.execute` spans |
| IDENTIFY | Risk posture awareness | KRI dashboards, `risk.threshold.breach` events |
| PROTECT | Access control enforcement | `tool.execute` spans with least-privilege verification |
| PROTECT | Cryptographic control operation | KMS audit trail, certificate expiry alerts, TLS handshake spans |
| PROTECT | Secure development evidence | CI/CD pipeline traces, security scan result spans |
| DETECT | Continuous monitoring coverage | OTel span coverage metrics, dead-letter monitoring |
| DETECT | Anomaly detection effectiveness | Alert-to-signal conversion rate, detection latency metrics |
| DETECT | Event correlation | Distributed trace views linking agent actions across layers |
| RESPOND | Incident response timeliness | Incident timeline spans: detect → acknowledge → contain → resolve |
| RESPOND | Escalation effectiveness | Escalation OTel events with timing relative to SLA targets |
| RESPOND | Log integrity for forensics | WORM storage verification, hash chain validation |
| RECOVER | Recovery time measurement | Recovery OTel spans with RTO/RPO compliance metrics |
| RECOVER | DR drill validation | Drill execution traces, recovery success/failure records |

## 4. Remaining Gaps

| Gap | CSF Requirement | What's Needed | Criticality |
|-----|----------------|---------------|-------------|
| **Runtime security tooling** | PR.PS-02, DE.CM-01 | Deployment must configure actual SIEM, IDS/IPS, EDR, and vulnerability scanners — the framework defines requirements but not runtime tooling | Critical — detection/protection depends on tooling |
| **Network security implementation** | PR.IR-01, DE.CM-01 | Deployment must implement actual network segmentation, firewall rules, and monitoring infrastructure | Critical — protection requires runtime configuration |
| **Identity provider integration** | PR.AA-01, PR.AA-03 | Deployment must connect to an actual IdP (e.g., Okta, Azure AD) for human and service identity lifecycle | High — framework defines policy but not IdP configuration |
| **Security awareness programme** | PR.AT-01, PR.AT-02 | Formal human security awareness training beyond agent instructions; phishing simulations, role-based training | High — agent instructions are not a human training programme |
| **Physical security** | PR.AA-06, DE.CM-02, A.7.x controls | Out of scope for a software framework — deployment-specific based on hosting model | Medium — depends on deployment model (cloud vs. on-premise) |
| **External threat intelligence feeds** | DE.AE-07, ID.RA-02 | Deployment must subscribe to and integrate actual CTI feeds (STIX/TAXII, ISACs) | Medium — framework supports signal ingestion but needs actual feeds |
| **Formal risk quantification** | GV.RM-02, ID.RA-04 | Deployment should implement quantitative risk methods (FAIR, Monte Carlo) beyond the qualitative matrix provided | Medium — qualitative method in policy, quantitative is deployment choice |
| **Regulatory notification procedures** | RS.CO-03, RC.CO-04 | Deployment must define jurisdiction-specific breach notification timelines and contacts | Medium — varies by regulatory environment |
| **Backup and DR infrastructure** | RC.RP-01, RC.RP-02 | Deployment must provision actual backup infrastructure, replication, and failover targets matching tiered RTO/RPO | Medium — framework defines targets, deployment implements them |
| **Penetration testing programme** | ID.RA-01, PR.PS-06 | Regular external penetration testing and red team exercises | Low — framework defines shift-left security, pen testing is operational |
| **Cyber insurance** | GV.RM-07 | Organization-level decision on cyber insurance coverage | Low — business decision outside framework scope |

## 5. External References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework) — The framework itself (free)
- [NIST CSF 2.0 Reference Tool](https://csrc.nist.gov/projects/cybersecurity-framework/filters#/csf/filters) — Interactive subcategory browser
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Detailed security controls (CSF informative references)
- [NIST CSF 2.0 Quick Start Guides](https://www.nist.gov/cyberframework/getting-started) — Implementation guidance by audience
- [NIST CSF 1.1 to 2.0 Transition](https://www.nist.gov/cyberframework) — Changes and migration guidance
- [ISO 27001 to NIST CSF Mapping](https://www.nist.gov/cyberframework/informative-references) — Cross-framework reference
