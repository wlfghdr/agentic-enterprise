# OpenClaw Setup Guide for Agentic Enterprise

> **Purpose:** Practical operator guide for running the Agentic Enterprise operating model on [OpenClaw](https://openclaw.ai).
> **Audience:** Operators bootstrapping an "agentic company" runtime (fleet, loops, automation).
> **Status:** Living document — adjust as your fleet, budgets, and reliability needs evolve.

---

## Table of Contents

1. [Design Principles](#design-principles)
2. [A Minimal Fleet (recommended starting point)](#a-minimal-fleet-recommended-starting-point)
3. [Model Tier Strategy (no hard-coded model names)](#model-tier-strategy-no-hard-coded-model-names)
4. [OpenClaw Agent IDs and Naming](#openclaw-agent-ids-and-naming)
5. [Heartbeat Strategy](#heartbeat-strategy)
6. [Cron Automation (GitHub loops)](#cron-automation-github-loops)
7. [Safe Auto-Merge Gates](#safe-auto-merge-gates)
8. [Issue Intake Rules (human vs assistant identity)](#issue-intake-rules-human-vs-assistant-identity)
9. [Self-Organizing via Repo Artifacts](#self-organizing-via-repo-artifacts)
10. [Cost and Reliability Notes](#cost-and-reliability-notes)

---

## Design Principles

1. **Keep your provider policy tight.** Fewer providers = fewer keys and failure modes.
2. **Role-first, model-second.** Assign *tiers* to roles; map tiers to concrete models in one place.
3. **Model transparency in agent identity (internally).** Operator-facing agent IDs should tell you what they are.
4. **Repo is the coordination protocol.** Loops close via PRs + artifacts, not hidden state.
5. **Heartbeats are a tax.** Use them only where they create real value (triage/ops/orchestration), not for builders.

---

## A Minimal Fleet (recommended starting point)

Start with **5 agents**. This is enough to ship reliably without runaway cost.

| Agent (example ID) | Role | Tier | What it does |
|---|---|---|---|
| `steering` | Direction & prioritization | **Frontier reasoning** | Turns signals into mission briefs and evolution proposals. |
| `orchestrator` | Decomposition & coordination | **Frontier reasoning** | Breaks missions into small PR-sized work and assigns it. |
| `builder` | Engineering execution | **Mid-tier coding** | Implements code/tests/docs at high volume. |
| `quality` | Policy & review automation | **Mid-tier reasoning** | Runs structured evaluations and enforces repo policy gates. |
| `ops` | Monitoring/triage | **Cost-efficient** | Watches for new work, PR states, failures; files signals. |

Optional scale-ups:
- **`security`** (frontier reasoning) for security-sensitive reviews.
- **`content`** (mid-tier general) for GTM/docs/website copy.

---

## Model Tier Strategy (no hard-coded model names)

Avoid hard-coding specific model names in docs and long-lived instructions. Use tiers:

| Tier | Use when | Notes |
|---|---|---|
| **Frontier reasoning** | architecture/strategy, tricky review comments, planning | Highest quality, highest cost. |
| **Mid-tier coding** | implementation, refactors, tests | Best cost×quality for shipping. |
| **Mid-tier reasoning** | evaluations, structured PR reviews | Reliable, cheaper than frontier. |
| **Cost-efficient** | triage, routing, routine checks | Fastest + cheapest; keep scope tight. |

**Operator pattern:** keep a single mapping that you can update quarterly without reworking the fleet.

---

## OpenClaw Agent IDs and Naming

### Runtime wiring checklist (make this explicit)
Before judging whether “autonomy works”, ensure each runtime agent is wired to:
- the **correct repo path** (the company fork)
- the **instruction hierarchy** (AGENTS.md → layer AGENT.md → division → mission brief)
- an **output channel** (PRs + repo artifacts)

If this step is missing, agents will behave like generic chatbots and adopters will misdiagnose it as an LLM problem.

Two practical approaches:

### Option A — Simple IDs (recommended)
Use stable IDs and document tiers in config:
- `steering`, `orchestrator`, `builder`, `quality`, `ops`

This keeps everything readable and avoids churn when models change.

### Option B — Transparent IDs (advanced)
Encode provider+tier into IDs so logs are self-explanatory:
- `anthropic-frontier-steering`
- `openai-mid-builder`

If you choose this, **keep it internal** (operator docs) and avoid scattering model names into public docs.

---

## Heartbeat Strategy

Heartbeats are periodic wake-ups. They should **batch** small checks and either:
- create a repo artifact (signal, digest, status update), or
- respond with `HEARTBEAT_OK`.

### Adaptive heartbeat backoff (cost control)
A good default is **adaptive cadence**:
- set a **min** interval (fast enough to feel alive)
- set a **max** interval (hard budget barrier)
- **double** the interval on each idle run
- **reset** back to min when visible work appears

Example defaults (starter company):
- min: 30m
- max: 24h

This can be implemented even if your runtime only supports a fixed heartbeat schedule:
run the heartbeat frequently, but self-gate in the agent’s checklist using a small state file.

### Who gets heartbeat?

| Agent | Heartbeat | Cadence | Why |
|---|---:|---:|---|
| `ops` | ✅ | 30–60 min | Most value per token: triage and routing. |
| `orchestrator` | ✅ | 60–120 min | Only if you have ongoing missions to coordinate. |
| `quality` | ✅ | 120–240 min | Scans for PRs needing evaluation/commentary. |
| `steering` | ✅ (optional) | 1–2× / day | Strategic digest. Not needed hourly. |
| `builder` | ❌ | — | Builders should be **triggered**, not polling. |

### Adaptive backoff (recommended)

Don't run fixed-interval heartbeats — use **exponential backoff** that adapts to activity:

| Condition | Cadence | Rationale |
|---|---|---|
| Recent activity (new signals, open PRs, missions in-flight) | **10 min** (minimum) | High change rate → agents should react quickly. |
| Moderate activity (some work in progress, no urgency) | **30–60 min** | Normal operating rhythm. |
| Low activity (no open missions, no pending PRs) | **2–4 hours** | Save tokens; wake faster if a new signal lands. |
| Idle (nothing changed since last heartbeat) | **1× daily** (maximum) | Baseline liveness check — still produces `HEARTBEAT_OK`. |

**How it works:**
1. After each heartbeat, the agent evaluates how much actionable work it found.
2. If work was found → reset cadence to **minimum** (10 min).
3. If no work was found → **double** the interval (up to the daily cap).
4. External events (new signal filed, PR opened, webhook) → immediately reset to minimum regardless of current interval.

This keeps costs near zero during quiet periods while ensuring sub-15-minute response times during active development.

**Cost rule of thumb:** if a heartbeat doesn't create a tangible artifact or reduce human load, disable it.

### Heartbeat checklist pattern
Keep a short `HEARTBEAT.md` checklist in the workspace, owned by `ops`.

---

## Cron Automation (GitHub loops)

Use OpenClaw cron when you need **exact timing** and **isolated runs**.

A proven baseline loop:
- Every hour:
  - merge eligible PRs (approved + clean + checks green)
  - handle actionable review comments (spawn one fix agent)
  - start the next assistant-owned issue if idle

Keep cron conservative:
- max **one** spawned sub-agent per run
- never merge with `CHANGES_REQUESTED`
- require `mergeable_state == clean`

---

## Troubleshooting: Multi-agent setups (credentials, provider IDs, dispatch state, restarts)

This section is specific to **OpenClaw-based** fleets where you have a dispatcher/orchestrator that triggers one or more **execution agents**.

### 1) Execution-agent credentials are per `agentDir` (not implicitly shared)

In multi-agent setups, each agent may run with a different `agentDir`. In OpenClaw terms, that means:
- each agent can have its own local config + auth store
- credentials you set up for one agent are **not guaranteed** to be available to another

**Symptom:** dispatcher works, but an execution agent fails with an auth error even though “keys are set somewhere”.

**Operator check:** verify the execution agent can see credentials for the provider/profile it is actually using (in its own `agentDir`).

### 2) Provider/model identifier mismatches ("I set OPENAI_API_KEY, why is it asking for something else?")

Some model selections route through provider IDs that may not match your mental model.

**Symptom:** the runtime logs mention a provider/profile you didn't expect.

**Operator check:** look at the provider ID/profile name the runtime is requesting in the execution agent's logs, then ensure credentials exist **for that exact provider/profile** in that agent's environment/auth config.

### 3) Dispatch idempotency: state file contract (re-dispatch safely)

Handsfree dispatch scripts should persist an idempotency state file so they don't spam duplicate work.

Recommended minimal schema:

```json
{
  "version": 1,
  "prs": {
    "123": {
      "lastDispatchedAt": "2026-02-24T00:00:00Z",
      "status": "dispatched",
      "note": "optional freeform"
    }
  }
}
```

**Safe operator action:** to re-dispatch a single PR, remove just that PR key (e.g. `"123"`) and keep the rest of the file intact.

### 4) Container restarts: `systemctl --user` is often unavailable

In containerized environments, `systemctl --user` frequently isn't available.

**Recommendation:** document your restart path in terms of your actual supervisor:
- Docker Compose: `docker compose restart <service>`
- Kubernetes: roll the deployment

Where OpenClaw supports dynamic reloads, prefer reload over restart.

---

## Safe Auto-Merge Gates

Recommended gates (all must pass):
1. Approved by the human owner
2. All checks passing
3. `mergeable_state == clean`
4. No changes to protected paths (`policy/`, `CODEOWNERS`, etc.) without explicit approval

If you want to go further, add:
- PR size limits
- "quality eval" bot comment requirement

---

## Issue Intake Rules (human vs assistant identity)

**Key rule:** keep human work separate from assistant work.

- Issues assigned to your **human owner account** = human-owned; do **not** auto-start.
- Issues assigned to your **assistant/bot identity** = assistant-owned; eligible for automation.

**Practical tip:** create a dedicated GitHub user/bot (e.g., `YourCompanyAI`) for automation assignments.
This prevents the assistant from hijacking the human's backlog and makes ownership explicit.

---

## Daily human reporting (default trust artifact)
A repo-native agentic company should produce one predictable, human-friendly report per day.

Recommended:
- Write: `work/reports/daily/YYYY-MM-DD.md`
- Send: a short chat summary to the human owner (what changed, what’s next, blockers)

This prevents the system from feeling “silent” and keeps trust high.

## Self-Organizing via Repo Artifacts

The loops work when agents write to the repo:

- `work/signals/` — raw signals and observations
- mission briefs (`work/missions/.../BRIEF.md`) — what to do next
- `STATUS.md` — progress + blockers
- evaluation notes — why a PR is safe/unsafe to merge

If an agent finishes a mission, it should create at least one new signal ("next improvement").

---

## Cost and Reliability Notes

### Cost controls
- Run heartbeats on **ops** first; add others only if needed.
- Batch 2–4 checks per heartbeat.
- Consider night-mode cadence reduction.

### Reliability controls
- Keep both providers configured (failover option).
- Set conservative rate limits.
- Prefer deterministic, artifact-producing routines over chatty polling.

---

*See also:* the wider operating model in [`OPERATING-MODEL.md`](../../OPERATING-MODEL.md) and the [runtimes index](README.md) for other runtime implementation guides.
