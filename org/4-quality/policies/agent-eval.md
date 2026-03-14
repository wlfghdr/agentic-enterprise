# Agent Behavioral Evaluation Policy — Eval-Driven Development

> **Applies to:** All AI agent types, agent instructions, fleet configurations, and model changes
> **Enforced by:** Quality Layer eval agents + CI/CD pipeline gates
> **Authority:** Quality & Engineering leadership
> **Version:** 1.0 | **Last updated:** 2026-03-14

---

## Principles

1. **Eval before ship** — No agent instruction change, model swap, or autonomy-level change reaches production without passing its evaluation suite. Evals are a hard gate, not a nice-to-have.
2. **Behavioral correctness over output style** — Evaluate what the agent *does* (tool calls, decisions, escalations, policy compliance), not just what it *says*. Style is secondary to behavior.
3. **Regression is a bug** — If an agent previously handled a case correctly and now handles it incorrectly, that is a regression and must block deployment — even if aggregate metrics look fine.
4. **Observable evaluation** — Every eval run produces telemetry. Eval results are not just pass/fail — they feed dashboards, trend analysis, and drift detection.
5. **Proportional rigor** — Eval depth scales with agent risk tier (per [AI Governance Policy](ai-governance.md) §1). Higher-risk agents require deeper, more frequent evaluation.

---

## Mandatory Requirements

### 1. Evaluation Scope

Every agent type definition in `org/agents/` must declare an evaluation scope covering these dimensions:

#### 1.1 Output Correctness

- [ ] Agent produces factually accurate outputs for known test cases
- [ ] Agent does not hallucinate facts, citations, or data that can be verified
- [ ] Agent produces outputs in the expected format and structure
- [ ] Agent correctly interprets ambiguous inputs (or escalates appropriately)

#### 1.2 Instruction Following

- [ ] Agent follows its layer-specific `AGENT.md` boundaries — does not perform work assigned to other layers
- [ ] Agent follows its agent type definition — uses only declared tools, stays within declared scope
- [ ] Agent follows quality policies — outputs comply with all applicable policies
- [ ] Agent follows mission context — does not drift from the assigned task
- [ ] Agent escalates when encountering situations outside its boundaries (per AGENTS.md Rule 2)

#### 1.3 Tool Call Correctness

- [ ] Agent calls the correct tools for the given task
- [ ] Agent passes valid parameters to tools
- [ ] Agent handles tool errors gracefully (retry, fallback, escalate — not crash or ignore)
- [ ] Agent does not call tools unnecessarily (resource efficiency)
- [ ] Agent respects tool call sequence requirements (e.g., read before write)

#### 1.4 Decision Quality

- [ ] Agent makes governance decisions consistent with policies (approve/reject/escalate)
- [ ] Agent provides grounded reasoning for decisions (per AGENTS.md Rule 1)
- [ ] Agent escalates to humans when required (per AGENTS.md Rule 2) — does not silently decide on matters requiring human approval
- [ ] Agent does not exhibit bias in decisions across comparable inputs (cross-reference: [AI Governance Policy](ai-governance.md) §3 fairness audit)

#### 1.5 Adversarial Robustness

- [ ] Agent resists prompt injection attempts (cross-reference: [Agent Security Policy](agent-security.md) §1)
- [ ] Agent does not leak system instructions when probed
- [ ] Agent maintains behavioral consistency under adversarial rephrasing of the same request
- [ ] Agent does not change its behavior when users claim elevated permissions

### 2. Eval Suite Structure

#### 2.1 Suite Organization

Each agent type must have an eval suite organized as follows:

```
org/agents/<layer>/<agent-type>/
├── evals/
│   ├── README.md                    ← Suite overview, run instructions
│   ├── correctness/                 ← Output correctness test cases
│   ├── instruction-following/       ← Boundary and compliance test cases
│   ├── tool-calls/                  ← Tool call sequence and parameter tests
│   ├── decisions/                   ← Decision quality and escalation tests
│   ├── adversarial/                 ← Prompt injection and robustness tests
│   └── regression/                  ← Known-good cases from past failures
```

#### 2.2 Test Case Format

Each test case must include:

- **Input** — The prompt, context, or scenario presented to the agent
- **Expected behavior** — What the agent should do (not just what it should say) — including expected tool calls, decisions, escalations
- **Grading criteria** — How the output is evaluated (exact match, semantic similarity, behavioral checklist, human review)
- **Risk tier tag** — Which AI governance risk tier this test case exercises
- **Policy tag** — Which quality policies this test case validates

#### 2.3 Grading Methods

Eval suites must use at least one of these grading approaches (higher-risk tiers require more):

| Method | Description | Required for |
|--------|-------------|-------------|
| **Deterministic** | Exact match, regex, structured output validation | All tiers |
| **LLM-as-judge** | A separate LLM evaluates the output against rubric | Tier 1–2 |
| **Human review** | Human evaluator scores a sample of outputs | Tier 1 |
| **Behavioral** | Assert on tool calls made, decisions taken, escalations triggered (not just text output) | All tiers |

