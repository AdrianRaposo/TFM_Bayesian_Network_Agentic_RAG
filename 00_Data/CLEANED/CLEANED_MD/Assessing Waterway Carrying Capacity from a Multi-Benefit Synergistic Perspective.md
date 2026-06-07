# Article 

## Assessing Waterway Carrying Capacity from a Multi-Benefit Synergistic Perspective

Yanyi Chen ${ }^{1}$ (D), Bozhong Zhou ${ }^{1}$ (D), Xiaofeng Pan ${ }^{2, *}$ (D), Hao Zhang ${ }^{3}$ (D), Honglu Qian ${ }^{4}$, Wen Cheng ${ }^{4}$ and Weiqing Yin ${ }^{4}$<br>check for updates<br>Citation: Chen, Y.; Zhou, B.; Pan, X.;<br>Zhang, H.; Qian, H.; Cheng, W.; Yin,<br>W. Assessing Waterway Carrying<br>Capacity from a Multi-Benefit<br>Synergistic Perspective. Sustainability<br>2024, 16, 4379. https://doi.org/<br>10.3390/su16114379<br>Academic Editor: Maria José Andrade Marques<br>Received: 23 March 2024<br>Revised: 9 May 2024<br>Accepted: 17 May 2024<br>Published: 22 May 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Transportation and Logistics Engineering, Wuhan University of Technology, Wuhan 430063, China; chenyanyi163@163.com (Y.C.); 13205990012@163.com (B.Z.)
2 Intelligent Transportation Systems Research Center, Wuhan University of Technology, Wuhan 430063, China
3 School of Management, Wuhan University of Technology, Wuhan 430063, China; hzhang@whut.edu.cn
4 Changjiang Institute of Survey, Planning, Design and Research, Wuhan 430010, China; qianhonglu@cjwsjy.com.cn (H.Q.); chengwen@cjwsjy.com.cn (W.C.); yinweiqing@cjwsjy.com.cn (W.Y.)

* Correspondence: x.pan@whut.edu.cn

Abstract: To support decision-making on the sustainable development of inland waterways, this paper proposes a framework for evaluating their waterway carrying capacity (WCC) from the perspective of different stakeholders and introduces an improved assessment method for WCC that combines the fuzzy belief rule and Bayesian network. Compared with traditional assessment methods, the proposed one can integrate the synergy of waterway multi-benefits into the carrying capacity and improve the accuracy of WCC assessment with data uncertainty. The method was applied to an empirical case of the middle Yangtze River from Yichang to Hukou, in which the current development status and the optimal development size in the future were obtained. The results and conclusions can provide insights and support for decision-making toward the development and maintenance of inland waterways.

Keywords: waterway carrying capacity; synergy; Bayesian network; fuzzy belief rule; Middle Yangtze River

## 1. Introduction

As waterway transportation accounts for more than $80 \%$ of the volume of all worldwide trade [1], the shipping industry is becoming increasingly important. Its advantages of safety, low emissions, cost effectiveness, and high throughput make waterways attract increasing attention in freight transport [2-5]. The importance of the sustainable development of inland waterways cannot be overstated and requires high demands on the development planning and operational management of waterways [6,7]. However, with the expansion of economic sizes, decision-makers would typically increase the channel size to meet the increasing transportation demand. However, the channel size of an inland waterway cannot be expanded without limitation given each inland waterway has its carrying capacity, which is mainly determined by the waterway's hydrological characteristics and geomorphological conditions [8,9]. Meanwhile, expanding the channel size often comes with various degrees of damage to the waterway ecosystem [10] and even to flood control safety, while the cost of making up for this damage is far greater than the benefits of channel expansion [11]. Therefore, it is necessary to carry out this study to adapt to the requirements of economic and social development and to guide the future planning and sustainable development of waterways.

Carrying capacity is a scientific concept that measures the interrelationship between human economic and social activities and the natural environment and has been widely studied in the fields of demography, ecology, and land science [12]. Specifically, the waterway carrying capacity (WCC) was described in many studies as the threshold of a

waterway that can be developed under the constraints of various factors [13-15]. Previous studies concerning the WCC mostly focused on the economic and ecological impacts on the thresholds of waterway development [14]. However, inland waterways have various other functions that cannot be ignored, such as flood control, water supply, and power generation [16]. In the year 2021, 59.01 million people were impacted by flood disasters in China, and the direct economic losses were up to CNY 245.89 billion [17]. Hence, flood control is an imperative function for inland waterways. At the same time, inland waterways are an important source of water supply for industry, agriculture, and drinking water [16], and hydropower contributes to the development of renewable energies and the security of water and energy supply [18]. Therefore, a comprehensive consideration of waterway multi-benefits is important for evaluating the WCC. However, as the number of factors to be considered increases, the carrying capacity evaluation system becomes more and more complex and some of the data are uncertain (e.g., incompleteness, vagueness). Considering the above views, the main objective of this study was to quantify and clearly define the carrying capacity of inland waterways based on a synergistic development scenario of ecology, economy, flood control, power generation, and water supply in order to identify the optimal development thresholds of waterways. The achievement of this objective will support decision-makers in providing rational allocation of limited waterway resources.

To achieve this objective, this study established a WCC evaluation index system to comprehensively assess the WCC from the perspective of multi-benefit synergistic use of waterways. In addition, by combining a Bayesian network (BN) with a fuzzy belief rule base (FBRB), an advanced WCC evaluation model was established to deal with uncertainty, which provides a basis for assessing the carrying capacity of different waterways at different spatial and temporal scales. Finally, this model was applied to the middle Yangtze River, which is an ideal case with a complex multi-branched reach, thus obtaining its development thresholds for the coming period. The novel contributions of this study are as follows: (1) A multi-dimensional synergistic evaluation model of WCC was developed from the vantage point of the whole waterway usage. This novel model, for the first time, incorporates the synergy between various benefits when quantifying the waterway's carrying capacity, facilitating a more comprehensive understanding and modeling of WCC. (2) The newly proposed WCC evaluation model adopts a fuzzy-rule-based structure to delineate the interactions between the root nodes within the BN model, which is instrumental in modeling the uncertainties concerning inter-node relations. Compared with current BN models, our proposal can overcome the deficiency of heavy scoring and judgment work required by experts, thereby expanding the BN's scope of application. (3) The proposed model was verified using the middle Yangtze River, and the results obtained can provide insights for the planning and management of the middle Yangtze River.

The remainder of this paper is structured as follows. The next section reviews the relevant literature and identifies the research gaps. Section 3 presents the new method of WCC evaluation. The feasibility and superiority of the proposed method are demonstrated in Section 4 with the case of the middle Yangtze River waterway. The main contributions of this study are discussed and summarized in Section 5.

# 2. Literature Review 

### 2.1. Concept of WCC

