# RESEARCH ARTICLE 

## Systematic review of predictive models of microbial water quality at freshwater recreational beaches

Cole Heasley*, J. Johanna Sanchez, Jordan Tustin, Ian Young

School of Occupational and Public Health, Ryerson University, Toronto, Ontario, Canada

* cole.heasley@ryerson.ca


## Abstract

Citation: Heasley C, Sanchez JJ, Tustin J, Young I (2021) Systematic review of predictive models of microbial water quality at freshwater recreational beaches. PLoS ONE 16(8): e0256785. https://doi. org/10.1371/journal.pone. 0256785

Editor: Zaher Mundher Yaseen, Ton Duc Thang University, VIET NAM

Received: May 4, 2021
Accepted: August 14, 2021
Published: August 26, 2021
Peer Review History: PLOS recognizes the benefits of transparency in the peer review process; therefore, we enable the publication of all of the content of peer review and author responses alongside final, published articles. The editorial history of this article is available here: https://doi.org/10.1371/journal.pone. 0256785

Copyright: © 2021 Heasley et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data are within the paper and its S1-S9 Tables and S1 Protocol files.

Funding: IY and JT received funding for the project by the Public Health Agency of Canada: https://


#### Abstract

Monitoring of fecal indicator bacteria at recreational waters is an important public health measure to minimize water-borne disease, however traditional culture methods for quantifying bacteria can take 18-24 hours to obtain a result. To support real-time notifications of water quality, models using environmental variables have been created to predict indicator bacteria levels on the day of sampling. We conducted a systematic review of predictive models of fecal indicator bacteria at freshwater recreational sites in temperate climates to identify and describe the existing approaches, trends, and their performance to inform beach water management policies. We conducted a comprehensive search strategy, including five databases and grey literature, screened abstracts for relevance, and extracted data using structured forms. Data were descriptively summarized. A total of 53 relevant studies were identified. Most studies ( $n=44,83 \%$ ) were conducted in the United States and evaluated water quality using E. coli as fecal indicator bacteria ( $n=46,87 \%$ ). Studies were primarily conducted in lakes ( $n=40,75 \%$ ) compared to rivers ( $n=13,25 \%$ ). The most commonly reported predictive model-building method was multiple linear regression ( $n=37,70 \%$ ). Frequently used predictors in best-fitting models included rainfall ( $n=39,74 \%$ ), turbidity ( $n=$ $31,58 \%$ ), wave height ( $n=24,45 \%$ ), and wind speed and direction ( $n=25,47 \%$, and $n=$ $23,43 \%$, respectively). Of the 19 (36\%) studies that measured accuracy, predictive models averaged an $81.0 \%$ accuracy, and all but one were more accurate than traditional methods. Limitations identifed by risk-of-bias assessment included not validating models ( $n=21$, $40 \%$ ), limited reporting of whether modelling assumptions were met ( $n=40,75 \%$ ), and lack of reporting on handling of missing data ( $n=37,70 \%$ ). Additional research is warranted on the utility and accuracy of more advanced predictive modelling methods, such as Bayesian networks and artificial neural networks, which were investigated in comparatively fewer studies and creating risk of bias tools for non-medical predictive modelling.


## Introduction

Between 2000 and 2014, 140 outbreaks were reported in 35 states and a territory in the United States (U.S.) in untreated recreational water sources, leading to 4958 cases of waterborne

www.canada.ca/en/public-health.html. Grant number: 2021-HQ-000017. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.

Abbreviations: AUC, Area under the curve; AUROC, Area under the receiver operator curve; CHARMS, Checklist for critical Appraisal and data extraction for systematic Reviews of prediction Modelling Studies; FIB, Fecal indicator bacteria; Fn, Fourier transform; LASSO, Least absolute shrinkage and selection operator; NSE, NashSutcliffe efficiency; PBIAS, Percent bias; PRISMA, Preferred Reporting Items for Systematic Reviews and Meta-Analyses; qPCR, quantitative polymerase chain reaction; RMSE, Root mean squared error; U.S., United States.
disease, with $84 \%$ of the outbreaks associated with a lake, pond, or reservoir [1]. However, when accounting for non-outbreak linked cases, underreporting, and missing state data, the estimate for total water-borne illness from recreational surface waters in the U.S. is around 90 million cases annually, costing $\$ 2.2-\$ 3.7$ billion USD in healthcare services [2]. Routine monitoring for water-borne pathogens is infeasible at recreational beaches, therefore, fecal indicator bacteria (FIB) are sampled as a marker of potential pathogen concentrations and risk of infection to bathers. There are many pathogens that are spread via recreational water use that can cause recreational water illness, including enteric viruses (e.g. norovirus, adenovirus) and bacterial and protozoal pathogens (e.g. Campylobacter, Salmonella, Cryptosporidium) [3, 4]. E. coli is often used as the indicator for the presence of these pathogens in freshwater beaches [5]. Enterococcus is occasionally used as an indicator in addition to or in place of E. coli, most commonly in marine waters [6-8]. E. coli is often a preferred indicator in freshwater sources due to its strong association with the risk of gastrointestinal illness in bathers [5, 9].

