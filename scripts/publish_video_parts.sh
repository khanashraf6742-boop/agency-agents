#!/usr/bin/env bash
#
# publish_video_parts.sh — make a large video downloadable from GitHub.
#
# GitHub rejects any single file over 100 MB, and in a sandbox the release-asset
# upload endpoint (uploads.github.com) may be unreachable. This script publishes
# a video through the one route that always works: plain files in the repo,
# stored as sub-40 MB parts, with a README telling the viewer how to rejoin them.
#
# Usage:
#   ./scripts/publish_video_parts.sh VIDEO SLUG [options]
#
#   VIDEO   path to the finished .mp4
#   SLUG    coverage name, e.g. "batch2-rules-11-30" (becomes the folder name)
#
# Options:
#   --part-size BYTES     bytes per part (default 38000000 = 38 MB)
#   --crf N               x264 CRF for the compact copy (default 28; high CRF = smaller)
#   --audio-bitrate B     AAC bitrate for the compact copy (default 72k)
#   --no-encode           publish VIDEO as-is, do not make a compact copy
#   --force-encode        always make a compact copy, even under the size limit
#   --dir PATH            output folder (default download_parts/SLUG)
#   --title TEXT          human title used in the generated README
#   --branch NAME         branch to push to (default: current branch)
#   --no-push             commit but do not push
#   --local-only          do everything except any git operation (safe rehearsal)
#   --dry-run             print what would happen, change nothing
#   -h, --help            this text
#
# Examples:
#   ./scripts/publish_video_parts.sh pension_b2_hinglish_FULL.mp4 batch2-rules-11-30
#   ./scripts/publish_video_parts.sh out/part3.mp4 batch2-rules-31-45 --crf 30 --no-push
#
set -euo pipefail

die() { printf 'error: %s\n' "$*" >&2; exit 1; }
note() { printf '\n\033[1m== %s\033[0m\n' "$*"; }
info() { printf '   %s\n' "$*"; }

VIDEO=""
SLUG=""
PART_SIZE=38000000
CRF=28
ABR=72k
ENCODE=1
OUT_DIR=""
FORCE_ENCODE=0
TITLE=""
BRANCH=""
PUSH=1
LOCAL_ONLY=0
DRY_RUN=0

while [ $# -gt 0 ]; do
  case "$1" in
    --part-size)   PART_SIZE="$2"; shift 2 ;;
    --crf)         CRF="$2"; shift 2 ;;
    --audio-bitrate) ABR="$2"; shift 2 ;;
    --no-encode)   ENCODE=0; shift ;;
    --force-encode) FORCE_ENCODE=1; shift ;;
    --dir)         OUT_DIR="$2"; shift 2 ;;
    --title)       TITLE="$2"; shift 2 ;;
    --branch)      BRANCH="$2"; shift 2 ;;
    --no-push)     PUSH=0; shift ;;
    --local-only)  LOCAL_ONLY=1; PUSH=0; shift ;;
    --dry-run)     DRY_RUN=1; LOCAL_ONLY=1; PUSH=0; shift ;;
    -h|--help)     sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*)            die "unknown option: $1" ;;
    *)             if [ -z "$VIDEO" ]; then VIDEO="$1"; elif [ -z "$SLUG" ]; then SLUG="$1"; else die "unexpected argument: $1"; fi; shift ;;
  esac
done

[ -n "$VIDEO" ] && [ -n "$SLUG" ] || die "usage: $0 VIDEO SLUG [options]  (see --help)"
[ -f "$VIDEO" ] || die "no such file: $VIDEO"

