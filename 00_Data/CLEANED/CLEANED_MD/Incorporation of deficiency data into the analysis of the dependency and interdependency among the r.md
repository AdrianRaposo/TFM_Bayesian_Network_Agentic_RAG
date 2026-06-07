# LJMU Research Online 

Wang, Y, Zhang, F, Yang, Z and Yang, Z

## Incorporation of deficiency data into the analysis of the dependency and interdependency among the risk factors influencing port state control inspection

## http://researchonline.ljmu.ac.uk/id/eprint/14879/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Wang, Y, Zhang, F, Yang, Z and Yang, Z (2020) Incorporation of deficiency data into the analysis of the dependency and interdependency among the risk factors influencing port state control inspection. Reliability Engineering and Svstem Safetv. 206. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Incorporation of deficiency data into the analysis of the dependency and interdependency among the risk factors influencing port state control 

inspection


#### Abstract

Port State Control (PSC) inspection aids to control substandard ships and ensure safety at sea. Current risk-based PSC research and practice fail to incorporate ship deficiency records into detention probability analysis, because of the difficulty introduced by the involved big deficiency data. In this paper, a new Bayesian Network (BN) based PSC risk probabilistic model is developed to analyze the dependency and interdependency among the risk factors influencing PSC inspections based on big data derived from the inspection database of Tokyo MoU for the period between 2014 and 2017. The results reveal that ship's safety condition related deficiencies as well as technical features of the inspected vessel itself are among the most influential factors concerning PSC inspections and ship detention. New Bayesian learning methods are used to improve the model efficiency in ship detention prediction. As a result, the newly developed model has shown a reliable performance on dynamic prediction and cause-effect diagnosis of ship detention probabilities by pioneering the incorporation of ship deficiency records in the analysis. The findings provide important insights on how to facilitate risk-based PSC inspections for both ship owners and port states. They provide support for port state authorities to implement rational inspection policies.


Keywords: Port state control, Bayesian networks, maritime safety, interdependency analysis, maritime transport.

# 1. Introduction 

The sustainable development of maritime transport plays a significant role in promoting international trade, and in consequence serves as the driving force of world economic prosperity. However, catastrophic maritime accidents seriously affect the sustainability of international trade due to their social and economic impacts [30][7][20][1]. For instance, the spill of Amoco Cadiz oil tanker caused 230,000 tons of crude oil to leak into the sea and the grounding of the Aegean Sea seriously polluted the local beach and caused serious depression of local tourism business. To ensure maritime safety, along with the joint efforts made by shipowners, classification societies and flag state administrations, the Port State Control (PSC) inspection came into the scene for controlling substandard ships[19][26][4].

PSC inspection is carried out by port state authorities with the objective of ensuring the calling foreign vessels to meet the requirements of safety and pollution regulations. It consists of various inspection aspects, including the safety of life and property on board, prevention of pollution, living and working conditions and so on. If any serious deficiencies were found, the ship would be detained and instructed to rectify the deficiencies before its departure.

In recent years, many studies assessing the interaction of factors influencing safety have been conducted in the maritime transportation field (e.g. [41][50][42]). Most of them are associated with ship navigational safety assurance, which leaves a gap in the relevant studies of risk-based PSC inspection area [48][49]. Few pioneering studies have been undertaken by utilizing PSC inspection data (e.g. [38][24][21]), and fewer have quantitatively addressed the interactions among the influential factors. Actually, in practice, the identified deficiency of a particular influential factor is often associated with the deficiencies of its relevant factors. In this paper, when one factor is influenced by other factors, this one-directional relationship is defined as dependency. When two factors influence each other, this bi-directional relationship is defined as interdependency. [12]. In addition, due to the uncertainty in the PSC data, previous studies often use partial risk factors for which the relevant data can be obtained to conduct PSC analysis, which often leads to an error-prone correlation analysis.

As a consequence, it is well noted that incorporation of risk assessment into PSC is able to identify the potential hazards in PSC inspection and improve inspection efficiency. However, because of the lack of requiring big data for the safety condition of calling vessels, the interdependency among risk factors influencing PSC inspections is often ignored or difficult to explore in previous studies, demonstrating these research outputs are arguably not fully verified.

