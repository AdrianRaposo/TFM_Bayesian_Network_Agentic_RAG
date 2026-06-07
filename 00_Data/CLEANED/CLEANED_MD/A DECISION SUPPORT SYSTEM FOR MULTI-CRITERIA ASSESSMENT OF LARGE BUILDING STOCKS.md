# A DECISION SUPPORT SYSTEM FOR MULTI-CRITERIA ASSESSMENT OF LARGE BUILDING STOCKS 

Alessandro CARBONARI ${ }^{1^{*}}$, Alessandra CORNELI ${ }^{1}$, Giuseppe Martino DI GIUDA ${ }^{2}$, Luigi RIDOLFI ${ }^{1}$, Valentina VILLA ${ }^{3}$<br>${ }^{1}$ DICEA Department, Faculty of Engineering, Polytechnic University of Marche, Ancona, Italy<br>${ }^{2}$ ABC Department, Faculty of Engineering, Polytechnic of Milan, Milan, Italy<br>${ }^{3}$ DISEG Department, Faculty of Engineering, Polytechnic of Turin, Turin, Italy

Received 30 October 2018; accepted 12 March 2019


#### Abstract

Both public administrations and private owners of large building stocks need to work out plans for the management of their property, while having to deal with yearly budget limitations. Particularly for the former, this is a rather critical challenge, since public administrations are given the responsibility of sticking to very strict budget distributions over the years. As a consequence, when planning the actions to be taken on their building stocks in order to comply with their current use and the legislation in-force, they need to classify refurbishment priorities. The aim of this paper is to develop a first tool based on Bayesian Networks that offers an effective decision support service for owners even in case some information is incomplete. This tool can be used to evaluate the compliance of existing buildings with the latest standards. The decision support platform proposed includes a multi-criteria evaluation approach combining several performance indicators, each of which related to a specific regulatory area. This tool can be applied to existing buildings, where the building with the lowest score shows the highest priority of intervention. Also, the platform performs an assessment of expected costs for required refurbishment or renovation actions.


Keywords: BIM, decision support system, Bayesian Networks, multi-criteria analysis, decision making, Analytic Hierarchy Process.

## Introduction

Private and public institutions are often owners of large real estate assets. They are variously managed, depending on their peculiarities such as: use (e.g., residential, commercial, municipal), their age and their ownership (e.g., private ownership, public housing, public authorities) (Volk, Stengel, \& Schultmann, 2014). What makes the situation even more challenging is that these assets are often distributed throughout large territories, so the capabilities of technical staff may vary and a uniform approach for surveying and describing assets is seldom applied. Rather, public administrations need to perform an assessment of the existing stock over time, possibly based on shared and objectively defined criteria. For this reason, in this paper a tool that is applicable to existing buildings and that helps owners manage even large building stocks while making conscious choices even in the presence of different peculiarities.

The main regulatory requirements that must be accounted for by public administrations are included in the
system architecture (i.e., accessibility, energy and acoustic performances, fire prevention). Since these criteria are measured on different scales and often have heterogeneous nature, they cannot be directly compared. For this reason, a method that weighs the different characteristics leading to an overall and comprehensive assessment needs to be implemented.

The adoption of the approach proposed in this paper would help overcome the limitations posed by paper-based information, which is typical of traditional processes involving big archives of documentation in scattered locations. When dealing with existing buildings, documentation might be missing or incomplete and its retrieval often involves a significant effort in terms of additional time and costs. In fact, the assessment of existing buildings normally involves a greater degree of uncertainty than in the case of new buildings. This is mainly due to limited access to places, practical and economic limitations related to onsite verifications and tests and the limited availability of

[^0]
[^0]:    *Corresponding author. E-mail: alessandro.carbonari@univpm.it

design and as-built drawings and material specifications. These issues often lead the surveyor to make assumptions about some missing evidence (e.g., materials, layers of components).

Building Information Modelling (BIM) integrated with a Decision Support System (DSS) may constitute a powerful methodology to support the selection of actions for strategic management. More specifically, BIM models are meant to store information. Bayesian Networks must perform inference for decision making and manage uncertain information.

However, BIM-based processes were originally developed to support the design of new buildings and are seldom applied to the management of maintenance and refurbishment operations of existing buildings. The scarce implementation of BIM in this field is mainly due to the great modelling effort required to transfer information from paper documents or CAD data into BIM models; this process often asks managers for handling uncertain or missing information (Volk et al., 2014).

Due to the reasons stated above, in this paper a tool that offers owners an effective decision support system under conditions of uncertainty is proposed. In particular, Building Information Modelling and Bayesian Networks have been integrated. Also, some remarks about what data are necessary to be extracted from the respective BIM models in order to be transferred as inputs into the Bayesian Networks are presented. Each Bayesian Network (BN) is used to evaluate all the requirements considered in the several regulatory areas. In addition, this approach is easily scalable, so it can be applied to any building. Once the BN for each regulatory area has been created, it is possible to re-use these networks for each building under analysis, inserting required information and performing inferences, which updates output variables within very limited computational time. In Section 4, the implementation of the DSS is shown relatively to two school buildings located in the municipality of Melzo (Milan, Italy).

For each of the regulatory area mentioned above, indicators are worked out by Bayesian Networks to verify the compliance with the latest legislation. Furthermore, a multi-criteria evaluation tool, based on the Analytic Hierarchy Process (AHP) approach, is included in the decision support system. Its task is to define a final ranking of the facilities and to identify the building having the lowest score, hence the highest priority of intervention. Finally, a "cost BN" for the estimation of renovation costs is created, in order to help size the necessary budget expected for carrying out renovation or refurbishment works. More details about the methodology are provided in Section 2, while Section 1 provides relevant background. Section 3 outlines the test cases and the development of the DSS for "accessibility", "energy efficiency", "acoustics" and "cost estimation" regulatory areas. The results are discussed in Section 4.

## 1. Literature review

In most cases, when evaluating the compliance of a building with the latest standards, several indicators must be assessed. Furthermore, making decisions for the management of any large building stock requires the integration of various information which, however, is sometimes incomplete or unknown, due to missing or incomplete building documentation.

