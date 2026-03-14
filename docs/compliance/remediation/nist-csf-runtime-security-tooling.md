<!-- placeholder-ok -->
# NIST CSF 2.0 — Runtime Security Tooling Integration Guide

> **Closes gap:** Runtime security tooling (SIEM, IDS/IPS, EDR)
> **Standard:** NIST CSF 2.0 — PR.PS-02, DE.CM-01
> **Severity:** Critical — detection and protection depend on deployed tooling
> **Related issue:** [#133](https://github.com/wlfghdr/agentic-enterprise/issues/133)
> **Related compliance doc:** [NIST CSF Compliance Reference](../nist-csf.md)

---

## 1. Gap Summary

The Agentic Enterprise framework provides the **governance and policy layer** for cybersecurity — quality policies define what must be monitored, how incidents must be handled, and what telemetry agents must emit. However, the framework does not provision or deploy the **runtime security tooling** that actually performs detection and protection in a live environment.

Specifically:

- The [Security Policy](../../../org/4-quality/policies/security.md) mandates shift-left scanning, dependency vulnerability management, and mTLS — but does not deploy a SIEM to aggregate and correlate security events.
- The [Observability Policy](../../../org/4-quality/policies/observability.md) requires every agent action to produce an OTel span — but the telemetry pipeline terminates at the OTel Collector; no security analytics platform consumes the data for threat detection.
- The [Incident Response Policy](../../../org/4-quality/policies/incident-response.md) defines SEV1-SEV4 severity levels and response SLAs — but assumes a detection path exists (Section "How Compliance Is Ensured") without specifying the tooling that provides it.

**Without deployed SIEM, IDS/IPS, and EDR, the framework's detection (DE.CM-01) and platform security (PR.PS-02) controls exist only on paper.**

This guide provides the requirements, architecture, and configuration guidance for closing this gap.

---

## 2. Minimum Security Tooling Requirements

### By Deployment Tier

| Tier | Description | Required Tooling |
|------|-------------|-----------------|
| **Tier 1 — Development / POC** | Non-production, no sensitive data | Basic log aggregation (e.g., ELK stack or CloudWatch Logs), OS-level endpoint protection (built-in AV/EDR), dependency scanning in CI |
| **Tier 2 — Staging / Internal** | Internal use, limited sensitive data | SIEM with log correlation and basic alerting, host-based IDS on agent workload hosts, EDR on all endpoints, vulnerability scanner on schedule |
| **Tier 3 — Production** | Customer data, regulated workloads | Full SIEM with correlation rules and automated response playbooks, network IDS/IPS at zone boundaries, EDR fleet-wide with centralized management, vulnerability scanner (scheduled + CI/CD integrated), WAF on all external-facing services |

Deployment tier should be determined by the data classification level (per the [Data Classification Policy](../../../org/4-quality/policies/data-classification.md)) of the highest-sensitivity data processed by the agent fleet.

### Tooling Categories

#### SIEM (Security Information and Event Management)

**Purpose:** Centralized collection, correlation, and analysis of security events from all sources — agent telemetry, infrastructure logs, network flows, authentication events, and application logs.

**NIST CSF mapping:** DE.CM-01 (continuous monitoring), DE.AE-02 (adverse event analysis), DE.AE-03 (event correlation from multiple sources)

**Example products:**
- **Open-source:** Elastic SIEM (ELK + Security), Wazuh (SIEM + HIDS), Apache Metron
- **Commercial:** Splunk Enterprise Security, Microsoft Sentinel, Google Chronicle SOAR

**Key requirements for this framework:**
- Must ingest OTel-formatted logs and traces (OTLP or via Collector export)
- Must support correlation rules mapping `agent.id`, `agent.layer`, and `governance.decision` span attributes
- Must integrate with the incident response workflow for alert-to-incident escalation

---

#### IDS/IPS (Intrusion Detection / Prevention System)

**Purpose:** Monitor network traffic for known attack signatures and anomalous patterns. IDS alerts on threats; IPS actively blocks them.

**NIST CSF mapping:** PR.PS-02 (software and platform security maintenance), DE.CM-01 (network monitoring)

**Example products:**
- **Open-source:** Suricata (IDS/IPS with NSM capabilities), Snort (signature-based IDS/IPS), Zeek (network analysis framework)
- **Commercial:** Palo Alto Threat Prevention, Cisco Secure IPS, CrowdStrike Falcon Network

**Key requirements for this framework:**
- Deploy at zone boundaries (see network segmentation in [Network Security Guide](nist-csf-network-security.md))
- Monitor east-west traffic between agent execution zones and data zones
- Export alerts to SIEM for correlation with agent telemetry
- IPS mode required at Tier 3 for external-facing zone boundaries

---

#### EDR (Endpoint Detection and Response)

**Purpose:** Continuous monitoring of endpoints (servers, containers, workstations) for malicious activity, with automated investigation and response capabilities.

**NIST CSF mapping:** DE.CM-01 (endpoint monitoring), RS.MA-01 (incident response execution), DE.CM-09 (computing hardware/software monitored)

**Example products:**
- **Open-source:** Wazuh (HIDS + EDR capabilities), OSSEC, Velociraptor
- **Commercial:** CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne Singularity

**Key requirements for this framework:**
- Installed on all hosts running agent workloads (containers, VMs, bare metal)
- Covers the agent execution zone, orchestration zone, and management zone
- Exports telemetry to SIEM for cross-correlation
- Supports automated containment actions for SEV1 threats (isolation, process termination)

---

#### Vulnerability Scanner

**Purpose:** Identify known vulnerabilities in operating systems, applications, container images, dependencies, and infrastructure configurations.

**NIST CSF mapping:** ID.RA-01 (vulnerabilities identified), PR.PS-06 (secure development practices)

**Example products:**
- **Open-source:** Trivy (containers, filesystems, Git repos), Grype (container images), OpenVAS (network scanning)
- **Commercial:** Nessus (network + host scanning), Qualys VMDR, Snyk (developer-focused, code + containers)

**Key requirements for this framework:**
- Integrated into CI/CD pipeline (shift-left, per [Security Policy](../../../org/4-quality/policies/security.md))
- Scheduled scans of production infrastructure (weekly minimum for Tier 3)
- Results feed into SIEM for trending and risk scoring
- Critical/high findings block deployment (enforced by quality gates)

---

#### WAF (Web Application Firewall)

**Purpose:** Inspect and filter HTTP/HTTPS traffic to web applications, blocking common attack patterns (OWASP Top 10, bot traffic, API abuse).

**NIST CSF mapping:** PR.PS-02 (platform security), PR.IR-01 (network protection)

**Example products:**
- **Open-source:** ModSecurity (with OWASP Core Rule Set), Coraza WAF
- **Commercial:** AWS WAF, Cloudflare WAF, Azure Front Door WAF

**Key requirements for this framework:**
- Required at Tier 3 for all external-facing API endpoints
- OWASP Core Rule Set as baseline, with custom rules for agent-specific patterns
- Bot detection and rate limiting for public-facing agent APIs
- WAF logs exported to SIEM

---

## 3. OTel Integration with Security Tooling

The framework's OpenTelemetry pipeline is the natural integration point between agent telemetry and security tooling. The [OTel contract](../../otel-contract.md) defines the canonical span attributes and resource attributes that security tooling can correlate on.

### Architecture

```
Agent Workloads
     │
     ▼
OTel SDK (traces, logs, metrics)
     │
     ▼
OTel Collector (central aggregation)
     ├──────────────────────┐
     ▼                      ▼
Observability Platform     SIEM
(dashboards, SLOs)    (security correlation)
                            │
                ┌───────────┼───────────┐
                ▼           ▼           ▼
           IDS/IPS        EDR      Vuln Scanner
           alerts        alerts      findings
```

### How It Works

1. **OTel Collector as central aggregation point:** All agent telemetry flows through the OTel Collector, which is already required by the [Observability Policy](../../../org/4-quality/policies/observability.md). The Collector exports to the observability platform for operational monitoring and to the SIEM for security analysis — using separate exporters in the Collector pipeline.

2. **SIEM ingests OTel traces and logs via OTLP or syslog:** Configure the OTel Collector with a secondary exporter targeting the SIEM endpoint. For SIEM platforms that support OTLP natively (e.g., Elastic), use the OTLP exporter directly. For platforms requiring syslog (e.g., legacy Splunk), use the syslog exporter with appropriate attribute mapping.

3. **Correlation between agent telemetry and security events:** The SIEM correlates agent activity spans (carrying `agent.id`, `agent.layer`, `agent.type`, `mission.id`) with security events from IDS/IPS, EDR, and vulnerability scanners. This enables questions like:
   - "Which agent was active when the IDS alert fired?"
   - "Did this agent access any tools outside its declared permission set before the EDR detection?"
   - "Are vulnerability findings correlated with specific agent fleet deployments?"

4. **Alert routing — security tool alerts to incident response workflow:** When the SIEM generates a correlated alert, it routes to the incident response workflow defined in the [Incident Response Policy](../../../org/4-quality/policies/incident-response.md). The severity mapping (Section 4 below) determines the response SLA and escalation path.

### CONFIG.yaml Integration Entries

Add the following to the `integrations` section of `CONFIG.yaml`:

```yaml
integrations:
  siem:
    status: active
    category: observability
    provider: "{{SIEM_PROVIDER}}"   # e.g., "elastic", "splunk", "sentinel"
    connection:
      protocol: OTLP/syslog
      endpoint: "https://{{SIEM_ENDPOINT}}"
    capabilities: [log-aggregation, correlation, alerting, threat-detection]
    data_flow: inbound       # OTel Collector → SIEM
    side_effect_level: none  # read-only analysis
    approval_mode: auto
  edr:
    status: active
    category: observability
    provider: "{{EDR_PROVIDER}}"   # e.g., "crowdstrike", "defender", "wazuh"
    connection:
      protocol: API
      endpoint: "https://{{EDR_ENDPOINT}}"
    capabilities: [endpoint-protection, threat-detection, response, isolation]
    data_flow: bidirectional  # telemetry in, containment actions out
    side_effect_level: high   # can isolate endpoints
    approval_mode: human-approval  # containment actions require human approval
  ids_ips:
    status: active
    category: observability
    provider: "{{IDS_IPS_PROVIDER}}"  # e.g., "suricata", "palo-alto"
    connection:
      protocol: syslog
      endpoint: "{{IDS_IPS_SYSLOG_TARGET}}"
    capabilities: [intrusion-detection, intrusion-prevention, network-monitoring]
    data_flow: inbound
    side_effect_level: low    # IPS can block traffic
    approval_mode: auto       # blocking rules are pre-approved via policy
  vulnerability_scanner:
    status: active
    category: enterprise-toolchain
    provider: "{{SCANNER_PROVIDER}}"  # e.g., "trivy", "nessus", "snyk"
    connection:
      protocol: API
      endpoint: "https://{{SCANNER_ENDPOINT}}"
    capabilities: [vulnerability-scanning, compliance-scanning, container-scanning]
    data_flow: bidirectional
    side_effect_level: none
    approval_mode: auto
```

### OTel Collector Configuration (SIEM Exporter)

```yaml
# otel-collector-config.yaml — add SIEM exporter to existing pipeline
exporters:
  otlp/siem:
    endpoint: "https://{{SIEM_OTLP_ENDPOINT}}:4317"
    tls:
      cert_file: /etc/otel/certs/collector.crt
      key_file: /etc/otel/certs/collector.key
    headers:
      Authorization: "Bearer {{SIEM_API_TOKEN}}"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, memory_limiter]
      exporters: [otlp/observability, otlp/siem]   # dual export
    logs:
      receivers: [otlp]
      processors: [batch, memory_limiter]
      exporters: [otlp/observability, otlp/siem]   # dual export
```

---

## 4. Alert Routing to Incident Response

Security tool alerts must map to the severity model defined in the [Incident Response Policy](../../../org/4-quality/policies/incident-response.md). The following mapping aligns security tool alert severities with the framework's SEV1-SEV4 model and its associated response SLAs.

| Security Tool Alert | Example Trigger | Framework Severity | Acknowledge SLA | Mitigate SLA | Action |
|---------------------|-----------------|-------------------|-----------------|-------------|--------|
| **Critical** (active exploitation) | EDR detects active ransomware, IDS confirms data exfiltration in progress | **SEV1** | 15 min | 1 hour | Immediate paging of primary + secondary on-call; executive/security escalation engaged; incident commander assigned; containment actions initiated |
| **High** (confirmed threat) | SIEM correlation confirms unauthorized access, EDR detects lateral movement attempt | **SEV2** | 1 hour | 4 hours | Page primary on-call; open incident record and coordination channel; begin investigation and containment |
| **Medium** (suspicious activity) | IDS anomaly alert, failed authentication spike, SIEM detects unusual agent behavior pattern | **SEV3** | 4 hours | 24 hours | Create tracked response item; investigate and determine if escalation needed; apply workaround if available |
| **Low** (informational) | Routine vulnerability scan finding, policy compliance deviation, low-confidence SIEM correlation | **SEV4** | 24 hours | 3 business days | Track in backlog; schedule remediation in normal operations; escalate if pattern indicates systemic issue |

### Alert Routing Architecture

```
Security Tool Alert
        │
        ▼
   SIEM Correlation
   (enrich with agent context from OTel)
        │
        ▼
   Severity Classification
   (mapping table above)
        │
        ├── SEV1/SEV2 ──→ Paging system (PagerDuty/Opsgenie) ──→ Incident commander
        │
        └── SEV3/SEV4 ──→ Ticketing system ──→ Operations queue
```

---

## 5. Integration Registry Entries

For each tooling category, create an integration registry entry following the [Integration Registration Template](../../../org/integrations/_TEMPLATE-integration.md). Below are the key fields for each entry.

### SIEM Integration Registry Entry

| Field | Value |
|-------|-------|
| **Integration Name** | {{SIEM_PRODUCT_NAME}} |
| **Vendor / Project** | {{SIEM_VENDOR}} |
| **Category** | `observability` |
| **Connection Pattern** | OpenTelemetry (OTLP) + syslog ingestion |
| **Access Mode** | Read-write (receives logs; agents query for investigation) |
| **Side-Effect Level** | none (analysis platform) |
| **Approval Mode** | auto |
| **Layers Affected** | Quality, Orchestration, Execution |
| **Loops Affected** | Operate, Ship |

### IDS/IPS Integration Registry Entry

| Field | Value |
|-------|-------|
| **Integration Name** | {{IDS_IPS_PRODUCT_NAME}} |
| **Vendor / Project** | {{IDS_IPS_VENDOR}} |
| **Category** | `observability` |
| **Connection Pattern** | Syslog export to SIEM + API for rule management |
| **Access Mode** | Read-write (monitoring + blocking rules) |
| **Side-Effect Level** | low (IPS can block traffic) |
| **Approval Mode** | operational-approval (rule changes require Orchestration Layer approval) |
| **Layers Affected** | Quality, Orchestration |
| **Loops Affected** | Operate |

### EDR Integration Registry Entry

| Field | Value |
|-------|-------|
| **Integration Name** | {{EDR_PRODUCT_NAME}} |
| **Vendor / Project** | {{EDR_VENDOR}} |
| **Category** | `observability` |
| **Connection Pattern** | API (management + response actions) |
| **Access Mode** | Read-write (telemetry + containment) |
| **Side-Effect Level** | high (can isolate endpoints, terminate processes) |
| **Approval Mode** | human-approval (containment actions require explicit human authorization) |
| **Layers Affected** | Quality, Execution |
| **Loops Affected** | Operate |

### Vulnerability Scanner Integration Registry Entry

| Field | Value |
|-------|-------|
| **Integration Name** | {{SCANNER_PRODUCT_NAME}} |
| **Vendor / Project** | {{SCANNER_VENDOR}} |
| **Category** | `enterprise-toolchain` |
| **Connection Pattern** | API + CI/CD plugin |
| **Access Mode** | Read-only (scanning results) |
| **Side-Effect Level** | none |
| **Approval Mode** | auto |
| **Layers Affected** | Execution, Quality |
| **Loops Affected** | Build, Ship |

### WAF Integration Registry Entry

| Field | Value |
|-------|-------|
| **Integration Name** | {{WAF_PRODUCT_NAME}} |
| **Vendor / Project** | {{WAF_VENDOR}} |
| **Category** | `observability` |
| **Connection Pattern** | API + log export to SIEM |
| **Access Mode** | Read-write (monitoring + rule management) |
| **Side-Effect Level** | low (blocks malicious HTTP traffic) |
| **Approval Mode** | operational-approval (rule changes require Orchestration Layer approval) |
| **Layers Affected** | Quality, Orchestration |
| **Loops Affected** | Operate |

---

## 6. Verification Checklist

Use this checklist to confirm that the runtime security tooling gap is fully closed.

### Tooling Deployment

- [ ] SIEM deployed and receiving logs from all agent workloads
- [ ] IDS/IPS monitoring network traffic at zone boundaries for agent fleet
- [ ] EDR installed on all endpoints running agent workloads
- [ ] Vulnerability scanner running on schedule and integrated into CI/CD pipeline
- [ ] WAF deployed on all external-facing services (Tier 3 deployments)

### Integration and Configuration

- [ ] OTel Collector configured with SIEM exporter (dual export to observability platform and SIEM)
- [ ] Agent telemetry (traces and logs) confirmed flowing into SIEM
- [ ] SIEM correlation rules configured for agent-specific attributes (`agent.id`, `agent.layer`, `governance.decision`)
- [ ] Alert routing configured per incident response policy severity mapping (Section 4)
- [ ] Integration registry entries created for all deployed security tooling (per Section 5)
- [ ] All security tooling registered in `CONFIG.yaml` integrations section (per Section 3)

### Operational Readiness

- [ ] SIEM detection rules validated against test scenarios (simulated attack patterns)
- [ ] Alert-to-incident escalation path tested end-to-end (alert fires, pages correct on-call, incident record created)
- [ ] EDR containment actions tested (endpoint isolation, process termination) with human approval gate confirmed
- [ ] Vulnerability scan findings flowing to SIEM for trending and risk scoring
- [ ] Monthly review of detection rules and alert efficacy scheduled and assigned to security operations owner
- [ ] Vendor security assessments completed for all tooling providers (per [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md))

### Evidence for Audit

- [ ] SIEM dashboards demonstrating continuous monitoring coverage (DE.CM-01 evidence)
- [ ] IDS/IPS alert logs demonstrating network threat detection (PR.PS-02 evidence)
- [ ] EDR deployment report showing fleet coverage percentage
- [ ] Vulnerability scan reports with remediation tracking
- [ ] Incident response drill report showing security alert → incident response workflow integration
