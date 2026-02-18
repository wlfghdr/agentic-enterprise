## What does this PR do?

<!-- A clear, concise description of the change. -->

## Why?

<!-- Link to issue, discussion, or signal that motivated this change. -->

Closes #

## Type of Change

<!-- Check all that apply -->

- [ ] 🏗️ Framework improvement (layers, loops, hierarchy, model)
- [ ] 📋 Template (new or improved)
- [ ] 📜 Quality policy (new or refined)
- [ ] 🤖 Agent instructions (new agent type, division, or instruction update)
- [ ] 🔌 Runtime integration (bootstrap prompt, code sample, skill config)
- [ ] 🔧 Tooling / CI (GitHub Actions, validators, linters)
- [ ] 📖 Documentation (README, guides, examples)
- [ ] 🐛 Bug fix (broken link, YAML error, inconsistency)

## Changed Files

<!-- List key files affected. Helps reviewers understand scope. -->

| File | Change |
|------|--------|
| `path/to/file` | Description |

## Validation

<!-- How did you verify your change? -->

- [ ] YAML files parse without errors (`python3 -c "import yaml; yaml.safe_load(open('CONFIG.yaml'))"`)
- [ ] No broken internal links
- [ ] No unfilled `{{PLACEHOLDER}}` markers in non-template files
- [ ] Follows [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
- [ ] Maintains instruction hierarchy (AGENTS.md > layer AGENT.md > division AGENT.md)
- [ ] Does not introduce contradictions with existing policies

## Framework vs. Fork

<!-- Confirm this belongs in the upstream repo -->

- [ ] This is a **framework improvement** (not company-specific customization)
- [ ] I have read [CONTRIBUTING.md](../CONTRIBUTING.md)

## Additional Context

<!-- Screenshots, diagrams, links to discussions, or anything else helpful. -->
