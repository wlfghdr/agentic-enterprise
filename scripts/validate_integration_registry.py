#!/usr/bin/env python3
"""
Integration registry consistency validation for Agentic Enterprise framework.

Validates:
  - CONFIG.yaml integration categories match integration category docs
  - Observability integration exists and declares required OTel/OTLP fields
  - Configured integration entries have the expected registry keys
  - Integration specification files (if present) include required metadata

Closes #117.

Usage:
  python3 scripts/validate_integration_registry.py

Exit codes:
  0  All validations passed
  1  One or more validation failures
  2  Setup/import error (pyyaml not installed)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).parent.parent.resolve()
CONFIG_PATH = REPO / "CONFIG.yaml"
INTEGRATIONS_DIR = REPO / "org" / "integrations"
CATEGORY_DIR = INTEGRATIONS_DIR / "categories"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def format_rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def is_placeholder(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        stripped = value.strip()
        return stripped == "" or "{{" in stripped or "}}" in stripped
    return False


def category_doc_keys() -> set[str]:
    return {
        path.stem.replace("-", "_")
        for path in CATEGORY_DIR.glob("*.md")
        if path.is_file() and path.name != "README.md"
    }


def load_config() -> dict:
    data = yaml.safe_load(read_text(CONFIG_PATH))
    return data if isinstance(data, dict) else {}


def iter_config_entries(config: dict) -> list[tuple[str, str | None, dict]]:
    integrations = (config.get("integrations") or {})
    entries: list[tuple[str, str | None, dict]] = []

    observability = integrations.get("observability") or []
    if isinstance(observability, list):
        for entry in observability:
            entries.append(("observability", None, entry))

    enterprise_toolchain = integrations.get("enterprise_toolchain") or {}
    if isinstance(enterprise_toolchain, dict):
        for subgroup, items in enterprise_toolchain.items():
            if not isinstance(items, list):
                continue
            for entry in items:
                entries.append(("enterprise_toolchain", subgroup, entry))

    for category in ("business_systems", "communication"):
        items = integrations.get(category) or []
        if isinstance(items, list):
            for entry in items:
                entries.append((category, None, entry))

    return entries


def validate_category_docs(config: dict) -> list[str]:
    errors: list[str] = []
    configured = set((config.get("integrations") or {}).keys())
    docs = category_doc_keys()

    for key in sorted(configured - docs):
        errors.append(
            f"CONFIG.yaml: integration category '{key}' has no matching file in "
            f"org/integrations/categories/"
        )

    for key in sorted(docs - configured):
        errors.append(
            f"org/integrations/categories/{key.replace('_', '-')}.md: category file has "
            f"no matching entry under CONFIG.yaml integrations"
        )

    for path in sorted(CATEGORY_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(path)
        if "**Category:**" not in text:
            errors.append(f"{format_rel(path)}: missing required metadata '**Category:**'")

    return errors


def validate_observability_exists(config: dict) -> list[str]:
    errors: list[str] = []
    observability = ((config.get("integrations") or {}).get("observability"))
    if not isinstance(observability, list) or not observability:
        errors.append("CONFIG.yaml: integrations.observability must be a non-empty list")
    return errors


def validate_config_entries(config: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    allowed_connections = {
        "opentelemetry",
        "native-agent",
        "api",
        "mcp",
        "webhook",
        "data-export",
    }

    for index, (category, subgroup, entry) in enumerate(iter_config_entries(config), start=1):
        label = f"CONFIG.yaml: integrations.{category}"
        if subgroup:
            label += f".{subgroup}"
        label += f"[{index}]"

        if not isinstance(entry, dict):
            errors.append(f"{label}: integration entry must be a mapping")
            continue

        for field in ("id", "name", "connection"):
            if field not in entry:
                errors.append(f"{label}: missing required field '{field}'")

        connection = entry.get("connection")
        if connection and connection not in allowed_connections:
            warnings.append(
                f"{label}: connection '{connection}' is outside the current validator allowlist"
            )

        if "mcp_server" in entry and not isinstance(entry.get("mcp_server"), bool):
            errors.append(f"{label}: mcp_server must be true or false")

        active = any(
            not is_placeholder(entry.get(field))
            for field in ("name", "vendor", "otlp_endpoint")
        )

        if category == "observability":
            for field in ("vendor", "capabilities", "mcp_server"):
                if field not in entry:
                    errors.append(f"{label}: missing required field '{field}'")

            if "capabilities" in entry and not isinstance(entry.get("capabilities"), list):
                errors.append(f"{label}: capabilities must be a list")

            if connection == "opentelemetry" and "otlp_endpoint" not in entry:
                errors.append(
                    f"{label}: opentelemetry observability integrations must declare 'otlp_endpoint'"
                )

            if active:
                for field in ("name", "vendor"):
                    if is_placeholder(entry.get(field)):
                        errors.append(
                            f"{label}: active observability integration must populate '{field}'"
                        )
                if connection == "opentelemetry" and is_placeholder(entry.get("otlp_endpoint")):
                    errors.append(
                        f"{label}: active opentelemetry integration must populate 'otlp_endpoint'"
                    )

        if entry.get("mcp_server") is True and is_placeholder(entry.get("name")):
            warnings.append(f"{label}: mcp_server enabled on an unnamed integration entry")

    return errors, warnings


def integration_spec_files() -> list[Path]:
    return sorted(
        path
        for path in INTEGRATIONS_DIR.rglob("*.md")
        if path.is_file()
        and path.name != "README.md"
        and "_TEMPLATE" not in path.name
        and "categories" not in path.parts
    )


def parse_status(text: str) -> str | None:
    match = re.search(r"\*\*Status:\*\*\s*`?([a-z-]+)`?", text, re.IGNORECASE)
    return match.group(1).strip().lower() if match else None


def validate_integration_specs() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in integration_spec_files():
        rel = format_rel(path)
        text = read_text(path)
        for field in ("**Status:**", "**Category:**"):
            if field not in text:
                errors.append(f"{rel}: missing required metadata '{field}'")

        status = parse_status(text)
        if status == "active" and "{{" in text:
            errors.append(f"{rel}: active integration spec contains placeholder values")
        elif status is None:
            warnings.append(f"{rel}: could not determine integration status")

    return errors, warnings


def main() -> int:
    config = load_config()

    all_errors = []
    all_warnings = []

    all_errors.extend(validate_category_docs(config))
    all_errors.extend(validate_observability_exists(config))

    errors, warnings = validate_config_entries(config)
    all_errors.extend(errors)
    all_warnings.extend(warnings)

    errors, warnings = validate_integration_specs()
    all_errors.extend(errors)
    all_warnings.extend(warnings)

    if all_warnings:
        print(f"{len(all_warnings)} warning(s):")
        for warning in all_warnings:
            print(f"  ⚠  {warning}")
        print()

    if all_errors:
        print(f"{len(all_errors)} integration registry error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    print("Integration registry validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
