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
| `signals/` | Market, customer, technical, internal observations | `process/templates/signal.md` | Anyone |
| `signals/digests/` | Weekly signal digest summaries | `process/templates/signal-digest.md` | Steering Layer |
| `missions/` | Mission briefs, outcome contracts, status updates, outcome reports, quality evaluations | `process/templates/mission-brief.md` | Strategy Layer |
| `decisions/` | Architecture and strategy decisions | `process/templates/decision-record.md` | Any Layer |
| `releases/` | Release contracts for shipped software | `process/templates/release-contract.md` | Ship Loop (Orchestration) |
| `assets/` | Non-code deliverable registry entries | `process/templates/asset-registry-entry.yaml` | Execution Layer |
| `retrospectives/` | Postmortems and incident reports | `process/templates/postmortem.md` | Operate Loop agents |

## Naming Conventions

- **Signals:** `YYYY-MM-DD-<descriptive-name>.md`
- **Signal Digests:** `YYYY-WXX-digest.md` (ISO week number)
- **Missions:** `<mission-name>/BRIEF.md` (folder per mission)
- **Mission Status:** `<mission-name>/STATUS.md` (append-only updates)
- **Outcome Reports:** `<mission-name>/OUTCOME-REPORT.md` (mission closure)
- **Quality Evaluations:** `<mission-name>/evaluations/YYYY-MM-DD-<eval-name>.md`
- **Decisions:** `YYYY-MM-DD-<descriptive-name>.md`
- **Releases:** `YYYY-MM-DD-<release-name>.md`
- **Assets:** `<descriptive-asset-name>.yaml`
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
