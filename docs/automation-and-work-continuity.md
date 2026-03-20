# Automation and Work Continuity

> Short operational rules for keeping the operating model alive without creating noisy loops.

This guide defines the minimum automation expectations once a team uses the framework with recurring agent or automation passes.

## Core Rule

**Open assigned work should not be silently abandoned.**

That includes:
- assigned issues
- open PRs
- requested reviews
- active missions
- open tasks linked to an approved mission
- open signals that already have enough clarity for direct triage or decomposition

The default expectation is: revisit, continue, close, escalate, or explicitly pause.

## What a Continuity Pass Checks

A compact continuity pass should review:

1. open assigned issues and PRs
2. review requests
3. active or blocked missions
4. open tasks under active missions
5. referenced product-repo issues that belong to those missions

The pass should prefer one compact sweep over many tiny loops.

## Self-Assignment Defaults

Use self-assignment only when all of the following are true:
- the repo permits agent-owned work items
- the task is clearly executable without new human scope decisions
- the work is operationally useful to mark as owned

Good candidates:
- documentation gaps
- broken links
- missing wiring for already-approved behavior
- clearly scoped follow-up tasks derived from an approved mission

Do **not** self-assign when:
- approval or prioritization is still unclear
- scope changes strategy, roadmap, architecture, security posture, or spend
- the work would look like an implicit human decision

## Approval Boundaries

Agents may continue execution inside already-approved scope.

Agents should **not** silently push missions across human decision gates such as:
- approving a mission brief
- materially expanding mission scope
- shipping sensitive production changes without the expected approval path
- merging changes that repo policy expects humans to review
- closing strategic questions that the mission explicitly leaves for a human

When approval is needed, create or update the artifact so the next human decision is easy:
- summarize current state
- state the blocking decision
- link the exact issue, PR, or mission
- stop there

## Backoff and Cadence

Avoid tight loops.

Recommended pattern:
- run a compact scheduled pass (for example daily, twice daily, or workday morning/evening)
- do one useful sweep per run
- prefer batched updates over repetitive micro-comments
- if nothing is clearly actionable, leave the system quiet

Bad pattern:
- polling every few minutes
- repeated "still blocked" comments
- creating many tiny follow-up issues that should have been one pass

## Daily / Morning Review Expectation

A healthy instance usually has one lightweight review rhythm:
- check assigned work
- check open reviews
- check active missions and blocked tasks
- continue what is executable
- escalate what needs a human

This can be done by a human, an agent, or scheduled automation.

## Cross-Repo Continuity Rule

If a mission in the instance repo creates product work in another repo, continuity should follow the full chain:

`signal -> mission -> task -> product issue -> PR`

At minimum, the mission or task should link to the product issue, and the product issue should link back to the originating mission.

## Practical Outcome States

After each continuity pass, each reviewed item should land in one of five states:
- **done** — completed and closed
- **in progress** — actively advanced
- **blocked** — waiting on a named dependency
- **awaiting approval** — waiting on an explicit human decision
- **not now** — intentionally deferred with rationale

The important thing is not constant activity. The important thing is that open work remains explainable.
