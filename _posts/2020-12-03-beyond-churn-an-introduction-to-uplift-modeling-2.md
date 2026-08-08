---
title: "Beyond Churn: An Introduction to Uplift Modeling"
date: 2020-12-03
excerpt: "\"Knowing which customers might churn is helpful, but uplift modeling can give you a new window into the nuances of customers’ responses, among other applications."
original_url: "https://towardsdatascience.com/beyond-churn-an-introduction-to-uplift-modeling-d1d9af7be"
publication: "Towards Data Science"
categories: [data-science]
---
*Originally published at [https://towardsdatascience.com/beyond-churn-an-introduction-to-uplift-modeling-d1d9af7be](https://towardsdatascience.com/beyond-churn-an-introduction-to-uplift-modeling-d1d9af7be)*

## Knowing which customers might churn is helpful, but uplift modeling can give you a new window into the nuances of customers’ responses, among other applications.

![](https://miro.medium.com/max/10000/1*8w7z1-2vby1qmil5VrfqXg.jpeg?q=20000000)

*Photo by* [*James Zwadlo*](https://unsplash.com/@jzwadlo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/lift?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

You may have heard of modeling techniques to predict the probability of churn for a customer, or to assess whether a customer will or won’t respond to an offer. But what about figuring out which customers might increase their purchasing — or could stop buying — as the result of a promotion?

Often we focus predictive analytics on modeling customer churn or a response to an offer (perhaps using logistic regression, as demonstrated in [this excellent blog post](https://innovation.alteryx.com/modeling-churn/)). Uplift modeling takes a different tack. This technique is often used to identify the customers most likely to respond and act upon receiving a “treatment,” such as a promotional email.

Uplift modeling can supplement experimental data from A/B testing by identifying the incremental impact on particular individuals of a specific treatment, as opposed to the overall lift or decrease caused by a treatment. This technique may help you assess whether other attributes of those individuals (e.g., demographic characteristics) could help explain their response. This nuanced analysis allows for future targeting only of those most likely to respond positively to a treatment.

Although [retail and marketing](https://www.hbs.edu/faculty/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf) are the best-known uses for uplift modeling, this approach is also used in fundraising, clinical trials, medical treatment, human resources, and even [political campaigns](https://searchbusinessanalytics.techtarget.com/video/How-uplift-modeling-helped-Obamas-campaign-and-can-aid-marketers) who seek to find those who can be persuaded by the right intervention or “treatment” at the right time.

![](https://miro.medium.com/max/10000/0*96EoEE89nvy_xI1J?q=20000000)

*Image via* [*GIPHY*](https://giphy.com/gifs/CBSAllAccess-star-trek-cbs-all-access-picard-dw3jr2nVMHBZ97LLF7)

# Who Should We Target?

Odds are, you subscribe to something: a magazine, a digital service, a “bagel of the month” club. (Yes, that’s a real thing.) If you got an email today informing you that you could upgrade that subscription to a premium version, how would you react?

Maybe you’d be excited to upgrade and would seize the opportunity. Maybe you’d realize upon seeing the email that you tired of bagels, so you’d head over to the website to cancel — not the response the email sender wanted! Or maybe you’d do nothing at all.

![](https://miro.medium.com/max/10000/1*v02JXhTfvZK46JT2bnof3g.png?q=20000000)

Image by author

This is a dilemma for the person sending the email. They hoped the recipients would choose to upgrade, and without sending out the notifications, that might not happen at all. Sure, some passionate customers might happen to stop by the bagel club website and spot the upgrade opportunity. Those fans would have upgraded without the email. By sending the email to all subscribers, the club unfortunately also lost some business.

The bagel club truly benefited only from sending the email to the people who *needed* to receive the email to take action and upgrade. In a perfect world, promotion emails could go *only* to those subscribers, maximizing the resulting upgrades and minimizing the risk of cancellations.

To generalize from our bagel example, here’s how this typology is usually described in discussions of uplift modeling. We’ll use the term “treatment” to refer to all the different situations in which you might use this approach: to send the promotional email or not, to offer a new recruit a signing bonus or not, to provide additional educational support or not, and so forth. Also, substitute “buy,” “donate,” or whatever verb is relevant for you where “act” is used below.

![](https://miro.medium.com/max/10000/1*RiO6Ion3ASOyGevFwFln-A.png?q=20000000)

Image by author

Time and money spent on the sure things, the sleeping dogs and the lost causes is wasted or even counterproductive. The persuadables are the people we really want to reach — the ones who, without our email or other form of “treatment,” would not take action. So who are those sought-after persuadables, and how do we identify them? That’s the job of uplift modeling.

What’s tricky, of course, is that we don’t know which people fit into each quadrant in the typology above *before* we treat them. We can’t do some sort of Schrödinger’s promotional offer in which we both send and don’t send our email! We can only send or not send, treat or not treat. We have to use the power of modeling to figure out who’s most likely to fit in each group before we take action.

![](https://miro.medium.com/max/10000/0*O4a_RAFt-oP5VUX3?q=20000000)

*Image via* [*GIPHY*](https://giphy.com/gifs/Quarks-cat-wdr-quarks-YT2JWERt7AzfYe6Sbb)

# Finding the Lift

This strategy is tricky because we’re facing a [causal inference](https://community.alteryx.com/t5/Alter-Everything-Podcast/44-Causality/ba-p/473475) problem: We want to identify people for whom treatment will cause a specific effect. [This paper](http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf) details and compares three main uplift modeling approaches used for this challenge. However, we’ll take a look at the method called Transformed Outcome, which is used in the Python package pylift we’ll use.

This method does rely on having some data already in hand. Ideally, you’ve done a randomized experiment, and you have data for both a control (untreated) group and a treatment group. You know who responded to the treatment and who did not. That response variable will be transformed into new values:

![](https://miro.medium.com/max/10000/1*Aq2DP1Rizl0rGSrBvkW1qw.png?q=20000000)

Image by author

When applied to the control and treatment groups, these new values result in an average across the board that is the same as the lift caused by the treatment for the entire group.

However, simply trying to predict these transformed outcomes as class labels — say, using the classification algorithm of your choice — can be problematic. The pylift package makes some necessary adjustments to the transformation to accommodate your groups’ sizes, to adapt the evaluation metrics to prevent overfitting, and to tune hyperparameters. You can still customize many aspects.

# Implementing Pylift in Designer

Pylift was built by data scientists at Wayfair (the company that also brought me the awesome rug in my home office).

![](https://miro.medium.com/max/10000/0*NYCsC8D6xDkHdwsN?q=20000000)

*Image via* [*GIPHY*](https://giphy.com/gifs/yXBqba0Zx8S4/)

I’ll use [an email marketing dataset](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html) for the sample workflow demonstrated here. The treatment is whether the customer was sent a promotional email. For the outcome, I’ve chosen the “visit” variable, which reflects whether or not the customer visited the retailer’s website in the two weeks after the email was sent.

You’ll need to get your dataset in shape first, either wrangling everything in your Designer workflow or within your Jupyter Notebook in the Python Tool. Pylift expects your data types to be integer, float or boolean, so you may need to one-hot encode data (again, either [in Designer](https://community.alteryx.com/t5/Data-Science/One-Hot-Encoding-What-s-It-All-About/ba-p/578652) or in Python using [pandas’ get\_dummies or sklearn’s OneHotEncoder](https://stackoverflow.com/questions/36631163/what-are-the-pros-and-cons-between-get-dummies-pandas-and-onehotencoder-sciki)).

For pylift, you’ll also need to have two binary variables labeled Treatment and Outcome, with values of 0 and 1. For Treatment, 0 indicates the treatment was not administered (e.g., no email was sent), and 1 indicates it was. For Outcome, 0 indicates the desired behavior or result did not occur (e.g., the customer did not visit the website), and 1 indicates it did occur. (Pylift can also work with [continuous outcome](https://pylift.readthedocs.io/en/latest/usage.html#continuous-outcome) variables instead of a binary outcome, such as a dollar amount spent by a customer, but things get a bit more complicated.)

The pylift package is built on sklearn, and so the process of using it looks similar. Pylift transforms the outcome variable as described above. All you need to do is specify your data and identify the Treatment and Outcome columns of the dataframe. Pylift will create training and test sets itself, and I chose to stratify these by the outcome variable due to the imbalance in the dataset (there were far more emails sent than visits to the website). This ensures that some of the few positive results for the outcome appear in both sets. You can also specify an estimator in the line below. Pylift uses [XGBRegressor](https://www.datatechnotes.com/2019/06/regression-example-with-xgbregressor-in.html) by default, but you [can use](https://pylift.readthedocs.io/en/latest/usage.html?highlight=xgbregressor#fit-and-hyperparameter-tunings-passing-custom-parameters) other options.

```
up = TransformedOutcome(df, col_treatment='Treatment',   
col_outcome='Outcome',   
stratify=df[‘Outcome’])
```

After this step, you can use [pylift’s EDA options](https://pylift.readthedocs.io/en/latest/eda.html) to dig into your data. For example, you can view a chart of the [net information value](https://multithreaded.stitchfix.com/blog/2015/08/13/weight-of-evidence/) provided by each variable in your dataset. This measure shows the relative strength of the relationship of each feature to the target.

![](https://miro.medium.com/max/10000/0*krsuLbJQ0lpi8MoV?q=20000000)

Net information value for predictor features

Finding the best parameters for the model and fitting it requires just two lines of code:

You can then view some evaluation metrics and visualizations for your model. For example, the cumulative gain chart for our email marketing campaign is shown below. This curve shows how much the campaign generated “incremental gains” (blue line) in website visits above simply randomly sending the email to customers (dashed line). “Fraction of data” refers to the proportion of our customers who were targeted. As shown below, this model shows that the campaign boosted website visits by around four percent when 80 percent of the customers received the email. If we were to use this model again to identify likely website visitors and send out the same email campaign, that could be the result we’d see.

However, in terms of evaluating this model, the small distance between our model and our random baseline shows that this model is not identifying “responders” very effectively. We might want to try other algorithms (i.e., [another classifier](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning) supported by sklearn) to see if we can generate a model that more clearly distinguishes between the customers who are and aren’t likely to visit.

![](https://miro.medium.com/max/10000/0*nz-3tKvNkpqt1Wzb?q=20000000)

I read [these authors’ analysis](https://pbiecek.github.io/xai_stories/story-uplift-marketing1.html) of this same dataset after I’d already generated this model, and I thought their explanation of our similar results was helpful:

> *It can be seen that our model is better than random choice but much worse than the practical/theoretical maximum possible. It is also worse than the case without ‘sleeping dogs’. Compared to uplift modeling in different domains, i.e. medical applications, treatment in marketing has generally smaller impact on individuals, therefore the dataset itself is more noisy and cumulative gains are smaller. It is also worth noting, that due to the small number of features, there are multiple cases in the dataset where two observations with the same features have different answers. This kind of noise in data also tremendously impacts the score and requires caution when training models. Also, since uplift itself is an interaction, our model does have to take them into consideration.*

When you’ve generated a model that is satisfactory, you can delve into [interpreting](https://community.alteryx.com/t5/Data-Science/Interpretability-Explainability-and-Machine-Learning/ba-p/630765) the model with [SHAP](https://christophm.github.io/interpretable-ml-book/shap.html) and partial dependency plots, following these authors’ [approach](https://pbiecek.github.io/xai_stories/story-uplift-marketing1.html#explanations-2).

# Moving Forward with Predictions

You can also try predicting the potential impact of the same campaign on data for other customers who were not previously targeted in the experiment that generated your original data. Pylift is able to generate predictions for new data, and you can calculate the predicted incremental gain for each customer in the new dataset (i.e., the decrease or increase in the outcome behavior resulting from the treatment).

What do you do with those predictions? You can exclude those whose chance of response is predicted to be affected negatively by the treatment. You also may want to target only a smaller group with the highest predicted incremental gain from treatment. Using your dataset with the predictions, you might use the Tile tool in your workflow on the prediction field to create groups representing levels of likely response. You could consider targeting only those customers in the top groups. Narrowing your outreach could make your treatment (e.g., your email campaign) more cost-effective, and also avoid the negative impact of disturbing those “sleeping dogs.”

![](https://miro.medium.com/max/10000/0*c7uIaqRONdN6bkk3?q=20000000)

*Don’t disturb the sleeping dogs! Image via* [*GIPHY*](https://giphy.com/gifs/47zMW1zumv5jyYPJc2)

For example, with this dataset and Alteryx Designer, I filtered out the negative predictions and then used the smart tile option in the Tile tool to create groups of customers with a predicted incremental gain. The tool created six groups of predicted outcomes, with the highest-scoring two groups including only 44 percent of the customers on the list used for predictions. It would likely make sense for me to focus my effort on these individuals most likely to respond to my campaign.

# What’s Next?

Uplift modeling is a complex topic with multiple approaches and nuances. I’d recommend exploring it in greater depth before giving it a shot, but I hope this example demonstrates the potential benefits of this technique: greater efficiency and higher return on your investment of effort and money.

In the version of this blog post on the Alteryx Community, you can find a sample workflow with a macro you can use in Alteryx Designer to try this analytic approach. You can use the included sample dataset and/or your own data. (Be sure you are running Designer [as an administrator](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/How-to-Always-Run-Alteryx-as-an-Administrator/ta-p/28440) so the macro can install the necessary Python package.)

Check out some of the recommended reading below for further details and inspiration!

# Recommended reading:

* [Pylift: A Fast Python Package for Uplift Modeling](https://tech.wayfair.com/data-science/2018/10/pylift-a-fast-python-package-for-uplift-modeling/), blog post and explainer from its creators at Wayfair
* [Causal Inference and Uplift Modeling: A Review of the Literature](http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf)
* [Uplift Modeling: eXplainable predictions for optimized marketing campaigns](https://pbiecek.github.io/xai_stories/story-uplift-marketing1.html)
* [Incremental Lift Model at Cineplex (Alteryx use case)](https://community.alteryx.com/t5/Alteryx-Use-Cases/Incremental-Lift-Model-at-Cineplex/ta-p/182859)