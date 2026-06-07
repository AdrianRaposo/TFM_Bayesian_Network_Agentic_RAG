# Article 

## A Novel Risk Assessment for Cable Fires Based on a Hybrid Cloud-Model-Enabled Dynamic Bayesian Network Method

Shenyuan Gao ${ }^{1,2,3}$, Guozhong Huang ${ }^{1}$, Zhijin Xiang ${ }^{1}$, Yan Yang ${ }^{1}$ and Xuehong Gao ${ }^{1, * *}$


#### Abstract

check for updates Citation: Gao, S.; Huang, G.; Xiang, Z.; Yang, Y.; Gao, X. A Novel Risk Assessment for Cable Fires Based on a Hybrid Cloud-Model-Enabled Dynamic Bayesian Network Method. Appl. Sci. 2023, 13, 10384. https:// doi.org/10.3390/app131810384

Academic Editors: Zhao Zhang, Dengpan Xiao and Kai Liu

Received: 17 August 2023
Revised: 9 September 2023
Accepted: 12 September 2023
Published: 17 September 2023


## (0) 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Research Institute of Macro-Safety Science, University of Science and Technology Beijing, Beijing 100083, China; shenyuan_gao@163.com (S.G.); hjxhuanggz@ustb.edu.cn (G.H.); g20208097@xs.ustb.edu.cn (Z.X.); yangyan@ustb.edu.cn (Y.Y.)
2 China National Institute of Standardization, Beijing 100088, China
3 Key Laboratory of Product Defect and Safety for State Market Regulation, Beijing 100088, China

* Correspondence: gaoxh2020@ustb.edu.cn


#### Abstract

The fire risk of cables constantly changes over time and is affected by the materials and working conditions of cables. To address its internal timing property, it is essential to use a dynamic analysis method to assess cable fire risk. Meanwhile, data uncertainty resulting in the deviation of risk values must also be considered in the risk assessment. In this regard, this study proposes a hybrid cloud model (CM)-enabled Dynamic Bayesian network (DBN) method to estimate the cable fire risk under uncertainty. In particular, the CM is initially applied to determine the membership degrees of the assessment data relative to different states of the root nodes; then, these degrees are considered the prior probabilities of DBN, where the dynamic risk profiles are reasoned. Subsequently, the Birnbaum and Fussell-Vesely importance measures are constructed to identify the key nodes for risk prevention and control, respectively. Moreover, a case study of the Chongqing Tobacco Logistics Distribution Center is conducted, the computational results of which indicate the proposed method's decision-making effectiveness. Finally, a comparison of the reasoning results between the proposed and traditional methods is performed, presenting strong evidence that demonstrates the reliability of the proposed method.


Keywords: cable fires; dynamic Bayesian network; cloud model; dynamic risk assessment

## 1. Introduction

Wires and cables play a pivotal role as crucial conduits for both power and information transmission. In contemporary society, cables find widespread application across diverse industrial settings, including but not limited to chemical plants [1], industrial warehouses [2], nuclear power plants [3], wind farms [4], and many other industrial places [5]. Simultaneously, fires resulting from wire- and cable-related disasters exhibit the highest incidence rates compared to other categories of electrical products [6]. In the United States, an estimated $24 \%$ of industrial or manufacturing fires are attributable to electrical issues, predominantly stemming from cable failures [7]. Cable fires and their subsequent propagation can give rise to catastrophic disasters [6,8]. Undoubtedly, cable fires represent a substantial menace to industrial production safety. Consequently, it is imperative to mitigate cable fire risks and guarantee the secure operation of cables.

Risk analysis and assessment serve as the foundational pillars for the implementation of effective risk control and safety management. In the context of cable fire risk analysis, scholars have centered their focus on comprehending the underlying mechanisms responsible for cable fire incidents [9-13]. The combustion characteristics of wires and cables are intricately linked to the combustion attributes of their constituent materials and structural compositions, which are further influenced by operational conditions and environmental factors [11]. The cause factors of cable fire [10] include cable core overheating, external heating, arc fault, loose cables, wire insulation moisture absorption, cable aging, etc. The

influencing factors and evolution mechanisms of cable fires studied so far have established an important foundation for cable fire risk analysis. However, applying these results to the prevention and control of cable fires in the working process has more practical significance.

Fire risk assessment stands as a fundamental decision-making tool within the realm of risk control and safety management, providing potential risk information before the onset of a fire event. Presently, research endeavors in the field of cable fire risk assessment predominantly revolve around static analytical methodologies, including the weighted fuzzy Petri [14], the survey scoring method [15], and BN [16]. These methods integrate historical monitoring data and expert assessment data relative to risk factors to realize quantitative risk assessments based on multi-source information fusion [14,17]. However, extant studies have regrettably overlooked several pivotal issues: (1) As the factors influencing cable safety undergo temporal variations, the evolution of cable fire risks inherently exhibits dynamic characteristics. Consequently, static risk assessment methodologies fall short of capturing the nuanced and evolving nature of cable fire risks, rendering them unsuitable for dynamic risk monitoring and the timely implementation of prevention and control measures. (2) Faced with the uncertainty in dynamic monitoring data [18,19,20] and the vagueness associated with expert experiential data [21], the development of a cable fire risk assessment model should focus on the stochastic and imprecise aspects of converting quantitative values and qualitative standards. Therefore, the establishment of a dynamic cable fire risk assessment methodology that takes into account the influence of uncertainty in the assessment process is indispensable.

