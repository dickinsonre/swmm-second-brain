---
title: Checking a SWMM5 model's conversion into ICM
type: concept
updated: 2026-11-17
sources: [S164, S165, S45, S166, S179, S184, S188, S202, S204]
tags: [icm, swmm5, conversion, verification, benchmark]
reviewed: no
---
When a SWMM5 model and its ICM copy disagree, the difference may come from the engines or from the conversion. Two notes Bob supplied on 16 November 2026 set out how to tell which. ChatGPT drafted them from Autodesk Help [S179](../sources/S179-note-icm-notes-drafted-by-chatgpt.md), so they are AI-written; their Autodesk facts are reported from Autodesk's help and not checked here, and nothing in them has been run (Q90).

**Three routes, tracked apart** [S164](../sources/S164-note-swmm-inp-conversion-qa.md)
1. An EPA SWMM `.inp` into an ICM SWMM network.
2. An `.inp` into an ICM InfoWorks network. Autodesk describes partial imports and objects that need extra data on this route.
3. ICM's own conversion from a SWMM network to an InfoWorks network.

Autodesk's 2027 conversion pages list importer support through EPA SWMM 5.1.015, so a later feature may or may not import; the note says to record what the installed build imports, feature by feature [S164](../sources/S164-note-swmm-inp-conversion-qa.md).

**What to check on each route** [S164](../sources/S164-note-swmm-inp-conversion-qa.md)

| Check | Compare |
|---|---|
| IDs and topology | node and link counts, end-node IDs, outfall type |
| Units and geometry | flow units, node inverts, link end elevations, cross-section, roughness |
| Options and events | rainfall source, time window, reporting and routing intervals, ponding, controls |
| Inflows and treatment | DWF patterns, RDII, LID and SuDS, network-specific objects lost |
| Results | continuity, peak and timing, volume, one downstream hydrograph |

Each feature is marked preserved, mapped, omitted or edited by hand. An example: an upstream invert of 102.0 ft with a 1.5 ft offset should become a link end elevation of 103.5 ft. For a round trip, compare the source and exported `.inp` and run both in the same pinned EPA executable [S164](../sources/S164-note-swmm-inp-conversion-qa.md).

**A two-pipe benchmark** [S165](../sources/S165-note-epa-swmm-ruby-icm-benchmark.md). Small enough to inspect in every environment:
- Two junctions and a free outfall at inverts of 100, 99 and 98 ft; rims 5 ft above invert.
- Two circular conduits, 200 ft long, 12 in in diameter, Manning's n 0.013, no offsets.
- Dry start, one hour, results every minute.
- Inflow at the first junction rising from 0 to 0.5 ft³/s at 10 min and 1.0 ft³/s at 20 min, back to 0 at 30 min.

The order matters. First EPA SWMM 5.2.4 against `swmm5-ruby` on the same `.inp`, held to the Ruby port's byte gate. That fixes the engine baseline before ICM enters. Then ICM SWMM, with its log and engine input. Then ICM InfoWorks, with geometry, boundary, initial state and inflow checked separately. Compare outfall peak, peak time, volume and continuity, and agree the acceptable differences before running [S165](../sources/S165-note-epa-swmm-ruby-icm-benchmark.md). On its own gate, 478 of the Ruby translation's 480 models ran and all 478 matched EPA; the other 2 stopped at the time limit [S45](../sources/S45-swmm5-ruby-readme.md); see [SWMM5 language translations](../entities/swmm5-language-ports.md).

**Why it matters here.** The note links Q16, which asks whether this wiki's published SWMM and ICM comparison numbers rest on runs of both engines. The benchmark is a design that has not been run [S165](../sources/S165-note-epa-swmm-ruby-icm-benchmark.md).

**Related.** [SWMM 5 versus ICM InfoWorks](swmm5-versus-icm-infoworks.md), [ICM network tables and result fields](icm-tables-and-result-fields.md), [Byte-for-byte gate](byte-for-byte-gate.md).

**The other direction: InfoWorks to ICM SWMM.** Bob's 2023 article lists two validation errors after converting an InfoWorks network to ICM SWMM: SWMM needs a rain gage to hold the rainfall, and it does not let a subcatchment and a node share an ID. The fix for the second is an SQL statement, `SET subcatchment_id = 'S_' + subcatchment_id;`. Features InfoWorks has and SWMM lacks are dropped [S184](../sources/S184-li-unified-2d-engine-icm.md).

**From Bob's 2021 webinar** [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). The route he used for about 100 models: import a SWMM 5, InfoSWMM or XP SWMM file into an ICM SWMM network, run it, then convert that network to an ICM network and run again. Two practical points he gives:
- The conversion renames the links, so a graph of one link in both networks finds nothing to match. His fix: reset the link names with a SQL `SET` and keep the original names in a user text field.
- Importing a SWMM 5 file brings its rainfall, inflows and patterns in as ICM events, usable by both network types, and a run can be exported back to SWMM 5 with its time series.
When graphing the two, remember that ICM shows a link's ends and SWMM 5 its midpoint flow [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md).

**Added 17 November 2026: why matching flow is not enough.** [One Model, Three Engines (app)](../entities/one-model-three-engines.md) shows it on a teaching pipe: 15 in, 1.2 cfs, 1.00 ft of water at the outlet. At normal depth the pipe runs 0.56 ft deep at 2.25 ft/s; the backwater profile puts 0.76 ft at mid-length at 1.54 ft/s. Both carry exactly 1.2 cfs. On twelve such pipes the flows match while depth misses by up to 0.47 ft and velocity by up to 1.22 ft/s [S202](../sources/S202-one-model-three-engines-summary.md). Its advice after a conversion is to compare depth and velocity as well as flow. These numbers come from the app's teaching solvers; no ICM engine ran [S202](../sources/S202-one-model-three-engines-summary.md).

**Added 17 November 2026: step 1 of the benchmark is run.** EPA SWMM 5.2.4 and swmm5-ruby ran the two-pipe model with dynamic wave at a fixed 1 s step and wrote byte-identical `.out` files. The outfall peaks at 0.9665 cfs at minute 21 on the 1-minute grid and J1 at 0.4356 ft at minute 20; continuity error 0.000 %. At EPA's default 20 s variable step the peaks move to 0.9691 cfs and 0.4324 ft [S204](../sources/S204-note-two-pipe-benchmark-step1-run.md). The run record lists every minute, so it is the reference for steps 2 and 3. Those need ICM, and nobody has run them.
