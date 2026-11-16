# Index

Every page in the wiki, one line each. An agent reads this first. Updated on every ingest. Last update: 2026-11-14 (72 sources, 38 concepts, 32 entities).

## Start here
- [Overview: what this wiki holds so far](wiki/overview.md): what the wiki holds so far, by Bob's six themes, and what is missing.
- [Open questions](wiki/open-questions.md): 56 contradictions, doubtful numbers and gaps waiting for a source or for Bob, and 3 settled by a primary document.
- [Schema](CLAUDE.md): how the wiki is kept. [Log](log.md): what was done and when.

## Concepts

Hydraulics
- [Dynamic wave routing](wiki/concepts/dynamic-wave-routing.md): SWMM 5's node-link solution of the St. Venant equations, its inherited stability options, and why it tops the forum's problem list.
- [Kinematic wave and steady flow routing](wiki/concepts/kinematic-wave-and-steady-flow.md): the two simpler routing methods, their dendritic limit, and which products have them.
- [SWMM 5 network objects, boundary and initial conditions](wiki/concepts/swmm5-network-objects.md): the four node types, conduits, control settings, and how a run starts, from Chapter 2 of the EPA manual.
- [Pumps and pump curves](wiki/concepts/pumps-and-pump-curves.md): five pump kinds, how a curve is read, and the rule that keeps an inlet node from going dry.
- [Orifices](wiki/concepts/orifices.md): side and bottom orifices, coefficient 0.6, weir behavior when not submerged, and the surface area kept from the equivalent pipe.
- [Weirs and outlets](wiki/concepts/weirs-and-outlets.md): weir kinds and coefficients (3.33, 2.5, 2.34 to 3.32), the corrected side weir exponent, submergence, surcharge, and rating-curve outlets.
- [Preissmann slot and surcharge](wiki/concepts/preissmann-slot-and-surcharge.md): slot against EXTRAN surcharge; SLOT arrived in 5.1.013; the two reach different steady states (F-0001).
- [Conduit lengthening](wiki/concepts/conduit-lengthening.md): storage that does not exist and that continuity does not flag (F-0007).
- [Force main friction](wiki/concepts/force-main-friction.md): Manning 2.53, Hazen-Williams 3.21, Darcy-Weisbach 1.58 cfs for one 12 in pipe.
- [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](wiki/concepts/extran-solvers-xroute-yroute-zroute.md): SWMM 4.4H's three dynamic-wave solvers, what SWMM 5 kept, and how they compare on EXTRAN Example 1.
- [The crown cap at mid-pipe](wiki/concepts/crown-cap-at-mid-pipe.md): why a pipe surcharged at one end is treated as partly full at mid-length, worth 17,497 to 20,560 ft³ of flooding on one example.
- [OpenSWMM 6 solvers, measured](wiki/concepts/openswmm6-solvers-measured.md): the dynamic wave and finite-volume solvers beside SWMM 5.2.4 on an example, a channel and the Bellinge sewer.
- [Hot start: what a restart loses](wiki/concepts/hot-start-restart-state.md): 0 of 282 stock restarts reproduce the run that wrote them; five pieces of state named.
- [Run duration floored to whole seconds](wiki/concepts/run-duration-floor.md): one line of `project.c` that ends some runs a second early, met independently by two apps.

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
- [WebAssembly builds against native builds](wiki/concepts/wasm-against-native-builds.md): 59 of 449 models differ in the browser, all traced to the C math library; and ten builds of one engine.