Decisions on whether to close or post beaches as potentially unsafe for swimming due to water quality concerns are conducted by public health officials or other beach managers. Traditionally, these decisions are based on evaluating whether FIB levels in beach waters exceed health-action threshold values. This approach has been termed the "persistence model" of beach management, because it typically relies on culture-based laboratory assessments of FIB counts which require 18-24 hours to obtain a result, leading beach managers to make water quality decisions using the previous day's measurements. More modern genetic techniques, such as qPCR, can achieve results in 3-4 hours, but are costly for beach management and laboratories to run daily [10]. Some beach managers have moved to forecasting FIB levels using predictive models. These models typically use environmental inputs such as temperature, precipitation, and turbidity to predict FIB levels at beaches on a given day, which can then be validated and assessed with the subsequent FIB lab results [11, 12]. A wide variety of predictive modelling methods have been used at recreational beaches; including multiple linear regression [13, 14], artificial neural networks [15], and Bayesian networks [16]. These models use local weather and environmental data, collected from various sources, that are associated with FIB concentrations in the water $[6,17]$.

Given the variety of predictive modelling approaches and applications published to-date, there is a need to identify and describe existing approaches, trends, and their accuracy to inform beach water management policies. The purpose of this systematic review was to identify and summarize modelling methods used, where they have been applied, and their performance in correctly predicting beach water quality to support management decisions (e.g., posting a beach as unsuitable for swimming due to poor water quality). The review was conducted as part of a larger study to examine environmental influences on freshwater beach quality in Canada. Therefore, we have focused the scope on models developed for freshwater, recreational sites located in a temperate climate. To our knowledge, no systematic review exists on predictive models of fecal indicator bacteria at freshwater recreational sites in temperate climates.

## Methods

## Review question and eligibility criteria

The protocol for this review was created in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) Protocol 2015 checklist [18]. The remainder of this review was written using the PRISMA 2020 statement [19]; a PRISMA checklist is located in S1 Table. A review protocol was developed a priori following Cochrane Collaboration review guidelines (see S1 Protocol) [20]. However, the protocol was not registered with

any databases. The research questions were: 1) what types of predictive models were created for predicting FIB concentrations based on environmental variables for freshwater beach management decisions? 2) which predictors were included in these models? 3) how accurate are the models in determining if recreational water quality exceeds guideline recommendations?

Our eligibility criteria followed the PECO approach: Population, Exposure, Comparison, and Outcome. Our population of interest included freshwater beaches in temperate climates that are used for recreational purposes. Therefore, we excluded models focusing on coastal and estuarial waters, and waters not used for recreation (drinking water sources). Our exposure of interest included environmental data that can be collected in real time to support beach water monitoring, such as weather parameters and water conditions. We included models that compared accuracy to their original dataset, to persistent models, and that used other validation methods (e.g., bootstrapping). Our outcome of interest was FIB levels. Models predicting algal blooms were excluded. We included publications reporting on the development and/or evaluation of predictive models, reported in journal articles, conference proceedings, thesis and dissertations, and government reports. Reviews and commentary articles were excluded.

# Search strategy 

We designed a comprehensive search strategy in collaboration with a research librarian. The following databases were used to search for relevant articles: Medline via OVID, SciTech Premium, Scopus, Web of Science, and ProQuest Dissertations and Thesis Global. The search terms used in each database are provided in S2 Table. As an example of the search terms used, the search in Scopus was:
(Escherichia coli OR enterococc ${ }^{+}$OR fecal indicator bacteria) AND (regression analysis OR predict ${ }^{+}$OR nowcast ${ }^{+}$OR forecast ${ }^{+}$OR model ${ }^{+}$) AND ("fresh water" OR recreational water OR beach ${ }^{+}$OR lake OR river) AND (weather OR monitor ${ }^{+}$OR rain ${ }^{+}$OR environmental).

All articles published until the search date, December 15, 2020, were included with no publication date restrictions. A grey literature search was also conducted and involved searching nine targeted government websites from December 10-14, 2020. A list of websites searched is available in the S3 Table. To ensure all relevant publications were captured, reference lists of relevant articles were hand-searched for additional potentially relevant articles.

## Relevance screening

