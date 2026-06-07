# LJMU Research Online 

## Özaydın, E, Fışkın, R, Uğurlu, Ö and Wang, J

## A hybrid model for marine accident analysis based on Bayesian Network (BN) and Association Rule Mining (ARM)

## http://researchonline.ljmu.ac.uk/id/eprint/17372/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Özaydın, E, Fışkın, R, Uğurlu, Ö and Wang, J (2022) A hybrid model for marine accident analysis based on Bayesian Network (BN) and Association Rule Mining (ARM). Ocean Engineering, 247. ISSN 0029-8018

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# A Hybrid Model for Marine Accident Analysis based on Bayesian Network (BN) and Association Rule Mining (ARM) 

Özkan Uğurlu ${ }^{a}$ (corresponding author), Remzi Fışkın ${ }^{\text {b }}$, Emre Özaydın ${ }^{\text {c }}$, Jin Wang ${ }^{d}$<br>${ }^{a}$ Faculty of Marine Sciences, Ordu University, Ordu, Turkey, ougurlu@odu.edu.tr, ozkanugurlu24@hotmail.com, 00905058179839, https://orcid.org/0000-0002-3788-1759<br>${ }^{\text {b }}$ Faculty of Marine Sciences, Ordu University, Ordu, Turkey, https://orcid.org/0000-0002-5949-0193<br>${ }^{\text {c }}$ Abdullah Kanca Vocational School, Karadeniz Technical University, Trabzon, Turkey<br>${ }^{d}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores<br>University, Liverpool, United Kingdom, https://orcid.org/0000-0003-4646-9106

# 1. Introduction 

Modern ships and advanced fishing equipment have transformed fishing into a more practical and faster field of activity (Marchal et al., 2007). Fishing is one of the occupational groups with high risk (Hasselback and Neutel, 1990, IMO, 2020, McGuinness et al., 2013a). It is estimated that over 24,000 fishermen die and approximately 24 million fishermen are injured each year (Fernando and Rubén, 2006). According to FAO (2001), the accident occurring rate in the fishing industry in Australia is 17.7 times higher than other industries. Roberts (2004) stated that the fatal incidents experienced in fishing activities in the UK are twice more than those on commercial vessels. Moreover, Lincoln and Lucas (2010) reported that the fatal occupational accident rate experienced in the fishing industry of the USA is 35 times higher than other occupational groups. The fact that occupational accidents frequently occur on fishing vessels, and with a high mortal accident rate compared to other industries, obliged the International Maritime Organization (IMO) to take strict safety measures on fishing vessels (Uğurlu et al., 2020a). Despite modern-advanced fishing equipment and rigid regulations taken to prevent accidents, accidents in fishing activities still continue.

Case studies investigating accidents occurring on fishing vessels in Poland and the UK have taken their place in the literature as the first scientific research on safety in the fishing industry (Bowdler, 1954, Burns, 1955, Ejsmont, 1958). Following these pioneering studies, the concept of safety in the fishing industry has become a multi-disciplinary field of research and has begun to be widely investigated. Many authors have prepared numerous papers in the last decades on this field. Roberts (2004) examined a total of 616 fatal accidents that occurred on fishing vessels in the UK between 1976 and 1995 and found that 73\% (454 accidents) of the accidents occurred during fishing activities. Lucas and Lincoln (2007) concluded that 24\% of occupational accidents on fishing vessels in Alaska occurred as a result of man overboard, and these accidents were primarily caused by slipping, losing balance, heavy weather conditions

and alcohol. Petursdottir et al. (2007) examined the fatal accidents that occurred on fishing vessels in Iceland between 1980 and 2005. They found that occupational accidents occurred on fishing vessels were mostly caused by the sinking, man overboard and being hit by an object. Frantzeskou et al. (2012) conducted surveys with 100 fishermen in Greece to determine the health and safety risk of fishing vessels. In this study, the accident exposure rate of the fishermen was found to be $28 \% ; 14 \%$ of them stated that they had fallen into the sea at least once. McGuinness et al. (2013a) and McGuinness et al. (2013b) surveyed fatalities and injuries in the commercial fishing fleet of Norway. The results show that there is a considerable reduction in fatalities and injuries number in the fishing fleet of Norway thanks to preventative strategies. Moreover, Domeh et al. (2021) presented a Bayesian Network application for risk assessment of man overboard cases in fishing vessels. "Failed to use fall arrest system" was demonstrated as the main pre-existing condition to cause a man overboard accident. In the effects of accidents perspective, Kaustell et al. (2019) focused on occupational injuries and diseases of fishermen in Finland. Dislocation, sprain and strain were found the most prevalent injury types for Finn fishermen. Furthermore, Soykan et al. (2021) tried to point out the fatality rate of accidents in the fishing industry in Turkey. The fatal accident rate in the fishing industry was determined much higher than in many other industries such as mining, construction and transportation.

Inadequate procedures, work preparation, training and insufficient experience are referred to as potential causes for maritime accidents in the literature (Coraddu et al., 2020; Chang and Lin, 2006; Puisa et al., 2018; Graziano et al., 2016). These phenomena, all of which are human error-based, may also be key factors for fishing vessels. Obeng et al. (2022), for example, revealed that inadequate training and insufficient experience are the risk causal factors for fishing trawlers. Moreover, Lazakis et al. (2014) conducted a comprehensive review of the factors contributing to accidents and near-miss incidents occurring on fishing vessels in the UK.

The study concluded that trawlers have more occupational accidents than other fishing vessel types and, the majority ( $89 \%$ ) of these occupational accidents were based on human error. Thorvaldsen et al. (2020) focused on the occupational health, safety and work environment of Norwegian fishermen. They demonstrated that the work environment may affect the fishers' health condition with strain and acute injuries being the most common injuries due to a poor working environment.

Consequently, Table 1 summarizes aforementioned studies carried out within the scope of occupational accidents on fishing vessels.

Table 1. Current studies on the analysis of occupational accidents occurred on fishing vessels

Learning lessons from past accidents is critically important for reducing and preventing the occurrence of them (Uğurlu et al., 2015). However, the lack of reliable and valid accident data is a serious limitation to doing so (Pirdavani et al., 2010). Data on occupational accidents is still not reliably reported in most countries around the world (Jacinto and Aspinwall, 2004, Uğurlu et al., 2017). The commercial concern of the ship-owners is thought to be significant in failing to collect the occupational accident reports regularly and systematically (Jensen et al., 2014). The reporting rate of marine accidents is $59 \%$ in Norway, $44 \%$ in the UK and $90 \%$ in Canada (Hassel et al., 2011). According to the study by Thomas and Skjong (2009), only 30\% of fire and explosion accidents in chemical tankers are reported. Wang et al. (2005) emphasized that the reporting rate is also limited in fishing vessels activities. Particularly, minor fisher injuries are not reported regularly and reliably (McGuinness et al., 2013b).

