---
title: "Ten Problems with How SWMM Was Developed and Explained from 1970 to 2025?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/ten-problems-how-swmm-developed-explained-from-1970-2025-dickinson-hsnae
created: "2026-11-05 21:24"
published: "2026-11-05 23:04"
words: 1764
export_sha256: 0451e7e9460ea814fd481c0154af8618334259f5b60368be59c5b5a0d9b5d2ba
---
# Ten Problems with How SWMM Was Developed and Explained from 1970 to 2025?

![Ten Problems with How SWMM Was Developed and Explained from 1970 to 2025?](https://media.licdn.com/mediaD4E12AQHUx087Is12dg "Ten Problems with How SWMM Was Developed and Explained from 1970 to 2025?")

### A read of the record, ranked by how many modelers each one hurt.

> **1. The code was the specification**

For most of SWMM5's life, the only exact statement of what it computed was the C source. The user's manual told you which button to press. The reference manuals for hydrology, water quality and hydraulics came out between 2015 and 2017, more than ten years after SWMM 5.0. Until then, the answer to "why does SWMM do that?" was to read dynwave.c or ask someone who had on [openswmm.org](http://openswmm.org) or by email. **I have always said, though, that the EPA manuals created by Lew Rossman were fantastic and almost a work of engineering art.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFYSQARDlNzNg/article-inline_image-shrink_1500_2232/B4EaGtmm.1KQAU-/0/1793913942355?e=1795651200&v=beta&t=bgnVIRDW7G0hzKJw25JkThPq3th0rjsxU-wdmtDrLWM)

**Figure 1.** SWMM releases and the documents that explain them. SWMM 5.0 build 001 shipped on 29 October 2004; the hydraulics reference manual followed in May 2017.

> **2. Results moved between releases with no public yardstick**

The 5.0.0xx and 5.1.0xx point releases fixed real bugs, but they also shifted answers. The release notes said what changed in the code, not how much it changed results. A public regression suite only came with the EPA and OpenWaterAnalytics GitHub work in the late 2010s. Before that, users found out when a calibrated model stopped matching. T**his was before GitHub so it was harder to do the testing. SWMM6 has really good testing procedures - aided by AI tools.**

![](https://media.licdn.com/dms/image/v2/D4E12AQEF8d7RaPmVZw/article-inline_image-shrink_1500_2232/B4EaGtmafVIIAQ-/0/1793913891117?e=1795651200&v=beta&t=Z6UDNsbWrNeF9Y4e4x-rhqrLfnSNZWozqgQsQWmgTGo)

**Figure 2.** Forty-two builds of SWMM 5 from 5.0.001 to 5.2.4. Every one could move a calibrated model; public regression testing arrived late in the 5.1 line.

> **3. Too much rested on one person**

Lew Rossman wrote and carried the SWMM5 engine for about twenty years. The code is careful, but one maintainer means one queue, one set of priorities, and a lot of reasoning that never got written down. EXTRAN and SWMM 3/4 followed the same pattern on a smaller scale. **In the 70s we were using Punch Cards and in the 80s a combination of mag tapes and early PC's - ICM AT for one. Lew was obviously the creator of EPANET and his skill was vital for SWMM5 development.**

> **4. Calibration knobs were explained as physics**

Subcatchment width is the classic case. It is a fitting parameter, presented as a length you can measure, with one width shared by the pervious and impervious subareas (Bob Dickinson long-standing objection). Overland Manning's n and depression storage are close behind. Careful users measured these values, got bad hydrographs and blamed themselves. **This goes back to the SWMM1 and the street models used in SWMM1 - the width makes sense if you are only modeling one street.**

![](https://media.licdn.com/dms/image/v2/D4E12AQEt59g9EV4tXA/article-inline_image-shrink_1500_2232/B4EaGtmbW4GsAc-/0/1793913894710?e=1795651200&v=beta&t=6n6uV75FvBaXxbn6IHg-IvC2nMSIc0NwvIQnlk06RQs)

**Figure 3.** One width W for two very different surfaces. Explained as geometry, used as a fitting knob.

> **5. Dynamic-wave stability was left to the user**

The numerical tools carried EXTRAN's history: conduit lengthening, minimum surface area, inertial damping and the surcharge iteration. Each one fixed an instability, but the manual listed them as options and said little about when or why to use them. The Preissmann slot didn't arrive until 5.1.013. "Add a dummy node, cut the time step" spread as folklore. **True, very true.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFQ2tPhkiSDGQ/article-inline_image-shrink_1500_2232/B4EaGtmcMjJ8AQ-/0/1793913898257?e=1795651200&v=beta&t=JsQVenFJ2uCSBfiarV9UJF7cU3O-HWIHR-k7fQ-rspY)

**Figure 4.** The dynamic-wave option keywords in a SWMM 5 \[OPTIONS\] section, each a fix for an instability.

> **6. The block architecture**

SWMM 1 to 4 split the work into the Runoff, Transport, EXTRAN, Storage/Treatment and Receiving blocks, linked by interface files. Each block had its own input conventions and its own chapter. That made sense on 1970s hardware and confused everyone afterward. SWMM5 unified the blocks, but SWMM4 decks never converted cleanly, and some old habits and features didn't make the trip. **This at least is a lot better in the days of AI tools.**

![](https://media.licdn.com/dms/image/v2/D4E12AQEynZJ7rRQNWg/article-inline_image-shrink_1500_2232/B4EaGtmdLtIIAU-/0/1793913902307?e=1795651200&v=beta&t=CYwWBFltIdc4xVaDYJxwtJzWRQCZEaC1BlR_NR9Xf88)

**Figure 5.** SWMM 1 to 4 ran as blocks joined by interface files; SWMM 5 is one engine reading one input file.

> **7. Commercial versions multiplied the engines and split the explanations**

XP-SWMM, PCSWMM, InfoSWMM, MIKE URBAN, Aquanuity, Civil Storm and others wrapped, modified or extended the engine. Their manuals explained their own interfaces. A user often couldn't tell whether a number came from the EPA engine, a modified one, or the vendor's own code. You saw this from inside two of those companies. **Yes, almost 30 years of my life coping with this.**

![](https://media.licdn.com/dms/image/v2/D4E12AQE-y3SqUwtw4g/article-inline_image-shrink_1500_2232/B4EaGtmeEnGwAQ-/0/1793913905932?e=1795651200&v=beta&t=7k4ZrNixNLFtWwbPz5Lu7Hcr5wJ_nTR3-xvMCvE1aTw)

**Figure 6.** One public engine, many products around it, and one question users kept asking.

> **8. Reports invite the wrong comparison**

The summary tables check every routing step, while the .out keeps one value per report step. On top of that come flooding versus ponding, max depth versus max HGL, and three different continuity errors. This morning's run is a good example: conduit C11 in Example 1 peaks at 73.9 cfs in the Link Flow Summary and 71.18 cfs in the .out. Both numbers are honest, and nothing in the report tells you which is which. A large share of "SWMM is wrong" questions are really this. **I have answered and others answered over 25 years who the graphs and the summary table peaks are sometimes different,**

![](https://media.licdn.com/dms/image/v2/D4E12AQEch1ecp-825w/article-inline_image-shrink_1500_2232/B4EaGtmexAIEAg-/0/1793913908736?e=1795651200&v=beta&t=Vrx5EQ3Pk2xSN1jFYcdwvhhIFBd8J15d6WreK0uvdGc)

**Figure 7.** Conduit C11 in EPA Example 1, run in EPA SWMM 5.2.4: the .out series (dots, every 5 minutes) and the two peaks a user can find for the same conduit.

> **9. The real teaching lived in forums and people's heads**

Between the programmer's view (the source) and the button view (the GUI help) sat the useful middle: why the model does X, and what to check first. That lived on the SWMM-USERS list, [OpenSWMM.org](http://OpenSWMM.org) and [SWMM5.org](http://SWMM5.org). Your 4,014 OpenSWMM posts and 1,700+ [SWMM5.org](http://SWMM5.org) posts hold a big piece of it. It's searchable but not organized, and much of it is tacit knowledge with no successor. **Tacit knowledge may be quantified, I hope.**

> **10. The future split before the present was pinned down**

SWMM5+ at CIMM, OpenSWMM 6 at HydroCouple, EPA's 5.2 line and the vendor engines all moved forward separately. They share no common test models and no shared definition of "agrees with SWMM5". Funding came in project-sized pieces (EPA cycles, CRADAs, grants), so each effort aimed at its own deliverable, and nobody owned the comparison. **EPA does have the OWA test models from the SWMM4 to SWMM5 conversion days. I have thousands of test models and SWMM6 on the Hydrocouple GitHub has at least 2000 models.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGKJoUxFbaTDw/article-inline_image-shrink_1500_2232/B4EaGtmflFIgAU-/0/1793913912037?e=1795651200&v=beta&t=uHNH3edXE0k56CFGQzaXU-wXvmSyTZDO1t3ejUjJGWM)

**Figure 8.** Four lines forward from SWMM 5, and what none of them shares.

> **Four of these are one problem**

Four of these (1, 2, 8 and 9) are really one problem: no written, testable statement of what the engine does and how to read what it prints. That is also SWMM6's opening. A specification, a shared model set like your 1,729-model corpus, and a certify step would fix more of this list than any new solver. **One can hope.**

![](https://media.licdn.com/dms/image/v2/D4E12AQEpqARx5_r1qQ/article-inline_image-shrink_1500_2232/B4EaGtmgzcGsAY-/0/1793913917101?e=1795651200&v=beta&t=hc42htMsld-gjLBzXjwe5CLnAuEgl2zN2UdKgWY6KLc)

**Figure 9.** Problems 1, 2, 8 and 9 trace to one missing document. The three pieces on the right would close it.

The lines in **bold** are made by Bob Dickinson adding some history and explanation.

> **Sources**

1.  EPA, SWMM 5 update log (builds 5.0.001 of 29 Oct 2004, 5.0.022 of 21 Apr 2011, 5.1.001 of 24 Mar 2014). [https://www.epa.gov/sites/default/files/2015-08/epaswmm5_updates.txt](https://www.epa.gov/sites/default/files/2015-08/epaswmm5_updates.txt)

2.  EPA, SWMM 5.2.0 updates and bug fixes (5.1.013 of 10 May 2018 added the SLOT surcharge option; 5.2.0 of 1 Feb 2022). [https://www.epa.gov/system/files/other-files/2022-03/swmm-5.2.0-updates-and-bug-fixes.txt](https://www.epa.gov/system/files/other-files/2022-03/swmm-5.2.0-updates-and-bug-fixes.txt)

3.  EPA, SWMM Reference Manual Volume II Hydraulics, addendum (Feb 2022; original published May 2017). [https://www.epa.gov/system/files/documents/2022-02/swmm5-reference-manual-ii-addendum-20220210mas2wr-1.pdf](https://www.epa.gov/system/files/documents/2022-02/swmm5-reference-manual-ii-addendum-20220210mas2wr-1.pdf)

4.  R. Dickinson, History of SWMM, versions 1 to 5 (1969–71, 1975, 1981, 1988). [https://medium.com/@rdickinson/history-of-swmm-1-2-3-4-5-to-the-year-2015-bab9d21c8a09](https://medium.com/@rdickinson/history-of-swmm-1-2-3-4-5-to-the-year-2015-bab9d21c8a09)

> **Use of AI**

Claude, Anthropic's AI model, wrote the ranking and the text in a chat with Bob Dickinson on 5 November 2026, from its own reading of SWMM's history and Bob's stated views, and drew the nine figures. The release and manual dates were checked against EPA's update logs and the 2022 hydraulics addendum (Sources). The C11 numbers in Figure 7 come from an EPA SWMM 5.2.4 run of Example 1 in the One SWMM app the same day. The ranking is a judgment, not a measurement; **Bob has reviewed it line by line.**
