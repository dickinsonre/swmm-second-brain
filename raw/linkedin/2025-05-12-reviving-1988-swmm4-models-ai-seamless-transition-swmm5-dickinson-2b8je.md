---
title: "Reviving 1988 SWMM4 Models with AI: A Seamless Transition to SWMM5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/reviving-1988-swmm4-models-ai-seamless-transition-swmm5-dickinson-2b8je
created: "2025-04-27 15:28"
published: "2025-05-12 22:47"
words: 1818
export_sha256: 66f26ff8ec4f6f54fe42631f0ce2281ff60d887e1a3ea4e6d4e2954d5e886a6d
---
# Reviving 1988 SWMM4 Models with AI: A Seamless Transition to SWMM5

![Reviving 1988 SWMM4 Models with AI: A Seamless Transition to SWMM5 ](https://media.licdn.com/mediaD4E12AQEemNlcsIccZQ "Reviving 1988 SWMM4 Models with AI: A Seamless Transition to SWMM5
")

> **Introduction**

Bridging Decades with AI Imagine being handed a stormwater model from 1988, written for SWMM4, and tasked with making it run on modern software. Sounds daunting, right? Legacy models like these are critical for infrastructure planning and regulatory compliance, but their outdated formats can be a nightmare to update. Enter modern AI tools, which made converting a 1988 SWMM4 file to SWMM5 surprisingly straightforward. Here’s how we did it—and what we learned along the way. Essentially, we are duplicating the Visual Basic 6 converter you can download from the **EPA SWMM5** [download page](https://www.epa.gov/water-research/storm-water-management-model-swmm) to see if it can now be done using any AI tool in 2025. Spoiler: it can, and since VB 6 is not as common as it used to be means those in the future who want to do this do not have to use the VB 6 code.

![](https://media.licdn.com/dms/image/v2/D4E12AQF1wmGkVZWAfA/article-inline_image-shrink_1500_2232/B4EZbB63ajGQAU-/0/1747010159157?e=1795651200&v=beta&t=j_1vVfa189QmywAk9htk1snW-6G_JaK127X3i8OcF30)

Reviving 1988 SWMM4 Models with AI: A Seamless Transition to SWMM5

I’m excited to share a throwback to my work on the SWMM5 redevelopment project (2001–2005). When I worked with CDM, we had a CRADA with the USEPA (led by Lew Rossman). A part of the CRADA work was to create a Visual Basic-based SWMM4 to SWMM5 converter, created ably by Carl Chan of CDM. As part of this CRADA, I compiled around 500 SWMM4 models, with additional detailed models contributed by CDM’s Cincinnati office, to support the conversion process.

Recently, I uploaded these 500 SWMM4 .dat files to my GitHub repository, 1729-SWMM-

![](https://media.licdn.com/dms/image/v2/D4E12AQEZvNWk-h76OA/article-inline_image-shrink_1500_2232/B4EZbGkwujHIAU-/0/1747088250129?e=1795651200&v=beta&t=Nfi3qpKu2maOTDOICZqvPcd31HyXtFxeLQkE_f-brwQ)

> **Why This Matters for SWMM**

(Storm Water Management Model) has been a cornerstone of hydraulic modeling since the 1970s. SWMM4, popular in the 1980s, used the EXTRAN block (EXTRAN is the dynamic wave solver for SWMM3 and SWMM4) for dynamic wave routing, while SWMM5, the current standard, offers enhanced features and a user-friendly GUI. Converting old SWMM4 files to SWMM5 ensures historical data remains usable, saving time and preserving decades of engineering insights. With AI, this process becomes faster and more accessible, even for complex models.

> **The Conversion Process**

AI in Action We used an AI tool (in this case, a large language model trained for data parsing) to read a 1988 SWMM4 DAT file and generate a SWMM5 INP file. The process involved several key steps:

- Parsing Legacy Data: The AI interpreted SWMM4’s EXTRAN block (EXTRAN is the dynamic wave solver for SWMM3 and SWMM4), mapping its conduit and junction data to SWMM5’s format. As an aid, I made two blogs with the [data format for SWMM4](https://swmm5.org/2025/04/28/swmm4-extran-4-swmm-4-99-data-file-format/) for the current and future AI tools.

- Estimating Coordinates: Since SWMM4 files lack spatial data, the AI assumed a linear network, assigning X,Y coordinates starting at (0,0) for the Inflow node, with 100-foot increments based on conduit lengths. SWMM4 did not have x, y coordinates so I just said make up reasonable values based on the link lengths and starting at 0.0

- Adjusting Parameters: We applied SWMM5’s default settings for solver parameters like DW (dynamic wave routing) and MIN_SURFAREA, ensuring compatibility.

- Validation: The resulting INP file loaded seamlessly into SWMM5’s GUI, visualized a linear network of 2-foot circular conduits, and ran without errors, producing hydraulic results consistent with the original SWMM4 simulation’s intent, especially for modeling surcharge.

![](https://media.licdn.com/dms/image/v2/D4E12AQHamxb5Fx4NPA/article-inline_image-shrink_1500_2232/B4EZbB7oHwHMAU-/0/1747010362688?e=1795651200&v=beta&t=rag5iSO4riIDXDtW3WIQFnCAvPLz1AmnJyJD_yt0y2E)

Conversion Process: AI in Action We used an AI tool (in this case, a large language model trained for data parsing) to read a 1988 SWMM4 DAT file and generate a SWMM5 INP file

For a sample SWMM4 DAT files, check out my [1729 SWMM Models GitHub Repository](https://github.com/your-repo-link).

Challenges and Solutions Despite the smooth conversion, a few hurdles emerged:

- Ambiguous Elements: The SWMM4 file included unclear lines, like “J1 1” (possibly a control switch) and repeated numbers in D1 junction lines (e.g., 4040 for Inflow, perhaps indicating storage). Lacking documentation, we excluded these from the SWMM5 file.

- Missing Spatial Data: Estimating coordinates was a best guess. Real-world networks may need actual coordinates for precise visualization.

- Solver Approximations: SWMM4 parameters like SURTOL and SURJUN were approximated using SWMM5 defaults, which could slightly affect convergence under surcharge conditions.

These issues were minor and didn’t prevent a runnable SWMM5 model, but they underscore the need for context or documentation when working with legacy files. See the link above for the SWMM4 data format.

> **Outcomes**

A Modern Model with Historical Roots The converted SWMM5 model was a success: it ran error-free, visualized correctly, and preserved the original simulation’s hydraulic behavior. This compatibility stems from both SWMM4 and SWMM5 relying on the St. Venant equations for dynamic wave routing. By leveraging AI to automate parsing and coordinate estimation, we saved hours of manual work while enhancing the model’s usability in SWMM5’s GUI. The process highlights how AI can bridge legacy and modern platforms, making historical stormwater models relevant for today’s challenges.

> **Lessons Learned**

- **AI Saves Time**: Large language models can parse complex SWMM4 files in minutes, cutting down hours of manual work. Python-based LLMs may also work.

- **Documentation is Crucial**: Unclear parameters in old files can stall progress. Track down original docs or consult model creators to resolve ambiguities. See the link above for the SWMM4 data format.

- **Always Validate**: Compare outputs like surcharge levels between SWMM4 and SWMM5 to ensure accuracy. Start with small test cases to catch errors early.

- **Share and Learn**: I’ve shared 500 SWMM4 models on my GitHub repository (#). Explore them and let me know your conversion tips in the comments!

![](https://media.licdn.com/dms/image/v2/D4E12AQH4-XF2BkmS9w/article-inline_image-shrink_1500_2232/B4EZbB8ydnHwAU-/0/1747010661809?e=1795651200&v=beta&t=quzhYTy--h6Pe8A7IxYz_rMVcAVQ_3YmaQHl7Iay2Fc)

Lessons I learned from this exercise

.

Recently, I uploaded these 500 SWMM4 .dat files to my GitHub repository, 1729-SWMM-Models, and decided to test how 2025 AI tools handle this conversion. The results? Impressively accurate! To streamline the process, I also published a few blogs detailing the input formats for SWMM4 Runoff and Extran data files. It’s been a fascinating journey revisiting this project and seeing how modern AI enhances legacy model conversions. Check out the repository and blogs to explore more! \#Stormwater \#SWMM \#Hydrology \#AI \#Engineering

The process of converting a SWMM4 .dat file, designed for the EXTRAN block, into a valid SWMM5 .inp file was a successful endeavor that required careful mapping of the older model’s structure and parameters to the modern SWMM5 format. The SWMM4 file, representing a linear network of 10 conduits, 11 junctions, an outfall, and an inflow hydrograph for a test case labeled "SWMM CRADA Example 1," was systematically translated to ensure compatibility with SWMM5’s dynamic wave routing and section-based input format. Key steps included preserving the network geometry by mapping junctions and conduits, converting the hydrograph to SWMM5’s \[TIMESERIES\] and \[INFLOWS\] sections, and aligning simulation parameters like time steps and solver settings. Specific updates, such as changing FLOW_ROUTING to DW for dynamic wave routing, using MIN_SURFAREA for minimum nodal surface area, and adding a \[COORDINATES\] section with best-guess X, Y coordinates based on conduit lengths, ensured the file met the user’s requirements. The resulting .inp file was loaded into SWMM5, visualized correctly in the GUI, and ran successfully, producing hydraulic results consistent with the original SWMM4 simulation’s intent, particularly for modeling surcharge in 2-foot circular conduits.

![](https://media.licdn.com/dms/image/v2/D5612AQHmP8Oo6bxyOg/article-inline_image-shrink_1500_2232/B56ZZ52pVlGkAU-/0/1745801091543?e=1795651200&v=beta&t=b38DtWZZIPTosFr7MPyHo-dFdUIi4tFcON5IDitjt7s)

What does an SWMM4 dat file look like? See this folder in my 1729 SWMM Models GitHub Repository., You used comments to guide you about the meaning of the parameters on each data line.

Despite the success, a few issues and challenges arose during the conversion process. First, the SWMM4 file contained ambiguous elements, such as the J1 1 line, which likely pertains to a control switch but lacked clear documentation, leading to its exclusion from the SWMM5 file. Similarly, the repeated numbers in the D1 junction lines (e.g., 40 40 for Inflow) were unclear, possibly indicating storage or surface area parameters, but were omitted as they didn’t map directly to SWMM5’s junction properties. Another challenge was estimating node coordinates, as the SWMM4 file provided no spatial data. Assuming a linear layout with 100-foot conduit lengths starting at a (0,0) datum for the Inflow node was a reasonable guess, but real-world networks might require actual coordinates for accurate visualization. Additionally, some SWMM4 solver parameters, like SURTOL and surjun, were approximated using SWMM5’s default settings, which might slightly affect convergence behavior under surcharge conditions. These issues were minor and did not prevent the creation of a valid, runnable SWMM5 model, but they highlight the importance of understanding legacy file nuances.

![](https://media.licdn.com/dms/image/v2/D4E12AQFbkLHWOnRNhA/article-inline_image-shrink_1000_1488/B4EZbCBitlGQAQ-/0/1747011907377?e=1795651200&v=beta&t=8-jaeHvuQPzyiCaFMOUcFcxoN1fGsvsmmXLTv22ToRc)

Why SWMM4 and its free format inp file was so much better than the SWMM3 fixed format.

![](https://media.licdn.com/dms/image/v2/D4E12AQE1prdDoJeJSg/article-inline_image-shrink_1500_2232/B4EZaHU2YTHcAU-/0/1746027112597?e=1795651200&v=beta&t=wAAXmNjwifRv9lgPmKek5VQX0kkVTTm6F9lgi92vywM)

January 2003 Repository of 500 SWMM4 input data files

The successful conversion underscores the compatibility between SWMM4’s EXTRAN block and SWMM5’s dynamic wave routing, facilitated by their shared reliance on the St. Venant equations. By addressing the specified changes—using DW, MIN_SURFAREA, and adding coordinates—the process not only met the technical requirements but also enhanced the model’s usability in SWMM5’s GUI, where the linear network was visually verifiable. The few unresolved elements, like J1 and D1 ambiguities, suggest that older SWMM4 files may require additional context or documentation for perfect fidelity. Nonetheless, the resulting .inp file ran without errors, demonstrating that careful translation can bridge the gap between SWMM4 and SWMM5, preserving the original simulation’s purpose while leveraging SWMM5’s modern features. This process serves as a valuable example for engineers transitioning legacy models to current platforms, ensuring continued usability of historical stormwater simulations.

![](https://media.licdn.com/dms/image/v2/D4E12AQEroTyQie8k-w/article-inline_image-shrink_1500_2232/B4EZbGlT_GHcAc-/0/1747088392887?e=1795651200&v=beta&t=zNGGPj4aZMynWt2Goj_1H0ZPDK3TdC81_yl0roPN_2k)

The converted SWMM5 model from SWMM4
