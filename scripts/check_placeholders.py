#!/usr/bin/env python3
"""Blocking CI check: detect unfilled placeholders in non-template docs.

Exit codes:
  0 — no violations found
  1 — violations found (CI should fail)

Self-check mode (--self-check):
  Runs against a set of synthetic in-memory fixtures and reports PASS/FAIL.

Per-file opt-out:
  Add the line  <!-- placeholder-ok -->  anywhere in the file to suppress
  all placeholder warnings for that file.  Use sparingly — only when a file
  intentionally uses placeholder syntax that cannot be placed in a template
  and is not already covered by FRAMEWORK_FILES below.

Template detection (always excluded):
  • Filename starts with  _TEMPLATE  (e.g. _TEMPLATE-mission-brief.md)
  • File resides anywhere inside a directory named  _TEMPLATE
  • File is inside a  templates/  or  docs/templates/  directory
  • GitHub PR/issue templates in  .github/

Framework base files (always excluded):
  These files ship with the OSS framework template and intentionally contain
  {{VAR}} markers that operators fill in via CONFIG.yaml.  They are excluded
  by path so that they do not require a <!-- placeholder-ok --> pragma or a
  version bump every time the placeholder check is updated.
  See FRAMEWORK_FILES below.

Detected placeholder patterns (case-insensitive unless noted):
  1. {{SOME_VAR}}          — unfilled Mustache/double-brace template variable
  2. [TODO]                — square-bracket TODO marker
  3. [TBD]                 — square-bracket TBD marker
  4. [PLACEHOLDER]         — explicit bracket placeholder
  5. __PLACEHOLDER__       — dunder placeholder
  6. <PLACEHOLDER>         — angle-bracket placeholder
  7. <TODO>                — angle-bracket TODO
  8. T.B.D.                — abbreviation with periods (case-insensitive)
  9. Coming Soon           — common holding text (case-insensitive)
 10. _TO_BE_DEFINED_       — underscore-bounded variant
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Placeholder patterns — (label, compiled regex)
# ---------------------------------------------------------------------------
PLACEHOLDER_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("unfilled template variable {{…}}", re.compile(r"\{\{[A-Za-z_][A-Za-z0-9_ ]*\}\}")),
    ("[TODO] marker", re.compile(r"\[TODO\]", re.IGNORECASE)),
    ("[TBD] marker", re.compile(r"\[TBD\]", re.IGNORECASE)),
    ("[PLACEHOLDER] marker", re.compile(r"\[PLACEHOLDER\]", re.IGNORECASE)),
    ("__PLACEHOLDER__ marker", re.compile(r"__PLACEHOLDER__", re.IGNORECASE)),
    ("<PLACEHOLDER> marker", re.compile(r"<PLACEHOLDER>", re.IGNORECASE)),
    ("<TODO> marker", re.compile(r"<TODO>", re.IGNORECASE)),
    # \b doesn't match after '.' — use negative lookahead/lookbehind instead
    ("T.B.D. abbreviation", re.compile(r"(?<![A-Za-z])T\.B\.D\.(?![A-Za-z])", re.IGNORECASE)),
    ("'Coming Soon' text", re.compile(r"\bcoming\s+soon\b", re.IGNORECASE)),
    ("_TO_BE_DEFINED_ marker", re.compile(r"_TO_BE_DEFINED_", re.IGNORECASE)),
]

# Per-file opt-out pragma (anywhere in the file)
OPT_OUT_PRAGMA = "<!-- placeholder-ok -->"

# ---------------------------------------------------------------------------
# Hard-coded filename exemptions
# These files explain placeholder syntax or are framework meta-docs.
# ---------------------------------------------------------------------------
EXEMPT_FILENAMES: frozenset[str] = frozenset(
    {
        "CONTRIBUTING.md",
        "CUSTOMIZATION-GUIDE.md",
        "AGENT-BOOTSTRAP-PROMPT.md",
        "OPERATING-MODEL.md",
    }
)

# ---------------------------------------------------------------------------
# Framework base files — excluded by relative path.
#
# These ship with the OSS template and intentionally contain {{VAR}} markers
# for operators to fill in via CONFIG.yaml.  They are NOT work artifacts and
# should never be flagged as violations.  The list is maintained here (not via
# per-file pragmas) so that no version bumps are required on those governed
# files merely because the placeholder check was introduced.
#
# To add a new exclusion, append the path relative to the repository root.
# ---------------------------------------------------------------------------
FRAMEWORK_FILES: frozenset[str] = frozenset(
    {
        # Root identity & navigation
        "AGENTS.md",
        "CLAUDE.md",          # symlink → AGENTS.md
        "COMPANY.md",
        "FILE-GUIDE.md",
        "README.md",
        # Org layer instructions (ship with {{COMPANY_SHORT}} etc.)
        "org/README.md",
        "org/0-steering/AGENT.md",
        "org/0-steering/EVOLUTION.md",
        "org/1-strategy/AGENT.md",
        "org/2-orchestration/AGENT.md",
        "org/3-execution/AGENT.md",
        "org/4-quality/AGENT.md",
        "org/agents/README.md",
        # Execution division stubs (placeholder names by design)
        "org/3-execution/divisions/core-domain-1/DIVISION.md",
        "org/3-execution/divisions/core-domain-2/DIVISION.md",
        # Quality policies (reference {{OBSERVABILITY_TOOL}} etc.)
        "org/4-quality/policies/architecture.md",
        "org/4-quality/policies/delivery.md",
        "org/4-quality/policies/experience.md",
        "org/4-quality/policies/observability.md",
        "org/4-quality/policies/performance.md",
        "org/4-quality/policies/security.md",
        # Integration registry (uses {{OTLP_INGEST_ENDPOINT}} etc.)
        "org/integrations/categories/observability.md",
        # Process guides (use {{CANARY_PERCENTAGE}} etc.)
        "process/README.md",
        "process/1-discover/GUIDE.md",
        "process/3-ship/GUIDE.md",
        "process/4-operate/GUIDE.md",
        # Steering evolution log
        "org/0-steering/EVOLUTION.md",
    }
)


class Violation(NamedTuple):
    file: Path
    line_no: int
    line: str
    pattern_label: str
    match: str


def is_template_file(path: Path, repo_root: Path) -> bool:
    """Return True if *path* is a template file that should be excluded."""
    name = path.name
    rel_parts = path.relative_to(repo_root).parts

    # Filename-based: starts with _TEMPLATE
    if name.startswith("_TEMPLATE"):
        return True

    # Any ancestor directory named _TEMPLATE (e.g. org/…/_TEMPLATE/DIVISION.md)
    for part in rel_parts[:-1]:
        if part == "_TEMPLATE":
            return True

    # Directory-based: templates/ or docs/templates/
    for part in rel_parts[:-1]:
        if part.lower() == "templates":
            return True

    # GitHub PR / issue templates
    if ".github" in rel_parts and "TEMPLATE" in name.upper():
        return True

    return False


def is_framework_file(path: Path, repo_root: Path) -> bool:
    """Return True if *path* is a known framework base file."""
    try:
        rel = str(path.relative_to(repo_root))
    except ValueError:
        return False
    return rel in FRAMEWORK_FILES


def is_exempt_file(path: Path) -> bool:
    """Return True if the file is in the hard-coded name-based exemption list."""
    return path.name in EXEMPT_FILENAMES


def scan_file(path: Path) -> list[Violation]:
    """Scan *path* for placeholder violations. Returns a list of Violation."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    # Per-file opt-out
    if OPT_OUT_PRAGMA in text:
        return []

    violations: list[Violation] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for label, pattern in PLACEHOLDER_PATTERNS:
            m = pattern.search(line)
            if m:
                violations.append(
                    Violation(
                        file=path,
                        line_no=line_no,
                        line=line.rstrip(),
                        pattern_label=label,
                        match=m.group(0),
                    )
                )
                break  # one violation per line is enough
    return violations


