# 6 OPEN ACCESS 

Citation: Lo lacono G, Armstrong B, Fleming LE, Elson R, Kovats S, Vardoulakis S, et al. (2017) Challenges in developing methods for quantifying the effects of weather and climate on waterassociated diseases: A systematic review. PLoS Negl Trop Dis 11(6): e0005659. https://doi.org/ 10.1371/journal.pntd. 0005659

Editor: Justin V. Remais, University of California Berkeley, UNITED STATES

Received: January 31, 2017
Accepted: May 23, 2017
Published: June 12, 2017
Copyright: © 2017 Lo lacono et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: Search terms and list of reviewed papers are available in the supporting information.

Funding: This work was supported by the National Institute for Health Research Health Protection Research Unit (NIHR HPRU) in Environmental Change and Health at the London School of Hygiene and Tropical Medicine in partnership with Public Health England (PHE), and in collaboration with the University of Exeter, University College

## RESEARCH ARTICLE

## Challenges in developing methods for quantifying the effects of weather and climate on water-associated diseases: A systematic review

Giovanni Lo lacono ${ }^{1 *}$, Ben Armstrong ${ }^{2}$, Lora E. Fleming ${ }^{3}$, Richard Elson ${ }^{4}$, Sari Kovats ${ }^{2}$, Sotiris Vardoulakis ${ }^{1,2,3,5}$, Gordon L. Nichols ${ }^{3,4,6,7}$<br>1 Chemical and Environmental Effects Department, Centre for Radiation, Chemical and Environmental Hazards, Public Health England, Chilton, United Kingdom, 2 Department of Social and Environmental Health Research, London School of Hygiene and Tropical Medicine, London, United Kingdom, 3 European Centre for Environment and Human Health, University of Exeter Medical School, Truro, Cornwall, United Kingdom, 4 Gastrointestinal Infections, National Infection Service, Public Health England, London, United Kingdom, 5 Institute of Occupational Medicine, Edinburgh, United Kingdom, 6 University of East Anglia, Norwich, United Kingdom, 7 University of Thessaly, Larissa, Thessaly, Greece

* gianni.loiacono@PHE.gov.uk


## Abstract

Infectious diseases attributable to unsafe water supply, sanitation and hygiene (e.g. Cholera, Leptospirosis, Giardiasis) remain an important cause of morbidity and mortality, especially in low-income countries. Climate and weather factors are known to affect the transmission and distribution of infectious diseases and statistical and mathematical modelling are continuously developing to investigate the impact of weather and climate on water-associated diseases. There have been little critical analyses of the methodological approaches. Our objective is to review and summarize statistical and modelling methods used to investigate the effects of weather and climate on infectious diseases associated with water, in order to identify limitations and knowledge gaps in developing of new methods. We conducted a systematic review of English-language papers published from 2000 to 2015. Search terms included concepts related to water-associated diseases, weather and climate, statistical, epidemiological and modelling methods. We found 102 full text papers that met our criteria and were included in the analysis. The most commonly used methods were grouped in two clusters: process-based models (PBM) and time series and spatial epidemiology (TS-SE). In general, PBM methods were employed when the bio-physical mechanism of the pathogen under study was relatively well known (e.g. Vibrio cholerae); TS-SE tended to be used when the specific environmental mechanisms were unclear (e.g. Campylobacter). Important data and methodological challenges emerged, with implications for surveillance and control of water-associated infections. The most common limitations comprised: non-inclusion of key factors (e.g. biological mechanism, demographic heterogeneity, human behavior), reporting bias, poor data quality, and collinearity in exposures. Furthermore, the methods often did not distinguish among the multiple sources of time-lags (e.g. patient physiology, reporting bias, healthcare access) between environmental drivers/

London, and the Met Office; and the UK Medical Research Council (MRC) and UK Natural Environment Research Council (NERC) for the MEDMI Project. The views expressed are those of the author(s) and not necessarily those of the NHS, the NIHR, the Department of Health or Public Health England. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.
exposures and disease detection. Key areas of future research include: disentangling the complex effects of weather/climate on each exposure-health outcome pathway (e.g. per-son-to-person vs environment-to-person), and linking weather data to individual cases longitudinally.

## Author summary

Unsafe water supplies, limited sanitation and poor hygiene are still important causes of infectious disease (e.g. Cholera, Leptospirosis, Giardiasis), especially in low-income countries. Climate and weather affect the transmission and distribution of infectious diseases. Therefore, scientists are continuously developing new analysis methods to investigate the impacts of weather and climate on infectious disease, and particularly, on those associated with water. As these methods are based on an imperfect representation of the real world, they are inevitably subjected to many challenges. Based on a systematic review of the literature, we identified seven important challenges for scientists who develop new analysis methods.

## Introduction

The seasonal and geographic distributions of infectious diseases are currently among the best indications of an association with weather and climate. The literature on climate effects is expanding in response to concerns about global climate change. The significance of the methods and data available is not only confined to the technical procedural aspects; methods and data also impact on the formulation of the specific scientific questions, their selection, and the development of hypotheses. Although our understanding of how weather and climate affect diseases has improved, the wide range of research methods applied make it difficult to get a robust overview of the state of research.

The relationship between climate/weather and infectious diseases is complex (e.g.[1]), as shown in the example illustrated in Fig 1. Investigating the effects of weather and climate on infectious diseases requires the ability to: i) disentangle concurrent modes of transmissions (e.g. environmental from human-to-human transmission); ii) tease apart the individual effects of multiple exposures at different temporal and spatial scales; iii) identify and separate socioeconomic drivers and behavioural causes; iv) integrate all these different processes into a unified perspective; v) attribute changes in disease to observed environmental changes (such as climate change); and vi) quantify infectious disease burden resulting from current social, economic and environmental conditions which can help to project the future disease burden resulting from these changes. These are difficult methodological and conceptual demands, and the scientific and public health community could benefit from a critical overview of the available research methods and the challenges ahead.

