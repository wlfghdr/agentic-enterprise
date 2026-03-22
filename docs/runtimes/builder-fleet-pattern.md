# Builder Fleet Pattern

> **Version:** 1.0 | **Layer:** Execution (Layer 3) | **Status:** Reference

---

## What Is a Builder Fleet?

A **builder fleet** is a specialized subset of the execution layer in which **thin orchestrating agents delegate focused work units to specialized builder agents** that implement, verify, and hand back results.

This is distinct from the general Execution Layer concept: a builder fleet is not just "agents doing work" — it is a **structured, role-separated runtime pattern** in which the roles of planner, executor, checker, and verifier are explicitly separated and independently operated.

---

## When to Use This Pattern

Use a builder fleet when:

- Work requires **multi-step construction with verifiable intermediate outputs** (code, documents, configs)
- A mission cannot be safely completed in one agent call without meaningful verification checkpoints
- Multiple specialized builders must collaborate on a shared artifact
- You need **wave-based execution**: plan → build → check → verify → integrate

Do not use this pattern for lightweight tasks that a single execution agent can complete without risk of compounding errors.

---

## Core Role Separation

| Role | Responsibility |
|---|---|
| **Orchestrator** | Receives mission intent from Orchestration Layer. Decomposes into work units. Delegates to builders. Monitors progress. Escalates exceptions. |
| **Builder** | Implements a single, well-scoped work unit. Produces a concrete artifact (code, config, doc section, test). Does not steer the overall mission. |
| **Checker** | Validates the builder's output against the work unit spec: correctness, completeness, style/lint, schema conformance. Returns pass/fail + diff. |
| **Verifier** | Validates end-to-end integration: does the assembled artifact satisfy the mission outcome contract? Bridges builder output and mission success criteria. |

---

## Execution Flow

```
Orchestration Layer
       │
       ▼
  Orchestrator Agent
       │
       ├─── Decomposes mission into work units (wave plan)
       │
       ▼
  Wave 1: Builders (parallel where independent)
       │
       ├─── Builder A → output A
       ├─── Builder B → output B
       └─── Builder C → output C
       │
       ▼
  Checkers (per builder output)
       │
       ├─── Check A → pass / fail + feedback
       ├─── Check B → pass / fail + feedback
       └─── Check C → pass / fail + feedback
       │
       ▼
  Retry loop (failed builders rework with checker feedback)
       │
       ▼
  Wave N: Verifier
       │
       ├─── Integration check: assembled artifact vs. outcome contract
       └─── Pass → handoff to Orchestration / PR / release
            Fail → escalate to Orchestrator (may trigger re-planning)
```

---

## Wave-Based Execution

Work is organized into **waves**: groups of work units that can be built in parallel within one wave, where later waves depend on earlier wave outputs.

- **Within a wave:** builders run in parallel (or sequentially if tooling requires)
- **Between waves:** Checker/Verifier gates must pass before the next wave starts
- **Failure in a wave:** builder retries with checker feedback before escalating to the orchestrator

This produces a **traceable execution record**: which wave, which builder, which check result, which retry.

---

## State and Observability

Builder fleets should maintain **file-backed or artifact-backed state** that survives individual agent call boundaries:

- Wave plan (what was planned and in what order)
- Per-builder work units and outputs
- Checker results and retry counts
- Verifier verdict and integration evidence

This state is the input to OTel span instrumentation (see [otel-contract.md](../otel-contract.md)) and feeds back into mission observability.

---

## Attachment to the Operating Model

The builder fleet pattern **extends**, not replaces, the Agentic Enterprise operating model:

| Operating model concept | Builder fleet equivalent |
|---|---|
| Mission outcome contract | Verifier's acceptance criteria |
| Task list (TASKS.md) | Wave plan + builder work units |
| Execution agent | Builder agent |
| Quality evaluation | Checker + Verifier roles |
| Signal / escalation | Orchestrator → Orchestration Layer escalation |

The operating model governs **what gets built and why** (governance, approval, release). The builder fleet governs **how it gets built** (execution mechanics, verification loops, retry discipline).

---

## Runtime-Agnostic

This pattern does not require a specific runtime. It can be implemented in:

- **Claude Code / OpenClaw** — sub-agent spawning for builder roles, file-backed state
- **LangGraph** — graph nodes for each role with conditional edge back-loops for retries
- **CrewAI** — crew = builder fleet, task = work unit, sequential process with review task
- **AutoGen** — agent-to-agent message passing with explicit checker messages

See [README.md](README.md) for runtime guides that connect this pattern to specific runtimes.

---

## External Reference: GSD

[Get Shit Done (GSD)](https://github.com/getrobert/gsd) is an open-source implementation of the builder fleet pattern that demonstrates:

- Thin orchestrators delegating to specialized builders
- Planner / executor / checker / verifier role separation
- Wave-based execution with retry loops
- Multi-runtime support with runtime-specific fallback behavior
- Persistent file-backed execution state

GSD is a useful **existence proof** of this pattern in production: it shows how operating-model-level governance (what to build) and builder-runtime-level mechanics (how to build it) can coexist without collapsing the separation.

> **Note:** This framework does not adopt or standardize on GSD. It is referenced here as a concrete example of the builder fleet pattern, not as a prescribed runtime.

---

## Related Docs

- [Runtime Implementation Guides](README.md) — runtime-specific deployment guides
- [otel-contract.md](../otel-contract.md) — how to instrument builder fleet spans
- [automation-patterns.md](../automation-patterns.md) — scheduling and event-driven triggers
- [mission-lifecycle.md](../mission-lifecycle.md) — mission phases that builder fleets operate within
