#!/usr/bin/env python3
"""
find_pending_work.py — Report actionable work items for all agents.

Prints a machine- and human-readable summary of:
  1. Untriaged signals (no triage record)
  2. Proceed signals without mission briefs
  3. Approved missions without TASKS.md (needs orchestration)
  4. Proposed missions awaiting human approval (steering gate)
  5. Active missions with open tasks (needs execution)
  6. Missions completed (all tasks done, not yet closed)

Usage:
    python3 scripts/find_pending_work.py [--json]

Exit code:
  0 — no pending work
  2 — pending work exists (actionable items found)
  1 — error
"""

import sys
import re
import json
from pathlib import Path

from work_backend import (
    gh_json,
    get_project_statuses,
    issue_reference_from_body,
    load_work_backend,
    prefixed_label,
)

REPO_ROOT = Path(__file__).parent.parent
SIGNALS_DIR = REPO_ROOT / "work" / "signals"
TRIAGE_DIR = SIGNALS_DIR / "triage"
MISSIONS_DIR = REPO_ROOT / "work" / "missions"
WORK_BACKEND = load_work_backend(REPO_ROOT)

EXCLUDE_PREFIXES = ("_TEMPLATE", "_")
EXCLUDE_DIRS = {"triage", "digests"}

RE_STATUS = re.compile(r"\*\*Status:\*\*\s*([^\n|]+)", re.IGNORECASE)
RE_TASK_OPEN = re.compile(r"^- \[ \]", re.MULTILINE)
RE_TASK_DONE = re.compile(r"^- \[x\]", re.MULTILINE | re.IGNORECASE)


def slug_from_filename(filename: str) -> str:
    name = filename.replace(".md", "")
    parts = name.split("-", 3)
    if len(parts) >= 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        return parts[3]
    return name


RE_DATED_SIGNAL = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")


def find_untriaged_signals() -> list[str]:
    untriaged = []
    for f in SIGNALS_DIR.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        if not RE_DATED_SIGNAL.match(f.name):
            continue  # skip README, templates, etc.
        slug = slug_from_filename(f.name)
        if not (TRIAGE_DIR / f"{slug}.md").exists():
            untriaged.append(slug)
    return untriaged


RE_OUTCOME_PROCEED = re.compile(r"\*\*Outcome:\*\*\s*proceed\s*$", re.MULTILINE)


def issue_backend_report() -> dict:
    repo = WORK_BACKEND.configured_issue_repo()
    missions = {}
    tasks_by_mission: dict[int, dict[str, int]] = {}
    report = {
        "untriaged_signals": [],
        "proceed_without_brief": [],
        "proposed_missions": [],
        "approved_without_tasks": [],
        "active_with_open_tasks": [],
        "completed_missions": [],
    }

    try:
        issues = gh_json(
            [
                "issue",
                "list",
                "--state",
                "all",
                "--limit",
                "300",
                "--json",
                "number,title,url,state,labels,body",
            ],
            repo=repo,
            cwd=REPO_ROOT,
        )
    except RuntimeError as exc:
        report["backend_error"] = str(exc)
        return report

    # Fetch project statuses for all issues in one batch
    all_numbers = [i["number"] for i in issues]
    try:
        project_statuses = get_project_statuses(WORK_BACKEND, all_numbers)
    except RuntimeError:
        project_statuses = {}

    for issue in issues:
        artifact = prefixed_label(issue, "artifact:")
        status = project_statuses.get(issue["number"])

        if artifact == "artifact:signal" and issue.get("state") == "OPEN":
            if status in (None, "Backlog", "Triage"):
                report["untriaged_signals"].append(issue)
            if status == "Approved":
                report["proceed_without_brief"].append(issue)

        if artifact == "artifact:mission" and issue.get("state") == "OPEN":
            missions[issue["number"]] = issue
            if status == "Backlog":
                report["proposed_missions"].append(issue)

        if artifact == "artifact:task":
            parent_issue = issue_reference_from_body(issue.get("body", ""), "Parent Mission", "Mission")
            if not parent_issue:
                continue
            task_state = tasks_by_mission.setdefault(parent_issue, {"open": 0, "done": 0})
            if issue.get("state") == "OPEN" and status in {"Backlog", "In Progress", "Blocked"}:
                task_state["open"] += 1
            if status == "Done" or issue.get("state") == "CLOSED":
                task_state["done"] += 1

    for number, mission in missions.items():
        counts = tasks_by_mission.get(number, {"open": 0, "done": 0})
        status = project_statuses.get(number)
        if status in {"Approved", "Planning"} and counts["done"] == 0 and counts["open"] == 0:
            report["approved_without_tasks"].append(mission)
        if status == "In Progress" and counts["open"] > 0:
            report["active_with_open_tasks"].append({
                "number": number,
                "title": mission["title"],
                "url": mission["url"],
                "open": counts["open"],
                "done": counts["done"],
            })
        if status == "In Progress" and counts["open"] == 0 and counts["done"] > 0:
            report["completed_missions"].append(mission)

    return report


