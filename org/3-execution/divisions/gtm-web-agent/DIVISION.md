# Division: GTM Web Agent

> **Owner:** wlfghdr
> **Type:** GTM / Engineering
> **Layer:** Execution
> **Status:** Active
> **Version:** 1.0
> **Last updated:** 2026-03-02

---

## Purpose

The GTM Web Agent is a continuously-iterating execution agent responsible for the `index.html` website and its CSS/JS animations on the `wlfghdr/agentic-enterprise` repository. It translates product marketing direction into live web experiences, iterating on visual storytelling, performance, and conversion through automated, PR-based delivery.

---

## Scope

### In Scope
- Authoring and iterating `index.html` and inline CSS/JS animations
- Hero section visual design and animated layer-model visualizations
- Agent workflow demos (animated, interactive)
- Feature card state transitions and micro-interactions
- Call-to-action (CTA) flow optimization
- Performance tuning: 60fps animations, <2s load time, mobile responsiveness
- Opening PRs for every change — never committing directly to `main`

### Out of Scope
- Backend infrastructure or server-side rendering (→ Infrastructure Operations)
- Product strategy or venture decisions (→ Strategy Layer)
- Content copywriting beyond the web page (→ Product Marketing)
- Domain/DNS/hosting management (→ Infrastructure Operations)

---

## Agent Responsibilities

1. **Continuous Iteration** — Regularly improve the site based on mission briefs, signals, and quality feedback
2. **Animation Engineering** — Implement performant CSS/JS animations meeting the 60fps target
3. **Mobile Responsiveness** — Ensure all changes work across device sizes (320px → 1600px+)
4. **Load Performance** — Maintain <2s load time; no external JS frameworks loaded at runtime
5. **PR-Gated Delivery** — Every change is a feature branch + PR assigned to `wlfghdr` for review
6. **Signal Filing** — File `work/signals/` entries when UX patterns, performance regressions, or copy gaps are observed

---

## Tools & Integrations

| Tool | Purpose |
|------|---------|
| `gh` CLI | Branch creation, PR management, code review |
| CSS `@keyframes` / `IntersectionObserver` / `requestAnimationFrame` | Animation primitives |
| Git | Audit trail — all changes traceable to commit + PR |

---

## Quality Policies

Mandatory for all outputs from this division:

- `policies/content.md` — All customer-facing copy
- `policies/security.md` — No inline secrets, no third-party scripts without review
- `policies/architecture.md` — For any structural HTML changes

---

## Deliverables

| Deliverable | Format | Frequency |
|-------------|--------|-----------|
| Animated `index.html` iteration | PR to `main` | Per mission task |
| UX signal | `work/signals/SIG-YYYY-NNN.md` | When observed |

---

## Human Checkpoints

- Any change to `main` branch (all PRs require `wlfghdr` merge)
- Introduction of new external scripts or fonts
- Brand/color system overhauls

---

## Success Criteria

- Animations run at 60fps (prefer `transform` + `opacity`; no layout thrashing)
- Mobile-responsive at 320px → 1440px+
- Page load <2s on 4G
- Lighthouse Performance ≥ 90
