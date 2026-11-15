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