Unreported marine accidents are still an important issue for the maritime industry. Conducting studies based on unreported marine accident data enables researchers to reveal the causes of accidents that have not been brought to light, and to strengthen the shortcomings of

accident investigations. In this perspective, many studies were conducted based on unreported accidents data (Uğurlu et al., 2017, Hassel et al., 2011, Frantzeskou et al., 2012). Unlike studies in the literature, in this study, unreported occupational accidents that occurred on Turkish fishing vessels were analysed. A two-stage approach combining the Bayesian Network (BN) and Association Rule Mining (ARM) methods, was utilized for the analysis of accidents. As a result of the study, not only the causes of the accidents and the environmental conditions affecting the occurrence of the accidents but also the relationship between them, were examined (via BN). In addition, in this study, the minimum requirements required for the occurrence of occupational accidents on fishing vessels were determined by taking the accident data into consideration (via ARM). This study provides a hybrid model for the analysis of occupational accidents on fishing vessels.

The remaining sections of the paper are structured as follows. Section 2 and Section 3 introduce the modelling theories to be utilized, followed by Section 4, which provides the proposed methodology and its explanation. Experimental results of the methods implemented and discussions with other studies are presented in Section 5. Finally, Section 6 concludes the study including the final evaluation of the results.

# 2. Bayesian Network 

Bayesian Networks (BNs) are widely employed in quantitative risk assessments, especially in non-precision information estimates under uncertainty (Petra et al., 2016, Ni et al., 2016, Li et al., 2014). A BN is a graphical model that encodes probabilistic relationships among a group of variables (Martin et al., 2009, Jensen et al., 2009). In general, a BN consists of two main parts, the graphical part where the nodes and edges are shown, and the quantitative part where the variables are expressed by conditional probability tables (Wang et al., 2013; Cakir et al., 2021). There are 4 types of nodes in a BN: Root node, parent node, child node and result

node (Trucco et al., 2008, Loughney and Wang, 2018). The absence of an edge between two nodes in a network indicates that there is no possible relationship between these variables (Bhattacharya, 2012). There are no restrictions on the number of parent or child nodes that the network may have (Korb and Nicholson, 2004).

Conditional probability logic must be known in order to calculate the probability values of nodes in the BN. They can be expressed by statements such as "B occurs given that A has already occurred" and "given event A, the probability of event B is ' p '", which is denoted by $P(A \mid B)=\mathrm{p}$. This especially means that if event A occurs and everything other than A is unrelated to event B , then the probability of B is ' p '. Conditional probabilities are part of the joint probability of the intersection of A and $\mathrm{B}, P(A \cap \mathrm{~B})$.

$$
P(A \cap \mathrm{~B})=P(B \mid A) \times P(B)=P(A \mid B) \times P(A)
$$

Suppose $\left(B_{i}, i, \in n\right)$ is a countable collection of events. Let $A$ be another event and suppose $\mathrm{P}\left(\mathrm{B}_{\mathrm{i}}\right)$ and $\mathrm{P}\left(\mathrm{A} \mid \mathrm{B}_{\mathrm{i}}\right)$ for each $\mathrm{i} \in \mathrm{n}$ are known. Then the total probability formula is:

$$
P(A)=\sum_{i=1}^{n} P(B i) P(A \mid B i)
$$

There are n number of B events that intersect with the A event; the probability of event Bi given event A is known:

$$
P(B i \mid A)=\frac{P(A \mid B i) \times P(B i)}{P(A)} \quad i=1,2,3, \ldots, n
$$

# 3. Association Rule Mining (ARM) 

Data mining, whose main purpose is to understand data, is defined as a process of producing knowledge from a large amount of data (Han et al., 2011). There are three main

components of data mining: Clustering, classification and prediction. Extracting knowledge from data is performed depending on these three basic components (Wu et al., 2008). One of the most important and frequently used functions of data mining is ARM. Compared with traditional parametric and non-parametric methods, ARM has a flexible structure. The most advantageous aspects is that it has a simple structure and does not need dependent variables (Győrödi et al., 2004). The disadvantage of the ARM method is that there are irrelevant or unnecessary rules created in high-dimensional data sets. Certain restrictions can be used to filter these rules. The purpose of this filter is to discover important association rules and speed up the search process. The fields where the method is most frequently employed are medicine and health (Nahar et al., 2013), transportation (Changhai and Shenping, 2019, Weng and Li, 2019), and finance (Ho et al., 2012).

The rule structure emerging in ARM can be exemplified as follows. Assuming that the consequent variable is a serious accident, the association rule structure can be formed as: "If \{Strong_wind $=$ Yes, Lookout_failure $=$ Yes, Operation_error $=$ Yes $\} \rightarrow$ class "serious". 'Class' denotes a predetermined target or dependent variable. 'Serious' is the label of a class to which records can be assigned. This rule states that serious accidents may occur as a result of a combination of strong wind, lookout failure and operational errors (Weng and Li, 2019). The mathematical definition of ARM is as follows.

Suppose there are a set of attributes $I=\left\{a_{1}, a_{2}, \ldots a_{m}\right\}$ and a set of transactions $D=\left\{t_{1}, t_{2}\right.$, $\left.\ldots, t_{n}\right\}$ called items and dataset, respectively. Each transaction has a unique feature and contains a subset of items $t_{i} \subset I$ called an itemset. The association rule is an extraction $X \rightarrow Y$, where $X$ and $Y$ are two itemsets, and holds $X \cap Y=\varnothing . X$ is called as the antecedent (Left Hand Side (LHS)) and $Y$ is called as the consequent (Right Hand Side (RHS)) (Agrawal and Srikant, 1994). In ARM, there are two metrics that measure the importance and significance of the rules:

"support" and "confidence". "Support" defines the number of database records within which the association can be observed (Sinthuja et al., 2017).

$$
\text { support }(X \rightarrow Y)=\frac{X U Y}{\text { Total number of transactions in data base }}
$$

On the other hand, "confidence" refers to the ratio of all data containing $X U Y$ to all data containing $X$ in the dataset, and is defined by Equation (5). "Support (X)" is the number of transactions that contain X. "Support $(X U Y)$ " is the number of transactions involving X and Y together.

$$
\text { confidence }(X \rightarrow Y)=\frac{\text { support }(X \cup Y)}{\text { support }(X)}
$$

