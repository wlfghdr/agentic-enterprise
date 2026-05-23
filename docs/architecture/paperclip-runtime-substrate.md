# Paperclip as Runtime Substrate, Agentic Enterprise as Policy Overlay

## Position

If Paperclip matures into a credible multi-tenant runtime substrate, Agentic Enterprise should **stop competing at the runtime layer**.

The intended split is:

- **Paperclip** owns runtime execution, delegation, task state, approvals, heartbeats, tenant isolation, and runtime coordination.
- **Agentic Enterprise** owns operating-model semantics, governance policy, quality expectations, compliance mappings, observability meaning, and enterprise-specific overlays.

Agentic Enterprise should therefore evolve from a "framework that also implies runtime patterns" into a **portable governance and semantics overlay** that can run on top of Paperclip or any other capable runtime.

## Boundary Rule

Use this rule when deciding where a capability belongs:

- If it is about **running agents safely and reliably**, it belongs in **Paperclip**.
- If it is about **what work means, who may approve it, how it is evaluated, and how it maps to enterprise governance**, it belongs in **Agentic Enterprise**.
- If it needs both, Paperclip should provide the primitive and Agentic Enterprise should provide the policy, taxonomy, and operator guidance.

## Inventory of Agentic Enterprise Concepts

| Concept / capability | Classification | Why it belongs there | AE role if Paperclip exists |
|---|---|---|---|
| Organizational runtime, agent lifecycle, workers, queues, retries | **Paperclip-native** | Core execution substrate concerns | Reference only, do not re-specify implementation |
| Task backend and durable work state | **Paperclip-native** | Runtime persistence and orchestration primitive | Map AE mission/work artifacts onto Paperclip tasks |
| Delegation and sub-agent spawning | **Paperclip-native** | Runtime coordination primitive | Define which roles may delegate and under what policy |
| Human approval interrupts and resumptions | **Paperclip-native** | Runtime control-flow primitive | Define approval policy, authority, and evidence requirements |
| Heartbeats, wakeups, scheduling | **Paperclip-native** | Runtime automation primitive | Define when heartbeats are allowed, required, or escalated |
| Company / tenant isolation | **Paperclip-native** | Runtime security and isolation primitive | Define governance requirements for isolation boundaries |
| Tool attachment and plugin loading | **Paperclip-native** | Runtime extension mechanism | Define approved integration classes, MCP profiles, and vendor controls |
| Runtime coordination across agents | **Paperclip-native** | Scheduler / state / routing concern | Define mission semantics and role boundaries |
| Signals → missions → work lifecycle | **Intentionally external** | This is the operating model itself, not a generic runtime feature | Remains a core AE semantic layer |
| 5-layer org model and division structure | **Intentionally external** | Enterprise governance taxonomy, not runtime machinery | Remains a core AE semantic layer |
| Quality policy domains and evaluation criteria | **Intentionally external** | Enterprise policy content is repo-governed and organization-specific | Remains core AE content |
| CODEOWNERS / PR governance / Git audit model | **Intentionally external** | Governance backbone choice, independent of runtime | Remains core AE operating pattern |
| Compliance mappings and control crosswalks | **Intentionally external** | Enterprise interpretation and audit posture are externalized by design | Remains core AE content |
| Observability semantics and evidence interpretation | **Intentionally external** | Meaning of telemetry for governance is policy-level, not runtime-level | Remains AE contract and guidance |
| Knowledge manifests, capability contracts, skill manifests, MCP profiles | **Representable by convention/plugin** | Runtime can carry them, but AE defines their governance semantics | AE defines schemas/rules; Paperclip may load or enforce them |
| Agent role instructions and templates | **Representable by convention/plugin** | Runtime can inject prompts/instructions, but the content is AE-owned | AE remains source of truth |
| Mission templates, decision templates, release templates | **Intentionally external** | Business operating artifacts, not runtime internals | Remain in AE |
| Work backend choices, including Git files vs issue tracker | **Intentionally external** | Organizational workflow decision above the runtime | Remains AE guidance |
| OTel contract wiring and exporter implementation | **Paperclip-native** | Runtime emits telemetry | AE defines canonical fields, mappings, and governance expectations |
| Runtime-to-governance telemetry mapping | **Representable by convention/plugin** | Needs both substrate hooks and enterprise schema | Shared boundary, AE-led semantics |
| Policy-as-code gates and validation scripts | **Intentionally external** | Governance enforcement in repo lifecycle, not runtime core | Remains AE content |
| Enterprise overlays for regulated industries or internal standards | **Intentionally external** | This is precisely the residual AE scope | Remains AE differentiator |
| Cross-runtime portability guidance | **Intentionally external** | Needed so AE is not captive to one runtime | Remains AE architecture guidance |
| Approval semantics richer than substrate defaults (RACI, policy-based escalation, evidence thresholds) | **Representable by convention/plugin** | Runtime can expose primitives; enterprise meaning sits above them | AE defines policy, Paperclip executes hooks |
| First-class mission / signal / release objects in runtime | **Missing upstream** | Useful if Paperclip wants to understand AE artifacts natively | AE can model externally until upstream exists |
| First-class governance object model for policies, controls, exceptions, evidence | **Missing upstream** | Helpful for deeper enterprise integration | Keep external until upstream proves stable |
| Native support for governed observability semantics beyond generic spans/events | **Missing upstream** | Runtime telemetry is not enough; enterprise evidence needs semantic overlays | AE maintains mapping contract until upstream exists |

