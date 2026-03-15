#!/usr/bin/env python3
"""
Agent instruction hierarchy validation for Agentic Enterprise framework.

Validates:
  - Layer AGENT.md files have required sections and metadata
  - Division DIVISION.md files have required fields
  - Agent type definitions in org/agents/ conform to template structure
  - Instruction hierarchy references are consistent

Closes #112.

Usage:
  python3 scripts/validate_agent_instructions.py

Exit codes:
  0  All validations passed
  1  One or more validation failures
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()

LAYERS = [
    "0-steering",
    "1-strategy",
    "2-orchestration",
    "3-execution",
    "4-quality",
]

# ── Required metadata for AGENT.md files ─────────────────────────────────────

AGENT_REQUIRED_METADATA = [
    ("Version", r"\*\*Version:\*\*\s*(\d+\.\d+)"),
    ("Last updated", r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})"),
]

# ── Required sections for AGENT.md files ─────────────────────────────────────
# These are checked flexibly — some layers use slightly different names

AGENT_REQUIRED_SECTIONS = [
    "Changelog",
]

# At least one of these "purpose/identity" sections must exist
AGENT_PURPOSE_SECTIONS = [
    "Your Purpose",
    "Identity",
    "Role",
    "Purpose",
]

# At least one of these "responsibilities" sections must exist
AGENT_RESPONSIBILITY_SECTIONS = [
    "What You Do",
    "Responsibilities",
    "What You Own",
    "Core Responsibilities",
    "Evaluation Protocol",  # Quality layer equivalent
]

# ── Required metadata for DIVISION.md files ──────────────────────────────────

DIVISION_REQUIRED_METADATA = [
    ("Owner", r"\*\*Owner:\*\*\s*(.+)"),
    ("Type", r"\*\*Type:\*\*\s*(.+)"),
    ("Layer", r"\*\*Layer:\*\*\s*(.+)"),
    ("Status", r"\*\*Status:\*\*\s*(.+)"),
    ("Version", r"\*\*Version:\*\*\s*(\d+\.\d+)"),
    ("Last updated", r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})"),
]

DIVISION_REQUIRED_SECTIONS = [
    "Purpose",
    "Scope",
    "Changelog",
]

# ── Required fields for agent type definitions ───────────────────────────────

AGENT_TYPE_REQUIRED_SECTIONS = [
    "Identity",
    "Classification",
    "Lifecycle",
    "Description",
    "Capabilities",
    "Changelog",
]

AGENT_TYPE_REQUIRED_METADATA = [
    ("Template version", r"\*\*Template version:\*\*\s*(\d+\.\d+)"),
    ("Last updated", r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})"),
]


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_sections(text: str) -> set[str]:
    """Return set of second-level heading titles (## ...)."""
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+)", text, re.MULTILINE)}


def has_any_section(sections: set[str], candidates: list[str]) -> bool:
    """Check if any candidate section name appears (case-insensitive partial match)."""
    for candidate in candidates:
        for section in sections:
            if candidate.lower() in section.lower():
                return True
    return False


def check_metadata(text: str, required: list[tuple[str, str]], rel: str) -> list[str]:
    """Check required metadata fields. Returns error messages."""
    errors = []
    for name, pattern in required:
        if not re.search(pattern, text):
            errors.append(f"{rel}: missing required metadata '**{name}:**'")
    return errors


def check_hierarchy_reference(text: str, rel: str) -> list[str]:
    """Check that an AGENT.md references the parent AGENTS.md."""
    errors = []
    # Check for reference to global instructions
    has_agents_ref = any(term in text for term in [
        "AGENTS.md", "CLAUDE.md", "Agent Instructions (Global)",
        "global agent rules", "Global Rules",
    ])
    if not has_agents_ref:
        errors.append(f"{rel}: no reference to parent AGENTS.md / global instructions found")
    return errors


# ── Validators ───────────────────────────────────────────────────────────────

