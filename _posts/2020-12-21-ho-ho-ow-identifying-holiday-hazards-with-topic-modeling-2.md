---
title: "Ho, Ho … Ow! Identifying Holiday Hazards with Topic Modeling"
date: 2020-12-21
excerpt: "\"When I think of dangerous Christmas decorations, I always think of scenes like this one from “National Lampoon’s Christmas Vacation”:"
original_url: "https://community.alteryx.com/t5/Data-Science/Ho-Ho-Ow-Identifying-Holiday-Hazards-with-Topic-Modeling/ba-p/682235"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Ho-Ho-Ow-Identifying-Holiday-Hazards-with-Topic-Modeling/ba-p/682235](https://community.alteryx.com/t5/Data-Science/Ho-Ho-Ow-Identifying-Holiday-Hazards-with-Topic-Modeling/ba-p/682235)*

When I think of dangerous Christmas decorations, I always think of scenes like this one from “National Lampoon’s Christmas Vacation”:

And yet the most dangerous part of holiday decorating doesn’t involve electricity.

I downloaded and analyzed the U.S. Consumer Product Safety Commission’s latest 10 years of data on injuries involving Christmas-related products. Applying a bit of data science, we’ll find where danger might lurk among the sparkly lights and shiny ornaments. You might be surprised: One dangerous item is something you probably use year-round.

## **Unwrapping the Data**

There are 3,917 injuries related to Christmas products in the dataset from the CPSC’s [National Electronic Injury Surveillance System](https://www.cpsc.gov/Research--Statistics/NEISS-Injury-Data). Covering the years 2010 to 2019, the data include the injured person’s gender, age, involved body part, diagnosis, location (e.g., home, school), whether they were admitted to a hospital or not, and a brief text narrative of the incident. Although I retrieved data only for injuries including Christmas products, other involved products or key features of the injuries are also included (e.g., the injury occurred on a porch).

Here’s the first surprise: In about half of the injuries, non-electric Christmas decorations were a major culprit. People aren’t primarily getting shocked by their decorations; instead, they’re stepping on them, getting cut by them and even eating them (well, those are mostly very young folks, unfortunately!). Sometimes they just want to stay festive by attempting to permanently wear the ornaments: “13-month-old male has a Christmas jingle bell stuck on thumb.” (Don’t worry; it was successfully removed.)

![holiday injuries infographic for blog post.png](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/large.jpeg)

Christmas tree light bulbs were also often chewed or ingested by little ones. Adults strained their backs, necks and other body parts while hanging their lights. Be sure to warm up and stretch before decorating, folks!

![SusanCS_1-1608251118050.gif](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/medium.png)

Image via GIPHY

But most frightening of all: the ladders. I converted the “disposition” variable, which showed whether an injured person was treated and released or admitted to the hospital, into a 0 or 1 “severity” score, respectively. Looking just at the primary product identified for each incident, I averaged those severity scores across all the incidents for each product to see how often various products were associated with trips to the hospital. An average closer to 1 indicates a greater proportion of more severe incidents.

![SusanCS_2-1608251117032.png](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/large.bin)

Although ladders weren’t the most frequently occurring product among these injuries, they stand out among the products for the relative frequency and severity of incidents. 😧

## **The Stories Behind the Injuries**

Although [exploratory data analysis](https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267) reveals some of the potential risks of different Christmas items, we also have in this dataset a potentially rich source of information about Christmas injuries: the text narratives about each incident. Reading almost 4,000 of them doesn’t sound like much fun, but what if Designer could handle that task for us?

Fortunately, the [Intelligence Suite](https://community.alteryx.com/t5/Analytics/Unleashing-Advanced-Analytics-with-the-Alteryx-Intelligence/ba-p/574803) is an ideal tool for this task! We can feed the narratives to the Text Pre-Processing, Topic Modeling and Word Cloud tools to gain insights into the stories behind the data.

First, the topic modeling (check out [this blog post series](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-1-What-is-LDA/ba-p/611874) if you need a refresher!): I ran the narratives through pre-processing and into the Topic Modeling tool. I asked the model to look for three primary topics. The topics don’t come back neatly labeled, and sometimes it can be difficult to discern something coherent from the groupings of words provided to represent each topic. However, in this case, the topics seem readily apparent, as shown in the GIF below:

![SusanCS_3-1608251117036.gif](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/medium-1fec01d8.png)

Topic 1 looks tree-decorating related, with “decoration,” “strain,” “putt” (the [lemmatized](https://community.alteryx.com/t5/Data-Science/Text-Normalization-in-Alteryx/ba-p/611283) version of “putting,” not a golf reference!), and “lumbar” showing up. Topic 2 is more focused on ornament-related injuries and ingestion, with “foot,” “glass,” “swallow,” “foreign” (as in “foreign body”) and “piece” coinciding. (Anyone else cringing? Sorry!) Finally, Topic 3 is where ladders, lights and gravity coincide. “Fall,” “light,” “ladder” and “hang” are the top words here.

The scores for each topic are added to each incident in the dataset; I used a formula to identify the highest scoring topic for each incident. We can check out which topics, or kinds of incidents, might potentially occur more often alongside other variables. For example, we can see if age might relate to varieties of injuries. I used the [Tile](https://help.alteryx.com/current/designer/tile-tool) tool to quickly create age groups: up to age 5; 5 to 24; 25 to 54; and 55 and up. I made a [Contingency Table](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Contingency-Table/ta-p/356042) showing the percentage of each age group’s injuries that best fit into each topic:

![contingency.png](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/large-38fdecb4.bin)

Christmas product injuries definitely shift as we age. We eventually learn not to try to eat ornaments, but physical strains and falls become more prevalent among older folks.

And finally, this “festive” word cloud sums it all up: the text of all the narratives, minus a few obvious [stop words](https://en.wikipedia.org/wiki/Stop_word) that were already self-evident from the theme, like “Christmas.”

![word_cloud_crop.png](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/374x401.png)

## **A Bonus Analytic Method**

We could also use market basket analysis on this dataset in a somewhat atypical way. (Refresh your knowledge of this approach with our two-part [blog](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/ba-p/661963) [discussion](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-102-Alteryx-Designer-Python/ba-p/662029)!) We could consider each of these injury reports like a “transaction,” and determine the most frequent co-occurrences of the involved products.

![SusanCS_6-1608251117103.gif](/assets/images/posts/ho-ho-ow-identifying-holiday-hazards-with-topic-modeling-2/medium-a82efcfe.png)

Image via GIPHY

Using the market basket tools, we can identify the combination of injury products/features with the highest [lift](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/ba-p/661963): balconies and electric Christmas decorations (other than lights). Yikes. Combinations of decorations with porches, shelves and fireplaces also earned high rankings among the product combinations, even above combinations including ladders. I’m sure you can imagine many possible scenarios.

The moral of this data-driven holiday tale? Stay low to the ground, handle ornaments gently and beware of ladders! Don’t become part of next year’s dataset; have a fun and safe holiday season. 🎄

*P.S.: Check out the holiday injury data yourself and try out these approaches with the attached workflow.*