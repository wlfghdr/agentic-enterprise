# Minimal Startup Loop — Solo Founder Edition

> **For:** 1-person startups using this framework to build, deploy, and iterate a software product.  
> **Prerequisite:** You have a Vision and a Mission. That's it.  
> **No external observability platform required.** The repo _is_ the observability.

---

## 1. The Minimal Agent Team

You need exactly **4 agent roles**. Each maps to a model tier:

| Role | What it does | Recommended model | When it runs |
|------|-------------|-------------------|-------------|
| **Orchestrator** | Reads signals, creates missions, assigns work, checks DoD | Claude Sonnet 4 | On every signal or mission state change |
| **Coder** | Implements missions — writes code, tests, PRs | Claude Sonnet 4 / Codex | When a mission is `assigned` |
| **Researcher** | Deep analysis, architecture decisions, market research | Claude Opus 4 | When a signal needs investigation or a mission needs design |
| **Triage** | Cheap pre-filter: classifies signals, checks CI, does reviews | Claude Haiku / GPT-4.1-mini | Continuously (webhook/cron) |

> **Solo founder rule:** You are the Steering Layer. You merge PRs. That's your only required action.

---

## 2. Where Things Live

```
CONFIG.yaml                          ← Your Vision + Mission (fill once)
work/signals/                        ← Incoming observations (auto or manual)
work/signals/_TEMPLATE-signal.md     ← Signal format
work/missions/                       ← Active work units
work/missions/<slug>/BRIEF.md        ← What to do
work/missions/<slug>/OUTCOME-CONTRACT.md  ← Definition of Done
work/missions/<slug>/STATUS.md       ← Current state (created by Orchestrator)
```

**Vision** lives in `CONFIG.yaml` → `vision.north_star`  
**Mission** lives in `CONFIG.yaml` → `vision.mission`  
Everything else flows from these two fields.

---

## 3. The Loop (Signal → Mission → Done → Signal)

```
┌─────────┐     ┌──────────┐     ┌─────────┐     ┌──────────┐
│  Signal  │────▶│  Mission  │────▶│  Work   │────▶│   Done   │
│ (detect) │     │ (plan)    │     │ (build) │     │ (verify) │
└─────────┘     └──────────┘     └─────────┘     └──────────┘
     ▲                                                  │
     └──────────────── new signals ◀────────────────────┘
```

### 3a. What is a Signal?

A **Signal** is a file in `work/signals/` that says "something happened that might need action." Signals come from:

- **Triage agent** watching CI failures, error logs, dependency updates
- **You** dropping a note ("I talked to a user and they want X")
- **Operate loop** detecting production anomalies
- **Retrospectives** identifying process gaps
- **Any agent** noticing friction or opportunity

A signal is just a markdown file following `_TEMPLATE-signal.md`. Minimum viable signal:

```markdown
# Signal: Users can't sign up on mobile

## Source
- **Category:** customer
- **Confidence:** high

## Observation
3 users reported signup form doesn't submit on iOS Safari.

## Recommendation
- **Action:** Create a mission to fix mobile signup.
```

### 3b. How a Signal Becomes a Mission

1. **Triage** agent scans `work/signals/` for files without a `## Resolution` section
2. **Triage** adds initial assessment (urgency, impact, affected area)
3. **Orchestrator** reads assessed signals, decides:
   - **Create mission** → writes `work/missions/<slug>/BRIEF.md` + `OUTCOME-CONTRACT.md`
   - **Defer** → adds `## Resolution: deferred` to signal with reason
   - **Reject** → adds `## Resolution: rejected` to signal with reason
4. Orchestrator links the signal to the mission in both files

### 3c. Mission Lifecycle

States tracked in `work/missions/<slug>/STATUS.md`:

```
created → assigned → in-progress → review → done
```

- **created**: Orchestrator wrote the brief
- **assigned**: Orchestrator assigned it to Coder or Researcher
- **in-progress**: Agent is working (PR opened)
- **review**: PR ready, waiting for your merge
- **done**: PR merged, outcome contract satisfied

