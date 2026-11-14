# Index

Every page in the wiki, one line each. An agent reads this first. Updated on every ingest. Last update: 2026-11-14 (67 sources, 36 concepts, 28 entities).

## Start here
- [Overview: what this wiki holds so far](wiki/overview.md): what the wiki holds so far, by Bob's six themes, and what is missing.
- [Open questions](wiki/open-questions.md): 41 contradictions, doubtful numbers and gaps waiting for a source or for Bob, and 3 settled by a primary document.
- [Schema](CLAUDE.md): how the wiki is kept. [Log](log.md): what was done and when.

## Concepts

Hydraulics
- [Dynamic wave routing](wiki/concepts/dynamic-wave-routing.md): SWMM 5's node-link solution of the St. Venant equations, its inherited stability options, and why it tops the forum's problem list.
- [Kinematic wave and steady flow routing](wiki/concepts/kinematic-wave-and-steady-flow.md): the two simpler routing methods, their dendritic limit, and which products have them.
- [Preissmann slot and surcharge](wiki/concepts/preissmann-slot-and-surcharge.md): slot against EXTRAN surcharge; SLOT arrived in 5.1.013; the two reach different steady states (F-0001).
- [Conduit lengthening](wiki/concepts/conduit-lengthening.md): storage that does not exist and that continuity does not flag (F-0007).
- [Force main friction](wiki/concepts/force-main-friction.md): Manning 2.53, Hazen-Williams 3.21, Darcy-Weisbach 1.58 cfs for one 12 in pipe.

Hydrology
- [Runoff surfaces and subarea routing](wiki/concepts/runoff-surfaces-and-subarea-routing.md): three subareas, three routing options, and their ICM equivalents.
- [Subcatchment width](wiki/concepts/subcatchment-width.md): a fitting knob presented as a length; Bob's objection to one width for all subareas.
- [Infiltration methods](wiki/concepts/infiltration-methods.md): Curve Number, Horton, Modified Horton and Green-Ampt by their entry points in the code.
- [Green-Ampt Newton test order](wiki/concepts/green-ampt-newton-test-order.md): a candidate finding in `infil.c`: the correction is tested before it is applied; one clay run lost 21 % of its infiltration at a 15 s wet step. Not rerun.
- [RDII unit hydrographs (RTK)](wiki/concepts/rdii-unit-hydrographs.md): R, T and K, unit hydrograph groups, and the interface file format.
- [Two-layer soil infiltration (SOIL2)](wiki/concepts/two-layer-infiltration.md): Bob's SOIL2 proposal, a second soil layer through the LID machinery.
- [Design storms and temporal patterns](wiki/concepts/design-storm-patterns.md): hyetographs from mass curves, who each pattern is credited to, and why a closed volume does not make a pattern right.
- [LID bio-retention layers](wiki/concepts/lid-bioretention-layers.md): the storage-layer and no-storage setups, soil ET off while infiltrating, and defect D2 (a drain with no storage layer makes water).
- [Topsoil over compacted clay](wiki/concepts/topsoil-over-compacted-clay.md): one soil pair, five SWMM setups, 67.1 to 100.0 % of big winter storms captured.
- [Evaporation during rain (DRY_ONLY)](wiki/concepts/evaporation-during-rain.md): switching it off moves capture by 1.3 points at most, and why.

Reading and trusting results
- [Reading SWMM output](wiki/concepts/reading-swmm-output.md): why the summary table says 73.9 cfs and the .out file 71.18 cfs for the same conduit.
- [Continuity is not validation](wiki/concepts/continuity-is-not-validation.md): four cases where the mass balance closed and the answer was wrong, or the check itself was.
- [Verification against printed runs](wiki/concepts/verification-against-printed-runs.md): how the rebuilt 1971 and 1981 engines are scored against old printouts.
- [The missing specification](wiki/concepts/the-missing-specification.md): four of the ten problems are one: no written, testable statement of what the engine does.
- [SWMM 5 versus ICM InfoWorks](wiki/concepts/swmm5-versus-icm-infoworks.md): thirteen differences in one table.

