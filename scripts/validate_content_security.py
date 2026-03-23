#!/usr/bin/env python3
"""
Content security validation for Agentic Enterprise framework.

Scans governed files (agent instructions, policies, work artifacts, templates,
division configs) for prompt injection patterns, instruction override attempts,
hierarchy violations, and other content-level security risks.

This complements structural validators (validate_policy_structure.py,
validate_agent_instructions.py, validate_work_artifacts.py) by checking
the *content* of governed files — not just their structure.

Policy reference: org/4-quality/policies/agent-security.md §1–§4
OWASP LLM Top 10: LLM01 (Prompt Injection), LLM02 (Insecure Output Handling)

Usage:
  python3 scripts/validate_content_security.py [--root PATH] [--verbose]

Options:
  --root PATH   Alternate repository root (e.g., examples/e2e-loop)
  --verbose     Print details for each scanned file

Exit codes:
  0  All validations passed
  1  One or more content security findings
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent.resolve()

# ── Injection pattern categories ──────────────────────────────────────────────
#
# Each pattern has:
#   - id:          short identifier for suppression / reporting
#   - category:    grouping for the report
#   - description: human-readable explanation
#   - pattern:     compiled regex (case-insensitive)
#   - severity:    "error" (blocks CI) or "warning" (advisory)
#   - applies_to:  list of file categories this pattern applies to
#                  ("all", "instructions", "work", "templates", "scripts")

PATTERNS: list[dict] = [
    # ── 1. Direct instruction override attempts ───────────────────────────
    {
        "id": "INJ-001",
        "category": "Instruction Override",
        "description": "Direct instruction override phrase detected",
        "pattern": re.compile(
            r"(?:ignore|disregard|forget|override|bypass|skip)\s+"
            r"(?:all\s+)?(?:previous|prior|above|earlier|existing|your|the)\s+"
            r"(?:instructions?|rules?|guidelines?|directives?|constraints?|policies?|prompts?)",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    {
        "id": "INJ-002",
        "category": "Instruction Override",
        "description": "New instruction injection phrase detected",
        "pattern": re.compile(
            r"(?:new\s+instructions?|updated\s+instructions?|revised\s+instructions?|"
            r"from\s+now\s+on\s+you\s+(?:will|must|should|are)|"
            r"your\s+new\s+(?:role|instructions?|directives?|rules?)|"
            r"act\s+as\s+(?:if|though)\s+you\s+(?:are|were)\s+(?:a|an|the))\b",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    {
        "id": "INJ-003",
        "category": "Instruction Override",
        "description": "System prompt extraction attempt detected",
        "pattern": re.compile(
            r"(?:reveal|show|display|print|output|repeat|echo|dump|expose)\s+"
            r"(?:your\s+)?(?:system\s+prompt|instructions?|internal\s+(?:rules?|instructions?|prompt))",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    # ── 2. Role impersonation ─────────────────────────────────────────────
    {
        "id": "INJ-004",
        "category": "Role Impersonation",
        "description": "Role reassignment phrase detected",
        "pattern": re.compile(
            r"you\s+are\s+now\s+(?:a|an|the)\s+\w+",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["work", "templates"],
    },
    {
        "id": "INJ-005",
        "category": "Role Impersonation",
        "description": "Privilege escalation phrase in non-instruction file",
        "pattern": re.compile(
            r"(?:you\s+(?:now\s+)?have\s+(?:admin|root|full|unlimited|elevated|unrestricted)\s+"
            r"(?:access|permissions?|privileges?|rights?|authority)|"
            r"grant(?:ed)?\s+(?:yourself|you)\s+(?:admin|root|full|elevated)\s+(?:access|permissions?))",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["work", "templates"],
    },
    # ── 3. Hierarchy violations ───────────────────────────────────────────
    {
        "id": "HIE-001",
        "category": "Hierarchy Violation",
        "description": "Lower-level file attempts to override parent rules",
        "pattern": re.compile(
            r"(?:this\s+(?:overrides?|supersedes?|replaces?|takes?\s+precedence\s+over)\s+"
            r"(?:AGENTS?\.md|global\s+(?:rules?|instructions?)|parent\s+(?:rules?|instructions?))|"
            r"notwithstanding\s+(?:AGENTS?\.md|global\s+(?:rules?|instructions?)))",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["instructions", "work"],
    },
    {
        "id": "HIE-002",
        "category": "Hierarchy Violation",
        "description": "Non-Negotiable Rules redefinition attempt outside AGENTS.md",
        "pattern": re.compile(
            r"(?:^|\n)#+\s+Non-Negotiable\s+Rules",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["instructions_not_global"],
    },
    # ── 4. Unsafe code patterns in governed files ─────────────────────────
    {
        "id": "CODE-001",
        "category": "Unsafe Code Pattern",
        "description": "Dynamic execution directive in markdown",
        "pattern": re.compile(
            r"(?:eval|exec|subprocess\.call|os\.system|os\.popen|__import__)\s*\(",
            re.IGNORECASE,
        ),
        "severity": "warning",
        "applies_to": ["instructions", "work", "templates"],
    },
    {
        "id": "CODE-002",
        "category": "Unsafe Code Pattern",
        "description": "Shell injection risk — unquoted variable expansion in code block",
        "pattern": re.compile(
            r"\$\{?\w+\}?\s*[|;&]",
        ),
        "severity": "warning",
        "applies_to": ["instructions", "templates"],
    },
    # ── 5. Encoded payload detection ──────────────────────────────────────
    {
        "id": "ENC-001",
        "category": "Encoded Payload",
        "description": "Suspicious base64-encoded block (>100 chars) in governed file",
        "pattern": re.compile(
            r"(?:base64[:\s]+|data:[^;]+;base64,)[A-Za-z0-9+/=]{100,}",
            re.IGNORECASE,
        ),
        "severity": "warning",
        "applies_to": ["all"],
    },
    # ── 6. Trust boundary violations ──────────────────────────────────────
    {
        "id": "TRUST-001",
        "category": "Trust Boundary",
        "description": "Instruction to concatenate external content directly into prompts",
        "pattern": re.compile(
            r"(?:concatenate|inject|insert|embed|append|prepend)\s+"
            r"(?:external|user|untrusted|raw)\s+"
            r"(?:content|input|data|text)\s+"
            r"(?:into|to|in)\s+"
            r"(?:the\s+)?(?:system\s+)?prompt",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    {
        "id": "FLOW-001",
        "category": "Workflow Drift",
        "description": "Stale approval-label semantics detected",
        "pattern": re.compile(
            r"(?:approval:required|approval-required\s+semantics|approval\s+label|label\s+change\s+for\s+issue\s+backend)",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["instructions", "templates", "work", "scripts"],
    },
    {
        "id": "TRUST-002",
        "category": "Trust Boundary",
        "description": "Directive to skip or disable input validation",
        "pattern": re.compile(
            r"(?:skip|disable|bypass|turn\s+off|remove|ignore)\s+"
            r"(?:input\s+)?(?:validation|sanitization|filtering|escaping|checking)",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    # ── 7. Social engineering in work artifacts ───────────────────────────
    {
        "id": "SOC-001",
        "category": "Social Engineering",
        "description": "Urgency manipulation phrase in work artifact",
        "pattern": re.compile(
            r"(?:do\s+not\s+(?:review|check|verify|validate|question|inspect)|"
            r"skip\s+(?:review|approval|validation|testing|checks?)|"
            r"approve\s+(?:immediately|without\s+review|blindly|now)|"
            r"merge\s+(?:immediately|without\s+review|now\s+before)|"
            r"no\s+time\s+(?:to|for)\s+(?:review|check|verify))",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["work"],
    },
    # ── 8. Policy bypass attempts ─────────────────────────────────────────
    {
        "id": "POL-001",
        "category": "Policy Bypass",
        "description": "Directive to ignore or disable quality policies",
        "pattern": re.compile(
            r"(?:ignore|disable|bypass|skip|suspend|waive)\s+"
            r"(?:all\s+)?(?:quality\s+)?(?:policies?|compliance|governance|controls?|checks?|gates?)",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["all"],
    },
    {
        "id": "POL-002",
        "category": "Policy Bypass",
        "description": "Attempt to self-authorize a governance exception",
        "pattern": re.compile(
            r"(?:self[- ]?authoriz|auto[- ]?approv|pre[- ]?approv|blanket\s+(?:exception|waiver|approval))",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["work"],
    },
    # ── 9. CI pipeline integrity ──────────────────────────────────────────
    {
        "id": "CI-001",
        "category": "Pipeline Integrity",
        "description": "continue-on-error in workflow file could silently suppress security failures",
        "pattern": re.compile(
            r"continue-on-error:\s*true",
        ),
        "severity": "warning",
        "applies_to": ["workflows"],
    },
    {
        "id": "CI-002",
        "category": "Pipeline Integrity",
        "description": "Workflow job or step disabled with 'if: false'",
        "pattern": re.compile(
            r"if:\s*false\b",
        ),
        "severity": "error",
        "applies_to": ["workflows"],
    },
    {
        "id": "CI-003",
        "category": "Pipeline Integrity",
        "description": "Unquoted github.event context in run: block (shell injection vector)",
        "pattern": re.compile(
            r"\$\{\{\s*github\.event\.",
        ),
        "severity": "warning",
        "applies_to": ["workflows"],
    },
    {
        "id": "CI-004",
        "category": "Pipeline Integrity",
        "description": "Remote script fetch-and-execute pattern (curl|wget piped to shell)",
        "pattern": re.compile(
            r"(?:curl|wget)\s+.*\|\s*(?:sudo\s+)?(?:ba)?sh",
        ),
        "severity": "warning",
        "applies_to": ["workflows"],
    },
    {
        "id": "CI-005",
        "category": "Pipeline Integrity",
        "description": "Workflow removes or disables a validation/security step",
        "pattern": re.compile(
            r"#\s*(?:disabled|removed|skip|TODO:?\s*re-?enable)\s+.*(?:validat|secur|scan|lint|check)",
            re.IGNORECASE,
        ),
        "severity": "error",
        "applies_to": ["workflows"],
    },
    # ── 10. OPA/Rego policy integrity ─────────────────────────────────────
    {
        "id": "REGO-001",
        "category": "Policy-as-Code Integrity",
        "description": "Rego rule commented out or permanently disabled",
        "pattern": re.compile(
            r"#\s*deny\s+contains\s+msg\s+if",
        ),
        "severity": "error",
        "applies_to": ["rego"],
    },
]

# ── Inline suppression ────────────────────────────────────────────────────────
# Lines containing this marker are skipped (for legitimate references to
# injection patterns, e.g., in the agent-security policy itself or docs).
SUPPRESSION_MARKER = "content-security:allow"

# ── File categories ───────────────────────────────────────────────────────────


def categorize_file(path: Path, repo_root: Path) -> list[str]:
    """Return the categories a file belongs to, for pattern matching."""
    rel = str(path.relative_to(repo_root))
    categories: list[str] = ["all"]

    # Agent instructions (AGENT.md, DIVISION.md, AGENTS.md, agent type defs)
    if path.name in ("AGENTS.md", "CLAUDE.md"):
        categories.append("instructions")
        # AGENTS.md is the global file — not subject to "instructions_not_global"
    elif path.name == "AGENT.md" and "org/" in rel:
        categories.extend(["instructions", "instructions_not_global"])
    elif path.name == "DIVISION.md":
        categories.extend(["instructions", "instructions_not_global"])
    elif "org/agents/" in rel and path.suffix == ".md":
        categories.extend(["instructions", "instructions_not_global"])

    # Work artifacts
    if "work/" in rel and "_TEMPLATE" not in path.name:
        categories.append("work")

    # Templates
    if "_TEMPLATE" in path.name:
        categories.append("templates")

    # Scripts
    if path.suffix == ".py" and "scripts/" in rel:
        categories.append("scripts")

    # Quality policies
    if "4-quality/policies/" in rel:
        categories.append("instructions")

    # CI/CD workflow files
    if ".github/workflows/" in rel and path.suffix in (".yml", ".yaml"):
        categories.append("workflows")

    # OPA/Rego policy-as-code files
    if path.suffix == ".rego" and "policy/" in rel:
        categories.append("rego")

    return categories


# ── Scanner ───────────────────────────────────────────────────────────────────


def workflow_run_lines(lines: list[str]) -> set[int]:
    """Return 1-based line numbers that are part of workflow run commands."""
    run_lines: set[int] = set()
    in_run_block = False
    run_indent = 0

    for index, line in enumerate(lines, 1):
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if in_run_block and stripped and indent <= run_indent:
            in_run_block = False

        match = re.match(r"^(\s*)run:\s*(.*)$", line)
        if match:
            run_indent = len(match.group(1))
            remainder = match.group(2).strip()
            if remainder in {"|", "|-", ">", ">-"}:
                in_run_block = True
            elif remainder:
                run_lines.add(index)
            continue

        if in_run_block:
            run_lines.add(index)

    return run_lines


def scan_file(path: Path, repo_root: Path) -> list[dict]:
    """Scan a single file for content security issues. Returns findings."""
    findings: list[dict] = []
    rel = str(path.relative_to(repo_root))
    categories = categorize_file(path, repo_root)

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    lines = text.splitlines()
    run_scoped_lines = workflow_run_lines(lines) if "workflows" in categories else set()

    for pattern_def in PATTERNS:
        # Check if this pattern applies to any of the file's categories
        pattern_applies = any(
            cat in categories for cat in pattern_def["applies_to"]
        )
        if not pattern_applies:
            continue

        for i, line in enumerate(lines, 1):
            # Skip suppressed lines
            if SUPPRESSION_MARKER in line:
                continue

            # These workflow checks are only meaningful inside executable run blocks.
            if pattern_def["id"] in {"CI-003", "CI-004"}:
                if i not in run_scoped_lines:
                    continue
                if line.lstrip().startswith("#"):
                    continue

            match = pattern_def["pattern"].search(line)
            if match:
                findings.append({
                    "file": rel,
                    "line": i,
                    "pattern_id": pattern_def["id"],
                    "category": pattern_def["category"],
                    "severity": pattern_def["severity"],
                    "description": pattern_def["description"],
                    "matched_text": match.group(0)[:80],
                    "context": line.strip()[:120],
                })

    return findings


def get_scan_targets(root: Path) -> list[Path]:
    """Collect all governed files to scan."""
    targets: list[Path] = []

    # Markdown files in governed directories
    governed_dirs = [
        root / "org",
        root / "work",
        root / "process",
    ]
    for d in governed_dirs:
        if d.exists():
            targets.extend(
                p for p in d.rglob("*.md")
                if ".git" not in p.parts
                and "node_modules" not in p.parts
                and "archive" not in p.parts
            )

    # Top-level governed files
    for name in ("AGENTS.md", "CLAUDE.md", "COMPANY.md"):
        top_file = root / name
        if top_file.exists():
            targets.append(top_file)

    # Templates anywhere in the repo
    targets.extend(
        p for p in root.rglob("_TEMPLATE-*.md")
        if ".git" not in p.parts
        and "node_modules" not in p.parts
        and p not in targets
    )

    # CI/CD workflow files
    workflows_dir = root / ".github" / "workflows"
    if workflows_dir.exists():
        targets.extend(
            p for p in workflows_dir.iterdir()
            if p.suffix in (".yml", ".yaml")
        )

    # OPA/Rego policy-as-code files
    policy_dir = root / "policy"
    if policy_dir.exists():
        targets.extend(p for p in policy_dir.rglob("*.rego"))

    return sorted(set(targets))


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> int:
    verbose = "--verbose" in sys.argv

    # Support --root for alternate paths (e.g., examples/e2e-loop)
    root = REPO
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--root" and i < len(sys.argv) - 1:
            candidate = Path(sys.argv[i + 1])
            if not candidate.is_absolute():
                candidate = REPO / candidate
            if candidate.is_dir():
                root = candidate.resolve()
            else:
                print(f"ERROR: --root path does not exist: {candidate}")
                return 1

    targets = get_scan_targets(root)

    if not targets:
        print("WARNING: No governed files found to scan.")
        return 0

    all_findings: list[dict] = []
    scanned = 0

    for target in targets:
        findings = scan_file(target, root)
        scanned += 1
        if findings:
            all_findings.extend(findings)
        elif verbose:
            rel = str(target.relative_to(root))
            print(f"  ✓  {rel}")

    # ── Report ────────────────────────────────────────────────────────────
    errors = [f for f in all_findings if f["severity"] == "error"]
    warnings = [f for f in all_findings if f["severity"] == "warning"]

    if warnings:
        print(f"\n⚠  {len(warnings)} content security warning(s):")
        for w in warnings:
            print(f"  ⚠  [{w['pattern_id']}] {w['file']}:{w['line']} — {w['description']}")
            print(f"      Matched: {w['matched_text']}")
            if verbose:
                print(f"      Context: {w['context']}")

    if errors:
        print(f"\n✗  {len(errors)} content security error(s):")
        for e in errors:
            print(f"  ✗  [{e['pattern_id']}] {e['file']}:{e['line']} — {e['description']}")
            print(f"      Matched: {e['matched_text']}")
            if verbose:
                print(f"      Context: {e['context']}")

        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) in {scanned} files.")
        print(
            "\nTo suppress a legitimate reference (e.g., in documentation or policy),\n"
            "add '<!-- content-security:allow -->' to the flagged line.\n"
            "\nPolicy: org/4-quality/policies/agent-security.md §1 (Prompt Injection)\n"
            "OWASP: LLM01 (Prompt Injection), LLM02 (Insecure Output Handling)"
        )
        return 1

    print(f"\nContent security validation passed ({scanned} files scanned, {len(warnings)} warnings).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
