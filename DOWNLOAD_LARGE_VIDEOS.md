# Publishing large videos so they can be downloaded

How to hand over a finished video that is too big for GitHub's file limit — worked out
on the Pension Batch 2 film (139 MB master) and written so it can be repeated for any
other coverage.

**Short version:** make a compact copy, cut it into ~38 MB parts with `split`, commit the
parts, and give the viewer a one-line command to rejoin them. One script does all of it:

```
./scripts/publish_video_parts.sh my_video.mp4 coverage-slug
```

---

## 1. Why this route, and not the obvious ones

Everything below was actually attempted; the last row is the one that works.

| Route | What happened |
|---|---|
| **Preview / dev-server URL** (`https://PORT-SANDBOXID.e2b.app/file.mp4`) | Not reachable from the viewer's browser for a 139 MB file. Works for pages, not for large downloads. |
| **GitHub release asset** (`gh release create … file.mp4`) | `Post "https://uploads.github.com/…": EOF` — the upload endpoint is not in a sandbox's outbound allowlist. Fails instantly. |
| **Commit the master file to Git** | GitHub hard-rejects any single file over 100 MB. Push refused. |
| **Git LFS** | Needs paid LFS quota and a client on the viewer's machine. Not worth it for one file. |
| **Commit ~38 MB parts to Git** | ✅ Works. Verified: three parts, byte-identical on reassembly, links resolve publicly. |

Two useful corollaries:

- **The 100 MB limit is per file, not per commit.** Three 38 MB files in one commit are fine.
- **If the viewer can use a desktop browser**, uploading the master to a GitHub release by
  hand (drag-and-drop in the Releases UI) is the nicest result — one file, one link, no
  rejoining. That is the only step a sandbox cannot do for you.

---

## 2. Run the script (normal case)

```bash
# from the repo root, on the branch you want to publish from
chmod +x scripts/publish_video_parts.sh
./scripts/publish_video_parts.sh pension_b2_hinglish_FULL.mp4 batch2-rules-11-30
```

It will:

1. check the file is under the size target, and re-encode a compact copy if not;
2. split it into parts of 38,000,000 bytes;
3. prove the parts rebuild the original (SHA-256 of `cat part*` vs the source);
4. write `download_parts/<slug>/README.md` with rejoin + verify instructions for the viewer;
5. commit and push;
6. print the public download URLs.

### Flags worth knowing

| Flag | Use it when |
|---|---|
| `--crf N` | You want a smaller or better-looking compact copy. 28 default; 30–32 for smaller. |
| `--audio-bitrate 72k` | Audio is speech; 64k–96k is plenty. |
| `--part-size BYTES` | Default 38 MB. Keep parts under 95 MB; smaller parts also survive flaky mobile downloads better. |
| `--no-encode` | File is already small (under ~95 MB) and you want it published untouched. |
| `--force-encode` | File is small but you still want a lighter copy (slow connections). |
| `--title "…"` | Nicer heading in the generated README. |
| `--no-push` | Commit locally, push yourself later. |
| `--local-only` | Do everything except git — a safe rehearsal. |
| `--dry-run` | Print the plan, change nothing. |

Rehearse on any coverage first:

```bash
./scripts/publish_video_parts.sh my_video.mp4 test-slug --dry-run
```

---

## 3. The manual version (if you want to do it by hand)

```bash
# 0. variables for this coverage
SRC=pension_b2_hinglish_FULL.mp4
SLUG=batch2-rules-11-30
DIR=download_parts/$SLUG
LIMIT=95000000        # stay under GitHub's 100 MB hard limit

# 1. compact copy (only if the master is over the limit)
ffmpeg -y -i "$SRC" \
  -c:v libx264 -crf 28 -preset veryfast -tune stillimage -pix_fmt yuv420p \
  -c:a aac -b:a 72k -ac 2 -movflags +faststart "${SRC%.*}_DL.mp4"

# 2. split
mkdir -p "$DIR"
split -b 38000000 -d -a 1 "${SRC%.*}_DL.mp4" "$DIR/$(basename "${SRC%.*}_DL").mp4.part"
ls -l "$DIR"

# 3. verify the parts really rebuild the file
sha256sum "${SRC%.*}_DL.mp4"
cat "$DIR"/*.part* | sha256sum          # must match the line above

# 4. write the rejoin README (see section 5 for the template)

# 5. publish
git add -f "$DIR"                       # -f if *.mp4 is git-ignored
git commit -m "Publish $SLUG video in parts for download"
git push origin "$(git rev-parse --abbrev-ref HEAD)"

# 6. collect the links
gh api "repos/OWNER/REPO/contents/$DIR?ref=BRANCH" \
  --jq '.[] | select(.name|test("part")) | .download_url'
```

Notes that cost time if you learn them the hard way:

- **`split -d -a 1`** gives `.part0 … .part9`. Past nine parts use `-a 2` (`.part00`), or
  `cat part*` will sort `part10` before `part2` and silently corrupt the join.
- **Quote the glob** (`"$DIR"/*.part*`) so a stray `.part0.tmp` does not sneak in.
- **`-movflags +faststart`** moves the MP4 index to the front — the file starts playing
  before it is fully downloaded.
- **Force-add the parts** if the repo ignores video files; `git check-ignore -v file` tells
  you which rule matched.

