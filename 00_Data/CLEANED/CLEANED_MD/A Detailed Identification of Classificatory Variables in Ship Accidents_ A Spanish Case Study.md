# Article 

## A Detailed Identification of Classificatory Variables in Ship Accidents: A Spanish Case Study

Candela Maceiras ${ }^{1}$, José M. Pérez-Canosa ${ }^{1}$ (D) Diego Vergara ${ }^{2}$ (D) and José A. Orosa ${ }^{1, *}$ (D)<br>check for updates

Citation: Maceiras, C.; Pérez-Canosa, J.M.; Vergara, D.; Orosa, J.A. A Detailed Identification of Classificatory Variables in Ship Accidents: A Spanish Case Study. J. Mar. Sci. Eng. 2021, 9, 192. https:// doi.org/10.3390/jmse9020192

Academic Editor: Claudio Ferrari

Received: 26 January 2021
Accepted: 9 February 2021
Published: 12 February 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Navigation Science and Marine Engineering, University of A Coruña, Paseo de Ronda, 51, 15011 A Coruña, Spain; candelaria.maceiras@udc.es (C.M.); jose.pcanosa@udc.es (J.M.P.-C.)
2 Department of Mechanical Engineering, Catholic University of Ávila, C/Canteros, s/n, 05005 Avila, Spain; diego.vergara@ucavila.es

* Correspondence: jaorosa@udc.es; Tel.: +34-981-167-000 (ext. 4320)

Abstract: The present paper shows an original study of more than 163 ship accidents in Spain showing which of the usually employed variables are related to each type of vessel accident due to the lack of information in this region. To this end, research was carried out based on the Spanish Commission for Investigation of Maritime Accidents and Incidents (CIAIM) reports. Detailed combinatory ANOVA analysis and Bayesian networks results showed a good agreement with studies of other regions but with some particularities per each type of accident analyzed. In particular, ship length was defined as the more relevant variable at the time to differentiate types of accidents. At the same time, both the year of build and the fact that the ship meets the minimum crew members required were excellent variables to model ship accidents. Despite this, the particularities of the Spanish Search and Rescue (SAR) region were defined at the time to identify accidents. In this sense, although variables like visibility and sea conditions were employed in different previous studies as variables related to accidents occurrences, they were the worst variables to define accidents for this region. Finally, different models to relate variables were obtained being the base of deterministic dynamic analysis. Furthermore, to improve the accuracy of the developed work some indications were obtained; revision of CIAIM accidents scales, identification of redundant variables, and the need for an agreement at the time to define the classification limits of each identification variable.

Keywords: ship; identification; accidents; modelling; ANOVA; Bayesian network

## 1. Introduction

The traditional approach to studying or analyzing maritime safety is generally reactive rather than proactive. Hence, the importance of historic technical studies to try to foresee risk situations. Knowing which situations involve greater risk will in turn mean anticipating a possible accident. An accident theory is a collection of propositions to illustrate the principles that lead to accidents and an accident model is a simplified description of a system or process to help present the occurrence of accidents based on an accident theory [1]. According to Perrow [2], a normal accident is an intrinsic characteristic of any system. Given the characteristics of a system, multiple and unexpected interactions causing failures are inevitable. In this sense, the interactive complexity and the close characteristic coupling of the system inevitably produces an accident called "Normal Accident" or "System Accident". These accidents are the ones that must be accepted as an acceptable risk.

According to a study of Allianz, shipping in the 21st century is now safer than ever [3], probably due to a combination of factors both at technical level (technological advances), regulatory environment (international and national regulations), and fundamentally, to the influence of human factor (preparation and training). In this sense, it is in standard O-134: International Association of Marine Aids to Navigation and Lighthouse Authorities (IALA) Recommendation on the Risk Management Tool for Ports and Restricted Waterways

(2009) [4], where it addresses the IALA Waterway Risk Assessment Program (IWRAP) and Ports and Waterway Safety Assessment (PAWSA) tools.

The aim is to make available to the Member States aid for the measurement (quantitative and qualitative) of risk. The IWRAP MK2 tool, which IALA makes available to member states, calculate risk, based on the theory of Fujii and MacDuf (1974) [5,6] and presents results based on the possibility of an accident (although only collisions and groundings). Other researchers like Hollnagel and Goteman [7], proposed the Functional Resonance Accident Model, FRAM in its English nomenclature (for Functional Resonance Accident Model). The idea suggests that accidents occur due to functional resonance within a system.

To reach this so complex objective a revision of the evolution of accidents analysis is needed. In this sense, previous research works [8,9] indicated that around 75 to $96 \%$ of maritime accidents are caused, at least in part, by some type of human error. Specifying that this human error contributes to between $89 \%$ and $96 \%$ of collisions, $75 \%$ of explosions, $79 \%$ of landings, and $75 \%$ of collisions. What is more, $56 \%$ of the approaches are caused by non-compliance or violation of Convention on the International Regulations for Preventing Collisions at Sea, COLREGs [10,11].

Despite the previous indications, no single model has the capability of being useful to satisfy all demands of the maritime industry at any moment. To solve this problem, different research works were done in the last decades. In this sense, in 2007, Ibn Awal et al. [12], proposed a dynamic model for maritime accident focused on ship-to-ship collision, using two models of simulations, pre and post-accident, with the goal being to increase the maritime transport safety. Although it can be considered one of the accidents that has the worst consequences in the maritime world (for own ships, crewmembers, cargo, and the environment), the model does not include aspects so relevant as the waves or wind forces. This fact can give us an idea of the difficulty of proposing a model that can satisfy the huge number of variables that can be present in maritime transport.

In 2005, Liu et al. [13] analyzed more than 100 marine incidents in order to improve the navigation safety system (frequencies and causes) of a specific area through the Gray Clustering Method (Gray system Theory). In this research work, it highlights the need of models that can be useful for areas where the maritime accidents/incidents database is incomplete or poor due to the unpredictability of maritime accidents, a fundamental characteristic of this Theory. Furthermore, a reliable database is not always available everywhere due to the opacity that the maritime industry sometimes presents when an accident happens. In consequence, it is shown how the knowledge of frequency and causes of maritime accidents can be very useful for shipping lines, underwriters and, in general, stakeholders in the maritime industry.

