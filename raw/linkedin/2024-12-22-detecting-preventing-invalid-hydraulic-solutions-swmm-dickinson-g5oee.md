---
title: "Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5 (Robert E. Dickinson, Khalid K. Khan, and James T. Smullen | CDM Inc.)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/detecting-preventing-invalid-hydraulic-solutions-swmm-dickinson-g5oee
created: "2024-12-22 17:33"
published: "2024-12-22 17:55"
words: 1119
export_sha256: a62a4a3bf3a2abc2cbf5d1d866d2e5cd11f3e6c3854fc7c883fedc52373e3e70
---
# Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5 (Robert E. Dickinson, Khalid K. Khan, and James T. Smullen | CDM Inc.)

![Urban Runoff Modeling (Humboldt State University, Arcata, California, July 22-27, 2007)](https://media.licdn.com/mediaD4E12AQElbgDt5jACkw "Urban Runoff Modeling (Humboldt State University, Arcata, California, July 22-27, 2007)")

While recently organizing my garage, I discovered an intriguing poster I'd created comparing the 1D St Venant Terms between SWMM4 and SWMM5. Originally crafted in Microsoft Publisher for the **2007 Urban Runoff Modeling Conference at Humboldt State University,** this poster presented a compelling analysis of hydraulic solutions. Though the original Publisher file remains tucked away on an old CDM hard drive, I decided to explore a novel approach: leveraging AI technology to extract and validate the poster's content. Using two AI systems**—**one to interpret the image and another to verify findings against SWMM5's public domain source code—I was able to reconstruct the technical insights from this historical comparison.

> **1/ AI Interpretations of the Image**

**Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5** *(Robert E. Dickinson, Khalid K. Khan, and James T. Smullen \| CDM Inc.)*

### Continuous Simulation SWMM 5 Tools

1.  **Continuous Simulation Needs:**

2.  **Model Challenges:**

3.  **Boundary Conditions:**

------------------------------------------------------------------------

### Continuous Simulation Concerns

1.  The objective is to use the longest possible time step to optimize runtime without compromising the model’s stability.

2.  Maintaining numerical accuracy and avoiding numerical mishaps is critical.

3.  Generating sufficient text and graphical feedback ensures confidence in the results.

------------------------------------------------------------------------

### Key Hydraulic Dynamics

### Flow Dynamics and Terms

- Flow reacts to the **four dynamic terms**: dqdq, dq3, and dq4 (which drives the dynamic wave equation).

- Stability of the model is contingent on the balance between these terms.

### Visual Representations:

1.  Graphs depict the flow's reaction to the four dynamic terms, showing fluctuations over time.

2.  A comparison of normal flow against the dynamic wave equation highlights divergences.

------------------------------------------------------------------------

### Dynamic Wave Equation and Stability

1.  At each time step, the **reasonableness** of the solution is assessed by comparing changes in dq1, dq2, dq3, and dq4 across successive iterations.

2.  **SWMM 4 vs. SWMM 5:**

------------------------------------------------------------------------

### Adverse Slopes and Improvements

- SWMM 5 advances over SWMM 4 by solving key challenges associated with unbounded negative flows.

- By validating both positive and negative results, SWMM 5 prevents invalid hydraulic behavior when dealing with reverse flows.

------------------------------------------------------------------------

### Extended Summary

This poster discusses methodologies and tools for ensuring the accuracy and stability of continuous simulations in SWMM 5 (Storm Water Management Model), an essential tool for hydrological and hydraulic analysis. Continuous simulations, unlike single-event simulations, demand careful handling of dynamic and frequently changing boundary conditions such as weather variables, flow rates, and system stresses. The complexity of these simulations can lead to challenges such as system instability, backflows, and numerical errors.

Central to the poster are discussions about the **Dynamic Wave Equation**, which governs hydraulic behavior in open channel and closed conduit systems. The authors highlight the importance of balancing the four primary dynamic terms, ensuring the simulation adheres to physical laws. Graphs visually illustrate the dynamic balance and the flow's sensitivity to changes in these terms.

One of the primary innovations in SWMM 5, compared to SWMM 4, is its ability to assess hydraulic stability in both forward and reverse flows, addressing critical weaknesses of its predecessor. While SWMM 4 only validated positive flows, SWMM 5 incorporates robust checks for negative flows to prevent unbounded or invalid solutions during reverse flow events.

In conclusion, the poster emphasizes the need for rigorous testing and thoughtful configuration to achieve accurate, reliable, and efficient continuous simulation outcomes in stormwater management.

> **2/ 2nd AI Opinion**

This is a good summary of a poster presentation about SWMM 5, but there are a few minor inaccuracies and areas that could be clarified:

**1. Flow Dynamics and Terms:**

- **Inaccurate:** "Flow reacts to the four dynamic terms: dqdq, dq3, and dq4 (which drives the dynamic wave equation)."

- **Corrected:** The four dynamic terms in the Saint-Venant equations (which underlie SWMM's hydraulic calculations) are typically represented as: **∂Q/∂t:** Rate of change of flow with respect to time. **∂Q²/∂x:** Rate of change of momentum flux with respect to distance. **gA∂H/∂x:** Force due to gravity and slope. **gA(Sf - So):** Force due to friction (Sf) and bed slope (So).

- **Clarification:** While "dqdq" might be shorthand, it's not standard notation and could be confusing. Using the more conventional symbols and explaining what they represent (e.g., Q = flow, A = cross-sectional area, H = water depth) would improve clarity.

![](https://media.licdn.com/dms/image/v2/D4E12AQG_JGTcGBSB1Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1734968022981?e=1795651200&v=beta&t=fpk2ZcNAljr1DZMeCJddjDK28fSoZ_2eeauLALpsx0k)

Flow Dynamics and Terms

**2. Dynamic Wave Equation and Stability:**

- **Inaccurate:** "At each time step, the reasonableness of the solution is assessed by comparing changes in dqdq and dq2dq2 across successive iterations."

- **Corrected:** SWMM 5 checks for excessive changes in **flow (Q) and water depth (H)** between iterations to determine stability. It's not just about the first two terms of the equation.

- **Clarification:** It would be helpful to briefly mention the criteria for assessing "reasonableness" (e.g., tolerances or thresholds for changes in Q and H).

**3. SWMM 4 vs. SWMM 5:**

- **Accurate but could be stronger:** "SWMM 5 advances over SWMM 4 by solving key challenges associated with unbounded negative flows."

- **Improved:** "SWMM 5 significantly improves upon SWMM 4 by addressing a critical weakness in handling reverse flows. While SWMM 4 only validated positive flow solutions, SWMM 5 incorporates checks for both positive and negative flows, preventing unrealistic or unbounded solutions that could occur during backwater or surcharge conditions."

**4. Extended Summary:**

- **Generally accurate:** The extended summary provides a good overview of the poster's key points.

- **Suggestion:** It could explicitly mention the importance of these improvements for modeling complex systems with backwater effects, tidal influences, or looped networks.

**Overall:**

The summary is mostly accurate but could benefit from some minor corrections and clarifications to improve precision and understanding, especially for those familiar with the technical details of SWMM and hydraulic modeling.

![](https://media.licdn.com/dms/image/v2/D4E12AQEvsctj7G3vmw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1734889214595?e=1795651200&v=beta&t=5e-TviUXpaLdmA1uk6r5t2r7DMzEr6AlhgNJ0YU80lc)

Detecting and Preventing Invalid Hydraulic Solutions in SWMM 5 (Robert E. Dickinson, Khalid K. Khan, and James T. Smullen \| CDM Inc.)

> Closing Note

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time you read one of these posts.**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
