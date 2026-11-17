---
name: One SWMM
file: one-swmm.html
version: 0.2.0
date: 2026-11-09
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/4GNUobZyDSHnCiZrYkZ5KA", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4 (7952ca8379)", license: public domain}
  - {name: OpenSWMM 6, version: "6.0.0-alpha.1 to 6.0.0-alpha.4", source: "HydroCouple/openswmm.engine tags v6.0.0-alpha.1 (74ef6e27aa), alpha.2 (0df29948a4), alpha.3 (86c28a886e) and swmm6_rel at 3c30f1e6c2 (2026-10-17)", license: Apache-2.0}
  - {name: SWMM 4.4H, version: "4.4H, corrected build of the SWMM 4.4H Workbench", license: not stated in the page}
  - {name: EXTRAN III, version: "April 1981 listing", license: not stated in the page}
  - {name: InfoWorks ICM, version: not run, note: "peaks read from a CSV and compared, never run"}
units: "each engine runs the file in its own FLOW_UNITS; the display switch converts to US or SI"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says One SWMM was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/4GNUobZyDSHnCiZrYkZ5KA, version 1794263479-1aef (index.html, 15,075,016 bytes, SHA-256 2d940671dfd7ca68d4c17da4989615c4223aaefe229cd2db2cef92603b2ad935), its About and Doc tabs read in headless Chromium on 2026-11-16. No model was run to write this file."
---

# One SWMM: Bob's SWMM5, SWMM6 and ICM tools behind one page with two faces

## In three points
- **What:** One page with two faces for Bob's SWMM5, SWMM6 and ICM tools: four Simple doors (run my model, compare engines, is it stable, explain this number) and an Expert view with every engine and the Agent verbs.
- **So what:** Every engine's numbers on Example1 match the Seven SWMM Engines 1.2 runs of 28 October 2026, and a tolerance fix stopped a 0.01 ft floating-point difference at four nodes from withholding the SWMM6 alpha.4 certificate.
- **Now what:** Start at the four doors. A certificate covers one model, one tolerance and one browser session, and no person has yet used the front door on their own model.

This summary was written after the fact. The page ships no technical summary of its own. Every number below is copied from the page's About tab. No engine was run to write this file.

## What it does

One SWMM puts Bob Dickinson's SWMM tools behind one page with two faces. The Simple face is four doors: run my model, compare engines, is it stable, explain this number. The Expert face is the same page with the drawers open: every engine, the map, the results tables, the reports, and the Agent view with the verbs, the ledger and the certificates.

It joins three earlier apps:

- **Seven SWMM Engines 1.2** supplies the engines and the workspace (EPA SWMM 5.2.4, OpenSWMM 6 alpha.1 to alpha.4, SWMM 4.4H, EXTRAN III, all in WebAssembly). See the Seven SWMM Engines summary for the engine table and its checks.
- **The SWMM Results Kit 1.0** reads every .rpt and .out into one run record, so every view and every verb sees the same numbers.
- **The SWMM Agent Engine's contract** supplies the verbs: run, diagnose, explain, series, diff, certify and verify, plus an ICM import.

The page's rule for the two faces: "the simple view may hide machinery, never a caveat." When the expert view would withhold a certificate, the door says "does not agree yet" and shows no green check. A pair certified for flow and depth still says so when its water quality is off.

## How it computes

- The verbs were rebuilt over the results kit from the Agent Engine's recorded contract. That app's own core (its expected-difference register ED-1 to ED-8 and its 778 tests) was not in the session, so no expected difference is active and every difference counts.
- A certificate covers peak depth, HGL, flow, runoff and flooding under one tolerance, on one model, in one browser session.
- Kit fix: a difference exactly equal to the tolerance now passes. Before, floating-point subtraction turned 4971.72 - 4971.71 into 0.010000000000218 ft, which failed a 0.01 ft HGL tolerance; on Example1 that alone withheld the SWMM6 alpha.4 certificate (four nodes, each 0.01 ft).
- ICM is read, never run. Its peaks come in as a CSV and are compared, not certified.
- The diagnose bands are the app's own rules, stated on the Agent view.

## Inputs and outputs

Reads a SWMM 5 .inp (Example1 and the Bellinge sample are built in) and an ICM peaks CSV. Writes run records, a ledger (one-swmm-ledger.json) and CSV exports.

## Checks (as stated on the page)

- A headless browser test of the four doors, the ICM import (a synthetic CSV with one peak moved 8%), certificate tampering, the ledger chain, phone width and page errors.
- Every engine's numbers on Example1 match the Seven SWMM Engines 1.2 runs of 28 October 2026.
- 0.2.0: an outside review of 0.1.0 reported six faults. Each was reproduced in a headless browser, fixed and retested:
  1. The storm swap: 73.90 cfs with the wet rain.dat; 0.00 cfs and a new input fingerprint with the dry one.
  2. A partial result that had certified is now withheld (4 of 42 expected peaks).
  3. The option writer: ROUTING_STEP 7 now stays 7 under the dynamic-wave preset.
  4. The hydrograph clock: a 06:00 report start now reads hour 6.00 (results kit changed to 1.0.1 for this).
  5. The ICM coverage headline: 1 of 11 model links matched, 15.47BAD rejected.
  6. The surcharge explanation.
- The checks are mechanical. The page says no person has rerun them.

## What this does not show

- Engines agreeing is not proof that any of them is right; nothing here is checked against field data.
- A certificate is for one model, one tolerance and one browser session.
- The diagnose bands are evidence, not proof.
- No person has yet used the front door on their own model or reviewed its plain-language wording.

## How to reproduce

Open the page, load Example1, use the four doors or switch to Expert and run the engines. The 0.2.0 fault tests are described on the About tab; the test files are not shipped with the page.

## Credits and licenses

EPA SWMM 5.2.4: USEPA, public domain. OpenSWMM 6: HydroCouple/openswmm.engine, Apache-2.0. SWMM 4.4H and EXTRAN III as in Seven SWMM Engines. Bellinge dataset: Nedergaard Pedersen et al. (2021), CC BY 4.0.

## AI use

The page says One SWMM 0.2.0 was built with Claude, Anthropic's AI model, in a Claude session on 5 November 2026, under the direction of Robert (Bob) Dickinson. He asked for one app holding the SWMM5, SWMM6 and ICM tools with a way to simplify it for normal use, and chose to start from Seven SWMM Engines, the Agent Engine verbs and the results kit. Claude drew the front-door design, wrote the verb layer, the four doors, the ICM import, the Agent view, the Simple/Expert switch, the Doc essay and the About text, found and fixed the tolerance defect in the kit, and wrote the tests. On 9 November 2026 it answered the outside review. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 0.2.0 (2026-11-09): answers an outside review of 0.1.0 (six faults, listed under Checks); results kit 1.0.1.
- 0.1.0: the version the outside review read. The page gives no date for it; its AI-use note dates the build session 5 November 2026.