Once the main data are collected, they must be analyzed, and the probabilistic method is one of the most used in the maritime industry, in addition to simulation modelling and statistical analysis of data [11]. In this sense, in 2009, Ulusçu, et al. [14] developed a paradigmatic case such as the navigation risks in the Strait of Istanbul. In this study, the authors implement a safety risk analysis with a model based on probabilistic data. In the mathematical model proposed, factors that define situations and affecting the probability of accident are grouped in vessel attributes (type, length, age, flag, tugboat, and pilot assistance), and environmental attributes. Attributes also influence consequences; in this case, vessel attributes (type and length) and shore attributes (populations, property, and infrastructure).

After slicing the Strait in several legs and collecting local information from different sources, the risk is calculated in two-tier accident types, related to a set of instigators that may cause an accident (human error, steering, propulsion, communication, navigation, mechanical, or electrical failure). As a weak point, in part of a study, authors resort to the opinion of two experts (for comparative purposes) due to the lack of a solid database, which can help to clarify the final result. As an example, the plotting of the normal probability of residuals and residuals vs. predicted variable of pair is shown, focused mainly on the human error and its influence in the collision.

At the same time, at the time to define the variables related to accidents in vessels, it is of interest to center this study on fishing vessels due to the high number of accidents. In particular, recent review works based on journal articles and reports from the maritime authorities in Poland, United Kingdom, Norway, Iceland, Denmark, United States and Alaska, and Canada [15] showed that these fishing vessels are still $50 \%$ higher at risk than on-shore workers, which is particularly high with respect to other types of vessels.

In addition, most of the previous works about fishing vessel accidents were centered on just one main variable, for instance, human factor [16-19]. Despite this, other variables were indicated as the main causes of fishing vessel accidents other than human error [19,20], e.g., weather conditions, operational status of the vessel, vessel location, seasons, and unsuitable fishing equipment [21-23]. In particular, a statistical study of accidents in fishing vessels in the northeastern United States emphasized that the probabilities of accidents in fishing vessels increase with wind speed and with placement near the shore and in the winter season [24]. In this same year, more research studies showed Marine Accident Investigation Branch (MAIB) as the better data source regarding fishing vessels accidents despite a certain tendency of under-reporting [19]. In this work, a conclusion was obtained that confirms the previous comments; the risk of accidents on fishing vessels increases as vessel length decreases. What is more, a more recent study about fishing vessel accidents in the northeastern of the United States [25] showed that the damage severity of accidents, defined in accordance with the Damage equation obtained by [26], increases with loss of stability, sinking, daytime wind speed, vessel age, and distance to shore, in agreement with previous studies. At the same time, it was obtained that the damage severity of accidents on fishing vessels increases as vessel length decreases (inversely proportional).

At the time, to identify the variables related to accidents, different research works about the analysis of the variance (ANOVA) were done. In particular, a statistical analysis centered on questionnaires and posterior ANOVA and correlations analysis was done by [16]. Its main results showed that there were clearly differentiated groups of age, vessel types, and occupation, among others. At the same time, in this work, there were assumptions of regression analysis such as linearity, normality, and multicollinearity, which were tested and found satisfactory. In consequence, it was possible to define the coefficient of the relation between related variables. From this relation it was concluded that the safety attitude is a fundamental parameter that depends on the previous experiences like people that sought medical attention (less positive attitude) and fishermen involved in accidents (positive attitude).

Once the main variables of these accidents were identified, there was a need to predict these accidents. In this sense, Mullai and Pulasson [27] developed a conceptual model based on the principles of Grounded Theory and content analysis of empirical data, in order to explain and predict maritime accidents. For that purpose, a database containing the marine accidents classified by ship and variable was used. Most of the variables were nonmetric and were grouped into 11 main categories (constructs). The design of variables was based on the European Statistics guidelines, the International Maritime Organization (IMO) investigations code, and the DAMA coding system (agreed in 1990 by the Scandinavian countries for the analysis of maritime accidents). In total, 87 variables were taken into account for designing the model, reduced to 11 "sets" or "constructs", grouped as per their common properties. Therefore, the model carried out consisted of a multilevel model of 87 variables in complex relationships and permits one to obtain the correlations among a large number of independent variables as ship's age, length, Gross Register Tonnage (GRT), and the number of persons on board.

Another paper related to human factors is based on the human factors index system of ship accidents to develop a multidimensional association rules algorithm by incorporating the Reason model and classic correlation rules algorithm [28]. Other works are centered on human factor as the main cause of most serious maritime accidents [29]. Authors use the model Human Factor Analysis and Classification System (HFACS) based on the Swiss Cheese model of human error, which had been developed to provide a methodological tool

to investigating an accident in the aviation industry. The modification of this model had been implemented by the same authors to maritime accidents some years before, and for this paper, more than 150 real cases were handled. The model consists of two interrelated causal sequences: An active failure pathway and a latent failure pathway. Once coded, the causal factors are presented and divided (organizational influences, unsafe supervision, preconditions for unsafe acts and unsafe acts). Afterwards, the first-, second-, and third-tier results are depicted.

More recent works try to address the human factor and statistical procedure together to quantify the correlation path mode of the causal factor involved in marine accidents, making use of complex structural chains supported by HFACS together with the statistical method Structural Equation Modelling (SEM), used to quantitatively analyse the relationships among human factors in accidents [30]. The paper is focused on the human factor because authors consider that in the shipping industry, despite having achieved a high level of safety from the point of view of equipment, human behavior still remains the cause of many maritime accidents. In the research, a Swiss Cheese model is also produced, and a novel method to analyze causal factors in the accidents is introduced with the help of SEM, due to the difficulty of doing the basic premises of path analysis (relationship among variables).

The measurement equation of SEM describes the relationship between the observed dependent variable and the latent independent variable. Structure equations describe the relationship between the latent variable. For the study, a database of 894 accident with the presence of human error as the cause was taken. Depending on the consequences, five levels were selected: Incidents, minor accidents, general accidents, major accidents, and serious accidents. The data were integrated into 16 major accident factors and path diagrams were carried out to check the accuracy and reliability of the model (relationships of observation or indicator variables).

