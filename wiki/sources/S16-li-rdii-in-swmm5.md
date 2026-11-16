---
title: "S16: How Does RDII Work in SWMM5, InfoSWMM and InfoWorks ICM? (LinkedIn, 2019)"
type: source
raw: raw/linkedin/2019-10-04-how-does-rdii-work-swmm5-infoswmm-infoworks-icm-robert-dickinson.md
kind: linkedin-article
author: Robert Dickinson
published: 2019-10-04
ingested: 2026-11-14
tags: [rdii, hydrology, swmm5]
drafted_by: an AI (not named), rewriting EPA SWMM5 help text
reviewed: 2026-11-15
---
**What it is.** The SWMM5 help-file text on rainfall-dependent inflow and infiltration, "refactored". Raw file: [raw/linkedin/2019-10-04-how-does-rdii-work-swmm5-infoswmm-infoworks-icm-robert-dickinson.md](../../raw/linkedin/2019-10-04-how-does-rdii-work-swmm5-infoswmm-infoworks-icm-robert-dickinson.md). The title also names InfoSWMM and ICM, but the exported text covers SWMM5 only; those parts were images.

**How it was written.** EPA SWMM5 help text, later rewritten with an AI tool (emoji throughout); the article does not name it.

**Claims worth keeping**
- A unit hydrograph set holds up to three triangular hydrographs: short-term, intermediate-term and long-term response.
- A unit hydrograph group holds up to 12 sets, one per month, and names the rain gage that feeds it.
- Each hydrograph has three parameters: R, the fraction of rainfall volume that enters the sewer; T, hours from the start of rain to the peak; K, the ratio of time to recession to time to peak.
- Initial abstraction has three parameters: Dmax, Drec and Do. A blank parameter is taken as 0.
- A node receives RDII by naming a unit hydrograph group and a sewershed area in its Inflows property.
- RDII and routing interface files share one text format; RDII files written by SWMM are binary.
- With calibrated unit hydrographs, RDII can stand in for the subcatchment rainfall-runoff procedure.

**Feeds:** [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md).
