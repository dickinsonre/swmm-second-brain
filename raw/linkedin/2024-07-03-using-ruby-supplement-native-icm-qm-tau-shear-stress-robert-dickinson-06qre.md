---
title: "Using Ruby to supplement Native ICM QM Tau or Shear Stress"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-supplement-native-icm-qm-tau-shear-stress-robert-dickinson-06qre
created: "2024-03-23 21:15"
published: "2024-07-03 09:30"
words: 658
export_sha256: 25d3c1d4c14eb71408f2c2b6f0032784eb5fcf65072188e9a674c79369dd9dc4
---
# Using Ruby to supplement Native ICM QM Tau or Shear Stress

![](https://media.licdn.com/mediaD4E12AQF0cWQxVaNQBw)

This Ruby code processes the results of an ICM Infoworks run, focusing on specific links within the model. It employs a user-defined equation for selected links to compute the shear stress at upstream and downstream ends. This approach allows customized shear stress (tau) calculations without relying on the QM (Quality Model) module. Users can implement their tau equations, tailoring the analysis to their requirements.

• The Ruby script operates within the WSApplication framework for an ICM Infoworks network

• Key functions:

\- Calculates hydraulic gradients and depths in conduits

\- Allows the user to choose between USA or SI units for Tau calculation

\- Retrieves and counts time steps in the current network

\- Calculates time intervals between steps (in seconds and minutes)

• Data handling:

\- Uses specific result field names ('HYDGRAD', 'us_depth', 'ds_depth')

\- Fetches data from selected nodes

• Calculation process:

\- Iterates over selected objects in the network

\- Calculates Tau values (shear stress) at upstream and downstream points

\- Adjusts depth values and considers chosen unit system for density calculation

\- Collects Tau values across time steps for statistical analysis

> **Shear Stress is automatically calculated if you use the QM or Quality Model**

![](https://media.licdn.com/dms/image/v2/D4E12AQHHGvJw5P6v4w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1719995997951?e=1795651200&v=beta&t=eDwMoVysnrlGxcnfGKQF-8iJXLC0gxHDbdjpltdhqco)

Shear Stress is automatically calculated if you use the QM or Quality Model in ICM InfoWorks.

> **Ruby Output for Upstream and Downstream with user-defined tau equation**

![](https://media.licdn.com/dms/image/v2/D4E12AQGfIIfKhkFrAQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1719998293421?e=1795651200&v=beta&t=MI2FcWNwAv1pNBYFu4e14jX8gSaNmGVi4RzvhLDdXCA)

Ruby Output for Upstream and Downstream with user-defined tau equation

> **Shear Stress based on Average Depth (you can modify to suit your need)**

For open channel flow or partially filled pipes, the shear stress (τ) can be calculated using the following equation:

τ = γ *R* S

Where: γ = specific weight of the fluid R = hydraulic radius S = energy slope (often approximated by the pipe slope for uniform flow)

The shear stress (τ) in open channel water, considering the average depth, is calculated using the following formula (using depth for hydraulic radius):

τ = ρ *g* D \* S

Where:

- τ is the Shear Stress (N/m²)

- ρ is the Density of Water (N/m³, typically 1000 kg/m³ for fresh water at room temperature)

- g is the Acceleration due to Gravity (9.81 m/s²)

- D is the Average Water Depth (m)

- S is the Water Surface Slope (dimensionless, it's the change in water surface elevation per unit length)

This formula is typically used in open channel flow, such as rivers and streams, and assumes steady, uniform flow. The shear stress represents the force the moving water exerts on the channel bed.

This formula is based on the depth-slope product concept, which is widely used in river engineering, stream restoration, sedimentology, and fluvial geomorphology\[1,2\].

\[1\]: [Shear Stress - Oregon State University](https://www.fsl.orst.edu/geowater/FX3/help/8_Hydraulic_Reference/Shear_Stress.htm)

\[2\]: [https://ponce.sdsu.edu/critical_shear_stress_versus_critical_velocity.html](https://ponce.sdsu.edu/critical_shear_stress_versus_critical_velocity.html)

![](https://media.licdn.com/dms/image/v2/D4E12AQFyQgDOmQUy9Q/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1719832926407?e=1795651200&v=beta&t=x3UArR9JdRU7nZXuLA45aw5wQOFbWLStDl8uXnYakhc)

Shear Stress - Oregon State University

> **Location of the Ruby Code**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0153 - Tau or Shear Stress non-QM Calculations](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0153%20-%20Tau%20or%20Shear%20Stress%20non%20QM%20%20Calculations)

> **Annotated Ruby Code**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, ready to inform and help when specific circumstances arise.*
