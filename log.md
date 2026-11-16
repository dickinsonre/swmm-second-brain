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

## [2026-11-14] ingest | S65, S66: World Rainfall Pattern Painter

A raw file was changed, by Bob. At 16:19 on 14 November he replaced the content of `raw/apps/rain-canvas-studio-v2026.1.2.md` on GitHub (commit fc42e96) with the World Rainfall Pattern Painter summary, version 3.2.0. Until then the file was a byte-identical second copy of the Rules for Responsible Modeling summary, marked `duplicate` and cited by no page, so nothing in the wiki rested on the old content, and that content survives in the file S62 cites. `tools/manifest.py` reports the change once and records the new hash. The file name still says v2026.1.2, another app's version; raw files are not renamed, so the name stays and the source page says so.

Read in full and ingested: that summary (S65) and the queued LinkedIn article that announced the app on 25 February 2026 (S66). Pages created: S65, S66, [World Rainfall Pattern Painter (app)](wiki/entities/world-rainfall-pattern-painter.md), [Design storms and temporal patterns](wiki/concepts/design-storm-patterns.md). Pages changed: continuity is not validation, InfoWorks ICM, the two other Lovable app pages, S62, overview, open questions, index, README.

Found at ingest. Q42: the article lists HEC-HMS export as coming; the app's change list dates it three months earlier. Q43: two oddities in the climate uplift table, and no factor checked against published guidance. Q35, Q38 and Q19 extended. Arithmetic checked and found right: 19 test files sum to 1,502; 3 + 57 + 279 = 339; 1,017 and 9,153 are 339 times 3 and 27; the credits table has 37 rows.

Noted for the next lint: the Robert Dickinson page is about 790 words, past the 600-word rule, and should be split.

After this ingest: 316 raw files, 66 ingested, 247 queued, 3 duplicate; 131 pages; 40 questions open, 3 settled.

## [2026-11-14] ingest | S67, Bob's first note on the template: Green-Ampt Newton test order

Bob uploaded `raw/notes/green-ampt-newton-test-order.md`, written on `raw/notes/_TEMPLATE.md`. Read in full. Its AI-use line says Claude drafted it from test runs Claude made in a chat with Bob, and that the runs have not been rerun; its status line reads "working". The wiki uses that status and upgrades nothing.

Pages created: S67 and [Green-Ampt Newton test order](wiki/concepts/green-ampt-newton-test-order.md). Pages changed: infiltration methods, continuity is not validation (a fifth case), the findings register, EPA SWMM 5, overview, open questions, index, README.

Checked at ingest. The ten quoted lines of `grnampt_getF2` were compared with `src/solver/infil.c` at tag v5.2.4 in USEPA/Stormwater-Management-Model, fetched on 14 November 2026: identical, at lines 847 to 856 as the note says. The note's threshold of 0.432 follows from those lines, and its two break points (F above 0.67 in at 15 s, above 2.86 in at 30 s) follow from the threshold. None of the run results was checked: the test `.inp`, the patch and the longer write-up the note links to are not in the repository (Q44).

After this ingest: 317 raw files, 67 ingested, 247 queued, 3 duplicate; 133 pages; 41 questions open, 3 settled.

## [2026-11-14] setup | App summaries pulled from the apps themselves (Netlify batch 1)

Bob gave six Netlify names and addresses and asked for their .md files. They are five apps. Each address was checked against his Netlify account and each app's source was read from his published Claude artifact.

| Netlify site | App | What went into `raw/apps/` |
|---|---|---|
| swmm5-code-house | SWMM5 Code House | `swmm5-code-house-v1.15.1.md`, extracted from the page's `script#app-md` |
| heartfelt-daffodil-ca3a6a | a second copy of SWMM5 Code House | nothing; same app |
| swmm6-code-house | SWMM6 Code House | `swmm6-code-house-v1.2.1.md`, extracted |
| swmm-app-complexity-vs-hydrocouple | SWMM App Complexity Meter | nothing; the embedded summary equals `swmm-app-complexity-meter.md` (S02) but for one leading blank line |
| swmm5-engine-what-if | SWMM Engine What If | `swmm-engine-what-if-v1.4.md`, extracted |
| nine-swmm5-engines-not-c | SWMM Engines, Byte for Byte | `swmm-engines-v2026-11-06.md`, written by Claude from the page |

Three files are byte-for-byte copies of what the apps carry. The fourth is new writing: the Byte for Byte page ships no summary, so Claude wrote one from the page's About tab and its embedded results object, with every number read from that object by script and nothing rerun. Its front matter and its source page say so, and Bob has been asked to read it (Q49).

All five public sites serve older builds than these summaries describe (Q45). A plain download of a Netlify address from the workspace failed; the pages were read through the web fetch tool, which sees the page source and not what scripts change.

## [2026-11-14] ingest | S68 to S72: the Code Houses, Engine What If, Byte for Byte

Read in full and ingested: the four summaries above (S68 to S71) and the queued LinkedIn article on the SWMM6 Code House of 4 November 2026 (S72). Pages created: S68 to S72; [SWMM5 Code House (app)](wiki/entities/swmm5-code-house.md), [SWMM6 Code House (app)](wiki/entities/swmm6-code-house.md), [SWMM Engine What If (app)](wiki/entities/swmm-engine-what-if.md), [SWMM Engines, Byte for Byte (app)](wiki/entities/swmm-engines-byte-for-byte.md); [Wrap, translate or extend](wiki/concepts/wrap-translate-or-extend.md), [SWMM5 translations: the re-run of 12 November 2026](wiki/concepts/swmm5-ports-rerun-2026-11.md). Pages changed: both translation pages, glibc math, byte-for-byte gate, where languages part from C, reading SWMM output, EPA SWMM 5, OpenSWMM 6 and HydroCouple, swmm524-perched, Lew Rossman, the findings register, overview, open questions, index, README.

What the batch added to the synthesis. The translations page rested on each repository's own README; S70 is one session that rebuilt twenty of them and timed them together, which narrows Q27 to R and to long models. S71 and S72 add findings from reading and translating the engines: five numbered EPA 5.2.4 defects, a possible culvert defect, and 20 reading notes on OpenSWMM 6 that their own source calls hypotheses (Q47).

Found at ingest. Q46: the size of the 5.2.4 solver is given as 51,080 and 50,788 lines and as 969, 962 and 968 functions. Q48: the What If app's list of empty repositories is older than two READMEs already here. Arithmetic checked and found right: the 28 test scripts of S68, the 376 checks of S69, 21 x 7 x 2 = 294 in S70, and 351,187 / 51,080 = 6.9 for "about seven times".

After this ingest: 321 raw files, 72 ingested, 246 queued, 3 duplicate; 144 pages; 46 questions open, 3 settled.

## [2026-11-14] setup | The 75-site Netlify list: triage, and four more summaries queued

Bob sent the 75 sites on the first page of his Netlify account. For the 31 that match a published Claude artifact by name, the page was read and searched for an embedded summary (`script#app-md`).

Added to `raw/apps/`, byte for byte from the pages, and left queued: `swmm1-runoff-engine-v3.13.md` (so 3.12, never ingested, is now `superseded`), `swmm-icm-knowledge-library-v70.md`, `bob-usefulness-index-v2.2.md`, `fractal-swmm-generator-v2.3.md`. Three more embedded summaries (EXTRAN III Workbench 1.6.0, Under Load 1.4.0, Speak 100) are identical to files already queued here, so nothing was added for them.

Twenty apps have a readable page and no summary inside; about forty-four have no artifact that matches by name, and their Netlify pages cannot be downloaded from this workspace (the proxy refuses the host). Nothing was written for either group in this step.

After this step: 325 raw files, 72 ingested, 249 queued, 1 superseded, 3 duplicate.

## [2026-11-14] setup | Branch `ingest-netlify-batch-1` merged into main

While the branch was open, Bob marked two pages reviewed on main (App build contract, App complexity index: `reviewed: 2026-11-14`) and uploaded `raw/apps/swmm-icm-knowledge-library.md`. His upload is byte-identical to the `swmm-icm-knowledge-library-v70.md` extracted on the branch, so the branch's copy was dropped before the merge and his file is the one kept. No conflict.

After the merge: 325 raw files, 72 ingested, 249 queued, 1 superseded, 3 duplicate; 144 pages, 2 of them reviewed by Bob; 46 questions open, 3 settled.

