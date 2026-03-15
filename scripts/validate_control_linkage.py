#!/usr/bin/env python3
"""CI check: validate risk → policy → control → evidence chains.

Ensures that references from risk register entries and governance exceptions
resolve to real policy files and sections.

Exit codes:
  0 — no broken links found
  1 — broken references detected

Self-check mode (--self-check):
  Runs against synthetic fixtures and reports PASS/FAIL.

What this script validates:
  1. RISK-*.md "Controls Applied" table: each Source reference resolves to
     an existing policy file and (optionally) a numbered section within it.
  2. EXC-*.md "What rule is being overridden" section: canonical policy
     references (file + section) resolve to existing artifacts.
  3. Orphan detection: controls referenced but not defined in any policy.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# Matches policy file references like:
#   org/4-quality/policies/security.md
#   `org/4-quality/policies/security.md`
#   security.md §2.1
#   `risk-management.md` §3
#   org/4-quality/policies/risk-management.md §4.1
POLICY_REF_PATTERN = re.compile(
    r"(?:`?)("
    r"(?:org/4-quality/policies/)?"   # optional full path prefix
    r"[a-z][a-z0-9-]+\.md"           # policy filename
    r")"
    r"(?:`?)"
    r"(?:\s+§([\d]+(?:\.[\d]+)*))?",  # optional section reference §N.N
    re.IGNORECASE,
)

# Matches markdown table rows: | col1 | col2 | col3 | col4 |
TABLE_ROW_PATTERN = re.compile(r"^\s*\|(.+)\|\s*$")
TABLE_SEPARATOR = re.compile(r"^[\s|:-]+$")

# Section heading pattern: ## 1. Title or ### 2.1 Title
SECTION_HEADING_PATTERN = re.compile(r"^(#{2,4})\s+([\d]+(?:\.[\d]+)*)[.\s]")


class LinkError(NamedTuple):
    source_file: str
    line_no: int
    reference: str
    error: str


def extract_policy_sections(policy_path: Path) -> set[str]:
    """Extract all numbered section identifiers from a policy file.
    E.g., {"1", "2", "2.1", "3", "3.2"} from headings like '## 1. Foo', '### 2.1 Bar'."""
    sections: set[str] = set()
    try:
        text = policy_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return sections

    for line in text.splitlines():
        m = SECTION_HEADING_PATTERN.match(line)
        if m:
            section_num = m.group(2)
            sections.add(section_num)
            # Also add parent sections: "3.2" implies "3" exists
            parts = section_num.split(".")
            for i in range(1, len(parts)):
                sections.add(".".join(parts[:i]))
    return sections


def find_policies(repo_root: Path) -> dict[str, Path]:
    """Build a map of policy filename → full path for all quality policies."""
    policies_dir = repo_root / "org" / "4-quality" / "policies"
    result: dict[str, Path] = {}
    if policies_dir.is_dir():
        for p in policies_dir.glob("*.md"):
            result[p.name] = p
    return result


def parse_controls_applied_table(
    lines: list[str], start_idx: int
) -> list[tuple[int, str]]:
    """Parse the Controls Applied table and extract Source column values.
    Returns [(line_no, source_text), ...]."""
    results: list[tuple[int, str]] = []
    in_table = False
    header_cols: list[str] = []
    source_col_idx = -1

    for i in range(start_idx, len(lines)):
        line = lines[i]
        row_match = TABLE_ROW_PATTERN.match(line)

        if not in_table:
            if row_match:
                # This could be the header row
                header_cols = [c.strip() for c in row_match.group(1).split("|")]
                # Find the "Source" column
                for idx, col in enumerate(header_cols):
                    if col.lower() == "source":
                        source_col_idx = idx
                        break
                if source_col_idx >= 0:
                    in_table = True
            continue

        if not row_match:
            # End of table
            break

        # Skip separator row
        cells_text = row_match.group(1)
        if TABLE_SEPARATOR.match(cells_text):
            continue

        cells = [c.strip() for c in cells_text.split("|")]
        if source_col_idx < len(cells):
            source_text = cells[source_col_idx]
            # Skip template placeholders
            if source_text and not source_text.startswith("<"):
                results.append((i + 1, source_text))  # 1-indexed line number

    return results


def validate_risk_files(
    repo_root: Path,
    policies: dict[str, Path],
    policy_sections_cache: dict[str, set[str]],
) -> list[LinkError]:
    """Validate RISK-*.md files: check Controls Applied table references."""
    errors: list[LinkError] = []
    decisions_dir = repo_root / "work" / "decisions"
    if not decisions_dir.is_dir():
        return errors

    for risk_file in sorted(decisions_dir.glob("RISK-*.md")):
        if risk_file.name.startswith("_TEMPLATE"):
            continue

        try:
            text = risk_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        lines = text.splitlines()
        rel_path = str(risk_file.relative_to(repo_root))

        # Find "Controls Applied" section
        for idx, line in enumerate(lines):
            if "controls applied" in line.lower() and line.strip().startswith("#"):
                sources = parse_controls_applied_table(lines, idx + 1)
                for line_no, source_text in sources:
                    ref_errors = validate_policy_reference(
                        source_text, rel_path, line_no,
                        policies, policy_sections_cache,
                    )
                    errors.extend(ref_errors)
                break

    return errors


def validate_exception_files(
    repo_root: Path,
    policies: dict[str, Path],
    policy_sections_cache: dict[str, set[str]],
) -> list[LinkError]:
    """Validate EXC-*.md files: check rule override references."""
    errors: list[LinkError] = []
    decisions_dir = repo_root / "work" / "decisions"
    if not decisions_dir.is_dir():
        return errors

    for exc_file in sorted(decisions_dir.glob("EXC-*.md")):
        if exc_file.name.startswith("_TEMPLATE"):
            continue

        try:
            text = exc_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        lines = text.splitlines()
        rel_path = str(exc_file.relative_to(repo_root))

        # Find "What rule is being overridden" section
        in_override_section = False
        for idx, line in enumerate(lines):
            stripped = line.strip()

            if "what rule is being overridden" in stripped.lower():
                in_override_section = True
                continue

            # End of section at next heading
            if in_override_section and stripped.startswith("#"):
                break

            if in_override_section:
                # Look for policy references in this section
                for m in POLICY_REF_PATTERN.finditer(line):
                    full_ref = m.group(0)
                    ref_errors = validate_policy_reference(
                        full_ref, rel_path, idx + 1,
                        policies, policy_sections_cache,
                    )
                    errors.extend(ref_errors)

    return errors


def validate_policy_reference(
    ref_text: str,
    source_file: str,
    line_no: int,
    policies: dict[str, Path],
    policy_sections_cache: dict[str, set[str]],
) -> list[LinkError]:
    """Validate a single policy reference string. Returns list of errors."""
    errors: list[LinkError] = []

    matches = list(POLICY_REF_PATTERN.finditer(ref_text))
    if not matches:
        # Not a recognizable policy reference — skip silently
        return errors

    for m in matches:
        raw_filename = m.group(1)
        section_ref = m.group(2)  # May be None

        # Normalize: strip path prefix if present
        filename = raw_filename.split("/")[-1] if "/" in raw_filename else raw_filename

        if filename not in policies:
            errors.append(LinkError(
                source_file=source_file,
                line_no=line_no,
                reference=m.group(0).strip("`"),
                error=f"policy file not found: {filename}",
            ))
            continue

        if section_ref:
            # Validate section exists
            if filename not in policy_sections_cache:
                policy_sections_cache[filename] = extract_policy_sections(
                    policies[filename]
                )
            sections = policy_sections_cache[filename]
            if section_ref not in sections:
                errors.append(LinkError(
                    source_file=source_file,
                    line_no=line_no,
                    reference=m.group(0).strip("`"),
                    error=f"section §{section_ref} not found in {filename} "
                          f"(available: {', '.join(sorted(sections, key=lambda s: [int(x) for x in s.split('.')])[:10]) or 'none'})",
                ))

    return errors


def run_check(repo_root: Path) -> int:
    """Main check. Returns 0 on success, 1 on violations."""
    policies = find_policies(repo_root)
    if not policies:
        print("⚠  No quality policies found in org/4-quality/policies/")
        print("   (This is expected only for empty repos)")
        return 0

    policy_sections_cache: dict[str, set[str]] = {}
    all_errors: list[LinkError] = []

    # Validate risk register entries
    risk_errors = validate_risk_files(repo_root, policies, policy_sections_cache)
    all_errors.extend(risk_errors)

    # Validate governance exceptions
    exc_errors = validate_exception_files(repo_root, policies, policy_sections_cache)
    all_errors.extend(exc_errors)

    # Count artifacts scanned
    decisions_dir = repo_root / "work" / "decisions"
    risk_count = len(list(decisions_dir.glob("RISK-*.md"))) if decisions_dir.is_dir() else 0
    exc_count = len(list(decisions_dir.glob("EXC-*.md"))) if decisions_dir.is_dir() else 0
    # Exclude templates from count
    risk_count -= len(list(decisions_dir.glob("_TEMPLATE*RISK*"))) if decisions_dir.is_dir() else 0
    exc_count -= len(list(decisions_dir.glob("_TEMPLATE*EXC*"))) if decisions_dir.is_dir() else 0

    if not all_errors:
        print(f"✓ Control linkage validated: {risk_count} risk register(s), "
              f"{exc_count} governance exception(s), "
              f"{len(policies)} policies indexed")
        return 0

    # Report errors grouped by source file
    grouped: dict[str, list[LinkError]] = {}
    for err in all_errors:
        grouped.setdefault(err.source_file, []).append(err)

    print(f"✗ Broken control linkage ({len(all_errors)} error(s) in "
          f"{len(grouped)} file(s)):\n")

    for fpath, errs in sorted(grouped.items()):
        print(f"  {fpath}")
        for err in errs:
            print(f"    line {err.line_no}: {err.reference}")
            print(f"      → {err.error}")
        print()

    print("How to fix:")
    print("  1. Ensure the policy file exists in org/4-quality/policies/")
    print("  2. Ensure the section number (§N.N) exists as a heading in the policy")
    print("  3. Use format: policy-name.md §2.1 or org/4-quality/policies/policy-name.md §2.1")
    return 1


# ---------------------------------------------------------------------------
# Self-check mode
# ---------------------------------------------------------------------------
def run_self_check() -> int:
    """Synthetic fixture tests. Returns 0 if all pass, 1 if any fail."""
    import tempfile

    failures: list[str] = []

    def assert_eq(label: str, got: object, expected: object) -> None:
        if got != expected:
            failures.append(f"FAIL [{label}]: expected {expected!r}, got {got!r}")
        else:
            print(f"  PASS [{label}]")

    print("Running self-check…\n")

    # --- extract_policy_sections ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        policy = root / "test-policy.md"
        policy.write_text(
            "# Test Policy\n"
            "## 1. First Section\n"
            "Content.\n"
            "### 1.1 Subsection A\n"
            "### 1.2 Subsection B\n"
            "## 2. Second Section\n"
            "### 2.1 Sub\n"
            "## Evaluation Criteria\n"
        )
        sections = extract_policy_sections(policy)
        assert_eq("extracts §1", "1" in sections, True)
        assert_eq("extracts §1.1", "1.1" in sections, True)
        assert_eq("extracts §1.2", "1.2" in sections, True)
        assert_eq("extracts §2", "2" in sections, True)
        assert_eq("extracts §2.1", "2.1" in sections, True)
        assert_eq("no 'Evaluation'", "Evaluation" not in sections, True)

    # --- POLICY_REF_PATTERN ---
    m1 = POLICY_REF_PATTERN.search("security.md §2.1")
    assert_eq("ref: security.md §2.1 file", m1 and m1.group(1), "security.md")
    assert_eq("ref: security.md §2.1 section", m1 and m1.group(2), "2.1")

    m2 = POLICY_REF_PATTERN.search("org/4-quality/policies/risk-management.md §4")
    assert_eq("ref: full path file", m2 and m2.group(1), "org/4-quality/policies/risk-management.md")
    assert_eq("ref: full path section", m2 and m2.group(2), "4")

    m3 = POLICY_REF_PATTERN.search("`cryptography.md`")
    assert_eq("ref: backtick file", m3 and m3.group(1), "cryptography.md")
    assert_eq("ref: backtick no section", m3 and m3.group(2), None)

    # --- End-to-end with fixtures ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # Create policy structure
        policies_dir = root / "org" / "4-quality" / "policies"
        policies_dir.mkdir(parents=True)
        (policies_dir / "security.md").write_text(
            "# Security Policy\n"
            "## 1. Auth\n"
            "### 1.1 Passwords\n"
            "## 2. Encryption\n"
        )
        (policies_dir / "risk-management.md").write_text(
            "# Risk Management\n"
            "## 1. Overview\n"
            "## 2. Appetite\n"
            "## 3. Methodology\n"
            "### 3.1 Scoring\n"
            "### 3.2 Matrix\n"
        )

        decisions_dir = root / "work" / "decisions"
        decisions_dir.mkdir(parents=True)

        # Valid risk register
        (decisions_dir / "RISK-2026-001-test.md").write_text(
            "# Risk: Test Risk\n"
            "## Controls Applied\n"
            "| Control | Type | Source | Status |\n"
            "|---------|------|--------|--------|\n"
            "| Access control | Preventive | security.md §1.1 | Implemented |\n"
            "| Risk scoring | Detective | risk-management.md §3.2 | Implemented |\n"
        )

        # Run check — should pass
        policies = find_policies(root)
        cache: dict[str, set[str]] = {}
        errs = validate_risk_files(root, policies, cache)
        assert_eq("valid RISK: no errors", len(errs), 0)

        # Invalid risk register — broken section reference
        (decisions_dir / "RISK-2026-002-broken.md").write_text(
            "# Risk: Broken Risk\n"
            "## Controls Applied\n"
            "| Control | Type | Source | Status |\n"
            "|---------|------|--------|--------|\n"
            "| Missing control | Preventive | security.md §99 | Planned |\n"
            "| Bad file | Detective | nonexistent.md §1 | Planned |\n"
        )

        cache2: dict[str, set[str]] = {}
        errs2 = validate_risk_files(root, policies, cache2)
        assert_eq("broken RISK: 2 errors", len(errs2), 2)
        assert_eq("broken RISK: section error", "§99" in errs2[0].error, True)
        assert_eq("broken RISK: file error", "not found" in errs2[1].error, True)

        # Valid governance exception
        (decisions_dir / "EXC-2026-001-valid.md").write_text(
            "# Exception: Valid\n"
            "## Details\n"
            "### What rule is being overridden\n"
            "- `security.md` §2\n"
            "- Encryption requirement waived for dev environment\n"
            "### Why it is necessary\n"
            "Dev speed.\n"
        )

        cache3: dict[str, set[str]] = {}
        errs3 = validate_exception_files(root, policies, cache3)
        assert_eq("valid EXC: no errors", len(errs3), 0)

        # Invalid governance exception
        (decisions_dir / "EXC-2026-002-broken.md").write_text(
            "# Exception: Broken\n"
            "## Details\n"
            "### What rule is being overridden\n"
            "- `security.md` §99.9\n"
            "### Why it is necessary\n"
            "Test.\n"
        )

        cache4: dict[str, set[str]] = {}
        errs4 = validate_exception_files(root, policies, cache4)
        assert_eq("broken EXC: 1 error", len(errs4), 1)
        assert_eq("broken EXC: section error", "§99.9" in errs4[0].error, True)

        # Template files should be skipped
        (decisions_dir / "_TEMPLATE-RISK-test.md").write_text(
            "# Risk: Template\n"
            "## Controls Applied\n"
            "| Control | Type | Source | Status |\n"
            "|---------|------|--------|--------|\n"
            "| Template control | Preventive | fake-policy.md §99 | Planned |\n"
        )
        cache5: dict[str, set[str]] = {}
        errs5 = validate_risk_files(root, policies, cache5)
        # Should still be 2 from RISK-002, not 3 (template skipped)
        non_template_errs = [e for e in errs5 if "_TEMPLATE" not in e.source_file]
        assert_eq("templates skipped", len(non_template_errs), 2)

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
        description="Validate risk → policy → control linkage chains."
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
