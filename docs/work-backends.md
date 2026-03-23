# Work Backends — Git Files vs. Issue Tracker

> **Version:** 1.5 | **Last updated:** 2026-03-23

> **What this document is:** A comprehensive guide to how work artifacts can be tracked using different backends — either as Markdown files in Git (the original model) or as issues in an issue tracker (GitHub Issues, Jira, Linear, etc.).

> **Use this document for:** choosing a backend, configuring `CONFIG.yaml`, understanding which artifacts stay in Git, and comparing backend behavior.
> **Do not use this document for:** step-by-step GitHub issue operations. For that, use [github-issues.md](github-issues.md).

---

## Why Two Backends?

The operating model defines **what artifacts exist** and **how they flow** between layers and loops. The original framework tracked everything as Markdown files in `work/`. This is fully self-contained and auditable, but creates friction for human collaboration:

- **Visibility:** Scanning 20+ Markdown files to understand mission status is harder than glancing at a labeled issue board.
- **Interaction:** Commenting, assigning, re-labeling, and triaging are native to issue trackers — and clunky via file edits + PRs.
- **Notifications:** Issue trackers have built-in notification, mention, and subscription systems.
- **Mobile:** Issue trackers work well on mobile. Editing Markdown in a repo does not.
- **Collaboration:** Discussion threads, reactions, and cross-references are first-class in issue trackers.

The framework now supports **both backends**. The choice is made at instance configuration time via `CONFIG.yaml → work_backend`.

---

## The Three File Categories

Not everything moves. The framework distinguishes three categories:

### 1. Governance Backbone — Always in Git

These define the **structure, rules, and shape** of the organization. They change slowly and deliberately. They are **never** tracked in an issue system.

| What | Location | Why Git |
|------|----------|---------|
| Org structure | `org/` | Defines layers, divisions, agent types |
| Quality policies | `org/4-quality/policies/` | Law — changes need PR review |
| Agent instructions | `org/*/AGENT.md` | Agent behavior boundary — needs version control |
| Agent type registry | `org/agents/` | Governed lifecycle (proposed → active → deprecated) |
| Process definitions | `process/` | Loop-by-loop guides |
| Integration registry | `org/integrations/` | Governed connections to external tools |
| Configuration | `CONFIG.yaml` | Source of truth for everything configurable |
| Global rules | `AGENTS.md`, `CLAUDE.md` | Non-negotiable agent rules |
| Templates | `_TEMPLATE-*.md` everywhere | Schema definitions — stay in Git as references |

### 2. Persistent Documentation Artifacts — Always in Git

These are **long-lived deliverables** that benefit from version control, code review, and diff history.

| Artifact | Why Git |
|----------|---------|
| **Technical Designs** | Architecture decisions tightly coupled to code — need PR-based review |
| **Asset Registry Entries** | Persistent documentation references — part of the knowledge base |
| **Governance Exceptions** | Audit-critical — time-bounded policy overrides need full traceability |
| **Runbooks** | Operational procedures co-located with service definitions |
| **Signal Digests** | Weekly synthesis artifacts consumed across layers — diffable history matters more than issue interaction |
| **Quality Evaluation Reports** | Immutable evidence artifacts that should not be edited through issue comments |
| **Outcome Reports** | Measured results against the outcome contract — stored as durable mission evidence |
| **Fleet Performance Reports** | Periodic fleet analysis that benefits from file-based version history |

### 3. Operational Work Artifacts — Configurable Backend

These are the **dynamic, frequently-changing** artifacts that track active work. They can live in Git files OR in an issue tracker.

| Artifact | Git Files | Issue Tracker |
|----------|-----------|--------------|
| **Signals** | `work/signals/YYYY-MM-DD-name.md` | Issue with `artifact:signal` label |
| **Missions** | `work/missions/<name>/BRIEF.md` | Issue with `artifact:mission` label |
| **Outcome Contracts** | `work/missions/<name>/OUTCOME-CONTRACT.md` | Section in mission issue body or linked issue |
| **Mission Status** | `work/missions/<name>/STATUS.md` (append-only) | Comments on mission issue |
| **Tasks** | `work/missions/<name>/TASKS.md` | Sub-issues linked to mission issue |
| **Decision Records** | `work/decisions/YYYY-MM-DD-name.md` | Issue with `artifact:decision` label |
| **Release Contracts** | `work/releases/YYYY-MM-DD-name.md` | Issue with `artifact:release` label |
| **Retrospectives** | `work/retrospectives/YYYY-MM-DD-name.md` | Issue with `artifact:retrospective` label |
| **Locks** | `work/locks/<lock-id>.md` | Not applicable — locks stay in Git (concurrency mechanism) |

