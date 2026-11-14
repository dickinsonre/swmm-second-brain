---
title: "Using Ruby to Create Sensitivity Scenarios in ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-create-sensitivity-scenarios-icm-infoworks-dickinson-eprde
created: "2024-03-23 21:58"
published: "2024-06-03 12:01"
words: 579
export_sha256: 0ec018ff216c244bdaadf65ba8656cc028d7b962e04cbb3977e9fed54d29c5ce
---
# Using Ruby to Create Sensitivity Scenarios in ICM InfoWorks

![Using Ruby to Create Sensitivity Scenarios in ICM InfoWorks for Horton Infiltration](https://media.licdn.com/mediaD4E12AQFltkHzelbD7A "Using Ruby to Create Sensitivity Scenarios in ICM InfoWorks for Horton Infiltration")

This Ruby script focuses on managing scenarios in an InfoWorks network using the WSApplication API. Here's a summary of the main ideas:

1\. The script starts by defining a set of factors and parameters to create scenarios based on them. **It establishes four scenarios with parameter changes of -25, -10, +10 and +25 percent. You can alter these factors and the number of factors in the Ruby code.**

2\. It generates scenario names by combining each parameter with each factor, resulting in a list of scenarios. **This makes it easier to see the factors' effect after running the model.**

3\. The script deletes all existing scenarios in the network, except for the base scenario, to ensure a clean slate. **An important note - this is intended for text networks and not your actual network.**

4\. It then iterates over each generated scenario and its corresponding factor:

adds a new scenario to the network with the generated name.

begins a transaction to modify the network data within the current scenario.

\- Retrieves all the conduit objects in the network using .

\- Updates the attribute of each conduit by multiplying it with .

collects the updated values and keeps track of the total roughness and the number of links modified.

commits the transaction to save the changes.

5\. Finally, the script displays the total number of scenarios added to the network.

The script also includes user-friendly messages:

\- It informs the user about the successful deletion of old scenarios and the addition of new ones.

\- It provides instructions on how to revert the changes if performed in error.

\- It displays the factor value for each scenario during the iteration.

\- It summarizes the total bottom roughness and the number of links modified for each scenario.

Overall, this script automates creating and managing scenarios in an InfoWorks network based on predefined factors and parameters, making it easier to perform sensitivity analysis or test different network configurations.

![](https://media.licdn.com/dms/image/v2/D4E12AQHZvDLDyysKNQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195777450?e=1795651200&v=beta&t=pNb41OiK7FArvEcs85ePc94po-dGGkZIvpWEbkERq7g)

The test network is one of the SWMM5 Test models converted to ICM InfoWorks.

![](https://media.licdn.com/dms/image/v2/D4E12AQFp46jORyuhdw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721191416347?e=1795651200&v=beta&t=c4W7IXyUmbSAQ4lXITDtSH8fMsfjoBjRX0eQwt4s0-E)

The Ruby Output Script shows the factors and the changed values.

![](https://media.licdn.com/dms/image/v2/D4E12AQFASWGxLzNaTg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721194621516?e=1795651200&v=beta&t=IYrkC6Hf1TkKWj2xJl6-b85W5GoaRIGSNkD-j8jyxQE)

Use the Simulation Results Graphs so you can see all of the scenario output.

![](https://media.licdn.com/dms/image/v2/D4E12AQH1sddld-Bflg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195446702?e=1795651200&v=beta&t=lvRbMmQPvLQg-y23JZrU5QySZbqQFAHhDJS--0N2jfg)

In this network, the peak flow is less sensitive to changes in the bottom roughness than is the depth.

> **Ruby Script** [**Readme.MD**](http://Readme.MD) **0150 - Scenario Sensitivity - InfoWorks Link Mannings N**

> **The Ruby Script**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQFzsnSlnWgSog/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721195813964?e=1795651200&v=beta&t=db89sFeYvBJ9ER3r6oURyqC41PTe0dE4ZWdsrw354dw)

Gren Infrasturucture AI Hand
