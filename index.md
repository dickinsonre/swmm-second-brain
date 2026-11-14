# Index

Every page in the wiki, one line each. An agent reads this first. Updated on every ingest. Last update: 2026-11-14 (26 sources, 25 concepts, 17 entities).

## Start here
- [Overview: what this wiki holds so far](wiki/overview.md): what the wiki holds so far, by Bob's six themes, and what is missing.
- [Open questions](wiki/open-questions.md): 21 contradictions, doubtful numbers and gaps waiting for a source or for Bob.
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
- [RDII unit hydrographs (RTK)](wiki/concepts/rdii-unit-hydrographs.md): R, T and K, unit hydrograph groups, and the interface file format.
- [Two-layer soil infiltration (SOIL2)](wiki/concepts/two-layer-infiltration.md): Bob's SOIL2 proposal, a second soil layer through the LID machinery.

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

## Entities

Engines and programs
- [SWMM 1 (1971)](wiki/entities/swmm-1.md): the 1971 program: builders, blocks, methods, and 14 faults found in the listing.
- [EXTRAN](wiki/entities/extran.md): the dynamic-wave block before SWMM 5, its test models, and its rebuild.
- [EPA SWMM 5](wiki/entities/swmm-5.md): the C rewrite of 2004: origin, releases, status, Bob's variants.
- [InfoWorks ICM](wiki/entities/infoworks-icm.md): the Wallingford and Autodesk engine: solver, surcharge, network types.
- [InfoSWMM and InfoSewer](wiki/entities/infoswmm-and-infosewer.md): the two Innovyze products Bob led from 2008.
- [OpenSWMM 6 and HydroCouple](wiki/entities/openswmm-6-and-hydrocouple.md): the little the ingested sources say so far, and four findings.

Apps
- [SWMM 1 Engine (app)](wiki/entities/swmm-1-engine-app.md): three engines in one page, version 3.6.
- [SWMM App Complexity Meter (app)](wiki/entities/swmm-app-complexity-meter.md): version 1.9.1, its checks and limits.
- [SWMM and ICM St. Venant comparison (app)](wiki/entities/swmm-icm-st-venant-app.md): the Replit comparison app behind Edition 54.
- [Claude chat archive (app)](wiki/entities/claude-chat-archive.md): 1,671 conversations and 800 apps as of 14 October 2026.

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

## Sources

App summaries
- [S01](wiki/sources/S01-swmm1-engine-app-md.md) (2026-11-13): SWMM 1 Engine, technical summary, v3.6.
- [S02](wiki/sources/S02-complexity-meter-app-md.md) (2026-11-11): SWMM App Complexity Meter, technical summary, v1.9.1.

Notes and data
- [S03](wiki/sources/S03-findings-register-format.md) (2026-10-09): findings register, format and twenty candidates.
- [S04](wiki/sources/S04-findings-register-seed.md) (2026-10-09): findings register, seed entries F-0001 to F-0014.
- [S05](wiki/sources/S05-swmm5org-article-facts.md) (2026-10-16): fact sheet measured from the chat archive.
- [S09](wiki/sources/S09-openswmm-thread-list.md) (2026-11-01): OpenSWMM thread list, 1995 to 2026.
- [S10](wiki/sources/S10-openswmm-top25-problems.md) (2026-11-06): top 25 problems tagged from thread titles.

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

## Queue

223 raw files are queued: 216 LinkedIn articles, 4 swmm5.org topic pages, 2 SWMM 1 build notes and 1 app summary. Three more LinkedIn files are byte-identical copies of others (LinkedIn exported those articles twice) and are marked `duplicate`. `raw/MANIFEST.csv` lists them all. Suggested next batches, in order:

1. The four remaining swmm5.org topic pages and the SWMM 1 build notes (small, and they complete themes 3 to 6).
2. EXTRAN: the six test-file articles and Edition 38. Settles Q14.
3. SWMM history: Edition 40, "SWMM1 to SWMM5 Documentation Archive", "Reviving 1988 SWMM4 Models with AI", "SWMM 44H Fortran Code".
4. Inside SWMM5: the dynwave.c and dwflow.c stories, "Understanding SWMM5 through the Tables in text.h and keywords.h", "100 SWMM5 Quiz Questions".
5. SWMM5 and ICM: the DWF, RDII, groundwater, runoff surface and buildup and washoff comparisons. Settles Q13.
6. Ruby and SQL for ICM: 70 articles; ingest by family, not one by one.
