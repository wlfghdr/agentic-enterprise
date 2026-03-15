# Compliance Remediation Guides

> **Purpose:** Actionable guides and templates for closing high-priority compliance gaps identified in the [compliance reference docs](../README.md).

These guides are for **adopters deploying the framework** in a real environment. Each guide addresses a specific gap from the compliance reference documents and provides step-by-step remediation instructions.

## P0-Critical Guides

| Guide | Standard | Gap | Issue |
|-------|----------|-----|-------|
| [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md) | SOC 2 Type II | No runtime evidence for Type II audit | [#123](https://github.com/wlfghdr/agentic-enterprise/issues/123) |
| [NIST CSF Runtime Security Tooling](nist-csf-runtime-security-tooling.md) | NIST CSF 2.0 | No SIEM/IDS/IPS/EDR provisioned | [#133](https://github.com/wlfghdr/agentic-enterprise/issues/133) |
| [NIST CSF Network Security Architecture](nist-csf-network-security.md) | NIST CSF 2.0 | No network segmentation/firewall/monitoring | [#134](https://github.com/wlfghdr/agentic-enterprise/issues/134) |
| [EU AI Act Conformity Assessment](eu-ai-act-conformity-assessment.md) | EU AI Act | No conformity assessment procedure | [#129](https://github.com/wlfghdr/agentic-enterprise/issues/129) |
| [EU AI Act CE Marking & EU Database](eu-ai-act-ce-marking.md) | EU AI Act | No CE marking or EU database registration | [#130](https://github.com/wlfghdr/agentic-enterprise/issues/130) |

## SOC 2 Audit Readiness Guides

| Guide | Standard | Gap | Issue |
|-------|----------|-----|-------|
| [SOC 2 Operating Effectiveness Evidence](soc2-operating-effectiveness.md) | SOC 2 Type II | No runtime evidence for Type II audit | [#123](https://github.com/wlfghdr/agentic-enterprise/issues/123) |
| [SOC 2 Formal Control Testing Documentation](soc2-control-testing.md) | SOC 2 Type II | No formal control testing matrix, cadence, or result records | [#124](https://github.com/wlfghdr/agentic-enterprise/issues/124) |
| [SOC 2 CPA Audit Engagement](soc2-cpa-engagement.md) | SOC 2 Type II | No guidance on CPA-firm engagement, management assertion preparation, or auditor access coordination | [#125](https://github.com/wlfghdr/agentic-enterprise/issues/125) |

## ISO 27001 Core ISMS Templates

| Template | Standard | Gap | Issue |
|----------|----------|-----|-------|
| [ISMS Scope Statement](../templates/_TEMPLATE-isms-scope.md) | ISO 27001 Clause 4.3 | No formal ISMS scope definition | [#120](https://github.com/wlfghdr/agentic-enterprise/issues/120) |
| [Statement of Applicability](../templates/_TEMPLATE-soa.md) | ISO 27001 Clause 6.1.3d | No SoA listing all 93 Annex A controls | [#121](https://github.com/wlfghdr/agentic-enterprise/issues/121) |
| [Internal Audit Programme](../templates/_TEMPLATE-isms-internal-audit.md) | ISO 27001 Clause 9.2 | No audit programme or schedule | [#122](https://github.com/wlfghdr/agentic-enterprise/issues/122) |

## ISO 42001 Core AIMS Assets

| Resource | Standard | Gap | Issue |
|----------|----------|-----|-------|
| [AIMS Scope and AI System Inventory Guide](iso-42001-aims-scope.md) | ISO 42001 Clause 4.3 | No formal AIMS boundary definition or inventory guidance | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |
| [AIMS Scope Statement](../templates/_TEMPLATE-aims-scope.md) | ISO 42001 Clause 4.3 | No formal AIMS scope definition | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |
| [AI System Inventory](../templates/_TEMPLATE-ai-system-inventory.md) | ISO 42001 Clause 4 | No AI system inventory with risk classification | [#126](https://github.com/wlfghdr/agentic-enterprise/issues/126) |

## ISO 42001 Certification Guides

| Guide | Standard | Gap | Issue |
|-------|----------|-----|-------|
| [ISO 42001 Conformity Assessment Preparation](iso-42001-conformity-assessment.md) | ISO 42001 Clause 10 / certification | No guidance on third-party certification body process | [#127](https://github.com/wlfghdr/agentic-enterprise/issues/127) |

## How to Use These Guides

1. **Identify your deployment context** — which standards apply to your organization
2. **Follow the remediation steps** — each guide provides concrete actions, templates, and configuration examples
3. **Collect evidence** — use the evidence mapping to feed your audit preparation
4. **Validate** — use the verification checklist at the end of each guide to confirm gap closure
