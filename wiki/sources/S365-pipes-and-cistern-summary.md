---
title: "S365: Pipes & Cistern, summary written from the page (v1.0)"
type: source
raw: raw/apps/pipes-and-cistern-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, teaching, tanks, orifices]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Pipes & Cistern, version 1.0: the exam rate problems, and what a real tank with a hole does instead. Raw file: [raw/apps/pipes-and-cistern-v1.0.md](../../raw/apps/pipes-and-cistern-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Diae8f2gzMwTokUbuRzYDq, version 1792898560-6bb1 (index.html, 1,206,613 bytes, SHA-256 5ac2ab99236c7ad160e04aeb27f6bbf9892c0a8d072c18da81dba42eee6b0d2e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in October 2026 under the direction of Robert (Bob) Dickinson, who built the original Lovable app, supplied its source and asked for an HTML version; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Practice problems, live calculators and the formula sheet for the two classic rate problems, Time & Work and Pipes & Cistern, plus a Real Tank tab that shows what a straight-walled tank with a hole in the floor actually does, with an exact Torricelli solution and a SWMM5 model to export.
- The exam answer assumes constant rates; a real leak slows as the water falls. With a 6-hour pipe and an 18-hour leak the exam line fills at 9 h and the real tank at 11.66 h; with a 6-hour pipe and a 10-hour leak the exam fills at 15 h and the real tank stalls at 69.4% full. Depths from EPA SWMM 5.2.4 runs of the exported files fall on the exact curve. Sixteen defects in the Lovable version are fixed (D1 to D16), including a chart that ignored Pipe B.
- The generator harness: 20,000 draws per template, each answer re-solved independently from the question text; six generator defects and one duplicate template fixed (D1 to D6).
- Ten calculator and formula defects fixed (D7 to D16), among them the √xy and pairwise formulas.
- The exact tank solution against Runge-Kutta integration and against SWMM 5.2.4 (three cases).
- Contrast check of both themes; headless-browser screenshots at desktop and phone widths in both themes.

**Limits it states.** As the page lists it: constant rates in the exam model (no pump curves, no reservoir-fed pipe that slows as heads converge); one kind of leak (a sharp-edged hole in the floor of a straight-walled tank, constant discharge coefficient, nothing downstream); the SWMM check covers three cases, not a sweep; the eighteen templates cover the common exam patterns, not every one in the books.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Pipes & Cistern (app)](../entities/pipes-and-cistern.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Orifices](../concepts/orifices.md).
