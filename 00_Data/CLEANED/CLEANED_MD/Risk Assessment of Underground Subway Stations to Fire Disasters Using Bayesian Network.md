# Article 

## Risk Assessment of Underground Subway Stations to Fire Disasters Using Bayesian Network

Jiansong Wu *, Zhuqiang Hu, Jinyue Chen and Zheng Li<br>Department of Safety Technology and Management, China University of Mining \& Technology, Beijing 100083, China; 1510120108@student.cumtb.edu.cn (Z.H.); 1510130123@student.cumtb.edu.cn (J.C.); 1510130109@student.cumtb.edu.cn (Z.L.)<br>* Correspondence: 201310@cumtb.edu.cn; Tel.: +86-10-6233-9029

Received: 18 September 2018; Accepted: 16 October 2018; Published: 22 October 2018


#### Abstract

Subway station fires often have serious consequences because of the high density of people and limited number of exits in a relatively enclosed space. In this study, a comprehensive model based on Bayesian network (BN) and the Delphi method is established for the rapid and dynamic assessment of the fire evolution process, and consequences, in underground subway stations. Based on the case studies of typical subway station fire accidents, 28 BN nodes are proposed to represent the evolution process of subway station fires, from causes to consequences. Based on expert knowledge and consistency processing by the Delphi method, the conditional probabilities of child BN nodes are determined. The BN model can quantitatively evaluate the factors influencing fire causes, fire proof/intervention measures, and fire consequences. The results show that the framework, combined with Bayesian network and the Delphi method, is a reliable tool for dynamic assessment of subway station fires. This study could offer insights to a more realistic analysis for emergency decision-making on fire disaster reduction, since the proposed approach could take into account the conditional dependency in the fire propagation process and incorporate fire proof/intervention measures, which is helpful for resilience and sustainability promotion of underground facilities.


Keywords: urbanization and sustainability; subway station fire; dynamic risk assessment; Bayesian network

## 1. Introduction

The urgent demands for land resources in urban development, more and more underground spaces, such as subway stations, underground malls, parking lots, and so on, are explored and constructed. Due to the compact structure, high population density, limited number of exits, and other factors, serious consequences can be induced by disasters in subway stations, which have become a great public concern. According to the statistics, fire accidents rank at the top of the list for subway station disasters, making up nearly $30 \%$ of the total accidents that occurred in subway stations around the world. The subway system has been playing an extremely important role in urban transportation development these years. Therefore, it is of great importance to carry out disaster prevention and emergency response work in subway stations, especially on the risk assessment of fire disaster in the subway stations, which is of great significance for urbanization and sustainability.

In the past ten years, a lot of scholars have been focusing on studying the problem of fires in subway stations. As for the methods used to analyze subway station fires, experimental approaches have been started earlier. According to similarity theory, the physical phenomenon of subway station fires can be simulated in full-size or reduced-size experimental apparatuses for subway stations. The fire characteristics, like heat release rate, temperature distribution, smoke concentration, and radiation heat, are obtained [1-6]. For some subway station fire scenarios,

