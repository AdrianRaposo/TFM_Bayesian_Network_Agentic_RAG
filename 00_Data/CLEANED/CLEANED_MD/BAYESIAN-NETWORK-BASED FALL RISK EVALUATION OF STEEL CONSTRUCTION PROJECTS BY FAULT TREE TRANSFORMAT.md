# BAYESIAN-NETWORK-BASED FALL RISK EVALUATION OF STEEL CONSTRUCTION PROJECTS BY FAULT TREE TRANSFORMATION 

Sou-Sen LEU, Ching-Miao CHANG<br>National Taiwan University of Science and Technology, 43 Keelung Road, Section 4, Taipei 106, Taiwan

Received 05 Mar 2012; accepted 16 Nov 2012


#### Abstract

A fall (also referred to as a tumble) is the most common type of accident at steel construction (SC) sites. To reduce the risk of falls, current site safety management relies mainly on checklist evaluations. However, current onsite inspection is conducted under passive supervision, which fails to provide early warning to occupational accidents. To overcome the limitations of the traditional approach, this paper presents the development of a fall risk assessment model for SC projects by establishing a Bayesian network (BN) based on fault tree (FT) transformation. The model can enhance site safety management through an improved understanding of the probability of fall risks obtained from the analysis of the causes of falls and their relationships in the BN. In practice, based on the analysis of fall risks and safety factors, proper preventive safety management strategies can be established to reduce the occurrences of fall accidents at SC sites.


Keywords: Bayesian network, fault tree, steel construction, fall risks.

## Introduction

Steel structures are commonly used in high-rise buildings. However, falls are the most frequent occupational accidents at steel construction (SC) project sites because of work at height. In Taiwan, the percentage of fall accidents at SC project sites rose to $67 \%$ over the past decade (2000-2010). Fall accidents at SC sites occur frequently because of unqualified safety equipment and unsafe worker behavior, particularly for steel member-lifting work. Construction companies implement every possible safety measure to prevent occupational accidents. The current method for implementing on-site safety management is to conduct regular safety inspections using a checklist of unsafe equipment and unsafe worker behaviors. However, current on-site inspection is conducted under passive supervision, which fails to provide early warning regarding occupational accidents. Several effective approaches have recently been developed to define the relationship among safety variables so that preventive safety measures could be proposed. Structural equation models (SEM) and BNs are typical examples of these approaches (Kao et al. 2009; Martin et al. 2008; Paul, Maiti 2007).

BNs can be used to identify the most important causes of site accidents and determine the relationships among these causes to enable defining early and preventive safety measures. Because of the constraint of data availability, the construction of a practical BN is generally based on the experiences of domain experts. However, it
is difficult to establish mutual relationship among nodes in the network by directly incorporating the views of experts. It may be more effective to build BN through FT transformation (Franke et al. 2009; Xiao et al. 2008).

The remainder of this paper is organized as follows: Section 1 reviews state of art on safety risk assessment methods and BNs; Section 2 provides descriptions of the basic concepts of FTs and BNs, as well as the BN development process. A multi-state FT provided the fundamental frameworks to develop the BN through FT transformation. Section 3 introduces the development of a BN-based fall risk assessment model for SC building projects. Section 4 details the validation of the model against six SC building projects; and lastly, conclusions are provided.

## 1. Literature survey

Several risk assessment methods have been used for safety risk assessment at construction sites, such as fault tree analysis (FTA), failure mode and effect criticality analysis (FMECA), and the decision tree (Hartford, Baecher 2004; Kales 2006). Basic probabilities and Boolean operations are used in FTA algorithms. To simplify FT operations using Boolean logic, events in an FT are generally assumed to be mutually independent. However, a number of safety factors (such as the interaction between unsafe behaviors and unsafe environments and their effect on accidents) can be highly coupled. Such mutual dependencies are not effectively addressed by classical approaches.

To overcome the constraint of classical safety assessment, in recent years, BNs have become popular tools for safety risk assessments based on uncertain causal relationships between multidimensional parameters. Martin et al. (2008) used a BN to analyze workplace accidents caused by falls from considerable heights. Bedford and Gelder (2003) assessed the safety of third parties during construction in multiple spaces using BNs. Matias et al. (2007) indicated that, in addition to their excellent predictive capacity, BNs have a satisfactory interpretative capacity regarding workplace accidents.

