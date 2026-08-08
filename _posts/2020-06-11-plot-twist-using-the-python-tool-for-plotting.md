---
title: "Plot Twist: Using the Python Tool for Plotting"
date: 2020-06-11
excerpt: "(view in My Videos)
Designer’s awesome tools offer lots of options for plots, tables, and images. But if you’re a pro with -- or just curious about! -- Python plotting tools like matplotlib or seaborn, it’s relatively easy to create your plots in the…"
original_url: "https://community.alteryx.com/t5/Data-Science/Plot-Twist-Using-the-Python-Tool-for-Plotting/ba-p/584670"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Plot-Twist-Using-the-Python-Tool-for-Plotting/ba-p/584670](https://community.alteryx.com/t5/Data-Science/Plot-Twist-Using-the-Python-Tool-for-Plotting/ba-p/584670)*

[(view in My Videos)](https://community.alteryx.com/t5/video/gallerypage/video-id/6162531099001)

Designer’s awesome tools offer lots of options for plots, tables, and images. But if you’re a pro with -- or just curious about! -- Python plotting tools like `matplotlib` or `seaborn`, it’s relatively easy to create your plots in the Python Tool, then extract images from the tool in Designer.

This capability adds even more flexibility to Designer’s already robust plotting options. While you can make many kinds of plots quickly and easily with built-in Designer tools, you can also customize plots as much as your heart desires by adding a bit of Python.

## Create Your Plot

I’ve generated a quick example using [a dataset from Kaggle](https://www.kaggle.com/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney) of TV shows available on four popular streaming services. I explored the question: *How many shows for different age groups does each streaming service offer?* Maybe we’d like to know which service offers more shows for younger viewers ... or maybe we don’t care about kid-friendly content and just want the grittier, grown-up stuff!

I made a stacked bar plot that displays the number of shows for each age group available from each streaming service.

![SusanCS_0-1591118083511.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/116211i7566F0039621FE7C/image-size/large?v=1.0&px=999)

Here’s the code that generated this plot, using the dataframe `df3` as its source. In this case, I’m using `pandas`’ built-in plotting, which is a wrapper on `matplotlib`.

```
colors = ["#5a61c5", "#ffc6c3", "#05dcac", "#b6fbaf"] # choose custom colors
final_plot = df3.plot.bar(stacked=True, color=colors, figsize=(12, 10)) # create plot
plt.xticks(rotation=30) # rotate x-axis ticks
plt.title("Shows on Streaming Services by Recommended Viewer Age") # add plot title
plt.xlabel("Minimum Age of Viewer") # add label to x-axis
plt.ylabel("Number of Shows Available on Service") # add label to y-axis
```

## Save the Plot and Retrieve in Your Workflow

Once you’ve customized your perfect plot, you’ll want to save it to a file. When you run a Designer workflow, a [new temporary folder](https://help.alteryx.com/current/TempFiles.htm) is created, and temporary files for that workflow are saved to that directory. There’s a workflow constant, `Engine.TempFilePath`, that contains that directory’s path.

We can access that constant within the Python Tool to generate a file path to the plot’s new home, where it will be saved as `plot.png`. We’ll then put that file path into a super-simple dataframe -- just one column containing the text of the file path -- since the Python Tool has to output a dataframe.

```
# get Alteryx temporary folder and create file path to save plot, using file name plot.png
chart_path = Alteryx.getWorkflowConstant("Engine.TempFilePath") + 'plot.png'

# replace backslashes in file path with forward slashes; display path
chart_path = chart_path.replace('\\', '/')
print(chart_path)

# save plot to chart_path 
final_plot.figure.savefig(chart_path)

# write file path and file name as a dataframe to output anchor #1
# dataframe will have one column, chart_path, with type V_WString and length 999,999
Alteryx.write(pd.DataFrame([chart_path], columns = ['chart_path']), 1, 
              {'chart_path':{'type':'V_WString','length': 999999}})
```

Outside the Python Tool, we’ll use the [Image Tool](https://community.alteryx.com/t5/Alteryx-Designer-Knowledge-Base/Tool-Mastery-Image/ta-p/49546) to grab the file path coming out of the Python Tool output, and add a Browse Tool to it so we can view our plot within Designer.

![SusanCS_1-1591118083536.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/116210i12EF42B8FD711868/image-size/large?v=1.0&px=999)

Image Tool settings

And voilà! The plot renders in the Browse Tool’s Report tab.

![SusanCS_2-1591118083552.png](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/116212i7BCBC7A27965877C/image-size/large?v=1.0&px=999)

Plot on the left, visible in the Browse Tool’s Report tab; workflow at top right, with the tiny dataframe output from the Python Tool shown in the Results window at bottom right.

If you want to learn more about Python plotting libraries, check out more details on `matplotlib` (especially the [gallery](https://matplotlib.org/gallery/index.html) of sample plots and code). Built on top of `matplotlib`, `seaborn` offers still more options, as shown by its [gallery](https://seaborn.pydata.org/examples/index.html). R users wanting to experiment with some Python might especially appreciate `plotnine`, which uses a [“grammar of graphics”](https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149) approach similar to R's `ggplot2`.

Give this approach a try to expand your plotting options and customize your data visualizations even further.