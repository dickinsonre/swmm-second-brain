---
title: Rules for Responsible Modeling (app)
type: entity
updated: 2026-11-14
sources: [S62, S63]
tags: [apps, calibration, uncertainty, swmm5, wasm, lovable]
reviewed: no
---
Bob's interactive edition of the 2005 book by [William (Bill) James](william-james.md), built with Lovable and served at https://rulesforresponsiblemodeling.lovable.app [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md). Version 2026.1.2, 14 November 2026, MIT license [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). Its subject is on [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md).

**Why Bob built it.** The book "was also a PDF", downloaded once and not opened again; an engineer with a deadline needs the chapter that fits the problem in hand [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md).

**Two dated descriptions**

| | February 2026 [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md) | Version 2026.1.2, November 2026 [S62](../sources/S62-rules-for-responsible-modeling-app-md.md) |
|---|---|---|
| Reading | 17 chapters, four guided pathways | Chapter lessons, micro-apps |
| Tools | Diagnostic tool by symptom; 40 item checklist by project phase; three templates | Browser SWMM Playground; browser-local Model Library; a fictional worked case |
| Engine | none mentioned | [EPA SWMM 5](swmm-5.md), declared 5.2.4, as WebAssembly |
| Chat | none mentioned | "Ask James", `google/gemini-3-flash-preview`, answering from app-written summaries |
| Tests reported | none | 61 of 61 |

**The engine in the page** [S62](../sources/S62-rules-for-responsible-modeling-app-md.md)
- `public/wasm/swmm5.wasm`, run in a web worker; the page writes the `.inp`, calls `swmm_run` and parses the `.rpt` and the binary `.out`.
- Declared EPA SWMM 5.2.4. The source commit, compiler flags and upstream license are "not checked", and no comparison against a native build was run (Q39).
- Tutorial run, 14 November 2026: return code 0, 72 periods, 3.100 in of rain, peak junction depth 1.2856794595718384 ft, peak pipe flow 13.327461242675781 cfs, continuity -0.011 % runoff and 0.019 % routing.

**The worked case** [S62](../sources/S62-rules-for-responsible-modeling-app-md.md)
- Fictional. Three subcatchments of 40, 30 and 25 acres drain to a gauged 4 ft pipe; the "observations" are a model run with hidden parameter values, with seeded noise, a gap and a spike added.
- The user audits the data, calibrates three parameters, runs a seeded ensemble of 20 to 200 runs and fills a checklist. The thresholds are on the concept page.

**Checks** [S62](../sources/S62-rules-for-responsible-modeling-app-md.md)
- `bun test tests`, 14 November 2026: 61 passed, 0 failed, 9 files, 5,064 expectation calls.
- The tests use the project's own fixtures. Published benchmark tables verified: 0.
- Review log: 83/100, 85/100 and 80/100 in early November 2026, reviewer not recorded (Q38).
- Human checks of this revision: 0.

**What it says of itself.** "These are measured software checks, not field validation, native-solver equivalence or engineering approval" [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). The 17 chapter mappings to the printed book have not been checked by a person, and the chat answers are not verified against the book's text [S62](../sources/S62-rules-for-responsible-modeling-app-md.md).

**Open.** The summary was uploaded twice, once under another app's name, and its front matter carries that app's identifier (Q35). See [Open questions](../open-questions.md).
