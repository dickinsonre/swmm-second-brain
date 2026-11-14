---
title: "SWMM3 Orifice Extran3 Test File for AI, GitHub, SWMM5, ICM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/swmm3-test-files-ai-github-swmm5-icm-robert-dickinson-gqkoe
created: "2024-12-28 03:44"
published: "2024-12-28 12:20"
words: 1026
export_sha256: dfb90ab90587886aa6849131def02a75368c93b821333fe03bb424ac224c10b2
---
# SWMM3 Orifice Extran3 Test File for AI, GitHub, SWMM5, ICM

![SWMM3 Orifice Extran3 Test File for AI, GitHub, SWMM5, ICM](https://media.licdn.com/mediaD4E12AQEvXf0iL0Mknw "SWMM3 Orifice Extran3 Test File for AI, GitHub, SWMM5, ICM")

**The SWMM3 Orifice Test File: A Historical Reference for Modern Hydraulic Modeling**

This test file holds special historical significance in the development of stormwater modeling. Originally published in the 1981 EXTRAN 3 manual by CDM (now CDM Smith), it was specifically designed to validate orifice calculations in hydraulic networks. The file served as a critical quality assurance tool during the evolution of SWMM, supporting the transition from SWMM3 through SWMM4 and into the current SWMM5.

I documented this file's importance in a 2009 Posthaven blog post, which I have updated using various AI tools to maintain its relevance. Today, this historical test case continues to prove valuable across multiple modern modeling platforms, such as ICM SWMM—as an example. It is also on the EPA GitHub as a test model.

To make this valuable reference more accessible to the hydraulic modeling community, I've prepared several modern implementations:

1\. A newly formatted PID RT version compatible with SWMM5

2\. A GitHub repository containing the file and its documentation

3\. Imported versions for both InfoWorks ICM and ICM SWMM Network platforms

As part of this article, you can download the original test file to explore this piece of stormwater modeling history yourself or use it for your own quality assurance testing.

> **Example Real-Time Control (RTC) rule for an Orifice in SWMM5**

**Explanation of Components:**

1.  RULE Orifice1:

2.  IF SIMULATION CLOCKTIME \>= 01:00:00:

3.  AND SIMULATION CLOCKTIME \<= 2:00:00:

4.  THEN ORIFICE OR1@82309b-15009b SETTING = 1:

5.  ELSE ORIFICE OR1@82309b-15009b SETTING = 0:

6.  PRIORITY 1:

7.  ; Opens up the orifice at hour 1 of the simulation:

**Functionality:**

This rule effectively opens the orifice "OR1@82309b-15009b" fully at 1:00:00 AM (one hour into the simulation) and keeps it open until 2:00:00 AM. After 2:00:00 AM, the orifice is fully closed.

**Variations, Improvements, and Considerations:**

1.  Partial Opening:

2.  Time-Based Gradual Opening/Closing:

3.  Sensor-Based Control:

4.  Multiple Conditions:

5.  Multiple Orifices:

6.  Rule Interaction

7.  Saving RTC Rules:

- RTC rules are typically written in a separate text file (e.g., "rules.txt") and then referenced in the SWMM5 input file (.inp) under the \[RULES\] section. You would add a line like: \[RULES\] FILE "rules.txt" Or you can paste the rules directly into the \[RULES\] section of the .inp file.

**Example of a More Advanced Rule (Conceptual)**

Let's say you want to implement a rule that mimics a PID (Proportional-Integral-Derivative) controller to maintain a target water level in a storage unit by adjusting an orifice:

**Explanation of the Advanced Rule**

- Constants: Kp, Ki, and Kd are tuning parameters that determine the controller's response. TargetDepth is the desired water level.

- Variables: ErrorSum keeps track of the accumulated error over time (integral term), and PrevError stores the error from the previous time step (for the derivative term).

- Initialization: At the start of the simulation (IF SIMULATION START), initialize ErrorSum and PrevError to 0.

- Error Calculation: The error is the difference between the TargetDepth and the CurrentDepth at the storage unit.

- Integral Term: The ErrorSum is updated by adding the current Error.

- Derivative Term: The DeltaError is calculated as the difference between the current Error and the PrevError.

- PID-like Control: The Adjustment is calculated using a formula similar to a PID controller, but without proper time-based integration and differentiation.

- Adjustment Limiting: The Adjustment is limited to prevent drastic changes in the orifice setting.

- Setting Application: The calculated NewSetting is applied to the orifice after being constrained to the valid range \[0, 1\].

- Storing Previous Error: The current Error is stored in PrevError for use in the next time step.

**Important Notes About the Advanced Rule**

- This is a *simplified* example and not a true PID implementation because SWMM5's basic RTC rules don't directly support time-based calculations required for accurate integral and derivative terms.

- Proper PID control would typically involve dividing the integral term by the time step and multiplying the derivative term by the time step.

- Tuning the Kp, Ki, and Kd constants is crucial for stable and effective control.

- This type of rule might require smaller simulation time steps for better performance.

- You can set the value of a variable using the THEN portion of a rule.

> In Conclusion

SWMM5's RTC rules provide a powerful way to simulate the dynamic control of hydraulic structures like orifices. You can create rules that range from simple time-based operations to more complex sensor-based and feedback control systems. Remember to carefully consider rule interactions, priorities, and potential improvements to create robust and realistic simulations. While basic RTC rules have limitations, especially for advanced control strategies, understanding the fundamentals will help you leverage their capabilities effectively in your SWMM5 models.

![](https://media.licdn.com/dms/image/v2/D4E12AQHL5_ct0BdsJw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1735357625513?e=1795651200&v=beta&t=E4SxSl1uAL4Rj_xYegn3ximUUHHQsuN8Hxf6rZAVqTg)

SWMM5 Output Graph

> **The PID RTC SWMM5 version of the original SWMM3 Model**

> ** How does this look in ICM InfoWorks and ICM SWMM?**

![](https://media.licdn.com/dms/image/v2/D4E12AQGYY9LPe74cNA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1735387567778?e=1795651200&v=beta&t=uBhlYRIjQI6onB7_eSgoLnSYSF1jifm16XSDOt-pZyY)

InfoSWMM Engine == OneSWMM for InfoDrainage and ICM SWMM

> Full Reference for the 1981 version of Extran for SWMM3

![](https://media.licdn.com/dms/image/v2/D4E12AQHSk1oP6xLViA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1736595057786?e=1795651200&v=beta&t=EKuqbagEvkdUwmhzCBwntnLLQ8V3vGmJT1a_huP7o28)

Full Reference for the 1981 version of Extran for SWMM3

> Closing Note

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time you read one of these posts.**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
