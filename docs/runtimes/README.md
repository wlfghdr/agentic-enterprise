# Runtime Implementation Guides

> **Purpose:** This folder contains operator guides for running the Agentic Enterprise framework on specific agent runtimes and platforms.
> The framework itself is runtime-agnostic — these guides describe how to connect it to concrete runtimes.

---

## What Is a Runtime Guide?

A runtime guide describes how to connect the Agentic Enterprise framework to a specific agent runtime, platform, or orchestration system. Each guide covers the same core questions for its runtime:

- **Instruction injection** — how to load `AGENTS.md` and layer-specific `AGENT.md` files into the runtime
- **Tool bindings** — which tools the runtime needs (GitHub, file access, web search)
- **Fleet sizing** — agent roles, model tier assignments, and scaling recommendations
- **Scheduling** — heartbeat/cron patterns for the 4-loop lifecycle
- **Runtime-specific conventions** — naming, identity, cost controls, reliability patterns

---

## Available Runtime Guides

| Runtime | Guide | What it covers |
|---|---|---|
| **OpenClaw** | [`openclaw.md`](openclaw.md) | Fleet sizing, model tier strategy, heartbeat scheduling, auto-merge gates, cost/reliability controls |

---

## Recommended Runtimes for This Framework

The Agentic Enterprise framework maps well to runtimes that support **loops, multi-agent coordination, and event-driven scheduling**. Here are the strongest candidates:

| Framework | Loop/Scheduling | Multi-Agent | Why relevant |
|---|---|---|---|
| **LangGraph** | Graph-based state machine with loops, branches, pause/resume | Yes, multiple agents as graph nodes | Agents can loop, branch back, wait on events — ideal for the 4-loop architecture |
| **CrewAI** | Crews (autonomous teams) + Flows (event-driven) | Yes, role-based agent teams | Closest to the "Division" concept — each agent has a role, crews collaborate |
| **Microsoft AutoGen** | Message-passing loop, asynchronous | Yes, peer-to-peer communication | Agents discuss with each other, good for Steering↔Strategy communication |
| **Claude Agent SDK** | Custom loops possible | Yes, via sub-agents | Direct Claude integration, MCP-native, simplest path for this repo |
| **n8n** | Cron/webhook-based scheduling, event-driven | Yes, via AI nodes + workflows | Best option for regular triggering — "Every Monday: Steering agent processes signals" |

### Recommended Two-Layer Architecture

The core challenge — "agents must be triggered manually every time" — is **not solved by the agent runtime itself**, but by a **scheduling/event layer in front of it**. For production use, combine two layers:

#### Layer 1: Scheduling + Event Layer (n8n, Temporal, or similar)

This layer handles the **when** and **why** of agent activation:

- **Cron jobs:** "Mondays: create signal digest", "Hourly: check production health"
- **Webhooks:** "New signal filed → trigger Strategy agent", "PR merged → trigger Quality agent"
- **Event watchers:** File system events, GitHub webhooks, Slack messages

This eliminates the need for manual agent invocation and enables the continuous operation the 4-loop lifecycle requires.

#### Layer 2: Agent Runtime (LangGraph, CrewAI, or Claude Agent SDK)

This layer handles the **how** of agent execution:

- **LangGraph** — if you want to model the 4-loop graph architecture directly (loops, branches, conditional edges)
- **CrewAI** — if you want to map the Divisions/Roles model 1:1 (each division = a crew, each agent type = a role)
- **Claude Agent SDK** — pragmatic fast path: direct Claude integration with MCP tool bindings, sub-agent spawning, and minimal setup overhead

#### Pragmatic Quick-Start Option

The fastest route to a running system: **Claude Agent SDK + a simple file watcher** (e.g., `chokidar` in Node.js or a lightweight polling script) that monitors `work/signals/` and automatically spawns the next agent when new files appear. Add a cron job for periodic heartbeats (signal digests, health checks) and you have a minimal but functional event-driven loop without heavy infrastructure.

---

## How to Add a New Runtime Guide

1. Create `docs/runtimes/<runtime-name>.md` (or a subfolder for complex runtimes)
2. Structure it around the core questions above (instruction injection, tool bindings, fleet sizing, scheduling, conventions)
3. Add a row to the table above
4. Keep it operator-focused — implementation detail, not framework theory

**What belongs here vs. in the framework core:**
- Runtime guides → `docs/runtimes/` (you are here)
- Framework rules and governance → `AGENTS.md`, `org/*/AGENT.md`, `org/4-quality/policies/`
- Company identity and config → `CONFIG.yaml`, `COMPANY.md`
- Active work artifacts → `work/`

---

## The Runtime-Agnostic Principle

The framework core — `AGENTS.md`, `org/`, `process/`, quality policies — must remain runtime-agnostic. This means:

- No specific model names in governance documents (use tier labels like "frontier reasoning" instead)
- No runtime-specific tool syntax in quality policies
- No platform-specific scheduling assumptions in process guides

Runtime-specific configuration belongs here, not in the framework core. This ensures the framework can run on any runtime (or multiple runtimes simultaneously) without core changes.

---

*Back to [docs/README.md](../README.md) | [OPERATING-MODEL.md](../../OPERATING-MODEL.md)*
