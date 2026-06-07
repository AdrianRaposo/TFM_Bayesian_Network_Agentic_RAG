![img-0.jpeg](img-0.jpeg)

# Entropy-Based Metrics for URREF Criteria to Assess Uncertainty in Bayesian Networks for Cyber Threat Detection 

Valentina Dragos, Juergen Ziegler, Johan Pieter de Villiers, Alta de Waal, Anne-Laure Jousselme, Erik Blasch

## To cite this version:

Valentina Dragos, Juergen Ziegler, Johan Pieter de Villiers, Alta de Waal, Anne-Laure Jousselme, et al.. Entropy-Based Metrics for URREF Criteria to Assess Uncertainty in Bayesian Networks for Cyber Threat Detection. 22nd International Conference on Information Fusion, Jul 2019, OTTAWA, Canada. hal-02988290

## HAL Id: hal-02988290 <br> https://hal.science/hal-02988290v1

Submitted on 4 Nov 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Entropy-Based Metrics for URREF Criteria to Assess Uncertainty in Bayesian Networks for Cyber Threat Detection 

V. Dragos ${ }^{*}$, J. Ziegler ${ }^{\dagger}$, J.P de Villiers ${ }^{\dagger},{ }^{\ddagger}$ A. de Waal ${ }^{\S}$ A-L. Jousselme ${ }^{\S}$, E. Blasch ${ }^{\text {, }}$,<br>* ONERA-The French Aerospace Lab, Palaiseau, France, valentina.dragos@onera.fr<br>${ }^{\ddagger}$ Competence Centres ISR, IABGmbH, Ottobrunn, Germany, jziegler@iabg.de<br>${ }^{\dagger}$ University of Pretoria, Pretoria, South Africa, pieter.devilliers@up.ac.za<br>${ }^{\ddagger}$ CSIR, Pretoria, South Africa, jdvilliers1@csir.co.za<br>${ }^{\S}$ University of Pretoria \& Center for Artificial Intelligence Research (CAIR), Pretoria, South Africa, alta.dewaal@up.ac.za<br>${ }^{\S}$ NATO-STO Centre for Maritime Research and Experimentation, La Spezia, IT, Anne-Laure.jousselme@cmre.nato.int<br>${ }^{\text {® }}$ Air Force Research Lab, Arlington, VA, USA, erik.blasch.1@us.af.mil


#### Abstract

Bayesian Networks are widely accepted as efficient tools to represent causal models for decision making under uncertainty. In some applications, networks are built where the conditional probability tables are not derived from scientific laws but rely on expert knowledge. Such applications require assessment as to whether the knowledge representation is precise enough to infer reliable results. The uncertainty representation and reasoning evaluation framework (URREF) ontology offers a unified framework for the objective assessment of uncertainty representation and reasoning. This paper addresses the analysis of uncertainty in Bayesian networks (BNs) and develops metrics for URREF criteria based on the principle of entropy. BNs uncertainty includes variable transformation (accuracy), model structure (precision), and reasoning (probability distribution interpretations). The set of metrics are used to investigate a practical use case for probabilistic modeling of cyber threat analysis, and are correlated to a set of complementary metrics already described in a former contribution. The goal of the paper is to provide a new set of metrics able to assess, for a specific model and given input sources, the quality of results of BNbased inferences, in terms of accuracy, precision and end-user interpretation.


Index Terms-cyber threats, Bayesian networks, knowledge representation, uncertainty, URREF ontology, simplicity, expressiveness, accuracy, entropy

## I. INTRODUCTION

Developing cyber threats detection systems is a challenging task, as those systems often include human elements, control procedures, complex failure mechanisms and a variety of dynamic interactions of components. Incomplete information and probabilistic representation of knowledge are generally prevalent in applications designed for cyber threat analysis.

A challenge when using Bayesian networks (BNs) is the construction and maintenance of the BN - i.e. the structure of the causal model (the graph), the conditional probability tables (CPTs) and possible a-priori distributions. For real life applications, BNs have hundreds of nodes and complex structures, with many nodes having multiple parent nodes.

