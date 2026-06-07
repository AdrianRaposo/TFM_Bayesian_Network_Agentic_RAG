# LJMU Research Online 

## Wang, $L$ and Yang, $Z$

Bayesian network modelling and analysis of accident severity in waterborne transportation: A case study in China
http://researchonline.ljmu.ac.uk/id/eprint/10397/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Wang, L and Yang, Z (2018) Bayesian network modelling and analysis of accident severity in waterborne transportation: A case study in China. Reliability Engineering and System Safety, 180. pp. 277-289. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Bayesian network modelling and analysis of accident severity in waterborne transportation: a case study in China 

Likun Wang ${ }^{1}$, Zaili Yang ${ }^{2}$

1. College of Transport and Communication, Shanghai Maritime University, Shanghai, China
2. Liverpool Logistics, Offshore and Marine Research Institute, Liverpool John Moores University, Liverpool, UK


#### Abstract

The rapid development of the shipping industry requires the use of large vessels carrying highvolume cargoes. Accidents incurred by these vessels can lead to a heavy loss of life and damage to the environment and property. As a leading country in international trade, China has developed its waterway transport systems, including inland waterways and coastal shipping, in the past decades. A few catastrophic shipping accidents have occurred during this period. This paper aims to develop a new risk analysis approach based on Bayesian networks (BNs) to enable the analysis of accident severity in waterborne transportation. Although the risk data are derived from accidents that occurred in China's waters, the risk factors influencing accident severity and the risk modelling methodology are generic and capable of generating useful insights on waterway risk analysis in a broad sense.

To develop the BN-based risk model, waterway accident data are first collected from all accident investigation reports by China's Maritime Safety Administration (MSA) from 1979 to 2015. Based on the derived quantitative data, we identify the factors related to the severity of waterway accidents and use them as nodes of the risk model. Second, based on a receiver operating characteristic (ROC) curve, an augmented naïve $\mathrm{BN}(\mathrm{ABN})$ model is selected through a comparative study with a naïve $\mathrm{BN}(\mathrm{NBN})$ model to analyse the key risk factors influencing waterway accident severity. The results show that the key factors influencing waterway safety include the type and location of the accident and the type and age of the ship. Moreover, a novel scenario analysis is conducted to predict accident severity in various situations by combining different states (e.g., high risk) of the key factors to generate useful insights for accident prevention. More specifically, the findings can aid transport authorities, ship owners and other stakeholders in improving waterborne transportation safety under uncertainty.


## 1. Introduction

Waterborne transportation is vital for sustaining national economic development given its capability of providing cheaper and greener solutions compared to other transport modes. For instance, over the past several years, China's waterway (including both coastal and inland) shipping has been developing rapidly. By 2016, its waterway freight volume reached 6.382 billion tonnes, which was a $480 \%$ increase from 2001, and its water transport ship load capacity reached 266.22 million tonnes, 211.73 million tonnes more than that in 2001. Due to increasing shipping demand, waterway traffic density increases, and the navigational environment becomes complex, leading to

a high level of risk. It has been reported that in 2016 alone, 196 accidents occurred and 203 people died in China's waterways (Statistical Bulletin of Transportation Industry Development, 2017). Maritime accidents cause casualties, economic loss, environmental degradation and waterway congestion (Zhang et al. 2013). Compared to ocean transportation, ships used in inland and coastal waterways are smaller, and their ability to tackle emergencies is lower. Hence, the probability and severity of the accidents that involve these ships are probably higher. It has been found that larger Danish-flagged cargo ships often suffer fewer accidents (Danish Maritime Authorities, 2010). Hansen, Jepsen, and Hermansen (2012) concluded that vessels smaller than 3000 GT put their crews at great risk of being in a maritime accident, which requires the crews of such vessels to abandon ship more frequently than those of large vessels. Statistics from the Maritime Accident Investigation Branch (MAIB) in 2010 disclosed that the risk of the total loss of a small ship is much higher than that of a large vessel. This paper therefore aims to analyse the characteristics of shipping accidents involving small vessels in inland and coastal waterways and, based on a data-driven Bayesian network (BN), to identify the important risk factors influencing accident severity for risk prediction and accident prevention. The accident data used in this study are obtained from the accident investigation reports by China's Maritime Safety Administration (MSA) over the past 30 years. Accidents that occurred in China's inland and coastal waterways are selected, and those associated with deep-sea transportation are eliminated. The term "accident" in this paper refers to both accidents and casualties, as defined by the International Maritime Organization (IMO).

This paper is organised as follows. Section 2 describes the current literature relating to maritime accidents, with a focus on maritime risk assessment using BNs. In Section 3, the method and results of accident data mining are presented. Section 4 presents the methodology of developing a BN-based risk model for the analysis of waterway accidents. In contrast to previous relevant studies that rely, more or less, on expert judgments to interpret subjective probabilities, the novelty of the methodology lies in the use of data-driven approaches to identify key risk factors and quantify their interdependencies. There are no studies in the literature that analyze all accident investigation reports of a particular country/region (e.g., China) over a long time span (e.g., 30 years). In Section 5, the BN model verification is conducted by comparing two models based on different BN calculations. Section 6 describes the scenario analysis for drawing useful findings in terms of risk prediction and accident prevention. Conclusions and future work are discussed in Section 7.

# 2. Literature review 

### 2.1 Studies of maritime accidents

Previous studies on maritime accidents involve a wide variety of geographical locations, including the Gulf of Finland (Mazaheri, Montewka, and Kujala 2014), Istanbul Strait (Aydogdu, 2014), the UK (Chauvin et al. 2013; Bhattacharya, 2012), Greece (Tzannatos and Kokotos, 2009), Sweden (Mullai and Paulsson 2011), the heritage regions of Tubbataha and Banc d'Arguin (Heij et al. 2013), the Arctic (Kum and Sahin 2015), the North Atlantic and Arctic regions (Knapp, Bijwaard, and Heij 2011), and China's Yangtze River (Zhang et al. 2013; Zhang et al. 2014).

