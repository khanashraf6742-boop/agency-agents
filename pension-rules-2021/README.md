# CCS (Pension) Rules 2021 — Batch 4 explainer (Rules 42–52)

A single-file Python compiler that renders a 43-chapter, screenshot-style explainer video for
**Rules 42 to 52** of the CCS (Pension) Rules, 2021 (Chapters VI to IX), with the on-screen text in
English and the narration in Hinglish. Everything is Roman script — no Devanagari anywhere.

```
build_pension_b4.py                        the compiler (the deliverable)
build_pension_b4_simple_english_video.md   the same file, wrapped as a copy-paste document
pension_b4_audit_report.md                 generated: 297 rows of provision-by-provision coverage
pension_b4_reference_sheet.md              generated: the full wording behind every on-screen card
preview/                                   four rendered stills, one per visual layout
```

## Language decision

| Layer | Language | Script | Why |
|---|---|---|---|
| On-screen text: labels, cards, tables, charts, trap strip | English | Roman | Your reference frame is English; it also keeps the exam answers quotable verbatim |
| Narration: teacher + student | Hinglish | Roman | City Hinglish is what the audience actually hears; Roman keeps the source file free of Devanagari |
| Subtitles (burned into the video) | Hinglish | Roman | They must match the voice, not the slides |
| Full-wording reference sheet | English | Roman | Written-answer material |

The TTS layer includes an explicit **Devanagari guard**: `normalize_for_tts()` raises if it ever finds a
character in the `U+0900–U+097F` range, and `validate_scenes()` refuses to render a card that contains one.
Roman Hinglish words are respelled for an `en-IN` neural voice (`nahi → naheen`, `kyunki → kyonki`,
`zyada → zyaada`) so it reads them the way an Indian speaker would.

## What the audit found in the old build

The old build was well-structured but had **statutory holes and a stated-versus-corrected conflict**.
Everything below is now inside the cards, and the `--audit` run proves it mechanically.

**Missing provisions that are now taught**

1. **Rule 47(4) to (8)** — post-death marriage or a brother turning 18, minor through the guardian,
   the natural-guardian rule, the **20 per cent on an Indemnity Bond in Format 7** exception, and the
   Form 9 independent-processing rule. Two whole chapters were absent.
2. **Rule 50(8)(b) to (k)** — the old build had *one* card for an eleven-clause sub-rule. The childless
   widow on re-marriage, more widows than one, the widow with no child, children of a dead or divorced
   wife, children of a void marriage, judicial separation with and without a minor child, and the
   annual "not earning" certificate are now clause-by-clause.
3. **Rule 50(9)(d) to (p)** — birth order, twins, the seven conditions for a lifetime disability
   pension (including the RPwD/Medical Board certificate and the National Trust guardianship
   certificate), the **daughter-beyond-25 route with its six conditions and two provisos**, children of
   more than one mother, and the four ways a child's pension ends.
4. **Rule 50(14)** — the family-pension murder charge, the **guardian bar on the accused spouse**, the
   conviction and acquittal dates and their provisos. This sub-rule was **completely absent**.
5. **Rule 50(15) and (16)** — Form 4, Form 5, Form 10, the disability certificate, and the
   re-employment exclusion.
6. **Rule 51(4) to (7) and (9) to (11)** — gratuity on going missing, the claim papers, the pay base on
   the last day on duty, **arrears / leave salary / GPF**, the fraud exclusion, and the bar on paying a
   non-family member.
7. **Rule 52(2) proviso limb (i)** — the **Group 'A' post test** was missing; only two of the three
   conditions were being taught.
8. **Rule 45(6) Explanation** — the eleven-clause definition of "family" for Rules 45 to 49 was only
   name-checked. It is now a full table, because it decides Rules 47, 48 and 49.

**Corrections to statements that were previously wrong**

