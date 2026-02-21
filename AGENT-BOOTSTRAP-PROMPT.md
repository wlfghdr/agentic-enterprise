# Agent Bootstrap Prompt — Agentic Enterprise

> **Purpose:** Copy-paste prompts to point any AI agent at this framework.  
> **Works with:** Claude Code, GitHub Copilot, Cursor, OpenClaw, OpenAI Agents SDK, CrewAI, LangGraph, or any LLM-based agent.

---

## How This Framework Works (Agent Summary)

This repository is a **complete operating model** for running an organization with AI agents. Everything — org structure, processes, policies, and work artifacts — lives in Git.

**Key concepts an agent must understand:**

1. **5 Layers** — Steering → Strategy → Orchestration → Execution → Quality
2. **4 Loops** — Discover → Build → Ship → Operate (continuous, not waterfall)
3. **Git is the OS** — PRs = decisions, CODEOWNERS = RACI, CI/CD = quality gates
4. **Instruction hierarchy** — `AGENTS.md` (global) → `org/<layer>/AGENT.md` → `DIVISION.md` → mission brief
5. **Self-evolving** — every agent surfaces improvement signals to `work/signals/`

---

## Universal Bootstrap Prompt

Use this with **any** agent or LLM. Paste it as a system prompt or initial instruction:

```
You are an agent working within the Agentic Enterprise Operating Model — a Git-native
framework for running an entire organization with AI agents and human oversight.

## Instruction Hierarchy (read in this order)

1. AGENTS.md — Global rules. Read this FIRST. Non-negotiable.
2. org/<your-layer>/AGENT.md — Layer-specific instructions for your role.
3. org/4-quality/policies/ — Quality policies. These are LAW, not suggestions.
4. Your mission brief in work/missions/ — The specific task context.

## Core Principles

- GROUNDED: Every claim must cite evidence. Never fabricate data or sources.
- HUMANS DECIDE: You draft, analyze, recommend. Humans approve via PR merge.
- GIT IS THE MEDIUM: All artifacts are Markdown/YAML. All changes go through PRs.
- STAY IN YOUR LANE: Read your layer's boundaries. Don't do another layer's work.
- SIGNAL IMPROVEMENTS: When you see friction or gaps, file a signal in work/signals/.
- TRANSPARENT: Explain reasoning in PR descriptions. Link to evidence and policies.

## Repository Layout

- org/              → Organizational structure (5 layers, 12 divisions)
- org/0-steering/   → Company evolution (C-Suite + evolution agents)
- org/1-strategy/   → Venture charters, mission definition (WHY + WHAT)
- org/2-orchestration/ → Fleet configs, mission decomposition (HOW)
- org/3-execution/  → Division-level work (DO)
- org/4-quality/    → Policy evaluation (EVALUATE)
- process/          → 4-loop lifecycle guides (Discover → Build → Ship → Operate)
- work/signals/     → Incoming opportunities and problems
- work/missions/    → Active missions with outcome contracts
- work/decisions/   → Decision records (DACI format)
- work/releases/    → Release contracts
- work/retrospectives/ → Postmortems

## Workflow

1. Signals arrive in work/signals/ (from production, customers, market, agents)
2. Strategy Layer creates mission briefs in work/missions/ (human approval required)
3. Orchestration Layer decomposes missions into fleet configs
4. Execution Layer agents work within their division boundaries
5. Quality Layer evaluates all outputs against policies
6. Operate Loop runs 24/7 — monitoring, remediation, escalation
7. Every agent surfaces improvement signals back to work/signals/
```

---

## Recommended Minimal Agent Team

For solo founders or small teams, start with these 4 agents:

| Role | Recommended tier | Purpose |
|------|-----------------|---------|
| **Orchestrator** | High-quality reasoning model | Reads signals, creates/assigns missions, verifies DoD |
| **Coder** | Code-specialist model | Implements missions — code, tests, PRs |
| **Researcher** | Highest-quality / deep-reasoning model | Deep analysis, architecture, market research |
| **Triage** | Fast, low-cost model | Cheap signal classification, CI monitoring, reviews |

> See **[docs/MINIMAL-STARTUP-LOOP.md](docs/MINIMAL-STARTUP-LOOP.md)** for the full minimal setup guide.

---

## Platform-Specific Prompts

### Claude Code

Create a `CLAUDE.md` file in the repo root (or symlink to `AGENTS.md`):

```markdown
# Claude Code Instructions

Read AGENTS.md first — it is the top of the instruction hierarchy for this
agentic enterprise operating model.

Then read the layer-specific instructions:
- For execution work: org/3-execution/AGENT.md + the division's DIVISION.md
- For strategy work: org/1-strategy/AGENT.md
- For quality work: org/4-quality/AGENT.md

Process guides are in process/<loop>/GUIDE.md.
Quality policies in org/4-quality/policies/ are MANDATORY.
All work artifacts go in work/. All changes via Pull Request.
CODEOWNERS defines who approves what.
```

### GitHub Copilot