Approaches for the handling of a wide variety of information with decision making systems have been carried out in several studies for a wide variety of engineeringrelated issues in the construction industry. A few examples of research initiatives regarding this topic are provided in the following. A model to predict the energy performance of the existing residential building stock at a urban scale was presented by Braulio-Gonzalo, Juan, Bovea, and Ruá (2016). The approach included the development of an assessment method which considered five parameters affecting energy efficiency, such as the year of construction, the building shape, the orientation of the building's main façade, the street height-width ratio and urban block pattern. The dataset for this study was obtained by modelling the energy performance of some sample buildings with EnergyPlus simulation software. The results obtained from the simulations were then used as input data to develop prediction models using Bayesian inference. The final model was deemed a useful decision-making tool to make the identification of those urban areas that require more urgent interventions and energy refurbishment easier for local authorities, architects, urban planners and developers. Another paper moved from the assumption that many energy conservation measures can help reduce the energy consumption of buildings, although some measures can be far more effective than others. Since building owners wish to know what measures will yield the highest return on investment and how reliable the different measures are, a methodology based on Bayesian statistics was developed to evaluate the effectiveness of energy conservation measures on existing buildings applied to a case study of a commercial building in Sargans (Switzerland) (Lindelöf, Alisafaee, Borsò, Grigis, Mocellin, \& Viaene, 2017).

A DSS can be also used to make decisions at an early design development stage, helping designers identify multiple technical and commercial options compliant with pre-determined specifications and that can be presented to clients in real time. This is the case of Kassem, Dawood, and Mitchell (2012), in which a DSS was applied to the selection of a curtain wall system at the design development stage.

A challenging aspect that is very often encountered with existing buildings is having to make decisions in the situation of uncertain or incomplete information on the current status of the buildings. For example, in the research carried out by Kundu, Eaton, Al-Jumali, Sikdar,

and Pullin (2017), the presence of a significant amount of uncertainty associated with the operational conditions and measurements, made the problem of damage identification quite hard. In this case, uncertainties were generated by the fact that the signals measured were affected by irregular geometries, imperfect boundary conditions, existing damages. Even in applications regarding thermal comfort, field studies have showed that not all occupants of a same building wish to stay in the same thermal conditions, hence there is no metrics that can accurately predict the thermal preferences of each occupant. In order to tackle this issue, a Bayesian modelling approach to learn the thermal preferences of individual occupants even in those cases in which the model structure is complex and the amount of data collected from each occupant is relatively limited was presented by Lee, Bilionis, Karava, and Tzempelikos (2017). Moreover, an approach for considering the incomplete knowledge about material properties in the assessment of existing masonry buildings based on a Bayesian framework was presented by Bracchi, Rota, Magenes, and Penna (2016). The use of a Bayesian approach makes it possible to update the values of the building material properties assumed as prior knowledge by taking into account all the experimental information gathered during the assessment process. However, in many decision problems the evaluation of alternatives is complicated by a limited knowledge of relevant attributes or current performances.

In what seems to be a recurring theme, the Bayesian approach is becoming increasingly popular because of its ability to perform inference even in the presence of uncertainty. Although several techniques have been tested to quantify uncertainty, Bayesian methods are notable for their support in almost all related fields, from general metrology to decision support (Carstens, Xia, \& Yadavalli, 2018).

The implementation of Decision Support Systems in building performance assessment and control is becoming more and more important and various methods have been trialed and used to support multi-criteria decisionmaking.

For example, multi-criteria decision models have been developed with the aim of presenting a framework enabling any decision maker to select the best performing alternative in terms of energy consumption, installation costs and other relevant criteria (Rasiulis, Ustinovichius, Vilutiené, \& Popov, 2016). The final purpose is allowing stakeholders to rank the different criteria according to their importance and in relation to the decision problem and to various alternative options (Hopfe, Augenbroe, \& Hensen, 2013). In fact, a ranking method was shown to rate, qualify and sort various scenarios (Roulet et al., 2002) through a methodology called ORME (Office building Rating Methodology for Europe), which was proposed to rate office buildings and select among retrofit scenarios. A typical application of this methodology is to determine whether, for a given building, a retrofit scenario is on the
overall better than others, in circumstances in which it is hard to decide to what extent any strategy may improve the building's performance; with this methodology, all the possible scenarios can be included in the ranking, according to several criteria which use decision support tools.

Another critical task for public administrations can be the determination of the necessary costs for refurbishment actions, since owners usually have to deal with limited budgets. The study developed by Lai, W.-C. Wang, and H.H. Wang (2008) identified an appropriate list of evaluation criteria and proposed a procedure to estimate the budgets for public building construction projects. In this case, the Analytic Hierarchy Process (AHP) approach was used to weight the several assessment criteria. Another study was developed to provide systematic means for priority setting of maintenance activities in various hospital buildings as well as a comprehensive Key Performance Indicator for building performance evaluation (Shohet, 2003). A further application of AHP was presented by Sasmal, Ramanjaneyulu, and Lakshmanan (2007). This study dealt with the problem of prioritizing existing old bridges in need for some kind of refurbishment. Reinforced concrete bridges deteriorate with time, due to fatigue, environmental effects and possible overloading, and authorities have the responsibility to maintain their bridges in a safe status. Hence, the paper presented a systematic methodology for priority ranking towards condition assessment of existing bridges using AHP.

The authors stressed that this method would help decision makers in determining a ranking of those bridges mostly in need for repair, resulting in the reduction in the number of catastrophic failures and in better use of public money.

The aforementioned research papers report relevant research in the field of DSS, but they do not deal with the integration between decision support systems and BIM models. Indeed, information related to existing buildings cannot be complete unless an accurate field inspection is undertaken, which requires a big effort. Hence, the updating of information and the handling of uncertain data, objects and relations in BIM are typical challenges related to building stock management. In addition, these studies do not deal with composite models made of several probabilistic networks. In the case presented in our paper, the platform is able to assess the level of compliance with the latest legislation for each regulatory area, starting from inputs integrated as attributes and properties in BIM models. After ranking and comparing the buildings, the one that is mostly in need for renovation is identified. An additional BN estimates costs necessary to perform these specific actions.

The platform is targeted to those organisations, especially in the public sector, which own a large variety of buildings and facilities and have to manage their maintenance, renovation, reconstruction (Rosenfeld \& Shohet, 1999). The prioritization of refurbishment actions is based on selected performance indicators which are weighted

through a multi-criteria assessment method. Multi Criteria Decision Making (MCDM) approaches help decision makers make decisions according to their preferences in those cases in which there is more than one conflicting criterion to be taken into account (Løken, 2007). Following a survey throughout scientific literature, it was found that the majority of the methods used are based on the AHP, ELECTRE and PROMOTHEE approaches, among which the AHP method clearly stands out in terms of usage, thanks to its simplicity of application and flexibility and ability to provide decision makers with a robust solution (Sabaei, Erkoyuncu, \& Roy, 2015). Therefore, this method has been applied in this paper to rank alternatives and assist the decision maker, according to the theory suggested by Saaty (1990).