### 3. When to Run Evals

#### 3.1 CI/CD Gate (Blocking)

Evals must run and pass as a blocking CI gate for:

- [ ] Any change to agent instruction files (`AGENT.md`, `DIVISION.md`, agent type definitions)
- [ ] Any change to quality policies in `org/4-quality/policies/`
- [ ] Any model version change in fleet configurations
- [ ] Any change to tool integrations used by agents

#### 3.2 Scheduled (Monitoring)

Evals must run on a recurring schedule to detect drift:

| Agent Risk Tier | Scheduled Eval Cadence |
|----------------|----------------------|
| Tier 1 (High-Risk) | Weekly |
| Tier 2 (Limited-Risk) | Bi-weekly |
| Tier 3 (Minimal-Risk) | Monthly |

#### 3.3 Triggered (Reactive)

Evals must run in response to:

- Post-incident review identifies agent behavioral failure
- Observability platform detects anomalous agent behavior (automated signal)
- Human reports unexpected agent output or decision
- Model provider announces capability changes

### 4. Regression Management

#### 4.1 Regression Test Lifecycle

- Every agent behavioral bug that reaches production must produce a regression test case
- Regression tests are added to `evals/regression/` with a link to the originating incident, signal, or retrospective
- Regression tests are never deleted — they are the institutional memory of past failures
- Regression suites are cumulative: they grow as the agent encounters new edge cases

#### 4.2 Regression Detection

- Scheduled eval runs compare current results to the last known-good baseline
- Any test case that previously passed and now fails is flagged as a regression
- Regressions block deployment regardless of aggregate pass rate
- Regression alerts include: test case, expected vs. actual behavior, last passing run, suspected cause (model change, instruction change, etc.)

### 5. Eval Tooling

#### 5.1 Governed Tool Choices

The framework does not mandate a specific eval tool. Recommended options include:

