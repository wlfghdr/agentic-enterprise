# Technical Design: [Mission Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Purpose:** Bridge the gap between mission-level outcomes and implementation-level specifications. Required for multi-stream missions, novel architecture patterns, or missions marked `design-required: true`.  
> **Produced by:** Execution Layer (Technical Design Agent or Tech Lead)  
> **Reviewed at:** Architecture review human checkpoint (before stream execution begins)  
> **Lives alongside the mission brief in** `work/missions/<name>/`

---

## Metadata

| Field | Value |
|-------|-------|
| **Mission ID** | _(e.g., MISSION-2026-042)_ |
| **Mission brief** | [BRIEF.md](./BRIEF.md) |
| **Outcome contract** | [OUTCOME-CONTRACT.md](./OUTCOME-CONTRACT.md) |
| **Fleet config** | _(link to fleet config)_ |
| **Status** | draft | in-review | approved | superseded |
| **Author** | _(agent type or human)_ |
| **Reviewers** | _(Architecture Governor, Tech Lead, Security Lead as needed)_ |
| **Created** | YYYY-MM-DD |
| **Approved** | YYYY-MM-DD |

---

## Context & Goals

[Brief summary — what is being built, why, and the key constraints that shape the design. Reference the Mission Brief objective and Outcome Contract targets. Keep this to 2–4 paragraphs. This section is the "why" behind the technical choices below.]

---

## API Contracts

> **Requirement:** Per architecture policy — "Design the contract before the implementation."  
> Define all new or modified API surfaces. Use OpenAPI 3.x (REST), Protocol Buffers (gRPC), or GraphQL schema fragments.

### [API / Service Name 1]

```yaml
# OpenAPI 3.x fragment — or link to full spec file
openapi: 3.0.3
paths:
  /api/v2/example:
    post:
      summary: "[Description]"
      operationId: createExample
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExampleRequest'
      responses:
        '202':
          description: Accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExampleResponse'
        '400':
          description: Validation error
        '429':
          description: Rate limited

components:
  schemas:
    ExampleRequest:
      type: object
      properties:
        # Define request shape
    ExampleResponse:
      type: object
      properties:
        # Define response shape
```

<!-- Repeat for additional APIs -->

---

## Data Model

> Define schema changes, new entities, relationships, and migration strategy. Include enough detail for implementation agents to build without ambiguity.

### New / Modified Entities

| Entity | Change | Fields | Notes |
|--------|--------|--------|-------|
| _(e.g., ExportJob)_ | new | id, customerId, format, status, createdAt, completedAt | _(notes)_ |

### Entity Relationships

```
[Entity A] 1──* [Entity B]
[Entity B] *──1 [Entity C]
```

### Migration Strategy

- [ ] Backward-compatible schema change (additive only)
- [ ] Requires data migration — migration plan: _(describe)_
- [ ] Feature-flag gated schema change

---

## Interface Contracts Between Streams

> For each inter-stream dependency from the Fleet Config, define the **content** of that interface — not just that a dependency exists.

| From Stream | To Stream | Interface | Contract |
|-------------|-----------|-----------|----------|
| _(e.g., data-processing)_ | _(api-implementation)_ | _(e.g., shared types)_ | _(describe: shared type definitions, event schema, file format, etc.)_ |
| _(e.g., api-implementation)_ | _(ui-integration)_ | _(e.g., API spec)_ | _(describe: endpoint URLs, request/response shapes, auth requirements)_ |

### Shared Type Definitions

```typescript
// Define shared types, DTOs, or event schemas that cross stream boundaries
interface ExampleSharedType {
  id: string;
  // ...
}
```

---

## Behavioral Specifications

> Define key behaviors as Given/When/Then scenarios. These bridge the gap between outcome-level acceptance criteria (Outcome Contract) and implementation-level test cases. Focus on behaviors that are ambiguous, complex, or cross stream boundaries.

### Behavior 1: [Name]

**Relates to:** Outcome Contract acceptance criterion #N

```gherkin
Scenario: [Descriptive name]
  Given [precondition]
  And [additional context]
  When [action or trigger]
  Then [expected outcome]
  And [additional assertion]
```

### Behavior 2: [Name]

```gherkin
Scenario: [Descriptive name]
  Given [precondition]
  When [action or trigger]
  Then [expected outcome]
```

