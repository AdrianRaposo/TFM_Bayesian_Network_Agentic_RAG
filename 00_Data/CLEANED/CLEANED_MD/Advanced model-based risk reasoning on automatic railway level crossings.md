# HAL open science 

## Advanced model-based risk reasoning on automatic railway level crossings

Ci Liang, Mohamed Ghazel, Olivier Cazier, Laurent Bouillaut

## To cite this version:

Ci Liang, Mohamed Ghazel, Olivier Cazier, Laurent Bouillaut. Advanced model-based risk reasoning on automatic railway level crossings. Safety science, 2020, 124, pp1-11. 10.1016/j.ssci.2019.104592 . hal-02461175

## HAL Id: hal-02461175 <br> https://hal.science/hal-02461175v1

Submitted on 31 Jan 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Advanced model-based risk reasoning on automatic railway level crossings 

Ci Liang a,b,c, ${ }^{\text {a }}$, Mohamed Ghazel ${ }^{\text {b,c,a }}$, Olivier Cazier ${ }^{\text {d,a }}$, Laurent Bouillaut ${ }^{\text {e }}$<br>${ }^{a}$ FCS Railenium, Valenciennes, France<br>${ }^{b}$ IFSTTAR-COSYS / ESTAS, Lille-Villeneuve d'Ascq, France<br>${ }^{c}$ University Lille Nord de France, Lille-Villeneuve d'Ascq, France<br>${ }^{d}$ SNCF Réseau, Paris, France<br>${ }^{e}$ IFSTTAR-COSYS / GRETTIA, Paris-Marne-la-Vallée, France


#### Abstract

Safety is a core issue in the railway operation. In particular, as witnessed by accident/incident statistics, railway level crossing (LX) safety is one of the most critical points in railways. In the present paper, a Bayesian network (BN) based framework for causal reasoning related to risk analysis is proposed. It consists of a set of integrated stages, namely risk scenario definition, real field data collection and processing, BN model establishment and model performance validation. In particular, causal structural constraints are introduced to the framework for the purpose of combining empirical knowledge with automatic learning approaches, thus to identify effective causalities and avoid inappropriate structural connections. Then, the proposed framework is applied to risk analysis of LX accidents in France. In details, the BN risk model is established on the basis of real field data and the model performance is validated. Moreover, forward and reverse inferences based on the BN risk model are performed to predict LX accident occurrence and quantify the contribution degree of various impacting factors respectively, so as to identify the riskiest factors. Besides, influence strength and sensitivity analyses are further carried out to scrutinize the influence strength of various causal factors on the LX accident occurrence likelihood and determine which factors the LX accident occurrence is most sensitive to. The main outputs of our study attest that the proposed framework is sound and effective in terms of risk reasoning analysis and offers significant insights on exploring practical recommendations to prevent LX accidents.


Keywords: Level crossing safety, Risk analysis, Bayesian network modeling, Causality identification, Influence and sensitivity analysis;

## 1. Context and related works

On December 14, 2017, a train and a school bus collided at a railway Level crossing (LX) near Perpignan in southern France, killing 6 children between 8 and 14 years old and injuring more than 20 others (Willsher, 2017). The accident happened at an automatic LX (SAL2, refer to section 5.1) on a two-lane road as the bus crossed a single-track railway line secured by a barrier and warning lights in each direction. LXs are potentially hazardous locations where trains, road vehicles and pedestrians move in close proximity. LX safety remains one of the most critical issues for railways despite an ever-increasing focus on improving design and application practices (Ghazel, 2009). In France, the railway network shows more than 18,000 LXs for $30,000 \mathrm{~km}$ of railway lines, which are crossed daily by 16 million vehicles on average, and around 13,000 LXs show heavy road and railway traffic (Liang et al., 2018a, 2017b; SNCF Réseau, 2011). Despite numerous measures already taken to improve the LX safety in 2016, there were 111 collisions at LXs in France leading to 31 deaths (Liang et al., 2017c). About $90 \%$ of the accidents involved cars or light vehicles,

[^0]
[^0]:    ${ }^{a}$ Corresponding author at: IFSTTAR, Lille-Villeneuve, France.
    Email: ciliang.lc@gmail.com.

reported by SNCF Réseau, the French national railway infrastructure manager (Plesse, 2017). This number was half the total number of collisions per year at LXs a decade ago, but still too high. In order to significantly reduce the accidents and lessen their related consequences at LXs, effective risk assessment means are needed urgently.

In this paper, a novel framework of Bayesian Network (BN) based Inference for Risk Reasoning (BNI-RR) is proposed to deal with the analysis of accident causes and consequences at LXs. Besides, this framework describes a general risk analysis process that is not limited to the LX context and can be applied to other domains. Specifically, the present study involves: 1) developing an effective modeling framework (BNI-RR) for risk reasoning, which includes a set of comprehensive stages, i.e., risk scenario definition, real field data collection and processing, BN model establishment and model performance validation; 2) introducing causal structural constraints to the BNI-RR framework for the purpose of combining empirical knowledge with automatic learning approaches, so as to avoid inappropriate structural connections and highlight main causes; 3) developing BN models and performing corresponding analysis for French LX risk scenario using the BNI-RR framework, thus to identify potential impacting factors that contribute most to LX accident occurrence. The underlying aim is to pave the way toward discovering practical design measures and improvement recommendations to prevent accidents at LXs. Note that although the BN model in this paper is developed on the basis of a quite preliminary model discussed in (Liang et al., 2017a), the methodologies to build the models and the models themselves are completely different. Namely, the developed BN model in this paper comprehensively considers both static factors and motorist behavior related factors. Moreover, the established model in this paper allows us to perform consequence evaluation based on the combination of field data and expert knowledge, compared with only three static factors considered in the model presented in (Liang et al., 2017a).

