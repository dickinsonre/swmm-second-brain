---
title: "Forma × SWMM6 (app)"
type: entity
updated: 2026-11-18
sources: [S282]
tags: [apps, swmm6, openswmm, cde, versioning, storage-volume]
reviewed: no
---
Bob's app Forma × SWMM6: a SWMM6 model kept the way a common data environment keeps a drawing: one fictional subdivision, Cedar Run, as four versions, each run in EPA SWMM 5.2.4 and OpenSWMM 6 alpha 4 in the browser, compared line by line, with a SWMM Static Volume Summary and, on the Netlify edition, a connection to the user's own Autodesk Forma project. Version 1.2, 2026-11-01 [S282](../sources/S282-forma-swmm6-summary.md). Netlify address, from its `links:` line: https://forma-swmm6.netlify.app [S282](../sources/S282-forma-swmm6-summary.md).

**A caution about its source.** The page ships no technical summary. [S282](../sources/S282-forma-swmm6-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S282](../sources/S282-forma-swmm6-summary.md)
- Cedar Run outfall peaks: V1 predevelopment 28.30 cfs (SWMM6 28.31); V2 built out with old pipes 47.71 cfs and about 115,000 gallons of overflow; V3 upsized trunk 74.91 cfs; V4 with the pond 31.35 cfs.
- The Static Volume Summary on a level-pool twin matched both engines' own .out to the printed 0.1 ft3: 36 checks, and 224 on a census model with all 21 cross-section shapes and six storage shapes.
- O1: with DYNAMIC_SLOT a full pipe books slot water as stored volume (C1 of V3 reads 2,463.5 ft3 against 1,963.5 ft3 of pipe, +25.5%); on the still pool, routing continuity reads -1.035% (V4) and -32.064% (V1).
- O2: FV does not hold the pressurized still pool (link flows reach 74 cfs in V4, continuity -9.021%). O4: on the free-surface still pool every dynamic-wave run, 5.2.4 included, reads -3.713% routing continuity in V1 with every flow zero.
- O5: a TABULAR storage curve with no zero-depth row gives 50 ft3 at 1.00 ft and 1.005 ft3 at 1.01 ft in 5.2.4 and SWMM6 alike.

**What it does not show.** The live Forma connection was tested only against a mock of Autodesk's endpoints; the sample folder's container states are simulated; nothing says InfoDrainage reads SWMM6 files; the site and storm are fictional. [S282](../sources/S282-forma-swmm6-summary.md)

**Noted at ingest.** 2,463.5 / 1,963.5 = 1.255, the +25.5% printed (our arithmetic). The engine observations are the page's and were not reported upstream when it was published.

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Seven SWMM Engines (app)](seven-swmm-engines.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Shape curves, transects and storage curves](../concepts/shape-curves-transects-storage-curves.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
