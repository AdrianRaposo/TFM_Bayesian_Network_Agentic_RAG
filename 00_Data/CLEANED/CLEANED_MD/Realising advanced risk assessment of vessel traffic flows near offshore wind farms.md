# LJMU Research Online 

Yu, Q, Liu, K, Chang, C-H and Yang, Z

## Realising advanced risk assessment of vessel traffic flows near offshore wind farms

## http://researchonline.ljmu.ac.uk/id/eprint/13299/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Yu, Q, Liu, K, Chang, C-H and Yang, Z (2020) Realising advanced risk assessment of vessel traffic flows near offshore wind farms. Reliability Engineering \& System Safety, 203. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Risk assessment of the collisions between vessels and wind turbines 


#### Abstract

: Offshore wind farms (OWFs) are relatively new installations at sea. Accident records related to vessel collisions with OWFs are insufficient to support a full quantitative risk analysis using traditional probabilistic approaches. This paper aims to develop a semi-qualitative risk model to assess the vesselturbine collision risks by incorporating Bayesian networks (BN) with evidential reasoning (ER) approaches. First, a BN is trained based on Automatic Identification Systems (AIS) data to characterise real vessel traffic flows, including the detailed information and relationships between traffic flow parameters. Secondly, through synthesising expert judgements by ER, five risk factors influencing the probability and consequence of vessel-turbine collisions are identified (incl. the associated conditional probabilities) in the established BN. Finally, the updated BN with ER input is tested through ten real scenarios and validated by processing a validity framework. This paper pioneers the use of multi-datadriven BNs to characterise traffic flows and assess vessel-turbine collision risk for navigational safety assurance near OWFs. The research findings provide empirical evidence of using ER to supplement BN subjective data to advance its applications in risk analysis.


Keywords: AIS data, offshore wind farm, Bayesian network, maritime safety, maritime risk, evidential reasoning, ship collision

## 1. Introduction

The increasing demand of green energy promotes the construction of offshore wind farms (OWFs). The growing OWFs affect navigational safety, as they are often installed in the waters near shores, where established shipping routes with intensive traffic exist (Yu et al., 2020). A new OWF installation will affect vessel traffic flows during the period of its construction. Its operations and maintenance will also increase navigational complexity, causing the possible collisions between vessels and offshore wind turbines (V-T collision) with a consequence of the potential damage on vessel/turbine structures, oil leakage, sinking of vessels or collapse of OWF turbines (Presencia and Shafiee, 2018; Wu et al., 2018). To deal with such risks, it is essential to conduct risk assessment and to simulate the interactions between vessel traffic flows and OWF activities. However, the historical data (e.g. collision accidents) in this field is scanty (Mehdi and Schröder-Hinrichs, 2016), which makes it difficult to use classical quantitative risk analysis (QRA) methods. Information from other sources such as automatic identification system (AIS) and expert judgement had been used to complement accident data in maritime risk analysis previously. They include the estimation of a collision probability based on AIS data (Mujeeb-Ahmed et al., 2018), the degree of impact of OWF installations

on ship routes (Yu et al., 2020), and the severity of V-T collisions by subjective risk models (Staid and Guikema, 2015). Although showing attractiveness, using indirect data sources to evaluate V-T collision still reveals some problems in their practical applications. For instance, processing AIS data with statistical analysis is very time-consuming, it requires complex data cleansing and classification process to reduce the uncertainty in AIS data. The subjective risk models are arguable given that it is difficult to establish a bias-free correlation among risk influential factors (RIFs) purely using expert judgements (Hooper et al., 2017; Presencia and Shafiee, 2018). As a result, a generic approach that can rapidly process data and develop a reliable risk model based on multiple data sources relating to ship traffic flow and possible collisions with OWFs is required with urgency.

To overcome the abovementioned difficulties, this study proposes a hybrid risk analysis approach (i.e. $B a L E R$ ) to tackle V-T collision risk and to provide the relevant empirical evidence. The BaLER approach firstly aids to construct a data-driven Bayesian network (BN) from AIS data to characterise the navigation environments of the traffic flows in the vicinity of OWFs. Next, subjective judgements are used to identify the RIFs and evaluate the V-T collision risk under different environments. Evidential reasoning (ER) is used to synthesise the subjective evaluations from multiple experts and the aggregated data is transformed into conditional probability tables (CPTs) by applying a rule-based approach (Yang et al., 2009b). After the development of the baseline model with multiple data sources, BaLER helps analyse and prioritise the risk levels of different scenarios involving V-T collision possibilities, identify the key RIFs through sensitivity analysis, and conduct a ratio analysis to generate useful insights and rich implications for V-T collision avoidance. By doing this, one new feature of this hybrid approach is to combine AIS data and subjective judgements in a complementary way for the new formulation of a multi-data-driven BN-based risk analysis method. Another new contribution is to train maritime risk BNs with AIS data by using a target-free data learning approach.

The remainder of this paper is organised as follows. Section 2 reviews the current challenges in the maritime and offshore risk analysis, with a focus on the use of a Bayesian approach. In Section 3, a hybrid risk analysis approach is developed by combining a BN for model training and ER for expert judgement synthesis. In Section 4, BaLER is applied to model the V-T collision to draw empirical evidence to support a multi-data-driven BN in maritime risk analysis. In Section 5, a series of cases are undertaken with a baseline model to find useful research implications of identifying the critical situations in the V-T collision risk. In Section 6, the BN is validated and finally, the conclusion is drawn in Section 7.

# 2. Literature review 

### 2.1 Risk definitions

In the risk field, various types of risk definitions are proposed and each of them computes risk from different perspectives. One of the most formal and well-established definition to describe risk $(R)$ is to multiply probability of risk $(P)$ and consequence of severity $(C)$, i.e. $R=P \times C$ (Rausand, 2013).

However, risk is a complex and interdisciplinary concept with a variety of variables involved in addition to the probability and consequence, such as uncertainty, exposure and scenarios (Aven, 2012). To better describe risk, Kaplan and Garrick (1981) quantify risk with a risk triplet, which defines risk by three variables (i.e. $R=(P, C, S)$ ), where $S$ is explained as under a specific scenario. Aven (2012) suggests that a subjective risk assessment should also consider limitations of background knowledge $(B K)$, and defines risk as $R=(P, C, U, B K)$, where $U$ represents uncertainty of data.

In line with Bayes risk theory, Lindley (1970) and Singpurwalla (2006) suggest risk is a problem that should be measured by considering evidence and observations. Different from probability risk theory, variables of prior probability and conditional probability are used in the Bayes risk theory to demonstrate a frequentist probability. Thus, risk can be revised to a model with a set of subjective prior evidence and conditional probabilities, reflecting risk is a dynamic concept under different conditions when different evidence is introduced into the probability model.

In this paper, we use the risk parameters by Aven (2012) to develop our model in which both P and C are considered in the BN directly while the $U$ is addressed by CPTs in BN and $B K$ is described by incompleteness in ER. To accommodate both objective and subjective data in the same framework, risk measures for $C$ and $P$ are expressed well established linguistics terms which are often used to define subjective risks.

### 2.2 Challenges on data in OWF risk analysis