This study aims to propose a Bayesian Networks (BNs) risk assessment model to investigate the dependency and interdependency among the influencing factors of PSC inspections, as well as identify and prioritize the most important critical factors for ship detention. To achieve this, the inspection database of seven Asian countries from 2014 to 2017 in Tokyo MOU was collected. The parameters of the model are categorized into three sections, including: 1) the technical features of ship, such as the ship type, ship age, grosstonnage, flag of ship and classification society of ship; 2) the inspective activities, such as the type of inspection and place of inspection; and 3) the ship deficiency details (i.e. a total of 30 types of ship deficiencies), covering the safety, pollution and other requirements. The development, reasoning and validation of the PSC BNs model are realized through BNlearn software packages of R language and Netica.

Additionally, the proposed model can predict the detention rate of an inspected ship under dynamic situations. For instance, when the deficiencies are observed in an inspection, a forward prediction of the ship's detention probability could be done by taking into account of the existing status. Oppositely, if the ship is detained, a backward diagnosis can be conducted to suggest the status of technical features of the ships for efficient rectification when ship detention information is available. This is particularly useful for shipping companies and maritime service authorities to improve ships' inspection performance as well as for port authorities to implement rational inspection policies.

The remainder of this paper is organized as follows. Through a rigorous literature review, Section 2 summaries the factors influencing PSC inspections, reviews risk analysis studies associated with PSC inspections, as well as analyses the applications of BNs in the maritime safety field. Section 3 presents the development process of data-driven PSC BNs. Research findings and discussion are described in Section 4. Finally, the recommendations and conclusions are presented in Section 5.

# 2. Literature review 

### 2.1 Identification of the factors influencing PSC inspections

As a favorable supplementary means to ensure maritime safety, the research on PSC inspections has attracted great attention from scholars. Clarke [10] firstly analyzed the responsible parties who should be blamed for substandard ships and the corresponding actions that need to be taken incorporate with them. Hare [19] studied the effectiveness and significance of PSC inspection in preventing substandard ships from participating in international trade. Later, the PSC mechanism research [32][23], legal issues of PSC [15], and the impact of the new inspection regime ([47][45]) promoted the development of a scientific and comprehensive PSC inspection procedure in practice.

The influential factors in risk-based PSC are often associated with the pre-established safety standards, which serve as the principle for selecting substandard ships for inspections. Cariou et al. [5] applied the inspection database of the Indian Ocean MOU to analyze the evidence on the target factors used for PSC inspection. The main contributors to the ship detention were obtained, including the age and flag of ships. Later, they did further analysis to improve the selection process for port state authorities through quantitative regressions [6]. Knapp \& Franses [24] considered the ship particulars, place of inspections and the index of ship deficiency to analyse the economic benefits of PSC inspection. The results showed that the combination of different data can effectively improve the effect of targeting substandard ships. As a relative consensus followed by port state authorities, the target factors usually contain the following three categories of information: 1) the technical features of vessels such as gross-tonnage, age and type of ship; 2) the inspective activities including type of inspection and place of inspection; and 3) various inspected ship deficiencies.

Among the factors influencing PSC inspection, scholars had shown a particular interest on ship deficiency. Cariou et al. [3] claimed that vessel age, vessel type and flag state were three main factors affecting the number of deficiencies. They latter applied 4080 inspections records from the Swedish Maritime Administration to investigate the effectiveness of PSC inspections and found that $63 \%$ of the total number of deficiencies

was reduced during the next PSC inspection [4]. Unfortunately, the differences in the severity of these deficiencies were ignored in the study. For improving the performance of PSC inspections, Wolff and Cariou [44] tried to advocate increasing weights of the previous inspection factors. However, those previous studies revealed that the causal interrelationship among the deficiency remains unclear. On the basis of the above research, this paper takes the lead in bringing 30 types of deficiencies into the risk model of PSC inspection, in order to disclose the interdependency among the factors.

# 2.2 Risk studies on PSC inspections 

Kara [22] assessed the risk value of each incoming ship across the Istanbul Strait by using the method of weighted points. It offered a scientific basis for the PSC inspections against the Black Sea MOU. The factors such as the performance of flag States, deficiencies index and accidents were taken into account in the calculation. However, the quantification and applications of the above factors were based on the experience of experts while the accuracy of the results was arguably not fully verified.