## 2. Methodology

### 2.1. Overview

The DSS (Figure 1) is conceived for the verification of multiple regulatory areas, including accessibility, energy efficiency, and acoustics. By means of a dedicated interface between the BIM database and Bayesian Networks, data about the domain can be automatically extracted
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic diagram of the structure of the Decision Support System
from the BIM database (e.g., BIM model or IFC file) into the Bayesian Networks, evaluating the compliance of the building. In addition, the platform includes a multicriteria evaluation of performance indicators, each relating to a specific regulatory framework, carried out with the AHP approach. The output is the assessment of a final ranking of the buildings subjected to evaluation, in which the one with the lowest score shows the highest priority of intervention. In addition, Bayesian Networks dedicated to the estimation of costs for refurbishing of the building have been developed. The platform can even allow the user to add information such as the limit of the budget to be allocated.

In the application presented in this paper as proof of concepts, the first three areas of interest, i.e. Accessibility, Energy Efficiency, Acoustics, were analyzed and associated to the corresponding Bayesian models.

### 2.2. Bayesian Networks

Bayesian Networks are a computational tool for the development of qualitative probabilistic models. They are oriented graphs whose nodes represent random variables that are linked by arcs which correspond to casual relationships among previous nodes.

Bayesian Networks make use of probability theory and graph theory to make decisions in conditions of uncertainty. The potential of the BN instrument lies in its dual structure. The first one is a set of nodes representing system variables. Each variable may be given two or more possible states which can be of numerical (i.e. discrete), interval (i.e. subdivision into ranges), label or Boolean type. The second one is a set of links representing the casual relationships between nodes. An arc from any set of $n$ variables, called $a_{i}$, to another variable $b$ denotes that the set $a_{i}$ causes $b$ and $a_{i}$ are said to be the parents of $b$ ( $b$ is their child). The graphical part illustrates and communicates the interactions among the set of variables through a Directed Acyclic Graph (DAG). Furthermore, Bayesian Networks represent the quantitative strength of the connections between variables, allowing probabilistic beliefs to be updated automatically as new information becomes available, by applying the principles of the Bayes' theorem (Catenacci \& Giupponi, 2009).

The strength of these relationships is quantified by conditional probability tables (CPTs), where the probability of observing any state of the child variable is given with respect to all the combinations of its parents' states. These probabilities are usually labelled $P\left(b \mid a_{1}, a_{2}, \ldots, a_{n}\right)$, where any variable $a_{i}$ is conditionally independent of any variable of the domain that is not its parent. Thus, it is possible to obtain a conditional probability distribution over every domain, where the state of each variable can be determined by the knowledge of the state of its parents only, and the joint probability of a set of variables E can be computed by applying the "chain rule" (Pearl, 1998):

$$
P(E)=P\left(E_{1}, E_{2}, \ldots, E_{n}\right)=P\left(E_{n} \mid \operatorname{parents}\left(E_{n}\right)\right)
$$

The joint probability of a set $E_{n}$ of variables is equal to the conditional probability of the variable, given only its parents. Other relevant benefits are: the DAG provides a clear understanding of the qualitative relationships among variables; every node can be conditioned upon the acquisition of new information (e.g. in the case study presented, evidence about the features of a building); belief updating of nodes is supported from consequences to causes, also known as diagnostic reasoning, and can be applied when the budget for renovation is limited and inference must be conducted from child nodes (e.g., cost of renovation) back to parent nodes (e.g., status of a building sub-system). Finally, CPTs can describe the relationships among variables of different types (e.g., Boolean nodes, interval node, etc.), even within the same network.

Often, the only data available to train a probabilistic model are incomplete, because some variables can be difficult or even impossible to be observed. Therefore, it is important that a learning algorithm knows how to make an efficient use of the data observed. One of the most efficient algorithms for learning parameters is the EM (Ex-pectation-Maximisation) algorithm, which is used in the presence of missing values and which, through equations of the Expectation step (Eqn (2)) and the Maximisation step (Eqn (3)), estimates unknown parameters using the set of observed data. The EM algorithm is an approximation algorithm that can find a local maximum of a probability $p(\cdot \mid \Theta, \xi)$ as a function of parameters $\Theta$. For example, given a database $\mathrm{D}=\left\{C_{1}, \ldots, C_{m}\right\}$ with missing data, we can use the EM algorithm to find a local maximum for $p\left(D \mid B^{h}{ }_{i}, \Theta_{B i}, \xi\right)$. To illustrate the method, let us suppose we wish to find a local maximum for $p\left(D \mid B^{h}{ }_{i}, \Theta_{B i}, \xi\right)$. We begin by assigning values to $\Theta_{B i}$ somehow. Next, rather than sample a complete database $D^{\prime}$, we compute the expected sufficient statistics for the missing entries in the database. In particular, we compute:

$$
E\left(N_{i j k} \mid \Theta_{B i}, \xi\right)=\sum_{i=i}^{m} P\left(x_{i}=k, \Pi_{i}=j \mid C_{l}, \Theta_{B i}, \xi\right)
$$

When $x_{i}$ and all the variables $\Pi_{i}$ are observed in case $C_{l}$, the term for this case requires no computation: it is either zero or one. Otherwise, we can use any Bayesian Network inference algorithm to evaluate the term. This computation is called the expectation step of the EM algorithm.

Next, rather than sample new values for $\Theta_{B i}$, we use the expected sufficient statistics as if they were actual sufficient statistics from a database $D^{\prime}$, and set the new values of $\Theta_{B i}$ to be those that maximize $p\left(D^{\prime} \mid B_{h i}, \Theta_{B i}, \xi\right)$. Namely, we set:

$$
\Theta_{i j k}=\frac{E\left(N_{i j k} \mid \Theta_{B i}, \xi\right)}{E\left(N_{i j} \mid \Theta_{B i}, \xi\right)}
$$

This assignment is called the maximization step of the EM algorithm (Fayyad, Piatetsky-Shapiro, Smyth, \& Uthurusamy, 1996).