The present paper is structured as follows: section 2 gives a review on existing related works. Section 3 recalls the theory of probability which underlies BNs. Section 4 elaborates each stage of the BNI-RR framework. Section 5 is dedicated to the application of the BNI-RR framework to French LX risk analysis, particularly establishing and validating the BN risk model. Section 6 analyzes and discusses the outcomes of the BN risk model and finally, some concluding remarks and further directions are given in section 7.

# 2. Related work review 

In current years, risk analysis approaches are required to deal with increasingly complex systems with a large number of involved parameters. Moreover, an intelligent decision support system for risk analysis shall have the ability of making inference based on the risk causal knowledge. Therefore, such approaches should fulfill the following characteristics (Liang et al., 2018b):

- Having strong modeling ability,
- Having high computational efficiency,
- Providing simple means to specify a risk scenario/project,
- Offering effective reasoning between risky factors and scenario/project,
- Effectively identifying the most important risky factors.

More recently, risk analysis/safety improvement based on formal modeling, regression models, fuzzy logic and neural networks have expanded. For example, in order to compare the effectiveness of two main Automatic Protection Systems (APSs) at LXs, namely two-half-barrier APS and four-half-barrier APS, Generalized Stochastic Petri Nets (GSPNs) were used in (Ghazel and El-Koursi, 2014) to analyze the aleatory fluctuations of various parameters involved in the dynamics within the LX area. Yan et al (2010) introduced hierarchical tree-based regression models to explore train-vehicle crash prediction and analyze the impact of factors on crash frequency at passive highway-rail LXs. Niittymaki and Kikuchi (1998) discussed a Fuzzy Logic controller for managing the timing of a pedestrian crossing signal. The controller was designed to emulate the decision process of an experienced crossing guard. In (Neumann, 2002), the principal component analysis is combined with Neural Networks to perform software risk classification and discriminate high-risk projects with imbalanced data sets. Mahmoud and Katsifolis (2010) proposed a classification system using a supervised Neural Network, which is applied to the detection and recognition of intrusion and non-intrusion events at LXs. However, these approaches are unable to identify causality effectively.

Over the last decade, Bayesian network (BN) has been an increasingly popular notation used for risk reasoning

analysis of safety-critical systems or large and complex dynamic systems, using probabilities (Liang et al., 2018b). When making risk analysis and seeking to obtain proper and effective risk control, risk planning should be performed based on risk causality, which can provide detailed information for decision making. In this context, a method for software risk analysis based on BNs combining with expert knowledge and V-structure discovery algorithm was proposed in (Hu et al., 2013). In (Lauría and Duchessi, 2006), authors discussed how to build BNs from real-world data and incorporated BNs into decision support systems to support "what-if" analysis about Information Technology implementations. Heuristic model searching techniques and Maximum a Posteriori (MAP) estimation are used in this study to estimate the structure and parameters of the BN. A semi-formal method for constructing the graphical structure of BNs based on domain knowledge using the causal mapping approach is discussed in (Nadkarni and Shenoy, 2004). The causal knowledge of experts is formally represented by causal maps, so as to consider the reasoning underlying the cause-effect relations perceived by individuals. In (Bouillaut et al., 2013), the authors discussed the development of a decision tool realized on the basis of hierarchical Dynamic BNs (DBNs), which is dedicated to the maintenance of metro lines in Paris. This modeling work has comprehensively described the rail degradation process, the different diagnosis actors (devices and staff) and the decisions pertaining to maintenance actions. (Langseth and Portinale, 2007) discussed the applicability of BNs for reliability analysis and offered an instance of BNs' application for preventive maintenance. Moreover, the authors of this paper discussed the advantages behind BNs as follows: a) BNs constitute a modeling framework, which is particularly easy to use for interaction with domain experts; b) the sound mathematical formulation has been utilized in BNs to generate efficient learning methods and c) BNs are equipped with an efficient calculation scheme which often makes BNs preferable to traditional tools like Fault Trees (FTs).

To sum up, the BN technique offers interesting features: flexibility of modeling, strong modeling power, high computational efficiency and, most importantly, the outstanding advantages involving the conjunction of domain expertise and automatic structure/parameters learning, causality analysis based on both forward inference (deductive reasoning) and reverse inference (abductive reasoning) (Weber et al, 2012), as well as further influence and sensitivity analysis. For our study, given all the interesting features characterizing BNs, we adopted this notation as the underpinning of the BNI-RR framework that will be discussed in the sequel.

# 3. Bayesian networks 

A BN is a graphical model that can be characterized by its structure and a set of parameters known as conditional probability tables (CPTs) (Jensen, 1996). $B N=(P, \mathcal{G})$, where $P$ represents the parameters of conditional probabilities assigned to the arcs, while $\mathcal{G}$ defines the model structure. In fact, $\mathcal{G}=(N, L)$ is a Directed Acyclic Graph (DAG) that is comprised of a finite set of nodes $(N)$ linked by directed arcs $(L)$. The nodes represent random variables, while the directed arcs between pairs of nodes represent dependencies between the variables. For instance, a three-variable BN is shown in Fig. 1. This net shows a "V" structure while the conditional probabilities of states are defined in each node.

The semantics of BN is based on the theory of probability. Assume that there is a set of mutually exclusive events: $B_{1}, B_{2}, \ldots, B_{n}$ and a given event $A$ such that $P(A)$ can be expressed as follows:

$$
P(A)=\sum_{i=1}^{n} P\left(B_{i}\right) P\left(A \mid B_{i}\right)
$$

According to Bayes' formula:

$$
P\left(B_{i} \mid A\right)=\frac{P\left(B_{i}\right) P\left(A \mid B_{i}\right)}{\sum_{j=1}^{n} P\left(B_{j}\right) P\left(A \mid B_{j}\right)}
$$

Hence, Eq. (2) can be converted into:

$$
P\left(B_{i} \mid A\right)=\frac{P\left(B_{i}\right) P\left(A \mid B_{i}\right)}{P(A)}
$$

