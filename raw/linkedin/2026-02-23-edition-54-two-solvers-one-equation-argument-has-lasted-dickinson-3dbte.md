---
title: "Edition 54: Two Solvers, One Equation, and the Argument That Has Lasted Forty Years"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-54-two-solvers-one-equation-argument-has-lasted-dickinson-3dbte
created: "2026-02-23 17:03"
published: "2026-02-23 17:58"
words: 2628
export_sha256: 3e2ca716aab35db144606f0fff733e183c637b57c3c2dfdceb034260da8a0313
---
# Edition 54: Two Solvers, One Equation, and the Argument That Has Lasted Forty Years

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Edition 54: Two Solvers, One Equation,, and the Argument That Has Lasted Forty Years ](https://media.licdn.com/mediaD4E12AQHYaoqYVdx39w "Edition 54: Two Solvers, One Equation,, and the Argument That Has Lasted Forty Years ")

### A 150-year-old equation, two different ways to solve it, and why your pipe design might depend on which one you choose.

There is a set of equations that governs the movement of water in every pipe, channel, ditch, and culvert on Earth. They were written down in 1871 by a French mathematician and engineer named Adhemar Jean Claude Barre de Saint Venant, and they have not changed since. The equations express two ideas that are, individually, almost childishly simple. Mass is conserved. Momentum is conserved. What flows into a section of pipe must either flow out or accumulate. A force applied to water produces acceleration proportional to the force and inversely proportional to the mass. Newton would have recognized the principles instantly. They are, at bottom, his principles, applied to a fluid in a conduit instead of an apple in a vacuum.

> **Continuity and Momentum**

The equations themselves fit on a napkin. The continuity equation says that the rate of change of cross sectional area with respect to time plus the rate of change of flow with respect to distance equals the lateral inflow. The momentum equation says that the rate of change of flow with respect to time plus the convective acceleration plus the pressure gradient plus the friction slope equals zero. Four terms. Two equations. The complete mathematical description of unsteady flow in an open channel, published in a single paper over one hundred and fifty years ago and not improved upon since.

> **Solutions Angst**

The difficulty is not writing them down. The difficulty is solving them. The Saint Venant equations are nonlinear partial differential equations, which is a mathematician's way of saying that they do not have a closed form solution for any geometry that actually exists in a real sewer network. You cannot solve them with algebra. You cannot solve them with calculus. You can only solve them approximately, by replacing the smooth continuous equations with discrete numerical approximations and letting a computer grind through millions of arithmetic operations to produce an answer that is close enough to be useful.

> **SWMM5 vs ICM InfoWorks St Venant 1D**

And here is where the argument begins. Because there is more than one way to approximate a set of partial differential equations. The choice of numerical method determines the accuracy, the stability, the computational speed, and the behavior of the solution under extreme conditions. Two software packages can implement the identical physics using different numerical schemes and produce different answers for the same pipe carrying the same water under the same rainfall. Both answers are approximations. Both are defensible. Neither is exact. And the practicing engineer who must choose between them is left to navigate a landscape of trade offs that most textbooks describe only in the abstract.

> **Extran vs Wallingford**

For the past forty years, two numerical approaches have been around the urban drainage modeling in the English speaking world. The first, descended from the EXTRAN module of the original EPA Storm Water Management Model, uses a node link formulation with an implicit backward Euler time integration scheme and successive relaxation for convergence. The second, developed by Wallingford Software in England and now maintained by Autodesk as InfoWorks ICM, uses a Preissmann four point implicit finite difference scheme with Newton Raphson iterations and adaptive time stepping.

> **Most people do not want to to see PDEs**

Those two sentences contain more consequential technical detail than most engineers encounter in a year of practice. And yet the implications ripple through every model, every design, every flood prediction, and every infrastructure decision that depends on computational hydraulics.

I built an application to make those implications visible. It lives at swmm icm st venant robertdickinson dot replit dot app, and it does something that no textbook or reference manual has ever done effectively. It lets you watch both solvers work on the same network simultaneously and see exactly where and why they differ in colorful animations.

> **Let me explain what it contains and why each piece matters.**

The fundamental architectural difference between the two solvers is spatial discretization. This is the question of how the solver divides the physical pipe network into computational pieces. SWMM 5 inherits the EXTRAN tradition of treating each conduit as a single computational element. Head is calculated at the nodes. Flow is calculated in the link. There are no intermediate calculation points along the pipe. A four hundred foot conduit has exactly two points where the solver computes anything. One at each end.

ICM takes a fundamentally different approach. It divides each conduit into multiple segments, typically one segment every hundred fifty to two hundred feet. Head and flow are calculated at every segment boundary. A four hundred foot pipe might have three or four internal computation points in addition to the two end nodes. Information does not jump instantaneously from one end of the pipe to the other. It propagates through the segments, point by point, the way a real pressure wave propagates through a real pipe filled with real water.

> **117 Animations**

The application includes an animation that makes this difference viscerally clear. You introduce a flow pulse at the upstream end and watch it travel through the network. In the SWMM 5 panel, the entire link updates simultaneously. The flow changes from zero to nonzero across the whole conduit in a single time step, as if someone flipped a switch. In the ICM panel, you can see the wave front advancing from segment to segment, arriving at the downstream node perceptibly later than it arrives at the upstream node. In a short pipe during a slowly changing storm, this distinction is academic. In a long conduit during a rapidly rising hydrograph, the distributed approach captures flow variations along the pipe length that the single element approach averages away.

Then there is the matter of how each solver handles the transition from open channel flow to pressurized flow. This is the problem of surcharge, and it is one of the most numerically challenging situations in computational hydraulics. In open channel flow, the water has a free surface. The equations describe waves propagating at relatively modest speeds. When the pipe fills completely and becomes pressurized, the physics changes abruptly. Pressure waves in a full pipe travel at the speed of sound in water, roughly one thousand meters per second, compared to the one to five meters per second of a gravity wave in a partially full pipe. This discontinuity can wreak havoc on numerical solvers.

> **Preissmann slot.**

Both SWMM 5 and ICM address this through a device called the Preissmann slot. The concept is elegant. You place an infinitely narrow virtual slot on top of the pipe cross section, extending upward above the crown. When the water level rises above the pipe crown, it enters this fictitious slot, which provides a tiny amount of virtual free surface area. This keeps the free surface equations mathematically valid even when the pipe is technically full. The wave speed in the slot is high but finite, governed by the slot width. A narrower slot produces a faster wave speed that more closely approximates real pressurized behavior but requires a smaller time step for numerical stability. A wider slot is more forgiving numerically but less physically accurate.

ICM has used the Preissmann slot as its default surcharge method from the beginning. SWMM 5 added it as an option in version 5.1.013, released around 2012. Before that, SWMM used a separate surcharge algorithm inherited from EXTRAN that explicitly switched between open channel and pressurized equations. The application includes an iterative equation that lets you adjust pipe diameter and slot width factor and watch the resulting wave speed change in real time. You develop an intuitive understanding of the relationship between slot geometry and solver behavior that would take hours of reading to acquire from a textbook.

> **Manning's equation comparison calculator**

There is a Manning's equation comparison calculator that reveals something most engineers never notice. SWMM 5 and ICM use slightly different numerical methods to compute the geometric properties of partially full circular pipes. The cross sectional area, hydraulic radius, and top width at a given depth are computed through different internal approximations. The resulting differences in flow rate are small, typically under one percent for most depth to diameter ratios. But they exist. And if you are trying to reconcile results between the two platforms and you are chasing the last fraction of a percent of discrepancy, the calculator shows you exactly where it comes from. The difference is not a bug in either software. It is a consequence of different valid approximation methods applied to the same geometry.

> **Force main comparison**

There is a force main comparison that illustrates one of the most practically important differences between the two platforms. When a pipe operates under pressure, the choice of friction equation matters enormously. SWMM 5 offers three options. Manning's formula, which was designed for open channel flow and is theoretically inappropriate for pressurized conditions but widely used anyway. Hazen Williams, which is empirical and developed specifically for pressurized pipe flow. And Darcy Weisbach, which is the most theoretically rigorous but requires knowledge of the pipe wall roughness in absolute terms rather than as a Manning's coefficient.

The application lets you toggle between all three and see the resulting flow for identical conditions. For a twelve inch pipe with five feet of head above the crown, Manning's equation gives 2.53 cubic feet per second. Hazen Williams gives 3.21. Darcy Weisbach gives 1.58. That is not a rounding discrepancy. The highest answer is more than double the lowest. The choice of friction equation in a force main can change your design flow by over one hundred percent. Most engineers do not realize this until they see the numbers side by side, which is exactly what the calculator provides.

ICM handles force mains through a dedicated link object type with pressurized flow equations built into the solver. The transition from open channel to pressurized conditions occurs smoothly through the Preissmann slot without requiring an explicit equation switch. This architectural difference means that ICM does not present the user with a choice of friction formula in the same way SWMM 5 does. The pressurized flow behavior is embedded in the solver design rather than offered as a user option.

> **Live network comparison.**

The flagship feature of the application is the live network comparison. A five node network with one inflow hydrograph, the same network geometry, the same Manning's roughness, the same boundary conditions, run through both solvers simultaneously. You set the peak inflow and storm duration. You click run. Two hydrographs develop side by side. SWMM 5 on the left. ICM on the right.

For a moderate storm on a well behaved gravity system, the two hydrographs are nearly indistinguishable. The peaks differ by perhaps two to three percent. The timing differs by one or two time steps. The continuity errors differ. SWMM 5 typically reports 0.1 to 0.5 percent. ICM typically reports 0.01 to 0.1 percent, a consequence of its distributed volume accounting across multiple computational points per conduit.

Where the solvers diverge meaningfully is at the extremes. Heavy surcharge. Rapid flow reversals. Supercritical to subcritical transitions where a hydraulic jump forms inside a pipe. Very long conduits with short duration inflow pulses where wave propagation timing matters. Networks with loops where flow direction is ambiguous and can reverse during a storm. These are the conditions where the choice of solver genuinely affects the engineering answer, and these are the conditions the application is designed to illuminate.

> **Solver recommendation tool**

The application also includes a solver recommendation tool. You answer nine questions about your project and receive a weighted recommendation. Network size. Stability priority. Whether you need two dimensional surface flooding, which only ICM provides through its mesh based overland flow module. Whether your budget is constrained, which favors SWMM 5 since it is free and open source. Whether you have dry weather or intermittent flow conditions, which SWMM 5 handles natively while ICM maintains a minimum base flow. Whether you need complex real time control logic. Whether you need the large time steps that ICM's convergence based adaptive stepping enables. Whether your project has a green infrastructure or LID focus, which SWMM 5 supports through its dedicated LID module. Whether there is an EPA regulatory requirement that effectively mandates SWMM 5.

The recommendation is never that one solver is universally superior. It is always contextual. SWMM 5 is public domain, open source, the regulatory standard for EPA compliance work, and the only platform with built in LID and water quality modeling. ICM is commercial, distributed, capable of coupled one dimensional and two dimensional simulation, and demonstrably faster for very large networks where its ability to take larger stable time steps more than compensates for the additional computational work per time step.

The application organizes all of this across twelve tabs. Solver mechanics. Solver options. Dynamic wave options. Temporal dynamics. Operational controls. Advanced analysis. Hydrologic methods. Climate and infiltration. ICM simulation specifics. Surface to sewer coupling. Green infrastructure. And code architecture. Each tab contains side by side comparisons, interactive calculators, or animated demonstrations. Each one addresses a specific aspect of the question that every hydraulic modeler eventually asks. Which solver should I use and why.

> **Robert Heinlein on Tools**

A Heinlein character would frame it simply. A competent hydraulic engineer should understand both tools well enough to know where they agree, where they disagree, why they disagree, and which disagreements matter for the project at hand. Choosing a solver because it is the one you learned in school is not engineering. Choosing a solver because you understand its numerical assumptions, its limitations, its strengths relative to your specific network and your specific design questions, that is engineering. The application provides the information needed to make that choice with eyes open.

> **More St Venant and Why Not**

Saint Venant published his equations in 1871. He could not have imagined the computational machinery we would build to solve them. But the equations themselves remain perfect. They describe the conservation of mass and momentum in one dimensional unsteady flow with a fidelity that one hundred and fifty four years of subsequent science has not found reason to correct. What we argue about is not the equations. We argue about the approximations. And the only responsible way to navigate that argument is to understand exactly what each approximation does, where it excels, and where it falls short.

The application is free and available now at swmm icm st venant robertdickinson dot replit dot app. Both solvers. Same network. Side by side. Interactive calculators for every major difference. A recommendation engine for solver selection. Twelve tabs of comparative analysis. And the complete reference library linking to every source document for both solver implementations.

> **The End and A Link**

The water, as always, solves the Saint Venant equations perfectly. It has been doing so since before Saint Venant was born. It is only we who approximate. The least we can do is approximate honestly and understand what our approximations cost us.

[https://swmm-icm-st-venant--robertdickinson.replit.app/](https://swmm-icm-st-venant--robertdickinson.replit.app/)