Newly built offshore installations have several potential impacts on wildlife, natural environment and navigational safety (Kim et al., 2018). Their impact on V-T collisions is a major issue among the navigational effects of OWFs (Petersen, 2015). Previous research works were carried out for V-T collision consequence analyses and V-T collision mechanisms (e.g., Dai et al., 2013; Bela et al., 2017; Presencia and Shafiee, 2018). However, the difficulty of identifying risk situations is highlighted as data of V-T collision accidents is scanty and hard to access (Presencia and Shafiee, 2018).

An alternative way of analysing the risk is to characterise traffic flows by using statistical analysis or geometrical analysis based on AIS data. Several studies used AIS data to assess the impact of offshore

installations on vessel traffic in different regions, such as Thames Estuary (Rawson and Rogers, 2015), the Penghu waterway (Chang et al., 2014) and the south coast of Busan (Mujeeb-Ahmed et al., 2018). Yu et al. (2020) compared the vessel traffic flows before and after OWF installations in the China southern coast to examine the degree of impact of these new installations. A framework, including AIS data filtering, mixture-Gaussian-based traffic flow modelling approach and traffic flow statistical analysis models, was applied to analyse the AIS data collected before and after the OWF installations. The results quantitatively characterised the impacts of the OWFs on marine traffic flows and showed that the impacts were diverse based on various factors (e.g. ship type categories, season). It provided useful insights on vessel traffic characteristics nearby the OWFs and identified the important factors that had significant impact on vessel-turbine collision risk. Mujeeb-Ahmed et al. (2018) used a geometric causation probability model to estimate the collision probabilities with respect to vessels under different categories, and then evaluated the collision risk based on statistical results of traffic flows. The obtained results did not show any statistically significant increase in the frequency of V-T collisions. Copping et al. (2016) compared the likelihoods of commercial vessel accidents in existing shipping routes from historical AIS data, and proposed the routes in the presence of wind farms along the Atlantic coast using a numerical simulation model. Although these studies provide insightful findings on the OWF impacts on traffic flows, the drawbacks of using AIS data are also revealed. For instance, statistical analysis is inefficient and the geometric causation probability model is unable to give precise results since the causation probabilities are general and may not suitable to modelling a specific navigational environment.

Subjective data is an alternative resource to overcome the above shortcomings by supplementing the risk evaluation through experience (e.g. expert judgements). A multiple data-driven risk model can be presented through hierarchy or network techniques (e.g. BNs) by modelling the interrelationships among variables (e.g., Dai et al., 2013; Staid and Guikema, 2015). When using subjective data, uncertainties and personal biases should be tackled appropriately by applying rational aggregation and conversion approaches (e.g. ER) (Yang et al., 2009b).

# 2.3 Use of BNs in maritime and offshore risk analysis 

BNs are widely used in maritime safety studies because of their visualisation and capability of realising bi-directional (i.e. forward prediction and backward diagnosis) risk analysis. Furthermore, BNs can accommodate both objective and subjective data to form conditional probabilities to describe the interdependency among the nodes (i.e. risk factors) in the networks (Yang et al., 2018a). The application of a BN in risk analysis normally includes the following steps: (i) determining RIFs in a

BN; (ii) constructing a qualitative graphical network; (iii) inputting the quantitative dependencies among the variables; and (iv) computing the results of risk assessment. Serval studies have applied BNs in maritime risk assessment (e.g. Trucco et al., 2008; Zhang et al., 2013; Montewka et al., 2014; Wu et al., 2017; Bye and Aalberg, 2018; Wang and Yang, 2018). For the development of BN models, some studies construct BN from hierarchical structures (e.g. Sotiralis et al., 2016; Afenyo et al., 2017) and prove that BNs are superior as they combine multiple state variables and aggregate probabilistic values from interdependent variables to better present the uncertainty in data. There are also some studies of quantifying maritime risk via BNs, such as ship-ship collision risks and oil spill from tankers (Goerlandt and Montewka, 2015), marine transportation in arctic waters (Khan et al., 2018; Baksh et al., 2018), influential variable analysis on ship collision (Hänninen et al., 2012), human errors on different ship accidents (Antão and Soares, 2019) and decision making in transportation policy (Ulengin et al., 2007).

It is revealed that in many of the aforementioned studies, developing BNs from subjective/objective data requires a large amount of information on prior probabilities and conditional probabilities. The size of CPTs will exponentially increase when the network becomes larger and more complex (Zhang et al., 2013). Therefore, BNs have been combined with other approaches (e.g. fuzzy logic) for advancing risk modelling ability to tackle uncertainty in data (e.g. Yang and Wang, 2015; Zhou et al., 2018; Wan et al., 2019).

# 2.4 Data-based Bayesian learning approaches 

Bayesian learning approaches are introduced to reduce the high requirement on prior probabilities on constructing BNs from data and improve the reliability of the structure. To train BNs from objective data, the approaches often use one of two Bayesian classifier theories: the dependency analysis theory or the search and score theory. The dependency analysis theory is developed by Spirtes and Glymour (1991), and it evaluates the dependency of each variable in data and defines relationships on the basis of dependency values. However, it is difficult to use this theory to design a BN structure with a small amount of data when an extensive independency relation test is carried out (Singh and Valtorta, 1995). In contrast, the Bayes-based search and score approach proposed by Cooper and Herskovits (1992) is relatively common, involving many applications such as tree-augmented naive Bayes, the Bayesian search (K2) and the augmented naive Bayes approaches (Friedman et al., 1997). This approach explains how to identify a BN structure from the candidates that can best represent the causality and dependency by scoring all possible structures.

A Bayesian learning approach is considered as a well-established tool for the BN construction in risk

assessment that can fill the gap between modelling and reality. Wang and Yang (2018) used different Bayesian learning approaches to develop BNs from data of 229 maritime accidents in Chinese waters and compared the obtained BNs that trained with different Bayesian learning approaches. Yang et al. (2018b) used a tree-augmented naive Bayesian learning approach to train a BN from a set of port state control records, the obtained BN was then analysed to support port control decision making. When applying the Bayesian learning approaches to maritime safety assessment, they normally require the input data to be associated with a specific target factor (e.g. risk degree, collision risk) and some of the learned dependencies in a BN structure may be inconsistent with reality and require subjective modifications based on the user's knowledge.

# 3. Methodology 

This paper proposes a novel model to investigate the collisions between ships and offshore wind turbines by taking into account the relevant factors such as traffic flow information (e.g. number of passing ships, ship types, traffic density), ship characteristics (e.g. ship speed, ship size, time), ships' passing distances, safety area of OWFs and seasons.

For the abovementioned propose, this section describes a new data-driven BN approach (BaLER) for V-T collision risk analysis. The first step is to train a data-driven BN from historical AIS data to characterise traffic flows by using a target free Bayesian learning approach. In the second step, the obtained BN is supplemented with new risk nodes (i.e. collision probability, collision consequence and collision risk) involving subjective prior probabilities that are obtained by using an ER approach to synthesise judgements from multiple experts. Meanwhile, the nodes in the BN are prioritised with the aid of sensitivity analysis. In the last step, the evaluations are used to prioritise the risk under different navigation environments, and critical situations are identified through an advanced ratio analysis. Figure 1 shows a flowchart consisting of all the necessary steps in BaLER.

### 3.1 Constructing a data-driven BN from AIS data

### 3.1.1 Acquiring, filtering and classifying AIS data

