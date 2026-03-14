# Customization Guide — Agentic Enterprise Operating Model

> **Version:** 3.4 | **Last updated:** 2026-03-14

> **Start here** after cloning this framework.
> This guide walks you through every step of making this operating model your own.

> **New to the repo layout?** Read [docs/FILE-GUIDE.md](docs/FILE-GUIDE.md) first — it explains which root files are part of the open-source template infrastructure (safe to delete in a private fork) and which are your company's actual operating model content (fill in and own).

---

## Quick Start (30 minutes to a working framework)

### Step 1: Fill in CONFIG.yaml (10 min)

Open [CONFIG.yaml](CONFIG.yaml) and fill in every field. This gives the framework your company's identity, toolchain, and organizational shape. The most critical fields:

| Field | Why It Matters |
|-------|---------------|
| `company.name` | Appears throughout every document |
| `vision.north_star` | Anchors all strategic alignment checks |
| `vision.mission` | Guides every agent's decision-making |
| `toolchain.*` | Determines which concrete tools implement your quality policies |
| `work_backend.type` | Determines where work artifacts are tracked (git files or issue tracker) |

### Step 2: Search & Replace Placeholders (5 min)

After filling CONFIG.yaml, do a global search-and-replace across the repository:

```bash
# Replace company name throughout
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_NAME}}/YourCompanyName/g'
find . -name "*.md" -o -name "*.yaml" | xargs sed -i '' 's/{{COMPANY_SHORT}}/YourShort/g'
```

### Step 3: Review Core Documents (10 min)

Read and adjust these three files — they set the tone for everything:

1. [COMPANY.md](COMPANY.md) — Vision, mission, strategic beliefs. Make them yours.
2. [AGENTS.md](AGENTS.md) — Global agent rules. Adjust identity section.
3. [OPERATING-MODEL.md](OPERATING-MODEL.md) — The meta-description. Verify it matches your reality.

### Small Team or Solo Founder?

If you're a small team or solo founder, start with a **minimal agent fleet** — one agent per active layer. See [Minimal Agent Fleet](#minimal-agent-fleet) below for the exact setup.

### Step 4: Choose Your Work Backend (2 min)

Decide where operational work artifacts (signals, missions, tasks, decisions) will be tracked:

| Backend | Best For | Set In CONFIG.yaml |
|---------|----------|--------------------|
| **Git files** (default) | Self-contained, no external dependencies, maximum auditability | `work_backend.type: "git-files"` |
| **GitHub Issues** | Better human collaboration, native boards, labels, notifications, mobile access | `work_backend.type: "github-issues"` |

If using GitHub, **GitHub Issues is recommended** — it's always available and provides dramatically better visibility for humans. See [docs/WORK-BACKENDS.md](docs/WORK-BACKENDS.md) for the full guide including label taxonomy.

> **Note:** Governance backbone files (org structure, policies, agent instructions, templates) always stay in Git regardless of this choice.

### Step 5: Register Your Integrations (5 min)

Review `CONFIG.yaml → integrations` and register the external tools your organization uses:

1. **Observability** — Your monitoring platform (Dynatrace, Grafana, Datadog, etc.) — essential for scaling agent governance
2. **Enterprise toolchain** — CI/CD, ITSM, security scanning, service catalogs
3. **Business systems** — CRM, support platforms, analytics
4. **Communication** — Chat, messaging, notification channels

See `org/integrations/` for detailed guides per category. Start with observability and CI/CD — they provide the most immediate value.

### Step 6: Start Using It (5 min)

**Git-files backend:** Create your first signal in `work/signals/` and you're live.

**Issue backend:** Create your first GitHub Issue with label `artifact:signal` and you're live. Use the template structure from `work/signals/_TEMPLATE-signal.md` for the issue body.

---

## Minimal Agent Fleet

For small teams and solo founders, start with **5 agents — one per layer**. This gives every layer a dedicated owner with clear boundaries and no collapsed responsibilities. Expand agent counts within each layer as signal volume and mission throughput grow.

### Minimal 5-Agent Fleet

| Agent | Layer | Responsibility | When it runs |
|---|---|---|---|
| **Steering Agent** | Layer 0 | Signal aggregation, weekly digests, pattern detection, evolution proposals | Weekly (digest cadence) + on signal volume threshold |
| **Strategy Agent** | Layer 1 | Signal triage, mission brief creation, outcome contracts, venture health | On every signal digest + mission lifecycle events |
| **Orchestration Agent** | Layer 2 | Fleet config, mission decomposition, release preparation, mission status tracking | On every mission state change + release events |
| **Execution Agent(s)** | Layer 3 | Implementation — code, research, content, tests, PRs | When a task is assigned |
| **Quality Agent** | Layer 4 | Policy evaluation, operate-loop signaling, outcome measurement, stall detection | Continuously (after builds, before merges, on measurement schedule dates) |

