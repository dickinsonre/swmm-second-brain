---
title: "Enhancing your ICM SWMM Network Simulation: Leveraging Ruby Scripts for Optimal Time Step Selection"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/enhancing-your-icm-swmm-network-simulation-leveraging-dickinson
created: "2023-05-18 15:17"
published: "2023-05-18 20:21"
words: 1103
export_sha256: 601fd8902dbca4dc291ae829669df9173630cd2910fc8d1aaac600a7c4f238ff
---
# Enhancing your ICM SWMM Network Simulation: Leveraging Ruby Scripts for Optimal Time Step Selection

![](https://media.licdn.com/mediaD4E12AQHEfDVuNinoHw)

> Enhancing your ICM SWMM Network Simulation: Leveraging Ruby Scripts for Optimal Time Step Selection

In SWMM, the conduit lengthening time step parameter is primarily used to ensure numerical stability in the model. It controls how much a conduit (or pipe) can be artificially lengthened to meet the Courant condition for stability.

The Courant condition essentially states that the computational time step should be less than the time it takes for water to traverse the smallest computational element. In the context of SWMM, this is typically the smallest conduit.

The routing time step in SWMM is the time step used to compute flow routing in the system. The routing time step needs to be small enough to accurately capture the dynamics of the flow, especially in systems with rapid changes, but large enough to keep computational time reasonable.

The relationship between the conduit lengthening time step and the routing time step is critical. The conduit lengthening time step should ideally be equal to or smaller than the routing time step. If it's larger, the model might become unstable and produce inaccurate results.

To balance accuracy and computation time, one could start with a longer routing time step and adjust downward until the desired level of detail is captured. Correspondingly, conduit lengths can be adjusted to meet the stability conditions for the chosen routing time step.

However, it's important to note that this is a simplified explanation, and other factors may also need to be considered based on the specifics of the network and the goals of the simulation.

In summary, the conduit lengthening time step and routing time step in SWMM need to be carefully chosen and balanced. Too large a time step can lead to unstable and inaccurate results, while too small a time step can lead to unnecessarily long computation times. Understanding and properly setting these parameters can greatly enhance the efficiency and accuracy of your SWMM simulations.

> ICM SWMM network Run Dialog with the conduit lengthening option

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEdnO4HxU10tA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1684438851160?e=1795651200&v=beta&t=-OiJh786FTuzeYQZuMJAuuZKkvhQ-K9aYNqJnDuOt0U)

ICM SWMM network Run Dialog with the conduit lengthening option set to 1 second

> Why is the Conduit lengthening option important in SWMM5 modeling?

The Courant-Friedrichs-Lewy (CFL) condition plays a crucial role in defining the time step for explicit numerical methods, which SWMM also employs. The CFL condition states that numerical diffusion or dispersion will be minimized when the computational time step is less than the time for wave propagation across the computational element.

In SWMM, the CFL condition is satisfied when the computational time step (Δt) is less than the conduit length (L) divided by the wave celerity (c), which is the sum of the flow velocity (v) and the wave speed (a). The square root of the product of gravitational acceleration (g) and hydraulic depth (h) here determines wave speed. Thus, the condition can be written as:

Δt \< L / (v + a)

Δt \< L / (v + √(g \* h))

This explicit time step formulation ensures the stability of the solution, as it constrains the time step so that water does not move across more than one computational element (in this case, a conduit) within a single time step. If the actual routing time step exceeds this CFL time step, the simulation may suffer from numerical instability, causing inaccurate results.

Therefore, the routing time step, the conduit lengthening time step, and the CFL time step are all interconnected. The conduit lengthening and routing time steps should be set to ensure they do not exceed the CFL time step, keeping in mind the balance between computational efficiency and the level of detail or accuracy required for your specific model.

Remember, adjusting these parameters appropriately is fundamental to generating reliable and meaningful simulation results with SWMM.

> How is the time step (hydraulic time step) defined in ICM SWMM? In timestep control with 10 seconds

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHbLiLmqDpcXQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1684439388209?e=1795651200&v=beta&t=Kx9XWdaz2gCZ2o349zGh-1ZlDdYeLTSrwL-eyt4g0S8)

Timestep Control for ICM SWMM, report, and hydraulic timesteps

> What is the time step used during the simulation?

Look at the Routing Time Step Summary. The conduit lengthening value helps determine the minimum time step.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQF989HhCOsZRQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1684439556639?e=1795651200&v=beta&t=dWaMXAXpBHMoVMtKBwZrlRKfyJT4dVn0pV8D1eda-Us)

Routing Time Step Summary in the RPT file of SWMM5

The smaller the link length in your model, the more likely it is that a small time step during the simulation will be used. The Ruby code shown below shows the min, max, mean, and lowest ten percent of the link lengths.

> The Ruby code for finding the mean and lowest ten percent of the pipe lengths.

```
# Find the smallest 10 percent of pipe
net = WSApplication.current_network
net.clear_selection

link_lengths = []
ro = net.row_objects('hw_conduit').each do |ro|
  link_lengths << ro.conduit_length if ro.conduit_length
end

# Calculate the threshold length for the lowest ten percent
threshold_length = link_lengths.min + (link_lengths.max - link_lengths.min) * 0.1

# Calculate the median length (50th percentile)
sorted_lengths = link_lengths.sort
median_length = sorted_lengths[sorted_lengths.length / 2]

# Select the links whose length is below the threshold or median length
selected_links = []
ro = net.row_objects('hw_conduit').each do |ro|
  if ro.conduit_length && (ro.conduit_length < threshold_length || ro.conduit_length < median_length)
    ro.selected = true
    selected_links << ro
  end
end

total_links = link_lengths.length

if selected_links.any?
  printf("%-440s %-0.2f\n", "Minimum link length", link_lengths.min)
  printf("%-440s %-0.2f\n", "Maximum link length", link_lengths.max)
  printf("%-44s %-0.2f\n", "Threshold length for lowest 10%", threshold_length)
  printf("%-44s %-0.2f\n", "Median link length (50th percentile)", median_length)
  printf("%-44s %-d\n", "Number of links below threshold", selected_links.length)
  printf("%-44s %-d\n", "Total number of links", total_links)  
else
  puts "No links were selected."
endsaa
```

**Innvoyze**, the software development company, has recently updated its official Github repository to include a new segment of code that is written in Ruby and SQL for ICM SWMM Networks in addition to ICM InfoWorks Networks. The link is shown below.

\[embedded item\]

> More about the time step used in SWMM5 at this link

\[embedded item\]

  

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEEEatyvDcuRg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1684435139194?e=1795651200&v=beta&t=oxNgRYsngXpmgpwgAVAMwQ-J2FCHM9K83RLCTfKAHLg)

A GIF showing the Ruby code in action for both SWMM and InfoWorks networks.

The End?