This paper outlines the use of BNs for cyber threats detection while considering uncertainty as an important factor affecting the quality of results. Construction of BNs for threat detection requires to build a network structure with a set of CPTs and there are two main practical approaches: the first one performs variable selection, and the second one scores each variable.

From a practical standpoint, a useful BN is able to provide reliable results and is simple enough to be maintained and upgraded during its life-cycle. Uncertainties affecting a BN are typically associated with external factors (human sources, measurement accuracy), incomplete information and partial domain knowledge. The goal of this work is to characterize BN developed for cyber threat detection by estimating the quality of the model, the accuracy of inputs and outputs while using a BN that is simple and easy to handle. A pervasive uncertainty analysis highlights the quality of results by using metrics that are estimated every time the model is used in practice.

This paper tackles the characterization of BNs whose structure and CPTs are generated semi-automatically by using expert knowledge [1] and the joint analysis of uncertainties affecting various elements and stages of the BNs construction process. Uncertainty analysis is carried out using the uncertainty representation and reasoning evaluation framework (URREF) ontology http://eturwg.c4i.gmu.edu/?q=URREFv3 and metrics are defined following the concept related to the entropy of Bayesian networks.

The paper is organized into five sections. Section II describes the construction of BNs for cyber threat detection, motivates the use of URREF ontology for uncertainty assessment and discusses the selection of URREF criteria to be used for the use case. Section III reviews metrics introduced in a previous work, discusses the concepts related to the entropy for BN networks, describes the selection of additional uncertainty criteria and defines new metrics. Section IV illustrates the assessment of uncertainty applied to a use case on cyber

threat detection and empirically validates the results. Section V concludes the paper and sketches directions for future work.

## II. BAYESIAN NETWORKS FOR THREAT DETECTION AND UNCERTAINTY ANALYSIS

The detection of cyber threats was addressed in various studies using Bayesian-based approaches [2], [3] and complex frameworks for probability inference [4]. Several studies related cyber attacks detection to continuous [5] and dynamic situating awareness processes [6] in perceptual environments [7]. Those are reasonable choices because the most probable course of action may be deduced with probabilistic inference from one action to the next. There are several approaches to perform the generation and parametrization of CPTs: they can be defined manually, if the size of the network is not too large or its structure is not too complex [8] or they can be defined semi-automatically [1] thanks to a an expert intervention aiming at refining the model learned automatically [9]. For some applications, the CPT or even the structure of the model can be generated automatically, by using ontologydriven approaches [10], machine learning techniques [11] or structural equation modelling [12]. For the latter case, the entropy can also be used for parameter optimization during network construction.

Entropy has been used in several works as a metric for the construction and parameterisation of BNs [13]-[16]. Entropy assessment guides the overall network construction in [13] by adding arcs between nodes in an initial network, where all nodes are marginally independent, until some entropy threshold has been reached. The authors of [16] present a new rules for pruning sub-optimal parent sets in BN structure learning, thereby reducing the search space and also providing tighter bounds on the maximum number of parents of each variable. In some applications, the sensible discretization of continuous BN variables is not always clear. The authors of [14] use entropy by choosing a discretization which minimizes the information loss, relative to the number of intervals used to represent the variable. In [15] the maximum entropy method is applied to the CPT parameterization of BNs. However, owing to the way a BN factorizes a joint probability distribution, maximum entropy optimization constraints become non-linear and [15] provides a method for dealing with these nonlinear constraints.

From a different perspective, the URREF ontology defines criteria that are detailed enough to capture model-embedded uncertainties [17] or to compare different fusion approaches [18]. The frame was used for uncertainty analysis several applications: vessel identification for maritime surveillance [19] and imagery analysis for large area monitoring [20]. This paper fills the gap and introduces entropy-based metrics for URREF criteria able to analyze the quality of BNs developed for cyber threat detection.

## A. BN Model Generation for Cyber Threat Detection

The use case considered for this paper models possible attacks on various components of an aircraft and is focused on the assessment of possible risks caused by attacks to air craft passengers. The generation of the BN for cyber threat analysis is carried by following four steps (see [1] for details).

