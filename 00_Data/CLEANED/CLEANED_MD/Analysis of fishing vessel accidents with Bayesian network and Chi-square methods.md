# LJMU Research Online 

## Ugurlu, F, Yildiz, S, Boran, M, Ugurlu, O and Wang, J

## Analysis of fishing vessel accidents with Bayesian network and Chi-square methods

## http://researchonline.ljmu.ac.uk/id/eprint/12787/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Ugurlu, F, Yildiz, S, Boran, M, Ugurlu, O and Wang, J (2020) Analysis of fishing vessel accidents with Bayesian network and Chi-square methods. Ocean Engineering, 198. ISSN 0029-8018

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Analysis of Fishing Vessel Accidents with Bayesian Network and Chi-Square Methods 

Funda UĞURLU ${ }^{\mathrm{a}}$, Serdar YILDIZ ${ }^{\mathrm{b}}$, Muhammet BORAN ${ }^{\mathrm{c}}$, Özkan UĞURLU ${ }^{\mathrm{d}}$ and Jin WANG ${ }^{\mathrm{e}}$<br>${ }^{a}$ Republic of Turkey Ministry of Food Agriculture and Livestock, Department of fisheries and aquaculture, Trabzon, Turkey, funda.ugurlu@tarim.gov.tr<br>${ }^{\text {b }}$ Maritime Transportation and Management Engineering Department, Karadeniz Technical University, Trabzon, Turkey, serdaryildiz@ktu.edu.tr<br>${ }^{c}$ Maritime Transportation and Management Engineering Department, Karadeniz Technical University, Trabzon, Turkey, mboran@ktu.edu.tr<br>${ }^{\text {d }}$ Maritime Transportation and Management Engineering Department, Karadeniz Technical University, Trabzon, Turkey, ozkanugurlu24@hotmail.com, ougurlu@ktu.edu.tr, +905058414026 (Corresponding author)<br>${ }^{e}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Faculty of Engineering and Technology, Liverpool John Moores University, Liverpool, UK, J.Wang@ljmu.ac.uk


#### Abstract

Commercial fishing is an important industry that generates income directly or indirectly to many people in the world. It is impossible to carry out a fishing activity on this scale without a vessel. Therefore, fishing vessels are the most important element of the modern fishing industry. Fishing vessels play a key role in fishing, transporting and storing fish. Thousands of people die every year as a result of fishing vessel accidents. In order to carry out sustainable fishing operations, fishing vessel accidents should be investigated and measures should be taken to prevent them. Therefore, in this study for analysing accidents that occurred between 2008 and 2018 in fishing vessels with full lengths of 7 meters and above, a Bayesian network and chisquare methods were used. An Accident (Bayes) Network, which summarizes the occurrence of accidents on fishing vessels, is presented. These networks allow to understand the occurrence of accidents in fishing vessels and to estimate the occurrence of accidents in various conditions. It was also found that there was a significant relationship between the accident category and vessel length, vessel age, loss of life and loss of vessel. Based on the obtained results, recommendations were made to prevent possible fishing vessel accidents.


Key Words: Fishing Vessel; Marine Accident; Accident Analysis; Bayesian Network; Maritime Safety.

# 1. Introduction 

Maritime activity, especially fishing is one of the most dangerous occupational groups with high mortality (Jaremin and Kotulak, 2004; Jin and Thunberg, 2005; FAO, 2014). On average, 24,000 fishermen died each year in this profession as a result of accidents (FAO, 2000; Petursdottir et al., 2001; Jensen et al., 2014). The rate of fatal accidents in the fishing sector is 115 times higher than other fatal accidents in the UK and 25 times higher than the Australian and US national averages (Håvold, 2010). One of the most important reasons why the profession carries such a high risk is the difficulties in the implementation of compulsory safety measures applied on merchant vessels (Wang et al., 2005; Piniella and Fernández-Engo, 2009).

When the fishing vessel accidents are examined, it is seen that most of the accidents occurred during the fishing activities (Havold 2009). Many researchers emphasize that human error is one of the main reasons of accidents in the fishing industry (Rothblum, 2000; Uberti, 2001; Ozguc, 2019; Wang et al., 2005). Marine accidents are the sequence of events that occur as a result of chain reactions. Causal factors (latent failures) give rise to root causes (active failures) and the accident becomes inevitable if root causes have appropriate operational conditions (enviromental factors) (Uğurlu, 2015; Uğurlu et al., 2018). Environmental factors have a role as complementary factors in the transformation of human error into accidents (Uğurlu and Yıldız, 2016). In many studies, adverse weather conditions, operational status of the vessel, neglected or unsuitable fishing vessel structure were indicated as the main causes of fishing vessel accidents other than human error (Jaremin and Kotulak, 2004; Roberts, 2004; Wang et al., 2005; Laursen et al., 2008). In addition, vessel location, seasons and unsuitable fishing equipment also trigger accidents on fishing vessels (Jin et al., 2002; Davis et al., 2019; Pitman et al., 2019).

Many researchers have studied fishing vessel accidents and their causes. Jin and Thunberg (2005) emphasized that the probabilities of accidents in the fishing vessels increase with wind speed. In addition, they have shown that accidents are more likely to occur in coastal waters and accidents are higher in winter conditions. Wang et al., (2005) found that the risk of accidents on fishing vessels increases as vessel length decreases. Jin (2014) exposed that the severity of vessel damage in fishing vessels was inversely proportional to the length of the vessel, and that the severity of the crew's injury was directly proportional to the loss of stability and sinking of the vessel. In addition to these studies, there are many investigations related to the analysis of occupational accidents in fishing vessels (Reilly, 1985; Törner et al., 1995; Roberts, 2004; Chauvin and Le Bouar, 2007; Laursen et al., 2008), analysis of accidents occurring in a certain period of time (Branch et al., 2002, 2008), and analysis of fishing vessel accidents occurring in

