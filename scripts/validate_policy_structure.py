#!/usr/bin/env python3
"""
Policy structure validation for Agentic Enterprise framework.

Validates all policies in org/4-quality/policies/ have required sections,
metadata fields, and compliance mapping entries.

Closes #111.

Usage:
  python3 scripts/validate_policy_structure.py [--fix]

Exit codes:
  0  All validations passed
  1  One or more validation failures
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()
POLICIES_DIR = REPO / "org" / "4-quality" / "policies"

# ── Required metadata fields (in blockquote header) ──────────────────────────

REQUIRED_METADATA = [
    ("Version", r"\*\*Version:\*\*\s*(\d+\.\d+(?:\.\d+)?)"),
    ("Last updated", r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})"),
]

# Fields that should be present but with flexible patterns
EXPECTED_METADATA = [
    ("Applies to", r"\*\*Applies to:\*\*\s*(.+)"),
    ("Enforced by", r"\*\*Enforced by:\*\*\s*(.+)"),
    ("Authority", r"\*\*Authority:\*\*\s*(.+)"),
]

# ── Required sections ────────────────────────────────────────────────────────
# Some policies use numbered subsections (## 1. ..., ## 2. ...) instead of
# a single "## Mandatory Requirements" section. The validator accepts either
# a literal "Mandatory Requirements" heading (with optional qualifier) or
# the presence of numbered subsections (## N. ...) as equivalent.
# Similarly, "Principles" may appear as a standalone heading or the policy
# may use a "Prime Directive" / "Observable by Default" style opening.

REQUIRED_SECTIONS = [
    "Evaluation Criteria",
    "Changelog",
]

# Sections checked with flexible matching (accept variants)
FLEXIBLE_SECTIONS = {
    "Principles": {
        "description": "Principles or equivalent opening section",
        "check": "principles_or_numbered",
    },
    "Mandatory Requirements": {
        "description": "Mandatory Requirements or numbered requirement subsections",
        "check": "requirements_or_numbered",
    },
}

# ── Known compliance frameworks ──────────────────────────────────────────────

KNOWN_FRAMEWORKS = [
    "SOC 2",
    "ISO 27001",
    "GDPR",
    "ISO 42001",
    "NIST AI RMF",
    "EU AI Act",
    "HIPAA",
]


def get_sections(text: str) -> dict[str, int]:
    """Return dict of second-level heading titles → line numbers."""
    sections: dict[str, int] = {}
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^##\s+(.+)", line)
        if m:
            sections[m.group(1).strip()] = i
    return sections


def check_non_empty_section(text: str, section_name: str, sections: dict[str, int]) -> str | None:
    """Check that a section has content (not just the heading)."""
    if section_name not in sections:
        return None  # Missing section is caught elsewhere

    line_num = sections[section_name]
    lines = text.splitlines()
    # Look at lines after the heading until next heading or EOF
    content_lines = []
    for line in lines[line_num:]:  # line_num is 1-based, slice is 0-based after heading
        if re.match(r"^##\s+", line):
            break
        stripped = line.strip()
        if stripped and stripped != "---":
            content_lines.append(stripped)

    if not content_lines:
        return f"section '## {section_name}' is empty"
    return None


def validate_policy(path: Path) -> list[str]:
    """Validate a single policy file. Returns list of error messages."""
    errors: list[str] = []
    rel = path.relative_to(REPO)

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read — {exc}"]

    # ── Metadata fields ───────────────────────────────────────────────────
    for name, pattern in REQUIRED_METADATA:
        if not re.search(pattern, text):
            errors.append(f"{rel}: missing required metadata '**{name}:**'")

    for name, pattern in EXPECTED_METADATA:
        if not re.search(pattern, text):
            errors.append(f"{rel}: missing expected metadata '**{name}:**'")

    # ── Required sections ─────────────────────────────────────────────────
    sections = get_sections(text)
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"{rel}: missing required section '## {section}'")
        else:
            empty_err = check_non_empty_section(text, section, sections)
            if empty_err:
                errors.append(f"{rel}: {empty_err}")

    # ── Flexible sections (accept variants) ───────────────────────────────
    # Check for numbered subsections (## 1. ..., ## 2. ...)
    has_numbered = any(re.match(r"^\d+\.\s+", s) for s in sections)

    # Alternate headings that serve as "Principles" equivalent
    principles_alternates = ["prime directive", "why this policy exists", "purpose"]

    for section_name, config in FLEXIBLE_SECTIONS.items():
        has_exact = section_name in sections
        has_partial = any(section_name.lower() in s.lower() for s in sections)

        if config["check"] == "principles_or_numbered":
            has_alternate = any(
                alt in s.lower() for s in sections for alt in principles_alternates
            )
            if not has_exact and not has_partial and not has_numbered and not has_alternate:
                errors.append(f"{rel}: missing '## {section_name}' section or equivalent")
        elif config["check"] == "requirements_or_numbered":
            if not has_exact and not has_partial and not has_numbered:
                errors.append(f"{rel}: missing '## {section_name}' section or numbered requirement subsections")

    # ── Compliance mapping ────────────────────────────────────────────────
    # Policies that deal with governance, security, privacy, risk, or data
    # MUST have compliance framework references. Others get a warning.
    compliance_critical_keywords = [
        "security", "privacy", "risk", "governance", "data-classification",
        "cryptography", "incident", "log-retention", "availability",
        "vendor", "agent-security", "agent-eval",
    ]
    is_compliance_critical = any(kw in path.stem for kw in compliance_critical_keywords)

    has_compliance_ref = any(
        fw.lower() in text.lower() for fw in KNOWN_FRAMEWORKS
    )
    compliance_section = any(
        "compliance" in s.lower() and "mapping" in s.lower()
        for s in sections
    )
    if not has_compliance_ref and not compliance_section:
        if is_compliance_critical:
            errors.append(
                f"{rel}: compliance-critical policy missing compliance framework references "
                f"(expected references to SOC 2, ISO 27001, GDPR, etc.)"
            )
        else:
            # Non-critical: print warning but don't fail
            print(f"  ⚠  {rel}: no compliance mapping section (recommended but not required)")

    # ── Changelog table ───────────────────────────────────────────────────
    if "Changelog" in sections:
        # Check for table structure (Version | Date | Change)
        changelog_start = sections["Changelog"]
        remaining = "\n".join(text.splitlines()[changelog_start:])
        if not re.search(r"\|.*[Vv]ersion.*\|.*[Dd]ate.*\|", remaining):
            errors.append(f"{rel}: Changelog section missing table with Version/Date columns")

    # ── Observability cross-reference ─────────────────────────────────────
    if "observability" in path.name:
        if "OTEL-CONTRACT" not in text and "otel-contract" not in text:
            errors.append(
                f"{rel}: observability policy should reference docs/OTEL-CONTRACT.md or docs/otel-contract.md"
            )

    return errors


def suggest_fix(path: Path) -> str:
    """Generate suggested additions for a policy file."""
    text = path.read_text(encoding="utf-8")
    sections = get_sections(text)
    suggestions = []

    for section in REQUIRED_SECTIONS:
        if section not in sections:
            suggestions.append(f"Add section:\n## {section}\n\n[TODO: Add content]\n")

    for name, pattern in REQUIRED_METADATA:
        if not re.search(pattern, text):
            if name == "Version":
                suggestions.append("Add to header blockquote: > **Version:** 1.0")
            elif name == "Last updated":
                suggestions.append("Add to header blockquote: > **Last updated:** 2026-03-15")

    return "\n".join(suggestions) if suggestions else "No fixes needed."


def main() -> int:
    fix_mode = "--fix" in sys.argv

    if not POLICIES_DIR.exists():
        print(f"ERROR: Policies directory not found: {POLICIES_DIR.relative_to(REPO)}")
        return 1

    policy_files = sorted(
        p for p in POLICIES_DIR.glob("*.md")
        if p.is_file() and p.name != "README.md" and "_TEMPLATE" not in p.name
    )

    if not policy_files:
        print("WARNING: No policy files found in org/4-quality/policies/")
        return 0

    all_errors: list[str] = []
    all_ok: list[str] = []

    for policy in policy_files:
        errors = validate_policy(policy)
        rel = str(policy.relative_to(REPO))
        if errors:
            all_errors.extend(errors)
            if fix_mode:
                print(f"\n  Suggestions for {rel}:")
                print(f"  {suggest_fix(policy)}")
        else:
            all_ok.append(rel)
            print(f"  ✓  {rel}")

    if all_errors:
        print(f"\n{len(all_errors)} policy structure error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    print(f"\nPolicy structure validation passed ({len(all_ok)} policies checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
