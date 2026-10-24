# Publishing large admin-rules videos for download

A general procedure for handing over finished training videos on **any administrative-rules
content** — CCS Conduct Rules, CCS Leave Rules, non-statutory leave, pension rules, GPF,
joining time, pay fixation, or any other coverage — when the film is too big for GitHub's
file limit.

Applies to every coverage in this library. Nothing here is specific to one batch.

**Short version:** make a compact copy, split it into ~38 MB parts, commit the parts, and
give the viewer a one-line command to rejoin them. One script does all of it:

```
./scripts/publish_video_parts.sh my_video.mp4 <coverage-slug>
```

---

## 1. Why this route, and not the obvious ones

Each of these was tried for real; only the last works without help.

| Route | What happens |
|---|---|
| **Preview / dev-server URL** (`https://PORT-SANDBOXID.e2b.app/file.mp4`) | Not reachable from the viewer's browser for a large file. Fine for pages, not for downloads. |
| **GitHub release asset** (`gh release create … file.mp4`) | `Post "https://uploads.github.com/…": EOF` — the upload endpoint is not in a sandbox's outbound allowlist. Fails instantly. |
| **Commit the master file to Git** | GitHub hard-rejects any single file over 100 MB. Push refused. |
| **Git LFS** | Needs paid LFS quota plus a client on the viewer's machine. Not worth it for one film. |
| **Commit ~38 MB parts** | ✅ Works. Parts reassemble byte-identically and the links resolve publicly. |

Two corollaries:

- **The 100 MB limit is per file, not per commit.** Three 38 MB files in one commit are fine.
- **With a desktop browser**, dragging the master into a GitHub Release by hand gives the
  nicest result — one file, one link, no rejoining. That is the only step a sandbox
  cannot do for you.

---

## 2. Run the script (normal case)

```bash
# from the repo root, on the branch you will publish from
chmod +x scripts/publish_video_parts.sh
./scripts/publish_video_parts.sh conduct_rules_rules_1_20.mp4 conduct-rules-1-20 \
  --title "CCS (Conduct) Rules — Rules 1 to 20"
```

The script:

1. checks the file against the size target, and re-encodes a compact copy if needed;
2. splits it into parts of 38,000,000 bytes;
3. **proves the parts rebuild the original** (SHA-256 of `cat part*` vs the source);
4. writes `download_parts/<slug>/README.md` with rejoin and verify steps for the viewer;
5. commits and pushes;
6. prints the public download URLs.

### Flags

| Flag | Use it when |
|---|---|
| `--crf N` | You want a smaller or better-looking compact copy. 28 default; 30–32 smaller. |
| `--audio-bitrate 72k` | Narration only; 64k–96k is plenty. |
| `--part-size BYTES` | Default 38 MB. Keep every part under 95 MB. |
| `--no-encode` | File is already under ~95 MB and should be published untouched. |
| `--force-encode` | File is small but you still want a lighter copy for slow connections. |
| `--title "…"` | Heading inside the generated README. |
| `--branch NAME` | Publish to a specific branch (e.g. a per-coverage downloads branch). |
| `--no-push` | Commit locally, push yourself later. |
| `--local-only` | Everything except git — a safe rehearsal. |
| `--dry-run` | Print the plan, change nothing. |

Rehearse before publishing:

```bash
./scripts/publish_video_parts.sh my_video.mp4 test-slug --dry-run
```

The script needs `ffmpeg` (system, or `pip install imageio-ffmpeg`), `split`, `sha256sum`,
and `gh` for the link printout. Copy `scripts/publish_video_parts.sh` into any other repo
you want to use it in — it has no project-specific dependencies.

---

## 3. The manual version

```bash
SRC=conduct_rules_rules_1_20.mp4
SLUG=conduct-rules-1-20
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

# 4. write the rejoin README (template in section 6)

# 5. publish
git add -f "$DIR"                       # -f if *.mp4 is git-ignored
git commit -m "Publish $SLUG video in parts for download"
git push origin "$(git rev-parse --abbrev-ref HEAD)"

# 6. collect the links
gh api "repos/OWNER/REPO/contents/$DIR?ref=BRANCH" \
  --jq '.[] | select(.name|test("part")) | .download_url'
```

Points that cost time if you learn them the hard way:

- **`split -d -a 1`** yields `.part0 … .part9`. Past nine parts use `-a 2`, otherwise
  `cat part*` sorts `part10` before `part2` and silently corrupts the join.
- **Quote the glob** (`"$DIR"/*.part*`) so a stray temporary file cannot sneak in.
- **`-movflags +faststart`** puts the MP4 index at the front, so playback starts before the
  download finishes.
- **Force-add the parts** if the repo ignores video files; `git check-ignore -v file` names
  the rule that matched.
- **Check the reassembly hash every time.** Splitting is silent when it goes wrong.

---

## 4. Realistic sizes for admin-rules videos

Benchmarks from a 58-minute, 1920×1080 rules-explainer film with static slides and
narration, useful for planning any similar coverage:

| | Value |
|---|---|
| Master, high quality | 58 m 37 s, 1920×1080, 138.9 MB (≈331 kb/s total) |
| Compact copy, CRF 28 + 72k audio | **75.4 MB** (video 99 kb/s, audio 71 kb/s) |
| Parts at 38 MB | 3 × (38.0 MB, 38.0 MB, 3.0 MB) |
| Reassembly | byte-identical, verified by SHA-256 |

