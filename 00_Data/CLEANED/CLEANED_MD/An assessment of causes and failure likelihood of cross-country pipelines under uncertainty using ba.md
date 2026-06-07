# LJMU Research Online 

Hassan, S, Wang, J, Kontovas, CA and Bashir, M

## An assessment of causes and failure likelihood of cross-country pipelines under uncertainty using bayesian networks

## http://researchonline.ljmu.ac.uk/id/eprint/15936/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Hassan, S, Wang, J, Kontovas, CA and Bashir, M (2021) An assessment of causes and failure likelihood of cross-country pipelines under uncertainty using bayesian networks. Reliability Engineering and System Safety, 218. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# An assessment of Causes and Failure Likelihood of Cross-Country Pipelines under Uncertainty using Bayesian Networks 

Shamsu Hassan ${ }^{1}$, Jin Wang², Christos Kontovas ${ }^{3}$, Musa Bashir ${ }^{4}$<br>Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores<br>University, Liverpool, UK

## Highlights

- An integrated approach to dynamic pipeline failure likelihood analysis
- Incorporates subjective data and accommodates uncertainties using BN and AHP
- Identifies parameters that have the most impact on reducing pipeline loss of containment
- Nigeria's pipeline system used to show model application in situations where failure data is limited or unreliable


## Abstract

The increased incidents of pipeline failures and resultant consequences of fires, explosions and environmental pollution motivate stakeholders to find solutions in dealing with these emerging threats as part of process safety management. This is further compounded by the absence of reliable failure data, particularly in developing countries. To address such challenges, a Bayesian Network (BN) model has been developed. The aim of the model is to highlight the contributing failure factors to the identified pipeline hazards and their interrelationships. The BN approach is appropriate for this work because it accommodates data uncertainty, or the lack of data, and can integrate the expert's knowledge. The model is especially good at updating the results whenever new data becomes available.
The proposed model has been applied to a case study focusing on estimating the failure probabilities of Nigeria's cross-country oil pipeline system - 2B as part of the pipeline risk assessment. The model takes into account multiple interactions between several failure parameters to reduce the risk of pipeline failure. Such parameters include human factors (e.g., third party intervention and operation damage), mechanical factors (e.g., corrosion and material defect) and natural hazards. The main focus of the research is the construction of a model that shows the influence of the multiple parameters and their interactions resulting in a pipeline leak or rupture. The model enables the pipeline stakeholders and operators to determine those parameters or interventions that have the most impact on the reduction in pipeline loss of containment as part of the risk management. The novelty of this work is the integration of both the objective and subjective data, and the explicit accommodation and treatment of the sparse and incomplete local data into the failure likelihood analysis. The model, therefore, provides the managers with dynamic information on how to prevent undesired outcomes as part of a safety management plan.
The model analyses pipeline failure risks under uncertainty. However, it can also be used to focus on a sub-threat arising from the third-party activities, for example, in order to gain a wider understanding and to identify an effective combination of risk reduction and intervention factors.

Keywords: Bayesian Networks, Failure Likelihood, Cross-country Pipeline System, Risk Assessment, Failure Factors, Third Party Damage

[^0]
[^0]:    ${ }^{1}$ s.i.hassan@2017.ijmu.ac.uk
    ${ }^{2}$ j.wang@ljmu.ac.uk
    ${ }^{3}$ c.kontovasi@ljmu.ac.uk
    ${ }^{4}$ m.b.bashir@ljmu.ac.uk

# 1. Introduction 

In many countries, the oil and gas pipeline industry have a structured process of failure data collection, which informs the failure probability analysis as part of the process safety management. However, in developing countries where data is either unavailable or unreliable, this kind of analysis may produce unreliable results. This, in addition to peculiar local environmental and other conditions, leads to higher-than-average pipeline failure scenarios. These scenarios can escalate into catastrophic events leading to a significant loss of life, on top of the economic loss [1,2]. For example, according to Nigeria's premier oil company, the Nigerian National Petroleum Corporation (NNPC), Nigeria is reported to have lost about 22 million barrels of oil due to pipeline theft in the first half of 2019 [3].

To ensure a more reliable assessment of the likelihood or probability of failure which informs the pipeline risk assessment process, a Bayesian Network (BN) model is adopted as outlined in Section 3. This approach can accommodate data uncertainty or lack of data by utilising experts' judgement. The model is especially useful at updating the uncertainty whenever new data becomes available.

## 2. Literature Review

Identification of the probability or likelihood of a pipeline failure is required as part of the risk assessment process; see BSI [4] and DNV [5]. Several studies have assessed the probability or likelihood of pipeline failure where data is lacking or is unreliable, including [6-13]. The models used vary, from Analytic Hierarchy Process (AHP) to Fuzzy Rule Base. However, they all have one commonality, namely trying to address lack of knowledge and uncertainty as part of the pipeline risk assessment process. For instance, Dey [13] and Al-Khalil et al. [11] used expert judgement and AHP to develop a risk-based cross-country pipeline failure analysis. The studies identified and categorised pipeline failure modes and used expert elicitation to assess and rank the pipeline risks. Experts were invited to score the likelihood of failure and the associated cost implication. The input is used to assign weights to the pipeline segments, allowing for assessing relative exposure and ranking of each pipeline segment. The ranking also forms the basis for pipeline failure repair budget and prioritisation.

However, much of the literature does not address many of the challenges faced by pipeline operators and, especially, those in developing countries. These include the interactions of multiple influencing factors, lack of knowledge and data, uncertainty related to vagueness, randomness, and ignorance. For instance, whilst fuzzy set theory can be used to deal with vagueness, it lacks the ability to conduct inference inversely. Approximate reasoning approaches are strictly unidirectional, that is, when a model is given a set of inputs, it can predict the output, but not vice versa. This may have a limitation on the flexibility of a safety assessment method that focuses on exploring causal relationships among risk factors [14]. Additionally, these approaches assume a direct event-consequence inference. This is true under certain circumstances, where a rate of pipeline leak consequence is directly linked to, for example, corrosion event. However, recent developments in many developing countries indicate that the relationship is often indirectly related. Increase in the rate of pipeline leaks and the period of political electioneering are an example of such indirect relationships.

Unlike rule-based and other similar approaches, the use of Bayesian Networks allows the user to replicate the main features of reasoning inference in a consistent, efficient, and mathematically sound way. In addition, the beliefs can be updated when new evidence becomes available, which can be used to infer causality from consequence events. As an implementation of probability theory, BN is a powerful tool both for graphically representing the relationships among a set of variables and for dealing with the uncertainties related to such variables.