---

## Configuring the Work Backend

Set the backend in `CONFIG.yaml`:

```yaml
work_backend:
  type: "github-issues"    # "git-files" | "github-issues"

  github_issues:
    repo: ""                # empty = same repo; or "org/repo" for separate issue repo
    use_projects: true      # use GitHub Projects for board views + status tracking
    project_owner: ""       # GitHub org or user that owns the project
    project_number: 0       # GitHub Project v2 number
    use_label_prefixes: true # use artifact:, layer:, loop: prefixes

  overrides:
    # Force specific artifacts to a backend regardless of the global type.
    # Useful when most work is in issues but some artifacts must stay in Git.
    technical-design: "git-files"
    governance-exception: "git-files"
    asset-registry: "git-files"
    # lock: "git-files"  ← always git, not configurable
```

When `work_backend.type` is `"git-files"` (the default), the framework behaves exactly as before — all work artifacts are Markdown files in `work/`.

---

## Issue Backend: Label Taxonomy

When using an issue tracker, **labels provide categorization metadata** while **status is tracked via the GitHub Project Status field**. Labels replace file paths and YAML frontmatter for artifact type, layer, loop, and priority — but not for workflow status.

### Artifact Type Labels (`artifact:`)

| Label | Maps to Template |
|-------|-----------------|
| `artifact:signal` | `_TEMPLATE-signal.md` |
| `artifact:mission` | `_TEMPLATE-mission-brief.md` |
| `artifact:task` | `_TEMPLATE-tasks.md` (individual task) |
| `artifact:decision` | `_TEMPLATE-decision-record.md` |
| `artifact:release` | `_TEMPLATE-release-contract.md` |
| `artifact:retrospective` | `_TEMPLATE-postmortem.md` |
| `artifact:governance-exception` | `_TEMPLATE-governance-exception.md` |

### Status Tracking (GitHub Project Status Field)

**Status is tracked via the GitHub Project v2 Status field, not via labels.** This provides single-select workflow semantics, native Kanban board views, and transition logic that labels cannot offer.

| Project Status | Used By |
|----------------|---------|
| Backlog | All artifacts (newly filed, not yet prioritized) |
| Triage | Signals (being evaluated) |
| Approved | Missions, Decisions, Releases, Governance Exceptions |
| Planning | Missions (being decomposed into tasks) |
| In Progress | Missions, Tasks, Releases |
| Blocked | Tasks (waiting on dependency) |
| Done | All artifacts (completed — ready to close) |

Terminal states use GitHub's native close mechanism:
- **Completed** → close issue (reason: `completed`)
- **Cancelled** → close issue (reason: `not planned`)

See [github-issues.md](github-issues.md) for the full status model and setup instructions.

**Status label rule:** Do not use `status:*` labels. Use the Project Status field exclusively.

### Layer Labels (`layer:`)

Which organizational layer owns or originated this artifact.

| Label | Layer |
|-------|-------|
| `layer:steering` | Layer 0 — Steering |
| `layer:strategy` | Layer 1 — Strategy |
| `layer:orchestration` | Layer 2 — Orchestration |
| `layer:execution` | Layer 3 — Execution |
| `layer:quality` | Layer 4 — Quality |

### Loop Labels (`loop:`)

Which process loop this artifact belongs to.

| Label | Loop |
|-------|------|
| `loop:discover` | Discover & Decide |
| `loop:build` | Design & Build |
| `loop:ship` | Validate & Ship |
| `loop:operate` | Operate & Evolve |

### Priority Labels (`priority:`)

