# GitHub Issues Backend Guide

> **Version:** 1.1 | **Last updated:** 2026-03-08

> **What this document is:** The concrete implementation guide for running operational work artifacts in GitHub Issues. Use this when `CONFIG.yaml → work_backend.type` is `github-issues`.

---

## Goal

This guide makes the GitHub issue backend operational without implicit knowledge.

If a human needs to approve something, the required label change is written out explicitly.
If GitHub needs configuration, the exact repo settings, labels, and issue forms are listed here.

Use this guide together with [WORK-BACKENDS.md](WORK-BACKENDS.md) and [REQUIRED-GITHUB-SETTINGS.md](REQUIRED-GITHUB-SETTINGS.md).

---

## Minimum Setup Checklist

Complete these steps before using the issue backend in a real fork:

1. Set `work_backend.type: "github-issues"` in `CONFIG.yaml`.
2. Enable GitHub Issues and Issue Forms in the repository settings.
3. Copy the sample forms from `docs/github-issues/forms/` into `.github/ISSUE_TEMPLATE/` in your instance repository.
4. Copy `docs/github-issues/config.sample.yml` to `.github/ISSUE_TEMPLATE/config.yml` in your instance repository and customize the links.
5. Create the required labels listed below.
6. Tell humans who approve work to use the approval transitions exactly as written in the approval table.
7. Keep Git-backed companion artifacts in the repository: signal digests, technical designs, quality evaluations, fleet reports, outcome reports, asset registry entries, governance exceptions, and locks.

---

## CONFIG.yaml Sample

Use this as the minimal GitHub-backed configuration:

```yaml
work_backend:
  type: "github-issues"

  github_issues:
    repo: ""                    # empty = same repo
    use_projects: true
    use_label_prefixes: true

  overrides:
    technical-design: "git-files"
    governance-exception: "git-files"
    asset-registry: "git-files"
```

Example for a dedicated issue repository:

```yaml
work_backend:
  type: "github-issues"

  github_issues:
    repo: "acme/operating-work"
    use_projects: true
    use_label_prefixes: true

  overrides:
    technical-design: "git-files"
    governance-exception: "git-files"
    asset-registry: "git-files"
```

---

## Required Labels

These labels are the minimum viable set for the issue backend.

### Artifact Labels

- `artifact:signal`
- `artifact:mission`
- `artifact:task`
- `artifact:decision`
- `artifact:release`
- `artifact:retrospective`

### Status Labels

- `status:new`
- `status:proposed`
- `status:approved`
- `status:planning`
- `status:active`
- `status:paused`
- `status:completed`
- `status:cancelled`
- `status:pending`
- `status:in-progress`
- `status:blocked`
- `status:proceed`
- `status:defer`
- `status:monitor`
- `status:done`
- `status:accepted`
- `status:superseded`
- `status:deprecated`
- `status:draft`
- `status:deploying`
- `status:deployed`
- `status:rolled-back`

### Layer Labels

- `layer:steering`
- `layer:strategy`
- `layer:orchestration`
- `layer:execution`
- `layer:quality`

### Loop Labels

- `loop:discover`
- `loop:build`
- `loop:ship`
- `loop:operate`

### Priority Labels

- `priority:critical`
- `priority:high`
- `priority:medium`
- `priority:low`

### Recommended Additional Labels

- `urgency:immediate`
- `urgency:next-cycle`
- `urgency:monitor`
- `category:market`
- `category:customer`
- `category:technical`
- `category:internal`
- `category:competitive`
- `category:financial`
- `confidence:high`
- `confidence:medium`
- `confidence:low`

### Label Rule

Use exactly one `status:` label per issue.
When the state changes, remove the old `status:*` label and add the new one in the same action.

---

## Label Bootstrap Sample

If you manage labels as code, this YAML structure is a practical starting point:

```yaml
labels:
  - name: "artifact:signal"
    color: "1D76DB"
    description: "Operational signal"
  - name: "artifact:mission"
    color: "5319E7"
    description: "Mission issue"
  - name: "artifact:task"
    color: "0E8A16"
    description: "Mission task"
  - name: "artifact:decision"
    color: "0052CC"
    description: "Decision record"
  - name: "artifact:release"
    color: "FBCA04"
    description: "Release contract"
  - name: "artifact:retrospective"
    color: "B60205"
    description: "Incident retrospective"
  - name: "status:new"
    color: "D4C5F9"
    description: "Freshly filed"
  - name: "status:proposed"
    color: "C2E0C6"
    description: "Awaiting human approval"
  - name: "status:approved"
    color: "0E8A16"
    description: "Approved by authorized human"
  - name: "status:active"
    color: "1D76DB"
    description: "Work is in flight"
  - name: "status:completed"
    color: "5319E7"
    description: "Work completed"
  - name: "status:blocked"
    color: "B60205"
    description: "Blocked pending action"
  - name: "status:draft"
    color: "F9D0C4"
    description: "Draft awaiting approval"
```

If you prefer GitHub CLI, create labels with `gh label create` using the same names.

---

## Human Approval Table

Humans should not have to guess what “approve” means — and they should never need to manage labels.

**How it works:** When an agent needs a human decision, it assigns the issue to the human and leaves a comment that explains what to review and what the options are. The human comments with their decision in plain language and re-assigns to the agent. The agent then applies the correct label.

| Artifact | What the agent's comment tells the human | Human does this |
|----------|------------------------------------------|-----------------|
| Signal | “Please triage this signal. You can: **Proceed** (create a mission), **Defer** (not now), **Monitor** (watch for more data), or **Done** (no action needed). Comment your decision and assign back to me.” | Comment (e.g., “Proceed — this is high priority”) and re-assign to agent |
| Mission | “Please review the scope and outcome contract. You can: **Approve** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment (e.g., “Approved” or “Rejected — scope too broad”) and re-assign to agent |
| Decision | “Please review context and tradeoffs. You can: **Accept** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |
| Release | “Please review rollout and rollback plan. You can: **Approve** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |
| Retrospective | “Please review findings and follow-ups. You can: **Accept** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |

Do not use issue closure as the approval signal.
Closure archives completed work. The label transition (performed by the agent after reading the human's comment) is the approval event.

---

## Assignment Rules

Every issue, PR, and review request must have an assignee. Assignment is how ownership and next-action responsibility are communicated. These rules apply to **all GitHub artifacts**, not just issues.

### Who Gets Assigned — Issues

| Issue state | Assigned to | Rationale |
|-------------|-------------|-----------|
| Newly created, awaiting triage | Triaging human or orchestration agent | Someone must pick it up |
| Agent is executing | Agent bot account | Agent owns the work |
| Awaiting human approval | The approving human | Human must act next |
| Approved, execution continues | The executing agent | Agent resumes work |
| Blocked, needs human input | The human who can unblock | Prevents silent stalls |
| Completed, pending closure | The person closing | Clean handoff |

### Who Gets Assigned — Pull Requests

| PR state | Assigned to | Reviewers | Rationale |
|----------|-------------|-----------|-----------|
| Just opened by agent | Agent bot account | Human(s) from CODEOWNERS or relevant approver | Author owns the PR; reviewer sees it in their queue |
| Changes requested | Agent bot account | Reviewer stays assigned | Agent must address feedback |
| Feedback addressed | Agent bot account | Re-request same reviewer | Reviewer must re-evaluate |
| Approved, ready to merge | Person who merges (human or agent) | — | Clean handoff |
| Blocked by failing checks | Agent bot account | — | Agent investigates |

### Handoff Mechanics — Issues

**Core principle:** Humans comment and re-assign. Agents handle all label management. Humans never need to know the label system.

When work transitions between agent and human:

1. **Agent finishes, needs approval:** Agent sets the `status:` label, re-assigns to the approving human, and leaves a comment that (a) summarizes what was done, (b) explains what to review, and (c) lists the human's options in plain language (e.g., "You can: **Approve** — comment 'approved' and assign back to @acme-ai-bot | **Reject** — comment what needs to change and assign back to @acme-ai-bot").
2. **Human decides:** Human comments with their decision in plain language (e.g., "Approved", "Looks good, go ahead", "Rejected — need more detail on rollback") and re-assigns to the agent.
3. **Agent processes decision:** Agent reads the comment, interprets the decision, applies the appropriate label change, and continues. If the comment is ambiguous, the agent asks a clarifying question and keeps the issue assigned to the human.

### Handoff Mechanics — Pull Requests

1. **Agent opens PR:** Agent creates the PR, assigns itself, requests review from the appropriate human(s), and writes a description that summarizes the change, links to the originating issue/task, explains what to focus on, and lists the reviewer's options (approve, request changes, comment).
2. **Reviewer acts:** Reviewer submits a GitHub review. No re-assignment needed — GitHub's review system handles notification.
3. **Agent processes review:** If approved and the agent has merge permission, it merges. If changes are requested, the agent addresses them, pushes, and re-requests review with a comment summarizing what changed. If the review is unclear, the agent asks for clarification on the PR.
4. **Merge handoff:** If branch protection requires a human to merge, the agent comments that the PR is ready and assigns it to the human who should merge.

### Agent Identity

Agents must use a dedicated GitHub bot/user account (e.g., `acme-ai-bot`) so that human-owned and agent-owned items are visually distinguishable at a glance — across issues, PRs, and reviews.

---

## Human Operating Rules

These rules keep GitHub collaboration consistent. **You never need to manage labels — agents do that.**

### For Issues
1. Always leave a short comment when approving, rejecting, or requesting changes. Plain language is fine — the agent interprets it.
2. After commenting, always re-assign the issue to the agent (or next responsible human). Never leave an issue assigned to yourself after you've made your decision.
3. Never leave an issue unassigned — if you are done with your part, assign it forward.
4. Close child task issues before closing the parent mission issue.
5. For missions, keep the issue body as the current mission brief and use comments for running status updates.
6. For tasks, put acceptance criteria directly in the task issue body so execution and quality agents can evaluate against them.
7. If the agent's handoff comment lists your options, pick one and state it clearly. If none of the options fit, explain what you'd prefer instead.

### For Pull Requests
1. When assigned as a reviewer, submit a GitHub review (approve, request changes, or comment). The PR description explains what to focus on.
2. If you request changes, be specific about what needs to change — the agent will address your feedback and re-request your review.
3. If branch protection requires you to merge, do so after all checks pass. The agent will comment when the PR is ready.
4. Never leave a PR without reviewers — if you can't review it, re-assign the review to someone who can.

---

## Sample Files To Copy Into An Instance Repo

This template repository keeps the operational GitHub issue forms as documentation samples so the framework repo itself does not behave like an instance repo.

Copy these into `.github/ISSUE_TEMPLATE/` in your company fork when you enable the issue backend:

- `docs/github-issues/config.sample.yml`
- `docs/github-issues/forms/signal.sample.yml`
- `docs/github-issues/forms/mission.sample.yml`
- `docs/github-issues/forms/task.sample.yml`
- `docs/github-issues/forms/decision.sample.yml`
- `docs/github-issues/forms/release.sample.yml`
- `docs/github-issues/forms/retrospective.sample.yml`

These samples pre-apply the base artifact labels and ask for the fields humans typically forget.

---

## GitHub Projects Recommendation

If `use_projects: true`, create these minimum views:

| Project View | Filter |
|--------------|--------|
| Signal Triage | `label:artifact:signal is:open` |
| Active Missions | `label:artifact:mission is:open` |
| Mission Tasks | `label:artifact:task is:open` |
| Release Pipeline | `label:artifact:release is:open` |

---

## Companion Git Artifacts That Still Matter

Even with GitHub Issues enabled, these stay in Git:

- `work/signals/digests/`
- `work/missions/<name>/TECHNICAL-DESIGN.md`
- `work/missions/<name>/evaluations/`
- `work/missions/<name>/FLEET-REPORT.md`
- `work/missions/<name>/OUTCOME-REPORT.md`
- `work/assets/`
- `work/decisions/EXC-*.md`
- `work/locks/`

The issue backend is for operational coordination.
Git still holds the durable review-heavy artifacts.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-03-08 | Added assignment rules for issues and PRs, handoff mechanics for both, agent identity requirement, human operating rules for issues and PRs, comment-based approval model |
| 1.0 | 2026-03-07 | Initial version — concrete GitHub issue-backend implementation guide |