To improve the accuracy of risk assessment for PSC inspections, Chi and Jun [9] proposed a new automatic optimization and self-evolution algorithm, which used the parameter redundant factors originally from a generalized additive model to predict the risk of incoming ships. Evaluation results showed that the ship targeting system could be automatically optimized. Xu et al. [46] considered both the historical inspections factors and generic factors of ships to build a ship risk assessment model based on support vector machine (SVM). As a result, the accuracy of risk analysis was greatly improved by the proposed model. Gao et al. [14] improved the ship selection process for port state authorities on the basis of a hybrid SVM and K-nearest neighbour (KNN) algorithm. Their results suggested that the combined algorithm was conductive in improving the service efficiency of PSC inspections. Chen et al. [8] utilized a Grey Rational Analysis (GRA) model with improved entropy weight to understand how much the varied factors influence the decision of ship detention under PSC. Despite showing some attractiveness, the above methodologies still exhibit some limitations in their practical applications from the perspective of dynamic prediction in uncertain environments. Further, most of the previous studies focused on the impact of influencing factors on the risk of ship detention,

while the analysis of the interaction among these factors was ignored. It leaves a research gap for revealing the cause-effect interactions in ship's PSC inspection.

# 2.3 Bayesian Networks (BNs) in PSC research 

Methodologies applied in the PSC relevant research had been growing over the past decades. They covers statistical methods (e.g. [5]), regression analysis (e.g. [24][25][18][6]), machine learning (e.g. [46][14]), and game model (e.g. [49][13]). However, as mentioned above, most of them were either often subjective or lacks the ability of undertaking dynamic analysis, while some were not capable of dealing with very complex systems.

In recent years, a wider interest in the application of BNs into maritime safety analysis were evidenced by the fast-growing number of published studies. For instance, the maritime risk estimation [27][16][37]; and the maritime accident analysis [50][18][29][28]. As stated by Hänninen [18] that BNs are capable of representing complex and uncertain relationships between variables and providing the possibility of combining data with expert knowledge in addition to model updating as new evidence is acquired. Meanwhile, scholars also tried to integrate logistic regression (e.g.[27]) into BNs or suggest to construct the BN on the basis of data-driven (e.g. [51]) for alleviating the bias brought by the expert estimation. The Tree Augmented Naïve (TAN) Bayes classifier by Wang et al. [43] and the probabilistic approach for ship risk assessment by Dinis et al. [11] are the typical examples developed upon the PSC dataset. In light of this development, based on the PSC inspection database obtained from Paris MoU, Yang et al. [48] applied BNs to establish a risk assessment model. Although the result proved that BNs were effective in predicting the potential risk of an inspected ship, the influence of ship deficiency on detention was not addressed, leaving an important research gap to fill from a practical perspective. It is necessary to conduct a new study in which all the factors influencing PSC inspection (i.e. those mentioned in MOU) including both deficiency and detention are incorporated particularly given the significant impact of deficiency on the ship detention in PSC and the strong interest from shipowners on ship deficiency analysis for rectifications if their ships are in detention,. To do so, the dependency and interdependency among the variables requires a thorough analysis.

In light of the above analysis, the first innovative contribution of this study lies in its pioneering attempt of incorporating ship deficiency into the BNs-based risk analysis of PSC inspections. The correlation among the targeted factors as well as the ship detention probability in an uncertain environment could therefore be examined precisely. From an applied research perspective, this work pioneers the dynamic risk analysis of PSC inspection in Tokyo MoU areas. The findings can be used to conduct a comparative analysis to see the PSC inspection difference between Asia and EU which attracts the most dynamic risk-based PSC studies in the literature. They can also provide empirical evidence on the most important variables that PSC inspection focuses on when vessels visit Tokyo MOU ports.

# 3. Methodology 

A risk-based BN for PSC is constructed to capture the dependencies and interdependencies among different risk factors influencing PSC inspections. Fig. 1 shows the flowchart of the proposed methodology.

## [Please insert Figure 1 here]

The detailed description of the proposed methodology is presented as follows:

### 3.1 Data

This research uses a crawler program to collect a total of 46,496 records of PSC inspections of seven major Asian countries (i.e. China, Japan, Australia, Indonesia, Philippines, Republic of Korea, Vietnam) from 2014 to 2017 after the implementation of the PSC New Inspection Regime of Tokyo MOU. From such records, 38 factors influencing PSC inspections are identified and classified in three groups:1) the technical features of vessels (e.g. type of ship, age, gross-tonnage, ship flag, and classification society; 2) the inspective activities (e.g. type of inspection and place of inspection); and 3) the ship deficiency details. In the ship deficiency group, 30 types of deficiencies are further divided into six categories including certificates \& documentation, working and living conditions, labor conditions, pollution prevention, safety conditions and ISM, and others.

