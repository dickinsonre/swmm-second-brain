---
title: Checking a SWMM5 model's conversion into ICM
type: concept
updated: 2026-11-16
sources: [S164, S165, S45, S166, S179, S184]
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