BN modelling has been used in different domains by many researchers, including in oil and gas as part of the process safety regime to assess and prioritise failures of safety systems under uncertainty. A number of researchers [14-20] have used BN models for a dynamic risk-based offshore pipeline safety and integrity assessment. While the rest of the researchers applied only the BN model, Adumene [20] used an integrated model of BN-Markove Misture (MM) with Monte Carlo simulation for operational safety assessment of pipelines with multiple Microbiologically Influence Corrosion (MIC) defects. Sulaiman and Tan [15] used a North Sea subsea pipeline as a case study, where there are historic data going back several decades. However, the work relies mostly on expert elicitation due to the unsuitability of those data. The use of the BN has also been shown to be effective in identifying influencing factors leading to third party damage to the pipelines [21-26]. While the majority of the researchers assessing third party damage limit their work on unintentional third party damage, [21] extended their model using game theory to assess malicious damages. The incessant pipeline damages and resultant consequences of fires, explosion and environmental pollution due to malicious third-party events in Africa have been widely investigated [27-29]. The European pipeline database also shows an astronomical increase in the pipeline third-party damage due to intentional purposes, from two incidences in 2012 to 87 in 2015 [30].

Research on corrosion prediction of the pipeline has been reported mostly using numerical methods such as Monte Carlo simulation. However, BN has also been employed to predict pipeline corrosion with promising results [31-34]. Abubakirov [31], for instance, used Dynamic Bayesian Network (DBN) to estimate both internal and external corrosion damage and assess the probability of failure to support inspection intervals optimisation. Kim et al. [34] used small observation and simulated data, and applied time-dependent generalised extreme value distribution and Bayesian inference to predict corrosion depth distribution on pipelines. The results indicate a good prediction of the defect distribution by incorporating the observation data in the form of prior distribution.

The use of BN to identify and analyse failure factors for gas pipelines under uncertainty has been reported by various researchers [35-39]. They used the incident databases to identify and investigate loss cases, and together with the pipeline characteristics developed the BN model outlining the failure incident evolution and built a relationship between variables. The researchers show that the BN developed was able to perform probabilistic inference and belief updating to predict failure frequency. However, the researchers utilised failure data mainly from European and US databases and applied it to their case study region without assessing the suitability of such data with respect to the local environment including consideration for management systems and human factors. The study did not indicate whether any expert elicitation has been carried out to put the data into context with respect to the case study pipeline and the region that it has been applied.

The risks of tank stations and pumps have been assessed using BN [40-44]. Zarei et al. [43] used a bow-tie to develop a BN model as part of the accident scenario modelling for conditional dependencies and risk updating of natural gas stations. The BN approach facilitates the model development in which part of the needed information as a priori is available in measured data and functional relations or as expert knowledge, and part is uncertain and unknown. The BN then serves data mining purposes for the unknown part which is then updated as a posteriori with the uncertainty reduced by a later experience or observations. Pasman \& Rogers [41] compared the risks of the $\mathrm{H}_{2}$ tank stations and that of the associated pipelines using BN.

Kabir et al. [45], Ren et al.[46] and Yang et al. [47] used a combination of fuzzy rule and BN to assess risks of offshore installations. Kabir et al. [45] used the combined model to prioritise the risk of collision between a Floating Production Storage and Offloading (FPSO) system and a shuttle tanker. The model first establishes the appropriate fuzzy rule base, estimates the failure factors using expert elicitation, conducts risk inference using fuzzy Bayesian reasoning and finally assigns utility functions to prioritise the failures. The model has been demonstrated to successfully utilise human knowledge to deliver risk criticality values in support of safety-based decision-making. The model, though, did not test the interdependence of the failure factors and how that may affect the model's sensitivity.

Khakzad et al. [48] investigated and compared BNs with fault tree analysis in safety analysis within the process industry. The study concluded that the BN technique provides better outcomes in safety analysis where data availability is at stake, due to its flexibility, allowing the assessment to fit a wide variety of accident scenarios.

The reviewed literature address some of the identified weaknesses of other models such as approximate reasoning and fuzzy rule base. It also assessed the application of the BN in oil and gas domains including subsea oil pipelines and urban gas distribution pipelines. However, they still do not robustly address the challenges faced by operators of cross-country pipelines in developing countries relating to availability and fidelity of failure data, uncertainty, the integration of the multitude and complex interdependence between different factors and interrelations of technical human and organisational malfunctions. Therefore, this study proposed new models that address those problems, including allowing for the effect of indirect relationship of the available variables. The main goal of the study is to develop a framework for the prediction of failure likelihood for cross-country pipelines through identification and assessment of the critical failure factors of oil pipelines. A case study of a cross country pipeline to analyse the contribution and the interaction between various factors leading to loss of contentment as a result of either a pipeline leak or rupture is presented. Pipeline failure likelihood and the interdependence of different failure factors are analysed to provide a comprehensive picture to support decision making. The use of BN has several advantages, such as the ability to integrate expert judgement and empirical data into the analysis. This is particularly useful in situations where data is absent, sparse or unreliable. BN's ability to deal with uncertainty by facilitating inference and allowing new evidence to be incorporated when it becomes available is particularly useful.

# 3. Background Theory 

### 3.1 Bayesian Networks Framework

BN is the graphical presentation of the Bayes' Theorem and has been developed from the conditional probability product rule. The Bayes rule is presented as shown below [49]:
$P(H \mid E)=\frac{P(E \mid H) \cdot P(H)}{P(E)}$
$P(H)$ is called the prior or marginal probability of $H$ and represents the state of knowledge of $H$ at the initial stage before the evidence is considered, whilst $P(H / E)$ is called the posterior probability and represents the updated knowledge given the evidence $E . P(E / H)$ is the likelihood (also referred to as the conditional probability) of $E$ given $H . P(E)$ is the marginal probability of $E$ and the evidence to enable $P(H)$ to be updated.

A BN is a Directed Acyclic Graph (DAG) that encodes the Conditional Probability Distributions (CPDs) of the underlying variables. A BN has two components, the physical graph structure that shows the interconnections between nodes and the quantitative part that encodes the probability distribution. Generally, a BN over variables $\boldsymbol{X}$ is a pair of $(G, \Theta)$, where [50]:

- $G$ is a directed acyclic graph over variables $\boldsymbol{X}$;
- $\Theta$ is a set of CPTs, one CPT $\Theta_{X \mid U}$ for each variable $X$ and its parents $\mathbf{U}$ in $G$. The CPT $\Theta_{X \mid U}$ maps each instantiation to a probability $\theta_{X \mid U}$ such that $\sum_{X} \theta_{X \mid \mu}=1$.

The upper-case letters represent variables, lower-case letters represent individual values and bold lower-case letters represent an instantiation of the values. The qualitative component of the BN is the DAG, which consists of nodes and edges. The nodes represent variables of interest and the DAG provides the directed influence amongst the nodes. The relationship is represented by the connecting edges with the arrow showing the influence direction. Figure 1 shows a BN example and the relationships between the nodes.
![img-0.jpeg](img-0.jpeg)

Figure 1: Example of a Bayesian Network

### 3.2 Conditional Probability Table (CPT)

Determining the prior probabilities for parent nodes $P(A 1)$ and $P(A 2)$ in Figure 1 is straightforward given hard data. However, it is not often straightforward to determine the conditional probability of the

