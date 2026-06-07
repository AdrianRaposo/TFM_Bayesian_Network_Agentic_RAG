# Article 

## An Integrated Model for Risk Assessment of Urban Road Collapse Based on China Accident Data

Zewei Zhang ${ }^{1,2, *}$, Qingjie Qi ${ }^{1,2}$, Ye Cheng ${ }^{1,2}$, Dawei Cui ${ }^{1,2}$ and Jinghu Yang ${ }^{1,2, *}$


#### Abstract

check for updates Citation: Zhang, Z.; Qi, Q.; Cheng, Y.; Cui, D.; Yang, J. An Integrated Model for Risk Assessment of Urban Road Collapse Based on China Accident Data. Sustainability 2024, 16, 2055. https://doi.org/10.3390/su16052055

Academic Editors: Isidoro Russo, Gianluca Genovese and Ciro Caliendo

Received: 25 January 2024
Revised: 28 February 2024
Accepted: 28 February 2024
Published: 1 March 2024


#### Abstract

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /)$.


[^0]
## 1. Introduction

As the urbanization process continues to accelerate, the number of road infrastructure construction projects has been increasing year by year in China. A large amount of underground space is being utilized for the development and construction of public facilities such as rail transit, various urban lifelines, and urban comprehensive utility tunnels [1]. However, with the increasing level of utilization of urban underground space, the impact of human activities on the subsurface geological environment has been increasingly intensified, and the ensuing urban safety problems represented by road collapse have been more prominent. Ground collapse refers to a phenomenon or process in which the surface rock and soil bodies are affected by natural factors or human engineering activities to fall downward and form subsidence pits (holes) on the ground and cause disasters [2]. Due to the sudden, hidden, and destructive characteristics of road collapse [3], it will not only lead to property loss and affect normal production and life but also cause panic among the masses. Thus, road collapse risk assessment is important for accident early warning and early emergency response, which is important for promoting the sustainability of societies.

The occurrence of urban road collapse is the result of a combination of human and natural factors [1-3]. The first step in implementing the risk assessment of road collapse is to identify risk factors. Existing studies related to collapse risk assessment mainly focus on geological and environmental indicators, such as lithology and soil type [4,5],


[^0]:    1 Research Institute of Emergency Science, Chinese Institute of Coal Science (CICS), Beijing 100013, China
    2 China Coal Technology \& Engineering Group (CCTEG), Beijing 100013, China

    * Correspondence: zhangzew16@tsinghua.org.cn (Z.Z.); yjh_cumtb@126.com (J.Y.); Tel./Fax: +86-010-84264759 (Z.Z. \& J.Y.)


    Abstract: With the deepening development and utilization of urban underground space, the risk of urban road collapse is becoming increasingly prominent, which is a serious threat to the safety of life and property. Therefore, the risk assessment of urban road collapse has vital significance for the safety management of cities. The main idea is to predict ongoing accidents by analyzing historical accident cases in depth. This paper explores the combination of Interpretative Structural Modeling (ISM) and Bayesian Networks (BNs) to construct a risk assessment model of road collapse. First, the main risk factors of road collapse and their coupling relationships are identified, which is used to increase the low reliability of complex systems. Then, the risk factors of road collapse are logically divided by ISM to obtain the BN hierarchy. Finally, the BN node probabilities are evaluated by the Expectation-Maximization (EM) algorithm using the collected 92 real road collapse accident cases. The model can be used to quantify the coupling strength and influence degree of each risk factor on the occurrence of road collapse accidents, which in turn can predict the probability of road collapse accidents in a given scenario. This study can provide a theoretical basis for urban safety management and reduce the risk of road collapse and potential loss of life and property, which is important for the sustainable development of societies.

    Keywords: EM algorithm; Bayesian Network; interpretative structural modeling; risk assessment; urban road collapse

changes in river and groundwater levels [6], quantity of rainfall [7], fault zones [8], etc. Related studies on the influence of human factors on road collapse have mainly focused on vehicle loads [9,10], underground construction [11], etc., and have insufficient attention to management factors. Moreover, research on risk assessment of urban road collapse has a high degree of concentration on risk factor selection, focusing mainly on a few specific risk factors [12] and paying insufficient attention to the coupling effect among multiple risk factors, such as evaluating the probability of occurrence about urban road collapse based on pipeline ruptures [13-15], soil type [16] and rainfall [17], underground structures [18], etc. This type of approach analyzes in depth the influence mechanism of specific risk factors on road collapse accidents, but the coupling mechanism of multiple risk factors is not sufficiently explored. As a result, there is an urgent need to further improve the accuracy of the risk assessment model for road collapse based on the collection and analysis of accident case data and intensively study the comprehensive impact of multiple risk factors on urban road collapse accidents.

