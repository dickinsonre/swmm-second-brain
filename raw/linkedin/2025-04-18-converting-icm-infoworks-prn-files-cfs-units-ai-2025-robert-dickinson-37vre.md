---
title: "Converting ICM InfoWorks PRN Files to CFS Units with AI in 2025"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/converting-icm-infoworks-prn-files-cfs-units-ai-2025-robert-dickinson-37vre
created: "2025-04-18 12:09"
published: "2025-04-18 14:58"
words: 550
export_sha256: bd123c5ad8fc45c2b6a27f2aabdcf0a310c3c1e815903e9db3c3e162cdfd0c6f
---
# Converting ICM InfoWorks PRN Files to CFS Units with AI in 2025

![Converting ICM InfoWorks PRN Files to CFS Units with AI in 2025 ](https://media.licdn.com/mediaD4E12AQGK_pftKFz18g "Converting ICM InfoWorks PRN Files to CFS Units with AI in 2025

")

This article was inspired by a question on our User Feedback Page about unit conversions in ICM InfoWorks, a topic that resonates with me as I frequently compare InfoWorks ICM and SWMM5 models. A common frustration, shared by myself and others for over 15 years, is that InfoWorks ICM’s PRN file—akin to SWMM5’s RPT file—outputs results exclusively in SI units (e.g., meters, cubic meters per second). In contrast, SWMM5’s RPT file offers more flexibility, including options for U.S. customary units like cubic feet per second (cfs). This article explores this limitation and offers insights for users working with InfoWorks ICM outputs. I won't go into the details for SWMM5, as anyone who wants to use AI to convert units would be used to the SWMM5 RPT file.

The PRN file in InfoWorks ICM is a text-based summary of simulation results, detailing node and link data such as water levels, flows, and volumes. While comprehensive, its fixed SI unit output can be inconvenient for users in regions like the U.S., where cfs and feet are standard. SWMM5’s RPT file, by comparison, allows users to select units (e.g., cfs or liters per second) during simulation setup, making it more adaptable for diverse workflows.

To address this in InfoWorks ICM, users can:

- Post-Process Outputs: Export PRN file data to tools like Excel or Python and apply conversion factors (e.g., 1 m³/s = 35.3147 cfs, 1 m = 3.28084 ft). Scripts can automate this process for large datasets.

- Use InfoWorks ICM Tools: Leverage built-in reporting features or Ruby scripts (e.g., the export_hw_conduit_data_to_csv.rb script from our series) to customize outputs, though unit conversion may still require manual steps.

- Advocate for Enhancements: Share feedback with the InfoWorks ICM development team to request unit flexibility in future PRN file outputs, similar to SWMM5.

- **OR, use an AI prompt to convert all of the numbers in the attached file from SI to CFS based units and make a new, changed file.**

Any 2025 AI program will do. The results are correct and informative. Figure 1 shows the PRN file, and Figure 2 shows the converted PRN file from SI units to CFS. Easy, the AI does the coding and basically you just copy and paste from the ICM UX to an external text file.

![](https://media.licdn.com/dms/image/v2/D4E12AQG-t4ECadATxA/article-inline_image-shrink_1500_2232/B4EZZI7.K8HcAU-/0/1744980403664?e=1795651200&v=beta&t=ky0Vusjw0GnQ1mxlQRBe9g63UuqiFDAM0EC7DgkGWeA)

Figure 1: ICM InfoWorks Networks have an output file called PRN in which the units are always SI

![](https://media.licdn.com/dms/image/v2/D4E12AQHb1D5dCCvuhw/article-inline_image-shrink_1500_2232/B4EZZI7vm5HcAU-/0/1744980344012?e=1795651200&v=beta&t=U9D9THHgWmo-wP5sd5JkI_-_tTNaMDEfZBAE-dTt4QQ)

Figure 2: AI transformed PRN file from the native SI units to CFS.

> Closing Th**ought**

This is related to simulations versus reality. The brain can't distinguish between vivid imagination and reality. "Research in neuroscience shows that imagination and perception activate many of the same neural pathways. When we vividly imagine something, our brains can produce similar physiological responses to actually experiencing it."
