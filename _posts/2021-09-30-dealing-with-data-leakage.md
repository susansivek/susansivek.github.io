---
title: "Dealing with Data Leakage"
date: 2021-09-30
excerpt: "You’re studying for an upcoming exam. The exam is open-book, so you’re using your reference materials as you review, and you’re doing great. But when you show up on test day, suddenly you’re told the exam isn’t open-book anymore. It doesn’t go so…"
original_url: "https://community.alteryx.com/t5/Data-Science/Dealing-with-Data-Leakage/ba-p/827583"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Dealing-with-Data-Leakage/ba-p/827583](https://community.alteryx.com/t5/Data-Science/Dealing-with-Data-Leakage/ba-p/827583)*

You’re studying for an upcoming exam. The exam is open-book, so you’re using your reference materials as you review, and you’re doing great.

But when you show up on test day, suddenly you’re told the exam isn’t open-book anymore. It doesn’t go so well.

Image via GIPHY

This sounds like an academic overachiever’s anxiety dream, but it’s similar to what’s happening when target leakage occurs in a machine learning model. Say you build a model that’s intended to predict a certain outcome, and you train it with information that helps the model make its prediction. That model may perform well ... perhaps *suspiciously* well. But if some of that information won’t be available to the model at the actual time it has to make its prediction, its real performance will be lower. That’s the result of target leakage — a data scientist’s anxiety dream!

I recently heard one of our in-house Alteryx experts call target leakage the toughest problem in machine learning. But how does it happen, and how can you avoid this issue with your models? And how does it relate to “data leakage” more generally?

Image via GIPHY

## **Target Leakage**

Target leakage occurs when a model is trained with data that it will not have available at the time of prediction. The model does well when it is initially trained and tested, but when it’s put into production, the lack of that now-missing data causes the model to perform poorly. Just like you studying with your books, then taking the exam without them, the model is missing helpful information that improved its performance during training.

Here are some scenarios that represent target leakage:

* Including the outcome to be predicted as a feature in the dataset used to train the model (this may sound silly, but it could happen; for example, duplicating and renaming your target variable field, then forgetting about that duplication, could lead you to inadvertently use the extra version of the target as a predictor);
* Including a feature representing the number of years a student attended a college in a model predicting whether the student would accept an offer of admission to that college;
* Including a feature representing the number of months of a subscription in a model predicting whether a potential customer would subscribe or not;
* Including a feature representing whether a fire-related insurance claim was approved in a model predicting fires in homes with a certain type of siding; and
* Including information from other datasets that introduces details not otherwise available to the model at the time of prediction.

In all of these cases, information that can’t be known at the time of prediction was included when the model was built. We can’t know how many months a customer will subscribe when we are still trying to figure out if they’ll subscribe in the first place. (Can we build a model that could try to predict how many months a subscriber will subscribe? Sure. But we’d base that on our data about *known* subscribers, not the entire pool of those who may or may not subscribe.) Similarly, if we’ve told a model that people in homes built with certain materials have made fire insurance claims, we’re introducing knowledge from *after* the fires have occurred into our model trying to predict the fires.

Even seemingly innocent details like file size or timestamps can unintentionally be proxies for a target variable. For example, a 2013 Kaggle competition [had to be paused](https://www.kaggle.com/c/the-icml-2013-whale-challenge-right-whale-redux/discussion/4865#25839) and the dataset revamped because of this kind of issue. The team that discovered (and diligently reported) the leakage enjoyed a brief stint on the top of the leaderboard!

What results from data leakage is overfitting to your training data. Your model can be very good at predicting with that extra knowledge — excelling on the open-book exam — but not so good when that information isn’t provided at prediction time.

Image via GIPHY

## **Train-Test Contamination**

Another form of data leakage is sometimes called “train-test contamination.” This problem may not specifically involve your target variable, but it does affect model performance. It’s another way we might inadvertently add knowledge about future data into our training data, resulting in performance metrics that look better than they would in production. (By the way, if you look for more reading on this topic, be forewarned that “data leakage” is also a term sometimes used by cybersecurity folks to talk about [data breaches](https://en.wikipedia.org/wiki/Data_breach).)

A common way train-test contamination occurs is preprocessing your dataset in its entirety *before* splitting it into training and test sets or prior to using cross-validation.

For example, [normalizing data](https://community.alteryx.com/t5/Data-Science/Normalization-Standardization-and-Regularization-in-Alteryx-and/ba-p/733996) requires using the numerical range of each variable in the dataset. Normalizing the entire dataset as a whole provides that “knowledge” to the model when it’s evaluated. However, a model that is put into production won’t have that knowledge, and so won’t perform as well when it is used for prediction. Similarly, standardizing the full dataset would inappropriately inform the model about the mean and standard deviation of the entire dataset. [Imputing missing values](https://help.alteryx.com/20213/designer/imputation-tool) also uses summary statistics about your dataset (e.g., median, mean).

All of these clues can help the model perform better on your training and test data than it will when it is eventually introduced to brand-new data. [This article](https://machinelearningmastery.com/data-preparation-without-data-leakage/) provides an in-depth exploration of this kind of data leakage, including code to demonstrate.

Another issue can emerge if you’re using [k-fold cross-validation](https://community.alteryx.com/t5/Data-Science/Holdouts-and-Cross-Validation-Why-the-Data-Used-to-Evaluate-your/ba-p/448982) to evaluate your model. As long as your dataset includes only *one* observation from each individual person/source, this type of leakage should not be an issue for you. However, if you have multiple observations (i.e., rows of data) from each person or source in your dataset, all of those observations from the same source need to be grouped together when the subsets or “folds” of your data are created for training and testing the model.

For example, you may end up using training data from person A to predict an outcome for test data from person A, if observations from person A end up included in both the training group and the test group. The model will seem to perform better on the test set — which again includes person A — because it already knows something about person A from the training set. But in production, it won’t have that advantage of prior exposure. For more elaboration on this issue (sometimes called “group leakage”), check out [this article](https://machinelearningmastery.com/k-fold-cross-validation/).

Image via GIPHY

## **Repairing Data Leakage**

When a faucet drips in your house, you know it by the sound and puddles. But these types of leakage can be difficult to detect. There are still preventive maintenance and repairs you can do to address this challenge.

Unusually good model performance may be a sign of leakage. If your model is performing shockingly, remarkably well, resist the temptation to pat yourself on the back and ship it. That performance might be the result of garden-variety overfitting, but it may also be reflecting target or data leakage.

To try to stave off data leakage in the first place, you can do thorough [exploratory data analysis](https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267) (EDA) and look for features that have especially high correlations with your outcome variable. It’s worth looking closely at those relationships to ensure there isn’t the potential for leakage if the highly correlated features are used together in the model. This review can be challenging if you have a high-dimensional dataset with many features, so using a tool like the [Pearson Correlation Tool](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Pearson-Correlation/ta-p/388744) in Designer and filtering and/or visualizing its output could be helpful.

To avoid train-test contamination, be sure to split your data into training/test/holdout sets prior to applying any transformations such as normalization, then train the model on the training set. Follow up by applying the transformations to the test/holdout sets with the same parameters applied to the training set, then test your model’s performance.

Image via GIPHY

Additionally, be sure you fully understand all the features in your dataset. [This Kaggle example](https://www.kaggle.com/alexisbcook/data-leakage) shows how a feature named “expenditures” in a credit card application approval dataset could cause target leakage if used in a model to predict approved applications. “Expenditures” as a feature name could mean a lot of things, but in this case, it referred to how much credit card users spent on their cards. That feature implied that they were indeed approved for the cards and informed the model’s prediction of approvals inappropriately, since expenditure information would not be available at the time of prediction.

Finally, checking your features’ relative importance and reviewing other interpretability tools could help you catch leakage. In the credit card application approval example above, “expenditures” might have looked like a really important feature in a prediction of credit card approvals. If in doubt, you can try removing a feature to see how your model’s performance changes, and then determine whether the model suddenly performs at a more realistic level.

Image via GIPHY

## **Another Option: Assisted Modeling and AutoML**

If you’re reading this and thinking, *I don’t want to worry about all this* — well, we can’t remove the worry entirely, but be reassured that the Alteryx Intelligence Suite tools for Assisted Modeling and AutoML have some safeguards in place to help you identify features that may be duplicative of, or suspiciously highly correlated with, your target variable.

I tinkered with the housing price dataset (included in Designer under Help > Sample Datasets). Imagine we wanted to use that dataset, which includes details of houses’ square footage and characteristics, in a model to predict the “price” variable. Let’s say that “price” actually represented the house’s “most recent sale price” in the year 2019, and let’s add a pretend variable for “current asking price,” the price for which the house was listed in 2021 (created by adding 20% to the “price” variable).

If using this lightly fictionalized dataset to create a model to predict the 2019 sales prices, one might inadvertently include the 2021 data, causing target leakage. Predicting 2019 prices while using 2021 data would obviously be a temporal problem, giving the model anachronistic information it shouldn’t have.

Even though I knew this could be an issue, I asked Assisted Modeling to walk me step-by-step through building a regression model for the “most recent sales price,” and handed it the whole dataset.

At the feature selection step, sure enough, Assisted Modeling noticed that my “current asking price” variable was “too highly correlated” with my target variable, and it automatically eliminated that variable from inclusion in the models it built for me. Thanks for saving me from that target leakage, Assisted Modeling!

## **Leakproofing Your Models**

I hope this overview has provided you some new plumbing skills to help you avoid these leaky situations! With careful EDA and thorough knowledge of your dataset, as well as correct preprocessing and cross-validation setup, you should be able to keep your targets nicely contained and your datasets free from contamination.

***Do you still have questions? Which other tools or data science concepts would you like to see addressed here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***

## **Recommended Reading**