the experimental technique could provide some valuable data to examine the fire combustion and spreading process. However, for fires in some complex subway station layouts, experimental analysis is risky, time-consuming, and costly. Recently, with the development of computer science and technology, and numerical methodologies, numerical tools have been a popular way to investigate subway station fires. Many computational fluid dynamic (CFD) models or software, such as FLUENT, and FDS, among others, are widely used in analyzing fire smoke evolution in subway stations and tunnels [7-13]. CFD-based simulations can reproduce well the evolution process of subway station fires if appropriate initial and boundary conditions are implemented. At present, the CFD-based numerical results on subway station fire characteristics and development process are of significance for making "Preparedness" strategies for fire disaster, e.g., safety evacuation design and fire prevention measures in subway stations. However, for the fire emergency decision, the existing fire simulation model based on CFD is inefficient, because of the large amount of calculations. Consequently, some researchers recently have been working on rapid risk assessment tool for subway station fires from qualitative and quantitative perspectives, based on probabilistic methods and stochastic approaches, like event tree analysis, fuzzy fault tree analysis, cluster analysis, failure modes and effects analysis, optimized neural network, analytic hierarchy process, grey-analytic hierarchy process, etc. [14-20]. Fang et al. established a fire risk assessment system of shopping malls by cluster analysis and Analytic Hierarchy Process (AHP), and calculated the index weight value of the evaluation system [14]. Liu et al. proposed the fault tree model of the main risk factors of subway fires by using fuzzy fault tree analysis, and sorted the critical probability importance of the events at the bottom of the fault tree [15]. Nezhad et al. used Failure Mode and Effects Analysis (FMEA) model and fuzzy theory to evaluate the Zagros subway, and obtained two important fire risks in the Zagros subway line [16]. Roshan et al. employed an event tree analysis method to construct an event tree for each fire event, and calculated the probabilities of multiple scenes to evaluate the fire risk of the Tehran subway station [17]. Yu et al. concluded 21 subway fire risk factors, and then established the subway fire risk assessment model through neural network [18]. Zheng et al. carried out fire risk assessment of a highway tunnel from three levels through a grey-analytic hierarchy process [19]. However, these traditional risk analysis methods, like fuzzy fault tree analysis and event tree analysis, can be very large for complex systems, which brings difficulties to qualitative and quantitative analysis. Traditional risk analysis methods, like fuzzy fault tree analysis and event tree analysis, can be very large for complex systems, which brings difficulties to qualitative and quantitative analysis, and can only use discrete variables for static analysis. The estimated results of optimized neural networks cannot reflect the importance of individual risk factors with poor generalization, and it is not applicable to multi-objective evaluation processes. The grey-analytic hierarchy process has less quantitative data, but more qualitative components, so is not convincing. In addition, some researchers have achieved a lot on the risk analysis of other crowded places with potential fire risk, e.g., finding out the types of bridges most susceptible to fire by statistical analysis of a large number of historical data [21], and proposing a way of weighted factors to quantify bridge fire risk [22].

BN has some attractive advantages over conventional risk assessment methods. Bayesian node variables can be classified with multiple states, which could facilitate various kinds of influential factors. Furthermore, BN can achieve dynamic probability updating with newly emerged evidence [23]. Therefore, Bayesian network has been widely used in process safety and natural hazard assessment. Recently, in fire disaster analysis, like office building fire spread modeling, dwelling fire development, and occupancy escape, safety barrier for fire, ship fire, fire protection systems, subway station evacuation, etc. [24-29]. For subway station fires that refer to many dynamic influencing factors, the risk assessment of fire using Bayesian network is rare.

In order to comprehensively represent and assess the fire risk in subway stations, this study proposes an integrated risk assessment framework for rapid and dynamic modeling of subway station fire using a combination of Bayesian network and the Delphi method. The proposed BN-based framework can not only represent static influential factors, like subway station type, platform type,

fire source position, fire alarm system, ventilation systems, sprinkler system, etc., but also incorporate dynamic fire development information and mitigation measures, such as fire impacts, emergency rescue or intervention measures in the process of fire evolution, and so on. This BN-based framework accomplishes an effective and dynamic "Scenario Response"-based risk and possible "resilience" assessment of subway fire evolution process, which is of great importance to the prevention, evaluation, and control of subway station fires, and is helpful for the resilience and sustainability promotion of underground facilities.

# 2. Methodology 

### 2.1. Bayesian Network

Bayesian network (BN) is a directed acyclic graph (DNG) containing a set of nodes, arcs, and conditional probability tables (CPTs) to reflect the joint probability distributions between node variables. The nodes in BN can be divided into two types: the parent node and the child node, as shown in Figure 1. The nodes in BN can also be divided into three types: root node, intermediate node, and leaf node. The root node has no parent node. The leaf node has no child node. The other nodes are generally called intermediate nodes. BN has been applied to many areas, like chemical accidents, farmland protection, dust explosion, wildfire, water quality, gas pipeline, metro construction, and project risk management, and has been proven to be an effective method because of its flexibility, convenience, and high efficiency [30,31,32,33,34,35,36,37,38,39].
![img-0.jpeg](img-0.jpeg)

Figure 1. A simple example of Bayesian network (BN).
One of BN's advantages is that the joint probability distributions can be simply calculated. When analyzing a BN, if the probability of the variable $X_{i}$ 's parent nodes is defined as $P a\left(X_{i}\right)$, the joint probability distributions $P(X), X=\left(X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right)$ can be expressed as:

