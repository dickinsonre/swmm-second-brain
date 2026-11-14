---
title: "Using ChatGPT to Understand what I programmed in 1988 for SWMM4"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-chatgpt-understand-what-i-programmed-1988-swmm4-dickinson-3a1ge
created: "2024-02-03 11:57"
published: "2024-02-03 12:26"
words: 315
export_sha256: 9327072b6408cceb0c3922c17d9d6d365641fbffacab6cbcd87cdff1c0503c5e
---
# Using ChatGPT to Understand what I programmed in 1988 for SWMM4

![A fictional image of the St Venant Equation by an AI program.](https://media.licdn.com/mediaD4E12AQE_BfR3lyMYCA "A fictional image of the St Venant Equation by an AI program.")

> Introduction

**Background for this:** I recently had to revisit the numerical solution for SWMM4 Runoff as it is part of our software programs XPSWMM and ICM InfoWorks SWMM Hydrology. Looking at the code without any comments made it a bit hard to understand. I used GPT4 to analyze the Fortran code. It found it to be a form of Richardson's equation and explained nicely how the subroutine works.

> What does the Fortran Code Look like?

It is subroutine overlnd.for written in 1988. The structure is simple, but there are no comments other than my name. I guess I thought that was important at the time. The whole purpose of the routine is to solve WCC\*DO\*\*1.6666667, or the Runoff equation for SWMM4.

> How does ChatGPT explain the SWMM4 Runoff code?

It is a Richardson extrapolation. While the code doesn’t correspond to a standard, widely-known numerical method like Runge-Kutta or Euler's method, it seems to be a customized implementation that combines elements of Richardson extrapolation for error control and an iterative approach for solving the SWMM4 nonlinear runoff equation.

> How is this solved in the SWMM5 C Code?

It is solved as a 5th-order RK. Interestingly enough, the code is from Numerical Recipes in C. I took Richardson's Extrapolation code from the book Numerical Recipes in Fortran or a different edition of the book

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
