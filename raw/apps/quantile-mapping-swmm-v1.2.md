---
name: Quantile Mapping to SWMM5 / SWMM6
file: quantile-mapping-swmm.html
version: "1.2"
date: 2026-10-20
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/PEkNxyDmUpfD5qDBSTqtMy", repo: none named in the page}
engines:
  - {name: a JavaScript port of SWMM5's runoff routine, note: "compared in 72 numbers with EPA SWMM 5.2.4"}
paper: "Niranjan Kumar et al. (2022), Hydrological Sciences Journal 67:6"
units: mm/day, as in the paper
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says Claude (Opus 5) built it in September 2026 and wrote the document in October, under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/PEkNxyDmUpfD5qDBSTqtMy, version 1792508736-2add (index.html, 125,318 bytes, SHA-256 4b8cea993439aaecaa5d7a6f889eaa70be55af95223cca96737415b8df95ccdc), its tabs and Doc read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Quantile Mapping to SWMM5 / SWMM6: can a rainfall bias correction feed the engine?

## In three points
- **What:** Shows how quantile mapping corrects a weather model's rainfall (after Niranjan Kumar et al. 2022), runs the paper's three variants (EQM, PQM, GPQM) on a synthetic monsoon, and carries a corrected daily total into SWMM.
- **So what:** On 2,440 synthetic monsoon days rain falls on 70 per cent but the model rains on 92 per cent; SWMM5 cannot do quantile mapping (its only rainfall adjustment is one monthly multiplier in gage.c), but it can use a corrected [TIMESERIES].
- **Now what:** Correct forecast rain before it reaches the model and pass it in as a time series. The climate is synthetic, the three variants diverge past the largest training day, and no person has checked the implementations against the paper.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.2 · 2026-10-20"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file. The page works in metric (mm/day, as the paper does).

## What it does

Four tabs and a Doc: 1, How QM works (drag a forecast across two CDFs; x-hat = F_obs^-1(F_mod(x)), with a dry-day fix); 2, EQM vs PQM vs GPQM, scored on seasons the fitting never saw; 3, Into SWMM, carrying a corrected total through a port of SWMM5's runoff routine and writing an input file; 4, the SWMM5 / SWMM6 verdict; 5, Doc. The paper trained on the IMDAA reanalysis and applied the mapping to NCUM operational forecasts for a Mumbai flood-warning setting.

## Results the page reports

- Training record: 2,440 generated monsoon days; observed rain on 70 per cent, model rain on 92 per cent.
- The three corrections and SWMM5's monthly multiplier agree to about 40 mm on the default climate; past the largest training day they extrapolate.
- Linear scaling (one multiplier) cannot delete drizzle or stretch a tail; it is the only rainfall adjustment SWMM5 offers natively (Adjust.rainFactor from Adjust.rain[month-1] in climate.c, applied in gage.c).

## Checks (as stated on the page)

- A 72-number comparison of the runoff port against EPA SWMM 5.2.4, run and rerun while the document was written.
- Every figure computed by executing the page's own exported code.

## What this does not show

- The climate is synthetic.
- No person has independently reviewed the quantile-mapping implementations against the paper, which was unavailable to the build.

## How to reproduce

Open the page and work through tabs 1 to 4; tab 3 writes the SWMM input.

## Credits and licenses

Niranjan Kumar et al. (2022), Hydrological Sciences Journal 67:6. EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says Robert Dickinson directed the work and is responsible for it: he chose the paper, set the question, required that physics claims be checked against a compiled engine, and reviewed the result. Claude (Opus 5, Anthropic) built the page in September 2026 (the quantile-mapping implementations, the synthetic climate generator, the port of SWMM5's runoff routine, the input-file writer, the plotting) and in October 2026 wrote the document and its figures. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.2 (2026-10-20): the version read; the Doc was written in October 2026.
- Earlier versions: September 2026.
