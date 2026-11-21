---
name: Fluid DNA Flow
file: fluid-dna-flow.html
version: 2.0.1
date: 2026-11-21
author: Robert Dickinson
links: {netlify: fluid-dna-flow.html (deploy URL not recorded), artifact: https://claude.ai/artifact/AGKtLdRtUMBBSWGk4yr4um, repo: none, replaces: FluidDnaFlow (Replit app; source zip supplied 2026-11-21)}
engines:
  - {name: Fluid DNA Flow LBM, version: 2.0.0, kind: D2Q9 lattice Boltzmann, collision: BGK (default) or TRT (magic parameter 3/16), subgrid: Smagorinsky Cs 0.10 optional, license: MIT}
units: lattice units in the engine; US customary (ft/s, Hz, psf, lbf/ft) by dynamic similarity for water or air at 60 F
ai_use: built with Claude (Anthropic); see AI use
---

# Fluid DNA Flow: 2D lattice-Boltzmann flow around obstacles, with measured forces

Fluid DNA Flow is a one-file 2D lattice-Boltzmann wind tunnel that measures drag, lift and shedding frequency on any obstacle; on the Schafer-Turek cylinder benchmark its Strouhal number is 0.300, inside the 0.295 to 0.305 band.

This app rebuilds Bob Dickinson's Replit app FluidDnaFlow as a single HTML file. A D2Q9 lattice-Boltzmann engine runs in a Web Worker; the force on the obstacle is summed over every fluid-to-solid link, and the Strouhal number comes from the peak of the lift spectrum. Before release the engine was run in Node against exact and published answers: channel flow matches the exact parabola to round-off with the two-relaxation-time scheme, mass holds to about one part in 10^13, and the Schafer-Turek benchmark gives the right shedding frequency with drag a few percent high from staircase walls. The Replit version blew up within 121 to 289 steps at every setting it shipped with. The limits: two dimensions, Re up to about 1000.

## What it does
A single HTML file that runs a D2Q9 lattice-Boltzmann simulation of 2D flow past an obstacle (cylinder, square, flat plate, NACA 0012 airfoil, round-nose bridge pier, tandem cylinders, DNA-style helix, or cells painted by the user) in a Web Worker. It measures drag and lift every step and the Strouhal number from the lift spectrum, compares two Reynolds numbers side by side, runs its own verification checks in the browser, converts results to US customary units, and has an Ask tab that answers only from engine runs and asks the user to predict first in Learn mode. Rebuilt from the Replit app FluidDnaFlow (React, Express, Drizzle), whose server only served source text to its documentation page.

## How it computes
- Lattice: D2Q9, directions 0 rest, 1 E, 2 N, 3 W, 4 S, 5 NE, 6 NW, 7 SW, 8 SE; weights 4/9, 1/9, 1/36.
- Equilibrium: f_eq_i = w_i rho (1 + 3 c_i.u + 4.5 (c_i.u)^2 - 1.5 u.u).
- Collision: BGK f* = f - (f - f_eq)/tau; TRT splits pairs into symmetric (tau+) and antisymmetric (tau-) parts with (tau+ - 1/2)(tau- - 1/2) = 3/16.
- Viscosity: nu = (tau - 1/2)/3; the user sets Re, the app sets nu = U L / Re with L the body's reference length in cells (diameter, side, plate height, chord = 2.5 x base size, pier width, helix height).
- Subgrid (optional): Smagorinsky, tau_eff = (tau + sqrt(tau^2 + 18 sqrt(2) Cs^2 |Pi_neq| / rho)) / 2, Cs = 0.10.
- Streaming: fused collide-and-push through a precomputed link table (Int32Array, 9 N entries).
- Walls: halfway bounce-back (no-slip), specular reflection (slip) or periodic, on the top and bottom; bodies by halfway bounce-back.
- Inlet and outlet: Guo, Zheng and Shi (2002) non-equilibrium extrapolation; inlet velocity uniform (live view) or parabolic (benchmarks), outlet density 1.
- Force: momentum exchange, F = sum over fluid-to-solid links of 2 f_i c_i (Ladd 1994), reported as the mean of two consecutive steps (moves the 2D-2 peaks by less than 1e-5). Cd = 2 Fx / (rho U^2 L), Cl = 2 Fy / (rho U^2 L).
- Strouhal: peak of a Hann-windowed Fourier transform of Cl over the last 40 L/U, St 0.04 to 0.45, parabolic refinement; the side-wall acoustic tone cs/(2 ny) and two harmonics are skipped (+/- 8 percent); shedding when the peak's Cl amplitude exceeds 0.05 over 3 or more cycles.
- Blow-up guard: the run stops when density at sampled nodes leaves 0.2 to 5.
- Stability verdict: Mach = U sqrt(3) > 0.45 "mach"; tau < 0.505 "tau-low"; tau < 0.53 or Mach > 0.3 "marginal"; otherwise ok.

## Inputs and outputs
Inputs: Reynolds number 10 to 1000 (typed 5 to 2000), lattice speed U 0.02 to 0.30, shape, size, angle, grid (200 x 80, 320 x 128, 480 x 192), side walls, collision model, subgrid model; URL query parameters re, u, shape, size, ang, grid, walls, coll, les, field, theme on a normal host. Outputs: PNG snapshot, field CSV (i, j, x/L, y/L, solid, u/U, v/U, Cp, vorticity L/U), force CSV (step, t U/L, Cd, Cl), Verify CSV, Ask ledger CSV, captioned GIF (own LZW encoder, no network), this file.

## Checks
All run on engine.js as shipped, Node 22.23, before release; the Verify tab reruns them in the browser.
- Poiseuille, H = 20 cells, body force 1e-6: TRT L2 relative error 1.9e-12, 5.7e-12, 1.7e-11, 2.8e-12, 6.2e-12, 1.8e-12 at tau 0.600, 0.800, 0.933, 1.000, 1.500, 2.000; BGK 3.2e-3, 1.8e-3, 2.7e-11, 1.1e-3, 1.5e-2, 3.8e-2 (exact only at tau 0.933).
- Mass in a closed channel with a cylinder, 5000 steps: relative change below 1e-13 for no-slip, slip and periodic walls (BGK and TRT).
- Null control: no obstacle gives 0 body links and force exactly 0. Determinism: two identical runs, 2000 steps, force series bit-identical.
- Schafer-Turek 2D-1, Re 20 (steady), D 20 cells, U 0.025, TRT: Cd 5.679, Cl 0.01079 (reference Cd 5.57 to 5.59, Cl 0.0104 to 0.0110).
- Schafer-Turek 2D-1, Re 20 (steady), D 20 cells, U 0.05, TRT (Verify full): Cd 5.766, Cl 0.01088 (reference same).
- Schafer-Turek 2D-1, Re 20 (steady), D 20 cells, U 0.10, TRT: Cd 6.164, Cl 0.01138 (reference same).
- Schafer-Turek 2D-1, Re 20 (steady), D 10 cells, U 0.05, TRT (Verify quick): Cd 5.822, Cl 0.01232 (reference same).
- Schafer-Turek 2D-2, Re 100 (shedding), D 20 cells, U 0.06, TRT (Verify full): Cd max 3.425, Cl max 1.125, St 0.3001 (reference Cd max 3.22 to 3.24, Cl max 0.99 to 1.01, St 0.295 to 0.305).
- Schafer-Turek 2D-2, Re 100 (shedding), D 20 cells, U 0.035, TRT: Cd max 3.407, Cl max 1.093, St 0.2988 (reference same).
- Schafer-Turek 2D-2, Re 100 (shedding), D 10 cells, U 0.10, BGK (Verify quick): Cd max 3.743, Cl max 0.998, St 0.2984 (reference same).
- Cd at zero Mach, 2D-1, D = 20, extrapolated in U^2 from U 0.05 and 0.025: 5.650.
- Strouhal vs Williamson fit (St = -3.3265/Re + 0.1816 + 0.00016 Re), slip walls 8 D apart: D = 10: Re 50 St 0.1458 (18.5 %); Re 60 St 0.1545 (13.8 %); Re 80 St 0.1675 (9.6 %); Re 100 St 0.1767 (7.5 %); Re 130 St 0.1844 (4.3 %); Re 160 St 0.1907 (2.3 %); Re 180 St 0.1945 (1.3 %). D = 16: Re 60 St 0.1570 (15.7 %); Re 80 St 0.1714 (12.2 %); Re 100 St 0.1813 (10.3 %); Re 130 St 0.1918 (8.5 %); Re 160 St 0.2008 (7.7 %); Re 180 St 0.2061 (7.4 %).
- Side-wall acoustic tone: 2 ny / cs = 443.6 steps on the 128-cell grid; lift spectrum second peak at St 0.446 to 0.448 against 0.451 predicted.")[0]}; mutants caught: .
- Replit engine (client/src/lib/lattice-boltzmann.ts, unchanged, Node with type stripping): NaN at step 138, 289, 172, 121 for default, Laminar, Vortex Street and High Re; identical results at Re 10 and 1000; no NaN in 600 steps at u = 0.1; its top and bottom wall rule conserves mass to 1.6e-13 over 5000 steps.
- Speed (Node, one core): 320 x 128, BGK 25 million cell updates per second (611 steps/s); TRT 19.

## What this does not show
- Three-dimensional flow. Above about Re 190 a real cylinder wake develops spanwise structure that a 2D model cannot have.
- High Reynolds numbers. The lattice runs to about Re 1000 with the Smagorinsky subgrid model, which adds viscosity where the flow shears; above that, and even near it, treat the pattern as qualitative.
- Curved surfaces. Bodies are whole cells. Peak drag on the benchmark runs 6.0 percent high at 20 cells per diameter, and peak lift 12.5 percent high.
- Incompressible flow. The lattice fluid is slightly compressible: forces drift with the Mach number, sound rings between the side walls, and the impulsive start sends pressure pulses that show as faint vertical stripes near the inlet for a while. The live tiles skip the first 10 convective times for that reason.
- Field data. Every check is against an exact solution, a published benchmark or a published fit. None is against a measured flume or river.
- The Ask tab offline understands only the phrasings listed in its chips. With Claude available it can call only the engine's own tools, and it cannot apply a change without your click.
- Known defects in this edition: (1) TRT unstable with the open boundaries below tau about 0.53 (default is BGK); (2) staircase bodies, no curved-boundary correction; (3) at D = 20 the 2D-2 peaks run high: Cd max 6.0 percent and Cl max 12.5 percent from their band centres.

## Defect register: the Replit version
### LD-1. Inflow speed far above the lattice speed of sound
```
// ControlPanel.tsx
<input type="range" ... min="0.1" max="5.0" step="0.1" value={simulationState.velocity} .../>
// simulation.tsx
velocity: urlParams.velocity ?? 2.0,
// presets
laminar: { ..., viscosity: 0.15, velocity: 1.0 }, vortex: { ..., viscosity: 0.08, velocity: 2.5 }, turbulent: { ..., viscosity: 0.02, velocity: 4.0 }
```
What it did: The lattice speed of sound is 1/sqrt(3) = 0.577 cells per step, so the default 2.0 is Mach 3.46. The Replit engine, run unchanged in Node, went to NaN at step 138 with the defaults and at steps 289, 172 and 121 with the three presets; with u = 0.1 it ran 600 steps cleanly. On screen, NaN fell through the colour map and painted the field one flat colour, with no message.

In this edition: U slider 0.02 to 0.30, default 0.08; Mach shown live with a warning past 0.17; a run stops when its density leaves 0.2 to 5, with a banner that says why.

### LD-2. Reynolds slider not connected to the physics
```
// lattice-boltzmann.ts
this.reynolds = params.reynolds;
this.omega = 1.0 / (3.0 * this.viscosity + 0.5);
```
What it did: Re was stored and displayed but the relaxation rate came from viscosity alone. Runs at Re 10 and Re 1000, everything else equal, were identical (both NaN at step 138).

In this edition: The Reynolds number sets the viscosity through nu = U L / Re, using the body's own reference length in cells.

### LD-3. Compare mode compared a run with itself
```
// ComparisonCanvas.tsx
lbmARef.current = new LatticeBotzmann(halfWidth, gridHeight, { viscosity: simulationState.viscosity, velocity: simulationState.velocity, reynolds: reynoldsA });
lbmBRef.current = new LatticeBotzmann(halfWidth, gridHeight, { viscosity: simulationState.viscosity, velocity: simulationState.velocity, reynolds: reynoldsB });
```
What it did: Because Re was unused (LD-2), both halves ran the same viscosity and speed under different Re labels, on the main thread.

In this edition: Each Compare run gets nu from its own Re and runs in its own Web Worker.

### LD-4. Time Step box not connected
```
// ControlPanel.tsx
<Input type="number" value={simulationState.timeStep}
       onChange={(e) => onParameterChange('timeStep', parseFloat(e.target.value))} .../>
```
What it did: timeStep was stored in the page state and read nowhere else; the lattice step is always 1.

In this edition: Removed. The lattice time step is fixed at 1; Steps per frame sets how fast time runs on screen.

### LD-5. Drag coefficient was a pressure difference, and the shape labels were high-Re values
```
// lattice-boltzmann.ts getDragCoefficient()
const deltaPressure = (upstreamPressure / upCount) - (downstreamPressure / downCount);
const dynamicPressure = 0.5 * 1.0 * this.velocity * this.velocity;
return Math.abs(deltaPressure / dynamicPressure);
// ControlPanel.tsx
<SelectItem value="cylinder">Cylinder (Cd ~1.0-1.2)</SelectItem>
<SelectItem value="square">Square (Cd ~2.0-2.2)</SelectItem>
<SelectItem value="airfoil">Airfoil (Cd ~0.02-0.05)</SelectItem>
```
What it did: The 'drag coefficient' compared pressure five cells upstream and downstream across the body's height and dropped the sign: not a force, and blind to friction drag. The labels are values for Reynolds numbers in the tens of thousands, not for the 10 to 1000 the app could reach.

In this edition: Force summed as 2 f c over every fluid-to-solid link each step (momentum exchange); Cd and Cl live; reference values quoted only from the Schafer-Turek benchmark.

### LD-6. Shapes built from circles; the square was hollow
```
// obstacle-shapes.ts generateSquare(): small circles along the four sides only
for (let side = 0; side < 4; side++) {
  ...
  this.obstacles.push({ x: rx, y: ry, radius: size * 0.25 });
}
```
What it did: Rasterized with the Replit code on its medium grid, the medium square is 188 solid cells around 65 cells of fluid sealed inside; the cylinder is 19 circles with 4 sealed cells. The airfoil and helix had none.

In this edition: Disk, rotated square, flat plate, NACA 0012 thickness formula, round-nose pier, tandem pair and helix, each tested at cell centres.

### LD-7. Physical units were fixed SI scale factors
```
// PerformanceMetrics.tsx
const PHYSICAL_SCALE = { length: 0.001, velocity: 0.01, pressure: 1000 };
```
What it did: Lattice velocity times 0.01 was shown as m/s and pressure times 1000 as Pa, tied to no Reynolds number, fluid or body size.

In this edition: V = Re nu / L for the chosen fluid and body size, then f = St V / L and drag per foot = Cd q L.

## How to reproduce
Node 22: `node tests/t1.js` (Poiseuille, mass, null, determinism, speed); `node tests/st.js 1|2 D U bgk|trt` (Schafer-Turek); `node tests/sweep.js low|med 60,80,100` (Strouhal); `node tests/stab.js`; `node tests/trtper.js`; `node tests/chat_test.js`. The engine is the text of the script element engine-src in the HTML; save it as engine.js.

## Credits and licenses
Original app and direction: Robert Dickinson. Methods: Frisch, Hasslacher and Pomeau (1986); McNamara and Zanetti (1988); Qian, d'Humieres and Lallemand (1992); Ginzburg's two-relaxation-time scheme; Guo, Zheng and Shi (2002); Hou and co-workers (1996); Ladd (1994). Benchmarks: Schafer and Turek (1996); Williamson's Strouhal fit. Engine-chat kernel v1.0 from Bob's socratic-engine-chat skill, with call and commit made async. License: MIT.

## AI use
This edition was built with Claude, Anthropic's AI model (Claude Opus 5.5), in November 2026, under the direction of Robert (Bob) Dickinson, who wrote the original Replit app FluidDnaFlow, asked for the single-file rebuild and is responsible for the result. Claude read the Replit source, ran its engine in Node to find the defects in the register (LD-1 to LD-7), wrote the new lattice-Boltzmann engine, the page, the Ask tab's tools and tests, the GIF encoder, the Doc essay, this .docx and the technical summary (.md). The checks are mechanical, not the AI's judgment: an exact channel solution, mass and null controls, the Schafer-Turek benchmark, Williamson's Strouhal fit, and a 88-check test suite for the Ask tab that four deliberately broken copies of its kernel each fail. No person has yet checked the essay's history against the original papers or run the Verify buttons in a browser other than the build machine's headless Chromium.

## Changes
- 2.0.1 (2026-11-21): canvas resizing moved out of the ResizeObserver callback into the next animation frame; resizing inside the callback raised "ResizeObserver loop completed with undelivered notifications" in the artifact viewer. Engine unchanged (2.0.0).
- 2.0.0 (2026-11-21): single-file rebuild of the Replit FluidDnaFlow; new engine (typed arrays, link table, BGK and TRT, LES, Guo boundaries, momentum-exchange force, spectral Strouhal); Compare in workers; Verify tab with defect register; Ask tab; US customary units; own GIF encoder; Doc tab, .docx and this file.
