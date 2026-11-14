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

## [2026-11-14] ingest | Third batch: the 19 SWMM5 translation READMEs

S36 to S54, the READMEs of the 19 swmm5-* repositories, for the themes "inside SWMM5" and "using AI to compare models". Each was read in full; after the first (S41, Go), each was read as the paragraphs it does not share with the ones before it, since the family repeats its parity contract, corpus note and gate commands word for word. Pages created: 19 source pages; entity [SWMM5 language translations](wiki/entities/swmm5-language-ports.md); concepts [What the gate cannot see](wiki/concepts/gate-blind-spots.md) and [Where languages part from C](wiki/concepts/where-languages-part-from-c.md). Pages changed: Byte-for-byte gate, Matching glibc math in a translation, 1729-SWMM5-Models-2030 (how the 480 were chosen, now answered), EPA SWMM 5, Lew Rossman, Robert (Bob) Dickinson, the overview, open questions (Q24 to Q28), the index.

The first six READMEs (6 November) do not say in their own text who wrote them; the later thirteen say Claude did. Contradiction found: Q24, the `%#g` case given as 999999.75 by two READMEs and 999999.5 by eight. The SWMM5 READMEs report EPA facts worth having beyond the ports: 1,524,961,124 math calls over the gate models, 43 models that change on glibc's generic routines, and the null and positive controls.

This makes three ingests; a lint read-through is due (schema: after every third ingest).

## [2026-11-14] lint | After the third ingest

`tools/lint.py`: 0 errors, 0 warnings (two orphan source pages, S36 and S37, were linked from the SWMM5 translations page). Read-through of the pages made today: no claim stated two ways across pages; the open items are Q20 to Q28, filed during the ingests. Arithmetic checked where the sources allow it, and it holds: 480 + 38 = 518 gate-folder models (S41); F#'s 1,785 + 551 = 2,336 returns and 85 + 1 = 86 continues (S48); R's 37,055 s against EPA's 91.4 s is 405 times, "about 400" (S54), and against Hy's 4,402 s is 8.4 times (S54); Ruby SWMM6's stopped runs, 42,334,342 of 78,975,850 bytes = 53.6 % and 17,545,557 of 155,158,965 = 11.3 % (S35); 336 + 116 = 452 extra decks (S29 against S23).