AIS data provides a considerable amount of information on traffic flows and can be obtained from various sources such as maritime authorities or commercial companies. To train a BN with AIS data, the data should be filtered to ensure their integrity. Ten variables are obtained from the AIS data, including 'ship category', 'length', 'beam', 'depth', 'displacement', 'speed', 'course' 'season', 'day/night' and 'minimum passing distance', in which the first seven variables are directly acquired from the data; 'season' and 'day/night' are converted from the raw AIS data; and 'minimum passing distance' is calculated by a closed point approach, which is introduced by Yu et al. (2020).

![img-0.jpeg](img-0.jpeg)

Figure 1. Framework of the BaLER approach in V-T collision risk analysis
Meanwhile, a set of linguistic states is assigned, with reference to previous studies, domain expert experience and/or relevant regulations/practice, to each variable in the AIS data to transform continuous data into a discrete mode.

# 3.1.2 Learning a BN from AIS data 

In a BN, relationships among variables are qualitatively described by directional arc and quantitatively defined by conditional probabilities. Generally, the relationships are defined based on background knowledge. It is difficult to avoid biases and uncertainties exist in subjective judgements (Pitchforth and Mengersen, 2013). To overcome this issue, this study applies a machine learning approach to develop a data-driven BN based on the collected AIS data to model vessel traffic flows near OWFs. A Bayes-based learning approach is carried out to generate a network that both directional arc and conditional probabilities are determined from the collected data. A Bayesian searching approach (BSA) determines the relationships between variables (qualitative relationships) and a 'Bayes estimator' calculates conditional probabilities among variables (quantitative relationships) (Cooper \& Herskovits, 1992; Ma et al., 2016).

BSA is applied to train a network structure as it requires no pre-definition of any target factor before

training (Cooper \& Herskovits, 1992). As the AIS data only record ships' dynamic/static states, it does not contain a target factor, thus a target free learning approach can best fit the requirements. BSA evaluates all possible belief network structures based on a database under the conditions of 'how likely the case is to occur if a system uses a specific structure' and 'how the dependencies are described with the given structure and evidence'. In this study, this approach is explained within the context of vessel traffic flows. Assuming AIS data provides a variable set $X$ that contains $m$ discrete variables $x_{i}(i \in$ $m$ ) to describe traffic flows characteristics. Let a variable $x_{i}$ has $n$ possible states as $\left(v_{i}^{1}, v_{i}^{2}, \ldots, v_{i}^{n}\right)$, a AIS database $D$ contains $N$ records, each of which contains a value assignment for each variable in $X$. There are $h$ possible BN structures $\left(B_{1}, B_{2}, \ldots, B_{h}\right)$ that describe interrelationships between traffic flow variables, and each structure represents a unique interrelation between variables that are identified from the AIS database $D$. In a specific $B_{c}(c \in h), x_{i}$ has a set of parent nodes, which can be presented with a list of variables as $l$. There is a total of $r$ instantiations in the $l$ and the $j$ th $(j \in r)$ unique instantiation relative to $D$ is $l_{j}$. Then we define $N_{i j k}(k \in n)$ to be the number of records in $D$ in which variables $x_{i}$ has the value $v_{i}^{k}$ and $l$ is instantiated as $l_{j}$. Meanwhile, the sum of $N_{i j k}(k \in n)$ is defined as $N_{i j}=\sum_{k=1}^{n} N_{i j k}$. After defining the above parameters, BSA calculates the likelihood $P\left(B_{c} \mid D\right)$ for $B_{c}$ in the $D$ by using Eq. (1) and (2):

$$
P\left(B_{c} \mid D\right)=\frac{P\left(B_{c}, D\right)}{\sum_{c=1}^{h} P\left(B_{c}, D\right)}
$$

where

$$
P\left(B_{c}, D\right)=P\left(B_{c}\right) \prod_{i=1}^{m} \prod_{j=1}^{r} \frac{(n-1)!}{\left(N_{i j}+n-1\right)!} \prod_{k=1}^{n} N_{i j k}!
$$

and $P\left(B_{c}\right)$ is a constant prior probability for each $B_{c}$. In this way, the structure that obtains the highest score is selected to be the most likely BN structure 1 .

The CPT of each node can be calculated when the most likely $B_{c}$ is selected. Assuming that the conditional probabilities $O_{i j k}$ for $v_{i}^{k}$ in $x_{i}$ are consistent with the Dirichlet distribution, a 'Bayes estimator' $E$ can be used to calculate $O_{i j k}$ for $v_{i}^{k}$ under $B_{c}$ and $l_{j}$ in $D$. This gives the following equation (Cooper and Herskovits 1992):

$$
E\left(O_{i j k} \mid D, B_{c}\right)=\frac{N_{i j k}+1}{N_{i j}+n}
$$

where $E\left(O_{i j k} \mid D, B_{c}\right)$ is the estimator value for $O_{i j k}$. By using a table to combine all

[^0]
[^0]:    ${ }^{1}$ A numerical example is provide in Appendix A for its demonstration.

$E\left(O_{i j k} \mid D, B_{c}\right)(k=1,2, \ldots, n)$ under $B_{c}$ in $D$, a CPT for $x_{i}$ is obtained.

# 3.1.3 Validating the data-driven BN 

A new data-driven BN requires a certain level of validation to ensure its reliability and soundness. This is important and desirable when a BN is generated from data learning. The validation of a BN can be carried out by comparing the simulation results from the BN with the real AIS data. Additionally, evaluations by domain experts can also provide a reasonable amount of confidence in the validity of a data-driven BN.

### 3.2 Supplementing the BN with subjective judgements

Subjective information (e.g. expert judgement) is introduced into the data-driven BN to supplement risk evaluations. For this purpose, necessary steps are carried out, including: (i) identifying the RIFs from the variables in the BN, (ii) introducing new risk nodes into the BN and assigning their linguistic states, (iii) acquiring and aggregating subjective information relating to the evaluation of the risk under different navigation situations, (iv) transforming the aggregated results into CPTs and developing a multiple-data-driven and BN-based risk model, (v) validating the risk model and (vi) analysing sensitivity of the key nodes (RIFs) in the obtained model.

### 3.2.1 Identifying the RIFs

In order to make an overall risk assessment on navigation environments meanwhile reduce the size of variables in the risk model, RIFs of collision risk are identified from the variables in the data-driven BN. Identification of the RIFs is very dependent on the field of model applications. For example, the vessel width is an important variable influencing vessel-bridge collisions, but not for V-T collisions. The identifications normally use information from expert judgements and/or previous studies to identify high-impact variables and these variables are selected as RIFs. Previous studies on relative ship accidents (e.g. grounding, collision) are first used to identify preliminary RIFs in this study. Then, domain experts are invited to evaluate the importance of the RIFs within the context of V-T collision and insignificant RIFs are eliminated.

### 3.2.2 Introducing new risk nodes

Three subjective variables are introduced into the data-driven BN, including two intermediate nodes (i.e. collision probability and collision consequence) and their child node (i.e., collision risk). Psychological research suggests 4-7 grades for exercising effective expert judgements (Guilford, 1954; Sii et al., 2001). 5 and 7 linguistic terms are widely used in maritime subjective risk analysis (e.g. Yang et al., 2009; Goerlandt and Montewka, 2014; Yang and Wang, 2015; Wu et al., 2018). 7 grades will