Here, $P\left(B_{i}\right)$ is called the prior probability, while $P\left(B_{i} \mid A\right)$ is the posterior probability. Therefore, when the CPTs of variables are given in a BN, the posterior probability can be computed.

![img-0.jpeg](img-0.jpeg)

Fig. 1. An instance of a three-variable BN

For any set of random variables in a BN, the joint distribution can be computed through conditional probabilities using the chain rule as shown in Eq. (4):

$$
\begin{aligned}
& P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)=\prod_{v=1}^{n} P\left(X_{v}=x_{v} \mid X_{v+1}=\right. \\
& \left.x_{v+1}, \ldots, X_{n}=x_{n}\right)
\end{aligned}
$$

Due to the conditional independence, $X_{v}$ only relates to its parent node $P a\left(X_{v}\right)$ and is independent of the other nodes. Hence, Eq. (4) can be rewritten as follows:

$$
P\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)=\prod_{v=1}^{n} P\left(X_{v}=x_{v} \mid P a\left(X_{v}\right)\right)
$$

# 4. BNI-RR framework 

A modeling paradigm has to view an influential network not merely as passive parsimonious codes for storing factual knowledge, but also as a computational architecture for reasoning about the knowledge. It means that the links in the network should be treated as the only pathways and activation units that direct and propel the flow of data in the process of querying and updating causal knowledge. In this section, while having in mind this principle, the BNI-RR framework is proposed. The BNI-RR framework can be illustrated as shown in Fig. 2. Namely, the process of BNI-RR approach consists of the following stages:

1) Risk scenario definition: before performing risk analysis and in order to set the research target, a clear definition of the risk scenario boundary must be achieved. One should focus on this defined risk scenario to ensure that the follow-up study does not deviate from the original intention.
2) Real field data collection and processing: for risk analysis and cause diagnosis, real field data related to the defined risk scenario need to be collected. These data should be recorded in a workable database and used as the basis of data processing. Data processing includes data merging/cleansing and data discretization, which is the basis of parameters learning and CPT definition. Note that the ethics approval needs to be considered when collecting field data.
3) BN model establishment: on the one hand, the model structure is constructed with regard to the combination of automatic structure learning and causality constraints derived from expert knowledge (cf. 4.1). On the other hand, the model CPTs are generated on the basis of the post-processing field data. Model structure constructing in this stage will be elaborated in section 4.1.

4) Model validation: the Receiver Operating Characteristic (ROC) curve and the Area Under the ROC Curve (AUC) (Hanley and McNeil, 1982) are adopted to validate the model performance of prediction. The ROC curve is a two-dimensional graph that can be obtained by plotting the true positive rate (TPR) (Y-axis) against the false positive rate (FPR) (X-axis) at various threshold settings (Powers, 2011). The TPR is known as the sensitivity, the recall or the probability of detection in machine learning. The FPR is known as the fall-out or the probability of false alarm. The ROC curve thus depicts relative trade-offs between benefits (true positives) and costs (false positives). In order to facilitate the evaluation of classifier performance, one may want to reduce ROC performance to a single scalar value that can represent the expected performance. A common method is to calculate the AUC which is a portion of the area of a unit square, and the value of which falls into the interval between 0 and 1. When using normalized units, the AUC is equal to the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one. The ROC curve of a finite set of samples is based on a step function, and its AUC can be computed by the normalized Wilcoxon-Mann-Whitney (WMW) statistic (Yan et al, 2003):

$$
A U C=\frac{\sum_{i=1}^{m} \sum_{j=1}^{n} I\left(x_{i}, y_{j}\right)}{m \times n}
$$

where $x_{i}, i=1, \ldots, m$, is the sample of positive classifier outputs; $y_{j}, j=1, \ldots, n$, is the sample of negative classifier outputs and

