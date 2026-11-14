---
title: "SWMM3 Weir Extran4 Test File for AI, GitHub, SWMM5, ICM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/swmm3-weir-extran4-test-file-ai-github-swmm5-icm-robert-dickinson-s0u9e
created: "2025-01-11 11:19"
published: "2025-01-19 21:55"
words: 1075
export_sha256: 3c7d5c18a435a99febe1c2baa113f69a1d445be9735db0219da43ff1a1a63f56
---
# SWMM3 Weir Extran4 Test File for AI, GitHub, SWMM5, ICM

![SWMM3 Weir Extran4 Test File for AI, GitHub, SWMM5, ICM](https://media.licdn.com/mediaD4E12AQHF9Opy37z11w "SWMM3 Weir Extran4 Test File for AI, GitHub, SWMM5, ICM")

**The SWMM3 Weir Test File: A Historical Reference for Modern Hydraulic Modeling**

This test file holds special historical significance in the development of stormwater modeling. Originally published in the 1981 EXTRAN 3 manual by CDM (now CDM Smith), it was specifically designed to validate orifice calculations in hydraulic networks. The file served as a critical quality assurance tool during the evolution of SWMM, supporting the transition from SWMM3 through SWMM4 and into the current SWMM5.

I documented this file's importance in a 2009 Posthaven blog post, which I have updated using various AI tools to maintain its relevance. Today, this historical test case continues to prove valuable across multiple modern modeling platforms, such as ICM SWMM—as an example. It is also on the EPA GitHub as a test model.

This **Example 4 from the Extran Manual** was an excellent test model for SWMM back in the early 1980s precisely because it combined several challenging hydraulic elements (multiple inflows, a weir, dynamic wave routing) into a relatively compact network that could be run on what were then very limited computer resources (we used punch cards or terminals and a mainframe computer at UF). At the time, personal computers were not invented for SWMM3, and while they existed by the time of SWMM4, they were slow, and large‐memory mainframes were not readily accessible to most modelers, so every model had to be small enough to fit into limited RAM and run in a feasible amount of CPU time. **Yet this example still demonstrated SWMM’s powerful capability to capture unsteady flow conditions—like surcharging, backwater effects, and control structures—in one integrated simulation.** The inclusion of a weir, various pipe shapes, and multiple inflow hydrographs showcased SWMM’s flexibility to handle both standard conveyance links and special hydraulic controls, confirming that dynamic wave routing could be effectively computed given the technology of the day. Overall, it illustrated that, despite modest hardware and software constraints, SWMM was already advanced enough to handle complex urban drainage systems, laying the groundwork for today’s much larger and more detailed models.

**Yet this example still demonstrated SWMM’s powerful capability to capture unsteady flow conditions—like surcharging, backwater effects, and control structures—in one integrated simulation.**

> **Example Real-Time Control (RTC) rule for a Weir in SWMM5**

**Explanation of Components:**

1.  RULE Orifice1:

2.  IF SIMULATION CLOCKTIME \>= 01:00:00:

3.  AND SIMULATION CLOCKTIME \<= 2:00:00:

4.  THEN ORIFICE OR1@82309b-15009b SETTING = 1:

5.  ELSE ORIFICE OR1@82309b-15009b SETTING = 0:

6.  PRIORITY 1:

7.  ; Opens up the orifice at hour 1 of the simulation:

**Functionality:**

This rule effectively opens the orifice "OR1@82309b-15009b" fully at 1:00:00 AM (one hour into the simulation) and keeps it open until 2:00:00 AM. After 2:00:00 AM, the orifice is fully closed.

**Variations, Improvements, and Considerations:**

1.  Partial Opening:

2.  Time-Based Gradual Opening/Closing:

3.  Sensor-Based Control:

4.  Multiple Conditions:

5.  Multiple Orifices:

6.  Rule Interaction

7.  Saving RTC Rules:

- RTC rules are typically written in a separate text file (e.g., "rules.txt") and then referenced in the SWMM5 input file (.inp) under the \[RULES\] section. You would add a line like: \[RULES\] FILE "rules.txt" Or you can paste the rules directly into the \[RULES\] section of the .inp file.

**Example of a More Advanced Rule (Conceptual)**

Let's say you want to implement a rule that mimics a PID (Proportional-Integral-Derivative) controller to maintain a target water level in a storage unit by adjusting an orifice:

![](https://media.licdn.com/dms/image/v2/D4E12AQGqnhbR8249xA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1737309397502?e=1795651200&v=beta&t=psS0sX85CNknYQDOicSyKbZQGVPRp3NGhS4_CYEFhZc)

RTC SWMM5 version of the original SWMM3 Model

> **Summary of of the Input FIle**

Project Configuration Analysis:

1.  Hydraulic Routing Parameters

- Flow Units: CFS (cubic feet per second)

- Routing Method: Dynamic Wave with the following specifications: Inertial Damping: None Normal Flow Limited: Both upstream and downstream Force Main Equation: Hazen-Williams Head Tolerance: Default configuration System Flow Tolerance: 5 Lateral Flow Tolerance: 5

1.  Temporal Configuration

- Simulation Period: 01/01/2002 00:00:00 to 01/01/2002 08:00:00

- Critical Time Steps: Reporting Interval: 15 minutes Wet Weather Step: 15 minutes Routing Step: 20 seconds Rule Step: 0 seconds (continuous evaluation)

Network Infrastructure Components:

1.  Node Configuration

- 9 Junctions with elevations ranging from 101.6 to 128.2 ft

- 1 Free outfall at elevation 89.9 ft

- Maximum junction depth range: 8.8 to 42.7 ft

1.  Conveyance System

- 9 Conduits with varying characteristics: Diameters: 4.0 to 6.0 ft (circular sections) Manning's n: 0.015 to 0.034 Lengths: 300 to 5100 ft

- 1 Transverse weir (ID: 90010) Crest Height: 3.0 ft Discharge Coefficient: 3.33

Control Logic Implementation:

The system implements 7 hierarchical control rules (R1-R7) managing weir 90010:

1.  Depth-based control (Priority 1)

2.  Flow-based control (Priority 2)

3.  Time-of-day operation (Priority 3)

4.  Seasonal control (Priority 4)

5.  Weekly scheduling (Priority 5)

6.  Multi-condition control (Priority 6)

7.  System-wide flow management (Priority 7)

Inflow Configuration:

- Three defined inflow nodes (80408, 81009, 82309)

- Time series data structured with: Peak flows: 40-50 CFS Duration: 3 hours Uniform distribution pattern

> **The PID RTC SWMM5 version of the original SWMM3 Model**

> ** How does this look in ICM InfoWorks and ICM SWMM?**

![](https://media.licdn.com/dms/image/v2/D4E12AQG5S6IqlUa3Dw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1737322267758?e=1795651200&v=beta&t=3QDt1-dRpy8M5PeEg7ijO2DVsmUnmp4AsuKgaS1PZFM)

InfoSWMM Engine == OneSWMM for InfoDrainage and ICM SWMM

> Full Reference for the 1981 version of Extran for SWMM3

![](https://media.licdn.com/dms/image/v2/D4E12AQF2pua-7F2kEg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1736595128049?e=1795651200&v=beta&t=coFWrrwM-chZJgjqmVedmW6p3r0xt1PfHdEpjyH_VJE)

> Closing Note

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time you read one of these posts.**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