In terms of variable status, ship types in this paper include general cargo/multipurpose

ships, chemical tankers and bulk carriers. The ages of the ships are classified into 0-5, 5-$10,10-15,15-20,20-25,25-30$ and over 30 . Similarly, the factors of gross-tonnage, ship flag, classification society, type of inspection, place of inspection, ship deficiency details and their status learned from the data are clearly highlighted in Table 1. The statuses of all deficiencies are defined as either yes or no with respect to their natural feature.

# [Please insert Table 1 here] 

### 3.2 BNs learning

Normally, a BN is constructed using human expert knowledge or subjective judgments. However, network construction and model parameterization process based on this approach is time consuming, and heavy emphasis is placed on experts to provide both the local probability parameters and dependency among the parameters, which may cause uncertainty and biases [43]. By taking advantage of abundant empirical data as mentioned above, this paper applies the data-driven based BNs learning method, which can reduce the dependence on subjective manners and produce more accurate and objective outputs.

BNs learning generally consists of the following two processes, namely structure and parameter learning. The former is to determine the variables (nodes) related to the research target, while the latter is to configure the conditional probability table (CPT) of each node under a given BN structure. BNlearn is an R package which provides any combination of multiple learning algorithms included in the latest study, either network scores or conditional independence tests [36][31]. Meanwhile, it simplifies the analysis of the learned networks by providing a single object for all the algorithms and a set of utility functions to perform descriptive statistics and basic inference procedures [34][35]. Considering its versatility and practicality, this paper uses the BNlearn package to implement the BNs learning.

### 3.2.1 Structure learning

In the case of comprehensive database, a large number of BNs structure learning algorithms exist and could be divided into two categories: constraint-based methods and scoring-based methods [39][17]. The constraint-based methods aim to establish BNs that reflects the relationships among the variables to the greatest extent by discovering whether

they are dependent or independent. The scoring-based methods, which are used in conjunction with searching algorithms, score all possible network structures by setting a scoring function and then selecting the structure with the highest score. As the scoringbased method is more convenient to obtain an optimal network structure with sufficient data (e.g. [42][48]), this paper uses a scoring-based algorithm to construct the risk-based BN.

First of all, a Bayesian Information Criterion (BIC) scoring function is defined for the network, and in consequence the optimal network structure is found by the searching algorithm of hill climbing.

BIC refers to the approximate calculation of the value of a boundary likelihood function under the premise of large sample data, and it is a commonly used scoring function in practice.

Its formula is presented as follows:

$$
\log P(S \mid D) \approx \log P\left(D \mid S, \theta^{*}\right)-\frac{d}{2} \log n
$$

where $\log \left(P\left(D \mid S, \theta^{*}\right)\right)$ represents the matching degree between the structure $S$ and data $D . \theta^{*}$ is the value of a parameter when its posterior probability achieves the maximum. $\frac{d}{2} \log n$ is the penalty term for a complex model in BIC scoring. $d$ and $n$ refers to the dimension of the Gaussian function and the sample size, respectively.

A hill climbing algorithm is a mathematical optimization technique which belongs to the family of local searching [2]. It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by making an incremental change to the solution. If the change does produce a better solution, another incremental change is consequently made to the new solution, and such a process continues until no further improvement could be made.

# 3.2.2. Parameter learning 

Once the network structure is determined, the calculation of the CPTs of the parameters will be undertaken. Since the data obtained in this paper is complete, the Maximum

Likelihood Estimation (MLE) algorithm is used to calculate the network parameters [40]. The likelihood function can be expressed as follows:

$$
L(D \mid \theta)=\log P(D \mid \theta)=\log \prod_{i=1}^{m} P\left(d_{i} \mid \theta\right)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} m_{i j k} \log \theta_{i j k}
$$

where $m_{i j k}$ denotes the number of samples in which the value of the node $V_{i}$ is k when the parent node takes the $j_{t h}$ value combination, $m_{i j}$ shows the number of samples of all values of the node $V_{i}$ under the combination of the $j_{t h}$ value of the parent nodes.

Then, the MLE is computed as

$$
\theta_{i j k}^{*}=\arg \max _{\theta} L(D \mid \theta)=\frac{m_{i j k}}{m_{i j}}
$$

# 3.3 BNs reasoning 