Other studies are not centered on the human factor and develop their predictive procedures like a risk probabilistic model [31] in order to evaluate the probability of a ship-grounding accident taking into account the causal factors. The database contained more than 200 accident and incident reports, although using only a single accident report for modelling has its own disadvantages. As in other papers, the grounding model was developed used the Human Factor Analysis and Classification System for Grounding (HFACS-Ground). In the model construction, in order to set up a qualitative causal model, the Bayesian Belief Network (BBN) modelling was used. The model can quantify the probability of grounding given a set of input parameters.

Finally, in recent works [32], this same methodology of a chi square method and Bayesian networks were employed to be a help to estimate the occurrence of accidents when the main variables of the problem change.

In the present work, based on these previous research works and the need for indepth study of these parameters, a real case study has been conducted analyzing more than 163 accidents in the Spanish Search and Rescue (SAR) sea regions in the time frame between 2008 and 2017. For this purpose, the official reports published by the Spanish Commission for Investigation of Maritime Accidents and Incidents (CIAIM) were taken into account [33]. In particular, a procedure similar to previous research activities was employed but employing a more detailed analysis, replacing the VCH square method by the Analysis of Variance for each type of accident. This procedure will help to identify the more appropriate variable that allows us to identify the more probable type of accident in the particular sea region of the Spanish Search and Rescue (SAR). This initial study will be the base case to predict the occurrence of accidents when the main variables of the problem change based on future Bayesian networks studies.

# 2. Materials and Methods 

### 2.1. CIAIM Accidents Analysis

The Spanish Commission for the Investigation of Maritime Accidents and Incidents, CIAIM [33] performs investigations into maritime accidents and incidents in Spanish waters, including inland waters, the territorial sea, and any area outside the territorial sea upon which, in accordance with international law and on application of its domestic legislation, the Kingdom of Spain exercises jurisdiction or sovereign rights. In particular, in this study, the Spanish SAR territory has been selected. That is, the waters where the Spanish State holds responsibility in terms of search and rescue missions. At the same time, the selected period (2008-2017) was in accordance with the need to circumscribe our analysis to a stable regulatory framework, essential for the coherence of the comparative conclusions. In consequence, more than 163 accidents were analyzed in this case study.

Based on both these reports and previous research works [16,31-33], the different typical variables usually employed in those reports and associated with some types of accidents were classified. In this sense, the variables selected for this study, per accident were: Type of Ship, Year of construction, Wind direction, Wind force, Sea condition, Night or day accident, Visibility, Ship Breadth, Ship Length, GT, Crewmembers, and the Minimum number of crew members required. At the same time, the causes of the accidents were also identified for future modelling applications. Finally, all these variables were codified in accordance with standard scales like the Beaufort scale for wind force or the Douglas scale for sea conditions, and other variables were codified in accordance with the typical scales employed in the own reports. All the variable and its codes are shown in Tables A1-A8 (Appendix A).

### 2.2. Software Resources

Different software resources were employed to develop each different statistical study. In this sense, to develop such specific statistical studies like One-Way ANOVA, the software Statistical Package for the Social Sciences (SPSS) version 22 was employed [34]. Despite this, due to the need for multivariable curve fit of response surface modelling, the software Minitab version 18 was selected [35]. To classify the information, different datasheets were employed.

### 2.3. Statistical Analysis

In the present paper, different statistical studies were employed. First of all, the descriptive statistic and histograms were developed to identify each variable. After that, to identify the variables actually related to accidents, a One-Way ANOVA was employed. This statistical procedure determines whether the groups analyzed (defined by the levels of the independent variable (accidents)) are different in their means respect the overall mean of the dependent variable. To apply this study, some assumptions must be considered; independence of observation (data collection), normally distributed response variable (it will be showed by histograms), and homogeneity of variance. The other important curve-fitting statistical procedure employed in this research work was the response surface technique. This is a polynomial curve fitting with more than 3 variables (which is the main limitation of the general curve fitting defined in most of the software resources). It is an initial curve fitting tool that, like a neural network, models a process in accordance with a minimum square procedure but with the advantage that gives us the mathematical model obtained (IA is based in a black box).

### 2.4. Methodology

The original methodology employed in this research work is based on the inference statistical procedure applied to the particular case study of ship accidents understanding. In this sense, the first step was to define the correlation between each variable. It is a linear correlation defined by the determination factor and just for linear relations will show an adequate value over 0.9 .

After that, an ANOVA analysis between the accidents type and each different selected variable (selected in accordance with CIAM reports) will show the variables related to the accidents and not identified by a linear correlation, taking it a step further than previous works [16]. Besides, as it is evident, not all the variables are related in the same way with all the types of accidents so a specific ANOVA analysis between each accident with respect to the other is a more in-depth analysis that what has been done in previous statistical works. In consequence, the relevance of each variable to the detection of each different type of accident will be described and, in consequence, the adequacy of the employed scale in some variables. Finally, due to about 7 dependent variables that were related to the accident type, a response surface model will be defined to relate this influence with the type of accident (TA) as an initial general identification model. In this sense, based on the previous information obtained from the initial ANOVA study, different models that related these independent variables will be shown. This process is summed up in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Proposed methodology.

# 3. Results 

### 3.1. Linear Correlation Analysis

In this section, an initial correlation study between the main selected variables was done. As we can see in Table 1, the determination factor is very high when it is obtained between two variables. For instance, the highest value was obtained between length (L) and breadth (B) (0.95), which is a common-sense value due to some design criteria of these types of merchant ships. This same length variable is directly related to gross tonnage ( 0.79 ) and the number of crew members ( 0.78 ). This is another logical result due to the fact that these two new variables are usually related to the ship dimensions. A similar relation, but with lower determination factor, was obtained between the breadth and the Gross Tonnage, GT, (0.70) and between the breadth and the number of crewmembers (0.77). To sum up this initial correlation study, it can be concluded that the length of the ship is a representative variable that can replace other variables like breadth, GT, and number of crewmembers at the time to develop a mathematical model to identify the type of accident.

Table 1. Linear correlation analysis.


