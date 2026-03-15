#!/usr/bin/env python3
"""
Compliance mapping validation for Agentic Enterprise policies.

Validates:
  - Compliance Mapping sections in quality policies parse as markdown tables
  - Framework names normalize to a known set of supported standards
  - Control identifiers follow expected framework-specific formats
  - Primary compliance reference docs exist for frameworks cited in policy mappings
  - Re-used control IDs with materially different descriptions are surfaced

Closes #116.

Usage:
  python3 scripts/validate_compliance_mapping.py

Exit codes:
  0  All validations passed
  1  One or more validation failures
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()
POLICIES_DIR = REPO / "org" / "4-quality" / "policies"
COMPLIANCE_README = REPO / "docs" / "compliance" / "README.md"


@dataclass(frozen=True)
class MappingRow:
    policy: Path
    framework: str
    control: str
    description: str


FRAMEWORK_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^SOC 2\b", re.IGNORECASE), "SOC 2"),
    (re.compile(r"^ISO(?:/IEC)? 27001(?::2022)?\b", re.IGNORECASE), "ISO 27001"),
    (re.compile(r"^GDPR\b", re.IGNORECASE), "GDPR"),
    (re.compile(r"^ISO(?:/IEC)? 42001(?::2023)?\b", re.IGNORECASE), "ISO 42001"),
    (re.compile(r"^NIST AI RMF\b", re.IGNORECASE), "NIST AI RMF"),
    (re.compile(r"^EU AI Act\b", re.IGNORECASE), "EU AI Act"),
    (re.compile(r"^NIST SP 800-53\b", re.IGNORECASE), "NIST SP 800-53"),
    (re.compile(r"^NIST SP 800-60\b", re.IGNORECASE), "NIST SP 800-60"),
    (re.compile(r"^NIST SP 800-57\b", re.IGNORECASE), "NIST SP 800-57"),
    (re.compile(r"^NIST SP 800-175B\b", re.IGNORECASE), "NIST SP 800-175B"),
    (re.compile(r"^PCI DSS(?: v\d+(?:\.\d+)?)?\b", re.IGNORECASE), "PCI DSS"),
]

PRIMARY_FRAMEWORK_DOCS = {
    "SOC 2": REPO / "docs" / "compliance" / "soc2.md",
    "ISO 27001": REPO / "docs" / "compliance" / "iso-27001.md",
    "GDPR": REPO / "docs" / "compliance" / "gdpr.md",
    "ISO 42001": REPO / "docs" / "compliance" / "iso-42001.md",
    "NIST AI RMF": REPO / "docs" / "compliance" / "nist-ai-rmf.md",
    "EU AI Act": REPO / "docs" / "compliance" / "eu-ai-act.md",
}

CONTROL_PATTERNS = {
    "SOC 2": re.compile(r"(CC\d(?:\.\d+)?|A1(?:\.\d+)?|PI1(?:\.\d+)?|C1(?:\.\d+)?|P\d(?:\.\d+)?)"),
    "ISO 27001": re.compile(r"(A\.\d+\.\d+(?:\.\d+)?)"),
    "GDPR": re.compile(r"(Art\. \d+(?:\(\d+\))?(?:[–-]\d+(?:\(\d+\))?)?)"),
    "ISO 42001": re.compile(r"((?:A\.\d+|\d+(?:\.\d+)?(?:[–-]\d+(?:\.\d+)?)?))"),
    "NIST AI RMF": re.compile(r"((?:GOVERN|MAP|MEASURE|MANAGE)(?:\s+\d+(?:\.\d+)?)?)"),
    "EU AI Act": re.compile(r"(Art\. \d+(?:[–-]\d+)?)"),
    "NIST SP 800-53": re.compile(r"([A-Z]{2,3}-\d+(?:\(\d+\))?)"),
    "NIST SP 800-60": re.compile(r"([A-Za-z][A-Za-z0-9 /-]+)"),
    "NIST SP 800-57": re.compile(r"([A-Za-z][A-Za-z0-9 /-]+)"),
    "NIST SP 800-175B": re.compile(r"([A-Za-z][A-Za-z0-9 /-]+)"),
    "PCI DSS": re.compile(r"(Req ?\d+(?:\.\d+)?)"),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def format_rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def extract_markdown_section(text: str, heading_fragment: str) -> str | None:
    lines = text.splitlines()
    in_section = False
    collected: list[str] = []

    for line in lines:
        if re.match(r"^##\s+", line):
            if in_section:
                break
            if heading_fragment.lower() in line.lower():
                in_section = True
                continue
        elif in_section:
            collected.append(line)

    if not in_section:
        return None
    return "\n".join(collected).strip()


def parse_markdown_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    for index in range(len(lines) - 1):
        if not lines[index].startswith("|"):
            continue
        if not lines[index + 1].startswith("|"):
            continue

        header_cells = [cell.strip() for cell in lines[index].strip("|").split("|")]
        separator_cells = [cell.strip() for cell in lines[index + 1].strip("|").split("|")]
        if not header_cells or any(not set(cell) <= {"-", ":"} for cell in separator_cells):
            continue

        rows: list[dict[str, str]] = []
        for row_line in lines[index + 2:]:
            if not row_line.startswith("|"):
                break
            cells = [cell.strip() for cell in row_line.strip("|").split("|")]
            if len(cells) != len(header_cells):
                continue
            rows.append(dict(zip(header_cells, cells)))
        return header_cells, rows

    return [], []


def normalize_framework(value: str) -> str | None:
    cleaned = re.sub(r"\*+", "", value).strip()
    for pattern, normalized in FRAMEWORK_PATTERNS:
        if pattern.search(cleaned):
            return normalized
    return None


def extract_control_ids(framework: str, value: str) -> list[str]:
    pattern = CONTROL_PATTERNS.get(framework)
    if pattern is None:
        return []
    return pattern.findall(re.sub(r"\*+", "", value))


def normalize_description(value: str) -> str:
    cleaned = re.sub(r"\*+", "", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip().lower()
    return cleaned


def find_control_column(headers: list[str]) -> str | None:
    for header in headers:
        lower = header.lower()
        if "control" in lower or "requirement" in lower:
            return header
    return None


def find_framework_column(headers: list[str]) -> str | None:
    for header in headers:
        if "framework" in header.lower():
            return header
    return headers[0] if headers else None


def validate_policy_mappings(path: Path) -> tuple[list[str], list[str], list[MappingRow]]:
    errors: list[str] = []
    warnings: list[str] = []
    rows_out: list[MappingRow] = []

    section = extract_markdown_section(read_text(path), "Compliance Mapping")
    if section is None:
        return errors, warnings, rows_out

    headers, rows = parse_markdown_table(section)
    rel = format_rel(path)
    if not headers or not rows:
        errors.append(f"{rel}: Compliance Mapping section missing a parseable markdown table")
        return errors, warnings, rows_out

    framework_col = find_framework_column(headers)
    control_col = find_control_column(headers)
    if framework_col is None or control_col is None:
        errors.append(
            f"{rel}: Compliance Mapping table must include framework and control/requirement columns"
        )
        return errors, warnings, rows_out

    for row in rows:
        raw_framework = row.get(framework_col, "")
        normalized_framework = normalize_framework(raw_framework)
        if normalized_framework is None:
            errors.append(f"{rel}: unknown framework in Compliance Mapping row: {raw_framework!r}")
            continue

        raw_control = row.get(control_col, "")
        control_ids = extract_control_ids(normalized_framework, raw_control)
        if not control_ids:
            errors.append(
                f"{rel}: control/reference {raw_control!r} does not match expected format for "
                f"{normalized_framework}"
            )
            continue

        description = raw_control
        for control_id in control_ids:
            rows_out.append(
                MappingRow(
                    policy=path,
                    framework=normalized_framework,
                    control=control_id,
                    description=description,
                )
            )

    return errors, warnings, rows_out


def validate_reference_docs(frameworks: set[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    readme_text = read_text(COMPLIANCE_README)

    for framework in sorted(frameworks):
        doc_path = PRIMARY_FRAMEWORK_DOCS.get(framework)
        if doc_path is None:
            continue
        if not doc_path.exists():
            errors.append(
                f"docs/compliance: missing reference document for framework '{framework}'"
            )
            continue
        doc_text = read_text(doc_path)
        if framework not in doc_text:
            warnings.append(
                f"{format_rel(doc_path)}: framework name '{framework}' is not explicitly mentioned"
            )
        if doc_path.name not in readme_text:
            errors.append(
                f"{format_rel(COMPLIANCE_README)}: missing index entry for {format_rel(doc_path)}"
            )

    return errors, warnings


def validate_consistency(rows: list[MappingRow]) -> list[str]:
    warnings: list[str] = []
    grouped: dict[tuple[str, str], list[MappingRow]] = defaultdict(list)
    for row in rows:
        grouped[(row.framework, row.control)].append(row)

    for (framework, control), entries in sorted(grouped.items()):
        policy_names = {format_rel(entry.policy) for entry in entries}
        if len(policy_names) < 2:
            continue

        descriptions = {
            normalize_description(entry.description): entry.description
            for entry in entries
            if entry.description.strip()
        }
        if len(descriptions) <= 1:
            continue

        normalized_values = list(descriptions.keys())
        if any(a in b or b in a for a in normalized_values for b in normalized_values if a != b):
            continue

        warnings.append(
            f"{framework} {control}: reused across policies with different descriptions "
            f"({', '.join(sorted(policy_names))})"
        )

    return warnings


def main() -> int:
    all_errors: list[str] = []
    all_warnings: list[str] = []
    mapping_rows: list[MappingRow] = []
    frameworks_seen: set[str] = set()
    policies_with_sections = 0

    for path in sorted(POLICIES_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        errors, warnings, rows = validate_policy_mappings(path)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        if rows:
            policies_with_sections += 1
            mapping_rows.extend(rows)
            frameworks_seen.update(row.framework for row in rows)

    if policies_with_sections == 0:
        all_errors.append("No policy Compliance Mapping sections were found to validate")

    errors, warnings = validate_reference_docs(frameworks_seen)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    all_warnings.extend(validate_consistency(mapping_rows))

    if all_warnings:
        print(f"{len(all_warnings)} warning(s):")
        for warning in all_warnings:
            print(f"  ⚠  {warning}")
        print()

    if all_errors:
        print(f"{len(all_errors)} compliance mapping error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    print(
        f"Compliance mapping validation passed "
        f"({policies_with_sections} policy sections, {len(mapping_rows)} mapping rows)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
