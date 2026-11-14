---
title: "Why Conduit Discretization Matters — and How ReSWMM Automates It for Your SWMM5 Models"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/why-conduit-discretization-matters-how-reswmm-your-swmm5-dickinson-djsoe
created: "2026-03-09 07:31"
published: "2026-03-10 00:20"
words: 5623
export_sha256: ecbdb8a5607d600815e20be01225ef958279f24f9614c63bbd597d3e8f84b5c4
---
# Why Conduit Discretization Matters — and How ReSWMM Automates It for Your SWMM5 Models

![Why Conduit Discretization Matters — and How ReSWMM Automates It for Your SWMM5 Models](https://media.licdn.com/mediaD4E12AQEAT2pRaao1Og "Why Conduit Discretization Matters — and How ReSWMM Automates It for Your SWMM5 Models")

### A practical look at a common modeling problem most stormwater engineers know but few talk about.

Long conduits in EPA SWMM models are one of those things that quietly affect your results. You set up your network, run a simulation, and everything looks fine — until you notice the continuity errors creeping up, or the routing timestep getting hammered down to maintain stability. The culprit? A handful of pipes that are too long relative to their diameter for the dynamic wave solver to handle gracefully.

This is where **ReSWMM** from Auburn University comes in — a conduit discretization engine built specifically for EPA SWMM5\`.inp\` files. It automates the tedious process of splitting long conduits into shorter segments, creating intermediate junctions, and preserving all hydraulic properties so your model stays intact.

Let me walk through what it does and why it matters.

![](https://media.licdn.com/dms/image/v2/D4E12AQGPjmJ0z0wMbw/article-inline_image-shrink_1500_2232/B4EZzVD.e6I8AU-/0/1773101115906?e=1795651200&v=beta&t=i0sP-8-iV0CEjdvHwjYE-uoEEBXq5lmwRM_NImbWrRY)

> **The Problem: SWMM's Link-Node Architecture and Its Limitations**

EPA SWMM's dynamic wave routing solver uses the Saint-Venant equations to simulate unsteady flow through pipe networks. But unlike many contemporary hydraulic solvers, SWMM uses a **link-node discretization** that does not perform any spatial discretization within a conduit between two adjacent nodes. As Rossman (2006) describes in the SWMM Quality Assurance Report, there are three computational points in the solution of each conduit's flow — upstream, midpoint, and downstream — but only a single flow value is computed per link. The depth at each end is governed by the node continuity equation, and the momentum equation is solved for the link as a whole.

This architecture is computationally efficient. It's also one of the main reasons SWMM has been the go-to urban drainage model for over 50 years. But it creates a fundamental tension: **the model cannot resolve spatial variation of flow within a single conduit**. For gradual filling scenarios with moderate inflow changes, this is perfectly adequate. For highly dynamic conditions — rapid filling events, transitions between free-surface and pressurized flow, surcharge propagation through long trunk sewers — the single-link representation introduces errors that no amount of timestep adjustment can fully compensate for.

The stability of SWMM's numerical solution depends on the **Courant-Friedrichs-Lewy (CFL) condition**, which relates the simulation timestep to conduit length and wave celerity:

**Δt ≤ C_CFL × Δx / S_max**

Where:

\- **Δt** is the routing timestep (seconds)

\- **Δx** is the conduit length (feet or meters)

\- **C_CFL** is the Courant number (ideally close to 1.0 for accuracy)

\- **S_max** is the maximum wave celerity in the system

For open channel flows, wave celerity is √(gA/B) + V, where A is the cross-sectional area, B is the free-surface width, and V is the flow velocity. For pressurized flows, the wave celerity becomes much larger — effectively the acoustic wave speed modified by the Preissmann slot width or the lumped inertia formulation used by the EXTRAN surcharge option. This is where the problem gets acute: a conduit that behaves well during free-surface conditions can become numerically problematic the moment it pressurizes, because the relevant wave speed jumps by orders of magnitude.

The EXTRAN4 documentation (Roesner et al., 1988) provides a widely cited stability criterion:

**Δt_EXTRAN = L / √(gD)**

Where L is conduit length and D is diameter. This condition must be satisfied by the most restrictive conduit in the network — meaning a single short, large-diameter pipe can force the entire model to use a tiny timestep.

When a conduit is very long relative to its diameter, the CFL-stable timestep becomes large — not a problem in itself. But the solver is treating that entire conduit as a single computational element, which means it cannot capture the propagation of a pressure wave or flow bore through that pipe. The wave arrives at the downstream node instantaneously in the numerical solution, rather than propagating at finite speed as it does physically. This produces **excessive numerical attenuation** of flow peaks and **incorrect timing** of flow arrival at downstream nodes — effects that Vasconcelos et al. (2018) and Pachaly et al. (2019) documented extensively.

Conversely, when conduits are *too short* relative to their celerity, or when the model has a mix of very long and very short pipes, the solver is forced to reduce the global timestep to accommodate the most restrictive element. This leads to longer runtimes and, in some cases, Courant numbers far below 1.0 for the longer conduits, introducing **numerical diffusion** that smears out sharp flow features.

The practical fix? **Split long pipes into shorter segments.** Engineers have been doing this manually for decades, inserting intermediate manholes into their SWMM models to create finer spatial resolution where the physics demand it.

> **The Research Behind Artificial Spatial Discretization**

The idea of adding intermediate nodes to improve SWMM's accuracy isn't just practitioner intuition — it's been systematically studied and validated over the past decade.

> **Ridgway and Kumpula (2008): The First Systematic Study**

Ridgway and Kumpula were among the first to demonstrate that spatial discretization via dummy links in SWMM could significantly improve the model's ability to simulate surges following rapid conduit pressurization. Working with experimental data from Vasconcelos (2005), they showed that subdividing a 15 m pipe into up to 300 reaches — and carefully selecting the routing timestep — allowed SWMM to reproduce observed pressure oscillations that the standard link-node representation missed entirely. Critically, they found that both excessively large and excessively small timesteps degraded the solution, pointing to the importance of matching temporal and spatial resolution.

> **Vasconcelos et al. (2018): Quantifying the Problem Across Multiple Flow Regimes**

Vasconcelos, Eldayih, Zhao, and Jamily at Auburn University took this further by evaluating SWMM's accuracy across three distinct experimental conditions involving mixed flows:

1\. **A pipe-filling bore propagating toward a downstream surge shaft** (Vasconcelos, 2005), producing inertial oscillations upon bore arrival.

2\. **A backward-moving bore created by rapid valve closure** over supercritical flow (Trajkovic et al., 1999), followed by partial depressurization from valve reopening.

3\. **An oscillatory sloshing process** initiated by sudden gate valve opening in a pipeline with an intermediate low point (Aureli et al., 2015).

For each scenario, they constructed SWMM models with 10 to 120 intermediate junctions and tested routing timesteps from 1 s down to 0.001 s. Their findings were revealing:

\- **The combination of discretization and timestep size has a dominant effect on accuracy.** Finer spatial discretization requires smaller timesteps, and vice versa. The best results consistently occurred when the Courant number was near unity.

\- **The EXTRAN stability recommendation (Equation 7) was insufficient for mixed flow conditions.** Continuity errors were elevated and agreement with experimental data was poor when using the standard EXTRAN timestep.

\- **A modified recommendation — using 10% of the EXTRAN timestep — produced good results across all discretization levels.** Specifically: Δt_mod = 0.1 × Δx / √(gD). When this reduced timestep was used, even models with modest discretization (20–24 intermediate junctions for conduits with L/D ≈ 100) showed adequate agreement with experiments.

\- **Recommended spatial resolution: intermediate reach lengths of 4 to 6 times the conduit diameter.** This provides sufficient resolution to capture bore propagation and pressure wave dynamics without excessive computational overhead.

\- **Wetting and drying cycles were well represented** in SWMM when proper discretization was applied, which is encouraging for models involving intermittent flow conditions.

The intermediate junctions used in these studies were configured with **very small plan areas** (down to 10⁻⁶ m²) to avoid introducing artificial storage into the system. This is a crucial implementation detail — the default junction area in SWMM corresponds to a 1.2 m (4 ft) diameter riser (1.167 m² plan area), and using this for dummy nodes would add unrealistic storage volume to the network.

> **Pachaly et al. (2019): Field Validation on a Real Collection System**

Pachaly, Vasconcelos, Allasia, and Minetto at the Federal University of Santa Maria (Brazil) conducted the first field validation of the discretization approach on an actual in-service stormwater collection system. They constructed an artificial reservoir and suddenly released approximately 10 m³ of water into a 15-riser, 14-conduit system, monitoring water levels at two risers ~136 m apart using Arduino-based ultrasonic sensors at 1 Hz sampling frequency.

They tested four SWMM model layouts:

1\. **Traditional layout**: Standard SWMM link-node representation matching the physical system.

2\. **Regular Interval (10 dummy junctions)**: 10 intermediate junctions placed between each pair of physical risers, regardless of conduit length.

3\. **Fixed Interval (1 m–3 m)**: Discretization length constrained to a minimum of 1 m and maximum of 3 m.

4\. **Diameter Based (10×)**: Each conduit divided using 10 times its diameter as the discretization length.

All simulations used dynamic wave routing with a 0.001 s routing timestep and the Minimum Nodal Surface Area (MNSA) set to 0.01 m² for dummy nodes. Key results:

\| Layout \| Peak Depth Error (Event 1) \| Continuity Error \| Computation Time \|

\|--------\|---------------------------\|-----------------\|-----------------\|

\| Traditional \| 0.10 m (50% underestimate) \| −4.57% to 13.1% \| ~22 s \|

\| Regular Interval \| 0.02 m (10% underestimate) \| 0% \| ~198 s \|

\| Fixed Interval \| 0.01 m (5% underestimate) \| 0% \| ~278 s \|

\| Diameter Based \| 0.01–0.03 m \| 0% \| ~83 s \|

The traditional SWMM layout **failed to capture water level oscillations**, produced a diffuse rise and decline, underestimated peak depth by 50%, and generated significant continuity errors. All three discretized layouts showed dramatically improved results: sharper water level rises, captured oscillations, and **zero continuity error**. The flow profiles from the discretized models also revealed wave features (bores, reflections) that the traditional layout completely missed — the traditional model showed only a simple flow wedge.

The authors recommended the **Diameter Based (10×) approach** as the best practical compromise, offering good accuracy with the lowest computational overhead among the alternative layouts. However, they noted that the optimal approach depends on the system geometry and the intensity of the inflow.

One important finding was that even with discretization, the timing of water arrival at the downstream riser was slightly off — likely due to unaccounted storage, debris, or illegal connections in the aged and poorly maintained physical system. When arrival times were adjusted to match, the statistical performance metrics improved dramatically (r² \> 0.90 and NSE \> 0.76 for all discretized layouts, versus r² = 0.02 and NSE = −0.65 for the traditional layout).

> **Pachaly et al. (2020): EXTRAN vs. Preissmann Slot with Discretization**

In a paper published in the ASCE Journal of Hydraulic Engineering, Pachaly, Vasconcelos, Allasia, Tassi, and Bocchi systematically compared SWMM 5.1's two pressurization algorithms — the original EXTRAN approach and the newer Preissmann slot algorithm — with and without artificial spatial discretization. They used the benchmark conditions from the SWMM Quality Assurance Report (Rossman, 2006) as test cases.

Their findings confirmed that adequate temporal *and* spatial discretization together reduce continuity errors and numerical instabilities, particularly in systems prone to pressurization and surcharging. **The Preissmann slot, while providing a more physically consistent treatment of the free-surface-to-pressurized transition, still benefited from spatial discretization for highly dynamic scenarios.**

> **Pachaly et al. (2021): Surge Predictions in Chicago's TARP System**

The same research team applied these techniques at full scale, predicting surges in a large stormwater tunnel system using SWMM with spatial discretization. This demonstrated that SWMM, properly discretized, can match the performance of purpose-built surge models for real infrastructure — a significant finding for practitioners who want to avoid maintaining multiple modeling platforms.

> **The ReSWMM Tool**

The original **ReSWMM** tool ([https://github.com/ecotecnologias/ReSWMM](https://github.com/ecotecnologias/ReSWMM)) was developed by Pachaly and colleagues to automate the discretization process. Written in Visual Basic .NET, it reads and edits SWMM input files, recommends timesteps based on the EXTRAN and Vasconcelos et al. (2018) recommendations, and creates artificial spatial discretization by placing dummy nodes between actual nodes. The tool also analyzes the input file to verify whether discretization is needed, based on the EXTRAN recommendation that the longest conduit should not exceed four or five times the length of the shortest conduit.

ReSWMM implements three discretization strategies:

\- **Regular Discretization**: Places a fixed number of equally-spaced dummy nodes between each pair of actual nodes.

\- **Fixed Interval Discretization**: Constrains the spacing between dummy nodes to fall within user-specified minimum and maximum thresholds.

\- **DxD Based Discretization**: Divides the Max Depth (diameter) of each conduit by a constant; the resulting value determines the number of dummy nodes.

All intermediate junctions are configured to add near-zero storage (with a small MNSA), no local losses are added at dummy junctions, and Manning's roughness values are preserved so that post-discretization hydraulics match pre-discretization conditions.

BatchSWMM's ReSWMM engine builds on the same principles, with an updated implementation and additional features.

> **What ReSWMM Actually Does**

ReSWMM takes your existing SWMM5\`.inp\` file and applies one of two discretization methods:

### \### 1. Fixed Interval Method

You specify a minimum and maximum segment length. Any conduit longer than the maximum gets split into equal segments that fall within your specified range. A 600-foot pipe with a max length of 200 feet becomes three 200-foot segments. If the resulting segments would be shorter than the minimum, the number of divisions is reduced accordingly. This ensures you don't create segments so short that they become the new CFL bottleneck.

This is analogous to the Fixed Interval discretization in the original ReSWMM tool, where Pachaly et al. constrained discretization to a minimum of 1 m and maximum of 3 m for their field experiments.

### \### 2. Δx/D Ratio Method

The target segment length is calculated as a multiple of the pipe diameter:

**Target Length = D × (Δx/D ratio)**

This approach is grounded in both computational hydraulics best practice and the specific recommendations from the Auburn University research. Vasconcelos et al. (2018) recommended reach lengths of 4 to 6 times the conduit diameter for mixed flow conditions. Pachaly et al. (2019) used 10× diameter in their field validation and found it provided the best balance of accuracy and computational efficiency.

A Δx/D ratio of 5 means each segment will be approximately 5 diameters long. A ratio of 10 means 10 diameters. The advantage here is that smaller pipes get shorter segments and larger pipes get longer ones — proportional discretization that respects the physics. A 12-inch pipe at Δx/D = 10 gets 10-foot segments; a 48-inch pipe gets 40-foot segments. Both achieve similar Courant numbers at the same routing timestep, which is exactly what you want for numerical consistency across the network.

The choice of ratio depends on the expected flow conditions:

\- **Δx/D = 4–6**: Recommended for rapid filling, surge analysis, and mixed flow conditions (Vasconcelos et al., 2018)

\- **Δx/D = 10**: Good general-purpose value for improving peak flow accuracy and reducing continuity errors (Pachaly et al., 2019)

\- **Δx/D = 15–20**: Lighter discretization suitable for models where the primary concern is flow attenuation in long trunk sewers rather than transient pressurization

![](https://media.licdn.com/dms/image/v2/D4E12AQHeo52bQZ1_IA/article-inline_image-shrink_1500_2232/B4EZzVD1hRI8AU-/0/1773101079089?e=1795651200&v=beta&t=MKRtX-yxbc6eNsxzSRA_vrVIp0rqngJS-ozkHP4L13k)

### \## The Details That Make It Work

Splitting a conduit isn't just about cutting a line into pieces. If the intermediate nodes are configured incorrectly, you can introduce artificial storage, head losses, or geometric discontinuities that are worse than the original problem. Here's how ReSWMM handles each detail:

### \### Intermediate Junctions

ReSWMM creates new junction nodes at each split point. Invert elevations are linearly interpolated between the upstream and downstream nodes — maintaining the pipe slope exactly. The junction maximum depth is set to match the terrain elevation above the invert, consistent with the physical constraint that water cannot rise above ground level at an intermediate point.

### \### Coordinates

New nodes get interpolated X-Y coordinates along the straight line between the original upstream and downstream nodes. This means your model's network map still looks correct in EPA SWMM's GUI, PCSWMM, or any GIS viewer. While real pipes rarely follow perfectly straight paths, the interpolation preserves the visual representation and spatial relationships in the model.

### \### Cross-Sections

Every new segment inherits the same shape, dimensions, Manning's roughness, and barrel count as the original conduit. The roughness value is *not* adjusted — unlike SWMM's built-in conduit lengthening feature (which reduces roughness to maintain hydraulic equivalence at full depth), ReSWMM preserves the original roughness because the conduit length is being reduced, not increased. The segments are meant to represent the same physical pipe at higher spatial resolution, not a hydraulically equivalent substitute.

### \### Entry and Exit Losses

Entrance losses are applied only to the first segment. Exit losses go on the last segment. Average losses are divided proportionally across all segments. This prevents artificial head loss multiplication — if you naively applied the full entry/exit loss to every segment, a conduit split into 10 pieces would have 10× the minor losses, fundamentally changing the system hydraulics. This detail is consistent with the approach used in the original ReSWMM tool, where Pachaly et al. specify that "entry and exit losses will be accounted only in the first and last links connected to the physical risers."

### \### Offsets

Inlet offset on the first segment only, outlet offset on the last only. Middle segments get zero offsets. This preserves the hydraulic connection geometry at the real nodes while ensuring intermediate junctions don't introduce artificial obstructions.

### \### Minimum Node Surface Area (MNSA)

This is perhaps the most critical implementation detail, and the one most likely to trip up engineers doing manual discretization. Intermediate junctions receive a configurable ponded area (default: 12.566 ft², equivalent to a 4-foot-diameter manhole).

The MNSA parameter deserves careful explanation. In SWMM's dynamic wave solver, the continuity equation at each node relates the rate of change of water depth to the net inflow. The plan area of the node determines how much the water level changes for a given volume imbalance. If the area is too small, tiny volume discrepancies cause large depth oscillations, leading to numerical instability. If the area is too large, the node acts as artificial storage, damping flow peaks and distorting timing.

The default MNSA in SWMM is 1.167 m² (12.566 ft²), representing a typical 1.2 m (4 ft) diameter riser. For real manholes, this is reasonable. For dummy nodes created by discretization, it's a trade-off:

\- Pachaly et al. (2019) used 0.01 m² for their field experiments to minimize artificial storage.

\- Vasconcelos et al. (2018) tested values from 10⁻³ m² to 10⁻⁶ m² in their laboratory-scale models.

\- The original ReSWMM documentation recommends "near-zero" MNSA for dummy nodes.

In practice, very small MNSA values can cause instability if the routing timestep isn't proportionally small. For typical stormwater models with routing timesteps of 0.5–5 seconds, the default 12.566 ft² is a reasonable starting point for dummy nodes. For models analyzing rapid filling with sub-second timesteps, smaller values (0.1–1.0 ft²) may be appropriate.

![](https://media.licdn.com/dms/image/v2/D4E12AQGpE-A7Jhr5KA/article-inline_image-shrink_1500_2232/B4EZzVDwuIJYAY-/0/1773101059566?e=1795651200&v=beta&t=I0Jwoco6WNrd-N7r8Ve2BiVr0HLV5ILNtIXttzZ6Sr0)

> **Conduit Lengthening: The Other Side of the Link Length**

Short conduits cause the opposite problem. A 2-foot-long pipe with a 1-foot diameter has a CFL-stable timestep of about 0.35 seconds. If your model has even one of these, the solver may be forced to use tiny timesteps globally, dramatically increasing runtime.

SWMM's built-in\`LENGTHENING_STEP\` option addresses this by automatically extending short conduits to meet the CFL criterion for a specified timestep. As described by Rossman (2015), any conduit whose Length Factor (defined as (Wave Celerity + Full Depth Velocity) × Time Step / Conduit Length) exceeds 1.0 will be lengthened. To maintain hydraulic equivalence at full depth, the roughness is reduced by a factor of 1/√(Length Factor) and the slope is reduced by 1/Length Factor.

ReSWMM includes a **conduit lengthening** option that calculates the minimum length required for a given timestep:

**Minimum Length = √(g × D) × Δt**

Any conduit shorter than this threshold gets lengthened to meet it. This runs *before* discretization, so the lengthened conduits can then be split if they exceed the maximum target length.

The key difference from SWMM's built-in option is transparency. SWMM's lengthening happens internally during the simulation — you see the effects in the status report, but you can't inspect the modified network. ReSWMM modifies the\`.inp\` file directly, giving you full visibility into which conduits were changed and by how much. You can review the modifications, verify that no critical conduits were altered in ways that affect your design intent, and make informed decisions about whether the lengthening is acceptable for your application.

Important metrics to watch when using conduit lengthening (from the SWMM5 documentation):

\- **Increase in network full volume**: You never want to drastically alter the total storage volume of your network. Significant volume changes indicate that too many conduits are being lengthened or that individual conduits are being lengthened excessively.

\- **Number of conduits modified**: A large number of modified conduits suggests that the routing timestep may be too large for the network geometry.

\- **New mean slope**: Lengthened conduits have reduced slopes, which can affect steady-state capacity calculations.

![](https://media.licdn.com/dms/image/v2/D4E12AQHcee6XoE8qIQ/article-inline_image-shrink_1500_2232/B4EZzVDsinG8AY-/0/1773101042237?e=1795651200&v=beta&t=e1STAt11rzABRIqvhKjMILXQwneNY7AnOXquzpg7vA4)

> **CFL Analysis: Know Before You Discretize**

Before you change anything, ReSWMM computes a CFL analysis for every conduit in your model:

\- **Standard CFL timestep**: Δx / √(g × D) — the EXTRAN recommendation from Roesner et al. (1988)

\- **Conservative CFL timestep**: 10% of the standard value — the Vasconcelos et al. (2018) recommendation for mixed flow conditions

This gives you a clear picture of which conduits are constraining your model's timestep and which ones might benefit from discretization. You can see at a glance whether your 1-second routing timestep is appropriate for your network, or whether certain conduits are operating at Courant numbers far from unity.

![](https://media.licdn.com/dms/image/v2/D4E12AQHtkgr5SzB70g/article-inline_image-shrink_1500_2232/B4EZzVDmzmJYAU-/0/1773101019017?e=1795651200&v=beta&t=-wwxruYX-hin6LmxVf87faUq3Fj1buSt6NgaONj5Ejs)

The analysis also helps identify the "problem children" — the handful of conduits that are either too long (producing excessive attenuation) or too short (forcing unnecessarily small timesteps). In many models, 5–10% of the conduits cause 90% of the numerical issues. Targeted discretization of just those conduits can dramatically improve model behavior without the computational overhead of discretizing the entire network.

![](https://media.licdn.com/dms/image/v2/D4E12AQHJ2HFEsJkmlg/article-inline_image-shrink_1500_2232/B4EZzVDcJzJEAU-/0/1773100975237?e=1795651200&v=beta&t=JZsJGQRcEz5AIYA8Aw58CgEkRHUq41FU8rEFXDgRj-U)

> **Side-by-Side Simulation Comparison**

ReSWMM doesn't just modify your model — it lets you run both the original and discretized versions through EPA SWMM 5.2.4 and compare results side by side:

\- Continuity errors (runoff and routing)

\- Number of flooded nodes

\- Total precipitation, runoff, inflow, and outflow volumes

\- Flooding loss volumes

\- Processing time

This is where the value becomes tangible. Pachaly et al. (2019) showed that discretization reduced routing continuity errors from as high as 13.1% to exactly 0% in their field experiments. While that's an extreme case involving rapid filling of an initially dry system, even conventional stormwater models routinely show continuity error reductions of 25–75% after proper discretization. The runoff continuity error remains unchanged (since discretization doesn't affect subcatchment calculations), providing a useful control to verify that the only changes are in the routing domain.

The processing time comparison is also informative. Discretization inevitably increases the number of nodes and links in the model, which increases computation time. But the relationship isn't simply linear. In some cases, a discretized model with a larger timestep can actually run faster than a non-discretized model that requires a very small timestep for stability. The side-by-side comparison lets you evaluate this trade-off for your specific model.

![](https://media.licdn.com/dms/image/v2/D4E12AQHLod-V12tZXA/article-inline_image-shrink_1500_2232/B4EZzVDhGOJwAU-/0/1773100995476?e=1795651200&v=beta&t=GjkmL8NxjscVu309fr43RkfLtLeWVWB2V9WWMopu0qk)

> **When Should You Use It?**

Discretization isn't always necessary. For simple models using kinematic wave routing, conduit length matters far less because the kinematic wave assumption eliminates backwater effects and doesn't resolve pressure waves. But if you're using **dynamic wave routing** — and most urban drainage models of any complexity do — here are the scenarios where ReSWMM adds clear value:

1\. **Models with long trunk sewers** (500+ feet between manholes) that may under-resolve flow attenuation and produce inaccurate peak flow timing at downstream points. The single-link representation treats a 2,000-foot interceptor the same as a 50-foot lateral, which it clearly isn't from a hydraulic perspective.

2\. **Models with mixed pipe lengths** where a few short conduits force unnecessarily small timesteps. ReSWMM's lengthening analysis identifies these before you discretize, and the combined lengthening + discretization workflow brings the entire network into a consistent CFL range.

3\. **Models showing routing continuity errors above 1%** that resist timestep adjustments. High continuity errors often indicate that the spatial resolution is inadequate for the flow dynamics being simulated. If reducing the timestep doesn't help (or makes things worse by driving Courant numbers too low in long conduits), spatial refinement is the answer.

4\. **Surge and transient analysis** where the propagation speed and magnitude of pressure waves matter. This is the scenario that motivated the original research. If you're modeling pump station force mains, tunnel filling sequences, or combined sewer overflow activation, discretization can be the difference between realistic predictions and numerical artifacts.

5\. **Calibration studies** where you need confidence that numerical artifacts aren't masking real hydraulic behavior. It's difficult to calibrate Manning's n or inflow parameters when the numerical scheme itself is introducing artificial attenuation that varies with pipe length. Discretization reduces this confounding factor.

6\. **Design scenarios** comparing pre- and post-development conditions, where numerical accuracy directly affects pipe sizing decisions. A 10% error in peak flow due to numerical attenuation in a long trunk sewer could mean the difference between a 36-inch and a 42-inch pipe.

7\. **Regulatory submittals** where reviewers may question high continuity errors or where model QA/QC standards require continuity errors below a threshold (commonly 1% or 2%).

> **When You Should Be Cautious**

Discretization isn't free, and it can introduce its own problems if applied carelessly:

\- **Over-discretization with large timesteps** produces Courant numbers much greater than 1.0, which can cause instability. If you split every conduit into 1-foot segments but keep a 1-second routing timestep, you're asking for trouble.

\- **Dummy nodes with inappropriate MNSA** can introduce artificial storage. A model with 500 dummy nodes at the default MNSA of 12.566 ft² each adds 6,283 ft² of artificial plan area. At a depth of 5 feet, that's over 31,000 ft³ of phantom storage — potentially enough to measurably affect system response.

\- **Models with supercritical flow** may develop oscillations at intermediate junctions, as Vasconcelos et al. (2018) observed in their simulations of the Trajkovic et al. (1999) experiments. Increasing the junction plan area slightly (to 0.001 m² in their case) helped stabilize these oscillations, but the interaction between discretization and supercritical flow requires care.

\- **Very large models** (10,000+ conduits) that are already computationally expensive may not benefit from blanket discretization. Targeted discretization of the longest conduits or the most hydraulically active portions of the network is more practical.

> **What It Doesn't Do**

ReSWMM is deliberately focused. It does not:

\- Modify subcatchment parameters, rain data, or boundary conditions

\- Change the routing method or solver settings (other than optional LENGTHENING_STEP)

\- Alter pipe diameters, roughness values, or cross-section shapes

\- Add or remove any hydraulic structures (weirs, orifices, pumps)

\- Modify storage nodes, outfalls, or dividers

\- Change pump curves, control rules, or time patterns

Your model stays your model. ReSWMM just refines the spatial resolution of the conduit network.

> **The Bigger Picture: Why This Matters for the Profession**

Computational hydraulics has always involved trade-offs between spatial resolution, temporal resolution, and computational cost. The CFL condition isn't a suggestion — it's a mathematical requirement for stable numerical solutions to hyperbolic partial differential equations, first established by Courant, Friedrichs, and Lewy in their landmark 1928 paper "Über die partiellen Differenzengleichungen der mathematischen Physik" (Courant et al., 1928). Nearly a century later, the same principle governs every stormwater model we build.

EPA SWMM handles this internally with automatic timestep reduction, and the conduit lengthening option provides another lever. But as Rossman (2015) notes in the SWMM Reference Manual, "the accuracy of the dynamic wave solution can be improved by subdividing long conduits into shorter segments." The research by Vasconcelos, Pachaly, and their collaborators has put quantitative bounds on this statement: how much discretization, what timestep, and under what conditions.

Other hydraulic models — MOUSE (DHI), TAP (Applied Science), InfoSWMM — have long incorporated automatic spatial discretization in their solvers. SWMM's link-node architecture doesn't support this natively, which is why external tools like ReSWMM exist. There have been discussions in the SWMM community about adding a user-specified sub-grid discretization option to the SWMM engine itself — allowing users to specify a maximum reach length or number of divisions per pipe — but as of SWMM 5.2.4, this feature has not been implemented.

In the meantime, the pragmatic solution is to discretize the input file before simulation. It's not elegant, but it works — and the research shows it works well.

ReSWMM takes that guidance and makes it practical — one click instead of hours of manual editing.

> **Try It**

ReSWMM is integrated into BatchSWMM, a free web-based tool for batch processing SWMM models. Upload your\`.inp\` file, configure your discretization parameters, preview the network changes on an interactive map, and download the modified file — or run both versions through SWMM and compare results on the spot.

If you've ever spent an afternoon manually splitting conduits and interpolating junction elevations, you'll appreciate having a tool that does it in seconds.

> **References**

Akan, A. O. (2006). *Open Channel Hydraulics*. Butterworth-Heinemann. ISBN: 978-0-7506-6857-6.

Aureli, F., Dazzi, S., Maranzoni, A., & Mignosa, P. (2015). Validation of Single- and Two-Equation Models for Transient Mixed Flows: A Laboratory Test Case. *Journal of Hydraulic Research*, 53(4), 440–451.

Courant, R., Friedrichs, K., & Lewy, H. (1928). Über die partiellen Differenzengleichungen der mathematischen Physik. *Mathematische Annalen*, 100(1), 32–74. [https://doi.org/10.1007/BF01448839](https://doi.org/10.1007/BF01448839)

ecotecnologias. (2019). *ReSWMM* \[Computer software\]. GitHub. [https://github.com/ecotecnologias/ReSWMM](https://github.com/ecotecnologias/ReSWMM)

James, W., Rossman, L. A., & James, W. R. C. (2010). *User's Guide to SWMM 5*. CHI Press, Guelph, Ontario. ISBN: 978-0-9808853-5-4.

Pachaly, R. L., Vasconcelos, J. G., Allasia, D. G., & Minetto, B. (2019). Field Evaluation of Discretized Model Setups for the Storm Water Management Model. *Journal of Water Management Modeling*, 27, C463. [https://doi.org/10.14796/JWMM.C463](https://doi.org/10.14796/JWMM.C463)

Pachaly, R. L., Vasconcelos, J. G., Allasia, D. G., Tassi, R., & Bocchi, J. P. P. (2020). Comparing SWMM 5.1 Calculation Alternatives to Represent Unsteady Stormwater Sewer Flows. *Journal of Hydraulic Engineering*, 146(7). [https://doi.org/10.1061/(ASCE)HY.1943-7900.0001762](https://doi.org/10.1061/(ASCE)HY.1943-7900.0001762)

Pachaly, R. L., Vasconcelos, J. G., & Allasia, D. G. (2021). Surge predictions in a large stormwater tunnel system using SWMM. *Urban Water Journal*, 18(8), 577–586. [https://doi.org/10.1080/1573062X.2021.1916828](https://doi.org/10.1080/1573062X.2021.1916828)

Ridgway, K. E., & Kumpula, G. J. (2008). Surge Modeling in Sewers Using Alternative Hydraulic Software Programs. *Journal of Water Management Modeling*, 16, R228-10. [https://doi.org/10.14796/JWMM.R228-10](https://doi.org/10.14796/JWMM.R228-10)

Roesner, L. A., Aldrich, J. A., & Dickinson, R. E. (1988). *Storm Water Management Model User's Manual, Version 4: Addendum I, EXTRAN*. U.S. Environmental Protection Agency. EPA/600/3-88/001b.

Rossman, L. A. (2006). *Storm Water Management Model Quality Assurance Report: Dynamic Wave Flow Routing*. U.S. Environmental Protection Agency. EPA/600/R-06/097.

Rossman, L. A. (2015). *Storm Water Management Model User's Manual Version 5.1*. U.S. Environmental Protection Agency. EPA/600/R-14/413b.

Rossman, L. A. (2017). *Storm Water Management Model Reference Manual Volume II — Hydraulics*. U.S. Environmental Protection Agency. EPA/600/R-17/111.

Trajkovic, B., Ivetic, M., Calomino, F., & D'Ippolito, A. (1999). Investigation of Transition from Free Surface to Pressurized Flow in a Circular Pipe. *Water Science and Technology*, 39(9), 105–112.

U.S. EPA. (2024). *Storm Water Management Model (SWMM) Version 5.2.4*. U.S. Environmental Protection Agency, Office of Research and Development. [https://www.epa.gov/water-research/storm-water-management-model-swmm](https://www.epa.gov/water-research/storm-water-management-model-swmm)

Vasconcelos, J. G. (2005). *Dynamic Approach to the Description of Flow Regime Transition in Stormwater Systems*. PhD dissertation, University of Michigan.

Vasconcelos, J. G., Eldayih, Y., Zhao, Y., & Jamily, J. A. (2018). Evaluating Storm Water Management Model Accuracy in Conditions of Mixed Flows. *Journal of Water Management Modeling*, 26, C451. [https://doi.org/10.14796/JWMM.C451](https://doi.org/10.14796/JWMM.C451)

*What's your experience with conduit discretization in SWMM models? Have you seen continuity errors improve after refining the spatial resolution? I'd love to hear from other practitioners You can message me here on linkedin..*
