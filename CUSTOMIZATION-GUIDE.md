# Customization Guide — Agentic Enterprise Operating Model

> **Start here** after cloning this framework.  
> This guide walks you through every step of making this operating model your own.

> **New to the repo layout?** Read [docs/FILE-GUIDE.md](docs/FILE-GUIDE.md) first — it explains which root files are part of the open-source template infrastructure (safe to delete in a private fork) and which are your company's actual operating model content (fill in and own).

---

## Quick Start (30 minutes to a working framework)

### Step 1: Fill in CONFIG.yaml (10 min)

Open [CONFIG.yaml](CONFIG.yaml) and fill in every field. This gives the framework your company's identity, product names, toolchain, and organizational shape. The most critical fields:

| Field | Why It Matters |
|-------|---------------|
| `company.name` | Appears throughout every document |
| `vision.north_star` | Anchors all strategic alignment checks |
| `vision.mission` | Guides every agent's decision-making |
| `products.*` | Referenced in architecture policies, agent instructions, and templates |
| `toolchain.*` | Determines which concrete tools implement your quality policies |

### Step 2: Search & Replace Placeholders (5 min)

After filling CONFIG.yaml, do a global search-and-replace across the repository:

```bash
# Replace company name throughout
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_NAME}}/YourCompanyName/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_SHORT}}/YourShort/g'

# Replace product names
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{PRODUCT_NAME}}/YourProduct/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{AI_INTELLIGENCE_NAME}}/YourAI/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{ASSISTANT_NAME}}/YourAssist/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{AGENT_BRAND}}/YourAgents/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{DATA_STORE_NAME}}/YourDataStore/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{QUERY_LANGUAGE}}/YourQL/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{DESIGN_SYSTEM_NAME}}/YourDesignSystem/g'
```

### Step 3: Review Core Documents (10 min)

Read and adjust these three files — they set the tone for everything:

1. [COMPANY.md](COMPANY.md) — Vision, mission, strategic beliefs. Make them yours.
2. [AGENTS.md](AGENTS.md) — Global agent rules. Adjust identity and product naming.
3. [OPERATING-MODEL.md](OPERATING-MODEL.md) — The meta-description. Verify it matches your reality.

### Small Team or Solo Founder?

If you're a small team or solo founder, start with a **minimal agent fleet** — one agent per active layer. See [Minimal Agent Fleet](#minimal-agent-fleet) below for the exact setup.

### Step 4: Register Your Integrations (5 min)

Review `CONFIG.yaml → integrations` and register the external tools your organization uses:

1. **Observability** — Your monitoring platform (Dynatrace, Grafana, Datadog, etc.) — essential for scaling agent governance
2. **Enterprise toolchain** — CI/CD, ITSM, security scanning, service catalogs
3. **Business systems** — CRM, support platforms, analytics
4. **Communication** — Chat, messaging, notification channels

See `org/integrations/` for detailed guides per category. Start with observability and CI/CD — they provide the most immediate value.

### Step 5: Start Using It (5 min)

Create your first signal in `work/signals/` and you're live.

---

## Minimal Agent Fleet

For small teams and solo founders where humans act as Steering and Strategy, start with **3 active agents** — one per operational layer. Expand as signal volume and mission throughput grow.

### How the 5 Layers Map to a Small Team

| Layer | Small team | Scales to |
|---|---|---|
| **Steering** — evolve the company | You (human) | Steering agents + AI assistance |
| **Strategy** — decide WHY + WHAT | You (human) | Strategy agents |
| **Orchestration** — HOW to execute | Orchestration Agent | Fleet of orchestrators |
| **Execution** — DO the work | Execution Agent(s) | Dozens of specialized agents |
| **Quality** — EVALUATE outputs | Quality Agent | Domain-specific evaluators |

> **Solo founder rule:** You are Steering and Strategy. You merge PRs. That is your only required action.

### Minimal 3-Agent Fleet

