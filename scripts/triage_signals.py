#!/usr/bin/env python3
"""
triage_signals.py — Signal Triage Script (agentic-enterprise)

Scans work/signals/*.md for untriaged signals, decides disposition,
and writes triage records to work/signals/triage/<slug>.md.

Idempotent: safe to run multiple times. Already-triaged signals are skipped.

Disposition rules:
  immediate + any impact     → proceed  (mission brief)
  next-cycle + high impact   → proceed  (mission brief)
  next-cycle + medium/low    → defer    (add to digest queue)
  monitor + any              → monitor  (add to digest queue)

Exit codes:
  0 — success (may have done nothing)
  1 — error
"""

import os
import re
import sys
import json
import subprocess
import datetime
from pathlib import Path

from work_backend import gh_json, label_names, load_work_backend, prefixed_label, strip_prefix

REPO_ROOT = Path(__file__).parent.parent
SIGNALS_DIR = REPO_ROOT / "work" / "signals"
TRIAGE_DIR = SIGNALS_DIR / "triage"
MISSIONS_DIR = REPO_ROOT / "work" / "missions"
DIGEST_QUEUE = SIGNALS_DIR / "digests" / "_queue.json"
WORK_BACKEND = load_work_backend(REPO_ROOT)

# Exclude patterns
EXCLUDE_PREFIXES = ("_TEMPLATE", "_")
EXCLUDE_DIRS = {"triage", "digests"}

# Regex patterns for extracting signal fields
RE_URGENCY = re.compile(r"\*\*Urgency:\*\*\s*(immediate|next-cycle|monitor)", re.IGNORECASE)
RE_IMPACT  = re.compile(r"\*\*Potential impact:\*\*\s*(high|medium|low)", re.IGNORECASE)
RE_CATEGORY = re.compile(r"\*\*Category:\*\*\s*([^\n|]+)", re.IGNORECASE)
RE_TITLE = re.compile(r"^#\s+Signal[:\s—-]+(.+)$", re.MULTILINE)


def handle_issue_backend(apply_issue_labels: bool) -> int:
    repo = WORK_BACKEND.configured_issue_repo()
    try:
        issues = gh_json(
            [
                "issue",
                "list",
                "--state",
                "open",
                "--limit",
                "200",
                "--label",
                "artifact:signal",
                "--json",
                "number,title,url,labels,body",
            ],
            repo=repo,
            cwd=REPO_ROOT,
        )
    except RuntimeError as exc:
        print(f"ERROR: unable to query GitHub Issues backend: {exc}", file=sys.stderr)
        return 1

    pending = []
    for issue in issues:
        if prefixed_label(issue, "status:") != "status:new":
            continue
        urgency = strip_prefix(prefixed_label(issue, "urgency:"), "urgency:")
        signal = {
            "slug": f"issue-{issue['number']}",
            "title": issue["title"],
            "urgency": urgency,
            "impact": None,
            "category": strip_prefix(prefixed_label(issue, "category:"), "category:") or "unknown",
            "number": issue["number"],
            "url": issue["url"],
        }
        disposition = decide_disposition(signal)
        pending.append((issue, disposition))

    if not pending:
        print("No GitHub signal issues awaiting triage.")
        return 0

    changed = 0
    for issue, disposition in pending:
        recommendation = f"#{issue['number']} → recommend status:{disposition} ({issue['title']})"
        if apply_issue_labels:
            subprocess.run(
                [
                    "gh",
                    "issue",
                    "edit",
                    str(issue["number"]),
                    "--remove-label",
                    "status:new",
                    "--add-label",
                    f"status:{disposition}",
                    *( ["--repo", repo] if repo else [] ),
                ],
                cwd=str(REPO_ROOT),
                check=False,
                capture_output=True,
                text=True,
            )
            changed += 1
            print(f"  [APPLIED] {recommendation}")
        else:
            print(f"  [REVIEW] {recommendation}")
            print(f"           {issue['url']}")

    print("\n=== Issue Triage Summary ===")
    print(f"  open status:new signals : {len(pending)}")
    print(f"  label changes applied   : {changed}")
    if not apply_issue_labels:
        print("  human approval remains required; rerun with --apply-issue-labels only if explicitly desired")
    return 0


def slug_from_filename(filename: str) -> str:
    """Extract slug from signal filename: YYYY-MM-DD-<slug>.md → <slug>"""
    name = filename.replace(".md", "")
    # Remove leading date if present (YYYY-MM-DD-)
    parts = name.split("-", 3)
    if len(parts) >= 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        return parts[3]
    return name


def parse_signal(path: Path) -> dict:
    """Parse a signal file and return its metadata."""
    text = path.read_text(encoding="utf-8")
    urgency_m = RE_URGENCY.search(text)
    impact_m  = RE_IMPACT.search(text)
    category_m = RE_CATEGORY.search(text)
    title_m   = RE_TITLE.search(text)

    return {
        "filename": path.name,
        "slug": slug_from_filename(path.name),
        "title": title_m.group(1).strip() if title_m else path.stem,
        "urgency": urgency_m.group(1).lower() if urgency_m else None,
        "impact": impact_m.group(1).lower() if impact_m else None,
        "category": category_m.group(1).strip() if category_m else "unknown",
    }