children node given the influence of the parent nodes, that is, $P(B \mid A 1, A 2)$. The Bayesian Theory approach would require the prior probability details for the distribution to be provided which sometimes could be obtained via field data or historical cases. In reality, however, this is difficult, especially in geographical areas where the basic data is often not available or not reliable and detailed data to form prior probabilities is rare. Even where data is available, it is often not suitable as an input into the BN analysis. To overcome the unreliability or lack of data, the subjective probability distribution is relied upon, often provided by expert elicitation using AHP, or similar models, to represent the experts' degrees of belief.

Different methods have been proposed to address the conditional probability distribution, including Noisy-Or [51] and symmetric methods [52]. A symmetric method will be adopted in this work as outlined in Section 3.2.1. The symmetric method is better suited for this research as it addresses some of the problems encountered when using the Noisy-Or method. The problems include its inability to consider multiple causes for the presence of a child node (leaky Noisy-Or is supposed to address that problem) and the fact that the model is asymmetric in nature, that is, it is only true in one direction.

# 3.2.1 Symmetric Models 

The symmetric model provides input as a set of relative weights which maps the relative strength of the parent nodes as they influence child nodes. This is represented as a probability distribution table and grows linearly as the number of parent nodes increases. The symmetric model can take input either in the form of experimental data, expert opinion or a combination of the two.

The use of a symmetric model eases the input requirements for a CPT and ensure objective and consistent input. Assuming in Figure 1, the two parents nodes $A 1$ and $A 2$ have both three states of low $(L)$, medium $(M)$ and high $(H)$, whilst the child note $B$ has two states of yes $(Y)$ and no $(N)$, then the influence of one of the parent states over the child state can be represented, for example, as $P(B=\text { yes } \mid A 1=\text { low })=P\left(B_{y} \mid A 1_{l}\right)$ This is the probability of obtaining 'yes' for $B$ given $A 1$ is in the state of 'low'; all other states of $A 1$ are ignored.

Since the model distributes the expert's opinion on the relative importance of each parent to its associated child node (normalised weight), the normalised space $\left(P\left(B_{y} \mid \hat{A} 1_{l}\right)\right)$ stands for the relative importance of the first parent's state $L$ to the child node assuming all other states do not occur. Thus:
$\mathrm{P}\left(B=\right.$ yes $\mid A_{1}=l o w)=P\left(B / \hat{A} 1_{l}\right)=\frac{P\left(B / A 1_{l}\right)}{\sum_{i=1}^{n} P\left(A_{i}\right)}$
$\mathrm{P}\left(B=\right.$ yes $\mid A_{n}=l o w)=P\left(B / \hat{A} n_{l}\right)=\frac{P\left(B / A n_{l}\right)}{\sum_{i=1}^{n} P\left(A_{i}\right)}$
$\therefore$
$P\left(B / \hat{A} 1_{l}\right)+\ldots \ldots . .+P\left(B / \hat{A} n_{l}\right)=1$

The influence of an individual parent node on the CPT of the child node for each Boolean parent node $A r$ (where $r$ can be $1,2, \ldots . . n$ ) is obtained as follows:
$\mathrm{P}(B=$ yes $|A 1=$ low $)=\omega_{1}, \mathrm{P}(B=$ yes $|A 2=$ low $)=\omega_{2}, \ldots, \mathrm{P}(B=$ yes $|A n=$ low $)=\omega_{n}$
$\sum_{r=1}^{n} \omega_{r}=1$
Equations 2 and 3 can be combined, where there is symmetry (normalisation), to produce:
$P(B / A 1, A 2 \ldots \ldots . . A n)=\sum_{r=1}^{n} \varpi_{r}$
where:
$\varpi_{r}=\omega_{r}$ if the state of the parent node $r$ is identical to the state of the child,
$\varpi_{r}=0$ if the state of the parent node $r$ is not identical to the state of the child node.

# 3.2.2 AHP Pairwise Comparison 

To obtain the relative weight of the parent node (as it affects the child node), the AHP technique is used. The relative weight provides the input required to fill in the conditional probability tables in Section 3.2.1. AHP, introduced by Saaty [53], is an effective tool for dealing with decision-making, reducing complex decisions to a series of pairwise comparisons, and helping to synthesise the results. AHP can calculate a weight for each evaluation criterion based on the decision maker's pairwise comparison of each criterion against the others. The more important the criterion, the higher its corresponding weight.

The assessment involves assigning scores to each option in accordance with the decision maker's pairwise comparison of the options based on that criterion. Qualitative judgements from experts on each pair of attributes $A_{i}$ and $A_{j}$ are represented in a form of $n \times n$ matrix [54].
$A=\left(a_{i j}\right)=\left[\begin{array}{cccc}1 & a_{12} & \cdots & a_{1 n} \\ a / a_{12} & 1 & \cdots & a_{2 n} \\ \cdot & \cdot & \cdots & \cdot \\ 1 / a_{1 n} & 1 / a_{2 n} & \cdots & 1\end{array}\right]$
where $i, j=1,2,3, \ldots, \mathrm{n}$ and each $a_{i j}$ is the relative importance of attribute $A_{i}$ to attribute $\lambda$.
A weight vector, which indicates the priority of each element in the pairwise comparison matrix, is represented in Equation 6. The weight determines the overall contribution of each element to the overall goal of the decision-making process.

$\omega_{k}=\frac{1}{n} \sum_{j=1}^{n}\left(\frac{a_{k j}}{\sum_{i=1}^{n} a_{i j}}\right)(k=1,2,3, \ldots n)$
where $a_{i j}$ is the entry of row $i$ and column $j$ in the matrix of order $n$.
More details of the AHP are outlined in [53].

# 3.3 BN Software 

Due to the complexity of the BN calculations, several software packages exist to simplify the assessment, converting the numerical inputs into DAG visualisation for ease of understanding and analysis. Examples of such software include Hugin, BayesiaLab, GeNie, and AgenaRisk. For the case study in this work, Hugin [55] is adopted, which has been used widely both for research and field applications. The Hugin software can be used to make a higher number of nodes in BN modelling faster and error-free [51]. The graphical representation of the node properties in the software simplifies the process of network analysis and understanding the results.

## 4. Methodology

The methodology in this research is based on the combination of Bayesian Networks, AHP and Symmetric models. These have been used to obtain reliable assessments of the likelihood of failure. Figure 2 illustrates the main steps in building the model, including entering the CPT values (e.g., weights obtained using AHP pairwise comparisons or hard data) and obtaining the overall results to be used by the decision maker.

### 4.1 Construction of the Bayesian Network and Data Modelling

The first step in the assessment is to build the model. In order to do so, input from relevant past cases, literature and expert opinion have been used. To develop the nodes, a determination must be carried out of the parent or root nodes and the child or the target node. The root nodes are not directly influenced by any other node in the BN and it is defined as a level 1 node (first stage). Each child node is defined as a level 2 node (second stage) and the target node is defined as the level 3 node (third stage).