$$
I\left(x_{i}, y_{j}\right)=\left\{\begin{array}{l}
1, x_{i}>y_{j} \\
0, \text { otherwise }
\end{array}\right.
$$

is based on pairwise comparisons between $x_{i}$ and $y_{j}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The BNI-RR framework

# 4.1. BN model structure constructing 

### 4.1.1. Causality discovery

Causality is the relationship between a cause and a consequence. Identifying such causal relationships is a crucial issue in the process of risk reasoning. In particular, a functional intelligent decision/prediction model should have the ability of making reasoning based on causal knowledge.

For instance, in railways, potential hazards such as equipment failures, human errors and environment aspects, may lead to incidents/accidents. Taking human errors for example, this can be expressed as a rule IF human errors occur, THEN accidents may occur. Therefore, the DAG $\mathcal{G}_{C}$ of a causal network can be interpreted by a causal semantics as follows:

$$
\mathcal{G}_{C}=\{I F, T H E N, C A K\}
$$

where:
$\mathcal{G}_{C}$ is a 3-tuple causal DAG;
$I F$ is a set of causes, $I F=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$;
THEN is a set of consequences caused by the causes in $I F, T H E N=\left\{y_{1}, y_{2}, \ldots, y_{m}\right\}$;
CAK represents the CAusal Knowledge, which is a set of directed pairs of the cause $x_{i} \in I F$ and the corresponding consequence $y_{j} \in T H E N: C A K=\left\{\left(x_{i}, y_{j}\right) \mid x_{i} \in I F, i=1,2, \ldots, n ; y_{j} \in T H E N, j=1,2, \ldots, m\right\}$ while note that $\left(x_{i}, y_{j}\right)$ is a directed variable pair that defines the structure of $\mathcal{G}_{C}: x_{i} \rightarrow y_{j}$ and cannot be reversed, which reflects the causal relationship between $x_{i}$ and $y_{j}$ at the same time. For example, in Fig. 1, $\mathcal{G}_{C}=\left\{I F=\left\{B_{1}, B_{2}\right\}, T H E N=\{A\}, C A K=\left\{\left(B_{1}, A\right),\left(B_{2}, A\right)\right\}\right\}$.

Hence, by considering the causality in the BN , the states of the target variable can be predicted even when the states of the other factors are changed. More importantly, once a given state of the target variable occurs, the contribution of the impacting factors can be investigated.

In practice, preliminary causality is discovered through automatic structure learning. Here we introduce six structure learning approaches that are widely used to build BN structures:

1) The Bayesian Search (BS) algorithm is one of the earliest and the most popular algorithms used. It was introduced in (Cooper and Herskovits, 1992) and later was refined in (Heckerman et al., 1994). It follows essentially a hill climbing procedure, generally guided by a scoring heuristic, with random restarts.
2) The Essential Graph Search (EGS) algorithm, proposed in (Dash and Druzdzel, 1999), performs a search for essential graphs based on a combination of the constraint-based search and BS approach.
3) The Greedy Thick Thinning (GTT) algorithm performs based on the BS approach and has been described in (Cheng et al., 1997). GTT starts with an empty graph and repeatedly adds the arc (without creating a cycle) that maximally increases the marginal likelihood until no arc addition results in a positive increase (thickening phase). Then, it repeatedly removes arcs until no arc deletion results in a positive increase in the marginal likelihood (thinning phase).
4) The Naïve Bayes approach (Good, 1965) creates a Bayesian network including its structure and parameters, directly from data. In fact, the structure of a Naïve Bayes network is not learned but rather fixed by an assumption: the class variable is the only parent of all remaining feature variables and there are no other connections between the nodes of the network. Note that the Naïve Bayes structure assumes that the feature variables are independent conditional on the class parent variable, which leads to inaccuracies when they are not independent in reality.
5) The Augmented Naïve Bayes (ANB) algorithm is a semi-naive structure learning method based on the BS approach (Friedman et al., 1997). The ANB algorithm starts with a Naïve Bayes structure (i.e., the class variable is the only parent of all remaining feature variables) and adds connections between the feature variables to account for possible dependence between them and conditional on the class variable. There is no limit on the number of additional connections between the feature variables. The ANB algorithm is simple and has been found to perform reliably better than Naïve Bayes.
6) The Tree Augmented Naïve Bayes (TAN) algorithm is also a semi-naive structure learning method based on

the BS approach (Friedman et al., 1997). Compared with The ANB algorithm, The TAN algorithm imposes the limit of only one additional parent of each feature variable (additional to the initial class variable that is the parent of every feature variable). The TAN algorithm is simple and performs better than Naïve Bayes as well.

# 4.1.2. Causality optimizing 

In terms of causal reasoning, one can notice that model structures learned on the basis of the aforementioned approaches are often preliminary, even make no sense of reasonability. These preliminary structures are inconsistent with the causal relationships in reality, and in some cases, some connections are more likely correlations rather than causalities in reality and impede identification of important causes. Causalities can be identified from correlations, however, causalities are not equal to correlations. Many previous methods cannot achieve this important issue; therefore, causality optimizing is indispensable to be performed based on causal constraints, for the purpose of finely distinguishing causalities from correlations.

Pearl and Verma (1995) have stated that an intelligent reasoning system should have the competence of distinguishing causalities from correlations in terms of causation. Moreover, empirical expert knowledge is significant to achieve such a distinction. Therefore, causal structural constraints (Campos and Castellano, 2007) (CSCs) generated from expert knowledge are adopted to achieve causality optimizing in the present study.

In general, there are 3 types of directed CSCs of BNs: Existence Constraint (EC), Forbidden Constraint (FC), and Potential Directed Constraint (PDC). For instance, given a BN $\mathcal{N}$ and two variables $x$ and $y$ of $\mathcal{N}$, based on the definition of $C A K$, an EC $(x, y)_{p}$ means that there must be a direct connection from $x$ to $y$; an FC $(x, y)_{f}$ means that there must not be a direct connection from $x$ to $y$; a PDC $(x, y)_{p}$ means that if there exists a direct connection between $x$ and $y$, it should be from $x$ to $y$, while from $y$ to $x$ is not allowed. Utilizing PDCs can control constraint granularity and be perspicuous to describe a contrary edge orientation to an inappropriate automatic learning structure.

To sum up, adopting jointly the above directed CSCs can effectively perform combination of automatic structure learning from observational data and expert knowledge. The detailed advantages are three-fold: 1) identifying unknown but potentially valuable causalities, especially when samples are limited, 2) verifying the already known causalities, and 3) avoiding inappropriate connections to facilitate highlighting main causes.

## 5. Application

In this section, the BNI-RR framework is applied to the risk analysis of French LXs. The risk analysis is carried out based on the real field accident/incident data collected by SNCF. In the sequel, we will discuss the various steps of the framework.

### 5.1. Risk scenario definition

There are four LX types in France (Liang et al., 2017a; SNCF, 2015): a) SAL4: Automated LXs with four half barriers and flashing lights; b) SAL2: Automated LXs with two half barriers and flashing lights; c) SAL0: Automated LXs with flashing lights but without barriers; d) Crossbuck LXs, without automatic signaling.

As shown in Table 1 (Liang et al., 2017a), SAL2 (more than 10,000) is the most widely used type of LX in France according to the LX data recorded by SNCF. Moreover, the accident/incident records show that more than 4,000 accidents at SAL2 contributed most to the total number of accidents at LXs from 1974 to 2014. In addition, according to SNCF statistics, the accidents at SAL2 LXs can be considered as the most representative of LX accidents in general. Besides, being given the number of SAL2 LXs, dealing with this LX category constitutes a priority issue for SNCF. According to the previous statistical analysis, one can notice that the motorized vehicle is the main transport mode causing accidents at LXs (Liang et al., 2017a, 2018a). Considering the train/motorized vehicle (train-MV) collisions, SAL2 LXs also report the most accidents from 1978 to 2013 (Liang et al., 2017a). It should be noted that suicide scenarios are not in the scope of our study. In what follows, we consider the risk scenario corresponding to the situation where the "motorized vehicles cross SAL2 LXs when trains are approaching".