Citations identified by the searches were stored in a Mendeley database (Elsevier, Amsterdam, Netherlands), deduplicated, and then uploaded into DistillerSR (Evidence Partners, Ottawa, Canada). All articles were independently screened twice by CH and JS in two levels of screening: title and abstract screening (Level 1) and full article screening (Level 2).

Level 1 screening involved the question:
Is this reference potentially relevant to our review? (Yes/No).
Level 2 involved three screening questions:
Is this article about microbial water quality? (e.g., measuring E. coli, Enterococcus).
Is this article about freshwater, recreational beaches in a temperate region?
Does this article report on a predictive model for beach water quality using environmental data? (Yes/No for all).

Beaches were defined as any site intended for primary water contact activities (e.g., swimming, wading, water sports) to capture all recreational water sites. All screening forms were created prior to any screening and pre-tested by two reviewers screening 50 articles and discussing discrepancies. Pre-testing of Level 1 screening resulted in a kappa score of 0.76 , after

which the reviewers discussed their conflicts and agreed to proceed with independent reviewing after improving clarity on how to apply the eligibility criteria. Questions for level 2 were discussed prior to screening and tested on five articles by both reviewers to ensure consistent interpretation and clarity of the questions.

# Data characterization and extraction 

Articles passing the screening process were obtained as full-texts and data were extracted using a pre-specified and pre-tested form. Data were extracted by CH into a form in DistillerSR, which can be found in S5 Table. The form included 20 questions that collected information such as location details of beaches, length of study, type of predictive model, variables explored in making the model, performance metrics of the model, and risk-of-bias. Data extraction results were independently validated by JS.

## Risk-of-bias assessment and data analysis

Risk of bias of each relevant article was assessed using the CHecklist for critical Appraisal and data extraction for systematic Reviews of prediction Modelling Studies (CHARMS) [21]. We adapted the checklist from human health predictive models to environmental modelling. We considered "participants" to be beach days, and questions relating to human health were removed (e.g., details of treatments, blinding outcomes). Of 21 CHARMS questions, 10 were included in the data extraction form. Questions included sources of data, blinding predictors from outcomes, number and handling of missing data, predictor selection method, predictor transformations, and model validation methods and performance measures. Due to a priori knowledge that many studies collect data from government sources, predictor measurement methods were not included. CHARMS does not score studies based on bias, therefore, we did not determine an overall risk-of-bias score or rating for each study. Data from DistillerSR were downloaded in Excel (Microsoft, Redmond, United States) for analysis, which consisted of descriptive summary tabulations. Data visualizations were also created in Excel. While we report on performance metrics, we do not draw conclusions on validity nor compare models to each other. Meta-analysis was not deemed appropriate for this review given that predictive modelling approaches and performance metrics varied widely across studies.

## Results

Of 1710 unique citations identified in the search, 53 relevant studies were identified and included in the review (Fig 1). A descriptive summary of the model types, variables, and performances from each relevant study is presented in Table 1.

Studies were published from 2000 to 2021 (median of 2013). S6 Table summarizes study characteristics, including number of years of model building and publication type (Figs 2 and 3). While the maximum number of swimming seasons included in model building was 12 seasons [33], 19 (36\%) of the studies used only one swimming season of data for model creation. Around half ( 26 studies, $49 \%$ ) used two seasons or less. However, the number of seasons used in model building do not include seasons that were used solely for model validation in the 21 $(40 \%)$ of studies that used temporal validation.

Five countries were represented in this study: U.S. (44 publications), Germany (4), Canada (2), New Zealand (2), and France (1). Additionally, the studies mostly focused on the Great Lakes, in particular Lake Michigan (20 studies) and Lake Erie (14) (Fig 4). Lake Ontario and Lake Superior were investigated in two studies each. No studies included Lake Huron. Overall, 40 studies ( $75 \%$ ) modelled lakes and 13 studies ( $25 \%$ ) modelled rivers. Fig 5 shows the frequency of the number of beaches in each study.

![img-0.jpeg](img-0.jpeg)

Fig 1. PRISMA flow diagram of article selection.
https://doi.org/10.1371/journal.pone.0256785.g001
Table 2 summarizes modelling methods employed in the studies. The most commonly used model building method was multiple linear regression, which was used in 37 studies ( $70 \%$ ), while univariate linear regression used in three (6\%). Logistic regression, using a dichotomous outcome variable representing whether recreational waters met thresholds for safe use by bathers, were explored in five studies ( $9 \%$ ). Additionally, tree regression or random forests were utilized in six studies (11\%). Decision trees were created in three studies (6\%). Beginning in 2012, more computationally advanced models were introduced including Bayesian networks, artificial neural networks, and deterministic or hydrodynamic models, of which there were five ( $9 \%$ ), three ( $6 \%$ ), and four ( $8 \%$ ) of these model types, respectively. Various studies involved multiple modelling methods to compare their efficacy, comparing multivariate linear regression, artificial neural networks, hydrodynamic models, Bayesian networks, and stacking of multiple models together.
E. coli was the most commonly investigated FIB ( $\mathrm{n}=46$ studies, $87 \%$ ), while $11(21 \%)$ modelled Enterococcus, one ( $2 \%$ ) modelled total fecal coliforms, and one ( $2 \%$ ) included models for Salmonella and Campylobacter. Of these, 34 (64\%) studies log-transformed the concentration of the FIB of interest.

