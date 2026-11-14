---
title: "The Steady State,  EPS, and Kinematic, Dynamic Wave Options in InfoSewer, SWMM5, InfoSWMM, ICM SWMM, and ICM INFOWORKS"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/steady-state-eps-kinematic-dynamic-wave-options-swmm5-dickinson-x3uhe
created: "2024-07-28 00:51"
published: "2024-07-28 02:23"
words: 1339
export_sha256: f050c349d719cef1bb05823957fff7d19899d9ee2e4c1aa177bbbbcedda8c9be
---
# The Steady State,  EPS, and Kinematic, Dynamic Wave Options in InfoSewer, SWMM5, InfoSWMM, ICM SWMM, and ICM INFOWORKS

![The Steady State, EPS, and Kinematic, Dynamic wave options in InfoSewer, SWMM5, InfoSWMM, ICM SWMM, and ICM INFOWORKS](https://media.licdn.com/mediaD4E12AQFP5CQFikK9gA "The Steady State,  EPS, and Kinematic, Dynamic wave options in InfoSewer, SWMM5, InfoSWMM, ICM SWMM, and ICM INFOWORKS")

The terms "Steady State," "EPS," and "Kinematic, Dynamic Wave options" refer to different types of hydraulic simulation methods used to analyze and predict the behavior of water in sewer and stormwater systems.

### 1. Steady State

- **Definition**: A steady-state simulation assumes that flow conditions do not change over time. It is used to model systems under constant flow conditions, typically representing a system snapshot under specific input conditions.

- **Application**: This method is useful for analyzing the system's capacity under peak conditions, such as during a maximum flow scenario. It simplifies the model by not considering time-dependent factors. **SWMM5, infoSWMM, and InfoSewer have Steady State. InfoSewer, in my opinion, is the best as it has good flow loading and flow splitting options.** ICM SWMM and InfoWorks have a quasi-steady state approximation

### 2. EPS (Extended Period Simulation)

- **Definition**: EPS refers to simulations that consider changes in the system over time, typically over a longer period, such as days, weeks, or months. This method accounts for variations in flow and other conditions. **Infosewer, SWMM5, InfoSWMM, ICM SWMM and ICM InfoWorks all have EPS modeling.**

- **Application**: EPS is crucial for understanding how a system responds to varying conditions, such as daily or seasonal changes in water use, rainfall, or other factors. It helps evaluate the system's long-term performance and reliability.

### 3. Kinematic, Dynamic Wave Options

These terms refer to different methods for modeling the movement of water through the system, each with varying levels of complexity and accuracy:

### Kinematic Wave:

**Description**: This is a simplified method that models flow using a one-dimensional approximation of the Saint-Venant equations, ignoring the effects of backwater, surcharge, and downstream controls. **Only SWMM5 and InfoSWMM have KW routing.**

- **Application**: It's suitable for systems where backwater effects are negligible and flow is predominantly uniform. It's computationally less intensive and often used to simulate overland flow in catchments.

### Dynamic Wave:

- **Description**: This is the most comprehensive method for solving the full Saint-Venant equations, including the effects of inertia, pressure flow, and other complex interactions.

- **Application**: It is necessary to accurately model systems with significant backwater effects, surcharging, or complex hydraulic controls. It provides a detailed representation of the system's response to dynamic conditions, such as rapidly changing flows due to storm events. SWMM5, ICM InfoWorks, ICM SWMM, and InfoSWMM all have various solutions to the 1D St Venant equation.

> **1: InfoSewer Options**

**Two infoSewer Routing Options**

![](https://media.licdn.com/dms/image/v2/D4E12AQFvyFkwu0p7sQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1722132149236?e=1795651200&v=beta&t=8DFaNQ8iURQZFyTgUQzvnzAuX5OcNe9llavdaUvS4gs)

**Two infoSewer Routing Options**

> **2: SWMM5 Options**

![](https://media.licdn.com/dms/image/v2/D4E12AQHrXiSuqHFeQw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722131614386?e=1795651200&v=beta&t=o4JqaPOA5F34-XSAaPatn_9UTNVb1M7p7VVkWOXL0pM)

**Three SWMM5 Routing Options**

**Steady Flow** routing represents the simplest type of routing possible (actually no routing) by assuming that flow is uniform and steady within each computational time step. Thus, it simply translates inflow hydrographs at the upstream end of the conduit to the downstream end, with no delay or change in shape. The normal flow equation relates flow rate to flow area (or depth). This type of routing cannot account for channel storage, backwater effects, entrance/exit losses, flow reversal, or pressurized flow. It can only be used with dendritic conveyance networks, where each node has only a single outflow link (unless the node is a divider, in which case two outflow links are required). This routing form is insensitive to the time step employed and is only appropriate for preliminary analysis using long-term continuous simulations.

**Kinematic wave** routing method solves the continuity equation along with a simplified form of the momentum equation in each conduit. The latter assumes that the slope of the water surface equal the slope of the conduit. The maximum flow conveyed through a conduit is the full normal flow value. Any flow over this entering the inlet node is either lost from the system or can pond atop the inlet node and be re-introduced into the conduit as capacity becomes available. Kinematic wave routing allows flow and area to vary spatially and temporally within a conduit. This can result in attenuated and delayed outflow hydrographs as inflow is routed through the channel. However, this form of routing cannot account for backwater effects, entrance/exit losses, flow reversal, or pressurized flow, and it is also restricted to dendritic network layouts. It can maintain numerical stability with moderately large time steps, 1 to 5 minutes. If the effects above are not expected to be significant, this alternative can be an accurate and efficient routing method, especially for long-term simulations.

**Dynamic Wave routing** solves the complete one-dimensional Saint Venant flow equations and produces the most theoretically accurate results. These equations consist of the continuity and momentum equations for conduits and a volume continuity equation at nodes. With this routing form, it is possible to represent pressurized flow when a closed conduit becomes full so that flows can exceed the full normal flow value. Flooding occurs when the water depth at a node exceeds the maximum available depth, and the excess flow is either lost from the system or can pond atop the node and re-enter the drainage system. Dynamic wave routing can account for channel storage, backwater, entrance/exit losses, flow reversal, and pressurized flow. Because it couples the solution for both water levels at nodes and flows in conduits, it can be applied to any general network layout, even those containing multiple downstream diversions and loops. It is the method of choice for systems subjected to significant backwater effects due to downstream flow restrictions and with flow regulation via weirs and orifices. This generality comes at the price of using much smaller time steps in an order of thirty seconds or less (SWMM can automatically reduce the user-defined maximum time step as needed to maintain numerical stability).

> **3: InfoSWMM Options**

**Three InfoSWMM Routing Options - the same as SWMM5.**

![](https://media.licdn.com/dms/image/v2/D4E12AQH7rBVWzgp7mg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722132227864?e=1795651200&v=beta&t=jJdj03zKpBDBxQuhltGWaoaweLpl8phQ_I414m00iHA)

**Three InfoSWMM Routing Options**

> **4: ICM SWMM Options**

**One ICM SWMM Routing option** (the default is the SWMM5 dynamic wave or 1D Steady State) can create a quasi-steady state by saving a state from a previous run and running the model for a few minutes.

![](https://media.licdn.com/dms/image/v2/D4E12AQGPoW8r_3ePiQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722132354135?e=1795651200&v=beta&t=ca1wfIfjsXg_WgWQHO66xxiE1_mhNABInmNYHi7Uh3U)

One ICM SWMM Routing option (the default is the SWMM5 dynamic wave) can create a quasi-steady state by saving a state from a previous run and running the model for a few minutes.

> **5: ICM Infoworks Options**

**One ICM InfoWorks Routing option** (the default is the ICM St Venant implicit solution) can create a quasi-steady state by saving a state from a previous run and running the model for a few minutes.

![](https://media.licdn.com/dms/image/v2/D4E12AQGmlGYj2NkfpQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722132737922?e=1795651200&v=beta&t=WmSqK65vR_Xe_rLnj3AtvxFYYe-xeu6KqA8rVRlSY6U)

**One ICM InfoWorks Routing option** (the default is the ICM St Venant implicit solution) can create a quasi-steady state by saving a state from a previous run and running the model for a few minutes.

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
