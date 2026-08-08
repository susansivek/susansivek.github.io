---
title: "The Data Science Celebrity Q&A: Meet P. Value (aka p-value)"
date: 2021-04-07
excerpt: "The mystery and influence of P. Value (also known as the p-value) have made it the most popular celebrity calculation of our time — and maybe also the most misunderstood. Despite “significant” starring roles in thousands of data analyses, many still…"
original_url: "https://community.alteryx.com/t5/Data-Science/The-Data-Science-Celebrity-Q-amp-A-Meet-P-Value-aka-p-value/ba-p/743016"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/The-Data-Science-Celebrity-Q-amp-A-Meet-P-Value-aka-p-value/ba-p/743016](https://community.alteryx.com/t5/Data-Science/The-Data-Science-Celebrity-Q-amp-A-Meet-P-Value-aka-p-value/ba-p/743016)*

The mystery and influence of P. Value (also known as the p-value) have made it the most popular celebrity calculation of our time — and maybe also the most misunderstood. Despite “significant” starring roles in thousands of data analyses, many still find P. Value mystifying, or even misleading.

So who is P. Value, really? Our interviewer sat down with P. Value for an exclusive Q&A to hear its origin story and find out why its success isn’t just due to chance. And, yes, we asked the tough questions: You’ll learn the truth behind that “p-hacking” controversy you’ve heard about.

Read on for our no-holds-barred conversation!

![SusanCS_0-1617644508619.gif](https://community.alteryx.com/t5/image/serverpage/image-id/178952i95C9EF47DC17A814/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Tell us about your roots. What’s P. Value’s life story?**

You want me to spill the [tea](https://www.merriam-webster.com/words-at-play/tea-slang-meaning-origin), huh? Funny. I was actually born because of an experiment about tea.

[Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) is my dad, but he was kind of an … well, anyway, he was an English statistician and geneticist — and he also had some [terrible ideas](https://www.newstatesman.com/international/science-tech/2020/07/ra-fisher-and-science-hatred). At the same time, he did some interesting things in statistics that people still use. Like, maybe you’ve heard of Fisher’s exact test? Or maximum likelihood estimation? And you can blame him for that [iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) that everyone uses to try out data science stuff.

It was one day sometime in the early 1920s. This coworker of my dad’s, [Muriel Bristol](https://en.wikipedia.org/wiki/Muriel_Bristol) — who had a Ph.D. and studied algae — made a bold claim. She said she could taste the difference between tea that had milk added before or after pouring the tea. It’s kind of a [long story](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2012.00620.x), and there’s different versions, too. There’s even [a whole book](https://en.wikipedia.org/wiki/The_Lady_Tasting_Tea) that got its title from the incident.

Anyway, apparently, my dad and a biochemist, William Roach, set up an experiment to see if Muriel really could tell which was which. And it inspired him to think about me.

![SusanCS_1-1617644505090.png](https://community.alteryx.com/t5/image/serverpage/image-id/178950iD72EF4BFEC9DDF12/image-size/medium?v=v2&px=400)

Ronald Fisher and Muriel Bristol

## **So what happened? And how did you help them understand the results of the experiment?**

They had a “null hypothesis” and an “alternative hypothesis” for the tea situation. The null hypothesis was that Muriel *couldn’t* tell the difference between the cups of tea with milk poured before or after pouring. The alternative hypothesis was that she *could* actually tell the difference.

You do an experiment to figure out whether the null or alternative hypothesis could better explain what’s happening. These guys had to ask how they could set up an experiment that would effectively test this. Also, how many cups of tea did Muriel have to identify correctly for my dad and Roach to feel like there was support for the alternative hypothesis?

That’s where I came in. Basically, my dad made me up to solve this problem. I’m a calculation that shows whether your results are *different enough* from what you would expect under the null hypothesis … such that you should consider the alternative hypothesis to potentially be a better explanation for what’s happening.

And, spoiler: Muriel could actually taste the difference! She even married William Roach.

![SusanCS_2-1617644506304.gif](https://community.alteryx.com/t5/image/serverpage/image-id/178951iBD29F8B99BA9FBCA/image-size/medium?v=v2&px=400)

## **OK, but talk more about this “results are different enough” business — what does that mean?**

What I do is tell the experimenter whether the results are different enough from just guessing, just chance, to see if there might be something different going on — by which I mean, there’d be support for the alternative hypothesis.

The smaller I get, the less likely your results are just due to chance. Usually people are looking for me to be 0.05 or less. That means there is a 5% or lower probability that you’d get these results if you assumed that the null hypothesis was the case. You could think of these results as “less expected” or “surprising.”

The 0.05 bar is generally accepted for most hypothesis testing purposes. But sometimes people are OK with a higher or lower number for me. It depends on the specific situation. Some folks are more relaxed, and some are more demanding, you know.

However, here's an important detail. A p-value at or below 0.05, or whatever threshold, just means that there is a statistically significant relationship between your independent and dependent variable. And that’s only in the context where you’re testing it.

For example, if you build a regression model, you’ll see p-values next to each independent variable in the model, and an overall value for the p-value of the F-statistic that’s calculated for the model as a whole. That’s a lot of p-values!

If you’ve got p-values below that 0.05 (or your chosen threshold) for a specific independent variable, that just means that within that regression model, there’s a statistically significant relationship between that variable and your outcome variable.

![giphy](https://community.alteryx.com/t5/image/serverpage/image-id/179164i07FBEC792B36EF69/image-size/large?v=v2&px=999)

## **Yay! So you're telling me which variables better predict my outcome.**

No. Sorry. This is *way* more complicated.

Super small values for p don’t mean that a “significant” variable is necessarily *really good* at predicting your outcome variable. Small p-values don’t imply big predictive power. It’s also a calculation specific to that configuration of that regression model, with whatever other variables you’ve included, and your specific data in that specific analytical approach. All very … specific. So that variable isn’t just significant forever in all situations.

(Unfortunately, that super specific-ness to your analysis means that you could also have other variables that *do* have predictive power, but whose p-values are too big to be significant. Weird but [true](https://www.pnas.org/content/pnas/112/45/13892.full.pdf)! So domain knowledge and other methods for examining your data are still important.)

A small p-value just means there’s a better chance you can reject the null hypothesis — which is probably that there was *no relationship* between that variable and the outcome variable. In other words, that teeny p-value is just an indicator that the variable is *relevant* to your outcome variable. I know you like to find things that are relevant, so that’s still good. It’s a step toward understanding your data.

And that p-value for your whole regression model, based on the [F-test](https://statisticsbyjim.com/regression/interpret-f-test-overall-significance-regression/#:~:text=The%20F%2Dtest%20of%20overall%20significance%20indicates%20whether%20your%20linear,that%20contains%20no%20independent%20variables.&text=F%2Dtests%20can%20evaluate%20multiple,fits%20of%20different%20linear%20models.)? It just says that the relationship you proposed by setting up a specific set of variables that you think connect in that particular way — well, if the p-value is as low as you’d like, congratulations! Your model is doing a better job of fitting the data than a model with *no* variables. I know, your model doesn’t feel like such an achievement anymore. But, yeah, still good information to have.

A final mind-blowing fact: You can have a model that’s significant overall but has no individually significant independent variables. I know, right?! That just [means](https://statisticsbyjim.com/regression/interpret-f-test-overall-significance-regression/#:~:text=The%20F%2Dtest%20of%20overall%20significance%20indicates%20whether%20your%20linear,that%20contains%20no%20independent%20variables.&text=F%2Dtests%20can%20evaluate%20multiple,fits%20of%20different%20linear%20models.) that the joint interaction of those variables is significant … but no variable alone makes the cut.

There’s one more thing I have to tell you, before you start telling everybody how your alternative hypothesis you came up with is totally the real explanation for things. Tiny p-values don’t “prove” your alternative hypothesis is “true.” It just means your null hypothesis is less likely to be the case.

![giphy-downsized](https://community.alteryx.com/t5/image/serverpage/image-id/179168iC568F5B517335010/image-size/large?v=v2&px=999)

## **Where can we find you working your magic in different statistical analyses today?**

I get awesome roles in all the statistical genres! You’ll see me starring (get it? \*) in the t-test when you want to see if two groups have significantly different means for some variable. That’s the [Test of Means Tool](https://help.alteryx.com/current/designer/test-means-tool) in Designer. A t-test is also at the heart of the [A/B Analysis](https://help.alteryx.com/current/designer/ab-analysis-tool), so I have a supporting role there, too. I also show up with a [Contingency Table](https://help.alteryx.com/current/designer/contingency-table-tool) when you’re checking for actual differences in the relationships between your variables.

Of course, I also play a part in analyzing [correlations](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Association-Analysis/ta-p/40459), like you see below. The numbers in the lower table of this output are my values for each of these correlations.

![SusanCS_4-1617644505107.png](https://community.alteryx.com/t5/image/serverpage/image-id/178953iA5A2248D0486D0B9/image-size/large?v=v2&px=999)
![SusanCS_5-1617644507109.gif](https://community.alteryx.com/t5/image/serverpage/image-id/178955i9A8905EA75D319E8/image-size/medium?v=v2&px=400)

Image via GIPHY

If you’re into modeling, well, I do that, too, in addition to my other glamorous jobs. We talked about regression earlier. If you build a regression model, like we said, I’ll pop up by each of your independent variables to show you which ones have a statistically significant relationship with your outcome variable. Again, that statistical significance just means that the result found by analyzing your variables’ relationship is *surprising* and potentially meaningful, but not that the variables found to have lower p-values are necessarily the stronger predictors for your outcome variable. And, of course, you'd want to check that p-value for the F-test to see how the whole model did.

![SusanCS_6-1617644505108.png](https://community.alteryx.com/t5/image/serverpage/image-id/178956i4A50352A4383FCFB/image-size/large?v=v2&px=999)

That's a model predicting a wine quality score with the [red wine dataset](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009). Look at that [Pr(>|t|)](https://stats.stackexchange.com/questions/49939/interpreting-summary-function-for-lm-model-in-r) column on the right and be starstruck! The \*\*\* means that alcohol and sulphates have a p-value of less than 0.001, but the blank spot by residual sugar means its p-value was over 0.05. So, in this particular model and this dataset, residual sugar is probably less relevant to wine quality than the other two variables, given that it didn’t show an unexpected or surprising connection to the outcome variable of wine quality. However, sulphates and alcohol may be relevant to the wine quality in this specific data situation.

You can also see me playing a supporting role in [comparing machine learning models](https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/). Want to know if it was just chance that one model performed better than another? I can give you a hand there, too.

Basically, if you’ve got a hypothesis, I can help you test it.

![SusanCS_7-1617644505115.gif](https://community.alteryx.com/t5/image/serverpage/image-id/178957i0D20D9743D8D1D86/image-size/medium?v=v2&px=400)

Image via GIPHY

## **You’ve been named in some scandals in research lately -- that “**[**p-hacking**](https://www.wired.com/story/were-all-p-hacking-now/)**” folks have probably heard about. What’s that about?**

Yeah, well, none of that was my fault. I’m just a calculation, you know? And hacking sounds kind of criminal or something — but this stuff can just happen in data analysis, even when people have good intentions.

Some people get so determined to find statistically significant results in their research that they just keep digging around in their data, running their numbers every which way, until they get some result where I’m less than 0.05. Some people call it data dredging or — my favorite — significance questing. I like being the goal of a quest!

It’s a bummer when people think that just because they didn’t find anything statistically significant, all their work is just not worthy of sharing. Like, not finding something can be important, too.

Anyway, it’s best practice to decide and state what hypothesis you’re testing and what your test statistic is going to be, like the t-statistic in a t-test or chi-square for a contingency table … *before* you start analyzing your data. That way you can’t change things up later when your results don’t turn out the way you hoped. You’ve got to commit. Put a ring on that analytical method.

And also, a significant relationship, well, it might not actually make a difference in the real world. [Somebody](https://web.csulb.edu/~msaintg/ppa696/696stsig.htm) said to me one time, “Statistical significance is not the same as practical significance.”

That’s deep. We all have to ask, what really matters in this world? I just want to do my part to help answer that question.

![SusanCS_8-1617644509194.gif](https://community.alteryx.com/t5/image/serverpage/image-id/178958iD860524B4B603344/image-size/medium?v=v2&px=400)

*I hope you enjoyed this interview with celebrity guest P. Value! Do you still have questions? Which other tools or data science concepts would you like to see addressed here on the blog? (Many thanks to [@damc](https://community.alteryx.com/t5/user/viewprofilepage/user-id/101793) for* [*requesting*](https://docs.google.com/document/d/1RWvBd8JZ8_OyWlacZZ8ESKwiXP8KxeyMcwXygZoJkZs/edit?usp=sharing) *the topic of p-values!) Put your questions or requests in the comments below, and subscribe to the blog to get future articles.*

## **Recommended Reading**

## **Bonus**

Want another explanation for the p-value with the assistance of some very cute puppies? Check out this video from Cassie Kozyrkov, chief decision scientist at Google. (Thanks for the tip, [@AJacobson](https://community.alteryx.com/t5/user/viewprofilepage/user-id/83624)!)