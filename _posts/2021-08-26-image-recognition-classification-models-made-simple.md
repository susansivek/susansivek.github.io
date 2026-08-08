---
title: "Image Recognition: Classification Models Made Simple"
date: 2021-08-26
excerpt: "If you’ve been around American pop culture for even a little while, you can probably name the characters in the image above. With over 30 years on TV, The Simpsons has provided plenty of “training data” so we can recognize all or many characters from…"
original_url: "https://community.alteryx.com/t5/Data-Science/Image-Recognition-Classification-Models-Made-Simple/ba-p/802313"
---

*Originally published at [https://community.alteryx.com/t5/Data-Science/Image-Recognition-Classification-Models-Made-Simple/ba-p/802313](https://community.alteryx.com/t5/Data-Science/Image-Recognition-Classification-Models-Made-Simple/ba-p/802313)*

![SusanCS_0-1629150822241.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198346i190BF15172408C6F/image-size/medium?v=v2&px=400)

Image via GIPHY

If you’ve been around American pop culture for even a little while, you can probably name the characters in the image above. With over 30 years on TV, *The Simpsons* has provided plenty of “training data” so we can recognize all or many characters from the show. Plus, as humans, we’re just pretty good at interpreting images.

But to recognize images, computers need not just training data, but also a method for understanding images and predicting who or what is within them. Fortunately, with the release of Alteryx Designer 21.3, the new [Image Recognition Tool](https://help.alteryx.com/20213/designer/image-recognition) in the Intelligence Suite provides exactly that. This tool helps you build an image classification model trained on a set of labeled images with two or more classes (multiclass classification). You can then use the [Predict Tool](https://help.alteryx.com/20213/designer/predict-tool) from the Machine Learning tool group to label new images.

Let’s take a look at how we can use Image Recognition to train a model that can identify the members of the Simpson family almost as well as you and I can.

![SusanCS_1-1629150822783.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198347iE7BAE1AA0BDBCE8F/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Don’t Have a Cow, Man: Prepping and Inputting Images**

This [dataset of images](https://www.kaggle.com/mathurinache/simpsons-images) from The Simpsons is available on Kaggle, and it includes over 16,000 still images from the show, organized into training and test directories that represent 19 different characters. For simplicity, I’m using 5,637 images, each of which shows one of just four characters: Homer, Marge, Bart and Lisa. The model will try to “classify” each image as the character it thinks is shown, essentially “recognizing” that character.

I put 70% of the images into a training dataset, 20% in a validation set, and 10% in a holdout set. (For more on why this division matters, check out [this post](https://community.alteryx.com/t5/Data-Science/Holdouts-and-Cross-Validation-Why-the-Data-Used-to-Evaluate-your/ba-p/448982).) The Directory Tool makes it easy to bring in the full training and validation directories, plus their subdirectories organized by each of the four Simpsons characters. I used a Formula Tool to extract the label name (the Simpsons character shown in the image) from the name of each subdirectory and put it in a new field called “Class.” With the images organized and labels established, everything is ready for the Image Input Tool to bring in the actual image files.

![input_prep_workflow_part.png](https://community.alteryx.com/t5/image/serverpage/image-id/198545i43736B20ACB6F40C/image-size/large?v=v2&px=999)

But — “d’oh!” as Homer would say — we aren’t ready to build the model just yet. It’s important to process the images first for consistency and for compatibility with the model-building process. In particular, you may need to use the [Image Processing Tool](https://help.alteryx.com/20212/designer/image-processing) — discussed in [this blog post](https://community.alteryx.com/t5/Data-Science/Picture-Perfect-Inside-Image-Processing/ba-p/767828) — to make the images consistent in size and apply other transformations they may need. (However, don’t convert them to grayscale, as that’s not compatible with the Image Recognition Tool.) Choose a uniform size for images; the smaller your images, the faster your model will be, but it may have lower accuracy. The minimum size for images depends on the pre-trained model you choose (more on that in a moment). A good starting point is 128 x 128, and that’s what I used here. You can experiment to see which dimensions give you the best results. It’s important to apply the same processing to your training, validation and test images.

![SusanCS_3-1629150822363.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198349i6A25C1F6FDE1EC1F/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Woo-Hoo! Configuring Image Recognition**

The Image Recognition Tool comes next in the workflow, and as shown below, it requires some configuration choices. We need to specify where the training and validation images are coming from and which field in each data stream contains labels for the images.

![tool configuration.png](https://community.alteryx.com/t5/image/serverpage/image-id/198624i170A00801AACC8B6/image-size/large?v=v2&px=999)

We also have options for Epochs and Batch Size. A *batch* here is a subset of our training data, and the default in the tool is 32 images. Those 32 images are sent through the neural network that’s under construction; the error is calculated based on that group, and the model parameters updated to try to reduce error.

The number of epochs represents the number of times you want *all* the training data (in one or more batches) to be sent through the model-in-progress. The default here is 10, but you can experiment with different values to see what works best for your dataset. The idea is to run the data through the model sufficient times to find parameters that minimize error.

With 32 batches and 10 epochs, the parameters of your model will be updated 320 times; therefore, keep in mind that your workflow will take longer if you increase these numbers. Adding more epochs [can also lead](https://datascience.stackexchange.com/questions/46523/is-a-large-number-of-epochs-good-or-bad-idea-in-cnn/46534) to your model overfitting. Again, you can experiment with these options to see which combination produces the best results.

![SusanCS_5-1629150823175.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198350iED7AF50FA751F8C0/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Mmm, Models: Selecting a Pre-Trained Model**

Finally, you have a list of choices for Pre-Trained Model. The Image Recognition Tool doesn’t build a deep [convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network) model for image classification completely from scratch. You probably wouldn’t want it to, unless you have a lot of computing power and time on your hands! Instead, it uses pre-trained models built by experts who *did* have those resources, plus millions of images for training and refining their models. The pre-trained models contain existing “knowledge,” so to speak, about image features, and they can “transfer” that knowledge to analyzing your images (hence the term “[transfer learning](https://builtin.com/data-science/transfer-learning),” which is a method also used with other types of data, such as in natural language processing).

The default here is InceptionV3, but you can also choose VGG16, InceptionResNetV2, or Resnet50V2. As the Image Recognition Tool [documentation](https://help.alteryx.com/20213/designer/image-recognition) explains, each has its own advantages and disadvantages in terms of accuracy, speed and computational expense, and you’ll need to prioritize those criteria for your use case. Again, you can easily try multiple options here and see how each version of your model performs. If your images are small, be sure to note the minimum sizes required by the pre-trained models; VGG16 and ResNet50V2 require 32 x 32, and InceptionV3 and InceptionResNetV2 require 75 x 75.

Finally, in order to use your trained model for prediction on new, unlabeled images, you can include your new data and a prediction process in the same workflow, perhaps using containers to separate the parts of the process. Alternatively, you can save the model for later use in a separate workflow. To save the model, add an Output Tool after the Image Recognition Tool to put the model in a .yxdb file.

![SusanCS_6-1629150821965.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198353i82FE3D35BFF93624/image-size/medium?v=v2&px=400)

Image via GIPHY

## **Cowabunga! Training the Model and Making Predictions**

When you run your workflow, you can watch your epochs play out in the Results window. You’ll see the progress and, for each epoch, the evolving model’s performance on both your training and validation data. Often, though not always, you’ll see accuracy mostly increasing and loss mostly decreasing as the epochs proceed. This pattern shows that your model’s ability to predict the image label is improving as it repeatedly looks at the data and makes adjustments to its own parameters.

![SusanCS_7-1629150821739.png](https://community.alteryx.com/t5/image/serverpage/image-id/198351i8F32AA9B392E0A91/image-size/large?v=v2&px=999)

Want to see how all the pre-trained model options performed? Open the spoiler tag below.

Now you can use your model for prediction, either directly within the same workflow or in a separate workflow. Whichever option you choose, prior to predicting their labels, your new images for classification should be processed in the same way as your original images; in my workflow, I resized my new, unlabeled images to 128 x 128 as well.

![predict_workflow_part.png](https://community.alteryx.com/t5/image/serverpage/image-id/198547i4A3B8B39AD9E95D4/image-size/large?v=v2&px=999)

I set up a second half of my workflow that brings in the saved Image Recognition model through an Input Tool. I connected the model to the M input anchor and my holdout data to the D anchor on the Predict Tool.

I also added a bit of data tidying and analysis after the Predict Tool to assess how well my model performed on the holdout images. I added a variable to mark whether the prediction matched the original label on the image, which let me quickly see with a Filter Tool which images’ labels were predicted correctly and which weren’t.

Finally, I used a Contingency Table Tool to display what’s essentially a confusion matrix, comparing the actual and predicted labels for the images. This visualization can give you quick insight into what your model is learning and where it’s making mistakes.

![SusanCS_9-1629150821967.png](https://community.alteryx.com/t5/image/serverpage/image-id/198354i4DBC3A2FF767798A/image-size/large?v=v2&px=999)

My best-performing model used the ResNet50V2 pre-trained model, and it achieved 90% overall accuracy across all the classes (characters, in this case). It did slightly better identifying Lisa and Marge than Bart and Homer. I could experiment further with image and batch sizes, as well as the number of epochs, to see if I could get even better results. Nice work, Image Recognition!

![SusanCS_10-1629150823203.gif](https://community.alteryx.com/t5/image/serverpage/image-id/198356iDB45B0E533EA7F7A/image-size/large?v=v2&px=999)

Image via GIPHY

## **Live Action: Image Classification Applications**

What images do you have among your collections of interesting data? You may need to hand-label some images to get started, but with enough prepared examples, you can generate predictions on new data. Remember also that there are important ethical considerations to keep in mind with the use of images, especially those of people; here’s [a concise overview](https://www.gartner.com/smarterwithgartner/how-to-use-facial-recognition-technology-responsibly-and-ethically/) of some issues to consider, and there are [many](https://venturebeat.com/2021/03/28/mit-study-finds-systematic-labeling-errors-in-popular-ai-benchmark-datasets/) [more](https://arxiv.org/pdf/2011.13583.pdf) [resources](https://community.alteryx.com/t5/Data-Science-Mixer/Putting-AI-ethics-into-practice-Abhishek-Gupta/ba-p/772453) out there.

Data generated from your images can be mixed and mingled in your workflows with other data sources, as usual — which means you’ve expanded your data possibilities once again. Or, as they’d say in Springfield, “embiggened” them.

***Do you still have questions about Image Recognition? Which other tools or data science concepts would you like to see addressed here on the blog? Let me know with a comment below, and subscribe to the blog to get future articles.***

## **Recommended Reading**

***Update: By [request](https://community.alteryx.com/t5/Data-Science/Image-Recognition-Classification-Models-Made-Simple/bc-p/807531/highlight/true#M777), I've attached this workflow to the post! Please note you'll need to download the [original dataset](https://www.kaggle.com/mathurinache/simpsons-images) yourself, update the file paths included in the workflow, and have access to Intelligence Suite tools. Have fun!***