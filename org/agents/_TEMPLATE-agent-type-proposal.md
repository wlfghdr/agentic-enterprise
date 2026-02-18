# Agent Type Proposal: [Agent Name]

> **Template version:** 1.0  
> **Proposed by:** [name / division / layer]  
> **Date:** YYYY-MM-DD  
> **Status:** proposed | under-review | approved | rejected  
> **Related signal:** [link to signal in `work/signals/` that identified the capability gap]

---

## Summary

[One paragraph: what agent type is being proposed and why it's needed]

## Problem Statement

**Capability gap:** [What can't the current agent fleet do that this agent would solve?]

**Evidence:**
- [Signal or metric that demonstrates the need]
- [Current workaround and its cost]
- [Frequency / volume of the unmet need]

## Proposed Agent Type

| Attribute | Value |
|-----------|-------|
| **Name** | [e.g., "Release Impact Analyzer"] |
| **Layer** | [steering / strategy / orchestration / execution / quality] |
| **Division** | [If execution layer — which division? Otherwise N/A] |
| **Category** | [e.g., signal-processing, code-generation, evaluation, coordination] |

## Capabilities

### Skills
- [Skill 1 — what the agent can do]
- [Skill 2]

### Tool & System Access
- [MCP server / API / tool it needs access to]
- [Data sources it needs to read]

### Interactions
- **Produces:** [What artifacts does it create? e.g., signals, evaluation reports, code PRs]
- **Consumes:** [What artifacts does it need as input? e.g., mission briefs, fleet configs]
- **Collaborates with:** [Other agent types it works alongside]
- **Escalates to:** [Human roles for edge cases]

## Scaling Requirements

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Min instances** | [e.g., 0 — on-demand] | [Why] |
| **Max instances** | [e.g., 5] | [Based on expected workload] |
| **Scaling trigger** | [e.g., "mission-assignment" or "signal-volume > 50/day"] | [What creates demand] |
| **Cost class** | [light / medium / heavy] | [Resource consumption profile] |

## Quality & Safety

### Applicable Policies
- [ ] [Policy 1 — e.g., security.md]
- [ ] [Policy 2 — e.g., architecture.md]

### Boundary Constraints
- [What this agent must NOT do]
- [Escalation conditions]
- [Human oversight requirements]

### Risk Assessment
- **Over-scoping risk:** [Could this agent's scope creep into another agent's domain?]
- **Under-scoping risk:** [Is this agent too narrow to be worth the overhead?]
- **Safety risk:** [Could this agent's actions cause harm if it malfunctions?]

## Impact Assessment

### Affected Layers / Divisions
- [Which parts of the org will this agent interact with?]

### Existing Agent Overlap
- [Does any existing agent type partially cover this capability? If so, how does this differ?]

### Expected Benefits
- [Quantified if possible — e.g., "reduce signal triage time by 60%"]

## Implementation Estimate

| Phase | Duration | Dependencies |
|-------|----------|-------------|
| Design (instructions, boundaries) | [e.g., 1 week] | [Quality Layer review] |
| Implementation (skills, tools) | [e.g., 2 weeks] | [MCP server availability] |
| Validation (quality review) | [e.g., 1 week] | [Test environment] |
| Deployment | [e.g., 1 day] | [Registry entry creation] |

## Approval

- [ ] Steering Layer evaluation complete
- [ ] Quality Layer boundary review complete
- [ ] CTO approval
- [ ] Registry entry created in `org/agents/<layer>/<agent-id>.md`