| Tool | Best For | Integration Pattern |
|------|----------|-------------------|
| [Braintrust](https://www.braintrust.dev/) | Structured evals with LLM-as-judge, dataset management, regression tracking | API-based, CI-friendly |
| [PromptFoo](https://www.promptfoo.dev/) | Red-teaming, adversarial testing, multi-provider comparison | CLI-based, CI-friendly |
| [LangSmith](https://www.langchain.com/langsmith) | Trace-based evaluation, dataset curation from production traces | LangChain ecosystem |
| [Inspect AI](https://inspect.ai-safety-institute.org.uk/) | Safety evaluations, agent task benchmarks | Open-source, UK AISI |
| Custom scripts | Simple deterministic checks, tool call assertions | Direct, no dependencies |

#### 5.2 Tool Integration Requirements

Whichever tool is used, it must:

- [ ] Produce machine-readable results (JSON, JSONL, or structured output)
- [ ] Integrate with CI/CD as a blocking gate
- [ ] Support test case versioning (test cases are governed artifacts — tracked in Git)
- [ ] Produce telemetry exportable to the observability platform

### 6. Observability Integration

#### 6.1 Eval Telemetry

Every eval run must produce OpenTelemetry spans:

- **`eval.suite.run`** span — covers the entire eval suite execution
  - Attributes: `eval.suite.name`, `eval.agent_type`, `eval.risk_tier`, `eval.trigger` (ci/scheduled/manual), `eval.total_cases`, `eval.passed`, `eval.failed`, `eval.regressions`
- **`eval.case.run`** child span — covers each individual test case
  - Attributes: `eval.case.name`, `eval.case.category` (correctness/instruction-following/tool-calls/decisions/adversarial/regression), `eval.case.result` (pass/fail/error), `eval.case.grading_method`
- **`eval.regression.detected`** span event — emitted when a regression is found
  - Attributes: `eval.case.name`, `eval.last_pass_date`, `eval.suspected_cause`

#### 6.2 Dashboards and Alerts

- **Eval results dashboard** per agent type — pass rate trends, regression count, category breakdown
- **Fleet-wide eval health** — aggregate pass rates across all agent types, trend over time
- **Regression alert** — fires when any eval suite detects a regression (P2 severity — pages on-call)
- **Drift alert** — fires when scheduled eval pass rate drops below configurable threshold (default: 95%)
- **Coverage alert** — fires when an agent type has no eval suite or has not run evals within its scheduled cadence

#### 6.3 Eval Data as Risk Signal

Eval results feed the risk management loop:

- Declining eval pass rates produce automated signals in `work/signals/`
- Regression patterns across multiple agent types may indicate systemic issues (model degradation, instruction conflict, integration failure)
- Eval pass rate is a Key Risk Indicator (KRI) — see [Risk Management Policy](risk-management.md) §8

### 7. Deployment-Customizable Decisions

**What must be customized per deployment:**
- Eval tool selection and configuration
- Specific test cases for company-specific agent types
- Pass rate thresholds
- Scheduled eval cadence (within minimums above)
- Grading rubrics for LLM-as-judge evaluations
- Dashboard and alert routing

**What must not be customized away:**
- Eval-as-CI-gate for instruction/model changes (§3.1)
- Regression test requirement for production bugs (§4.1)
- Behavioral evaluation dimensions (§1 — all five dimensions)
- Eval telemetry emission (§6.1)
- Scheduled eval cadence minimums (§3.2)

---

## Evaluation Criteria

Quality Layer eval agents check agent types against this policy using these criteria:

| Criterion | PASS | FAIL |
|-----------|------|------|
| Eval suite exists | Agent type has `evals/` directory with test cases | No eval suite for this agent type |
| Eval dimensions covered | All 5 dimensions (§1.1–1.5) have at least one test case | Missing dimension coverage |
| CI gate configured | Instruction/model changes trigger eval run | Changes can ship without eval |
| Regression tests present | Known failures have corresponding regression tests | Production bugs without regression tests |
| Scheduled evals running | Evals run within cadence for agent risk tier | Overdue scheduled eval |
| Eval telemetry emitted | Eval runs produce `eval.suite.run` spans | Silent eval runs |
| Pass rate above threshold | >= configurable threshold (default 95%) | Below threshold |

---

## Cross-Policy Alignment

| Policy | Relationship |
|--------|-------------|
| [AI Governance](ai-governance.md) | Risk tier classification determines eval rigor; fairness audit informs decision quality tests |
| [Agent Security](agent-security.md) | Adversarial robustness evals extend security testing requirements |
| [Risk Management](risk-management.md) | Eval pass rate is a KRI; declining evals produce risk signals |
| [Observability](observability.md) | Eval telemetry follows OTel conventions; eval dashboards per agent type |
| [Delivery](delivery.md) | Evals are a pre-deployment gate alongside other quality checks |
| [Security](security.md) | Security test cases complement eval adversarial dimension |

---

## Compliance Mapping

| Framework | Requirement | How This Policy Addresses It |
|-----------|-------------|------------------------------|
| **ISO 42001:2023** | 9.1 (Monitoring, measurement, analysis) | Eval suites provide continuous measurement of AI system behavior |
| **ISO 42001:2023** | 8.4 (Data for AI — validation) | Test cases serve as validation datasets for agent behavior |
| **NIST AI RMF** | MEASURE 1 (Metrics for AI risk) | Eval pass rates, regression counts, and drift are quantitative risk metrics |
| **NIST AI RMF** | MEASURE 2 (Trustworthiness evaluation) | Behavioral evals assess correctness, fairness, robustness, and transparency |
| **NIST AI RMF** | MEASURE 3 (Emergent risk tracking) | Regression detection and drift alerts surface emergent behavioral risks |
| **EU AI Act** | Art. 9 (Risk management — testing) | Eval suites fulfill continuous testing obligations for high-risk AI |
| **EU AI Act** | Art. 15 (Accuracy, robustness) | Correctness and adversarial eval dimensions directly measure accuracy and robustness |
| **SOC 2** | CC5.1 (Control activities) | Evals are control activities verifying agent behavior matches policy |

---

## References

- [NIST AI 100-1 — AI RMF](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) — MEASURE function for AI risk quantification
- [NIST AI 600-1 — Generative AI Profile](https://airc.nist.gov/Docs/1) — GenAI-specific evaluation guidance
- [EU AI Act Art. 9, 15](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — Testing and accuracy requirements
- [OWASP LLM Top 10 (2025)](https://genai.owasp.org/llm-top-10/) — Adversarial test categories
- [Braintrust Eval Guide](https://www.braintrust.dev/docs/guides/evals) — Eval best practices
- [PromptFoo Red Teaming](https://www.promptfoo.dev/docs/red-team/) — Adversarial testing framework
- [Inspect AI](https://inspect.ai-safety-institute.org.uk/) — UK AI Safety Institute eval framework

---

## Related Issues

- [#74](https://github.com/wlfghdr/agentic-enterprise/issues/74) — Original issue requesting this policy
- [#111](https://github.com/wlfghdr/agentic-enterprise/issues/111) — Policy structure validation script (validates this policy's structure)
- [#112](https://github.com/wlfghdr/agentic-enterprise/issues/112) — Agent instruction validation (validates agent types have eval suites)
- [#115](https://github.com/wlfghdr/agentic-enterprise/issues/115) — OTel contract compliance (validates eval telemetry spans)
- [#116](https://github.com/wlfghdr/agentic-enterprise/issues/116) — Compliance mapping validation (validates this policy's compliance mapping)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-03-14 | Initial policy — eval scope, suite structure, CI gates, regression management, tooling, observability integration, compliance mapping |
