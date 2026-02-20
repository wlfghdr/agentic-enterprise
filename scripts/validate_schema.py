#!/usr/bin/env python3
"""
Schema validation for core Agentic Enterprise framework artifacts.

Validates:
  - CONFIG.yaml             → schemas/config.schema.json       (JSON Schema)
  - work/signals/**         → schemas/work/signal.schema.json  (custom markdown)
  - work/missions/**/mission-brief.md  → schemas/work/mission-brief.schema.json
  - work/releases/**        → schemas/work/release-contract.schema.json

Usage:
  python3 scripts/validate_schema.py [--strict]

Exit codes:
  0  All validations passed
  1  One or more validation failures (schema errors)
  2  Setup/import error (jsonschema not installed)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ── Dependency check ──────────────────────────────────────────────────────────
try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

try:
    import jsonschema
    from jsonschema import validate, ValidationError, SchemaError
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

# ── Repo root ─────────────────────────────────────────────────────────────────
REPO = Path(__file__).parent.parent.resolve()

# ── Helpers ───────────────────────────────────────────────────────────────────


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _strip_value(raw: str) -> str:
    """Strip trailing whitespace, inline comments and `_` emphasis chars."""
    value = raw.strip()
    # Remove trailing markdown italic wrapper: e.g. "true _(...)"
    value = re.sub(r"\s+_\(.*$", "", value)
    return value.strip()


# ── CONFIG.yaml validation (JSON Schema) ─────────────────────────────────────


def validate_config(schema_path: Path, config_path: Path) -> list[str]:
    """Validate CONFIG.yaml against its JSON Schema. Returns list of error messages."""
    errors: list[str] = []
    schema = load_json(schema_path)

    try:
        instance = load_yaml(config_path)
    except yaml.YAMLError as exc:
        return [f"CONFIG.yaml: YAML parse error — {exc}"]

    if instance is None:
        return ["CONFIG.yaml: file is empty"]

    try:
        validate(instance=instance, schema=schema)
    except ValidationError as exc:
        path_str = " → ".join(str(p) for p in exc.absolute_path) or "(root)"
        errors.append(f"CONFIG.yaml [{path_str}]: {exc.message}")
    except SchemaError as exc:
        errors.append(f"Schema error in {schema_path.name}: {exc.message}")

    return errors


# ── Markdown work-artifact validation ─────────────────────────────────────────


def get_sections(text: str) -> set[str]:
    """Return the set of second-level heading titles (## ...) found in markdown text."""
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+)", text, re.MULTILINE)}


def validate_markdown_artifact(path: Path, schema: dict) -> list[str]:
    """Validate a single markdown artifact file against a custom markdown schema."""
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{path}: cannot read file — {exc}"]

    rel = path.relative_to(REPO)

    # ── Filename pattern ───────────────────────────────────────────────────
    filename_pattern = schema.get("filename_pattern")
    if filename_pattern and not re.search(filename_pattern, path.name):
        errors.append(
            f"{rel}: filename '{path.name}' does not match expected pattern '{filename_pattern}'"
        )

    # ── Required sections ──────────────────────────────────────────────────
    present_sections = get_sections(text)
    for section in schema.get("required_sections", []):
        if section not in present_sections:
            errors.append(f"{rel}: missing required section '## {section}'")

    # ── Required fields ────────────────────────────────────────────────────
    for field_def in schema.get("required_fields", []):
        name = field_def["name"]
        pattern = field_def["inline_pattern"]
        required = field_def.get("required", True)

        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            if required:
                errors.append(f"{rel}: missing required field '**{name}:**'")
            continue

        raw_value = match.group(1) if match.lastindex else ""
        value = _strip_value(raw_value)

        # Skip unfilled template placeholders like [text] or YYYY-MM-DD
        if value.startswith("[") or value.startswith("YYYY") or value == "":
            # Unfilled template field — only warn if strictly required
            # (templates themselves are excluded from scanning, so this
            #  indicates an actual artifact was left unfilled)
            errors.append(
                f"{rel}: field '**{name}:**' appears unfilled (value: '{value}')"
            )
            continue

        # Enum check
        allowed = field_def.get("allowed_values")
        if allowed and value.lower() not in [v.lower() for v in allowed]:
            errors.append(
                f"{rel}: field '**{name}:**' has invalid value '{value}' "
                f"(expected one of: {', '.join(allowed)})"
            )

        # ID pattern check
        id_pattern = field_def.get("id_pattern")
        if id_pattern and not re.match(id_pattern, value, re.IGNORECASE):
            errors.append(
                f"{rel}: field '**{name}:**' value '{value}' does not match "
                f"expected pattern '{id_pattern}'"
            )

    return errors


