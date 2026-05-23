# Agent Type Definition: [Agent Name]

> **Template version:** 1.4 | **Last updated:** 2026-05-23
> **Governed registry entry for a single agent type.**  
> **Governance:** New types require Steering Layer evaluation + CTO approval via PR.

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | _(unique identifier, e.g., "steering-signal-scanner")_ |
| **Name** | _(human-readable name, e.g., "Customer Signal Scanner")_ |
| **Version** | 1.0.0 |

## Classification

| Field | Value |
|-------|-------|
| **Layer** | _(steering / strategy / orchestration / execution / quality)_ |
| **Division** | _(division ID — required for execution agents, optional otherwise)_ |
| **Category** | _(e.g., "signal-processing", "code-generation", "evaluation")_ |

## Lifecycle

| Field | Value |
|-------|-------|
| **Status** | proposed _(proposed / approved / implementing / active / deprecated / retired)_ |
| **Proposed date** | YYYY-MM-DD |
| **Approved date** | |
| **Active date** | |
| **Deprecated date** | |
| **Retired date** | |
| **Superseded by** | _(agent type ID that replaces this one, if deprecated)_ |

## Ownership

| Field | Value |
|-------|-------|
| **Owning team** | |
| **Contact** | _(primary human contact)_ |
| **Approved by** | _(e.g., "CTO")_ |

## Description

**What this agent does:**  
_(one-paragraph description)_

**Problem solved:**  
_(what capability gap or problem this agent addresses)_

**Value proposition:**  
_(why the enterprise needs this agent type)_

## Capabilities

### Skills
- _(e.g., "code-review", "test-generation")_

### MCP Servers
- _(e.g., "github", "jira", "slack")_

### Tool Access
- _(e.g., "git", "ci-cd-pipeline", "observability-api")_

### Languages
- _(programming languages for code agents, e.g., "python", "typescript")_

### Data Access
- _(e.g., "crm", "support-tickets", "telemetry")_

## Identity & Access Boundary

| Field | Value |
|-------|-------|
| **Runtime identity** | _(service account, workload identity, named principal, or equivalent)_ |
| **Credential source** | _(e.g., "KMS-issued secret", "OIDC workload identity", "OAuth client credentials")_ |
| **Credential scope** | _(per-agent-type / per-mission ephemeral / shared-with-fleet — shared requires justification)_ |
| **Allowed environments** | _(e.g., "dev + staging write, production read-only")_ |
| **Allowed data classifications** | _(e.g., "INTERNAL", "CONFIDENTIAL with ticket scope")_ |
| **High-impact approval gates** | _(what requires explicit human approval before use)_ |

### Access Boundary Notes
- _(document blast-radius limits, secrets handling expectations, identity rotation, and when this agent must escalate instead of using its access)_

## Instructions Reference

| Field | Value |
|-------|-------|
| **Layer AGENT.md** | _(e.g., "org/0-steering/AGENT.md")_ |
| **Division DIVISION.md** | _(e.g., "org/3-execution/divisions/core-api/DIVISION.md")_ |

### Additional Context
- _(additional instruction files this agent must read)_

## Interactions

### Produces
- _(artifact types this agent produces, e.g., "signal", "quality-evaluation-report")_

### Consumes
- _(artifact types this agent consumes, e.g., "mission-brief", "fleet-config")_

### Collaborates With
- _(other agent type IDs this agent frequently interacts with)_

### Escalates To
- _(human roles or agent types for escalation)_

## Scaling

| Parameter | Value |
|-----------|-------|
| **Min instances** | 0 _(0 = on-demand only)_ |
| **Max instances** | 1 |
| **Scaling trigger** | _(e.g., "mission-assignment", "signal-volume > 50/day")_ |
| **Cost class** | _(light / medium / heavy)_ |

## Model Governance

> Required for all agent types that use LLM or ML models. Depth scales with risk tier per [ai-governance.md](../../4-quality/policies/ai-governance.md).

| Field | Value |
|-------|-------|
| **AI Risk Tier** | _(0: Prohibited / 1: High-Risk / 2: Limited-Risk / 3: Minimal-Risk — per ai-governance.md §1)_ |
| **Model(s) used** | _(e.g., "claude-sonnet-4-6", "gpt-4o" — list all models this agent may use)_ |
| **Model selection rationale** | _(why this model was chosen over alternatives — capability, cost, safety, licensing)_ |
| **Autonomy tier** | _(1: Human-directed / 2: Supervised / 3: Semi-autonomous / 4: Full autonomy — per risk-management.md §6.1)_ |

### Intended Use & Scope
_(What this agent is designed to do and what it must NOT be used for. Include scope boundaries.)_

### Known Limitations & Failure Modes
_(Document known weaknesses, hallucination patterns, edge cases, and situations where the agent should escalate rather than act.)_

### Training Data & Context
_(For Tier 1–2: describe training data sources, fine-tuning data, or context documents. For Tier 3: "Standard LLM — no custom training data" is acceptable.)_

### Data Resources (ISO/IEC 42001 A.4.3 / B.4.3)
Document the data resources used by this AI system. Cross-reference the AI system inventory entry in [`docs/compliance/templates/_TEMPLATE-ai-system-inventory.md`](../../docs/compliance/templates/_TEMPLATE-ai-system-inventory.md) so system-level inventory and model-level resource documentation stay aligned.

