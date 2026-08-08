---
title: "Adventures in Data: Exploratory Data Analysis"
date: 2020-03-26
excerpt: "\"It can be so tempting. You finally have that dataset you’ve been longing for. Its secrets and insights are just sitting there waiting for you. You want to start running your analysis right away and find the amazingness within."
original_url: "https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267](https://community.alteryx.com/t5/Data-Science/Adventures-in-Data-Exploratory-Data-Analysis/ba-p/545267)*

It can be so tempting. You finally have that dataset you’ve been longing for. Its secrets and insights are just sitting there waiting for you. You want to start running your analysis right away and find the amazingness within.

But wait. Take a breath. Prepare yourself, because instead of jumping right in, we’re going on a little journey through your data. But it’ll be a great adventure with a lot to see along the way!

Investing the time to deeply explore your data is worthwhile in itself, and it can save you time and trouble later on. Exploratory data analysis (EDA) is the name for this effort, and it's a critical part of [the data science lifecycle](https://community.alteryx.com/t5/Data-Science-Blog/The-Data-Science-Lifecycle/ba-p/408625). It usually includes checking specific aspects of your data, investigating it numerically and visually, and identifying potential issues before continuing your analysis. It may sound boring, but EDA pays off. There are some terrific tools in Designer (and Python and R) to empower your exploration.

### **Waypoints on Your EDA Journey**

Here are some waypoints to guide your EDA process.