Ship accidents are caused by equipment failure, human error, environmental effects, excessive loads, or a combination of these factors (Guedes Soares and Teixeira, 2001; Antao and Guedes Soares, 2008). The integration of established and novel techniques to assess risks is a current goal within many maritime organisations. The application of probabilistic methods to model some of

these high risks is a current practice because it has potential to help in the process of decision making, which would allow regulatory changes to be proposed (Guedes Soares and Teixeira, 2001)

Some papers set natural weather conditions as one of various variables that influence ship accidents (Zhang et al., 2013; Mullai and Paulsson, 2011; Balmat et al., 2009), whereas Knapp et al. (2011) focus on oceanographic conditions. This paper uses econometric models to measure the effect of significant wave height and wind strength on the probability of vessel casualty, and the results show that the probability of vessel casualty is influenced by seasonality, wind strength and wave height.

It is commonly stated that $80 \%$ of all accidents are associated with human factors (Antao and Guedes Soares, 2008). Several human factor analysis models have been introduced and widely used, such as the Human Factors Analysis and Classification System (HFACS), the Technique for Retrospective and Predictive Analysis of Cognitive Errors (TRACEr), the Cognitive Reliability and Error Analysis Method (CREAM) and Accident Analyse Mapping (AcciMap). Chen et al. (2013) established a maritime incident analysis framework using HFACS-MA. Akyuz (2015) assessed human factors in ship grounding accidents with AcciMap. Sotiralis et al. (2016) calculated the collision accident probability due to human error with TRACEr and BN. Yang et al., (2013), Wu et al. (2017) and Xi et al., (2017) proposed different modified CREAM based on evidential reasoning to estimate the human error probability in maritime accidents.

Reviewing these studies reveals that although diverse causes of accidents are presented in different routes/locations, common risk factors influencing the occurrence probability or consequence severity of accidents exist; these are presented in Table 1. The analysis of such causes and factors aids the analysis of the initial set of risk variables in this study.

Table 1
Variables from the relevant literature



Maritime accident risk models often involve quantitative analysis. The IMO proposed a formal safety assessment (FSA) method for risk management in maritime accident analysis. The FSA method is a systematic approach to ship accident analysis that considers ship condition, organisational management, human operation and hardware (Guedes Soares and Teixeira, 2001).

To further compute the causal relationships among the above factors, some quantitative risk assessments are provided in maritime accident research. For example, fault-tree analysis (FTA) has been used to analyse the causes of maritime accidents (Ronza et al. 2003, Kum and Sahin 2015). Antao and Guedes Soares (2006) used the FSA method to identify basic events that could lead to a Ro-Ro vessel accident, and they built an FTA model to analyse the relation between the relevant events. Recently, Zhang et al. (2013) used the FSA method to analyse ship accident consequences in the Yangtze River and then used the BN tool for quantitative analysis. In addition, Fabiano et al. (2010) proposed summarised statistics for evaluating accident frequency over time or certain risk control levels. Balmat et al. (2011) evaluated maritime risk assessment based on a fuzzy-logic approach.

Maritime accident data are available from established datasets and accident investigation reports. Among the most often used historical datasets are Lloyd's Register Fairplay, Lloyd's Maritime Intelligence Unit, and the IMO. The contained statistics consist of ship names, ship registries, accident dates and times, types of casualties, consequences, locations, ship types, gross tonnages, classification societies, dead weights, and injured or dead people. Lloyd's data normally cover ships larger than 100 gross registered tons and thus omit a large percentage of fishing vessels (Guedes Soares and Teixeira, 2001).

Heij et al. (2013) used the accident statistics of Lloyd's Register Fairplay, Lloyd's Maritime Intelligence Unit and the IMO. Wu et al. (2015) used accident statistics of the Yangtze River MSA, and Weng and Yang (2015) used shipping accident statistics managed by Lloyd's List Intelligence Company.

Accident investigation reports are a useful way to obtain more complete accident data. The investigation reports of maritime accidents are often available from maritime authorities, such as the MAIB of the UK, the MSA of China, and the Transport Safety Board of Canada. These reports provide much more detailed information than existing databases and contain details of what occurred, subsequent actions taken and recommendations. In the present literature, few studies use accident investigation reports to conduct accident analysis, and even fewer use them to conduct quantitative risk analysis simply due to the large workload required to aggregate the data from each report for a dataset of meaningful critical mass. For instance, from cases of high-speed craft

accidents, Antao and Guedes Soares (2008) found the chain of events that led to the accidents and their associated contributory factors and causes. With the taxonomy of the TRACEr method, Graziano et al. (2016) coded and analysed grounding and collision accidents investigation reports to identify human and organisational errors (HOFs). Chauvin et al. (2013), Akhtar and Utne (2014), and Chen et al. (2013) analysed accident reports of selected cases to investigate maritime accident HOFs.

The data collection and analysis method based on accident reports, though time consuming, will no doubt bring new findings and rich information that cannot be easily obtained from existing databases and facilitate the use of primary data in maritime accident analysis. Its novelty is also highlighted by feeding such information into an advanced BN model for enabling risk prediction and accident prevention, instead of discussing the importance of individual factors based on basic statistical analysis. It will therefore help the authors generate new findings in this study region, in contrast to previous relevant studies, which rely on data derived from the same/similar sources.

# 2.2 Use of BN in maritime accident analysis 