territorial waters of a particular region or country (Perez-Labajos et al., 2006; Roberts et al., 2010).

The share of fishing vessels in world maritime trade is approximately 40 times the share of commercial vessels, and accidents in fishing vessels are more frequent than other types of vessels (FAO, 2000; Petursdottir et al., 2001; Jensen et al., 2014). Today's technology and its' innovative applications have changed the way vessel accidents occur (Suuronen et al., 2012; Uğurlu et al., 2018). Fishing vessel accidents were also affected by this change (transfiguration). In order to ensure sustainable maritime safety in maritime transport, it is necessary to analyze the current accidents occurring in fishing vessels, to review the existing measures and to reveal the needed innovative measures. Therefore in this study, current accidents on fishing vessels were analyzed using a Bayesian network approach and Chi-square methods. In this study, the accident (Bayes) networks which make it possible to evaluate the occurrence of fishing vessel accidents are presented in terms of the causal factors, root causes and operational conditions that play an important role in the formation of fishing vessel accidents. Considering this network structure, all parties of the maritime trade (ship operators, accident investigators, accident researcher, etc.) can predict the risk of accident according to variable conditions in fishing vessels. The Chi-square independence test was used to check the presence-absence of the relationship between the vessel type, vessel length, vessel age, accident site, daylight, loss of vessel and loss of life. Such parameters are thought to be related to the type of accident. As a result, the relationship between them was revealed statistically.

# 2. Bayesian Networks 

The Bayesian approach is a widely accepted conditional probability approach which is used in many studies. It is used in many sectors for modelling and interpreting sequences of events with uncertainty (Demirel and Bodur, 2004; Howson and Urbach, 2006; Yang et al., 2008). In the Bayesian approach, a Directed Acyclic Graph model (DAG) is created by using nodes and edges in order to understand the formation pattern (Loughney and Wang, 2017). In the generated model, by means of directional arrows (edges), the statistical relationship between the variables is reflected in the network model as in real events. In other words, nodes in a network model represent variables with a finite set of states; edges express the relationship between nodes (states). In Bayesian network models, reasoning is also possible when constructing the causal relationship between nodes. Therefore, the creation of the Bayesian network represents a qualitative approach (Trucco et al., 2008; Loughney and Wang, 2017). In the established network, the part consisting of the Conditional Probability Table (CPT)

connected to each node and covering the determination of numerical values represents the quantitative approach (John et al., 2016; Li et al., 2014).

In order to understand Bayesian networks, first of all, conditional probability logic must be understood. The concept of conditional probability means that additional information related to that event should be used in the calculation of the probability of occurrence of an event and explains how it will be used. For example, let A and B be two events connected to each other by conditional probability, and let B be seen when A is seen. In this case when event A is observed, the probability of event B can be expressed as: $P(B \mid A)=p$. Based on this information, when event B is seen, the probability of occurrence of event A can be expressed as follows (Trucco et al., 2008; Kragt, 2009; Akhtar and Utne, 2014):
$P(A \mid B)=P(A \cap B) / P(B), P(B)>0$
$\mathrm{P}(\mathrm{A} \cap \mathrm{B})=\mathrm{P}(\mathrm{A} \mid \mathrm{B}) \cdot \mathrm{P}(\mathrm{B})=\mathrm{P}(\mathrm{B} \mid \mathrm{A}) \cdot \mathrm{P}(\mathrm{A})$
where $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=$ conditional probability of event A when event B occurs, $\mathrm{P}(\mathrm{A} \cap \mathrm{B})=$ intersection of probabilities where A and B are seen together, and $\mathrm{P}(\mathrm{B})=$ probability of event B independent from event A (initial probability of event B )

For the mathematical expression of Bayes theorem, given the concept of conditional probability (Equations 1 and 2), we assume that there are k number of A events that intersect with event B; Probability of event $\mathrm{A}_{\mathrm{i}}$ given event B is known:

$$
\begin{gathered}
\mathrm{P}\left(\mathrm{~A}_{\mathrm{i}} \mid \mathrm{B}\right)=\frac{\mathrm{P}\left(\mathrm{~A}_{\mathrm{i}}\right) \mathrm{P}\left(\mathrm{~B} \mid \mathrm{A}_{\mathrm{i}}\right)}{\mathrm{P}(\mathrm{~B})}, \mathrm{i}=1,2,3,4, \ldots, \mathrm{k} \\
\mathrm{P}(\mathrm{~B})=\mathrm{P}\left(\mathrm{~A}_{1}\right) \mathrm{P}\left(\mathrm{~B} \mid \mathrm{A}_{1}\right)+\mathrm{P}\left(\mathrm{~A}_{2}\right) \mathrm{P}\left(\mathrm{~B} \mid \mathrm{A}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{~A}_{\mathrm{k}}\right) \mathrm{P}\left(\mathrm{~B} \mid \mathrm{A}_{\mathrm{k}}\right)=\sum_{\mathrm{j}=1}^{\mathrm{k}} \mathrm{P}\left(\mathrm{~A}_{\mathrm{j}}\right) \cdot \mathrm{P}\left(\mathrm{~B} \mid \mathrm{A}_{\mathrm{j}}\right)
\end{gathered}
$$

where $P\left(A_{i} \mid B\right)=$ the hypothesis' posterior probability ( $A_{i}$ is likely to be seen in a specific "B" state); $P\left(A_{i}\right)=$ the predetermined probability of the hypothesis (independent of B), i.e. the probability that event A is in a certain " i " state; $P\left(B \mid A_{i}\right)=$ conditional probability of B when a certain $A_{i}$ condition is observed; and $P(B)=$ the probability (initial probability) of B when it is independent from $A_{i}$.

# 3. Chi-Square Test and SPSS 

