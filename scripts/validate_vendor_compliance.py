#!/usr/bin/env python3
"""CI check: verify configured integrations have current compliance attestations.

Exit codes:
  0 — all vendors OK (or no vendors configured)
  1 — missing or expired attestations found

Self-check mode (--self-check):
  Runs against synthetic fixtures and reports PASS/FAIL.

What this script does:
  1. Parses CONFIG.yaml integrations for vendor entries
  2. Scans work/assets/ for vendor security assessment files
  3. Validates attestation currency (Assessment Date < 1 year, Next Reassessment not past)
  4. Checks Tier 1-2 vendors have required certifications (SOC 2 or ISO 27001)
  5. Reports missing, expired, or incomplete attestations
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, NamedTuple

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
TIER_PATTERN = re.compile(r"\*\*Criticality Tier:\*\*\s*(\d)", re.IGNORECASE)
RATING_PATTERN = re.compile(
    r"\*\*Overall Rating:\*\*\s*(PASS|CONDITIONAL|FAIL)", re.IGNORECASE
)
ASSESSMENT_DATE_PATTERN = re.compile(
    r"\*\*Assessment Date:\*\*\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE
)
REASSESSMENT_DATE_PATTERN = re.compile(
    r"\*\*Next Reassessment:\*\*\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE
)
VENDOR_NAME_PATTERN = re.compile(
    r"\*\*Vendor:\*\*\s*(.+)", re.IGNORECASE
)

# Certification row pattern in attestation table
# Matches: | SOC 2 Type II | current | yes | 2026-12-31 | |
CERT_ROW_PATTERN = re.compile(
    r"^\s*\|\s*(SOC 2 Type II|SOC 2 Type I|ISO 27001)"
    r"\s*\|\s*(current|expired|not held)"
    r"\s*\|",
    re.IGNORECASE,
)


class VendorInfo(NamedTuple):
    name: str
    source: str  # "config" or "assessment"


class AssessmentInfo(NamedTuple):
    file: str
    vendor_name: str
    tier: int | None
    rating: str | None
    assessment_date: date | None
    reassessment_date: date | None
    has_soc2: bool  # current SOC 2 Type II
    has_iso27001: bool  # current ISO 27001


class Finding(NamedTuple):
    severity: str  # "error" or "warning"
    vendor: str
    message: str


def extract_vendors_from_config(config: dict[str, Any]) -> list[VendorInfo]:
    """Extract vendor names from CONFIG.yaml integrations section."""
    vendors: list[VendorInfo] = []
    integrations = config.get("integrations", {})
    if not isinstance(integrations, dict):
        return vendors

    for category, entries in integrations.items():
        if isinstance(entries, list):
            for entry in entries:
                if isinstance(entry, dict):
                    name = entry.get("name") or entry.get("vendor", "")
                    if name and not name.startswith("{{"):
                        vendors.append(VendorInfo(name=name.strip(), source="config"))
        elif isinstance(entries, dict):
            for sub_key, sub_entries in entries.items():
                if isinstance(sub_entries, list):
                    for entry in sub_entries:
                        if isinstance(entry, dict):
                            name = entry.get("name") or entry.get("vendor", "")
                            if name and not name.startswith("{{"):
                                vendors.append(VendorInfo(name=name.strip(), source="config"))

    return vendors


def parse_assessment_file(path: Path, repo_root: Path) -> AssessmentInfo | None:
    """Parse a vendor security assessment file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    rel = str(path.relative_to(repo_root))

    # Vendor name
    vendor_match = VENDOR_NAME_PATTERN.search(text)
    vendor_name = vendor_match.group(1).strip() if vendor_match else path.stem

    # Tier
    tier_match = TIER_PATTERN.search(text)
    tier = int(tier_match.group(1)) if tier_match else None

    # Rating
    rating_match = RATING_PATTERN.search(text)
    rating = rating_match.group(1).upper() if rating_match else None

    # Assessment date
    assess_match = ASSESSMENT_DATE_PATTERN.search(text)
    assessment_date = None
    if assess_match:
        try:
            assessment_date = date.fromisoformat(assess_match.group(1))
        except ValueError:
            pass

    # Reassessment date
    reassess_match = REASSESSMENT_DATE_PATTERN.search(text)
    reassessment_date = None
    if reassess_match:
        try:
            reassessment_date = date.fromisoformat(reassess_match.group(1))
        except ValueError:
            pass

    # Check certifications
    has_soc2 = False
    has_iso27001 = False
    for line in text.splitlines():
        cert_match = CERT_ROW_PATTERN.match(line)
        if cert_match:
            cert_name = cert_match.group(1).strip().lower()
            cert_status = cert_match.group(2).strip().lower()
            if cert_status == "current":
                if "soc 2 type ii" in cert_name:
                    has_soc2 = True
                elif "iso 27001" in cert_name:
                    has_iso27001 = True

    return AssessmentInfo(
        file=rel,
        vendor_name=vendor_name,
        tier=tier,
        rating=rating,
        assessment_date=assessment_date,
        reassessment_date=reassessment_date,
        has_soc2=has_soc2,
        has_iso27001=has_iso27001,
    )


