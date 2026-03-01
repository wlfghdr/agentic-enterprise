# Skill Manifests Registry

Each file in this directory is a **skill manifest** — a declarative, versioned definition of one capability an agent type may be granted.

## Schema

All manifests must conform to [`schemas/skill-manifest.schema.json`](../../schemas/skill-manifest.schema.json).

## Naming Convention

```
<skill-id>.skill.json
```

Example: `github-pr-review.skill.json`

## Lifecycle

1. Propose a new skill via PR — add a `.skill.json` file.
2. Steering Layer evaluates and approves.
3. Once merged, the skill becomes available for assignment in capability contracts.
4. Reference skills in agent type definitions (`org/agents/<layer>/<type>.md`) under `## Capabilities > Skills`.

## Index

| Skill ID | Category | Version | Description |
|---|---|---|---|
| `github-pr-review` | code-review | 1.0.0 | Review pull requests on GitHub repositories |
| `github-code-implementation` | code-generation | 1.0.0 | Implement code changes and open pull requests |
| `signal-triage` | signal-processing | 1.0.0 | Triage incoming signals and route to appropriate missions |
| `quality-evaluation` | evaluation | 1.0.0 | Evaluate artifacts against quality gates and policy |
| `mission-orchestration` | orchestration | 1.0.0 | Decompose missions and coordinate agent work |