The Chi-square test is based on whether the difference between observed frequencies (O) and expected frequencies (E) is statistically significant. The Chi-square test uses qualitative data (Lewis and Burke, 1949; Güngör and Bulut, 2008; McHugh, 2013). In determining the statistical test to be used in the Chi-square approach, the characteristics of the data set and the requirements are taken into consideration. There are three types of Chi-square tests commonly

used in the literature: good fit test, homogeneity test and independence test. A good fit test is used to test the suitability of the sample to a particular data set or distribution (Binomial, Poisson, Discrete, Normal) (Ergöl and Kürtüncü, 2014; Köksal and Türedi, 2014). The homogeneity test is used to measure whether a sample of a selected volume of sample selected from the population varies in similar characteristics to the population. The Chi-square independence test is used to determine whether there is a statistically significant relationship between the two variables (Bircan et al., 2003; Sirkin, 2006). In this study, it is decided to use the Chi-square independence test as a study is conducted to examine the relationship between variables. One of the major advantages of the Chi-square independence test is that it can be applied to nominal data as well as numerical data (Burns and Dobson, 1981; Sirkin, 2006). The general hypotheses of the Chi-square independence test are presented below (Burns and Dobson, 1981; McHugh, 2013).

- $\mathrm{H}_{0}$ : There is no significant relationship between the two variables compared (these variables are independent).
- $\mathrm{H}_{1}$ : There is a significant relationship between the two variables compared (these variables are dependent).


# 4. Method 

In this study, accidents that occurred in motor fishing vessels with full lengths of 7 meters and over were investigated. Accident data was collected for a period between 2009 and 2018. The data consists of fishing vessel accidents in the very serious and serious accident categories that have occurred and reported worldwide. In this study, more than 6,000 accidents were obtained from sources including GISIS (Global Integrated Shipping Information System), MAIB (Marine Accident Investigation Branch), EMSA (European Maritime Safety Agency), ATSB (Australian Transport Safety Bureau), and TSB (Transportation Safety Board of Canada) databases. There are 226 fishing vessel accidents that meet the criteria of the study. The study consists of 3 steps.

In the first step of the study, accident data on fishing vessels was collected. An accident database based on Microsoft Excel was created by evaluating such accident data. This database contains detailed information about the content of accidents. Thus, it became possible to analyse accidents more systematically and easily.

After the database was prepared, the most appropriate accident analysis model was determined in the second stage of the study. In this study, it was decided to use the Bayesian network method which is frequently used in the literature in the context of accident analysis

(Akhtar and Utne, 2014; Lehikoinen et al., 2015; Zhou et al., 2018) and safety assessment (Brooker, 2011; Khakzad et al., 2011; Li et al., 2014; Pristrom et al., 2016). The Bayesian network is a logic network diagram that enables both qualitative and quantitative analysis. In this study, Bayesian Network (BN) was used to model and analyse the sequence of events that cause fishing vessel accidents according to conditional probabilities. This feature distinguishes the BN model from many models and methods used in the literature. In this study, the Bayesian network model was built for the most common types of accidents, such as sinking and collision in fishing vessels. At this stage of the study, BN models that summarize the occurrence of accidents were established by evaluating the root causes of accidents, causal factors, environmental factors and the formation of accidents. Hugin Software was used to analyse accident data (Hugin, 2018). The conditional probability tables in the study were formed based on the accident data (Tables A1 and A2). Axiom tests were performed to provide the validation of the network structure established. After the axiom tests were successfully completed, sensitivity analysis was applied to the network structure established to determine the effect of changes in the root nodes, child nodes and parent nodes on accident occurrences. Finally, the effect of active failures (root causes), latent failures (causal factors) and environmental factors (operational conditions) that cause fishing vessel accidents according to each accident category were determined. The network structures presented in this study make it possible to understand and analyse the occurrence of accidents in fishing vessels and to estimate the risk of accident occurrence in various conditions.

In the third stage, the data presented in the first stage of the study was analysed statistically. For this purpose, the relationship between the accident type and vessel type, length of vessel, age of vessel, place of accident, daylight, loss of vessel and loss of life was investigated. Chi-square test of independence was used to examine the relationship. As a result of the Chi-square test, factors related to the type of accident were identified and recommendations were made to prevent accidents.

# 4.1. Fishing Vessel Accidents 

In this study, accidents that occurred in fishing vessels are discussed in 7 accident categories: collision, grounding, sinking, fire-explosion, occupational accident, man overboard and other. The other category of accidents includes poisoning, gas leaking, etc. Table 1 provides information about the types of accidents occurring in fishing vessels and their contents.

Table 1. Distribution of fishing vessel accidents

# 4.2. Formation of Accident Networks 

Accident networks (Bayes networks) were created to reveal the formation patterns of accidents occurring in fishing vessels. In this study, accident networks were established separately for two most common types of accidents: sinking $(\mathrm{n}=55)$ and collision $(\mathrm{n}=56)$ (Figures 1 and 2). Accident networks include 3 stages: causal factors, root causes and environmental factors.

Figure 1. Bayesian Network structure of sinking accidents

Figure 2. Bayesian Network structure of collision accidents

The last events in the accident networks are accidents themselves (sinking, collision). Accident occurrences in this study are limited to sinking and collision accidents. The first level (yellow colour) in the Bayesian network represents causal factors, Level 2 root causes (green colour), Level 3 environmental factors (blue colour) and the last level represents accident occurrences (red colour).

The relationship between the causes in each accident network has been established by considering the accident reports and the occurrences of accidents. For each accident, an accident network was created which summarized the occurrence of the accident. In this process, edges are drawn to the parent and child nodes where each node in the formation of the accident interacts. After this process was done for each accident, all accident networks were combined to form a general Bayes network (accident network). In this way, the relationship between the causes of accidents is preserved and reflected to the whole network. The probability values and conditional probability tables of the nodes are calculated on the basis of mathematical equations given under the Bayesian networks section (Equations 3 and 4) (Table A1, A2). The test case application for the calculations is given below. The descriptive information about the framework is presented in the following section.