In this paper, the 'Junction Tree' algorithm is adopted for probabilistic reasoning. The main idea is to transform a BN into a junction tree, and thereby to carry out probabilistic reasoning by defining the message transmission process in the junction tree [33]. A junction tree is defined as $J T=(C, S)$, where $C$ is a cluster of the junction tree, $S$ is the segmentation set which exists between any two adjacent clusters $C_{i}$ and $C_{j}$. The junction tree algorithm propagates beliefs (or posteriors) over a junction tree when a new piece of evidence comes in so that the factors over the junction tree stay consistent with each other [52].

### 3.4 Sensitivity analysis

Sensitivity analysis is essential in this research for verifying the effectiveness of the proposed model quantitatively and determining the key factors influencing ship detention. During this process, mutual information is calculated to measure the mutual dependence between two random variables. The concept of mutual information is intricately linked to that of entropy of a random variable, which is a measure of unpredictability of the status, or equivalently of its average information content [16]. Considering a discrete random variable $X$ with possible values $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ and probability mass function as $P(X)$,

the entropy could explicitly be written as

$$
H(X)=-\sum_{i=1}^{n} P\left(x_{i}\right) \log _{a} P\left(x_{i}\right)
$$

where $b$ is the base of the logarithm used, and it is generally valued as 2 .
Based on above theory, it is logical that the mutual information between 'detention' variable and other inspection variables in BNs could be calculated as the following formula:

$$
I(D, \beta)=-\sum_{d, i}\left(d, \beta_{i}\right) \log _{b} \frac{P\left(d, \beta_{i}\right)}{P(d) P\left(\beta_{i}\right)}
$$

$I(D, \beta)$ represents the mutual information between 'detention' variable $(D)$ and other inspections variables $(\beta)$ in BNs. The greater the value of mutual information, the stronger the relationship between $\beta$ and $D$. The key factors influencing ship detention are therefore identified from the ranking of mutual information result.

After the mutual information calculation is completed, another sensitivity analysis method, scenario simulation, was applied to further validate the rationality and reliability of the BN model. This method was proved to be a novel and effective model validation approach in the previous studies (Yang et al.,2018; Alyami et al., 2016).

# 4. Results and analysis 

### 4.1. Model structure

The network structure of this model is obtained from BNlearn package. It consists of 38 nodes which represent the variables identified in Table 1 in Section 3.1.The interrelationships among the factors influencing PSC inspections are various and complicated. For example, the variable 'type of inspection' (i.e. V1) is the parent of 24 other nodes, while the variable 'place of inspection' (i.e. V6) is the parent of 18 other nodes.

Meanwhile, nearly one third of the variables of ship deficiencies are the child of either 'fire safety' (i.e. V30) or 'safety of navigation' (i.e. V27), which means that the occurrence of many ship deficiencies is related to these two variables. On the contrary,

the node 'Pollution prevention - Marpol annex III' (i.e. V10) and 'Pollution prevention anti fouling' (i.e. V14) are independent from any other variables in the model, and therefore they have no effect on other factors.

In order to display the network more intuitively, the Netica software was used to present the model as shown in Figure 2.
[Please insert Figure 2 here]

# 4.2 CPT calculation 

Due to the large number of nodes and their complicated relationships exhibited in the model, conditional probabilities are illustrated by setting the nodes of 'gross-tonnage', 'type of ship', 'flag of ship' and 'dangerous goods' as examples. Others are calculated in a similar way. In regarding to the nodes' probabilities of different status, 'Gross-tonnage' is a root node and directly obtained from the data. The conditional ones of 'type of ship', 'flag of ship' and 'dangerous goods' are obtained via the 'MLE' algorithm (i.e. Equation 3). The CPT of these four example nodes are shown in Tables 2 to 5, respectively.
[Please insert Table 2 here]
[Please insert Table 3 here]
[Please insert Table 4 here]
[Please insert Table 5 here]

### 4.3 Model results and validation

### 4.3.1. Model results

Figure 3 shows the model result in a network with the marginal probability of each node. Accordingly, the predicted average ship detention rate is $2.05 \%$ which is harmony with the average ship detention rate $(2.01 \%)$ of Tokyo MOU during the named period. This result partially helps validate the developed model.
[Please insert Figure 3 here]
There are more findings of real implications. For instance, nearly two-thirds of the PSC inspected ships in the Asia-Pacific areas are bulk carriers. Ships with a load capacity of