| Label | Meaning |
|-------|---------|
| `priority:critical` | Blocking — immediate action required |
| `priority:high` | Important — next cycle |
| `priority:medium` | Normal priority |
| `priority:low` | Nice to have |

### Signal-Specific Labels

| Label | Meaning |
|-------|---------|
| `urgency:immediate` | Needs action now |
| `urgency:next-cycle` | Next triage cycle |
| `urgency:monitor` | Watch and wait |
| `category:market` | Market signal |
| `category:customer` | Customer signal |
| `category:technical` | Technical signal |
| `category:internal` | Internal signal |
| `category:competitive` | Competitive signal |
| `category:financial` | Financial signal |
| `confidence:high` | High confidence in signal |
| `confidence:medium` | Medium confidence |
| `confidence:low` | Low confidence |

### Division Labels (`division:`)

Created dynamically based on configured divisions in `CONFIG.yaml`. Examples:

- `division:data-foundation`
- `division:core-services`
- `division:customer-experience`
- `division:engineering-foundation`

### Quality Verdict Labels (`verdict:`)

| Label | Meaning |
|-------|---------|
| `verdict:pass` | Quality evaluation passed |
| `verdict:pass-with-notes` | Passed with observations |
| `verdict:fail` | Failed — blocking issues found |
| `verdict:escalate` | Needs human judgment |

### Severity Labels (for retrospectives)

| Label | Meaning |
|-------|---------|
| `severity:sev1` | Critical outage |
| `severity:sev2` | Major impact |
| `severity:sev3` | Moderate impact |
| `severity:sev4` | Minor impact |

---

## Issue Backend: Structural Conventions

For an operational GitHub implementation, including issue forms, human approval steps, and label bootstrap samples, see [docs/github-issues.md](github-issues.md).

### Missions as Issue Hierarchies

A **mission** in the issue backend is an issue with `artifact:mission` label. Its structure:

```
Mission Issue (#42)
  ├── artifact:mission, layer:strategy, loop:build  (Project Status: In Progress)
  ├── Body: Mission brief content (from template structure)
  ├── Comment: Outcome Contract (or linked issue)
  ├── Comment: Status Update 1 (newest first)
  ├── Comment: Status Update 2
  │
  ├── Sub-Issue: Task 1 (#43) — artifact:task, division:core-services  (Project Status: In Progress)
  ├── Sub-Issue: Task 2 (#44) — artifact:task, division:data-foundation  (Project Status: Backlog)
  └── Sub-Issue: Task 3 (#45) — artifact:task, division:engineering-foundation  (Project Status: Blocked)
```

Git-backed companion artifacts still exist alongside the issue hierarchy where required:

- `work/signals/digests/YYYY-WXX-digest.md`
- `work/missions/<name>/evaluations/*.md`
- `work/missions/<name>/OUTCOME-REPORT.md`
- `work/missions/<name>/FLEET-REPORT.md`
- `work/missions/<name>/TECHNICAL-DESIGN.md` (when required)

### Cross-References

- **Signal → Mission:** Mission issue body references signal issue: "Origin: #31"
- **Mission → Tasks:** Tasks are sub-issues of the mission issue
- **Task → PR:** Task issue links to implementing PR(s)
- **Quality Eval → Mission:** Git evaluation report references the mission issue and task issue
- **Retrospective → Signal:** Retro issue references generated signal issues
- **Decision → Mission:** Decision issue references the mission it supports

### Issue Templates

GitHub Issue Templates (`.github/ISSUE_TEMPLATE/`) can mirror the Markdown templates. In this template repository, the operational forms are stored as docs-only samples under `docs/github/issue-templates/forms/` so the framework repo itself does not behave like an instance repo. The preferred instantiation path is the scripted installer in `scripts/instantiate_instance.py`.

- `signal.sample.yml` — maps to `_TEMPLATE-signal.md`
- `mission.sample.yml` — maps to `_TEMPLATE-mission-brief.md`
- `task.sample.yml` — maps to `_TEMPLATE-tasks.md`
- `decision.sample.yml` — maps to `_TEMPLATE-decision-record.md`
- `release.sample.yml` — maps to `_TEMPLATE-release-contract.md`
- `retrospective.sample.yml` — maps to `_TEMPLATE-postmortem.md`

