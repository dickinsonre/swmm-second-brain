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

## [2026-11-15] setup | The reader app: tools/build_app.py

Bob asked for a Claude HTML app for the second brain. `tools/build_app.py` (with `app_template.html`, `app_doc.py` and `app_doc.md`) builds one HTML page of the whole wiki into `build/`, which git ignores: a full document for Netlify and a body-only copy for the Claude artifact. Views: Read, Search, Open questions, To review, About, Doc. `tools/build_app_docx.js` makes the Doc essay as a .docx from the same source. CLAUDE.md now names the two tools and adds the rebuild to step 8 of an ingest. The app's own summary is `raw/apps/swmm-second-brain-v0.1.0.md`, queued, as Bob's rule for app summaries asks. Complexity measured with Bob's SWMM App Complexity Meter: index 38.1 on the four code files (`tools/app_complexity.json`).
Counts: 154 of 399 raw files ingested, 241 queued.

## [2026-11-16] ingest | S155 to S157: three surrogate apps, summaries written by Claude from the live Netlify pages
Bob asked where his modpods app was; three Netlify sites matched, none with a summary in `raw/apps/`. At his request Claude read each live page tab by tab in a browser (fetching from the sandbox is blocked) and wrote a summary under app rule 6, with `written_from:` and nothing rerun: `modmods-explained-v2026-08-21.md`, `automatic-rainfall-runoff-models-v2026-08-21.md` and `swmm5-lstm-calibration-v2.0.md`. The first two pages carry no version, so the version is the Netlify deploy date. Sources: S155 (modpods, for a SWMM person), S156 (Automatic Rainfall-Runoff Models: Evidence Atlas), S157 (LSTM + SWMM5 v2.0).
New pages: entities modpods, modpods-explainer-app, arrm-evidence-atlas, lstm-swmm5-app; concepts surrogates-hidden-state-missing-forcing and calibrating-through-a-surrogate. Changed, each with an "Added 16 November 2026" paragraph and a `changed_after_review:` line: rdii-unit-hydrographs, wasm-against-native-builds, reading-swmm-output, calibration-validation-uncertainty, surrogate-distilled-from-swmm. Overview: one bullet, counts 157 of 402 and 80 app summaries, open items corrected from sixty to eighty.
Contradictions: the explainer and the Atlas, built from the same replication package, give different folder counts and a different worst junction (Q85, Q86); one Atlas table does not add up (Q85). New open items: Q84 (three unread summaries; two pages have no AI-use note; the LSTM page does not credit Amin Talei), Q87 (F-9, SWMM 5.2.4's late monthly rainfall adjustment, no register ID).

## [2026-11-16] ingest | S60, sections 1.2 to 1.5 of the EPA hydraulics manual
Bob chose the next manual chapter. Read in full: 1.2 SWMM's Object Model (Table 1-2), 1.3 Process Models, 1.4 Simulation Process Overview (Table 1-3), 1.5 Interpolation and Units (Table 1-4). Figures 1-1 to 1-6 are not in the raw file, and Equations 1-1 and 1-2 were lost in the conversion; both are described in words.
New page: concepts/swmm5-objects-state-time-loop. Changed: S60 (read: list, an Added 16 November 2026 block), reading-swmm-output (one sentence), Q87 (two sentences), overview (one bullet), index.
Primary document against an app: section 1.5 describes as the design what the LSTM + SWMM5 app found as F-1 (a reported rainfall intensity is the value at the start of the runoff step). Recorded on Q87; F-9 stays open. No contradiction found. Remaining in S60: Chapters 5 and 7 and the appendices.

## [2026-11-16] ingest | S158: Tivadar Danka, Graph Theory For Visual Learners (reading note), as graph concepts
Bob asked to add https://thepalindrome.org/p/graph-theory-for-visual-learners-320 "as graph concepts" with the right citation. The article (The Palindrome, 11 November 2026, by Tivadar Danka) is third-party and copyrighted, so `raw/notes/graph-theory-for-visual-learners-danka-2026-11-11.md` holds Claude's digest of it, written after reading the whole post in a browser, with the full citation; the text itself is not copied.
New pages: concepts graph-basics, graph-paths-and-search, graph-cycles-and-trees, planar-graphs, graph-coloring-and-ramsey, graph-random-walks-and-centrality (a new Concepts group, Graph theory); entity tivadar-danka. The article does not mention SWMM; the links to SWMM rest on S60 (kinematic wave's directed acyclic networks, Kahn's algorithm) and S08 (swmm5-kw), cited where they appear. Q88 added (the note waits for Bob's read; where third-party digests belong).
Also added today, queued and not ingested: seven ICM notes of Bob's in `raw/notes/`, from ICM-Ruby-SWMM-Markdown.zip.

## [2026-11-16] ingest | S159 to S165: seven ICM notes Bob supplied
The seven notes added this morning from ICM-Ruby-SWMM-Markdown.zip: ICM Ruby in the UI and in Exchange (S159), Ruby version compatibility (S160), the Exchange run lifecycle (S161), network tables and fields (S162), the results field crosswalk (S163), SWMM .inp conversion checks (S164) and a two-pipe EPA, Ruby and ICM benchmark design (S165). None names its author; they refer to Bob in the third person. Their Autodesk facts are reported from Autodesk's help and were not checked against ICM; every procedure awaits a run.
New pages: concepts icm-ruby-ui-and-exchange, icm-tables-and-result-fields, swmm5-to-icm-conversion-checks. Changed, each with an "Added 16 November 2026" paragraph: entities/infoworks-icm, concepts/swmm5-versus-icm-infoworks. Q89 added (authorship, unchecked facts, nothing run); one sentence added to Q16 (the benchmark is the run Q16 lacks). Overview: one bullet under SWMM 5 and ICM InfoWorks; counts 165 of 410.
No contradiction with earlier pages: no earlier source gives ICM's Ruby version, table names or import limit.

## [2026-11-16] ingest | S166 to S178: ten ICM 2D notes, Bob's note on where the ICM notes come from, and two Curve Number articles
Bob asked to ingest the ten ICM 2D notes and said they come from the GPT plugin for Autodesk, which he uses a lot; his sentence is filed as `raw/notes/icm-notes-from-gpt-plugin-2026-11-16.md` (S166). It settles Q89; that it covers the seven earlier ICM notes too is Claude's reading, recorded as such. All seventeen ICM notes are now marked AI-written, not checked against ICM.
Sources: S166 (Bob's note), S167 to S176 (the 2D notes: terrain and mesh, boundaries, rainfall and infiltration, node exchange, river banks, subgrid, timestep, volume balance, results and hazard, benchmark cases), S177 and S178 (Bob's 2023 and 2024 Curve Number articles, which the rainfall note points to).
New pages: concepts icm-2d-mesh-and-subgrid, icm-2d-boundaries-and-exchange, icm-2d-rainfall-and-infiltration, icm-2d-runs-and-checks, icm-2d-benchmark-cases (a new Concepts group, ICM 2D). Changed: entities/infoworks-icm and concepts/infiltration-methods (dated paragraphs), icm-tables-and-result-fields (hw_2d_infil_surface), the seven earlier ICM note source pages and the three ICM concept pages (authorship), overview, index, README. Q89 ticked; Q90 added (nothing in the seventeen notes checked or run).
Checked: the rainfall box, 10,000 sq ft x 1.00 in / 12 = 833.33 cu ft, agrees. The 2023 article lists four 2D infiltration types and the 2025.1 article six; a change in ICM, not a disagreement.

## [2026-11-16] ingest | S179: ChatGPT drafted the seven ICM notes
Bob pasted, after "do this -", a passage from ChatGPT saying it drafted S159 to S165 from Autodesk Help, left the author out of the ZIP, and that the seven checked-in notes match the ZIP byte for byte; record ChatGPT as the drafter and keep the ICM runtime tests pending. Filed as `raw/notes/icm-notes-drafted-by-chatgpt-2026-11-16.md` (S179), with the two voices kept apart.
Checked: the seven files in `raw/notes/` compared with a fresh extraction of ICM-Ruby-SWMM-Markdown.zip; all identical.
Changed: S159 to S165 (a `drafted_by:` line and How it was written), S166 (confirmation), the three ICM concept pages, entities/infoworks-icm, concepts/swmm5-versus-icm-infoworks, overview, index, README. Q89 confirmed for the seven (it was ticked on S166); Q90 stays open, with Bob's word to keep the runtime tests pending.

## [2026-11-16] setup | Ontology draft: typed relations, tried on the ICM and Curve Number pages
Caleb Buahin asked whether the wiki could have a formal ontology; Bob asked for a draft to show him. New: `ONTOLOGY.md` (14 relations mapped to RDF, SKOS, PROV and Dublin Core where they fit; 12 classes; prefixes), `tools/ontology.py` (reads each page's `**Relations**` table, checks it, writes `ontology/second-brain.trig`, `.jsonld`, `relations.csv` and `graph.md`; `--check` parses the output with rdflib and runs `ontology/queries/*.rq`), a Relations table on three pages (icm-tables-and-result-fields, icm-2d-rainfall-and-infiltration, icm-ruby-ui-and-exchange). Every row cites a source, and each statement is filed in the named graph of each source it cites, with that source's `drafted_by:` and `reviewed:`.
First build: 88 statements, 57 terms, 9 source graphs. rdflib 7.6.0 parses TriG and JSON-LD to the same 517 quads; four sample queries answered (fields reporting the same quantity, the InfoWorks to ICM SWMM crosswalk with its cautions, what came in which release, and where each statement comes from). Lint now checks Relations tables; a test page with four bad rows produced the four expected errors.
Schema changes, for Bob to accept or change: CLAUDE.md page rule 11 (Relations, draft and optional), the layout lines for ONTOLOGY.md, ontology/ and tools/ontology.py, and ingest step 8 runs tools/ontology.py. Also: `drafted_by:` added to S167 to S176, the ten 2D notes, from S166.

## [2026-11-16] setup | Bob accepted the ontology draft
Bob said "merge" on branch ontology-draft at 17:26 Eastern, which accepts CLAUDE.md page rule 11 (Relations tables, draft and optional), the layout lines for ONTOLOGY.md, ontology/ and tools/ontology.py, and the ingest step that rebuilds the ontology.

## [2026-11-16] setup | Ontology tightened: qualifiers, what each relation can connect, unknown drafters
Three changes that ChatGPT suggested when Bob showed it the draft, made on branch ontology-tighten at his request ("try to use these GPT suggestions").
- Qualifiers. A row's Note can carry `condition`, `tested_on`, `as_of` and `verification` (run, pending, documented) as `` `key: value` ``; they become properties of the reified statement. The 2023 Curve Number approximation row now carries its condition, test model and storms, date and `verification: run` from S177; DEPNOD close_match HEAD carries `condition: on a common vertical datum` and `verification: pending` (Q90); rows reported from Autodesk's help carry `verification: documented`.
- Domain and range. ONTOLOGY.md's Relations table gained "Subject must be" and "Object must be" columns, and `tools/lint.py` checks them. The check found one gap at once: `icm:JobTimeout` had no is_a row; added as `sb:Parameter` from S161. A scratch copy with seven bad rows (DEPNOD reports icm:2027.0, an unknown qualifier, a bad verification value, a qualifier with no space, replaces across classes, a close_match with no is_a, translation_of on a quantity) gave eight errors, as expected.
- Attribution. A source page with no `drafted_by:` line now gives `sb:draftedBy "unknown"` (and `sb:reviewed "unknown"` with no `reviewed:` line). ONTOLOGY.md says why caveated mappings use close_match: SKOS exactMatch is transitive.
New queries: 5-comparable-fields (the test question), 6-approximations, 7-not-yet-run; 2-crosswalk and 4-provenance now show conditions, verification and "unknown". Page rule 11 in CLAUDE.md gained one sentence on qualifiers. 89 statements on 3 pages; rdflib parses TriG and JSON-LD to 588 quads each.

## [2026-11-16] setup | Bob accepted the tightened ontology
Bob said "merge" on branch ontology-tighten at 17:56 Eastern, which accepts the added sentence in CLAUDE.md page rule 11 (qualifiers and the check of what each relation may connect) and the changes to ONTOLOGY.md, tools/ontology.py and the three Relations tables.

## [2026-11-16] lint | Grok's review: stale README, review queue, AI-dependence count
Bob passed on a review of the repository by Grok (xAI), graded A− (91/100). Its limits: about 40% ingested, human review incomplete, ontology on few pages, no license, dependence on AI-drafted sources. What it got wrong came from the README, which still said 313 raw files and about 1,060,000 words (now 422 and about 1,330,000) and "No wiki page has been read by a person yet" (Bob read every page on 11/16/2026); both corrected, with the wiki counts (354 pages, about 176,000 words).
- `tools/lint.py --review` prints the review queue in reading order: additions to pages Bob has read, then unread wiki pages (those resting only on AI-drafted sources first, then the most linked), then unread source pages (AI-drafted first). Today: 5, 15 and 22.
- `tools/lint.py` now counts source pages with a `drafted_by:` line (17) and pages resting only on them (0). The count is low: 84 more source pages name an AI under "How it was written" and carry no `drafted_by:` line.

## [2026-11-16] setup | License, and who drafted each source
Bob's answers to three questions after Grok's review (18:20 Eastern).
- License: MIT for `tools/`; CC BY 4.0 for the wiki, the ontology, the README, schema and log, and Bob's own writing in `raw/`; files in `raw/` by others keep their own terms (U.S. government reports are public domain; the SWMM 4.4 block documentation keeps its 2004 CDM/OSU terms; port READMEs carry their repositories' licenses). `LICENSE` added; README gained a License section and an up-to-date AI-use note.
- `drafted_by:` added to 153 source pages, each restating the page's own "How it was written" (Bob: a metadata line, not a change after review; CLAUDE.md says so). With the 17 already there, 170 of 179 source pages carry it. The tools read the leading name: 138 sources drafted by an AI (Claude, ChatGPT, the GPT plugin for Autodesk, Replit Agent, Lovable or an unnamed AI), 20 `unknown` (the text only reads as AI-drafted, or nothing is stated), the rest Bob's own words. 95 wiki pages rest only on AI-drafted sources; `tools/lint.py --review` lists them. The ontology gained `sb:aiDrafted` (yes, no, unknown), shown by query 4.

## [2026-11-16] ingest | S60, Chapter 5 of the EPA hydraulics manual: Cross-Section Geometry
Bob chose "Next EPA manual chapter" (primary documents first, after Grok's point on coverage). Read in full: sections 5.1 to 5.5 (raw lines 3379 to 5464). Not in the raw file: pages 80 and 102, and Equation 5-26 (Q92). Most equations are garbled, so the pages describe them in words.
- New pages: [Conduit cross-sections: the built-in shapes](wiki/concepts/conduit-cross-sections.md) (20 standard shapes, lookup tables, Table 5-13 area at maximum flow, area from section factor, critical and normal depth) and [Shape curves, transects and storage curves](wiki/concepts/shape-curves-transects-storage-curves.md).
- Changed after review, each with an Added paragraph and a `changed_after_review:` line: S60 (read list, claims, feeds), [SWMM 5 network objects](wiki/concepts/swmm5-network-objects.md), [Kinematic wave and steady flow](wiki/concepts/kinematic-wave-and-steady-flow.md), the overview and the open questions.
- New open questions: Q91 (six section cross-references off by one level, Equations 5-14 and 5-15 numbered twice, conductance called "section factor times roughness") and Q92 (missing pages). No contradiction with an existing page: no page covered cross-section geometry before.
- Every number on the new pages was matched to the chapter's raw text by script; three Table 5-5 coefficients are split by superscript markup in the raw file and are flagged as such.

## [2026-11-16] setup | Purpose: model comparison; AI-drafted summaries are by design
Bob, 19:14 Eastern: "i am not worried about the ai generaged md files, that is the whole purpose of them - anyway, i am doing this to make model comparisons and not be a writer - the simulatons are the whole point". So:
- CLAUDE.md gained a Purpose paragraph (the simulations are the point; AI-drafted summaries are expected; what matters is whether a run backs a claim), and the order of ingest now puts sources that report simulation runs and comparisons first within a theme.
- `tools/lint.py` reports `drafted_by:` as a plain provenance count; the "pages resting only on AI-drafted sources" count and list are gone, and the review queue is ordered by links, not by drafter.
- README: the AI-drafting line now says the same.
`drafted_by:` and `sb:aiDrafted` stay, for AI-use disclosure.

## [2026-11-16] ingest | S180 to S187: the EXTRAN test models, the 2006 QA report, Rosetta Stone 2.6.2, the unified 2D engine, and Bob on purpose and testing
Bob said "ingest and then merge" at 19:18 Eastern; simulation sources first, as the schema now says.
- S180 to S183: four LinkedIn articles of April 2025 on EXTRAN manual Examples 1, 2, 5, 6 and 7. Same frame, template slips noted, .inp summaries "created with AI Help". Each dates the SWMM3 to SWMM4 and SWMM4 to SWMM5 checks two ways (Q93). The AI summary of Example 6 calls the Type 1 curve's volumes "ft head"; S185 and S186 give cubic feet.
- S184: Bob's 2023 article on ICM's one 2D engine (MULFLOOD) shared by InfoWorks and ICM SWMM networks; conversion errors and the SQL fix; more flooding in ICM SWMM, put down to hydrology.
- S185: EPA's 2006 quality assurance report, SWMM 4.4h against SWMM 5.0.006 on twenty examples. Long document: Chapters 1 to 4, 7 and 8 read; 5, 6 and the appendices not; nine pages of Chapter 4 missing from the raw file. SWMM 5.0.006 limited the iteration to four trials (5.2.4 allows eight). It cites the Extran Addendum as October 1992 where S19 has August 1988 (Q94). It says SWMM 4 limits a pump to its inflow when the node would run dry; Register 31 of S186 measures XROUTE pumping from a dry junction (Q95). It supports October 2004 for SWMM 5's release (note on Q32). The five Challenge Test Cases are Bob's, from CDM.
- S186: Rosetta Stone 2.6.2, superseding S75 (superseded_by added). Over 15,000 words, read in part. 1,342 runs; Examples 2 to 7 on ten configurations; Registers 23 and 31 to 33. XROUTE's -6.87 percent on Example 7 is SWMM 4's figure in S185. Its quote of 5.2.4's dry-node pump rule goes into Q62, which stays open.
- S187: Bob's two statements of the evening, filed as a note in his words: the wiki is for model comparison and the AI-drafted summaries are by design (19:14), and he dogfoods and tests his apps with fifty years of testing behind him (19:24). CLAUDE.md's Purpose paragraph and the README cite it.
- New pages: The EXTRAN manual test models; SWMM 4 against SWMM 5: the 2006 quality assurance tests. Added paragraphs on 14 reviewed pages (each flagged changed_after_review) and on two unread ICM pages.
- Grok's second review (A, 94/100, as a comparison and simulation substrate) suggested making `verification` mandatory on comparison claims, with `tested_on` when the verification is a run. Done: `tools/ontology.py` reports a `same_as`, `close_match` or `approximates` row without them as an error; ONTOLOGY.md says so. A scratch copy with two such rows gave the two errors.
- Every number on the new source and concept pages was matched to the batch's raw files by script; the only ones not found there are word counts, the 159 s total of Table 7.1 (ours; SWMM 5 totals 143 s) and 42.4 cfs, our conversion of 1.2 m3/s. S186's run counts were added up at ingest.

## [2026-11-16] merge | grok-review into main
Bob said "ingest and then merge". Branch grok-review (Grok's first review, the license, drafted_by on the source pages, Chapter 5 of the EPA hydraulics manual, the simulation-first purpose, the Doc tab's "What is unique" section, and this batch) fast-forwarded into main.

## [2026-11-16] setup | Two raw folders: talks/ and press/
Bob supplied a webinar transcript and a press release and said "add it now". Neither fits an existing folder, so `raw/talks/` (transcripts of talks and webinars Bob gave, as supplied, with a short header) and `raw/press/` (press releases and announcements about his work, as supplied) were added, and CLAUDE.md's layout lists them.

## [2026-11-16] ingest | S188 to S190: the 2021 Water Talks webinar, Bob's note on joining Innovyze, the 2008 press release
Bob, 19:32 to 19:45 Eastern, in a Claude session other than the one that ingested S180 to S187: the time-stamped transcript of the Water Talks webinar he gave with Nathan of Innovyze on the ICM SIM and ICM SWMM engines, its link (https://lnkd.in/p/gX8v9RQB, which the agent's workspace could not open), his account of when he joined Innovyze, and the press release of 18 January 2008. "add it now".
- S188: the webinar, about 62 minutes, read in full. An automatic caption transcript: Claude's readings of garbled terms (Preissmann, EXTRAN, halving, Sjöberg, WALLRUS, One SWMM) are listed on the source page. Undated; 27 April 2021 is our inference (Q96). Only the page's "Read More" and "Show less" lines were removed from the raw file, as its header says.
- S189: Bob's words, "I agreed to go work at Innovyze the week of christmas, took off a few weeks went to Los Angeles after the 2nd of Janualy". The years are Claude's reading.
- S190: MWH Soft's press release. It is the primary document for the announcement that S11 prints, and differs from S11's version in five places (Q97): MWH Soft, not "Innovyze"; Urban Drainage Technology Leader, not Product Sector Leader; over thirty years, not 35; "A principal developer", not "the principal developer"; two products, not four.
- New page: [Time stepping in ICM and SWMM 5](wiki/concepts/time-stepping-icm-and-swmm5.md).
- Added paragraphs, each flagged changed_after_review where Bob had reviewed the page: SWMM 5 versus ICM InfoWorks, Preissmann slot and surcharge, InfoWorks ICM, EPA SWMM 5, Robert (Bob) Dickinson, InfoSWMM and InfoSewer, the overview, the open questions; and Checking a SWMM5 model's conversion into ICM (not reviewed).
- Open questions: Q96 and Q97 added; a sentence added to Q01 (a third, spoken date for the slot), Q05 (the release says "A principal developer"), Q13 (Bob says ICM holds SWMM 5 water quality and LIDs) and Q29 (start settled: agreed at the end of 2007, started January 2008; S55's 2005 and the end year remain).
- Three pages are past 600 words and due a split at the next lint: SWMM 5 versus ICM InfoWorks, Checking a SWMM5 model's conversion into ICM, and Robert (Bob) Dickinson.
- Every number on the new pages was checked against the transcript and the release.

## [2026-11-16] ingest | S191: Kukkonen and others (2022), the Flow Systems Ontology

Bob supplied the paper (Automation in Construction 134, 104067; open access, CC BY 4.0) and said "add it". It is the first journal paper by other authors in `raw/`, so a new folder `raw/papers/` holds it with `raw/papers/_SOURCE.md` giving its provenance and license; `CLAUDE.md` lists the folder and `LICENSE` names its terms. The PDF is copied byte for byte (SHA-256 6e8d322b...).

Ingested as S191. New page: [Flow Systems Ontology (FSO)](wiki/concepts/flow-systems-ontology.md). `ONTOLOGY.md` gains the `fso` prefix and a section proposing an alignment of seven SWMM 5 objects (as S60 describes them) to FSO's component classes; neither source states the alignment, no Relations table uses it, and Q98 asks Bob to accept or change it. The paper is about building HVAC and never mentions drainage; its authors say use outside HVAC was not investigated and that FSO describes topology only.

Counts: 191 of 427 raw files ingested, 232 queued. Lint: 0 errors.

## [2026-11-17] ingest | S192 to S202: eleven app summaries on engines and comparisons

Bob uploaded eleven app summaries to `raw/apps/` on 17 November 2026 and said "ingest and then merge". All eleven report runs or comparisons, so they come first in his order. Three ship with their apps (S192 SWMM QA Report Bench, S197 SWMM5 Engine Race, S201 InfoSewer_2009); eight are summaries Claude wrote on 16 November from the published pages, with nothing rerun (S193 SWMM 3 Runoff & Transport, S194 SWMM 4 Twin Engines, S195 swmm5-kw, S196 SWMM5 RASPIPE, S198 Two Engines One Town, S199 Seven SWMM Engines, S200 One SWMM, S202 One Model Three Engines). Q99 asks Bob to read the eight.

- New pages (14): SWMM QA Report Bench, SWMM 3 Runoff & Transport, SWMM 4 Twin Engines, SWMM5 Engine Race, Two Engines One Town, Seven SWMM Engines, One SWMM, InfoSewer_2009, One Model Three Engines (apps); swmm5-kw, SWMM5 RASPIPE, swmm5-infosewer, SWMM Results Kit; and EPANET, named on twenty pages with no page of its own.
- Added paragraphs, flagged changed_after_review where Bob had reviewed the page: block architecture, byte-for-byte gate, continuity is not validation, converting models for older engines, dynamic wave routing, engine speed, findings register, force main friction, hot start, kinematic wave and steady flow, OpenSWMM 6 solvers measured, pumps, reading SWMM output, SWMM version history, wasm against native, weirs and outlets, wrap translate or extend; the corpus, EPA SWMM 5, OpenSWMM 6 and HydroCouple, the EXTRAN III Workbench, Bellinge, InfoSWMM and InfoSewer; the overview and the open questions. Not reviewed, edited directly: the 2006 QA page, the EXTRAN test models, conversion checks into ICM, cycles and trees.
- Open questions: Q99 (the eight summaries), Q100 (which Example 1 peak each app reports: 73.9 or 71.18 cfs), Q101 (InfoSewer's 339,295 ft3 is 14.68 percent, printed 14.6; seven of swmm5-kw's 3,218 what-if models unaccounted for), Q102 (the SWMM 3 page says no Version III listing survives, while EXTRAN III runs from its printed 1981 listing). Sentences added to Q47 (more app-local finding labels, among them F-1, which looks like the register's own series), Q55 (two more apps name the math library) and Q94 (the SWMM 3 page dates the SWMM 4 User's Manual 1988).
- Agreements noted: swmm5-kw's 3,737 identical models and swmm5-infosewer's 11,894,156 values match the counts S70 gave; One SWMM's 73.90 cfs matches Seven SWMM Engines.
- Every number in the new source and entity pages was checked by script against its raw file; the arithmetic that can be redone is in each source page's "Checked at ingest".
- Lint is overdue (the last was on 16 November, five ingests ago). Seven pages crossed 600 words in this ingest: byte-for-byte gate, hot start, the 2006 QA page (609, after its addition was cut back to a pointer), weirs and outlets, wrap translate or extend, Bellinge, the corpus. Fourteen more were already past it.
- The InfoSewer_2009 summary calls its model a real utility's network and asks that the app stay private unless the utility agrees. The wiki names neither the utility nor its location.

Counts: 202 of 438 raw files ingested, 232 queued. Lint: 0 errors, 0 warnings. Reader app rebuilt and republished.

## [2026-11-17] ingest | S203: Topsoil Recovery Check summary, version 2026-11-17

Bob said yes to correcting the app's .md and the wiki pages after two findings on 17 November 2026: the perched engine ignores DRAIN lines only when a model has a SOIL2 line, and EPA 5.2.4 reads a SOIL2 line as a second SOIL line with no error. The corrected summary is a new raw file, `raw/apps/topsoil-recovery-check-v2026-11-17.md`; the 2026-11-12 file stays as it is. Ingested as S203; S59 gets `superseded_by: S203` and is otherwise unchanged.

- Changed, each with an "Added 2026-11-17" paragraph and a changed_after_review line (all reviewed 2026-11-15 or later): LID bio-retention layers, Two-layer soil infiltration (SOIL2), the findings register, EPA SWMM 5, swmm524-perched, Topsoil Recovery Check (app). No new pages.
- Contradiction: S59 against S203 on the perched engine and DRAIN lines, Q103, ticked as settled by the run S203 reports, not by Bob. One sentence added to Q33: the SOIL2 misread has no register ID either.
- S203 also records Windows x64 builds of EPA 5.2.4 and swmm524-perched (byte-identical to Linux builds under Wine on 8 runs; not yet run on Windows) and links to the engine repository and Bob's two GitHub accounts.
- The overview did not move.

## [2026-11-17] lint | ChatGPT's review: can someone else use and continue it?

Bob passed on a review of commit 2b9ebac by ChatGPT (OpenAI). Its verdict: an experienced SWMM or ICM modeler can already understand and reuse much of the collection; what is missing is a first task for a newcomer, a few complete reference cases, a dependable link from each page to the working materials, Bob's own explanations of his decisions, and a way for someone else to maintain and review it. Its counts matched the files (397 wiki pages, 202 of 438 raw files ingested, 94 open questions, 80 pages unreviewed, 37 changed after review). It was right that the counts in README.md and index.md were stale (the README still said 423 raw files and 366 pages) and that `gallery/README.md` links three files that are not in the repository.
- `wiki/start-here.md`, a synthesis page: how to read a claim; four first tasks that each end in something done (modeler: EXTRAN4 and the weir's surcharge flag, from S192; developer: swmm5-ruby against EPA 5.2.4, from S45; ICM user: the two-pipe benchmark, from S165, not yet run; maintainer: one page and the checker); where the working materials are. Linked first from the README and from index.md.
- `tools/state.py` writes the counts into README.md and index.md between `<!-- state:KEY -->` markers; `tools/lint.py` warns when one is stale; ingest step 8 in CLAUDE.md now runs it. That is a schema change: merging this branch accepts it.
- Counted from the `links:` lines of the 94 ingested app summaries: 29 name a GitHub repository or a live Netlify address, 16 only a Claude artifact, 49 neither.
- Q104 to Q107 for Bob: keeping the assets available, review by someone other than Bob, the explanations only he can give, a rehearsal with a colleague. Not done here: the reference cases themselves, which need runs, and the gallery files, which Bob holds.
- This branch, gpt-review-2026-11-17, starts from fix-topsoil-drain-soil2 (S203), so merging it merges that too.

## [2026-11-17] ingest | S204: step 1 of the two-pipe benchmark, run

Bob said "go" to the first step of the two-pipe benchmark that ChatGPT designed (S165) and its review of 17 November called one of the highest-value additions. Claude built EPA SWMM 5.2.4 from the v5.2.4 source with swmm5-ruby's reference Makefile (gcc 13.3.0, `-O2`, glibc 2.39, x86-64 with FMA and AVX2: the port's reference platform), cloned swmm5-ruby at 0c97906, wrote the model from S165's description, ran it in both engines and filed the run as `raw/notes/two-pipe-benchmark-step1-run-2026-11-17.md`, then ingested it as S204.
- Result: `.out` byte-identical and `.rpt` identical apart from the three time lines, at a fixed 1 s step and at EPA's default 20 s variable step. Outfall peak 0.9665 cfs at minute 21, J1 0.4356 ft at minute 20, continuity 0.000 %. The note tabulates all 59 minutes as the reference for the ICM steps.
- Found: the 1-hour run writes 59 records, because `project.c` line 165 floors 3599.9999997904524 s to 3599. A third sighting for [Run duration floored to whole seconds], and a second source for its line number. Ending at 01:01:00 writes 60 records and leaves minutes 1 to 59 unchanged.
- Pages changed: run-duration-floor, swmm5-to-icm-conversion-checks, swmm5-language-ports, start-here (task 3), overview (theme 3), open questions (Q16 and Q90 stay open: no ICM run), index.
- The options S165 leaves open (dynamic wave, the 1 s step, EPA's defaults for the rest, the start date) were Claude's choice and are listed in the note. Steps 2 and 3 need ICM.
