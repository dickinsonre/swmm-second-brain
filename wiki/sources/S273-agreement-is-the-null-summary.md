---
title: "S273: Agreement Is the Null, summary written from the page (v1.1.0)"
type: source
raw: raw/apps/engine-ageement-is-the-null-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-04
ingested: 2026-11-18
tags: [apps, engine-comparison, verification, swmm5, extran, step-sensitivity]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Agreement Is the Null, version 1.1.0: a rethink of engine comparison measured on 16 public test models (864 conduits, 328 runs of EPA SWMM 5.2.4), putting every option difference on one scale: the uniform change in Manning's n that moves the result as far. Raw file: [raw/apps/engine-ageement-is-the-null-v1.1.0.md](../../raw/apps/engine-ageement-is-the-null-v1.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/TEHw1e5WwvAuzsVfoBLQXg, version 1791082767-18b1 (index.html, 998,363 bytes, SHA-256 e6d0936791265279b15201ef4176669fd8d849a984bb0ccb761807b960d35fa3), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page carries no AI-use note; it is a Claude artifact on Bob's account, built in a claude.ai session.

**Claims worth keeping** (all copied from the file)
- EXTRAN example 1, median time-averaged conduit difference: same run twice byte-identical; finest two steps 0.030%; shipped against refined step 0.122%; inertial terms off against on 0.177%; SLOT against EXTRAN surcharge 1.06%; n raised 2%, 5%, 10%: 0.509%, 1.25%, 2.43%.
- Its thesis: when the physics forces two engines to the same answer, their agreement describes the network; the finding is where they part.
- Agreement between engines that share code is regression testing; an independent formulation can corroborate; validation needs observations.
- Models: OpenWaterAnalytics swmm-nrtestsuite EXTRAN examples 1 to 10 (8b left out), Example3 and user1 to user5, cloned 2026-10-03; EPA SWMM 5.2.4 from swmm-toolkit.

**Limits it states.** No ICM, HEC-RAS, SWMM6, SWMM5+ or XPSWMM run: option switches stand in for cross-engine differences; no observed data; only the time step refined; fixed routing steps only; medians hide worst instants (one conduit moved 80%); the Lineage tab's scheme summaries are recalled from documentation and were not run.

**Checked at ingest.** The summary lists the models as "16 small models, close cousins, not the larger corpus". Its percentages are differences between runs of one engine, not errors against observations. The `links:` line gives Netlify as https://engine-ageement-is-the-null.netlify.app.

**Feeds:** [Agreement Is the Null (app)](../entities/agreement-is-the-null.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
