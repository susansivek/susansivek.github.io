---
title: "Collaboration with Automation: A Personal Coach for Data Science"
date: 2020-05-12
excerpt: "\"You’ve got some data. You’ve got some questions about it. And you’ve got a whole bunch of predictive tools at your disposal."
original_url: "https://community.alteryx.com/t5/Data-Science/Collaboration-with-Automation-A-Personal-Coach-for-Data-Science/ba-p/568380"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Collaboration-with-Automation-A-Personal-Coach-for-Data-Science/ba-p/568380](https://community.alteryx.com/t5/Data-Science/Collaboration-with-Automation-A-Personal-Coach-for-Data-Science/ba-p/568380)*

You’ve got some data. You’ve got some questions about it. And you’ve got a whole bunch of predictive tools at your disposal.

Now what?

I had the privilege of being a guest for this week’s episode of the Alter Everything podcast and interviewing Doris Jung-Lin Lee, a doctoral candidate at the University of California, Berkeley. Lee and her research collaborators are doing some very cool work on developing “human-in-the-loop” automated machine learning systems. (We've got links to their work and other resources in the [podcast show notes](https://community.alteryx.com/t5/Alter-Everything-Podcast/60-Analytics-automation-keeping-humans-in-the-loop/ba-p/568377).) Their research shows how automation not only can increase data workers’ productivity, but also can increase their ability to focus on the most satisfying parts of their work. The combination of automation and human thinking power makes the most of humans’ contributions to the data analytic process. But what might that look like in practice?

Last week, we looked at [simple linear regression](https://community.alteryx.com/t5/Data-Science-Blog/Simply-Powerful-Solving-Nonprofits-Data-Challenges-with-Linear/ba-p/565913), used by some of the student participants in the Alteryx for Good Data Challenge as they analyzed their nonprofit partners’ data. I shared an example of using simple linear regression to see if we could predict movie ratings by Rotten Tomatoes users based on critic ratings compiled by Metacritic.

But there’s a lot more in that dataset, and my simple linear regression didn’t really offer impressive results. Maybe other predictive tools could do a better job -- but maybe I’d also like to have a “coach” guide me through using them. I can be the “human in the loop,” and [Assisted Modeling](https://community.alteryx.com/t5/Analytics-Blog/Is-Assisted-Modeling-for-Me/ba-p/422682) in Designer (currently in beta; [details here](https://www.alteryx.com/assisted-modeling)) can automate my exploration, model building and model comparison.

Let’s reimagine the same movie rating prediction task from last week. My dataset includes movie ratings from IMDb, Rotten Tomatoes and Metacritic, including both user and critic ratings. Last week’s example was simple, literally; I used simple linear regression to see if I could predict Rotten Tomatoes user ratings with the Metacritic critic ratings. (I can’t prove from this regression that Metacritic critic ratings actually have any kind of causal effect on the Rotten Tomatoes user ratings, but I can at least see if there is a strong relationship between them.)

![SusanCS_0-1589217600536.png](/assets/images/posts/collaboration-with-automation-a-personal-coach-for-data-science/medium-078e2d46.png)

My simple linear regression workflow from last week.

My simple linear regression was … pretty meh. It resulted in an RMSE (root mean squared error) of 0.73. The RMSE is expressed in the original units of my target variable, which is the normalized Rotten Tomatoes rating, on a scale from 0 to 5 … and being up to three-quarters of a point off in my predictions is not fantastic.

What if I wanted to try some other predictive models for these data, but I wasn’t 100% sure which model would be best, or which other variables I might use from this rich dataset? That’s where Assisted Modeling helps me out. I can introduce the tool to my data, then guide it through a few steps to ensure it makes the right decisions about the type of prediction I want and the kinds of data I have.

First, I’ll recreate last week’s simple linear regression. I tell Assisted Modeling that I want the Metacritic critic rating as my predictor variable, and the Rotten Tomatoes user rating as my target variable. The tool correctly identifies that I want to perform a regression, since I’m working with two continuous numeric variables.

But, plot twist! The Assisted Modeling tool offers me not just linear regression, but also two other models: [Decision Tree](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Planting-Seeds-An-Introduction-to-Decision-Trees/ta-p/134623) and [Random Forest](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Seeing-the-Forest-for-the-Trees-An-Introduction-to-Random-Forest/ta-p/158062). You might first think of these models as tools for classification, but both can also be used for regression. The tool builds all three models for me and displays a neat leaderboard that succinctly summarizes the models’ performance for me. It even places a little medal next to the model it recommends I use. 🏅

The Assisted Modeling leaderboard.

Closer examination of those leaderboard results, though, reveals that none of the three models the tool and I initially generated does better than my simple, manually built linear regression. (This regression model likely differs from my manually built model because the Assisted Modeling tool splits data differently for building and testing.) Am I out of luck for coming up with a better model?

It turns out that I’m actually well positioned with Assisted Modeling to refine and improve my modeling predictions. Here’s where that human and machine collaboration comes in, as we discuss in the podcast episode!

Right now, I’m leaving a whole bunch of other potentially useful data untouched in my dataset. Maybe I didn’t consider those variables at first or didn’t feel confident expanding the model beyond a couple of variables. But if I revisit the configuration option that allows me to choose predictor variables for Assisted Modeling, I see that the tool has identified other potentially “good predictors” for me:

Part of the Assisted Modeling analysis of the variables in my dataset.

Here’s where my human “wisdom” -- well, my knowledge of my dataset, at least! -- is critical, though. The tool is simply looking for other variables in my dataset that are strongly related to my target. However, the first, second, and fourth checked items on that list are just other forms of my target variable that also happen to be in the dataset, so of course they are strongly related. I won’t want to use those as predictors. I also have three other variables here that are different forms of the same IMDb movie ratings, so I should choose only one of those to use. I’ll go with the “IMDB\_norm” variable. So, of all the potential options you see checked above, I ended up using only the last one, which represents IMDb users’ ratings of the movies.

I then build the models again using *two* predictor variables -- getting fancy, with Assisted Modeling’s help! I get these results:

![SusanCS_3-1589217600356.png](/assets/images/posts/collaboration-with-automation-a-personal-coach-for-data-science/large-eebbba3d.png)

The second leaderboard for my two-variable modeling attempt.

As you can see, adding that extra predictor variable helped quite a bit, with the RMSE for my new two-predictor Random Forest model dropping to 0.44. With a couple more clicks, I can add any or all of these models to my workflow and use them however I wish.

![SusanCS_4-1589217600199.png](/assets/images/posts/collaboration-with-automation-a-personal-coach-for-data-science/large-ed47465e.png)

The three models shown on my canvas together.

My predictions for Rotten Tomatoes’ user ratings are now going to be rather better, thanks to the insights Assisted Modeling and I discovered together.

In the podcast episode below, Doris and I address how automated data analysis tools are developing that, like Assisted Modeling, serve as a “personal coach” and collaborator for those who are building their data science and predictive skills. Human insights, critical thinking, and experience are still essential to data analysis, but having more guidance to make building models easier and potentially more sound will likely be a welcome addition to our data science process.

Check out the podcast episode below!