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
