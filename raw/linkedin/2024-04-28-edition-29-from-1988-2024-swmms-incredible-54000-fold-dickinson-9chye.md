---
title: "Edition 29: From 1988 to 2024: SWMM's Incredible 54,000-fold Engine or PC Speed Improvement"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-29-from-1988-2024-swmms-incredible-54000-fold-dickinson-9chye
created: "2024-03-28 02:43"
published: "2024-04-28 18:35"
words: 2239
export_sha256: 319280d7106abc76b463ad3fa721f679d82dc351201f0a589730d118fbe2ee27
---
# Edition 29: From 1988 to 2024: SWMM's Incredible 54,000-fold Engine or PC Speed Improvement

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 29: From 1988 to 2024: SWMM's Incredible 54,000-fold Engine or PC Speed Improvement](https://media.licdn.com/mediaD4E12AQG8qfF3QMlWGw "Edition 29: From 1988 to 2024: SWMM's Incredible 54,000-fold Engine or PC Speed Improvement")

**Edition 29** has 15 sections and shows how SWMM evolved from Punch Cards in 1977 to Mag Tapes in 1990 and PC's in 1988: Here are the sections:

1.  Methodology of the Test Model (Extran1.INP): Describes the history and evolution of the test model from Extran 3 in 1981 to SWMM5. Compares the runtime of the model on an ICM AT in 1987–1988 to the current version of SWMM5. Highlights the significant improvement in performance, with SWMM5 being 54,060 times faster than in 1987.

2.  Punch Cards and their usage in running SWMM models: Explains what punch cards look like and how they were created using a punch card machine. Describes the process of using punch cards and a card reader to run SWMM models.

3.  Magnetic Tapes and Their Role in Storing SWMM3: This article discusses the appearance of magnetic tapes and their usage in storing the SWMM3 program from 1980 to 1990. Mentions the role of Job Control Language (JCL) in specifying the magnetic tape to use when running SWMM3 on mini or mainframe computers.

4.  Storage and documentation of SWMM in boxes: describes how SWMM 2.5 and SWMM 3 were stored in ten boxes and had to be carried to computer labs for running the model. Mentions the ability to document the cards by writing on top of them.

5.  SWMM 1 and SWMM 2 Pioneers: This photo shows SWMM 1 and SWMM 2 pioneers in front of Black Hall at the University of Florida (UF). Mentions the author's experience as an undergraduate at UF in 1974 and the use of punch cards for SWMM from 1977 to 1980.

6.  ICM AT in 1987 or 1988: Displays an image of an ICM AT from 1987 or 1988, which was used to create SWMM 4 using a two-pass Fortran compiler.

7.  5 1/4 Floppy Disks before 1990: Shows an image of a 5 1/4 floppy disk used before 1990 to mail SWMM4 to users.

8.  SWMM 5 version of the SWMM 3 Test Model (Example 1): Presents an image of the SWMM 5 version of the SWMM 3 test model, originally called Extran 3 in 1981.

9.  SWMM5 Modification for the Model Speed Test: Describes the modification made to the SWMM5 model for the speed test, using baseline patterns instead of a flow time series to have the same flow every day of every year.

10. SWMM 5 implementation and performance: Explains that SWMM 5 is written in C and can utilize multiple cores on a PC, with the test PC having 32 cores. Provides the output of running the SWMM 5 model from 1988 to 2024 on 32 cores, taking 5 minutes to complete.

11-14. SWMM Input Files and References: - Includes the SWMM 5 INP file (.INP) and the SWMM 4 Input Data file (.DAT) for the test model. - Lists references to SWMM 3, 4, and 5 user manuals and related publications.

1.  Wayne C. Huber's History of SWMM: Mentions Wayne C. Huber's presentation on the history of SWMM at ICWMM 2020.

> **1/ Methodology of the Test Model aka Extran1.INP**

The test model, originally from Extran 3 in 1981, was modified to work in SWMM4 in 1987 and 1988. It also became part of the SWMM5 suite of tests and is included in the OWA-Extran set of hydraulic sample models. During a two-year period (1987–1988),, I frequently compiled the Fortran code and ran the test model using an ICM AT. The experience is etched in my memory: it took 5 minutes to compile the code using a two-pass compiler and another 5 minutes to run the sample model on the ICM AT.