Despite such efforts, the uncertainty (e.g., incompleteness and randomness) in historical failure data in the maritime industry stimulates the use of advanced techniques in risk assessment. For instance, the IMO considered the incorporation of BN modelling in risk quantification in FSA studies (Yang et al., 2013a). BNs have been used in waterway transport accident research due to their advantages, including their usefulness in conducting backward risk diagnosis and forward risk prediction and in accommodating new evidence to update an analysis without the need to significantly change the original network (Yang et al., 2009; 2013b).

In applying a BN in maritime accident analysis, the first challenge is to construct the BN structure. Normally, a BN is constructed with aid from data correlation, expert knowledge, a literature review, or a combination of the above (Zhang, 2016). Trucco et al. (2008) presented a BN of maritime accidents with human and organisational factors, which was an extension of the fault tree. With the aid of experts in the maritime and petroleum industries, a BN was obtained to predict the risk of maritime piracy against offshore oil fields (Bouejla et al. 2014). Based on the available data from the Maritime Authority (DGAM), expert knowledge was consulted for the construction and validation of the BBN model (Antao and Guedes Soares, 2008). With the suggestions of six selected experts who were consulted to identify major factors influencing the likelihood of a successful hijacking of a ship, a BN model was developed to estimate the likelihood of a ship being hijacked in the Western Indian or Eastern African regions (Pristrom et al. 2016). With a combination of statistics and expert knowledge, Zhang et al. (2016) built a Bayesian belief network to express the dependencies between the indicator variables and the consequences of the Tianjin port accident.

When BN structures are developed from data using a machine learning algorithm, there is a possibility that the generated casual relationships are unreasonable and ambiguous. Previous studies have used expert knowledge or a taxonomy model to optimise such structures. Zhang et al. (2013) estimated navigational risks on the Yangtze River using a BN technique; the preliminary structure of the BN was obtained from data via the necessary path condition algorithm, and additional domain knowledge was referenced to further consolidate the structure. Ma et al. (2016) presented a BNbased target-extraction method to extract moving vessels from numerous blips captured in frame-by-frame radar images; at the beginning, an initial BN structure was established based on expert judgment and was then improved with the help of a K2 scoring algorithm. Akhtar and Utne (2014)

developed a Bayesian causal network to analyse maritime accidents using the qualitative model (HFACS) and its taxonomy for structuring fatigue-related factors into levels, which decreased the number of links (correlations) in need.

To avoid the subjectivity associated with expert input in BN modelling, two plain machine learning algorithms, the naïve $\mathrm{BN}(\mathrm{NBN})$ and the augmented $\mathrm{NBN}(\mathrm{ABN})$ (Friedman et al., 1997), are applied in this study because of their demonstrated efficiency and capability. With the core idea of classification, the NBN and ABN models can be built to simplify BN structures without sacrificing the accuracy of the model.

Previous studies in which a BN was applied to maritime risk tended to focus on the probabilities of shipping accidents rather than their severity, and accident data were frequently obtained directly from existing databases rather than compiled from investigation reports. The novelty of this study is its attempt to construct a BN from primary data directly derived from accident investigation reports containing rich information that fits the specific requirement of this study.

Furthermore, we extract influencing factors and the nature of waterway transportation accidents from accident investigation reports using text mining techniques. The text mining method has a wealth of applications in other disciplines, such as enterprise management and sociology (Glaser, 1992). However, the use of this text coding approach in maritime risk data elicitation, such as in Mullai and Paulsson (2011), is scant. To develop a rational BN structure, we use and compare the NBN and ABN algorithms to select the best-fit BN structure with specific evaluating indicators.

# 3. Data mining 

### 3.1 Data acquisition

We collected 229 accident investigation reports from Chinese coastal waterways and inland rivers from China's MSA and its fourteen subordinates. As many as 350 vessels were involved in these reported accidents from 1979 to 2015. Each report includes a description of the ship(s), crew, ship companies, accident location, navigational environment, accident process, losses, and an analysis of the cause.

With regards to severity, a maritime accident can be classified as a catastrophic accident, a critical accident, a major accident or a minor accident (MoT, 2002). Their explanations are detailed in Table 2.
Table 2
Classification of the consequences of accidents



Source: Regulation of Water Transportation Accident Statistics, Ministry of Transport (MoT), China, 2002.

# 3.2 Coding 

The grounded theory (GT) method is a systematic methodology involving the discovery of theory through the analysis of data (Glasser and Strauss, 1967). Selective reduction is the kernel of GT. Using the GT method, we stepwise process the 229 text cases collected from MSA by coding, conceptual formulation, categorisation and repeated comparisons to extract the influencing risk factors and their effects on waterway transport accidents. The specific process is described as follows.
(1) Coding: we read the original case reports word by word and sentence by sentence to encode the data. We mark the sentences in the original text that involve the consequences of each waterway accident and the related risk factors.
(2) Conceptual formulation: We borrow the concepts of the existing literature or use the report analyst's language, and we group the marked sentences into similar concepts of the related risk factors and the consequences of the waterway accidents.
(3) Categorisation: We study all cases repeatedly, and we make constant comparisons between the reported cases. We unify concepts of the same meaning to form the categories at higher levels of abstraction. Then, we retrieve the ultimate accident-related categories, which are presented in Table 3. In this process, the attributes and their categorisation in previous studies (in Table 1) are used as a reference.
(4) Attribution: According to the categories in Table 3, we obtain the related attribute values of each case. Finally, we obtain a database with 350 records with 21 columns.
(5) Relationships recognition: When contrasting explanations (i.e. causal relationships) appear, one solution is to use domain expert evaluations with reference to the mainstream explanations in the literature. If the experts argue the explanations opposite to the mainstream ones, extra justifications are needed. The other is to mark the contrasting explanations, in order to test the sensitivity in the model validation process.

