# Runtime Instrumentation Guide

> **Version:** 1.0 | **Last updated:** 2026-03-17
> **Purpose:** How to instrument Claude Code, Claude Agent SDK, and OpenClaw runtimes to emit OpenTelemetry spans conforming to the [OTel Contract](../otel-contract.md).
> **Audience:** Operators setting up agent fleets who need runtime-level telemetry, not just Git-based audit trails.

---

## Table of Contents

1. [Why Runtime Instrumentation Matters](#1-why-runtime-instrumentation-matters)
2. [Instrumentation Strategy: Three Tiers](#2-instrumentation-strategy-three-tiers)
3. [Prerequisites](#3-prerequisites)
4. [Claude Code: Two-Layer Instrumentation](#4-claude-code-two-layer-instrumentation)
5. [Claude Agent SDK: Code-Level Instrumentation](#5-claude-agent-sdk-code-level-instrumentation)
6. [OpenClaw: Environment-Based Instrumentation](#6-openclaw-environment-based-instrumentation)
7. [OTel Collector on VPS](#7-otel-collector-on-vps)
8. [Span Mapping Reference](#8-span-mapping-reference)

---

## 1. Why Runtime Instrumentation Matters

The framework has two coordination channels:

```
Git Repository            Observability Platform
──────────────            ──────────────────────
What was decided          What actually happened
Governance trail          Execution trail
Asynchronous              Real-time
```

Without runtime instrumentation, you only have the Git side. You cannot answer:
- Which agent tool calls are slow or failing?
- How long does an `agent.run` actually take end-to-end?
- Which missions generate the most tool retries?
- Are quality evaluation spans showing policy violation patterns?

Runtime instrumentation closes this gap by emitting OTel spans from inside the agent runtime itself.

---

## 2. Instrumentation Strategy: Three Tiers

Choose the tier that matches your operational maturity. Start at Tier 1 and promote as needed.

| Tier | What you have | What you emit | When to use |
|---|---|---|---|
| **Tier 1 — Structured logs** | Nothing extra | JSON logs to stdout | Starting out, no OTel backend yet |
| **Tier 2 — Native OTel** | OTel env vars + OTel Collector | Inference spans, token usage, latency | First OTel step — zero code changes |
| **Tier 3 — Native + Hooks** | Tier 2 + `otelcli` hooks | Full coverage: inference + tool + agentic attributes | Active fleet, dashboards, mission tracking |
| **Tier 4 — Full trace hierarchy** | Tier 3 + trace context propagation | Parent-child span trees across agents | Production fleet, multi-agent tracing |

**Do not skip to Tier 4 prematurely.** Tier 1 is fully compliant with the framework's minimum viable observability requirement. Tier 2 is the right first OTel step for Claude Code.

---

## 3. Prerequisites

### 3.1 otelcli (required for Claude Code hook-based instrumentation)

[`otelcli`](https://github.com/equinix-labs/otelcli) is a CLI tool that emits OTel spans from shell scripts. It is the bridge between Claude Code hooks (which are shell commands) and your OTLP endpoint.

**Install on VPS:**
```bash
# Download latest release for linux/amd64
curl -L https://github.com/equinix-labs/otelcli/releases/latest/download/otelcli_linux_amd64.tar.gz \
  | tar xz -C /usr/local/bin otelcli
chmod +x /usr/local/bin/otelcli
otelcli version
```

**Install locally (macOS):**
```bash
brew install equinix-labs/otelcli/otelcli
```

### 3.2 Environment variables (all runtimes)

Set these before starting any agent runtime:

```bash
# OTLP endpoint — your collector or direct backend
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"        # local collector (gRPC)
# or direct to backend:
# export OTEL_EXPORTER_OTLP_ENDPOINT="https://your-backend/otlp"

# Agent identity — used as OTel service.name
export AGENT_ID="cc-ops-triage"                                    # e.g. cc-ops-triage, cc-exec-builder
export AGENTIC_LAYER="execution"                                   # steering|strategy|orchestration|execution|quality
export AGENTIC_MISSION_ID="MSN-2026-001"                           # current mission (update per session)
export OTEL_SERVICE_NAME="$AGENT_ID"
export OTEL_SERVICE_VERSION="1.0.0"
export DEPLOYMENT_ENVIRONMENT="production"                         # production|staging|development
```

Add these to `/root/.bashrc` or `/etc/environment` on the VPS for persistent configuration.

---

## 4. Claude Code: Two-Layer Instrumentation

Claude Code instrumentation is achieved through two complementary layers that together cover the full OTel contract:

```
Layer 1 — Native OTel (env vars)
  Covers: inference spans, token usage, latency, model identity
  How:    Standard OTEL_* env vars activate the underlying SDK's built-in export

Layer 2 — Hooks (otelcli)
  Covers: tool.execute, git.operation, agent.run boundaries, agentic.* attributes
  How:    PostToolUse and Stop hooks emit spans via otelcli shell calls
```

Neither layer alone gives full coverage. Use both.

### 4.1 Layer 1 — Native OTel (env vars)

Claude Code is built on the Anthropic SDK, which supports OpenTelemetry natively. Set `OTEL_EXPORTER_OTLP_ENDPOINT` and the SDK automatically emits inference spans including token counts, model identity, and latency — with no code changes or hooks required.

**What native OTel covers:**

| Span | Attributes automatically included |
|---|---|
| `chat claude-sonnet-4-6` (inference) | `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.finish_reasons` |
| Session-level trace context | Trace ID propagated across all SDK calls in the session |

**Activate by setting env vars before launching Claude Code:**

```bash
# OTLP endpoint (local collector or direct backend)
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL="grpc"          # grpc (default) or http/protobuf

# Service identity (maps to OTel resource attributes)
export OTEL_SERVICE_NAME="cc-ops-triage"
export OTEL_SERVICE_VERSION="1.0.0"
export OTEL_RESOURCE_ATTRIBUTES="deployment.environment.name=production,service.namespace=agentic-enterprise,agentic.layer=strategy,agentic.mission.id=MSN-2026-001"

# Privacy — disable prompt/completion content capture (framework default)
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"
```

Then simply launch Claude Code normally:
```bash
claude
# or in non-interactive mode:
claude --print "your task here"
```

Inference spans flow automatically to your OTLP endpoint.

### 4.2 Layer 2 — Hooks (otelcli, complementary)

The native OTel layer does not emit `tool.execute`, `git.operation`, or `agent.run` spans with `agentic.*` attributes. The hooks layer fills this gap.

Hooks are configured in `.claude/settings.json` at the repo root (or `~/.claude/settings.json` globally). They fire on agent events and receive a JSON payload via **stdin**:

```json
// PostToolUse payload
{
  "session_id": "abc123",
  "tool_name": "Bash",
  "tool_input": { "command": "git status" },
  "tool_response": { "output": "..." }
}
```

**Activate by adding to `.claude/settings.json`:**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [{ "type": "command", "command": ".claude/hooks/otel-tool-span.sh" }]
      }
    ],
    "Stop": [
      {
        "hooks": [{ "type": "command", "command": ".claude/hooks/otel-agent-stop.sh" }]
      }
    ]
  }
}
```

Ready-to-use hook scripts are at `.claude/hooks/` in this repo (make them executable with `chmod +x`):

- **`otel-tool-span.sh`** — emits `tool.execute` (or `git.operation`) after each tool call with `agentic.*` attributes
- **`otel-agent-stop.sh`** — emits `agent.run` when the session ends

**Test hooks manually:**
```bash
echo '{"session_id":"test-123","tool_name":"Bash","tool_input":{"command":"ls"}}' \
  | .claude/hooks/otel-tool-span.sh
```

### 4.3 Combined Coverage Map

| Span / Attribute | Layer 1 (native) | Layer 2 (hooks) |
|---|---|---|
| `inference.chat` (LLM calls) | ✅ automatic | ✗ |
| `gen_ai.usage.input_tokens` | ✅ automatic | ✗ |
| `gen_ai.usage.output_tokens` | ✅ automatic | ✗ |
| `gen_ai.request.model` | ✅ automatic | ✗ |
| Session trace context (trace ID) | ✅ automatic | ✗ |
| `tool.execute` spans | ✗ | ✅ via PostToolUse hook |
| `git.operation` spans | ✗ | ✅ detected in Bash tool calls |
| `agent.run` span boundary | ✗ | ✅ via Stop hook |
| `agentic.layer` attribute | ✗ | ✅ from env var |
| `agentic.mission.id` attribute | ✗ | ✅ from env var |
| `governance.decision` events | ✗ | ✗ (not available via hooks — use Agent SDK) |

### 4.4 Tier 4 — Full Trace Hierarchy (parent-child spans)

For proper parent-child trace trees where `tool.execute` spans are children of `agent.run`, use `otelcli span background`:

```bash
# Before launching Claude Code: start background agent.run span, save trace context
TRACEPARENT=$(otelcli span background start \
  --name "agent.run" \
  --service "$OTEL_SERVICE_NAME" \
  --attrs "gen_ai.agent.id=$AGENT_ID,agentic.layer=$AGENTIC_LAYER,agentic.mission.id=$AGENTIC_MISSION_ID" \
  --endpoint "$OTEL_EXPORTER_OTLP_ENDPOINT" \
  --timeout 30m)
export OTEL_TRACEPARENT="$TRACEPARENT"

# Launch Claude Code — hooks use $OTEL_TRACEPARENT for child spans
claude --print "your task"

# After Claude Code exits: close the parent span
otelcli span background end --endpoint "$OTEL_EXPORTER_OTLP_ENDPOINT"
```

Update the hook scripts to pass `--tp-traceparent "${OTEL_TRACEPARENT:-}"` to each `otelcli span create` call. See [`otelcli` background span docs](https://github.com/equinix-labs/otelcli) for full details.

---

## 5. Claude Agent SDK: Code-Level Instrumentation

When using the Anthropic Python or TypeScript SDK to build agents, you have direct access to the OTel SDK. This enables Tier 3 full trace hierarchy including inference spans.

### 5.1 Python Setup

```bash
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc anthropic
```

### 5.2 Instrumentation Pattern

```python
import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import anthropic

# Initialize OTel
resource = Resource.create({
    "service.name": os.environ["AGENT_ID"],
    "service.version": "1.0.0",
    "deployment.environment.name": os.environ.get("DEPLOYMENT_ENVIRONMENT", "production"),
    "service.namespace": "agentic-enterprise",
})
provider = TracerProvider(resource=resource)
exporter = OTLPSpanExporter(endpoint=os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"])
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Wrap agent invocation in agent.run span
def run_agent(mission_id: str, task: str):
    with tracer.start_as_current_span(
        "agent.run",
        attributes={
            "gen_ai.operation.name": "invoke_agent",
            "gen_ai.provider.name": "anthropic",
            "gen_ai.agent.id": os.environ["AGENT_ID"],
            "agentic.layer": os.environ.get("AGENTIC_LAYER", "execution"),
            "agentic.mission.id": mission_id,
        }
    ) as span:
        client = anthropic.Anthropic()
        # Wrap each tool call in tool.execute spans via your tool-calling loop
        result = client.messages.create(
            model="claude-sonnet-4-6",
            messages=[{"role": "user", "content": task}],
            # ... tools, max_tokens, etc.
        )
        span.set_attribute("gen_ai.usage.input_tokens", result.usage.input_tokens)
        span.set_attribute("gen_ai.usage.output_tokens", result.usage.output_tokens)
        return result
```

### 5.3 Governance Decision Events

Emit `governance.decision` events inside spans when the agent makes an approval/rejection decision:

```python
from opentelemetry import trace

span = trace.get_current_span()
span.add_event("governance.decision", attributes={
    "governance.decision": "approve",     # approve|reject|escalate|delegate
    "governance.reason": "All quality policies pass",
    "governance.pr.number": 142,
})
```

---

## 6. OpenClaw: Environment-Based Instrumentation

OpenClaw supports OTel via standard environment variables. No code changes required — configure before launching the fleet.

### 6.1 Required Configuration

```bash
# Set before launching OpenClaw
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_SERVICE_NAME="openclaw-fleet"
export OTEL_SERVICE_VERSION="1.0.0"
export OTEL_RESOURCE_ATTRIBUTES="deployment.environment.name=production,service.namespace=agentic-enterprise,agentic.layer=execution"

# Optional: disable content capture (privacy default — keep this on)
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"
```

### 6.2 Per-Agent Identity

If OpenClaw supports per-agent configuration, set per-agent resource attributes to distinguish spans by agent role in your dashboards:

```bash
# For the ops-triage agent
export OTEL_RESOURCE_ATTRIBUTES="service.name=cc-ops-triage,agentic.layer=strategy,..."

# For the builder agent
export OTEL_RESOURCE_ATTRIBUTES="service.name=cc-exec-builder,agentic.layer=execution,..."
```

### 6.3 Verify

```bash
# Check that OpenClaw is exporting spans
otelcli status --endpoint "$OTEL_EXPORTER_OTLP_ENDPOINT"
```

---

## 7. OTel Collector on VPS

Running a local OTel Collector on the VPS decouples agent instrumentation from the observability backend. You can fan out to multiple backends and change backends without touching agent configuration.

### 7.1 Option A — Dynatrace OneAgent (recommended if OneAgent is installed)

If Dynatrace OneAgent is running on the host, it acts as a local OTLP receiver. No separate collector needed — OneAgent forwards spans directly to your Dynatrace tenant.

**Endpoint:** `http://localhost:14499/otlp/v1/traces`
**Protocol:** `http/protobuf` (Dynatrace does not support gRPC)
**Authentication:** none required (OneAgent handles auth to DT cloud)
**Signals:** traces only (metrics and logs require Option B)

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:14499/otlp/v1/traces"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
export OTEL_SERVICE_NAMESPACE="agentic-enterprise"
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"
```

> **Prerequisite:** Extension Execution Controller (EEC) must be active on the host. Verify with `systemctl status oneagent` — if OneAgent is running, EEC is typically active by default on Full-Stack deployments.

### 7.2 Option B — Direct Dynatrace API (traces + metrics + logs)

For full signal coverage (traces, metrics, logs) or when OneAgent is not available, export directly to the Dynatrace API. Requires an API token.

**Create token:** Dynatrace tenant → **Access Tokens → Generate token**
Required scopes: `openTelemetryTrace.ingest`, `metrics.ingest`, `logs.ingest`

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="https://<your-env-id>.live.dynatrace.com/api/v2/otlp"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token <your-dt-api-token>"
export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE="DELTA"
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"
```

> **Note:** The environment ID in the endpoint URL uses `.live.dynatrace.com`, not `.apps.dynatrace.com` — even if you access the DT UI via the new platform.

### 7.3 Option C — Generic OTel Collector (vendor-agnostic)

For fanout to multiple backends or when running without Dynatrace, deploy the OTel Collector Contrib:

```yaml
# /opt/otel-collector/docker-compose.yml
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:4318:4318"    # OTLP HTTP — localhost only
    volumes:
      - ./config.yaml:/etc/otel/config.yaml
    command: ["--config=/etc/otel/config.yaml"]
```

```yaml
# /opt/otel-collector/config.yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s

exporters:
  debug:
    verbosity: detailed    # Tier 1: stdout only

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]
```

```bash
cd /opt/otel-collector && docker compose up -d
```

---

## 8. Span Mapping Reference

How the framework's canonical span names (from [`otel-contract.md`](../otel-contract.md)) map to each runtime:

| Span Name | Claude Code | Claude Agent SDK | OpenClaw |
|---|---|---|---|
| `agent.run` | `Stop` hook → `otelcli span create` | `tracer.start_as_current_span("agent.run")` | Emitted natively |
| `tool.execute` | `PostToolUse` hook → `otelcli span create` | Wrap each tool call in a child span | Emitted natively per tool call |
| `agent.subagent.invoke` | `PostToolUse` hook (when `tool_name == "Agent"`) | Explicit child span before subagent call | Emitted natively |
| `git.operation` | `PostToolUse` hook (when `tool_name == "Bash"` and `command` contains `git`/`gh`) | Wrap git subprocess calls | Emitted natively |
| `quality.evaluate` | `PostToolUse` hook (when `tool_name` matches quality eval tool) | Explicit span in quality eval function | Emitted natively |
| `inference.chat` | Not available via hooks | `tracer.start_as_current_span("chat <model>")` | Emitted natively |
| `governance.decision` | Not available via hooks | `span.add_event("governance.decision", ...)` | Configurable |

---

*See also:* [`otel-contract.md`](../otel-contract.md) for canonical span names and attributes, [`otel-architecture.md`](otel-architecture.md) for the observability feedback loop, and [`docs/runtimes/`](../runtimes/) for runtime-specific setup guides.
