# Integration Registration: {{INTEGRATION_NAME}}

> **Status:** `proposed` | `active` | `deprecated`  
> **Category:** `observability` | `enterprise-toolchain` | `business-system` | `communication`  
> **Owner:** {{APPROVING_LAYER}} Layer  
> **Last updated:** YYYY-MM-DD

---

## Overview

| Field | Value |
|-------|-------|
| **Integration Name** | {{INTEGRATION_NAME}} |
| **Vendor / Project** | {{VENDOR_OR_PROJECT}} |
| **Category** | {{CATEGORY}} |
| **Connection Pattern** | MCP Server / API / Webhook / Data Export / OpenTelemetry |
| **Layers Affected** | Steering / Strategy / Orchestration / Execution / Quality |
| **Loops Affected** | Discover / Build / Ship / Operate |

---

## What It Does

<!-- Brief description of what this integration enables in the operating model -->

## Connection Details

### Protocol

<!-- MCP, REST API, GraphQL, Webhook, gRPC, OpenTelemetry (OTLP), etc. -->

### Authentication

<!-- How agents authenticate: API key, OAuth, service account, mTLS, etc. -->
<!-- Reference secrets management from CONFIG.yaml → toolchain.secrets_manager -->

### Data Flow

```
Direction:  Inbound / Outbound / Bidirectional

Inbound:   External system → Operating model (signals, metrics, events)
Outbound:  Operating model → External system (actions, updates, notifications)
```

### Endpoints / Resources

<!-- List the specific APIs, MCP tools, or resources this integration exposes -->

| Resource | Type | Description |
|----------|------|-------------|
| | | |

---

## Layer & Loop Mapping

### Which agents use this integration?

| Agent Type | Layer | How They Use It |
|------------|-------|-----------------|
| | | |

### Which loops benefit?

| Loop | Benefit |
|------|---------|
| Discover | |
| Build | |
| Ship | |
| Operate | |

---

## Governance

### Approval

- **Structural approval:** {{WHO_APPROVES}} (Steering Layer)
- **Operational activation:** {{WHO_ACTIVATES}} (Orchestration Layer)
- **Data governance review:** Required / Not Required

### Security & Compliance

- **Data classification:** What data flows through this integration?
- **Retention:** What retention policies apply?
- **Audit:** How is usage logged and auditable?
- **Policy references:** Which quality policies apply?
  - [ ] `org/4-quality/policies/security.md`
  - [ ] `org/4-quality/policies/delivery.md`
  - [ ] `org/4-quality/policies/customer.md`

### Failure Mode

- **If unavailable:** How do agents behave when this integration is down?
- **Fallback:** Is there a degraded-mode behavior?
- **SLA dependency:** What uptime does this integration require?

---

## Configuration

```yaml
# Add to CONFIG.yaml → integrations section
integrations:
  {{CATEGORY}}:
    - id: "{{INTEGRATION_SLUG}}"
      name: "{{INTEGRATION_NAME}}"
      vendor: "{{VENDOR}}"
      connection: "{{PROTOCOL}}"
      # Additional configuration fields as needed
```

---

## Validation Checklist

- [ ] Integration registered in CONFIG.yaml
- [ ] Security review completed
- [ ] Data governance review completed (if required)
- [ ] Connection tested and documented
- [ ] Failure mode and fallback defined
- [ ] Affected agent types updated with integration awareness
- [ ] Quality policies reviewed for compliance
