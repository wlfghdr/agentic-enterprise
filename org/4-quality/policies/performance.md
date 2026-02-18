# Performance Policy

> **Applies to:** All services, APIs, data pipelines, and user-facing applications  
> **Enforced by:** Quality Layer eval agents  
> **Authority:** Engineering leads

---

## Principles

1. **Measure first** — No optimization without data.
2. **Budget-aware** — Every feature has a performance budget.
3. **Scale-tested** — Performance validated at expected production scale.
4. **Cost-conscious** — Resource consumption efficiency matters.

## Mandatory Requirements

### Service Performance
- [ ] API response times within SLO (p50, p95, p99 defined)
- [ ] No N+1 query patterns
- [ ] Database queries use appropriate indexes
- [ ] Connection pooling for all external dependencies
- [ ] Circuit breakers for external service calls
- [ ] Timeouts configured for all outbound requests

### Resource Efficiency
- [ ] CPU and memory limits defined per container/service
- [ ] No memory leaks (validated via load tests)
- [ ] Efficient serialization (avoid unnecessary data transformation)
- [ ] Batch operations where appropriate (not one-by-one)
- [ ] Caching strategy defined (what, where, TTL, invalidation)

### Scalability
- [ ] Services stateless or state externalized
- [ ] Horizontal scaling tested
- [ ] Load tested at {{LOAD_TEST_MULTIPLIER}}x expected production load
- [ ] Graceful degradation under overload (shed load, don't crash)
- [ ] Auto-scaling policies defined

### Monitoring & Alerting
- [ ] SLIs and SLOs defined for every service
- [ ] Dashboards for key metrics (latency, throughput, errors, saturation)
- [ ] Alerts configured for SLO violations
- [ ] Distributed tracing enabled
- [ ] Custom metrics for business-critical operations

### Cost Optimization
- [ ] Resource consumption profiled
- [ ] Cost per request/operation estimated
- [ ] No idle resources in production
- [ ] Right-sizing recommendations reviewed quarterly

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| SLO defined | All endpoints have SLOs | Missing SLO definitions |
| Load testing | Tested at target scale | No load test evidence |
| Resource limits | Defined and right-sized | Missing or unbounded |
| Monitoring | SLIs, dashboards, alerts | Missing observability |
| Query performance | Indexed, bounded | Unbounded or N+1 queries |
