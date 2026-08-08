---
title: "Happiness is a Network of Friends"
date: 2020-04-21
excerpt: "Even though we may be physically distant from the people who are our closest social connections right now, those relationships feel more precious than ever. Quantifying the quantity and quality of those treasured social ties might feel a little…"
original_url: "https://community.alteryx.com/t5/Data-Science/Happiness-is-a-Network-of-Friends/ba-p/556129"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Happiness-is-a-Network-of-Friends/ba-p/556129](https://community.alteryx.com/t5/Data-Science/Happiness-is-a-Network-of-Friends/ba-p/556129)*

Even though we may be physically distant from the people who are our closest social connections right now, those relationships feel more precious than ever. Quantifying the quantity and quality of those treasured social ties might feel a little strange. But the strength of individuals’ social relationships is an important variable in the “Analytics of Happiness,” as the most recent episode of our Alter Everything podcast describes.

In the podcast, researcher Matthew Ackman explains how the [World Happiness Report](https://happiness-report.s3.amazonaws.com/2020/WHR20.pdf) (WHR) is generated annually by the United Nations Sustainable Development Solutions Network, a UN affiliate. It seems like quantifying happiness would be near impossible, but the WHR researchers have developed a set of measures to summarize the emotional status of each country’s population.

One data point used in the WHR happiness measures -- which feels especially poignant in the current moment -- is survey respondents’ answer to this Gallup World Poll question: “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?” Being able to answer “yes” to this question is important not only for happiness; people with robust support networks also may experience [better health and longer lives](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3150158/).

If you want to try analyzing your own network, data science (and Alteryx) have you covered. Although modeling and visualizing social networks have been part of multiple academic disciplines for over a century, data scientists have developed sophisticated ways of crunching much bigger data on interconnectivity. Designer’s own [Network Analysis Tool](https://help.alteryx.com/current/Network_Analysis.htm) provides a versatile way to explore and visualize network data. I tried out [this workflow](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Network-Analysis-Tool/m-p/5108/highlight/true#M2510) provided in the Community by [@Tim\_Napier](https://community.alteryx.com/t5/user/viewprofilepage/user-id/3596) and quickly generated this visualization of my own LinkedIn connections, grouped by company.

![SusanCS_0-1586964627973.png](/assets/images/posts/happiness-is-a-network-of-friends/medium-e07c22d6.png)

For Python and R folks, the package `igraph` is one option for exploring networks. [This example](https://rpubs.com/wctucker/302110) demonstrates the “Six Degrees of Kevin Bacon” game with `igraph` in R, and [this example](https://towardsdatascience.com/visualising-graph-data-with-python-igraph-b3cc81a495cf) shows how to use `igraph` in Python to analyze scholarly article authorship. Other uses for network analysis include social networking apps and analytics (obviously), recommender systems, user behavior analysis, text analysis and search engines.

![SusanCS_1-1586964627966.jpeg](/assets/images/posts/happiness-is-a-network-of-friends/medium-fb16b67c.jpg)

*Phylogenetic network of 160 SARS-CoV-2 genomes (*[*source*](https://www.pnas.org/content/early/2020/04/07/2004999117)*).*

At the moment, network analysis is also a tool for understanding pandemic spread. [One recent study](https://www.sciencedaily.com/releases/2020/04/200409085644.htm) used this approach to link genomic information among SARS-CoV-2 virus strains, tracing the evolution of the virus and its infection routes. That network is shown in the graphic above. Network modeling also [helps epidemiologists understand](https://physics.aps.org/articles/v13/43) how disrupting some social connections (for example, closing schools) might change the progress of a pandemic’s spread.

Right now, even though some of our personal networks may be disrupted, we are fortunate to live in a time when we can still socially connect, even if at a distance. And -- as the World Happiness Report suggests -- we’ll still gain so much personal and communal happiness from enjoying our networks of connections.