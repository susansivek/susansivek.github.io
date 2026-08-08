---
title: "Data-Driven Cocktail Challenge"
date: 2021-02-25
excerpt: "\"Ready for a refresher on your pandas skills — or just ready for a refreshing drink?"
original_url: "https://medium.com/swlh/data-driven-cocktail-challenge-ae29bd4d410b"
publication: "Medium"
categories: [data-science]
---
*Originally published at [https://medium.com/swlh/data-driven-cocktail-challenge-ae29bd4d410b](https://medium.com/swlh/data-driven-cocktail-challenge-ae29bd4d410b)*

![](https://miro.medium.com/max/10000/1*WDTpJ-ZDiBEg8BCtF4qSIg.jpeg?q=20000000)

Photo by [Sara Cervera](https://unsplash.com/@saracervera?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/cocktail?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Ready for a refresher on your pandas skills — or just ready for a refreshing drink?

Pandas, the widely used Python library for data analysis and data wrangling, has an incredible variety of useful functions. If you’re new to pandas or just want to practice, this Data-Driven Cocktail Challenge will help you gain familiarity with indexing, utility functions, string functions, and more.

Be sure to refer to the [pandas documentation](https://pandas.pydata.org/docs/) for help if you need it, and, of course, Google and Stack Overflow are your friends, too.

If you want to be extra Pythonic, try to solve each step in just one line of code.

To complete the challenge, check out the image below and complete the blanks in the recipe. It’s like Mad Libs (but with a drink!).

![](https://miro.medium.com/max/10000/1*iJtiHf9RKTyBu3vnyCDhsQ.png?q=20000000)

Fill out this recipe as you work through the steps below.

If you’d rather start with a Jupyter Notebook and also see the answers in one, grab them from [Github](https://github.com/ssivek/tsds-cocktail-challenge).

# Making Your Data-Driven Cocktail

**Step 1a**Find the cocktail in the dataset that includes raspberry vodka as its first ingredient. What is the measurement for that first ingredient?

**Step 1b**Only one drink contains apricot brandy as its first ingredient and apple brandy as its second. What’s the quantity for apricot brandy?

**Step 1c**  
Only one drink is served in a highball glass and has sugar as its first ingredient. What’s the quantity for sugar?

**Step 1d**  
Only one drink is served in a punch bowl (as its “glass”) and has “apple” in its name. What’s the measurement for its first ingredient?

**Step 2a**  
First ingredient: Find the drink at index 462. What is its second ingredient?

**Step 2b**  
Second ingredient: Find the size of the cocktail dataframe. Divide the size by 93 and round the result to 0 decimal places. Find the cocktail at that index in the dataframe. What is its first ingredient?

**Step 2c**  
Third ingredient: How many drinks in the dataset are listed as “Alcoholic”?  
Find that number and subtract 29. Then identify the drink at that index in the dataset and find its fourth ingredient.

**Step 2d**  
Fourth ingredient: Three drinks have names 13 characters long that contain the word “Amaretto.” Find the third ingredient of the drink whose name is second alphabetically among those three drinks.

**Step 2e**  
Fifth ingredient: How many unique values are there for the first measurement column? Find the drink at the index for that value. Identify its third ingredient. You will need a slice of that ingredient as your final item for the recipe.

**Step 3**  
Shake or stir? How many drinks contain “stir” in their instructions? Be sure your query is not case sensitive. If the number is less than 200, use “shake” in your recipe; if 200 or more, use “stir” in the recipe.

**Step 4**  
Which kind of glass should this drink use? Find the memory in bytes used by the names of the drinks (‘strDrink’ column). What is the third digit of the resulting number? Find the drink at that index; put the same kind of glass it uses into your recipe’s instructions.

When you think you’ve got the answers, check out [this PDF](https://drive.google.com/file/d/1fjhhOSO8btHNO-_mAP-Crww2eGxu0Gno/view?usp=sharing) to see how you did, and refer to [the completed Jupyter Notebook](https://github.com/ssivek/tsds-cocktail-challenge\) for one solution!

# **An Alteryx Option**

And, a bonus: If you’re an Alteryx user, we’re featuring a two-part [Weekly](https://community.alteryx.com/t5/Weekly-Challenge/Challenge-254-DATA-DRIVEN-COCKTAIL-RECIPE-PART-1/td-p/714928) [Challenge](https://community.alteryx.com/t5/Weekly-Challenge/Challenge-255-DATA-DRIVEN-COCKTAIL-RECIPE-Part-2/td-p/718894) that will guide you through this same challenge with different steps. That version of this challenge will introduce you to some of the Alteryx predictive modeling and statistical analysis tools, too! Check it out on the [Alteryx Community](https://community.alteryx.com/t5/Weekly-Challenge/bd-p/weeklychallenge).

# Data Science Refreshment

If you enjoyed having a little fun with data science, you might also like the new Data Science Mixer podcast, best consumed with a happy hour drink and snack. Check out the show and be sure to subscribe through your favorite podcast player or the [Alteryx Community](https://community.alteryx.com/t5/Data-Science-Mixer-Podcast/bg-p/mixer)!

Check out all the episodes with this playlist!