$$
P(X)=P\left(X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right) \quad(i=1,2, \ldots, n)
$$

where, $X=\left(X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right)$ represent various BN variables, $n$ is the number of BN variables.
Another advantage of BN is that the probability can be updated dynamically when there is new evidence available. If given a new evidence (event $Y$ ) to BN , the posterior probability of event $X$ $(P(X \mid Y))$ is calculated as:

$$
P(X \mid Y)=\frac{P(X) P(Y \mid X)}{P(Y)}=\frac{P(X) P(Y \mid X)}{\sum_{i=1}^{n} P\left(Y \mid X_{i}\right)} \quad(i=1,2, \ldots, n)
$$

where, $P(Y)$ represents the marginal probability of event $Y, P(X)$ is the prior probability of the event $X$.

### 2.2. Delphi Method

The Delphi method is a kind of technique with structured communication. It can enhance expert experience through an anonymous evaluation of reincarnation by expert groups. It is widely used in forecasting, information emerging, and policy-making [40]. Firstly, a leadership team is formed to form the questionnaire of expertise needed, and to organize the whole process. Next, the experts complete the questionnaire by anonymous evaluation under the organization. Experts anonymously share

opinions and reconsider new information when answering the questionnaire again. Then, effective expert experience could be obtained through a series of repetition. In addition, the coefficient of variation and Cronbach's coefficient alpha are added, to conduct a consistency test for the obtained data, because the Delphi method has no evaluation criteria for the collected data. Finally, the required empirical data can be obtained by averaging the eventual-round collected data. The coefficient of variation $V$ refers to the coordination degrees between experts. The Cronbach's coefficient alpha represents the consistency of the results [41]. Cronbach's coefficient alpha was calculated for each node in the BN, so as to test the data consistency. It is acceptable when $\alpha>0.8$.

$$
V_{j}=\frac{\sigma_{j}}{\bar{x}_{j}}
$$

where $\sigma_{j}$ are variances of the components and $\bar{x}_{j}$ is the average of the components.

$$
\alpha=\frac{K}{K-1}\left(1-\frac{\sum_{i=1}^{K} \sigma_{Y}^{2}}{\sigma_{X}^{2}}\right)
$$

where $\sigma_{X}^{2}$ is variances of the total scores, $\sigma_{Y}^{2}$ is variance of the components, and $K$ is the number of components, respectively.

The whole process of building the Bayesian network with treatments by the Delphi method is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Framework of building Bayesian network combining the Delphi method.

# 3. Bayesian Network Building 

### 3.1. Determining BN Nodes

In this study, the fire evolution process of subway stations is divided into three stages, based on the case studies of many typical fire accidents in subway stations, and a further evaluation is made on the judgment of experts. Based on the three stages, we propose 28 nodes that have dependency relationships for representing the subway station fires, from causes to consequences. The proposed Bayesian nodes are divided into three types, and their state classifications are described below.

### 3.1.1. Root Nodes

(1) Fire source material (state: Circuit; Luggage; Commodity)

Different to public places on the ground, the types of combustible materials in subway station are relatively specific, which could lead to a variety of consequences. Fires in subway stations are mainly caused by combustible substances carried by passengers or man-made attacks. From the previous statistics, the fire combustibles in subway stations can be divided into three major categories, which include circuit, luggage, and commodity.
(2) Fire alarm system (state: Normal; Malfunction)

This node represents the presence of fire alarm systems. According to the national criteria in China, the fire alarm system must be equipped in subway stations. The state "Normal" refers to that the fire alarm system has been equipped and is in a normal working condition, while the state "Malfunction" means that the fire alarm system might be a substandard product or aging, and might not function in case of fire.
(3) Sprinkler system (state: Normal; Malfunction)

This root node represents the presence of an automatic response sprinkler system in subway stations. The state "Normal" refers to that a standard sprinkler system has been installed, and it can work well in case of fire, while the state "Malfunction" means the sprinkler system is a substandard product, aging, or faces accidental blockages that could be useless in case of fire.
(4) Extinguisher (state: Normal; Malfunction)

This root node presents the performance of extinguishers in subway stations. The state "Normal" indicates that extinguishers are in a normal working state, while the state "Malfunction" means they might be substandard, out-of-date, used before, and may not work in case of fire.
(5) Fire time (state: Peak period; Other time)

