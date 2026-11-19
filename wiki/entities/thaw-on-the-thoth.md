---
title: "Thaw on the Thoth (document)"
type: entity
updated: 2026-11-19
sources: [S308, S377]
tags: [documents, swmm5, fiction, gravity, weirs, finite-volume]
reviewed: no
---
Bob's document Thaw on the Thoth: a story of two boys, one Martian canal and the spring thaw of 2097. Version and date 2026-10-21 [S308](../sources/S308-thaw-on-the-thoth-summary.md). Its `links:` line names no live Netlify address [S308](../sources/S308-thaw-on-the-thoth-summary.md).

**A caution about its source.** The page ships no technical summary. [S308](../sources/S308-thaw-on-the-thoth-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S308](../sources/S308-thaw-on-the-thoth-summary.md)
- A short story in seven chapters and an afterword, in the spirit of Robert A. Heinlein's Red Planet (1949). Two boys at a Mars colony check the Canal Company's SWMM forecast for a thaw on an invented canal, the Thoth, and find that gravity hides in Manning's n and the weir coefficient. The people, the colony and the night of the thaw are invented. The canal model, the two engines and every number on every chart come from runs of EPA SWMM 5.2.4 and swmm524-fvlink rebuilt with Mars gravity, and the afterword sorts one from the other.
- Changing GRAVITY from 32.2 to 12.2 alone left mile one at 2.38 ft at base flow, because gravity sits in both the slope term and the friction term (Conduit[k].roughFactor = GRAVITY * SQR(roughness/PHI)). Holding g·n² fixed scales n by 1.625 (0.015 to 0.0244) and the weir coefficient by 0.6155 (3.33 to 2.050). The Upper Thoth then carries 4,439 cfs bank-full instead of 7,213, against a 4,200 cfs crest, and the basin reaches the top of its 14.5 ft levee at hour 40.3 (the chart's legend says 40.4) instead of cresting at the Company's 13.3 ft. Building the model also found water running uphill through a finite volume throat, now entered as FVL-15 in the branch's defect register.

**How to use it, as the summary puts it.** Use it to see why a constant that was right on Earth can be wrong in a model, and where to look for it. The Thoth has no survey behind it, the n and weir scaling is a dimensional argument no one has checked against data, and no person has yet reviewed the story or rerun the models. [S308](../sources/S308-thaw-on-the-thoth-summary.md)

**What it does not show.** As the document states: the Thoth is invented and has no survey behind it; the scaling of n and the weir coefficient is ordinary dimensional reasoning that has never been checked against flow in a lined canal on Mars; the gauge readings are fiction set near the model's values; no person has yet reviewed the story or rerun the models, and no other engineer has checked the scaling. [S308](../sources/S308-thaw-on-the-thoth-summary.md)

**Noted at ingest.** The story's text says the basin reaches the top of the levee at hour 40.3; the legend of its chart "The forecast at the levee" says "at the crest by hour 40.4" (Q118). A Claude Docs document, exported as HTML with its 16 pictures for Netlify.

**Added 19 November 2026.** [FV Link Lab](fv-link-lab.md) 1.1.0 runs the Thoth canal in a Mars tab [S377](../sources/S377-fv-link-lab-app-md.md). Gravity is compiled into SWMM (`consts.h:37 #define GRAVITY 32.2`), so the tab turns each Mars model into an equivalent Earth model with k = sqrt(32.2 / 12.2) = 1.624606: flows multiplied by k, times divided by k, Manning's n 0.0244 to 0.0150 and the weir coefficient 2.050 to 3.330 [S377](../sources/S377-fv-link-lab-app-md.md). Run natively, the scaled gate-shut model gives 134.827 Mgal over the levee against 134.830 from the Mars-gravity build, with continuity -0.039 % in both [S377](../sources/S377-fv-link-lab-app-md.md). The same file gives the levee hour as 40.33 in the story's runs, which kept Earth handbook n on the culvert, Chute, intake channel and Old Canal, and 40.50 with every n scaled; the tab's own nospill runs give 40.49 (stock) and 40.41 (FV) [S377](../sources/S377-fv-link-lab-app-md.md) (Q121). The defect the story found, FVL-15, is still open: five prototype fixes were tried and none adopted [S377](../sources/S377-fv-link-lab-app-md.md).

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [EPA SWMM 5](swmm-5.md).
