---
title: "How Spooky is Your City? Mapping and Predicting Scary Stuff"
date: 2020-10-29
excerpt: "Whether you’re the kind of person who seeks out the spooky or not, guess what: You probably live near some creepy things.
To commemorate the season, we thought it would be fun to do some macabre mapping and petrifying prediction of spooky phenomena.…"
original_url: "https://community.alteryx.com/t5/Data-Science/How-Spooky-is-Your-City-Mapping-and-Predicting-Scary-Stuff/ba-p/657900"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/How-Spooky-is-Your-City-Mapping-and-Predicting-Scary-Stuff/ba-p/657900](https://community.alteryx.com/t5/Data-Science/How-Spooky-is-Your-City-Mapping-and-Predicting-Scary-Stuff/ba-p/657900)*

Whether you’re the kind of person who seeks out the spooky or not, guess what: You probably live near some creepy things.

To commemorate the season, we thought it would be fun to do some macabre mapping and petrifying prediction of spooky phenomena. Data science doesn’t have to be just for serious subjects! Enjoy this eerie adventure into the creepier side of data.

## **The Spookiest Places in the U.S. (and the Least Spooky)**

To look at how spooky U.S. metro areas are, I created a (silly) Spooky Score for each area, based on the density of cemeteries and haunted places in each metro area, as well as the per capita UFO sightings and Bigfoot encounters. (More on the data sources below.) The map below shows 352 metro areas and those data points for each.

Did your city make the top 10?

1. Washington-Arlington-Alexandria, DC-VA-MD-WV
2. Philadelphia-Camden-Wilmington, PA-NJ-DE-MD
3. New York-Newark-Jersey City, NY-NJ-PA
4. Kingsport-Bristol-Bristol, TN-VA
5. Allentown-Bethlehem-Easton, PA-NJ

As a West Coast resident, I was a little bummed to see the decidedly eastern focus of the Top 10 list! (Surely all the Bigfoot sightings in Oregon count for something?!) But these rankings make sense as you dive into the data. The top 10 places tend to have large numbers of cemeteries packed into small geographic areas. They have long histories and many haunted places, and they have many UFO sightings (especially New York).

Did you discover from the map that you’re in a horrifying hotbed of paranormal activity? Want to get some distance from ghouls, aliens, Bigfoot and ghosts? Let’s see where in the U.S. you can be furthest away from the creepy and crawly. The map below is based on the latitude/longitude for all the spooky stuff: cemeteries, haunted places, Bigfoot encounters, and UFO sightings — so more intense areas on the heat map have more of those.

Though the heat map might initially make it seem like everywhere is ominous, zoom in to find an oasis of peace and quiet for your escape!

#### *Which quiet spot on this map will you choose to get away from ghosts, goblins and other scary creatures? [Click to tweet](https://ctt.ac/9PS2f) and share your destination.*

## **Finding the Frightening Places to Map**

First, of course, I needed to find the creepy stuff: the locations and details of cemeteries, [haunted places](https://data.world/timothyrenner/haunted-places), [UFO sightings](https://data.world/timothyrenner/ufo-sightings) and [Bigfoot encounters](https://data.world/timothyrenner/bfro-sightings-data) around the country. Amazingly, the latter three, including latitude/longitude data, had all been compiled by data scientist Timothy Renner and shared publicly. The cemetery locations, however, were a little trickier to find. I used [these U.S. Census files](https://www2.census.gov/geo/tiger/TIGER2019/AREALM/) of notable landmarks in each state, filtering to identify only cemeteries, and pulled out their latitude and longitude.

After combining these data, I used spatial tool Create Points with the latitude/longitude for each “spooky place,” including all four categories of creepy stuff. The Allocate Input tool brought in useful demographic and geographic information for major U.S. metropolitan areas, including the spatial object representing the physical area of each city.

Ultimately, I wanted to assign each spooky place to its correct metro area. Plugging the spooky points and the metro areas’ spatial objects into the Spatial Match tool did all the work of figuring that out for me, and made it possible to join the demographic data to the places as well.

![SusanCS_0-1603914619571.gif](https://community.alteryx.com/t5/image/serverpage/image-id/141556i3F80BDCF4260439E/image-size/medium?v=1.0&px=400)

## **Constructing the Maps**

I built these maps using the Python Tool and the package [Folium](https://python-visualization.github.io/folium/), which was a super easy way to place the latitude/longitude points of each metro area onto a map and to generate a heat map. Folium uses [leaflet.js](https://leafletjs.com/) for interactivity, but all the JavaScript happens behind the scenes. A wide variety of customization options are possible, including eight different free background maps to give your map some style, as well as options to use tooltips, minimaps and emoji markers.

Folium also allows you to use HTML to make nicely formatted popups for your markers, too, which was fun to use here. [This example](https://www.kaggle.com/dabaker/fancy-folium) shows one way to format the HTML, and you can see how I used this option in the attached workflow as well.

Your finished map can be saved to an HTML file that goes to a file path you designate (be sure to replace the placeholder text in the Jupyter notebook for this). In the attached workflow, I saved the two file paths I created into a dataframe and wrote it out of the Python Tool for convenience. Open the file in your browser to enjoy your creation.

With the information I’d collected at this point, making the maps was easy and fun. But in addition to figuring out where spookiness occurs in the U.S., I also wanted to know: Could we predict what would make a particular metro area more spooky?

![SusanCS_1-1603914619649.gif](https://community.alteryx.com/t5/image/serverpage/image-id/141555iFA7383206B3918AB/image-size/medium?v=1.0&px=400)

## **Adding Frightening Features**

What else could make an area more spooky? I thought of a few possible factors for which I could locate publicly available data in a reasonable amount of time:

* Severe weather phenomena that could relate to perceptions of paranormal “activity”
* Locals’ beliefs about the paranormal (if more people believe, maybe more “happens”?)
* Population density (do spooky encounters tend to happen in areas where people are more or less spread out?)
* Locals’ ages (maybe older or younger populations are more inclined to see/report the paranormal?)
* Housing prices (maybe people in more or less affluent states tend to experience more spooky things?)

Want to know which data I picked for each of these in more detail? Pop open the spoiler tag below.

I didn’t find quite the ideal data for each of these, but moving forward with less-than-ideal data is just the usual, of course. So we’ll see if we can actually do any predictions of spookiness with these data.

![SusanCS_2-1603914619556.gif](https://community.alteryx.com/t5/image/serverpage/image-id/141554i93756F8870A134E1/image-size/medium?v=1.0&px=400)

## **Modeling the Macabre**

Admittedly, this is not the most “scientific” of data science tasks. But let’s see what we can come up with, just for the silly spookiness of it.

The goal of the predictive model is to predict the Spooky Score for a metro area. I chose to use as predictors the metro area’s population density, the region’s belief in an afterlife, the average home price, all of the separate weather variables, and the metro area population’s median age. The Spooky Scores overall didn’t correlate strongly with any single variable; the top correlation was 0.37 with population density.

I also noticed in exploratory analysis that there was a strong right skew in the Spooky Scores, so prior to moving forward with modeling, I did a [log transformation](https://medium.com/@ODSC/transforming-skewed-data-for-machine-learning-90e6cc364b0) of the Spooky Scores to achieve a more normal distribution in the scores. Using [a tip from](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/How-to-do-Feature-Normalization-in-Alteryx-incl-Python-Code-tool/td-p/313366) [@DavidM](https://community.alteryx.com/t5/user/viewprofilepage/user-id/10894), I also [normalized](https://towardsai.net/p/data-science/how-when-and-why-should-you-normalize-standardize-rescale-your-data-3f083def38ff) the other predictors, as their scale varied widely.

I tried linear regression, spline, and random forest models. Using an 80/20 training/test split and the [Model Comparison](https://help.alteryx.com/current/designer/model-comparison-tool) tool, I found that the random forest model performed best, explaining 58 percent of the variance in the scores. This model offered an RMSE of 0.56 and a 0.79 correlation between its predictions and the actual Spooky Scores. The plot below shows the relative importance of the features in the model.

![SusanCS_3-1603914619568.png](https://community.alteryx.com/t5/image/serverpage/image-id/141557iD84F66DDC15E7179/image-size/medium?v=1.0&px=400)

I also let [Assisted Modeling](https://community.alteryx.com/t5/Analytics/One-Click-Modeling-With-Alteryx-Intelligence-Suite/ba-p/614316) take a crack at predicting Spooky Scores. Its best-performing model, using the same train/test data, was also a random forest regressor, with an RMSE of 0.72 and about 0.78 correlation between its predictions and the actual Spooky Scores. However, Assisted Modeling also informed me that the [adjusted R-squared](https://www.statisticshowto.com/adjusted-r2/) was 0.48; adjusted R-squared is another measure of correlation that takes into account the number of variables used in the model, penalizing models with more variables.

![SusanCS_4-1603914619600.png](https://community.alteryx.com/t5/image/serverpage/image-id/141559i900BC15F0885ACE7/image-size/large?v=1.0&px=999)
![SusanCS_5-1603914619583.png](https://community.alteryx.com/t5/image/serverpage/image-id/141558i65142E1F86F0E9F2/image-size/large?v=1.0&px=999)
![SusanCS_6-1603914619549.png](https://community.alteryx.com/t5/image/serverpage/image-id/141560i2A88BC4A83516947/image-size/large?v=1.0&px=999)

To enhance this analysis, I’d have loved to get more specific with metro area-level data on beliefs in the paranormal, and I’d take more time fine-tuning the weather and home price data, instead of using state aggregations. Additionally, it would have been cool to include data for: 1) the year a city was founded, in order to address the number of cemeteries accumulated over time (as discussed in [this blog post/visualization](https://www.joshuastevens.net/blog/graveyards-of-the-contiguous-usa/)); and 2) the distance to the nearest military base and/or airport, to help account for UFO sightings (or would it?! 👽 👽 👽).

So, neither modeling result was really spectacular, but considering what we’re modeling and the degree of imprecision in the data — well, they’re just fine, and it’s fun to think about what these models tell us about spookiness. Areas with higher population density have more people today, but they also have more corpses in all their cemeteries. The severe weather events don’t seem to have strong connections to the paranormal encounters (I thought some sort of weather would at least correlate with UFO sightings, but nope!).

Maybe spooky things aren’t so predictable after all … they’re just spooky, and that’s what keeps them fun and intriguing. The mysteries continue! 👻