## [2026-11-14] setup | Five app summaries written from page source (not ingested)

Bob asked for summaries of five apps whose pages carry none. Claude wrote one file for each from the published artifact's page source and embedded records, in the form of `swmm-engines-v2026-11-06.md`. No engine was run and nothing was rerun. Each file says so in its front matter (`written_from:`) and under "What this does not show".

Added to `raw/apps/`, all queued:
- `mirab-test-bench-v1.0.md` (app dated 2026-10-24)
- `teacher-forced-swmm-v1.0.md` (2026-10-25)
- `control-section-lab-v1.2.md` (2026-10-18)
- `bellinge-v2.0.md` (2026-10-18)
- `people-as-pollutants-v1.0.0.md` (2026-10-29)

In these five the `date:` line is the app's own build date and a new `written:` line gives the day the summary was written. The earlier written summary (`swmm-engines-v2026-11-06.md`) put the writing date in `date:`; it is left as it is.

Checked before commit: every number in the five files was searched for in its page's source. The only numbers not found are unit conversions made by the summaries (feet from meters, inches from mm), which each file's `units:` line declares.

Noted while writing, for the ingest: the Bellinge essay's byline reads "Robert Dickinson, with Claude"; its section 9 cites Table 3 for numbers that are in Table 4; its test table is dated 19 October 2026 against a build record of 18 October. Each app keeps its own finding IDs (S, C, M, P; R and D; F1 to F9; D-1 to D-3), none mapped to the findings register. The Netlify pages of the five were not read.

After this step: 330 raw files, 72 ingested, 254 queued, 1 superseded, 3 duplicate. Wiki pages unchanged at 144.

## [2026-11-15] ingest | Sixteen app files and one note: S73 to S89

Bob said "ingest the app summaries". Sixteen of the seventeen queued files in `raw/apps/` were read in full and ingested, SWMM 1 Engine v3.13 first. One note was added and ingested in the same pass.

Sources written: S73 SWMM 1 Engine v3.13 (S01, for v3.6, now carries `superseded_by: S73`); S74 EXTRAN III Workbench v1.6.0; S75 St. Venant Solver Rosetta Stone v2.4.0; S76 Inside the Network v1.1.0; S77 Under Load v1.4.0; S78 Fractal SWMM5/SWMM6 Network Generator v2.3; S79 to S83, the five summaries Claude wrote from app pages on 14 November (Teacher-Forced SWMM, Control Section Lab, Bellinge, Mirab Test Bench, People as Pollutants); S84 SWMM & ICM Knowledge Library v70; S85 Bob Usefulness Index v2.2; S86 Master SWMM PDF (page text, not a summary); S87 the corpus README; S88 Speak 100; S89 a note on the corpus name.

Not ingested, on purpose: `raw/apps/PyBME-issue-drafts.md`. It is not an app summary; it holds fourteen draft issues about another person's library. Left queued for Bob to decide (Q56).

The note. While the ingest ran, Bob answered the corpus page's line "Not in the sources. What 1729 and 2030 stand for." Claude filed his answer as `raw/notes/corpus-name-1729-2030.md` on the note template, in his words, and ingested it as S89. One family detail in his message was left out of the public repository; Bob confirmed that, and ruled that his age may be given where it is the point and that family members' names never appear.

Pages created (21). Entities: EXTRAN III Workbench, St. Venant Solver Rosetta Stone, Inside the Network, Under Load, Fractal SWMM5/SWMM6 Network Generator, Teacher-Forced SWMM, Control Section Lab, Bellinge, Mirab Test Bench, People as Pollutants, SWMM & ICM Knowledge Library, Bob Usefulness Index, Master SWMM PDF, Speak 100. Concepts: EXTRAN's three solvers (XROUTE, YROUTE, ZROUTE); The crown cap at mid-pipe; OpenSWMM 6 solvers, measured; Hot start: what a restart loses; Run duration floored to whole seconds; WebAssembly builds against native builds; Converting SWMM 5 models for older engines.

Pages changed (25, with the overview, the open questions, the index and the README besides). Rewritten: SWMM 1 Engine (app). Entities added to: EXTRAN, the corpus, SWMM 1, EPA SWMM 5, OpenSWMM 6 and HydroCouple, OpenSWMM.org, swmm5.org, SWMM App Complexity Meter, SWMM5 Code House, SWMM and ICM St. Venant comparison, SWMM Engines Byte for Byte, Robert (Bob) Dickinson, Wayne C. Huber. Concepts added to, each with one paragraph headed "Added 15 November 2026": Verification against printed runs, App complexity index, The SWMM findings register, Dynamic wave routing, Preissmann slot and surcharge, Continuity is not validation, Reading SWMM output, Matching glibc math in a translation, What the gate cannot see, SWMM version history, SWMM 5 versus ICM InfoWorks.

Those eleven concept pages had been reviewed by Bob on 14 and 15 November. His `reviewed:` dates are kept, and each page now carries `changed_after_review:` in its front matter.

Schema changes (CLAUDE.md), each made in this ingest:
- A page changed after Bob's review keeps its `reviewed:` date, gets the new text under "Added <date>", and gets a `changed_after_review:` line. `tools/lint.py` now lists such pages.
- Page rule 9: Bob's age may be given where it is the point; family members' names never appear.
- App rule 6: a summary the agent writes from an app's page carries `written_from:` and stays an open question until Bob reads it.
- What not to do: an answer Bob gives in a session is filed as a note in `raw/notes/` and ingested, not written straight into a page.