To analyse the primary pipeline failure data and predict failure characteristics using the BN model, a generic model building, and analysis procedure has been adapted and is explained in this section. The steps as outlined here are key to error-free analysis and form part of the quality control procedure that ensures that the model performs consistently as expected irrespective of the domain of application. It also ensures processes and results comparability.

The number of steps and the details contained vary from application to application and are also dependent on the level of modelling details envisaged. However, the basic procedure shares a similarity and has been adapted for this work as described below.

![img-1.jpeg](img-1.jpeg)

Figure 2: Flowchart of the methodology

# 4.1.1 Identification of Variables 

This step entails identifying the variables that are required in the model. In identifying them, care must be taken to ensure that the number is kept to the minimum that is necessary to provide expected results. In this research, the determination of the factors that affect cross-country pipeline integrity and loss prevention mechanisms is the main driver of the variables' development. To reduce complications and difficulties that will arise from unwieldy variables (and hence the data for the Conditional Probability Tables - CPTs), the number of the parent nodes for each child node is suggested to be limited (e.g., up to three). This ensures that all the identified major factors leading to pipeline failure are included whilst the number of variables is kept to the minimum in order for the assessment not to be complicated. The granularity of the analysis should be balanced with the practicality of the available information and the modelling effort.

### 4.1.2 Creation of Nodes Corresponding to all Variables Identified

Having identified all the variables, this step involves creating nodes that describe the problem to be addressed. The nodes represent the relevant variables, and their development involves a determination as to whether each node is discrete, continuous or if it has several states.

### 4.1.3 Identification of a Set of States for Each Variable

The states of each variable are to be determined based on the available data, the modeller's perspective and the complexity envisaged. The states of the nodes can be discrete, continuous or involving several states.

### 4.1.4 Specification of the State of Each Node

For this assessment, a Boolean state with the option of "yes" and "no" has been adopted. Only the

top-level node has three states - leak, rupture and operational. The use of three states as opposed to two that were used on other nodes is to mirror the major failure modes mostly associated with pipelines, that is, "leak" and "rupture". The "operational" state indicates that the pipe did not encounter any failure and is, thus, still operational.

# 4.1.5 Identification of Node Dependencies 

The identified nodes are connected to the influencing/influenced nodes via arc connections. This step creates the DAG that the BN relies on for information parsing and probability propagation. The nodes which represent the causes and effects are linked to one another via directed edges or arcs. The model ensures that the assessment nodes established are connected, as appropriate, to the variables identified, and that the levels of information propagation are correct.

### 4.1.6 Construction of Conditional Probability Table

A CPT for each node will be set at this step and can be specified based on either available data or expert elicitation. The number of probabilities required depends on the structure of the model.

In this research, the information that makes up the CPT is obtained from the Concawe database [30], the US DOT [56] and NNPC [57], among others. Where direct data is not available, expert elicitation using AHP and a symmetric model [58] are used to complete the CPT as described in Sections 2.2.1 and 2.2.2.

### 4.2 Analysis of the BN model

Once all the data required is provided, and the correct connections are made, the next stage is ensuring that all the values entered for the CPT are normalised so that each set of nodes has a sum total equal to 1 .

Based on the designed network and the data inputs the BN software package is then used to perform the necessary calculations. This includes extracting marginal probabilities and interrogating the data to extract the belief values for certain assumptions and inputs. The baseline model gives the marginal probabilities of the end event, given the various input conditions of the contributing variables. These baseline results can be interrogated further given additional evidence to observe the impact of that new evidence on the overall results. This can then be used for a "what if" scenario analysis to better understand the impact of each input variable or sub-variable.

Predictive, diagnostic and sensitivity analysis can also be carried out as part of the decision-making process and model validation to provide insight, supporting managers in predicting the consequences of certain decisions or the impact of a certain intervention. It can also help with post-accident analysis, where the failure is diagnosed to find the likely contributing factors leading to it.

### 4.2.1 Model Validation

To ensure that the BN model behaves as expected, a sensitivity analysis needs to be carried out. The aim is to test how sensitive the model is to the incremental or decremental changes to the inputs. A representative model will have a relative increase or decrease in the results for a similar increase or decrease in the input. A sound model with logical inference reasoning should be able to pass the following three axioms [59]:

Axiom 1: A slight increase/decrease in the prior subjective probability of each parent node should certainly result in the effect of a relative increase/decrease of the posterior probabilities of child nodes.

Axiom 2: Given the variation in subjective probability distributions of each parent node, its influence magnitude to child node values should be kept consistent.

Axiom 3: The total influence magnitude of the combination of the probability variations, from $x$ attributes, on the values should always be greater than that of the set of $x-y$ ( $y \in x$ ) attributes.

# 5. Case Study: Section 2B of Nigeria's cross-country pipeline 

The BN model methodology described in Section 4 is used in this research to demonstrate the model's practical application in onshore cross-country pipeline failure analysis as part of the operator's process safety management. The BN model incorporates a symmetric model and the AHP pairwise comparison technique to generate conditional probability tables for nodes with multiple parents where data is insufficient or not available. The proposed model is then analysed for prediction and diagnosis. Verification and sensitivity analyses have been carried out to ensure that the model is constructed correctly and behaves as expected. This provides a level of confidence in the model's analysis and the results.

### 5.1 Description of the Pipeline System

The BN model is applied to an onshore Nigeria cross-country pipeline, Section 2B, located in southwestern Nigeria shown in Figure 3. The total length of the system is circa 500km. The relevant pipeline connects Lagos (including the Atlas Cove import jetty) in southwestern Nigeria to Mosimi and terminating at Ilorin in north-central Nigeria. The system includes the Oil pipeline, Pipeline manifold, Pigging (pig launchers and receivers), Metering system, Pumps, Utility systems and Future tie-in connections. The pipelines are multiproduct systems for the supply of Premium Motor Spirit (PMS), Dual Purpose Kerosene (DPK), Aviation Turbine Kerosene (ATK) and Automotive Gas Oil (AGO). To ensure a safe operation of the pipeline, they are buried about one metre deep on average.

Pipeline 2B is representative of the country's pipeline system as a whole with respect to failure frequency, as it is in the middle quartile overall in the failure records across the country. The pipeline has a high level of reported loss of containment with the associated consequence of fires and explosions. The last fire and explosion resulting from pipeline 2B failure was in March 2020 which caused about twenty-three fatalities and destroyed buildings and structures within about a hundred thousand square meters [1].

![img-2.jpeg](img-2.jpeg)

Figure 3: Onshore Pipeline Map - Case Study System is pipeline between Lagos and Ilorin (Source: [28])

The case study is a continuation of previous work [60], where a modified FMEA approach has been utilised to identify and rank all potential failure modes for the pipeline system. The failure mode that ranks highest is the pipeline's loss of containment due to a leak or rupture.

# 5.2 Events Flow 

