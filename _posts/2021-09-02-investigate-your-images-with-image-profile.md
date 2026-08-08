---
title: "Investigate Your Images with Image Profile"
date: 2021-09-02
excerpt: "It’s always fun to watch TV detectives notice details and solve crimes by just looking around a crime scene. Their powers of observation are dramatic and impressive (though sometimes they face a few humorous challenges along the way, depending on the…"
original_url: "https://community.alteryx.com/t5/Data-Science/Investigate-Your-Images-with-Image-Profile/ba-p/815532"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Investigate-Your-Images-with-Image-Profile/ba-p/815532](https://community.alteryx.com/t5/Data-Science/Investigate-Your-Images-with-Image-Profile/ba-p/815532)*

It’s always fun to watch TV detectives notice details and solve crimes by just looking around a crime scene. Their powers of observation are dramatic and impressive (though sometimes they face a few humorous challenges along the way, depending on the show).

![SusanCS_0-1630537382213.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200779i6BC74A0E592046ED/image-size/medium?v=v2&px=400)

Image via GIPHY

The new [Image Profile Tool](https://help.alteryx.com/20213/designer/image-profile) is also amazingly good at quickly observing the details of your images. This new addition to the Alteryx Intelligence Suite’s Computer Vision tool group quickly analyzes images, allowing you to integrate insights about them into your larger workflow. You can get information about each image’s format, its colors, where it was taken (if the [EXIF](https://photographylife.com/what-is-exif-data) data is available and includes GPS details), and a variety of summary statistics about the image. (An example of the latter is finding the standard deviation of the values of an image’s pixels to quantify the level of contrast in the image.)

You can use this information for all kinds of purposes across industries, from agriculture to retail to manufacturing. Maybe you want to know which product colors are most popular among certain segments of your customers. Maybe you want to map images by their attached location data to look for geographic patterns, and use Designer’s [Allocate](https://help.alteryx.com/20213/designer/demographic-analysis) tools to build out demographic details. Maybe you want to use the image data in a recommendation engine or an image-based search system. The “evidence” you can glean from images can enhance many projects.

![SusanCS_1-1630537377763.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200778i15FE0B4DBC7C6F5F/image-size/medium?v=v2&px=400)

Image via GIPHY

Whatever your motive, I’ll give you a quick tour of the tool and its options, and I’ll throw in a bonus for our Python fans: a way to assign human-friendly names to the images’ most frequent colors using an open-source Python package released by Stitch Fix. Plus we’ll explore a method for generating a custom visualization of those colors. Let the investigation begin!

![SusanCS_2-1630537383033.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200780iB47CD69E1F8D2516/image-size/medium?v=v2&px=400)

Image via GIPHY

## **If the Shoe Fits: Preparing the Clothing Dataset**

For this demo, I used [this dataset](https://github.com/alexeygrigorev/clothing-dataset-small) of 3,781 images of different clothing items on plain backgrounds. I brought the images into the workflow using a Directory Tool, and then used a Regex Tool to extract the type of clothing from each directory’s name, thinking that could be useful for later sorting and analysis. I then used an Image Input Tool to start off the image portion of the workflow.

I ended up using an [Image Processing Tool](https://community.alteryx.com/t5/Data-Science/Picture-Perfect-Inside-Image-Processing/ba-p/767828) before getting to the profiling step. My initial exploration of these images showed that a surprisingly large proportion had different shades of gray as a dominant color. Many of the clothes were photographed on gray backgrounds. I used the Image Processing Tool to crop the images to a 200 px square of their central regions in order to try to focus on the actual clothing pictured. That isn’t a perfect strategy; gaps between pant legs and shoes may skew the final results a little. An [object-detection](https://machinelearningmastery.com/object-recognition-with-deep-learning/) step in this process could help focus the analysis on just the clothes. But I saw more “colorful,” varied results after adding this step, so it seems to have helped.

![SusanCS_3-1630537378773.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200783iC0F83801B42C7D39/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Interrogating the Images: Image Profile at Work**

Finally, the investigator enters the scene: the Image Profile Tool, which requires minimal configuration. Just tell it which field contains your images, and which profile(s), or set of details described [here](https://help.alteryx.com/20213/designer/image-profile), you’d like to retrieve for each image.

![SusanCS_4-1630537376320.png](https://community.alteryx.com/t5/image/serverpage/image-id/200781i4F7D4DAA49AB282E/image-size/large?v=v2&px=999)

Running the workflow provides the key details of each image. The base profile includes the fields shown below and many more. Below are fields showing the most frequent color in the image, expressed in both RGB and hex formats, and the number of dark and bright pixels.

![Results.png](https://community.alteryx.com/t5/image/serverpage/image-id/200932iA77D65589479DCEA/image-size/large?v=v2&px=999)

## **Explain Yourself: Translating Color Results Into Human Terms**

No one ever says, “My favorite color is #afada6!” or “I want a shirt in a nice shade of [37, 150, 190].” What are those colors?

You might be satisfied with having the RGB and/or hex codes for your purposes. For example, you could use these RGB details to cluster images, or to match new images to these using nearest neighbors. But if it would be helpful to translate your color results into human terms and visualize their frequency, keep reading.

![SusanCS_6-1630537383363.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200786i819DC31913F1D442/image-size/medium?v=v2&px=400)

Image via GIPHY

As usual, [xkcd](https://xkcd.com/1882/) shows us the way. Results of a color-naming survey by the webcomic’s creator were integrated and enhanced in the open-source Python package colornamer, developed by the data science team at Stitch Fix. These data scientists especially need to be sure they’re making nuanced differentiations among colors for their clothing recommendations. To that end, they created a color hierarchy with specific, human-readable names and varying levels of distinctions, with palette options ranging in size from over 900 named colors to just two options (“color” or “neutral”). All the details of their process and the color palettes are shown in [the Stitch Fix blog post](https://multithreaded.stitchfix.com/blog/2020/09/02/what-color-is-this/), along with an interactive graphic of the colors.

With colornamer and just a few lines of code in a Python Tool, I was able to generate the human-friendly names of each image’s most frequent color and add those to my dataset. For example, check out the image below and its dominant color.

![coat_and_maroon_color.png](https://community.alteryx.com/t5/image/serverpage/image-id/200790iD9917C9F604FA6B9/image-size/medium?v=v2&px=400)

The Image Profile Tool tells us that the most frequent color’s RGB values are [70.72, 28.02, 37.88], and that color’s hex code is #461c25. That color is shown at right above. With colornamer, we can retrieve these names for those values, from most to least specific:

xkcd Color: dark maroon

These color names can help you filter or group your images in an easily interpreted way, and then use the images in a document or automatically generate PowerPoint slides with the Reporting tools.

![SusanCS_9-1630537377792.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200789i8A356CAEE639446E/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Getting Fancy with Custom Colors in Visualizations**

From this point, it’s pretty simple to make a plot showing how often each color was a dominant image in your image dataset. But personally, I found it discombobulating to see the colors’ names all portrayed by a single default color in the plot. (This is a great example of the [Stroop effect](https://www.simplypsychology.org/stroop-effect.html), in which our brains struggle to process incongruent stimuli!)

Fortunately, it’s not too hard to create a custom color palette based on the most frequently appearing dominant image colors and then use those in a plot. We can then simply use pandas’ built-in plotting capabilities to generate a bar plot and output its location to our workflow. (I [blogged here](https://community.alteryx.com/t5/Data-Science/Plot-Twist-Using-the-Python-Tool-for-Plotting/ba-p/584670) about getting plots out of the Python Tool.) From there, it’s easy to view and/or save the plot.

![SusanCS_10-1630537376629.png](https://community.alteryx.com/t5/image/serverpage/image-id/200787i70E5D1E97A510A1D/image-size/large?v=v2&px=999)

I plotted how often the top 10 dominant colors appeared in this dataset. There’s still a lot of gray, but looking through some images where gray dominated confirms that the actual clothes, not just the backgrounds, really are often gray. (And here I thought my own gray-themed wardrobe was an outlier.)

Keep in mind that custom color palettes may or may not be colorblindness-friendly. You can read more about that concern and find some tools and resources in [this blog post](https://community.alteryx.com/t5/Data-Science/Data-Visualization-and-Accessibility-Three-Recommended-Reads-and/ba-p/592374).

![SusanCS_11-1630537377561.gif](https://community.alteryx.com/t5/image/serverpage/image-id/200788i3938A996F809679A/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Solving with Images**

The Image Profile Tool presents cool opportunities to bring intriguing information about images into your workflows. Enjoy your own image investigation, equipped with this new inspection tool. I hope you find some exciting, arresting results!

Want to try this out? [Download the dataset](https://github.com/alexeygrigorev/clothing-dataset-small), unzip it, and grab the workflow attached to this post. Bring the dataset into the workflow using the Directory Tool. (Be sure to update the filepath in the Render Tool at the end of the workflow, too.) You'll need to be running Designer as an administrator so the Python Tool can install the colornamer package for you.

***Do you still have questions about using Image Profile? Which other tools or data science concepts would you like to see addressed here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***