Instance repos should copy these samples into `.github/ISSUE_TEMPLATE/` when enabling the issue backend. Agents can still create issues with structured body text directly.

### GitHub Projects Integration

When `use_projects: true` (recommended), create a GitHub Project v2 with a **Status** single-select field. The Project provides native Kanban board views grouped by status — no label-based grouping needed.

| Board | View | Filter |
|-------|------|--------|
| **Signal Triage** | Board (Kanban) | `label:artifact:signal` |
| **Active Missions** | Board (Kanban) | `label:artifact:mission` |
| **Mission Tasks** | Board per mission | `label:artifact:task` + mission reference |
| **Release Pipeline** | Board (Kanban) | `label:artifact:release` |
| **Quality Dashboard** | Table | Mission-linked Git reports + evaluation references |

---

## Assignment Discipline (Issues, PRs, and Reviews)

**Every issue, pull request, and review request must have an assignee at all times.** This applies regardless of which work backend is configured — PRs exist in both modes (governance backbone changes always go through PRs). Assignment is not optional metadata — it is the primary mechanism for communicating ownership and expected next action. **Assignee state is the source of truth for who must act next.** If human input, approval, or a decision is required, the item must be assigned to that human rather than left with the agent and explained only in text.

### Assignment Rules — Issues

| Situation | Assignee | Why |
|-----------|----------|-----|
| Agent is executing a task | Agent's GitHub bot account | Agent owns the work and is responsible for completion |
| Work needs human approval | The approving human | Human must act — review, approve, reject, or request changes |
| Work needs human decision | The deciding human | Human must make a judgment call |
| Agent is blocked, needs human input | The human who can unblock | Prevents silent stalls |
| Issue just created, not yet triaged | The triaging human or orchestration agent | Ensures someone picks it up |
| Completed work, pending closure | The person who will close/archive | Clean handoff to final step |

### Assignment Rules — Pull Requests

| Situation | Assignee | Reviewers | Why |
|-----------|----------|-----------|-----|
| Agent opens a PR | Agent bot account (author) | Human(s) from CODEOWNERS or relevant approver | Author owns the PR; reviewer must act |
| PR review requested | Agent bot account (author) | The specific human(s) who should review | Reviewer sees it in their review queue |
| Reviewer requests changes | Agent bot account | Same reviewer (stays assigned) | Agent must address feedback |
| Agent addresses feedback | Agent bot account | Re-request review from same reviewer | Reviewer must re-evaluate |
| PR approved, ready to merge | The person who will merge (human or agent if permitted) | — | Clean handoff to final step |
| PR is blocked or has failing checks | Agent bot account | — | Agent must investigate and fix |

A PR without both an owner path and a reviewer path is operationally incomplete. The minimum acceptable state is:
- a named assignee who owns the next step
- explicit reviewer request(s) when human review is required
- a PR description that tells reviewers what to review and what they can do next

### Handoff Protocol — Issues

**Core principle:** Humans never need to touch labels or project status fields. They comment and re-assign. Agents handle all label and project status management.

1. **Agent → Human (approval needed):** Agent sets the project status (e.g., `Triage`), re-assigns to the approving human, and leaves a comment that:
   - Summarizes what was done and what to review
   - Lists the human's options in plain language (e.g., "You can: **Approve** — comment 'approved' and assign back to @acme-ai-bot | **Reject** — comment what needs to change and assign back to @acme-ai-bot | **Ask questions** — comment your questions and keep yourself assigned")
   - Links to relevant artifacts if applicable
   - Never relies on the comment alone to indicate human ownership; the assignee must also change
2. **Human → Agent (any decision):** Human leaves a comment with their decision in plain language (e.g., "Approved", "Looks good", "Rejected — the rollback plan is incomplete", "Please revise the scope to exclude X") and re-assigns to the agent.
3. **Agent processes human decision:** Agent reads the comment, interprets the decision, updates the project status field accordingly (e.g., `Backlog` → `Approved`), and continues with the next step. If the agent cannot confidently interpret the comment, it asks a clarifying question in a follow-up comment and keeps the issue assigned to the human.

