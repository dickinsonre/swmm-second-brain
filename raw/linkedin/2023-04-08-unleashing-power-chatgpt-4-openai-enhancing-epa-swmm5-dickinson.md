---
title: "Unleashing the Power of GPT4 and OpenAI: Enhancing EPA SWMM5 Test Model Building and Sensitivity Analysis"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/unleashing-power-chatgpt-4-openai-enhancing-epa-swmm5-dickinson
created: "2023-04-08 06:27"
published: "2023-04-08 07:22"
words: 704
export_sha256: eab995c2925372ab8c06e4443badeb25f0bad7a323ea154e22f3cc13d4c0119c
---
# Unleashing the Power of GPT4 and OpenAI: Enhancing EPA SWMM5 Test Model Building and Sensitivity Analysis

![](https://media.licdn.com/mediaD4E12AQHdxUgMCnfb_A)

The focus of our exploration is the capability of GPT4, OpenAI's latest language model, to comprehend and manipulate small SWMM5 INP files based on text prompts. We are working with compact models containing SWMM5 input sections with column labels to examine how GPT4 can effectively modify data parameters and geometry.

1.  Comprehensive integration: The article would demonstrate the seamless integration of GPT4 and OpenAI with EPA SWMM5, showcasing the benefits of combining advanced language models and hydrological modeling software for improved analysis.

2.  Enhanced model building: By leveraging GPT4's natural language processing capabilities, the article would explore new ways to efficiently create, modify, and validate EPA SWMM5 test models, ultimately saving time and effort for modelers.

3.  Sensitivity analysis: The article would provide insights into how GPT4 and OpenAI can perform sensitivity analysis on EPA SWMM5 models, helping engineers and researchers better understand the impacts of various input parameters and assumptions on model outputs.

4.  Improved decision-making: By demonstrating how GPT4 and OpenAI can aid in identifying key parameters and their effects on model outcomes, the article would highlight the potential for more informed decision-making in urban stormwater management and environmental planning.

5.  Accessible learning: The article would cater to professionals and enthusiasts alike, offering an engaging and informative approach to learning about the cutting-edge combination of AI and hydrological modeling.

6.  Real-world applications: By providing practical examples and case studies, the article would show readers how to apply the concepts and techniques discussed in real-world scenarios, thus bridging the gap between theory and practice.

7.  Future possibilities: Lastly, the article would also touch on the potential future developments and applications of AI-driven tools like GPT4 in the field of environmental modeling and management, inspiring readers to explore new opportunities and possibilities.

I show the prompts and tests below, but in case you do not want to see them all - it successfully used my prompts and made a new working, albeit small model, ideal for students and testing. Or in the words of GPT4

Throughout our conversation, we made several modifications to the SWMM5 input file:

1.  Changed the outfall name to "OutfallTwo".

2.  Modified the subcatchment IDs to "wBioCell" and "woBioCell".

3.  Updated Manning's N values to default SWMM5 values and adjusted infiltration parameters for soil class B.

4.  Created two new scenarios with prefixes "Scen1" and "Scen2", duplicating the subcatchments and modifying the raingage ID to "rainStorm".

5.  Updated the coordinates of the new subcatchments so they are offset by 500 and 1000 units, respectively.

6.  Updated the LID_USAGE table to include the new scenarios, Scen1 and Scen2.

7.  Modified the number of LID units in Scen1 to 10 and in Scen2 to 50.

These changes allow for an expanded analysis of scenarios with varying LID parameters, infiltration settings, and subcatchment configurations.

![](https://media.licdn.com/dms/image/v2/D4E12AQGxsuQFa0x7qQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1680938195149?e=1795651200&v=beta&t=_vufLwiteU1BIcJPvz5b2-xnIt-vFqA-w0vHYUb4S_Q)

OpenAI model on the left - original on the right. Despite these modifications, the newly created model worked seamlessly in the EPA SWMM5 software without any issues. This demonstrates the power and adaptability of the ChatGPT-4 model in understanding and working with complex file formats like the SWMM5 input file.

> First test - we will do something simple - change the outfall node name.

My prompt is "Change the outfall name to OutfallTwo" It changes the outfall name and the subcatchment section where it drains to the original outfall 2.

**Second test** - can it make changes to the inp file from outside information suech as Soil Class? My prompt is "now change the subcatchment id to w and wo BioCell, change the manning's n to default swmm5 values, and use infiltration for soil class b" It makes the asked-for changes as shown below.

> **Fourth test** - "update the coordinates so the new Subcatchments are offset by 500 and 1000, respectively"

> **Fifth Test** - Change the name of the Raingage and make copies of the Subcatchments. The prompt is "make two copies of the Subcatchments and use a prefix of Scen1 and Scen12 respectively, change the raingage ID to rainStorm" It does it correctly.
