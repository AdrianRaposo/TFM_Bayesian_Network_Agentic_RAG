# FALL RISK ASSESSMENT OF BRIDGE CONSTRUCTION USING BAYESIAN NETWORK TRANSFERRING FROM FAULT TREE ANALYSIS 

Tung-Tsan CHEN, Chih-Hui WANG<br>Department of Civil Engineering and Engineering Management, National Quemoy University, No. 1 University Rd., Kinmen County, 892, Taiwan (R.O.C.)

Received 24 Nov 2014; accepted 09 Apr 2015


#### Abstract

Falling is the most common one during bridge construction. Current safety management on site mainly relies on checklist assessment. Yet the assessment result is often influenced by the ability and experience of the evaluator, thus is not impossible to achieve consistent and systematic assessment objective. Moreover, most critical factors that can prevent occurrence of accidents cannot be found from existing safety management and assessment method. This paper built a Bayesian Network (BN) model by converting Fault Tree to assess the fall risk of bridge construction projects. We analyse falling factors and their relationships in Bayesian Network, and collect prior probability event and calculate the probability for the entire model. Using the model to analyse and validate with the current bridge projects under construction, the results from Bayesian Network is consistent with that from conventional labour safety performance assessment. Therefore, the ability to manage site safety of the model is proven to be useful.


Keywords: Bayesian network, fault tree analysis, bridge construction, fall risk, site safety, risk assessment.

## Introduction

Construction industry plays an important role in major national projects. Site safety of construction industry and national development are closely correlated. Transportation, which is highly related to civic life, living environment and quality, plays an important role and is one of the major indexes of national development. A complete transportation network enhances social benefits, saves time and promotes convenience. Whether it is high speed rail or highway system, all transportation system relies heavily on the application of bridges.

As modern technologies grow, various new bridge construction methods are developed. However, the new constructed bridges are splendid in appearance and shape but complicated in structure and construction. If the design is not appropriate or is poor in quality, extra cost and even site casualty might be induced.

Based on the above-mentioned problems, it is imperative first to reduce the occupational accidents by finding the defects encountered during existing bridge construction. Then find their correlations and analyse the probability of occupational injuries and casualties to further propose counter measurements for bridge constructors.

The research analysed the past ten year's data from the Construction Knowledge Platform of Major Occupational Injuries \& Casualties and found that falling is the most profound accident which leads to death. Therefore,
falling in bridge construction is the major topic of this research. Our goal is to seek new and effective ways to prevent fall accidents during construction.

## 1. Literature review

This research adopts the deduction logic of Fault Tree to judge the event causes and the relationships among different factors leading to falling. Bayesian Network is applied to cope with the problem of insufficient data and calculate values of probability. Therefore, literature reviews are focused on Fault Tree, Bayesian Network, Fall Tree conversion to Bayesian Network and Bridge Construction.

Fault Tree Analysis (FTA) is a technique that can effectively analyse the cause and effect relationship and probability of an event. However, some factors are fuzzy, riddled with human errors, their occurrence probability is hard to assess accurately.

In the following, examples of Fault Tree Applications are shown. Rodak and Sillima (2012) Fault trees (FT) integrated with probabilistic risk analysis (PRA) was applied on the management of underground water resources. Durga Rao et al. (2009) applied traditional Fault Trees analysis on complicated engineering systems to assess their reliability and safety. A defined gate is added into the definition of Dynamic Fault Trees to simu-

late the complicated interactions. Lai (2009) used Fuzzy Fault Tree Analysis to analyze the deteriorating factors of the bridge abutment. Zhang et al. (2014a) present a Fuzzy fault tree analysis probabilistic decision approach for safety risk analysis for metro construction in complex project environments.

Several scholars use Bayesian Network (BN) on educational tests, such as Almond et al. (2002) and Mislevy et al. (2003). The proposed Evidence-Centered Design (ECD) Assessment Design is based on the framework of BN as the diagnosis and analytical tool. The analysis is conducted through technical analysis of BN probability model combining with Test Reaction Theory Parameters Model to understand the feasibility of BN application on TASA.