It is well-established that a dynamic Bayesian network (DBN) offers distinct advantages for dynamic risk analysis. It not only elucidates the intricate structure of risk transmission but also tracks the evolving probabilities associated with risk over time [22,23]. Thus far, DBN has found widespread application in dynamic risk assessment across various domains [24,25,26]. Nevertheless, the utilization of DBN in the context of cable fire risk assessment remains uncharted territory. Given the critical consequences of cable fires, exploring this research gap is of paramount importance. Moreover, when addressing data uncertainty in the risk assessment process, the cloud model (CM) [27] emerges as a potent tool. It has introduced an innovative bidirectional conversion method that bridges qualitative fuzzy concepts and quantitatively precise data. The cloud model adeptly considers both fuzziness and randomness within the evaluation process and has found extensive use in tackling problems involving uncertainty conversion [28,29]. Accordingly, the application of the hybrid CM-enabled DBN method in cable fire dynamic risk assessments is warranted.

With the identified research gaps highlighted above, only a limited number of approaches have previously attempted to tackle the aforementioned problem. Given the dynamic nature of cable fire risk assessment of uncertainty, the primary objective of this study is to present a dynamic risk assessment methodology and subsequently evaluate the probability of cable fires, taking into account both randomness and fuzziness within the assessment process. Notably, this study pioneers the utilization of dynamic Bayesian networks (DBNs) in determining the dynamic risk probability of cable fires. To enhance the precision of this assessment, the CM is applied to calculate membership degrees, characterizing the dynamic data with respect to various states of the root nodes. These membership degrees are then integrated into the DBN as prior probabilities for the root nodes. Additionally, the Birnbaum (BM) importance measure [30] and Fussell-Vesely (FV) importance measure [31] are introduced to offer valuable insights for dynamic risk prevention and control strategies. Ultimately, the viability and rationality of the proposed methodology are substantiated via a comprehensive case study involving a cable located in a low-voltage distribution room at the Chongqing Tobacco Logistics Distribution Center.

The remainder of this paper is organized as follows. Section 2 presents the framework of cable fire risk assessment and the hybrid CM-enabled DBN method proposed in this study. Section 3 first describes the primary concerns of the case study and then provides the computational results obtained from the case study to validate the effectiveness of the proposed fire risk assessment method. The fire risk assessment results and a comparison

between the proposed method and the traditional DBN method are presented in Section 4. Finally, Section 5 concludes the study by providing valuable managerial insights and future directions.

# 2. Hybrid CM-Enabled DBN Method 

### 2.1. Dynamic Risk Assessment Framework for Cable Fires

The dynamic framework proposed for cable fire risk assessment is presented in Figure 1 and includes the following three modules:
![img-0.jpeg](img-0.jpeg)

Figure 1. Dynamic risk assessment framework for cable fires.
Establishment of the DBN for cable fires: According to the cable characteristics and working environment conditions, the basic risk factors are identified, and the risk evolution mechanism of cable fires is analyzed. Subsequently, a DBN is built for specific circumstances based on the risk evolution mechanism of cable fires.

Data processing based on CM: The standard cloud characteristic parameters are defined with reference to the range of states of the root node. Meanwhile, the cloud parameters of data are extracted from multisensory monitoring and dynamic expert scoring using data transformation in CM. Thereafter, the membership degrees of the dynamic data were calculated for the standard clouds of each state.

Dynamic risk probability reasoning: The membership degree is taken as the prior probability of each evaluation state of the root node in the DBN. Subsequently, the dynamic risk profiles of cable fires and the changes in BM importance and FV importance are determined based on the dynamic reasoning of the DBN. Finally, we assessed the dynamic risk of cable fires by analyzing the important factors for risk prevention and control.

2.2. Dynamic Bayesian Network

A BN is a type of probabilistic reasoning network based on Bayesian conditional probability and graph theory [32]. A BN assumes the form of a directed acyclic graph, as visually illustrated in Figure 2, wherein nodes symbolize random variables, and directed arcs delineate the causal relationships among these variables. In this context, a node responsible for generating an arc is denoted as the parent node, while the node receiving the directed arc is referred to as the child node [33]. The conditional dependencies between child nodes and their parent nodes were characterized using conditional probability tables (CPTs). Considering the conditional dependencies of variables, the joint probability distribution $P(X)$ of variable $X=\left\{X_{1}, \ldots, X_{n}\right\}$ in the BN can be expressed as follows:

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where $P a\left(X_{i}\right)$ indicates the parent set of $X_{i}$ for any $i=1, \ldots, n ; P\left(X_{i} \mid P a\left(X_{i}\right)\right)$ represents the conditional probability of variable $X_{i}$, and the chain rule of probability and the property of conditional independence have been extensively adopted [34].
![img-1.jpeg](img-1.jpeg)

