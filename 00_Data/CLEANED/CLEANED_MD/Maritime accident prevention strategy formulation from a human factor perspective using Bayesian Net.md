# LJMU Research Online 

Fan, S, Zhang, J, Blanco-Davis, E, Yang, Z and Yan, X
Maritime accident prevention strategy formulation from a human factor perspective using Bayesian Networks and TOPSIS
http://researchonline.ljmu.ac.uk/id/eprint/13282/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Fan, S, Zhang, J, Blanco-Davis, E, Yang, Z and Yan, X (2020) Maritime accident prevention strategy formulation from a human factor perspective using Bayesian Networks and TOPSIS. Ocean Engineering, 210. ISSN 00298018

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# 1 Maritime accident prevention strategy formulation from a human factor perspective 

## 2 using Bayesian Networks and TOPSIS

3 Shiqi Fan ${ }^{1,2,3}$, Jinfen Zhang ${ }^{1,2 *}$, Eduardo Blanco-Davis ${ }^{3 *}$, Zaili Yang ${ }^{3}$, Xinping Yan ${ }^{1,2}$

4 ${ }^{1}$ Intelligent Transport Systems Research Centre (ITSC), Wuhan University of Technology, Wuhan, China
$5{ }^{2}$ National Engineering Research Centre for Water Transport Safety (WTSC), MOST, Wuhan, China
$6{ }^{3}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, Liverpool, UK
7
8 *Corresponding Author: Jinfen Zhang* and Eduardo Blanco-Davis*
9
10 Abstract: Human factors contribute to majority of maritime accidents. This study proposes an advanced methodology for maritime accident prevention strategy formulation from a human factor perspective. It is conducted by incorporating Bayesian network (BN) and Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) in a multi-criteria decision-making system. In order to develop rational accident prevention strategies, this work integrates Multiple Correspondence Analysis (MCA), Hierarchical Clustering (HC) and Classification Tree (CT) to generate strategies and describes accident types as criteria for a new multi-criteria risk-based decision-making system. Specifically, MCA is performed to detect patterns of contributory factors explaining maritime accident types. It is complemented by HC and a CT, aiming at creating different classes of vessels. Next, a Bayesian-based TOPSIS model is built to illustrate the features of multiple criteria and the relations among alternatives (i.e. strategies), so as to select the best-fit strategies for accident prevention. The results show that the information, clear order, and safety culture are the three most effective recommendations for maritime accident prevention considering human errors, which presents new insights for accident prevention practice for maritime authorities.

23 Keywords: Accident investigation, maritime accidents, human factors, accident prevention, TOPSIS, BN.

# 1. Introduction 

Maritime accidents may cause loss of human lives, damage to the environment, and loss of economy (Zhang and Thai, 2016). Most maritime accidents are characterised by low probability but high consequence, which implies the significance of risk assessment for shipping activities. It is also recognised that organisation, working condition, and navigational environment are among the major driving forces to maritime accidents (García-Herrero et al., 2012). Although modern ships have been equipped with advanced technologies, including e-navigation technology, onboard information, bridge resource management systems, human factors still reveal a major contribution to maritime accidents.

Generally, the International Maritime Organisation (IMO) focused on human factors much later than the studies and regulations in other transportation modes such as aviation or railway (Schroder-Hinrichs et al., 2011). The maritime sector initiated the studies on the contribution of human and organisational factors (HOFs) from the occurrence of the capsizing of the Herald of Free Enterprise in 1987 (Transport, 1987). Since then, accident investigations pay more attention to human factors in maritime safety. Statistically, human failures/errors account for approximately $80 \%$ of maritime accidents, which play an essential role in terms of accident prevention (Trucco et al., 2008; Tzannatos, 2010; Fan et al., 2018). Human factors in maritime accidents are usually associated with other relevant factors, including workplace conditions, physical and natural environment, procedures, technology, training, organisation, management, as well as individual factors (e.g. fatigue, task load, mental state) (Psarros, 2015). Human factors are often viewed as causes behind anything that goes improperly at sea.

the notification of an accident, maritime administrations may carry out the investigation in order to learn how safety-critical systems failed and why the specific accident happened (Schroder-Hinrichs et al., 2011). Many maritime administrations take this opportunity to review regulations, standards and management associated with technical and non-technical skills related to navigation. To mitigate the risk and improve the safety of marine transportation, IMO introduced the Formal Safety Assessment (FSA) methodology for its applications to the rule-making process (IMO, 2002; IMO, 2013). Moreover, the majority of marine accidents or incidents and hazardous events can be avoided by risk management and countermeasures such as operational procedures or training (Vander Hoorn and Knapp, 2015).