| Agent | Layer | What it does | When it runs |
|---|---|---|---|
| **Orchestration Agent** | Layer 2 | Reads signals, creates mission briefs, assigns work to execution, verifies DoD | On every signal or mission state change |
| **Execution Agent** | Layer 3 | Implements missions — code, research, content, tests, PRs | When a mission is assigned |
| **Quality Agent** | Layer 4 | Evaluates outputs against policies, triages new signals, flags stalled missions | Continuously (after builds, before merges) |

Add specialized Execution Agents first as you scale (e.g., one coding-focused, one research-focused), then a dedicated Orchestration or Steering Agent when signal volume justifies it.

### The Self-Sustaining Loop

Every completed mission **must** produce at least one new signal. This is the anti-stall mechanism:

```
Signal → Mission → Work → Done → Signal (≥1)
  ↑                                   │
  └───────────────────────────────────┘
```

A mission is **done** when all of the following are true:

- [ ] `OUTCOME-CONTRACT.md` acceptance criteria are met
- [ ] PR is merged to `main`
- [ ] `STATUS.md` updated to `done` with completion date
- [ ] **At least one new signal filed** in `work/signals/`

The last item is the key: even "nothing to improve" is worth filing. It keeps the loop turning.

### What You Don't Need

- ❌ External project management tool — missions **are** your tickets
- ❌ Observability platform for agent health — git history **is** your audit log
- ❌ Standup meetings — `STATUS.md` **is** the standup
- ❌ Separate OKR framework — `CONFIG.yaml` vision + active missions = your strategy

---

## Initialization Sequence: Day 0 → Day 1

> The Quick Start gives you the files. This section shows you how to **bootstrap the living system** — from a populated template to a company where signals flow, missions execute, and feedback loops close.

### Day 0 — Foundation (1-2 hours)

Complete the Quick Start above (Steps 1-4), then:

1. **Seed COMPANY.md** — Write your real vision, mission, and 4-8 strategic beliefs. These anchor every agent's decision-making. Don't ship placeholder text.
2. **Create your first venture charter** — Copy `org/1-strategy/ventures/_TEMPLATE-venture-charter.md` → `org/1-strategy/ventures/<your-first-product>.md`. Define success metrics and measurement schedule. Even rough targets are better than none.
3. **Define CODEOWNERS** — Review and customize the [CODEOWNERS](CODEOWNERS) file with actual GitHub teams or users that map to each layer's approval authority.

### Day 0.5 — Organizational Skeleton (1-2 hours)

4. **Create your divisions** — For each team you have, copy `org/3-execution/divisions/_TEMPLATE/` → `org/3-execution/divisions/<your-division>/`. Write the `DIVISION.md` charter with scope boundaries and "never do" rules.
5. **Seed the agent type registry** — For each agent role you plan to deploy:
   - Copy `org/agents/_TEMPLATE-agent-type.md` → `org/agents/<layer>/<agent-type-id>.md`
   - Fill in capabilities, layer, division assignment, scaling limits, and quality gates
   - Set `status: active` for agents you're deploying immediately; `proposed` for planned ones
   - At minimum, seed one agent type per layer (Steering, Strategy, Orchestration, Execution, Quality)
6. **Define initial quality policies** — Review all files in `org/4-quality/policies/`. For each, either:
   - Customize thresholds to match your current capabilities (be honest — aspirational but achievable)
   - Or mark sections as `# TODO: Define threshold` so agents know to escalate

### Day 1 — First Signal Flow (30 minutes)

7. **File your first signal** — Create `work/signals/YYYY-MM-DD-<your-first-opportunity>.md` from the template (`work/signals/_TEMPLATE-signal.md`). This is the input that kicks off the entire lifecycle.
8. **Triage to a mission** — The Steering Layer produces a signal digest, the Strategy Layer triages, and if the signal warrants action:
   - Create `work/missions/<mission-name>/MISSION-BRIEF.md` from `work/missions/_TEMPLATE-mission-brief.md`
   - Create `work/missions/<mission-name>/OUTCOME-CONTRACT.md` from `work/missions/_TEMPLATE-outcome-contract.md`