Different subway stations generally have different passenger flow densities at distinct time periods. In this study, we just classify the time into two periods: "Peak period", i.e., at the rush hours to or off work, and "Other time" when there are not many passengers.
(6) Fire source position (state: Inside train; On platform)

According to previous statistical data, the main fire locations are in the train and on the station platform, and quite a few of the fire source positions are in the subway tunnel [42]. Herein, we do not pay more attention to the subway tunnel and other locations, and simply classify fire source positions according to two states: Inside train and On platform, and the probabilities are distributed to this node according to the statistical results.
(7) Subway station type (state: Single floor; Double floor; Complex)

The vertical structure of subway stations is divided into three levels, according to the actual practice in Chinese subway stations. The subway station of single layer is only one floor underground. The underground part of the double floor subway station consists of two floors. For example, the station hall is located on the first underground floor, while the platform, the trains, and the tunnel are located on the second underground floor. Another kind of vertical subway structure is called complex, whose vertical structure is more complex, which is more common in interchange stations [43].
(8) Platform type (state: Island type platform; Side type platform; Combined type platform)

There are generally three types of subway station platforms: island type, where the platform is designed between two tracks; side type, where the platforms are located on two sides of the track; combined type, that integrated the island type and the side type. Each kind of platform type has its advantages. The subway station area and changes of the passenger flow are different for these three platform types, which have a great influence on economic loss and casualties in case of subway station fire [44].
(9) Fire brigade location (state: Within 3 min distance; Over 3 min distance)

This root node is set up to examine the significance of firefighters for firefighting and rescue. The distance from the subway station to the fire brigade has a significant impact on the rescue effectiveness organized by firefighters. Previous studies show that the best escape time is 300 s during fire development in an underground subway station. According to experts' experience, the proper duration for firefighters' arrival is three minutes. Therefore, the states of this node are set as "Within three minutes" and "Over three minutes". The former represents that the firefighters could arrive at the subway station within three minutes, and the latter one represents that the firefighters take more than three minutes to reach the subway station.
(10) Smoke extraction system (state: Normal; Malfunction)

Smoke is a critical factor affecting casualties in case of fire. A subway station can be regarded as a closed or semi-closed underground space, so the ventilation system is crucial for the diffusion of fire smoke. The states of this node are set as "Normal" and "Malfunction", to represent if the smoke extraction system could work well.

# 3.1.2. Intermediate Nodes 

(11) Fire detection by human (state: Yes; No)

Whether the fire can be detected by field staff or passengers in time has great impact on the probability of successful evacuation and dialing the fire alarm phone, which will significantly influence the casualties. The states of this node are set to "Yes" and "No". "Yes" means that field person could detect the fire in time, and vice versa.
(12) Safe evacuation (state: Yes; No)

As we know, evacuation will directly affect the number of casualties. Since underground subway stations are relatively closed spaces, safe evacuation is more difficult than other places. In the early stage of fire development and expansion, hot and hazardous smoke flow is the primary influencing factor to escape routes and trappers' safe evacuation.
(13) Fire call (state: Yes; No)

When a fire occurs, if field staff or passengers do not discover it at the initial stage of the fire, the fire call will be delayed, which may cause more serious fire loss.
(14) Firefighters' arrival time (state: Before flashover; After flashover)

Firefighters play a major role in personnel rescue, fire control, and fire extinguishment. Therefore, it is important to discuss firefighters' arrival time, and the states of this node are divided into "Before flashover" and "After flashover". Flashover is a critical stage in fire evolution.
(15) Fire alarm system response (state: In time; Not in time)

A fire alarm system is a crucial factor in the detection of fire, and the response time is associated with the time when people detect the fire. The states of this node are classified into "In time" and "Not in time". To specifically reflect the response of a fire alarm system, "In time" represents that the fire alarm system responds within 30 s after it detects a fire (China, GB50166-2007).
(16) Initial stage of fire (Stage 1) (state: Smolder; Fire)

In the initial stage of fire, also called Stage 1 of fire development, there are two different combustion modes: smolder and fire. If smolder occurs in the initial stage, it is very hard for the alarm system to detect the fire, and the sprinkler system to conduct a prompt response.
(17) Sprinkler system response (Stage 1) (state: In time; Not in time)