This paper aims to construct a risk assessment model for urban road collapse. Traditional risk assessment models have been widely used in collapse risk assessment. Existing research mainly incorporates risk factors represented by soil type and pipeline ruptures into road collapse risk assessment models and classifies and grades road collapse losses. Then, road collapse losses are categorized and rated, and semi-quantitative ground collapse risk assessment is realized through consequence prediction grading. The existing road collapse risk assessment model based on fuzzy comprehensive evaluation assumes that each risk factor is relatively independent, and insufficient consideration is given to the coupling relationship between each factor [7,19-25]. The accuracy of road collapse risk assessment models based on the analytic hierarchy process [1,26-31] and weighted arithmetic mean method [12,32-36] heavily depends on the level of expert knowledge with high subjectivity. Consequently, the validation of the assessment results based on accident cases is difficult to realize, and it is still necessary to build a quantitative risk assessment model for urban road collapse accidents based on the coupling relationship between road collapse risk factors. Machine learning models have been widely used in disaster risk assessment [37,38], and models such as Convolutional Neural Networks (CNNs) [39,40], Artificial Neural Networks (ANNs) [41,42], and Support Vector Machines (SVMs) [43,44] are beginning to be used in risk assessment for natural disasters with large amounts of monitoring data, such as earthquakes and floods. However, the process of modeling quantitative risk assessment for urban road collapse accidents is not yet directly applicable to the process of modeling natural hazard risk due to its characteristics of multiple risk factors and difficulty in capturing accident data.

This paper proposes a risk assessment model combining ISM and BN models to predict the probability of urban road collapse accidents. Risk factors are defined by limited case analysis and literature research. The selected risk factors of road collapse are not necessarily causally related to each other, and there is a more complex coupling relationship. Therefore, traditional causal inference methods are not applicable to constructing hierarchical structures among risk factors. The risk assessment model proposed in this paper integrates the coupling effect of each risk factor on road collapse accidents and can also predict the change in accident probability by changing the state of a single risk factor. In this paper, ISM is selected to sort out the hierarchical structure among risk factors of road collapse, learn parameters by BN, and determine the accident case data structure. The influence intensity of each factor on road collapse is quantitatively evaluated by how the probability of road collapse changes with the state of the risk factor by selecting the risk factors with the greatest influence on road collapse accidents for different scenarios, providing decisionmaking support for risk prevention and control departments. The ability of the constructed model to predict the probability of urban road collapse is verified with the real accident case. This study provides new ideas for identifying the risk factors of urban road collapse, predicting the probability of collapse, and improving urban safety management.

# 2. Methodology 

In this paper, the risk assessment model of road collapse was constructed using the ISM and BN models. Urban road collapse accidents are the result of the combined effect of multiple risk factors. Therefore, the risk factors were identified, and their coupling relationship was sorted out to reveal the combined effects of each risk factor on road collapse, which can be used to assess and predict the collapse risk. In this paper, we established a risk assessment model for road collapse accidents by deducing the influence mechanism of each risk factor on road collapse accidents and verifying the feasibility of the model through real cases. The framework of methodology used in this paper is shown in Figure 1, which includes three phases.
![img-0.jpeg](img-0.jpeg)

Figure 1. Framework of methodology in this paper.
Phase 1: determination of risk factors. The risk factors that cause road collapse are preliminarily identified through research and combing of literature. Selected 10 experts are invited to evaluate the relationships between the identified risk factors, and the consistency of the summarized experts' opinions is tabulated.

Phase 2: construction of risk assessment models. Determining the relationship between the various risk factors on road collapse through ISM, the hierarchical division between the risk factors is determined. The BN structural framework is constructed based on the hierarchy of risk factors. Based on the EM algorithm, Bayesian parameters are learned from collected case data of road collapse accidents to establish the risk assessment model.

Phase 3: model application in risk assessment and decision support. The mechanism of each risk factor's role in road collapse accidents and its degree of influence are sorted out by analyzing the influence change of single factor state on collapse probability. A real road collapse accident scenario is selected to verify the application of the proposed risk assessment model in risk assessment and decision support.

### 2.1. Interpretative Structural Modeling

Interpretive Structural Modeling (ISM) is a model method used to analyze the hierarchical structure of complex systems [45]. This method makes it possible to construct a hierarchical structural model of the elements in the system and visualize the overall structural relationships. It is often used to stratify the factors affecting the target variable. The exact process of the method is as follows.

1. The adjacency matrix