History
- [SWMM version history, 1969 to 2026](wiki/concepts/swmm-version-history.md): dated timeline, 1969 to 2026, with the disagreements marked.
- [Block architecture and interface files](wiki/concepts/block-architecture.md): the 1971 blocks, the interface tape, and what SWMM 5 unified.
- [Engine speed, 1988 to 2024](wiki/concepts/engine-speed-1988-2024.md): the 54,060-fold claim and a check of its arithmetic.
- [Anecdotes of SWMM](wiki/concepts/swmm-anecdotes.md): recollections in people's own words: SWMM 2.5 as 20,000 punch cards, Canberra in 1991 and 1992 for XP-EXTRAN, double pipes (barrels) for a phosphate plant, reel tapes and card decks.
- [Converting SWMM 5 models for older engines](wiki/concepts/converting-swmm5-models-for-older-engines.md): what three converters to 1971, 1981 and 2004 engines carry, approximate and drop.

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
- [Wrap, translate or extend](wiki/concepts/wrap-translate-or-extend.md): three roads to SWMM in another language or with new physics, and the four engines that extend EPA's C.
- [SWMM5 translations: the re-run of 12 November 2026](wiki/concepts/swmm5-ports-rerun-2026-11.md): twenty translations rebuilt on one machine, gated again and timed by one benchmark.
- [Calibration, validation and uncertainty](wiki/concepts/calibration-validation-uncertainty.md): William James's rules as Bob reports them, and the thresholds his app teaches (NSE 0.7, peak 15 %, volume 10 %).
- [Replit apps and the summaries Replit Agent wrote](wiki/concepts/replit-app-summaries.md): the first eighteen Replit apps, what their agent-written summaries have in common and where they differ.
- [Replit apps: the second seventeen summaries](wiki/concepts/replit-app-summaries-second-batch.md): seventeen more Replit apps: which run an engine, which pass their tests, and what the agent found doubtful.
- [Replit apps: six more summaries](wiki/concepts/replit-app-summaries-third-batch.md): six more Replit apps brought over on the evening of 15 November 2026: none runs an engine, one has a test suite, four have names that do not say what they are.
- [Replit apps: a fourth set of six summaries](wiki/concepts/replit-app-summaries-fourth-batch.md): six more Replit apps and two notes of Bob's: two run an engine, none has a test that runs, one was deleted for running visitors' code.
- [LinkedIn posts that were well received](wiki/concepts/linkedin-post-reception.md): which of 50 posts were most seen, most reacted to and most answered on 15 November 2026, and where the two posts Bob named stand.

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
- [SWMM 1 Engine (app)](wiki/entities/swmm-1-engine-app.md): three engines in one page, version 3.13.
- [SWMM App Complexity Meter (app)](wiki/entities/swmm-app-complexity-meter.md): version 1.9.1, its checks and limits.
- [SWMM and ICM St. Venant comparison (app)](wiki/entities/swmm-icm-st-venant-app.md): the Replit comparison app behind Edition 54.
- [Claude chat archive (app)](wiki/entities/claude-chat-archive.md): 1,671 conversations and 800 apps as of 14 October 2026.
- [Topsoil Recovery Check (app)](wiki/entities/topsoil-recovery-check.md): five engines in one page, verify.py with 1,181 cases, version 2026-11-12.
- [Rules for Responsible Modeling (app)](wiki/entities/rules-for-responsible-modeling-app.md): the Lovable edition of William James's book, with EPA SWMM 5.2.4 in the page; 61 of 61 tests, version 2026.1.2.
- [Cost Allocation Game Theory Explorer (app)](wiki/entities/cost-allocation-explorer.md): the Lovable app of the 1982 Heaney and Dickinson paper; five methods, 101 of 101 tests, version 1.0.1.
- [SWMM5 Code House (app)](wiki/entities/swmm5-code-house.md): the 5.2.4 source as a walkable house, 58 rooms and 51,080 lines, with the engine running inside; version 1.15.1.
- [SWMM6 Code House (app)](wiki/entities/swmm6-code-house.md): the OpenSWMM 6 source as a house, 102 rooms and 351,187 lines; reads results, runs nothing; version 1.2.1.
- [SWMM Engine What If (app)](wiki/entities/swmm-engine-what-if.md): which language, for which job, by which road; version 1.4 re-ran all twenty SWMM 5 translations.
- [SWMM Engines, Byte for Byte (app)](wiki/entities/swmm-engines-byte-for-byte.md): stored gate verdicts for eight SWMM 5 and six SWMM6 translations, and five EPA 5.2.4 defects.
- [World Rainfall Pattern Painter (app)](wiki/entities/world-rainfall-pattern-painter.md): the Lovable design-storm generator; 339 patterns (3 High, 57 Medium, 279 Low confidence), 1,502 of 1,502 tests, version 3.2.0.
- [EXTRAN III Workbench (app)](wiki/entities/extran-iii-workbench.md): the 1981 EXTRAN from its printed listing; 2,253 of 2,424 printed values exact; ten faults fixed.
- [St. Venant Solver Rosetta Stone (app)](wiki/entities/st-venant-solver-rosetta-stone.md): six dynamic-wave solvers by source line and 1,157 engine runs, version 2.4.0.
- [Inside the Network (app)](wiki/entities/inside-the-network-cfd.md): a particle CFD along one path of a SWMM 5 network, beside SWMM 5.2.4.
- [Under Load (app)](wiki/entities/under-load.md): how far a design storm is from the next regime change; omega sweep; `.rpt` against `.out` flooding.
- [Fractal SWMM5/SWMM6 Network Generator (app)](wiki/entities/fractal-swmm-generator.md): 22 fractal patterns to runnable test models, with a replayed build and a pipe-by-pipe audit.
- [Teacher-Forced SWMM (app)](wiki/entities/teacher-forced-swmm.md): comparing two engine versions by restarting one from the other's state.
- [Control Section Lab (app)](wiki/entities/control-section-lab.md): one steady channel; where SWMM 5 misses a choke and critical depth, and OpenSWMM 6's finite volume does not.
- [Bellinge (app)](wiki/entities/bellinge-app.md): an open Danish sewer model through seven SWMM engines, 1981 to 2026.
- [Mirab Test Bench (app)](wiki/entities/mirab-test-bench.md): Mirab's results against EPA SWMM 5.2.4; a first-pattern defect in SWMM5+.
- [People as Pollutants (app)](wiki/entities/people-as-pollutants.md): a transit station as a SWMM 5 model, and two SWMM defaults it ran into.
- [SWMM & ICM Knowledge Library (app)](wiki/entities/swmm-icm-knowledge-library.md): 9,964 records of Bob's published work in one searchable file.
- [Bob Usefulness Index (app)](wiki/entities/bob-usefulness-index.md): a 100-point scorecard read from the library; baseline 66.
- [Master SWMM PDF (app)](wiki/entities/master-swmm-pdf.md): 38 SWMM and rainfall-runoff documents, each tied to its citation by a file fingerprint.
- [Speak 100 (app)](wiki/entities/speak-100.md): an eight-language speaking trainer; not a SWMM app.
- [SWMM5-UI (app)](wiki/entities/swmm5-ui.md): Replit app that edits SWMM models and runs them in six engine modes, among them EPA SWMM 5.2.4 and OpenSWMM 6 in the browser.
- [SWMM5 Network Miner (app)](wiki/entities/swmm5-network-miner.md): Replit app for a library of SWMM model files: search, compare, QA/QC and runs through PySWMM.
- [SWMM5 INP MAKER (app)](wiki/entities/swmm5-inp-maker.md): Replit app that generates seeded SWMM5 `.inp` models and can run them in EPA SWMM 5.2.4.
- [SWMM5 Lego Model (app)](wiki/entities/swmm5-lego-model.md): Replit app: paint a drainage layout on a grid and run it in a quick JavaScript simulation or in EPA SWMM5 as WebAssembly.
- [Camel_SWMM (app)](wiki/entities/camel-swmm.md): Replit Flask app that manages, validates and runs SWMM models through swmm-toolkit, with optional AI review.
- [SWMM5 Manual Search (app)](wiki/entities/swmm5-manual-search.md): Replit app that searches the SWMM manual: 621 indexed sections, calculators, an `.inp` runner and an AI assistant.
- [SWMM Manual Search landing page (app)](wiki/entities/swmm-manual-search-landing-page.md): Replit landing page that promotes the separate manual-search site.
- [InfoSewer and InfoSWMM Legacy Model Reader (app)](wiki/entities/infosewer-infoswmm-legacy-model-reader.md): Replit app that reads InfoSWMM ISDB and InfoSewer IEDB models from their DBF tables and prepares SWMM5 and ICM exports.
- [XPX to Shapefile Converter (app)](wiki/entities/xpx-to-shapefile-converter.md): Replit app that turns an XPSWMM XPX file into point, line and polygon shapefiles.
- [SWMM5 .inp File Viewer (app)](wiki/entities/swmm5-inp-file-viewer.md): Replit Streamlit app that shows the sections of a SWMM5 `.inp` file as tables.
- [SWMM5 Topology Sandbox (app)](wiki/entities/swmm5-topology-sandbox.md): Replit teaching app: 22 network patterns, estimated hydrographs and an INP export, with no engine.
- [Green-Ampt Infiltration Calculator (app)](wiki/entities/green-ampt-infiltration-calculator.md): Replit calculator for Green-Ampt, Modified Green-Ampt, Horton and Curve Number infiltration in its own code.
- [SWMM5 Runoff and Infiltration (app)](wiki/entities/swmm5-runoff-and-infiltration.md): Replit app with five infiltration models, LID settings and rainfall from Open-Meteo; no engine.
- [SingaPourApps (app)](wiki/entities/singapourapps.md): Replit app that parses a SWMM `.inp` file into rainfall, runoff-parameter and discharge summaries.
- [InfoDrainage Explorer (app)](wiki/entities/infodrainage-explorer.md): Replit reference and quiz app about Autodesk InfoDrainage.
- [MapSWMMSewer Code Repository (app)](wiki/entities/mapswmmsewer-code-repository.md): Private Replit app that stores and searches code files for SWMM, sewer analysis and h2oCalc.
- [City Temperature Explorer (app)](wiki/entities/city-temperature-explorer.md): Replit app comparing city temperatures across decades; not about SWMM.
- [GeoAI Flood Impact (app)](wiki/entities/geoai-flood-impact.md): Replit app presenting stored flood-exposure records; not about SWMM.
- [SWMM5 MicroGPT (app)](wiki/entities/swmm5-microgpt.md): Replit app, v2; trains a small character-level GPT on SWMM5 `.INP` text in the browser; runs no engine.
- [EPANET for SWMM5 Experts (app)](wiki/entities/epanet-for-swmm5-experts.md): Replit app, v1.0; one-page reference that explains EPANET to SWMM5 users, with 32 tabs of calculators; one of its 10 built-in checks fails.
- [SWMM5 Explorer (app)](wiki/entities/swmm5-explorer.md): Replit app, v1.0.0; browser of the SWMM 5.2.4 source with Sankey diagrams and AI explanations; its browser engine is a stub.
- [BatchSWMM56 (app)](wiki/entities/batchswmm56.md): Replit app, v1.1.0; batch runner that puts one model through seven engine entries (EPA 5.2.4, a KW/SF extension, OWA, two SWMM6 builds, Hydra) and compares the results.
- [SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)](wiki/entities/code-rosetta-stone.md): Replit app, v1.0.0; SWMM and EPANET algorithms side by side in 37 languages, and 72 engine selections that include 30 imported translations at exact commits.
- [ForceMain SWMM5 EPANET Comparison (app)](wiki/entities/forcemain-swmm5-epanet-comparison.md): Replit app, v1.0; Streamlit app that designs force mains, writes paired SWMM5 and EPANET models and runs both through PySWMM and WNTR.
- [Hindsight Prophet (app)](wiki/entities/hindsight-prophet.md): Replit app, v1.0.0; sends a stormwater-modeling question to a council of four or six AI personas and returns a consensus and roadmap; runs no engine.
- [SWMManywhere Explorer (app)](wiki/entities/swmmanywhere-explorer.md): Replit app, v1.0.0; static guide to the separate SWMManywhere Python project; generates and simulates nothing.
- [SWMM5 Modeler (app)](wiki/entities/swmm5-modeler.md): Replit app, v0.0.0; generates or imports a drainage network, runs it in EPA SWMM5 5.1.14 as WebAssembly, grades it and proposes fixes; six rule-based "agents".
- [bobSWMM Auto Research (app)](wiki/entities/bobswmm-auto-research.md): Replit app, v0.0.0; AI-written research reports and chat on SWMM questions, with browser calculators and `.inp` and `.rpt` inspectors; runs no engine.
- [Kinematic Wave Router (app)](wiki/entities/kinematic-wave-router.md): Replit app, v2026.11.15; Ruby web app that routes a constant inflow through a SWMM5 network by kinematic wave, splits and loops included; its test suite does not run.
- [SWMM Ecosystem (app)](wiki/entities/swmm-ecosystem.md): Replit app, v1.0.0; reference app on SWMM's history and the software around it: 51 catalog records, contributor cards, a 285-entry glossary; runs no model.
- [ICM InfoWorks release history (app)](wiki/entities/icm-release-history-app.md): Replit app, v1.0.0; browser of InfoWorks ICM release history: 50 releases and 822 features held in the project, with AI answers; calls no ICM engine.
- [EPANET 2.3 Generator (app)](wiki/entities/epanet-23-generator.md): Replit app, v4.6; builds synthetic water and drainage networks from a seed, runs them in EPANET and SWMM 5.1.015 in the browser, and exports the files.
- [Historical Water Inventions (app)](wiki/entities/historical-water-inventions.md): Replit app, v1.0.0; educational app on the history of water engineering: 1,286 invention records, maps, quizzes and 12 SWMM5 templates; runs no solver.
- [PySWMM Explorer (app)](wiki/entities/pyswmm-explorer.md): Replit app, v1.0.0; reference and learning app for PySWMM; its Playground prints sample output and runs no Python or SWMM.
- [SWMM5 Control Rule Editor (app)](wiki/entities/swmm5-control-rule-editor.md): Replit app, v0.1.0; browser editor that reads and writes SWMM5 `[CONTROLS]` rules; runs no engine.
- [SWMM5 & EPANET INP Explorer (app)](wiki/entities/swmm5-epanet-inp-explorer.md): Replit app, v1.0.0; reference to the SWMM and EPANET input-file formats, with a section builder and a paste-in parser; runs no engine.
- [SWMM5 .inp File Interactive Viewer (app)](wiki/entities/swmm5-inp-file-interactive-viewer.md): Replit app, v0.1.0; Streamlit page that shows an input file's sections as data grids with statistics and charts; runs no engine.
- [SWMM5 Topo Network Wizard (app)](wiki/entities/swmm5-topo-network-wizard.md): Replit app, v1.0.0; generates network layouts from 49 topology methods and a particle simulation and exports SWMM5 input files; runs no SWMM engine.
- [SWMM Documents Explorer (app)](wiki/entities/swmm-documents-explorer.md): Replit app, v1.0.0; guide to the SWMM documentation archive: 8 eras, 13 timeline entries, 29 documents; runs no engine.
- [SWMM5 Quizzer (app)](wiki/entities/swmm5-quizzer.md): Replit app, v1.0.0; 250 multiple-choice SWMM questions, 25 a quiz, and a Simulation Quiz on stored scenarios; runs no engine.
- [SWMMCRAFT, infiltration simulator (app)](wiki/entities/swmmcraft-infiltration-simulator.md): Replit app, v1.0.0; Horton, Green-Ampt and Curve Number infiltration for one storm in its own code; runs no engine.
- [SWMM5Wiki (app)](wiki/entities/swmm5wiki.md): Replit app, v1.0.0; SWMM guide with 5 sections and 8 glossary terms, and a game of 16 challenges; runs no engine.
- [BobSWMM Writer (app)](wiki/entities/bobswmm-writer.md): Replit app, v2.1.0; drafts posts and articles with Claude from notes and recordings that Gemini transcribes.
- [ICM PRN File Reader (app)](wiki/entities/icm-prn-file-reader.md): Replit app, v1.0.0; reads InfoWorks ICM PRN output, flags flooding, surcharge and capacity, exports CSV, Excel or PDF; 24 tests pass.
- [ICM Ruby to Nano Banana Prompt (app)](wiki/entities/icm-ruby-nano-banana-prompt.md): Replit app, v1.0.0; draws a workflow from ICM Ruby scripts and counts SWMM5 sections; Gemini explains the code; runs no engine.
- [InfoSewer to InfoWorks ICM (app)](wiki/entities/infosewer-to-infoworks-icm-guide.md): Replit app, v1.0.0; guide to moving InfoSewer models into ICM, with ID, CSV and SQL checkers; converts nothing itself.
- [SWMManywhere Explorer at swm-explorer (app)](wiki/entities/swmmanywhere-explorer-swm.md): Replit app, v1.0.0; generates drainage models with SWMManywhere 0.1.17 and runs them in a SWMM5 WebAssembly engine; same app name as S122.
- [OpenSWMM Engine (app)](wiki/entities/openswmm-engine-app.md): Replit app, v6.0.0-alpha.1; runs the legacy SWMM engine of HydroCouple/OpenSWMMCore in WebAssembly; says MIT, which Bob says is no longer the license.
- [EPANET Quizzer (app)](wiki/entities/epanet-quizzer.md): Replit app, v1.0.0; 250 EPANET and water-distribution questions in four categories; runs no engine.
- [InfoWorks ICM Ruby Script Runner (app)](wiki/entities/icm-ruby-script-runner.md): Replit app, v0.1.0, deleted by Bob on 15 November 2026; ran visitors' Ruby on the server with no sandbox; gpt-5 explanations.

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
- [S68](wiki/sources/S68-swmm5-code-house-app-md.md) (2026-11-11): SWMM5 Code House, technical summary, v1.15.1.
- [S69](wiki/sources/S69-swmm6-code-house-app-md.md) (2026-11-11): SWMM6 Code House, technical summary, v1.2.1.
- [S70](wiki/sources/S70-swmm-engine-what-if-app-md.md) (2026-11-12): SWMM Engine What If, technical summary, v1.4.
- [S71](wiki/sources/S71-swmm-engines-byte-for-byte-summary.md) (2026-11-14): SWMM Engines, Byte for Byte, summary written from the page by Claude.
- [S73](wiki/sources/S73-swmm1-engine-app-md-v3-13.md) (2026-11-13): SWMM 1 Engine, technical summary, v3.13; replaces S01 as the current one.
- [S74](wiki/sources/S74-extran3-workbench-app-md.md) (2026-11-11): EXTRAN III Workbench, technical summary, v1.6.0.
- [S75](wiki/sources/S75-st-venant-rosetta-stone-app-md.md) (2026-11-13): St. Venant Solver Rosetta Stone, technical summary, v2.4.0.
- [S76](wiki/sources/S76-inside-the-network-cfd-app-md.md) (2026-11-12): Inside the Network, technical summary, v1.1.0.
- [S77](wiki/sources/S77-under-load-app-md.md) (2026-11-11): Under Load, technical summary, v1.4.0.
- [S78](wiki/sources/S78-fractal-swmm-generator-app-md.md) (2026-11-12): Fractal SWMM5/SWMM6 Network Generator, technical summary, v2.3.
- [S79](wiki/sources/S79-teacher-forced-swmm-summary.md) (2026-10-25): Teacher-Forced SWMM v1.0, summary written from the page by Claude.
- [S80](wiki/sources/S80-control-section-lab-summary.md) (2026-10-18): Control Section Lab v1.2, summary written from the page by Claude.
- [S81](wiki/sources/S81-bellinge-summary.md) (2026-10-18): Bellinge v2.0, summary written from the page by Claude.
- [S82](wiki/sources/S82-mirab-test-bench-summary.md) (2026-10-24): Mirab Test Bench v1.0, summary written from the page by Claude.
- [S83](wiki/sources/S83-people-as-pollutants-summary.md) (2026-10-29): People as Pollutants v1.0.0, summary written from the page by Claude.
- [S84](wiki/sources/S84-swmm-icm-knowledge-library-app-md.md) (2026-11-14): SWMM & ICM Knowledge Library, technical summary, artifact v70.
- [S85](wiki/sources/S85-bob-usefulness-index-app-md.md) (2026-11-11): Bob Usefulness Index, technical summary, v2.2.
- [S86](wiki/sources/S86-master-swmm-pdf-page-text.md) (2026-10-25): Master SWMM PDF, text of the page and its Doc essay.
- [S88](wiki/sources/S88-speak-100-app-md.md) (2026-11-13): Speak 100, technical summary, v2026.11.13b.
- [S96](wiki/sources/S96-swmm5-ui-replit-summary.md) (2026-11-15): SWMM5-UI, summary written by Replit Agent, v1.0.0.
- [S97](wiki/sources/S97-swmm5-network-miner-replit-summary.md) (2026-11-15): SWMM5 Network Miner, summary written by Replit Agent, v1.0.0.
- [S98](wiki/sources/S98-swmm5-inp-maker-replit-summary.md) (2026-07-20): SWMM5 INP MAKER, summary written by Replit Agent, v1.0.0.
- [S99](wiki/sources/S99-swmm5-lego-model-replit-summary.md) (2026-11-15): SWMM5 Lego Model, summary written by Replit Agent, v0.0.0.
- [S100](wiki/sources/S100-camel-swmm-replit-summary.md) (2025-08-18): Camel_SWMM, summary written by Replit Agent, v1.0.0.
- [S101](wiki/sources/S101-swmm5-manual-search-replit-summary.md) (2026-07-20): SWMM5 Manual Search, summary written by Replit Agent, v5.2.
- [S102](wiki/sources/S102-swmm-manual-search-landing-page-replit-summary.md) (2026-11-15): SWMM Manual Search, summary written by Replit Agent, v1.0.0.
- [S103](wiki/sources/S103-legacy-model-reader-replit-summary.md) (2026-07-22): InfoSewer and InfoSWMM Legacy Model Reader, summary written by Replit Agent, v1.0.0.
- [S104](wiki/sources/S104-xpx-to-shapefile-replit-summary.md) (2026-11-15): XPX to Shapefile Converter, summary written by Replit Agent, v0.1.0.
- [S105](wiki/sources/S105-swmm5-inp-file-viewer-replit-summary.md) (2025-08-26): SWMM5 .inp File Viewer (ala InfoSWMM), summary written by Replit Agent, v0.1.0.
- [S106](wiki/sources/S106-swmm5-topology-sandbox-replit-summary.md) (2026-01-19): SWMM5 Topology Sandbox, summary written by Replit Agent, v1.0.0.
- [S107](wiki/sources/S107-green-ampt-calculator-replit-summary.md) (2026-11-15): Green-Ampt Infiltration Calculator, summary written by Replit Agent, v1.0.0.
- [S108](wiki/sources/S108-runoff-and-infiltration-replit-summary.md) (2026-11-15): SWMM5 Runoff and Infiltration App, summary written by Replit Agent, v1.0.0.
- [S109](wiki/sources/S109-singapourapps-replit-summary.md) (2025-12-24): SingaPourApps, summary written by Replit Agent, v1.0.0.
- [S110](wiki/sources/S110-infodrainage-explorer-replit-summary.md) (2026-02-11): InfoDrainage Explorer, summary written by Replit Agent, v1.0.0.
- [S111](wiki/sources/S111-mapswmmsewer-code-repository-replit-summary.md) (2026-03-09): MapSWMMSewer - Code Repository, summary written by Replit Agent, v1.0.0.
- [S112](wiki/sources/S112-city-temperature-explorer-replit-summary.md) (2026-03-16): City Temperature Explorer, summary written by Replit Agent, v1.0.0.
- [S113](wiki/sources/S113-geoai-flood-impact-replit-summary.md) (2026-11-15): GeoAI Flood Impact, summary written by Replit Agent, v2.4.1_b.
- [S114](wiki/sources/S114-swmm5-microgpt-replit-summary.md) (2026-02-16): SWMM5 MicroGPT v2, summary written by Replit Agent, v2.
- [S115](wiki/sources/S115-epanet-for-swmm5-experts-replit-summary.md) (2026-03-15): EPANET for SWMM5 Experts - The Rosetta Stone, summary written by Replit Agent, v1.0.
- [S116](wiki/sources/S116-swmm5-explorer-replit-summary.md) (2026-01-29): SWMM5 Explorer, summary written by Replit Agent, v1.0.0.
- [S117](wiki/sources/S117-batchswmm56-replit-summary.md) (2026-09-12): BatchSWMM56, summary written by Replit Agent, v1.1.0.
- [S118](wiki/sources/S118-swmm5-vs-icm-infoworks-networks-replit-summary.md) (2026-07-22): SWMM5 vs ICM InfoWorks Networks, summary written by Replit Agent, v1.0.0.
- [S119](wiki/sources/S119-code-rosetta-stone-replit-summary.md) (2026-11-15): SWMM5 Rosetta Stone, summary written by Replit Agent, v1.0.0.
- [S120](wiki/sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md) (2026-11-15): ForceMain SWMM5 EPANET Comparison, summary written by Replit Agent, v1.0.
- [S121](wiki/sources/S121-hindsight-prophet-replit-summary.md) (2025-11-22): Hindsight Prophet, summary written by Replit Agent, v1.0.0.
- [S122](wiki/sources/S122-swmmanywhere-explorer-replit-summary.md) (2026-05-13): SWMManywhere Explorer, summary written by Replit Agent, v1.0.0.
- [S123](wiki/sources/S123-swmm5-modeler-replit-summary.md) (2026-11-15): SWMM5 Modeler, summary written by Replit Agent, v0.0.0.
- [S124](wiki/sources/S124-bobswmm-auto-research-replit-summary.md) (2026-03-12): bobSWMM Auto Research, summary written by Replit Agent, v0.0.0.
- [S125](wiki/sources/S125-kinematic-wave-router-replit-summary.md) (2026-11-15): Kinematic Wave Router, summary written by Replit Agent, v2026.11.15.
- [S126](wiki/sources/S126-swmm-ecosystem-replit-summary.md) (2025-08-29): SWMM Ecosystem, summary written by Replit Agent, v1.0.0.
- [S127](wiki/sources/S127-icm-infoworks-release-history-replit-summary.md) (2025-11-13): ICM InfoWorks, summary written by Replit Agent, v1.0.0.
- [S128](wiki/sources/S128-epanet-23-generator-replit-summary.md) (2026-07-20): EPANET 2.3 Generator, summary written by Replit Agent, v4.6.
- [S129](wiki/sources/S129-historical-water-inventions-replit-summary.md) (2026-11-15): Historical Water Inventions, summary written by Replit Agent, v1.0.0.
- [S130](wiki/sources/S130-pyswmm-explorer-replit-summary.md) (2026-02-11): PySWMM Explorer, summary written by Replit Agent, v1.0.0.
- [S131](wiki/sources/S131-swmm5-control-rule-editor-replit-summary.md) (2026-11-15): SWMM5 Control Rule Editor, summary written by Replit Agent, v0.1.0.
- [S132](wiki/sources/S132-swmm5-epanet-inp-explorer-replit-summary.md) (2026-11-15): SWMM5 & EPANET INP Explorer, summary written by Replit Agent, v1.0.0.
- [S133](wiki/sources/S133-swmm5-inp-file-interactive-viewer-replit-summary.md) (2026-11-15): SWMM5 .inp File Interactive Viewer, summary written by Replit Agent, v0.1.0.
- [S134](wiki/sources/S134-note-linkedin-two-well-received-posts.md) (2026-11-15): note, two LinkedIn posts that drew a good response, with their counts.
- [S135](wiki/sources/S135-li-fifty-posts-with-counts.md) (2026-11-15): LinkedIn, fifty of Bob's posts with their reactions, comments and impressions.
- [S136](wiki/sources/S136-swmm5-topo-network-wizard-replit-summary.md) (2026-11-15): SWMM5 Topo Network Wizard, summary written by Replit Agent, v1.0.0.
- [S137](wiki/sources/S137-swmm-documents-explorer-replit-summary.md) (2026-02-11): SWMM Documents Explorer, summary written by Replit Agent, v1.0.0.
- [S138](wiki/sources/S138-swmm5-quizzer-replit-summary.md) (2026-11-15): SWMM5 Quizzer, summary written by Replit Agent, v1.0.0.
- [S139](wiki/sources/S139-swmmcraft-infiltration-replit-summary.md) (2025-12-25): SWMMCRAFT (Replit project SWMM-Infiltration), summary written by Replit Agent, v1.0.0.
- [S140](wiki/sources/S140-swmm5wiki-replit-summary.md) (2025-08-28): SWMM5Wiki (Replit project GatorSWMM), summary written by Replit Agent, v1.0.0.
- [S141](wiki/sources/S141-bobswmm-writer-replit-summary.md) (2026-02-11): BobSWMM Writer, summary written by Replit Agent, v2.1.0.
- [S142](wiki/sources/S142-icm-prn-file-reader-replit-summary.md) (2025-08-05): ICM PRN File Reader, summary written by Replit Agent, v1.0.0.
- [S143](wiki/sources/S143-note-icm-prn-reader-fix.md) (2026-11-15): note, Bob reports that he fixed "the prn problem" in the ICM PRN File Reader.
- [S144](wiki/sources/S144-note-icm-prn-reader-fix-which.md) (2026-11-15): note, the PRN problem Bob fixed was the file list anyone could read.
- [S145](wiki/sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) (2025-11-19): ICM Ruby to Nano Banana Prompt, summary written by Replit Agent, v1.0.0.
- [S146](wiki/sources/S146-infosewer-to-infoworks-icm-replit-summary.md) (2026-02-12): InfoSewer to InfoWorks ICM, summary written by Replit Agent, v1.0.0.
- [S147](wiki/sources/S147-swmmanywhere-explorer-swm-replit-summary.md) (2026-11-15): SWMManywhere Explorer (swm-explorer), summary written by Replit Agent, v1.0.0.
- [S148](wiki/sources/S148-openswmm-engine-app-replit-summary.md) (2026-11-15): OpenSWMM Engine, summary written by Replit Agent, v6.0.0-alpha.1.
- [S149](wiki/sources/S149-epanet-quizzer-replit-summary.md) (2026-11-15): EPANET Quizzer, summary written by Replit Agent, v1.0.0.
- [S150](wiki/sources/S150-icm-ruby-script-runner-replit-summary.md) (2025-11-07): InfoWorks ICM Ruby Script Runner, summary written by Replit Agent, v0.1.0.
- [S151](wiki/sources/S151-note-openswmm-license-not-mit.md) (2026-11-15): note, Bob says the OpenSWMM license has moved away from MIT.
- [S152](wiki/sources/S152-note-ruby-script-runner-deleted.md) (2026-11-15): note, Bob deleted the InfoWorks ICM Ruby Script Runner; ICM Exchange is the better way.

