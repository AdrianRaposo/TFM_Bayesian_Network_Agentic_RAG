# Use of evidential reasoning for eliciting Bayesian subjective probabilities in human reliability analysis: a maritime case 

Zaili Yang1Jin Wang1, Salman Nazir3 *, Khalifa Mohamed Abujaafar1, Zhuohua Qu2,

* Corresponding

1. Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, UK
2. Liverpool Business School, Liverpool John Moores University, UK
3. Human Factors Research Group, Department of Maritime Technology and Innovation, University College of Southeast Norway, Norway.

Ocean Engeneering, 186.
DOI: $\quad$ 10.1016/j.oceaneng.2019.05.077
This article has been accepted for publication and undergone full peer review but has not been through the copyediting, typesetting, pagination and proofreading process, which may lead to differences between this version and the Version of Record. This article is protected by copyright. All rights reserved.

# Use of evidential reasoning for eliciting Bayesian subjective probabilities in human 

reliability analysis: a maritime case

Zaili Yang ${ }^{1 *}$, Khalifa Mohamed Abujaafar ${ }^{1}$, Zhuohua $\mathrm{Qu}^{2}$, Jin Wang ${ }^{1}$, Salman Nazir ${ }^{3}$

1. Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores University, UK
2. Liverpool Business School, Liverpool John Moores University, UK
3. Human Factors Research Group, Department of Maritime Technology and Innovation, University College of Southeast Norway, Norway.
[^0]
[^0]:    * Corresponding author: z.yang@ljmu.ac.uk

# Use of evidential reasoning for eliciting Bayesian subjective probabilities in human reliability analysis: a maritime case 


#### Abstract

Modelling the interdependencies among the factors influencing human error (e.g. the common performance conditions (CPCs) in Cognitive Reliability Error Analysis Method (CREAM)) stimulates the use of Bayesian Networks (BNs) in Human Reliability Analysis (HRA). However, subjective probability elicitation for a BN is often a daunting and complex task. To create conditional probability values for each given variable in a BN requires a high degree of knowledge and engineering effort, often from a group of domain experts. This paper presents a novel hybrid approach for incorporating the evidential reasoning (ER) approach with BNs to facilitate HRA under incomplete data. The kernel of this approach is to develop the best and the worst possible conditional subjective probabilities of the nodes representing the factors influencing HRA when using BNs in human error probability (HEP). The proposed hybrid approach is demonstrated by using CREAM to estimate HEP in the maritime area. The findings from the hybrid ER-BN model can effectively facilitate HEP analysis in specific and decision-making under uncertainty in general.


Keywords: Human reliability analysis, human error probability, evidential reasoning, Bayesian network, maritime risk.

## 1. Introduction

The second generation Human Reliability Analysis (HRA) methods such as the Cognitive Reliability and Error Analysis Method (CREAM) (Hollnagel, 1998) were used to proactively assess the erroneous human actions in complicated systems in a way that the context influencing human action is appropriately taken into account. While facilitating the quantitative development of HRA, these methods exposed some problems in their practical applications. For instance, the prospective assessment model of the basic approach to estimate human error probability (HEP) in CREAM (Hollnagel, 1998) cannot provide a crisp value of the consequences of human performance, and the HEP estimation mechanism is not sensitive to minor changes associated with the nine common performance conditions (CPCs) in CREAM (Yang et al., 2013; Xi et al., 2017). A fuzzy Bayesian reasoning approach was developed to deal with this problem through using Bayesian Networks (BNs) to model the parent-child relationship between the CPCs and Contextual Control Model Controlling Modes (COCOM-CMs) in CREAM (Yang et al., 2013; Abujaafar et al., 2016). However, it requires too much information about the prior conditional probabilities assigned to the node of COCOM-CMs, jeopardising the applicability of the approach. Furthermore, Bayesian inference requires probability completeness. Subjective judgements are usually used to complement the unavailability of statistical data. Even though subjective probabilities can be elicited by experts, it often raises the problems relating

to accuracy, consensus and completeness of judgements. The evidential reasoning (ER) approach (Yang and $\mathrm{Xu}, 2002$ ) has shown its attractiveness to tackle the high uncertainty in data (e.g. incompleteness) associated with subjective judgements and has therefore been used to synthesise experts' estimates in HRA (Xi et al., 2017). However, so far the two challenging but essential features of uncertain data in HRA, interdependency among performance factors and incompleteness in subjective estimates have not been simultaneously addressed with success, in order for effective solutions to be found. Obviously, such incomplete probabilities can be effectively elicited by incorporating partial degrees of belief. In this regard, an ER algorithm has been developed on the basis of the Dempster-Shafer (D-S) theory of evidence (Dempster, 1968; Shafer, 1976), which can be well suited to modelling subjective credibility induced by partial evidence observation (Smets, 1988). The ER's synthesising capability of partial degrees of belief has enlarged the utilisation scope of the traditional probabilistic theory, particularly in describing and handling uncertain information (e.g. incompleteness and ignorance) by using the concept of degrees of belief (Yang et al., 2008; Wan et al., 2019). Therefore, it is proposed to be integrated with BNs in this research to tackle the incapability of BNs in modelling incomplete, subjective probabilities introduced by multiple experts.

This paper presents a new hybrid approach for combining an ER algorithm with BNs in a complementary way, taking into account both interdependent performance factors and incomplete subjective data simultaneously. The kernel of the proposed method is that two individual assessment scenarios involving the best and worst evaluation models for all the nodes of incomplete subjective probabilities, are created, in which the remaining probability masses (due to incompleteness) of the nodes are assigned back to their best (i.e. that contributes to the lowest HEP) and worst (i.e. that contributes to the highest HEP) grades, homogeneously and respectively. To achieve the above aim, the literature on the use of conventional CREAM and the development of the extended CREAM are reviewed to reveal the associated weaknesses and formulate the research problems in Section 2. In Section 3, a new hybrid approach by combining ER and BNs is developed to overcome the problems identified. Its applicability and feasibility are demonstrated by an illustrative example for easy understanding of the relevant mathematical algorithms in Section 4 and by studying the Deepwater Horizon accident case in Section 5. Section 6 concludes the achieved results.