BNs are a useful tool because they make it possible to combine prior knowledge with new data, where different types of variables and knowledge from various sources need to be integrated within a single framework. Once a model is compiled, a software program (e.g., Hugin Researcher ${ }^{\mathrm{TM}}$ ) can implement inferences throughout the networks within very limited computational time by using the already established conditional probability distribution tables (Jaitha, 2017).

The variables that are the objects of inference are defined as output variables, while the variables whose information must be provided in advance to perform inference are known as input variables. Bayesian Networks are not limited to predicting a single output. They can simultaneously predict multiple outputs. In addition, Bayesian Networks have become among the most used tools for reasoning under conditions of uncertainty (Kofod-Petersen, Langseth, \& Aamodt, 2010).

### 2.3. Multi-criteria ranking

As shown in Figure 1, the last step of the methodology consists in the multi-criteria analysis. The Multi criteria approach takes into account the subjectivity of preferences by giving the opportunity to choose some criteria instead of others, hence it can be customised to the owners' specific needs. There are different Multi-Criteria Analysis methodologies, which can be divided into two main groups: i) Multi-Criteria Objectives Analysis (MCOA) and ii) Multi Criteria Attributes Analysis (MCAA). In the case of MCOA, the decisional process consists in the selection of the best solution within a group of infinite alternatives implicitly defined by the problem boundaries. On the contrary, MCAA is a multidimensional evaluation method subset, whose final purpose is to locate the best strategy among a restricted number of alternatives, which are ranked according to their preferences (Bourdic, Salat, \& Nowacki, 2012). MCAA can act as a support in the decision-making process (Douglas Balcomb \& Curtner, 2000), leading through a systematic analysis of the solutions.

For the reasons stated in the previous section, the AHP methodology was applied in this study. In order to make decisions in an organized way and generate priorities, any decision process must be decomposed into the following steps (Saaty, 2008):

- definition of the problem and the needed inputs;
- structuring of the decision hierarchy from the top with the "decision and objectives" goal giving a broad perspective, through the intermediate levels (criteria on which subsequent elements depend) down to the lowest levels (which is usually a set of alternatives);
- construction of a set of pairwise comparison matrices; each element in any upper level is used to compare the elements in its level immediately below;
- use of the priorities obtained from the comparisons to weigh the priorities in the level immediately below.

This is done for every element. Then, for each element in the lowest level, its weighted value is added and the overall or global priority is obtained. This weighting and adding process must be iterated until the final priorities of the alternatives in the bottom level are obtained.
In order to perform comparisons, it is necessary to define a scale of numbers that indicates how much more important or dominant one element is over other elements, with respect to the criterion or property chosen for the evaluation.

In the application presented in this paper, the hierarchy is defined as the first step: the top level is "stock value", the second level is composed of all the areas of interest such as accessibility, energy efficiency, acoustics; the third level is made up of the outputs from the BN "Level of Compliance" (LoC) node for Accessibility, "EPI" and "Heat Transfer Coefficient" nodes for Energy Efficiency and "Level of Compliance" (LoC) and "Compliance of acoustic requirements", as reported in Section 4. The second step consists in the pairwise comparison between the values obtained from the BN and the weights determined by means of the pairwise comparison (Corneli, Meschini, Villa, Di Giuda, \& Carbonari, 2017).

## 3. Development of the decision support system

### 3.1. The case studies

In this paper, two school buildings located in Melzo (Milan, Italy) were chosen as a proof of concept (Figure 2). Thanks to the collaboration between the Polytechnic of Milan and the Municipality of Melzo, two BIM models were developed in Autodesk Revit ${ }^{\mathrm{TM}}$ environment. Inputs were acquired from dedicated surveys and on-site tests. The first one is "Ungaretti" primary school, whose surface area measures $4528 \mathrm{~m}^{2}$ and is arranged on four levels, one of which is the basement while the remaining three floors are placed above ground. The gymnasium is situated in a separate building, which communicates with the main building through two horizontal connections in the basement and one connection placed on the ground floor. The basement houses the canteen, the kitchen, laboratories, archives, refreshment areas and infirmary. On the ground floor there are classrooms and offices, on the first floor there are classrooms only while on the second-floor there are classrooms and the auditorium. Restrooms are located throughout the building and near the gym.

The second case study is "Mascagni" secondary school in Melzo. The school has a surface area of $5736 \mathrm{~m}^{2}$ and is composed of three functional blocks. One block holds classrooms and laboratories, which are located over two floors above ground, the other two blocks hold the cafeteria/auditorium and the gymnasium.

Table 7 in Section 4 reports the necessary information (available in the model, not available but derivable from the BIM models and obtained after post-processing) for the accessibility network, energy efficiency network and
![img-1.jpeg](img-1.jpeg)

Figure 2. BIM models of the case studies: a - Ungaretti school; b - Mascagni school
acoustics network. In addition, it shows how most of the inputs can be directly derived from the BIM models, either through an interface which automatically picks out relevant inputs from the BIM models and transfer them to the related BN or through a manual approach.

### 3.2. Development of the Bayesian Networks

In this section, the BNs in charge of performance and cost estimations are described: the Accessibility BN, the Energy Efficiency BN, the Acoustics BN and the Cost estimation BN.

### 3.2.1. Accessibility Bayesian Network

Italian legislation (i.e. Italian Decree D.M. no. 236/89 (Ministero delle infrastrutture e dei Trasporti, 1989)) was taken as a reference to define all the requirements and the related technical standards that are assessed using the Accessibility Bayesian Network (Figure 3). The output node "Level of Compliance" is a child node of several parent nodes, each concerning a specific sub-area, and represents the percentage of sub-areas the building is compliant with, related to the total number of sub-areas (Architectural Barriers Act (ABA) Standards, 2015):

- "Accesses": e.g. width, handle height, maximum opening force;
- "Doors": e.g. width, handle height, maximum opening force, manoeuvring clearance;
- "Parking spaces": e.g. parking space width;
- "Lift": e.g. car elevator dimensions, car control keypad height;
- "Floors": e.g. floor frictional coefficient, floor joint width, floor ridges, changes in level;

![img-2.jpeg](img-2.jpeg)

Figure 3. Accessibility Bayesian Network

- "Stairways and Ramps": e.g. handrails, tread and riser size, stair width, maximum slope;
- "Restrooms": e.g. water closet position, grab bar location and size, lavatory position;
- "Routes": e.g. clear width of an accessible route, passing space interval;
- "Windows and balconies": e.g. railings, manoeuvring clearance, window opening force, handle height;
- "Facilities outlets": e.g. facilities outlet height.

