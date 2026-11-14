---
title: "From SWMM5 and ICM to InfoWater Pro 2024: Insights and Lessons from Daily Standups with my IWP Programming CoWorkers"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/from-swmm5-icm-infowater-pro-2024-insights-lessons-daily-dickinson-yj1ge
created: "2023-12-02 17:27"
published: "2023-12-02 17:59"
words: 819
export_sha256: 9ef0857d1361666717c3700bee0e55b4e23ec382751363f19b9784f273c9294c
---
# From SWMM5 and ICM to InfoWater Pro 2024: Insights and Lessons from Daily Standups with my IWP Programming CoWorkers

![InfoWater Pro 2024.3 Run Manager and Model Explorer](https://media.licdn.com/mediaD4E12AQGQwFKEyyY9bA "InfoWater Pro 2024.3 Run Manager and Model Explorer")

> Introduction

I participate in a daily stand-up meeting with my InfoWater Pro colleagues, a group brimming with DevOps and programming expertise. This opportunity allows me to stay abreast of the latest developments, enhancements, and innovations within InfoWater Pro as they unfold, undergo testing, and are conceptualized. The software, a potent and intricate modeling tool within **ArcGIS Pro**, occasionally stirs a touch of melancholy in me as I ponder the potentialities of what **InfoSWMM Pro** might have embodied. Nevertheless, my affection for **ICM SWMM**, augmented with **Ruby**, remains steadfast, and I frequently find myself writing about it with enthusiasm. Concurrently, my usage of InfoWater Pro is not just habitual but filled with admiration for its sophisticated execution of the enhanced **EPANET** engine.

> InfoWater Pro 2024.3

The latest update to InfoWater Pro brings enhanced diagnostic capabilities 🛠️. The Hydraulic Diagnostics Report now includes additional warnings for pumps, valves, hydraulic disconnections, and temporarily closed pipes next to tanks during simulations, all conveniently displayed in the Hydraulic Diagnostic tab. This tab neatly organizes the warnings with types and counts for easy understanding. Moreover, the integration with Info360 has been deepened, offering two innovative options for pattern mapping 🔄. Users can now utilize direct virtual sensor data from Info360 for SCADA events, allowing models to dynamically adapt to recorded conditions. Additionally, existing InfoWater Pro simulation pipe results can be uploaded to Info360 Asset, streamlining data management and analysis.

A new design fire flow algorithm 🚒 has been introduced, ensuring faster convergence and more accurate results, particularly with max velocity thresholds. This feature comes with an optional checkbox, giving users the flexibility to toggle between the new method and the previous one. The System Demand Graph Report is now more comprehensive, including Unsatisfied Demand and Emitter Flow data, plus additional charts for pressure-dependent simulations 📊. The pressure-dependent demand engine has been updated in line with the anticipated EPANET 2.3 release, ensuring compliance and improved performance. Furthermore, automatic generation of selection sets for fire-flow excluded elements and disconnected elements post-failed runs adds to the software’s robustness. Lastly, saving Map Display items now defaults to the last element type saved, enhancing user experience and efficiency.

![](https://media.licdn.com/dms/image/v2/D4E12AQHZCpiykoK5CA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1701538313208?e=1795651200&v=beta&t=cU_y6jcvgR8a2ArwVk_cTAG73i2I_QPwbDlB6m6kZQ0)

Control Rules for an InfoWater Pro Networ

> InfoWater Pro in General

InfoWater Pro offers direct ARCGIS PRO integration 🌐, enabling engineers and GIS professionals to work simultaneously on the same integrated platform with continuity 🔄 and fluidity 💧. This integration allows for an opportunity to command powerful GIS analysis and hydraulic modeling in a single environment using a single dataset, providing continuity in data handling 📊 and model fluidity. You can create, edit, modify, run, map, analyze, design, and optimize your water network models with uniformity and instantly review, query, and display simulation results with clarity from within ArcGIS Pro. 

InfoWater Pro's powerful ArcGIS Pro integration features include:

- Build/Run Network Model in ArcGIS Pro™ with fidelity and utility 🔧.

- Provide Native ArcGIS Pro™ Model-Building Tools, ensuring continuity and usability 🛠️.

- Construct/Update Models Directly from Geodatabase and Geometric Network or Any External Data Source with adaptability and flexibility 💡.

- Allow Complete or Filtered Data Exchange on Geometric and/or Non-Geometric Data with Geodatabase or RDBMS, maintaining data integrity and fluidity 🔄.

- Treat Pumps and Valves as Nodes (Points) with specificity ⚙️.

- Create/Edit Multiple Scenarios in the Same Geodatabase with versatility 🌟.

- View fully Animated Extended Period Simulation (Dynamic) Results Sequentially Using VCR-Style Controls Directly in ArcGIS Pro™, demonstrating continuity and clarity 🎥.

- Generate Contours, Graphs, and Tables of Modeling Results Directly in ArcGIS Pro™ with precision and accuracy 📈.

- Combine Input and Output Attribute Tables for unified data management 📑.

- Use Relational Database and Geodatabase to Store Model Data with security and stability 🔒.

- Fully Automate GIS Data Exchange with ESRI Data Sources (e.g., Valve Status) for efficiency and productivity 🚀.

- Pick any GIS Attributes Automatically Without Mapping any Fields, ensuring simplicity and utility 👌.

- Automatically Publish Simulation Results to Enterprise Geodatabase and/or RDBMS for accessibility and connectivity 🌍.

- Fully Compatible with Intergraph GeoMedia and GeoMedia Professional, ensuring compatibility and interoperability 🔗.

These features underscore InfoWater Pro's commitment to providing a seamless and integrated solution for water network modeling, emphasizing continuity, clarity, and uniformity in GIS integration and hydraulic analysis 🌊💻.

![](https://media.licdn.com/dms/image/v2/D4E12AQGQrskfKixOkg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1701538524730?e=1795651200&v=beta&t=0f3Q7qCw5nCiXswa1KvePCD9jO7I3BQ-LMDre2nW8Ro)

Random GPT4 Simulation Modeling Imaginative Image

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