# 5.2. Data collection and processing 

The approach for causal inference in the present study is based on field-observational-data. For the main purpose of assessing risk level and diagnosing causes, real field accident/incident data related to the defined risk scenario need to be collected. This is an important preparatory stage that is required prior to the establishment of the BN model. It should be noted that, in terms of ethics approval, the data collected in the present study do not hold any personal or private aspects. Only the agreement to install the recording devices was needed.

SNCF Réseau investigated and recorded various attributes of LX accidents/incidents, such as railway and roadway traffic characteristics, surrounding characteristics of LXs and then, provided two accident/incident databases to support our study. The first database (D1) records the accident/incident data that cover SAL2 LXs in mainland France from 1990 to 2013. From D1, the sub-dataset (SD1) including the data ranging in the decade from 2004 to 2013 is selected, which provides reliable and sufficient information about both LX accidents and static railway, roadway and LX characteristics (considered as permanent characteristics related to LXs). Namely, the selected LX inventory presents the LX identification number, the LX accident timestamp, the railway line involved, the LX kilometer point, the average daily railway traffic, the average daily road traffic, the rail speed limit, the LX length and width, the profile and alignment of the entered road and geographic region involved. There are 8,332 public SAL2 LXs included in SD1.

According to the statistics, the majority of train-MV accidents at LXs are caused by motorist violations. Due to the lack of accident causes in SD1, causal reasoning analysis cannot be performed with regard to the static factors and motorist behavior. Therefore, we need to utilize another database which records detailed accident causes. Fortunately, the second database (D2) contains the information about SAL2 LX accidents during the period from 2010 to 2013, namely, the LX identification number, the railway line involved, fatalities, injuries, and accident causes (including static factors and inappropriate motorist behavior). Thus, using the LX ID and the railway line ID, data merging of these two databases is carried out to create a new database (ND) containing the LX accident information, static railway, roadway and LX characteristics, the number of fatalities and injuries, and accident causes related to static factors and motorist behavior. This combined database ND covers LX accidents during a period of 4 years from 2010 to 2013, which forms the basis of our present study.

The accident causes were classified into three levels: primary, secondary and third-level causes. The various causes considered in this study are shown in Table 3. It should be noted that corrected moment $\left(C M=V^{0.354} \times T^{0.646}\right)$ (Liang et al., 2018a) which is a secondary cause, is a variant of the conventional traffic moment. The conventional traffic moment is defined as: Traffic moment $=$ Road traffic frequency $\times$ Railway traffic frequency (Liang et al., 2017a). However, based on some previous analyses, we adopt CM instead. $C M=V^{a} \times T^{b}$, where $b=1-a$ and the best value of $a$ in terms of fitting is computed to be $a=0.354$ according to the statistical analysis performed by SNCF Réseau (SNCF Réseau, 2010). In fact, railway traffic has a more marked impact on LX accidents than road traffic. Therefore, $\left(V^{0.354} \times T^{0.646}\right)$ is considered as an integrated parameter that reflects the combined exposure frequency of both railway and road traffic. Moreover, data discretization is applied on continuous causal variables. Namely, the continuous causal variables, i.e., "Average Daily Road Traffic", "Average Daily Railway Traffic", "Railway Speed Limit", "LX Width", "Crossing Length" and "Corrected Moment", are divided into 3 groups that each group has the similar number of samples. As for the "Region Risk" factors corresponding to 21 regions in mainland France, they are divided into 3 groups as well, ranked according to the risk level in descending order, and each group contains 7 region risk factors. As for the finite discrete causal variables, i.e., "Alignment", "Profile", "Stall on LX", "Zigzag Violation", "Blocked on LX" and "Stop on LX", we allocate an individual state to each value of the variable.

Table 1. Accidents at different types of LXs in France from 1974 to 2014


# 5.3. BN modeling 

It is worthwhile to mention here that GeNIe is used as the BN modeling tool to build our BN risk model and perform analyses related to the BN risk model. In the subsequent sections, we will go through the various steps of the BN model development.

### 5.3.1. Variable definition

Based on the combined database ND, the pre-processed data of causal variables aforementioned in section 5.2 are organized as input sources which will be used to generate the CPTs of our BN risk model. On the other hand, consequence variables, i.e., "Fatalities", "Severe Injuries" and "Minor Injuries", are defined respectively with two states according to the domain expertise and the coefficient of variation (StdDev/Mean) (Reed, 2002) of the three variables.

Besides, in our BN risk model, an additional variable corresponding to the consequence severity (EN 50126, 1999) is defined according to the number of fatalities and injuries in a given SAL2 accident. The definition of consequence severity pertaining to an SAL2 accident is illustrated in Table 2. Five levels of consequence severity are set according to the number of fatalities, severe injuries and minor injuries caused by the accident, respectively. The consequence severity increases progressively from level 1 to 5 . Thus, a summary of the states corresponding to each node in the

Table 2. Consequence severity definition.


BN risk model is given in Table 3.

### 5.3.2. Model structure establishment

In this stage, CSCs are adopted to set up our BN risk model. As shown in Table 3, the causal variables considered fall into two types: static factors and motorist behavior factors. We firstly identify the internal CSCs within static factors and motorist behavior factors, respectively. Furthermore, it is worth noticing that there are some potential connections between static factors and motorist behavior. SNCF experts provide their knowledge about CSCs between these two types of factors, while checking the potential correlation relations. Therefore, the whole CSCs are identified as shown in Fig. 3. In this figure, blue, red and green arcs represent ECs, FCs and PDCs, respectively. Note that the "Consequence Severity" shown in Table 3 is a Deterministic node that is not considered in the process of CSC identification. In order to show these CSCs more clearly, we list them in Table 4. PDCs and some FCs are suggested by SNCF experts. With these CSCs, the final BN risk model is generated as shown in Fig. 6. In addition, CPTs are generated based on the post-processing real field accident/incident data.

