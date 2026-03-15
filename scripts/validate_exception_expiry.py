#!/usr/bin/env python3
"""CI check: early-warning for governance exceptions approaching expiry.

Exit codes:
  0 — no expired exceptions (warnings are advisory)
  1 — expired exceptions found without renewal or closure

Self-check mode (--self-check):
  Runs against synthetic fixtures and reports PASS/FAIL.

What this script does:
  1. Scans EXC-*.md files in work/decisions/ (and archive/)
  2. Extracts Status, Duration, and Expiry date fields
  3. Warns (non-blocking) when exceptions expire within --warn-days (default 30)
  4. Errors (blocking) when exceptions are past expiry and status is not
     'expired', 'revoked', or 'closed'
  5. Prints a summary of all active exceptions with remaining time
"""

from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Date extraction patterns
# ---------------------------------------------------------------------------

# ISO date anywhere in text: 2026-03-15
DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

# Status field: **Status:** approved | expired | revoked
STATUS_PATTERN = re.compile(
    r"\*\*Status:\*\*\s*(proposed|approved|expired|revoked|closed)",
    re.IGNORECASE,
)

# Duration field: **Duration:** ... 2026-06-15 ...
DURATION_PATTERN = re.compile(r"\*\*Duration:\*\*\s*(.+)", re.IGNORECASE)


class ExceptionInfo(NamedTuple):
    file: str
    exception_id: str
    status: str
    expiry_date: date | None
    owner: str


def parse_date(text: str) -> date | None:
    """Extract the last ISO date from text (the expiry is usually the end date)."""
    dates = DATE_PATTERN.findall(text)
    for d in reversed(dates):
        try:
            return date.fromisoformat(d)
        except ValueError:
            continue
    return None


