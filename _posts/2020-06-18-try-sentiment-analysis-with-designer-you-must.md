---
title: "Try Sentiment Analysis with Designer, You Must"
date: 2020-06-18
excerpt: "\"Does it mean the writer thinks Vader is actually evil? Or do the emoji add a hint of sarcasm and admiration, suggesting the writer maybe thinks he’s ... kind of cool?"
original_url: "https://community.alteryx.com/t5/Data-Science/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153](https://community.alteryx.com/t5/Data-Science/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153)*

Does it mean the writer thinks Vader is *actually* evil? Or do the emoji add a hint of sarcasm and admiration, suggesting the writer maybe thinks he’s ... kind of cool?

Understanding the nuances of text is hard for humans, and even more so for algorithms. Despite the challenge, identifying feelings in text data can be incredibly helpful. Maybe you want to make sure customers are happy with your products and services. Maybe you want to figure out what people are saying about your company on social media and whether it’s positive or negative. Or maybe you want to find customer email inquiries that are especially pleased or upset to provide them special attention. Sentiment analysis is exactly what you need to explore these issues.

It sounds complicated, but don’t worry! You’ll quickly become a sentiment analysis Jedi. With the release of the [Alteryx Intelligence Suite](https://www.alteryx.com/products/alteryx-platform/intelligence-suite) and its text mining tools (check out this [video demo](https://www.youtube.com/watch?reload=9&v=40iYJe_zd2A) for a comprehensive look), you can explore all that tricky text data. And don’t worry -- this post’s theme will make sense very soon.

## **The Basics of Sentiment Analysis**

> *“In a dark place we find ourselves, and a little more knowledge lights our way.” - Yoda*

The idea of using computers to identify emotion in human-generated text has been around for a long time. The availability of online customer reviews and the capability to process large-scale text data really boosted this effort, however. According to [one study](https://arxiv.org/pdf/1612.01556.pdf), the number of scholarly research papers on sentiment analysis grew by a factor of 50 between 2005 and 2016 (and, fun fact: that study used [topic modeling](https://help.alteryx.com/current/designer/topic-modeling-tool) to understand the history of sentiment analysis, which is available in another new Intelligence Suite tool).

Social media content added a new type of text to study that presented new challenges. In small amounts of text like tweets, there are fewer “context clues” for extracting meaning. We also use language differently in social media, plus emoji. (If you’ve ever been surprised to find out what particular emoji might *actually* mean, especially among younger folks...well, imagine how confusing that can be for algorithms.)

The algorithm used by the [Sentiment Analysis tool](http://downloads.alteryx.com/betawh_xnext/SentimentAnalysis.htm) in the Intelligence Suite is called [VADER](https://github.com/cjhutto/vaderSentiment): the Valence Aware Dictionary for sEntiment Reasoner. (Clearly it was a bit of a challenge to get that acronym, but so worth it.) VADER’s first version was released in 2014, and [this paper](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM14/paper/download/8109/8122) explains it in detail; it’s now been integrated into the `nltk` Python package. As its authors note, VADER builds upon previous approaches like the Linguistic Inquiry and Word Count lexicon (yep, that’s LIWC, pronounced “Luke” … see a theme here?).

Yes. That Luke.

A “lexicon” in sentiment analysis is a list of words judged by humans to be positive or negative (their “valence”), each with a score (“magnitude”) representing their relative intensity. In part, VADER uses a lexicon; for example, “OK" has a positive valence of 0.9, while “good" gets a positive valence of 1.9 and “great” scores a 3.1. The researchers determined these valences after gathering thousands of human ratings from [Amazon Mechanical Turk](https://www.mturk.com/) workers.

In addition to its lexicon, VADER also uses a set of five rules reflecting how humans use grammar, punctuation, and syntax to amplify their expressions’ emotional intensity. For example, the sentence “Star Wars is awesome!!!” would be rated as more positive than “Star Wars is awesome.” The same is true for capitalization used for emphasis.

Another challenge in sentiment analysis is negation. A reviewer who says “The latest Star Wars movie wasn’t great” is actually giving a negative opinion, despite the presence of the word “great.” VADER can account for that nuance because it understands how “not” works subtly in everyday language.

*That added “oooooooo” would tell VADER that this is a more extreme expression of sentiment.* 😆

Combining its sentiment lexicon and its rules, VADER can perform as well or better than human raters and other classifier algorithms in sorting social media content into positive, negative, or neutral categories, according to its creators. VADER’s creators attribute much of this success to humans’ input into the creation of the lexicon and rules: “Our results highlight the gains to be made in computer science when the human is incorporated as a central part of the development process.”

You don’t need training data to use VADER; instead, VADER simply applies its knowledge of words’ emotional valence and its rules to your text. And, yes, it can understand emoticons 🙂 and [UTF-8 emoji](https://github.com/cjhutto/vaderSentiment/blob/master/additional_resources/emoji-test.txt), which are included in its lexicon. 🤩

It’s important to note that although VADER is great at mimicking human raters in its analysis, it unfortunately might mimic and perpetuate human biases as well. VADER and other sentiment analysis algorithms may score and classify text in ways that reflect [gender, political, or racial bias](https://www.fatml.org/media/documents/darling_or_babygirl_stylistic_bias.pdf) or [age bias](https://dl.acm.org/doi/pdf/10.1145/3173574.3173986). Good [“algorithmic hygiene”](https://www.brookings.edu/research/algorithmic-bias-detection-and-mitigation-best-practices-and-policies-to-reduce-consumer-harms/) means continually monitoring our analyses’ potential for bias and ensuring equitable use of our results.

## **Trying the Sentiment Analysis Tool in Designer**

> *"Do or do not. There is no try." - Yoda*

[(view in My Videos)](https://community.alteryx.com/t5/video/gallerypage/video-id/6165407366001)

The video above shows you a walkthrough of the new Sentiment Analysis tool in a workflow that analyzes text from clothing reviews. The tool is easy to use and offers a quick path to new insights. I find it incredibly fun to see how text is so rapidly interpreted, and how you can easily connect those interpretations to other aspects of your data.

Configuration options for the Sentiment Analysis tool.

The [documentation](https://help.alteryx.com/current/designer/sentiment-analysis-tool) for this tool is super clear, so I’ll just highlight a few key points. First, notice that VADER works best on the sentence level. If you have sentences in your text data with end punctuation, you’ll want to choose “Find Sentiment at Sentence Level.” Also, if you have full sentences, don’t remove punctuation during your data cleansing and text pre-processing if your intent is to run sentiment analysis later. If there are multiple sentences in each chunk of text you want to analyze (e.g., multi-sentence product reviews), VADER will calculate a score for each sentence and combine them to provide a final score for that entire chunk. (This approach makes a lot of sense when you think about how humans write text like reviews: “This product looked great online. I was disappointed when I saw it in person. However, it turned out to be great.” Positive, negative, positive -- what a roller coaster of emotion!)

Do you care more about nuanced scoring of your text’s emotional content, or more about the overall takeaway it conveys? If the latter, you might want to check “Output Categorical Sentiment,” which will add to your results a simple classification of “positive,” “neutral,” or “negative” for each text item you have analyzed. You can fine-tune how those categories are determined using the Max Negative Classification and Min Positive Classification settings.

After you run your analysis, you’ll see positive, neutral, and negative scores for each chunk of text. These scores each range from 0 to 1, with scores closer to 1 representing more of that sentiment. These are based on the words’ valences as recorded in VADER’s lexicon, plus adjustments from its rules (like the ones for ALL CAPS!!! and emotional punctuation). The compound sentiment score ranges from -1 to 1, with -1 the most negative and 1 the most positive, with a score of 0 representing -- you guessed it -- neutral. Finally, if you chose to use it, you’ll see the categorical sentiment classification, which is generated based on the Max Negative Classification and Min Positive Classification settings.

Here’s a sample review of a shirt from my dataset to illustrate:

Review text: *Gorgeous top, very nice detail work, soft and flattering. I don't think it's too* *full on the bottom at all - mine has a loose but pretty straight silhouette. Word of warning: soft pink is not pink. It is peach with some pink - and definitely not my color.*

Negative sentiment: 0.081

Neutral sentiment: 0.692

Positive sentiment: 0.227

Compound sentiment score: 0.262

This review is pretty even-handed; it says some good things, but also has some cautions for other shoppers. The classification as “neutral” overall seems fair, and we can see how a compound sentiment score on the positive side -- but not highly so -- makes a lot of sense.

## **Using Insights from Sentiment Analysis**

> *"Your focus determines your reality." - Qui-Gon Jinn*

What can you do with your sentiment-analyzed text data? As in my example here, maybe you want to see which products are getting the most positive and negative reviews, with a little more sophistication than a simple star-based review, and quickly find patterns in the praise and complaints. For social media data, maybe you want to identify recurring themes in positive and negative public discussions of your company (or your competitors) that could be useful for campaigns or strategy. For customer email inquiries, maybe especially fiery ones could be more quickly escalated to representatives with more authority to quickly resolve issues.

Whatever your particular application, the Sentiment Analysis tool is a new way to find all kinds of harder-to-access insights. And, hey, another awesome analytic approach might make you say, “This is SO FUN!!! 😃” -- which VADER would give a very positive score.

The end.