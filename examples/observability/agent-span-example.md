# Agent Span Example: Well-Instrumented Workflow

> **Version:** 1.0 | **Last updated:** 2026-03-09
> **Contract reference:** [`docs/otel-contract.md`](../../docs/otel-contract.md)
> **Purpose:** Concrete end-to-end example of a compliant agent trace from mission start through quality evaluation.

This example shows a complete, compliant trace for a single execution-layer agent run: the agent receives a task, calls an LLM twice (with a tool call in the middle), emits a governance decision, and is evaluated by the quality layer. All attribute names conform to `docs/otel-contract.md`.

---

## Scenario

**Mission:** MSN-2026-042 — Add observability instrumentation to component `payment-service`
**Agent:** `InstrumentationAgent` (execution layer, software-engineering division)
**Task:** Write OTel SDK initialization code and emit a test span

---

## Resource Attributes (set once at SDK init)

```
service.name                  = "execution-agent"
service.version               = "3.2.0"
service.instance.id           = "agent-pod-f3a9b2"
service.namespace             = "agentic-enterprise"
deployment.environment.name   = "staging"
telemetry.sdk.name            = "opentelemetry"
telemetry.sdk.version         = "1.29.0"
```

---

## Full Trace

```
agent.run InstrumentationAgent                   [INTERNAL]  duration: 4.3s
│
│  # Required span attributes (agent.run)
│  gen_ai.agent.name         = "InstrumentationAgent"
│  gen_ai.agent.id           = "agent_instr_001"
│  agentic.layer             = "execution"
│  agentic.mission.id        = "MSN-2026-042"
│  agentic.division          = "software-engineering"
│  agentic.task.id           = "TSK-2026-042-07"
│  agentic.session.id        = "session_f3a9b2_001"
│  agentic.loop              = "build"
│
├── inference.chat claude-3-5-sonnet             [CLIENT]    duration: 1.2s
│   │
│   │  # OTel GenAI standard attributes
│   │  gen_ai.operation.name         = "chat"
│   │  gen_ai.provider.name          = "anthropic"
│   │  gen_ai.request.model          = "claude-3-5-sonnet-20241022"
│   │  gen_ai.response.model         = "claude-3-5-sonnet-20241022"
│   │  gen_ai.usage.input_tokens     = 847
│   │  gen_ai.usage.output_tokens    = 312
│   │  gen_ai.response.finish_reasons = ["tool_calls"]
│   │  gen_ai.response.id            = "msg_01XaT5abc123"
│   │  gen_ai.conversation.id        = "conv_msn042_007"
│   │  server.address                = "api.anthropic.com"
│   │  server.port                   = 443
│   │
│   └── tool.execute read_file                   [CLIENT]    duration: 0.04s
│         tool.name     = "read_file"
│         tool.type     = "function"
│         tool.call.id  = "call_abc123"
│
├── inference.chat claude-3-5-sonnet             [CLIENT]    duration: 1.8s
│   │
│   │  gen_ai.operation.name         = "chat"
│   │  gen_ai.provider.name          = "anthropic"
│   │  gen_ai.request.model          = "claude-3-5-sonnet-20241022"
│   │  gen_ai.response.model         = "claude-3-5-sonnet-20241022"
│   │  gen_ai.usage.input_tokens     = 1204
│   │  gen_ai.usage.output_tokens    = 589
│   │  gen_ai.response.finish_reasons = ["stop"]
│   │  gen_ai.response.id            = "msg_01XaT5def456"
│   │  gen_ai.conversation.id        = "conv_msn042_007"
│   │
│   └── tool.execute write_file                  [CLIENT]    duration: 0.02s
│         tool.name     = "write_file"
│         tool.type     = "function"
│         tool.call.id  = "call_def456"
│
├── git.operation commit                         [CLIENT]    duration: 0.1s
│     git.operation       = "commit"
│     git.branch          = "copilot/MSN-2026-042-instrumentation"
│     git.repo            = "wlfghdr/payment-service"
│     agentic.mission.id  = "MSN-2026-042"
│
├── git.operation pr_open                        [CLIENT]    duration: 0.15s
│     git.operation         = "pr_open"
│     git.pr.number         = 142
│     git.branch            = "copilot/MSN-2026-042-instrumentation"
│     git.repo              = "wlfghdr/payment-service"
│     agentic.mission.id    = "MSN-2026-042"
│
│   # Native span event: governance decision emitted directly on agent.run span
│   [SPAN EVENT] governance.decision
│     governance.decision   = "approve"
│     governance.reason     = "Instrumentation complete, PR opened for review"
│     governance.pr.number  = 142
│
└── quality.evaluate observability               [INTERNAL]  duration: 0.3s
      quality.policy.id = "observability"
      quality.verdict   = "pass"
      agentic.mission.id = "MSN-2026-042"
```