### Handoff Protocol — Pull Requests

1. **Agent opens PR:** Agent creates the PR, assigns itself, requests review from the appropriate human(s), and writes a PR description that:
   - Summarizes the change and its purpose
   - Links to the originating issue/mission/task
   - States what the reviewer should focus on
   - Lists the reviewer's options (e.g., "You can: **Approve** the review | **Request changes** with comments | **Comment** with questions")
2. **Reviewer acts:** Reviewer submits a GitHub review (approve, request changes, or comment). No re-assignment needed — the review system handles notification.
3. **Agent processes review:** If approved and agent has merge permission, it merges. If changes are requested, the agent addresses them, pushes new commits, and re-requests review. If the review comment is unclear, the agent replies on the PR asking for clarification.
4. **Merge handoff:** If the agent cannot merge (branch protection requires a human), it comments on the PR stating it is ready to merge and assigns the PR to the human who should merge.

### Next-Action Clarity

Every assigned issue, PR, and review request must make the expected next action obvious. An assignee or reviewer should be able to look at an item and immediately understand what they need to do and what their options are — without reading the full history or knowing the label system.

Mechanisms for next-action clarity:
- **Agent-authored handoff comment** (issues) — always present when an agent hands off to a human; lists options in plain language
- **PR description** — always explains what to review and what the reviewer's options are
- **Review re-request** — after addressing feedback, agent comments summarizing what changed
- **Issue description** — for new issues, the description itself states the expected action and available options
- **Project status field** — maintained by agents as machine-readable state; humans can ignore it

### Unassigned Item Sweep

Orchestration agents must periodically scan for unassigned open issues and PRs. Unassigned items are workflow failures — they represent work that nobody is driving. For each unassigned item:
1. Determine the correct assignee based on the artifact type, status, and layer
2. Assign the item (and request reviewers for PRs if missing)
3. If the correct assignee cannot be determined, escalate by assigning to the orchestration layer's human supervisor

### Agent Identity

Agents must use a dedicated GitHub bot/user account (e.g., `acme-ai-bot`). This makes it unambiguous whether an item is human-owned or agent-owned, across issues, PRs, and reviews. Configure the agent identity in `CONFIG.yaml → work_backend.github_issues`.

---

## Agent Behavior Differences by Backend

### Creating Artifacts

| Action | Git Files Backend | Issue Backend |
|--------|-------------------|---------------|
| File a signal | Create `work/signals/YYYY-MM-DD-name.md`, commit, open PR | Create issue with `artifact:signal` + metadata labels |
| Create a mission | Create `work/missions/<name>/BRIEF.md`, commit, open PR | Create issue with `artifact:mission` label, body from template |
| Decompose tasks | Edit `TASKS.md`, commit | Create sub-issues with `artifact:task` labels |
| Update status | Append to `STATUS.md`, commit | Add comment to mission issue, update project status field |
| Quality evaluation | Create `evaluations/*.md`, commit | Create `evaluations/*.md`, commit, and reference the mission/task issues |
| Decision record | Create `work/decisions/*.md`, commit, open PR | Create issue with `artifact:decision` label |
| Close mission | Update status in files, archive folder | Set project status to `Done`, then close issue |

### Approval Mechanisms

| Mechanism | Git Files Backend | Issue Backend |
|-----------|-------------------|---------------|
| Signal triage | PR merge = approval | Human comments with triage decision (e.g., "proceed", "defer", "monitor", "done") and re-assigns to agent. Agent updates the project status field accordingly (e.g., `Triage` → `Approved`). |
| Mission approval | PR merge = approval | Human comments approval (e.g., "approved") and re-assigns to agent. Agent changes project status `Backlog` → `Approved`. |
| Decision approval | PR merge = approval | Human comments acceptance and re-assigns to agent. Agent changes project status `Backlog` → `Approved`. |
| Quality gate | Evaluation file with PASS verdict | Evaluation file in Git references the issue-backed mission/task |
| Release go/no-go | PR merge = approval | Human comments approval and re-assigns to agent. Agent changes project status `Backlog` → `Approved`. |

