---
title: "Saving Koalas with Maps and Entropy"
date: 2020-05-26
excerpt: "What’s the probability of finding a koala in your neighborhood?
Unfortunately, it’s zero in my neighborhood in Oregon. But for the lucky folks in the areas of Australia where these adorable critters reside, there’s a real chance that a koala could be…"
original_url: "https://community.alteryx.com/t5/Data-Science/Saving-Koalas-with-Maps-and-Entropy/ba-p/575116"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Saving-Koalas-with-Maps-and-Entropy/ba-p/575116](https://community.alteryx.com/t5/Data-Science/Saving-Koalas-with-Maps-and-Entropy/ba-p/575116)*

![SusanCS_0-1589911058491.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/113737i0EE8A31C524DD244/image-size/medium?v=1.0&px=400)

What’s the probability of finding a koala in your neighborhood?

Unfortunately, it’s zero in my neighborhood in Oregon. But for the lucky folks in the areas of Australia where these adorable critters reside, there’s a real chance that a koala could be nearby at any given moment. And, thanks to an innovative mapping project, residents of New South Wales in Australia can find out their location’s “koala likelihood” -- vital information for helping these cute animals.

I learned about this project after listening to this week’s episode of the Alter Everything podcast, which features the work of One Tree Planted and other groups who are using data for environmental restoration and wildlife protection. I had to check out the koala mapping projects that were mentioned -- cuteness plus data, yes, please! -- and found the Koala Likelihood Map especially interesting.

The [Koala Likelihood Map](https://datasets.seed.nsw.gov.au/dataset/koala-likelihood-map-v2-0-august-2019) provides information on koala habitat in order to preserve the environments where these unique animals live. These efforts are even more important after the devastating wildfires this year and last year in Australia.

I wanted to see how the mapping team developed their koala likelihood model and to find out what we could learn for other kinds of modeling from their creative thinking. As it turns out, maximum entropy modeling -- in addition to having a cool name -- turns out to be relevant to this kind of project, and has lots of uses in other areas, too.

### **Koalas Here, Koalas (Not) There, but More Koalas Everywhere**

The Koala Likelihood Map is a project of the New South Wales Department of Planning, Industry and Environment. New South Wales (NSW) is Australia’s most populous state, with the most humans and about [30,000 to 40,000 wild koalas](https://koala.nsw.gov.au/). The map identifies areas where koalas might be present. The map quickly demonstrates areas humans need to protect to preserve these unusual animals.

![SusanCS_1-1589911058439.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/113738iF58CDF061D24D2A6/image-size/medium?v=1.0&px=400)

A look at “koala likelihood” near Sydney.

By cleverly combining data sources, the Koala Likelihood Map displays a percent likelihood that a particular square on the map grid will contain koalas, even including a confidence interval for that prediction. The data include a model for koala-appropriate habitat locations; data on koala-preferred tree species, native plant life, and bodies of water; maps of Areas of Regional Koala Significance, where koala populations and threats exist; and a map of all koala sightings recorded through [NSW BioNet](http://www.bionet.nsw.gov.au/), which tracks wildlife sightings submitted by professional and citizen scientists.

![SusanCS_2-1589911058579.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/113736iB5FE54D7ADD2F15D/image-size/medium?v=1.0&px=400)

Some of the koala sightings in 2019.

The researchers [validated](https://www.epa.nsw.gov.au/your-environment/native-forestry/mapping-research/koala-mapping-program/mapping-koala-occurrence) their approach through an independent survey of koalas that supported their model and map. The koala map’s availability has important effects on strategies for koalas’ preservation, keeping these critters’ cuteness around and protecting biodiversity.

### **Koalas and … Entropy?**

When I dug into a paper distributed by the mapping team as part of their initial 2014 mapping effort, I found the appendix on their modeling choices especially interesting. The map designers decided not to use a popular prediction method for species prevalence, called *maximum entropy modeling*, because it would likely predict koalas’ presence in areas where there had in fact been little data gathering. Instead, they used a simpler method that reflected koalas’ known presence in an area relative to the numbers of other mammals, as counted in wildlife surveys.

Yet maximum entropy, or “maxent,” modeling is still a useful tool for not only in biology, but also in computer vision and natural language processing (NLP) tasks, like sentiment analysis, spam detection and translation. The `NLTK` package in Python for NLP has a [module](https://www.nltk.org/api/nltk.classify.html?highlight=maxent#module-nltk.classify.maxent) for maxent modeling. These models classify data by calculating which labels or conditions generate maximum entropy.

![SusanCS_3-1589911059105.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/113739i2C6A0CFE056CA7CD/image-size/medium?v=1.0&px=400)

Koala experiencing the absence of entropy

Entropy can be thought of as “disorder” or variation. [Decision trees](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Planting-Seeds-An-Introduction-to-Decision-Trees/ta-p/134623), for example, are built by [minimizing the entropy](https://bricaud.github.io/personal-blog/entropy-in-decision-trees/) in their nodes as they classify data, so each resulting group is as orderly and consistent as possible. There is another stage in decision tree usage where entropy could also apply. When we consider predictions generated by a decision tree, one label might tend to dominate, or we might see that the chance of classification into any one label was pretty even across all our labels. In the former situation, we could say that entropy was low in those data and in that system of labels we applied; one bucket tidily caught most of our data. In the latter, entropy was high, with data getting distributed all over into different bins.

What if you designed a model based on that state of higher entropy? [Maxent modeling](https://www.nltk.org/book/ch06.html#maximum_entropy_index_term) chooses the option that demonstrates the most entropy and that is consistent with “what we already know” about the data, i.e., its existing distribution. The model selects the most “uniform” distribution among the features you want to analyze -- like the “different bins” scenario above. The algorithm uses iterative optimization to figure out this maximum-entropy solution, and it can take a long time to train a model with this method. (Here’s [a more complete explanation](https://dl.acm.org/ft_gateway.cfm?id=234289&type=pdf) of how maxent models work.) These models, despite what superficially seems like an embrace of chaos, often perform well. And although they might not have been ideal for the koala map, maxent models still have lots of utility in other areas.

![SusanCS_4-1589911059846.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/113740i40D2CD3329F90AE2/image-size/medium?v=1.0&px=400)

Fortunately, as the Alter Everything episode shows, there are creative folks like the Koala Likelihood Map creators and many others working to help koalas and other wildlife with all kinds of sophisticated data strategies. For example, [drone imagery and convolutional neural networks](https://www.nature.com/articles/s41598-019-39917-5) might play a part. We can also try to [predict](https://www.publish.csiro.au/AM/AM16043) *where* a koala might cross the road -- but we’re probably never going to know exactly *why*. (Sorry not sorry.)

Check out the podcast episode for more on Australian critters, conservation and data analytics.