In this paper, we focus on the particularly important, especially in developing countries, class of infectious diseases associated with water (including those classified as neglected tropical diseases (NTD) according to the World Health Organisation (WHO) [2] the US Centers for Disease Control and Prevention (CDC) [3]) and the journal Plos NTD [4]) (Table 1). According to WHO estimates, 1.1 billion people globally drink water that is of at least 'moderate' risk of faecal contamination [5], and 842,000 annual deaths are attributable to unsafe

![img-0.jpeg](img-0.jpeg)

Fig 1. Illustration of the steps and potential pathways from being exposed to the pathogen reservoir to detection of disease. The red (blue) taps and swimmers represent contaminated (uncontaminated) drinking and recreational water. The red (blue) silhouette represents infected (notinfected) humans. Here and throughout, any kind of environment-containing pathogens that can serve as a medium for transmission (e.g. drinking water, sewage system) is referred to as "pathogen reservoir"; any form of direct or indirect contact with such medium, irrespective of the presence of the pathogen, is referred to as an "exposure". According to this conceptual scheme, a disease-free situation is the combination of negligible pathogen

population in, and/or negligible exposure of susceptible individuals to, the pathogen reservoir. Infections arise from increased interactions of exposed susceptibles with the pathogen reservoir. This can be caused by a growth in the pathogen population (driven, for example, by temperature) and/or larger exposure to the pathogen. An increase in the exposure can be directly or indirectly driven by meteorological/climate variables (e.g. high temperature increasing the risk of drinking contaminated water), environmental causes (e.g. poor water drainage management due to land use), and behavioural and/or socio-economic factors (e.g. recreational activity in unclean water). Changes in the population of susceptibles (for example due to immigration, loss of immunity and/or human-to-human transmission) can alter the patterns of exposure.
https://doi.org/10.1371/journal.pntd.0005659.g001
water supply, sanitation and hygiene (including 361,000 deaths of children under age five), mostly in lower income countries [6,7].

Infectious diseases associated with water are classified as follows: "water-system-related" infections (i.e. via aerosols from poorly managed cooling systems, e.g. Legionellosis), "waterbased" infections (i.e. via aquatic vectors or intermediate in hosts, e.g. Schistosomiasis), "water-borne" infections (i.e. via bacterial, parasitic and viral oral-faecal infection through ingestion, e.g. cholera), and "water-washed" infections (i.e. infections arising from poor hygiene due to insufficient water, these can also include oral-faecal infection, e.g. hookworm) [8] (see Table 1). Here and throughout, we use the expression "water-associated" to refer to these latter classes of diseases. Of note, we excluded diseases arising from ingestion/contact with inorganic and other chemical compounds (e.g. arsenic) and vector-borne infections linked with water (e.g. malaria, rift valley fever, river blindness) from the "water-associated" diseases.

This Review is not a prescriptive guideline of available methods for a range of problems. We reviewed and summarised the methods used to investigate the effects of weather and climate on infectious diseases associated with water, with the objective of identifying the challenges that scientists are facing when develop new analysis methods. We focused on quantitative analytical approaches, such as: mathematical models, statistical analysis, computational techniques, numerical simulations, epidemiological models and computer-generated agent based models. We excluded purely descriptive observational studies [9].

Discriminating between studies which build explanatory models versus create predictive models is particularly important in statistical modelling [10]. We however avoided this way of grouping. The dichotomy explanatory vs predictive models might be clear from an epistemological point of view [10], nevertheless, we have found it really challenging to rigorously separate papers according to this classification. For most papers, a formal distinction is often impossible as the causal relationships are inferred/discussed from the patterns captured from predictive models, and vice versa the hypothetical-deductive models (e.g. driven by causal relationships), could both be able to predict a range of future scenarios.

# Methods 

## Search strategy, selection criteria and methods

The methods for the systematic review followed the Guidelines developed by the Cochrane Collaboration [11]. We searched for English language articles published from 2000 to April 2015. The following databases were searched: Scopus, Medline, EMBASE, CINAHL, Cochrane Library, Global Health and LILACS bibliographic databases. The literature after April 2015 was also monitored using a daily email alert tool provided by Google Scholar (searching for "water borne disease" and "water related disease") to identify potential papers adopting newlydeveloped methods not covered by the initial search.

We used search terms related to water-associated diseases (e.g. "water transmission" OR "contaminated fresh water" OR "unsafe water supply" etc.) and quantitative methodologies (e.g. "mathematical epidemiology" OR "simulation") and weather and climate. The full list of


Table 1. Organisms causing diseases related to water (excluding vector borne diseases). The symbol ● specifies the known routes of transmission (not exclusively); (●) specifies the probable route of transmission but no direct evidence available. The last column indicates which organism is classified as Neglected Tropical disease, according to the World Health Organisation (W) [2], the Centers for Disease Control and Prevention (C) [3], and the journal PLOS Neglected Tropical Diseases (P) [4]. The different routes of transmission are: A) Drinking water borne; B) Water washed (reduced water access); C) Water based; D) Foodborne through water; E) Water infecting wounds; F) Bathing water transmission; G) Respiratory waterborne; H) Toxic poisoning through a bloom; I) Infection or disease related to damp; J) Medical water or solutions.



#### **Table 1.** (*Continued*)





1. https://doi.org/10.1371/journal.pntd.0005659.t001

search terms is in the Supporting Information, S2 Text. Papers were reviewed by two people (GL and GN). As the pool of returned papers was quite large, we decided to not use additional specific search terms for pathogens (e.g. 'cholera', 'rotavirus') or diagnosis/symptoms (e.g. 'diarrhoea', 'gastroenteritis'), as this would require a subjective list of potential pathogens and introduce unnecessary bias in the selection of the papers. We included articles that: i) were published in peer reviewed journals; ii) included an infectious disease in human beings; and iii) developed new methods and/or applied established methods to investigate the effects of weather and/or climate on infectious diseases (including papers for which weather and climate variables were among other equally important factors driving disease transmission).

