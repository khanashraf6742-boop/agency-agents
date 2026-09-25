#!/usr/bin/env bash
set -euo pipefail

# Install xAI's Grok Build CLI without vendoring its upstream source into this repo.
# Usage: ./scripts/install-grok-build.sh [install-dir]
INSTALL_DIR="${1:-${HOME}/.local/bin}"
mkdir -p "$INSTALL_DIR"

if command -v grok >/dev/null 2>&1; then
  echo "grok is already installed at $(command -v grok)"
  grok --version || true
  exit 0
fi

if command -v curl >/dev/null 2>&1; then
  echo "Installing Grok Build from x.ai..."
  curl -fsSL https://x.ai/cli/install.sh | bash
elif command -v powershell.exe >/dev/null 2>&1; then
  powershell.exe -NoProfile -Command "irm https://x.ai/cli/install.ps1 | iex"
else
  echo "Neither curl nor PowerShell is available; see https://x.ai/cli" >&2
  exit 1
fi

echo
echo "Grok Build installation requested. Start a new shell, then run:"
echo "  grok"
