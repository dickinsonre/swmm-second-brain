---
title: "ICM Sediment Field Guide (app)"
type: entity
updated: 2026-11-17
sources: [S205, S246]
tags: [apps, icm, sediment, 2d, teaching]
reviewed: no
---
Bob's app ICM Sediment Field Guide: Bob's earlier outline for a LinkedIn article on 1D and 2D sediment modeling in InfoWorks ICM, brought to November 2026 and written in full, with two labs that run the textbook formulas the article names. ICM's solver is not run. Version 1.1, 2026-11-02 [S246](../sources/S246-icm-sediment-field-guide-summary.md). Netlify address: https://icm-sediment-field-guide.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S246](../sources/S246-icm-sediment-field-guide-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S246](../sources/S246-icm-sediment-field-guide-summary.md)
- A flat sediment bed in a circular pipe, with the same n and hydraulic gradient, takes 2.8, 7.7, 20.4 and 64.0 percent of full-flow capacity at 5, 10, 20 and 50 percent depth; a 24 in pipe half full drops from the 16 cfs on the drawings to 5.76 cfs.
- An independent review of version 1.0 (graded 78/100), supplied by Bob on 2 November 2026, reproduced the capacity curve to four decimals.
- Kinematic viscosity follows the water temperature through the Vogel equation, scaled so that 68 F gives 1.0 x 10^-6 m2/s.
- Checks are sorted by kind of evidence: branch continuity, hand calculations, independent references and outside reproduction; the page notes that agreement among outputs sharing one implementation does not verify the implementation.
- Version 1.1 separated total load from bed load, corrected transport units to ft2/s and marked undocumented ICM defaults.

**What it does not show.** Every number is a textbook formula at one instant, not ICM's solver. The capacity curve assumes the same Manning n and hydraulic gradient clean and sedimented; a real bed is rougher. [S246](../sources/S246-icm-sediment-field-guide-summary.md)

**Noted at ingest.** 16 x (1 - 0.640) = 5.76 cfs.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](infoworks-icm.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md).
