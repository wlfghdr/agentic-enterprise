#!/usr/bin/env python3
"""
OTel contract compliance validation for Agentic Enterprise framework.

Validates:
  - docs/otel-contract.md exposes a machine-readable span contract
  - Agent type definitions reference the OTel contract and declare telemetry
  - Skill manifests declare telemetry aligned to the OTel contract
  - Observability integration docs expose required OTel/OTLP examples
  - Policies that rely on telemetry reference the canonical OTel contract

Closes #115.

Usage:
  python3 scripts/validate_otel_contract.py

Exit codes:
  0  All validations passed
  1  One or more validation failures
  2  Setup/import error (pyyaml not installed)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).parent.parent.resolve()
OTEL_CONTRACT = REPO / "docs" / "otel-contract.md"
OBSERVABILITY_DOC = REPO / "org" / "integrations" / "categories" / "observability.md"

CANONICAL_CONTRACT_REF = "docs/otel-contract.md"
KNOWN_CONTRACT_REFS = ("docs/otel-contract.md", "docs/OTEL-CONTRACT.md")

CORE_AGENT_SPANS = {"agent.run", "tool.execute"}
INFERENCE_SPANS = {"inference.chat", "inference.generate"}
TELEMETRY_POLICY_HINTS = (
    "OpenTelemetry",
    "agent.run",
    "tool.execute",
    "governance.decision",
    "inference.",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_contract_reference(text: str) -> bool:
    return any(ref in text for ref in KNOWN_CONTRACT_REFS)


def extract_markdown_section(text: str, title: str) -> str | None:
    pattern = rf"^##\s+{re.escape(title)}\s*$\n(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    return match.group(1).strip()


def extract_contract_schema() -> dict:
    text = read_text(OTEL_CONTRACT)
    match = re.search(
        r"^##\s+11\.\s+Machine-Readable Schema Appendix.*?^```yaml\n(.*?)^```",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError("docs/otel-contract.md: missing machine-readable YAML appendix")

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"docs/otel-contract.md: cannot parse YAML appendix — {exc}") from exc

    if not isinstance(data, dict) or "span_types" not in data:
        raise ValueError("docs/otel-contract.md: YAML appendix missing top-level 'span_types'")

    return data


def discover_agent_type_files() -> list[Path]:
    return sorted(
        path
        for path in (REPO / "org" / "agents").rglob("*.md")
        if path.is_file() and path.name != "README.md" and "_TEMPLATE" not in path.name
    )


def discover_policy_files() -> list[Path]:
    return sorted(
        path
        for path in (REPO / "org" / "4-quality" / "policies").glob("*.md")
        if path.is_file() and path.name != "README.md"
    )


def discover_skill_manifests() -> list[Path]:
    return sorted((REPO / "org" / "skills").glob("*.skill.json"))

def format_rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def validate_agent_types(contract: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    contract_span_names = {
        item.get("name")
        for item in contract.get("span_types", [])
        if isinstance(item, dict) and item.get("name")
    }

    missing_contract_spans = sorted((CORE_AGENT_SPANS | INFERENCE_SPANS) - contract_span_names)
    if missing_contract_spans:
        errors.append(
            "docs/otel-contract.md: machine-readable schema missing canonical span types: "
            + ", ".join(missing_contract_spans)
        )
        return errors, warnings

    for path in discover_agent_type_files():
        rel = format_rel(path)
        text = read_text(path)

        if not has_contract_reference(text):
            errors.append(f"{rel}: missing reference to {CANONICAL_CONTRACT_REF}")

        telemetry = extract_markdown_section(text, "Telemetry")
        if telemetry is None:
            errors.append(
                f"{rel}: missing '## Telemetry' section declaring contract-aligned spans"
            )
            continue

        for span in sorted(CORE_AGENT_SPANS):
            if span not in telemetry:
                errors.append(
                    f"{rel}: Telemetry section missing required span declaration '{span}'"
                )

        has_model_governance = bool(
            re.search(r"^##\s+Model Governance\b", text, re.MULTILINE)
        )
        if has_model_governance and not any(
            span in telemetry or "inference.*" in telemetry for span in INFERENCE_SPANS
        ):
            errors.append(
                f"{rel}: model-governed agent must declare `inference.chat` and/or "
                f"`inference.generate` in Telemetry section"
            )
    return errors, warnings


def validate_skill_manifests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in discover_skill_manifests():
        rel = format_rel(path)
        try:
            data = json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON — {exc}")
            continue

        telemetry = data.get("telemetry")
        if not isinstance(telemetry, dict):
            errors.append(f"{rel}: missing required `telemetry` object")
            continue

        contract_ref = telemetry.get("contract")
        if contract_ref != CANONICAL_CONTRACT_REF:
            errors.append(
                f"{rel}: telemetry.contract must be '{CANONICAL_CONTRACT_REF}', got {contract_ref!r}"
            )

        required_spans = telemetry.get("required_spans")
        if not isinstance(required_spans, list):
            errors.append(f"{rel}: telemetry.required_spans must be a list")
            continue

        for span in sorted(CORE_AGENT_SPANS):
            if span not in required_spans:
                errors.append(f"{rel}: telemetry.required_spans missing '{span}'")

        conditional_spans = telemetry.get("conditional_spans", [])
        if conditional_spans and not isinstance(conditional_spans, list):
            errors.append(f"{rel}: telemetry.conditional_spans must be a list when present")
        elif isinstance(conditional_spans, list):
            invalid_spans = sorted(set(conditional_spans) - INFERENCE_SPANS)
            if invalid_spans:
                errors.append(
                    f"{rel}: telemetry.conditional_spans contains unknown spans: "
                    + ", ".join(invalid_spans)
                )

        decision_events = telemetry.get("decision_events")
        if not isinstance(decision_events, list) or "governance.decision" not in decision_events:
            errors.append(
                f"{rel}: telemetry.decision_events must include 'governance.decision'"
            )

        if not conditional_spans:
            warnings.append(
                f"{rel}: telemetry.conditional_spans is empty; add inference spans if the "
                f"skill uses model-backed reasoning"
            )

    return errors, warnings


def validate_observability_docs() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    obs_doc = read_text(OBSERVABILITY_DOC)
    if not has_contract_reference(obs_doc):
        errors.append(
            f"{format_rel(OBSERVABILITY_DOC)}: missing reference to {CANONICAL_CONTRACT_REF}"
        )

    for token in ("connection:", "mcp_server:"):
        if token not in obs_doc:
            errors.append(
                f"{format_rel(OBSERVABILITY_DOC)}: missing configuration example field '{token}'"
            )
    if "otlp_endpoint:" not in obs_doc and not ("endpoints:" in obs_doc and "otlp:" in obs_doc):
        errors.append(
            f"{format_rel(OBSERVABILITY_DOC)}: missing OTLP endpoint configuration example"
        )

    return errors, warnings


def validate_policies() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in discover_policy_files():
        rel = format_rel(path)
        text = read_text(path)
        if not any(hint in text for hint in TELEMETRY_POLICY_HINTS):
            continue

        if not has_contract_reference(text):
            errors.append(f"{rel}: telemetry-relevant policy missing {CANONICAL_CONTRACT_REF}")

        if "OTEL-CONTRACT.md" in text:
            warnings.append(
                f"{rel}: uses legacy 'OTEL-CONTRACT.md' spelling; prefer '{CANONICAL_CONTRACT_REF}'"
            )

    return errors, warnings


def main() -> int:
    all_errors: list[str] = []
    all_warnings: list[str] = []
    ok_labels: list[str] = []

    try:
        contract = extract_contract_schema()
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if not contract.get("resource_attributes"):
        all_errors.append("docs/otel-contract.md: YAML appendix missing 'resource_attributes'")

    errors, warnings = validate_agent_types(contract)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    if not errors:
        ok_labels.append("agent type telemetry")

    errors, warnings = validate_skill_manifests()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    if not errors:
        ok_labels.append("skill manifest telemetry")

    errors, warnings = validate_observability_docs()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    if not errors:
        ok_labels.append("observability integration docs")

    errors, warnings = validate_policies()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    if not errors:
        ok_labels.append("telemetry-aware policies")

    for label in ok_labels:
        print(f"  ✓  {label}")

    if all_warnings:
        print(f"\n{len(all_warnings)} warning(s):")
        for warning in all_warnings:
            print(f"  ⚠  {warning}")

    if all_errors:
        print(f"\n{len(all_errors)} OTel contract error(s):")
        for err in all_errors:
            print(f"  ✗  {err}")
        return 1

    print("\nOTel contract validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
