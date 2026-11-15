---
title: "S60: EPA SWMM Reference Manual, Volume II, Hydraulics (Rossman, May 2017)"
type: source
raw: raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md
kind: epa-manual
author: Lewis A. Rossman
published: 2017-05-01
ingested: 2026-11-14
coverage: partial
read: [1.1 Introduction and Table 1-1, "Chapter 3 Dynamic Wave Analysis (3.1 to 3.4)"]
tags: [swmm5, hydraulics, primary-document, epa]
reviewed: 2026-11-15
---
**What it is.** EPA/600/R-17/111, the hydraulics volume of the SWMM 5 reference manual, by Lewis A. Rossman, U.S. EPA Office of Research and Development. A primary document: the engine's author describing what the engine computes. Raw file: [raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md](../../raw/manuals/EPA_SWMM_VOLUME_II_HYDRAULICS.md), about 50,000 words.

**How it was written.** A U.S. government report, in the public domain. The markdown is a conversion of the PDF kept in Bob's `SWMMEnablement/SWMM_MD_Documents` repository. The conversion lost most equations (symbols are garbled or missing) and the 47 figures are not in `raw/`. The prose and the numbered procedures survive. Check any equation against the EPA PDF before quoting it.

**Coverage: partial.** Read in full so far: section 1.1 with Table 1-1, and Chapter 3, Dynamic Wave Analysis. Not yet read: Chapters 2, 4, 5, 6, 7 and the appendices. Claims in the wiki come only from the parts read.

**Claims worth keeping**
- SWMM was first developed in 1969 to 1971.
- Table 1-1, development history: SWMM I, 1971, Metcalf & Eddy, Water Resources Engineers and the University of Florida; SWMM II, 1975, University of Florida, the first widely distributed version; SWMM 3, 1981, University of Florida and Camp Dresser & McKee, adding the full dynamic wave routine, Green-Ampt infiltration, snow melt and continuous simulation; SWMM 3.3, 1983, US EPA, the first PC version; SWMM 4, 1988, Oregon State University and Camp Dresser & McKee, adding groundwater, RDII and irregular channel cross-sections over the 1990s; SWMM 5, 2005, US EPA and CDM-Smith, a complete rewrite in C.
- Dynamic wave modeling entered SWMM in version 3, in 1981, as a separate module called EXTRAN. Its node-link method came from the Sacramento-San Joaquin Delta Model (1965) and the WRE Transport Model (1975).
- Earlier versions solved the link equation with an explicit method (forward Euler; more exactly the two-step Modified Euler). SWMM 5 uses an implicit backward Euler method "to provide improved stability".
- The implicit equations are solved by functional iteration (successive approximations, or Picard's method): new flow for each link, relaxation, new head for each node, relaxation, repeat until the heads stop changing.
- The relaxation factor is 0.5. The default convergence tolerance is 0.005 ft and the default maximum number of trials is 8.
- Flows and heads are updated one conduit and one node at a time, not simultaneously, so there is no spatial coupling between elements and the Courant condition "would still apply but perhaps not as strictly".
- Minimum nodal surface area defaults to 12.56 sq ft, the area of a 4 ft manhole. It is a computational device and adds no volume.
- Inertial damping: the factor is 1 for Froude numbers up to 0.5, 0 at 1 or higher, linear between. A second option ignores the inertial term altogether.
- A node is surcharged when all conduits connected to it are full or its water level is above the crown of the highest connected conduit. Head is then updated by a perturbation equation, and under-relaxation is not applied to it.
- A node whose head would exceed its maximum is flooded and the excess is lost from the system, unless the node has a ponded area, in which case the water is stored above it and returns.
- A system continuity error above 5 to 10 percent may be a sign of numerical instability. The Flow Instability Index of a link ranges from 0 to 150 and does not measure the size of the fluctuations.
- Example: a 2 ft by 2 ft conduit, 2,000 ft long, in 10 sections of 200 ft has a stable time step of about 25 s; as one 2,000 ft section, about 250 s. A fixed step of 120 s on the 10-section conduit is completely unstable; a variable step capped at 120 s is stable.

**Feeds:** [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [EXTRAN](../entities/extran.md), [SWMM 1 (1971)](../entities/swmm-1.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [Open questions](../open-questions.md).
