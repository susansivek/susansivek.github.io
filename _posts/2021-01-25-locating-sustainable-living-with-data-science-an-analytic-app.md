---
title: "Locating Sustainable Living with Data Science + an Analytic App"
date: 2021-01-25
excerpt: "\"With more companies accepting that remote work is feasible for their employees, some formerly location-locked workers are exploring new possibilities for places to live."
original_url: "https://community.alteryx.com/t5/Data-Science/Locating-Sustainable-Living-with-Data-Science-an-Analytic-App/ba-p/706297"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Locating-Sustainable-Living-with-Data-Science-an-Analytic-App/ba-p/706297](https://community.alteryx.com/t5/Data-Science/Locating-Sustainable-Living-with-Data-Science-an-Analytic-App/ba-p/706297)*

With more companies accepting that remote work is feasible for their employees, some formerly location-locked workers are exploring new possibilities for places to live.

Our very own [@ewoodard](https://community.alteryx.com/t5/user/viewprofilepage/user-id/77457) suggested that we could use data and Alteryx to check out new options! We ran with her great idea and thought it would be interesting to see how different places measured up on aspects of sustainability. If sustainable living is important to you, why not pick a place that reflects those values?

While you can find plenty of lists of “green cities” on the interwebz, neighborhoods vary within cities. And since Alteryx lets us work through big datasets very quickly, why not consider, oh, every neighborhood in the U.S.? Mashing up public data with spatial information, and applying some analytic thinking and data science, all resulted in [an analytic app](https://gallery.alteryx.com/#!app/Sustainable%2BNeighborhood%2BFinder/6008dcf9826fd310d446c742) you can try now in the Alteryx Analytics Gallery! (But first, read on to find out how it works …)

## **Gathering Neighborhood Data**

I gathered data on the level of the [census block group](https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_geography_details.html#BLKGRP) (CBG), which is the smallest unit for which the U.S. Census Bureau provides its sample data. Each CBG typically contains 600 to 3,000 people. CBGs may work a bit better than ZIP codes for grouping households in consistent ways. (Check out [this article](https://carto.com/blog/zip-codes-spatial-analysis/) for a full discussion of some of the possible issues with ZIP codes.)

The analytic app uses data from these sources:

Fortunately, many government agencies offer data at the CBG level, letting us drill down to small areas that best fit our sustainability criteria. When the agencies didn’t specify CBGs, I was able to use Alteryx’s [Spatial Match](https://help.alteryx.com/current/designer/spatial-match-tool) and/or [Allocate Append](https://help.alteryx.com/current/designer/allocate-append-tool) tools to identify them myself.

Finally, CBG-level data wasn’t available for air quality, so I assigned each neighborhood the air quality metrics for its metro area, when available. Air does move around, after all!

## **Using Clustering to Diversify Results**

Unfortunately, it can be tricky to find neighborhoods that satisfy *all* of the sustainability criteria, especially if you prefer to be in a smaller city or outside of a metro area. I wanted the app to still offer something to the user who maybe only received a couple of matches to their criteria.

I used [clustering](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-K-Centroids-Cluster-Analysis/ta-p/302154) (the K-Centroids Cluster Analysis and Append Clusters tools) to identify and assign groups to all of the neighborhoods. With the clusters identified, the app will offer not just the perfect matches for the user’s chosen criteria, but also offer five more neighborhoods from the same cluster.

In addition to ensuring every user sees more than just a few results, this approach also might spark new ideas for the user, in terms of thinking of new geographic possibilities, and perhaps even noticing patterns or rethinking their original criteria selections.

## **Building the App**

With the data all tidied up and the clusters assigned to each CBG, the app was straightforward to construct (despite the fact that this is my first analytic app!). I found the [resources](https://community.alteryx.com/t5/Santalytics-2020/Analytic-App-and-Use-Case-Resources/ta-p/668861) that @WillM compiled for [Santalytics 2020](https://community.alteryx.com/t5/Santalytics-2020/gh-p/appchallenge) to be quite helpful, so check those out if you’re a fellow app newbie.

The app allows the user to choose how important various criteria are for their location selection, and then filters the CBGs to find those meeting (or exceeding) the criteria. The app provides maps of the locations and a table of the key information for each, plus a link to Google Maps for each place so it’s easy to investigate further.

Are you ready for a greener new neighborhood? [Try the app](https://gallery.alteryx.com/#!app/Sustainable%2BNeighborhood%2BFinder/6008dcf9826fd310d446c742) to see which places might fit you and your sustainability goals best.

#### *Where are you moving to? What are your ideas for using an analytic app? Comment below to share your neighborhood results or ideas on how you’d use an analytic app like this one!*

[Susan Currie Sivek](https://community.alteryx.com/t5/user/viewprofilepage/user-id/143008)    
**Data Science Journalist**

Susan Currie Sivek, Ph.D., is the data science journalist for the Alteryx Community, where she explores data science concepts with a global audience. Her background in academia and social science informs her approach to investigating data and communicating complex ideas — with a dash of creativity from her training in journalism. Susan also loves getting outdoors with her dog and relaxing with some good science fiction.