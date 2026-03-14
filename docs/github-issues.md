# GitHub Issues Backend Guide

> **Version:** 2.1 | **Last updated:** 2026-03-09

> **What this document is:** The concrete implementation guide for running operational work artifacts in GitHub Issues. Use this when `CONFIG.yaml → work_backend.type` is `github-issues`.

---

## Goal

This guide makes the GitHub issue backend operational without implicit knowledge.

If a human needs to approve something, the required status transition is written out explicitly.
If GitHub needs configuration, the exact repo settings, labels, project setup, and issue forms are listed here.

Use this guide together with [work-backends.md](work-backends.md), [required-github-settings.md](required-github-settings.md), and [github/README.md](github/README.md).

---

## Minimum Setup Checklist

Complete these steps before using the issue backend in a real fork:

1. Set `work_backend.type: "github-issues"` in `CONFIG.yaml`.
2. Enable GitHub Issues and Issue Forms in the repository settings.
3. **Create a GitHub Project (v2)** with a **Status** field containing these single-select options: `Backlog`, `Triage`, `Approved`, `Planning`, `In Progress`, `Blocked`, `Done`. Set `project_owner` and `project_number` in `CONFIG.yaml`.
4. Copy the sample forms from `docs/github/issue-templates/forms/` into `.github/ISSUE_TEMPLATE/` in your instance repository.
5. Copy `docs/github/issue-templates/config.sample.yml` to `.github/ISSUE_TEMPLATE/config.yml` in your instance repository and customize the links.
6. Create the required labels listed below. (Note: status is tracked via the Project Status field, not via labels.)
7. Tell humans who approve work to use the approval transitions exactly as written in the approval table.
8. Keep Git-backed companion artifacts in the repository: signal digests, technical designs, quality evaluations, fleet reports, outcome reports, asset registry entries, governance exceptions, and locks.

---

## CONFIG.yaml Sample

Use this as the minimal GitHub-backed configuration:

```yaml
work_backend:
  type: "github-issues"

  github_issues:
    repo: ""                    # empty = same repo
    use_projects: true
    project_owner: ""           # GitHub org or user owning the project
    project_number: 0           # GitHub Project v2 number
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
    project_owner: "acme"
    project_number: 2
    use_label_prefixes: true

  overrides:
    technical-design: "git-files"
    governance-exception: "git-files"
    asset-registry: "git-files"
```

---

## Required Labels

These labels are the minimum viable set for the issue backend. **Status is tracked via the GitHub Project Status field, not via labels** — see the Status Tracking section below.

### Artifact Labels

- `artifact:signal`
- `artifact:mission`
- `artifact:task`
- `artifact:decision`
- `artifact:release`
- `artifact:retrospective`

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

---

## Status Tracking via GitHub Project

**Status is a workflow state — it belongs in the GitHub Project Status field, not in labels.** Labels are for categorization (artifact type, priority, layer, loop, division). Status is a single-select field with ordered transitions that naturally produce a Kanban board.

### Project Status Field Options

| Project Status | Meaning |
|----------------|---------|
| Backlog | Newly filed or not yet prioritized |
| Triage | Being evaluated (signals undergoing triage) |
| Approved | Approved by human, waiting for capacity |
| Planning | Being decomposed into tasks (missions) |
| In Progress | Actively being worked on |
| Blocked | Waiting on a dependency |
| Done | Work completed — ready to close |

### Terminal States

Terminal states use GitHub's native **close** mechanism, not a project status:

- **Completed** → close the issue (reason: `completed`)
- **Cancelled** → close the issue (reason: `not planned`)

"Done" as a Project Status is the board-visible state before formal closure. The true terminal state is `CLOSED` with the appropriate close reason. Scripts should check both: `state == "CLOSED"` AND project status == `"Done"`.

### Why Not Labels?

Labels lack workflow semantics:
- No enforced single-select — multiple `status:*` labels can coexist by mistake
- No ordering or transition logic — anyone can set any label
- No native board view — Projects v2 renders the Status field as a Kanban board automatically
- Label explosion — 20 status labels + artifact + layer + priority + division = unmanageable dropdown

Moving status to the Project field removes ~20 labels and gives you a Kanban board for free.

### Status Mapping by Artifact Type

| Artifact | Typical status flow |
|----------|---------------------|
| Signal | Backlog → Triage → Approved / Done |
| Mission | Backlog → Approved → Planning → In Progress → Done → close |
| Task | Backlog → In Progress → Blocked → Done → close |
| Decision | Backlog → Approved → close |
| Release | Backlog → Approved → In Progress → Done → close |
| Retrospective | Backlog → In Progress → Done → close |

---

## Label Bootstrap Sample

If you manage labels as code, this YAML structure is a practical starting point. Note that status labels are no longer needed — status is tracked via the GitHub Project Status field.

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
  - name: "layer:steering"
    color: "C5DEF5"
    description: "Steering layer"
  - name: "layer:strategy"
    color: "BFD4F2"
    description: "Strategy layer"
  - name: "layer:orchestration"
    color: "D4C5F9"
    description: "Orchestration layer"
  - name: "layer:execution"
    color: "C2E0C6"
    description: "Execution layer"
  - name: "layer:quality"
    color: "F9D0C4"
    description: "Quality layer"
  - name: "priority:critical"
    color: "B60205"
    description: "Blocking — immediate action required"
  - name: "priority:high"
    color: "D93F0B"
    description: "Important — next cycle"
  - name: "priority:medium"
    color: "FBCA04"
    description: "Normal priority"
  - name: "priority:low"
    color: "0E8A16"
    description: "Nice to have"
