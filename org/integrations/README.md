# Integration Registry

> **What this is:** The governed registry of external tools, platforms, and services that connect to the agentic enterprise operating model. While the operating model's definitions live in the filesystem (Markdown + YAML), real enterprises run on a rich ecosystem of specialized tools. This registry makes those connections explicit, governed, and auditable.  
> **Governance:** Changes via Pull Request → Steering Layer (structural) or Orchestration Layer (operational) approval

---

## Why an Integration Registry?

The operating model uses Git as the **system of record** — the canonical source of truth for organizational structure, process definitions, agent instructions, quality policies, and work artifacts. But Git is not the **only system**. Enterprises operate with:

- **Enterprise toolchains** — ITSM platforms, project management, CI/CD pipelines, security scanners, communication tools
- **Observability platforms** — Telemetry collection, analysis, dashboarding, alerting, and AI-powered root cause analysis
- **Business systems** — CRM, ERP, HR, finance, customer support platforms
- **Developer platforms** — Service catalogs, developer portals, build infrastructure
- **Communication channels** — Chat, messaging, email, video conferencing

These tools are not being replaced. They play critical roles in enterprise operations. What changes is **how they connect** — through governed, declarative integration definitions rather than ad-hoc point-to-point wiring.

---

## Integration Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Git Repository (System of Record)                                 │
│   ├── Org structure, agent instructions, policies, work artifacts   │
│   └── Integration definitions (this registry)                       │
│                                                                     │
├──────────────┬──────────────┬──────────────┬───────────────────────┤
│              │              │              │                         │
│  Enterprise  │ Observability│   Business   │   Communication        │
│  Toolchain   │  & Telemetry │   Systems    │   Channels             │
│              │              │              │                         │
│  CI/CD       │  Metrics     │  CRM         │  Chat / Messaging      │
│  ITSM        │  Traces      │  ERP         │  Email                 │
│  Security    │  Logs        │  HR          │  Notifications         │
│  Catalogs    │  AI Analysis │  Finance     │  Dashboards            │
│              │              │              │                         │
└──────────────┴──────────────┴──────────────┴───────────────────────┘
```

### Connection Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **MCP Server** | Agent connects to external tool via Model Context Protocol | Agent reads Jira tickets, queries Dynatrace, creates ServiceNow incidents |
| **API Integration** | Direct API calls from agent toolchains | REST/GraphQL calls to business systems |
| **Webhook / Event** | External system triggers Git-based workflows | CI/CD completion → signal creation, alert → incident response |
| **Data Export** | Periodic or streaming data flow into the operating model | Observability metrics → fleet performance dashboards |
| **OpenTelemetry** | Standardized telemetry collection for agent activity | Agent spans, metrics, and logs exported via OTLP |

---

## Registry Structure

```
org/integrations/
├── README.md                        ← You are here
├── _TEMPLATE-integration.md         ← Template for registering new integrations
├── categories/
│   ├── observability.md             ← Observability & telemetry integrations
│   ├── enterprise-toolchain.md      ← CI/CD, ITSM, security, catalogs
│   ├── business-systems.md          ← CRM, ERP, HR, finance
│   └── communication.md             ← Chat, messaging, notifications
└── vendors/                         ← Per-vendor integration specs (optional)
```

Each integration entry defines:
- **What it connects to** — the external system
- **How it connects** — MCP, API, webhook, data export, OpenTelemetry
- **What it enables** — which layers, loops, and agent types benefit
- **Governance** — who approves activation, what data flows, what policies apply

---

## How Adopters Register Integrations

1. **Choose your tools** — Review the category guides to understand integration patterns
2. **Register in CONFIG.yaml** — Add your tool choices to the `integrations` section
3. **Create integration specs** — For complex integrations, create a spec from the template
4. **Wire the connections** — Implement MCP servers, webhooks, or API clients in your agent runtime
5. **Validate with quality policies** — Ensure integrations comply with security and data governance policies

---

## Principles

### 1. Git is the system of record, not the only system

The operating model's definitions, decisions, and governance live in Git. But execution happens across many systems. Agents create branches and PRs in Git while simultaneously querying observability platforms, updating ITSM tickets, and sending chat messages. The integration registry makes these connections explicit.

### 2. Integrations are governed, not ad-hoc

Every external tool connection is registered, reviewed, and approved through the same PR-based governance as everything else. No shadow IT, no untracked API keys, no invisible data flows.

### 3. Vendor-neutral by default, specific by choice

The registry defines integration **patterns** (e.g., "observability platform") and **protocols** (e.g., OpenTelemetry, MCP). Adopters choose specific vendors. The framework doesn't lock you in.

### 4. Observability is essential for scaling agent governance

As agent fleets grow, filesystem-based governance alone cannot provide the real-time visibility, anomaly detection, and causal analysis needed to maintain trust. Observability platforms become the **scaling layer** — processing the telemetry that agents and systems generate far faster than any human or file-based process could.

### 5. Open standards preferred, proprietary supported

Prefer OpenTelemetry for telemetry, MCP for tool connections, and open APIs for data exchange. But real enterprises use proprietary platforms — and that's fine. The registry supports both.