Step 1 - modelling objects and relations: several objects are selected to describe cyber threats for specific applications and their relations are identified. The selection is based on a standard for Cyber Threat Models, called STIX [21] and usually a subset of the so-called STIX-Domain Objects (SDO) and relations is used. The result is a domain specific model that is simple and intuitive enough so that domain experts can define the possible states of the SDO, describe relations and define qualitative values for weighted dependencies between the states. The possible qualitative weighting values are impossible, very unlikely, unlikely, unclear, probable, very probable and sure. For example, the use case highlights a dependency between the state Ego-attract attention of the attribute Actor-Motivation to the goal unauthorized access to in-flight entertainment system having the weight very probable.

The outcome of the first step is the expert model. For this work the following elements were defined: SDO threat actor (group, type, motivation, sophistication), tools (insider and physical resources) campaign-goals, attack pattern (action chains) and indicators (technical IT-based anomaly detection, IT derived and Open Source Intelligence (OSINT)) as illustrated in Figure 1. The arcs in the figure show dependencies of the elements.
![img-1.jpeg](img-1.jpeg)

Fig. 1. Simplified Expert Model

Attack pattern encode action chains which are represented by dependencies between different states of elements. Action chains in the model describe possible attacks on various elements of the aircraft internal software equipment. Several attacks require intruders or internal actors, since the equipment cannot be accessed from outside. The model assumes that the aircraft is operated by an airline having not only technical indicators integrated in the aircraft equipment, but also operating a Security Operation Center (SOC) which collects all anomalous information from aircraft in order to derive additional information (IT derived) and which is also equipped with OSINT methods to derive information (OSINT indicators) from internet sources (e.g., the dark net).

Step 2 - BN construction: a BN is generated automatically from the expert model using information about the exclusivity of states within the domain model. Qualitative values are translated into numerical values by using the method of scalebased information retrieval [22]. Prior values of states can also be defined in a qualitative way and translated by following this method. Steps 1 and 2 implement the semi-automatic model definition and generation of BN for threat detection. The BN of the use case contains more than 200 nodes, 300 arcs and 14,000 parameters. Several nodes have three or more parents.

Step 3 - Application: the BN model is applied to perform inferences and provide results about on-going cyber threats. Observations are used as evidences for the BN and can be provided by sensors in the IT system (e.g. intrusion detection systems, anomaly detection systems) or by applying intelligence methods for open sources processing e.g. to find information about activities of potential threat actors in internet. Additionally, assumptions about possible threats can be represented by adding additional priors. The BN is used to calculate state values (posteriors) in the BN and results are back-translated into the language of the expert model (qualitative results).

Step 4 - Testing: during this step a data set available for testing (evidences with the correlated ground truth) is used and results of inferences for the test data are compared to the ground truth.

Cyber threat detection using BNs relies on several steps (definition of the expert model, BN generation, cyber threat detection and testing), each involving specific types of uncertainty. From model generation to analysis of results, uncertainty induced by modelling decisions, quality of evidences, limitations of representation formalisms and end-user interpretation should be considered. URREF criteria can be used to capture specific aspects of uncertainty, and the goal of the overall uncertainty assessment is to analyze whether BNbased inferences provide reliable results in terms of accuracy, precision and end-user interpretation.

## B. Requirements for the application of the URREF criteria

The selection of URREF criteria is carried out by following several requirements:

- URREF criteria capture the effort needed to define the set of model parameters to be defined manually.
- URREF criteria support the assessment of the amount of information that can be potentially represented in the expert model and the current information content of the expert model.
- URREF criteria assess the impact of changes in the model and the integration of new pieces of evidence (observations).
- URREF criteria captures whether the current model, including the set of available evidences is sufficient to provide good quality results in terms of precision.
- URREF criteria support the analysis of results compared with the available truth.


## C. URREF Ontology and Selection of Uncertainty Criteria

The uncertainty representation and reasoning evaluation framework (URREF) ontology [23] provides a set of criteria for uncertainty analysis and evaluation in information fusion systems. The ontology defines several classes of criteria intended to capture different types of uncertainty affecting: sources and data inputs of the system, internal representations knowledge, algorithms, procedures for automated reasoning, results and outputs of the information fusion process. The URREF ontology has four main classes for uncertainty criteria.

