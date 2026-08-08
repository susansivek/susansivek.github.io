---
title: "Notable Nodes: Identifying Influencers with Network Analysis"
date: 2021-04-20
excerpt: "\"My dog loves napping in his super-fuzzy dog bed. And I have to confess: I like to think I’m a rational consumer, but I bought him the bed because of cute photos and a discount code shared by a social media influencer."
original_url: "https://towardsdatascience.com/notable-nodes-identifying-influencers-with-network-analysis-2f51f1d8fec4"
publication: "Towards Data Science"
categories: [data-science]
---
*Originally published at [https://towardsdatascience.com/notable-nodes-identifying-influencers-with-network-analysis-2f51f1d8fec4](https://towardsdatascience.com/notable-nodes-identifying-influencers-with-network-analysis-2f51f1d8fec4)*

![](https://miro.medium.com/fit/c/56/56/2*hZfc88aZ_kt98p5b_2REOw.jpeg)

[*Johannes Groll*](https://unsplash.com/@followhansi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/network?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

My dog loves napping in his super-fuzzy dog bed. And I have to confess: I like to think I’m a rational consumer, but I bought him the bed because of cute photos and a discount code shared by a social media influencer.

Identifying social media influencers who can help promote your business is both an art and a science. There are plenty of commercial services that say they can tell you who those people are. But why pay for that service when you can use a tool already at your fingertips to find and analyze potential influencers and their posts? Alteryx has network analysis capabilities that can help you identify these people and determine whether they’re a good fit for your needs.

Let’s take a closer look at the [Network Analysis Tool](https://help.alteryx.com/current/designer/network-analysis-tool) and build our own workflow to identify potential Twitter influencers.

*Image via* [*GIPHY*](https://media.giphy.com/media/gf5Q6uzTN0RkEAQaxA/giphy-downsized.gif)

# Retrieving and Preparing Tweets

A while back, I [demonstrated](https://community.alteryx.com/t5/Data-Science/How-Your-City-Feels-According-to-Social-Media/ba-p/649518?utm_content=748634&utm_source=tds) how to retrieve and analyze tweets using the Twitter API, the user-created [Twitter API Authorization Header macro](https://gallery.alteryx.com/#!app/Twitter-API-Authorization-Header/5bb29ea4826fd30c4cd5533e), and the Sentiment Analysis Tool from the [Alteryx Intelligence Suite](https://www.alteryx.com/products/alteryx-platform/intelligence-suite?utm_content=community).

You can use the approach and workflow provided in that post to get started on our influencer identifier. You might choose a keyword, a location, or — as I will do here — a hashtag relevant to your interests as your starting point.

I’m going to look at tweets with the hashtag #ODSCEast from the recent [Open Data Science Conference East](https://odsc.com/boston/). One use for these tweets could be identifying influencers who might be helpful in promoting our [Data Science Mixer podcast](https://community.alteryx.com/t5/Data-Science-Mixer/bg-p/mixer?utm_content=748634&utm_source=tds) and/or could be future guests.

I retrieved tweets using that hashtag twice a day for all three days of the conference, resulting in a collection of 600 tweets. Unfortunately, Twitter’s [standard search](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview) [limits](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits) access to tweets, but this sample is a good starting point.

*Image via* [*GIPHY*](https://media.giphy.com/media/3o7TKBdA6WLOR8anxm/giphy-downsized.gif)

The number of followers someone has is just one possible measure of influence on Twitter. Another way to think about influence might be to examine who is often connected with other people in actual tweets — who often is linked with others due to common interests and broad recognition. In the case of this conference, people might be mentioned together in tweets related to upcoming sessions or talks, revealing connections that wouldn’t be evident otherwise. Users who co-occurred often with other users in the collected tweets could be key connections, helpful for reaching a wide audience. This is the approach we’ll try here.

After parsing the Twitter data, I wanted just the usernames of everyone mentioned in the tweets, so I used the [RegEx Tool](https://help.alteryx.com/current/designer/regex-tool) and the expression *@(\w+)* to tokenize the usernames into rows. With help and ideas from [Neil Ryan](https://community.alteryx.com/t5/user/viewprofilepage/user-id/1443?utm_content=748634&utm_source=tds) and [Ben Moss](https://community.alteryx.com/t5/user/viewprofilepage/user-id/5143?utm_content=748634&utm_source=tds), everything eventually got into the form I wanted prior to network analysis: a two-field, 155-row table with the pairs of usernames that had actually appeared together in tweets, and a one-field, 115-row table with just the unique usernames of everyone who had shown up in any tweet. The first rows of each table are below.

Images by author

# Constructing the Network

As usual, the process of generating those two tables took a lot longer than actually analyzing the data! I used the [Network Analysis Tool](https://help.alteryx.com/current/designer/network-analysis-tool) to see how the Twitter users I identified were all interconnected in the tweets I’d gathered.

Let’s start with the resulting diagram of the network and work backwards to explore how it was formed. There’s a static image below, but you can also check out the [interactive dashboard](https://s3-us-west-1.amazonaws.com/ayx.community.assets/odsc_network.html), which is available in Designer from the I output of the Network Analysis Tool. (You can also export it to various formats, such as HTML, with the Render Tool.)

Try the [interactive version](https://s3-us-west-1.amazonaws.com/ayx.community.assets/odsc_network.html). Image by author.

In this diagram, the circles are “nodes.” Each Twitter user identified here is considered a node in this network. The lines between the nodes are called “edges.” As you can see in the network graph, most edges lead to [@odsc](https://twitter.com/odsc), the Twitter account of the organizers of the conference, and it makes sense that they would end up central to the discussion of their own event.

However, as I mouse over and click on the individual nodes, it looks like nodes other than @odsc are also pretty well interconnected. For example, [@aliciaframe1](https://twitter.com/aliciaframe1) mentioned other users or was mentioned by them fairly often, as revealed by the blue nodes and edges below:

Image by author.

In addition to exploring the interactive diagram, I can also use the numeric output from the Network Analysis Tool to examine my potential influencers more closely. The output includes five network centrality measures, each of which reflect different ways of evaluating how “central” a node is to a network. You can read about [all the centrality measures](https://en.wikipedia.org/wiki/Centrality), but here are simplified definitions of each:

* **Betweenness**: the number of times a node serves as a bridge on the shortest path between other nodes. A node that is often a bridge can control the spread of information, allowing or limiting its flow.
* **Degree**: the number of nodes one link away from any one node. As [one source](https://www2.unb.ca/~ddu/6634/Lecture_notes/Lecture_4_centrality_measure.pdf) states, “Though simple, degree is often a highly effective measure of the influence or importance of a node: In many social settings people with more connections tend to have more power and [are] more visible.”
* **Closeness**: the average length of the shortest path possible from a specific node to all the other nodes in the network. The more central a node, the closer all the other nodes. This measure is sometimes used to reflect how quickly information might spread among nodes in a network.
* **Eigenvalue centrality** (“evcent” field in Designer): a measure of how influential a certain node is within the network, assigned relative to all the other nodes. The score is based on the idea that connections from “high-scoring” nodes are more valuable than connections from “low-scoring” nodes.
* **PageRank**: yes, [that](https://en.wikipedia.org/wiki/PageRank) PageRank you may have heard of. It’s somewhat similar to eigenvalue centrality, but it also includes the direction of the links between nodes and the weight or importance of those links, which can help identify people perceived as authoritative by others.

As you would expect from the top diagram above, the @odsc account scores most highly on all the centrality measures. However, looking further into the data reveals which individuals and companies were notable nodes during the conference.

*Image via* [*GIPHY*](https://media.giphy.com/media/xT9IgN8YKRhByRBzMI/giphy-downsized.gif)

Following this procedure with the goal of identifying influencers, you might be most interested in the degree or PageRank metrics. It would also be helpful to join your network analysis output with the original [user information retrieved from Twitter](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup) in order to have their centrality measures, profile, links, and follower data all together. This information will enrich your new insights into how these users have co-occurred with others in the collected tweets. You could then sort by followers, find users in specific locations, and also evaluate their centrality within the relevant network.

And, to get extra meta, you could even retrieve the lists of followers of your first round of potential influencers, and add them to your network analysis. Doing so would enlarge the network and might introduce people less tightly connected to your main search topic. However, if your initial gathering of account names resulted in a small number of potential influencers, this additional collection might help you identify more people to consider.

# Investigating the Influencers

Finally, you can use this same process to retrieve a sample of potential influencers’ recent tweets, then automate “reading” their past posts. With the [Alteryx Intelligence Suite](https://www.alteryx.com/products/alteryx-platform/intelligence-suite?utm_content=community) tools for [word clouds](https://help.alteryx.com/current/designer/word-cloud) and [sentiment analysis](https://help.alteryx.com/current/designer/sentiment-analysis), you can quickly get a sense of the content and tone of your influencer candidates’ social discussions.

Whether you’re selling dog beds to indulgent pet parents, building a podcast audience, or spreading public health information, social media influencers can be a powerful resource for sharing your message. Get a handle on their conversations quickly with these tools.

# Recommended Reading