In general, expert knowledge is used to develop BNs that describe problems with the causal relationships between nodes and their conditional probabilities. The direct construction of a BN is more applicable to simple problems; however, it is difficult to directly develop complex BNs. Some scholars have proposed several systematic approaches to BN construction through FT transformation. The main techniques make use of 「OR Gate」 and
「AND Gate」 logic and then transform into a BN to perform probabilistic analyses of event occurrences (Franke et al. 2009; Marsh, Bearfield 2007; Xiao et al. 2008). Several prior studies regarded events and logic gates in FT as nodes in BN; however, these two have differing definitions and purposes. Logic gates are used mostly to describe the relationship between events in a sequence; it is meaningless to convert logic gates into physical BN nodes. Therefore, we combined FTA and a BN to develop a more reasonable transformation process from FT to BN. A fall risk assessment model for SC projects was established based on the transformation procedures proposed in this study.

## 2. Methods and process

The construction of a BN can be complex, and its network structure is problem-specific. It is preferable to first construct a BN hierarchy by following the concept of FTA and subsequently transform basic FT into BN framework. Finally, meaningful supplementary links among BN nodes and a conditional probability table (CPT) can be introduced by incorporating expert experiences. FTA, BN , and the transformation processes are explained in detail in the following subsections.

### 2.1. Fault tree analysis (FTA)

FTA first identifies a particular undesired event as a top event. The construction of an FT proceeds in a top-down manner. It starts from the events and proceeds to their causes until the basic components are obtained. The relationships between events and causes are defined and represented using 「AND」 or 「OR」 logic gates (Franke et al. 2009; Graves et al. 2007; Xiao et al. 2008). Because FTA qualitatively or quantitatively analyzes the defects and weaknesses of a system, FTA is widely used for reliability and security testing and fault diagnoses in decision-making models (Lindhea et al. 2009; Kales 2006; O'Connor, Kleyner 2002).

The events of the conventional FTA methodology are regarded as statistically independent; however, this
may be unsuitable for real-world cases. A number of variables in complex problems are interrelated. Because FTA cannot demonstrate complex causal relationships, probabilistic network approaches (such as BNs) can be used to solve this problem.

### 2.2. Bayesian network (BN)

Combined with probability theory and graph theory, BNs consist of nodes, joints among nodes, and CPTs. A BN is a probabilistic graphical model that represents a set of random variables and their conditional dependencies through a directed acyclic graph. Over the past 25 years, BNs have emerged as a practically feasible form of knowledge representation. Compared to other learning models, BNs have several advantages: 1) transparent representation of causal relationships among variables from various sources (such as expert knowledge, empirical data, output from other models); 2) management of incomplete data sets; and 3) efficient updating when new knowledge or evidence is available. BNs have higher efficiency and accuracy in uncertain inferences, especially for complex systems with highly correlated elements, such as disease diagnosis assistance, industrial design, financial investment, ecology, failed machine system, file filtering, graphical interpretation, and factory planning under uncertain conditions (Doguc, Ramirez-Marquez 2009; Marquez et al. 2010; Stewart-Koster et al. 2010).

Three BN construction approaches are generally used: 1) learning from a large amount of training data; 2) based on the experience of domain experts; and 3) hybrid. The second approach is generally used for practical BN construction because of the constraint of data availability. However, it is generally difficult to establish mutual relationships among nodes in the network based only on the knowledge of engineers and experts. Therefore, several transformation processes from FT to BN have been proposed (Franke et al. 2009; Xiao et al. 2008). The classical transformation of logic gates from FT into BN is generally one-to-one; that is, logic gates in an FT are converted into corresponding physical nodes in the BN. However, the meanings of an event node in BN differ from those of a logic gate in an FT. An event node is used to represent a variable in the problem domain, whereas a logic gate is used to describe the logical relationship between nodes. For the transformation from FT to BN , the event nodes and the logic gates must be managed separately. In the transformation process of logic gates, the CPT in BN, which corresponds to logic gates, must be analyzed under two states or multiple states by using the probability values.

### 2.3. Conversion from FT to BN

The proposed conversion process was divided into two parts: framework conversion and CPT calculation. The basic steps for framework conversion are as follows: 1) direct transformation from the events and the vertical links in FT to the nodes and the fundamental links in BN (logic gates are excluded); and 2) insertion of supplementary links using knowledge of experts and engineers. Furthermore,

the CPT calculation was performed based on the logic gates among nodes. Each step is detailed as follows.

### 2.3.1. Framework conversion

The proposed method of conversion from FT to BN is a modification of techniques from previous studies (Franke et al. 2009; Xiao et al. 2008). In summary, the conversion process of BN structure from FT is shown in Figure 1. The top events, intermediate events, and basic events in the FT were directly mapped into the nodes in the BN. The overlapping nodes were combined into a single node. The arrows among the BN nodes follow the definition of event relationships in the FT. Furthermore, a number of supplementary arrows were inserted into the fundamental BN structure based on expert opinions.

### 2.3.2. CPT calculation

