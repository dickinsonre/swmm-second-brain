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

Bob asked to use the contents of `dickinsonre/swmm-brain`, which he plans to remove. All six files (commit 70348bb, 22 August 2026) were copied into `raw/swmm-brain/`, and the note template to `raw/notes/_TEMPLATE.md`. Two were renamed on the way in, because their original names would act on this repository: `CLAUDE.md` to `CLAUDE-swmm-brain.md` and `.gitignore` to `_gitignore.txt`. Sources S55 to S58 read in full. Pages created: 4 source pages, 3 concept pages (two-layer infiltration, a surrogate distilled from SWMM, app build contract), 2 entity pages (the old repository, Bob's GitHub repositories). Pages updated: dynamic wave routing, Preissmann slot, infiltration methods, RDII, version history, app quality markers, SWMM 5, EXTRAN, Robert Dickinson, overview, open questions.

Contradictions found: Q29 (Innovyze from 2005 or from 2008), additions to Q06 (first model run in 1974) and Q14 (Extran manual in 1981). Gap found: Q30, the two-layer source files the README describes are not in the repository.

## [2026-11-14] schema | raw/swmm-brain/ and templates

`CLAUDE.md` gains `raw/swmm-brain/` in the layout, and a rule that a file under `raw/` whose name starts with `_` is a template or a housekeeping copy, not a source; `tools/common.py` skips such files.

## [2026-11-14] lint | After the swmm-brain ingest

`tools/lint.py`: 0 errors. 21 open questions.

## [2026-11-14] schema | App summaries and versions

Bob asked for a rule that every app .md is added to `raw/apps/`, without piling up duplicates. `CLAUDE.md` gains the section "App summaries and versions": one file per released version, named `APPNAME-vVERSION.md`; never overwrite; the newest version of an app is the current one. `tools/manifest.py` now gives two more statuses: `superseded` (an older, never-ingested version of an app) and `duplicate` (a byte-identical file), and adds `app` and `version` columns. `tools/lint.py` warns when an app's newest summary is not the one ingested.

First run found 3 duplicates already in `raw/linkedin/`: LinkedIn's export held three articles twice. The queue is 223, not 226; counts on four pages corrected.

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

## [2026-11-14] setup | Bob's upload merged

While the third batch was being ingested, Bob uploaded 8 files to `raw/apps/` through GitHub (commit f6fac51): the 1729-SWMM5-Models-2030 README, Master SWMM PDF, PyBME issue drafts, extran3-workbench, inside-the-network-cfd, st-venant-solver-rosetta-stone, swmm1-runoff-engine (a newer copy) and under-load. The ingest commits were rebased onto his; the manifest now lists the 8 as queued (288 raw files, 54 ingested).

## [2026-11-14] setup | Branch `ingest-swmm-brain` merged into main

Three sessions worked on the repository at once on 14 November. While the swmm-brain branch was open, main gained S23 to S54 (the translation READMEs) and Q20 to Q28, and Bob uploaded 8 app files. To merge, the swmm-brain sources were renumbered S23 to S26 -> S55 to S58 and their questions Q20, Q21 -> Q29, Q30; the entries above that describe that ingest use the new numbers. Conflicts in `index.md`, `log.md`, `overview.md`, `open-questions.md` and two entity pages were resolved by keeping both sides. `CLAUDE.md` gains `raw/ports/` in the layout.

After the merge: 292 raw files, 58 ingested, 231 queued, 3 duplicate; 110 pages; 30 open questions; `tools/lint.py` 0 errors, 1 warning. The warning is the new version rule at work: Bob's upload `raw/apps/swmm1-runoff-engine (7).md` is SWMM 1 Engine 3.12, newer than the ingested 3.6 (S01), and is next in the queue.

Still unmerged: branch `ingest-topsoil-recovery-check` (another session), whose source page is numbered S23 and collides with main's S23; it needs renumbering to S59 before it can merge.

Lesson for the schema, not yet written into it: one session at a time should hold the next source number, or sessions should take numbers at merge time.

## [2026-11-14] setup | Primary documents added to raw/manuals/

Bob pointed to his repository `SWMMEnablement/SWMM_MD_Documents` (commit 6a6b317). Copied byte for byte into `raw/manuals/`: nine U.S. government reports as markdown (the SWMM 5.1 User's Manual, Reference Manual volumes II and III, the 2006 quality assurance report, the SWMM 3 User's Manual in two parts, the SWMM-CAT guide, a 1980 USGS report, FHWA HDS-5) and eleven text files of SWMM 4.4 block documentation. About 630,000 words. `raw/manuals/_SOURCE.md` lists each file and what was left in the source repository and why: a commercial textbook, a dissertation and a thesis, Innovyze and Autodesk product documentation, source code, and scanned PDFs.

## [2026-11-14] schema | Long documents

`CLAUDE.md` gains "Long documents": a manual is ingested a chapter at a time, its source page carries `coverage: partial` and `read: [...]`, and claims come only from the parts read. Equations in the converted manuals are not to be copied without checking the PDF. `tools/lint.py` reports how many long documents are read in part.

## [2026-11-14] ingest | S60, EPA Reference Manual Volume II, Hydraulics (in part)

Read in full: section 1.1 with Table 1-1, and Chapter 3, Dynamic Wave Analysis. Source number S60 (S59 is left for the unmerged Topsoil Recovery Check branch). Pages updated: dynamic wave routing (the six-step solution procedure, the stability devices), Preissmann slot and surcharge (how the EXTRAN-method surcharge works), reading SWMM output (flooding against ponding), continuity is not validation, version history (EPA's own table), EXTRAN, SWMM 1, Lew Rossman, overview.

Three open questions settled by this primary document and ticked: Q02 (SWMM I was built by Metcalf & Eddy, Water Resources Engineers and the University of Florida), Q12 (SWMM 5 is implicit in time, uncoupled in space; its predecessors were explicit) and Q14 (EXTRAN arrived with SWMM 3 in 1981). Two new ones: Q31 (first PC version: 1983 or 1988) and Q32 (SWMM 5 dated 2005 or October 2004).

`tools/lint.py`: 0 errors, 1 warning (SWMM 1 Engine 3.12 is queued behind the ingested 3.6). 29 questions open, 3 settled.

## [2026-11-14] ingest | S59, Topsoil Recovery Check app summary

Raw file added: `raw/apps/topsoil-recovery-check.md`, the technical summary that ships with the Topsoil Recovery Check page (version 2026-11-12), copied byte for byte from the delivered site folder in the Claude session that built the page. Read in full. Pages created: S59, [Topsoil over compacted clay](wiki/concepts/topsoil-over-compacted-clay.md), [LID bio-retention layers](wiki/concepts/lid-bioretention-layers.md), [Evaporation during rain (DRY_ONLY)](wiki/concepts/evaporation-during-rain.md), [Topsoil Recovery Check (app)](wiki/entities/topsoil-recovery-check.md), [swmm524-perched](wiki/entities/swmm524-perched.md). Pages changed: infiltration methods, continuity is not validation, findings register, EPA SWMM 5, OpenSWMM 6 and HydroCouple, OpenSWMM.org, the top 25 problems, SWMM 5 versus ICM, overview, open questions, index.

No contradiction with an earlier page. S59 gives the detail behind the `MODIFIED_HORTON` candidate in S03 (its defect D1). Open questions added: Q33 (register IDs for D1 and D2), Q34 (swmm524-perched license). The source names no person who raised the question, and neither does the wiki.

## [2026-11-14] setup | Branch `ingest-topsoil-recovery-check` merged into main

The Topsoil Recovery Check ingest, made in another session from the first commit, used S23 and Q20, Q21, which main had since given to other sources. Renumbered to S59, Q33 and Q34; the entry above that describes that ingest uses the new numbers. Conflicts in `index.md`, `log.md`, `overview.md`, `open-questions.md` and four pages resolved by keeping both sides.

One connection made at the merge: S59 shows that swmm524-perched implements a `SOIL2` layer, which partly answers Q30 (the two-layer code named in the old swmm-brain README). The rule differs from the README's, so Q30 stays open for the `UseAsInfil` design and the `lid_twolayer.c` files. Pages updated: two-layer infiltration, swmm524-perched, open questions.

After the merge: 313 raw files, 60 ingested, 250 queued, 3 duplicate; 117 pages; 31 questions open, 3 settled; `tools/lint.py` 0 errors, 1 warning (SWMM 1 Engine 3.12 queued behind 3.6). No branch is left unmerged.

## [2026-11-14] ingest | S61 to S64: two Lovable apps and the articles that announced them

Bob uploaded three files to `raw/apps/`. They are two apps. `cost-allocation-explorer-v1.0.1.md` is the Cost Allocation Game Theory Explorer. `rain-canvas-studio-v2026.1.2.md` and `Rules for Responsible Modeling lessons and browser drainage experiments.md` are one summary of Rules for Responsible Modeling, byte for byte the same. No summary of the rain-canvas-studio app itself is in `raw/apps/`.

Both summaries carry `file: rain-canvas-studio`. The cause is the prompt Claude gave Bob for Lovable on 14 November: its example front matter named that one project, and both projects copied it. With that line the manifest had marked the cost allocation summary `superseded`, as an older version of the other app. Raw files are not edited; the next version of each app should carry its own `file:` line (Q35).

Read in full and ingested: the two summaries (S61, S62) and the two queued LinkedIn articles on the same apps, Edition 53 of 23 February 2026 (S63) and the Heaney article of 8 March 2026 (S64). S62 is filed against the file named for the app; the misnamed copy is now `duplicate`.

Pages created: S61 to S64; [Cost Allocation Game Theory Explorer (app)](wiki/entities/cost-allocation-explorer.md), [Rules for Responsible Modeling (app)](wiki/entities/rules-for-responsible-modeling-app.md), [James P. (Jim) Heaney](wiki/entities/james-heaney.md), [William (Bill) James](wiki/entities/william-james.md); [Cost allocation by cooperative game theory](wiki/concepts/cost-allocation-methods.md), [Calibration, validation and uncertainty](wiki/concepts/calibration-validation-uncertainty.md). Pages changed: Robert Dickinson, Wayne Huber, version history, continuity is not validation, dynamic wave routing, EPA SWMM 5, subcatchment width, block architecture, OpenSWMM.org, overview, open questions, index, README.

Found at ingest. Seven open questions, Q35 to Q41: the shared `file:` line; a difference in S61's table larger than the largest it reports; "253 citations" beside a single paper with 144; review grades with no reviewer on record in either app; the SWMM build inside Rules for Responsible Modeling has no pinned source; "the model is never the problem" in S63 against the defects in the register; 1967 against 1969 for the start of the Florida work. Q31 gains a source: S63 has PCSWMM in use in 1983. Q19 gains S63 and S64. Arithmetic checked and found right: both test tables sum to their totals (101 and 61), the Three Towns saving, the tutorial rainfall depth and period count, and three Manning capacities.

Left out by page rule 9: family details and the memorial link in S64.

## [2026-11-14] schema | One `file:` line per app; tools

`CLAUDE.md`, "App summaries and versions", rule 4 now says what the `file:` line must be and what the tool does when two apps share one. `tools/manifest.py`: summaries that share `file:` but differ in `name:` are grouped by name, with a note; of byte-identical files the ingested copy is kept, else the shortest name. `tools/lint.py`: `%20` in a link is read as a space, so a source page can link a raw file whose name has spaces.

After this ingest: 316 raw files, 64 ingested, 248 queued, 4 duplicate; 127 pages; 38 questions open, 3 settled.