significantly increase the requirement of prior probability configuration, and hence a set of 5 grade linguistic states are assigned to three risk nodes as follows. The linguistic grades for the collision probability are 'very low', 'low', 'average', 'frequent' and 'highly frequent'; whereas those for the consequences are defined as 'negligible', 'marginal', 'moderate', 'critical' and 'catastrophic' (Yang and Wang, 2015). The collision risk is described by 'very low risk', 'low risk', 'average', 'high risk' and 'very high risk'.

The variables that are selected as the RIFs are connected with two intermediate nodes as the parent nodes by considering their diverse impact on collision probability, consequence or both.

# 3.2.3 Aggregating the judgements from multiple experts using ER 

After identifying the RIFs and introducing the subjective risk nodes, a certain navigation environment can be expressed with the RIFs by combining a specific linguistic state in each RIF. Two lists that cover all the state combinations are firstly developed for the purposes of traversing overall navigation environment and then used to collect the judgements of probability and consequence under each navigation environment from domain experts. An ER approach is employed to aggregate the judgements as it provides an alternative way of handling the uncertainty by converting both quantitative and qualitative information into the concept of degree of belief, so that the information can be systematically and consistently aggregated and modelled using a belief structure (Yang et al., 2009b). The latest ER algorithm for evidence aggregation is developed and presented in Yang and Xu (2002). Comparing with other aggregation mathematical/behavioural approaches (e.g. Delphi, linear opinion pool method), the ER approach shows the following advantages: 1) it can aggregate data when prior-knowledge is unavailable; 2) it is capable of dealing with uncertain data during aggregation; 3) the data's importance can be considered by assigning relevant important weight to data; 4) the aggregated results can be presented in a more precise way that contains states and relative assignment values (Zhang et al., 2013).

### 3.2.4 Transforming the aggregated result into conditional probabilities

The aggregated results are converted into CPTs by using a rule-based approach, which is an approach that describes causality between $I F$ and THEN parts in a rule. In this approach, a defined rule is used to convert $p$ attendance attributes $\left\{A_{1}, A_{2}, \ldots, A_{p}\right\}$ (IF part) into $q$ states $\left\{C_{1}, C_{2}, \ldots, C_{q}\right\}$ (THEN part) by assigning a belief degree $\beta_{s}(s=1,2 \ldots, q)$ to $C_{s}(s \in q)$ For example, the $w$ th conventional $I F$ THEN rule $R_{w}$ in a rule-based set can be expressed as:

$$
R_{w}: \text { IF } A_{1}^{w} \text { and } A_{2}^{w} \text { and } \ldots \text { and } A_{p}^{w}, \text { THEN }\left\{\left(\beta_{1}^{w}, C_{1}\right),\left(\beta_{2}^{w}, C_{2}\right), \ldots,\left(\beta_{q}^{w}, C_{q}\right)\right\}
$$

In the $w$ th rule, $R_{w}$, the IF part is a set of linguistic inputs $A^{w}=\left\{A_{1}^{w}, A_{2}^{w}, \ldots, A_{p}^{w}\right\}$. Under this situation, a set of belief degrees is assigned to the THEN part as $\left\{\left(\beta_{1}^{w}, C_{1}\right),\left(\beta_{2}^{w}, C_{2}\right), \ldots,\left(\beta_{q}^{w}, C_{q}\right)\right\}$ for the description of how each $C_{s}(s=1,2 \ldots, q)$ is believed to be the result of $\beta_{s}$ in the $R_{w}$, in which the $\beta_{s}$ can be assigned with experience or by using converting methods (e.g. equivalent influential method (Yang et al., 2009a)). Combining all rules of $R$, a multiple-input and multiple-output rule-based set can be developed.

In this study, three CPTs are established. Two CPTs to intermediate nodes (probability and consequence) are developed by converting the aggregated results with the rule-based approach and one CPT to the final node (collision risk) is obtained by combining risk influence from probability and consequence. Therefore, a multiple-data-driven BN risk model is developed by introducing the CPTs into BN.

# 3.3 Analysing the results 

The risk degrees under different navigation environments are prioritised with utility values, in which the results of probability distributions from a node in the BN are converted into crisp values $C R$ by using an utility function below (Wang and Yang 2018):

$$
C R=\sum_{z=1}^{t} P_{z} U_{z}
$$

where $t$ is the number of the linguistic variables that a node has. $P_{z}$ is the belief degree to the $z$ th linguistic variable of the target node (i.e. collision risk) in the $\mathrm{BN} . U_{z}$ is the synthesised utility value that assigned to the $z$ th linguistic variable. A linear distribution of utility values (from 1 the lowest and 9 the highest) is used to assign the values of the linguistic states (e.g. Yang et al., 2018a; Wan et al., 2019). Using the Equation 4, outputs from the risk model are converted into a crisp value to which the results are prioritised by ranking their $C R$ values, where a high $C R$ value represents a high collision risk level.

To realise a comprehensive risk assessment, a ratio analysis is introduced to incorporate the BN risk result of a specific navigation scenario and the proportion of the scenario occurred in reality (based on the AIS data). The analysis uses a ratio value $(R V)$ to represent the ratio of a particular navigation environment situation in the AIS database. By combining the ratio and collision risk of each navigation environments, a navigation situation with a high $C R$ and a high $R V$ is defined as a critical situation.

### 3.4 Validation

The BN-based risk model requires validation to check whether the model is robust and results are

reliable. This validation is especially important when subjective judgements are involved in generating conclusions. As claimed by Graham (1995), 'any determination that a risk has been "verified" is itself a judgement that is made on the basis of standards of proof that are to some extent arbitrary, disputable and subjective'. Most of the state-of-art validation approaches are based on a comparison between models and reality. However, It is difficult to apply contrast validation approaches for BN validity as the non-observable parameters in BN (e.g. collision risk) are presented as chance, not an observation value.

Therefore, uncertainty-sensitivity validation is often used to test a new BN risk model as it provides reasonable confidence on results. For this purpose, Aven and Heide (2009) distinguish the difference between frequency-based and Bayesian approaches to see the extent to which risk analysis meets the requirements of reliability and validity, and introduce some important principles and procedures to validate different risk models. Yang et al. (2009b) and Jones et al. (2010) suggest BNs should satisfy certain axioms in uncertainty-sensitivity analysis. For instance, 1) A slight increase or decrease in the prior probabilities of each parent node should cause a relative change in the posterior probability of the child/target node (e.g. collision risk). 2) Given the variation of subjective probability distributions of each parent node, the influence magnitude from these parent nodes to the child/target node values should reflect the weights of the parent nodes. 3) The total influence magnitudes of the combination of the probability variations from $\varphi$ attributes (evidence) on the values should be always greater than the one from the set of $\varphi-\omega(\omega \in \varphi)$ parent nodes. Pitchforth and Mengersen (2013) reviewed previous validity approaches and grouped the approaches into five types, while the complexity of validating a no-objective-data-based BN is discussed to show the needs of a novel framework for BN validation. Based on previous studies, Pitchforth and Mengersen proposed a psychometrics framework to validate BNs that is developed based on expert elicitations. The framework contained seven types of validity, which are nomological, face, content, concurrent, convergent, discriminant and predictive validity. This framework has been applied to validate the BNs in maritime risk assessment (e.g. Goerlandt and Montewka, 2014; Wang and Yang, 2018; Valdez et al., 2019).