The final set of papers was archived in EndNote (see Supporting Information, S1 Table). We identified specific questions related to the nature of the methods, their range, applicability and limitations (Table 2) that we wanted the Review to address. We then created a spreadsheet consisting of records (rows) corresponding to each paper in our final database, and columns to address the specific questions. Analysis was done in R open source analytic software [12].

Papers were clustered according to the methodology used. More precisely, for each paper we identified the list of technical keywords associated with the methods, including both general concepts (e.g. "time series analysis") and sub-analysis terms (e.g. "partial autocorrelation function"); the full list of technical keywords is presented in the Supporting Information, S1 Table. Papers that share the same keyword are often connected. Consequently, analytical

Table 2. List of scientific questions and related notes.


https://doi.org/10.1371/journal.pntd.0005659.t002

methods that are likely to be used together in the same papers tend to cluster. Analysis was done by using the "igraph" package in R [13].

# Results 

Overall, 102 papers were included in the analysis (Fig 2). Analysis of the findings and synthesis of the challenges in formulating new methods are summarised below.

## Analysis: Seven particular scientific questions addressed by the review

1) What are the main water-associated pathogens investigated and where do they occur? Fig 3 shows the frequency of pathogens in the final set of papers. Vibrio cholerae has been studied most for climate and weather effects. A significant proportion (approximately $20 \%$ of papers) focused on unspecified water-associate pathogens and these studies were mostly theoretical process-based models. The next significant categories of studies were papers that looked at diarrheal illness as a broad category based on health service data that did not include pathogen-specific information. In terms of pathogen -specific outcomes, the following pathogens were most studied (after Vibrio cholerae): Cryptosporidium spp., Leptospira spp., Schistosoma spp. Giardia sp. and Salmonella spp. Many of these are classified as NTD [2-4] e.g. Vibrio cholerae, Leptospira spp., Schistosoma spp. Giardia sp. (Table 1).

Fig 4 shows the countries where the studies were based. A good proportion of these theoretical process-based models did not link their study with any data for diseases occurring in a particular country (therefore, the outcome was listed as "General" in Fig 4). The country with the most studies (about $10 \%$ of papers) was Bangladesh, mostly in relation to cholera, followed by studies on disease data collected in US, China and Canada (Fig 4).

Thus, the pathogens reported in these studies reflect geographic (origin of infections) and socio-economic (quality of data) features: studies on cholera were associated with low and middle income countries, while Cryptosporidium spp. and Campylobacter spp. were more likely reported in high income countries that have good laboratory-based passive surveillance systems (Fig 4).
2) What methods have been used? The set of all technical keywords describing the methods used in at least two papers is displayed in a keyword network in Fig 5 (a high-resolution image for the methods used in each paper can be found in the Supporting Information, S1 Fig, see also S1 Table). The figure suggests that the most commonly used methods can be grouped into two main clusters:

- Process-Based Models (PBM), which are typically described by mechanistic compartmental models [14],
- Time series and spatial epidemiology (TS-SE) such as time series and regression analysis [15] and spatial methods typically based on geographic information system (GIS) [16].

These clusters can overlap. For examples, instances of spatial compartmental models have been developed.

Fig 5 is perhaps the most objective way of representing the methods used in the reviewed papers as it is based simply on the technical keywords recorded by their authors. As the technical keywords can be very specific, the next exercise was to identify the general methods used in the papers. A list of the most common general methods is shown in Fig 6 and in S1 Table in the Supporting Information. The entries in Fig 6 and S1 Table do not reflect an established"taxonomy" of the methods (which is not available in the literature); they are mainly guided by the patterns which emerged from keyword network (Fig 5) and selected based on their


# 7,895 excluded 

5,461 Duplicates
1,636 Conference Abstracts
798 Non-English

17,048 abstracts were stored in EndNote ${ }^{\circledR}$. By using EndNote search tool, the list of abstracts was further filtered to select documents focusing on waterassociated infectious diseases only
![img-1.jpeg](img-1.jpeg)

## 15,518 excluded

Most of these documents investigated risk and hazard associated with water (e.g. hurricanes, flood, in-organic pollutant) of non-pathogenic nature

1530 abstracts from systematic search

1547 abstracts were reviewed in total 1530 from the search plus 17 abstracts already known to the authors (in the next step, 3 of the 17 abstracts were excluded after reading the full text)
![img-2.jpeg](img-2.jpeg)

## 1,331 excluded

324 not infectious diseases; 1007 no use of quantitative methods and/or no study of the effect of weather/climate on infectious disease. For 12 of these papers the full text not available

204 full text review

## 102 excluded

No use of quantitative methods and/or no study of the effect of weather/climate on infectious disease.

102 studies included

Fig 2. Flow chart describing the selection process of all abstracts.
https://doi.org/10.1371/journal.pntd.0005659.g002

Vibrio vulnificus
Trichuris Trichiura
Salmonella Typhi
Rotavirus
Pathogens and harmful algal blooms (mixed)
Mycobacteria ulcerans
Mycobacteria malmoense
Mycobacteria avium
Different Enteroviruses (Hand, foot and mouth disease)
Chlamydia trachomatis
Ascaris lumbricoides
Ancylostoma spp.
Aeromonas spp.
Necator americanus
Hepatitis A
Fasciola hepatica
Shigella spp.
Escherichia coli
Campylobacter spp.
Salmonella spp.
Giardia sp.
Schistosoma spp.
Leptospira spp.
Cryptosporidium spp.
Non-cholerae Diarrheal Pathogens
Generic Water-Borne Pathogens
Vibrio cholerae
Proportion of Reviewed Papers \%

