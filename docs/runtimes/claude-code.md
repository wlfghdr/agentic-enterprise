# Claude Code Setup Guide for Agentic Enterprise

> **Purpose:** Practical operator guide for running the Agentic Enterprise operating model using Claude Code as the agent runtime.
> **Audience:** Operators bootstrapping the 4-loop lifecycle with Claude Code's native capabilities (CronCreate, Agent tool, TaskCreate).
> **Status:** Living document — adjust as your fleet evolves.

---

## Table of Contents

1. [Design Principles](#design-principles)
2. [Minimal Fleet (recommended starting point)](#minimal-fleet-recommended-starting-point)
3. [Model Tier Strategy](#model-tier-strategy)
4. [Claude Code Agent Identity](#claude-code-agent-identity)
5. [Heartbeat Strategy (CronCreate loops)](#heartbeat-strategy-croncreate-loops)
6. [Subagent Architecture (Agent tool)](#subagent-architecture-agent-tool)
7. [Human Gates](#human-gates)
8. [Session vs. Persistent Operation](#session-vs-persistent-operation)
9. [New Skills for Claude Code Runtime](#new-skills-for-claude-code-runtime)
10. [Cost and Reliability Notes](#cost-and-reliability-notes)

---

## Design Principles

1. **Repo is the coordination protocol.** Claude Code agents read and write repo artifacts — signals, missions, evaluations. No hidden state outside Git.
2. **Loops via CronCreate, parallelism via Agent.** Claude Code's native `CronCreate` handles heartbeats; the `Agent` tool handles concurrent subagents — no external scheduler needed.
3. **Session-aware, not session-dependent.** Loops are session-bound by default. For persistent 24/7 operation, run Claude Code on a VPS with a persistent session manager (see [Session vs. Persistent Operation](#session-vs-persistent-operation)).
4. **Humans gate merges.** Agents commit to branches and open PRs. CODEOWNERS + branch protection require human approval before anything merges into main.
5. **Idle is cheap.** Adaptive backoff means quiet periods cost nearly nothing. Agents wake fast when new work arrives.

---

## Minimal Fleet (recommended starting point)

Start with **5 agents**. This covers all 4 loops without runaway cost.

| Agent ID | Layer | Loop type | Cadence | What it does |
|---|---|---|---|---|
| `cc-ops-triage` | Strategy/Operate | CronCreate heartbeat | 30–60 min | Watches `work/signals/`, classifies, routes to missions |
| `cc-orch-orchestrator` | Orchestration | Triggered (event-driven) | Per new mission | Decomposes mission briefs into TASKS.md, spawns builder subagents |
| `cc-exec-builder` | Execution | Subagent (spawned) | Per task | Implements code/docs/content, opens PRs |
| `cc-quality-reviewer` | Quality | CronCreate heartbeat | 120–240 min | Scans open PRs, evaluates against quality policies |
| `cc-steering-digest` | Steering | CronCreate heartbeat | 1–2× / day | Aggregates signal digests, produces evolution proposals |

**Builder does not get a heartbeat.** Builders are spawned by the orchestrator on demand — never polling.

**Optional scale-ups:**
- `cc-exec-content` (mid-tier general) — GTM docs, marketing copy, knowledge base
- `cc-quality-security` (frontier reasoning) — security-sensitive PR reviews

---

## Model Tier Strategy

Claude Code runs on Claude models only. Map tiers to current model IDs in one place and update quarterly without reworking the fleet:

| Tier | Recommended model | Use for |
|---|---|---|
| **Frontier reasoning** | `claude-opus-4-6` | Steering digest, Orchestration, Quality (complex policy evaluation) |
| **Mid-tier coding** | `claude-sonnet-4-6` | Builder (execution), Signal triage |
| **Cost-efficient** | `claude-haiku-4-5` | Ops heartbeats, routing checks, HEARTBEAT_OK runs |

Configure model selection per-agent in your fleet configs at `org/2-orchestration/fleet-configs/`.

---

## Claude Code Agent Identity

Each agent in Claude Code is a **prompt context**, not a persistent process. Identity is established by:

1. **System prompt** — load `AGENTS.md` + the layer's `AGENT.md` as context
2. **Task description** — the mission brief, task, or heartbeat instruction
3. **Working directory** — your instance repo root

### Naming convention

Agent IDs used in fleet configs, CronCreate registrations, and commit attributions:

```
cc-<layer>-<role>
```

Examples: `cc-ops-triage`, `cc-orch-orchestrator`, `cc-exec-builder`, `cc-quality-reviewer`, `cc-steering-digest`

### Commit attribution

Every agent commit must include a `Co-Authored-By` line that makes the agent identity visible in Git history:

```
Co-Authored-By: cc-exec-builder (Claude Sonnet 4.6) <noreply@anthropic.com>
```

---

## Heartbeat Strategy (CronCreate loops)

Claude Code's `CronCreate` registers a recurring task that fires a prompt on a cron interval. Use it to implement the agent heartbeats that drive the 4-loop lifecycle.

### Who gets a CronCreate loop?

| Agent | Cadence | Condition |
|---|---|---|
| `cc-ops-triage` | 30–60 min | Always — this is the main intake loop |
| `cc-quality-reviewer` | 120–240 min | Only if there are open PRs pending evaluation |
| `cc-steering-digest` | Once daily (e.g. 08:00) | Only if signals are accumulating |
| `cc-orch-orchestrator` | **No heartbeat** — triggered only | Triggered by `cc-ops-triage` when a new mission brief is ready |
| `cc-exec-builder` | **No heartbeat** — spawned only | Spawned by orchestrator per task |

### Adaptive backoff

Don't use fixed-interval polling. After each heartbeat:

| Situation | Next interval |
|---|---|
| Work found (new signals, open PRs, pending missions) | Reset to **minimum** (10–30 min) |
| No work found | **Double** the interval (max: 4 hours) |
| New artifact committed to repo | Reset to minimum regardless of current interval |

**Cost rule of thumb:** if a heartbeat doesn't create a tangible artifact or reduce human load, disable it.

### Heartbeat prompt pattern

Each heartbeat prompt must:
1. `git pull` to get fresh repo state (never work on stale data)
2. Check for actionable work (new signals, open PRs, stalled missions)
3. Either produce a repo artifact OR respond `HEARTBEAT_OK`
4. Never produce duplicate artifacts — check before writing

**Minimum heartbeat for `cc-ops-triage`:**

```
You are cc-ops-triage, a signal triage agent in the [COMPANY] Agentic Enterprise.
Instructions: read and follow AGENTS.md and org/1-strategy/AGENT.md.
Apply the signal-triage skill (org/skills/signal-triage.skill.json).

1. git pull to get latest repo state.
2. Scan work/signals/ for unprocessed signals (no triage annotation yet).
3. For each unprocessed signal: classify by type and priority, annotate with triage metadata.
4. If signal warrants action: draft a mission brief in work/missions/ (max 3 per run).
5. Commit any new artifacts on a branch: signal-triage-YYYY-MM-DD-HH, open PR.
6. If nothing to process: respond HEARTBEAT_OK.
```

---

## Subagent Architecture (Agent tool)

The `Agent` tool lets the orchestrator spawn parallel Claude Code subagents without external infrastructure.

### Orchestration pattern

```
cc-orch-orchestrator (main agent)
  ├── Spawns cc-exec-builder (subagent A) → Task 1  [parallel]
  ├── Spawns cc-exec-builder (subagent B) → Task 2  [parallel]
  └── Spawns cc-quality-reviewer (subagent C) → Evaluate outputs  [after A+B]
```

### Constraints

- **Max 5 concurrent subagents** per orchestration run (aligns with `mission-orchestration` skill)
- **Max depth 1** — subagents do not spawn further subagents
- **Independent tasks → parallel**; dependent tasks → sequential (wait for results first)
- Orchestrator writes `FLEET-REPORT.md` summarizing all subagent outcomes
- Failed subagent runs must produce a signal — never silently discarded

### Subagent prompt template

When spawning a builder subagent, the orchestrator must include:

```
You are cc-exec-builder, an execution agent in the [COMPANY] Agentic Enterprise.
Instructions: read and follow AGENTS.md and org/3-execution/AGENT.md.
Apply the github-code-implementation and claude-code-repo-sync skills.
Apply quality policies from org/4-quality/policies/ before submitting.

Task:
[TASK CONTENT FROM TASKS.md]

Originating mission: work/missions/[MISSION-ID]/BRIEF.md

Deliverable:
- git pull first — work on fresh state only.
- Create branch: feat/[task-id]
- Implement the task (code, tests, docs as required)
- Self-evaluate against quality policies before opening PR
- Open a PR referencing the mission brief
- Do not merge — leave for cc-quality-reviewer approval
- Commit with: Co-Authored-By: cc-exec-builder (Claude Sonnet 4.6) <noreply@anthropic.com>
```

---

## Human Gates

The following transitions **always require human approval** (PR merge or explicit comment). Agents must not bypass these:

| Transition | Gate mechanism |
|---|---|
| Mission brief → approved for execution | Human PR review of BRIEF.md |
| PR → merge into main | CODEOWNERS + branch protection |
| Quality eval FAIL → governance exception | `work/decisions/EXC-*` + Steering approval |
| Architecture decision records | Human PR approval |
| Security-sensitive PRs | Always escalate, never auto-merge |
| Changes to `policy/`, `CODEOWNERS`, `AGENTS.md` | Explicit human-only approval required |

**What agents may auto-commit (with PR, no auto-merge):**
- Signal annotation branches (additive, no logic change)
- Mission brief drafts (human reviews before execution starts)
- Quality evaluation reports (human reads before acting on FAIL verdicts)
- Release records (after human has merged the delivery PR)

---

## Session vs. Persistent Operation

### Local development (session-bound)

CronCreate loops run while the Claude Code session is active. Close the terminal — loops stop.

**Setup:**
1. Open Claude Code CLI in your instance repo directory
2. Register heartbeat loops via CronCreate
3. Work proceeds while the session is open

Good for: development, testing loops, supervised runs.

### Persistent operation on a VPS

For continuous 24/7 operation, run Claude Code on a server with a persistent session manager.

**Recommended VPS setup (tmux):**

```bash
# SSH into your VPS
ssh root@yourserver.example.com

# Create a persistent tmux session for Claude Code
tmux new-session -d -s agentic -c /path/to/your-repo

# Start Claude Code in that session
tmux send-keys -t agentic 'claude' Enter

# Detach — the session survives SSH disconnect
# tmux attach -t agentic  ← to return later
```

**Required environment variables on VPS:**

```bash
export ANTHROPIC_API_KEY=<your-key>
export GITHUB_TOKEN=<pat-with-repo-scope>  # for gh CLI / MCP GitHub tools
```

**SSH key setup for git push from VPS:**
Ensure the VPS has an authorized SSH key registered with your GitHub account so agents can push branches and open PRs without password prompts.

**Key difference from local:** CronCreate loops registered in the VPS session persist until explicitly deleted (`CronDelete`) or the session ends. Register loops once — they run continuously without user interaction.

---

## New Skills for Claude Code Runtime

Three skills extend the core 5 skill manifests specifically for the Claude Code runtime:

| Skill ID | File | What it adds |
|---|---|---|
| `claude-code-loop` | `org/skills/claude-code-loop.skill.json` | CronCreate-based heartbeat loops with adaptive backoff |
| `claude-code-subagent` | `org/skills/claude-code-subagent.skill.json` | Agent-tool-based parallel subagent spawning for orchestrators |
| `claude-code-repo-sync` | `org/skills/claude-code-repo-sync.skill.json` | Git pull → process → commit → push cycle for all agents |

### Skill combinations per agent

| Agent ID | Core skills | Claude Code runtime skills |
|---|---|---|
| `cc-ops-triage` | `signal-triage` | `claude-code-loop`, `claude-code-repo-sync` |
| `cc-orch-orchestrator` | `mission-orchestration` | `claude-code-subagent`, `claude-code-repo-sync` |
| `cc-exec-builder` | `github-code-implementation` | `claude-code-repo-sync` |
| `cc-quality-reviewer` | `quality-evaluation`, `github-pr-review` | `claude-code-loop`, `claude-code-repo-sync` |
| `cc-steering-digest` | — | `claude-code-loop`, `claude-code-repo-sync` |

---

## Cost and Reliability Notes

### Cost controls

- **Ops first.** Register only `cc-ops-triage` CronCreate initially. Add others after validating cost.
- **Adaptive backoff is mandatory.** Idle periods should cost near zero.
- **Haiku for ops.** Routing and HEARTBEAT_OK checks don't need frontier models.
- **Batch in heartbeats.** 2–4 checks per heartbeat tick, not one check per loop.
- **Builder on demand only.** Never give builders a heartbeat — spawn them only when there is a task.

### Reliability controls

- **Idempotent prompts.** Every heartbeat prompt must be safe to run twice — check before writing artifacts.
- **No shared branches.** One branch per agent per task — no merge conflicts.
- **Additive work/ patterns.** Agents write new files; they never overwrite existing signals or releases.
- **Locks for critical shared files.** Use `work/locks/` for files multiple agents might access simultaneously.
- **git pull first, always.** Every agent run starts with a pull — never work on stale repo state.

### Known limitations

- **Session-bound loops** — CronCreate loops stop when the Claude Code process exits. Mitigation: VPS + tmux (see above).
- **No built-in webhook triggers** — CronCreate is interval-based only; no native GitHub webhook support. Mitigation: `cc-ops-triage` heartbeat is frequent enough (30–60 min) to catch new artifacts within one interval.
- **Sequential tool calls within an agent** — Claude Code processes tool calls one at a time within a single agent context. The `Agent` tool achieves true parallelism by spawning independent subprocesses with their own tool access.

---

## 11. OpenTelemetry Instrumentation

Claude Code uses a **two-layer instrumentation approach** that together covers the full OTel contract:

| Layer | Mechanism | What it covers |
|---|---|---|
| **Layer 1 — Native** | `OTEL_*` env vars (built into Anthropic SDK) | Inference spans, token usage, model identity, trace context |
| **Layer 2 — Hooks** | `PostToolUse`/`Stop` hooks + `otelcli` | `tool.execute`, `git.operation`, `agent.run`, `agentic.*` attributes |

### Minimum setup (Layer 1 only)

**With Dynatrace OneAgent on the host (recommended):**
```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:14499/otlp/v1/traces"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
export OTEL_SERVICE_NAME="cc-ops-triage"
export OTEL_SERVICE_NAMESPACE="agentic-enterprise"
export OTEL_RESOURCE_ATTRIBUTES="deployment.environment.name=production,agentic.layer=strategy,agentic.mission.id=MSN-2026-001"
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"   # privacy default
claude  # inference spans flow automatically to Dynatrace
```

**Direct to Dynatrace API (no OneAgent required):**
```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="https://<env-id>.live.dynatrace.com/api/v2/otlp"
export OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token <your-dt-token>"
export OTEL_SERVICE_NAME="cc-ops-triage"
export OTEL_GENAI_CAPTURE_MESSAGE_CONTENT="false"
claude
```

> **Dynatrace note:** Always use `http/protobuf` — Dynatrace does not support gRPC for OTLP ingest.

### Full setup (Layer 1 + 2)

Add to `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": ".claude/hooks/otel-tool-span.sh" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": ".claude/hooks/otel-agent-stop.sh" }] }
    ]
  }
}
```

Ready-to-use hook scripts are at `.claude/hooks/` in this repo. Install `otelcli` on the VPS before activating:
```bash
curl -L https://github.com/equinix-labs/otelcli/releases/latest/download/otelcli_linux_amd64.tar.gz \
  | tar xz -C /usr/local/bin otelcli
```

See full details including OTel Collector setup and Tier 4 trace hierarchy in [`docs/observability/runtime-instrumentation.md`](../observability/runtime-instrumentation.md).

---

*See also:* [`openclaw.md`](openclaw.md) for the OpenClaw runtime guide, [`docs/runtimes/README.md`](README.md) for the runtimes index, and [`org/README.md`](../../org/README.md) for the overall operating model.
