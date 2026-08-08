---
title: "Market Basket Analysis 101: An Introduction"
date: 2021-03-09
excerpt: "I cook green bean casserole just once a year. Although it’s kind of a culinary travesty, we still make it with Thanksgiving dinner for sentimental reasons. Its essential ingredients are green beans, canned cream of mushroom soup and — most important…"
original_url: "https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/bc-p/729968"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/bc-p/729968](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-101-An-Introduction/bc-p/729968)*

I cook green bean casserole just once a year. Although it’s kind of a culinary travesty, we still make it with Thanksgiving dinner for sentimental reasons. Its essential ingredients are green beans, canned cream of mushroom soup and — most important — so-called “french fried” onions (also from a can) sprinkled on top. All three ingredients often are grouped together in the grocery store around the holidays.

But how’d the grocery stores know to showcase those items together? Do they have a sentimental attachment to green bean casserole, too?

Nope, the stores are making the most of their customer data — and so can you. An analytic approach called market basket analysis reveals which items buyers purchase together. Among other purposes, this analysis can show retailers how to locate products together and how to cross-promote and recommend items that customers often put in their shopping carts at the same time. Marketing messages and promotions can highlight those items occurring together often, and key products that often relate to additional purchases can be identified. This approach works whether the stores and carts are physical or digital. Market basket analysis can also be used to analyze web browsing history, detect fraud and manage inventory.

Let’s walk through the essential concepts underlying market basket analysis here, and in [Part 2](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-102-Alteryx-Designer-Python/ba-p/662029), we’ll talk about how to make this strategy come to life with Alteryx and a bit of Python.

Image from GIPHY

## **Key Concepts for Market Basket Analysis**

Although its results are visible all around us in our lives as consumers, market basket analysis at first sounds a bit foreign: “Apriori”? “Antecedents” and “consequents”? A metric called “conviction”? Don’t worry — we’ll get through this terminology together.

First, we’ll assume that you have a dataset of transaction information where the components of each transaction are identified, like this:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Transaction 1 | Turkey | Pasta | Soda | Apples |
| Transaction 2 | Frozen pizza | Green beans | Wine | Pumpkin pie |
| Transaction 3 | Turkey | Green beans | French fried onions | Cream of mushroom soup |
| Transaction 4 | Turkey | Green beans | French fried onions | Pecan pie |

Given those data, we want to find out which items are often purchased together. (It looks like the customer for Transaction 3 has green bean casserole on the dinner menu!) We can eyeball these four transactions and see that two include turkey, green beans and french fried onions. One turkey buyer didn’t buy either of the other two items, though, and one person bought green beans and none of the other casserole ingredients.

We might guess from these four transactions that there’s some relationship among the three casserole ingredients, but it would be hard to determine if that’s the case across a much larger dataset.

The market basket approach to making that determination is to build “association rules.” The word “rule” sounds very authoritative or definitive, but really these are just statements that connect an “antecedent” item to a “consequent” item. Association rules also do not imply causal relationships, only co-occurrence, so don’t be deceived by those little arrows. In our example, we might wonder if green beans would be an antecedent item for french fried onions.

*{antecedent} ➡️ {consequent}*

*green beans ➡️ french fried onions*

To find out if that’s the case, we first create “itemsets” from our transaction data. An itemset might be *{green beans, french fried onions}*.

In our tiny dataset above, we see that two of the four transactions contain that itemset; but two also contain the itemset *{turkey, green beans}*. If we had a bigger dataset, how would we know which of those itemsets’ relationships was more important and should be the basis for, say, how we organize our grocery store? It’s even more complicated if you imagine all the possible combinations of the 10 different items included in our four transactions.

