#!/usr/bin/env python3
"""
Cross-reference integrity validation for Agentic Enterprise framework.

Validates:
  - Markdown path references in work artifacts resolve to existing files
  - Signal supersession references point to existing active or archived signals
  - Governance exception references point to existing, non-expired exceptions
  - Quality policy cross-references resolve, including bare file mentions

Closes #114.

Usage:
  python3 scripts/validate_cross_references.py [--root <path>]

  --root <path>   Validate work artifacts in an alternate root directory
                  (e.g., examples/e2e-loop). Repo-level policy and CONFIG
                  checks run only when validating the repository root.

Exit codes:
  0  All validations passed
  1  One or more validation failures
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()
TODAY = date.today()

WORK_DIR_NAMES = ("work", "docs", "org", "process", "examples")

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:work|docs|org|process|examples)/[^`\s]+?\.md(?:#[^`\s]+)?)`",
    re.IGNORECASE,
)
REPO_PATH_RE = re.compile(
    r"(?<![\w/])((?:work|docs|org|process|examples)/[A-Za-z0-9_./-]+\.md(?:#[A-Za-z0-9_.:-]+)?)",
    re.IGNORECASE,
)
BARE_MD_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+\.md)(?![A-Za-z0-9_./-])")
EXCEPTION_ID_RE = re.compile(r"\b(EXC-\d{4}-\d{3})\b")


@dataclass(frozen=True)
class Reference:
    line_no: int
    target: str


def is_external(target: str) -> bool:
    lower = target.lower()
    return lower.startswith(("http://", "https://", "mailto:", "tel:", "ftp://"))


def is_template(path: Path) -> bool:
    return "_TEMPLATE" in path.name


def should_skip_target(target: str) -> bool:
    value = target.strip()
    if not value:
        return True
    if is_external(value) or value.startswith("#"):
        return True
    if any(token in value for token in ("{{", "}}", "<", ">", "[", "]")):
        return True
    if "YYYY" in value or "<name>" in value.lower():
        return True
    return False


def strip_anchor(target: str) -> str:
    cleaned = target.strip()
    if cleaned.startswith("<") and cleaned.endswith(">"):
        cleaned = cleaned[1:-1].strip()
    if "#" in cleaned:
        cleaned = cleaned.split("#", 1)[0]
    return cleaned


def iter_non_code_lines(path: Path) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_fence = False
    text = path.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append((line_no, line))
    return lines


def extract_targets(path: Path, include_bare: bool) -> list[Reference]:
    refs: list[Reference] = []
    for line_no, line in iter_non_code_lines(path):
        seen: set[str] = set()

        for pattern in (MARKDOWN_LINK_RE, BACKTICK_PATH_RE, REPO_PATH_RE):
            for match in pattern.findall(line):
                target = match.strip()
                if target not in seen:
                    refs.append(Reference(line_no, target))
                    seen.add(target)

        if not include_bare:
            continue

        for match in BARE_MD_RE.findall(line):
            target = match.strip()
            if target not in seen:
                refs.append(Reference(line_no, target))
                seen.add(target)

    return refs


def resolve_target(current_file: Path, target: str, work_root: Path) -> Path | None:
    raw = strip_anchor(target)
    if should_skip_target(raw):
        return None

    if raw.startswith(("work/", "docs/", "org/", "process/", "examples/")):
        if raw.startswith("work/"):
            return (work_root / raw).resolve()
        return (REPO / raw).resolve()

    if raw.startswith(("./", "../")):
        return (current_file.parent / raw).resolve()

    if "/" in raw:
        return (current_file.parent / raw).resolve()

    for candidate in (
        (current_file.parent / raw).resolve(),
        (work_root / raw).resolve(),
        (REPO / raw).resolve(),
    ):
        if candidate.exists():
            return candidate

    repo_matches = sorted(
        path.resolve()
        for path in REPO.rglob(raw)
        if path.is_file()
    )
    if repo_matches:
        return repo_matches[0]

    template_matches = sorted(
        path.resolve()
        for path in REPO.rglob(f"_TEMPLATE-{raw}")
        if path.is_file()
    )
    if template_matches:
        return template_matches[0]

    raw_lower = raw.lower()
    ci_matches = sorted(
        path.resolve()
        for path in REPO.rglob("*.md")
        if str(path.relative_to(REPO)).lower().endswith(raw_lower)
    )
    if ci_matches:
        return ci_matches[0]

    return (current_file.parent / raw).resolve()


def filename_case_warning(target: str, resolved: Path) -> str | None:
    raw = strip_anchor(target)
    if should_skip_target(raw):
        return None

    referenced_name = Path(raw).name
    actual_name = resolved.name
    if referenced_name.lower() == actual_name.lower() and referenced_name != actual_name:
        return (
            f"filename case mismatch: referenced '{referenced_name}' "
            f"but actual file is '{actual_name}'"
        )
    return None


def rel(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def discover_work_files(root: Path) -> list[Path]:
    work_dir = root / "work"
    if not work_dir.exists():
        return []
    return [
        path
        for path in work_dir.rglob("*.md")
        if path.is_file() and not is_template(path) and path.name != "README.md"
    ]


def discover_policy_files() -> list[Path]:
    return sorted((REPO / "org" / "4-quality" / "policies").glob("*.md"))


def signal_candidates(root: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for directory in (root / "work" / "signals", root / "work" / "signals" / "archive"):
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            if path.name == "README.md" or is_template(path):
                continue
            index[path.name] = path
    return index


def find_signal_path(root: Path, reference: str) -> Path | None:
    raw = strip_anchor(reference)
    if should_skip_target(raw):
        return None

    if raw.startswith("work/signals/"):
        candidate = (root / raw).resolve()
        if candidate.exists():
            return candidate
        archive_candidate = (root / "work" / "signals" / "archive" / Path(raw).name).resolve()
        if archive_candidate.exists():
            return archive_candidate
        return candidate

    if raw.endswith(".md"):
        indexed = signal_candidates(root)
        if raw in indexed:
            return indexed[raw]
        archive_candidate = (root / "work" / "signals" / "archive" / raw).resolve()
        if archive_candidate.exists():
            return archive_candidate
        return (root / "work" / "signals" / raw).resolve()

    return None


def parse_exception_status(text: str) -> str | None:
    match = re.search(r"\*\*Status:\*\*\s*([A-Za-z-]+)", text)
    return match.group(1).strip().lower() if match else None


def parse_exception_expiry(text: str) -> date | None:
    patterns = [
        r"\*\*Expires:\*\*\s*(\d{4}-\d{2}-\d{2})",
        r"Expiry date[:\s|]*([0-9]{4}-[0-9]{2}-[0-9]{2})",
        r"\*\*Duration:\*\*.*?(\d{4}-\d{2}-\d{2})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        try:
            return date.fromisoformat(match.group(1))
        except ValueError:
            return None
    return None


def find_exception_by_id(root: Path, exception_id: str) -> Path | None:
    decisions_dir = root / "work" / "decisions"
    if not decisions_dir.exists():
        return None
    matches = sorted(decisions_dir.glob(f"{exception_id}-*.md"))
    return matches[0] if matches else None


def validate_work_refs(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in discover_work_files(root):
        for ref in extract_targets(path, include_bare=False):
            resolved = resolve_target(path, ref.target, root)
            if resolved is None:
                continue
            if not resolved.exists():
                errors.append(
                    f"{rel(path, root)}:{ref.line_no}: reference '{ref.target}' "
                    f"does not exist"
                )
                continue
            warning = filename_case_warning(ref.target, resolved)
            if warning:
                warnings.append(f"{rel(path, root)}:{ref.line_no}: {warning}")

    return errors, warnings


def validate_signal_supersedes(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    signals_dir = root / "work" / "signals"
    if not signals_dir.exists():
        return errors, warnings

    pattern = re.compile(r"\*\*Supersedes:\*\*\s*(.+)", re.IGNORECASE)
    alt_pattern = re.compile(r"\*\*Superseded signal:\*\*\s*(.+)", re.IGNORECASE)

    for path in sorted(signals_dir.glob("*.md")):
        if path.name == "README.md" or is_template(path):
            continue

        for line_no, line in iter_non_code_lines(path):
            match = pattern.search(line) or alt_pattern.search(line)
            if not match:
                continue
            target = match.group(1).strip()
            if should_skip_target(target):
                continue
            target_path = find_signal_path(root, target)
            if target_path is None or not target_path.exists():
                errors.append(
                    f"{rel(path, root)}:{line_no}: supersession target '{target}' "
                    f"does not resolve to an active or archived signal"
                )
                continue
            warning = filename_case_warning(target, target_path)
            if warning:
                warnings.append(f"{rel(path, root)}:{line_no}: {warning}")

    return errors, warnings


def validate_governance_exception_refs(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    files = discover_work_files(root)
    if root == REPO:
        files.extend(discover_policy_files())

    for path in files:
        for line_no, line in iter_non_code_lines(path):
            linked_paths = []
            for pattern in (MARKDOWN_LINK_RE, BACKTICK_PATH_RE, REPO_PATH_RE):
                for match in pattern.findall(line):
                    if "EXC-" in match:
                        linked_paths.append(match.strip())

            for target in linked_paths:
                resolved = resolve_target(path, target, root)
                if resolved is None:
                    continue
                if not resolved.exists():
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception reference "
                        f"'{target}' does not exist"
                    )
                    continue
                warning = filename_case_warning(target, resolved)
                if warning:
                    warnings.append(f"{rel(path, root)}:{line_no}: {warning}")
                exception_text = resolved.read_text(encoding="utf-8")
                status = parse_exception_status(exception_text)
                expiry = parse_exception_expiry(exception_text)
                if status in {"expired", "revoked"}:
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception '{target}' "
                        f"is not active (status: {status})"
                    )
                elif expiry and expiry < TODAY:
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception '{target}' "
                        f"expired on {expiry.isoformat()}"
                    )

            for match in EXCEPTION_ID_RE.findall(line):
                exception_id = match.strip()
                exception_path = find_exception_by_id(root, exception_id)
                if exception_path is None:
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception ID "
                        f"'{exception_id}' does not match any exception file"
                    )
                    continue
                exception_text = exception_path.read_text(encoding="utf-8")
                status = parse_exception_status(exception_text)
                expiry = parse_exception_expiry(exception_text)
                if status in {"expired", "revoked"}:
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception ID "
                        f"'{exception_id}' is not active (status: {status})"
                    )
                elif expiry and expiry < TODAY:
                    errors.append(
                        f"{rel(path, root)}:{line_no}: governance exception ID "
                        f"'{exception_id}' expired on {expiry.isoformat()}"
                    )

    return errors, warnings


def validate_policy_cross_refs() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in discover_policy_files():
        for ref in extract_targets(path, include_bare=True):
            resolved = resolve_target(path, ref.target, REPO)
            if resolved is None:
                continue
            if not resolved.exists():
                errors.append(
                    f"{rel(path, REPO)}:{ref.line_no}: policy reference '{ref.target}' "
                    f"does not exist"
                )
                continue
            warning = filename_case_warning(ref.target, resolved)
            if warning:
                warnings.append(f"{rel(path, REPO)}:{ref.line_no}: {warning}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        help="Validate against an alternate root directory (e.g., examples/e2e-loop)",
    )
    args = parser.parse_args()

    root = (args.root.resolve() if args.root else REPO)
    errors: list[str] = []
    warnings: list[str] = []

    work_errors, work_warnings = validate_work_refs(root)
    errors.extend(work_errors)
    warnings.extend(work_warnings)

    supersedes_errors, supersedes_warnings = validate_signal_supersedes(root)
    errors.extend(supersedes_errors)
    warnings.extend(supersedes_warnings)

    exception_errors, exception_warnings = validate_governance_exception_refs(root)
    errors.extend(exception_errors)
    warnings.extend(exception_warnings)

    if root == REPO:
        policy_errors, policy_warnings = validate_policy_cross_refs()
        errors.extend(policy_errors)
        warnings.extend(policy_warnings)

    if errors:
        print("Cross-reference integrity failures found:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")
        print(f"\nTotal failures: {len(errors)}")
        return 1

    if warnings:
        print("Cross-reference integrity warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if root == REPO:
        print("Cross-reference integrity validated: work artifacts and policies OK")
    else:
        print(f"Cross-reference integrity validated under {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