Sprinkler systems can effectively control the spread of fire. If the sprinkler system responds in time, especial in Stage 1 of fire development, there may be a higher probability that the fire can be put out or well controlled. The states of this node can be set to "In time" and "Not in time", whereby "In time" means that the sprinkler system responds within 30 s in the initial stage of fire development.
(18) Put out early (Stage 1) (state: Yes; No)

This node is set to reflect extinguishment effectiveness during the fire development. At the initial stage of fire, i.e., Stage 1 of fire development, it is possible to put out the fire by the field people.
(19) Growth stage of fire (Stage 2) (state: None; Slow development; Flashover)

If the fire is not put out in Stage 1, it will develop further to flashover or slow development, which is called Stage 2 of fire development in this study. If the fire is put out in stage 1, it will not develop into Stage 2.
(20) Sprinkler system response (Stage 2) (state: In time; Not in time)

According to the response effectiveness of automatic fire extinguishing system in Stage 2, this node was divided into two states: "In time" and "Not in time". Different from the sprinkler system response in Stage 1, it is more difficult to extinguish the fire in Stage 2, but it is likely to mitigate the spread of fire.
(21) Put out late (Stage 2) (state: Yes; No)

Depending on fire development situation in Stage 2, and the working effectiveness of automatic fire extinguishing systems and firefighters, the fire in Stage 2 could be extinguished, or not be extinguished.
(22) Fully developed to quenched (Stage 3) (state: Yes; No)

This node is to represent the final stage of a fire, i.e., Stage 3: the fully-developed fire to quenched (going out) at last. If the fire develops to this stage, it indicates that the fire is not effectively controlled.
(23) Severity of fire development (state: Slight; Moderate; Serious)

The burning proportions of main fire body parts are generally divided into local burning ( $<30 \%$ ), major burning ( $30-70 \%$ ) and total burning ( $\geq 70 \%$ ). According to this, the node is classified into three states to represent the severity of fire: Slight, Moderate, and Serious.
(24) Smoke extraction system response (state: In time; Not in time)

The response of the smoke extraction system determines whether the smoke generated by fires can be discharged in time, which is of great significance for the safe evacuation of trapped people in the subway station.
(25) Concentration of hazardous gas (state: Less than critical value; More than critical value)

The concentration of hazardous gases, such as $\mathrm{CO}, \mathrm{HCl}, \mathrm{H}_{2} \mathrm{~S}$, and others, will increase faster in fire, and the toxic and harmful gases in the fire are often the main cause of casualties. Hence, the states of this node were divided into "Less than critical value" and "More than critical value". The accumulated critical values for 5 min causing death of $\mathrm{CO}, \mathrm{HCl}$, and $\mathrm{H}_{2} \mathrm{~S}$, are $5000 \mathrm{ppm}, 3000 \mathrm{ppm}$, and 800 ppm , respectively.
(26) Temperature (state: Less than $100^{\circ} \mathrm{C}$; More than $100^{\circ} \mathrm{C}$ )

According to the statistics of related medical and physiological experiments, high temperature smoke in fires will cause a certain degree of harm to the human body. To judge whether the smoke temperature is dangerous or not, the smoke temperature nearby human eyes is usually used as the critical temperature. Herein, this node is divided into "Less than $100^{\circ} \mathrm{C}$ " and "More than $100^{\circ} \mathrm{C}$ ".

# 3.1.3. Leaf Nodes 

(27) Economic loss (state: Less than 50 million; 50 to 100 million; More than 100 million)

Economic loss is a quantitative assessment of consequences in metro station fire accidents. In this study, it is classified into three states: "Less than 50 million", "50 to 100 million", and "More than 100 million" [42].
(28) Casualties (state: Less than 3 persons; 3 to 10 persons; More than 10 persons)

Casualties are the most commonly used evaluation index of consequence severity in subway station fires. In this study, this node is classified into three states: "Less than 3 persons", that the accident resulted in deaths of less than 3 people or serious injuries of less than 10 people; " 3 to 10 persons", that the accident resulted in deaths of more than 3 to 10 persons or serious injuries of less than 10 to 50 persons; and "More than 10 persons", that the accident resulted in more than 30 deaths or more than 100 serious injuries [45].

All the BN nodes and their classifications are listed in Table 1. Based on the case analysis of typical subway station fire disasters and further expert evaluation to determine the dependencies between each node, the structure of Bayesian network for representing subway station fire evolution is established as shown in Figure 3.