There are many proposed ARM algorithms in the literature. However, the most widely recognized and used ones are Apriori, Predictive Apriori and Tertius. These algorithms have been applied in many studies (Patil et al., 2011, Weng and Li, 2019). Therefore, in this study, the association rules were proposed using a Predictive Apriori algorithm, which is an extended form of the Apriori algorithm, to explore the unreported fishing vessel accidents' contributory factors. The ARM application was performed utilizing the Weka tool, version 3.8.3 (Frank et al., 2016).

The Predictive Apriori algorithm, proposed by Scheffer (2001), is an algorithm extended from the Apriori algorithm. The algorithm is based on the principle of providing the maximum accuracy by evaluating the support and confidence values of the association rules together. Unlike the Apriori algorithm, in the Predictive Apriori algorithm, in order to measure the importance and meaningfulness of association rules, the support and confidence parameters are gathered under a single criterion called predictive accuracy (Mutter et al., 2004). The Predictive Apriori algorithm takes the support value into account in addition to the confidence value in

measuring the rules. It uses the Bayesian framework in implementing the algorithm procedure (Nahar et al., 2013). This procedure is described by Scheffer (2001) as follows: "Let $D$ be a database whose individual records $r$ are generated by a static process $P$, let $[x \rightarrow y]$ be an association rule. The predictive accuracy $c([x \rightarrow y])=P r[r$ satisfies $y \mid r$ satisfies $x]$ is the conditional probability of $y \subseteq r$ given that $x \subseteq r$ when the distribution of $r$ is governed by $P$. "

The mathematical definition of predictive accuracy is defined by Equation (6) (Scheffer, 2001):

$$
E(c(r) \mid \hat{c}(r), s(X))=\frac{\int c B[c, s(X)](\hat{c}(X \rightarrow Y)) \pi(c) d c}{\int B[c, s(X)](\hat{c}(X \rightarrow Y)) \pi(c) d c}
$$

where $E(c(r) \mid \hat{c}(r), s(X))$ is the expected predictive accuracy of a rule $r(X \rightarrow Y), \hat{c}$ denotes the confidence, $s(X)$ denotes the support of $X, B$ refers the binomial distribution, and $\pi$ defines the prior accuracy.

As a result, considering the above mathematical definition, the relationship between support $s(X)$ and confidence $\hat{c}(X \rightarrow Y)$ to represent the predictive accuracy $\mathrm{c}(X \rightarrow Y)$ of rule $(X \rightarrow Y)$ is represented with a three-dimensional diagram illustrated in Figure 1.

Figure 1. Contributions of support $s(X)$ and confidence $\hat{c}(X \rightarrow Y)$ to predictive accuracy $\mathrm{c}(X \rightarrow Y)$ of rule $(X \rightarrow Y)($ Scheffer, 2001)

# 4. Method 

In order to ensure maritime safety and sustainable maritime trade, it is very important for all stakeholders of the industry to carry out studies on unreported marine accidents. Therefore, this study is aimed to collect and analyse the data of unreported occupational accidents that occurred in commercial fishing activities. In this study, occupational accidents on fishing vessels with a full length of 12 meters and over between 2000 and 2018 are

investigated. The fishing vessels are limited to trawlers and purse seiners operating in Turkey. It is the responsibility of Turkish Accident Investigation Board (KAIK) to prepare and store accident investigation reports for marine accidents on Turkish flagged vessels. However, the number of accident reports related to fishing vessels in the database is very low. In order to ensure maritime safety and sustainable maritime trade, it is very important for all stakeholders of the industry to carry out studies on unreported marine accidents. Therefore, this study is aimed to collect and analyse the data of unreported occupational accidents that occurred in commercial fishing activities. Accident data was collected through face-to-face interviews with fishermen at the ports where fishery cooperatives are located. As a result of the interviews, a total of 173 unreported occupational accidents are obtained. The accident data collected in this study is related to cases of injuries, disability or deaths. Cases such as ship loss, environmental pollution or ship structural damage are not included in the scope of this study.

This study revealed that Bayesian Network and ARM methods could be used in a hybrid way within the scope of accident analysis. An accident network structure that summarizes occupational accidents in fishing vessels with the Bayesian network approach has been revealed. This network structure allows users to predict the risk of occupational accidents on fishing vessels under variable conditions. With the Predictive Apriori algorithm, the minimum conditions required for occupational accidents to occur on fishing vessels can be determined. The study consists of the following 4 steps.

Step 1: In the first step of the study, a Microsoft Excel based database with data obtained from fishermen is created. In accident investigation studies, data pre-processing is applied to make the data for analysis available before starting the analysis. For this purpose, many researchers identify descriptive information as well as reasons that play a role in the occurrence of accidents. The database contains descriptive information such as operation status, ship type,

hull length, accident consequence, weather and sea condition, the hunting equipment causing the accident, the time of the accident (daylight or night) as well as the causes of the accident.

Step 2: In Reason's Swiss Cheese Model, the events leading to accidents are grouped under two main headings: Latent factors and active failures. Active failures are the visible side of accidents. According to this model, each accident contains active failures, and behind the active failures there are latent factors (Reason, 1990, Uğurlu et al., 2018). In the modified human factor classification system (HFACS-PV) proposed by Uğurlu et al., (2018) for the analysis of marine accidents, it has been observed that marine accidents do not occur only as a result of active failures and latent factors, but also every active failure requires appropriate operational conditions (environmental factors) to result in an accident. Operational conditions are not a pre-condition (latent factor) that leads to unsafe act, but a necessary complementary factor for unsafe act to result in an accident. Each marine accident needs at least one operational condition. Operational conditions include the internal-external operational environment in which the accident occurred, meteorological conditions and malfunctions that prevent ship movement. They proved the validation of this classification (latent factors, active failures, and operational conditions) with 4 studies (Uğurlu et al., 2018, Uğurlu et al., 2020a, Uğurlu et al., 2020b, Sarıalioğlu et al., 2020). In this study, the causes of occupational accidents on fishing vessels are categorized by considering this hierarchical structure. At this step of the study, the data obtained in the previous step is thoroughly examined, and active failures, latent factors and environmental factors of accidents are identified. Based on such data, an accident network is created that summarizes the occurrence of occupational accidents on fishing vessels. The BN method is used for the establishment of the accident network. The fact that the BN model does not depend on a single variable and can be made inference for all variables in the network makes it an effective decision-making and analysis tool (Uğurlu et al., 2020b). The relationship between nodes, and conditional probability tables can be established using two main

approaches. The first one is based on statistical data obtained from the database and the other one is based on expert opinions. In practice, if needed, these two approaches can be used in a combined way. For example, while numerical parameters can be obtained from a database, the network structure may be created taking the expert opinion into account (Cheng and Greiner, 2001, Pristrom et al., 2016; Uğurlu et al., 2020a, Uğurlu et al., 2020b). In this study, a combined approach is chosen for use. The network structure is established by taking expert opinions into consideration; conditional probability tables are created based on the data obtained from the database. The experts interviewed in this study are knowledgeable in the fields related to maritime, fishing and hunting operations. Explanatory information about the expert group is as follows:

Expert 1: Maritime expert on accident investigation with experience in marine accidents, occupational accidents and fishing vessel accidents - 1 person.

Expert 2: Marine engineer specialized in hunting technologies, design of fishing gear, underwater technologies, and management of fishing vessels - 2 persons.

Expert 3: Marine engineer specialized in fisheries management, fish farming, aquaculture marketing and fishing vessels - 2 persons.

Expert 4: Master mariner with 10 years of experience on fishing vessels - 2 persons
Step 3: In the third step of the study, a total of 3 axiom tests are applied to demonstrate the accuracy of the network (accident network). Axiom tests are used for validation in many BN studies (Pristrom et al., 2016). Sensitivity analysis is performed after proving the validity of the network, as well. With sensitivity analysis, the effect of nodes on accident occurrence can be observed (Uğurlu et al., 2020b). The BN created in this study summarizes the occurrence of occupational accidents on fishing vessels. With this network, accident investigators can predict the occurrence of occupational accidents under changeable conditions (operational conditions, active failures and latent factors). Furthermore, the effect of the measures taken to

prevent accidents on fishing vessels can be observed. In this study, all calculations and analyses are conducted using the software tool named Genie. Genie is selected for use due to its easy and understandable user interface (Fusion, 2017).

Step 4: Marine accidents occur as a result of chain errors. Identifying combinations of factors leading to accidents allows accident investigators to understand how accidents occur (Uğurlu et al., 2015). ARM is a useful method especially in extracting the implicit knowledge within databases and discovering the association rules among a set of variables (Nahar et al., 2013). In this study, the BN method explains the occupational accidents that occur on fishing vessels with the conditional probability approach. The ARM method, on the other hand, defines the minimum conditions required for the occurrence of an occupational accident. Similar to the BN, data pre-processing is also required in ARM. For this purpose, the antecedent and consequent variables to be used in the application should be determined (Agrawal and Srikant, 1994, Sinthuja et al., 2017). In this study, ARM variables are obtained from the accident database created in the first step of the study. The antecedent variables in the ARM method include the operational conditions under which the accident occurred, and the general characteristics of vessels and the demographic profile of seafarers. The consequents, which are called "class" variables, on the other hand, are accident type and accident consequence. These 9 variables used in the ARM application are:

I- Education level: nominal - 3 values: uneducated (having no diploma but can read and write), primary education (having primary education diploma), and at least high school education (having at least high school or higher education diploma).

II- Vessel length: nominal - 2 values: $<24$ (under 24 m ), $\geq 24$ (greater than or equal to 24 m ). III- Vessel type: nominal - 2 values: trawl, seine.

IV- Experience: nominal - 2 values: $<10$ (under 10 years), $\geq 10$ (greater than or equal to 10 years).

V- Weather and sea condition: nominal - 2 values: good (4 Beafourt and below), bad (5 Beafourt and above).

VI- Day status (Time): nominal - 2 values: daylight (06:00/17:59), night (18:00/05:59).
VII- Sleeplessness: nominal - 2 values: no (at least 8 hours sleep over the last 24 hours), yes (less than 8 hours sleep over the last 24 hours); classified regarding the sleep time duration recommendation report prepared by Hirshkowitz et al. (2015) on behalf of Sleep Foundation of US.

VIII- Accident type (class variable): nominal - 3 values: man overboard, hit by an object, and jamming.

IX- Accident consequence (class variable): nominal - 3 values: injury, disabled, dead.

# 4.1. Occupational Accidents on Fishing Vessels 

The most frequently observed occupational accidents on fishing vessels are man overboard ( 66 accidents), hit by an object ( 65 accidents) and jamming ( 42 accidents). $73 \%$ of fatal accidents, $83 \%$ of disability and $68 \%$ of injuries occurred in purse seine (Table 2). The most frequently observed accident category in purse seine vessels is hit by an object, whereas man overboard in trawl vessels. One of the interesting findings of the study is that occupational accidents are concentrated in fishermen with 10 years or more experience ( $49 \%$ ). $67 \%$ of the accidents are associated with seafarers' lack of sleep which is the main cause of fatigue. 79\% of accidents occurred on fishing vessels with a length of 24 meters and over.

Table 2. General distribution of occupational accidents on Turkish fishing vessels.

# 4.2. Bayesian Network Applications 

The BN created in the study consists of 4 levels: Level 1 - latent factors, Level 2 - active failures, Level 3 - operational conditions (environmental factors), and Level 4 - accidents (Figure 2). Each node in the network represents a cause of the accident or an operational condition. The BN (accident network) is created considering the accident data (based on interviews), the way accidents occurred and expert opinions. Table 3 shows the nodes in the BN created in this study with their abbreviations, probability values, parents and child nodes.

Figure 2. Accident network (Bayesian network) structure used in this study
Table 3. Content of the Bayesian network

### 4.2.1. Factors that Play a Role in the Occurrence of Occupational Accidents on Fishing Vessels

### 4.2.1.1. Latent Factors

The latent factors are represented in green in the BN (Figure 2). Many researchers emphasize that latent factors in accidents are difficult to identify (Gordon, 1998, Uğurlu et al., 2018). In this study, latent factors are examined at two sub-levels: Pre-conditions for unsafe acts (dark green) and inconveniences (light green) leading to the formation of these preconditions. (Figure 2). Pre-conditions for unsafe acts are examined under 4 nodes as nonconformity in hunting gear, inappropriate personal protective equipment, lack of situational awareness and lack of communication.

Non-conformity in Hunting Equipment: Nowadays, fishing gears have been developed in parallel with technologies (Szczepanek et al., 2018, Uğurlu et al., 2020a). However, these technological developments, which provide great convenience to the employees, bring new risk factors (Kim et al., 2019, Sur and Kim, 2020). Non-conformities in fishing gears (such as

windlass, net, fish pumps, net reels, davit and mast equipment) are considered under this node. There are two parent nodes for this node: Malfunction in the fishing gears and hunting equipment experience (Figure 2).

Inappropriate Personal Protective Equipment: Protective equipment is personal protective safety equipment designed to prevent a hazard in working conditions or to protect the employee in case of danger. These include personal equipment such as hard hats, lifejackets, safety shoes, gloves and seat belts. When the accident is unavoidable (Hollnagel, 2016), protective equipment provides the last barrier, helping mitigate consequences. Parent nodes that play a role in the formation of inappropriate personal protective equipment are protective equipment ergonomics defect (uncomfortable equipment), insufficient training and lack of equipment. Situational Awareness: Lack of situational awareness affects seafarers' perception of existing risks and may lead to an accident (Sanfilippo, 2017). This may occur as a result of fatigue, alcohol or busyness with another work (Hystad et al., 2017, Last et al., 2017). There are two factors that affect fatigue formation in the BN established in the study. These are excessive workload and sleeplessness.

