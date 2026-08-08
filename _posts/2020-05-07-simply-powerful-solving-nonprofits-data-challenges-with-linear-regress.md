---
title: "Simply Powerful: Solving Nonprofits’ Data Challenges with Linear Regression"
date: 2020-05-07
excerpt: "\"Simple enough for statistical beginners, powerful enough to help solve big problems: That’s what some data analytics students learned about linear regression in a recent data challenge."
original_url: "https://community.alteryx.com/t5/Data-Science/Simply-Powerful-Solving-Nonprofits-Data-Challenges-with-Linear/ba-p/565913"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Simply-Powerful-Solving-Nonprofits-Data-Challenges-with-Linear/ba-p/565913](https://community.alteryx.com/t5/Data-Science/Simply-Powerful-Solving-Nonprofits-Data-Challenges-with-Linear/ba-p/565913)*

Simple enough for statistical beginners, powerful enough to help solve big problems: That’s what some data analytics students learned about linear regression in a recent data challenge.

The latest episode of the Alter Everything podcast features the participants of the Alteryx for Good Data Challenge, four teams of analytics students from Australia’s Western Sydney University and University of New South Wales. These students used Alteryx licenses donated through Alteryx for Good to find useful insights for four nonprofit organizations. The nonprofits provided the datasets and objectives; members of the data science team at NBN, RXP Group, Alteryx and Alteryx ACEs provided training and mentorship; and the students provided the all-important effort, creativity, and youthful motivation. The winning team -- selected last month -- received $10,000 for the nonprofit they represented, co-sponsored by Alteryx for Good and RXP Group.

Two of the student groups used good ol’ linear regression in their analyses. Linear regression is often one of the first modeling techniques statistical beginners learn, but it’s worth keeping in your toolbox, even when you’ve become familiar with more complex tools. If you’ve got [continuous](https://www.mathsisfun.com/data/data-discrete-continuous.html) numerical data, you may be able to use linear regression.

![SusanCS_0-1588706767317.png](/assets/images/posts/simply-powerful-solving-nonprofits-data-challenges-with-linear-regress/medium-de48830d.png)

The plot above helps us envision simple linear regression. If the line weren’t there, and all you had was the points, you’d probably think, Hey, those variables appear to be positively correlated! Yes, indeed -- values of the variable on the Y-axis tend to go up as values for the variable on the X-axis increase.

Recognizing that relationship is awesome ... but what if that correlation could also be used to predict the value of Y, if all you knew was the value of X?

That’s where linear regression comes in. In this case, we’ll try out bivariate (two-variable), simple linear regression. Ideally, we’d have a strong relationship between the two variables, which we can find by calculating the correlation coefficient for them. (If you aren’t sure how correlation works, [check this out](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Pre-Predictive-Using-the-Data-Investigation-Tools-Part-3-of-4/ta-p/100909) before you read on.)

We can use one variable as the predictor variable and the other as the response variable. You may have heard these called the independent and dependent variables.

On the above plot, the points roughly take the shape of a line, meaning that there is a *linear* relationship between the variables. (You could also see a nonlinear relationship occur; for example, a curved line could be apparent in the points. But that requires a different approach; we’re focused only on linear relationships here.)

Our goal with this regression is to find the equation that represents the line in the plot above, or in other words, the equation for the line that best “fits” our points in our dataset. This equation will have the response variable, Y, on one side; on the other will be an intercept (a constant number showing where the line hits the y-axis), the predictor variable or X (with some coefficient that actually represents the slope of the line), and an error term (a measure of random stuff that causes variation in your data, sort of like the margin of error in poll results). You may never actually see or use this equation, but it’s working in the background for you.

The cool thing about the equation is that we can plug in a value for our predictor variable and get a “fitted” value that is predicted for the response variable. We do have to stay within our known range of values for the predictor variable -- you can’t go crazy here! -- but still, being able to predict even on that level is pretty neat.

Remember that just because we see a correlation between these variables -- and despite the predictor/response names we use -- we can’t assume that the predictor variable necessarily *causes* the response variable. We’re still really just looking at correlation here, which as we all know, doesn’t prove any causal relationships exist.

As you can see, simple linear regression is a great tool for your statistical toolbox, but don’t stop here. There are many other varieties of regression, including:

* Multiple linear regression (for situations where you have more than one predictor variable; this is actually what the two student groups used!)
* Logistic regression (for predicting a binary response, like whether or not a customer purchased a subscription)
* Poisson regression (for count data, like the number of visitors to a mall as predicted by mall square footage)
* Polynomial regression (for nonlinear relationships)
* Multivariate regression (for several predictor variables *and* several response variables)

Try out the attached package for a fun introduction to simple linear regression with movie ratings from Metacritic and Rotten Tomatoes!

And be sure to listen to the podcast episode to find out how the data challenge student participants made the most of linear regression and other analytic approaches to help out their nonprofit partners.