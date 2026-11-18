---
title: "SWMM Canon (app)"
type: entity
updated: 2026-11-17
sources: [S205, S208]
tags: [apps, swmm5, inp, verification, hashing]
reviewed: no
---
Bob's app SWMM Canon: five fingerprints for every SWMM 5 .inp, each forgetting one more kind of difference (bytes, spelling, order, names, and the defaults EPA fills in), plus a sixth for the .out; the lowest fingerprint two files share says what separates them. It reads files and runs no engine. Version 1.4, 2026-11-02 [S208](../sources/S208-swmm-canon-summary.md). Netlify address: https://swmm-canon.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S208](../sources/S208-swmm-canon-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S208](../sources/S208-swmm-canon-summary.md)
- Layers: L0 bytes; spelling; order; L3 names, with references as typed edges including names inside [CONTROLS] and [TREATMENT]; L4 "as EPA builds it", with defaults filled per each *_readParams and order hazards H1 to H6 kept as marks; L5 for the objects [REPORT] writes to the .out.
- Export, read and export again gives the same bytes at L2, L3 and L4 on every test file and on 428 corpus models.
- 160 short corpus models run as saved and as their L4 export: of the 145 that finish, 126 are bit-identical for every object, 132 agree to six significant figures and 7 differ by more than one part in ten thousand of a variable's peak. Four stop with an error before reporting, with the same code both ways. The page explains the differences by EPA adding flows in file order.
- EPA keeps only the last row for an inflow, a dry-weather flow, a coverage, a loading, a buildup or washoff function, a treatment, an inlet usage and an adjustment pattern; an NC row of zeros keeps the previous transect roughness, already scaled by the last meander factor.
- With [SUBAREAS] before [SUBCATCHMENTS], EPA quietly runs the subcatchments as all pervious; a second review found the L4 export of that demo changed surface runoff from 0.000 to 0.035 in, since fixed.
- Every one of EPA's 46 section readers was checked for state another section sets (audit_readers.py).

**What it does not show.** An equal L3 hash is a Weisfeiler-Lehman invariant, not a proof that two networks are the same; the Name map tab verifies an explicit mapping first. L4 knows only the defaults and order hazards listed on its Evidence tab. Same L4 means the same model, not the same arithmetic. L5 covers only the objects [REPORT] writes. [S208](../sources/S208-swmm-canon-summary.md)

**Noted at ingest.** Of the 160 corpus models, 145 finish and 4 stop with an error; the page as summarized does not say what became of the other 11. Its Round-trip audit is aimed at files that come back from another program, such as ICM's SWMM export, the subject of [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