To identify the initial variables for the modelling, an assessment of the primary failure factors that affect onshore oil and gas pipelines, both globally and locally in Nigeria, has been carried out. As a result of incomplete information on pipeline failure factors for Nigeria (and this is also the case for other African countries), the European and American data is used to augment the primary failure factors that will inform the variables. The databases on data in these regions for the onshore crosscountry refined products pipelines are the most relevant. There are some issues related to the terminology and differences in recording techniques, but the main failure factors are broadly similar and are grouped under tier 1 factors, listed in Table 3, that lead to a pipeline leak or rupture.

For a pipeline to fail, there is either going to be (i) a human interference consisting of a third-party or operational damage, (ii) a mechanical failure consisting of corrosion and a material defect or (iii) a

natural hazard. These are the tier 1 factors. Directly beneath each of the tier 1 factors are tier 2 factors. The root events (tier 3) are the basic failure factors. These are outlined in Table 3 (based on the US DOT and EU Concawe databases).

A qualitative assessment carried out and the opinion of the experts sought as part of this BN model development indicate that the Concawe database [30] is more appropriate for Nigeria's pipeline system, compared to the US DOT database [56], and, therefore, the Concawe nomenclature and the majority of its data has been used in this work.

Table 1: Primary and Secondary Pipeline Failure Factors


# 5.2.1 Model Structure 

The developed BN model shows the relationship between failure factors and their conditional dependencies. The BN simulates the cause and effect of pipeline failure and the various factors affecting it, including mechanical factors, corrosion damage, human and organisational failure, and third-party damages. The representation of the Bayesian model is shown in Figure 4. The description of all nodes and their states is given in Table 4.

![img-3.jpeg](img-3.jpeg)

Figure 4: Hugin Graphical Output of the BN Model
Table 2: Variables used in the BN and their Descriptions



# 5.3 Parameter Estimation 

### 5.3.1 Pipeline Failure Data

The pipeline failure data relevant to the pipeline system under consideration has been collected and used to inform the model. Nigeria's pipeline failure data has been collected from the pipeline operator which recorded the pipeline 2B loss of containment and its trend. However, the information contained in the database is incomplete and not detailed to support risk assessment when compared with established databases such as the UKOPA (UK Onshore Pipeline Operators Association) or Concawe. For example, the database recorded very few failure categories and is mainly geared towards assessing repair costs as opposed to recording failure details. Integrating the available local data with other relevant international data and expert elicitation could be revolutionary. In addition to Nigeria's available data, the other relevant data chosen for this assessment is the EU Concawe database [30]. Even though this database is for European cross-country pipelines our qualitative assessment and expert opinion indicates that it is the most relevant database to augment Nigeria's patchy pipeline failure data. The Concawe report [30] documents loss of containment incidents in European cross-country pipelines and their underlying statistics from 1971 to 2016. The report, which analyses the short and long-term trends of containment loss, covers over 140 pipeline systems provided by 66 pipeline operators, with a total length of about $38,000 \mathrm{~km}$ with a total throughput of $755 \mathrm{Mm}^{3}$ of refined products and crude oil. However, as the occurrence probabilities data for the fiveyear moving average is unrealistically low when adapted to developing countries like Nigeria, an average over 1971 to 2015 is used, which is more conservative.

Most of the failure factors identified and their long-term failure trends are deemed appropriate for use in this assessment in the absence of specific data for Nigeria's pipeline systems, with the exception of operational and third-party factors. For operational factors, the high quality of management regimes and supervision means that failure probabilities in the European pipelines are very low compared to those of Nigeria; the US DOT database for operational factors is more suitable in this instance.

Additionally, third-party intervention and especially theft/intentional and incidental damages are very low for both the Concawe and US DOT databases compared to the reported incidences for Nigeria. The patchy data obtained from Nigeria is very unreliable but seems to indicate that a significant

percentage, up to $90 \%$ of failures, is due to third-party intervention, specifically intentional and theft [57,61]. However, the domain experts consulted for this work, as outlined in Section 5.3.2, agreed that both the local data, and the Concawe data, which has an up to $60 \%$ reported failure probability due to third-party damage in 2015, should be used but adjusted.

In all other areas where direct data is not available, or if it is not applicable in the given context, expert elicitation has been adopted; see Section 5.3.2. Table 5 summarizes the data sources for each variable.

Table 3: Variables and Data Sources


# 5.3.2 Expert Elicitation 

A key strength of the BN method is that it allows for the use of subject matter experts in the absence of hard data. In this model, probability tables for some of the child nodes cannot be completed with the data available. As a result, expert opinion is used to compensate for the lack of data. Typically, the direct estimates from such experts for the nodes are elicited for the probabilities. However, this approach often leads to inconsistencies and unreliable results due to subjective biases, especially when a node has more than two states [62]. The experts also find it difficult to provide input for the high number of conditional probabilities in CPTs.

To address these shortcomings, AHP-based pairwise comparisons have been used. A questionnaire has been developed for the pairwise comparison for variables where expert input is required. The experts are selected based on their relevant experience and qualification. The backgrounds of the experts used in this case study are summarised in Table 6.

Table 4: Experts Selected for the Research


### 5.3.2.1 AHP Questionnaire and Pairwise Comparison

Expert opinion has been obtained for all children nodes where data is not sufficient to fill the prior probabilities. Questionnaires in the form of AHP and pairwise comparison have been utilised. Once questionnaire responses have been obtained, Equation 7 is used to assess the weight of each variable. A total for each column in Table 7 is required to assess the weighting. Each of the ratings in the table is divided by the total for each column. This gives the ratio of each rating as a percentage of the total for each variable as shown in Table 8. The indicative matrices for 'Material Defect' and 'Corrosion' are presented; the same approach is followed for other nodes as required.

To obtain the relative weighting for each variable, the average weighting across the row of the matrix is calculated as shown in Table 8. The average weightings are the values required along with the symmetric model to populate the node probability table of each respective child node.

Table 5: Pairwise Comparison Matrix


Note: DF is a design fault, CF is construction fault, MQ is material quality EC is external corrosion, IC is internal corrosion, and SC is stress cracking.

Table 6: Standard Matrix Relative Weighting Calculation


However, to ensure that the above assessment has been carried out in compliance with the AHP procedure and that the results are within the acceptable consistency bounds, a consistency check using the Cl criterion is carried out. All Cl values obtained are less 0.10 , passing the consistency check.

# 5.3.2.2 Symmetric Method and Relative Weight Development 

Determining the conditional probabilities requires filling out the CPT, using the symmetric model and relative weight development that has been introduced in Section 3.1.6. The application of the symmetric model in the CPT development is shown below, for the two example nodes - 'Material defect' and 'Corrosion' - to illustrate the process. The required input for the assessment includes the failure probabilities of the parent nodes, obtained from historical data, and the AHP pairwise comparison, derived from the expert elicitation. The AHP pairwise comparison method has been used to identify the relative influence of each parent node to the associated child node. That relative influence is shown as the average weighting in Table 9. The average weighting of each variable is multiplied with its failure probability to obtain the variable's specific importance. This is then used to calculate the symmetric method weighting $\omega_{r}$, and that would be the input value for the CPTs of the child nodes. In all cases, $\hat{\sum}_{i=1}^{n} \omega_{i}=1$ where $n$ is the number of decision factors. Table 9 shows the process and the results for the child nodes material effect and corrosion.

