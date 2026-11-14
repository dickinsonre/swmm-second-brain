---
title: "Exploring EPASWMM5 Code Variables Through the Lens of Visual AI (w/Emoji)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/exploring-epaswmm5-code-variables-through-lens-visual-dickinson-4zcpe
created: "2023-11-23 13:42"
published: "2023-11-23 16:09"
words: 2737
export_sha256: 9594990a98c053dbfd22a2fbc1d348d5321650189f6f8dadec2d0e4a949e3d49
---
# Exploring EPASWMM5 Code Variables Through the Lens of Visual AI (w/Emoji)

![](https://media.licdn.com/mediaD4E12AQE_BbLlIpRuDg)

In this approach to understand the SWMM 5.2.4 C code, particularly the .h files, a visual representation using emojis was created. This project, executed by GPT-4, provides a unique and engaging perspective on some of the main constants and data objects in the software. To maintain focus, the visualization was limited to ten key sections. Below is a summary of these sections:

1.  **🔍 Data Objects in SWMM5:** Representation of various data objects used in SWMM5.

2.  **📋 Input Option Types for SWMM5:** Types of input options available for configuring the model.

3.  **SWMM5 📋 Input Section Types:** Different input sections encountered in the model's configuration.

4.  **📐 Cross Section Shape Types:** Shapes for cross-sections of channels, pipes, or other structures.

5.  **Constants in SWMM5:** Fundamental constants used throughout the program.

6.  **Computed SWMM5 Output Quantities:** Enumerated computed results for subcatchments, nodes, links, and system-wide metrics.

7.  **Constants for Link Flow, Buildup/Washoff, Time Series and Runoff:** Specific constants related to flow dynamics, pollution Buildup, and Washoff.

8.  **SWMM 5.2.4 Control Constants Overview 📚:** Overview of control constants in the software.

9.  **Infiltration Constants:** Constants related to the infiltration processes in the model.

10. **🌟 SWMM5 Calibration Files Overview 🌟:** Overview of calibration files and their significance in the model.

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 1 - 🔍 Data Objects in SWMM5**

### 📚🔍 Data Objects:

- *Temp (TTemp):* 🌡️ Temperature data ➡️ 🌡️

- *Evap (TEvap):* 💧 Evaporation data ➡️ ☀️💧

- *Wind (TWind):* 🌬️ Wind speed data ➡️ 🌬️

- *Snow (TSnow):* ❄️ Snow melt data ➡️ ❄️

- *Adjust (TAdjust):* ⚙️ Climate adjustments ➡️ 🔄

- *Snowmelt (TSnowmelt*):\* 🌨️ Array of snow melt objects ➡️ 🌨️

- *Gage (TGage*):\* 🌧️ Array of rain gages ➡️ 🌧️

- *Subcatch (TSubcatch*):\* 🏞️ Array of subcatchments ➡️ 🏞️

- *Aquifer (TAquifer*):\* 🌊 Array of groundwater aquifers ➡️ 🌊

- *UnitHyd (TUnitHyd*):\* 📊 Array of unit hydrographs ➡️ 💹

- *Node (TNode*):\* 📍 Array of nodes ➡️ 📍

- *Outfall (TOutfall*):\* 🚰 Array of outfall nodes ➡️ 🚰

- *Divider (TDivider*):\* ➗ Array of divider nodes ➡️ ➗

- *Storage (TStorage*):\* 📦 Array of storage nodes ➡️ 📦

- *Link (TLink*):\* 🔗 Array of links ➡️ 🔗

- *Conduit (TConduit*):\* 🚇 Array of conduit links ➡️ 🚇

- *Pump (TPump*):\* 🌪️ Array of pump links ➡️ 🌪️

- *Orifice (TOrifice*):\* ⭕ Array of orifice links ➡️ ⭕

- *Weir (TWeir*):\* 🚧 Array of weir links ➡️ 🚧

- *Outlet (TOutlet*):\* 🛍️ Array of outlet device links ➡️ 🛍️

- *Pollut (TPollut*):\* ☠️ Array of pollutants ➡️ ☠️

- *Landuse (TLanduse*):\* 🌲 Array of land uses ➡️ 🌲

- *Pattern (TPattern*):\* 🎨 Array of time patterns ➡️ 🎨

- *Curve (TTable*):\* 📈 Array of curve tables ➡️ 📈

- *Tseries (TTable*):\* 🕰️ Array of time series tables ➡️ 🕰️

- *Transect (TTransect*):\* 📏 Array of transect data ➡️ 📏

- *Street (TStreet*):\* 🛣️ Array of defined street cross-sections ➡️ 🛣️

- *Shape (TShape*):\* ⛓️ Array of custom conduit shapes ➡️ ⛓️

- *Event (TEvent*):\* 🎉 Array of routing events ➡️ 🎉

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 2 - 📋 Input Option Types for SWMM5**

📋 **Input Option Types:** Types of input options available for configuring a stormwater management model.

- FLOW_UNITS: Units for flow measurements. ➡️ 🚰

- INFIL_MODEL: Infiltration model selection. ➡️ 💧

- ROUTE_MODEL: Routing model selection. ➡️ 🚶‍♂️

- START_DATE: Simulation start date. ➡️ 📅

- START_TIME: Simulation start time. ➡️ 🕗

- END_DATE: Simulation end date. ➡️ 📆

- END_TIME: Simulation end time. ➡️ 🕖

- REPORT_START_DATE: Start date for report generation. ➡️ 📅📊

- REPORT_START_TIME: Start time for report generation. ➡️ 🕗📊

- SWEEP_START: Street cleaning start month. ➡️ 🧹🗓️

- SWEEP_END: Street cleaning end month. ➡️ 🧹🛑

- START_DRY_DAYS: Initial dry days before simulation. ➡️ ☀️📅

- WET_STEP: Time step for wet weather conditions. ➡️ 🌧️⏲️

- DRY_STEP: Time step for dry weather conditions. ➡️ ☀️⏲️

- ROUTE_STEP: Time step for routing. ➡️ 🚶‍♂️⏲️

- RULE_STEP: Time step for control rule processing. ➡️ 📜⏲️

- REPORT_STEP: Time step for report generation. ➡️ 📊⏲️

- ALLOW_PONDING: Flag to allow water ponding in conditions. ➡️ 🚫🌊

- INERT_DAMPING: Inertia damping option for flow calculations. ➡️ ⚖️🌊

- SLOPE_WEIGHTING: Weighting of slope in flow calculations. ➡️ 📉🌊

- VARIABLE_STEP: Allow variable time step option. ➡️ ⌛

- NORMAL_FLOW_LTD: Limit for normal flow conditions. ➡️ 🚫🌊

- LENGTHENING_STEP: Time step lengthening factor. ➡️ 📏⏲️

- MIN_SURFAREA: Minimum surface area for stability. ➡️ 📏🌍

- COMPATIBILITY: Model compatibility mode. ➡️ 🔄

- SKIP_STEADY_STATE: Skip initial steady-state phase. ➡️ ➡️🛑

- TEMPDIR: Temporary directory for intermediate files. ➡️ 📂🔄

- IGNORE_RAINFALL: Ignore rainfall data during simulation. ➡️ 🚫🌧️

- FORCE_MAIN_EQN: Equation type for force main calculations. ➡️ 📜=️

- LINK_OFFSETS: Offset method for links. ➡️ ➡️🔗

- MIN_SLOPE: Minimum slope for channels/pipes. ➡️ 📉🚰

- IGNORE_SNOWMELT: Ignore snowmelt data during simulation. ➡️ 🚫❄️

- IGNORE_GWATER: Ignore groundwater during simulation. ➡️ 🚫⛲

- IGNORE_ROUTING: Ignore routing processes during simulation. ➡️ 🚫🚶‍♂️

- IGNORE_QUALITY: Ignore water quality processes. ➡️ 🚫💧

- MAX_TRIALS: Maximum trials for iterative methods. ➡️ 🔄🔢

- HEAD_TOL: Tolerance for hydraulic head calculations. ➡️ 🌊⚖️

- SYS_FLOW_TOL: System flow tolerance for balance. ➡️ 🚰⚖️

- LAT_FLOW_TOL: Lateral flow tolerance for balance. ➡️ ➡️🚰⚖️

- IGNORE_RDII: Ignore RDII data. ➡️ 🚫🌧️➡️

- MIN_ROUTE_STEP: Minimum routing time step. ➡️ 🚶‍♂️⏳

- NUM_THREADS: Number of computational threads. ➡️ 🔄🔢

- SURCHARGE_METHOD: Method for calculating surcharge. ➡️ 🌊📜

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 3 - SWMM5** 📋 **Input Section Types**

📋 **Input Section Types:** Types of input sections in a stormwater management model configuration or input file.

- s_TITLE: Title/header of the model/data. ➡️ 📜

- s_OPTION: Model/simulation options. ➡️ ⚙️

- s_FILE: File references/paths. ➡️ 📂

- s_RAINGAGE: Rainfall measurement devices. ➡️ 🌧️

- s_TEMP: Temperature data/settings. ➡️ 🌡️

- s_EVAP: Evaporation parameters/data. ➡️ 💨

- s_SUBCATCH: Subcatchment definitions. ➡️ 🌍

- s_SUBAREA: Sub-area properties within subcatchment. ➡️ 🟩

- s_INFIL: Infiltration parameters. ➡️ 💧

- s_AQUIFER: Groundwater aquifer properties. ➡️ 🌊

- s_GROUNDWATER: Groundwater related data/settings. ➡️ ⛲

- s_SNOWMELT: Snowmelt parameters/data. ➡️ ❄️

- s_JUNCTION: Junction nodes in drainage system. ➡️ ➕

- s_OUTFALL: Outfall nodes/discharge points. ➡️ 🔚

- s_STORAGE: Storage unit definitions (ponds/reservoirs). ➡️ 🚰

- s_DIVIDER: Flow dividers/splitting nodes. ➡️ ↔️

- s_CONDUIT: Conveyance channels/pipes. ➡️ 🚇

- s_PUMP: Pump stations/facilities. ➡️ 💹

- s_ORIFICE: Orifice flow control structures. ➡️ ⭕

- s_WEIR: Weir flow control structures. ➡️ 🌊

- s_OUTLET: Outlet structures/nodes. ➡️ 🔛

- s_XSECTION: Cross-sectional properties of channels/pipes. ➡️ 📏

- s_TRANSECT: Irregular channel cross-sectional data. ➡️ 📐

- s_LOSSES: Conveyance loss parameters. ➡️ ➖

- s_CONTROL: Control rules/logic for system. ➡️ 🎛️

- s_POLLUTANT: Pollutant definitions/properties. ➡️ ☣️

- s_LANDUSE: Land use categories/properties. ➡️ 🌲

- s_BUILDUP: Pollutant buildup settings. ➡️ 📈

- s_WASHOFF: Pollutant washoff parameters. ➡️ 🚿

- s_COVERAGE: Land use coverage data. ➡️ 🌍

- s_INFLOW: External inflow data/settings. ➡️ ➡️

- s_DWF: Dry weather flow parameters. ➡️ ☀️

- s_PATTERN: Repeating patterns for parameters. ➡️ 🔁

- s_RDII: Rainfall-dependent inflow/infiltration data. ➡️ 🌧️➡️

- s_UNITHYD: Unit hydrograph definitions. ➡️ 📉

- s_LOADING: Pollutant loading data. ➡️ ⚖️

- s_TREATMENT: Treatment facility/mechanism definitions. ➡️ 🏥

- s_CURVE: Generic curve data (e.g., pump curves). ➡️ 📈

- s_TIMESERIES: Time series data/references. ➡️ 🕐

- s_REPORT: Reporting options/settings. ➡️ 📊

- s_COORDINATE: Geographical coordinates. ➡️ 🌐

- s_VERTICES: Vertices for irregular shapes/paths. ➡️ ⭐

- s_POLYGON: Polygonal area definitions. ➡️ ⬛

- s_LABEL: Labels/annotations. ➡️ 🏷️

- s_SYMBOL: Symbols/icons. ➡️ ❇️

- s_BACKDROP: Backdrop/background settings. ➡️ 🖼️

- s_TAG: Tags/metadata. ➡️ 🏷️

- s_PROFILE: Profile views/settings. ➡️ 📏

- s_MAP: Map data/settings. ➡️ 🗺️

- s_LID_CONTROL: Low Impact Development control parameters. ➡️ 🌱

- s_LID_USAGE: Usage settings for Low Impact Development controls. ➡️ 🌿

- s_GWF: Groundwater flow settings. ➡️ ⛲

- s_ADJUST: Adjustment/calibration parameters. ➡️ 🔧

- s_EVENT: Specific rainfall/other events. ➡️ 🌩️

- s_STREET: Street/roadway properties. ➡️ 🛣️

- s_INLET_USAGE: Usage settings for street inlets. ➡️ 🕳️

- s_INLET: Inlet design/properties. ➡️ ⬇️

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 4 -** 📐 **Cross Section Shape Types**

📐 **Cross Section Shape Types:** Different shapes for cross-sections of conveyance structures in the stormwater system.

- DUMMY: 0️⃣ Placeholder or undefined shape.

- CIRCULAR: 🟠 1️⃣ Closed circle.

- FILLED_CIRCULAR: 🟡 2️⃣ Filled circle (with substance/obstruction).

- RECT_CLOSED: 🟥 3️⃣ Closed rectangle.

- RECT_OPEN: 🟩 4️⃣ Open rectangle (like a trench).

- TRAPEZOIDAL: 📏 5️⃣ Trapezoid shape.

- TRIANGULAR: 📐 6️⃣ Triangle shape.

- PARABOLIC: 🌌 7️⃣ Parabola shape.

- POWERFUNC: 8️⃣ Shape defined by a power function.

- RECT_TRIANG: 📏 9️⃣ Combination of rectangle and triangle.

- RECT_ROUND: 🟪 1️⃣0️⃣ Rounded rectangle.

- MOD_BASKET: 🧺 1️⃣1️⃣ Modified basket shape.

- HORIZ_ELLIPSE: 🥚 1️⃣2️⃣ Horizontal ellipse (closed).

- VERT_ELLIPSE: 🥚 1️⃣3️⃣ Vertical ellipse (closed).

- ARCH: 🌈 1️⃣4️⃣ Arch shape (closed).

- EGGSHAPED: 🥚 1️⃣5️⃣ Egg-shaped (closed).

- HORSESHOE: 🐴 1️⃣6️⃣ Horseshoe shape (closed).

- GOTHIC: ⛪ 1️⃣7️⃣ Gothic arch shape (closed).

- CATENARY: 🌌 1️⃣8️⃣ Catenary curve shape (closed).

- SEMIELLIPTICAL: 🌓 1️⃣9️⃣ Semi-elliptical shape (closed).

- BASKETHANDLE: 🧺 2️⃣0️⃣ Basket handle shape (closed).

- SEMICIRCULAR: 🌓 2️⃣1️⃣ Semi-circular shape (closed).

- IRREGULAR: ⚪ 2️⃣2️⃣ Irregular or undefined shape.

- CUSTOM: 🟣 2️⃣3️⃣ Custom shape (closed).

- FORCE_MAIN: 💪 2️⃣4️⃣ Main force/pressure pipe shape (closed).

- STREET_XSECT: 🛣️ 2️⃣5️⃣ Street cross-section.

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 5 - Constants in SWMM5**

🌐 **General Constants:** These constants are fundamental values used throughout the program:

- VERSION: 52000 ➡️ 🆔📈 (Software version)

- MAGICNUMBER: 516114522 ➡️ 🎩✨ (Unique identifier)

- EOFMARK: 0x1A ➡️ 📝🔚 (End-of-file mark)

- MAXTITLE: 3 ➡️ 📜🔝 (Maximum title lines)

- MAXMSG: 1024 ➡️ 📝🔝 (Max message text characters)

- MAXLINE: 1024 ➡️ 📄🔝 (Max characters per input line)

- MAXFNAME: 259 ➡️ 📂🔝 (Max file name characters)

- MAXTOKS: 40 ➡️ 📊🔝 (Max items per input line)

- MAXSTATES: 10 ➡️ 🌊🔢 (Max hydraulic variables)

- MAXODES: 4 ➡️ 🧮🔝 (Max ODE's)

- NA: -1 ➡️ 🚫🔢 (Not applicable code)

- TRUE: 1 ➡️ ✅ (True state)

- FALSE: 0 ➡️ ❌ (False state)

- BIG: 1.E10 ➡️ 📈🔝 (Large value)

- TINY: 1.E-6 ➡️ 📉🔝 (Small value)

- ZERO: 1.E-10 ➡️ 0️⃣ (Zero value)

- MISSING: -1.E10 ➡️ ❓🔢 (Missing value code)

- PI: 3.141592654 ➡️ π (Value of pi)

- GRAVITY: 32.2 ➡️ 🌍⬇️ (Gravity in US units)

- SI_GRAVITY: 9.81 ➡️ 🌍⬇️📏 (Gravity in SI units)

🚰 **Hydraulic Constants:** These constants pertain to hydrological and hydraulic calculations:

- PHI: 1.486 ➡️ 🌊📏 (Manning Equation factor)

- MIN_RUNOFF_FLOW: 0.001 ➡️ 💧🔍 (Minimal runoff flow)

- MIN_TOTAL_DEPTH: 0.004167 ➡️ 🌊🔍 (Minimal total depth)

- FLOW_TOL: 0.00001 ➡️ 🛤️🔍 (Flow tolerance for steady state)

- FUDGE: 0.0001 ➡️ 🌊📊 (Minimum flow depth and area)

🔄 **Conversion Factors:** These constants are used for unit conversions:

- GPMperCFS: 448.831 ➡️ 🚰🔄 (Gallons/min per cfs)

- AFDperCFS: 1.9837 ➡️ 🌊🔄 (Acre-feet/day per cfs)

- MGDperCFS: 0.64632 ➡️ 🚰📈 (Million gallons/day per cfs)

- IMGDperCFS: 0.5382 ➡️ 🚰🇬🇧 (Imperial million gallons/day per cfs)

- LPSperCFS: 28.317 ➡️ 💧🔄 (Liters/sec per cfs)

- LPMperCFS: 1699.0 ➡️ 💧🕒 (Liters/min per cfs)

- CMHperCFS: 101.94 ➡️ 🌊🕒 (Cubic meters/hour per cfs)

- CMDperCFS: 2446.6 ➡️ 🌊📅 (Cubic meters/day per cfs)

- MLDperCFS: 2.4466 ➡️ 💧📈 (Million liters/day per cfs)

- M3perFT3: 0.028317 ➡️ 📏🔄 (Cubic meters per cubic foot)

- LperFT3: 28.317 ➡️ 💧📏 (Liters per cubic foot)

- MperFT: 0.3048 ➡️ 📏🔄 (Meters per foot)

- PSIperFT: 0.4333 ➡️ 💪📏 (Pounds/square inch per foot)

- KPAperPSI: 6.895 ➡️ 💪🔄 (Kilopascals per psi)

- KWperHP: 0.7457 ➡️ ⚡🔄 (Kilowatts per horsepower)

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 6 - Computed SWMM5 Output Quantities**

📋 **Computed Subcatchment Quantities:** Defining computed results for subcatchments in a stormwater management model.

- SUBCATCH_RAINFALL: Rainfall intensity. ➡️ 🌧️

- SUBCATCH_SNOWDEPTH: Snow depth. ➡️ ❄️

- SUBCATCH_EVAP: Evaporation loss. ➡️ ☁️

- SUBCATCH_INFIL: Infiltration loss. ➡️ 💧🌱

- SUBCATCH_RUNOFF: Runoff flow rate. ➡️ 🚰🌧️

- SUBCATCH_GW_FLOW: Groundwater flow rate to node. ➡️ ⛲

- SUBCATCH_GW_ELEV: Elevation of saturated groundwater table. ➡️ ⛰️⛲

- SUBCATCH_SOIL_MOIST: Soil moisture. ➡️ 🌱💦

- SUBCATCH_WASHOFF: Pollutant washoff concentration. ➡️ 🚿💧

📋 **Computed Node Quantities:** Defining computed results for nodes in the system.

- NODE_DEPTH: Water depth above invert. ➡️ 🌊

- NODE_HEAD: Hydraulic head. ➡️ 💧⬆️

- NODE_VOLUME: Volume stored & ponded. ➡️ 🚰📏

- NODE_LATFLOW: Lateral inflow rate. ➡️ ➡️🚰

- NODE_INFLOW: Total inflow rate. ➡️ 🚰➡️

- NODE_OVERFLOW: Overflow rate. ➡️ 🌊⬆️

- NODE_QUAL: Concentration of each pollutant. ➡️ 💧🔍

📋 **Computed Link Quantities:** Listing computed results for links in the system.

- LINK_FLOW: Flow rate. ➡️ 🚰➡️

- LINK_DEPTH: Flow depth. ➡️ 🌊📏

- LINK_VELOCITY: Flow velocity. ➡️ 💨🚰

- LINK_VOLUME: Link volume. ➡️ 🚰📏

- LINK_CAPACITY: Ratio of area to full area. ➡️ 🚰➗

- LINK_QUAL: Concentration of each pollutant. ➡️ 💧🔍

📋 **System-wide Quantities:** Defining overall computed results for the entire system.

- SYS_TEMPERATURE: Air temperature. ➡️ 🌡️

- SYS_RAINFALL: Rainfall intensity. ➡️ 🌧️

- SYS_SNOWDEPTH: Snow depth. ➡️ ❄️

- SYS_INFIL: Infiltration. ➡️ 💧🌱

- SYS_RUNOFF: Runoff flow. ➡️ 🚰🌧️

- SYS_DWFLOW: Dry weather inflow. ➡️ ☀️🚰

- SYS_GWFLOW: Groundwater inflow. ➡️ ⛲

- SYS_IIFLOW: RDII inflow. ➡️ 🌧️➡️

- SYS_EXFLOW: External inflow. ➡️ 🚰➡️

- SYS_INFLOW: Total lateral inflow. ➡️ 🚰➡️

- SYS_FLOODING: Flooding outflow. ➡️ 🌊⬆️

- SYS_OUTFLOW: Outfall outflow. ➡️ 🚰⬅️

- SYS_STORAGE: Storage volume. ➡️ 🚰📏

- SYS_EVAP: Evaporation. ➡️ ☁️

- SYS_PET: Potential ET. ➡️ 🌱☀️

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 7 - Constants for Link Flow, Buildup/Washoff, Time Series and Runoff**

🛤️ **Conduit Flow Classifications:** Defining various classes of flow within a conduit.

- DRY: Dry conduit. ➡️ 🚫💧

- UP_DRY: Upstream end is dry. ➡️ ⬆️🚫💧

- DN_DRY: Downstream end is dry. ➡️ ⬇️🚫💧

- SUBCRITICAL: Sub-critical flow. ➡️ 🌊🔽

- SUPCRITICAL: Super-critical flow. ➡️ 🌊🔼

- UP_CRITICAL: Free-fall at upstream end. ➡️ ⬆️🌊🔽

- DN_CRITICAL: Free-fall at downstream end. ➡️ ⬇️🌊🔽

- MAX_FLOW_CLASSES: Number of flow classes. ➡️ 📊🔢

- UP_FULL: Upstream end is full. ➡️ ⬆️💧

- DN_FULL: Downstream end is full. ➡️ ⬇️💧

- ALL_FULL: Completely full. ➡️ 💧🔄

🌧️ **Runoff Flow Categories:** Defining categories of runoff flows.

- RUNOFF_RAINFALL: Rainfall. ➡️ 🌧️

- RUNOFF_EVAP: Evaporation. ➡️ ☁️

- RUNOFF_INFIL: Infiltration. ➡️ 💧🌱

- RUNOFF_RUNOFF: Runoff. ➡️ 🚰🌧️

- RUNOFF_DRAINS: LID drain flow. ➡️ ⛲🔀

- RUNOFF_RUNON: Runon from outfalls. ➡️ 🚰⤴️

🌱 **Surface Pollutant Loading Categories:** Defining categories for pollutant loading on surfaces.

- BUILDUP_LOAD: Pollutant buildup load. ➡️ 🍂📈

- DEPOSITION_LOAD: Rainfall deposition load. ➡️ 🌧️💧📉

- SWEEPING_LOAD: Load removed by sweeping. ➡️ 🧹💨

- BMP_REMOVAL_LOAD: Load removed by BMPs. ➡️ 🌱🔄

- INFIL_LOAD: Runon load removed by infiltration. ➡️ 💧🌱⤵️

- RUNOFF_LOAD: Load removed by runoff. ➡️ 🚰🌧️⤵️

- FINAL_LOAD: Load remaining on surface. ➡️ 🍂🔄

📊 **Input Data Options:** Defining various types and sources of input data.

- RAINFALL_INTENSITY: Rainfall as intensity. ➡️ 🌧️🔍

- RAINFALL_VOLUME: Rainfall as volume. ➡️ 🌧️📏

- CUMULATIVE_RAINFALL: Cumulative rainfall volume. ➡️ 🌧️📈

- NO_TEMP: No temperature data. ➡️ 🚫🌡️

- TSERIES_TEMP: Temperatures from time series. ➡️ 🌡️📈

- FILE_TEMP: Temperatures from file. ➡️ 🌡️📂

- MONTHLY_WIND: Monthly varying wind speed. ➡️ 🌬️📅

- FILE_WIND: Wind speed from file. ➡️ 🌬️📂

- CONSTANT_EVAP: Constant evaporation rate. ➡️ ☁️🔄

- MONTHLY_EVAP: Monthly varying evaporation. ➡️ ☁️📅

- TIMESERIES_EVAP: Evaporation from time series. ➡️ ☁️📈

- TEMPERATURE_EVAP: Evaporation from daily temperature. ➡️ ☁️🌡️

- FILE_EVAP: Evaporation from file. ➡️ ☁️📂

- RECOVERY: Soil recovery pattern. ➡️ 🌱🔄

- DRYONLY: Evaporation in dry periods only. ➡️ ☀️🔄

- PER_AREA: Buildup per unit area. ➡️ 🍂📏

- PER_CURB: Buildup per curb length. ➡️ 🍂🚧

- NO_BUILDUP: No buildup. ➡️ 🚫🍂

- POWER_BUILDUP: Power function buildup equation. ➡️ 🍂🔍📈

- EXPON_BUILDUP: Exponential buildup equation. ➡️ 🍂🔍📉

- SATUR_BUILDUP: Saturation buildup equation.

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 8 - SWMM 5.2.4 Control Constants Overview 📚**

📚 **Constants Overview:**

🔄 **Rule States:**

- r_RULE: 🔀

- r_IF: ❓

- r_AND: ⛓️

- r_OR: 🔗

- r_THEN: ➡️

- r_ELSE: ⬅️

- r_PRIORITY: 🌟

- r_VARIABLE: 📊

- r_EXPRESSION: 💹

- r_ERROR: ❌

🔍 **Rule Objects:**

- r_GAGE: 📏

- r_NODE: 📍

- r_LINK: 🔗

- r_CONDUIT: 🚇

- r_PUMP: 🌪️

- r_ORIFICE: ⭕

- r_WEIR: 🚧

- r_OUTLET: 🛍️

- r_SIMULATION: 🔄

📝 **Rule Attributes:**

- r_DEPTH: ⬇️

- r_MAXDEPTH: 🔽

- r_HEAD: 🤕

- r_VOLUME: 🔊

- r_INFLOW: ➡️

- r_FLOW: 💧

- r_FULLFLOW: 🌊

- r_FULLDEPTH: 🌌

- r_STATUS: 📜

- r_SETTING: ⚙️

- r_LENGTH: 📏

- r_SLOPE: 📉

- r_VELOCITY: 🚀

- r_TIMEOPEN: 🕗

- r_TIMECLOSED: 🕛

- r_TIME: ⏲️

- r_DATE: 📅

- r_CLOCKTIME: 🕰️

- r_DAYOFYEAR: 🗓️

- r_DAY: 🌞

- r_MONTH: 📆

🔢 **Rule Relations:**

- EQ (Equals): ✅ (=)

- NE (Not Equals): ❎ (\<\>)

- LT (Less Than): ⬇️ (\<)

- LE (Less Than or Equal): ↙️ (\<=)

- GT (Greater Than): ⬆️ (\>)

- GE (Greater Than or Equal): ↗️ (\>=)

🎚️ **Rule Settings:**

- r_CURVE: 📈

- r_TIMESERIES: 🕰️

- r_PID: 🎛️

- r_NUMERIC: 🔢

🗂️ **Misc. Constants:**

- ObjectWords: Various objects 📋

- AttribWords: Various attributes 📜

- RelOpWords: Relation symbols 🔄

- StatusWords: OFF, ON ⏯️

- ConduitWords: CLOSED, OPEN 🚪

- SettingTypeWords: Setting types ⚙️

- IntensityWord: "INTENSITY" 💥

------------------------------------------------------------------------

------------------------------------------------------------------------

> ** Section 9 - Infiltration Constants**

 🔍🌐 **Enumerated Constants (InfilType):**

- 🌦️🌱 **HORTON:** Horton infiltration

- 🌧️☔ **MOD_HORTON:** Modified Horton infiltration

- 💧🌊 **GREEN_AMPT:** Green-Ampt infiltration

- 🌀🌪️ **MOD_GREEN_AMPT:** Modified Green-Ampt infiltration

- 📈📊 **CURVE_NUMBER:** SCS Curve Number infiltration

🌦️🌱 **Horton Infiltration (THorton):**

- f0: double ⏱️ Initial infiltration rate (ft/sec)

- fmin: double 📉 Minimum infiltration rate (ft/sec)

- Fmax: double 📈 Maximum total infiltration (ft)

- decay: double ⏳ Decay coefficient of infiltration rate (1/sec)

- regen: double 🔄 Regeneration coefficient of infiltration rate (1/sec)

- tp: double 🕐 Present time on infiltration curve (sec)

- Fe: double 🌱 Cumulative infiltration (ft)

💧🌊 **Green-Ampt Infiltration (TGrnAmpt):**

- S: double 🧽 Average capillary suction (ft)

- Ks: double 🚰 Saturated conductivity (ft/sec)

- IMDmax: double 🌵 Maximum soil moisture deficit (ft/ft)

- IMD: double 🌧️ Current initial soil moisture deficit

- F: double 🚿 Current cumulative infiltrated volume (ft)

- Fu: double 🌊 Current upper zone infiltrated volume (ft)

- Lu: double 📏 Depth of upper soil zone (ft)

- T: double ⏳ Time until start of next rain event (sec)

- Sat: char 💧 Saturation flag

📈📊 **Curve Number Infiltration (TCurveNum):**

- Smax: double 🗻 Maximum infiltration capacity (ft)

- regen: double 🔄 Infiltration capacity regeneration constant (1/sec)

- Tmax: double ⌛ Maximum inter-event time (sec)

- S: double 📊 Current infiltration capacity (ft)

- F: double 🚰 Current cumulative infiltration (ft)

- P: double ☔ Current cumulative precipitation (ft)

- T: double ⏲️ Current inter-event time (sec)

- Se: double 🌱 Current event infiltration capacity (ft)

- f: double 📉 Previous infiltration rate (ft/sec)

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 10 - 🌟 SWMM5 Calibration Files Overview 🌟**

Calibration files are pivotal in the modeling process, offering a comparison between real-world measurements and simulation outputs. 📈 Each file caters to a specific aspect of the water cycle or pollutant transport, allowing for targeted calibration and analysis. 🎯 Here's what each file typically contains:

- 🌧️ **Subcatchment Runoff**: Measurements of the volume of runoff generated by each subcatchment, crucial for validating surface water simulations.

- 💧 **Subcatchment Groundwater Flow**: Data on the flow of groundwater into or out of the subcatchment, aiding in calibrating subsurface hydrological models.

- 📏 **Subcatchment Groundwater Elevation**: Records of groundwater levels, which are essential to ensure the accuracy of groundwater table simulations.

- ❄️ **Subcatchment Snow Pack Depth**: Information on the depth of snow accumulation, providing insights into seasonal snowmelt and its impact on runoff.

- 🚮 **Subcatchment Pollutant Washoff**: Concentrations of pollutants washed off by stormwater, crucial for water quality modeling and pollution control strategies.

- 🌊 **Node Depth**: Data on the depth of water at network nodes, reflecting the performance of drainage systems during peak flow conditions.

- 🔄 **Node Lateral Inflow**: Measurements of lateral inflows to nodes, often used to fine-tune inflow distribution in complex network models.

- 🏊♀️ **Node Flooding**: Instances of overflow and flooding from nodes, providing real-world events to test the system's capacity and design thresholds.

- 🧪 **Node Water Quality**: Quality parameters at the nodes, ensuring that the simulation accurately reflects pollution levels throughout the network.

- 🚀 **Link Flow**: The rate of flow within conduits, fundamental for verifying the hydraulic performance of the modeled conduits.

- 💨 **Link Velocity**: The speed of flow in the conduits, used to assess energy gradients and sediment transport capabilities.

- 📏 **Link Depth**: The water depth in conduits, which is necessary for understanding the filling and capacity usage of the network under various conditions.

------------------------------------------------------------------------

------------------------------------------------------------------------

> **Section 10 - Input Section Types: LID Processes and Structures**

📋 **Input Section Types: LID Processes and Structures**

**Enumerations:**

- **LidTypes:**

  BIO_CELL: 🌱 Bio-retention cell.RAIN_GARDEN: 🌼 Rain [garden.GREEN](http://garden.GREEN)\_ROOF: 🏠🌿 Green roof.INFIL_TRENCH: ⛏️ Infiltration trench.POROUS_PAVEMENT: 🛣️ Porous pavement.RAIN_BARREL: 🛢️ Rain barrel.VEG_SWALE: 🌾 Vegetative swale.ROOF_DISCON: 🏠🚫 Roof disconnection.

- **TimePeriod:**

  PREVIOUS: ⏮️ Previous time period.CURRENT: ⏭️ Current time period.

**Data Structures:**

- **Surface Layer (TSurfaceLayer):** Parameters for the surface layer of an LID practice, such as bioretention cells, including thickness, void fraction, roughness, and slopes.

- **Pavement Layer (TPavementLayer):** Describes the characteristics of a porous pavement layer including thickness, void fraction, permeability, and clogging factors.

- **Soil Layer (TSoilLayer):** Details of a soil layer in an LID unit, including its thickness, porosity, field capacity, and hydraulic properties.

- **Storage Layer (TStorageLayer):** Defines a storage layer's parameters such as thickness, void fraction, hydraulic conductivity, and clogging aspects.

- **Drain Layer (TDrainLayer):** Parameters for underdrain systems in LID units, including coefficients, offsets, and flow equations.

- **Drain Mat Layer (TDrainMatLayer):** Characteristics of drainage mats typically used in green roofs, including thickness, void fraction, and roughness.

- **LID Process (TLidProc):** A comprehensive structure representing a generic LID design, encompassing various layers and drainage systems.

- **Water Balance Statistics (TWaterBalance):** Tracks water balance components like inflow, evaporation, infiltration, and surface runoff in an LID unit.

- **LID Report File (TLidRptFile):** Structure for storing detailed reporting information for LID processes.

- **LID Unit (TLidUnit):** Represents a specific LID process applied over an area, containing details about the unit's design, area, inflow, and performance statistics.

------------------------------------------------------------------------

------------------------------------------------------------------------

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time!