# 2. Literature review 

### 2.1 Traditional CREAM method

To model the causal relations, the CREAM methodology has been derived from its core, the Contextual Control Model (COCOM). COCOM focuses on the principle that human performance is the outcome of the purposive use of competence adjusted to specific working conditions rather than of the predetermined sequence of response to given events (Yang et al., 2013). As one of the most widely known 'second generation' HRA methods, CREAM presents a consistent error classification system that

integrates individual, technological and organizational factors. The classification describes the relations between causes and effects by defining a number of sub-groups and tables, which are provided for the error modes on the one hand and the organisational causes on the other. As a kind of context-related HRA method, CREAM provides an approach to the assessment of cognitive processes during emergencies, and thus it has been widely recognised and used in the analysis of marine accidents. Among the recent examples are Zhou et al. (2017) and Ung (2018). However, CREAM (both basic and extended methods) has exposed certain practical limitations in its applications especially in the maritime industry. The failure rate intervals of Human Failure Probability (HFP) values from the basic method appear to be unacceptably wide even for the use in screening (Fujita and Hollnagel, 2004). It is also difficult to further use and interpret such failure rate intervals in practice. The extended method uses the output from the basic CREAM and appropriate data sources to calculate the probability of each cognitive function failure (Hollnagel, 1998). Lack of critical mass in statistical failure data, however, proves the tasks of adapting the extended method in the maritime area to be challenging ( Xi et al., 2017). All of these limitations stimulate the development of advanced techniques in CREAM.

# 2.2 Extensions of CREAM with uncertainty treatment techniques 

Over the past decade, advanced quantification approaches for HEP in CREAM have been proposed by using different uncertainty treatment techniques including fuzzy logic (Ung, 2015), BNs (Marseguerra et al. 2007), and ER (Xi et al., 2017). Kim et al. (2006) proposed a probabilistic method by using Bayesian networks for a better estimation of the control mode, which is able to produce mathematically correct results when levels of CPCs are given probabilistically. Konstandinidou et al. (2006) developed a fuzzy classification system for the estimation of the probability of human erroneous actions according to CREAM. The results obtained were in the form of crisp numbers, which can be used directly in other risk analysis models (e.g. fault tree model) for the quantification of specific undesired events. Although some attractiveness is observed in terms of the enhancement of CREAM in certain specific aspects though involving one (or some) of these uncertainty treatment techniques, a number of practical problems are still exposed. Examples of such problems include the loss of useful information in fuzzy Max-Min inference operations, lack of adequacy of modelling CPC dependencies and of instant human failure probability estimation, and inability of incorporating different effects/importance on human performance that CPCs may have in the practical HRA applications.

In view of the above-mentioned concerns, Yang et al. (2013) developed a generic BN-based HRA methodology, in which the prospective analysis of CREAM is modified, to facilitate the quantification of maritime human failures by effectively incorporating both fuzzy logic and Bayesian inference mechanisms. The framework has used fuzzy IF-THEN rule bases with belief structures and BNs to aggregate all the rules associated with a seafarer's task in order to estimate his/her failure probability. However, it is realised that large BNs of multi-tier nodes often exist in application domains. Their

complexity is sometimes beyond the current knowledge of domain experts. In addition, conventional mathematical methods are simply not applicable. Therefore, heuristic methods based on 'causal linkage' rather than detailed equations present a feasible way to proceed at present (McErleani et al., 1999). It is particularly important when the aforementioned BN-based HRA models fail to cope with situations where incomplete conditional probabilities are raised/assigned by multiple experts.

# 3. Methodology 

Use of the ER-BN approach in HRA is demonstrated through its application in the CREAM framework given that BNs have been widely used in CREAM-based HRA modelling due to their feature, which takes into account the interaction between the nine CPCs (which are "Adequacy of organisation (\#1)", "Working conditions (\#2)", "Adequacy of man-machine interface and operational support (\#3)", "Availability of procedures and plans (\#4)", "Number of simultaneous goals (\#5)", "Available time (\#6)", "Time of day (\#7)", "Adequacy of training and experience (\#8)" and "Crew collaboration quality (\#9)"). In this research, the proposed ER-BN model consists of the following four steps:

Step 1. The rule base of modelling probabilistic causal relation between parent-child nodes in the BNbased CREAM (e.g. Figure 2) is developed (Yang et al., 2013; Abujaafar et al., 2016). It reflects the interaction among the nine CPCs originally defined in CREAM (Hollnagel, 1998). During this process, the conditional probabilities of the parent-child nodes are elicited in either a complete or incomplete format by a group of domain experts.

Step 2. The ER approach (Yang and $\mathrm{Xu}, 2002$ ) is used to synthesise the complete/incomplete conditional probabilities and aggregate the child nodes' conditional probabilities that are symmetrically affected by the nodes associated with the nine CPCs.

Step 3. The unknown/remaining probability masses (i.e. the unassigned probabilities to the grades of the child node) due to incomplete judgements are assigned back to the best (i.e. that contributes to the lowest HEP) and worst (i.e. that contributes to the highest HEP) grades of the nodes. Two BN models, representing the best scenario in which all the remaining probability masses of the nodes having unknown probabilities are assigned to the best grades of their corresponding nodes, and the worst scenarios in which they are assigned to the worst grades of the nodes, are constructed respectively.

Step 4. The two results from the best and worst scenarios are aggregated to obtain a crisp HEP using ER. Different weights can be assigned to the results obtained from the best and worst scenarios to present the HEPs in a range from optimistic to pessimistic perspectives.
3.1 Developing the rule base of modelling parent-child nodes and eliciting the complete or incomplete degrees of belief of COCOM-CMs