Generally, accidents are investigated for serving as performance indicators for decision making or policy making, supporting data for research, dealing with responsibility allocation, or to take a disciplinary action against crews onboard (Stoop, 2003). It is significant to draw lessons from accidents to prevent reoccurrence of similar events, incidents, or accidents in the future. Maritime accident prevention strategies have been proposed to reduce the risk level of navigation. And recommendations from maritime accident investigation may provide insight into the details of underlying actions or decisions of stakeholders (Stoop, 2003). Only focusing on better analysis methods for maritime accidents does not contribute to rational recommendations. Other issues like multi-criteria decision making bring new perspectives on investigations (Liu et al., 2016; Othman et al., 2015), which reflects adjustments to how factors control over the performance of systems, rather than analysing single factor that contributes to the causation of accidents.

Some other research works reveal the human factors' significance in accident prevention accounting for multiple criteria (Othman et al., 2015; Antão and Guedes Soares, 2019). Human factors have been proposed

as the main contributor and significant issues to serious maritime accidents. However, the lack of effective information and poor quality of data restrain the steps of accident investigation in view of human factors. For example, the databanks for maritime accidents are filled with uncertain records on the situations of accidents. Furthermore, working on extracting human factors from the accident reports which contain details on the process of accidents is time consuming. From this point of view, it is necessary to develop a methodology to incorporate human factors into decision making for effective accident prevention.

A methodology for analysing the human factors and their contribution to maritime accident prevention is proposed in this paper by incorporating Bayesian Network (BN) and TOPSIS. The rest of the paper is structured as follows. The literature review on accident investigation and multi-criteria decision-making systems used for accident prevention is conducted in Section 2. Section 3 demonstrates the methodology of integrating Multiple Correspondence Analysis (MCA) and Hierarchical Clustering (HC) to generate strategies, and BN modelling and TOPSIS method to prioritise the generated strategies. In section 4, the detailed data collection, generation of strategies, and the results of the Bayesian-based TOPSIS model are present and discussed with illustrative real cases. Finally, Section 5 concludes the paper.

# 2. Literature review 

### 2.1 Accident investigation in maritime transportation

By the end of the $19^{\text {th }}$ century, it had been required to clarify the responsibility of the events by investigation of naval disasters. Such investigations were followed by disciplinary actions, focusing on the role of the captain and officers on board, but did not take organisational, policy and institutional factors into account.

Then, independent accident investigation agencies were established by law and act as an independent organisation, avoid the contrary interest with maritime authorities. Besides clarification of the blame, they focused on understanding what exactly happened by analysing system safety deficiencies. As the growing interest of the public after serious accidents, they also helped victims and their families come to terms with their suffering (Stoop, 2003).

There is not lacking of research on how to evaluate recommendations for accident preventions in the literature. For instance, strategies for dealing with resistance to recommendations derived from Swedish accident investigators are developed. However, they did not find out how common or widespread the strategies are (Lundberg et al., 2012). Wan et al. (2019) developed a model to assess risk factors of maritime supply chains by integrating a fuzzy belief rule approach and Bayesian networks for rational accident prevention. The investigations on multi-criteria decision making issues emerge for rational recommendations (Liu et al., 2016; Othman et al., 2015). In addition, research suggested that significant work remained to be done after having the causations identified. Yang et al. (2018) proposed a Bayesian Network-based approach to analyse risk factors influencing Port State Control (PSC) inspections and predict the detention probabilities under different situations. The findings could support port authorities to rationalise their inspection regulations as well as the allocation of the resources. From this point of view, sorting out recommendations is based on to control the variables in the Multi Criteria Decision Making (MCDM) systems rather than just explaining the variables (Stoop, 2003).

Moreover, human factors are significant issues among accident preventions accounting for multiple criteria (Othman et al., 2015). For instance, Antão and Guedes Soares (2019) suggested to proactively optimise

accident prevention through the development of specific procedures for fishing vessels and training for recreation vessels' crews, and reactively reduce the consequences of occurrence through equipping more lifesaving equipment to the areas more prone to specific accidents. However, it revealed limited information regarding the direct impact of a human error into an occurrence. Othman et al. (2015) introduced TOPSIS method to maritime accident investigation and found that Senior Deck Cadets (SDC) are the most affected by distractions during the ship's operation, but did not illustrate the relations among sub-criteria. From this point of view, it is worth developing a methodology to incorporate human factors into effective accident prevention.

