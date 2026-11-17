---
title: "S188: Water Talks webinar, the ICM SIM engine and the ICM SWMM engine (2021, transcript)"
type: source
raw: raw/talks/water-talks-icm-sim-and-icm-swmm-engines-2021.md
kind: talk-transcript
author: Robert Dickinson and Nathan (Innovyze)
published: 2021-04-27
ingested: 2026-11-16
tags: [icm, swmm5, comparison, time-step, surcharge, history]
drafted_by: unknown; an automatic caption transcript of the spoken webinar
reviewed: no
---
**What it is.** A 62-minute Innovyze Water Talks webinar in which Bob compares the two 1D engines inside InfoWorks ICM: the ICM engine ("ICM SIM") and the EPA SWMM 5 engine that runs ICM SWMM networks. Nathan, an Innovyze systems engineer of six years, hosts and asks questions. Raw file: [raw/talks/water-talks-icm-sim-and-icm-swmm-engines-2021.md](../../raw/talks/water-talks-icm-sim-and-icm-swmm-engines-2021.md). Bob supplied the time-stamped transcript and the recording's link on 16 November 2026.

**How it was written.** Spoken, not written: the text is an automatic caption transcript, with time stamps. It garbles names and terms. Claude's readings of the garbled ones, used on the wiki pages: "pre-spin", "free SWMM four-point box" and "Prism box" are Preissmann; "XTRAN" is EXTRAN; "time step having" is halving; "so sure formula" is the Sjöberg formula; "Wallrus" is WALLRUS; "OneSwim" is One SWMM; "swim five" is SWMM 5; "3D parameters" is 2D parameters; "the CHI conference" is probably ICWMM. Everything in it is what the speakers said in 2021, from their experience and from screens the transcript does not show. No run file from the webinar is in this wiki.

**Date.** Not stated. The talk calls ICM 2021.3 the current version and SWMM 5.1.015 the current SWMM 5, with 5.2 still to come (09:21, 09:48); Innovyze was "recently acquired by Autodesk" (10:53). Three upcoming sessions follow, "next week", "the following week" and "finally May 18th" (03:04 to 03:57). If the series ran weekly, the talk was 27 April 2021; that is our inference, recorded as Q96.

**Claims worth keeping** (time stamps in the transcript)
- Bob's history as he gave it: "SWMM 3, SWMM 4, XP SWMM, SWMM 5 from 2001 to 2006. Been at Innovyze since the end of 2007" (01:48).
- The One SWMM engine is Innovyze's build of SWMM 5, used by ICM SWMM networks, InfoSWMM and InfoDrainage. At least 500 test files are run every night against EPA SWMM 5.1.015, with statistical comparisons of all nodes and links, to catch any change in answer. Bob imported about 100 of them into ICM SWMM networks and converted them to ICM networks for the comparisons (07:09 to 08:50, 11:50).
- ICM 2021.3 had 2D in ICM SWMM networks, using essentially the same 2D engine as ICM (09:21).
- ICM's lineage, as Bob gave it: "going back at least to the late '70s": WALLRUS, SPIDA, HydroWorks CS, "a few RS versions", then ICM "I guess since 2009" (10:22). ICM contains SWMM 5 water quality, SWMM 5 LIDs (called SUDS in ICM), SWMM 5 and SWMM 4 RDII, SWMM hydrology and SWMM infiltration; its Green-Ampt and modified Horton "is actually SWMM" (10:22 to 10:53).
- Autodesk SSA runs a modified SWMM 5 engine on top of AutoCAD Civil 3D (11:20).
- ICM has three 1D solutions, conduit, pressure and force main, which keep different terms of the St. Venant equations; pressure and force main drop the unsteady and nonlinear terms. ICM offers Manning or Colebrook-White, and converts a force main's Hazen-Williams to Manning "using the SWMM 5 equation" (13:43 to 14:53).
- SWMM 5 has no losses at nodes; its losses are in the links (entrance, exit and other, as K V²/2g). ICM "does not use a node continuity equation"; it computes a node head loss by one of six types (none, normal, high, fixed, user defined, FHWA), and its matrix solution ties that loss to the depths in the links on either side. "Fixed" uses the same values as SWMM 5 (15:47 to 19:15).
- SWMM 5 has one flow per link, at its midpoint, computed from the areas, hydraulic radii and widths at the two ends; Bob calls this "a big source of instability", with flow oscillating from one end to the other. ICM has at least five computational points per link, more on long links between a minimum and a maximum space step, with a Preissmann implicit scheme (17:00 to 17:53, 20:38, 23:44).
- In SWMM 5, break a long force main (his example: 5,000 ft) into three or four parts with intermediate nodes (20:06).
- Slot: SWMM 5 offers EXTRAN or SLOT; Bob prefers the slot and advises SLOT in SWMM 5 for any comparison with ICM. SWMM 5's slot width is 1 %, with the Sjöberg formula ("so sure formula" in the captions) as the pipe nears full; ICM sets it by a celerity ratio, where 14.4 gives 1 % and 20 gives 2 %. A SWMM 5 force main still uses the slot; an ICM force main does not (21:00 to 23:14). He says Lew Rossman added the slot "two years ago" (21:00).
- Time steps: ICM halves its step when a step does not converge and climbs back once it converges; SWMM 5 sets its step from the CFL condition and does not halve it; XP SWMM halves (24:43 to 25:29, 1:00:05).
- Inverted siphon example, started dry: ICM went down to 7.5 s while the siphon filled and then back to 60 s; SWMM 5 needed about 1 s and stayed at 1 to 2 s for the whole run. SWMM 5 was unstable at the start, with no continuity error, and did better with SLOT than with EXTRAN; flows "basically match", velocities differ more (29:33, 32:27 to 34:26, 35:31, 36:05).
- SWMM 5 is solved by Picard successive iteration, each node and link apart, normally four to eight iterations; ICM solves a matrix (29:00).
- Graphs: ICM shows only the upstream and downstream ends of a link, SWMM 5 the midpoint flow, so a graphical comparison sets an end against a midpoint; ICM can add point results along a link (26:28 to 27:29).
- Converting an ICM SWMM network to ICM renames the links, which breaks a graphical comparison; Bob resets the names with a SQL `SET` and keeps the originals in a user text field (30:52). Importing a SWMM 5 file now brings in its rainfall, inflows and patterns as ICM events, and an ICM run can be exported back to SWMM 5 with its time series (39:56, 43:37).
- Minimum depth and base flow: SWMM 5 keeps a minimum depth of 0.0001 ft; ICM keeps a base flow that the user can set, and starts every run from an initialization to a steady state, which Bob calls "a super hot start". For force mains in SWMM 5 he advises a hot start file (53:26 to 55:14, 59:21).
- When to use which (Nathan): ICM is generally faster and has more options for real-time control; some U.S. communities require EPA SWMM so that small consultants can work on the models (48:34 to 49:26). Bob: ICM is "a lot more robust", and in SWMM 5 "you need to sometimes play with the options and the time step" (50:55).
- An anecdote: the nightly One SWMM builds notify Bob's watch "three or four times" a night (08:09).

**What it does not hold.** No numbers from the comparison runs beyond the time steps above; the graphs were on screen.

**Feeds:** [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [InfoWorks ICM](../entities/infoworks-icm.md), [EPA SWMM 5](../entities/swmm-5.md), [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [Open questions](../open-questions.md) (Q01, Q13, Q29, Q96).
