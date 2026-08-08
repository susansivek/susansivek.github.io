---
title: "Free Data Science Tools for Designer: A Gallery Tour"
date: 2020-11-24
excerpt: "\"Did you know there are even more data science tools available for Alteryx, beyond what you see in your Designer palettes, for statistics, data prep, modeling and more?"
original_url: "https://community.alteryx.com/t5/Data-Science/Free-Data-Science-Tools-for-Designer-A-Gallery-Tour/ba-p/669590"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Free-Data-Science-Tools-for-Designer-A-Gallery-Tour/ba-p/669590](https://community.alteryx.com/t5/Data-Science/Free-Data-Science-Tools-for-Designer-A-Gallery-Tour/ba-p/669590)*

Did you know there are even more data science tools available for Alteryx, beyond what you see in your Designer palettes, for statistics, data prep, modeling and more?

Image via GIPHY

In [this week’s episode](https://community.alteryx.com/t5/Alter-Everything-Podcast/75-Fun-analytics-for-all/ba-p/670517) of our Alter Everything podcast, Chris [@mceleavey](https://community.alteryx.com/t5/user/viewprofilepage/user-id/3589) talks about building his own Alteryx tools. One of Chris’s projects is especially helpful for many modeling tasks: a [one-hot encoding tool](https://gallery.alteryx.com/#!app/One-Hot-Encoder/5b100277826fd31ed0054c28) that handles that pesky but important step. (He also wrote a [blog post](https://community.alteryx.com/t5/Data-Science/One-Hot-Encoding-What-s-It-All-About/ba-p/578652) about one-hot encoding!)

Alongside Chris’s work, there are many more useful tools for data science in the [Alteryx Analytics Gallery](https://gallery.alteryx.com/), our public repository of workflows, macros and analytic apps. Many of these tools reside in the [Predictive District](https://gallery.alteryx.com/#!districts/56327e37aa690a17f0760bdc), but we scrounged up more from other corners of the Gallery.

Image via GIPHY

Here’s a list of freely available macros, tools and sample workflows for data science tasks that might save you time and effort, plus a bonus package of tools developed by Alteryx enthusiasts.

## **Data Preparation and Statistics**

+ Use for [Box-Cox transformation](https://towardsdatascience.com/box-cox-transformation-explained-51d745e34203), which transforms a variable with a non-normal distribution so that it has a normal distribution

+ Allows you to group records by one field prior to calculating Pearson correlations

Image via GIPHY

## **More Modeling Options**

+ Creator: Alteryx Solutions
+ Features sample workflows for essential prediction tasks, including linear and logistic regression and A/B testing

+ Creator: Alteryx Innovation
+ Offers another clustering method using the [Partitioning Around Medoids (PAM) algorithm](https://www.geeksforgeeks.org/ml-k-medoids-clustering-with-example/), which may handle noisy data better; check out the [K-Medoids Sample](https://gallery.alteryx.com/#!app/K-Medoids-Sample/5d9267048a933711e4473920) once you have the macro for a demonstration

+ Creator: Alteryx Innovation
+ Provides macro and example for another method of [market basket analysis](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/ba-p/661963) using alternative measures of affinity, such as cosine similarity ([documentation](https://help.alteryx.com/current/designer/mb-affinity-tool))

+ Creator: Alteryx Innovation
+ Carries out [survival analysis](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_survival/BS704_Survival_print.html) ([documentation](https://help.alteryx.com/current/designer/survival-analysis-tool)) and generates relative risk and survival time when used with the [Survival Score](https://gallery.alteryx.com/#!app/Survival-Score/5d926a18826fd30b84537864) macro; see them at work in the [sample workflow](https://gallery.alteryx.com/#!app/Survival-Analysis-Sample/5d926a750462d7065c3fd8e2)

+ Creator: Alteryx Innovation

Image via GIPHY

## **Evaluating and Understanding Models**

+ Creator: Alteryx Innovation
+ Performs [cross-validation](https://community.alteryx.com/t5/Data-Science/Holdouts-and-Cross-Validation-Why-the-Data-Used-to-Evaluate-your/ba-p/448982) to compare and evaluate models. Note: Download the .yxi file linked in the description; you’ll need admin privileges to install this new tool. Once the tool is installed, try out the [sample workflow](https://gallery.alteryx.com/#!app/Cross-Validation-Sample/5d92687a8a933711e4473976) to see how to use the tool in a workflow with various models.

+ [Scales features](https://en.wikipedia.org/wiki/Feature_scaling) so their values are between 0 and 1, a necessary step for some algorithms; can also back-transform values

+ Creator: Alteryx Innovation
+ Provides an approach to [feature selection](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/) based on feature importance

+ Creator: Alteryx Innovation
+ Generates a report providing the [variance inflation factors](https://online.stat.psu.edu/stat462/node/180/) for variables in a model to help assess multicollinearity; see it in a [sample workflow](https://gallery.alteryx.com/#!app/Variance-Inflation-Factors-Sample/5d926b68826fd30b845378ae)

+ Creator: Alteryx Innovation
+ Outputs the model coefficient names and values from count, gamma, linear, or logistic regression models

+ Creator: Alteryx Innovation
+ Compares how models perform on a test set, and provides error measures and prediction results for each model, as shown in the [sample workflow](https://gallery.alteryx.com/#!app/Model-Comparison-Sample/5d9274848a933711e4473bad)

Image via GIPHY

## **For Time Series Analysis Fans**

+ Creator: Alteryx Products
+ Creates ARIMA or ETS time series models for multiple groups simultaneously ([documentation](https://help.alteryx.com/current/designer/ts-model-factory-tool))

+ Creator: Alteryx Products
+ Generates forecasts from groups of time series models (ARIMA or ETS) for your specified number of future periods ([documentation](https://help.alteryx.com/current/designer/ts-forecast-factory-tool))

+ Divides a time series dataset sorted chronologically to create training and test sets and visualizations

And a bonus item: The [ayx-builders pack on Github](https://github.com/ayx-builders), created by @nick612haylund and @tlarsen7572, offers multiple handy tools for data science tasks, including a data generator and a Twitter scraping tool.

With these free tools, you can extend the data science capabilities of Designer and finish projects more easily and efficiently.

And, of course, be sure to listen to the Alter Everything conversation with Chris for inspiration, then share your own custom creations.