Fig 3. Proportion of papers investigating a particular pathogen or disease.
https://doi.org/10.1371/journal.pntd.0005659.g003
potential relevance for the study of the effects of weather and climate. For example, a close inspection of Fig 5 suggests that a substantial number of papers in the PBM clusters employed "Dose-Response Model" (which often use environmental variables, such as temperature as inputs); we therefore identified "Models comprising Exposure-Response Relantionship" as a general method.

The same principle guided the structure of Table 3, which presents some key features of the clusters of methods. In Table 3, however, we did not discuss methods such as "Descriptive Statistics" and "Survey/Surveillance/Sampling" since these were too generic in terms of their use

![img-3.jpeg](img-3.jpeg)

**Fig 4.** (a) Distribution of countries for which water-associated disease data were the focus of the reviewed papers (b) Geographic distribution of the 7 most commonly studied water-associated pathogens (resulting either in an epidemic or endemic situations) which were the focus of the reviewed papers. Each circle refers to specific countries. In particular, the largest circle in Asia refers to Bangladesh.

<https://doi.org/10.1371/journal.pntd.0005659.g004>

![img-4.jpeg](img-4.jpeg)

**Fig 5. Cluster analysis of methods.** Each dot corresponds to a reviewed paper; the brown bubbles correspond to the keywords describing the techniques. A connection between a paper and a keyword occurs when the related technique is used. The size of the bubble increases (logarithmically) with the number of papers citing the keyword. For visual purpose only, i) the bubbles are displayed with different shades of brown and ii) the technical keywords (listed in S1 Table in the Supporting Information) describing methods used by only one paper are not displayed (the full set is shown in S1 Fig in the Supporting Information). The graph was produced by using the i-graph package[13] in R.

<https://doi.org/10.1371/journal.pntd.0005659.g005>

![img-5.jpeg](img-5.jpeg)

Fig 6. The most common, general methods used in the reviewed papers (listed in S1 Table in the supporting information).
https://doi.org/10.1371/journal.pntd.0005659.g006
for investigating the effect of weather and/or climate change on water-associated diseases. Conversely, the table contains additional entries that did not emerge from the patterns from Fig 5, but we recognized that they are important for such use (e.g. "Investigation of seasonality" and separation of "Time Series Regression" in short and long term studies).

Process-based methods (PBM). Most PBM are based on compartmental models, i.e. a subdivision of the entire population into relevant epidemiological categories, such as susceptible, infected, and recovered people [14]. The population dynamics of each category is usually governed by a system of non-linear differential equations (with each single equation corresponding

Table 3. Discussion of some key features of the general methods and their relevance to the investigation of the effect of weather and/or climate change.


(Continued)


to the rate of change of each compartment). This class of models has been extended to stochastic, spatial and age-specific models. The compartmental models in our Review included an additional compartment describing the dynamic of the pathogen population in the environment (e.g. the concentration of the pathogen in the water reservoir) which is then linked in some way to temperature and/or rainfall factors (e.g., rainfall affects the volume of the water reservoir, which determines the dilution of the pathogen and, thus, the probability of contracting the disease; temperature affects the growth and survival of many free living pathogens, such as E. coli, in the water reservoir). An infection occurs when a susceptible person comes in contact with this additional category. Infected people can excrete pathogens, and feedback into the environment compartment (included in the majority of the PBM-papers), although for some infections there is no excretion and thus no feedback into the environment (e.g. Legionella). Ten percent of PBM-papers also included person-to-person transmission via contacts between susceptible and infected persons. The cluster PBM also contained sub-clusters: "ExposureResponse Relationship", "Stability Analysis", "Human Mobility", and "Network Analysis" (Fig 5). Important features of the clusters are discussed in Table 3.

Cluster TS-SE. Time series regression (TSR) analysis [15,17] is one of the most common methods used by the papers reviewed to analyse temperature and rainfall exposures as they can vary over time. Many studies used generalized linear models (GLMs) and generalized additive models (GAMs) often included terms allowing for over-dispersion. Terms to control for seasonality (time stratified model, Fourier terms, spline functions) and autocorrelation terms are often included. In most cases, residual variation in the response variable (e.g. daily counts of disease occurrence) was modelled as a Poisson distribution, followed by negative binomial. The most common exposure factors were temperature and rainfall. Socio-economic indicators were often included in the analysis.

As noted in the systematic review of Imai and Hashizume [15], only a few studies included variations in the susceptible population over time, due to, for instance, changes in immunity following disease recovery. Autoregressive models (e.g. ARMA, ARIMA, SARIMA, ARIMAX), which intrinsically take into account correlation, were used in some studies (Fig 6), although many studies in the regression tradition used ad hoc approaches for this. These methods were often used to investigate the temporal lag between the exposure and the response variable (e.g. daily counts of disease occurrence).

Spatial methods for linking datasets use geographical information systems (GIS) to link disease data with information on socio-economic indicators, temperature and rainfall (or proxy indicators), and vegetation and land use data within the same geographical framework. Georeferenced environmental data can be collected by remote sensing [16,18] and ground-station data.

Other less commonly used analytical methods included wavelet analysis [19], and the social science approach of participatory modelling [20].
3) Is the method applied to investigate the effects of climate or weather? Most of the reviewed papers ( $49 \%$ of the papers explicitly emphasized this application in the Abstract) investigated the effects of weather (i.e. short-term changes in the atmosphere, such as daily or weekly exposures to rainfall) on infectious disease. Only $9 \%$ of the reviewed papers applied the methodology to study the effects of climate, i.e. long-term averages of weather such as El Niño cycles (these applications are not mutually exclusive); and $7 \%$ used modelled future climate projections. Collinearity of exposures, i.e. highly correlated predictor variables in regression models, is an important limitation in weather and climate studies but was only explicitly identified as a limitation in $7 \%$ of studies).
4) Does the type of method depend on the disease/pathogen under investigation? Approximately $50 \%$ of papers investigating Vibrio cholerae employed methods based on