def find_proceed_without_brief() -> list[str]:
    if not TRIAGE_DIR.exists():
        return []
    result = []
    for f in TRIAGE_DIR.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        if f.name.startswith(tuple(EXCLUDE_PREFIXES)):
            continue
        text = f.read_text(encoding="utf-8")
        if RE_OUTCOME_PROCEED.search(text):
            slug = f.stem
            if not (MISSIONS_DIR / slug / "BRIEF.md").exists():
                result.append(slug)
    return result


def find_proposed_missions() -> list[str]:
    result = []
    for brief in MISSIONS_DIR.glob("*/BRIEF.md"):
        text = brief.read_text(encoding="utf-8")
        m = RE_STATUS.search(text)
        if m and m.group(1).strip().lower() == "proposed":
            result.append(brief.parent.name)
    return sorted(result)


def find_approved_without_tasks() -> list[str]:
    result = []
    for brief in MISSIONS_DIR.glob("*/BRIEF.md"):
        text = brief.read_text(encoding="utf-8")
        m = RE_STATUS.search(text)
        if m and m.group(1).strip().lower() == "approved":
            tasks = brief.parent / "TASKS.md"
            if not tasks.exists():
                result.append(brief.parent.name)
    return result


def find_active_with_open_tasks() -> list[dict]:
    result = []
    for tasks_file in MISSIONS_DIR.glob("*/TASKS.md"):
        text = tasks_file.read_text(encoding="utf-8")
        open_count = len(RE_TASK_OPEN.findall(text))
        done_count = len(RE_TASK_DONE.findall(text))
        if open_count > 0:
            result.append({
                "slug": tasks_file.parent.name,
                "open": open_count,
                "done": done_count,
            })
    return result


def find_completed_missions() -> list[str]:
    result = []
    for tasks_file in MISSIONS_DIR.glob("*/TASKS.md"):
        text = tasks_file.read_text(encoding="utf-8")
        open_count = len(RE_TASK_OPEN.findall(text))
        done_count = len(RE_TASK_DONE.findall(text))
        if open_count == 0 and done_count > 0:
            brief = tasks_file.parent / "BRIEF.md"
            if brief.exists():
                brief_text = brief.read_text(encoding="utf-8")
                m = RE_STATUS.search(brief_text)
                if m and m.group(1).strip().lower() == "active":
                    result.append(tasks_file.parent.name)
    return result