- The first class is DataCriterion and consists of criteria relating to quality of input and output data, the reliability of sources and the impact of taking into account specific variables on the results.
- The second class gathers criteria associated with data handling under the general concept DataHandlingCriterion and includes DataInterpretation and Traceability.
- The third class is called RepresentationCriterion and characterizes the quality of domain knowledge representation through five criteria : KnowledgeHandling, Simplicity, Expressiveness, Adaptability and Compatibility.
- The fourth class is ReasoningCriterion and captures how well reasoning procedures performs, by including the following criteria : Correctness, Consistency, Performance (Throughput and Timeliness), Computational cost and Scalability.
According to requirements discussed above, the following URREF criteria are selected:

To characterize how strong the set of input data support inferences, the criterion Weight of evidence under DataCriteria is selected to assess the impact of evidences.

To characterize the quality of data, the criterion Accuracy under DataCriteria is selected to assess the quality of both input data (observations, evidence i.e. the accuracy of the probability distributions of the states of the BN after inference) and results.

To characterize knowledge representation Simplicity and Expressivenes are selected under the class RepresentationCriteria. For the purpose of this work, Simplicity is used to assess whether the expert model can be easily defined and maintained by experts and whether BN expert can understand and verify the BN while Expressiveness is used to assess the information content of both the Expert model and the BN.

## III. CRITERIA AND METRICS FOR UNCERTAINTY ASSESSMENT

To investigate the utility of the BN in practical applications, we analyze the nature of uncertainty induced by modeling decisions and expert assertions. For the application considered in this paper, uncertainty enters the BNs in three main forms: uncertainty of variable transformation or accuracy uncertainty, uncertainty of model structure or causality uncertainty, and reasoning uncertainty encompassing uncertainty in the CPTs and its propagation during the estimation of marginal posterior probability distributions. The first type of uncertainty is related

to evidence nodes; the second type captures imperfections of knowledge representation while the last type of uncertainty affects the set of results.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Application of URREF criteria

Figure 2 shows how uncertainty criteria can be used to characterize the expert model, the BN and the quality of results. Thus, values of simplicity and expressiveness for both the expert model and the BN can be used to measure whether the model can be maintained (simplicity) easily. The estimation of both the entropy of evidences (EoE) and the entropy of the nodes (EoN) after inferences offer good indicators of the reliability of results. When ground truth is available, results can be tested with respect to various "gold standard" data sets and the accuracy of results can be measured.

For applications having a large volume of test data, the values of the URREF based metrics that assess the model, the BN and input data, can be used to predict the reliability of results.

## A. Metrics for Knowledge Representation Assessment

This paper complements a previous contribution described in [1] where metrics were defined for two criteria: simplicity and expressiveness.

In order to discuss metrics for both criteria let's consider the following variables:

- $N$ the number of nodes in the network and the model;
- $M$ the number of evidence nodes in the network;
- $N_{s}$, the number of states in the network and the model;
- $N_{c}$ the number of connections in the network and the model
- $N_{p}$ the number of parameters in the model;
- $S_{g}$ the average weight of parameters.

The weight associates a coefficient to parameters according to the confidence in the experts statements. Thus, more important weights are assigned to items considered as being sure by experts. The weighting values are impossible, very unlikely, unlikely, unclear, probable, very probable and sure. Those linguistic values are translated into numerical values by assigning: 3 to sure and impossible, 2 for very probable and very unlikely, 1 for probable and unlikely and 0 for unclear.

The average weighting value is calculated as the arithmetic mean of all parameters.

In order to define a metric for Simplicity we defined first an additional metric called ergonomic complexity $(E C)$ as

$$
E C=\log (N)\left[\log \left(N_{s}-1\right)+\log \left(N_{c}\right)+\log \left(N_{p}\right)\right]
$$