Table 1. Classified states of BN nodes.


![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network of subway station fire evolution.

# 3.2. Determining Conditional Probability Tables 

To analyze the evolution of subway station fire, we need to get the dependency intensity between some nodes in BN. The dependency intensity is reflected by a conditional probability table (CPT). The conditional probabilities of each node with the joint distribution of its parent nodes are recorded in CPT. Conditional probabilities can be obtained by parameter learning or expert scoring. However, in the case of subway fires, there is little historical data for reference, so it is difficult to determine the CPTs by parameter learning.

In the Bayesian network of this paper, unconditional probabilities (priori probabilities) of the root nodes (nodes without parent) are mainly determined based on statistical fire data. For other nodes, we invite five experts with rich experience in underground subway station fire to fill out CPT questionnaires of the proposed BN. The CPT of each node is obtained according to expert experience, with consistent processing using the Delphi method. For determining the CPTs of Bayesian nodes, we developed software for applying the Delphi method for expert data processing and analysis (Delphi_data analysis V1.0.0) by MATLAB. This software can read the questionnaire and verify the consistency of the expert data, such as data table import, Cronbach's coefficient alpha calculation, data table output, and taking the mean value of reliable data, finally outputs CPT.

Herein, take determining the CPT of "Temperature" node as an example. The results of the scores of five experts are listed in Table 2. In the "Expert opinion" column, the probability values corresponding to E1-E5 are the results of five experts' rating of "Temperature" node. When the "Severity of fire development " state is "Slight" and "Smoke extraction system response" is "In time", the probability of the expert E1 in the "TL" column ("TL" means "Temperature" is "less than $100^{\circ} \mathrm{C}$ " and "TM" means "Temperature" is "more than $100^{\circ} \mathrm{C}$ ") is 0.74 , which represents that expert E1 thinks that if the severity of fire development is slight, and the smoke extraction system response is in time, the probability of fire temperatures less than $100^{\circ} \mathrm{C}$ is 0.74 .

Table 2. Experts' conditional probability table (CPT) score of "Temperature".


After two rounds of checking with experts through the Delphi method, the final opinion of five experts can be obtained. Then, Cronbach's coefficient alpha is used to verify the consistency of the data collected from the five experts, and the calculated alpha is 0.968 based on Equation (4), which signifies that the data has been reliable. Finally, the average results of the five experts are listed in column E. In this paper, the probabilities of column $m$ are the priori probabilities that are input to each node of the Bayesian network.

Through this method, the initial BN with CPTs can be obtained as Figure 4 shows and, next, the proposed Bayesian network can be used to analyze the evolution of subway station fires. In this study, the probabilistic inference was performed using Netica (Netica 4.16, Norsys Software Corp., Vancouver, BC, Canada), which has been widely used to deal with belief networks and influence diagrams in BN analysis, such as predicting the probabilistic evaluation of pipelines and flood [46-48].

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Initial BN with CPTs.

# 4. Results and Discussion 

### 4.1. Sensitivity Analysis

Sensitivity analysis refers to an uncertainty analysis technology which finds sensitive factors that have an important impact on the subject from several influential factors, and further discusses the influence of related factors changing on a certain or set of key indicators from quantitative analysis. To make the calculated results more reliable when using the proposed Bayesian network, it is necessary to identify the nodes that have a greater impact on object nodes.

In this study, we use the sensitivity analysis function of Netica software to determine the nodes which have a greater impact on "Casualties" and "Economic loss". In Netica, click the Node "Casualties" and select "Network $\rightarrow$ Sensitivity to findings", and then a detailed report will be generated in the "Message" window. The sensitivity analysis results of "Casualties" and "Economic loss" to other nodes are listed in Tables 3 and 4.

Table 3. Sensitivity analysis of "Casualties".


Table 4. Sensitivity analysis of "Economic loss".


From the data in Table 3, it can be seen that the node "Casualties" is mainly affected by "Safe evacuation" and "Concentration of hazardous gas", which conforms to an actual situation, since according to statistics, toxic and harmful gases are the main cause of casualties in the fire [49]. According to the data in Table 4, the node "Economic loss" is mainly impacted by "Severity of fire development". This is also consistent with reality. The greater the fire severity and damage to the equipment, the larger the fire-impacted area and economic loss will be.

According to the results of sensitivity analysis, as "Safe evacuation" has the greatest impact on "Casualties", and the nodes that affect "Safe evacuation" are "Fire time", "Subway station type", and "Platform type", then, the influence of "Fire time", "Subway station type", and "Platform type" on "Safe evacuation" should be primarily taken into account in the assessment of casualties. In the assessment of economic losses, the main considerations should be the effects of "Fire alarm system", "Sprinkler system", and "Extinguisher", on "Severity of fire development" by transmission of "Fire severity".

### 4.2. Impact of Fire Time, Subway Station Type, and Platform Type

According to the experience of experts, fire time has a significant impact on the number of casualties. In this part, we select two typical fire times to be executed in the Bayesian network, namely, "Peak period" and "Other time". In order to mainly discuss the impact of fire time on casualties, the parent nodes "Subway station type", "Platform type", and "Fire brigade location" are given as listed in Table 5.

In the proposed BN model, the estimated probability of casualty is shown in Figure 5. When "Fire time" transfers from "Other time" to "Peak period", the probability that the "Casualties" is in the state "More than 3 persons" increases from 0.602 to 0.692 , and when the fire happens at "Peak period", the probability of "More than 10 persons" of "Casualties" goes up to 0.37. The results show that the fire protection management should be strengthened during the peak period of subway operation.

Table 5. Initial setup of some BN nodes for assessment of "Fire time".


![img-4.jpeg](img-4.jpeg)

Figure 5. Inference results of "Casualties" on the condition of different fire times.
Obviously, the type of subway station impact also has great impact on fire consequences. Herein, the state combinations of some BN nodes are given as follows: (a) the states of "Fire time", "Platform type", and "Fire brigade location" are set to be "Peak period", "Island type platform", and "Within 3 min' distance" respectively; (b) the parent node "Subway station type" is set to three states, as shown in Table 6. The inference results for these scenarios are illustrated in Figure 6. It shows that the degree of casualties of "Double floor" or "Complex" is higher than that of "Single floor". This may be because "Double floor" and "Complex" are much farther away from the ground compared with a single floor type subway station, and their structures are more complicated; on the other hand, fire smoke accumulates more easily inside the subway station, which brings about great difficulty for the crowd evacuation, escape, and rescue.

Table 6. Given state evidences of some BN nodes for assessment of "Subway station type".


![img-5.jpeg](img-5.jpeg)

Figure 6. Inference results of "Casualties" on condition of different subway station type.
According to the experience of experts, the platform type also has an impact on the number of casualties. In this section, we select three main types of platform to be implemented in the Bayesian network: "Island type", "Side type", and "Combined type". The states combination of BN nodes for this analysis are given in Table 7. From the results shown in Figure 7, it is found that the degree of casualties of the island type platform, or combined type platform, is higher than that of the side type platform. This is perhaps because two trains share one platform in island type platforms, which results in a situation where the crowd is likely increasing, while the available escape exits greatly decreases. It is extremely easy for a stampede to occur during evacuation of the crowds.

Table 7. Given state evidences of some BN nodes for assessment of "Platform type".


![img-6.jpeg](img-6.jpeg)

Figure 7. Inference results of "Casualties" on condition of different platform type.

# 4.3. Impact of Fire Source Position 

Take fire source materials from passengers' luggage as an example, meanwhile, the sprinkler system and fire extinguisher are both in "Normal" condition, and we analyze the influence of fire source position on fire severity and economic loss. The inference results are listed in Table 8.

Table 8. Estimated probabilities for assessment of fire source position.


The results show that, if fire position is on a platform, the possibility that the fire severity is slight is 0.625 ; the sum possibility of the fire turning into moderate and serious is 0.375 . If the fire source position is inside the train, the sum possibility of the fire becoming moderate and serious increases to 0.477. In the meantime, the degree of economic loss located on the platform correspondingly increases compared with that of inside train. It is observed that the possibility of "Growth stage of fire (Stage 2)" is "Flashover", and that fire occurs on the platform, is 0.12 . However, the "Flashover" possibility, when fire is located inside the train, goes up to 0.408 . We can find that the change of "Growth stage of fire (Stage 2)" state leads to greater fire severity and economic loss.

### 4.4. Impact of Fire Prevention and Extinguishing Facilities

According to previous statistical results, the possibility of fire source position inside the train is 0.77 , of which, $50 \%$ of incidents are caused by electrical circuit faults. When "Fire source position" is selected as "Inside train" and "Fire source material" is "Circuit fault" and, meanwhile, fire prevention and control response changes from effective (i.e., the automatic fire extinguishing system, alarm system, and fire extinguisher are in a "Normal" condition) to poor (i.e., the automatic fire extinguishing system, alarm system, and fire extinguisher are all in an "Abnormal condition"), the estimated probability of fire "Economic loss" to be "More than 100 million" turns from 0.283 to 0.439 as shown in Figures 8 and 9. Thus, ensuring the automatic alarm system and sprinkler system in normal working conditions and keeping the effectiveness of fire extinguishers are extremely important for the control of subway station fire.

![img-7.jpeg](img-7.jpeg)

**Figure 8.** Inference results with poor fire control response.

![img-8.jpeg](img-8.jpeg)

Figure 9. Inference results with effective fire control response.

# 5. Conclusions 

In order to comprehensively represent and assess the fire risk in subway stations, this study proposes an integrated risk assessment framework for rapid and dynamic modeling subway station fire combined Bayesian network and the Delphi method. The proposed BN-based framework can represent both static and dynamic information on fire causes, fire proof/intervention, emergency rescue, and fire consequences. The main conclusions are
(a) Subway station type and platform type significantly affect fire evolution process and final casualties. Particularly, complex subway stations (more common in interchange station) and combined type platform have the greatest impact on fire severity because of the complex structure and large passenger flow.
(b) Fire in peak periods will likely result in serious casualties than the other fire times, which indicates that the operation management of subway station in peak periods should be strictly instructed.
(c) Fire source position has a greater influence on fire development and consequences. If the fire location is in the train, the probability of flashover would still reach 0.386 , even though the working condition of alarm system, sprinkler system, and fire extinguisher are all "Normal". In this case, the fire will likely result in a serious economic loss and casualties.
(d) It is quantitatively demonstrated that the normal working condition of the alarm system, sprinkler system, and fire extinguisher play an important role in the fire control of in subway station.
(e) The proposed dynamic and integrated BN framework is demonstrated to be of great significance to the prevention, evaluation, and control of subway station fire and, thus, helpful to perform "Scenario Response"-based fire disaster response and reduction, which can be used as a reference for risk assessment and emergency response of other disasters or accidents.

At present, due to the scarcity of detailed records of subway station fire cases (especially specific fire evolution processes and fire consequences), it is difficult to comprehensively validate the proposed BN model against past fire incidents. However, the applicability of this proposed Bayesian framework to real life situation could be improved and optimized with many emerging underground subway station fire cases in the future. Although the present version of the proposed Bayesian framework may not provide very accurate results, it could present comparatively quantitative risk distribution for reference, that could benefit the emergency response to an underground subway station fire. In addition, a resilience assessment can be achieved dynamically in the pre-event, during-event, and post-event phases of subway station fire with BN-based model. In this study, "resilience" was mainly to represent and incorporate fire prevention/intervention to minimize damage and functional interruption during an event. Resilience strength can resist extreme events in the pre-event phase, minimize the damage and function interruption during the event, and can facilitate recovery in the post-event phases. "Resilience assessment" to subway station fire could be extended more specifically in the pre-and post-event phase of subway station fires in future work.

Author Contributions: For research articles with several authors, a short paragraph specifying their individual contributions must be provided. The following statements should be used "conceptualization, J.W. and Z.H.; methodology, J.W.; software, Z.H.; formal analysis, J.W.; investigation, Z.H. and J.C.; data curation, Z.L.; writing-original draft preparation, J.W., Z.H., J.C. and Z.L.; writing-review and editing, J.W.; supervision, J.W.; funding acquisition, J.W."
Funding: This work was supported by the National Natural Science Foundation of China (Grant No. 11502283), National Key Research and Development Program of China (Grant No. 2017YFC0805001) and the Yue Qi Scholar/Young Scholar Program of China University of Mining \& Technology, Beijing.
Acknowledgments: Great gratitude is extended to the experts for their opinion on the BN building.
Conflicts of Interest: The authors declare no conflict of interest.