9. **Assemble a fleet** — The Orchestration Layer creates a fleet config (`org/2-orchestration/fleet-configs/<mission>.md`) referencing active agent types from the registry.
10. **Execute** — Execution agents produce work within mission scope, Quality agents evaluate, Ship agents release, Operate agents monitor. The full loop is live.

### Day 2+ — Progressive Automation

11. **Weekly cadence** — Establish the signal digest rhythm:
    - Operate agents surface production signals → `work/signals/`
    - Steering agents produce weekly digests → `work/signals/digests/YYYY-WXX-digest.md`
    - Strategy agents update venture health → file in venture charter or as standalone report
12. **First outcome report** — When a mission's measurement window closes, the Ship Loop produces an outcome report (`work/missions/<name>/OUTCOME-REPORT.md`). This closes the Build→Measure→Learn loop.
13. **First retrospective** — After any incident, produce a postmortem → `work/retrospectives/`. Signals from postmortems feed back into Loop 1.
14. **Evolve** — When signal digests reveal patterns (capability gaps, structural friction, new opportunities), the Steering Layer creates evolution proposals (`org/0-steering/_TEMPLATE-evolution-proposal.md`) — including proposals for new agent types.

> **Tip:** Don't try to automate everything on Day 1. Start with one signal → one mission → one execution cycle. Expand the number of active agents, divisions, and ventures progressively as the team builds confidence in the process.

---

## Deep Customization Guide

After the quick start, customize layer by layer. Each section below tells you **what** to customize, **where** the files are, and **why** it matters.

---

### Level 1: Company Identity & Strategy

**Files to customize:**

| File | What to Do | Priority |
|------|-----------|----------|
| [COMPANY.md](COMPANY.md) | Rewrite vision, mission, strategic beliefs to match your company | **Critical** |
| [CONFIG.yaml](CONFIG.yaml) | Fill all fields — this drives placeholder replacement | **Critical** |

**Guidance:**

- **North Star:** Should be aspirational but grounded. Not "be the best" — more like "be the [specific role] for [specific audience]."
- **Strategic Beliefs:** Write 4-8 enduring convictions. They should be controversial enough to be meaningful (i.e., not everyone would agree) but stable enough to last 3-5 years. The framework ships with 6 generic beliefs about agentic enterprises. Replace them with beliefs specific to your industry and competitive position.
- **Strategic Posture table:** The "From → To" table should capture your actual transformation. What are you today? What are you becoming?

---

### Level 2: Organizational Structure

**Files to customize:**

| File | What to Do | Priority |
|------|-----------|----------|
| [org/README.md](org/README.md) | Adjust layer headcounts, role names, division list | **High** |
| [org/0-steering/AGENT.md](org/0-steering/AGENT.md) | Customize CxO function names to match your exec team | Medium |
| [org/1-strategy/AGENT.md](org/1-strategy/AGENT.md) | Adjust strategy role names | Medium |
| [org/2-orchestration/AGENT.md](org/2-orchestration/AGENT.md) | Adjust orchestration role names | Medium |
| [org/3-execution/AGENT.md](org/3-execution/AGENT.md) | Most customization here — see below | **High** |
| [org/4-quality/AGENT.md](org/4-quality/AGENT.md) | Adjust quality domain names | Medium |

**Key decisions:**

1. **Do your 5 layers make sense?** The Steering → Strategy → Orchestration → Execution → Quality model is general-purpose. Most enterprises can use it as-is. If you have a very flat org, you might merge Steering + Strategy. If you're very large, you might split Execution into sub-layers.