compartmental models, followed by time-series/regression analysis and spatial/GIS analysis using cholera case observations. Similar patterns were observed for unspecified water-associated pathogens. As expected, for generic diarrheal pathogens (for which there is much more uncertainty about the causes), spatial/GIS and time-series/regression analysis were the most commonly used methods (but see discussion in [1] and [21]).
5) Some key feature in the methods: e.g. What are the independent variables in the models? Does the model take into account seasonality? More than $70 \%$ of studies included observed or modelled temperature and/or rainfall/precipitation data in their analysis. A smaller proportion of studies included (the inclusion is not mutually exclusive) other environmental factors (e.g., relative humidity, vapor air pressure, evaporation) and socio-economic indicators (e.g. access to water, index of poverty, age, education, human mobility) in the analysis (Fig 7).

Around $40 \%$ of the methods explicitly included the effects of seasonality (intra-annual climate variability). A small proportion of papers (7\%) included the effects of El Niño/Southern Oscillation (ENSO) and North Atlantic Oscillations (NAO). Almost 40\% of the methods took into account spatial variation. Only a small proportion of the methods explicitly modelled the pathogen dynamics in the wider environment or the specific water reservoir; a proportion of these studies (typically, theoretical works for a proof of concept) developed general methods without focusing on specific environmental variables, but the method could be potentially applied to investigate their effects.
6) How were the results assessed? The statistical methods used to fit a model with the observed data were assessed with information criteria (such as Akaike Information Criterion, AIC and Bayesian Information Criterion, BIC) in almost 20\% of cases. In a significant proportion of papers ( $10 \%$ ), the validation of the method was based on out-of-sample predictions, i.e. a subset of the data were used to train/calibrate the method (e.g. to estimate model parameters), and then the method was applied to the rest of the data. In some cases, there was no assessment of the methods. Situations where the methods did not require comparison with real data (e.g. theoretical works requiring solely logical demonstration of theorems) were also present.
7) What are the method limitations for analysing climate and weather effects identified by the authors? The lack of inclusion of relevant factors in the methods was the most common limitation acknowledged by the authors. These included: spatial and socio-economic heterogeneity, seasonality, changing immunity, and other environmental drivers. In almost 20\% of papers, the authors identified reporting bias as a key limitation. Examples of reporting bias were: sample collections not properly designed (e.g. not stratified by age); voluntary internetbased survey reflecting survey respondents' idiosyncrasies; and health-seeking behaviours and socio-economic factors affecting access to health facilities.

The poor quality of the data was another important source of limitation according to the authors, and this was explicitly mentioned in around $30 \%$ of reviewed papers. Typical examples of poor data quality were: low spatio-temporal resolution of the exposure data (e.g. environmental exposure covered a wide geographic area or linked to a single weather stations); lack of longitudinal data (only cross-sectional surveys were undertaken); and low accuracy of the data (e.g. reliance on proxy data, missing data due to asymptomatic or unobserved infections).

In $10 \%$ of cases, the methods were not able to explain the observed patterns in the disease outcome. The authors identified the absence of underlying mechanistic explanation as a problem in about $10 \%$ of the studies. In $10 \%$ of papers, the authors highlighted that the methods were calibrated only for a specific situation (e.g. a limited region), and the findings were not generalizable.

# Synthesis: Seven challenges in developing methods for quantifying the effects of weather and climate on water-associated diseases 

## 1) Disentangling multiple transmission pathways and identifying the bio-physical mechanism of how weather affects disease and seasonality. In general, the spread of many

pathogens is subjected to concurrent modes of transmissions, as exemplified in Fig 1. For instance, cholera can be acquired from contamination of household water storage containers, food preparation, direct person-to-person contacts, and/or via contact with environmental reservoir with long pathogen persistence [22,23]. Identifying a potential signature for the particular pathways in the patterns of diseases is perhaps the ideal goal. In particular, to separate person-to-person transmission from other modes of disease transmissions a range of methods have been proposed, including nonlinear time series approaches linked with wavelet analysis [24] and mechanistic compartmental approaches [22,23]. Despite such efforts, isolating the contributions of person-to-person transmission on the burden of these diseases is a compelling problem not only for water-associated diseases but all infectious diseases [25,26].

Different transmission pathways can be strongly affected by weather and/or climate. For example, temperature may have direct effects on Salmonella bacterial proliferation at various stages in the food chain (including bacterial loads on raw food production, transport and inappropriate storage), and indirect effects on eating behaviours during hot days [27]. Rainfall might increase person-to-environment transmission of cholera, by facilitating the contamination of fresh water from the sewage system. Rainfall might also dilute the concentrations of the pathogens, reducing environment-to-person transmission [28]. Compartmental models have also been used to investigate the effects of pathogen dilution due to the seasonal variation of water volume (e.g. with monsoons) and the potential interactions with other environmental drivers (e.g. temperature [29,30] and the effects of human mobility) [31].

The key challenge ahead are increasing the awareness of the drivers of disease and a deeper integration with fields such as microbiology (e.g. identifying dose-response curves to use as input for modelling, potential coexistence of human-to-human transmission), social science (e.g. to identify and include in the methods social contacts, patterns of mobility, adaptation, etc.), and ecology (e.g. to understand and incorporate the dynamics of free living organisms in water).
2) Reducing uncertainty in reporting. Measuring the 'true' incidence of disease, and therefore morbidity and mortality rates, is a common problem in epidemiology. This includes: the under-ascertainment arising when not all cases seek healthcare; under-reporting due to failure in the surveillance system; and reporting bias [32,33]. Community-based studies have been employed to reduce the uncertainty in reporting a range of diseases, including waterassociated diseases [34]. These methods usually involve the acquisition of data, e.g. by questionnaire possibly accompanied by biological sampling (e.g. serological surveys), in a representative population such as a retrospective cohorts or a population cross-sections. These methods can be integrated with statistical and mathematical approaches to estimate incidence. For a review of these methods, see [34] and references therein.

