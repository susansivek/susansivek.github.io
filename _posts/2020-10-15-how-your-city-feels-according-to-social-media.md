---
title: "How Your City Feels, According to Social Media"
date: 2020-10-15
excerpt: "\"What’s the mood in your town right now? What’s the public’s attitude toward a local or state agency? Are people happy with the services they’re getting? What other needs do they have?"
original_url: "https://community.alteryx.com/t5/Data-Science/How-Your-City-Feels-According-to-Social-Media/ba-p/649518"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/How-Your-City-Feels-According-to-Social-Media/ba-p/649518](https://community.alteryx.com/t5/Data-Science/How-Your-City-Feels-According-to-Social-Media/ba-p/649518)*

What’s the mood in your town right now? What’s the public’s attitude toward a local or state agency? Are people happy with the services they’re getting? What other needs do they have?

We’ve all got our own sense of what’s going on in public opinion, but social media are a rich source of data to challenge our intuition. While national politics might seem to dominate online discussions, issues closer to home also appear in people’s daily status updates. They’re full of insights into how people are feeling about local or regional affairs.

Various social media management platforms offer their own varieties of analytics. But they don’t necessarily show you all the original data and let you dig into its nuances just how you want. Naturally, we’ve got a way to make this process easier with Designer, using tools you already know and love! Read all about it, and be sure to check out the video walkthrough and ready-to-use workflow at the bottom of this post, too.

Twitter in particular offers an easy route to downloading public posts through its API and keywords you choose. Keywords can be general, like the name of your town or state, or they can include usernames of interest, like the official accounts of agencies or services. You can dissect the relevant tweets every which way to see what themes emerge and where action may be needed. (And you can tailor this approach to your own interests; use any keywords you’re curious about in this analysis!)

Let’s look at one way to retrieve tweets and crunch through some of their significant features with Designer. (Want a different strategy? Here’s [another post](https://community.alteryx.com/t5/Engine-Works/GET-Trends-an-Example-of-Working-With-the-Twitter-API/ba-p/458971#) by ACE [@BenMoss](https://community.alteryx.com/t5/user/viewprofilepage/user-id/5143) that talks about more ways to gather tweets!)

To use this approach, you’ll need Twitter developer credentials. [Apply here](https://developer.twitter.com/en/apply-for-access) to get access. Once you have them, you’ll need to create an app, then grab your consumer API key and API secret key from [the Apps page](https://developer.twitter.com/en/apps) on the Twitter developer site.

Once you have this information, you can plug it into the [Twitter API Authorization Header macro](https://gallery.alteryx.com/#!app/Twitter-API-Authorization-Header/5bb29ea4826fd30c4cd5533e) included in the package attached to this post.

There are some limitations to Twitter’s [standard search](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview/standard), without upgrading to a paid option. You’ll only get tweets from the last seven days, and not *all* tweets during that time, but a “sample.” Twitter says those sampled results will be based “on relevance *and not completeness*” (their italics). If you need a comprehensive collection of *all* tweets related to your search terms, you’ll need to explore other options.

Also, be forewarned: You may come across some tweets that are NSFW! Even off-color content is useful for sentiment analysis — yes, the [VADER lexicon](https://github.com/cjhutto/vaderSentiment/blob/master/vaderSentiment/vader_lexicon.txt) used in our Sentiment Analysis Tool includes four-letter words and creative variations on them! — but you might need to be careful about displaying your results to others.

## Analyzing Tweets

You have a number of options for digging into the tweets’ content, depending on your interests. You can…

* Use [sentiment analysis](https://community.alteryx.com/t5/Data-Science/Try-Sentiment-Analysis-with-Designer-You-Must/ba-p/589153) to assign scores to the tweets for positive/neutral/negative content, then look more deeply at the kinds of things people make positive and negative statements about.
* Use regex to extract usernames of people involved in these discussions to locate influencers and to respond to questions and concerns.
* Create word clouds of tweet content, either for positive/negative tweets specifically or those related to a particular topic, or simply of words from all tweets, to look for recurring interests or concerns.
* Filter tweets by user location to see only what locals think (acknowledging, however, that this user-provided information is potentially inaccurate).
* Include specific usernames in your search. In the attached workflow, I look for tweets including the City of New York’s account, @nycgov.

The workflow attached to this post includes these analyses. Note that the text mining tools used are part of the [Intelligence Suite](https://www.alteryx.com/products/alteryx-platform/intelligence-suite?UTM_Content=community), so be sure to check that out if you haven’t already!

Notice that depending on how busy your search terms are, you may get different results every time you run your workflow! As you can imagine, some places, usernames and keywords are more active than others. Additionally, you are [limited](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits) in the number of tweets you can retrieve through Twitter’s free search API. You may want to cache your data when you retrieve the tweets, or output your data (then [turn it into an input](https://help.alteryx.com/current/designer/output-data-tool#convert-output-data-tool-to-input-data-tool)) to “freeze” it while you do your analysis.

## Feeling Geographical?

Another option to drill into tweets for a specific geographic area is to modify your call to the Twitter API to include latitude and longitude for a specific point, plus a radius around that point. With a Text Input Tool, you can make columns for latitude, longitude and the desired radius in miles or kilometers, potentially for multiple points (for example, to represent the major cities with your state). The retrieved tweets will be those for which the user has opted to provide geolocation information.

Feed your lat/long and radius information into a Formula Tool that builds a URL in the following pattern, replacing the numbers in the geocode section with the latitude and longitude for your point of interest:

[`https://api.twitter.com/1.1/search/tweets.json?q=&geocode=-22.912214,-43.230182,1km`](https://api.twitter.com/1.1/search/tweets.json?q=&geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent)

You will likely need to use `ToString()` to convert your latitude and longitude to strings that can be appended to the rest of the URL text, and use mi or km as the abbreviation with the radius. No spaces should appear in the resulting URL.

## Putting the Analysis to Work

Although social media posts can vary in, er, quality, you can still find useful information. Public relations outreach on various issues can be refined and targeted based on the community sentiment and major topics found in social media content. For example, regardless of the location I chose for running my sample workflow, I found plenty of discussions around pandemic concerns and specific questions that could be addressed through a city or area’s own outreach.

Area residents’ feedback on particular services or issues could be gathered and analyzed easily, even with large numbers of posts. As [this report](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3370217&download=yes) describes, getting people to respond to surveys or fill out feedback forms is challenging, but spontaneously provided, public social media reactions and opinions are a ready-to-use resource — and maybe even more authentic and honest. Social media can also provide a window into the opinions of younger people and others who may be less inclined or unable to send letters or attend public meetings.

Of course, there is a privacy concern to keep in mind here. The Twitter users whose tweets have been collected are sharing their thoughts publicly, but they don’t necessarily intend for their ideas to be gathered and analyzed. Care needs to be taken with the names and any personal details of the users whose tweets show up in analyses.

[(view in My Videos)](https://community.alteryx.com/t5/video/gallerypage/video-id/6200697961001)

Check out the workflow attached below and see what you can learn about your hometown! Comment to share how you might put this approach to work for your own area of interest.