The concept of "carrying capacity" has its roots in the field of physics and originally referred to the greatest load that an object can support without suffering immediate harm [19]. Subsequently, this concept was extended to other related fields, such as demography, population biology, and applied ecology. On the other hand, related indicators are utilized to quantitatively assess the carrying state [20], which can be traced back to the population theory of Malthus [21]. Since then, many scholars have used similar terms, such as "saturation level" [22], "upper limit" [23], "maximum population size" or "S-curve asymptote" [24], and "holding capacity" [25], to describe carrying capacity depending on their particular disciplinary viewpoints.

However, the study of WCC was just recently undertaken, and the majority of studies have concentrated on waterway regulation technology and waterway passing capacity [26,27]. Hijdra et al. [8] suggested that the development of a waterway should take into account its multiple uses and values, in addition to the transportation purposes. Liu et al. [28] put forward the concept and prospect of WCC when studying waterway regulation technology, but did not involve the corresponding connotation and evaluation method.

Many studies focused on the influence of single factors on waterways, including the impacts of economic development or ecological protection [29,30]. With the enrichment of studies on WCC, studies have gradually examined the influence of two factors or multiple factors on the carrying capacity of waterways in recent years [14,31,32]. For instance, Zhao et al. [15] used the theory of system dynamics to develop a system structure of factors influencing the Yangtze River waterway's carrying capacity by considering ecological, economic, shipping, and social factors. Li et al. [14] defined the WCC as the ability of a waterway to carry sustainable socio-economic development at a certain scale within a certain period of time and a certain river section. Wang et al. [31] considered WCC as the exploitable limit of channel scale (depth $\times$ width $\times$ radius) in response to the coordinated needs of flood control, economic demand, river ecology, and water resources allocation required for the sustainable development of a waterway. Regrettably, although these investigations recognized the significance of evaluating WCC from a multi-benefit perspective, they overlooked the essential synergistic interrelations between these benefits.

# 2.2. WCC Evaluation Methods 

Compared with other resource carrying capacities, the research on the evaluation model of WCC is still in the initial stage [33,34]. Generally speaking, the carrying capacity level of a waterway can be finally reflected by the maximum developable scale, which is usually estimated using the stable navigation depth method [35]. Specifically, the maximum developable depth of a waterway is calculated based on the river-facies relationship under the flow of good river sections. However, this approach ignores the numerous functional advantages of waterways, including the economic and ecological advantages. Li et al. [14] investigated the impact of economic demand on WCC and utilized the supply-demand balance method to assess the WCC. The defects of this evaluation method are similar to the stable navigation depth method, which only considers some of the factors that affect the carrying capacity of a waterway. To assess the sustainability of global golden inland waterways, Wang et al. [32] suggested a hierarchical model, which reveals the sustainable evolution and appropriate development sizes of inland waterways at different stages of development from a global perspective based on a multi-dimensional evaluation index system. However, it does not involve the specific impacts of various factors in the model on the development scale and does not reflect the maximum exploitable scale of the waterway. Wang et al. [31] developed a comprehensive evaluation model of WCC. They also investigated a comprehensive evaluation method that combines the two evaluation techniques of comprehensive index evaluation and fuzzy pattern recognition with the AHP. Compared with each other, the two methods can more objectively reflect the carrying capacity levels of different grades. However, these studies failed to capture the degree of synergy between the demands, and it is difficult to examine the state of mutual constraints or coordinated development between the demands.

It merits attention that the previous methods of assessing WCC seldom address the inherent uncertainties of such evaluations, and they fail to capture the intricate interplay between diverse contributing factors. Thus, there is an urgent need for a new methodology to address these uncertainties, and a BN offers a promising tool to meet this need.

### 2.3. Bayesian Network

A BN (also known as a belief network) approach is based on well-defined Bayesian probability theory and network techniques [36]. A BN is a graphical representation of probability, which when combined with mathematical reasoning calculations, provides a

powerful framework for representing knowledge. It is also well suited to modeling randomness and capturing non-linear causality, thus enabling reasoning based on incomplete, imprecise, and uncertain information. As an approach that is both mathematically rigorous and intuitively understandable [37], the BN approach has been applied in a range of practical applications, particularly when it comes to the prediction and diagnosis of complex system properties. For example, Wang et al. [38] established a Bayesian-network-based environment-water resource carrying capacity overloading risk assessment method system for determining the probability distributions of environment-water carrying capacity and water resource carrying capacity to compute the carrying state of a water system and its corresponding probabilities by means of Bayesian formulations and spatiotemporal laws. Fan et al. [39] introduced a novel model that incorporates fuzzy logic and Bayesian networks to evaluate the resilience of a strait. Overall, the application of a BN to the evaluation of WCC, which is a complex system, is appropriate.

# 2.4. Research Gap 

In summary, the concept of WCC is defined in this paper as the maximum exploitable scale of the waterway (depth $\times$ width $\times$ radius) of a certain area under the synergistic development of various demands, with the natural resources and environment as the basic condition; economic development as the supporting condition; and flood control, ecology, and water supply as the constraint conditions. Some specific research gaps can be identified regarding this definition and previous studies:
(1) Most previous studies on the evaluation of WCC paid special attention to the impacts of economic or ecological demands on waterway development [13,32], and only a few studies examined WCC from multiple dimensions [15,31]. However, all these studies neither mention the synergistic effect between the dimensions nor consider its specific impact on the carrying capacity, resulting in evaluation results that cannot reflect the real level of the carrying capacity.
(2) Considering the contradiction between the sustainable development of waterways and the utilization of resources, as well as the complexity of the interactions between various demands, the subsystems of WCC and the factors for their evaluation tend to be uncertain, and the corresponding relationships tend to be non-linear. The current methods for quantitatively analyzing the WCC expose incapability and drawbacks in dealing with such issues. For example, the fuzzy comprehensive evaluation method, as a widely used method to deal with uncertainties and non-linearities in the evaluation of the carrying capacity, has a complexity of computation that is not friendly to users who do not have strong mathematical ability and have the drawbacks of excessive subjectivity in the setting of the elemental weights [40,41]. In addition, a much-debated limitation of Bayes is that too much information is needed to construct a conditional probability table, which is nearly impossible to obtain in WCC assessments due to the complexity of the metrics at multiple scales.

To fill in the research gaps, this paper proposes a method that combines the fuzzy belief rule and Bayesian network for WCC evaluation. This is achieved by the following: (1) the establishment of a multilayer evaluation index system based on four aspects (i.e., ecology, water supply, economy, and flood control) and the introduction of the degree of synergy between subsystems into fuzzy rules into the process of evaluating the WCC; (2) fuzzy logic to model the relationship between WCC and influencing factors and a Bayesian network to reason from uncertain information [36,42]; (3) fuzzy belief rules combined with the AHP method, in which the calculated weights are assigned to the consequent part of the rule to solve the problem that the rule base is difficult to establish due to incomplete information.

## 3. Methods

The availability and accuracy of data, the difficulty of methods, and the complexity and uncertainty of the interrelationships between factors are the key elements that affect the selection of WCC evaluation methods [43]. To fully reflect the complex concept of WCC, it