The predictor variables examined and included in final models are presented in S7 Table (and Fig 6). The variables used in most studies' final models were turbidity, wind direction, wave height, and wind speed. Time variables were important in creating models, as seen with the regular inclusion of day of year, sampling time, and month/ sub-season variables in final models. Forty-five ( $85 \%$ ) studies assessed rainfall variables, including amount of rainfall in the previous $<24,24,48$, or 72 or more hours, the length of time since the last rainfall, or intensity of the last rainfall. Three commonly transformed variables were $\log _{10}$ (turbidity), $\log _{10}$ (discharge), and weighted rainfall. Most studies obtained these environmental variables from government sources such as US Geological Survey river gauges and National Weather Service airport weather stations.






1 Season | Air Temperature, Water temperature, Turbidity, Wind speed, Wind direction, Relative humidity, Conductivity, pH, Water level, Chloride, [NH4+], [NO3-] | Air Temperature, Water temperature, Turbidity, Wind speed, Wind direction, Relative humidity, Conductivity, pH, [NH4+], [NO3-], Water level | Multiple Linear Regression | Bootstrapping/cross validation | Mean square error of prediction = 1.85, 3.67, and 2.71 | Temporal synchronization analysis of environmental predictors improved the predictive regression models.  |
12 Seasons | Rainfall 72+ hr, Barometric pressure, Wind speed, Wind direction, Discharge/flow, Total nitrogen, Total phosphorus, Distance from lake exit, Suspended solids, Particulate inorganic phosphorus | Rainfall 72+ hr, Wind speed, Distance from Lake exit, Particulate inorganic phosphorus | Multiple Linear Regression | Temporal validation (2 new seasons) | Sensitivity = 0%-50% Specificity = 96.67%-100% Adjusted R2 = 0.73 Accuracy = 96.67%-100% RMSE = 0.23-0.64 | Models worked well, could be used for guiding swimming advisories.  |
3 Seasons | Rainfall 24hr, Rainfall 48 hr, Rainfall 72+ hr, Water temperature, Wave height, Previous day [FIB], Solar radiation, Turbidity, Wind speed, Wind direction, Discharge/flow, Conductivity, Bird count, Day of year, Water level, Current direction, Days since last rainfall | Rainfall 24hr, Rainfall 72+ hr, Wave height, Previous day [FIB], Turbidity, Wind direction, Discharge/flow, Bird count, Current direction, Day of year, Days since last rainfall | Multiple Linear Regression | Original Dataset | R2 = 0.17-0.58 Accuracy = 71.2%-90.9% False positive rate = 4.0%-15.1% False negative rate = 3.9%-14.6% | Models were beach specific, future research could test created models in future years, and test whether adding subsequent years' data improves the models.  |
2 Seasons | Rainfall 24hr, Rainfall 48 hr, Rainfall 72+ hr, Air Temperature, Water temperature, Wave height, Solar radiation, Barometric pressure, Turbidity, Wind speed, Wind direction, Relative humidity, Discharge/flow, Conductivity, pH, Chlorophyll a, Day of year, Bird count, Debris assessment, Dissolved O3, Wave period, Sub-season, Current direction, Current speed, Cloud cover, Water level, Algae category, Bather count, Weather category | Rainfall 24hr, Rainfall 48 hr, Rainfall 72+ hr, Air temperature, Water temperature, Wave height, Solar radiation, Barometric pressure, Turbidity, Wind speed, Wind direction, Relative humidity, Discharge/flow, Conductivity, Chlorophyll a, Day of year, Bird count, Debris assessment, Current direction, Cloud cover, Water level, Sub-season, Algae category, Bather count, Weather category | Multiple Linear Regression | Temporal validation (new season) | Sensitivity = 0%-100% Specificity = 40.4%-100% Accuracy = 55.8%-98.4% | 24 of the 42 models performed at least 5% more accurately than persistence models.  |





(Continued)

PLCOS ONE | https://doi.org/10.1371/journal.pone.0256785 August 26, 2021 10/31





(Continued)


(Continued)