Fast forward to SWMM 5.2+, and the sample model now runs in a mere fraction of a second. To better compare the times, I created a longer simulation model. The original 1987 model was run for a simulation time of 6 hours with 3 hours of flow in a time series. I developed a similar model with a 3-hour baseline pattern that repeats daily and adjusted the simulation dates so that the current version of SWMM5 also took 5 minutes to complete.

The SWMM5 model was run for the period between January 1, 1988, and January 1, 2024, which spans 324,360 hours. Remarkably, SWMM5 is now 54,060 times faster than it was in 1987. **In other words, the 5-minute real-time run in 1987, which simulated 6 hours. The same 5 minutes now in SWMM5 can simulate 324,360 hours (or 36 years).** This incredible improvement in performance showcases the significant advancements made in the SWMM engine over the past few decades.

The significant speed increase in SWMM5 can be attributed to several factors, both on the software and hardware side.From the SWMM5 perspective, the improvements include a more efficient engine, optimized C code, and the ability to utilize multiple cores on modern PCs. These software enhancements have undoubtedly contributed to the faster execution of the model.

However, Moore's Law can largely explain the remarkable advancements in computer hardware over the past few decades that have led to the most significant speed improvement. Moore's Law is an observation and projection stating that the number of transistors in a dense integrated circuit doubles about every two years. This has led to exponential growth in computing power, allowing for faster processing speeds and more efficient execution of complex software like SWMM5.

> **2/ What does a Punch Card look like and how it was created in Punch Card Machine. How did you use the Punch Cards to run a SWMM model - use a Punch Card Reader**

![](https://media.licdn.com/dms/image/v2/D4E12AQGW4QChRyP-vA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714317470610?e=1795651200&v=beta&t=5zpln9osdDyv0qNv-VvWobpx4yWKyJW4EB2J7OombVg)

IBM Keypunch Machine

> **3/ What does a Magnetic Tape look like? The SWMM3 program was stored on a mag tape and the Job Control Language (JCL) told the PC operators that Mag Tape to use when you ran SWMM3 on a Mini or Mainframe computer.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHkbemftHD8Xg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714303918652?e=1795651200&v=beta&t=BIV9Wi_Y4jfPGeCXtQQ__s-VOZLLXKmjE0dSJ76B1mQ)

The SWMM3 program was stored on a mag tape from 1980 to 1990

![](https://media.licdn.com/dms/image/v2/D4E12AQHSEJHeChpHmA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714304887276?e=1795651200&v=beta&t=_ucUGsoTWUqHMWiQf5Ygyx2QAbaEfqMox_MtAlR3rQg)

Mainframe operator with a library of Magnetic Tapes in the Mainframe lab.

> **4/ You stored SWMM in boxes and had to carry the boxes to the Computer labs to run the model. SWMM 2.5 and SWMM 3 were in ten boxes. You can document the cards by writing on top of them.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGViCR8vY8EyQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714304591160?e=1795651200&v=beta&t=E7LGZYxuEzFRPrnIy_jwt_5XZq_B04REjH3CisxcitA)

SWMM 2.5 and SWMM 3 were in ten boxes. You can document the cards by writing on top of them.

> **5/ SWMM 1 and SWMM 2 Pioneers in front of Black Hall at UF. You can see Wayne Huber on the right. I was around Black Hall in 1974 but was a lowly undergrad. Wayne and Jim Heaney had offices on the 4th floor. Which mean i had to walk down the stairs multiple times per day to run SWMM - the Computer Lab was in the Electrical Engineering Building. I used the Punch cards for SWMM from 1977 to 1980.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGtjdNuNA_A_Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714304185830?e=1795651200&v=beta&t=inm6G_u8PN8CcTofXTFqXQBL_915Q3wLNTtxY0h5SnY)

SWMM 1 and SWMM 2 Pioneers in front of Black Hall at UF. You can see Wayne Huber on the right.

> **6/ What an** IBM PC AT (with internal hard drive) **looked like in 1987 or 1988. It was used to make SWMM 4 with a two pass Fortran Compiler. The compiler worked on the hard drive.**