# --- locate tooling -----------------------------------------------------------
# Order: $FFMPEG env var, system ffmpeg, a venv python with imageio-ffmpeg,
# then a direct search of imageio-ffmpeg's bundled binary. The bundled static
# build is what saves you when the sandbox has no ffmpeg at all.
find_ffmpeg() {
  if [ -n "${FFMPEG:-}" ] && [ -x "${FFMPEG}" ]; then printf '%s\n' "$FFMPEG"; return; fi
  if command -v ffmpeg >/dev/null 2>&1; then command -v ffmpeg; return; fi
  local py
  for py in "$(command -v python3 || true)" "$(command -v python || true)" \
            "${VIRTUAL_ENV:-}/bin/python" "./.venv/bin/python" \
            /home/*/work/.venv/bin/python; do
    [ -n "$py" ] && [ -x "$py" ] || continue
    local found
    found="$("$py" -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())' 2>/dev/null || true)"
    if [ -n "$found" ] && [ -x "$found" ]; then printf '%s\n' "$found"; return; fi
  done
  local bundled
  bundled="$(ls -1 /home/*/work/.venv/lib/python*/site-packages/imageio_ffmpeg/binaries/ffmpeg-* \
                ./.venv/lib/python*/site-packages/imageio_ffmpeg/binaries/ffmpeg-* 2>/dev/null | head -1 || true)"
  if [ -n "$bundled" ] && [ -x "$bundled" ]; then printf '%s\n' "$bundled"; fi
}
FFMPEG="$(find_ffmpeg)"
[ -n "$FFMPEG" ] && [ -x "$FFMPEG" ] || die "no ffmpeg found (install ffmpeg, set \$FFMPEG, or pip install imageio-ffmpeg)"

OUT_DIR="${OUT_DIR:-download_parts/$SLUG}"
TITLE="${TITLE:-$(basename "$VIDEO")}"
[ -n "$BRANCH" ] || BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"

run() {
  if [ "$DRY_RUN" = 1 ]; then printf '   [dry-run] %s\n' "$*"; else "$@"; fi
}

probe() {
  # prints "duration | resolution" from ffmpeg's banner.
  # `ffmpeg -i` with no output always exits non-zero, so swallow the status.
  "$FFMPEG" -hide_banner -i "$1" 2>&1 | awk '
    /Duration:/ {d=$2; sub(/,$/,"",d)}
    # >=2 digits each side skips codec hex tokens such as 0x31637661
    /Video:/ && !seen { if (match($0, /[0-9][0-9]+x[0-9][0-9]+/)) {r=substr($0, RSTART, RLENGTH); seen=1} }
    END { printf "%s | %s", (d?d:"?"), (r?r:"?") }' || true
}

human_size() { awk -v b="$1" 'BEGIN{printf "%.1f MB", b/1048576}'; }
file_size() { wc -c < "$1" | tr -d ' '; }

note "Input"
info "video:     $VIDEO ($(human_size "$(file_size "$VIDEO")"))"
info "slug:      $SLUG"
info "output:    $OUT_DIR"
info "branch:    $BRANCH"
info "ffmpeg:    $FFMPEG"
info "part size: $(human_size "$PART_SIZE") ($PART_SIZE bytes)"

STAGE="$VIDEO"
SIZE="$(file_size "$VIDEO")"
LIMIT=95000000   # stay well under GitHub's 100 MB hard limit

# --- optional compact copy ----------------------------------------------------
if [ "$ENCODE" = 1 ] && { [ "$SIZE" -gt "$LIMIT" ] || [ "$FORCE_ENCODE" = 1 ]; }; then
  note "Re-encoding a compact copy (CRF $CRF, audio $ABR)"
  STAGE="$(dirname "$OUT_DIR")/$(basename "${VIDEO%.*}")_DL.mp4"
  info "target: $STAGE"
  [ "$DRY_RUN" = 1 ] || mkdir -p "$(dirname "$STAGE")"
  run "$FFMPEG" -y -hide_banner -loglevel warning \
      -i "$VIDEO" \
      -c:v libx264 -crf "$CRF" -preset veryfast -tune stillimage -pix_fmt yuv420p \
      -c:a aac -b:a "$ABR" -ac 2 -movflags +faststart "$STAGE"
  if [ "$DRY_RUN" = 0 ]; then
    NEWSIZE="$(file_size "$STAGE")"
    info "compact copy: $(human_size "$NEWSIZE") (was $(human_size "$SIZE"))"
    [ "$NEWSIZE" -le "$LIMIT" ] || info "WARNING: still over 95 MB — raise --crf and re-run"
  fi
elif [ "$SIZE" -gt "$LIMIT" ]; then
  die "$VIDEO is $(human_size "$SIZE"), over the 95 MB target, and --no-encode was given"
else
  info "small enough to publish as-is (no re-encode needed)"
fi