7 Seasons | Rainfall 24hr, Rainfall 48 hr, Rainfall 72+ hr, Air Temperature, Water temperature, Wave height, Barometric pressure, Turbidity, Wind speed, Wind direction, Discharge/flow, Water level, Bird count, Algae category, Debris category, Fecal matter category, Odor (Y/N), Combined sewer overflow (Y/N), Day of year, Wave direction, Cloud cover, Current speed, current direction | Rainfall 24hr, Rainfall 48 hr, Rainfall 72+ hr, Air Temperature, Water temperature, Wave height, Barometric pressure, Turbidity, Wind speed, Wind direction, Discharge/flow, Water level, Bird count, Algae category, Debris category, Fecal matter category, Odor (Y/N), Combined sewer overflow (Y/N), Day of year, Wave direction, Cloud cover, Current speed, Current direction | Model stacking of these outputs: Multiple Linear Regression (including Partial least squares, sparse partial least squares), Bayesian modelling, Tree regression/ random forest | Bootstrapping/ cross-validation (leave one year out cross-validation) | Accuracy = 78%, 81%, and 82.3% | A model stacking approach improved robustness of prediction power, with random forest contributing the most weight in the model.  |
1 Season | Solar radiation, Conductivity, Current speed, Current direction, decay rate | Solar radiation, Conductivity, Current speed, Current direction, decay rate | Hydrodynamic modelling | Original dataset | RMSE = 0.600, 0.647, and 0.809
PBIAS = 6.511, 10.489, 24,283
Fourier Norms = 0.408, 0.408, 0.660 | Model could accurately simulate FIB concentrations at beaches using unstructured grids.  |
5 Seasons | Air Temperature, Water temperature, Wave height, Solar radiation, Barometric pressure, Wind speed, Wind direction, Day of year | Wave height, Barometric pressure, Day of year | Multiple Linear Regression | Original dataset | Adjusted R2 = 0.20–0.41 | Beaches geographically close to each other had correlated E. coli fluctuations.  |
1 Season | Rainfall 24hr, Water temperature, Wave height, Previous day [FIB], Solar radiation, Turbidity, Wind speed, Wind direction, Discharge/flow, Conductivity, Past [FIB] beyond one day | Rainfall 24hr, Water temperature, Wave height, Turbidity, Wind speed, Discharge/ flow, Past [FIB] beyond one day | Artificial neural networks: Nonlinear input-output (NIO), nonlinear autoregressive neural network (NAR), nonlinear autoregressive network with exogenous inputs (NARX), NAR + discrete wavelet transform (WA-NAR) | Division of original dataset | Sensitivity: NIO = 0, 1, 1
NAR = 0, 0.5–0.5
NARX1 = 0, 0.5, 1
NARX2 = 0, 0.5, 1
WA-NAR = 0.5, 0.33, 0.4
Specificity: NIO = 1, 1, 1
NARX1 = 1, 0.99, 1
NARX2 = 1, 1, 0.99
WA-NAR = 1, 1, 1
R2: NIO = 0.53, 0.43, 0.46
NAR = 0.38, 0.34, 0.59
NARX1 = 0.80, 0.82, 0.80
NARX2 = 0.77, 0.83, 0.82
WA-NAR = 0.62, 0.57, 0.62
RMSE: NIO = 0.33, 0.53, 0.32
NAR = 0.24, 0.41, 0.45
NARX1 = 0.15, 0.31, 0.23
NARX2 = 0.26, 0.23, 0.29
WA-NAR = 0.07, 0.10, 0.11 | NARX performed the best, with WA-NAR in second but requiring no explanatory variables. All models were comparable to or outperformed other predictive models previously built the these beaches.  |



a If different lengths of time were used at different locations, the highest number of seasons is presented. Only seasons used in model building were included, entire seasons used for model validation are not included in this count.

b Statistics for validation of models used over calibration data when available.

- Conference proceeding, only an abstract was available.

Definitions: Area under the curve (AUC), Area under the receiver operator curve (AUROC), Root mean squared error (RMSE), Percent bias (PBIAS), Least absolute shrinkage and selection operator (LASSO), Nash-Sutcliffe efficiency (NSE), Fourier transform (Fn).

https://doi.org/10.1371/journal.pone.0256785.t001

![img-1.jpeg](img-1.jpeg)

Fig 2. Frequency of the number of swimming seasons used in building models.
https://doi.org/10.1371/journal.pone.0256785.g002
Accuracy of predictive models was measured in 19 studies. The overall accuracy of these studies was $81 \%$ (S8 Table). Of these studies, 13 compared their accuracy to pre-existing persistence models at those locations, and with the exception of one study, all or most of their models were more accurate than persistence models.