In this study, our BNs are tested through multiple approaches to present their reliability and validity. First, a case study is undertaken to assess ten real scenarios using the proposed BN. Collision risk for each scenario is calculated and prioritised, while the obtained results are compared with direct intuitional judgements from domain experts to prove that the results are consistent with experience. Secondly, the BN is validated through a panel of experts to ensure it is consistent with their knowledge and experience. Experts are asked to provide judgements on whether the BN structure and the used nodes are sound. Thirdly, content validity is conducted through an entropy approach, which expresses

the information uncertainties between the target variable and other variables by computing the entropy reduction using a nonlinear function (Yang et al., 2018a). Since the objective of this study is to evaluate the collision risk, which is assigned as the target node. A higher entropy reduction value represents a higher importance of the associated variables. At last, the BN is tested by a sensitivity analysis to identify the essential navigational condition that has the highest collision risk in the investigated waters. For this purpose, every conditional and prior probability in the BN needs to be systematically changed from the lowest to highest in turn while locking the evidence of the others. It is time-consuming and difficult to manually process a test in a BN of many nodes and states, therefore, we used the GeNIe software to simulate all the possible scenarios and process this sensitivity analysis.

# 4. Applying BaLER in V-T collision analysis 

### 4.1 Collecting and processing AIS data

An OWF located off the south coast of China is selected as a real investigation case in this study. To train a data-driven BN, AIS data in the vicinity of the OWF is collected from the China Maritime Safety Authority. It includes four weeks data in each season in 2017, with total 638 records of vessels' trajectories. After filtering the incomplete records, 590 records are retained for BN training.

The states of variables are defined on the basis of supporting evidence to provide the best descriptions of traffic flow characteristics (see Table 1). Such evidence is further explained against each RIF in the ensuing section.
(1) Ship categories: The categorisation in the AIS system is used to define states of ship categories, which include: (i) 'general cargo vessel', (i.e. bulkers, general cargo ships and containers); (ii) 'oil and gas tanker', (i.e. oil tankers, LNG/LPG gas tankers, chemical tankers and other liquid and gas tankers); (iii) 'supply vessel', (i.e. tugs, maintenance ships, construction ships, OWF supply ships and other service ships); and (iv) 'fishing vessel'. Ferries and passenger ships are not included in this study, as there are no records in the database.
(2) Minimum passing distance: The states of the minimum passing distance refers to the UK recommendation MGN 543 (Maritime and Coastguard Agency, 2016). It defines the minimum passing distance into three states, including (i) 'intolerable' (ships passing at a distance of less than 0.5 nm ); (ii) 'tolerable' (passing distance between 0.5 and 3.5 nm ); and (iii) 'broadly acceptable' (ships passing the OWF at a distance greater than 3.5 nm ).
(3) Season and day/night time: the states of 'season' and 'day/night' are defined based on the local best practices. Four states of season are defined as spring (March, April and May), summer (June, July

and August), autumn (September, October and November) and winter (December, January and February). In addition, day is defined from 8 am to 8 pm while night is defined from 8 pm to 8 am of the next day.
(4) Courses: the only shipping route near the OWF is the Nanri one, where the northbound traffics are the courses from $305^{\circ}$ to $125^{\circ}$ and the southbound are the courses from $125^{\circ}$ to $305^{\circ}$.
(5) Others: the states for 'length', 'beam', 'depth', 'displacement', and 'speed' are first defined by analysing the state distributions of each variable in the database and then amended with reference to the local best practices to ensure that the states are reasonable (e.g. Yu et. al., 2020, Wu et. al., 2019). For example, traffic flows after OWF installations are analysed and results present that the average passing speed is 8.53 knots. A large amount of ship speeds are concentrated in the range 6-12 knots and they are defined as middle speeds. Speeds between 2 and 6 knots are defined as low, larger than 12 knots as high and less than 2 knots as drifting speeds. In a similar way, distributions of other variables including the length, beam, depth and displacement are also analysed to classify their states. The states for each variable are provided to experts (see Table 3) to check if they are consistent with their experience. As results, the states of length are defined as: 1) length less than 80 metres; 2) between 80-120 metres and 3) 120 metres and over. The states of beam are 1) less than 10 metres; 2) between 10-20 metres; 3) between 20-30 metres and 4) 30 metres and over. The states of depth are 1) less than 3 metres; 2) between 3-6 metres; 3) between 6-9 metres and 4) 9 metres and over. The states of displacement (gross tonnes) are 1) very small (less than 2 tonnes); 2) small (300 to 3,000 tonnes); 3) average (3,000-10,000 tonnes) and large ( 10,000 tonnes and over).

Table 1. State definitions of the variables



# 4.2 Learning and validating a data-driven BN 

A Bayesian software application (GeNIe) is applied to train the BN from the purified and classified AIS data (i.e. 590 sets) by deploying the BSA as the BN learning approach. We set the constant prior probabilities for all structures with the same value of 1 as there is no background knowledge input. The training report of the data-driven BN (i.e. original BN) is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Training report for the BN structure
To ensure the dependencies among the nodes reflect real traffic flow characteristics, we validate the original BN by removing unrealistic links between nodes. For example, there is no direct causal relationship between 'beam' and 'minimum passing distance' and the interrelationship between 'day/night' and 'minimum passing distance' is very weak as the conditional probabilities of the states between these two nodes do not show any significant difference. As a result, the amended BN structure is given in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. Fine-tuned data-driven BN structure
The fine-tuned data-driven BN is then tested by the local AIS data for its validation. The BN shows the following consistencies: (i) the number of oil and gas tankers makes up the highest proportion (43\%), which well reflects the reality; (ii) approximately $67 \%$ of vessels pass the OWF areas at a 'tolerable' distance (from 0.5 nm to 3.5 nm ), approximately $18 \%$ of vessels pass with a distance less than 0.5 nm , and the rest of vessels pass at a broadly acceptable distance (more than 3.5 nm ). This is consistent with the local vessel traffic records; (iii) the number of fishing vessels in summer ( $16 \%$ of the total fishing vessels in the database) is the least among four seasons as the local fishing prohibited season is between May and October. As results, the data-driven BN is partially verified as the findings from the BN marginal probability analysis are in harmony with the real statistics. In addition, the advantage of visualising traffic flow characteristics by using BN is also presented.

To further validate the BN model, the K-fold cross validation method is applied. Detailed descriptions of the method are found in Hastie et al. (2009), and James et al. (2013). To demonstrate its application in this study, an example of the node of 'ship category' is used for illustration through 590 AIS records. Suggested by Hastie et al. (2009), we set the fold count as 10 and the folding seed as 0 (meaning to divide the data into 10 parts and no random assignment of records to different folds). As results, the total accuracy for the node of 'ship category' is $77.12 \%$, with $71.67 \%$ (ship category=general), $83 \%$ (ship category=oil and gas tanker), $94.55 \%$ (ship category=fishing vessel) and $50 \%$ (ship category=service vessel) respectively. A ROC (receiver operating characteristic) curve for 'ship category=oil and gas tanker' is presented in Figure 4a) to demonstrate the accuracy of the BN. It shows the AUC (area under curve) value in the ROC curve is 0.87 (AUC is excellent within the range of ( 0.85 to 0.95 )). A calibration curve is also given in Figure 4b) to present the accuracy of model

predictions. By comparing the output probability (horizontal axis) to the actually observed frequencies in the data (vertical axis), the curve in Figure 4 b) is consist with the dim diagonal line, in which every output prediction is precisely equal to the data. Therefore, the test proves the robustness of the model.
![img-3.jpeg](img-3.jpeg)