# --- split --------------------------------------------------------------------
note "Splitting into parts"
BASE="$(basename "${STAGE%.*}").mp4"
if [ "$DRY_RUN" = 1 ]; then
  TOTAL="$(file_size "$STAGE")"
  NPARTS=$(( (TOTAL + PART_SIZE - 1) / PART_SIZE ))
  info "[dry-run] would write $NPARTS parts of up to $(human_size "$PART_SIZE") into $OUT_DIR"
else
  mkdir -p "$OUT_DIR"
  rm -f "$OUT_DIR/$BASE".part*
  split -b "$PART_SIZE" -d -a 1 "$STAGE" "$OUT_DIR/$BASE.part"
  ls -l "$OUT_DIR" | awk 'NR>1 {printf "   %s  %.1f MB\n", $9, $5/1048576}'
fi

# --- verify the parts really rebuild the file ---------------------------------
note "Verifying parts rebuild the original"
if [ "$DRY_RUN" = 1 ]; then
  info "[dry-run] would compare sha256 of concatenated parts vs $STAGE"
else
  WHOLE="$(sha256sum "$STAGE" | awk '{print $1}')"
  JOINED="$(cat "$OUT_DIR/$BASE".part* | sha256sum | awk '{print $1}')"
  [ "$WHOLE" = "$JOINED" ] || die "parts do not rebuild the file (hash mismatch)"
  info "sha256 $WHOLE"
  info "OK — parts reassemble byte-for-byte"
fi

# --- README for the downloader ------------------------------------------------
note "Writing $OUT_DIR/README.md"
if [ "$DRY_RUN" = 1 ]; then
  info "[dry-run] would generate rejoin instructions + checksum"
else
  META="$(probe "$STAGE")"
  DURATION="${META%% | *}"
  RES="${META##* | }"
  PARTS_LIST="$(cd "$OUT_DIR" && ls "$BASE".part* | sed 's/^/    /')"
  CATLINE="$(cd "$OUT_DIR" && ls "$BASE".part* | tr '\n' ' ' | sed 's/ $//')"
  COPYLINE="$(cd "$OUT_DIR" && ls "$BASE".part* | paste -sd+ -)"
  cat > "$OUT_DIR/README.md" <<EOF
# $TITLE

Downloadable copy of \`$(basename "$STAGE")\` — $DURATION, $RES, $(human_size "$(file_size "$STAGE")").

Stored in parts because GitHub rejects any single file over 100 MB.

## 1. Download every part

$PARTS_LIST

## 2. Rejoin them

**macOS / Linux**
\`\`\`
cat $CATLINE > ${SLUG}.mp4
\`\`\`

**Windows (PowerShell)**
\`\`\`
cmd /c copy /b $COPYLINE ${SLUG}.mp4
\`\`\`

## 3. Verify

\`\`\`
$(sha256sum "$STAGE" | awk '{print $1}')
\`\`\`

\`shasum -a 256 ${SLUG}.mp4\` (macOS) or \`sha256sum ${SLUG}.mp4\` (Linux) must print the same string.

## Rebuilding the parts (maintainers)

\`\`\`
./scripts/publish_video_parts.sh <original.mp4> ${SLUG}
\`\`\`
EOF
  info "written"
fi

# --- publish ------------------------------------------------------------------
if [ "$LOCAL_ONLY" = 1 ]; then
  note "Skipping git (local-only / dry-run)"
  exit 0
fi

note "Committing to $BRANCH"
# Parts may match an ignore rule such as *.mp4 — force them in, and say so.
if git check-ignore -q "$OUT_DIR/$BASE.part0" 2>/dev/null; then
  info "note: $OUT_DIR is git-ignored; adding with -f"
  run git add -f "$OUT_DIR"
else
  run git add "$OUT_DIR"
fi
run git commit -q -m "Publish $SLUG video in parts for download"
if [ "$PUSH" = 1 ]; then
  run git push -q origin "$BRANCH"
fi

note "Download links"
if [ "$PUSH" = 1 ]; then
  REPO="$(git config --get remote.origin.url | sed -E 's#.*github\.com[:/]##; s#\.git$##')"
  gh api "repos/$REPO/contents/$OUT_DIR?ref=$BRANCH" \
    --jq '.[] | select(.name|test("part")) | "\(.download_url)"' 2>/dev/null \
    || info "(gh not available — open https://github.com/$REPO/tree/$BRANCH/$OUT_DIR)"
else
  info "not pushed; links will appear after: git push origin $BRANCH"
fi
