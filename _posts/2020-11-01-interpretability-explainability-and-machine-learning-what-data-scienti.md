---
title: "Interpretability, Explainability, and Machine Learning – What Data Scientists Need to Know"
date: 2020-11-01
excerpt: "I use one of those credit monitoring services that regularly emails me about my credit score: “Congratulations, your score has gone up!” “Uh oh, your score has gone down!” These fluctuations of a couple of points don’t mean much. I shrug and delete…"
original_url: "https://www.kdnuggets.com/2020/11/interpretability-explainability-machine-learning.html"
---

*Originally published at [https://www.kdnuggets.com/2020/11/interpretability-explainability-machine-learning.html](https://www.kdnuggets.com/2020/11/interpretability-explainability-machine-learning.html)*

I use one of those credit monitoring services that regularly emails me about my credit score: “Congratulations, your score has gone up!” “Uh oh, your score has gone down!”

These fluctuations of a couple of points don’t mean much. I shrug and delete the emails. But what’s causing those fluctuations?

Credit scores are just one example of the many automated decisions made about us as individuals on the basis of complex models. I don’t know exactly what causes those little changes in my score.

Some machine learning models are “black boxes,” a term often used to describe models whose inner workings — the ways different variables ended up related to one another by an algorithm — may be impossible for even their designers to completely interpret and explain.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132118i20EC116FE722170F/image-size/medium?v=1.0&px=400)

*Photo by* [*Christian Fregnan*](https://unsplash.com/@christianfregnan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/box?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

This strange situation has resulted in questions about priorities: How do we prioritize accuracy, interpretability, and explainability in the development of models? Does there have to be a tradeoff among those values?

But first, a disclaimer: There are a lot of different ways of defining some of the terms you’ll see here. This article is just one take on this complex issue!

### Interpreting and Explaining Models

Let’s take a closer look at *interpretability* and *explainability* with regard to machine learning models. Imagine I were to create a highly accurate model for predicting a disease diagnosis based on symptoms, family history, and so forth.

If I created a logistic regression model for this purpose, you would be able to see exactly what weights were assigned to each variable in my model to predict the diagnosis (i.e., how much each variable contributed to my prediction).

But what if I built a complex neural network model using those same variables? We could look at the layers of the model and their weights, but we might have a difficult time understanding what that configuration actually meant in the “real world,” or, in other words, how the layers and their weights corresponded in recognizable ways to our variables. The neural network model might have lower *interpretability*, even for experts.

Additionally, we can consider *global* interpretability (how does the model work for all our observations?) and *local* interpretability (given these specific data points, how is the model generating a specific prediction?). Both of those levels of understanding have value.

As you can imagine, with something like disease prediction, patients would want to know exactly how my model predicted that they had or didn’t have a disease. Similarly, my credit score calculation could have a significant impact on my life. Therefore, we’d ideally like to have models that are not just interpretable by the experts who construct them but also *explainable* to people affected by them.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132111i92B4370C2FAD5302/image-size/medium?v=1.0&px=400)

