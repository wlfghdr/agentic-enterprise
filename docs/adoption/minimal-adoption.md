# Minimal Adoption Guide

> The simplest way to start using the Agentic Enterprise framework — no agents required.

## Start Without Agents

The framework is designed so you can adopt it incrementally. You don't need AI agents, an observability platform, or a fully staffed organization to begin. You need:

1. A Git repository
2. A team willing to use structured artifacts instead of ad-hoc communication

That's it.

## The Minimal Setup (30 minutes)

### Step 1: Fork and Configure (10 min)

```bash
git clone https://github.com/wlfghdr/agentic-enterprise.git my-company
cd my-company
```

Edit `CONFIG.yaml` with your company name and basics. You can leave most fields as defaults for now.

### Step 2: Set Up Work Directories (5 min)

You only need three directories to start:

```
work/
├── signals/       ← Where observations go
├── missions/      ← Where scoped work goes
└── releases/      ← Where outcomes are recorded
```

These already exist in the repo. Delete the example files and keep the `_TEMPLATE-*` files.

### Step 3: Set Up CODEOWNERS (5 min)

Define who approves what. A minimal `CODEOWNERS`:

```
# Everything requires at least one review
*                    @your-team-lead

# Signals can be filed by anyone
work/signals/        @your-team

# Missions need lead approval
work/missions/       @your-team-lead

# Policies need exec approval
org/4-quality/       @your-exec
```

### Step 4: Enable Branch Protection (5 min)

On GitHub, enable branch protection for `main`:
- Require pull request reviews before merging
- Require status checks to pass (if you have CI)

### Step 5: Start Working (5 min)

File your first signal. See the [10-Minute Quickstart](../quickstart/10-minute-agentic-enterprise.md) for a walkthrough.

---

## What You Get Immediately

Even without agents, the framework gives you:

| Capability | How |
|-----------|-----|
| **Structured intake** | Signals replace Slack messages and "hey can you look at this" |
| **Scoped work** | Mission briefs replace vague tickets and unbounded tasks |
| **Governance** | PRs + CODEOWNERS = every change is reviewed and traceable |
| **Audit trail** | Git history shows who decided what, when, and why |
| **Quality gates** | CI checks + PR reviews catch problems before they ship |
| **Outcome tracking** | Release records tie work back to the signal that started it |

## Growing Into the Framework

Adopt more as you need it. Here's a natural progression:

### Level 1: Signals + Missions + PRs (Week 1)

- File signals when you observe problems or opportunities
- Convert signals to missions with clear scope and outcomes
- Use PRs for all changes, even non-code (docs, processes, decisions)
- Record releases when work ships

**Humans do everything. Git provides structure and traceability.**

### Level 2: Add Quality Policies (Month 1)

- Pick 2-3 policies from `org/4-quality/policies/` that matter most to your team
- Use them as review checklists during PR reviews
- Add CI checks for the policies you care about most

**Humans still do everything, but with explicit standards.**

### Level 3: Add Your First Agent (Month 2-3)

- Start with a single agent handling a narrow task (e.g., "triage new signals" or "check PRs against policy")
- Give it read access to the repo and the ability to comment on PRs
- Keep humans as approvers for all decisions

**One agent assists. Humans govern.**

### Level 4: Expand Agent Participation (Month 3+)

- Add agents for execution tasks (code changes, documentation, testing)
- Add observability (even basic structured logging)
- Let agents file signals and draft mission briefs for human review

**Multiple agents execute. Humans steer and approve.**

### Level 5: Full Operating Model (Month 6+)

- All 5 layers staffed with agents
- Observability platform integrated with automated signal generation
- Continuous improvement loop running: telemetry → signals → missions → releases
- Humans focus on strategy, policy, and exception handling

**Agents run the operating loop. Humans evolve the organization.**

---

## What You Can Skip

Not everything in the framework is needed from day one. Here's what to defer:

| Component | When You Need It |
|-----------|-----------------|
| Steering Layer (`org/0-steering/`) | When you want agents to propose org changes |
| Fleet Configs (`org/2-orchestration/fleet-configs/`) | When you have multiple agents to coordinate |
| Integration Registry (`org/integrations/`) | When you connect external tools |
| Decision Records (`work/decisions/`) | When decisions need formal documentation |
| OTel telemetry | When you have agents running at scale |
| 15 execution divisions | Start with 1-2 that match your team structure |

## What You Should Not Skip

These are load-bearing from day one:

| Component | Why |
|-----------|-----|
| `CONFIG.yaml` | Central configuration — everything references it |
| `CODEOWNERS` | Without it, governance has no enforcement |
| Signal → Mission → PR flow | This is the core workflow — everything else supports it |
| At least one quality policy | Without standards, reviews are subjective |

## Common Mistakes

1. **Trying to adopt everything at once.** Start with signals, missions, and PRs. Add layers as you need them.

2. **Skipping CODEOWNERS.** Without it, PRs have no mandatory reviewers and governance is voluntary.

3. **Not linking artifacts.** Every mission should reference its signal. Every PR should reference its mission. Every release should reference its PR. The chain of traceability is the audit trail.

4. **Treating signals as tickets.** Signals are observations, not assignments. They become missions (scoped work) only after triage and approval.

5. **Over-engineering agent instructions before having agents.** Get the human workflow right first. Agent instructions are natural language — they can read the same artifacts humans use.

## Next Steps

- [10-Minute Quickstart](../quickstart/10-minute-agentic-enterprise.md) — Walk through the workflow
- [End-to-End Example](../../examples/e2e-loop/) — See a complete lifecycle
- [Architecture Overview](../architecture/agentic-enterprise-architecture.md) — Understand the full system
- [customization-guide.md](../customization-guide.md) — Full onboarding walkthrough