Figure 2. Simple Bayesian network.
Compared to the traditional static BN, the DBN is a derivative of the BN, which introduces the influence of the internal time series. The dependencies between nodes in a DBN can be distinguished into two types: (i) conditional dependencies under the same time slice and (ii) conditional dependencies across different time slices [22]. A DBN can be defined within a double variable $\left(B_{0}, B_{\rightarrow}\right)$ framework, where $B_{0}$ is a BN that defines the probability distribution $\mathrm{P}\left(X_{0}\right)$ at the initial time, and $B_{\rightarrow}$ is called a "two-slice temporal Bayesian network (2TBN)," which defines the conditional distribution among variables between two time slices according to the following equation [35,36]:

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{n} P\left(X_{i, t} \mid P a\left(X_{i, t}\right)\right)
$$

where $X_{i, t}$ denotes the $i$-th node at time $t, P a\left(X_{i, t}\right)$ indicates the parent node of $X_{i, t}$ for the previous and same time slices, and $n$ indicates the number of nodes in the network.

Meanwhile, a DBN typically follows two assumptions: (1) the Markov hypothesis, which is the probability that the nodes in time $t$ are only affected by time $t-1$, independent of the time segment before $t-1$; and (2) the stationary hypothesis, which states that the conditional probability in $B_{\rightarrow}$ does not change with time [37]. According to the initial probability distribution in $B_{0}$ and the conditional distribution between adjacent time slices in $B_{\rightarrow}$, the joint probability distribution of the nodes from time $t=0$ to $t=T$ can be expressed as follows:

$$
P\left(X_{0: T}\right)=\prod_{t=0}^{T} \prod_{i=1}^{n} P\left(X_{i, t} \mid P a\left(X_{i, t}\right)\right)
$$

where $X_{0: T}$ represents all nodes from time slice $t=0$ to $t=T$.
Figure 3a presents the initial network $B_{0}$ of a DBN, where all variables are static. Figure 3b depicts 2TBN $B_{\rightarrow}$, where the virtual arcs represent the conditional dependencies

of the nodes under different time slices. Extending $B_{\rightarrow}$ to a certain number of time slices yields a complete DBN. To simplify the structure, an abstract form of the DBN is generally used [38], as shown in Figure 3c. The dotted lines in the image refer to the corresponding nodes in the preceding and following time periods.
![img-2.jpeg](img-2.jpeg)

Figure 3. Sample composition diagram of DBN.

# 2.3. Cloud Model Theory 

### 2.3.1. Cloud Model

CM is a bidirectional cognitive model that combines probability theory and fuzzy set theory to deal with problems under uncertainty [27,39]. Three characteristic parameters are utilized to characterize the qualitative concepts in CM: Ex (expectation), En (entropy), and He (hyperentropy). Ex is the measure of the basic certainty of the qualitative concept, which is the most representative point of the qualitative concept. En is a measure of the uncertainty of qualitative concepts, which is determined by the fuzziness and randomness of qualitative concepts, and He reflects the uncertainty of entropy. Forward cloud transformation (FCT) and backward cloud transformation (BCT) algorithms are utilized to realize the bidirectional conversion of qualitative concepts and quantitative values.

The FCT is used to transform the qualitative concept into multiple cloud drops with respect to three characteristic parameters (Ex, En, and He), which involves the following four steps [39,40]:

Step 1. To generate a normal random number Enn $N\left(\right.$ En, He $\left.^{2}\right)$;
Step 2. To generate a normal random number $x_{i} \sim N\left(E x, E n n^{2}\right)$;
Step 3. The Gaussian certainty degree related to the qualitative concept is calculated using Equation (4):

$$
\mu\left(x_{i}\right)=e^{\frac{-\left(x_{i}-E x\right)^{2}}{2 E n n^{2}}}
$$

Step 4. Steps 1, 2, and 3 are repeated until the total number of cloud drops is generated.
The BCT transforms a group of cloud drops into three characters (Ex, En, and He) using the following equation:

$$
\left\{\begin{array}{l}
E x=\frac{1}{m} \sum_{d=1}^{m} X_{d} \\
E n=\sqrt{\frac{\alpha}{2} \times \frac{1}{m} \sum_{d=1}^{m}}\left|X_{d}-E x\right| \\
H e=\sqrt{S^{2}-E n^{2}}
\end{array}\right.
$$

where $X_{d}$ indicates the data series $(d=1,2, \ldots, m), m$ denotes the number of data series, and $S$ symbolizes the variance in $X_{d}$.

The bidirectional conversion using CM is illustrated in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Bidirectional conversion of the cloud model.

# 2.3.2. CM-Based Membership Degree 

In the context of this study, the process of assessing the risk of cable fires necessitated the fusion of information from multiple sources. To extract valuable insights from this amalgamated data, each foundational risk factor is subdivided into distinct states, serving as benchmarks for evaluation. To mine useful information from multi-source data, each basic risk factor can be further divided into different states as a reference standard for evaluation, and the membership degrees of the data for assessment at different states should be calculated [18]. The calculation steps emphasized by Guo, Amin [41] are as follows.
(1) Define the standard cloud characteristic parameters ( $E x^{\prime}, E n^{\prime}$, and $H e^{\prime}$ ) for each state using the following equation $[19,42]$ :

$$
\left\{\begin{array}{c}
E x^{\prime}=\frac{\left(x_{\max }+x_{\min }\right)}{2} \\
E n^{\prime}=\frac{\left(x_{\max }-x_{\min }\right)}{6} \\
H e^{\prime}=\bar{k}
\end{array}\right.
$$

where $x_{\max }$ and $x_{\min }$ represent the upper and lower boundaries of each state, respectively, and the boundary is determined by expert experience or existing criteria. $k$ indicates a constant value, which can be adjusted according to the characteristics of the variable itself. In practice, for a state with only one boundary, such as $\left(-\infty, x_{\max }\right)$ or $\left(x_{\min },+\infty\right)$, default boundary parameters or expectations can be defined according to the actual upper and lower limits of the variable [43].
(2) The cloud feature parameters of the discrete data to be evaluated are extracted using Equation (5).
(3) $n$ cloud drops (i.e., $n=3000$ ) are generated using FCT, and the certainty degrees of each cloud drop are calculated relative to the evaluation standard cloud, with the average value of all results as the membership degree $\mu_{j}(j=0,1, \ldots, m)$.
(4) Membership degree $\mu_{j}$ is standardized, and the final membership degree of the data to be evaluated for the $j$-th state is as follows:

$$
\mu_{j}^{\prime}=\frac{\mu_{j}}{\sum_{j=0}^{m} \mu_{j}}
$$

### 2.4. Importance Measure

Importance measures serve as valuable metrics for gauging the significance of individual components within a system. Importance measures are instrumental tools in identifying system weaknesses and determining the priority of reliability improvement activities [30,44]. In the field of risk assessment, importance measures can be used to analyze the impact of specific risk factors on the evolution of an entire risk system [34,45]. In this study, BM and FV importance measures are introduced to analyze the risk factors of cable fires in terms of risk prevention and control, and they are calculated based on Bayesian reasoning.

In a multi-state case, BM importance can represent the probability change in the target risk event caused by influencing factor $X_{i}$ from the normal state to the dangerous states [30,34], which can be expressed as follows:

$$
B M\left(X_{i}\right)=\frac{\sum_{j=0}^{m}\left|P\left(\varphi(X)=1 \mid X_{i}=b_{i j}\right)-P(\varphi(X)=1) \mid X_{i}=b_{i 0}\right)|}{\left|b_{i}\right|-1}
$$

where $b_{i j}$ represents the $j$-th state of $X_{i}, b_{i 0}$ represents the normal state of $\mathrm{Xi}, P\left(\varphi(X)=1\right) \mid X_{i}=b_{i j}$ ) represents the probability of the target risk event when $X_{i}$ is in the $j$-th state, and $\left|b_{i}\right|$ is the number of states for $X_{i}$.

FV importance is often interpreted as a measure of relative risk reduction in the field of the risk analysis of complex systems [31], and the calculation formula is given as follows:

$$
F V\left(X_{i}\right)=\frac{P\left(\varphi(X)=1\right)-P\left(\varphi(X)=1 \mid X_{i}=b_{i 0}\right)}{P(\varphi(X)=1)}
$$

The larger the $B M\left(X_{i}\right)$ value, the greater the importance of factor $X_{i}$ in terms of risk prevention, and the larger the $F V\left(X_{i}\right)$ value, the greater the importance of factor $X_{i}$ in terms of risk control.

# 3. Case Study 

To demonstrate the practicality of the methods proposed in this study, we conducted a comprehensive assessment of cable fire risk within a low-voltage power distribution room of the Chongqing Tobacco Logistics Distribution Center. The distribution center can be divided into sorting areas, elevated storage areas, business operation rooms, and underground operating spaces. The sorting area is equipped with a total of 15 lines. The elevated storage area has 21 lines. The business operation rooms and underground operating spaces are centrally wired and also have many lines. This facility is characterized by an extensive array of electrical components, necessitating numerous distribution boxes and an extensive network of distribution cables to facilitate power distribution. This underscores the paramount significance of cable fire prevention measures within this region. The single-core cables for internal wiring ( 60227 IEC 05 (BV)) with a nominal cross-sectional area of $0.75 \mathrm{~mm}^{2}$ were selected as the subject to be evaluated. This type of cable has a strong representativeness relative to its presence in factory areas, with the largest amount of wiring and the most intensive production. Table 1 lists the cable's parameters and specifications. The impact load limit of the cable is 17 A , the conductive material comprises solid copper, and the working voltage is 380 V . Subsequently, a risk assessment was implemented based on the proposed assessment framework. Additionally, all calculations in this case are implemented using GeNIe 4.0 Academic (software dedicated to Bayesian modeling), and all experiments were executed on a computer with an Intel(R) Xeon(R) Gold 6230R CPU @ 2.10 GHz under the Windows Server 2019 Standard.

Table 1. Main parameters and performance of type 60227 IEC 05(BV) cables.


### 3.1. DBN Establishment

### 3.1.1. Basic Risk Factors Identification and Risk Evolution Mechanism Analysis

