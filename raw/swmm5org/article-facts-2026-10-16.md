# Fact sheet for the swmm5.org canonical posts

Measured 16 October 2026 from the archive rebuilt on 14 October 2026.
Every figure below says where it came from. Nothing here is an estimate.

**Read this first:** the six quality markers were re-measured today against
new, written-down patterns. They do **not** match the numbers in
`swmm-app-quality-trend.xlsx`, and one of them moved a long way. Section 3
explains why.

---

## 1. The archive, as of 14 October 2026

Source: `data.json` embedded in `claude-chat-archive.html`, built from the
Claude.ai export taken 14 October 2026, plus the DeepSeek and Claude Code
transcripts merged earlier.

| Figure | Value |
|---|---|
| Conversations | 1,671 |
| Messages | 17,991 |
| App-building conversations | 533 |
| Distinct apps | 800 |
| Claude projects | 15 |
| First conversation | 21 November 2023 |
| Last conversation | 14 October 2026 |
| Span | 1,059 days |
| Days with activity | 720 (68% of the span) |
| Searchable text | 26.9 million characters |

Where the records come from:

| Source | Conversations |
|---|---|
| Claude.ai chat | 1,565 |
| DeepSeek | 96 |
| Claude Design | 6 |
| Claude Code | 4 |

Active days count days with a Claude.ai chat message. The other three sources
carry no per-day stamps, so their messages are in the message total but not in
the active-day count.

### By year

| Year | Conversations | Messages | App conversations | Apps | Active days |
|---|---|---|---|---|---|
| 2023 | 11 | 168 | 0 | 0 | 8 |
| 2024 | 164 | 2,526 | 1 | 2 | 207 |
| 2025 | 429 | 3,099 | 18 | 19 | 231 |
| 2026 | 1,067 | 12,198 | 514 | 779 | 274 |

2026 runs to 14 October only.

### 2026 month by month

| Month | Conversations | Apps |
|---|---|---|
| January | 54 | 51 |
| February | 100 | 85 |
| March | 142 | 122 |
| April | 178 | 99 |
| May | 213 | 147 |
| June | 74 | 71 |
| July | 110 | 84 |
| August | 64 | 50 |
| September | 59 | 51 |
| October (to the 14th) | 73 | 19 |

May was the peak. September ran at 28% of May's conversation count and 35% of
its apps.

### Shape of the work

| Figure | Value |
|---|---|
| Messages per conversation, median | 6 |
| Messages per conversation, mean | 10.8 |
| 90th percentile | 23 |
| Longest conversation | 356 messages |
| Busiest day | 4 May 2026, 201 messages |
| App conversations that produced one app | 357 |
| …two apps | 126 |
| …three apps | 32 |
| …four or more | 18 |

Conversations in which each thing happened at least once: code ran, 914;
the web was searched, 461; past chats were searched, 128; a question came
back to you, 97; a chart was drawn, 28.

---

## 2. What the apps were built from

Counted from the files each conversation actually produced. A conversation
counts as app-building when it created or presented an `.html`, `.htm` or
`.jsx` file, or created an HTML or React artifact.

Caution for the article: 2024 and 2025 look near-zero not because you built
nothing then, but because those conversations rarely wrote files — you were
working in artifacts and in chat. The 2026 figures are a count; the earlier
ones are a floor. Say so if you quote them.

---

## 3. The six quality markers, re-measured

### What changed, and why the old numbers are not these numbers

The workbook's series was measured with patterns that were never written
down. I could not reproduce them, so rather than mix old numerators with new
denominators I defined six patterns today, wrote them into
`markers.py`, and applied the same six to every quarter. Two differences
matter:

1. **The denominators moved.** The rebuild counts 533 app conversations where
   the workbook had 503, and it distributes them differently across quarters.
2. **One marker moved a long way.** My first pass put "found a defect" at 73%
   for 2026Q3. Reading the actual matches showed the pattern was catching
   *regression tests*, *mismatch checks* and quiz apps' "wrong answer" text.
   Tightened, the same quarter reads 47%. The 65% in the workbook sits between
   the two, and I cannot tell you which definition produced it.

If you publish a marker series, publish the patterns with it. That is the
only way the number survives someone checking it.

### The table

Share of that quarter's app-building conversations showing each marker.

| Marker | 2025Q4 | 2026Q1 | 2026Q2 | 2026Q3 |
|---|---|---|---|---|
| App conversations in quarter | 14 | 149 | 234 | 115 |
| Runs a real engine | 29% | 30% | 31% | 62% |
| Verified against engine output | 29% | 12% | 28% | 60% |
| Reports N/N test results | 7% | 13% | 24% | 72% |
| Found a defect | 0% | 7% | 23% | 47% |
| Went through review rounds | 0% | 16% | 15% | 27% |
| Produced a negative result | 0% | 11% | 12% | 15% |

Counts behind the percentages:

| Marker | 2025Q4 | 2026Q1 | 2026Q2 | 2026Q3 |
|---|---|---|---|---|
| Runs a real engine | 4 | 45 | 72 | 71 |
| Verified against engine output | 4 | 18 | 65 | 69 |
| Reports N/N test results | 1 | 19 | 55 | 83 |
| Found a defect | 0 | 10 | 54 | 54 |
| Went through review rounds | 0 | 24 | 36 | 31 |
| Produced a negative result | 0 | 16 | 27 | 17 |

