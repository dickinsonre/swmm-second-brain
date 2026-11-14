---
title: "Edition 59: How One Web App Unlocks Two Worlds of Hydraulic Modeling: EPASWMM5 and EPANET"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-59-how-one-web-app-unlocks-two-worlds-epanet-robert-dickinson-rqdve
created: "2026-03-13 14:03"
published: "2026-03-25 01:27"
words: 4263
export_sha256: 4b8cc16dd7c0113880c7f36faa70ebd0acab7b628dc29b868376802792fd49f0
---
# Edition 59: How One Web App Unlocks Two Worlds of Hydraulic Modeling: EPASWMM5 and EPANET

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![How One Web App Unlocks Two Worlds of Hydraulic Modeling: EPASWMM5 and EPANET](https://media.licdn.com/mediaD4E12AQHIBlXGg_xQuA "How One Web App Unlocks Two Worlds of Hydraulic Modeling: EPASWMM5 and EPANET")

### Or: Who is the common thread between SWMM5 and EPANET.

*Dedicated to the still active Dr. Lewis A. Rossman, creator of EPANET at the US EPA (1991–2026) and SWMM5 from 2001 to 2024. After 30+ years of service,* [*Lew retired in April 2014*](https://www.openepanet.org/Topic/23233/lew-rossmans-retirement)*. Every pressurized pipe model in the world traces back to his work.*

> **The Day in 2001 that SWMM Started to Breathe**

It was in Cincinnati, summer 2001. I was walking from the University of Cincinnati toward the old EPA building, a few blocks away. I was on my way to meet Lew Rossman as part of the SWMM5 CRADA team with CDM, now CDM Smith.

Inside, Lew already had SWMM5 running in a bare early form. The INP file was partly defined, the engine was in C, and there was even a simple UX to draw a network. EPANET had clearly laid some of the groundwork, and his earlier decision to rewrite distribution system solvers in C was already paying off here. SWMM4 and all earlier versions of SWMM were written in Fortran and the code still showed the legacy of mainframe computers.

You could tell this wasn’t just another version bump. It was a different way of thinking about how we build and share hydraulic models.

This means the real story of SWMM5 starts long before the public release in 2004 — it starts in rooms like that one, with an engineer or scientist quietly reshaping the tools we still use today.

------------------------------------------------------------------------

> **How We Got There**

Before SWMM5, we lived in Fortran. SWMM3 and SWMM4 did serious work, but they carried layers of patched logic, fixed-format input in SWMM3 and a better free form in SWMM4 but still rooted in the punch card era of computing. More annoying it lived in a world of interface files connecting runoff to Extran so there was no time step to time step link.

You could model with them. You just couldn’t easily see *why* the model behaved the way it did without digging through arrays and COMMON blocks and making ascii graphs.

The CRADA — a Cooperative Research and Development Agreement — between USEPA and CDM opened a different door. It gave Lew the space to rebuild SWMM from first principles and gave the rest of us a way to collaborate, test, and critique without legal or proprietary walls in the way.

Lew’s design goal was simple and demanding: a hydrology and hydraulics engine you could both run and read. EPANET had the same DNA: well-organized C, clear functions, and comments that doubled as documentation.

By the early 2000s, the core INP format for SWMM5 felt stable. Every object — junction, conduit, subcatchment, RDII input — had a clear home and syntax. That clarity is why we can still pass SWMM5 models around the world and across decades without losing meaning.

This means the INP file wasn’t just a data container. It became the link between engineers, software, and future versions of ourselves. Now in the age of AI tools it is universally understood by all AIs.

> **What Made SWMM5 Different**

SWMM5 unified every element — nodes, conduits, Subcatchments — into typed structures in C. A conduit became a link object, a node became a node object, a subcatchment became an area object, all managed consistently in memory. That sounds routine now, but at the time it was a major step toward transparency and maintainability.

Routing options were familiar but sharper: Steady flow. Kinematic wave. Dynamic wave — the full Saint Venant equations, documented in the SWMM5 hydraulics reference under dynamic wave analysis.

Most models lived in dynamic wave. That’s where surcharging, backwater, and flow reversal all come into play. Lew coded the solver in a way you could follow: continuity and momentum equations laid out, iterative solution, surcharge checks, and time step control, all visible in the structure of the code.

He didn’t hide the math. Manning’s equation for friction slope appears in his QA report and manuals with units spelled out: Manning’s n in s/m1/31/3, velocity V*V* in m/s, hydraulic radius R*R* in m, conversion factor k*k* tied to units. Variable by variable, the math lined up with the physics.

The edge cases were named, not buried. Surcharged nodes causing oscillations in the Newton iteration. Outfalls with tailwater conditions that can flip flow behavior. Wet/dry transitions where step size and control options in the dynamic wave settings become the difference between convergence and numerical noise.

If you’ve ever stepped through SWMM5’s status report and watched flooding, continuity errors, and flow balances match up, you’re seeing the result of that careful, explicit design.

This means SWMM5’s biggest step wasn’t the GUI. It was the decision that any competent engineer should be able to read the engine and understand what it’s doing. This was also part of SWMM4 and SWMM3 but massive mainframe printouts made it harder to visualize the model.

------------------------------------------------------------------------

> **Seeing the System Like Glass**

We can think of the earlier SWMM versions as watching flow through fogged glass. You saw results, but the internal state was hard to inspect. SWMM5 was more like putting the network inside a glass box. Every node head, every conduit flow, every RDII inflow time series could be traced and plotted. The output structure finally matched how we think about systems in our heads. The code if looked at the code was beautifully written and that code now lives in every AI.

When we run the dynamic wave solver, we’re watching the Saint Venant equations solve in time, but we’re also watching design decisions play out: surcharge relief, ponding, backwater, and storage node behavior. It becomes a conversation between the equations and the network map which you can see in the SWMM UX as themes and 3rd party software.

That’s part of why I like what I call *vibe coding*. Sometimes I write tools or little apps not because the world needs another interface, but because I want to feel the hydraulics and water quality move under a different lens. SWMM5 and EPANET are perfect engines for that kind of exploration due to the code and the wonderful reference manuals by the EPA/Lew.

------------------------------------------------------------------------

> Twelve Years After Retirement

Lew Rossman announced on the SWMM-USERS list that he would retire from USEPA as of April 1, 2014, after more than 30 years of service. That’s a formal retirement date, not an endpoint.

In the years since, he’s still been active through documentation, discussions on EPANET and SWMM, and ongoing support of the modeling community. Many of us still refer back to his explanations on topics like routing algorithms and water quality behavior because the original reasoning is laid out so plainly.

You can measure influence in citations, but you feel it in the day-to-day work. SWMM5 and EPANET are still one of the default engines in countless cities, consulting firms, and universities. This means Lew didn’t just publish tools. He set a standard for how clear environmental modeling code can be. This app connects the dots between EPANET and SWMM5.

> **I. The Problem That No One Talks About**

Isaac Asimov once wrote that the most exciting phrase in science is not "Eureka!" but "That's funny..." The most exciting phrase in water engineering — the one that precedes every major modeling error, every project disaster, every beautifully wrong answer — is this:

*"I'll just use EPANET for this."*

Or its mirror image: *"SWMM5 can handle force mains, right?"*

The problem is not that these tools are bad. The problem is that they are *brilliant* — each in its own domain — and that brilliance makes engineers assume the domains overlap more than they do. SWMM5 and EPANET were written by the same man. They share a file format. They use the word "pipe" with apparent synonymy. And yet, at the level of physics, they are solving fundamentally different mathematical problems for fundamentally different physical systems.

SWMM5 solves the Saint-Venant equations — hyperbolic partial differential equations that describe waves propagating through partially-full pipes. The water has a free surface. The depth varies. The Courant-Friedrichs-Lewy condition governs the timestep. A 100-foot pipe with 5 ft/s flow and a 15 ft/s wave speed demands a timestep no larger than 6.7 seconds. If you violate this, the solver oscillates. The continuity error climbs. The answer becomes physically meaningless. Lew Rossman knew this when he wrote the dynamic wave solver, and the fact that it handles the Preissmann slot transition — a fictitious narrow slot at the pipe crown that maintains a virtual free surface when the pipe surcharges — is one of the quiet masterpieces of computational hydraulics. The slot width for a 48-inch pipe at a target pressure wave speed of 1000 ft/s is 0.0004 feet. That number is absurd. It also works.

EPANET solves something entirely different. There is no free surface. The pipe is always full. Always. The only unknowns are the head at each node and the flow in each pipe. These satisfy algebraic equations — conservation of mass at every junction, conservation of energy along every pipe — solved simultaneously by Newton-Raphson iteration on a sparse matrix. The timestep can be one hour. There is no Courant condition. The solver either converges or it doesn't. It is clean. It is stable. It is, in its own way, beautiful.

Lew Rossman wrote this one too. After thirty years at the EPA, he retired in 2014, and the EPANET user community marked it as the end of an era. The Open Water Analytics community took over development. But the engine — the Gradient Algorithm, the Todini-Pilati formulation, the elegant sparse-matrix solution — that is all Rossman and others. Every pressurized pipe model in the world, or nearly so, traces back to code he wrote in a government office in Cincinnati.

The problem is that engineers trained in one language assume they can speak the other. They cannot. Not without help.

> **II. Gravity Makes Trees. Pressure Makes Loops.**

This is central insight, and it is the kind of first-principle revelation, not because it is surprising, but because, once stated, it becomes so obvious that you wonder why no one said it sooner.

Consider: gravity is a one-way force. Water flows downhill. It cannot flow uphill. It cannot loop back on itself, because a loop would require flowing downhill in one pipe and uphill in another, and the uphill pipe needs a pump — at which point you've left the world of gravity and entered the world of pressure.

Therefore, gravity drainage networks are *trees*. Dendritic. Branching from many sources to few outlets. The natural watershed pattern. Every storm sewer, every sanitary sewer, every combined sewer that ever existed converges toward its outfall like a river toward the sea, because the physics demands it.

Pressure, by contrast, is omnidirectional. A pump can push water uphill, downhill, sideways, or in circles. This freedom allows — and the need for reliability *demands* — looped networks. If any single pipe fails in a dead-end system, everyone downstream loses service. If the same pipe fails in a looped system, water routes around the break. Loops are how you build reliability into a system whose energy source can fail. Gravity doesn't fail. Pumps do.

The app makes this tangible. You can see it. You can *feel* it. The interactive pipe cross-section lets you toggle between SWMM mode and EPANET mode, and the Froude number — that dimensionless ratio of flow velocity to wave speed that governs whether the flow is subcritical or supercritical — appears and disappears like a quantum effect. In SWMM5, the Froude number matters. It determines whether a hydraulic jump will form. It governs the regime. In EPANET, the concept doesn't exist. There's no free surface. There's no wave speed. There's no Froude number. The entire edifice of open-channel hydraulics collapses into a single algebraic equation.

![](https://media.licdn.com/dms/image/v2/D4E12AQGs4RTyvQqw8Q/article-inline_image-shrink_1500_2232/B4EZ0ikCjrGQAU-/0/1774401368093?e=1795651200&v=beta&t=0T-PHzbeQ7c7_c0iSx4h7woR649v3pfYjLbjZ8Lp0Lo)

> **III. The Object-by-Object Translation**

The apps greatest practical contribution is its object-by-object translation dictionary. Every SWMM5 object has a direct or close analog in EPANET, and the app catalogs them with the precision of a lexicographer:

\- **Junction** maps to **Junction** — same name, but the EPANET junction has elevation and demand instead of invert elevation and ponded area, and it has zero storage volume. A SWMM5 junction is a bucket that fills and drains. An EPANET junction is a point in space where flows balance.

\- **Outfall** maps to **Reservoir** — and here the direction flips. The SWMM5 outfall is where water *leaves*. The EPANET reservoir is where water *enters*. The translation requires mental inversion. Rossman understood this intuitively when he designed both boundary conditions.

\- **Conduit** maps to **Pipe** — but the SWMM5 conduit has 20+ cross-section shapes (circular, rectangular, trapezoidal, egg, horseshoe, basket handle) while the EPANET pipe is always circular and always full. The simplification is not a limitation; it is a liberation. EPANET doesn't need the \[XSECTIONS\] section because the geometry is trivial when the pipe is always full.

\- **Subcatchment** maps to **No equivalent** — and this is the most important translation. EPANET has no hydrology. No rainfall. No runoff. No infiltration. No imperviousness. Water enters through reservoirs and leaves through demands. The entire rainfall-runoff process that SWMM5 models from first principles is simply absent. If you are an EPANET expert trying to understand SWMM5, this is the conceptual wall you must climb.

\- **Dry Weather Flow** maps to **Base Demand + Pattern** — and this is the most satisfying translation. The SWMM5 DWF at 0.5 CFS with a diurnal pattern maps directly to an EPANET base demand of 150 GPM with an identical demand pattern. The syntax is nearly identical. The math is identical. The only difference is direction: DWF adds water to the system; demand removes it.

The app shows the .INP files side by side, and the structural similarity is striking. Both use \[SECTION\] headers. Both use semicolon comments. Both use whitespace-delimited fields. If you can read a SWMM5 .inp file — and with 1,700+ blog posts on the subject, the target audience certainly can — you can read an EPANET .inp file with the same eyes.

Rossman designed both formats. The consistency is not accidental. It is the work of an engineer who understood that practitioners would need to move between tools, and who made the file structure a bridge rather than a barrier.

> **IV. The Force Main Converter: Where the Two Worlds Collide**

If there is a single feature in the app that demonstrates its depth, it is the Force Main n↔C Converter.

A force main is a pressurized pipe in a gravity system — a pressurized island in a gravity ocean. It is the physical embodiment of the boundary between SWMM5 and EPANET. Upstream: gravity, free surface, Manning's equation. Downstream: gravity, free surface, Manning's equation. In between: full pipe, pressurized, Hazen-Williams or Darcy-Weisbach. The SWMM5 solver must transition between these two regimes seamlessly, and the equivalent n — the Manning's roughness that produces the same headloss as the given Hazen-Williams C at full-pipe conditions — is the key to that transition.

The app doesn't just compute this. It shows the *actual SWMM5 source code*: double forcemain_getEquivN(int j, int k)

And then it explains what the code does: SWMM5 drops the friction slope term Sf^(-0.04) from the full derivation, treating it as approximately 1.0. This makes the conversion independent of flow conditions but introduces a 20–40% error in the friction slope at typical slopes. It doesn't matter for simulation accuracy because SWMM5 uses H-W directly during force main routing — the equivalent n is only for display.

This is the kind of detail that separates a good educational resource from a great one. Anyone can show the formula. Showing the formula, then showing the source code, then explaining the approximation, then explaining why the approximation doesn't matter — that is the work of someone who has spent years inside the SWMM5 codebase and emerged with understanding, not just familiarity.

The app also distinguishes between the Reference Manual formula (which uses D/S₀ and blows up for flat force mains) and the actual source code formula (which uses R = D/4 and is slope-independent). This is known only to people who have read the source code. Most engineers haven't. The app serves as their guide.

Lew Rossman's fingerprints are everywhere in the SWMM5 source — clean code, well-organized, commented just enough to be readable by others. The fact that the Rosetta Stone app can point to specific functions in specific files and explain their mathematical content is a tribute to that readability. A messier codebase would be unteachable. Rossman's is not.

![](https://media.licdn.com/dms/image/v2/D4E12AQGM3Am8Un0Skw/article-inline_image-shrink_1500_2232/B4EZ0ikSTXHQAU-/0/1774401434328?e=1795651200&v=beta&t=Bs8zc99GwKKpy_M1uVmq0Gakjs2UIPZ-2DwQIWR-hEk)

> **V. The Solver Comparison: Explicit vs. Implicit, Time-Marching vs. Equilibrium**

The app's treatment of the solver comparison is the section that most directly serves the expert audience, and it is superb.

SWMM5's dynamic wave solver is described with appropriate reverence: the staggered finite-difference scheme, the node-link decoupling, the explicit time-marching with Courant-limited timesteps, the Preissmann slot for surcharge transitions, the variable timestep adaptation. These are concepts that SWMM5 modelers use daily but rarely see explained from first principles. The app does both — first principles AND practical implications.

EPANET's Gradient Algorithm is described with equal clarity: the Todini-Pilati formulation, the Newton-Raphson linearization, the sparse matrix assembly, the convergence behavior (5–10 iterations for well-conditioned networks), and the fundamental insight that EPANET finds equilibrium at each timestep rather than marching through transients.

The key comparison — and this is where the app transcends mere reference material — is the Extended Period Simulation equivalence:

\> *"EPANET doesn't track wave propagation through pipes. Instead, it solves a steady-state at each timestep, then updates tank levels and demand patterns for the next step. It's like running SWMM in steady-state mode, then jumping forward in time, updating boundary conditions, and running steady-state again."*

This single paragraph accomplishes what weeks of training courses often fail to achieve: it maps EPANET's temporal behavior onto a concept the SWMM5 expert already understands. The Courant condition. The CFL. The thing that governs every timestep SWMM5 takes. In EPANET, it doesn't exist. The app explains why — there are no waves to track — and then delivers the punchline:

\> *"No Courant condition. No instabilities. No tiny timesteps."*

Six words that free a SWMM5 expert from thirty years of anxiety about continuity errors.

> **VI. The Treatment Expression Editor: Rossman's Ghost in the Machine**

I want to speak briefly about the Treatment Expression Editor, because it represents something important about the app's ambition.

SWMM5 treatment expressions are notoriously difficult to construct. The user must write mathematical expressions using process variables (HRT, FLOW, DEPTH, AREA), built-in functions (EXP, LOG, SQRT, STEP), and cross-references to other pollutants' removal percentages. A typical expression might be: R = k *DEPTH* STEP(DEPTH - d_min)

This says: fractional removal increases with depth above a minimum threshold. If you're an experienced modeler, you can parse this. If you're new, it's opaque.

The app turns this into a visual builder. You click buttons for variables, functions, and operators. You select from template expressions (exponential decay, constant removal, Kadlec-Knight wetland model, settling velocity, depth-dependent removal, co-removal linked to TSS, two-stage bi-exponential). The editor validates your expression in real-time. It shows a treatment curve. It computes influent and effluent concentrations. It exports the expression in SWMM5 format.

This is not a reference tool. This is a *development environment* for treatment expressions. It is the kind of feature that belongs in the official SWMM5 GUI. The fact that someone built it as a web app — and made it free — is an act of genuine generosity to the SWMM5 community.

> **VII. The First Principles Deconstruction: Unlearning as Learning**

The most intellectually ambitious section of the app is the "First-Principles Deconstruction: EPANET → SWMM5." It begins with a provocative premise:

\> *"An EPANET modeler carries a pressurized-pipe, demand-driven, quasi-steady-state mental model into a domain that is open-channel, rainfall-driven, fully unsteady, and nonlinear. Nearly every inherited instinct is wrong or dangerously incomplete."*

It then catalogs every inherited assumption — 20 of them, organized into five categories:

\- **Category A: The Pipe Itself** — six assumptions about full pipes, simple headloss, and instantaneous flow adjustment

\- **Category B: The Node** — five assumptions about dimensionless junctions and demand-driven analysis

\- **Category C: The Solver / Time** — five assumptions about steady-state convergence and benign timesteps

\- **Category D: The System Boundary** — five assumptions about the network being the complete model

\- **Category E: Design Philosophy** — five assumptions about pressure being the answer

For each assumption, the app explains where it comes from (EPANET's framework) and why it breaks in SWMM5's world. Then it rebuilds the mental model from bedrock truths: conservation of mass with time-varying storage, conservation of momentum with all five terms (local acceleration, convective acceleration, pressure gradient, friction, local losses), the free surface as the central variable, gravity as the engine, the catchment as the boundary condition, flow reversal as normal behavior, dry elements as normal states, and the Courant condition as a physical law.

The section concludes with what it calls "The Deepest Trap":

\> *"SWMM5 is not EPANET with rain. It is a rainfall-runoff + unsteady open-channel flow + water quality simulator. EPANET is a steady-state pressurized network solver. They share the word 'pipe' and approximately nothing else at the physics level."*

> **VIII. The Gotchas: Five Things That Will Ruin Your Day**

The app catalogs five "gotchas" for SWMM veterans entering the EPANET world. Each is a land mine:

1\. **Flow units change everything.** EPANET defaults to GPM. SWMM5 uses CFS. A demand of "10" means 10 GPM in EPANET, not 10 CFS. That is a 62× difference. The app flags this prominently.

2\. **Elevation means something different.** In SWMM5, junction elevation is the invert (bottom of the pipe). In EPANET, it's the ground level or pipe centerline. There is no "invert" concept because pipes are full. If you copy SWMM5 invert elevations directly into EPANET, every pressure calculation will be wrong.

3\. **Negative pressures are your "flooding."** In SWMM5, you worry about depth exceeding maximum. In EPANET, the analogous failure mode is pressure dropping below zero. The mental mapping is direct: surcharge → low pressure. Flooding → negative pressure.

4\. **No dynamic routing — water travels instantly.** In SWMM5's dynamic wave, flow propagates at the wave speed. In EPANET, changing a pump status affects the entire network simultaneously at that timestep. The temporal dimension that dominates SWMM5 is absent in EPANET.

5\. **Demand-driven vs. pressure-driven analysis.** Traditional EPANET assumes demands are always met. EPANET 2.2+ supports pressure-driven demand where demands decrease with low pressure. The app correctly identifies this as analogous to SWMM5's surcharge limiting inflow.

Each gotcha includes a one-sentence rule of thumb and a brief explanation. They are exactly the right length — enough to prevent disaster, not so much as to overwhelm.

> **IX. The Quick Reference Card and Decision Guide**

The app concludes with a Quick Reference Card — a single table mapping every concept between SWMM5 and EPANET — and a Decision Guide with a flowchart:

\> *Does rainfall drive the system? → SWMM5.*

\> *Pressurized water distribution network? → EPANET.*

\> *Force mains in collection? → SWMM5 + Force Main.*

\> *Chlorine residual needed? → EPANET + Quality.*

\> *Collection AND distribution together? → Use both.*

This is the section that most practitioners will visit first, and it delivers. The flowchart is correct. The decisions are sound. The guidance is actionable.

> **X. What This App Is and What It Means**

If you model water systems — stormwater, wastewater, drinking water, force mains, or all of the above — you should read this app. And when you're done, you will understand something that most water engineers never fully grasp: that SWMM5 and EPANET are not competing tools. They are complementary tools, each perfectly designed for its domain, each incompletely understood without the other. The Rosetta Stone is the missing manual for the space between them.

Lew Rossman built the two worlds.

*🔗 Bookmark this: \[*[*epanet-swmm-experts.replit.app*](http://epanet-swmm-experts.replit.app)*\](*[*https://epanet-swmm-experts.replit.app/)*](https://epanet-swmm-experts.replit.app/)*)

*📅 Published March 2026*

*🏷️ \#SWMM5 \#EPANET \#Stormwater \#WaterDistribution \#HydraulicModeling \#CivilEngineering \#OpenSource \#WaterResources \#LID \#GreenInfrastructure \#ForceMains \#DigitalTwin*

### Again: Who is the common thread between SWMM5 and EPANET?

***Dedicated to Dr. Lewis A. Rossman****, creator of EPANET at the US EPA (1991–2014). After 30+ years of service, Lew retired in April 2014. Every pressurized pipe model in the world traces back to his work.*

##