def decide_disposition(signal: dict) -> str:
    """Return disposition string based on urgency + impact."""
    urgency = signal.get("urgency")
    impact  = signal.get("impact")

    if urgency == "immediate":
        return "proceed"
    if urgency == "next-cycle" and impact == "high":
        return "proceed"
    if urgency == "next-cycle" and impact in ("medium", "low"):
        return "defer"
    if urgency == "monitor":
        return "monitor"
    # Fallback: monitor if fields are missing
    return "monitor"


def write_triage_record(signal: dict, disposition: str, today: str) -> Path:
    """Write work/signals/triage/<slug>.md and return its path."""
    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    record_path = TRIAGE_DIR / f"{signal['slug']}.md"

    mission_line = ""
    slug = signal["slug"]
    if disposition == "proceed":
        mission_line = f"\n- **Mission slug:** `{slug}`\n- **Mission path:** `work/missions/{slug}/BRIEF.md`"

    proceed_action = f"→ Draft mission brief: `work/missions/{slug}/BRIEF.md` (see HEARTBEAT.md Step 3)"
    defer_action = "→ Add to digest queue for weekly summary."
    proceed_steps = (
        f"- [ ] Ops: draft `work/missions/{slug}/BRIEF.md` from signal content (HEARTBEAT.md Step 3)\n"
        f"- [ ] Human: review and approve mission brief"
    )
    defer_steps = "- [ ] Ops: include in next `work/signals/digests/YYYY-WXX.md`"

    content = f"""# Triage Record: {signal['title']}

> **Created:** {today}
> **Signal:** `work/signals/{signal['filename']}`

## Triage Outcome

- **Outcome:** {disposition}
- **Urgency:** {signal.get('urgency', 'unknown')}
- **Potential impact:** {signal.get('impact', 'unknown')}
- **Category:** {signal.get('category', 'unknown')}{mission_line}

## Decision Rationale

Automatically triaged by `scripts/triage_signals.py` using disposition rules from `docs/ARTIFACT-FLOW.md`.

{proceed_action if disposition == "proceed" else defer_action}

## Next Steps

{proceed_steps if disposition == "proceed" else defer_steps}
"""
    record_path.write_text(content, encoding="utf-8")
    return record_path


def mission_brief_exists(slug: str) -> bool:
    """Check if a mission brief already exists for this slug."""
    return (MISSIONS_DIR / slug / "BRIEF.md").exists()


def update_digest_queue(signal: dict, disposition: str, today: str):
    """Append signal to the digest queue JSON."""
    queue = []
    if DIGEST_QUEUE.exists():
        try:
            queue = json.loads(DIGEST_QUEUE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            queue = []

    # Avoid duplicates in queue
    existing_slugs = {entry["slug"] for entry in queue}
    if signal["slug"] not in existing_slugs:
        queue.append({
            "slug": signal["slug"],
            "filename": signal["filename"],
            "title": signal["title"],
            "category": signal["category"],
            "urgency": signal.get("urgency"),
            "impact": signal.get("impact"),
            "disposition": disposition,
            "queued_at": today,
        })
        DIGEST_QUEUE.parent.mkdir(parents=True, exist_ok=True)
        DIGEST_QUEUE.write_text(json.dumps(queue, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    apply_issue_labels = "--apply-issue-labels" in sys.argv
    if WORK_BACKEND.uses_issues_for("signal"):
        return handle_issue_backend(apply_issue_labels)

    today = datetime.date.today().isoformat()
    results = {"proceed": [], "defer": [], "monitor": [], "skipped": [], "errors": []}

    # Collect signal files (only dated: YYYY-MM-DD-<slug>.md)
    dated_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    signal_files = [
        f for f in SIGNALS_DIR.iterdir()
        if f.is_file()
        and f.suffix == ".md"
        and dated_pattern.match(f.name)
    ]

    if not signal_files:
        print("No signal files found.")
        return 0

    for sig_path in sorted(signal_files):
        slug = slug_from_filename(sig_path.name)
        triage_record = TRIAGE_DIR / f"{slug}.md"

        # Idempotency check: skip if already triaged
        if triage_record.exists():
            results["skipped"].append(slug)
            continue

        try:
            signal = parse_signal(sig_path)
            disposition = decide_disposition(signal)

            # Write triage record (idempotency lock)
            write_triage_record(signal, disposition, today)

            if disposition == "proceed":
                results["proceed"].append(slug)
                if not mission_brief_exists(slug):
                    print(f"  [PROCEED] {slug} → needs mission brief at work/missions/{slug}/BRIEF.md")
                else:
                    print(f"  [PROCEED] {slug} → mission brief already exists, skipping creation")
            else:
                results[disposition].append(slug)
                update_digest_queue(signal, disposition, today)
                print(f"  [{disposition.upper()}] {slug} → added to digest queue")

        except Exception as e:
            results["errors"].append(slug)
            print(f"  [ERROR] {slug}: {e}", file=sys.stderr)

    # Summary
    print("\n=== Triage Summary ===")
    print(f"  proceed : {len(results['proceed'])} signals → need mission briefs")
    print(f"  defer   : {len(results['defer'])} signals → queued for digest")
    print(f"  monitor : {len(results['monitor'])} signals → queued for digest")
    print(f"  skipped : {len(results['skipped'])} (already triaged)")
    print(f"  errors  : {len(results['errors'])}")

    if results["proceed"]:
        print("\n[ACTION REQUIRED] Create mission briefs for:")
        for slug in results["proceed"]:
            if not mission_brief_exists(slug):
                print(f"  work/missions/{slug}/BRIEF.md")

    return 1 if results["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
