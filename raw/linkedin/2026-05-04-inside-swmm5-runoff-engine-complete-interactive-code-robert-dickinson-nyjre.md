---
title: "Inside the SWMM5 Runoff Engine: A Complete Interactive Code Explorer"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/inside-swmm5-runoff-engine-complete-interactive-code-robert-dickinson-nyjre
created: "2026-04-30 23:41"
published: "2026-05-04 00:15"
words: 594
export_sha256: df40427e35d1dd864a63e03a2f51e72aa08f78c61fd61b20f12b8374fe97b8ec
---
# Inside the SWMM5 Runoff Engine: A Complete Interactive Code Explorer

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Inside the SWMM5 Runoff Engine: A Complete Interactive Explorer 5](https://media.licdn.com/mediaD5612AQHRKLG67Ue4Bw "Inside the SWMM5 Runoff Engine: A Complete Interactive Explorer 5")

I made an open-source app that shows you interactively how SWMM5 solves for subcatchment runoff. It shows you the code and has an interactive diagram showing how the code works. It is an HTML app and was made using Claude Code. The app code is on GitHub, and the app can be run from GitHub as a GitHub page. It shows you how the three‑surface runoff engine inside EPA SWMM 5. Whether you teach, model, or review stormwater systems, this tool lets you see exactly how SWMM5 turns rainfall into runoff, step by step.

------------------------------------------------------------------------

### 🧱 Three Surfaces, One Nonlinear Reservoir

SWMM5 splits every subcatchment into **three independent surfaces**:

- **A1 – Impervious, no depression storage** (rain → immediate runoff)

- **A2 – Impervious with depression storage** (rain fills storage first, then runoff)

- **A3 – Pervious** (rain minus infiltration and evaporation → runoff)

Each surface is a separate continuity equation solved by a **Cash-Karp 5th‑order Runge‑Kutta adaptive ODE solver**. The app visualizes the six stages (k₁…k₆) for each surface in real time, showing where the solver works hardest during a storm.

![](https://media.licdn.com/dms/image/v2/D4E12AQF7YBnE95W6Nw/article-inline_image-shrink_1500_2232/B4EZ3wRsCJIMAU-/0/1777852663416?e=1795651200&v=beta&t=Xu6OoFnOin1lJW3DAORmZtpV0cnudOs-cQYyADqt3cM)

------------------------------------------------------------------------

### 🧪 Interactive Simulation & Live Parameter Tuning

- Choose from **design storms** (SCS Types I, IA, II, III, Chicago, etc.) or drop your own hyetograph.

- Adjust every parameter — area, slope, width, Manning’s **n**, depression storage, infiltration (Horton, Green‑Ampt, SCS Curve Number) — and instantly see updated hydrographs, water balances, and peak flows.

- Watch the three outflow components separately, plus surface water depths and infiltration rates, all animated during playback.

![](https://media.licdn.com/dms/image/v2/D4E12AQGumAGf1J-Npg/article-inline_image-shrink_1500_2232/B4EZ3wR9mSGYAU-/0/1777852735350?e=1795651200&v=beta&t=wbDEcegGttiElWc6-1JV1XVohu4CuOLJ2Mv7ggQFQK4)

------------------------------------------------------------------------

### 📊 Validate Against Real SWMM5 Runs

The app isn’t just a toy. You can:

- **Export the model to a standard .INP file** and run it in EPA SWMM5.

- **Drop a real .RPT or .OUT file** onto the page to overlay the official engine’s results directly on the in‑browser simulation.

- Compare hydrographs, total runoff volumes, peak flows, and continuity errors side‑by‑side—instantly spotting differences due to solver nuances. mismatches

![](https://media.licdn.com/dms/image/v2/D4E12AQHUYIM1gZzqRw/article-inline_image-shrink_1500_2232/B4EZ3wSTr2IoAU-/0/1777852824929?e=1795651200&v=beta&t=VwzH_YhlJX-4kmOGhFVgXi5Yt1pcjp8zTr93Z4VU55U)

------------------------------------------------------------------------

### 🔗 Bonus: SWMM5 ↔ ICM InfoWorks Mapping

For engineers using both platforms, the app includes a **complete parameter crosswalk** and step‑by‑step guide to reproduce the same SWMM runoff engine inside InfoWorks ICM. A Ruby script automates the setup, making it a practical bridge for model conversions.

![](https://media.licdn.com/dms/image/v2/D4E12AQHidaeyjZqB6g/article-inline_image-shrink_1500_2232/B4EZ3wSi1aIoAU-/0/1777852886982?e=1795651200&v=beta&t=KF0-j-k0qKl-1r50ljFdJTWTiWm3d86JDQ3elhFV8vE)

------------------------------------------------------------------------

### 💡 Why It Matters

- **For modelers:** debug and trust your run-off results.

- **For reviewers:** see exactly what assumptions underlie a hydrograph.

- **For students and teachers:** a visual, live textbook of the SWMM5 runoff algorithm.

- **For ICM users:** avoid mismatch when switching between EPA SWMM and InfoWorks hydrology.

------------------------------------------------------------------------

### 🚀 Try It Yourself

The app runs entirely in your browser (no server, no login). 👉 [SWMM5 Runoff Explorer](https://swmmbobswmm6.github.io/swmm5-runoff-explorer/)

###