**Rules videos compress extremely well.** They are mostly static slides with a caption band
and speech, so CRF 28 at 1080p is visually indistinguishable from the master here. Do not
copy settings from camera footage — you will ship a file several times larger than needed.

Rough planning rule for slide-based content at 1080p:

| Duration | Compact size at CRF 28 | Parts at 38 MB |
|---|---|---|
| 15 minutes | ~20 MB | 1 |
| 30 minutes | ~40 MB | 2 |
| 60 minutes | ~75 MB | 3 |
| 90 minutes | ~115 MB | 4 |

**Part size choice:**

| Situation | Part size |
|---|---|
| Default | 38 MB — few files, safe on mobile |
| Flaky or metered connections | 10–20 MB — more parts, but each retry is cheap |
| Fewest possible files | 90 MB — still under the limit, but a failed download wastes more |

---

## 5. Slugs and folders

The slug becomes the folder name and stays in every link you share, so choose it once,
make it say what it covers, and never rename it.

```
download_parts/
  conduct-rules-1-20/
    README.md
    conduct_rules_rules_1_20_DL.mp4.part0
    conduct_rules_rules_1_20_DL.mp4.part1
  leave-rules-1-30/
    README.md
    …
  pension-batch2-rules-11-30/
    README.md
    …
  nonstat-leave-complete/
    README.md
    …
```

Naming convention that stays readable as the library grows:

```
<subject>-<part-or-range>        e.g.  conduct-rules-1-20
                                       leave-rules-21-35
                                       pension-b2-rules-11-30
                                       nonstat-leave-full
```

**Never reuse a folder for a different film.** Old parts plus new parts with the same names
produce a file that reassembles successfully and is corrupt — the worst possible failure,
because the checksum is the only thing that catches it.

---

## 6. Rejoin block to give the viewer

The script generates this automatically; here is the template for pasting into any message.

````markdown
Download all parts, then rejoin them.

**macOS / Linux**
```
cat MY.mp4.part0 MY.mp4.part1 MY.mp4.part2 > MY.mp4
```

**Windows (PowerShell)**
```
cmd /c copy /b MY.mp4.part0+MY.mp4.part1+MY.mp4.part2 MY.mp4
```

Verify — this must print exactly <sha256>:
```
shasum -a 256 MY.mp4      # macOS
sha256sum MY.mp4          # Linux
```
````

Always ship the checksum. It turns "the video looks odd" into "part 1 downloaded short" in
ten seconds.

---

## 7. Per-coverage checklist

1. **Render the film** with the usual pipeline for that coverage.
2. **Confirm it plays end to end** — check a frame early, middle and late, and that the
   caption band shows the right speaker throughout. Publishing a broken film in parts is
   much worse than publishing late.
3. **Pick the slug** per section 5.
4. **Publish:**
   ```bash
   ./scripts/publish_video_parts.sh <file>.mp4 <slug> --title "<Coverage title>"
   ```
5. **Hand over** the links plus the rejoin block from section 6.
6. **Record** in the production notes: slug, duration, size, SHA-256, branch, date.

---

## 8. Repo cost, and keeping it sane

- **Every published film stays in Git history permanently**, even if you delete the folder
  afterwards. A 75 MB coverage costs ~75 MB of history, forever.
- Publishing many coverages? Use **one branch per coverage**, or a dedicated `downloads`
  branch, so the main branch stays light, and prune branches whose links are retired.
- **Do not re-commit the same parts under a new name** — that doubles the history for one
  film.
- `git count-objects -vH` reports repo size. `git gc --aggressive --prune=now` removes only
  *unreachable* objects; it cannot shrink committed films.
- Keep the **master** out of Git. Publish the compact copy only; the master belongs on
  Drive/S3 or in the Arena viewer.

---

## 9. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `File … is 139.00 MB; this exceeds GitHub's file size limit of 100.00 MB` | Committed the master | Re-encode, commit only the compact copy |
| `Post "https://uploads.github.com/…": EOF` | Sandbox cannot reach the upload host | Use parts, or upload the release asset from your own browser |
| `The following paths are ignored by one of your .gitignore files` | `*.mp4` ignore rule | `git add -f download_parts/<slug>` |
| Rejoined file will not play, or plays only briefly | Missing, short or out-of-order parts | Re-download, compare SHA-256, check `-a 1` vs `-a 2` naming |
| `cat` produced a file but the hash differs | A part was truncated | Compare each part's byte size with the repo listing |
| Script says `no ffmpeg found` | Bare environment | `pip install imageio-ffmpeg`, or set `FFMPEG=/path/to/ffmpeg` |
| Link 404s later | Branch renamed or file moved | Parts must stay at the same path on the same branch |
| Video plays but captions look wrong | Regenerated slides without rebuilding clips | Rebuild that range of clips before publishing |

---

## 10. Quick reference

```bash
# rehearse
./scripts/publish_video_parts.sh video.mp4 slug --dry-run

# publish (encode, split, verify, README, commit, push, links)
./scripts/publish_video_parts.sh video.mp4 slug --title "Coverage title"

# list what is already published
gh api "repos/OWNER/REPO/contents/download_parts?ref=BRANCH" --jq '.[].name'

# repo weight check
git count-objects -vH
```
