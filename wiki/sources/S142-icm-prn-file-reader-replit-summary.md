---
title: "S142: ICM PRN File Reader, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/icm-reader-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-08-05
ingested: 2026-11-15
tags: [apps, replit, icm, results]
reviewed: no
---
**What it is.** A technical summary of ICM PRN File Reader, version 1.0.0: an app that reads InfoWorks ICM PRN output, extracts node, link and mass-balance data, flags flooding, surcharge and capacity, converts units and exports CSV, Excel or PDF; it runs no simulation. It is one of Bob's Replit apps, at `icm-reader-robertdickinson.replit.app`. Raw file: [raw/apps/icm-reader-robertdickinson-v1.0.0.md](../../raw/apps/icm-reader-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Git commit authors record Replit Agent contributions, among them interface setup, dark mode, parsing improvements and sample-file fixes, and `robertdickinson` on the workbook and PDF export commit. The copy here was read out of the editor of the Replit project named ICMReader on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** The deployed app was not loaded. Upload, conversion, the results tabs and downloads were not exercised in the browser, and conversion accuracy and export integrity were not checked. Reverse conversion of US customary input, other PRN variants and security were not tested.

**Checked at ingest.** Arithmetic. The thresholds agree with the conversion factors: 10 x 35.3147 = 353.147, 0.05 x 35.3147 = 1.765735 and 0.5 x 3.28084 = 1.64042 (our arithmetic). The `date:`, 5 August 2025, is the first Git record of version 1.0.0; all ten listed changes are from 22 July 2026 (Q75). Git names Replit Agent (Q80). The open file-list route is Replit Agent's reading of the code, not a test (Q76). It is the only one of the six with a test suite. Its continuity percent is computed from the PRN totals and, the file says, is not a mass-conservation audit; see [Continuity is not validation](../concepts/continuity-is-not-validation.md).

**Feeds:** [ICM PRN File Reader (app)](../entities/icm-prn-file-reader.md), [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md).
