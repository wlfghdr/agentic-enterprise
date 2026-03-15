# 10-Minute Quickstart

> Understand the Agentic Enterprise operating model by walking through its core workflow — from observation to release — in 10 minutes.

## The Core Idea

Everything in Agentic Enterprise follows one loop:

```
Observe → Decide → Execute → Ship → Learn → Repeat
```

The artifacts that drive this loop are:

| Step | Artifact | Location |
|------|----------|----------|
| Observe | **Signal** | `work/signals/` |
| Decide | **Mission Brief** | `work/missions/` |
| Execute | **Pull Request** | GitHub |
| Ship | **Release** | `work/releases/` |
| Learn | **New Signal** | `work/signals/` |

That's it. The entire operating model is a structured way to move through these steps with governance, quality gates, and audit trails.

---

## Step 1: Clone the Repository (1 min)

```bash
git clone https://github.com/wlfghdr/agentic-enterprise.git
cd agentic-enterprise
```

Browse the repo structure. The key directories are:

- `org/` — Organizational structure (who does what)
- `process/` — Process definitions (how work flows)
- `work/` — Active work artifacts (what's happening now)
- `org/4-quality/policies/` — Quality policies (the rules)

---

## Step 2: Create a Signal (2 min)

A **Signal** is an observation — something you noticed that might require action. It's the entry point for all work.

Create a new file `work/signals/2026-03-14-api-docs-outdated.md`:

```markdown
# Signal: API Documentation Is Outdated

> **Created:** 2026-03-14
> **Revision:** 1 | **Last updated:** 2026-03-14
> **Author:** Jane (Engineering Lead)

---

## Source

- **Category:** technical
- **Source system:** Customer support tickets
- **Confidence:** high

## Observation

Three customer support tickets this week referenced incorrect API endpoints
in our public documentation. The docs were last updated 4 months ago and
no longer match the current API surface.

## Initial Assessment

- **Urgency:** next-cycle
- **Potential impact:** medium
- **Affected divisions:** knowledge-enablement, core-applications

## Recommended Disposition

- [x] Proceed to opportunity validation
```

**What just happened:** You created a structured observation that anyone (human or agent) can triage. It's version-controlled, linked to a source, and has a clear recommendation.

---

## Step 3: Convert to a Mission (3 min)

A human reviews the signal and decides: "Yes, this is worth doing." The signal becomes a **Mission Brief** — a scoped piece of work with clear outcomes.

Create `work/missions/MISSION-2026-012-api-docs-refresh/BRIEF.md`:

```markdown
# Mission Brief: API Documentation Refresh

> **Mission ID:** MISSION-2026-012
> **Status:** approved
> **Created:** 2026-03-14
> **Author:** Strategy Layer

---

## Origin

- **Signal(s):** `work/signals/2026-03-14-api-docs-outdated.md`
- **Sponsor:** Jane (Engineering Lead)

## Objective

Update all public API documentation to match the current API surface,
eliminating customer confusion and reducing support tickets by 50%.

## Scope

### In Scope
- Audit current API endpoints against documentation
- Update all outdated endpoint references
- Add missing endpoints from the last 4 months

### Out of Scope
- API redesign or breaking changes
- Internal API documentation

## Outcome Contract

| Metric | Target | Deadline |
|--------|--------|----------|
| Documentation accuracy | 100% of endpoints documented | 2026-03-28 |
| Support ticket reduction | 50% fewer docs-related tickets | 2026-04-14 |

## Human Checkpoints

1. **Scope review** — Before work begins → Engineering Lead
2. **Final review** — Before publishing → Engineering Lead
```

**What just happened:** The signal became actionable work with clear scope, measurable outcomes, and human approval gates.

---

## Step 4: Do the Work via Pull Request (2 min)

Work happens through Git. An agent (or human) creates a branch, makes changes, and opens a PR.

```bash
git checkout -b mission/2026-012-api-docs-refresh
# ... make the documentation changes ...
git add docs/api/
git commit -m "docs: update API endpoints to match current surface

Mission: MISSION-2026-012
Signal: 2026-03-14-api-docs-outdated"
git push -u origin mission/2026-012-api-docs-refresh
```

The PR description links back to the mission. Reviewers are assigned per `CODEOWNERS`. CI runs quality checks. A human approves and merges.

**What just happened:** The change is tracked, reviewed, and linked to the mission that authorized it. Git history is the audit trail.

---

## Step 5: Document the Release (1 min)

After the PR merges, create a release record in `work/releases/`:

```markdown
# Release: API Documentation Refresh

> **Release ID:** REL-2026-012
> **Created:** 2026-03-28
> **Mission:** MISSION-2026-012

## What Shipped

- Updated 47 API endpoint references
- Added 12 new endpoint entries
- Removed 3 deprecated endpoint references

## Outcome Measurement

| Metric | Target | Actual |
|--------|--------|--------|
| Documentation accuracy | 100% | 100% |
| Support ticket reduction | 50% | Measuring (check 2026-04-14) |
```

**What just happened:** The release is documented with measurable outcomes tied back to the original mission and signal.

---

## Step 6: The Loop Closes (1 min)

Two weeks later, support ticket data shows a 62% reduction in docs-related tickets. This is recorded in the mission's outcome report.

But during the docs refresh, someone noticed that the API versioning strategy is inconsistent. They file a **new signal**:

```markdown
# Signal: API Versioning Strategy Inconsistent

> **Created:** 2026-03-25
> **Author:** Agent (during MISSION-2026-012 execution)

## Observation

While updating API docs, found that 3 services use path-based versioning
(/v1/, /v2/) while 2 services use header-based versioning. No documented
standard exists.
```

And the loop begins again: Signal → Mission → PR → Release → Signal → ...

---

## What You Just Learned

In 10 minutes, you walked through the complete operating loop:

```
Signal (observation)
  → Mission (scoped decision)
    → PR (governed execution)
      → Release (documented outcome)
        → Signal (new observation)
```

Every step is:
- **Version-controlled** — Git history is the audit trail
- **Human-governed** — Humans approve at key checkpoints
- **Agent-ready** — Any AI agent can read and participate in this workflow
- **Traceable** — Every artifact links to the one before it

## Next Steps

- [End-to-end example](../../examples/e2e-loop/) — See a complete lifecycle with all artifacts
- [Minimal Adoption Guide](../adoption/minimal-adoption.md) — Start using the framework today
- [Architecture Overview](../architecture/agentic-enterprise-architecture.md) — Understand the full system
- [customization-guide.md](../customization-guide.md) — Full onboarding walkthrough