A minimal network with two nodes, two states per node, two connections per node and two parameters per node gets a complexity value 1.0. Theoretically, complexity has no upper limit. Therefore the values are within the interval $[1.0, \infty[$. The number of parameters in the expert model and in the BN is dependent on the number of states and the number of connections. It might seem like double counting to include all of these counts in $E C$, but when it comes to the ease of domain expert knowledge elicitation, the number of nodes and states per node are of interest. It captures whether experts are able to maintain a coherent view of the problem properties during the definition and parametrization of the models. The same holds for the number of parameters. Thus we defined ergonomic simplicity $E S$ as the inverse of ergonomic complexity, i.e.

$$
E S=(1 / E C)
$$

Since the criterion Simplicity is defined as inverse of Complexity, the values of the metric ergonomic simplicity are elements of $[0.0,1.0]$. This metric captures the intuition that a small model and network with few nodes, states, dependencies and parameter values is rather simple.

Considering the notation above, the metric model expressiveness $(M E)$ is defined as

$$
M E=\log (N-1) *\left[\log \left(N_{s}\right)+\log \left(N_{c}\right)+\log \left(N_{p} * S_{g}\right)\right]
$$

The interval for the values of $M E$ is also limited to $[1.0, \infty]$. According to the URREF definitions, the formula is dedicated to the "Dependency" part of the criterion. If $S_{g}=1$ (which correlates to the intermediate weightings probable/unlikely), $M E$ has the same value as $E C$. The value for $M E$ is higher than for $E C$, if the intermediate weight assumes a more certain medium value than probable or unlikely. This corresponds to the intuitive assumptions, that a model might be complex but not so expressive if the network contains many information sources with low influence on the result. The intuition behind $M E$ is that the more entities, connections, states at node level with significant parameter values a model has, the more able it is to capture and describe entities and interactions of the model.

In [1] those metrics were used to assess both the expert model defined during the modelling step 1 and the BN built after the modelling step. Note that this definition is of greater importance for the modelling step, since the BN is generated automatically from the expert model.

We can use the already defined averaged significance $S_{g}$, see [1], to assess the quality of observations and results in the language of the expert model, since the expert model represents the current states of observations and the values of the inference results of the states of the objects of the

expert model with the same qualitative values as the weights of dependencies.

## B. Entropy-Related Metrics for Bayesian Networks

The concept of entropy was introduced by Claude Shannon in his seminal work on information theory [24]. Entropy quantifies the uncertainty manifested in the probability distribution of a variable and intuitively, minimizing the entropy of a probability distribution decreases its uncertainty. This section introduces the concept of entropy in Bayesian networks, its related concepts - mutual information, Kullback-Leibler divergence and information content - and defines metrics for URREF criteria based on those concepts.

A BN describes a probability distribution for the product of $N$ random variables $X_{1}, X_{2}, \ldots, X_{N}$ taking into account the conditional probabilities between them.

Definition III.1. Bayesian Network: Let us consider a set of $N$ random variables $X=\left(X_{1}, X_{2}, \ldots, X_{N}\right)$ forming a directed acyclic graph with $n$ numbered nodes and let us suppose node $j,(1 \leq j \leq N)$ of the graph is associated to the $X_{j}$ variable. Then the graph is a Bayesian Network, representing the variables $X_{1}, X_{2}, \ldots, X_{N}$, if

$$
P(X)=P\left(X_{1}, X_{2}, \ldots, X_{N}\right)=\prod_{j=1}^{n} P\left(X_{j} \mid \operatorname{parents}\left(X_{j}\right)\right)
$$

where parents $\left(X_{j}\right)$ denotes the set of all variables $X_{i}$, such there is an arc from node $i$ to node $j$ in the graph [25] and $P$ is the joint probability mass function defined over the set of variables $X$.

The BN considered for this work contains, by construction, random variables representing discrete events. In this case, the conditional probabilities of children nodes conditioned upon parent nodes are represented by the Conditional Probability Tables (CPTs).

1) Information Content: A natural measure for information content is Shannon's information content (measured in bits) [26] given by

$$
h(x)=\log _{2}\left(\frac{1}{P(x)}\right)
$$

where $x$ is an outcome of $X$. For a random variable $X$ with discrete set of $n$ possible events $1, \ldots, n$ that occur with probabilities $p=\left(p_{1}, p_{2}, \ldots, p_{n}\right)$, the normalized entropy is the average information content of the random variable, and is given by

$$
H(X)=\sum_{i=0}^{n} p_{i} \log \left(\frac{1}{p_{i}}\right)
$$

Normalized entropy quantifies the information gain from learning information on a set of evidence in a BN. The maximum entropy value increases logarithmically with the number of states of the variables, so the entropy of variables with different number of states cannot be directly compared. Normalized entropy takes the maximum entropy value into account and uncertainty can then be directly compared between
variables. Given $n$ states for a random variable $X$, the entropy is maximized if the probability distribution of $X$ is uniform:

$$
H(X) \leq \log (n)
$$

Normalizing $H(X)$ by $\log (n)$ gives $H_{N}(X) \in[0,1]$. Mackay [26] defined redundancy as:

$$
1-\frac{H(X)}{\log (n)}=1-H_{N}(X)
$$

so $H_{N}(X)$ can be thought of as the efficiency of $X$, although this is not a formal definition.
2) Mutual Information: Whereas entropy quantifies how much information is gained by learning information from an evidence set, mutual information quantifies how much information we will gain on average - considering all values of a node. The mutual information (denoted by $I$ ) between two random variables $X$ and $Y$ is given by