30,000 tons or more accounts for a large proportion ( $47.1 \%$ ) of the inspections. $76.3 \%$ of the ships are subject to initial inspection. Meanwhile, ship's safety condition still presents a major threat to maritime transportation and shipping companies need to strengthen the management of ship's relevant safety risk. For example, among all the ship deficiencies, the 'fire safety', 'safety of navigation', 'life-saving appliances', 'emergency systems' and 'documents' have high probabilities of occurrence. In addition, the impacts of the probabilities of occurrence of 'MARPOL Annex II', 'MARPOL Annex III', 'anti-fouling' and 'minimum requirements for seafarers' are relatively low, which indicates that most of the ships can meet the requirements of pollution prevention and seafarers regulations.

# 4.3.2. Model validation 

Sensitivity analysis is conducted based on the 'entropy' theory to measure the interdependence among variables. In according to Equation (5), the mutual information between the 'detention' variable and all other 37 variables is computed, as shown in Table 6 .

## [Please insert Table 6 here]

As shown above, the top eight influencing factors contributing to ship detention come from all the three categories. The top two belong to the inspective activities, namely 'type of inspection' and 'place of inspection', followed by the safety condition of ships including 'safety of navigation' and 'fire safety'. The remaining four are 'gross-tonnage', 'type of ship', 'flag of ship' and 'classification society', which all belong to the technical features of vessel. Moreover, the pollution prevention deficiencies such as the 'Marpol annex I, II, III' and 'anti-fouling' show less impact on detention.

To reduce ship detention possibilities and improve the rationality of PSC inspections, the top eight factors mentioned above need more attention from both ship owners and port state authorities due to their high impacts on detention in order.

After the mutual information calculation is completed, another sensitivity analysis method, scenario simulation, was applied to further verify the reliability of the BN model. This method was introduced in the studies of Yang et al.,(2018) and Alyami et al., (2016), and is being used as a new and effective method to verify the data-driven BN models. The

basic principle of the validation process is: if the proposed BN model is reasonable and logical, it must satisfy the following two axioms:

Axiom 1. A slight increase/decrease in the prior probabilities of each parent node should certainly result in the effect of a relative increase/decrease of the posterior probabilities of the child node.

Axiom 2. The total influence magnitudes of the combination of the probability variations from $x$ attributes (evidence) on the values should be always greater than the one from the set of $x-y(y \epsilon x)$ attributes (sub-evidence).

Table 7 shows the calculation results of scenario simulation, in which the first row of the table represents the original detention rate, while the rest of the table presents the updated detention rate by constantly changing the risk probability of each influencing factor. The comparison with the initial detention rate shows that the proposed model satisfies both Axiom 1 and Axiom 2, which proves that the proposed model is reasonable and reliable.
[Please insert Table 7 here]

# 4.4 Useful insights for implications 

### 4.4.1 Dependency and interdependency among the factors influencing PSC inspections

This section is to identify the factors that are interactive and to determine how these influential factors are causally related to each other.

## The technical features of vessels

First of all, the variable of 'gross-tonnage' is a pure influential factor while arcs are originated from it to its child nodes. It influences other factors related to technical features of vessels (e.g. 'type of ship', 'flag of ship', 'classification society' and 'vessel age'). When the status of 'gross-tonnage' is known, 'type of ship', 'flag of ship', 'classification society' and 'vessel age' variables are conditionally independent. Meanwhile, Table 6 shows that the 'gross-tonnage' variable is ranked as the 5th most influential factors affecting the inspection results, which indicates the importance of the 'gross-tonnage' in PSC inspections.

# The inspective activities 

The two variables from the category of inspective activities, namely 'type of inspection' and 'place of inspection', have close relationships with other variables within the constructed network. Their child nodes cover almost all the factors, including certificates \& documentation, working and living conditions, labor conditions, pollution prevention, safety conditions and ISM, and others. Hence, the occurrence of above deficiencies highly depends on the status of 'type of inspection' and 'place of inspection'. For example, as shown in Figures 4 and 5 respectively, when the 'type of inspection' node is set to 'initial inspection' or 'follow-up inspection' respectively, the corresponding results of the deficiency probabilities are completely different. In the former case, the occurrence probabilities of deficiencies such as 'fire safety', 'safety of navigation', 'life-saving appliances', 'documents' and 'emergency systems' are high. However, in contrast, the occurrence probabilities of most deficiencies will significantly decrease in the latter case. Specifically, the occurrence probability of 'fire safety' decreases from $24.2 \%$ to $1 \%$. As a result, inspectors can make a rational decision, based on the specific inspection condition (i.e. initial or follow-up inspections), on how to prioritize their inspection items in PSC practice. The relationships among the factors influencing PSC inspections under dynamic environment can be effectively obtained in the same way via the model.
[Please insert Figures 4 here]
[Please insert Figures 5 here]

