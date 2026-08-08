---
title: "Picture Perfect: Inside Image Processing"
date: 2021-06-07
excerpt: "Computers may “see,” but we can help them improve their vision. Learn how images are converted into numbers and can be processed for better analysis.
Susan Currie Sivek, Ph.D.
Just now·8 min read
Scary red eyes. Overexposures. Blurry pets. My…"
original_url: "https://susansivek.medium.com/picture-perfect-inside-image-processing-3d15c04049a1"
---

*Originally published at [https://susansivek.medium.com/picture-perfect-inside-image-processing-3d15c04049a1](https://susansivek.medium.com/picture-perfect-inside-image-processing-3d15c04049a1)*

## Computers may “see,” but we can help them improve their vision. Learn how images are converted into numbers and can be processed for better analysis.

[Susan Currie Sivek, Ph.D.](https://susansivek.medium.com/?source=post_page-----3d15c04049a1--------------------------------)

[Just now·8 min read](https://susansivek.medium.com/picture-perfect-inside-image-processing-3d15c04049a1?source=post_page-----3d15c04049a1--------------------------------)

![](https://miro.medium.com/max/2560/1*Cz6lBA8C-b0AelsHAO8GrQ.jpeg)

Photo from nappy.co

Scary red eyes. Overexposures. Blurry pets. My childhood photos are full of these photographic flaws; adjusting photos on the spot wasn’t something the average person did back then. But now we all edit photos routinely — and, even more impressively, we can do it at scale, preparing many images quickly so we can extract useful information from them.

[The Computer Vision tool palette](https://community.alteryx.com/t5/Data-Science/Unlocking-Insights-from-Images-using-Computer-Vision/ba-p/754517) in the Alteryx Intelligence Suite now unites the tool previously known as PDF Input with an array of tools that make image-based data even more accessible. Because let’s face it: Many documents and images you might like to analyze are kind of like my childhood photos — fuzzy, off-kilter, or otherwise hard to decipher.

The Image Processing Tool can help us deal with these issues. Let’s take a closer look at how it operates to clean up your image inputs. Ideally, this deeper understanding will help you make the most of your Image Processing choices — and then make the most of the data in your images!

To show you how awesome this tool is, I’ve got an example for you. Check out the side-by-side comparison to get a taste of what this tool can do for your imperfect images.

Image by author

This receipt was stapled to an invoice, folded, and jammed into my purse after a recent service visit at our local Toyota dealership (yes, it really is Damian Lillard Toyota, for you basketball fans out there!). Then I took a poorly lit photo of it with my phone.

Despite such mistreatment and sad photography, Image Processing still made the receipt image tidy enough to extract nearly perfect text from it (and its mistakes are completely reasonable — it’s hard to find text where there’s an actual hole in the paper!). I then parsed the text into rows and could use it in an analysis if I wished.

Image by author

Here’s a tiny workflow to demonstrate how you can get an image into Designer and prepare it for optical character recognition (OCR), the process that extracts text from images. The Image Input tool can accept BMP, JPEG, PNG or PDF files.

Image by author

Once the Image Input tool is connected to the Image Processing tool, you’ll have quite a few configuration options for how you want to fix up your images. And since this is the Data Science Blog, we’re going to nerd out on what each of the options actually does behind the scenes.

First, let’s talk about what happens when you turn an image into data. As is probably obvious, the only way your computer has “vision” is by converting images into numbers. For the Image Processing tool, which draws on the OpenCV package, images are converted into arrays. These arrays are arrangements of numbers that represent values for each pixel in the image.

If your image measures 200 pixels by 200 pixels and is in grayscale, you will need only one number to represent each pixel. If the image is in color, you will need three numbers (“channels”) to represent each pixel, with each of the three saying how much blue, green or red (BGR) should be in the pixel to generate the color you see. (Just to keep us on our toes, OpenCV [uses the BGR color format](https://learnopencv.com/why-does-opencv-use-bgr-color-format/), not the RGB, or red/green/blue, format that may be more familiar from selecting colors with RGB values in other photo or graphics apps.) Then, each of those sets of three numbers is positioned in the array to match the configuration of the pixels in your image. Your computer translates and reassembles the various-colored pixels back into an image.

If we take the Alteryx Community logo and transform it into an array, we can pull out individual pixels and see how their BGR values translate into the colors of those pixels. For example, the location in the array that represents the pixel in row 320 and column 786 of the image (toward the bottom right-hand corner) has the BGR values [197, 129, 24].

*Bonus: Want to see how to view an image as an array or vice versa? Open the Kaggle Notebook linked below for a bit of Python code you can try with your own favorite image.*

## [Image Example](https://www.kaggle.com/susancurriesivek/image-example)

### [Explore and run machine learning code with Kaggle Notebooks | Using data from [Private Datasource]](https://www.kaggle.com/susancurriesivek/image-example)

[www.kaggle.com](https://www.kaggle.com/susancurriesivek/image-example)

If I take the second set of three numbers from the top matrix and plug them into a [color picker](https://www.w3schools.com/colors/colors_picker.asp), adjusting the order for RGB, the result looks familiar … it’s “Alteryx Blue”!

Image by author

Knowing that images are just sets of numbers to your computer is helpful to understanding how algorithms process, analyze and make predictions using images. So now, let’s get back to the Image Processing tool and look at what’s happening when you use each of its capabilities.

*Crop*

Image by author

The crop option is just like cropping an image in your everyday photography life; it removes the parts of the image you don’t want. But now that you know how the image is represented numerically, you can imagine what’s happening behind the scenes. Some of the pixels, represented by those rows and columns of numbers, are cut off of the array. Only the part representing the pixels you want is retained.

*Scale*

Image by author

This option makes your input image bigger or smaller to match the size you input. This one is a little trickier to imagine. You’re essentially telling the algorithm, “Hey, here’s this 200-pixel x 200-pixel image — but make it 400-pixel x 400-pixel.” You’re asking it to take 40,000 pixels and somehow make them into 160,000 pixels. How does the algorithm know what colors to put in all those new pixels to make your image look the same, but bigger?

The answer is [interpolation](https://en.wikipedia.org/wiki/Interpolation): generating new data that fits into the range of your known data. If you’d like to know more about which types of interpolation are used for increasing and decreasing images’ size, check out the [OpenCV documentation](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d) for this capability.

Alternatively, how does the algorithm know which pixels’ information to retain if it’s reducing the size of an image? You still need a recognizable result, so it can’t just arbitrarily pick some pixels to delete. In this case, the algorithm does an operation similar to averaging the values in the original pixels, “resampling” the image.

Want to see what these procedures’ results look like in practice? Check out [this example](https://chadrick-kwag.net/cv2-resize-interpolation-methods/).

You have the option to maintain the same aspect ratio in your rescaled images as in your originals, which will prevent distortion.

*Alignment*

Image by author

Understanding how scaling works helps us with understanding how alignment works. Essentially, the tool looks for “stable” points called “keypoints” in your image that stay the same when the image is rescaled or rotated. Once it has identified those keypoints, it is able to shift their locations collectively, as well as everything around them. (Vocabulary word of the day: This process utilizes [homography](https://en.wikipedia.org/wiki/Homography_(computer_vision)).)

Your image stays intact and recognizable, but is essentially re-aligned along new vertical and horizontal axes that have been rotated from their original position by the number of degrees you’ve input.

*Grayscale*

Image by author

Converting a color image to shades of black and white can provide better results in OCR. It can also speed up your analytic process because instead of requiring three numbers to describe each pixel, only one number is needed to express the shade of black/gray/white to be used. Amazingly enough, OpenCV makes this conversion with [a simple equation](https://docs.opencv.org/4.4.0/de/d25/imgproc_color_conversions.html):

> Gray ← 0.114\*B + 0.587\*G + 0.299\*R

Our chosen pixel from the Community logo above with the BGR values [197, 129, 24] would be represented as simply [105] if we converted the logo to grayscale.

*Thresholding*

Image by author

Thresholding is a method for removing noise in your images, creating a simplified black-and-white image and allowing your analysis to focus on the main image elements. You can see it at work in my sample image above, where the shadows and the smears of receipt-paper color were removed, dramatically improving clarity. When you apply thresholding, your image is converted into grayscale, whether or not you explicitly choose grayscale as a step in the Image Processing tool.

With the simplest thresholding method, Binary, pixels that don’t meet a certain threshold value for their shade of gray are converted to white; those that do are converted to black. Other methods can work better in certain situations; you can [read more](https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html) about them in the OpenCV documentation and see [some examples](https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html).

For my receipt image above, I used Adaptive Gaussian thresholding, which can be better when lighting varies on different portions of the image; ideally, this method would help address my shadowy, messy receipt.

*Brightness Balance*

Image by author

This option has either an Auto or a Custom mode, and as you’d expect, it makes the entire image darker or brighter.

In the Auto mode, a technique called [Yen’s method](https://ieeexplore.ieee.org/document/366472?arnumber=366472) is used. This method considers the image to have multiple segments and adjusts the intensity of their colors so that each segment is displayed at an optimal brightness. However, to minimize the computational demands, this method also considers how increasing the number of segments will also increase the number of bits required to represent the adjusted image, and it seeks a compromise between those factors. In practice, you should see good results from this method with a variety of images and different lighting conditions.

You can test out the combination and order of processing steps to see what works best for your unique set of images. Ideally you’ll find a configuration that produces clean images and, if it’s part of your workflow, reliable OCR results that feed into your analysis seamlessly.

* [OpenCV Getting and Setting Pixels](https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/) for more on how pixels are translated into colors and grayscale
* [Feature Based Image Alignment using OpenCV](https://learnopencv.com/feature-based-image-alignment-using-opencv-c-python/)
* [OpenCV Resize Image](https://www.pyimagesearch.com/2021/01/20/opencv-resize-image-cv2-resize/)
* [CV2 Resize Interpolation Methods](https://chadrick-kwag.net/cv2-resize-interpolation-methods/)
* [Image Processing with Python: Thresholding](https://datacarpentry.org/image-processing/07-thresholding/index.html)

*Originally published on the* [*Alteryx Data Science Portal*](https://community.alteryx.com/datascience?utm_source=tds)*.*