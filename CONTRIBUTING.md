# Contributing to Agentic Enterprise

Thank you for your interest in improving this operating model! This guide covers how to contribute effectively — whether you're fixing a typo, proposing a new quality policy, or building a full runtime integration.

## What This Project Is

Agentic Enterprise is an **operating-model framework** — not a runtime, library, or SDK. Contributions are primarily Markdown and YAML files that define organizational structure, agent instructions, quality policies, and process guides.

The framework is **runtime-agnostic**. It works with any agent platform (OpenClaw, CrewAI, LangGraph, AutoGen, OpenAI Agents SDK, etc.) and any Git host (GitHub, GitLab, Bitbucket).

## Table of Contents

- [Quick Start](#quick-start)
- [Types of Contributions](#types-of-contributions)
- [Contribution Workflow](#contribution-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Architecture Decisions](#architecture-decisions)
- [Framework vs. Fork Customization](#framework-vs-fork-customization)
- [Development Setup](#development-setup)
- [Community](#community)
- [Recognition](#recognition)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Quick Start

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/agentic-enterprise.git
cd agentic-enterprise

# 2. Add the upstream remote
git remote add upstream https://github.com/wlfghdr/agentic-enterprise.git

# 3. Create a branch (use conventional naming)
git checkout -b feat/your-feature-name
# or: fix/broken-link, docs/improve-readme, policy/owasp-alignment

# 4. Make your changes (see contribution types below)

# 5. Validate locally (see Development Setup section below for full commands)
find . -name "*.yaml" | grep -v '.github/' | xargs -I{} python3 -c "import yaml; yaml.safe_load(open('{}'))" 2>&1

# 6. Commit with Conventional Commits
git commit -m "feat(quality): add OWASP-aligned security checks"

# 7. Push and open a Pull Request
git push origin feat/your-feature-name
# Then open a PR on GitHub — the PR template will guide you
```

## Types of Contributions

### Framework Contributions (core model)

Changes to the operating model itself — layer definitions, process loops, agent hierarchies.

- **Files:** `org/`, `process/`, `AGENTS.md`, `OPERATING-MODEL.md`
- **Requires:** Strong understanding of the 5-layer model and 4-loop process
- **Review:** Maintainers + community discussion recommended
- **Start with:** Open a [Discussion](https://github.com/wlfghdr/agentic-enterprise/discussions) first for significant changes

### Templates

New or improved templates for missions, decisions, signals, fleet configs, etc.

- **Files:** `work/*/`, `org/*/` (files prefixed with `_TEMPLATE`)
- **Guidelines:** Follow existing template conventions, include clear placeholder markers (`{{PLACEHOLDER}}`)
- **Test:** Verify the template works by filling it out with realistic example data

### Quality Policies

New or refined policies that govern agent output quality.

- **Files:** `org/4-quality/policies/`
- **Requirements:** Must be actionable and auditable — agents need to be able to evaluate compliance
- **Domains:** architecture, content, customer, delivery, experience, observability, performance, security
- **References:** Align with industry standards where applicable (OWASP, CIS, NIST, SLSA)

### Agent Instructions

Division-specific agent instructions, new agent type definitions, or improvements to existing ones.

- **Files:** `org/3-execution/divisions/*/`, `org/agents/`
- **Guidelines:** Follow the instruction hierarchy defined in `AGENTS.md`
- **Test:** Bootstrap an AI agent with your instructions and verify it behaves correctly

### Runtime Integrations

Patterns for connecting this model to agent runtimes.

- **Files:** `docs/runtimes/`, `examples/`
- **Requirements:** Include working code samples, tested against the target runtime
- **Supported runtimes:** [OpenClaw](https://github.com/nicepkg/openclaw), [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), [CrewAI](https://github.com/crewAIInc/crewAI), [LangGraph](https://github.com/langchain-ai/langgraph), [AutoGen](https://github.com/microsoft/autogen), [Semantic Kernel](https://github.com/microsoft/semantic-kernel)

### Tooling & CI

GitHub Actions, validation scripts, linters, dashboards.

- **Files:** `.github/`, project root scripts
- **Requirements:** Must not break existing workflows or add runtime dependencies

### Documentation

README improvements, guides, examples, tutorials.

- **Files:** `README.md`, `examples/`, `CUSTOMIZATION-GUIDE.md`
- **Guidelines:** Keep language clear and jargon-free

## Contribution Workflow

### For Small Changes (typos, broken links, template fixes)

1. Fork → branch → fix → PR. No discussion needed.

### For Medium Changes (new template, policy improvement, new agent type)

1. Open an Issue using the appropriate [issue template](https://github.com/wlfghdr/agentic-enterprise/issues/new/choose)
2. Fork → branch → implement → PR referencing the issue

### For Large Changes (structural changes, new layers/loops, major integrations)

1. Start a [Discussion](https://github.com/wlfghdr/agentic-enterprise/discussions) with an RFC
2. Gather feedback from the community
3. Once there's rough consensus, open an Issue
4. Fork → branch → implement → PR referencing both the discussion and issue

### Roadmap Items (known limitations)

The [Known Limitations](https://github.com/wlfghdr/agentic-enterprise#known-limitations--roadmap) section in the README tracks the biggest open challenges. Each has a linked GitHub Issue with detailed research and references. These are the highest-impact areas for contribution:

| # | Limitation | Difficulty | Good First? |
|---|-----------|------------|-------------|
| 1 | Mono-repo → multi-repo guidance | Medium | No |
| 2 | Agent runtime integration examples | Medium | Yes |
| 3 | Quality policy calibration (OWASP/CIS/NIST) | High | Yes (per policy) |
| 4 | Wire governance (Branch Protection, CODEOWNERS) | Low | Yes |
| 5 | Skills/tools/MCP beyond AGENT.md | High | No |
| 6 | Multi-channel interaction (Slack/Teams) | Medium | Yes |
| 7 | Dashboards & visualization | Medium | Yes |
| 8 | Cross-repo orchestration | High | No |
| 9 | Agent instruction enforcement | High | No |
| 10 | Real system connections (MCP/A2A) | High | No |

Look for the `good first issue` label for beginner-friendly entry points.

## Contribution Guidelines

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(quality): add data-governance policy
fix(template): correct placeholder in mission brief
docs(readme): add CrewAI integration example
chore(ci): update validation workflow
refactor(agents): simplify execution layer hierarchy
```

**Scopes:** `quality`, `template`, `readme`, `agents`, `steering`, `strategy`, `orchestration`, `execution`, `ci`, `tooling`, `runtime`, `examples`

### Pull Request Process

1. **One concern per PR** — don't bundle unrelated changes
2. **Fill out the PR template** — explain what and why
3. **Link to context** — reference issues, discussions, or signals that motivated the change
4. **Self-review** — check your own diff before requesting review
5. **Be patient** — maintainers review on a best-effort basis

### What Makes a Good PR

- Follows existing file naming conventions
- Maintains the instruction hierarchy (AGENTS.md > layer AGENT.md > division AGENT.md)
- Doesn't introduce contradictions with existing policies
- Includes clear rationale in the PR description
- Templates use `{{PLACEHOLDER}}` markers consistently
- YAML files parse without errors

### What to Avoid

- Changing `CONFIG.yaml` placeholders to company-specific values (that's for forks)
- Adding runtime dependencies — this is a text-based framework
- Submitting AI-generated content without review and validation
- Breaking the layer separation (strategy agents shouldn't reference execution code)
- Large PRs with no prior discussion

## Architecture Decisions

When proposing significant changes, keep these design principles in mind:

1. **Git-native** — Everything must work as plain files in a Git repository. No databases, no proprietary formats, no build steps required.
2. **Runtime-agnostic** — The framework must not favor any specific agent runtime. Runtime-specific guides go in `docs/runtimes/`; integration examples go in `examples/`.
3. **Layer separation** — The 5-layer model is a core architectural constraint. Each layer has clear boundaries and responsibilities.
4. **Policies over enforcement** — Quality policies describe WHAT must be true, not HOW to check it. Enforcement tooling is separate.
5. **Templates over opinions** — Provide structure, not prescriptive content. Placeholders let adopters fill in their own context.
6. **Progressive disclosure** — New adopters should be able to start with CONFIG.yaml and a single division. Don't require understanding everything upfront.

## Framework vs. Fork Customization

| Change Type | Where |
|---|---|
| Improve the model itself | PR to this repo |
| Customize for your company | Fork, edit `CONFIG.yaml`, modify divisions |
| Add your company's divisions | Fork — see `CUSTOMIZATION-GUIDE.md` |
| Fix a bug in a template | PR to this repo |
| Add a company-specific template | Fork |
| Add a new generic agent type | PR to this repo |
| Configure agent types for your stack | Fork |

See [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) for details on tailoring the framework.

## Development Setup

No build tools required. You need:

- A text editor (VS Code recommended)
- Git
- Python 3.x (optional, for YAML validation)
- An AI coding assistant (recommended for testing agent instructions)

### Validating Changes

```bash
# Check YAML files parse correctly
find . -name "*.yaml" -o -name "*.yml" | grep -v '.github/' | \
  xargs -I{} python3 -c "import yaml; yaml.safe_load(open('{}'))" 2>&1

# Check for broken internal links (basic)
grep -rn ']\(\./' --include="*.md" . | grep -v node_modules

# Check for unfilled placeholders in non-template files
grep -rn '{{' --include="*.md" . | grep -v '_TEMPLATE' | grep -v 'CONFIG.yaml' | \
  grep -v 'CONTRIBUTING.md' | grep -v 'CUSTOMIZATION-GUIDE.md'

# Validate structure (required files exist)
for f in README.md AGENTS.md CONFIG.yaml COMPANY.md OPERATING-MODEL.md CODEOWNERS LICENSE; do
  [ -f "$f" ] && echo "OK: $f" || echo "MISSING: $f"
done
```

The CI pipeline (`.github/workflows/validate.yml`) runs these checks automatically on every PR.

### Testing Agent Instructions

The best way to test changes to agent instructions is to actually use them:

1. Pick an AI coding assistant (Claude Code, Cursor, Copilot, etc.)
2. Point it at the repository with your changes
3. Ask it to perform a task within the framework (e.g., "create a new signal", "review this mission brief")
4. Verify it follows the instruction hierarchy and respects quality policies

## Community

- **[GitHub Issues](https://github.com/wlfghdr/agentic-enterprise/issues)** — Bug reports and feature requests
- **[GitHub Discussions](https://github.com/wlfghdr/agentic-enterprise/discussions)** — Questions, ideas, RFCs, and community conversation
- **[Pull Requests](https://github.com/wlfghdr/agentic-enterprise/pulls)** — The primary mechanism for all changes

## Recognition

All contributors are valued. Significant contributions will be acknowledged in the README. If you've built something interesting on top of the framework, share it in [Discussions](https://github.com/wlfghdr/agentic-enterprise/discussions) — we'd love to feature it.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Report unacceptable behavior to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](LICENSE).
