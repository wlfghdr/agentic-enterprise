# SOC 2 Control Testing Matrix

> **Standard:** SOC 2 Type II — Trust Service Criteria
> **Purpose:** Define the full control population, testing cadence, and test procedures for SOC 2 readiness and audit support

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | SOC2-CTM-001 |
| Version | {{VERSION}} |
| Organization | {{ORGANIZATION_NAME}} |
| Audit period | {{AUDIT_PERIOD_START}} to {{AUDIT_PERIOD_END}} |
| Owner | {{CONTROL_TESTING_OWNER}} |
| Approved by | {{APPROVER}} |
| Review cycle | Quarterly (minimum) |
| Related | [SOC 2 Control Test Result Template](_TEMPLATE-soc2-control-test-result.md) |

## How to Use This Template

1. Expand the seeded control families below into the full deployment-specific control inventory.
2. Assign a unique `Control ID` and a named owner to each row.
3. Replace framework references with the actual deployed control implementation where needed.
4. Link each completed test to a result record created from `_TEMPLATE-soc2-control-test-result.md`.
5. Update this matrix whenever new systems, vendors, workflows, or control changes enter scope.

## Status Legend

| Status | Meaning |
|--------|---------|
| Planned | Control exists in scope but has not yet been tested in the current cycle |
| In progress | Test execution is underway |
| Pass | Latest test supports operating effectiveness |
| Pass with exception | Control largely operated but exceptions require remediation |
| Fail | Test failed or evidence was insufficient |
| Not applicable | Criterion not in scope for this deployment (justify separately) |

## Control Population

| Control ID | TSC | Control Objective | Framework Artifact / Policy | Deployment Implementation | Frequency | Test Method | Population / Sample Rule | Evidence Source | Control Owner | Tester | Latest Result Ref | Status |
|------------|-----|-------------------|-----------------------------|---------------------------|-----------|-------------|--------------------------|----------------|---------------|--------|-------------------|--------|
| CC1-001 | CC1 | Governance changes require appropriate approval and ownership handoff | `AGENTS.md`, `CODEOWNERS`, PR workflow | {{DEPLOYMENT_REFERENCE}} | Quarterly | Inspection + sampling | Sample merged PRs from each quarter; verify reviewer and assignee history | PR metadata, review history, issue/PR assignee trail | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC3-001 | CC3 | Risks are identified, scored, and reviewed on schedule | `org/4-quality/policies/risk-management.md` | {{DEPLOYMENT_REFERENCE}} | Quarterly | Inspection + inquiry | Sample open and recently updated risks; verify review dates and treatment | Risk register, review notes, alerts | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC5-001 | CC5 | Quality gates block non-compliant changes before merge | `.github/workflows/validate.yml`, policy checks workflow | {{DEPLOYMENT_REFERENCE}} | Per change + monthly review | Reperformance + inspection | Inspect one successful run per month plus failed runs with remediation | Workflow runs, logs, remediation issues | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC6-001 | CC6 | Access to governed changes and credentials is restricted appropriately | `CODEOWNERS`, branch protection, cryptography policy | {{DEPLOYMENT_REFERENCE}} | Monthly / quarterly | Inspection + observation | Review privileged users and recent access changes | Access roster, branch settings, KMS logs | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC7-001 | CC7 | Monitoring, log integrity, and incident handling operate effectively | observability + log retention controls | {{DEPLOYMENT_REFERENCE}} | Monthly | Inspection + requery | Review alerts, incidents, and log integrity evidence for the month | Dashboards, incident records, WORM verification | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC8-001 | CC8 | Changes follow approved workflow before deployment | PR workflow, delivery policy, release gates | {{DEPLOYMENT_REFERENCE}} | Monthly / quarterly | Sampling + inspection | Sample changes across the audit period; verify approval, checks, and release evidence | PRs, CI logs, deployment traces | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| CC9-001 | CC9 | Critical vendors are assessed and monitored on schedule | `org/4-quality/policies/vendor-risk-management.md` | {{DEPLOYMENT_REFERENCE}} | Quarterly / annual | Inspection | Review all Tier 1-2 vendors or sample by criticality if volume is high | Vendor assessments, attestations, SLA reports | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| A1-001 | A1 | Availability commitments are monitored and recovery readiness is tested | availability + observability controls | {{DEPLOYMENT_REFERENCE}} | Monthly + drill cadence | Inspection + observation | Review monthly SLOs and the latest drill / restore exercise | SLO dashboards, DR drill records, runbooks | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| PI1-001 | PI1 | Processing integrity controls detect malformed or incomplete changes | validation workflows, release checks | {{DEPLOYMENT_REFERENCE}} | Per change + monthly review | Reperformance + sampling | Re-run selected validators and inspect failed-change remediation | Workflow logs, defect records, deployment health | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| C1-001 | C1 | Confidential data is classified, encrypted, and access-controlled | data classification + cryptography policies | {{DEPLOYMENT_REFERENCE}} | Quarterly | Inspection | Sample sensitive stores and transmission paths | Classification evidence, encryption settings, KMS logs | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |
| P1-001 | P1-P8 | Privacy obligations are executed for in-scope personal information | privacy policy and DSAR / breach workflows | {{DEPLOYMENT_REFERENCE}} | Quarterly / upon event | Inspection + sampling | Review all DSARs / privacy incidents or sample by quarter | DSAR records, breach logs, retention evidence | {{OWNER}} | {{TESTER}} | {{RESULT_REF}} | Planned |

## Planned Test Calendar

| Quarter / Month | Controls Scheduled | Notes |
|-----------------|--------------------|-------|
| {{PERIOD_1}} | {{CONTROL_IDS}} | {{NOTES}} |
| {{PERIOD_2}} | {{CONTROL_IDS}} | {{NOTES}} |
| {{PERIOD_3}} | {{CONTROL_IDS}} | {{NOTES}} |

## Exception and Retest Tracking

| Control ID | Result Ref | Exception Summary | Severity | Remediation Owner | Target Date | Retest Ref | Status |
|------------|------------|-------------------|----------|-------------------|-------------|------------|--------|
| {{CONTROL_ID}} | {{RESULT_REF}} | {{EXCEPTION}} | {{SEVERITY}} | {{OWNER}} | {{DATE}} | {{RETEST_REF}} | Open / Closed |

## Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial control testing matrix |