# ── File discovery ────────────────────────────────────────────────────────────

def is_template(path: Path) -> bool:
    return "_TEMPLATE" in path.name or "stale.yml" in path.name


def discover_signals() -> list[Path]:
    """Find non-template signal markdown files (top-level in work/signals/, not in digests/)."""
    signals_dir = REPO / "work" / "signals"
    if not signals_dir.exists():
        return []
    return [
        p for p in signals_dir.glob("*.md")
        if p.is_file() and not is_template(p) and p.name != "README.md"
    ]


def discover_mission_briefs() -> list[Path]:
    """Find BRIEF.md / mission-brief.md files in work/missions/ subdirectories."""
    missions_dir = REPO / "work" / "missions"
    if not missions_dir.exists():
        return []
    results = []
    for pattern in ("BRIEF.md", "mission-brief.md"):
        results.extend(
            p for p in missions_dir.rglob(pattern)
            if p.is_file() and not is_template(p)
        )
    return results


def discover_release_contracts() -> list[Path]:
    """Find release-contract.md files in work/releases/."""
    releases_dir = REPO / "work" / "releases"
    if not releases_dir.exists():
        return []
    return [
        p for p in releases_dir.glob("*.md")
        if p.is_file()
        and not is_template(p)
        and p.name != "README.md"
        and "release-contract" in p.name
    ]


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> int:
    all_errors: list[str] = []
    all_ok: list[str] = []

    # ── 1. CONFIG.yaml ─────────────────────────────────────────────────────
    config_schema_path = REPO / "schemas" / "config.schema.json"
    config_path = REPO / "CONFIG.yaml"

    if not config_schema_path.exists():
        all_errors.append(f"Schema file missing: {config_schema_path.relative_to(REPO)}")
    elif not config_path.exists():
        all_errors.append("CONFIG.yaml not found at repository root")
    else:
        errs = validate_config(config_schema_path, config_path)
        if errs:
            all_errors.extend(errs)
        else:
            all_ok.append("CONFIG.yaml")

    # ── 2. Signal artifacts ────────────────────────────────────────────────
    signal_schema_path = REPO / "schemas" / "work" / "signal.schema.json"
    if signal_schema_path.exists():
        signal_schema = load_json(signal_schema_path)
        signal_files = discover_signals()
        if not signal_files:
            print("INFO: No non-template signal files found — skipping signal validation.")
        for f in signal_files:
            errs = validate_markdown_artifact(f, signal_schema)
            if errs:
                all_errors.extend(errs)
            else:
                all_ok.append(str(f.relative_to(REPO)))
    else:
        all_errors.append(f"Schema file missing: {signal_schema_path.relative_to(REPO)}")

    # ── 3. Mission briefs ──────────────────────────────────────────────────
    mission_schema_path = REPO / "schemas" / "work" / "mission-brief.schema.json"
    if mission_schema_path.exists():
        mission_schema = load_json(mission_schema_path)
        mission_files = discover_mission_briefs()
        if not mission_files:
            print("INFO: No non-template mission-brief files found — skipping mission validation.")
        for f in mission_files:
            errs = validate_markdown_artifact(f, mission_schema)
            if errs:
                all_errors.extend(errs)
            else:
                all_ok.append(str(f.relative_to(REPO)))
    else:
        all_errors.append(f"Schema file missing: {mission_schema_path.relative_to(REPO)}")

    # ── 4. Release contracts ───────────────────────────────────────────────
    release_schema_path = REPO / "schemas" / "work" / "release-contract.schema.json"
    if release_schema_path.exists():
        release_schema = load_json(release_schema_path)
        release_files = discover_release_contracts()
        if not release_files:
            print("INFO: No non-template release-contract files found — skipping release validation.")
        for f in release_files:
            errs = validate_markdown_artifact(f, release_schema)
            if errs:
                all_errors.extend(errs)
            else:
                all_ok.append(str(f.relative_to(REPO)))
    else:
        all_errors.append(f"Schema file missing: {release_schema_path.relative_to(REPO)}")

    # ── Report ──────────────────────────────────────────────────────────────
    for ok in all_ok:
        print(f"  ✓  {ok}")

    if all_errors:
        print(f"\n{len(all_errors)} schema validation error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        print(
            "\nSee schemas/ for definitions and docs/SCHEMA-GUIDE.md for contribution guidelines."
        )
        return 1

    total = len(all_ok)
    print(f"\nSchema validation passed ({total} artifact(s) checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
