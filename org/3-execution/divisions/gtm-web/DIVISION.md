# Division: GTM Web

> **Owner:** <!-- Division lead name -->
> **Type:** GTM / Engineering
> **Layer:** Execution
> **Status:** Active
> **Version:** 1.1
> **Last updated:** 2026-03-02

---

## Purpose

Owns the public-facing web presence — marketing sites, landing pages, interactive demos, and conversion flows. Translates product marketing direction into performant, accessible web experiences through PR-based delivery.

## Scope

### In Scope
- Marketing website pages and landing pages
- Interactive product demos and visualizations
- Hero sections, feature showcases, and conversion flows
- CSS/JS animations and micro-interactions
- Web performance optimization (Core Web Vitals, load time, 60fps animations)
- Mobile responsiveness and cross-browser compatibility
- SEO-relevant markup and structured data

### Out of Scope
- Backend infrastructure or server-side rendering (→ Infrastructure Operations)
- Product strategy or venture decisions (→ Strategy Layer)
- Content copywriting and messaging strategy (→ Product Marketing)
- Domain/DNS/hosting management (→ Infrastructure Operations)
- Application UIs behind authentication (→ Core Applications)

## Key Responsibilities

1. **Web Experience Delivery** — Build and iterate on marketing web pages based on mission briefs and signals
2. **Animation & Interaction Engineering** — Implement performant CSS/JS animations meeting the 60fps target
3. **Mobile Responsiveness** — Ensure all changes work across device sizes (320px → 1600px+)
4. **Performance** — Maintain fast load times; minimize external dependencies loaded at runtime
5. **Conversion Optimization** — Structure CTAs, navigation, and user flows for maximum engagement
6. **Signal Filing** — File `work/signals/` entries when UX patterns, performance regressions, or content gaps are observed

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Receives from | Product Marketing | Copy, messaging, and positioning direction |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Knowledge & Enablement | Documentation and tutorial pages |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/content.md` — All customer-facing copy
- `policies/security.md` — No inline secrets, no third-party scripts without review
- `policies/architecture.md` — For structural HTML/CSS changes

## Human Checkpoints

These decisions require human division lead involvement:

- Any change to production web pages (all PRs require human merge)
- Introduction of new external scripts, fonts, or CDN dependencies
- Brand/color system overhauls
- Navigation structure changes

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Prefer CSS transforms + opacity for animations (no layout thrashing)
3. Test across breakpoints: 320px, 768px, 1024px, 1440px+
4. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
5. Keep pages loading fast — avoid heavy JS frameworks for marketing pages

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Marketing site | `index.html` | Primary landing page |
| Visualizations | `concept-visualization.html` | Interactive demo |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-15 | Initial version with changelog and versioning metadata |
