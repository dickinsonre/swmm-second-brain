---
title: "A Story about the C-Code Hydrology of SWMM5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/story-c-code-hydrology-swmm5-robert-dickinson-2x0we
created: "2024-02-10 12:32"
published: "2024-02-10 13:59"
words: 3521
export_sha256: f39de3f541d0ec878239df7f27754bf733d46759c0b77aa318df28350d8e8a7a
---
# A Story about the C-Code Hydrology of SWMM5

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![A Story about the C-Code Hydrology of SWMM5](https://media.licdn.com/mediaD4E12AQEp77nh9d9R0g "A Story about the C-Code Hydrology of SWMM5")

Note: The format of this newsletter edition is changed from the previous. Here are seven sections on the hydrology of SWMM5 instead of seven embedded LinkedIn posts or articles.

There are eight sections in the 12th edition of the newsletter.

**Runoff, Alternate Runoff, Runoff Detailed View, the Runoff numerical solution, Curve Number Infiltration, Horton Infiltration, Green Ampt Infiltration, and Groundwater.**

> **1/ The Main Story - Runoff**

Imagine a vibrant, bustling city where every neighborhood (subcatchment) tells its unique story through the rhythm of nature’s elements. In this grand narrative, our code is like a meticulous chronicler, documenting the myriad interactions of water and earth across the city's tapestry. Let's unfold this tale through the lens of the enumerated SubcatchResultType:

1.  **The Arrival of Rain (**SUBCATCH_RAINFALL**)**: As dawn breaks, clouds gather, heralding the arrival of rain. The SUBCATCH_RAINFALL holds the tale of these pristine droplets as they grace the city with their presence, marking the beginning of a captivating hydrological narrative.

2.  **The Blanket of Snow (**SUBCATCH_SNOWDEPTH**)**: In the quiet embrace of winter, a soft blanket of snow envelops the city. The SUBCATCH_SNOWDEPTH captures the essence of this serene, white mantle, its depth narrating the chill’s gentle tale.

3.  **The Whisper of Evaporation (**SUBCATCH_EVAP**)**: As the sun ascends, a subtle dance of evaporation begins. The SUBCATCH_EVAP tells the story of water's tender ascent, its soft whispers leaving a trace of moisture in the air.

4.  **The Embrace of Infiltration (**SUBCATCH_INFIL**)**: The earth tenderly embraces the rain, drawing it into its depths. The SUBCATCH_INFIL chronicles this gentle embrace, as the soil quenches its thirst.

5.  **The Journey of Runoff (**SUBCATCH_RUNOFF**)**: Not all water is drawn into the earth; some embarks on a riveting journey across the city’s surface. The SUBCATCH_RUNOFF narrates the adventures of this daring runoff as it explores the urban landscape.

6.  **The Hidden Flow (**SUBCATCH_GW_FLOW**)**: Beneath the city, a hidden river of groundwater flows silently. The SUBCATCH_GW_FLOW delves into the mysteries of this subterranean flow, revealing its quiet journey to the nodes.

7.  **The Rising Table (**SUBCATCH_GW_ELEV**)**: The SUBCATCH_GW_ELEV tells of the groundwater table's quiet rise and fall, its elevation a silent testimony to the earth’s pulsing heart.

8.  **The Soil’s Tender Moisture (**SUBCATCH_SOIL_MOIST**)**: Nestled within the earth’s bosom, the soil cradles its precious moisture. The SUBCATCH_SOIL_MOIST unfolds the tale of this nurturing moisture, vital for the land’s fecundity.

9.  **The Dance of Washoff (**SUBCATCH_WASHOFF**)**: As rain dances across the city, it sweeps along a ballet of substances. The SUBCATCH_WASHOFF chronicles this dance, capturing the concentration of pollutants whisked away in the washoff.

> 2/ Alternate Main Story

### Chapter I: The Arrival of Rain (SUBCATCH_RAINFALL)

As the first light of dawn caresses the skyline, the heavens gather a symphony of clouds, heralding the arrival of rain. The city, a stage set for the day's performance, waits in anticipation. The SUBCATCH_RAINFALL captures the descent of pristine droplets, each a messenger of the skies, initiating the grand hydrological narrative that saturates the urban canvas with life-giving moisture.

### Chapter II: The Blanket of Snow (SUBCATCH_SNOWDEPTH)

In the serene silence of winter, the city finds itself wrapped in a delicate blanket of snow. The SUBCATCH_SNOWDEPTH chronicles the depth of this white mantle, a testament to the chill's gentle embrace. This chapter narrates a tale of tranquility and rest, as the snow insulates the city, transforming it into a tableau of serene beauty.

### Chapter III: The Whisper of Evaporation (SUBCATCH_EVAP)

With the sun's ascent, an invisible ballet begins—a dance of evaporation that whispers across the city. The SUBCATCH_EVAP tells the story of water's tender journey upwards, its vaporous trails a soft caress against the city's skin, leaving behind a fleeting moisture in the air, a hidden dialogue between sun and earth.

### Chapter IV: The Embrace of Infiltration (SUBCATCH_INFIL)

Beneath the surface, the earth opens its arms, welcoming the rain into its depths. The SUBCATCH_INFIL documents this gentle communion, a testament to the soil's eternal thirst and its nurturing embrace. Here, in the quiet beneath the city's hustle, the narrative of rejuvenation unfolds, a symbiotic tale of life's sustenance.

### Chapter V: The Journey of Runoff (SUBCATCH_RUNOFF)

Not all raindrops are destined for the soil's embrace. Some embark on a daring odyssey across the urban expanse. The SUBCATCH_RUNOFF narrates the saga of these adventurous waters as they traverse the landscape, exploring the contours of the city, a dynamic journey of discovery and interaction.

### Chapter VI: The Hidden Flow (SUBCATCH_GW_FLOW)

Beneath the city's vibrant pulse lies a secret river, the groundwater flow. The SUBCATCH_GW_FLOW delves into the enigmatic world of this hidden current, its silent passage a testament to the unseen forces that shape the urban beneath. This chapter explores the depths, revealing the quiet strength that supports the city from below.

### Chapter VII: The Rising Table (SUBCATCH_GW_ELEV)

The tale of the groundwater table, chronicled in the SUBCATCH_GW_ELEV, speaks of the subtle rise and fall, a rhythm akin to the earth’s breathing. This narrative captures the silent fluctuations, a gentle pulse beneath the city’s feet, marking the ebb and flow of nature’s unseen dance.

### Chapter VIII: The Soil’s Tender Moisture (SUBCATCH_SOIL_MOIST)

In the embrace of the earth lies the precious moisture, cradled within the soil. The SUBCATCH_SOIL_MOIST unfolds the story of this life-giving essence, the foundation of fertility and growth. Here, the narrative weaves a tale of nurturing and care, the soil's gift to the city above.

### Chapter IX: The Dance of Washoff (SUBCATCH_WASHOFF)

As the rain weaves its path through the city, it gathers a ballet of substances, a washoff that carries with it the stories of urban life. The SUBCATCH_WASHOFF chronicles this dance, capturing the movement and the concentrations of pollutants whisked away in the water's flow, a testament to the city’s dynamic interaction with the rain.

> **3/ A More Detailed Look at Subarea Runoff**

a meticulous ensemble of methods—SUB-AREA METHODS—plays a pivotal role. These guardians are tasked with a noble purpose: to compute and manage the runoff and losses from each subarea, ensuring the city's resilience against the whims of weather.

### Chapter I: The Prelude to Runoff (getSubareaRunoff)

As the city awakens, a symphony of rainfall and snowmelt descends upon it, setting the stage for the guardians' work. The getSubareaRunoff method, a sage among algorithms, takes center stage. It assesses the area of each subcatchment, the intensity of precipitation, and the caress of evaporation against the skin of the earth. With each timestep, it calculates the runoff rate, a narrative of water's journey from the heavens to the urban expanse.

### Chapter II: The Embrace of the Earth (getSubareaInfil)

Beneath the city's bustling life, the earth awaits, ready to embrace the falling rain. The getSubareaInfil method, a whisperer of secrets, speaks to the soil's thirst. It calculates the infiltration rate, determining how much of the storm's gift will seep into the depths, nourishing the land and replenishing the hidden aquifers.

### Chapter III: The Saga of Surface Flow (findSubareaRunoff)

Not all rain is destined to join the earth in its silent embrace. Some must journey across the surface, a quest for the sea. The findSubareaRunoff method charts this odyssey, measuring the depth of water that dances above the ground, defying infiltration to become runoff. It's a tale of movement and momentum, where every droplet's path weaves through the city's veins.

### Chapter IV: The Depths of Reflection (updatePondedDepth)

In the heart of the storm, as water gathers and pools, the updatePondedDepth method reflects on the depths that form. It calculates the new ponded depth over the subarea, pondering the balance between inflow and storage, between the rain's bounty and the earth's capacity to hold it. This narrative speaks to the transient beauty of puddles and ponds, ephemeral mirrors to the skies.

### Chapter V: The Dance of Variables (adjustSubareaParams)

As seasons change and the city breathes, the adjustSubareaParams method adjusts the rhythm of the dance. It fine-tunes the depression storage and runoff coefficient, ensuring that the guardians' calculations resonate with the time of year, the weather's mood, and the land's whisper.

> **4/ The Numerical Solution for Runoff**

the odesolve_integrate method stands as a sentinel at the gates of time. Its purpose: to navigate the turbulent waters of differential equations, steering the ship of inquiry from the shores of initial conditions to the horizon of solutions.

### Chapter I: The Voyage Begins (odesolve_integrate)

Our saga commences with a tapestry of initial values, each a thread in the grand design of the cosmos. The odesolve_integrate method, a sage of computation, embarks on its quest, armed with the precision of Runge-Kutta integration and the wisdom of adaptive stepsize control. It seeks to unravel the mysteries of dynamics, propelling the variables from the dawn of x1 to the twilight of x2, through the fabric of time and space.

### Chapter II: The Dance of the Cosmos (rkqs)

As the journey unfolds, the rkqs method, a disciple of the sage, performs a delicate ballet. With each step, it evaluates the terrain, adjusting its stride with the grace of a celestial dancer. It navigates the path of integration, monitoring the local truncation error, a harbinger of accuracy and adjuster of stepsize. This dance, intricate and precise, balances the scales of error and estimation, ensuring the fidelity of the voyage through the mathematical ether.

### Chapter III: The Alchemy of Runge-Kutta-Cash-Karp (rkck)

In the heart of the quest, amidst the swirling mists of calculation, the rkck method emerges, a master of alchemy. It conjures the essence of the Runge-Kutta-Cash-Karp method, a formula of great power and subtlety. Through its incantations, y\[\] is advanced, transformed by the magic of differential equations. This alchemy, woven from the threads of coefficients and derivatives, shapes the journey, guiding the variables towards their destiny. As the saga draws to a close, the odesolve_integrate and its companions, rkqs and rkck, converge at the nexus of understanding

![](https://media.licdn.com/dms/image/v2/D4E12AQHoMMk2Bfi3YA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1707573010089?e=1795651200&v=beta&t=gDGVAGrENQbIuFgCtmhcFr9aH5_1_ymZ9DUDyc4kLfs)

The Actual C Code for SWMM5

> **5/ Curve Number Infiltration**

Amidst the complexity of urban subcatchments, where the terrain is a patchwork of permeable earth and impermeable surfaces, the Curve Number infiltration method stands as a sentinel. It is here, in this nuanced landscape, that the curvenum_getInfil function begins its work, tasked with a mission of utmost importance: to calculate the rate at which rainfall permeates the soil, replenishing the earth and mitigating the surge of stormwater runoff.

### Act I: The Gathering Storm

As clouds gather and rain begins to fall, the stage is set for the function's opening act. The rainfall rate (irate), a key protagonist in our story, makes its entrance, accompanied by the depth of runon and ponded water (depth). These elements converge at the threshold of the Curve Number model, where the initial conditions of infiltration capacity (infil-\>S) and the elapsed time since the last rainfall event (infil-\>T) await their cue.

### Act II: The Awakening

The first droplets of rain signal the awakening of the Curve Number model from its slumber. Should the inter-event time exceed a predetermined threshold (infil-\>Tmax), a new chapter begins, resetting the cumulative precipitation (infil-\>P), infiltration (infil-\>F), and the effective saturation (infil-\>Se). This reset symbolizes the soil's readiness to embrace the incoming rainfall, its pores open and eager for the nourishment the heavens provide.

### Act III: The Dance of Infiltration

With the stage thus set, the dance of infiltration begins. The function calculates the potential new cumulative infiltration (F1), a delicate interplay between the current rainfall and the soil's existing moisture deficit. This dance, governed by the immutable laws of hydrology, determines the infiltration rate (f1), a measure of how swiftly the rain is absorbed by the soil.

Should the rain abate, leaving only the memory of its touch in the form of ponded water, the function adapts. It revisits the previous infiltration rate (infil-\>f), ensuring that the soil continues to drink from the pooled reserves, even as it yearns for the rain's return.

### Act IV: The Cycle of Renewal

In the absence of rainfall, the narrative shifts towards regeneration. The soil's capacity to infiltrate (infil-\>S), diminished by its recent embrace of the rain, begins to recover, nourished by the passage of time and the absence of further precipitation. This cycle of depletion and renewal, a core motif of the Curve Number method, underscores the dynamic relationship between rain and land.

> **6/ Horton Infiltration and Modified Horton**

The Horton Infiltration model plays a crucial role, guiding the rain's journey from the urban canopy to the earth's embrace. Let's explore the choreography behind the horton_getInfil and modHorton_getInfil functions, revealing the beauty and precision of their operations.

### Act I: Setting the Stage (horton_getInfil)

As the curtain rises, we find ourselves observing the Horton Infiltration model in action. The stage is set with variables: the tstep marking time, irate as the intensity of our rainfall, and depth representing the ponded water, awaiting its descent into the soil.

The model begins its dance with a calculation of available water (fa), a blend of rainfall, melted snow, and any existing ponded water. This moment captures the anticipation of infiltration, the soil's readiness to absorb the rain's offering.

### Act II: The Dance of Infiltration

With the stage set, the model delves into its core performance. It calculates the potential infiltration rate (fp), guided by the Horton equation's balance between maximum (f0) and minimum (fmin) infiltration rates, adjusted by the infiltration factor (InfilFactor), and influenced by the soil's current saturation (Fmax) and the passage of time (tp).

As the dance unfolds, two scenarios emerge:

- **For a thirsty soil**, the model calculates the average infiltration rate over the timestep, adjusting for the soil's capacity to absorb water. This is a delicate balance, ensuring that the rate does not exceed what the rain and ponded water can offer (fa).

- **For a soil quenched or drying**, the model explores the regenerative capacity of the soil (kr), allowing the soil to recover and prepare for the next downpour.

### Act III: Encore Performance (modHorton_getInfil)

In a variation on the theme, the modHorton_getInfil function presents a modified Horton Infiltration model. This encore performance incorporates a nuanced approach to handling saturated conditions and the soil's drying phase.

Here, the calculation of available water (fa) sets the stage for a performance that considers the soil's saturation. If the soil is already saturated, the dance pauses, acknowledging the limit of absorption. Yet, in the presence of water, the soil's capacity to infiltrate is re-evaluated, reflecting a dynamic interaction between soil and water.

### Epilogue: The Cycle Continues

As the performance concludes, the models leave behind a landscape transformed by the rain's passage. Through the horton_getInfil and modHorton_getInfil functions, the Horton Infiltration model orchestrates the complex interplay between rainfall and soil, ensuring that every drop of water is accounted for, either nourishing the earth or joining the urban water cycle as runoff.

> **7/ Green Ampt Infiltration**

Within the intricate dance of the urban water cycle, the Green-Ampt infiltration model plays a pivotal role, delicately managing the interplay between rainfall and the earth's absorbent embrace. The grnampt_getInfil function, a cornerstone of this model, orchestrates a complex ballet of hydrological processes, ensuring that water's journey from sky to soil is both efficient and harmonious. Let's delve deeper into the narrative woven by this function and its supporting cast.

### Act I: Prelude to Infiltration

Our story begins with the grnampt_getInfil function setting the stage for infiltration's intricate dance. Armed with the timestep (tstep), the net rainfall rate (irate), and the depth of ponded water (depth), this function prepares to navigate the delicate balance between water's desire to penetrate the earth and the soil's capacity to accept it. The stage is further set by determining the model type, distinguishing between the standard and modified Green-Ampt approaches.

### Act II: The Unveiling of Potential

At the heart of our tale lies the decision fork where the path of infiltration diverges based on the soil's saturation state. If the soil thirsts for moisture, unsaturated infiltration takes center stage, with the grnampt_getUnsatInfil function calculating how much of the waiting water can seep into the ground. Conversely, if the soil is already quenched, the narrative shifts to grnampt_getSatInfil, exploring the dynamics of saturated infiltration.

### Act III: The Dance of the Unsaturated

In the realm of the unsaturated, the function meticulously calculates the available infiltration rate, considering both the rainfall and any existing ponded water. It contemplates the soil's current state, weighing the potential for moisture recovery against the backdrop of ongoing rainfall. This delicate balance is maintained through a dance of calculations that ensure the soil's readiness to welcome new rainfall, all the while considering the upper soil zone's saturation and the intricate dynamics of moisture recovery.

### Act IV: The Symphony of Saturation

As we venture into saturated territories, the narrative deepens, exploring the soil's limits and its intricate relationship with water. The grnampt_getSatInfil performance unfolds, a calculated ballet where every drop of water is accounted for, ensuring that infiltration rates are meticulously aligned with the soil's capacity and the prevailing hydrological conditions. This act celebrates the harmony between water and earth, a testament to the model's precision and the depth of understanding it encapsulates.

### Epilogue: The Cycle Continues

As our story concludes, the grnampt_getInfil function, along with its unsaturated and saturated counterparts, leaves behind a legacy of balance and efficiency. Through their meticulous calculations and nuanced understanding of soil-water interactions, they ensure that the urban water cycle proceeds with grace and precision. This narrative, woven from code and calculation, highlights the elegance of hydrological models in managing one of our most precious resources: water.

In this tale of infiltration, the Green-Ampt model stands not just as a method but as a storyteller, weaving together the many strands of hydrology into a coherent and harmonious narrative.

> **8/ GroundWater**

Groundwater's journey in SWMM5 is meticulously orchestrated by the gwater_getVolume and gwater_getGroundwater functions, pivotal components of the Groundwater model in SWMM. These functions, akin to conductors in an elaborate symphony, ensure the harmonious flow of groundwater through the urban subsurface. Let's explore the narrative woven by these functions, casting a light on their roles in managing groundwater's delicate balance.

### Act I: The Quest for Volume (gwater_getVolume)

Our tale begins with a quest to uncover the hidden volume of groundwater nestled within the urban terrain's upper and lower zones. The gwater_getVolume function steps forward, embarking on this journey with precision and purpose. It delves into the depths of the subcatchment, guided by indices and parameters, to unveil the total volume of groundwater stored, marrying the metrics of depth and porosity in a dance of calculation.

### Act II: The Groundwater Ballet (gwater_getGroundwater)

As the narrative unfolds, the stage is set for the gwater_getGroundwater function to perform its ballet of hydrological processes. This act delves into the heart of groundwater flow, navigating through evaporation, infiltration, and the time-stepped dynamics that govern the subsurface's response to rainfall and urban runoff.

Within this ballet, variables and equations intertwine, each step and turn calculated to reflect the groundwater's response to the urban environment. The function crafts a delicate balance, ensuring that every drop of water either contributes to the nourishment of the earth or is accounted for in the urban water cycle.

### Act III: The Symphony of Fluxes

At the core of our tale lies the intricate symphony of water fluxes, a complex interaction of evaporation, percolation, and groundwater flow. The getFluxes function, with its ensemble of calculations, choreographs the movement of water through the soil's layers, from the upper zone's thirst for moisture to the lower zone's capacity to channel water back to the urban fabric.

This symphony, conducted beneath the city's surface, showcases the intricate balance between water retention and release, ensuring that groundwater's journey is both sustainable and harmonious with the urban ecosystem.

### Epilogue: The Harmony Restored

As the curtain falls on our narrative, the gwater_getVolume and gwater_getGroundwater functions,

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