```

If you prefer GitHub CLI, create labels with `gh label create` using the same names.

---

## Human Approval Table

Humans should not have to guess what "approve" means — and they should never need to manage labels or project status fields.

**How it works:** When an agent needs a human decision, it assigns the issue to the human and leaves a comment that explains what to review and what the options are. The human comments with their decision in plain language and re-assigns to the agent. The agent then updates the Project Status field accordingly.

| Artifact | What the agent's comment tells the human | Human does this |
|----------|------------------------------------------|-----------------|
| Signal | “Please triage this signal. You can: **Proceed** (create a mission), **Defer** (not now), **Monitor** (watch for more data), or **Done** (no action needed). Comment your decision and assign back to me.” | Comment (e.g., “Proceed — this is high priority”) and re-assign to agent |
| Mission | “Please review the scope and outcome contract. You can: **Approve** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment (e.g., “Approved” or “Rejected — scope too broad”) and re-assign to agent |
| Decision | “Please review context and tradeoffs. You can: **Accept** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |
| Release | “Please review rollout and rollback plan. You can: **Approve** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |
| Retrospective | “Please review findings and follow-ups. You can: **Accept** or **Reject** (with reason). Comment your decision and assign back to me.” | Comment decision and re-assign to agent |

Do not use issue closure as the approval signal.
Closure archives completed work. The project status transition (performed by the agent after reading the human's comment) is the approval event.

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

**Core principle:** Humans comment and re-assign. Agents handle all label and project status management. Humans never need to know the label system or the project field.

When work transitions between agent and human:

1. **Agent finishes, needs approval:** Agent sets the project status (e.g., `Triage` or `Backlog`), re-assigns to the approving human, and leaves a comment that (a) summarizes what was done, (b) explains what to review, and (c) lists the human's options in plain language (e.g., "You can: **Approve** — comment 'approved' and assign back to @acme-ai-bot | **Reject** — comment what needs to change and assign back to @acme-ai-bot").
2. **Human decides:** Human comments with their decision in plain language (e.g., "Approved", "Looks good, go ahead", "Rejected — need more detail on rollback") and re-assigns to the agent.
3. **Agent processes decision:** Agent reads the comment, interprets the decision, updates the project status field accordingly (e.g., `Backlog` → `Approved`), and continues. If the comment is ambiguous, the agent asks a clarifying question and keeps the issue assigned to the human.

### Handoff Mechanics — Pull Requests

1. **Agent opens PR:** Agent creates the PR, assigns itself, requests review from the appropriate human(s), and writes a description that summarizes the change, links to the originating issue/task, explains what to focus on, and lists the reviewer's options (approve, request changes, comment).
2. **Reviewer acts:** Reviewer submits a GitHub review. No re-assignment needed — GitHub's review system handles notification.
3. **Agent processes review:** If approved and the agent has merge permission, it merges. If changes are requested, the agent addresses them, pushes, and re-requests review with a comment summarizing what changed. If the review is unclear, the agent asks for clarification on the PR.
4. **Merge handoff:** If branch protection requires a human to merge, the agent comments that the PR is ready and assigns it to the human who should merge.

### Agent Identity

Agents must use a dedicated GitHub bot/user account (e.g., `acme-ai-bot`) so that human-owned and agent-owned items are visually distinguishable at a glance — across issues, PRs, and reviews.

---

## Human Operating Rules

These rules keep GitHub collaboration consistent. **You never need to manage labels or project status fields — agents do that.**

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

- `docs/github/issue-templates/config.sample.yml`
- `docs/github/issue-templates/forms/signal.sample.yml`
- `docs/github/issue-templates/forms/mission.sample.yml`
- `docs/github/issue-templates/forms/task.sample.yml`
- `docs/github/issue-templates/forms/decision.sample.yml`
- `docs/github/issue-templates/forms/release.sample.yml`
- `docs/github/issue-templates/forms/retrospective.sample.yml`

These samples pre-apply the base artifact labels and ask for the fields humans typically forget.

---

## GitHub Projects Recommendation

When `use_projects: true` (recommended), create a GitHub Project v2 with a **Status** single-select field containing the options listed in the Status Tracking section above. Create these minimum views:

| Project View | Filter |
|--------------|--------|
| Signal Triage | `label:artifact:signal is:open` |
| Active Missions | `label:artifact:mission is:open` |
| Mission Tasks | `label:artifact:task is:open` |
| Release Pipeline | `label:artifact:release is:open` |

The Status field produces a native Kanban board automatically — no label-based grouping needed.

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
| 2.1 | 2026-03-09 | Updated sample file paths after consolidating GitHub instance assets under `docs/github/`. |
| 2.0 | 2026-03-08 | Migrated status tracking from labels to GitHub Project Status field. Removed ~20 status labels. Added project setup guidance, project_owner/project_number config fields, unified status model (Backlog → Done + close), terminal state documentation. |
| 1.1 | 2026-03-08 | Added assignment rules for issues and PRs, handoff mechanics for both, agent identity requirement, human operating rules for issues and PRs, comment-based approval model |
| 1.0 | 2026-03-07 | Initial version — concrete GitHub issue-backend implementation guide |