According to reference legislation, the compliance of any "Route Width" in a school is conditionally dependent on the states of the nodes "Route Type" and "Clear Width". The variables "Route Type" and "Clear width" are marginally independent. In Figure 4, two examples of instanti-
a)
![img-3.jpeg](img-3.jpeg)

Figure 4. Fragment of instantiated Accessibility BN: a - true state in "Route width" node; b - false state in "Route width" node
ated network are shown, from which it can be noticed that the dependent variable can only be "true" or "false", depending on the compliance with legislation. Its state is conditionally dependent on the evidences collected by its parent nodes (e.g. if "Route Type" is set as Internal and "Clear Width" is set as 100 -inf, the result is that in this case "Route width" complies with the legislation).

In turn, the final check on "Routes" is conditionally dependent on "Passing Space Interval" and "Route width" (Figure 5). The Boolean "Routes" node can be either "true" or "false", and depends on "Passing Space Interval", which means it is compliant only if an accessible route has enlargements at the ends of the corridors or every 10 meters of linear development of the same to allow people on wheelchairs to reverse.
a)
![img-4.jpeg](img-4.jpeg)

Figure 5. Fragment of instantiated Accessibility BN: a - true state in "Routes" node;
b - false state in "Routes" node

In conclusion, the Conditional Probability Tables (CPTs) learned in this BN are meant to check whether every requirement determined by the legislation in force is successfully verified. The combination of states provides the final value of every node referred to all the requirements (violet nodes in Figure 3). Finally, the "Level of compliance" node (yellow nodes in Figure 3) gives the ratio of requirements that are successfully verified.

### 3.2.2. Energy Efficiency Bayesian Network

According to Italian legislation, two of the most important indicators of the energy behavior of building facilities are: the average heat transmittance due to the building envelope and the average energy consumption during the heating season. As a result, the Energy Efficiency BN (Figure 6) was used to estimate two performance indicators:

- heat Transfer Coefficient (HTC), i.e. global average heat transfer coefficient of building envelope;
- seasonal Energy Performance (SEPi), i.e. energy performance index for winter air conditioning. This indicator depends on the gross volume heated and on heating energy needs. In fact, legislation refers to the global performance index (EPgl) obtained as the sum of the energy performance indices for winter and summer air conditioning, production of Domestic Hot Water, transport service of people or things, ventilation and artificial lighting. Since the model was made only for the calculation of heating consumption, the coefficient of Seasonal Energy Performance index has been defined, because it is referred to the winter season only.
Both the qualitative and the quantitative structures of the Energy Efficiency BN were worked out from previous experience on energy performance simulations. A useful resource for obtaining variable values to be introduced in
the Energy Efficiency Bayesian Network was the dynamic simulation of reduced-order models. Reduced-order models are models with a reduced number of parameters estimated starting from limited information, but which can still guarantee a physical interpretation of results and an effective assessment of the energy behaviour of the building in short time and using few resources. As the number of parameters that characterise the models is limited, conditional dependencies between variables can be seamlessly read and turned into the formalism of BNs.

In particular, previous research projects were carried out referring to RC-network reduced models to model the heat dynamics derived from the analogy with electric circuits (Benedettelli, Carbonari, Naticchia, \& Vaccarini, 2016). According to this type of models, the thermal mass of the building is lumped to a discrete number of parameters in which the resistances and the electrical capacities represent the thermal resistances and capacities; the external temperatures are represented as voltage generators and thermal contribution like current generators. As a result, the BN structure depicted in Figure 6 was worked out from the qualitative analysis.

The high affordability of those models was shown by means of a validation against measured consumption based on the NMBE (Normalised Mean Bias Error) and CV-RMSE (Coefficient of Variation of the Root Mean Squared Error) indicators (Giretti, Lemma, Casals, Macarulla, Fuertes, \& Jones, 2017).

Therefore, using these models it was possible to quickly generate a set of energy simulation results that could include enough information about the thermal behaviour of the two schools. Simulations were carried out using the Dymola Software. Dymola is a software that makes it possible to simulate dynamic behaviour and complex
![img-5.jpeg](img-5.jpeg)

Figure 6. Energy efficiency Bayesian Network

interactions among systems related to many engineering fields: mechanics, electrical engineering, thermodynamics, hydraulics, thermal and control systems. Dymola makes it possible to perform modelling and simulation of lumped parameter systems, validate control system on integrated models of the real thermal plant and to create new libraries or to modify existing ones to get better modelling thanks to the Modelica open source language.

In order to set up the simulation dataset, the range of input and output nodes was estimated according to the technology variability that is proper of the building types' subject of this study. A number of simulations high enough to generate a significant dataset of all the possible combinations of input parameters of the reduced-model was then defined.

To learn the CPTs of the BN from the data collected, the results of the reduced-order model simulations were sorted out into a database containing the following variables: Irradiation_w (radiation transmitted through the transparent envelope), Irradiation_op (radiation transmission through the opaque envelope), Conduction (conduction heat flow through the opaque envelope), System (contribution of the winter/summer air conditioning system), Gains_tot (thermal contribution from user and equipment). These datasets were used to learn the CPTs of the fragments: Internal Gains, Transparent Heat Transfer, Opaque Heat Transfer and Heating Energy needs. The CPTs of the Energy Efficiency BN were learned through the EM-learning tool implemented in the Hugin ${ }^{\mathrm{TM}}$ software program (Fayyad et al., 1996). The other fragments of the Energy Efficiency BN were extrapolated from the BIM models and through calculations implemented in a spreadsheet. One of them is the average transmittance of the transparent and opaque elements. In this case the transmittance of each transparent and opaque element was read in the BIM models and the average transmittance was then computed by means of a spreadsheet. In addition, several nodes which define the relationship between input
nodes and output nodes, such as the heating energy needs Q_h and the global heat transfer coefficient Ht_adj, were identified directly in the network by means of a tool available in Hugin software which generates CPTs through the simulation of scenarios from mathematical relationships.

