---
title: "Metric Matters, Part 2: Evaluating Regression Models"
date: 2021-03-02
excerpt: "Welcome to part 2 of our discussion of metrics for evaluating your machine learning models! If you missed part 1 and would like a general intro to the meaning of “metrics,” plus a deep dive into the metrics often used for classification models, be…"
original_url: "https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-2-Evaluating-Regression-Models/ba-p/722596"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-2-Evaluating-Regression-Models/ba-p/722596](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-2-Evaluating-Regression-Models/ba-p/722596)*

Welcome to part 2 of our discussion of metrics for evaluating your machine learning models! If you missed part 1 and would like a general intro to the meaning of “metrics,” plus a deep dive into the metrics often used for classification models, be sure to [check out that post](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-1-Evaluating-Classification-Models/ba-p/719190).

In this post, we’ll refresh our knowledge of regression before reviewing some options for metrics used with regression models. Whether you’re feeling determined, absolute or maximum, there’s a metric for your particular regression needs.

## **Regression, Residuals and Error**

As mentioned in part 1, regression models use a different set of metrics from classification models because what you’re trying to predict is a numeric value, not one of a predetermined set of outcomes or classes. Instead of predicting something like “high” or “low,” you’re seeking to predict “1,390,000” or “15.” (Here’s a refresher on [linear regression](https://community.alteryx.com/t5/Data-Science/Simply-Powerful-Solving-Nonprofits-Data-Challenges-with-Linear/ba-p/565913) for the basics of that approach. [Random forest](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Forest-Model/ta-p/305724) and [decision tree](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Decision-Tree/ta-p/144452) models can also be used for regression, among other options.)

Image via GIPHY

With regression, we build models to make predictions that are as close as possible to the observed outcome values we have on hand in our dataset — for example, the selling prices for houses. Our model suggests a specific mathematical relationship between the predictor variables we choose and the observed outcome values.

When we compare our model’s predicted house prices to the observed house prices, we are calculating what’s called residuals, the differences between predictions and the observed values. The term “error” is also often used to refer to those differences. (There is a statistical distinction between “residual” and “error,” but to avoid the semantic weeds, I’ll refer you to [these](https://community.alteryx.com/t5/Data-Science/Alteryx-Data-Science-Design-Patterns-Predictive-Model-Form-Part/ba-p/38323) [explanations](https://en.wikipedia.org/wiki/Errors_and_residuals#Regressions); you’ll see both terms used in this post.)

For example, if we’re trying to predict houses’ selling prices, and we have a dataset showing that a house sold for $200,000 but our model predicts a sales price of $180,000, the residual is $20,000. Our model will be more useful if we can reduce that difference between the observed and predicted prices — and not just for this house, but across all the houses in our dataset.

We have different options for summarizing a model’s error across all its predictions. That’s where things can get a little fuzzy, because there are a lot of different approaches. As in our discussion of classification metrics, you have to decide which strategy works best for your particular situation: your data, your preferred kind of prediction error, and your need for [explainability](https://community.alteryx.com/t5/Data-Science/Interpretability-Explainability-and-Machine-Learning/ba-p/630765).

Let’s walk through the different options for metrics you can use in evaluating your regression model. (There are still more, but we’ll just look at the choices offered for the optional customization of the objective function in [the AutoML tool](https://community.alteryx.com/t5/Analytics/Power-to-the-Process-in-2021-1/ba-p/713080), as in part 1 of this post.)

Image via GIPHY

First we’ll check out some different ways of looking at your model’s blunders — specifically, the gaps between its predictions and our observed values. Let’s make up a dataset for the cost of holiday gifts. We’ll assume there were some other features used for prediction here, but to keep it simple, let’s just look at the actual cost, your model’s predicted cost, and the error.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Gift ID** | **Actual** | **Predicted** | **Error** | **Squared error** |
| Mean absolute error: $36.67 | Mean squared error: 1633.33 |

## **Mean (or median) absolute error**

*Definition:* the average (or median) of the [absolute value](https://davenport.libguides.com/math-skills-overview/absolute-value) of the error for all your model’s predictions. Values range from 0 to infinity, and lower values reflect a better-performing model. The mean absolute error for our tiny dataset above is $37; the median absolute error is $30.

*Important to know:*

* This metric is calculated across all of your model’s predictions.
* Using the absolute value here means positive and negative errors are treated the same way. It doesn’t matter for this metric if your model makes errors above or below the true values, but that may matter to you, so that’s something to consider about this metric.
* The MAE is in the same units as your original outcome variable, which can make it easier to understand and explain to others. In other words, if you’re trying to predict a price in dollars, you can easily think about the MAE as showing how much the predictions deviate from reality in dollars.

Image via GIPHY

## **Mean squared error (MSE)**

*Definition:* the squared values of all the errors, averaged. Values range from 0 to infinity, and lower values reflect a better-performing model. The MSE for our tiny dataset is 1633.33.

*Important to know:*

* The MSE tends to penalize large errors harshly. What does that mean? Our tiny dataset above shows one substantial error in the prediction of Gift 2, where our model was $60 away from the real price. What if all the errors were more consistent in size, but still the same amount in total?
* Check out a different version of our predictions below. The absolute value of the total error in the predictions is the same as in the above predictions ($110). The mean absolute error is the same. However, the MSE is notably lower at 1366.67. All that’s changed is that the model’s error is now more evenly distributed across its predictions, instead of concentrated in that one very wrong prediction.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Gift ID | Actual | Predicted | Error | Squared error |
| Mean absolute error: $36.67 | Mean squared error: 1366.67 |

* This tendency to penalize large errors harshly may make MSE a good metric for you to choose if you are concerned about your model making big (if maybe infrequent) mistakes. If big mistakes in prediction could be especially problematic or costly for you, MSE will help you compare models and see which one better avoids those large errors. However, maybe a generally good model that only freaks out on rare occasions is acceptable for your purposes.
* This penalty for large errors may be an issue for datasets with outliers, so if your data are noisy with some unusual values here and there, you might consider using a different metric or contending with the outliers prior to modeling. The [Data Health tool](https://help.alteryx.com/current/designer/data-health) can help you identify and deal with outliers.

## **Maximum residual error**

*Definition:* this is your worst-case-scenario metric. Out of all the predictions your model makes, what is the absolute value of its largest mistake? If your model is perfectly fitted (which is unlikely), the maximum residual error will be 0 because every prediction matched the true outcome value. Values begin at 0 and can range up to the largest absolute value of the outcome variable in your data.

*Important to know:*

* This metric differs from MSE in that it will be in the same units as your original data, and so it may be more explainable. It also differs from the above error calculations because it doesn’t try to summarize all the errors across all the predictions in one value; instead, it represents the model’s *single* biggest error in prediction.
* If you are concerned that your model’s biggest prediction error or “worst case” is below a certain threshold, this could be a useful metric to evaluate.

Our last two metrics assess how well your model and its chosen set of predictors can account for the variation in the outcome variable’s values.

## **Coefficient of determination (R****2****)**

*Definition:* Represents the proportion of the [variance](https://community.alteryx.com/t5/Data-Science/Bias-Versus-Variance/ba-p/351862) in the outcome variable that the model and its predictor variables are accounting for. Values typically range from 0 to 1, with higher values showing that the model is a better fit.

*Important to know:*

* Despite having “determination” in the name, R2 can’t show a causal relationship between your predictor and outcome variables.
* Adding more predictor variables to your regression model will increase the value of R2, but also creates a more complex model and can lead to overfitting. For this reason, [adjusted R2](https://www.statisticshowto.com/adjusted-r2/) is often preferred to R2 because it takes into account the number of predictor variables used and the sample size.
* For a lot more detail on how to use and interpret R2, check out [this reference](https://people.duke.edu/~rnau/rsquared.htm).

## **Explained variance score**

*Definition:* This is very similar to R2, representing the proportion of variance in the outcome variable explained by your model — but there’s a twist. Explained variance also incorporates the mean error in its calculation, which will account for skew in your model’s residuals (i.e., whether its results tend to bias in a consistent way).

*Important to know:*

* Here again, even though “explained” is in the metric’s name, this metric doesn’t say anything about an actual explanation for the outcome variable, in the sense of establishing a causal relationship.
* This metric and R2 may be equivalent if your mean error is 0, which is true for ordinary least squares (OLS) linear regression. If your data aren’t linear, though, the values will differ. The linearity (or nonlinearity) of your data then may determine whether you want to use this metric instead of R2. Exploratory data analysis may help you here, too.

Image via GIPHY

You’re now equipped to review metrics for both classification and regression problems! The choice of which metrics to evaluate isn’t easy, but it’s cool to be able to decide what you want to prioritize for the unique goals and applications of your model.

## **Additional Resources**