ST: Type of ship, TA: Type of accident; CY: Year of build; WD: Wind direction; WF: Wind force; SC: Sea condition; V: Visibility; N: Nocturnal; L: Length; B: Breadth; GT: Gross Tonnage; CA: Cause of accidents (Human factor); CM: Crewmembers; MNC: Minimum number of crew members.

Another interesting determination factor is that which relates to the type of accident and if the ship fulfills the minimum crewmembers required in the moment of the accident ( 0.46 ). In consequence, these two variables can be defined as of interest, but cannot be derived one from another due to the not-so-high determination factor like in the previous cases.

Another high determination factor was derived from the study of the wind force and sea conditions ( 0.76 ). It is another logical result that will let us replace both variables by just one at the time to define the main variables related to a ship accident.

Finally, a reduced determination factor of 0.22 shows a slight relationship between the type of accident and the year of construction. In this sense, caution must be taken at the time to understand this so low value. As it will be shown in the next sections, the year of build is a decisive variable, but it does not exert a linear effect over accidents. In consequence, posterior, not linear, correlation between variables must be done for the variables with a low linear determination factor; for instance, wind direction, type of ship, visibility, night period, the cause of the accident, and the real number of crew members were not directly related to the type of accident.

# 3.2. One Way ANOVA 

### 3.2.1. Accidents Independent Variables Recognition

As explained before, due to the determination factor shown in the correlation analysis being related to a line relation between variables, a One-Way ANOVA study must be done. In this sense, a significance of 0.05 was selected as it used to be done in this kind of technical analysis. Main results are shown in Tables 2 and 3 for an ANOVA analysis between variables and type of accidents and between variables and causes of accidents, respectively.

In these two tables, the variables with a significance below 0.05 were highlighted in grey due to the fact that they are statistically different in the categories or groups of the independent variable (the type of accident or cause of the accident, respectively). From Table 2, it can be observed that year of build, ship length, and the cause of accident have lower significant values, and, in consequence, they show great differences with respect to the type of accident; or what is more, they have more possibility to be a better variable for a curve fitting model that predicts the type of accident. As opposite variables, the number of crew members and wind direction cannot be defined as having changed for each different type of accident, so they are not good variables for a future modelling process.

Table 2. Identification of related variables with accidents (significance).


Finally, it is interesting to understand that, despite the fact that the cause of each accident is a good curve fitting variable, it cannot be employed to develop a model to predict the type of accident. What is more, as it can be observed in Table 3, the cause of the accident can just be related to the GT and wind force variables.

Table 3. Identification of variables related with the cause of the accident (significance).


# 3.2.2. In-Depth Analysis of Types of Accidents Identification Variables 

As it was explained before, the initial classification of types of ships, sea conditions, etc., were developed as common sense and in accordance with the usual procedure in this type of accidents. Despite this, the selected a variable and its scale may not be statistically adequate to identify the different type of accidents. In consequence, it is necessary to develop an ANOVA study employing each independent variable to identify the real statistical difference to each different type of accident respect the others. To do so, the first goal of the study was to do the ANOVA analysis of the accident type a1 when it is compared with the others, employing the ship Type (Appendix B, Table A9), year of construction (Appendix B, Table A10), sea conditions (Appendix B, Table A11), the time period (Appendix B, Table A12), visibility level (Appendix B, Table A13), the ship length (Appendix B, Table A14), and the Minimum crew member required (Appendix B, Table A15) as independent variables.

From Table A9 (Appendix B), as a result of the ANOVA analysis, it can be concluded that accidents a2, a6, a8, and a10 can be identified as significantly statistically different to accident a1 by employing the type of ship as the comparative variable. So, this variable can be employed to predict future accidents and its type. In other words, there are different types of ships for each type of accident. Thus, from the data, it can be seen that accident 1 (a1) is associated with a vessel type $3,2,7,8$, and 5 accident 3 (a3) is associated with ship types 3,7 , and 10; accident 4 (a4) to ship type 3 and 2; and accident 5 (a5) to type 4,3 , and 2. In particular, accident type 2 (a2) is always with type 3 vessels. Finally,

it is interesting to remember that it does not mean that the other groups of column 1 of Table A9 (Appendix B) are equal, they are just not dependent groups to this a1 variable.

If we now compare each of these tables, it can be concluded that visibility level and sea conditions are the worst variables to differentiate types of accidents. At the same time, the year of build and if the ship meets the minimum crew members required are better variables to differentiate types of accidents, in agreement with the initial general ANOVA analysis. Despite this, it must be observed that ship length shows, only for the types of accidents that it can differentiate, the lowest significance level so it is a stronger differentiation parameter. What is more, the year of construction (Table A10, Appendix B) is the more useful variable to differentiate accidents, except accident type 2 (a2), to the others a1, a3, and a4. It must be related with the fact that, when employing the year of construction as identifier variable, it may be not easy to differentiate sinking, an approach, grounding, or collision due to the fact that these variables maybe not really be related to the antiquity of the ship. This same effect happens in Table A15 (Appendix B) when differentiating a2 (sinking) from the other accidents based on the minimum number of crew members required. In addition, in this particular case, the minimum crew members seems to be slightly worse in identifying accidents than the year of construction based on the difficulty to differentiate a3 (Grounding) from other accidents. Despite this, it is the second-best parameter.

From Table A9 (Appendix B), it can be concluded that ship type can be employed to differentiate the accidents a5 (Fire), a6 (Capsizing), a8 (Stranded), and a10 (operational Accident) from the other accidents and that it is not as useful of a parameter as it is usually considered. From Table A14 (Appendix B), it is observed that the ship length is a good parameter, but it has some difficultness in differentiating a2 (sinking) and a6 (Overturning), while it is better at differentiating the other accidents due to its significance being zero in most of the cells. This important information must be considered, and it can be concluded that, in accordance with the type of accident to be identified, the ship length may be the best one variable. Finally, sea conditions (Table A11, Appendix B), that used to be considered the most important variable to identify a ship accident, was the worst variable due to not allowing researchers to differentiate the types of accidents at the time to classify it.