Construction industry encountered several uncertainty and risk on safety. Historical data are at times insufficient, which means the probabilities are incorrectly acquired. Yang (2008) used Bayesian Network to combine experts' objective opinions, which in turn is used to deduct the Probability value of BN. Yang's research enables BN to be analysed by more reliable probabilities in the later research.

## 2. Statistics of Taiwan construction occupational accidents

According to the occupational accident records from Ministry of Labour in Taiwan, The occupational accident rate in the construction industry is relative high, as shown in Figure 1. After examining 88 accident cases for bridge engineering in the past 10 years from Ministry of Labour in Taiwan, we found that there are 97 casualties, 66 serious injuries and 5 minor injuries. Among the reported accidents, the most frequent occurring accident types are
the falling and rolling off (Table 1). Most of the accident causes might be environmental constraints, unsafe behaviour of labour, human misconducts, obsolete equipment, lack of expenses, rushing schedule, and etc. Among the reasons listed above, some safety procedures are not strictly complied because of scheduling difficulties, this might cause accidents such as supports of form work collapse, falling of concrete mass when RC is grounding, or dismantling of supporting frames. The above-mentioned reasons usually cause major accidents that result in casualties, serious injuries, huge loss in machinery and materials, progress delay, and etc.

## 3. Methodology and research process

This research first uses fault tree analysis (FTA) to analyse the falling/rolling off from bridge construction and related operations of occupational accidents; Bayesian Network (BN) is then applied to calculate the probabilities of the related operations of occupational accidents. Building a BN is rather complicated because there are often problems with its network structure. Therefore, first a FTA system is built; afterwards, it is converting into BN framework. Experts' experiences are then integrated into BN nodes and expressed by conditional probability table (CPT). The proposed conversion process of FTA and BN is depicted in detail in Figure 2 and in following passages.

### 3.1. Fault Tree Analysis (FTA)

Fault Tree Analysis (FTA) first assesses one undesirable event as the top event. A top-down approach is adopted to construct FTA. Starting from top event to the causes until the fundamental causes are found, the relationships among events and causes are expressed by "AND" and
![img-0.jpeg](img-0.jpeg)

Fig. 1. Fatalities persons in construction industry and all industries (excluding deaths from occupational disease and traffic accidents), 2001-2010

Table 1. Type of bridge project under structure occupational accident


![img-1.jpeg](img-1.jpeg)

Fig. 2. Transformation flow chart from FT to BN
"OR" logic gates (Bobbio et al. 1999, 2001; Xiao et al. 2008; Boudali, Dugan 2005; Bearfield, Marsh 2007; Qian et al. 2005; Franke et al. 2009). FTA is a qualitative and quantitative analysis of the drawbacks and weak points of a system, therefore FTA can be comprehensively applied on the reliability and safety tests and fault diagnosis decision model (Ebeling 1997; Rao 1992; O’Connor, Kleyner 2002; Kales 2006). Through logic deduction, FTA is able to give insight the improvement and maintenance of a system design. The events of the traditional FTA approach are assumed to be statistically independent, and the state of each event binary-failure or normal.

### 3.2. Bayesian Network (BN)

Combining theory of probability and graphic theory, Bayesian Network (BN) includes node, links and conditional probability tables, (CPTs) between nodes. BN is a graphic probability model in which a set of random parameters, the associated relationships are expressed by a directed acyclic graphical model.

BN has higher efficiency and deduction accuracy under uncertainty. It is particular suitable for complicated systems and highly correlated elements (Qian et al. 2005; Bobbio et al. 1999; Xiao et al. 2008). In recent years, BN is widely applied in areas with high uncertainty or inter-correlation such as diseases diagnosis, industrial design, financial investment, ecology, machine failure, files filtering, factory planning and construction industry, etc. (Qian et al. 2005; Bobbio et al. 1999; Xiao et al. 2008; Zhang et al. 2013, 2014b; Holicky et al. 2013; Khakzad et al. 2014).

