---
title: "Ghost Hunting: Factor Analysis with Python and Alteryx"
date: 2020-05-26
excerpt: "Update: Keep reading here for all the details on factor analysis, but also check out this follow-up article where we provide a macro for easier use of this analytic method!
Those cheesy “ghost hunting” TV shows usually start the same way. Mysterious…"
original_url: "https://community.alteryx.com/t5/Data-Science/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/bc-p/577065"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/bc-p/577065](https://community.alteryx.com/t5/Data-Science/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/bc-p/577065)*

*Update: Keep reading here for all the details on factor analysis, but also check out [this follow-up article](https://community.alteryx.com/t5/Data-Science-Blog/A-Factor-Analysis-Macro-for-Designer/ba-p/573354) where we provide a macro for easier use of this analytic method!*

Those cheesy “ghost hunting” TV shows usually start the same way. Mysterious things are happening in a family’s home, with no clear explanation. The ghost hunters bring in fancy equipment to look for a hidden, supernatural cause of the strange events disturbing the peace and quiet.

Today I’ll introduce you to the equivalent of ghost hunting for your data. What if you believe something is happening in your data that isn’t precisely reflected by a single variable you measured -- maybe because it wasn’t or couldn’t be observed? Do you want to hunt for that mysterious explanation?

![SusanCS_0-1588786320658.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111515i28888009573AAC94/image-size/medium?v=1.0&px=400)

Factor analysis is your ghost hunting tool. This method is especially popular in market research, finance, and survey research (e.g., for human resources). The concept here is that patterns in your observed variables -- the ones you measured -- actually are the result of some hidden *latent* variables that are not directly present in your dataset, but that could be identified by identifying relationships among your observed variables. Factor analysis looks for those relationships and helps you determine whether there may actually be a “ghost in the machine.”

# Basics of Factor Analysis

We'll focus here on exploratory factor analysis, which is geared toward identifying those hypothetical “ghosts,” or latent variables, shaping your data. (There’s another variety called confirmatory factor analysis, but that will have to wait for a future post!) In exploratory factor analysis, the goal is to condense multiple observed variables into a smaller number of unobserved “factors” that represent a large amount of the variance and covariance among the observed variables. Your original variables are transformed into linear combinations of the factors; in other words, the observed variables can be restated using the factors calculated through the data analysis.

After factor analysis, we may see our observed data in a new light. If a subset of variables shows a high level of correlation, perhaps one latent “factor” shaped all of them together. We can examine how each variable, along with a subset of our other variables, contributes to a previously unobserved “factor” that was unrecognized among our data.

![SusanCS_1-1588786321474.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111516i6D180BB50157D348/image-size/medium?v=1.0&px=400)

You might be thinking that this sounds a lot like [Principal Components Analysis (PCA)](https://community.alteryx.com/t5/Data-Science-Blog/Tidying-up-with-PCA-An-Introduction-to-Principal-Components/ba-p/382557), and you’d be right. Both are “dimensionality reduction” techniques that try to reduce the number of variables, or dimensions, you have to cope with. But they *are* different in key ways. In PCA, the goal is to reduce a large number of variables to a small number of “principal components” that each explain a big chunk of the total variance among all the *observations*. The components are linear combinations of the original variables, and it can be hard to identify exactly how each observed variable plays a part in those components. PCA is a useful tool, but it has a different goal.

# An Illustration of Factor Analysis

In the attached workflow, I’ve provided an example of how factor analysis works and code for executing it in the Python Tool within Designer. We’ll get into its mechanics in a moment, but first let’s look at the “ghosts” we found in the data to better understand what factor analysis can do for us.

For my example, I’m using data from [a 2018 survey of employee satisfaction](https://data.tempe.gov/dataset/employee-survey) conducted by the city of Tempe, Arizona. I excluded a few questions that did not use a five-point Likert scale (the familiar Strongly Agree to Strongly Disagree range of choices). The 71 remaining [questions](https://gis.tempe.gov/employee-survey-dict-2018/) range broadly over many parts of an employee’s work life, including communication, infrastructure needs, support for development, and so forth. Understanding the responses to all of those questions holistically and finding deeper patterns could be challenging.

![SusanCS_2-1588786321720.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111517iA04FFBF2EEBBD258/image-size/medium?v=1.0&px=400)

But -- factor analysis to the rescue! I can extract four possible factors that capture much of the variation in the employees’ responses across the board. These each reflect my original variables (responses to the 71 survey questions), but were not *directly* measured in this way in the survey. I’ve examined the factors and made a judgment call about how best to characterize each of them, which is a subjective part of factor analysis. That’s part of the reason this process is considered exploratory.

Factor 1 appears to reflect employees’ sense of mutual respect and positive relationships with their supervisors. We could call this factor “strong employee-supervisor relationships.” Looking at the top eight questions in this factor (as ranked by their factor loadings, which I’ll explain shortly), all of them relate to comfort expressing opinions, clear expectations, respect, appreciation, and constructive feedback. (Choosing eight top questions is a bit of an arbitrary cut-off here, but for most of the factors, the loadings shrink after that point.)

Factor 2 includes issues of relationships among employees and departments, as well as motivation. We might label this factor “empowered, connected employees.” The top eight questions here all connect to communication between peers, feelings of innovation and motivation, and being encouraged to provide input on decisions.

Factor 3 reflects perceptions of parts of the city bureaucracy and how well they support employees. The questions all ask the employee about different parts of the city government that should offer services and guidance for employees. This factor could be called “perceptions of institutional support.”

Finally, Factor 4 is clearly focused on “employee compensation and benefits,” with the top questions all related to these issues.

How is this reduction to four factors helpful? We could, of course, just calculate averages of employees’ responses to different questions and see how they feel about different areas of their work experience. However, if we want to try to understand potential, larger underlying factors -- the “ghosts” that might quietly shape employees’ experiences but are not directly observable in a comprehensive way -- factor analysis helps us understand which combinations of our variables best explain differences in employees’ experiences.

![SusanCS_3-1588786320654.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111519iEA9EF0A65BFC2C59/image-size/medium?v=1.0&px=400)

# The Details of Factor Analysis in Python and Alteryx

To generate this example, I first loaded and lightly cleaned the Tempe survey data in Designer, then brought it into the Python Tool.

In Python, you have a few options for factor analysis: `scikit-learn`, `statsmodels`, or `factor_analyzer`. The first two packages are loaded by default for you when you use the Python Tool, and both have factor analysis components. However, the `scikit-learn` module for factor analysis (`sklearn.decomposition.FactorAnalysis`) doesn’t include an option for rotation, an element I’ll explain in a moment; `statsmodels.multivariate.factor` does have that option, but only in an experimental state right now.

I chose to use `factor_analyzer`, which does include rotation options and plays very nicely with the Python Tool. You can install it with `Package.installPackages(factor_analyzer)` in your Python Tool’s Jupyter Notebook. Be sure you're [running Designer as an administrator](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/How-to-Always-Run-Alteryx-as-an-Administrator/ta-p/28440) to install the package successfully.

You’ll need two more lines to get going with `factor_analyzer`:

```
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
```

That second line imports a tool for [Bartlett’s test of sphericity](https://www.statology.org/a-guide-to-bartletts-test-of-sphericity/). That test, briefly summarized, makes sure that your dataset actually contains correlated variables among which potential hidden factors can be recognized and built. The value returned from this test needs to be statistically significant, so as you’ll see in my notebook in the attached workflow, I print the value of *p* from this test before proceeding with my factor analysis. It shows up as “0.0,” meaning it’s tiny, so I can proceed as planned.

![SusanCS_4-1588786322054.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111520i62098A277CF17182/image-size/medium?v=1.0&px=400)

There’s one more interesting wrinkle in the factor analysis process: How many factors should you be looking for? You do have to provide `factor_analyzer` a number in its parameter `n_factors`. There are a variety of ways to determine a good number of factors, but one of the easiest to interpret is the scree plot, so named because it looks like a steep cliffside. The scree plot displays the eigenvalues for the various numbers of factors you might consider, ranging from 1 to the number of variables in your dataset (which would be a bit pointless, given that we’re trying to reduce dimensionality here). Factors with an eigenvalue of 1 or greater explain more variance in the observed variables than any single variable alone.

Typically the scree plot of factor numbers vs. eigenvalues will show a sharp drop, followed by a straight or only slightly sloped line. You’ll want to choose the number of factors that’s right before the straight line begins. The scree plot is demonstrated in my sample workflow’s Jupyter Notebook and is shown below. Four points are plotted on the “cliff” before the start of the straight line. Though this seems like a really simplistic method of choosing your number of factors, it works well in practice.

![SusanCS_5-1588786320678.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111518i8114F2F5A8B7B751/image-size/medium?v=1.0&px=400)

Scree plot for this dataset

There’s one more choice to make in setting the parameters for your factor analysis, which is whether and how your factors should be [rotated](https://www.theanalysisfactor.com/rotations-factor-analysis/). This is a complex topic, and you can find all sorts of opinions about how to make this decision. One key item is whether you care if your factors are allowed to correlate with each other or not. If you don’t care if they’re correlated, you can use an *oblique* rotation method; if you do want to avoid correlated factors, you should choose an *orthogonal* rotation method. The default in `factor_analyzer` is a type of oblique rotation (‘`promax`’) but you can choose a common orthogonal rotation if you prefer (‘`varimax`’), or one of five other options. For my example, correlated factors aren’t a concern, so I am using the default oblique method.

You’ll then fit the factor analysis model to the data and generate the factor loadings. Factor loadings reflect the degree to which a particular variable (in my example, a survey question) is correlated to the underlying, latent, “ghost” variable that we are assuming exists. Loadings closer to 1 or -1 show a stronger relationship, and the sign reflects whether the observed variable has a positive or negative effect on the latent variable. For example, the survey question “I am comfortable expressing my opinions about work-related issues to my immediate supervisor” has a loading of 0.95 for our Factor 1 described above. This high value suggests a very strong relationship between this observed variable and the latent variable we’re calling “strong employee-supervisor relationships.”

So we’ve got four interesting, intuitively sensible factors in these data. How much are they explaining about this dataset? That’s where examining the factors’ *proportional variance* comes into play. We can see that Factor 1, supervisor relationships, explains about 20% of the differences among employees’ responses in these data; Factor 2, peer/interdepartmental relationships, explains about 13%; Factor 3, institutional support, explains about 7%; and Factor 4, another 7% -- so we’re at about 48% total in *cumulative variance* across these four factors.

We’re still leaving over half of the variance in these data unexplained. That also makes sense, though. There are a great many personal and contextual issues that go into employee satisfaction, and we probably can’t find them all with a survey and a factor analysis. So maybe explaining 48% of the variation isn’t such a bad result. Depending on your use case, you may see that your factors explain much more or much less variance than we see in this example.

Another potentially interesting data point generated in the factor analysis is the communalities for each variable. Communalities represent how much of an individual variable’s variance can be explained by the factors identified in the analysis. For these survey data, 94% of the variance in the responses to the question “My immediate supervisor treats me with respect” can be explained with these factors (the two types of relationships and the institutional support).

![SusanCS_6-1588786321661.gif](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111522i0AF77DE6E2C0677C/image-size/medium?v=1.0&px=400)

# There Were Ghosts!

This factor analysis identified four reasonable “ghost” variables that underlie a large portion of the variance in the employee satisfaction survey responses. Are any of them terribly surprising? Not really -- of course, employees who feel respected will likely be happier across the board in their jobs -- but they do provide a convenient way of summarizing the data and reducing the 71 variables to a more manageable set of four factors.

Factor analysis might not be as dramatic as ghost hunters’ “discoveries” of supernatural beings, but it’s still fascinating to uncover those hidden variables that help explain your data more broadly.

Check out factor analysis for yourself with the Designer package attached below (update: or try the macro provided with [this follow-up article](https://community.alteryx.com/t5/Data-Science-Blog/A-Factor-Analysis-Macro-for-Designer/ba-p/573354)!).

![SusanCS_7-1588786320698.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/111521iCDC619DE7B80CCF5/image-size/large?v=1.0&px=999)