Figure 4: a) Receiver operating characteristic (ROC) curve and b) calibration curve for ship category is stated as 'general'.

# 4.3 Identifying RIFs 

To identify the relevant RIFs, 15 previous studies regarding ship and offshore collisions are reviewed (see Table 2). Among the studies, the variables of 'ship category', 'displacement', 'speed', 'minimum passing distance' and 'season' are selected as they are frequently mentioned in the previous studies (more than three times). They will be used as the parent nodes of the two intermediate nodes of likelihood and consequence. The remainder that include 'length', 'beam', 'draught', 'course' and 'day/night' are defined as sub-influential factors (SIFs) and retained in the BN.

Table 2. Identification of the RIFs from the literature


Next, the RIFs are divided into likelihood and/or consequence groups based on their individual features, in which 'ship category', 'season' and 'minimum passing distance' are grouped as the RIFs that affect the V-T collision probability (e.g. Ellis et al., 2008; Mujeeb-Ahmed et al., 2018; Yu et al., 2020), and 'ship category', 'speed' and 'displacement' are the RIFs for collision consequences (e.g. Biehl, 2006; Dai et al., 2013).

Three additional nodes are introduced into the BN structure, including two intermediate nodes of collision probabilities and collision consequences and one final node of collision risk. As a result, the structure for the multi-data-driven BN-based risk model for V-T collision is established and shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. General structure for the V-T collision BN model
4.4 Subjective data acquiring and aggregating

A panel of three experts are invited to provide judgements of the risk of collision under different navigation environments, includes a captain of the China National Offshore Oil Corporation company who sails frequently in the waters near the investigated OWF, a chief officer of an OWF maintenance company who is responsible for the maintenance and operation of several OWF projects in the same

area, and a fishing ship captain, running a ship to fish in the area for decades (see Table 3). Given a relatively small number of OWFs near main shipping routes, the experts of good experience on navigational safety passing OWFs are very limited. In this case study, it is even worse given that the OWF was only established in Year 2017. Despite the huge effort from the authors, only three experts are qualified by taking into account their experience and knowledge to provide valuable data. However, the experts presents different groups of stakeholders who are closely working in relative fields to ensure the quality of the obtained subjective database. In addition, the confidence of the data quality comes from the high consistency among their judgements (see Table 4). Furthermore, the good result from the sensitive analysis in the validation part proves the quality of the data from the experts.

Table 3. Detailed information on the invited experts

| Expert
No. | Type of ship worked on | Position | Age | Gender | Education | Years of working experience | Type of experience |

A survey that covers all navigation environments is designed from two risk dimensions (collision probabilities and collision consequences) is designed to collected experts' judgements about impact magnitudes in terms of the RIFs. The obtained subjective probabilities are derived from the experts' background knowledge and expressed by specific linguistic states with a belief structure. For example, a question is designed as 'what is the collision probability if a general cargo vessel passes water areas with an intolerable distance in spring', and a judgement of the collision probability is [0.8(average), 0.2(frequent)]. The judgements for all possible state combinations that represent different navigation environments are collected and shown with tables. The judgement results for the collision probability is shown in Table 4.

Table 4. Judgement results for the probability of a collision



The acquired judgements are aggregated through an ER to appropriately cope with the uncertainty in their judgements (subjective data). In the first step of using ER, we assign a weight to each expert based on their background. The weights can be generated referring to the criteria in Lavasani (2010) and the information in Table 3, and the weights for the three experts are $0.405,0.333$ and 0.262 , respectively. Then an ER's associated computing software Intelligent Decision System program, is used to combine the judgements. The aggregated results of collision probability and consequence are shown in Table 5 and Table 6, respectively.

Table 5. Aggregated results for the probability of collision


Table 6. Aggregated results for the consequences



The incompleteness (i.e. uncertainty in data) of their judgement is remained in the aggregated results (see the "Unknown" in Table 5 Table 6). The "worst-case scenario" concept in risk science is applied to assign the unknown values to the state of 'highly frequent' in Table 5 and to the state of 'catastrophic' in Table 6, respectively. Therefore, the CPTs for two intermediate nodes are established ${ }^{2}$.

The CPT for the final node synthesises the influence from collision probability and collision consequence by using an equivalent influential method to conduct a rule-based set. The obtained CPT for the final node is given in Table 7.

Table 7. Conditional probability of collision risk


By introducing the above information into the BN structure (Figure 5), a multi-data-driven BN-based risk model for the evaluation of the V-T collision is developed and presented in Figure 6.

[^0]
[^0]:    ${ }^{2}$ The unknown belief degree can be assigned to different grades based on the best scenarios or average scenarios. The results can be used to compare the analysis of the worst case scenario (e.g. Yang et al. 2011).

![img-5.jpeg](img-5.jpeg)

Figure 6. Results of the multi-data-driven BN

# 4.5 Risk ranking 

To prioritise the risk, a set of utility values is assigned to the two intermediate nodes as $U_{\text {probability }}\{1$, (very low); 3,(low);5,(average);7,(frequent);9,(highly frequent) $\}$ and $U_{\text {consequnece }}\{1$, (negligible); 3, (marginal);5, (moderate);7,(critical);9, (catastrophic)\} (Wang and Yang, 2018). By synthesising the above assignments, the utility values of the states of the final node (i.e. collision risk) are calculated as follows: $U_{\text {collision risk }}($ very low $)=\times$ $U_{\text {probability }}$ (very low) $\times U_{\text {consequence }}$ (negligible) $=1 \times 1=1 \quad, \quad U_{\text {collision risk }}($ low $)=$ $9 \quad, \quad U_{\text {collision risk }}$ (average) $=25 \quad, \quad U_{\text {collision risk }}$ (high risk) $=49 \quad$ and $U_{\text {collision risk }}$ (very high risk) $=81$. Meanwhile, the crisp values are used as threshold values to define different risk levels and the obtained result can be associated with the five risk levels by linear calculation (Yang et. al., 2009b).

By applying Equation 4, the general baseline results of (13\% (VHR), 10\% (HR), 29\% (A), 23\% (LR) and $25 \%$ (VLR)) of the final node (from Figure 6) is converted into a crisp value of $C R=0.13 \times 81+$ $0.10 \times 49+0.29 \times 25+0.23 \times 9+0.25 \times 1=25$. The general V-T collision risk in the study areas is evaluated as $100 \%$ of average situation $\left(U_{\text {collision risk }}(\right.$ average $)=25$ ).

# 5. Application of the proposed BN for V-T collision risk analysis 

### 5.1 Case description

To select the most representative cases in terms of traffic flow characteristic, information from AIS data and expert experience are both used in a combined manner. For example, the obtained BN (see Figure 6) shows oil and gas tankers and general cargo vessels are two main ship types given an oil dock is located near the studied waters. They are naturally selected as the main objects to assess the collision risk. Furthermore, the invited experts supplement that the fishing vessels and OWF service vessels are risky given that they often approach to the wind turbines in a much closer distance than other ships. Therefore, we select general cargo vessels, oil tankers, fishing vessels and service vessels involving ten cases (Table 8) to develop our scenarios as the reflection to the reality.

