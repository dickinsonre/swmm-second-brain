---
title: "S278: Chanakya's Counsel for SWMM, summary written from the page (v1.6.0)"
type: source
raw: raw/apps/chanakya-swmm5-swmm6-v1.6.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, decision-making, review, swmm5, teaching]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Chanakya's Counsel for SWMM, version 1.6.0: a decision app that walks one SWMM drainage decision through five stations taken from Kautilya's Arthashastra (Brief, Audit, Spies, Alternatives, Writ), with six measures run in EPA SWMM 5.2.4 on one sample model. Raw file: [raw/apps/chanakya-swmm5-swmm6-v1.6.0.md](../../raw/apps/chanakya-swmm5-swmm6-v1.6.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/DAmSUwjkmJT4qppSYm3BH6, version 1792434855-a876 (index.html, 2,133,599 bytes, SHA-256 18809cc3172052a84151227580a0ae3458aa4d6477f8fc0d9a7dc3ffcc88b5ee), its room, Sources and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude in Claude Code sessions in October 2026 under Bob's direction, with nine outside reviews; for 1.6 five separate Claude reviewers checked the claims, code, accessibility, citations and importer.

**Claims worth keeping** (all copied from the file)
- 64 engine runs of one sample model, all in the page's evidence package; three separate engine builds reproduce every packaged report exactly.
- At the 2.0 in decision storm the opening measure ("War: enlarge the pipe") gives an outfall peak of 42.3 cfs.
- With inertial damping off, storage at J3 floods 0.014 ac-ft at 2.0 in, and kinematic-wave routing nearly quadruples the base flooding.
- The page marks its pairing of statecraft and modeling as its own analogy and says the popular "three questions" saying is not in the Arthashastra.

**Limits it states.** No cost; no calibration (the meter reading is invented for teaching); one network; one two-hour storm shape; no water quality; no person has checked the quotations against the printed books; no screen reader, Safari or Firefox tried.

**Checked at ingest.** Nothing in the summary can be checked by arithmetic. The `links:` line gives Netlify as https://chanakya-swmm5-swmm6.netlify.app.

**Feeds:** [Chanakya's Counsel for SWMM (app)](../entities/chanakya-counsel.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md).
