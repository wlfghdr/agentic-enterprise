# Automation Patterns

> How to automate agentic-enterprise operations efficiently.

## Principle: Script First, LLM Second

LLM tokens are expensive and slow. Most operational automation in an agentic enterprise is **deterministic** — it can (and should) be scripted. LLMs should only be used for tasks that require understanding, reasoning, or generation.

```
Signal filed → triage_signals.py (script, instant)     ← NOT an LLM call
Pending work → find_pending_work.py (script, instant)   ← NOT an LLM call
Mission brief → LLM agent (reasoning required)          ← YES, this needs an LLM
Task decomposition → LLM agent (reasoning required)     ← YES, this needs an LLM
Code implementation → LLM agent (generation required)   ← YES, this needs an LLM
Morning report → script collects data, LLM formats      ← HYBRID
```

## Classification

### Pure Scripts (no LLM needed)

| Task | Script | Purpose |
|------|--------|---------|
| Signal triage | `scripts/triage_signals.py` | Rule-based disposition of new signals |
| Pending work scan | `scripts/find_pending_work.py` | Find actionable items across missions/signals |
| Approval queue | `scripts/approval_queue.py` | Build list of items awaiting human approval |
| Work archival | `scripts/archive_work.sh` | Move closed/completed items to archive/ |
| Run log archival | `scripts/archive_runs.sh` | Monthly rotation of run artifacts |
| Schema validation | `scripts/validate_schema.py` | Validate YAML/Markdown against schema |
| Governance check | `scripts/check_github_governance.py` | Verify GitHub settings match policy |
| Placeholder check | `scripts/check_placeholders.py` | Detect unfilled template placeholders |
| Lock enforcement | `scripts/check_locks.py` | Verify lock files are respected |

### Pure LLM Tasks (requires understanding/reasoning/generation)

| Task | Agent/Layer | Why LLM? |
|------|-------------|----------|
| Create mission brief from signal | Strategy/Steering | Requires understanding signal context, framing strategic intent |
| Decompose mission into tasks | Orchestration | Requires understanding scope, dependencies, agent capabilities |
| Implement code from task | Execution (Engineering) | Requires code generation |
| Write documentation/content | Execution (Content) | Requires natural language generation |
| Quality evaluation of PR | Quality | Requires understanding code + policies |
| External engagement | Content | Requires reading/writing issue comments with nuance |

### Hybrid (Script collects, LLM decides/formats)

| Task | Pattern | Efficiency gain |
|------|---------|-----------------|
| Morning Report | `approval_queue.py` + `find_pending_work.py` → LLM formats summary | 80% less tokens (LLM only sees pre-filtered data) |
| Dispatch Loop | `find_pending_work.py --json` → LLM decides routing + spawns agents | 90% less tokens (no scanning, only decision) |
| Heartbeat | Script checks (PRs, signals, calendar) → LLM decides "worth reporting?" | 75% less tokens |

## Scheduling

### GitHub Actions (preferred for deterministic checks)
Validation, policy enforcement, security scanning, DORA metrics, stale issue cleanup — all run as workflows triggered by push/PR events. No LLM involved.

### Cron (for periodic LLM tasks)
Only use cron for tasks that **require LLM reasoning**. Always feed scripts' output into the LLM prompt to minimize token usage.

```
# Good: script pre-processes, LLM only formats
1) Run: python3 scripts/find_pending_work.py --json > /tmp/pending.json
2) LLM prompt: "Here is the current pending work: [contents of pending.json]. Format a morning report."

# Bad: LLM does everything
1) LLM prompt: "Scan all missions, check all PRs, read all signals, format a report."
```

### Event-driven (future ideal)
GitHub webhooks → agent dispatch. No polling at all. The agentic-enterprise model supports this via the Operate loop (process/4-operate/).

## Work Backend

Scripts use `work_backend.py` to abstract the storage backend. See `docs/WORK-BACKEND.md` for details on git-files vs. github-issues configuration.
