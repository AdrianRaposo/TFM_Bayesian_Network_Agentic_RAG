# Article 

## Risk Assessment of Seaplane Operation Safety Using Bayesian Network

Qin Xiao ${ }^{1}$, Fan Luo ${ }^{1, *}$ and Yapeng $\mathrm{Li}^{2, *}$<br>1 School of Management, Wuhan University of Technology, Wuhan 430070, Hubei, China; 1259012677@whut.edu.cn<br>2 School of Transportation, Wuhan University of Technology, Wuhan 430070, Hubei, China<br>* Correspondence: luofan@whut.edu.cn (F.L.); 148773@whut.edu.cn (Y.L.)

Received: 4 May 2020; Accepted: 28 May 2020; Published: 30 May 2020


#### Abstract

Seaplanes have become popular tourism and transportation tools with the ability of take-off and land on water. Recent seaplane accidents are highlighting the need for safety analysis of the seaplane operation process, which includes the sequential stages of water-taxiing, take-off, flight, and landing. This paper proposes a novel approach to modeling the risk of seaplane operation safety using a Bayesian network (BN). The rough risk factors that may cause seaplane accidents are identified by historical data, literature review, and interviews with experts. Based on the identification result, a risk evaluation indicator system is constructed and screened by the Delphi method. The structure of the proposed BN is derived from the indicator system. The parameter of the BN is obtained by expert experience and parameter learning from statistical data. The BN model is validated with an out-of-sample test demonstrating nearly $95 \%$ prediction accuracy of the accident severity level. The model is then applied to conduct diagnosis inference and sensitivity analysis to identify the key risk factors for seaplane operation accidents. The result shows that the four most critical risk factors are mental barrier, mechanical failure, visibility, and improper emergency disposal. It provides an early warning to take appropriate preventive and mitigative measures to enhance the overall safety of the seaplane operation process.


Keywords: seaplane operation safety; Bayesian network; risk assessment; sensitivity analysis

## 1. Introduction

The seaplane is a kind of fixed-wing aircraft able to take off from and land on water (Commission Regulation (EU) No 965/2012). It can be classified into the two types, water only and amphibious, according to take-off and landing patterns. Due to thisunique ability, seaplanes are quite suitable for short-distance travel in a broad range of scenarios [1] and have become popular tourism and transportation tools. In recent years, however, the frequent seaplane accidents causing significant social and economic losses have brought attention to the safety issues of seaplanes. On 20 July 2016, a nine-seat seaplane crashed into a bridge in Shanghai's Jinshan District, killing five people onboard and injuring the other five. An investigation showed that management failure and lack of qualifications were the main causes of the accident. On 14 May 2019, a deadly mid-air collision of two seaplanes in Alaska killed six people and injured ten. The investigation by the National Transportation Safety Board (NTSB) reported that the seaplane safety could be improved by applying advanced crash prevention technology. This paper focuses on the risk assessment of the seaplane operation process, which will be helpful for authorities and operators to find critical risk factors and develop effective measures to reduce seaplane accidents.

The difficulty of risk assessment for seaplane operation safety exists in the enormous risk factors [2] and their complex and uncertain interrelations [3,4]. Risk factors are closely associated with the whole

operation process, which includes the sequential stages of water-taxiing, take-off, flight (initial climb, en route, and approach), and landing. The seaplane operation process starts and ends in water aerodromes [5,6] and is a visual flight, which distinguishes seaplanes from land aircraft. Seaplanes have no brakes; once a seaplane casts off or is untied, wind will keep the seaplane in constant motion, making the seaplane different from a ship. Seaplane pilots should do their best to maintain balance and ensure operation safety. Furthermore, wind has a significant impact on the direction of the seaplane, and weather conditions may limit the visibility of the pilot. Both the maritime sector and the civil aviation authorities are responsible for supervising seaplanes, which brings great challenges for seaplane administration [2].

