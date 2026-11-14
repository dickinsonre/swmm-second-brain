---
title: "Ruby Scripts for Customizing your ICM SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/ruby-scripts-customizing-your-icm-swmm-networks-robert-dickinson
created: "2022-10-14 00:05"
published: "2022-10-23 10:13"
words: 1618
export_sha256: f880b12ff2e6f8eb41a4a6c89dd16207c2aa85dbdeaae7a41b95b253d82cfda5
---
# Ruby Scripts for Customizing your ICM SWMM Networks

![](https://media.licdn.com/mediaD4E12AQE3dG_G3ERk6g)

ICM InfoWorks by Autodesk Innovyze is a powerful and complete software platform for analyzing, designing, and managing water, sewage, and stormwater systems. It has a state-of-the-art 1D and 2D engine that lets users run complex simulations and analyses of different parts of water and wastewater systems. However, due to the many different components and features that make up the program, working with ICM InfoWorks can be quite complicated, especially for users who are new to the platform. One way to manage this complexity and streamline the process of working with ICM InfoWorks is to use SQL and Ruby to automate tasks that are either complex or repetitive in nature.

In this blog, we will talk about using SQL and Ruby to make the process of assigning watershed outlet nodes for ICM SWMM networks more automated. By using the power and flexibility of these programming languages, users can manage and organize their ICM SWMM networks more easily. This makes sure that all of the necessary data is entered into the system correctly and quickly. This can be especially useful for users who are working with large and complex networks, as it can help reduce the amount of time and effort required to set up and configure the system. Ultimately, the use of SQL and Ruby to automate tasks within ICM InfoWorks can help to make the process of working with the program more efficient and effective, allowing users to get the most out of the software. This has blog number Ruby 1729/1/1.

### What are we hoping to achieve by Combining Ruby with ICM SWMM Networks?

1.  We want to find the outlet ID for the closest node to a Subcatchment in an ICM SWMM Network.
2.  Ruby will use the Geometry tools of ICM to find the closest node.
3.  What is an ICM SWMM Network? It is a Network in ICM that uses SWMM 5.1.015 data and most/many of the tools of the ICM GUI. ICM of course also has InfoWorks Networks.
4.  What am I showing in the Post header image? Autodesk has Subscription versions of ICM (Standard and Ultimate), but I am showing the Thales versions of ICM which are both 32bit and 64bit, and comingled ICM InfoWorks and ICM SWMM Networks. I also use InfoWater Pro (Arc GIS Pro) and InfoSWMM which uses Arc Map and has a direct import into an ICM SWMM Network.

> ICM SWMM Network Data in the Autodesk Innvovyze ICM GUI

![ICM SWMM Network Subcatchment Data](https://media.licdn.com/dms/image/v2/D4E12AQFh8rls-a_fJA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1665789094177?e=1795651200&v=beta&t=-QhdjhdpTPUJ9_kjvO4HdejMNDoMbQq2it3fpUsuQsk)

### Why use Ruby for InfoWorks ICM SWMM Networks?

> Why Ruby - it is part of ICM and easy to understand with a lot of Modeling features. It is part of Network Menu Commands. You can use a new Script or a past used script so it is easy to find.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGqRzRN6wNq9w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1665789702427?e=1795651200&v=beta&t=72xlKRkl9DXgBrCvA0D4e39m1FnfJq91_HvMDMunjWA)

>   

### What is an InfoWorks ICM SWMM Network?

> ICM SWMM uses the SWMM 5.1.015 engine and has most of the UX features of ICM InfoWorks Networks including 2D. A different 1D network and solution of course.

### What is an example of Ruby Scripts?

```
net=WSApplication.current_network
puts 'Running ruby for SWMM Networks'
nodes=Array.new
net.row_object_collection('sw_node').each do |n|
        if n.selected?
                temp=Array.new
                temp << n.id
                temp << n.x
                temp << n.y
                nodes << temp
        end
end
net.transaction_begin
net.row_object_collection('sw_subcatchment').each do |s|
        if s.selected?
                sx = s.x
                sy = s.y
                nearest_distance = 999999999.9
                (0...nodes.size).each do |i|
                        nx = nodes[i][1]
                        ny = nodes[i][2]
                        n_id = nodes[i][0]
                        distance=((sx-nx)*(sx-nx))+((sy-ny)*(sy-ny))
                        if distance < nearest_distance
                                nearest_distance=distance
                                s.outlet_id = n_id
                        end
                end
        else
        puts 'You forgot to select anything'
        end
        s.write
end
puts 'Ending ruby'
net.transaction_commit
```

  

### Where can I find the Ruby Scripts?

Innovyze has a Github that you can use to copy or download dozens of Ruby and SQL scripts. If registered on our Portal, you can find Salesforce Knowledge Base articles and many other sources of help. at https://github.com/innovyze/Open-Source-Support. SQL and Ruby functionality exist to be used by users with knowledge of programming languages. We provide resources to assist customers in building their scripts through the existing self-help frameworks, including documentation on Ruby, help files, and more recently a wealth of GitHub examples - link above.

### How do I use Ruby Scripts?

> Easy - Go to the Network Menu and choose Run Ruby Scripts or Recent Ruby Scripts

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQG_nJaKYMKBbA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1665791563841?e=1795651200&v=beta&t=Q_TVlgn10jKvMD93mZ1XtfDG9C87s8QagTC-DEQtks0)