Risk-of-bias characteristics of each individual study are presented as S9 Table, while summary data are presented in Table 3. We found that one study adjusted predictor weights to address overfitting (regularization of data) and only three studies (6\%) compared predictors' calibration distributions to validation distributions. Additionally, little information was provided on the handling of missing data, with only $17(32 \%)$ studies reporting any method of dealing with missing FIB concentrations or predictor values. Modelling assumptions, such as normality, were rarely fully addressed, with only $12(23 \%)$ studies affirming they met all model assumptions.

Predictor measurements were mostly collected from governmental sources ( 37 studies, $70 \%$ ) or directly by the authors ( 28 studies, $53 \%$ ) deploying their own instruments or water sampling. Most predictor transformations were categorizations ( 20 studies, $38 \%$ ), weighting rainfall over several days ( 11 studies, $21 \%$ ), or logarithmic ( 18 studies, $34 \%$ ), however some studies utilized other transformations such as polynomial [64] or trigonometric transformations [34]. Twenty-seven studies ( $51 \%$ ) reported they used no pre-screening criteria for selecting variables that were evaluated in multivariable modelling. To select predictors in final models, 13 studies ( $25 \%$ ) used model fit characteristics of predicted values compared to actual values of FIB concentrations in many or all possible models. A full model approach using all variables was used in 10 studies (19\%). Other techniques included backwards elimination,

![img-2.jpeg](img-2.jpeg)

**Fig 3. Frequency of publication types.**

<https://doi.org/10.1371/journal.pone.0256785.g003>

![img-3.jpeg](img-3.jpeg)

**Fig 4. Frequency of the location of beaches.**

<https://doi.org/10.1371/journal.pone.0256785.g004>

![img-4.jpeg](img-4.jpeg)

Fig 5. Frequency of the number of beaches, or sampling sites if beaches not provided.
https://doi.org/10.1371/journal.pone.0256785.g005
Akaike's Information Criterion, and forward selection. Seven (13\%) studies created models using the Virtual Beach software tool.

# Discussion 

This review compiles results of the literature reporting on predictive models of FIB at fresh, recreational waters using environmental predictors. It provides novel insight on key variables of interest, modeling techniques, and considerations of modeling for those looking to create predictive models at other waters. Our review is the first to provide a systematic approach to reviewing the literature in this area. It focuses exclusively on fresh, recreational waters, and further explores the role of various environmental predictors, which is novel to the literature of

Table 2. Modelling techniques for creating the predictive models present in 53 relevant studies.


https://doi.org/10.1371/journal.pone.0256785.t002

![img-5.jpeg](img-5.jpeg)

Fig 6. Frequency of environmental variables explored in studies and frequency of variables included in final models.

<https://doi.org/10.1371/journal.pone.0256785.g006>

This type of modeling de Brauwere *et al.* reviewed regression and hydrodynamic models predicting FIB in all surface waters in 2014 and provided an in-depth summary of important processes for hydrodynamic models [72]. We similarly found that most relevant studies in this area were conducted in the U.S. despite wider search parameters. Additionally, this review reports on the validation techniques and amount of data used during model building and validation of reviewed studies.

As the geology, pollution sources, and climate of beaches differ geographically, building beach-specific models are important for accuracy [13, 65, 72]. Even in the same region, different bodies of water behave differently. For example, Hatfield [43] created an effective model for FIB in Lake Erie, but a similar model for a nearby artificial lake was not successful due to poor efficacy. However, geographically similar beaches within a specific region may be able to be modeled similarly to help reduce resources required to build models [54]. Different beach models may require different modeling approaches and environmental variables, so it is important to explore these elements in new contexts before generalizing models to other beaches.

Predictive modeling has the ability to overcome several issues in recreational water monitoring. Firstly, it addresses the reliance on persistence models, where the accuracy of posting beaches as suitable or unsuitable for swimming and other water activities depends on FIB concentrations remaining consistent across the 24-hour lab-response time. It also does not require the large resource and capacity investment of upgrading to qPCR for rapid testing, as most beach managers collect FIB data and government weather and water stations are already set up

Table 3. Risk of bias checklist summary for 53 relevant studies.


Table 3. (Continued)


https://doi.org/10.1371/journal.pone.0256785.t003 at or near many recreational waterways, resulting in less investment to collect data to develop and implement models. However, these techniques can still be integrated together. The city of Chicago has adopted a hybrid model for determining beach water quality [73]. The five beaches (out of 20) that produce $56 \%$ of poor water quality days are tested with qPCR everyday, with the others placed into clusters, with one beach per cluster tested with qPCR and the rest predicted with models. This hybrid approach identifies poor water quality days three times more accurately than the previous predictive models alone. The rapid testing ensures accuracy, while the predictive models reduce costs and may provide a solution to the shortcomings of both methods.

