# Component Onboarding Checklist

> **Template version:** 1.0  
> **Component:** [component name]  
> **Type:** service | library | app | API | data-pipeline  
> **Division:** [owning division]  
> **Created:** YYYY-MM-DD

---

## Pre-Development

- [ ] Component registered in Software Catalog ({{SERVICE_CATALOG}})
- [ ] Repository created with standard structure
- [ ] CI/CD pipeline configured
- [ ] Code quality tool project created
- [ ] Team ownership assigned in Software Catalog

## Architecture

- [ ] API contract defined (OpenAPI / Proto / GraphQL schema)
- [ ] Architecture Decision Record created (if novel patterns)
- [ ] Dependencies identified and documented
- [ ] Data model documented
- [ ] Security threat model completed (for customer-facing components)

## Quality Setup

- [ ] Linting configured (language-appropriate)
- [ ] Test framework configured (unit, integration)
- [ ] Code coverage threshold set (≥ {{MIN_CODE_COVERAGE}})
- [ ] Security scanning configured
- [ ] Dependency vulnerability scanning configured

## Observability

> **Policy reference:** [../../org/4-quality/policies/observability.md](../../org/4-quality/policies/observability.md) — nothing ships without observability.

### Instrumentation (mandatory before first production deployment)
- [ ] At least one instrumentation source active and verified (OTel SDK, APM agent, or API ingest)
- [ ] Telemetry data verified in {{OBSERVABILITY_TOOL}} within 5 minutes of deployment
- [ ] Distributed tracing enabled with W3C Trace Context propagation
- [ ] Custom spans for business-critical operations
- [ ] Agent workflows produce spans for tool calls, LLM invocations, and decisions (if agent component)

### Metrics
- [ ] RED metrics on all endpoints (Rate, Errors, Duration — p50, p95, p99)
- [ ] Business metrics defined (feature adoption, workflow completion)
- [ ] Agent metrics: token consumption, tool call success/failure, decision latency (if agent component)

### Logs
- [ ] Structured logging configured (JSON with trace ID and span ID correlation)
- [ ] Log levels used correctly (ERROR = actionable, WARN = degraded, INFO = events, DEBUG = off in prod)
- [ ] No PII in logs (cross-ref: security policy)

### Health Targets & Alerting
- [ ] Availability target defined (≥ 99.5% unless justified)
- [ ] Latency target defined (per performance policy budgets)
- [ ] Health targets configured with appropriate alerts
- [ ] Health check endpoint implemented
- [ ] Custom alerts: health metric thresholds aligned with operational policies
- [ ] Every alert has a documented runbook action
- [ ] Alert definitions stored as code

### Dashboards
- [ ] Service health dashboard created in {{OBSERVABILITY_TOOL}} (key metrics, health target status, dependencies, deployments)
- [ ] Dashboard linked in Software Catalog entity metadata
- [ ] Alerts configured for health target violations

## Deployment

- [ ] Deployment pipeline configured
- [ ] Container image building configured
- [ ] Resource limits defined (CPU, memory)
- [ ] Environment variables documented
- [ ] Secrets configured in {{SECRETS_MANAGER}}
- [ ] Feature flag integration configured (if applicable)
- [ ] Progressive rollout plan defined

## Documentation

- [ ] README.md with setup instructions
- [ ] API documentation generated
- [ ] Architecture documentation in {{SERVICE_CATALOG}} TechDocs
- [ ] Runbook for on-call using `org/3-execution/divisions/_TEMPLATE/_TEMPLATE-runbook.md` (if service)
- [ ] Component onboarding entry in asset registry (`work/assets/<name>.md`)

## Post-Onboarding

- [ ] Deployed to staging environment
- [ ] Integration tests passing
- [ ] Performance baseline established
- [ ] On-call rotation configured (if service)
- [ ] Added to release train (if applicable)