Researchers have dedicated their efforts to understanding and analyzing the safety risks of seaplane operation. References [7,8] identified the risk factors of seaplane-ship collision by using human engineering theory. By applying approaches including decision-making trial, evaluation laboratory, and interpretative structural modeling, they established a four-level hierarchical structure model of the risk factors. Reference [9] designed the three-dimensional structure for the management mode of seaplane navigation safety based on the Hall 3D structure in system engineering. Reference [10] analyzed the conflict risks of the seaplane runway on the water aerodrome by using the fault tree method and the Bayesian network (BN) method. Their research indicated that the meteorological factor and the hydrological one are the most sensitive factors leading to the runway conflict. However, these researches on safety analysis of seaplane operation mainly focused on asingle accident event and analysis of specific operation stages. There is lack of systematic risk identification and assessment for the entire seaplane operation process.

There are some risk and safety analysis techniques widely used to reduce accidents: fault tree [11,12], event tree [13,14], bow-tie [15,16], and Bayesian network [17-21]. Compared to other techniques, Bayesian network (BN) has strong applicability in obtaining the probability when data are inaccurate, incomplete, or subjective and in dealing with uncertainty through probabilistic values [12]. Further, it is possible for BN to perform probability updating and sequential learning [18], which means BN can be used to do risk analysis with a temporal dimension. Due to these advantages, the BN approach is adopted in this paper to evaluate the safety risks of the seaplane operation process.

This paper aims to build a practical Bayesian network (BN) model for risk assessment of seaplane operation. The complicated risk factors are classified into four categories: pilot, aircraft, environment, and management. The risk factors causing seaplane accidents are identified according to historical data, literature review, and interviews with experts. With a screening approach, we construct an indicator system with 4 second-level risk factors and 18 third-level risk factors. The structure of the indicator system is used to build the structure of the BN model. Expert experience and statistical data are used to determine the prior probabilities and the conditional probability table of the BN model. The structure and the probability parameters together define the BN model. The model is validated with an out-of-sample test, which demonstrates approximately $95 \%$ prediction accuracy of the accident severity level. The validated model is then applied to conduct diagnosis inference and sensitivity analysis to identify the key risk factors for seaplane operation accidents. Results show that the four most critical risk factors are mental barrier, mechanical failure, visibility, and improper emergency disposal. These results provide an early warning to take appropriate preventive and mitigative measures to enhance the overall safety of the seaplane operation process.

The rest of the paper is organized as follows. Section 2 reviews the main research methodology. Section 3 presents the proposed approach for seaplane operation safety risk modeling, including risk identification, construction and screening of the indicator system, establishment of the BN model, and BN validation test. Section 4 applies the BN model to do diagnosis inference and sensitivity analysis. Section 5 discusses the principle contributions of this paper and Section 6 offers concluding remarks.

# 2. Research Methodology 

This paper uses the approaches of statistical analysis, expert interview, Delphi method to identify and screen risk factors and Bayesian network (BN) to establish the BN model.

### 2.1. Statistical Analysis