The sum of the relative weights for each of the two variables is:
$\sum_{r=1}^{n} \omega_{r}($ material defect $)=\omega_{1}+\omega_{2}+\omega_{3}=0.395+0.209+0.395=1$
$\sum_{r=1}^{n} \omega_{r}($ corrosion $)=\omega_{1}+\omega_{2}+\omega_{3}=0.312+0.499+0.189=1$
From the values calculated in Table 9, and using Equation 5, the node or conditional probability table is completed, as shown in Table 10. The values for material defect (MD), are arrived at as below, for a probability of material defect leading to pipeline failure being 'yes'. The probability for 'no' is 1 minus that of 'yes'.

Table 7: Symmetric Method Relative Weight for Variables


Note: The occurrence probabilities for the main failure factors - material defects and corrosion - are obtained from the data (1971 to 2015) in Concawe [63], which is more conservative than the five-year moving average. The failure probabilities for the variables (e.g., DF and CF) are derived by weighting each sub-variable, based on its recorded failures, against the main factors' failure probabilities.

Table 8: Node Probability Table for Material Defect and Corrosion


# 5.4 Analysis and Validation of the Model 

The model has now been built, and all prior probabilities have been computed based on the failure data and the AHP pairwise comparison method applied. Figure 5 shows the BN nodes for the probability of a pipeline failure, including its marginal probabilities.

The BN shows that the likelihood of pipeline failure resulting in full rupture is $7.51 \%$ per year whilst that of a leak is $14.72 \%$ per year. The leak likelihood being double compared to that of a rupture's likelihood is not surprising because the biggest threat to oil pipelines in Nigeria is theft due to drilling intended to create a tapping point on the pipeline [64]. The other threat is the deliberate destruction of the pipeline system by insurgency, which is rife in the country for political and socio-economic

reasons [65]. This results provide a baseline failure likelihood for the system based on the information gathered. It also provides interrelationships between different factors leading to either a leak or rupture incident. However, the power of the BN model is in providing managers with a tool to carry out a "what if" assessment or investigate past incidents to gain insight into the likely contributing factors that led to the incident.

To assess the robustness of the model, predictive, diagnostic and sensitivity analyses have been performed.
![img-4.jpeg](img-4.jpeg)

Figure 5: BN Model Showing Marginal Probabilities for Pipeline Failure

# 5.4.1 Evidence Propagation 

In undertaking BN model analysis, certain assumptions are made, and certain inputs are provided based on data that may not be directly relevant to this particular case. Evidence propagation allows the analyst to observe changes in the probability distribution if some of the assumptions were to be amended, either in isolation or in combination with other changes. For instance, in order to find out what combinations of factors must be avoided, different scenarios and combinations of events can be propagated as new evidence and compared with the baseline probability distribution. Figure 5 shows that human-related intervention has a higher failure likelihood on the selected Nigerian pipeline system, with a $30.76 \%$ failure likelihood, compared to mechanical failure which has a value of $4.19 \%$ and natural hazards which have a value of $0.75 \%$. The operator might wish to model different scenarios related to, for example, increased security to prevent criminal activities (such as the destruction of pipelines) or to test the effect of ageing pipelines. To estimate the pipeline failure probability, two hypothetical scenarios are examined:

Scenario 1: the government's effective security policies and political intervention result in a significant drop in third-party intervention due to intentional and incidental damages. This scenario will assume a best-case scenario of a $5 \%$ factor for those variables compared to the baseline model.

Scenario 2: the ageing pipeline may deteriorate further with time, resulting in increased cases of corrosion failure and material defect. This scenario assumes a worst-case scenario of a $90 \%$ failure probability for these factors, compared to the baseline.

Table 11 shows the baseline model input and the results for the two scenarios, i.e., the probability that the pipeline remains operational ( O ) and occurrence probabilities for leaks ( L ) and rapture ( R ). The baseline model results indicate occurrence probabilities of $14.72 \%$ for leaks and $7.51 \%$ for ruptures. The pipeline remains operational $77.77 \%$ of the time. Scenario 1 results (best case) indicate the level of loss reduction that is possible if efforts were to be made to reduce the occurrence of the two factors - theft and incidental damages. A reduction of up to $75.00 \%$ and $55.00 \%$ for leaks and ruptures is possible if the occurrence probabilities of theft and incidental damages can be reduced from the baseline $30.00 \%$ and $22.00 \%$ down to $5.00 \%$ and $5.00 \%$, respectively. The leak and rupture probabilities are reduced from $14.72 \%$ and $7.51 \%$ to $3.90 \%$ and $3.30 \%$, respectively. The pipeline availability increases from $77.77 \%$ to $92.80 \%$.

Table 9: Evidence Propagation


For scenario 2, which assumes a worst-case scenario of progressive pipeline deterioration due to ageing and lack of maintenance, the availability of the pipeline drops significantly, from $77.77 \%$ to $39.80 \%$. The scenario assumes a $90.00 \%$ occurrence probability from a mechanical failure, which

encompasses material defect and corrosion. All other factors remain the same. The occurrence probabilities for leaks and ruptures jump twofold and fourfold from $14.72 \%$ and $7.51 \%$ to $27.30 \%$ and $32.90 \%$, respectively.

From the above analyses, the importance of evidence propagation in decision-making and forecasting is clear. Our methodology allows the decision-maker to assess a great combination of what-if scenarios in order to examine their impact on the operation of the pipeline system. This will help direct scarce resources into areas where they will have the most impact.

# 5.4.2 Posterior Probabilities Assessment 

The main advantage of BN modelling is its ability to support the decision-making process by allowing for an update to the model in the presence of new observations or evidence. That evidence can be propagated in either direction.

However, diagnostic analysis, which is the determination of the posterior probabilities of the parent nodes given new evidence for the child node, is the most popular [48]. Therefore, diagnostic analysis inference will be used to calculate the posterior probability distribution of each risk factor in the case of a confirmed pipeline failure.

The first part of the diagnostic analysis assesses the impact of given evidence for the pipeline failure node on its parent nodes. The effect of such evidence can easily be propagated backwards to see which of the parent nodes has the most impact on the confirmed condition of a pipeline. Two different pieces of evidence have been propagated - a confirmed pipeline leak (probability of leak equal to 100\%) and a confirmed pipeline rupture (probability of rupture equal to 100\%). Figure 6 and Figure 7 show the BN model with both leak and rupture evidence inserted. The new occurrence probabilities for the parent nodes - human, mechanical and natural hazard - as a result of the evidence are also shown. For comparison, the baseline model occurrence probabilities are $30.76 \%, 4.19 \%$ and $0.75 \%$ for human damage, mechanical failure and natural hazards, respectively.
![img-5.jpeg](img-5.jpeg)

