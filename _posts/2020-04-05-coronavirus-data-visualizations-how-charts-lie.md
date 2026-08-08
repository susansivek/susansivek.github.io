---
title: "Coronavirus Data Visualizations + How Charts Lie"
date: 2020-04-05
excerpt: "\"We’ve all got that one Facebook friend who posts charts that make you cringe: the ever-popular 3D pie chart, the questionable bar chart with no source or the scatter plot “proving” that X causes Y."
original_url: "https://www.alteryx.com/input/coronavirus-data-visualizations-and-how-charts-lie"
publication: "Alteryx"
categories: [data-science]
---
*Originally published at [https://www.alteryx.com/input/coronavirus-data-visualizations-and-how-charts-lie](https://www.alteryx.com/input/coronavirus-data-visualizations-and-how-charts-lie)*

We’ve all got that one Facebook friend who posts charts that make you cringe: the ever-popular 3D pie chart, the questionable bar chart with no source or the scatter plot “proving” that X causes Y.

Unfortunately, the novel coronavirus (COVID-19) pandemic provides new material for the same data visualization problems that have always existed. In a time of uncertainty and fear, poorly designed visualizations can spread misinformation and provoke even more emotion.

I recently read Alberto Cairo’s 2019 book, "How Charts Lie: Getting Smarter about Visual Information," and have pulled out some major points from the book that can inform how we create and analyze data visualizations about any topic. Cairo, a journalist, designer, and University of Miami professor, is also the author of the well-known data visualization books "The Functional Art" and "The Truthful Art."

"How Charts Lie" is an excellent primer for anyone wanting to develop their “graphicacy,” or graphical literacy, and is a terrific reminder of key principles of good visualization design for anyone who ever generates a chart. Though the book’s title sounds negative, Cairo focuses primarily on the ways designers may inadvertently misrepresent their data and mislead viewers. To be sure, there are those who make charts deliberately to mislead and confuse, but this book is mainly for readers hoping to make a good, honest chart, or who just want to understand charts better.

I’ve chosen a few recent coronavirus-related visualizations to demonstrate some of his major points. Instead of being like your cringe-y Facebook friend, though, I’ll show you some interesting visualizations that show the thoughtful, rigorous communication of data that he encourages. As Cairo notes, “Public debates in modern societies are driven by statistics, and by charts, which are the visual depiction of those statistics.” Just having a chart lends you authority and credibility. That’s a power to wield carefully! Let’s see how it’s being done well at this critical time.

##### Simpler is Not Always Better

Should a good chart be understandable at a glance? Not necessarily, Cairo says.

**“Contrary to what many people believe, most good charts aren’t simple, pretty illustrations that can be understood easily and intuitively,” Cairo writes. Complexity is sometimes necessary to effectively communicate complicated things: “Many [charts], particularly those that contain rich and deep messages, may require time and effort, which will pay off if the chart is well designed. Many charts can’t be simple because the stories they tell aren’t simple.”**

For example, the chart below [from the "Financial Times](https://www.ft.com/coronavirus-latest)" is pretty complicated at first glance.

*(To note: All charts included here are from March 25, 2020.)*

*![COVID chart](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/ft-covid-chart-3c588e0e.png)*

There’s a lot going on here **—** numbers on two vertical axes! Colors! Dashed and dotted lines! And some stars sprinkled about for good measure. Whew. And yet, investing time in understanding this chart pays off. Not only can you compare the number of coronavirus deaths in each country, but it’s also easy to see the countries’ trajectories, and how the slope of each country’s line compares to benchmarks (the dashed lines marking “deaths double every day,” two days, etc.). Continental trends are also visible through the lines’ color-coding. The stars mark significant events. Taking time to fully grasp each element of this chart provides the viewer with a ton of information.

That chart tells a lot about the pandemic story. But does it tell us why these countries have such different trajectories **—** for example, why South Korea and Japan look so different from other countries? Or how those starred events affected the disease’s spread **—**for example, whether Spain’s lockdown decision made any impact?

As well constructed as it is, this chart can’t answer these questions. Cairo says that charts “just help us discover intriguing features that may later lead us to look for those answers by other means. Good charts empower us to pose good questions.” Those are the bigger, deeper questions that will help policymakers and public health experts figure out the right path forward.

##### Be Honest About Uncertainty

We’d all love to be able to generate completely accurate measurements and predictions, but that’s not realistic (and recent events sure show that, well, you just never know what’s coming next). But the presence of statistics and a chart can imply certainty, even if you don’t mean to imply that your data provide a definitive answer. As Cairo writes,

**“Uncertainty confuses many people because they have the unreasonable expectation that science and statistics will unearth precise truths, when all they can yield is imperfect estimates that can always be subject to changes and updates.”**

Cairo says that the “crisp and sharp” edges of a nice, clean traditional chart can be misleading, and we should be “mentally blurring” those edges to allow uncertainty into our understanding of the data. Chart designers can also incorporate literal blurriness.

A current example of this kind of “blurriness” that I found effective is the bottom portion of [this pyramid chart from Our World in Data](https://ourworldindata.org/coronavirus#the-severity-of-the-symptoms-of-covid-19), which has assembled a fascinating set of constantly updated visualizations related to the pandemic. The designers acknowledge here that though we have a reasonably good handle on the data in the upper portions of the pyramid, there’s still uncertainty around the true number of actual coronavirus cases. The blurry bottom portion of the pyramid is also the widest, showing there could have been a great many unrecognized cases, beyond even the thousands of known mild cases.

![Severity of coronavirus cases in China](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/Severity-of-coronavirus-cases-in-China-1-34470a18.webp)

Acknowledging the presence of uncertainty, even in more routine business and life situations, can help your chart’s viewers take away a more realistic understanding of your data and the insights it can offer. Some familiar [examples of showing uncertainty](https://flowingdata.com/2018/01/08/visualizing-the-uncertainty-in-data/) include displaying ranges or confidence intervals on a chart; showing time series forecasts with a [fan chart](https://en.wikipedia.org/wiki/Fan_chart_(time_series)) (like the one below, generated with the [TS Forecast](https://help.alteryx.com/current/TS_Forecast.htm) tool, that displays 80% and 95% confidence intervals in dark and light gray respectively); or sharing a distribution instead of a single measure of central tendency (e.g., a mean or median) when a solitary value may not effectively capture the possibilities for a variable.

![Fan chart](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/time-series-fan-chart-5647c458.png)

Use Maps Wisely

Cairo also discusses the use of maps, which he says are some of “most misused” data visualizations. For example, a chart creator might color a U.S. map with different shades in each state to show how many customers a nationwide company has in each state, but in doing so ends up really just reflecting a larger or smaller state population. After all, the more people, the more likely there’s a large number of customers there. Instead, Cairo suggests, it usually makes more sense to use the adjusted data for each area, like a [per capita](https://www.thebalance.com/per-capita-what-it-means-calculation-how-to-use-it-3305876) measurement or a percentage of the population, in lieu of the raw data.

There are probably thousands of maps on the internet displaying coronavirus-related data, including [static](https://inspiringingenuity.net/2020/03/24/a-tale-of-2-maps/), [animated](https://graphics.reuters.com/CHINA-HEALTH-MAP/0100B59S39E/index.html) and [interactive](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) varieties. Their creators made difficult choices about how best to display their data, though most have chosen to display raw numbers of cases in each locality instead of normalized numbers.

Here are two maps from Our World in Data side by side: the map with the red color scheme displays the raw count of cases, while the map with the blue-green color scheme displays a normalized count per million population.

![Raw cases of coronavirus](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/raw-cases-map-a27e5881.png)
![Coronavirus normalized cases map](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/normalized-cases-map_0-66dd02f8.png)

Is the map of the raw number of cases more or less informative than the map of the normalized data? To be sure, the map of the raw counts is frightening and emphasizes the intensity of the pandemic, with so many countries shown in deeper shades of red. However, the map of the normalized data raises some different questions: Why does Russia have so many fewer cases relative to its population than do other Eurasian countries? (Population density?) What is different about Central America and Africa that they have fewer cases so far? (Weather?) Are there other questions we can generate from studying the mapped normalized data that could help us cope with this pandemic or prevent future ones? It’s not that one approach is right or wrong; both maps are useful. They each tell part of the story, and they each provoke interesting questions.

Alteryx co-founder Ned Harding also recently explored the challenge of mapping U.S. coronavirus cases effectively. He explains his thought process [in a blog post with examples created in Alteryx](https://inspiringingenuity.net/2020/03/24/a-tale-of-2-maps/), starting with an initial effort that displayed the cases per 100,000 of population in counties. Finding that less approach than ideal, he ultimately created a map with individual points for each case, mapped onto the states in which they occurred, plus animation to demonstrate the growth in cases — an element of the story that is hard to communicate with a static map.

With a complex issue like the pandemic, there are many options for displaying data, and each choice tells a slightly different side of the story. Similarly, in our everyday data visualization, we can consider what parts of a data story our charts and maps emphasize or omit. What is the key takeaway we want our audience to have? A better understanding of an overall problem versus just the numbers? A sense of the change over time versus the situation at a specific moment? What angle matters most to move the discussion forward?

##### **Keeping an Open Mind**

Whatever the topic of a data visualization, Cairo also emphasizes that we must approach it with an open mind as much as possible. “The more we cherish an idea, the more we’ll love any chart that corroborates it,” he writes. We all tend toward confirmation bias and rationalization, and we’ll interpret visualizations in ways that support our existing beliefs.

**As we move forward through — and, eventually, beyond — this pandemic, we’ll start to see new visualizations showing the end of the disease’s spread, and others for all kinds of issues that will be reimagined in the world that comes after.**

Charts and maps will be “conversation enablers” in that process, to use Cairo’s phrase. The more we can craft useful visualizations and encourage their careful use and interpretation, the better the conversations we can have, whether within a business or industry or in society more broadly.

#### STAY PUT.

[![Susan Sivek](/assets/images/posts/coronavirus-data-visualizations-how-charts-lie/sivek_headshot_500x500-a63814c3.webp)](https://www.alteryx.com/input/authors/susan-currie-sivek)

Susan Currie Sivek, Ph.D., is the Data Science Journalist for the Alteryx Community. She’s a writer and data geek who loves figuring out the best ways to share complex ideas. She spends her free time outdoors with her dog or indoors with a good book.