The CPT structure becomes complex when a node in a BN has several parent nodes, or when each parent node and child node has several states. In addition, the CPT values are generally defined by experts based on their experiences. The elicited probability values may be inconsistent, especially under a complex CPT condition. AgenaRisk (2012) software was used to alleviate these difficulties. The probability values in the CPT can be calculated quickly using the parameters defined in the software and the weights among nodes defined by experts.

The definition of the expression function in AgenaRisk (2012) is crucial to define CPTs. Two main logic gates in an FT (AND and OR) are defined as follows: in the selection of the expression function items, the minimum is selected if the corresponding logic gate in the FT is $\ulcorner$ AND $\lrcorner$, whereas the maximum is selected if the logic gate is $\ulcorner$ OR $\lrcorner$. Through deduction, the fault probabilities of the top event in FTA and the BN can be proven to be identical.

After the selection of the expression functions in AgenaRisk (2012) is defined based on the logic gates in the FT, the weights are determined and inputted through the opinion poll of experts based on the contribution of parent nodes to children nodes. The weight score ranged from 1 to 5 . A weight score of 1 indicates the lowest effect of one parent node on the child node, and a weight score of 5 indicates the highest effect. Once the data are
![img-0.jpeg](img-0.jpeg)

Fig. 1. Transformation flow chart from FT to BN
entered into AgenaRisk (2012), all CPTs in the BN can be quickly calculated. Furthermore, all posterior probabilities of the top event and all intermediate nodes in the BN can be inferred using AgenaRisk (2012).

## 3. BN-based fall risk evaluation of steel construction projects

A BN-based fall risk evaluation model for SC building projects was developed based on the proposed BN construction process. To obtain reliable knowledge and data, 22 specialists with an average of 18 years of work experience were interviewed for the construction of the model. Furthermore, the correctness of the model was validated against six steel building projects. Finally, the sensitive causes affecting fall risks were assessed and discussed using sensitivity analysis. The details of the model development are presented in the following subsection.

### 3.1. Construction of FT framework

Based on the domino theory of safety management (Jitwasinkul, Hadikusumo 2011; Lingard, Rowlinson 2005), the causes of fall accidents at SC projects can be classified into accident locations (such as beams, columns, and steel decks), indirect causes (such as unsafe behavior, unsafe equipment, and unsafe environments), and root causes (such as improper safety plans and poor safety management).

Falls can basically occur at three main locations (T): 1) steel beam construction areas (G1); 2) steel column construction areas (G2); and 3) deck construction areas (G3). Using steel beam erection as an example, the circumstances surrounding work tasks that can trigger a fall accident were analyzed in detail based on expert interviews and literature reviews. The three main tasks that can lead to a fall are as follows: 1) hoisting SC beams; 2) beam installation and permanent fixation; and 3) limb discordance in operation. If necessary, these tasks can be divided into detailed subtasks. Furthermore, the indirect causes that may trigger a fall accident during steel beam erection were sequentially analyzed.

Finally, the four root causes that result in occupational accidents are insufficient safety training, poor site environment management, improper health and safety planning, and inadequate safety and health management. Based on occupational accident records, safety theories, and expert interviews, the interaction of these root causes and the indirect causes was identified to form the overall FT. The completed FTs of falls at SC project sites are shown in Figures 2-4.

### 3.2. Construction of BN from FT and CPT calculations

Based on the transformation process described in Section 2, all FT diagrams were transformed to the BN. The complete BN framework is shown in Figure 5. AgenaRisk (2012) was used to calculate a CPT based on the constructed

![img-1.jpeg](img-1.jpeg)

Fig. 2. FT of falling accidents at beam erection of SC projects

![img-2.jpeg](img-2.jpeg)

Fig. 3. FT of falling accidents at column erection of SC projects

BN framework. Questionnaires were designed to collect information on the relative weights of parent nodes to their child nodes. In total, 22 experts were invited to assess 136 questions based on their practical experiences, and their answers were statistically analyzed. The CPTs for all arcs in the BN were calculated using the input data.

### 3.3. Assessment of prior probabilities

Four crucial root causes were defined in the model. A safety performance evaluation table was established to assess the prior probabilities of these causes. If more items are marked based on the site investigation, the higher probability of poor performance of the root cause would be subjectively evaluated. By inputting prior probabilities

![img-3.jpeg](img-3.jpeg)

Fig. 4. FT of falling accidents at deck installation of SC projects
into the BN, fall risks at SC building project sites and their significant causes can be identified using this model.

## 4. Model validation and sensitivity analysis

### 4.1. Model validation