$$
I(X ; Y)=H(X)-H(X \mid Y)
$$

where $H(X \mid Y)$ is the conditional entropy of $X$ given $Y$. Conditional entropy measures the average uncertainty remaining about $X$ when $Y$ is known. Mutual information measures the reduction in uncertainty about $X$ as a result of learning the value of $Y$ or vice versa, meaning that $I(X ; Y)=I(Y ; X)$. Figure 3 provides a breakdown of the total entropy of the variables $X$ and $Y[26]$.


Fig. 3. Breakdown of total entropy $H(X, Y)$ into marginal, conditional and mutual entropy (taken from [26]).
3) Kullback-Leibler Divergence: An information metric closely related to mutual information is the Kullback-Leibler (KL) divergence. KL divergence compares two probability distributions $P$ and $Q$, defined on the same set of variables $X$ as

$$
D_{K L}(P \mid Q)=\sum_{x} P(x) \log _{2}\left(\frac{P(x)}{Q(x)}\right)
$$

If $P$ is the probability distribution associated to a given network, and $Q$ is the probability distribution associated to the same network with a specific arc removed, then $D_{K L}(a)$ can be interpreted as the force of the arc of interest $a$. Mutual information and KL divergence are identical when the child node in the probability distribution has only one parent. KL divergence takes into account the joint probability rather than only the arc between two nodes and is therefore considered a more powerful metric of information gain [27].

4) Node Force: Finally, node force is a term defined in [27] as the sum of $D_{K L}(a)$ associated with a node. Three types of node forces are defined as:

- Incoming node force $\left(\sum_{\substack{\text{incoming } \\\text{arcs }}} D_{K L}(a)\right)$
- Outgoing node force $\left(\sum_{\substack{\text{outgoing } \\\text{arcs }}} D_{K L}(a)\right)$
- Total node force $\left(\sum_{\substack{\text{total } \\\text{arcs }}} D_{K L}(a)\right)$

The incoming node force gives some indication of the complexity of the node as it represents the information content of the CPT of the node whereas the outgoing node force gives an indication of the expressiveness of the node as its information content is propagated through multiple information channels.

## C. Entropy-based metrics for URREF criteria

1) Metrics for knowledge representation: Uncertainty of knowledge representation can be assessed with Simplicity and Expressiveness criteria for both the expert model and the BN. Uncertainties of the expert model are captured by Ergonomic Simplicity (ES) and Model Expressiveness (ME) metrics. Metrics for BNs are improved by taking into account the information content concept to replace $S_{g}$ and referred to as $S_{g_{B N}}$. The outgoing node force as defined above is used to calculate $S_{g_{B N}}$ before any evidence is entered into the network. Consider $N$ as the number of nodes with outgoing arcs in the BN. Then $S_{g_{B N}}$ is defined as