Manuals and reports (primary documents)
- [S60](wiki/sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md) (2017-05): EPA SWMM Reference Manual, Volume II, Hydraulics, by L. A. Rossman. Read in part: section 1.1 and Chapters 2, 3, 4 and 6 (the raw file lacks pages 64 to 66 and 122).

Notes and data
- [S03](wiki/sources/S03-findings-register-format.md) (2026-10-09): findings register, format and twenty candidates.
- [S04](wiki/sources/S04-findings-register-seed.md) (2026-10-09): findings register, seed entries F-0001 to F-0014.
- [S05](wiki/sources/S05-swmm5org-article-facts.md) (2026-10-16): fact sheet measured from the chat archive.
- [S09](wiki/sources/S09-openswmm-thread-list.md) (2026-11-01): OpenSWMM thread list, 1995 to 2026.
- [S10](wiki/sources/S10-openswmm-top25-problems.md) (2026-11-06): top 25 problems tagged from thread titles.
- [S67](wiki/sources/S67-note-green-ampt-newton-test-order.md) (2026-11-14): note, the Green-Ampt Newton loop tests its correction before applying it.
- [S87](wiki/sources/S87-corpus-1729-readme.md) (2026-10-23): 1729-SWMM5-Models-2030, repository README and inventory.
- [S89](wiki/sources/S89-note-corpus-name.md) (2026-11-15): note, what 1729 and 2030 stand for in the corpus name.
- [S90](wiki/sources/S90-note-swmm-anecdotes-linkedin-comments.md) (2026-11-15): note, SWMM anecdotes from the comments on one of Bob's LinkedIn posts.
- [S91](wiki/sources/S91-note-q64-answers-canberra-barrels-post-link.md) (2026-11-15): note, Bob's answers to Q64: the post's link, Canberra from November 1991 to December 1992, double pipes are barrels.
- [S92](wiki/sources/S92-note-barrels-transport-is-not-extran.md) (2026-11-15): note, Bob's answer to Q65: Transport is not Extran, so barrels were added to Extran later.
- [S93](wiki/sources/S93-note-xp-swmm-renamed-xpswmm-1993.md) (2026-11-15): note, XP-SWMM was the original name, changed to XPSWMM in 1993.
- [S95](wiki/sources/S95-note-punch-card-box-held-2000-cards.md) (2026-11-15): note, a box of punch cards held 2,000 cards.

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
- [S72](wiki/sources/S72-li-swmm6-code-house-article.md) (2026-11-04): SWMM6 Code House, Every Line of OpenSWMM 6 on a Wall: both houses, and 20 reading notes.
- [S94](wiki/sources/S94-li-post-my-earlier-history-with-swmm.md) (2026-11-14): LinkedIn post, my earlier history with SWMM: SWMM at 17, at work on it at 22, SWMM 2.5 as 20,000 punch cards.

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