### Do I need to use SQL?

It helps if you have a simple global grid command and you do not want to edit the grid. Here is a simple SQL that sets the SWMM Network OUTLET_ID to blank. You can save the SQL on the project explorer window and then click to activate the dialog.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFpYActd1eg1Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1665868076221?e=1795651200&v=beta&t=fpKM_L8-ZxAPWqKvCdZtk1yNOc7m0JpI8j6T_9zKJeM)

### What does each line of the Ruby Script represent and what does it perform for the ICM SWMM Network?

The annotated snippet below shows the steps used in the script. ICM SWMM Networks are sw\_ whereas ICM InfoWorks Networks are hw\_ (for reference)

```
net=WSApplication.current_network

# Opens the current network on the ICM Geoplan

puts 'Running ruby for SWMM Networks'

# Tell the user some actions are being done by the script

nodes=Array.new

# Makes a new array - uses swmm nodes or sw_node

net.row_object_collection('sw_node').each do |n|
        if n.selected?
                temp=Array.new
                temp << n.id
                temp << n.x
                temp << n.y
                nodes << temp
        end
end
# Save the id, x coordinate, y coordinate to the nodes array of SELECTED Elements

net.transaction_begin

# start finding the nodes to set to the outlet of the subcatchment

net.row_object_collection('sw_subcatchment').each do |s|

# use swmm subcatchments or sw_subcatchment

        if s.selected?

# use the SELECTED Elements

                sx = s.x
                sy = s.y

# use the centroid of the subcatchment

                nearest_distance = 999999999.9
                (0...nodes.size).each do |i|
                        nx = nodes[i][1]
                        ny = nodes[i][2]
                        n_id = nodes[i][0]

# for each node find the x and y coordinates

                        distance=((sx-nx)*(sx-nx))+((sy-ny)*(sy-ny))

# compute the node to subcatchment distance
 
                       if distance < nearest_distance
                                nearest_distance=distance
                                s.outlet_id = n_id

# We have found the closed node and set the outlet ID to the node ID
                        end
                end
        else
        puts 'You forgot to select anything'

# message to remind ourself we forget to select any nodes or subcatchments

        end
        s.write
end
puts 'Ending ruby'
# Tell the user some actions were by the script

net.transaction_commit

# commit our new found ID to the current network (ICM SWMM Network)
```

I'm attaching a YouTube video that explains the previous stages. It is for ICM SWMM Networks, which utilizes SQL to remove or set the SWMM Subcatchment's OUTLET ID to Null and Ruby to determine the closest node to the Subcatchment's centroid and assign it as the OUTLET ID. I made a mistake and ran Ruby without using ICM to pick any items, which resulted in nothing being done, but at least I received a notice about not choosing any components.

  

### Summary of the Ruby Script

Ruby code that is intended to be run in the context of a stormwater management model in software such as SWMM5 or InfoWorks. The code is performing the following actions:

1.  Initializing variable nodes as an empty array.
2.  Iterating through all of the nodes in the current network and selecting those that are marked as selected.
3.  For each selected node, add its ID, X coordinate, and Y coordinate to the **nodes** array as an array of values.
4.  Starting a transaction in the current network.
5.  Iterating through all of the subcatchments in the current network and selecting those that are marked as selected.
6.  For each selected subcatchment, find the nearest node in the **nodes** array and set the outlet ID of the subcatchment to the ID of that node.
7.  Writing the updated subcatchment to the network and committing the transaction.

This code looks like it's meant to help update the outlet ID of certain subcatchments in the current network based on how close they are to specific nodes. It could be helpful in cases where you want to update the outlet ID of a group of subcatchments to reflect their actual location in the network rather than their original location in the model.

\[embedded item\]

### What do we end up with after using Ruby in ICM?

> We end up wih New (hopefully better) outlet nodes for our Subcatchments. The arrows show you both the centroid of the Subcatchment and the Outlet Node. The same or a similar script can be used for an ICM InfoWorks Network.

  

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGo2tTatF6cFg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1665706674938?e=1795651200&v=beta&t=XeF7fl-wN7SGLUQdy3yGWGp5zOHKFZFq4vinsO9e-IY)

**Global Note:** This is part of the 1729 Series of Hydrology and Hydraulics Modeling Blogs. 1729 has the factorization of 7 × 13 × 19 and the divisors of 1, 7, 13, 19, 91, 133, 247, 1729