The efficacy of predictive models depends on the quality and accuracy of information put into them. Thirty-seven studies collected at least some of their environmental data from governmental sources, which are likely to be reliable in quality. While they might reflect slightly different weather conditions from beaches, due to being located elsewhere, such small changes are not likely to be a limitation in modelling. Rainfall is an important environmental factor as it washes microbial contamination from urban surfaces and agricultural sources into larger bodies of water, and increases sewer and river discharge [35, 47]. As a result, elevated E. coli levels are often associated with extreme rainfall events [69]. A wide range of timeframes for antecedent rainfall were explored, from a few hours prior to sampling to several days before. For easier interpretation, this review categorized these times as $<24$ hours, 24 hours, 48 hours, and 72 or more hours. Of the studies that explored times across this range, the most commonly used time in final models was $72+$ hours [48, 61, 64]. Some studies also evaluated weighted

rainfall variables that emphasized more recent rainfall across a 3-day period. Regardless, when explored in a study, every rainfall variable was included in at least one final model more than $50 \%$ of the time, indicating the value of examining and comparing a variety of ways of expressing rainfall.

After rainfall, turbidity was the most frequently included variable in at least one final model. It's importance relates to the association of bacteria with sediments and particulate suspended solids [74]. As UV radiation can kill E. coli, higher turbidity can protect the bacteria by absorbing or scattering solar radiation [75]. The importance of sand-associated FIB was shown at a beach in Lake Huron, where erosion of sand was the main source of E. coil from the foreshore to surface water, mediated by wave height [76]. Larger waves may also be responsible for washing bird fecal matter from the beach into the water [54]. Wind direction and speed are important explanatory variables as they are associated with driving FIB from sediments or point sources towards the beach [77, 78]. Winds, waves, and turbidity are often correlated parameters, as winds and waves churn sediments which increases turbidity [43, 78].

While explored less often, temporal variables were consistently included in final models, $100 \%$ of the time for day of year, day of week, and time of sampling, and $75 \%$ of the time for sub-season/month. FIB may accumulate in water bodies over the summer and, on average, increase over time during the bathing season [34]. Depending on characteristics, FIB concentrations may increase as the day progresses [66] or decrease [65] due to solar inactivation. This result is also dependent on enumeration method, as Telech et al. found that time of day was an important predictor of Enterococcus cell counts, but not qPCR results [65]. Pollution sources, such as waterfowl, other bathers, and discharge into the body of water were similarly explored less often but were nonetheless important considerations.

Numerous modelling techniques and predictor selection methods were utilized in this review. Multiple linear regression methods were the most popular and were shown to produce accurate predictions. However, other methods may produce more accurate predictions. Comparing models built at different locations with different variables and rates of FIB exceedances would not yield accurate comparisons; however, four studies included in this review compared modelling techniques using the same data and were thus able to compare techniques. The best performing models in these four studies were artificial neural networks [50], Bayesian networks [23], gradient boosting machine (a type of random forest) [30], and a model stacking algorithm that combines two or more models into one prediction [67]. All outperformed regression methods such as ordinary, partial, and sparse partial least squares methods for multiple linear regression, and were more consistent across years and locations. Further research is warranted on these approaches and their utility for implementation in routine beach water quality monitoring.

Predictor selection was also varied, but no comparisons of methods were conducted. However, seven studies (13\%) used the Virtual Beach tool, created by the U.S. Environmental Protection Agency, which is intended to aid researchers and beach managers in creating predictive models [79]. The tool allows users to upload data, explore relationships among variables, transform variables, use different regression-based modelling techniques (including a recent addition of a gradient boosting machine), and evaluate models based on several model fit characteristics. The tool is free and designed to be user-friendly to support implementation of modelling at more beaches. While a gradient boosting machine was added, it still relies on regression techniques. Models created by the tool outperformed persistence models in some studies [27] but not others [37].

A few key limitations in the literature were found in the risk-of-bias. For instance, 22 studies validated their models by refitting the model through the original dataset that built the model without internal validation (bootstrapping or cross-validation), which increases the risk

of overfitting [21]. Furthermore, only 13 studies (25\%) specified whether or not modelling assumptions were met, which could impact model accuracy and reliability. Lastly, 37 studies (70\%) did not provide any information about how missing data were dealt with, which raises additional concerns about reliability of the models. The risk of bias checklist, CHARM, required several modifications for this review compared to it's intended context of human health outcomes. A checklist intended for systematic reviews of non-health related predictive models would benefit future reviews and improve reporting of risk of bias information when creating predictive models in this research area.