Fig. 1 presents the ships involved in the accidents. It shows that accidents involving bulk cargo ships occur most frequently, as found by Zhang et al. (2016), followed by container ships, and more than $50 \%$ of the catastrophic accidents involve bulk cargo ships. The frequencies of the other variables are presented by the percentage values attached at each state of them in Table 3.
Table 3
Categories



*The flag of convenience (FOC) refers to vessel registry in the following locations: Panama, Limassol, Kingston,

Valletta, Belize, Majuro, Cyprus, Phnom Penh, Cambodia, and Willemstad.
** The maritime accidents were divided into eight types, i.e., collision, contact, standing, grounding, fire/explosion, sinking, wind strike and other, according to the Regulation of Water Transportation Accidents Statistics provided by the MoT (2002).

In the subsequent quantitative analysis, accident severity is defined as a dependent variable, the other categories in Table 3 are treated as influencing variables, and the attributes correspond to the variable states. ${ }^{1}$
![img-0.jpeg](img-0.jpeg)

Fig. 1. Percentage of each ship type involved in minor, major, critical, and catastrophic accidents.

# 4. Use of BN modelling to analyse the severity of maritime accidents 

BN theory was introduced by Pearl (1988) and can be expressed as the following pair: $S=<G$, $P>. G$ is a directed acyclic graph, the nodes in the network correspond to the variables, the tangential arc refers to the causal relationship between variables, the directional arc from node $X$ to node $Y$ indicates that $X$ has a direct causal effect on $Y$, and the conditional probability $P(Y \mid X)$ represents the intensity of the causal effect.

$$
P(Y \mid X)=P(X \mid Y) \cdot P(Y) / P(X)
$$

$P(Y)$ is the prior probability of the hypothesis, i.e., the likelihood that $Y$ will be in a certain state, prior to consideration of any other relevant information (evidence), which is $X . P(X \mid Y)$ is the conditional probability (the likelihood of evidence given the hypothesis to be tested), and $P(Y \mid X)$ is the posterior probability of the hypothesis (the likelihood of $Y$ being in a certain state, conditional on the evidence provided) (Akhtar and Utne 2014).

The development of a BN model includes the following steps: BN structure learning, BN monitoring and analysis and model validation, sensitivity analysis, estimation and evaluation (Zhang et al. 2013).

Two methods are available for developing the structure of a BN. One method is the use of expert knowledge. Its disadvantage is that some causal relationships are not easily analysed or are expressed subjectively. An alternative method for BN construction is to develop the network

[^0]
[^0]:    ${ }^{1}$ The entire process was conducted in Chinese given that the accident investigation reports were all in this language. The identified categories were later translated to English for this paper.

structure and parameter estimation by data-driven machine learning methods and use experts to validate the final structure to assure the meaningfulness of the relationships. Considering the availability of the historical data derived from the accident reports, data-driven BN approaches are applied in this study. A significant drawback of the data-driven approach is that the number of possible structures for a given problem increases super-exponentially with the number of variables in the problem domain (Yang et al., 2018).

NBN and the ABN can reduce the complexity given that the partial structure of the network is fixed. An NBN is a simple structure that has an independent node as the parent node of all the other nodes, and no other connections are allowed in the structure. However, strong assumptions are required in most NBN cases. To make the model more realistic, we adopted an ABN model, whose architecture consists of a naïve architecture that is made richer by basing the ties between the child nodes on the value of the target node. Since ABN is based on NBN, the latter is introduced first.

# 4. 1 NBN learning 

An NBN is a network structure in which the target node is directly connected to all other nodes and each child node is independent of the other nodes. The NBN structure is generated by specification. The NBN model is most commonly applied to classification problems (Friedman et al., 1997).
a) Let 'accident severity' be the class variable $(S)$ with one state for each possible state, and let $\quad R=\left\{R_{S T}, R_{H T}, R_{S A}, R_{S F}, R_{L e}, R_{G T}, R_{S S}, R_{S D}, R_{L}, R_{C}, R_{L o}, R_{R}, R_{F}, R_{V}, R_{w}, R_{s}, R_{T D}, R_{N E}\right.$, $\left.R_{H F}, R_{A T}\right\}$ be the set of risk variables $\left(R_{k}\right)$ (i.e., ship type, hull type, ship age, ship flag, length, gross tonnage, ship speed, ship defects, loading, crew, location, rain, fog, visibility, wind, season, time of day, navigational environment, human factors, and accident type, respectively), where each variable represents a property that we observe and include in our model.
b) Given the simplicity and strong assumption of the pairwise independence of the attributes, two types of structures can be obtained to describe the relationships between $S$ and $R_{k}$.

Fig. 2(a) shows the first structure, in which $R_{k}$ is the parent node of 'accident severity', and 'accident severity' is the only child of each risk factor node and no other structure. In our study, the 'accident severity' of four states can be assigned to $S$, and it has 20 influencing variables, each of which can be assigned to more than one state, as in Table 3. For any set of observations $R=$ $\left\{R_{S T}, R_{H T}, \cdots, R_{A T}\right\}$, the complexity of computing the conditional probability distribution $P\left(S \mid R_{S T}, R_{H T}, \cdots, R_{A T}\right)$ is non-linear, and there may be more than $2 \mathrm{E}+09$ conditional probability distributions that need to be computed (the size of the conditional probability table increases exponentially with the number of parents).

Let 'accident severity' have no parents, and let it be the only parent of each feature variable. Fig. 2(b) shows the second structure; $S$ is the only parent of each child node. The structure consists of the prior distribution $P(S)$ and 65 conditional probability distributions $P\left(R_{k} \mid S\right)$. This classifier algorithm is much simpler, and it can be used to express the relationship between variables. In this paper, we adopt the structure in Fig. 2(b) as the NBN structure.

