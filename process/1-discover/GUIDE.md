# Discover Loop — Guide

> **What this covers:** How signals become missions. The complete Discover loop workflow.

---

## Signal Sources

> **Customize:** Add your organization's specific signal sources.

| Source Category | Examples | How Agents Access |
|----------------|----------|-------------------|
| **Market** | Industry reports, analyst briefings, competitive announcements | Configured feeds, web monitoring |
| **Customer** | Support tickets, NPS feedback, feature requests, churn signals | {{CRM_SYSTEM}}, {{SUPPORT_SYSTEM}} |
| **Technical** | Production incidents, performance trends, tech debt metrics | {{OBSERVABILITY_TOOL}}, {{ALERTING_SYSTEM}} |
| **Internal** | Team retrospectives, architecture proposals, process friction | Git PRs, internal wikis |
| **Competitive** | Competitor product launches, pricing changes, market positioning | Market intelligence tools |
| **Financial** | Revenue trends, cost anomalies, margin changes | {{FINANCE_SYSTEM}} |

## Workflow

### Step 1: Signal Capture

Anyone (human or agent) can create a signal:

```bash
# Create a new signal file
cp process/templates/signal.md work/signals/YYYY-MM-DD-<descriptive-name>.md
# Fill in the template
# Submit as a Pull Request
```

**Signal file must include:**
- Source (where did this signal come from?)
- Category (market | customer | technical | internal | competitive | financial)
- Raw data or observation
- Initial assessment of urgency
- Link to source data if available

### Step 2: Signal Triage (Strategy Layer)

Strategy Layer agents and humans review new signals:
- **Group** related signals into clusters
- **Prioritize** based on strategic alignment and urgency
- **Disposition:** proceed to opportunity validation | defer | archive

### Step 3: Opportunity Validation

For signals that proceed:
1. Assess alignment with strategic beliefs
2. Estimate size: small (1 division, < 2 weeks) | medium (2-3 divisions, 2-6 weeks) | large (4+ divisions, 6+ weeks)
3. Identify division involvement
4. Check for conflicts with active missions
5. Draft an opportunity summary

### Step 4: Mission Brief Creation

If the opportunity is validated:
1. Use `templates/mission-brief.md`
2. Define scope (in-scope / out-of-scope)
3. Create outcome contract (`templates/outcome-contract.yaml`)
4. Identify human checkpoint moments
5. Estimate fleet composition
6. Submit as PR for Strategy Layer approval

### Step 5: Mission Approval

- Strategy Layer human reviews mission brief
- Steering Layer consulted for large missions
- Approved mission brief → moves to Build loop
- Rejected mission brief → feedback provided, may be revised or archived

---

## Signal Quality Checklist

A good signal has:
- [ ] Clear source attribution
- [ ] Specific data or observation (not vague feelings)
- [ ] Initial urgency assessment
- [ ] Relevance to at least one strategic belief
- [ ] No duplicate of existing signal

## Anti-Patterns

- ❌ Signals without sources ("I think we should...")
- ❌ Jumping from signal to execution (skipping validation)
- ❌ Mission briefs without outcome contracts
- ❌ Overly broad missions (break them up)
- ❌ Ignoring conflicting signals (capture both)
