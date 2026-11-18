# Step 1 of the two-pipe benchmark: EPA SWMM 5.2.4 and swmm5-ruby write the same bytes, and the run stops at 59 minutes

**Status:** working
**Date:** 2026-11-17

## The idea
Step 1 of the two-pipe benchmark (`epa-swmm-ruby-icm-benchmark.md`) runs one small model in EPA SWMM 5.2.4 and in the Ruby translation, swmm5-ruby, before anyone touches ICM. Both engines ran it on 17 November 2026. The `.out` files are byte-identical and the `.rpt` files differ only in the three time lines, which is the port's pass rule. The outfall peaks at 0.9665 cfs at minute 21 on the 1-minute grid, against an inflow peak of 1.0 cfs at minute 20. One surprise: the 1-hour run writes 59 report records, minutes 1 to 59, not 60. EPA's `project.c` floors the run length to whole seconds, and for this start date the product comes out at 3599.99999979 s, so the run ends at 3599 s and the 1:00 record is never written. Whoever lines ICM's results up with these needs to know that; ending the run at 01:01:00 gives a record at minute 60 and leaves minutes 1 to 59 unchanged.

## Proof / from scratch

**What the benchmark note leaves open, and what this run chose.** Dynamic wave routing; a fixed 1 s routing step (`VARIABLE_STEP 0`); EPA's defaults for inertial damping (PARTIAL), normal flow limit (BOTH), minimum surface area (12.566 ft2), trials (8) and head tolerance (0.005 ft); flow units CFS; start 01/01/2026 00:00; a free, ungated outfall; junction rims 5 ft above invert (`MaxDepth 5`), no ponding; the inflow is a SWMM time series, so values between the listed times are interpolated linearly. A second run, variant B, uses EPA's default step instead (20 s, `VARIABLE_STEP 0.75`).

**The model**, `two_pipe.inp`, SHA-256 a681e171e4af4228dc54e01004d9c484d8df7171062766c5c5bf5b879df55f5b:

```
[TITLE]
;;Project Title/Notes
Two-pipe benchmark (second brain S165), step 1: EPA SWMM 5.2.4 against swmm5-ruby

[OPTIONS]
;;Option             Value
FLOW_UNITS           CFS
INFILTRATION         HORTON
FLOW_ROUTING         DYNWAVE
LINK_OFFSETS         DEPTH
MIN_SLOPE            0
ALLOW_PONDING        NO
SKIP_STEADY_STATE    NO
START_DATE           01/01/2026
START_TIME           00:00:00
REPORT_START_DATE    01/01/2026
REPORT_START_TIME    00:00:00
END_DATE             01/01/2026
END_TIME             01:00:00
SWEEP_START          01/01
SWEEP_END            12/31
DRY_DAYS             0
REPORT_STEP          00:01:00
WET_STEP             00:05:00
DRY_STEP             01:00:00
ROUTING_STEP         1
RULE_STEP            00:00:00
INERTIAL_DAMPING     PARTIAL
NORMAL_FLOW_LIMITED  BOTH
FORCE_MAIN_EQUATION  H-W
VARIABLE_STEP        0
LENGTHENING_STEP     0
MIN_SURFAREA         12.566
MAX_TRIALS           8
HEAD_TOLERANCE       0.005
SYS_FLOW_TOL         5
LAT_FLOW_TOL         5
MINIMUM_STEP         0.5
THREADS              1

[JUNCTIONS]
;;Name  Elevation  MaxDepth  InitDepth  SurDepth  Aponded
J1      100        5         0          0         0
J2      99         5         0          0         0

[OUTFALLS]
;;Name  Elevation  Type  StageData  Gated
O1      98         FREE             NO

[CONDUITS]
;;Name  FromNode  ToNode  Length  Roughness  InOffset  OutOffset  InitFlow  MaxFlow
C1      J1        J2      200     0.013      0         0         0         0
C2      J2        O1      200     0.013      0         0         0         0

[XSECTIONS]
;;Link  Shape     Geom1  Geom2  Geom3  Geom4  Barrels  Culvert
C1      CIRCULAR  1      0      0      0      1
C2      CIRCULAR  1      0      0      0      1

[INFLOWS]
;;Node  Constituent  TimeSeries  Type  Mfactor  Sfactor  Baseline  Pattern
J1      FLOW         Q1          FLOW  1.0      1.0

[TIMESERIES]
;;Name  Time   Value
Q1      0:00   0.0
Q1      0:10   0.5
Q1      0:20   1.0
Q1      0:30   0.0
Q1      1:00   0.0

[REPORT]
;;Reporting Options
INPUT     NO
CONTROLS  NO
NODES     ALL
LINKS     ALL

[COORDINATES]
;;Node  X-Coord  Y-Coord
J1      0        0
J2      200      0
O1      400      0
```

