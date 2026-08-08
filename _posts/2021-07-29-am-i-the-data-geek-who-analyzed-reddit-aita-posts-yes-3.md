---
title: "Am I the…Data Geek Who Analyzed Reddit AITA Posts? Yes."
date: 2021-07-29
excerpt: "It’s the dataset that’s been calling my name. I’m not quite sure what that says about me.
Ever since I heard of it, I’ve wanted to explore a dataset of Reddit posts from a well known subreddit called “Am I the Asshole?” (AITA), in which users post…"
original_url: "https://susansivek.medium.com/am-i-the-data-geek-who-analyzed-reddit-aita-posts-yes-4954a8d37055?source=user_profile---------0----------------------------"
---

*Originally published at [https://susansivek.medium.com/am-i-the-data-geek-who-analyzed-reddit-aita-posts-yes-4954a8d37055?source=user_profile---------0----------------------------](https://susansivek.medium.com/am-i-the-data-geek-who-analyzed-reddit-aita-posts-yes-4954a8d37055?source=user_profile---------0----------------------------)*

![](https://miro.medium.com/max/1400/1*6cQpkAS2aEuITCiHXoijZQ.jpeg)

*Photo by* [*Susan Q Yin*](https://unsplash.com/@syinq?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/@ssivek/likes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

It’s the dataset that’s been calling my name. I’m not quite sure what that says about me.

Ever since I heard of it, I’ve wanted to explore a [dataset](https://github.com/iterative/aita_dataset) of Reddit posts from a well known subreddit called [“Am I the Asshole?”](https://www.reddit.com/r/AmItheAsshole/) (AITA), in which users post stories of conflicts in which they weren’t sure if they did the right thing or were instead the, um, asshole. Other users comment and vote with their judgment: You’re the Asshole (YTA), Not the Asshole (NTA), Everyone Sucks Here (ESH), No Assholes Here (NAH), or Not Enough Info (INFO).

*Image via* [*GIPHY*](https://media.giphy.com/media/6RoOocJxK3Ypq/giphy.gif)

The dataset contains the text of over 97,000 posts, plus the voting outcome and the number of comments for each. In only about 27% of the cases, users rendered a judgment of either YTA or ESH, which means almost three-quarters of the cases were judged to contain no assholery. That’s actually reassuring about human nature and our tendency to worry about doing the right thing.

Though the assholes turned out to be the minority, we can dig further into this rich dataset of complicated human situations. It’s a lot of text, but we have the necessary tools in Alteryx Designer and the [Text Mining](https://help.alteryx.com/20212/designer/text-mining) palette from the [Alteryx Intelligence Suite](https://www.alteryx.com/products/alteryx-platform/intelligence-suite).

I decided to use those tools and the Data Investigation tool palette to explore interesting patterns in the AITA posts. Enjoy this slightly rude refresher on sentiment analysis, topic modeling and correlations. Maybe we’ll gain more insight into human behavior along the way.

> ***Some AITA post titles and the judgments***
>
> ***AITA…***
>
> *for wiping my dog’s drool back on him when he licks my arm? (NTA)*
>
> *for remarking on a sriracha bottle that expired in 2013? (YTA)*
>
> *for only wanting to give my Secret Santa giftee stuff for their cat? (NTA)*
>
> *for putting all the moldy dirty dishes and garbage from my roommate in her bathroom? (NTA)*
>
> *for getting upset at this game of Monopoly? (YTA)*
>
> *for hiding candy in the store so I can buy it when it’s on sale? (YTA)*

# Rush to Judgment: Text Analysis in Three Easy Steps

The dataset was pretty clean (in the data sense of the word, anyway), so I just tidied up some small text formatting issues and created a new variable for the length of the original post. I thought it would be interesting to see if the length of a post — the complexity of a situation and/or the degree to which someone felt they had to explain themselves — would correlate with the other variables.

Before doing any other processing on the text, I used the [Sentiment Analysis Tool](https://community.alteryx.com/t5/Data-Science/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153) to assess the positive, neutral or negative valence, or emotional weight, of the title and body of each post. VADER, the algorithm behind this tool, is designed to work well even on text that contains NSFW words, emojis, exaggerated punctuation!!! and other oddities in social media content. All of those should be left intact for sentiment analysis.

*Image via* [*GIPHY*](https://media.giphy.com/media/vttfd2k9qktNey2Zcp/giphy.gif)

However, prior to topic modeling, I prepared the text a bit more. The Text Pre-processing Tool took care of that big task. (Read all about it in [part one](https://community.alteryx.com/t5/Data-Science/Tokenization-and-Filtering-Stopwords-with-the-Text-Pre/ba-p/607660) and [two](https://community.alteryx.com/t5/Data-Science/Text-Normalization-in-Alteryx/ba-p/611283) of our posts on text normalization.) This tool is based on the Python NLP library [spaCy](https://github.com/explosion/spaCy), and it will normalize and filter the text. It does one weird thing: It replaces pronouns with the notation -PRON-. If you’ve spent any time on the internet, you might suspect that spaCy is referring to something other than pronouns. In reality, this abbreviation is its substitution for pronouns in text. I removed all of those notations from the titles and from the processed post text with a [REGEX\_Replace](https://help.alteryx.com/20212/designer/string-functions#regex_replace) function in a Formula Tool.

I then added the Topic Modeling Tool to the workflow and [configured it](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-2-How-to-Configure/ba-p/613596) to identify three topics in the posts. The resulting [visualization](https://community.alteryx.com/t5/Data-Science/Getting-to-the-Point-with-Topic-Modeling-Part-3-Interpreting-the/ba-p/614992) was pretty easy to interpret; check out the GIF below to see the main topics that emerged.

*Topic 1: work/job; Topic 2: romance/friendships; Topic 3: family*

Based on the lists of salient words for each topic and knowing the AITA context, the three topics could be said to represent “family issues,” “romantic/friend relationship conflicts” and “work/job problems.” The three topics are nicely separated in the Intertopic Distance Map, and the lists of words characterizing each topic make sense. The Topic Modeling Tool also adds a score for each topic to each post in the dataset, reflecting the degree to which that topic appears in the post.

It’s awesome to quickly find the major themes in more than 97,000 posts, plus analyze the sentiment within them. But did those themes and sentiment levels connect to the AITA judgments passed by users? To find out, I broke out the Data Investigation tool palette to see what we could find about patterns in these posts and the responses.

*Image via* [*GIPHY*](https://media.giphy.com/media/l1J9LVgNqSYv71Ag8/giphy-downsized.gif)

# Investigating A\*\*holery and Sentiment

The [Contingency Table Tool](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Contingency-Table/ta-p/356042) makes it easy to compare categorical variables and see how their values coincide. It’s a great way to look more closely at the sentiment analysis results and the AITA judgments. We can compare the positive or negative sentiment of the titles and posts with the “is\_asshole” variable provided in the dataset. (The is\_asshole variable is 0 if the final vote was Not the Asshole, No Assholes Here, or Not Enough Info, and 1 if the result was You’re the Asshole or Everyone Sucks Here.)

Maybe surprisingly, in terms of quantity, there wasn’t much of a difference between the emotional valence of the titles and posts that were judged to contain assholery and those that weren’t. Positive posts were actually judged YTA or ESH slightly more than negative posts.

*Post sentiment compared to asshole presence*

Digging in a little deeper with the [Association Analysis Tool](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Association-Analysis/ta-p/40459), we can check out the correlations between our sentiment valence scores, topic scoring, and the post length variable I added. I chose the “Target a field for more detailed analysis” option to get [p-values](https://community.alteryx.com/t5/Data-Science/The-Data-Science-Celebrity-Q-amp-A-Meet-P-Value-aka-p-value/ba-p/743016) for these variables’ relationship with the “is\_asshole” variable.

Here we see, somewhat surprisingly, that while negative sentiment in titles and posts didn’t have a significant correlation with assholery, *positive* sentiment in titles and posts did. So being positive about a situation maybe makes it more likely that YTA, or at least that you’ll be judged as such.

Of course, Pearson correlations are based on linear relationships between variables; we can also try the [Spearman Correlation Tool](https://help.alteryx.com/20212/designer/spearman-correlation-tool), whose calculation doesn’t assume a linear relationship. As with Pearson correlations, values closer to -1 or 1 suggest a stronger negative or positive relationship, respectively.

The Spearman correlation between positivity of post titles and is\_asshole is 0.31. The more positive the title, the more likely the judgment of assholery. (With this dataset, we have to be a little skeptical; for example, one post title with high positive valence is “best friend party potty fiasco.” VADER might be thrown off a bit by the happy sound of “best friend” and “party,” but not pick up on the concerning last two words in that title.)

*The most positive AITA post titles, originally all preceded by “AITA”*

The Spearman correlation between positivity of posts and is\_asshole is only 0.04, so titles may matter more in setting voters’ expectations (though we can’t assume there’s a causal relationship).

*Image via* [*GIPHY*](https://media.giphy.com/media/PH5B8oLFhjOLb9mIsz/giphy-downsized.gif)

# A\*\*holes at Home and Work

Enough about feelings; which topics seem to involve the most assholery? Do people tend to be judged as assholes more when they share family, romance/friendship or work situations? We can look at the correlations above for this comparison, but it’s also possible to look at these as categories. I identified which of the three topics scored highest for each post, and then compared how the topics were judged across the board. Another Contingency Table Tool revealed the comparison below.

It turns out that bad behavior is pretty evenly distributed in our lives, at least according to these scenarios and judges. The Reddit voters were slightly more lenient toward family and work situations and judged romance/friendship issues somewhat more harshly, but the proportions aren’t all that different.

*Image via* [*GIPHY*](https://media.giphy.com/media/6PAbFX7jVXWTK/giphy.gif)

# What Gets People Interested?

If you’re curious about whether YTA and want to submit your dilemma to the AITA voters, what will get people to upvote or comment on your post? The “score” variable in this dataset represents the net votes a post received (upvotes minus downvotes), and it’s naturally highly correlated with the number of comments (Pearson correlation of 0.83). Overall, there was only a mild correlation between judgments of YTA or ESH and the number of comments on the post, and very little correlation with the score.

Turns out, if you dish about your family (“topic 3” in the results above) in your post or at least write a lot, people may be slightly more likely to engage with it. But don’t write a positive-sounding title, as positivity in titles was slightly *negatively* correlated with comments and the score.

# Quantifying Human Behavior, Good and Bad

This analysis of the AITA posts shows how it’s possible to quickly distill a lot of unstructured text information into topical and emotional insights that can be analyzed in many different ways. This kind of approach could be used on your social media content, product reviews, survey responses and many other kinds of text data, and integrated into predictive models as well. Whatever your project, I hope you find that the assholes are in the minority in your data, too.

## Recommended Reading

*Originally published on the Alteryx Community* [*Data Science Blog*](https://community.alteryx.com/t5/Data-Science/Am-I-the-Data-Geek-Who-Analyzed-Reddit-AITA-Posts-Yes/ba-p/789146?utm_content=789146&utm_source=tds)*.*