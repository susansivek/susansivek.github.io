---
title: "Normalization, Standardization, and Regularization in Alteryx and Python"
date: 2021-03-18
excerpt: "\"\\\"Normal,\\\" \\\"standard,\\\" “regular”: Those are all fairly similar. Let’s just put -ization on the end of each one, too. That won’t ever be confusing, right?"
original_url: "https://community.alteryx.com/t5/Data-Science/Normalization-Standardization-and-Regularization-in-Alteryx-and/ba-p/733996"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Normalization-Standardization-and-Regularization-in-Alteryx-and/ba-p/733996](https://community.alteryx.com/t5/Data-Science/Normalization-Standardization-and-Regularization-in-Alteryx-and/ba-p/733996)*

"Normal," "standard," “regular”: Those are all fairly similar. Let’s just put -ization on the end of each one, too. That won’t ever be confusing, right?

If we could go back to the beginnings of statistics and data science, maybe we could advocate for choosing more distinctive words for these concepts. Alas, we’re stuck with these terms for now.

Each of these three -izations plays a unique role in your data preparation and analysis process. Let’s get some clarity on each so you know when and how to use them, whether you’re using Alteryx Designer, Python, or both.

Image via GIPHY

## **Feature Scaling: Normalization and Standardization**

Our own [@SydneyF](https://community.alteryx.com/t5/user/viewprofilepage/user-id/17210) wrote [a great article](https://community.alteryx.com/t5/Data-Science/Text-Normalization-in-Alteryx/ba-p/611283) on *text* normalization, the process by which text is prepared for analysis with natural language processing tools. She also wrote a [fantastic explanation](https://community.alteryx.com/t5/Data-Science/Data-Normalization-What-You-Need-to-Know-Before-Feature/ba-p/713658) of data normalization that addresses how the term is used in database structure and organization.

As Sydney notes in that second article, though, there’s yet another commonly used (but still somewhat variable) meaning of normalization: methods for scaling your data.

Let’s talk first about what “scaling your data” means with the fictional library dataset below. Say you have a variable (aka feature) that has a wide range of values (and hence [variance](https://en.wikipedia.org/wiki/Variance)), like the “Library Checkouts” field below — especially as compared to the variance of “Average Rating”:

|  |  |  |
| --- | --- | --- |
| **Title** | **Average Rating (1 to 5)** | **Library Checkouts** |
| Uncanny Valley | 3.0 | 45 |
| Quantum | 3.4 | 1,301 |
| The Lady Tasting Tea | 3.8 | 2,122 |
| The Midnight Library | 4.1 | 12,310 |

This variation in variance (oof) can cause issues for machine learning. To address it, feature scaling in some form, such as the methods described below, is generally recommended. [Neural networks](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Neural-Network/ta-p/300589) and support vector machines are sensitive to scaling, along with algorithms that use the distances between points in their calculations, like clustering and [PCA](https://community.alteryx.com/t5/Data-Science/Tidying-up-with-PCA-An-Introduction-to-Principal-Components/ba-p/382557).

Image via GIPHY

A feature with wide-ranging values can have disproportionate influence on these models’ predictions when compared to other features. Therefore, it’s typically better to constrain all the features’ values to a narrower range so they are all integrated equally into the model. “Scaling” encompasses a variety of procedures that make the variables more comparable.

***Min-Max Normalization***

Let’s dive into one form of normalization, which is one variety of feature scaling. “Min-max normalization” or “min-max scaling” recalculates all the values of your variables so that they fall within the range [0, 1] or [-1, 1]. (Check out [an equation](https://sebastianraschka.com/Articles/2014_about_feature_scaling.html#about-min-max-scaling) for this process.) The [0, 1] range is typically required for neural networks.

Our dataset above, if scaled so that values fall within [0, 1], would look like this:

|  |  |  |
| --- | --- | --- |
| **Title** | **Average Rating (1 to 5)** | **Library Checkouts** |
| Uncanny Valley | 0 | 0 |
| Quantum | 0.364 | 0.102 |
| The Lady Tasting Tea | 0.727 | 0.169 |

As you can see, the minimum values and maximum values for each variable end up at the top and bottom of the [0, 1] range; the other values lie in between. Most importantly, all the values across the features are more comparable and may contribute to a better-performing model. However, as you can imagine, this method is not as effective with outliers, which can pull the minimum and/or maximum values strongly in one direction.

In Alteryx Designer, you can try out the user-created [FeatureScaler](https://gallery.alteryx.com/#!app/FeatureScaler/5e342b880462d70decb5e915) macro, available in the Alteryx Analytics Gallery (alongside many other [useful data science tools](https://community.alteryx.com/t5/Data-Science/Free-Data-Science-Tools-for-Designer-A-Gallery-Tour/ba-p/669590)!). This macro can also convert your data (for example, a model’s predictions on your normalized data) from their normalized form back to their original units.

If you want to use this approach in Python and are using scikit-learn (one of the libraries included in the [Python Tool](https://help.alteryx.com/current/designer/python-tool) in Designer), you can use [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler), for which the [0, 1] range is the default. [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler) is another option and may be better for sparse datasets, as it preserves the data’s inherent structure. The scikit-learn User Guide has [an excellent section](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler) on these techniques. @DavidM [has also written](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/How-to-do-Feature-Normalization-in-Alteryx-incl-Python-Code-tool/td-p/313366) on the Community about normalization with the Python Tool.

***Standardization***

Just to be extra confusing, standardization is sometimes used to cover all these forms of scaling. However, one popular use of the term is a scaling method that can be more specifically called z-score standardization. This approach takes your features’ values and scales them so that they end up being [normally distributed](https://stattrek.com/probability-distributions/normal.aspx) (fitting that familiar old bell curve). The values are transformed so their mean is 0, and their standard deviation is 1. This method is also sensitive to outliers’ influence.

Standardization is especially important for machine learning algorithms that use distance measures (e.g., k-nearest neighbors, k-means clustering, principal component analysis) and for those that are built on the assumption that your data are normally distributed. These will likely perform better if you provide data that fits that assumption.

If you want to standardize your data in Designer, you can locate and use [this macro](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Standardize-Normalize-Metrics/m-p/32272/highlight/true#M12943) that’s installed to support your predictive analytics tools.

And, as above, another option is to use the Python Tool and scikit-learn, where [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler) will tackle this job.

***Which Method and When?***

As in the [recent](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-1-Evaluating-Classification-Models/ba-p/719190) [posts](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-2-Evaluating-Regression-Models/ba-p/722596) on model evaluation metrics, there’s no one right answer for all situations. You can try multiple methods of normalization and see which one helps your model perform better.

If your data has outliers that could be problematic for the approaches described above, you may want to try [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler) in scikit-learn, which uses the median and interquartile range to scale the data and retains the outliers. Here’s [a helpful tutorial](https://machinelearningmastery.com/robust-scaler-transforms-for-machine-learning/) for RobustScaler, and you can also check out [this great visual comparison](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html) of what data with outliers look like when handled with each of these approaches.

To make it a bit easier to normalize/standardize your data, I’ve built a simple macro using the Python Tool that will run your selected features from your dataset through your choice of four scaling options available in scikit-learn: MinMaxScaler, MaxAbsScaler, StandardScaler and RobustScaler. The macro is attached to this post.

Finally, remember that you usually will want to apply these methods to your training dataset only, not to your entire dataset. Scaling your entire dataset and *then* splitting it for training/testing allows some information about the distribution of the entire dataset to be available during training. If you split after scaling, your test dataset’s scaled values would be determined by “knowledge” of the entire dataset. However, that information will not be available when the model is actually used in production. This problem is one form of what’s called [data leakage](https://en.wikipedia.org/wiki/Leakage_(machine_learning)). Instead, split your dataset, train your model, preprocess your test data according to the same parameters used for the training data, and then assess your model’s performance.

Image via GIPHY

## **Regularization: Addressing a Different Issue**

This term seems like it should be sorted into the same category with normalization and standardization. Just looking at the word itself — it sounds like a similar concept, right?

Regularization is actually a strategy used to build better-performing models by reducing the odds of overfitting, or when your model does such a good job of matching your training data that it performs badly on new data. In other words, regularization is a way to help your model generalize better by preventing it from becoming too complex.

However, regularization is not part of data preprocessing, unlike normalization and standardization. Instead, it is an optional component in the model-building process. Regularization is often discussed in the context of regression models, and in Designer, you can optionally [use ridge regression, LASSO or elastic net regularization](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Regularization-in-Alteryx/ta-p/150873) when building linear and logistic regression models. However, regularization is definitely also relevant for other algorithms, including [neural networks](https://machinelearningmastery.com/introduction-to-regularization-to-reduce-overfitting-and-improve-generalization-error/) and support vector machines.

In the simplest terms, depending on the method used, regularization for regression models may reduce the number of variables included in a model and/or may try to bring their coefficients closer to zero, or a combination of both. For neural networks, regularization could also include [weight decay](https://machinelearningmastery.com/weight-regularization-to-reduce-overfitting-of-deep-learning-models/); [dropout](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf), where some layers’ output is ignored; and [early stopping](https://en.wikipedia.org/wiki/Early_stopping) when a model’s training ends early because it is generalizing less well as training proceeds (among [other approaches](https://machinelearningmastery.com/introduction-to-regularization-to-reduce-overfitting-and-improve-generalization-error/)).

As you can tell, regularization is in a whole different zone of the machine learning process from normalization and standardization, so don’t let its deceptively similar sound trip you up!

Image via GIPHY

And finally, check out the macro attached below as a starting point for your feature scaling tasks.

***I hope this article has helped you better understand these three important terms! Do you still have questions? Are there other data science terms you’d like to see clarified here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***

## **Additional Resources**