![img-1.jpeg](img-1.jpeg)

Fig. 2(a). BN converging structure with 'accident severity' as a child node.
![img-2.jpeg](img-2.jpeg)

Fig. 2(b). BN diverging structure with 'accident severity' as the parent node.
c) Estimate the conditional probability distribution as follows:

$$
P\left(S \mid R_{S T}, R_{H T}, \mathrm{~L}, R_{A T}\right)=P\left(S \mid R_{k}\right)=\frac{P(S) \prod_{k=1}^{\alpha} P\left(R_{k} \mid S\right)}{\prod_{k=1}^{\alpha} P\left(R_{k}\right)}
$$

# 4. 2 ABN learning 

The ABN consists of an NBN enriched by the relationships between the child nodes and the value of the target node (the common parent). The ABN modelling technique is implemented as follows.
a) Generate a Naïve Bayes structure with the target node (e.g., 'accident severity') directly connected to all other nodes $\left(R_{k}\right)$.
b) Create different ABN structures by changing the parameter of the structural coefficient $(\alpha)$. Set $0<\alpha \leq 1$ and let $N^{\prime}=N / \alpha$, where $N$ is the number of samples in the dataset $(0<\alpha \leq 1)$. Given different values of $\alpha$, assume that the relationship between child nodes $\left(R_{k}\right)$ is allowed to exist by fixing the links from the target node $(S)$ to the children $\left(R_{S T}, R_{H T}, \cdots, R_{A T}\right)$. With the aim of the minimum description length score (Lam, Bacchus 1993), a greedy search algorithm among the children is used to obtain the augmented part of the ABN given different values of $\alpha$.

$$
M D L(B, D)=\alpha D L(B)+D L(D \mid B)
$$

where $B$ represents the ABN , and $D$ represents the dataset given to ABN $B$.
c) Evaluate the structure/data ratios of different ABN structures, where the structure/data ratios are $D L(B) / D L(D \mid B), D L(B)$ is the description length of the ABN , and $D L(D \mid B)$ is the description length of the data given the ABN.

The structure/data ratios allow us to consider the structural complexity and predictive performance of the network. The lower the value of $\alpha$ is, the higher the value of $D L(B) / D L(D \mid B)$ will be. In other words, when $\alpha$ equals 0.1 , the ABN structure in Fig. 3(a) is more complex than the structure with $\alpha=1$ in Fig. 3(b), and the target predictive precision of $\operatorname{ABN}(\alpha=0.1)$ is higher than that of $\operatorname{ABN}(\alpha=1)$. After comparing the structure/data ratios under different $\alpha$, an ABN structure $(B)$ will be selected with a satisfied trade-off between predictive performance versus network

complexity.
![img-3.jpeg](img-3.jpeg)

Fig. 3(a). ABN structure with $\alpha=0.1$
![img-4.jpeg](img-4.jpeg)

Fig. 3(b). ABN structure with $\alpha=1$
d) Estimate the conditional probability distribution as follows:

$$
P\left(S \mid R_{S T}, R_{H T}, \mathrm{~L}, R_{A T}\right)=\frac{P(S) \prod_{k=1}^{\infty} P\left(R_{k} \mid \pi\left(R_{k}\right)\right)}{\prod_{k=1}^{\infty} P\left(R_{k}\right)}
$$

where $\pi\left(R_{k}\right)$ denotes the parents of node $R_{k}$.

# 4.3 Model verification 

The types of construction validity tests for BN models include nomological, face, content, concurrent and convergent validity, qualitative features and the sensitivity test (Pitchforth and Mengersen, 2013; Mazaheri, 2016; Sotiralis et al., 2016). In this paper, the NBN structure is fixed by nature, so the structure and parameters need not be checked. In contrast, during the process of ABN structure learning, the model content verification will be done. In section 5.2, three domain experts were interviewed to verify the parameters and their relationships in the ABN model. The sensitivity test is described in detail in sections 4.4 and 6.2 .

In addition, this paper uses the receiver operating characteristic (ROC) curve to verify the model from the data statistics view. ROC is a plot of the true positive rate (Y-axis) against the falsepositive rate (X-axis), and the ROC index represents the surface under the ROC curve divided by the total surface. For the different BN models, we use the indicator of the ROC curve to evaluate the fitness of the NBN and ABN models in this paper.

### 4.4 Sensitivity analysis

Sensitivity analysis is a common method of uncertainty analysis used to quantify the uncertainties associated with relevant variables. Sensitivity analysis is useful for increasing our

understanding of the relationships between input and output variables (Wu et al. 2015). Because the nodes in this study are categories listed in Table 3, mutual information(MI) is used to compute the strengths of the relationships between the target node (i.e., severity) and influencing nodes (i.e., risk variables), and the value of the target node is computed under different states of the influencing nodes, which share a large amount of mutual information with the target node.

One of the key advantages of mutual information $I(Y, X)$ is that it can be computed between categorical variables. It measures how much (on average) the observation of a random variable $y$ tells us about the uncertainty of $x$, i.e., by how much the entropy of $x$ is reduced if we have information on $y$. If $I(Y, X)>0$, then the association between $y$ and $x$ is strong; if $I(Y, X) \approx 0$, then the association is weak, and $y$ and $x$ occur simultaneously only by chance; and if $I(Y, X)<0$, then $y$ and $x$ are complementary, and there is no association. The mutual information between 'accident severity' and other risk variables can be defined as

