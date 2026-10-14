#!/usr/bin/env python3
"""Fail if Markdown files carry hand-maintained versions or changelogs.

Git history (and the generated release notes) is the change record. Files must
not contain **Version:** / **Template version:** / **Last updated:** /
**Revision:** header fields, `| **Version** | x.y |` rows, `## Changelog` /
`## Revision History` sections, or a `version:` key in Markdown frontmatter.
Fenced code blocks are ignored. Root CHANGELOG*.md files are exempt.

--keep-instance GLOB marks files whose *instance* fields are legitimate (for
example ISO controlled-document templates); there only template metadata is
rejected.

Usage: check_no_file_versioning.py [--keep-instance GLOB ...]
"""
import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

FIELDS_ALL = {"version", "template version", "last updated", "revision"}
FIELDS_TEMPLATE_ONLY = {"template version", "last updated"}
SECTIONS_ALL = {"changelog", "change log", "revision history", "version history"}
SECTIONS_TEMPLATE_ONLY = {"changelog", "change log"}

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FIELD = re.compile(r"\*\*([^*:]+):\*\*")
TABLE_ROW = re.compile(r"^\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]*)\|")
VERSIONISH = re.compile(r"^`?v?\d+(\.\d+){1,2}`?$")
PLACEHOLDER = re.compile(r"\{\{|YYYY|\[|<")


def strip_header_line(line, fields, keep_placeholders=False):
    """`> **Version:** 1.0 | **Last updated:** … | **Status:** x` → keep other fields."""
    body = line.rstrip("\n")
    m = re.match(r"^(\s*>\s*|\s*-\s+)?(.*)$", body)
    prefix, rest = m.group(1) or "", m.group(2)
    if not FIELD.search(rest):
        return line
    parts = re.split(r"\s+\|\s+", rest.strip())
    kept, dropped = [], False
    for part in parts:
        fm = re.match(r"^\*\*([^*:]+):\*\*", part.strip())
        if fm and fm.group(1).strip().lower() in fields:
            value = part.strip()[fm.end():].strip()
            if keep_placeholders and PLACEHOLDER.search(value):
                kept.append(part.strip())
                continue
            dropped = True
            continue
        kept.append(part.strip())
    if not dropped:
        return line
    if not kept or all(not k for k in kept):
        return None
    return prefix + " | ".join(kept) + "\n"


def clean(text, fields, sections, strip_frontmatter_version, keep_placeholders=False):
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    # YAML frontmatter
    if strip_frontmatter_version and lines and lines[0].strip() == "---":
        j = 1
        while j < len(lines) and lines[j].strip() != "---":
            j += 1
        if j < len(lines):
            fm = [l for l in lines[1:j] if not re.match(r"^version:\s*\S", l)]
            out.extend([lines[0], *fm, lines[j]])
            i = j + 1
    in_fence = False
    skip_level = None
    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            if skip_level is None:
                out.append(line)
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            if skip_level is None:
                out.append(line)
            i += 1
            continue
        h = HEADING.match(line)
        if h:
            level, title = len(h.group(1)), h.group(2).strip().lower()
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and level >= 2 and title in sections:
                skip_level = level
                # drop a horizontal rule + blank lines right before the section
                while out and out[-1].strip() == "":
                    out.pop()
                if out and out[-1].strip() in ("---", "***", "___"):
                    out.pop()
                    while out and out[-1].strip() == "":
                        out.pop()
                if out:
                    out.append("\n")
                i += 1
                continue
        if skip_level is not None:
            i += 1
            continue
        if "last updated" in fields and re.match(r"^\s*(#\s*)?Last updated:\s*\S", line):
            i += 1
            continue
        tm = TABLE_ROW.match(line)
        if tm and tm.group(1).strip().lower() in ("version", "template version") \
                and tm.group(1).strip().lower() in fields and VERSIONISH.match(tm.group(2).strip()):
            i += 1
            continue
        if FIELD.search(line) and re.match(r"^\s*(>\s*|-\s+)?\*\*[^*:]+:\*\*", line):
            new = strip_header_line(line, fields, keep_placeholders)
            if new is None:
                # drop the line; collapse a now-empty blockquote separator after it
                if i + 1 < len(lines) and lines[i + 1].strip() == ">":
                    i += 1
                i += 1
                continue
            line = new
        out.append(line)
        i += 1
    result = "".join(out)
    result = re.sub(r"\n{3,}", "\n\n", result)
    # a blockquote header that lost every line can leave "\n>\n" stubs
    result = re.sub(r"(?m)^>\s*\n(?=\n)", "", result)
    return result.rstrip("\n") + "\n" if result.strip() else result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep-instance", action="append", default=[])
    args = ap.parse_args()
    files = subprocess.run(["git", "ls-files", "*.md"], capture_output=True,
                           text=True, check=True).stdout.split()
    offenders = []
    for rel in files:
        if re.match(r"(?i)^CHANGELOG[^/]*\.md$", rel):
            continue
        keep = any(fnmatch.fnmatch(rel, g) for g in args.keep_instance)
        text = Path(rel).read_text(encoding="utf-8")
        cleaned = clean(text,
                        FIELDS_TEMPLATE_ONLY if keep else FIELDS_ALL,
                        SECTIONS_TEMPLATE_ONLY if keep else SECTIONS_ALL,
                        strip_frontmatter_version=not keep, keep_placeholders=keep)
        if cleaned != text:
            offenders.append(rel)
    if offenders:
        print("Hand-maintained versions/changelogs found (Git history is the record):")
        for rel in offenders:
            print(f"  ✗ {rel}")
        print("\nRemove version/date/revision fields and changelog sections; describe")
        print("the change in a Conventional Commit PR title instead.")
        return 1
    print(f"OK: {len(files)} Markdown files without per-file versioning")
    return 0


if __name__ == "__main__":
    sys.exit(main())
