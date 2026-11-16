# A SWMM conversion needs checks for each import and export route

**Status:** seed
**Date:** 2026-11-16

## The idea

Track EPA SWMM `.inp` to ICM SWMM, `.inp` to ICM InfoWorks, and native ICM network conversion as distinct routes. Autodesk publishes conversion notes for each `.inp` destination and describes partial imports and objects that require additional data for the InfoWorks destination. The 2027 conversion pages list importer support through EPA SWMM 5.1.015. Record what your installed build imports for each later feature you exercise, along with the engine version used to run the model.

## Proof / from scratch

Use a small model with one feature under test. Keep the source `.inp`, the import log, the destination network commit and scenario, and any exported `.inp`.

| Check | What to compare |
|---|---|
| IDs and topology | Node and link counts, end-node IDs, and outfall type |
| Units and geometry | Flow units, node inverts, link end elevations, cross-section shape, and roughness |
| Options and events | Rainfall source, time window, reporting and routing intervals, ponding, and controls |
| Inflows and treatment | DWF patterns, RDII assignments, LID/SuDS settings, and any loss of network-specific objects |
| Results | Continuity, peak and timing, volume, and the hydrograph at one downstream location |

An upstream node invert of 102.0 ft with a 1.5 ft depth offset implies a link end elevation of 103.5 ft. Verify the value after conversion. For each feature, record whether it was preserved, mapped, omitted, or required a manual edit.

For a round trip, compare the source and exported `.inp` sections and run both through the same pinned EPA executable. For a native InfoWorks simulation, keep the original conversion record with the results so differences can be traced to either the inputs or the solver.

## Links

- [Autodesk SWMM5 conversion notes for ICM SWMM networks](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-5F0C41F8-1BF4-490E-A1CA-160BF2395352.htm)
- [Autodesk SWMM5 conversion notes for InfoWorks networks](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-5F192463-1FC1-41FD-922E-2945470FBBB7.htm)
- [Autodesk SWMM network to InfoWorks network import](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-3D69851A-4694-48AC-9098-2ACE93803E50.htm)
- [Bob's batch SWMM5 import article already queued for ingest](https://github.com/dickinsonre/swmm-second-brain/blob/main/raw/linkedin/2025-12-05-edition-48-using-icm-ruby-scripts-import-2k-swmm5-files-dickinson-s4cne.md)
- [EPA SWMM, Ruby, and ICM benchmark](./epa-swmm-ruby-icm-benchmark.md)