One can notice that, the BN risk model contains two layers: 1) Layer 1 is used for diagnosing influential factors; 2) Layer 2 is used for evaluating consequences related to LX accidents. The "SAL2 MV Accident" node colored in yellow is the key node connecting the two layers, as well as the target node of accident prediction. In Layer 1, we split the network into 2 sub-networks: the static factor related network (SFN) and the motorist behavior factor related network (MBFN).

Table 3. States of nodes in the BN risk model.


SF: Static factor; MBF: motorist behavior factor.

# 5.4. Model performance validation 

Now that the BN structure is set up, we need to deal with model validation. In this section, ROC and AUC are adopted to evaluate the prediction performance of the present BN risk model. Regarding the AUC test, we should recall the following:

1) If $\mathrm{AUC}=1$, it is a perfect prediction model. When using it, a perfect prediction can be obtained with at least one threshold value.
2) If $0.5<\mathrm{AUC}<1$, it is better than random guessing and has relatively sound predictive value.

![img-2.jpeg](img-2.jpeg)

Fig. 3. CSCs identified for the BN risk model.
3) If $\mathrm{AUC}=0.5$, it is the same as random guessing, for example, throwing coin, thus, this model has no predictive value.
4) Otherwise, $\mathrm{AUC}<0.5$, it is worse than random guessing and valueless; but obviously, for the reverse-prediction, it is better than random guessing.

Therefore, one can notice that the ideal perfect ROC curve (cf. section 4) is the point $(0,1)$. Moreover, the closer the AUC to 1, the better the performance of a prediction model.

Besides, the K-fold cross-validation method is used to perform validation (GeNIe, 2017) (the Deterministic node should be excluded when performing validation). Here, we set $\mathrm{K}=2$, namely, the data set is divided into two parts of equal size and the first part is used for parameters training, while the second part is used for validation. In our BN risk model, "SAL2 MV Accident", "Fatalities", "Severe Injuries" and "Minor Injuries" are the targeted prediction nodes which we care about.

Further comparison related to the prediction performance of the 4 nodes is performed between our BN model and the BN models automatically generated by BS, EGS, GTT, Naïve Bayes, ANB and TAN. As shown in Table 5, through investigating the results of the other 6 learning approaches, the entire accuracy and AUC values of our proposed model are clearly better than those of the other 6 learning approaches.

Moreover, the prediction accuracy for accident/consequence occurrence is investigated to further compare the prediction performance between our model and the 6 traditional learning approaches. As shown in Table 6, the accuracy values for "SA = False"/"SA = True" (1/0.9622), "F = 0"/"F = 0_up" (1/0.9020), "S = 0_2"/"S = 2_up" $(1 / 0.6)$ and "M = 0_3"/"M = 3_up" $(1 / 0.75)$ of our model are relatively higher than those of the other 6 learning approaches. Note that the sample size of single accident related to "severe injuries more than 2" and "minor injuries more than 3" is small in reality, which lead to the lower accuracy compared with the accuracy of "SA = True" and "F $=0 \_u p$ ".

The better performance of our proposed model is mainly attributed to the incorporation of expert knowledge and preliminary causality identification. Indeed, this significantly reduces the negative effect of trivial correlations

Table 4. CSCs for the BN risk model


Table 5. Comparison of entire prediction performance.


ACCU: accuracy;
and improves the reliability of the identified causal relationships among the variables considered. Therefore, these validation results indicate that our BN risk model has relatively sound prediction performance and allow us to consider the outcomes of the model to be trustworthy. Besides, this attests that the proposed BNI-RR framework promotes the efficiency of risk analysis.

# 6. Analysis and discussion 

In this section, we will illustrate how the BNI-RR framework can be advantageously worked out to perform risk analysis on LXs. We should mention that the aspects discussed in the sequel do not represent the exhaustive capabilities through our framework, and should be regarded as illustrations.

### 6.1. Forward and reverse inferences

Based on the BN risk model, one can estimate the probability of a train-MV accident occurring at an SAL2 LX through forward inference. As shown in Fig. 4, the general probability of a train-MV accident occurring at an SAL2 over the four years influenced by the interaction of all the factors considered, is estimated as almost 0.0061 . As an illustration, the probability of a train-MV accident caused by static factors is about 0.0011 and the probability of a train-MV accident caused by inappropriate motorist behavior is about 0.0049 . Moreover, fatalities and severe injuries caused by the accident are, to a large extent, fewer than 1 and 2 , respectively $(P(F=F . .0)=0.9993, P(S=S . .0 . .2)=$ 0.9999 ). Minor injuries caused by an SAL2 accident are most likely to be fewer than $3(P(M=M . .0 . .3)=0.9998)$. Thus, the consequence severity level is most likely to be level $1(P(C S=$ Level_1 $)=0.9990)$.

Table 6. Comparison of prediction performance for accident/consequence occurrence.


$\mathrm{ACCU}:$ accuracy;


$\begin{array}{llll}\text { Motorist_Behavior_Accident } & \text { Fatalities } & 0.99894278 \\ \text { True } & 0.9960918269 & \text { True } & 0.0010572159\end{array}$


$\begin{array}{llll}\text { Severe_Injuries } & \text { Minor_Injuries } & \\ \text { 5_0_2 } & 0.99987146 & \text { M_0_3 } & 0.99979531 \\ \text { 5_2_up } & 0.00012853755 & \text { M_3_up } & 0.00020468538\end{array}$


Fig. 4. General prediction.


