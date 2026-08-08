---
title: "Balancing Act: Classification with Imbalanced Data"
date: 2021-11-04
excerpt: "Yoga, relaxation, a gratitude journal: All of these might help you find peace and harmony. But your datasets also need your help to achieve an ideal balance — and, like self-care for humans, things can go awry if we don’t take time to find…"
original_url: "https://community.alteryx.com/t5/Data-Science/Balancing-Act-Classification-with-Imbalanced-Data/ba-p/841878"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Balancing-Act-Classification-with-Imbalanced-Data/ba-p/841878](https://community.alteryx.com/t5/Data-Science/Balancing-Act-Classification-with-Imbalanced-Data/ba-p/841878)*

Yoga, relaxation, a gratitude journal: All of these might help you find peace and harmony. But your datasets also need your help to achieve an ideal balance — and, like self-care for humans, things can go awry if we don’t take time to find equilibrium.

![SusanCS_0-1635870878126.gif](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium.jpeg)

Image via GIPHY

Understanding the distribution of your training data among the classes you want to predict and making adjustments accordingly are key steps in creating a quality classification model. Imbalanced datasets are especially likely to occur when you are trying to predict something infrequent, like fraudulent transactions that occur rarely or unusual equipment failures. However, regardless of your specific domain, you’ll always want to assess the distribution of the target classes.

Take a deep cleansing breath, and let’s explore the how and why of contending with imbalanced datasets. We’ll focus on *binary* classification here, where there are two possible outcomes for your target variable. We’ll check out some tools in Designer and Python to make the process easier, too.

## **Free Your Mind with EDA**

It’s probably part of your data analysis routine already, but thorough exploratory data analysis (EDA) is vital to successful model building. In particular, for our purposes here, you’ll want to pay close attention to the distribution of your outcome variable. Whether you are attempting to build a model for binary classification (just two classes) or multi-class classification (more than two options), your path forward is simplest if your data are pretty evenly distributed among the classes.

Of course, things rarely work out that smoothly. Let’s take a look at the [credit card fraud detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle as an example. I created a smaller version of this dataset with 57,355 rows for this demo, with each row representing a transaction. I kept the imbalance between its fraudulent/non-fraudulent transactions, though, with only 492 of those transactions marked fraudulent.

In Designer, it’s easy to get quick insight into your variables’ distribution with the [Basic Data Profile Tool](https://help.alteryx.com/20213/designer/basic-data-profile-tool) and the [Frequency Table Tool](https://help.alteryx.com/20213/designer/frequency-table-tool), among other options. The latter generates a histogram like the one below that makes the imbalance in this dataset painfully obvious.

![SusanCS_1-1635870874309.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium.bin)

*A histogram for the 0 and 1 labels in the “Class” field, where 1 represents the comparatively few fraudulent transactions.*

## **Losing Your Balance**

If you repeatedly picked a row of this dataset at random and asked me whether it was one of the fraudulent transactions or not, I’d have pretty good odds of being right if I just said, “No,” over and over again. Similarly, if you simply jumped into training a model on these imbalanced data and only looked at your model’s accuracy, it would seem like you had an amazing model. You can read more about choosing the right metrics for classification models [in this article](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-1-Evaluating-Classification-Models/ba-p/719190); for now, just keep in mind that accuracy alone is really misleading for imbalanced data.

![SusanCS_2-1635870878467.gif](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium.png)

Image via GIPHY

As a quick example, let’s split my mini-dataset with 70% for training and 30% for validation. I could naively build a random forest model with no adjustment to the balance between the target classes. (You can follow along by opening the Alteryx package attached to this post.) I might be impressed at first: Wow, the model only misclassified 70 observations out of 40,149! But let’s take a closer look:

![SusanCS_3-1635870873826.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large.bin)

Unfortunately, as you can see, the model did great on predicting non-fraudulent transactions — but, sorry, credit card account holders; it didn’t do nearly as well at its actual job of detecting fraud. Time to make some adjustments for better results!

## **A Meditation on Sampling**

We have some ways to balance our datasets to avoid this situation, thankfully. Let’s explore some options, ranked from least involved to most complex (but still very manageable!).

![SusanCS_4-1635870878322.gif](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium-3de1eab1.png)

*Alteryx Machine Learning*

You’re in luck if you’re one of the first users of [Alteryx Machine Learning](https://www.alteryx.com/products/alteryx-machine-learning?utm_content=community) — especially if you’re contending with imbalanced data. Alteryx Machine Learning will automatically examine the distribution of class labels (e.g., 0/1, True/False, etc.) in your dataset. It’ll then apply appropriate oversampling or undersampling, depending on the size of your dataset, to accommodate any imbalance it finds. For example, it may apply the oversampling technique SMOTE, which we’ll discuss in a moment.

In the initial “Auto Insight” data exploration stage, Alteryx Machine Learning produces an easily downloadable plot, like the one below, that displays the distribution of class labels for your target variable.

![SusanCS_5-1635870873839.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium-e1e64d0f.bin)

Bar plot of target variable label distribution from Alteryx Machine Learning

In this case, as shown on the right side of the image below, Alteryx Machine Learning decided to undersample from the majority class, the non-fraudulent transactions, in my imbalanced dataset, and then built a selection of models to see which performed best. (Alteryx Machine Learning is so speedy that I could use the full dataset instead of a sample.)

Here, I selected balanced accuracy as the metric for evaluating the models, and a random forest classifier comes out on top in that comparison. The model performs even better in the next step of the process when it’s evaluated on the holdout data, with 91% balanced accuracy.

![SusanCS_6-1635870874407.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large.png)

*Alteryx Intelligence Suite*

With the Intelligence Suite in Designer, you have a couple of options. First, you can use the AutoML Tool to automatically build and evaluate models that prioritize the metric you choose. In the tool’s Advanced Parameters options, you can select a [metric](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-1-Evaluating-Classification-Models/ba-p/719190) better suited to an imbalanced dataset, or try multiple options to see how they compare. For example, you could tell the tool to prioritize balanced accuracy or log loss in its evaluation of various models.

![SusanCS_7-1635870874309.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium-57884715.png)

Setting up AutoML with two different objective function options suited for imbalanced data

![SusanCS_8-1635870873827.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large-5b25778e.png)

*Results from two AutoML-generated models*

Assisted Modeling is also an option here, but you’ll want to take a close look at the model leaderboard to see how the various metrics look. Again, accuracy isn’t the only measure to consider, so be sure to check out the balanced accuracy and F1 scores provided for each model as well, and make sure you’re pleased with how your chosen model(s) performs across the classes.

![SusanCS_9-1635870874000.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large-562ec3aa.png)

Results from Assisted Modeling’s classification models for these data

*Oversample Field Tool*

The [Oversample Field Tool](https://help.alteryx.com/20213/designer/oversample-field-tool) is included with Designer and is very easy to use, though its name is a bit confusing; it really undersamples your majority class, instead of oversampling your minority class. Simply drop it into your workflow and tell it which variable you want it to adjust, what the “positive” class is for that variable (e.g., in this case, a “1” for “fraudulent”) and what class proportions you want in the dataset. Essentially, this tool will then remove enough of your “negative” cases at random to achieve those proportions.

Depending on the size of your dataset and the relative (in)frequency of your positive class, however, you may end up with very few records remaining as a result, and as such, you won’t have much information on which to build your model. For example, if you have 1,000 records and only 100 of them represent the positive class, and you ask the tool to achieve a 50/50 balance for you, you’ll end up with just 200 records to build your model. That may be less than ideal for your particular modeling needs.

*Simple Oversampling*

Another balancing method would be to stratify your training data by the values of the target variable and then randomly sample with replacement from the smaller “minority” class. The goal would be to overrepresent those observations in the training dataset. However, this [“naive” sampling method](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/) results in repeated data and could cause your model to learn too much from those data points, potentially causing overfitting.

Fortunately, wise machine learning researchers have developed more sophisticated approaches to achieving balance.

![SusanCS_10-1635870878759.gif](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium-aa973dd8.png)

*Introducing SMOTE*

Another option for balancing your data is a procedure called SMOTE, which stands for Synthetic Minority Oversampling TEchnique. SMOTE is a widely used technique for dealing with class imbalance. Basically, this method makes up some data for you — but in a good way. That “synthetic” part refers to a process by which additional data similar to those in your minority class are generated and can be added to your dataset to bring the classes into balance.

SMOTE works by choosing one of your observations representing the minority class, finding its nearest neighbors (you can specify how many), and using the relationship between the chosen observation and the neighbor(s) to generate a new example of the minority class.

*SMOTE Family Macro*

One way to apply SMOTE is to use the SMOTE Family Macro, created by [@TimothyL](https://community.alteryx.com/t5/user/viewprofilepage/user-id/26394) and included in the Alteryx package attached to this post. This R-based macro uses the [smotefamily](https://cran.r-project.org/web/packages/smotefamily/smotefamily.pdf) package, which includes a variety of methods for implementing techniques based on SMOTE.

For example, in the attached workflow, passing the data through the SMOTE Family Macro and using the regular SMOTE option, achieves a better balance: 39,791 non-fraudulent transactions and 39,738 “fraudulent” ones. Of the latter, only 492 were in my original data, while the remainder have been synthesized.

Let’s then revisit the random forest model I attempted earlier, but now using the post-SMOTE dataset. My model can now learn about fraudulent transactions from more examples (even if most of them are synthetic), and as such, it does a better job of classifying the data:

![SusanCS_11-1635870873784.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large-c6f81bf8.bin)

Performance of the model built with data processed through the SMOTE Family Macro

The post-SMOTE model isn’t perfect, but it only misclassified 27 transactions, and its accuracy was roughly the same across the two classes, instead of making more mistakes on one than the other.

In addition to the configuration options provided in the macro, remember that you can also open the macro and alter its code however you’d like to suit your needs. [This article](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/A-Cheat-Sheet-of-Functions-to-Use-in-the-R-Tool/ta-p/178979) provides some of the ins and outs of working with R in Designer.

![SusanCS_12-1635870876609.gif](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/medium-16ff5d3c.png)

*SMOTE in Python*

Finally, if you’re happiest with Python solutions, you can use the [imbalanced-learn](https://imbalanced-learn.org/stable/index.html) library to implement various sampling methods that can address your data imbalances, including SMOTE. It only takes a few lines of code in a Python Tool to use this approach in a workflow, as you can see in the attached demo. However, this approach opens up a great many customization options.

You will need to install the package, as it’s not included with Designer; that means you’ll need to be running Designer as an admin. After that step is complete, you’ll simply divide your dataset into predictors and the target variable, resample using SMOTE or your chosen method from the library’s [options](https://imbalanced-learn.org/stable/user_guide.html), and then reassemble the dataset. You can then write the better-balanced, partly synthesized data out of the Python Tool for further use however you like in your workflow.

I did exactly that and then again used the Forest Model Tool to build a random forest model. The results look much like the results from the model built on the SMOTE Family Macro data above:

![new-smote-python.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large-3b6e18b4.bin)

Performance of the model built with data processed through SMOTE, implemented through imbalanced-learn in the Python Tool

Here again, overall accuracy is better, and the model’s mistakes are evenly spread between the two classes, instead of showing poor performance on the “minority” class less represented in the original data.

Let’s toss all three models — the naive model and the two SMOTE’d models — into the Model Comparison Tool to take a holistic look:

![SusanCS_14-1635870873944.png](/assets/images/posts/balancing-act-classification-with-imbalanced-data-2/large-6e276c07.png)

The Model Comparison Tool’s report on the three models’ performance

As you can see in the table above from the comparison report, all three models had great *overall* accuracy above 99%. However, the naive model built on the imbalanced data had lower performance on the fraudulent transactions. The two models built on better-balanced data both performed slightly better. If we’d used the full dataset provided on Kaggle, with almost 300,000 transactions, we could probably get even better performance. And, if with something as potentially costly as detecting fraud, even a small performance improvement could be financially quite meaningful.

## **Finding the Perfect Balance**

You’re now equipped with new tools for finding balance in your data and your life! Well, in data, at least, although better models could perhaps bring you happiness, too. Be sure to check out the recommended reading links below for additional information and options for addressing this important concern.

***Do you still have questions? Which other tools or data science concepts would you like to see addressed here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***

**Recommended Reading**