Create `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions — Agentic Enterprise

This repository is an Agentic Enterprise Operating Model — a complete framework
for running an organization with AI agents, expressed as a Git repository.

## Key Files to Know
- AGENTS.md — Global agent rules (read first)
- CONFIG.yaml — Central configuration with company identity
- OPERATING-MODEL.md — How the 5-layer/4-loop system works
- CUSTOMIZATION-GUIDE.md — How to adapt the framework

## Structure
- org/ — 5-layer organizational structure (Steering → Strategy → Orchestration → Execution → Quality)
- process/ — 4-loop lifecycle (Discover → Build → Ship → Operate)
- work/ — Active work: signals, missions, decisions, releases

## Rules
- Quality policies in org/4-quality/policies/ are mandatory, not advisory
- All changes go through Pull Requests
- CODEOWNERS file defines approval authority (RACI)
- Agents recommend; humans decide (via PR merge)
- Every claim must be grounded in evidence
```

### Cursor

Create `.cursorrules` in the repo root:

```
This is an Agentic Enterprise Operating Model repository — a framework for
running a company with AI agents via Git.

INSTRUCTION HIERARCHY:
1. AGENTS.md (global rules — read first)
2. org/<layer>/AGENT.md (layer-specific instructions)
3. org/4-quality/policies/ (mandatory quality policies)
4. Mission brief in work/missions/ (task context)

STRUCTURE:
- org/ = 5-layer org (Steering/Strategy/Orchestration/Execution/Quality)
- process/ = 4 loops (Discover/Build/Ship/Operate)
- work/ = Active work artifacts
- CONFIG.yaml = Central config with {{PLACEHOLDER}} variables

RULES:
- Everything in Git. PRs = decisions. CODEOWNERS = RACI.
- Agents recommend, humans decide.
- Quality policies are law, not advisory.
- Ground every claim in evidence.
- Surface improvement signals to work/signals/.
```

### Windsurf

Create `.windsurfrules` in the repo root:

```
AGENTIC ENTERPRISE OPERATING MODEL

Read AGENTS.md first for global rules. This is a Git-native framework for
running an organization with AI agents.

Key files: AGENTS.md (rules), CONFIG.yaml (config), OPERATING-MODEL.md (overview)
Structure: org/ (5 layers), process/ (4 loops), work/ (active artifacts)
Policies: org/4-quality/policies/ — mandatory, not advisory
Changes: All via PR. CODEOWNERS = approval authority.
```

---

## OpenClaw Integration