The combustion characteristics of wires and cables are related to the combustion characteristics of component materials and their structures, and they are affected by operating conditions and environmental factors. A comprehensive evaluation of the factory's working and wiring conditions revealed that the fundamental risk factors associated with

cable fires predominantly stem from three key aspects: (i) abnormal electrical condition, (ii) poor line condition, and (iii) adverse operation environment. Abnormal electrical conditions refer to overvoltage or overcurrent, which may be caused by the abnormal load of electrical components; poor line condition refers to insulation damage, insulation aging, poor connection, or insufficient laying spacing for cables, which mainly result from cable performance and manual operation; adverse operation environment refers to high ambient temperature or humidity for cables.

Upon pinpointing the fundamental risk factors and referring to relevant research [16,46], we have illustrated the cable fire risk evolution mechanism within the power distribution room, as depicted in Figure 5. This mechanism comprises two stages: early risk transmission and fire formation. The risk emanates from the foundational risk factors, traverses through intermediate risk factors, and ultimately culminates in the occurrence of a cable fire. The interpretation of the concept of risk varies across different contexts. Generally, risk is commonly defined as the likelihood of an undesirable event occurring or as a combination of the probability and severity of adverse effects. Various disciplines provide differing definitions of risk for their final quantified values, encompassing concepts such as the probability of occurrence, objective uncertainty, the amalgamation of probability and severity, and more. Although the precise forms of these definitions may differ, the consideration of the probability of risk occurrence remains a central aspect for the majority of scholars [47,48]. In this paper, for the sake of simplicity, risk corresponds to the probability of an event in this case.
![img-4.jpeg](img-4.jpeg)

Figure 5. Risk evolution mechanism of cable fires in the power distribution room.

# 3.1.2. Network Structure and Parameter Determination 

The factors and logical relationships in the proposed risk evolution mechanism were mapped onto a DBN, as shown in Figure 6. According to their dependencies, the nodes in the DBN are divided into three categories: (i) root nodes, (ii) intermediate nodes, and (iii) leaf nodes. The solid arrows represent risk transfer between different nodes, and the dashed arrows represent risk transfer within the same node.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** DBN structure of cable fire in the power distribution room.

The assessment states for each node have been systematically categorized based on cable performance and real-world operational conditions (see Table 2). In particular, each root node is divided into three states, S0, S1, and S2, which indicate that the basic risk factors represented by the root nodes are in the optimal, relatively unfavorable, and most unfavorable states, respectively. Moreover, within this set of eight root nodes, the assessment states for X1 to X4 are delineated based on quantitative monitoring data, whereas those for X5 to X8 are determined using expert evaluations that employ a scale ranging from 0 to 10.

The DBN segments' continuous time into discrete time slices. However, the evolution degree of the risk is different for time slices with different lengths. Therefore, before determining the CPT of the DBN, the length of the time slice must first be determined. Generally, the cable (60227 IEC 05 (BV)) reaches a balanced temperature increase within 2 min. To proactively mitigate risks at the earliest opportunity, the time slice length of the DBN in this case was defined as 1 min, serving as the foundation for determining the CPT.

The CPT in a DBN can generally be determined using parameter learning or expert knowledge, and parameter learning is based on a large amount of statistical data. Due to a lack of available data, the CPTs of the nodes were primarily determined by expert knowledge and referred to the CPT data from Chen, Huang [16]. For example, the CPT of leaf node Z is listed in Table 3. The system model's factors correspond to the various represented root node factors. Based on the structure and parameters of the DBN, we can instantiate the DBN. With the principles of DBN introduced in Section 2, we performed dynamic inference using the GeNle software, and a modeling schematic is shown in Figure 7.

**Table 2.** The state division of each node.

S1: mild overload (300~345 V)
S2: severe overload (>345 V) | Y1 | Insulating capacity | S0: good
S1: general
S2: bad  |

Table 2. Cont.


Table 3. A simplified CPT sample about node Z.


![img-6.jpeg](img-6.jpeg)

Figure 7. Schematic diagram of GeNIe-based DBN modeling.

# 3.2. Collection of Processing Data Based on CM 

We opted to conduct a dynamic risk assessment for cable fires in the power distribution room during the operational hours between 2 P.M. and 3 P.M. on 22 November 2021, during which data processing took place. The assessment data for root nodes $\mathrm{X} 1-\mathrm{X} 4$ were derived from the continuous monitoring data collected by four sensors, with readings recorded every three seconds. The fluctuations in these four sets of monitoring data are visually depicted in Figure 8. In addition, the evaluation data of root nodes $\mathrm{X} 5-\mathrm{X} 8$, which can be updated irregularly, were obtained using dynamic expert scoring. Given the brief time frame of this case study, the expert scores remained unaltered throughout the hour, as detailed in Table 4. The expert scoring method is a technique employed to quantify qualitative descriptions, wherein experts assign scores based on their experience and evaluation criteria. In this paper, X5-X8 (insufficient laying spacing, insulation aging, insulation damage, and poor connection quality) are not real-time data and cannot be measured multiple times in a short period. Instead, their risk levels are derived from experts' observations and accumulated work experience. These four risk factors exhibit minimal changes over short timeframes, resulting in scoring results with extended validity that do not necessitate frequent updates. Consequently, based on the aforementioned factors, it can be inferred that the absence of updates within a 60 min interval would not significantly impact the results.

