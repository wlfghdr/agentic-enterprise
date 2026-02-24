# Mission Lifecycle Guide

> **Purpose:** End-to-end reference for how missions flow from proposal through completion. Documents status transitions, the Divide & Conquer decomposition pattern, gate requirements, and common failure modes.
>
> **Audience:** All layers. Orchestration and Execution agents reference this guide most frequently, but Strategy and Quality agents also need to understand the lifecycle to time their contributions correctly.

---

## The Divide & Conquer Pattern

Missions follow a decomposition pattern that turns strategic intent into executable work:

```
SIGNAL                          Observation filed by any agent or human
  ↓  Discover Loop
MISSION BRIEF (BRIEF.md)        Strategic intent, outcomes, constraints
  ↓  Strategy Layer approves
OUTCOME CONTRACT                Measurable success criteria
  ↓  Orchestration Layer decomposes
FLEET CONFIG                    Agent pool composition and stream structure
  ↓  Orchestrator decomposes further
TASKS (TASKS.md)                Concrete, assignable work items
  ↓  Execution Agents pick up
ASSETS (commits, PRs, files)    Delivered artifacts with registry entries
  ↓  Quality Layer evaluates
OUTCOME REPORT                  Targets vs. actuals measurement
```

Each arrow represents a **Git PR** with **CODEOWNERS-enforced approval**. The Git history is the audit trail.

### Who Does What

| Role | Responsibility |
|------|---------------|
| **Strategy Layer** | Defines the mission brief and outcome contract. Approves mission scope. |
| **Orchestrator** | Decomposes BRIEF.md into Fleet Config and TASKS.md. Monitors progress. |
| **Execution Agents** | Pick up tasks from TASKS.md, execute, update status, generate assets. |
| **Quality Layer** | Evaluates outputs against policies. Issues verdicts. |
| **Steering Layer** | Aggregates signals, approves structural changes, owns company evolution. |

---

## Mission Statuses

| Status | Meaning |
|--------|---------|
| **proposed** | Brief created, awaiting Strategy Layer approval |
| **approved** | Approved by Strategy Layer, ready for orchestration |
| **planning** | Orchestrator creating fleet config and decomposing tasks |
| **active** | Tasks exist and execution agents are working |
| **paused** | Temporarily suspended by human decision |
| **completed** | Outcomes measured, mission closed |
| **cancelled** | Terminated before completion, with documented rationale |

---

## Status Transitions and Gates

Every status transition has a **gate** — a condition that must be satisfied before the transition can occur. Gates prevent missions from advancing into states where downstream agents cannot act.

```
proposed ──→ approved ──→ planning ──→ active ──→ completed
                                        ↕            ↑
                                      paused ────────┘
                          ↑
    ╌╌╌╌╌╌╌╌ any status ╌╌╌╌╌╌╌╌ ──→ cancelled
```

| From | To | Gate | Who |
|------|----|------|-----|
| `proposed` | `approved` | Strategy Layer human approves Mission Brief via PR merge | Strategy Layer human |
| `approved` | `planning` | Orchestrator creates Fleet Config; Technical Design initiated if `design-required: true` | Orchestrator |
| `planning` | `active` | **TASKS.md exists with at least one task.** Technical Design approved (if required). | Orchestrator (gate checked by Orchestrator and CI) |
| `active` | `paused` | Human decision — resource conflict, external blocker, reprioritization | Human (any layer) |
| `paused` | `active` | Human decision; original gate conditions still satisfied | Human (any layer) |
| `active` | `completed` | Outcome Report produced; outcomes measured against contract | Strategy Layer + Orchestrator |
| _any_ | `cancelled` | Human decision with documented rationale in STATUS.md | Human (Strategy or Steering) |

### The Critical Gate: `planning` → `active`

This is the gate that Issue #56 identified as the most failure-prone transition. The invariant is:

> **A mission cannot transition to `active` without a TASKS.md file containing at least one decomposed task.**

Without this gate, execution agents have nothing to pick up. The mission appears active but is effectively dead — a silent failure that is hard to diagnose.

**Exception — missions without Execution tasks:** Some missions are scoped entirely to Strategy or Steering considerations (e.g., market analysis, policy evolution, organizational restructuring). These missions produce artifacts like decision records, evolution proposals, or policy updates — but they do not generate TASKS.md because no Execution Layer work is involved. Such missions may transition to `active` without TASKS.md, provided this is explicitly documented in the Mission Brief's Scope section with a rationale.

---

## Task Decomposition

When the Orchestrator decomposes a mission into tasks, the following criteria apply:

### Task Granularity
- Each task should be independently deliverable by a single agent or agent pool
- Tasks should be completable within one work cycle
- If a task requires coordination across multiple divisions, split it into division-aligned subtasks

### Task Assignment Criteria

| Criterion | Description |
|-----------|-------------|
| **Division alignment** | The owning division determines which agents are eligible |
| **Agent capability matching** | Tasks route to agents with the right skills (infra, frontend, data, etc.) |
| **Capacity and parallelization** | Independent tasks can run in parallel across agents |
| **Dependency ordering** | Dependent tasks must declare blockers explicitly to prevent agents from waiting on each other |