![](https://media.licdn.com/dms/image/v2/D4E12AQE9a84aObtkNg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714319533315?e=1795651200&v=beta&t=olLgO8Z8zP0k8gawNQXyIvZbNQ65ZUkYem5wTqghr0c)

**What an** IBM PC AT (with internal hard drive) **looked like in 1987 or 1988. It was used to make SWMM 4 with a two pass Fortran Compiler. The compiler worked on the hard drive.**

> **7/ What a 5 1/4 Floppy Disk looked Like before 1990. It was used to mail SWMM4 to Users.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFP1g_LuUFUGw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714319702655?e=1795651200&v=beta&t=6zEtAhcGvIgsozyZc-yaA8fA-MfUegaZondfhtlsrLI)

What a 5 1/4 floppy disk looked like before 1990. Used to mail SWMM4 to users.

> **8/ SWMM 5 version of the SWMM 3 Test Model called Example 1 from 1981 - it was called Extran 3 in 1981**

![](https://media.licdn.com/dms/image/v2/D4E12AQFqq4HLsq-3yA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714303462315?e=1795651200&v=beta&t=4KRzF8iSnPioiqmG1yV5rbtuOIBSBXlAkcCF6ZGMdBI)

SWMM 5 version of the SWMM 3 Test Model called Example 1 from 1981 - it was called Extran 3 in 1981

> **9/ SWMM5 Modification for this Model Speed Test - Baseline Patterns were used instead of a flow time series so we can have the same flow every day of every year.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHYHVvL26ditA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714318449769?e=1795651200&v=beta&t=FhS2kxushobWR3DN6gpRMFCQx9tLUGmunjDMUCzHcn8)

SWMM5 Modification for this Model Speed Test - Baseline Patterns were used instead of a flow time series so we can have the same flow every day of every year.

> **10/ SWMM 5 is written in C and not Fortran and can use as many cores as you have on your PC. My test PC has 32 cores.**

![](https://media.licdn.com/dms/image/v2/D4E12AQHWkfTOVhCE4Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1714303606273?e=1795651200&v=beta&t=KJmyIPFs00Xh2So6GFfLhoOqdzk0i-NiY5OC30RpMZo)

SWMM 5 is written in C and not Fortran and can use as many cores as you have on your PC. My test PC has 32 cores.

> **11/ SWMM 5 is simulated from 1988 to 2024 on 32 cores and takes 5 minutes to run.**

> **12/ SWMM 5 INP file (.INP) as a variation on the Extran 4 model. It now has patterns.**

> **13/ SWMM 4 Input Data file (.DAT) It has a lot of comments or comment lines**

> **14/ SWMM 3,4,5 References**

Storm Water Management Model User's Manual, Version III, Huber, W.C., Heaney, J.P., Nix, S. J., Dickinson, R.E. and Polmann, D.J., "Storm Water Management Model User's Manual Version III," EPA 600/2 84 109a (NTIS PB84 198423), USEPA, Cincinnati, OH (also available from Dept. of Environmental Engineering Sciences, University of Florida, Gainesville), **November 1981**

Storm Water Management Model, Version 4: User's Manual, Huber, W.C. and Dickinson, R.E.,"Storm Water Management Model, Version 4: User's Manual," First Printing, NTIS PB88 236641/AS, Environmental Research Laboratory office of Research and Development U.S. Environmental Protection Agency, Athens, Georgia, **August, 1988**

Storm Water Management Model User's Manual Version 4: Extran Addendum, Roesner, L.A., Aldrich, J.A., Dickinson, R.E., "Storm Water Management Model User's Manual Version 4: Extran Addendum," EPA/600/3 88/001b,Environmental Research Laboratory Office of Research and Development, U.S. Environmental Protection Agency, Athens, Georgia, **August, 1988**

Rossman, L.A., Dickinson, R.E., Schade, T., Chan, C.C., Burgess, E., Lai, F.H. Sullivan, D. 2003. Redevelopment of the US EPA Stormwater Management Model. Proceedings of **WEFTEC 2003. Los Angeles, CA. Oct. 11-15 SWMM5**

> **15/ Wayne C Huber History of SWMM from ICWMM 2020**

\[embedded item\]

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133, or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