> **Solo founder rule:** You still merge PRs — that is your only required action. But each layer now has a dedicated agent, so no responsibilities are collapsed or dropped.

### Why 5 Agents, Not 3

The original 3-agent fleet collapsed Steering + Strategy + Orchestration into a single Orchestration Agent and overloaded the Quality Agent with operate-loop duties. This caused:

- **Signal triage gap:** No agent explicitly owned the Signal → Mission Brief flow
- **Digest gap:** Weekly signal aggregation had no owner
- **Ship/Release gap:** Release preparation was not wired to any agent
- **Operate-loop gap:** Production signaling and stall detection were undocumented responsibilities

With one agent per layer, every loop in the lifecycle has an explicit owner.

### How the 5 Layers Map to a Small Team

| Layer | Small team (1 agent) | Scales to |
|---|---|---|
| **Steering** — evolve the company | Steering Agent (+ you as approver) | Multiple steering agents + AI assistance |
| **Strategy** — decide WHY + WHAT | Strategy Agent (+ you as approver) | Venture-specific strategy agents |
| **Orchestration** — HOW to execute | Orchestration Agent | Fleet of orchestrators per domain |
| **Execution** — DO the work | Execution Agent(s) | Dozens of specialized agents per division |
| **Quality** — EVALUATE outputs | Quality Agent | Domain-specific evaluators |

Add specialized Execution Agents first as you scale (e.g., one coding-focused, one research-focused), then additional Orchestration or Steering Agents when signal volume or mission throughput justifies it.

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

- ❌ Heavyweight project management tool — missions **are** your tickets (whether as issues or files)
- ❌ Standup meetings — mission status updates **are** the standup (issue comments or STATUS.md)
- ❌ Separate OKR framework — `CONFIG.yaml` vision + active missions = your strategy
- ✅ An issue tracker is optional but **recommended** for human-facing visibility (`work_backend.type: "github-issues"`)

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

7. **File your first signal:**
   - **Git-files backend:** Create `work/signals/YYYY-MM-DD-<your-first-opportunity>.md` from the template (`work/signals/_TEMPLATE-signal.md`).
   - **Issue backend:** Create a GitHub Issue with label `artifact:signal` and the structured body from the signal template. The issue's Project Status will default to `Backlog`.
   This is the input that kicks off the entire lifecycle.
8. **Steering Agent: Produce first digest** — The Steering Agent aggregates signals into a weekly digest (`work/signals/digests/YYYY-WXX-digest.md`), detecting patterns and flagging priorities.
9. **Strategy Agent: Triage to a mission** — The Strategy Agent consumes the digest, triages signals, and if a signal warrants action:
   - Creates `work/missions/<mission-name>/MISSION-BRIEF.md` from `work/missions/_TEMPLATE-mission-brief.md`
   - Creates `work/missions/<mission-name>/OUTCOME-CONTRACT.md` from `work/missions/_TEMPLATE-outcome-contract.md` (with `measurement_schedule` dates)
10. **Orchestration Agent: Assemble fleet + decompose tasks** — The Orchestration Agent creates a fleet config (`org/2-orchestration/fleet-configs/<mission>.md`), decomposes the mission into tasks (TASKS.md), and prepares release contracts when outputs are quality-approved.
11. **Execution Agent(s): Execute** — Execution agents produce work within mission scope (code, docs, content, tests).
12. **Quality Agent: Evaluate + close the loop** — The Quality Agent evaluates outputs against policies, triggers outcome reports when measurement schedule dates arrive, files production signals, and detects stalled missions. The full 5-layer loop is live.

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
   - **Core divisions:** Data Foundation, Core Services, Core Applications
   - **Domain divisions:** Placeholders — fill with your product-specific domains
   - **Ops divisions:** Engineering Foundation, Infrastructure Operations
   - **GTM divisions:** Product Marketing, Knowledge & Enablement
   - **Customer divisions:** Customer Experience
   - **Optional extensions:** AI & Intelligence, GTM Web, Quality & Security Engineering when your operating model truly needs dedicated execution-side specialization

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

The framework ships with 16 quality policies. Customize each:

| Policy | What to Customize |
|--------|------------------|
| [security.md](org/4-quality/policies/security.md) | Your specific security requirements, compliance frameworks (SOC2, HIPAA, etc.) |
| [agent-security.md](org/4-quality/policies/agent-security.md) | Your agent-specific security posture (prompt injection mitigations, tool abuse prevention, OWASP LLM Top 10 coverage) |
| [ai-governance.md](org/4-quality/policies/ai-governance.md) | Your AI risk tier assignments per agent type, fairness metrics and thresholds, model allowed list, token budget ceilings, adversarial test suites, explainability implementation, EU AI Act applicability assessment |
| [risk-management.md](org/4-quality/policies/risk-management.md) | Your risk appetite thresholds (via `CONFIG.yaml → risk_appetite`), agent autonomy tier assignments, risk taxonomy applicability, regulatory crosswalk for your target certifications |
| [cryptography.md](org/4-quality/policies/cryptography.md) | Your approved algorithms, key rotation schedules (via `CONFIG.yaml → encryption`), certificate lifetimes, KMS integration, post-quantum migration timeline |
| [privacy.md](org/4-quality/policies/privacy.md) | Your controller/processor model, lawful bases, DPA terms, DSAR channels, breach-notification contacts, transfer mechanisms |
| [data-classification.md](org/4-quality/policies/data-classification.md) | Your classification taxonomy extensions (industry-specific sub-labels), data category inventory, retention schedules per level, access control mappings to your IAM, PII inventory for your data landscape |
| [architecture.md](org/4-quality/policies/architecture.md) | Your API conventions, service patterns, catalog requirements |
| [experience.md](org/4-quality/policies/experience.md) | Your design system name, accessibility standards, UI patterns |
| [performance.md](org/4-quality/policies/performance.md) | Your specific latency budgets, cost constraints, resource limits |
| [delivery.md](org/4-quality/policies/delivery.md) | Your deployment model, environments, rollback procedures |
| [incident-response.md](org/4-quality/policies/incident-response.md) | Your on-call model, escalation paths, communication thresholds, and any stricter contractual incident targets |
| [availability.md](org/4-quality/policies/availability.md) | Your service tiers, RTO/RPO targets, backup/restore design, failover strategy, drill cadence |
| [content.md](org/4-quality/policies/content.md) | Your brand guidelines, documentation standards, content taxonomy |
| [customer.md](org/4-quality/policies/customer.md) | Your SLA definitions, customer interaction standards |
| [observability.md](org/4-quality/policies/observability.md) | Your telemetry standards, agent observability requirements, alerting thresholds |