The coupled logic diagram of the risk factors reflects the interactions between the factors. According to the logical relationship diagram of each risk factor of road collapse accidents, an adjacency matrix $M$ with $n$ rows and $n$ columns can be constructed. $n$ is the number of risk factors for road collapse accidents, and the values of the elements within the matrix are shown in Equation (1). If the factor $F_{i}$ has an effect on $F_{j}$, the value of $m_{i j}$ is 1 . Conversely, if the factor $F_{i}$ has no effect on $F_{j}$, the value of $m_{i j}$ takes 0 .

$$
m_{i j}=\left\{\begin{array}{c}
1:\left(\text { when } F_{i} \text { has an direct effect on } F_{j}\right) \\
0:\left(\text { when } F_{i} \text { has no effect on } F_{j}\right)
\end{array}\right.
$$

# 2. The reachability matrix 

$R$ is the reachability matrix of the adjacency matrix $M .(M+I)$ is the sum of the adjacency matrix $A$ and the unit matrix $I$. Then, the exponentiation of the matrix $(M+I)$ for the integer $n$ is calculated using Equation (2).

$$
R=(M+I)^{n+1}=(M+I)^{n} \neq \ldots(M+I)^{2} \neq(M+I)
$$

The above exponentiation is obtained based on the Boolean algebra algorithm [45], and the matrix $R$ is a reachable matrix. If the element $r_{i j}$ is 1 , it denotes the risk factor $F_{i}$ can reach the factor $F_{j}$. If the element $r_{i j}$ is 0 , it denotes the risk factor $F_{j}$ is not reachable by the factor $F_{i}$.
3. The reachable set and the antecedent set

The reachable and current sets are obtained based on decomposing the reachable matrix. The reachable set $S\left(F_{i}\right)$ is the set sum of other factors that can be triggered by a risk factor through a certain path. The antecedent set $A\left(F_{i}\right)$ is the set sum of factors that this risk factor can reach. Intersection of reachable sets and antecedent sets $L\left(F_{i}\right)=R\left(F_{i}\right) \cap A\left(F_{i}\right)$.
4. The hierarchical decomposition of the reachable matrix

Elements in a coupled system are usually disordered. Therefore, it is possible to sort out the logical relationship between risk factors by decomposing the reachability matrix. Moreover, it contributes to enhance the understanding of the coupled influence mechanism between risk factors, and further distinguish between direct and indirect influences between factors. The influencing factors can be extracted layer-by-layer by solving the reachable set $S\left(F_{i}\right)$, the antecedent set $A\left(F_{i}\right)$, and the intersection set $L\left(F_{i}\right)$ for each risk factor. The hierarchy of the urban road collapse system can be divided according to the extraction order.
5. The hierarchical diagram of the risk factors

After the hierarchical decomposition, the hierarchical structure diagram is constructed based on the hierarchical results and the relationship between the risk factors.

### 2.2. Bayesian Network

Bayesian networks are based on Bayesian decision theory [46]. Combined with graph theory methods, the risk factors are expressed through nodes and the logical relationships between risk factors are expressed through directed connections between nodes and conditional probabilities between nodes. It is suitable for analyzing risk warning problems with complex development and evolution processes.

The Bayes' theorem is the basis of Bayesian decision theory [47]. Bayes' theorem is simplified as follows based on the decision problem, $E=\left\{E_{1}, E_{2}, E_{i} \ldots, E_{n}\right\}$, which is the set of possible events. $P\left(E_{i}\right)$ is the probability of occurrence of event $E_{i}$, which is often referred to as the a priori probability, $E_{i} \cap E_{j}=\varnothing, \quad i \neq j, i, j=1,2, \ldots, n . P(I)$ is the probability of occurrence of event $I$, which occurs only if partial event $E_{i}$ occurs. When event $I$ occurs only in the presence of a partial event $E_{i}, P\left(I / E_{i}\right)$ is the occurrence

probability of event $I$ with given occurrence probability of event $E_{i}$. Thus, given that event $I$ has occurred, the conditional probability of event $E_{r}$ is

$$
P\left(E_{r} / I\right)=\frac{P\left(E_{r}\right) P\left(I / E_{r}\right)}{P(I)}=\frac{P\left(E_{r}\right) P\left(I / E_{r}\right)}{\sum_{j=1}^{n}\left(E_{j}\right) P\left(I / E_{j}\right)}
$$

Bayes' theorem is the theoretical basis of BN, which combines a priori cognition with actual observations, and uses new observations to continuously update our knowledge of the unknown parameters to obtain a new posteriori cognition. In this paper, the nodes in BN represent the variables (road collapse risk factors), the arcs represent the influence relationships between the nodes, and CPT (Conditional Probability Table) is used to quantify the strength of complex dependencies between random variables.

# 2.3. Expectation-Maximization Algorithm 

The EM algorithm was first proposed in 1977 by Dempster et al. [48]. The idea is to group the data used for parameter estimation, estimate the parameters separately within each group, and regroup the data according to the new estimated parameters. The alternate iterations for data decomposition and parameter estimation are used to improve the quality of parameter estimation. The grouping results will eventually converge with the parameter likelihood increases. The algorithm is used to solve the estimation problem when the system parameters are missing. Now, it can be used to solve the problem of parameter estimation under a small amount of data through continuous improvement. The specific steps are as follows:

Inputs: observed variable data $Y$, latent variable data $Z$, joint distribution $P(Y, Z \mid \theta)$, and conditional distribution $P\left(Z \mid Y, \theta^{(i)}\right)$;

Output: model parameters $\theta$.
(1) Parameters are initialized and iteration starts.
(2) Solve the expectation: $\theta^{i}$ is the estimated value of $\theta$ at iteration step $i$. The expectation $Q\left(\theta, \theta^{i}\right)$ is calculated as follows:

$$
Q\left(\theta, \theta^{i}\right)=E_{Z}\left[\log P(Y, Z \mid \theta)\left|Y,\left|\theta^{(i)}\right|=\sum_{Z} \log P(Y, Z \mid \theta) P\left(Z \mid Y, \theta^{(i)}\right)\right.\right.
$$

(3) Expectation maximization: $\theta$ is obtained by maximizing $Q\left(\theta, \theta^{i}\right)$. The value $\theta^{i+1}$ of the next iteration at step $(i+1)$ is calculated from Equation (5).

$$
\theta^{(i+1)}=\arg \max _{\theta} Q\left(\theta, \theta^{i}\right)
$$

(4) Repeat the expectation-solving step and the expectation-maximization step until convergence.

### 2.4. Construction of Risk Assessment Model

2.4.1. Identification of Risk Factors

Based on the safety system engineering theory, the risk factors of road collapse accidents are sorted out from four aspects: human, physical, environmental, and management factors. Through the comparative analysis of related literature, it can be summarized that there are certain similarities in the causes of urban road collapse accidents through the comparative analysis of the related literature [1-3]. The reports of major urban road collapse accidents in recent years are selected for a depth analysis, which is shown in Table 1; the risk factors are shown in Table 2.

Based on the analysis of 92 cases of urban road collapse accidents, this study focuses on analyzing the mechanism of human and management factors in ground collapse accidents. Although the environmental factors and physical factors are important risk factors, their


influence mechanism on the road collapse accident is only used as a reference in this model. Because they have been taken into account in the initial stage of the design of the road and underground space, the natural environment risk factor is difficult to avoid. The 92 cases of road collapse accident data analyzed in this paper are mainly from the accident investigation report, which has a more adequate analysis and elaboration of human factors and management factors as the more common risk factors for road collapse accidents, human and management risks are easier to avoid than objective factors such as the environment. Moreover, human and management factor-related interventions can play an important role in preventing road collapse accidents [3].

Table 2. Risk factors of urban road collapse in this paper.


# 2.4.2. Hierarchical Structure of Road Collapse 

The construction of a Bayesian Network for urban road collapse accidents requires determining the structure of the network among risk factors and its parameters. This section analyzes the coupling relationship between risk factors for road collapse accidents and identifies their hierarchical structure. The interactions between risk factors of road collapse were evaluated by selected experts, whose opinions were obtained through questionnaires. First, 5 relevant experts were invited to complete the first round of the questionnaire, which consisted of 9 similar structured questions. The question format is: Please select the risk factor(s) that have an impact on XX factor(s). The options included the 8 factors in Table 2

in addition to the factor in question, and the response format was multiple choice. If all 5 experts agreed that there was an influential relationship between the two factors, the influence between two risk factors was defined. If at least 1 expert considered that there was no influence between the two factors, the question was left for the second round of the questionnaire. Three additional experts were invited to the second round of questionnaires, but the questionnaires only addressed impact relationships that were not specified in the previous round. Influence relationships that were all confirmed by the interviewed experts in the second-round questionnaires were added to the coupling relationships, and other influence relationships were not established. The establishment of the coupling relationship between the factors helps to further optimize the initial risk factor structure, which can be used as the basis for eliminating the independent factors, merging the overlapping factors, and finally obtaining the coupling relationship between the risk factors of the urban road collapse accident.

The resulting coupling relationships between risk factors need to be hierarchically structured before they can be mapped into a Bayesian Network structure. The ISM was used to classify the risk factors into multiple levels. The adjacency matrix was extracted from the coupling relations, as shown in Table 3, which is the initial input matrix of the ISM. The reachable matrix is shown in Table 4. It can be obtained through the matrix calculation, which indicates there is a certain influence path between two factors.

Table 3. The elements in adjacency matrix.


Table 4. The elements in reachable matrix.


The reachable set $S$ and the antecedent set $A$ are separated from the reachable matrix and set $L$ is their intersection. Their specifics are shown in Table 5. The risk factor decomposition can be realized by using the intersection $L$, as shown in Table 6. The 9 risk factors were organized into 4 levels. $\mathrm{F}_{3}$ (Soil displacement) and $\mathrm{F}_{4}$ (Instability of underground structures) were on the first level. $\mathrm{F}_{1}$ (Human error), $\mathrm{F}_{7}$ (Vehicle load), and $\mathrm{F}_{8}$ (Pipeline leakage) were on the second level. $\mathrm{F}_{2}$ (Defects in safety technical measures) and $\mathrm{F}_{6}$ (River damage) were on the third level. $\mathrm{F}_{5}$ (Heavy rainfall) and $\mathrm{F}_{9}$ (Inadequate safety checks) were on the fourth level.

At this point, the initial hierarchical relationship graph between road collapse risk factors was further optimized to obtain a hierarchical network. Two other experts were

invited to verify the initial hierarchical relationships of the road collapse risk factors, which mainly consisted of eliminating redundant relationships between the risk factors and checking their compatibility with the BN structure. The invited experts considered the initial hierarchical relationships to be compatible with the BN structure and identified some of the redundant influence relationships that could be eliminated. Figure 2 illustrates the optimized influence relationships between risk factors, with the dashed line showing the deleted redundant relationships. For example, the effect of $\mathrm{F}_{9}$ (Inadequate safety checks) on $\mathrm{F}_{4}$ (Instability of underground structure), $\mathrm{F}_{9}$ mainly affects $\mathrm{F}_{4}$ by influencing $\mathrm{F}_{8}$ (Vehicle load) and $\mathrm{F}_{7}$ (Pipeline leakage), so the direct influence between $\mathrm{F}_{9}$ and $\mathrm{F}_{4}$ can be deleted as a redundant relationship. Similarly, the influence relationship between $\mathrm{F}_{2}$ (Defects in safety technical measures) and $\mathrm{F}_{3}$ (Soil displacement) was also deleted. Then, the optimized hierarchical network was mapped onto the BN structure, as shown in Figure 3.

Table 5. Reachable and antecedent sets and their intersection.


Table 6. Hierarchical division of risk factors.


![img-1.jpeg](img-1.jpeg)

Figure 2. Optimized influence relationships of risk factors.

![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian Network (BN) structure of urban road collapse.

# 2.4.3. Construction of BN Model 

The coupling strength between risk factors was quantified through the BN model to determine the main path of road collapse accidents. Then, the top node "Collapse" was added to the optimized hierarchical network. The risk factor hierarchical network was mapped to the BN structure through GeNIe 4.1, as shown in Figure 3. The status of each node was defined before parameter learning and the value of each factor was divided. The status of the risk factors in this paper was set to "yes/no", depending on the actual status. For example, for the node $\mathrm{F}_{1}$ (Human error), human error was set as "yes" or "no" based on whether it occurred or not.
a. BN structure

The implementation of the inference function about the BN structure needed to be combined with corresponding probability parameters. The prior probability needed to be determined for the edge node in the BN structure, and CPT needed to be determined for the non-edge node. The parameter values of all nodes were determined by the EM algorithm, except the "Collapse" node. The parameter values of the "Collapse" node were determined by expert assignment. The determination process of the CPT of the "Collapse" node is shown in Table 7.

Table 7. The CPT (Conditional Probability Table) of the top node "collapse".


b. Parameter learning

Data learning was used to calculate the parameters of other nodes with the EM algorithm. There are three steps in this process, including case data collection, data standardization, and EM algorithm learning.

Step 1 case data collection This paper collects data related to urban road collapse accidents through official websites of emergency management departments, WeChat official accounts, and official news. A complete accident investigation report is required for the collected road collapse cases. The case study presented in this paper is primarily based on the investigation report of road collapse accidents. A total of 93 typical road collapse accidents and their corresponding accident investigation reports are collected as required. Then, 92 of these accidents were used as input datasets in the parameter learning of the EM algorithm; 1 additional accident was used as a test case for the collapse risk assessment model.

Step 2 data standardization Case data from road collapse accident investigation reports need to be standardized before they can be used as a collection of learning data inputs to the EM algorithm. Until then, a data standardization criterion needs to be established for road collapse investigation reports. This criterion is mainly reflected in setting the nodes in the BN structure to the corresponding status values. The standardization of node $\mathrm{F}_{1}$ (Human error) is taken as an example, as shown in Table 8. When an expression similar to "illegal construction", "unprofessional operation", "dangerous operation", etc. appears in the report, the status of $\mathrm{F}_{1}$ is defined as "yes" at this point; otherwise, it is "no". Then, the standardized dataset can be built to input into GeNIe 4.1 by the space part of the standardized dataset, as shown in Table 9 .

Table 8. Standardization example of accident data ( $\mathrm{F}_{1}$ Human error).


Table 9. The normalized dataset in the GeNIe 4.1 (partial dataset as example).


Step 3 Parameter learning based on EM algorithm
Finally, the standardized dataset was imported into the BN model for road collapse accidents using GeNIe 4.1. The probability of each node in the BN structure was calculated

using the EM algorithm. The probability of urban road collapse can be predicted after parameterizing the BN, which is presented in the next section.

# 3. Results and Discussion 

### 3.1. Action Mechanism of Risk Factors

In the hierarchical network, $\mathrm{F}_{5}$ (Heavy rainfall) and $\mathrm{F}_{9}$ (Inadequate safety checks) comprised the underlying risk factors. They only had a one-way impact on other risk factors but were not affected by other risk factors. These risk factors are defined as basic risk factors or potential risk factors. The impact of these risk factors on road collapse accidents is indirect and important, although it may not seem obvious. In contrast to this, $\mathrm{F}_{3}$ (Soil displacement) and $\mathrm{F}_{4}$ (Instability of underground structures) were the top factors in the hierarchical network. They were only influenced by other risk factors in one direction but did not affect other risk factors. These risk factors are defined as direct factors, which are the more direct causes of road collapse accidents. Moreover, the other risk factors are defined as independent risk factors, such as $\mathrm{F}_{1}$ (Human error), $\mathrm{F}_{2}$ (Defects in safety technical measures), $\mathrm{F}_{6}$ (River damage), $\mathrm{F}_{7}$ (Vehicle load), and $\mathrm{F}_{8}$ (Pipeline leakage). These risk factors serve as a connecting link between the preceding and the following in the hierarchical network. They may not only be influenced by other factors but also have an impact on them. The accident investigation report focuses more on identifying indirect risk factors that cause road collapse. In this risk assessment model, the basic risk factors play a role in the development of accidents by influencing other factors. The indirect risk factors play a role by influencing the direct factors, which often directly lead to road collapse.

### 3.2. Influence Intensity of Individual Risk Factor

It is possible to gain a deeper understanding of the role of each factor in road collapse accidents by analyzing the mechanism of different risk factors. For the safety management of the relevant sectors, the impact of risk factors should be eliminated as far as possible by taking into account the overall relevant safety. Managers should not only focus on the prevention and resolution of direct risk factors but also take effective measures to avoid the impact of indirect and potential factors.

Risk assessment models for road collapse accidents focus on decision support for safety managers. The status of each node (risk factors) within the model is changed by the effective application of some security management measures. For example, the node status of $\mathrm{F}_{9}$ (Inadequate safety checks) can be changed from a "yes" status to a "no" status through rational planning of inspection cycles and effective implementation of daily inspections. The effectiveness of the measures taken to prevent the occurrence of accidents is reflected in how the state of the nodes can be changed to avoid the occurrence of road collapse accidents. It can be assessed by the extent to which a single factor influences a road collapse accident. Therefore, it is significant for decision support by analyzing the influence intensity of a single risk factor on road collapse accidents. During the calculation process, when the status or probability distribution of a node changes, it can be simply evaluated by the change in probability of the top nodes, each of which is ranked by the strength of its influence. For example, when the status of node $\mathrm{F}_{4}$ (Instability of underground structures) changed from "Yes" to "No", the probability of road collapse decreased from $67 \%$ to $23 \%$, a decrease of $44 \%$, which indicates that maintaining the stability of underground structures plays a key role in reducing the risk of road collapse. This paper does not consider the normalization of different risk factors and focuses mainly on reducing the risk of urban road collapse accidents by changing the status of risk factor combinations. The influence intensity of each risk factor on road collapse accidents is shown in Table 10.

The influence intensity of each risk factor can be obtained by comparing the differences in probability changes. The order of influence intensity from highest to lowest was: $\mathrm{F}_{4}$ (Instability of underground structures) $>\mathrm{F}_{3}$ (Soil displacement) $>\mathrm{F}_{1}$ (Human error) $>\mathrm{F}_{9}$ (Inadequate safety checks) $>\mathrm{F}_{6}$ (River damage) $>\mathrm{F}_{5}$ (Heavy rainfall) $>\mathrm{F}_{8}$ (Pipeline leakage) $>\mathrm{F}_{2}$ (Defects in safety technical measures) $>\mathrm{F}_{7}$ (Vehicle load). It can be seen that "Instability

of underground structures" and "Soil displacement" had a greater impact on urban road collapse, accounting for about $40 \%$ of the total. "Defects in safety technical measures" and "Vehicle load" had a relatively small impact among the many risk factors. It is possible to plan a combination of decisions to reduce the overall risk by evaluating the effectiveness of each risk factor in reducing the risk of road collapse, especially if the sector concerned has limited risk control investment.

Table 10. The influence of risk factors on collapse probability.


# 3.3. Case Study 

### 3.3.1. Case Introduction

Risk prediction mainly refers to the estimation of the probability and impact of accidents through various scientific and technical means based on available data and known information. This paper is concerned with the probability prediction of urban road collapse accidents. The core idea is to set the relevant node status based on the known risk factor information and estimate the status situation of other nodes through BN inference. The risk prediction process in this section is based on a real case of an urban road collapse accident, which was not added as a learning case to the input dataset.

The real collapse accident case for validation of the risk assessment model was the "20220818" urban road collapse accident in Longhua Street, Shenzhen City, Guangdong Province. The case scenario was set up as follows. City A has a sewer pipeline leakage that needs rehabilitation operations. The contractor for the rehabilitation operations is B, the contracting company is C, and the supervisory company for the project is D. After winning the bid, Company C subcontracted the labor for the pipeline rehabilitation to Company E. The following conditions are known: (1) the specific construction personnel in Company E did not provide the foundation pit support during excavation; (2) the relevant technicians in Company C were not present to perform their duties during construction, and had neglectful management and oversight in the operation process; (3) Company D did not fulfill its supervisory duties; (4) the construction purpose was pipeline rehabilitation to the sewage pipe; and (5) displacement of unsupported soil in the pit.

# 3.3.2. Risk Prediction of Road Collapse 

Based on the scenario setup above, the status of the five nodes with known information can be determined, as shown in Figure 4. For example, the status of node $\mathrm{F}_{9}$ (Inadequate safety checks) was set to "Yes", and the status of node $\mathrm{F}_{5}$ (Heavy rainfall) was set to "No". Therefore, the probability of a road collapse accident in this case was $98 \%$ through BN deduction. In this paper, the risk of road collapse accidents was categorized into three levels based on the probability: below $33 \%$ as low risk, $33-67 \%$ as medium risk, and more than $67 \%$ as high risk. It can be seen that the probability of road collapse accidents in the simulation scenario was very high, and timely measures must be taken to avoid them. In the real accident case, the road collapse was precisely due to the construction workers not providing support in the excavation pit, and the collapse accident caused the death of the excavation operation workers. The prediction results are in good agreement with the actual results of the accident.
![img-3.jpeg](img-3.jpeg)

Figure 4. Collapse risk prediction in case scenario.
The prevention and control of road collapse accidents are mainly aimed at human factors and management factors. The states of risk factors $\mathrm{F}_{1}$ (Human error), $\mathrm{F}_{2}$ (Defects in safety technical measures), $\mathrm{F}_{8}$ (Pipeline leakage), and $\mathrm{F}_{9}$ (Inadequate safety checks) in this case were changed to predict the road collapse result. When the state of $\mathrm{F}_{1}$ changed from "yes" to "no" and the states of other risk factors remained unchanged, the model predicted a $57 \%$ probability of road collapse accidents. When the state of $\mathrm{F}_{2}$ changed from "yes" to "no", the model predicted a $29 \%$ probability of road collapse accidents. When the state of $\mathrm{F}_{8}$ changes from "yes" to "no", the model predicts a $61 \%$ probability of road collapse accidents. When the state of $\mathrm{F}_{9}$ changed from "yes" to "no", the model predicted a $35 \%$ probability of road collapse accidents. It can be seen that $\mathrm{F}_{2}$ (Defects in safety technical measures) and $\mathrm{F}_{9}$ (Inadequate safety checks) were the two controllable risk factors that had the greatest impact on road collapse accidents in this case. This is consistent with the statement in the

official accident investigation report that it "did not provide the foundation pit support during excavation" and "did not fulfill its supervisory duties". The feasibility of the risk assessment model is verified by the collapse risk prediction of the real case.

# 4. Conclusions 

In this paper, a risk assessment model for urban road collapse is constructed by combining ISM and BN. These include several key steps, risk factor identification of road collapse, coupling relationship analysis among risk factors, risk assessment of road collapse, and BN inference for supporting safety decisions. The main conclusions are as follows.

1. Based on risk factor identification and coupling relationship analysis, this research deepens our understanding of risk management for urban road collapse accidents. In response to some of the problems that exist in the qualitative study of road collapse accidents, this paper detects, through a limited number of case studies, that management factors and human factors are important causes of road collapse accidents in China. Thus, safety systems engineering theory (people, machines, environment, and management) is selected as the framework for risk factor composition. The process of determining the risk factors for road collapse accidents paid more attention to human and management factors from a safety management perspective (two human factors and three management factors are included in the nine risk factors).
2. The risk assessment model for urban road collapse is constructed based on BN, and the road collapse probability is quantitatively analyzed through real accident cases. The hierarchical network structure of road collapse incidents is mapped to BN using GeNIe 4.1. Ninety-two cases of Chinese urban road collapse accidents are collected from various online sources, and their accident reports are compiled into an accident dataset. After normalizing and organizing the accident data, the EM algorithm is used to determine the parameters of each node of the accident. The model can be used to quantify the influence intensity of each risk factor on road collapse accidents and to predict the probability of urban road collapse. Risk prediction results based on datasets constructed from real accidents can provide valuable references for safety decision-making in relevant departments.
3. The proposed risk assessment model for road collapse can be used to support safety management decisions in relevant departments. Scenario deduction based on real accident scenarios verifies the reasonableness of the established risk assessment models for road collapse. Substituting the accident scenarios into the established risk assessment model, the deduced occurrence probability of road collapse is high and consistent with real accident cases. Furthermore, the deduction process of the risk assessment model can intuitively obtain the probability change of each node, which helps the relevant departments to make corresponding safety decisions more efficiently and accurately.
This study can provide a theoretical basis for the prevention and emergency response of urban road collapse accidents. The effectiveness of each risk factor in reducing the risk of road collapse has been assessed by analyzing the action mechanism and influence intensity of each risk factor on collapse accidents. It can support the relevant departments in making targeted safety decisions, especially when their capacity is limited. In addition, the model has certain reference significance for risk prediction of urban road collapse accidents, which contributes to the further improvement of the predictability and accuracy of risk assessment for road collapse accidents.

In the face of the severe situation of frequent urban road collapse accidents, this study can help the relevant departments to optimize resource allocation in the case of limited capacity and avoid the greater risk of road collapse accidents at a lower cost. Risk prediction models can be used to assess the probability of urban road collapse under specific scenarios, provide early warning of collapse accidents, and suggest targeted safety decisions. It is also hoped that the results of this research will contribute to urban safety management in China.

In addition, due to the limitations of this study, the risk assessment model of urban road collapse in this paper is only a preliminary model that needs to be improved in the future. First, the data source of urban road collapse accident cases is relatively single, and the learning results of model parameters will be limited by the number of accident cases. In the future, further case data about urban road collapse accidents can be accumulated over time, and the case dataset can be continuously enriched. In addition, analyzed cases validated with relevant scenarios can be added to the value dataset to further improve the proposed risk assessment model. The continuous enhancement of the case dataset will lead to better learning, which can further improve the accuracy of the model. Meanwhile, with the increasing and standardized data on real road collapse accidents, an attempt can be made to construct a database of urban road collapse accidents in China. The continuous enrichment and improvement of the database will lay the research foundation for risk management of urban road collapse accidents. In addition, with the continuous accumulation of case data, the individual states of road collapse risk factors can be further refined, which will have a positive effect on improving the accuracy of risk prediction with the proposed model.

Author Contributions: Conceptualization, Z.Z.; methodology, Z.Z. and J.Y.; supervision, Q.Q. and J.Y.; visualization, Z.Z. and Y.C.; writing-original draft, Z.Z.; writing-review and editing, D.C. and J.Y.; funding acquisition, Q.Q. and J.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the Innovation and Entrepreneurship Science and Technology Project of China Coal Technology and Engineering Group (No. 2022-2-MS003) and the Innovation and Entrepreneurship Science and Technology Project of Chinese Institute of Coal Science (No. 2021-JSYF-006).

Data Availability Statement: Data are contained within the article.
Conflicts of Interest: All Authors are employed by the company China Coal Technology \& Engineering Group (CCTEG), The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.
