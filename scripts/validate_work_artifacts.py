#!/usr/bin/env python3
"""
Work artifact validation for Agentic Enterprise framework.

Validates decision records, governance exceptions, retrospectives,
and technical designs have required sections and fields.

Extends validate_schema.py coverage (which handles signals, missions, releases).

Closes #113.

Usage:
  python3 scripts/validate_work_artifacts.py [--root <path>]

  --root <path>   Validate against an alternate root directory
                  (e.g., examples/e2e-loop) instead of the repo root.
                  The directory must contain a work/ subdirectory.

Exit codes:
  0  All validations passed
  1  One or more validation failures
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()


# ── Helpers ──────────────────────────────────────────────────────────────────

def is_template(path: Path) -> bool:
    return "_TEMPLATE" in path.name


def get_sections(text: str) -> set[str]:
    """Return set of second-level heading titles (## ...)."""
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+)", text, re.MULTILINE)}


def has_field(text: str, field_name: str) -> bool:
    """Check if a bold field exists in text."""
    return bool(re.search(rf"\*\*{re.escape(field_name)}[:\*]", text))


def validate_file(
    path: Path,
    required_sections: list[str],
    required_fields: list[str],
    artifact_type: str,
    root: Path | None = None,
) -> list[str]:
    """Validate a single work artifact file."""
    errors: list[str] = []
    base = root or REPO
    rel = str(path.relative_to(base))

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read — {exc}"]

    sections = get_sections(text)

    for section in required_sections:
        # Flexible match: section name may appear as substring
        found = any(section.lower() in s.lower() for s in sections)
        if not found:
            errors.append(f"{rel}: missing required section '## {section}' ({artifact_type})")

    for field in required_fields:
        if not has_field(text, field):
            errors.append(f"{rel}: missing required field '**{field}**' ({artifact_type})")

    return errors


# ── Artifact type definitions ────────────────────────────────────────────────

DECISION_RECORD = {
    "glob": "work/decisions/*.md",
    "type": "decision record",
    "required_sections": ["Context", "Decision", "Alternatives Considered", "Consequences"],
    "required_fields": ["Decision ID", "Status"],
}

GOVERNANCE_EXCEPTION = {
    "glob": "work/decisions/EXC-*.md",
    "type": "governance exception",
    "required_sections": ["Summary", "Details"],
    "required_fields": ["Exception ID", "Risk", "Mitigation"],
}

RETROSPECTIVE = {
    "glob": "work/retrospectives/*.md",
    "type": "retrospective/postmortem",
    "required_sections": ["Timeline", "Root Cause", "Follow-Up"],
    "required_fields": ["Incident ID", "Severity", "Status"],
}

TECHNICAL_DESIGN = {
    "glob": "work/missions/*/technical-design.md",
    "type": "technical design",
    "required_sections": ["Context", "Observability Design", "Architecture Decisions"],
    "required_fields": ["Mission ID", "Status"],
}

# Also check for Observability Design in any file named *technical-design*
TECHNICAL_DESIGN_ALT = {
    "glob": "work/missions/**/technical-design*.md",
    "type": "technical design",
    "required_sections": ["Observability Design"],
    "required_fields": [],
}


# ── Discovery ────────────────────────────────────────────────────────────────

def discover_artifacts(base_dir: Path, glob_pattern: str) -> list[Path]:
    """Find non-template, non-README markdown files matching pattern."""
    return [
        p for p in base_dir.glob(glob_pattern)
        if p.is_file()
        and not is_template(p)
        and p.name != "README.md"
    ]


# ── Main ─────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate work artifact structure")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Alternate root directory containing a work/ subdirectory (e.g., examples/e2e-loop)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve() if args.root else REPO

    if not (root / "work").exists():
        print(f"ERROR: No work/ directory found in {root}")
        return 1

    all_errors: list[str] = []
    all_ok: list[str] = []

    artifact_configs = [
        ("Decision records", "work/decisions/*.md", DECISION_RECORD, ["EXC-", "DPA-", "DPIA-", "RISK-"]),
        ("Governance exceptions", "work/decisions/EXC-*.md", GOVERNANCE_EXCEPTION, []),
        ("Retrospectives", "work/retrospectives/*.md", RETROSPECTIVE, []),
    ]

    for label, glob_pattern, config, exclude_prefixes in artifact_configs:
        files = discover_artifacts(root, glob_pattern)

        # For decision records, exclude governance exceptions and other sub-types
        if exclude_prefixes:
            files = [
                f for f in files
                if not any(f.name.startswith(prefix) for prefix in exclude_prefixes)
            ]

        if not files:
            print(f"INFO: No {label.lower()} found — skipping.")
            continue

        print(f"Validating {label}...")
        for f in files:
            errors = validate_file(
                f,
                config["required_sections"],
                config["required_fields"],
                config["type"],
                root=root,
            )
            rel = str(f.relative_to(root))
            if errors:
                all_errors.extend(errors)
            else:
                all_ok.append(rel)
                print(f"  ✓  {rel}")

    # Technical designs (search recursively under work/missions/ only)
    missions_dir = root / "work" / "missions"
    all_tech = []
    if missions_dir.exists():
        all_tech = [
            p for p in missions_dir.rglob("technical-design*.md")
            if p.is_file() and not is_template(p)
        ]

    if all_tech:
        print("Validating technical designs...")
        for f in all_tech:
            errors = validate_file(
                f,
                TECHNICAL_DESIGN["required_sections"],
                TECHNICAL_DESIGN["required_fields"],
                TECHNICAL_DESIGN["type"],
                root=root,
            )
            rel = str(f.relative_to(root))
            if errors:
                all_errors.extend(errors)
            else:
                all_ok.append(rel)
                print(f"  ✓  {rel}")
    else:
        print("INFO: No technical designs found — skipping.")

    # ── Template structure validation ─────────────────────────────────────
    # Validate that templates themselves have required sections
    # (ensures new instances will be guided correctly)
    # Skipped when using --root (templates live in the main repo root)
    if root == REPO:
        print("Validating work artifact templates...")
        template_checks = [
            (
                REPO / "work" / "decisions" / "_TEMPLATE-decision-record.md",
                DECISION_RECORD,
            ),
            (
                REPO / "work" / "decisions" / "_TEMPLATE-governance-exception.md",
                GOVERNANCE_EXCEPTION,
            ),
            (
                REPO / "work" / "retrospectives" / "_TEMPLATE-postmortem.md",
                RETROSPECTIVE,
            ),
            (
                REPO / "work" / "missions" / "_TEMPLATE-technical-design.md",
                TECHNICAL_DESIGN,
            ),
        ]

        for template_path, config in template_checks:
            if not template_path.exists():
                print(f"  ⚠  Template not found: {template_path.relative_to(REPO)}")
                continue

            errors = validate_file(
                template_path,
                config["required_sections"],
                config["required_fields"],
                f"{config['type']} template",
            )
            rel = str(template_path.relative_to(REPO))
            if errors:
                all_errors.extend(errors)
            else:
                all_ok.append(rel)
                print(f"  ✓  {rel}")

    # ── Report ────────────────────────────────────────────────────────────
    if all_errors:
        print(f"\n{len(all_errors)} work artifact error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    total = len(all_ok)
    print(f"\nWork artifact validation passed ({total} artifact(s) checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