---

## 4. What the numbers looked like for this project

Measured on the Batch 2 film, so you can predict your own:

| | Value |
|---|---|
| Master | 58 m 37 s, 1920×1080, 138.9 MB (≈331 kb/s total) |
| Compact copy, CRF 28 + 72k audio | **75.4 MB** (≈179 kb/s; video 99 kb/s) |
| Parts | 3 × (38.0 MB, 38.0 MB, 3.0 MB) |
| Reassembly | byte-identical, SHA-256 `5297403e…58b903` |

**Static slides compress extremely well.** A talking-slide video needs a fraction of the
bitrate of camera footage; CRF 28 at 1080p is visually indistinguishable here because
almost every frame is a still. If your coverage is screen-recorded or slide-based, expect
similar — do not assume you need CRF 20.

### Picking a part size

| Situation | Part size |
|---|---|
| Default | 38 MB — three parts for a ~75 MB file, safe on mobile |
| Very flaky connections | 10–20 MB — more parts, each retry is cheap |
| You want the fewest files | 90 MB — still under the hard limit, but a failed download wastes more |

---

## 5. Rejoin instructions to give the viewer

The script generates this; here is the template so you can paste it into a message anywhere.

````markdown
Download all three parts, then rejoin them:

**macOS / Linux**
```
cat MY.mp4.part0 MY.mp4.part1 MY.mp4.part2 > MY.mp4
```

**Windows (PowerShell)**
```
cmd /c copy /b MY.mp4.part0+MY.mp4.part1+MY.mp4.part2 MY.mp4
```

Verify — this must print exactly `<sha256>`:
```
shasum -a 256 MY.mp4      # macOS
sha256sum MY.mp4          # Linux
```
````

Always ship the checksum. It is the difference between "the video looks odd" and "one part
downloaded short" — and it takes ten seconds to add.

---

## 6. Applying this to another coverage

Per-coverage checklist:

1. **Render the film** (same pipeline as Batch 2: `build_*.py` → `make_video2.py`).
2. **Confirm it plays end to end** before publishing — check a frame early, middle and late.
   A part-published broken film is much worse than a late one.
3. **Pick a slug** that says what it covers: `batch2-rules-11-30`,
   `leave-rules-1-20`, `conduct-part2`. It becomes the folder name, so keep it short and
   stable — renaming later breaks any link you have already shared.
4. **Publish:**
   ```bash
   ./scripts/publish_video_parts.sh my_video.mp4 <slug> --title "CCSP Rules 2021 — …"
   ```
5. **Hand over the links** and the rejoin block from section 5.
6. **Record it** in your production notes: slug, duration, size, SHA-256, branch, date.

### Naming and layout

```
download_parts/
  batch2-rules-11-30/
    README.md                        # rejoin + checksum, written by the script
    pension_b2_hinglish_DL.mp4.part0
    pension_b2_hinglish_DL.mp4.part1
    pension_b2_hinglish_DL.mp4.part2
  leave-rules-1-20/
    README.md
    …
```

One folder per coverage. Never reuse a folder for a different film — old parts plus new
parts with the same names produce a file that reassembles successfully and is corrupt.

---

## 7. Repo cost, and how to keep it sane

- **Every published film stays in Git history forever**, even if you delete the folder later.
  A 75 MB coverage costs ~75 MB of history, permanently.
- If you publish a lot of these, consider **one branch per coverage** (or a dedicated
  `downloads` branch) so the main branch stays light, and prune old branches when the
  links are no longer needed.
- **Do not re-commit the same parts with a new name** — you double the history for one file.
- `git count-objects -vH` shows the repo size; `git gc --aggressive --prune=now` will not
  remove reachable objects, only unreachable ones.
- Keep the master (highest quality) **out** of Git. Publish only the compact copy; the
  master belongs on Drive/S3 or in the Arena viewer.

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `remote: error: File … is 139.00 MB; this exceeds GitHub's file size limit of 100.00 MB` | Committed the master | Re-encode (section 3, step 1) and commit only the compact copy |
| `Post "https://uploads.github.com/…": EOF` | Sandbox cannot reach the upload host | Use parts, or upload the release asset from your own browser |
| `The following paths are ignored by one of your .gitignore files` | `*.mp4` rule | `git add -f download_parts/<slug>` |
| Rejoined file won't play, or plays only briefly | Parts missing / downloaded short / wrong order | Re-download, compare SHA-256, check part count and the `-a 1` vs `-a 2` naming |
| `cat` produced a file but the hash differs | A part was truncated by a dropped download | Compare each part's byte size with the repo listing |
| Script says `no ffmpeg found` | Bare sandbox, no system ffmpeg | `pip install imageio-ffmpeg`, or set `FFMPEG=/path/to/ffmpeg` |
| Link 404s after a while | Branch renamed, or file moved | The parts must stay at the same path on the same branch |

---

## 9. Quick reference

```bash
# rehearse
./scripts/publish_video_parts.sh video.mp4 slug --dry-run

# publish (handles encode, split, verify, README, commit, push, links)
./scripts/publish_video_parts.sh video.mp4 slug --title "Coverage title"

# list what is already published
gh api "repos/OWNER/REPO/contents/download_parts?ref=BRANCH" --jq '.[].name'

# repo weight check
git count-objects -vH
```
