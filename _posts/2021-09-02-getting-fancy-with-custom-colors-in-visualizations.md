---
title: "Getting Fancy with Custom Colors in Visualizations"
date: 2021-09-02
excerpt: "Use the Image Profile Tool in Alteryx Designer to quickly learn about your image dataset, then add just a few lines of Python to create a data visualization with a custom color palette It’s always fun to watch TV detectives notice details and solve…"
original_url: "https://towardsdatascience.com/investigating-images-and-customizing-colors-in-visualizations-with-python-5226c834cb65?source=user_profile---------6----------------------------&gi=f0a7e2f4b0ae"
---

*Originally published at [https://towardsdatascience.com/investigating-images-and-customizing-colors-in-visualizations-with-python-5226c834cb65?source=user_profile---------6----------------------------&gi=f0a7e2f4b0ae](https://towardsdatascience.com/investigating-images-and-customizing-colors-in-visualizations-with-python-5226c834cb65?source=user_profile---------6----------------------------&gi=f0a7e2f4b0ae)*

## Use the Image Profile Tool in Alteryx Designer to quickly learn about your image dataset, then add just a few lines of Python to create a data visualization with a custom color palette

![](https://miro.medium.com/max/1400/1*2f26dXyx_aEKV3RwCCllcg.jpeg)

[*Sam Beasley*](https://unsplash.com/@sam_beasley?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) *on* [*Unsplash*](https://unsplash.com/s/photos/colors?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

It’s always fun to watch TV detectives notice details and solve crimes by just looking around a crime scene. Their powers of observation are dramatic and impressive (though sometimes they face a few humorous challenges along the way, depending on the show).

![](https://miro.medium.com/max/800/0*JqogxBlC1UdfzlrM)

Image via [GIPHY](https://media.giphy.com/media/XLIWxLU3KsmNM3Wt8w/giphy.gif?cid=ecf05e47osgzaefdzahe8iob9yiy107zldm26750bu4xhmv7&rid=giphy.gif&ct=g)

The new [Image Profile Tool](https://help.alteryx.com/20213/designer/image-profile) is also amazingly good at quickly observing the details of your images. This new addition to the Alteryx Intelligence Suite’s Computer Vision tool group quickly analyzes images, allowing you to integrate insights about them into your larger workflow. You can get information about each image’s format, its colors, where it was taken (if the [EXIF](https://photographylife.com/what-is-exif-data) data is available and includes GPS details), and a variety of summary statistics about the image. (An example of the latter is finding the standard deviation of the values of an image’s pixels to quantify the level of contrast in the image.)

You can use this information for all kinds of purposes across industries, from agriculture to retail to manufacturing. Maybe you want to know which product colors are most popular among certain segments of your customers. Maybe you want to map images by their attached location data to look for geographic patterns, and use Designer’s [Allocate](https://help.alteryx.com/20213/designer/demographic-analysis) tools to build out demographic details. Maybe you want to use the image data in a recommendation engine or an image-based search system. The “evidence” you can glean from images can enhance many projects.

![](https://miro.medium.com/max/800/0*TAJyoEiM_MBvwHtJ)

*Image via* [*GIPHY*](https://media.giphy.com/media/1AdZhmcdYrLVopELHh/giphy.gif?cid=790b761143b03a9507b7051e0459e646db7fca60ab7c894b&rid=giphy.gif&ct=g)

Whatever your motive, I’ll give you a quick tour of the tool and its options, and I’ll throw in a bonus for our Python fans: a way to assign human-friendly names to the images’ most frequent colors using an open-source Python package released by Stitch Fix. Plus we’ll explore a method for generating a custom visualization of those colors. Let the investigation begin!

![](https://miro.medium.com/max/800/0*KMYCngHdrKEaZAy6)

*Image via* [*GIPHY*](https://media.giphy.com/media/YOjW8IpbWneVLNkRhe/giphy-downsized.gif?cid=ecf05e47yltlts8bnbt4fckygcat5bmyhj82d0qpkc94ipik&rid=giphy-downsized.gif&ct=g)

# If the Shoe Fits: Preparing the Clothing Dataset

For this demo, I used [this dataset](https://github.com/alexeygrigorev/clothing-dataset-small) of 3,781 images of different clothing items on plain backgrounds. I brought the images into the workflow using a Directory Tool, and then used a Regex Tool to extract the type of clothing from each directory’s name, thinking that could be useful for later sorting and analysis. I then used an Image Input Tool to start off the image portion of the workflow.

I ended up using an [Image Processing Tool](https://community.alteryx.com/t5/Data-Science/Picture-Perfect-Inside-Image-Processing/ba-p/767828?utm_content=815532&utm_source=tds) before getting to the profiling step. My initial exploration of these images showed that a surprisingly large proportion had different shades of gray as a dominant color. Many of the clothes were photographed on gray backgrounds. I used the Image Processing Tool to crop the images to a 200 px square of their central regions in order to try to focus on the actual clothing pictured. That isn’t a perfect strategy; gaps between pant legs and shoes may skew the final results a little. An [object-detection](https://machinelearningmastery.com/object-recognition-with-deep-learning/) step in this process could help focus the analysis on just the clothes. But I saw more “colorful,” varied results after adding this step, so it seems to have helped.

![](https://miro.medium.com/max/800/0*1H33KgfLPRtTpEHZ)

*Image via* [*GIPHY*](https://media.giphy.com/media/YRVgSMuu8QBuM9oKxN/giphy.gif?cid=ecf05e47wfrlat8ouef1jswgtubgzy520bjaewnxxrjvkma5&rid=giphy.gif&ct=g)

# Interrogating the Images: Image Profile at Work

Finally, the investigator enters the scene: the Image Profile Tool, which requires minimal configuration. Just tell it which field contains your images, and which profile(s), or set of details described [here](https://help.alteryx.com/20213/designer/image-profile), you’d like to retrieve for each image.

![](https://miro.medium.com/max/1400/0*UOuo50_grQDQlx_n)

Image by author

Running the workflow provides the key details of each image. The base profile includes the fields shown below and many more. Below are fields showing the most frequent color in the image, expressed in both RGB and hex formats, and the number of dark and bright pixels.

![](https://miro.medium.com/max/1400/1*c2qf0nyRHBMyTR0-4AtViw.png)

Image by author

# Explain Yourself: Translating Color Results Into Human Terms

No one ever says, “My favorite color is #afada6!” or “I want a shirt in a nice shade of [37, 150, 190].” What are those colors?

You might be satisfied with having the RGB and/or hex codes for your purposes. For example, you could use these RGB details to cluster images, or to match new images to these using nearest neighbors. But if it would be helpful to translate your color results into human terms and visualize their frequency, keep reading.

![](https://miro.medium.com/max/800/0*5EAyBUvtNPf0Hc-5)

*Image via* [*GIPHY*](https://media.giphy.com/media/1lyPd9XMwZpfUS5hxp/giphy-downsized.gif?cid=ecf05e47fc1plxh44z8sdisz16tqyzwwjyedcbocezgwnlqq&rid=giphy-downsized.gif&ct=g)

As usual, [xkcd](https://xkcd.com/1882/) shows us the way. Results of a color-naming survey by the webcomic’s creator were integrated and enhanced in the open-source Python package colornamer, developed by the data science team at Stitch Fix. These data scientists especially need to be sure they’re making nuanced differentiations among colors for their clothing recommendations. To that end, they created a color hierarchy with specific, human-readable names and varying levels of distinctions, with palette options ranging in size from over 900 named colors to just two options (“color” or “neutral”). All the details of their process and the color palettes are shown in [the Stitch Fix blog post](https://multithreaded.stitchfix.com/blog/2020/09/02/what-color-is-this/), along with an interactive graphic of the colors.

With colornamer and just a few lines of code in a Python Tool, I was able to generate the human-friendly names of each image’s most frequent color and add those to my dataset. For example, check out the image below and its dominant color.

![](https://miro.medium.com/max/800/0*IljBZhfo2Az15Ng5)

Image by author

The Image Profile Tool tells us that the most frequent color’s RGB values are [70.72, 28.02, 37.88], and that color’s hex code is #461c25. That color is shown at right above. With colornamer, we can retrieve these names for those values, from most to least specific:

> xkcd Color: dark maroon
>
> Design Color: Dark Burgundy
>
> Common Color: Maroon
>
> Color Family: Red Violet
>
> Color Type: Dark Color
>
> Color or Neutral: Color

These color names can help you filter or group your images in an easily interpreted way, and then use the images in a document or automatically generate PowerPoint slides with the Reporting tools.

![](https://miro.medium.com/max/800/0*GrF4-o2y8k1UbpIm)

*Image via* [*GIPHY*](https://media.giphy.com/media/Qy7JZwgK1MFlEHHvHC/giphy.gif?cid=ecf05e47xjo229lxbbx3s7yul6dr6vuv5qwp5tkmfg113t3v&rid=giphy.gif&ct=g)

From this point, it’s pretty simple to make a plot showing how often each color was a dominant image in your image dataset. But personally, I found it discombobulating to see the colors’ names all portrayed by a single default color in the plot. (This is a great example of the [Stroop effect](https://www.simplypsychology.org/stroop-effect.html), in which our brains struggle to process incongruent stimuli!)

Fortunately, it’s not too hard to create a custom color palette based on the most frequently appearing dominant image colors and then use those in a plot. We can then simply use pandas’ built-in plotting capabilities to generate a bar plot and output its location to our workflow. (I [blogged here](https://community.alteryx.com/t5/Data-Science/Plot-Twist-Using-the-Python-Tool-for-Plotting/ba-p/584670?utm_content=815532&utm_source=tds) about getting plots out of the Python Tool.) From there, it’s easy to view and/or save the plot.

![](https://miro.medium.com/max/1400/0*BdLFCt3rOGq7heKI)

Image by author

I plotted how often the top 10 dominant colors appeared in this dataset. There’s still a lot of gray, but looking through some images where gray dominated confirms that the actual clothes, not just the backgrounds, really are often gray. (And here I thought my own gray-themed wardrobe was an outlier.)

Keep in mind that custom color palettes may or may not be colorblindness-friendly. You can read more about that concern and find some tools and resources in [this blog post](https://community.alteryx.com/t5/Data-Science/Data-Visualization-and-Accessibility-Three-Recommended-Reads-and/ba-p/592374).

![](https://miro.medium.com/max/800/0*-TCZPzeKIdCHbg6t)

*Image via* [*GIPHY*](https://media.giphy.com/media/t9lPSqrGSc1IOnajTz/giphy.gif?cid=790b7611654a178fbea0d767628f504fe65fa43c803b5006&rid=giphy.gif&ct=g)

# Solving with Images

The Image Profile Tool presents cool opportunities to bring intriguing information about images into your workflows. Enjoy your own image investigation, equipped with this new inspection tool. I hope you find some exciting, arresting results!

Want to try this out? [Download the dataset](https://github.com/alexeygrigorev/clothing-dataset-small), unzip it, and grab the workflow attached to [this post as originally published](https://community.alteryx.com/t5/Data-Science/Investigate-Your-Images-with-Image-Profile/ba-p/815532) on the Alteryx Community. Bring the dataset into the workflow using the Directory Tool. (Be sure to update the filepath in the Render Tool at the end of the workflow, too.) You’ll need to be running Designer as an administrator so the Python Tool can install the colornamer package for you.