The goal of predictive models is to produce more accurate results than persistence models, using the previous day's FIB measurement for current day decisions. Most models included in this review outperformed persistence models to varying degrees, in terms of sensitivity, specificity, and/or accuracy, supporting the use of predictive models in management decisions [27, $35,64,70,80]$. However even if models are used for management decisions, routine water sampling for FIB should still be conducted to ensure models remain valid, and are updated and refined as appropriate, across seasons. To ensure models are up to date, the U.S. Geological Survey suggests that beach managers update their predictive models before every new bathing season [27, 70], which may not always occur in practice [81].

Once an accurate model is created, their use by beach management or the public to make decisions regarding recreational activities requires a user-friendly interface. The U.S. Geological Survey Great Lakes NowCast [81] provides real-time estimates of beach water quality along Lake Erie and Lake Ontario to the public [81]. Built from the Ohio NowCast system, several studies in this review were used in developing this tool [35, 36, 38]. The predictive models created for the Cuyahoga river were also added into the Ohio NowCast [27, 28]. The website allows users to examine current and past conditions, and also explains factors in the model. The Philly Rivercast [82] provides nowcasts for the Skullykill River and it's development was outlined by Maimone et al. [49]. These platforms are used by beach managers and the public, which allows authorities to make real-time water quality decisions easily, and the pubic to learn about beach postings prior to arrival and make decisions about whether or not to swim or engage in other recreational activities at the beach. Additionally, as seen with the Great Lakes NowCast, these platforms can be modified and scaled to include new beaches as appropriate.

There were several limitations to this study. Firstly, while grey literature was included, only selected government websites were searched. Therefore, we could have missed some relevant studies. However, our search verification strategy helped to mitigate this potential bias. Lastly, our review was geographically limited to fresh, recreational waters in temperate regions, excluding models created for marine, tropical and subtropical waters. Predictive models in those settings may have different environmental predictors and performance.

# Conclusions 

This review is the first to systematically examine literature on predictive models for FIB levels in fresh, recreational waters. The review reports on 53 relevant articles extracted from five databases. We have highlighted commonly explored and frequently used environmental variables and modelling techniques that can inform future predictive modelling projects and options for beach managers. Rainfall, turbidity, wind, and wave height were most commonly incorporated into final models, and most models used linear regression. Evidence supports use of real-time models of FIB levels as an indicator of water quality rather than or in addition to using persistence models. At locations with consistent monitoring of FIB, predictive models can improve the effectiveness and response times of risk communication with beachgoers

about recreational water quality risks, which can help to potentially reduce water-borne illness. A risk of bias checklist was adapted for this review and identified common limitations in the literature. Future research may benefit from a risk of bias checklist intended for non-medical predictive models. This review provides insight for researchers and beach managers interested in creating their own predictive models in terms of key variables, modelling approaches, and bias-reduction techniques to consider. More research should be conducted to evaluate the effectiveness and utility of more advanced predictive modelling approaches such as artificial neural networks, Bayesian approaches, and other machine learning methods.

# Supporting information 

S1 Table. PRISMA checklist for systematic reviews components and location they can be found in the review.
(PDF)
S2 Table. Search terms used in each database.
(PDF)
S3 Table. Grey literature search of government websites and their URLs. Searched December 10-14, 2020.
(PDF)
S4 Table. Eligibility criteria to define microbes of interest, geography, predictors of interest, and types of publications.
(PDF)
S5 Table. Data extraction form, including primary outcomes and risk of bias questions. (PDF)

S6 Table. Descriptive summary of number of swimming seasons used for model building, number of beaches investigated, FIB of interest, geography of beaches, and type of publication of the 53 relevant studies.
(PDF)
S7 Table. Frequency of variables explored in studies and used in a final model for predicting microbial water quality.
(PDF)
S8 Table. Average accuracy of models that assessed accuracy and whether or not they performed better than persistence models.
(PDF)
S9 Table. Risk-of-bias characteristics of 53 articles reporting on predictive models of fecal indicator bacteria using environmental predictors, excluding characteristics found in Table 1 of main text.
(PDF)
S1 Protocol. Protocol for systematic literature review.
(PDF)

## Acknowledgments

We would like to thank Cecile Farnum, a research librarian at Ryerson University, for assistance with the search strategy.

# Author Contributions 

Data curation: Cole Heasley, J. Johanna Sanchez.
Funding acquisition: Jordan Tustin, Ian Young.
Investigation: Cole Heasley.
Methodology: Cole Heasley, Ian Young.
Validation: J. Johanna Sanchez.
Writing - original draft: Cole Heasley.
Writing - review \& editing: J. Johanna Sanchez, Jordan Tustin, Ian Young.