def parse_exception_file(path: Path, repo_root: Path) -> ExceptionInfo | None:
    """Parse an EXC-*.md file and extract key fields."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    rel = str(path.relative_to(repo_root))

    # Extract exception ID
    exc_id_match = re.search(r"\*\*Exception ID:\*\*\s*(EXC-[\w-]+)", text)
    exc_id = exc_id_match.group(1) if exc_id_match else path.stem

    # Extract status
    status_match = STATUS_PATTERN.search(text)
    status = status_match.group(1).lower() if status_match else "unknown"

    # Extract owner
    owner_match = re.search(r"\*\*Owner:\*\*\s*@?(\S+)", text)
    owner = owner_match.group(1) if owner_match else "unknown"

    # Extract expiry date — check Duration field first, then Expiry section
    expiry_date = None

    # Try Duration field
    duration_match = DURATION_PATTERN.search(text)
    if duration_match:
        expiry_date = parse_date(duration_match.group(1))

    # Try "Expiry / rollback" or "Expiry date" section
    if expiry_date is None:
        expiry_section = re.search(
            r"###?\s*Expiry\s*/?\s*rollback.*?\n(.*?)(?=\n###?\s|\n---|\Z)",
            text,
            re.IGNORECASE | re.DOTALL,
        )
        if expiry_section:
            expiry_date = parse_date(expiry_section.group(1))

    # Fallback: scan full text for "expiry" or "expires" near a date
    if expiry_date is None:
        for line in text.splitlines():
            if re.search(r"expir", line, re.IGNORECASE):
                expiry_date = parse_date(line)
                if expiry_date:
                    break

    return ExceptionInfo(
        file=rel,
        exception_id=exc_id,
        status=status,
        expiry_date=expiry_date,
        owner=owner,
    )


def collect_exceptions(repo_root: Path) -> list[ExceptionInfo]:
    """Find and parse all EXC-*.md files."""
    results: list[ExceptionInfo] = []
    decisions_dir = repo_root / "work" / "decisions"

    if not decisions_dir.is_dir():
        return results

    # Scan both active and archive directories
    for exc_file in sorted(decisions_dir.rglob("EXC-*.md")):
        if exc_file.name.startswith("_TEMPLATE"):
            continue
        info = parse_exception_file(exc_file, repo_root)
        if info:
            results.append(info)

    return results


def run_check(repo_root: Path, warn_days: int = 30, today: date | None = None) -> int:
    """Main check. Returns 0 on success, 1 on blocking violations."""
    if today is None:
        today = date.today()

    exceptions = collect_exceptions(repo_root)

    if not exceptions:
        print(f"✓ No governance exceptions found — nothing to check.")
        return 0

    # Classify
    terminal_statuses = {"expired", "revoked", "closed"}
    active = [e for e in exceptions if e.status not in terminal_statuses]
    closed = [e for e in exceptions if e.status in terminal_statuses]

    warnings: list[tuple[ExceptionInfo, int]] = []  # (info, days_remaining)
    errors: list[tuple[ExceptionInfo, int]] = []    # (info, days_overdue)
    no_expiry: list[ExceptionInfo] = []
    ok: list[tuple[ExceptionInfo, int]] = []        # (info, days_remaining)

    for exc in active:
        if exc.expiry_date is None:
            no_expiry.append(exc)
            continue

        days_remaining = (exc.expiry_date - today).days

        if days_remaining < 0:
            errors.append((exc, abs(days_remaining)))
        elif days_remaining <= warn_days:
            warnings.append((exc, days_remaining))
        else:
            ok.append((exc, days_remaining))

    # --- Summary ---
    print(f"Governance Exception Expiry Report ({today.isoformat()})")
    print(f"{'=' * 55}")
    print(f"  Active: {len(active)}  |  Closed/Expired/Revoked: {len(closed)}")
    print()

    has_errors = False

    if errors:
        has_errors = True
        print(f"✗ EXPIRED ({len(errors)}) — status is not expired/revoked/closed:")
        for exc, days in errors:
            print(f"  {exc.exception_id}  expired {days} day(s) ago"
                  f"  (expiry: {exc.expiry_date})  owner: {exc.owner}")
            print(f"    → {exc.file}")
        print()

    if warnings:
        print(f"⚠ EXPIRING SOON ({len(warnings)}) — within {warn_days} days:")
        for exc, days in warnings:
            print(f"  {exc.exception_id}  {days} day(s) remaining"
                  f"  (expiry: {exc.expiry_date})  owner: {exc.owner}")
            print(f"    → {exc.file}")
        print()

    if no_expiry:
        print(f"⚠ NO EXPIRY DATE ({len(no_expiry)}) — exceptions must be time-boxed:")
        for exc in no_expiry:
            print(f"  {exc.exception_id}  status: {exc.status}  owner: {exc.owner}")
            print(f"    → {exc.file}")
        print()

    if ok:
        print(f"✓ OK ({len(ok)}):")
        for exc, days in ok:
            print(f"  {exc.exception_id}  {days} day(s) remaining"
                  f"  (expiry: {exc.expiry_date})")
        print()

    if not errors and not warnings and not no_expiry:
        print("✓ All active exceptions have valid expiry dates and are not near expiry.")

    if has_errors:
        print("How to fix:")
        print("  1. Update the exception status to 'expired' or 'revoked', or")
        print("  2. Renew the exception with a new expiry date and approval")
        return 1

    return 0


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

    # --- parse_date ---
    assert_eq("parse date simple", parse_date("expires 2026-06-15"), date(2026, 6, 15))
    assert_eq("parse date multiple", parse_date("from 2026-01-01 to 2026-06-30"),
              date(2026, 6, 30))  # last date
    assert_eq("parse date none", parse_date("no date here"), None)

    # --- parse_exception_file ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        decisions = root / "work" / "decisions"
        decisions.mkdir(parents=True)

        # Well-formed exception
        (decisions / "EXC-2026-001-test.md").write_text(
            "# Governance Exception: Test\n"
            "> **Status:** approved\n"
            "## Summary\n"
            "- **Exception ID:** EXC-2026-001\n"
            "- **Owner:** @alice\n"
            "- **Duration:** 2026-01-01 to 2026-06-15\n"
            "## Details\n"
            "### Expiry / rollback\n"
            "- Expiry date: 2026-06-15\n"
        )
        info = parse_exception_file(decisions / "EXC-2026-001-test.md", root)
        assert_eq("parses ID", info and info.exception_id, "EXC-2026-001")
        assert_eq("parses status", info and info.status, "approved")
        assert_eq("parses owner", info and info.owner, "alice")
        assert_eq("parses expiry", info and info.expiry_date, date(2026, 6, 15))

        # Exception with status=expired (should not trigger error)
        (decisions / "EXC-2026-002-closed.md").write_text(
            "# Governance Exception: Closed\n"
            "> **Status:** expired\n"
            "## Summary\n"
            "- **Exception ID:** EXC-2026-002\n"
            "- **Owner:** @bob\n"
            "- **Duration:** 2025-01-01 to 2025-03-01\n"
        )

        # Exception that is past expiry but status=approved (ERROR)
        (decisions / "EXC-2026-003-overdue.md").write_text(
            "# Governance Exception: Overdue\n"
            "> **Status:** approved\n"
            "## Summary\n"
            "- **Exception ID:** EXC-2026-003\n"
            "- **Owner:** @charlie\n"
            "- **Duration:** 2025-01-01 to 2025-12-31\n"
        )

        # Exception expiring soon (WARNING)
        soon = (date(2026, 3, 15) + timedelta(days=10)).isoformat()
        (decisions / "EXC-2026-004-soon.md").write_text(
            f"# Governance Exception: Soon\n"
            f"> **Status:** approved\n"
            f"## Summary\n"
            f"- **Exception ID:** EXC-2026-004\n"
            f"- **Owner:** @dave\n"
            f"- **Duration:** 2026-01-01 to {soon}\n"
        )

        # Template should be skipped
        (decisions / "_TEMPLATE-EXC-test.md").write_text(
            "# Governance Exception: Template\n"
            "> **Status:** approved\n"
            "- **Duration:** 2020-01-01 to 2020-01-02\n"
        )

        # Collect and check
        all_exc = collect_exceptions(root)
        assert_eq("finds 4 exceptions (skips template)", len(all_exc), 4)

        # Run check with fixed "today"
        fixed_today = date(2026, 3, 15)
        result = run_check(root, warn_days=30, today=fixed_today)
        assert_eq("returns 1 (overdue exception)", result, 1)

        # Remove the overdue one, should pass
        (decisions / "EXC-2026-003-overdue.md").unlink()
        result2 = run_check(root, warn_days=30, today=fixed_today)
        assert_eq("returns 0 (no overdue)", result2, 0)

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
        description="Check governance exceptions for expiry and early warnings."
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
    parser.add_argument(
        "--warn-days",
        type=int,
        default=30,
        help="Warn when exceptions expire within N days (default: 30).",
    )
    args = parser.parse_args(argv)

    if args.self_check:
        return run_self_check()

    repo_root = Path(args.root).resolve()
    return run_check(repo_root, warn_days=args.warn_days)


if __name__ == "__main__":
    sys.exit(main())
