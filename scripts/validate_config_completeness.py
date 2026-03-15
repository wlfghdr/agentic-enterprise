#!/usr/bin/env python3
"""CI check: ensure all {{VARIABLE}} tokens used in framework files are defined
and populated in CONFIG.yaml.

Exit codes:
  0 — all variables accounted for (or advisory-only warnings)
  1 — blocking violations found

Self-check mode (--self-check):
  Runs synthetic fixture tests and reports PASS/FAIL.

What this script does:
  1. Scans framework files for {{VARIABLE}} tokens
  2. Resolves each token to a CONFIG.yaml path via the canonical mapping
  3. Reports tokens that have no mapping (unknown variables)
  4. Reports mapped variables whose CONFIG.yaml value is empty/placeholder
  5. Validates value formats for known variable types (URL, domain, date, etc.)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Canonical mapping: {{VARIABLE}} → CONFIG.yaml dot-path
#
# Source of truth: docs/customization-guide.md § "Complete Placeholder Reference"
# ---------------------------------------------------------------------------
VARIABLE_TO_CONFIG: dict[str, str] = {
    # Company identity
    "COMPANY_NAME": "company.name",
    "COMPANY_SHORT": "company.short_name",
    # Ventures (indexed)
    "VENTURE_1_NAME": "ventures[0].name",
    "VENTURE_1_DESCRIPTION": "ventures[0].description",
    "VENTURE_2_NAME": "ventures[1].name",
    "VENTURE_2_DESCRIPTION": "ventures[1].description",
    "VENTURE_3_NAME": "ventures[2].name",
    "VENTURE_3_DESCRIPTION": "ventures[2].description",
    # Domain divisions (indexed)
    "DOMAIN_CAP_1_NAME": "divisions.engineering_domain[0].name",
    "DOMAIN_CAP_1_DESCRIPTION": "divisions.engineering_domain[0].description",
    "DOMAIN_CAP_2_NAME": "divisions.engineering_domain[1].name",
    "DOMAIN_CAP_2_DESCRIPTION": "divisions.engineering_domain[1].description",
    # Toolchain
    "GIT_HOST": "toolchain.git_host",
    "CI_CD": "toolchain.ci_cd",
    "OBSERVABILITY_TOOL": "toolchain.observability",
    "SERVICE_CATALOG": "toolchain.service_catalog",
    # Integrations
    "OBSERVABILITY_PLATFORM_NAME": "integrations.observability[0].name",
    "OTLP_ENDPOINT": "integrations.observability[0].otlp_endpoint",
    # Risk appetite
    "RISK_MAX_DOWNTIME_MINUTES": "risk_appetite.max_downtime_minutes",
    "RISK_COST_OVERRUN_THRESHOLD": "risk_appetite.cost_overrun_threshold_pct",
    "RISK_KILL_SWITCH_TARGET_SECONDS": "risk_appetite.kill_switch_target_seconds",
    "RISK_ESCALATION_RATE_THRESHOLD": "risk_appetite.escalation_rate_threshold_pct",
    "RISK_TOOL_FAILURE_THRESHOLD": "risk_appetite.tool_failure_threshold_pct",
    "RISK_CYCLE_TIME_VARIANCE": "risk_appetite.cycle_time_variance_pct",
    "RISK_HALLUCINATION_THRESHOLD": "risk_appetite.hallucination_threshold_pct",
    # Encryption / cryptography
    "CRYPTO_ROTATION_SYMMETRIC_DAYS": "encryption.rotation_symmetric_days",
    "CRYPTO_ROTATION_SIGNING_DAYS": "encryption.rotation_signing_days",
    "CRYPTO_ROTATION_ASYMMETRIC_DAYS": "encryption.rotation_asymmetric_days",
    "CRYPTO_ROTATION_API_KEY_DAYS": "encryption.rotation_api_key_days",
    "CRYPTO_CERT_LIFETIME_DAYS": "encryption.cert_lifetime_days",
    "CRYPTO_RSA2048_DEPRECATION_DATE": "encryption.rsa2048_deprecation_date",
    "CRYPTO_REVOCATION_TARGET_HOURS": "encryption.revocation_target_hours",
    "CERT_MANAGER": "encryption.cert_manager",
    # Ship process
    "CANARY_PERCENTAGE": "quality.canary_percentage",
    "CANARY_DURATION": "quality.canary_duration",
    "EARLY_ADOPTER_PERCENTAGE": "quality.early_adopter_percentage",
    "EARLY_ADOPTER_DURATION": "quality.early_adopter_duration",
    "GA_PERCENTAGE": "quality.ga_percentage",
    "GA_DURATION": "quality.ga_duration",
    "MAX_ERROR_RATE_INCREASE": "quality.max_error_rate_increase",
    "MAX_HEALTH_CHECK_FAILURE_RATE": "quality.max_health_check_failure_rate",
    # Discover process
    "CRM_SYSTEM": "toolchain.crm_system",
    "SUPPORT_SYSTEM": "toolchain.support_system",
    "ALERTING_SYSTEM": "toolchain.alerting_system",
    "FINANCE_SYSTEM": "toolchain.finance_system",
    # Quality
    "MIN_CODE_COVERAGE": "quality.code_coverage_minimum",
    "PRODUCT_NAME": "product_name",
    # Org size (from org/README.md)
    "STEERING_SIZE": "org_size.steering_layer",
    "STRATEGY_SIZE": "org_size.strategy_layer",
    "ORCHESTRATION_SIZE": "org_size.orchestration_layer",
    "EXECUTION_SIZE": "org_size.execution_layer",
    "QUALITY_SIZE": "org_size.quality_layer",
    # Policy variables
    "DESIGN_SYSTEM_NAME": "toolchain.design_system",
    "SECRETS_MANAGER": "toolchain.secrets_manager",
    "LOAD_TEST_MULTIPLIER": "quality.load_test_multiplier",
    "POST_DEPLOY_VALIDATION_WINDOW": "quality.post_deploy_validation_window",
    # Log retention policy
    "RETENTION_AUDIT_YEARS": "quality.retention_audit_years",
    "RETENTION_SECURITY_YEARS": "quality.retention_security_years",
    "RETENTION_ACCESS_YEARS": "quality.retention_access_years",
    "RETENTION_OPERATIONAL_DAYS": "quality.retention_operational_days",
    "RETENTION_DEBUG_DAYS": "quality.retention_debug_days",
    # Integration observability
    "OTLP_INGEST_ENDPOINT": "integrations.observability[0].otlp_endpoint",
    "OBSERVABILITY_DASHBOARD_URL": "integrations.observability[0].dashboard_url",
    "API_ENDPOINT": "integrations.observability[0].api_endpoint",
    "VENDOR": "integrations.observability[0].vendor",
}

# Format validators for known variable types
# Each entry: config_path_substring → (label, compiled regex)
FORMAT_VALIDATORS: list[tuple[str, str, re.Pattern[str]]] = [
    ("otlp_endpoint", "URL format", re.compile(r"^https?://\S+")),
    ("domain", "domain format", re.compile(r"^[a-zA-Z0-9]([a-zA-Z0-9-]*\.)+[a-zA-Z]{2,}$")),
    ("rsa2048_deprecation_date", "date format (YYYY-MM-DD)", re.compile(r"^\d{4}-\d{2}-\d{2}$")),
]

# Variable token pattern
VAR_PATTERN = re.compile(r"\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}")

# Files/directories to skip when scanning for variable usage
SKIP_DIRS = {".git", "node_modules", "archive", "examples"}
SKIP_FILES = {
    "CHANGELOG.md",
    "customization-guide.md",
    "CONTRIBUTING.md",
}
# Directory prefixes to skip — these contain fill-in-the-blank templates
# with their own {{VAR}} placeholders that are NOT CONFIG.yaml references
SKIP_DIR_PREFIXES = {
    "docs/compliance/guides",  # Legal/compliance document templates
}
# Files that *document* placeholder syntax rather than *using* it
DOCUMENTATION_FILES = {
    "docs/placeholder-check.md",
    "docs/security-scanning.md",
    "docs/file-guide.md",
    "docs/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
}


def resolve_config_path(data: dict[str, Any], dot_path: str) -> Any:
    """Resolve a dot-path like 'company.name' or 'ventures[0].name' against
    a parsed YAML dict. Returns None if path doesn't exist."""
    parts = re.split(r"\.", dot_path)
    current: Any = data
    for part in parts:
        # Handle array index: "ventures[0]"
        m = re.match(r"^(\w+)\[(\d+)\]$", part)
        if m:
            key, idx = m.group(1), int(m.group(2))
            if not isinstance(current, dict) or key not in current:
                return None
            lst = current[key]
            if not isinstance(lst, list) or idx >= len(lst):
                return None
            current = lst[idx]
        else:
            if not isinstance(current, dict) or part not in current:
                return None
            current = current[part]
    return current