### Error & Edge Case Scenarios

```gherkin
Scenario: [Error case name]
  Given [precondition]
  When [invalid action or failure condition]
  Then [expected error handling behavior]
```

<!-- Add as many scenarios as needed to remove ambiguity -->

---

## Security Threat Model

> Identify assets, threats, and mitigations. Use STRIDE or equivalent. Focus on threats introduced or affected by this mission — not a full system review.

### Assets at Risk

| Asset | Classification | Exposure |
|-------|---------------|----------|
| _(e.g., customer data export files)_ | _(e.g., confidential)_ | _(e.g., temporary storage, API endpoint)_ |

### Threat Analysis

| Threat | Category (STRIDE) | Likelihood | Impact | Mitigation |
|--------|--------------------|------------|--------|------------|
| _(e.g., unauthorized access to export files)_ | _(e.g., Elevation of Privilege)_ | _(high/med/low)_ | _(high/med/low)_ | _(e.g., signed URLs with 15-min TTL)_ |

### Security Controls

- [ ] Authentication: _(describe auth mechanism for new endpoints)_
- [ ] Authorization: _(describe RBAC/ABAC rules)_
- [ ] Input validation: _(describe validation approach)_
- [ ] Data encryption: _(at rest / in transit)_
- [ ] Audit logging: _(what actions are logged)_
- [ ] Rate limiting: _(describe limits)_

---

## Performance Budgets

> Define quantitative performance targets per component. These become pass/fail criteria during quality evaluation.

| Component | Metric | Budget | Measurement Method |
|-----------|--------|--------|--------------------|
| _(e.g., Export API endpoint)_ | p95 latency | _(e.g., < 200ms for job creation)_ | _(e.g., load test, APM)_ |
| _(e.g., Data processing)_ | throughput | _(e.g., 1M records in < 5 min)_ | _(e.g., benchmark test)_ |
| _(e.g., UI component)_ | time to interactive | _(e.g., < 100ms added)_ | _(e.g., Lighthouse)_ |

### Load Test Plan

| Scenario | Concurrent users | Duration | Success criteria |
|----------|-----------------|----------|-----------------|
| _(e.g., steady state)_ | _(100)_ | _(30 min)_ | _(p99 < 500ms, error rate < 0.1%)_ |
| _(e.g., burst)_ | _(1000)_ | _(5 min)_ | _(rate limiting activates, no data loss)_ |

---

## Architecture Decisions

> Key technical choices made during design. For novel patterns, create a full Architecture Decision Record in `work/decisions/`. For standard choices, document them inline here.

### Decision 1: [Title]

| Field | Value |
|-------|-------|
| **Context** | _(why this decision is needed)_ |
| **Options considered** | _(list alternatives)_ |
| **Decision** | _(what was chosen)_ |
| **Rationale** | _(why)_ |
| **Consequences** | _(trade-offs accepted)_ |
| **ADR** | _(link to full ADR in `work/decisions/` if novel pattern, or "inline — standard pattern")_ |

<!-- Repeat for additional decisions -->

---

## Open Questions

> Unresolved items requiring human input before execution can proceed. Each must have an owner and target resolution date.

| # | Question | Impact if Unresolved | Owner | Target Date | Resolution |
|---|----------|---------------------|-------|-------------|------------|
| 1 | _(e.g., "Which file storage backend for exports?")_ | _(blocks stream X)_ | _(Tech Lead)_ | YYYY-MM-DD | _(filled when resolved)_ |

---

## Design Review Checklist

Before submitting this design for review, verify:

- [ ] API contracts defined for all new/modified endpoints
- [ ] Data model changes documented with migration strategy
- [ ] All inter-stream interface contracts specified
- [ ] Behavioral specs cover ambiguous or cross-stream behaviors
- [ ] Security threat model completed for new attack surfaces
- [ ] Performance budgets set with measurement methods
- [ ] Architecture decisions documented (or linked to ADRs)
- [ ] Open questions have owners and target dates
- [ ] Design is consistent with architecture policy requirements
- [ ] Design addresses all acceptance criteria from the Outcome Contract
---

## Revision History

| Rev | Date | Author | Summary |
|---|---|---|---|
| 1 | YYYY-MM-DD | [agent/human] | Initial draft |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