## Residual Long-Term Role of Agentic Enterprise

If Paperclip becomes enterprise-ready, Agentic Enterprise should converge on five durable responsibilities:

1. **Operating-model semantics**
   - signals, missions, decisions, releases, quality verdicts, escalation meanings
2. **Governance policy**
   - approval rules, role boundaries, control expectations, exception handling
3. **Compliance interpretation**
   - mappings from work and telemetry to ISO 42001, ISO 27001, SOC 2, GDPR, EU AI Act, and related frameworks
4. **Observability semantics**
   - canonical telemetry meaning, evidence expectations, and audit interpretation
5. **Enterprise overlays**
   - industry, company, or regulatory customization layered on a general-purpose runtime

In short, **Paperclip runs the company. Agentic Enterprise explains how the company should be governed while it runs.**

## Practical Cross-Repo Boundary

A practical split should look like this:

### Paperclip repository should own

- runtime APIs and execution engine
- task model and state transitions
- approvals as runtime interrupts
- delegation primitives
- heartbeat/scheduler behavior
- tenancy and isolation model
- plugin/tool loading model
- telemetry emission hooks

### Agentic Enterprise repository should own

- org structure under `org/`
- process semantics under `process/`
- quality policies under `org/4-quality/policies/`
- compliance reference docs under `docs/compliance/`
- observability contract and governance interpretation
- mission/signal/release templates and Git governance patterns
- runtime comparison and adoption guidance

### Shared contract between them

- artifact identifiers and lifecycle state mapping
- approval event schema
- delegation event schema
- telemetry field mapping
- tenant / organization identity mapping
- plugin capability declaration format

Paperclip should expose primitives. Agentic Enterprise should consume those primitives through documented contracts rather than by re-implementing them.

## Migration Path: from Framework to Overlay

### Phase 1, Current state

Agentic Enterprise remains runtime-agnostic and keeps describing some runtime-adjacent concepts so adopters can succeed even without Paperclip.

### Phase 2, Boundary tightening

As Paperclip closes runtime gaps:

- remove AE prose that sounds like a runtime implementation guide unless it is explicitly runtime-neutral
- move Paperclip-specific execution mechanics into Paperclip docs
- keep AE runtime guides focused on configuration and policy integration only

### Phase 3, Overlay mode

Agentic Enterprise becomes primarily:

- a governance repo structure
- policy and compliance content
- semantic contracts and templates
- adapter docs for supported runtimes, with Paperclip as the most complete target

### Phase 4, Optional native integration

If Paperclip later adds first-class support for AE concepts such as missions, approvals with RACI semantics, policy bundles, and evidence objects, AE should consume those native objects where it helps, but still keep the governance model portable.

## Migration Checklist

1. **Name the boundary explicitly** in architecture docs and runtime guides.
2. **Stop duplicating runtime concerns** once Paperclip has stable primitives for them.
3. **Preserve portability** by keeping AE schemas and policy semantics runtime-neutral.
4. **Publish adapter mappings** from AE artifacts to Paperclip objects and events.
5. **Treat missing upstream features as adapters first**, not as a reason to re-grow a parallel runtime inside AE.
6. **Keep Git as governance backbone unless intentionally changed**, even if execution moves deeper into Paperclip.

## Decision Summary

Agentic Enterprise should not try to become a second runtime when Paperclip can be the substrate. Its durable value is the layer above execution: policy, semantics, evidence, compliance, and enterprise customization.