2. **What are your ventures?** Ventures are market-facing offerings. Create one charter per venture in `org/1-strategy/ventures/`. The framework ships with placeholder examples — replace them with yours (e.g., "Cloud Migration", "DevOps Suite", "Security Suite", "Customer Analytics").

3. **What are your divisions?** Divisions are execution teams — each groups agents by expert knowledge, specialized tools, and domain-specific goals. Create one folder per division in `org/3-execution/divisions/`. The framework ships with generic categories:
   - **Core divisions:** Data Foundation, Core Services, Core Applications, AI & Intelligence
   - **Domain divisions:** Placeholders — fill with your product-specific domains
   - **Ops divisions:** Engineering Foundation, Infrastructure Operations, Quality & Security
   - **GTM divisions:** Product Marketing, Knowledge & Enablement
   - **Customer divisions:** Customer Experience

   **To add a division:** Create `org/3-execution/divisions/<name>/DIVISION.md` using the template pattern.

   **To remove a division:** Delete the folder and remove references from `org/README.md`.

---

### Level 3: Ventures (Strategy Layer)

**Location:** `org/1-strategy/ventures/`

The framework ships with placeholder venture charters. For each of your actual ventures:

1. Create a file: `org/1-strategy/ventures/<venture-slug>.md`
2. Define: market positioning, target personas, strategic goals, key divisions, success metrics
3. Map which divisions contribute to this venture

**Template structure for a venture charter:**

```markdown
# Venture: [Name]

## Market Positioning
[What problem does this solve? For whom?]

## Target Personas
[Who buys, who uses, who benefits]

## Strategic Goals
[3-5 measurable goals for this venture]

## Divisions Involved
[Which execution divisions deliver this venture]

## Success Metrics
[How you measure venture health]
```

---

### Level 4: Divisions (Execution Layer)

**Location:** `org/3-execution/divisions/`

Each division folder should contain a `DIVISION.md` that defines:

- **Scope:** What this division owns
- **Boundaries:** What it does NOT own (prevents scope creep)
- **Key Technologies:** Tools, languages, frameworks this team works with
- **Interfaces:** How this division connects to others
- **Agent Context:** What agents need to know to work in this division

---

### Level 5: Quality Policies

**Location:** `org/4-quality/policies/`

The framework ships with 8 generic quality policies. Customize each:

| Policy | What to Customize |
|--------|------------------|
| [security.md](org/4-quality/policies/security.md) | Your specific security requirements, compliance frameworks (SOC2, HIPAA, etc.) |
| [architecture.md](org/4-quality/policies/architecture.md) | Your API conventions, service patterns, catalog requirements |
| [experience.md](org/4-quality/policies/experience.md) | Your design system name, accessibility standards, UI patterns |
| [performance.md](org/4-quality/policies/performance.md) | Your specific latency budgets, cost constraints, resource limits |
| [delivery.md](org/4-quality/policies/delivery.md) | Your deployment model, environments, rollback procedures |
| [content.md](org/4-quality/policies/content.md) | Your brand guidelines, documentation standards, content taxonomy |
| [customer.md](org/4-quality/policies/customer.md) | Your SLA definitions, customer interaction standards |
| [observability.md](org/4-quality/policies/observability.md) | Your telemetry standards, agent observability requirements, alerting thresholds |