is necessary to cover as many factors that affect WCC as possible. However, because some objective data are extremely difficult to obtain, this would inevitably require the supplement of qualitative indicators and subjective information, which brings in the uncertainty of WCC evaluation. On top of this, waterways in different regions are characterized differently and WCC influence factors vary from region to region, which is another key factor that contributes to the uncertainty in WCC evaluation. In this sense, this paper proposes a method that combines fuzzy belief rules with Bayesian networks to evaluate WCC under uncertainty. The method transforms qualitative and quantitative indicators into a unified linguistic evaluation grade, uses fuzzy logic to deal with the ambiguity of the data, and adopts Bayesian inference to aggregate the relevant rules. This proposed method has the ability to flexibly model the relationship between each demand and WCC and the ability to reflect the interrelationships of various factors by combining expert judgment and statistical analysis, thus eliminating the uncertainty in WCC evaluation.

The major research steps for WCC evaluation are shown in Figure 1 and there were three phases. Phase 1 (establishment of indicator evaluation systems): In this phase, a WCC evaluation system was established from the perspective of multi-benefit utilization of waterways, and the weights were calculated by the AHP method. Then, the indicator data were transformed into a unified evaluation grade to obtain the a priori probability. Phase 2 (construction of evaluation network): FBRBs were constructed, in which synergy was taken as a new parameter input, and the FBRBs were combined as conditional probability tables with the a priori probability for the BN inference. After this, the inference results were quantified and classified. Phase 3 (results and analysis): the model was applied to the case to obtain the WCC of the middle Yangtze River and further analyzed and discussed.
![img-0.jpeg](img-0.jpeg)

Figure 1. The major research steps of evaluating WCC.

# 3.1. Evaluation Index System of WCC 

### 3.1.1. The Multi-Layer Evaluation Index System

The indicators of WCC should be selected in a scientific, clear, and representative manner, taking into account a variety of components, including ecology, water supply, economy, and flood control. Since the essence of the research on WCC is the scale of the waterway, the research on the factors affecting WCC should be conducted by combining the factors affecting the scale of the waterway and the passing capacity of the waterway.

The selected indicators should be comprehensive, quantitative, or qualitative. They should not only respond to real-time changes and adapt to the needs of social development but also ensure the relative stability of the evaluation of WCC over a certain period.

An evaluation model of WCC was proposed based on the study of the influencing factors of WCC [15]. First, WCC is the central component of the model and solely composes the target layer. Second, the WCC is directly impacted by four subsystems that make up the subsystem layer. Third, the indicator layer is made up of the 17 subordinate indicators, which are the specific elements influencing the WCC (Figure 2). The definitions of the evaluation indicators are detailed in Table A1.
![img-1.jpeg](img-1.jpeg)

Figure 2. WCC evaluation system.

# 3.1.2. Determination of Indicator Weights 

Considering the multi-dimensionality, multiple indicators, complexity, and other characteristics of the WCC evaluation index system, this study adopted the AHP for the weight allocation to ensure reasonableness and accuracy and to reduce the bias brought about by weighing a large number of indicators simultaneously [44].

AHP establishes judgment matrices for each indicator based on the hierarchical structure of the evaluation indicator system. The importance of each factor is measured using a 9-point Likert scale from 1 to 9 , which is used to calculate the corresponding relative weight to the indicators in the previous layer. Therefore, the relative weight of each indicator to

Table 1. Determination of index weights.


# 3.1.3. Calculation of the Membership Degree 

We defined a set of fuzzy language grades to facilitate subjective data collection and representation of judgments associated with the WCC and related influencing factors. With reference to the relevant studies, we suggest the following set of linguistic grades: Collapsing, Unbearable, Critical bearable, Bearable, and Fully bearable [15,31]. It is notable that the number of linguistic grades and their definitions are flexible and can be tailored based on the specific characteristics of waterways. Meanwhile, since both quantitative and qualitative indicators are included in the evaluation system, they should be transformed into a unified fuzzy language grade. Consequently, the grades of qualitative indicators are defined in Table 2.

Table 2. Definition of linguistic evaluation grade for qualitative indexes.


To translate quantitative indicators into evaluation levels harmonized with qualitative indicators. The membership degree of quantitative indicators can be obtained through the fuzzy triangular distribution and fuzzy trapezoidal distribution shown in Figure 3, in which the letters a, b, c, d, and e denote the maximum possible values of Collapsing, Unbearable, Critical bearable, Bearable, and Fully bearable, respectively. Suppose a subsystem has a score of $x$ :
(1) When $x \leq a$, the grading is $100 \%$ Collapsing;
(2) When $a<x<b$, the grading is Collapsing with a probability $(b-x) /(b-a)$ and Unbearable with a probability $(x-a) /(b-a)$;
(3) When $b \leq x<c$, the grading is Unbearable with a probability $(c-x) /(c-b)$ and Critical bearable with a probability $(x-b) /(c-b)$;
(4) When $c \leq x<d$, the grading is Critical bearable with a probability $(d-x) /(d-c)$ and Bearable with a probability $(x-c) /(d-c)$;

(5) When $d \leq x<e$, the grading is Bearable with a probability $(e-x) /(e-d)$ and Fully bearable with a probability $(x-d) /(e-d)$;
(6) When $x \geq e$, the grading is $100 \%$ Fully bearable.
![img-2.jpeg](img-2.jpeg)

Figure 3. Graph of membership degree function.
In this study, the grade thresholds of the quantitative indicators were obtained from historical data, Chinese national standards, relevant research results, and expert judgment $[15,45-47]$, as depicted in Table 3.

Table 3. Thresholds of linguistic evaluation grades for quantitative indexes.


# 3.2. Methodology behind the FBRB and BN 

### 3.2.1. Degree of Synergy

The coupling synergy model can be used to calculate the degree of synergy development between subsystems within the system, that is, the degree of interaction between subsystems [48], as shown below:

$$
\begin{gathered}
D=(C \times T)^{1 / 2} \\
C=m\left\{\left(U_{1} \times U_{2} \cdots U_{m}\right) /\left(U_{1}+U_{2} \cdots U_{m}\right)^{m}\right\}^{1 / m} \\
T=\sum_{i=1}^{4} W_{i} U_{i}
\end{gathered}
$$

where $D$ is the degree of synergy; $T$ is the subsystem-integrated synergy index, which reflects the overall synergistic effect of the system; $C$ is the system coupling degree, which can determine whether the subsystems are adapted to each other; $m$ is the number of subsystems; $U_{i}$ is the utility value, which represents the contribution of subsystem $i$ to the order degree of the total system; and $W_{i}$ is the weight of subsystem $i$.

# 3.2.2. Fuzzy Belief Rule 

Fuzzy rules are derived from fuzzy set theory and typically use "IF-THEN" rules to represent the mapping relationship between two domains. The general form of a fuzzy rule is as follows: if x is A , then y is B [36], where A and B are fuzzy sets defined by linguistic values on the domains x and y , respectively. " x is A " is known as the premise and " y is B " is the conclusion.

Since an absolute mapping relationship between linguistic values may not be established in practical applications, scholars have proposed fuzzy rules based on belief degrees [49]:

$$
\begin{aligned}
R_{k}: & \text { IF } A_{1}^{k} \text { and } A_{2}^{k} \text { and } \ldots \text { and } A_{M}^{k} \\
& \text { THEN } \backslash\left\{\left(D_{1}, \beta_{1}^{k}\right),\left(D_{2}, \beta_{2}^{k}\right), \ldots\left(D_{N}, \beta_{N}^{k}\right)\right\} \\
& \left(\sum_{j=1}^{N} \beta_{j}^{k} \leq 1\right)
\end{aligned}
$$

where $\beta_{1}^{k}(i=1,2, \ldots, N)$ is the degree of belief (DoB) to which $D_{j}$ is considered to be the consequence in the $k$ th packed rule when the input meets the antecedents $A_{k}=\left\{A_{1}^{k}, A_{2}^{k}, \ldots, A_{M}^{k}\right\}$; $N$ is the total number of possible consequences; and the $k$ th rule is considered completely only when $\sum_{j=1}^{N} \beta_{j}^{k}=1$.

### 3.2.3. BN

A Bayesian network's structure is a directed acyclic graph $(E, A)$, where nodes represent variables $E=\left\{E_{1}, E_{2}, \ldots, E_{n}\right\}$, and the relationships between variables are indicated by directed arcs $A$. The direction of an arc goes from a cause node to a consequent node, that is, from a parent node to a child node. Nodes that are not directly connected represent independence from each other. The parameters of a Bayesian network are the conditional probability tables (CPTs) that represent the relationships between variables, represented as $P\left(E_{i} \mid P_{a}\left(E_{i}\right)\right)$. They signify the interdependencies between variables. In other words, a Bayesian network is composed of a network structure with interdependent relationships between nodes and conditional probability tables that connect the variables. For directed edges $\left(E_{i}, E_{j}\right)$, the parent nodes of $E_{i}$ are represented as $P_{a}\left(E_{i}\right)$, and non-descendant nodes can be represented as $A\left(E_{i}\right)$. Under the condition of given parent nodes, non-descendant nodes are conditionally independent of the parent nodes, as shown in Equation (5). From this, the joint probability can be obtained as shown in Equation (6).

$$
\begin{aligned}
P\left(E_{i} \mid P_{a}\left(E_{i}\right), \mathrm{A}\left(E_{i}\right)\right) & =P\left(E_{i} \mid P_{a}\left(E_{i}\right)\right) \\
P\left(E_{1}, E_{2}, E_{3}, \ldots E_{K}\right) & =\prod_{i=1}^{k} P\left(E_{i} \mid E_{i-1}, E_{i-2}, \ldots E_{i}\right) \\
& =\prod_{i=1}^{k} P\left(E_{i} \mid P_{a}\left(E_{i}\right)\right)
\end{aligned}
$$

### 3.3. Construct and Variables

### 3.3.1. Establishment of the FBRB

As shown in Figure 2, the index system of WCC has three layers with four subsystems. Therefore, five FBRBs need to be established in total to evaluate the carrying capacity of the four subsystems and the waterway. This section takes the establishment process of the FBRB that represents the fuzzy logic between the WCC and the subsystems as an example. Other FBRBs are similar, only except for the degree of synergy.

In the WCC system, there is a certain contradiction between the subsystems, such as competition for water rights, unequal distribution of resources, and different goals at different stages of development. Obviously, there are non-linear relationships between them, and the influence of the degree of synergy on the evaluation of the WCC cannot be effectively supported by objective data to a large extent. Therefore, a method based on fuzzy belief rules was adopted in this study. Based on the demand factor of the WCC, the FBRB can be described according to Equation (4).

In the process of building the FBRB, the four subsystems and the degree of synergy were taken as the antecedent attributes of the fuzzy rules (the IF part), as represented by E (ecology), W (water supply), EC (economy), F (flood control), and S (synergy). The WCC is the consequent attribute (the THEN part). The DoB is assigned to the fuzzy linguistic grade that is used to describe the consequent attribute WCC in the FBRB. Among the antecedent attributes, the degree of synergy expressed as a numerical value can be converted into corresponding grades by means in Figure 3.

Regarding the results of the FBRB, the DoB of the rules can be assigned based on the knowledge accumulated from past events [50], or directly derived from experts' opinions [51]. But in practice, for a large belief rule base with hundreds of rules, it is very difficult to make accurate and reasonable belief assignments based on the subjective knowledge of experts alone. In recognition of this, Alyami et al. [50] proposed a proportion method to calculate the DoB. This method provides a simple, intuitive, and logical way to calculate the belief level of the THEN part. However, it ought to be noted that the method ignores the relative importance of the antecedent attributes when assigning the DoB, which may lead to a significant deviation in the results when the importance of the attributes varies greatly. Therefore, the relative importance of antecedent attributes should be taken into account when assigning the DoB.

In the current study, the weights of each antecedent attribute calculated by the AHP method (Table 1) were used as the basis for the DoB assignment. Furthermore, because of the difficulty in quantifying the impact of synergy on the WCC, an equal proportional weight of 0.2 was assigned to the synergy, and the weights of the remaining antecedent attributes were adjusted accordingly ( $W_{i} \times 0.8$ ). All attributes in the rule were described by the same linguistic variables, and for any particular consequent attribute, the DoB belonging to a particular grade could be calculated by summing the normalized weights of all antecedent attributes of the same grade. Rule 3 provides an instance:

Rule \#3: IF E is Collapsing, W is Collapsing, EC is Collapsing, F is Critical bearable, S is Unbearable with a 0.52 DoB , and Critical bearable with a 0.48 DoB , THEN the WCC is Collapsing with a 0.64 DoB, Unbearable with a 0.1 DoB, Critical bearable with a 0.26 DoB , Bearable with a 0 DoB , and Fully bearable with a 0 DoB .

When calculating the synergy, the numbers from 0.2 to 1 with an increment equaling 0.2 are used to map the utility value of each grade of carrying capacity, where 0.2 indicates the lowest grade (Collapsing) and 1 indicates the highest grade (Fully bearable). The synergy of the rule equals 0.496 according to Equation (1) and is transformed to linguistic evaluation grade Unbearable with a 0.52 DoB and Critical bearable with a 0.48 DoB based on Figure 3. The total weights of all antecedent attributes with Collapsing, Unbearable, and Critical bearable grades are $0.64((0.215+0.143+0.442) \times 0.8), 0.1(0.52 \times 0.2)$, and $0.26(0.2 \times 0.8+0.48 \times 0.2))$, respectively. Likewise, an FBRB for evaluating the WCC containing $625\left(5^{4}\right)$ rules can be developed, partly as shown in Table 4.

# 3.3.2. Aggregation Rules Using Bayesian Networks 

Once all the data are converted into defined linguistic grades, rule aggregation can be performed using Bayesian networks. The reason for using this technique in this study is that Bayesian networks can overcome the drawbacks of traditional rule aggregation methods, such as the complexity of the evidential reasoning method, and can provide results quickly and accurately [36]. Moreover, it has a great ability to capture non-linear causality, which enables it to handle rule bases with a complex large number of rules [50].

