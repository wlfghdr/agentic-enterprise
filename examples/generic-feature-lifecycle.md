# Example: Generic Feature Lifecycle

> **Purpose:** Complete walkthrough of a feature from initial signal through production operation, showing how all 5 layers, all 4 loops, specific agent types, and every major artifact interact.
>
> **Scenario:** Enterprise customers are requesting a bulk data export capability. This is a representative example — any B2B software company will recognize the pattern: customer demand → validation → build → ship → operate.

---

## Artifact Chain (Overview)

```
Signal → Signal Digest → Mission Brief + Outcome Contract → Fleet Config + STATUS.md
→ Technical Design (for design-required missions)
→ Execution Outputs + Asset Registry → Quality Evaluation Reports → Decision Records
→ Release Contract → Production → Outcome Report + Venture Health Update
→ New Signals (cycle continues)
```

Each arrow represents a **Git PR** with **CODEOWNERS-enforced approval**. The Git history is the audit trail.

---

## Phase 1: Signal Detection

**Layer:** Execution · **Loop:** Operate · **Agent type:** `customer-signal-scanner`

A `customer-signal-scanner` agent runs continuously, analyzing support tickets, CRM data, and customer success notes. It detects a recurring pattern: 15 enterprise customers (representing $2.4M ARR) have requested bulk data export functionality in Q1 2026. Eight of these customers are in active renewal discussions.

The agent creates a signal via PR:

**Artifact created:** `work/signals/2026-03-15-bulk-export-customer-demand.md`  
**Template:** `work/signals/_TEMPLATE-signal.md`  
**Branch:** `signal/2026-03-15-bulk-export-customer-demand`

```markdown
# Signal: Bulk Data Export — Recurring Customer Demand

## Source
- Category: customer
- Source system: CRM + Support ticket analysis
- Confidence: high

## Observation
15 enterprise customers (representing $2.4M ARR) have requested bulk data export 
functionality in Q1 2026. 8 of these are in renewal discussions. Export formats 
requested: CSV (12), JSON (9), Parquet (4). Largest requested dataset: ~50M records.

## Initial Assessment
- Urgency: next-cycle
- Strategic alignment: "Customer success drives growth"
- Potential impact: high (retention risk on $2.4M ARR)
- Affected divisions: Core Services, Data Foundation, Customer Experience

## Recommended Disposition
- [x] Proceed to opportunity validation
```

