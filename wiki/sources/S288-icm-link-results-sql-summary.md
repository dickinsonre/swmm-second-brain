---
title: "S288: ICM Link Results SQL, summary written from the page (v1.0)"
type: source
raw: raw/apps/icm-link-results-sql-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-18
tags: [apps, icm, sql, results, link-variables]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app ICM Link Results SQL, version 1.0: the 2026 edition, as an app, of Bob's article on the link variables of InfoWorks ICM SQL: the tsr. time-series fields for InfoWorks and SWMM networks, a builder that writes the aggregate query, and a synthetic sample run. Raw file: [raw/apps/icm-link-results-sql-v1.0.md](../../raw/apps/icm-link-results-sql-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/UKwRW35Hn1SBZMh4RpXehf, version 1793652990-4020 (index.html, 116,945 bytes, SHA-256 2dbd8dc92f3e9b2cec43042fe2989a66d80050d78d433d3d91b7e232d897034a), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file." The page says it was built with Claude under Bob's direction; no ICM run was made for this build.

**Claims worth keeping** (all copied from the file)
- SQL sees only the saved timesteps, so MAX misses a peak between saves, and SUM of a flow stays in cfs until multiplied by the save interval; in the sample run 49,496 ft3 pass the upstream end of C1 in six hours.
- The InfoWorks engine reports a link at both ends (tsr.us_flow and tsr.ds_flow); the SWMM network reports one value per conduit (tsr.flow).
- Given the published query's eight fields, the builder reproduces its 40 aggregate columns word for word; 33 mechanical checks pass.
- Full-bore Manning flow for C1 is 20.23 cfs; the largest open-channel flow in a circular pipe is at y/D = 0.9382, 1.0757 times full-bore flow.

**Limits it states.** No ICM run; the field spellings taken from the help and the SWMM-network queries are untested in ICM; the sample run is a teaching model. It may be a later version of an older site (icm-sql-cookbook).

**Checked at ingest.** The y/D = 0.9382 and 1.0757 figures come from the page's own scan of 10,000 depths; nothing else in the summary can be checked by arithmetic. The `links:` line gives Netlify as "not yet deployed (an older site".

**Feeds:** [ICM Link Results SQL (app)](../entities/icm-link-results-sql.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
