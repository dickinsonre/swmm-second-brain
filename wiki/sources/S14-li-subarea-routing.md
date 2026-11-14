---
title: "S14: Subcatchment Subarea Internal Routing in SWMM5, ICM SWMM and ICM InfoWorks (LinkedIn, 2024)"
type: source
raw: raw/linkedin/2024-02-03-subcatchment-subarea-internal-routing-swmm5-icm-swmm-dickinson-ebepe.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-02-03
ingested: 2026-11-14
tags: [hydrology, swmm5, icm]
reviewed: no
---
**What it is.** The three subarea routing options of SWMM5 set beside the three in an ICM InfoWorks network, with two test networks of three scenarios each. Raw file: [raw/linkedin/2024-02-03-subcatchment-subarea-internal-routing-swmm5-icm-swmm-dickinson-ebepe.md](../../raw/linkedin/2024-02-03-subcatchment-subarea-internal-routing-swmm5-icm-swmm-dickinson-ebepe.md). The result screenshots are not in the export, so the test outcomes are not recoverable from this file.

**How it was written.** By Bob (created June 2023, published February 2024); the option descriptions follow the SWMM5 help text.

**Claims worth keeping**
- SWMM5 options: IMPERV sends pervious runoff to the impervious area; PERV sends impervious runoff to the pervious area; OUTLET sends both straight to the outlet.
- Percent Routed sets the share that is rerouted. At 20 %, 20 % goes to the other subarea and 80 % to the outlet. At zero, everything goes to the outlet.
- InfoWorks options: Direct, To pervious, To impervious. The article dates the InfoWorks feature to version 6.5, November 2015.
- Section 5 is captioned "Impervious in SWMM, Impervious to Pervious in InfoWorks", which does not match the definition of IMPERV given in section 1. See [open question Q07](../open-questions.md).

**Feeds:** [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).
