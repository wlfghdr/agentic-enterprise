# Fleet Configuration: [Mission Name]

> **Template version:** 1.0 | **Last updated:** 2026-02-19  
> **Configuration for agent fleet deployment on a specific mission.**  
> **Created by:** Orchestration Layer (Mission Lead + Agent Fleet Manager)

---

## Mission

| Field | Value |
|-------|-------|
| **Mission ID** | _(e.g., MISSION-2026-042)_ |
| **Mission brief** | [BRIEF.md](../../work/missions/<name>/BRIEF.md) |
| **Status** | active _(proposed / active / paused / completed)_ |

## Orchestration

| Role | Person |
|------|--------|
| **Mission Lead** | |
| **Fleet Manager** | |

## Streams

### Stream: [Stream Name]

| Field | Value |
|-------|-------|
| **Agent pool** | _(e.g., "implementation-agents")_ |
| **Division** | _(which division handles this stream)_ |
| **Exclusive** | yes _(if yes, no other stream may touch these paths)_ |

**Working paths:**
- _(file paths this stream owns)_

**Quality policies:**
- security
- architecture

**Human checkpoints:**

| Trigger | Who | Action |
|---------|-----|--------|
| _(e.g., "architecture_novelty_score > 0.7")_ | _(e.g., "Tech Lead")_ | _(e.g., "Review and approve pattern")_ |

**Success metrics:**

| Metric | Target | Measurement |
|--------|--------|-------------|
| _(e.g., "PR merge rate")_ | _(e.g., "> 90%")_ | _(e.g., "Git analytics")_ |

<!-- Copy the stream section above for additional streams -->

## Dependencies

| From | To | Type |
|------|----|------|
| _(stream name)_ | _(stream name)_ | _(blocks / informs / shared-resource)_ |

## Monitoring

| Parameter | Value |
|-----------|-------|
| **Quality threshold** | 0.8 _(minimum quality score before alert)_ |
| **Throughput alert** | _(alert if throughput drops below this)_ |
| **Escalation policy** | _(who gets notified on issues)_ |
---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-19 | Initial version |