$$
I\left(S, R_{k}\right)=\sum_{r_{k} \in R_{k}} p\left(r_{k}\right) \sum_{s \in S} p\left(s \mid r_{k}\right) \log _{2} \frac{p\left(s \mid r_{k}\right)}{p(s)}
$$

where $s$ represents each state of 'accident severity', $r_{k}$ represents each state of the risk variables, and $I\left(S, R_{k}\right)$ represents the mutual information shared between 'accident severity' and the waterway accident risk variables in this paper.

For the risk variable, which has a strong relationship with 'accident severity', a sensitivity analysis to determine how the risk variable affects 'accident severity' is performed as follows.

The value of the target node (e.g., 'accident severity') is computed when the state of one child node (e.g., risk variable) is assigned different values, and the states of the other child nodes are locked. In other words, for a specific $k$, where $R_{k}$ has a strong relationship with $S$, we set $R_{k}$ to a different state $i$, then compute the joint probability $P\left(S=j, R_{k}=i\right)$ and the mean value $E\left(S, R_{k}=i\right)$.

$$
\begin{aligned}
& P\left(S=j, R_{k}=i\right)=P(S=j) \times P\left(R_{k}=i \mid S=j\right) \\
& E\left(S, R_{k}=i\right)=\sum_{j} j \times P\left(S=j, R_{k}=i\right)
\end{aligned}
$$

# 5. BN structure learning 

### 5.1 NBN structure learning

Assuming that all the child nodes are independent, we can construct an NBN as shown in Fig. 4 .

![img-5.jpeg](img-5.jpeg)

Fig. 4. NBN structure

# 5.2 ABN structure learning 

(1) Structural coefficient

We set the structural coefficient ( $\alpha$ ) equal to $\{0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1\}$. The relationship between $\alpha$ and the structure/data ratio is presented in Fig. 5; the X -axis represents $\alpha$, and the Y-axis represents the structure/data ratio.
![img-6.jpeg](img-6.jpeg)

Fig. 5. Representation of Structure/Data Ration variation for different values of the Structural coefficient (a).

The complexity of the structure increases with a decreasing structural coefficient. This complexity becomes problematic when it increases more rapidly than the predictive precision. Visual inspection suggests that there could be a trade-off (e.g., the sharp bend of the curve) between the predictive performance and the network complexity when $\alpha$ is equal to 0.3 .
(2) Content validity

In addition, in the process of learning the structure in ABN , the common sense, accident report and expert knowledge should be used to ensure the rational causal relationships between the BN nodes. Hanninen, Kujala (2014) used prior knowledge to forbid some arcs while using a hillclimbing algorithm to learn a BN structure in ship accidents. With reference to Hanniene Kujala's work, when learing the ABN structure in this work, we consider the following prior knowledge to

argue the casual relationships which are not harmony with the current understanding learnt from the literature.

- 'Ship type' should have no relationships with 'Ship age' and 'Ship flag'; 'Ship age' should have no relationships with 'Ship flag', 'Length', 'Gross tonnage'; 'Ship flag' has no relationships with 'Ship flag', 'Length', 'Gross tonnage';
- Ship static characteristics (e.g., 'Ship type', 'Hull type', 'Ship age', 'Ship flag', 'Length', 'Gross tonnage') should have no relationships with accident environment states (e.g., 'Rain', 'Fog', 'Visibility', 'Wind'), the ship loading state (e.g., 'Loading'), the crew seaworthiness (e.g., 'Crew'), and accident time and location (e.g., 'Location', 'Season', 'Time of day');
- 'Ship defect' or 'Crew' should have no relationships with 'Rain', 'Fog', 'Visibility', 'Wind', 'Season', 'Time of day', 'Ship speed' and 'Navigational environment';

Using the above prior knowledge to prohibit relevant arcs, we obtain a BN structure from data with the ABN algorithm $(\alpha=0.3)$, as shown in Fig. 6(a). The arc orientation is the opposite of the causal relation for low computational complexity (4.1). It is observed that 'Ship speed $\rightarrow$ Time of day', 'Loading $\rightarrow$ Navigational environment' and 'Length $\rightarrow$ Human factors', is not consistent with the actual situation because accident time will not influence ship speed. In addition, it can be shown that navigational environment has a small consequence for ship loading situation, also the human factors should have a small consequence for ship length.
![img-7.jpeg](img-7.jpeg)

Fig. 6(a). ABN model structure with initial forbidden arcs.
![img-8.jpeg](img-8.jpeg)

Fig. 6(b). ABN model structure with additional forbidden arcs 'Ship speed $\rightarrow$ Time of day', 'Loading $\rightarrow$ Navigational environment', 'Length $\rightarrow$ Human factors'.

Therefore, we adjust the ABN structure with additional forbidden arcs of 'Ship speed $\rightarrow$ Time of day', 'Loading $\rightarrow$ Navigational environment', 'Length $\rightarrow$ Human factors'. As a result, the revised structure is shown in Fig. 6(b); the arc 'Accident type $\rightarrow$ Time of day' in Fig.6(b) is not consistent

with the actual situation, and we forbidden this arc and adjust the ABN structure, and the updated structure is shown in Fig. 6(c).
![img-9.jpeg](img-9.jpeg)

Fig. 6(c). Final ABN structure with additional forbidden arcs 'Accident type $\rightarrow$ Time of day'.

# 5.3 ROC curve 

We use the indicators of ROC to evaluate the fitness of the different BN models. The results are shown in Table 4.
Table 4
Degrees of fit of the models


The ROC value of the ABN model is higher, indicating that this model yields a better result. Thus, we select the $A B N$ model (Fig. 6(c)) for the subsequent data analysis.

## 6. Model results

### 6.1 Prior probability distribution of the BN model

Fig. 7 shows the initial prior probability distributions of the factors involved in the adjusted ABN.