Also, there are several publications focusing on HOFs by analysing accident reports (Schroder-Hinrichs et al., 2011; Macrae, 2009; Uğurlu et al., 2015). Analysing maritime accident reports has been a rational option to generate insights for accident prevention (Fan et al., 2020). Chauvin et al. (2013) utilised MCA and hierarchical clustering to reveal three patterns of factors but was restricted by a small number of reports with a large number of variables. It had been developed as a rational way to explain the causations behind maritime accidents by statistical analysis. Moreover, it was associated with human factors or human performance into maritime accident modelling. Sotiralis et al. (2016) developed the BN model integrating elements from the Technique for Retrospective and Predictive Analysis of Cognitive Errors (TRACEr) and calculated the collision accident probability. It was applied to assess the collision risk of a feeder operating in Dover strait due to human error. Through the review of 41 accident investigation reports, Schroder-Hinrichs et al. (2011) found that organisational factors were not identified by maritime accident investigators to the extent which the IMO guidelines expected. In addition, Fuzzy Cognitive Map (FCM)-based technique (de Maya et al. 2019) was applied to generating weight the importance of human factors as prior failure probabilities, which helped create the BN model. The accident scenario analysis showed that the lack of safety culture contributed the

In general, the maritime sector lacks critical mass in historical accident data to support meaning statistical analysis of various factors contributing to maritime accidents. Besides, the uncertainty and incompleteness of database further contributes to the limitation of statistical research, especially in view of human factors.

# 2.2 Multi-criteria decision-making for accident prevention 

MCDM provides decision makers with a comprehensive approach to determine complex, poorly defined problems with multiple and interrelated criteria. Recommendations based on maritime accident investigation is in essence a MCDM issue involving reducing the risks of navigation considering frequencies and severities of different types of accidents, cost, social benefits, and their associations. Generally, some criteria can be measured numerically, and others cannot, as each criterion may have different units of measurement, quality characteristics, and weights (Zavadskas et al., 2016). Individually, the decision maker of MCDM problem ranks alternatives after the qualitative or quantitative analysis of a set of criteria, and find the most desirable alternative based on the intersection of selected criteria (Yue, 2011).

The MCDM methods provide solutions for a wide range of society, economics, engineering, and management (Ming et al., 2014; Efe, 2016). MCDM has been applied to many sectors, such as system selection (Sadeghi et al., 2013), location selection (Keršulienė and Turskis, 2014), technology selection (Ishizaka et al., 2013), and robot selection (Vahdani et al., 2013; Rashid et al., 2014) . Besides, MCDM has been developed and applied to the maritime sector, especially for accident prevention. For instance, Hollnagel (2004) developed barrier functions and modelled barrier systems that will enable informed decisions for system changes for

accident prevention rather than accident analysis. It was stated that accidents could be prevented through a combination of multiple criteria, including performance monitoring and barrier functions, rather than through the elimination of causes, which is a proactive approach. From this point of view, it provided insights for the recommendations in the cases of accidents and decision making of onboard operations for seafarers.

TOPSIS has been one of most popular methods for solving the MCDM problem, which was initially designated to solve crisp valuated MCDM problems (Behzadian et al., 2012). Wu et al. (2016) introduced TOPSIS for final decision-making, integrated with consistency-based linear programming model to obtain the interval weights of attributes, which provided a practical decision framework for safety control of not under control ship. Then, Wu et al. (2018) incorporated evidential reasoning and TOPSIS into group decision making for handling ship without command. Othman et al. (2015) used a TOPSIS method to rank the alternatives in the order of how they are affected by the psychological problem of distraction. It proved that Senior Deck Cadets (SDC) are most affected by distractions when they are engaged in the ship's operation.

Due to the advantage of its application in a fuzzy environment, Liu et al. (2016) proposed an extended TOPSIS model to compare fuzzy numbers with the same expected value and make the fuzzy number with lower expected value but higher reliability to outperform that with higher expected value but lower reliability. In addition, the fuzzy TOPSIS approach was applied to sort through alternative solutions to improve port safety (Özdemir, 2016). In this way, TOPSIS is well known for multi-criteria decision making problems but cannot represent the relations among alternatives, nor their effects to criterion of interest.

Bayesian Network (BN) has been widely used for risk analysis and accident prevention. Yang et al. (2018) proposed a Bayesian-based approach to analyse risk factors influencing PSC inspections and simulated

scenario to illustrate the multiple factors' influences on vessel detention. It revealed BN's advantages of representing causal relationships between variables and predicting the effect of factor changes to the criterion of interest. However, BN only focuses on single criteria of the system. Although it provides a powerful decision support tool and predicts properties of safety systems, BN is not applicable for multi-criteria decision making cases. Combining the merits of BN and TOPSIS, Yang et al. (2009) developed a methodology to allocate all relevant decision attributes in the form of the nodes in BNs to produce certain associated attribute values and integrate with TOPSIS to rank a set of options. It was evidence that the BN-based TOPSIS method was applicable to the MCDM system.