As stated above, there are 3 sources to build a BN: (1) vast amount of training data; (2) experiences of area experts; and (3) a mixed of (1) \& (2). Because of the constraints on data usability, the second method is usually used for practical BN building. Despite of this, it is difficult to build the correlated relationships of nodes in a network by merely relying on the knowledge of engineers and experts. Therefore, several processes that convert Fault Tree to Bayesian Network are proposed (Bob-
bio et al. 1999, 2001; Xiao et al. 2008; Boudali, Dugan 2005; Bearfield, Marsh 2007; Qian et al. 2005; Franke et al. 2009; Chen, Leu 2014). Normally, the conversion of an FT to a BN follows a one to one relationship; in other words, the logic gates of FT are converted to corresponding physical nodes of BN. Nevertheless, the definition of a BN node and a logic gate of a FT are not completely identical. An event node of a BN expresses a variable of a problem domain, while a logic gate of a FT describes the logical relationship between nodes. With respect to conversion of FT and BN, event nodes and logic gates should be processed separately. In the process of logic gate conversion, conditional probability table (CPT) in BN is essentially the same as logic gate in FT, and the conditions may not always be binary.

### 3.3. Converting Fault Tree to Bayesian Network

The proposed conversion process is divided into two parts, structure conversion and calculation of CPT. The fundamental steps of structure conversion include: (1) direct conversion from events in Fault Tree and vertical connections to nodes and basic links in Bayesian Network (excluding logic gates); and (2) Insert supplementary links through knowledge of experts and engineers. Moreover, the calculation of CPT is conducted based on the logic gates of nodes. Each step is illustrated in details in the sections below.

### 3.3.1. Structure conversion

The proposed method to convert FT to BN is based on previous applied technique (Qian et al. 2005; Fenton, Neil 2004; Boudali, Dugan 2005; Ebeling 1997; Bobbio et al. 1999; Xiao et al. 2008). Top event, middle event and basic event of a Fault Tree reflect to the nodes of Bayesian Network. The basic arrows between nodes of BN are defined according to the events relationships of FT. Furthermore, some supplementary links with means are inserted into BN framework based on expert opinions. In summary, the process of converting FT into BN is depicted as follows:

1) All FT events (including fundamental events) are expressed as nodes in BN. Repeated FT events are eliminated, which are only represented by a single BN node.
2) The relationships of links and nodes of BN are defined by the relationships of FT events.
3) If there are meaningful relationships within a BN structure, but are not well defined in a FT, arrows should be inserted into the fundamental BN to express the interactive relationships of nodes in a clear manner.

### 3.3.2. Calculation of Conditional Probability Table (CPT)

If a node has multiple parent nodes or multiple states, then the structure of the CPT become rather complicated. For example, a node and two parent nodes with these five states to each node would mean that the number of CPT

will expand to $5^{3}$ (125). Besides, value of CPT is normally defined by the experiences of experts, which might not be consistent, especially in the above mentioned complicated states of CPT. AgenaRisk software is used to deal with the above mentioned difficulties in the research process (Agena 2008). Through parameter definition in the software and the weight of nodes set by the experts, the probability value in the CPT can be calculated promptly.

When using AgenaRisk to define the CPT, it is important to express function definitions in the software. There are two major logic gates, "AND" \& "OR", they are defined as follows.

In expressing events, if the corresponding logic gate of FT is "AND", the smallest is chosen; if the corresponding logic gate of FT is "OR", the biggest is chosen. Through deduction and the consistency of Fault Tree analysis and Bayesian Network, the failure probability of the top event can be proved. In other word, assume that there are two independent events A and B. Their top event is C. There are two states for event A, B, and C: A1, B1 and C1 are normal, A2, B2 and C2 are failure respectively.

Based on the assumption of independent event and "AND" logic gate of FT, the failure probability can be calculated as follows:

$$
P\left(C_{2}\right)=P\left(A_{2} \cap B_{2}\right)=P\left(A_{2}\right) \times P\left(B_{2}\right)
$$

Use concept of BN, the failure probability can be calculated as:

$$
\begin{gathered}
P\left(\mathrm{C}_{2}\right)=\mathrm{C}_{2} A_{1} B_{1} \times A_{1} \times B_{1}+\mathrm{C}_{2} A_{1} B_{2} \times A_{1} \times B_{2}+ \\
\mathrm{C}_{2} A_{2} B_{1} \times A_{2} \times B_{1}+\mathrm{C}_{2} A_{2} B_{2} \times A_{2} \times B_{2}= \\
0 \times A_{1} \times B_{1}+0 \times A_{1} \times B_{2}+0 \times A_{2} \times B_{1}+1 \times A_{2} \times B_{2}= \\
P\left(\mathrm{~A}_{2}\right) \times P\left(B_{2}\right)
\end{gathered}
$$

According to the assumption of independent event and "OR" logic gate, the failure probability can be defined as follows:

$$
\begin{gathered}
P\left(C_{2}\right)=P\left(A_{2} \cup B_{2}\right)=P\left(A_{2}\right)+P\left(B_{2}\right)-P\left(A_{2} \cap B_{2}\right)= \\
1-\left[\left(1-P\left(A_{2}\right)\right) \times\left(1-P\left(B_{2}\right)\right)\right]=1-P\left(A_{1}\right) \times P\left(B_{1}\right)
\end{gathered}
$$

According to the concept of BN, the failure probability can be deducted as:

$$
\begin{gathered}
P\left(\mathrm{C}_{2}\right)=\mathrm{C}_{2} A_{1} B_{1} \times A_{1} \times B_{1}+\mathrm{C}_{2} A_{1} B_{2} \times A_{1} \times B_{2}+ \\
\mathrm{C}_{2} A_{2} B_{1} \times A_{2} \times B_{1}+\mathrm{C}_{2} A_{2} B_{2} \times A_{2} \times B_{2}= \\
0 \times A_{1} \times B_{1}+1 \times A_{1} \times B_{2}+1 \times A_{2} \times B_{1}+1 \times A_{2} \times B_{2}= \\
A_{1} \times B_{2}+A_{2} \times B_{1}+A_{2} \times B_{2}= \\
1-P\left(\mathrm{~A}_{1}\right) \times P\left(B_{1}\right)
\end{gathered}
$$

In the comparison between Eqns (3) and (4), we found that the top event probability of FTA and BN are the same. In AgenaRisk software, the selection of expressing function is in accordance with the logic gate of

FT. The weights, which are the comprehensive opinions from experts on the contributions from parent nodes to child nodes, are inputted afterwards.

The weight ranges from 1 to 5 . A 1 represents the least influential of a parent node to child node while a 5 represents the most influential. Once the above mentioned data are inputted into AgenaRisk, all CPT in BN can be calculated promptly. Moreover, probabilities of the top event and all middle nodes can be deducted by AgenaRisk.

## 4. Bayesian Network risk assessment on falling of bridge project

From the proposed BN building process, a risk assessment model on falling in bridge project based on BN is developed. For knowledge supports and model building, in this research we have invited 36 experts to assess 97 questions based on their professional practical experiences. In order to validate the model, 4 bridge construction projects using advancing shoring method were selected. The causes that sensitively influenced falling risk are then assessed. Through sensitivity analysis and discussions, the detail model development is described as follows.

### 4.1. Constructing Fault Tree framework

Because falling represents the most frequent occupational accident in bridge construction projects, it is selected as the top event in the fault tree in the research. Under the safety management domino theory (Heinrich et al. 1980), the causes of work falling accidents can be categorized as accident location and accident condition (such as steel frame support work, bridge deck structure and hoisting operation etc.) and their details, indirect causes and their details (such as unsafe behaviours, unsafe equipment and unsafe environments etc.) and fundamental causes (such as inappropriate safety plan, inappropriate environment maintaining, insufficient safety training and poor safety management etc.) Theses causes and top event are connected by the logic gates as shown in Figure 3.

Take falling accident of poor steel support operation as example. Through expert interview and literature review, the related operations of the steel support operation can provide more information to enable a more detail analysis on the falling accident event. There are 2 operations that might cause possible falling: (1) Poor support assembly or inappropriate movement and (2) Inappropriate dismantling of steel supports. If required, the operation can be further decomposed into more detailed suboperations. These indirect causes could then be analysed.