$\begin{array}{llll}\text { SAL2_MV_Accident } & \text { Static_Factor_Accident } \\ \text { $\square$ False } & 0.9615858 & \text { False } & 0.99107373 \\ \text { $\square$ True } & 0.0384142 & \text { True } & 0.008926271\end{array}$


Fig. 5. Prediction related to the occurrence of severest states of secondary causes.

Fig. 5 shows that the probability of a train-MV accident occurring at an SAL2 would increase to 0.0384 if all the risky states of secondary causes occur, namely "Corrected Moment" in the "CM_49_up" group, "Railway Speed Limit" in the "RSL_110_up" group, "Alignment" in the "S_shape" group, "Profile" in the "Hump_cavity" group, "Width" in the "W_6_up" group, "Length" in the "L_11_up" group, "Region Risk" in the "R_high" group, "Stall on LX" being true and "Zigzag Violation" being true. The related consequences are likely to be severer as well. In this way, various prediction results for the targeted nodes in terms of various combinations of the different states of the

other impacting factors can be obtained through forward inference. Here, we do not discuss all the prediction results due to limited space.

Subsequently, the "SAL2 MV Accident = True" state is configured as the targeted state. In this way, one can assess the contribution degree of each influential factor to train-MV accident occurrence through reverse inference. Detailed results are given in Fig. 6. It is worth noticing that accidents caused by inappropriate motorist behavior contribute to $80 \%$ to the entire train-MV accidents at SAL2 LXs, while accidents caused by static factors contribute to only $17 \%$. As for inappropriate motorist behavior, "Zigzag Violation" is more significant than "Stall on LX" in terms of causing train-MV accidents, because of the contribution of $58 \%$ (compared with $42 \%$ contribution of "Stall on LX"). On the other hand, in terms of static factors, when a train-MV accident occurs at an SAL2 LX, this LX has the probabilities of $74 \%, 38 \%, 44 \%, 37 \%$ and $46 \%$ respectively involved in the most risky situations that "Corrected Moment" in the "CM_49_up" group, "Railway Speed Limit" in the "RSL_110_up" group, "Width" in the "W_6_up" group, "Length" in the "L_11_up" group and "Region Risk" in the "R_high" group. These results indicate that more attention needs to be paid to LXs having the above risky characteristics. Moreover, special accommodation and/or technical solutions need to be implemented to prevent motorist zigzag violations. For instance, transforming SAL2 LXs into SAL4 LXs (Four-half barrier systems) or SAL2F LXs (two-full barrier systems), or installing median separators between opposing lanes of road traffic in front of SAL2 LXs. As for the consequences caused by accident, it is most likely to be 0 fatality $(P(F=F . .0)=0.8875)$, less than 2 severe injuries $(P(S=S . .0 .2)=0.9789)$ and less than 3 minor injuries $(P(M=M . .0 . .3)=0.9664)$. Thus, to a large extent, the consequence severity would be Level 1 $(P(C S=$ Level_1) $=0.8396, P(C S=$ Level_2) $=0.0292, P(C S=$ Level_3) $=0.0181, P(C S=$ Level_4) $=0.0006$ and $P(C S=$ Level_5) $<0.1125)$. Hence, one can set various states of the consequence nodes as the targeted states to make thorough corresponding diagnosis of causal factors through reverse inference.

# 6.2. Influence and sensitivity analysis 

Based on the BN risk model, the influence strength (IS), which represents the impact level of parent nodes on their respective child nodes, can be computed through GeNIe tool using Euclidean distance (Koiter, 2006). Fig. 6 shows the normalized influence strength (labeled on the arcs) between each pair of parent and child nodes. Fatalities (1) has stronger influence on consequence severity than severe injuries ( 0.5000 ) and minor injuries ( 0.4800 ). Moreover, inappropriate motorist behavior ( 0.7099 ) impacts more on LX accident occurrence than static factors ( 0.2899 ). Among the static factors, the influence level of the region risk factor, Alignment, Corrected Moment, Width, Length, Railway Speed Limit and Profile on LX accident occurrence decreases progressively. The result is consistent with that in the article (Liang et al., 2018a). The reason for the slightest impact of Profile is that on the one hand, the "hump or cavity" profile would cause an increasing risk of accidents involving long/heavy vehicles (trucks, buses, etc.), with relatively low population. On the other hand, for most of ordinary cars, such a profile obliges ordinary cars to cross the LX with low speed, which helps reducing the risk of LX accident occurrence (Liang et al., 2018a). In addition, zigzag violation ( 0.1143 ) impacts more on LX accident occurrence caused by inappropriate motorist behavior, compared with the impact of "stall on LX" (0.0137). The detailed impact of prolonged LX closure time, LX location and road traffic density on motorist behavior is analyzed in our article (Liang et al., 2017c). Further static and time-dependent factors shall be investigated when we will have to investigate the potential reasons for motorist violation, in the future.

Furthermore, the sensitivity analysis is performed to interpret the sensitivity of $P(S A=$ True $)$ to various conditional probabilities of different variable combinations. The Sensitivity Tornado Diagram (STD) is shown in Fig. 7. The top horizontal axis represents the values of $P(S A=$ True $)$. The vertical axis represents the general prediction value of $P(S A=$ True $) \approx 0.0061$, which is set as the datum axis. The horizontal bars are viewed as two parts divided by the datum axis. Green bars represent the values of $P(S A=$ True $)$ decreasing from the datum value while red bars represent the values of $P(S A=$ True $)$ increasing from the datum value, according to the changes of impacting conditional probabilities $\left(P_{c}\right)$. As the values of $P_{c}$ change within the interval $\left[P_{c}-0.1 P_{c}, P_{c}+0.1 P_{c}\right]$ (setting the spread degree as 0.1 ), the values of $P(S A=$ True $)$ change within an interval $\left[P(S A=\right.$ True $\left.)_{\min }, P(S A=\right.$ True $\left.)_{\max }\right]$ and distribute with respect to the changing values of $P_{c}$ in the whole range $\left[P_{c}-0.1 P_{c}, P_{c}+0.1 P_{c}\right]$ accordingly. Here, the values of $P(S A=$ True $)$ change within the interval $[0.0045,0.1055]$.