$$
S_{g_{B N}}=\frac{1}{N} \sum_{i=0}^{N} \sum_{\substack{\text{outgoing } \\\text{arcs }}} D_{K L}(a)
$$

The outgoing node force is used since the $S_{g}$ of the Expert Model is also correlated with the weightings of the expertdefined parent to child connections. Therefore, the entropybased expressiveness of the BN model is then defined by

$$
M E_{B N}=\log (N-1)\left[\log \left(N_{s}\right)+\log \left(N_{c}\right)+\log \left(N_{p} S_{g_{B N}}\right)\right]
$$

2) Metrics for data characterization: Two metrics are defined for Accuracy criterion in order to capture the definiteness and the accuracy of results, respectively.

The definiteness of state values takes into account the normalized entropy $\left(H_{N}(X)\right)$ of nodes and is defined as

$$
U A(X)=1-H_{N}(X)
$$

This metric can be applied to assess specific nodes of interest, in order to verify if inferences improve or have a negative impact of the quality of their results.

Accuracy of results is defined as the Euclidean distance between the ground truth and state values of the nodes. If $t(i)$ is the truth value and $p_{i}$ is the probability of state $i$ of variable $X$, the accuracy is calculated as

$$
R A(X)=1-\sqrt{\frac{1}{2}}\left(\sum_{i=0}^{n}\left(p_{i}-t(i)\right)^{2}\right)
$$

where $t(i)$ is the ground truth probability distribution such that $t(i)=1$ for the true state of $X$. This metric can be
applied when ground truth is available, in order to estimate how accurate those results are with respect to ground truth, regardless of the positive or negative impact of inferences.

Impact of evidences is defined as the average value of mutual information estimated for evidence nodes as

$$
I o E=\sum_{i=0}^{M} \frac{I(E)}{M}
$$

where $M$ is the number of evidence nodes, and $I(E)$ is the mutual information between evidence nodes. This metric can be applied for a given BN, in order to estimate the overall impact of various sets of evidences and provides a global characterization of evidence nodes.

Table I shows a synthetic view of criteria, URREF class of criteria and associated metrics.

TABLE I
URREF CRITERIA AND ASSOCIATED METRICS


## IV. ILLUSTRATION ON CYBER THREAT DETECTION

## A. Scenario for cyber threat detection

To make the analysis specific, the following scenario was used as narrative for metrics estimations: several hackers travel to a specific destination in order to attend a conference. Many of them use wireless connections of the airline which is equipped with on-board-sensors, a security operation center (SOC) and the OSINT. During the conference, vulnerabilities of on-board-systems of aircraft shall be discussed and the challenge is to get evidence about vulnerabilities from practical examples. However, the hackers do not want to give rise to any danger to the air traffic. The travelling hackers try to intrude the in-flight entertainment (IFE) systems of the aircraft to perform research about the internal vulnerabilities of these systems.

For illustration purposes, the following elements for ground truth are available: threat actor type: white-hat hacker and hacktivists, threat actor motivation: Ideological Security Awareness and Egoistic Attention Seeking and also the action research for asset address (within the aircraft of the scenario).

Over the time, the set of evidences evolve as follows: first the IT-based anomaly detection within the aircraft detects a wrong IP-address and a wrong payload in a message within the network where the inflight entertainment system is running. Thereafter the SOC receives messages from several aircraft containing the information that someone tries to connect to the IFE system to research for asset addresses within the IFE network. Finally the subsequent OSINT research within

the SOC discovers the information about a hacker conference taking place near the destination of several aircraft which were under attack.

## B. Metrics assessment and interpretation of results

The introduction of expert model was motivated by simplicity considerations: domain experts should be able to represent their knowledge and to interact with the system although often they are not able to handle large Bayesian networks. Uncertainty criteria were selected for the following steps: generation of the expert model by domain experts, calculation of results, interpretation of results, update of the model and analysis of BN by experts.