Figure 6: Posterior Probabilities for Parent Nodes Given Evidence of a Leak

From Figure 6 and Figure 7 the impact of new evidence on the parent node is clear, with the highest change affecting human intervention, which increases from 0.31 to 0.96 for a confirmed leak and from 0.31 to 0.80 for a confirmed rupture. This shows, counter-intuitively, that the impact of human intervention resulting in a pipeline leak is greater than such impact resulting in a pipeline rupture. This can be explained by the fact that the human intervention factor is skewed by a disproportionate failure rate due to third-party theft/intentional intervention, and there are more incidents of theft via hottapping than there are for the intentional destruction of the pipelines for political reasons.
![img-6.jpeg](img-6.jpeg)

Figure 7: Posterior Probabilities for Parent Nodes Given Rupture Evidence
Conversely, the occurrence probabilities of both mechanical failure and natural hazards have been affected more by new evidence due to a confirmed rupture than due to a confirmed leak, as shown in Figure 6 and Figure 7. There is a twofold increase for a leak and fivefold increase for a rupture for both mechanical failure and natural hazards, respectively. Unlike human damage, the contribution of primary variables to the change of failure probability spreads amongst both the corrosion and materials defect factors and not skewed by a single factor.

Figure 8 and Figure 9 shows how the new evidence only accentuates the contribution made by the largest three factors to the overall failure probability. For the baseline model, the three largest primary failure contributors are theft/intentional damage (22\%), incidental (18\%) and external corrosion (8\%). Upon new evidence of a confirmed leak, the contribution of theft/intentional damage to the overall failure probability jumps to $65 \%$, that of incidental damage to $32 \%$ and that of external corrosion to $10 \%$.

The results obtained in this analysis are generally in agreement with the Concawe database [30], with the exception of the outsized contribution of theft or intentional damage and incidental damage. These are particularly high due to the peculiar challenges resulting from a prevalence of criminality and politically motivated actions in Nigeria. The European pipeline database also shows an astronomical

increase in third-party damage due to intentional actions, from two incidents in 2012 to 87 incidents in 2015. The prevalence of incidental damage has not seen any increase in Europe, but it has seen an increase in Nigeria due to a significant population increase over the past two decades and encroachment into the pipeline's right of way due to weak implementation of the law. The encroachment into the pipeline's right of way, including construction activities and farming, increases the likelihood of damages occurring, which subsequently lead to pipeline loss of containment.
![img-7.jpeg](img-7.jpeg)

Figure 8: Primary Variables' Posterior Probabilities Given Leak Evidence

![img-8.jpeg](img-8.jpeg)

Figure 9: Primary Variables' Posterior Probabilities Given Rupture Evidence

The revised failure probabilities due to new evidence can be further interrogated by providing additional evidence. For example, given the assumption that a leak is more likely to occur as a result of intentional damage, inserting a $100 \%$ chance of failure due to intentional damage reduces the failure probability contribution of other factors; the incidental damage contribution is reduced from $18 \%$ to $10 \%$, whilst external corrosion reduces from $8 \%$ to $6 \%$. This intercausal inference attempts to explain the contribution of other variables by reducing their failure rates in place of plausible reasons to assume one variable caused the incident.

The main benefit of diagnostic analysis is affording fault diagnosis and investigation by identifying the variables that are more likely to contribute to a pipeline failure. Additionally, the diagnostic analysis can be used to identify factors that will likely cause a certain failure in the future, hence concentrating the mind of the operator on what to focus on. By performing these analyses, the posterior joint probabilities of all the variables, given new evidence of an event, are very useful for safety evaluation. Additionally, the causal path of an accident can be identified using this model, thus reducing the need for dependence on subject matter experts at all times.

# 5.5 Sensitivity Analysis 

Sensitivity analysis measures the sensitivity or responsiveness of the model's results to a variation of the inputs. The accuracy, robustness and reliability of the model are linked to the posterior probability distribution for changes to the input of the likelihood value. Sensitivity analysis offers the confidence that is necessary to show that the model is built correctly and produces results that are within the bounds of reality. This section examines the BN properties by applying incremental changes to the

likelihood input values and observing the output values to ensure that it follows a similar trend. As outlined in Figure 9, the most influential variables have been identified and they will assist in the analysis, as they will affect the model more than other variables with insignificant influence on the model.

Parameter sensitivity or one-way sensitivity analysis has been used for this analysis and this is incorporated into the Hugin software. The sensitivity function is such that the causation probability $P_{C}$ is a function of the parameter $z=P\left(Y=y_{i} \mid \pi\right)$ where $y_{i}$ is the one state of variable $Y$ and $\pi$ is the combination of the states for Y's parent nodes [66]. The sensitivity analysis is carried out by selecting the hypothesis variable (in this case a pipeline failure), the desired state(s) of the hypothesis variable (in this case a leak) and finally selecting the parameter variable. The parameter variables can be parent nodes of the hypothesis variable or they can be any other nodes whose input variation will influence the outcome of the hypothesis variable. For the parameter variables, the primary failure factors have been chosen and only the yes state is assessed.

Figure 10 shows the sensitivity graph of various variables against pipeline failure (leak). When assessed against the three axioms outlined in Section 3.2.1, it can be seen in Figure 10 that a slight increase and decrease in the prior probabilities of the parent node, $3^{\text {rd }}$ party damage, results in a relative increase and decrease in the child node, human factor. Also, the magnitude of the influence of the parent node, $3^{\text {rd }}$ party damage, to the child node, human factor, remains consistent for the assessed input variation.
![img-9.jpeg](img-9.jpeg)

Figure 10: Sensitivity for Pipeline Failure (Leak) Against Other Variables

Figure 11 shows a graph of sensitivity analyses output for the given evidence. It can be observed that theft/intentional damage has the highest sensitivity value implying that the incremental increase of this variable results in the greatest influence on the outcome of pipeline failure. This aligns with the outcome of the analysis in Figure 9, where the posterior probability distribution for theft is shown as the largest and the most significant influence for any new evidence entered in regards to pipeline failure.

Sensitivity Analysis for a Pipe Leak
![img-10.jpeg](img-10.jpeg)

Figure 11: Sensitivity Values for Given Evidence

# 6. Discussion 

This research analyses onshore cross-country oil pipeline failure due to a leak or rupture, which is ranked as the most common factor for loss of containment for the pipeline system 2B [60]. The BN model looks at this failure mode in detail, including all the initiating failure factors, that is, the contributing factors behind a pipeline leak or rupture.

Identifying and inserting conditional probabilities for the primary failure factors is straightforward. However, specifying marginal probabilities for the CPTs of the child nodes is challenging in the absence of relevant data. Generally, the CPTs are filled using elicitation of domain experts. This is not usually simple if the node has multiple states or multiple probability tables, as it burdens the experts and is prone to biases. To address this shortcoming, both the AHP pairwise comparison method and the symmetric model have been adopted to generate the CPT by synthesising the experts' opinions. This approach ensures that the seeming weakness of the BN is addressed.