Communication and Coordination: Lack of communication and coordination on fishing vessels is caused by bad team synergy, hearing barrier and vision barrier. Fishing is teamwork. Disagreements and personal conflicts among the fishermen can cause tensions within the team. This situation, which is called bad team synergy, weakens the communication and coordination among the fishermen. On fishing vessels, main engines, auxiliary engines and fishing gears are the main source of noise. Noise causes temporary hearing loss. This situation in the BN is called as hearing barrier. Obstacles on deck, poor lighting and strong sun rays weaken the vision. This situation in the BN is called as vision barrier.

# 4.2.1.2. Active Failures 

In this study, the events causing the accident are named as active failures. Most accident reports contain detailed information about active failures. Focusing on active failures is the first step to understanding accident occurrences (Uğurlu et al., 2018). Therefore, active failures are the main focus of accident investigations (Li and Harris, 2006). Accident investigators can easily reveal possible latent factors by analysing the active failures in-depth. In this study, nonconformities causing active failures are addressed under the pre-conditions for unsafe acts.

### 4.2.1.3. Operational Conditions

Accident occurrences are inevitable when active failures are combined with inappropriate operational conditions (Uğurlu et al., 2018). Each accident event involves at least an active failure and an operational condition (Sarıalioğlu et al., 2020, Uğurlu et al., 2020). The operational condition is divided into 2 sub-categories as internal and external environment (Uğurlu et al., 2020b). They are shown in blue in the BN. Internal environmental factors are conditions, which can be partially controlled by fishermen. In this study, it is named as an inappropriate operational environment. The preconditions that lead to an inappropriate operational environment are a messy working environment and slippery ground. The presence of fishing gears such as nets and ropes on fishing vessels causes a crowded and mixed working area (Fulmer and Buchholz, 2002). Failure to stack the nets properly after fishing activities and leaving the ropes scattered pose a risk to fishermen. These situations are shown as a messy working environment in the BN. Fishing activities are usually carried out on the deck which is the main location of occupational accidents occurrences onboard (McGuinness et al., 2013b). Seawater spillage, oil spillage and sea creatures create a dangerous working environment for fishermen while working on deck. They are called slippery ground in the BN. External environmental factors are conditions that occur outside the control of fishermen. Weather and sea conditions, and day status are considered as external environmental factors.

# 4.2.1.4. Result Nodes 

The BN in this study has 3 result nodes: Man overboard, hit by an object, and jamming. They are represented by orange in the BN. Table 3 provides explanatory information about the result nodes. The most common causes of man overboard are slippery surface, loss of balance and entanglement in the fishing gear. Being stuck in a rolled rope and catching by a capstan are evaluated as jamming. Hit by an object, on the other hand, is associated with falling of any object, rope breaking and crashing lifting equipment.

### 4.2.2. Test Case for Bayesian Network

Child node "Fatigue" (Yes/No) is chosen for the calculation example. This node has two parent nodes, namely "Workload" (Excessive/Normal) and "Sleeplessness" (Yes/No) (Figure 3), which are root nodes.

Based on the accident data, the initial (marginal) probability values of these two root nodes are calculated as follows. The "Excessive Workload" is seen in 58 of 173 accidents. Therefore, the initial probability value for the "Excessive" state of the "Workload" node is calculated as $58 / 173=0.3352$ (33.52\%). The probability value for the "Normal" state is 1$0.3352=0.6648(66.48 \%)$. The initial probability value for the "Yes" state of the "Sleeplessness" root node is $32.94 \%$ (57/173), and the initial probability value for the "No" state is $67.06 \%$ (1-0.3294) (Figure 2).

Figure 3. Bayes network structure for the "Fatigue" node
Table 4. Conditional probability tables for the "Fatigue" node

According to the BN created in the study, there are a total of 4 combinations in which "Fatigue" is "Yes" or "No". The conditional probability values for these 4 combinations are presented in Table 4. Based on these conditions, the posterior probability values for the "Yes"

and "No" states of the "Fatigue" node are calculated as $35 \%$ and $65 \%$, respectively. The posterior probability value for the "Yes" state of "Fatigue" is obtained as follows:

$$
\begin{aligned}
& \mathrm{P}(\text { Fatigue (Yes) })=\left[(\mathrm{P}(\text { Fatigue(Yes }) \mid \text { Workload(Excessive), Sleeplessness(Yes) }) \times\right. \\
& \mathrm{P}(\text { Workload(Excessive })) \times \mathrm{P}(\text { Sleeplessness(Yes }))]+ \\
& \left[(\mathrm{P}(\text { Fatigue(Yes) } \mid \text { Workload(Excessive), Sleeplessness(No) }) \times\right. \\
& \mathrm{P}(\text { Workload(Excessive }) \times \mathrm{P}(\text { Sleeplessness (No }))]+ \\
& \left[(\mathrm{P}(\text { Fatigue(Yes) } \mid \text { Workload(Normal), Sleeplessness(Yes) }) \times\right. \\
& \mathrm{P}(\text { Workload(Normal })) \times \mathrm{P}(\text { Sleeplessness(Yes }))]+ \\
& \left[(\mathrm{P}(\text { Fatigue(Yes) } \mid \text { Workload(Normal), Sleeplessness(No) }) \times\right. \\
& \mathrm{P}(\text { Workload(Normal }) \times \mathrm{P}(\text { Sleeplessness(No }))] \\
& =\left(0.98 \times 0.34 \times 0.33\right)+\left(0.41 \times 0.34 \times 0.67\right)+\left(0.58 \times 0.66 \times 0.33\right)+ \\
& \left.(0.05 \times 0.66 \times 0.67\right) \\
& =0.35(35 \%)
\end{aligned}
$$

The posterior probability value for the "No" state of "Fatigue" is:

$$
\begin{aligned}
& =1-0.35 \\
& =0.65(65 \%)
\end{aligned}
$$

The nodes in the network and their posterior probability values are shown in Figure 4.

# 4.2.3. Validation 

Axiom tests are conducted to prove the validity of the network established in the study and the conditional probability tables it contains. Axiom tests are widely used by many researchers in Bayesian studies (Uğurlu et al., 2020a, Uğurlu et al., 2020b, Salleh et al., 2017). This study includes 3 axiom tests: Axiom 1, Axiom 2 and Axiom 3 tests.

Figure 4. Nodes in the network and their posterior probabilities

Axiom 1: The increase or decrease in the probability values of each parent node should cause a relative increase or decrease in the child node (Uğurlu et al., 2020a). The "Man Overboard" child node is chosen for the example. The parental nodes of this node are "Operational Environment", "Weather and Sea Condition", "Unsafe Act", and "Day Status" (Figure 4). As a

result of the test, it is observed that the increase (100\%) and decrease (100\%) of the parental nodes caused an increase and decrease in the child node in the corresponding direction (Table 5). Axiom 1 tests are applied for all nodes and similar results are obtained.

Table 5. Axiom 1 test results for the "Man Overboard" node.

Axiom 2: The impact of the gradual change in the probability values of each parent node (10\%, $20 \%, 30 \%, \ldots, 100 \%$ ) on the child node is expected to be consistent (Yang et al., 2008). The "Hit by an Object" node is chosen as an example to demonstrate the Axiom 2 test. The parent nodes of this node are "Weather and Sea Conditions", "Unsafe Acts" and "Day Status" (Figure 4). A gradual increase of each of these nodes causes a corresponding increase in the probability of the child node (Figure 5). Similar tests are made for the result nodes of "Man Overboard" and "Jamming" (Figure 6-7). The obtained results satisfy Axiom 2.

Figure 5. Probability changes of the "Hit by an Object" node
Figure 6. Probability changes of the "Man Overboard" node
Figure 7. Probability changes of the "Jamming" node

Axiom 3: The individual effects of parent nodes on child nodes are expected to be less than their combined effects (John et al., 2016). As an example, for Axiom 3, the "Unsafe Act" node is selected. The parent nodes of this node are "Non-conformity in Hunting Equipment", "Personal Protective Equipment", "Situational Awareness" and "Communication and Coordination". When the negative expressions of these parent nodes are made 100\% individually, the probability values for the "Yes" state of the "Unsafe Act" node are observed $51 \%, 47 \%, 53 \%$ and $50 \%$, respectively. When these four parent nodes' negative statements are made $100 \%$ together, it is found that the probability value for the "Yes" state of the "Unsafe

Act" node is 100\%. Axiom 3 test is applied to all child and parent nodes. The obtained results are in line with Axiom 3.

# 4.2.4. Sensitivity Analysis 

Sensitivity analysis can be used to identify the most critical nodes in the BN causing system failure. Sensitivity analysis allows researchers to observe the impact of each node on the result nodes (Dai et al., 2019, Wang et al., 2017). In this study, sensitivity analysis is applied for each level of the network. Thus, researchers can observe major vulnerabilities that play a role in the accident occurrence at each level with a view to recommending preventive solutions. In this study, there are 30 nodes in total, excluding the result nodes. The probability values of each node are set first $0(0 \%)$ and then $1(100 \%)$. Thus, the effect of each node on the result nodes is observed. The sensitivity analysis results are illustrated in Figures 8-11.

Figure 8. Sensitivity analysis results for a) "Man Overboard", b) "Hit by an Object", and c) "Jamming"

Figure 9. Sensitivity analysis results for "Pre-condition for Unsafe Acts"
Figure 10. Sensitivity analysis results for "Operational Conditions"
Figure 11. Sensitivity analysis results for "Unsafe Acts"

### 4.3. ARM Applications

### 4.3.1. Test Case for Association Rule Mining

In the ARM application, initially, itemsets consisting of one or more items are determined. Then, the frequency of occurrence of the determined itemsets in the dataset is calculated which is defined as the support count ( $\alpha$ ). The ratio of the support count ( $\alpha$ ) to the number of data (N) is determined as support (s). $N$ denotes the total number of data sets, which refer to a total of 173 unreported occupational accidents, used in the study (i.e., the total number

of rows within historical data). Confidence (c), on the other hand, is the ratio of the total number of $X U Y$ itemsets to the total number of data containing the set of $X$ itemset where $X$ is called as the antecedent and $Y$ is called as the consequent. To show the calculation process, a test case is conducted with a sample dataset series from the dataset used in this study. In the test case, "education level, vessel type, weather and sea condition" (antecedent variables $(X)$ ) and "accident type" (consequent variable $(Y)$ ) are selected. The values of these variables are shown in detail in Step 4 in the method section of the study. The sample dataset for the test case is shown in Table 6.

Table 6. Sample dataset for test case of ARM

Considering Equations (4), (5) and (6), association rules extracted using the Predictive Apriori algorithm can be exemplified as follows:

Sample rule 1:

$$
\begin{aligned}
& \text { support }=\frac{\alpha(\{\text { primary education }, \text { trawl, man overboard }\})}{(N)}=\frac{2}{7}=0.28 \\
& \text { confidence }=\frac{\alpha(\{\text { primary education }, \text { trawl, man overboard }\})}{\alpha(\{\text { primary education }, \text { trawl }\})}=\frac{2}{2}=1
\end{aligned}
$$

If \{education_level $=$ primary_education $\cap$ vessel_type $=$ trawl $\}=>$ class man_overboard (support $=0.28$, confidence $=1$, predictive accuracy $=0.91$ (Figure 1)).

Sample rule 2:

$$
\begin{aligned}
& \text { support }=\frac{\alpha(\{\text { good, jamming }\})}{(N)}=\frac{2}{7}=0.29 \\
& \text { confidence }=\frac{\alpha(\{\text { good, jamming }\})}{\alpha(\{\text { good }\})}=\frac{2}{4}=0.5
\end{aligned}
$$

If \{ weather_and_sea_condition $=$ good $\}=>$ class jamming (support $=0.29$, confidence $=$ 0.50 , predictive accuracy $=0.46$ (Figure 1$)$ ).

# 4.3.2. Application of ARM on Fishing Vessel Accidents Dataset 

In this study, two experiments are performed on the dataset set for ARM application. The first experiment revealed the rules considering man overboard, jamming and hit by an object. In the second experiment, the association rules for the accident consequence (injury, dead and disabled) together with the accident type are discovered. The Predictive Apriori algorithm is employed to extract the association rules regarding these consequent variables. Because of the unbalanced distribution of data, nine rules with the highest predictive accuracy level for each consequent variable are selected. The details of these two experiments are given below.

### 4.3.2.1. Association Rule Mining to Find Out Accident Type Conditions (The First Experiment)

In the first experiment, man overboard, jamming and hit by an object are determined as consequents. Six of the nine rules for the hit by an object class are attributed to the vessel length greater than or equal to 24 m and seine fishing vessels. The result indicates that accidents occurring on large seine type fishing vessels are likely to be due to hit by an object. On the other hand, the ARM results reveal weather and sea condition as a good indicator for accident type. More specifically, jamming and hit by an object are correlated with good weather and sea condition, while man overboard is attributed to bad weather and sea condition All rules based on the accident type created by the Predictive Apriori algorithm are shown in Table 7 in detail.

Table 7. Rule extraction for accident type using the Predictive Apriori algorithm

### 4.3.2.2. Association Rule Mining to Find Out Accident Consequence Conditions (The Second Experiment)

In the second experiment, injury, dead and disabled are determined as consequents. Predictive Apriori discovered the results for injury, dead and disabled especially for education level. It is revealed that accident risk increases as the education level decreases. Fishermen with at least high school education, for example, are less likely to experience an occupational accident due to man overboard and hit by an object accidents. On the other hand, according to the rules produced by Predictive Apriori, it should be noted that accidents experienced by fishermen with 10 years or more experience are likely to result in fatal accidents due to hit by an object. All rules based on the result created by the Predictive Apriori algorithm are shown in Table 8.

Table 8. Rule extraction for accident consequence using the Predictive Apriori algorithm

# 5. Result and Discussion 

Determining which combinations of factors cause an accident event is a complex problem, especially when it comes to human factors (Coraddu et. al., 2020). Innovative approaches or hybrid models for determining the human factors that contribute to maritime accidents are frequently used within the scope of accident analysis recently. These approaches help us understand the accident occurrences in detail and determine preventive measures to prevent the recurrence of these accidents (Babaleye et al.2020, Navas de Maya et al., 2020, Navas de Maya et al., 2021). Within the scope of maritime accident analysis, many analysis models such as Human Factors Analysis and Classification System (HFACS), BN, Fault Tree Analysis (FTA), Event Tree Analysis (ETA), Cognitive Reliability and Error Analysis Method (CREAM), Hazard \& Operability Analysis (HAZOP) have been used in a hybrid way to make in-depth analysis in the literature. Unlike the studies in the literature, BN and ARM methods were used in a way demonstrated in this study. The Bayesian network presented in this study

enables both qualitative and quantitative analysis of the factors that lead to the occurrence of occupational accidents on fishing vessels. The Predictive Apriori algorithm, on the other hand, determines the minimum conditions required for the occurrence of occupational accidents on fishing vessels. This study revealed that BN and ARM methods can be used within the scope of accident analysis. The important results of the study are given below.

The data used in this study shows that $71 \%$ of occupational accidents occurred on seine vessels and $29 \%$ on trawlers, which is not fairly supported by the literature. McGuinness et al. (2013b) and Lazakis et al. (2014) identified the trawler fleet has the highest occupational accidents rates of injury occurrence. The most common occupational accident category on Turkish fishing vessels is man overboard (Table 2). Domeh et al. (2021) also highlighted that man overboard is a major accident scenario for fishing vessels. Furthermore, Abraham (2001) stated that the rate of man overboard in all accidents has $27 \%$ in the USA, $27 \%$ in Norway, $30 \%$ in Denmark and 33\% in Iceland. In the report published by MAIB (2008), it was reported that $33 \%$ of the fishing vessel accidents that occurred in the UK were man overboard. The rate of man overboard for Turkey in this study was calculated as $38 \%$ (Table 2). $32 \%$ of the man overboard accidents observed in Turkish fishing vessels resulted in deaths, $65 \%$ in injuries, and $3 \%$ in being permanently disabled. When the BN sensitivity analysis results were analysed, the factors that play a role in man overboard were found as inappropriate operational environment, bad weather and sea conditions, unsafe acts and day state (night). These results show that operational conditions are a dominant factor in man overboard (Figure 8). Fishing gears, setting and hauling which is the most risky work conducted onboard in fishing vessels (McGuinness et al., 2013b), and the space they occupy on decks, lead to a tight working area (Fulmer and Buchholz, 2002). Failure to stack nets properly in this congested working area, leaving the ropes scattered, and slippery ground cause an inappropriate working area on fishing vessels. The BN and sensitivity analysis results established in the study support this argument (Figure 4 and

Figure 10). It was revealed that the most important factor that plays a role in the formation of an inappropriate working area is slippery ground. Fishing activities are usually carried out from the deck. Seawater, oil and sea creatures create a dangerous environment for fishermen working on the deck (ILO, 2014). Especially, wet nets and uncleaned sea creatures caught in the net's eyes pose a great risk in terms of falling into the sea. According to a study by Jensen et al. (2014) in the USA, $30 \%$ of the occupational accident that occurred on the fishing vessels resulted in man overboard and the reason for $33 \%$ of them is slippery surface. Wang et al. (2005) stated that $2.7 \%$ of fishing vessel accidents in the UK were caused by slippery surface. This rate is $12.14 \%$ in occupational accidents that occur in Turkish fishing vessels (slippery ground). Preventing accidents caused by slippery surface is possible with the installation of non-slippery deck surfaces and the use of protective equipment. The use of protective equipment can prevent the occurrence of occupational accidents on fishing vessel. It was stated as a common problem during the interviews with fishermen that the structure of the protective equipment is not designed for fishing activities. Many fishermen said that they are not able to perform fishing activities with protective equipment. Protective equipment designed for merchant ships is used on fishing vessels. In the report published by MAIB (2008), it was seen that in only one of the 65 man overboard accidents, the fisherman was wearing a lifejacket. In the study by Lang (2000), many fishermen emphasized that they are reluctant to wear the lifejacket due to impracticality and difficulty in working. Although much protective equipment has proven itself, a study conducted in Sweden notes that the personal protective equipment is not used in the $73 \%$ of occupational accidents on fishing vessels (Törner et al., 1995). Similar to the studies in the literature, the results of this study reveal that the protective equipment used on fishing vessels should be designed considering the nature and working environment of the fishing activities. Thus, the risk of accident or the impact of its consequences can be minimized.

The data used in this study also shows that $38 \%$ of occupational accidents occurred as a result of hit by an object, $38 \%$ man overboard and $24 \%$ by jamming. Considering all occupational accident categories, the death rate in the accidents is $27 \%$ and the rate of permanently disability is $9 \%$. These results of the study again reveal that the fishing activities are a dangerous occupation, as stated by the studies in the literature (Fulmer and Buchholz, 2002, Håvold, 2010). According to the results of the BN sensitivity analysis, the factors that play a role in the accident formation for hit by an object and jamming were found to be unsafe act, heavy weather and sea conditions and night. Although unsafe act is in three accident categories, it is more significant in hit by an object and jamming accidents (Figure 8). Preconditions playing a role in the occurrence of unsafe act are insufficient situational awareness, non-conformity in hunting equipment, non-ergonomics of personal protective equipment and lack of communication and coordination. (Figure 9). The most important reason for insufficient situational awareness was found as fatigue (Figure 11). Fatigue is one of the accident factors that cause human errors resulting from excessive workload and insomnia (Kurt et al., 2016, Navas de Maya et. al., 2018). In many recent studies, it has been revealed that there is a relationship between maritime accidents and fatigue (De Maya and Kurt, 2020, Fan et al. 2021). Along with the increasing operational demands on ships, the decrease in the number of crew triggers fatigue. Fatigue prevents a job from being carried out safely (Uğurlu et. al., 2021). Many fishing vessel crews have to carry out intense work throughout the season in order to generate income. This intense work tempo causes excessive workload and fatigue. Accidents are inevitable with the effect of fatigue caused by excessive workload and sleeplessness. This issue can be addressed by a quota application to all fishing vessels. A quota application can reduce competition in fishermen, as a result the excessive workload and fatigue caused by sleeplessness will be prevented. Other non-conformities that play a role in the formation of the unsafe act are presented in Figure 11.

BN sensitivity analysis results show that heavy weather and sea conditions are significant in man overboard (38\%) and jamming (26\%) accidents. Lucas and Lincoln (2007) found that $47 \%$ of man overboard accidents that occurred on fishing vessels in Alaska occurred in heavy weather and sea conditions. Fishermen can get information about weather and sea conditions in advance, with today's technology. Nowadays, heavy weather and sea conditions are no longer a fate for seafarers. However, ship owners may prefer to hunt by taking the risk of accident in fishing in such dangerous weather conditions. In the study by Woodley (2000), it is emphasized that the weaknesses in the rules and applications related to fisheries management cause this.

In this study, an ARM method (Predictive Apriori algorithm), which predicts accident type and accident consequences, was employed in order to better understand the cause-effect relationship between antecedent and dependent variables. The ARM application is based on the accident data created in the first step of this study. This database includes antecedent variables such as day status, weather and sea condition and experience (Tables 7 and 8). In this study, the Predictive Apriori algorithm determined the minimum conditions (rules) required for the occurrence of each occupational accident (Table 7). In addition, the Predictive Apriori algorithm created rules by considering results of the accidents as well as the accident category (Table 8). The first 2 rules with the highest accuracy revealed by the Predictive Apriori algorithm for fatal man overboard, hit by an object and jamming (occupational accident types) that occurred on fishing vessels are listed below (Other rules created by the algorithm are presented in Tables 7 and 8 in detail):

# Fatal man overboard accident: 

Rule 1: If \{education level $=$ primary education $\cap$ vessel type $=$ seine $\cap$ weather and sea conditions $=$ bad $\}=>$ class man overboard $($ fatal $)(98.18 \%)$.

Rule 2: If \{education level $=$ primary education $\cap$ vessel length $=\geq 24 \cap$ weather and sea conditions $=$ bad $\cap$ day status $=$ night $\cap$ sleeplessness $=$ no\} $=>$ class man overboard (fatal) $(96.47 \%)$.

# Fatal hit by an object accident: 

Rule 1: If $\{$ vessel type $=$ seine $\cap$ experience $=\geq 10 \cap$ weather and sea conditions $=$ good $\cap$ day status $=$ daylight $\cap$ sleeplessness $=$ yes $\} \Rightarrow$ class hit by an object (fatal) $(90.59 \%)$.

Rule 2: If \{education level $=$ primary education $\cap$ vessel type $=$ seine $\cap$ experience $=\geq 10 \cap$ weather and sea conditions $=$ bad $\cap$ day status $=$ night $\}=>$ class hit by an object (fatal) $(68.92 \%)$.

## Fatal jamming accident:

Rule 1: If $\{$ education level $=$ uneducated $\cap$ vessel type $=$ trawl $\cap$ experience $=10>\}=>$ class jamming (fatal) $(93.73 \%)$.

Rule 2: If \{education level $=$ uneducated $\cap$ vessel type $=$ trawl $\cap$ sleeplessness $=$ yes $\}=>$ class jamming (fatal) $(93.73 \%)$.

In many accident analyses studies on grounding and sinking of merchant ships, it is emphasized that the lack of education and bad weather conditions are the factors that cause accidents (Uğurlu et al., 2020b). The rules produced by ARM in this study show that there is a similar situation for fatal man overboard accidents on fishing vessels (Rule 1-2). Laasjord (2006) and Laursen et al. (2008) stated that hit by an object is one of the most important causes of deaths in fishing vessels and these accidents mostly occur in trawl vessels. However, in this study, it was revealed that hit by an object is the second most fatal accident type after man overboard accidents, and the accidents of this type were concentrated in seine vessels. In this study, as in studies by Törner et al. (1995), Antoa et al. (2008) and Kaustell et al. (2016), the ARM results determined that jamming accidents are one of the most common accident causes in trawl vessels.

# 6. Conclusion 

Fishing, which is carried out in an environment away from health and rescue services, is inherently difficult and dangerous. Even simple movements in rough seas are difficult and tiring. Fishermen are working between complicated fishing gears in a narrow and moving area in all weather conditions regardless of day and night. This causes the fishing activities to be considered a very dangerous occupation in many countries.

In this study, a hybrid model that can be used in the analysis of occupational accidents on fishing vessels is suggested. A network structure that enables the qualitative and quantitative analysis of occupational accidents on fishing vessels with the Bayesian network method has been put forward and, with the ARM method, on the other hand, the minimum conditions required for the occurrence of these accidents are determined. The BN presented in this study summarizes the occurrence of occupational accidents on fishing vessels. With the conditional probability approach used in the BN, it becomes possible to analyse active failures, latent factors and operational conditions that cause occupational accidents and to observe how these factors affect the occurrence of accidents. In addition, this network allows predicting the occurrence of an accident under changeable conditions. In other words, the network structure allows modelling and evaluation of fishing vessel accident scenarios. For example, changes in situational awareness can be observed in the event of fatigue (yes $=100 \%$ ) and alcohol use (yes $=100 \%$ ) for a fisherman. Thus, the impact of situational awareness on the occurrence of an accident can be estimated by considering the sea situation, day condition and working area.

In this study, ARM was also applied using the Predictive Apriori algorithm to analyse occupational accidents resulting in deaths, injuries and disability on fishing vessels. The application is based on the descriptive variables of the study (education level, vessel length, etc.). Many studies within the scope of accident analysis are conducted by considering the

causes of accidents. In this study, in addition to BN modelling, an analysis of occupational accidents in fishing vessels was carried out with ARM based on descriptive variables of the dataset. The algorithm creates accident occurrence rules by considering the influencing factors affecting accidents. These rules allow for understanding how occupational accidents occur on fishing vessels. Thus, necessary measures can be determined to prevent the occurrence of occupational accidents.
