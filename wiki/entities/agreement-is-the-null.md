---
title: "Agreement Is the Null (app)"
type: entity
updated: 2026-11-18
sources: [S273]
tags: [apps, engine-comparison, verification, swmm5, extran, step-sensitivity]
reviewed: no
---
Bob's app Agreement Is the Null: a rethink of engine comparison measured on 16 public test models (864 conduits, 328 runs of EPA SWMM 5.2.4), putting every option difference on one scale: the uniform change in Manning's n that moves the result as far. Version 1.1.0, 2026-10-04 [S273](../sources/S273-agreement-is-the-null-summary.md). Netlify address, from its `links:` line: https://engine-ageement-is-the-null.netlify.app [S273](../sources/S273-agreement-is-the-null-summary.md).

**A caution about its source.** The page ships no technical summary. [S273](../sources/S273-agreement-is-the-null-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S273](../sources/S273-agreement-is-the-null-summary.md)
- EXTRAN example 1, median time-averaged conduit difference: same run twice byte-identical; finest two steps 0.030%; shipped against refined step 0.122%; inertial terms off against on 0.177%; SLOT against EXTRAN surcharge 1.06%; n raised 2%, 5%, 10%: 0.509%, 1.25%, 2.43%.
- Its thesis: when the physics forces two engines to the same answer, their agreement describes the network; the finding is where they part.
- Agreement between engines that share code is regression testing; an independent formulation can corroborate; validation needs observations.
- Models: OpenWaterAnalytics swmm-nrtestsuite EXTRAN examples 1 to 10 (8b left out), Example3 and user1 to user5, cloned 2026-10-03; EPA SWMM 5.2.4 from swmm-toolkit.

**What it does not show.** No ICM, HEC-RAS, SWMM6, SWMM5+ or XPSWMM run: option switches stand in for cross-engine differences; no observed data; only the time step refined; fixed routing steps only; medians hide worst instants (one conduit moved 80%); the Lineage tab's scheme summaries are recalled from documentation and were not run. [S273](../sources/S273-agreement-is-the-null-summary.md)

**Noted at ingest.** The summary lists the models as "16 small models, close cousins, not the larger corpus". Its percentages are differences between runs of one engine, not errors against observations.

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
