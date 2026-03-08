#!/usr/bin/env python3
"""approval_queue.py — Build a concise human approval prompt.

Purpose
- Provide a single place that turns "pending approvals" into a short message.
- Avoid spamming: compare a hash of the queue to work/ops/heartbeat-state.json.

Queue sources (minimal):
- Proposed missions: work/missions/<slug>/BRIEF.md with **Status:** proposed
- Open PRs in this repo (best-effort via `gh pr list`)
- PRs with **CHANGES_REQUESTED** (require explicit approval unless the requester is the human owner; see `scripts/pr_review_dispatch.py`)

Usage:
  python3 scripts/approval_queue.py
  python3 scripts/approval_queue.py --json
  python3 scripts/approval_queue.py --emit-if-changed

Exit codes:
  0: nothing to ask / no change
  2: prompt should be emitted (changed + non-empty)
  1: error
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
import re

from work_backend import gh_json, load_work_backend, prefixed_label

REPO_ROOT = Path(__file__).parent.parent
MISSIONS_DIR = REPO_ROOT / "work" / "missions"
STATE_FILE = REPO_ROOT / "work" / "ops" / "heartbeat-state.json"
WORK_BACKEND = load_work_backend(REPO_ROOT)

RE_STATUS = re.compile(r"\*\*Status:\*\*\s*([^\n|]+)", re.IGNORECASE)


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def proposed_missions() -> list[dict]:
    out: list[dict] = []
    for brief in MISSIONS_DIR.glob("*/BRIEF.md"):
        text = _read_text(brief)
        m = RE_STATUS.search(text)
        if m and m.group(1).strip().lower() == "proposed":
            slug = brief.parent.name
            out.append({
                "slug": slug,
                "path": f"work/missions/{slug}/BRIEF.md",
            })
    return sorted(out, key=lambda x: x["slug"])


def open_prs_best_effort() -> list[dict]:
    # Best effort: if gh isn't configured, just return empty.
    cmd = [
        "gh",
        "pr",
        "list",
        "--limit",
        "20",
        "--json",
        "number,title,isDraft,url,author,updatedAt,reviewDecision",
    ]
    try:
        r = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return []

    if r.returncode != 0:
        return []

    try:
        items = json.loads(r.stdout or "[]")
    except json.JSONDecodeError:
        return []

    out = []
    for pr in items:
        out.append({
            "number": pr.get("number"),
            "title": pr.get("title"),
            "url": pr.get("url"),
            "isDraft": bool(pr.get("isDraft")),
            "reviewDecision": pr.get("reviewDecision"),
        })
    return out


def compute_hash(payload: dict) -> str:
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:12]


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(_read_text(STATE_FILE))
    except Exception:
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build() -> dict:
    if WORK_BACKEND.uses_issues_for("mission") or WORK_BACKEND.uses_issues_for("release") or WORK_BACKEND.uses_issues_for("signal"):
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
                    "--json",
                    "number,title,url,labels",
                ],
                repo=repo,
                cwd=REPO_ROOT,
            )
        except RuntimeError:
            issues = []

        signal_triage = []
        mission_approvals = []
        release_approvals = []
        for issue in issues:
            artifact = prefixed_label(issue, "artifact:")
            status = prefixed_label(issue, "status:")
            if artifact == "artifact:signal" and status == "status:new":
                signal_triage.append(issue)
            if artifact == "artifact:mission" and status == "status:proposed":
                mission_approvals.append(issue)
            if artifact == "artifact:release" and status == "status:draft":
                release_approvals.append(issue)

        return {
            "signal_triage": signal_triage,
            "proposed_missions": mission_approvals,
            "release_approvals": release_approvals,
            "open_prs": open_prs_best_effort(),
        }

    return {
        "proposed_missions": proposed_missions(),
        "open_prs": open_prs_best_effort(),
    }


def render(queue: dict) -> str:
    lines = []

    st = queue.get("signal_triage") or []
    pm = queue.get("proposed_missions") or []
    ra = queue.get("release_approvals") or []
    prs = queue.get("open_prs") or []

    if st:
        lines.append("Signals (status:new → need triage label change):")
        for issue in st:
            lines.append(f"- #{issue['number']} — {issue['title']}")
            if issue.get("url"):
                lines.append(f"  {issue['url']}")

    if pm:
        if lines:
            lines.append("")
        lines.append("Missions (proposed → need your approval):")
        for m in pm:
            if "slug" in m:
                lines.append(f"- {m['slug']}  ({m['path']})")
            else:
                lines.append(f"- #{m['number']} — {m['title']}")
                if m.get("url"):
                    lines.append(f"  {m['url']}")

    if ra:
        if lines:
            lines.append("")
        lines.append("Releases (draft → need go/no-go approval):")
        for issue in ra:
            lines.append(f"- #{issue['number']} — {issue['title']}")
            if issue.get("url"):
                lines.append(f"  {issue['url']}")

    if prs:
        # split: changes requested first
        changes = [p for p in prs if (p.get("reviewDecision") or "").upper() == "CHANGES_REQUESTED" and not p.get("isDraft")]
        rest = [p for p in prs if p not in changes]

        if changes:
            if lines:
                lines.append("")
            lines.append("PRs with CHANGES_REQUESTED (needs fix; explicit approval unless you requested it):")
            for pr in changes:
                lines.append(f"- #{pr['number']} — {pr['title']}")
                if pr.get("url"):
                    lines.append(f"  {pr['url']}")

        if rest:
            if lines:
                lines.append("")
            lines.append("Open PRs (pick any to review/approve/merge):")
            for pr in rest:
                draft = " [DRAFT]" if pr.get("isDraft") else ""
                lines.append(f"- #{pr['number']}{draft} — {pr['title']}")
                if pr.get("url"):
                    lines.append(f"  {pr['url']}")

    if not lines:
        return ""

    lines.append("")
    lines.append("Reply with what you want to approve, e.g.:\n- approve mission <slug>\n- review PR #<n>\n- merge PR #<n>")
    return "\n".join(lines)


def main() -> int:
    emit_if_changed = "--emit-if-changed" in sys.argv
    as_json = "--json" in sys.argv

    queue = build()
    non_empty = bool(queue.get("signal_triage") or queue.get("proposed_missions") or queue.get("release_approvals") or queue["open_prs"])

    h = compute_hash(queue)
    state = load_state()
    last_h = state.get("lastApprovalQueueHash")

    changed = (h != last_h)

    if emit_if_changed:
        if non_empty and changed:
            state["lastApprovalQueueHash"] = h
            save_state(state)
            print(render(queue))
            return 2
        return 0

    if as_json:
        print(json.dumps({"hash": h, "queue": queue}, indent=2, ensure_ascii=False))
    else:
        print(render(queue) or "")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
