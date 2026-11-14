---
title: "Edition 64 -- A Talking SWMM5 Out File Inspector Rover"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-64-talking-swmm5-out-file-inspector-rover-robert-dickinson-tcqpe
created: "2026-07-16 14:24"
published: "2026-07-16 19:01"
words: 532
export_sha256: 5ad4f8244a3754306a92c0d124ecde7598a093ca0e34d014852765c79325ee6b
---
# Edition 64 -- A Talking SWMM5 Out File Inspector Rover

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 64 -- A Talking SWMM5 Out File Inspector Rover](https://media.licdn.com/mediaD4E12AQGuJaPGYVgfNw "Edition 64 -- A Talking SWMM5 Out File Inspector Rover")

### Meet the SWMM5 Inspector Rover.

For years, every time a customer handed me a model, I did the same thing: open it up, hunt around through graphs, and guess where it's flooding, where it's unstable, and where the continuity error is eating the results and nobody's caught it yet. No system to it. Just hunting.

> **So I built a robot dog to do the hunting for me**.

The Rover loads your .inp, .rpt, and .out files straight in the browser and patrols the network node by node, conduit by conduit, flagging what it finds as it goes: severe, moderate, or advisory/OK. Run it against the demo model, Kestrel Creek (10 nodes, 9 conduits), and it turns up 16 findings, the worst one a flooding node at J3 under DYNWAVE routing.

![](https://media.licdn.com/dms/image/v2/D4E12AQGen6wKlPx4vQ/article-inline_image-shrink_1000_1488/B4EZ9rorb8HAAM-/0/1784217253861?e=1795651200&v=beta&t=Eaw1aTk3QAiVmh-t4R87nD3NKUs1elFTQmI0KuPaNOQ)

None of that is a guess. The parsers are checked against real SWMM 5.2.4 engine output, value for value, and the QA thresholds match what the engine itself expects: continuity error under 1% is good, over 5% needs a fix, velocity checks trip above 15 ft/s.

![](https://media.licdn.com/dms/image/v2/D4E12AQG2jOiHFPL-Sw/article-inline_image-shrink_1000_1488/B4EZ9ro9RcJUAM-/0/1784217326985?e=1795651200&v=beta&t=QGCZDhppq1XIuh8a8Yl6sy6iKF0mZPvqbcDFU8ReR6E)

> **Two ways I use it:**

📌 One model at a time, patrol mode animated, speed and dwell time both adjustable, every finding backed by report numbers, element data, and a time-series graph pulled straight from the .out.

![](https://media.licdn.com/dms/image/v2/D4E12AQFm9REkNrHERw/article-inline_image-shrink_1500_2232/B4EZ9roaRrIkAQ-/0/1784217183916?e=1795651200&v=beta&t=60BfTSMomjwJO_g04av_Vei8dnOdSPIl4ffWFHGHCNo)

> **You can load it from GitHub**

![](https://media.licdn.com/dms/image/v2/D4E12AQF59e3liemVJw/article-inline_image-shrink_1500_2232/B4EZ9sR5FNKIAU-/0/1784228057781?e=1795651200&v=beta&t=BgfAmtnA6nYL4ik0IhEGYh_rrA1Sm3JAXiYgE2VqmYc)

📌 A whole folder at once. I've got about four thousand SWMM models sitting in my GitHub, and the Rover pulls straight from there, hundreds of files in one pass. That's the part that's changed how I work. Load the folder, press Start Patrol, read the report.

![](https://media.licdn.com/dms/image/v2/D4E12AQEOyWFkszZe_w/article-inline_image-shrink_1500_2232/B4EZ9roULgIcAQ-/0/1784217158914?e=1795651200&v=beta&t=-9Fp_vGTVudSHKUTAreq7fHbtm3SulLRXEUU3MmGFJI)

![](https://media.licdn.com/dms/image/v2/D4E12AQGu6ONjl4MNIg/article-inline_image-shrink_1500_2232/B4EZ9sQyYEJgAU-/0/1784227768577?e=1795651200&v=beta&t=P0q7_KyYxzFfr4HM6gBhgjYvSBCZEEsgWYAwXrXLsME)

Single-file HTML. Nothing to install. Runs i the browser end to end, and the source is up on my GitHub gist if you want to see how it's built:

> **Links**

[https://gist.github.com/dickinsonre/9619008f7603e534cc663be48810d71e](https://gist.github.com/dickinsonre/9619008f7603e534cc663be48810d71e)

Try it: [https://swmm5-out-inspector-rover.netlify.app/](https://swmm5-out-inspector-rover.netlify.app/)

\#SWMM \#HydraulicModeling \#WaterEngineering \#VibeCoding