def main():
    output_json = "--json" in sys.argv

    if WORK_BACKEND.uses_issues_for("signal") or WORK_BACKEND.uses_issues_for("mission") or WORK_BACKEND.uses_issues_for("task"):
        report = issue_backend_report()
        backend_error = report.get("backend_error")
        has_work = any(bool(report[key]) for key in (
            "untriaged_signals",
            "proceed_without_brief",
            "proposed_missions",
            "approved_without_tasks",
            "active_with_open_tasks",
            "completed_missions",
        ))
        if output_json:
            print(json.dumps(report, indent=2))
            if backend_error:
                return 1
        else:
            print("=== Pending Work Report ===\n")
            if backend_error:
                print(f"[ERROR] Unable to query GitHub Issues backend: {backend_error}")
                return 1
            if report["untriaged_signals"]:
                print(f"[STRATEGY] {len(report['untriaged_signals'])} signal issue(s) awaiting triage:")
                for issue in report["untriaged_signals"]:
                    print(f"  → review issue #{issue['number']}: {issue['title']}")
                    print(f"    {issue['url']}")
            if report["proceed_without_brief"]:
                print(f"\n[STRATEGY] {len(report['proceed_without_brief'])} signal issue(s) triaged to proceed and ready for mission creation:")
                for issue in report["proceed_without_brief"]:
                    print(f"  → create mission issue from signal #{issue['number']}: {issue['title']}")
                    print(f"    {issue['url']}")
            if report["proposed_missions"]:
                print(f"\n[STEERING] {len(report['proposed_missions'])} mission issue(s) awaiting approval:")
                for issue in report["proposed_missions"]:
                    print(f"  → approve mission #{issue['number']}: {issue['title']}")
                    print(f"    {issue['url']}")
            if report["approved_without_tasks"]:
                print(f"\n[ORCHESTRATION] {len(report['approved_without_tasks'])} approved/planning mission issue(s) need task decomposition:")
                for issue in report["approved_without_tasks"]:
                    print(f"  → create task issues under mission #{issue['number']}: {issue['title']}")
                    print(f"    {issue['url']}")
            if report["active_with_open_tasks"]:
                print(f"\n[EXECUTION] {len(report['active_with_open_tasks'])} active mission issue(s) have open tasks:")
                for mission in report["active_with_open_tasks"]:
                    print(f"  → mission #{mission['number']} ({mission['open']} open, {mission['done']} done): {mission['title']}")
                    print(f"    {mission['url']}")
            if report["completed_missions"]:
                print(f"\n[OPS] {len(report['completed_missions'])} mission issue(s) appear ready to close:")
                for issue in report["completed_missions"]:
                    print(f"  → close mission #{issue['number']} after final status note: {issue['title']}")
                    print(f"    {issue['url']}")
            if not has_work:
                print("Nothing pending. HEARTBEAT_OK.")
        return 2 if has_work else 0

    report = {
        "untriaged_signals": find_untriaged_signals(),
        "proceed_without_brief": find_proceed_without_brief(),
        "proposed_missions": find_proposed_missions(),
        "approved_without_tasks": find_approved_without_tasks(),
        "active_with_open_tasks": find_active_with_open_tasks(),
        "completed_missions": find_completed_missions(),
    }

    has_work = any(bool(v) for v in report.values())

    if output_json:
        print(json.dumps(report, indent=2))
    else:
        print("=== Pending Work Report ===\n")

        if report["untriaged_signals"]:
            print(f"[OPS] {len(report['untriaged_signals'])} untriaged signal(s):")
            for s in report["untriaged_signals"]:
                print(f"  → run: python3 scripts/triage_signals.py  (will process: {s})")

        if report["proceed_without_brief"]:
            print(f"\n[OPS] {len(report['proceed_without_brief'])} proceed signal(s) without mission brief:")
            for s in report["proceed_without_brief"]:
                print(f"  → draft mission brief from signal content (see HEARTBEAT.md Step 3): {s}")

        if report["proposed_missions"]:
            print(f"\n[STEERING] {len(report['proposed_missions'])} mission(s) awaiting human approval:")
            for s in report["proposed_missions"]:
                print(f"  → review: work/missions/{s}/BRIEF.md  (set **Status:** proposed → approved)")

        if report["approved_without_tasks"]:
            print(f"\n[ORCHESTRATION] {len(report['approved_without_tasks'])} approved mission(s) needing TASKS.md:")
            for s in report["approved_without_tasks"]:
                print(f"  → work/missions/{s}/BRIEF.md  (create TASKS.md from template)")

        if report["active_with_open_tasks"]:
            print(f"\n[EXECUTION] {len(report['active_with_open_tasks'])} mission(s) with open tasks:")
            for m in report["active_with_open_tasks"]:
                print(f"  → work/missions/{m['slug']}/TASKS.md  ({m['open']} open, {m['done']} done)")

        if report["completed_missions"]:
            print(f"\n[OPS] {len(report['completed_missions'])} mission(s) ready to close:")
            for s in report["completed_missions"]:
                print(f"  → update work/missions/{s}/BRIEF.md status: active → completed")

        if not has_work:
            print("Nothing pending. HEARTBEAT_OK.")

    return 2 if has_work else 0


if __name__ == "__main__":
    sys.exit(main())
