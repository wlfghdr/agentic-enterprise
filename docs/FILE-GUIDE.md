# File Guide — What Is What and What to Do in a Fork

> **Purpose:** This repo serves a dual role. It is simultaneously an **open-source template project** (publicly hosted on GitHub) and a **concrete example of a company operating model** (the thing you fork and run with). That means the root directory mixes two very different kinds of files. This guide tells you exactly what each file is for, and what to do with it when you fork.

---

## The Two Contexts

| Context | Meaning |
|---|---|
| **Template/OSS** | This public repo — describes, demonstrates, and evolves the *framework itself* |
| **Company fork** | Your private fork — instantiates the framework *for your org* |

Most adopters only ever need the **Company fork** context. The OSS context matters if you want to contribute improvements back to the upstream framework.

---

## Root File Classification

### Category 1 — OSS Framework Infrastructure
> **In your fork:** Safe to delete. These files exist because `github.com/wlfghdr/agentic-enterprise` is a public open-source project. They do not contain company-specific content — they describe the *framework itself* to potential adopters and OSS contributors.

| File | Purpose | Fork action |
|---|---|---|
| `README.md` | Public-facing overview of the open-source framework. 496-line marketing/adoption doc targeting GitHub visitors. | Delete or replace with your own internal README |
| `CONTRIBUTING.md` | How to contribute to the upstream OSS template. | Delete (irrelevant to a private fork) |
| `CODE_OF_CONDUCT.md` | OSS community conduct standards (Contributor Covenant). | Delete (or keep if your org wants community norms documented) |
| `SECURITY.md` | Security disclosure policy for the public OSS project. | Delete or replace with your org's actual security policy |
| `LICENSE` | Apache 2.0 — required for OSS. **You must keep this** to honour attribution. | Keep (required by Apache 2.0) |
| `NOTICE` | Attribution notice (Apache 2.0 requirement). | Keep (required by Apache 2.0) |
| `index.html` | Landing/demo page for the public GitHub Pages site (`wlfghdr.github.io/agentic-enterprise`). | Delete |
| `concept-visualization.html` | Interactive HTML visualization of the framework model — demo/presentation aid. | Delete (or keep for internal presentations) |

### The `.github/` folder — file by file

The `.github/` folder mixes OSS infrastructure with governance tooling that's genuinely useful in a company fork. Do not delete it wholesale — read the per-file guidance below.

**Quick summary:**
- **Keep:** `workflows/validate.yml`, `PULL_REQUEST_TEMPLATE.md`, `copilot-instructions.md`
- **Keep if using the CI feature:** `workflows/policy.yml`, `workflows/security.yml`
- **Delete:** `workflows/stale.yml`, `ISSUE_TEMPLATE/`

| File / Folder | OSS purpose | Company fork action |
|---|---|---|
| `workflows/validate.yml` | Core CI: validates operating model docs, schemas, locks, placeholders | **Keep** — these gates enforce governance in your fork too. They check that your config, policies, and artifacts stay consistent. |
| `workflows/policy.yml` | OPA/Conftest policy enforcement (workflow permissions, pinned actions) | **Keep** if using the Policy-as-Code gate (see `docs/POLICY-AS-CODE.md`); delete if not |
| `workflows/security.yml` | Gitleaks secret scanning + GitHub Dependency Review | **Keep** if using security scanning (see `docs/SECURITY-SCANNING.md`); delete if not |
| `workflows/stale.yml` | Marks and closes stale GitHub Issues/PRs (OSS housekeeping) | **Delete** — irrelevant in a private fork. Your work flows through `work/signals/` and `work/missions/`, not GitHub Issues. |
| `ISSUE_TEMPLATE/` | Bug report and config forms for OSS contributors | **Delete** — your fork uses `work/signals/` for signal intake, not GitHub Issues for internal triage |
| `PULL_REQUEST_TEMPLATE.md` | PR checklist reminding contributors to cite policies and evidence | **Keep and adapt** — update checklist items to match your fork's governance conventions |
| `copilot-instructions.md` | GitHub Copilot agent instructions for working in this repo | **Keep and update** — edit after customization to reference your company name, divisions, and active missions |
| `prompts/` | Agent skill prompts (e.g., `/deploy` workflow) | **Keep and adapt** — update prompts to reference your company's structure and toolchain |

---

### Category 2 — Company Operating Model Content
> **In your fork:** These ARE your operating model. Fill them in. Own them. They represent the actual substance of your agentic enterprise. **Do not delete.** Do not contribute these back to the upstream OSS repo.