To assess HEP, it requires the evaluation of the CREAM context through the effect levels of the nine CPCs. By using a BN, it is possible to graphically map the nine CPCs in a convergent connection to infer the probabilities of the COCOM-CMs (in which the four characteristic control modes are "Scrambled", "Opportunistic", "Tactical" and "Strategic" ). In this context, each CPC is described by a number of discrete states including four states for three CPCs and three states for the remaining six CPCs, according to the original CREAM. Different levels of each CPC along with their individual effect on human performance are described in Table 1, and the relation between CPCs and the control modes is depicted in Figure 1.

Table 1. Description of CPCs and associated linguistic variables (Hollnagel, 1998)


![img-0.jpeg](img-0.jpeg)

Figure 1. The relation between CPCs and control modes (Hollnagel, 1998)

Such convergent connection will result in $46,656\left(4^{3} \times 3^{6}\right)$ discrete conditional probabilities to be assigned. The configuration of such a large number of discrete conditional probabilities subjectively by domain experts will be of great difficulty. Therefore a divorcing method is introduced to simplify the task of assigning subjective probabilities by adding three attributes (the second tier) and two subattributes (the third tier) shown in Figure 2. The three attributes (nodes) are "Action load", "Working environment" and "Operator preparedness" directly influencing COCOM-CMs' probability (Marseguerra et al., 2007). Each attribute is associated with different CPCs according to the reasoning in CPCs' evaluation by Hollnagel (1998). The attribute "Working environments" is influenced by five CPCs. To further simplify its conditional probability table (CPT) assignment, two new sub-attributes, "Adequacy of working culture" and "Adequacy of perception conditions" are also introduced. The CPTs of the attributes and sub-attributes are assigned based on the uniformly defined states, "Inappropriate", "Acceptable" and "Appropriate" which present the reduced, satisfactory and improved effects to human reliability, with respect to the defined grades of the nine CPCs in CREAM. A divorcing concept has no significant effect on modelling mathematical inference if attributes and sub-attributes' CPTs are assigned properly (Kim et al., 2006). The use of a divorcing concept simplifies the assignment of CPTs of the developed BN-based CREAM model. It also makes it possible to introduce fuzzy rule bases (FRB) to facilitate the elicitation of subjective CPTs of the child nodes. For example, the interactive logical relation between the effect levels of the three attributes "Action load (A)", "Working environments (W)" and "Operator preparedness (O)", and the COCOM-CMs is described as follows while the CPT of the COCOM-CMs under the three parents is established in Table 5. The interaction among the nine CPCs (at the fifth and sixth tiers) and their relationship with the four adjusted CPCs (at the fourth tier) are modelled based on the original CREAM method (Hollnagel, 1998). Since the development of this part (Tier 4 to Tier 6) of the network has been described in Yang et al., (2013), it is not repeated in this paper.

![img-1.jpeg](img-1.jpeg)

Figure 2. BN based CREAM generic model for human performance reliability assessment
To model the interactive relations between the new attributes and COCOM-CMs in a logical form, fuzzy logic can be used to construct IF-THEN rules. Each of IF-THEN rules includes two parts: an antecedent that responds to the fuzzy input of the three attributes (each of which has three grades) and a consequence associated with the COCOMs' four control modes as the fuzzy output. In this study, a collection of multiple-input multiple-output FRB (consisting of 27 rules (i.e. $3 \times 3 \times 3$ )) is defined as follows (Yang et al., 2009; 2010):

$$
R_{l}: \text { IF } L_{1}{ }^{k, l} \text { and } L_{2}{ }^{k, l} \text { and } L_{3}{ }^{k, l}, \text { THEN }\left(\beta_{1, l}, \beta_{2, l}, \beta_{3, l}, \beta_{4, l}\right)
$$

In a fuzzy rule $R_{l}(l=1,2, \ldots, 27)$, if the input satisfies the antecedent linguistic vector(s) $L_{r}{ }^{k, l}(r=1$, $2,3 ; l=1,2, \ldots, 27 ; k=1,2,3)$, the output $\beta_{j, l}(j=1,2,3,4 ; l=1,2, \ldots, 27)$ represents the belief degree(s) to which a control mode $D_{j}(j=1,2,3$ or 4$)$ is believed to be the consequence. Linguistic vector $L_{r}{ }^{k, l}$ is defined with its nature of having "Appropriate" (improved), "Acceptable" (not significant) or "Inappropriate" (reduced) effects on COCOM-CMs. Obviously, if $L_{1}^{k, l}$ is "Action load", then $L_{1}{ }^{k, l}$ can be any of the three linguistic variables used to describe "Action load", which are Inappropriate $\left(L_{1}{ }^{1, l}\right)$, Acceptable $\left(L_{1}{ }^{2, l}\right)$, and Appropriate $\left(L_{1}{ }^{3, l}\right)$. The following illustrative rule is developed to interpret the rules with a belief structure.

- $R_{2}$ : IF the "Action load" is Inappropriate AND the "Working environments" are Appropriate AND "Operator preparedness" is Inappropriate, THEN the belief degrees of operator COCOMCM would be $0 \%$ "Strategic", $0 \%$ "Tactical", $10 \%$ "Opportunistic", and $90 \%$ "Scrambled". It can be further simplified and presented as:

- $R_{2}$ : IF $L_{1}{ }^{1}$. AND $L_{2}{ }^{1}$. AND $L_{3}{ }^{2}$. THEN $\left(D_{1}, 0\right),\left(D_{2}, 0\right),\left(D_{3}, 0.1\right),\left(D_{4}, 0.9\right)$
where each $L_{r}{ }^{k, 2}(r=1,2,3 ; k=1,2,3)$ in Rule 2 indicates the $k^{\text {th }}$ linguistic variable descriptor associated with the $r^{\text {th }}$ attribute. The set of degrees of belief $\beta_{j, 2}(j=1,2,3,4)=(0,0,0.1,0.9)$ represents the combined subjective conditional probabilities from domain experts. The way of calculating $\beta_{j . i}$ is given in Section 3.2.2. Such a rule base represents the possible functional mappings of uncertainty between the three new attributes and the four control modes. It provides a more informative, realistic scheme than a simple IF-THEN rule base does on uncertain knowledge representation. However, the challenge lies in the incompleteness knowledge encounters by the experts when assigning degrees of belief in the rule base modelling the relation among $\mathrm{O}, \mathrm{A}, \mathrm{W}$ and COCOMs. In other words, the problem appears in a situation, where the sum of the elicited degrees of belief is less than 1. In order to incorporate them into the estimate of COCOM-CMs probabilities in a convergent connection of a BN, the synthesizing capability of the ER algorithm is investigated accordingly.


# 3.2 Synthesising the complete and incomplete expert judgements' degrees of belief 

In order to investigate the capability of the ER approach in synthesising incomplete assessments, a hierarchy of two levels of attributes is considered, where the upper level represents the synthesised states $D_{j}(j=1,2,3,4)$ of the child node (i.e. COCOM), and the lower level represents the states of the parent nodes (i.e. $\mathrm{O}, \mathrm{A}, \mathrm{W}$ ) that are denoted by $L_{r}{ }^{k}(r=1,2,3 ; k=1,2,3)$.

In this respect, the assessment of the conditional probability $\beta_{j}^{i}$ of $D_{j}(j=1,2,3,4)$ by the $i_{t h}$ expert $E_{i}$ from a group of $M(i=1,2, \ldots M)$ conditional on $L_{r}{ }^{k}$ mathematically, is represented by the following distribution:

$$
P\left(E_{i} \mid L_{r}^{k}\right)=\left(D_{j}, \beta_{j}^{i}\right),(i=1,2, \ldots M ; j=1,2,3,4 ; r=1,2,3 ; k=1,2,3)
$$

where, $0 \leq \beta_{j}^{i} \leq 1, \sum_{j=1}^{4} \beta_{j}^{i} \leq 1$ and $\beta_{j}^{i}$ denotes a conditional degree of belief assigned to the $j_{t h}$ state of the COCOM-CMs node by the $i_{t h}$ expert. The above distribution reads that the conditional probability $\beta_{j}$ of the child node has been subjectively assessed using the evaluation grade(s) $D_{j}$ distinctively and conditionally on the parents' evaluation grades $L_{r}{ }^{k}$ combined with a conditional degree of belief $\beta_{j}^{i}$. An assessment by $E_{i}$ is complete if $\sum_{j=1}^{4} \beta_{j}^{i}=1$ and incomplete if $\sum_{j=1}^{4} \beta_{j}^{i}<1$. Such partial or complete ignorance is not rare in many distinctive evaluation problems.

Suppose the importance or the relative weight of the expert $E_{i}$ is given by the weight $\omega_{i}(i=1,2, \ldots, M)$ with the condition that $0 \leq \omega_{i} \leq 1$. In this regard, the relative importance of $E_{i}$ plays an important role

in a group assessment. Collectively, $\omega_{i}(i=1,2, \ldots, M)$ has to be normalized for the consistency of the assessment.

To capture the non-linear relationship between different experts $\boldsymbol{E}_{\boldsymbol{i}}(i=1,2, \ldots, M)$, the ER approach is used to combine all $\beta_{j}^{i}(j=1,2,3,4)$ from each $\boldsymbol{E}_{\boldsymbol{i}}$ and generate a final conclusion. Having represented belief degree distributions $\beta_{j}^{i}$, the ER approach can be implemented as follows. First, it is required to transform the degrees of belief $\beta_{j}^{i}$ for all $j=1,2,3,4$, and $i=1,2, \ldots, M$ into basic probability masses using the following equations (Yang and Xu, 2002; Liu et al., 2005):

$$
\begin{aligned}
& m_{j}^{i}=w_{i} \beta_{j}^{i} \\
& m_{D}^{i}=1-\sum_{j=1}^{4} m_{j}^{i}=1-w_{i} \sum_{j=1}^{4} \beta_{j}^{i} \\
& \bar{m}_{D}^{i}=1-w_{i} \\
& \tilde{m}_{D}^{i}=w_{i}\left(1-\sum_{j=1}^{4} \beta_{j}^{i}\right), \text { for all } j=1,2,3,4 \text { and } i=1,2, \ldots, M
\end{aligned}
$$

where $m_{j}^{i}$ are individual degrees to which $E_{i}$ supports the final synthesised conclusion $D ; w_{i}$ represents the relevant importance of $E_{i}$ and thus $\sum_{i=1}^{M} w_{i}=1$; and $m_{D}^{i}=\bar{m}_{D}^{i}+\tilde{m}_{D}^{i}$ for all $i=1,2, \ldots, M$. The probability mass of $E_{i}\left(m_{D}^{i}\right)$ unassigned to the final synthesised conclusion $D$, which is unassigned to any individual output variables $D_{j}$, is split into two parts, one caused by the relative importance of $E_{i}$ $\left(\bar{m}_{D}^{i}\right)$, and the other due to the incompleteness of the belief degree assessment $\beta_{j}^{i}\left(\bar{m}_{D}^{i}\right)$.

Then, it is possible to aggregate all the outputs from $E_{i}(i=1,2, \ldots, M)$ to generate the combined degree of belief $\left(\beta_{j}\right)$ in each possible $D_{j}$ of $D$. Suppose $m_{j}^{C(i)}$ is the combined belief degree in $D_{j}$ by aggregating all the outputs from the $M$ experts and $m_{D}{ }^{C(i)}$ is the remaining belief degree unassigned to any $D_{j}$. Let $m_{j}^{C(i)}=m_{j}{ }^{j}$ and $m_{D}{ }^{C(i)}=m_{D}{ }^{i}$. Then the overall combined belief degree in $D_{j}$ is generated as follows (Liu et al., 2005).