![img-7.jpeg](img-7.jpeg)

Figure 8. Monitoring data for nodes $\mathrm{X} 1-\mathrm{X} 4$.

Table 4. Expert scores for nodes $\mathrm{X} 5-\mathrm{X} 8$.


# 3.2.1. Evaluation Standard Cloud Determination 

Prior to computing membership using the CM, it is imperative to convert the initial evaluation state into evaluation standard clouds for precise quantitative interpretation. The standard cloud characteristic parameters $\left(E x^{\prime}, E n^{\prime}, H e^{\prime}\right)$ for the states of the root nodes in Table 2 are defined by Equation (6), as listed in Table 5.

Table 5. Standard cloud characteristic parameters for different states of root nodes.


3.2.2. State Membership Degree Calculation

The assessment period was divided into 60 discrete slices, with each lasting 1 min. Within each of these time slices, the state membership degrees of the datasets were fed into the DBN as prior probabilities. Initially, the cloud characteristic parameters of the data were extracted using Equation (5), and cloud drops were generated via the FCT for comparisons with the evaluation standard clouds of node states. Considering the cloud conversion in the first minute as an example, Figure 9 shows a comparison of the cloud distribution between the root node data and evaluation standards. The membership degree calculation was based on Equations (4) and (7). Figure 10 shows the membership changes in the monitoring data of nodes X2 and X4 relative to different states within 60 min, while the membership degrees of node X1 and X3 data for state S0 are always one. Moreover, because expert scoring data are not updated within 60 min, the state membership degrees of the nodes from X5 to X8 remain unchanged. Table 6 lists the cloud characteristic parameters and the state membership degrees of the expert scoring data.

![img-8.jpeg](img-8.jpeg)

**Figure 9.** Comparison of cloud distribution between the root node data and the evaluation standards in the first minute.

![img-9.jpeg](img-9.jpeg)

Figure 10. Membership degree changes of monitoring data of nodes.

Table 6. Cloud characteristic parameters and state membership degrees of the expert scoring data.


# 3.3. Dynamic Risk Reasoning and Analysis 

### 3.3.1. Dynamic Risk Profiles

Upon the completion of data processing using the CM, the state membership degrees of the datasets were input into the established DBN framework for dynamic cable fire risk assessments. By realizing probabilistic reasoning using the GeNIe program, we inquired about the state progression of intermediate nodes over the course of the 1 h monitoring period, as depicted in Figure 11. The dynamic risk profile for cable fires was also obtained (see Figure 12), and the risk assessment results were expressed in terms of safety or risk probability. Intermediate nodes serve as the direct factors responsible for igniting fires. Therefore, analyzing the evolution of intermediate node states helps us understand the interactions among various root nodes and the impacts they bring. Furthermore, it offers valuable insights into the potential numerical states of intermediate nodes once they reach various risk levels, facilitating the more effective implementation of safety measures in subsequent stages.

![img-10.jpeg](img-10.jpeg)

Figure 11. State evolution of the intermediate nodes.
![img-11.jpeg](img-11.jpeg)

Figure 12. Dynamic risk profile for cable fires.
As depicted in Figure 11, except for Y3 (loose contact) and Y4 (poor heat dissipation), the risk status of the intermediate node primarily changes with the membership degree of X2 nodes in Figure 10, and the risk transmission path of these dynamic change nodes is $\mathrm{Y} 2 \rightarrow \mathrm{Y} 6 \rightarrow \mathrm{Y} 7 \rightarrow \mathrm{Y} 1 \rightarrow \mathrm{Y} 5$. As the S 1 state value of X 2 first increased and then decreased, the S1 state values of Y2 and Y6 also increased first and then decreased, whereas the S1 state values of Y7, Y1, and Y5 entered a relatively stable status around the 40th minute following a rapid increment (see Figure 10). This is because material pyrolysis and the subsequent reduction in insulation capacity are irreversible, leading to related risks are cumulative.

Meanwhile, in nodes Y5-Y7, which directly affect the fire risk, the S1 and S2 values (i.e., 0.534 and 0.051 , respectively) of node Y7 were the highest during this 60 min .

According to Figure 12, the development of the cable fire risk within 60 min can be divided into three phases. The first phase is $0-16 \mathrm{~min}$, with a slow increase in fire risk; the second phase is $17-37 \mathrm{~min}$ when the risk value rapidly reaches the peak of 0.230 and exceeds a Level 1 Warning, thus necessitating the consideration of measures for risk control in this phase; the third phase is $38-60 \mathrm{~min}$, with the risk value steadily decreasing to approximately 0.1 . Meanwhile, the changing trend of the overall fire risk was roughly consistent with the changing trend of the S1 value of node X2 in Figure 10.

In this study, our primary goal is to evaluate the fire risk of cables by considering various external risk factors through a risk assessment lens rather than addressing the reliability issues of the electrical system itself. As a result, we have not extensively explored the multivariate models of the terminal situation of energy flow transmission and associated equations.

