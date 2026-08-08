---
title: "Sources Agree: Data Science Skills Go Beyond Data"
date: 2020-08-04
excerpt: "This week’s episode of the Alter Everything podcast showcases Carlene Jones, data and analytics consultant, and Nynne Haagensen, a data enthusiast who worked with Carlene. Carlene and Nyenne discuss the wide range of skills that data professionals…"
original_url: "https://community.alteryx.com/t5/Data-Science/Sources-Agree-Data-Science-Skills-Go-Beyond-Data/ba-p/613738"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Sources-Agree-Data-Science-Skills-Go-Beyond-Data/ba-p/613738](https://community.alteryx.com/t5/Data-Science/Sources-Agree-Data-Science-Skills-Go-Beyond-Data/ba-p/613738)*

[This week’s episode](https://community.alteryx.com/t5/Alter-Everything-Podcast/67-Calling-from-Copenhagen-building-a-grassroots-data-culture/ba-p/613043) of the Alter Everything podcast showcases Carlene Jones, data and analytics consultant, and Nynne Haagensen, a data enthusiast who worked with Carlene. Carlene and Nyenne discuss the wide range of skills that data professionals need, which extend well beyond the technical aspects of data manipulation and analysis. Their conversation reinforces that people skills, communication abilities and business savvy are all critical to success in data science and analytics.

To explore online conversations around this skill set, I decided to gather and analyze some data, naturally. You may have recently read the first two parts of [@SydneyF](https://community.alteryx.com/t5/user/viewprofilepage/user-id/17210)'s fantastic [topic](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-1-What-is-LDA/ba-p/611874) [modeling](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-2-How-to-Configure/ba-p/613596) trilogy here on the Data Science blog (part 3 is coming soon!). This seemed like an opportunity to apply topic modeling to what folks have discussed out there on the interwebz about the data science skill set. ([Topic Modeling](https://help.alteryx.com/current/designer/topic-modeling-tool) is part of the [Alteryx Intelligence Suite](https://community.alteryx.com/t5/Analytics/Unleashing-Advanced-Analytics-with-the-Alteryx-Intelligence/ba-p/574803), which offers some awesome new text mining tools.)

## **Gathering Opinions**

I built a workflow in Designer that scraped 64 articles from the data science site [KDnuggets](https://www.kdnuggets.com/) tagged “skills” and cleaned up the text. I also used [Text Pre-processing](https://help.alteryx.com/current/designer/text-pre-processing-tool) to quickly prep the remaining text before sending it into the [Topic Modeling](https://help.alteryx.com/current/designer/topic-modeling-tool) and [Word Cloud](https://help.alteryx.com/current/designer/word-cloud) tools. The word cloud below gives you a preview of some of the prominent ideas, but topic modeling lets us dig a little deeper.

![ds skills word cloud 2.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/126532i3E1D6137D5B0E156/image-size/large?v=1.0&px=999)

I asked the Topic Modeling tool to identify three dominant topics in the text of these articles. You should definitely read [all the details](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-1-What-is-LDA/ba-p/611874) on how this process works, but in a nutshell: This is an unsupervised approach, meaning that I’m not specifying what I want the model to find in advance, but rather letting it identify on its own the key ideas in the text of the articles. This tool assumes that each chunk of text I feed it is a mixture of those three different topics, since I asked for three. It figures out how those topics are represented in each chunk based on the probability that certain words occur together. It doesn't give a name to the topics it finds, though; it needs us to figure out what its groupings of words mean.

## **Technical Skills and More**

![ds skills topic 1.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/126529i72AFACCBF9034832/image-size/large?v=1.0&px=999)

The topic model that results from this analysis is open to interpretation, but here’s what I see. Topic 1 looks to describe the role of the data analyst or data scientist within an organization, with some technical terms mentioned (Python, SQL, Hadoop). However, it also includes concepts like “value,” “market” and “demand” that could reflect the business expertise a skilled data professional brings to the organization. Some of the chunks of original text that scored highly for the presence of Topic 1 include:

* “... a data scientist doesn't just possess technical skills, they also have domain expertise”
* “Knowing the basic principles of data science and machine learning is still required, but knowing how to apply them to your problem is even more valuable”
* “Remember, my goal wasn’t to invent a new machine learning algorithm; it was to demonstrate to a client the potential machine learning had or didn't have for their business”

![ds skills topic 2.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/126533i9BB56A17A9F6E3E3/image-size/large?v=1.0&px=999)

Topic 2 has “learning” as its most relevant term and “machine” in second place, so a quick conclusion would be that Topic 2 reflects the prominence of machine learning skills for data science. However, a closer review suggests that maybe “learning” could also be interpreted in another way. Some of the chunks of text that scored highly for Topic 2 include:

* “Apart from classroom learning, you can practice what you learned in the classroom by building an app, starting a blog, or exploring data analysis to enable you to learn more”
* “Communication problems are harder than technical problems”
* “If you're stuck on a problem, sitting and staring at code may solve it or may not. Instead talk it out in language with a teammate”

Some of the other terms included in this topic are “question,” “understand,” “team,” “approach” and “offer.” This topic seems to have a theme of ongoing learning and skill development for the data professional.

![ds skills topic 3.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/126530iFCB04D7C9B891130/image-size/large?v=1.0&px=999)

Finally, Topic 3 looks like it represents the intersection of technical skills and problem-solving, with terms “problem,” “solve,” “think,” “model,” and “code” showing up as highly relevant. “Math” also appears here, as do “research” and “concept,” suggesting some of the more specific intellectual skills useful in the data fields.

* “Machine learning can seem magical. And in some cases it is. But in the cases it’s not, it’s important to acknowledge it.”
* “There are too many data points for a human to make sense of it. It is a textbook case of death by information overload”
* “Communication skills” and “data visualization”
* “Spend time thinking about the products of the company, how your job impacts the core of the business, and a few ideas of how you would do your job to solve an important problem”
* “It’s perfectly fine if you’re overwhelmed by the skills needed (So am I!)”

## **The Human Context for Analysis**

Yes, it is a lengthy list of skills indeed! This quick analysis suggests that in discussions of data science skills, there is a recurring emphasis not just on technical skills, but on the capabilities that put data analyses into human and business contexts. The best model or analysis doesn’t mean much without humans empowered to figure out the right problem-solving strategy, the questions to ask, the methods to use and the interpretation of their results.

Learn more about how Carlene and Nynne view the skills needed for a data-driven company culture and professional success in this week’s Alter Everything episode.