History
- [SWMM version history, 1969 to 2026](wiki/concepts/swmm-version-history.md): dated timeline, 1969 to 2026, with the disagreements marked.
- [Block architecture and interface files](wiki/concepts/block-architecture.md): the 1971 blocks, the interface tape, and what SWMM 5 unified.
- [Engine speed, 1988 to 2024](wiki/concepts/engine-speed-1988-2024.md): the 54,060-fold claim and a check of its arithmetic.

Measurement and method
- [The top 25 problems in 31 years of forum threads](wiki/concepts/forum-problems-top-25.md): what 2,879 forum threads were about, ranked.
- [The SWMM findings register](wiki/concepts/findings-register.md): the numbered record of what was checked; seed entries F-0001 to F-0014.
- [Negative results](wiki/concepts/negative-results.md): five ideas that did not work, kept on purpose.
- [App complexity index (HydroCouple = 100)](wiki/concepts/app-complexity-index.md): the eight-dimension index with HydroCouple = 100, and nine scores on record.
- [Six quality markers for app-building work](wiki/concepts/app-quality-markers.md): six markers of checking in Bob's app-building conversations, by quarter.
- [App build contract (four working principles)](wiki/concepts/app-build-contract.md): four working principles and the floor every app ships with.
- [A surrogate distilled from SWMM](wiki/concepts/surrogate-distilled-from-swmm.md): an idea at seed stage: train the emulator on SWMM's own storms.
- [Byte-for-byte gate](wiki/concepts/byte-for-byte-gate.md): how a translation is held to its original: identical `.out`, `.rpt` but three clock lines, same exit code, on 480 + 452 decks.
- [Matching glibc math in a translation](wiki/concepts/glibc-math-in-translation.md): 19 math functions, two routes (translate glibc's code, or call the system glibc), and how each is tested.
- [What the gate cannot see](wiki/concepts/gate-blind-spots.md): controls, checked builds, runtime replays, untested paths, and models stopped at the limit.
- [Where languages part from C](wiki/concepts/where-languages-part-from-c.md): the traps the SWMM5 translations met, from the sign of zero to HotSpot's method-size limit.
- [Calibration, validation and uncertainty](wiki/concepts/calibration-validation-uncertainty.md): William James's rules as Bob reports them, and the thresholds his app teaches (NSE 0.7, peak 15 %, volume 10 %).

Economics
- [Cost allocation by cooperative game theory](wiki/concepts/cost-allocation-methods.md): SCRB, MCRS, Shapley value, nucleolus and equal split on a $7M project for three towns.

## Entities

Engines and programs
- [SWMM 1 (1971)](wiki/entities/swmm-1.md): the 1971 program: builders, blocks, methods, and 14 faults found in the listing.
- [EXTRAN](wiki/entities/extran.md): the dynamic-wave block before SWMM 5, its test models, and its rebuild.
- [EPA SWMM 5](wiki/entities/swmm-5.md): the C rewrite of 2004: origin, releases, status, Bob's variants.
- [InfoWorks ICM](wiki/entities/infoworks-icm.md): the Wallingford and Autodesk engine: solver, surcharge, network types.
- [InfoSWMM and InfoSewer](wiki/entities/infoswmm-and-infosewer.md): the two Innovyze products Bob led from 2008.
- [OpenSWMM 6 and HydroCouple](wiki/entities/openswmm-6-and-hydrocouple.md): the commit the translations start from, licence, modules, and four findings.
- [SWMM6 language translations (swmm6-*)](wiki/entities/swmm6-language-ports.md): thirteen languages, results table, how each was made and rechecked.
- [SWMM5 language translations (swmm5-*)](wiki/entities/swmm5-language-ports.md): EPA SWMM 5.2.4 in 19 languages, results and speeds as published, how the back ends descend from each other.
- [swmm6-rust](wiki/entities/swmm6-rust.md): OpenSWMM 6 in safe Rust, 1D on 932 decks and 2D on 1,315 of 1,415, with state-level gates.
- [swmm524-perched](wiki/entities/swmm524-perched.md): EPA 5.2.4 plus SOIL2, van Genuchten and STRUCT lines; byte-identical to 5.2.4 without them.

Apps
- [SWMM 1 Engine (app)](wiki/entities/swmm-1-engine-app.md): three engines in one page, version 3.6.
- [SWMM App Complexity Meter (app)](wiki/entities/swmm-app-complexity-meter.md): version 1.9.1, its checks and limits.
- [SWMM and ICM St. Venant comparison (app)](wiki/entities/swmm-icm-st-venant-app.md): the Replit comparison app behind Edition 54.
- [Claude chat archive (app)](wiki/entities/claude-chat-archive.md): 1,671 conversations and 800 apps as of 14 October 2026.
- [Topsoil Recovery Check (app)](wiki/entities/topsoil-recovery-check.md): five engines in one page, verify.py with 1,181 cases, version 2026-11-12.
- [Rules for Responsible Modeling (app)](wiki/entities/rules-for-responsible-modeling-app.md): the Lovable edition of William James's book, with EPA SWMM 5.2.4 in the page; 61 of 61 tests, version 2026.1.2.
- [Cost Allocation Game Theory Explorer (app)](wiki/entities/cost-allocation-explorer.md): the Lovable app of the 1982 Heaney and Dickinson paper; five methods, 101 of 101 tests, version 1.0.1.
- [World Rainfall Pattern Painter (app)](wiki/entities/world-rainfall-pattern-painter.md): the Lovable design-storm generator; 339 patterns (3 High, 57 Medium, 279 Low confidence), 1,502 of 1,502 tests, version 3.2.0.

Data
- [1729-SWMM5-Models-2030 (the corpus)](wiki/entities/corpus-1729.md): Bob's public model repository; 480 of its models are the translations' gate set.

Sites
- [OpenSWMM.org (the forum)](wiki/entities/openswmm-forum.md): Bob's 4,014 posts in 2,879 threads since 1995.
- [swmm5.org](wiki/entities/swmm5-org.md): the WordPress site and its six topic pages.

Repositories
- [Bob's GitHub repositories (where the rest of the material lives)](wiki/entities/bobs-github-repositories.md): 30 repositories named in the sources, with Bob's description of each; the map for future ingests.
- [swmm-brain (the old brain repository)](wiki/entities/swmm-brain-repo.md): the earlier brain repository this one replaced, and what carried over.

People
- [Robert (Bob) Dickinson](wiki/entities/robert-dickinson.md): professional timeline from his own articles, with the dates that disagree.
- [Lewis A. (Lew) Rossman](wiki/entities/lew-rossman.md): author of EPANET and of the SWMM 5 engine.
- [Wayne C. Huber](wiki/entities/wayne-huber.md): first author of the SWMM 3 and SWMM 4 manuals.
- [James P. (Jim) Heaney](wiki/entities/james-heaney.md): co-author of the SWMM 3 manual and first author of the 1982 cost allocation paper.
- [William (Bill) James](wiki/entities/william-james.md): author of Rules for Responsible Modeling (2005); taught the 1978 SWMM 2 class Bob took.

## Sources

App summaries
- [S01](wiki/sources/S01-swmm1-engine-app-md.md) (2026-11-13): SWMM 1 Engine, technical summary, v3.6.
- [S02](wiki/sources/S02-complexity-meter-app-md.md) (2026-11-11): SWMM App Complexity Meter, technical summary, v1.9.1.
- [S59](wiki/sources/S59-topsoil-recovery-check-app-md.md) (2026-11-12): Topsoil Recovery Check, technical summary, version 2026-11-12.
- [S61](wiki/sources/S61-cost-allocation-explorer-app-md.md) (2026-11-14): Cost Allocation Game Theory Explorer, technical summary, v1.0.1.
- [S62](wiki/sources/S62-rules-for-responsible-modeling-app-md.md) (2026-11-14): Rules for Responsible Modeling, technical summary, v2026.1.2.
- [S65](wiki/sources/S65-world-rainfall-pattern-painter-app-md.md) (2026-11-14): World Rainfall Pattern Painter, technical summary, v3.2.0.

Manuals and reports (primary documents)
- [S60](wiki/sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) (2017-05): EPA SWMM Reference Manual, Volume II, Hydraulics, by L. A. Rossman. Read in part: section 1.1 and Chapter 3.

Notes and data
- [S03](wiki/sources/S03-findings-register-format.md) (2026-10-09): findings register, format and twenty candidates.
- [S04](wiki/sources/S04-findings-register-seed.md) (2026-10-09): findings register, seed entries F-0001 to F-0014.
- [S05](wiki/sources/S05-swmm5org-article-facts.md) (2026-10-16): fact sheet measured from the chat archive.
- [S09](wiki/sources/S09-openswmm-thread-list.md) (2026-11-01): OpenSWMM thread list, 1995 to 2026.
- [S10](wiki/sources/S10-openswmm-top25-problems.md) (2026-11-06): top 25 problems tagged from thread titles.
- [S67](wiki/sources/S67-note-green-ampt-newton-test-order.md) (2026-11-14): note, the Green-Ampt Newton loop tests its correction before applying it.

The old swmm-brain repository
- [S55](wiki/sources/S55-swmm-brain-readme.md) (2026-08-22): README: enhancements, apps, scripts, timeline.
- [S56](wiki/sources/S56-swmm-brain-note-surrogate.md) (2026-06-29): note, a surrogate distilled from SWMM's own storms.
- [S57](wiki/sources/S57-swmm-brain-setup-script.md) (2026-08-22): setup.sh, the list of knowledge repositories.
- [S58](wiki/sources/S58-swmm-brain-working-principles.md) (2026-08-22): four working principles for building apps.

swmm5.org pages
- [S06](wiki/sources/S06-swmm5org-topics-index.md) (2026-11-01): Topics landing page.
- [S07](wiki/sources/S07-swmm5org-topic-swmm-history.md) (2026-11-01): topic page, SWMM History.
- [S08](wiki/sources/S08-swmm5org-topic-inside-swmm5.md) (2026-11-01): topic page, Inside SWMM5.

LinkedIn articles
- [S11](wiki/sources/S11-li-my-history-with-swmm.md) (2016-11-18): My History with Various Versions of SWMM.
- [S16](wiki/sources/S16-li-rdii-in-swmm5.md) (2019-10-04): How Does RDII Work in SWMM5, InfoSWMM and InfoWorks ICM?
- [S13](wiki/sources/S13-li-three-runoff-surfaces.md) (2024-02-01): A Tale of Three Runoff Surfaces in SWMM5.
- [S14](wiki/sources/S14-li-subarea-routing.md) (2024-02-03): Subcatchment Subarea Internal Routing.
- [S15](wiki/sources/S15-li-hydrology-code-story.md) (2024-02-10): A Story about the C-Code Hydrology of SWMM5.
- [S19](wiki/sources/S19-li-edition-29-engine-speed.md) (2024-04-28): Edition 29, the 54,000-fold speed improvement.
- [S17](wiki/sources/S17-li-routing-options.md) (2024-07-28): Steady State, EPS, Kinematic and Dynamic Wave Options.
- [S12](wiki/sources/S12-li-diamond-village.md) (2024-12-22): Diamond Village at the University of Florida.
- [S18](wiki/sources/S18-li-invalid-hydraulic-solutions-poster.md) (2024-12-22): Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5 (2007 poster).
- [S20](wiki/sources/S20-li-edition-54-two-solvers.md) (2026-02-23): Edition 54, Two Solvers, One Equation.
- [S21](wiki/sources/S21-li-edition-56-swmm-history.md) (2026-03-02): Edition 56, The $350,000 Model.
- [S22](wiki/sources/S22-li-ten-problems.md) (2026-11-05): Ten Problems with How SWMM Was Developed and Explained.
- [S63](wiki/sources/S63-li-edition-53-measure-of-honest-numbers.md) (2026-02-23): Edition 53, The Measure of Honest Numbers: William James and the app of his book.
- [S64](wiki/sources/S64-li-heaney-1982-paper-cost-allocation-app.md) (2026-03-08): From a 1982 Water Resources Paper to an Interactive App: Jim Heaney and the cost allocation app.
- [S66](wiki/sources/S66-li-design-storm-app-66-patterns.md) (2026-02-25): Design Storm App for 6 Continents and 66 Patterns: the rainfall app as announced.

Repository READMEs (SWMM6 translations)
- [S23](wiki/sources/S23-swmm6-csharp-readme.md) (2026-11-04): swmm6-csharp, the OpenSWMM 6 engine in C#; 480 of 480, 452 of 452.
- [S24](wiki/sources/S24-swmm6-go-readme.md) (2026-11-04): swmm6-go, the OpenSWMM 6 engine in Go; 480 of 480, 452 of 452.
- [S25](wiki/sources/S25-swmm6-java-readme.md) (2026-11-04): swmm6-java, the OpenSWMM 6 engine in Java; 480 of 480, 452 of 452.
- [S26](wiki/sources/S26-swmm6-typescript-readme.md) (2026-11-05): swmm6-typescript, the OpenSWMM 6 engine in TypeScript; 480 of 480, 452 of 452.
- [S27](wiki/sources/S27-swmm6-fortran-readme.md) (2026-11-04): swmm6-fortran, the OpenSWMM 6 engine in Fortran; 480 of 480, 452 of 452.
- [S28](wiki/sources/S28-swmm6-python-readme.md) (2026-11-06): swmm6-python, the OpenSWMM 6 engine in Python; 412 of 413 run, 450 of 452.
- [S29](wiki/sources/S29-swmm6-rust-readme.md) (2026-11-12): swmm6-rust, the OpenSWMM 6 engine in Rust; 1D on all 932 decks; 2D on 1,315 of 1,415.
- [S30](wiki/sources/S30-swmm6-kotlin-readme.md) (2026-11-10): swmm6-kotlin, the OpenSWMM 6 engine in Kotlin; 480 of 480, 452 of 452.
- [S31](wiki/sources/S31-swmm6-groovy-readme.md) (2026-11-10): swmm6-groovy, the OpenSWMM 6 engine in Groovy; 480 of 480, 452 of 452.
- [S32](wiki/sources/S32-swmm6-javascript-readme.md) (2026-11-10): swmm6-javascript, the OpenSWMM 6 engine in JavaScript; 480 of 480, 452 of 452.
- [S33](wiki/sources/S33-swmm6-fsharp-readme.md) (2026-11-10): swmm6-fsharp, the OpenSWMM 6 engine in F#; 480 of 480, 452 of 452.
- [S34](wiki/sources/S34-swmm6-hy-readme.md) (2026-11-10): swmm6-hy, the OpenSWMM 6 engine in Hy; 478 of 480, 450 of 452.
- [S35](wiki/sources/S35-swmm6-ruby-readme.md) (2026-11-12): swmm6-ruby, the OpenSWMM 6 engine in Ruby; 478 of 480, 450 of 452.

Repository READMEs (SWMM5 translations)
- [S36](wiki/sources/S36-swmm5-fortran-readme.md) (2026-11-06): swmm5-fortran, EPA SWMM 5.2.4 in Fortran; 480 of 480.
- [S37](wiki/sources/S37-swmm5-csharp-readme.md) (2026-11-06): swmm5-csharp, EPA SWMM 5.2.4 in C#; 480 of 480.
- [S38](wiki/sources/S38-swmm5-python-readme.md) (2026-11-06): swmm5-python, EPA SWMM 5.2.4 in Python; 465 (14 of 29 slow sampled).
- [S39](wiki/sources/S39-swmm5-typescript-readme.md) (2026-11-06): swmm5-typescript, EPA SWMM 5.2.4 in TypeScript; 480 of 480.
- [S40](wiki/sources/S40-swmm5-java-readme.md) (2026-11-06): swmm5-java, EPA SWMM 5.2.4 in Java; 480 of 480.
- [S41](wiki/sources/S41-swmm5-go-readme.md) (2026-11-06): swmm5-go, EPA SWMM 5.2.4 in Go; 480 of 480; the corpus, controls and math census.
- [S42](wiki/sources/S42-swmm5-kotlin-readme.md) (2026-11-08): swmm5-kotlin, EPA SWMM 5.2.4 in Kotlin; 480 of 480.
- [S43](wiki/sources/S43-swmm5-pascal-readme.md) (2026-11-08): swmm5-pascal, EPA SWMM 5.2.4 in Free Pascal; 480 of 480.
- [S44](wiki/sources/S44-swmm5-zig-readme.md) (2026-11-08): swmm5-zig, EPA SWMM 5.2.4 in Zig; 480 of 480.
- [S45](wiki/sources/S45-swmm5-ruby-readme.md) (2026-11-09): swmm5-ruby, EPA SWMM 5.2.4 in Ruby; 478 of 480, 2 not run.
- [S46](wiki/sources/S46-swmm5-javascript-readme.md) (2026-11-09): swmm5-javascript, EPA SWMM 5.2.4 in JavaScript; 480 of 480.
- [S47](wiki/sources/S47-swmm5-php-readme.md) (2026-11-09): swmm5-php, EPA SWMM 5.2.4 in PHP; 480 of 480.
- [S48](wiki/sources/S48-swmm5-fsharp-readme.md) (2026-11-09): swmm5-fsharp, EPA SWMM 5.2.4 in F#; 480 of 480.
- [S49](wiki/sources/S49-swmm5-perl-readme.md) (2026-11-09): swmm5-perl, EPA SWMM 5.2.4 in Perl; 478 of 480, 2 not run.
- [S50](wiki/sources/S50-swmm5-groovy-readme.md) (2026-11-09): swmm5-groovy, EPA SWMM 5.2.4 in Groovy; 480 of 480.
- [S51](wiki/sources/S51-swmm5-lua-readme.md) (2026-11-09): swmm5-lua, EPA SWMM 5.2.4 in Lua; 480 of 480.
- [S52](wiki/sources/S52-swmm5-hy-readme.md) (2026-11-10): swmm5-hy, EPA SWMM 5.2.4 in Hy; 480 of 480.
- [S53](wiki/sources/S53-swmm5-mojo-readme.md) (2026-11-10): swmm5-mojo, EPA SWMM 5.2.4 in Mojo; 480 of 480.
- [S54](wiki/sources/S54-swmm5-r-readme.md) (2026-11-12): swmm5-r, EPA SWMM 5.2.4 in R; 465 of 480, 15 not run.

## Queue

247 raw files are queued: 213 LinkedIn articles, 19 manual files in `raw/manuals/` (8 EPA, USGS and FHWA documents not yet started, and 11 SWMM 4.4 documentation files), 9 app files, 4 swmm5.org topic pages and 2 SWMM 1 build notes. Three more LinkedIn files are byte-identical copies of others and are marked `duplicate`. One queued app file, SWMM 1 Engine 3.12, is a newer version of an ingested one (3.6) and should go early. `raw/MANIFEST.csv` lists them all. Suggested next batches, in order:

0. The rest of the EPA hydraulics manual, a chapter at a time (S60 is read in part), then the 2006 quality assurance report and the SWMM 5.1 User's Manual. These are the primary documents; ingesting them first lets later articles be checked against them.
1. The four remaining swmm5.org topic pages and the SWMM 1 build notes (small, and they complete themes 3 to 6).
2. EXTRAN: the six test-file articles and Edition 38. Settles Q14.
3. SWMM history: Edition 40, "SWMM1 to SWMM5 Documentation Archive", "Reviving 1988 SWMM4 Models with AI", "SWMM 44H Fortran Code".
4. Inside SWMM5: the dynwave.c and dwflow.c stories, "Understanding SWMM5 through the Tables in text.h and keywords.h", "100 SWMM5 Quiz Questions".
5. SWMM5 and ICM: the DWF, RDII, groundwater, runoff surface and buildup and washoff comparisons. Settles Q13.
6. Ruby and SQL for ICM: 70 articles; ingest by family, not one by one.
