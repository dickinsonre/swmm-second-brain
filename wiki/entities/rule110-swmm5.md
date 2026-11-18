---
title: "Rule 110 in SWMM5 (app)"
type: entity
updated: 2026-11-17
sources: [S204, S205, S229]
tags: [apps, swmm5, controls, storage, cellular-automata, wasm]
reviewed: no
---
Bob's app Rule 110 in SWMM5: an unmodified EPA SWMM 5.2.4 model whose storage nodes are the cells of any of the 256 elementary cellular automata, written by the page, run in the browser and checked cell by cell against the automaton. Version 1.0.0, 2026-11-09 [S229](../sources/S229-rule110-swmm5-summary.md). Netlify address: https://rule110-swmm5.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S229](../sources/S229-rule110-swmm5-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S229](../sources/S229-rule110-swmm5-summary.md)
- A cell is a storage node of 1,000 ft2 that reads 1 when its depth is above a 2 ft read line. A pump at a flat 0.5 cfs writes it, stopped by a rule at 4 ft (4 ft x 1,000 ft2 / 0.5 cfs = 8,000 s); a 6 in orifice erases it. A day holds two generations in four 6-hour phases.
- Default run: Rule 110, 48 cells, 40 generations, 20.25 simulated days at a 60 s step: 1,968 cells read from the .out, 0 disagreements. Every 1 stood at 4.020 ft or more and every 0 at 0.0043 ft or less; routing continuity 0.000 %.
- Eight automata from seven rules (110, 30, 90, 108, 54, 150, 184) ran in native EPA SWMM 5.2.4 and in the browser build: all 10,700 cells matched in both, and the two engines' results were byte-identical in every case.
- Pump sweep: the write pump must lift at least 0.0926 cfs; at 0.09 cfs 513 of 1,968 cells are wrong, at 0.095 cfs none. Orifice sweep: at 0.1 ft diameter 342 cells are wrong.
- The infographic printed eight rule bits as 0 1 1 0 1 1 0 0, which is Rule 108, not Rule 110.
- Side findings: the bundled @bjorn3/browser_wasi_shim 0.4.2 grows files to their exact size on every write, and a twelve-line patch cut the default run from 14.4 s to 3.5 s with a byte-identical .out. Native Linux EPA SWMM 5.2.4 aborts with "buffer overflow detected" on a relative input path when fortify checks are on (getAbsolutePath in swmm5.c, realpath into a 260-byte buffer).
- 773 logic checks pass, including all 256 rules against an independent table and Rule 30's centre column against OEIS A051023.

**What it does not show.** Not a universal computer: the tape has at most 96 cells. No conduits, dynamic-wave momentum, surcharge or ponding: every link is a pump, an orifice or the one weir. One hydraulic design; only EPA SWMM 5.2.4 was run. [S229](../sources/S229-rule110-swmm5-summary.md)

**Noted at ingest.** 2 ft x 1,000 ft2 / 21,600 s = 0.0926 cfs, the minimum the page gives. The fortify abort is the one the two-pipe run avoided with `-D_FORTIFY_SOURCE=0` [S204](../sources/S204-note-two-pipe-benchmark-step1-run.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Orifices](../concepts/orifices.md), [The SWMM findings register](../concepts/findings-register.md), [swmm5-kw](swmm5-kw.md).