The formulated BN model has been used to show the contributing factors behind pipeline failures and their interrelationships. The model, therefore, provides managers with dynamic information on how to prevent undesired outcomes and can be used for a safety management plan.

Figure 5 shows the predictive analysis, which outlines the marginal occurrence probability of the loss events. Figure 6 and Figure 7 outline the diagnostic analysis, which shows the significant failure factor that contributes towards the pipeline failure. The human damage node is shown as the parent node that has the most influence on the rupture state of the pipeline failure node. The human related

activities include failure due to operations such as system malfunction and human error. It also includes third-party activities such as theft and incidental damage. The three largest contributors to the failure probability are theft, incidental damage and external corrosion.

The results obtained in this analysis are generally in agreement with the Concawe database [30], with the exception of the outsized contribution of theft or intentional damage and incidental damage. The outsized contribution of the theft and incidental damage led to higher reported failure frequency, in km-years, for the 5 year average to 2015 of 6.0E-01 compared to Concawe (9.50E-04) or UKOPA (1.08E-04).

Table 11 shows the evidence propagation in the presence of new information, for example, if the operator wants to assess the impact of certain actions or spending on pipeline integrity improvements. It shows that if the third party and incidental damage probabilities were to be reduced, from $30.00 \%$ to $5.00 \%$ and from $21.60 \%$ to $5.00 \%$, respectively, this would lead to a reduction in the hypothesis variable, by fourfold for leak and twofold for rupture. On the other hand, if the material defect and corrosion probabilities were to be increased from $6.20 \%$ to $90.00 \%$ and from $3.80 \%$ to $90.00 \%$, respectively, the hypothesis variable will see an increase in failure probability. This jumps from $14.72 \%$ and $7.50 \%$ to $27.30 \%$ and $32.90 \%$, respectively.

Model validation and sensitivity analysis have been carried out to ensure that the model has been built and is operating within the bounds of expectation. As indicated in Figure 10, theft/intentional damage is found to have the most influence on the leak failure state of the pipeline failure variable. The sensitivity analysis shows that the BN developed to help in pipeline failure identification decisionmaking is reliable and accurate, although the accuracy can be improved with more objective data.

It is worth noting that the application of the Bayes' rule in risk analysis and uncertainty propagation has its drawbacks and limitations, as espoused by Ferson [67], including the inadequacy of the Bayesian model of ignorance which does not distinguish between incertitude and equiprobability. Also, the consequent overconfidence of conclusions that are derived by the analysis can hide a number of assumptions embedded in the assessment. Finally, there is a lack of wider acceptance of using subjectivity in public policy decision making, which may hamper its wider adoption in the industry.

# 7. Conclusions 

Managing safety and risks for oil and gas pipelines especially in developing countries is becoming a challenge due to the increasing number of failures often from third party activities. In Nigeria, the safety concerns of such pipeline failure resulting in injury, loss of lives, environmental damage and loss of revenue are occupying the mind of the stakeholders. The main challenge of addressing such safety concerns is the uncertainty resulting from inadequate data, socio-economic and political factors, among others. The use of BN as part of the process safety and risk management of those pipelines especially to address the lack of or unreliability of the data by incorporating the existing scarce data, literature and expert's elicitation can be revolutionary.

The BN model described in this paper enumerates the cause and effect relationship that can be established between failure factors and pipeline failure conditions for the pipeline systems where there is inadequate or unreliable data. The model has been applied to a case study of Nigeria's cross country pipeline system - 2B to estimate their failure probabilities. The research focussed on the model construction that shows the influence of the multiple parameters and their interactions resulting in a pipeline leak or rupture.

The results of the analysis have shown the three largest failure factors that contribute towards the pipeline failure for the case study pipeline are deliberate third party activities, incidental damage and external corrosion. The analysis has also shown how an end-user can assess and measure the relative effectiveness of interventions and spending on pipeline integrity improvements and control measures. Example of control measures include detection measures (such as leak detection/impact monitors and patrol), prevention measures (such as Supervisory Control and Data Acquisition (SCADA) and barrier), and mitigation measures (such as spill response and right of way control) [68].

Managing risks of pipeline systems in developing countries often involves a high level of uncertainty due to inadequate data, socio-economic and political factors, among others. The operation of pipelines in such circumstances where failure due to technical, human and organizational factors may contribute to a range of possible accidents requires a new approach to address those identified challenges.

This work helps to address those challenges by analysing the refined petroleum products pipeline risks and examining the multiple interactions between several failure factors and their likelihood in causing a loss of containment. A case study of a pipeline system in Nigeria has been used to show how the model can be applied. The assessment carried out in this research can provide the operator with tools to be used to predict pipeline integrity issues and diagnose recent loss events to identify the most likely responsible failure factors.

The assessment can also be used to update the degree of beliefs given any new information or evidence. The predictive analysis serves to provide valuable information during the design and operation of the system and helps in directing resources to the factors with the most influence on a particular integrity issue. The diagnostic analysis helps to determine the critical failure factors that may lead to a catastrophic loss event. The diagnostic analysis can also help with the identification of an accident event path.

The model accommodates subjective judgements from experts and allows for beliefs updates for given information, making it ideal for operators to keep updating their uncertain parameters as more data becomes available. It is expected that the model will assist decision makers in identifying and ranking failure factors for effective risk mitigation, taking into account the local conditions.

The novelty of this research is that instead of relying solely on the European and US databases in absence of a reliable database in Nigeria, the work integrates the subjective expert's elicitation in addition to accommodating the available Nigerian data. This helped to put the assessment in context, including consideration for the management systems and human factors, with respect to the case study pipeline and the region where it has been applied.

The key advantage of the model is its ability to incorporate both objective and subjective data; this is important for developing countries, where historical data is often unavailable or not reliable. The use of subjective data obtained using experts' elicitation ensures that the results reflect the local industry best practices and experience.

The work has shown how the BN model can be applied as a part of the package of tools to quantify failure factors and minimise uncertainty in carrying out process safety analysis for onshore crosscountry oil pipelines, particularly in developing countries where data availability and reliability is often a challenge.

The BN model developed has limitations, such as the incorporation of only two states for most of the nodes, either 'yes' or 'no'. This became necessary in order to reduce the complexity of the CPTs within the nodes and due to the lack of data required to fill in complex CPTs. However, this approach limits the model in many ways and also limits the validation and verification process.

The BN model developed required CPT construction, which in this analysis used AHP and the symmetric method in the absence of hard data. The symmetric method is one of several methods that could be used to construct the CPTs. A future work that uses other technique, such as the Noisy-OR, to build the CPTs to compare with the approach used in this work can identify which approach yields better results.

# Acknowledgements 

This research is partially supported by the Federal Government of Nigeria through the Petroleum Technology Development Fund.