def collect_assessments(repo_root: Path) -> list[AssessmentInfo]:
    """Find and parse all vendor assessment files."""
    results: list[AssessmentInfo] = []
    assets_dir = repo_root / "work" / "assets"
    if not assets_dir.is_dir():
        return results

    # Look for vendor assessment files (any naming convention)
    for f in sorted(assets_dir.rglob("*.md")):
        if f.name.startswith("_TEMPLATE"):
            continue
        # Check if it's a vendor assessment by content
        try:
            header = f.read_text(encoding="utf-8", errors="replace")[:500]
        except OSError:
            continue
        if "vendor" in header.lower() and ("assessment" in header.lower() or "attestation" in header.lower()):
            info = parse_assessment_file(f, repo_root)
            if info:
                results.append(info)

    return results


def normalize_name(name: str) -> str:
    """Normalize vendor name for matching."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def load_config(repo_root: Path) -> dict[str, Any]:
    """Load CONFIG.yaml."""
    import yaml
    config_path = repo_root / "CONFIG.yaml"
    if not config_path.exists():
        return {}
    try:
        with open(config_path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def run_check(repo_root: Path, max_age_days: int = 365, today: date | None = None) -> int:
    """Main check. Returns 0 on success, 1 on blocking violations."""
    if today is None:
        today = date.today()

    config = load_config(repo_root)
    config_vendors = extract_vendors_from_config(config)
    assessments = collect_assessments(repo_root)

    if not config_vendors and not assessments:
        print("✓ No vendors configured and no assessments found — nothing to check.")
        return 0

    # Build lookup by normalized name
    assessment_map: dict[str, AssessmentInfo] = {}
    for a in assessments:
        assessment_map[normalize_name(a.vendor_name)] = a

    findings: list[Finding] = []

    # Check each configured vendor has an assessment
    for vendor in config_vendors:
        norm = normalize_name(vendor.name)
        assessment = assessment_map.get(norm)

        if assessment is None:
            findings.append(Finding(
                severity="warning",
                vendor=vendor.name,
                message="no vendor security assessment found in work/assets/",
            ))
            continue

        # Check assessment age
        if assessment.assessment_date:
            age_days = (today - assessment.assessment_date).days
            if age_days > max_age_days:
                findings.append(Finding(
                    severity="error",
                    vendor=vendor.name,
                    message=f"assessment is {age_days} days old (max {max_age_days}), "
                            f"assessed: {assessment.assessment_date}",
                ))
        else:
            findings.append(Finding(
                severity="warning",
                vendor=vendor.name,
                message="assessment has no Assessment Date",
            ))

        # Check reassessment not overdue
        if assessment.reassessment_date and assessment.reassessment_date < today:
            overdue = (today - assessment.reassessment_date).days
            findings.append(Finding(
                severity="error",
                vendor=vendor.name,
                message=f"reassessment overdue by {overdue} days "
                        f"(due: {assessment.reassessment_date})",
            ))

        # Check Tier 1-2 have SOC 2 or ISO 27001
        if assessment.tier is not None and assessment.tier <= 2:
            if not assessment.has_soc2 and not assessment.has_iso27001:
                findings.append(Finding(
                    severity="error",
                    vendor=vendor.name,
                    message=f"Tier {assessment.tier} vendor requires current SOC 2 Type II "
                            f"or ISO 27001 (per vendor-risk-management.md §1)",
                ))

        # Check rating
        if assessment.rating == "FAIL":
            findings.append(Finding(
                severity="error",
                vendor=vendor.name,
                message="assessment overall rating is FAIL",
            ))

    # Also check assessments not tied to config vendors (standalone)
    for assessment in assessments:
        norm = normalize_name(assessment.vendor_name)
        if norm not in {normalize_name(v.name) for v in config_vendors}:
            # Standalone assessment — still check dates
            if assessment.reassessment_date and assessment.reassessment_date < today:
                overdue = (today - assessment.reassessment_date).days
                findings.append(Finding(
                    severity="warning",
                    vendor=assessment.vendor_name,
                    message=f"standalone assessment overdue for reassessment by {overdue} days",
                ))

    # --- Report ---
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    print(f"Vendor Compliance Report ({today.isoformat()})")
    print(f"{'=' * 50}")
    print(f"  Configured vendors: {len(config_vendors)}")
    print(f"  Assessment files: {len(assessments)}")
    print()

    if errors:
        print(f"✗ ERRORS ({len(errors)}):")
        for f in errors:
            print(f"  {f.vendor}: {f.message}")
        print()

    if warnings:
        print(f"⚠ WARNINGS ({len(warnings)}):")
        for f in warnings:
            print(f"  {f.vendor}: {f.message}")
        print()

    if not errors and not warnings:
        print("✓ All configured vendors have current, valid assessments.")

    if errors:
        print("How to fix:")
        print("  1. Create/update vendor assessment in work/assets/ using")
        print("     work/assets/_TEMPLATE-vendor-security-assessment.md")
        print("  2. Ensure Assessment Date and Next Reassessment are current")
        print("  3. For Tier 1-2 vendors: obtain SOC 2 Type II or ISO 27001 attestation")
        return 1

    return 0


# ---------------------------------------------------------------------------
# Self-check mode
# ---------------------------------------------------------------------------
def run_self_check() -> int:
    """Synthetic fixture tests."""
    import tempfile
    import yaml

    failures: list[str] = []

    def assert_eq(label: str, got: object, expected: object) -> None:
        if got != expected:
            failures.append(f"FAIL [{label}]: expected {expected!r}, got {got!r}")
        else:
            print(f"  PASS [{label}]")

    print("Running self-check…\n")

    # --- extract_vendors_from_config ---
    config = {
        "integrations": {
            "observability": [
                {"id": "primary", "name": "Datadog", "vendor": "Datadog Inc"},
            ],
            "enterprise_toolchain": {
                "ci_cd": [{"id": "pipeline", "name": "GitHub Actions"}],
                "itsm": [],
            },
            "business_systems": [],
            "communication": [],
        }
    }
    vendors = extract_vendors_from_config(config)
    assert_eq("extracts 2 vendors", len(vendors), 2)
    assert_eq("first vendor name", vendors[0].name, "Datadog")
    assert_eq("second vendor name", vendors[1].name, "GitHub Actions")

    # Skip placeholder vendors
    config2 = {
        "integrations": {
            "observability": [{"name": "{{VENDOR_NAME}}"}],
        }
    }
    vendors2 = extract_vendors_from_config(config2)
    assert_eq("skips placeholder vendors", len(vendors2), 0)

    # --- End-to-end ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        assets = root / "work" / "assets"
        assets.mkdir(parents=True)

        # Write CONFIG.yaml
        config_data = {
            "integrations": {
                "observability": [
                    {"id": "obs", "name": "Acme Monitor", "vendor": "Acme"},
                ],
                "enterprise_toolchain": {
                    "ci_cd": [{"id": "ci", "name": "BuildBot"}],
                },
            }
        }
        (root / "CONFIG.yaml").write_text(yaml.dump(config_data))

        # Valid assessment for Acme Monitor
        (assets / "vendor-acme-monitor.md").write_text(
            "# Vendor Security Assessment: Acme Monitor\n"
            "> **Vendor:** Acme Monitor\n"
            "> **Criticality Tier:** 1\n"
            "> **Assessment Date:** 2026-01-15\n"
            "> **Next Reassessment:** 2026-07-15\n"
            "> **Overall Rating:** PASS\n"
            "## 2. Attestations & Certifications\n"
            "| Certification | Status | Scope Covers Our Use? | Expiry Date | Notes |\n"
            "|--|--|--|--|--|\n"
            "| SOC 2 Type II | current | yes | 2026-12-31 | |\n"
            "| ISO 27001 | current | yes | 2027-06-30 | |\n"
        )

        fixed_today = date(2026, 3, 15)
        result = run_check(root, today=fixed_today)
        assert_eq("valid assessment: warning for missing BuildBot only", result, 0)

        # Make Acme assessment expired
        (assets / "vendor-acme-monitor.md").write_text(
            "# Vendor Security Assessment: Acme Monitor\n"
            "> **Vendor:** Acme Monitor\n"
            "> **Criticality Tier:** 1\n"
            "> **Assessment Date:** 2024-01-01\n"
            "> **Next Reassessment:** 2025-01-01\n"
            "> **Overall Rating:** PASS\n"
            "## 2. Attestations & Certifications\n"
            "| Certification | Status | Scope Covers Our Use? | Expiry Date | Notes |\n"
            "|--|--|--|--|--|\n"
            "| SOC 2 Type II | current | yes | 2026-12-31 | |\n"
        )

        result2 = run_check(root, today=fixed_today)
        assert_eq("expired assessment: returns 1", result2, 1)

        # Tier 1 without certs
        (assets / "vendor-acme-monitor.md").write_text(
            "# Vendor Security Assessment: Acme Monitor\n"
            "> **Vendor:** Acme Monitor\n"
            "> **Criticality Tier:** 1\n"
            "> **Assessment Date:** 2026-02-01\n"
            "> **Next Reassessment:** 2026-08-01\n"
            "> **Overall Rating:** CONDITIONAL\n"
            "## 2. Attestations & Certifications\n"
            "| Certification | Status | Scope Covers Our Use? | Expiry Date | Notes |\n"
            "|--|--|--|--|--|\n"
            "| SOC 2 Type II | not held | no | | |\n"
            "| ISO 27001 | not held | no | | |\n"
        )

        result3 = run_check(root, today=fixed_today)
        assert_eq("tier 1 no certs: returns 1", result3, 1)

        # Template should be skipped
        (assets / "_TEMPLATE-vendor-security-assessment.md").write_text(
            "# Vendor Security Assessment: {{VENDOR_NAME}}\n"
            "> **Vendor:** {{VENDOR_NAME}}\n"
        )
        assessments = collect_assessments(root)
        template_found = any("_TEMPLATE" in a.file for a in assessments)
        assert_eq("template skipped", template_found, False)

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
        description="Validate vendor compliance attestations."
    )
    parser.add_argument(
        "--self-check",
        action="store_true",
        help="Run synthetic fixture tests.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root (default: current directory).",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=365,
        help="Maximum assessment age in days (default: 365).",
    )
    args = parser.parse_args(argv)

    if args.self_check:
        return run_self_check()

    repo_root = Path(args.root).resolve()
    return run_check(repo_root, max_age_days=args.max_age_days)


if __name__ == "__main__":
    sys.exit(main())
