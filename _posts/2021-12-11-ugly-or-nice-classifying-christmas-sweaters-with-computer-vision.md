---
title: "Ugly or Nice? Classifying Christmas Sweaters with Computer Vision"
date: 2021-12-11
excerpt: "Can we quantify the “ugly Christmas sweater”? It’s news you can use — not just for data science projects, but also for your festive fashion choices. · 6 min read If you’ve been invited to an “ugly Christmas sweater” themed party, you might wonder: Is…"
original_url: "https://medium.com/codex/ugly-or-nice-classifying-christmas-sweaters-with-computer-vision-30e5ff8bdcf7"
---

*Originally published at [https://medium.com/codex/ugly-or-nice-classifying-christmas-sweaters-with-computer-vision-30e5ff8bdcf7](https://medium.com/codex/ugly-or-nice-classifying-christmas-sweaters-with-computer-vision-30e5ff8bdcf7)*

## Can we quantify the “ugly Christmas sweater”? It’s news you can use — not just for data science projects, but also for your festive fashion choices.

· 6 min read

![](https://miro.medium.com/max/10000/0*H6g2JTd9FfWw0PF6)

Photo by on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

If you’ve been invited to an [“ugly Christmas sweater”](https://www.thedatingdivas.com/the-ultimate-ugly-sweater-party/) themed party, you might wonder: Is this sweater I picked *actually* ugly, or am I just a poor judge of fashion? Or maybe you just wear what you think is a “nice” holiday sweater. What if you then get compliments on your “ugly” choice?

Fortunately, we have the data science tools to address this dilemma! After all, it’s just a binary classification problem — “ugly” or “nice.”

![](https://miro.medium.com/max/10000/0*SwornFdVfJwQzddc?q=2)

*Image via* [*GIPHY*](https://media.giphy.com/media/10M4bOvsYKKTYI/giphy.gif)

With the Computer Vision tools in the Alteryx Intelligence Suite and a tiny bit of Python, we’ll see if we can classify sweaters correctly, and then explore whether we can quantify any characteristics that might define an “ugly Christmas sweater.” It’s timely news you can use — not just for your data science projects, but also for your festive fashion choices. (Visit the [original blog post](https://community.alteryx.com/t5/Data-Science/Ugly-or-Nice-Classifying-Christmas-Sweaters-with-Computer-Vision/ba-p/851932?utm_content=851932&utm_source=tds) to grab the attached workflow if you’d like to follow along!)

To build an ugly/nice sweater image classification model, we need many images of sweaters fitting both categories. Quickly gathering images was easy with a Python image-scraping package called [jmd\_imagescraper](https://joedockrill.github.io/jmd_imagescraper/), which collects images from the DuckDuckGo search engine based on your chosen search terms.

After some experimentation, I landed on “cute dressy Christmas sweater” as a reliable search term for more normal-looking holiday garb. Though potentially biased toward more typically feminine styles, the sample did include more masculine sweaters as well.

![](https://miro.medium.com/max/10000/0*cZBcEyvJkM-Irej4?q=2)

*A sample of the allegedly “cute” sweaters as shown in the image cleaning interface. Image by author.*

With just a few lines of code in the Python Tool, I quickly had 900 images of sweaters. The jmd\_imagescraper package also includes a convenient little utility that allows you to preview and delete duplicated or inappropriate images, which in this case included the occasional clip art images or illustrations. After some cleanup, I ended up with 752 images, almost evenly divided between the “ugly” and “nice” labels (avoiding the problem of [imbalanced data](https://community.alteryx.com/t5/Data-Science/Balancing-Act-Classification-with-Imbalanced-Data/ba-p/841878?utm_content=851932&utm_source=tds)).

![](https://miro.medium.com/max/10000/0*SnZBcCvcO_aV3rfE?q=2)

*Image via* [*GIPHY*](https://media.giphy.com/media/3oz8xwQF1zecBpmHcI/giphy-downsized.gif)*.*

With the images in hand, I was able to quickly parse their labels from the directory names generated in the scraping process, and then brought the images into the workflow through the [Image Input Tool](https://help.alteryx.com/20213/designer/image-input). (As a whole, the model-building process is similar to what I described in [this blog post](https://community.alteryx.com/t5/Data-Science/Image-Recognition-Classification-Models-Made-Simple/ba-p/802313?utm_content=851932&utm_source=tds) recently.)

I used the [Image Processing Tool](https://help.alteryx.com/20213/designer/image-processing) to make sure the images were a consistent size, though [it can do more](https://community.alteryx.com/t5/Data-Science/Picture-Perfect-Inside-Image-Processing/ba-p/767828?utm_content=851932&utm_source=tds) than just resize images. The Create Samples Tool tidily divided the images into evaluation, validation and holdout sets, and I fed the first two into the Image Recognition Tool.

After experimenting with the pre-trained model options in the [Image Recognition Tool](https://help.alteryx.com/20213/designer/image-recognition), I settled on the VGG16 option as the best performer overall. I saved the model, then used the [Predict Tool](https://help.alteryx.com/20213/designer/predict-tool) to assign labels for the holdout set. The [Contingency Table Tool](https://help.alteryx.com/20213/designer/contingency-table-tool) helped me sum up the model’s performance on that holdout set, shown in what’s basically a [confusion matrix](https://community.alteryx.com/t5/Data-Science/What-is-a-Confusion-Matrix/ba-p/537567?utm_content=851932&utm_source=tds) below. The model classified the sweaters as “ugly” or “nice” with about 79% accuracy across the board. Interestingly, it did a little bit better with the ugly sweaters.

![](https://miro.medium.com/max/10000/0*ktNm9ve3NLg5Nsbh?q=2)

*Using a Contingency Table Tool to evaluate the performance of the model on the holdout images. Image by author.*

For my personal fashion choices, I’d be pretty happy if I managed to correctly choose the “cute” option about 8 out of 10 times. Your standards may be higher.

![](https://miro.medium.com/max/10000/0*GuJkt94ikn_a3xEE?q=2)

*Image via* [*GIPHY*](https://media.giphy.com/media/TgMAkXzRxAXyyhYRWn/giphy-downsized-large.gif)

It’s hard to know what aspects of the images most influenced the model’s predictions. However, we can review the images’ characteristics with the Image Profile Tool to see if there are any interesting differences that might have shaped the original labeling of these sweaters as ugly or cute (i.e., on the websites where they were originally found). In other words, can we analyze these images quantitatively to see what characteristics correlate with considering the sweaters ugly or not?

The Image Profile Tool provides a number of characteristics for each image, such as the most frequently appearing color (as demonstrated in [this post](https://community.alteryx.com/t5/Data-Science/Investigate-Your-Images-with-Image-Profile/ba-p/815532?utm_content=851932&utm_source=tds)) and the number of bright and dark pixels.

If you picture a black-to-gray-to-white gradient, “bright pixels” are those that lean more toward the white end of the scale; brightness doesn’t refer to the specific color. However, if you think of Santa Claus’s suit and the darker red of mulled wine, the Santa suit is a brighter red. In terms of the value assigned to a specific pixel of an image, red pixels in a photo of Santa will have higher numeric values than those in a photo of mulled wine.

As it turns out, one difference between the ugly and nice sweaters is that the ugly sweater images have a statistically significant higher number of bright pixels in them, according to a quick check with the [Test of Means Tool](https://help.alteryx.com/20213/designer/test-means-tool). So if you’re looking for an ugly Christmas sweater for a party, going brighter is probably better (worse?).

![](https://miro.medium.com/max/10000/0*TTd4BkAoy0EbTp8X?q=2)

Image by author.

And when we look at the standard deviation for each of the “channels” of red, green and blue pixels in the images, we can see that the standard deviation (SD) of values for the red channel was significantly higher for the ugly sweater images (*p* < 0.001), though not for green or blue.

![](https://miro.medium.com/max/10000/0*Jbvp17s8zTXerqbL?q=2)

Image by author.

![](https://miro.medium.com/max/10000/0*WLQlv8olf-LfmjdA?q=2)

*Generated by the Plot of Means Tool to show the difference in Channel 1 Pixel Standard Deviation. Image by author.*

That significant difference means there was more variation in the display of red in those images — or in other words, either a lot of red and a little of some other color (as on the left below, with a low SD for channel 1) … or a little red and a lot of something else (as on the right below, with a high SD).

![](https://miro.medium.com/max/10000/0*1svyagLD6Lw7aUcr?q=2)

*With apologies to the chemists and cat lovers: two ugly Christmas sweaters in the image dataset. Image sources:* [*chemistry*](https://www.350yeezyshop.com/p/?iid=151464878&pr=52.99)*,* [*cats*](https://i5.walmartimages.com/asr/d0d5c380-e1c1-4822-bd33-36e263dd642d_1.b0aa46a5c5e7c43c308cf1926134fb4e.jpeg)

So perhaps one aspect of an ugly Christmas sweater is that striking use of red — either going full-on Santa red all over, or using strategic pops of red minimally for a maximally disturbing effect.

Fashion advice informed by data science? It’s fun to have a bit of algorithmic insight to inform your festive garb selection, whether you opt for “ugly” or “nice”! And, of course, you can try this approach with all sorts of image classification problems, which is something to celebrate.