Contradictions and checks:
- Q50, new, part settled by a lookup: the Rosetta Stone's "EPA SWMM 5.2.4" is commit 07c371f. `git ls-remote` against the USEPA repository on 15 November 2026 shows that is the head of branch develop; tag v5.2.4 is 7952ca8, which four other sources use.
- Q51, new: the EXTRAN III converter ran 259 corpus models (S05) or 257 (S74), from a repository named differently from the corpus page's.
- Q54, new: 1,327 swmm5.org posts (S84) against 1,700 or more (S22).
- Q57, new: three different SWMM 5 files stand for EXTRAN Example 1 in three sources, with 114,824 and 114,210 ft3 of flooding in two of them.
- Q55, new: two apps report unexplained browser-against-native differences that the Mirab bench's glibc-against-musl result may explain; neither was rerun.
- Q52, Q53, Q56, Q58, Q59, new: five Claude-written summaries for Bob to read; small faults in app pages (among them an essay byline "Robert Dickinson, with Claude"); the PyBME file; what the complexity scale's anchor includes; four pages past the length limit.
- Extended: Q16, Q17 (the 1988 manual's second printing is dated October 1992), Q18, Q38, Q47 (six more sets of app findings with colliding IDs), Q48.
- Two findings met independently by two sources each: the run-duration floor in `project.c` (S76 and S79), and the 260-byte path buffer in `swmm5.c` (S71 and S82).

Arithmetic checked at ingest is recorded on each source page. Numbers on the new pages were searched for in the raw files they cite; what was not found is arithmetic or a conversion marked as ours.

After this ingest: 331 raw files, 89 ingested, 238 queued, 1 superseded, 3 duplicate. 182 wiki pages: 89 sources, 45 concepts, 46 entities, overview, open questions. 56 questions open, 3 settled. 38 pages reviewed by Bob, 11 of them changed since.

## [2026-11-15] setup | Main merged into the ingest branch

While the ingest ran, Bob marked 30 more pages reviewed on main: 25 entity pages, the overview, the open questions and three source pages. Main was merged into the branch with no conflict. Eleven of those pages are also changed by this ingest (EXTRAN, the corpus, OpenSWMM 6 and HydroCouple, OpenSWMM.org, Robert (Bob) Dickinson, the SWMM and ICM St. Venant comparison, swmm5.org, Wayne C. Huber, the overview, the open questions, and S01's front matter). Bob's dates are kept, and each carries a `changed_after_review:` line naming the paragraphs that are new.

After the merge: 68 of 182 pages reviewed by Bob, 22 of them changed since his review; 114 not yet reviewed.

## [2026-11-15] setup | Branch `ingest-app-summaries` merged into main

Before the merge Bob marked more pages reviewed on main, most of the source pages among them. Main was merged into the branch a second time with no conflict. Three more pages he had reviewed are changed by the ingest (SWMM 1 Engine (app), which is rewritten for version 3.13; EPA SWMM 5; SWMM App Complexity Meter) and now carry `changed_after_review:`.

After the merge: 182 wiki pages, 141 reviewed by Bob, 25 of those changed since his review, 41 not yet reviewed. 331 raw files, 89 ingested, 238 queued. 56 questions open, 3 settled.

## [2026-11-15] ingest | S60 continued: Chapters 2, 4 and 6 of the EPA hydraulics manual

"Ingest the next batch", taken as item 0 of the suggested order in `index.md`: the EPA hydraulics manual, a chapter at a time. Read in full, from `raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md`: Chapter 2 (the hydraulic model), Chapter 4 (kinematic wave) and Chapter 6 (pumps and regulators), about 12,900 words. Chapters 2 and 4 were taken in order; Chapter 6 was taken ahead of 5 because it is prose and procedure, and Chapter 5 is mostly geometry tables. Still unread: sections 1.2 to 1.5, Chapter 5, Chapter 7 and the appendices. S60 stays `coverage: partial`. No raw file changed status.

Pages created (4, all `reviewed: no`): SWMM 5 network objects, boundary and initial conditions; Pumps and pump curves; Orifices; Weirs and outlets. A single regulators page came to 764 words and was split in two before it was kept.

Pages changed (6, all reviewed by Bob, each now marked `changed_after_review:`): S60 (read list, coverage, 31 new claims, feeds); Kinematic wave and steady flow routing (one added section); Dynamic wave routing (one added sentence of links; the page was already over length, Q59); the overview (one bullet, raw count); open questions; plus `index.md` and the state lines of `README.md`, which still said 46 questions and no page reviewed.

Found:
- Q60, new: the raw file lacks pages 64 to 66 (the end of section 4.1 and all of 4.2, the kinematic wave solution method) and page 122 (section 6.3.6 and four steps of the weir summary). The page numbers in the converted text jump. Nothing in the wiki rests on the missing pages.
- Q61, new: Bob's article says kinematic wave hydrographs are attenuated (S17); the manual says "no attenuation" in section 2.2 and Table 2-1, and "a very modest attenuation" from numerical diffusion in section 4.4.
- Q62, new: section 6.1 says a pump's flow stays within its curve, and also that a pump on a non-storage node that would go dry is set to the node's inflow. It does not say which holds when the inflow is above the curve.
- Q63, new: three wording slips in the converted text (an equation number in the storage-node side bar, "weirs" for orifices in 6.2.6, an equation number in 6.3.2), to check against the PDF.
- Arithmetic checked: the constants of the pump energy equation (0.7457 and 8.814) are kilowatts per horsepower and 550/62.4. Equations are otherwise described in words, by rule 4 for long documents.

Also added to `raw/apps/`, under the app-version rule and not ingested: `st-venant-solver-rosetta-stone-v2.6.2.md`, the summary of the version delivered on 14 November 2026 (S75 holds version 2.4.0). It describes a pump test deck that bears on Q62.

After this ingest: 332 raw files, 89 ingested, 239 queued, 1 superseded, 3 duplicate. 186 wiki pages: 89 sources, 49 concepts, 46 entities, overview, open questions. 60 questions open, 3 settled. 4 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-hydraulics-ch2-4-6`.

## [2026-11-15] setup | Branch `ingest-hydraulics-ch2-4-6` merged into main

Bob said "merge". Main had not moved since the branch was cut at 97806db, so there was nothing to reconcile. After the merge: 186 wiki pages, 4 of them not yet reviewed by Bob (the four new concept pages), 27 changed since his review. 332 raw files, 89 ingested, 239 queued. 60 questions open, 3 settled.

## [2026-11-15] ingest | S90, SWMM anecdotes from the comments on a LinkedIn post

Bob pasted the comment thread under one of his LinkedIn posts and said it might be good to add as anecdotes of SWMM. Claude typed `raw/notes/swmm-anecdotes-linkedin-comments-2026-11.md` from the paste: Bob's four comments, and the sentences of seven other people that recall SWMM or their own modeling work, word for word under the names they were posted under. Left out because the repository is public: comments that only congratulate, remarks about anyone's family or private life, job titles, reaction counts. The post itself was not in the paste.

Pages created (2, `reviewed: no`): S90; Anecdotes of SWMM, a concept page under History meant to collect more of these. Pages changed: Robert (Bob) Dickinson (one added paragraph; already marked changed after review), the overview (one bullet, counts), open questions, `index.md`, `README.md`.

Found:
- Q06, extended: the LinkedIn headline says "SWMM since the 1977", one more start date.
- Q64, new: the note waits for Bob's read; the post, the year of the Australian stay for the XP-EXTRAN update, and what the "double pipes" were are not in the sources; and whether other people's quoted comments should stay is his to decide.
- No contradiction with an existing page. The wiki had nothing on John Haestad, Jack Cook, Canberra, the Prime mainframe, the phosphate plant or DUFLOW before this note.

After this ingest: 333 raw files, 90 ingested, 239 queued, 1 superseded, 3 duplicate. 188 wiki pages: 90 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 3 settled. 6 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-swmm-anecdotes`.

## [2026-11-15] setup | Branch `ingest-swmm-anecdotes` merged into main

Bob said "merge". Main had not moved since `5b20417`, so the merge is a fast-forward. It brings in S90, the Anecdotes of SWMM page, the addition to the Robert Dickinson page, the extension of Q06 and the new Q64. Nothing else changed. Q64 stays open: the post's text, date and link, the year of the Australian stay, and what the "double pipes" were.

## [2026-11-15] ingest | S91, Bob's answers to Q64

Bob answered the three gaps of Q64 in a Claude session. Claude copied his answers into `raw/notes/q64-answers-canberra-barrels-post-link.md` in his words and ingested the note. The post is https://lnkd.in/p/e8TVNFQZ, "from yesterday" (14 November 2026). The stay in Canberra ran "from november 1991 to december 1992". "double pipes are called barrels in swmm5 - i guess i added them to swmm4".

Page created (1, `reviewed: no`): S91. Pages changed: Anecdotes of SWMM, Robert (Bob) Dickinson (the paragraph added earlier today extended; its wording "to SWMM 3" corrected, because S90 does not say which version the double pipes went into), S90 (one pointer to S91), the overview (one bullet extended, counts; its stale count of open items corrected from fifty-nine to sixty-two), open questions, `index.md`, `README.md`.

Found:
- Q64, settled in part, not ticked. Still open: the text of the post (LinkedIn refused an automated fetch), whether "XSWMM" is XP-SWMM, and Bob's read of both notes.
- Q65, new, under "Sources that disagree": Weaver's comment places the double pipes in the SWMM 3 years; Bob guesses SWMM 4. A text search of the queued manuals finds a BARREL field in the Transport Block card data of the SWMM 3 manual and in SWMM 4.4 TRANS.doc, and no "barrel" in EXTRAN44.doc. Those files are not ingested, so the search is recorded in Q65 as a pointer and not as a wiki claim.
- Checked: November 1991 to December 1992 is 13 to 14 months, against "one year" in S90. Not a conflict.

After this ingest: 334 raw files, 91 ingested, 239 queued, 1 superseded, 3 duplicate. 189 wiki pages: 91 sources, 50 concepts, 46 entities, overview, open questions. 62 questions open, 3 settled. 7 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S92, Bob's answer to Q65

Shown what the text search of the queued manuals had found, Bob answered: "transport is not extran so barrels were added later =- not a big matter". Claude copied it into `raw/notes/barrels-transport-is-not-extran.md` in his words and ingested the note.

Page created (1, `reviewed: no`): S92. Pages changed: Anecdotes of SWMM, open questions, the overview (counts), `index.md`, `README.md`.

Q65 ticked, on Bob's word: the BARREL field of the SWMM 3 Transport block is not the double pipes of the anecdote; those were barrels in Extran, added later. The version stays his guess of SWMM 4 (page rule 5: a guess is not upgraded).

After this ingest: 335 raw files, 92 ingested, 239 queued, 1 superseded, 3 duplicate. 190 wiki pages: 92 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 4 settled. 8 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S93, the name XP-SWMM and its change to XPSWMM in 1993

Bob typed: "xp-swmm was the original and we changed it to xpswmm in 1993". Claude copied it into `raw/notes/xp-swmm-renamed-xpswmm-1993.md` in his words and ingested the note.

Page created (1, `reviewed: no`): S93. Pages changed: Anecdotes of SWMM (one sentence; two sentences cut to keep the page under 600 words), Robert (Bob) Dickinson (one sentence in the paragraph added today), open questions (Q64 extended), the overview (counts), `index.md`, `README.md`.

Q64 stays open for two things: the text of the LinkedIn post, and Bob's read of the four notes Claude typed today (S90 to S93). That "XSWMM" in his comment is this program is Claude's reading of his answer, and is marked so.

Checked: his 2016 article (S11) writes both "XP-SWMM" and "XPSWMM"; no other source dates the change.

After this ingest: 336 raw files, 93 ingested, 239 queued, 1 superseded, 3 duplicate. 191 wiki pages: 93 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 4 settled. 9 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S94, Bob's LinkedIn post of 14 November 2026

Bob pasted the text of the post that the comments in S90 answer. It is a post, not an article, so it was not in the LinkedIn export. Claude copied the paste into `raw/linkedin/2026-11-14-post-my-earlier-history-with-swmm.md` without changing a word and ingested it. The file holds the post as Bob published it. By page rule 9 the wiki carries only what bears on SWMM: he learned about SWMM at 17, started working on it at 22, and "SWMM 2.5 was 20,000 punch cards".

Page created (1, `reviewed: no`): S94. Pages changed: Anecdotes of SWMM (one anecdote added, five sentences cut to keep the page near 600 words), Robert (Bob) Dickinson (one sentence in the paragraph added today), open questions, the overview (one bullet, counts), `index.md`, `README.md`.

Found:
- Q64 ticked, on Bob's answers and the post itself. His read of S90 to S94 is tracked by `reviewed: no`.
- Q06 extended: age 22, with "75 in 2030" from S89, puts his start on SWMM between 1976 and 1978.
- Q66, new: 20,000 cards for SWMM 2.5 (S94) against ten boxes for SWMM 2.5 and SWMM 3 together (S19). No source gives cards per box.

After this ingest: 337 raw files, 94 ingested, 239 queued, 1 superseded, 3 duplicate. 192 wiki pages: 94 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 5 settled. 10 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | The post corrected ("Since"), and S95, a box held 2,000 cards

Two answers from Bob.

"ince should be since". Raw files are never edited, so the corrected text went in beside the first file as `raw/linkedin/2026-11-14-post-my-earlier-history-with-swmm-corrected.md`, with that one letter restored and its own account of how it was made. S94 now names the corrected file as its raw file. The as-pasted file stays, is listed as queued, and is not to be ingested; `index.md` says so.

"i remember it was 2000 - i remember as it was importat", on how many cards a box held. Claude copied it into `raw/notes/punch-card-box-held-2000-cards.md` in his words and ingested it.

Page created (1, `reviewed: no`): S95. Pages changed: S94, Anecdotes of SWMM, open questions, the overview (counts), `index.md`, `README.md`.

Found:
- Q66 ticked, on Bob's word: ten boxes of 2,000 cards are 20,000 cards, so his post (S94) and his 2024 article (S19) agree.
- A slip of Claude's corrected: S94 and Q66 had the article saying the two programs "together filled" ten boxes. The article's words are "SWMM 2.5 and SWMM 3 were in ten boxes".

After this ingest: 339 raw files, 95 ingested, 240 queued (one of them the as-pasted post, kept on purpose), 1 superseded, 3 duplicate. 193 wiki pages: 95 sources, 50 concepts, 46 entities, overview, open questions. 60 questions open, 6 settled. 11 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] setup | Bob's decision on the post in `raw/`

Asked whether the full text of his post of 14 November 2026, including what it says about his family, should sit in this public repository's `raw/` folder, Bob answered: "all public". The post stays in `raw/` as he published it. Page rule 9 is unchanged: the wiki still carries only what bears on SWMM.

## [2026-11-15] setup | Branch `ingest-q64-answers` merged into main

Bob said "merge". Main had moved: between 8:27 and 8:30 that morning Bob marked six pages reviewed (Orifices, Pumps and pump curves, Weirs and outlets, SWMM 5 network objects, Anecdotes of SWMM, S90) and cleared the `changed_after_review:` line on 27 pages. His commits were merged into the branch first, then main was fast-forwarded.

Three conflicts, all in front matter, all resolved the same way: his `reviewed:` dates kept, and a new `changed_after_review:` line listing only what the branch changed after his review. Five reviewed pages carry such a line: Anecdotes of SWMM, S90, Robert (Bob) Dickinson, open questions, the overview. On the Anecdotes page the changes are in place, not in a separate "Added" paragraph, because the page was `reviewed: no` when they were written; the line lists each one.

The merge brings in S91 to S95, the corrected copy of the post beside the as-pasted one, and the ticks on Q64, Q65 and Q66.

After the merge: 339 raw files, 95 ingested, 240 queued (one of them the as-pasted post, kept on purpose), 1 superseded, 3 duplicate. 193 wiki pages. 60 questions open, 6 settled. 5 pages not yet reviewed (S91 to S95); 5 changed since Bob's review.

## [2026-11-15] raw | 17 app summaries brought over from Bob's Replit workspace

Bob ran the summary prompt in Replit Agent on his projects and could not download the files. At his request the agent read each file out of the Replit editor through his browser and wrote it to `raw/apps/`. Each copy was checked against a SHA-256 computed inside Replit on the editor's text: all 17 match, and those hashes are the ones in `raw/MANIFEST.csv`.
Files: bob-swmm-info-v1.0.0, data-importer-robertdickinson-v1.0.0, fractal-swmm-gen--robertdickinson-v1.0.0, green-infiltration-v1.0.0, horton-model--robertdickinson-v1.0.0, singa-pour-site-v1.0.0, spatial-impact-insight-v2.4.1_b, swmm-5-inp-reader-robertdickinson-v0.1.0, swmm-filebase--robertdickinson-v1.0.0, swmm-inp-maker-v1.0.0, swmm-lego-model-v0.0.0, swmm-manual-search-robertdickinson-v5.2, swmm-pilot-robertdickinson-v1.0.0, swmm-ui-engine-v1.0.0, temp-monitor-1-v1.0.0, video-search-v1.0.0, xps-to-shape--robertdickinson-v0.1.0.
Every one says in its body that Replit Agent wrote it on 15 November 2026 and that Bob has not reviewed it. None is ingested yet; all are queued.
Held back, not committed: sewer-code-search-v1.0.0 (the app is a private deployment; waiting for Bob's say before it goes into a public repository).
No summary found in two projects, where Replit Agent stopped and asked to switch to its paid Power mode: EPANET SWMM Experts and SWMM Explorer.

## [2026-11-15] raw | sewer-code-search-v1.0.0 added on Bob's say

Bob was asked whether the Sewer Code Search summary, held back on 15 November because the app is a private deployment, should go into the public repository. He answered yes. The file is now in `raw/apps/`, queued. Its SHA-256 matches the one computed inside Replit (e4ee62fd...d0bc). That makes 18 Replit summaries in this batch.

## [2026-11-15] ingest | Eighteen Replit app summaries, S96 to S113

Bob said "ingest" for the batch brought over from Replit earlier in the day. Each file was read in full.
Sources written: S96 SWMM5-UI, S97 SWMM5 Network Miner, S98 SWMM5 INP MAKER, S99 SWMM5 Lego Model, S100 Camel_SWMM, S101 SWMM5 Manual Search, S102 the SWMM Manual Search landing page, S103 InfoSewer and InfoSWMM Legacy Model Reader, S104 XPX to Shapefile Converter, S105 SWMM5 .inp File Viewer, S106 SWMM5 Topology Sandbox, S107 Green-Ampt Infiltration Calculator, S108 SWMM5 Runoff and Infiltration App, S109 SingaPourApps, S110 InfoDrainage Explorer, S111 MapSWMMSewer - Code Repository, S112 City Temperature Explorer, S113 GeoAI Flood Impact.
Replit project each file came from, as seen in Replit (the files do not carry this name): S96 Swmm UI Engine, S97 SWMM Filebase, S98 SWMM INP Maker, S99 SWMM Lego Model, S100 Swmm5AppEngine, S101 SJ_SWMM5_Manual_Search, S102 Video Search, S103 InfoSWMM-InfoSewer-Reader, S104 XpsToShape, S105 SWMM5InpReader, S106 Fractal SWMMGen, S107 Green Infiltration, S108 SWMM5RunoffInfiltration, S109 SingaPour Site, S110 InfoDrainage Explorer, S111 Sewer Code Search, S112 Temp Monitor, S113 Spatial Impact Insight.
Pages created: 18 app pages under `wiki/entities/` and one concept page, Replit apps and the summaries Replit Agent wrote.
Pages changed, each with one paragraph headed "Added 15 November 2026" and a `changed_after_review` line: InfoSWMM and InfoSewer (S103 names tables inside an ISDB model, which the page had listed as not in the sources), Fractal SWMM5/SWMM6 Network Generator (S106), Infiltration methods (S107, S108), Bob's GitHub repositories (four repositories). The overview got one bullet and new counts; the README and index were updated.
Open questions added: Q67 (none of the eighteen has been read by Bob), Q68 (dates and versions that are not release facts), Q69 (faults Replit Agent reported, none rerun), Q70 (names), Q71 (which AI built each app), Q72 (engine provenance not recorded), Q73 (two generators with 22 patterns).
Checked at ingest: every number on the new pages was searched for in the raw file it cites; the counts on the concept page (12 with no engine, 14 with no repository, 8 dated with the summary date, 18 with no human review) were counted from the front matter and bodies. In two files the `file:` line is shorter than the site name in `links:` (green-infiltration, singa-pour-site).
Tools: `tools/lint.py` now prints source numbers of any length (it cut S100 to "S10").
Correction: the log entry for the Sewer Code Search summary was first dated 16 November by mistake; it is 15 November.
Not ingested, still queued in `raw/apps/`: st-venant-solver-rosetta-stone-v2.6.2 and PyBME-issue-drafts (Q56).

## [2026-11-15] setup | Main merged into `replit-summaries`; a zip is now in `raw/apps/`

While the ingest ran, Bob uploaded the same 18 summaries to `raw/apps/` on main, together with `replit-app-summaries.zip`, the bundle the agent had sent him. The 18 files are byte-identical to the ones already on the branch, so the merge changed nothing in them. The zip is a copy of those files, not a source. The agent does not delete raw files; it stays queued until Bob removes it on GitHub or says to leave it. Counts are now 113 of 358 raw files ingested and 241 queued.

## [2026-11-15] setup | Bob removed the zip from `raw/apps/`

Bob deleted `raw/apps/replit-app-summaries.zip` on main (his commit 1a1ac92). It was a bundle of the 18 summaries already ingested, not a source. Main was merged into `replit-summaries` again. Counts are back to 113 of 357 raw files ingested and 240 queued.

## [2026-11-15] raw | Six more Replit summaries brought over

Bob sent links to three more summaries, and the agent found others in the projects he had worked in that morning. Read out of the Replit editor and checked against a SHA-256 computed there, as before: micro-gpt-swmm-v2, epanet-swmm-experts-v1.0, swmm-explorer--robertdickinson-v1.0.0, batch-swmm-runner-robertdickinson-v1.1.0, swmm-icm-st-venant--robertdickinson-v1.0.0, code-rosetta-stone-v1.0.0. All six match. Queued, not ingested. The first three settle the note of this morning that EPANET SWMM Experts and SWMM Explorer had no summary.
Replit projects: MicroGPT SWMM, EPANET SWMM Experts, SWMM Explorer, BatchSWMMRunner, SWMM ICM StVenant, Code Rosetta Stone.

## [2026-11-15] raw | Seven more Replit summaries brought over

Bob kept sending links. Read out of the Replit editor and checked against a SHA-256 computed there, as before: force-main-robertdickinson-v1.0, hindsight-prophet-robertdickinson-v1.0.0, swmmanywhere-explorer-v1.0.0, mirofish-swmm-v0.0.0, bob-swmm-auto-research-v0.0.0, ruby-swmm-router-v2026.11.15, swmm-history-robertdickinson-v1.0.0. All seven match. Queued, not ingested. That makes thirteen Replit summaries waiting, after the eighteen ingested as S96 to S113.
Replit projects: ForceMain_SWMM5_EPANET_Comparison, HindsightProphet, Swmmanywhere Explorer, Mirofish SWMM, BobSWMM Auto Research, RubySwmmRouter, SwmmHistory.
Two of his links were for files already here. The Manual Search summary in Replit has the same SHA-256 as the raw file behind S101, and the St. Venant summary has the same SHA-256 as the copy queued earlier today. Neither changed.
Counts: 113 of 370 raw files ingested, 253 queued. The README and the queue paragraph of the index carry the new counts; the overview keeps its count until the next ingest.
Tools: `tools/manifest.py` now strips quotation marks from a `version:` value that is followed by a comment (`"0.0.0" # where it came from` was stored as `0.0.0"`).

## [2026-11-15] raw | Two more Replit summaries brought over

Bob sent a link for ICMNewView. While in Replit the agent looked again at the three projects that had shown no summary that morning and found one in EPANET SWMM5 Generate. Read out of the Replit editor and checked against a SHA-256 computed there: icm-new-view-robertdickinson-v1.0.0 (app name in the file: ICM InfoWorks) and epanet-swmm-5-generate-v4.6 (app name in the file: EPANET 2.3 Generator). Both match. Queued, not ingested. That makes fifteen Replit summaries waiting.
HistoricalWaterInventions and Pyswmm Explorer still show no summary file name.
Counts: 113 of 372 raw files ingested, 255 queued.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for HistoricalWaterInventions. Read out of the Replit editor and checked against a SHA-256 computed there: historical-mystery-robertdickinson-v1.0.0 (app name in the file: Historical Water Inventions). It matches. Queued, not ingested. That makes sixteen Replit summaries waiting.
Pyswmm Explorer still shows no summary file name.
Counts: 113 of 373 raw files ingested, 256 queued.

## [2026-11-15] raw | The Pyswmm Explorer summary brought over

Bob sent a link for Pyswmm Explorer. Read out of the Replit editor and checked against a SHA-256 computed there: pyswmm-explorer-v1.0.0 (app name in the file: PySWMM Explorer). It matches. Queued, not ingested. That makes seventeen Replit summaries waiting, and every project on the list of that morning now has a summary here.
He also sent the link for the EPANET SWMM5 Generate summary; the file in Replit has the same SHA-256 as the copy brought over an hour earlier.
Counts: 113 of 374 raw files ingested, 257 queued.

## [2026-11-15] ingest | Seventeen more Replit app summaries, S114 to S130

Bob said "ingest" for the files brought over from Replit that afternoon, and "merge when done". Each file was read in full.
Sources written: S114 SWMM5 MicroGPT v2, S115 EPANET for SWMM5 Experts - The Rosetta Stone, S116 SWMM5 Explorer, S117 BatchSWMM56, S118 SWMM5 vs ICM InfoWorks Networks, S119 SWMM5 Rosetta Stone, S120 ForceMain SWMM5 EPANET Comparison, S121 Hindsight Prophet, S122 SWMManywhere Explorer, S123 SWMM5 Modeler, S124 bobSWMM Auto Research, S125 Kinematic Wave Router, S126 SWMM Ecosystem, S127 ICM InfoWorks, S128 EPANET 2.3 Generator, S129 Historical Water Inventions, S130 PySWMM Explorer.
Replit project each file came from, as seen in Replit: S114 MicroGPT SWMM, S115 EPANET SWMM Experts, S116 SWMM Explorer, S117 BatchSWMMRunner, S118 SWMM ICM StVenant, S119 Code Rosetta Stone, S120 ForceMain_SWMM5_EPANET_Comparison, S121 HindsightProphet, S122 Swmmanywhere Explorer, S123 Mirofish SWMM, S124 BobSWMM Auto Research, S125 RubySwmmRouter, S126 SwmmHistory, S127 ICMNewView, S128 EPANET SWMM5 Generate, S129 HistoricalWaterInventions, S130 Pyswmm Explorer.
Pages created: 16 app pages under `wiki/entities/` and one concept page, Replit apps: the second seventeen summaries. S118 is the summary of an app that already had a page, SWMM and ICM St. Venant comparison (app), so that page got a paragraph and no new page was made.
Pages changed, each with one paragraph headed "Added 15 November 2026" and a `changed_after_review` line: SWMM and ICM St. Venant comparison (S118), SWMM5 language translations and SWMM6 language translations (S119), Kinematic wave and steady flow routing (S117, S125), Force main friction (S115, S120), InfoWorks ICM (S125, S127), SWMM version history (S126), Fractal SWMM5/SWMM6 Network Generator (S123, S128), Bob's GitHub repositories (seven repositories). The first Replit concept page, not yet reviewed, was edited in place: its opening sentence, and its note that two projects had no summary. The overview got one bullet, a new first sentence and new counts; the README and index were updated.
Contradiction found: Bob's article of 23 February 2026 gives the St. Venant comparison app twelve tabs and 117 animations (S20); the summary written from the source on 15 November 2026 gives 13 topics, 16 diagram categories and 118 diagram entries (S118). Both are on the app page and it is Q78. The same summary settles what that page had left open: the app runs neither engine.
Open questions added: Q74 (none of the seventeen has been read by Bob), Q75 (dates and versions that are not release facts), Q76 (faults Replit Agent reported, none rerun), Q77 (names, three Rosetta Stones among them), Q78 (the St. Venant app counted two ways), Q79 (engine and repository provenance), Q80 (which AI built each). One sentence was added to Q67 and one to Q73.
Checked at ingest: every number in the claims and limits of the seventeen source pages was searched for in the raw file it cites, and every code fragment in backticks was matched verbatim; no misses. The counts on the new concept page (seven with an `engines:` entry, five failing a TypeScript check, ten calling an AI model at run time, seven naming a repository, five dated with the summary date) were counted from the front matter and bodies.
Length: four reviewed pages now stand over 600 words after their added paragraphs: Kinematic wave and steady flow routing (625), SWMM6 language translations (623), SWMM5 language translations (674, 606 before) and SWMM version history (803, 768 before). They are due for a split at the next lint.
Counts: 130 of 374 raw files ingested, 240 queued; 264 wiki pages; 74 open questions and 6 settled.
Not ingested, still queued in `raw/apps/`: st-venant-solver-rosetta-stone-v2.6.2 and PyBME-issue-drafts (Q56).

## [2026-11-15] setup | Main fast-forwarded to the ingest of S114 to S130

Bob had said "merge when done". Main now stands at the ingest commit. The agent cannot delete branches on GitHub; `replit-summaries-2` is merged and can go.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for the project SWMM5ControlRules. Read out of the Replit editor and checked against a SHA-256 computed there: hydro-control-v0.1.0 (app name in the file: SWMM5 Control Rule Editor). It matches. Queued, not ingested, on the branch `replit-summaries-3`.
He also sent the link for the Sewer Code Search summary; the file in Replit has the same SHA-256 as the raw file behind S111, and the EPANET SWMM Experts file has the same SHA-256 as the raw file behind S115.
Counts: 130 of 375 raw files ingested, 241 queued.

## [2026-11-15] ingest | SWMM5 Control Rule Editor, S131

Bob said "ingest". The file was read in full. Source written: S131 SWMM5 Control Rule Editor, from the Replit project SWMM5ControlRules. Page created: SWMM5 Control Rule Editor (app).
Pages changed: the second Replit concept page got an eighteenth row and one sentence (it is not yet reviewed, so it was edited in place); Pumps and pump curves got one paragraph headed "Added 15 November 2026" and a `changed_after_review` line; one sentence was added to Q74; the overview, README and index carry the new counts.
No contradiction found. The app runs no engine and has no tests, and its summary says exported rules were not validated by a simulation.
Checked at ingest: every number and every code fragment in backticks on the source page was searched for in the raw file; no misses.
Length: Pumps and pump curves stands at 711 words (666 before); it joins the four pages due for a split at the next lint.
Branches: Bob deleted the branches on GitHub while this ingest ran. `replit-summaries-3` held the raw file and had not been merged, so the agent pushed it again with this ingest on it. Main is unchanged until Bob says "merge".
Counts: 131 of 375 raw files ingested, 240 queued; 266 wiki pages; 74 open questions and 6 settled.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for the project SwmmInpViewer. Read out of the Replit editor and checked against a SHA-256 computed there: swmm-inp-viewer--robertdickinson-v1.0.0 (app name in the file: SWMM5 & EPANET INP Explorer). It matches. Queued, not ingested. This is not the app behind S105, whose file is swmm-5-inp-reader-robertdickinson-v0.1.0.
He also sent the link for the SWMManywhere Explorer summary; the file in Replit has the same SHA-256 as the raw file behind S122.
Counts: 131 of 376 raw files ingested, 241 queued.

## [2026-11-15] ingest | SWMM5 & EPANET INP Explorer, S132

Bob said "ingest". The file was read in full. Source written: S132 SWMM5 & EPANET INP Explorer, from the Replit project SwmmInpViewer. Page created: SWMM5 & EPANET INP Explorer (app).
Pages changed, none of them yet reviewed, so edited in place: the second Replit concept page got a nineteenth row; SWMM5 .inp File Viewer (app) got a paragraph naming this second app with a like name; SWMM Ecosystem (app) got a paragraph saying this app embeds its site. One sentence was added to Q74 and one to Q77. The overview, README and index carry the new counts.
No contradiction found. The app runs no engine and has no tests; its TypeScript check fails with 22 diagnostics, as reported by Replit Agent and not rerun.
Checked at ingest: every number and every code fragment in backticks on the source page was searched for in the raw file; no misses.
Counts: 132 of 376 raw files ingested, 240 queued; 268 wiki pages; 74 open questions and 6 settled.

## [2026-11-15] setup | Main fast-forwarded to S132

Bob said "merge". Main now holds S131 and S132. `replit-summaries-3` is merged and can go; the agent cannot delete branches on GitHub.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for the project SWMM5NetworkAnalyzer. Read out of the Replit editor and checked against a SHA-256 computed there: social-network-analyzer-robertdickinson-v0.1.0 (app name in the file: SWMM5 .inp File Interactive Viewer). It matches. Queued, not ingested, on the branch `replit-summaries-4`. It is a third app with a name like an INP viewer, after S105 and S132.
Counts: 132 of 377 raw files ingested, 241 queued.

## [2026-11-15] ingest | SWMM5 .inp File Interactive Viewer, S133

Bob said "ingest". The file was read in full. Source written: S133 SWMM5 .inp File Interactive Viewer, from the Replit project SWMM5NetworkAnalyzer. Page created: SWMM5 .inp File Interactive Viewer (app).
Pages changed, none of them yet reviewed, so edited in place: the second Replit concept page got a twentieth row and lost its Version column, which keeps it under 600 words (versions are on the app pages); SWMM5 .inp File Viewer (app) and SWMM5 & EPANET INP Explorer (app) each got a paragraph naming this third app with a like name. One sentence was added to Q74 and one to Q77. The overview, README and index carry the new counts.
No contradiction found. The app runs no engine and has no tests.
Checked at ingest: every number and every code fragment in backticks on the source page was searched for in the raw file; no misses.
While this ran, Bob wrote that he has some similar apps on Replit from last year and will combine them or get rid of them. That is not yet filed as a note; the agent asked him whether to file it, since it bears on Q77.
Counts: 133 of 377 raw files ingested, 240 queued; 270 wiki pages; 74 open questions and 6 settled.

## [2026-11-15] ingest | Note: two LinkedIn posts that drew a good response, S134

Bob wrote that he had got pretty good responses on two posts, one about HydroCouple and one personal post, sent a screenshot of the counts under both, and asked that the repository keep something about his better received LinkedIn posts. The agent filed his sentence and the eight figures as a note on the template, `raw/notes/linkedin-two-well-received-posts-2026-11.md`, and ingested it. The screenshot is not in the repository because it shows a profile photograph.
Source written: S134. Page created: LinkedIn posts that were well received (concept). Pages changed, each with a paragraph headed "Added 15 November 2026" and a `changed_after_review` line: OpenSWMM 6 and HydroCouple, Robert Dickinson. Q81 added: the links and dates of the two posts, which strip of the screenshot belongs to the personal post, and what a usual post of his gets.
Page rule 9: Bob names the second post by a member of his family. The raw note keeps his sentence as typed, with no name. The wiki calls it his personal post and says no more.
Arithmetic at ingest, ours: per 1,000 impressions the engine post had 10.1 reactions, 0.5 comments and 0.5 reposts; the personal post 19.5, 3.4 and 0.1. Impressions ratio 1.96.
A departure from an earlier choice, at Bob's request: the anecdotes note (S90) left reaction counts out; this note keeps counts because he asked for them.
Counts: 134 of 378 raw files ingested, 240 queued; 272 wiki pages; 75 open questions and 6 settled.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for the project SWMM5 Topo Network Wizard. Read out of the Replit editor and checked against a SHA-256 computed there: topo-network-wizard-v1.0.0 (app name in the file: SWMM5 Topo Network Wizard). It matches. Queued, not ingested. It is a fourth network generator, after those of Q73.

## [2026-11-15] ingest | LinkedIn: fifty posts with their counts, S135

Asked for a LinkedIn analytics export, Bob wrote "let me do this then" and attached a paste of 50 of his posts with their counts, with the words "this might be enough for now". The agent read the whole paste and typed `raw/linkedin/2026-11-15-fifty-posts-with-counts.md` from it: each post's place, age, first twelve words, attached title and counts. The full text of the posts was left out of the public repository because it names many people and one post gives an email address. If Bob wants the paste itself in `raw/`, he can say so.
Source written: S135. Page rewritten (not yet reviewed, so in place): LinkedIn posts that were well received, now built on the 50 posts. Pages changed: S134 and S94 each got a line; the paragraph added that afternoon to OpenSWMM 6 and HydroCouple was rewritten from the list; sentences were added to Q81.
Settled by S135, and said so under Q81: the personal post of S134 is the post of 14 November 2026 (S94), and the lower strip of the screenshot is that post's.
Disagreements recorded under Q81: reposts (9 and 1 on the screenshot, none shown on the list); the age "2d" for a post S91 dates to the day before; "slide" in the note against "GIF" in the post's own text.
Arithmetic at ingest, ours: middle values of the 50 are 11,941 impressions, 39 reactions and 4 comments. The HydroCouple post is 21st in impressions, 2nd in reactions and 4th in reactions per 1,000 impressions (10.1; middle value 2.1). The post of 14 November is 42nd in impressions, 3rd in reactions, 1st in comments, and 1st in both reactions and comments per 1,000 impressions (19.5 and 3.4; middle values 2.1 and 0.2).
Counts: 135 of 380 raw files ingested, 241 queued; 273 wiki pages; 75 open questions and 6 settled.

## [2026-11-15] ingest | SWMM5 Topo Network Wizard, S136

Bob said "ingest and then merge". The file was read in full. Source written: S136 SWMM5 Topo Network Wizard, from the Replit project of the same name. Page created: SWMM5 Topo Network Wizard (app).
Pages changed, none of them yet reviewed, so edited in place: the second Replit concept page got a twenty-first row; SWMM5 Topology Sandbox (app) got a paragraph naming this other generator built on topology. One sentence was added to Q73 and one to Q74. The overview, README and index carry the new counts.
No contradiction found. The app's three `engines:` entries are its own code; it runs no SWMM engine and has no tests, and its exported INP was not run in EPA SWMM.
Checked at ingest: every number and every code fragment in backticks on the source page was searched for in the raw file; no misses.
Counts: 136 of 380 raw files ingested, 240 queued; 275 wiki pages; 75 open questions and 6 settled.

## [2026-11-15] setup | Main fast-forwarded to S136

Main now holds S133 to S136. `replit-summaries-4` is merged and can go.

## [2026-11-15] raw | One more Replit summary brought over

Bob sent a link for the project SWMM Documents Explorer. Read out of the Replit editor and checked against a SHA-256 computed there: swmm-documents-explorer-v1.0.0 (app name in the file: SWMM Documents Explorer). It matches. Queued, not ingested, on the branch `replit-summaries-5`.
Counts: 136 of 381 raw files ingested, 241 queued.

## [2026-11-15] raw | The SWMM5 Quizzer summary brought over

Bob sent a link for the project SWMM5QuizMaster. Read out of the Replit editor and checked against a SHA-256 computed there: quiz-master-robertdickinson-v1.0.0 (app name in the file: SWMM5 Quizzer). It matches. No earlier copy was in `raw/apps/`. Queued, not ingested, on the branch `replit-summaries-5`.
Counts: 136 of 382 raw files ingested, 242 queued.

## [2026-11-15] raw | Two older Replit summaries brought over

Bob sent links for the projects SWMM-Infiltration and GatorSWMM. Each was read out of the Replit editor and checked against a SHA-256 computed there: swmm-infiltration--robertdickinson-v1.0.0 (app name in the file: SWMMCRAFT; last commit 2025-12-25) and gator-swmm-robertdickinson-v1.0.0 (app name in the file: SWMM5Wiki; last commit 2025-08-28). Both match. Neither had an earlier copy in `raw/apps/`. The name SWMMCRAFT here belongs to an infiltration simulator; no other SWMMCRAFT summary is in `raw/apps/`. Queued, not ingested, on the branch `replit-summaries-5`.
Counts: 136 of 384 raw files ingested, 244 queued.

## [2026-11-15] raw | BobSWMM Writer and ICM PRN File Reader summaries brought over

Bob sent links for the projects BobSWMMWriter and ICMReader. Each was read out of the Replit editor and checked against a SHA-256 computed there: snagit-video-article--robertdickinson-v2.1.0 (app name in the file: BobSWMM Writer) and icm-reader-robertdickinson-v1.0.0 (app name in the file: ICM PRN File Reader). Both match. Neither had an earlier copy in `raw/apps/`. Queued, not ingested, on the branch `replit-summaries-5`.
Counts: 136 of 386 raw files ingested, 246 queued.

## [2026-11-15] ingest | S137 to S142: six Replit summaries

Ingested the six summaries Replit Agent wrote that came over after S136: S137 SWMM Documents Explorer, S138 SWMM5 Quizzer, S139 SWMMCRAFT (Replit project SWMM-Infiltration), S140 SWMM5Wiki (Replit project GatorSWMM), S141 BobSWMM Writer and S142 ICM PRN File Reader. None runs an engine; one (S142) has a test suite, 24 passing.
Created: six source pages, six entity pages and the concept page "Replit apps: six more summaries". Changed: the second-batch concept page (one pointer), the Green-Ampt Infiltration Calculator and SWMM5 Runoff and Infiltration pages (a paragraph each on a third infiltration app), Bob's GitHub repositories (a paragraph naming SWMMEnablement/SWMM_MD_Documents; reviewed page, marked changed_after_review), overview (a bullet and the counts), open questions (sentences added to Q74, Q75, Q76, Q77, Q79 and Q80; Q82 added), index, README.
Contradiction: S139 reports that its Curve Number reference page and server use different denominators; with Ia = 0.2 S the two are the same expression (our algebra). Filed as Q82, not settled.
Checked at ingest: numbers and code fragments on the new pages were searched for in their raw files; the misses are our own arithmetic, marked as such, and "SHA-256".
Bob wrote at 17:20 that he is fixing two errors; which two is not yet known. The pages describe the apps as their summaries found them; a fixed version arrives as a new summary file and a new source page.
Counts: 142 of 386 raw files ingested, 240 queued; 288 wiki pages; 76 open questions and 6 settled.

## [2026-11-15] ingest | S143: Bob's note that he fixed the PRN problem

Bob wrote at 17:27: "i fixed the prn problem and merge". Filed in his words as raw/notes/icm-prn-reader-fix-2026-11-15.md and ingested as S143. Changed: the ICM PRN File Reader page (a paragraph), Q76 (a sentence), overview and README counts, index. Which of the two problems he fixed (the open file list or the differing thresholds) is not said; the summary of the fixed version has not come in.
Counts: 143 of 387 raw files ingested, 240 queued; 289 wiki pages; 76 open questions and 6 settled.

## [2026-11-15] setup | Main fast-forwarded to S143

Main now holds S137 to S143. `replit-summaries-5` is merged and can go.

## [2026-11-15] ingest | S144: which PRN problem Bob fixed

Asked which problem he fixed, Bob answered at 17:28: "the file that anyone can read". Filed in his words as raw/notes/icm-prn-reader-fix-which-2026-11-15.md and ingested as S144. The open file list of the ICM PRN File Reader is now fixed on Bob's word; the differing thresholds stay as reported. Changed: the app page, Q76, overview and README counts, index. On the branch `replit-summaries-6`.
Counts: 144 of 388 raw files ingested, 240 queued; 290 wiki pages; 76 open questions and 6 settled.

## [2026-11-15] setup | Main fast-forwarded to S144

Main now holds S144. `replit-summaries-6` is merged and can go.

## [2026-11-15] raw | Four more Replit summaries brought over

Bob sent links for the projects ICMFlowVisualizer, InfoSewerToICMSteps, SWMManywhere-App and Open-SWMM-Core. Each was read out of the Replit editor and checked against a SHA-256 computed there: icm-flow-visualizer-robertdickinson-v1.0.0 (app name in the file: ICM Ruby to Nano Banana Prompt), data-sewer-robertdickinson-v1.0.0 (InfoSewer to InfoWorks ICM), swm-explorer-v1.0.0 (SWMManywhere Explorer) and open-swmm-core-v6.0.0-alpha.1 (OpenSWMM Engine). All four match. None had an earlier copy in `raw/apps/`. The SWMManywhere-App file carries the same app name as `swmmanywhere-explorer-v1.0.0.md` (S122) but a different `file:` line, `swm-explorer`, and runs SWMManywhere 0.1.17 and a SWMM5 WebAssembly engine where S122 gives `engines: none`; the manifest treats them as two apps. Queued, not ingested, on the branch `replit-summaries-7`.
Counts: 144 of 392 raw files ingested, 244 queued.

## [2026-11-15] raw | EPANET Quizzer and Ruby Script Runner summaries brought over

Bob sent five links. Two were new and were read out of the Replit editor and checked against a SHA-256 computed there: epanet-quizzer-robertdickinson-v1.0.0 (app name in the file: EPANET Quizzer) and ruby-script-ai-v0.1.0 (InfoWorks ICM Ruby Script Runner). Both match. One link to RubyScriptAI came twice. The RubySwmmRouter file hashed the same as `ruby-swmm-router-v2026.11.15.md` already here (S125), so nothing was added for it. The RubyMakerAI link is to `attached_assets/linkedin_article_rubymaker.md`, an article text with no front matter that is not among the LinkedIn articles in `raw/linkedin/`; it was read and hash-checked but not added, pending Bob's word on whether it was published. Queued, not ingested, on the branch `replit-summaries-7`.
Counts: 144 of 394 raw files ingested, 246 queued.

## [2026-11-15] raw | Bob's note: the OpenSWMM license is no longer MIT

Bob wrote at 18:42: "OpenSWMM license has moved away from MIT". Filed in his words as raw/notes/openswmm-license-not-mit-2026-11-15.md and queued, to be ingested with the OpenSWMM Engine summary (open-swmm-core-v6.0.0-alpha.1), which says MIT. The wiki already gives Apache-2.0 for OpenSWMM `swmm6_rel` from several sources (S59, S69, S96 and the OpenSWMM 6 page); none of its pages says MIT for OpenSWMM. On the branch `replit-summaries-7`.
Counts: 144 of 395 raw files ingested, 247 queued.

## [2026-11-15] raw | Bob's note: the Ruby Script Runner is deleted

Bob wrote at 18:55: "it is gonem, it is better to use icm exchange anyway". He had deleted the InfoWorks ICM Ruby Script Runner (Replit project RubyScriptAI) after its summary showed it ran visitors' Ruby on the server and Replit Agent found no sandbox available. Filed in his words as raw/notes/ruby-script-runner-deleted-2026-11-15.md and queued, to be ingested with ruby-script-ai-v0.1.0, which stays as the record of the app. On the branch `replit-summaries-7`.
Counts: 144 of 396 raw files ingested, 248 queued.

## [2026-11-15] ingest | S145 to S152: six Replit summaries and two notes

Ingested S145 ICM Ruby to Nano Banana Prompt, S146 InfoSewer to InfoWorks ICM, S147 SWMManywhere Explorer (swm-explorer), S148 OpenSWMM Engine, S149 EPANET Quizzer and S150 InfoWorks ICM Ruby Script Runner, with Bob's notes S151 (the OpenSWMM license is no longer MIT) and S152 (he deleted the Ruby Script Runner; ICM Exchange is the better way).
Created: eight source pages, six entity pages and the concept page "Replit apps: a fourth set of six summaries". Changed: the third-batch concept page (one pointer); the SWMManywhere Explorer, InfoSewer and InfoSWMM Legacy Model Reader and SWMM5 Quizzer pages (a paragraph each); OpenSWMM 6 and HydroCouple (reviewed page, a paragraph on the app and the license, marked changed_after_review); overview (a bullet and the counts); open questions (sentences added to Q74, Q75, Q76, Q77, Q79 and Q80); index; README.
Contradiction: S148 says the OpenSWMM Engine app identifies OpenSWMMCore and HydroCouple as MIT; S59, S69 and S96 give Apache-2.0 for swmm6_rel of HydroCouple/openswmm.engine. Filed as Q83 and settled by Bob (S151): the license has moved away from MIT. Bob also said at 18:44 that he would fix the app now; a fixed version comes as a new summary.
Checked at ingest: numbers and code fragments on the new pages were searched for in their raw files; the misses are our arithmetic, marked, and "SHA-256".
Counts: 152 of 396 raw files ingested, 240 queued; 305 wiki pages; 76 open questions and 7 settled.

## [2026-11-15] setup | Main fast-forwarded to S152

Main now holds S145 to S152. `replit-summaries-7` is merged and can go.

## [2026-11-15] raw | OpenSWMM Engine summary, version 6.0.0-alpha.2

Bob sent a link for open-swmm-core-v6.0.0-alpha.2.md in the Replit project Open-SWMM-Core, written after he had the app's license statement fixed. Read out of the Replit editor and checked against a SHA-256 computed there; it matches. The alpha.1 file (S148) is unchanged beside it. The new file pins the engine to HydroCouple/OpenSWMMCore commit 87664bf518104e618f0537340b9500a1fdfe797c, gives the engine license as Apache-2.0 for OpenSWMM contributions with the USEPA portions public domain, and says the app has not yet been republished. Queued, not ingested, on the branch `replit-summaries-8`; lint warns that a newer summary is waiting, as expected until it is ingested.
Counts: 152 of 397 raw files ingested, 241 queued.

## [2026-11-15] raw | Bob's note: OpenSWMM Engine alpha.2 is published

Bob wrote at 19:16: "it is published". Claude loaded https://open-swmm-core.replit.app at about 19:17 and found alpha.2, the pinned commit 87664bf, the Apache-2.0 statement for OpenSWMM with the USEPA public-domain line, the NOTICE text, and MIT stated for the app's own code only. Filed as raw/notes/openswmm-engine-alpha2-published-2026-11-15.md and queued with the alpha.2 summary. Bob also said he is done with Replit for now. On the branch `replit-summaries-8`.
Counts: 152 of 398 raw files ingested, 242 queued.

## [2026-11-15] ingest | S153 and S154: OpenSWMM Engine alpha.2

Ingested S153, the summary Replit Agent wrote of OpenSWMM Engine 6.0.0-alpha.2 after the license fix, and S154, Bob's note that it is published with a check of the live page. S148 (alpha.1) gets `superseded_by: S153` and is otherwise unchanged. Rewritten: the OpenSWMM Engine app page, for the current version, with a paragraph on what changed from alpha.1. Changed: the fourth-batch concept page (one sentence), OpenSWMM 6 and HydroCouple (reviewed page, one sentence added to its Added paragraph, marked changed_after_review), open questions (sentences added to Q74, Q75, Q79 and Q83), overview and README counts, index.
Noted: the engine version label moved from Legacy SWMM 5.x with a 5.2.4 baseline (S148) to Legacy SWMM 5.3.0 (S153); S59 names an OpenSWMM legacy 5.3.0-beta.3 at another commit; not said whether they are the same engine (Q79).
Counts: 154 of 398 raw files ingested, 240 queued; 307 wiki pages; 76 open questions and 7 settled.

## [2026-11-15] setup | Main fast-forwarded to S154

Main now holds S153 and S154. `replit-summaries-8` is merged and can go.

## [2026-11-15] setup | Log restored: 31 entries lost on 15 November put back

While building the reader app, the agent found that the commit for the S90 ingest (4448db4, 15 November 2026, 07:55 Eastern) had replaced `log.md` instead of appending to it, so the 31 entries before S90, from the setup on 14 November to the merge of `ingest-hydraulics-ch2-4-6`, were gone from the file. They were taken unchanged from the version before that commit (5b20417) and put back at the top; every later entry is untouched. Nothing else changed.
