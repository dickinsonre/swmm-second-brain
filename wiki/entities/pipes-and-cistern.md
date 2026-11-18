---
title: "Pipes & Cistern (app)"
type: entity
updated: 2026-11-18
sources: [S365]
tags: [apps, teaching, tanks, orifices]
reviewed: no
---
Bob's app Pipes & Cistern: the exam rate problems, and what a real tank with a hole does instead. Version 1.0, 2026-10-25 [S365](../sources/S365-pipes-and-cistern-summary.md). Its `links:` line names no live Netlify address [S365](../sources/S365-pipes-and-cistern-summary.md).

**A caution about its source.** The page ships no technical summary. [S365](../sources/S365-pipes-and-cistern-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S365](../sources/S365-pipes-and-cistern-summary.md)
- Practice problems, live calculators and the formula sheet for the two classic rate problems, Time & Work and Pipes & Cistern, plus a Real Tank tab that shows what a straight-walled tank with a hole in the floor actually does, with an exact Torricelli solution and a SWMM5 model to export.
- The exam answer assumes constant rates; a real leak slows as the water falls. With a 6-hour pipe and an 18-hour leak the exam line fills at 9 h and the real tank at 11.66 h; with a 6-hour pipe and a 10-hour leak the exam fills at 15 h and the real tank stalls at 69.4% full. Depths from EPA SWMM 5.2.4 runs of the exported files fall on the exact curve. Sixteen defects in the Lovable version are fixed (D1 to D16), including a chart that ignored Pipe B.
- The generator harness: 20,000 draws per template, each answer re-solved independently from the question text; six generator defects and one duplicate template fixed (D1 to D6).
- Ten calculator and formula defects fixed (D7 to D16), among them the √xy and pairwise formulas.
- The exact tank solution against Runge-Kutta integration and against SWMM 5.2.4 (three cases).
- Contrast check of both themes; headless-browser screenshots at desktop and phone widths in both themes.

**How to use it, as the summary puts it.** Use it to drill the exam method and to see where it stops matching a tank. The exam model ignores pump curves and falling heads, the Real Tank covers one kind of leak, and the SWMM check covers three cases, not the whole map. [S365](../sources/S365-pipes-and-cistern-summary.md)

**What it does not show.** As the page lists it: constant rates in the exam model (no pump curves, no reservoir-fed pipe that slows as heads converge); one kind of leak (a sharp-edged hole in the floor of a straight-walled tank, constant discharge coefficient, nothing downstream); the SWMM check covers three cases, not a sweep; the eighteen templates cover the common exam patterns, not every one in the books. [S365](../sources/S365-pipes-and-cistern-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Orifices](../concepts/orifices.md).
