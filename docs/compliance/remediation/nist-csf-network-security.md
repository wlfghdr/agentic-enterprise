<!-- placeholder-ok -->
# NIST CSF 2.0 — Network Security Architecture Guide

> **Closes gap:** Network security implementation (segmentation, firewalls, monitoring)
> **Standard:** NIST CSF 2.0 — PR.IR-01, DE.CM-01
> **Severity:** Critical — protection requires runtime network configuration
> **Related issue:** [#134](https://github.com/wlfghdr/agentic-enterprise/issues/134)
> **Related compliance doc:** [NIST CSF Compliance Reference](../nist-csf.md)

---

## 1. Gap Summary

The Agentic Enterprise framework defines security policies that reference network protection and monitoring, but does not implement the actual network infrastructure required to enforce them:

- The [Security Policy](../../../org/4-quality/policies/security.md) mandates mTLS for all service-to-service communication and zero-trust principles — but does not specify network architecture, segmentation, or firewall rules.
- The [NIST CSF compliance mapping](../nist-csf.md) records PR.IR-01 (networks protected) as addressed by "network segmentation requirements, mTLS" — but the framework provides the policy requirement, not the implementation.
- The [Observability Policy](../../../org/4-quality/policies/observability.md) requires continuous monitoring (DE.CM-01) — but network-level monitoring (flow analysis, DNS inspection, east-west traffic) is not configured.
- The [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) specifies TLS 1.3 minimum and mTLS requirements — but certificate infrastructure and network enforcement points are deployment-specific.

**Without network segmentation, firewall rules, and traffic monitoring, the framework's protection (PR.IR-01) and detection (DE.CM-01) controls for network-layer threats are unenforceable.**

This guide provides the reference architecture, deployment-specific guidance, and verification steps for closing this gap.

---

## 2. Network Security Architecture for Agent Fleets

### Reference Architecture

A multi-agent system requires network isolation between functional zones to contain blast radius, enforce least-privilege communication, and enable targeted monitoring. The following zone model aligns with the framework's 5-layer organizational structure.

```
                    ┌─────────────────────────────┐
                    │       EXTERNAL ZONE          │
                    │  API Gateway / WAF / CDN     │
                    │  Public-facing endpoints      │
                    └──────────────┬───────────────┘
                                   │ HTTPS (TLS 1.3)
                    ┌──────────────▼───────────────┐
                    │     ORCHESTRATION ZONE        │
                    │  Fleet management / Control   │
                    │  plane / API routing          │
                    ├──────────┬───────────────┬────┘
                    │          │               │
         ┌─────────▼──┐  ┌───▼────────┐  ┌──▼──────────┐
         │ AGENT EXEC  │  │ AGENT EXEC │  │ AGENT EXEC  │
         │  ZONE A     │  │  ZONE B    │  │  ZONE C     │
         │ (Division 1)│  │(Division 2)│  │(Division N) │
         └──────┬──────┘  └─────┬──────┘  └──────┬──────┘
                │               │                 │
                └───────────────┼─────────────────┘
                                │ mTLS
                    ┌───────────▼──────────────────┐
                    │         DATA ZONE             │
                    │  Databases / Object storage   │
                    │  Secrets manager / KMS        │
                    └──────────────────────────────┘

                    ┌──────────────────────────────┐
                    │       MANAGEMENT ZONE         │
                    │  Observability platform / SIEM│
                    │  Admin access / CI/CD         │
                    └──────────────────────────────┘
```

### Zone Definitions

| Zone | Purpose | Framework Mapping | Ingress From | Egress To |
|------|---------|-------------------|-------------|-----------|
| **External** | Public-facing services, API gateway, WAF | External integrations, customer-facing APIs | Internet (filtered by WAF) | Orchestration zone only |
| **Orchestration** | Agent fleet control plane, task dispatch, API routing | Orchestration Layer (`org/2-orchestration/`) | External zone, management zone | Agent execution zones, data zone, management zone, external zone |
| **Agent Execution** | Individual agent workloads, grouped by division or fleet | Execution Layer (`org/3-execution/divisions/`) | Orchestration zone | Data zone, management zone (telemetry) |
| **Data** | Databases, object storage, secrets manager, KMS | Persistent data stores, [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) key material | Agent execution zones, orchestration zone | Management zone (audit logs) |
| **Management** | Observability platform, SIEM, admin bastion, CI/CD | Quality Layer (`org/4-quality/`), [SIEM integration](nist-csf-runtime-security-tooling.md) | All zones (telemetry ingress), admin VPN | All zones (monitoring only, no data-plane access) |

### Network Segmentation Patterns

**Micro-segmentation per agent fleet / division:**
Each division or fleet configuration (`org/2-orchestration/fleet-configs/`) maps to its own network segment within the agent execution zone. This ensures that a compromise in one division's agent fleet does not grant lateral movement to another division.

**East-west traffic inspection between zones:**
All traffic crossing zone boundaries passes through an inspection point (firewall, service mesh sidecar, or IDS/IPS sensor). Traffic between agent execution zones is denied by default — agents in Division A cannot communicate directly with agents in Division B unless explicitly permitted.

**North-south traffic through WAF / API gateway:**
All traffic entering from or exiting to the external zone traverses the WAF and API gateway. No agent workload has direct internet access. External API calls from agents route through a controlled egress proxy in the orchestration zone.

**Service mesh for mTLS between agents:**
Per the [Security Policy](../../../org/4-quality/policies/security.md) requirement for mutual TLS on all service-to-service communication, a service mesh (Istio, Linkerd, or equivalent) enforces mTLS with short-lived certificates for all inter-agent and agent-to-service traffic. The [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) specifies TLS 1.3 minimum and approved cipher suites.

---

## 3. Deployment-Specific Guidance

### Cloud (AWS / Azure / GCP)

**VPC / VNet design with subnet isolation:**
- Create a dedicated VPC (AWS), VNet (Azure), or VPC (GCP) for the agent fleet
- Each zone maps to a private subnet (agent execution, data, orchestration, management) or public subnet (external zone only)
- Use separate subnets per agent execution zone (one per division) for micro-segmentation

**Security groups / NSGs per zone:**
- Agent execution subnets: allow ingress only from orchestration subnet on specific service ports; allow egress to data subnet and management subnet (telemetry ports only)
- Data subnet: allow ingress only from agent execution and orchestration subnets on database ports; deny all internet access
- Management subnet: allow ingress from all subnets on telemetry ports (OTLP 4317/4318, syslog 514); allow admin ingress from VPN only
- External subnet: allow ingress from internet on HTTPS (443) through WAF/ALB; allow egress to orchestration subnet only

**Private endpoints for data services:**
- Use VPC endpoints (AWS), Private Link (Azure), or Private Service Connect (GCP) for all data services (databases, object storage, KMS, secrets manager)
- No data service should be reachable from the public internet, even with authentication

**NAT gateway for controlled egress:**
- Agent execution zones access external APIs through a NAT gateway in the orchestration zone
- Egress is filtered by destination allowlist (only approved integration endpoints from `CONFIG.yaml`)
- All egress traffic is logged for SIEM correlation

**Example — AWS Security Group rules for agent execution zone:**

```
# Agent Execution Security Group
Inbound:
  - Protocol: TCP, Port: 8080-8090, Source: sg-orchestration  # service calls
  - Protocol: TCP, Port: 443, Source: sg-orchestration         # HTTPS from control plane

Outbound:
  - Protocol: TCP, Port: 5432, Destination: sg-data            # PostgreSQL
  - Protocol: TCP, Port: 4317, Destination: sg-management      # OTel OTLP gRPC
  - Protocol: TCP, Port: 4318, Destination: sg-management      # OTel OTLP HTTP
```

### Kubernetes

**Network policies (Calico / Cilium) per namespace:**
- Map each zone to a Kubernetes namespace: `agent-exec-div-a`, `agent-exec-div-b`, `orchestration`, `data`, `management`
- Apply `NetworkPolicy` resources that implement zone ingress/egress rules
- Default deny all ingress and egress; explicitly allow only required flows

**Example — Kubernetes NetworkPolicy for agent execution namespace:**

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: agent-execution-policy
  namespace: agent-exec-div-a
spec:
  podSelector: {}   # applies to all pods in namespace
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              zone: orchestration
      ports:
        - protocol: TCP
          port: 8080
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              zone: data
      ports:
        - protocol: TCP
          port: 5432
    - to:
        - namespaceSelector:
            matchLabels:
              zone: management
      ports:
        - protocol: TCP
          port: 4317    # OTel OTLP
```

**Service mesh (Istio / Linkerd) for mTLS:**
- Enable strict mTLS mode mesh-wide (all pod-to-pod traffic encrypted and mutually authenticated)
- Configure `PeerAuthentication` in strict mode for all namespaces
- Use `AuthorizationPolicy` to enforce per-service access control (only orchestration can call agent workloads; agents can only call permitted data services)
- Short-lived certificates (24h default, per [Cryptography Policy](../../../org/4-quality/policies/cryptography.md) rotation requirements)

**Ingress controller with WAF:**
- Deploy an ingress controller (NGINX Ingress, Envoy Gateway) with WAF integration (ModSecurity, Coraza)
- All external traffic enters through the ingress controller — no `NodePort` or `LoadBalancer` services exposed directly
- Rate limiting and bot detection at the ingress layer

**Pod security standards:**
- Enforce `restricted` Pod Security Standard on all agent execution namespaces
- No privileged containers, no host networking, no host PID, read-only root filesystem
- Run as non-root (per [Security Policy](../../../org/4-quality/policies/security.md) container security requirements)

### On-Premise

**VLAN segmentation:**
- Map each zone to a dedicated VLAN: VLAN 100 (external), VLAN 200 (orchestration), VLAN 300-399 (agent execution, one per division), VLAN 400 (data), VLAN 500 (management)
- Inter-VLAN routing through Layer 3 firewall with explicit ACLs

**Next-gen firewall between zones:**
- Deploy a next-generation firewall (Palo Alto, Fortinet, pfSense) at the core routing layer
- Application-aware rules (not just port-based) for east-west traffic
- Deep packet inspection for agent-to-agent and agent-to-data traffic
- IDS/IPS enabled at the firewall for all inter-zone traffic

**DMZ for external-facing services:**
- External-facing services (API gateway, WAF) in a dedicated DMZ segment
- Dual firewall architecture: external firewall (internet to DMZ), internal firewall (DMZ to internal zones)
- No direct path from DMZ to data zone — traffic must traverse the orchestration zone

---

## 4. Network Monitoring Requirements

All network monitoring data feeds into the SIEM as described in the [Runtime Security Tooling Guide](nist-csf-runtime-security-tooling.md).

| Monitoring Type | CSF Subcategory | Implementation | Data Destination |
|----------------|-----------------|----------------|-----------------|
| **Traffic flow analysis** | DE.CM-01 | NetFlow/sFlow/IPFIX exported from routers, switches, and cloud VPC flow logs | SIEM — baseline traffic patterns and anomaly detection |
| **Anomaly detection** | DE.AE-02 | ML-based traffic baseline established per zone; alerts on volume deviations, new connection patterns, unusual port usage | SIEM correlation engine — triggers SEV3 investigation |
| **East-west inspection** | DE.CM-01 | Service mesh telemetry (Istio/Linkerd metrics and access logs) or network TAP/SPAN port mirroring at zone boundaries | SIEM + observability platform — correlate with agent `tool.execute` spans |
| **DNS monitoring** | DE.CM-01 | DNS query logging on internal resolvers; correlation with threat intelligence domain lists (DGA detection, known C2 domains) | SIEM — DNS tunneling and exfiltration detection |
| **Certificate transparency** | PR.DS-02 | TLS certificate inventory maintained; automated alerts on expiry (30/14/7 day thresholds); CT log monitoring for unauthorized certificates | Certificate management system — alerts to SIEM on anomaly |
| **Egress monitoring** | DE.CM-01 | All outbound connections logged at NAT gateway / proxy; alerts on connections to unapproved destinations | SIEM — data exfiltration detection |

### OTel Integration for Network Monitoring

The OTel Collector can receive network telemetry alongside agent traces:

```yaml
# otel-collector-config.yaml — network monitoring receivers
receivers:
  syslog:
    protocol: rfc5424
    listen_address: "0.0.0.0:54526"
    # Receives firewall logs, IDS/IPS alerts, DNS logs
  netflow:
    # If using a netflow-to-OTLP converter
    endpoint: "0.0.0.0:2055"

processors:
  attributes/network:
    actions:
      - key: telemetry.source
        value: network-infrastructure
        action: upsert

exporters:
  otlp/siem:
    endpoint: "https://{{SIEM_OTLP_ENDPOINT}}:4317"

service:
  pipelines:
    logs/network:
      receivers: [syslog]
      processors: [batch, attributes/network]
      exporters: [otlp/siem]
```

---

## 5. Zero-Trust Architecture Recommendations

The following principles align with the [Security Policy](../../../org/4-quality/policies/security.md) zero-trust mandate and apply specifically to network-level implementation for agent fleets.

### Never Trust, Always Verify

Every agent-to-agent and agent-to-service call is authenticated via mTLS. Network location (being "inside the VPC") does not confer trust. Even within the agent execution zone, each connection presents a valid, short-lived certificate tied to the agent's identity.

**Implementation:** Service mesh with strict mTLS and identity-aware authorization policies. The agent's `agent.id` (from the [OTel contract](../../otel-contract.md)) is embedded in the certificate's SAN field, enabling per-agent access control.

### Least-Privilege Network Access

Agents can only reach the services they need for their current mission. Network access is scoped per agent type and fleet configuration, not per zone.

**Implementation:**
- Kubernetes: `AuthorizationPolicy` resources matching on service account (one per agent type)
- Cloud: Security group rules referencing specific service tags
- On-premise: Firewall rules referencing source VLAN + destination service port

### Microsegmentation for Blast Radius Containment

If one agent workload is compromised, the attacker gains access only to the services that specific agent type is permitted to reach — not the entire zone, not the entire fleet, and never the data zone directly.

**Implementation:**
- One network policy per agent type (not per zone)
- Default deny between agent execution segments
- Explicit allow only for declared dependencies in fleet config

### Continuous Verification

Authentication is not a one-time event at connection establishment. Short-lived certificates (24h rotation per [Cryptography Policy](../../../org/4-quality/policies/cryptography.md)) ensure that revoked or expired agents lose network access automatically. The service mesh performs certificate verification on every request, not just at TLS handshake.

**Implementation:**
- Certificate rotation: 24h maximum lifetime, automated renewal via cert-manager or Vault PKI
- Connection draining on certificate expiry — no long-lived persistent connections bypass rotation
- Certificate revocation checked via OCSP stapling or CRL distribution point

### Encrypted Everywhere

All traffic is encrypted with TLS 1.3 minimum, as mandated by the [Cryptography Policy](../../../org/4-quality/policies/cryptography.md). This applies to:
- Agent-to-agent traffic (mTLS via service mesh)
- Agent-to-database traffic (TLS with server certificate validation)
- Telemetry export (OTLP over TLS to observability platform and SIEM)
- Management access (SSH/HTTPS over VPN with MFA)

**No plaintext traffic is permitted on any network segment, including management and monitoring traffic.**

---

## 6. CONFIG.yaml Network Security Configuration

Add the following to `CONFIG.yaml` to declare the network security architecture for the deployment:

```yaml
security:
  network:
    architecture: zero-trust
    tls_minimum: "1.3"
    mtls_enabled: true
    certificate_rotation: "24h"
    certificate_provider: "{{CERT_PROVIDER}}"  # e.g., "cert-manager", "vault-pki", "aws-acm"
    zones:
      external:
        description: "Public-facing services — API gateway, WAF, CDN"
        allowed_ingress: [internet]   # filtered by WAF
        allowed_egress: [orchestration]
      orchestration:
        description: "Agent fleet control plane — task dispatch, API routing"
        allowed_ingress: [external, management]
        allowed_egress: [agent_execution, data, management, external]
      agent_execution:
        description: "Agent workloads — isolated per division/fleet"
        allowed_ingress: [orchestration]
        allowed_egress: [data, management]
        denied_egress: [external, internet]  # agents do not access internet directly
        segmentation: per-division           # micro-segmented by division
      data:
        description: "Databases, object storage, KMS, secrets manager"
        allowed_ingress: [agent_execution, orchestration]
        denied_ingress: [external, internet]
        allowed_egress: [management]         # audit logs only
      management:
        description: "Observability, SIEM, admin bastion, CI/CD"
        allowed_ingress: [all_zones_telemetry, vpn_admin]
        allowed_egress: [all_zones_monitoring]  # monitoring only, no data-plane
    monitoring:
      flow_analysis: true
      dns_monitoring: true
      east_west_inspection: true
      egress_logging: true
      certificate_transparency: true
```

---

## 7. Verification Checklist

Use this checklist to confirm that the network security gap is fully closed.

### Network Architecture

- [ ] Network zones defined and documented (external, orchestration, agent execution, data, management)
- [ ] Network architecture diagram maintained and current (reviewed at least quarterly)
- [ ] Zone boundaries enforced by firewall rules, security groups, or network policies
- [ ] Micro-segmentation implemented per division / agent fleet within agent execution zone
- [ ] Default deny policy in place — only explicitly permitted traffic flows

### Access Control

- [ ] mTLS enforced for all agent-to-agent and agent-to-service communication
- [ ] TLS 1.3 minimum enforced on all network segments (per [Cryptography Policy](../../../org/4-quality/policies/cryptography.md))
- [ ] Short-lived certificates (24h maximum) with automated rotation
- [ ] Agent workloads have no direct internet egress — all external API calls route through controlled proxy
- [ ] Data zone has no ingress from external zone — enforced at network level

### Monitoring and Detection

- [ ] East-west traffic monitored (service mesh telemetry or network TAP)
- [ ] Network flow data (NetFlow/sFlow/VPC flow logs) exported to SIEM
- [ ] DNS monitoring enabled with threat intelligence correlation
- [ ] Egress monitoring active — alerts on connections to unapproved destinations
- [ ] Certificate expiry monitoring with 30/14/7-day alerting thresholds
- [ ] Anomaly detection baseline established for each zone's traffic patterns

### Configuration and Governance

- [ ] Network security configuration declared in `CONFIG.yaml` (Section 6)
- [ ] Zero-trust principles documented and applied (Section 5)
- [ ] Deployment-specific implementation completed (Section 3 — cloud, Kubernetes, or on-premise)
- [ ] Network monitoring feeds integrated with SIEM (per [Runtime Security Tooling Guide](nist-csf-runtime-security-tooling.md))
- [ ] Quarterly network security review scheduled and assigned to security operations owner
- [ ] Firewall rule / security group change process governed via PR (infrastructure-as-code)

### Evidence for Audit

- [ ] Network architecture diagram with zone boundaries and traffic flows (PR.IR-01 evidence)
- [ ] Firewall rule / security group export demonstrating least-privilege configuration
- [ ] mTLS certificate deployment report showing coverage percentage
- [ ] Network flow analysis dashboard demonstrating continuous monitoring (DE.CM-01 evidence)
- [ ] DNS monitoring dashboard with threat correlation examples
- [ ] Network security review report from most recent quarterly review
