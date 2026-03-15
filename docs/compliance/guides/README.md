# Compliance Implementation Guides

> **Purpose:** Actionable guides and templates for implementing deployment-specific compliance requirements identified in the [compliance reference docs](../README.md).

These guides are for **adopters deploying the framework** in a real environment. Each guide addresses a specific requirement from the compliance reference documents and provides step-by-step implementation instructions.

## P0-Critical Guides

| Guide | Standard | Requirement | Issue |
|-------|----------|-------------|-------|
| [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md) | SOC 2 Type II | Runtime evidence collection for Type II audit | [#123](https://github.com/wlfghdr/agentic-enterprise/issues/123) |
| [NIST CSF Runtime Security Tooling](nist-csf-runtime-security-tooling.md) | NIST CSF 2.0 | SIEM/IDS/IPS/EDR provisioning | [#133](https://github.com/wlfghdr/agentic-enterprise/issues/133) |
| [NIST CSF Network Security Architecture](nist-csf-network-security.md) | NIST CSF 2.0 | Network segmentation, firewall, and monitoring | [#134](https://github.com/wlfghdr/agentic-enterprise/issues/134) |
| [EU AI Act Conformity Assessment](eu-ai-act-conformity-assessment.md) | EU AI Act | Conformity assessment procedure | [#129](https://github.com/wlfghdr/agentic-enterprise/issues/129) |
| [EU AI Act CE Marking & EU Database](eu-ai-act-ce-marking.md) | EU AI Act | CE marking and EU database registration | [#130](https://github.com/wlfghdr/agentic-enterprise/issues/130) |

## SOC 2 Audit Readiness Guides

| Guide | Standard | Requirement | Issue |
|-------|----------|-------------|-------|
| [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md) | SOC 2 Type II | Runtime evidence collection for Type II audit | [#123](https://github.com/wlfghdr/agentic-enterprise/issues/123) |
| [SOC 2 Formal Control Testing Documentation](soc2-control-testing.md) | SOC 2 Type II | Formal control testing matrix, cadence, and result records | [#124](https://github.com/wlfghdr/agentic-enterprise/issues/124) |
| [SOC 2 CPA Audit Engagement](soc2-cpa-engagement.md) | SOC 2 Type II | CPA-firm engagement, management assertion preparation, and auditor access coordination | [#125](https://github.com/wlfghdr/agentic-enterprise/issues/125) |

## NIST AI RMF Measurement Assets

| Resource | Standard | Requirement | Issue |
|----------|----------|-------------|-------|
| [NIST AI RMF Quantitative Measurement Guide](nist-ai-rmf-measure-metrics.md) | NIST AI RMF 1.0 | Standard metric catalog, baseline method, dashboard structure, and report format for MEASURE 1-4 | [#128](https://github.com/wlfghdr/agentic-enterprise/issues/128) |
| [NIST AI RMF MEASURE Dashboard Template](../templates/_TEMPLATE-nist-ai-rmf-measure-dashboard.md) | NIST AI RMF 1.0 | Reusable dashboard specification for AI risk quantification | [#128](https://github.com/wlfghdr/agentic-enterprise/issues/128) |
| [NIST AI RMF Measurement Report Template](../templates/_TEMPLATE-nist-ai-rmf-measure-report.md) | NIST AI RMF 1.0 | Reusable report format for periodic AI-risk measurement outputs | [#128](https://github.com/wlfghdr/agentic-enterprise/issues/128) |

## ISO 27001 Core ISMS Templates

| Template | Standard | Requirement | Issue |
|----------|----------|-------------|-------|
| [ISMS Scope Statement](../templates/_TEMPLATE-isms-scope.md) | ISO 27001 Clause 4.3 | Formal ISMS scope definition | [#120](https://github.com/wlfghdr/agentic-enterprise/issues/120) |
| [Statement of Applicability](../templates/_TEMPLATE-soa.md) | ISO 27001 Clause 6.1.3d | SoA listing all 93 Annex A controls | [#121](https://github.com/wlfghdr/agentic-enterprise/issues/121) |
| [Internal Audit Programme](../templates/_TEMPLATE-isms-internal-audit.md) | ISO 27001 Clause 9.2 | Audit programme and schedule | [#122](https://github.com/wlfghdr/agentic-enterprise/issues/122) |

## ISO 42001 Core AIMS Assets

| Resource | Standard | Requirement | Issue |
|----------|----------|-------------|-------|
| [AIMS Scope and AI System Inventory Guide](iso-42001-aims-scope.md) | ISO 42001 Clause 4.3 | Formal AIMS boundary definition and inventory | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |
| [AIMS Scope Statement](../templates/_TEMPLATE-aims-scope.md) | ISO 42001 Clause 4.3 | Formal AIMS scope definition | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |
| [AI System Inventory](../templates/_TEMPLATE-ai-system-inventory.md) | ISO 42001 Clause 4 | AI system inventory with risk classification | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |

## ISO 42001 Certification Guides

| Guide | Standard | Requirement | Issue |
|-------|----------|-------------|-------|
| [ISO 42001 Conformity Assessment Preparation](iso-42001-conformity-assessment.md) | ISO 42001 Clause 10 / certification | Third-party certification body process | [#127](https://github.com/wlfghdr/agentic-enterprise/issues/127) |

## How to Use These Guides

1. **Identify your deployment context** — which standards apply to your organization
2. **Follow the implementation steps** — each guide provides concrete actions, templates, and configuration examples
3. **Collect evidence** — use the evidence mapping to feed your audit preparation
4. **Validate** — use the verification checklist at the end of each guide to confirm readiness
