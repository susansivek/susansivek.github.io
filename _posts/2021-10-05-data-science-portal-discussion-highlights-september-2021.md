---
title: "Data Science Portal Discussion Highlights, September 2021"
date: 2021-10-05
excerpt: "The leaves may be changing colors, but the enthusiasm for data conversation on our Data Science Portal is evergreen! Mandatory seasonal reference: check. 🍁 Now let’s jump right into September’s top data science conversations. Time Series Tips A few…"
original_url: "https://community.alteryx.com/t5/Data-Science/Data-Science-Portal-Discussion-Highlights-September-2021/ba-p/830296"
publication: "Alteryx Community"
categories: [data-science]
---
*Originally published at [https://community.alteryx.com/t5/Data-Science/Data-Science-Portal-Discussion-Highlights-September-2021/ba-p/830296](https://community.alteryx.com/t5/Data-Science/Data-Science-Portal-Discussion-Highlights-September-2021/ba-p/830296)*

The leaves may be changing colors, but the enthusiasm for data conversation on our Data Science Portal is evergreen!

Image via GIPHY

Mandatory seasonal reference: check. 🍁 Now let’s jump right into September’s top data science conversations.

## **Time Series Tips**

A few good questions came up in September about using time series tools in Designer. First, what if you have multiple time series models that you want to use jointly to generate forecasts? [@Fierel](https://community.alteryx.com/t5/user/viewprofilepage/user-id/126737) raised [that question](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/timeseries-prediction-for-multiple-departments/m-p/828219#M202889), and [@vsoni](https://community.alteryx.com/t5/user/viewprofilepage/user-id/58890) suggested checking out the [TS Forecast Factory Tool](https://help.alteryx.com/20213/designer/ts-forecast-factory-tool).

[@Aleks\_Data](https://community.alteryx.com/t5/user/viewprofilepage/user-id/241908) also [asked how to retrieve](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/ARIMA-Residuals/m-p/827028#M202494) the [residuals](https://otexts.com/fpp2/residuals.html) generated when a model is fitted (typically, residuals are the differences between observed values and fitted values). [@NeilR](https://community.alteryx.com/t5/user/viewprofilepage/user-id/1443) and [@apathetichell](https://community.alteryx.com/t5/user/viewprofilepage/user-id/198910) conspired to come up with the right solution for the job, ultimately finding resolution in a blast-from-the-past post by [@cwkoops](https://community.alteryx.com/t5/user/viewprofilepage/user-id/39705) from 2019.

If you can’t tour the chocolate factory, the forecast factory will have to do. Image via

[*GIPHY*](https://media.giphy.com/media/11E0hI5eDiCpiM/giphy.gif)

## **Tool Palette Trick: Save Your Faves**

If you have favorite macros like TS Forecast Factory, why not make them permanent features of your Designer tool palette? [@tomtveidt](https://community.alteryx.com/t5/user/viewprofilepage/user-id/251324) asked [how to keep those tools handy](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/From-Gallery-to-Tool-Palette/m-p/826039#M202184) in Designer, and [@Garabujo7](https://community.alteryx.com/t5/user/viewprofilepage/user-id/88413) hopped in with the magic to make that happen. Grab [your favorite data science tools](https://community.alteryx.com/t5/Data-Science/Free-Data-Science-Tools-for-Designer-A-Gallery-Tour/ba-p/669590) and customize your tool categories for convenience with this awesome Designer trick.

Custom homes for your tools. Image via

## **Dataframes in Columns in Dataframes**

[@Hamder83](https://community.alteryx.com/t5/user/viewprofilepage/user-id/114466) ran into an interesting challenge when [using the Python package tabula](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Python-and-alteryx-Tabula/m-p/827829#M202783) to extract data from a PDF within Designer. [@clmc9601](https://community.alteryx.com/t5/user/viewprofilepage/user-id/190284) diagnosed the issue, detecting that pandas was combining dataframes of different sizes within single columns. [@dbmurray](https://community.alteryx.com/t5/user/viewprofilepage/user-id/248621) dropped by to mention that tabula is also available as an R package, for those who prefer that flavor of code.

Dataframes getting squished. Image via GIPHY

## **Outlier Observation**

Finally, [@ArnabSengupta](https://community.alteryx.com/t5/user/viewprofilepage/user-id/181520) posted questions about observing and dealing with outliers in your dataset, and received two great macro suggestions: [@MarqueeCrew](https://community.alteryx.com/t5/user/viewprofilepage/user-id/3557) [offered](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Eliminating-outliers/m-p/822582#M200980) an [outlier detection macro](https://gallery.alteryx.com/#!app/CReW-Modify-Outliers/5a80861feffc2a2658b0ad96), and [@mst3k](https://community.alteryx.com/t5/user/viewprofilepage/user-id/65990) [mentioned](https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Removing-outliers-using-Z-score-method/m-p/822543#M200962) the hidden z-score macro in Designer as well. In the Alteryx Intelligence Suite, the Data Health Tool could also be useful; check out this [Data Science Blog article](https://community.alteryx.com/t5/Data-Science/Vital-Signs-Assessing-Data-Health-and-Dealing-with-Outliers/ba-p/738655) about it and other methods of contending with outliers.

It’s always great to see these helpful, thoughtful conversations. We also had a super fun Data Science Mixer podcast chat in September with [Dr. Heather Lynch](https://community.alteryx.com/t5/Data-Science-Mixer/Innovating-in-data-science-for-Antarctica-s-wildlife-Dr-Heather/ba-p/817881), whose research on wildlife in Antarctica could inform your data work in business in surprising ways.

Stay tuned for more compelling articles, podcast episodes and discussions by keeping up with the [Data Science Portal](https://community.alteryx.com/datascience). See you there!