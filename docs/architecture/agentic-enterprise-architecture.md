# Architecture Overview

## The Ecosystem

Agentic Enterprise is a layered system with clear separation between the framework, your organization, your runtime, and your observability platform.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. FRAMEWORK (this repository)                                │
│   ─────────────────────────────                                 │
│   Templates, policies, agent instructions, process definitions  │
│   You fork this. It defines HOW your organization operates.     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   2. YOUR ORGANIZATION (your fork)                              │
│   ────────────────────────────────                              │
│   Filled-in CONFIG.yaml, customized divisions, real signals,    │
│   missions, decisions, releases. Your company, in Git.          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   3. RUNTIME (bring your own)                                   │
│   ─────────────────────────────                                 │
│   Agent platforms that execute the work: Claude Code, OpenAI    │
│   Agents SDK, CrewAI, LangGraph, OpenClaw, or any other.        │
│   The framework is runtime-agnostic.                            │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   4. OBSERVABILITY (the feedback channel)                       │
│   ───────────────────────────────────────                       │
│   OpenTelemetry traces, metrics, dashboards. Agents emit        │
│   telemetry as they work. The platform surfaces patterns        │
│   and feeds signals back into governance.                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## The Operating Loop

All work flows through four continuous loops:

```
                    ┌──────────────────────┐
                    │                      │
          ┌────────▼────────┐    ┌────────┴────────┐
          │   1. DISCOVER    │    │   4. OPERATE     │
          │   & DECIDE       │    │   & EVOLVE       │
          │                  │    │                   │
          │   Signal → Brief │    │   Monitor → Fix   │
          │   Hours–Days     │    │   24/7             │
          └────────┬─────────┘    └────────▲──────────┘
                   │                       │
          ┌────────▼─────────┐    ┌────────┴──────────┐
          │   2. DESIGN       │    │   3. VALIDATE      │
          │   & BUILD         │    │   & SHIP            │
          │                   │    │                     │
          │   Brief → Code    │    │   Staging → GA      │
          │   Days–Weeks      │    │   Days               │
          └───────────────────┘    └─────────────────────┘

          Telemetry from Loop 4 feeds new Signals into Loop 1.
          The system improves itself continuously.
```

## The 5-Layer Organization

Every function operates within the same structure:

```
  STEERING (Layer 0)        Evolve the company itself
       │                    Executives + agents adjust structure,
       │                    policies, and divisions
       ▼
  STRATEGY (Layer 1)        Define WHY and WHAT
       │                    Venture leads set direction
       │                    and constraints
       ▼
  ORCHESTRATION (Layer 2)   Translate strategy into work
       │                    Mission leads decompose,
       │                    assign, and sequence
       ▼
  EXECUTION (Layer 3)       Do the work
       │                    Specialized divisions execute
       │                    (engineering, marketing, etc.)
       ▼
  QUALITY (Layer 4)         Evaluate the output
                            Policy-driven evaluation
                            against 19 quality domains
```

## Artifact Flow

Every piece of work produces a chain of traceable artifacts:

```
Signal                    "We observed X"
  │                       (work/signals/)
  ▼
Mission Brief             "We will do Y about X"
  │                       (work/missions/)
  ▼
Technical Design          "Here is how we build Y"
  │                       (work/missions/<name>/)
  ▼
Pull Request              "Here is the change"
  │                       (GitHub)
  ▼
Quality Evaluation        "Does it meet policy?"
  │                       (org/4-quality/)
  ▼
Release Contract          "What shipped and what it achieved"
  │                       (work/releases/)
  ▼
New Signal                "We learned Z from shipping Y"
                          (work/signals/)
```

## Git as the Governance Backbone

```
┌────────────────────────────────────────────────────────┐
│                    Git Repository                       │
│                                                        │
│   Branches        = Workflow states                     │
│   Pull Requests   = Decisions (approve/reject)          │
│   CODEOWNERS      = RACI matrix (who approves what)     │
│   CI/CD           = Automated quality gates             │
│   Git History     = Complete audit trail                 │
│   Markdown/YAML   = Agent-readable instructions         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

No ticket system, no wiki, no status meetings. Git is the single source of truth for organizational state, decisions, and history.

## Two Communication Channels

Agents interact with the system through two native channels:

```
Channel 1: THE REPOSITORY (asynchronous)
──────────────────────────────────────────
  Agents read:   AGENT.md instructions, mission briefs, policies
  Agents write:  Signals, code, documentation, status updates
  Governed by:   PRs, CODEOWNERS, CI/CD checks
  Audit trail:   Git history

Channel 2: OBSERVABILITY PLATFORM (real-time)
──────────────────────────────────────────────
  Agents emit:   OpenTelemetry spans, metrics, events
  Agents read:   Dashboards, baselines, anomalies
  Governed by:   OTel contract (docs/otel-contract.md)
  Audit trail:   Telemetry storage
```

Both channels feed the governance loop. The repo captures decisions. Observability captures execution reality. Together they provide a complete picture.

## Framework vs. Runtime — Explicit Separation

| Concern | Framework (this repo) | Runtime (you bring) |
|---------|----------------------|---------------------|
| Org structure | Defined in `org/` | N/A |
| Agent instructions | `AGENT.md` files | Loaded as system prompts |
| Process definitions | `process/` loops | Implemented as workflows |
| Quality policies | `org/4-quality/policies/` | Enforced at runtime |
| Work tracking | `work/` artifacts or issues | Agents create and update |
| Integrations | Declared in `CONFIG.yaml` | Connected via MCP/API |
| Telemetry contract | `docs/otel-contract.md` | Instrumented in agent code |
| Governance | PRs + CODEOWNERS | Git operations |

The framework defines **what** the organization does and **how** it's governed. The runtime executes it. This separation means you can swap runtimes without changing your organizational model.

## Proof at Scale

This architecture is not theoretical. The reference organization has produced:

- **99 work items** — signals triaged, missions scoped, tasks tracked
- **108 pull requests** — each governed by CODEOWNERS, reviewed, and merged
- **440+ commits** — every change traceable in Git history

The Git history is the operational proof that the architecture works as designed.

## Next Steps

- [10-Minute Quickstart](../quickstart/10-minute-agentic-enterprise.md) — Walk through the core workflow
- [Observability Architecture](../observability/otel-architecture.md) — How telemetry integrates
- [Minimal Adoption Guide](../adoption/minimal-adoption.md) — Start using the framework
- [Reference Organization](../reference-organization/) — See the framework in action
