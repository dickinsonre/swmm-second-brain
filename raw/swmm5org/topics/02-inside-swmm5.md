Inside SWMM5

*How EPA SWMM 5.2.4 computes runoff, routing and everything between, one app at a time.*

Each app here opens one part of EPA SWMM 5.2.4: the source file, the equation and the numbers it produces. Many of them run the real engine, compiled to WebAssembly, in your browser.

The oldest posts here are from 2013, on the iterations inside every dynamic wave time step.

Start here

- [**Hydraulic Jump, Froude Number and \#INSIDE_SWMM5**](https://swmm5.org/2017/07/01/froude-number-and-inside_swmm5/). The Froude number and hydraulic jumps in SWMM5.

- [**Refactoring the SWMM 5 Help File: Routing**](https://swmm5.org/2019/01/20/refactoring-the-swmm-5-help-file-routing-in-swmm5/). Flow routing in SWMM5, explained topic by topic.

- [**Refactoring the SWMM 5 Help File: Hydrology**](https://swmm5.org/2019/01/20/refactoring-the-swmm-5-help-file-hydrology-in-swmm5/). Runoff, infiltration and the rest of SWMM5 hydrology.

- [**QA Report: Dynamic Wave Flow Routing, 2006**](https://swmm5.org/2025/01/18/markdown-version-of-the-storm-water-management-model-quality-assurance-report-dynamic-wave-flow-routing-2006/). EPA’s 2006 dynamic wave QA report, as markdown.

- [**Successive Under-Relaxation for the SWMM 5 Dynamic Wave Solution**](https://swmm5.org/2013/08/08/successive-under-relaxation-for-the-swmm-5-dynamic-wave-solution/). The iteration inside every dynamic wave step.

Try a tool

- [**Inside SWMM**](https://inside-swmm.netlify.app/). Inside the Node and Inside the Orifice & Weir: what happens inside a junction and a regulator.

- [**Dynamic Wave Midpoint Area**](https://swmm5-dw-midpoint-area.netlify.app/). How dynamic wave blends normal flow with the St. Venant terms, and what each Normal Flow Criterion option does.

- [**Cross-Section Explorer**](https://swmm5-xsection-explorer.netlify.app/). The built-in geometry tables behind every SWMM5 conduit shape.

More apps on this topic

- [**Slot-Free Pressurization**](https://slot-free-pressurization-swmm.netlify.app/). Surcharge handled without a Preissmann slot.

- [**Dynamic Wave Explainer**](https://swmm5-dynamic-waver-explainer.netlify.app/). Why SWMM5’s explicit dynamic wave solution stays robust.

- [**Lua SWMM5 Playground**](https://lua-swmm5-playground.netlify.app/). Drive the EPA SWMM 5.2.4 engine from Lua in your browser.

- [**SWMM5 .out Inspector Rover**](https://swmm5-out-inspector-rover.netlify.app/). Open a SWMM5 .out file and ask questions about it.

- [**The Bowl Is Full**](https://bowl-full-horton-cn-swmm5-sclark.netlify.app/). Soil compaction expressed as an apparent Curve Number.

- [**Topsoil Recovery Check**](https://topsoil-recovery-check.netlify.app/). Horton versus the LID two-layer soil for decompacted topsoil, in EPA SWMM 5.2.4.

- [**Fourier Cross Sections**](https://fourier-xsection-swmm5-swmm6.netlify.app/). Fit irregular cross sections with a Fourier series.

- [**Runoff Explorer**](https://swmmbobswmm6.github.io/swmm5-runoff-explorer/). How hydrographs respond to width, slope and imperviousness.

Work through an example

- [**Runoff Routing Options Example in SWMM 5**](https://swmm5.org/2013/08/05/runoff-routing-options-example-in-swmm-5/). The subarea routing options on one example.

- [**Example 5: Runoff Water Quality**](https://swmm5.org/2017/10/12/example-5-runoff-water-quality-for-swmm5-and-infoswmm-from-the-epa-applications-manual/). From the EPA Applications Manual.

- [**EPA SWMM regression models**](https://github.com/USEPA/swmm-nrtestsuite). EPA’s own test models.

Code and automation

- [**SWMMBobSWMM6/Stormwater-Management-Model**](https://github.com/SWMMBobSWMM6/Stormwater-Management-Model). My fork of EPA SWMM, with branches for new solvers and fixes (staggered grid, Preissmann box, node surface area, six Curve Number changes).

- [**SWMMBobSWMM6/swmm5-kw**](https://github.com/SWMMBobSWMM6/swmm5-kw). Kinematic wave and steady flow that split flow at junctions and route loops.

- [**SWMMBobSWMM6/swmm524-perched**](https://github.com/SWMMBobSWMM6/swmm524-perched). SWMM 5.2.4 with a perched two-layer soil.

- [**dickinsonre/alt-swmm5**](https://github.com/dickinsonre/alt-swmm5). A catalog of proposed SWMM5 engine features.

- [**dickinsonre/swmm-brain**](https://github.com/dickinsonre/swmm-brain). Engine changes, a WebAssembly build, and Ruby and PySWMM scripts.

- [**SWMM5 in other languages**](https://github.com/SWMMBobSWMM6/swmm5-cplus). C++ (swmm5-cplus), with Rust, Fortran, C#, Python, TypeScript, Java and Go versions in the same GitHub account.

Recently added

- [**Fixing EPA SWMM 5.2.4, One Proven Defect at a Time**](https://swmm5.org/2026/10/20/fixing-epa-swmm-524-one-proven-defect-at-a-time-hydrocouple-review/). October 2026.

- [**Topsoil Recovery Check**](https://topsoil-recovery-check.netlify.app/). October 2026.

- [**SWMM5 in other languages**](https://github.com/SWMMBobSWMM6). October 2026.

Explore the archive

- [**Inside SWMM5 posts**](https://swmm5.org/category/inside-swmm5/). Everything tagged Inside SWMM5.

- [**Hydraulics (older topic page)**](https://swmm5.org/topics/hydraulics/). Flow, surcharge, flooding and solver stability.

- [**Hydrology & RDII (older topic page)**](https://swmm5.org/topics/hydrology-rdii/). Rainfall, runoff, infiltration and wet-weather response.

- [**swmmfive.com**](https://www.swmmfive.com). My older blog, more than 2,000 posts.

Explore the six topics

- [SWMM History: SWMM1 to SWMM6](https://swmm5.org/topics/swmm-history/)

- **Inside SWMM5** (this page)

- [SWMM5 and ICM InfoWorks](https://swmm5.org/topics/swmm5-and-icm/)

- [ICM InfoWorks and SWMM6](https://swmm5.org/topics/icm-and-swmm6/)

- [Inside SWMM6](https://swmm5.org/topics/inside-swmm6/)

- [Comparing Models with AI](https://swmm5.org/topics/ai-model-comparison/)

[View all topics](https://swmm5.org/topics/) · [Subscribe to the newsletter](https://www.linkedin.com/newsletters/epaswmm5-related-software-7159940733972434944/)

*Use of AI: Claude (Anthropic) drafted this page in November 2026. It picked the entries from my swmm5.org posts, Netlify apps and GitHub repositories and wrote the one-line descriptions. I chose the six topics and the layout.*
