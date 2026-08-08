---
title: "LLMs Alone Won’t Solve Your Business’s Predictive Needs"
date: 2023-12-08
excerpt: "In a nutshell: Large language models (LLMs) aren't suitable for all predictive tasks in businesses. LLMs are designed for words, not numbers, and are inefficient for analyzing numerical, tabular data. Traditional machine learning models are better…"
original_url: "https://www.pecan.ai/blog/llm-prediction-business/"
---

*Originally published at [https://www.pecan.ai/blog/llm-prediction-business/](https://www.pecan.ai/blog/llm-prediction-business/)*

**In a nutshell:**

* Large language models (LLMs) aren't suitable for all predictive tasks in businesses.
* LLMs are designed for words, not numbers, and are inefficient for analyzing numerical, tabular data.
* Traditional [machine learning](https://www.pecan.ai/blog/steps-machine-learning-for-marketing) models are better suited for predictive tasks using numerical data.
* LLMs lack interpretability and explainability, making them challenging to optimize for specific business needs.
* Pecan's [Predictive GenAI](https://www.pecan.ai/blog/what-is-predictive-genai) combines the strengths of LLMs with traditional [machine learning techniques](https://www.pecan.ai/blog/generative-ai-predictive-ai-machine-learning) to make [predictive model](https://www.pecan.ai/blog/building-in-house-predictive-analytics)ing more accessible for business users.

ChatGPT and similar tools based on large language models (LLMs) are amazing. But they aren’t all-purpose tools.

It’s just like choosing other tools for building and creating. You need to pick the right one for the job. You wouldn’t try to tighten a bolt with a hammer or flip a hamburger patty with a whisk. The process would be awkward, resulting in a messy failure.

LLMs actually represent just a portion of the larger machine learning toolkit, which includes both [generative AI and predictive AI](https://www.pecan.ai/blog/generative-ai-vs-predictive-ai/). It’s essential to choose the right kind of machine learning model to fit the task at hand.

Let’s dig a little deeper into why LLMs are a better fit for helping you draft text or come up with gift ideas than for tackling your business’s most critical predictive modeling tasks. There’s still a vital role for the “traditional” machine learning models that preceded LLMs and have repeatedly proven their worth in businesses. We’ll also explore a pioneering approach for using these tools together — an exciting development we at Pecan call Predictive GenAI.

## **LLMs are designed for words, not numbers**

In machine learning, different mathematical methods are used to analyze what’s called training data, an initial sample of data that represents the problem the [data analyst](https://www.pecan.ai/blog/ai-for-data-analysts-guide/) or [data scientist](https://www.pecan.ai/blog/analyst-scientist-perform-predictive-modeling) wants to tackle.

The training data is critical. It contains the patterns and relationships that a machine learning model will “learn” to predict outcomes when it looks at new data it hasn’t seen before.

But wait: What is an LLM in the world of AI? LLMs, or large language models, are a type of machine learning. They come from a specific area of machine learning called deep learning, and their structure has been explicitly refined for natural language processing.

You might say they’re built on a foundation of words. Their goal is simply to predict which word will be the next in a sequence of words. For example, iPhones’ autocorrect feature in iOS 17 [now uses an LLM](https://techcrunch.com/2023/06/05/thanks-to-ai-ios-17-will-learn-your-swears/?tpcc=tcplustwitter) to better predict which word you will most likely intend to type next.

![list of strengths of LLMs and of traditional machine learning for different tasks](https://cdn.letterdrop.co/images/2023/12/11/strengths-llms-machine-learning-models_w6ah.png) list of strengths of LLMs and of traditional machine learning for different tasks

Now, imagine you’re a machine learning model. (Bear with us, we know it’s a stretch.) You’ve been trained to predict words. You’ve read and studied millions of words from a vast range of sources on all kinds of topics. Your mentors (aka developers) have helped you learn the best ways to predict words and create new text that fits a user’s request.

But here’s a twist. A user now gives you a massive spreadsheet of customer and transaction data, with millions of rows of numbers, and asks you to predict numbers related to this existing data.

How do you think your predictions would turn out? First, you’d probably be annoyed that this task doesn’t match what you worked so hard to learn. (Fortunately, as far as we know, LLMs don’t yet have feelings.) More importantly, you’re being asked to do a task that doesn’t match what you’ve learned to do. And you probably won’t perform so well.

This mismatch of training and task is one reason why LLMs aren’t a good fit for predictive tasks using numerical, tabular data — which is the format of most of the data typical businesses collect. Instead, a machine learning model that has been designed and refined with this style of data will perform better. It’s literally been trained for this.

## **LLMs’ efficiency and optimization challenges**

In addition to being a better match for numerical data, traditional machine learning methods are far more efficient and easier to optimize for better performance than LLMs.

Let’s go back to your experience impersonating an LLM. Reading all those words and studying their style and sequence sounds like a ton of work, right? It would take a lot of effort to internalize all that information.

‎

Similarly, LLMs’ complex training can result in models with billions of parameters. That complexity allows these models to understand and respond to the tricky nuances of human language. However, heavy-duty training comes with heavy-duty computational demands when LLMs generate responses. Numerically oriented “traditional” machine learning algorithms, like decision trees or neural networks, will likely need far fewer computing resources. And this isn’t a case of “bigger is better.” Even if LLMs could handle numerical data, this difference would mean that traditional machine learning methods would still be faster, more efficient, more environmentally sustainable, and more cost-effective.

Additionally, have you ever asked ChatGPT how it knew to provide a particular response? Its answer will likely be a bit vague:

> I generate responses based on a mixture of licensed data, data created by human trainers, and publicly available data. My training also involved large-scale datasets obtained from a variety of sources, including books, websites, and other texts, to develop a wide-ranging understanding of human language. The training process involves running computations on thousands of GPUs over weeks or months, but exact details and timescales are proprietary to OpenAI.

How much of the “knowledge” reflected in that response came from the human trainers vs. the public data vs. books? Even ChatGPT itself isn’t sure: “The relative proportions of these sources are unknown, and I don't have detailed visibility into which specific documents were part of my training set.”

It’s a bit unnerving to have ChatGPT provide such confident answers to your questions but not be able to trace its responses to specific sources. LLMs’ lack of interpretability and explainability also makes them challenging to optimize for particular business needs and to understand why they offered certain information or predictions. In some business contexts, regulatory requirements exist for understanding the factors influencing a model’s predictions. These challenges mean that traditional machine learning models — which offer greater interpretability and explainability — are again likely preferable for business [use case](https://www.pecan.ai/blog/best-use-cases-for-ai)s.

## **The right place for LLMs in businesses’ predictive toolkit**

So, should we just leave LLMs to their word-related tasks and forget about them for predictive use cases? It might now seem like they can’t assist with [predicting customer churn](https://www.pecan.ai/blog/implement-predictive-churn-modeling) or customer lifetime value after all.

Here’s the thing: While saying “traditional machine learning models” makes those techniques sound widely understood and easy to use, we know from our experience at Pecan that businesses are still largely struggling to adopt even these more familiar forms of AI.

According to [recent research from Workday](https://www.emarketer.com/content/many-companies-worldwide-have-yet-adopt-ai-machine-learning), 42% of companies in North America haven’t started using AI at all or are only just beginning to research their options. And it’s been [over a decade](https://en.wikipedia.org/wiki/Timeline_of_machine_learning) since machine learning tools became more accessible to companies. They’ve had the time, and various tools are available.

For some reason, [successful AI implementati](https://www.pecan.ai/blog/overcoming-roadblocks-to-ai-implementation)[ons](https://www.pecan.ai/resource/survey-data-science-not-benefiting-marketers/) have been surprisingly rare despite the massive buzz around data science and AI — and their acknowledged potential for significant business impact. Some important mechanism is missing to help bridge the gap between the promises made by AI and the ability to implement it productively.

And that’s precisely where we believe LLMs can now play a vital bridging role. LLMs can help business users cross the chasm between identifying a business problem to solve and developing a predictive model.

With LLMs now in the picture, business and data teams that don’t have the capability or capacity to hand-code machine learning models can now better translate their needs into models. They can “use their words,” as parents like to say, to kickstart the modeling process.

‎

## **Fusing LLMs with machine learning techniques built to excel on business data**

That capability has now arrived in Pecan’s Predictive GenAI, which is fusing the strengths of LLMs with our already highly refined and automated machine learning platform. Our LLM-powered Predictive Chat gathers input from a business user to guide the definition and development of a predictive question — the specific problem the user wants to solve with a model.

Then, using GenAI, our platform generates a Predictive Notebook to make the next step toward modeling even easier. Again, drawing on LLM capabilities, the notebook contains pre-filled SQL queries to select the training data for the predictive model. Pecan’s automated data preparation, feature engineering, model building, and deployment capabilities can carry out the rest of the process in record time, faster than any other predictive modeling solution.

In short, Pecan’s Predictive GenAI uses the unparalleled language skills of LLMs to make our best-in-class predictive modeling platform far more accessible and friendly for business users. We’re excited to see how this approach will help many more companies succeed with AI.

So, while LLMs *alone* aren’t well suited to handle all your predictive needs, they can play a powerful role in moving your AI projects forward. By interpreting your use case and giving you a head start with automatically generated SQL code, Pecan’s Predictive GenAI is leading the way in uniting these technologies. You can [check it out now with a free trial](https://signup.pecan.ai/).