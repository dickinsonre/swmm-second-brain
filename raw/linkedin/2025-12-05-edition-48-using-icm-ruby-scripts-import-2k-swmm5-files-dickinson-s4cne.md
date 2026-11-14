---
title: "Edition 48 - Using ICM Ruby Scripts to Import 2K SWMM5 Files to ICM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-48-using-icm-ruby-scripts-import-2k-swmm5-files-dickinson-s4cne
created: "2025-12-05 21:53"
published: "2025-12-05 21:56"
words: 702
export_sha256: 28ba3a0b37c44923c3e4cc9d4fb89994dd9562689464818583b8636d9db53e04
---
# Edition 48 - Using ICM Ruby Scripts to Import 2K SWMM5 Files to ICM

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![Using ICM Ruby Scripts to Import 2K SWMM5 Files to ICM ](https://media.licdn.com/mediaD4E12AQHI5HChHgr5lA "Using ICM Ruby Scripts to Import 2K SWMM5 Files to ICM ")

This 48th Edition of the newsletter is about the awesomeness of Ruby scripting in ICM InfoWorks. I now have thousands of SWMM5 models in ICM (something I wanted to do for years - but you know importing them one by one is not that much fun). Why do I want this? I want to be able to compare ICM InfoWorks to SWMM5 for a whole range of models and not the simple models we used to test SWMM4 and SWMM5.

How was this accomplished? At AWI or Autodesk Water we had a Ruby Hackathon a few months ago lead by our talented Water PM Nathan Gerdts, PE and we created a lot of useful Ruby code - you can see our GitHub for some of this code. In the Hackathon our stellar engineer for SSF Kate Maschmann, PE made a giant contribution to the software import capability. She use ICM Exchange to import **ALL** of the scenarios from InfoSWMM to an ICM SWMM Network which is much better than the one scenario at a time menu import in ICM. I was amazed at what she accomplished and used her code and applied it to SWMM5 and not InfoSWMM. As you know SWMM5 does not have scenarios so I changed the Ruby importer to find all inp files in a directory and import them to ICM SWMM. It works very fast and in a few minutes I had all of my GitHub SWMM5 models imported. The beauty of her code is not only is the network created but the model run and ancillary data.

The banner image shows what this looks like after it is imported and the five steps you take in Ruby to do the import. AWI is all for open source so you can get this code from out GitHub and see the readme files in markdown for the two Ruby Scripts. I will be using these 2K files for a lot of extended testing such as the [Bill James Similarity Index](https://www.linkedin.com/posts/robertdickinson_bill-james-similarity-index-to-compare-swmm5-activity-7303115167335088129-8L3f?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEAvcwBVte4NjFU9EyFPNigxyghgnrHf9c) which I have mentioned on LinkedIn,

The ruby code is in two files, one for the [UI](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0022%20-%20Hackathon%20AWI%20OffShoots/SWMM5_Import_ICM_SWMM_with_Cleanup_UI.rb) and one for [Exchange](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0022%20-%20Hackathon%20AWI%20OffShoots/SWMM5_Import_ICM_SWMM_with_Cleanup_Exchange.rb) (you need ICM Ultimate to run Exchange). You can see in Figure 1 a diagram of the UI code and in Figure 2 a diagram of the EX Code. The readme markdown files can be see on the Innovyze or Autodesk Water Infrastructure (AWI) GitHub for the [UI](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0022%20-%20Hackathon%20AWI%20OffShoots/SWMM5_Import_ICM_SWMM_with_Cleanup_UI.md) Ruby and [EX](https://github.com/innovyze/Open-Source-Support/blob/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0022%20-%20Hackathon%20AWI%20OffShoots/SWMM5_Import_ICM_SWMM_with_Cleanup_Exchange.md) Ruby Code. A note on how the diagrams were made, I used DeepSeek to read the Ruby Code and create a Nano Banana Pro prompt and of course Nano for the diagram. The Markdown files were made with Claude Opus 4.5Figure 1 - Nano Banana Diagram of UI Ruby Code

![](https://media.licdn.com/dms/image/v2/D4E12AQGACOPQfNsLsg/article-inline_image-shrink_1500_2232/B4EZrwgUlcHUAY-/0/1764971596503?e=1795651200&v=beta&t=TNFm3UyagIfTi-K7xJjLxaCNYwhPX1CqBkzb6SNWLMg)

Figure 1 - Nano Banana Diagram of UI Ruby Code

![](https://media.licdn.com/dms/image/v2/D4E12AQGoptNO50YtAg/article-inline_image-shrink_1500_2232/B4EZrwgUlaKcAc-/0/1764971596507?e=1795651200&v=beta&t=jd8m1QfoKr4zVXw7j734C2GEX1HA6QrAEsM2yiEPNm8)

Figure 2 - Nano Banana Diagram of the Exchange Ruby Code
