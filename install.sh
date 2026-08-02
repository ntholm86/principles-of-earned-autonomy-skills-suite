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

SKILLS=(intent destination improve trail orient)

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

mkdir -p "$DST"

for skill in "${SKILLS[@]}"; do
  if [ -f "$SRC/$skill/SKILL.md" ]; then
    mkdir -p "$DST/$skill"
    cp "$SRC/$skill/SKILL.md" "$DST/$skill/SKILL.md"
    echo "  installed: $skill"
  else
    echo "  skipped:   $skill (no SKILL.md found)"
  fi
done

# Optional: PRINCIPLES.md alongside the skills folders
if [ -f "$SRC/PRINCIPLES.md" ]; then
  cp "$SRC/PRINCIPLES.md" "$DST/PRINCIPLES.md"
  echo "  installed: PRINCIPLES.md"
fi

echo ""
echo "Installed PEA skills to: $DST"
echo "Actions: Destination (/destination); Run (/improve)"
echo "Automatic: intent before work; trail afterward; orientation when evidence makes it stale"
if [ "$RESEARCH" -eq 1 ]; then
  echo "Research: /probe installed for ARF experiments"
else
  echo "Probe omitted. Re-run with --research only for ARF experiments"
fi
