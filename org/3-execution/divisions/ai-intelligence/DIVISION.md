# Division: AI & Intelligence

> **Owner:** <!-- Division lead name -->
> **Type:** Core
> **Layer:** Execution
> **Status:** Active

---

## Purpose

Owns AI reasoning, natural language interfaces, agent orchestration, workflow automation, and AI safety. This division provides the intelligence layer that powers agentic capabilities across the enterprise.

## Scope

### In Scope
- AI reasoning and causal analysis engines
- Natural language interfaces and conversational AI
- Agent orchestration and workflow automation
- AI safety — prompt injection prevention, hallucination detection, output validation
- Trust scoring and agent reliability metrics

### Out of Scope
- Data storage and pipelines (→ Data Foundation)
- UI and dashboard rendering (→ Core Applications)
- Security scanning of code artifacts (→ Quality & Security Engineering)

## Key Responsibilities

1. **AI Reasoning** — Develop and optimize the intelligence that powers all agent capabilities
2. **Workflow Automation** — Translate natural language intents into executable automation workflows
3. **Agent Safety** — Prevent prompt injection, detect hallucinations, and validate agent outputs
4. **Trust Infrastructure** — Calculate and maintain agent trust scores based on evidence quality

## Interfaces

| Direction | With | Interface |
|-----------|------|-----------|
| Receives from | Strategy Layer | Mission briefs involving this division |
| Delivers to | Quality Layer | Work outputs for quality evaluation |
| Collaborates with | Core Applications, Data Foundation | Shared data contracts / APIs |

## Quality Policies

The following quality policies are mandatory for all work produced by this division:

- `policies/security.md` — Always
- `policies/architecture.md` — For code / API changes
- `policies/security.md` — For AI safety and trust scoring

## Human Checkpoints

These decisions require human division lead involvement:

- Architecture-changing proposals
- New external integrations
- Customer-impacting schema changes
- Work that crosses division boundaries

## Agent Instructions

When working within this division:
1. Read all applicable quality policies before starting
2. Check the Software Catalog for existing services before creating new ones
3. Follow established code patterns in this division's codebase
4. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
5. Register new components via `org/3-execution/divisions/_TEMPLATE/_TEMPLATE-component-onboarding.md`

## Assets & Repositories

| Asset | Location | Description |
|-------|----------|-------------|
| Source code | <!-- repo URL --> | Main repository |
| Documentation | <!-- doc URL --> | User-facing docs |
| API specs | <!-- API spec URL --> | OpenAPI specs |
