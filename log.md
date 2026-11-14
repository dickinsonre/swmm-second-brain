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

## [2026-11-14] ingest | S23, Topsoil Recovery Check app summary

Raw file added: `raw/apps/topsoil-recovery-check.md`, the technical summary that ships with the Topsoil Recovery Check page (version 2026-11-12), copied byte for byte from the delivered site folder in the Claude session that built the page. Read in full. Pages created: S23, [Topsoil over compacted clay](wiki/concepts/topsoil-over-compacted-clay.md), [LID bio-retention layers](wiki/concepts/lid-bioretention-layers.md), [Evaporation during rain (DRY_ONLY)](wiki/concepts/evaporation-during-rain.md), [Topsoil Recovery Check (app)](wiki/entities/topsoil-recovery-check.md), [swmm524-perched](wiki/entities/swmm524-perched.md). Pages changed: infiltration methods, continuity is not validation, findings register, EPA SWMM 5, OpenSWMM 6 and HydroCouple, OpenSWMM.org, the top 25 problems, SWMM 5 versus ICM, overview, open questions, index.

No contradiction with an earlier page. S23 gives the detail behind the `MODIFIED_HORTON` candidate in S03 (its defect D1). Open questions added: Q20 (register IDs for D1 and D2), Q21 (swmm524-perched license). The source names no person who raised the question, and neither does the wiki.