### Human Approval Cheat Sheet

Humans approve by **commenting and re-assigning** — they never need to touch labels or project status fields. The agent's handoff comment always explains the available options.

| Artifact | Human does this | Agent does this after |
|----------|-----------------|---------------------|
| Signal | Review the issue, comment with triage decision (e.g., "proceed" or "defer — not a priority this quarter"), re-assign to agent | Agent updates the project status based on the comment (e.g., `Triage` → `Approved` or `Done`) |
| Mission | Review scope and outcomes, comment approval or rejection, re-assign to agent | Agent changes project status `Backlog` → `Approved` (or keeps and notes rejection) |
| Decision | Review context and tradeoffs, comment acceptance or rejection, re-assign to agent | Agent changes project status `Backlog` → `Approved` (or keeps and notes rejection) |
| Release | Review rollout and rollback plan, comment approval, re-assign to agent | Agent changes project status `Backlog` → `Approved` |
| Retrospective | Review findings and follow-ups, comment acceptance, re-assign to agent | Agent changes project status to `Done` |

Do not rely on issue closure alone as approval. Closure archives work; the project status transition (performed by the agent) is the approval event.

### Audit Trail

| Aspect | Git Files Backend | Issue Backend |
|--------|-------------------|---------------|
| Who changed what | Git blame + commit history | Issue activity log + project status change history |
| When | Commit timestamps | Issue event timestamps |
| Why | Commit messages + PR descriptions | Issue comments + status change context |
| Completeness | Full — Git captures everything | Full — issue trackers log all events |

---

## Migration Between Backends

### Git Files → Issue Backend

1. Set `work_backend.type: "github-issues"` in `CONFIG.yaml`
2. For each active artifact in `work/`, create a corresponding issue with appropriate labels
3. Keep Git-only artifacts in place (`TECHNICAL-DESIGN.md`, evaluation reports, fleet reports, outcome reports, signal digests, asset registry, governance exceptions, locks)
4. Archive (don't delete) only the Git-file operational artifacts that moved to issues — they remain as historical record
5. Going forward, agents create issues instead of files for configurable artifacts

### Issue Backend → Git Files

1. Set `work_backend.type: "git-files"` in `CONFIG.yaml`
2. For each open issue with `artifact:*` labels, create corresponding files in `work/`
3. Close the issues with a note linking to the Git artifact
4. Going forward, agents create files instead of issues

### Hybrid Operation

Using `overrides` in CONFIG.yaml, you can run both backends simultaneously for different artifact types. For example:
- Signals, Missions, Tasks → issues (high human interaction)
- Technical Designs, Governance Exceptions → git files (need code review)
- Decisions → issues (discussion-heavy)
- Asset Registry → git files (persistent documentation)

---

## Templates as Schema Definitions

Regardless of backend, the `_TEMPLATE-*.md` files in `work/` remain in the repository. They serve as:

1. **Schema definitions** — what fields/sections an artifact must contain
2. **Reference documentation** — what each field means and what values are valid
3. **Fallback** — if no issue backend is configured, they're used directly
4. **Issue template source** — GitHub Issue Templates can be generated from them

Templates are **never** tracked in the issue system. They are framework files, governed by the template lifecycle (Rule 11 in AGENTS.md).

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.5 | 2026-03-23 | Clarified that assignee state is the source of truth for next action and that human-needed work must be explicitly reassigned to the human owner. |
| 1.4 | 2026-03-09 | Consolidated backend configuration here and removed the duplicate `WORK-BACKEND.md` doc. Clarified this file's scope vs. `github-issues.md`. |
| 1.2 | 2026-03-08 | Added assignment discipline section covering issues, PRs, and reviews — mandatory assignees, handoff protocols for both issues and PRs, next-action clarity, unassigned item sweep, agent identity. Human approval via comment+re-assign (agents handle labels). |
| 1.1 | 2026-03-07 | Clarified Git-only companion artifacts, added human approval cheat sheet, removed issue-only claims for digests/evaluations/outcome reports/fleet reports, linked GitHub implementation guide |
| 1.0 | 2026-03-07 | Initial version — introduced work backend abstraction concept |
