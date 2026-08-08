---
title: "Data Science and Disability: Enhancing Care With Innovation"
date: 2020-08-20
excerpt: "Data science has presented new possibilities for greater independence, improved care, and better outcomes for people with disabilities. Here are some examples of this kind of innovation. Could the time it takes for you to…"
original_url: "https://medium.com/swlh/data-science-and-disability-enhancing-care-with-innovation-35577b3c992a"
publication: "Medium"
categories: [data-science]
---
*Originally published at [https://medium.com/swlh/data-science-and-disability-enhancing-care-with-innovation-35577b3c992a](https://medium.com/swlh/data-science-and-disability-enhancing-care-with-innovation-35577b3c992a)*

![](https://miro.medium.com/max/330/0*kdTXR-2yBCEw-cz4)

## Data science has presented new possibilities for greater independence, improved care, and better outcomes for people with disabilities. Here are some examples of this kind of innovation.

*Photo from* [*Disabled and Here*](https://affecttheverb.com/disabledandhere/)

Could the time it takes for you to water your houseplants say something about your health? Or might the amount you’re moving around your neighborhood reflect your mental health status?

When translated into data and analyzed, these measures could indeed provide insights into the health of people living with chronic physical or mental illness or disabilities.

Data science has presented new possibilities for greater independence, improved care and better outcomes. Whether it’s healthcare organizations using data to deliver care more effectively, developers creating data-driven apps that help identify early warning signs of illness, or inventors creating new sensors and devices to detect health issues, all these tools rely on data science techniques to help people living with disabilities or mental illness. Here are some examples of this kind of innovation that I found especially intriguing.

# Anomaly Detection at Home

People who are able to live mostly independently could benefit from advances in smart home technologies and sensors embedded in their living environments. [Anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection) is a key data science technique used in many different contexts, such as detecting credit card fraud and monitoring manufacturing processes. Researchers are also working on using anomaly detection to identify deviations from typical behavior for people living in “smart” homes equipped with sensors, such as cameras and computerized pill dispensers that report on medication habits.

In [one study](https://rpaudel42.github.io/assets/anomaly-detection-elderly-3.pdf), researchers established a baseline for movement and behavior at home by having volunteers complete “Instrumental Activities of Daily Living,” or routine home activities like watering plants or microwaving food. The researchers constructed [an activity graph](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8) representing how that behavior looked in time and physical space for each volunteer.

Knowing that baseline, the researchers’ anomaly detection algorithms could identify deviations that could represent cognitive or physical concerns. These researchers plan to integrate this capability into a real-time monitoring application that could show both sudden or longer-term deviations from a person’s baseline behavior patterns at home.

*The anomalous pattern on the bottom shows that the resident is taking an unusually long time to fill a watering can in order to complete the task of watering plants. That anomaly could reveal larger challenges in completing household activities. Image from* [“Anomaly Detection of Elderly Patient Activities in Smart Homes using a Graph-Based Approach,”](https://rpaudel42.github.io/assets/anomaly-detection-elderly-3.pdf) by Ramesh Paudel, William Eberle, and Lawrence B. Holder

# Cluster Analysis for Parkinson’s Disease

It’s hard for people with Parkinson’s disease and their caregivers to identify, track and respond to the many different ways the disease can manifest and progress. Wearable sensors and the data they generate could help address this challenge, however.

For example, this [research study](https://www.frontiersin.org/articles/10.3389/fneur.2017.00677/full) explained how a wearable device could gather data for patients and clinicians, including tracking of activity, sleeping, falls, gait characteristics and “freezing” (a temporary inability to move that is experienced by those with Parkinson’s). That data could offer more comprehensive insights than those available in a brief office visit with a medical provider.

However, the researchers also point out that better analytic techniques are needed to make full use of this kind of data. They highlight the potential for unsupervised clustering techniques that could make sense of the large quantity of data gathered by a constantly worn device. Their research used [t-Distributed Stochastic Neighbor Embedding](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding) (t-SNE), which is a way to visualize high-dimensional datasets in two dimensions. The image below shows an example.

Image from [“A Perspective on Wearable Sensor Measurements and Data Science for Parkinson’s Disease,”](https://www.frontiersin.org/articles/10.3389/fneur.2017.00677/full) by Ricardo Matias, Vitor Paixão, Raquel Bouça, and Joaquim J. Ferreira

The image shows the clustering of movement data from a wearable sensor worn by a patient with Parkinson’s. The red Xs represent movement during an “off state” (the term used to describe a period when a patient doesn’t respond well to levodopa medication); the blue dots represent movement during an “on state,” when medication was working well. The clustering approach shows the difference between those times and could help identify patterns in a patient’s movement that would be useful in refining a personalized treatment strategy.

# Geolocation for Mental Health

Do your movements in your local area reflect your mental health status? What about the number of phone calls you make or text messages you send?

Researchers have been studying the potential of smartphone data for treating mental illness for some time. Mobility, social interaction and survey responses could all be useful in helping people with mental illness manage and assist caregivers in knowing when an intervention might be timely.

One [pilot study](https://www.nature.com/articles/s41386-018-0030-z) of an app designed for people with schizophrenia used both active data collection (asking users about their symptoms) and passive data (e.g., geolocation, communication frequency). The data were integrated into a multivariate time series model and could be monitored for days when multiple features were “simultaneously and sufficiently anomalous.” Those occurrences could predict relapse and hospitalization for app users, potentially providing “early warning signs” for caregivers.

*The image above shows the p values for different data points for one patient, collected in the study of an app for people with schizophrenia. There’s increased variability in the patient’s daily mobility, sociability and self-reported symptoms right before a relapse and hospitalization. Image from* [“Relapse prediction in schizophrenia through digital phenotyping: a pilot study,”](https://www.nature.com/articles/s41386-018-0030-z#Fig2) by Ian Barnett, John Torous, Patrick Staples, Luis Sandoval, Matcheri Keshavan and Jukka-Pekka Onnela

The researchers noted that mental illness is extremely varied and complex. They suggest that data-driven approaches may be best used in creating a personalized model for relapse, reflecting one individual’s unique patterns, versus trying to create a generalizable model that applies to everyone contending with the same disease.

# Important Considerations

If you’ve been reading this and thinking, “But … privacy!” — yes, indeed. There’s certainly a great deal of personal information that is shared to use smart home sensors, wearable devices or smartphone apps as indicators of physical and/or mental health.

[One study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6581733/) showed that older adults would be willing to share this kind of data with their primary medical professionals and “most trusted people,” and would be OK with the data being stored short term (defined in the study as up to one week). With regard to mental health, a worrisome [2017 study](https://www.sciencedirect.com/science/article/pii/S2214782918300460) showed that fewer than half of the 116 available mental health smartphone apps had a privacy policy. A [2018 survey](https://www.sciencedirect.com/science/article/pii/S2214782918300460) of people with a history of mental illness showed they had strong concerns about the external monitoring of their health, the potential for undesired sharing to social networks, and the risk of exposure of sensitive information to third parties or hackers.

Data science techniques will undoubtedly help address many health challenges, but the public may need a little reassurance about how their data will be used in this effort. Still, the potential for both personalized treatment and widespread insights into a wide variety of diseases is clear and exciting.