---
title: "How Spooky is Your City? Mapping and Predicting Scary Stuff"
date: 2020-10-29
excerpt: "\"Interactive maps and predictive modeling for creepy phenomena…why not? Let’s have some Halloween fun with data science."
original_url: "https://towardsdatascience.com/how-spooky-is-your-city-mapping-and-predicting-scary-stuff-26b7dea892bd"
publication: "Towards Data Science"
categories: [data-science]
Whether you’re the kind of person who seeks out the spooky or not, guess what: You probably live near some creepy things.
---
*Originally published at [https://towardsdatascience.com/how-spooky-is-your-city-mapping-and-predicting-scary-stuff-26b7dea892bd](https://towardsdatascience.com/how-spooky-is-your-city-mapping-and-predicting-scary-stuff-26b7dea892bd)*

## Interactive maps and predictive modeling for creepy phenomena…why not? Let’s have some Halloween fun with data science.

![](https://miro.medium.com/max/10000/1*XueuyJzLEM7knmtbO7tDSw.jpeg?q=20000000)

Photo *by* [*Gary Meulemans*](https://unsplash.com/@anakin1814?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/spooky?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*.*

Whether you’re the kind of person who seeks out the spooky or not, guess what: You probably live near some creepy things.

To commemorate the season, we thought it would be fun to do some macabre mapping and petrifying prediction of spooky phenomena. Data science doesn’t have to be just for serious subjects! I’ll show you how I used Alteryx Designer, Python and the mapping package Folium to analyze and map these data.

# The Spookiest Places in the U.S. (and the Least Spooky)

To look at how spooky U.S. metro areas are, I created a (silly) Spooky Score for each area, based on the density of cemeteries and haunted places in each metro area, as well as the per capita UFO sightings and Bigfoot encounters. (More on the data sources below.)

The map below shows 352 metro areas and, in popups, those data points for each. (Please [visit this site](https://community.alteryx.com/t5/Data-Science/How-Spooky-is-Your-City-Mapping-and-Predicting-Scary-Stuff/ba-p/657900) for the interactive version.) I’ll tell you below how I built it with Folium.

![](https://miro.medium.com/max/10000/1*TJuWp075z6Wfky19rAiv0w.png?q=20000000)

Image by author

> Explore the map and find your city! [Click to tweet](https://ctt.ac/X3Nf5) how scary your town is.

Did your city make the top 10?

## 🏆 Top 10 Spookiest Metro Areas 🏆

1. Worcester, MA-CT
2. Providence-Warwick, RI-MA
3. Washington-Arlington-Alexandria, DC-VA-MD-WV
4. Boston-Cambridge-Newton, MA-NH
5. Philadelphia-Camden-Wilmington, PA-NJ-DE-MD
6. New York-Newark-Jersey City, NY-NJ-PA
7. Barnstable Town, MA
8. Kingsport-Bristol-Bristol, TN-VA
9. Allentown-Bethlehem-Easton, PA-NJ
10. Cincinnati, OH-KY-IN

As a West Coast resident, I was a little bummed to see the decidedly eastern focus of the Top 10 list! (Surely all the Bigfoot sightings in Oregon count for something?!) But these rankings make sense as you dive into the data. The top 10 places tend to have large numbers of cemeteries packed into small geographic areas. They have long histories and many haunted places, and they have many UFO sightings (especially New York).

Did you discover from the map that you’re in a horrifying hotbed of paranormal activity? Want to get some distance from ghouls, aliens, Bigfoot and ghosts? Let’s see where in the U.S. you can be furthest away from the creepy and crawly. The heat map below — also built with Folium—is based on the latitude/longitude for all the spooky stuff: cemeteries, haunted places, Bigfoot encounters, and UFO sightings — so more intense areas on the heat map have more of those. (Please [visit this site](https://community.alteryx.com/t5/Data-Science/How-Spooky-is-Your-City-Mapping-and-Predicting-Scary-Stuff/ba-p/657900) for the interactive version.)

![](https://miro.medium.com/max/10000/1*7unOzA6WAZVdEdyHfEROOw.png?q=20000000)

Image by author

Though the heat map might initially make it seem like everywhere is ominous, zoom in to find an oasis of peace and quiet for your escape!

> Which quiet spot on this map will you choose to get away from ghosts, goblins and other scary creatures? [Click to tweet](https://ctt.ac/9PS2f) and share your destination.

# Finding the Frightening Places to Map

First, of course, I needed to find the creepy stuff: the locations and details of cemeteries, [haunted places](https://data.world/timothyrenner/haunted-places), [UFO sightings](https://data.world/timothyrenner/ufo-sightings) and [Bigfoot encounters](https://data.world/timothyrenner/bfro-sightings-data) around the country. Amazingly, the latter three, including latitude/longitude data, had all been compiled by data scientist Timothy Renner and shared publicly. The cemetery locations, however, were a little trickier to find. I used [these U.S. Census files](https://www2.census.gov/geo/tiger/TIGER2019/AREALM/) of notable landmarks in each state, filtering to identify only cemeteries, and pulled out their latitude and longitude.

After combining these data in Alteryx Designer, I used its spatial tool Create Points with the latitude/longitude for each “spooky place,” including all four categories of creepy stuff. Designer’s Allocate Input tool brought in useful demographic and geographic information for major U.S. metropolitan areas, including the spatial object representing the physical area of each city.

Ultimately, I wanted to assign each spooky place to its correct metro area. Plugging the spooky points and the metro areas’ spatial objects into Designer’s Spatial Match tool did all the work of figuring that out for me, and made it possible to join the demographic data to the places as well.

![](https://miro.medium.com/max/10000/0*tI01WUMFKbXJSISz?q=20000000)

Image from [GIPHY](https://gph.is/g/EqX1O6w)

# Constructing the Maps

I built these maps using the Python Tool within Alteryx Designer and the package [Folium](https://python-visualization.github.io/folium/), which was a super easy way to place the latitude/longitude points of each metro area onto a map and to generate a heat map. Folium uses [leaflet.js](https://leafletjs.com/) for interactivity, but all the JavaScript happens behind the scenes. A wide variety of customization options are possible, including eight different free background maps to give your map some style, as well as options to use tooltips, minimaps and emoji markers.

Folium also allows you to use HTML to make nicely formatted popups for your markers, too, which was fun to use here. [This example](https://www.kaggle.com/dabaker/fancy-folium) shows one way to format the HTML, and you can see how I used this option below.

I then set up the map to start at a specific location (the center of the continental U.S.), to use a dark theme, and to include a map scale. Additionally, because 352 markers on the map would overwhelm the viewer, I decided to cluster the markers; each cluster expands into separate markers as the user zooms in. The for loop iterates through the dataframe and generates the points for the map, formatted within the HTML I provided, and adds them to the clusters of markers to be placed on the map.

I also had the latitude and longitude for all the spooky encounters and locations in a separate data file, and that’s what I used to generate the heat map above. Creating a heat map with Folium is even simpler than making the marker-based map above:

Your finished map can be saved to an HTML file at a file path you designate. In Alteryx Designer, I just saved the two file paths I created into a dataframe and wrote it out of the Python Tool for convenience. Whatever method you use, just open the file in your browser to enjoy your creation.

With the information I’d collected at this point, making the maps was easy and fun. But in addition to figuring out where spookiness occurs in the U.S., I also wanted to know: Could we predict what would make a particular metro area more spooky?

![](https://miro.medium.com/max/10000/0*ss00sK-8bse1rF8s?q=20000000)

Image from [GIPHY](https://gph.is/2yAbItw)

# Adding Frightening Features

What else could make an area more spooky? I thought of a few possible factors for which I could locate publicly available data in a reasonable amount of time:

* Severe weather phenomena that could relate to perceptions of paranormal “activity”
* Locals’ beliefs about the paranormal (if more people believe, maybe more “happens”?)
* Population density (do spooky encounters tend to happen in areas where people are more or less spread out?)
* Locals’ ages (maybe older or younger populations are more inclined to see/report the paranormal?)
* Housing prices (maybe people in more or less affluent states tend to experience more spooky things?)

For severe weather data, I grabbed the [2018 records](https://www.spc.noaa.gov/wcm/#data) for tornadoes, hail and damaging wind events from the NOAA, and compiled them by state before matching them to my larger dataset (though with more time, I could’ve matched them all to specific metro areas with Alteryx Designer’s Spatial Match tool).

Public data regarding Americans’ beliefs about the paranormal was harder to find; there’s definitely data available, but most needed to be purchased. I ended up using the 2018 General Social Survey, which [included the question](https://gssdataexplorer.norc.org/variables/300/vshow): “Do you believe there is a life after death?” In the publicly available data, participants’ responses are only marked with one of nine geographic regions, not their specific location, but I was able to at least attach each paranormal encounter to the percent of people who believe in an afterlife for that region.

Population density was easy to calculate and add as a new variable using the Census data I previously brought in. That data also included the metro area median age. For housing prices, I used Zillow’s publicly available [median sale price data](https://www.zillow.com/research/data/) for single-family homes, and calculated the average for each state).

I didn’t find quite the ideal data for each of these, but moving forward with less-than-ideal data is just the usual, of course. So we’ll see if we can actually do any predictions of spookiness with these data.

![](https://miro.medium.com/max/10000/0*5C6GfeJ4DNP4VL9q?q=20000000)

Image from [GIPHY](http://gph.is/1nL3DK1)

# Modeling the Macabre

Admittedly, this is not the most “scientific” of data science tasks. But let’s see what we can come up with, just for the silly spookiness of it.

The goal of the predictive model is to predict the Spooky Score for a metro area. I chose to use as predictors the metro area’s population density, the region’s belief in an afterlife, the average home price, all of the separate weather variables, and the metro area population’s median age. The Spooky Scores overall didn’t correlate strongly with any single variable; the top correlation was 0.37 with population density.

I also noticed in exploratory analysis that there was a strong right skew in the Spooky Scores, so prior to moving forward with modeling, I did a [log transformation](https://medium.com/@ODSC/transforming-skewed-data-for-machine-learning-90e6cc364b0) of the Spooky Scores to achieve a more normal distribution in the scores. Using [a tip from](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/How-to-do-Feature-Normalization-in-Alteryx-incl-Python-Code-tool/td-p/313366) [@DavidM](https://community.alteryx.com/t5/user/viewprofilepage/user-id/10894) on the Alteryx Community, I also [normalized](https://towardsai.net/p/data-science/how-when-and-why-should-you-normalize-standardize-rescale-your-data-3f083def38ff) the other predictors, as their scale varied widely.

I tried linear regression, spline, and random forest models. Using an 80/20 training/test split and the [Model Comparison](https://help.alteryx.com/current/designer/model-comparison-tool) tool, I found that the random forest model performed best, explaining 58 percent of the variance in the scores. This model offered an RMSE of 0.56 and a 0.79 correlation between its predictions and the actual Spooky Scores. The plot below shows the relative importance of the features in the model.

![](https://miro.medium.com/max/10000/0*J-313h8jbUYFFFw2?q=20000000)

Image by author

I also let the [Assisted Modeling](https://community.alteryx.com/t5/Analytics/One-Click-Modeling-With-Alteryx-Intelligence-Suite/ba-p/614316) capabilities of Alteryx Designer’s Intelligence Suite take a crack at predicting Spooky Scores. Its best-performing model, using the same train/test data, was also a random forest regressor, with an RMSE of 0.72 and about 0.78 correlation between its predictions and the actual Spooky Scores. However, Assisted Modeling also informed me that the [adjusted R-squared](https://www.statisticshowto.com/adjusted-r2/) was 0.48; adjusted R-squared is another measure of correlation that takes into account the number of variables used in the model, penalizing models with more variables.

![](https://miro.medium.com/max/10000/0*RX7Ymh8xX_SjYYCd?q=20000000)
![](https://miro.medium.com/max/10000/0*Y7Au9621yy5AF5vx?q=20000000)

Above three images by author

To enhance this analysis, I’d have loved to get more specific with metro area-level data on beliefs in the paranormal, and I’d take more time fine-tuning the weather and home price data, instead of using state aggregations. Additionally, it would have been cool to include data for: 1) the year a city was founded, in order to address the number of cemeteries accumulated over time (as discussed in [this blog post/visualization](https://www.joshuastevens.net/blog/graveyards-of-the-contiguous-usa/)); and 2) the distance to the nearest military base and/or airport, to help account for UFO sightings (or would it?! 👽 👽 👽).

So, neither modeling result was really spectacular, but considering what we’re modeling and the degree of imprecision in the data — well, they’re just fine, and it’s fun to think about what these models tell us about spookiness. Areas with higher population density have more people today, but they also have more corpses in all their cemeteries. The severe weather events don’t seem to have strong connections to the paranormal encounters (I thought some sort of weather would at least correlate with UFO sightings, but nope!).

Maybe spooky things aren’t so predictable after all … they’re just spooky, and that’s what keeps them fun and intriguing. The mysteries continue! 👻