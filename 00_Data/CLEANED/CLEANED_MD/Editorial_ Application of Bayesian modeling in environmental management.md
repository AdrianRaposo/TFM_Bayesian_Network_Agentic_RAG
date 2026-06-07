## OPEN ACCESS

EDITED AND REVIEWED BY
Alexander Kokhanovsky,
German Research Centre for Geosciences, Germany
*CORRESPONDENCE
Marie Anne Eurie Forio,
(1) marie.forio@ugent.be

SPECIALTY SECTION
This article was submitted
to Environmental Informatics
and Remote Sensing,
a section of the journal
Frontiers in Environmental Science
RECEIVED 20 December 2022
ACCEPTED 21 December 2022
PUBLISHED 10 January 2023
CITATION
Forio MAE, Moltchanova E and
Goethals PLM (2023), Editorial: Application
of Bayesian modeling in
environmental management.
Front. Environ. Sci. 10:1128055.
doi: 10.3389/fenvs.2022.1128055
COPYRIGHT
(c) 2023 Forio, Moltchanova and Goethals. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Editorial: Application of Bayesian modeling in environmental management

Marie Anne Eurie Forio ${ }^{1 *}$, Elena Moltchanova ${ }^{2}$ and Peter L. M. Goethals ${ }^{1}$<br>${ }^{1}$ Department of Animal Sciences and Aquatic Ecology, Ghent University, Ghent, Belgium, ${ }^{2}$ School of Mathematics and Statistics, University of Canterbury, Christchurch, New Zealand

KEYWORDS
Bayesian network, environmental modeling, Bayesian models, environmental risk assessment, water-energy-food nexus, habitat suitability, water quality modeling

## Editorial on the Research Topic <br> Application of Bayesian modeling in environmental management

## 1 Introduction

Over the past decade, Bayesian models have been increasingly applied in environmental modelling particularly to support decision-making, policymaking and environmental risk assessment. Bayesian modelling uses Bayes' theorem to combine the prior information on the parameters with the data to obtain the posterior distribution for the parameters of interest. The resulting posterior probabilities are used to solve the original problem. Among the Bayesian models are Bayesian networks which are probabilistic graphical models. A Bayesian network essentially consists of a directed acyclic graph (DAG), identifying the relationships (edges) between the variables (nodes), and a set of conditional probability tables, which quantify these relationships. Often, the DAG is specified a priori based on expert knowledge. However, there is also a possibility of leaving at least some possible connections or even all of them to the machine learning algorithm such as illustrated by Ramazi et al. (2021). One area of application, where Bayesian networks are becoming popular is habitat suitability modelling (Tantipisanuh et al., 2014; Hamilton et al., 2015). They provide more flexibility than traditional regression-based models since they do not assume linearity in parameters. And unlike MaxEnt, the model does not have to be fully specified a priori but is rather learned from the data. A second application in which Bayesian networks gained attention during recent years is the modelling of complex environmental systems, for instance in the context of ecosystem services analysis and scenario forecasting (Forio et al., 2020). The related popularity among practitioners is due to their transparency and ability to incorporate uncertainty. Particularly, these Bayesian networks are recently and increasingly being applied in ecology and environmental risk assessment. This Research Topic aims to exemplify novel applications of Bayesian networks in environmental modelling and management, particularly in the analysis of habitat suitability, environmental risk assessment, water quality and complex environmental interactions such as the water-energy-food nexus in river basins.

## 2 Insights gained from the article research topic

Wilson et al. apply Bayesian networks to map winter habitat for mountain goats in coastal British Columbia, Canada. The mountain goats are an iconic species, which are important culturally as well as environmentally. The study included observations between March 1990 and January 2022 over an area of approximately $285,000 \mathrm{~km}^{2}$. The authors used a number of relevant factors to describe the habitat and found the model to be most sensitive to changes in slope, forest age class, and snow zone. The reported mean precision was $91 \%$ based on 10 -fold crossvalidation for observations and $86 \%$ for random locations, indicating good performance overall. The authors conclude that while the results of their Bayesian Network are similar to the standard resource selection function modelling, which typically entails logistic regression, it provides a flexible and intuitive alternative, which may become more attractive as the number of potential explanatory variables and relationships between them grows.

Li and MacDonald Gibson use Bayesian networks to predict the occurrence and risks of emerging pollutants. Their work focuses on the risk of exposure to short-chain per- and polyfluoroalkyl substances (PFAS) in groundwater. The study is based on the data collected between 2001 and 2019 by the Minnesota Department of Health. The concentrations of four types of chemical compounds were dichotomised according to whether or not they were above the health hazard threshold. Out of a total of 87 potential variables, the final models contained 11-13 predictors. The variables distance to the 3 M factory, distance to the former Oakdale disposal site, the total number of aircraft within 10 km , and distance to the nearest large river were found to be common influencers for all four outcomes. The crossvalidated AUCs for all the models were above .96 . The authors admit drawbacks such as dichotomisation and the lack of data on some important variables including wind direction but conclude that despite these limitations their models are highly accurate and robust classifiers of risk.

Mentzel et al. applied Bayesian network for the environmental risk assessment of five selected pesticides. They combined probability distributions for exposure and effect into a risk characterization (i.e., the probability distribution of a risk quotient). The Bayesian network model was used to account for the variability of the predicted pesticide exposure in agricultural streams, and inter-species variability in sensitivity to the pesticide among freshwater species. The study predicted the probability distribution of the risk quotients in 2050 and 2085. The authors found that although the risks posed by the pesticides were generally low, a stronger increase in risk was predicted with an increased pesticide application as a result of a potential adaptation to a future climate with higher pests pressures.

Glendell et al. developed a decision-support tool using a Bayesian network that facilitates system-level thinking about nutrient pollution (phosphorus) in rivers. The authors brought together academic and stakeholder communities to co-construct a Bayesian network model simulating the probability of soluble reactive phosphorus (SRP) concentration falling into the Water Framework Directive good or moderate/poor ecological status classifications. The Bayesian network model was also used to investigate the effectiveness of three mitigation
measures (i.e., buffer strips, fertilizer input reduction, and septic tank management) on the ecological status of rivers. Model simulations suggested an increase of good ecological status (GES) probability (5\%) by reducing fertilizer inputs below optimal agronomic levels and an increase of GES probability ( $8 \%$ ) by managing the septic tanks while the implementation of riparian buffers did not have an observable effect on the number of sites characterized by a GES.

De Cock et al. identified and elaborated on the water-energyfood nexus in the Guayas River basin (Ecuador) and linked these interactions to the UN Sustainable Development Goals. The authors developed a conceptual diagram for the development of a Bayesian network model and highlighted the relevance of using a Bayesian network approach when modelling the WEF nexus due to the complex spatial situation and the limited data availability in the basin. Their insights reveal how land-based food and energy production systems affect downstream food production systems based on aquaculture and capture fisheries. In this manner, the Bayesian network models are highly valuable to start and moderate stakeholder discussions and develop integrated approaches to optimise food, energy and water production at a large scale.

## 3 Conclusion

The authors highlighted the benefits of Bayesian network in environmental modelling which include the ability to integrate diverse and sparse information and account for uncertainty, while being flexible and transparent. Despite the increasing number of Bayesian models applied in environmental setting, their application is still limited. There thus remains enormous potential of Bayesian methodological approach in the future research in various environmental domains such as disease control, climate change adaptation, sustainable use of natural resources, cost-benefit analyses of mitigation and restoration actions and disaster risk reduction measures, to name but a few.

## Author contributions

MF: Conceptualization, drafting and revising, EM: Drafting and revising, PG: Revising.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.