In order to validate the Energy Efficiency Bayesian Network, a comparison between the results provided by the network and the results provided by a commercial software tool was worked out for both the schools, Ungaretti and Mascagni. The evaluation of the Energy Performance Index for the heating season (EPI ${ }_{\text {winter }}$ ) was performed using the Revit "Edilclima" plug-in, from which, once the gross volume of the two buildings was known, it was possible to derive the annual consumption, that is, the data calculated by the reduced model in order to have a quick feedback on the results obtained. As shown in Figure 7, the network estimated a value that is in accordance with the result expected. The most likely interval estimated by the network is between $45-47 \mathrm{kWh} /$ $\mathrm{m}^{3}$ year (that is $29.37 \%$ ), which is very close to the result obtained from the software calculation, that is, for "Ungaretti" school, EPI equal to $47.86 \mathrm{kWh} / \mathrm{m}^{3}$ year, hence the deviation between the average value inferred by the BN and the software is within $3.2 \%$. Similarly, the validation performed in the case of the "Mascagni" school too gave back good results (Table 1).

### 3.2.3. Acoustics Bayesian Network

In order to evaluate the acoustic conditions of the buildings, the acoustic performance level was analysed.

In this specific area, indicators were identified to verify at which level the required requisites were satisfied.

New and existing buildings need to be characterised by specific noise insulation performance. The legislation (DPCM-December 5, 1997 - "Determination of passive acoustic requirements of buildings" (Il presidente del consiglio dei ministri, 1997) and DM-January 11, 2017 "Adopting minimum environmental criteria for interior,
![img-6.jpeg](img-6.jpeg)

Figure 7. Probability distribution referred to EPI node
Table 1. Comparison between the results deriving from the BN and those from Edilclima plug-in


building and textiles product" (Ministero dell'ambiente e della tutela del territorio e del mare, 2017)) defines all the requirements and concerns:

- insulation from airborne noises between different real estate units;
- insulation from external noise (façade insulation);
- insulation from trampling noise;
- insulation from the noise produced by the systems;
- acoustic insulation of internal walls;
- reverberation time of classrooms and gyms.

For each type of noise, the DPCM indicates:

- the indicators to be used (respectively to the aforementioned requirements: $R^{\prime}{ }_{w}, D_{2 m, n T w}, L^{\prime}{ }_{n w}, L_{A S \max }$, $\left.D_{n t, w}, T_{60}\right)$;
- the threshold values to be met depending on the intended use of the building (Table 2).
Subsequently, all the aspects that can be assessed for the formalization of the verification network were taken into consideration. The Acoustics BN (Figure 8) has been divided into two sub-networks, the first one reflecting the Sabine equation for the calculation of reverberation time and has been, therefore, of an analytical nature; while the second one has been used for the control of the remaining parameters.

The learning phase of CPTs was performed according to different approaches (e.g. literature survey, mathematical relationship) for the several fragments of the network (Frulla, 2017). In this case, the structure of the network reflected the structure of the analytical equations used for the calculation of the various indicators.

In fact, for variables dependent on mathematical relationships (e.g. Lic, Lid, STI, $L^{\prime}{ }_{n w}, D_{n t w}, T_{60}$ ), the related equations were used in the network to obtain the output results (violet nodes in Figure 8), in order to verify the level of compliance (yellow node in Figure 8). The input variables the equations and the final results depend on are mainly the characteristics of the components of the buildings (e.g. wall type, wall thickness, floor type, floor thickness). For example, the fragments regarding the airborne sound insulation index of internal wall $D_{n t, w}$ were estimated using the following equation:

$$
\begin{aligned}
& D_{n T}=R^{\prime}+10 \log \left(\frac{T_{2} \cdot 0,16 \cdot V_{2}}{0,5 \cdot S \cdot T_{2}}\right)= \\
& R^{\prime}+10 \log \left(0,32 \cdot \frac{V_{2}}{S}\right)=R^{\prime}+\Delta
\end{aligned}
$$

Table 2. Acoustic threshold values


![img-7.jpeg](img-7.jpeg)

Figure 8. Acoustics Bayesian Network

Rooms with standard size showed variations between $\pm 3.8 \mathrm{~dB}$. For the acoustic quality control, the Speech Transmission Index STI, represented by the Signal/Noise ratio, was verified. The correlation used to create the network that relates the perception of individuals with the respective STI values is shown in Table 3.

Table 3. STI values


On the other hand, for the variables dependent on on-site measurements (e.g. $R_{w}$ and $L_{n w e q}$ to calculate $R^{\prime}{ }_{w}$ and $L^{\prime}{ }_{n w}$, respectively), the stratigraphy tables present in literature were used (Magrini, 2005). In addition, for the calculation of $L^{\prime}{ }_{n w}$ (Eqn (5)), the interval node $L_{n, w}$, which is associated to an expression equal to the difference between the trampling noise of the rough floor slab and the contribution due to the finishing layer, was introduced. While the former contribution was identified from literature, the latter was obtained from data sheets of building materials manufacturers.

$$
L_{n, w}^{\prime}=L_{n w, e q}-\Delta L_{w}+K
$$

Once the results for the indicators of the Acoustic BN were obtained, a validation was accomplished per each index referring to the Ungaretti school so as to compare the results of the network with those obtained from the acoustic simulation. In order to validate the network, an acoustic analysis of the building was carried out. The evaluation of the various acoustic indicators was performed using SuoNus tool.

The comparison between the results, are shown in Table 4, referring, by way of example, to Room no. 39. In addition, to evaluate the compliance with the legislation, the threshold values in Table 2 have been considered.

### 3.2.4. Cost estimation Bayesian Network

This section focuses on the development of a methodology for the creation of Bayesian Networks dedicated to the estimation of costs for building refurbishments. The input data that can be used for the network were collected from the BIM database. Therefore, in addition to ranking, to determine the priority of intervention, additional
information was obtained, such as the range of the budget to be allocated to intervene on the most critical buildings and the preliminary knowledge of the intervention to be carried out. Public administrations often rely on a limited budget and they must be able to predict future costs. Therefore, this network helps managers assess all the possible intervention scenarios from an economic point of view. The first challenge that led to the development of the Bayesian Network was the creation of a dataset wide enough to include all the relevant scenarios.

Therefore, we created tables in a spreadsheet including all the independent variable affecting the final renovation prices (e.g., renovation types and materials). The data present in the price-list, such as unit of measure and price unit, were recorded. The whole database was built based on four price-lists representative of the Italian territory: a price-list for Milan, a price-list for the Marche region, a price-list for Latium region and a price-list for Sicily.

In fact, the purpose was to create a decision model that could be applied to all the national territory. The Cost BN is capable of estimating costs while considering several variables, such as:

- the different construction types of the building envelope;
- the location of the building in the national territory;
- the variability of the technology used for the interventions;
- technical differences in the categories of the pricelists adopted.
Once the relevant variables were defined, a spreadsheet including all the node ranges and node states of the variables that could affect the price of admissible renovation actions for the case study was created. As a result, the dataset included all the possible combinations of renovation actions resulting from the combination of variable states, and the corresponding prices of the actions were estimated, based on the price-lists.

The combinations of the input variables and their prices inserted in the spreadsheet were referenced to other "Pivot" type tables. The "Pivot" tables turned out to be a fundamental reference for the construction of the Bayesian Network, because they summed up all the combinations and averaged the final prices when a variability in the choice of some of the inputs was included (e.g., range of size of one element). The average values and standard deviations were then transferred to the cost BN, as depicted in Table 5.

The collection of all the tables described above made it possible to build all the fragments that were subsequently combined into the overall network shown in Figure 9.

Table 4. Comparison between the results deriving from the BN and those from SuoNus tool


Table 5. Example of "Pivot" table
![img-8.jpeg](img-8.jpeg)

Figure 9. Cost estimation Bayesian Network

The CPTs learning process was performed by means of the EM algorithm.

An example of the instantiation of the Cost Estimation Bayesian Network in the circumstance of an Accessibility area (e.g. Access door) that did not comply with the legislation is presented. When a school has only one access door whose handle height does not comply with legislation, the fixture requires replacing.

Table 6 lists the input nodes that need to be provided to the network.

As a result, the replacement cost range is included between 600-700 Euro with a probability of $35.69 \%$.

Subsequently, when the material of the new fixture is chosen, a more precise cost estimation is provided, and the network is updated accordingly, with the maximum
probability within the range between 900-1000 Euro and a value of $53.53 \%$, as depicted on Figure 10.

Finally, the reasoning can even be reversed from consequences back to causes. Assuming the maximum budget available for the replacement of the fixture is limited

Table 6. Input data assumed in the case of fixture replacement


to no more than 600 Euro, the network can identify the best combination. In practice, a $100 \%$ probability is set in the cost range between 500-600 Euro in the "Accesses Cost" node and the network (Figure 11) works out the most likely material for the fixture (either steel of PVC equally likely).

Regarding the threshold, the network shows that it could be between $2-3 \mathrm{~cm}$ in thickness, since the probabilities are $58.26 \%$ and $41.74 \%$, respectively.

### 3.3. Required information from BIM models

Once BIM models are available, Bayesian Networks can be interfaced directly to those models and estimations can be facilitated. The development of the interface between the BIM and every BN is out of the scope of this paper. But some remarks will be provided in the rest of this subsection.

In order to perform this process, BIM models must comply with a minimum information level to be able to automatically retrieve information and transfer it as input into each BN. The management of this information poses extremely important issues relating to:

- the kind of information to be entered and how/where to enter it;
- how to extract information from the model in order to be able to carry out the processing.

The feasibility of an interface is shown by several applications in literature. For example, the paper presented by Solihin, Eastman, Lee, and Yang (2017) showed how to integrate spatial operations into standardized SQL queries making the BIM data accessible for wide ranges of query capabilities. Such feature allows much better visibility into BIM data for better decision-making processes. In addition, Khaja, Seo, and McArthur (2016) used parametric tools such as Dynamo to automate the information transfer between the BIM models and other systems.

For both schools, the necessary data were extracted from the respective BIM models related to each requirement of the Accessibility BN, Energy Efficiency BN and Acoustics BN. In the absence of applications that automatically extrapolate information from the BIM model, information can be extracted manually.

Therefore, in this study all the required information was listed and split into three different groups (Table 7):

1. Data that are already available in the BIM model, e.g. because they are normally included as properties or attributes of the building components;
2. Data that are normally not available in BIM models but that can be inserted by designers and surveyors, e.g. by creating new fields in the families;
3. Data that must be derived by means of post-processing of information, e.g. through the use of Dynamo routines.
![img-9.jpeg](img-9.jpeg)

Figure 10. Cost estimation performed by the Cost BN, once the material was chosen
![img-10.jpeg](img-10.jpeg)

Figure 11. Reversed reasoning when choosing an input variable from a fixed budget

## 4. Results and discussion

### 4.1. Implementation of the DSS

These networks have been implemented to analyze the two case studies described in sub-section 3.1. Figure 12 shows some of the outputs from each BN, estimating the values of performance parameters in the three areas of interest that were developed in Section 3. For both schools, the
necessary data were extracted from the respective BIM models.

The Accessibility BN requires 62 inputs, the Energy Efficiency BN requires 32 inputs, while the Acoustics BN requires, respectively, 11 inputs for the Sabine Bayesian Network regarding the reverberation time and 20 inputs for the overall Acoustics Bayesian Network for the control of the remaining parameters.
![img-11.jpeg](img-11.jpeg)

Figure 12. Example of Bayesian Network outputs: a -Accessibility BN; b - Energy Efficiency BN; c - Acoustics BN

Out of the 125 inputs, 8 and 13 (belonging, respectively, to "accessibility" and "acoustics") are directly available from the BIM model, while 39 and 10 (belonging, respectively, to "accessibility" and "acoustics") are not directly available because they are not native attributes of the families and types on which BIM models are based. So, they can be inferred by the user and they are listed in the column "not available in BIM but derivable", as Table 7 shows. The remaining data could be obtained only through combined analyses or more complex algorithms. As for the "acoustics BN", the compliance was checked room by room, obtaining as final output an acoustic performance index for each of the rooms, these indexes were subsequently averaged into one KPI value per each parameter.

Table 7 reports the necessary information (available in the model, not available but derivable from the BIM models and obtained after post-processing) for the Accessibility network, Energy Efficiency network and Acoustics network.

### 4.1. Results from the application of the multi-criteria assessment

As shown in Figure 1, the last step of the methodology is the multi-criteria analysis based on the AHP approach. The AHP is a method of measurement through pairwise comparison to define priorities and support complex decision making. As stated in Section 2.3, the structure is built from the top representing the goal of the decision, then the criteria from a broad perspective, through the intermediate levels (sub-criteria) to the lowest level (which is usually a set of alternatives). In Table 8 the values of the BN output nodes are listed for the two schools. The output "Level of Compliance" (LoC, in the second column) represents the percentage of requirements that are met in the accessibility area of interest, according to the information entered in the network. The other two columns give the outputs of the indicators chosen to assess Energy Efficiency. The rightmost column shows the percentage of the 'Level of Compliance' (LoC) node in the area of interest "Acoustics".

Table 8. BN outputs for the two case studies


The results shown in Table 8 were combined into a priority ranking, according to the AHP decision approach. Once the different levels of the AHP analysis (e.g. goal, criteria, sub-criteria and alternatives) were established, a pairwise comparison between the different areas of interest and the different indicators within the same area (e.g. energy efficiency) was carried out. As a result, the final ranking was inferred as a combination of the values obtained from BN and the weights (Table 9) determined by means of the pairwise comparison as follows:

$$
R=W_{A}{ }^{*} A+W_{E E}{ }^{*} E E+W_{K P I}{ }^{*} K P I
$$

where $A$ is the "Level of Compliance" for the Accessibility BN and KPI is the "Level of Compliance" for the Acoustics BN reported in Table 7; $W_{a}, W_{e e}$ and $W_{k p i}$ are the weights (Table 9) and $E E$ is computed as follows:

$$
E E=W_{1}{ }^{*} H T C+W_{2}{ }^{*} S E P i
$$

Table 9. Weight values


The application of Eqns (6) and (7) to the cases of the two schools gave the following ranking results: R is equal to 0.66 in the case of "Ungaretti" school and 0.67 in the case of "Mascagni" school. Hence, as "Mascagni" school is ranked higher, the refurbishment should be prioritised for the "Ungaretti" school.

Table 7. Source of information to implement the BNs


Besides helping prioritise interventions, the use of Bayesian Networks would allow managers to deal with uncertainty or missing parameters connected with BIM models. For example, in the case of the Accessibility BN, assuming that some information is not available, all the states of a node can be set according to a uniform distribution (e.g. $50 \%$ false and $50 \%$ true in the case of a Boolean node). Figure 13 depicts how this information can be included when there is no information about the doors. As a result, the new output shown in Table 10 would be obtained.
![img-12.jpeg](img-12.jpeg)

Figure 13. Accessibility BN when no information about the doors is available

Table 10. BN outputs when no information about the doors is available


The application of equations to the case of the two schools gave the following new ranking results: $R$ is equal to 0.67 in the case of "Ungaretti" school and 0.68 in the case of "Mascagni" school. Notwithstanding the partial lack of information, the overall assessment is still made possible thanks to the capabilities of Bayesian Networks, showing that "Ungaretti" school is still the school that gets the lower score, so the first one to require intervention.

Concurrently, the availability of the "cost BN" makes it possible to estimate the necessary budget to improve the level of compliance of the buildings. In this research, this methodology has been applied to the "accessibility" requirement of "Ungaretti" school. In this case, the elements that did not comply with the regulations were the accesses, windows, doors, stairs and ramps.

Figure 14 compares the estimation of renovation costs made with the price-list for Milan (where the school is located) and performed by the Cost BN. This result is quite accurate: looking at the percentage of the states in Figure 14b, the most likely price is in the interval between 400,000-500,000 Euro (55\%). This is the interval within which even the value that was estimated through manual processing of the price-list, shown in Figure 14(a), falls.
a)
![img-13.jpeg](img-13.jpeg)

