---
title: "ICM Link Results SQL (app)"
type: entity
updated: 2026-11-18
sources: [S288]
tags: [apps, icm, sql, results, link-variables]
reviewed: no
---
Bob's app ICM Link Results SQL: the 2026 edition, as an app, of Bob's article on the link variables of InfoWorks ICM SQL: the tsr. time-series fields for InfoWorks and SWMM networks, a builder that writes the aggregate query, and a synthetic sample run. Version 1.0, 2026-11-02 [S288](../sources/S288-icm-link-results-sql-summary.md). Its `links:` line names no live Netlify address [S288](../sources/S288-icm-link-results-sql-summary.md).

**A caution about its source.** The page ships no technical summary. [S288](../sources/S288-icm-link-results-sql-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S288](../sources/S288-icm-link-results-sql-summary.md)
- SQL sees only the saved timesteps, so MAX misses a peak between saves, and SUM of a flow stays in cfs until multiplied by the save interval; in the sample run 49,496 ft3 pass the upstream end of C1 in six hours.
- The InfoWorks engine reports a link at both ends (tsr.us_flow and tsr.ds_flow); the SWMM network reports one value per conduit (tsr.flow).
- Given the published query's eight fields, the builder reproduces its 40 aggregate columns word for word; 33 mechanical checks pass.
- Full-bore Manning flow for C1 is 20.23 cfs; the largest open-channel flow in a circular pipe is at y/D = 0.9382, 1.0757 times full-bore flow.

**What it does not show.** No ICM run; the field spellings taken from the help and the SWMM-network queries are untested in ICM; the sample run is a teaching model. It may be a later version of an older site (icm-sql-cookbook). [S288](../sources/S288-icm-link-results-sql-summary.md)

**Noted at ingest.** The y/D = 0.9382 and 1.0757 figures come from the page's own scan of 10,000 depths; nothing else in the summary can be checked by arithmetic.

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md), [InfoWorks ICM](infoworks-icm.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