This explainability is so important that it has even been legislated in some places. The EU’s General Data Protection Regulation (GDPR) includes a [“right to explanation”](https://www.privacy-regulation.eu/en/recital-71-GDPR.htm) that has proven somewhat [challenging to interpret](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3196985), but that mandates greater “algorithmic accountability” for institutions making data-driven decisions that affect individuals. The U.S. Equal Credit Opportunity Act requires that financial institutions provide people who are denied credit or given less favorable lending terms a clear explanation of how that decision was made. If an algorithm was used in that decision, it should be explainable. As the [Federal Trade Commission says](https://www.ftc.gov/news-events/blogs/business-blog/2020/04/using-artificial-intelligence-algorithms), “... the use of AI tools should be transparent, explainable, fair, and empirically sound while fostering accountability.”

But even if explainability isn’t legally required for a particular situation, it’s still important to be able to communicate about a model’s workings to stakeholders affected by it. Some kinds of models are inherently easier to translate to a less technical audience. For example, some models can be visualized readily and shared. [Decision tree models](https://community.alteryx.com/t5/Alteryx-Knowledge-Base/Planting-Seeds-An-Introduction-to-Decision-Trees/ta-p/134623) can often be plotted in a familiar flowchart-esque form that will be explainable in many cases. (If you want to see a super cool animated visualization, scroll through [this tutorial](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) on decision trees.) Some natural language processing methods, like [topic modeling](https://community.alteryx.com/t5/Data-Science-Blog/Getting-to-the-Point-with-Topic-Modeling-Part-1-What-is-LDA/ba-p/611874) with LDA, may [provide visuals](http://bl.ocks.org/AlessandraSozzi/raw/ce1ace56e4aed6f2d614ae2243aab5a5/) that help viewers understand the rationale for their results.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132110iFA8B5A36ACD2DA88/image-size/medium?v=1.0&px=400)

In other cases, you may have to rely on quantitative measures that demonstrate how a model was constructed, but their meaning is less obviously apparent, especially for non-technical audiences. For example, many statistical models display how each variable is related to the model’s output (e.g., the coefficients for predictor variables in linear regression). Even a [random forest model](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Seeing-the-Forest-for-the-Trees-An-Introduction-to-Random-Forest/ta-p/158062) can offer a measure of the relative importance of each variable in generating the model’s predictions. However, you won’t know exactly how all the trees were constructed and how they all contributed together to the final predictions offered by the model.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132112i0A3CC604257BED13/image-size/medium?v=1.0&px=400)

*An example of the variable (feature) importance plot generated by the* [*Forest Model Tool*](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Forest-Model/ta-p/305724)*.*

Whichever method is used to gain insight into a model’s operation, being able to discuss how it makes predictions with stakeholders is important for improving the model with their informed input, ensuring the model’s fairness, and increasing trust in its output. This need for insight into the model might make you wonder if black boxes are worth the challenges they pose.

### Should Black Boxes be Avoided? What About Accuracy?

There are some tasks that today rely on black-box models. For example, image classification tasks are often handled by [convolutional neural networks](https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/) whose detailed operation humans struggle to understand — even though humans built them! As I’ll discuss in the next section, fortunately, humans have also built some tools to peek into those black boxes a little bit. But right now, we have many tools in our everyday lives that rely on difficult-to-interpret models, such as devices using facial recognition.

However, a model that is a “black box” doesn’t necessarily promise greater accuracy in its predictions just because it’s opaque. As [one researcher](https://www.nature.com/articles/s42256-019-0048-x) puts it, “When considering problems that have structured data with meaningful features, there is often no significant difference in performance between more complex classifiers (deep neural networks, boosted decision trees, random forests) and much simpler classifiers (logistic regression, decision lists) after preprocessing.”

It appears there doesn’t always have to be a tradeoff between accuracy and interpretability, especially given new tools and strategies being developed that lend insight into the operation of complex models. [Some researchers](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8882211) have also proposed “stacking” or otherwise combining “white-box” (explainable) models with black-box models to maximize both accuracy and explainability. These are sometimes called “gray-box” models.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132114i61A9E1136B48FB24/image-size/medium?v=1.0&px=400)

### Tools for Peeking Into Black Boxes

As mentioned above, humans are building tools to better understand the tools they’ve already created! In addition to the visual and quantitative approaches described above, there are a few other techniques that can be used to glimpse the workings of these opaque models.

Python and R packages for model interpretability can lend insight into your models’ functioning. For example, LIME (Local Interpretable Model-agnostic Explanations), creates a local, linear, interpretable model around a specific observation in order to understand how the global model generates a prediction with that data point. (Check out the [Python](https://github.com/marcotcr/lime) package, the [R](https://cran.r-project.org/web/packages/lime/index.html) port and [vignette](https://cran.r-project.org/web/packages/lime/vignettes/Understanding_lime.html), an [introductory overview](https://www.oreilly.com/content/introduction-to-local-interpretable-model-agnostic-explanations-lime/), or the [original research paper](https://arxiv.org/pdf/1602.04938.pdf).)

*This video offers a quick overview of LIME from its creators.*

Another toolkit called [SHAP](https://github.com/slundberg/shap), which relies on the concept of Shapley values drawn from game theory, calculates each feature’s contribution toward the model’s predictions. This approach provides both global and local interpretability for any kind of model. (Here again, you have options in [Python](https://github.com/slundberg/shap) or [R](https://github.com/ModelOriented/shapper), and can read the [original paper](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf) explaining how SHAP works.)

[Partial dependence plots](https://christophm.github.io/interpretable-ml-book/pdp.html) can be used with many models and allow you to see how a model’s prediction “depends” on the magnitude of different variables. These plots are limited to just two features each, though, which may make them less useful for complex, high-dimensional models. Partial dependence plots can be built with [scikit-learn](https://scikit-learn.org/stable/modules/partial_dependence.html) in Python or [pdp](https://bgreenwell.github.io/pdp/articles/pdp.html) in R.

![](https://community.alteryx.com/t5/image/serverpage/image-id/132113iD78C6192084EDF72/image-size/medium?v=1.0&px=400)

*Image from the* [*scikit-learn documentation*](https://scikit-learn.org/stable/modules/partial_dependence.html) *that shows how each feature affected the outcome variable of house value.*

[This paper](https://www.researchgate.net/profile/Josua_Krause/publication/301931162_Interacting_with_Predictions_Visual_Inspection_of_Black-box_Machine_Learning_Models/links/5a299994a6fdccfbbf8178ae/Interacting-with-Predictions-Visual-Inspection-of-Black-box-Machine-Learning-Models.pdf) shows an interesting example of an interactive interface built to explain a random forest model for a diabetes diagnosis to stakeholders. The interface used the concept of partial dependence in a user-friendly format. With this explanation, the stakeholders not only better understood how the model operated but also felt more confident about supporting further development of additional predictive tools.

Even the operation of complex image recognition algorithms can be glimpsed in part. “Adversarial patches,” or image modifications, can be used to manipulate the classifications predicted by neural networks, and in doing so, [offer insight](https://www.wired.com/story/inside-black-box-of-neural-network/) into what features the algorithm is using to generate its predictions. The modifications can sometimes be very small but still produce an incorrect prediction for an image that the algorithm previously classified accurately. Check out [some examples here](https://christophm.github.io/interpretable-ml-book/adversarial.html). (Cool/worrisome side note: This approach can also be used to fool computer vision systems, like [tricking surveillance systems](https://openaccess.thecvf.com/content_CVPRW_2019/papers/CV-COPS/Thys_Fooling_Automated_Surveillance_Cameras_Adversarial_Patches_to_Attack_Person_Detection_CVPRW_2019_paper.pdf), sometimes with a change to just one pixel of an image.)

Whatever approach you take to peek inside your model, being able to interpret and explain its operation can increase trust in the model, satisfy regulatory requirements, and help you communicate your analytic process and results to others.

**Recommended reading:**

* [The Mythos of Model Interpretability](https://arxiv.org/pdf/1606.03490.pdf), paper by Zachary C. Lipton, for a deep dive into definitions and their usefulness
* [Interpretable Machine Learning: A Guide for Making Black Box Models Explainable](https://christophm.github.io/interpretable-ml-book/), free online book by Christoph Molnar
* "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead," [article](https://www.nature.com/articles/s42256-019-0048-x) by Cynthia Rudin in *Nature Machine Intelligence*

[Original](https://community.alteryx.com/t5/Data-Science/Interpretability-Explainability-and-Machine-Learning/ba-p/630765). Reposted with permission.

**Bio:** [**Susan Currie Sivek**](https://www.linkedin.com/in/ssivek/)**, Ph.D.**, is a writer and data geek who enjoys figuring out how to explain complicated ideas in everyday language. After 15 years as a journalism professor and researcher in academia, Susan shifted her focus to data science and analytics, but still loves to share knowledge in creative ways. She appreciates good food, science fiction, and dogs.