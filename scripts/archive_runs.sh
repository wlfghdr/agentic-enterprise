#!/usr/bin/env bash
set -euo pipefail

# Archives work/runs/*.md into work/runs-archive/YYYY-MM/.
# Works for both tracked and untracked files.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -d work/runs ]; then
  echo "No work/runs directory."
  exit 0
fi

shopt -s nullglob
files=(work/runs/*.md)
if [ ${#files[@]} -eq 0 ]; then
  echo "No run markdown files to archive."
  exit 0
fi

month=$(date +%Y-%m)
dest="work/runs-archive/${month}"
mkdir -p "$dest"

moved=0
for f in "${files[@]}"; do
  bn=$(basename "$f")
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
    git mv "$f" "$dest/$bn"
  else
    mv "$f" "$dest/$bn"
  fi
  moved=$((moved+1))
done

echo "Archived ${moved} files to $dest"
