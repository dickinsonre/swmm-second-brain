---
title: "S282: Forma × SWMM6, summary written from the page (v1.2)"
type: source
raw: raw/apps/forma-swmm6-v1.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-01
ingested: 2026-11-18
tags: [apps, swmm6, openswmm, cde, versioning, storage-volume]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Forma × SWMM6, version 1.2: a SWMM6 model kept the way a common data environment keeps a drawing: one fictional subdivision, Cedar Run, as four versions, each run in EPA SWMM 5.2.4 and OpenSWMM 6 alpha 4 in the browser, compared line by line, with a SWMM Static Volume Summary and, on the Netlify edition, a connection to the user's own Autodesk Forma project. Raw file: [raw/apps/forma-swmm6-v1.2.md](../../raw/apps/forma-swmm6-v1.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Sjv8Vv75yuMsAobYVvWw8Y, version 1793588262-0575 (index.html, 6,336,104 bytes, SHA-256 7c0b735f386b1589de5e251c89d66b560f197bb7b06c6c6a15585c07a9c4584d), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude (Opus 5.5) from 30 October to 1 November 2026 at Bob's direction, after the InfoDrainage 2027.2 Forma announcement, and revised after an outside evaluation of v1.1.

**Claims worth keeping** (all copied from the file)
- Cedar Run outfall peaks: V1 predevelopment 28.30 cfs (SWMM6 28.31); V2 built out with old pipes 47.71 cfs and about 115,000 gallons of overflow; V3 upsized trunk 74.91 cfs; V4 with the pond 31.35 cfs.
- The Static Volume Summary on a level-pool twin matched both engines' own .out to the printed 0.1 ft3: 36 checks, and 224 on a census model with all 21 cross-section shapes and six storage shapes.
- O1: with DYNAMIC_SLOT a full pipe books slot water as stored volume (C1 of V3 reads 2,463.5 ft3 against 1,963.5 ft3 of pipe, +25.5%); on the still pool, routing continuity reads -1.035% (V4) and -32.064% (V1).
- O2: FV does not hold the pressurized still pool (link flows reach 74 cfs in V4, continuity -9.021%). O4: on the free-surface still pool every dynamic-wave run, 5.2.4 included, reads -3.713% routing continuity in V1 with every flow zero.
- O5: a TABULAR storage curve with no zero-depth row gives 50 ft3 at 1.00 ft and 1.005 ft3 at 1.01 ft in 5.2.4 and SWMM6 alike.

**Limits it states.** The live Forma connection was tested only against a mock of Autodesk's endpoints; the sample folder's container states are simulated; nothing says InfoDrainage reads SWMM6 files; the site and storm are fictional.

**Checked at ingest.** 2,463.5 / 1,963.5 = 1.255, the +25.5% printed (our arithmetic). The engine observations are the page's and were not reported upstream when it was published. The `links:` line gives Netlify as https://forma-swmm6.netlify.app.

**Feeds:** [Forma × SWMM6 (app)](../entities/forma-swmm6.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [Shape curves, transects and storage curves](../concepts/shape-curves-transects-storage-curves.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