According to the domino theory and safety management concept (Jitwasinkul, Hadikusumo 2011; Lingard, Rowlinson 2005), the four basic reasons that cause occupational accident are: insufficient safety training; poor site environment management; poor safety and health management; and inappropriate health and safety planning. Based on the records of occupational accident, safety theory and expert interview, the research confirms the

![img-2.jpeg](img-2.jpeg)

Fig. 3. Overall FT of falling accidents of bridge construction projects
interactions of the fundamental factors and indirect causes in order to construct a whole fault tree. The completed fault tree of bridge construction project falling event is shown in Figure 3. Their codes and definitions are summarized in Table 2.

### 4.2. Converting from Fault Tree to Bayesian Network

Based on the conversion process shown in Section 4, a Fault Tree diagram is first converted to Bayesian Network, where the overlapped nodes are merged into one. Afterwards, several meaningful supplementary links are added in the BN according to the data of expert experience. A complete Bayesian Network is shown in Figure 4. Further analysis and explanation is as follows.

### 4.3. Calculation of CPT

When a BN structure is assembled, AgenaRisk can be used to calculate the conditional probabilities. The types for expressing functions are maximum risk value and the minimum risk value defined according to fault tree logic gate. Furthermore, questionnaire is designed to collect the relative weight of related parent node and child node. Examples of questionnaire items are shown in Table 3. 36 experts are invited to assess 97 questions based on
![img-3.jpeg](img-3.jpeg)

Fig. 4. BN of falling accidents at bridge construction projects

Table 2. Codes and definition of overall FT of falling accidents


Table 3. Questionnaire example of relative weights of BN arcs


Table 3. Questionnaire example of relative weights of BN arcs (Continued)


Note: x is 5-0; 5 represents the greatest influence; 0 is minimal influence.
their practical experiences. A statistical analysis is conducted based on their replies. Through these input the conditional probabilities in BN could be calculated. Then, the complete BN model could be assembled by further analysing the probabilities of fundamental causes. Lastly, after probabilities of all BN nodes are deducted, the value of failure occurrence probability can be found.

### 4.4. Assessment of prior probability

As stated above, there are four fundamental causes defined in the model, insufficient safety training, poor site safety management, poor safety and health management and inappropriate safety and health planning. In order to confirm the prior probability of these causes, a safety measure of performance shown in Table 4; the table shows several important items on safety performance. Every fundamental cause is listed in the table for further analysis. Through input of prior probability in the BN, the probability of fall risk in bridge construction project can be calculated and understood.

## 5. Model validation and sensibility analysis

The deducted result of BN is validated by the actual safety check records of four bridge construction projects in Taiwan. Sensibility analysis is conducted further to confirm the critical causes falling accidents of the bridge construction project. The result of the sensibility analysis could be an important reference to future diagnosis and safety prevention strategy.

### 5.1. Model validation

The proposed Bayesian Network is validated from actual safety records of four bridge construction projects and the results of posterior probability of top event of Bayesian Network. The basic information of the four bridge construction projects is shown as Table 5 and of which the actual safety check record is concluded on Table 6.

In the research process, the safety performance of every project is evaluated with the safety performance evaluation table. The prior probabilities of the four fundamental causes are objectively evaluated and inputted into AgenaRisk to deduct the posterior probabilities of the BN nodes. The comparisons of the BN model analysis result and the actual safety records are shown in Table 6. The
findings of the results show that the ranking of the probabilities deducted from BN model is consistent with that of the actual safety records.

A survey was conducted to scrutinize the monthly safety check records of the four bridge construction projects. The $1^{\text {st }}$ project is an excellent project with excellent site safety management, no poor record on safety performance, such as fine. On the contrary, the project with the lowest rank is riddled with safety mismanagement. Its fall risk deducted from BN model is as high as $81.264 \%$. Through practical evaluation and validation on the four bridge construction projects, the result validates the accuracy and adaptability of the proposed falling risk assessment BN model and proves that the proposed model can be used as a fall risk assessment tool in bridge construction project applied with advanced shoring method.

