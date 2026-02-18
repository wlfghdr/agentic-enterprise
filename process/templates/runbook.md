# Runbook: [Service/Component] — [Alert/Scenario Name]

> **Template version:** 1.0  
> **Service/Component:** [component name]  
> **Division:** [owning division]  
> **Alert name:** [alert that triggers this runbook, if applicable]  
> **Severity:** SEV1 | SEV2 | SEV3 | SEV4  
> **Last updated:** YYYY-MM-DD  
> **Author:** [Execution Layer — Ops agent or on-call engineer]  
> **Storage:** Alongside component documentation (division convention)

---

## Overview

**What this runbook covers:** [One sentence — what scenario or alert does this address?]

**When to use this runbook:**
- [Trigger condition 1 — e.g., "Alert: high-error-rate-service-x fires"]
- [Trigger condition 2 — e.g., "Customer reports inability to log in"]

**Expected resolution time:** [e.g., "< 15 minutes for automated, < 30 minutes for manual"]

---

## Diagnosis

### Step 1: Verify the Alert

```
# Check if the alert condition is real (not a false positive)
[command or dashboard link to verify]
```

**Expected output:** [what you should see if the alert is genuine]  
**If false positive:** [how to determine it's false, what to do]

### Step 2: Assess Blast Radius

- [ ] Check which endpoints/services are affected: [dashboard link]
- [ ] Check customer impact: [metrics dashboard link]
- [ ] Check SLO burn rate: [SLO dashboard link]
- [ ] Determine severity:
  - **SEV1:** Multiple SLOs breached, significant customer impact → escalate immediately
  - **SEV2:** Single SLO breached, limited impact → proceed with remediation
  - **SEV3:** Anomaly, no SLO breach → investigate and remediate
  - **SEV4:** Informational → log and monitor

### Step 3: Identify Root Cause

| Symptom | Likely Cause | Verification |
|---------|-------------|-------------|
| [symptom 1] | [probable cause] | [how to confirm — command, dashboard, log query] |
| [symptom 2] | [probable cause] | [how to confirm] |
| [symptom 3] | [probable cause] | [how to confirm] |

---

## Remediation

### Option A: [Primary Remediation — e.g., "Restart Service"]

```
# Step-by-step commands
[command 1]
[command 2]
```

**Expected result:** [what should happen after remediation]  
**Verification:** [how to confirm the fix worked]

### Option B: [Fallback — e.g., "Rollback to Previous Version"]

```
# Rollback commands
[command 1]
[command 2]
```

**Expected result:** [what should happen after rollback]  
**Verification:** [how to confirm]

### Option C: [Emergency — e.g., "Feature Flag Kill Switch"]

```
# Kill switch commands
[command 1]
```

**When to use:** [only if Options A and B fail, or if severity requires immediate action]

---

## Escalation

| Condition | Escalate To | Contact Method |
|-----------|------------|---------------|
| Remediation fails after [N] attempts | [on-call engineer] | [pager / Slack / phone] |
| Customer-visible impact > [N] minutes | [Reliability Policy Author] | [pager / Slack] |
| Data integrity concern | [Tech Lead + Security Policy Author] | [pager / Slack / phone] |
| Unable to determine root cause within [N] minutes | [Tech Lead] | [Slack] |

---

## Verification

After remediation, verify full recovery:

- [ ] Error rate returned to baseline: [dashboard link]
- [ ] Latency returned to baseline: [dashboard link]
- [ ] SLO burn rate normalized: [dashboard link]
- [ ] No cascading failures in dependent services: [dashboard link]
- [ ] Smoke tests passing: [test command or link]

---

## Post-Incident

- [ ] Log the incident with timeline and remediation steps taken
- [ ] If SEV1/SEV2: create a postmortem using `process/templates/postmortem.md`
- [ ] If runbook was inadequate: update this runbook and file an improvement signal
- [ ] If a new failure mode was encountered: file a signal in `work/signals/`

---

## Related Resources

- **Service dashboard:** [link]
- **SLO configuration:** [link]
- **Architecture decision:** [link to relevant decision record]
- **Related runbooks:** [links to related runbooks for dependent services]
- **On-call rotation:** [link to on-call schedule]
