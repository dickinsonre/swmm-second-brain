---
title: "German Hydrology in InfoSWMM, InfoSWMM SA and H2OMAP SWMM 14.5 with Full SWMM5 LID and SuDs Modeling"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/german-hydrology-infoswmm-145-h2omap-swmm-full-swmm5-lid-dickinson
created: "2017-01-27 00:37"
published: "2017-01-27 00:58"
words: 882
export_sha256: 42044eadb218abdcf328e582cc0666cfce71ea0f25bec85c08fa45705ffe6c05
---
# German Hydrology in InfoSWMM, InfoSWMM SA and H2OMAP SWMM 14.5 with Full SWMM5 LID and SuDs Modeling

This blog describes how the German Runoff hydrology converts precipitation excess (rainfall and/or snowmelt less infiltration, evaporation, and initial abstraction) into surface runoff (overland flow). InfoSWMM is a distributed model as it allows a study area to be subdivided into any number of irregularly shaped Subcatchment areas to best capture the effect that spatial variability in rainfall, topography, drainage pathways, land cover, and soil characteristics have on runoff generation. Generation of runoff is therefore computed on a Subcatchment by Subcatchment basis with the option of having the runoff go to a node or another Subcatchment. 

> All of the ancillary processes possible in InfoSWMM: LID’s, 5 types of infiltration (Horton, Modified Horton, Green Ampt, Modified Green Ampt and SCS CN), groundwater, evaporation, snowmelt, 2D processes and water quality are active and used in the German Hydrology Option.

The source of the equations used in the German Runoff hydrology method Is the program Storm.XXL (Storm XXL. was developed by InnoAqua )which can be seen at: [http://www.sieker.de/daten/download/sieker/public/manual_storm2006.pdf](http://www.sieker.de/daten/download/sieker/public/manual_storm2006.pdf). It uses the a mathematical model called the storage cascade. The storage cascade is a further development of the linear single storage. The linear storage cascade consists of several single storages that are switched to an in-line cascade. It is a linear storage equation and has two parameters (a Storage Constant in minutes) and a reservoir count that is integer and normally ranges from 1 to 5 ([Figure 1](http://blog.innovyze.com/wp-content/uploads/2016/09/GSS00.png)). The user sets the storage time for each reservoir and the number of reservoirs for each Subcatchment either in the DB Table for Subcatchments ([Figure 2](http://blog.innovyze.com/wp-content/uploads/2016/09/gss4.png)) or the Attribute Browser ([Figure 3](http://blog.innovyze.com/wp-content/uploads/2016/09/gss33.png)).

> New in InfoSWMM v14.5 is the ability of all 13 hydrology methods to interact with **SWMM 5 LID (Low Impact Development)** aka SuDS or WSUD Controls. The German hydrology option interacts with evaporation, groundwater and all LID controls as well. In previous versions of InfoSWMM only the EPA Non Linear Runoff allowed LID controls.

The numerical equations for each storage and the total runoff from the cascading storages are shown in [Figures 4](http://blog.innovyze.com/wp-content/uploads/2016/09/GSS0.png) and [5](http://blog.innovyze.com/wp-content/uploads/2016/09/GSS1.png), respectively. The Run Manager with German Runoff is shown in [Figure 6](http://blog.innovyze.com/wp-content/uploads/2016/09/gss66.png). The effect of varying the reservoir count and storage constant are shown in [Figures 7](http://blog.innovyze.com/wp-content/uploads/2016/09/GSS77.png) and [8](http://blog.innovyze.com/wp-content/uploads/2016/09/GH2.png).

![](https://media.licdn.com/dms/image/v2/C5112AQENqFMta4DvUg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520250053803?e=1795651200&v=beta&t=Ji49sVlOHExyzHSv7RKL3hLpb9zrYZ-BaMwN6GezH80)

Figure 1. Linear Storage Cascade with two parameters per Subcatchment: (1) Storage Constant in minutes (Lagerung Constant) and (2) the number of linear reservoirs or the Reservoir Graf.

![](https://media.licdn.com/dms/image/v2/C4E12AQHZuh47Zr8BJA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520572856016?e=1795651200&v=beta&t=xGkVoWqQPO2xhjhbzNufwkqFWHybD6L8yrvPHPe0kxE)

Figure 2. The German Runoff 2 parameters can be entered in the Subcatchment DB Table of InfoSWMM

![](https://media.licdn.com/dms/image/v2/C4E12AQGBg3aws7KjKA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520572854916?e=1795651200&v=beta&t=_jBNy9zQxLK1SILHsMJeNq6xuCeHaV-5-8kuF7eqay4)

Figure 3. The German Runoff 2 parameters can be entered in the Attribute Browser of InfoSWMM.

![](https://media.licdn.com/dms/image/v2/C4E12AQG_5yba_jxluA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520572854803?e=1795651200&v=beta&t=JgMZIwiUHQz0-r8oQwKCz8vbX9NPmMKR3agC4H3utx8)

Figure 4. The differential equation for each storage for flow, time and rainfall excess.

![](https://media.licdn.com/dms/image/v2/C5112AQH2Ia09tEJO4Q/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520250814836?e=1795651200&v=beta&t=63cIUFBR6uaoQhm1lRj4t59djiwaMYH7UtnpETMe22U)

Figure 5. The equation used to compute the runoff based on the storage constant and the number of reservoirs. Paulsen (1987) gives this equation as a solution for the differential equation system for dt \<= K. The effect of the model parameters n and K are similar. A large value for the storage constant K enlarges the retention period and curbs the runoff hydrology. A large number for n also has a dampening effect.

![](https://media.licdn.com/dms/image/v2/C4E12AQEusCdqc9bkEg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520572855047?e=1795651200&v=beta&t=ohQf_XwQLvkCSRdNlHGQDoYtGSnuUOQv6jAZJzeJyn4)

Figure 6. InfoSWMM Run Manager with 12 Options for Hydrology including German Runoff.

![](https://media.licdn.com/dms/image/v2/C4E12AQH1vG9ZqKZMGw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520572854953?e=1795651200&v=beta&t=BYJzWAU5FKTea7y4i_LSb7TjTtwPuYnkhkIMOOHXjzY)

Figure 7. German Runoff with a SCS Hyetograph and a Storage Constant of 3 minutes. GH31 is a reservoir count of 1. GH32 is a reservoir count of 2 etc.

![](https://media.licdn.com/dms/image/v2/C5112AQG1692aYQjqUg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1520141286916?e=1795651200&v=beta&t=w5MBY1WB2batGnJYkDGI3kfO3HSOfzSuIpjtkdUwJQk)

Figure 8. German Runoff with a Balanced Hyetograph and two Scenarios: (1) Runoff with a Storage Constant of 3 minutes and 1 reservoir and (2) 3 minutes and 2 reservoirs.
