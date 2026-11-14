---
title: "SWMM6 Code House: Every Line of OpenSWMM 6 on a Wall"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/swmm6-code-house-every-line-openswmm-6-wall-robert-dickinson-ubs3e
created: "2026-11-04 18:10"
published: "2026-11-04 18:32"
words: 4427
export_sha256: 2676ed8d787ed0a8869c4169530e23e1d95565f7432cecef830a55e9de90d37a
---
# SWMM6 Code House: Every Line of OpenSWMM 6 on a Wall

![SWMM6 Code House: Every Line of OpenSWMM 6 on a Wall](https://media.licdn.com/mediaD4E12AQHIAraL3zTrMQ "SWMM6 Code House: Every Line of OpenSWMM 6 on a Wall")

*Companion to the SWMM6 Code House app. OpenSWMM 6.0.0-alpha.4, branch swmm6_rel, commit 9648837. A reading aid, not an OpenSWMM or USEPA release.*

Open the app: [swmm6-code-house.netlify.app](http://swmm6-code-house.netlify.app)

> **351,187 lines**

There is no such thing as a free hydrograph or link hydraulics plot. Somebody wrote every line that turned your rain into a number, and if you are going to sign your name under the number, you ought to know where those lines live.

OpenSWMM 6 is the successor engine to EPA SWMM 5, written in C++20 by the HydroCouple developers and still in alpha. It runs to 351,187 lines in 675 files. That is about seven times the SWMM 5.2.4 solver. Nobody reads that from the top. You need a map, and a map you can walk is easier to remember than a map you scroll.

So the code has been built into a house. You walk it as Froude, a water drop in rain boots. Each room holds the files that do one job, printed on the walls in full, and each door leads to the room that code calls.

> **What this is**

The SWMM6 Code House puts every line of the OpenSWMM engine source at commit 9648837, branch swmm6_rel, version 6.0.0-alpha.4, on walls you can read: 102 rooms on 9 floors, 6,683 functions, 427 doorways. Click a wall and the code opens in the reader. Press the question mark and the page tells you what that code does, from the code and its comments.

Understand what it is not. It is not an OpenSWMM release, it is not endorsed by HydroCouple or by USEPA, and it does not contain a compiled engine. It is a reading tool made by one engineer with an AI. The house opens a results file and displays it. It does not run a model.

*The screens in this document are version 1.1.0. A script took them from the standalone page in a headless browser with software graphics, so a real graphics card draws the house more smoothly.*

![](https://media.licdn.com/dms/image/v2/D4E12AQGjTqHtI9Csrw/article-inline_image-shrink_1500_2232/B4EaGnwolTIYAU-/0/1793815906981?e=1795651200&v=beta&t=zRQLlBw7DavWw0eP6fVxb7EZJ6r9gyLrAgV5_aZHRUI)

*The welcome screen. See what changed from SWMM 5, find a concept, or start walking.*

> **How the house is laid out**

Floors group related work. Height means nothing about execution order, and a floor is not a path for water. Room area follows line count, so a big room is a big job. The largest room is The Great Hall, with 13,652 lines.

The Front of the House holds the engine loop, the input reader, the reports and the plugin dock. The Pipe Gallery holds routing. The Surface Wing holds 2D. The Water Lab holds quality and heat. The Underground holds the subsurface. The Cellar holds the data stores and the math. The Public Counter is the C API and the SDK a program calls from outside.

![](https://media.licdn.com/dms/image/v2/D4E12AQFCHTvLZjSvLQ/article-inline_image-shrink_1000_1488/B4EaGnwwKmI8AM-/0/1793815937982?e=1795651200&v=beta&t=SStBDrX6sLurs6P31RhbtJ_kkew2CNe6IRThXAvGFg8)

*Lines of code on each floor. The Surface Wing holds the 2D solver, the largest new part of the engine.*

![](https://media.licdn.com/dms/image/v2/D4E12AQFwwQSj55wJkw/article-inline_image-shrink_1500_2232/B4EaGnwx8HIwAQ-/0/1793815945282?e=1795651200&v=beta&t=ikEYgfGhMRJlU6TBZYG0KxT-Ds-obQLuZIW0jl9EFKY)

*Inside the Finite Volume Hall. Froude stands with the code on the walls around him. The floor plan is at lower left, and the drawer on the right holds this room’s diagram.*

![](https://media.licdn.com/dms/image/v2/D4E12AQE3fhiSugyXOg/article-inline_image-shrink_1500_2232/B4EaGnwzs1KIAQ-/0/1793815952515?e=1795651200&v=beta&t=PeqNkQn2WdV7qSFYgRiH8jlgVTUCPQZas1m-_ELrNB4)

*Whole house view, with the nine floors pulled apart.*

> **Where the data went**

SWMM 5 keeps a Node struct for each node and a set of global arrays that any file can reach. It is simple, and it has a price: only one run can live in a process.

OpenSWMM moved the state of a run into one object, SimulationContext. The header calls it a central, reentrant simulation context, one per concurrent simulation, passed by reference to every solver function. Inside, a node is no longer a record. It is an index. Depth is ctx.nodes.depth\[i\] and head is a different array. A loop over depth walks one stretch of memory, which is the shape a vector unit wants. The Node Stores room lets you see it move.

The header comment in that file is worth your time. It maps each old global to its new home, line by line, and the Came from SWMM 5 links in each room are built from the same trail.

![](https://media.licdn.com/dms/image/v2/D4E12AQEB9MaRINMqyA/article-inline_image-shrink_1500_2232/B4EaGnw1E.KUAQ-/0/1793815958090?e=1795651200&v=beta&t=j4-fbNFLmLtITY4xR8oGr4DfS_PfEPsHIZjm1guLPS8)

*An array of structs against a structure of arrays. The picture shows the layout, not a measured speed.*

![](https://media.licdn.com/dms/image/v2/D4E12AQFRGx9hDaT3nw/article-inline_image-shrink_1500_2232/B4EaGnw2uyIIAU-/0/1793815964907?e=1795651200&v=beta&t=CrGwyThMnVNnPf0oG0IYgMFCIQVtI30bIP-3U1JXocg)

*The Read tab at SimulationContext, with the source in the middle and the names on each line explained at the side.*

> **What a run does**

A run is a state machine. EngineState runs CREATED, OPENED, INITIALIZED, RUNNING, ENDED, REPORTED, CLOSED, with ERROR_STATE beside them. Press Follow a run in the house and Froude walks that path, room by room.

One step is worth a second look. Output does not stop the solver any more. The main thread posts a snapshot to a bounded queue, eight items by default, and a separate IO thread writes it. If the writer falls behind, the post blocks, so the solver cannot outrun the disk without limit. The comment in IOThread.hpp notes the WebAssembly case writes synchronously, because there is no second thread to hand it to.

![](https://media.licdn.com/dms/image/v2/D4E12AQF3N6IW340V0Q/article-inline_image-shrink_1000_1488/B4EaGnw4JqIIAI-/0/1793815970685?e=1795651200&v=beta&t=l-RzZvMfjJNXwV4HDvfwUXzfKFAgsLOzdGgykFR99bQ)

*The engine states, as named in core/SimulationContext.hpp. A paused state exists and is marked for the future.*

> **Four ways to move water**

SWMM 5 modellers know three of these. The fourth is new. FV is an explicit conservative finite volume method, Godunov style with HLL or HLLC fluxes, and it lives in the Finite Volume Hall.

Explicit means there is no iteration to hide in. The step must obey its own speed limit or the answer blows up. In exchange, conservation is built in, cell by cell. That trade is the whole design, and nobody gets it for free.

![](https://media.licdn.com/dms/image/v2/D4E12AQFp73fYMd5YWQ/article-inline_image-shrink_1000_1488/B4EaGnw5j5IIAM-/0/1793815976479?e=1795651200&v=beta&t=ESIEC-ICDXXibPKmfb2wctrnWIAzYGCZqXC2DOeVjjQ)

*The RoutingModel enum in core/SimulationOptions.hpp. The numbers are the enum values.*

> **What is new**

Walk these rooms first if you know SWMM 5:

- The Surface Wing: 2D overland flow with local time stepping, and three choices of face flux.

- The Manhole Exchange: how a manhole and the street trade water.

- The Underground: soil columns, the subsurface solver and groundwater transport.

- The Richards Column: unsaturated flow through a LID soil layer.

- The Parcel Room and the Eulerian Room: LARD and ARD water quality, chosen by QUALITY_SOLVER, beside the legacy mixing.

- The Heat rooms in the Water Lab: temperature carried with the water.

- The Plugin Dock: input, output, report and state IO behind interfaces, with an SDK so others can add their own.

A warning on the Parcel Room. The enum comment says the Lagrangian solver is live for advection, mixing, dispersion, water age and first-order decay, and that reactions on segments, treatment interop and heat are not yet there, each behind a warning at open. Alpha means that. Read the comment before you believe a feature.

![](https://media.licdn.com/dms/image/v2/D4E12AQG_8NfMZo799Q/article-inline_image-shrink_1500_2232/B4EaGnw71HJkAU-/0/1793815985789?e=1795651200&v=beta&t=rDqOS_AmPlku4lnAEs0iSX6Q6YUSwSb36ZJIIgP3MZg)

*The diagram in the Marching Hall, one of the rooms new in OpenSWMM.*

> **Came from SWMM 5**

OpenSWMM did not start from a blank page. Comments in its source name 61 of the 76 SWMM 5 files, and each room whose comments do so shows a chip for that file. The chip opens the SWMM 5 file in the SWMM5 Code House, the sister app. You can read the old and the new side by side.

The Index tab has a table of each SWMM 5 file and the rooms that name it. The table comes from those comments. It is a reading aid. A name in a comment does not prove the logic moved unchanged.

> **Reading a results file**

The Results tab opens a binary .out file from either engine. Both write the same layout with the same magic number. The version word tells them apart, 60000 for OpenSWMM and 5xxxx for SWMM 5, and the panel shows it.

The rule here came from a review of another of Bob's apps, and it is a good one. A chart that plots a missing value as zero has told a lie, a small one, the kind that gets a pipe sized wrong. So each value here is one of five things. It is a number the file holds, or the panel says why not.

Give it a second .out and it overlays the two, report by report. It refuses if the IDs, the units, the report count or the report times differ, and it tells you which. Press Rank the largest events and it sorts every object by its highest saved value, and a click takes you there. A ranking of saved reports is not a ranking of what happened between them.

There is a trap in the node types. OpenSWMM's enum puts DIVIDER at 2 and STORAGE at 3. SWMM 5 has those two the other way round. The panel reads the code by the version word. A real file shows why that matters. baseline.out, in the OpenSWMM test data and written by 6.0.0-alpha.1, stores node ST1 as 3, and its own report calls ST1 storage. A reader built for SWMM 5 would call it a divider.

The sample here is a real OpenSWMM file: site_drainage_model.out from the OpenSWMM test data, written by 6.0.0-alpha.3. Three real files are tested, and a second reader written in Python, sharing no code with the page, holds the page to the numbers it finds. Those files came from earlier alphas than the source on the walls. Nothing here made them.

![](https://media.licdn.com/dms/image/v2/D4E12AQFWQX3qQyvl2w/article-inline_image-shrink_1000_1488/B4EaGnw9HEGwAM-/0/1793815991016?e=1795651200&v=beta&t=D1jH4qiOpeAMx663cxGB8_NSnCLLP13D2mmLhg2p2Ek)

*Missing is not zero. The Results panel keeps these cases apart.*

![](https://media.licdn.com/dms/image/v2/D4E12AQFD98Ll3aNwgQ/article-inline_image-shrink_1500_2232/B4EaGnw.v9H0AQ-/0/1793815997798?e=1795651200&v=beta&t=z0l_BOZdF5gzgXcFM1fxw3Uu5sbiicwKhj0gDim58KI)

*The Results tab with the sample file. It says which engine wrote the file, what the file can and cannot show, and which code stands behind each value.*

> **What a match does not prove**

Open an .inp beside your .out and the panel checks that the IDs and counts agree. If they do, the panel says the files can be read together. It does not say this .inp made this .out, because two scenarios of one model have the same IDs and different answers. Only a manifest with hashes written at run time could prove that, and neither engine writes one here.

![](https://media.licdn.com/dms/image/v2/D4E12AQE9hJPef4VKeA/article-inline_image-shrink_1000_1488/B4EaGnxAW_IIAI-/0/1793816004275?e=1795651200&v=beta&t=Hd07a7TyTH9DZFF8mT2XhMbs8K5yrNh_dMhOn5WsYTo)

*Compatibility is not provenance.*

> **What reading turned up**

Read a third of a million lines closely and you find things. 20 of them are written down in the Index tab and in the room where each one lives, every one with its line of code and its place. A script checks that each quoted line is really there.

Do not mistake these for bugs. Each is a source-reading hypothesis, an engineer saying that looks odd, go see. It stays a hypothesis until it has a minimal model, an actual engine run, an expected result and a difference somebody can repeat. The numbers quoted come from JavaScript copies, not from the engine, and some of what looks odd will turn out to be intended. Some is plainly inherited: three of them are the same in SWMM 5.2.4. One has been seen in a real file, the node type code, and it says so.

The four worth a look first:

- NetworkMeshBuilder.cpp line 456. The finite volume path gets K, M, C and Y and no form. HydClosureKernels.hpp then uses the power law for every culvert code, while dynamic wave sends Form 1 codes to a critical-depth solve (Culvert.cpp line 231). Drafting port, code 1, 4 ft pipe, slope 0.01, 2 ft head: 25.7 cfs against 183 cfs.

- NodeCoupling.cpp line 372. effectiveArea ramps from cp.area to twice cp.area over the 5 cm above the crown, and the flow gate six lines down opens over the same 5 cm. So nearly all exchange flow in the ORIFICE law runs at twice cp.area, and ORIFICE is the default law.

- InputReader.cpp line 265. A header that begins with a legacy word, such as \[JUNC\] or \[XSECT\], draws no unknown-section warning, because SWMM 5 reads those by prefix. The registry here matches whole tags, so no handler runs and the rows are dropped without a word. The comment at line 45 says the warning is left out on purpose. The dropped rows are the part worth a look.

- DynamicWave.cpp line 4419. SEMI_IMPLICIT. dV already holds the flows of the current iterate, and dy is applied from y_old, while the comment linearizes about the current estimate. The fixed point is then not A dy = dV. Drafting port, a toy chain of conduits: continuity -3.29 percent against +0.07 percent for EXPLICIT.

> **What this does not show**

Get this straight before you rely on it.

- No engine was compiled or run for this app. Nothing here shows OpenSWMM gives the right answer, or the same answer as SWMM 5.

- A diagram marked Port is a JavaScript copy of the C++ written by an AI. It was not compared with OpenSWMM. A diagram marked Picture computes nothing from a model.

- The call map is by name. C++ overloads, virtual calls and templates mean many calls cannot be resolved from text. The census resolved 26,223 calls and left 19,900 ambiguous. Those are counted and not drawn.

- The field meanings under the question mark resolve about 85 percent of field uses. The rest say so.

- The room plan and the comments come from the source at one commit of an alpha. It will move.

- No speed claim is made anywhere. The vector and layout rooms show arrangement, not timing.

- Sound and the 3D scene were tested in a headless browser with software graphics. Nobody has listened to it.

- No person has been tested with it, so nothing here shows that anybody learns from it.

![](https://media.licdn.com/dms/image/v2/D4E12AQH9JbDd30_b4w/article-inline_image-shrink_1000_1488/B4EaGnxBzsIEAI-/0/1793816010199?e=1795651200&v=beta&t=FwAdqChS5uVin6WzsQO7zLMUJswWTnLwYzdb05j9I5U)

*A text census sees what is written. A run would show what happens.*

![](https://media.licdn.com/dms/image/v2/D4E12AQE6Xe1JBc9QvQ/article-inline_image-shrink_1500_2232/B4EaGnxDXCJkAQ-/0/1793816016635?e=1795651200&v=beta&t=Vhjbqv8o_znbCz6OTQREioAoD1_fBM7oFA2UBUhEpz0)

*Read on a 390 pixel phone. The source gets the screen.*

> **How it was checked**

A passing test only covers what it tried. So the checks are sorted by what they can prove. The census tool throws if any file lands in no room or two rooms. The page tests open the delivered file, walk it, open every diagram, press every question mark and move every slider. The parser tests feed the Results panel empty, broken, truncated and partial files with known answers, and three real result files from the OpenSWMM test data.

The SWMM 5 tests in the sister app run a real engine. These cannot, and this document will not pretend otherwise.

![](https://media.licdn.com/dms/image/v2/D4E12AQHId_OGGHKpqg/article-inline_image-shrink_1000_1488/B4EaGnxFTbJoAI-/0/1793816024565?e=1795651200&v=beta&t=rwQ3b-61ucgpHcPdOMjPplzKGks3Ef6KGamnblUQQr0)

*Each kind of evidence covers its own ground. The last two boxes are empty on purpose.*

> **AI use**

Claude Code (Anthropic, model claude-opus-5-5) did the building. It wrote the census tools, the page, the essay, the diagrams and the tests, and read the C++ source to write them. Three of its subagents drafted room diagrams from the C++. Bob Dickinson chose the project, set the standards and reviews the result. Bob has not checked every sentence or formula, and no person has checked the diagrams line by line against the C++. The tests are also written by the same AI, so a passing test is weaker evidence than a person checking the work.

> **Credits**

OpenSWMM Engine, Copyright 2026 HydroCouple Developers, is licensed under the Apache License, Version 2.0. The source text shown on the walls comes from the swmm6_rel branch of Bob Dickinson's fork, SWMMBobSWMM6/openswmm.engine, commit 9648837. The text is unchanged and its copyright headers are intact. Tabs were expanded to four spaces. Portions of OpenSWMM derive from USEPA SWMM, which is in the public domain. USEPA and HydroCouple do not endorse this app. The full NOTICE and Apache-2.0 text are in the About tab and in the package.

Lead developer Caleb Buahin. Developer and documentation Corinne Wiesner-Friedman. House and page Copyright 2026 Robert Dickinson. three.js r128 draws the 3D scene.

![](https://media.licdn.com/dms/image/v2/D4E12AQFpHRkHeyt1bA/article-inline_image-shrink_1500_2232/B4EaGnxG8JGoAU-/0/1793816031304?e=1795651200&v=beta&t=Kt7Qc4Uaiq3UzAKHOdSeFdjPP__JfrSh_jzQ-m0yQMM)

*The About tab carries the upstream NOTICE in full and the Apache License.*

> **Sources**

- OpenSWMM engine: [github.com/HydroCouple/openswmm.engine](http://github.com/HydroCouple/openswmm.engine), branch swmm6_rel

- Fork read here: [github.com/SWMMBobSWMM6/openswmm.engine](http://github.com/SWMMBobSWMM6/openswmm.engine), commit 9648837fc23b88485196cb98dde1f070c70c5ca0

- EPA SWMM: [epa.gov/water-research/storm-water-management-model-swmm](http://epa.gov/water-research/storm-water-management-model-swmm)

> **Appendix: Walking Through 351,187 Lines of SWMM6**

Every line of the OpenSWMM 6 engine now sits on a wall of a house you can walk through, 351,187 lines in 102 rooms on nine floors. This virtual house of SWMM6 code was built from the OpenSWMM Engine code of the creative team of [Caleb Buahin](https://www.linkedin.com/in/calebbuahin/) and [Corinne Wiesner-Friedman, Ph.D.](https://www.linkedin.com/in/corinne-wiesner-friedman-ph-d-05736b45/) I posted links to the SWMM5 and SWMM6 houses on LinkedIn this week, and this newsletter is the longer story behind them.

OpenSWMM 6 is C++20, 675 files, about seven times the size of the SWMM 5.2.4 solver. Nobody reads that from the top. You need a map, and a map you can walk is easier to remember than a map you scroll.

The house holds OpenSWMM swmm6_rel at commit 9648837, version 6.0.0-alpha.4, and every wall was compared with its source file. Water comes in at the roof and falls through the house. The nine floors run from the Weather Loft through the Land Floor, the Front of the House (engine, context, input, output and plugins), the Public Counter (the C API that outside programs call), the Pipe Gallery, the Water Lab, the Surface Wing (2D overland flow) and the Underground, down to the Cellar.

> **Froude shows you around**

You walk both houses as Froude, a water drop in yellow rain boots with a headlamp. In the SWMM5 house one unit is one foot, Froude stands 1.2 feet tall, and if you hold Shift he goes supercritical on a real Froude number. A voice there tells you each room as you walk in (SWMM is said as “swim”).

Click a wall and the code opens in the reader. Press the question mark and the page tells you what that code does, from the code and its comments.

> **It started with SWMM5 on November 2**

On November 2 I asked Claude for a 3D house of the SWMM5 C code, with the code in the walls, interactive diagrams, doorways to connecting code rooms, and a water drop as the guide.

The first build put 51,080 lines of EPA SWMM 5.2.4 in 58 rooms on five floors. Room size comes from the code. link.c, at 2,692 lines, is a hall 26 feet on a side, and error.c, at 49 lines, is a closet. Nobody drew the doors by hand. A parser counted the calls from one file to another, and the doorways come from those counts.

Then I kept asking. I wanted a voice for each room, code big enough to read, a question mark on every diagram and more themes. I also asked what the principle was, since my other apps already run SWMM5 as a WebAssembly engine in the browser. Claude put the EPA SWMM 5.2.4 engine into the house. Twelve diagrams got a Run in the real engine button, and an Engine tab runs a sample model or your own .inp file. That engine matches stored native 5.2.4 output digit for digit on 75 of 78 test models, though its build record (the source commit, compiler and flags) is still missing.

I steered the rest with nine ChatGPT reviews. I attached each review and typed “add”, and Claude checked each claim against the C before changing a line. The SWMM5 house went from version 1.0 to 1.13. The grades in the chat climbed from 88 at version 1.7 to 95 at version 1.10, and then a tougher grader gave version 1.11 an 84.

While checking the diagrams, Claude found a possible defect in EPA’s culvert.c. For a Form 1 culvert the code runs the Ridder root finder and then returns the flow from its last trial, a midpoint, and not from the root.

Flow can jump by up to 2.29 cfs across 0.005 ft of head. Of 228 runs, 221 sit on the jagged curve within 0.01%. The likely fix is one more form1Eqn call at the root, but it exists only as a JavaScript copy and has not been compiled or tested on a real build.

> **Then the SWMM6 house**

On the evening of November 3 I asked for a SWMM6 Code House as a separate app. Same walk, different code. Every one of the 102 rooms has a diagram and a question mark, and 24 rooms have hand-made diagrams, each labeled Port or Picture. Three Claude subagents drafted room diagrams from the C++.

The Results tab opens a .out file. It never shows a missing value as zero, it ranks the largest events, and it compares two scenarios but refuses to compare files that do not match. Units can be the file’s own, US or SI.

The SWMM6 house does not run a model yet. It has no compiled engine, so it reads results and does not make them. It is a reading tool made by one engineer with an AI, and it is not an OpenSWMM release or endorsed by HydroCouple or USEPA.

> **Where the data went**

SWMM 5 keeps a Node struct for each node and a set of global arrays any file can reach, so only one run can live in a process. OpenSWMM moved the state of a run into one object, SimulationContext, one per concurrent simulation. A node is now an index. Depth is ctx.nodes.depth\[i\] and head is a different array, so a loop over depth walks one stretch of memory. The header comment for SimulationContext maps each old global to its new home, line by line.

Output no longer stops the solver. The main thread posts a snapshot to a bounded queue (eight items by default), and a separate IO thread writes it.

SWMM 5 modelers know three routing methods. The fourth, FV, is an explicit conservative finite volume method, Godunov style with HLL or HLLC fluxes, and it lives in the Finite Volume Hall.

While reading the C++ for the diagrams, Claude kept 20 reading notes, each with its line of code. None was confirmed by running anything. The numbers in them come from JavaScript copies, not from the engine. Some will turn out to be intended, and three are the same in SWMM 5.2.4. One is in plugins/DefaultOutputPlugin.cpp at line 451, which writes the node type to the .out file.

In OpenSWMM DIVIDER is 2 and STORAGE is 3. SWMM 5 has those two the other way round, so a reader written for SWMM 5 would swap them.

> **How this gets out the door**

I want every app to travel the road this one is on. Claude builds it, Netlify hosts it, a LinkedIn post points to it, a LinkedIn article and this newsletter tell the story, and at the core a [SWMM5.org](http://SWMM5.org) page holds it all, so someone can still find it in 2030.

The C on the SWMM5 walls is Lew Rossman’s, and the C++ on the SWMM6 walls comes from Caleb Buahin, Corinne Wiesner-Friedman and the OpenSWMM team. After 50 years with SWMM, I wish I had had a map like this. Some things are still open. No person has reviewed the lessons in the SWMM5 house, heard its sound or checked the diagrams line by line, so walk a room you know well and tell me what you find.

SWMM5 Code House: [swmm5-code-house.netlify.app](http://swmm5-code-house.netlify.app)

SWMM6 Code House: [swmm6-code-house.netlify.app](http://swmm6-code-house.netlify.app)

I built both houses with Claude (Anthropic). Claude wrote the code, the diagrams, the tests and the first draft of this article, and three Claude subagents drafted room diagrams for the SWMM6 house from the C++. I chose the project, set the standards and steered the SWMM5 house with nine ChatGPT reviews, and I review the results. I have not checked every sentence or formula, and the same AI that wrote the code wrote the tests.

\#SWMM \#OpenSWMM \#HydraulicModeling