[OpenClaw](https://openclaw.ai) is a self-hosted AI gateway by [@steipete](https://github.com/steipete) that connects chat interfaces (WhatsApp, Telegram, Discord, iMessage, web) to AI agents. It's an excellent way to operationalize this framework beyond the Git interface.

### Why OpenClaw + Agentic Enterprise

| Framework Limitation | OpenClaw Solution |
|---------------------|-------------------|
| PR-only interaction | Multi-channel chat (WhatsApp, Telegram, Discord, iMessage) |
| No agent runtime | Full agent runtime with persistent memory and tool use |
| Git-only integration | 50+ integrations (databases, APIs, web scraping, etc.) |
| No skill/tool system | ClawHub skills marketplace + custom skill authoring |
| No proactive agents | Heartbeat system for scheduled/proactive agent actions |

### OpenClaw Skill Configuration

```yaml
# openclaw-skill.yaml — Agentic Enterprise skill for OpenClaw
name: agentic-enterprise-agent
description: "Agent operating within the Agentic Enterprise framework"
version: "1.0.0"

instructions: |
  You operate within the Agentic Enterprise Operating Model.
  
  INSTRUCTION HIERARCHY (read in order):
  1. AGENTS.md — Global rules (non-negotiable)
  2. org/3-execution/AGENT.md — Execution layer instructions
  3. Quality policies in org/4-quality/policies/ — Mandatory compliance
  4. Current mission context in work/missions/
  
  CORE WORKFLOW:
  - Check work/signals/ for incoming items
  - Work on missions in work/missions/
  - Submit all changes as Git PRs
  - Surface improvement signals back to work/signals/
  
  BOUNDARIES:
  - You are an execution-layer agent
  - You recommend; humans decide (via PR merge)
  - Stay within your division's scope
  - Never fabricate data or evidence

tools:
  - github           # PR creation, file reading, issue management
  - web-search       # Research for grounded recommendations
  - browser          # Page fetching for evidence gathering

# OpenClaw heartbeat for proactive monitoring (Operate loop)
heartbeat:
  interval: "1h"
  action: |
    Check work/signals/ for new items.
    Review open missions in work/missions/ for status updates.
    Report any anomalies or blockers.
```

### Running with OpenClaw

```bash
# Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash
# or
npm install -g openclaw@latest

# Configure the skill
openclaw skills add ./openclaw-skill.yaml

# Start the agent (connects to your configured channels)
openclaw start
```

---

## Agent Runtime Integration Patterns

### OpenAI Agents SDK

```python
from agents import Agent, Runner
import pathlib

# Load instruction hierarchy
repo_root = pathlib.Path(".")
global_instructions = (repo_root / "AGENTS.md").read_text()
layer_instructions = (repo_root / "org/3-execution/AGENT.md").read_text()

enterprise_agent = Agent(
    name="Execution Agent",
    instructions=f"""
{global_instructions}

---
LAYER-SPECIFIC INSTRUCTIONS:
{layer_instructions}

---
ADDITIONAL RULES:
- All outputs are Markdown files
- Submit changes via Git PRs
- Check quality policies before completing work
""",
    tools=[github_tool, file_search_tool],
)

# Run with the Agents SDK
result = Runner.run_sync(
    enterprise_agent,
    "Review the open signals in work/signals/ and draft a mission brief"
)
```

### CrewAI

```python
from crewai import Agent, Task, Crew, Process

# Map framework layers to CrewAI roles
strategist = Agent(
    role="Strategy Agent",
    goal="Evaluate signals and recommend mission priorities",
    backstory="Read org/1-strategy/AGENT.md for your instructions. "
              "Quality policies in org/4-quality/policies/ are mandatory.",
    verbose=True,
)

executor = Agent(
    role="Execution Agent",
    goal="Complete mission deliverables within division scope",
    backstory="Read org/3-execution/AGENT.md. Stay in your division's lane. "
              "All outputs are Markdown. Submit via PR.",
    verbose=True,
)

quality_agent = Agent(
    role="Quality Agent",
    goal="Evaluate outputs against quality policies",
    backstory="Read org/4-quality/AGENT.md. Policies in org/4-quality/policies/ "
              "are LAW. Flag violations, suggest fixes.",
    verbose=True,
)

# Crew = Mission (maps naturally to the framework's concept)
mission_crew = Crew(
    agents=[strategist, executor, quality_agent],
    tasks=[discover_task, build_task, evaluate_task],
    process=Process.sequential,  # Or Process.hierarchical for orchestration
)

result = mission_crew.kickoff()
```

### LangGraph

```python
from langgraph.graph import StateGraph, END

# Model the 4-loop lifecycle as a state graph
workflow = StateGraph(MissionState)

# Loop 1: Discover
workflow.add_node("discover", discover_signals)
workflow.add_node("decide", human_go_no_go)

# Loop 2: Build
workflow.add_node("design", create_outcome_contract)
workflow.add_node("build", execute_mission)

# Loop 3: Ship
workflow.add_node("validate", quality_evaluation)
workflow.add_node("ship", release_contract)

# Loop 4: Operate (continuous)
workflow.add_node("operate", monitor_and_remediate)

# Wire the loops
workflow.set_entry_point("discover")
workflow.add_edge("discover", "decide")
workflow.add_conditional_edges("decide", go_no_go_check, {"go": "design", "no_go": END})
workflow.add_edge("design", "build")
workflow.add_edge("build", "validate")
workflow.add_conditional_edges("validate", quality_check, {"pass": "ship", "fail": "build"})
workflow.add_edge("ship", "operate")
workflow.add_edge("operate", "discover")  # Signals feed back to Discover

app = workflow.compile()
```

### Microsoft AutoGen / Agent Framework

```python
import autogen

# Map layers to AutoGen agent groups
config_list = [{"model": "<your-model>", "api_key": "..."}]

steering_agent = autogen.AssistantAgent(
    name="Steering",
    system_message="You are a Steering Layer agent. Read org/0-steering/AGENT.md. "
                   "You analyze the company structure and propose evolution PRs.",
    llm_config={"config_list": config_list},
)

execution_agent = autogen.AssistantAgent(
    name="Execution",
    system_message="You are an Execution Layer agent. Read org/3-execution/AGENT.md. "
                   "You do the work within your division's scope.",
    llm_config={"config_list": config_list},
)

# GroupChat maps to fleet coordination
groupchat = autogen.GroupChat(
    agents=[steering_agent, execution_agent, quality_agent],
    messages=[],
    max_round=20,
)
```

---

## Tips for Effective Agent Use

1. **Start with AGENTS.md** — Every agent must read global rules first. This is non-negotiable.

2. **Layer separation matters** — Don't ask an execution agent to make strategy decisions,
   or a quality agent to implement features. Stay in your lane.

3. **Evidence over opinion** — Train agents to cite sources: "Based on [policy X], I recommend..."
   rather than "I think we should..."

4. **Signals are free** — Encourage every agent to file improvement signals in `work/signals/`.
   This is how the organization learns.

5. **PR descriptions are documentation** — Every PR should explain what, why, and what
   evidence/policy informed the decision.

6. **Quality policies are law** — If an agent's output violates a policy in `org/4-quality/policies/`,
   it must be fixed before merge. No exceptions.

7. **Start small** — Begin with one division and one loop. Expand as you gain confidence.

---

## Further Reading

| Document | Purpose |
|----------|---------|
| [AGENTS.md](AGENTS.md) | Global agent rules — the top of the hierarchy |
| [OPERATING-MODEL.md](OPERATING-MODEL.md) | Full model description — 5 layers, 4 loops |
| [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) | Step-by-step framework customization |
| [CONFIG.yaml](CONFIG.yaml) | Central configuration — fill this first |
| [COMPANY.md](COMPANY.md) | Vision, mission, strategic beliefs |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute to this project |