def validate_layer_agent(path: Path) -> list[str]:
    """Validate a layer AGENT.md file."""
    errors: list[str] = []
    rel = str(path.relative_to(REPO))

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read — {exc}"]

    # Metadata
    errors.extend(check_metadata(text, AGENT_REQUIRED_METADATA, rel))

    # Required sections
    sections = get_sections(text)
    for section in AGENT_REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"{rel}: missing required section '## {section}'")

    # Purpose/Identity section (flexible)
    if not has_any_section(sections, AGENT_PURPOSE_SECTIONS):
        errors.append(
            f"{rel}: missing purpose/identity section "
            f"(expected one of: {', '.join(AGENT_PURPOSE_SECTIONS)})"
        )

    # Responsibilities section (flexible)
    if not has_any_section(sections, AGENT_RESPONSIBILITY_SECTIONS):
        errors.append(
            f"{rel}: missing responsibilities section "
            f"(expected one of: {', '.join(AGENT_RESPONSIBILITY_SECTIONS)})"
        )

    # Hierarchy reference
    errors.extend(check_hierarchy_reference(text, rel))

    return errors


def validate_division(path: Path) -> list[str]:
    """Validate a DIVISION.md file."""
    errors: list[str] = []
    rel = str(path.relative_to(REPO))

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read — {exc}"]

    # Metadata
    errors.extend(check_metadata(text, DIVISION_REQUIRED_METADATA, rel))

    # Required sections
    sections = get_sections(text)
    for section in DIVISION_REQUIRED_SECTIONS:
        if not has_any_section(sections, [section]):
            errors.append(f"{rel}: missing required section '## {section}'")

    # Layer field should say "Execution"
    layer_match = re.search(r"\*\*Layer:\*\*\s*(.+)", text)
    if layer_match:
        layer_val = layer_match.group(1).strip()
        if "execution" not in layer_val.lower():
            errors.append(f"{rel}: **Layer:** should be 'Execution', got '{layer_val}'")

    return errors


def validate_agent_type(path: Path) -> list[str]:
    """Validate an agent type definition file in org/agents/."""
    errors: list[str] = []
    rel = str(path.relative_to(REPO))

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read — {exc}"]

    # Metadata
    errors.extend(check_metadata(text, AGENT_TYPE_REQUIRED_METADATA, rel))

    # Required sections
    sections = get_sections(text)
    for section in AGENT_TYPE_REQUIRED_SECTIONS:
        if not has_any_section(sections, [section]):
            errors.append(f"{rel}: missing required section '## {section}'")

    # Classification table should have Layer field
    if not re.search(r"\*\*Layer\*\*", text):
        errors.append(f"{rel}: missing **Layer** in Classification table")

    return errors


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    all_errors: list[str] = []
    all_ok: list[str] = []

    # ── 1. Layer AGENT.md files ───────────────────────────────────────────
    print("Validating layer AGENT.md files...")
    for layer in LAYERS:
        agent_path = REPO / "org" / layer / "AGENT.md"
        if not agent_path.exists():
            all_errors.append(f"org/{layer}/AGENT.md: file not found")
            continue
        errors = validate_layer_agent(agent_path)
        rel = str(agent_path.relative_to(REPO))
        if errors:
            all_errors.extend(errors)
        else:
            all_ok.append(rel)
            print(f"  ✓  {rel}")

    # ── 2. Division DIVISION.md files ─────────────────────────────────────
    divisions_dir = REPO / "org" / "3-execution" / "divisions"
    if divisions_dir.exists():
        print("Validating division DIVISION.md files...")
        for div_dir in sorted(divisions_dir.iterdir()):
            if not div_dir.is_dir() or div_dir.name.startswith("_"):
                continue
            div_file = div_dir / "DIVISION.md"
            if not div_file.exists():
                all_errors.append(f"org/3-execution/divisions/{div_dir.name}/DIVISION.md: file not found")
                continue
            errors = validate_division(div_file)
            rel = str(div_file.relative_to(REPO))
            if errors:
                all_errors.extend(errors)
            else:
                all_ok.append(rel)
                print(f"  ✓  {rel}")

    # ── 3. Agent type definitions ─────────────────────────────────────────
    agents_dir = REPO / "org" / "agents"
    if agents_dir.exists():
        print("Validating agent type definitions...")
        for category_dir in sorted(agents_dir.iterdir()):
            if not category_dir.is_dir():
                continue
            for agent_file in sorted(category_dir.glob("*.md")):
                if "_TEMPLATE" in agent_file.name or agent_file.name == "README.md":
                    continue
                errors = validate_agent_type(agent_file)
                rel = str(agent_file.relative_to(REPO))
                if errors:
                    all_errors.extend(errors)
                else:
                    all_ok.append(rel)
                    print(f"  ✓  {rel}")

    # ── Report ────────────────────────────────────────────────────────────
    if all_errors:
        print(f"\n{len(all_errors)} agent instruction error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    print(f"\nAgent instruction validation passed ({len(all_ok)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
