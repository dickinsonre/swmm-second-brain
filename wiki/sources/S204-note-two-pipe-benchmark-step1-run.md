---
title: "S204: Note, step 1 of the two-pipe benchmark: EPA SWMM 5.2.4 and swmm5-ruby (2026-11-17)"
type: source
raw: raw/notes/two-pipe-benchmark-step1-run-2026-11-17.md
kind: note
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-17
tags: [swmm5, icm, benchmark, verification, byte-for-byte, run-record, time]
drafted_by: Claude (Anthropic), from runs it made at Bob's request
reviewed: no
---
**What it is.** A run record, on the note template, for step 1 of the two-pipe benchmark designed in [S165](S165-note-epa-swmm-ruby-icm-benchmark.md): the model, the two engine builds, the commands, the gate result and the results on the 1-minute grid. Its status line reads "working". Raw file: [raw/notes/two-pipe-benchmark-step1-run-2026-11-17.md](../../raw/notes/two-pipe-benchmark-step1-run-2026-11-17.md).

**How it was written.** Its AI-use line: drafted by Claude (Anthropic) on 17 November 2026 "from runs Claude made at Bob Dickinson's request ("go")". Claude chose the routing options the design leaves open, wrote the model, built and ran both engines and read the results. "No person has rerun it." This is a run record, so its numbers are what the engines wrote; the choices of options are Claude's.

**Claims worth keeping**
- The options the design leaves open, as chosen: dynamic wave; a fixed 1 s routing step; EPA's defaults for inertial damping (PARTIAL), normal flow limit (BOTH), minimum surface area (12.566 ft2), trials (8) and head tolerance (0.005 ft); CFS; start 01/01/2026 00:00; a free outfall; junction rims 5 ft above invert. Variant B uses EPA's default step, 20 s with `VARIABLE_STEP 0.75`.
- Engines: EPA SWMM 5.2.4 from the copy vendored in swmm5-ruby's `ref/epa524`, identical to the v5.2.4 tag (commit 7952ca837988b1c32f791812eccc9fd64547e093), built by swmm5-ruby's `ref/Makefile` with gcc 13.3.0 at `-O2`, glibc 2.39, x86-64 with FMA and AVX2; swmm5-ruby at commit 0c979068bfc729f827ff1f03e787618d87bfa819 under Ruby 3.3.6.
- Gate: in both runs the `.out` files are byte-identical (10,990 bytes each) and the `.rpt` files identical apart from the three time lines; both engines exit 0.
- Fixed step: flow routing continuity error 0.000 %; 2.00 iterations per step on average; all links stable; maximum depths J1 0.44 ft, J2 0.43 ft, O1 0.41 ft at 00:20; C1 peaks at 0.99 cfs and 3.03 ft/s, C2 at 0.97 cfs and 3.07 ft/s; outfall maximum 0.97 cfs.
- On the 1-minute grid of the `.out`: outfall O1 peaks at 0.9665 cfs at minute 21 and J1 at 0.4356 ft at minute 20. The note lists every minute.
- Variant B: outfall peak 0.9691 cfs at minute 21, J1 0.4324 ft at minute 20; the largest differences from the 1 s run on the grid are 0.0329 cfs and 0.0223 ft.
- The 1-hour run writes 59 report records, minutes 1 to 59. With SWMM's own date routines, end minus start is 0.041666666664241347 days, 3599.9999997904524 s, floored to 3599 s by `project.c` line 165, so the 1:00 record is never written. Ending at 01:01:00 writes 60 records, minutes 1 to 59 unchanged, in both engines.
- Run times on one 2-core machine: EPA 0.014 s, Ruby 0.92 s (fixed step).

**Limits it states.** Nothing about ICM; steps 2 and 3 need ICM SWMM and ICM InfoWorks, and the acceptable differences for step 4 are not agreed. Byte-identical output shows the translation follows EPA's arithmetic, "including its quirks", not that either is right. Kinematic wave and steady flow were not run.

**Checked at ingest.** The inflow hydrograph holds 0.25 x 600 + 0.75 x 600 + 0.5 x 600 = 900 ft3, which is 0.0207 ac-ft, printed as 0.021. 900 ft3 x 7.48 gal/ft3 = 6,732 gallons, printed as 0.007 million gallons (the conversion factor is ours). The ICM user's first task on [Start here](../start-here.md) now has an expected result for step 1.

**Feeds:** [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [Run duration floored to whole seconds](../concepts/run-duration-floor.md), [SWMM5 language ports](../entities/swmm5-language-ports.md), [Start here](../start-here.md), [Open questions](../open-questions.md).
