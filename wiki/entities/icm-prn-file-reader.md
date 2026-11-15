---
title: "ICM PRN File Reader (app)"
type: entity
updated: 2026-11-15
sources: [S142, S143, S144]
tags: [apps, replit, icm, results]
reviewed: no
---
Bob's Replit app ICM PRN File Reader: an app that reads InfoWorks ICM PRN output, extracts node, link and mass-balance data, flags flooding, surcharge and capacity, converts units and exports CSV, Excel or PDF; it runs no simulation. Version 1.0.0, at `icm-reader-robertdickinson.replit.app` [S142](../sources/S142-icm-prn-file-reader-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S142](../sources/S142-icm-prn-file-reader-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S142](../sources/S142-icm-prn-file-reader-replit-summary.md)
- It reads existing simulation results and does not run a hydraulic simulation. InfoWorks ICM is the upstream output format, not an embedded solver. `engines: none`.
- Node rows contain 9 numeric fields. Link rows use 14 or 8.
- `surchargeDepth = max(0, maxLevel - groundLevel)` and `freeboard = groundLevel - maxLevel`, rounded to 3 decimal places.
- Severe flooding starts at about 353.147 ft³ (10 m³); flooding exceeds about 1.766 ft³ (0.05 m³); surcharge applies below about 1.640 ft (0.5 m) of freeboard without flooding.
- `capacityPercent = abs(maxFlow) / pipeFullFlow * 100`, rounded to 1 decimal place.
- `volumeError = totalInflow - totalOutflow`. When the continuity error equals zero and inflow is positive, `continuityErrorPercent = volumeError / totalInflow * 100`. The parser marks mass balance warning above 5% and critical above 10%.
- The dashboard grades the same error good through 1%, warning through 5%, then critical. The parser marks a link over capacity above 100%; the dashboard counts exactly 100% as overloaded.
- Missing mass-balance components begin as zero. Dry-weather flow and flooding are not assigned extracted values.
- Conversions: `cfs = m³/s * 35.3147`, `ft = m * 3.28084`, `ft³ = m³ * 35.3147`, `ft² = m² * 10.7639`, `in = mm / 25.4`. Precision is 0 through 6 decimal places, 2 by default.
- Uploads up to 50 MiB are held in server memory. Expiration is checked after 3 hours, and cleanup targets 20 retained files. A restart discards them.
- `GET /api/prn/files` returns stored file objects, including their content, without route-level authentication.
- The bundled sample parsed to 37 nodes, 75 links, 0 unparsed data lines and 1 undefined capacity.
- `npx vitest run`: 24 tests passed and 0 failed, in 2 test files. `npm run check` passed.
- Exports are CSV, and XLSX with 4 worksheets or PDF. Project license MIT.

**What it does not show.** The deployed app was not loaded. Upload, conversion, the results tabs and downloads were not exercised in the browser, and conversion accuracy and export integrity were not checked. Reverse conversion of US customary input, other PRN variants and security were not tested. [S142](../sources/S142-icm-prn-file-reader-replit-summary.md)

**Noted at ingest.** Arithmetic. The thresholds agree with the conversion factors: 10 x 35.3147 = 353.147, 0.05 x 35.3147 = 1.765735 and 0.5 x 3.28084 = 1.64042 (our arithmetic). The `date:`, 5 August 2025, is the first Git record of version 1.0.0; all ten listed changes are from 22 July 2026 (Q75). Git names Replit Agent (Q80). The open file-list route is Replit Agent's reading of the code, not a test (Q76). It is the only one of the six with a test suite. Its continuity percent is computed from the PRN totals and, the file says, is not a mass-conservation audit; see [Continuity is not validation](../concepts/continuity-is-not-validation.md).

**Added 15 November 2026: Bob reports a fix.** Bob wrote that evening that he had fixed "the prn problem" [S143](../sources/S143-note-icm-prn-reader-fix.md). Asked which, he answered "the file that anyone can read" [S144](../sources/S144-note-icm-prn-reader-fix-which.md): the open file list is fixed on his word, and the differing thresholds are not said to be. The summary of the fixed version has not come in (Q76).

See [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [InfoWorks ICM](infoworks-icm.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).
