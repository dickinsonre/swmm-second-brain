---
title: "Using 31 Chaotic Systems with Almost Infinite Possibilities to Make SWMM5 Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-31-chaotic-systems-almost-infinite-make-swmm5-robert-dickinson-ms7ie
created: "2025-12-10 20:46"
published: "2025-12-11 07:39"
words: 937
export_sha256: 160545a8bf5b5b4eeda4494d351c0cd920abed8afa7aa64cd55032a017b4b69f
---
# Using 31 Chaotic Systems with Almost Infinite Possibilities to Make SWMM5 Networks

![31 chaotic systems. Infinite possibilities. One Exported SWMM5 network.](https://media.licdn.com/mediaD4E12AQFKUI_E-cNYaQ "31 chaotic systems. Infinite possibilities. One Exported SWMM5 network.")

The problem with using 50 year old simple models or even test models that started out as real models as we did in the SWMM5 redevelopment project are they are too nice for the most (with exceptions). This app uses strange attractors to make complex visually interesting models that look like strange attractors and exhibit a combination of short lengths and oscillating and hilly inverts that really stress SWMM5. Figure 1 shows the app with 31 strange attractor options. Figure 2 shows the hills in SWMM5 and Figure 3 shows how the created attractor looks like in swmm5. The app creates the attractor which is made up of swmm5 nodes and links. The exported SWMM5 model works right away in SWMM5 - see the docs section below to see the model network is set up. As you might expect often there is a continuity error in the model which has to be fixed by adjusting the parameters. This app was made with Replit.

> **The App**

[https://swmm-attractor--robertdickinson.replit.app](https://swmm-attractor--robertdickinson.replit.app)

![](https://media.licdn.com/dms/image/v2/D4E12AQG0j590851DaQ/article-inline_image-shrink_1500_2232/B4EZsKBH1eHUAU-/0/1765399627794?e=1795651200&v=beta&t=_ICJGDPUtVd3E0RlFKxuEIbeH1ZzUkQoLyeLre63W64)

Figure 1. Strange Attractor Ap to generate a swmm5 network.

![](https://media.licdn.com/dms/image/v2/D4E12AQGekInqKiUZRg/article-inline_image-shrink_1500_2232/B4EZsMQ3BfKUAU-/0/1765437305974?e=1795651200&v=beta&t=VRWd4chenxs-fhb62viMVfdwYwm_BoBsC6xf6IBd70c)

Figure 2. Extreme and oscillating inverts.

![](https://media.licdn.com/dms/image/v2/D4E12AQE4fJZeUsL84g/article-inline_image-shrink_1500_2232/B4EZsKBRmnKoAY-/0/1765399667033?e=1795651200&v=beta&t=XpPerG9TCidsVS8phIZ6AHgGrJ_EXD_sSronVWqGgDM)

Figure 3. Created working model in SWMM5.

## Strange Attractors SWMM5 Generator from the App Document

**Where chaos theory meets stormwater management**

Generate EPA SWMM5 hydraulic models that trace the beautiful, chaotic paths of strange attractors. Because drainage networks don't have to be boring!

------------------------------------------------------------------------

### What is this?

This application generates complete, valid EPA SWMM5 input files (.INP) where the drainage network follows the trajectory of various chaotic attractors. The X and Y coordinates define the plan view layout, while the Z coordinate becomes the invert elevation of each junction.

The result? Hydraulically-functional stormwater models shaped like butterflies, spirals, and other strange geometries.

------------------------------------------------------------------------

### Attractor Categories

### Classic (6 systems)

- **Lorenz** - The famous butterfly attractor

- **Rössler** - Spiral-folding chaos

- **Thomas** - Cyclically symmetric attractor

- **Aizawa** - Sphere-tube shaped chaos

- **Dadras** - Complex looping structure

- **Halvorsen** - Cyclically symmetric system

### Lorenz Family (2 systems)

- **Chen** - Lorenz-like with different dynamics

- **Lu** - Unified chaotic system variant

### Electronic (2 systems)

- **Chua** - Double scroll from circuit

- **Chua Multiscroll** - Extended multi-scroll version

### Symmetric (2 systems)

- **Burke-Shaw** - Symmetric folding

- **Rucklidge** - Convection-derived system

### Sprott (5 systems)

- **Sprott A, B, C** - Minimal quadratic systems

- **Sprott-Linz F** - Simplest dissipative flow

- **Nosé-Hoover** - Molecular dynamics system

### Oscillators (2 systems)

- **Duffing** - Driven nonlinear oscillator

- **Van der Pol** - Relaxation oscillator

### Fluid (2 systems)

- **Moore-Spiegel** - Stellar convection model

- **Shimizu-Morioka** - Laser physics system

### Mathematical (6 systems)

- **Genesio-Tesi** - Minimal polynomial system

- **Arneodo** - Cubic nonlinearity jerk

- **Newton-Leipnik** - Two-wing attractor

- **Rabinovich-Fabrikant** - Hidden attractors

- **Wimol-Banlue** - Tanh nonlinearity

- **Finance** - Economic dynamics model

### Hyperchaotic (3 systems)

- **Rössler Hyperchaotic** - 4D variant (3D projection)

- **Qi 4D** - Complex hyperchaotic system

- **Lorenz-Stenflo** - Atmospheric model

### Biological (1 system)

- **Lotka-Volterra** - Predator-prey dynamics

------------------------------------------------------------------------

### Controls

### Playback Controls

- **Play/Pause** - Start or pause the simulation

- **Stop** - Stop simulation and preserve the current trail

- **Reset** - Reset parameters to defaults and restart

### Parameters

Each attractor system has unique parameters. Hover over the help icons for descriptions.

### Global Settings

- **Simulation Speed** - How fast the trajectory is computed (0.1x to 5x)

- **Trail Length** - Number of points in the history buffer (1,000 to 20,000)

### Theme Toggle

Click the sun/moon icon to switch between dark and light themes.

------------------------------------------------------------------------

### SWMM5 Export

### Metric Units

All exports use metric units:

- Flow: **LPS** (liters per second)

- Dimensions: **meters**

- Pipe diameter: **300mm** (circular)

### Network Specifications

- **Junctions**: Max depth 1.2m, surcharge depth 1000m, no ponding

- **Inflow**: 10 LPS baseline at first node (J0)

- **Outfall**: FREE discharge at terminal node

- **Routing**: Dynamic Wave (DYNWAVE)

### What's Generated

- **\[TITLE\]** - Model identification

- **\[OPTIONS\]** - DYNWAVE routing, LPS units, 0.75 variable step

- **\[JUNCTIONS\]** - Nodes with elevations from Z-coordinates

- **\[INFLOWS\]** - 10 LPS at first junction

- **\[OUTFALLS\]** - FREE outfall at terminal node

- **\[CONDUITS\]** - Pipes with calculated 3D lengths

- **\[XSECTIONS\]** - 300mm circular pipes

- **\[COORDINATES\]** - X,Y positions in meters

- **\[VERTICES\]** - Intermediate points for curved conduit paths

### Elevations

- Base elevation starts at 30 meters

- Z-coordinate variations scaled and added to base

- Creates natural gravity flow through the network

------------------------------------------------------------------------

### How It Works

1.  **Generate Trajectory** - Runge-Kutta 4th order integration

2.  **Subsample Nodes** - Every 20th point becomes a junction

3.  **Scale Coordinates** - Maps to engineering units

4.  **Create Network** - Sequential junctions connected by conduits

5.  **Add Vertices** - Intermediate points for curved pipes

6.  **Export INP** - Valid SWMM5 format ready for simulation

------------------------------------------------------------------------

### Tips & Tricks

### Creating Interesting Networks

- Try different attractor categories for varied geometries

- Adjust parameters to change attractor shape

- Higher trail length = more nodes in export

### Best Export Results

1.  Let the simulation run until well-formed

2.  Use Stop to freeze the trail

3.  Export with 5,000+ trail length for substantial networks

### Performance

- Reduce trail length if experiencing slowdown

- Lower simulation speed for smoother animation

- Use light theme in bright environments

------------------------------------------------------------------------

### References

- [EPA SWMM Documentation](https://www.epa.gov/water-research/storm-water-management-model-swmm)

- [Lorenz System](https://en.wikipedia.org/wiki/Lorenz_system)

- [Strange Attractors](https://en.wikipedia.org/wiki/Attractor#Strange_attractor)

- [Sprott's Chaotic Systems](http://sprott.physics.wisc.edu/chaos/chaostsa/)

------------------------------------------------------------------------

*31 chaotic systems. Infinite possibilities. One drainage network.*