| Topic | Documentation required |
|-------|-------------------------|
| **Provenance** | _(where the data came from, owner/controller, collection method, licensing/usage rights)_ |
| **Last updated / modified** | _(YYYY-MM-DD and update cadence)_ |
| **Data categories by lifecycle stage** | _(training / validation / test / production / monitoring / feedback)_ |
| **Data categories per ISO/IEC 19944-1** | _(e.g., personal data, telemetry, user-generated content, synthetic data, derived data)_ |
| **Labelling process** | _(manual / automated / hybrid; who labels; QA controls; instructions used)_ |
| **Intended use of data** | _(what each dataset is used for and what it must not be used for)_ |
| **Data quality** | _(quality criteria, completeness, accuracy, representativeness, known gaps; reference ISO/IEC 5259-based assessment if used)_ |
| **Retention and disposal** | _(retention period, deletion triggers, archival handling, disposal method)_ |
| **Known or potential bias issues** | _(representation gaps, skew, drift, sensitive attributes, mitigation steps)_ |
| **Data preparation methods** | _(cleaning, filtering, normalization, augmentation, deduplication, redaction, feature engineering, prompt-context curation)_ |

### Tooling Resources (ISO/IEC 42001 A.4.4 / B.4.4)
Document the tooling resources used to build, evaluate, provision, and operate this AI system.

| Topic | Documentation required |
|-------|-------------------------|
| **Algorithm types and ML models** | _(model families, architectures, non-LLM algorithms, embedding/reranking models, classifiers, policies)_ |
| **Data conditioning tools or processes** | _(ETL, labeling, preprocessing, redaction, feature pipelines, prompt/context assembly)_ |
| **Optimization methods** | _(fine-tuning, prompt optimization, hyperparameter search, distillation, quantization, caching, routing)_ |
| **Evaluation methods** | _(benchmarks, human review, automated evals, red-team tests, acceptance thresholds)_ |
| **Provisioning tools for resources** | _(IaC, deployment tooling, model serving stack, schedulers, secret/config provisioning)_ |
| **Tools aiding model development** | _(notebooks, experiment tracking, vector DBs, annotation tools, observability, governance tooling)_ |
| **Software and hardware for design / development / deployment** | _(key SDKs, frameworks, runtimes, accelerators, endpoints, devices)_ |

### System & Computing Resources (ISO/IEC 42001 A.4.5 / B.4.5)
Document the system and computing resources required to run this AI system. Cross-reference the AI system inventory when summarizing system location or dependencies.

| Topic | Documentation required |
|-------|-------------------------|
| **AI system resource requirements** | _(CPU / GPU / memory / storage / latency / throughput requirements, including constrained-resource devices if applicable)_ |
| **Resource locations** | _(on-premises / cloud / edge / end-user device / hybrid, including regions or providers where relevant)_ |
| **Processing resources** | _(compute, network, storage, queues, accelerators, failover capacity, offline fallback)_ |
| **Hardware impact** | _(environmental impact from use or manufacturing where known, energy intensity assumptions, cost drivers, cost constraints)_ |

### Fairness Considerations
_(For Tier 1: document fairness evaluation results, metrics used, and demographic dimensions tested. For Tier 2: document fairness review. For Tier 3: "N/A — minimal-risk internal tooling" is acceptable.)_

### Token Budget
| Parameter | Value |
|-----------|-------|
| **Expected tokens per task** | _(e.g., "5K–20K input, 2K–8K output")_ |
| **Mission budget ceiling** | _(e.g., "500K tokens per mission" — or "per fleet config")_ |
| **Cost class** | _(light / medium / heavy)_ |

## Quality

### Applicable Policies
- _(e.g., "security", "architecture", "ai-governance")_

### Evaluation Frequency
_(e.g., "per-PR", "weekly")_

### Performance Metrics
- _(e.g., "pr-acceptance-rate", "eval-accuracy")_

## Telemetry

All agent actions produce OpenTelemetry spans per [`docs/otel-contract.md`](../../../docs/otel-contract.md).

- Required span types for every agent: `agent.run`, `tool.execute`
- Required native event for governed decisions: `governance.decision`
- Add `inference.chat` and/or `inference.generate` whenever the agent uses model-backed reasoning or generation
- Telemetry declarations here must stay aligned with the canonical contract in `docs/otel-contract.md`

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.4 | 2026-05-23 | Expanded embedded model card with ISO/IEC 42001 A.4.3, A.4.4, and A.4.5 resource documentation sections for data, tooling, and computing resources, including AI system inventory cross-reference. |
| 1.3 | 2026-03-27 | Added Identity & Access Boundary section so each agent type documents runtime identity, credential source/scope, allowed environments, allowed data classifications, and high-impact approval gates. |
| 1.2 | 2026-03-15 | Added Telemetry section with canonical OTel contract reference, required core spans, decision event, and conditional inference span guidance (#115) |
| 1.1 | 2026-03-14 | Added Model Governance section with AI risk tier, model identity, intended use, limitations, fairness considerations, and token budget per ai-governance.md policy (#91) |
| 1.0 | 2026-02-19 | Initial version |
