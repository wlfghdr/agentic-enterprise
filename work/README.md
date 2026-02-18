# Work — Active Work Tracking

> **What this is:** The living workspace where signals, missions, and decisions are tracked.  
> **Convention:** This is the only folder that changes frequently. Everything else (`org/`, `process/`) changes slowly and deliberately.

---

## Structure

```
work/
├── signals/              # Incoming observations from all sources
│   ├── digests/          # Weekly signal digests (Steering Layer)
│   └── README.md
├── missions/             # Active and completed missions
│   └── README.md
├── decisions/            # Architecture and strategy decisions
│   └── README.md
├── releases/             # Release contracts for shipped software
│   └── README.md
├── assets/               # Asset registry entries (non-code deliverables)
│   └── README.md
└── retrospectives/       # Postmortems and incident reports
    └── README.md
```

## How It Works

| Folder | What Goes Here | Template | Who Creates |
|--------|---------------|----------|-------------|
| `signals/` | Market, customer, technical, internal observations | `work/signals/_TEMPLATE-signal.md` | Anyone |
| `signals/digests/` | Weekly signal digest summaries | `work/signals/digests/_TEMPLATE-signal-digest.md` | Steering Layer |
| `missions/` | Mission briefs, outcome contracts, status updates, outcome reports, quality evaluations | `work/missions/_TEMPLATE-mission-brief.md` | Strategy Layer |
| `decisions/` | Architecture and strategy decisions | `work/decisions/_TEMPLATE-decision-record.md` | Any Layer |
| `releases/` | Release contracts for shipped software | `work/releases/_TEMPLATE-release-contract.md` | Ship Loop (Orchestration) |
| `assets/` | Non-code deliverable registry entries | `work/assets/_TEMPLATE-asset-registry-entry.md` | Execution Layer |
| `retrospectives/` | Postmortems and incident reports | `work/retrospectives/_TEMPLATE-postmortem.md` | Operate Loop agents |

## Naming Conventions

- **Signals:** `YYYY-MM-DD-<descriptive-name>.md`
- **Signal Digests:** `YYYY-WXX-digest.md` (ISO week number)
- **Missions:** `<mission-name>/BRIEF.md` (folder per mission)
- **Mission Status:** `<mission-name>/STATUS.md` (append-only updates)
- **Outcome Reports:** `<mission-name>/OUTCOME-REPORT.md` (mission closure)
- **Quality Evaluations:** `<mission-name>/evaluations/YYYY-MM-DD-<eval-name>.md`
- **Decisions:** `YYYY-MM-DD-<descriptive-name>.md`
- **Releases:** `YYYY-MM-DD-<release-name>.md`
- **Assets:** `<descriptive-asset-name>.md`
- **Retrospectives:** `YYYY-MM-DD-<incident-name>.md`

## Lifecycle

```
signal → triage → opportunity → mission brief → execution → outcome → feedback
    ↑                                               │            │        │
    │                              quality eval ←────┘            │        │
    │                              release contract ──→ deploy    │        │
    │                              asset registry entries         │        │
    │                              outcome report ────────────────┘        │
    │                              venture health rollup                   │
    └──────────────────────── new signals ←───────────────────────────────┘
```