(Fun fact: The average grocery store carried 28,112 items on its shelves in 2019, [according to](https://www.fmi.org/our-research/supermarket-facts) the Food Industry Association. Even creating itemsets of 10, they would still have about 8.5 x 1037 or 84,812,357,987,507,064,681,676,153,306,904,737,896 itemsets to examine. Thank goodness for software 😉 that can help with calculations for even one department!)

What we need to do next is not only measure the frequency of the itemsets we’ve identified among all our transactions, but also to assess the strength of the associations between those items. We’ll use some different metrics for that strength, and we will “prune” (discard) the rules that don’t meet a threshold we set. The association rules that remain should have a high level of [*interestingness*](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.89.6566&rep=rep1&type=pdf) (that’s a real term!).

*Image from* [*GIPHY*](https://giphy.com/gifs/interesting-walrus-hmm-Bcnj6ObXtCNtS)

## **Metrics for Evaluating Association Rules**

There are a few different interestingness metrics you may apply to your association rules:

* **Support**: This is the easiest metric to calculate, as it’s simply the proportion of all your transactions that contain an association rule.

number of transactions with *{green beans}* *➡️* *{french fried onions}*

total number of transactions

In our dataset above, we find support for *{green beans} ➡️ {french fried onions}* is 0.5 (2 transactions out of 4). Higher numbers closer to 1 are better here.

Support is easy to calculate, but imagine trying to do this for more popular items in the store. How many people buy *{bread, eggs}* when they shop? Probably a lot. You may get a high support metric for that association rule, but it won’t add much nuance to your understanding of your customers’ habits.

Image from GIPHY

* **Confidence**: Confidence brings a bit more specificity to your judgment of this association rule. In this case, it’s the proportion of all the transactions that contain all the items in the itemset over the proportion of transactions containing just one of them. (Yes, this is the same as dividing the support metric for *{green beans} ➡️ {french fried onions}* by the support metric for just *{green beans}* alone.)

proportion of transactions with green beans

In our dataset above, 2 of 4 transactions included both items, and 3 of 4 included green beans. That’s 0.5 / 0.75, or 0.67. Again, higher numbers closer to 1 are better here.

Confidence gives us the probability that a customer will purchase the consequent, the item on the right of our association rule — the french fried onions — given that they purchased green beans, our antecedent. As you can see, this metric provides a different and perhaps more useful insight into the nature of customers’ behavior; we are getting not just frequency, but also a measure of likelihood.

Image from GIPHY

* **Lift**: Some people will buy green beans. Some will buy french fried onions. Some will buy both. If we imagine there’s no relationship between the two items, then we can see by how much we actually exceed that expectation when people *do* buy both. That calculation is called *lift*.

proportion of transactions with *{green beans} ➡️ {french fried onions}*

(proportion of transactions with *{green beans}*) \* (proportion of transactions with *{french fried onions}*)

For our mini dataset, this comes out to 0.5 / (0.75 \* 0.5) or 1.33. Here’s how you can assess lift:

* If lift is greater than 1, the antecedent is in fact increasing the likelihood of the consequent also appearing in a transaction (yes to green beans, more likely a yes to french fried onions, which is our case here).
* If lift is below 1, then it’s the opposite; the antecedent decreases the likelihood of the consequent (yes to green beans, more likely a no to french fried onions). This might be the case with products filling the same need; for example, if I buy a bottle of my usual brand of shampoo during a shopping trip, odds are I won’t buy a bottle of another brand, too.
* If lift equals 1, then the antecedent isn’t affecting the chance of buying the consequent.

The lift metric lets us know whether our assumption of “no relationship” between the items — that they are independent — is reality or not.

Want still more metrics? Support, confidence and lift are the most commonly known metrics for this analysis, and you’ll see them in the market basket tools in Designer. You may also see [leverage and conviction](https://michael.hahsler.net/research/recommender/associationrules.html) discussed on the interwebz. These are additional options for assessing the strength of the co-occurrence relationship expressed in an association rule.

## **Apriori and Eclat Algorithms for Association Rule Mining**

Clearly, those are a lot of potential calculations to carry out for many potential association rules based on many potential itemsets, if you have more than a few items. How can you expend your computational power efficiently in this process, which is often called *association rule mining*?

The most frequent approach is to apply the [*Apriori algorithm*](http://www.vldb.org/conf/1994/P487.PDF), which starts out by generating the frequent itemsets for your data with a minimum number of items *k*, which you can set. It decides which itemsets are frequent by requiring them to meet a minimum level of support (explained above). Then, those frequent itemsets are partitioned (divided) and re-combined repetitively and the support calculated for each combination, until no more itemsets can be created.

Association rules are generated from the frequent itemsets by splitting them apart into antecedents and consequents, and then the confidence for each rule is calculated. Only the association rules that meet a minimum confidence level will be retained, and the others are discarded.

The process of whittling down the itemsets (and thereby reducing the number of association rules to evaluate) is *pruning*. Pruning is important to reduce the computational demands of reviewing the data repeatedly and of calculating metrics for many potential itemsets.

The *eclat algorithm* is also used for building association rules. ECLAT is actually an acronym that stands for [Equivalence Class Clustering and bottom-up Lattice Traversal](https://sci2s.ugr.es/keel/pdf/algorithm/articulo/2000%20-%20IEEETKDE%20-%20Zaki%20-%20(Eclat)%20ScalableAlgorithms%20for%20Association%20Mining%20.pdf) (though the word *éclat* itself actually means “ostentatious display” or “dazzling effect” ... its creators set some high expectations!).

Éclat ... not the eclat algorithm. Image from

Instead of the [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) approach that the Apriori algorithm uses to identify frequent itemsets, eclat uses a [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) approach. It looks at each item, identifies the transaction IDs for the transactions in which that item appears, and makes a list of those IDs. It then looks for intersections among those lists for the various items and calculates support based on the intersections.

The eclat algorithm can be faster, but it also can be memory-intensive as it constructs and uses the lists at these intermediary steps. (For more comparison and contrast between these algorithms, check out [these slides](https://www.slideshare.net/wanaezwani/apriori-and-eclat-algorithm-in-association-rule-mining).)

Another way of limiting the number of association rules requiring analysis is *aggregating* items into larger categories prior to constructing the rules. For example, in our grocery transactions above, we could put the turkeys and pizza into a “frozen food” category, and put the two pies into a larger “desserts” category. We’d then end up with association rules that could tell us how often purchases within these larger categories coincided. However, while we’d gain efficiency in aggregating these items, we would lose detail that might be useful.

## **Analyze My Basket!**

Now that we’ve covered the core concepts you need to get into market basket analysis, we’ll take a look in [Part 2](https://community.alteryx.com/t5/Data-Science/Market-Basket-Analysis-102-Alteryx-Designer-Python/ba-p/662029) at how you can use this analytic approach in Designer. We’ll also check out some ways to visualize your results and make it easier to understand the relationships you’ve found.

[Susan Currie Sivek](https://community.alteryx.com/t5/user/viewprofilepage/user-id/143008)    
**Data Science Journalist**

Susan Currie Sivek, Ph.D., is the data science journalist for the Alteryx Community, where she explores data science concepts with a global audience. Her background in academia and social science informs her approach to investigating data and communicating complex ideas — with a dash of creativity from her training in journalism. Susan also loves getting outdoors with her dog and relaxing with some good science fiction.