Official accident reports play an essential role in risk factor analysis because the reports are written by an accident investigation board and usually present valuable and detailed information about the causes and results of accidents [22]. We collected and analyzed a total of 28 seaplane accident reports during 2010-2016 from a government website (https://www.ntsb.gov/investigations/AccidentReports/ Pages/aviation.aspx). The statistics of the accidents indicate that collision is the most typical accident type in seaplane operation.

### 2.2. Expert Interview

The purpose of the expert interview is to obtain risk factors from the practice of seaplane operation. In this paper, we designed a series of questions and interviewed five experts with different backgrounds related to seaplane research and practical experience, as shown below:

Expert 1: An academic expert in aviation safety management.
Expert 2: An academic expert in ship sailing safety.
Expert 3: A safety manager from the general aviation industry in China who has investigated the current development of seaplanes in the US and Canada.

Expert 4: An experienced seaplane pilot from the general aviation industry in China.
Expert 5: A technical manager from the general aviation industry in China.

### 2.3. Delphi Method

This paper constructs a rough indicator system based on risk factors identified from statistical analysis, literature review and expert interview. However, not all indicators are important. It is necessary to screen the indicators and obtain a convincing indicator system. Here we use the Delphi method which has been considered as a popular qualitative analysis technique to screen indicator systems. The Delphi method, proposed as an expert opinion survey method in the 1950s [23], is a systematic and interactive research approach forobtaining the opinions of a group of experts on a specific topic. In the method, the selected experts are asked to participate in two or more rounds of structured surveys. Anonymous response, iterative and controlled feedback, and statistical group response are the main characteristics of the Delphi method [24].

In this paper, the five experts mentioned in "Expert interview" were asked to participate in the questionnaire survey due totheir experience and knowledge. Two rounds of structured surveys were performed in this paper. The first aimed to screen the preliminary indexes according to their expert opinions. The second was to screen indexes by degree of importance calculated by expert rating. The expert rating scale for the operation safety risk assessment of the seaplane is based on the five-point Likert scale, where 5 means most important, 4 means important, 3 means generally important, 2 means not too important, and 1 means not important. Arithmetic mean value $N_{j}$ and variation coefficient value $v_{s}$ are the main matrix of screening indicators.

$$
N_{j}=\left(\sum_{i=1}^{n_{j}} X_{i j}\right) / n_{j}
$$

where $N_{j}$ is the arithmetic mean value of the $j$ th index, $n_{j}$ is the number of experts who participated in the evaluation of the $j$ th index, and $X_{i j}$ represents the rating value of the $i$ th expert on the $j$ th index. A higher value of $N_{j}$ means that an index is more important.

$$
v_{s}=\sqrt{\sum_{i=1}^{n_{j}}\left(X_{i j}-N_{j}\right)^{2} / n_{j}} / N_{j}
$$

where $v_{s}$ is the variation coefficient value of the $j$ th index, which reflects the relative discrete degree of expert evaluation results. A lower value of $v_{s}$ means an index has better convergence.

Based on the result of a consultation with the experts, this study sets $N_{j} \geq 3.5$ and $v_{s} \leq 0.4$ as the screening criteria.

# 2.4. Bayesian Network 

BN is a widely used tool for modeling complex systems, particularly in the absence of accessible data [25]. On the other hand, as a probabilistic inference method, it has advantages in that it usesprobability theory to deal with uncertainties. Here the BN model is selected to assess the operation safety risks of seaplanes because this risk assessment work is an activity that requires inference from incomplete, inaccurate, or uncertain knowledge and information.

Combined with probability theory and graph theory, a BN is a directed acyclic graph (DAG) that includes a certain number of nodes and edges [26-28]. DAG reflects the causal dependency and causal inference between nodes. For an edge connecting two nodes, the node it starts from is called a parent node and the node it ends at is called a child node. For example, if an edge from $X 2$ to $X 4$ exists, $X 2$ is the parent node and $X 4$ is the child node. A node that edges only start from is called a root node, which means a root node cannot be regarded as a child node for any edges. Root nodes are presented within a prior probability table. The remaining nodes have their conditional probability distributions and are presented within a conditional probability table. It should be noted that the probability of a parent node will affect the conditional probability of its child node(s).

In BN, the network structure can be regarded as a qualitative part of the model, whereas the probability parameters represent the quantitative aspect of the model [29]. The joint probability distribution of a set of random variables $U=\left\{\begin{array}{ll}x_{1}, & \cdots, \quad x_{n}\end{array}\right\}$ based on the conditional independence and the chain rule [26], is included in the network as:

$$
P(U)=\prod_{i=1}^{n-1}\left(x_{i} \mid x_{i+1} \quad \cdots \quad x_{n}\right)=\prod_{i=1}^{n}\left(x_{i} \mid P_{a}\left(x_{i}\right)\right)
$$

where $P(U)$ is the joint probability distribution and $P_{a}\left(x_{i}\right)$ as the parent set of variable $x_{i}$. A simple BN with a set of dependent random variables $x_{i}$ is illustrated in Figure 1 and the joint probability distribution is expressed as:

$$
P\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=P\left(x_{1}\right) \times P\left(x_{2} \mid x_{1}\right) \times P\left(x_{3} \mid x_{1}\right) \times P\left(x_{4} \mid x_{2}, x_{3}\right)
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. A sample of a Bayesian network.
DAG represents the qualitative relationship of the BN. The conditional probability table (CPT) is used to describe the quantitative relationship in DAG for discrete random variables. The Bayes theory is the basis of BN, which can be expressed as:

$$
P(V \mid \theta)=\frac{P(\theta \mid V) P(V)}{P(\theta)}
$$

where $\theta$ is the evidence, $P(V)$ is the prior probability before considering any evidence, $P(V \mid \theta)$ is the posterior probability (given evidence of $\theta$, the likelihood of $V$ ), $P(\theta \mid V)$ is the conditional probability which represents how likely the evidence is true. $P(\theta)$ is the normalization factor [28].

# 3. Proposed Approach for Seaplane Operation Safety Risk Modeling 

### 3.1. Risk Identification

The goal of risk identification is to obtain all possible risk factors affecting the seaplane operation safety for analysis. Three sources, historical data, literature review, and interviews with experts are used to identify the risk factors. The SHEL model [30] is adopted to help identify risk factors from four categories: pilot risk, aircraft risk, environmental risk, and management risk. For most risk factors, they can be mapped to the four categories obviously. For other factors whose categories are not clear, we classify them by discussing with experts. We identified 30 main risk factors from the three sources. They are listed as follows (refer to Table A1 for a description of risk factors and Figure A1 for which operation stage they occur at):
(1) Identified 12 risk factors by historical data

Pilot skill error, illegal operation, lack of experience, handling error, mental barrier, performance defect, weight imbalance, visibility, environmental complexity of the takeoff and landing field, communication distortion, supervision error, and system loss.
(2) Identified 16 risk factors by literature review

Excessive flying time [31], mechanical failure [32], maintenance error [33], wind/oblique flow threat [34], wind/swell threat [34], weather changes during flight [35], bird damage [36], inapplicability of laws and regulations [32] and management failure [37], lack of experience [38], handling error [39,40], mental barrier [41], performance defect [42], visibility [34,35], environmental complexity of the takeoff and landing field [40], communication distortion [43], andsupervision error [37].
(3) Identified 21 risk factors by interviews with experts

Skill assessment failure, low flight experience, mental barrier, overloading, weight imbalance, maintenance error, wind/oblique flow, visibility, wind/swell, improper channel/anchorage layout,

blurry sea lanes, traffic flow, low-altitude surveillance command error, channel invasion, bird damage, weather changes during flight, communication distortion, inapplicability of laws and regulations, departmental conflicts, operational command error, and improper emergency disposal.

# 3.2. Construction and Screening of the Indicator System 

The indicator system must reflect the entire process of the seaplane operation safety risk. Hence, it should meet scientific, systematic, targeted, and practical principles. Risk factors are the foundation of constructing an indicator system, which serves as the macroscopic reflection of the risk factors. This study constructs an indicator system including 4 second-level indicators and 30 third-level indicators derived from the result of risk identification. The Delphi method is then used to screen the indicator system. Statistical results of arithmetic mean value and variation coefficient value are presented in Table 1.

Table 1. Expert statistical result of seaplane operation safety risk indicators.


In the "Note" column in Table 1, an asterisk (*) means that the corresponding risk factor meets the requirements of $N_{j} \geq 3.5$ and $v_{s} \leq 0.4$ while a blank space indicates that the factor does not satisfy the requirements. After eliminating the factors which may not be important, we obtain 18 basic indicators in total. Finally, an indicator system with 4 second-level indicators and 18 third-level indicators is constructed, as shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Seaplane risk evaluation indicator system.

# 3.3. Establishment of the Bayesian Network 

The construction of a Bayesian network (BN) includes the structure aspect and the parameter aspect. The BN structure can be obtained usingthree approaches: manually, automatically, or a combination of both [44]. In this paper we obtain the structure manually according to the three-level indicator system. The BN parameters are composed of the prior probability tables (PPT) and the conditional probability tables (CPT). In this paper we utilize both expert experience and the parameter learning algorithm expectation-maximization (EM) [45]. Hugin 8.4 is used to establish the BN.

First we need to figure out the BN structure. As the classification of risk factors in the above indicator system is relatively independent, the risk factors are drawn layer by layer, which means that the correlation between the factors in the same category is stronger than the correlation between the factors in the third level. Therefore, this study does not consider the possible weak correlation between the factors in the third level when constructing the BN structure [46]. The BN structure is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network structure of the seaplane.

There are 18 root nodes, 4 intermediate nodes and 1 leaf node in the BN structure. The single leaf node (U) represents seaplane accidents. It has three states of "minor", "substantial", and "destroyed", which describe the severity levels of accidents. The seaplane accidents are mainly prevented by fouraspects of measures: pilot (U1), aircraft (U2), environmental (U3), and management (U4). Each measure has two states,"yes" and "no", where "yes" means the measure works and "no" means failure. The measures include the prevention of the basic risk events (U11, U12, ..., U45). These events are represented by root nodes with two states, where "yes" indicates the risk event happens and "no" means safety.

Based on the above structure, the BN parameters are obtained by two steps. First the PPT and the CPT are directly elicited by the same five experts mentioned in Section 3.2. The problem scope, the elicitation process, and the fundamental theory of BN were introduced in detail to each expert to guarantee that they understood the objective of this process [32]. A consensus on the BN parameters was reached in the end. The second step is parameter learning. We adopt a random statistical method to gather information on 110 seaplane accidents during 2010-2016 from the Aviation Safety Network database, which includes the 28 accidents from the reports mentioned in Section 3.1. Of the 110 accidents, 87 are input into the parameter learning algorithm EM to obtain the final PPT and CPT (the remaining 23 were used for validation testing in Section 3.4). It should be noted that without the first step the parameter learning can also work. However, the expert experience in the first step provides the prior knowledge for the parameter learning and thus makes the BN model more accurate and practical.

The established BN is shown in Figure 4. It is obvious that the occurrence probability of minor accidents ( 0.4847 ) or destroyed accidents ( 0.3380 ) is greater than that of substantial accidents ( 0.1773 ). As for the risk factors leading to accidents, aircraft factors play the most important role with an occurrence probability of 0.3551 , followed by pilot factors with 0.2385 , environmental factors with 0.2000 , and management factors with 0.0682 . It can be seen that pilot factors and aircraft factors are the key risk factors of seaplane accidents, which is in accordance with the risk factor research on aviation aircraft accidents $[47,48]$.
![img-3.jpeg](img-3.jpeg)

Figure 4. The Bayesian network for seaplane operation safety risk assessment.

# 3.4. BN Validation Test 

The remaining 23 of the 110 seaplane accidents referred to in Section 3.3 are used to test the accuracy of the BN model. In the total accident data and the test data, $17 \%$ of required data are missing, namely, for each accident case, on average, $17 \%$ of the nodes in BN have an unknown state. This is mainly due to some risk factors not being included in the accident reports. Similar to the validation process employed by Sheehan et al. (2019), the out-of-sample test is performed for each of the 23 accident cases, where the accident severity level is predicted using the constructed BN model. The prediction severity level is assumed to be the state forecasted with the highest probability. The test result for 10 cases is shown in Table 2. The prediction state (in bold) is compared with the actual state from each accident case. It is predicted accurately in 22 out of 23 accident cases, which is nearly $95 \%$ accuracy.

Table 2. Out-of-sample test result for 10 accident cases.


# 4. Application of the BN model 

With the Bayesian network (BN) model, the diagnosis inference and the sensitivity analysis can be conducted to analyze the causal relationship of risk factors that cause accidents, as well as to identify the key risk factors from the categories of pilot, aircraft, environmental, and management.

### 4.1. Diagnosis Inference

The BN model can be applied to diagnose the most likely risk factors when a result such as an accident happens. In this section we analyze the following two scenarios: when different severity levels of accidents happen and when different categories of measures fail. The index of change rate is used here to indicate how a given result affects the occurrence probability of a risk factor. It is calculated as follows:

$$
\text { Change rate }=\frac{\text { Posterior probability }- \text { Prior probability }}{\text { Prior probability }} \times 100 \%
$$

We adopt the real value instead of the absolute value. Thus, a positive change rate represents an increase in the occurrence possibility of the risk factor while a negative rate represents a decrease when evidence is found.

For the first scenario, the states of seaplane accidents (U) are set to "minor", "substantial", and "destroyed", respectively, to observe the occurrence probability of the state "yes" for all the other nodes, as shown in Table 3. The result shows that in minor and substantial accidents, the order of the most possible risk factors causing the accidents is: environment (U3) $>$ aircraft (U2) $>$ management (U4) $>$ pilot (U1). However, in destroyed accidents, the order is completely opposite: pilot (U1) $>$ management (U4) $>$ aircraft (U2) $>$ environment (U3). As for the change rate, in minor accidents, the change rates of the risk factors system loss (U41), failure of skill assessment (U11), and wind/oblique flow threat (U31) are greater than those of other risk factors. On the other hand, the risk factors visibility (U33), mechanical failure (U22), aircraft performance defect (U21), and environmental complexity of the take-off and landing field (U34) are more prominent in substantial accidents. The risk factors mental barrier (U15), improper emergency disposal (U45), mechanical failure rate (U22), and operation command error rate (U44) are responsible for destroyed accidents.

For the second scenario, the states of pilot risk (U1), aircraft risk (U2), environmental risk (U3), and management risk (U4) are set to "yes" and "no" respectively.
(1) Diagnosis inference for pilot factors

Table 4 illustrates the occurrence probabilities of casual risk factors under the assumption that pilot risk occurs. We can say that with a small increase in the probability of U1, the occurrence probability of U15 increases the most, which means that mental barrier is the key risk factor for pilot risk.
(2) Diagnosis inference for aircraft factors

Table 5 illustrates the probability of casual risk factors under the assumption that aircraft risk occurs. The posterior probabilities of the third-level indicators of aircraft increase fast and the change rates of mechanical failure(U21) and performance defect (U22) ranked in front, which means they become the main risk factors.
(3) Diagnosis inference for environmental factors

The diagnosis inference result for environmental factors is shown in Table 6. When the environmental risk appears, the change rates of probabilities are more than $100 \%$, which illustrates that all risk factors affect the environmental risk significantly and that visibility (U34) is the key factor.
(4) Diagnosis inference for management factors

The probability distribution of risk factors causing management risk is presented in Table 7. When management risk exists, the change rate of improper emergency disposal (U45) reaches the top ranking of $724.35 \%$, which means it is the most important risk factor for management risk.

Table 3. Probability distribution of the nodes.


Table 4. Diagnosis inference result for pilot factors.


Table 5. Diagnosis inference result for aircraft factors.


Table 6. Diagnosis inference result for environmental factors.


Table 7. Diagnosis inference result for management factors.


# 4.2. Sensitivity Analysis 

In this section the BN model is applied to identify the most important risk factors causing a seaplane accident. The sensitivity value of the node $U_{i}$ to the node $U$ (top event) is calculated as follows:

$$
\begin{aligned}
\text { Sensitivity value } \\
& =|P\left(U=\text { state } i \mid U_{i}=y e s\right) \\
& -P\left(U=\text { state } i \mid U_{i}=n o\right) \mid
\end{aligned}
$$

Given that no uniform criteria areused to judge the change in percentage caused by each risk factor, the change in percentage is judged subjectively in relation to other risk factors. The judgment results are highly relevant to decision makers. However, by selecting relatively more important risk factors, decision makers can develop efficient measures to prevent accidents [46].

In the first scenario, the influence of various risk factors on seaplane operation safety can be determined through sensitivity analysis, as shown in Figure 5. The sensitivity values of pilot (U1), aircraft (U2), and management (U4) are larger than that of environment (U3) in minor accidents. Risk factors such as mechanical failure (U22), aircraft performance defect (U21), pilot's mental barrier (U15), improper emergency disposal (U45), operation command error (U44), and visibility (U33) are also sensitive to minor accidents. Aircraft (U2) and environment (U3), including mechanical fault (U22), visibility (U33), and aircraft performance defect (U21), are more sensitive to substantial accidents. Pilot (U1), management (U4), and aircraft (U2) factors are more sensitive to destroyed accidents compared with environmental (U3) factors, and the sensitivity value of mental barrier (U15), mechanical failure (U22), improper emergency disposal (U45), and performance defect (U21) are highlighted. The results of sensitivity analysis verify the diagnosis inference results to some extent, though large differences appear between sensitivity analysis and diagnosis inference for the risk factors of minor accidents.

![img-4.jpeg](img-4.jpeg)
(a) The sensitivity of $U$ (state $=$ "minor").(b) the sensitivity of $U$ (state $=$ "substantial").
![img-5.jpeg](img-5.jpeg)
(c) The sensitivity of $U$ (state $=$ "destroyed").

Figure 5. Result of risk factor sensitivity analysis.

# (1) Sensitivity analysis for pilot factors 

Sensitivity analysis for pilot factors shows that the sensitivity value of mental barrier ranks first at 0.47 , followed by handling error at 0.33 and illegal operation at 0.27 . The sensitivity value of low flight experience is 0.2 , which is close to that of skill assessment failure at 0.19 . The result is consistent with the diagnosis inference, which demonstrates the key risk factors of the pilot.

## (2) Sensitivity analysis for aircraft factors

The sensitivity analysis result indicates that mechanical failure is the most sensitive factor among aircraft factors, with a sensitivity value of 0.65 . The next sensitivityfactors are performance defect at 0.52 and weight imbalance at 0.36 . The sensitivity of maintenance error is weak at 0.33 .

## (3) Sensitivity analysis for environmental factors

The results illustrate that visibility has the highest sensitivity at 0.51 , followed by the complexity of the landing field environment at 0.45 . The sensitivity values of wind/oblique flow threat and wind/swell threat are 0.33 and 0.30 , respectively.

## (4) Sensitivity analysis for management factors

The sensitivity analysis result shows that improper emergency disposal reaches a maximum of 0.51 , followed by operation command at 0.46 . The sensitivity values of communication distortion and management failure are 0.31 and 0.27 , respectively, and system loss has the minimum sensitivity at 0.18 .

## 5. Discussion

The Bayesian network (BN) approach is adopted in this paper to evaluate the safety risk of the seaplane operation process. Before the construction of the BN model, the main risk factors causing seaplane accidents are identified and screened fromhistorical data, literature review, interviews with experts, and the Delphi method. An indicator system with 4 second-level indicators and 18 third-level indicators is obtained, which helps build the structure of the BN model. The parameters of the BN model are determined by expert experience and parameter learning from 87 accident cases. An out-of-sample validation test by 23 accident cases shows that the BN model is able to predict the accident severity level with $95 \%$ accuracy. Then the validated BN model is applied to conduct diagnosis inference and sensitivity analysis for various scenarios. It is found that the four most critical risk factors of seaplane operation are mental barrier, mechanical failure, visibility, and improper emergency disposal.

The identified risk factors causing seaplane accidents are classified into four categories: pilot, aircraft, environment, and management. The classification approach (the SHEL model) is common in the research field of seaplane safety or the broader general aviation safety. However, this research has identified some risk factors which are not covered by previous research [2,8,10]. The risk factors illegal operation (U13) identified by historical data and operation command error (U44) identified by interviews with experts are included in the BN network. According to the results of diagnosis inference (Table 3) and sensitivity analysis (Figure 5), they have an intermediate impact on the seaplane accidents in relation tothe other risk factors, which means they should not be ignored. The risk factors identified in this paper could be used by the community of seaplane/general aviation risk analysis research as a reference.

The prior probability tables (PPT) and the conditional probability tables (CPT) are obtained by both expert experience and parameter learning in this paper. Expert opinions are valuable in determining these probabilistic parameters as they provide practical prior knowledge, which is used by previous work [10] to construct their BN models of seaplane risk assessment. Parameter learning from case data is preferred by risk assessment research in other fields [49], which is also a popular approach to construct a BN model. However, seaplane accident data are not organized well for risk assessment.

We collected and analyzed 110 accident reports in detail for this research. For parameter learning, 87 accident cases were used, and 23 cases for the validation test. We believe the BN network constructed with both expert opinions and accident data could provide more practical risk analysis results.

Based on the BN model, diagnosis inference and sensitivity analysis are carried out to identify the most critical risk factors. By diagnosis inference, it is found that in minor and substantial accidents, aircraft and environment are the key factors leading to accidents, whereas in destroyed accidents, pilot and management are the main risk factors for seaplane accidents, which is consistent with practice. For pilot factors, mental barrier and handling error are the main risk factors; mechanical failure and performance defect play important roles in aircraft risk; environmental complexity of the take-off and landing field and visibility are the main environmental factors; and improper emergency disposal and operational command error are the key factors in management risk. By sensitivity analysis, the key factors affecting the seaplane safety risk. The parameter variation in the analysis is the variation of the occurrence probability of risk factors from $0 \%$ (state $=$ "no") to $100 \%$ (state $=$ "yes"), and we observe how this variation affects the occurrence probability of an accident. The four risk factors which influence the accident the most are mental barrier, mechanical failure, visibility, and improper emergency disposal. These results can be useful for seaplane operators to take targeted and effective measures to improve seaplane operation safety.

# 6. Conclusions 

This paper proposes a novel risk assessment approach for seaplane operation safety using Bayesian network (BN). The BN model is constructed according to historical accident data and experts in the seaplane field. It is validated by predicting the severity level of actual accidents with $95 \%$ accuracy. Diagnosis inference and sensitivity analysis are performed to find key risk factors in particular scenarios for decision making purposes. The result shows that the four most critical risk factors are mental barrier, mechanical failure, visibility, and improper emergency disposal. It provides an early warning to take appropriate preventive and mitigative measures to enhance the overall safety of seaplane operation process.

The future directions of this research are as follows. Firstly, the structure of the BN model could be improved to better reflect the casual relationships of nodes by structure learning from much more accident data. Secondly, other safety analysis methods such as system dynamics could be combined with BN to study the relationships among risk factors. Finally, the BN model will be applied to more practical scenarios for validation and modification.

Author Contributions: "conceptualization, Q.X. and F.L.; methodology, Q.X.; software, Q.X.; validation, Q.X., F.L. and Y.L.; formal analysis, Q.X.; investigation, Q.X. and F.L.; resources, F.L..; data curation, Q.X.; writing-original draft preparation, Q.X.; writing-review and editing, Y.L.; visualization, Y.L.; supervision, F.L.; project administration, F.L.; funding acquisition, F.L." All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by National Natural Science Foundation of China, grant number 71271163, and Humanities and Social Sciences Fund of the Ministry of Education of China, grant number 18YJA630076.
Acknowledgments: Great gratitude is extended to the experts for their opinion on the risk identification, index screening and BN building.
Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to publish the results.

# Appendix A 

## 1. The Description of Risk Factors

Table A1. Risk factors for seaplane operation safety.


# 2. Risk Factors of the Operation Process 

![img-6.jpeg](img-6.jpeg)

Figure A1. Risk factors of the operation process.
