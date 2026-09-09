#!/usr/bin/env bash
# Install the PEA hook at Git's effective hook location.
# Run from the target repo root.
set -e

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "Not inside a git repo."
  exit 1
}

HOOKS_SRC=$(cd "$(dirname "$0")/hooks" && pwd)
HOOK_TARGET=$(git rev-parse --path-format=absolute --git-path hooks/pre-commit)

if [ -e "$HOOK_TARGET" ] || [ -L "$HOOK_TARGET" ]; then
  if ! cmp -s "$HOOKS_SRC/pre-commit" "$HOOK_TARGET"; then
    echo "ERROR: existing hook differs: $HOOK_TARGET. Review and integrate it manually; nothing was overwritten." >&2
    exit 1
  fi
else
  mkdir -p "$(dirname "$HOOK_TARGET")"
  cp "$HOOKS_SRC/pre-commit" "$HOOK_TARGET"
fi
chmod +x "$HOOK_TARGET"

echo "Installed pre-commit hook to $HOOK_TARGET"