As an illustrative example of the interpretation of these tables showing the relation between accidents and each related variable, histograms of Figures 2-4 were developed for construction year, ship length, and ship type. From these histograms, one of the requirements of ANOVA analysis can be observed, the normality, as it was done in previous research works [16]. It must be highlighted that this normality can be identified by a single mode: It is asymptotic to the abscissa axis and it is symmetric with respect to the mean. In this sense, Figure 2 shows a wave similar to a normal distribution if it is considered a decreasing frequency from 2007 until present day. In consequence, it seems logical to obtain a good accident identification based on this so characteristic ship variable. From these figures, it can also be concluded that most of the ships were built between 1999 and 2007, with a length between 24 m and 44 m , and belong to ship type 3 (Fishing vessels).

As a final analysis, it is interesting to see in Table A16 (Appendix B) that the human factor is an interesting variable that allows one to differentiate ship contact (a1) from the other accidents with maximum accuracy (sig. 0.000). At the same time, it allows one to differentiate grounding, collision, and fire accidents (a3, a4, and a5) from capsizing and groundings (a6 and a8).

After these initial conclusions, it is interesting to conduct a comparison with results from previous research works. In this sense, it was defined by previous studies that flooding, grounding, and collision are influenced by the human factor in a high percentage [8]. If we analyze this indication with our results, it was observed that, when the accidents were compared in accordance with some variable, for instance, ship type, sea conditions, and visibility, it cannot differentiate the accidents a2, a3, and a4, which implies that another factor must exert a strong influence, presumably the human factor. It is in agreement with previous works' indications, and a possible solution is highlighted in this paper

showing that just ship length allows one to successfully differentiate between the difficult identification of these types of accidents. Finally, all these tables are summed up in Table 4.

From Table 4 it can be concluded that year of construction, crew members, and vessel length are the more useful variables to differentiate between the types of possible accidents in vessels.
![img-1.jpeg](img-1.jpeg)

Figure 2. Construction year histogram.
![img-2.jpeg](img-2.jpeg)

Figure 3. Ship length histogram.
![img-3.jpeg](img-3.jpeg)

Figure 4. Ship type histogram.

Table 4. Sum up of the utility of each defined classificatory variable per each type of accident.


# 3.3. Bayesian Networks 

In a similar way to the study recently conducted by Uğurlu et al. [32] (Figure 2), in the present research work, a Bayesian network was developed to define the probability of each type of accident based on the causal variables, which are identified in the previous sections.

Previous to develop the graphical model, it is necessary to define the ranges of the three more relevant variables identified in Table 4. In particular, as ship was identified as New if the ship was built after 1996, identified as Long if the ship had a length higher than 12 m , and, finally, it was identified as having a high number of crew members when it was higher than the minimum number required.

Once these ranges were defined, it is possible to define the initial probability of each one, as it is reflected in Figure 5. Despite this, it may be not a realistic value that allows us understand the importance of each variable, so further analysis must be done.
![img-4.jpeg](img-4.jpeg)

Figure 5. The initial probability of each different type of accident.
In this sense, by applying the Bayesian theorem, it is possible to define the new probability of each related variable (relevance) once it is known that one type of accident happens. In consequence, the Bayesian theorem allows us to define the new probability of vessel age, vessel length, and vessel number of crew members for the more representative accidents (a1, a4, and a10), in a similar way to how it was done in previous studies; this is reflected in Table 5.

As it was explained before, Table 5 shows the relevance of each related variable once a type of accident is identified. In this sense, from this table, an increase can be observed of the probability (from 17.17 to $58.82 \%$ ) of the relationship between accident a1 (contact) and a minimum compulsory number of crew members employed. The same happens with

this same accident, being more strongly related to a high ship length, and experiencing an increment of probability from $46 \%$ to $77 \%$.

Table 5. Probability of each different causes once it is known the type of accident happened (Posteriori).


In a similar way, when an operational accident happens (a4), a reduced ship length experiences an increment of implication in the accident by increasing the conditioned probability from $47 \%$ to $77 \%$.

Finally, once again, it was observed that, when ship length is high, it exerts an increment of its relevance and conditioned probability in collision accidents (a10). In this particular situation, there is an increment from $52.14 \%$ to $71.43 \%$, as it is shown in Table 5.

All these results were in agreement with previous works developed in other regions like that done by [32]. In general terms, a clear agreement with [32] was obtained in the identification of the relation between vessel length, age, and accident types.

Despite this, some differences with respect to. previous works were obtained. In this sense, sea conditions do not seem to be related to most of the accidents analyzed, in disagreement with [32] that identifies sea conditions and weather as some of the more relevant variables related to accidents. It must be related to the fact that the region that is the object of this study does not experience bad weather conditions or casualties. In consequence, there is a need to develop a recompilation of real case studies of different regions to develop a general stochastic model.

Finally, old ships (in this research work, identified as that with more than 24 years) only showed a higher relevance in operation accidents, in disagreement with the general conclusion obtained by [32]. Once again, it must be related to the particularities of each region object of study. In consequence, a ship age limitation of 20 years, as it is proposed by other researchers [32], may be not of interest in this particular fishing region.

At the same time, another difference with previous studies was obtained at the time to analyze ship length effect. The research work developed by [32] concludes that in smaller ships, the accidents increase. In our case study, this conclusion was obtained for operation accidents and the inverse effect for contact and collision accidents. In this sense, it is of interest to introduce the concept of a small ship due to it dependence on the limits fished at the time to analyze the problem. In our particular case study, the classificatory limit value of 12 m was selected and in [32], it was 24 m in accordance with different national standards.

From these results, it can be concluded that there is a need to develop particular case studies for different regions and to obtain variable conclusions per each type of accident due to the differences in accidents between regions paper.

# 3.4. Response Surface 

### 3.4.1. Accident Modelling

As it was explained in previous sections, most research works try to define the stochastic probability of each variable in each type of accident [36-38], but once the main variables are identified, it is of interest to define a deterministic model that allows us to understand the dynamic risk of each situation as it used in different engineering areas.

In this sense, a modelling procedure based on the response surface may help to obtain a mathematical model that allows us to relate the type of accident and the main independent variables. As it was shown in Table A1 (Appendix A), the ANOVA study allowed us to define the main related variables identified with a significance level below 0.05. In consequence, it could be defined as a mathematical model that interrelates the independent variable with all seven dependent ones. For this objective, the response surface procedure was selected due to the useful curve fitting of multivariable models. Based on this procedure, a model with a determination factor of $54.89 \%$ could be considered as adequate due to its proceeds from real sample data in 163 case studies. The model obtained is shown in Equation (1):