The expert model used for this work has 15 nodes, 18 connections, 300 states and 504 parameters. $S_{g}$ the significance of the expert weightings of the dependencies is 1.496 . The BN generated from the expert model has 212 nodes, 316 connections, 527 states and 14075 parameters.

The median significance for the nodes of the BN derived from the Kullback-Leibler divergence is 0.2248 , and according to this value, the significance of the BN seems to be very small compared to the expert model. However, if we consider the combination (significance $\times$ number) of parameters, which is 754 for the expert Model and 3164 for the BN, the values are similar since the weightings of the expert model are integrated into the CPT of the BN during the automatic construction of the BN. ${ }^{1}$

Simplicity and Expressiveness criteria were used to asses the knowledge representation of both the expert model and the BN by using specified metrics for those criteria. Numerical values are shown in Table II.

TABLE II
Simplicity and Expressiveness


Values of simplicity for the expert model and the BN (see Table II,) reconfirm the intuition that understanding the BN is considerably more difficult than understanding the expert model. In the same table, values of expressiveness indicate that the BN offers a richer representation of expert knowledge. Metrics developed for data characterization are used to analyse three specific nodes of the BN: ThreatActorType, ThreacActorMotivation and ResearchForAssetAddress. The node ThreatActorType has 19 states, the node ThreacActorMotivation has 17 states and the node ResearchForAssetAddress is a binary node. The ground truth for type and motivation is represented by two values 0.5 for the scenario assumptions as described above and 0.0 for the other state values. The state true

[^0]TABLE III
DEFINITENESS OF RESULTS


Initial evidence has a strong impact on the node ResearchForAssetAddress, but its implications for threat actor type and motivation are weak. Next iterations and additional evidences improve the quality of these two nodes.

TABLE IV
ACCURACY OF RESULTS


Weight of evidence shows a different trend: initial steps have important values of IoE see Table V, which decrease drastically as inferences are performed.

TABLE V
IMPACT OF EVIDENCE


This evolution is consistent with the intuition that initial evidences are useful to support decision but their utility decreases in time.

Although the assessment of metrics already highlights consistent results, there are several aspects to be covered by additional criteria of the URREF and associated metrics: for example, the average quality and the consistency of all evidence nodes should be taken into account.

## C. Relations between metrics and URREF Criteria

The URREF ontology allows to represent relations between criteria. The relations can be used as a basis to identify dependent criteria which can be analyzed together.

Criteria selected for this work are directly or indirectly correlated, as shown in Figure 4.

Simplicity and expressiveness have a negative correlation and increasing values of expressiveness results in decreased values for simplicity. Results of inferences that are unambiguous and accurate are considered as 'good'. If there is a large data set allowing building different versions of the model for an application, the subset having the ability to generate good results can be selected to create a model having the highest values of simplicity.


[^0]:    ${ }^{1}$ All BN calculations were performed in Bayesialab 8.0.1

![img-3.jpeg](img-3.jpeg)

Fig. 4. URREF metrics and Criteria

## V. CONCLUSION AND FUTURE WORK

BN are useful tools to support cyber threat detection but often practical applications require building complex BNs, having an important number of nodes and to define CPTs for multiple parent nodes. To overcome those difficulties, expert models can be used to facilitate the representation of knowledge and construction of BN.

This paper addresses the characterization of BN built automatically from expert models and discusses uncertainty criteria describing imperfections of knowledge representation, input data and results. URREF criteria are selected to capture those aspects and the concept of entropy is used to define several metrics for those criteria. Metrics assessment is illustrated with an applicative use case of possible cyber threats against the IT equipment of an aircraft and their numerical values provide consistent results for uncertainty analysis.

Directions for future work are threefold. First, future work can improve the definition of metrics by taking into account the average quality and consistency of all evidence nodes. Second, the assessment of uncertainty metrics should be performed for different versions of the model and for several combinations of evidences. The results provided can be further analyzed to find the optimal sub-set of data leading to reliable inference results. And third, the set of criteria can be applied to different techniques for uncertainty representation (e.g. Dempster - Shafer or machine learning approaches) for which the definition of adequate variants of the metrics should be investigated.