Before evaluating the ten selected real cases, the attributes are classified based on the criteria given in Table 1. For instance, the first case is classified as follows: the displacement of the vessel is within the range between 300 tonnages to 3000 tonnages, thus is defined as 'small'; the speed is between 6 knots to 12 knots and is defined as 'middle'; and the minimum passing distance is less than 0.5 nautical miles, which is 'intolerable'. Therefore, the first case can be converted into a set of linguistic variables that \{Sc=service, $T=$ very small, $V=$ middle, $S e=$ spring and $M P D=$ intolerable $\}$. Similarly, other cases are classified. The detail information and classified results for the ten cases are shown in Table 8.

Table 8. Detailed information on the ten cases


### 5.2 Case evaluation and result prioritisation

The cases are evaluated with the developed BN based risk model. For example, the information for Case 5 is inputted into the BN by locking the nodes as [100\%, (Sc=general cargo), 100\%, (T= large), $100 \%$, (V= high), 100\%, (Se= summer), 100\%, (MPD=intolerable)] (see Figure 7). By inferring the collision risk under such a navigation environment, Case 5 generates a result with a distribution in the

node of 'collision risk' as (37\% (very high risk), 41\% (high risk), 22\% (average), 0 (low risk), 0 (very low risk)). This result is converted into a $55.56 C R$ (between high risk (i.e. 49) and very high risk (i.e. 81)). The risk of Case 5 can be calculated by a linear function as Risk level ${ }_{\text {very high risk }}=$ $\frac{C R-U_{\text {collision risk }}(\text { high risk })}{U_{\text {collision risk }(\text { very high risk })-U_{\text {collision risk }}(\text { high risk })}}=\frac{55.56-49}{81-49}=20.5 \%$ and Risk level ${ }_{\text {high risk }}=1-$ Risk level ${ }_{\text {very high risk }}=79.5 \%$. Therefore, Case 5 is $20.5 \%$ very high risk and $79.5 \%$ high risk.
![img-6.jpeg](img-6.jpeg)

Figure 7. Graphical network results for Case 5
Other cases are also evaluated in a similar way and the evaluation results are prioritised by ranking their $C R \mathrm{~s}$ (see Table 9).

Table 9. Collision risk analysis results and ranking



Table 9 ranks the collision risk of the cases in an increasing order of Case 8, Case 6, Case 2, Case 10, Case 3, Case 7, Case 1, Case 4, Case 9 and Case 5. Among these cases, Case 8, 6, 210 and 3 are under the low-risk situations (lower than average threshold value of 25); and high-risk situations include Case 7, 1, 4, 9 and 5 (higher than 25).

From a comparative analysis of the low and high risk cases, the common features of the low-risk cases are (i) vessels sailing below high speed; (ii) the minimum passing distance is either 'tolerable' or 'broadly acceptable'. Meanwhile, all the high-risk cases have the common feature that their minimum passing distance is intolerable. This is because that in shipping navigation, if minimum passing distance is smaller than certain level, it is treated as an incident. If in the meantime the other factors in a favour of occurrence of a collision, the collision accident can occur and (iii) oil and gas tankers have high risk than other vessels as they may lead to more serious collision consequences (Goerlandt and Montewka, 2015). For example, Case 3 and 7 have broadly acceptable passing distances but their collision risks are relevantly higher than other cases.

Based on the above evaluation results, the vessels in Cases 1, 4, 5 and 9 should immediately change

course and/or reduce speed to maintain a safe passing distance. The vessels in Cases 3 and 7 should take extra collision avoidance operations if the navigation environments are changed. The vessels in Cases 2, 6, 8 and 10 could maintain their courses and speed.

# 5.3 Ratio analysis 

To identify critical situations, a ratio analysis is conducted. We firstly calculate the ratio value ( $R V$ ) of a particular navigation environment situation in the whole set of 590 AIS data, and then analyse the critical level for each case by locating the cases in a matrix, which uses $C R$ as the horizontal coordinate and the $R V$ as the vertical coordinate. In the matrix, a case with a high $C R$ and a high $R V$ is identified as a critical situation. For example, in the obtained AIS database, there are 63 records similar with Case 5, and the $R V$ for Case 5 is thus calculated as $R V_{5}=63 \div 590=0.107$. Combining with its $C R$ of 55.56 , Case 5 is identified as a critical situation.
![img-7.jpeg](img-7.jpeg)

Figure 8. The matrix to identify the critical situations
As shown in Figure 8, the matrix identifies that Case 5 is the most critical case among others. Case 1, 4 and 9 are located in the relative dangerous situations as the collision risks $(C R)$ for these cases are high. Low risk situations include the rest of six cases, which are Cases 2, 3, 6, 7, 8 and 10.

# 6. Validation and discussion 

In this section, the proposed BN model is discussed through various validation steps to present more detail information of the model's reliability and robustness. The implications of the BN model in light of the adopted case study results are also further discussed.

In general, the validity of a BN in a physical phenomenon such as V-T collision could be analysed by testing the BN's fitness with data. However, it is unfeasible for OWF studies due to following reasons: on the one hand, the accident reports about V-T collision in OWF waters are insufficient and difficult to access, so that performing a test to collect an experimental database would be impractical and limited compared to the scope of model scenarios. On the other hand, models from previous studies do not specifically consider the traffic flow parameters conditioning to a specific OWF water and hence can only provide a rudimentary indication of the variables' impact. For these reasons, a BN validation framework proposed by Pitchforth and Mengersen (2013) is adopted in this study. It contains serval conceptual tests to improve the confidence in the BN modelling, including face validity and content validity. A face validity tests the performance of a BN translating the construct under investigation into an operationalisation, whereas a content validity suggests the extent to which the model can be accepted.

### 6.1 Face validity

We first discuss a face validity for the rationality and consistence of the BN with expert experience and previous studies. The obtained BN is evaluated by experts who were introduced in Section 4.4. Experts agree with the statement that the BN can be considered as an appropriate model for V-T collision as it produces rational structure and selects RIFs are consistent with their experience. Meanwhile, it is clear from the BN construction that the collected data and approaches are reliable and experience from previous studies is reasonably applied that fits well with their knowledge. Therefore, the BN is expected to provide reliable evaluations. However, experts suggest some limitations that need to be improved in further studies. More AIS data should be used in the BN training process from more waters involving OWFs for generating a generic result.

### 6.2 Content validity

As the RIFs used in the BN are selected based on previous studies and expert judgements, the importance of the RIFs and the rationality of their selection should also be tested to see if the RIFs present higher importance than the SIFs. Thus, an entropy approach is performed to identify the most informative variables based on the collected multiple. A high entropy value represents a high importance, and vice versa (Hänninen and Pentti, 2012). By selecting the final node (i.e. collision risk)

as the target, the relative importance for all the variables that include RIFs and SIFs are calculated and presented in Table 10.

Table 10. Uncertainties of variables


From Table 10, the minimum passing distance obtains the highest value of 0.061 thus is defined as the key factor in the V-T collision risk, following by displacement, ship category, season, and speed. The variables of draught and course have the importance values of 0.013 and 0.011 respectively. Although they are allocated as the SIFs, their entropy values are close to the variable of speed ( 0.016 ), indicating that a ship's draught and course also have significance impact for C-T collision.