$$
\begin{aligned}
& T A=1085-62 \cdot S T-0.75 \cdot C Y+57.8 \cdot W F-105.9 \cdot S C-67.7 \cdot V-86.7 \cdot N-14.1 \cdot L+0.42 \cdot G T+ \\
& +18.3 \cdot N C+0.2 \cdot M N C+0.279 \cdot S T^{2}+0.000109 \cdot C Y^{2}-0.232 \cdot W F^{2}+0.156 \cdot S C^{2}+0.353 \cdot V^{2}- \\
& -0.00479 \cdot L^{2}-0.0464 \cdot N C \cdot N C+0.078 \cdot M N C^{2}+0.0300 \cdot S T \cdot C Y+1.36 \cdot S T \cdot W F-1.96 \cdot S T \cdot S C+ \\
& +1.11 \cdot S T \cdot V-0.89 \cdot S T \cdot N+0.0411 \cdot S T \cdot L-0.00110 \cdot S T \cdot G T-0.165 \cdot S T \cdot N C- \\
& -1.020 \cdot S T \cdot M N C-0.0295 \cdot C Y \cdot W F+0.0545 \cdot C Y \cdot S C+0.0308 \cdot C Y \cdot V+0.0420 \cdot C Y \cdot N+ \\
& +0.00730 \cdot C Y \cdot L-0.000222 \cdot C Y \cdot G T-0.0086 \cdot C Y \cdot N C+0.0001 \cdot C Y \cdot M N C+0.019 \cdot W F \cdot S C- \\
& -0.377 \cdot W F \cdot V+0.013 \cdot W F \cdot N+0.0416 \cdot W F \cdot L-0.00084 \cdot W F \cdot G T-0.120 \cdot W F \cdot N C+ \\
& +0.047 \cdot W F \cdot M N C+0.213 \cdot S C \cdot V+1.178 \cdot S C \cdot N-0.0324 \cdot S C \cdot L+0.00133 \cdot S C \cdot G T- \\
& -0.068 \cdot S C \cdot N C-0.153 \cdot S C \cdot M N C+1.110 \cdot V \cdot N-0.100 \cdot V \cdot L+0.00430 \cdot V \cdot G T+ \\
& +0.042 \cdot V \cdot N C+0.474 \cdot V \cdot M N C-0.144 \cdot N \cdot L+0.00232 \cdot N \cdot G T+0.009 \cdot N \cdot N C- \\
& -0.061 \cdot N \cdot M N C+0.000093 \cdot L \cdot G T+0.0326 \cdot L \cdot N C-0.0239 \cdot L \cdot M N C- \\
& -0.000102 \cdot G T \cdot N C+0.00170 \cdot G T \cdot M N C-0.072 \cdot N C \cdot M N C
\end{aligned}
$$

If we try to define a model that incorporates the human factor, a better equation is obtained with a higher determination factor of 62.51 , as we can see in Equation (2):

$$
\begin{aligned}
& T A=2713+14 \cdot S T-2.55 \cdot C Y+59.9 \cdot W F-112.4 \cdot S C-102.7 \cdot V-8.7 \cdot N+3.90 \cdot L-0.204 \cdot G T- \\
& -7.3 \cdot C A-13.9 \cdot M N C+0.438 \cdot S T^{2}+0.000601 \cdot C Y^{2}-0.150 \cdot W F^{2}+0.303 \cdot S C^{2}- \\
& -0.202 \cdot V^{2}-0.000366 \cdot L^{2}+2.111 \cdot C A^{2}+0.023 \cdot C M N^{2}-0.0087 \cdot S T \cdot C Y+0.88 \cdot S T \cdot W F- \\
& -1.35 \cdot S T \cdot S C+1.41 \cdot S T \cdot V-0.81 \cdot S T \cdot N+0.0416 \cdot S T \cdot L-0.001512 \cdot S T \cdot G T- \\
& -2.33 \cdot S T \cdot C A-0.869 \cdot S T \cdot M N C-0.0306 \cdot C Y \cdot W F+0.0581 \cdot C Y \cdot S C+0.0496 \cdot C Y \cdot V+ \\
& +0.0021 \cdot C Y \cdot N-0.00165 \cdot C Y \cdot L+0.000090 \cdot C Y \cdot G T+0.0012 \cdot C Y \cdot C A+ \\
& +0.0081 \cdot C Y \cdot M N C-0.236 \cdot W F \cdot S C-0.422 \cdot W F \cdot V+0.255 \cdot W F \cdot N-0.0087 \cdot W F \cdot L+ \\
& +0.00062 \cdot W F \cdot G T+0.862 \cdot W F \cdot C A+0.298 \cdot W F \cdot M N C+0.303 \cdot S C \cdot V+0.596 \cdot S C \cdot N- \\
& -0.0452 \cdot S C \cdot L+0.00052 \cdot S C \cdot G T-1.073 \cdot S C \cdot C A-0.225 \cdot S C \cdot M N C+ \\
& +0.869 \cdot V \cdot N-0.0654 \cdot V \cdot L+0.00335 \cdot V \cdot G T+0.284 \cdot V \cdot C A+0.025 \cdot V \cdot M N C- \\
& -0.058 \cdot N \cdot L+0.00141 \cdot N \cdot G T+0.829 \cdot N \cdot C A+0.340 \cdot N \cdot M N C+0.000057 \cdot L \cdot G T+ \\
& +0.0456 \cdot L \cdot C A-0.1173 \cdot L \cdot M N C+0.00040 \cdot G T \cdot C A+0.00249 \cdot G T \cdot M N C-0.380 \cdot C A \cdot M N C
\end{aligned}
$$

In this sense, human factor allows an increase in the accuracy of the developed model and to differentiate the approach accidents to the others. Despite this, results indicate that the accuracy and, in consequence, its human factor scale, must be improved, therefore changing the simple scale usually employed in most of the CIAIM reports to a more in-depth scale allows us to improve the accident classification.