| File | Purpose | Fork action |
|---|---|---|
| `CONFIG.yaml` | **Start here.** Company identity, product names, toolchain, integrations, org shape. Every `{{VARIABLE}}` placeholder in the repo references this. | Fill in completely — see `CUSTOMIZATION-GUIDE.md` |
| `COMPANY.md` | Company vision, mission, strategic beliefs, and long-term direction. Currently has `{{COMPANY_NAME}}` placeholders. | Replace placeholders with your actual company content |
| `AGENTS.md` | Global agent rules — the top of the instruction hierarchy. Every agent in every layer reads this first. Partly template scaffolding, partly company-specific governance. | Customise the Identity section and Product Naming rules with your own |
| `OPERATING-MODEL.md` | Meta-description of how the operating model works inside your company. | Adjust to match your actual deployment choices |
| `CODEOWNERS` | RACI map — who approves what. Replace placeholder role names with real GitHub team names. | Populate with actual `@org/team-name` handles |
| `org/` | Org structure: 5 layers, agent type registry, integration registry, quality policies. | Customise divisions, add ventures, fill in integration configs |
| `process/` | 4-loop lifecycle guides (Discover → Build → Ship → Operate). | Adjust to your actual delivery workflow |
| `work/` | Active work artifacts — signals, missions, decisions, releases, retrospectives. | Use daily. File signals, open missions, record decisions. |

---

### Category 3 — Agent Bootstrap (Companion Files)
> **In your fork:** Keep and update. These are utility files that let AI coding assistants and agent runtimes automatically pick up the right instructions without manual prompting.

| File | Purpose | Fork action |
|---|---|---|
| `CLAUDE.md` | Auto-loaded by Claude Code (Anthropic's agent). **Mirrors the content of `AGENTS.md`** for the Claude tooling context. When you update `AGENTS.md`, keep this in sync — they must be consistent. Exists solely because Claude Code reads `CLAUDE.md` by convention; `AGENTS.md` is the canonical source of truth. | Keep and sync with `AGENTS.md` after any changes |
| `CUSTOMIZATION-GUIDE.md` | Step-by-step guide for tailoring this framework to your company. | Read and follow during initial setup; keep for onboarding new team members |

---

### Category 4 — Examples (Reference Only)
> **In your fork:** Keep as reference or delete. These illustrate how the framework operates in practice — they are not live work artifacts.

| File | Purpose | Fork action |
|---|---|---|
| `examples/` | Illustrative lifecycle walkthroughs (feature build, fleet change, company optimization). Show how missions and loops work together. | Keep for onboarding or delete once your team knows the model |

---

## The CLAUDE.md / AGENTS.md Relationship

These two files contain near-identical content. This is intentional:

```
AGENTS.md          ← Canonical source of truth (humans + all agents read this)
CLAUDE.md          ← Claude Code companion (auto-loaded by Anthropic tooling)
```

**Workflow:** Edit `AGENTS.md` first. Then propagate changes to `CLAUDE.md`. Treat `CLAUDE.md` as a derived file. If you use other agent runtimes that have similar auto-load conventions (e.g., `.cursor/rules`, GitHub Copilot instructions), add analogous companion files and document them here.

---

## What a Clean Fork Looks Like

After forking and completing `CUSTOMIZATION-GUIDE.md` Step 1–5, your root should contain:

```
# Keep & fill in — this is your operating model
CONFIG.yaml
COMPANY.md
AGENTS.md
CLAUDE.md                   # keep, sync with AGENTS.md
CODEOWNERS                  # update with real team handles
OPERATING-MODEL.md
CUSTOMIZATION-GUIDE.md      # keep for onboarding

# OSS attribution — required by Apache 2.0
LICENSE
NOTICE

# Optionally keep
examples/                   # useful until team is fluent

# Delete — OSS/demo only, irrelevant in a private fork
README.md                   # replace with your own
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md                 # replace with your org's policy
index.html
concept-visualization.html

# .github/ — keep selectively (see per-file table above)
# Keep: validate.yml, PULL_REQUEST_TEMPLATE.md, copilot-instructions.md
# Delete: stale.yml, ISSUE_TEMPLATE/
```

---

## CODEOWNERS Classification

The [CODEOWNERS](../CODEOWNERS) file follows the same categorization:

| Section | Who Reviews |
|---|---|
| OSS Framework Infrastructure | `@steering-executive` |
| Agent Runtime Bootstrap (`CLAUDE.md`) | `@steering-executive` |
| Company Operating Model Content | `@steering-executive` |
| Layer org structure | Layer-appropriate owner (see CODEOWNERS) |
| Work artifacts | Role closest to the artifact type |

In a private fork, replace all placeholder handles (`@steering-executive`, `@cto`, etc.) with actual GitHub team names from your organization.
