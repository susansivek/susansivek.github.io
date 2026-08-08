---
title: "Metric Matters, Part 1: Evaluating Classification Models"
date: 2021-03-01
excerpt: "\"Imagine taking a 100-question multiple-choice test and giving the right answer to 85 questions. You get a score of 85%. You must have studied and learned the material!"
original_url: "https://www.kdnuggets.com/2021/03/metrics-evaluating-classification-models-part1.html"
publication: "KDnuggets"
categories: [data-science]
But maybe the reality was a little different: You’d actually forgotten to study,…"
---
*Originally published at [https://www.kdnuggets.com/2021/03/metrics-evaluating-classification-models-part1.html](https://www.kdnuggets.com/2021/03/metrics-evaluating-classification-models-part1.html)*

Imagine taking a 100-question multiple-choice test and giving the right answer to 85 questions. You get a score of 85%. You must have studied and learned the material!

But maybe the reality was a little different: You’d actually forgotten to study, so you just went down your answer sheet and picked answer A for every question. Your teacher had gotten tired of putting the right answer in different places and just stuck 85 of the answers in option A. You lucked out!

![](/assets/images/posts/metric-matters-part-1-evaluating-classification-models/large-b448267d.svg)

There was probably a better way to measure your abilities than your score on this test. The same may be true of how you measure machine learning models’ prediction abilities.

The metrics — the quantitative measures of model performance — that you choose to evaluate your models matter, but with so many choices, which one should you select? You’ll definitely have to face this decision if you’re hand-coding your own machine learning models. However, you might also like to know more about your options, even if you’re using the awesome [new AutoML tool](https://community.alteryx.com/t5/Analytics/Power-to-the-Process-in-2021-1/ba-p/713080) in Designer 21.1, or for using Assisted Modeling to guide your model creation in either [assisted](https://community.alteryx.com/t5/Data-Science/Assisted-Modeling-The-Power-of-Augmented-Intelligence/ba-p/608237) or [automatic](https://community.alteryx.com/t5/Data-Science/Inside-the-Model-Construction-Zone-with-Automatic-Mode/ba-p/649430) mode. This knowledge is also helpful for using a package like [EvalML](https://community.alteryx.com/t5/Data-Science/Easy-Open-Source-AutoML-in-Python-with-EvalML/ba-p/715052).

### Objective Function vs. Metric

This is a distinction you'll need if you want to delve into the optional “Advanced Parameters'' of the [AutoML tool](https://help.alteryx.com/current/designer/automl). While you don’t have to tweak the Advanced Parameters settings, you can select which *objective function* you want to prioritize as AutoML evaluates different algorithms and parameters. Think of “objective” here as a “goal” for the model; which measure do you want it to maximize or minimize?

With that goal in mind, the AutoML process will build and evaluate a variety of models for you. It will rank the models it creates based on the objective function and will offer you its top choice as its output. But sometimes, a particular measure of the model’s performance may be especially relevant to your use case. If so, you may want to select the best fit for your needs from the objective function list.

When the model is built, you’ll see not only how it performed with regard to the measure you chose but also other metrics that reflect its performance in different ways. You may be interested in what those all mean, even if you didn’t choose them as your top priority for the model-building process.

So, to be a little more clear: all these quantitative measures of a model’s performance can be called *metrics*, but only one is used as the deciding factor for AutoML’s model selection in the objective function.

### Which Metrics Matter?

It depends. Don’t you love that answer?

The first step is to understand your options, and then you can decide which one best fits your situation. First, there are different metrics for classification problems than for regression problems. (Classification problems are when you want to find the category that something best fits, out of two or more choices, like true/false or low/medium/high. Regression is when you want to find a numeric value for something, like predicting a score or a home’s value.)

### Don't Be Confused or Imbalanced

This post relies on the idea of a [confusion matrix](https://community.alteryx.com/t5/Data-Science/What-is-a-Confusion-Matrix/ba-p/537567) and what it means to have true positives, false positives, true negatives and false negatives. I’ve included a confusion matrix for each metric below, with blue text showing which results are used in its calculation. It’ll also be good to know what “balanced” and “imbalanced” datasets are.

Here’s a confusion matrix for a binary (two-outcome) classification problem with possible outcomes of “Yes” or “No”:

|  |  |
| --- | --- |
| **Prediction**: Yes | **Prediction**: No |
| **Truth**: Yes | *True positive (TP)* The model predicted “Yes,” and the reality was “Yes.” | *False negative (FN)* The model predicted “No,” and the reality was “Yes.” |
| **Truth**: No | *False positive (FP)* The model predicted “Yes,” and the reality was “No.” | *True negative (TN)* The model predicted “No,” and the reality was “No.” |

Of course, outcomes could be all sorts of things: “voter” or “nonvoter,” “default” or “no default,” “conversion” or “no conversion.” Multiclass problems could have multiple potential outcomes, like “high risk,” “medium risk” and “low risk.”

One more thing: When we discuss “balanced” datasets in the context of classification, we mean that your outcome variable is pretty evenly distributed between/among the potential options, not heavily skewed or “imbalanced” such that one or some outcomes dominate. It takes a little extra consideration to build models when your training dataset has 99 “yes” outcomes and 1 “no” outcome, for example. Be sure to do thorough [exploratory data analysis](https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267), so you understand the distribution of your data before you choose a model and evaluation metric(s).

### Accuracy

|  |  |
| --- | --- |
| Prediction: Yes | Prediction: No |
| Truth: Yes | ***TP*** | *FN* |
| Truth: No | *FP* | ***TN*** |

*Definition:* Accuracy is the proportion of times your model predicted the right class out of all the predictions it made. Values range from 0 to 1, with higher values reflecting greater accuracy.

*Important to know:*

* This is the simplest metric to understand. It’s like your 85% on the test in our example above: 85% of your answers were right.
* However, just like the test, accuracy as a metric can make your model look really good when your data aren’t evenly distributed among classes (or, as in our example above, the "answers" heavily tend toward one option).
* Accuracy also considers errors in classification (false positives and false negatives) to be equally concerning to you. If one of those kinds of errors is especially risky for your use case, check out other metrics.

### Balanced accuracy

|  |  |
| --- | --- |
| Prediction: Yes | Prediction: No |
| Truth: Yes | ***TP*** | *FN* |
| Truth: No | *FP* | ***TN*** |

*Definition:* the average of the accuracy calculated for all classes (i.e., the proportion of correct predictions out of all predictions made). In a multiclass problem, there are different ways of calculating balanced accuracy, as [explained here](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score) with links to full references. Values range from 0 to 1, with higher values reflecting higher accuracy across all classes.

*Important to know:*

* Balanced accuracy is a good way to ensure that a model doesn’t just have good accuracy with one class in its predictions and terrible accuracy with the others. Instead, we’re looking for a good rate of correct predictions across all classes on average.
* This metric is an appropriate choice for imbalanced datasets because it considers all classes, so even if your model performs really well when predicting one class but terribly for another, you’ll see that reflected in this metric.Let’s say you have a dataset for training your model with a sample size of 100 and two potential outcomes, Yes or No. The outcome variable is imbalanced, with 85 items labeled “Yes” and 15 labeled “No.” Your first model’s effort to classify the data gives you this confusion matrix:  

  In this case, the model’s regular accuracy would be how many guesses it got right out of its 100 tries: 85%. You might see that metric and think, wow, awesome! However, the model was only good at predicting the “Yes” labels, and not great at predicting the “No” labels; in fact, it got all of those wrong.

  Balanced accuracy takes that not-great performance into account, and in this case, is only 42.5% (the average of the accuracy for the individual classes in the columns above). The model is suddenly looking a lot less awesome, but you’re awesome for checking on this metric and catching the problem.

* If the model performs equally well when predicting different classes, accuracy and balanced accuracy will have equal values.
* If you’re wanting to see generally good performance across classes and are not especially concerned about the specific types of errors being made, balanced accuracy might be a good metric for you.

![](/assets/images/posts/metric-matters-part-1-evaluating-classification-models/medium-7adb4871.svg)

### Precision

|  |  |
| --- | --- |
| Prediction: Yes | Prediction: No |
| Truth: Yes | ***TP*** | *FN* |

*Definition:* For a binary classification problem, this is the proportion of times the model predicted outcome A correctly out of the total predictions of outcome A (whether correct or incorrect). For a multiclass classification problem, precision is calculated with [averaging techniques](https://sebastianraschka.com/faq/docs/multiclass-metric.html). For both binary and multiclass problems, values for precision range from 0 to 1, with higher values reflecting greater precision.

*Important to know:*

* If false positives are more of a concern to you than false negatives, precision may be a good metric to use. In other words, you really want your model to be right when it predicts a certain class because your action on that prediction will be expensive or significant.
* For example, a model that predicts whether a patient has a disease might need to demonstrate high precision if the follow-up testing to diagnose the patient for certain is risky in itself. You wouldn’t want to undertake that testing unless you felt confident in the model’s prediction of a “true positive” or that the disease is actually present.

### F1 score

|  |  |
| --- | --- |
| Prediction: Yes | Prediction: No |

*Definition:* The weighted average of precision and recall, and one of the most popular metrics for evaluating model performance. (Recall is the proportion of times a model predicted Outcome A when Outcome A was truly present. It can also be called “sensitivity” or “probability of detection,” both of which are more descriptive names than “recall.”) The F1 score is calculated by multiplying precision by recall, dividing that by their sum, and then multiplying by 2, or: 2 \* [(precision \* recall) / (precision + recall)]. This metric can also be used for multiclass problems by averaging the scores for each class. Values range from 0 to 1, with higher values reflecting more correct predictions overall.

*Important to know:*

* If you read about the metrics above and thought, “But I care about both how well my model predicts both positive and negative results,” this may be your happy place. The F1 score is frequently used in machine learning, particularly for imbalanced data like our weird multiple-choice test example above.
* However, that doesn’t mean that the F1 score is always the perfect metric for all scenarios. This metric considers precision and recall to be *equally* important to your situation. That may be true, but what if different kinds of classification error present different degrees of concern for your situation? [Some researchers](https://www.jstor.org/stable/41819855) have suggested ways of weighting precision and recall.

### Matthews correlation coefficient

|  |  |
| --- | --- |
| Prediction: Yes | Prediction: No |

*Definition:* This metric incorporates true and false positives and negatives, as well as the number of items in each class, so it can be used on imbalanced datasets. Another way to think of this metric is that it addresses all the cells of a [confusion matrix](https://community.alteryx.com/t5/Data-Science/What-is-a-Confusion-Matrix/ba-p/537567), unlike some other metrics, plus the number of items in each class. The MCC can be used for binary and multiclass problems. For a binary problem, values range from -1 to 1; 1 represents perfect predictions, 0 represents predictions equivalent to random guesses, and -1 represents inverse predictions (i.e., the model is predicting the opposite outcome consistently). The value ranges [change for multiclass problems](https://en.wikipedia.org/wiki/Matthews_correlation_coefficient#Multiclass_case) depending on the data.

*Important to know:*

* [Some researchers](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6413-7) suggest that the MCC is more informative for binary classification problems than a measure like F1 or balanced accuracy because it considers all the outcomes of the model and the size of the classes.

### AUC

*Definition:* AUC is an acronym that stands for “area under the [receiver operating characteristic, or ROC] curve.” This one requires [an explanation of the ROC](https://community.alteryx.com/t5/Data-Science/ROC-Curves-in-Python-and-R/ba-p/138430) as well; we’ll just say here that this metric looks at how likely your model is to predict the probability of model outcomes in the correct rank order. It doesn’t consider what threshold you might choose for accepting the model’s prediction of a particular class. (Here are some [nice visuals](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) for this ranking process.) Values range from 0 to 1. An AUC of 0 means the model’s predictions are all wrong, and an AUC of 1 means they are all correct. An AUC greater than 0.5 shows that the model performs better than chance, i.e., better than simply guessing.

*Important to know:*

* Because AUC doesn’t factor in the threshold you want your model to consider in making its predictions, this metric might not be the best choice if you want your model to be very sure about its predictions. For example, maybe you really want to avoid false positives or false negatives for some domain-specific reason. In that case, you might look to a metric that incorporates that threshold.
* This metric might also be misleading for imbalanced datasets (see section 4 of [this paper](https://arxiv.org/pdf/1812.01388.pdf) for an explanation with visuals).

### Log loss

*Definition:* a measure that penalizes the model for incorrect predictions but also incorporates the model’s confidence about its predictions. This metric is used for binary and multiclass classification and is suited for models that provide the probabilities for assigning each potential class. Lower scores are considered ‘better’ with regard to model performance, but this value is not very informative if you’re looking at just one model; it is more useful for model comparison. Values can range from 0 (probabilities were perfectly predicted) to, well, infinity.

*Important to know:*

* If a model predicts a certain class with high confidence but is totally wrong, log loss will increase.
* Here’s one way to think about log loss: Imagine you have a friend who sometimes makes incorrect predictions but always proclaims loudly how correct their predictions will be. You’d probably be less likely to trust that friend’s predictions than those of a different friend who also sometimes makes incorrect predictions but who isn’t so arrogant about whether they’ll be right. Log loss essentially gives you a measure of how much you can trust your model’s predictions while considering how strongly it asserts those predictions’ truth. If the model says, well, I predict A but only with 42% certainty, then that prediction, if incorrect, wouldn’t be penalized as harshly as predicting A with 89% certainty.
* Log loss may be a good choice for imbalanced datasets.

Remember, no one metric is right for every situation, so choose the option that makes the most sense for your particular goals and desired outcomes. It’s an important decision, but I hope this list has helped you evaluate your choices.

[Original](https://community.alteryx.com/t5/Data-Science/Metric-Matters-Part-1-Evaluating-Classification-Models/ba-p/719190). Reposted with permission.

**Bio:** [Susan Currie Sivek, Ph.D.](https://www.linkedin.com/in/ssivek/), is the data science journalist for the Alteryx Community, where she explores data science concepts with a global audience. Her background in academia and social science informs her approach to investigating data and communicating complex ideas — with a dash of creativity from her training in journalism. Susan also loves getting outdoors with her dog and relaxing with some good science fiction.