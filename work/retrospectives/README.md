# Retrospectives

Postmortems, incident reports, and blameless retrospectives from production operations. These artifacts capture learnings from incidents and feed high-quality signals back into the Discover loop.

## How to Create a Postmortem

1. Use the template: `process/templates/postmortem.md`
2. Name the file: `YYYY-MM-DD-<incident-name>.md`
3. Submit as a Pull Request

## Naming Convention

- `YYYY-MM-DD-<descriptive-incident-name>.md`

## When to Create

- After any P1/P2 incident resolution
- After any incident where the root cause reveals a systemic issue
- After chaos engineering experiments that reveal resilience gaps
- After any production event that generates ≥3 improvement signals

## Who Creates

- Operate Loop agents (draft)
- On-call engineers + Reliability Policy Authors (review and finalize)

## Feedback Loop

Every postmortem should generate:
- At least one improvement signal in `work/signals/`
- Policy update recommendations (if gaps were found)
- Runbook updates (if existing runbooks were insufficient)