In MGN 543 (2016), it suggests a ship route should keep an acceptable distance to OWF turbines, and should able to distance itself from turbines based on its ship features, crewmembers' experience, and radar reception results, etc. to ensure safety. Thus, the entropy analysis results are consistent with the policy. When comparing the results the previous studies and expert's experience (e.g. Ellis et al., 2008; MGN 543, 2016; Yu et. al., 2020), we also find the good fitness of the RIF selections in this study. In addition, the analysis shows some limitations of previous studies. For instance, a couple of SIFs (e.g. draught, course) show some impacts to V-T collision but they have not been modelled in previous studies. Meanwhile, as the AIS/expert judgement data is scattered, the linguistic states using to describe variables have significant impacts on the results. Using appropriate linguistic states for variables could reduce data uncertainties and improve model reliability.

# 6.3 Sensitivity analysis for implications 

The variable sensitivity in terms of the collision risk is calculated and determined in this section. During a sensitivity test, three subjective nodes are selected as target nodes to determine critical

scenarios. After applying a sensitivity test to the developed model, the top 10 high impact scenarios for probability, consequence and collision risk are presented in Figures 9-11, respectively.
![img-8.jpeg](img-8.jpeg)

Figure 9 Sensitivity analysis results for probability
![img-9.jpeg](img-9.jpeg)

Figure 10 Sensitivity analysis results for consequence

![img-10.jpeg](img-10.jpeg)

Figure 11 Sensitivity analysis results for collision risk
The most critical situations leading to collision risk can be determined based on the multiple data sources (i.e. AIS database and experts' judgements). Figure 9 shows that when the probability of collision is highly frequent, the most critical scenario is $\{\mathrm{SC}=$ service vessel, $\mathrm{Se}=$ spring, $M P D=$ intolerable $\}$, with a sensitivity value of $0.0014(0.0183-0.0169)$, which covers a sensitivity range between 0.0169 to 0.0183 . Figure 10 reveals that the most critical scenario leading to catastrophic consequence is $\{\mathrm{SC}=$ oil and gas tanker, $\mathrm{T}=$ small, $\mathrm{V}=$ middle $\}$, with a sensitivity value of 0.1407 , which covers a range between 0.2483 to 0.3890 . By considering both the collision probability and consequence, Figure 11 demonstrates the most critical scenario is $\{\mathrm{SC}=$ oil and gas tanker, $T=$ small, $V=$ middle $\}$ that leads to a very high collision risk, with a sensitivity value of 0.1057 given that the sensitivity range is between 0.0976 to 0.2033 ).

There are useful implications drawn from the sensitivity analysis. A scenario of a small oil and gas tankers passing OWF waters with a middle range speed is the most critical scenario in the studied waters. As shown in Figure 6, the ship type of oil and gas tankers counts the highest number in the collected AIS data, (e.g. $41 \%$ of total ship number in the studied OWF waters). Among these tankers, about $68 \%$ are small tankers (displacement between 300 tons and 3000 tons), approximate $71 \%$ of them navigate at a middle speed (between 6 and 12 knots) (see Figure 12). This is due to the fact that there is refuelling port near the OWF water as explained by a local maritime administration officer. As the collision between tankers and turbines could cause a catastrophic consequence not only financial lose but also water pollutions, scenarios concerning tankers require high safety attention accordingly.

![img-11.jpeg](img-11.jpeg)

Figure 12: Details of oil and gas tankers in the study waters.

# 7. Conclusion 

This paper proposes a new BN modelling approach (i.e. BaLER), which pioneers the use of combined AIS and subjective data to aid V-T collision-avoidance decision. Following this approach, BSA is first applied to visualise traffic flow characteristics. Then, ER aggregates the expert judgements to obtain subjective information for risk evaluations. At last, the established IF-THEN rules convert the subjective information into CPTs to develop a multiple-data-driven and BN based risk model.

To provide empirical evidence for the use of the proposed approach, ten real scenarios are simulated by using the developed risk model to prioritise their collision risks and analyse the critical situations. As a result, among the most critical scenarios is large general cargo vessels passing the OWFs with a high speed and an intolerable passing distance. To verify the finding, the BN model is validated through various methods including sensitivity analysis, which suggests that the minimum passing distance is the key factor in V-T collision risk and the most significant combined critical factor in the study waters is the middle-speed small oil and gas tankers.

The main contributions of this paper are: (i) a multi-data-driven BN-based risk analysis approach is proposed to use AIS data and expert experience in BN for maritime risk analysis; (ii) a target-free data

learning approach is introduced train data-driven BNs using AIS data. It helps enhance the traffic flow visualisation and simulation; (iii) the proposed BaLER is a generic BN based approach can be widely used in many transport traffic flow related collision risk assessments; and (iv) an application of BaLER in an emerging research topic of V-T collision establishes an effective risk model to support collision avoidance and decision-making in OWFs.

# Acknowledgements 

The research work is financially supported by China Scholarship Council (CSC) and National Natural Science Foundation of China (Grant No. 51479157). The authors also acknowledge the funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 823904 (ENHANCE). The authors also really appreciate the anonymous reviewers' comments and their effort to help improve the quality of this work.

# Appendix A 

## An illustrative numerical example of the data training BN approach

Assuming a $D$ containing ten records $(N=3)$ is presented in Table 11. The $D$ contains three variables $x_{1}, x_{2}$ and $x_{3}(m=3)$. Let a possible structure $B_{1}=\left(x_{1} \rightarrow x_{2} \rightarrow x_{3}\right)$, where $P_{\left(x_{1}=H\right)}=5, P_{\left(x_{1}=L\right)}=$ $5, P_{\left(x_{2}=H \mid x_{1}=H\right)}=4, P_{\left(x_{2}=L \mid x_{1}=H\right)}=1, P_{\left(x_{2}=H \mid x_{1}=L\right)}=1, P_{\left(x_{2}=L \mid x_{1}=L\right)}=$ $4, P_{\left(x_{3}=H \mid x_{2}=H\right)}=5, P_{\left(x_{3}=L \mid x_{2}=H\right)}=0, P_{\left(x_{3}=H \mid x_{2}=L\right)}=1$ and $P_{\left(x_{3}=L \mid x_{2}=L\right)}=4$.

Table 11: A database example


The likelihood of $P\left(B_{1} \mid D\right)$ can be calculated as follow:

$$
\begin{aligned}
P\left(B_{1}, D\right)=P\left(B_{1}\right) & \times \frac{(2-1)!\times 5!\times 5!}{(10+2-1)!} \frac{(2-1)!\times 4!\times 1!}{(5+2-1)!} \frac{(2-1)!\times 4!\times 5!}{(5+2-1)!} \frac{(2-1)!\times 0!\times 5!}{(5+2-1)!} \frac{(2-1)!\times 4!\times 1!}{(5+2-1)!} \\
& =2.23 \times 10^{-9} P\left(B_{1}\right)
\end{aligned}
$$

In similar way, likelihood for another structure $B_{2}=\left(x_{1} \rightarrow x_{2}\right.$ and $\left.x_{1} \rightarrow x_{3}\right)$ is also obtained as $P\left(B_{2}, D\right)=$ $2.23 \times 10^{-10} P\left(B_{2}\right)$. If there are no background knowledge assigned to two structures (i.e. $P\left(B_{1}\right)=$ $P\left(B_{2}\right)$ ), likelihood of $B_{l}$ is 10 times higher than $B_{2}$, thus the $B_{l}$ is selected as the network structure to represent relationships among variables in $D$.