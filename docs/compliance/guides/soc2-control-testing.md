<!-- placeholder-ok -->
# SOC 2 — Formal Control Testing Documentation Guide

> **Implements:** Formal control testing documentation
> **Standard:** SOC 2 Type II — Trust Service Criteria
> **Severity:** High — required before formal audit fieldwork
> **Related issue:** [#124](https://github.com/wlfghdr/agentic-enterprise/issues/124)
> **Related compliance doc:** [SOC 2 Compliance Reference](../soc2.md)
> **Companion guide:** [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md)

---

## 1. Purpose

The Agentic Enterprise framework provides the raw ingredients for SOC 2 testing:

- control design in the quality policies and governance model
- runtime evidence collection guidance in the [operating effectiveness guide](soc2-operating-effectiveness.md)
- CI/CD validations, policy-as-code checks, and Git-based approval trails

This guide provides the **formal documentation layer** that auditors expect when they ask, "Show me how you test each control, how often you test it, what evidence you reviewed, and how you tracked failures."

Adopters use this guide to build a repeatable control testing programme. It provides:

1. a control testing methodology
2. a reusable testing matrix template
3. a reusable test result template
4. a mapping from existing framework validations to SOC 2 control tests

Use this guide together with the [operating effectiveness evidence guide](soc2-operating-effectiveness.md):

- this guide explains **how to test controls**
- the companion guide explains **how to retain evidence over the observation period**

---

## 2. What Auditors Expect From Formal Control Testing

Formal control testing means more than keeping a spreadsheet of controls. At minimum, an auditor expects the organization to maintain the following documented information:

| Artifact | Purpose | Minimum Content |
|---------|---------|-----------------|
| **Control testing matrix** | Defines the full control population and how each control is tested | Control ID, TSC mapping, owner, frequency, test method, evidence source, tester |
| **Test procedures** | Makes the testing approach repeatable | Inspection steps, sample logic, expected result, failure criteria |
| **Test result records** | Proves testing actually occurred | Test date, population/sample, evidence reviewed, exceptions, conclusion |
| **Remediation tracker** | Shows failed tests were acted on | Exception description, severity, owner, due date, retest status |
| **Testing calendar** | Demonstrates planned intervals | Monthly / quarterly / annual schedule tied to control type |

If any of these are missing, the testing programme is usually treated as ad hoc rather than governed.

---

## 3. Control Testing Methodology

### 3.1 Build the Control Population

Start with the framework's SOC 2 control mapping in [soc2.md](../soc2.md). Convert the high-level criterion mapping into a deployment-specific control inventory. Each control in the inventory should answer:

- What is the control trying to prevent or detect?
- Which TSC criterion does it support?
- Who owns the control?
- Is it automated, manual, or hybrid?
- What evidence proves it operated effectively?

The [control testing matrix template](../templates/_TEMPLATE-soc2-control-testing-matrix.md) is the governed place to capture this inventory.

### 3.2 Classify Controls by Testing Method

Use the testing method that matches how the control actually works.

| Method | When to Use | Example in This Framework |
|--------|-------------|---------------------------|
| **Inspection** | Review documents, configuration, or system settings | Inspect `CODEOWNERS`, policy versions, branch protection screenshots |
| **Inquiry** | Confirm understanding of a process with the control owner | Interview the reviewer responsible for release approvals |
| **Observation** | Watch the control being performed | Observe an access review or incident drill |
| **Reperformance** | Re-run the control or recreate the test | Re-run a validation script against the current branch |
| **Data requery / sampling** | Pull a population and sample it | Review merged PRs for approval evidence and passing checks |

Auditors rarely accept inquiry alone. Prefer inspection, reperformance, or data requery wherever possible.

### 3.3 Set Minimum Testing Frequency by Control Category

Frequency should be risk-based, but the table below provides a strong default baseline for this framework.

| Control Category | Typical Examples | Minimum Frequency | Notes |
|------------------|------------------|-------------------|-------|
| **Governance and oversight** | CODEOWNERS reviews, policy approval flows, risk review cadence | Quarterly | Increase if governance exceptions or process bypasses occur |
| **Automated SDLC / CI controls** | schema validation, content security scanning, policy-as-code checks | Per change + monthly summary review | Automated controls should also have periodic reviewer validation |
| **Access and change management** | branch protection, reviewer approvals, credential rotation evidence | Monthly or quarterly | Higher cadence if privileged access changes frequently |
| **Operations and monitoring** | alerting, incident handling, log integrity, SLO monitoring | Monthly | Evidence should span the full observation period |
| **Vendor and privacy controls** | vendor attestations, DPA checks, DSAR workflow | Quarterly or upon material change | Also retest after vendor scope changes |
| **Resilience and recovery** | DR drills, backup restores, rollback tests | Quarterly or annual, depending on risk | Retain drill outputs and follow-up actions |

### 3.4 Define Sampling Rules Up Front

Sampling rules should be written before testing starts. This prevents cherry-picking.

Recommended default sampling rules:

- **Automated controls that run on every change:** inspect one successful run from each month in the audit period plus any failed run that triggered remediation
- **Manual quarterly controls:** inspect all occurrences if the population is small; otherwise sample at least one occurrence per quarter
- **Recurring approvals:** sample enough items to cover different reviewers, systems, and months in the period under review
- **Exception handling controls:** test all exceptions, because the population should be small and each exception is high-signal

If an auditor or CPA firm provides stricter sample guidance, follow that instead.

---

## 4. How to Use the Control Testing Matrix

Instantiate the [SOC 2 control testing matrix template](../templates/_TEMPLATE-soc2-control-testing-matrix.md) as a deployment artifact, for example:

- `docs/compliance/soc2-control-testing-matrix.md`
- `work/assets/soc2-control-testing-matrix.md`

The matrix should be the master index for the testing programme. Each row represents one control or one independently testable control family.

### 4.1 Required Columns

At minimum, keep these fields for every row:

- control ID
- trust service criterion
- control objective
- framework artifact or policy
- deployment implementation reference
- testing frequency
- test method
- evidence source
- control owner
- tester
- latest result reference

### 4.2 Example TSC-to-Test Mapping

The template is pre-seeded with a starter mapping. Expand it to match the actual deployment.

| TSC | Example Control Family | Suggested Procedure |
|-----|------------------------|---------------------|
| **CC1** | Governance and approval boundaries | Sample merged PRs and verify required reviewer approval and correct assignee handoff |
| **CC3** | Risk assessment process | Inspect risk register entries and confirm review cadence matches policy |
| **CC5** | Quality gates | Reperform CI validations and inspect failed-run remediation |
| **CC6** | Access control | Inspect privileged access roster, credential rotation records, and branch protection settings |
| **CC7** | Monitoring and incident response | Inspect alerting configuration, incident timelines, and immutable log settings |
| **CC8** | Change management | Sample deployments and confirm linked PR approval, green checks, and rollback readiness |
| **CC9** | Vendor oversight | Inspect vendor assessments, attestation currency, and review cadence |
| **A1** | Availability commitments | Inspect SLO reporting, capacity thresholds, and DR drill evidence |
| **PI1** | Processing integrity | Inspect validation results, deployment health checks, and defect remediation |
| **C1** | Confidentiality | Inspect data classification enforcement and encryption verification outputs |
| **P1-P8** | Privacy operations | Inspect DSAR, breach handling, consent, and retention evidence as applicable |

---

## 5. Mapping Existing CI/CD Validations to SOC 2 Control Tests

The framework already includes a meaningful automated control surface. These checks can serve as part of formal control testing when they are documented in the matrix and paired with retained evidence.

### 5.1 Validate Framework Workflow

| Workflow / Check | Primary TSC Coverage | How to Test It | Evidence to Retain |
|------------------|----------------------|----------------|--------------------|
| `validate-yaml` | PI1, CC8 | Reperform on a recent change set and confirm malformed YAML does not merge | Workflow run logs and remediation for any failures |
| `validate-markdown` | PI1, CC5 | Inspect a sample of successful runs and one failed run if available | Workflow logs showing broken-link detection and correction |
| `validate-placeholders` | PI1, CC5 | Reperform and confirm non-template docs do not ship unresolved placeholders | Workflow logs and corrected commit references |
| `validate-versioning` | CC2, CC8 | Inspect governed-file changes and verify version/date enforcement triggered | Workflow logs plus diff showing updated metadata |
| `validate-github-governance` | CC1, CC6, CC8 | Inspect advisory output and pair it with direct verification of CODEOWNERS and branch protection settings | Advisory run logs plus GitHub settings evidence |
| `validate-schema` | PI1, CC5 | Reperform against `CONFIG.yaml` and governed schemas | Workflow logs and schema validation outputs |
| `validate-content-security` | CC5, CC7 | Reperform to confirm prompt-injection and unsafe-content patterns are blocked | Workflow logs and any approved suppression rationale |
| `validate-policy-structure` | CC5 | Inspect that policy metadata and cross-policy references remain complete | Workflow run logs |
| `validate-otel-contract` | CC7, PI1 | Reperform and confirm telemetry-linked artifacts reference the canonical contract | Workflow logs |
| `validate-compliance-mapping` | CC5, PI1 | Reperform and confirm policy mappings remain structurally valid | Workflow logs |
| `validate-integration-registry` | CC7, CC9 | Reperform and confirm observability integrations remain structurally complete | Workflow logs |
| `validate-agent-instructions` | CC1, CC5 | Reperform and verify hierarchy and boundary enforcement | Workflow logs |
| `validate-work-artifacts` | CC2, PI1 | Inspect run results for structured artifact compliance | Workflow logs |
| `validate-cross-references` | PI1, CC8 | Reperform and confirm references between governed artifacts resolve | Workflow logs |

### 5.2 Policy-as-Code Workflow

| Workflow / Check | Primary TSC Coverage | How to Test It | Evidence to Retain |
|------------------|----------------------|----------------|--------------------|
| `Policy Checks (OPA/Conftest)` | CC5, CC7, CC8 | Reperform against workflow definitions and inspect deny/warn outputs | Conftest run logs and remediation for policy violations |

### 5.3 Important Limitation

Automated validations are strong evidence, but they do **not** replace all manual control testing. They prove that certain detective or preventive controls executed. They do not, by themselves, prove:

- that branch protection is configured in GitHub correctly
- that reviewers were actually independent where required
- that vendor evidence was current and interpreted correctly
- that exception handling followed policy after a failure

Treat CI/CD controls as one layer of the testing programme, not the entire programme.

---

## 6. How to Document Test Results

Use the [SOC 2 control test result template](../templates/_TEMPLATE-soc2-control-test-result.md) for every executed test. Instantiate it into a stable location such as:

- `docs/compliance/testing-results/`
- `work/assets/soc2-testing-results/`

Each test result should capture:

- the control being tested
- the period under review
- the exact sample or population tested
- the evidence reviewed
- step-by-step procedure execution notes
- whether the test passed, failed, or passed with exceptions

### 6.1 Result Rating Guidance

| Result | Meaning | Required Follow-up |
|--------|---------|--------------------|
| **Pass** | Control operated as designed with no exceptions | Retain evidence and continue normal cadence |
| **Pass with exception** | Control operated, but one or more exceptions were found that do not invalidate the control overall | Track remediation and consider expanded sampling |
| **Fail** | Control did not operate effectively, or evidence is insufficient to support operation | Immediate remediation plan, owner assignment, and retest |
| **Not tested** | Planned test not executed | Record reason and reschedule promptly |

### 6.2 Exception Handling

Every failed test or meaningful exception should be linked to a remediation record. Good options in this framework include:

- a tracked issue in GitHub
- a risk entry using [work/decisions/_TEMPLATE-risk-register.md](../../../work/decisions/_TEMPLATE-risk-register.md) when the exception raises ongoing risk
- a retrospective if the exception caused a production incident

Do not overwrite failed results. File a new retest record after remediation.

---

## 7. Recommended Testing Calendar

The table below is a practical default cadence for the framework's control set.

| Month / Quarter | Activity |
|-----------------|----------|
| **Monthly** | Review automated CI/CD controls, monitoring alerts, and any failed exceptions that need retest |
| **Quarterly** | Test governance, access, vendor, and privacy controls; update sampling across the observation period |
| **Semi-annually** | Reassess testing coverage and adjust the matrix for new systems, integrations, or scope changes |
| **Annually** | Perform full control testing refresh, readiness review, and align with the CPA firm's expected audit window |
| **Upon significant change** | Add or retest controls after new integrations, policy changes, major incidents, or control failures |

If the organization changes scope mid-year, revise the matrix immediately. Waiting until the next annual cycle creates uncovered areas.

---

## 8. Verification Checklist

Use this checklist before calling the control testing programme audit-ready.

- [ ] A control testing matrix exists and covers every in-scope TSC criterion
- [ ] Every matrix row defines frequency, method, evidence source, owner, and tester
- [ ] Existing CI/CD validations are explicitly mapped where they act as control tests
- [ ] Test result records exist for executed tests and are linked from the matrix
- [ ] Sampling rules are documented before testing begins
- [ ] Exceptions are tracked with owners and target dates
- [ ] Failed tests are retested with a new result record after remediation
- [ ] Testing cadence aligns to the control risk level and audit period
- [ ] The testing programme is used together with the [operating effectiveness guide](soc2-operating-effectiveness.md) so evidence retention spans the full observation window

---

## References

- [SOC 2 Compliance Reference](../soc2.md)
- [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md)
- [SOC 2 Control Testing Matrix Template](../templates/_TEMPLATE-soc2-control-testing-matrix.md)
- [SOC 2 Control Test Result Template](../templates/_TEMPLATE-soc2-control-test-result.md)
- [Delivery Policy](../../../org/4-quality/policies/delivery.md)
- [Observability Policy](../../../org/4-quality/policies/observability.md)
- [Log Retention Policy](../../../org/4-quality/policies/log-retention.md)
- [Vendor Risk Management Policy](../../../org/4-quality/policies/vendor-risk-management.md)
- [Risk Management Policy](../../../org/4-quality/policies/risk-management.md)
