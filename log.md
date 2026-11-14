# Log

Append-only. One entry per operation, newest at the bottom. `grep "^## \[" log.md | tail -5` lists the last five.

## [2026-11-14] setup | Repository created

Skeleton built by Claude (Anthropic) at Bob's request, after Karpathy's LLM wiki pattern: `raw/`, `wiki/`, `index.md`, `log.md`, `CLAUDE.md`, `tools/`. Raw sources copied in from what was in the workspace: 231 published LinkedIn articles (converted from the LinkedIn data export by `tools/li2md.py`; 57 unpublished drafts left out on purpose), 3 app summaries, the findings register and its seed, 2 SWMM 1 build notes, the swmm5.org fact sheet and 7 topic pages, the OpenSWMM thread list and the top-25 tally. 248 raw files; the markdown among them holds about 324,000 words.

## [2026-11-14] ingest | First batch: 22 sources

Sources S01 to S22: 2 app summaries, 5 notes and data files, 3 swmm5.org pages, 12 LinkedIn articles, chosen for the themes "history of SWMM" and "the insides of SWMM5". Each was read in full, except S15, whose AI-written narrative was skimmed for the function and variable names it carries. Pages created: 22 source pages, 22 concept pages, 15 entity pages, the overview and the open-questions list. The OpenSWMM counts on S09 were computed from the CSV with a script.

Not ingested though read: nothing. Not ingested and noted for later: the dynwave.c and dwflow.c "story" articles (13,000 words of AI-written narrative; low fact density).

## [2026-11-14] lint | First pass

`tools/lint.py`: 0 errors. Read-through found 19 open questions (Q01 to Q19), written to `wiki/open-questions.md`: 8 places where sources disagree, 5 arithmetic or wording checks, 4 questions left open inside a source, 2 gaps to decide. The three with a primary document on one side: the Preissmann slot date (2018, not "around 2012"), the builders of SWMM 1 (Water Resources Engineers, not Camp Dresser & McKee), and the 54,060 speed ratio (the stated span gives 52,596).

No wiki page has been read by Bob yet; every page carries `reviewed: no`.

## [2026-11-14] setup | Published to GitHub

Pushed to https://github.com/dickinsonre/swmm-second-brain. The repository is public; Bob chose that over a private one after being told what it holds (working notes, unconfirmed findings, the thread list, the open questions). README and schema reworded from "private" to match.

## [2026-11-14] ingest | Second batch: the 13 SWMM6 translation READMEs

At Bob's say, the READMEs of the 32 public translation repositories under SWMMBobSWMM6 (19 SWMM5, 13 SWMM6) were copied into `raw/ports/` exactly as GitHub serves them, each named by the date of its repository's last commit. All 32 are public; none is a draft. This batch ingests the 13 SWMM6 ones (S23 to S35), for the themes "inside SWMM6" and "using AI to compare models"; the 19 SWMM5 ones stay queued for the next batch.

Each was read in full. Twelve follow one template, so the later ones were read as their differences from Go's (S24) and Kotlin's (S30). Pages created: 13 source pages; entities [SWMM6 language translations](wiki/entities/swmm6-language-ports.md), [swmm6-rust](wiki/entities/swmm6-rust.md), [1729-SWMM5-Models-2030 (the corpus)](wiki/entities/corpus-1729.md); concepts [Byte-for-byte gate](wiki/concepts/byte-for-byte-gate.md), [Matching glibc math in a translation](wiki/concepts/glibc-math-in-translation.md). Pages changed: OpenSWMM 6 and HydroCouple, Robert (Bob) Dickinson, the overview, open questions (Q20 to Q23), the index.

Every one of these READMEs was written by Claude, as each says; the counts rest on that text and on the gate records in the repositories. Contradiction found: Q20, S22's "no common test models" against the 480-model set used for both SWMM5 and SWMM6 translations (a tension rather than a clash of fact).
