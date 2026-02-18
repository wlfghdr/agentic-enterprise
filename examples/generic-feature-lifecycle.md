# Example: Generic Feature Lifecycle

> **Purpose:** Walkthrough of a feature from initial signal through production deployment, showing how all layers and loops interact.

---

## Phase 1: Signal (Discover Loop)

A customer success agent detects a pattern: 15 enterprise customers have requested a bulk data export feature in the last quarter. The agent creates a signal:

**File created:** `work/signals/2026-03-15-bulk-export-customer-demand.md`

```markdown
# Signal: Bulk Data Export — Recurring Customer Demand

## Source
- Category: customer
- Source system: CRM + Support ticket analysis
- Confidence: high

## Observation
15 enterprise customers (representing $2.4M ARR) have requested bulk data export 
functionality in Q1 2026. 8 of these are in renewal discussions.

## Initial Assessment
- Urgency: next-cycle
- Strategic alignment: "Customer success drives growth"
- Potential impact: high (retention risk)
- Affected divisions: Core API, Data Services, Customer Success
```

---

## Phase 2: Opportunity Validation (Discover Loop)

The Strategy Layer reviews the signal:

1. **Strategic fit check:** Aligns with "customer success drives growth" belief
2. **Size estimate:** Medium (2-3 divisions, ~4 weeks)
3. **Division scoping:** Core API (primary), Data Services (supporting)
4. **Conflict check:** No conflicts with active missions

Decision: Proceed to mission brief.

---

## Phase 3: Mission Brief (Discover → Build Handoff)

**File created:** `work/missions/bulk-data-export/BRIEF.md`

Key elements:
- **Objective:** Enable enterprise customers to export data in bulk (CSV, JSON, Parquet) via API and UI
- **Scope:** API endpoint + UI button + documentation
- **Out of scope:** Real-time streaming export, custom formats
- **Outcome contract:** API available within 4 weeks, export latency < 30s for 1M records, 3 enterprise customers using it within 2 weeks of launch

**Approval:** Strategy Layer human reviews and approves ✅

---

## Phase 4: Fleet Configuration (Build Loop — Orchestration)

The Orchestration Layer decomposes the mission:

**File created:** `org/2-orchestration/fleet-configs/bulk-data-export.md`

```yaml
mission:
  id: "MISSION-2026-015"
  
streams:
  - name: "api-implementation"
    division: "Core API"
    quality_policies: ["security", "architecture", "performance"]
    
  - name: "ui-integration"
    division: "Frontend"
    quality_policies: ["architecture", "experience"]
    
  - name: "documentation"
    division: "Documentation"
    quality_policies: ["content"]

dependencies:
  - from: "ui-integration"
    to: "api-implementation"
    type: "blocks"
```

---

## Phase 5: Execution (Build Loop)

### Stream 1: API Implementation
- Execution Layer agent reads quality policies (security, architecture, performance)
- Writes API endpoint: `POST /api/v2/export/bulk`
- Writes unit tests (92% coverage)
- Writes integration tests
- Self-evaluates against policies
- Submits PR

### Stream 2: UI Integration (starts after API is merged)
- Agent reads experience policy
- Implements "Export" button using design system components
- Implements progress indicator for long-running exports
- Writes e2e tests
- Self-evaluates
- Submits PR

### Stream 3: Documentation (in parallel)
- Agent drafts API reference (reference type)
- Agent drafts "How to export data" (how-to type)
- Self-evaluates against content policy
- Submits PR

---

## Phase 6: Quality Evaluation (Build Loop)

Quality Layer eval agents review each PR:

| Stream | Verdict | Notes |
|--------|---------|-------|
| API | PASS WITH NOTES | Suggestion: add rate limiting |
| UI | PASS | All criteria met |
| Documentation | FAIL | Code examples not tested |

Documentation agent iterates → fixes code examples → resubmits → PASS ✅

Architecture decision recorded: `work/decisions/2026-03-25-bulk-export-api-design.md`

---

## Phase 7: Release (Ship Loop)

**File created:** Release contract using `work/releases/_TEMPLATE-release-contract.md`

```
Progressive rollout:
  Stage 1: Internal canary (5%) — 24 hours
  Stage 2: Early adopter customers (25%) — 48 hours  
  Stage 3: General availability (100%)

Rollback trigger: Error rate > 2% above baseline
```

Human approves release contract ✅

---

## Phase 8: Deployment (Ship Loop)

1. **Canary (5%):** 24 hours — error rate 0.1%, latency p95 = 280ms ✅
2. **Early adopters (25%):** 48 hours — 3 customers using export, positive feedback ✅
3. **GA (100%):** Feature flag enabled for all customers ✅

---

## Phase 9: Outcome Measurement (Ship Loop)

After 2 weeks:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| API available | 4 weeks | 3.5 weeks | ✅ Met |
| Export latency (1M records) | < 30s | 22s | ✅ Met |
| Enterprise customers using | 3 within 2 weeks | 5 | ✅ Exceeded |

---

## Phase 10: Feedback (Ship → Discover)

New signals generated from production:
1. `work/signals/2026-04-15-bulk-export-large-dataset-timeout.md` — Exports > 10M records timeout → future mission
2. `work/signals/2026-04-18-bulk-export-scheduled-request.md` — Customers want scheduled recurring exports → feature request

The cycle continues. 🔄

---

## Key Takeaways

This example demonstrates:
- **Signal → Mission flow:** Customer demand validated and scoped
- **Layer interaction:** Strategy approved, Orchestration decomposed, Execution produced, Quality evaluated
- **Loop interaction:** Discover → Build → Ship → new Discover signals
- **Human checkpoints:** Mission approval, release approval
- **Quality gates:** Eval agents catch issues before production
- **Progressive delivery:** Incremental rollout with health monitoring
- **Outcome measurement:** Success criteria tracked against actuals