Fig. 7 shows the top 10 impacting $P_{c} \mathrm{~s}$ which $P(S A=$ True $)$ is most sensitive to. One can notice that $P(S A=$ False $\mid S F=$ False, $M B=$ False $)$ impacts $P(S A=$ True $)$ most. Namely, $P(S A=$ True $)$ decreases from 0.1055 to 0.0059 as $P(S A=$ False $\mid S F=$ False, $M B=$ False $)$ increases from 0.8999 to 1 . As for the $P_{c} \mathrm{~s}$ related to motorist

![img-3.jpeg](img-3.jpeg)

Fig. 6. Cause diagnosis when a train-MV accident occurs
behavior, $P(M B=\operatorname{False} \mid$ Stall $=\operatorname{False}, Z V=\operatorname{False})$ (taking the second place) impacts $P(S A=\operatorname{True})$ most, compared with the other $P_{x} \mathrm{~s}$ related to motorist behavior. As for the $P_{y} \mathrm{~s}$ related to static factors, $P(S A=\operatorname{True})$ is most sensitive to $P(S F=\operatorname{False} \mid R=R \_$high, $A=\operatorname{Straight}, W=W, 6 \_u p, P=\operatorname{Normal}, C M=C M, 49 \_u p, L=$ $L \_11 \_u p, R S L=R S L \_110 \_u p)$ (taking the sixth place), compared with the other $P_{y} \mathrm{~s}$ related to static factors. These results further attest that the LX accident occurrence is more sensitive to inappropriate motorist behavior than static factors. Moreover, as for motorist behavior factors, the LX accident occurrence is most sensitive to zigzag violation occurrence, compared with other motorist behavior factors. On the other hand, as for static factors, the LX accident occurrence is most sensitive to the riskiest states of various static factors. Therefore, the improvement measures need to be targeted on mitigating the above high-sensitivity factors, since a small scale of improvement in such factors can potentially reduce the LX risk as a whole on a large scale.

# 7. Conclusions 

In the present study, an effective and comprehensive modeling framework for risk reasoning, called BNI-RR, is proposed, which consists of a set of integrated processes, namely risk scenario definition, real field data collection and processing, BN model establishment and model performance validation. The output of our study offers a valuable

![img-4.jpeg](img-4.jpeg)

Fig. 7. Sensitivity tornado diagram.
support for decision making regarding LX safety. Although the BNI-RR framework is applied to the risk analysis of French LXs in our study, this framework is a general approach that can be applied to different contexts related to risk analysis.

The main contributions of the present study are as follows:

1) A causal semantics definition is proposed to describe the DAG of BN, which consists of three elements, namely $I F, T H E N$ and $C A K$. Thus, causal structural constraints are introduced based on the concept of $C A K$ for the purpose of causality optimizing. With the help of causal structural constraints, empirical knowledge can be integrated to distinguish causalities from correlations. Therefore, inappropriate connections are neglected so as to facilitate highlighting the main causes leading to LX accidents.
2) Based on the causal BN model, we were able to make forward inference and reverse inference, which are two valuable complementary means for performing inductive and deductive diagnosis. For instance, our BN risk model allows us not only to predict the probability of accident occurrence, but also evaluate the related consequence severity level, quantify the respective contribution degrees of various factors to the overall risk and identify the riskiest factors. These aspects are rarely achieved in existing related works and demonstrate the effectiveness of utilizing our BNI-RR framework.
3) Influence strength analysis and sensitivity analysis are two further approaches that were adopted to finely investigate the influence strength of causal factors on consequence factors and determine which causal factors the consequence factors are most sensitive to. Based on the obtained results, adequate targeted technical solutions and improvement recommendations can be identified to act on specific causal factors.

To sum up, the aforementioned contributions show that the BNI-RR approach offers an integrated modeling and analysis framework that allows for performing thorough risk analyses. The findings obtained through applying the BNI-RR framework on LX risk analysis offer a significant perspective on the major factors causing LX accidents and pave the way for identifying practical design measures and improvement recommendations to prevent accidents at LXs. In future works, dynamic BNs (DBNs) (Murphy, 2002) will be considered for further modeling the temporal situation of some of the considered constraints nodes (railway traffic, road traffic, etc.) to improve the risk analysis prevision, while the time-dependent conditional probabilities can be obtained. Besides, while the Bayesian Networks framework is based on the probability theory, some other approaches for knowledge representation were also developed in the past decades, considering several mathematical approaches for modeling uncertainty. If the belief functions theory (Shafer, 1976) was proposed as a competitive alternative to probabilities, we can also refer to Shenoy's work that proposed a formal mathematical framework for representing and reasoning with knowledge, named Valuation-Based

Systems (VBS) (Shenoy, 1976). The graphical representation of such formalism, named valuation network (Shenoy, 1994), offers a notation that allows for capturing any uncertainty calculations. The formalism is presented by Shenoy as an abstraction of probability theory, belief function theory and possibility theory. However, compared with the aforementioned frameworks, DBNs can perfectly meet our expectations w.r.t the potential extensions of this work.

In addition, since inappropriate motorist behavior has been identified as the main cause of LX accidents, a thorough analysis of this issue (e.g., further analysis on the possible influence of static and time-dependent factors on motorist behavior with more field data) combining both qualitative and quantitative techniques will be carried out to determine the adequate countermeasures.

# Acknowledgements 

This work has been in the framework of "MORIPAN project: MOdèle de RIsque pour les PAssages à Niveau" within the Railenium Technological Research Institute, in cooperation with the National Society of French Railway Networks (SNCF Réseau) and the French Institute of Science and Technology for Transport, Development and Networks (IFSTTAR).