A common problem with these methods is that they are sensitive to the particular situation under investigation, such as country, age and social group. In addition, the climate and/or weather can have a direct impact on reporting. For example, impassable roads reducing the ability to seek medical care, and therefore detection, during the rainy season might explain the apparent seasonality of incidence of Lassa fever in humans in Sierra Leone [35]. This last example underscores the importance of integrating a variety of approaches including not only serology, lab-based sampling and statistical/mathematical models, but also participatory modelling and ethnographic research [36] to assess perceptions of risk, approaches to hygiene,

health-seeking behaviour and accessibility; and how economic and social factors affect the reliability of data collection by, or reporting to, the surveillance system [35-37].
3) Identifying the key risk factors/disease determinants and tackling collinearity. A key task is often to detect the main risk factors or disease determinants, and quantify their impacts. A closely related problem is collinearity (also called multi-collinearity), i.e. the situation where two or more predictor variables in a statistical model are linearly related. Collinearity might generate numerical problems, i.e. instability of parameter estimates and inflated variance of the estimated regression coefficient. In particular, collinearity often makes it impossible to attribute the effects on the response variable to the individual predictor variables [38]. This is part of the wider epistemological problem of association vs. causation, which is not discussed here and we refer the interested reader to, for instance, the Bradford-Hill guidelines [39].

In our context, a common source of collinearity is the highly correlated climatic variables such as temperature and rainfall. In some cases, collinearity can have a limited impact on inference, if the correlation between variables remains unchanged [40]. Patterns of collinearity between climatic variables, however, strongly depend on geographic location and environment (e.g. eco-zones) [38]; and they might vary in time due to climate change. This prevents meaningful interpretation/extrapolation of the findings beyond the geographic or environmental range of sampled data.

We share the view of Dormann et al. [38] that without a mechanistic understanding of the biophysical process, collinear variables cannot be separated by statistical means alone. This requires an understanding of the relationships between the different predictor variables, e.g. the dependence of humidity on temperature and rainfall, e.g. [41], or between the response variable and one or more predictor variables, e.g. the dependence of Salmonella growth on temperature.

Such mechanistic insights are not always available and one must rely on solely statistical approaches. Under this scenario, Dormann et al. [38] conducted a systematic review of methods to deal with collinearity and a simulation study evaluating their performance (in absence of mechanistic understanding) with regard to robust model fitting and prediction.

The methodologies assessed in [38], for detecting and removing collinearities include clustering (e.g. Principal Component Analysis-based Clustering, Iterative Variance Inflation Factor Analysis), cluster-independent methods (e.g. Selection of Uncorrelated Variables, Sequential Regression), latent variable regressions (e.g. Principal Component Regression, Partial Least Squares, Dimension Reduction Techniques), and a range of approaches that may be less sensitive to collinearity (e.g. Penalised Regressions, Machine-Learning methods, Collinear-ity-Weighted Regression). Fourier analysis is another approach that, from each time series of predictors, extracts a set of orthogonal data to be used as new descriptor uncorrelated variables [18,42]. Bayesian Network Analysis is another promising tool to identify statistical dependencies between multiple variables, and to separate these into those directly and indirectly dependent with one or more response variables [43]. This data-driven statistical tool produces a graphical network, whose structure describes the interdependency between variables [43,44]. In contrast with Path Analysis [45], Bayesian network analysis does not assume any causal relationships although this can be introduced by appropriate prior distribution for the structure of the graphical network. In particular, the method has been applied to investigate socioeconomic determinants for diarrheal diseases and the role of weather in animal diseases [43,46]. Another method, applied to the 1993 Milwaukee Cryptosporidium outbreak [47], integrates population dynamic models with Profile Likelihood approach [48]. The problem of collinearity is removed by fixing the value of one or more parameters, and then estimating the remaining ones by maximizing the (log-) likelihood of the associated model; the approach is

then repeated for a range of values of the fixed parameters. The method, which is suitable for a limited subset of the parameters, provides a better understanding of the relationship among different parameters.
4) Identifying and quantifying the different sources of the temporal lag from the start of the pathway to infection to disease detection. The effects of the different meteorological, climatic, environmental and socio-economic factors on occurrence of disease are not instantaneous. Fig 1 illustrates some of the complexity. Sources of the temporal lag include the time required for potential growth of pathogen population in the environment, exposure dynamics, incubation period, and delays in reporting.

Further complications can arise from feedback from the infected population to the pathogen reservoir (e.g. rainfall facilitating contamination of fresh water from the sewage system). The required time $t_{\text {res }}$, for the pathogen population in the reservoir to replicate and reach a sufficient value to cause infections, depends on a range of environmental and microbiological factors specific to the pathogen under investigation. Methods to estimate this time and its distribution are beyond the scope of this Review; here we simple mention some mechanistic approaches and a separate published review for temperature-driven bacterial growth in food and in water drinking systems [49-53]. The required time $t_{\text {exp }}$, for susceptible individuals to be infected after being exposed to the pathogen reservoir, depends on the particular route of transmission and type of exposure.

The literature on microbial risk assessment framework (hazard identification, doseresponse relationships, exposure assessment, quantitative risk characterization) represents an important source of methods to estimate the probability of infection and disease resulting from exposure to a variety of pathogenic microorganisms [54-56]. The effect of exposure events is, in general, distributed over a time interval. A range of approaches, based on time series analysis, has been implemented to study the distributed effects of multiple episodes of exposure on infectious outbreaks (see [57] and references therein). A general statistical framework that can simultaneously represent non-linear exposure-response dependencies (due to, for example, depletion of susceptibles) and delayed effects has been recently formulated [58].