$$
\begin{gathered}
\left\{D_{j}\right\}: m_{j}^{C(i+1)}=K_{C(i+1)}\left[m_{j}^{C(i)} m_{j}^{i+1}+m_{j}^{C(i)} m_{D}^{i+1}+m_{D}^{C(i)} m_{j}^{i+1}\right] \\
m_{D}^{C(i)}=\tilde{m}_{D}^{C(i)}+\bar{m}_{D}^{C(i)}, i=1,2, \ldots, M-1 \\
\{D\}: \tilde{m}_{D}^{C(i+1)}=K_{C(i+1)}\left[\tilde{m}_{D}^{C(i)} \tilde{m}_{D}^{i+1}+\tilde{m}_{D}^{C(i)} \bar{m}_{D}^{i+1}+\bar{m}_{D}^{C(i)} \tilde{m}_{D}^{i+1}\right]
\end{gathered}
$$

$$
\begin{aligned}
& \bar{m}_{D}^{C(i+1)}=K_{C(i+1)}\left[\bar{m}_{D}^{C(i)} \bar{m}_{D}^{i+1}\right] \\
& K_{C(i+1)}=\left[1-\sum_{j=1}^{4} \sum_{i=1}^{4} m_{j}^{C(i)} m_{i}^{i+1}\right]^{-1}, i=1,2, \ldots, M-1 \\
& \left\{D_{i}\right\}: \beta_{j}=\frac{m_{j}^{C(M)}}{1-\bar{m}_{D}^{C(M)}} \quad(j=1,2,3,4) \\
& \left\{D_{i}\right\}: \beta_{D}=\frac{\bar{m}_{D}^{C(M)}}{1-\bar{m}_{D}^{C(M)}}
\end{aligned}
$$

where $\beta_{j}$ indicates the normalised belief degree assigned to $D_{i}$ in the final synthesised conclusion $D$ and $\beta_{D}$ represents the normalised remaining belief degree unassigned to any $D_{i}$.

# 3.3 Distributing the unassigned probability masses in the COCOM-CMs BN to obtain a HEP interval 

The unassigned probability mass $\beta_{D}$ caused by the incompleteness of judgements is assigned back to $B_{1}$ (i.e. Strategic) representing the best scenario with the lowest possible HEP and to $B_{4}$ (i.e. Scrambled) indicating the worst scenario with the highest possible HEP, respectively. Similarly, all the unassigned probability masses of the other child nodes in Figure 2 are assigned to their own CPTs with respect to the best and worst scenarios. Consequently, two individual COCOM BNs are established, from which the CPTs associated with the best and worst cases will be used to calculate the lowest and highest HEP values. The highest and lowest HEPs can be used as the two limits of an interval. It reflects the fact that the HEP analysis with incomplete input delivers its values in an interval, in which the actual HEP exists.

### 3.4 HEP quantification and ranking

To quantify the human failures, each $D_{i}(j=1, \ldots, 4)$ requires the assignment of an appropriate utility value $U_{D j}$. The values can be obtained by using a Weighted Mean of Maximum (WMoM) method as $2.24 \times 10^{-4}, 0.01,0.0708$ and 0.316 , respectively (Yang et al., 2013). A new HEP index can be calculated as:

$$
H E P=\sum_{j=1}^{4} \beta_{j} U_{D_{j}}
$$

The larger the value of HEP is, the lower the reliability level of human performance. However using Eq 14, the highest and lowest HEPs with respect to the best and worst scenarios can only construct a

HEP interval. Human action is more reliable than the other if and only if its highest value is smaller than the lowest one of the other. It is worth noting that such an approach is not preferred for a ranking purpose. A new coefficient, $\alpha$, is introduced to indicate evaluators' perception on the two sets of $\beta_{j}$ (i.e. $\left.\beta_{j}^{*} \text { and } \beta_{j}^{*}\right)$ with regards to the best and worst scenarios. More specifically, $\alpha$ means the extent to which the evaluators believe the HEP belongs to the best scenario and 1- $\alpha$ represents the extent to which HEP belongs to the worst scenario. If the evaluators are optimistic, $\alpha=1$ and the final HEP is the lower limit of the HEP interval. If the evaluators are pessimistic, $\alpha=0$ and the final HEP is the upper limit for the HEP interval. If $0<\alpha<1$, the final HEP can be calculated by using Eq. 15 .

$$
\beta_{j}=\alpha \beta_{j}^{*} \cup(1-\alpha) \beta_{j}^{*}
$$

where $U$ means the combination of the two sets by the ER algorithm in Eqs. 3 - 13 and $\alpha$ is set as 0.5 when the evaluators are neutral. The final crisp HEP is then calculated by applying the combined $\beta_{j}$ to Eq. 14 .

# 4. Case study of proposed methods in the Deepwater Horizon accident 

In this section, a case study of the Deepwater Horizon accident is conducted to illustrate the feasibility and applicability of the hybrid ER-BN model in facilitating the HEP analysis, and the evaluation results are compared with those obtained from traditional CREAM methods. The main reasons of using the proposed ER-BN model to investigate the Deepwater Horizon accident include that 1) there were several main governing factors symmetrically affecting the effect levels of the nine CPCs over the whole period of the drilling operations, and 2) the uncertainty associated with the available information during the final stages of drilling operations was high.

### 4.1 Background information of the Deepwater Horizon accident

In the evening of April 20, 2010, a well control event allowed hydrocarbons to escape from Macondo well onto Transocean's Deepwater Horizon, resulting in explosions and fire on the rig. 11 people lost their lives, and 17 others were injured. The fire, which was caused by the hydrocarbons from the well, continued for 36 hours until the rig sank. Hydrocarbons continued to flow from the reservoir through the wellbore and the Blow Out Preventer (BOP) for 87 days, causing a spill of a national significance.

