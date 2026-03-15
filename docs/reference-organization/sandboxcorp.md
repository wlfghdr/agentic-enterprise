# Reference Organization

## What Is the Reference Organization?

The Agentic Enterprise framework is exercised by a **reference organization** — a real operational instance that runs the operating model end-to-end. It exists to prove the framework works, not in theory, but by producing real artifacts, enforcing real governance, and completing real missions.

Think of it as the **reference implementation** for the framework. The same way a programming language ships with a standard library, Agentic Enterprise ships with a reference organization that exercises every layer, loop, and policy.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   Agentic Enterprise         Reference Organization      │
│   ─────────────────         ─────────────────────────    │
│   The framework              A running instance           │
│   (templates, policies,      (real signals, missions,     │
│    agent instructions,        PRs, releases, decisions)   │
│    process definitions)                                   │
│                                                          │
│   You fork this.             You study this.              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Why a Reference Organization?

Without a running example, the framework is just templates. The reference organization answers three questions:

1. **Does the governance model actually work?** — It files signals, converts them to missions, runs quality gates, and produces releases. If any process step breaks, the framework gets fixed.

2. **What does "good" look like?** — New adopters can see real mission briefs, real decision records, and real outcome reports instead of guessing how to fill in templates.

3. **How does the feedback loop close?** — Operational experience generates improvement signals that flow back into the framework itself (see [AGENTS.md Rule 13a](../../AGENTS.md)).

## Operational Proof

This is not a thought experiment. The reference organization has produced real, auditable work:

| Metric | Count | What It Represents |
|--------|------:|---------------------|
| **Work items** (signals, missions, tasks) | 99 | Observations triaged, work scoped, tasks tracked |
| **Pull Requests** | 108 | Governed changes — each reviewed, approved, merged |
| **Commits** | 440+ | Individual changes with audit trail |
| **Governed artifacts total** | 647+ | Every decision traceable in Git history |

Every one of these artifacts was produced through the operating model: a signal was filed, a mission was scoped, work was executed through PRs, and outcomes were measured. The Git history is the proof.

## What It Does

The reference organization maintains two products under the same governance model:

1. **The framework itself** — using the framework to improve the framework. Templates, policies, agent instructions, and process definitions are all treated as products with signals, missions, and quality gates. This makes the framework self-improving: every friction point discovered while using it becomes a signal that leads to a fix.

2. **A fully functional application** — a real application with real dependencies, built and operated under the same governance. This proves the framework works beyond self-reference — it exercises the full lifecycle (design, build, ship, operate) against production-grade software.

| Activity | What It Produces |
|----------|-----------------|
| **Signal detection** | Improvement opportunities filed from operations, telemetry, and policy gaps |
| **Mission execution** | End-to-end mission lifecycle — from brief through fleet config to outcome report |
| **Governance validation** | 108 PRs that exercise CODEOWNERS, quality policies, and approval workflows |
| **Policy testing** | Quality evaluations that verify policies are enforceable and measurable |
| **Observability integration** | OTel telemetry patterns tested against real agent workflows |
| **Framework improvement** | 440+ commits of changes driven by operational friction |

## Example Missions

These are representative missions that the reference organization runs to exercise the framework:

| Mission | What It Tests |
|---------|--------------|
| **Add privacy policy surface** | Full lifecycle: signal → mission → policy creation → quality eval → release |
| **Implement incident response SLAs** | Cross-division coordination, policy authoring, observability requirements |
| **Onboard a new execution division** | Steering layer evolution, org structure changes, CODEOWNERS updates |
| **Close compliance gaps** | Compliance-driven work, gap analysis, remediation guides, evidence production |
| **Integrate observability platform** | Integration Registry, CONFIG.yaml changes, OTel contract validation |

## How It Improves the Framework

The reference organization operates a continuous feedback loop:

```
Run the framework
       │
       ▼
Discover friction, gaps, or failures
       │
       ▼
File improvement signal
       │
       ▼
Triage → Mission → Fix
       │
       ▼
Merge improvement into framework
       │
       ▼
Run the framework again (improved)
```

Every template change, policy addition, and structural improvement in the framework's history was discovered by running the reference organization against it. This is how the framework stays grounded in operational reality rather than drifting into pure theory.

## Framework vs. Organization — The Key Distinction

| | Agentic Enterprise | Reference Organization |
|---|---|---|
| **What it is** | Open-source operating model | Running instance |
| **What you do with it** | Fork and customize | Study and learn from |
| **Contains** | Templates, policies, agent instructions, process definitions | Filled-in artifacts, real missions, operational history |
| **Changes how?** | Community PRs, upstream contributions | Running the framework and feeding back learnings |
| **Your equivalent** | Your fork of the repo | Your company running on the fork |

## Getting Started with Your Own Organization

The reference organization is a proof point — you build your own. Start with:

1. [Minimal Adoption Guide](../adoption/minimal-adoption.md) — the simplest path to running the framework
2. [10-Minute Quickstart](../quickstart/10-minute-agentic-enterprise.md) — understand the core workflow
3. [customization-guide.md](../customization-guide.md) — full onboarding walkthrough
