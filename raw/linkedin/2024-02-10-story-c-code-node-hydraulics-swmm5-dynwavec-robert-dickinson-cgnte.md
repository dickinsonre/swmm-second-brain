---
title: "A Story about the C-Code Node Hydraulics of SWMM5 or Dynwave.c"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/story-c-code-node-hydraulics-swmm5-dynwavec-robert-dickinson-cgnte
created: "2024-02-10 14:54"
published: "2024-02-10 23:32"
words: 6754
export_sha256: e7dfc090a3689de591a937ad8df14d779608786d96b7e6bf870381ce54587388
---
# A Story about the C-Code Node Hydraulics of SWMM5 or Dynwave.c

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![A Story about the C-Code Node Hydraulics of SWMM5](https://media.licdn.com/mediaD4E12AQH6aXnvBlDw-w "A Story about the C-Code Node Hydraulics of SWMM5")

These code bits or code paragraphs are from the EPASWMM5 code dynwave.c There are fourteen sections: Node and Link Initialization, Dynamic Wave Validation, How is the CFL Time Step Found, Run Dynwave, Find Capacity Limited Links, Find Conduit Flows, Find non-conduit flows, Find Pump Flows, Find Node Depths, Get the Node Depth, Get the Flooded Depth, Find the Variable (not fixed) Time Step, Find the Link Time Step, Find the Node Time Step.

## 1/ The Story Starts: Node and Link Initialization

The dynwave_init function is a key component in setting up the dynamic wave routing method within a stormwater management model, specifically in the context of urban hydrology simulation software like SWMM (Storm Water Management Model). This method is used for more complex simulations of flow in stormwater and sewer networks, where it accounts for backwater effects, entrance and exit losses, and pressurized flow under surcharged conditions. Here's a breakdown of how the function works and its purpose:

### Function Overview:

- **Purpose**: The primary goal of dynwave_init is to prepare the simulation environment for dynamic wave routing calculations. This involves initializing memory for storing node states, setting up initial conditions for nodes and links in the network, and configuring parameters that affect the routing calculations.

### Process Details:

1.  **Memory Allocation for Node States**:Allocates memory for an array of TXnode structures, one for each node in the system. TXnode likely stores additional information needed for dynamic wave routing calculations that are not part of the basic node structure.Checks if the memory allocation was successful. If not, it reports an error message indicating insufficient memory for dynamic wave routing, then exits the initialization process.

2.  **Initialize Node Surface Areas and Crown Elevations**:Iterates through all nodes, setting their initial and new surface areas to zero.Sets each node's crownElev to its invertElev, which is the baseline elevation for the node. The crown elevation is later adjusted based on the geometry of incoming and outgoing links.

3.  **Initialize Links and Update Node Crown Elevations**:Iterates through all links in the network, performing several key operations:For both the upstream (node1) and downstream (node2) nodes of each link, it calculates a potential new crown elevation based on the link's geometry (offset and full depth) and the node's invert elevation.Updates the node's crownElev to the maximum of its current value or the newly calculated value. This step ensures the crownElev reflects the highest point water can reach before spilling or entering a pressurized flow state in any connected conduit.Initializes the link's flow classification to DRY and sets its flow derivative (dqdh) to 0.0, preparing it for the upcoming simulation steps.

4.  **Set Crown Cutoff for Top Width Calculations**:Depending on the surcharge method configured for the simulation (SurchargeMethod), sets a CrownCutoff value. This value is used to determine how the top width of closed conduits is calculated when the flow approaches the crown of the conduit. The choice of cutoff value affects how the model handles transitions between open and pressurized flow in conduits.

------------------------------------------------------------------------

## 2/ Dynamic Wave Validation

The dynwave_validate function plays a crucial role in the setup phase of dynamic wave routing simulations, particularly in urban hydrology models like the Storm Water Management Model (SWMM). Its purpose is to ensure that the simulation parameters related to dynamic wave routing are within acceptable bounds and to apply default values where necessary. This adjustment process is critical for maintaining the integrity of the simulation and ensuring that the dynamic wave routing calculations proceed smoothly and accurately. Here’s an overview of how the function works:

### Process Breakdown:

1.  **Minimum Routing Step Validation**:The function checks if the MinRouteStep (the minimum routing time step for the simulation) is greater than the RouteStep (the time step for routing calculations). If it is, the MinRouteStep is adjusted to equal the RouteStep. This ensures that the minimum routing step is not set to a value larger than the simulation’s actual routing [step.It](http://step.It) then verifies that MinRouteStep is not less than MINTIMESTEP, a predefined minimum allowable time step for the simulation. If MinRouteStep is smaller, it is adjusted to MINTIMESTEP. This step prevents the routing calculations from attempting to proceed with an excessively small time step, which could lead to computational inefficiencies or numerical instability.

2.  **Minimum Surface Area Adjustment**:If MinSurfArea (the minimum nodal surface area for dynamic wave calculations) is set to 0.0, indicating it hasn't been explicitly defined, it is assigned a default value DEFAULT_SURFAREA. This default value ensures there's a baseline surface area for nodes, which is necessary for accurately calculating hydraulic properties and flow dynamics.If MinSurfArea is not 0.0, it is adjusted by dividing it by the square of the unit conversion factor for length (UCF(LENGTH)), converting it to the model's internal units. This adjustment ensures consistency in surface area measurements throughout the simulation.

3.  **Head Tolerance Adjustment**:If HeadTol (the tolerance for changes in head at each node between successive iterations of the dynamic wave routing calculations) is 0.0, it is set to a default value DEFAULT_HEADTOL. This provides a baseline tolerance for judging when the iterative process of finding a hydraulic solution has converged.If HeadTol is not 0.0, it is adjusted by dividing it by the unit conversion factor for length, ensuring that the head tolerance is consistent with the model's internal unit system.

4.  **Maximum Trials Adjustment**:If MaxTrials (the maximum number of iterations allowed for the dynamic wave routing calculations to achieve convergence within each time step) is set to 0, indicating it hasn't been explicitly defined, it is assigned the value DEFAULT_MAXTRIALS. This ensures that there is a limit on the number of iterations, preventing endless loops in cases where convergence is difficult to achieve.

### Conclusion:

The dynwave_validate function ensures that key parameters controlling the dynamic wave routing process are set to reasonable and consistent values before the simulation begins.

## 3/ How is the CFL Time Step Found

The dynwave_getRoutingStep function is an essential part of managing time steps within dynamic wave routing simulations, particularly in complex urban drainage system models. This function's purpose is to determine the appropriate routing time step for the simulation, which can vary based on the conditions of the flow and the user's configurations. Here's an explanation of how the function works and its significance:

### Function Workflow:

1.  **Fixed Step Validation**: Initially, the function checks if the variable step option is turned off (indicated by CourantFactor == 0.0) or if the user-supplied fixed step (fixedStep) is smaller than the minimum allowable variable time step (MINTIMESTEP). In either case, the function returns the fixedStep as the routing time step. This ensures that when variable stepping is not enabled or desired, the simulation proceeds with the stable, user-defined fixed step.

2.  **Initial Variable Step**: If the simulation is just starting (identified by VariableStep == 0.0), the function sets the variable step to MinRouteStep. This initial setting is crucial because it establishes a starting point for the variable stepping mechanism, ensuring that the simulation begins with a step size that respects the minimum routing constraints.

3.  **Variable Step Computation**: If the conditions above are not met, implying that variable stepping is enabled and the simulation is ongoing, the function calculates the variable step based on the current flow solution. This is done through the getVariableStep function (not shown here), which likely considers factors such as the Courant condition, flow velocities, and system geometry to dynamically adjust the time step for efficiency and accuracy.

4.  **Step Adjustment**: After computing the variable step, the function adjusts it to be a multiple of a millisecond (floor(1000.0 \* VariableStep) / 1000.0). This adjustment ensures that the time step is discretized to a precise and practical granularity, facilitating computations and potentially enhancing numerical stability.

### Significance:

- **Efficiency**: By allowing for variable time stepping, the function can increase simulation efficiency. Smaller steps can be used in periods of rapid change to capture dynamics accurately, while larger steps can be used during periods of little change to speed up the simulation.

- **Accuracy**: Adjusting the time step based on flow conditions helps maintain the accuracy of the simulation, ensuring that critical events are not missed and that the numerical solution adheres closely to physical reality.

- **Flexibility**: Providing the option to use a fixed step or a variable step based on the Courant condition and flow characteristics gives users flexibility in configuring the simulation to meet specific needs or constraints.

In summary, the dynwave_getRoutingStep function intelligently manages the complexity of time stepping in dynamic wave routing simulations, balancing between computational efficiency, numerical accuracy, and user-defined configurations to tailor the simulation time step to the evolving conditions of the urban drainage network.

## 4/ Run Dynwave

The dynwave_execute function is a core component of dynamic wave routing in hydraulic and hydrologic modeling, particularly within the context of urban drainage systems. This function is tasked with simulating how water flows through a network of pipes, channels, and other drainage elements over a given time step, using the dynamic wave approach, which accounts for momentum conservation and can accurately simulate backwater effects, looped connections, and surcharged conditions. Here's a detailed breakdown of its operation and purpose:

### Overview of Operation:

1.  **Initialization**:Checks for any pre-existing error conditions (ErrorCode). If an error is present, the function terminates immediately, returning 0 iterations.Initializes variables such as Steps (the iteration counter) and converged (a flag indicating whether the solution has converged) to their starting values.Sets Omega to a predefined relaxation factor (OMEGA) to aid in the iterative solution process.Calls initRoutingStep() to prepare the system for a new routing step, initializing states and conditions for nodes and links.

2.  **Iterative Solution**:Enters a loop that continues until the solution converges or the number of iterations reaches a pre-defined maximum (MaxTrials).Within each iteration:Initializes node states with initNodeStates().Computes link flows with findLinkFlows(tStep), determining how much flow moves through each link in the network.Attempts to find new depths at each node with findNodeDepths(tStep), checking for convergence in the process.Increments the iteration counter (Steps).If more than one iteration has occurred and the system has not yet converged, checks if any link calculations can be bypassed in the next step to improve efficiency (findBypassedLinks()).

3.  **Post-Iteration**:If the system has not converged after the loop exits, updates convergence statistics with updateConvergenceStats(), logging the occurrence of a non-convergence event.Identifies any links that are capacity-limited with findLimitedLinks(), marking conduits that cannot convey additional flow due to physical or hydraulic limitations.

### Purpose and Impact:

- **Dynamic Wave Routing**: This method offers a detailed and comprehensive way to simulate flow in drainage networks, capturing complex hydraulic behaviors that simpler methods may not. It's particularly useful in urban flood modeling, stormwater management, and sewer system design and analysis.

- **Convergence and Efficiency**: The iterative approach, combined with checks for convergence and the ability to bypass unnecessary calculations, balances the need for accuracy with computational efficiency. This is crucial for large or complex networks where simulation time can become significant.

- **Error Handling and Diagnostics**: By checking for convergence and updating statistics related to iterations and convergence, the function provides valuable diagnostics that can help identify potential issues in the model setup or in the system being simulated.

- **Adaptability**: By adjusting the number of iterations based on convergence, the function can adapt to varying conditions within the simulation, ensuring that the model remains stable and accurate across different scenarios.

In summary, the dynwave_execute function embodies the complexity and precision required for dynamic wave routing in urban hydrology models. Its design reflects a careful balance between the need for detailed, accurate simulation of hydraulic phenomena and the practical considerations of computational resources and simulation time.

## 5/ Find Capacity Limited Links

### Purpose:

To determine which conduit links within the drainage network are capacity limited. A conduit is considered capacity limited when it cannot convey additional flow due to being fully filled or due to hydraulic gradient constraints.

### Process:

1.  **Iterate Through Links**: The function loops through all links in the model, focusing on those that are true conduits (i.e., capable of conveying water).

2.  **Check for Full Capacity**:For each conduit, it first checks if the upstream end is full. This is determined by comparing the area of flow (a1) at the start of the conduit to the full flow area (aFull) of the conduit's cross-section (xsect). If a1 is equal to or greater than aFull, it implies that the conduit is operating at or near its full capacity.

3.  **Hydraulic Gradient Check**:Next, it assesses whether the hydraulic gradient (head difference between upstream and downstream ends) exceeds the conduit's slope, a condition indicating that the conduit could be hydraulically capacity [limited.It](http://limited.It) calculates the hydraulic head (h1 and h2) at the upstream (n1) and downstream (n2) nodes, respectively, by adding the node depth to the invert elevation of each node.If the difference in hydraulic head (h1 - h2) is greater than the product of the conduit's length and its slope (fabs(Conduit\[k\].slope) \* Conduit\[k\].length), the conduit is marked as capacity limited.

### Significance:

- **Hydraulic Accuracy**: By identifying capacity-limited links, the model can more accurately simulate hydraulic conditions, especially under surcharge or full-flow scenarios.

- **Flood Risk Management**: Knowing which links are capacity limited helps in assessing flood risks and can inform decisions on infrastructure improvements or operational changes.

- **Optimization**: This identification can be used to prioritize simulations or to adjust operational strategies, such as opening diversion gates or activating pumps, to mitigate capacity limitations.

- **Model Feedback**: The identification of limited links provides valuable feedback for model calibration and verification, allowing modelers to adjust parameters or reconsider system designs to address hydraulic limitations.

## 6/ Find Conduit Flows

The findLinkFlows function is a pivotal part of the hydraulic simulation process in dynamic wave routing, which is typically used in models for stormwater, sewer systems, or any networked flow systems. This function calculates the flow rates in all types of links (conduits, pumps, orifices, weirs, etc.) within the network for a given time step. Here’s a detailed explanation:

### Function Overview

- **Objective**: To update the flow rates in every link based on current hydraulic conditions and the time step dt.

### Process Details

1.  **Parallel Processing for True Conduits**:The function uses OpenMP (a parallel programming extension for C/C++ and Fortran) to parallelize the flow calculation for true conduits (actual physical pipes or channels, not dummy elements or control devices). This parallel section aims to enhance computational efficiency by utilizing multiple threads (NumThreads).Within the parallel section, it iterates through all links. For each link that is a true conduit and not bypassed (!Link\[i\].bypassed), it calls dwflow_findConduitFlow to calculate the new flow within that conduit for the current time step dt, using the dynamic wave flow method.

2.  **Update Inflow/Outflows for Nodes Attached to True Conduits**:After computing the flows in the conduits, the function iterates again through all links. For each link that is a true conduit, it updates the inflow and outflow rates of the nodes connected to these conduits (updateNodeFlows), ensuring the node water balances are accurate and reflect the new conduit flows.

3.  **Handle Non-Conduit Links**:The function then processes non-conduit links, which include dummy conduits, pumps, and flow control structures like orifices and weirs. For each non-conduit link that isn't bypassed, it calculates the new flow using findNonConduitFlow, which likely involves specific hydraulic calculations based on the link type (e.g., pump curves, orifice equations).It updates the inflow and outflow rates for the nodes connected to these non-conduit links, similar to the process for true conduits.

### Significance

- **Efficiency and Scalability**: By employing parallel processing for the computationally intensive task of flow calculation in conduits, the function can significantly reduce computation times for large networks, making it scalable for complex urban drainage systems.

- **Hydraulic Accuracy**: This function is critical for maintaining hydraulic accuracy throughout the network. By calculating flows based on updated hydraulic conditions and ensuring node balances, it allows the model to dynamically respond to changing conditions, such as varying rainfall intensities or operational changes in pumps and gates.

- **Flexibility**: The separation of flow calculations for true conduits and non-conduit links (like pumps and regulators) provides flexibility. It allows the model to incorporate a wide range of hydraulic behaviors and control strategies, making it applicable to diverse hydraulic systems.

## 7/ Find non-conduit flows

The findNonConduitFlow function is designed to calculate the flow for links in a hydraulic network that do not behave like traditional conduits. Non-conduit links can include pumps, orifices, weirs, and other control structures that have flow characteristics different from pipes or channels. This function is essential in hydraulic modeling for accurately simulating the wide array of hydraulic behaviors observed in complex drainage systems. Here’s how it operates:

### Inputs and Outputs

- **Input**:i: The index of the link within the network's array of links.dt: The current time step in seconds.

- **Output**: None directly, but the function updates the flow rate (newFlow) for the non-conduit link.

### Process

1.  **Previous Flow Retrieval**: The function starts by storing the last calculated flow rate (qLast) for the link. This value is important for implementing under-relaxation techniques that smooth transitions in flow rates from one iteration to the next, enhancing numerical stability.

2.  **Initial Flow Calculation**:It then determines the new inflow (qNew) to the link based on the upstream node conditions. This step involves calling link_getInflow, which accounts for possible restrictions like flap gates being closed or pumps being offline.For pump links, the inflow is further adjusted by getModPumpFlow to ensure that the pumping rate does not exceed the volume of water available at the pump's inlet node, which prevents negative volumes and unrealistic simulation results.

3.  **Surface Area Calculation**: The function calls findNonConduitSurfArea to calculate the surface area contributed by the non-conduit link to its upstream and downstream nodes. This is essential for accurately computing hydraulic gradients and for flow calculations in subsequent iterations.

4.  **Flow Update with Under-Relaxation**:The function then applies under-relaxation to the new flow calculation by blending the new inflow (qNew) with the previous flow rate (qLast). The parameter Omega is the under-relaxation factor, controlling the extent to which the new flow calculation is adjusted towards [stability.It](http://stability.It) ensures that flow direction changes are handled carefully, not allowing the flow to change direction abruptly without passing through zero. This step prevents numerical oscillations and ensures a smooth convergence towards the steady or quasi-steady state.

5.  **Flow Assignment**: Finally, the updated flow rate (qNew) is assigned to the link's newFlow property, updating the model state for the current time step.

### Significance

- **Hydraulic Modeling Flexibility**: This function allows hydraulic models to accurately represent a wide range of hydraulic structures beyond simple pipes, adapting to the real-world complexity of urban drainage systems.

- **Numerical Stability**: By using under-relaxation and careful handling of flow direction changes, the function enhances the numerical stability of the simulation, which is crucial for obtaining reliable results over long simulation periods.

- **Adaptation to Dynamic Conditions**: Adjusting pump flows based on available water and applying under-relaxation makes the model responsive to dynamic hydraulic conditions, improving the accuracy of simulations involving variable flows and operating conditions.

## 8/ Find Pump Flows

The getModPumpFlow function is crucial for hydraulic modeling, particularly in urban drainage or sewer network simulations, where pumps are commonly used to move water from lower to higher elevations or across drainage areas. This function dynamically adjusts the flow rate of a pump based on the available water at the pump's inlet node, ensuring the simulation remains realistic under varying hydraulic conditions. Here’s how it works:

### Purpose

To adjust the pumping rate determined by a pump's curve to account for the physical limitation of water availability at the pump's inlet node. This prevents scenarios where the model would unrealistically simulate pumping water that isn't there, ensuring the conservation of mass within the system.

### Process

1.  **Initial Checks**:The function begins by checking if the proposed pump flow rate (q) from the pump curve is zero. If it is, the function immediately returns this value, as there's no need for adjustment.

2.  **Inlet Node Type Determination**:The function identifies the pump's inlet node (j) and checks if it is a storage type node. For storage nodes, the function ensures that the pumping does not deplete the storage volume below zero by calling node_getMaxOutflow.

3.  **Pump Type and Flow Adjustment**:The function then checks the type of pump (TYPE1_PUMP, TYPE2_PUMP, TYPE3_PUMP, TYPE4_PUMP) based on the pump's index (k).For TYPE1_PUMP, similar to storage nodes, it ensures that the node volume doesn’t go negative.For other pump types, the function calculates a new net inflow rate to the node (newNetInflow) by subtracting the proposed pump outflow and existing node outflow from the node [inflow.It](http://inflow.It) then translates this rate into a net flow volume over the timestep and adjusts the node's depth accordingly. If this adjustment would result in a negative depth at the upstream node, indicating there's not enough water to support the proposed pumping rate, the pump flow is set equal to the node's inflow to prevent unrealistic depletion.

### Output

The function returns the modified pump flow rate (q), which is either the initially proposed pump flow, an adjusted flow to prevent storage depletion, or the inflow rate to the pump's inlet node if the initial flow rate was unsustainable.

### Significance

- **Hydraulic Realism**: Ensures hydraulic simulations remain realistic by preventing pumps from extracting more water than is available, reflecting physical constraints.

- **System Stability**: Helps maintain numerical stability in the model by avoiding negative volumes or depths, which could lead to simulation errors.

- **Operational Accuracy**: Reflects real-world operational limits of pumps in varying hydraulic conditions, improving the model's utility for planning and operational decision-making.

## 9/ Find Node Depths

The findNodeDepths function is a crucial part of the dynamic wave routing process in hydraulic modeling, specifically within the context of modeling stormwater systems, sewer networks, or any other hydraulic systems being simulated. This function's primary goal is to calculate the new water depth at each node within the network for a given timestep and determine whether the simulation has reached a state of convergence based on these new depths. Here's a breakdown of its operation:

### Purpose

To calculate the water depth at all nodes (except outfalls) for a given timestep and assess whether the depth changes are within a specified convergence tolerance, indicating that a steady or quasi-steady state has been reached.

### Process

1.  **Outfall Depths**: The function begins by setting the depths at outfall nodes, which are the endpoints of the system where water exits. The depth at these nodes is typically determined based on the flow conditions in the connecting links.

2.  **Depth Calculation for Non-Outfall Nodes**: For each non-outfall node, the function calculates the new depth based on current hydraulic conditions and the timestep (dt). This involves accounting for inflow, outflow, storage characteristics, and any specific node attributes that influence depth, such as weir or orifice settings in the case of control structures.

3.  **Convergence Check**: After calculating the new depths, the function assesses convergence by comparing the depth change (difference between the new depth and the depth from the previous iteration) against a predefined tolerance (HeadTol). If the depth change for any non-outfall node exceeds this tolerance, the system has not yet converged, and further iterations are needed.

4.  **Parallel Processing**: The depth calculation and convergence check processes are parallelized to enhance computational efficiency, particularly for large and complex networks. This parallelization ensures that the computations for different nodes can occur simultaneously, reducing the overall computation time.

### Output

The function returns a Boolean value indicating whether the system has converged:

- **TRUE**: If the depth change at all non-outfall nodes is within the convergence tolerance, indicating that the simulation has reached a stable state for this timestep.

- **FALSE**: If any non-outfall node's depth change exceeds the tolerance, indicating that further iterations are required to achieve convergence.

### Significance

- **Hydraulic Stability**: Ensuring convergence is critical for achieving hydraulic stability in the model, which is essential for producing reliable and accurate simulation results.

- **Model Accuracy**: Accurate depth calculations are vital for determining flow rates, velocities, and other hydraulic parameters throughout the network.

- **Iterative Solution**: The dynamic wave routing method is iterative, and the convergence check is a key step in determining when the iterative process can stop for a given timestep.

In summary, the findNodeDepths function is fundamental in dynamic wave routing, enabling the simulation to accurately predict water depths and achieve hydraulic stability through iterative calculations and convergence checks.

## 10/ Get the Node Depth

The setNodeDepth function is part of the dynamic wave routing process in hydraulic simulations, specifically designed to update the depth of water at each non-outfall node in a hydraulic network (such as a stormwater drainage system) after a simulation time step. This function plays a crucial role in hydraulic modeling, ensuring accurate calculation of water depths at various points in the network based on the flow conditions. Here's a detailed explanation of its operation:

### Purpose

To calculate and update the water depth at each non-outfall node based on the net flow (difference between inflow and outflow) during the current time step, while considering the node's capacity to store or convey water. This calculation is essential for accurately simulating the hydraulic behavior of the network.

### Process

1.  **Initial Checks and Conditions**: Determines if the node can pond water above its designated full depth and whether it is currently ponded or surcharged. Surcharged conditions occur when the water level exceeds the node's capacity, potentially due to high inflow rates or blockages.

2.  **Calculating Net Flow and Volume Change**: Calculates the net flow into the node and the corresponding change in volume over the time step. This involves averaging the net flow at the start and end of the time step and multiplying by the time step duration.

3.  **Determining New Depth**:For non-surcharged nodes, the change in depth is calculated based on the change in volume and the surface area of the node. This calculation assumes that the water spreads out evenly over the surface area.For surcharged nodes, the depth change considers the hydraulic characteristics of the node and its connections, such as the sum of the derivatives of flow with respect to depth (dqdh) for the links connected to the node.

4.  **Applying Corrections and Constraints**:The function applies corrections for newly ponded nodes to prevent unrealistic depth changes.Ensures that calculated depths are within physical and operational limits, such as preventing negative depths or depths exceeding the maximum allowed by ponding conditions.

5.  **Updating Node Depth**: The calculated new depth is saved as the current depth for the node, which will be used in subsequent calculations and iterations of the simulation.

6.  **Volume and Overflow Calculations**: If the new depth exceeds the node's capacity, the function calculates the depth and volume of water that is effectively flooded, adjusting the node's depth and volume accordingly.

### Output

The function updates the depth at each non-outfall node based on the net inflow or outflow, considering the possibility of ponding or surcharging. It ensures that depths are realistic and comply with the physical constraints of the system.

### Significance

- **Hydraulic Modeling Accuracy**: Accurately setting node depths is crucial for modeling the hydraulic performance of drainage systems, affecting calculations of flow rates, velocities, and the overall behavior of the network under various conditions.

- **Flood Risk Assessment**: By determining when and where nodes become surcharged or flooded, the function aids in assessing flood risks and identifying critical points in the network.

- **Operational and Design Decisions**: Insights gained from the depth calculations can inform operational strategies and design improvements to mitigate surcharging and flooding, enhancing the resilience and efficiency of the hydraulic system.

In summary, the setNodeDepth function is integral to dynamic wave routing, enabling the simulation to capture the complex interactions between inflow, storage, and conveyance within a hydraulic network.

## 11/ Get the Flooded Depth

The getFloodedDepth function calculates the depth, volume, and overflow for a node that has exceeded its capacity to handle incoming water, effectively becoming flooded. This function is part of a hydraulic simulation, typically used in modeling stormwater drainage systems or sewer networks. The calculation is crucial for accurately assessing flood risks and the performance of drainage infrastructure under excess flow conditions. Here’s a detailed breakdown of its operation:

### Purpose

To compute the new depth of water at a node when it is in a flooded state, taking into account the node's ability to pond water and the change in water volume over a specified time step. It also calculates the volume of water that overflows from the node due to flooding.

### Process

1.  **Handling Non-Pondable Nodes**: For nodes that cannot pond water (e.g., nodes with no designated storage area above a certain depth), the overflow is calculated directly from the change in volume (dV) divided by the time step (dt). The node’s new volume is set to its full volume capacity, and its depth is set to the maximum depth before ponding (yMax).

2.  **Handling Pondable Nodes**: For nodes that can pond water (e.g., areas where water can accumulate above the normal full depth), the new volume is calculated by adding the change in volume (dV) to the old volume, ensuring it does not drop below the node's full volume. The overflow is calculated based on the increase in volume above the node’s full volume or old volume, whichever is greater, divided by the time step (dt).

3.  **Overflow Adjustment**: If the calculated overflow is negligible (below a certain small threshold or "fudge" factor), it is set to zero to avoid numerical inaccuracies.

4.  **Depth Adjustment**: The depth (yNew) is adjusted to reflect the flooded condition, ensuring that it accurately represents the physical state of the node after accounting for the overflow.

### Output

The function returns the adjusted depth of the node when it is flooded. Additionally, it updates the node's volume and overflow properties to reflect the excess water that the node cannot contain within its normal capacity.

### Significance

- **Flood Risk Management**: Understanding how nodes within a drainage system behave under flood conditions is vital for flood risk assessment and management. It helps identify critical infrastructure improvements needed to mitigate flooding.

- **Hydraulic Performance Analysis**: The function aids in analyzing the hydraulic performance of drainage systems during extreme weather events, providing insights into where and why overflow occurs.

- **Design and Planning**: For engineers and urban planners, the ability to predict node flooding and overflow is essential for designing adequate stormwater management systems and planning urban development to minimize flood risks.

In summary, the getFloodedDepth function is a critical component of hydraulic simulations, providing valuable data on how water levels at specific nodes respond to exceedance events, thereby informing flood risk assessments and infrastructure design decisions.

## 12/ Find the Variable (not fixed) Time Step

The getVariableStep function is designed to calculate an appropriate time step for a hydraulic simulation that adheres to a stability criterion while not exceeding a user-defined maximum time step. This function is crucial for ensuring the simulation remains stable and accurate by dynamically adjusting the time step based on the current state of the system's nodes and links (e.g., pipes, channels). Here’s an in-depth look at how it operates:

### Inputs:

- **maxStep**: The maximum time step, in seconds, as specified by the user. This acts as the upper limit for the time step calculation to ensure that the simulation does not advance too quickly, which might overlook critical changes in system states.

### Process:

1.  **Initialization**:It initializes variables to hold the indices of the link and node with the minimum time steps (minLink and minNode) and sets them initially to -1, indicating that no specific link or node has been identified yet.tMin, which represents the allowable time step, is initially set to the user-supplied maxStep.

2.  **Finding Stable Time Steps**:The function first calculates a stable time step for the system's links by calling getLinkStep, passing the current tMin as the starting point. This function returns the minimum time step required for the links to satisfy the Courant condition for [stability.Next](http://stability.Next), it calculates a stable time step for the nodes by calling getNodeStep, using the time step obtained from the links as its input. This ensures that the node calculations are constrained by the link stability requirements.

3.  **Selecting the Smallest Time Step**:The function then compares the time steps calculated for links and nodes (tMinLink and tMinNode), choosing the smaller of the two. This ensures the chosen time step meets the stability criteria for both the system's links and nodes.If the node time step is smaller, it updates tMin to tMinNode and resets minLink to -1 to indicate that the critical constraint comes from a node rather than a link.

4.  **Updating Statistics**:It calls stats_updateCriticalTimeCount with the indices of the critical node and link. This function likely updates simulation statistics, tracking how often each node or link becomes the limiting factor for the time step, which can be useful for diagnostic and optimization purposes.

5.  **Enforcing a Minimum Time Step**:The function ensures that the calculated time step does not fall below a predefined absolute minimum (MinRouteStep). This is a safeguard against excessively small time steps that could significantly slow down the simulation or cause numerical instability.

### Output:

- Returns tMin, the calculated time step that satisfies the stability criteria for both links and nodes, constrained by the user-defined maximum time step and an absolute minimum time step.

This function plays a critical role in adaptive time-stepping mechanisms in hydraulic simulations, allowing for efficient and stable model operation by adjusting the time step according to the system's current hydraulic conditions.

## 13/ Find the Link Time Step

This C function, getLinkStep, calculates the critical time step for conduits in a hydraulic simulation based on the Courant criterion. The Courant condition is a stability condition that must be satisfied for numerical solutions of partial differential equations (like those governing fluid flow) to ensure stability and accuracy. This function is designed to work within a larger hydraulic modeling system, where it iteratively examines each conduit to find the one with the smallest time step that still satisfies the Courant condition. Here's a breakdown of its operation:

### Inputs:

- **tMin**: The minimum critical time step found so far, in seconds. This is the starting point for comparison.

- **minLink**: A pointer to an integer that will store the index of the conduit link with the critical time step.

### Outputs:

- The function updates **minLink** with the index of the link that has the critical time step.

- Returns the critical time step in seconds, which is the smallest time step that satisfies the Courant criterion across all conduits examined.

### Process:

1.  **Initialization**: The function starts with a local variable tLink initialized to tMin, which holds the smallest critical time step found during the iteration.

2.  **Iteration over Conduits**:The function iterates over all links in the system (Nobjects\[LINK\] represents the total number of links).It checks if a link is a conduit (Link\[i\].type == CONDUIT). Only conduits are considered because the Courant criterion is relevant to them due to their flow characteristics.

3.  **Criteria for Continuing the Evaluation**:The function skips conduits with negligible flow (q), cross-sectional area (Conduit\[k\].a1), or Froude number (Link\[i\].froude). These checks prevent division by zero and ensure that only meaningful conduits are evaluated.

4.  **Computing the Time Step**:For each conduit that passes the initial checks, the function computes a time step t based on the conduit's flow characteristics and geometry, ensuring it satisfies the Courant condition. The computation considers the flow rate (q), the volume of water in the conduit (Link\[i\].newVolume), the modified length of the conduit (Conduit\[k\].modLength), the actual length of the conduit (link_getLength(i)), and the Froude number.

5.  **Updating the Critical Time Step**:If the computed time step t for a conduit is smaller than the current critical time step tLink, the function updates tLink with this new value and records the index of this conduit in \*minLink.

### Return Value:

- After examining all conduits, the function returns the smallest critical time step (tLink) found, which ensures the simulation's stability and accuracy.

This approach allows the hydraulic simulation to dynamically adjust time steps based on flow conditions, enhancing the model's stability and efficiency.

## 14/ Find the Node Time Step

The getNodeStep function calculates the critical time step for nodes in a hydraulic simulation, ensuring that the projected change in water depth at any node does not exceed a maximum allowable limit. This is part of a stability and accuracy control mechanism in simulations that deal with water flow and storage dynamics, such as stormwater management systems, sewer networks, or river basins. Here's an explanation of how the function operates:

### Inputs:

- **tMin**: The critical time step found so far, in seconds. This serves as the initial value against which the function will compare the calculated time steps for each node.

- **minNode**: A pointer to an integer that will store the index of the node with the critical time step.

### Process:

1.  **Initialization**:The function initializes tNode with tMin, which represents the critical time step for nodes, to be determined.

2.  **Iterating Over Nodes**:The function loops through each node in the system (Nobjects\[NODE\] indicates the total number of nodes). It performs checks to determine whether a node should be considered for further evaluation based on its type and depth characteristics.

3.  **Skipping Certain Nodes**:Nodes of type OUTFALL are skipped because their depths are not constrained in the same way as other nodes.Nodes with a depth (newDepth) less than or negligible (FUDGE) are skipped, as they are not significantly affected by depth changes.Nodes where the depth is already at or near the crown elevation (accounting for a small tolerance, FUDGE) are also skipped, as they cannot significantly change without causing overflow or similar issues.

4.  **Calculating Maximum Allowable Depth Change**:For nodes that pass the initial checks, the function calculates a maximum allowable depth change as a fraction (25% in this case) of the difference between the node's crown elevation and invert elevation. This limit ensures that changes in depth do not rapidly exceed the physical constraints of the node.

5.  **Determining the Critical Time Step**:The function calculates the time (t1) it would take for the depth at a node to reach the maximum allowable change, based on the current rate of depth change (dYdT). This is a predictive measure to avoid instability or excessive depth changes within a single time step.If this calculated time is smaller than the current critical node time step (tNode), tNode is updated to this new value, and the node's index is stored in \*minNode.

### Output:

- The function updates \*minNode with the index of the node that has the critical time step.

- Returns the critical time step for nodes, tNode, in seconds. This is the smallest time step that prevents any node from experiencing an allowable depth change that could compromise the simulation's stability or accuracy.

------------------------------------------------------------------------

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
