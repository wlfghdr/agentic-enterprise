# OTel GenAI Semantic Conventions for Agent Observability

> **Version:** 1.0 | **Last updated:** 2026-03-08
> **Spec reference:** [OTel GenAI Semantic Conventions (Development)](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — verify currency before use
> **Related:** `work/missions/_TEMPLATE-observability-design.md` (full instrumentation design template)

---

## Why This Matters

The Agentic Enterprise template already mandates telemetry emission (AGENTS.md Rule 9a) and telemetry consumption (Rule 9b). What it does **not** yet specify is *which span names and attributes* agents should use when instrumenting LLM calls and agent workflows.

Without a shared convention, teams instrument ad-hoc: `llm.call`, `model_request`, `ai_inference`, `agent_step` — all describing the same operation but producing incompatible traces. No standard tooling (dashboards, cost analyzers, latency p95 alerts, token quota monitors) can aggregate across these.

The OpenTelemetry GenAI Semantic Conventions Working Group has standardized this. Adopting these conventions here produces three concrete advantages:

1. **Tooling compatibility** — Any OTel-native observability platform (Dynatrace, Grafana, Honeycomb, etc.) that supports the GenAI semantic conventions will automatically parse your spans into token cost dashboards, latency histograms, and error rate panels — without custom configuration.
2. **Cross-team comparability** — Teams adopting this template produce comparable traces. Benchmarking, shared dashboards, and fleet-level cost analysis become trivially achievable.
3. **Ecosystem longevity** — The GenAI conventions are on the standards track. Aligning now avoids a painful migration later.

This file is a **quick-reference** for agents and developers. For the full instrumentation design template (span hierarchy, metrics design, SLOs, alerting, dashboard spec), see [`work/missions/_TEMPLATE-observability-design.md`](../work/missions/_TEMPLATE-observability-design.md).

---

## Rule 9a Extension: Standard Span Names and Attributes

Every agent that makes an LLM call **MUST** emit spans conforming to the OTel GenAI conventions described below, in addition to the general span requirements in AGENTS.md Rule 9a.

---

## Span Types

### Agent Spans — `invoke_agent` / `create_agent`

Emitted when an orchestrator invokes or instantiates a downstream agent.

**Span name format:** `{gen_ai.operation.name} {gen_ai.agent.name}`

**Example:**
```
invoke_agent DataAnalysisAgent
```

**Required attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `gen_ai.operation.name` | `invoke_agent` |
| `gen_ai.provider.name` | `openai`, `anthropic`, `aws.bedrock` |
| `gen_ai.agent.name` | `DataAnalysisAgent` |
| `gen_ai.agent.id` | `asst_5j66UpCpwteGg4YSxUnt7lPY` |

**Recommended attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `gen_ai.agent.version` | `1.0.0` |
| `gen_ai.agent.description` | `Analyses sales data and produces summaries` |
| `gen_ai.conversation.id` | `conv_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.request.model` | `gpt-4o` |

---

### Inference (Model) Spans — `chat` / `generate_content`

Emitted once per LLM API call. This is where token usage is recorded.

**Span name format:** `{gen_ai.operation.name} {gen_ai.request.model}`

**Examples:**
```
chat gpt-4o
generate_content gemini-2.0-flash
```

**Required attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `gen_ai.operation.name` | `chat` |
| `gen_ai.provider.name` | `openai` |

**Recommended attributes:**

| Attribute | Example Value | Notes |
|-----------|---------------|-------|
| `gen_ai.request.model` | `gpt-4o` | Model name as requested |
| `gen_ai.response.model` | `gpt-4o-2024-08-06` | Actual model version that responded |
| `gen_ai.usage.input_tokens` | `512` | Prompt tokens consumed |
| `gen_ai.usage.output_tokens` | `256` | Completion tokens generated |
| `gen_ai.usage.cache_read.input_tokens` | `128` | Tokens served from provider cache |
| `gen_ai.response.finish_reasons` | `["stop"]` | Array — why the model stopped |
| `gen_ai.response.id` | `chatcmpl-abc123` | Provider-assigned completion ID |
| `gen_ai.conversation.id` | `conv_5j66UpCpwteGg4YSxUnt7lPY` | Session/thread ID |
| `error.type` | `rate_limit_exceeded` | Set on error spans |

> **Token cost tracking:** `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` are the foundation of all token cost dashboards and quota alerts. These attributes are **non-negotiable** on every inference span. If your SDK does not populate them automatically, set them manually from the model API response.

---

### Tool Call Spans — `execute_tool`

Emitted once per tool invocation requested by the model. Must be a **child span** of the parent inference span.

**Span name format:** `execute_tool {tool_name}`

**Example:**
```
execute_tool search_codebase
execute_tool write_file
execute_tool call_api
```

**Required attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `gen_ai.operation.name` | `execute_tool` |
| `gen_ai.provider.name` | _(the agent framework or tool provider)_ |

**Recommended attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `error.type` | `timeout` | Set if the tool call fails |

---

### Retrieval Spans — `retrieval`

Emitted once per vector store / knowledge base search. Must be a **child span** of the inference or agent span it belongs to.

**Span name format:** `retrieval {store_name}`

**Example:**
```
retrieval pinecone-knowledge-base
retrieval chroma-docs
```

**Required attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `gen_ai.operation.name` | `retrieval` |
| `gen_ai.provider.name` | `pinecone`, `chroma`, `weaviate` |

**Recommended attributes:**

| Attribute | Example Value |
|-----------|---------------|
| `server.address` | `api.pinecone.io` |
| `server.port` | `443` |
| `error.type` | `connection_timeout` |

---

## Full Attribute Reference

The following table consolidates all core OTel GenAI attributes. All are from the [OTel GenAI attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) (status: Development as of 2026-03-08).

| Attribute | Type | Requirement Level | Description | Example |
|-----------|------|-------------------|-------------|---------|
| `gen_ai.operation.name` | string | Required | Operation being performed | `chat`, `invoke_agent`, `execute_tool`, `retrieval`, `create_agent`, `generate_content` |
| `gen_ai.provider.name` | string | Required | GenAI provider identifier | `openai`, `anthropic`, `aws.bedrock`, `azure.ai.openai`, `gcp.gemini` |
| `gen_ai.agent.name` | string | Cond. Required (agent spans) | Human-readable agent name | `DataAnalysisAgent` |
| `gen_ai.agent.id` | string | Cond. Required (agent spans) | Unique agent instance identifier | `asst_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.agent.version` | string | Recommended | Agent version | `1.0.0` |
| `gen_ai.agent.description` | string | Recommended | Agent description | `Analyses sales data` |
| `gen_ai.request.model` | string | Cond. Required (if available) | Requested model name | `gpt-4o`, `claude-3-5-sonnet-20241022` |
| `gen_ai.response.model` | string | Recommended | Model that generated the response | `gpt-4o-2024-08-06` |
| `gen_ai.usage.input_tokens` | int | Recommended | Prompt tokens used | `512` |
| `gen_ai.usage.output_tokens` | int | Recommended | Completion tokens generated | `256` |
| `gen_ai.usage.cache_read.input_tokens` | int | Recommended | Input tokens from cache | `128` |
| `gen_ai.usage.cache_creation.input_tokens` | int | Recommended | Input tokens written to cache | `64` |
| `gen_ai.response.finish_reasons` | string[] | Recommended | Why the model stopped | `["stop"]`, `["length"]` |
| `gen_ai.response.id` | string | Recommended | Provider completion ID | `chatcmpl-abc123` |
| `gen_ai.conversation.id` | string | Cond. Required (if available) | Session/thread ID | `conv_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.output.type` | string | Cond. Required (if applicable) | Requested output type | `text`, `json`, `image` |
| `error.type` | string | Cond. Required (on error) | Error class | `timeout`, `rate_limit_exceeded`, `500` |
| `server.address` | string | Recommended | GenAI server hostname | `api.openai.com` |
| `server.port` | int | Cond. Required (if server.address set) | GenAI server port | `443` |

---

## Span Hierarchy Example

A minimal orchestrator → agent → model → tool call workflow produces this trace:

```
invoke_agent OrchestratorAgent                    ← INTERNAL span (entry point)
  └── invoke_agent DataAnalysisAgent              ← CLIENT span (remote agent)
        ├── chat gpt-4o                           ← CLIENT span (LLM call)
        │     gen_ai.usage.input_tokens: 512
        │     gen_ai.usage.output_tokens: 256
        │     gen_ai.response.finish_reasons: ["tool_calls"]
        │     └── execute_tool search_codebase    ← CLIENT span (tool call)
        │           └── [HTTP span to search API]
        └── chat gpt-4o                           ← CLIENT span (second turn)
              gen_ai.usage.input_tokens: 768
              gen_ai.usage.output_tokens: 312
              gen_ai.response.finish_reasons: ["stop"]
```

**Span kind:** Use `CLIENT` for any remote call (model API, remote agent, remote tool). Use `INTERNAL` for in-process operations.

**Trace context propagation:** Use W3C Trace Context (`traceparent` / `tracestate` headers) across all HTTP boundaries. Inject/extract manually if the framework doesn't support auto-instrumentation.

---

## Standard Metrics

In addition to spans, agents making LLM calls **SHOULD** emit these two standard OTel GenAI metrics. They are the basis for cost dashboards and latency SLOs:

| Metric Name | Instrument | Unit | Key Dimensions |
|-------------|-----------|------|----------------|
| `gen_ai.client.token.usage` | Histogram | `{token}` | `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.token.type` (`input`/`output`), `gen_ai.request.model` |
| `gen_ai.client.operation.duration` | Histogram | `s` | `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model` |

Emit once per inference span. See the full [OTel GenAI Metrics spec](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/) for bucket boundaries and additional dimensions.

---

## Instrumentation Checklist

Use this as a PR-level quality gate when adding or modifying agent LLM calls:

- [ ] Every agent invocation has an `invoke_agent` span with `gen_ai.agent.name` and `gen_ai.agent.id`
- [ ] Every LLM call has a `chat` (or `generate_content`) span
- [ ] `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` populated on every inference span
- [ ] Every tool call has an `execute_tool` child span under the inference span
- [ ] Every retrieval has a `retrieval` span
- [ ] `gen_ai.conversation.id` propagated through all spans belonging to the same session
- [ ] `error.type` set and span status set to ERROR on all failure paths
- [ ] Trace context (`traceparent`) propagated across all network boundaries
- [ ] `gen_ai.client.token.usage` metric emitted per inference operation
- [ ] `gen_ai.client.operation.duration` metric emitted per inference operation

---

## Relationship to Other Templates

| File | Purpose |
|------|---------|
| `AGENTS.md Rule 9` | Mandate: all agents MUST emit OTel spans (what to do) |
| **This file** | Standard: which span names and attributes to use (how to do it) |
| `work/missions/_TEMPLATE-observability-design.md` | Full design template: span hierarchy, metrics, SLOs, dashboards, alerting for a complete mission |
| `org/integrations/` | Integration Registry: where spans are exported (OTLP endpoint config) |

---

## Further Reading

- [OTel GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OTel GenAI Span spec](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/)
- [OTel GenAI Agent Span spec](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/)
- [OTel GenAI Metrics spec](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/)
- [OTel GenAI Attribute Registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
