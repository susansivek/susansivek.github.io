---
title: "Back to the Future: ARIMA and Forecasting with Covariates"
date: 2020-09-03
excerpt: "Crafting a reliable forecast of a phenomenon feels like having a very specialized crystal ball on your desk that can answer critical questions. Time series analysis and forecasting are powerful methods of understanding how something has changed over…"
original_url: "https://community.alteryx.com/t5/Data-Science/Back-to-the-Future-ARIMA-and-Forecasting-with-Covariates/bc-p/628887"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Back-to-the-Future-ARIMA-and-Forecasting-with-Covariates/bc-p/628887](https://community.alteryx.com/t5/Data-Science/Back-to-the-Future-ARIMA-and-Forecasting-with-Covariates/bc-p/628887)*

Crafting a reliable forecast of a phenomenon feels like having a very specialized crystal ball on your desk that can answer critical questions. Time series analysis and forecasting are powerful methods of understanding how something has changed over time and how it may occur in the future.

If you’ve been curious about using time series methods, our Academy team has just released a terrific new set of [interactive lessons](https://community.alteryx.com/t5/Interactive-Lessons/tkb-p/interactive-lessons/label-name/Time%20Series%20Forecasting) in the [Data Science Learning Path](https://community.alteryx.com/t5/Learning-Paths/Data-Science-Learning-Path/ta-p/504157) to guide you toward skillful time series analysis.

After you’ve reviewed those excellent resources — or if time series analysis is already a familiar tool — let’s dive a little deeper into one aspect of time series that can sometimes mystify: the utility and selection of covariate time series.

When you build a time series model with the [ARIMA tool](https://help.alteryx.com/current/designer/arima-tool) in Designer, you’re offered a little checkbox that allows you to add *covariates* to the time series model. *Covariate* *time series* are separate series that help explain your primary time series of interest. But when Designer shows you all the other variables in your data as options, which ones should you choose?

Let’s explore criteria for good covariate time series to include in your model and forecasts, and how you might think about their role in your analysis.

## **Choosing Your Covariates**

Consider a time series situation like the one provided in the Designer sample workflow for time series forecasting (Help>Sample Workflows>Predictive tool samples>Predictive Analytics>15 Time\_Series\_Forecasting\_Sample), which demonstrates how to forecast room bookings at a mountain lodge using 10 years of monthly data. The original time series is simple. It covers 120 months, each with a single number representing the number of bookings for that month.

Now we’ll use our imaginations: It’s not just a mountain lodge, but a *ski* lodge … on a snowy mountain, with roaring fires in stone fireplaces, hot chocolate, and all the requisite accoutrements. Which phenomena could coincide with bookings at a ski lodge?

I’m no skier, but I’m thinking *snow* could be important! Could high amounts of snow correlate with the number of people wanting to go to a ski lodge? I mean, I’d go just to drink hot chocolate and read a novel by one of those fireplaces, but snow is the main attraction for most folks.

We’ll think about “bookings” as our *response variable* here, and “snow” as a *predictor* variable. We need to evaluate the snow and bookings relationship, though. Importantly, a series of snow measurements would be *external* to the system that created your primary time series of interest, the lodge bookings. It’s hard for humans to affect the quantity of natural snow (setting aside our impact on climate change for the moment). Certainly the number of lodge bookings does not affect the amount of snow. But the snow quantity *could* perhaps affect whether people want to stay at the lodge.

Side note: What if your model’s “outputs” (response variables) *do* affect the “inputs” (predictor variables)? Ideally, you’d use a more complex modeling approach with multiple equations. These kinds of analyses are typically projects for econometrician-type experts who are used to analyzing complicated systems with theory and models.

But back to our simpler situation: Given all these considerations, a time series of snow quantities could be a useful covariate series for our ski lodge booking time series. We would include the snow time series as a covariate in our ARIMA model. We’d want to be sure to structure our snow series in the same way that the bookings series is structured. If we have monthly totals for bookings, we should have monthly snow amount data in the snow series.

Moreover, any covariate series you use should be correlated with the noise -- the unexplained variation -- that remains in your original time series model, without the covariate. That correlation means that the covariate series helps to explain some of that remaining variation and adds information to the model, as well as accuracy to the forecast.

Finally, note that categorical variable time series can be used as covariate series in your model and forecast. They will be [one-hot encoded](https://community.alteryx.com/t5/Data-Science/One-Hot-Encoding-What-s-It-All-About/ba-p/578652) by Designer so that they take a numerical form in the analysis.

Keeping these guidelines about covariate selection and series structure in mind, we can choose variables we want to include as covariates within our ARIMA model in the configuration options.

## **Adding a Covariate to a Forecast**

If you want to create a forecast using an ARIMA model that includes a covariate, you’ll need to use the [TS Covariate Forecast](https://help.alteryx.com/current/designer/ts-covariate-forecast-tool) tool. To do that, you’ll need future values of the covariate series for every time period you wish to forecast. In our example here, to generate a yearlong forecast of monthly lodge bookings, you’ll need to include monthly snow data for each month in the year to be forecast.

Yes. You need future values. I know, right?! Getting information from the future is not easy, or at least that’s what science fiction tells me.

In a perfect world, you would know what’s going to happen in the future with regard to your covariate predictor variable. For example, the availability of a certain component for manufacturing may be known for the next year. In many situations, though, data about the future will itself need to be forecasted. For example, economic forecasts may be offered by government agencies (such as [U.S. housing forecasts](http://www.freddiemac.com/research/forecast/20200616_quarterly_forecast_economy_recovering.page?) from Freddie Mac). Specialized forecasts may be offered by private firms focused on different industries.

However, these forecasts need to: 1) cover the time span you want to forecast in its entirety; 2) be structured in the same time increments in which you want your forecast, and in which you have your original data; and 3) be reasonably accurate. As you can imagine, these may be difficult criteria to satisfy in some circumstances. As described in Chatfield and Xing’s time series text (details below), “a multivariate model is only able to give ‘good’ forecasts when forecasts of explanatory variables can be made (much) more accurately than those of the response variable.”

## **Leading or Lagging?**

The concept of leading and lagging indicators is important for understanding covariate time series as well. A *leading indicator* is a predictor variable whose change precedes change in your response variable. For example, increased demand for residential building permits in a specific area (the predictor) might occur prior to increased demand for space in nearby schools (the response). More homes being built for families would “indicate” that more students will soon need to go to a nearby school.

Identifying a leading indicator that reliably relates to your desired response variable could be valuable, though it can be difficult to know the right way to use it. For example, the time gap between the leading indicator and the response of interest may not occur consistently. For example, sometimes the effect of the leading indicator may be visible in a month, but at other times, it may take two months.

A *lagging indicator* is a measure that is not known until an action is taken. For example, in a human resources scenario, there would be a “time lag” or gap between employees becoming dissatisfied with their jobs and their eventual resignations. The resignations indicate dissatisfaction -- though they arrive a little too late to make changes.

## **Past, Present, and Future**

For our ski lodge bookings forecast, here’s one possible approach. We could construct an ARIMA model using a primary series of historical monthly bookings and a covariate series of snow data by the month. If that model performed well and we then wanted to create a forecast using it for the next year, we could use a long-term weather forecast [like this one for the U.S.](https://www.cpc.ncep.noaa.gov/products/predictions/long_range/two_class.php) to construct a series to use with the TS Covariate Forecast tool. The forecasted snow time series would need to have the same field name as our historical snow time series used as a covariate to build the original ARIMA model. It also needs to be ordered such that the soonest forecast period is listed first in the series, with the most distant forecast period at the end of the series. Once you’ve set up the forecasted series correctly and configured the TS Covariate Forecast tool, you’ll find that the tool’s output looks just like a regular TS Forecast output.

The big question, of course, is whether that forecasted snow data will be accurate enough to add real value to our bookings forecast or not. With apologies to meteorologists, do you fully trust weather forecasts for 10 days from now, much less 12 months from now? For some low-risk situations, maybe you can be comfortable with these layers of uncertainty; for other situations, not so much.

Time series analysis and forecasting are both art and science. As you can tell, there are many ways to customize your models and forecasting approach, depending on the situation. With careful judgment and attention to these details, though, you can maximize your model’s potential to be informative about the past and the future.

## Recommended reading:

* *The Analysis of Time Series: An Introduction with R* (7th ed.), Chris Chatfield and Haipeng Xing
* *Practical Time Series Analysis: Prediction with Statistics and Machine Learning*, Aileen Nielsen