def is_empty_value(value: Any) -> bool:
    """Return True if a CONFIG.yaml value is empty or still a placeholder."""
    if value is None:
        return True
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return True
        # Still contains a {{VAR}} placeholder
        if VAR_PATTERN.search(s):
            return True
        return False
    if isinstance(value, (int, float, bool)):
        return False
    return False


def validate_format(config_path: str, value: Any) -> str | None:
    """Return an error message if value doesn't match the expected format
    for its config path, or None if OK / not applicable."""
    if not isinstance(value, str) or not value.strip():
        return None
    for path_substr, label, regex in FORMAT_VALIDATORS:
        if path_substr in config_path:
            if not regex.match(value.strip()):
                return f"value {value!r} does not match expected {label}"
    return None


def scan_framework_files(repo_root: Path) -> dict[str, list[tuple[str, int]]]:
    """Scan framework files for {{VARIABLE}} tokens.
    Returns {variable_name: [(relative_path, line_no), ...]}."""
    found: dict[str, list[tuple[str, int]]] = {}

    for p in sorted(repo_root.rglob("*")):
        if p.is_dir():
            continue
        if p.suffix not in (".md", ".yaml", ".yml"):
            continue
        # Skip directories
        rel = p.relative_to(repo_root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        # Skip specific files
        if rel.name in SKIP_FILES:
            continue
        if str(rel) in DOCUMENTATION_FILES:
            continue
        # Skip directory prefixes (compliance templates, etc.)
        rel_str = str(rel)
        if any(rel_str.startswith(prefix) for prefix in SKIP_DIR_PREFIXES):
            continue
        # Skip template files
        if rel.name.startswith("_TEMPLATE"):
            continue
        if "_TEMPLATE" in rel.parts:
            continue

        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        for line_no, line in enumerate(text.splitlines(), start=1):
            for m in VAR_PATTERN.finditer(line):
                var_name = m.group(1)
                # Skip meta-references like {{VARIABLE}} in CONFIG.yaml comments
                if var_name == "VARIABLE":
                    continue
                found.setdefault(var_name, []).append((str(rel), line_no))

    return found


def load_config(repo_root: Path) -> dict[str, Any]:
    """Load CONFIG.yaml. Returns empty dict on failure."""
    import yaml

    config_path = repo_root / "CONFIG.yaml"
    if not config_path.exists():
        return {}
    try:
        with open(config_path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def run_check(repo_root: Path) -> int:
    """Main check. Returns 0 on success, 1 on violations."""
    config = load_config(repo_root)
    if not config:
        print("✗ Could not load CONFIG.yaml")
        return 1

    variables_in_use = scan_framework_files(repo_root)

    # Also add all variables from the canonical mapping that might not
    # appear in scanned files (they may be in template-excluded files)
    all_variables = set(variables_in_use.keys()) | set(VARIABLE_TO_CONFIG.keys())

    unmapped: list[str] = []
    empty: list[tuple[str, str]] = []
    format_errors: list[tuple[str, str, str]] = []
    ok_count = 0

    for var in sorted(all_variables):
        config_path = VARIABLE_TO_CONFIG.get(var)
        if config_path is None:
            # Only report unmapped if actually used in framework files
            if var in variables_in_use:
                unmapped.append(var)
            continue

        value = resolve_config_path(config, config_path)
        if is_empty_value(value):
            empty.append((var, config_path))
        else:
            # Format validation
            fmt_err = validate_format(config_path, value)
            if fmt_err:
                format_errors.append((var, config_path, fmt_err))
            else:
                ok_count += 1

    # --- Report ---
    has_errors = False

    if unmapped:
        print(f"\n⚠  Unmapped variables ({len(unmapped)}):")
        print("   These {{VARIABLE}} tokens appear in framework files but have")
        print("   no mapping in VARIABLE_TO_CONFIG. Add a mapping or remove usage.\n")
        for var in unmapped:
            locations = variables_in_use[var]
            print(f"   {{{{  {var}  }}}}")
            for path, line in locations[:3]:
                print(f"      used in {path}:{line}")
            if len(locations) > 3:
                print(f"      … and {len(locations) - 3} more location(s)")
        has_errors = True

    if empty:
        print(f"\n⚠  Empty or placeholder CONFIG.yaml values ({len(empty)}):")
        print("   These variables are mapped but their CONFIG.yaml value is empty")
        print("   or still contains a {{…}} placeholder.\n")
        for var, path in empty:
            print(f"   {var}  →  {path}")
        # Empty values are advisory for the upstream template — operators fill them
        # So we report but don't fail CI for these

    if format_errors:
        print(f"\n✗  Format validation errors ({len(format_errors)}):")
        for var, path, err in format_errors:
            print(f"   {var}  →  {path}: {err}")
        has_errors = True

    total = ok_count + len(empty) + len(format_errors)
    print(f"\n{'✓' if not has_errors else '⚠'}  Config completeness: "
          f"{ok_count}/{total} variables populated"
          f"{f', {len(unmapped)} unmapped' if unmapped else ''}"
          f"{f', {len(format_errors)} format error(s)' if format_errors else ''}")

    if has_errors:
        return 1
    return 0


# ---------------------------------------------------------------------------
# Self-check mode
# ---------------------------------------------------------------------------
def run_self_check() -> int:
    """Synthetic fixture tests. Returns 0 if all pass, 1 if any fail."""
    failures: list[str] = []

    def assert_eq(label: str, got: Any, expected: Any) -> None:
        if got != expected:
            failures.append(f"FAIL [{label}]: expected {expected!r}, got {got!r}")
        else:
            print(f"  PASS [{label}]")

    print("Running self-check…\n")

    # --- resolve_config_path ---
    sample = {
        "company": {"name": "Acme Corp", "short_name": "Acme"},
        "ventures": [
            {"id": "v1", "name": "Core", "description": "Core product"},
            {"id": "v2", "name": "Platform", "description": "Platform"},
        ],
        "toolchain": {"git_host": "GitHub", "observability": ""},
        "encryption": {"rsa2048_deprecation_date": "2028-12-31"},
        "integrations": {
            "observability": [
                {"name": "Datadog", "otlp_endpoint": "https://otel.example.com/v1"}
            ]
        },
    }

    assert_eq("resolve scalar", resolve_config_path(sample, "company.name"), "Acme Corp")
    assert_eq("resolve nested", resolve_config_path(sample, "company.short_name"), "Acme")
    assert_eq("resolve indexed", resolve_config_path(sample, "ventures[0].name"), "Core")
    assert_eq("resolve indexed[1]", resolve_config_path(sample, "ventures[1].description"), "Platform")
    assert_eq("resolve missing key", resolve_config_path(sample, "company.nonexistent"), None)
    assert_eq("resolve index OOB", resolve_config_path(sample, "ventures[5].name"), None)
    assert_eq("resolve deep indexed", resolve_config_path(sample, "integrations.observability[0].name"), "Datadog")

    # --- is_empty_value ---
    assert_eq("empty string", is_empty_value(""), True)
    assert_eq("None", is_empty_value(None), True)
    assert_eq("whitespace", is_empty_value("  "), True)
    assert_eq("placeholder", is_empty_value("{{VENTURE_1_NAME}}"), True)
    assert_eq("filled string", is_empty_value("Acme"), False)
    assert_eq("number", is_empty_value(42), False)
    assert_eq("zero", is_empty_value(0), False)
    assert_eq("bool false", is_empty_value(False), False)

    # --- validate_format ---
    assert_eq("valid URL", validate_format("otlp_endpoint", "https://otel.example.com/v1"), None)
    assert_eq("invalid URL", validate_format("otlp_endpoint", "not-a-url") is not None, True)
    assert_eq("valid domain", validate_format("domain", "acme.com"), None)
    assert_eq("invalid domain", validate_format("domain", "just-a-word") is not None, True)
    assert_eq("valid date", validate_format("rsa2048_deprecation_date", "2028-12-31"), None)
    assert_eq("invalid date", validate_format("rsa2048_deprecation_date", "next year") is not None, True)
    assert_eq("no validator", validate_format("company.name", "anything"), None)

    # --- scan_framework_files (with temp dir) ---
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)

        # Create a framework file with variables
        (root / "test.md").write_text("Welcome to {{COMPANY_NAME}}!\nPowered by {{GIT_HOST}}.\n")

        # Create a template file (should be skipped)
        (root / "_TEMPLATE-mission.md").write_text("{{SHOULD_NOT_APPEAR}}\n")

        # Create a CHANGELOG file (should be skipped)
        (root / "CHANGELOG.md").write_text("Fixed {{SOME_VAR}} issue\n")

        found = scan_framework_files(root)
        assert_eq("finds COMPANY_NAME", "COMPANY_NAME" in found, True)
        assert_eq("finds GIT_HOST", "GIT_HOST" in found, True)
        assert_eq("skips _TEMPLATE", "SHOULD_NOT_APPEAR" not in found, True)
        assert_eq("skips CHANGELOG", "SOME_VAR" not in found, True)

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
        description="Validate CONFIG.yaml completeness against {{VARIABLE}} usage."
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
