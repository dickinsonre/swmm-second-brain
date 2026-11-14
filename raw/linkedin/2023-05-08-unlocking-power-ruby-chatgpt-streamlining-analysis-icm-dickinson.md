---
title: "Unlocking the Power of Ruby with ChatGPT: Streamlining Subcatchment Analysis in InfoWorks ICM Network"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/unlocking-power-ruby-chatgpt-streamlining-analysis-icm-dickinson
created: "2023-05-08 15:17"
published: "2023-05-08 16:11"
words: 1395
export_sha256: 500e97df5f315aa7a3d037ebd7503c3c5957d1f2b750b2add472537bc47e99ab
---
# Unlocking the Power of Ruby with ChatGPT: Streamlining Subcatchment Analysis in InfoWorks ICM Network

![Using Ruby Scripts to find the Upstream Area for all Subcatchments Draining to any Node](https://media.licdn.com/mediaD5612AQEJVxUpEEhBZg "Using Ruby Scripts to find the Upstream Area for all Subcatchments Draining to any Node")

> **1/** This code snippet performs the following tasks in the context of an InfoWorks ICM network (Note: The script is in subfolder 70 on my [Github](https://github.com/ICM-SWMM-Tools-and-Examples/ICM-SWMM-Ruby/tree/main/0070%20-%20Upstream%20Subcatchments%20from%20an%20Outfall) repository):

1.  Accesses the current network and assigns it to the variable **net**.
2.  Retrieves all subcatchments from the network and assigns them to the variable **all_subs**.
3.  Creates an empty hash (dictionary) called **node_sub_hash_map**.
4.  Retrieves all nodes from the network and assigns them to the variable **all_nodes**.
5.  Iterates through all the nodes and assigns their node IDs as keys in the **node_sub_hash_map** with empty lists as their corresponding values.
6.  Retrieves all subcatchments from the network again and assigns them to the variable **all_subs**.

The main purpose of this code is to create a hash map connecting node IDs to their associated subcatchments.

```
net = WSApplication.current_network

# Get all subcatchments from the network and assign them to the variable all_subs
all_subs=net.row_objects('_subcatchments')

# Create an empty hash variable named node_sub_hash_map
node_sub_hash_map={}

# Get all nodes from the network and assign them to the variable all_nodes
all_nodes=net.row_objects('_nodes')

# Assign node ID's as hash keys in the node_sub_hash_map
all_nodes.each do |h|
    node_sub_hash_map[h.node_id]=[]
end

# Get all subcatchments again and assign them to the variable all_subs
all_subs=net.row_objects('_subcatchments')
```

> **2/** This code snippet performs the following tasks in the context of an InfoWorks ICM network:

1.  Retrieves all the selected rows in the **\_nodes** collection and assigns them to the variable **roc**.
2.  Creates a new empty array called **unprocessedLinks**.

The main purpose of this code is to access the selected nodes in the network and initialize an empty array that will be used to store unprocessed links, likely for further processing in the script.

```
# Get all the selected rows in the _nodes collection and assign them to the variable ro
roc = net.row_object_collection_selection('_nodes')

# Create an empty array named unprocessedLinks
unprocessedLinks = Array.new
```

> **3/** This code snippet iterates through a collection of selected nodes in the InfoWorks ICM network and performs the following tasks:

1.  For each node, it iterates through all its upstream links.
2.  If a link hasn't been processed yet, it's added to the **unprocessedLinks** array and marked as seen.
3.  While there are still unprocessed links, the code processes each link, selects it, and retrieves its upstream node.
4.  If the upstream node hasn't been processed, it is selected and its upstream subcatchments are identified using a previously created hash map (**node_sub_hash_map**).
5.  The IDs of the subcatchments connected to the upstream node are printed.
6.  The code then iterates through all the upstream links of the current upstream node, and if they haven't been processed, they are added to the **unprocessedLinks** array and marked as seen.

The main purpose of this code is to identify and process all upstream subcatchments connected to the selected nodes in the network.

```
roc.each do |ro
    # Iterate through all the upstream links of the current row object
    ro.us_links.each do |l|
        # if the link has not been seen before, add it to the unprocessedLinks array
        if !l._seen
            unprocessedLinks << l
            l._seen=true
        end
    end
    # While there are still unprocessed links in the array
    while unprocessedLinks.size>0
        # take the first link in the array and assign it to the variable working
        working = unprocessedLinks.shift
        working.selected=true
        # get the upstream node of the current link
        workingUSNode = working.us_node
        # if the upstream node is not nil and has not been seen before
        if !workingUSNode.nil? && !workingUSNode._seen
            workingUSNode.selected=true
            # Now that hash is ready with node id's as key and upstream subcatchments as paired values, keys can be used to get an array containing upstream subcathments
            # In the below code id's of subcatchments upstream of node 'node_1' are printed. The below code can be reused multiple times for different nodes within the script without being computationally expensive
            node_sub_hash_map[workingUSNode.id].each  do |sub|
                puts "Found Upstream Subcatchment #{sub.id} connected to Node #{workingUSNode.id}"
                sub.selected=true
            end
            # Iterate through all the upstream links of the current node and add them to the unprocessedLinks array
            workingUSNode.us_links.each do |l|
                if !l._seen
                    unprocessedLinks << l
                    l.selected=true
                    l._seen=true
                end
            end
        end
    end
end|
```

> **4/** You do need to select at least one node to find the upstream Subcatchments.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D5612AQFJClHJ1STyuA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683560484244?e=1795651200&v=beta&t=1KNP9C9keaLydks0TSyqgTUVR3Nh_hyKmFZ4KA7ZgbQ)

The Ruby Script finds the upstream Subcatchments and makes a table of the found Subcatchemnts

> **5/** Now let us use ChatGPT to find the total area and total number of found Subcatchments

ChatGPT Prompt - I have already used the Ruby code in ChatGPT to summarize the code (see above)

```
add a final table that tells me the total number of found Subcatchments and the total area
```

The response from ChatGPT Note the area variable is not correct so I need to change it to "total_area += sub.total_area" for ICM

The output now looks like with the total number of Subcatchemntns and total area.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D5612AQHZUWMhzGwxxg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1683561769080?e=1795651200&v=beta&t=foczffo4GaGiiTVBOgvctWk53sOz5UPx-X8gdUII7Ic)

The output now shows the total number of Subcatchemntns and the total area.

Code for printing the "The output now looks like with the total number of Subs and total area.

```
# Initialize a counter variable for th"  e total number of subcatchments and a variable for the total ar
total_subcatchments = 0
total_area = 0.0

roc.each do |ro|
    # The existing code goes here
    # ...
end

# Add the found upstream subcatchment's area to the total area
node_sub_hash_map.each_value do |subcatchments|
  subcatchments.each do |sub|
    total_area += sub.area
    total_subcatchments += 1
  end
end

# Print the total number of subcatchments and the total area
puts "Total number of found Subcatchments: #{total_subcatchments}"
puts "Total area of found Subcatchments: #{total_area}"e
```

> My reasoning about this elephant story list of blogs.

Bottom-up technical blogs can be highly beneficial for engineering, particularly when it comes to explaining deep dive features. These blogs often present detailed insights, experiences, and practical examples from engineers and industry professionals, making them an excellent resource for understanding complex engineering concepts. Some of the reasons why bottom-up technical blogs are good for engineering when explaining deep dive features include:

1.  Real-world experience: Engineers who contribute to bottom-up blogs often share their hands-on experience with specific technologies, tools, or techniques. This practical knowledge allows readers to better understand deep dive features and their real-world applications, which may not be covered as thoroughly in textbooks or academic articles.
2.  Accessibility: Bottom-up blogs tend to use more conversational language and break down complex concepts into simpler terms, making deep dive features more accessible to a broader audience. This can be particularly useful for engineers who are new to a specific topic or looking to expand their knowledge in a particular area.
3.  Community-driven knowledge sharing: By sharing their insights and experiences in bottom-up blogs, engineers contribute to a collective knowledge base. This promotes collaboration, encourages continuous learning, and helps engineers stay up-to-date with the latest developments and best practices.
4.  Problem-solving and troubleshooting: Bottom-up technical blogs often present real-world examples of engineers' challenges and the solutions they've developed. This can help readers learn from others' experiences, avoid common pitfalls, and adopt effective strategies for tackling complex engineering problems.
5.  Personalized learning: Since bottom-up blogs often focus on specific topics or deep dive features, engineers can selectively choose the most relevant content to their needs and interests, allowing for a more personalized learning experience.
6.  Networking opportunities: Bottom-up technical blogs can foster connections among engineers with similar interests and areas of expertise. Engaging in discussions in the comments section or connecting with authors and other readers can help engineers build professional networks and enhance their career prospects.
