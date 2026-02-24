# Missions

Active and completed missions. Each mission gets its own folder.

## How to Create a Mission

1. A signal must be validated through the Discover loop first
2. Use the template: `work/missions/_TEMPLATE-mission-brief.md`
3. Create a folder: `<mission-name>/`
4. Add `BRIEF.md` and `OUTCOME-CONTRACT.md` to the folder
5. Submit as a Pull Request for Strategy Layer approval
6. Once approved, the Orchestrator creates `TASKS.md` (from `_TEMPLATE-tasks.md`) during the `planning` phase — this is **required** before the mission can become `active`

For the full lifecycle and status transition rules, see [docs/mission-lifecycle.md](../../docs/mission-lifecycle.md).

## Mission Structure

```
missions/
└── <mission-name>/
    ├── BRIEF.md                 # Mission brief (from template)
    ├── OUTCOME-CONTRACT.md      # Measurable success criteria
    ├── TASKS.md                 # Decomposed work items (REQUIRED for active status)
    ├── STATUS.md                # Progress updates (append-only, latest first)
    ├── TECHNICAL-DESIGN.md      # Technical design (if design-required: true)
    ├── FLEET-REPORT.md          # Fleet performance report (optional)
    ├── OUTCOME-REPORT.md        # Final outcome measurement (mission closure)
    └── evaluations/             # Quality evaluation reports
        └── YYYY-MM-DD-<eval>.md # Individual quality evaluations
```

> **Important:** A mission cannot transition to `active` without a TASKS.md file containing at least one task. See [docs/mission-lifecycle.md](../../docs/mission-lifecycle.md) for the full lifecycle guide and gate requirements.

## Mission Statuses

| Status | Meaning |
|--------|---------|
| **proposed** | Brief created, awaiting Strategy Layer approval |
| **approved** | Approved by Strategy Layer, ready for orchestration |
| **planning** | Orchestrator creating fleet config and decomposing tasks |
| **active** | TASKS.md exists, execution agents are working |
| **paused** | Temporarily suspended by human decision |
| **completed** | Outcomes measured, mission closed |
| **cancelled** | Terminated before completion, rationale documented in STATUS.md |

---

## Core Missions (Pre-created)

These missions are bootstrapped as universally applicable to any agentic enterprise:

| Mission ID | Name | Folder | Priority |
|------------|------|--------|----------|
| MISSION-2026-001 | [Agentic Enterprise Product Launch](agentic-enterprise-product-launch/) | `agentic-enterprise-product-launch/` | critical |
| MISSION-2026-002 | [Fleet Cost Optimization](fleet-cost-optimization/) | `fleet-cost-optimization/` | high |
| MISSION-2026-003 | [DORA Metrics Excellence](dora-metrics-excellence/) | `dora-metrics-excellence/` | high |
| MISSION-2026-004 | [Automated Security Response](automated-security-response/) | `automated-security-response/` | critical |
| MISSION-2026-005 | [Automated Issue Response](automated-issue-response/) | `automated-issue-response/` | high |
| MISSION-2026-006 | [Support Automation at Scale](support-automation-at-scale/) | `support-automation-at-scale/` | high |
| MISSION-2026-007 | [Data Governance](data-governance/) | `data-governance/` | high |
| MISSION-2026-008 | [Security Posture Hardening](security-posture-hardening/) | `security-posture-hardening/` | critical |
| MISSION-2026-009 | [Compliance Automation](compliance-automation/) | `compliance-automation/` | high |

---

## Example Missions Catalog

The following missions are examples from the Agentic Enterprise Blueprint. They are not pre-created but serve as inspiration for missions your enterprise may choose to activate. Create them using the templates when ready.

| Example Mission | Category | Key Metric Example |
|----------------|----------|-------------------|
| Intelligent Feature Flag Management | Engineering | 78% faster flag lifecycle, 94% stale flag cleanup |
| Developer Experience Foundation | Engineering | 3.2x faster onboarding, 89% self-service resolution |
| Predictive Capacity Planning | Infrastructure | $2.1M annual savings, 99.97% prediction accuracy |
| Cloud Cost Optimization | Infrastructure | 41% cost reduction, 94% resource utilization |
| Infrastructure Cost Optimization | Infrastructure | Cost per transaction optimization |
| AI-Powered Sales Enablement | Sales & GTM | 340% pipeline ROI, 67% win rate improvement |
| Digital Experience Optimization | Product | 23% conversion improvement, 41% engagement increase |
| Automated QBR Generation | Customer Success | 85% preparation reduction, data-driven insights |
| Regulated Growth Expansion | Compliance | Regulatory compliance for market expansion |
| Proactive Issue Prevention | Operations | Predictive incident avoidance |
| Customer Onboarding Automation | Customer Success | Reduced time-to-value for new customers |
| Zero-Downtime Database Migration | Engineering | Seamless data migration with no downtime |
| Multi-Region Expansion | Infrastructure | Geographic redundancy and performance |
| Cloud Native Migration | Infrastructure | Modernization from legacy to cloud-native |
| API Modernization | Engineering | Modern API layer for legacy systems |
| Knowledge Base Automation | Knowledge | AI-maintained internal knowledge systems |
