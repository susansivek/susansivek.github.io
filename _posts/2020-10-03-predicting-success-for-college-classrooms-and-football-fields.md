---
title: "Predicting Success for College Classrooms and Football Fields"
date: 2020-10-03
excerpt: "Caps, gowns, diplomas … and data! Each student’s journey through a higher education institution creates lots of data. Recruitment, advising, retention, financial aid, administrative processes, assessment measures, course work, athletics and alumni…"
original_url: "https://towardsdatascience.com/predicting-success-for-college-classrooms-and-football-fields-5f45e20153bf"
---

*Originally published at [https://towardsdatascience.com/predicting-success-for-college-classrooms-and-football-fields-5f45e20153bf](https://towardsdatascience.com/predicting-success-for-college-classrooms-and-football-fields-5f45e20153bf)*

![](https://miro.medium.com/max/1200/1*YLHfH_9nIIBgR1dmx3AtzQ.jpeg)

*Photo by* [*MD Duran*](https://unsplash.com/@mdesign85?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/graduates?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Caps, gowns, diplomas … and data!

Each student’s journey through a higher education institution creates lots of data. [Recruitment](https://youtu.be/S0ejeB1OPR0), advising, [retention](https://community.alteryx.com/t5/Alteryx-Use-Cases/Predicting-and-Improving-Student-Retention/ta-p/599950), financial aid, [administrative](https://community.alteryx.com/t5/Alteryx-Use-Cases/Hkust-Saves-15-Hours-Month-with-Code-Free-Expense-Allocation/ta-p/599103) [processes](https://community.alteryx.com/t5/Alteryx-Use-Cases/Solving-Student-Number-Projections-Work-in-2-Minutes-Using/ta-p/497570), [assessment measures](https://community.alteryx.com/t5/Alteryx-Use-Cases/The-Thrill-of-Solving-in-Higher-Education-Alteryx-PolyU/ta-p/167050), course work, athletics and alumni activities all can be tracked in detail.

That data can be put to work in predictive models that advance institutional goals and aid student success. In addition to the effective use cases linked above, here are two more innovative ways researchers have used machine learning to make predictions in the world of higher ed. While there are challenges, of course, predictive analytics can provide insights into all kinds of higher ed data.

# KISS: Keep It Simple for Students (… and Models)

With many colleges and universities primarily teaching online right now, students are facing unusual learning challenges. Online learning management systems (LMS) offer tons of data on how students engage with course activities, online resources and each other. But which data best predict which students may struggle, and which models offer the most utility?

[A team of researchers](https://www.mdpi.com/2076-3417/10/15/5371) gathered data from Moodle, a popular LMS, across four semesters of an online introductory computer programming course. The data included students’ “cognitive interactions” with course content, their “social interactions” with each other, and their “teaching interactions” with the instructor; the researchers thought these categories might have differing predictive power. They also collected more data, such as the students’ total LMS interactions overall, and gave students a questionnaire about motivation and demographics. Finally, they built new features, including a “commitment factor,” a ratio of a student’s weekly total of interactions to the average for all students in the class.

*Photo by* [*Iris Wang*](https://unsplash.com/@irishappens?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/student-laptop?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

With all this intriguing data on hand, the researchers tested 13 different combinations of data and six different predictive algorithms to see which would best identify students at risk of dropping out of the course or failing by the eighth week.

Surprisingly, they found that — despite trying to develop new ways to examine students’ data — “the simple counting of interactions can be used to generate predictive models,” though other research had suggested this might not be enough sophistication. Their top-performing model for predicting at-risk students was an [AdaBoost](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Boosted-Model/ta-p/419302) classifier trained on total counts of all student interactions, and the second-best model also used AdaBoost with the same counts plus the “commitment factor” feature. Even the student questionnaire didn’t enhance the models beyond these few simple data points.

“We are able to conclude that a more structured course, with dozens of materials, best fits the students’ needs, because they can have good interactions with the course and, consequently, succeed. It also seems that student interaction means engagement, and more engagement leads students to succeed,” the researchers wrote.

While it seems like a no-brainer — build a robust online course, and students are more likely to succeed! — these results are helpful for those wanting to try out learning analytics and prediction themselves. You don’t necessarily have to build a super-complex model to identify and reach out to at-risk students. A simpler approach that tracks students’ online engagement and identifies those less engaged could still contribute to students’ success.

*Photo by* [*Andrew McElroy*](https://unsplash.com/@mcelroyaw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/%22american-football%22-twitter?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

# Predictive Analytics in College Athletics: Tweets for Success

Machine learning isn’t just for universities’ academic and administrative needs. Another [research project](https://ir.uiowa.edu/cgi/viewcontent.cgi?article=7872&context=etd), “From Hashtags to Heismans: Social Media and Networks in College Football Recruiting,” demonstrated how [logistic regression](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Logistic-Regression/ta-p/159461) could be used with football student-athletes’ Twitter posts to predict with 87% accuracy whether they would receive a scholarship offer in the month after those tweets.

Logistic regression outperformed other algorithms, including [random forest](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Seeing-the-Forest-for-the-Trees-An-Introduction-to-Random-Forest/ta-p/158062) and [SVM](https://community.alteryx.com/t5/Data-Science/And-For-My-Next-Trick-An-Introduction-to-Support-Vector-Machines/ba-p/360762), in correctly predicting the offers. The researcher hand-labeled over 7,000 tweets, but automated natural language processing, like [sentiment analysis](https://community.alteryx.com/t5/Data-Science-Blog/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153), could also have been useful.

Though selecting an athlete for a team would seem like a complex decision with a lot of intangible elements, it’s interesting that Twitter content by itself turned out to be predictive. Important variables included whether the athletes posted “self-promoting” tweets, “ingratiating” tweets praising specific coaches and teams, and information such as camps they attended or coaches who had visited them. Bigsby also created another logistic regression model that could predict whether the athletes would commit or “decommit” to certain teams.

Beyond athletics and higher education, the research also offers ideas for how this predictive approach could be creatively used for recruitment for all kinds of jobs.

*Photo by* [*Roman Mager*](https://unsplash.com/@roman_lazygeek?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/math?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

# Potential Issues

While these examples use data that’s pretty easy to access from LMSes or public social media, higher education data can be tough to gather and analyze in practice. Institutional silos, decentralized data, and concerns about student privacy and biases all pose challenges.

This recent [article](https://hechingerreport.org/predictive-analytics-boosting-college-graduation-rates-also-invade-privacy-and-reinforce-racial-inequities/) from The Hechinger Report covers some potential unintended consequences of using predictive analytics for student outcomes in particular. A model (and an advisor interpreting it) could steer a student away from a first-choice major that’s predicted to be too ambitious for that student … but the student might have been able to rise to the challenge. Is the model and advisor’s guidance in the student’s best interests? That’s not an easy question to answer. Questions about privacy and systemic biases also come into play.

To be sure, there are complex questions here. With care, though, there are many ways that predictive analytics can be used to help students and everyone else involved in crafting a quality higher ed experience.

For more inspiration on how to use predictive analytics, watch the video below from Educause, where some institutional leaders explain the role of predictive analytics at their institutions. You can also check out this [free e-book](https://www.alteryx.com/e-book/data-innovators-in-higher-ed?UTM_Content=community) that showcases seven different schools’ use of analytics in different areas of their institutions.