Figure 14. Validation of the Cost Estimation BN

## Conclusions

The decision support system developed in this paper is aimed at helping facility managers prioritize refurbishment actions when they have to manage large building stocks scattered over wide territories. One of the main challenges is connected to the scarce availability of information on existing buildings, which is often not complete, despite the incremental use of building information models. This is mainly due to the lack of knowledge and to the practical and economic limitations related to on-site verifications and tests and/or to the limited availability of construction drawings and original material specifications. A limiting aspect is also the implementation of BIM in this field, which requires a great modelling effort to transfer data from paper documents or CAD data to BIM models.

In fact, previous research studies showed a scarce implementation of BIM methodology in existing buildings.

For these reasons, the DSS presented in this paper has been built on top of Bayesian Networks, which can manage uncertainty and missing information and are in charge of estimating the values of some indicators regarding the quality of a building in three areas of interest: accessibility, energy efficiency and acoustics. A further "cost BN" has been developed to estimate the budget that must be set aside to perform renovation actions.

One of the drawbacks of this system could be the updating of large dataset with many variables being estimat-

ed. These BNs are trained through datasets and these data must be generated either from simulations or evidences. As a consequence, changes in standard or technology, for example in building materials which involve making further simulations, require to extend and update the dataset to be used for additional learning of Bayesian Networks. However, BNs can be a powerful tool used in many fields where there is need for prediction and outcome is uncertain.