Variant B is the same file with `ROUTING_STEP 20`, `VARIABLE_STEP 0.75` and a changed title (SHA-256 6c40db77fcf5874f02cedf1766e3b54160fd09cd61f1a79b2c3adaf743c6b301).

**The engines and the machine**
- EPA SWMM 5.2.4: the copy of the v5.2.4 source vendored in swmm5-ruby's `ref/epa524`, checked identical (`diff -rq`, no output) to USEPA/Stormwater-Management-Model at tag v5.2.4, commit 7952ca837988b1c32f791812eccc9fd64547e093. Built by swmm5-ruby's `ref/Makefile`: `gcc -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -Iepa524/solver -Iepa524/solver/include epa524/solver/*.c epa524/run/main.c -o runswmm -lm`. gcc 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1), glibc 2.39, x86-64 with FMA and AVX2. Binary SHA-256 1fc015f7890391a7595f1e504d6fe2713f79dcf32de08ed9a95406a2d7a2ebc5.
- swmm5-ruby: SWMMBobSWMM6/swmm5-ruby at commit 0c979068bfc729f827ff1f03e787618d87bfa819 (2026-11-08), run with ruby 3.3.6 (2024-11-05 revision 75015d4c1f) [x86_64-linux] at /usr/local/bin/ruby.
- That is the reference platform the port's README names.

**Commands**, each run in its own folder:

```
../swmm5-ruby/ref/runswmm  two_pipe.inp two_pipe.rpt two_pipe.out     # EPA
../swmm5-ruby/ruby/runswmm two_pipe.inp two_pipe.rpt two_pipe.out     # Ruby
cmp epa/two_pipe.out ruby/two_pipe.out
diff <(grep -v "Analysis begun on\|Analysis ended on\|Total elapsed time" epa/two_pipe.rpt) \
     <(grep -v "Analysis begun on\|Analysis ended on\|Total elapsed time" ruby/two_pipe.rpt)
```

**Gate result**

| Run | .out | .rpt | Exit codes |
|---|---|---|---|
| Fixed 1 s step | byte-identical, 10,990 bytes, SHA-256 330421777e10a6c0d47cda4348ee5136f309cb133064587612687495eb0cfe08 | identical apart from the three time lines (163 lines) | 0 and 0 |
| Variant B, 20 s variable | byte-identical, 10,990 bytes, SHA-256 2b075ed03d36e64178c34f053a307c585337a5973e24bf1851ccd02a44c267b8 | identical apart from the three time lines (175 lines) | 0 and 0 |

Run times on this 2-core machine: EPA 0.014 s, Ruby 0.92 s (fixed step); 0.005 s and 0.20 s (variant B). One run each.

**From the EPA report, fixed step**
- Flow routing continuity error 0.000 %. External inflow 0.021 ac-ft (0.007 million gallons), external outflow 0.021 ac-ft, no flooding.
- Routing step 1.00 s throughout; 2.00 iterations per step on average; all links stable; convergence at every step.
- Maximum depth: J1 0.44 ft, J2 0.43 ft, O1 0.41 ft, all at 00:20. No node surcharged or flooded.
- Maximum flow: C1 0.99 cfs at 3.03 ft/s, 0.39 of full flow, 0.43 of full depth; C2 0.97 cfs at 3.07 ft/s, 0.38 of full flow, 0.42 of full depth. Outfall O1 maximum 0.97 cfs, average 0.32 cfs, flowing 77.19 % of the time.
- Node flow balance errors: J1 -0.194 %, J2 0.203 %.

**From the .out, on the 1-minute grid** (values as stored, 32-bit). Outfall O1 peaks at 0.9665 cfs at minute 21; J1 peaks at 0.4356 ft at minute 20. The sum of the 59 outfall values times 60 s is 899.9 ft3; the inflow hydrograph holds 900 ft3 (150 + 450 + 300 ft3 over its three legs).

