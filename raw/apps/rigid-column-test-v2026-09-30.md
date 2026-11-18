---
name: The Rigid Column Test
file: rigid-column-test.html
version: "2026-09-30"
date: 2026-09-30
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/J5Lf3bwToNCdfQsrKxBGL9", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "compiled from source on 30 September 2026; results recorded in the page"}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, note: "compiled from source on 30 September 2026"}
units: SI (m, m/s, m3/s) as the page uses them; US figures here are our conversions
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/J5Lf3bwToNCdfQsrKxBGL9, version 1790764357-4225 (index.html, 653,649 bytes, SHA-256 8bacce7b93142b0df20218cfbee9dfb3850767af7df6dd98488e391cf4bb1b7c), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# The Rigid Column Test: SWMM 5.2.4 and OpenSWMM 6 against an exact pressurised transient

## In three points
- **What:** A full horizontal pipe between two fixed heads, started from rest, has an exact closed-form answer, V(t) = V_inf tanh(t/tau); the page puts it to SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4, varying the surcharge method, node storage and virtual junctions one at a time.
- **So what:** EXTRAN in both engines lands on the exact curve within 1%; the 5.2.4 slot hits its own wave celerity within 4% but carries +3.8% on the steady velocity; the stock dynamic slot runs a factor of 1.414 fast; and the two virtual-junction runs fail on initial conditions.
- **Now what:** Use the exact pipe as a check on any surcharge method before trusting pressurised results. One pipe geometry, two engine builds of 30 September 2026.

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is its build date (both engines compiled on 30 September 2026). The file name above is ours. Every number below is copied from the page; US conversions are ours. Nothing was run to write this file.

## The test (as the page states it)

- Pipe: 1,000 m (3,281 ft), D 1 m (3.28 ft), n 0.013, horizontal, full at rest, from a 5 m reservoir to a 3 m fixed outfall (Delta H 2 m, 6.56 ft); a chain version splits it into 20 x 50 m with 19 junctions.
- Exact answer: V_inf = 1.3652 m/s (4.48 ft/s), Q_inf = 1.0722 m3/s (37.9 cfs), tau = 69.6 s; 76% of V_inf at 70 s, 99% at 184 s.

## Results the page reports

- Thirteen of fifteen runs share one number set with the single pipe (EXTRAN and every slot variant, both engines, both unit systems).
- Wave test (outfall dropped from 5 m to 3 m over one second after two minutes at equal heads): EXTRAN behaves as the incompressible limit; SWMM 5.2.4 SLOT (Sjoberg 1% slot, 27.8 m/s celerity) measured 26.7 to 28.5 m/s and +3.814% on V_inf in both unit systems.
- The two virtual-junction rows are an initial-condition failure, not a slot failure.
- The stock dynamic slot runs a factor of the square root of 2 (1.414) fast.
- A junction's storage is the larger of the slot's contribution and MIN_SURFAREA.

## What this does not show

- Any geometry other than this one pipe and its chain version.
- Builds after 30 September 2026.

## How to reproduce

Open the page; the exact solution and every recorded run are shown side by side.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); OpenSWMM 6 (HydroCouple), Apache-2.0. No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026-09-30: the version read.
