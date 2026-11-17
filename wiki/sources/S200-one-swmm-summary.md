---
title: "S200: One SWMM, summary written from the page (v0.2.0)"
type: source
raw: raw/apps/one-swmm-v0.2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, icm, comparison, results-reading, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of One SWMM, version 0.2.0 (9 November 2026): one page with two faces for Bob's SWMM5, SWMM6 and ICM tools. The Simple face is four doors; the Expert face holds every engine and the Agent verbs. Raw file: [raw/apps/one-swmm-v0.2.0.md](../../raw/apps/one-swmm-v0.2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary of its own. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1794263479-1aef) and its About and Doc tabs. No engine was run. Bob has not read it (Q99). The page says One SWMM was built with Claude on 5 November 2026 under Bob's direction; Bob asked for one app holding the tools with a simple face, and chose to start from Seven SWMM Engines, the Agent Engine verbs and the results kit. On 9 November Claude answered an outside review.

**Claims worth keeping** (all copied from the page)
- The four doors: run my model, compare engines, is it stable, explain this number. The page's rule: "the simple view may hide machinery, never a caveat." When the expert view would withhold a certificate, the door says "does not agree yet" and shows no green check.
- It joins three earlier apps: Seven SWMM Engines 1.2 (the engines: EPA SWMM 5.2.4, OpenSWMM 6 alpha.1 to alpha.4, SWMM 4.4H, EXTRAN III), the SWMM Results Kit 1.0 (one run record from every .rpt and .out), and the SWMM Agent Engine's contract (run, diagnose, explain, series, diff, certify, verify, plus an ICM import).
- The verbs were rebuilt over the results kit from the Agent Engine's recorded contract. That app's expected-difference register (ED-1 to ED-8) and its 778 tests were not in the session, so no expected difference is active and every difference counts.
- A certificate covers peak depth, HGL, flow, runoff and flooding under one tolerance, on one model, in one browser session.
- Kit fix: a difference exactly equal to the tolerance now passes. Floating-point subtraction had turned 4971.72 - 4971.71 into 0.010000000000218 ft, which failed a 0.01 ft HGL tolerance; on Example1 that alone withheld the SWMM6 alpha.4 certificate (four nodes, each 0.01 ft).
- ICM is read, never run: its peaks come in as a CSV and are compared, not certified.
- Every engine's numbers on Example1 match the Seven SWMM Engines 1.2 runs of 28 October 2026.
- The outside review of 0.1.0 reported six faults, each reproduced in a headless browser, fixed and retested: the storm swap (73.90 cfs with the wet rain.dat; 0.00 cfs and a new input fingerprint with the dry one); a partial result that had certified is now withheld (4 of 42 expected peaks); ROUTING_STEP 7 now stays 7 under the dynamic-wave preset; a 06:00 report start now reads hour 6.00 (results kit 1.0.1); the ICM coverage headline (1 of 11 model links matched, 15.47BAD rejected); the surcharge explanation.

**Limits it states.** Engines agreeing is not proof that any is right; nothing is checked against field data. The diagnose bands are the app's own rules, "evidence, not proof". No person has used the front door on their own model or reviewed its plain-language wording. The checks are mechanical and no person has rerun them.

**Checked at ingest.** In Python, 4971.72 - 4971.71 in double precision gives 0.010000000000218279, which is greater than 0.01, as stated. The 73.90 cfs here and 73.9 cfs in [S199](S199-seven-swmm-engines-summary.md) agree.

**Feeds:** [One SWMM (app)](../entities/one-swmm.md), [SWMM Results Kit](../entities/swmm-results-kit.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