## The ship deficiencies

The deficiencies relating to safety condition reveal strong interdependence, in particular the 'safety of navigation' and 'fire safety'. As shown in Figure 6, the variables of 'Water/Weathertight conditions', 'Radio Communications', 'Life saving appliances', 'Fire safety', 'Structural Conditions', 'Cargo operations including equipment' are all the children of 'safety of navigation', while 'Water/Weathertight conditions', 'Emergency Systems', 'Propulsion and auxiliary machinery', 'Structural Conditions' are children of 'Fire safety' variable. If the 'yes' states of 'safety of navigation' is set to $100 \%$, the occurrence probabilities of other deficiencies will significantly increase. For instance, the probability of 'life saving appliances' will increase from $15.5 \%$ to $40.2 \%$.

# [Please insert Figures 6 here] 

The 'dangerous goods' deficiency has a strong correlation with ship technical features, however, its occurrence probabilities against different ship types significantly vary. For example, the probability of dangerous goods deficiency occurred on chemical tankers is $70.3 \%$, while the ones on general cargo/multipurpose ships and bulk carriers are only $13.4 \%$ and $16.3 \%$, respectively.

The deficiency of 'living conditions' shows strong interdependency with the one of 'working conditions'. Once ship deficiency of 'working conditions' occurs, the occurrence probability of 'living conditions' will rapidly increase from $0.56 \%$ to $3.91 \%$. Further, the occurrence of 'working and living conditions' deficiencies also depend on the status of 'fire safety' and 'propulsion and auxiliary machinery'. This raises the importance of improving the ship's facilities configuration. Similarly, 'health protection, medical care, social security' should be given high priority among four deficiencies of labor conditions, because its occurrence will affect the probability of 'accommodation, recreational facilities, food and catering' and 'conditions of employment'.

Unlike the above relationships, the node 'Pollution prevention - Marpol annex III' and 'Pollution prevention - anti fouling' are independent from other factors in the network. Additionally, the probabilities of pollution prevention related deficiencies are generally small. For instance, the probabilities of 'MARPOL Annex III' and 'anti-fouling' are only $0.025 \%$ and $0.034 \%$ respectively. Clearly, shipping companies' safety awareness on pollution prevention is kept at a more satisfactory level compared to safety-oriented deficiencies.

## Ship detention

The interdependence results between the influential factors and ship detention indicates that the probability of detention is highly affected by 'gross-tonnage', 'type of ship' and 'classification society'. In other words, the variation of detention possibilities at each port state authority can be explained by the different technical characteristics of ships calling at the corresponding port, rather than the differences caused by the specific inspections policies. This finding from Toyko MoU data is consistent with the research result from Cariou et al. [5] (using Paris MoU data). Detailed dependencies are illustrated in Figure

7. It is evident that the variables 'type of inspection', 'place of inspection', 'safety of navigation' and 'fire safety' are the parents of detention, which means they directly affect detention possibilities. Meanwhile, the above four variables are direct or indirect connected with 'gross-tonnage', 'type of ship' and 'classification society', indicating that detention possibilities have close relationship with the technical characteristics of ships.

# [Please insert Figure 7 here] 

In summary, the relationships among the variables could be effectively obtained through the developed model in this paper. It is necessary to emphasize that particular attention should be paid to the variables 'gross-tonnage', 'type of inspection', 'place of inspection', 'fire safety', 'safety of navigation', 'type of ship', 'classification society', 'working conditions' and 'labour conditions - health protection, medical care, social security'. It is because that the above-mentioned variables show stronger interconnection with other variables in the network and have higher impact on PSC inspection and detention. The quantitative impact of these variables on the target node is analysed and seen in Section 4.3.2 (i.e. Table 7).

### 4.4.2 Implementation in practice

In practical operations, the proposed model can be used as a decision aid tool for PSC inspectors, ship owners and other relevant stakeholders. For example, a general cargo/multipurpose was inspected in Vietnam on $27^{\text {th }}$ December 2016 and the specific inspection information was obtained as following:

Type of inspection: follow-up inspection
Gross-tonnage: 15000-20000
Type of ship: General cargo/multipurpose
Flag of ship: Liberia
Classification society: Nippon Kaiji Kyokai
Place of inspection: Vietnam
Vessel age: 15-20
Deficiencies: no (no deficiencies from V8 to V37 occurred)

