#!/usr/bin/env python3
"""Advisory governance check for GitHub-hosted repos.

This check is intentionally *warning-only* by default.

It verifies:
- CODEOWNERS exists
- Default branch protection appears enabled (if the token has permission to read it)

It is best-effort because GitHub Actions tokens often lack permission to read
branch protection settings in some org configurations.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path


def api_get(url: str, token: str) -> tuple[int, dict | str]:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read().decode("utf-8", errors="replace")
            try:
                return resp.status, json.loads(data)
            except Exception:
                return resp.status, data
    except Exception as e:
        # urllib raises for non-2xx; try to extract status code if present
        status = getattr(getattr(e, "fp", None), "status", None)
        if status is None:
            return 0, str(e)
        try:
            body = e.fp.read().decode("utf-8", errors="replace")
            return int(status), body
        except Exception:
            return int(status), str(e)


def warn(msg: str) -> None:
    print(f"::warning::{msg}")


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()  # owner/name
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    default_branch = os.environ.get("GITHUB_DEFAULT_BRANCH", "main").strip() or "main"

    # 1) CODEOWNERS existence
    if not Path("CODEOWNERS").exists():
        warn("CODEOWNERS file is missing at repo root. Governance via CODEOWNERS cannot be enforced.")

    # 2) Branch protection (best-effort)
    if not repo:
        warn("GITHUB_REPOSITORY not set; skipping branch protection check.")
        return 0

    if not token:
        warn("GITHUB_TOKEN not set; skipping branch protection check.")
        return 0

    url = f"https://api.github.com/repos/{repo}/branches/{default_branch}/protection"
    status, payload = api_get(url, token)

    if status == 200:
        # Protection exists.
        return 0

    if status in (403, 404):
        # 404 can mean "not protected" or "not accessible" depending on permissions.
        warn(
            f"Unable to confirm branch protection for '{default_branch}' (HTTP {status}). "
            "Ensure branch protection + require CODEOWNERS review + required status checks are enabled. "
            "See docs/REQUIRED-GITHUB-SETTINGS.md"
        )
        return 0

    # Any other unexpected condition
    warn(
        f"Branch protection check returned unexpected status (HTTP {status}). "
        "Please verify branch protection manually."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