Deepwater Horizon was located approximately 50 miles south of Venice, LA at Mississippi Canyon 252. The accident on April 20, 2010, involved a well integrity failure, followed by a loss of hydrostatic control of the well. This followed a failure to control the flow from the well with the BOP equipment, which allowed the release and the subsequent ignition of hydrocarbons. Ultimately, the BOP emergency functions failed to seal the well after the initial explosions (BP, 2010).

### 4.2 Aggregating multi attribute effects on the root cause nodes (i.e. the nine CPCs)

The evaluation of CPCs in this case study is based on the accident investigation team's analysis results specifically presented in Appendix T of the Deepwater Horizon Accident Investigation Report (BP, 2010). The report describes the relevant practices, procedures, and expectations, comparing them with the rig crew's actions in monitoring the Macondo well and managing the well control event on 20 April 2010. It includes the documents that governed the drilling operations on board the Deepwater Horizon at the time of the accident; the available real-time data; and the witness account interview. In this respect, Table 2 summarizes the specified functional assessment attributes, the identified evidence, and their evaluation.

Table 2. Identified relevant practices, procedures, and expectations of rig crew's actions in monitoring the Macondo well and managing the well control event on 20 April 2010




The inherent variability effects that shaped operators' actions and observations in the context of events are used in CPCs' effect level evaluations. The evaluations listed in Table 3 have been conducted in a way in which 1) if there is direct evidence from Table 2 supporting a particular effect level of CPCs, then a $100 \%$ degree of belief is assigned accordingly, 2) if there is no evidence or relevant information available to support the evaluation with respect to a particular effect level of CPCs, then average degrees of belief are assigned across all the effect levels to reflect the unknown situation, and 3) if it is irrelevant to the effect, (x) is applied. Given the functional assessment attributes are exclusive factors influencing the effect level of the CPCs, their evaluations can be considered as pieces of evidence to support the performance of the CPCs, the ER algorithm (i.e. Eqs 3-13) is used to synthesise them to obtain the effect levels of the 9 CPCs within the context of the Deepwater Horizon case. The intelligent decision system (IDS) software (Yang and $\mathrm{Xu}, 2002$ ) is used to aggregate the evaluated degrees of belief of each

functional assessment attribute to obtain the unconditional probabilities of their associated CPCs' effect levels, as shown in Table 4.

Table 3. Evaluation of functional assessment attributes affecting CPCs' effect levels/descriptors


Table 4. CPCs effect levels/descriptors and the assigned degrees of belief aggregation with IDS



# 4.3 Calculate the CPTs in two BNs for the best and worst scenarios 

The use of the ER algorithm in the formation of CPTs in BN with incomplete information (e.g. subjective judgements) is demonstrated in this part. To obtain the information needed for constructing the CPT of the COCOM-CMs node (i.e. the node of human action performance at the top of Figure 2), three maritime experts $E_{l}(i=1,2,3)$ with significant domain knowledge were interviewed to provide their subjective elicitation on the evaluation grades of the COCOM-CMs in terms of conditional degrees of belief as defined by Eq. 1. Three offshore/marine engineers provided their input data within the context of marine engineering operations. The careful selection of the representative experts within the maritime industry is conducted to reduce the bias involved in the subjective judgements. Each of the three selected experts has over 15-year working experience on board offshore rigs or commercial ships and holds a high position in his/her companies. This contributes to the high quality of the initial data from experts. According to the collected feedback (i.e. Table 5), the initial judgements of the three experts keep a very high consistency, which proves that the judgements are at large in harmony and the data quality is assured. Their inputs are listed in Table 5.

Table 5. Elicitation of evaluation grades' conditional degrees of belief for the three attributes, O, W and A



Due to the similar seniority of the three experts, equal weight was assigned to each expert when synthesising their judgements using the ER algorithm. Taking Rule No. 7 in Table 5 as an example, the first two assessments by $E_{1}$ and $E_{2}$ are synthesised, as presented in Appendix A. In a similar way, the result of combining three experts' judgements can be obtained by synthesising the combination of the first two assessments (as one set) with the third assessment (expert $E_{3}$ ) using the same algorithm. It is worth noting that judgements from other experts can be also combined when more feedback from a wider range of interview is collected in future research. Consequently, the synthesised human action control modes' degrees of belief $B_{j}$ for the $7^{\text {th }}$ rule are Strategic $\left(B_{1}\right)=0$, Tactical $\left(B_{2}\right)=0.0252$, Opportunistic $\left(B_{3}\right)=0.3271$ and Scrambled $\left(B_{4}\right)=0.5713$. The results reveal that an unknown mass of 0.0744 is involved in the $7^{\text {th }}$ rule due to the expert judgements. Windows based IDS software was developed to simplify the above calculation process by Yang (2001). It is used to synthesise the basic attributes $E_{i}$ of Rule 7 with the same result obtained. IDS is also used in synthesising the other combined degrees of belief (or probabilities) listed in Table 5.

Although the ER algorithm is used to synthesise experts' combined degrees of belief mass $\beta_{j}$, a remaining unknown mass $\beta_{D}$, which is not assigned to any evaluation grades, is also developed. Consequently, the remaining unassigned degrees of belief are assigned back to the best evaluation grade "Strategic" and the worst evaluation grade "Scrambled" on all rules. Accordingly, two sets of evaluation grades are generated in Table 6 and used as prior probabilities in the generic COCOM BN model to calculate HEP estimates. Consequently, there are two BNs models presenting the best and worst scenarios.

Table 6. Synthesised and combined degrees of beliefs of COCOM-CMs evaluation grades