240 raw files are queued: 212 LinkedIn articles and the as-pasted copy of the post of 14 November 2026 (kept because raw files are never deleted; its corrected copy is S94, so it is not to be ingested), 19 manual files in `raw/manuals/` (8 EPA, USGS and FHWA documents not yet started, and 11 SWMM 4.4 documentation files), 4 swmm5.org topic pages, 2 SWMM 1 build notes and 2 files in `raw/apps/`. One, `PyBME-issue-drafts.md`, is not an app summary and was left queued on purpose (Q56). The other, `st-venant-solver-rosetta-stone-v2.6.2.md`, is the newer version of an app already ingested at version 2.4.0 (S75); it was added on 15 November 2026 and bears on Q62. Three more LinkedIn files are byte-identical copies of others and are marked `duplicate`. `raw/MANIFEST.csv` lists them all. Suggested next batches, in order:

0. The rest of the EPA hydraulics manual, a chapter at a time (S60: sections 1.2 to 1.5, Chapter 5, Chapter 7 and the appendices remain), then the 2006 quality assurance report and the SWMM 5.1 User's Manual. With them, the Rosetta Stone summary at version 2.6.2, which tests the pump rule of Q62. These are the primary documents; ingesting them first lets later articles be checked against them.
1. The four remaining swmm5.org topic pages and the SWMM 1 build notes (small, and they complete themes 3 to 6).
2. EXTRAN: the six test-file articles and Edition 38. Settles Q14.
3. SWMM history: Edition 40, "SWMM1 to SWMM5 Documentation Archive", "Reviving 1988 SWMM4 Models with AI", "SWMM 44H Fortran Code".
4. Inside SWMM5: the dynwave.c and dwflow.c stories, "Understanding SWMM5 through the Tables in text.h and keywords.h", "100 SWMM5 Quiz Questions".
5. SWMM5 and ICM: the DWF, RDII, groundwater, runoff surface and buildup and washoff comparisons. Settles Q13.
6. Ruby and SQL for ICM: 70 articles; ingest by family, not one by one.
