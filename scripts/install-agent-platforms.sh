#!/usr/bin/env bash
set -euo pipefail

# Fetch the requested upstream agent platforms without vendoring their large
# applications into this repository. Each platform remains independently
# updateable and keeps its own license, dependencies, and runtime.
ROOT="${AGENCY_AGENTS_PLATFORM_DIR:-${HOME}/.local/share/agency-agents/platforms}"

usage() {
  cat <<'USAGE'
Usage: install-agent-platforms.sh [all|name ...]

Names:
  autogpt  dify  ruflo  anything-llm  copilotkit

Examples:
  ./scripts/install-agent-platforms.sh all
  ./scripts/install-agent-platforms.sh dify ruflo
USAGE
}

if (($# == 0)); then usage; exit 1; fi

declare -A URL=(
  [autogpt]=https://github.com/khanashraf6742-boop/AutoGPT.git
  [dify]=https://github.com/khanashraf6742-boop/dify.git
  [ruflo]=https://github.com/khanashraf6742-boop/ruflo.git
  [anything-llm]=https://github.com/khanashraf6742-boop/anything-llm.git
  [copilotkit]=https://github.com/khanashraf6742-boop/CopilotKit.git
)

names=("$@")
if [[ " ${names[*]} " == *" all "* ]]; then
  names=(autogpt dify ruflo anything-llm copilotkit)
fi

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }
mkdir -p "$ROOT"

for name in "${names[@]}"; do
  if [[ -z "${URL[$name]+x}" ]]; then
    echo "Unknown platform: $name" >&2
    usage
    exit 1
  fi
  destination="$ROOT/$name"
  if [[ -d "$destination/.git" ]]; then
    echo "Updating $name..."
    git -C "$destination" pull --ff-only
  elif [[ -e "$destination" ]]; then
    echo "Refusing to overwrite non-git directory: $destination" >&2
    exit 1
  else
    echo "Fetching $name..."
    git clone --depth 1 "${URL[$name]}" "$destination"
  fi
done

echo
echo "Platforms are available under: $ROOT"
echo "Read each platform's README for its own development and startup commands."
