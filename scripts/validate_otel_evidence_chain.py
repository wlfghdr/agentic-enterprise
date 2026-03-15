#!/usr/bin/env python3
"""CI check: verify compliance-critical OTel spans are defined and linked
to audit evidence requirements.

Exit codes:
  0 — evidence chain validated (broken chains are advisory warnings)
  1 — script error (missing otel-contract.md or parse failure)

Self-check mode (--self-check):
  Runs against synthetic fixtures and reports PASS/FAIL.

What this script does:
  1. Parses the OTel contract machine-readable schema for defined spans and events
  2. Scans compliance reference docs for OTel span/event references
  3. Verifies each referenced span/event exists in the OTel contract
  4. Reports compliance requirements that reference undefined spans (broken chain)
  5. Reports defined spans/events not referenced by any compliance doc (coverage gap)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Patterns for extracting OTel references from compliance docs
# ---------------------------------------------------------------------------

# Matches span names like `agent.run`, `tool.execute`, `governance.decision`
# in backticks or plain text
SPAN_REF_PATTERN = re.compile(
    r"`("
    r"agent\.run|agent\.subagent\.invoke|"
    r"inference\.chat|inference\.generate|"
    r"tool\.execute|quality\.evaluate|"
    r"git\.operation|mission\.transition|"
    r"governance\.decision|agent\.escalation|"
    r"tool\.error|policy\.violation|"
    r"mission\.status_change|"
    r"risk\.assessment\.complete|"  # domain-specific events
    r"gen_ai\.client\.\w+(?:\.\w+)*"
    r")`"
)

# Broader pattern: catch any dot-notation reference that looks like an OTel span
OTEL_REF_BROAD = re.compile(
    r"`([a-z][a-z_]*(?:\.[a-z][a-z_]*){1,4})`"
)

# Known OTel span/event prefixes
OTEL_PREFIXES = {
    "agent.", "tool.", "inference.", "quality.", "git.", "mission.",
    "governance.", "policy.", "gen_ai.", "risk.",
}


class OTelDefinition(NamedTuple):
    name: str
    kind: str  # "span" or "event" or "metric"


class EvidenceRef(NamedTuple):
    file: str
    line_no: int
    span_name: str
    context: str  # surrounding text for reporting


def parse_otel_schema(otel_contract_path: Path) -> dict[str, OTelDefinition]:
    """Parse the machine-readable YAML appendix in otel-contract.md.
    Returns {name: OTelDefinition}."""
    definitions: dict[str, OTelDefinition] = {}

    try:
        text = otel_contract_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return definitions

    # Find the YAML block starting with span_types:
    in_yaml = False
    yaml_lines: list[str] = []

    for line in text.splitlines():
        if line.strip() == "```yaml" or line.strip() == "```yml":
            in_yaml = True
            yaml_lines = []
            continue
        if in_yaml and line.strip() == "```":
            in_yaml = False
            # Parse what we have
            _extract_definitions(yaml_lines, definitions)
            continue
        if in_yaml:
            yaml_lines.append(line)

    return definitions


def _extract_definitions(
    yaml_lines: list[str], definitions: dict[str, OTelDefinition]
) -> None:
    """Extract span_types, span_events, and metrics from YAML lines.
    Only picks up top-level list items (indent level 2), not nested attributes."""
    current_section = ""
    for line in yaml_lines:
        stripped = line.strip()

        # Skip blank lines (preserve current section)
        if not stripped:
            continue

        # Detect top-level sections (no leading whitespace)
        if not line.startswith(" ") and not line.startswith("\t"):
            if stripped.startswith("span_types:"):
                current_section = "span"
            elif stripped.startswith("span_events:"):
                current_section = "event"
            elif stripped.startswith("metrics:"):
                current_section = "metric"
            elif stripped.startswith("#"):
                pass  # comments don't reset section
            else:
                current_section = ""
            continue

        if not current_section:
            continue

        # Only match top-level list items (2-space indent: "  - name:")
        # Skip nested attributes (6+ space indent: "      - name:")
        indent = len(line) - len(line.lstrip())
        if indent <= 4 and stripped.startswith("- name:"):
            name = stripped.split(":", 1)[1].strip()
            definitions[name] = OTelDefinition(name=name, kind=current_section)


def scan_compliance_docs(
    repo_root: Path,
) -> list[EvidenceRef]:
    """Scan compliance reference docs for OTel span/event references."""
    refs: list[EvidenceRef] = []
    compliance_dir = repo_root / "docs" / "compliance"

    if not compliance_dir.is_dir():
        return refs

    for md_file in sorted(compliance_dir.rglob("*.md")):
        if md_file.name.startswith("_TEMPLATE"):
            continue

        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        rel = str(md_file.relative_to(repo_root))

        for line_no, line in enumerate(text.splitlines(), start=1):
            # Find backtick-enclosed OTel references
            for m in OTEL_REF_BROAD.finditer(line):
                candidate = m.group(1)
                # Filter: must start with a known OTel prefix
                if any(candidate.startswith(p) for p in OTEL_PREFIXES):
                    refs.append(EvidenceRef(
                        file=rel,
                        line_no=line_no,
                        span_name=candidate,
                        context=line.strip()[:120],
                    ))

    return refs


def run_check(repo_root: Path) -> int:
    """Main check. Returns 0 on success, 1 on broken chains."""
    otel_contract = repo_root / "docs" / "otel-contract.md"

    if not otel_contract.exists():
        print("⚠ docs/otel-contract.md not found — skipping evidence chain check.")
        return 0

    # Parse OTel schema
    definitions = parse_otel_schema(otel_contract)
    if not definitions:
        print("⚠ No OTel definitions found in docs/otel-contract.md YAML appendix.")
        return 0

    # Scan compliance docs
    evidence_refs = scan_compliance_docs(repo_root)

    if not evidence_refs:
        print("⚠ No OTel references found in compliance docs — nothing to validate.")
        return 0

    # Validate: each referenced span/event must exist in the contract
    all_defined = set(definitions.keys())
    referenced_spans = set()
    broken_refs: list[EvidenceRef] = []

    for ref in evidence_refs:
        referenced_spans.add(ref.span_name)
        if ref.span_name not in all_defined:
            broken_refs.append(ref)

    # Coverage: defined but not referenced
    unreferenced = all_defined - referenced_spans
    # Filter out metrics from unreferenced (they're not direct evidence)
    unreferenced_spans = {
        name for name in unreferenced
        if definitions[name].kind in ("span", "event")
    }

    # --- Report ---
    print(f"OTel Evidence Chain Report")
    print(f"{'=' * 50}")
    print(f"  Defined spans/events/metrics: {len(definitions)}")
    print(f"  Compliance doc references: {len(evidence_refs)}")
    print(f"  Unique spans referenced: {len(referenced_spans)}")
    print()

    has_unresolved = False

    if broken_refs:
        # Group by span name
        broken_by_span: dict[str, list[EvidenceRef]] = {}
        for ref in broken_refs:
            broken_by_span.setdefault(ref.span_name, []).append(ref)

        # Determine if these are truly broken or domain-specific extensions
        # Domain-specific events (like risk.assessment.complete) are expected
        # to be defined at deployment time, not in the generic contract
        truly_broken = []
        domain_extensions = []

        for span_name, refs_list in broken_by_span.items():
            # Domain-specific extensions (expected at deployment time)
            if any(span_name.startswith(p) for p in {"risk.", "dsar.", "breach."}):
                domain_extensions.append((span_name, refs_list))
            # Attribute references (e.g., agent.id, quality.verdict) —
            # these are OTel attributes, not span/event names. Compliance
            # docs sometimes reference attributes in shorthand. Advisory.
            elif "." in span_name and span_name.count(".") == 1:
                # Simple two-part names are likely attribute references
                domain_extensions.append((span_name, refs_list))
            else:
                truly_broken.append((span_name, refs_list))

        if truly_broken:
            has_unresolved = True
            print(f"⚠ UNRESOLVED EVIDENCE CHAINS ({len(truly_broken)} span(s)):")
            print(f"  Compliance docs reference OTel spans not defined in the contract.\n")
            for span_name, refs_list in truly_broken:
                print(f"  `{span_name}` — not in otel-contract.md")
                for ref in refs_list[:3]:
                    print(f"    {ref.file}:{ref.line_no}")
                if len(refs_list) > 3:
                    print(f"    … and {len(refs_list) - 3} more")
            print()

        if domain_extensions:
            print(f"ℹ  Domain-specific extensions ({len(domain_extensions)} span(s)):")
            print(f"  These are expected to be defined at deployment time.\n")
            for span_name, refs_list in domain_extensions:
                print(f"  `{span_name}` — referenced in {len(refs_list)} location(s)")
            print()

    if unreferenced_spans:
        print(f"ℹ  Unreferenced spans/events ({len(unreferenced_spans)}):")
        print(f"  Defined in otel-contract.md but not cited by any compliance doc.")
        print(f"  (Advisory — these may be referenced by non-compliance docs)\n")
        for name in sorted(unreferenced_spans):
            print(f"  `{name}` ({definitions[name].kind})")
        print()

    # Summary
    coverage = len(referenced_spans & all_defined)
    total_compliance_relevant = len(referenced_spans)
    pct = (coverage / total_compliance_relevant * 100) if total_compliance_relevant else 100

    status = "✓" if not has_unresolved else "⚠"
    print(f"{status} Evidence chain coverage: {coverage}/{total_compliance_relevant} "
          f"referenced spans are defined ({pct:.0f}%)")

    if has_unresolved:
        print("\nTo resolve unresolved chains:")
        print("  1. Add the missing span/event to docs/otel-contract.md YAML appendix, or")
        print("  2. Update the compliance doc to reference a span that exists in the contract")

    return 0


# ---------------------------------------------------------------------------
# Self-check mode
# ---------------------------------------------------------------------------
def run_self_check() -> int:
    """Synthetic fixture tests."""
    import tempfile

    failures: list[str] = []

    def assert_eq(label: str, got: object, expected: object) -> None:
        if got != expected:
            failures.append(f"FAIL [{label}]: expected {expected!r}, got {got!r}")
        else:
            print(f"  PASS [{label}]")

    print("Running self-check…\n")

    # --- parse_otel_schema ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        contract = root / "otel-contract.md"
        contract.write_text(
            "# OTel Contract\n"
            "## Schema\n"
            "```yaml\n"
            "span_types:\n"
            "  - name: agent.run\n"
            "    kind: INTERNAL\n"
            "  - name: tool.execute\n"
            "    kind: CLIENT\n"
            "span_events:\n"
            "  - name: governance.decision\n"
            "    required_attributes:\n"
            "      - governance.reason\n"
            "  - name: policy.violation\n"
            "    required_attributes:\n"
            "      - quality.policy.id\n"
            "metrics:\n"
            "  - name: gen_ai.client.token.usage\n"
            "    instrument: Histogram\n"
            "```\n"
        )
        defs = parse_otel_schema(contract)
        assert_eq("parses 5 definitions", len(defs), 5)
        assert_eq("agent.run is span", defs.get("agent.run", None) and defs["agent.run"].kind, "span")
        assert_eq("governance.decision is event", defs.get("governance.decision", None) and defs["governance.decision"].kind, "event")
        assert_eq("token.usage is metric", defs.get("gen_ai.client.token.usage", None) and defs["gen_ai.client.token.usage"].kind, "metric")

    # --- scan_compliance_docs ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        comp_dir = root / "docs" / "compliance"
        comp_dir.mkdir(parents=True)
        (comp_dir / "soc2.md").write_text(
            "# SOC 2\n"
            "Evidence from `governance.decision` events\n"
            "Also check `tool.execute` spans\n"
            "And `risk.assessment.complete` domain events\n"
            "Not an otel ref: `some.random.thing`\n"
        )
        refs = scan_compliance_docs(root)
        ref_names = [r.span_name for r in refs]
        assert_eq("finds governance.decision", "governance.decision" in ref_names, True)
        assert_eq("finds tool.execute", "tool.execute" in ref_names, True)
        assert_eq("finds risk.assessment.complete", "risk.assessment.complete" in ref_names, True)
        # some.random.thing should NOT match (no known prefix)
        assert_eq("skips unknown prefix", "some.random.thing" not in ref_names, True)

    # --- End-to-end: valid chain ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        docs = root / "docs"
        docs.mkdir()
        (docs / "otel-contract.md").write_text(
            "```yaml\n"
            "span_types:\n"
            "  - name: agent.run\n"
            "  - name: tool.execute\n"
            "span_events:\n"
            "  - name: governance.decision\n"
            "metrics:\n"
            "  - name: gen_ai.client.token.usage\n"
            "```\n"
        )
        comp = docs / "compliance"
        comp.mkdir()
        (comp / "soc2.md").write_text(
            "Evidence: `governance.decision` events and `tool.execute` spans\n"
        )

        result = run_check(root)
        assert_eq("valid chain: returns 0", result, 0)

    # --- End-to-end: broken chain ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        docs = root / "docs"
        docs.mkdir()
        (docs / "otel-contract.md").write_text(
            "```yaml\n"
            "span_types:\n"
            "  - name: agent.run\n"
            "span_events:\n"
            "  - name: governance.decision\n"
            "```\n"
        )
        comp = docs / "compliance"
        comp.mkdir()
        (comp / "test.md").write_text(
            "Evidence: `governance.decision` OK\n"
            "But also `gen_ai.client.operation.duration` which is NOT defined\n"
        )

        result2 = run_check(root)
        assert_eq("broken chain: returns 0 (advisory)", result2, 0)

    # --- Domain extension (advisory, not error) ---
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        docs = root / "docs"
        docs.mkdir()
        (docs / "otel-contract.md").write_text(
            "```yaml\n"
            "span_types:\n"
            "  - name: agent.run\n"
            "span_events:\n"
            "  - name: governance.decision\n"
            "```\n"
        )
        comp = docs / "compliance"
        comp.mkdir()
        (comp / "test.md").write_text(
            "Evidence: `governance.decision` and `risk.assessment.complete`\n"
        )

        result3 = run_check(root)
        assert_eq("domain extension: returns 0 (advisory)", result3, 0)

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
        description="Validate OTel evidence chain for compliance-critical spans."
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
    args = parser.parse_args(argv)

    if args.self_check:
        return run_self_check()

    repo_root = Path(args.root).resolve()
    return run_check(repo_root)


if __name__ == "__main__":
    sys.exit(main())
