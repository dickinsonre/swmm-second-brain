---
title: "Edition 63 -- SWMM5 Benchmark 3D Viewer for 4000 SWMM5 and SWMM6 Files"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-63-swmm5-benchmark-3d-viewer-4000-swmm6-files-dickinson-y20we
created: "2026-07-15 16:23"
published: "2026-07-15 17:33"
words: 1778
export_sha256: 84411eac36ba17ceb6bc8b0010054797bec3243bb69fac4e3a3f6be243f4e75d
---
# Edition 63 -- SWMM5 Benchmark 3D Viewer for 4000 SWMM5 and SWMM6 Files

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![](https://media.licdn.com/mediaD4E12AQEewKe8LZbUCw)

### SWMM5 Benchmark 3D Viewer Reads 4000 inp, rpt, and out files from GitHub, folders, and single files.

I first used a 3D view of an SWMM4 model in 1999 as part of CAiCE Software. We called it Visual Hydro, and we made it 1999. I’d joined CAiCE Software the year before, and we built a 3D view of an SWMM network running on VBA inside AutoCAD. Autodesk bought CAiCE in 2002, and the water tools, that 3D viewer included, didn’t survive the move. For trivia buffs, our main tool was Visual SWMM, which was basically XP-SWMM.

What I loved about it was the profile view. A 3D perspective shows the actual drop between high and low elevations and the real complexity of a network in a way a plan view never can. I missed that for 27 years.

This year I vibe-coded it back with Claude Fable: a 3D viewer for around 4,000 SWMM5 models. Load an .inp on its own, or add the .rpt and .out for results. It’s on my GitHub if you want to run your own model through it. Watch for the GIFs on LinkedIn. You can see the actual code on my Gists [https://gist.github.com/dickinsonre](https://gist.github.com/dickinsonre) and the 4000 models are at [https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030](https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030)

I built it as a small app on purpose. When I’m working a SWMM model, or looking at one in ICM, I drop it in and see the network in 3D without leaving what I’m doing.

The first 3D model I ever built, back at CAiCE in 1999, was Saw Mill Run in Pittsburgh. Uzair Shamsi had modeled that watershed in XP-SWMM and later SWMM4, and seeing it rendered in 3D for the first time, with all that relief and complexity in the terrain, was something else. Thank you. Sam, for getting me hooked on this.

Surveyed-transect geometry, animated storm playback, and every number verified against the SWMM 5.2.4 engine — in a single HTML file

[Open the live app →](https://swmm5-3d-viewer.netlify.app/) [swmm5-3d-viewer.netlify.app](http://swmm5-3d-viewer.netlify.app)

Source gist: [gist.github.com/dickinsonre](http://gist.github.com/dickinsonre)

> What it is

The SWMM5 Benchmark 3D Viewer turns the files a stormwater modeler already has — .inp geometry, .rpt summaries, and binary .out time series — into a 3D scene you can rotate, interrogate, animate, and export. It is one HTML file with no build step and no install, running Three.js from a CDN. It matters because most web viewers draw circles and call it a network. This one draws the hydraulics: junction shafts from invert to rim, conduits extruded in their true cross-section, surveyed irregular channels, a max-HGL ribbon, and a storm you can scrub through frame by frame.

The distinguishing rule of the project is simple: **no pixel renders before the math matches the engine.** Every geometry calculation the viewer performs was checked against EPA SWMM 5.2.4 output before it was allowed to draw anything.

![](https://media.licdn.com/dms/image/v2/D4E12AQGg6aHjzsJE2Q/article-inline_image-shrink_1500_2232/B4EZ9mxv_AKIAU-/0/1784135746027?e=1795651200&v=beta&t=0ty00btgopOALo0B9xRsafmm_XpWUBi6cWUxRaZVEKw)

> Why it exists

SWMM5 models are conventionally reviewed in plan view — boxes and arrows on a flat map. That view hides exactly the errors that cause the most trouble: a conduit with an absurd offset, two pipes crossing without a shared junction, an irregular channel whose surveyed section was pasted in wrong. In three dimensions, built from the model’s own inverts and depths and cross-sections, those problems announce themselves. The viewer was built to make model QA a matter of looking rather than squinting at tables, and to make results — the surcharge propagating through a network during a storm — something you can show a room rather than describe it.

![](https://media.licdn.com/dms/image/v2/D4E12AQEIYjk1s8pbiQ/article-inline_image-shrink_1500_2232/B4EZ9mx9rVHsAQ-/0/1784135801951?e=1795651200&v=beta&t=ud_LywCJYL4s_vHQyJQpf7YFi8vtZaA51pZ-pABPjZA)

> What it does

### Geometry and rendering

•     True cross-sections from \[XSECTIONS\]: egg, horseshoe, arch, box, trapezoid, ellipse, and IRREGULAR channels built from their surveyed \[TRANSECTS\] station-elevation data, so a floodplain looks like a floodplain.

•     Junction shafts drawn from \[JUNCTIONS\] invert plus max depth; pipes honor inlet/outlet offsets and diameters, positioned by \[COORDINATES\].

•     Subcatchment polygons from \[SUBCATCHMENTS\] + \[POLYGONS\], with filled, wireframe, and hidden modes.

•     Adjustable vertical exaggeration, pipe thickness, node and label sizing, depth fog, and a ground grid.

![](https://media.licdn.com/dms/image/v2/D4E12AQGMtJyhMeFvwA/article-inline_image-shrink_1500_2232/B4EZ9myQHKIcAU-/0/1784135877818?e=1795651200&v=beta&t=_Ooux3px7PX-r5-euXiAgk4sugJ6KuFkkd4Vfs7BzAQ)

> Results on the geometry

•     Load a .rpt for surcharge coloring and the max-HGL ribbon anchored to the 3D network.

•     Load a binary .out and scrub the storm on a playback timeline with live depth, velocity, and flooding colors, flood rings, and per-element hydrograph sparklines.

•     All 11 EXTRAN benchmark files carry SWMM 5.2.4 results bundled inside the app, so the timeline and Max HGL work the moment you pick a model — nothing to download.

![](https://media.licdn.com/dms/image/v2/D4E12AQHrm3B4DOTtTQ/article-inline_image-shrink_1000_1488/B4EZ9myalxJYAM-/0/1784135920377?e=1795651200&v=beta&t=flBeLfWEm37iDI4JSavw5qIfymxXEU7j5u_CVltN7pM)

> Loading a model set

•     Select .inp, .rpt, and .out together in one picker or one drop and the app pairs them by name; results are optional by design.

•     Upload a whole folder by button or by dragging it onto the app; multiple models route into a folder queue with previous/next navigation.

•     Browse any public GitHub repo of .inp files; clicking a model quietly fetches its same-name .rpt/.out siblings from the same folder.

> Analysis and export

•     Strahler stream-order coloring with a legend — network topology, not just pretty pipes.

•     Click or search any element to inspect its raw .inp parameters, with engine-verified transect statistics and a copy-as-JSON button for QA documentation.

•     PNG capture and animated GIF export up to HD, the GIF branded with the app name and model filename along the bottom edge.

![](https://media.licdn.com/dms/image/v2/D4E12AQF6Tr89KRT0hw/article-inline_image-shrink_1500_2232/B4EZ9mzWHEK4AQ-/0/1784136164063?e=1795651200&v=beta&t=PIr8zUwYcuG7cZZ6LSloxqA3b7YnNfWPQPReySv1rjs)

> The verification storyalysis and export

•     Strahler stream-order coloring with a legend — network topology, not just pretty pipes.

•     Click or search any element to inspect its raw .inp parameters, with engine-verified transect statistics and a copy-as-JSON button for QA documentation.

•     PNG capture and animated GIF export up to HD, the GIF branded with the app name and model filename along the bottom edge.

![](https://media.licdn.com/dms/image/v2/D4E12AQEUNM9cGqDnlQ/article-inline_image-shrink_1000_1488/B4EZ9mym.kJYAI-/0/1784135970941?e=1795651200&v=beta&t=70wDg5UhL4p0ccJdxsWyFg1Eo2TOQjpyZG4H5V8Xb8I)

> The verification story

Three chapters, each one a lesson about where truth lives in a modeling tool.

### Chapter 1 — Port the engine; do not paraphrase it

The irregular-channel geometry was not written from the manual or from memory. It is a line-for-line JavaScript port of the EPA engine’s transect.c. Both of the “reasonable interpretations” I tried first failed the numbers; only the literal port passed, and the source held surprises the documentation never mentions. The X1 card’s last value, named Yfactor in the code, is an elevation offset rather than a multiplier. The validate routine silently appends vertical wall stations at both ends of every transect. Panel conveyance multiplies by 1.486 while the hydraulic-radius back-solve divides by 1.49 — a 0.4 percent constant mismatch baked into SWMM since the beginning. Each wart was replicated deliberately.

The payoff, measured against the engine’s own Cross Section Summary across 45 irregular conduits in two models: full depth and full area match exactly on all 45, max width on 44, and effective hydraulic radius within 0.6 percent on 41. The four residuals are documented, within 2.4 percent, and do not affect the rendered shape, which comes straight from the exact station data.

### Chapter 2 — Eight reviewers, one pattern

The app was graded across eight rounds by five different AI models. Scores ran from an opening B− to a final A. The durable lesson was not any grade but a pattern: **counts survive verification; inferences do not.** One reviewer awarded an A while crediting three features that did not exist, including the transect parser, weeks before it was built. Two graded the error handling a D because a text scraper showed them a hidden error panel — built deliberately so failures would never be silent—and they read the smoke detector as the fire. Between them, those reviews recommended several features that had already shipped. The reviewers who actually clicked through the deployed app produced real findings the screenshot readers never could.

### Chapter 3 — A corpus of 1,729 core models and 4000 total models

The most valuable test was not a review. It was a corpus: thousands of real SWMM5 models accumulated over decades—EPA examples, the OWA suite, XPSWMM archives, and large NCIMM stress cases. Running 3,571 of them through the shipped parser found exactly one crash: a 275,000-element model that blew the JavaScript call stack through a spread-operator idiom no curated test would ever reach. After the fix, that model parses 91,270 nodes and 93,312 links in 1.9 seconds. Everything else parsed clean, most models in milliseconds. Scale found the bug that eloquence could not.

>  How to try it

•     Open [swmm5-3d-viewer.netlify.app](http://swmm5-3d-viewer.netlify.app) and pick any benchmark from the dropdown. The timeline and Max HGL light up on their own.

•     Drag your own .inp onto the page — alone, or together with its .rpt and .out. One drop loads the set.

•     Click GitHub, keep the default repo, open the Viewer-Demo-Results folder, and click user4.inp. A 288-timestep storm animation arrives over the wire with no file dialog anywhere.

> Links

Live app: [swmm5-3d-viewer.netlify.app](http://swmm5-3d-viewer.netlify.app)

Source gist: [gist.github.com/dickinsonre](http://gist.github.com/dickinsonre)

Model corpus with bundled results: [SWMMBobSWMM6/1729-SWMM5-Models-2030](https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030/tree/master/Viewer-Demo-Results)

Benchmark source: [OpenWaterAnalytics/swmm-nrtestsuite](https://github.com/OpenWaterAnalytics/swmm-nrtestsuite/tree/master/public/extran)