### Asset Entry Generation

Every completed task should generate **asset entries** (`work/assets/_TEMPLATE-asset-registry-entry.md`). This provides:

- **Traceability**: Mission → Task → Asset chain is auditable
- **Progress tracking**: Completed tasks with assets = measurable progress
- **Handoff documentation**: Future agents or humans can trace why something was built

---

## Mission Folder Structure

A fully active mission folder contains:

```
work/missions/<mission-name>/
├── BRIEF.md                 # Mission brief (from template)
├── OUTCOME-CONTRACT.md      # Measurable success criteria
├── TASKS.md                 # Decomposed work items (REQUIRED for active status)
├── STATUS.md                # Progress updates (append-only, latest first)
├── TECHNICAL-DESIGN.md      # Technical design (if design-required: true)
├── FLEET-REPORT.md          # Fleet performance report (optional)
├── OUTCOME-REPORT.md        # Final outcome measurement (mission closure)
└── evaluations/             # Quality evaluation reports
    └── YYYY-MM-DD-<eval>.md # Individual quality evaluations
```

---

## Common Failure Modes (Anti-Patterns)

These are known failure modes from real operating instances. Each has a named pattern and a documented fix.

### 1. The Wishful Mission

**Symptom:** Mission is `active` but has no TASKS.md. Execution agents find nothing to work on.

**Root cause:** Orchestrator skipped task decomposition, or the mission was fast-tracked from `approved` directly to `active`.

**Fix:** Enforce the `planning → active` gate. No TASKS.md = no `active` status.

### 2. The Orphan Task

**Symptom:** Tasks exist in TASKS.md but have no division assignment or agent type.

**Root cause:** Task decomposition was too abstract — tasks were written as goals, not assignable work.

**Fix:** Every task must have an `Assigned to` field with a division and agent type. Tasks without assignment are not actionable.

### 3. The Invisible Delivery

**Symptom:** Tasks are completed but no asset entries exist. Progress is undocumented.

**Root cause:** Execution agents completed work but did not file asset registry entries.

**Fix:** Acceptance criteria in each task should include asset entry generation. The Orchestrator verifies asset entries during status updates.

### 4. The Circular Block

**Symptom:** Two or more tasks are mutually dependent (`TASK-A depends on TASK-B`, `TASK-B depends on TASK-A`). Neither can start.

**Root cause:** Task decomposition did not properly sequence dependencies.

**Fix:** The Orchestrator reviews the dependency graph before setting status to `active`. Circular dependencies must be broken by splitting tasks or identifying the true ordering.

### 5. The Zombie Mission

**Symptom:** Mission is `active` but no status updates have been filed for multiple cycles. No blockers documented.

**Root cause:** Orchestrator lost track, or execution agents silently stalled.

**Fix:** The Orchestrator produces weekly STATUS.md entries for all active missions. A mission with no status update for 2+ cycles should be flagged by a signal and triaged — either pause, cancel, or unblock it.

---

## Lifecycle in the 4-Loop Model

The mission lifecycle spans multiple process loops:

| Loop | Mission phase | Key activities |
|------|--------------|----------------|
| **Loop 1: Discover** | `proposed` → `approved` | Signal detection, triage, mission brief drafting, Strategy Layer approval |
| **Loop 2: Build** | `planning` → `active` | Fleet config, task decomposition, execution, quality evaluation |
| **Loop 3: Ship** | `active` → `completed` | Release contract, deployment, outcome measurement, outcome report |
| **Loop 4: Operate** | Post-`completed` | Production monitoring, incident response, improvement signals |

Missions that are `cancelled` can originate from any loop — the cancellation rationale is documented in STATUS.md and any lessons learned are captured as signals for future reference.

---

## Quick Reference: Templates

| Artifact | Template | When created |
|----------|----------|-------------|
| Mission Brief | `work/missions/_TEMPLATE-mission-brief.md` | Discover loop — signal validated |
| Outcome Contract | `work/missions/_TEMPLATE-outcome-contract.md` | Discover loop — with brief |
| Tasks | `work/missions/_TEMPLATE-tasks.md` | Planning phase — Orchestrator decomposes |
| Fleet Config | `org/2-orchestration/fleet-configs/_TEMPLATE-fleet-config.md` | Planning phase — Orchestrator configures |
| Technical Design | `work/missions/_TEMPLATE-technical-design.md` | Planning phase — if design-required |
| Status Log | `work/missions/_TEMPLATE-mission-status.md` | Active phase — weekly updates |
| Quality Evaluation | `work/missions/_TEMPLATE-quality-evaluation-report.md` | Build loop — per output |
| Fleet Performance | `work/missions/_TEMPLATE-fleet-performance-report.md` | Active phase — periodic |
| Outcome Report | `work/missions/_TEMPLATE-outcome-report.md` | Ship loop — mission closure |
| Asset Entry | `work/assets/_TEMPLATE-asset-registry-entry.md` | Per completed task |
