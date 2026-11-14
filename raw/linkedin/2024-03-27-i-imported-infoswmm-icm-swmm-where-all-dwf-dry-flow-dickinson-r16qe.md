---
title: "I imported InfoSWMM to ICM SWMM - Where are all of the DWF (Dry Weather Flow) Allocator Rows?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/i-imported-infoswmm-icm-swmm-where-all-dwf-dry-flow-dickinson-r16qe
created: "2024-03-27 20:24"
published: "2024-03-27 21:16"
words: 1677
export_sha256: 93507a16264264ee6923b2a87189508a8de163e3317cf4475a9e052626a91470
---
# I imported InfoSWMM to ICM SWMM - Where are all of the DWF (Dry Weather Flow) Allocator Rows?

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![DWF Rows 2 onwards are under the Additional DWF Category](https://media.licdn.com/mediaD5612AQHPWgPq9OuXlg "DWF Rows 2 onwards are under the Additional DWF Category")

**Edition 24** - EPASWMM5 is restricted to only **one Dry Weather Flow (DWF) per node**, which can be limiting when modeling complex urban drainage systems. In contrast, InfoSWMM, through its GIS-based DWF Allocator tool, introduced the capability to allocate multiple DWF inputs per node, expanding the model's adaptability to simulate real-world conditions more accurately. This feature is further enhanced by additional simulation engine capabilities that support more than one row of DWF per node, allowing for a more detailed and nuanced representation of dry weather contributions to the system.

Building on the advancements in InfoSWMM, ICM SWMM incorporates these enhanced engine features, offering similar flexibility in handling multiple DWF inputs. However, within the ICM SWMM user interface, the original EPASWMM5 limitation is mirrored by designating a single DWF per node as DWF Baseflow, while supplementary DWF inputs are categorized under Additional DWF as Baseline Flow. Both primary and additional DWF inputs can utilize daily, weekend, weekday, and monthly patterns for a comprehensive temporal analysis. Importantly, these patterns, once defined in InfoSWMM, can be seamlessly transferred to an ICM InfoWorks Network, ensuring consistency in modeling approaches across platforms. 

![](https://media.licdn.com/dms/image/v2/D4E12AQGhtdxjADkv3g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711572090857?e=1795651200&v=beta&t=2Dc-We8fMMBYCpKKZ6Y-y8lc9JUOPTRdmR4W7cO8NYA)

InfoSWMM mainly due to the DWF Allocator tool can have more than one row of DWF per node - which is more than than the one allowed in native SWMM5. ICM SWMM also has more than one row of DWF but the extra rows are in the Additional DWF Field

 Solution:

EPASWMM5 is restricted to only **one Dry Weather Flow (DWF) per node**, which can be limiting when modeling complex urban drainage systems. In contrast, InfoSWMM, through its GIS-based DWF Allocator tool, introduced the capability to allocate multiple DWF inputs per node, expanding the model's adaptability to simulate real-world conditions more accurately. This feature is further enhanced by additional simulation engine capabilities that support more than one row of DWF per node, allowing for a more detailed and nuanced representation of dry weather contributions to the system.

Building on the advancements in InfoSWMM, ICM SWMM incorporates these enhanced engine features, offering similar flexibility in handling multiple DWF inputs. However, within the ICM SWMM user interface, the original EPASWMM5 limitation is mirrored by designating a single DWF per node as DWF Baseflow, while supplementary DWF inputs are categorized under Additional DWF as Baseline Flow. Both primary and additional DWF inputs can utilize daily, weekend, weekday, and monthly patterns for a comprehensive temporal analysis. Importantly, these patterns, once defined in InfoSWMM, can be seamlessly transferred to an ICM InfoWorks Network, ensuring consistency in modeling approaches across platforms.

![](https://media.licdn.com/dms/image/v2/D4E12AQEkmC2oSEubGg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711572145568?e=1795651200&v=beta&t=n5Xqsj_rtflYgHH37DCBoUYo4imdMPcnxZIPKRkoG88)

InfoSWMM DWF DB Table

ICM SWMM to InfoSWMM DWF DB Table In the node dialog, ICM SWMM Additional DWF for DWF more than one loading per node

![](https://media.licdn.com/dms/image/v2/D4E12AQHAeY-eAUMVqA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711572031477?e=1795651200&v=beta&t=moLp0LYFokvZNTNRzhKNRgiDfU8Sa6OiARjcadZQcck)

ICM SWMM to InfoSWMM DWF DB Table In the node dialog, ICM SWMM Additional DWF for DWF more than one loading per node

> 2/ SWWMM5 and ICM SWMM

\[embedded item\]

> **3/ Employing SWMM Networks within InfoWorks ICM. 🌐**

**Embarking on the Digital Odyssey:** Setting up SWMM Networks in InfoWorks ICM 🚀 In this digital era, akin to an interstellar journey, the first milestone is to incorporate a SWMM network into the database, akin to discovering a new galaxy through the Explorer window. Then, unveil this newly added SWMM network on the GeoPlan, much like unveiling a cosmic map. 🌌

**Crafting the Digital Cosmos:** Data Addition and Model Parameterization 🌟 As one crafts constellations in the sky, data is artfully added to the network. The process resembles aligning stars, where various options for model parameters are set - a crucial step much like aligning planets in a solar system. Pay particular attention to ensuring that network flow units and force main equations are correctly aligned. 🌠

**The Galactic Network:** Adding Objects and Defining Events 🛰️ Just as a galaxy is composed of diverse celestial bodies, the SWMM network is built with various objects - nodes, links, subcatchments, points, and polygons. These can be added through different methods, reflecting the diverse ways celestial objects form in the universe. Additionally, time-varying event data, the pulsars of our network, need to be specified, lending dynamic variability to our model. 🌍

**Intertwining Fates:** Linking Rainfall Events and Regulator Structures 🌧️ In the tapestry of our network galaxy, rainfall events act as nebulae, shaping the formation of our network. Ensure these are linked to the applicable network objects. Similarly, if regulator structures are the black holes of our system, define their control rules meticulously using the Control Rule Editor. 🌦️

**The Snowy Comets:** Specifying Snow Parameters ❄️ If your simulation orbits around modeling snow melt, do not forget to specify the snow parameters, akin to tracking comets in your cosmic model. 🌬️

**The Dimensional Dance:** Inclusion of 2D Simulations 🌈 For those daring to explore further dimensions, include a 2D simulation alongside the 1D one. This requires the creation of a 2D mesh, a step akin to unfolding the fabric of space-time. 🌀

**Final Preparations:** Validation and Simulation Settings 🛠️ Before launching this cosmic odyssey, validate the network. Correct any errors, much like fixing a spacecraft before a launch. Finally, set the parameters for your SWMM Run and embark on this digital journey. 🚀

**The Journey's Fruit:** Running Simulations and Harvesting Data 🌍 With dynamic wave routing at the heart of these simulations, akin to the pulsating core of a star, run your simulations. Then, observe the results, much like an astronomer gazing upon the outcomes of cosmic events. 📊

In this journey through the digital cosmos of SWMM Networks in InfoWorks ICM, we see a parallel to exploring the vast, mysterious universe. Each step, from setting up the network to running simulations, is akin to navigating through the endless expanse of space, uncovering the secrets held within our own digital universe. 🌌🔭

> **4/ A Conversion Poem**

> **5/ Diving Deep into Innovyze Tools: ICM InfoWorks, ICM SWMM, and ICM Validation 💧🌐🛠️**

![](https://media.licdn.com/dms/image/v2/D4E12AQG4MGg6AOKj7Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1711628472945?e=1795651200&v=beta&t=03XzhXUFW_XEEziSodRF3mg0saLDYp7Io1yr4LyeYKM)

Diving Deep into Innovyze Tools: ICM InfoWorks, ICM SWMM, and ICM Validation 💧🌐🛠️

> **6/ Excel and ICM Infoworks**

 When managing complex datasets and performing sophisticated analyses, the choice of tool is crucial. Let's dive into why using an Excel Spreadsheet might fall short compared to a robust modeling platform like ICM InfoWorks. 🛠️🔍

1.  **Scope & Complexity**: Excel is primarily designed for data tabulation and basic calculations. 📊 While it's versatile, it's not optimized for intricate hydrological and hydraulic modeling, which platforms like ICM InfoWorks are explicitly designed for. 🌊🔧

2.  **Data Handling**: As your dataset grows, Excel can become slow and unresponsive. 🐢 ICM InfoWorks can handle vast datasets more efficiently, ensuring smooth operation even with intricate models. 🚀📈

3.  **Accuracy**: While Excel can perform calculations, errors can easily creep in. 🐛 Whether from human error in formula creation or from the inherent limitations of Excel's computation capabilities, these errors can have significant consequences. ICM InfoWorks provides precise tools tailored for water modeling. 🎯🔬

4.  **Visualization**: Excel offers basic charting tools 📉, but ICM InfoWorks provides comprehensive visualization options like 1D and 2D modeling, helping users better understand and interpret their data. 🌐🎨

5.  **Scalability**: As projects grow, Excel sheets can become unwieldy and challenging to manage. 🌲🌳 On the other hand, ICM InfoWorks is designed to scale, accommodating larger and more complex projects seamlessly. 🏢🌆

6.  **Interactivity**: ICM InfoWorks offers dynamic modeling capabilities, allowing for real-time adjustments and simulations. 🔄 With Excel, you'd have to manually adjust parameters and recalculate, which can be time-consuming. ⏳

7.  **Collaboration**: While Excel allows for collaboration, ICM InfoWorks offers tools tailored for team-based water modeling projects. 🤝 This ensures everyone is on the same page and can collaborate efficiently. 👩‍💻👨‍💻

8.  **Integration**: ICM InfoWorks can integrate with other software and tools, providing a more holistic approach to water management. 🔄 Excel might require manual data imports and exports, which can be tedious. 📤📥

In essence, while Excel is a versatile tool for a wide range of applications, when it comes to specialized tasks like water modeling, platforms like ICM InfoWorks offer a more comprehensive, accurate, and efficient solution. 🌟👌

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
