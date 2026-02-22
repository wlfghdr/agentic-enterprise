# User Experience Policy

> **Applies to:** All user-facing surfaces — UI, CLI, APIs, documentation, error messages
> **Enforced by:** Quality Layer eval agents
> **Authority:** UX/Design team leads
> **Version:** 1.1 | **Last updated:** 2026-02-23

---

## Principles

1. **User-first** — Every interaction optimized for the end user, not the system.
2. **Consistent** — Common patterns across all surfaces.
3. **Accessible** — Usable by everyone, including users with disabilities.
4. **Progressive disclosure** — Show the essential first, details on demand.

## Mandatory Requirements

### Visual Design
- [ ] Uses the company design system components and tokens exclusively
- [ ] Typography, spacing, and color follow design system guidelines
- [ ] Icons from the approved icon set only
- [ ] No pixel-based sizing (use design tokens / rem / em)

### Interaction Design
- [ ] Loading states for all async operations
- [ ] Error states with actionable recovery guidance
- [ ] Empty states with clear next actions
- [ ] Confirmation for destructive actions
- [ ] Undo where feasible

### Accessibility
- [ ] WCAG 2.1 AA compliance minimum
- [ ] Keyboard navigation for all interactive elements
- [ ] Screen reader compatibility (proper ARIA labels)
- [ ] Sufficient color contrast ratios
- [ ] Focus management (visible focus indicators)

### Content & Microcopy
- [ ] Error messages explain what happened AND what to do
- [ ] Labels are clear, concise, and action-oriented
- [ ] No jargon in user-facing text (unless industry-standard)
- [ ] Consistent terminology (matches glossary)

### Performance (User-Perceived)
- [ ] Time to interactive < 3 seconds
- [ ] Perceived loading < 1 second for common operations
- [ ] Optimistic UI updates where appropriate
- [ ] No layout shifts during loading

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Design system usage | 100% standard components | Custom components |
| Accessibility | WCAG 2.1 AA | Any AA violation |
| Error handling | Actionable error messages | Generic "something went wrong" |
| Loading states | All async ops have states | Missing loading indicators |
| Keyboard navigation | Fully navigable | Keyboard traps or missing |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
| 1.1 | 2026-02-23 | Replace {{DESIGN_SYSTEM_NAME}} placeholder with generic "company design system" language |