In fact, during the implementation, the DSS showed several positive capabilities. First, it has been able to estimate the indicators for each of the areas of interest, once the inputs were available, and with limited computational effort. Secondly, the DSS developed in this paper is able to perform estimations and related rankings even in case the information concerning some parameters is uncertain or missing; the final assessment based on the outputs from Bayesian Networks is still accurate and the platform is able to provide an assessment, in our case indicating that the "Ungaretti" school is the one mostly in need for refurbishment. More importantly, the application of the AHP method for multi-criteria analysis made it possible to work out one overall index which is in charge of ranking any facility. It is this ranking that can support facility managers in their decisions.

The reliability of the networks was validated against simulations performed with standard computational tools. Also, an analysis regarding the input data that need to be made available to implement the DSS and whether these data can be retrieved from BIM models has been proposed. The analysis showed that some data are already included in the properties or attributes of the families in BIM software tools, but there is quite a high number of variables that need to be evaluated through a post-processing and which are not usually readily available in BIM models.

## Funding

This work was supported by the joint research grant funded by "Politecnico di Milano" (Milan, Italy) and "Università Politecnica delle Marche" (Ancona, Italy) entitled "Learning BIM with Intelligent Models" and signed as of $12^{\text {th }}$ September 2017.

## Author contributions

Alessandro Carbonari, Giuseppe Martino Di Giuda and Valentina Villa designed the whole study and managed the whole work. Alessandra Corneli and Luigi Ridolfi were responsible for the state of the art session. Alessandra Corneli developed the Accessibility, Acoustic and Cost estimation Bayesian Networks. Luigi Ridolfi developed the Energy efficiency Bayesian Network. Alessandro Carbonari supervised the development of all the Bayesian Networks. Valentina Villa developed the BIM models of the case studies. Luigi Ridolfi worked out the implementation of the DSS, while discussion and conclusions were written jointly by Alessandro Carbonari, Giuseppe Martino Di Giuda and Valentina Villa.

## Disclosure statement

The authors declare that they do not have any competing financial, professional, or personal interests from other parties.