Table 4. The FBRB in the assessment of WCC.

Bearable | Bearable | Fully
Bearable  |

First, the FBRB is converted into the form of a conditional probability. Since the degree of synergy is co-determined by other antecedent attributes, it is not an independent attribute. Meanwhile, in order to be consistent with the expression form of conditional probability, the output that involves the degree of synergy is adopted, while the input parameter of the degree of synergy during the conversion is eliminated. Rule 3 can be expressed using Equation (4) as follows:
$\mathrm{R}_{3}$ : IF Collapsing (E1), Collapsing (W1), Collapsing (EC1), and Critical bearable (F3), THEN \{(Collapsing (WCC1), 0.64), (Unbearable (WCC2), 0.1), (Critical bearable (WCC3), 0.26), (Bearable (WCC4), 0), (Fully bearable (WCC5), 0)\}.

Based on Equation (5), this rule can be further expressed in the form of a conditional probability as follows:

Given $E 1, W 1, E C 1$, and $F 3$, the probability of $W C C h(h=1,2,3,4,5)$ is $(0.64,0.1,0.26,0,0)$, or

$$
p(W C C h \mid E 1, W 1, E C 1, F 3)=(0.64,0.1,0.26,0,0)
$$

where the symbol "|" denotes a conditional probability.
In Bayesian networks, an FBRB can be modeled and transformed into a converging connection consisting of five nodes: including four parent nodes, denoted as $N_{E}, N_{E C}$, $N_{W}, N_{F}$ (nodes $E, W, E C, F$ ), and one child node, denoted as $N_{W C C}$. After transforming the FBRB into a Bayesian network, the assessment of WCC is simplified to calculate the marginal probability of node $N_{W C C}$. To marginalize the WCC, the conditional probabilities required for $N_{W C C}$ are obtained using Equation (7) and the result is a table containing the following values:
$p(W C C h \mid E i, W j, E C k, F l)(h, i, j, k, l=1,2,3,4,5)$ (see Table A2).
The prior probabilities of parent nodes NE, NEC, NW, and NF are obtained by Bayesian inference from the membership degree of the corresponding indicator, which are represented by $p(E i)=\beta_{i}, p(W j)=\beta_{j}, p(E C k)=\beta_{k}$, and $p(F l)=\beta_{l}$, respectively. The marginal probability of $N_{W C C}$ can be calculated from Equation (8) [52]:

