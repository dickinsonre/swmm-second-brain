---
title: "S177: Investigating Curve Number Approximations on an ICM InfoWorks 2D Infiltration Surface (LinkedIn, 2023)"
type: source
raw: raw/linkedin/2023-09-22-investigating-curve-number-approximations-icm-2d-robert-dickinson.md
kind: linkedin-article
author: Robert Dickinson
published: 2023-09-22
ingested: 2026-11-16
tags: [icm, 2d, infiltration, curve-number]
reviewed: no
---
**What it is.** Bob's article on standing in for the Curve Number method on an ICM InfoWorks 2D infiltration surface, before ICM offered it there. Raw file: [raw/linkedin/2023-09-22-investigating-curve-number-approximations-icm-2d-robert-dickinson.md](../../raw/linkedin/2023-09-22-investigating-curve-number-approximations-icm-2d-robert-dickinson.md). Most of the results are in images that are not in `raw/`.

**How it was written.** Bob's article. It does not state any AI use. No numbers from its result figures are in the text, so the claims below are what the text says.

**Claims worth keeping**
- In 2023, ICM subcatchments could use CN and CNSWMM infiltration on a pervious runoff surface, but 2D infiltration surfaces were limited to four types: Horton, Green-Ampt, Constant Infiltration and Fixed Infiltration.
- The four as the article describes them: Horton (capacity declines with time from an initial to a constant rate); Green-Ampt (a function of soil moisture, used for intense rainfall); Constant Infiltration (a constant rate and a fixed runoff coefficient); Fixed (a fixed runoff coefficient).
- So a user wanting Curve Number behavior on the 2D mesh had to approximate it with one of the four.
- The test model: 23 subcatchments, each with an ID equal to its Curve Number (subcatchment 80 has CN 80); one pervious runoff surface; SWMM hydrology; four 2D infiltration surfaces, one per type; four scenarios with the base using CN infiltration; three rainfall events of 0.065 in, 0.65 in and 6.5 in (1.65 mm, 16.5 mm and 165 mm; conversion ours). The infiltration parameters for each scenario were set with SQL.
- 1D result: as CN decreases, both the peak infiltration rate and the total infiltration volume increase.
- Setting a constant loss rate for Horton, Green-Ampt and ConstInf from the CN peak infiltration rate (by SQL) made the peak and volume of infiltration close across all four methods, given the simple hyetographs used in 2D modeling; for small storms they were almost the same.
- The article says SWMM's nonlinear reservoir hydrology helps align the 1D results, while on a 2D surface the results are bound to differ because of the varying depths across the mesh.
- 2D result: for the smaller rainfall, Constant Infiltration, Green-Ampt and Horton had the same effective infiltration rate and Fixed was different. The article reads this as showing that a rate calibrated to the CN rate can work on the 2D mesh. The 2D log reports the total infiltration for each surface.
- A Ruby script to compute mean and total infiltration per mesh element within a 2D infiltration polygon was then under development.

**Feeds:** [ICM 2D: rainfall and infiltration on the mesh](../concepts/icm-2d-rainfall-and-infiltration.md), [Infiltration methods](../concepts/infiltration-methods.md).
