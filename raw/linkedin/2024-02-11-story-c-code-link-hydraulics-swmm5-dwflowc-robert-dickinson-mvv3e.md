---
title: "A Story about the C-Code Link Hydraulics of SWMM5 or dwflow.c"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/story-c-code-link-hydraulics-swmm5-dwflowc-robert-dickinson-mvv3e
created: "2024-02-10 23:34"
published: "2024-02-11 02:59"
words: 6356
export_sha256: 085a41554762ccfa36b5d0df7d077fd1794771e372434660f2e4ff192a459f14
---
# A Story about the C-Code Link Hydraulics of SWMM5 or dwflow.c

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![A Story about the C-Code Link Hydraulics of SWMM5 or dwflow.c](https://media.licdn.com/mediaD4E12AQGSjpDXejXw8Q "A Story about the C-Code Link Hydraulics of SWMM5 or dwflow.c")

The SWMM5 solution of the 1D St. Venant Equation has 13 sections: Find the Conduit flow, Initial conditions, Actions for Zero Flow, St Venant Terms, St Venant Momentum Terms, Flow Limitation Checks, Details for Froude, Area weights and Velocity, Find the link surface area for the attached Nodes, Get the Flow Class, Check Normal Flow, Local Losses, Get Slot Width, Width, Area, and Hydraulic Radius, Force Main Assumptions.

## 1/ Find the Conduit Flow by solving the 1D St Venant Equation Overview

The dwflow_findConduitFlow function is a detailed and complex procedure designed to update the flow through a conduit link in a hydraulic simulation, such as in urban drainage or sewer systems. It incorporates a finite difference solution of the continuity and momentum (Saint-Venant) equations, which describe the flow of water in open channels and closed conduits. The function takes into account various hydraulic principles and conditions to ensure an accurate simulation of water flow. Here's a breakdown of how it operates:

![](https://media.licdn.com/dms/image/v2/D4E12AQG542j7TsTG8g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1707619921466?e=1795651200&v=beta&t=V4QaB3KH7RgrNaDpvRhcWoYDNtMUeFXW44S32zaqX7g)

Picard Iterantions

### Inputs:

- **j**: The index of the conduit link whose flow is to be updated.

- **steps**: The number of iteration steps taken so far in the simulation process.

- **omega**: The under-relaxation parameter used to stabilize the iterative solution process by mixing a portion of the previous iteration's result with the current iteration's result.

- **dt**: The time step in seconds for the simulation iteration.

### Process and Calculations:

1.  **Initialization**: Sets up local variables for hydraulic calculations, including geometric properties (e.g., invert elevations, flow depths, hydraulic radius), flow quantities from the previous iteration and time step, and flags indicating special flow conditions (e.g., full flow, closed conduit).

2.  **Adjustment for Control Actions**: Determines if the conduit is closed based on control settings.

3.  **Head Calculations**: Calculates the hydraulic head at both the upstream and downstream ends of the conduit, taking into account node elevations and flow depths.

4.  **Flow Area and Hydraulic Radius**: Computes the cross-sectional area and hydraulic radius at both ends of the conduit and at the midpoint, adjusting for any peculiarities like the Preissmann slot.

5.  **Flow Conditions**: Checks for special conditions such as the conduit flowing full or being completely dry, and sets the flow accordingly.

6.  **Velocity and Froude Number**: Calculates the flow velocity based on the previous flow estimate and uses it to compute the Froude number, which indicates flow regime (subcritical or supercritical).

7.  **Momentum Equation Terms**: Computes various terms of the momentum equation, including friction slope, energy slope, inertial terms, local losses, and losses due to evaporation and seepage.

8.  **Flow Calculation**: Combines the momentum equation terms to calculate the new flow rate, applying under-relaxation and checking against flow limitations (e.g., user-specified flow limits, flap gate conditions).

9.  **Final Adjustments**: Ensures the calculated flow does not cause unrealistic conditions, such as flow out of a dry node, and updates the conduit's flow, area, depth, and volume for the current iteration.

### Outputs:

While the function signature does not explicitly specify output parameters (due to being a void function), it effectively updates the flow rate (q) and other related hydraulic properties of the conduit identified by index j within the global data structures used by the simulation.

## 2/ Set Up the St Venant Solution

This code snippet is part of a larger function designed to update and calculate the flow through a conduit in a hydraulic simulation system. It performs a series of steps to adjust and calculate various hydraulic parameters based on the current and previous states of flow. Here's a breakdown of what each section does:

### Adjusting Conduit Status

- **Control Action Adjustment**: The conduit's status (open or closed) is adjusted based on control settings. If Link\[j\].setting is 0, the conduit is marked as closed (isClosed = TRUE).

### Retrieving Flow and Hydraulic Data

- **Flow Data**: Retrieves flow data from the last time step (qOld) and the previous iteration (qLast), adjusting for the number of barrels (parallel paths in the conduit) to normalize the flow rate.

- **Evaporation and Seepage Loss Rates**: Initializes evaporation and seepage loss rates to 0.0 for the current iteration, indicating no losses are initially considered.

### Hydraulic Heads and Depths

- **Hydraulic Heads**: Calculates the hydraulic heads (h1 and h2) at the upstream and downstream ends of the conduit based on node elevations and flow depths.

- **Flow Depths**: Determines the unadjusted flow depths (y1 and y2) at both ends of the conduit. These depths are adjusted to not exceed the conduit's full depth unless the surcharge method involves a slot, allowing for deeper flow.

### Hydraulic Parameters Calculation

- **Surface Area Contributions**: Calls findSurfArea to calculate the surface area contributions to upstream and downstream nodes based on the flow estimate from the previous iteration.

- **Cross-sectional Areas and Hydraulic Radius**: Calculates the cross-sectional areas (a1, a2, aMid) and hydraulic radius (r1, rMid) at the upstream end, downstream end, and midpoint of the conduit. These calculations account for the presence of a surcharge slot if applicable.

### Key Concepts and Calculations

- **Surcharge and Slot Width**: Determines if a surcharge slot's width should be considered in the calculations, which affects the flow area and hydraulic radius when the conduit is flowing under surcharged conditions.

- **Area from Previous Step**: Uses the flow area from the previous time step (aOld) in calculations, ensuring continuity and stability in the simulation.

- **Courant-modified Length**: Uses a modified length of the conduit (length), potentially adjusted for Courant conditions, rather than the actual physical length. This adjustment can help stabilize the numerical simulation by accounting for the speed of wave propagation relative to the time step size.

## 3/ Actions for Zero Flow

This code snippet represents a crucial decision-making step in a hydraulic simulation process, specifically dealing with the calculation of flow through a conduit under various conditions. It outlines how the simulation should proceed when the conduit is either dry or effectively closed (for instance, due to a flap gate being shut). Here's a detailed explanation of its functionality:

### Condition Checks

- The code first checks several conditions to determine if the flow through the conduit should be set to zero. These conditions include:**Dry Conditions**: If the conduit is classified as dry (DRY), upstream dry (UP_DRY), or downstream dry (DN_DRY).**Closure**: If the conduit is closed (isClosed), which could be due to control actions such as a closed valve or flap gate.**Minimal Midpoint Area**: If the cross-sectional area at the midpoint of the conduit (aMid) is less than or equal to a negligible threshold (FUDGE), indicating almost no flow capacity.

### Actions for Zero Flow

When any of the above conditions are met, indicating that no flow should occur through the conduit, the following actions are taken:

- **Average Area Calculation**: The average cross-sectional area (Conduit\[k\].a1) is calculated as the average of the upstream and downstream areas (a1 and a2), even though no flow is taking place. This step ensures that some physical characteristics of the conduit are maintained for potential future calculations.

- **Flow Reset**: The flow rates at the start (Conduit\[k\].q1) and end (Conduit\[k\].q2) of the time step, as well as the new flow rate (Link\[j\].newFlow), are set to zero.

- **Hydraulic Gradient Calculation**: The hydraulic gradient (Link\[j\].dqdh) is calculated using the gravitational constant (GRAVITY), the time step (dt), the midpoint area (aMid), the modified length of the conduit (length), and the number of barrels (barrels). This gradient is crucial for understanding the potential for flow initiation should conditions change.

- **Froude Number and New Depth**: The Froude number, indicating flow regime, is set to zero (Link\[j\].froude = 0.0) as there is no flow. The new depth (Link\[j\].newDepth) is set to the minimum of the midpoint depth (yMid) and the conduit's full depth (Link\[j\].xsect.yFull), ensuring it remains within physical limits.

- **Volume Calculation**: The new volume within the conduit (Link\[j\].newVolume) is updated based on the average area and the length of the conduit (link_getLength(j)), adjusted for the number of barrels, to reflect the potential storage volume even in the absence of flow.

## 4/ St Venant Terms Weights

This comprehensive section of code outlines the final steps in calculating the new flow through a conduit in a hydraulic modeling system, considering various hydraulic principles and control mechanisms. It integrates a multitude of factors, including velocity, Froude number, inertial damping, flow limitations, and under-relaxation techniques, to update the flow based on dynamic wave equations. Below is a detailed explanation of each part:

### Velocity and Froude Number

- **Velocity Calculation**: Determines flow velocity (v) based on the last flow estimate (qLast) and the midpoint area (aMid). Velocity is capped at a maximum value (MAXVELOCITY) to prevent unrealistic simulation outcomes.

- **Froude Number Calculation**: Calculates the Froude number, which indicates the flow regime (subcritical or supercritical). The flow class is updated based on the Froude number.

### Inertial Damping Factor (Sigma)

- Establishes an inertial damping factor (sigma) based on the Froude number to moderate the influence of inertia in the flow calculations. This factor varies, providing full damping, no damping, or a calculated damping based on the flow regime.

### Hydraulic Parameters Weighting

- Adjusts the upstream-weighted area (aWtd) and hydraulic radius (rWtd) based on the damping factor and the flow conditions, applying a method inspired by R. Dickinson's slope weighting.

### Momentum Equation Terms

- Calculates terms of the momentum equation, including friction slope, energy slope, inertial terms, local losses, and losses due to evaporation and seepage. These terms are integral to determining the new flow rate in the conduit.

### New Flow Calculation

- Combines the momentum equation terms to compute a new flow rate (q), adjusting for the effects of friction, slope, inertia, and losses. The calculation also includes a denominator (denom) to normalize the equation.

### Flow Limitations and Adjustments

- Applies various checks and adjustments, including inlet control for culverts, normal flow limitations, under-relaxation between iterations, user-defined flow limits, and checks against reverse flow due to closed flap gates or dry nodes. These mechanisms ensure that the flow remains within realistic and physically plausible limits.

### Final Flow and Hydraulic State Updates

- Updates the conduit's flow, area, depth, and volume with the newly calculated values, ensuring the model reflects the latest hydraulic state. Adjustments are made to account for the conduit potentially being full and to ensure flow does not occur from or to dry nodes.

### Conclusion

This section of code is critical for accurately simulating the hydraulic behavior of conduits within complex networks, such as urban drainage systems or sewer networks. It incorporates advanced hydraulic principles and empirical adjustments to model the flow dynamics realistically, accounting for various physical and operational conditions that can influence flow within a conduit. Through these calculations, the hydraulic model can predict water levels, flow rates, and system responses to various conditions, aiding in the design, analysis, and operation of water infrastructure.

### 6/ Details for Froude, Area weights and Velocity

### Velocity Calculation

- **Velocity (**v) is computed based on the last flow rate estimate (qLast) and the midpoint area (aMid). This calculation provides an average velocity for the flow within the conduit.

- If the absolute value of calculated velocity exceeds a predefined maximum velocity (MAXVELOCITY), the velocity is capped at this maximum value, with the sign (SGN) of the original velocity preserved. This step ensures that the simulation remains realistic and avoids excessively high velocities that could lead to numerical instability.

### Froude Number Calculation

- The **Froude number** is calculated using the computed velocity and the midpoint depth (yMid). The Froude number is a dimensionless quantity used in fluid dynamics to characterize the flow regime; it compares inertial forces to gravitational forces.

- If the conduit's flow is initially classified as subcritical but the calculated Froude number exceeds 1.0, the flow class is updated to supercritical. This change indicates a transition from a flow regime dominated by gravitational forces to one where inertial forces are more significant.

### Inertial Damping Factor (Sigma)

- **Inertial damping (σ)** is determined based on the Froude number to mitigate the effect of rapid changes in flow conditions, particularly in transitioning between flow regimes.

- A full damping (sigma = 0.0) is applied for Froude numbers of 1.0 or greater, indicating supercritical flow, where inertial effects dominate. No damping (sigma = 1.0) is applied for Froude numbers of 0.5 or less, representing stable, subcritical flow. For Froude numbers between these values, a linearly interpolated damping factor is used, reducing the impact of inertia as the flow transitions towards critical conditions.

### Upstream-weighted Area and Hydraulic Radius

- The **upstream-weighted area (**aWtd) and **hydraulic radius (**rWtd) are adjusted using the damping factor and a ratio (rho), which is influenced by the flow conditions and the inertial damping factor. This adjustment is a modified approach based on R. Dickinson's slope weighting, which is particularly useful in flows with significant directionality or slope influence.

- The rho factor adjusts the weighting between the upstream area and hydraulic radius versus their values at the midpoint, based on whether the flow is full and on the directionality and magnitude of the last flow estimate.

### Determination of Inertial Damping Application

- The extent of inertial damping to apply is dictated by the predefined settings (InertDamping). Depending on these settings, the damping factor can either be set to full damping, no damping, or the previously calculated damping factor. This step ensures that the model can be adjusted to simulate a range of hydraulic conditions and system responses accurately.

## 6/ St Venant Momentum Terms

This section of code advances the hydraulic modeling process by computing the new flow rate through a conduit, incorporating various hydraulic phenomena and adjustments to ensure accuracy and stability in simulations. The process involves the following steps:

### Full Inertial Damping for Surcharged Closed Conduits

- If the conduit is fully surcharged (flowing full) and it is not an open channel (!xsect_isOpen(xsect-\>type)), full inertial damping is applied (sigma = 0.0). This adjustment is crucial for modeling pressurized flow accurately, where the inertia of the flowing water does not significantly affect the pressure-driven flow.

### Momentum Equation Terms Calculation

1.  **Friction Slope Term (**dq1): Calculates the friction slope component of the momentum equation. For force mains flowing full, this is computed using the forcemain_getFricSlope function. Otherwise, it's calculated using the conduit's roughness factor and the weighted hydraulic radius (rWtd). This term accounts for the energy loss due to friction along the conduit's length.

2.  **Energy Slope Term (**dq2): Represents the slope of the energy gradient along the conduit, calculated using the gravitational constant (GRAVITY), the time step (dt), the weighted cross-sectional area (aWtd), and the difference in hydraulic heads between the upstream and downstream ends. This term is vital for energy conservation and flow dynamics analysis.

3.  **Inertial Terms (**dq3 and dq4): Account for the effects of inertia in the flow, with dq3 addressing changes in area along the conduit and dq4 considering variations in velocity. These terms are scaled by the inertial damping factor (sigma), allowing for adjustments in how strongly inertia influences the flow calculations.

4.  **Local Losses Term (**dq5): Calculates local hydraulic losses (e.g., at bends, junctions, or transitions) using the findLocalLosses function. These losses are proportional to the flow rate and inversely related to the conduit length, adding to the overall energy loss in the system.

5.  **Evaporation and Seepage Losses Term (**dq6): Accounts for additional losses due to evaporation and seepage, calculated based on a predefined loss rate, the flow velocity, and the conduit's length. This term adjusts the flow balance to reflect these external factors.

### New Flow Rate Calculation

- The new flow rate (q) through the conduit is calculated by combining these terms according to the momentum equation, adjusted for the time step and conduit characteristics. This comprehensive approach ensures that the simulation captures the complex interplay of forces and effects influencing water flow.

### Derivative of Flow with Respect to Head

- The derivative of flow with respect to hydraulic head (Link\[j\].dqdh) is computed, providing a measure of how flow rate changes with changes in hydraulic gradient. This parameter is crucial for dynamic wave modeling, allowing the simulation to adapt to varying flow conditions and hydraulic responses.

![](https://media.licdn.com/dms/image/v2/D4E12AQHt7_0AOsMSHg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1707620002992?e=1795651200&v=beta&t=gdUQ2xAZSMfi-vDIukxB8fjw28J-EcOInl3ZKeGSyUc)

Three Computational Points

## 7/ Flow Limitation Checks

This section of code finalizes the computation of flow through a conduit in a hydraulic simulation, applying several checks and adjustments to ensure the flow rate (q) adheres to physical, operational, and regulatory constraints. Here's an overview of the process and its implications:

### Flow Limitation Checks

1.  **Inlet Control Check for Culverts**: If the conduit is a culvert (indicated by a positive culvertCode) and not fully surcharged, the flow rate is potentially adjusted based on inlet control conditions using culvert_getInflow. This adjustment ensures the flow rate does not exceed what the inlet can physically pass under gravity flow conditions.

2.  **Normal Flow Limitation**: For conduits not fully filled (where y1 is less than the full depth of the conduit), and if the flow is classified as either subcritical or supercritical, the flow rate might be adjusted to the normal flow rate using checkNormalFlow. This ensures the flow does not exceed the capacity dictated by the conduit's slope and roughness under normal (non-pressurized) conditions.

### Under-relaxation

- To stabilize the solution, an under-relaxation technique is applied, blending the new flow rate (q) with the previous iteration's flow rate (qLast) using a factor (omega). This technique helps to mitigate oscillations and convergence issues in the simulation. If this blending results in a change of flow direction, a small, non-zero flow rate is assigned to transition smoothly between positive and negative flows.

### User-defined Flow Limit

- If a user-defined flow limit (Link\[j\].qLimit) is set and the absolute value of the calculated flow exceeds this limit, the flow rate is capped at the limit. This feature allows users to enforce operational constraints within the simulation.

### Flap Gate and Dry Node Checks

- **Flap Gates**: If a flap gate prevents reverse flow and such conditions are detected (link_setFlapGate), the flow is set to zero to reflect the physical blockage of flow.

- **Dry Nodes**: Flow is not allowed to originate from a dry node (where the depth is below a negligible threshold, FUDGE), ensuring the simulation remains physically realistic. This prevents the model from predicting flow from locations where insufficient water is present to contribute to flow.

### Updating Conduit and Link States

- The new average area (Conduit\[k\].a1), flow rates (Conduit\[k\].q1, Conduit\[k\].q2, and Link\[j\].newFlow), depth (Link\[j\].newDepth), and volume (Link\[j\].newVolume) are computed and saved, reflecting the updated state of the conduit based on the latest calculations. These updates ensure the conduit's state in the simulation accurately represents the outcome of the current time step's analysis.

## 8/ Get the link flow class

The getFlowClass function determines the flow classification for a conduit in a hydraulic simulation system based on the flow depths at the upstream and downstream ends of the conduit, as well as the flow rate through the conduit. This classification helps in understanding the hydraulic behavior within the conduit, which can be critical for accurate modeling and analysis of water flow in systems like storm sewers, rivers, and other channels. Here's an outline of how the function works:

### Inputs:

- **j**: Index of the conduit link being analyzed.

- **q**: Current flow rate through the conduit, in cubic feet per second (cfs).

- **h1**: Hydraulic head at the upstream end of the conduit (feet).

- **h2**: Hydraulic head at the downstream end of the conduit (feet).

- **y1**: Upstream flow depth in the conduit (feet).

- **y2**: Downstream flow depth in the conduit (feet).

- **yC**: Pointer to a variable where the critical flow depth will be stored (feet).

- **yN**: Pointer to a variable where the normal flow depth will be stored (feet).

- **fasnh**: Pointer to a variable where the fraction between normal and critical depth will be stored.

### Process:

1.  **Node Indexes and Offsets**: Retrieves the indexes for the upstream and downstream nodes of the conduit and their respective invert offsets. Adjustments are made for conduits connected to outfalls, considering the depth at the outfall.

2.  **Initial Flow Classification**: The default flow classification is set to subcritical, assuming the flow conditions are not extreme or unusual.

3.  **Determining Flow Conditions**:If both ends of the conduit are wet (have significant depth), the flow direction and depth are analyzed to classify the flow as either critical or subcritical at the upstream or downstream end, depending on the flow depth relative to calculated normal and critical depths.If the flow is negative (indicating reverse flow), the function checks for conditions that would classify the upstream end as critical.For positive flow, it checks if the downstream end meets criteria for being classified as critical or if it falls within a specific range between normal and critical depth.

4.  **Dry Conditions**: The function classifies the conduit as dry if there's no significant flow at either end.

5.  **Partial Wet Conditions**:If only the downstream end is wet and the downstream head is less than the upstream invert elevation, it's classified as UP_DRY.Conversely, if only the upstream end is wet and the upstream head is less than the downstream invert elevation, it's classified as DN_DRY.The function also considers cases where flow might be forced into a critical condition at the dry end due to hydraulic conditions, provided there's an offset at that end.

6.  **Adjustment for Critical and Normal Depths**: The function calculates and adjusts the critical and normal depths (yC and yN) and the fraction between them (fasnh) based on the flow rate and conduit characteristics.

### Output:

- Returns a flow classification code, which indicates the hydraulic condition of the flow in the conduit, such as subcritical, critical, dry, or conditions indicating reverse flow or partial wetness.

- Updates the yC, yN, and fasnh parameters with the critical depth, normal depth, and the fraction between these depths, respectively.

This classification is essential for hydraulic modeling as it influences the computation of flow velocities, pressures, and the overall behavior of water in the conduit, which are critical for designing and analyzing hydraulic structures and flood control measures.

## 9/ Find Local Losses

The findLocalLosses function calculates the local hydraulic losses in a conduit link, which are part of the momentum equation used in hydraulic simulations, particularly those employing the dynamic wave approach for flow routing. These local losses occur at the inlet, outlet, and along the length of the conduit due to factors like friction, bends, fittings, and changes in cross-sectional area. Here's how the function works:

### Inputs:

- **j**: The index of the conduit link for which local losses are being calculated.

- **a1**: The cross-sectional area at the upstream end of the conduit (in square feet).

- **a2**: The cross-sectional area at the downstream end of the conduit (in square feet).

- **aMid**: The cross-sectional area at the midpoint of the conduit, or an average area along the conduit (in square feet).

- **q**: The flow rate through the conduit (in cubic feet per second, cfs).

### Process:

1.  **Absolute Flow Rate**: The function first ensures that the flow rate q is considered as an absolute value to calculate losses regardless of the flow direction.

2.  **Calculating Losses**:The local losses are initialized to zero.The function then adds to the local losses based on the conduit's characteristics and the flow rate:**Inlet Losses**: If the upstream area a1 is significant (greater than a negligible threshold FUDGE), inlet losses are calculated as the product of the inlet loss coefficient (Link\[j\].cLossInlet) and the flow rate divided by the upstream area. This reflects losses due to flow entering the conduit.**Outlet Losses**: Similarly, if the downstream area a2 is significant, outlet losses are calculated using the outlet loss coefficient (Link\[j\].cLossOutlet) and the flow rate divided by the downstream area. This accounts for losses as flow exits the conduit.**Average Losses**: If the midpoint area aMid is significant, additional losses are accounted for using the average loss coefficient (Link\[j\].cLossAvg) and the flow rate divided by the midpoint area. These losses represent those occurring along the length of the conduit due to factors like friction and minor bends or fittings not explicitly modeled.

### Output:

- The function returns the total local losses (in feet per second) calculated from the inlet, outlet, and along the conduit length. These losses are used in the momentum equation to adjust the flow velocities and hydraulic grades along the conduit.

### Purpose:

Local losses play a crucial role in accurately simulating hydraulic systems, as they affect the energy gradient along the conduit and hence the flow velocity and depth. By accounting for these losses, hydraulic models can more accurately predict the behavior of real-world systems under various flow conditions.

![](https://media.licdn.com/dms/image/v2/D4E12AQGFRM4jNDidHQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1707620107478?e=1795651200&v=beta&t=jZHtJ95WaQW_ZD8RRinpFi6gVMp33s6Q23RpwPyYB1o)

Losses are at a link in SWMM5 - not a Node

## 10/ Find the Surface Area of the Link

The findSurfArea function is designed to calculate and assign the surface area contributions of a conduit to its upstream and downstream nodes based on the current hydraulic conditions. This calculation is crucial for accurately modeling the interaction between the conduit and its connecting nodes in hydraulic simulations, such as those used for stormwater management, sewer systems, or water distribution networks. Here's a detailed explanation of how this function operates:

### Inputs:

- **j**: The index of the conduit link being analyzed.

- **q**: The current flow rate through the conduit, measured in cubic feet per second (cfs).

- **length**: The length of the conduit, in feet.

- **h1**: A pointer to the hydraulic head at the upstream end of the conduit, in feet.

- **h2**: A pointer to the hydraulic head at the downstream end of the conduit, in feet.

- **y1**: A pointer to the flow depth at the upstream end of the conduit, in feet.

- **y2**: A pointer to the flow depth at the downstream end of the conduit, in feet.

### Process:

1.  **Initialization**: Retrieves the indexes for the upstream and downstream nodes and the current flow depths at these nodes.

2.  **Flow Classification**: Determines the flow classification of the conduit (subcritical, critical, dry, etc.) based on the flow depths and the conduit's hydraulic characteristics. This classification influences how the surface area is calculated.

3.  **Surface Area Calculation**: Depending on the flow classification, the function calculates the surface area associated with the conduit at both the upstream and downstream nodes. This involves:Calculating the flow depth at the midpoint of the conduit.Determining the top width of the conduit at the upstream, downstream, and midpoint based on the flow depths.Calculating the surface area contributions to the upstream and downstream nodes based on these widths and the conduit length.

4.  **Adjustments for Flow Conditions**:For conditions like UP_CRITICAL or DN_CRITICAL, the flow depth at the critical end is adjusted to either the critical or normal depth, whichever is smaller, and the hydraulic head is updated accordingly.For UP_DRY or DN_DRY conditions, the flow depth is set to a negligible value (FUDGE) to represent a nearly dry condition, and the surface area is calculated [accordingly.In](http://accordingly.In) the case of a completely dry conduit (DRY), a minimal surface area is assigned.

### Outputs:

- The function updates the values of h1, h2, y1, and y2 to reflect the calculated flow depths and hydraulic heads at the ends of the conduit based on the determined flow conditions.

- It also assigns the calculated surface area contributions to the upstream (surfArea1) and downstream (surfArea2) nodes, stored in the conduit's data structure. These surface areas are essential for accurately modeling how water is distributed to and from the nodes connected by the conduit.

### Purpose:

This function plays a critical role in hydraulic simulations by ensuring that the interaction between conduits and nodes accurately reflects the physical behavior of water flow. By determining the surface area contributions based on current flow conditions, the simulation can more accurately predict water levels, flow rates, and pressures throughout the system.

## 111/ Slot width, area, width and hydraulic radius

These functions are integral parts of hydraulic modeling software, specifically designed to calculate key hydraulic parameters of conduits such as slot width, top width, flow area, and hydraulic radius based on the flow depth. These calculations are essential for analyzing water flow in conduits, particularly under surcharge conditions or when employing specific hydraulic approximation methods like the Preissmann slot. Here's a breakdown of each function and its purpose:

### getSlotWidth

- **Purpose**: Calculates the width of a hypothetical slot at the top of a conduit to simulate surcharge conditions without explicitly modeling pressurized flow. This method is particularly used when the SurchargeMethod is set to SLOT.

- **Inputs**:xsect: Pointer to the conduit's cross-section data.y: Flow depth within the conduit.

- **Process**:If the slot surcharge method is not used or the cross-section type is open, it returns 0.0.For depths significantly above the full depth (greater than 1.78 times the full depth), it returns a width that is 1% of the maximum width of the conduit's cross-section.Otherwise, it calculates the slot width using the Sjoberg formula, which depends on the normalized flow depth.

- **Output**: The width of the slot in feet

![](https://media.licdn.com/dms/image/v2/D4E12AQHLIMxRjYc8hw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1707668531964?e=1795651200&v=beta&t=rwZVYwnJdiSrqbVb7i4zr8xB9ZRq6rmgr6iC7TX7EgQ)

Slot Calculations

- .

### getWidth

- **Purpose**: Computes the top width of the water surface in a conduit, considering the effect of a surcharge slot if applicable.

- **Inputs**:xsect: Pointer to the conduit's cross-section data.y: Flow depth within the conduit.

- **Process**:Calls getSlotWidth to determine if a slot width should be considered.If a slot width is used, that value is returned as the top width.For depths at or above a certain cutoff without considering an open cross-section, the depth is adjusted to this cutoff value before computing the top width.

- **Output**: The top width of the flow surface in feet.

### getArea

- **Purpose**: Calculates the cross-sectional flow area in a conduit.

- **Inputs**:xsect: Pointer to the conduit's cross-section data.y: Flow depth within the conduit.wSlot: Width of the surcharge slot, if any.

- **Process**:If the flow depth exceeds the full depth of the conduit, it calculates the area as the full cross-sectional area plus the area attributed to the flow in the slot.For depths below the full depth, it calculates the area based on the specific geometry of the conduit's cross-section.

- **Output**: The flow area in square feet.

### getHydRad

- **Purpose**: Computes the hydraulic radius of the flow in a conduit, which is a key parameter in hydraulic calculations such as determining flow velocity and resistance.

- **Inputs**:xsect: Pointer to the conduit's cross-section data.y: Flow depth within the conduit.

- **Process**:For depths at or above the full depth, it returns the hydraulic radius associated with the full depth.For lesser depths, it calculates the hydraulic radius based on the conduit's cross-sectional shape and flow depth.

- **Output**: The hydraulic radius in feet.

## 12/ Check Normal Flow

The checkNormalFlow function assesses whether the flow within a conduit should be adjusted to reflect a "normal flow" condition, rather than the flow rate determined from the dynamic wave equations typically used in hydraulic simulations. This check is crucial for ensuring that the simulated flow does not exceed what would be physically possible given the conduit's characteristics and the hydraulic gradient. Here's a breakdown of how this function works:

### Inputs:

- **j**: Index of the conduit link being evaluated.

- **q**: The flow rate in the conduit as calculated from dynamic wave equations, in cubic feet per second (cfs).

- **y1**: The flow depth at the upstream end of the conduit, in feet.

- **y2**: The flow depth at the downstream end of the conduit, in feet.

- **a1**: The cross-sectional flow area at the upstream end of the conduit, in square feet.

- **r1**: The hydraulic radius at the upstream end of the conduit, in feet.

### Process:

1.  **Initialization**: The function starts by checking if the conduit is connected to an outfall, which can influence whether normal flow conditions are considered.

2.  **Water Surface Slope Check**: It first checks if the normal flow conditions should be considered based on the slope of the water surface relative to the conduit's slope. If the water surface slope is less than the conduit slope, or if the link involves an outfall, the condition for checking normal flow is set to true.

3.  **Froude Number Check**: If the initial slope check doesn't trigger normal flow conditions and the settings allow, the function then examines the Froude number at the upstream end of the conduit. A Froude number equal to or greater than 1.0 indicates supercritical flow, prompting a check for normal flow. This check is skipped if an outfall is involved.

4.  **Normal Flow Calculation**: If either condition above indicates that normal flow conditions should be assessed, the function calculates the normal flow rate (qNorm) using the Manning formula, adjusted by a coefficient (beta), and the hydraulic radius and area at the upstream end. This calculation reflects the maximum flow rate that can be sustained given the conduit's slope and roughness under steady, uniform flow conditions.

5.  **Flow Rate Comparison and Adjustment**: If the calculated normal flow rate is less than the dynamic flow rate (q), indicating that the dynamic flow exceeds what is physically plausible under normal conditions, the function flags the flow as "normal flow" and returns the adjusted (reduced) flow rate. Otherwise, it returns the original dynamic flow rate.

### Output:

- Returns the modified flow rate in the link, either the original dynamic flow rate (q) or the calculated normal flow rate (qNorm), depending on the evaluation. This adjustment ensures that the flow rate in the simulation does not exceed the physical capabilities of the conduit under normal conditions.

### Purpose:

This function is integral to hydraulic simulations for correcting flow rates in conduits to reflect realistic hydraulic behavior. By ensuring that flow rates do not exceed what is physically possible given the conduit's characteristics, the simulation maintains accuracy in representing water movement within the system.

![](https://media.licdn.com/dms/image/v2/D4E12AQGpLFcYlT9vaQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1707620180717?e=1795651200&v=beta&t=35e7jVbogpRxlEYTaLujDL51-XYz3-iNzl0jLu51yxs)

Normal flow, if Used Only used the upstream point

## 13/ Force Mains

These functions are part of hydraulic simulation software, focusing on calculating various hydraulic parameters for force mains—pipes that convey water under pressure, typically used in sewer systems or water distribution networks. Each function has a specific purpose in evaluating and adjusting the hydraulic conditions within force mains based on established flow equations (Hazen-Williams or Darcy-Weisbach). Here's a summary of what each function does:

### forcemain_getEquivN

- **Purpose**: Computes an equivalent Manning's n (roughness coefficient) for a force main, ensuring that the Manning's equation yields the same flow value as the Hazen-Williams or Darcy-Weisbach equation under fully turbulent flow conditions.

- **Inputs**: Link index j, conduit index k.

- **Process**:Determines the equivalent Manning's n based on the force main's diameter, slope, and roughness, using either the Hazen-Williams or Darcy-Weisbach equation.

- **Output**: Equivalent Manning's n value.

### forcemain_getRoughFactor

- **Purpose**: Calculates a roughness adjustment factor for a force main to compensate for artificial lengthening of the pipe.

- **Inputs**: Link index j, lengthFactor which is the factor by which the pipe's length has been artificially extended.

- **Process**:Calculates the adjustment factor based on the selected force main equation and the conduit's characteristics.

- **Output**: Roughness adjustment factor.

### forcemain_getFricSlope

- **Purpose**: Computes the friction slope in a force main for use in dynamic wave flow routing, applying either the Hazen-Williams or Darcy-Weisbach formula.

- **Inputs**: Link index j, flow velocity v, hydraulic radius hrad.

- **Process**:Calculates the head loss per unit length based on the flow's velocity and hydraulic characteristics of the pipe.

- **Output**: The force main's friction slope.

### forcemain_getReynolds

- **Purpose**: Calculates the Reynolds number for flow in a force main, which is a dimensionless quantity used to predict flow patterns in different fluid flow situations.

- **Inputs**: Flow velocity v, hydraulic radius hrad.

- **Output**: Reynolds number.

### forcemain_getFricFactor

- **Purpose**: Computes the Darcy-Weisbach friction factor for a force main using the Swamee and Jain approximation to the Colebrook-White equation.

- **Inputs**: Roughness height e, hydraulic radius hrad, Reynolds number re.

- **Process**:Determines the friction factor based on the flow's Reynolds number and the pipe's roughness and hydraulic radius.

- **Output**: Darcy-Weisbach friction factor.

These functions collectively enable the simulation software to accurately model the behavior of flows in pressurized conduits, taking into account the unique hydraulic characteristics of force mains. By adjusting for factors like artificial pipe lengthening and applying appropriate flow equations, the software can provide more accurate predictions of flow velocities, pressures, and head losses in water distribution or sewer systems.

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
