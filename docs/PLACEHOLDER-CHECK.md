# Placeholder Check — CI Gate

**Status:** enforced (blocking CI)  
**Script:** `scripts/check_placeholders.py`  
**Workflow job:** `validate-placeholders` in `.github/workflows/validate.yml`

---

## What This Check Does

Every pull request runs a scan of all non-template Markdown files.  
If any file contains an **unfilled placeholder**, the CI job **fails** and
the PR cannot be merged until the placeholder is resolved.

This prevents partially-written documents from landing in `main`.

---

## Detected Placeholder Patterns

| Pattern | Example | Label |
|---|---|---|
| `{{VAR_NAME}}` | `{{COMPANY_NAME}}` | unfilled template variable |
| `[TODO]` | `Status: [TODO]` | square-bracket TODO marker |
| `[TBD]` | `Owner: [TBD]` | square-bracket TBD marker |
| `[PLACEHOLDER]` | `See [PLACEHOLDER]` | bracket placeholder |
| `__PLACEHOLDER__` | `Value: __PLACEHOLDER__` | dunder placeholder |
| `<PLACEHOLDER>` | `Contact: <PLACEHOLDER>` | angle-bracket placeholder |
| `<TODO>` | `Owner: <TODO>` | angle-bracket TODO |
| `T.B.D.` | `Budget: T.B.D.` | abbreviation with periods |
| `coming soon` | `Status: Coming Soon` | holding text (case-insensitive) |
| `_TO_BE_DEFINED_` | `Threshold: _TO_BE_DEFINED_` | underscore-bounded marker |

All patterns are **case-insensitive** (except `{{VAR}}` which is matched as-is).

---

## What Is Excluded

The following are **always excluded** from scanning:

| Exclusion | Reason |
|---|---|
| Files whose name starts with `_TEMPLATE` (e.g. `_TEMPLATE-mission-brief.md`) | These are template documents meant to contain placeholders |
| Files inside a directory named `_TEMPLATE` (e.g. `org/…/_TEMPLATE/DIVISION.md`) | Same — template scaffolding |
| Files inside `templates/` or `docs/templates/` directories | Template directories |
| `.github/` PR/issue templates | GitHub-managed templates |
| `CONTRIBUTING.md`, `CUSTOMIZATION-GUIDE.md`, `AGENT-BOOTSTRAP-PROMPT.md`, `OPERATING-MODEL.md` | Framework meta-docs that explain placeholder syntax |
| Files listed in `FRAMEWORK_FILES` in `scripts/check_placeholders.py` | Framework base files that ship with intentional `{{VAR}}` markers (e.g. `AGENTS.md`, `COMPANY.md`, layer `AGENT.md` files, quality policies) — filled in by operators via `CONFIG.yaml` |

---

## Per-File Opt-Out (`<!-- placeholder-ok -->`)

If a file **intentionally** contains placeholder-like syntax — for example, a
framework configuration file that ships with `{{VAR}}` markers the operator is
expected to fill in from `CONFIG.yaml` — add this HTML comment anywhere in the
file:

```
<!-- placeholder-ok -->
```

This suppresses all placeholder checks for that file.

### When to use it

✅ **Appropriate uses:**
- Guides or docs that document placeholder syntax for educational purposes
- A new framework file that hasn't been added to `FRAMEWORK_FILES` yet

❌ **Inappropriate uses:**
- Skipping the check on an actual work document that still needs writing
- Hiding incomplete sections in mission briefs, decision records, etc.

> **Note:** The standard framework base files (AGENTS.md, COMPANY.md, layer AGENT.md
> files, quality policies, etc.) are excluded via the `FRAMEWORK_FILES` list in
> `scripts/check_placeholders.py` — no per-file pragma needed for those.

> **Tip:** If you're writing a work document and you need more time, keep it on
> a feature branch until it's complete. Don't use `<!-- placeholder-ok -->` to
> sneak incomplete docs into `main`.

---

## How to Fix a Violation

1. **Fill in the content** — replace the placeholder with real information.
2. **Remove the section** — if the section isn't needed yet, delete it or mark
   it with a dated note instead (e.g. `_Not required for this mission._`).
3. **Use a template** — if you're starting a new document, copy the relevant
   `_TEMPLATE-*.md` file; placeholders inside `_TEMPLATE` files are excluded.
4. **Opt out** (last resort) — if the file genuinely must contain placeholder
   syntax, add `<!-- placeholder-ok -->` and document why.

---

## Running the Check Locally

```bash
# Full repo scan
python3 scripts/check_placeholders.py

# Self-check (tests the script logic with synthetic fixtures)
python3 scripts/check_placeholders.py --self-check

# Scan a specific directory
python3 scripts/check_placeholders.py --root /path/to/repo
```

Exit code `0` = clean. Exit code `1` = violations found.

---

## Adding New Placeholder Patterns

Edit `PLACEHOLDER_PATTERNS` in `scripts/check_placeholders.py` and add a
corresponding self-check assertion in `run_self_check()`.  The self-check step
runs before the scan in CI, so a broken regex will fail fast.

## Adding a New Framework File Exclusion

If you add a new framework base file that intentionally ships with `{{VAR}}`
markers, add its repo-root-relative path to `FRAMEWORK_FILES` in
`scripts/check_placeholders.py`:

```python
FRAMEWORK_FILES: frozenset[str] = frozenset(
    {
        ...
        "path/to/your/new-framework-file.md",
    }
)
```

This avoids requiring a `<!-- placeholder-ok -->` pragma inside the file itself,
which would otherwise trigger a version bump on a governed file.

---

## Related

- [`CONFIG.yaml`](../CONFIG.yaml) — defines `{{VAR}}` values for the framework
- [`CUSTOMIZATION-GUIDE.md`](../CUSTOMIZATION-GUIDE.md) — how to customize the framework
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution guidelines