The CPT of the COCOM-CMs node in the BN presenting the best scenario can be obtained by taking into account the values of (D1)C, (D2), (D3) and (D4), while the one for the worst scenarios is associated with the set of $\{(D 1),(D 2),(D 3)$ and $(D 4) C\}$ (See Table 6). For instance, in Rule 1 in Table 6 , if $O$ is inappropriate, $W$ is inappropriate, and $A$ is inappropriate, then COCOM-CMs are $\{$ 0.0211 Strategic, 0 Tactical, 0 Opportunistic, 0.9789 Scrambled $\}$ in the best scenario; and $\{\mathbf{0}$ Strategic, 0 Tactical, 0 Opportunistic, 1 Scrambled $\}$ in the worst scenario. As a result, the two BNs for the best and worst scenarios are constructed and presented in Figures 3 and 4, respectively.

![img-2.jpeg](img-2.jpeg)

Figure 3: BN model displaying human COCOM-CMs' posterior probabilities based on the best possible set of evaluation grades
![img-3.jpeg](img-3.jpeg)

Figure 4: BN model displaying human COCOM-CMs' posterior probabilities based on the worst possible set of evaluation grades

# 4.4 Quantification of human error in the Deepwater Horizon case

The evaluations of the CPCs' effect levels in Table 4 are used as input observations of root cause nodes in the two established BN models in Figures 3 and 4. The posterior probabilities of the two assessment models' evaluation grades and their transformed respective HEP results are shown in Table 7. During this process, Eq. 14 is used to calculate the lower and upper limits of the HEP interval from the best and worst scenarios. The result shows that the HEP estimates in the case are from $14.83 \%$ to $15.94 \%{ }^{1}$.

Finally, HEPs are presented in a utility interval rather than a crisp value. Such an interval could be used effectively to specify the uncertainty involved in the assessment. However, for a ranking purpose, a crisp value of the HEP interval can be calculated as 0.1547 using Eq. 15, as presented in Table 7. The result indicates a control mode of 'opportunistic' according to the values of probability of action failure defined in the CREAM methodology (See Table 8).

Table 7. Final HEPs of both assessed scenarios


Table 8. The control modes and probability intervals (Hollnagel, 1998)


# 4.5 Comparative analysis and discussion of the results

[^0] [^0]: ${ }^{1}$ Such HEPs are subject to the assignment of the utility values of the four control modes. Although the utility values are cited from the work from a leading journal (i.e. Ocean Engineering), further verification of such utility values is still required to fully validate the significance of the HEP values in terms of precise risk analysis. Having said that, it is believed that the obtained HEP values can be effectively used for risk prioritisation.

Based on the identified relevant practices, procedures, and expectations of rig crew's actions from the Deepwater Horizon Accident Investigation Report (as presented in Table 5), the traditional CREAM and fuzzy CREAM methods are applied in the same case study for the quantification of human error in HRA. It allows for a more practical and effective investigation of the applicability of the proposed model through a comparative analysis. In this subsection, we mainly focus on the comparison of their pros and cons in the real-life applications, as well as the similarity and difference of results obtained from different methods. Thus, detailed information on how to conduct these CREAM-based methods is not omitted here, and more information can be found in Hollnagel (1998) and Konstandinidou et al. (2006) for further reference. The evaluation results from different methods are presented and compared in Table 9.

Table 9. Comparison of the results obtained from different methods


At this stage of validation, it is worthwhile to differentiate the results obtained from different CREAM related methods. In this context, the traditional CREAM result is calculated based on CPCs' evaluation scores improved and reduced (1, 7); the plotting of these scores on the graph shown in Figure 1 reveals the result of opportunistic control mode and its related generic probability interval. It only provides a wide failure rate interval. Without a crisp value of HEP, it is not even suitable for screening in practical applications. The result generated by the fuzzy model, which can be expressed in the form of a crisp number, can be used directly in fault tree and event tree calculations for the quantification of specific undesired events. However, it also suffers from the problem of failing to incorporate the uncertainties in data (e.g. incomplete information) involved during the assessment. Besides, altogether 46656 fuzzy rules are included in the proposed fuzzy model (Konstandinidou et al., 2006), which, due to its complexity, inevitably hinders its industrial applications. In the proposed ER-BN CREAM model, the final calculation of HEP is 0.1547 failure/time; this HEP inclusively lies within the range of original opportunistic mode in CREAM $(0.1<$ HEP $<0.5)$, revealing the accuracy of the result. However it improves the accuracy of the HEP interval from $[0.01,0.5]$ to $[0.1483,0.1594]$ with a HEP crispy value of 0.1547 . Comparing the results with those obtained from other approaches, obviously, the specified HEP would provide a more accurate result with a better resolution that will enable an assessor to develop a rational preventative plan.

By changing the BN mode, it has been found that CPC8 (adequate training and expertise to $100 \%$ with respect to all functional assessment attributes) has the most significant impact on

the reduction of the HEP. Theoretically, such an analysis can provide scientific support on which $\mathrm{CPC}(\mathrm{s})$ should be better controls in the recommendations for avoidance of similar accidents in future. From a perspective of capability and competency, it is suggested to deepen the capabilities of personnel in key operational and leadership positions and augment existing knowledge and proficiency in management deep-water drilling and wells operations. Also, advanced deep-water well control programs that supplement current industry and regulatory training need to be developed (BP, 2010). With respect to the training and exercises of emergency response, the organization is suggested to motivate personnel to discuss safety-related concerns of the emergency drills and exercises to increase personnel's skills in the emergency. It is also important for organizations and personnel to regularly check the emergency equipment and procedures associated with their capacities, arrangement, and performance standards during the emergency drills and exercises (Norazahar et al., 2014).

# 5. Contribution and implication 