### 4.2.1. Test Case

The "Vessel Pipeline" (corroded / normal) child node in the sinking accident network for the example of the calculation of conditional probability tables was selected. This node has two parent nodes: "Planned Maintenance" (uncompleted/completed) and "Vessel Age" (old/new).

The probability value of the "Vessel Pipeline" node in the accident network shown in Figure 3 varies depending on the two parent nodes. The probability value for the inappropriate condition (uncompleted) of the Planned Maintenance node is calculated as $10 \%$ (6/55). The appropriate condition (completed) is $90 \%$ (100-10). The initial probability value for the "old" condition of the vessel age node is $74 \%$ (41/55) and the probability value for the "new" condition is $26 \%$ (100-74). There are 4 conditions that affect the formation of the "Vessel Pipeline" node, and the conditional probability values for these 4 conditions are presented in Table 2.

Figure 3. "Vessel Pipeline" node and its' parent nodes

Table 2. Probability values for "Vessel Pipeline" node

Depending on these conditions, the probability of the "Vessel Pipeline" node to be corroded is $67 \%$ and its probability of being normal is $33 \%$. According to Equations 3 and 4, the probability of the "Vessel Pipeline" node to be corroded is calculated as follows (VA: Vessel Age, PMS: Planned Maintenance):

P(Vessel Pipeline (Corroded)) $=[(\mathrm{P}($ Vessel Pipeline (Corroded) $\mid$ PMS (Sufficient), VA (New $))$ $\times \mathrm{P}(\mathrm{PMS}($ Sufficient $)) \times \mathrm{P}(\mathrm{VA}(\mathrm{New}))]+[(\mathrm{P}($ Vessel Pipeline (Corroded) | PMS (Sufficient), VA (Old)) $\times$ $\mathrm{P}(\mathrm{PMS}($ Sufficient $)) \times \mathrm{P}(\mathrm{VA}($ Old $))]+[(\mathrm{P}($ Vessel Pipeline (Corroded) | PMS (Insufficient), VA (New)) $\times \mathrm{P}(\mathrm{PMS}$ (Insufficient)) $\times \mathrm{P}(\mathrm{VA}($ New $))]+[(\mathrm{P}($ Vessel Pipeline (Corroded) | PMS (Insufficient), VA (Old)) $\times \mathrm{P}(\mathrm{PMS}$ (Insufficient)) $\times \mathrm{P}(\mathrm{VA}($ Old $))]$

$$
\begin{aligned}
= & {[(0 \times 0.90 \times 0.26)+(0.9 \times 0.9 \times 0.74)+(0.08 \times 0.10 \times 0.26)+} \\
& (0.96 \times 0.1 \times 0.74)] \\
= & 0.6725(67.25 \%)
\end{aligned}
$$

Probability of being normal of the vessel pipeline node:
$\mathrm{P}($ Vessel Pipeline (Normal $))=1-\mathrm{P}($ Vessel Pipeline (Corroded $))$

$$
\begin{aligned}
& =1-0.6725 \\
& =0.3275(32.75 \%)
\end{aligned}
$$

The network structure presented in this study can be used to determine the root causes, causal factors and environmental factors that cause accidents in fishing vessels, as well as to analyse how these factors interact (by conditional probability tables) in the accident (Figure 1, 2). For example, the "Corroded" state of the "Vessel Pipeline" node varies depending on two parent nodes (four conditions) (Figure 3, Table 2): "Vessel Age (old/new)" and "Planned Maintenance (uncompleted / completed)". For example, in Table 2, if the ship is old (over 20 years) and planned maintenance of the ship is incomplete, it was observed that the probability of vessel's pipelines "corroded" is $96 \%$. As in the example presented above, it is possible to analyse the interaction of the factors that caused the accident with the network structure and conditional probability tables presented in this study.

The second advantage of the network presented in the study is that it can predict the risk of accident in variable conditions. In other words, this study allows modelling of fishing vessel accident scenarios and evaluating risks with Bayesian Network. For example, in case of an insufficient number of seafarers (minimum number=100\%) on a fishing boat and restricted visibility (yes=100\%), users can estimate the risk of collision in different types of navigation (coastal water, offshore and port) (Figure 2).

# 4.2.2. Causal factors 

Causal factors form the basis of accident occurrences and offer the ground for the formation of root causes (Reason, 1997; Wiegmann and Shappell, 2001). Under this level in the Bayes network which was created for sinking accidents, vessel age (old/new), planned maintenance (improper/appropriate), loss of water tightness (present/absent), vessel structure (worn/normal), vessel pipeline (corroded/normal), used hunting equipment (improper/appropriate), hunting equipment overload (yes/no), design defect (yes/no), unstable loading (yes/no), overload (yes/no) were examined. Vessels aged 20 years and over are considered to be old vessels. Loss of water tightness means that the deck or hatch covers lose their water tightness. Improper use of hunting equipment refers to non-conformities in terms of width, length or weight in hunting equipment used. In the accident network created for collision accidents, under the causal factors level, manning (minimum number/optimum number), alcohol-drug use (yes/no), occupation with other tasks (yes/no), fatigue (yes/no), lookout (improper/proper), inter-ship communication (no/yes), bridge without a watchkeeper (yes/no) and use of navigation equipment (inadequate/adequate) were examined. Table 3 provides information on the causal factors of sinking accidents and Table 4 provides information on the causal factors of the collision accidents. Root nodes, child nodes, parent nodes, their probability

values, negative expressions and abbreviations are included in the tables. In the tables, nodes without parent node refer to root nodes.

Table 3. Accident network content of causal factors for sinking accidents

Table 4. Accident network content of causal factors for collision accidents

# 4.2.3. Root Causes 

Root courses are also called unsafe actions. It is the visible face of accidents. It is the level in which accident researchers and readers have an interest (Li and Harris, 2006). Most accident reports provide detailed information about the factors under this level. While focusing on root causes allows us to understand what is happening, analysing causal factors and root causes together allows us to understand why and how unsafe actions and accidents occur. Thus, we can take more constructive measures to prevent accidents. In this study, in the accident network created for sinking accidents, water intake (yes/no), loss of buoyancy (yes/no), loss of stability (yes/no), and carrying load above the transport limits (yes/no) were examined under this level (Table 5). In the accident network created for the collision accidents, the intention of other (target) vessel (not understood/understood) and the presence of the target vessel (not detected / perceived) were examined under this level (Table 6).

Table 5. Accident network content of root causes for sinking accidents

Table 6. Accident network content of root causes for collision accidents

### 4.2.4. Environmental Factors

At the last stage of accident occurrences, appropriate environmental factors are necessary for any unsafe action to result in an accident. Environmental factors include weather and sea conditions, type of navigation, day-night, heavy traffic, fog, currents, factors outside the structure of the vessel, which are not under the control of the operators of the vessel, and factors that affect vessel movement and are partially controllable by operators. In this study, environmental factors for sinking accidents are weather and sea conditions (bad/good) (Table 7), and for collision accidents, restricted visibility (yes/no) and the type of navigation (coastal waters/offshore/port) (Table 8).

Table 7. Accident network content of environmental factors for sinking accidents

Table 8. Accident network content of environmental factors for collision accidents

# 4.2.5. Consequence Nodes 

The consequence (resulting) nodes in the developed accident networks represent accident categories. The accident networks have 2 consequence nodes which are sinking and collision. In Table 9, the explanatory information is given about the consequence nodes of sinking and collision accidents.

Table 9. Accident network content of consequence nodes

### 4.2.6. Validity of the Model

The relationship between the nodes in this study, probability values and conditional probability tables are considered reliable because they are based on accident reports and statistical data in the database. However, sensitivity analysis was used in the study to provide confidence that the model was built correctly and worked as intended. If the model shown in Figures 1 and 2 makes sense, it should satisfy the following axioms (Pristrom et al., 2016):

Axiom 1. A slight increase/decrease in the preliminary probabilities of each parent node should certainly result in the relative increase/decrease of the subsequent probabilities of the child node.

Axiom 2. The effect of changes in the probability distributions of each parent node on the child nodes should be consistent.

Axiom 3. The total effect of the combination effects of probability variations should always be greater than their individual effects on the parent nodes.

### 4.2.6.1. Test of Axiom 1

In the study, Axiom 1's requirements were tested for the validity of the accident network which was established for sinking and collision accidents. For this purpose, the effect of changes in the parent nodes on the accident categories was observed for each accident. Table 10 shows the effect of the change in the parent nodes affecting the occurrence of accidents on the occurrence of sinking accidents. The parent nodes that affect the occurrence of sinking accidents are loss of stability, loss of buoyancy, carrying load above the transport limits, weather and sea conditions. For example, if the loss of stability occurs, the probability of

sinking increases from $41.26 \%$ to $64.72 \%$. If there is no loss of stability, the probability of an accident is reduced to $36.96 \%$. Similarly, if the weather and sea conditions are bad, the probability of sinking increases to $76.42 \%$, and if the weather and sea conditions are good, the probability of accident decreases to $23.94 \%$. Table 11 shows similar results for collision accidents. Thus, Tables 9 and 10 show that changing the value of each parent node in the final stage of the accident network affects the probability value of the accident as in reality. Therefore, the accident network established in the study fulfilled the Axiom 1 requirements.

Table 10. Axiom 1 test results for sinking accidents

Table 11. Axiom 1 test results for collision accidents

# 4.2.6.2. Test of Axiom 2 

Figure 4 shows the change in the probability of the "sinking" node with "weather and sea conditions", "loss of buoyancy", "loss of stability" and "carrying load above the transport limits". The shapes of the curves indicate that there are no outliers. If the probabilities of "weather and sea conditions = bad", "loss of buoyancy = yes", "loss of stability = yes" and "carrying load above the transport limits = yes" are changed, the occurrence probability for "sinking= yes" increases consistently. Similar observations were made for the collision node (Figure 5), and both consequence nodes were found to meet the Axiom 2 requirements.

Figure 4. Probability changes of sinking accidents

Figure 5. Probability changes of collision accidents

### 4.2.6.3. Test of Axiom 3

According to Axiom 3, the individual effect of each of the parent nodes on the child node should not have more effect than the collective effect. To explain this with an example, loss of stability (child node) consists of "hunting equipment overload", "design flaw" and "unstable loading" (parent nodes). "Hunting equipment overload = yes", "design flaw = yes" and "unstable loading = yes" are entered independently of each other. The occurrence probability of "sinking = yes" is estimated as $57.37 \%, 27.24 \%$ and $5178 \%$, respectively. When "hunting equipment overload = yes", "design flaw = yes" and "unstable loading = yes" are entered together, the occurrence probability of "sinking = yes" is estimated as $100 \%$. These results are

consistent with Axiom 3. In addition, the same tests were applied for the other levels of the accident network established in the study. All results are consistent with Axiom 3.

# 4.2.7. Sensitivity Analysis 

Accuracy analysis, risk analysis, nonconformity analysis, failure modelling, sensitivity analysis are carried out in order to observe the impact of changes in data on the results. Sensitivity analysis reveals the effect of the measures taken to prevent the negative event on the system; it helps to predict the damage to the system if the negative event is maximum (Jin et al., 2002; Wang et al., 2005; Uğurlu et al., 2015; Uğurlu, 2016). In Bayesian network studies, sensitivity analysis reveals the effect of the change in root nodes, parent nodes or child nodes that the network hosts. In other words, it allows to predict how changes made to the inputs of the system will affect the outputs.

In the Bayesian network, the parameters of the model are conditional probabilities of the model's inputs. The outputs of the Bayesian network created in this study are the probabilities of occurrence of collision and sinking accidents. Their inputs are root causes, environmental factors and causal factors that play a role in the occurrence of these accidents.

In this study, sensitivity analysis was applied separately for all three levels in each accident category. Within the scope of sensitivity analysis, the probability of the node under which sensitivity analysis was applied was made $0 \%$, then $100 \%$ while the other nodes were fixed. Then, the change in accident probability was examined for each accident category (Table 12 and Table 13). The effects of the factors that play a role in the occurrence of accidents are observed in this stage.

Table 12. Sensitivity analysis results of sinking accidents

Table 13. Sensitivity analysis results of collision water accidents

Accidents have a compact structure, so that the factors that cause the accident are evaluated independently and combined, allowing us to understand the occurrence of accidents. For this purpose, in the second stage of the sensitivity analysis, the effect of the sequence of events on the accident occurrences was evaluated. At this stage of the study, the most probable combinations and their effects that may lead to accident formation have been revealed. Figure 6 shows the results of the analysis of the main combinations of events that may cause sinking accidents and Figure 7 shows the combinations of collision accidents.

Figure 6. The most likely combinations that may cause sinking accidents

Figure 7. The most likely combinations that may cause collision accidents

# 4.3. Application of Chi-Square Independence Tests and Test Results 

The validity of 14 hypotheses, including zero hypotheses, which were thought to affect the type of accident, was tested on 226 accident data using IBM SPSS statistics 22.0 software. The findings obtained from the Chi-Square test are presented below in order of hypothesis (Table 14).

Table 14. Chi-square hypotheses established in the study and significance values

According to the Chi-square test results (sig. $=0.051>0.05$ ) between the accident type and vessel type, the $\mathrm{H}_{0}$ hypothesis was accepted and the $\mathrm{H}_{1}$ hypothesis was rejected (Table 14). In this case, there is no significant relationship between the accident type and vessel type. In other words, accident types showed random distribution on vessel types; they are not directly related to each other. The type of accidents occurring does not depend on the type of fishing vessels (Multi-purpose, dredger, trawler, etc.).

According to the Chi-square test results (sig. $=0.001<0.05$ ) between accident type and vessel length, the $\mathrm{H}_{2}$ hypothesis was rejected and the $\mathrm{H}_{3}$ hypothesis was accepted (Table 14). In this case, there is a significant relationship between the type of accident and the length of the vessel. The result of this study revealed that the length of the vessel affects the type of accident. The smaller the length of the vessel, the higher the risk of accidents. In particular, this increase is higher for sinking accidents.

According to the Chi-square test results (sig. $=0.002<0.05$ ) between the type of accident and vessel age, the $\mathrm{H}_{4}$ hypothesis was rejected and the $\mathrm{H}_{5}$ hypothesis was accepted (Table 14). In this case, there is a significant relationship between the type of accident and vessel age. The frequency of sinking accidents is directly proportional to the age of the vessel. The frequency of sinking accidents increases with increasing vessel age. Similarly, collisions, groundings, fire and explosion accidents have been observed to occur on a larger number ( $70-85 \%$ ) on older vessels over 20 years of age. More than half of occupational accidents are also concentrated on older vessels over 20 years of age. When the general situation is examined, the number of accidents observed increases with the vessel age. One of the most important reasons of this

strong relationship (Phi value: 0.374 ) is that equipment of the old vessels offers the ground for each type of accident.

According to the Chi-square test results (sig. $=0.051>0.05$ ) between accident type and accident area, the $\mathrm{H}_{6}$ hypothesis was accepted and the $\mathrm{H}_{7}$ hypothesis was rejected (Table 14). In this case, there is no significant relationship between accident type and accident area. The type of accidents that occur does not depend on the operational area (port, coastal waters, etc.) where the accidents occur. Accidents were randomly distributed in operational areas; they are not directly related to each other.

According to the Chi-square test results (sig. $=0.107>0.05$ ) between accident type and daylight (0800-1959-day shift/2000-0759-night shift), the $\mathrm{H}_{8}$ hypothesis was accepted and the $\mathrm{H}_{9}$ hypothesis was rejected (Table 14). In this case, there is no significant relationship between accident type and accident area. In other words, dark or light weather does not affect the type of accidents (seaports, coastal waters, etc.) at the time of the accident. Day or night accident types were randomly distributed; the are not directly related to each other. However, $60.7 \%$ of collision accidents occurred during the night shift. The main reason for this is that night watching is more difficult than watching in daytime.

According to Chi-square test results (sig. $=0.001<0.05$ ) between the accident type and vessel loss, the $\mathrm{H}_{10}$ hypothesis was rejected and the $\mathrm{H}_{11}$ hypothesis was accepted (Table 14). In this case, there is a significant relationship between the type of accident and vessel loss. $80 \%$ of the sinking accidents experienced vessel loss. In addition, $50 \%$ of the total vessel losses occurred as a result of sinking accidents, in this context sinking accidents are the riskiest fishing vessel accident type in terms of vessel loss. Other types of accidents where vessel loss risk is high are collision ( $20.5 \%$ ), grounding ( $15.9 \%$ ), fire and explosion ( $11.4 \%$ ). When the general situation is examined, $39 \%$ of the accidents in the data set have caused vessel loss. The relationship between accidents and loss of vessels (Phi value: 0.601 ) proves that accidents result in huge asset losses.

According to the Chi-square test results (sig. $=0.001<0.05$ ) between the accident type and loss of life, the $\mathrm{H}_{12}$ hypothesis was rejected and the $\mathrm{H}_{13}$ hypothesis was accepted (Table 14). In this case, there is a significant relationship between the type of accident and loss of life. The riskiest accident in terms of loss of life is man over board. $80.8 \%$ of the man over boards resulted in loss of life. Other accident types with high risk of loss of life are occupational accidents ( $53.8 \%$ ), sinking ( $43.6 \%$ ) and collision ( $19.6 \%$ ). When the general situation was examined, $37.6 \%$ of the accidents in the data set resulted in loss of life. The relationship between

accidents and loss of life proves (Phi value: 0.487 ) that accidents have resulted in significant moral destruction as well as asset losses.

# 5. Result and Discussion 

The most common accident categories observed in fishing vessels are collision and sinking, respectively (Table 1). Trawlers are the most common type of vessel with fishing accidents ( 118 accidents). $66 \%$ of collisions and $53.8 \%$ of occupational accidents occurred in trawlers. Sinking is the riskiest category of accident in terms of loss of vessel. $84.6 \%$ of grounding accidents, $63.5 \%$ of sinking accidents and $51.8 \%$ of collision accidents occurred in coastal waters. $74.7 \%$ of the accidents occurred in vessels of 20 years or older.

The Bayesian networks (accident network) created in this study summarize the occurrence of accidents for both fishing vessel accident types (sinking and collision). This network allows us to analyse not only the root causes of accidents, but also the causal and environmental factors. In addition, this network structure shows the relationship between these factors by using a conditional probability approach. Thus, network users can both understand the occurrence of accidents and estimate the risk of accident due to various conditions. When the results of the accident network sensitivity analysis are examined, the most important causal factors that play a role in the formation of sinking accidents in fishing vessels are: old vessel structure ( $25.66 \%$ ), overload vessel ( $19.06 \%$ ) and loss of water tightness ( $14.54 \%$ ) (Table 12). The most important root causes are: Loss of buoyancy ( $40.49 \%$ ), taking water ( $38.87 \%$ ) and loss of stability ( $27.96 \%$ ). The results related to loss of buoyancy and negative stability obtained from the accident network are similar to those reported by Håvold (2010) and Davis et al. (2019). In addition, this study shows that old vessel structure and the loss of water tightness affect the occurrence of sinking accidents.

As in the studies conducted by (Soares and Teixeira, 2001; Jin, 2014; Pitman et al. 2019) the most important environmental factor affecting the formation of sinking in fishing vessels was found to be bad weather and sea conditions. In this study, the effect of bad weather and sea conditions on the occurrence of sinking accidents is found to be $52.8 \%$. The accident network sensitivity analysis results in the study show that sinking is highly probable in bad weather and sea conditions when loss of buoyancy occurs ( $94.72 \%$ ). Unlike the studies in the literature, the accident network created in this study is able to estimate possible combinations of influencing factors and their probability values that may cause accidents in fishing vessels. The other most likely accident occurrence combinations are loss of stability ( $80.4 \%$ ) in bad weather and sea conditions, and when carrying loads (fished seafood) above the transport limits in bad weather

and sea conditions ( $78.4 \%$ ). The fact that all of the most probable accident occurrences take place in bad weather conditions reveals that this environmental factor is an important problem that should be considered in order to prevent accidents in fishing vessels.

Sometimes unsafe actions on one vessel and sometimes on both vessels can lead to the occurrence of collision accidents. In this study, only the role of fishing vessels in the occurrence of collision accidents was evaluated. The most important causal factors that play a role in the occurrence of collision accidents are respectively: improper lookout (39.78\%), occupation with other tasks (34.48\%), and remaining bridge without watchkeeper (34.26\%) (Table 13). The most important root causes are not being able to understand the intention of the target vessel $(41.02 \%)$ and not detecting the presence of the target vessel ( $40,26 \%$ ). Collision accidents are inevitable as a result of the inability to understand the target vessel's intention and as a result of the inability to make appropriate collision avoidance manoeuvre (violation of COLREG (The International Regulations for Preventing Collisions at Sea) rules 8 and 17) (Figure 2). Many studies that analyse collision accidents in the literature have emphasized the COLREG violation (Uğurlu et al., 2015) and the failure to detect the risk of collision (Belcher, 2002; Wang et al., 2005; Park et al., 2013; Kao and Chang, 2017). The failure to detect the target vessel is an indication that the lookout is improper. Although the emergence of this root cause at first glance seems to be incomprehensible, when the causal factors are examined, it is seen that the most important factors underlying this are occupation with other tasks, remaining bridge without watchkeeper and improper lookout. Occupation with other task and remaining bridge without watchkeeper are unacceptable unsafe acts. There is a high probability of a collision accident as a result of occupation with other task (net fishing, fishing activity, deck cleaning, etc.) (Table 13). In other words, as a result of these actions, the target vessel cannot be detected because the lookout could not be performed properly. Collision accidents can become inevitable, especially if there is improper lookout during night shifts or in restricted visibility. Even though the concentration of fishing vessel collisions at night can be related to the fact that fishing activities are usually carried out at night or in the early hours of the night, the limitation of the darkness of the night is the factor that plays a role in the formation of collision accidents. As it can be understood from the accident network established in the study, occupation with other tasks, fatigue and remaining bridge without watchkeeper on the other side are the most important reasons for this. Environmental factors that play a role in the occurrence of collision accidents are the type of navigation (navigating in coastal waters) ( $41.02 \%$ ) and the restricted visibility $(36.18 \%)$.

When the possible accident occurrence combinations are examined for collisions, it is seen that the accidents occur as a result of double and triple combinations. Binary combinations include type of navigation and root causes. Triple combinations include root causes, type of navigation and restricted visibility. The most likely dual accident occurrence combinations for collisions are one associated with ITV and CW (55.36\%), and one with PTV and OS (54.84\%). In other words, the risk of accident increases if a fishing vessel navigating in coastal waters does not understand the target vessel's intention or is unaware of the presence of the target vessel. These binary combinations have the highest value of the probability of collision accidents where there are factors restricting the visibility (e.g. presence of deck lighting, ambient lights and night).

In this study, Chi-square independence tests were conducted to evaluate the existence and level of the relationship between the accident type and vessel type, vessel length, vessel age, accident area, daylight, loss of vessel and loss of life variables. As a result of the study, it was found that there was a significant relationship between accident type and vessel length, vessel age, loss of vessel and loss of life. It was observed that sinking, collision and grounding accidents increased as the length of the vessel became shorter. This is in line with the findings reported (Jin and Thunberg, 2005; Wang et al., 2005). The vessels where accidents are most common have a length of 15-23 m. Sinking is most commonly seen on fishing vessels with a length of 7-14 m (58.2\%). As with other vessels, the legal regulations and safety measures to be applied in fishing vessels vary with the size of the vessel. As the vessel getting smaller, it is not subject to standard construction and operational safety requirements. Therefore, accidents and losses are more likely in these vessels. Unlike the studies in the literature (Turan et al., 2003; Kim et al., 2013; Davis et al., 2019; Pitman et al., 2019), the important result obtained from the Chi-square test is that vessel age has a significant relationship with accident types. For all types of accidents, the number of accidents increases as vessels become older. There was also a significant relationship between the type of accident and the loss of vessels. According to this result, the riskiest type of accident in terms of vessel loss is sinking accidents. In $80 \%$ of the sinking accidents in the data set examined, the vessel was completely sunk. The second riskiest type of accident in this regard is grounding accidents (30.4\%). Similarly, studies in the literature (Baldauf et al., 2014; Montewka et al., 2014; Lehikoinen et al., 2015; Uğurlu et al., 2015) indicate that sinking and collision accidents are the riskiest types of accidents in terms of losses. Finally, the Chi-square test results also show that the type of accident was related to loss of life. When the number of accidents with loss of life is examined, the riskiest types of

accidents are man over board (80.7\%), occupational accidents (48.7\%), sinking (43.6\%) and collision (19.7\%) accidents, respectively.

# 6. Conclusion 

Fishing vessel accidents often result in loss of life or loss of vessel. Most accident analysis studies conducted in the context of collusion and sinking accidents have focused on the responsibilities and role of commercial vessels in accidents (Jaremin and Kotulak, 2004; Håvold, 2010; Roberts et al., 2010; Jensen et al., 2014; Jin, 2014; Davis et al., 2019). In this study, an accident network is presented which summarizes the occurrence of collision and sinking accidents. This network allows to understand the occurrence of fishing vessel accidents and to take measures to prevent them. All results show that the safety measures applied in fishing vessels should be reviewed and additional measures should be taken in consideration with the above mentioned issues. The results of the study can be listed as follows:

- It has been found that the risk of sinking accidents is very high when loss of buoyancy occurs in fishing vessels navigating in bad weather and sea conditions. The most important causal factor in the formation of loss of buoyancy is the old vessel structure. In this study, it is found that the risk of accident is very high especially in vessels with an old vessel structure of 7-14 m long. In order to prevent sinking accidents, fishing vessels over 20 years of age, especially those under the length of 14 m , should be scrutinised in fishing activities. This is an important issue to be addressed.
- In this study, it was determined that another important root cause that caused the sinking accidents in bad weather and sea conditions was loss of stability. Causes of loss of stability in fishing vessels are overloading resulting from overfishing, and the use of improper fishing equipment. In order to eliminate the factors that cause loss of stability in fishing vessels, it is necessary to establish a vessel-specific hunting limit by considering the vessel length and hunting vehicles, and to ensure that the appropriate standards in the fishing equipment are used.
- Collisions have been observed in coastal waters as a result of inability to understand the target vessel's intention or to perceive the target vessel, especially at night. For fishing vessels, lookout (watchkeeping) activities should be meticulously carried out during night hours, especially in coastal waters, where the risk of collision accidents is high. It is important to have fishing vessels equipped with a sufficient number of seafarers and to ensure safety awareness of the personnel working on these vessels.
- One of the important results of this study is that there is a significant relationship between the accident type and vessel length, vessel age, loss of life and vessel loss. A significant

increase was observed in all accident categories as the ship age increased. Although this increase is mostly seen in sinking accidents, there is also a high increase in other accident categories such as collision, grounding, fire and explosion. Therefore, the old vessel structure plays an important role in the formation of accidents in all accident categories in fishing vessels. Concentration of accidents, especially on old vessels, can be interpreted as an indication that sanctions are inadequate. In order to reduce the risk of accidents in fishing vessels, age limitation must be introduced (e.g. 20 years).

- It has been observed that as the ship becomes smaller, the number of accidents increases. This increase is concentrated on vessels under 24 m . There is almost no accident occurrence in vessels over 24 m . Although this increase can be interpreted as the fact that the number of vessels over 24 m in the world fishing vessel fleet has a lower share compared to other boats, it can be thought that national and international measures applied to vessels over 24 m may play a role in avoiding frequent accidents. In other words, as the length of the vessel decreases, the minimum equipment required and the safety measures to be applied are reduced. This is the factor that causes the accident in fishing vessels.

Accidents can be prevented by understanding how they occur. Therefore, determination of the factors that play a role in the formation of fishing vessel accidents is important to prevent these accidents in the future. In order to prevent the occurrence of accidents, it is necessary to focus on unsafe events as well as the causal factors leading to the formation of these unsafe events. Preventing accidents becomes possible by focusing on these causal factors and understanding their occurrence.

# Acknowledgements 

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 730888. The study was supported by TUBITAK (The Scientific and Technological Research Council of Turkey/2219 scientific research support program). The authors would like to thank anonymous reviewers for their constructive suggestions.