Infections are typically revealed after the incubation period, $t_{\text {inc }}$, (the time between infections and symptoms onsets); which is associated with patient's physiology, whose distribution depends on the type of infection (see historical paper of Sartwell [59]). After symptoms start, only a proportion of the infected individuals seeks medical assistance (see issue above on reporting), and for only a proportion of these cases further diagnostic testing will be conducted and recorded in the public health system. This introduces a further time lag, $t_{\text {det }}$, between the time when infected individual approaches the health system and the actual appropriate laboratory detection with diagnosis [60,61]. Even in a simple scenario, the temporal lag between the start of the pathway to infection (which can be challenging to define) and disease detection is a combination the time lags $t_{\text {res }}, t_{\text {exp }}, t_{\text {inc }}, t_{\text {det. }}$ These are typically represented by random variables drawn from adequate distributions; for example a log-normal distribution has been proposed for $t_{\text {inc }}$ and $t_{\text {det }}$.

Key challenges include: these distributions are expected to be dependent on a range of factors (patient's physiology, environment, reporting bias), they are not necessarily stationary [61], and the technical difficulties inherent with the algebra of random variables [62]. Estimating the time lag between environmental/climatic variables and infections was a common task encountered in this Review, however, none of the methods used distinguished the different sources of time lag, and in most cases the assessment was based on trial and error methods (typically, searching for high correlation between the time series of incidence and the time series of temperature and/or rainfall at 1,2, etc. weeks before the date of reported case) followed by some significance tests or selection criteria (e.g. $p$-values, AIC [63]).

![img-6.jpeg](img-6.jpeg)

Fig 7. The most common environmental and socio-economic variables included in the reviewed papers.
https://doi.org/10.1371/journal.pntd.0005659.g007

Involving the wider community via community-based studies and citizen science could help in identifying the different sources of the temporal lag from the start of the pathway to infection to disease detection. This information could be used as inputs for agent based models (ABM) to simulate controlled processes in epidemics, and to assess the capability of these models to identify the multiple sources (physiology, environment, behaviour) of time lags and their statistical distributions.
5) Studying the evolution of pathogen in response to climate change/variability. Very little research has investigated the potential effect of observed climate change/variability on

the evolution and adaptation of pathogens [56], that is changes in the climate (e.g. mean temperature and rainfall, patterns of seasonality, etc.) on over decadal time scales. In particular, seasonality is expected to be an important driver of pathogen evolution (see [64-66] and references therein), as periods of high transmission are followed by population bottlenecks reducing strain diversity and causing rapid genetic shifts. Furthermore, external periodic perturbations (e.g. seasonality in temperature, rainfall) can resonate with the natural frequencies of the ecosystem, promoting emergency or suppression of particular strains of the pathogen [66]. Apart from the theoretical work of Koelle et al [67] which might explain the cholera strain replacement in Bangladesh due to changes in monsoon rainfall patterns, we are not aware of further research investigating evolution of water-associated pathogens in response to climate change.
6) Investigating the effects of time-varying factors on transmission patterns. The importance of and challenges in understanding the effects of seasonal drivers and climate variability on the dynamics of infectious diseases are largely recognized [24,64,68-71] and not repeated here. Further challenges arise from potential changes in seasonal patterns of the drivers, for example due to control measures, and aperiodic time-varying factors [72]. Stability analysis for seasonal systems, i.e. studying the conditions for pathogen invasion and establishment in systems characterized by fluctuating environmental forcing (based for example on Floquet analysis [30,73]), represents an interesting area for future research.
7) Dealing with different spatio-temporal scales. The mechanistic approaches reviewed here were in most cases deterministic compartmental models, which are strictly only valid for large epidemics. Water-associated disease outbreaks could be point-source, affecting a relatively small population. For this situation, stochastic process-based models coupled with local weather and environmental variables could be beneficial. Quantitative methodological studies applied to longer term climatic effects are limited. Extreme events, such as prolonged droughts (months or years) and heavy rain events (days or weeks), are expected to have a major impact on the dynamics of infectious diseases [74-77]. The papers reviewed here focused on the intensity of the events alone, not their frequency. Furthermore, there is no consensus on the definition of extreme weather events [77].

None of the reviewed paper investigated the long term effect of human adaptation to climatic change. The effects of Earth atmosphere range from short term weather events, to intermediate time periods events like ENSO, to longer term climate change. We are not aware of any unified approach linking together the effects of the different time-scales on water-associated infectious diseases and their spatial distribution. Spatial analysis was often performed on a temporal snapshot (cross sectional study), usually to find correlation among different variables on different locations. Only a small proportion of spatial studies included temporal dynamics, for example to study the spread of cholera in a particular region due to rainfall. Longer term changes, such as land use changes, were rarely incorporated.

# Discussion 

A range of diverse methods are used to study the effect of weather and climate on water-associated diseases. Most of these methods can be connected to two main groups: (i) process based models (PBM), and (ii) time series and spatial epidemiology. In general, PBM were employed when the bio-physical mechanism of transmission of the pathogen was known (as with Vibrio cholerae, the most studied pathogen). PBMs describe the progression of the infectious diseases by mimicking the bio-physical processes, typically, in terms of non-linear differential equations [14]. In contrast, statistically-oriented approaches (such as regression analysis over space or over time) tended to be used when the roles of specific environmental drivers were unclear

and the methods needed to find potential correlates between environmental and/or socio-economic variables and patterns of infections.

The two clusters resemble the groups of explanatory and predictive models. Although we recognize the importance of the debate in the philosophy of science about these two groups of models [10], we avoided a formal grouping of the studies according to this classification. Applying the guidelines provided by Shmueli [10] in a rigorous and objective manner was particularly challenging in our contest. For example, many modelling studies (e.g. [78]) provide maps of the risk of a disease, i.e. they make predictions, by calculating the Basic Reproductive Number, which is a typical tool in explanatory compartmental models as built on "First Principles". Should these models be classified as predictive or explanatory?

The use, or potential use, of the reviewed methodologies to investigate the effects of weather and/or climate is discussed in Table 3. Most of the studies focused on the short-term effects of weather as these time series of health data are more readily available.