**Key principle:** Start with the policies as shipped (they're reasonable defaults for a software enterprise). Then tighten or loosen based on your regulatory environment, risk tolerance, and maturity level.

---

### Level 6: Integrations (3rd-Party Tools)

**Location:** `org/integrations/` and `CONFIG.yaml → integrations`

The framework ships with integration category guides and a template. Connect your enterprise tools:

| Category | Guide | What to Register |
|----------|-------|-----------------|
| **Observability** | `org/integrations/categories/observability.md` | Your monitoring platform, telemetry pipeline, dashboarding — essential for scaling agent governance |
| **Enterprise Toolchain** | `org/integrations/categories/enterprise-toolchain.md` | CI/CD, ITSM, security scanners, service catalogs |
| **Business Systems** | `org/integrations/categories/business-systems.md` | CRM, ERP, support, analytics, marketing automation |
| **Communication** | `org/integrations/categories/communication.md` | Chat, messaging, notifications, escalation |

**Getting started:**

1. Register your observability platform in `CONFIG.yaml → integrations.observability` — this is the highest-value integration for governance at scale
2. Register CI/CD tools — these enforce quality gates
3. Add business systems and communication channels as needed
4. For complex integrations, create a spec from `org/integrations/_TEMPLATE-integration.md`

**Key principle:** Start with observability and CI/CD. Add other integrations incrementally as your agent fleet grows. Every integration must be registered — no shadow connections.

---

### Level 7: Process Customization

**Location:** `process/`

The 4-loop lifecycle (Discover → Build → Ship → Operate) is designed to be universal. Customize:

- **Loop durations:** The defaults (hours-days, days-weeks, days) may need adjustment for your velocity
- **Human checkpoints:** Add or remove approval gates based on your governance needs
- **Templates:** Adjust the co-located `_TEMPLATE-*` files in `work/` and `org/` to match your artifact conventions

---

### Level 8: Worked Examples

**Location:** `examples/`

The framework ships with a generic lifecycle example. Create your own:

1. Pick a real signal from your business
2. Walk it through the full lifecycle (signal → mission → build → ship)
3. Document it as a worked example that shows new team members how the system operates

---

## What to Customize vs. What to Keep

| Component | Keep As-Is? | Why |
|-----------|------------|-----|
| 5-layer model | ✅ Yes | Universal organizational pattern |
| 4-loop lifecycle | ✅ Yes | Universal process pattern |
| Git-native governance | ✅ Yes | Fundamental to the model |
| Agent instruction hierarchy | ✅ Yes | Critical for multi-agent governance |
| Improvement signal flow | ✅ Yes | Key innovation of the model |
| Integration Registry structure | ✅ Yes | Governed connection patterns |
| Company name/vision/mission | ❌ Customize | Your identity |
| Ventures | ❌ Customize | Your market offerings |
| Divisions | ❌ Customize | Your organizational units |
| Quality thresholds | ❌ Customize | Your risk tolerance |
| Toolchain references | ❌ Customize | Your infrastructure |
| Integrations | ❌ Customize | Your enterprise tool ecosystem |
| Observability platform | ❌ Customize | Your monitoring and telemetry stack |
| Product naming | ❌ Customize | Your brand |
| Role titles | 🟡 Optional | The generic titles work for most orgs |
| Templates | 🟡 Optional | The defaults are reasonable starting points |
| Policies | 🟡 Optional | Start with defaults, evolve over time |

---

## Placeholder Reference

All placeholders in the framework use the `{{VARIABLE}}` syntax. Here's the complete list:

| Placeholder | Where Defined | Used In |
|------------|--------------|---------|
| `{{COMPANY_NAME}}` | CONFIG.yaml → company.name | Everywhere |
| `{{COMPANY_SHORT}}` | CONFIG.yaml → company.short_name | Prose references |
| `{{PRODUCT_NAME}}` | CONFIG.yaml → products.core_product_name | Architecture, policies |
| `{{AI_INTELLIGENCE_NAME}}` | CONFIG.yaml → products.ai_intelligence_name | Agent instructions, policies |
| `{{ASSISTANT_NAME}}` | CONFIG.yaml → products.assistant_name | UX references, examples |
| `{{AGENT_BRAND}}` | CONFIG.yaml → products.agent_brand | Agent instructions |
| `{{DATA_STORE_NAME}}` | CONFIG.yaml → products.data_store_name | Architecture policy, data refs |
| `{{QUERY_LANGUAGE}}` | CONFIG.yaml → products.query_language | Architecture policy, data access |
| `{{DESIGN_SYSTEM_NAME}}` | CONFIG.yaml → products.design_system_name | Experience policy |
| `{{VENTURE_N_NAME}}` | CONFIG.yaml → ventures[n].name | Venture charters |
| `{{VENTURE_N_DESCRIPTION}}` | CONFIG.yaml → ventures[n].description | Venture charters |
| `{{DOMAIN_CAP_N_NAME}}` | CONFIG.yaml → divisions.engineering_domain[n].name | Division definitions |
| `{{DOMAIN_CAP_N_DESCRIPTION}}` | CONFIG.yaml → divisions.engineering_domain[n].description | Division definitions |
| `{{GIT_HOST}}` | CONFIG.yaml → toolchain.git_host | Process docs |
| `{{CI_CD}}` | CONFIG.yaml → toolchain.ci_cd | Delivery policy |
| `{{OBSERVABILITY_TOOL}}` | CONFIG.yaml → toolchain.observability | Monitoring references |
| `{{SERVICE_CATALOG}}` | CONFIG.yaml → toolchain.service_catalog | Catalog references |
| `{{OBSERVABILITY_PLATFORM_NAME}}` | CONFIG.yaml → integrations.observability[0].name | Integration guides |
| `{{OTLP_ENDPOINT}}` | CONFIG.yaml → integrations.observability[0].otlp_endpoint | Telemetry pipeline |

---

## Production Deployment Notes

This framework is a **structural template** — a starting point, not a turnkey deployment. For production use:

1. **Split into multiple repos:** Operating model, per-product code, GTM content, customer playbooks — connected via cross-repo references
2. **Wire governance:** CODEOWNERS, branch protection, CI/CD checks — not just described, but enforced
3. **Implement agent runtime:** The repo defines *what* agents do; you'll need LLM orchestration, tool bindings, and MCP integrations
4. **Wire integrations:** Connect registered integrations from `org/integrations/` — implement MCP servers, webhooks, API clients, and OpenTelemetry instrumentation for your specific tools
5. **Deploy observability:** Instrument agent runtimes with OpenTelemetry, connect to your observability platform, build fleet performance dashboards and governance visibility
6. **Calibrate policies:** Quality policies need real-world tuning — false positive rates, threshold adjustment, domain expert review
7. **Build UIs:** Dashboards, signal triage boards, mission control — visual layers over the Git data
8. **Connect business systems:** Agents need MCP servers, APIs, and tool integrations to interact with real business systems (ITSM, CRM, CI/CD toolchains)

---

## Getting Help

- **Structure questions:** Read [OPERATING-MODEL.md](OPERATING-MODEL.md)
- **Agent behavior questions:** Read [AGENTS.md](AGENTS.md) and the relevant layer's AGENT.md
- **Process questions:** Read [process/README.md](process/README.md)
- **Quality questions:** Read the relevant policy in `org/4-quality/policies/`
- **Examples:** See `examples/` for worked-through lifecycle examples

---

## Step 6 — Bootstrap Your Agents

With configuration complete, point your agents at the repo. Each agent needs three things, in order:

1. **Read `AGENTS.md`** — global rules. The top of the instruction hierarchy. Non-negotiable.
2. **Read their layer's `org/<layer>/AGENT.md`** — layer-specific instructions and boundaries.
3. **Read their assigned mission** in `work/missions/` — the specific task context.

That is the complete bootstrap. No additional configuration files required. AGENTS.md auto-loads in Claude Code (via `CLAUDE.md`) and GitHub Copilot (via `.github/copilot-instructions.md`) — for other runtimes, point them at `AGENTS.md` explicitly.

> **Tip:** Don't bootstrap agents against an unconfigured fork. Complete Steps 1–2 first — agents working against template placeholders will produce placeholder-filled outputs that fail CI.

For runtime-specific setup (fleet sizing, scheduling, model tier strategy), see **[docs/runtimes/](docs/runtimes/)**.
