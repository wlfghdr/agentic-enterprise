# Security Policy

## Scope

This repository is an **operating-model framework** (Markdown + YAML), not a
runtime platform. Security issues can still exist in:

- Agent instruction design (`AGENTS.md`, layer `AGENT.md`, division `DIVISION.md`)
- Governance and approval boundaries (`CODEOWNERS`, workflow rules)
- Quality policy gaps (`org/4-quality/policies/`)
- CI validation logic (`.github/workflows/`)
- Documentation that could mislead unsafe operational use

## Supported Versions

| Version | Supported |
|---------|-----------|
| `main`  | ✅ Yes |

## Reporting a Vulnerability

Please do **not** open a public issue for suspected vulnerabilities.

Report privately via GitHub Security Advisories:
- Go to: `Security` tab → `Report a vulnerability`
- Include: affected files, risk description, proof-of-concept, mitigation ideas

If Security Advisories are unavailable, contact maintainers directly at:
`wulf.ai.m@gmail.com`

## What to Include in Reports

Provide as much detail as possible:

1. **Summary**: What is the vulnerability?
2. **Impact**: What could happen if exploited?
3. **Affected files**: Paths and sections involved
4. **Reproduction steps**: Minimal reproducible scenario
5. **Suggested remediation**: If known

## Response Targets

- **Initial triage**: within 3 business days
- **Status update**: within 7 business days
- **Fix timeline**: based on severity and maintainer availability

## Severity Guidance

We prioritize issues that may cause:

- Privilege escalation through governance misconfiguration
- Unsafe automation recommendations in policies/instructions
- Approval bypass patterns in process documentation
- Misleading security guidance that could harm production usage

## Disclosure Policy

- We follow responsible disclosure.
- Please allow maintainers time to investigate and patch before public disclosure.
- We will credit reporters unless anonymity is requested.

## Hardening Recommendations for Adopters

For production use in your fork:

- Enforce protected branches + CODEOWNERS reviews
- Add mandatory status checks for policy validation
- Use signed commits for privileged branches
- Run periodic audits of agent instructions and quality policies
- Integrate policy-as-code checks (e.g., OPA/Rego) in CI
