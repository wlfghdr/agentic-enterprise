# Enterprise Toolchain Integration

> **Category:** Enterprise Toolchain  
> **Relevance:** Connects the operating model to the existing software delivery, operations, and security infrastructure that enterprises already rely on  
> **Layers Affected:** Primarily Orchestration, Execution, and Quality

---

## Why Enterprise Toolchain Integration Matters

Enterprises invest significantly in their toolchains — CI/CD pipelines, ITSM platforms, security scanners, service catalogs, and developer portals. The agentic enterprise operating model does not replace these investments. It **connects them** through a governed integration layer so that agents can leverage existing tools while maintaining the operating model as the system of record.

The operating model defines the *what* (missions, policies, quality gates). Enterprise tools execute the *how* (build pipelines, deployment infrastructure, security scanning). The integration layer bridges these two worlds.

---

## Integration Areas

### CI/CD Pipelines

The operating model treats CI/CD as the enforcement mechanism for quality gates.

| Tool Category | Examples | Integration Pattern |
|--------------|---------|---------------------|
| **Pipeline engines** | GitHub Actions, GitLab CI, Jenkins, CircleCI, Azure Pipelines | Webhook-triggered from PR events; status checks enforce quality policies |
| **Deployment** | ArgoCD, Flux, Spinnaker, AWS CodeDeploy | Progressive rollout definitions in release contracts; deployment status feeds operate loop |
| **Artifact registries** | ECR, GCR, Docker Hub, Artifactory | Asset registry entries reference deployed artifacts |
| **Feature flags** | LaunchDarkly, OpenFeature, Unleash, Split | Progressive exposure controlled by operate loop agents |

**Integration points:**
- PR creation → pipeline trigger → quality gate enforcement
- Deployment completion → release contract update → operate loop activation
- Feature flag state → agent-controlled progressive rollout

### ITSM & Project Management

While the operating model uses Git-based work artifacts, many enterprises need to keep existing ITSM and project management systems informed.

| Tool Category | Examples | Integration Pattern |
|--------------|---------|---------------------|
| **ITSM** | ServiceNow, Jira Service Management, Zendesk | Bidirectional sync: incidents from ITSM → signals in `work/signals/`; operating model actions → ITSM tickets |
| **Project management** | Jira, Linear, Azure DevOps, Asana | One-way sync: mission status → external visibility dashboards |
| **Documentation** | Confluence, Notion, SharePoint | Content publishing from `work/` artifacts |

**Key principle:** Git remains the system of record. ITSM/PM tools get synchronized views, not authoritative copies. This prevents the "two sources of truth" anti-pattern.

### Security & Compliance

Quality policies in `org/4-quality/policies/` define security requirements. Enterprise security tools enforce them.

| Tool Category | Examples | Integration Pattern |
|--------------|---------|---------------------|
| **Vulnerability scanning** | Snyk, Dependabot, Trivy, Checkmarx | Scan results → quality evaluation input; critical findings → automatic signals |
| **Secret detection** | GitLeaks, TruffleHog, GitHub Secret Scanning | Pre-commit and CI checks referencing security policy |
| **Compliance frameworks** | OPA/Rego, Kyverno, Checkov | Policy-as-code enforcement from quality policy definitions |
| **SIEM / Security analytics** | Splunk, Microsoft Sentinel, Elastic Security | Security events → incident signals → automated response |

### Service Catalogs & Developer Portals

The operating model's division structure maps naturally to service catalog entries.

| Tool Category | Examples | Integration Pattern |
|--------------|---------|---------------------|
| **Service catalogs** | Backstage, Port, OpsLevel, Cortex | Division/service metadata synced from `org/3-execution/divisions/` |
| **API catalogs** | SwaggerHub, Postman, Stoplight | API definitions from technical designs |
| **Developer portals** | Backstage, custom portals | Aggregated view of operating model + toolchain status |

---

## Connection Patterns

### MCP Servers (Recommended for Agent Access)

Agents interact with enterprise tools through MCP (Model Context Protocol) servers. Each tool gets an MCP server that exposes its capabilities as agent-callable tools.

```
Agent → MCP Server → Enterprise Tool
                          │
                  ┌───────┴────────┐
                  │  ServiceNow    │
                  │  Jira          │
                  │  Jenkins       │
                  │  Snyk          │
                  │  Backstage     │
                  └────────────────┘
```

### Webhooks (Tool → Operating Model)

External tools push events into the operating model via webhooks:

```
CI/CD pipeline completes → webhook → create signal or update mission status
Security scanner finds CVE → webhook → create security signal
ITSM ticket escalated → webhook → create improvement signal
Customer support case opened → webhook → create customer signal
```

### API Integration (Operating Model → Tool)

Agents make outbound API calls to enterprise tools:

```
Release contract approved → API → trigger deployment in ArgoCD
Incident detected → API → create ServiceNow incident
Mission completed → API → update Jira status
Quality evaluation → API → publish results to Backstage
```

---

## Configuration

Register your enterprise toolchain in CONFIG.yaml:

```yaml
integrations:
  enterprise_toolchain:
    ci_cd:
      - id: "primary-pipeline"
        name: "GitHub Actions"
        connection: "webhook"
        mcp_server: false
    
    itsm:
      - id: "incident-management"
        name: "ServiceNow"
        connection: "mcp"
        mcp_server: true
        sync_direction: "bidirectional"
    
    security:
      - id: "vulnerability-scanning"
        name: "Snyk"
        connection: "webhook"
        mcp_server: true
    
    catalog:
      - id: "service-catalog"
        name: "Backstage"
        connection: "api"
        mcp_server: false
```

---

## Getting Started

1. **Inventory your current tools** — List every tool your teams use for CI/CD, ITSM, security, and developer experience
2. **Map to integration patterns** — For each tool, identify: MCP server (agent access), webhook (inbound events), or API (outbound actions)
3. **Prioritize** — Start with CI/CD (quality gates) and observability (fleet monitoring) — these provide immediate value
4. **Register in CONFIG.yaml** — Add each tool to the integrations section
5. **Implement incrementally** — Wire one integration at a time, validate with quality policies, then expand