![img-10.jpeg](img-10.jpeg)

Fig. 7. The prior probability distribution of the adjusted BN model
The classical statistical analysis of these data provides some initial findings, including:
In the shipping accidents occurring in the coastal and inland waters of China, collision was the type of accident with the highest probability: $60.27 \%$. Dry bulk cargo vessels accounted for the largest percentage (i.e., $51.42 \%$ ) of shipments involved in accidents. Ships younger than 5 years were involved in the largest percentage (i.e., $44.63 \%$ ) of accidents. The majority of vessels involved in accidents, $63.70 \%$, were less than 100 m long. Gross tonnages in the range of $300-10000$ accounted for $61.46 \%$ of the ships involved in accidents.

With respect to the safety of the ships, $22.70 \%$ of the vessels involved in accidents had deficiencies or failed to conduct safety inspections, $7.92 \%$ were overloaded, and $20.87 \%$ had an insufficient number of crew members or a crew member with an incomplete or invalid certificate.

In terms of navigational environment, rain was present in $21.69 \%$ of the accidents, fog in $19.96 \%$, and poor visibility in $17.30 \%$. In addition, $42.14 \%$ of the accidents occurred between November and the following March, $64.38 \%$ occurred at night time, and $74.74 \%$ occurred in waterways with shipping congestion and other poor navigational environments.

# 6.2 Sensitivity analysis (SA) 

### 6.2.1 Most relevant variables of the target node

Fig. 8 shows the amount of mutual information shared between 'accident severity' and the other risk variables. The sizes of the nodes are proportional to the amount of mutual information shared with the target node given the available evidence.

Given that 'accident severity' is the target node, the variable 'accident type' has the strongest effect on the accident severity: the corresponding amount of mutual information is 0.1542 . Certain variables yield values of $I\left(S, R_{k}\right)$ exceeding 0.05 and thus have a significant effect on 'accident severity'; these variables are 'accident type', 'location', 'ship type' and 'ship age'. Additional variables that yield values of $I\left(S, R_{k}\right)$ greater than 0.02 but less than 0.05 , i.e., 'ship flag', 'ship speed', 'time (of day)', 'visibility', 'gross tonnage', 'environment', 'crew', 'season' and 'wind', also had a significant effect on 'accident severity'.

The variables 'ship defects', 'loading', 'fog', 'hull type', 'human factors', 'rain' and 'length' had a relatively weak effect on 'accident severity'.
![img-11.jpeg](img-11.jpeg)

Fig. 8. Mutual information shared with the target node (the size of the node is equal to the MI value)

### 6.2.2 Sensitivity analysis with respect to the target node

The variables 'accident type', 'location', 'ship type' and 'ship age' had their MI values higher than 0.05 with 'accident severity'; thus, we compute the effect of these four nodes on the target node.

In accordance with the ABN model described in Fig.9(a), we assign 'accident type' a state of 1 ('collision'). Consequently, the joint probability of $P\left(S=1, R_{A T}=1\right)$ is 0.1733 , $P\left(S=2, R_{A T}=1\right)=0.1465, P\left(S=3, R_{A T}=1\right)=0.2090$, and $P\left(S=4, R_{A T}=1\right)=0.4713$; then $E\left(S, R_{A C}=1\right)=2.9785$. The joint probabilities and the mean value show that when the accident is a collision, the severity of the waterway accident tends to be critical.

Similarly, the mean value and joint probabilities are obtained and presented in Figs. 9(a) to 9(d): the X -axis represents the state of a risk variable, the left Y -axis represents the mean value of 'accident severity', and the right Y-axis represents the joint probabilities of $j$ th 'accident severity' state with $i$ th state of each risk variable (e.g. accident type, location, ship type, ship age) .
![img-12.jpeg](img-12.jpeg)

Fig. 9(a). Mean values of 'accident severity' against different accident types, and the posterior probability of each state of 'accident severity' with respect to different accident types.

Fig. 9(a) shows that when the accident is a sinking, the 'accident severity' tends to be the highest, at a value of 3.237 . When a grounding occurs, the probability of 'minor accident' is the highest, and the mean probability of 'accident severity' is the lowest, which means that the waterway 'accident severity' tends to be minor.
![img-13.jpeg](img-13.jpeg)

Fig. 9(b). Mean values of 'accident severity' in different locations, and the posterior probability of each state of 'accident severity' in different locations.

Fig. 9(b) shows that when the accident occurs at a quay or a port channel, the mean values of accident severity is low. When the location is an anchoage, an inland or coastal waterway, the severity of the accident tends to be catastrophic.
![img-14.jpeg](img-14.jpeg)

Fig. 9(c). Mean values of 'accident severity' against different ship types, and the posterior probability of each state of 'accident severity' with respect to different ship types.

The severity of the waterway accident involving fishing vessel tends to be the highest: 3.456 . When the ship is hauling passengers, dry bulk cargo or a barge/tug, then the mean value of 'accident severity' are $2.801,3.007,3.310$, respectively. If the ship is a tanker, container ship, or ro/ro vessel, then the mean value of 'accident severity' are lower: $2.705,2.657$, and 2.501 , respectively.
![img-15.jpeg](img-15.jpeg)

Fig. 9(d). Mean values of 'accident severity' against different ship ages, and the posterior probability of each state of 'accident severity' with respect to different ship ages.

With increasing ship age, the severity of accidents generally rises. However, a 6-10 years ship tends to be safer than one aged $0-5$ years, probably because a new ship has a certain run-in period.

Ships aged 16-20 years tend to be slightly less safe than those more than 20 years.

# 6.3 Implications: Scenario analysis 