Finally, it is interesting to highlight that these models include aspects like wind forces, among other variables, as an improvement of the limitations defined in previous works [12]. It is true that, like in other studies [14], the determination factor must be improved in future analysis and it must be done paying special attention to the influence of the human factor

in some accidents, as it was concluded previously in agreement with the more recent research lines $[29,30]$.

As an example of future study, a final model was developed. In this sense, an analysis of the more representative variable (ship length) showed that it is in fishing vessels (with a length below 40 m ) where most of the values are centered. In consequence, a decrease of model definition is concluded at higher ship lengths due to a lack of a representative number of accidents of ships in this ship length range.

If we now simplify this data analysis to the most common vessel (fishing are 96 cases of 163 analyzed) just excluding two ambiguous accidents (sinking and operational accident), the model increases its precision to a determination factor of 0.83 , see Equation (3).

$$
\begin{aligned}
& T A=\begin{array}{l}
-2727+2.99 \cdot C Y+33.1 \cdot W F-192.2 \cdot S C-102 \cdot V+33.4 \cdot N+18.2 \cdot L-1.86 \cdot G T+40.8 \cdot C A-80.2 \\
\cdot M N C-0.000812 \cdot C Y^{2}-0.296 \cdot W F^{2}-0.204 \cdot S C^{2}-0.226 \cdot V^{2}-0.0100 \cdot L^{2}-0.000273 \\
\cdot G T^{2}+2.59 \cdot C A^{2}+0.047 \cdot M C N^{2}-0.0169 \cdot C Y \cdot W F+0.0978 \cdot C Y \cdot S C+0.0516 \cdot C Y \cdot V \\
-0.0194 \cdot C Y \cdot N-0.00922 \cdot C Y \cdot L+0.000950 \cdot C Y \cdot G T-0.0275 \cdot C Y \cdot C A+0.0425 \cdot C Y \\
\cdot M N C+0.443 \cdot W F \cdot S C+0.254 \cdot W F \cdot V-1.003 \cdot W F \cdot N-0.076 \cdot W F \cdot L+0.0044 \cdot W F \cdot G T \\
+1.044 \cdot W F \cdot C A+1.076 \cdot W F \cdot M C N-1.065 \cdot S C \cdot V+1.385 \cdot S C \cdot N+0.241 \cdot S C \cdot L \\
-0.0175 \cdot S C \cdot G T-2.044 \cdot S C \cdot C A-1.135 \cdot S C \cdot M C N+0.295 \cdot V \cdot N+0.152 \cdot V \cdot L \\
-0.0225 \cdot V \cdot G T+0.945 \cdot V \cdot C A-0.737 \cdot V \cdot M N C+0.168 \cdot N \cdot L-0.0420 \cdot N+2.084 \cdot N \\
\cdot C A-0.119 \cdot N \cdot M C N+0.00651 \cdot L \cdot G T-0.180 \cdot L \cdot C A-0.296 \cdot L \cdot M C N+0.0156 \cdot G T \\
\cdot C A+0.0157 \cdot G T \cdot M C N+0.13 \cdot C A \cdot M C N
\end{array}
\end{aligned}
$$

Finally, excluding operational accidents, a determination factor of 0.90 is obtained with 76 accidents analyzed, which are half of the sampled data, see Equation (4).

$$
\begin{aligned}
T A= & -7088+7.44 \cdot C Y-122 \cdot W F+186 \cdot S C-138 \cdot V-97 \cdot N+9.8 \cdot L+2.62 \cdot G T-138 \cdot C A+42.7 \\
& \cdot M C N-0.00194 \cdot C Y^{2}+0.501 \cdot W F^{2}+0.891 \cdot S C^{2}-0.229 \cdot V^{2}+0.0423 \cdot L^{2}+0.000712 \\
& \cdot G T^{2}-0.135 \cdot M C N^{2}+0.0582 \cdot C Y \cdot W F-0.092 \cdot C Y \cdot S C+0.070 \cdot C Y \cdot V+0.0474 \cdot C Y \cdot N \\
& -0.0071 \cdot C Y \cdot L-0.00093 \cdot C Y \cdot G T+0.0668 \cdot C Y \cdot C A-0.0180 \cdot C Y \cdot M C N-0.71 \cdot W F \cdot S C \\
& +0.479 \cdot W F \cdot V-1.86 \cdot W F \cdot N+0.187 \cdot W F \cdot L-0.0432 \cdot W F \cdot G T+0.71 \cdot W F \cdot C A+1.858 \\
& \cdot W F \cdot M C N-1.15 \cdot S C \cdot V+1.91 \cdot S C \cdot N+0.285 \cdot S C \cdot L-0.0005 \cdot S C \cdot G T-3.14 \cdot S C \cdot C A \\
& -1.61 \cdot S C \cdot M C N-1.36 \cdot V \cdot N+0.467 \cdot V \cdot L-0.0760 \cdot V \cdot G T+1.07 \cdot V \cdot C A-1.134 \cdot V \\
& \cdot M C N+0.417 \cdot N \cdot L-0.1075 \cdot N \cdot G T+5.80 \cdot N \cdot C A-0.86 \cdot N \cdot M C N-0.0107 \cdot L \cdot G T \\
& -0.038 \cdot L \cdot C A+0.032 \cdot L \cdot M C N-0.0303 \cdot G T \cdot C A-0.0156 \cdot G T \cdot M C N-2.53 \cdot C A \cdot M C N
\end{aligned}
$$

From these last models, it can be concluded that an adequate scale in accident reports and an adequate variables selection may allow researchers to define highly accurate models. What is more, the minimum number of ships that suffer an accident must be defined to prevent modelling accuracy problems. These are really interesting indications for future research works about ship accidents.

# 3.4.2. Relation between Variables and Scales Employed 

In the present section, different models to relate implied variables are developed and shown in Table 6 with the aim to simplify the previous accidents models of Equations (1)-(4). For instance, from Table 1, it was obtained that sea conditions are related to the wind force and now a model with a determination factor of $60 \%$ was obtained. It is in accordance with the previous relation between Beaufort and Douglas scales shown in Table A8 (Appendix A) and is a good proof of an adequate variable analysis and modelling. Another interesting model is that which relates the crew member and the ship dimensions with a determination factor of 79.15 , in agreement with common sense and international standards requirements.