Figure 8 shows the application the above information in the proposed model. The result shows that the probability of ship detention is predicted as 0 . It indicates that the ship is in a good condition and meets the PSC inspection standards with an extremely high probability and requires no need of inspection. In fact, this predication well reflects the actual inspection record at the time when vessel was inspected.

# [Please insert Figure 8 here] 

Similarly, a bulk carrier was inspected in Australia on $14^{\text {h }}$ June 2017, the specific inspection information was obtained as following:

Type of inspection: initial inspection
Grosstonnage: 35000 or more
Type of ship: Bulk carrier
Flag of ship: Hong Kong, China
Classification society: Bureau Veritas
Place of inspection: Australia
Vessel age: 10-15
Deficiencies: yes (ISM)
The model result of the above inspection is shown in Figure 9. The ship detention rate is predicted to be $9.92 \%$, which is nearly 5 times of the normal ship detention probability of $2.05 \%$. Meanwhile, it is much higher than that of the first case, which fully meets the PSC inspection standard. It means there will be hidden dangers when the ship continues to sail, and it must be detained. Consistent with the prediction results of the proposed model, the inspection records at that time showed that the ship was indeed detained.

## [Please insert Figure 9 here]

In addition, the model could also assist to analyze the characteristics of detained ships. As shown in Figure 10, when the 'place of inspection' node is set to 'Korea, Republic of ' and the node 'detention' is set to 'yes', it can be seen from the updated result that, among the detained ships in Korea, Republic of, $67.8 \%$ were bulk carriers, $18.6 \%$ were general cargo/multipurpose, while the vessels above 35,000 tons occupies the largest proportion. Additionally, Panama (the flag of ship) and Nippon Kaiji Kyokai (the classification society) are the most preferable types selected by ship owners. Among ship deficiencies, 'Life

saving appliances', 'Emergency Systems', 'ISM', 'Working conditions' and 'Documents' have higher occurrence probability than other deficiencies. Inspectors could better screen ships based on the characteristics of the detained ships calling at their ports to improve work efficiency and accuracy.
[Please insert Figure 10 here]

# 5. Conclusions 

Based on the PSC inspection data of seven Asian countries involving Tokyo MOU, this study proposes a BNs-based dynamic risk assessment model for analyzing the dependency and interdependency among the factors influencing PSC inspections. The results show that the constructed BNs model is effective in investigating the dependency and interdependency among the factors and identifying the most influential risk factors for ship detention. Furthermore, the prediction and cause-effect diagnosis of the detention probabilities of ships are carried out in a dynamic manner upon the available information in practical PSC operations. The paper pioneers the incorporation of 30 different types of deficiencies, as the key factors, in the ship detention risk model.

Among the factors influencing PSC inspections, it is suggested that particular attention should be paid to 'gross-tonnage', 'type of inspection', 'place of inspection', 'fire safety', 'safety of navigation', 'type of ship', 'classification society', 'working conditions' and 'labour conditions - health protection, medical care, social security'. Furthermore, the difference of the detention probabilities consistently mirrors the difference of the technical characteristics of the investigated ships, rather than inspection policies.

In terms of deficiency variables, the importance of ship safety condition related deficiencies are high. They have strong interdependence between each other. The occurrence of many deficiencies is due to 'fire safety' and 'safety of navigation'. Shipping companies is therefore suggested to strengthen their safety management coping with these deficiencies.

The proposed BN model is new in a sense of, for the first time, incorporating deficiency data into PSC risk assessment, and it has new findings contributing to the PSC literature

and generates significant implications in business practice, particularly in the Tokyo MoU region. Shipowners can use the model to assess the effect of different deficiencies on potential ship detention and rectify them precisely in a cost-effective manner. For shipping companies, it is beneficial to reduce the risk of detention as well as improve the company's PSC inspection performance. On the other hand, this model can be sued to guide port state authorities to improve their PSC inspection policies for identifying high risk ships to further strengthen maritime safety.

# Acknowledgment 

This research is sponsored by K.C.Wong Magna Fund in Ningbo University, Qianjiang Talent Project of Zhejiang Province of China (No. QJD1802022), and EU ERC consolidator grant under grant agreement No 864724 (TRUST) and Horizon 2020 research and innovation programmme under grant agreement No 823904 (ENHANCE).