def collect_md_files(repo_root: Path) -> list[Path]:
    """Yield all .md files that should be checked."""
    results = []
    for p in repo_root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        if "node_modules" in p.parts:
            continue
        if is_template_file(p, repo_root):
            continue
        if is_exempt_file(p):
            continue
        if is_framework_file(p, repo_root):
            continue
        results.append(p)
    return sorted(results)


def run_check(repo_root: Path) -> int:
    """Main check. Returns 0 on success, 1 on violations."""
    files = collect_md_files(repo_root)
    all_violations: list[Violation] = []

    for f in files:
        all_violations.extend(scan_file(f))

    if not all_violations:
        print(f"✓ Checked {len(files)} markdown file(s): no placeholder violations found.")
        return 0

    print(
        f"✗ Placeholder violations found in non-template docs"
        f" ({len(all_violations)} occurrence(s) in"
        f" {len({v.file for v in all_violations})} file(s)):\n"
    )
    grouped: dict[Path, list[Violation]] = {}
    for v in all_violations:
        grouped.setdefault(v.file, []).append(v)

    for fpath, viols in sorted(grouped.items()):
        rel = fpath.relative_to(repo_root)
        print(f"  {rel}  ({len(viols)} violation(s))")
        for v in viols:
            print(f"    line {v.line_no}: [{v.pattern_label}]  →  {v.match!r}")
            print(f"      {v.line[:120]}")
        print()

    print("How to fix:")
    print("  1. Fill in the placeholder with real content, or")
    print("  2. Remove the section if it is not yet applicable, or")
    print("  3. If this file intentionally uses placeholder syntax (e.g., a framework")
    print(f"     config file that ships with {{{{VAR}}}} markers), add:")
    print(f"       {OPT_OUT_PRAGMA}")
    print("     anywhere in the file.")
    print()
    print("Template files (*_TEMPLATE-*.md and files inside _TEMPLATE/ dirs) are")
    print("automatically excluded. See docs/PLACEHOLDER-CHECK.md for full guidance.")
    print()
    return 1


