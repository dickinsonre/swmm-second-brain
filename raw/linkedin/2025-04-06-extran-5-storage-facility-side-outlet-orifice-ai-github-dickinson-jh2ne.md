---
title: "Extran 5 Storage Facility with Side Outlet Orifice for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/extran-5-storage-facility-side-outlet-orifice-ai-github-dickinson-jh2ne
created: "2025-01-19 22:05"
published: "2025-04-06 20:32"
words: 2185
export_sha256: e990516507a54f5ef7255a90dc615bb595a68b4ee2db94a46ca301e2e26ecde5
---
# Extran 5 Storage Facility with Side Outlet Orifice for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests

![Extran 5 Storage Facility with Side Outlet Orifice for AI, GitHub, used in SWMM5, ICM SWMM and InfoWorks and SWMM 3rd Party Tests](https://media.licdn.com/mediaD4E12AQH2gQJLw-BuuQ "Extran 5 Storage Facility with Side Outlet Orifice for AI, GitHub, used in SWMM5, ICM SWMM and InfoWorks and SWMM 3rd Party Tests")

**The SWMM3 or Extran3 Side Outlet Orifice Test File: A Historical Reference for Modern Hydraulic Modeling**

This is a story about one inp file. It shows the continuity in stormwater modeling from 1980 to 2025 onwards. It is about Example 5 from the 1981 Extran Manual. This compact test case, born in the era of punch cards, has validated SWMM across decades—from SWMM3 to SWMM5—and remains a benchmark in 2025. This article explores its history, mechanics, and enduring value for hydraulic engineers.

Why would you be interested in the file? You are a student of SWMM history, and this file has been important since 1981. You want to make a new version of SWMM and need a file from the past that you can compare. You are testing new versions of SWMM and wonder why some files are very small and what they mean.

### Origin and Purpose

This test file is an important benchmark in stormwater modeling development, originating in the 1981 EXTRAN 3 manual (CDM/CDM Smith). Its primary function was validating side outlet orifice hydraulics within network simulations. The reason for this blog or article is "Sed fugit interea, fugit irreparabile tempus" Or I wanted to document how I learned about this file and why it is still used today by the USEPA and many software vendors (Autodesk is one).

Why does this file matter? Example 5 has been a cornerstone file in SWMM’s development, ensuring continuity across versions. For example, in 1981, it and the Extran 3 manual showed the general mainframe user of SWMM3 how Extran worked. In 1988, it validated the SWMM3-to-SWMM4 transition; in 2006, it verified SWMM5 algorithms by comparing it to SWMM4. Now, it is part of the test suite for newer versions of SWMM5 and used by many vendors using the SWMM5 or part of the SWMM5 engine.

> **What is a Side Outlet Orifice?**

It is a link using an orifice equation for a circular or rectangular shape with an offset from the bottom of the sewer or storm link. Often used for diverting flows to another link. A side outlet orifice is critical in stormwater management because it allows controlled diversion of flow to prevent system overloading during heavy rainfall events. The precise calculation of flow through these orifices is essential for designing systems that can handle both routine drainage and extreme weather events. This makes it an excellent test case for hydraulic modeling software - if a program can accurately simulate the complex physics of side outlet orifices, it can likely handle many other hydraulic scenarios reliably.

![](https://media.licdn.com/dms/image/v2/D4E12AQFWI40EiRWGcQ/article-inline_image-shrink_1500_2232/B4EZYMuAeQHcAU-/0/1743970116109?e=1795651200&v=beta&t=umJRvVVdsVoZafdxGcG3PNTpMoN6DXBFzrm7Mocc9Gs)

What is a side outlet orifice?

### Development Continuity for SWMM using this file

The file served as a quality assurance test file throughout SWMM's evolutionary progression:

- SWMM3 → SWMM4 transition validation,\` 1981

- SWMM4 → SWMM5 algorithm verification, 1988

- Cross-platform computational consistency assessment - vendors

- Used currently by the USEPA as part of the suite of test files on GitHub and is part of most (all?) software vendors for SWMM5 and even SWMM4 (XPSWMM). It is also part of the QA/QC test files in the **2006** report STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

- It is also—and I just managed to notice this - a part of the download for the PDF as part of the [SWMM5 download](https://www.epa.gov/water-research/storm-water-management-model-swmm) These ZIP files, archived in 2006, contain test cases still used today, available via EPA’s GitHub

![](https://media.licdn.com/dms/image/v2/D4E12AQGyYXlud-Vopg/article-inline_image-shrink_1500_2232/B4EZYMfXKLHYAU-/0/1743966271069?e=1795651200&v=beta&t=EfOvtkRZAQufV9dLfyohfBSVPdmqg7PmP0TlGY48p_0)

STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

### Contemporary Applications in 2025

This test case has relevance across modern hydraulic modeling platforms:

- Implemented in InfoWorks ICM SWMM network daily build validation protocols, It is also used in Autodesk Water InfoDrainage software.

- Integrated into EPA's GitHub repository as a standardized test model

- Functions as a cross-platform verification instrument for hydraulic solver validation

> **Why it is Good**

This **Example 5 from the Extran Manual** was an excellent test model for SWMM back in the early 1980s precisely because it combined several challenging hydraulic elements (multiple inflows, an orifice, and dynamic wave routing) into a relatively compact network that could be run on what were then very limited computer resources (we used punch cards or terminals and a mainframe computer at UF). At the time, personal computers were not invented for SWMM3, and while they existed by the time of SWMM4, they were slow, and large-memory mainframes were not readily accessible to most modelers, so every model had to be small enough to fit into limited RAM and run in a feasible amount of CPU time. **Yet this example still demonstrated SWMM’s powerful capability to capture unsteady flow conditions—like surcharging, backwater effects, and control structures—in one integrated simulation.**

The inclusion of an orifice, various pipe shapes, and multiple inflow hydrographs showcased SWMM’s flexibility to handle both standard conveyance links and special hydraulic controls, confirming that dynamic wave routing could be effectively computed given the technology of the day. Overall, it illustrated that, despite modest hardware and software constraints, SWMM was already advanced enough to handle complex urban drainage systems, laying the groundwork for today’s much larger and more detailed models.

![](https://media.licdn.com/dms/image/v2/D4E12AQHTywFPnAFCmA/article-inline_image-shrink_1000_1488/B4EZVEkLAvH0AU-/0/1740612088528?e=1795651200&v=beta&t=6ptqCW6u_OnsZzEO1f_rZWa1bsJyZI0ORHS9a6S5HRU)

Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing

![](https://media.licdn.com/dms/image/v2/D4E12AQFDaAdi-1ucAA/article-inline_image-shrink_1500_2232/B4EZVEmrKFHMAY-/0/1740612744570?e=1795651200&v=beta&t=MEfD-1nNDCeUcBspQlRkowXbg7nVvx7_98I_kHRCTSY)

Storage Facility with Side Outlet Orifice or Extran 5

> **SWMM5 QA/QC Manual Compares these files to SWMM4 Results**

This rigorous validation ensured SWMM5’s reliability as it was rewritten C code based on the SWMM4 Fortran code.

\[embedded item\]

> **Extran 1981 Manual.** Beyond its technical value, the 1981 manual holds personal significance as my entry into Extran modeling.

\[embedded item\]

> **Summary of the Extran5.inp created with AI Help.**

Below is a detailed summary of the provided SWMM 5 input file titled "Example 5 of Extran Manual - Storage + Side Orifice." It focuses on a stormwater management model with storage units, a side orifice, and dynamic wave routing. The summary covers all key components and settings of the model.

**Detailed Summary of SWMM 5 Input File: "Example 5 of Extran Manual - Storage + Side Orifice"**

This SWMM 5 input file models a stormwater drainage system designed to demonstrate the use of storage units and side orifices for flow control, as outlined in "Example 5 of the Extran Manual." The simulation employs dynamic wave routing and includes inflows at multiple nodes, with comprehensive reporting for all system components. Example 5 models a storage unit and side orifice, testing dynamic wave routing combining an orifice and link.

------------------------------------------------------------------------

**1. Project Title and General Settings**

- **Title**: "Example 5 of Extran Manual - Storage + Side Orifice"

- **Simulation Period**:

- **Flow Units**: Cubic feet per second (CFS)

- **Infiltration Method**: Horton

- **Flow Routing**: Dynamic wave with a routing step of 20 seconds

- **Link Offsets**: Depth-based

- **Minimum Slope**: 0 (no minimum enforced)

- **Allow Ponding**: No

- **Skip Steady State**: No

- **Inertial Damping**: None

- **Normal Flow Limited**: Both upstream and downstream conditions

- **Reporting Step**: 15 minutes

- **Output File**: Results saved to "Extran5.txt" under "Outflows/Calibration"

------------------------------------------------------------------------

**2. Network Components**

- **Junctions**: 9 junctions representing connection points in the drainage network:

- **Outfalls**: 1 free outfall ("10208"):

- **Storage Units**: 1 functional storage unit ("82309"):

- **Conduits**: 9 conduits (pipes) connecting nodes:

- **Orifices**: 1 side orifice ("90010"):

------------------------------------------------------------------------

**3. Cross-Sectional Geometry**

- **Conduits**:

- **Orifice**:

------------------------------------------------------------------------

**4. Inflows**

- **Inflow Nodes**: Three nodes receive direct inflows via time series:

- **Time Series Pattern** (same for all three):

------------------------------------------------------------------------

**5. Evaporation**

- **Type**: Constant

- **Rate**: 0.0 (no evaporation)

- **Dry Only**: No

------------------------------------------------------------------------

**6. Reporting**

- **Options**:

------------------------------------------------------------------------

**7. Spatial Configuration**

- **Map Dimensions**: 0 to 10,000 in both X and Y directions (unitless)

- **Coordinates**: Provided for all nodes, e.g.:

- **Labels**:

------------------------------------------------------------------------

**8. Key Features and Observations**

- **Storage Unit**: "82309" is a large storage unit (max depth 40.5 ft) designed to detain stormwater, with flow regulated by the side orifice "90010."

- **Side Orifice**: "90010" controls outflow from the storage unit to junction "82308," with a 2-ft diameter and a discharge coefficient of 0.85.

- **Dynamic Wave Routing**: The 20-second routing step ensures accurate simulation of unsteady flow conditions.

- **Inflows**: Hydrographs simulate a stormwater event with peak flows occurring between 15 minutes and 3 hours.

- **No Pumps**: Despite the query mentioning pumps, this model does not include them; the focus is on passive storage and orifice control.

- **System Layout**: The network flows from higher-elevation junctions (e.g., "81009" at 128.2 ft) through conduits and storage to the outfall "10208" at 89.9 ft.

**Conclusion**

This SWMM 5 input file represents a stormwater drainage system designed to test storage and orifice functionality, as per "Example 5 of the Extran Manual." It features 9 junctions, 1 outfall, 1 storage unit, 9 conduits, and 1 side orifice, with inflows peaking at 40–50 CFS over an 8-hour simulation on January 1, 2002. The model uses dynamic wave routing for precision and provides detailed output for all components, making it a robust example of passive stormwater management without pumps.

> ** How does this look in ICM InfoWorks and ICM SWMM?**

You can import the Extran5.inp file into both ICM SWMM and ICM InfoWorks networks. For true fidelity you can also convert the ICM SWMM networks from the imported Extran5.inp file internally to an ICM InfoWorks network.

![](https://media.licdn.com/dms/image/v2/D5612AQHVXeu3Xp1G5Q/article-inline_image-shrink_1500_2232/B56ZVPR4WDGUAU-/0/1740791843219?e=1795651200&v=beta&t=PyJGkWGfYSDyCd67sAwPt1LfsBNbgumrcKDFkdejnKA)

Extran 5 Model in ICM InfoWorks and ICM SWMM

> Full Reference for the 1981 version of Extran for SWMM3

![](https://media.licdn.com/dms/image/v2/D4E12AQHyNnoz9jiWhA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1737324310714?e=1795651200&v=beta&t=IuAMab6PctzGVc-P86JoiIXe6W9wZWqfU5M6RzWjCSM)

Full Reference for the 1981 version of Extran for SWMM3

> ***Extran 5.inp File as an example for the future. This also reminds me of the original 1981 Extran manual which had both the inp files and model output in the printed pages.***

> ***What the input file looked like in 1981 in fixed format***

![](https://media.licdn.com/dms/image/v2/D5612AQErFEPrly8y4A/article-inline_image-shrink_1500_2232/B56ZVPkisoGoAU-/0/1740796734835?e=1795651200&v=beta&t=KJYfp_eIkOGKxtB4HGYAAHzKKdivEQGSNrdm3EuvzBw)

What the input file looked like in 1981 in fixed format

> **Closing Note**

This exploration of the Extran 5 Storage Facility with Side Outlet Orifice test file reveals more than just technical specifications—it documents a remarkable continuity in hydraulic modeling spanning over four decades. From punch cards to GitHub repositories, this compact test case has served as a critical benchmark through multiple generations of software and hardware evolution. What began as a simple example in a 1981 manual has become an enduring standard for hydraulic solver validation across platforms and vendors.

The longevity of this test file demonstrates both the fundamental soundness of SWMM's early hydraulic principles and the engineering community's commitment to maintaining computational consistency in modeling tools. As stormwater management faces increasingly complex challenges from climate change and urbanization, these foundational test cases provide the reliable bedrock upon which modern solutions can confidently build.

> **Terminology Note**

What is the the difference between EPA SWMM and Extran:

EPA SWMM (Storm Water Management Model) is a comprehensive computer model developed by the Environmental Protection Agency for planning, analysis, and design of stormwater runoff, combined sewers, sanitary sewers, and other drainage systems. It's a complete package that can simulate rainfall, runoff quantity and quality, and system hydraulics for both single events and continuous simulations.

Extran (Extended Transport) was specifically the hydraulic flow routing module within earlier versions of SWMM (particularly SWMM3 and SWMM4). It handled the complex hydraulic calculations needed to model dynamic wave flow routing through pipes, channels, and control structures. Extran was developed to solve the complete Saint-Venant equations for gradually varied unsteady flow, allowing it to model pressurized flow, backwater effects, flow reversal, and complex networks with various hydraulic structures like weirs, pumps, and orifices.

In modern versions of SWMM (SWMM5 and later), the Extran module's functionality has been integrated into the main program, but hydraulic professionals still sometimes reference "Extran" when discussing the dynamic wave routing capabilities of SWMM, particularly when referencing historic benchmarks like the example files you're discussing in your article.