2026Q4 (1–14 October, 16 conversations) reads 50% / 56% / 50% / 31% / 31% / 6%.
Two weeks is too thin to put in a trend; leave it out or mark it partial.

Quarters before 2025Q4 hold one or two app conversations each. Do not quote
a percentage from them.

### The patterns, in plain words

Each marker is a test on the full text of one app-building conversation,
case-insensitive, counted once per conversation. The text is what you and
Claude said: no thinking, no tool output.

1. **Runs a real engine.** The text names a real engine or toolchain (`wasm`,
   `emscripten`, `emcc`, `wasm32-wasi`, `swmm5.exe`, `runswmm`, `epaswmm5`,
   `epanet2.exe`, `pyswmm`, `swmm_api`, `wntr`), **or** the conversation's
   tool calls invoke one (a command running `swmm5 something.inp`, a `.wasm`
   engine, `pyswmm`, and so on). The second channel matters: the archive's
   searchable text holds only what was said, so a run inside a bash call is
   invisible to a text pattern. That channel alone found 268 conversations
   across the archive; 87 compiled an engine, 142 ran a test script.
2. **Verified against engine output.** The text contains a verification word
   (`verified`, `verify`, `verification`, `cross-check`, `ground truth`)
   **and** names engine output (`.rpt`, `.out`, `engine output`,
   `continuity error`, `summary table`).
3. **Reports N/N test results.** The text carries an N-of-N result near a
   test word (`103/103`, `34/34 pairs`, `23 checks green`), **or** the tool
   calls ran a test script.
4. **Found a defect.** The text says a defect was found, in the narrow sense:
   `found a bug`, `is a bug`, `engine bug`, `a defect`, `defect register`,
   `does not match`, `disagrees with`, `off by one`, `wrong value/result/
   sign/units/order`, `silently wrong/fails/drops/truncates`. The words
   `regression` and `mismatch` are deliberately excluded.
5. **Went through review rounds.** The text names a review (`review`,
   `critique`, `audit`, `graded`, `feedback from`, `second opinion`) **and**
   the conversation runs to 20 messages or more.
6. **Produced a negative result.** The text records something that did not
   work: `didn't work`, `no improvement`, `negative result`, `dead end`,
   `abandoned`, `gave up`, `failed to reproduce/improve/converge`,
   `no measurable`, `made it worse`, `not faster`, `no speedup`.

### What this measures, and what it does not

A marker is evidence of discipline **in the transcript**. It does not measure
whether the app is correct, whether the physics is right, or whether anyone
used the app afterwards. A conversation with no marker may have produced a
fine app and said nothing about checking it.

The 2026Q1 dip in "verified against engine output" (12%, down from 29%) rests
on a 2025Q4 denominator of 14 conversations, four of which matched. Small-n
noise, not a decline. Avoid claiming a monotonic rise.

---

## 4. Things worth saying that the numbers support

- Verification roughly doubled between 2026Q2 and 2026Q3 (28% → 60%) while
  the monthly app count fell by roughly two-thirds from the May peak.
- N/N reporting is the marker that moved most: 7% → 72%.
- Negative results stay rare. 17 conversations in 2026Q3, 15% of that
  quarter's app work. This is the argument for the findings register: a
  result that nobody writes down lives only in a transcript.
- Review rounds are the marker with the least movement, 16% → 27%, and the
  obvious reason is that there are few people to review this work.

---

## 5. Numbers from your own notes, to confirm before publishing

These come from your records rather than from anything I measured today.
Check them against the source before they go in a canonical post.

**EXTRAN III workbench.** Your About-tab text says: the 1981 printed listing
cut into program units and the OCR damage repaired with each repair logged;
the engines compiled to WebAssembly; each run scored value by value against
the printed 1981 output; the SWMM5-to-EXTRAN converter run against SWMM 5.2.4
on 259 models; 139 doubtful listing lines not yet confirmed against page
images.

**Named engine findings** you have recorded as verified, usable as examples of
what the apps turned up:

- A SLOT-versus-EXTRAN difference between SWMM5 builds (Four-Engine Pipe
  Comparator).
- A metric-units fault in the OpenSWMM 6.0.0-alpha.2 timeseries inflow path
  (Self-Play Lab).
- A PUMP3 curve-order bug (EPANET↔SWMM5 Rosetta Stone).
- 23 documented deviations from SWMM5 in the Rust `hydra` engine.
- A `dt`-rounding bug (SWMM Arithmetic Fingerprints).

---

## 6. Archive and tooling facts, for the method article

| Figure | Value |
|---|---|
| Archive page size | 12.3 MB |
| Size before compression | 38.9 MB |
| Embedded data, uncompressed | 29,142,546 bytes |
| Decompression time in the browser | 630 ms |
| Verification of the decompressor | SHA-256 match against the original |
| Topic labels written by hand for the October refresh | 80 |
| Filename-clustering threshold | 0.62, chosen by scoring five values |
| Export parsed | 638 MB |

---

## AI use

Robert Dickinson directed this work and is responsible for it. Claude (Opus 5,
Anthropic) measured the archive in October 2026: it wrote the extractor, wrote
and ran the six marker patterns, read the matches, tightened the defect
pattern after finding false positives, and wrote this sheet. The archive
figures in sections 1, 2 and 6 are counts, reproducible from the dataset. The
marker percentages in section 3 depend on the patterns printed there, and no
person has reviewed the individual matches beyond the samples described. The
figures in section 5 are transcribed from Bob's own notes and have not been
re-verified.
