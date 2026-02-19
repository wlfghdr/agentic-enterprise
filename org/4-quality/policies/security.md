# Security Policy

> **Applies to:** All code, infrastructure configuration, API definitions, data pipelines, integrations
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team
> **Version:** 1.0 | **Last updated:** 2026-02-19

---

## Principles

1. **Zero Trust** — No implicit trust between services. All communication authenticated and authorized.
2. **Least Privilege** — Components and agents receive minimum required permissions.
3. **Defense in Depth** — Multiple independent security controls at every layer.
4. **Shift Left** — Security analysis in development, not after deployment.

## Mandatory Requirements

### Authentication & Authorization
- [ ] All service-to-service communication uses mutual TLS or equivalent
- [ ] All API endpoints require authentication (no anonymous access in production)
- [ ] Authorization checks at service boundary, not just at API gateway
- [ ] Token lifetimes follow organizational policy (short-lived preferred)

### Secrets Management
- [ ] No secrets in source code, environment variables in code, or configuration files in repositories
- [ ] All secrets stored in {{SECRETS_MANAGER}}
- [ ] Secret rotation procedures documented and automated
- [ ] Secrets referenced by name, never by value

### Input Validation
- [ ] All external input validated and sanitized
- [ ] Input length limits enforced
- [ ] Content-type validation on all API endpoints
- [ ] SQL injection prevention (parameterized queries only)
- [ ] XSS prevention (output encoding)

### Data Protection
- [ ] PII identified and classified
- [ ] Encryption at rest for sensitive data
- [ ] Encryption in transit (TLS 1.2+ minimum)
- [ ] Data retention policies defined and enforced
- [ ] Audit logging for access to sensitive data

### Dependency Security
- [ ] Dependencies scanned for known vulnerabilities
- [ ] No critical or high vulnerabilities in production dependencies
- [ ] Dependency update cadence defined (e.g., weekly automated PRs)
- [ ] License compliance checked (no copyleft in proprietary code unless approved)

### Container & Infrastructure Security
- [ ] Container images use minimal base images
- [ ] Containers run as non-root user
- [ ] No unnecessary ports exposed
- [ ] Resource limits defined (CPU, memory)
- [ ] Infrastructure as Code scanned for misconfigurations

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Secrets in code | None found | Any secret in source |
| Known vulnerabilities | No critical/high | Any critical/high |
| Authentication | All endpoints secured | Any anonymous production endpoint |
| Input validation | All external input validated | Unvalidated external input |
| Data classification | PII identified and protected | Unclassified PII |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