**Handover:** The PR is auto-merged (signals don't require approval — they are observations, not decisions). The signal is now visible to the Steering Layer's aggregation process.

> **Agent behavior note:** The `customer-signal-scanner` also files an **improvement signal** during this work: it noticed that CRM tags for "export" and "data download" are inconsistent, causing it to almost miss 3 related tickets. It files `work/signals/2026-03-15-crm-tagging-inconsistency.md` as an internal/process signal.

---

## Phase 2: Signal Aggregation & Digest

**Layer:** Steering · **Loop:** Continuous Sensing · **Agent type:** `signal-aggregation`

At the end of the week, the `signal-aggregation` agent compiles all signals from the period into a digest. It identifies that the bulk export signal converges with two other related signals:
- A `competitive-intelligence` agent flagged that two competitors launched bulk export features in the past quarter
- An `infrastructure-capacity-planning` agent noted increasing API usage patterns consistent with customers building workaround export scripts

**Artifact created:** `work/signals/digests/2026-W12-digest.md`  
**Template:** `work/signals/digests/_TEMPLATE-signal-digest.md`

```markdown
# Signal Digest: Week 2026-W12

## Summary
Total signals this period: 14
New signals: 9
Signals by disposition: proceed: 3 | defer: 2 | monitor: 4 | pending triage: 5

## Signals by Theme

### Theme: Data Export Capability Gap
Signal count: 3 | Trend: rising | Urgency: high

| Signal | Date | Category | Source |
|--------|------|----------|--------|
| Bulk Export — Customer Demand | 2026-03-15 | customer | customer-signal-scanner |
| Competitor Export Feature Launch | 2026-03-13 | competitive | competitive-intelligence |
| Workaround API Usage Spike | 2026-03-14 | technical | infrastructure-capacity-planning |

Pattern observation: Three independent signals from different sources all point to
an unmet bulk data export need. Customer demand is quantified ($2.4M ARR at risk),
competitive pressure is confirmed, and customers are already building workarounds.

Recommended action: Escalate to Strategy Layer for opportunity validation.
Urgency: high — 8 customers in renewal discussions.

## Pattern Alerts

### Pattern Alert: Data Export Convergence
- Signals involved: 3
- First signal: 2026-03-13
- Latest signal: 2026-03-15
- Pattern description: Customer demand, competitive pressure, and workaround behavior
  all converge on the same capability gap.
- Recommended action: Create mission brief
- Urgency: high
```

**Handover:** The digest is committed to `main` via PR. The Strategy Layer's `discovery-agent` monitors the digests directory for new entries and picks up the pattern alert.

---

## Phase 3: Opportunity Validation

**Layer:** Strategy · **Loop:** Discover · **Agent type:** `discovery-agent`

The `discovery-agent` reads the digest, follows the pattern alert, and performs opportunity validation following the Discover Loop guide:

1. **Strategic fit check:** Aligns with strategic belief "Customer success drives growth." Also supports "Platform extensibility" (export is a form of data portability).
2. **Size estimate:** Medium (3 divisions, ~4 weeks). Crosses API, data processing, and frontend boundaries.
3. **Division scoping:** Core Services (primary — API), Data Foundation (supporting — processing engine), Customer Experience (supporting — UI + docs).
4. **Conflict check:** No active missions in the same file paths. No blocking dependencies.
5. **Resource check:** Core Services division has capacity (current mission completing this week).

The agent prepares a recommendation memo and flags it for human review.

**Human checkpoint:** The Strategy Owner (e.g., VP Product) reviews the opportunity validation. They confirm the strategic priority given the renewal risk and approve proceeding to mission brief.

**Escalation note:** If the Strategy Owner had concerns (e.g., "We're considering a partnership instead of building this"), they would comment on the PR with questions. The `discovery-agent` would incorporate the feedback and re-submit. This is a **Tier 2 escalation** — strategic judgment that requires human input.

---

## Phase 4: Mission Brief + Outcome Contract

**Layer:** Strategy · **Loop:** Discover · **Agent types:** `product-strategy`

The `product-strategy` agent drafts two separate artifacts — the Mission Brief and the Outcome Contract. These are created as separate files because they serve different audiences: the brief is for everyone involved, the contract is for measurement.

### 4a. Mission Brief

**Artifact created:** `work/missions/bulk-data-export/BRIEF.md`  
**Template:** `work/missions/_TEMPLATE-mission-brief.md`

```markdown
# Mission Brief: Bulk Data Export

## Mission ID: MISSION-2026-015
## Status: proposed

## Origin
- Signal(s): work/signals/2026-03-15-bulk-export-customer-demand.md (+ 2 related)
- Signal digest: work/signals/digests/2026-W12-digest.md (Pattern Alert: Data Export Convergence)
- Strategic alignment: "Customer success drives growth", "Platform extensibility"
- Sponsor: VP Product

## Objective
Enable enterprise customers to export their data in bulk (CSV, JSON, Parquet) 
via API and UI. Addresses a quantified retention risk ($2.4M ARR across 8 customers
in renewal) and closes a competitive gap.

## Scope

### In Scope
- REST API endpoint for bulk export (async job-based)
- UI export button with progress tracking
- Support for CSV, JSON, and Parquet formats
- Export up to 10M records per job
- API reference documentation
- How-to guide for customers

### Out of Scope
- Real-time streaming export
- Custom/pluggable export formats
- Exports > 10M records (deferred — tracked as separate signal)
- Scheduled/recurring exports (deferred)

### Constraints
- Must not degrade existing API latency (p99 < 200ms baseline)
- Must use existing authentication/authorization model
- 4-week delivery target (renewals in 6 weeks)

## Divisions Involved

| Division | Role | Contribution |
|----------|------|-------------|
| Core Services | Primary | API endpoint, export engine, job queue |
| Data Foundation | Supporting | Data extraction pipeline, format converters |
| Customer Experience | Supporting | UI integration, documentation |

## Human Checkpoints
1. Mission approval — VP Product reviews brief → approves via PR merge
2. Architecture decision — if async pattern introduces novel architecture, Tech Lead reviews
3. Release approval — Engineering Manager approves release contract

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Export jobs overload database | medium | high | Dedicated read replica + rate limiting |
| Parquet format complexity | low | medium | Use proven library; fallback to CSV |
| 4-week timeline tight | medium | medium | Parallelize streams; documentation starts Day 1 |

## Estimated Effort
- Size: medium (2-4 weeks)
- Agent fleet size: 3 concurrent streams
- Human touchpoints: 3 (mission approval, architecture review, release approval)
```

### 4b. Outcome Contract

**Artifact created:** `work/missions/bulk-data-export/OUTCOME-CONTRACT.md`  
**Template:** `work/missions/_TEMPLATE-outcome-contract.md`

```markdown
# Outcome Contract: Bulk Data Export

## Mission
| Field | Value |
|-------|-------|
| Mission ID | MISSION-2026-015 |
| Mission brief | work/missions/bulk-data-export/BRIEF.md |

## Outcomes

### Outcome 1: API Availability
| Field | Value |
|-------|-------|
| Metric | Bulk export API endpoint available in production |
| Baseline | No bulk export capability exists |
| Target | Fully functional, GA-released |
| Measurement method | API responds to authenticated export requests |
| Deadline | 2026-04-12 |

### Outcome 2: Export Performance
| Field | Value |
|-------|-------|
| Metric | p95 export latency for 1M records |
| Baseline | N/A (new feature) |
| Target | < 30 seconds |
| Measurement method | APM tracing on export job completion |
| Deadline | 2026-04-12 |

### Outcome 3: Customer Adoption
| Field | Value |
|-------|-------|
| Metric | Enterprise customers actively using bulk export |
| Baseline | 0 |
| Target | ≥ 3 within 2 weeks of GA |
| Measurement method | Distinct customer IDs calling export endpoint |
| Deadline | 2026-04-26 |

### Outcome 4: Guardrail — API Latency
| Field | Value |
|-------|-------|
| Metric | Existing API p99 latency |
| Baseline | 180ms |
| Target | Must remain < 200ms |
| Measurement method | APM monitoring, continuous |
| Deadline | Ongoing |

## Acceptance Criteria
- [ ] All three export formats (CSV, JSON, Parquet) functional
- [ ] Export jobs cancelable by the initiating user
- [ ] Rate limiting enforced (max 5 concurrent exports per customer)
- [ ] API documentation published and reviewed

## Measurement Schedule
| Checkpoint | Timing |
|------------|--------|
| Initial check | 1 week post-GA |
| Follow-up | 2 weeks post-GA (adoption target measured) |
| Final evaluation | 4 weeks post-GA |
```

**Handover:** Both artifacts are submitted in a single PR on branch `mission/bulk-data-export/brief`. CODEOWNERS requires Strategy Layer human (VP Product) approval. The VP reviews, asks one clarifying question about the 10M record limit rationale, the `product-strategy` agent adds a note, and the VP approves via PR merge. ✅

**Status change:** Mission moves from `proposed` → `approved`.

---

## Phase 5: Fleet Configuration

**Layer:** Orchestration · **Loop:** Build · **Agent type:** `mission-orchestrator`

The `mission-orchestrator` agent reads the approved Mission Brief and decomposes the mission into executable streams. It creates two artifacts: the Fleet Configuration and the initial Mission Status entry.

### 5a. Fleet Configuration

**Artifact created:** `org/2-orchestration/fleet-configs/bulk-data-export.md`  
**Template:** `org/2-orchestration/fleet-configs/_TEMPLATE-fleet-config.md`

```markdown
# Fleet Configuration: Bulk Data Export

## Mission
| Field | Value |
|-------|-------|
| Mission ID | MISSION-2026-015 |
| Mission brief | work/missions/bulk-data-export/BRIEF.md |
| Status | active |

## Streams

### Stream: api-implementation
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Core Services |
| Exclusive | yes |

Working paths:
- src/api/v2/export/
- src/services/export/
- tests/api/v2/export/
- tests/services/export/

Quality policies:
- security
- architecture
- performance
- observability

Human checkpoints:
| Trigger | Who | Action |
|---------|-----|--------|
| Architecture novelty score > 0.7 | Tech Lead | Review async job pattern |
| Security-sensitive: file I/O + auth | Security Lead | Review export auth model |

### Stream: data-processing
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Data Foundation |
| Exclusive | yes |

Working paths:
- src/data/export/
- tests/data/export/

Quality policies:
- architecture
- performance

### Stream: ui-integration
| Field | Value |
|-------|-------|
| Agent pool | coding-agent-fleet |
| Division | Customer Experience |
| Exclusive | yes |

Working paths:
- src/ui/components/export/
- tests/ui/export/

Quality policies:
- architecture
- experience

### Stream: documentation
| Field | Value |
|-------|-------|
| Agent pool | doc-generation-agent |
| Division | Customer Experience |
| Exclusive | yes |

Working paths:
- docs/api/v2/export/
- docs/guides/bulk-export/

Quality policies:
- content

## Dependencies
| From | To | Type |
|------|----|------|
| ui-integration | api-implementation | blocks |
| data-processing | api-implementation | informs (shared interface contract) |
| documentation | api-implementation | informs (API spec needed) |

## Monitoring
| Parameter | Value |
|-----------|-------|
| Quality threshold | 0.85 |
| Throughput alert | < 1 PR/day per active stream |
| Escalation policy | Engineering Manager |
```

### 5b. Initial Mission Status

**Artifact created:** `work/missions/bulk-data-export/STATUS.md`  
**Template:** `work/missions/_TEMPLATE-mission-status.md`

```markdown
# Mission Status: Bulk Data Export

## Status Update: 2026-03-17

Overall status: on-track
Mission phase: active
Reporting period: 2026-03-17 → 2026-03-17

### Stream Progress
| Stream | Division | Status | Progress | Notes |
|--------|----------|--------|----------|-------|
| api-implementation | Core Services | active | Starting | Agent fleet spun up, branch created |
| data-processing | Data Foundation | active | Starting | Parallel with API stream |
| ui-integration | Customer Experience | blocked | Waiting | Depends on API stream interface |
| documentation | Customer Experience | active | Starting | API spec draft in progress |

### Next Milestones
| Milestone | Target Date | Status |
|-----------|------------|--------|
| API interface contract defined | 2026-03-21 | on-track |
| API endpoint functional | 2026-03-28 | on-track |
| UI integration complete | 2026-04-04 | on-track |
| Documentation complete | 2026-04-04 | on-track |
| Release contract submitted | 2026-04-07 | on-track |
```

**Handover:** Fleet config submitted via PR on branch `orchestration/bulk-data-export/fleet-config`. CODEOWNERS requires Orchestration Layer approval. The Mission Lead reviews and merges. Because this is a multi-stream mission (4 streams with dependencies), the mission is marked `design-required: true` — so a Technical Design step is triggered before stream execution begins.

---

## Phase 6: Technical Design

**Layer:** Execution · **Loop:** Build · **Agent type:** `technical-design-agent`

The Mission Brief is flagged `design-required: true` (multi-stream mission with inter-stream dependencies). The Orchestration Layer triggers the `technical-design-agent` before dispatching execution streams.

### 6a. Technical Design Document

**Artifact created:** `work/missions/bulk-data-export/TECHNICAL-DESIGN.md`  
**Template:** `work/missions/_TEMPLATE-technical-design.md`

The `technical-design-agent`:
1. Reads the Mission Brief, Outcome Contract, and Fleet Config
2. Identifies 3 inter-stream dependencies that need explicit interface contracts
3. Produces the Technical Design document:

```markdown
# Technical Design: Bulk Data Export

## Metadata
| Field | Value |
|-------|-------|
| Mission ID | MISSION-2026-015 |
| Status | in-review |
| Author | technical-design-agent |
| Reviewers | Tech Lead (Core Services), Architecture Governor |

## Context & Goals
Bulk Data Export allows customers to extract large datasets (up to 10M records)
in CSV, JSON, and Parquet formats. The design must handle async processing
(exports can take minutes), rate limiting, and secure file delivery — all within
the existing async job framework.

## API Contracts

### Export API (REST — OpenAPI 3.x fragment)
POST /api/v2/export/bulk → 202 Accepted (creates async export job)
  Request: { datasetId, format: "csv"|"json"|"parquet", filters?, columns? }
  Response: { jobId, status: "queued", estimatedDuration, _links: { status, cancel } }

GET /api/v2/export/bulk/{jobId} → 200 (job status)
  Response: { jobId, status: "queued"|"processing"|"completed"|"failed"|"cancelled",
              progress: 0-100, format, recordCount, fileSize?, downloadUrl?, error? }

GET /api/v2/export/bulk/{jobId}/download → 200 (signed file download)
  Response: binary stream (Content-Disposition: attachment)
  Auth: signed URL with 15-minute TTL

DELETE /api/v2/export/bulk/{jobId} → 204 (cancel in-progress export)

## Data Model

| Entity | Change | Fields |
|--------|--------|--------|
| ExportJob | new | id, customerId, datasetId, format, status, filters, columns, progress, fileUrl, createdAt, completedAt, errorMessage |
| ExportQuota | new | customerId, concurrentLimit (default: 5), dailyLimit |

## Interface Contracts Between Streams

| From Stream | To Stream | Interface | Contract |
|-------------|-----------|-----------|----------|
| data-processing | api-implementation | Shared types | ExportFormat enum, ExportJobStatus enum, ChunkResult type |
| api-implementation | ui-integration | API spec | Full OpenAPI spec above — UI polls GET /status, triggers download |
| api-implementation | documentation | API spec | Same OpenAPI spec — doc agent uses for reference docs |

### Shared Type Definitions
type ExportFormat = "csv" | "json" | "parquet"
type ExportJobStatus = "queued" | "processing" | "completed" | "failed" | "cancelled"
interface ChunkResult { recordCount: number; byteSize: number; chunkIndex: number }

## Behavioral Specifications

Scenario: Customer creates an export job
  Given a customer with available export quota
  When they POST /api/v2/export/bulk with valid parameters
  Then a job is created with status "queued"
  And the response includes a status polling URL

Scenario: Rate limiting enforced
  Given a customer already has 5 concurrent exports running
  When they POST /api/v2/export/bulk
  Then they receive 429 Too Many Requests
  And the response includes Retry-After header

Scenario: Export job completes successfully
  Given an export job in "processing" status
  When all data chunks are processed
  Then job status changes to "completed"
  And a signed download URL is generated with 15-min TTL

Scenario: Export cancellation
  Given an export job in "queued" or "processing" status
  When the customer sends DELETE /api/v2/export/bulk/{jobId}
  Then the job transitions to "cancelled"
  And any partial files are cleaned up

## Security Threat Model

| Threat | Category | Likelihood | Impact | Mitigation |
|--------|----------|------------|--------|------------|
| Unauthorized access to other customer's exports | Elevation of Privilege | med | high | Tenant isolation on all queries; jobId includes customerId hash |
| Download URL guessing | Information Disclosure | low | high | Signed URLs with 15-min TTL, 256-bit random tokens |
| Resource exhaustion via large exports | Denial of Service | med | med | Per-customer concurrency limit (5), daily limit, file size cap (5GB) |

## Performance Budgets

| Component | Metric | Budget |
|-----------|--------|--------|
| POST /export/bulk | p95 latency | < 200ms (job creation only) |
| GET /export/bulk/{id} | p95 latency | < 50ms (status lookup) |
| Data processing | throughput | 1M records in < 5 min |
| File download | throughput | 100 MB/s minimum |

## Architecture Decisions

Decision 1: Use existing async job framework (not a new queue)
  Context: Could build custom export queue or reuse existing framework
  Decision: Reuse existing async job framework
  Rationale: Proven at scale, already monitored, avoids new infrastructure
  ADR: inline — standard pattern

## Open Questions
(none — all resolved during design review)
```

### 6b. Design Review

**PR submitted:** `exec/bulk-data-export/technical-design → main`

The Architecture Governor and Core Services Tech Lead review the Technical Design:
- API contracts are consistent with existing API conventions ✅
- Shared type definitions are clear for cross-stream consumption ✅
- Security mitigations are proportionate to threats ✅
- Performance budgets are measurable and testable ✅
- All fleet config dependencies have explicit interface contracts ✅

**PR approved and merged.** Mission status updated: Technical Design approved. Execution streams can now begin with a shared, reviewed specification.

> **Key benefit:** The UI stream (previously "blocked" waiting for the API spec to emerge from implementation) now has the full API contract from the Technical Design. All 4 streams can reference the same authoritative spec, reducing integration rework.

---

## Phase 7: Execution — Parallel Streams

**Layer:** Execution · **Loop:** Build · **Agent types:** `coding-agent` (×3 streams), `doc-generation-agent`

Each stream operates on its own branch with exclusive folder ownership. Agents follow the concurrency rules: one branch per agent, no overlapping file paths, pessimistic locking on shared resources. **All streams reference the approved Technical Design** as the authoritative specification for API contracts, data models, shared types, and behavioral expectations.

### Stream 1: API Implementation

**Agent type:** `coding-agent` (from `coding-agent-fleet` pool)  
**Branch:** `exec/bulk-data-export/api-implementation`

The agent:
1. Reads the Mission Brief, Fleet Config, and **Technical Design** to understand its scope
2. Reads applicable quality policies: `security.md`, `architecture.md`, `performance.md`, `observability.md`
3. Implements `POST /api/v2/export/bulk` — matching the API contract from the Technical Design
4. Implements `GET /api/v2/export/bulk/{jobId}` — status polling endpoint
5. Implements `GET /api/v2/export/bulk/{jobId}/download` — file download endpoint
6. Implements the job queue processor using the existing async job framework
7. Adds rate limiting: max 5 concurrent exports per customer
8. Writes unit tests (94% coverage) and integration tests
9. Adds OpenTelemetry instrumentation (traces, metrics, structured logs with trace IDs)
10. **Self-evaluates** against each applicable policy before submitting:
    - Security: auth checks on all endpoints ✅, input validation ✅, no credential exposure ✅
    - Architecture: follows existing patterns ✅, uses established job queue ✅
    - Performance: async processing ✅, rate limiting ✅, tested at 1M records ✅
    - Observability: traces ✅, metrics ✅, structured logs ✅, health check ✅

**PR submitted:** `exec/bulk-data-export/api-implementation → main`

### Stream 2: Data Processing

**Agent type:** `coding-agent`  
**Branch:** `exec/bulk-data-export/data-processing`

The agent:
1. Implements format converters: CSV, JSON, Parquet
2. Implements chunked data extraction (avoids loading full dataset into memory)
3. Implements the read-replica query routing (mitigates database load risk)
4. Writes unit tests for each format converter
5. Self-evaluates against architecture and performance policies

**PR submitted:** `exec/bulk-data-export/data-processing → main`

### Stream 3: UI Integration

**Agent type:** `coding-agent`  
**Branch:** `exec/bulk-data-export/ui-integration`

This stream was previously **blocked** waiting for the API interface contract \u2014 but with the Technical Design approved, the full API spec is already available. The UI stream can start in parallel:

1. Reads the API contract from the Technical Design (endpoints, request/response shapes, shared types)
2. Implements "Export Data" button using the design system
2. Implements progress indicator polling the job status endpoint
3. Implements download trigger when export completes
4. Writes end-to-end tests
5. Self-evaluates against architecture and experience policies

**PR submitted:** `exec/bulk-data-export/ui-integration → main`

### Stream 4: Documentation

**Agent type:** `doc-generation-agent`  
**Branch:** `exec/bulk-data-export/documentation`

Starts in parallel (informed by the API spec, but not blocked):

1. Drafts API reference documentation (reference type per content policy)
2. Drafts "How to Export Data in Bulk" guide (how-to type per content policy)
3. Includes tested code examples in 3 languages (Python, JavaScript, curl)
4. Self-evaluates against content policy: structure ✅, tone ✅, code examples tested ✅

**PR submitted:** `exec/bulk-data-export/documentation → main`

> **Improvement signal:** During execution, the `coding-agent` working on stream 1 notices that the existing async job framework lacks a standard cancellation pattern. It files `work/signals/2026-03-20-async-job-cancellation-pattern-missing.md` as a technical signal with urgency "monitor."

---

## Phase 8: Quality Evaluation

**Layer:** Quality · **Loop:** Build · **Agent types:** `architecture-review`, `security-policy-enforcer`, `performance-evaluator`, `experience-evaluator`, `brand-content-policy`

Each PR triggers quality evaluation by the relevant eval agents (determined by the quality policies listed in the fleet config). Each evaluation produces a structured Quality Evaluation Report.

### Stream 1 (API) Evaluation

**Evaluated by:** `architecture-review`, `security-policy-enforcer`, `performance-evaluator`

**Artifact created:** `work/missions/bulk-data-export/evaluations/2026-03-25-api-implementation.md`  
**Template:** `work/missions/_TEMPLATE-quality-evaluation-report.md`

```markdown
# Quality Evaluation Report: Bulk Export API Implementation

## Policies Evaluated
| Policy | Applicable | Verdict | Notes |
|--------|-----------|---------|-------|
| security.md | yes | PASS | Auth model verified, input validation present |
| architecture.md | yes | PASS WITH NOTES | Follows established patterns; see advisory below |
| performance.md | yes | PASS | Async processing, rate limiting, tested at scale |
| observability.md | yes | PASS | Full instrumentation verified |

## Findings

### Major Findings
(none)

### Minor Findings (Advisory)
1. Finding: Rate limiting returns HTTP 429 but response body lacks Retry-After header
   Policy: architecture.md — "API responses must include actionable error information"
   Severity: minor
   Recommendation: Add Retry-After header with queue position estimate

## Overall Verdict: PASS WITH NOTES
Blocking issues: 0 critical, 0 major
Advisory notes: 1 minor finding
```

### Stream 2 (Data Processing) Evaluation

**Evaluated by:** `architecture-review`, `performance-evaluator`

**Verdict: PASS** — Clean implementation, good chunking strategy, read-replica routing verified.

### Stream 3 (UI) Evaluation

**Evaluated by:** `architecture-review`, `experience-evaluator`

**Verdict: PASS** — Design system components used correctly, progress indicator tested with slow connections, accessible.

### Stream 4 (Documentation) Evaluation

**Evaluated by:** `brand-content-policy`

**Verdict: FAIL**

```markdown
## Critical Findings (Blocking)
1. Finding: Python code example uses deprecated authentication method (API key in URL)
   Policy: content.md — "Code examples must use current, secure authentication patterns"
   Severity: critical
   Evidence: docs/guides/bulk-export/index.md line 45
   Remediation: Update to use Bearer token in Authorization header
```

**Iteration:** The `doc-generation-agent` reads the FAIL verdict, fixes the code examples to use Bearer token authentication, re-runs the examples to verify they work, and resubmits the PR. The `brand-content-policy` agent re-evaluates → **PASS** ✅

### Escalation Example

During the API evaluation, the `architecture-review` agent encounters a novel pattern: the export job uses a new fan-out approach for Parquet generation that doesn't match any established architecture pattern. The agent issues an **ESCALATE** verdict on this specific aspect:

```markdown
## Escalation
- Finding: Parquet export uses fan-out worker pattern not seen in existing codebase
- Policy: architecture.md — "Novel architectural patterns require human review"
- Verdict: ESCALATE — cannot determine if this pattern is appropriate
- Recommendation: Tech Lead should review the fan-out approach
```

**Human checkpoint (Tier 2):** The Tech Lead reviews the fan-out pattern, determines it's appropriate for this use case, and comments on the PR with approval and a note to document this as a reusable pattern. The `architecture-review` agent updates the verdict to **PASS**.

---

## Phase 9: Decision Record

**Layer:** Cross-layer · **Agent type:** `coding-agent` (authored), `architecture-review` (validated)

During execution, the API stream faced a design choice: synchronous export (simple but blocks on large datasets) vs. asynchronous job queue (more complex but scalable). The decision was made during implementation but is now formally recorded.

**Artifact created:** `work/decisions/2026-03-25-bulk-export-async-pattern.md`  
**Template:** `work/decisions/_TEMPLATE-decision-record.md`

```markdown
# Decision Record: Async Job Queue for Bulk Export

## Decision ID: DR-2026-012
## Status: accepted

## Context
Bulk export needs to handle datasets up to 10M records. Synchronous processing 
would block HTTP connections for minutes, risking timeouts and poor UX. The system 
needs to handle multiple concurrent exports without degrading the main API.

## Decision
Use the existing async job queue framework. Export requests create a job, return 
immediately with a job ID, and clients poll for completion. Completed exports are 
stored as temporary files with a 24-hour TTL.

## Alternatives Considered

### Alternative 1: Synchronous Streaming
- Pros: Simpler implementation, no job management
- Cons: HTTP timeout risk, no progress tracking, blocks connection pool
- Why rejected: Cannot reliably handle 10M records within HTTP timeout windows

### Alternative 2: WebSocket-based Streaming  
- Pros: Real-time progress, no polling
- Cons: Requires WebSocket infrastructure not yet in place, client complexity
- Why rejected: Infrastructure investment disproportionate to immediate need

## Consequences
### Positive
- Scalable to large datasets without HTTP timeouts
- Progress tracking built-in via job status
- Reuses existing job queue (no new infrastructure)

### Negative
- Clients must implement polling logic
- Temporary file storage requires cleanup management

## Review Schedule
Review when streaming export is considered (currently out of scope).
```

---

## Phase 10: Mission Status Update & Fleet Performance

**Layer:** Orchestration · **Loop:** Build · **Agent types:** `fleet-performance-monitor`

Midway through the mission, the `fleet-performance-monitor` agent produces an updated status entry and a fleet performance snapshot.

### 10a. Status Update (appended to STATUS.md)

```markdown
## Status Update: 2026-03-28

Overall status: on-track
Mission phase: active
Reporting period: 2026-03-17 → 2026-03-28

### Stream Progress
| Stream | Division | Status | Progress | Notes |
|--------|----------|--------|----------|-------|
| api-implementation | Core Services | active | 80% | PR submitted, in quality eval |
| data-processing | Data Foundation | completed | 100% | PR merged ✅ |
| ui-integration | Customer Experience | active | 40% | Unblocked, implementation underway |
| documentation | Customer Experience | active | 70% | Reworking code examples after FAIL |

### Key Decisions Made This Period
| Decision | Date | Decided By | Link |
|----------|------|-----------|------|
| Async job queue pattern | 2026-03-25 | Tech Lead + coding-agent | work/decisions/2026-03-25-bulk-export-async-pattern.md |

### Fleet Performance (This Period)
| Metric | Value |
|--------|-------|
| PRs generated | 6 |
| PRs merged | 3 |
| PRs rejected / needs-revision | 1 (documentation — code examples) |
| Quality eval pass rate | 83% (5/6) |
| Average cycle time (PR open → merge) | 18 hours |
```

### 10b. Fleet Performance Report

**Artifact created:** `work/missions/bulk-data-export/FLEET-REPORT.md`  
**Template:** `work/missions/_TEMPLATE-fleet-performance-report.md`

The `fleet-performance-monitor` also notes a **bottleneck**: quality evaluation turnaround on the API PR took 14 hours due to the ESCALATE verdict requiring human involvement. It recommends pre-flagging PRs with novel architectural patterns so human reviewers can be alerted earlier.

---

## Phase 11: Release Contract

**Layer:** Orchestration → Quality · **Loop:** Ship · **Agent type:** `release-coordinator`

With all streams merged and quality evaluations passed, the `release-coordinator` agent drafts the release contract.

**Artifact created:** `work/releases/2026-04-07-bulk-data-export.md`  
**Template:** `work/releases/_TEMPLATE-release-contract.md`

```markdown
# Release Contract: Bulk Data Export v1.0

## Release ID: REL-2026-008
## Status: draft

## Changes Included
| Change | Type | Mission | Quality Verdict |
|--------|------|---------|----------------|
| POST /api/v2/export/bulk | feature | MISSION-2026-015 | PASS |
| Export format converters (CSV, JSON, Parquet) | feature | MISSION-2026-015 | PASS |
| UI Export button + progress indicator | feature | MISSION-2026-015 | PASS |
| API docs + how-to guide | documentation | MISSION-2026-015 | PASS |

## Breaking Changes
- [x] No breaking changes in this release

## Progressive Rollout Plan
| Stage | Target | Duration | Health Criteria | Rollback Trigger |
|-------|--------|----------|-----------------|-----------------|
| Canary | 5% | 24 hours | Error rate < baseline + 0.5% | Auto-rollback on critical alert |
| Early Adopters | 25% (incl. 3 requesting customers) | 48 hours | Error rate stable, latency < 30s | Auto-rollback on health breach |
| General Availability | 100% | Ongoing | All metrics stable | Manual rollback available |

## Rollback Plan
- Mechanism: Feature flag disable (instant)
- Rollback tested: yes (in staging)
- Estimated rollback time: < 30 seconds
- Data rollback needed: no (export jobs are ephemeral)

## Pre-Deployment Checklist
- [x] All quality evaluations passed (4/4 streams)
- [x] Production readiness verified (observability.md):
  - [x] OpenTelemetry instrumentation active
  - [x] Distributed traces verified in staging
  - [x] Metrics: export_job_duration, export_job_count, export_job_errors
  - [x] Structured logs with trace ID correlation
  - [x] Health targets: p95 < 30s, error rate < 1%
  - [x] Dashboard created: "Bulk Export Health"
  - [x] Alerts configured with runbook link
- [x] Feature flag configured: bulk_export_enabled (default: off)
- [x] Database read-replica routing tested under load
- [ ] Release contract reviewed by human
- [ ] On-call team notified
```

**Human checkpoint:** The Engineering Manager reviews the release contract via PR on branch `release/2026-04-07-bulk-data-export`. They verify the rollout plan, rollback mechanism, and production readiness checklist. Approved via PR merge. ✅

---

## Phase 12: Deployment & Validation

**Layer:** Execution · **Loop:** Ship · **Agent type:** `deploy-agent`, `feature-flag-agent`

The `deploy-agent` executes the progressive rollout defined in the release contract. The `feature-flag-agent` manages the `bulk_export_enabled` flag.

### Stage 1: Canary (5%) — 24 hours

- `deploy-agent` enables the feature flag for 5% of traffic
- Monitors error rates, latency, resource consumption
- **Results after 24 hours:**
  - Error rate: 0.1% (baseline: 0.08%) — within threshold ✅
  - Export latency p95: 22s for 1M records ✅
  - Database load: +3% on read replica — within capacity ✅
  - No critical alerts triggered ✅

**Auto-progression:** Health criteria met → proceed to Stage 2.

### Stage 2: Early Adopters (25%) — 48 hours

- `feature-flag-agent` targets the 25% cohort to include the 8 requesting enterprise customers
- Customer Success is notified (via signal: `work/signals/2026-04-09-bulk-export-early-access-available.md`)
- **Results after 48 hours:**
  - 5 enterprise customers have used the export feature
  - 12 export jobs completed successfully
  - 1 export job timed out (8M records — near the limit) — non-critical, logged as signal
  - Customer feedback: positive — "Finally!"

**Auto-progression:** Health criteria met → proceed to Stage 3.

### Stage 3: General Availability (100%)

- `feature-flag-agent` enables for all customers
- `deploy-agent` runs post-deployment validation:
  - Smoke tests passing ✅
  - Error rates within normal bounds ✅
  - Resource consumption within expected bounds ✅

**Release status updated:** `deployed`

---

## Phase 13: Outcome Measurement & Report

**Layer:** Strategy · **Loop:** Ship → Discover · **Agent types:** `product-strategy`, `release-coordinator`

Two weeks after GA, the `product-strategy` agent produces the Outcome Report by comparing actuals against the Outcome Contract.

**Artifact created:** `work/missions/bulk-data-export/OUTCOME-REPORT.md`  
**Template:** `work/missions/_TEMPLATE-outcome-report.md`

```markdown
# Outcome Report: Bulk Data Export

## Mission Summary
MISSION-2026-015 set out to enable bulk data export for enterprise customers,
addressing a $2.4M ARR retention risk. Delivered in 3.5 weeks (0.5 weeks ahead
of the 4-week target). All primary outcomes met or exceeded.

## Targets vs. Actuals

| Metric | Target | Actual | Variance | Verdict |
|--------|--------|--------|----------|---------|
| API available | By 2026-04-12 | 2026-04-09 (GA) | -3 days | met |
| p95 export latency (1M records) | < 30s | 22s | -27% | met |
| Enterprise customers using | ≥ 3 within 2 weeks | 7 | +133% | exceeded |
| Guardrail: existing API p99 | < 200ms | 182ms | Within bounds | met |

## Delivered Assets
| Asset | Type | Registry Entry |
|-------|------|---------------|
| Bulk Export API | code | work/assets/bulk-export-api.md |
| Export UI Component | code | work/assets/bulk-export-ui.md |
| API Reference: Export | documentation | work/assets/bulk-export-api-docs.md |
| How-to: Bulk Export Guide | documentation | work/assets/bulk-export-guide.md |

## Quality Summary
| Evaluation | Date | Verdict |
|-----------|------|---------|
| API implementation | 2026-03-25 | PASS WITH NOTES |
| Data processing | 2026-03-24 | PASS |
| UI integration | 2026-03-30 | PASS |
| Documentation (2nd attempt) | 2026-03-27 | PASS |
| Production readiness | 2026-04-07 | PASS |

## Lessons Learned

### What worked well
- Parallel stream execution saved ~1 week vs. sequential
- Early API spec definition unblocked documentation stream
- Progressive rollout caught the near-limit timeout before GA

### What didn't work as expected
- Documentation FAIL cost 1 day — code examples should be auto-tested in CI
- Architecture ESCALATE on Parquet fan-out took 14 hours for human review

### Agent Fleet Observations
- Quality eval turnaround was the primary bottleneck (avg 18 hours)
- Suggestion: pre-flag PRs with architectural novelty to parallel human review

## Generated Signals
| Signal | Category | Filed As |
|--------|----------|----------|
| Near-limit timeout on 8M export | technical | work/signals/2026-04-10-export-large-dataset-timeout.md |
| Customers requesting scheduled exports | customer | work/signals/2026-04-18-bulk-export-scheduled-request.md |
| Quality eval bottleneck on novel patterns | process | work/signals/2026-04-08-quality-eval-turnaround.md |

## Venture Impact
| Venture | Metric Affected | Impact |
|---------|----------------|--------|
| Platform Product | NRR (Net Revenue Retention) | 8 at-risk renewals secured ($2.4M ARR) |
| Platform Product | Feature completeness vs. competitors | Gap closed |

## Recommendation
- [x] Close mission — Objectives achieved
- [x] Follow-up mission recommended for large dataset support (>10M records)

## Overall Outcome Verdict: EXCEEDED
```

### Venture Health Update

The `product-strategy` agent also updates the relevant venture health report to reflect the outcome:

**Artifact updated:** `org/1-strategy/ventures/platform-product/HEALTH-REPORT.md`

The NRR metric improves from "at-risk" to "on-track" based on the 8 secured renewals.

---

## Phase 14: Operate

**Layer:** Execution · **Loop:** Operate · **Agent types:** `monitoring-agent`, `incident-response-agent`, `feature-flag-agent`

The mission is complete, but the feature is now in production. The Operate Loop takes over.

### Ongoing Monitoring

The `monitoring-agent` watches the "Bulk Export Health" dashboard continuously:
- Export job success rate: 99.2%
- p95 latency: stable at 22–25s
- Feature adoption: growing (12 new customers in week 2)

### Incident Detection & Response

In week 3, the `monitoring-agent` detects an anomaly: export error rate spikes to 4.5% for Parquet format specifically. It triggers an alert.

The `incident-response-agent` activates:
1. **Triage:** Error logs show "out of memory" on Parquet serialization for datasets with > 500 columns
2. **Immediate remediation:** The agent adjusts Parquet writer memory configuration (within its authorized parameter range)
3. **Verification:** Error rate returns to baseline within 15 minutes
4. **Postmortem signal:** Files `work/signals/2026-04-22-parquet-memory-wide-tables.md`
5. **Runbook update:** Adds a "wide table Parquet failure" entry to the export service runbook

If the error had been outside the agent's remediation authority (e.g., requiring an architecture change), it would have escalated to the on-call engineer (**Tier 3 escalation** — production impact requiring human judgment).

### Feature Flag Lifecycle

The `feature-flag-agent` tracks the `bulk_export_enabled` flag:
- **Week 1–2:** Progressive rollout (managed above)
- **Week 4:** Flag has been at 100% for 3 weeks with stable metrics. Agent recommends flag cleanup.
- **Week 6:** Human approves flag removal. Agent creates a PR to remove the flag and replace conditional code with permanent implementation.

> **Improvement signal:** The `monitoring-agent` files an observation: the export health dashboard should include a per-format breakdown, since the Parquet issue was format-specific but the aggregate metrics initially masked it. Signal: `work/signals/2026-04-23-export-dashboard-per-format-metrics.md`.

---

## Phase 15: Continuous Improvement Signals

**Layer:** All layers · **Agent types:** Various

Throughout this mission lifecycle, agents across all layers filed improvement signals. Here is the complete set:

| Signal | Filed By | Layer | Category |
|--------|----------|-------|----------|
| CRM tagging inconsistency for export-related tickets | `customer-signal-scanner` | Execution | process |
| Async job framework lacks cancellation pattern | `coding-agent` | Execution | technical |
| Quality eval turnaround bottleneck on novel patterns | `fleet-performance-monitor` | Orchestration | process |
| Documentation code examples should be auto-tested | `doc-generation-agent` | Execution | process |
| Parquet memory issue on wide tables | `incident-response-agent` | Execution | technical |
| Export dashboard needs per-format breakdown | `monitoring-agent` | Execution | technical |
| Customer demand for scheduled exports | `customer-signal-scanner` | Execution | customer |
| Near-limit timeout on large datasets | `deploy-agent` | Execution | technical |

These signals feed back into the Steering Layer's next weekly digest. Some may become future missions. Some may trigger evolution proposals (e.g., the quality eval bottleneck might lead to a process improvement). The cycle continues.

---

## Layer × Loop Responsibility Matrix

| | Discover | Build | Ship | Operate |
|---|---|---|---|---|
| **Steering** | Aggregates signals into digests; highlights patterns | — | — | Receives improvement signals from all layers |
| **Strategy** | Validates opportunities; drafts mission briefs + outcome contracts | Updates venture health from outcomes | Measures outcomes against contracts | Monitors venture health trends |
| **Orchestration** | — | Decomposes missions; configures fleets; tracks status | Coordinates release; drafts release contract | — |
| **Execution** | Detects signals from production/customers | Implements in parallel streams; self-evaluates | Deploys progressively; manages feature flags | Monitors, remediates, manages incidents |
| **Quality** | — | Evaluates every PR against policies | Verifies production readiness | Evaluates incident response; updates policies |

---

## Complete Artifact Registry (This Mission)

| Artifact | Template | Created By | Approved By |
|----------|----------|-----------|-------------|
| Signal file | `_TEMPLATE-signal.md` | `customer-signal-scanner` | Auto-merged |
| Signal digest | `_TEMPLATE-signal-digest.md` | `signal-aggregation` | Steering human |
| Mission brief | `_TEMPLATE-mission-brief.md` | `product-strategy` | VP Product (PR merge) |
| Outcome contract | `_TEMPLATE-outcome-contract.md` | `product-strategy` | VP Product (PR merge) |
| Fleet config | `_TEMPLATE-fleet-config.md` | `mission-orchestrator` | Mission Lead |
| Mission status | `_TEMPLATE-mission-status.md` | `fleet-performance-monitor` | Auto-appended |
| Decision record | `_TEMPLATE-decision-record.md` | `coding-agent` | Tech Lead |
| Quality eval reports (×4) | `_TEMPLATE-quality-evaluation-report.md` | Various eval agents | Auto-generated |
| Fleet performance report | `_TEMPLATE-fleet-performance-report.md` | `fleet-performance-monitor` | Mission Lead |
| Asset registry entries (×4) | `_TEMPLATE-asset-registry-entry.md` | Stream agents | Division leads |
| Release contract | `_TEMPLATE-release-contract.md` | `release-coordinator` | Eng. Manager (PR merge) |
| Outcome report | `_TEMPLATE-outcome-report.md` | `product-strategy` | VP Product |
| Improvement signals (×8) | `_TEMPLATE-signal.md` | Various agents | Auto-merged |
| Postmortem (if incident) | `_TEMPLATE-postmortem.md` | `incident-response-agent` | On-call engineer |

---

## Key Takeaways

This example demonstrates the **complete artifact chain** flowing through all 5 layers and all 4 loops:

- **Steering Layer** aggregates raw signals into actionable intelligence (digests + pattern alerts)
- **Strategy Layer** validates opportunities, creates mission contracts, and measures outcomes
- **Orchestration Layer** decomposes missions into parallel streams and tracks fleet performance
- **Execution Layer** produces code, documentation, and deployments — each agent self-evaluates before submission
- **Quality Layer** independently evaluates every output against policies, with structured verdicts and escalation paths
- **Every agent** contributes improvement signals, feeding the continuous evolution cycle
- **Humans** decide at strategic checkpoints (mission approval, architecture escalation, release approval) — agents do the work between checkpoints
- **Git** is the single system of record: branches for isolation, PRs for review, CODEOWNERS for governance, history for audit