However, there are few studies on the later stages of the accident investigation process focusing on human factors where recommendations are formulated and assessed. One novelty of this study lies in strengthening the significance of human factors in accident investigation and generate related strategies to support the recommendations for accident prevention. That is to say, what risk factors contribute to human errors and how to formulate strategies from analysing risk factors, are focal points of the study. Besides, research on potential correlations between alternatives in the maritime domain is scanty. In order to effectively select countermeasures, another novelty of this study lies in modelling the MCDM problem considering interrelations among strategies and provide insights for the accident preventions accounting for human errors.

# 3. Methodology 

In order to formulate the maritime accident prevention strategy from human factors perspective, several approaches have been applied to promote the study. Firstly, the raw database is sorted out from the maritime accident reports, followed by statistical analysis of contributory factors in maritime accidents. This work

integrates Multiple Correspondence Analysis (MCA), Hierarchical Clustering (HC) and Classification Tree (CT) to generate strategies and describes accident types as criteria for a new multi-criteria risk-based decision-making system. Specifically, MCA is performed to detect patterns of contributory factors explaining maritime accident types. It is complemented by HC and a CT, aiming at creating different classes of vessels. Next, a Bayesian-based TOPSIS model is built to illustrate the features of multiple criteria and the relations among alternatives (i.e. strategies), so as to select the best-fit strategies for accident prevention.

# 3.1 Statistical analysis of risk factors and strategy formulation 

The risk factors contributing to human errors are selected from the investigation of 161 reports involving 208 vessels and thresholding according to the probability of occurrence in case of data distortion (Wan et al., 2017; Wang and Yang, 2018). The data is obtained from the case-by-case analysis of recorded maritime accidents from the Maritime Accident Investigation Branch (MAIB), and the Transportation Safety Board of Canada (TSB) that occurred from 2012 to 2017. MCA is performed to detect patterns of risk factors explaining accidents. Then it is completed with a Hierarchical Clustering, aiming at creating a Classification Tree. In this way, the strategies are formulated based on risk factors analysis from the above investigation.

There is a discussion that accident prevention strategies should focus on reforming the system by systematic thinking approaches rather than on fixing the broken poles. Although little guidance exists on how to translate incident data into accident prevention strategies that address the systematic causes of accidents (Goode et al., 2016), it has been a feasible approach to develop strategies by the statistical analyses of accidents or incidents. This study generates strategies for accident prevention based on the contributory factors analysis by conducting MCA associated with HC and CT. Such statistical analysis considers the patterns of causation

factors so as to reveal the rational generation of strategies.

MCA is a geometric data analysis method that explains the structure hidden in a data set for categorical data, which is the counterpart of Principal Component Analysis. It can represent data as points in low-dimensional Euclidean spaces, particularly applicable for a moderate number of individuals and a significant number of variables (Burt, 1950; Chauvin et al., 2013). Hierarchical Clustering is a clustering approach that classifies individuals in a hierarchy of clusters, while Classification Tree learning is a data mining method that uses input variables to predict the class to which the data belong (Hastie et al., 2005; Chauvin et al., 2013).

The above analyses presented are conducted using the R packages FactoMineR. It generated the criteria of maritime accidents in the form of accident types and the strategies for the countermeasures derived from above categorical data.

# 3.2 A BN-based approach to reveal interrelations among strategies 

In order to facilitate the modelling of the relations among strategies, BN is applied into the analysis of the maritime accident types under various risk factors. The data is obtained from the case-by-case analysis of recorded maritime accidents, and the risk factors in BN are from both maritime accident reports and the literature (Chauvin et al., 2013; Graziano et al., 2014; Kum and Sahin, 2015).

Human factors in maritime accidents are usually combined with other external factors, such as sea condition, weather condition, fairway traffic, and vessel condition that affect the safety procedure in navigation. From this perspective, it is beneficial to combine human factors with such external factors to investigate their combined effect on maritime safety. Therefore, the common factors with frequencies higher than average value,

$19.35 \%$, combined with the factors identified from the literature (Wang and Yang, 2018), encompass a
collection of 25 risk factors, as present in Table 1. Most of the definitions of variables' states can be extracted from accident investigation reports from MAIB or TSB, including 'accident type', 'ship type', 'hull type', 'ship operation', and 'voyage segment'. Some variables are degraded according to the literature (Wang and Yang, 2018), including 'ship age', 'length', and 'gross tonnage'. Then, 'vessel condition', 'communication', 'supervision', etcetera, are grading based on whether it is blamed for the faults in accidents, as data characteristic described in the reports. In addition, accident types are present in Table 2.