The model enables analysis of the severity of waterway accidents based on various scenarios involving different natural and navigational environments and vessel managerial conditions. Two scenarios are undertaken focusing on the environment and vessel management to demonstrate the possible research implications of the BN model.

### 6.3.1 Scenario one: Hypotheses of natural and navigational environment aspects

In scenario one, waterway risk under specific environmental conditions is estimated. Here, environmental factors, including 'season', 'wind', 'rain', 'fog', 'the time of day (TD)', and 'navigational environment (NE)', are chosen. The variables are assigned the following states: 'season' = 'winter', 'wind' = 'greater than 7 on the Beaufort scale', 'rain' = 'rain', 'fog' = 'fog', 'time' = 'night time', and 'environment' = 'high traffic density or other poor navigational environment'. Assuming that one or more than one of the above natural and navigational environment situations occurs, and considering that strong winds and heavy fogs, or heavy rain and heavy fog do not usually happen simultaneously, we obtain 40 combinations of different environmental conditions. If we fix the other variables in the ABN structure as constant (i.e. lock the evidence), we can computer the increasing percent of the posterior probability of "catastrophic" accident severity under 40 different combined conditions, respectively.

Any combination leading to over $30 \%$ increase is shown in Fig. 10. It is obserbed that a remarkable increase in accident severity compared to the initial state when the wind is strong; it is noted that the rain itself could not lead to serious accident severity, but when rain occurs with wind, the ship accident severity will increase significantly. In the meantime, the highest marginal contribution to ' $\mathrm{AS}=4$ ' comes from 'wind $=$ greater than 7 , time of day $=$ night, navigational environment $=$ poor $"$.

Obviously, all stakeholders should pay great attention when encountering poor navigational environments, especially severe weather conditions, given their significant effect on the accident severity.

![img-16.jpeg](img-16.jpeg)

Fig. 10. Posterior probabilities increasing by $30 \%$ for catastrophic accidents in scenario one.

# 6.3.2 Scenario two: Hypotheses of vessel managerial aspects 

In scenario two, the critical safety characteristics of vessels are identified to demonstrate how better monitoring and management can be undertaken to reduce risks. The variables representing aspects of vessel management in this scenario are assigned to the following designations or values: 'crew' = 'sufficiently staffed with valid certificates', 'ship defects' = 'no defects' and 'ship speed' 'smaller than 5 knots'. The drop percentages of mean values of the node 'accident severity' in scenario two is shown in Fig. 11. When the crew is sufficiently staffed, the ship has no defects, and the ship speed is slow, the mean value of accident severity decreases by $10 \%$ compared to the initial state. These values indicate a significant decrease in risk. The results indicate that the reduction of hidden managerial dangers can significantly reduce the severity of the accidents.
![img-17.jpeg](img-17.jpeg)

Fig. 11. Decreased percent of mean values of 'accident severity' in scenario two arranged in decreasing order.

# 7. Conclusions 

In this study, we extracted useful data from maritime accident investigation reports for risk analysis using the GT method and BNs. We analysed the reports of waterway accidents held by MSA in the past 30 years and then identified and analysed the causal factors influencing waterway transport accidents. A novel BN model was constructed to analyse waterway risks using ABN modelling.

Based on the mutual information contained in the ABN model, the risk variables are grouped and ranked according to their degrees of closeness to the node of accident severity in the following order: Among Group I (i.e. mutual information higher than 0.05 ) are accident type, location, ship type and ship age; Group II (i.e. mutual information greater than 0.02 but less than 0.05 ) includes ship flag (registry), ship speed, time of day, visibility, gross tonnage, environment, crew, season and wind; and Group III (i.e. mutual information less than 0.02): ship defects, loading, fog, hull type, human factors, rain and length.

From the analysis, useful insights are obtained as follows:
(i) When the type of accident is a sinking, the severity of the accident is the highest, and when the type is a grounding, the accident severity is the lowest.
(ii) When the accident occurs at a quay, the risk of serious consequences is the lowest. When the location is an inland or coastal waterway, the average severity is the highest, and the severity of the waterway accident tends to be catastrophic.
(iii) when the ship is a fishing vessel, the severity of the accident is the highest among all vessel types;
(iv) with increasing ship age, the accident severity generally increases.

The ABN model and the scenario analysis help investigate whether oceanographic conditions influence risk and if these effects change over time. The relevant findings will provide useful guides to the stakeholders, including ship operators to take better safety control options (with respect to the most influencing risk factors) to eliminate/reduce accident consequences; and policymakers (e.g. classification societies) to set new safety standards (e.g. design for safety with respect to the most ship-related influential risk factors).

The analysis of two scenarios reveals that navigational environments and ship management have significant effects on accident severity. Heavy winds obviously lead to serious accident severity. At night, heavy wind creating a poor navigational environment, causes the significant increase of the probability of a catastrophic accident. When the crew is sufficiently staffed, the ship has no defects, and the ship speed is slow, the mean value of accident severity decreases by $10 \%$. Obviously, such analysis results suggest appropriate way of developing countermeasures for accident prevention.

Despite the above contributions and findings, the paper has shown some limitations, among which the significant includes

1) The completeness of the data mined from the text case is arguable. More sources should be used to compensate the missing data.

2) In BN modelling, we used the Expectation Maximization (EM) algorithm to process missing data. This method is time costly. In future, advanced methods could be developed to improve its efficiency.
3) The study focuses more on objective variables and concerns little on human factor. Data relating to human factor and its impact on maritime accident severity should be derived from the accident reports to address this concern in future.

# Acknowledgements 

This research is sponsored by the Shanghai Pujiang Program (Grant No. 5PJC060), the National Science Foundation of China (Grant nos. 71573172 and 71402093), and the EU H2020 MC RISE programme (Grant No. GOLF-777742)