### 3d. Definition of Done (DoD)

A mission is **done** when ALL of:

- [ ] `OUTCOME-CONTRACT.md` acceptance criteria are met
- [ ] PR is merged to `main`
- [ ] `STATUS.md` is updated to `done` with completion date
- [ ] **At least one new signal is filed** (what did we learn? what's next?)

> **This is the anti-stall mechanism.** Every completed mission MUST produce at least one signal. This keeps the loop turning. Even "nothing to improve" is a signal worth filing.

---

## 4. Anti-Stall Guarantees

The system stalls when no agent has work. These rules prevent that:

| Rule | How it's enforced |
|------|------------------|
| Every done mission files ≥1 signal | DoD checklist in OUTCOME-CONTRACT |
| Unresolved signals are visible | `work/signals/` — no signal without Resolution section = open |
| Orchestrator runs on schedule | Cron/heartbeat checks `work/signals/` for unresolved items |
| Stuck missions are detectable | STATUS.md has `last_updated` — Triage flags missions idle >48h as a new signal |

**Stall detection query** (run by Triage on cron):
```bash
# Signals without resolution
grep -rL "## Resolution" work/signals/*.md 2>/dev/null

# Missions not updated in 48h
find work/missions/*/STATUS.md -mtime +2 2>/dev/null
```

---

## 5. Bootstrap Checklist

Do these once, in order:

- [ ] Fill `CONFIG.yaml` — at minimum: `company.name`, `vision.north_star`, `vision.mission`
- [ ] Create your first signal: `work/signals/bootstrap.md` — "Product doesn't exist yet. Build MVP."
- [ ] Run Orchestrator to create the first mission from that signal
- [ ] Assign Coder to the mission
- [ ] Merge the first PR
- [ ] Verify the loop: done mission → new signal → new mission

That's it. The system is now self-sustaining.

---

## 6. Recommended Agent Configuration

For OpenClaw / Claude Code / any orchestrator that spawns agents:

```yaml
agents:
  orchestrator:
    model: claude-sonnet-4-20250514
    trigger: cron (every 30min) OR on git push to work/signals/
    reads: work/signals/, work/missions/*/STATUS.md, CONFIG.yaml
    writes: work/missions/

  coder:
    model: claude-sonnet-4-20250514  # or codex for pure code tasks
    trigger: assigned by orchestrator
    reads: work/missions/<assigned>/BRIEF.md, OUTCOME-CONTRACT.md, source code
    writes: source code, tests, STATUS.md

  researcher:
    model: claude-opus-4-20250514
    trigger: assigned by orchestrator (design/research missions)
    reads: work/signals/, work/missions/, external sources
    writes: work/missions/<assigned>/, work/signals/ (new findings)

  triage:
    model: claude-haiku-3-20250514  # cheap, fast
    trigger: cron (every 15min) OR webhook (CI, errors)
    reads: work/signals/, CI output, error logs
    writes: work/signals/ (new + assessed)
```

---

## 7. What You DON'T Need

- ❌ Jira / Linear / project management tool (missions ARE your tickets)
- ❌ Observability platform for agent health (git history IS your audit log)
- ❌ Standup meetings (STATUS.md IS the standup)
- ❌ Org chart (4 agents, you're the boss)
- ❌ OKRs (your Vision + active missions = your strategy)

---

## FAQ

**Q: What if I want to add more agents later?**  
A: Add them as new roles in `org/agents/`. The Orchestrator just needs to know they exist. Start with 4, scale when you feel friction.

**Q: What if signals pile up faster than missions complete?**  
A: That's a signal itself ("too many signals, not enough throughput"). The Orchestrator should prioritize ruthlessly or you should reject low-value signals.

**Q: Can I skip the Researcher agent?**  
A: Yes. Have the Orchestrator do lightweight research and only spawn Researcher for deep-dive missions. Start cheap.

**Q: How do I know it's working?**  
A: `git log --oneline work/` — if commits are flowing, the loop is alive. If nothing for 48h, something stalled.
