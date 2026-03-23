# Work — Active Work Tracking

> **What this is:** The artifact definitions and templates for tracking operational work.
> **Backend:** Where these artifacts live depends on `CONFIG.yaml → work_backend`. See [docs/work-backends.md](../docs/work-backends.md).
> - **Git-files backend** (default): Artifacts are Markdown files in this folder. This is the only folder that changes frequently.
> - **Issue backend** (e.g., GitHub Issues): Artifacts are tracked as issues with structured labels. This folder contains only templates (as schema definitions) and persistent documentation artifacts.

---

## Structure

**Git-files backend** — all artifacts live here:

```
work/
├── signals/              # Incoming observations from all sources
│   ├── digests/          # Weekly signal digests (Steering Layer)
│   └── README.md
├── missions/             # Active and completed missions
│   └── README.md
├── decisions/            # Architecture decisions + Governance Exceptions
│   └── README.md
├── releases/             # Release contracts for shipped software
│   └── README.md
├── assets/               # Asset registry entries (non-code deliverables)
│   └── README.md
├── retrospectives/       # Postmortems and incident reports
│   └── README.md
└── locks/                # Concurrency locks for critical shared files
    └── README.md
```

**Issue backend** — only these remain in Git:

```
work/
├── assets/               # Asset registry entries (always in Git)
├── missions/             # Git-backed mission evidence and design artifacts
│   └── <name>/
│       ├── TECHNICAL-DESIGN.md
│       ├── FLEET-REPORT.md
│       ├── OUTCOME-REPORT.md
│       └── evaluations/
├── decisions/            # Governance exceptions (always in Git)
│   └── EXC-*.md
├── signals/
│   └── digests/          # Weekly signal digests (always in Git)
├── locks/                # Concurrency locks (always in Git)
└── _TEMPLATE-*.md        # Schema definitions (always in Git)
```

## How It Works

### Git-Files Backend

| Folder | What Goes Here | Template | Who Creates |
|--------|---------------|----------|-------------|
| `signals/` | Market, customer, technical, internal observations | `work/signals/_TEMPLATE-signal.md` | Anyone |
| `signals/digests/` | Weekly signal digest summaries | `work/signals/digests/_TEMPLATE-signal-digest.md` | Steering Layer |
| `missions/` | Mission briefs, outcome contracts, status updates, outcome reports, quality evaluations | `work/missions/_TEMPLATE-mission-brief.md` | Strategy Layer |
| `decisions/` | Architecture and strategy decisions | `work/decisions/_TEMPLATE-decision-record.md` | Any Layer |
| `decisions/` | Time-bounded policy exceptions (approved by Policy Author + Steering) | `work/decisions/_TEMPLATE-governance-exception.md` | Any Layer (human approval required) |
| `releases/` | Release contracts for shipped software | `work/releases/_TEMPLATE-release-contract.md` | Ship Loop (Orchestration) |
| `assets/` | Non-code deliverable registry entries | `work/assets/_TEMPLATE-asset-registry-entry.md` | Execution Layer |
| `retrospectives/` | Postmortems and incident reports | `work/retrospectives/_TEMPLATE-postmortem.md` | Operate Loop agents |
| `locks/` | Concurrency locks for critical shared files | `work/locks/_TEMPLATE-lock.md` | Any agent or human editing a protected file |

### Issue Backend (e.g., GitHub Issues)

| Artifact | Label | Who Creates | Approval |
|----------|-------|-------------|----------|
| Signal | `artifact:signal` | Anyone | Project Status → `Approved` by Steering |
| Mission | `artifact:mission` | Strategy Layer | Project Status → `Approved` |
| Task | `artifact:task` (sub-issue of mission) | Orchestration Layer | Project Status transitions; approval/handoff rules live in `docs/github-issues.md` |
| Decision | `artifact:decision` | Any Layer | Project Status → `Done` (accepted) |
| Release | `artifact:release` | Orchestration Layer | Project Status → `Approved` |
| Retrospective | `artifact:retrospective` | Operate Loop | Project Status → `Done` (accepted) |

Git-only companion artifacts still apply in issue backend: signal digests, technical designs, evaluation reports, fleet reports, outcome reports, asset registry entries, governance exceptions, and locks.

See [docs/work-backends.md](../docs/work-backends.md) for the full label taxonomy and [docs/github-issues.md](../docs/github-issues.md) for the GitHub setup guide.

## Naming Conventions

- **Signals:** `YYYY-MM-DD-<descriptive-name>.md`
- **Signal Digests:** `YYYY-WXX-digest.md` (ISO week number)
- **Missions:** `<mission-name>/BRIEF.md` (folder per mission)
- **Mission Status:** `<mission-name>/STATUS.md` (append-only updates)
- **Outcome Reports:** `<mission-name>/OUTCOME-REPORT.md` (mission closure)
- **Quality Evaluations:** `<mission-name>/evaluations/YYYY-MM-DD-<eval-name>.md`
- **Decisions:** `YYYY-MM-DD-<descriptive-name>.md`
- **Governance Exceptions:** `EXC-YYYY-NNN-<descriptive-name>.md` (e.g., `EXC-2026-001-skip-coverage-gate.md`)
- **Releases:** `YYYY-MM-DD-<release-name>.md`
- **Assets:** `<descriptive-asset-name>.md`
- **Retrospectives:** `YYYY-MM-DD-<incident-name>.md`
- **Locks:** `<lock-id>.md` where lock-id is path-derived slug (e.g., `org-4-quality-policies-security-md.md`)

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
