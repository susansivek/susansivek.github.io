---
title: "Repairing Broken Models (or Not) During a Pandemic"
date: 2020-04-29
excerpt: "With such immense disruption in so many systems, it’s hard to know what to do with your existing models. Here are some ways to adapt — and some reasons you might not try to repair those models. What do you do when you have an…"
original_url: "https://towardsdatascience.com/repairing-broken-models-or-not-during-a-pandemic-63ec1ade6897"
---

*Originally published at [https://towardsdatascience.com/repairing-broken-models-or-not-during-a-pandemic-63ec1ade6897](https://towardsdatascience.com/repairing-broken-models-or-not-during-a-pandemic-63ec1ade6897)*

![](https://miro.medium.com/max/640/1*CBQ2zhhryhNX4KN0ha360Q.jpeg)

With such immense disruption in so many systems, it’s hard to know what to do with your existing models. Here are some ways to adapt — and some reasons you might *not* try to repair those models.

Photo by [Jamie Street](https://unsplash.com/@jamie452?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/road-detour?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

What do you do when you have an amazing, even award-winning, model based on years of work that’s suddenly wrecked by a global pandemic?

Sound familiar?

Well, if you’re with the Delphi research group at Carnegie Mellon University, you pick yourself up and move on to think creatively about the next big problem.

In 2019, the Centers for Disease Control and Prevention (CDC) named the Delphi group a National Center of Excellence for Influenza Forecasting, following three years in which their forecasting systems won top spots for accuracy in the flu forecasting challenges created by the CDC. But in March, seeing that the influenza model would be dramatically affected by the COVID-19 pandemic, the CDC asked the researchers to turn their attention away from influenza and to try to forecast the spread of COVID-19 instead. The Delphi group has adapted in a variety of ways, including a reconsideration of “social anxiety” signals in their models and of their ability to forecast beyond a couple of weeks. (Read more about their adaptation [here](https://www.vox.com/future-perfect/2020/3/19/21185686/ai-predicting-coronavirus-spread-forecasting-covid-19) and [here](https://www.ml.cmu.edu/news/news-archive/2020/march/using-machine-learning-cdc-forecasting-flu-covid19-illness.html).)

Infectious disease models aren’t the only ones in need of re-invention right now. Anyone trying to generate predictions or forecasts for retail, supply chain, health care, education, or, well, pretty much any industry is faced with sudden, dramatic behavior in their data. Sometimes that’s in the positive direction: Folks in the video game industry, for example, are probably pretty pleased with [the record numbers](https://ew.com/gaming/coronavirus-videogames-industry-impact/) of users and gaming hours that they’re seeing right now. Sometimes, the changes in the data aren’t so positive.

So how do you rehabilitate a broken model to cope with these dramatic shifts? There have been some interesting discussions [on our Alteryx Community](https://community.alteryx.com/t5/Industry-Discussions/bd-p/industry-discussions) and [on social media](https://www.reddit.com/r/MachineLearning/comments/fqzwbo/d_how_are_you_all_thinking_about_demand_modeling/) about this challenge. Here I’ll discuss a few possible strategies that have emerged, each with its own complexities, plus one that should make us feel good about our human perspective on the world.

# Add New Model Features and Use Real-Time Data

One way to try to integrate the current situation into your models is to add features that try to account for the realities of the pandemic. Maybe this is a feature that captures the number of days a city has been under social distancing mandates, including school and business closures. Maybe it’s a feature for the percentage of a city’s population that is known to have contracted COVID-19 (acknowledging that these data are incomplete due to the inconsistencies of testing and unknown or asymptomatic cases). These could be tough to select, define, and keep updated, however, so they could be of negligible value; it is also difficult to validate their usefulness right now with the recency of these changes.

Another strategy is to get data that is as close to real-time as possible. That’s probably also easier said than done, of course. But imagine that one day soon, some inaccurate social media meme spreads that says a popular food cures COVID-19, and there’s a rush on that product. If you don’t know about that sudden popularity immediately, you won’t be able to maintain supplies. This is a time when having a repeatable, automated workflow is just invaluable to help you keep up with the speed of events.

# Adjust Forecasting Approaches

In many fields, forecasts generated for summer 2019 are not going to be super useful for the extremely different summer of 2020. For those working with time series data and forecasts, a method that weights more recent data more heavily in the forecast *might* be appropriate at the moment. If demand for a product has suddenly risen, for example, that recent increase won’t immediately disappear, but more likely will diminish gradually over time as consumer behavior slowly returns to normal.

For example, Prophet is a [free and publicly available forecasting package](https://facebook.github.io/prophet/) for either R or Python. [This post and Alteryx workflow](https://community.alteryx.com/t5/Data-Science-Blog/Expand-Your-Predictive-Palette-III-I-Sales-Forecast-with-Prophet/ba-p/504651) show an example of using the [Prophet](https://facebook.github.io/prophet/) forecasting tools and configuring trend [changepoints](https://facebook.github.io/prophet/docs/trend_changepoints.html) within Alteryx. Changepoints are defined as moments when the time series values suddenly change. Identifying these moments that have major impact on your data and incorporating them into your model would be critical. (Note that per the Prophet documentation, “By default changepoints are only inferred for the first 80% of the time series in order to have plenty of runway for projecting the trend forward and to avoid overfitting fluctuations at the end of the time series.” This behavior can be altered with `changepoint_range` in the original Prophet parameters, but if you use the above provided macro as it stands, without customizing it further, you’ll have to ensure that your changepoints are within that first 80% of your time series.)

Another possibility is to try to smooth time series data with a Kalman filter that could perhaps better deal with the peaks and valleys caused by the [“exogenous shock”](https://en.wikipedia.org/wiki/Shock_(economics)) of this major economic event. The `KFAS` package in R can be used for that purpose, as [this example](https://datascienceplus.com/kalman-filter-modelling-time-series-shocks-with-kfas-in-r/) shows. Even that approach might not be enough to accommodate such a dramatic turn of events, though.

# **Use Simulations**

Economic modelers sometimes use the V-U-L shapes of recessions and recovery to examine possibilities for the future. A [recent *Harvard Business Review* article](https://hbr.org/2020/03/what-coronavirus-could-mean-for-the-global-economy) showed how these models applied to the economy in past pandemics and could occur today. This is one way to imagine possible futures, even though thinking about that pessimistic “L” scenario is difficult.

*Visualizing V, U, and L recessions and recoveries, from left to right. Images from* [*Wikimedia*](https://en.wikipedia.org/wiki/Recession_shapes)

Those scenarios could offer a framework for developing simulations to model different possibilities. While simulations were for many years computationally expensive and daunting, that’s no longer the case. As [these researchers](https://drive.google.com/file/d/11Q5z0ea-gJ9Fy3SOAzbWC9zRMahI6ous/view) note:

… we now have (and can easily execute) effective statistical procedures that practically eliminate any gnawing uncertainty about our results’ precision; as real systems are, after all, mostly themselves stochastic, a simulation can capture that system variation in a realistic way, while still producing results that can be made as precise as desired.

The pandemic might be rather more extreme than most situations considered by these authors, but simulations might still have some utility, even if they can’t “eliminate” uncertainty.

Simulations can incorporate different assumptions about the effects of the pandemic on your situation, and then evaluate their different outcomes comparatively. The [Simulation Sampling Tool](https://help.alteryx.com/current/designer/simulation-sampling-tool) in Alteryx Designer can be used to sample or simulate data with a variety of methods. [Bootstrapping a time series](https://otexts.com/fpp2/bootstrap.html) — simulating multiple time series similar to your original data — can help account for greater uncertainty. Fitting a model to each of these series will generate different estimated parameters and random error terms. Combining the forecasts from these models will create larger prediction intervals and display a greater range of possible outcomes.

The utility of Monte Carlo simulations in this moment was also the topic of discussion for [a recent Reddit thread](https://www.reddit.com/r/datascience/comments/ftnuqe/using_monte_carlo_simulation_to_estimate/) on ways to address the pandemic’s challenge to forecasting, with respondents divided on their potential value, particularly because the Monte Carlo approach assumes uniformly distributed data. The `PyMC3` package offers a Python toolkit ([here’s a tutorial](https://docs.pymc.io/notebooks/getting_started.html)). R has many tools for simulation as well, including the package `MonteCarlo`, which has [a helpful vignette](https://cran.r-project.org/web/packages/MonteCarlo/vignettes/MonteCarlo-Vignette.html).

Whatever approach you attempt, forecasts are not going to be as helpful as they might normally be. It’s a good idea to [communicate plenty of uncertainty](https://community.alteryx.com/t5/Data-Science-Blog/A-Good-Honest-Chart-Coronavirus-Data-Visualizations-and-How/ba-p/547543) around your forecasts. Your audience needs to realize that those confidence intervals are even more important than usual.

# Choose Your Path Forward

Alas, there is no single solution to fix a once-prized, now-broken model, or to generate perfect predictions in such an uncertain time. But this moment demonstrates the importance of human intelligence and sensitivity — as well as domain expertise — in data analytics.

It might be the case that crafting every parameter of a new model is not the best use of your time and effort right now. There are so many unknowns right now that it may be more efficient to rely on informed, thoughtful human predictions.

This moment makes it even more obvious how critically important human input is in developing analytic strategies. Tools will misfire if they are just fed the same data and designed the same way they were in normal times. As Matissa Hollister, assistant professor of organizational behavior at McGill University, [wrote recently](https://www.weforum.org/agenda/2020/03/covid-19-crisis-artificial-intelligence-creativity/) on a World Economic Forum blog:

> *Humans can discern between places where algorithms are likely to fail and situations in which historical training data is likely still relevant to address critical and timely issues, at least until more current data becomes available. … Even though the particular nature of COVID-19 is unique and many of the fundamental rules of the labour market are not operating, it is still possible to identify valuable, although perhaps carefully circumscribed, avenues for applying AI tools.*

As Hollister suggests, there are still ways we can use our modeling skills, with caution. Many subtleties of this strange new time are unknown to even the best models. For example, there are undoubtedly changes right now not only in the kinds of food people are buying, but also in the specific places where they are buying it. Shopping at a tiny, less-busy neighborhood grocery store may be more appealing than mingling with the masses at the ginormous superstore on the highway. The relative appeal of those two settings to disease-fearing customers is difficult to quantify and incorporate into a model.

We may feel often like humans aren’t very good at understanding each other, but during this pandemic, we can recognize emotional and lifestyle nuances in data that models may miss. So while we can adjust our choices of data and our models’ design, it’s also a time to use human empathy and expertise to guide decisions and create solutions.

*This post was* [*originally published*](https://community.alteryx.com/t5/Data-Science-Blog/Repairing-Broken-Models-or-Not-During-a-Pandemic/ba-p/558570) *on the Alteryx Community Data Science Blog. Find more resources at the* [*Alteryx Data Science Portal*](http://alteryx.com/data-science)*.*