# ---------------------------------------------------------------------------
# Self-check mode
# ---------------------------------------------------------------------------
def run_self_check() -> int:
    """Synthetic fixture tests. Returns 0 if all pass, 1 if any fail."""
    import tempfile
    import os

    failures: list[str] = []

    def assert_violations(label: str, content: str, expected_count: int) -> None:
        """Write content to a temp file, scan it, assert violation count."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, prefix="placeholder_test_"
        ) as f:
            f.write(content)
            tmp = Path(f.name)
        try:
            viols = scan_file(tmp)
            if len(viols) != expected_count:
                failures.append(
                    f"FAIL [{label}]: expected {expected_count} violations, got {len(viols)}"
                )
            else:
                print(f"  PASS [{label}]")
        finally:
            os.unlink(tmp)

    print("Running self-check…\n")

    # Should detect violations
    assert_violations("{{VAR}} pattern", "The owner is {{COMPANY_NAME}}.", 1)
    assert_violations("[TODO] pattern", "Status: [TODO] fill this in", 1)
    assert_violations("[TBD] pattern", "Release date: [TBD]", 1)
    assert_violations("[PLACEHOLDER] pattern", "See [PLACEHOLDER] for details", 1)
    assert_violations("__PLACEHOLDER__ pattern", "Value: __PLACEHOLDER__", 1)
    assert_violations("<PLACEHOLDER> pattern", "Contact: <PLACEHOLDER>", 1)
    assert_violations("<TODO> pattern", "Owner: <TODO>", 1)
    assert_violations("T.B.D. at end", "Budget: T.B.D.", 1)
    assert_violations("T.B.D. mid-sentence", "The value is T.B.D. for now.", 1)
    assert_violations("Coming Soon lower", "Status: coming soon", 1)
    assert_violations("Coming Soon mixed", "Status: Coming Soon", 1)
    assert_violations("_TO_BE_DEFINED_ pattern", "Value: _TO_BE_DEFINED_", 1)

    # Should NOT detect violations
    assert_violations("clean file", "# Hello\nThis is a real document.", 0)
    assert_violations(
        "opt-out pragma suppresses all",
        f"<!-- placeholder-ok -->\n{{{{COMPANY_NAME}}}}\n[TODO] something",
        0,
    )
    assert_violations("multi-line two vars", "Line A {{VAR}}\nLine B {{OTHER}}", 2)
    assert_violations("TBD without brackets is fine", "See PR #TBD and PR #42.", 0)
    assert_violations("word containing TBD is fine", "KTBD is not a match.", 0)

    # Template filename and directory detection
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # A _TEMPLATE- file should be excluded
        tmpl = root / "_TEMPLATE-mission.md"
        tmpl.write_text("{{COMPANY_NAME}} [TODO]")
        files = collect_md_files(root)
        if files:
            failures.append(f"FAIL [_TEMPLATE- file should be excluded]: got {files}")
        else:
            print("  PASS [_TEMPLATE- file excluded]")

        # A file inside a _TEMPLATE directory should be excluded
        (root / "_TEMPLATE").mkdir()
        inner = root / "_TEMPLATE" / "DIVISION.md"
        inner.write_text("{{DIVISION_NAME}} [TODO]")
        files2 = collect_md_files(root)
        if files2:
            failures.append(f"FAIL [_TEMPLATE/ dir excluded]: got {files2}")
        else:
            print("  PASS [_TEMPLATE/ dir file excluded]")

        # A regular .md file in root should be scanned
        normal = root / "NORMAL.md"
        normal.write_text("{{COMPANY_NAME}}")
        files3 = collect_md_files(root)
        if len(files3) != 1 or files3[0] != normal:
            failures.append(f"FAIL [normal file included]: got {files3}")
        else:
            print("  PASS [normal file included]")

        # Framework files list exclusion
        # Create org/4-quality/policies/architecture.md inside the tmpdir — its
        # path relative to root is "org/4-quality/policies/architecture.md" which
        # IS in FRAMEWORK_FILES, so it should be excluded from scanning.
        subdir = root / "org" / "4-quality" / "policies"
        subdir.mkdir(parents=True)
        fw_file = subdir / "architecture.md"
        fw_file.write_text("{{MIN_CODE_COVERAGE}}")
        files4 = collect_md_files(root)
        if fw_file not in files4:
            print("  PASS [FRAMEWORK_FILES exclusion: architecture.md not scanned]")
        else:
            failures.append("FAIL [FRAMEWORK_FILES exclusion: architecture.md should be excluded]")

    print()
    if failures:
        for f in failures:
            print(f"  {f}")
        print(f"\n{len(failures)} self-check(s) failed.")
        return 1

    print("All self-checks passed.")
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Check non-template docs for unfilled placeholders."
    )
    parser.add_argument(
        "--self-check",
        action="store_true",
        help="Run synthetic fixture tests instead of scanning the repo.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root (default: current directory).",
    )
    args = parser.parse_args(argv)

    if args.self_check:
        return run_self_check()

    repo_root = Path(args.root).resolve()
    return run_check(repo_root)


if __name__ == "__main__":
    sys.exit(main())
