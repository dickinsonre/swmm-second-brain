---
title: "Example 7 of Extran Manual - Type 2 Pump for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/example-7-extran-manual-type-2-pump-ai-github-swmm5-dickinson-pj38e
created: "2025-04-07 01:43"
published: "2025-04-07 12:12"
words: 2045
export_sha256: 61621ea5e1d7d3ddd7b7f0fb945401bfaca7e6739a8e114c0635fe50ad7ca58f
---
# Example 7 of Extran Manual - Type 2 Pump for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests

![Example 7 of Extran Manual in InfoWorks ICM InfoWorks Network and an ICM SWMM Network](https://media.licdn.com/mediaD4E12AQEWzPFs6Wuzmg "Example 7 of Extran Manual in InfoWorks ICM InfoWorks Network and an ICM SWMM Network")

**The SWMM3 or Extran3 Type 2 Pump Test File: A Historical Reference for Modern Hydraulic Modeling**

This is a story about one inp file. It shows the continuity in stormwater modeling from 1980 to 2025 onwards. It is about Example 7 from the 1981 Extran Manual. This compact test case, born in the era of punch cards, has validated SWMM across decades—from SWMM3 to SWMM5—and remains a benchmark in 2025. This article explores its history, mechanics, and enduring value for hydraulic engineers.

Why would you be interested in the file? You are a student of SWMM history, and this file has been important since 1981. You want to make a new version of SWMM and need a file from the past that you can compare. You are testing new versions of SWMM and wonder why some files are very small and what they mean.

### Origin and Purpose

This test file is an important benchmark in stormwater modeling development, originating in the 1981 EXTRAN 3 manual (CDM/CDM Smith). Its primary function was validating side outlet orifice hydraulics within network simulations. The reason for this blog or article is "Sed fugit interea, fugit irreparabile tempus" or I wanted to document how I learned about this file and why it is still used today by the USEPA and many software vendors (Autodesk is one).

Why does this file matter? Example 7 has been a cornerstone file in SWMM’s development, ensuring continuity across versions. For example, in 1981, it and the Extran 3 manual showed the general mainframe user of SWMM3 how Extran worked. In 1988, it validated the SWMM3-to-SWMM4 transition; in 2006, it verified SWMM5 algorithms by comparing it to SWMM4. Now, it is part of the test suite for newer versions of SWMM5 and used by many vendors using the SWMM5 or part of the SWMM5 engine.

> **What is a Type 2 Pump?**

An in-line pump where flow increases incrementally with inlet node depth.

![](https://media.licdn.com/dms/image/v2/D4E12AQFbAJDsKY7qEw/article-inline_image-shrink_1500_2232/B4EZYN9RENHUAU-/0/1743990892900?e=1795651200&v=beta&t=wV74xo5xS1AO02EqBC4el2ibuLuqS0m0b1NwFJpcBSU)

An in-line pump where flow increases incrementally with inlet node depth.

### Development Continuity for SWMM using this file

The file served as a quality assurance test file throughout SWMM's evolutionary progression:

- SWMM3 → SWMM4 transition validation,\` 1981

- SWMM4 → SWMM5 algorithm verification, 1988

- Cross-platform computational consistency assessment - vendors

- Used currently by the USEPA as part of the suite of test files on GitHub and is part of most (all?) software vendors for SWMM5 and even SWMM4 (XPSWMM). It is also part of the QA/QC test files in the **2006** report STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

- It is also—and I just managed to notice this - a part of the download for the PDF as part of the [SWMM5 download](https://www.epa.gov/water-research/storm-water-management-model-swmm) These ZIP files, archived in 2006, contain test cases still used today, available via EPA’s GitHub

![](https://media.licdn.com/dms/image/v2/D4E12AQFKJhfaYufGfg/article-inline_image-shrink_1500_2232/B4EZYN6pWXHMBE-/0/1743990200164?e=1795651200&v=beta&t=EBsCH-EMingp4lNlQJu0pun5nzRkUQxSJzb42fzvbX4)

STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

### Contemporary Applications in 2025

This test case has relevance across modern hydraulic modeling platforms:

- Implemented in InfoWorks ICM SWMM network daily build validation protocols, It is also used in Autodesk Water InfoDrainage software.

- Integrated into EPA's GitHub repository as a standardized test model

- Functions as a cross-platform verification instrument for hydraulic solver validation

> **Why it is Good**

This **Example 7 from the Extran Manual** was an excellent test model for SWMM back in the early 1980s precisely because it combined several challenging hydraulic elements (multiple inflows, a pump, and dynamic wave routing) into a relatively compact network that could be run on what were then very limited computer resources (we used punch cards or terminals and a mainframe computer at UF). At the time, personal computers were not invented for SWMM3, and while they existed by the time of SWMM4, they were slow, and large-memory mainframes were not readily accessible to most modelers, so every model had to be small enough to fit into limited RAM and run in a feasible amount of CPU time. **Yet this example still demonstrated SWMM’s powerful capability to capture unsteady flow conditions—like surcharging, backwater effects, and control structures—in one integrated simulation.**

The inclusion of a simple pump, various pipe shapes, and multiple inflow hydrographs showcased SWMM’s flexibility to handle both standard conveyance links and special hydraulic controls, confirming that dynamic wave routing could be effectively computed given the technology of the day. Overall, it illustrated that, despite modest hardware and software constraints, SWMM was already advanced enough to handle complex urban drainage systems, laying the groundwork for today’s much larger and more detailed models.

![](https://media.licdn.com/dms/image/v2/D4E12AQGYZ_BVSRSK8w/article-inline_image-shrink_1500_2232/B4EZYN6pWXHMAU-/0/1743990200086?e=1795651200&v=beta&t=7ixAbFkEtfZ9VcOsSCeN-xDzhSI-r9SKf04CrKpuUY4)

Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing

![](https://media.licdn.com/dms/image/v2/D4E12AQFBC_j2vgb-kA/article-inline_image-shrink_1500_2232/B4EZYN7RfIHcAY-/0/1743990365080?e=1795651200&v=beta&t=t0qFqkv5R_GAIRgVAaCmgzViysV_EK6DE9VjiNHetA4)

Example 7 of Extran Manual - Type2 Pump

> **SWMM5 QA/QC Manual Compares these files to SWMM4 Results**

This rigorous validation ensured SWMM5’s reliability as it was rewritten C code based on the SWMM4 Fortran code.

\[embedded item\]

> **Extran 1981 Manual.** Beyond its technical value, the 1981 manual holds personal significance as my entry into Extran modeling.

\[embedded item\]

> **Summary of the Extran6.inp created with AI Help.**

Below is a concise summary of the SWMM5 input file titled "Example 7 of Extran Manual - Type 2 Pump." This summary highlights the key components, settings, and functionality of the stormwater management model, focusing on its structure, pump operation, and simulation details.

------------------------------------------------------------------------

Summary of SWMM5 Input File: "Example 7 of Extran Manual - Type 2 Pump"

**Overview**: This SWMM5 input file models a stormwater drainage system from "Example 7 of the Extran Manual," featuring a Type 2 pump (in-line pump) to manage flows. The simulation runs for 8 hours on January 1, 2002, using dynamic wave routing to test pump performance under controlled inflow conditions, with no additional control rules beyond the pump curve.

**General Settings**:

- **Title**: "Example 7 of Extran Manual - Type 2 Pump"

- **Flow Units**: Cubic feet per second (CFS)

- **Simulation Period**: January 1, 2002, 00:00 to 08:00

- **Routing**: Dynamic wave with a 20-second time step

- **Report Step**: 15 minutes, output saved to "Extran7.txt"

- **Infiltration**: Horton method; no evaporation or ponding allowed

- **Normal Flow**: Limited by both upstream and downstream conditions

**Network Components**:

- **Junctions**: 9 nodes (e.g., 80408 at 124.6 ft elevation, 82309 at 112.3 ft)

- **Outfall**: 1 free outfall (10208 at 89.9 ft elevation)

- **Conduits**: 9 pipes, varying in shape (circular 4-6 ft, trapezoidal 9 ft base), lengths (300-5100 ft), and roughness (0.015-0.034)

- **Pump**: 1 in-line pump (90010) from node 82309 to 15009, governed by "Curve1" (e.g., 8 ft head = 5 CFS, 100 ft = 20 CFS)

**Inflows**:

- **Nodes**: Three inflow points (80408, 81009, 82309)

- **Time Series**: Identical hydrographs peaking at 45-50 CFS from 15 minutes to 3 hours, then dropping to 0 CFS

- **Pattern**: Simulates a short, intense storm event

**Pump Operation**:

- **Type**: Type 2 (in-line pump), operating continuously based on head-discharge curve "Curve1"

- **Curve Details**: Pump capacity increases with head (5 CFS at 8 ft, 10 CFS at 25 ft, 20 CFS at 100 ft)

- **No Control Rules**: Unlike Example 6, pump operation relies solely on the curve, with no dynamic adjustments

**Spatial Configuration**:

- **Map**: Grid spans -1113 to 10650 (X) and 2165 to 7792 (Y), unitless

- **Coordinates**: Nodes range from -578.95 (10208) to 10115.79 (80408) in X, 2421.05 to 7536.84 in Y

**Key Features**:

- **Pump Focus**: Tests a Type 2 in-line pump’s performance within the conduit network, contrasting with Example 6’s off-line pump.

- **Dynamic Routing**: 20-second step ensures accurate simulation of unsteady flows (e.g., surcharging, backwater).

- **Simplicity**: Lacks additional control rules, focusing on pump curve-driven flow management.

- **Network Layout**: Flows converge at 82309, where the pump regulates discharge to 15009, then to the outfall.

**Conclusion**: This model simulates a stormwater system with an in-line pump managing flows from three inflows peaking at 45-50 CFS, routed through a network of conduits to a single outfall. It showcases SWMM5’s capability to handle a Type 2 pump under dynamic conditions, serving as a straightforward test case for pump-driven hydraulic modeling.

> ** How does this look in ICM InfoWorks and ICM SWMM?**

You can import the Extran5.inp file into both ICM SWMM and ICM InfoWorks networks. For true fidelity you can also convert the ICM SWMM networks from the imported Extran5.inp file internally to an ICM InfoWorks network.

![](https://media.licdn.com/dms/image/v2/D4E12AQGVLx_Y7m8pDg/article-inline_image-shrink_1500_2232/B4EZYN6pWXHgAU-/0/1743990201155?e=1795651200&v=beta&t=yh5nUlfZIH4dlWMM91EmDbYrWymZQeEoxsejHSKpisU)

Extran 6 Model in ICM InfoWorks and ICM SWMM

> Full Reference for the 1981 version of Extran for SWMM3

![](https://media.licdn.com/dms/image/v2/D4E12AQFd1_wRWl19ig/article-inline_image-shrink_1500_2232/B4EZYN6pWTHgAU-/0/1743990200105?e=1795651200&v=beta&t=t-dsJG5mrAyuaEuQrk7zX-jWC2k1w8LyU39KSdBH4_s)

Full Reference for the 1981 version of Extran for SWMM3

> ***Extran 6.inp File as an example for the future. This also reminds me of the original 1981 Extran manual which had both the inp files and model output in the printed pages.***

> ***What the input file looked like in 1981 in fixed format***

![](https://media.licdn.com/dms/image/v2/D4E12AQEwz2tuhGHlNg/article-inline_image-shrink_1500_2232/B4EZYN6pWRHgAU-/0/1743990200079?e=1795651200&v=beta&t=13uhffks89TX0IMv6hRoIjd6H23VbBus5-0ZyA_DcfY)

What the input file looked like in 1981 in fixed format

> **Closing Note**

This exploration of Example 7 of the Extran Manual - Type 2 Pump Test file reveals more than just technical specifications—it documents a remarkable continuity in hydraulic modeling spanning over four decades. From punch cards to GitHub repositories, this compact test case has served as a critical benchmark through multiple generations of software and hardware evolution. What began as a simple example in a 1981 manual has become an enduring standard for hydraulic solver validation across platforms and vendors.

The longevity of this test file demonstrates both the fundamental soundness of SWMM's early hydraulic principles and the engineering community's commitment to maintaining computational consistency in modeling tools. As stormwater management faces increasingly complex challenges from climate change and urbanization, these foundational test cases provide the reliable bedrock upon which modern solutions can confidently build.

> **Terminology Note**

What is the the difference between EPA SWMM and Extran:

EPA SWMM (Storm Water Management Model) is a comprehensive computer model developed by the Environmental Protection Agency for planning, analysis, and design of stormwater runoff, combined sewers, sanitary sewers, and other drainage systems. It's a complete package that can simulate rainfall, runoff quantity and quality, and system hydraulics for both single events and continuous simulations.

Extran (Extended Transport) was specifically the hydraulic flow routing module within earlier versions of SWMM (particularly SWMM3 and SWMM4). It handled the complex hydraulic calculations needed to model dynamic wave flow routing through pipes, channels, and control structures. Extran was developed to solve the complete Saint-Venant equations for gradually varied unsteady flow, allowing it to model pressurized flow, backwater effects, flow reversal, and complex networks with various hydraulic structures like weirs, pumps, and orifices.

In modern versions of SWMM (SWMM5 and later), the Extran module's functionality has been integrated into the main program, but hydraulic professionals still sometimes reference "Extran" when discussing the dynamic wave routing capabilities of SWMM, particularly when referencing historic benchmarks like the example files you're discussing in your article.
