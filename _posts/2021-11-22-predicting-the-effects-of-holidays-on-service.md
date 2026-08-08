---
title: "Predicting the Effects of Holidays on Service"
date: 2021-11-22
excerpt: "While many of us happily feast and relax on Thanksgiving, others are out there doing what’s necessary to keep society operating on the holiday. Local government agencies, law enforcement and others still take in requests for help and try to fulfill…"
original_url: "https://community.alteryx.com/t5/Data-Science/Predicting-the-Effects-of-Holidays-on-Service/ba-p/847820"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Predicting-the-Effects-of-Holidays-on-Service/ba-p/847820](https://community.alteryx.com/t5/Data-Science/Predicting-the-Effects-of-Holidays-on-Service/ba-p/847820)*

While many of us happily feast and relax on Thanksgiving, others are out there doing what’s necessary to keep society operating on the holiday. Local government agencies, law enforcement and others still take in requests for help and try to fulfill them.

![SusanCS_0-1637255909455.gif](https://community.alteryx.com/t5/image/serverpage/image-id/211297i4FC42B41C1390D67/image-size/medium?v=v2&px=400)

Image via GIPHY

But could the holiday affect how long it takes to deal with a request from the public to address a problem? What determines whether a request can be completed and closed within, say, 24 hours? (Of course, needing quick turnaround and closure is relevant to many other areas, such as delivery times, customer service tickets, appointment wait times, and more.)

Let’s check out one way to model this sort of question. We’ll look at the New York City 311 call data — specifically, [a dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-during-Thanksgiving-Week-2020/nkbi-zvx2) reporting all the calls to 311 during Thanksgiving week in 2020. We’ll build a model to predict whether a specific service request would likely be closed within 24 hours or not. Being able to predict this would help those taking the requests provide realistic forecasts of how long issues may take to address, given the specifics of the case. Our modeling process will also let us know which factors matter most in closing cases in less than a day, including whether it’s Turkey Day or not.

![SusanCS_1-1637255909049.png](https://community.alteryx.com/t5/image/serverpage/image-id/211296iF375084DD3A23482/image-size/large?v=v2&px=999)

Word cloud of issues reported to NYC’s 311 service during Thanksgiving week of 2020. (Notice the top left … yikes! ?

*🐀)*

## **Prepping Our Model’s Ingredients**

The dataset from the City of New York website is pretty clean, with just a bit of the usual tidying necessary to get dates into the correct format, to make text lower case for consistency, and to create a couple of features: a calculation of the time elapsed between the creation and closure of a service request, plus a variable based on the date that simply marks whether the request was initiated on Thanksgiving Day or not.

Additionally, there were many values in the original data for “Complaint Type” (e.g., “loud party”, “rat sighting” 😱) and “Location Type” (e.g., “street,” “vacant lot”). The R-based predictive tools in Designer, however, only work with 50 or fewer values per categorical variable, so I identified the top 50 complaint and location types, and retained only the 311 calls that used those most common types. That still left me with 29,060 calls to analyze, from the original 36,846, and 4,060 of those happened on Thanksgiving Day.

An impressive 19,118 of the calls were resolved within 24 hours, and 15,701 of them were referred to the New York Police Department for handling, with others directed to other city agencies, such as the Department of Sanitation and the Department of Parks and Recreation.

![SusanCS_2-1637255910504.gif](https://community.alteryx.com/t5/image/serverpage/image-id/211298iFE8518322EC6FC7B/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Cooking up a Model, Part 1: Alteryx Machine Learning**

We need a binary classification model to predict whether each case was resolved within 24 hours or not. The predictors were the agency name (that handled the issue), the complaint type, the location type, the borough, the method used for contacting 311 (e.g., phone, online), and whether the service request occurred on Thanksgiving Day itself or another day during the holiday week.

We can use [Alteryx Machine Learning](https://help.alteryx.com/machine-learning) to quickly move through the modeling process. It’ll make the most of this dataset with feature typing options, and will also rapidly build and evaluate multiple models, with minimal effort on our part.

![SusanCS_3-1637255910397.gif](https://community.alteryx.com/t5/image/serverpage/image-id/211301i29DB7359CFBE8AE2/image-size/medium?v=v2&px=400)

Image via GIPHY

The first step is, as usual, to import your data and prep it. At that point, you can make sure the data type is set correctly for each feature, drop features you don’t want, and check out the overall health of your dataset (i.e., its readiness for modeling).

A cool thing to notice at this stage is that you can be a little more detailed about your data types than you may be accustomed to in Alteryx Designer. For example, I could tell Alteryx Machine Learning that it should evaluate the “ZIP Codes” column as the type “Postal Codes.” (That’s because it’s [drawing on](https://woodwork.alteryx.com/en/stable/guides/logical_types_and_semantic_tags.html#PostalCode) [Woodwork](http://github.com/alteryx/woodwork), one of the Alteryx Open Source libraries, which handles data typing.)

In the next step, you’ll set your target variable, determining the general type of model you need (classification or regression). A quick pass through the dataset then reveals some essential details about your features, including correlations among them, outlier values and the distribution of labels for your target variable.

![SusanCS_0-1637256184335.png](https://community.alteryx.com/t5/image/serverpage/image-id/211304iB989CDE7DDE2CA09/image-size/large?v=v2&px=999)

*The correlation matrix for the variables in the dataset*

![SusanCS_5-1637255909114.png](https://community.alteryx.com/t5/image/serverpage/image-id/211299iDC6DF1CCCE7A87B2/image-size/large?v=v2&px=999)

The distribution of the yes/no values for our target variable (whether the request was closed in 24 hours or less)

This tool is built with methods for [handling imbalanced datasets](https://community.alteryx.com/t5/Data-Science/Balancing-Act-Classification-with-Imbalanced-Data/ba-p/841878), so you don’t need to worry if you have a lot more of a particular label for your outcome.

Alteryx Machine Learning will build a bunch of models in the Auto Model step, using various algorithms and hyperparameters, then provide you with its rundown of options to choose among — plus a recommendation.

The next step, Evaluate Model, is probably the most intriguing! You can see how well your selected model performs on various metrics, review a confusion matrix and your features’ relative importance, simulate the results of modified data, and even check out a sampling of good and bad predictions made by the model so you can better understand what it’s doing behind the scenes.

![SusanCS_1-1637256235381.png](https://community.alteryx.com/t5/image/serverpage/image-id/211305i0604B7447360883A/image-size/medium?v=v2&px=400)

Many metrics to examine for the recommended model

![SusanCS_2-1637256291030.png](https://community.alteryx.com/t5/image/serverpage/image-id/211306iDF668D7226E61B72/image-size/large?v=v2&px=999)

*Confusion matrix for the recommended model*

![SusanCS_3-1637256331750.png](https://community.alteryx.com/t5/image/serverpage/image-id/211307i0D16A3EA6C52C7C4/image-size/large?v=v2&px=999)

Prediction explanations for best and worst predictions offered by the model

There’s a lot to peruse in that step of the process. Once you’re happy with the model, you can upload new data upon which the model can generate new predictions, export the visuals displayed in the modeling process as images or PowerPoint slides, and export the model to use in a Designer workflow.

## **Cooking up a Model, Part 2: Alteryx Designer**

If you don’t have Alteryx Machine Learning, don’t worry — we can still get this holiday party started with our longtime friends, the R-based predictive tools. I used these tools to build both a logistic regression model and a random forest model in Designer. (Follow along with the attached workflow!)

The random forest model had a 93.4% accuracy rate, and performed about the same when predicting both positive and negative outcomes, as the confusion matrix below shows.

![SusanCS_4-1637256374462.png](https://community.alteryx.com/t5/image/serverpage/image-id/211308iB65714FD92773D60/image-size/large?v=v2&px=999)

Confusion matrix for the random forest model in Designer

The logistic regression model did almost as well, with 93.2% accuracy; however, its mistakes weren’t as evenly distributed.

![SusanCS_0-1637256792230.png](https://community.alteryx.com/t5/image/serverpage/image-id/211313i9AF8604F10E5C0AE/image-size/large?v=v2&px=999)

*Metrics for the logistic regression model built in Designer*

So let’s look more closely at the random forest model, and especially check out how the various features contributed to the predictions. The variable importance plot below tells us more:

![SusanCS_1-1637256835700.png](https://community.alteryx.com/t5/image/serverpage/image-id/211314i5374BF210B3808C3/image-size/large?v=v2&px=999)

*Variable importance plot for random forest model built in Designer*

The random forest classifier built in Designer performs similarly to the XGBoost classifier built by Alteryx Machine Learning. Both tools get the modeling job done, but with different interfaces and explanatory information available along the way.

If we were concerned about whether a request coming in on Thanksgiving would affect whether that request could be resolved during 24 hours … well, it turns out that was the least significant factor in predicting that outcome. Instead, the type of complaint, location and agency were notably more important in the model’s predictions.

![SusanCS_2-1637256890029.gif](https://community.alteryx.com/t5/image/serverpage/image-id/211315iF92C47C2A8E85C24/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Dessert: Predictions and More**

The modeling process helped us gain more insight into how the holiday could affect service request closure time (or not, in this case, since the “On Thanksgiving” feature turned out to be not very important compared to other features used in these models). We could also use our favorite model in the future to predict whether a service request with a particular set of characteristics would or would not be completed and closed within 24 hours. That information could help guide a customer’s expectations and shape response processes.

***Do you still have questions? Which other tools or data science concepts would you like to see addressed here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***