# 3.3.2. Dynamic Importance Analysis 

The networks (i.e., the risk evolution mechanism and DBN structure) presented in Figures 5 and 6 indicate that numerous risk factors may lead to cable fires in the distribution rooms. To pinpoint the critical basic factors that influence cable fires, we designated node Z (Fire) as the target node for the importance analysis of the root nodes. The significance of risk control was gauged using FV importance, while the importance of risk prevention was assessed via the BM's significance.

During the ascending phase of risk, the pivotal imperative is the timely control of risk. Consequently, we focused on assessing the significance of risk control for the second phase of rapid risk escalation, as depicted in Figure 12. The FV importance of the root nodes in the second phase is calculated according to Equation (9), and the results are presented in Figure 13. It can be observed that the FV importance values of nodes $\mathrm{X} 7, \mathrm{X} 8$, and X 2 are consistently significantly larger than those of other nodes, which means that improving the status of these nodes will reduce fire risks. Meanwhile, it is worth mentioning that the total FV importance value of the root nodes decreases from approximately $70 \%$ to approximately only $30 \%$ during this phase, which may be caused by the irreversible increase in the risks of intermediate nodes Y5 and Y7, which directly affect the fire risk (see Figure 11). Therefore, effectively reducing the risk level by controlling the risk factors of the root node is insufficient. As the risk exhibits an upward trend, the earlier prevention and control measures are taken, the lower the risk control effect. The power supply should be cut off as soon as possible to check for the pyrolysis of the cable, and the unqualified cable should be replaced in a timely manner.

According to Equation (8), BM importance across multiple states is determined by assessing the influence of each individual state change on the target node. Consequently, we initially examined the impact of various states of each root node on target node Z (Fire). Assuming that all root nodes are in their optimal states $(\mathrm{S} 0=1)$ at the initial time $(\mathrm{t}=0)$, we employed DBN reasoning to observe the alteration in cable fire risk probability over 10 time slices when the root node changes to two different states, as illustrated in Figure 14. In the S1 state, nodes X1 and X7 have the greatest impact on the probability of cable fire risk, and the impact of X7 increases with time. In the S2 state, nodes X1, X5, X2, X7, and X6 have a significant influence on cable fire risk probability, and the fire risk probability reaches one at the tenth time slice.

![img-12.jpeg](img-12.jpeg)

Figure 13. Dynamic FV importance of the root nodes.

![img-13.jpeg](img-13.jpeg)

Figure 14. Change in cable fire probability with time under different states of the root nodes.

The BM importance values within 10 time slices of each root node were then obtained using Equation (8), as depicted in Figure 15. The order of the BM importance values from the largest to smallest at the 10th time slice was X7 (0.887), X1 (0.75), X5 (0.6), X6 (0.549), X2 (0.498), X3 (0.271), X4 (0.03), and X8 (0), whereas the values of X7, X6, X2, and X3 increased over time. The greater the BM importance value, the higher the fire risk caused by the node. Therefore, the risk factors corresponding to nodes X7, X1, X5, X6, X2, and X3 in cable fire risk prevention should receive more attention.

![img-14.jpeg](img-14.jpeg)

Figure 15. Dynamic BM importance of the root nodes within 10 time slices.

# 4. Discussion 

### 4.1. Discussion on Dynamic Risk Reasoning and Importance Analysis

The landscape of cable fire risk factors is typically intricate, with a complex evolutionary mechanism. Through the construction of a DBN, the interplay between these risk factors is succinctly captured via directed arcs and conditional probabilities, as visually presented in Figure 6 and Table 3. Moreover, probability-based reasoning within the DBN empowers us to quantify risk and provide a lucid portrayal of risk evolution over time, as demonstrated in Figures 11 and 12. Hence, it is conducive to grasping the dynamic risk profiles of cable fires using the DBN. Furthermore, because the cable fire risk evolution is a continuous and dynamic process, the states of the intermediate nodes may be affected by the previous moment, such as Y6 (Overheating risk) and Y7 (pyrolysis risk). The DBN associates nodes between adjacent moments by introducing Markov chains, whereas the traditional BN cannot reflect the influence of nodes at different times. Therefore, it is reasonable to use a DBN for the dynamic risk reasoning of cable fires.

The purpose of risk assessment is to prevent and control risks over time. Thus, after obtaining quantitative dynamic risk profiles, it is necessary to analyze the key factors of risk prevention and control. As presented in Figures 12 and 14, FV importance reflects the degree of risk reduction caused by root node state improvement, and BM importance reflects the degree of risk increase caused by root node state deterioration. Therefore, introducing FV and BM into DBN can provide a dynamic and targeted reference for risk prevention and control.

### 4.2. Comparison with Traditional DBN Method

