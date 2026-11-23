#!/usr/bin/env bash
# install.sh — copy PEA skills into a Copilot skills directory.
#
# Usage:
#   bash install.sh [target-dir] [--research]
#
# Default target: ~/.copilot/skills (user-global).
# Pass a path to install into a project: bash install.sh ./my-repo/.copilot/skills
# Add --research to include the optional Probe skill.
set -e

SKILLS=(intent goal improve record learn)

SRC=$(cd "$(dirname "$0")" && pwd)
DST="$HOME/.copilot/skills"
RESEARCH=0
TARGET_SET=0

for arg in "$@"; do
  case "$arg" in
    --research)
      RESEARCH=1
      ;;
    *)
      if [ "$TARGET_SET" -eq 1 ]; then
        echo "ERROR: unexpected argument: $arg" >&2
        exit 2
      fi
      DST="$arg"
      TARGET_SET=1
      ;;
  esac
done

if [ "$RESEARCH" -eq 1 ]; then
  SKILLS+=(probe)
fi

for skill in "${SKILLS[@]}"; do
  if [ ! -f "$SRC/$skill/SKILL.md" ]; then
    echo "ERROR: missing required skill file: $SRC/$skill/SKILL.md. Installation not started." >&2
    exit 1
  fi
done

mkdir -p "$DST"

for skill in "${SKILLS[@]}"; do
  mkdir -p "$DST/$skill"
  cp "$SRC/$skill/SKILL.md" "$DST/$skill/SKILL.md"
  echo "  installed: $skill"
done

# The Trail skill was renamed Record in v5.0.0; remove a stale installed copy (only if it is that skill).
if grep -qx 'name: trail' "$DST/trail/SKILL.md" 2>/dev/null; then
  rm -rf "$DST/trail"
  echo "  removed: trail (renamed to record)"
fi

# The Orient skill was renamed Learn in v6.0.0; remove a stale installed copy (only if it is that skill).
if grep -qx 'name: orient' "$DST/orient/SKILL.md" 2>/dev/null; then
  rm -rf "$DST/orient"
  echo "  removed: orient (renamed to learn)"
fi

# The Destination skill was renamed Goal in v7.0.0; remove a stale installed copy (only if it is that skill).
if grep -qx 'name: destination' "$DST/destination/SKILL.md" 2>/dev/null; then
  rm -rf "$DST/destination"
  echo "  removed: destination (renamed to goal)"
fi

# Optional: PRINCIPLES.md alongside the skills folders
if [ -f "$SRC/PRINCIPLES.md" ]; then
  cp "$SRC/PRINCIPLES.md" "$DST/PRINCIPLES.md"
  echo "  installed: PRINCIPLES.md"
fi

echo ""
echo "Installed PEA skills to: $DST"
echo "Action: Run (/improve)"
echo "Automatic: intent before work; record afterward; goal and learning when evidence requires them"
if [ "$RESEARCH" -eq 1 ]; then
  echo "Research: /probe installed for ARF experiments"
else
  echo "Probe omitted. Re-run with --research only for ARF experiments"
fi