| Minute | Outfall O1 inflow (cfs) | J1 depth (ft) |
|---:|---:|---:|
| 1 | 0.0001 | 0.0524 |
| 2 | 0.0034 | 0.1126 |
| 3 | 0.0234 | 0.1574 |
| 4 | 0.0694 | 0.1872 |
| 5 | 0.1315 | 0.2095 |
| 6 | 0.1957 | 0.2291 |
| 7 | 0.2568 | 0.2475 |
| 8 | 0.3138 | 0.2652 |
| 9 | 0.3685 | 0.2822 |
| 10 | 0.4219 | 0.2985 |
| 11 | 0.4749 | 0.3140 |
| 12 | 0.5269 | 0.3290 |
| 13 | 0.5790 | 0.3435 |
| 14 | 0.6305 | 0.3575 |
| 15 | 0.6820 | 0.3712 |
| 16 | 0.7330 | 0.3846 |
| 17 | 0.7840 | 0.3977 |
| 18 | 0.8352 | 0.4105 |
| 19 | 0.8862 | 0.4231 |
| 20 | 0.9367 | 0.4356 |
| 21 | 0.9665 | 0.4225 |
| 22 | 0.9131 | 0.3982 |
| 23 | 0.8246 | 0.3723 |
| 24 | 0.7300 | 0.3450 |
| 25 | 0.6339 | 0.3164 |
| 26 | 0.5386 | 0.2858 |
| 27 | 0.4446 | 0.2524 |
| 28 | 0.3521 | 0.2152 |
| 29 | 0.2618 | 0.1719 |
| 30 | 0.1760 | 0.1171 |
| 31 | 0.1040 | 0.0731 |
| 32 | 0.0615 | 0.0515 |
| 33 | 0.0387 | 0.0389 |
| 34 | 0.0251 | 0.0308 |
| 35 | 0.0173 | 0.0252 |
| 36 | 0.0125 | 0.0212 |
| 37 | 0.0092 | 0.0182 |
| 38 | 0.0067 | 0.0157 |
| 39 | 0.0052 | 0.0137 |
| 40 | 0.0041 | 0.0120 |
| 41 | 0.0032 | 0.0105 |
| 42 | 0.0026 | 0.0093 |
| 43 | 0.0022 | 0.0082 |
| 44 | 0.0018 | 0.0073 |
| 45 | 0.0015 | 0.0064 |
| 46 | 0.0013 | 0.0056 |
| 47 | 0.0011 | 0.0050 |
| 48 | 0.0010 | 0.0044 |
| 49 | 0.0009 | 0.0038 |
| 50 | 0.0008 | 0.0034 |
| 51 | 0.0007 | 0.0030 |
| 52 | 0.0006 | 0.0027 |
| 53 | 0.0005 | 0.0024 |
| 54 | 0.0004 | 0.0022 |
| 55 | 0.0003 | 0.0020 |
| 56 | 0.0002 | 0.0018 |
| 57 | 0.0002 | 0.0016 |
| 58 | 0.0002 | 0.0015 |
| 59 | 0.0002 | 0.0013 |

**Variant B** (EPA's default step: 18.50 to 20.00 s, average 19.88 s, 2.01 iterations per step): continuity 0.000 %; outfall peak 0.9691 cfs at minute 21; J1 peak 0.4324 ft at minute 20. Against the 1 s run, the largest difference on the grid is 0.0329 cfs in outfall flow and 0.0223 ft in J1 depth.

**Why there are 59 records.** `src/solver/project.c` line 165, as it is in 5.2.4:

```c
        TotalDuration = floor((EndDateTime - StartDateTime) * SECperDAY);
```

Computed with SWMM's own `datetime.c` for this model: end minus start is 0.041666666664241347 days; times 86,400 that is 3599.9999997904524 s; the floor is 3599 s. The last report time, 3600 s, is never reached. Both engines do the same, which is why the bytes still match. Ending the run at 01:01:00 instead writes 60 records, minutes 1 to 60, with minutes 1 to 59 byte-for-byte the same values as the 1:00 run (checked in both engines; their `.out` files are byte-identical too); at minute 60 the outfall carries 0.0002 cfs and J1 0.0012 ft.

## What this does not show
- Nothing about ICM. Steps 2 and 3 of the benchmark need ICM SWMM and ICM InfoWorks, and the acceptable differences for step 4 have not been agreed.
- That either engine is right. Byte-identical output shows the translation follows EPA's arithmetic, including its quirks.
- Other routing choices. Kinematic wave and steady flow were not run.

## Links
- [The benchmark design](./epa-swmm-ruby-icm-benchmark.md): steps 1 to 4
- [swmm5-ruby](https://github.com/SWMMBobSWMM6/swmm5-ruby): the port, its README and the reference Makefile
- [EPA SWMM 5.2.4 source at v5.2.4](https://github.com/USEPA/Stormwater-Management-Model/tree/v5.2.4)
- [Run duration floored to whole seconds](../../wiki/concepts/run-duration-floor.md): the two earlier sightings of the 59-record cause

AI use: drafted by Claude (Anthropic) on 17 November 2026 from runs Claude made at Bob Dickinson's request ("go") in a Claude session. Claude chose the routing options the benchmark note leaves open, wrote the model, built and ran both engines, and read the results. No person has rerun it. The wording is Claude's until Bob rewrites it.
