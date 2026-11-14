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

## [2026-11-14] ingest | The old swmm-brain repository: 4 sources

Bob asked to use the contents of `dickinsonre/swmm-brain`, which he plans to remove. All six files (commit 70348bb, 22 August 2026) were copied into `raw/swmm-brain/`, and the note template to `raw/notes/_TEMPLATE.md`. Two were renamed on the way in, because their original names would act on this repository: `CLAUDE.md` to `CLAUDE-swmm-brain.md` and `.gitignore` to `_gitignore.txt`. Sources S23 to S26 read in full. Pages created: 4 source pages, 3 concept pages (two-layer infiltration, a surrogate distilled from SWMM, app build contract), 2 entity pages (the old repository, Bob's GitHub repositories). Pages updated: dynamic wave routing, Preissmann slot, infiltration methods, RDII, version history, app quality markers, SWMM 5, EXTRAN, Robert Dickinson, overview, open questions.

Contradictions found: Q20 (Innovyze from 2005 or from 2008), additions to Q06 (first model run in 1974) and Q14 (Extran manual in 1981). Gap found: Q21, the two-layer source files the README describes are not in the repository.

## [2026-11-14] schema | raw/swmm-brain/ and templates

`CLAUDE.md` gains `raw/swmm-brain/` in the layout, and a rule that a file under `raw/` whose name starts with `_` is a template or a housekeeping copy, not a source; `tools/common.py` skips such files.

## [2026-11-14] lint | After the swmm-brain ingest

`tools/lint.py`: 0 errors. 21 open questions.
