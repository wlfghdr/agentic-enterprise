# Business Systems Integration

> **Category:** Business Systems  
> **Relevance:** Connects agent workflows to the commercial and operational backbone of the enterprise  
> **Layers Affected:** Strategy, Execution (GTM + Customer divisions), Quality

---

## Why Business Systems Integration Matters

The operating model covers the entire company — not just engineering. Go-to-market, sales, customer success, and support divisions need access to their business systems to operate effectively within the agentic model.

---

## Integration Areas

| System | Examples | How Agents Use It |
|--------|---------|-------------------|
| **CRM** | Salesforce, HubSpot, Dynamics 365 | Sales intelligence agents query pipeline data; customer signal agents track health scores |
| **ERP** | SAP, Oracle, NetSuite | Finance agents track revenue impact of missions; resource planning |
| **Customer Support** | Zendesk, Freshdesk, Intercom | Support agents create and manage cases; escalation patterns feed signals |
| **HR / People** | Workday, BambooHR, Personio | Org structure sync; capacity planning; skills mapping for fleet assembly |
| **Analytics** | Mixpanel, Amplitude, Google Analytics | Discovery agents access product usage data; outcome reports reference adoption metrics |
| **Marketing Automation** | Marketo, Pardot, Mailchimp | GTM execution agents coordinate campaigns aligned with mission launch timelines |

---

## Connection Patterns

Business system integrations typically use **MCP servers** for agent read access and **API integrations** for write operations:

```
Strategy Agent (Discovery)  → MCP Server → CRM    (read pipeline, health scores)
Execution Agent (GTM)       → API        → CMS    (publish content, trigger campaign)
Execution Agent (Support)   → MCP Server → Zendesk (read tickets, update status)
Quality Agent               → API        → Analytics (read adoption metrics for outcome reports)
```

---

## Configuration

```yaml
integrations:
  business_systems:
    - id: "crm"
      name: "Salesforce"
      connection: "mcp"
      mcp_server: true
      used_by: ["strategy", "execution-customer"]
    
    - id: "support"  
      name: "Zendesk"
      connection: "mcp"
      mcp_server: true
      used_by: ["execution-customer"]
    
    - id: "analytics"
      name: "Mixpanel"
      connection: "api"
      used_by: ["strategy", "quality"]
```
