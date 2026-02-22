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

### Who gets heartbeat?

| Agent | Heartbeat | Cadence | Why |
|---|---:|---:|---|
| `ops` | ✅ | 30–60 min | Most value per token: triage and routing. |
| `orchestrator` | ✅ | 60–120 min | Only if you have ongoing missions to coordinate. |
| `quality` | ✅ | 120–240 min | Scans for PRs needing evaluation/commentary. |
| `steering` | ✅ (optional) | 1–2× / day | Strategic digest. Not needed hourly. |
| `builder` | ❌ | — | Builders should be **triggered**, not polling. |

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