The major contributions of the generated methods and models in this paper are explained from both practical and theoretical aspects. Practically, the uses of the BN inference and FRB structure can effectively help to forecasts the high HEPs of hazardous situations and send an early warning signal to prevent maritime accidents. Accordingly, the used techniques would provide the potential for identifying the most influencing $\mathrm{CPC}(\mathrm{s})$ and the associated functional assessment attributes (e.g. initiating events or root causes), to develop the risk control options effectively. In addition, using the ER algorithm for synthesising expert's judgments for Bayesian subjective probability elicitation is able to enhance CREAM based HRA methodology, which will facilitate the application of relevant methods in human performance reliability analysis in maritime and offshore domains where expert judgements are usually involved due to the lack of reliable data in maritime safety assessment. Theoretically, both BN probabilistic inference and ER synthesising capabilities are used to represent and process context knowledge and uncertainty. The combination provides a feasible solution to subjective elicitation of CPT in BN applications.

The developed methods possess enormous potential as valuable aids and effective alternatives to retain and improve human performance in marine engineering operations. It has the potential and flexibility to be tailored to handle the incompleteness of subjective data when using BNs to aid decision-making in other sectors.

## 6. Conclusion

ER's synthesising and aggregation capability has enlarged the scope of a BN mechanism inference viability in describing and handling uncertain information in an engineering operation context. By using the concept of degrees of belief, the ER-BN combination can model context knowledge incompleteness and ignorance explicitly at any BN assessment level. Combining degrees of ignorance with the best and worst evaluation grades can generate two BNs to describe the best and worst scenarios of COCOM-

CMs' probabilities. Subsequently, their results are transformed and presented in HEP intervals, where each could be further converted into a crisp HEP value for a ranking purpose, as demonstrated in the above case study. Consequently, a new hybrid ER-BN method is developed capable of handling the problems to which the traditional methods lack the ability to provide appropriate solutions. Applying it in HRA facilities the assessment of HEPs through the established CREAM BN generic model in a situation where incomplete subjective probability elicitation is necessary.

# Acknowledgements 

This work is partially supported by EU FP7 Marie Curie IRSES ENRICH project (ENRICH - 612546) and EU H2020 RISE ENHANCE project (MSCA-RISE 823904).

# Appendix A 

To calculate the basic conditional probability masses $m_{j}^{i}$ as defined by Eq. 2.
$m_{1}^{1}=0.333 \times 0=0 ; m_{2}^{1}=0.333 \times 0=0 ; m_{3}^{1}=0.333 \times 0.3=0.0999 ; m_{4}^{1}=0.333 \times 0.7=$ 0.2331
$m_{1}^{2}=0 \times 0.333=0 ; m_{2}^{2}=0.1 \times 0.333=0.0333 ; m_{3}^{2}=0.3 \times 0.333=0.0999 ; m_{4}^{2}=0.3 \times$ $0.333=0.0999$.
$m_{1}^{3}=0 \times 0.333=0 ; m_{2}^{3}=0 \times 0.333=0 ; m_{3}^{3}=0.4 \times 0.333=0.1332 ; m_{4}^{3}=0.6 \times 0.333=$ 0.1998 .

Next the remaining relative importance $\bar{m}_{D}^{i}$ for all $i=(1,2,3)$ is obtained as follows using Eq. 5
$\bar{m}_{D}^{1}=1-0.333=0.667$
$\bar{m}_{D}^{2}=1-0.333=0.667$
$\bar{m}_{D}^{3}=1-0.333=0.667$
The remaining probability mass $\bar{m}_{D}^{i}$ due to the possible incompleteness of any individual grade $\beta_{j}^{i}$ is defined by Eq. 6.
$\bar{m}_{D}^{1}=0.333[1-(0+0+0.3+0.7)]=0$
$\bar{m}_{D}^{2}=0.333[1-(0+0.1+0.3+0.3)]=0.0999$
$\bar{m}_{D}^{3}=0.333[1-(0+0+0.4+0.6)]=0$
The normalizing factor $K_{C(i+1)}$ for combining the two assessments from $E_{1}$ and $E_{2}$ is calculated using Eq. 11.
$K_{C(i+1)}=[1-(0 \times 0.0333+0 \times 0.0999+0 \times 0.0999)+(0 \times 0+0 \times 0.0999+0 \times$
$0.0999)+(0.0999 \times 0+0.0999 \times 0.0333+0.0999 \times 0.0999)+(0.2331 \times 0+0.2331 \times$
$0.0333+0.2331 \times 0.0999)]^{-1}=1.0464$

The remaining combined probability mass $\bar{m}_{D}^{C(i+1)}$ due to the possible incomplete assessment of $\beta_{j}^{i}$ by $E_{1}$ and $E_{2}$ is defined by Eq. 8.
$\bar{m}_{D}^{C(i+1)}=1.0464[(0 \times 0.0999)+(0.667 \times 0.0999)+(0 \times 0.667)]=0.0697$.
The combined remaining relative importance $\bar{m}_{D}^{C(i+1)}$ from the two assessments conducted by $E_{1}$ and $E_{2}$ are obtained using Eq. 9 .

$\bar{m}_{D}^{C(i+1)}=1.0464(0.667 \times 0.667)=0.4655$.
To calculate the combined probability mass $\beta_{j}$, Eq. 12 is employed as follows.
$\beta_{1}=1.0464[(0 \times 0)+(0 \times 0.7669)+(0.667 \times 0)]=0$
$\beta_{2}=1.0464[(0 \times 0.0333)+(0 \times 0.7669)+(0.667 \times 0.0333)]=0.0232$
$\beta_{3}=1.0464[(0.0999 \times 0.0999)+(0.0999 \times 0.7669)+(0.667 \times 0.0999)]=0.1537$
$\beta_{4}=1.0464[(0.2331 \times 0.0999)+(0.2331 \times 0.7669)+(0.667 \times 0.0999)]=0.2698$.
Finally, the remaining combined probability mass $\boldsymbol{\beta}_{\boldsymbol{\ell}}$, due to the possible incomplete assessment of $E_{1}$ and $E_{2}$ is calculated by Eq. 13.
$\beta_{23}=\frac{0.0697}{1-0.4655}=0.1304$