Teasing apart the individual effects of multiple abiotic factors (e.g. weather, climate, environmental, demographic, and socio-economic) on the incidence of water-associated infectious diseases is the main challenge. Additional challenges include many other methodological problems arising from the limited understanding of the complex bio-physical mechanisms, concurrent effects of many correlated factors, poor data quality and reporting bias, and uncertainty in the knowledge of relevant parameters; these are all intrinsic limitations of the methods and the data available. Addressing these challenges would enable the formulation of a framework to understand the overall effects of weather, climate, and possibly other environmental and socio-economic factors on water-associated infectious disease.

This research has the common limitations of any systematic review. An important one is the possibility we have missed relevant studies, for example due to the failure of the search engine or studies written in languages other than English. This problem could be overcome, at least in part, by the application of snowballing procedures, i.e. recursively pursuing relevant references cited in the retrieved literature and then adding them to the search results [79]. This technique is less feasible when the initial pool of documents is as large as in the current case.

Nevertheless, considering the high number of studies included in this Review, we expect that the general patterns in our findings are robust. We recognize that there are methods developed and applied to other different classes of infectious diseases (e.g. vector-borne diseases) potentially relevant to our context which were not included in our analysis. The protocol of our review was chosen to ensure the objectivity and reproducibility of the results and the research question we identified.

# Recommendations for future research 

The choice of a particular method in a study is driven by many factors, including the scientific background of the scientists involved (anecdotally, we noticed that most PBM are employed by scientists working in engineering or physics departments); the ease in implementing the methods (e.g. using freely available statistical packages); and probably the tendency to use already widely used methods, a phenomenon known as the Matthew Effect [80,81]. The choice of the methods ought to be driven by many factors, i.e. the scientific questions, the availability of data, the transmission pathways, and the bio-physical and socio-economic mechanism, as well as the state of the art of the methods. These should be critically assessed on a case-by-case basis, and not based on oversimplified, prescriptive guidelines. The findings of this Review can assist scientists in the critical selection and development of methods for quantifying the effects of weather and climate on water-associated diseases.

Tackling the many challenges. Important data and theoretical challenges emerged with implications for the surveillance and control of water-associated infections. The inter-connections between human health, the environment, and also animal health as advocated by the One Health holistic vision [82], are increasingly recognized. Being aware of these connections and the potential bio-physical mechanisms occurring at different spatio-temporal scales is crucial to separate out the multiple transmission pathways, to understand and quantify the different sources of the temporal lag, and to deal with collinearity. Incorporating information on human behaviour and socio-economic factors can help to reduce reporting bias, and improve understanding of the potential effect on infectious diseases of anthropogenic climate change and interventions.

Collecting and linking long term, high-resolution, epidemiological, socio-economic, environmental and climatic data. The integration of infection data with long-term, national-scale, environmental and land use data is an important growing approach [83]. For example, the national communicable diseases database of Public Health England has collected data from microbiology diagnostic laboratories (as well as patient's addresses in the last five years) for England and Wales since 1989. The location of the diagnostic laboratories, or the patient residences, could be used to link cases to local weather parameters supplied by the UK Met Office in a confidential manner. These cases could also be linked with the spatial density of livestock data. The utility of these datasets could be further improved, as most current datasets are one-off surveys. Data on the spatio-temporal infection prevalence in livestock are also important information.

The paucity of this kind of information is much more pronounced for data on wildlife; with the exception of voluntary based schemes (such as citizen science [84]), we are not aware of a systematic collection of such data. Involving the wider public via community-based studies and citizen science could help in reducing the uncertainty in reporting and in identifying the different sources of the temporal lag from the start of the pathway to infection to disease detection. For example, surveys could be used by public health institutions to gather data on patient behaviour, symptom onset, food and water exposures, the likelihood of seeking medical advice, and the location of the potential sources of infection, etc.

Integrating bio-physical and socio-economic mechanisms of infectious disease. The emergence, risk, spread, and control of infectious diseases are affected by many complex bio-physical, environmental and socio-economic factors [1]. These include climate and environmental change, land-use variation, and changes in population and human behaviour. For example, the abundance of long term, high-resolution, surveillance data (e.g. reported infectious diseases from Public Health England) linked with local weather parameters allows the analysis of the subset of epidemiological cases when all environmental variables (except one predictor, referred to as 'test variable') are fixed; in this way, the problem of collinearity is naturally removed. This exercise provides a family of curves of the rates of infection, which are function of the test variable and conditioned to all other fixed predictors. From the family of curves, the potential relationship between the predictors and the rate of infection can be inferred and potentially elucidate the bio-physical mechanism.

Conversely, functional relationships between epidemiological measures (e.g. incidence) and weather parameters arising from process-based models could be used as inputs for statistical models (e.g. by providing a particular relationship for the link function in a GLM). Feedbacks from community-based studies on human behaviour could also be integrated with process-based and statistical methods to design more realistic mathematical models, which in turn can assist with making policy decisions [35].

# Supporting information 

S1 Text. Technical keywords/expressions used in the documents.
(DOCX)
S2 Text. List of search words used for the MEDLINE database.
(DOC)
S1 Table. List of included papers.
(XLSX)
S1 Fig. High resolution, zoomable image for Fig 5.
(TIFF)

## Acknowledgments

We would like to thank Ms Caroline Braun from PHE for her help in searching the articles.

## Author Contributions

Conceptualization: GLI GLN.
Data curation: GLI.
Formal analysis: GLI.
Funding acquisition: SV LEF SK BA GLN.
Investigation: GLI.
Methodology: GLI GLN.
Project administration: GLI GLN.
Resources: GLI GLN SV BA LEF SK RE.
Software: GLI.
Supervision: GLI GLN SV BA LEF SK RE.
Validation: GLI.
Visualization: GLI.
Writing - original draft: GLI.
Writing - review \& editing: GLI GLN SV BA LEF SK RE.