Despite this, results indicate an inadequate model to relate the construction year and the minimum crew members to identify types of accidents. As it was commented in previous sections, the type of accident is, sometimes, a little ambiguous and the same happens with the minimum number of crew members (just meets (1) or does not meet (2)). Due to the information from CIAIM reports, a better understanding of these accidents and an improvement of these scales must be developed in the future.

Table 6. Models that relate main variables.


# 4. Conclusions 

In the present work, a case study about ship accidents in the Spanish SAR territory was conducted due to the lack of similar research works about this in this region. Despite the fact that a similar analysis was employed as that in previous case studies [16,32,33], in our case, it was done with more than two related variables. In consequence, the VCH square method was replaced with the Analysis of Variance, allowing for the definition of the relation between more numbers of variables for the particular Spanish Search and Rescue (SAR) sea regions. What is more, the importance of each of the three more relevant variables for each type of accident was defined by the Bayesian networks procedure. Finally, different deterministic models based on the variables identified were developed to show the feasibility of a deterministic model in a dynamic process. In consequence, a more in-depth analysis than before was done showing the sensibility of each implied variable to determine the more probable expected type of accident and the relevance of each variable to each type of accident. The main conclusions can be defined as:

1. The most relevant variables to identify the more probable type of accident and their average values were identified. In this sense, weather conditions do not have any kind of effect over analyzed accidents, in disagreement with previous works. Wind direction does not influence the type of accident or other parameters, and wind intensity is of interest and related to the sea condition. This effect is a consequence of the particularities of the region of study. The ship length and the year of construction were identified as other important parameters, which exert a clear effect over ships accidents (except some of type a2). This must be related to the standards of each country allowing the modification of the working life of ships higher than 20 years in this region.
2. It is possible to define different multinomial models that let us predict the type of accident in a deterministic way, that were developed based on the most relevant variables employed in accidents reports.
3. Improvements in accident reports and its scales are proposed, and common classificatory limits to define ship age, ship length, and crew members must be employed to compare results of different research works. What is more, a minimum number of accidents analyzed per each ship type must be defined.
Finally, it is of interest to highlight that this initial study will be the base case to predict the occurrence of accidents when the main variables of the problem change. In this sense, future works based on neural networks for clustering and accident modelling and prediction must be done to define the characteristics of the safest ship.

Author Contributions: Conceptualization, C.M., D.V., J.M.P.-C., and J.A.O.; methodology, C.M., D.V. and J.A.O.; software, D.V., J.M.P.-C.; validation, C.M., D.V., J.M.P.-C., and J.A.O.; formal analysis, C.M., J.M.P.-C., D.V., and J.A.O.; investigation, C.M., J.M.P.-C., D.V., and J.A.O.; resources, C.M., J.M.P.-C., and J.A.O.; data curation, D.V. and J.A.O.; writing-original draft preparation, C.M., D.V., J.M.P.-C., and J.A.O.; writing-review and editing, C.M., J.M.P.-C., D.V., and J.A.O.; visualization, C.M., J.M.P.-C., D.V., and J.A.O.; supervision, C.M., J.M.P.-C., D.V., and J.A.O.; project administration, C.M., D.V., J.M.P.-C., and J.A.O.; funding acquisition, C.M., D.V., J.M.P.-C., and J.A.O. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Sustainability Specialization Campus of the University of A Coruña grant number 6310G49279- 541A- 64900.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors wish to express their gratitude to Gonzalo Guillen Espejo Savedra (The Spanish Ministry of Transport, Mobility and Urban Agenda (MITMA)) and Francisco Mata Álvarez-Santullano (CIAIM).

Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

a1 Contact
a10 Operational accident
a2 Flooding
a3 Grounding
a4 Collision
a5 Fire
a6 Capsizing
a7 List
a8 Stranded
a9 Loss of Stability
AI Artificial Intelligence
B Breadth
BBN Bayesian Belief Network
CA Cause of accidents (Human factor)
CIAIM Spanish Commission for Investigation of Maritime Accidents and Incidents
CM Crewmembers
COLREG Convention on the International Regulations for Preventing Collisions at Sea
CY Year of build
DAMA A coding system agreed in 1990 by the Scandinavian countries for the registration and analysis of marine accidents.
FRAM Functional Resonance Accident Model
GRT Gross Register Tonnage
GT Gross Tonnage
HFACS Human Factor Analysis and Classification System
IA Intelligence Artificial
IALA International Association of Marine Aids to Navigation and Lighthouse Authorities
IMO International Maritime Organization
IWRAP IALA Waterway Risk Assessment Program
L Length
MNC Minimum number of crewmembers
N Nocturnal
PAWSA Ports and Waterway Safety Assessment
SAR Search and Rescue
SC Sea condition
SEM Structural Equation Modelling
SPSS Statistical Package for the Social Sciences
ST Type of ship
TA Type of accident
V Visibility
WD Wind direction
WF Wind force

# Appendix A. Variables and Its Codes 

Table A1. Ship type code.


Table A2. Type of accident code.


Table A3. Code of minimum crew members' requirement.


Table A4. Code of visibility level.


Table A5. Code of time period in which the accident occurs.


Table A6. Code of human factor influence.


Table A7. Code of wind velocity in accordance with the Beaufort scale.


Table A8. Code of sea conditions in accordance with the Douglas scale.


# Appendix B. Results 

Table A9. Identification of the accidents that can be identified as different to each other (columns) employing Ship type as dependent variable.


Table A10. Identification of the accidents that can be identified as different to each other (columns) employing year of construction as dependent variable.


Table A11. Identification of the accidents that can be identified as different to each other (columns) employing sea conditions as dependent variable.


Table A12. Identification of the accidents that can be identified as different to each other (columns) employing night or day period as dependent variable.


Table A13. Identification of the accidents that can be identified as different to each other (columns) employing visibility as dependent variable.


Table A14. Identification of the accidents that can be identified as different to each other (columns) employing length as dependent variable.


Table A15. Identification of the accidents that can be identified as different to each other (columns) employing minimum crew members as dependent variable.


Table A16. Identification of the accidents that can be identified as different to each other (columns) employing human factor as dependent variable.

