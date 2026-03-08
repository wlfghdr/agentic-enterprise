#!/usr/bin/env bash
set -euo pipefail

# Archive closed/completed/consolidated work artifacts.
# Usage: ./scripts/archive_work.sh [--dry-run]
#
# What it does:
# 1. Moves closed/completed/consolidated missions to work/missions/archive/
# 2. Moves archived signals' triage records to work/signals/triage/archive/
# 3. Moves old reports (>30d) to work/reports/archive/
# 4. Archives run logs via archive_runs.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DRY_RUN=false
INCLUDE_LEGACY_WORK=false

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --include-legacy-work) INCLUDE_LEGACY_WORK=true ;;
  esac
done

WORK_BACKEND_TYPE=$(python3 scripts/work_backend.py type 2>/dev/null || echo "git-files")

moved=0

archive_item() {
  local src="$1"
  local dest_dir="$2"
  local bn
  bn=$(basename "$src")

  if [ "$DRY_RUN" = true ]; then
    echo "[DRY-RUN] $src → $dest_dir/$bn"
    return
  fi

  mkdir -p "$dest_dir"
  if git ls-files --error-unmatch "$src" >/dev/null 2>&1; then
    git mv "$src" "$dest_dir/$bn"
  else
    mv "$src" "$dest_dir/$bn"
  fi
  moved=$((moved + 1))
}

echo "=== Archiving closed/completed/consolidated missions ==="
if [ "$WORK_BACKEND_TYPE" = "github-issues" ] && [ "$INCLUDE_LEGACY_WORK" != true ]; then
  echo "Issue backend active — skipping automatic mission/signal file archiving for operational artifacts."
  echo "Use --include-legacy-work only for explicitly legacy file artifacts that still need cleanup."
else
  for d in work/missions/*/; do
    bn=$(basename "$d")
    [ "$bn" = "archive" ] && continue
    [ "$bn" = "_templates" ] && continue
    sf="$d/STATUS.md"
    [ -f "$sf" ] || continue
    if grep -qE 'status: (closed|completed|consolidated)' "$sf"; then
      archive_item "$d" "work/missions/archive"
    fi
  done
fi

echo "=== Archiving triage records for archived signals ==="
if [ "$WORK_BACKEND_TYPE" = "github-issues" ] && [ "$INCLUDE_LEGACY_WORK" != true ]; then
  echo "Issue backend active — signal archival is issue closure, not file movement."
else
  for f in work/signals/archive/*.md; do
    [ -f "$f" ] || continue
    bn=$(basename "$f" .md)
    slug=$(echo "$bn" | sed 's/^2026-[0-9]*-[0-9]*-//')
    for triage in "work/signals/triage/${slug}.md" "work/signals/triage/${bn}.md"; do
      if [ -f "$triage" ]; then
        archive_item "$triage" "work/signals/triage/archive"
      fi
    done
  done
fi

echo "=== Archiving old reports (>30 days) ==="
if [ -d work/reports/daily ]; then
  cutoff=$(date -d '30 days ago' +%Y-%m-%d 2>/dev/null || date -v-30d +%Y-%m-%d 2>/dev/null || echo "")
  if [ -n "$cutoff" ]; then
    for f in work/reports/daily/*.md; do
      [ -f "$f" ] || continue
      bn=$(basename "$f" .md)
      if [[ "$bn" < "$cutoff" ]]; then
        archive_item "$f" "work/reports/archive"
      fi
    done
  fi
fi

echo "=== Archiving run logs ==="
if [ -f scripts/archive_runs.sh ]; then
  if [ "$DRY_RUN" = true ]; then
    echo "[DRY-RUN] Would run scripts/archive_runs.sh"
  else
    bash scripts/archive_runs.sh
  fi
fi

if [ "$DRY_RUN" = true ]; then
  echo "=== DRY RUN complete — no changes made ==="
else
  echo "=== Archived $moved items ==="
fi