---

## Metrics Emitted

For each `inference.*` span, the following metrics are also emitted:

```
gen_ai.client.token.usage
  dimensions:
    gen_ai.operation.name  = "chat"
    gen_ai.provider.name   = "anthropic"
    gen_ai.token.type      = "input"
    gen_ai.request.model   = "claude-3-5-sonnet-20241022"
  value: 847   (first LLM call)

gen_ai.client.token.usage
  dimensions:
    gen_ai.operation.name  = "chat"
    gen_ai.provider.name   = "anthropic"
    gen_ai.token.type      = "output"
    gen_ai.request.model   = "claude-3-5-sonnet-20241022"
  value: 312

gen_ai.client.operation.duration
  dimensions:
    gen_ai.operation.name  = "chat"
    gen_ai.provider.name   = "anthropic"
    gen_ai.request.model   = "claude-3-5-sonnet-20241022"
  value: 1.2   (seconds)
```

---

## Error Scenario: Tool Call Failure

If `read_file` fails, the `tool.execute` span looks like:

```
tool.execute read_file                           [CLIENT]    status: ERROR
  tool.name     = "read_file"
  tool.type     = "function"
  tool.call.id  = "call_abc123"
  error.type    = "file_not_found"

  [SPAN EVENT] tool.error
    error.type  = "file_not_found"
    tool.name   = "read_file"
```

The parent `inference.chat` span inherits ERROR status. The `agent.run` span also propagates ERROR status.

---

## Quality Evaluation Failure Scenario

If the quality evaluation rejects the PR:

```
quality.evaluate observability                   [INTERNAL]
  quality.policy.id = "observability"
  quality.verdict   = "fail"
  agentic.mission.id = "MSN-2026-042"

  [SPAN EVENT] policy.violation
    quality.policy.id = "observability"
    governance.reason = "Missing gen_ai.usage.input_tokens on inference spans"

  [SPAN EVENT] governance.decision
    governance.decision = "reject"
    governance.reason   = "Missing gen_ai.usage.input_tokens on inference spans"
    governance.pr.number = 142
```

---

## Deprecated Field — Migration Example

If existing instrumentation emits the legacy `agent.name` field, migrate as follows:

```diff
- span.set_attribute("agent.name", "InstrumentationAgent")
- span.set_attribute("agent.mission_id", "MSN-2026-042")
- span.set_attribute("agent.layer", "execution")
- span.set_attribute("agent.token_usage.input", 847)
- span.set_attribute("agent.token_usage.output", 312)
+ span.set_attribute("gen_ai.agent.name", "InstrumentationAgent")   # OTel GenAI standard
+ span.set_attribute("agentic.mission.id", "MSN-2026-042")           # custom, agentic.* prefix
+ span.set_attribute("agentic.layer", "execution")                   # custom, agentic.* prefix
+ span.set_attribute("gen_ai.usage.input_tokens", 847)               # OTel GenAI standard
+ span.set_attribute("gen_ai.usage.output_tokens", 312)              # OTel GenAI standard
```

See the full deprecation table in [`docs/otel-contract.md` Section 9](../../docs/otel-contract.md#9-canonical-mapping-and-deprecation-table).

---

## Instrumentation Checklist for This Workflow

- [x] `agent.run` span with `gen_ai.agent.name`, `gen_ai.agent.id`, `agentic.layer`, `agentic.mission.id`
- [x] `inference.chat` spans with `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens`
- [x] `tool.execute` child spans under inference spans
- [x] `git.operation` spans for commit and PR
- [x] `quality.evaluate` span with `quality.verdict`
- [x] Native `governance.decision` span event on decision points
- [x] `gen_ai.client.token.usage` metric per inference call
- [x] `gen_ai.client.operation.duration` metric per inference call
- [x] `gen_ai.conversation.id` propagated through all spans in the same session
- [x] `error.type` set and span status = ERROR on all failure paths
- [x] W3C `traceparent` header propagated across HTTP calls
- [x] Resource attributes set at SDK init (not on individual spans)
