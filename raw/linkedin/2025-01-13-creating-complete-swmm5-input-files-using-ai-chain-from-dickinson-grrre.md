---
title: "Creating Complete SWMM5 Input Files Using AI Chain Prompting from SWMM5 Rules"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/creating-complete-swmm5-input-files-using-ai-chain-from-dickinson-grrre
created: "2025-01-12 01:31"
published: "2025-01-13 00:01"
words: 591
export_sha256: a97ccd5a31256f51ce745d3c113142f76ff40e2cee0126a2a7ede90a1c34a6c2
---
# Creating Complete SWMM5 Input Files Using AI Chain Prompting from SWMM5 Rules

![Creating Complete SWMM5 Input Files Using AI Chain Prompting](https://media.licdn.com/mediaD4E12AQHBiDQesxuPrw "Creating Complete SWMM5 Input Files Using AI Chain Prompting")

Creating Complete SWMM5 Input Files Using AI Chain Prompting

When generating SWMM5 input files using AI, a two-prompt strategy proves highly effective. The first prompt acts as a comprehensive rulebook, establishing all the necessary requirements and conventions for a valid SWMM5 .inp file. This includes specifying all required sections, formatting rules, and data validation criteria.

This rulebook prompt is crucial because it prevents common AI shortcomings when generating SWMM5 files. Without explicit instructions, AI tends to abbreviate repetitive elements like rainfall time series or subcatchment polygon coordinates, often using ellipses (...) or notes like "remaining coordinates follow similar pattern." While this makes sense from a text generation perspective, it produces incomplete SWMM5 files that won't run properly.

The second prompt then defines the specific model you want to create. This could include details like the number of subcatchments, conduit sizes, rainfall patterns, or any other model parameters. Because the first prompt has established strict rules about completeness and proper formatting, the AI generates a fully detailed input file with all necessary components.

This two-stage approach ensures that generated SWMM5 files include all required elements, maintain proper syntax, and avoid shortcuts in repetitive sections. The result is a syntactically valid .inp file that can be directly imported into EPA SWMM5 without needing manual completion or correction.

![](https://media.licdn.com/dms/image/v2/D4E12AQEWg_ykxDOy1w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1736725455573?e=1795651200&v=beta&t=uX7Fg_IrKX-HcJj7HAU8MkSEBr418SrDlcpA7akldGQ)

**Two-Step Prompt**

> **1/ First Prompt Sets Up the Rules**

> **2/ Second Prompt** - What Do I want to make

> **3/ How to Use This Prompt**

1.  **Copy** this entire prompt into your AI interface or modeling environment.

2.  **Add specifics** such as the **number of subcatchments**, infiltration rates, rainfall series, node elevations, or conduit sizes.

3.  **Send or run** the prompt. The system should generate a fully structured SWMM5 file.

4.  **Save** the file and open it in SWMM5 to confirm it works.

5.  **Refine** as needed, adding or adjusting subcatchments, infiltration, or other parameters.

> **4/ End Result is a generated SWMM5 inp file**

Again, you copy the long prompt to set up the second prompt. In Claude the inp generated is to the right.

![](https://media.licdn.com/dms/image/v2/D4E12AQEoW2AJfjShSA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1736725939245?e=1795651200&v=beta&t=03FzWj0SK7rmXn89vCL6pckEOfiOJayrzbfLGdh7SzI)

**End Result is a generated SWMM5 inp file**

> **5/ SWMM5 Model Runs Right Away**

I just copy the generated file from the AI (Claude in this case) and save it as a text inp file. Next, I open up the file in SWMM5.2.4, and it runs right away. It may not work right away if the AI forgot to define the whole rainfall time series.

![](https://media.licdn.com/dms/image/v2/D4E12AQFdL6hynHqWog/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1736725964778?e=1795651200&v=beta&t=_krlXTLPNrKZT-ClWO2Z-SInbxkMdh-7GPhPv9QQhJo)

**SWMM5 Model Runs Right Away**

> Closing Note

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time you read one of these posts.**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
