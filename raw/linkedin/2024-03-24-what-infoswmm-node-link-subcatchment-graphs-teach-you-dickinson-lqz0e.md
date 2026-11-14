---
title: "What InfoSWMM Node, Link, and Subcatchment Graphs Teach You About the SWMM5 Engine"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/what-infoswmm-node-link-subcatchment-graphs-teach-you-dickinson-lqz0e
created: "2024-03-24 20:36"
published: "2024-03-24 21:30"
words: 1576
export_sha256: f595cca986884d6acdec2548dc86c4a98903f276fb6e63d3d1b9d4acb1f1fc43
---
# What InfoSWMM Node, Link, and Subcatchment Graphs Teach You About the SWMM5 Engine

![What InfoSWMM Node, Link and Subcatchment Graphs Teach you about the SWMM5 Engine](https://media.licdn.com/mediaD4E12AQFiPcIuf9ocyw "What InfoSWMM Node, Link and Subcatchment Graphs Teach you about the SWMM5 Engine")

The InfoSWMM engine through its graphs and tables shows the inner workings of the SWMM5 engine more than native SWMM5.

Subcatchment Table: The subcatchment table lists 15 parameters and variables that describe the physical characteristics, hydrological processes, and pollutant buildup/washoff in SWMM5 subcatchments. These include rainfall, runoff, evaporation loss, infiltration loss, snow depth, groundwater flow, groundwater elevation, groundwater soil moisture, and different types of runoff (e.g., impervious with and without depression storage, and pervious). The table also includes depths of water on different surface types and the total ponded depth.

Node Table: The node table lists 10 parameters that describe the hydraulic conditions and flow components at nodes within a SWMM5 model. These include head (water surface elevation), lateral inflow, total inflow, flooding, pressure, volume, surface area, Rainfall-Derived Infiltration and Inflow (RDII), and Dry Weather Flow (DWF). The table also includes the depth of water in the node.

Link Table: The link table lists 20 parameters that describe the hydraulic conditions and flow characteristics within conduits in a SWMM5 model. These include flow rate, depth, velocity, capacity, surcharge ratio, absolute depth ratio, Hydraulic Grade Line (HGL), flow volume, Froude number, velocity-depth product, top width, entry loss, exit loss, seepage rate, and upstream and downstream depths, velocities, and flow areas.

> **1/ SWMM5 Subcatchments**

InfoSWMM shows 15 output variables to show runoff, infiltration, evaporation, snow depth, groundwater flow, and, most importantly, runoff and surface ponding on the three SWMM5 Runoff Surfaces: impervious with depression storage, impervious without depression storage, and pervious area.

1.  Rainfall ⛈️ - The amount of water that falls from the sky as precipitation.

2.  Runoff 🌊 - The amount of water that flows over the land surface after rainfall or snowmelt.

3.  Evaporation Loss ☀️ - The loss of water from the land surface and water bodies to the atmosphere through evaporation.

4.  Infiltration Loss 💧 - The movement of water from the land surface into the soil.

5.  Snow Depth ❄️ - The depth of snow accumulated on the land surface.

6.  Ground Water Flow 🚰 - The movement of water through the saturated zone beneath the water table.

7.  Ground Water Elevation 📈 - The height of the water table above a reference datum.

8.  Ground Water Soil Moisture 💦 - The amount of water stored in the soil below the water table.

9.  No-Depression Impervious Runoff 🏙️ - Runoff from impervious areas that do not have depression storage.

10. Depression Impervious Runoff 🌀 - Runoff from impervious areas that have depression storage.

11. Pervious Runoff 🌿 - Runoff from pervious areas such as lawns, parks, and undeveloped land.

12. No-Depression Impervious Depth 📏 - The depth of water on impervious areas without depression storage.

13. Depression Impervious Depth 📐 - The depth of water stored in depressions on impervious areas.

14. **Pervious Depth** 🌱 - The depth of water on pervious areas.

15. **Total Ponded Depth** 🌊 - The total depth of water (both pervious and impervious) stored on the land surface.

These parameters help characterize the hydrological processes and conditions within a subcatchment in SWMM5, enabling the modeling of runoff generation, infiltration, evaporation, and groundwater interactions over three runoff surfaces.

![](https://media.licdn.com/dms/image/v2/D4E12AQE8c_Xgq3zJDg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711312969994?e=1795651200&v=beta&t=51pMpdH5aII6owaf6L47ZkbfJGJkGtBUO6pzvVuo-FI)

SWMM5 Subcatchments

> **2/ SWMM5 Nodes**

InfoSWMM shows 10 output variables for nodes showing the different components of flow to the node, upstream link flow, RDII flow, Lateral flow from subcatchments, DWF and the depth, volume, and area expected from a link node model. Note = volume is only shown for a storage node.

1\. Depth 📏 - The vertical distance between the bottom of the node and the water surface.

2\. Head 🔝 - The water surface elevation in the node, measured from a reference datum.

3\. Lateral Inflow 🔀 - The flow entering the node from sources other than upstream nodes, such as direct inflow from subcatchments or external hydrographs.

4\. Total Inflow 📥 - The sum of all inflows to the node, including lateral inflow and flow from upstream nodes.

5\. Flooding 🌊 - Water spills out of the node when the water surface elevation exceeds the maximum depth.

6\. Pressure 🗜️ - The force exerted by the water on the node walls and bottom, related to the water depth and specific weight.

7\. Volume 📦 - The volume of water stored in the node, calculated based on the water depth and the node's geometry.

8\. Surface Area 🟨 - The area of the water surface in the node, which can change with water depth for irregular cross-sections.

9\. RDII Flow 🌧️ - The flow entering the node from Rainfall-Derived Infiltration and Inflow (RDII), which represents the infiltration of rainfall into the sanitary sewer system.

10\. DWF Flow🚰 The Dry Weather Flow (DWF) entering the node typically represents the sanitary sewage flow from households and businesses during periods with and without rainfall.

These parameters help describe the hydraulic conditions and flow components at nodes within a SWMM5 model. They are essential for understanding the flow balance, water depths, and potential flooding at each node in the system.

![](https://media.licdn.com/dms/image/v2/D4E12AQH_vRlIXWsKWg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711313582110?e=1795651200&v=beta&t=uS7OmTjm7QIJMu7fL4-EPBeLoAGsLWParp8dJovdQFw)

SWMM5 Nodes

> **3/ SWMM5 Links**

InfoSWMM shows 20 output variables for nodes showing the different components of flow and hydraulic data used to compute the flow during a simulation. SWMM5 reports only one flow but uses the depth, area, width, Froude number and hydraulic radius to calculate the St Venant Flow.

1.  Flow 🌊 - The rate of water movement through the conduit, typically measured in volume per unit time.

2.  Depth 📏 - The vertical distance between the bottom of the conduit and the water surface.

3.  Velocity 💨 - The speed of water flow through the conduit, typically measured in distance per unit time.

4.  Capacity 🎯 - The maximum flow rate that the conduit can convey without surcharging or flooding.

5.  d/D Surcharged 🚨 - The ratio of the water depth to the conduit diameter when the conduit is flowing full and under pressure.

6.  d/D Absolute 📊 - The ratio of the water depth to the conduit diameter, regardless of the flow condition.

7.  Flow HGL 📈 - The Hydraulic Grade Line representing the water surface elevation along the conduit.

8.  Flow Volume 📦 - The volume of water stored in the conduit, calculated based on the water depth and the conduit's geometry.

9.  Froude Number 🌀 - A dimensionless number describing the flow regime, indicating whether the flow is subcritical, critical, or supercritical.

10. Velocity'Depth 🌪️ - The product of velocity and depth used in some hydraulic calculations.

11. Top Width 🌉 - The width of the water surface at the top of the conduit.

12. Entry Loss 🔙 - The energy loss due to the flow entering the conduit, typically caused by the contraction of the flow area.

13. Exit Loss 🔜 - The energy loss due to the flow exiting the conduit, typically caused by the expansion of the flow area.

14. Seepage Rate 💧 - The rate at which water infiltrates through the conduit walls or bottom, typically measured in volume per unit area per unit time.

15. Upstream Depth 🔼 - The water depth at the upstream end of the conduit.

16. Downstream Depth 🔽 - The water depth at the downstream end of the conduit.

17. Upstream Velocity 🔼💨 - The water velocity at the upstream end of the conduit.

18. Downstream Velocity 🔽💨 - The water velocity at the downstream end of the conduit.

19. Upstream Flow Area 🔼🟨 - The cross-sectional area of the flow at the upstream end of the conduit.

20. Downstream Flow Area 🔽🟨 - The cross-sectional area of the flow at the downstream end of the conduit.

![](https://media.licdn.com/dms/image/v2/D4E12AQG9-IQfFWxsug/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711314814985?e=1795651200&v=beta&t=n2jgLT5FvqZtGWoExQErzC1Gqg9Gf9SjDvSfU3e3hhI)

SWMM5 Links

![](https://media.licdn.com/dms/image/v2/D4E12AQFf4M3hg0_Nyw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1711315021918?e=1795651200&v=beta&t=H2Fe-aXDHayszBnyNHA8uUb4_g1Mq1bfGan4d7v6N_A)

20 SWMM5 Link Output Variables

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
