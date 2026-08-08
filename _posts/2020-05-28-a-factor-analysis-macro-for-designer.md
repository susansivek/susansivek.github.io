---
title: "A Factor Analysis Macro for Designer"
date: 2020-05-28
excerpt: "Last week I posted a full introduction to factor analysis, plus a workflow demonstrating one use of this analytic approach in Designer. But now the process is even easier with a macro -- attached at the bottom of this post -- that you can easily grab…"
original_url: "https://community.alteryx.com/t5/Data-Science/A-Factor-Analysis-Macro-for-Designer/bc-p/578615"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/A-Factor-Analysis-Macro-for-Designer/bc-p/578615](https://community.alteryx.com/t5/Data-Science/A-Factor-Analysis-Macro-for-Designer/bc-p/578615)*

Last week I posted [a full introduction](https://community.alteryx.com/t5/Data-Science-Blog/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/ba-p/566434) to factor analysis, plus a workflow demonstrating one use of this analytic approach in Designer. But now the process is even easier with a macro -- attached at the bottom of this post -- that you can easily grab and put into your own workflow!

### **Factor Analysis: What and Why**

A quick summary: Exploratory factor analysis helps you find potential “latent” or hidden variables -- aka “factors” -- that represent combinations of your known, measured variables. Maybe there’s a particular subset of variables that are all correlated with each other and that together represent an unobserved influence on your dataset.

Factor analysis is often used in survey analysis, market research and finance to look for previously unrecognized but meaningful patterns among variables. Here are some potential uses:

* Analyzing customer or employee satisfaction survey results to find underlying patterns of responses along certain variables
* Checking consumers’ responses to questions about a new product to look for latent beliefs and perceptions about the product
* Examining opinion polls to look for unexpressed attitudes that shaped responses to different issues or candidates
* Identifying patterns in consumer behavior and purchases that define previously unidentified market segments
* Grouping taste testers’ responses to flavor elements in order to link related flavor perceptions
* Reviewing test scores to look for relationships among different skill sets and test performance

### **Try the Factor Analysis Macro**

To simplify your factor analysis, try the macro attached to this post! Be sure you're [running Designer as an administrator](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/How-to-Always-Run-Alteryx-as-an-Administrator/ta-p/28440) so that the necessary Python package can be installed successfully. You’ll need to have your survey questions or other variable names in the field names of your dataset. Your data also needs to be numeric. Rows containing null values will be dropped, as factor analysis does not perform well with missing values; you may want to [impute values](https://help.alteryx.com/2018.3/Imputation_Macro.htm) before bringing your data into the macro.

All you’ll need to do to configure the macro is:

* Choose which numeric variables you want to use in the analysis; and
* Select the number of factors you want to look for in your data. That number should be bigger than 1 but smaller than the number of variables you are using, since the goal is to simplify and reduce your data.

+ You may want to start with a small number -- say, 3 or 4 -- and then examine the scree plot provided in the macro’s output to see what your best choice might be. ([Last week’s post](https://community.alteryx.com/t5/Data-Science-Blog/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/ba-p/566434) talks about choosing the number of factors in more detail. The scree plot will not change based on the number of factors you select as a starting point; it will be the same every time you run the analysis.)

Add a Browse tool to each output anchor on the macro.

After running your analysis, check out your five Browse tools to find:

1. The variables in each of the factors identified in your data, and the loadings on each of the variables within those factors.
2. The variances explained by your factors; you may be most interested in the cumulative variance at the far right, which shows how much variance in your data your factors can together explain.
3. The communalities for the variables in your analysis.
4. A scree plot for your data, like the one shown above, that can be used to determine a good number of factors to seek in the data.

Don’t worry -- there’s a complete explanation for all of these terms in [last week’s post](https://community.alteryx.com/t5/Data-Science-Blog/Ghost-Hunting-Factor-Analysis-with-Python-and-Alteryx/ba-p/566434), so check it out as you explore your results.

That screenshot above shows all you have to do -- grab your data, tidy it up, and send it into the macro! Happy hunting for hidden factors.

factor analysis error.PNG