* Figure out your **data cleansing and wrangling strategy**. Your EDA process can show you where data might need to be tidied up, where it might be necessary to [one-hot encode](https://bambielli.com/til/2018-02-11-one-hot-encoding/) a categorical variable, or where you might like to use binning to make categories for a numerical variable. (An example of binning is converting ages into age ranges; the Tile and Multi-Field Binning tools in Designer can help).

* Look for **weird data points** that may need to be corrected or omitted. These could be outliers you want to delete or ignore. Sometimes outliers are just data entry errors -- someone typed 1,000 but meant 100. Other times, they reveal unexpected elements you may want to investigate further. Some statistical and machine learning methods are “robust” to outliers, meaning your results won’t be too affected by them. Still, you’ll want to look at them closely, and make an informed decision about whether they should get corrected, be left alone, be deleted or get adjusted. [Read more](https://statisticsbyjim.com/basics/remove-outliers/) about handling outliers.

* Check your **data types**. I may be the only one who sees it when I try to find a mean for string-formatted data, but I still cringe a little! Avoid wasting time later by verifying all your data types right away during EDA.

* Contend with **missing data**. You might notice missing data -- empty cells, zeroes and/or nulls -- for one variable or across your dataset. Dealing with missing data deserves its own article ([here’s one](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/)), but the first step is to know you have a missing-data problem. You run the risk of developing faulty conclusions if you don’t deal with missing data appropriately.

* Watch for **important patterns**. Some initial visual investigation of your data -- as with histograms or scatterplots -- will quickly reveal intriguing trends and relationships (or their absence). You may also want to see whether numerical variables show something fairly close to a normal distribution (the familiar bell curve) and whether categorical variables show even distribution among categories (“balanced classes”). Some statistical and machine learning approaches can be thrown off more than others by skewed or imbalanced data. There are lots of methods for dealing with this situation, including [transforming data](https://medium.com/@ODSC/transforming-skewed-data-for-machine-learning-90e6cc364b0) numerically or [over-/under-sampling](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html) certain categories.

* Think of even **more interesting questions**. You’re already brimming with questions to ask of your data, but this EDA process will spur even more curiosity! You’ll notice intriguing things as you explore, which will only enrich your analytic adventure.

[](https://media.giphy.com/media/14bWswbeWGzYEo/giphy.gif)

You’ve got two main approaches for EDA -- visual and non-visual (numerical) -- and you’ll use a combination of both to get to know your data. Before you launch into these, I’d recommend just .... staring at your data. Scroll up and down, side to side -- what’s going on in this dataset? This is the low-tech approach; just zone out and let your brain soak in data for a few minutes. You won’t look at every cell, of course, but you may notice some things popping out that warrant investigation, even before you launch into more formal analysis.

**Numerical Exploration**

Let’s deal with numbers first. Check out the measures of central tendency: our old friends, mean, median and mode. Take a gander at minimum and maximum values for numerical variables. Do they look reasonable? This is an opportunity to spot outliers; Is the minimum bizarrely tiny? The mean way different from what's expected?

Also, look at the standard deviation for numerical variables, which tells you how spread out your data are, i.e., how much variation there is. The handy thing about standard deviation is that it's in the same units as your original measurement so you can interpret it easily. (Here's a [helpful resource](https://www.mathsisfun.com/data/standard-deviation.html) on standard deviation. Extra motivation: It includes dogs.)

You’ll want to check out correlations among your different variables -- both how the predictors relate to your target/outcome variable, and how the predictors relate to each other. You can look at raw numbers (such as the R2 values), checking for numbers closer to 1 that show where higher correlations (meaning, stronger relationships) exist between variables. You can also look at a correlation matrix, a visual representation that overlays your variables with themselves in a color-coded grid; color intensity usually reflects correlation level. (You can generate one in Designer with the [Association Analysis](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Association-Analysis/ta-p/40459) tool.)

However you look for them, these correlations are super important to understand. You may want to remove predictor variables that are correlated with each other from your modeling. There are many [different methods](http://www.biostat.jhsph.edu/~iruczins/teaching/jf/ch10.pdf) for choosing the best set of predictor variables for your model (aka feature selection), and there are other approaches you can take (such as [principal components analysis](https://help.alteryx.com/current/Principal_Components.htm) or PCA).

**Visual Exploration**

In addition to correlation matrices, you have other visual options for EDA. Two familiar tools are the histogram (aka bar chart) and the scatterplot.

A histogram shows how your data are distributed across different numerical values or categories. You can see whether your data fit the “bell curve” of a normal distribution, whether they are skewed higher or lower, or whether one or a few categories are over- or underrepresented in your dataset.

A scatterplot usually maps two variables as points positioned on an X and Y axis, showing how variables are related to each other. (You might make the points different colors to represent a third variable.) Scatterplots reveal whether variables are correlated, and can also show clusters in your data. You might also see a clear linear or curvilinear relationship reflected in the massed shape of the points on the plot.

[](https://media.giphy.com/media/fnHxVS8gD2Z0SBFuYn/giphy.gif)

But wait, there’s another plot to consider! Box plots are also nifty for understanding at a glance what numerical data look like, and they combine some of the intriguing items described above. A box plot contains a box (surprising, no?) that indicates the edges of the first and third quartile of values for this variable (in other words, the middle 50%, or everything from the 25th percentile to the 75th percentile). A line across the middle of the box indicates the median.

[](https://media.giphy.com/media/mtLsfrEXntTXO/giphy.gif)

You might remember hearing about a “box-and-whiskers plot” in school, which adds a twist. Whiskers can be used in different ways, including to indicate maximum/minimum values or to show one standard deviation above/below the mean. Finally, dots or stars outside the ends of the whiskers represent outliers. As a whole, once you get used to looking at them, box plots provide a terrific visual shorthand for understanding your data at a glance.

Depending on your favorite tools, you have options for the EDA portion of your analysis process.

**Alteryx Designer**

Designer offers a fantastic way to quickly view your dataset’s overall profile with the new holistic data profiling feature, available on the Browse tool anywhere in your workflow. [Check out](https://community.alteryx.com/t5/Analytics-Blog/A-360-View-of-Your-Data-Set-With-Holistic-Data-Profiling-in-2020/ba-p/539648) this full description and example. You can review not just the results window, but also see a summary in the left-hand pane for every. single. variable.

When a particular variable looks interesting (or, um, somehow wrong), click its name to take a closer look. You’ll then see the data quality (including numbers of uniques, blanks, and nulls), min/max and average values, shortest and longest values, and quantity of values with leading or trailing whitespace. You’ll get a quick histogram and a list of top values for the variable. The workflow and data shown below are in the files attached to this post.

**Python**

If you’re working with data in Python, you're likely using pandas. If so, let me introduce you to my friend [pandas\_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/). Here’s [an example](https://pandas-profiling.github.io/pandas-profiling/examples/census/census_report.html) of what this package can do with just the line `df.profile_report()`. You’ll get a quick summary of many dataset characteristics mentioned above (counts of uniques, missing data, mean, minimum/maximum, both across the dataset and by each variable). You’ll see a histogram for each variable, laid out according to pandas\_profiling’s best guess for the format that makes sense for that variable.

Other fun items in the report include a visualization of variables’ interaction, like an abstracted scatterplot, and a correlation matrix. There’s a cool display of how data is missing across your dataset, available in four formats. Finally, you’ll see the 10 first and last rows of the dataset to glimpse your data *au naturale.*

I’ve set up a notebook with a quick example of what you might see when you put a raw dataset -- that is admittedly very messy -- into pandas\_profiling. You can find it and a sample HTML report in the zipped file attached to this post.

Of course, there are many great Python visualization packages that can introduce you to your data efficiently. Matplotlib and Plotly are standbys for many, and packages like Folium can be useful for geospatial data.

**R**

If you’re an R fan instead, you’ve got even more options. I’ve set up R notebooks that each show one EDA package at work, all with the same data used above. I chose [DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/index.html), [explore](https://cran.r-project.org/web/packages/explore/index.html), and [dataMaid](https://cran.r-project.org/web/packages/dataMaid/index.html), but other popular possibilities are [arsenal](https://cran.r-project.org/web/packages/arsenal/index.html), [exploreR](https://cran.r-project.org/web/packages/exploreR/index.html), [funModeling](https://cran.r-project.org/web/packages/funModeling/index.html), [summarytools](https://cran.r-project.org/web/packages/summarytools/index.html), [SmartEDA](https://cran.r-project.org/web/packages/SmartEDA/index.html), and [inspectdf](https://cran.r-project.org/web/packages/inspectdf/index.html). For more info, check out [this detailed exploration](https://arxiv.org/pdf/1904.02101.pdf).

Each of the three packages has its strengths. Much like pandas\_profiling in Python described above, DataExplorer creates univariate histograms, a correlation matrix, and even a potential use of PCA (principal components analysis) to reduce the number of predictor variables. dataMaid is similar; it offers options to generate both a comprehensive dataset report and/or statistics and visualizations for all or selected variables. Explore() creates a fun, interactive Shiny interface that even includes a decision tree (though beware if your data is as messy as mine -- initial results are not to be trusted!). The bit of code below is all you need to see this nifty view of your data.

```
install.packages(explore)
library(explore)
explore(df) # generate report
```

Want to learn more? Notebooks for all three of these tools, plus PDFs of sample reports from DataExplorer and dataMaid, are in the zipped file attached to this post.

### **Equipped for the EDA Adventure**

Whichever tool you choose, EDA is a critical first step in your analysis. Just like when you’re cooking, no matter how hungry you are, you can’t just start throwing ingredients into a pot and hope for the best. You’ll want to understand the ingredients and recipe. I’ve been that person, standing in the kitchen with a bowl full of cookie dough, excited to have warm, fresh cookies -- but who forgot to preheat the oven, that necessary first step in the process!

Enjoy the adventure through your data that EDA offers. It should be a delightful adventure with these tools at hand.