Table 1 The risk factors identified from the literature and accident reports



Table 2 Accident type identification


A data-driven method, Tree Augmented Network (TAN), which relies on the learning algorithm in the BN model, was developed to generate BN structure and CPTs calculation by Netica software package (Norsys, http://www.norsys.com ). After sensitivity analysis, this model was used to illustrate the relations among the strategies, and provide the intersection of strategies under various criteria by adjusting the BN.

From this point of view, the strategies derived from Section 3.1 are revealed as risk factors with multiple states in the BN. By giving state to the risk factors in BN, the strategies are assumed to be given, the findings of the node of accident types are revealed as changeable values in the crisp values for the TOPSIS. The results of the networks are demonstrated in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Results of BN by TAN learning

Figure 1 presents the results of TAN involving all the retained 25 risk factors. Among the accidents, grounding and collision are among the most frequent accident types, accounting for $20.3 \%$ and $21.2 \%$, respectively. In addition, the relationships among various factors are generated by this data-driven approach. By adjusting one state of the variable, the differences of the findings will be reflected in BN.

# 3.3 TOPSIS for the formulation of accident prevention strategies 

In this section, TOPSIS method is applied to explaining the priorities among different strategies and the formulation of maritime accident prevention decisions. TOPSIS was proposed as an alternative to the ELECTRE method (Yoon, 1981; Yoon and Hwang, 1995), which was generated based on the idea that if an alternative has the shortest distance to the ideal solution within the Euclidean space (Streimikiene et al., 2012), and can be considered as the best one in the system. However, it is possible that such a solution that has the shortest Euclidean distance to the ideal solution also has a shorter distance to the negative ideal solution (Tzeng et al., 2002). Therefore, the TOPSIS method considers both the above distances. Moreover, modified TOPSIS method utilised the 'city block distance' (Yoon and Hwang, 1995) instead of the Euclidean distance, so that any solution that has the shortest distance to the positive ideal solution (PIS) can be guaranteed to have the farthest distance to the negative ideal solution (NIS) (Tzeng et al., 2002).

In this study, the nine states of accident types are treated as multiple criteria, and the strategies selected by statistical analysis are as alternatives in the TOPSIS. The procedures of TOPSIS include the following steps.

Step 1: Based on the crisp values obtained from BN model, an evaluation matrix consisting $m$ alternatives and $n$ criteria, where $m=9$ representing nine strategies, $n=9$ representing nine accident types is created, with the

intersection of each alternative and criterion given as $X_{i j}$, therefore a matrix $\left(X_{\mathrm{ij}}\right)_{m \times n}$. Each intersection is obtained from each state value of the node of accident type in BN model developed in Section 3.2.

Step 2: $\left(X_{\mathrm{ij}}\right)_{m \times n}$ is normalised to form the matrix $R=\left(r_{i j}\right)_{m \times n}$, using the following equation:
$r_{i j}=\frac{x_{i j}}{\sqrt{\sum_{i=1}^{m} x_{i j}{ }^{2}}}, i=1,2, \ldots, m, j=1,2, \ldots, n$

In this way, the normalisation of the matrix for the performance of strategies is obtained.

Step 3: Calculate the weighted normalised decision matrix $V=\left(\mathrm{v}_{i j}\right)_{m \times n}=\left(w_{j} r_{i j}\right)_{m \times n}, i=1,2, \ldots, m$, where $w_{j}=\frac{W_{j}}{\sum_{j=1}^{n} W_{j}}, j=1,2, \ldots, n$

So that $\sum_{j=1}^{n} w_{j}=1$, and $W_{j}$ is the original weight given to the criterion, representing initial correspondence value for the states of accident type in BN. That is to say, in this study, the weight of each criterion is given based on the occurrence probability of the accidents.

Step 4: Determine the NIS $A^{-}$and the PIS $A^{+}$.
$A^{-}=\left\{\left\langle\max \left(t_{i j} \mid i=1,2, \ldots, m\right) \mid j \ni J_{-}\right\rangle,\left\langle\min \left(t_{i j} \mid i=1,2, \ldots, m\right) \mid j \ni J_{+}\right\rangle\right\} \equiv\left\{t_{w j} \mid j=1,2, \ldots, n\right\}$,
$A^{+}=\left\{\left\langle\min \left(t_{i j} \mid i=1,2, \ldots, m\right) \mid j \ni J_{-}\right\rangle,\left\langle\max \left(t_{i j} \mid i=1,2, \ldots, m\right) \mid j \ni J_{+}\right\rangle\right\} \equiv\left\{t_{b j} \mid j=1,2, \ldots, n\right\}$

Where, $J_{+}=\{J=1,2, \ldots, n\}$ is associated with the criteria having a positive impact, and $J_{-}=\{J=1,2, \ldots, n\}$ is associated with the criteria having a negative impact. However, the criteria including nine types of accidents proposed herein all have negative impact.

276 Step 5: Calculate the Euclidean distance (commonly in most applications) measurements between target
strategies $i$ and the worst condition NIS $A^{-}$

$$
S^{+}=\left(\sum_{j=1}^{p}\left|v_{i j}-v_{j}^{+}\right|^{2}\right)^{0.5}, i=1,2, \ldots, m, j=1,2, \ldots, n
$$

279 And the distance measure between target alternative $i$ and the best condition PIS $A^{+}$:

$$
S^{-}=\left(\sum_{j=1}^{p}\left|v_{i j}-v_{j}^{+}\right|^{2}\right)^{0.5}, i=1,2, \ldots, m, j=1,2, \ldots, n
$$

281 Where $S^{-}$and $S^{+}$are the distance from the target alternative, $i$ to the worst and best strategies, respectively.

282 Step 6: Calculate the similarity to the worst condition, representing the performance of strategies.

$$
C_{1}=\frac{S^{-}}{\left(S^{+}+S^{-}\right)}, 0 \leq C_{i} \leq 1, i=1,2, \ldots, m
$$

$C_{1}=1$ if and only if the alternative solution has the best condition; and $C_{i}=0$ if and only if the alternative solution has the worst condition.

286 Step 7: Rank the strategies for maritime accident prevention according to the value of $C_{1}(i=1,2, \ldots, m)$.

# 4. Case study 

### 4.1 Maritime accident prevention strategy generation

Based on the statistical analysis in Section 3.1, the top 14 risk factors are selected for MCA according to the frequency threshold value of 0.19 , which is the average value among all frequencies. That is to say, the variable

with a frequency larger than 0.19 is selected as one of the 14 risk factors, as shown in Table 3.

Table 3 The frequencies of risk factors selected for MCA



293 In order to point out patterns of contributory factors (Chauvin et al., 2013), these risk factors are employed into MCA (see Figure 2).

295 Axis 1 explains $12.01 \%$ of the inertia. It is determined by attributes Information (no), weather_condition (no), sea_condition (no), A18 (no). It opposes:

- The modalities: Information (no), weather_condition (no), sea_condition (no), A18 (no), on the positive side, to
- The opposite modalities on the negative side.

300 As far as individual vessels are concerned, it opposes:

- Vessels experiencing an accident without sufficient information, in poor condition of sea and weather, having problems with ambiguous code, endorsement, regulations, procedure, or instructions, to
- Vessels experiencing an accident the opposite conditions.

304 This axis quantifies the intensity of environmental and management problems.


![img-1.jpeg](img-1.jpeg)

Figure 2. MCA factor map for contributory factors

Then, hierarchical clustering is carried out from the coordinates of individuals on all the axes. The analysis shows three different classes of cases, as shown in Figure 3. Associated with a classification tree (see Figure. 4), it shows the variables that best explain vessel allocation to the different classes among the above factors, which is helpful for the generation of strategies. Each tree distinguishes a class, where there are three classes. The left side of each branch corresponds to a "yes" to the question in the root, whereas the right side corresponds to a "no". Under each leaf, the class type and percentages of elements of each class in the leaf appear; the first line ' 1 ' means first class and $.23 / .67 / .10$ means that there are $23 \%$ of accidents belonging to the first class, $67 \%$ of accidents belonging to the second class and $10 \%$ of accidents of the third class. The

327 presence of weather condition appears to be a characteristic of the first class, which means many accidents are
328 caused by rain, wind, fog, or poor visibility. Moreover, weather condition factor is always associated with a
329 lack of safety culture, poor sea condition, unclear order, and dysfunctional management system. Class 1 is
330 well characterised by lack of safety culture, and integration of poor sea condition and unclear order. Class 2
331 is revealed to be connected with weather condition or sea condition, which is less affected by human factors.
332 Class 3 is reasonably characterised by the dysfunctional management system.
![img-2.jpeg](img-2.jpeg)

Figure 3 Hierarchical clustering for different classes of cases

![img-3.jpeg](img-3.jpeg)

Figure 4 Classification tree for variables explaining vessel allocation to different classes

Figure 4 illustrates the significant factors and the combination of them which classify the accidents. By doing this, such factors can be selected to support generating strategies for maritime accident prevention. There are strategies derived from the above results considering human factors. It should be noted that although weather and sea condition are significant factors from the statistical analysis, it reveals less information for the accident prevention countermeasures. Therefore, attention is given to factors associated with such environmental factors so as to propose the strategies to solve the safety issues.
(1) A21 (Safety culture): vessels should keep and maintain a good safety culture, and seafarers onboard should have precautionary thought.

(2) A6 (Clear order): good and clear order from documents is supposed to be accurately interpreted, and the requirements of a safe manning document should be applied.
(3) A20 (Management): appropriate management system should include shore management, maintenance management, bridge source management, onboard management, safety management systems, port service, qualification examination, inadequate training, practice, emergency drill.
(4) Information: sufficient and updated information should be provided; any insufficient or lack of updated information (e.g., poor quality of equipment data, falsified records of information, relies on a single piece of navigational equipment, without working indicators or light for necessary observing) should be avoided.
(5) A18 (Regulation): appropriate code, endorsement, regulations, procedure, instructions, formally published guidance, operation manual, requirement are required, and any ambiguous documents should be revised.
(6) A19 (Risk assessment): ship owners and ship authorities should keep enough risk assessment for the ship and crews.
(7) A11 (Experienced): crews should be familiar with equipment knowledge; experienced and well-prepared seafarers are required.
(8) A2 (Supervision): adequate supervision and supports should be given when on duty, and lone watchkeeper or working isolated, improper supervision of loading operation should be eliminated.
(9) Equipment: devices and equipment onboard should be operated correctly before the voyage; any

363 circumstances for problematic equipment (e.g., Bridge Navigational Watch \& Alarm System (BNWAS) 364 switched off, alarm system not in the recommended position or not noticed) should be eliminated.

# 3654.2 Calculation of TOPSIS matrices derived from BN 

366 Each accident type is seen as a criterion for the multiple criteria decision making. According to the BN 367 structure and results in Section 3.2, the weight of each criterion was given based on the probability of 368 occurrence of the accidents, which is revealed as initial correspondence value for the state of accident type in BN. Moreover, the evaluation matrix consisting of nine alternatives and nine attributes, with the intersection 370 of each alternative and criterion was given in Table 4, which generated step 1 of the TOPSIS method, where $S 1-S 9$ represent different types of accidents.

Table 4 Create an evaluation matrix for 9 alternatives and 9 attributes


373 With regards to the intersection of each alternative and criterion, crisp values in TOPSIS are generated from 374 BN rather than the fuzzy environment or vague information, which utilises the advantages of the data-driven 375 approach of BN accounting for the inter-relations among criteria. To be specific, this step overcomes the 376 drawback of the TOPSIS method, considering the interaction among strategies in BN model, which is more

rational in the real word. Besides, the weight of each criterion is determined by the initial probabilities of accident types, which implies that accident type with higher probability accounts for higher weight for MCDM.

# 4.3 Maritime accident prevention strategy selection 

In order to obtain the normalised matrix, calculations have been conducted to generate Table 5, where S1-S9 represent different types of accidents.

Table 5 The normalised matrix for the performance of strategies


Then weighted normalised matrix is obtained, followed by calculating the ideal best and ideal worst values.
After that, the Euclidean distances from the ideal best solution and the ideal worst solution are calculated by the equations in Section 3.3. At last, TOPSIS calculates the performance score and ranks the strategies, which is shown in Table 6.

Table 6 Calculation of performance score and the rank of strategies



389 From this table, it is evidence that strategies about equipment, information, and clear order are the top three recommendations for maritime accident prevention considering human factors. To be specific, these strategies are as follows.
(1) Effective and updated information should be provided. Any insufficient or lack of updated information (e.g., poor quality of equipment data, falsified records of information, relies on a single piece of navigational equipment, without working indicators or light for necessary observing) should be avoided.
(2) Good and clear order from documents is supposed to be accurately interpreted, and the requirements of a safe manning document should be applied.
(3) Vessels should keep and maintain a good safety culture, and seafarers onboard should have precautionary thought.

Besides, the first strategy about equipment shows most prospects among all strategies, based on the comparison of $C_{i}$ values. These values represent the similarity to the worst condition, which are used as the indicators for strategy ranking, as demonstrated in Section 3.3. It can be seen from Table 6 that $C_{i}(0.528)$ of 'Information' which ranks first, indicates significant performance in order to prevent accidents, compared to

# 4.4 Model evaluation 

### 4.4.1 Sensitivity analysis

To validate the model, it is examined by testing the combined effect of multiple RIFs to the accident types in BN model, because it contributes crisp values into TOPSIS matrix.

According to the literature, there are two axioms to be satisfied in the sensitivity analysis (Fan et al., 2020). For example, the 'information' in Figure 1 is selected as the first node, the state generating the highest changed value of 'collision' (S1) in 'accident type' is increased by $10 \%$, while the state generating the lowest changed value of 'collision' in 'accident type' is decreased by $10 \%$. This procedure is written as ' $\sim 10 \%$ '. And the same approach is applied to the next RIF 'vessel condition', and the integrated changed value is obtained and updated. From Table 7, the updated values of ' $S 1$ 'are gradually increasing when more RIFs are included. Similarly, the same updating procedures are applied into the state $2,3 \ldots 9$ in 'accident type' respectively, until all states are included. In this way, the updated values of the target node are gradually increasing or decreasing along with the continuously changing RIFs, so that two axioms are examined.

Table 7 Accident rate of minor change in RIFs


# 4.4.2 Reliability test for TOPSIS 

The reliability test for BN-based TOPSIS method is conducted by adjusting the human factors, which includes more strategies in the model to observe updated results of the ranking. Firstly, the less important human factor A12 has been added into maritime accident prevention strategies, which formulates a new evaluation matrix for 10 alternatives and 9 attributes, shown in Table 8. The $10^{\text {th }}$ alternative represent the strategy A12: The duties and the severity of the condition should be appropriately estimated with enough alertness.

Table 8 New evaluation matrix for 10 alternatives and 9 attributes (after adding A12)


425 Secondly, the corresponding weighted normalised matrix, Euclidean distances from the ideal best and ideal worst have changed accordingly. At last, the performance score and the strategies ranking are found in Table 9 .

Table 9 Performance score and strategy ranking after adding A12



429 Compared to the results of Table 6, it is evidence that the input of strategy A12 does not influence the ranking of strategies in Section 4.3, although the values of $C_{i}$ change slightly. In this way, it shows the reliability test of the above BN-based TOPSIS method.

432 With regard to the results of BN-based TOPSIS model, it demonstrates the rational selection of alternatives, as well as the decision making of multiple criteria considering the relations among multiple strategies.

434 Compared to the approach that proposed countermeasures by scenario simulation using BN (Yang et al., 2018), this method reveals some advantages. Although being able to reduce the probability of one state of the node by scenario simulation, BN cannot reflect the best scenario to reduce the overall probability of all accident types in this study by adjusting single factor or the combined factors. Therefore, TOPSIS method is applied into the final step for MCDM.

439 Overall, this method overcomes the drawback of the BN method that cannot determine the best scenario in multiple criteria system and the disadvantage of TOPSIS method that cannot reflect the crisp value by considering the correlations among alternatives. The results present the ranking order of strategies in view of human factors, which illustrates strategies that should be taken priority for maritime accident prevention.

# 5. Conclusion 

This study proposes an advanced methodology for human factors analysis and maritime accident prevention by incorporating BN and TOPSIS in the MCDM system. In order to generate the prevention strategies, it integrates MCA, HC and CT to generate alternatives for MCDM. MCA is performed to detect patterns of contributory factors explaining maritime accident types. It was also completed with HC, aiming at creating different classes of vessels, and a CT. Then, Bayesian-based TOPSIS model is built to illustrate the values of criteria and the relations among strategies for accident prevention. Specifically, TOPSIS is adopted for the strategies selection to generate new insights for accident prevention recommendations for transport authorities given human factors.

The results convey that strategies about information, clear order, and safety culture are the top three recommendations for maritime accident prevention considering human factors. In order to prevent accidents related to human factors, these strategies should be developed with higher priority to provide insights for the improvement of maritime safety. From these perspectives, transport authorities obtain insights from past accidents to generate significant strategies for accident prevention. Moreover, it would contribute to the accident investigation and human factors research in the maritime field to provide effective strategies or recommendations for the maritime industry and policymakers.

## Author contributions

- Shiqi Fan: Conceptualisation, Methodology, Software, Validation, Formal analysis, Data Curation, Visualization, Writing - Original Draft

- Jinfen Zhang: Conceptualisation, Writing - Review \& Editing,
- Eduardo Blanco-Davis: Supervision, Writing - Review \& Editing,
- Zaili Yang: Resources, Writing:- Review \& Editing
- Xinping Yan: Project administration, Funding acquisition, Supervision


# 466 Declaration of interest 

467 The authors declare that they have no known competing financial interests or personal relationships that could 468 have appeared to influence the work reported in this paper.

## Acknowledgements

470 The research was sponsored by National Key Technologies Research \& Development Program 471 (2017YFE0118000), Funds for International Cooperation and Exchange of the National Natural Science 472 Foundation of China (grant No. 51920105014). Gratitude is due to the European Union's Horizon 2020 473 Research and Innovation programme under the Marie Skłodowska-Curie grant agreement No 823904 474 (ENHANCE) and No 730888 (RESET).