The proposed BN model was validated using the results of actual safety inspection records of six SC building projects and the posterior probabilities of the top node in the BN. The basic information of these SC projects and a summary of their actual safety inspection records are shown in Table 1. Using the safety performance evaluation
tables, the prior probabilities of four root causes at the six projects were subjectively assessed and entered into AgenaRisk (2012) to determine the posterior probabilities of the nodes in the BN. Table 1 shows a comparison of the analytical results of the BN model with actual safety inspection records. A higher posterior probability indicates greater risk. However, a lower real assessment value indicates inferior site safety management. As shown in the table, the ranks of posterior probabilities from the BN model are highly consistent with those of safety performances obtained from the actual records. Only Projects 3 and 4 differed slightly.

![img-4.jpeg](img-4.jpeg)

Fig. 5. BN of falling accidents at steel construction projects

The error rate was further analyzed based on the standardized root mean square error (sRMSE), which is generally defined as $\sqrt{\sum_{i=1}^{n}\left(x_{1, i}^{2}-x_{2, i}^{2}\right) / n / \sigma}$ ( $\sigma$ : standard deviation). The assessed value ( 0.3381 ) was less than the threshold value (0.4) (Hengl et al. 2004). Moreover, the rank
result of BN analysis was statistically identical to that of actual safety records based on the Wilcoxon ranksum test. The actual appraisal and validation of these six SC projects showed that the proposed BN-based fall risk evaluation model is accurate and effective, and can be used as a tool for fall risk assessments of SC projects.

Table 1. Comparison between BN and real site assessment


### 4.2. Sensitivity analysis and discussions

Sensitivity analysis was conducted to further examine the main factors that affect the occurrence of falls at SC project sites. In BN sensitivity analysis, a single target node and one or more sensitivity nodes must be selected. Several sensitivity reports can be generated using AgenaRisk (2012), including sensitivity tables, tornado graphs, and receiver operating characteristic (ROC) curves. The top sensitivity nodes were selected based on the rank of the sensitivity nodes in the tornado graph, as shown in Table 2. The main direct cause of falls is hoisting steel beams without appropriate safety facilities, such as the lack of a safety net, limited construction pedal boards, and a lack of ideal fixed points of lifeline and safety belts. Therefore, workers who do not focus more are more prone to fall accidents. The statistical survey on occupational accidents that occur at SC project sites also indicated that hoisting steel beams is a crucial stage in SC projects because the occur-

Table 2. Top sensitivity factors of fall risk at SC projects


rence of occupational accidents during the steel component hoisting and assembling process is the highest (39\%). The other top three stages in which occupational accidents occur at SC building project sites are materiallifting works ( $17 \%$ ), member-fixing works ( $15 \%$ ), and member tearing-down ( $8 \%$ ).

The most sensitive indirect cause of occupational accidents is improper use of personal safeguards. Improper and inadequate use of personal safeguards results in laborers working without proper protection, which can easily lead to construction accidents. Based on the statistics of occupational accidents at SC project sites, approximately half of all occupational accidents that occur during the steel component assembly stage are caused by improper use of personal safeguards. Finally, the root factors include safety and health management and safety training, which play a vital role in the mitigation of fall occurrence at SC project sites. Recent studies have indicated that the most influential factor in the occurrence of accidents is management issues (Aksorn, Hadikusumo 2008).

In summary, this model assesses fall risks at SC building sites and identifies the causes of fall accidents through sensitivity analysis. Based on the analysis, project managers can propose preventive safety measures to reduce the occurrence of falls. Moreover, the fall risk assessment and sensitivity analysis allow project managers to allocate resources toward the critical safety causes early, to substantially mitigate fall risks.

## Conclusion and future developments

This study developed an effective process to build a BNbased fall risk evaluation model for SC building projects. The inference results of the BN were validated against six SC building projects in Taiwan. An analysis and comparison indicated that the BN analysis results are consistent with actual safety records, showing that the transformation process from an FT to a BN can effectively establish a realistic and accurate fall risk evaluation model. Therefore, based on the model assessment and sensitivity analysis, site project managers can prepare preventive safety measures and allocate resources in advance to substantially reduce fall risk at sites.

Although the transformation mechanism from FT to BN has been efficiently examined, the use of a BN relies on the inputs of experts for arcs and CPTs in BN. Data provided by various experts directly affect the accuracy and assessment quality of a BN. Future studies must focus more on expert elicitation. In addition, a BN can be learned from raw data. If complete and accurate safety data are available, an objective BN framework and parameters can be explored and established. Moreover, certain safety events and causes may interact in a time sequence. For such time-dependent safety analysis, a dynamic BN (DBN) may be an appropriate approach; a DBN can be easily built by transforming a dynamic FT (DFT). Finally, other occupational accidents occur frequently at SC project sites, such as object fall, object collapse, and electrocution. It may be necessary to extend the BN scope to cover these accidents and use the BN for an overall safety diagnosis at SC project sites to enhance safety operations and management.