| Provision | Was being taught | Now taught |
|---|---|---|
| Rule 42(2) | notice is optional | the sub-rule offers **notice or pay in lieu**; one of the two is required |
| Rule 43(1) P1 | "no administrative difficulty" certificate | certificate **of 20 years**, requested **before** the notice, issued in **15 days** |
| Rule 43(3) proviso | not mentioned | acceptance despite suspension / charge sheet needs the **President's approval** |
| Rule 44(6) illustration | not mentioned | born 20.08.1942 **and** 01.08.1942 both pay from **01.08.2022** |
| Rule 50(2)(a)(iii) | "27 years" | **age 67** — a typographical error in the source |
| Rule 50(13) | one cap | **Rs 1,25,000** while either pension is enhanced, **Rs 75,000** when both are ordinary |
| Rule 51(1)(b) limb (ii) | the day after pay stopped | **the date up to which pay was paid** — "date following" attaches to the leave limb only |
| Rule 51(8)(a) proviso | interest "not seen" | **interest under Rule 65** for delay beyond six months **from the date of the claim** |
| Rule 44(3) | cap implied | service gratuity under Rule 44(2) has **no 16.5-times cap**; that cap is in Rule 45 |

## Audit output (current build)

```
statutory provisions tracked : 297
provisions without a card    : 0
unexplained tags             : 0
density failures             : 0
rows below 30px or over 2 lines: 0
cards                        : 172
mean Flesch Reading Ease     : 61.2   (plain English; 60-70 is "standard")
Devanagari characters        : 0
VERDICT: PASS
```

## Visual system

Five layouts, all on the same 1920×1080 navy canvas with a 60px grid, so a chapter can change layout
without the video looking like it changed channel.

| Layout | Used for | Example |
|---|---|---|
| Label + row cards | the ordinary teaching chapter (four rows, purple label tile + wide content card) | `preview/01-layout-rows.png` |
| Comparison table | the four gratuities, Rule 45(6) family, Rule 50(8), the recap numbers | `preview/02-comparison-table.png` |
| Bar chart | the additional-pension slabs and the death-gratuity multiples | `preview/03-bar-chart.png` |
| Split compare | a two-or-four-way contrast that is not numeric | — |
| Trap strip | the yellow bottom bar on every chapter, dark ink for contrast | all stills |

Inline markup in the content layer drives colour and weight without any per-run Python:

```
**bold white**   ==yellow==   [[teal]]   {{purple}}   <<red>>   //blue//   ~~amber~~   __green__   @@muted@@
```

## Running it

```bash
pip install Pillow
python build_pension_b4.py --audit            # the proof: coverage, density, readability
python build_pension_b4.py --preview          # every slide, no ffmpeg
python build_pension_b4.py --master           # THE VIDEO: silent captioned master, no TTS needed
python build_pension_b4.py --master --part 2  # chapters 16-30 only
python build_pension_b4.py                    # full build with edge-tts narration
python build_pension_b4.py --no-tts           # silent timing run with placeholder audio
```

### The delivered video

`pension_b4_master_silent.mp4` — 1920x1080, 25 fps, **46 min 27 s**, 69,675 frames, 215 stills,
1,069 caption cues, ~60 MB, H.264 High + AAC.

### Narrated master (the finished video)

`pension_b4_master_narrated.mp4` is the delivered video: **48 min 47 s**, 1920x1080, H.264 High +
AAC 96 kbps stereo, ~91 MB, **spoken narration throughout**.

- **Teacher** voice reads the rule text, the worked examples and the trap warnings.
- **Student** voice asks the opening question of each chapter.
- The Hinglish captions stay burned into the reserved band, so the video works with sound off too.

The narration is not a words-per-second guess. Every clip was recorded from the exact script, then
split back into its script segments by a monotonic dynamic-programming alignment over the pauses the
voice actually makes (character share as the cost prior). Across the 253 measured units the
correlation between characters and spoken duration is **0.972**, so a slide is always on screen
while its own sentence is being spoken. Slide time, caption time and audio time all come from those
same measured durations, and the runtime is 48.78 min in all three.

Rebuild it with:

```bash
python narrate_build.py --status   # how many clips exist
python narrate_build.py --plan     # print the next batch of scripts to record
python narrate_build.py --build    # assemble video + narration
```

`pension_b4_master_silent.mp4` is kept as the voice-free fallback (46:27, 54 MB).

### Download

The MP4 is committed to this repository so it can be downloaded without the build sandbox:

- **Raw download:** <https://github.com/khanashraf6742-boop/agency-agents/raw/arena/f3b9d7cb-agency-agents/pension-rules-2021/pension_b4_master_silent.mp4>
- **File page (big Download button):** <https://github.com/khanashraf6742-boop/agency-agents/blob/arena/f3b9d7cb-agency-agents/pension-rules-2021/pension_b4_master_silent.mp4>

`.gitignore` keeps every other `*.mp4` out of the repository and whitelists only this file.
GitHub warns that it is above the 50 MB recommended size; it is well under the 100 MB hard limit.

**The caption band is reserved, not overlaid.** Four-card slides reach y=902, which is exactly
where burned captions sit, so a fixed overlay collided with the last card on the busiest chapters.
`--master` therefore scales the card area (everything above the trap strip) from 0..980 px into
0..860 px, fills 860..980 px with the slide's own background ramp, and pastes the yellow trap strip
and footer back untouched. Every frame now has an identical empty band at 860..980 px, and the
captions sit inside it — never over a card, never over the trap.

It is **silent by design**: every word of the Hinglish narration is burned in as a two-line caption in
the reserved band above the trap strip. That is deliberate, because this sandbox cannot reach the
edge-tts endpoint (`speech.platform.bing.com`) or any binary CDN, so neural speech could not be
generated here. The caption timing is caption-paced at 3.15 English words per second, which is a
comfortable read-aloud speed and also very close to what an `en-IN` neural voice produces, so a later
voice pass will drop onto the same timeline.

**To add the voice later**, on any machine with internet access:

```bash
python build_pension_b4.py --part 1     # chapters 1-15, real edge-tts narration
python build_pension_b4.py --part 2
python build_pension_b4.py --part 3
```

or build the whole thing in one pass with `python build_pension_b4.py`.

### ffmpeg

The compiler finds `ffmpeg` on `PATH`, and otherwise falls back to a bundled static build:

```bash
pip install imageio-ffmpeg     # provides ffmpeg 7.0 with libass, which the captions need
```

`--master` refuses to run on an ffmpeg without libass, and after encoding it samples eight cue
midpoints and fails the build if the caption band is empty — so a silent "captions did not burn"
failure cannot ship. The white narration cues sum to ~730 brightness, the amber student cues to
~532 and the navy slide background to under 90, so the threshold of 450 catches both voices.

**How the timeline is made frame-exact.** The ffmpeg concat demuxer injects phantom hold-frames at
every `file` boundary — measured at ~2.4 extra frames per still, which is about 16 s of drift over
215 stills and is enough to slide captions off their slides. So `--master` does not rely on it:
each still is encoded as its own clip with `-frames:v N` (N = round(seconds x fps)), the caption
layer is shifted to that still's global start time with `setpts=PTS+t0/TB,ass=...,setpts=PTS-t0/TB`,
and the clips are then stream-copied together with `-c copy`. Frame counts, not timestamps, are
authoritative, so the burned caption always matches the frame it belongs to.

Default voices are `en-IN-PrabhatNeural` (teacher) and `en-IN-NeerjaNeural` (student), which read
Roman Hinglish correctly. If you ever want Devanagari narration, `HI_TEACHER` / `HI_STUDENT` are
already defined — but the on-screen text must stay Roman.

## Still flagged as unverified

These are printed on the cards themselves, so nobody teaches them as settled law.

- The **Gazette PDF of G.S.R. 868(E)** was not opened directly. Wording is a close restatement from a
  faithful reproduction of Rules 40 to 55; treat the quotations as restatements, not certified text.
- The **DR revision from 01.07.2026** had not been announced as of mid-October 2026. 60 per cent from
  01.01.2026 is the last confirmed rate.
- No Gazette notification was found codifying either the **01.01.2024 marital-discord order** or the
  **Rs 25 lakh gratuity ceiling**. Both still live in the O.M., and the Rule text still prints twenty lakh.
- The **8th CPC** was constituted on 03.11.2025; its report (about May 2027) can move the pension floor
  and ceiling, which sit inside Rule 44(1).
- **G.S.R. 775(E) of 2026** was seen only through an earlier batch note and is outside Rules 42 to 52.
- The **DR sequence before the 60 per cent step** was not verified order by order.
