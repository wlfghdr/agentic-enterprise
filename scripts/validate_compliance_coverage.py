#!/usr/bin/env python3
"""
Compliance coverage gap validation for Agentic Enterprise policies.

Validates:
  - Documented compliance controls/clauses/articles are extracted from all
    primary reference docs in docs/compliance/
  - Quality policy Compliance Mapping tables reference those frameworks using
    parseable control identifiers
  - Unmapped documented controls are reported per standard
  - Standards exceeding a configurable unmapped percentage threshold are warned

Closes #165.

Usage:
  python3 scripts/validate_compliance_coverage.py
  python3 scripts/validate_compliance_coverage.py --warn-unmapped-pct 20

Exit codes:
  0  Validation completed (warnings may be present)
  1  Extraction or parsing errors prevented a reliable coverage report
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()
POLICIES_DIR = REPO / "org" / "4-quality" / "policies"
COMPLIANCE_DOCS = {
    "CCPA/CPRA": REPO / "docs" / "compliance" / "ccpa-cpra.md",
    "EU AI Act": REPO / "docs" / "compliance" / "eu-ai-act.md",
    "GDPR": REPO / "docs" / "compliance" / "gdpr.md",
    "HIPAA": REPO / "docs" / "compliance" / "hipaa.md",
    "ISO 22301": REPO / "docs" / "compliance" / "iso-22301.md",
    "ISO 27001": REPO / "docs" / "compliance" / "iso-27001.md",
    "ISO 42001": REPO / "docs" / "compliance" / "iso-42001.md",
    "ISO 9001": REPO / "docs" / "compliance" / "iso-9001.md",
    "NIST AI RMF": REPO / "docs" / "compliance" / "nist-ai-rmf.md",
    "NIST CSF": REPO / "docs" / "compliance" / "nist-csf.md",
    "SOC 2": REPO / "docs" / "compliance" / "soc2.md",
}

FRAMEWORK_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^CCPA/CPRA\b", re.IGNORECASE), "CCPA/CPRA"),
    (re.compile(r"^SOC 2\b", re.IGNORECASE), "SOC 2"),
    (re.compile(r"^ISO(?:/IEC)? 22301(?::2019)?\b", re.IGNORECASE), "ISO 22301"),
    (re.compile(r"^ISO(?:/IEC)? 27001(?::2022)?\b", re.IGNORECASE), "ISO 27001"),
    (re.compile(r"^ISO(?:/IEC)? 42001(?::2023)?\b", re.IGNORECASE), "ISO 42001"),
    (re.compile(r"^ISO 9001(?::2015)?\b", re.IGNORECASE), "ISO 9001"),
    (re.compile(r"^GDPR\b", re.IGNORECASE), "GDPR"),
    (re.compile(r"^HIPAA\b", re.IGNORECASE), "HIPAA"),
    (re.compile(r"^NIST AI RMF\b", re.IGNORECASE), "NIST AI RMF"),
    (re.compile(r"^NIST CSF(?: 2\.0)?\b", re.IGNORECASE), "NIST CSF"),
    (re.compile(r"^EU AI Act\b", re.IGNORECASE), "EU AI Act"),
]

DOC_TABLE_ID_HEADERS = {
    "article",
    "category",
    "clause",
    "control",
    "criterion",
    "function",
    "section",
    "standard",
}
DOC_TABLE_SKIP_HEADERS = {
    "ccpa/cpra theme",
    "genai risk",
    "iso 22301 concept",
    "qmp principle",
}

SOC2_TOKEN_RE = re.compile(
    r"\b(?:CC\d(?:\.\d+)?|A1(?:\.\d+)?|PI1(?:\.\d+)?|C1(?:\.\d+)?|P\d(?:\.\d+)?)"
    r"(?:[–-](?:CC\d(?:\.\d+)?|A1(?:\.\d+)?|PI1(?:\.\d+)?|C1(?:\.\d+)?|P\d(?:\.\d+)?))?\b"
)
SOC2_ID_RE = re.compile(r"([A-Z]+)(\d+)(?:\.(\d+))?")
ARTICLE_TOKEN_RE = re.compile(
    r"Art\. \d+(?:\(\d+\))?(?:\([a-z]\))?(?:[–-]\d+(?:\(\d+\))?(?:\([a-z]\))?)?"
)
SECTION_TOKEN_RE = re.compile(r"§\d+\.\d+(?:\([A-Za-z0-9]+\))*")
ISO_TOKEN_RE = re.compile(r"(?:A\.\d+(?:\.\d+){0,2}|\d+\.\d+(?:[–-]\d+\.\d+)?)")
NIST_AI_RMF_TOKEN_RE = re.compile(r"\b(?:GOVERN|MAP|MEASURE|MANAGE)(?:\s+\d+(?:\.\d+)?)?\b")
NIST_CSF_TOKEN_RE = re.compile(
    r"\b[A-Z]{2}\.[A-Z]{2}-\d{2}(?:[–-](?:[A-Z]{2}\.)?[A-Z]{2}-\d{2})?\b"
)


@dataclass(frozen=True)
class PolicyRequirement:
    policy: Path
    framework: str
    raw_requirement: str
    identifiers: tuple[str, ...]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def format_rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def clean_inline_markdown(value: str) -> str:
    cleaned = re.sub(r"\*+", "", value)
    cleaned = cleaned.replace("`", "")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


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


def parse_markdown_tables(section: str) -> list[tuple[list[str], list[dict[str, str]]]]:
    lines = [line.rstrip() for line in section.splitlines()]
    tables: list[tuple[list[str], list[dict[str, str]]]] = []
    index = 0

    while index < len(lines) - 1:
        current = lines[index].strip()
        next_line = lines[index + 1].strip()
        if not current.startswith("|") or not next_line.startswith("|"):
            index += 1
            continue

        headers = [cell.strip() for cell in current.strip("|").split("|")]
        separators = [cell.strip() for cell in next_line.strip("|").split("|")]
        if not headers or any(not set(cell) <= {"-", ":"} for cell in separators):
            index += 1
            continue

        rows: list[dict[str, str]] = []
        row_index = index + 2
        while row_index < len(lines):
            row_line = lines[row_index].strip()
            if not row_line.startswith("|"):
                break
            cells = [cell.strip() for cell in row_line.strip("|").split("|")]
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
            row_index += 1

        tables.append((headers, rows))
        index = row_index

    return tables


def normalize_framework(value: str) -> str | None:
    cleaned = clean_inline_markdown(value)
    for pattern, normalized in FRAMEWORK_PATTERNS:
        if pattern.search(cleaned):
            return normalized
    return None


def split_range_token(token: str) -> tuple[str, str | None]:
    normalized = token.replace("–", "-")
    if "-" not in normalized:
        return normalized, None
    start, end = normalized.split("-", 1)
    return start.strip(), end.strip()


def expand_soc2_token(token: str) -> list[str]:
    start, end = split_range_token(token)
    if end is None:
        return [start]

    start_match = SOC2_ID_RE.fullmatch(start)
    end_match = SOC2_ID_RE.fullmatch(end)
    if not start_match or not end_match:
        return [start, end]

    prefix_a, major_a, minor_a = start_match.groups()
    prefix_b, major_b, minor_b = end_match.groups()
    if prefix_a != prefix_b:
        return [start, end]

    if minor_a is not None and minor_b is not None and major_a == major_b:
        return [f"{prefix_a}{major_a}.{value}" for value in range(int(minor_a), int(minor_b) + 1)]

    if minor_a is None and minor_b is None:
        return [f"{prefix_a}{value}" for value in range(int(major_a), int(major_b) + 1)]

    return [start, end]


def expand_article_token(token: str) -> list[str]:
    start, end = split_range_token(token)
    if end is None:
        return [start]

    match = re.fullmatch(r"Art\. (\d+)-(\d+)", f"{start}-{end}")
    if not match:
        return [start, end]

    first, last = (int(value) for value in match.groups())
    return [f"Art. {value}" for value in range(first, last + 1)]


def expand_iso_token(token: str) -> list[str]:
    start, end = split_range_token(token)
    if end is None or start.startswith("A."):
        return [start]

    match = re.fullmatch(r"(\d+)\.(\d+)-(\d+)\.(\d+)", f"{start}-{end}")
    if not match:
        return [start, end]

    major_a, minor_a, major_b, minor_b = (int(value) for value in match.groups())
    if major_a != major_b:
        return [start, end]

    return [f"{major_a}.{value}" for value in range(minor_a, minor_b + 1)]


def expand_nist_csf_token(token: str) -> list[str]:
    match = re.fullmatch(
        r"([A-Z]{2})\.([A-Z]{2})-(\d{2})[–-](?:(?:([A-Z]{2})\.)?([A-Z]{2})-)?(\d{2})",
        token,
    )
    if match is None:
        return [token]

    prefix_a, family_a, start_value, prefix_b, family_b, end_value = match.groups()
    prefix_b = prefix_b or prefix_a
    family_b = family_b or family_a
    if prefix_a != prefix_b or family_a != family_b:
        return [token]

    return [
        f"{prefix_a}.{family_a}-{value:02d}"
        for value in range(int(start_value), int(end_value) + 1)
    ]


def extract_framework_ids(framework: str, value: str) -> list[str]:
    cleaned = clean_inline_markdown(value)
    if not cleaned:
        return []

    if framework == "SOC 2":
        return unique(
            [
                expanded
                for match in SOC2_TOKEN_RE.finditer(cleaned)
                for expanded in expand_soc2_token(match.group(0))
            ]
        )
    if framework in {"GDPR", "EU AI Act"}:
        return unique(
            [
                expanded
                for match in ARTICLE_TOKEN_RE.finditer(cleaned)
                for expanded in expand_article_token(match.group(0))
            ]
        )
    if framework in {"CCPA/CPRA", "HIPAA"}:
        return unique([match.group(0) for match in SECTION_TOKEN_RE.finditer(cleaned)])
    if framework in {"ISO 22301", "ISO 27001", "ISO 42001", "ISO 9001"}:
        return unique(
            [
                expanded
                for match in ISO_TOKEN_RE.finditer(cleaned)
                for expanded in expand_iso_token(match.group(0))
            ]
        )
    if framework == "NIST AI RMF":
        return unique([match.group(0) for match in NIST_AI_RMF_TOKEN_RE.finditer(cleaned)])
    if framework == "NIST CSF":
        return unique(
            [
                expanded
                for match in NIST_CSF_TOKEN_RE.finditer(cleaned)
                for expanded in expand_nist_csf_token(match.group(0))
            ]
        )
    return []


def extract_documented_targets(framework: str, path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    section = extract_markdown_section(read_text(path), "How This Framework Addresses It")
    if section is None:
        return [f"{format_rel(path)}: missing 'How This Framework Addresses It' section"], []

    documented: list[str] = []
    for headers, rows in parse_markdown_tables(section):
        if not headers:
            continue
        first_header = headers[0].strip().lower()
        if first_header in DOC_TABLE_SKIP_HEADERS or first_header not in DOC_TABLE_ID_HEADERS:
            continue

        id_column = headers[0]
        for row in rows:
            raw_identifier = row.get(id_column, "")
            identifiers = extract_framework_ids(framework, raw_identifier)
            if not identifiers:
                errors.append(
                    f"{format_rel(path)}: could not extract {framework} identifiers from "
                    f"{raw_identifier!r}"
                )
                continue
            documented.extend(identifiers)

    documented = unique(documented)
    if not documented:
        errors.append(
            f"{format_rel(path)}: no documented {framework} control identifiers found in section 2"
        )
    return errors, documented


def find_framework_column(headers: list[str]) -> str | None:
    for header in headers:
        if "framework" in header.lower():
            return header
    return headers[0] if headers else None


def find_requirement_column(headers: list[str]) -> str | None:
    for header in headers:
        lower = header.lower()
        if "control" in lower or "requirement" in lower:
            return header
    return None


def extract_policy_requirements() -> tuple[list[str], list[PolicyRequirement]]:
    errors: list[str] = []
    requirements: list[PolicyRequirement] = []

    for path in sorted(POLICIES_DIR.glob("*.md")):
        if path.name == "README.md":
            continue

        section = extract_markdown_section(read_text(path), "Compliance Mapping")
        if section is None:
            continue

        headers, rows = parse_markdown_table(section)
        rel = format_rel(path)
        if not headers or not rows:
            errors.append(f"{rel}: Compliance Mapping section missing a parseable markdown table")
            continue

        framework_column = find_framework_column(headers)
        requirement_column = find_requirement_column(headers)
        if framework_column is None or requirement_column is None:
            errors.append(
                f"{rel}: Compliance Mapping table must include framework and control/requirement columns"
            )
            continue

        for row in rows:
            framework = normalize_framework(row.get(framework_column, ""))
            if framework is None or framework not in COMPLIANCE_DOCS:
                continue

            raw_requirement = row.get(requirement_column, "")
            identifiers = extract_framework_ids(framework, raw_requirement)
            if not identifiers:
                errors.append(
                    f"{rel}: could not extract {framework} identifier(s) from requirement "
                    f"{raw_requirement!r}"
                )
                continue

            requirements.append(
                PolicyRequirement(
                    policy=path,
                    framework=framework,
                    raw_requirement=raw_requirement,
                    identifiers=tuple(identifiers),
                )
            )

    return errors, requirements


def build_coverage_index(requirements: list[PolicyRequirement]) -> dict[str, set[str]]:
    coverage: dict[str, set[str]] = {}
    for requirement in requirements:
        coverage.setdefault(requirement.framework, set()).update(requirement.identifiers)
    return coverage


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report compliance coverage gaps between reference docs and policy mappings."
    )
    parser.add_argument(
        "--warn-unmapped-pct",
        type=float,
        default=25.0,
        help="Warn when a framework has more than this percentage of documented controls unmapped.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    all_errors: list[str] = []
    documented_targets: dict[str, list[str]] = {}

    for framework, path in COMPLIANCE_DOCS.items():
        if not path.exists():
            all_errors.append(f"Missing compliance reference document: {format_rel(path)}")
            continue

        errors, identifiers = extract_documented_targets(framework, path)
        all_errors.extend(errors)
        if identifiers:
            documented_targets[framework] = identifiers

    policy_errors, requirements = extract_policy_requirements()
    all_errors.extend(policy_errors)

    if all_errors:
        print(f"{len(all_errors)} compliance coverage error(s):")
        for error in all_errors:
            print(f"  ✗  {error}")
        return 1

    coverage_index = build_coverage_index(requirements)
    warnings: list[str] = []

    total_documented = 0
    total_mapped = 0

    print(
        f"Compliance coverage summary (warn threshold: > {args.warn_unmapped_pct:.1f}% unmapped)\n"
    )

    for framework, path in COMPLIANCE_DOCS.items():
        targets = documented_targets.get(framework, [])
        mapped_ids = coverage_index.get(framework, set())
        uncovered = [identifier for identifier in targets if identifier not in mapped_ids]
        mapped_count = len(targets) - len(uncovered)
        total_documented += len(targets)
        total_mapped += mapped_count

        unmapped_pct = 0.0 if not targets else (len(uncovered) / len(targets)) * 100
        print(
            f"- {framework}: {mapped_count}/{len(targets)} mapped "
            f"({100 - unmapped_pct:.1f}% coverage) [{format_rel(path)}]"
        )
        if uncovered:
            print(f"  unmapped: {', '.join(uncovered)}")

        if unmapped_pct > args.warn_unmapped_pct:
            warnings.append(
                f"{framework}: {len(uncovered)}/{len(targets)} documented controls are unmapped "
                f"({unmapped_pct:.1f}% unmapped)"
            )

    overall_coverage = 0.0 if total_documented == 0 else (total_mapped / total_documented) * 100
    print(
        f"\nOverall documented coverage: {total_mapped}/{total_documented} "
        f"({overall_coverage:.1f}%)"
    )

    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  ⚠  {warning}")

    print("\nCompliance coverage validation completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