### 5.2. Sensitivity analysis and discussion

Further considering the key causes that affecting occurrence of falling, sensitivity analysis is conducted and concluded the key causes on Table 7.

In general, the most important direct causes are highly elevated bridge construction environment, vast amount of steel supports that increase the operation risk, incorrect use of safety belts and rings, disregard for safety equipment, limited supply of safety equipment, limited equipment for platform which meet standard, and etc. Due to the above-mentioned causes, fall accidents in bridge construction could easily take place without proper supervision. As shown on Figure 5, occupational accidents statistics in bridge construction shows that not taking safety measurement or ignoring warning, with a $62 \%$ chance, are the major causes to bridge construction occupational accident (MOL 2013).

The most sensitive indirect causes are disobeying work rules, failing to implement self-management, disregard of wearing personal protection equipment, incorrect use of safety belt, inappropriate work environment etc. These explain that labour is working under inappropriate protection condition, which can easily lead to construction accidents. Based on the statistics of bridge construction (occupational accidents) approximately half of the occupational accidents during bridge construction are caused by inappropriate personal protection measurement as shown on Figure 6 (MOL 2013). Finally, the most im-

Table 4. Checklist of construction safety performances
Project:
Date of inspection:


Table 5. Basic information of four advanced shoring bridge construction projects


Table 6. Comparison between BN and real site assessment


Table 7. Comparison of sensitive factors from BN and actual statistics

(B7) Failure to comply with code of practice
(C4) No use of safety belt and rings
(B12) No use of safety device
(D4) Improper removal of the main truss
(B14) No use of personal protective equipment
(C11) Safety belt not used properly
(C5) Improper Environmental Operating of strong winds
(G2) Poor bridge deck construction | Middle
High
Middle
High
High
Middle
Middle
Low
Low | (A4) Poor H/S management | High  |

![img-6.jpeg](img-6.jpeg)

Fig. 5. Unsafe behaviors of occupational accidents of bridge construction projects

![img-7.jpeg](img-7.jpeg)

Fig. 6. Unsafe conditions of occupational accidents of bridge construction projects

portant factors are the fundamental management of labour safety and hygiene education and training, which play vital roles in preventing and reducing falling accident in bridge construction projects.

To sum up, this model does not only assess the risk of falling accident of bridge construction site, but also confirm the major sensitive factors through sensitivity analysis. According to the above mentioned analysis, project manager may prepare safety prevention measures to reduce occurrence of falling accidents in bridge construction project site. In addition, falling risk assessment and sensitivity analysis enable us to allocate resources on key labour safety operations and thus substantially reduce the risk of falling accidents.

## Conclusions and future development

This paper establishes an effective process to build a falling risk assessment model based on Bayesian Network in bridge construction projects that use advanced shoring method. The assessment begins with the forming of fault tree, then converting it to a Bayesian Network. In addition, meaningful links between nodes are inserted into BN according to input from experts to complete the structure of BN. Finally, a logic converting method is developed to convert the logic gates of fault tree to the CPT of BN. A safety performance check table is constructed to objectively assess the prior probability of fundamental causes. The result in this study is validated by four bridge construction projects in Taiwan.

Through analysis and comparison, it is found that the result from BN analysis is consistent with the safety records of the 4 bridge construction projects. This implies that the converting process from multi states fault tree to Bayesian Network can effectively construct a real and accurate falling accident risk assessment model. Therefore, according to the assessment model and sensitivity analysis, site manager can decide the safety prevention measures and allocate resources in advance to reduce the fall risk on site. Despite good validation on converting FT to BN, expert input is still required on links of nodes and CPT in using the BN model.

Data provided by different experts will directly influence the accuracy and assessment quality of BN. Emphasis should be imposed on expert input in the future research. Besides, BN can learn from raw data. If a complete safety data set is present, a subjective BN model and parameters could be built. In addition, other occupational accidents in bridge construction projects such as collapsing, electricity shocks, hitting by falling objects etc. might be applied with BN extensively to cover comprehensive safety diagnosis, enhancing safety management and reducing site occupational hazards in bridge construction projects.
