---
title: "Oh my time step, oh my time step (for SWMM Models)  Ruby for Link Lengths"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/oh-my-time-step-swmm-models-ruby-link-lengths-robert-dickinson-eqige
created: "2024-02-02 19:19"
published: "2024-02-03 01:33"
words: 537
export_sha256: fe28b621ee3a91aa7cded2a28c712e6436594abca2fb9f9c644dae0e54de7c8a
---
# Oh my time step, oh my time step (for SWMM Models)  Ruby for Link Lengths

![Options for short lengths in SWMM5](https://media.licdn.com/mediaD4E12AQHzFadx1wEfhw "Options for short lengths in SWMM5")

> **Introduction to CFL**

The CFL condition provides a criterion for stability in numerical simulations of wave propagation and other time-dependent problems. It links the time step size (ΔtΔt) to the spatial step size (ΔxΔx) and the speed (vv) at which information or disturbances propagate through the computational domain. In terms of SWMM5 the shortest pipe with the largest velocity governs the time step SWMM5 uses. If you have a very short pipe and a big model, the more numerous pipes use the same time step as the short pipe.

> How Does SWMM5 Test for the CFL time step to use during the Simulation?

It is done with the function getLinkStep. If you notice, it is based on the modified length and the original length of the link. If you do not use the conduit lengthening option, the mod and original lengths are the same. CourantFactor is user-defined and in the UX it is called **Adjust Variable Time Steps by %**

> **How do I know what Time Step SWMM5 is Using?**

It is listed in the **Routing Time Step Summary** in the report file. It shows you the frequency of time step used along with the minimum, mean, and maximum.

> How do I know the links that are controlling the time step?

It is listed in the Time-Step Critical Elements in the report file. It shows you the frequency of the link that controlled the CFL time step. Usually, one or two links control the time step. In this case, link 3860 was controlling the CFL time step 98 percent of the time.

> **What are my options to make my model go faster?**

Use the conduit-lengthening option. This is a time step, in seconds, used to artificially lengthen conduits so that they meet the Courant stability criterion under full-flow conditions (i.e., the travel time of a wave will not be smaller than the specified conduit lengthening time step). As this value decreases, fewer conduits will require lengthening. A value of 0 means that no conduits will be lengthened. The ratio of the artificial length to the original length for each conduit is listed in the flow classification table.

The Flow Classification Summary shows the adjusted length ratio, the new length, and the new roughness. The roughness is changed to make the new link hydraulically the same. If you use conduit lengthening, you increase the volume of the network, so it should not be overused. How do I define overuse?

> Ruby code to make a histogram of the link lengths. It will tell you how many short links are in your network.

> Readme File for Ruby/02 SWMM/0011 - Pipe Length Histogram

> The Generated Script

A list of the links in ten percent intervals along with the total number of links in the network.

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
