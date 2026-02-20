#!/usr/bin/env python3
"""CI gate: enforce locking for protected paths.

Checks that every file changed in a PR that matches a protected-path glob
has a corresponding active (non-expired) lock in work/locks/.

Exit codes:
  0 — no violations
  1 — violations found (CI should block)

Environment variables:
  BASE  — base commit SHA (required for diff)
  HEAD  — head commit SHA (required for diff)
"""

import fnmatch
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(".")
LOCKS_DIR = REPO / "work" / "locks"
CONFIG_PATH = REPO / "locks.yaml"
EXEMPT_MARKER = "ci:lock-exempt"


def load_protected_paths() -> list[str]:
    """Parse locks.yaml without external deps (no PyYAML required)."""
    text = CONFIG_PATH.read_text(encoding="utf-8")
    patterns: list[str] = []
    in_list = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("protected_paths:"):
            in_list = True
            continue
        if in_list:
            if stripped.startswith("- "):
                value = stripped[2:].strip().strip('"').strip("'")
                if value and not value.startswith("#"):
                    patterns.append(value)
            elif stripped == "" or stripped.startswith("#"):
                continue
            else:
                break  # next top-level key
    return patterns


def get_changed_files(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", base, head],
        capture_output=True, text=True,
    )
    return [f.strip() for f in result.stdout.splitlines() if f.strip()]


def matches_any(filepath: str, patterns: list[str]) -> bool:
    """Check if filepath matches any glob pattern."""
    for pat in patterns:
        if fnmatch.fnmatch(filepath, pat):
            return True
        # For patterns without directory separators, also match basename
        if "/" not in pat and fnmatch.fnmatch(Path(filepath).name, pat):
            return True
    return False


def parse_lock_target(lock_path: Path) -> str | None:
    """Extract Target path from a lock file."""
    text = lock_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*Target:\*\*\s*`([^`]+)`", text)
    return m.group(1) if m else None


def parse_lock_expires(lock_path: Path) -> datetime | None:
    """Extract Expires timestamp from a lock file."""
    text = lock_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*Expires:\*\*\s*(\S+)", text)
    if not m:
        return None
    raw = m.group(1)
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


def get_active_locks() -> dict[str, Path]:
    """Return {target_path: lock_file} for all non-expired locks."""
    locks: dict[str, Path] = {}
    if not LOCKS_DIR.is_dir():
        return locks

    now = datetime.now(timezone.utc)
    for lf in LOCKS_DIR.glob("*.md"):
        if lf.name.startswith("_TEMPLATE"):
            continue
        if lf.name == "README.md":
            continue
        target = parse_lock_target(lf)
        if not target:
            continue
        expires = parse_lock_expires(lf)
        if expires and expires < now:
            continue  # expired
        locks[target] = lf
    return locks


def file_covered_by_lock(filepath: str, locks: dict[str, Path]) -> bool:
    """Check if a file is covered by any active lock target (exact or glob)."""
    for target in locks:
        if fnmatch.fnmatch(filepath, target):
            return True
        if filepath == target:
            return True
        # Lock target may be a directory — check prefix
        if filepath.startswith(target.rstrip("/") + "/"):
            return True
    return False


def commit_has_exempt(base: str, head: str) -> bool:
    """Check if any commit in the range has the exempt marker."""
    result = subprocess.run(
        ["git", "log", "--format=%B", f"{base}..{head}"],
        capture_output=True, text=True,
    )
    return EXEMPT_MARKER in result.stdout


def main() -> int:
    base = os.environ.get("BASE", "").strip()
    head = os.environ.get("HEAD", "").strip()

    if not base:
        print("No BASE SHA — skipping lock enforcement (initial push).")
        return 0

    if not CONFIG_PATH.exists():
        print("locks.yaml not found — skipping lock enforcement.")
        return 0

    patterns = load_protected_paths()
    if not patterns:
        print("No protected paths defined — nothing to enforce.")
        return 0

    changed = get_changed_files(base, head)
    protected_changed = [f for f in changed if matches_any(f, patterns)]

    if not protected_changed:
        print(f"No protected paths touched among {len(changed)} changed files. ✓")
        return 0

    # Check for blanket exemption
    if commit_has_exempt(base, head):
        print(f"Found '{EXEMPT_MARKER}' in commit messages — skipping enforcement for {len(protected_changed)} file(s).")
        return 0

    # Check locks
    locks = get_active_locks()
    violations: list[str] = []

    for f in protected_changed:
        if not file_covered_by_lock(f, locks):
            violations.append(f)

    if not violations:
        print(f"All {len(protected_changed)} protected file(s) have active locks. ✓")
        return 0

    print("╔══════════════════════════════════════════════════════╗")
    print("║  LOCK ENFORCEMENT FAILED                            ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()
    print(f"  {len(violations)} protected file(s) changed without an active lock:\n")
    for v in violations:
        print(f"    ✗ {v}")
    print()
    print("  To fix, either:")
    print("    1. Create a lock file in work/locks/ covering the target path")
    print("       (see work/locks/README.md and work/locks/_TEMPLATE-lock.md)")
    print("    2. Add 'ci:lock-exempt' to a commit message for an exception")
    print()
    print(f"  Protected path patterns (from locks.yaml): {patterns}")
    print(f"  Active locks found: {len(locks)}")
    for target, lf in locks.items():
        print(f"    • {target} → {lf}")
    print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
