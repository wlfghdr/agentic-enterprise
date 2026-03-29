# Canonical OTel Telemetry Contract

> **Version:** 1.3 | **Last updated:** 2026-03-29
> **Status:** Active — single source of truth for all agent telemetry
> **Supersedes:** inline attribute lists in `AGENTS.md` Rule 9a, `org/4-quality/policies/observability.md` Agent Observability section, and `org/integrations/categories/observability.md` semantic conventions section
> **Spec references:**
> - [OTel GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) (Development)
> - [OTel GenAI Agent Spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/)
> - [OTel Resource Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/resource/)
> - [OTel General Attribute Registry](https://opentelemetry.io/docs/specs/semconv/general/attributes/)

This is the canonical telemetry contract.
Use it for:
- canonical span names
- required attributes and metrics
- migration/deprecation decisions
- machine-checkable validation targets

Read it in two modes:
- **Operator / implementer path:** Design Principles, Span Naming, required GenAI attributes, Standard Metrics, Privacy defaults
- **Reference path:** mapping table, migration policy, schema appendix

---

## Design Principles

1. **OTel-first, custom-only-when-necessary.** Standard OpenTelemetry and OTel GenAI semantic conventions win by default. Custom `agentic.*` or `governance.*` attributes are used only where OTel has no suitable field.
2. **Single source of truth.** All attribute lists, span names, resource attributes, and event definitions live here. Other files reference this document; they do not repeat or diverge from it.
3. **Tooling compatibility.** Any OTel-native platform supporting GenAI conventions must be able to parse and visualize spans without custom configuration.
4. **Privacy by default.** Content capture (prompts, completions, tool inputs/outputs) is **off by default** and must be explicitly opted in.
5. **Forward compatibility.** OTel GenAI semantic conventions are in active development. This contract includes a migration policy so adopters can track upstream evolution without breaking existing instrumentation.

---

## Fast Path

If you only need the minimum to instrument correctly, implement these first:
1. Resource attributes in Section 1
2. canonical span names in Section 2
3. required GenAI attributes in Section 3.1
4. standard metrics in Section 7
5. privacy defaults in Section 8

Use the later sections mainly as reference and migration support.

---

## 1. Resource Attributes

Resource attributes describe **the service/agent process** and are set once at SDK initialization — not on individual spans. They are separate from span attributes.

### Required Resource Attributes

| Attribute | Type | Description | Example |
|-----------|------|-------------|---------|
| `service.name` | string | Logical name of the agent or service | `orchestration-agent`, `execution-agent` |
| `service.version` | string | Deployed version of the agent | `3.1.0` |
| `deployment.environment.name` | string | Deployment environment | `production`, `staging`, `development` |

### Recommended Resource Attributes

| Attribute | Type | Description | Example |
|-----------|------|-------------|---------|
| `service.instance.id` | string | Unique instance identifier | `agent-pod-abc123` |
| `service.namespace` | string | Logical grouping | `agentic-enterprise` |
| `telemetry.sdk.name` | string | SDK used (auto-populated) | `opentelemetry` |
| `telemetry.sdk.version` | string | SDK version (auto-populated) | `1.29.0` |

> **Why resource attributes are separate:** Resource attributes describe *who is emitting*, not *what happened*. OTel backends use them for filtering and grouping, not trace correlation. Do not repeat resource attributes on individual spans.

---

## 2. Span Naming Conventions

All agentic-enterprise span names use a fixed vocabulary. Non-standard span names will not be parseable by fleet dashboards or the OTel compliance check.

### Canonical Span Names

| Span Name | When to Emit | OTel Span Kind |
|-----------|-------------|----------------|
| `agent.run` | One full agent invocation / task turn | `INTERNAL` (if in-process) or `SERVER` (if remote-invoked) |
| `agent.subagent.invoke` | Orchestrator dispatching to a downstream agent | `CLIENT` |
| `tool.execute` | Single tool call (MCP, API, file, Git) | `CLIENT` |
| `quality.evaluate` | Quality layer policy evaluation | `INTERNAL` |
| `git.operation` | Any Git action (commit, push, PR open/merge) | `CLIENT` |
| `mission.transition` | Mission state change | `INTERNAL` |
| `inference.chat` | LLM inference call (`chat` operation) | `CLIENT` |
| `inference.generate` | LLM inference call (`generate_content` operation) | `CLIENT` |
| `retrieval` | Vector store / knowledge base search | `CLIENT` |

> **For LLM inference spans:** The OTel GenAI spec defines the span name format `{gen_ai.operation.name} {gen_ai.request.model}` (e.g. `chat gpt-4o`). Use this OTel format as the span name (e.g. `chat gpt-4o`, `generate_content gemini-2.0-flash`) rather than `inference.chat` or `inference.generate` for pure inference spans — it produces better compatibility with OTel GenAI tooling. The names `inference.chat` and `inference.generate` in the table above are canonical identifiers for referring to these span types in documentation and dashboards, and are used as span names only when the model is not yet known at span creation time.

---

## 3. Standard OTel and GenAI Attributes

These are **standard attributes from the OpenTelemetry semantic conventions registry**. Use them as-is. Do not create custom aliases or parallel fields.

### 3.1 OTel GenAI — Required on LLM / Agent Spans

| Attribute | Type | Requirement Level | Span Type | Description | Example |
|-----------|------|-------------------|-----------|-------------|---------|
| `gen_ai.operation.name` | string | Required | inference, agent | Operation performed | `chat`, `invoke_agent`, `execute_tool`, `generate_content`, `retrieval` |
| `gen_ai.provider.name` | string | Required | inference, agent | GenAI provider | `openai`, `anthropic`, `aws.bedrock`, `azure.ai.openai`, `gcp.gemini` |
| `gen_ai.agent.name` | string | Cond. Required (agent spans) | agent | Human-readable agent name | `DataAnalysisAgent` |
| `gen_ai.agent.id` | string | Cond. Required (agent spans) | agent | Unique agent instance ID | `asst_5j66abc` |
| `gen_ai.request.model` | string | Cond. Required (if available) | inference | Requested model | `gpt-4o`, `claude-3-5-sonnet-20241022` |
| `gen_ai.usage.input_tokens` | int | Required | inference | Prompt tokens consumed | `512` |
| `gen_ai.usage.output_tokens` | int | Required | inference | Completion tokens generated | `256` |

### 3.2 OTel GenAI — Recommended

| Attribute | Type | Span Type | Description | Example |
|-----------|------|-----------|-------------|---------|
| `gen_ai.response.model` | string | inference | Actual model that responded | `gpt-4o-2024-08-06` |
| `gen_ai.usage.cache_read.input_tokens` | int | inference | Tokens from provider cache | `128` |
| `gen_ai.response.finish_reasons` | string[] | inference | Why model stopped | `["stop"]`, `["tool_calls"]` |
| `gen_ai.response.id` | string | inference | Provider completion ID | `chatcmpl-abc123` |
| `gen_ai.conversation.id` | string | inference, agent | Session / thread correlation ID | `conv_5j66abc` |
| `gen_ai.agent.version` | string | agent | Agent version | `1.0.0` |
| `gen_ai.agent.description` | string | agent | Agent description | `Analyses sales data` |
| `gen_ai.output.type` | string | inference | Requested output type | `text`, `json` |

### 3.3 Standard OTel General Attributes

| Attribute | Type | Requirement Level | Description | Example |
|-----------|------|-------------------|-------------|---------|
| `error.type` | string | Cond. Required (on error) | Error class; set when span status = ERROR | `rate_limit_exceeded`, `timeout`, `500` |
| `server.address` | string | Recommended | GenAI / tool server hostname | `api.openai.com` |
| `server.port` | int | Cond. Required (if server.address set) | GenAI / tool server port | `443` |

---

## 4. Custom Agentic-Enterprise Attributes

These attributes have **no suitable OTel GenAI standard equivalent** as of this contract version. They are prefixed with `agentic.*` or `governance.*` to distinguish them clearly from standard OTel fields.

> **Rule:** Before adding a new custom attribute, verify that OTel semantic conventions do not already cover it. If OTel adds a standard equivalent, migrate to the standard field and deprecate the custom one per the policy in [Section 10](#10-semconv-stability-and-migration-policy).

### 4.1 Agentic-Enterprise Span Attributes

| Attribute | Type | Requirement Level | Description | Example |
|-----------|------|-------------------|-------------|---------|
| `agentic.layer` | string | Required on `agent.run` | Operating model layer | `steering`, `strategy`, `orchestration`, `execution`, `quality` |
| `agentic.mission.id` | string | Required on `agent.run` | Mission being executed | `MSN-2026-042` |
| `agentic.division` | string | Cond. Required (execution layer) | Execution division | `software-engineering` |
| `agentic.loop` | string | Recommended | Active operating loop | `discover`, `build`, `ship`, `operate` |
| `agentic.task.id` | string | Recommended | Task within the mission | `TSK-2026-042-03` |
| `agentic.session.id` | string | Recommended | Agent session / run correlation | `session_abc123` |
| `agentic.artifact.path` | string | Recommended on `git.operation` | Affected file path | `org/3-execution/divisions/eng/AGENT.md` |

### 4.2 Governance Attributes

| Attribute | Type | Requirement Level | Description | Example |
|-----------|------|-------------------|-------------|---------|
| `governance.decision` | string | Required on decision events | Decision made | `approve`, `reject`, `escalate`, `delegate` |
| `governance.reason` | string | Required on decision events | Rationale | `Policy violation: no observability design` |
| `governance.pr.number` | int | Cond. Required (if applicable) | Associated PR | `142` |

### 4.3 Tool and Quality Attributes

| Attribute | Type | Span Type | Description | Example |
|-----------|------|-----------|-------------|---------|
| `tool.name` | string | `tool.execute` | Tool identifier | `search_codebase`, `write_file`, `mcp.github` |
| `tool.type` | string | `tool.execute` | Tool category | `function`, `mcp`, `api`, `git`, `workflow` |
| `tool.call.id` | string | `tool.execute` | Call correlation ID | `call_abc123` |
| `quality.policy.id` | string | `quality.evaluate` | Policy being evaluated | `observability`, `security`, `architecture` |
| `quality.verdict` | string | `quality.evaluate` | Evaluation result | `pass`, `fail`, `needs_changes` |
| `git.operation` | string | `git.operation` | Git operation type | `branch_create`, `commit`, `push`, `pr_open`, `pr_comment`, `merge` |
| `git.pr.number` | int | `git.operation` | PR number if applicable | `142` |
| `git.branch` | string | `git.operation` | Branch name | `copilot/feature-xyz` |
| `git.repo` | string | `git.operation` | Repository identifier | `wlfghdr/agentic-enterprise` |
| `mission.status.from` | string | `mission.transition` | Previous mission status | `in-progress` |
| `mission.status.to` | string | `mission.transition` | New mission status | `completed` |
| `mission.phase` | string | `mission.transition` | Mission lifecycle phase | `build`, `ship` |

---

## 5. Span Hierarchy Example

This section is illustrative. It helps operators and implementers visualize the contract, but the normative requirements remain in the attribute and metric sections.

A minimal orchestrator → agent → model → tool call trace:

```
agent.run OrchestratorAgent                         ← INTERNAL (entry point)
  agentic.layer: orchestration
  agentic.mission.id: MSN-2026-042
  gen_ai.agent.name: OrchestratorAgent
  gen_ai.agent.id: agent_orch_001
  │
  └── agent.subagent.invoke DataAnalysisAgent       ← CLIENT
        gen_ai.operation.name: invoke_agent
        gen_ai.provider.name: anthropic
        gen_ai.agent.name: DataAnalysisAgent
        gen_ai.agent.id: agent_data_001
        gen_ai.conversation.id: conv_abc123
        │
        ├── inference.chat claude-3-5-sonnet         ← CLIENT
        │     gen_ai.operation.name: chat
        │     gen_ai.provider.name: anthropic
        │     gen_ai.request.model: claude-3-5-sonnet-20241022
        │     gen_ai.usage.input_tokens: 512
        │     gen_ai.usage.output_tokens: 256
        │     gen_ai.response.finish_reasons: ["tool_calls"]
        │     gen_ai.conversation.id: conv_abc123
        │     │
        │     └── tool.execute search_codebase       ← CLIENT
        │           tool.name: search_codebase
        │           tool.type: mcp
        │           tool.call.id: call_xyz789
        │
        └── inference.chat claude-3-5-sonnet         ← CLIENT
              gen_ai.usage.input_tokens: 768
              gen_ai.usage.output_tokens: 312
              gen_ai.response.finish_reasons: ["stop"]
```

**Trace context propagation:** Inject W3C `traceparent` / `tracestate` headers across all HTTP boundaries. Extract on the receiving side. If your framework does not auto-instrument this, set headers manually.

**Quality evaluation trace:**
```
quality.evaluate observability                      ← INTERNAL
  quality.policy.id: observability
  quality.verdict: fail
  governance.decision: reject
  governance.reason: Missing token usage on inference spans
  governance.pr.number: 142
```

**Git operation trace:**
```
git.operation pr_open                               ← CLIENT
  git.operation: pr_open
  git.pr.number: 142
  git.branch: copilot/feature-xyz
  git.repo: wlfghdr/agentic-enterprise
  agentic.mission.id: MSN-2026-042
```

---

## 6. Span Events - Native vs Derived

### 6.1 Native OTel Span Events

Native span events are attached directly to spans using the OTel SDK `span.add_event()` API. They are part of the trace and stored in the OTLP backend alongside spans.

Use native span events for:

| Event Name | Parent Span | Required Attributes |
|------------|------------|---------------------|
| `governance.decision` | `agent.run`, `quality.evaluate` | `governance.decision`, `governance.reason`, `governance.pr.number` (if applicable) |
| `agent.escalation` | `agent.run` | `governance.reason`, `agentic.layer` |
| `tool.error` | `tool.execute` | `error.type`, `tool.name` |
| `policy.violation` | `quality.evaluate` | `quality.policy.id`, `governance.reason` |
| `mission.status_change` | `mission.transition` | `mission.status.from`, `mission.status.to` |

### 6.2 Derived Events

Derived events are produced by the observability platform by processing span data — they are **not emitted directly by agents**. They feed dashboards, governance UIs, and signal pipelines.

| Derived Event | Source Span / Event | Produced By |
|--------------|---------------------|-------------|
| `governance.pr.opened` | Git webhook → `git.operation` span | Platform event pipeline |
| `governance.pr.merged` | Git webhook → `git.operation` span | Platform event pipeline |
| `governance.pr.rejected` | Git webhook → `git.operation` span | Platform event pipeline |
| `release.tagged` | Git tag webhook | Platform event pipeline |
| `agent.fleet.anomaly` | `gen_ai.client.token.usage` metric | Platform anomaly detection |
| `mission.slo_breach` | `gen_ai.client.operation.duration` metric | Platform SLO engine |

> **Rule:** Agents emit native span events. The observability platform produces derived events. Do not conflate the two. If a governance decision needs to be observable, emit a native span event on the relevant span — do not try to push a derived event directly.

### 6.3 Trace Context in Derived Records and UI Correlation

When traces are rendered in downstream dashboards or command-center UIs, correlation happens through the platform-exposed trace context identifiers attached to derived records:

| Identifier | Source | Use |
|-----------|--------|-----|
| `trace.id` | OTel trace context | Primary join key from an activity record to the full distributed trace |
| `span.id` | OTel span context | Optional deep-link to the specific span that produced the record |
| `parent.span.id` | OTel parent span context | Optional breadcrumb for reconstructing local hierarchy in flattened views |

Rules:

1. **Do not duplicate trace context as custom span attributes.** OTel already carries trace and span identifiers in context. Emit spans normally and let the backend expose `trace.id` / `span.id` on derived records and query results.
2. **Use dotted names in derived records when the platform supports them.** Prefer `trace.id`, `span.id`, and `parent.span.id` over ad-hoc aliases like `trace_id` and `span_id`.
3. **If a downstream ingest path cannot preserve dotted field names, map them losslessly at the edge and document the mapping.** The canonical names remain `trace.id`, `span.id`, and `parent.span.id`.
4. **UI correlation should start from `trace.id`.** `span.id` is a secondary precision key for linking an activity entry to a specific span in a waterfall or trace viewer.

This rule exists specifically to support observability surfaces such as agent command centers: spans remain the source of truth, while flattened activity/event records remain trace-linkable without introducing a second telemetry schema.

### 6.4 Collaboration and Deliberation Events

Multi-agent systems implementing collaboration memory or structured deliberation emit these native span events. Namespaces align with OTel emerging agent semantic conventions (`agent.collaboration.*`, `agent.deliberation.*`) to avoid collision and ensure forward compatibility.

#### Collaboration Events (agent interaction telemetry)

Emit on the `agent.run` span of the agent whose state is being updated.

| Event Name | Required Attributes | Description |
|------------|---------------------|-------------|
| `agent.collaboration.memory_update` | `agent.collaboration.source_agent`, `agent.collaboration.target_agent`, `agent.collaboration.signal_type`, `agent.collaboration.score_delta`, `agent.collaboration.score_after` | Emitted when an agent's collaboration memory scores change |
| `agent.collaboration.signal` | `agent.collaboration.source_agent`, `agent.collaboration.target_agent`, `agent.collaboration.signal_type`, `agent.collaboration.signal_weight` | Raw interaction signal recorded |
| `agent.collaboration.exploration_override` | `agent.collaboration.source_agent`, `agent.collaboration.target_agent` | Agent's exploration mechanism overrode normal memory-guided behavior |

**Collaboration attribute definitions:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `agent.collaboration.source_agent` | string | `agent.id` of the agent that initiated the interaction |
| `agent.collaboration.target_agent` | string | `agent.id` of the agent that was addressed or referenced |
| `agent.collaboration.signal_type` | string (enum) | One of: `mention`, `idea_building`, `challenge`, `human_reaction`, `synthesis_inclusion` |
| `agent.collaboration.signal_weight` | double | Numeric weight of the signal (policy-defined scale) |
| `agent.collaboration.score_delta` | double | Score change from this update |
| `agent.collaboration.score_after` | double | Collaboration score after the update |

> **Privacy note:** Agent names and score values are operational metadata, not PII. Human reactions are attributed to a generic `human` role, not to a named individual.

> **Cardinality note:** `source_agent × target_agent` is bounded by team size (typically < 15 agents); safe as metric dimensions.

#### Deliberation Events (structured multi-agent deliberation telemetry)

Emit on the `agent.run` span of the deliberation coordinator or convergence judge.

| Event Name | Required Attributes | Description |
|------------|---------------------|-------------|
| `agent.deliberation.phase_transition` | `agent.deliberation.phase`, `agent.deliberation.turns_used` | Phase changed (e.g. exploration → critique → synthesis) |
| `agent.deliberation.convergence_check` | `agent.deliberation.phase`, `agent.deliberation.confidence`, `agent.deliberation.turns_used`, `agent.deliberation.turns_budget` | Convergence judge evaluated group progress |
| `agent.deliberation.synthesis_generated` | `agent.deliberation.phase`, `agent.deliberation.turns_used` | Synthesis artifact was produced |
| `agent.deliberation.budget_exhausted` | `agent.deliberation.phase`, `agent.deliberation.turns_used`, `agent.deliberation.turns_budget` | Hard budget cap forced deliberation closure |

**Deliberation attribute definitions:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `agent.deliberation.phase` | string | Current deliberation phase name (e.g. `exploration`, `critique`, `synthesis`) |
| `agent.deliberation.confidence` | double | Convergence confidence score (0.0–1.0) |
| `agent.deliberation.turns_used` | int | Turns consumed in the current phase |
| `agent.deliberation.turns_budget` | int | Turn ceiling for the current phase |
| `agent.deliberation.extension_used` | boolean | Whether a one-shot extension was consumed |

#### Participation Quality Metrics

These are standard OTel metrics (Histogram or Gauge) emitted by agents implementing collaboration memory. Use **delta temporality** (required for Dynatrace).

| Metric | Instrument | Unit | Required Dimensions | Description |
|--------|-----------|------|---------------------|-------------|
| `agent.collaboration.score` | Gauge | `{score}` | `agent.collaboration.source_agent`, `agent.collaboration.target_agent` | Current collaboration score per source-target pair |
| `agent.deliberation.convergence_rate` | Histogram | `{ratio}` | `agent.deliberation.phase` | Turns-to-convergence / budget (lower = faster) |
| `agent.deliberation.challenge_ratio` | Histogram | `{ratio}` | `agent.deliberation.phase` | Fraction of turns containing genuine challenge |

> **Namespace rationale:** `agent.collaboration.*` and `agent.deliberation.*` are chosen to align with OTel's emerging multi-agent namespace rather than ad-hoc prefixes. If OTel stabilizes a different canonical namespace, this contract will migrate and issue a deprecation notice per Section 10.

> **Cross-reference:** See issue [agentic-enterprise#231](https://github.com/wlfghdr/agentic-enterprise/issues/231) for the original proposal and OTel alignment notes. For ACC read paths consuming these events, see [agent-command-center#89](https://github.com/wlfghdr/agent-command-center/issues/89) (Participation Quality Trends) and [agent-command-center#90](https://github.com/wlfghdr/agent-command-center/issues/90) (Collaboration Mesh).

---

## 7. Standard Metrics

Agents making LLM calls **MUST** emit these OTel GenAI standard metrics. They are required for cost dashboards and latency SLOs.

| Metric | Instrument | Unit | Required Dimensions |
|--------|-----------|------|---------------------|
| `gen_ai.client.token.usage` | Histogram | `{token}` | `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.token.type` (`input`/`output`), `gen_ai.request.model` |
| `gen_ai.client.operation.duration` | Histogram | `s` | `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model` |

See [OTel GenAI Metrics spec](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/) for bucket boundaries and additional optional dimensions.

---

## 8. Privacy and Content Capture Defaults

### 8.1 Default Behavior

**Content capture is OFF by default.** The following data MUST NOT be captured in telemetry unless explicitly opted in:

- LLM prompt content (system prompt, user messages)
- LLM completion content (model responses)
- Tool call inputs and outputs
- Retrieved document content

### 8.2 Opt-In Configuration

Content capture is enabled at the deployment level via `CONFIG.yaml → observability.content_capture`:

```yaml
observability:
  content_capture:
    enabled: false           # off by default
    include_prompts: false
    include_completions: false
    include_tool_inputs: false
    include_tool_outputs: false
```

When enabled, the following rules apply:

### 8.3 Redaction Rules

| Content Type | Rule |
|-------------|------|
| API keys, tokens, credentials | Always redacted — never captured |
| PII (names, emails, IDs) | Redacted unless deployment policy explicitly permits |
| Prompt content | Truncated to `max_content_length` (default: 1000 chars) |
| Completion content | Truncated to `max_content_length` (default: 1000 chars) |
| Tool outputs | Truncated to `max_tool_output_length` (default: 500 chars) |

### 8.4 Sensitivity Limits

| Field | Max Length (chars) | Config Key |
|-------|--------------------|------------|
| Prompt text | 1000 | `observability.content_capture.max_content_length` |
| Completion text | 1000 | `observability.content_capture.max_content_length` |
| Tool input | 500 | `observability.content_capture.max_tool_output_length` |
| Tool output | 500 | `observability.content_capture.max_tool_output_length` |
| Attribute string (any field) | 2048 | OTel SDK limit |

> **Audit note:** The telemetry emission mandate (AGENTS.md Rule 9a) is not weakened by these defaults. Every *action* must be observable (span emitted, duration recorded, outcome set). It is the *content* of actions that defaults to off.

---

## 9. Canonical Mapping and Deprecation Table

The following table documents migration decisions for all legacy attribute names that appear in existing repo files. The **Canonical Name** column is the authoritative field going forward.

| Legacy Field | Canonical Name | Source of Legacy | Migration Decision | Status |
|-------------|----------------|-----------------|-------------------|--------|
| `agent.name` | `gen_ai.agent.name` | AGENTS.md Rule 9a | **Migrate.** OTel GenAI has a direct equivalent. Remove `agent.name` from all new instrumentation. | ⚠️ Deprecated |
| `agent.mission_id` | `agentic.mission.id` | AGENTS.md Rule 9a | **Rename.** `agentic.*` prefix standardizes custom attribute namespace. | ⚠️ Deprecated |
| `agent.tool` | `tool.name` | AGENTS.md Rule 9a | **Rename.** More specific; aligns with `tool.*` attribute group. | ⚠️ Deprecated |
| `agent.model` | `gen_ai.request.model` | AGENTS.md Rule 9a | **Migrate.** OTel GenAI has a direct equivalent. | ⚠️ Deprecated |
| `agent.token_usage.input` | `gen_ai.usage.input_tokens` | AGENTS.md Rule 9a | **Migrate.** OTel GenAI standard — use it directly. | ⚠️ Deprecated |
| `agent.token_usage.output` | `gen_ai.usage.output_tokens` | AGENTS.md Rule 9a | **Migrate.** OTel GenAI standard — use it directly. | ⚠️ Deprecated |
| `agent.layer` | `agentic.layer` | AGENTS.md Rule 9a, observability.md | **Rename.** `agentic.*` prefix for custom attributes. | ⚠️ Deprecated |
| `agent.role` | `gen_ai.agent.description` (partial) | observability policy | **Assess.** If role is a structured type, use `agentic.layer`. If it's freeform, use `gen_ai.agent.description`. Field retired. | 🗑️ Removed |
| `agent.decision` | `governance.decision` (span event) | observability policy | **Migrate.** Emit as a native span event attribute, not a span attribute. | ⚠️ Deprecated |
| `agent.type` | `gen_ai.agent.name` (primary) + `agentic.layer` (secondary) | integrations/categories/observability.md | **Decompose.** `agent.type` conflates name and layer. Use the two canonical fields instead. | 🗑️ Removed |
| `mission.id` | `agentic.mission.id` | integrations/categories/observability.md | **Rename.** Aligns with `agentic.*` namespace. | ⚠️ Deprecated |
| `loop` | `agentic.loop` | integrations/categories/observability.md | **Rename.** `agentic.*` prefix for all framework-specific attributes. | ⚠️ Deprecated |
| `agent.division` | `agentic.division` | integrations/categories/observability.md | **Rename.** `agentic.*` prefix. | ⚠️ Deprecated |
| `pr.number` | `governance.pr.number` | integrations/categories/observability.md | **Rename.** Groups with other governance attributes. | ⚠️ Deprecated |

**Status legend:**
- ⚠️ **Deprecated** — supported in existing deployments; must be replaced in all new instrumentation; removed in next major version
- 🗑️ **Removed** — do not use; no replacement obligation for old spans

---

## 10. Semconv Stability and Migration Policy

OTel GenAI semantic conventions are **Development status** as of 2026-03-08. They will evolve.

### Stability Labels

| OTel Stability | Meaning for This Contract |
|---------------|--------------------------|
| `Stable` | Use unconditionally. No migration expected. |
| `Development` | Use now; expect possible breaking changes. Track upstream. |
| `Experimental` | Evaluate before adopting. Require explicit exception in this contract. |

### Migration Triggers

When any of the following occur, open a PR to update this contract within 30 days:

1. An OTel GenAI attribute used here moves to `Stable` — confirm naming and type are unchanged.
2. An OTel GenAI attribute is renamed or removed — update the deprecation table above and update all canonical names.
3. OTel adds a standard equivalent for a custom `agentic.*` attribute — migrate and deprecate the custom field.
4. A new OTel GenAI span type is added that supersedes an agentic-enterprise span name — add a mapping and migration entry.

### Monitoring Upstream

- **Source:** [OTel Semantic Conventions changelog](https://github.com/open-telemetry/semantic-conventions/blob/main/CHANGELOG.md)
- **Scope:** Track `gen-ai/` and `registry/attributes/gen-ai/` paths
- **Owner:** Whoever files the signal to update this contract (any layer agent may file the signal)

### Version Tracking

This contract tracks the OTel GenAI spec version it was validated against:

| Contract Version | OTel GenAI Spec Version | Validated Date |
|-----------------|------------------------|----------------|
| 1.2 | Development (2026-03-09 snapshot) | 2026-03-09 |

---

## 11. Machine-Readable Schema Appendix

This section is primarily for validators, CI, and tooling authors. Most operators can stop after Sections 1-10 unless they are implementing or extending automated checks.

The following YAML schema defines the minimum required span structure for automated validation. CI tools may parse this to enforce contract compliance.

```yaml
# agentic-enterprise OTel Contract — Machine-Readable Schema
# Version: 1.0
# Format: Declarative span contract for linting and test harness use.

resource_attributes:
  required:
    - name: service.name
      type: string
    - name: service.version
      type: string
    - name: deployment.environment.name
      type: string
  recommended:
    - name: service.instance.id
      type: string
    - name: service.namespace
      type: string

span_types:
  - name: agent.run
    kind: INTERNAL
    required_attributes:
      - name: gen_ai.agent.name
        type: string
        source: otel_genai
      - name: gen_ai.agent.id
        type: string
        source: otel_genai
      - name: agentic.layer
        type: string
        enum: [steering, strategy, orchestration, execution, quality]
        source: custom
      - name: agentic.mission.id
        type: string
        source: custom
    recommended_attributes:
      - name: agentic.session.id
        type: string
      - name: agentic.loop
        type: string
        enum: [discover, build, ship, operate]

  - name: agent.subagent.invoke
    kind: CLIENT
    required_attributes:
      - name: gen_ai.operation.name
        type: string
        value: invoke_agent
        source: otel_genai
      - name: gen_ai.provider.name
        type: string
        source: otel_genai
      - name: gen_ai.agent.name
        type: string
        source: otel_genai
      - name: gen_ai.agent.id
        type: string
        source: otel_genai

  - name: inference.chat
    kind: CLIENT
    required_attributes:
      - name: gen_ai.operation.name
        type: string
        value: chat
        source: otel_genai
      - name: gen_ai.provider.name
        type: string
        source: otel_genai
      - name: gen_ai.usage.input_tokens
        type: int
        source: otel_genai
      - name: gen_ai.usage.output_tokens
        type: int
        source: otel_genai
    recommended_attributes:
      - name: gen_ai.request.model
        type: string
      - name: gen_ai.response.model
        type: string
      - name: gen_ai.conversation.id
        type: string
      - name: gen_ai.response.finish_reasons
        type: string[]

  - name: inference.generate
    kind: CLIENT
    required_attributes:
      - name: gen_ai.operation.name
        type: string
        value: generate_content
        source: otel_genai
      - name: gen_ai.provider.name
        type: string
        source: otel_genai
      - name: gen_ai.usage.input_tokens
        type: int
        source: otel_genai
      - name: gen_ai.usage.output_tokens
        type: int
        source: otel_genai

  - name: tool.execute
    kind: CLIENT
    required_attributes:
      - name: tool.name
        type: string
        source: custom
      - name: tool.type
        type: string
        enum: [function, mcp, api, git, workflow]
        source: custom
    recommended_attributes:
      - name: tool.call.id
        type: string
      - name: error.type
        type: string

  - name: quality.evaluate
    kind: INTERNAL
    required_attributes:
      - name: quality.policy.id
        type: string
        source: custom
      - name: quality.verdict
        type: string
        enum: [pass, fail, needs_changes]
        source: custom

  - name: git.operation
    kind: CLIENT
    required_attributes:
      - name: git.operation
        type: string
        enum: [branch_create, commit, push, pr_open, pr_comment, merge, tag]
        source: custom
    recommended_attributes:
      - name: git.pr.number
        type: int
      - name: git.branch
        type: string
      - name: git.repo
        type: string
      - name: agentic.mission.id
        type: string

  - name: mission.transition
    kind: INTERNAL
    required_attributes:
      - name: mission.status.from
        type: string
        source: custom
      - name: mission.status.to
        type: string
        source: custom
    recommended_attributes:
      - name: mission.phase
        type: string
        enum: [discover, build, ship, operate]
      - name: agentic.mission.id
        type: string

span_events:
  - name: governance.decision
    required_attributes:
      - governance.decision
      - governance.reason
    optional_attributes:
      - governance.pr.number

  - name: agent.escalation
    required_attributes:
      - governance.reason
      - agentic.layer

  - name: tool.error
    required_attributes:
      - error.type
      - tool.name

  - name: policy.violation
    required_attributes:
      - quality.policy.id
      - governance.reason

  - name: mission.status_change
    required_attributes:
      - mission.status.from
      - mission.status.to

metrics:
  - name: gen_ai.client.token.usage
    instrument: Histogram
    unit: "{token}"
    required_dimensions:
      - gen_ai.operation.name
      - gen_ai.provider.name
      - gen_ai.token.type
      - gen_ai.request.model

  - name: gen_ai.client.operation.duration
    instrument: Histogram
    unit: s
    required_dimensions:
      - gen_ai.operation.name
      - gen_ai.provider.name
      - gen_ai.request.model

privacy:
  content_capture_default: false
  redact_always:
    - api_keys
    - tokens
    - credentials
    - pii
  max_content_length: 1000
  max_tool_output_length: 500

deprecated_attributes:
  - old: agent.name
    new: gen_ai.agent.name
    status: deprecated
  - old: agent.mission_id
    new: agentic.mission.id
    status: deprecated
  - old: agent.tool
    new: tool.name
    status: deprecated
  - old: agent.model
    new: gen_ai.request.model
    status: deprecated
  - old: agent.token_usage.input
    new: gen_ai.usage.input_tokens
    status: deprecated
  - old: agent.token_usage.output
    new: gen_ai.usage.output_tokens
    status: deprecated
  - old: agent.layer
    new: agentic.layer
    status: deprecated
  - old: agent.decision
    new: governance.decision (span event)
    status: deprecated
  - old: agent.type
    new: "gen_ai.agent.name + agentic.layer"
    status: removed
  - old: agent.role
    new: "gen_ai.agent.description or agentic.layer"
    status: removed
  - old: mission.id
    new: agentic.mission.id
    status: deprecated
  - old: loop
    new: agentic.loop
    status: deprecated
  - old: agent.division
    new: agentic.division
    status: deprecated
  - old: pr.number
    new: governance.pr.number
    status: deprecated
```

---

## Relationship to Other Files

| File | Role |
|------|------|
| **This file** | Single source of truth for all telemetry attribute names, span names, resource attributes, event contracts, privacy defaults, and migration decisions |
| `AGENTS.md` Rule 9a | Mandate: every agent MUST emit OTel spans. Attribute list deferred to this file. |
| `org/4-quality/policies/observability.md` | Policy: Agent Observability section references this file for attribute requirements |
| `org/integrations/categories/observability.md` | Integration: semantic conventions section references this file |
| `examples/observability/agent-span-example.md` | Example: concrete well-instrumented agent workflow |
| `work/missions/_TEMPLATE-technical-design.md` | Template: Observability Design section for mission-level instrumentation planning |

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 1.3 | 2026-03-29 | Added Section 6.4: collaboration and deliberation event semantics, participation quality metrics. Closes issue #231. |
| 1.2 | 2026-03-09 | (prior version — see git history) |
| 1.1 | 2026-03-09 | Folded the former `docs/observability-genai.md` quick-reference into the canonical telemetry contract to remove duplicate observability guidance. |
| 1.0 | 2026-03-09 | Initial canonical contract — consolidates AGENTS.md Rule 9a, observability policy, and integration docs. Closes issue #77. |
