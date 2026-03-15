# End-to-End Loop Example

This folder demonstrates a complete lifecycle through the Agentic Enterprise operating model — from initial observation to shipped release and back to new observations.

## The Story

A customer-experience agent detects that 34% of new customers abandon onboarding at Step 3. This observation flows through the operating model and results in a fix that reduces drop-off to 16%.

## Files

Read them in order:

| File | Stage | What It Shows |
|------|-------|--------------|
| [signal.md](signal.md) | Discover | An observation filed as a structured signal |
| [mission.md](mission.md) | Decide | The signal converted to scoped work with clear outcomes |
| [work-items.md](work-items.md) | Build | Tasks decomposed and tracked through execution |
| [example-pr.md](example-pr.md) | Ship | A governed pull request with quality gates |
| [release.md](release.md) | Operate | Documented outcomes and new signals for the next loop |

## The Loop

```
signal.md          →  "We see a 34% drop-off"
mission.md         →  "We will fix it by simplifying Step 3"
work-items.md      →  "Here are the 8 tasks to get it done"
example-pr.md      →  "Here is the governed code change"
release.md         →  "Drop-off reduced to 16%. Mobile has same problem."
                   →  New signal filed → next mission begins
```

## Key Takeaways

1. **Every piece of work traces back to an observation.** Nothing is done "just because."
2. **Scope is explicit.** The mission says what's in and out of scope before work begins.
3. **PRs are governed.** CODEOWNERS defines reviewers. Quality policies are checked. CI enforces standards.
4. **Outcomes are measured.** The release records whether targets were actually met.
5. **The loop never stops.** Every release generates new observations that feed back into the system.