**Key principle:** Start with the policies as shipped (they're reasonable defaults for a software enterprise). Then tighten or loosen based on your regulatory environment, risk tolerance, and maturity level.

> **Risk management note:** The risk management policy references configurable thresholds from `CONFIG.yaml → risk_appetite`. Fill in these values during Step 1 — they define your organization's risk tolerance for downtime, cost overruns, escalation rates, and agent behavioral thresholds. See the [Placeholder Reference](#placeholder-reference) for the full list of `{{RISK_*}}` variables.

> **Encryption note:** The cryptography policy references key rotation schedules and certificate lifetimes from `CONFIG.yaml → encryption`. Fill in these values during Step 1 — defaults are conservative (90-day symmetric key rotation, 90-day cert lifetime). Adjust based on your compliance requirements (PCI DSS, HIPAA, FedRAMP) and operational maturity. See the [Placeholder Reference](#placeholder-reference) for the full list of `{{CRYPTO_*}}` variables.

> **Data classification note:** The data classification policy defines a 4-level scheme (PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED) with handling requirements per level. Adopters should: (1) review whether the four levels fit their industry — add sub-labels if needed (e.g., `CONFIDENTIAL-FINANCIAL`, `RESTRICTED-HEALTH`) but do not remove levels; (2) create a PII inventory using `work/assets/_TEMPLATE-pii-inventory.md` for each personal data category they process; (3) map their existing data stores to classification levels; (4) align retention schedules with legal/regulatory requirements per classification level.

> **AI governance note:** The AI governance policy defines a 4-tier risk classification (Prohibited / High-Risk / Limited-Risk / Minimal-Risk) aligned with EU AI Act risk tiers. Adopters should: (1) classify each agent type by risk tier based on its impact and autonomy; (2) fill in the Model Governance section in each agent type definition (added to `org/agents/_TEMPLATE-agent-type.md`); (3) define fairness metrics and thresholds appropriate to their industry (the policy provides common metrics; adopters select which apply); (4) set token budget ceilings per mission type and agent type; (5) define their model allowed list (which LLMs are approved for which risk tiers). EU AI Act enforcement begins August 2026 — adopters in EU-regulated industries should prioritize Tier 1 (High-Risk) compliance.

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
| Git-native governance | ✅ Yes | Fundamental to the model (for governance backbone) |
| Agent instruction hierarchy | ✅ Yes | Critical for multi-agent governance |
| Improvement signal flow | ✅ Yes | Key innovation of the model |
| Integration Registry structure | ✅ Yes | Governed connection patterns |
| Company name/vision/mission | ❌ Customize | Your identity |
| Work backend choice | ❌ Customize | Git files or issue tracker — your preference |
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
| `{{RISK_MAX_DOWNTIME_MINUTES}}` | CONFIG.yaml → risk_appetite.max_downtime_minutes | Risk management policy |
| `{{RISK_COST_OVERRUN_THRESHOLD}}` | CONFIG.yaml → risk_appetite.cost_overrun_threshold_pct | Risk management policy |
| `{{RISK_KILL_SWITCH_TARGET_SECONDS}}` | CONFIG.yaml → risk_appetite.kill_switch_target_seconds | Risk management policy |
| `{{RISK_ESCALATION_RATE_THRESHOLD}}` | CONFIG.yaml → risk_appetite.escalation_rate_threshold_pct | Risk management policy |
| `{{RISK_TOOL_FAILURE_THRESHOLD}}` | CONFIG.yaml → risk_appetite.tool_failure_threshold_pct | Risk management policy |
| `{{RISK_CYCLE_TIME_VARIANCE}}` | CONFIG.yaml → risk_appetite.cycle_time_variance_pct | Risk management policy |
| `{{RISK_HALLUCINATION_THRESHOLD}}` | CONFIG.yaml → risk_appetite.hallucination_threshold_pct | Risk management policy |
| `{{CRYPTO_ROTATION_SYMMETRIC_DAYS}}` | CONFIG.yaml → encryption.rotation_symmetric_days | Cryptography policy |
| `{{CRYPTO_ROTATION_SIGNING_DAYS}}` | CONFIG.yaml → encryption.rotation_signing_days | Cryptography policy |
| `{{CRYPTO_ROTATION_ASYMMETRIC_DAYS}}` | CONFIG.yaml → encryption.rotation_asymmetric_days | Cryptography policy |
| `{{CRYPTO_ROTATION_API_KEY_DAYS}}` | CONFIG.yaml → encryption.rotation_api_key_days | Cryptography policy |
| `{{CRYPTO_CERT_LIFETIME_DAYS}}` | CONFIG.yaml → encryption.cert_lifetime_days | Cryptography policy |
| `{{CRYPTO_RSA2048_DEPRECATION_DATE}}` | CONFIG.yaml → encryption.rsa2048_deprecation_date | Cryptography policy |
| `{{CRYPTO_REVOCATION_TARGET_HOURS}}` | CONFIG.yaml → encryption.revocation_target_hours | Cryptography policy |
| `{{CERT_MANAGER}}` | CONFIG.yaml → encryption.cert_manager | Cryptography policy |

---

## Staying in Sync with the Upstream Framework

Your fork is a living instance of the [Agentic Enterprise](https://github.com/wlfghdr/agentic-enterprise) template. The upstream framework evolves — new patterns, improved policies, better templates. Treat the relationship as bidirectional: **pull improvements in, push discoveries back.**

### Adopting upstream updates

```bash
# Add upstream remote (one-time)
git remote add upstream https://github.com/wlfghdr/agentic-enterprise.git

# Fetch upstream changes
git fetch upstream main

# Review what changed
git log upstream/main --oneline --since="last month"
git diff main...upstream/main -- CHANGELOG.md
```

**Recommended cadence:** Check upstream at least monthly, or as part of your Steering Layer's evolution cycle. Compare the upstream `CHANGELOG.md` against your current `framework_version` in `CONFIG.yaml`.

**Merge selectively.** Not every upstream change applies to your instance — you may have deliberately diverged in areas like policies, divisions, or process. Evaluate each update against your local customizations:
- Template improvements (`_TEMPLATE-*.md`) → usually safe to adopt
- New agent types or policies → evaluate fit before merging
- Structural changes to `AGENTS.md` or `OPERATING-MODEL.md` → review carefully, may conflict with local rules

### Contributing improvements back

When your agents (or you) discover a pattern, fix, or improvement that is **not company-specific**, share it upstream:

1. **File an issue** on the template repo describing the improvement
2. **Open a PR** following the upstream `CONTRIBUTING.md` guidelines
3. Or at minimum, **start a discussion** — even a rough observation is valuable

What belongs upstream: bug fixes in templates, new generic agent types, policy refinements, structural patterns, documentation improvements.
What stays in your fork: company identity, proprietary strategies, division details, custom integrations, internal work artifacts.

**Why this matters:** Every instance that contributes back makes the framework better for all adopters. Your agents already observe friction and file improvement signals (Rule 7 in AGENTS.md) — extending that habit to the upstream framework is a natural evolution. Rule 13 in AGENTS.md instructs agents to do this automatically.

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
