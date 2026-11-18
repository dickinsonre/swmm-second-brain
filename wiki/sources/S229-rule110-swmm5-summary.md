---
title: "S229: Rule 110 in SWMM5, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/rule110-swmm5-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-09
ingested: 2026-11-17
tags: [apps, swmm5, controls, storage, cellular-automata, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Rule 110 in SWMM5, version 1.0.0: an unmodified EPA SWMM 5.2.4 model whose storage nodes are the cells of any of the 256 elementary cellular automata, written by the page, run in the browser and checked cell by cell against the automaton. Raw file: [raw/apps/rule110-swmm5-v1.0.0.md](../../raw/apps/rule110-swmm5-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1794321164-8899, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and its essay were built with Claude in a session on 9 November 2026 at Bob's request: Bob asked whether an infographic was of use and chose the idea of running Rule 110 inside a SWMM5 model; Claude designed the hydraulic machine, wrote the generator, the readers and the tests, and found two side issues. No person had reviewed the essay or the hydraulic design when it was published.

**Claims worth keeping** (all copied from the file)
- A cell is a storage node of 1,000 ft2 that reads 1 when its depth is above a 2 ft read line. A pump at a flat 0.5 cfs writes it, stopped by a rule at 4 ft (4 ft x 1,000 ft2 / 0.5 cfs = 8,000 s); a 6 in orifice erases it. A day holds two generations in four 6-hour phases.
- Default run: Rule 110, 48 cells, 40 generations, 20.25 simulated days at a 60 s step: 1,968 cells read from the .out, 0 disagreements. Every 1 stood at 4.020 ft or more and every 0 at 0.0043 ft or less; routing continuity 0.000 %.
- Eight automata from seven rules (110, 30, 90, 108, 54, 150, 184) ran in native EPA SWMM 5.2.4 and in the browser build: all 10,700 cells matched in both, and the two engines' results were byte-identical in every case.
- Pump sweep: the write pump must lift at least 0.0926 cfs; at 0.09 cfs 513 of 1,968 cells are wrong, at 0.095 cfs none. Orifice sweep: at 0.1 ft diameter 342 cells are wrong.
- The infographic printed eight rule bits as 0 1 1 0 1 1 0 0, which is Rule 108, not Rule 110.
- Side findings: the bundled @bjorn3/browser_wasi_shim 0.4.2 grows files to their exact size on every write, and a twelve-line patch cut the default run from 14.4 s to 3.5 s with a byte-identical .out. Native Linux EPA SWMM 5.2.4 aborts with "buffer overflow detected" on a relative input path when fortify checks are on (getAbsolutePath in swmm5.c, realpath into a 260-byte buffer).
- 773 logic checks pass, including all 256 rules against an independent table and Rule 30's centre column against OEIS A051023.

**Limits it states.** Not a universal computer: the tape has at most 96 cells. No conduits, dynamic-wave momentum, surcharge or ponding: every link is a pump, an orifice or the one weir. One hydraulic design; only EPA SWMM 5.2.4 was run.

**Checked at ingest.** 2 ft x 1,000 ft2 / 21,600 s = 0.0926 cfs, the minimum the page gives. The fortify abort is the one the two-pipe run avoided with `-D_FORTIFY_SOURCE=0` [S204](S204-note-two-pipe-benchmark-step1-run.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://rule110-swmm5.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Rule 110 in SWMM5 (app)](../entities/rule110-swmm5.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Orifices](../concepts/orifices.md), [The SWMM findings register](../concepts/findings-register.md), [swmm5-kw](../entities/swmm5-kw.md).