$$
\begin{aligned}
& p(W C C)=\sum_{i=1}^{5} \sum_{j=1}^{5} \sum_{k=1}^{5} \sum_{l=1}^{5} p(W C C h \mid E i, W j, E C k, F l) p(E i) \\
& p(W j) p(E C k) p(F l(h=l, 2,3,4,5)
\end{aligned}
$$

# 3.3.3. Quantify and Classify WCC 

Appropriate utility functions are desired to translate the DoB into explicit values and to determine the specific level of carrying capacity. In this study, the numerical preference values are linearly assigned to describe the preference degrees of the five linguistic grades based on utility theory [39]: the values of $U_{W C C h}$ are $U_{W C C 1}=0.2, U_{W C C 2}=0.4, U_{W C C 3}=$ $0.6, U_{W C C 4}=0.8$, and $U_{W C C 5}=1.0$.

Equation (9) is used to generate the score of WCC $(S W)$. The larger the $S W$ value, the better the carrying capacity of the waterway:

$$
S W=\sum_{h=1}^{5} p(W C C h) U_{W C C h}
$$

In order to identify the hierarchy of the carrying capacity more comprehensively for stakeholder analysis and decision-making, the levels of carrying capacity are defined using the $S W$, as shown in Figure 4. The advantage of this approach is that it allows for a more comprehensive consideration of uncertain information and does not result in any loss of belief information compared with other methods, such as the maximum membership principle [31].

![img-3.jpeg](img-3.jpeg)

Figure 4. Levels of WCC and corresponding thresholds of $S W$.
To illustrate the influence of incorporating the degree of synergy on the evaluation of WCC, Rule 619 and Rule 526 are used as instances:

Rule \#619: IF Fully bearable (E5), Fully bearable (W5), Bearable (EC4), and Bearable (F4), THEN {(Collapsing (WCC1), 0), (Unbearable (WCC2), 0), (Critical bearable (WCC3), 0), (Bearable (WCC4), 0.58), (Fully bearable (WCC5), 0.42)}.

Regarding Rule 619, the degree of synergy is 0.93 according to Equation (1), with a grade of Bearable with a 0.35 DoB, Fully Bearable with a 0.65 DoB, and the WCC score for Rule 619 is calculated based on Equation (9):

$$
\begin{aligned}
& S W=\sum_{h=1}^{5} p(W C C h) U_{W C C h} \\
& =0 \times 0.2+0 \times 0.6+0.58 \times 0.8+0.42 \times 1.0 \\
& =0.884
\end{aligned}
$$

When this rule does not involve the degree of synergy, its WCC score drops to 0.87 .
Rule \#525: IF Fully bearable (E5), Collapsing (W1), Fully bearable (EC5), and Fully bearable (F5), THEN {(Collapsing (WCC1), 0.11), (Unbearable (WCC2), 0), (Critical bearable (WCC3), 0), (Bearable (WCC4), 0.14), (Fully bearable (WCC5), 0.75)}.

Similarly, the WCC score for Rule 525 equals 0.880 . When Rule 525 ignores the degree of synergy, the score is increased to 0.885 . When the degree of synergy is not taken into account, it can be seen that Rule 525 's WCC score is higher than Rule 619 's. However, since Rule 525 's subsystems have a large carrying capacity gap, the synergy is relatively poor. As a result, the carrying capacity of Rule 525 is not as good as that of Rule 619 after taking the degree of synergy into account.

# 3.4. Data and Measures 

The middle Yangtze River serves as the primary habitat and breeding grounds for the four major Chinese carps: black carp (Mylopharyngodon piceus), grass carp (Ctenopharyngodon idellus), silver carp (Hypophthalmichthys molitrix), and bighead carp (Aristichthys nobilis). The conservation of these natural fish populations in the Yangtze River is vital for preserving the genetic diversity of the species and for the sustainable progress of the freshwater aquaculture industry [53]. Consequently, these four major Chinese carps were chosen as indicator species. Considering the depth and flow suitability, the habitat suitability index (HSI) for the middle Yangtze River could be calculated based on the habitat suitability equations given by Guo et al. [54] for the spawning and incubation periods of the four

major Chinese carp species. Moreover, according to Yu et al. [53], HSI $<0.5$ indicates poor, HSI between 0.5 and 0.8 indicates moderate, and HSI $>0.8$ indicates ideal.

A two-dimensional flow model was established using the body-fitted orthogonal curvilinear grid that fits the river channel characteristics. The governing equations and numerical solutions of the model can be found in Lu et al. [55]. Besides providing velocity and depth data for calculating the HSI, the two-dimensional flow model also enables the calculation of the stage-discharge relationship of specific reaches based on the hydrological data of the control station, which determines the navigation guarantee rate that meets the minimum navigable water level. Moreover, it supplies data on each indicator in the flood control subsystem, including the assessment of the impact on nearshore flow velocity and water level in specific river sections due to navigational channel regulation projects, the prediction of changes in the diversion ratio after project implementation, and the calculation of the blocking rate for regulating projects based on layout and size.

To simulate the complex boundary conditions and the main characteristics of sandy riverbed types in the middle reaches of the Yangtze River, we developed a two-dimensional sediment mathematical model [56]. On the one hand, the sediment model was combined with the flow model to predict and analyze the effect after the implementation of the regulation and determine the project scheme. On the other hand, the river adjustment affected by the regulation was analyzed, and the grade of the river regime stability index in the flood control dimension was determined. Data for other indicators were determined by reference to relevant historical statistical yearbooks and research literature. The sources of data for all indicators are shown in Table A1.

# 4. Analysis and Results 

To test the applicability of the proposed model in the middle Yangtze River, the Jiepai reach in the section from Chenglingji to Wuhan was taken as a case study. On the one hand, there is a main shallow located near the right trough of the entrance of the Jiepai channel bar, which shows a tendency of gradual deposition. Furthermore, the channel bar is in the process of periodic conversion from the right trough to the left, which indicates that the conditions of the channel are unstable. On the other hand, the selected section is covered by the National Nature Reserve for White-Flag Dolphins, where a region from Luoshan to Xinyuzhoutou (about 16 km ) are buffer and experimental zones and from Xinyuzhoutou to Shimatou (about 12 km ) and upstream from Luoshan (about 4 km ) are the core zones. Therefore, it has a high demand for ecological protection.

To sum up, the selected sections are the key sections of the middle Yangtze River for waterway transportation and are also constrained by the high demand for ecological protection. Thus, it is a representative case for the assessment of the carrying capacity of waterways.

### 4.1. Design of Regulation Program of Waterway Scale

By comparing the WCC of the waterway at different scales, the optimal development scale could be determined. Currently, the maintenance scale of the selected channel is $4.2 \times 150 \times 1000 \mathrm{~m}$, and the stable navigation depth method can be used to intuitively and efficiently predict the maximum scale based on the excellent hydraulic geometry [57]. Based on the analyses of the cross-sections from more than 10 parts during the dry season, it was calculated that when the proposed channel width is 200 m (i.e., the planned channel width of the middle Yangtze River), the maximum stabilized navigable depth is between 9.0 m and 9.5 m . According to the current status of the channel and the maximum stabilized navigable depth after regulation, three waterway scale programs are proposed for the following WCC evaluation: $6.0 \mathrm{~m} \times 200 \mathrm{~m} \times 1000 \mathrm{~m}$ (designed scale 1), $9.0 \mathrm{~m} \times 200 \mathrm{~m} \times 1000 \mathrm{~m}$ (designed scale 2), and $4.2 \mathrm{~m} \times 150 \mathrm{~m} \times 1000 \mathrm{~m}$ (the status quo scale).

In response to the navigation obstructions of the Jiepai reach, the following regulation program is proposed. First, lengthen the spur dikes on the right riverbank, and build two new spur dikes on the left bank. Second, build two submerged dikes in the upper section of

the left trough of the channel bar, and build a training dike and four beach protection belts at the head of the channel bar. Third, deepen the original 6 m deep channel to a 9 m deep one, and build another submerged dike between the two submerged dikes. Fourth, raise the existing channel bar to 0.5 m above the regulation water level, and build a new spur dike on the left bank with the elevation of the dam crest being controlled at the regulation water level.

# 4.2. Model Application 

### 4.2.1. Evaluation of WCC of Jiepai Reach

For the proposed regulation project, the evaluation indexes of the selected section at three waterway scales are shown in Figure 5. The membership degree of each indicator was calculated based on the fuzzy membership function in Figure 3, and the results under the status quo scale are shown in Table 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Index data for waterway at different scales.
Table 5. Membership degree of each index at the status quo scale of Jiepai reach.


The WCC inference was obtained by transforming the membership degree into the form of an a priori probability using Equation (7).

Using Equation (8), the status quo WCC could be calculated as $\mathrm{p}(W C C h)=\left(14.3 \%\right.$, $2.6 \%, 13.7 \%, 36.9 \%, 32.5 \%$ ), which is represented as \{(Collapsing, 14.3\%), (Unbearable, $2.6 \%$ ), (Critical bearable, 13.7\%), (Bearable, 36.9\%), (Fully bearable, 32.5\%)\}. The calculation was modeled using GeNIe 4.0 software to facilitate the Bayesian network computation.

As Figure 6 shows, any input modification related to the seventeen indexes triggered the change in the output nodes. This helped to automate the immediate WCC evaluation for any target waterway in the middle Yangtze River. Likewise, the WCC of the selected section under different scales could be obtained as follows:
![img-5.jpeg](img-5.jpeg)

Figure 6. WCC evaluation of "the Jiepai reach at the status quo scale" (using GeNLE 4.0 software).
WCC under designed scale 1
$=\mid$ (Collapsing, 1.7\%), (Unbearable, 21.9\%), (Critical bearable, 15.1\%), (Bearable, 23\%), (Fully bearable, 38.3\%) $\mid$;

WCC under designed scale 2
$=\mid$ (Collapsing, 18.3\%), (Unbearable, 3.1\%), (Critical bearable, 16.0\%), (Bearable, 25.8\%), (Fully bearable, 36.8\%) $\mid$;

The WCC expressed by the linguistic variables and DoB needs to be further analyzed for its score. The $S W$ under the status quo scale was calculated by Equation (9):

$$
\begin{aligned}
& S W_{\text {statusquo }}=\sum_{h=1}^{5} p(W C C h) U_{W C C h} \\
& =0.143 \times 0.2+0.026 \times 0.4+0.137 \times 0.6+0.369 \times 0.8+0.325 \times 1.0 \\
& =0.741
\end{aligned}
$$

Meanwhile, the $S W$ values at designed scale 1 and designed scale 2 were 0.748 and 0.719 , respectively. Therefore, the WCC was at a maximum (i.e., optimal) under designed scale 1 compared with those under other scales.

# 4.2.2. Analysis of Variation in Subsystems 

Similar to the calculation of the $S W$ of the waterway, the $S W$ of each subsystem could be obtained as demonstrated in Figure 7 and the corresponding grades could be obtained according to Figure 4.

![img-6.jpeg](img-6.jpeg)

Figure 7. Scores of the carrying capacity for the four subsystems at different waterway scales.

# 1. Ecological subsystem 

By aggregating the scores across six distinct indicators under varying scales, we observed a progressive shift in the evaluation of the ecological subsystem from Critical bearable to Bearable with the scales increasing. Notably, the primary driver behind this shift lay in the reduction rate of ship energy consumption (C6). The expansion of the waterway scale resulted in an increased passage rate of larger vessels, further leading to a substantial improvement in C6. Conversely, the remaining economic indicators exhibited negligible changes.

## 2. Water supply subsystem

The minimum navigable flow rose quickly as the waterway scale rose, and the guarantee rate of shipping water demand (C8) exhibited an obvious downward trend. In comparison with the carrying score of 0.96 for the score of water supply subsystem under the status quo scale, the rapid decline in C8 due to the increase in the waterway scale resulted in the grades of water supply subsystem under designed scales 1 and 2 being reduced to Critical bearable.

## 3. Economy subsystem

The linguistic evaluation of the economic subsystem under the status quo scale was Unbearable due to the collapse of C10. Compared with the rest of the subsystems, the economic subsystem displayed clear inadequacies and the synergy degree between the subsystems was low, which inhibited the coordinated development of the subsystem. When the waterway scale was increased, all the economic indicators except C12 were greatly increased, and the evaluation grades of the designed scales 1 and 2 were both increased to Critical bearable.

## 4. Flood control subsystem

A two-dimensional hydrodynamic mathematical model was developed to obtain the data about the flood control indexes. The collected data illustrate that the increase in the waterway scale would lead to a decrease in several indicators (C14, C15, C16, C17) of the flood control subsystem to various degrees. The linguistic evaluation grade of the flood control subsystem under the status quo scale was Fully bearable, whereas the upgraded waterway scale reduced the grade of the flood control subsystem under the designed scale 1 to Critical bearable. However, the grade fell to Unbearable under designed scale 2, indicating substantial flood safety pressures in the waterway. This discrepancy with other

subsystems diminished the overall system synergy, impeded normal system operations, and further led to a reduction in the level of the WCC.

# 4.3. Results on the WCC of the Middle Yangtze River 

The middle Yangtze River is a long-distance reach consisting of many waterways, which differ in terms of their natural characteristics, navigational impediments, and external influences (e.g., ecological protection, flood control safety, water-related projects). According to the characteristics of each waterway and other factors, such as economic development, flood control, and ecological characteristics, in this study, the middle Yangtze River was divided into four sections, namely, a section from Yichang to Dabujie, a section from Dabujie to Chenglingji, a section from Chenglingji to Wuhan, and a section from Wuhan to Hukou.

A further selection in each section was needed considering the navigational characteristics and external influences of each section. For the Yichang-Dabujie section, the Lujia River was selected, as it is a shallow waterway with sands and pebbles. For the Dabujie-Chenglingji section, the Taipingkou waterway was selected due to the complexity of its evolution, navigational characteristics, and the existing external constraints caused by bridges. For the Chenglingji-Wuhan section, the Jiepai waterway was selected. For the Wuhan-Hukou section, the Xinjiu waterway was selected due to the severe siltation and the bad navigation conditions after the flood in 2020.

Since the selected typical waterways were all located at the key choke points of the corresponding sections, it can be reasonably assumed that if the waterway scale of the typical waterway is improved, the waterway scale of the corresponding section can also be comprehensively improved. The designed scale schemes for each typical waterway are shown in Table 6.

Table 6. Status quo scale and designed scales of each reach.


Similar to the application of the WCC evaluation model on the Jiepai waterway (which is shown in Section 4.2), the WCC of the entire middle Yangtze River was analyzed. The results are exhibited in Figure 8, and their corresponding evaluation grades are presented in Fig. A1 according to Figure 4. Typically, the results indicate the following findings. First, the middle Yangtze River had a Critical bearable level under both the status quo scale and designed scale 1. Furthermore, the carrying capacity grew as the waterway scale was upgraded from the status quo scale to designed scale 1. The main reason may have been that the economic subsystems of all waterways under the status quo scale were graded as Unbearable, indicating that the current waterway scale cannot satisfy the economic demand of the middle Yangtze River. However, the economic subsystem scores rose rapidly under designed scale 1, and all were subsequently raised to the grade of Critical bearable. In addition, with the improvement in the economic subsystem, the gap between the subsystems narrowed and the system tended to be in a benign synergy level, which also promoted the further improvement of the carrying capacity. Second, the carrying capacity scores of each waterway basically showed a negative trend as the waterway scale continued to rise. This was due to the significant decline in the flood control subsystem

caused by the numerous projects of waterway scale improvement and in the water supply subsystem caused by the higher demand for navigable flows, especially for the WuhanHukou section under the design 2 scale $(9.5 \times 200 \times 1050 \mathrm{~m})$. Its carrying capacity became Unbearable due to the pressure on the flood control and water supply subsystems. In addition, a slight decrease in the score of economic subsystem was also an important reason, which was caused by the slow update of the ship types and the poor management and organization of the waterway traffic. An exception was the Yichang-Dabujie section, where continued economic and ecological improvements led to an upgrade in the carrying capacity. The benefits and drawbacks of upgrading the waterway scale could also be identified by conducting similar analyses for other sections or waterways. As a result, the evaluation model proposed in this paper can not only be used to evaluate the carrying capacity of inland waterways but can also be used as a tool to provide certain insights and to help the development and maintenance of waterways in the future.
![img-7.jpeg](img-7.jpeg)

Figure 8. Spatiotemporal changes of the WCC from Yichang to Hukou reaches in the middle Yangtze River.

# 4.4. Sensitivity Analysis of Weights of Antecedent Attributes 

While building an FBRB that represents the logical relationship between the WCC and subsystems, it is assumed that the weight of the antecedent attributes is $\frac{1}{\text { number of antecedent attributes }}$ (one fifth in this study). Due to the limited knowledge of the relative importance of synergy to the other four antecedent attributes, it is difficult to determine the appropriate weights. To test the sensitivity of the WCC evaluation model to the weights of the antecedent attributes, an improved one-at-a-time (OAT) method was adopted [58]. Taking the middle Yangtze River as an instance, the weight of one antecedent attribute was changed up and down by $10 \%, 30 \%$, and $50 \%$, and the weights of the rest of the antecedent attributes were changed accordingly based on the original weights. After the recalculation, the rate of change of the WCC evaluation score is presented in Figure 9. It can be seen that basically the rate of change was symmetrically distributed centered on 0 . Its sensitivity to the evaluation results showed a growing trend with the increase in the change rate of weights. Additionally, the rate of change varied between the antecedent attributes, and the sensitivity of the evaluation results to changes in the weights of economic and flood control were higher but still within $7 \%$. Overall, within a $50 \%$ fluctuation in the weights of individual antecedent attributes, the change rate of the carrying capacity score was much lower than the change rate of the weights, indicating that the evaluation results were relatively stable in general and the weights of the antecedent attributes were fairly reasonable. Thus, it can be concluded that the evaluation model had good robustness and reliability.

![img-8.jpeg](img-8.jpeg)

Figure 9. Change rates of WCC scores in response to antecedent attribute weights at status quo waterway scales.

# 5. Discussion 

Based on Figure 8, we could determine the optimal development threshold for the middle Yangtze River under multi-benefit synergistic development. Although the Lujia River waterway was an exception, more instances can show a general conclusion that the most appropriate development threshold to support the sustainable development of a waterway was generally smaller than the maximum developable threshold [10,59], thereby demonstrating the feasibility of the methodology. It is also of concern that the size of the channel in the Chenglingji-Wuhan reach at the status quo scale is insufficient to meet its economic needs, while the flood control function is high, and this imbalanced system leads to a low level of synergies, which further exacerbated the discrepancy from design scale 1 (WCC gap of 0.02 without considering synergies and 0.07 after considering synergies). This observation revealed that the proposed method could effectively take into account the impact of the synergy on the WCC.

Echoing Figure 7, the predominant restricting element of WCC at the status quo scale was economic, as evidenced by the middle reaches of the Yangtze River being in an Unbearable economic grade. As the scale upgraded, however, flood control and water supply emerged as the principal limiting factors. This shift was reflected by the continual decrease in scoring for both subsystems with the waterway's increased scale, and the carrying capacity of flood control of many waterways at design scale 2 had even reduced to an Unbearable grade. This is supported by the fact that the hydrological and fluvial stabilities of the middle reaches of the Yangtze River is decreasing due to the successive operation of cascade projects and soil/water conservation [60,61]. More seriously, the reduced WCC score at design scale 2 indicates that excess capacity due to over-exploitation at the channel scale will be unable to balance the pressures from flood safety, water supply, and even river ecology. The above phenomenon demonstrates the idea that the constraints of the WCC in the middle Yangtze River varied with the waterway scale. This is similar to Wang, who classified the development of inland waterways into three stages, which are initial, developing, and developed, and showed that waterways at different stages have different characteristics.

Consequently, the main measure to increase the WCC is to improve the flood control and water supply capacity of the middle Yangtze River, including the improvement of

the operation strategy of the upstream reservoirs and the construction of flood control infrastructures. Meanwhile, a reasonable layout of the regulation project can not only minimize the damage to the flood control subsystem but also release the pressure on ecological restoration, which is essential for the sustainable development of the waterway.

# 6. Conclusions and Contributions 

In the global context of the scarcity of freshwater resources in rivers, the growing conflict over water rights highlights the importance of determining the optimal scale of waterway development from the perspective of multifunctional utilization and synergistic development [10]. In this study, a novel method is proposed for WCC evaluation based on four subsystems and 17 indicators. AHP is used to derive the relative weights of factors within each layer, which are combined with the fuzzy belief rule to logically model the relationships between indicators, subsystems, and WCC. In addition, a synergy parameter is incorporated into the FBRB to consider the effect of the synergy between the subsystems on the WCC. The Bayesian network technique is adopted to achieve a comprehensive evaluation. A utility function is applied to convert the linguistic evaluation grade the DoB into a carrying capacity score to rank and grade the WCC at different scales. Taking the middle Yangtze River from Yichang to Hukou as an example, the two main conclusions were as follows: (1) The middle Yangtze River still needs further development, with the optimal waterway scales for the four sections (i.e., the Yichang-Dabujie section, the Dabujie-Chenglingji section, the Chenglingji-Wuhan section, and the Wuhan-Hukou section) were $5.5 \times 200 \times 750 \mathrm{~m}, 4.5 \times 200 \times 750 \mathrm{~m}, 6 \times 200 \times 750 \mathrm{~m}$, and $7 \times 200 \times 750 \mathrm{~m}$, respectively. (2) Through analyzing the WCC of the middle Yangtze River at different scales, we discovered that the WCC constraints in the middle Yangtze River varied with the waterway scale. More specifically, at the status quo scale, the primary limiting factor for the WCC in the middle Yangtze River was economic and gradually changed to flood control and water supply as the channel scale increased.

The contributions of this work can be summarized from both theoretical and practical perspectives. As far as the theoretical contributions are concerned, first, an extensive survey was conducted to show the most comprehensive WCC factors possible. Second, this study emphasized the importance of synergy in WCC assessment. Since the claims of different stakeholders for a waterway may differ significantly, the synergistic development of waterway benefits will contribute to the rational allocation and efficient use of water resources to support the sustainable development of the waterway [62]. Finally, the combination of a fuzzy rule base with a belief structure and BNs provides a powerful tool to combine subjective judgment for assessing WCC under uncertainty, especially when waterway data are incomplete. In the method proposed in this paper, the expression of the WCC and its influences as linguistic variables with probability distributions allows for the use of a unified form to model different types of information, thus offering the possibility of a fusion of information from multiple sources. In addition, the use of a BN enables the modeling of non-linear relationships between nodes, which provides a tool for the fusion of synergies, and also facilitates the reasoning of the carrying capacity, which can update the WCC results in time when new inputs are available.

The results of this study also contribute to management practices in the field of inland waterways. The proposed method provides a standard, generic framework for WCC assessment. Although it was applied and demonstrated in the case study of the middle Yangtze River, it has the potential and flexibility for wider application in different waterways. However, it is worth noting that the FBRB developed in this study needed to be reconstructed accordingly to fit the scenario under investigation. In addition, different influencing factors, as well as evaluation grades, need to be selected according to the characteristics of other waterways and the specific requirements for carrying out WCC evaluations.

Even though as many indicators as possible were considered in this study for the comprehensive evaluation of the WCC, a more equitable consideration of the indicators is needed to balance the demands of the economy, flood control, water resource allocation,

ecological protection, and navigation. Furthermore, although the case of the middle Yangtze River is representative, the natural characteristics of waterways in different regions are different, and the indicators and their evaluation thresholds should be adjusted according to the details of different waterways. Another limitation of this study was that even though the Bayesian network technique can deal with non-linear relationships between indicators that are interdependent, this study ignored the complex relationships that may exist between subsystems due to the limitations of the available data. It is therefore suggested that the evaluation of WCC should be carried out from a more systematic perspective in future work.

Author Contributions: Conceptualization, Y.C., B.Z., X.P., H.Q., W.C. and W.Y.; Methodology, Y.C. and B.Z.; Software, B.Z.; Validation, X.P.; Investigation, H.Q., W.C. and W.Y.; Resources, H.Z.; Data curation, Y.C., H.Q., W.C. and W.Y.; Writing—original draft, Y.C. and B.Z.; Writing—review \& editing, Y.C. and X.P.; Visualization, B.Z.; Supervision, X.P.; Project administration, W.Y.; Funding acquisition, H.Z. and W.Y. All authors have read and agreed to the published version of the manuscript.

Funding: This research was supported by the Program of National Key Research and Development Plan [grant number 2016YFC0402103].

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflicts of interest.

# Appendix A 

Table A1. Data sources and definitions of assessment indicators.


Table A1. Cont.


# Appendix B 

Table A2. The conditional probability table of WCC.


Appendix C
![img-9.jpeg](img-9.jpeg)

Figure A1. WCC evaluation grades of the middle Yangtze River from Yichang to Hukou at different scales ((a) status quo scale; (b) designed scale 1; (c) designed scale 2).
