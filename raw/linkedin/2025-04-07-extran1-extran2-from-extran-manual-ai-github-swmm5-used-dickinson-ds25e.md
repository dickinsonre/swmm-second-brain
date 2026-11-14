---
title: "Extran1 and Extran2 from the Extran Manual for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/extran1-extran2-from-extran-manual-ai-github-swmm5-used-dickinson-ds25e
created: "2025-04-07 12:47"
published: "2025-04-07 22:46"
words: 2433
export_sha256: fc077387fdac4a92c38e9b18e7b0822e7e651549fb2d719e53eef822c39ea0e2
---
# Extran1 and Extran2 from the Extran Manual for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests

![Extran1 and Extran2 from the Extran Manual for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests](https://media.licdn.com/mediaD4E12AQHZPBQ9W_i_Iw "Extran1 and Extran2 from the Extran Manual for AI, GitHub, SWMM5, used in ICM SWMM and InfoWorks and SWMM5 3rd Party Tests")

This is a story about two inp files. It shows the continuity in stormwater modeling from 1980 to 2025 onwards. It is about Extran1 (free outfall) and Extran 2 (fixed backwater with a tide gate) from the 1981 Extran Manual. This compact test case, born in the era of punch cards, has validated SWMM across decades—from SWMM3 to SWMM5—and remains a benchmark in 2025. This article explores its history, mechanics, and enduring value for hydraulic engineers.

Why would you be interested in the file? You are a student of SWMM history, and this file has been important since 1981. You want to make a new version of SWMM and need a file from the past that you can compare. You are testing new versions of SWMM and wonder why some files are very small and what they mean.

### Origin and Purpose

This test file is an important benchmark in stormwater modeling development, originating in the 1981 EXTRAN 3 manual (CDM/CDM Smith). Its primary function was validating side outlet orifice hydraulics within network simulations. The reason for this blog or article is "Sed fugit interea, fugit irreparabile tempus" or I wanted to document how I learned about this file and why it is still used today by the USEPA and many software vendors (Autodesk is one).

Why does this file matter? Extran1 and Extran2 have been cornerstone files in SWMM’s development, ensuring continuity across versions. I alone have run it hundreds of times for decades. For example, in 1981, it and the Extran 3 manual showed the general mainframe user of SWMM3 how Extran worked. In 1988, it validated the SWMM3-to-SWMM4 transition; in 2006, it verified SWMM5 algorithms by comparing it to SWMM4. Now, it is part of the test suite for newer versions of SWMM5 and used by many vendors using the SWMM5 or part of the SWMM5 engine.

> **What is a Tide Gate in SWMM5?**

In SWMM5 (Storm Water Management Model), a tide gate is a specialized hydraulic control feature typically implemented at an outfall to manage flow between a stormwater or sewer system and a receiving body of water, such as a river or ocean, where tidal influences are present. It is represented in the model as a gate associated with an outfall node, as seen in the "Example 2 of Extran Manual - Tide Gate" input file, where the outfall "10208" is defined with a fixed elevation of 89.9 ft, a stage of 94.4 ft, and a "YES" setting for the gated property. The tide gate allows outflow from the system when the water level upstream exceeds the downstream tidal level, preventing backflow into the system during high tide conditions. In the model, this is further supported by features like flap gates on conduits (e.g., conduit "1030" in the example), which act as one-way valves to enhance flow control.

![](https://media.licdn.com/dms/image/v2/D4E12AQG85FF1VScA9Q/article-inline_image-shrink_1500_2232/B4EZYSNp28GYAU-/0/1744062295358?e=1795651200&v=beta&t=JmGZP7jSLcex16IhJaUV_huMTEyGGzqusjV2GSP2YAE)

The tide gate allows outflow from the system when the water level upstream exceeds the downstream tidal level, preventing backflow into the system during high tide conditions.

### Development Continuity for SWMM using this file

The file served as a quality assurance test file throughout SWMM's evolutionary progression:

- SWMM3 → SWMM4 transition validation,\` 1981

- SWMM4 → SWMM5 algorithm verification, 1988

- Cross-platform computational consistency assessment - vendors

- Used currently by the USEPA as part of the suite of test files on GitHub and is part of most (all?) software vendors for SWMM5 and even SWMM4 (XPSWMM). It is also part of the QA/QC test files in the **2006** report STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

- It is also—and I just managed to notice this - a part of the download for the PDF as part of the [SWMM5 download](https://www.epa.gov/water-research/storm-water-management-model-swmm) These ZIP files, archived in 2006, contain test cases still used today, available via EPA’s GitHub

![](https://media.licdn.com/dms/image/v2/D4E12AQEtSlPGUsiGCg/article-inline_image-shrink_1500_2232/B4EZYQStMgGYAc-/0/1744030061876?e=1795651200&v=beta&t=C-nvUgd94NVE_jTAOt4WylwJa5-oYAsBX_lTs5_4QX8)

STORM WATER MANAGEMENT MODEL QUALITY ASSURANCE REPORT: Dynamic Wave Flow Routing By Lewis A. Rossman Water Supply and Water Resources Division National Risk Management Research Laboratory, Cincinnati, OH 45268

### Contemporary Applications in 2025

This test case has relevance across modern hydraulic modeling platforms:

- Implemented in InfoWorks ICM SWMM network daily build validation protocols, It is also used in Autodesk Water InfoDrainage software.

- Integrated into EPA's GitHub repository as a standardized test model

- Functions as a cross-platform verification instrument for hydraulic solver validation

> **Why it is Good**

**Extran1 and Extran2 from the Extran Manual** was an excellent test model for SWMM back in the early 1980s precisely because it combined several challenging hydraulic elements (multiple inflows, free outfall or a tide gate with fixed backwater, and dynamic wave routing) into a relatively compact network that could be run on what were then very limited computer resources (we used punch cards or terminals and a mainframe computer at UF). At the time, personal computers were not invented for SWMM3, and while they existed by the time of SWMM4, they were slow, and large-memory mainframes were not readily accessible to most modelers, so every model had to be small enough to fit into limited RAM and run in a feasible amount of CPU time. **Yet this example still demonstrated SWMM’s powerful capability to capture unsteady flow conditions—like surcharging, backwater effects, and control structures—in one integrated simulation.**

The inclusion of a free outfall or a tide gate, various pipe shapes, and multiple inflow hydrographs showcased SWMM’s flexibility to handle both standard conveyance links and special hydraulic controls, confirming that dynamic wave routing could be effectively computed given the technology of the day. Overall, it illustrated that, despite modest hardware and software constraints, SWMM was already advanced enough to handle complex urban drainage systems, laying the groundwork for today’s much larger and more detailed models.

![](https://media.licdn.com/dms/image/v2/D4E12AQF6LCnNDql0dg/article-inline_image-shrink_1500_2232/B4EZYQStMrHgAY-/0/1744030061751?e=1795651200&v=beta&t=yygVZVCf_2kQdIwbTdm9LkHjkdOnIJgQi-8P5BbnYE0)

Seven Classic SWMM5 Hydraulics Test Files from Extran3 in 1981 later used in SWMM4 and SWMM5 Testing

![](https://media.licdn.com/dms/image/v2/D4E12AQG3NCXwYWPckA/article-inline_image-shrink_1500_2232/B4EZYQStMiGgAU-/0/1744030062004?e=1795651200&v=beta&t=xHi9ef-ojjFif6bK3UYxydNcClqAe5fNy5oESR1g5m4)

Example 7 of Extran Manual - Type2 Pump

> **SWMM5 QA/QC Manual Compares these files to SWMM4 Results**

This rigorous validation ensured SWMM5’s reliability as it was rewritten C code based on the SWMM4 Fortran code.

\[embedded item\]

> **Extran 1981 Manual.** Beyond its technical value, the 1981 manual holds personal significance as my entry into Extran modeling.

\[embedded item\]

> **Summary of the Extran2.inp created with AI Help.**

The provided SWMM5 input file models a drainage system with a tide gate, based on Example 2 from the EXTRAN manual. Below is a detailed breakdown of its components and configuration:

\## Model Configuration

\- **Simulation period**: January 1, 2002 (00:00:00 to 08:00:00)

\- **Flow units**: CFS (cubic feet per second)

\- **Routing method**: Dynamic Wave (DYNWAVE) for pressurized pipe flow and backwater effects

\- **Infiltration method**: Horton equation

\- **Reporting interval**: 15 minutes

\## Network Components

**Junctions (9 nodes):**

\- Elevations range from 89.9 ft (outfall) to 128.2 ft (node 81009)

\- Example: Node 82309 has invert elevation 112.3 ft and max depth 42.7 ft

**Conduits (9 links):**

\- Lengths range from 300 ft to 5,100 ft

\- Roughness coefficients: 0.015-0.034 (Manning's n)

\- Example: Conduit 8040:

\- 1,800 ft long circular pipe (4 ft diameter)

\- Connects nodes 80408 (124.6 ft) to 80608 (118.3 ft)

**Special Elements:**

\- **Tide gate**: Outfall 10208 uses fixed stage (94.4 ft) with flap gate

\- **Trapezoidal channels**: Links 1030/1630 have 9ft base width and 3:1 side slopes

**Inflows:**

Three nodal hydrographs with triangular patterns:

\- Node 80408: 45 CFS peak (3-hour duration)

\- Node 81009: 50 CFS peak (3-hour duration)

\- Node 82309: 40 CFS peak (3-hour duration)

\## System Characteristics

\- **Tidal influence**: Fixed-stage outfall with anti-backflow gate

\- **Dynamic routing**: Accounts for pressure flow and surcharging

\- **Simplified hydrology**: Constant 0.0 evaporation rate (no ET losses)

\- **No water quality parameters**: Focused on hydraulic performance

This model is designed to test tide gate functionality under multiple inflow scenarios, using EXTRAN-based network configurations. The combination of circular pipes and trapezoidal channels with dynamic wave routing suggests an emphasis on accurate pressure/surcharge modeling\[1\]\[2\]\[7\].

Citations:

\[1\] [https://help2.innovyze.com/infoworksicm/Content/HTML/ICM_ILCM/SWMM5_Conversion_Notes%20(SWMM).htm](https://help2.innovyze.com/infoworksicm/Content/HTML/ICM_ILCM/SWMM5_Conversion_Notes%20(SWMM).htm)

\[2\] [https://www.openswmm.org/Topic/3400/swmm5-version-of-extran-examples](https://www.openswmm.org/Topic/3400/swmm5-version-of-extran-examples)

\[3\] [https://www.epa.gov/sites/default/files/2019-02/documents/epaswmm5_1_manual_master_8-2-15.pdf](https://www.epa.gov/sites/default/files/2019-02/documents/epaswmm5_1_manual_master_8-2-15.pdf)

\[4\] [https://www.openswmm.org/Topic/29958/understanding-swmm-summary-output](https://www.openswmm.org/Topic/29958/understanding-swmm-summary-output)

\[5\] [https://swmm5.org/2017/08/14/epa-swmm5-tutorial-with-images-for-swmm-5-1-012/](https://swmm5.org/2017/08/14/epa-swmm5-tutorial-with-images-for-swmm-5-1-012/)

\[6\] [https://swmm2000.com/forum/topics/swmm-5-example-files](https://swmm2000.com/forum/topics/swmm-5-example-files)

\[7\] [https://www.epa.gov/water-research/storm-water-management-model-swmm](https://www.epa.gov/water-research/storm-water-management-model-swmm)

\[8\] [https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10145M6.TXT](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10145M6.TXT)

\[9\] [https://www.openswmm.org/Topic/2636/swmm5-average-flow-time-patterns](https://www.openswmm.org/Topic/2636/swmm5-average-flow-time-patterns)

\[10\] [https://www.epa.gov/system/files/documents/2022-04/swmm-users-manual-version-5.2.pdf](https://www.epa.gov/system/files/documents/2022-04/swmm-users-manual-version-5.2.pdf)

\[11\] [https://swmm5.org/2016/09/07/how-do-you-interpret-the-flow-and-hydrology-summary-tables-in-swmm-5-1/](https://swmm5.org/2016/09/07/how-do-you-interpret-the-flow-and-hydrology-summary-tables-in-swmm-5-1/)

\[12\] [https://help.innovyze.com/space/infoswmm/17597955](https://help.innovyze.com/space/infoswmm/17597955)

\[13\] [https://downloads.tuflow.com/SWMM/SWMM5_Reference_Manual_Volume1_Hydrology_P100NYRA.pdf](https://downloads.tuflow.com/SWMM/SWMM5_Reference_Manual_Volume1_Hydrology_P100NYRA.pdf)

\[14\] [https://www.pcswmm.com/Downloads/USEPASWMM](https://www.pcswmm.com/Downloads/USEPASWMM)

\[15\] [https://www.swmm456.com/2024/04/the-two-main-reference-manuals-for.html](https://www.swmm456.com/2024/04/the-two-main-reference-manuals-for.html)

\[16\] [https://www.youtube.com/watch?v=H1XhSLI7-bM](https://www.youtube.com/watch?v=H1XhSLI7-bM)

\[17\] [https://www.openswmm.org/Topic/3994/swmm-5-applications-manual-now-available](https://www.openswmm.org/Topic/3994/swmm-5-applications-manual-now-available)

> ** How does this look in ICM InfoWorks and ICM SWMM?**

You can import the Extran5.inp file into both ICM SWMM and ICM InfoWorks networks. For true fidelity you can also convert the ICM SWMM networks from the imported Extran5.inp file internally to an ICM InfoWorks network.

![](https://media.licdn.com/dms/image/v2/D4E12AQERtdQSZmEOKA/article-inline_image-shrink_1500_2232/B4EZYSFkYeHkAU-/0/1744060173248?e=1795651200&v=beta&t=skO2rrwdYxuGttQ869UNrk3jdmaaOmlzbEc4xwjLUu0)

Extran1 (free outfall) and Extran 2 (fixed backwater with a tide gate) both in ICM SWMM networks and ICM InfoWorks Networks

> Full Reference for the 1981 version of Extran for SWMM3

![](https://media.licdn.com/dms/image/v2/D4E12AQEtJiMg-gx8KQ/article-inline_image-shrink_1500_2232/B4EZYQStMcHgAc-/0/1744030061850?e=1795651200&v=beta&t=NyNs3_CWBDBpKCkZuVvLvjGHIuwGT41E3wDDP75iV00)

Full Reference for the 1981 version of Extran for SWMM3

> ***Extran 6.inp File as an example for the future. This also reminds me of the original 1981 Extran manual which had both the inp files and model output in the printed pages.***

> ***What the input file looked like in 1981 in fixed format***

![](https://media.licdn.com/dms/image/v2/D4E12AQGr6ldtBU5AOQ/article-inline_image-shrink_1500_2232/B4EZYQStMaHgAY-/0/1744030061831?e=1795651200&v=beta&t=dRal2Zo8jiRV0r2xbHDqmQZTUkivQ94MiZqQwVAVKg8)

What the input file looked like in 1981 in fixed format

> **Closing Note**

These two files Extran1 (free outfall) and Extran 2 (fixed backwater with a tide gate) reveals more than just technical specifications—it documents a remarkable continuity in hydraulic modeling spanning over four decades. From punch cards to GitHub repositories, this compact test case has served as a critical benchmark through multiple generations of software and hardware evolution. What began as a simple example in a 1981 manual has become an enduring standard for hydraulic solver validation across platforms and vendors.

The longevity of this test file demonstrates both the fundamental soundness of SWMM's early hydraulic principles and the engineering community's commitment to maintaining computational consistency in modeling tools. As stormwater management faces increasingly complex challenges from climate change and urbanization, these foundational test cases provide the reliable bedrock upon which modern solutions can confidently build.

> **Terminology Note**

What is the difference between EPA SWMM and Extran?

EPA SWMM (Storm Water Management Model) is a comprehensive computer model developed by the Environmental Protection Agency for planning, analysis, and design of stormwater runoff, combined sewers, sanitary sewers, and other drainage systems. It's a complete package that can simulate rainfall, runoff quantity and quality, and system hydraulics for both single events and continuous simulations.

Extran (Extended Transport) was specifically the hydraulic flow routing module within earlier versions of SWMM (particularly SWMM3 and SWMM4). It handled the complex hydraulic calculations needed to model dynamic wave flow routing through pipes, channels, and control structures. Extran was developed to solve the complete Saint-Venant equations for gradually varied unsteady flow, allowing it to model pressurized flow, backwater effects, flow reversal, and complex networks with various hydraulic structures like weirs, pumps, and orifices.

In modern versions of SWMM (SWMM5 and later), the Extran module's functionality has been integrated into the main program, but hydraulic professionals still sometimes reference "Extran" when discussing the dynamic wave routing capabilities of SWMM, particularly when referencing historic benchmarks like the example files you're discussing in your article.
