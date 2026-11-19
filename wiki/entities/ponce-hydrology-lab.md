---
title: "Ponce Hydrology Lab (app)"
type: entity
updated: 2026-11-19
sources: [S361, S390]
tags: [apps, hydrology, calculators, audits]
reviewed: no
---
Bob's app Ponce Hydrology Lab: thirty-six hydrology and hydraulics modules after Victor Miguel Ponce's web library. Version 1.3, 2026-11-19 [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md); version 1.2 of 22 October 2026 is summarized in [S361](../sources/S361-ponce-hydrology-lab-summary.md). Netlify address: https://ponce-hydrology-lab.netlify.app [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md).

**A caution about its source.** Version 1.3 ships its own technical summary, written by Claude with the app [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md). Version 1.2 shipped none. [S361](../sources/S361-ponce-hydrology-lab-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the 1.2 summary says** [S361](../sources/S361-ponce-hydrology-lab-summary.md)
- Thirty-six hands-on hydrology and hydraulics modules in one file, built on the web hydrology library of Prof. Victor Miguel Ponce at San Diego State University: move a slider and the equation, the numbers and the chart answer at once. An independent adaptation, from Bob's Lovable project aquifer-quest-zone, and a teaching instrument, not a design code.
- Fifty-seven calculation defects were fixed across three versions (nineteen in v1.0, seven in v1.1, thirty-one in v1.2), each with the original code quoted in the Doc register. The page passes 208 unit tests and 26 formulation checks against Prof. Ponce's own calculator pages; in v1.2 the theory and reference text got 32 corrections and 13 dead links fixed.
- 208 unit tests; 26 formulation checks against Prof. Ponce's calculator pages.
- Every one of the 36 module pages, plus the home, About and Doc pages, opened in headless Chromium in both themes, both unit systems and at 375 px: no console errors, no sideways scroll, and in US mode no SI unit left on any page.
- 57 defects fixed, listed with the original code.

**How to use it, as the summary puts it.** Use it to teach hydrology methods with live numbers. Each method has a range where it stops working (the Doc maps the curve number method's: runoff under 0.5 in is the least reliable), and no person has checked the modules against Ponce's textbook. [S361](../sources/S361-ponce-hydrology-lab-summary.md)

**What it does not show.** As the page lists it, starting with the curve number method: no runoff below the initial abstraction, and runoff under 0.5 in is the least reliable region (TR-55). It is a teaching instrument, not a design code. The page lists further limits by module in the Doc. [S361](../sources/S361-ponce-hydrology-lab-summary.md)

**Version 1.3.** It changed no calculation: it reshaped the Doc to Bob's rules, wrote the summary and ran the complexity meter [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md). Its summary says what is unique: "Not the calculators", since Ponce's portal at onlinecalc.sdsu.edu has had one for every method since 2004, but the audit trail, a register of 57 defects with each offending line quoted and a 26-point comparison with his own calculator pages, worst difference 0.027 % [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md). It counts 216 unit tests in 23 files, against 208 in 1.2 (Q126); 41 routes rendered headless with 0 errors and 0 NaN at 1280 and 375 px; complexity 76.1 over 140 source files [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md). "Bob Dickinson directed the work and read the register; no hydrologist outside the project has reviewed the numbers" [S390](../sources/S390-ponce-hydrology-lab-app-md-v1-3.md).

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Infiltration methods](../concepts/infiltration-methods.md).