To address the uncertainty in the evaluation process, the data to be assessed underwent a conversion process using the CM, as depicted in Figure 6 and Table 4. The resultant membership degrees were subsequently employed as the prior probabilities for the root node within the DBN. To compare the difference between the CM-enabled DBN and traditional DBN methods in dealing with data uncertainty, the DBN reasoning result of the cable fire risk probability under the traditional threshold method [49] is shown in Figure 16. It is evident that the trends of the reasoning results of the two methods are almost identical. However, on the one hand, the fire risk probability using the traditional DBN is consistently lower than that of the proposed method. On the other hand, the fire probability of the first phase ( $0-16 \mathrm{~min}$ ) obtained by the traditional DBN is always zero, which is inconsistent with reality. This result may be due to the rough division of the data, which makes the threshold method less sensitive to uncertain data. The traditional DBN employs a frequency-based statistical method, where the occurrence frequency of assessment data in different states over a period of time is used as the prior probability input for root nodes. This represents a simplistic and rough division at the data level, consequently leading to final inference results of 0 . Accordingly, compared with the traditional threshold method, CM can obtain

more information in monitoring data and expert scoring data, and the reasoning results based on CM-enabled DBN are more sensitive and reliable.
![img-15.jpeg](img-15.jpeg)

Figure 16. Comparison of the fire risk probability obtained using different methods in monitoring time.

# 4.3. Limitations of the Proposed Method 

As previously mentioned, the feasibility and reasonability of the proposed method for the dynamic risk assessment of cable fires were verified in this study. However, this study has several considerable limitations. In the assessment case, the fire risk factors of the cables in the power distribution room, including 15 risk factors at two levels, were determined. However, due to some risk factors, such as external fire sources existing in the distribution room, the identified risk factors may not be sufficiently comprehensive. Furthermore, due to the lack of sufficient data, the risk transfer mechanism and CPTs were primarily determined by referring to experts' opinions and the relevant literature. Thus, a certain degree of subjectivity is inevitable in risk assessment. To reduce the subjective influence, structural learning and parameter learning [50,51] can be used in actual assessments to further improve the DBN. Moreover, the fire risk associated with cables is intrinsically connected to energy fluctuations within the electrical system and the reliability of equipment. To mitigate the subjectivity in fire risk assessment and bolster the quantitative interpretation and analysis of risks, we intend to include multivariate models of the terminal energy flow transmission situation and associated equations within our future research endeavors. Moreover, we only analyzed the importance of single-node risks for risk control, and investigating the importance of risk control in multi-node joint cases will be a focus of our future research.

## 5. Conclusions

Considering the dynamic evolution characteristics of cable fire risk and the uncertainty of the evaluation data, this study proposes a hybrid CM-enabled DBN method for cable fire risk assessment. First, a dynamic fire risk assessment framework was developed, where three modules were proposed: (i) cable fire DBN establishment, (ii) CM-based data processing construction, and (iii) dynamic fire risk reasoning and analysis. Subsequently, a DBN was applied to determine the dynamic risk probability of cable fires, and a CM was applied to deal with the uncertainty of the evaluation data. Subsequently, the BM and FV importance measures were introduced to provide a reference for dynamic risk prevention and control. Furthermore, a case study of the cable of a low-voltage distribution room at the Chongqing Tobacco Logistics Center was implemented to validate the proposed method. Dynamic risk profiles and importance changes were obtained, and the risk reasoning results were also discussed, which illustrates the feasibility and rationality of the proposed

method. Finally, the assessment results of the proposed method and the traditional DBN method were compared, which confirmed that the results based on the proposed hybrid CM-enabled DBN method are more reliable. According to the results and discussion, the primary contributions of the proposed method are as follows:

1. For the first time, DBN was applied to the dynamic risk assessment of cable fires, which not only realized the dynamic reasoning of fire risk values but also clearly depicted the state changes in risk factors.
2. CM was used to convert sensor monitoring data and expert scoring data into the state membership degrees of the root node; then, the membership degrees were input into the DBN as a prior probability. Using CM-based data processing, randomness and fuzziness are emphasized in the risk assessment process, and additional information can be mined from the data.
3. BM and FV importance was introduced to identify the key nodes from the two dimensions of risk prevention and risk control, respectively. Dynamic importance analysis can be realized based on its associated reasoning, which is conducive to reasonable risk prevention and timely risk control.
Given the above explanations, this study enables a dynamic risk assessment for cable fires by considering the uncertainty of the evaluation data. Based on the proposed framework, reasonable structure learning and parameter learning methods can be introduced in the future to develop a more scientific DBN, and investigating the importance of risk prevention and control in multi-node joints will be the focus of future research. Moreover, the proposed method can provide support for the real-time risk assessment of cable fire risk, and the assessment is expected to achieve wider application value in industrial fire prevention and risk management by integrating it with Internet of Things (IoT) technology.

Author Contributions: Conceptualization, Z.X.; Methodology, Z.X.; Software, Z.X.; Formal analysis, Y.Y.; Investigation, G.H. and X.G.; Writing—original draft, S.G.; Writing—review \& editing, X.G.; Supervision, G.H., Y.Y. and X.G.; Project administration, G.H.; Funding acquisition, X.G. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by the Interdisciplinary Research Project for Young Teachers of USTB (Fundamental Research Funds for the Central Universities) (No. FRF-IDRY-21-016) and the Central Basic Research Fund project (No. 282022Y-9462).

Data Availability Statement: The data used in this study has been provided in this article.
Conflicts of Interest: The authors declare no conflict of interest.
