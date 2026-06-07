![img-0.jpeg](img-0.jpeg)

This is a repository copy of On risk-based active learning for structural health monitoring.
White Rose Research Online URL for this paper:
https://eprints.whiterose.ac.uk/180703/
Version: Submitted Version

# Article: 

Hughes, A.J. orcid.org/0000-0002-9692-9070, Bull, L.A., Gardner, P. orcid.org/0000-0002-1882-9728 et al. (3 more authors) (Submitted: 2021) On risk-based active learning for structural health monitoring. arXiv. (Submitted)
(c) 2021 The Authors. Preprint available under the terms of the CC-BY-NC-ND licence (https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Reuse

This article is distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND) licence. This licence only allows you to download this work and share it with others as long as you credit the authors, but you can't change the article in any way or use it commercially. More information and the full terms of the licence here: https://creativecommons.org/licenses/

## Takedown

If you consider content in White Rose Research Online to be in breach of UK law, please notify us by emailing eprints@whiterose.ac.uk including the URL of the record and the reason for the withdrawal request.
![img-1.jpeg](img-1.jpeg)

# On risk-based active learning for structural health monitoring 

A.J. Hughes*, L.A. Bull, P. Gardner, R.J. Barthorpe, N. Dervilis, K. Worden<br>Dynamics Research Group, Department of Mechanical Engineering, University of Sheffield, Sheffield, S1 3JD, UK


#### Abstract

A primary motivation for the development and implementation of structural health monitoring systems, is the prospect of gaining the ability to make informed decisions regarding the operation and maintenance of structures and infrastructure. Unfortunately, descriptive labels for measured data corresponding to health-state information for the structure of interest are seldom available prior to the implementation of a monitoring system. This issue limits the applicability of the traditional supervised and unsupervised approaches to machine learning in the development of statistical classifiers for decision-supporting SHM systems.

The current paper presents a risk-based formulation of active learning, in which the querying of class-label information is guided by the expected value of said information for each incipient data point. When applied to structural health monitoring, the querying of class labels can be mapped onto the inspection of a structure of interest in order to determine its health state. In the current paper, the risk-based active learning process is explained and visualised via a representative numerical example and subsequently applied to the Z24 Bridge benchmark. The results of the case studies indicate that a decision-maker's performance can be improved via the risk-based active learning of a statistical classifier, such that the decision process itself is taken into account.


Keywords: structural health monitoring, decision-making, active learning, value of information

## 1. Introduction

The field of structural health monitoring (SHM) is concerned with the development and implementation of online data acquisition and processing systems for the purpose of damage detection in structures and infrastructure [1]. Impelling advancement in SHM is the desire for quantitative decision support regarding the operation and maintenance (O\&M) of high-value and/or safety-critical assets. By the incorporation of information provided by SHM systems into the decision process, thereby facilitating condition-based O\&M, it is hoped that both structural safety can be improved and operational costs can be reduced.

One approach to decision-making in SHM is to adopt a probabilistic risk-based framework [2], in which failure events and decidable actions - like maintenance - are assigned costs and utilities, respectively. Decisions are made so as to maximise expected utility gain or minimise expected utility loss. As a product of probability and utility, expected utility can be considered a measure of risk [3]. The risk-based framework employs probabilistic graphical modelling to form Bayesian network representations of fault trees to define a probability of a failure event conditioned on the health state of the structure. In addition, the approach uses transition/degradation models to forecast future health states. In accordance with [1], the framework in [2] utilises a statistical pattern recognition (SPR) approach to damage detection and localisation in the inference of structural health states.

[^0]
[^0]:    *Corresponding author

    Email address: ajhughes2@sheffield.ac.uk (A.J. Hughes)

A critical challenge associated with the (supervised) learning of statistical classifiers for SHM is a lack of labelled data corresponding to the health states of interest. Several methods have been investigated as a means to overcome this challenge, including the use of physics-based models [4] and transfer learning [5, 6]. An alternative approach, that enables the online development of classifiers, is active learning. An active learning framework for SHM has been developed in [7], in which probabilistic classifiers direct the acquisition of new labelled data according to an uncertainty measure, given the current model. Within the active learning framework for SHM, newly-acquired labelled data correspond to diagnostic information provided by an engineer, following an inspection of a structure. While this formulation provides a principled methodology for allocating inspection resource in a manner that optimises classification accuracy, in some scenarios it may be desirable/utility-optimal to consider the active learning of a classifier with respect to the context in which the classifier is being applied; supporting O&M decision-making.

The current paper aims to formulate the active learning process in the context of probabilistic risk-based SHM by considering the expected value of perfect information (EVPI) with respect to a maintenance decision process. The layout of the paper is as follows. Sections 2 and 3 provide background information on risk-based SHM and on machine learning for SHM, respectively. Section 4 presents the methodology for conducting risk-based active learning. Section 5 demonstrates riskbased active learning of a probabilistic mixture model for a simple, but representative, numerical dataset. Section 6 presents the risk-based active approach to learning as applied to the Z24 Bridge benchmark dataset. Finally, Sections 7 and 8 provide discussions and conclusions, respectively.

# 2. Probabilistic Risk-Based SHM 

### 2.1. Probabilistic graphical models

Probabilistic graphical models (PGMs) are graphical representations of factorisations of joint probability distributions and are a powerful tool for reasoning and decision-making under uncertainty. For this reason, they are apt for representing and solving decision problems in the context of SHM, where there is uncertainty in the health states of structures. While there exist multiple forms of probabilistic graphical model, the key types utilised for the risk-based decision frameworks are Bayesian networks (BNs) and influence diagrams (IDs) [8].

Bayesian networks are directed acyclic graphs (DAGs) comprised of nodes and edges. Nodes represent random variables and edges connecting nodes represent conditional dependencies between variables. In the case where the random variables in a BN are discrete, the model is defined by a set of conditional probability tables (CPTs). For continuous random variables, the model is defined by a set of conditional probability density functions (CPDFs).
![img-2.jpeg](img-2.jpeg)

Figure 1: An example Bayesian network.
Figure 1 shows a simple Bayesian network comprised of three random variables $X, Y$ and $Z$. $Y$ is conditionally dependent on $X$ and is said to be a child of $X$, while $X$ is said to be a parent of $Y . Z$ is conditionally dependent on $Y$ and can be said to be a child of $Y$ and a descendant of $X$, while $X$ is said to be an ancestor of $Z$. The factorisation described by the Bayesian network shown in Figure 1 is given by $P(X, Y, Z)=P(X) \cdot P(Y \mid X) \cdot P(Z \mid Y)$. Given observations on a subset of nodes in a BN, inference algorithms can be applied to compute posterior distributions over the remaining unobserved variables. Observations of random variables are denoted in a BN via grey shading of the corresponding nodes, as is demonstrated for $X$ in Figure 1.

Bayesian networks may be adapted into influence diagrams to model decision problems. This augmentation involves the introduction of two additional types of node that are shown in Figure 2: decision nodes, denoted as squares, and utility nodes, denoted as rhombi. For influence diagrams, edges connecting random variables to utility nodes denote that the utility function is dependent on the states of the random variables. Similarly, edges connecting decisions nodes to utility nodes

![img-3.jpeg](img-3.jpeg)

Figure 2: An example influence diagram representing the decision of whether to go outside or stay in under uncertainty in the future weather condition given an observed forecast.
denote that the utility function is dependent on the decided actions. Edges from decision nodes to random variable nodes indicate that the random variables are conditionally dependent on the decided actions. Edges from random variable or decision nodes to other decision nodes do not imply a functional dependence but rather order, i.e. that the observations/decisions must be made prior to the next decision being made.

To gain further understanding of IDs, one can consider Figure 2. Figure 2 shows the ID for a simple binary decision; stay home and watch TV or go out for a walk, i.e. domain $(D)=\{$ TV, walk $\}$. Here, the agent tasked with making the decision has access to a weather forecast $W_{f}$ which is conditionally dependent on the future weather condition $W_{c}$. The weather forecast and future condition share the same possible states domain $\left(W_{f}\right)=\operatorname{domain}\left(W_{c}\right)=\{$ bad, good $\}$. The utility achieved $U$, is then dependent on both the future weather condition and the decided action. For example, one might expect high utility gain if the agent decides to go for a walk and the weather condition is good.

In general, a policy $\delta$ is a mapping from all possible observations to possible actions. The problem of inference in influence diagrams is to determine an optimal strategy $\boldsymbol{\Delta}^{*}=\left\{\delta_{1}^{*}, \ldots, \delta_{n}^{*}\right\}$ given a set of observations on random variables, where $\delta_{i}^{*}$ is the $i^{\text {th }}$ decision to be made in a strategy $\boldsymbol{\Delta}^{*}$ that yields the maximum expected utility (MEU). For further details on the computation of the MEU for influence diagrams, the reader is directed to [9] and [10]. Defined as a product of probability and utility, the expected utility can be considered as a quantity corresponding to risk.

# 2.2. Decision Framework 

A probabilistic graphical model for a general SHM decision problem across a single time-slice is shown in Figure 3. Here, a maintenance decision $d$ is shown for a simple fictitious structure $\boldsymbol{S}$, comprised of two substructures $\boldsymbol{s}_{1}$ and $\boldsymbol{s}_{2}$, each of which are comprised of two components; $c_{1,2}$ and $c_{3,4}$, respectively.

The overall decision process model shown in Figure 3 is based upon a combination of three sub-models; a statistical classifier, a failure-mode model, and a transition model.

Within the decision framework, a random variable denoted $\boldsymbol{H}_{t}$ is used to represent the latent global health state of the structure at time $t$. For this decision process, a posterior probability distribution over the latent health state $\boldsymbol{H}_{t}$ is inferred with a statistical classifiers via observations on a set of discriminative features $\boldsymbol{\nu}_{t}$. It is assumed that the generative conditional distribution $P(\boldsymbol{\nu} \mid \boldsymbol{H})$ is learned implicitly or explicitly, depending on the choice of statistical classifier. Here, the use of a probabilistic classifier is vital to ensure decisions made are robust to uncertainty in the health state of the structure.

The failure condition of the structure $F_{\boldsymbol{S}}$ is represented as a random variable within the PGM and is conditionally dependent on the health states of the substructures denoted by the nodes $h \boldsymbol{s}_{1}$ and $h \boldsymbol{s}_{2}$. The health states of the substructures are dependent on the local health states of the constituent components denoted by the nodes $h c_{1-4}$. The local health states of the components are summarised in the global health-state vector $\boldsymbol{H}=\left\{h c_{1}, h c_{2}, h c_{3}, h c_{4}\right\}$. The conditional probability tables defining the relationship between these random variables correspond to the Boolean truth tables for each of the logic gates in the fault tree defining the failure mode $F_{\boldsymbol{S}}$ [11, 12]. This failure-mode model is repeated in each time-step. The failure states associated with the variable $F_{\boldsymbol{S}}$ are given utilities via the function represented by the node $U_{F}$. As it is necessary to consider

![img-4.jpeg](img-4.jpeg)

Figure 3: An influence diagram representing a partially-observable Markov decision process over one time-slice for determining the utility-optimal maintenance strategy for a simple structure comprised of four components. The fault-tree failure-mode model for time $t+1$ has been represented as the node $F_{t+1}^{\prime}$ for compactness.
the future risk of failure in the decision process, these utility functions are also repeated for each time-step.

Finally, a transition model is used to forecast the future health states given the current health state and a decided action, i.e. $P\left(\boldsymbol{H}_{t+1} \mid \boldsymbol{H}_{t}, d_{t}\right)$. The transition model considers the degradation of the structure under the various operational and environmental conditions a structure may experience, while accounting for uncertainties in each.

# 3. Machine Learning Paradigms 

### 3.1. Supervised and unsupervised learning for SHM

In taking a data-driven statistical pattern recognition approach to SHM, one employs machine learning tools to learn patterns in data acquired from structures in order to infer information about structural health states such as the presence, location, and type of damage. For classification in general, the $i^{\text {th }}$ measured data point $\boldsymbol{x}_{i} \in X$ can be categorised according to a descriptive label $y_{i} \in Y$ where $y_{i}$ corresponds to the ground truth of the classification problem. For SHM,

![img-5.jpeg](img-5.jpeg)

Figure 4: The general active learning heuristic from [7].

observations **x<sub>i</sub>** correspond to features extracted from the raw data acquired from a structure via signal processing, and the descriptive labels **y<sub>i</sub>** relate to structural health-state information.

As aforementioned, probabilistic classifiers are desirable in SHM. For probabilistic classifiers, the features **x<sub>i</sub>** are defined as random vectors existing in a *D*-dimensional feature space **X** ∈ **R**<sup>D</sup>. Additionally, the descriptive labels **y<sub>i</sub>** are defined by a discrete random variable such that **y<sub>i</sub>** ∈ **Y** = {1, ..., *K*} where **Y** is the label space and **K** is the number of classes required to uniquely identify the structural health states of interest.

Traditionally in SHM, classifiers are learned using one of two frameworks: *supervised* or *unsupervised* learning [13].

For a supervised classifier **f**, a mapping between the feature space and the label space is learned, i.e. **f : X → Y**. Supervised learning requires a fully-labelled training-set **D<sub>l</sub>** such that [14],

$$
\mathcal{D}_l = \left\{ (\mathbf{x}_i, y_i) \mid \mathbf{x}_i \in X, y_i \in Y \right\}_{i=1}^n \tag{1}
$$

for **n** collected data points. In the context of SHM, a fully-labelled training-set is often prohibitively expensive to obtain, or otherwise unavailable.

Conversely, unsupervised learning techniques (e.g. novelty detection [1]) may be applied when only unlabelled data are available and the training-set **D<sub>u</sub>** is of the form,

$$
\mathcal{D}_u = \left\{ \mathbf{x}_i \mid \mathbf{x}_i \in X \right\}_{i=1}^m \tag{2}
$$

for **m** collected data points. The issue with unsupervised techniques is that, without label information corresponding to the structural health conditions, the models learned are of limited usefulness for decision-making. For a more in-depth discussion of the use of supervised and unsupervised learning in SHM, the reader is directed to [7].

### 3.2. Active learning for SHM

Active learning is a form of *partially-supervised learning* [14]. Partially-supervised learning algorithms are characterised by their use of both labelled and unlabelled data, such that the dataset is,

$$
\mathcal{D} = \mathcal{D}_l \cup \mathcal{D}_u \tag{3}
$$

Active learning algorithms automatically query unlabelled data in **D<sub>u</sub>** to obtain labels allowing the labelled dataset **D<sub>l</sub>** to be extended. A generalised active learning heuristic is presented in Figure 4.

The probabilistic active learning framework for SHM developed in [7] details an approach built around a supervised probabilistic mixture model trained and retrained on **D<sub>l</sub>** as it is extended via the active querying process. The approach presented in [7] uses measures of uncertainty to guide querying of incipient data points; specifically, preferentially obtaining labels for data points that have high entropy (information) [15?] or low likelihood, given the current model.

After some thought, one can realise that the active learning approach overcomes several of the challenges associated with supervised and unsupervised learning in SHM, as decision-making may be facilitated by the acquisition of class labels whilst limiting the expenditure necessary to obtain them.

![img-6.jpeg](img-6.jpeg)

Figure 5: The general risk-based active learning heuristic.

# 4. Risk-based Active Learning 

The current paper proposes a variation on the active learning framework presented in [7] where, instead of using uncertainty measures to guide querying of data points according to their information or likelihood, incipient data are queried according to the expected value of perfect information with respect to the decision process, modelled using the risk-based SHM framework, in which the classifier is being applied. A generalised framework for risk-based active learning is presented in Figure 5.

### 4.1. Classifier initiation

To begin the risk-based active learning process, one must initiate the classifier to be learned. Typically, this initialisation is done in a supervised manner with the available labelled data $\mathcal{D}_{l}$. In the case that there are no available labelled data, i.e. $\mathcal{D}_{l}=\emptyset$, and one has opted for a Bayesian learning approach, the classifier may be initiated using only the prior distribution.

Here, it is worth noting that the risk-based approach to active learning assumes that the number of classes (health states of interest) to be targeted by the model is known a priori. Within an uncertainty-based approach to active learning, one can infer the number of classes from data [7]. In contrast, for the risk-based approach to active learning, it is required that the classes targeted by the classifier correspond to those represented in the decision process. The prescription of the target classes limits the flexibility of the classifier, while also facilitating the computation of value of information.

### 4.2. Value of information

The expected value of perfect information (EVPI) is often understood as the price that a decision-maker should be willing to pay in order to gain access to perfect information regarding an otherwise uncertain or unknown state. More formally, EVPI can be defined as [10],

$$
\operatorname{EVPI}(d \mid X):=\operatorname{MEU}\left(\mathcal{I}_{X \rightarrow d}\right)-\operatorname{MEU}(\mathcal{I})
$$

where $\operatorname{EVPI}(d \mid X)$ is the expected value of observing (with perfect information) a variable $X$ before making a decision $d, \mathcal{I}$ corresponds to an original influence diagram for a decision process involving a decision node $d$ and a random variable node $X$, and $\mathcal{I}_{X \rightarrow d}$ corresponds to a modified influence diagram incorporating an additional edge from $X$ to $d$. The EVPI has the important characteristic that it is strictly non-negative (when disregarding the cost of making the additional observation), i.e. $\operatorname{EVPI}(d \mid X) \geq 0$. This proposition can be realised by considering the conditional probability distributions over which the expected utility is optimised; the conditional probability distributions defined by the influence diagram $\mathcal{I}$ are a subset of those defined by $\mathcal{I}_{X \rightarrow d}$. Furthermore, $\operatorname{EVPI}(d \mid X)=0$ if and only if the optimal policy for $d$ in $\mathcal{I}$ remains optimal for $d$ in $\mathcal{I}_{X \rightarrow d}$; put simply, information has non-zero value when its possession results in a policy change.

In the context of an SHM decision process, the expected value of inspection can be represented as $\operatorname{EVPI}\left(d_{t} \mid \boldsymbol{H}_{t}\right)$, where the original influence diagram $\mathcal{I}$ corresponds to the decision process where the health state of the structure is inferred only via the observation of discriminative features with use of the statistical classifier. The modified influence diagram includes an additional edge from $\boldsymbol{H}_{t}$ to $d_{t}$ indicating the inspection of the structure. Considering the influence diagram shown in

Figure 3 as $\mathcal{I}$, the modified influence diagram $\mathcal{I}_{\boldsymbol{H}_{t}\rightarrow d_{t}}$ is shown in Figure 6. For the computation of the EVPI, it is assumed that inspection of the structure returns the ground-truth health state at the current time.
![img-7.jpeg](img-7.jpeg)

Figure 6: A modified influence diagram $\mathcal{I}_{\boldsymbol{H}_{t} \rightarrow d_{t}}$. The additional edge is shown in red.
An example calculation of EVPI is provided in Appendix A.

# 4.3. Inspection scheduling 

The EVPI of an unlabelled data point provides a convenient measure for determining whether a structure warrants inspection; if the EVPI for a data point $\boldsymbol{\nu}_{t}$ exceeds the cost of inspection $C_{\text {ins }}$, the structure should be inspected prior to $d_{t}$ and the corresponding health-state label for $\boldsymbol{H}_{t}$ obtained. Subsequently, $\left(\boldsymbol{\nu}_{t}, \boldsymbol{H}_{t}\right)$ can be incorporated into $\mathcal{D}_{l}$ and the classifier retrained. The risk-based active learning process for inspection scheduling and the development of statistical classifiers for risk-based SHM is shown in Figure 7.

### 4.4. Assessing performance

Typically, classifier performance is evaluated using measures of classification accuracy, a popular choice being the $f_{1}$-score. As the focus of this paper is the development of classifiers in the context of decision-making, classification accuracy is of secondary concern. Rather here, an alternative

![img-8.jpeg](img-8.jpeg)

Figure 7: Flow chart to illustrate the risk-based active learning process for classifier development and inspection scheduling.

metric for evaluating the more salient measure of decision-making performance is adopted, termed 'decision accuracy' [2].

Whereas, in the simplest sense, a classification accuracy is a comparison between the predicted outputs and the target outputs, 'decision accuracy' is defined as a comparison between the actions selected by an agent using the statistical classifier being evaluated, and the optimal actions selected by an agent given perfect information, i.e. an agent in possession of the true target outputs of the classifier. A decision is considered 'correct' if the agent utilising the classifier selects the same action as an agent with perfect information. A quantitative value for decision accuracy may be calculated by taking the ratio:

$$
\text { decision accuracy }=\frac{\text { number of correct decisions }}{\text { total number of decisions }}
$$

# 5. Numerical Example 

To demonstrate risk-based active learning for SHM in a visual manner, the framework was applied to a representative numerical case study. Consider a structure $S$ with four distinct health states of interest $H \in\{1,2,3,4\}$ :

- State 1 corresponds to the structure being undamaged and fully functional
- State 2 corresponds to the structure possessing minor damage whilst being fully functional
- State 3 corresponds to the structure possessing significant damage whilst operating at a reduced operational capacity
- State 4 corresponds to the structure possessing critical damage and being non-operational, i.e. failed.

5.1. Decision process

One can consider a decision process for the structure $S$, in which an agent at time $t$ is tasked with making a decision $d_{t}$, such that some degree of operational capacity is maintained and the structure is not in the failed state at time $t+1$. The influence diagram for such a decision process is shown in Figure 8.
![img-9.jpeg](img-9.jpeg)

Figure 8: An influence diagram representation of the decision process associated with structure $S$.
Here, the decision $d_{t}$ is a binary choice where, $d_{t}=0$ corresponds to 'do nothing' and $d_{t}=1$ corresponds to 'perform maintenance'. The utilities associated with $d_{t}$ are specified by the utility function $U\left(d_{t}\right)$ and are shown in Table 1. It is assumed that the 'do nothing' action has no utility associated with it, whereas the 'perform maintenance' action has negative utility relating to the expenditure associated with material and labour costs for structural maintenance. In practice, the specification of utility functions is non-trivial however may be achieved via expert elicitation during the operational evaluation stages of an SHM campaign. The elicitation of utility functions is beyond the scope of the current paper. Hence, for the purposes of the current case study, the relative values of utilities are selected to be somewhat representative of the SHM context.

Table 1: The utility function $U\left(d_{t}\right)$ where $d=0$ and $d=1$ denote the 'do nothing' and 'perform maintenance' actions, respectively.


For the 'do nothing' action $d_{t}=0$, it is assumed that the structure monotonically degrades, with a propensity to remain in its current health state. This assumption is reflected in the CPD $P\left(H_{t+1} \mid H_{t}, d_{t}=0\right)$ shown in Table 2.

For the 'perform maintenance' action $d_{t}=1$, it is assumed that the structure is returned to its undamaged health state with probability 0.99 and remains in its current state with probability 0.01 . The conditional probability distribution $P\left(H_{t+1} \mid H_{t}, d_{t}=0\right)$ is shown in Table 3.

For simplicity, within the decision process it is assumed that utilities may be attributed directly to the future health state $H_{t+1}$ of the structure without the need for modelling a specific failure

Table 2: The conditional probability table $P\left(H_{t+1} \mid H_{t}, d_{t}\right)$ for $d_{t}=0$.


Table 3: The conditional probability table $P\left(H_{t+1} \mid H_{t}, d_{t}\right)$ for $d_{t}=1$.


mode. The utility function used for the current case study was specified so as to reflect the relative utility values that may be expected in a typical SHM application. The utility function $U\left(H_{t+1}\right)$ is given in Table 4. Here, States 1 and 2, in which the structure $S$ is fully functional are assigned some positive utility, State 3 in which the structure is functional but with reduced capacity is assigned a lesser positive utility, and State 4 for which the structure is non-operational is assigned a relatively large negative utility to reflect the loss of functionality and some additional severe consequence associated with the failure, e.g. risk to human life.

Table 4: The utility function $U\left(H_{t+1}\right)$.


Finally, it is also assumed that the health state $H_{t}$ may be inferred via the use of a statistical classifier by observing a set of discriminative features $\boldsymbol{\nu}_{t}=\left\{\nu_{t}^{1}, \nu_{t}^{2}\right\}$. The ground-truth health state at time $t$ may be obtained via inspection at the cost of $C_{\text {ins }}=7$.

# 5.2. Statistical classifier 

The statistical classifier employed here was one similar to that used in [7] - a mixture of four multivariate Gaussian distributions learned in a supervised manner from the initial labelled dataset $\mathcal{D}_{l}$. Each Gaussian component defines a generative model for the discriminative features $\boldsymbol{\nu}_{t}$, given each of four possible health states of interest in the domain of $H_{t}$,

$$
p\left(\boldsymbol{\nu}_{t} \mid H_{t}=k\right)=\mathcal{N}\left(\boldsymbol{\mu}_{k}, \Sigma_{k}\right)
$$

where $\boldsymbol{\mu}_{k}$ and $\Sigma_{k}$ are parameters of the multivariate Gaussian distribution corresponding to the mean and covariance, respectively. In addition to the mean and covariance parameters of the Gaussian components, the mixture model requires specification of $p\left(H_{t}\right)$,

$$
H_{t} \sim \operatorname{Cat}(\boldsymbol{\lambda})
$$

where the categorical distribution is parametrised by a set of mixing proportions $\boldsymbol{\lambda}=\left\{\lambda_{1}, \lambda_{2}, \lambda_{3}, \lambda_{4}\right\}$ such that,

$$
P\left(H_{t}=k\right)=\lambda_{k}
$$

and,

$$
\sum_{k=1}^{4} P\left(H_{t}=k\right)=\sum_{k=1}^{4} \lambda_{k}=1
$$

The parameters of the Gaussian mixture model that describe the generative statistical distribution $p\left(H_{t}, \boldsymbol{\nu}_{t}\right)$ can be summarised as,

$$
\boldsymbol{\Theta}=\left\{\left(\boldsymbol{\mu}_{1}, \Sigma_{1}, \lambda_{1}\right), \ldots,\left(\boldsymbol{\mu}_{4}, \Sigma_{4}, \lambda_{4}\right)\right\}
$$

In order to learn the parameters $\boldsymbol{\Theta}$ from $\mathcal{D}_{l}$ in a manner that avoids over-fitting, a Bayesian approach was adopted here. In this approach, the parameters $\boldsymbol{\Theta}$ were treated as random variables with a prior placed over them. For conjugacy with the multivariate Gaussian distribution, a Normal-inverse-Wishart (NIW) prior was chosen such that,

$$
\boldsymbol{\mu}_{k}, \Sigma_{k} \sim \operatorname{NIW}\left(\boldsymbol{m}_{0}, \kappa_{0}, v_{0}, S_{0}\right)
$$

where $\boldsymbol{m}_{0}, \kappa_{0}, v_{0}$ and $S_{0}$ are hyperparameters of the probabilistic mixture model. These hyperparameters can be interpreted in the following way [13]: $\boldsymbol{m}_{0}$ is the prior mean for each class mean $\boldsymbol{\mu}_{k}$, and $\kappa_{0}$ specifies the strength of the prior; $S_{0}$ is proportional to the prior mean for each class covariance $\Sigma_{k}$, and $v_{0}$ specifies the strength of that prior. The hyperparameters were specified such that each class $H_{t}$ was initially represented as a zero-mean and unit-variance Gaussian distribution.

As a conjugate to the categorical distribution, a Dirichlet prior was placed over the mixing proportions $\boldsymbol{\lambda}$,

$$
\boldsymbol{\lambda} \sim \operatorname{Dir}(\boldsymbol{\alpha})
$$

and

$$
p(\boldsymbol{\lambda}) \propto \prod_{k=1}^{4} \lambda_{k}^{\alpha_{k}-1}
$$

where $\boldsymbol{\alpha}=\left\{\alpha_{1}, \ldots, \alpha_{4}\right\}$ are hyperparameters of the mixture model. The hyperparameters were specified such that the prior probability of each class in the mixture model was $\frac{1}{4}$, i.e. each state is equally weighted.

Posterior estimates of the parameters may be calculated using the labelled dataset $\mathcal{D}_{l}$. As conjugate priors were used, updates of the parameters may be computed analytically to obtain the posterior NIW distribution given by [16],

$$
\boldsymbol{\mu}_{k}, \Sigma_{k} \mid H_{t}=k, \mathcal{D}_{l} \sim \operatorname{NIW}\left(\boldsymbol{m}_{n}, \kappa_{n}, v_{n}, S_{n}\right)
$$

where $\boldsymbol{m}_{n}, \kappa_{n}, v_{n}, S_{n}$ are the updated parameters and are computed as follows,

$$
\begin{gathered}
\boldsymbol{m}_{n}=\frac{\kappa_{0}}{\kappa_{0}+n_{k}} \boldsymbol{m}_{0}+\frac{n_{k}}{\kappa_{0}+n_{k}} \hat{\boldsymbol{\nu}}_{k} \\
\kappa_{n}=\kappa_{0}+n_{k} \\
v_{n}=v_{0}+n_{k} \\
S_{n}=S_{0}+S+\kappa_{0} \boldsymbol{m}_{0} \boldsymbol{m}_{0}^{\top}-\kappa_{n} \boldsymbol{m}_{n} \boldsymbol{m}_{n}^{\top}
\end{gathered}
$$

where $n_{k}$ is the number of observations in $\mathcal{D}_{l}$ with label $k, \hat{\boldsymbol{\nu}}_{k}$ is the sample mean of observations with label $k$, and $S$ is the empirical scatter matrix given by the uncentered sum-of-squares for observations in class $k, S=\sum_{i \in \mathbb{I}_{k}} \boldsymbol{\nu}_{i} \boldsymbol{\nu}_{i}^{\top}$ where $\mathbb{I}_{k}$ is the set of indices for observations with label $k$.

The posterior distribution of the mixing proportions $\boldsymbol{\lambda}$ remains Dirichlet, and is given by [16],

$$
p\left(\boldsymbol{\lambda} \mid \mathcal{D}_{l}\right) \propto \prod_{k=1}^{4} \lambda_{k}^{n_{k}+\alpha_{k}-1}
$$

To make class predictions for unlabelled data in $\mathcal{D}_{u}$, the posterior predictive distributions over the labels and observations can be obtained by marginalising out the parameters of the model. The posterior predictive distribution for unlabelled observations is obtained via the following marginalisation,

$$
p\left(\boldsymbol{\nu}_{t} \mid H_{t}=k, \mathcal{D}_{l}\right)=\iint p\left(\boldsymbol{\nu}_{t} \mid \boldsymbol{\mu}_{k}, \Sigma_{k}\right) p\left(\boldsymbol{\mu}_{k}, \Sigma_{k} \mid H_{t}=k, \mathcal{D}_{l}\right) d \boldsymbol{\mu}_{k} d \Sigma_{k}
$$

resulting in the Student- $t$ distribution [13],

$$
\boldsymbol{\nu}_{t} \mid H_{t}=k, \mathcal{D}_{l} \sim \mathcal{T}\left(\boldsymbol{m}_{n}, \frac{\kappa_{n}+1}{\kappa_{n}\left(v_{n}-D+1\right)} S_{n}, v_{n}-D+1\right)
$$

where $\boldsymbol{m}_{n}, \kappa_{n}, v_{n}, S_{n}$ are the updated hyperparameters and $D$ is the dimensionality of the feature space. Here, the first two parameters of the Student- $t$ distribution correspond to the mean and scale, respectively. The third parameter specifies the degrees of freedom. The full functional form of the Student- $t$ distribution can be found in [13].

Similarly, the posterior predictive distribution over the labels is obtained via the following marginalisation,

$$
p\left(H_{t} \mid \mathcal{D}_{l}\right)=\int p\left(H_{t} \mid \boldsymbol{\lambda}\right) p\left(\boldsymbol{\lambda} \mid \mathcal{D}_{l}\right) d \boldsymbol{\lambda}
$$

resulting in,

$$
p\left(H_{t}=k \mid \mathcal{D}_{l}\right)=\frac{n_{k}+\alpha_{k}}{n+\alpha_{0}}
$$

where $n=\sum_{k=1}^{4} n_{k}$ and $\alpha_{0}=\sum_{k=1}^{4} \alpha_{k}$.
Finally, the predictive distribution for the class labels given a new unlabelled observation $\boldsymbol{\nu}_{t}$ can be obtained using the posterior predictive distribution and applying Bayes' rule [7],

$$
p\left(H_{t}=k \mid \boldsymbol{\nu}_{t}, \mathcal{D}_{l}\right)=\frac{p\left(\boldsymbol{\nu}_{t} \mid H_{t}=k, \mathcal{D}_{l}\right) p\left(H_{t}=k \mid \mathcal{D}_{l}\right)}{p\left(\boldsymbol{\nu}_{t} \mid \mathcal{D}_{l}\right)}
$$

In summary, a Gaussian mixture model was trained in a supervised Bayesian manner on $\mathcal{D}_{l}$ and subsequently retrained as $\mathcal{D}_{l}$ was extended via the risk-based active querying process. The classifier developed allows a probability distribution over possible health states to be obtained following an observation of the discriminative features.

# 5.3. Results 

The complete dataset associated with the structure $S$ in its various health states of interest $H_{t} \in\{1,2,3,4\}$ was comprised of 1997 data points and is shown in Figure 9. The data were generated to be representative of typical changes in SHM feature spaces due to progressive damage. One half of the data were randomly selected and set aside to form an independent test set, the remaining data were used to form the dataset $\mathcal{D}$.

A small ( $1.5 \%$ ) random subset of $\mathcal{D}$ was annotated with their corresponding labels to initialise $\mathcal{D}_{l}$ and the statistical classifier; it was ensured that at least one data point from each of the four classes was included in $\mathcal{D}_{l}$ upon initialisation. The remaining data $\mathcal{D}_{u}$ were left unlabelled to be sequentially presented to the decision model in the risk-based active learning process. An example of an initial model learned from $\mathcal{D}_{l}$ is shown in Figure 10 with data points in $\mathcal{D}_{l}$ circled.

It can be seen from Figure 10 that, in general, the initial model fits the data poorly as a result of insufficient data. The best fitted Gaussian component of the mixture model is for $H_{t}=2$; this is to be expected, since this cluster lies close to the zero-mean of the prior distribution. The EVPI across the feature space given the initial model is shown in Figure 11.

![img-10.jpeg](img-10.jpeg)

Figure 9: The 2-dimensional feature space of the complete dataset.
![img-11.jpeg](img-11.jpeg)

Figure 10: An initial statistical classifier $p\left(\boldsymbol{\nu}_{t}, H_{t}, \boldsymbol{\Theta}\right)$ learned from the original labelled dataset $\mathcal{D}_{l}$; maximum a posteriori (MAP) estimate of the mean $(+)$ and covariance (ellipses represent $2 \sigma$ ).

![img-12.jpeg](img-12.jpeg)

Figure 11: The EVPI over the two-dimensional feature space given the initial model shown in Figure 10.

Figure 11 shows the regions of high and low value of information. At this stage, it is worth reminding oneself that the expected value of information arises when obtaining information results in a change in policy; areas of high EVPI correspond to regions in the feature space where there is classification uncertainty in the vicinity of decision boundaries given the current model. Bearing this in mind, one can justify the observation that the feature space around the learned Gaussian component for Class 1 (corresponding to the structure being undamaged) has low EVPI. Additionally, the region of the feature space in the overlap between the learned Gaussian distributions for Class 1 and Class 2 (minor damage), where there is uncertainty between the two classes, has low EVPI as the optimal policy is unchanged regardless of whether the structure is in State 1 or State 2. On the other hand, areas with high EVPI correspond to regions of the feature space where there is classification uncertainty between a benign state and a more worrisome state; an example of this is the dominant vertical band of high EVPI feature space that corresponds to the set of points equidistant (Mahalanobis distance) from the learned clusters for State 1 and State 4 .

The labelled dataset $\mathcal{D}_{l}$ was extended according to the risk-based active learning process presented in Section 4. Data points $\boldsymbol{\nu}_{l}$ in $\mathcal{D}_{u}$ were considered in random order one-at-a-time and had their EVPI computed given the current model. A data point was queried, annotated with a label, and incorporated into $\mathcal{D}_{l}$ if the data point met the condition EVPI $>C_{\text {ins }}$. After each query, the statistical classifier was retrained on the newly-extended $\mathcal{D}_{l}$. After being presented with each data point in $\mathcal{D}_{u}$ one at a time, a final model trained on the fully-extended dataset in $\mathcal{D}_{l}$ is shown in Figure 12.

It can be seen from Figure 12 that data in Classes 2 and 3 have been preferentially queried, particularly in the overlap between clusters; this is to be expected because of the associated classification uncertainty between states that warrant different maintenance policies. It can be seen that very few samples have been made for data points belonging to States 1 and 4, resulting in poorly-fitting learned distributions. This result can be explained by again considering the EVPI of the feature space shown in Figure 10, which shows low value of information in the regions around those data.

![img-13.jpeg](img-13.jpeg)

Figure 12: A final statistical classifier $p\left(\boldsymbol{\nu}_{t}, H_{t}, \boldsymbol{\Theta}\right)$ learned from the extended labelled dataset $\mathcal{D}_{\mathrm{I}}$; maximum a posteriori (MAP) estimate of the mean $(+)$ and covariance (ellipses represent $2 \sigma$ ).
![img-14.jpeg](img-14.jpeg)

Figure 13: The EVPI over the two-dimensional feature space given the final model shown in Figure 12.

Figure 13 shows the EVPI over the feature space after the statistical classifier has been trained on the fully-extended version of $\mathcal{D}_{l}$. Similarities can be seen between Figure 11 and Figure 13 such as areas of low EVPI and the bands of high EVPI in regions equidistant from clusters corresponding to states that warrant differing maintenance actions. Figure 13 also shows a region of high EVPI that lies between the estimated means for the distributions learned for States 3 and 4; this is where the boundary between the structure being operational, and the structure being non-operational and requiring repair, lies. This result may indicate that the risk-based active learning approach preferentially incorporates data that strengthen decision boundaries.

To evaluate the change in classifier decision performance throughout the active learning process, the decision accuracy achieved on the independent test set was computed after each retraining of the classifier. The active learning process was repeated 1000 times using different random number generator seeds so that the data selected to be in $\mathcal{D}$ and the initial subset $\mathcal{D}_{l}$ were randomly varied. The mean and standard deviation of the decision accuracy as a function of the number of queries is shown in Figure 14. The mean and standard deviation of the decision accuracy for a classifier trained on $\mathcal{D}_{l}$ when extended with randomly-queried data points is also shown for comparison.
![img-15.jpeg](img-15.jpeg)

Figure 14: The variation in decision accuracy with number of label queries for an agent utilising a statistical classifier trained on $\mathcal{D}_{l}$ extended via (i) risk-based active querying (EVPI) and (ii) random sampling (Random). The dashed lines show $\pm 1 \sigma$.

The decision accuracy can be seen to increase more rapidly when guided by querying according to EVPI rather than random sampling, which suggests that incorporating data labels with high expected value into a classifier will improve an agent's decision-making. After approximately 20 queries, the improvement in decision accuracy gained per query is greatly reduced. Upon close examination, it can be seen that after 28 queries, the decision accuracy begins to decrease slightly. This may be a result of sampling bias introduced via the active learning process and will be further discussed in Section 7.

In summary, a risk-based approach to active learning was demonstrated for a representative numerical case study. A simple maintenance decision problem was formed for a structure with four key health states of interest, and EVPI was used to trigger 'inspections' to obtain class-label information corresponding to structural health states.

# 6. Experimental Case Study 

The risk-based active learning framework was applied to a dataset obtained from the Z24 Bridge [17]. The Z24 bridge was a concrete highway bridge near Solothurn in Switzerland, between the municipalities of Koppigen and Utzenstorf. Prior to demolition, the bridge was the focus of a cross-institutional research project (SIMCES), the goal of which was to provide a benchmark and prove the feasibility of vibration-based SHM [18, 19]. The Z24 Bridge benchmark has been widely used for SHM and modal analysis applications. The monitoring campaign on the bridge spanned a period of 12 months, during which time the bridge was instrumented with sensors to capture both the dynamic response of the structure and environmental conditions including air temperature, deck temperature, humidity and wind speed [20].

From the dynamic response measurements acquired, the first four natural frequencies of the structure were obtained. The variation in these natural frequencies throughout the monitoring campaign are shown in Figure 15. The dataset contains 3932 observations of the natural frequencies in total. Towards the end of the campaign, incremental damage was introduced to the structure artificially, beginning at observation 3476. Additionally, throughout the campaign, the bridge exhibited cold temperature effects, particularly prominent between observations 1200 and 1500. These are believed to be a result of the stiffening of the asphalt layer in the bridge deck induced by very low ambient temperatures.
![img-16.jpeg](img-16.jpeg)

Figure 15: Time history of the first four natural frequencies for the Z24 bridge.
To define a classification problem on which to apply risk-based active learning, the first four natural frequencies of the bridge were selected as the discriminative features such that $\boldsymbol{\nu}_{t} \in \mathbb{R}^{4}$. Furthermore, there are assumed to be four distinct classes of interest $H_{t} \in\{1,2,3,4\}$ :

- Class 1: normal undamaged condition (green)
- Class 2: cold temperature undamaged condition (blue)
- Class 3: incipient damaged condition (orange)

- Class 4: advanced damaged condition (pink).

Here, it has been assumed that the damaged data may be separated into two halves; the earlier half corresponding to incipient damage and the later half corresponding to advanced damage. It is believed that this is a reasonable assumption, given the incremental addition of damage during the monitoring campaign [17]. Furthermore, it is supported by the unsupervised clustering achieved using the Dirichlet process in [21]. The normal undamaged data are separated from the cold temperature effects using outlier analysis via the Minimum Covariance Determinant algorithm $[22,23]$.

# 6.1. Decision process 

Again, to undertake risk-based active learning, one must consider the decision process for the structure. As the bridge is long since demolished, here, a similar decision process to that considered for the visual example presented in Section 5 will be considered. This decision process focusses on a binary decision $d_{t}$ where $d_{t}=0$ corresponds to 'do nothing' and $d_{t}=1$ corresponds to 'perform maintenance'. Because of the similar nature of the problems, the influence diagram shown in Figure 8 can be used to represent the decision process considered for the Z24 bridge. However, the utility functions and conditional probability distributions defined by the influence diagram must be altered to reflect the operational context of the bridge.

The utilities associated with the decision $d_{t}$ specified by the utility function $U\left(d_{t}\right)$ are presented in Table 5. It is assumed that the 'do nothing' action has zero utility, whereas the 'perform maintenance' action has negative utility. Once again, the utilities for the current case study have been selected such that the relative values are appropriate for demonstrating the risk-based active learning approach. As discussed earlier, more representative or exact utilities may be obtained with the aid of expert judgement.

Table 5: The utility function $U\left(d_{t}\right)$ for the Z24 bridge where $d=0$ and $d=1$ denote the 'do nothing' and 'perform maintenance' actions, respectively.


For the decision action 'do nothing', the state transitions are specified such that the structure monotonically degrades, with a propensity to remain in its current state. For the current case study, however, there is the subtlety that States 1 and 2 both correspond to the undamaged health state but under differing environmental conditions. Here, the earlier assumption that there is a propensity to remain in the current state is exploited; simply, asserting that if the temperature is cold for any given measurement, it is more likely than not that the subsequent measurement will also be made at a cold temperature. The same reasoning is also applied to normal temperature conditions (if only weather forecasting really were so simple!). These assumptions are reflected in the conditional probability distribution $P\left(H_{t+1} \mid H_{t}, d_{t}=0\right)$ shown in Table 6. Here, the assumed distributions are sufficiently representative to demonstrate the risk-based active learning process. However, in practice, on may use degradation modelling, climate modelling and expert elicitation to develop these transition models. Moreover, it is worth acknowledging that, for some applications, it may be desirable to remove the effects of environmental and operational variables. This removal process has been demonstrated in [24].

The counterpart to the conditional probability distribution shown in Table $6, P\left(H_{t+1} \mid H_{t}, d_{t}=1\right)$, specifying the state transition probabilities given $d_{t}=1$ is shown in Table 7. This conditional probability distribution is based on the assumption that the 'perform maintenance' action returns the structure to one of the two undamaged states with high probability. The probabilities constituting this distribution, given the structure is in one of the two undamaged states initially, are specified such that the future undamaged state is independent of the action being undertaken. This assumption is, of course, a natural one to make due to the reasoning that (chaos theory aside) the act of repairing the bridge does not influence the weather. The remaining probabilities, conditional

Table 6: The conditional probability table $P\left(H_{t+1} \mid H_{t}, d_{t}\right)$ for $d_{t}=0$.


on the structure being in one of the two damaged states initially, are specified in a similar manner. Firstly, it is assumed that there is a small probability that the maintenance has no effect and the structure remains in its damaged state. Secondly, it is assumed that the remaining probability is attributed to each of the undamaged states in accordance with the stationary distribution obtained when considering the probability of being in normal or cold temperatures in the distant future. This assumption is made as the classes corresponding to damaged states do not distinguish between temperatures and therefore provide no information regarding which of the undamaged states the structure is likely to be returned to. More formally, it is asserted that,

$$
\begin{aligned}
P\left(H_{t+1}=1 \vee H_{t+1}=2 \mid H_{t}=3 \vee H_{t}\right. & \left.=4, d_{t}=1\right)= \\
& P\left(H_{t+1}=1 \vee H_{t+1}=2 \mid H_{t}=1 \vee H_{t}=2, d_{t}=1\right)^{\infty}
\end{aligned}
$$

where $\vee$ is the OR logical operator. As it is implicitly assumed that the states $H_{t}$ are mutually exclusive this is also equivalent to the XOR logical operator.

Table 7: The conditional probability table $P\left(H_{t+1} \mid H_{t}, d_{t}\right)$ for $d_{t}=1$.


For simplicity, it is once again assumed that utilities may be attributed directly to the states of interest for this decision problem. The utility function $U\left(H_{t+1}\right)$ is shown in Table 8 . Here, the undamaged states associated with the bridge are assigned small positive utilities as reward for the bridge being functional with minimal risk of failure. The incipient damage state is assigned moderately-sized negative utility to reflect possible reduced functionality or low-to-moderate risk of failure. The advanced damage state is assigned a very large negative utility to reflect the high risk associated with the failure of the bridge.

Table 8: The utility function $U\left(H_{t+1}\right)$.


Finally, the cost of inspection is specified to be $C_{\text {ins }}=30$. This moderate cost reflects the time required to inspect a large-scale structure such as a bridge.

# 6.2. Statistical classifier 

Once again, a probabilistic Gaussian mixture model was used as the statistical classifier; trained repeatedly in a supervised manner as $\mathcal{D}_{l}$ was extended via risk-based querying process. As

previously mentioned, the discriminative features used were the first four natural frequencies of the bridge, normalised with respect to the mean and standard deviations. The targets of the classifier were the four states of interest corresponding to two undamaged and two damaged states.

# 6.3. Results 

As previously mentioned, the Z24 dataset comprises of 3932 observations. Once again, these data were divided in half to form a training dataset and a test dataset. A small ( $1 \%$ ) random subset of the training dataset $\mathcal{D}$ was assigned to the initial labelled dataset $\mathcal{D}_{l}$ and the remaining data assigned to the unlabelled dataset $\mathcal{D}_{u}$ to be sequentially presented to the decision model in the risk-based active learning process. To facilitate visualisation, the four-dimensional feature space was projected down onto two-dimensions using principal component analysis [25]. The two-dimensional projection of the Z24 dataset is shown in Figure 16.
![img-17.jpeg](img-17.jpeg)

Figure 16: A two-dimensional projection of the feature space for the complete Z24 dataset.
An example of an initial model learned from the subset $\mathcal{D}_{l}$ is shown in Figure 17 with data in $\mathcal{D}_{l}$ circled. It can be seen from Figure 17, that it appears the Gaussian distribution best learned corresponds to the class $H_{t}=1$. The reasons for this are twofold, the data for this class are positioned closest to zero-mean of the prior, and more datapoints belonging to this class were, by chance, included in the initial labelled dataset $\mathcal{D}_{l}$. The other three distributions appear to have been learned poorly, being heavily influenced by the prior.

Figure 18 shows the EVPI contours over the projected feature space. It can be seen that there are regions of high expected value around the edges of the normal undamaged cluster (Class 1), this is intuitively understood by considering the adjacent regions of low expected value. The low-value region bounded by the high-value region occurs as a result of the classifier being confident that the structure is in its undamaged condition and therefore the decision-maker is confident that the optimal decision is 'do nothing'. Conversely, the low-value region enclosing the high-value region occurs as a result of the tolerable risk of damage/failure having been exceeded, as such the decision-maker is confident that the optimal decision for data in this region is 'perform maintenance'. Again, Figure 18 shows that there are larger swathes of high-value, corresponding to regions of high uncertainty between undamaged and damaged states.

![img-18.jpeg](img-18.jpeg)

Figure 17: A two-dimensional projection of an initial statistical classifier $p\left(\boldsymbol{\nu}_{t}, H_{t}, \boldsymbol{\Theta}\right)$ learned from the initial labelled dataset $\mathcal{D}_{l}$; maximum a posteriori (MAP) estimate of the mean $(+)$ and covariance (ellipses represent $2 \sigma$ ).
![img-19.jpeg](img-19.jpeg)

Figure 18: The EVPI over the two-dimensional projection the feature space given the two-dimensional projection of the initial model shown in Figure 17.

The laballed dataset $\mathcal{D}_{l}$ was extended via the risk-based active learning process as data were presented to the decision process in sequential order one-at-a-time. Again, labels for datapoints were queried and the classifier retrained on the extended dataset when the criterion EVPI $>C_{\text {ins }}$ was satisfied. The final model, corresponding to the updated version of the initial model shown in Figure 17 following risk-based active learning, is shown in Figure 19.
![img-20.jpeg](img-20.jpeg)

Figure 19: A two-dimensional projection of a final model statistical classifier $p\left(\boldsymbol{\nu}_{t}, H_{t}, \boldsymbol{\Theta}\right)$ learned from the extended labelled dataset $\mathcal{D}_{l}$; maximum a posteriori (MAP) estimate of the mean $(+)$ and covariance (ellipses represent $2 \sigma$ ).

It can be seen in Figure 19 that the active learner has preferentially queried datapoints belonging to Class 1 and, to a lesser extent, Class 2. Data on the boundary between Classes 1 and 3 appears to have been particularly heavily sampled. This observation is, again, to be expected when considering the distribution of EVPI shown in Figure 18, which shows low-value regions in the vicinity of advanced-damage data and high-value regions on the boundary of Class 1.

Figure 20 shows the EVPI over the projected feature space given a projection of the final model. Figure 20 shows very well-defined 'rings' of high expected value. Once again, the areas inside these rings can be considered regions on the feature space where the classifier is sufficiently confident that the structure is currently, and will be in the subsequent time-step, in an undamaged state such that the decision-maker can be confident that 'do nothing' is the optimal action without the need for inspection of the structure. Likewise, areas outside of the rings correspond to regions of the feature space where the decision-maker may be confident that 'perform maintenance' is the optimal action.

By comparison of Figures 18 and 20, it can be seen that the swathes of high-value feature space are replaced with a ring of high-value, associated with the cold temperature undamaged class. Additionally, the ring associated with the normal undamaged class becomes tighter. These phenomena indicate that, with hindsight, one can deem an agent utilising the initial classifier to be over-confident in its decision-making. For the current case study, it is to be expected that the areas in which a decision-maker can be confident that the 'do nothing' action are small because of the large negative utility associated with the advanced damage class and the large resulting risk. In fact, if one reduces the cost associated with the bridge being in its advanced damage state, then one can expect the rings to grow larger as the region of tolerable risk expands. This can be

![img-21.jpeg](img-21.jpeg)

Figure 20: The EVPI over the two-dimensional projection the feature space given a 2-dimensional projection of the final model shown in Figure 19.
observed in the merging of the rings shown in Figure 21. The final model shown in Figure 21 was learned with the cost associated with the advanced damage state reduced from 1000 to 500 .

Throughout the active learning process, the decision-making performance of an agent was evaluated by evaluating the decision accuracy for data in the independent test set. The active learning process was repeated 1000 times with differing random number generator seeds such that the data in $\mathcal{D}$ and the initial subset $\mathcal{D}_{l}$ were randomly varied. The mean and standard deviation of the decision accuracy as a function of the number of queries is shown in Figure 22. For comparison, the decision accuracy for a classifier training on a labelled dataset extended via random sampling is also shown.

The decision accuracy can be seen to improve almost monotonically when using risk-based active learning, as opposed to random sampling which initially results in a degradation in performance before improving. For risk-based active learning, in addition to the mean value of decision accuracy reaching close to unity with fewer queries than random sampling, the variance of the decision accuracy also converges more rapidly. This result indicates that using risk-based active learning may result in more consistent decision-making performance. Upon closer examination, it can be seen that, for higher numbers of queries, the decision accuracy slightly declines. This observation and the initial decrease in accuracy for random sampling can be explained by sampling bias, which is discussed further in the penultimate Section 7.

To summarise, risk-based active learning was applied to a 'real-world' case study, specifically the Z24 Bridge benchmark for SHM. A simple maintenance decision problem was constructed for the bridge. A probabilistic Gaussian mixture model was employed to distinguish between four salient states of interest using natural frequencies as a discriminative feature. The EVPI of incipient data points with respect to the decision process was used to guide the querying of health-state labels where querying would correspond to the inspection of the bridge.

![img-22.jpeg](img-22.jpeg)

Figure 21: The EVPI over the two-dimensional projection the feature space given a 2-dimensional projection of the final model learned when $U\left(H_{t}=4\right)=-500$.
![img-23.jpeg](img-23.jpeg)

Figure 22: The variation in decision accuracy with number of label queries for an agent utilising a statistical classifier trained on $\mathcal{D}_{l}$ extended via (i) risk-based active querying (EVPI) and (ii) random sampling (Random). The dashed lines show $\pm 1 \sigma$.

# 7. Discussion 

The results presented in Sections 5 and 6 indicate that making inspections of structures according to a risk-based active learning heuristic may provide a cost-effective method of developing statistical classifiers for use in decision processes in situations when no, or limited, labelled data are available a priori. Moreover, it is interesting to note from Figures 12 and 19 that classifiers do not necessarily need to accurately model the entire feature space to be useful in decision processes, and in fact, well-fitting models can be foregone in favour of decision performance. That being said, a statistical model that is able to accurately predict health-state labels has the potential to provide additional information such as damage locations and types that may be useful in directing more specific types of maintenance and coordinating repair teams - albeit at a potentially higher cost. Indeed, as the dimensionality of a decision space increases, the need for high classification accuracy becomes more crucial. Nevertheless, it can be said with confidence that the appropriate machine learning paradigm to be used for statistical classifier development in SHM is highly dependent on the context in which the monitoring system is being employed; taking into account factors such as: data availability, knowledge of relevant physics, and the decision support application of the monitoring system itself.

The risk-based approach to active learning presented in the current paper is not without its limitations. Notably, in order to evaluate EVPI as presented, it is necessary to assume that the number of classes (i.e. health states of interest) are known prior to the implementation of a monitoring system. This limits the flexibility of the classifier and may result in the mistreatment of unforeseen health states and associated failure events within the decision framework. Additionally, it is assumed that perfect information of the health state can be acquired my means of inspection. During the inspection procedure, human error may be introduced, and in some scenarios it may be vital to account for this uncertainty in the active learning framework by relaxing the perfect information assumption when possible.

### 7.1. Sampling bias

A noteworthy observation from Sections 5 and 6 that bears further discussion is that, whilst decision accuracy may be increased via risk-based active learning, after a certain number of queries have been made, any incipient data points whose true labels may have high expected value with respect to a structural maintenance decision process, may, in fact, be detrimental to the performance of a decision-maker when incorporated into the statistical classifier on which it relies.

A likely explanation for this observation is the phenomenon known as sampling bias; a known issue associated with active learning that has been documented to impact upon classification performance [7, 26]. Sampling bias occurs when specific regions of feature-space are over/undersampled resulting in a training dataset that is not representative of the underlying distributions; this can clearly be observed in Figure 12. In the numerical example presented in Section 5, sampling bias manifests as unrepresentative mixing proportions $\boldsymbol{\lambda}$, which may result in overconfident misclassifications that subsequently cause erroneous actions to be decided.

### 7.2. Future work

To overcome the dangers of sampling bias, two potential solutions could be considered for future work. The first would be to establish a heuristic-based methodology for switching between value of information-based and uncertainty-based measures for guided sampling. This would have the effect of establishing decision boundaries by querying regions of the feature space with high value of information, while also exploring low likelihood and high information (including low-value) regions of the feature space. An alternative approach would be to incorporate semi-supervised learning techniques [27, 28], such that the label predictions for the unlabelled data $\mathcal{D}_{u}$ may be utilised to retain representative estimates for the mixing proportions.

Another interesting avenue for further investigation is that of risk-based active learning applied to more complex decision spaces, such that the requirements of the statistical classifiers are extended to damage localisation and the identification of different types of damage. The case study presented in the current paper considered only a simply binary decision between 'do nothing'

and 'perform maintenance'. By increasing the number of decisions, and therefore the number of decision boundaries to be learned, the generalisation capabilities of the framework will be tested, as no doubt more queries will be required. This investigation will potentially result in the decision accuracy of the value-based querying approach being superseded by that of the random sampling approach for higher numbers of queries.

# 8. Conclusions 

The aim of the current paper has been to present a risk-based active learning approach for SHM. The approach utilises the expected value of perfect information of incipient data points to instigate inspections, such that structural health information may be obtained and incorporated into probabilistic classifiers. The methodology was demonstrated on a numerical case study to aid in visualisation and understanding of the risk-based active learning process. Additionally, the approach was demonstrated on an experimental dataset obtained from a previously-existing bridge, thereby highlighting its potential applicability to 'real-world' engineering problems. The results of the case studies indicated that the risk-based approach to active learning has the potential to provide a cost-effective solution to the development of decision-supporting SHM systems. This finding is valuable as, ordinarily, the comprehensive labelled datasets necessary for the fully-supervised learning of statistical classifiers are seldom available at the inception of a monitoring system.

## Acknowledgements

The authors would like to acknowledge the support of the UK EPSRC via the Programme Grant EP/R006768/1. KW would also like to acknowledge support via the EPSRC Established Career Fellowship EP/R003625/1.

## Conflict of interest

The authors declare that they have no conflict of interest.

# Appendix A. EVPI Calculation 

An illustrative calculation of the EVPI is provided here, based upon the example presented in Section 5 .

Consider Figure 8 as the influence diagram of the original decision process $\mathcal{I}$. The corresponding modified influence diagram $\mathcal{I}_{\boldsymbol{H}_{i} \rightarrow d_{i}}$ is shown below in Figure A.23.
![img-24.jpeg](img-24.jpeg)

Figure A.23: An influence diagram representation of the modified decision process associated with structure $S$.
With the EVPI given by equation (4), one must first calculate the MEU for the decision process represented by $\mathcal{I}$. The MEU for $\mathcal{I}$ is given by,

$$
\operatorname{MEU}(\mathcal{I})=\max _{d_{t}}\left[\sum_{H_{t}} \sum_{H_{t+1}} P\left(H_{t} \mid \boldsymbol{\nu}_{t}\right) P\left(H_{t+1} \mid H_{t}, d_{t}\right) U\left(H_{t+1}\right)+U\left(d_{t}\right)\right]
$$

For the purposes of the demonstration, it will be assumed that the classifier has predicted $P\left(H_{t} \mid \boldsymbol{\nu}_{t}\right)=\{0.4,0.3,0.2,0.1\}$, otherwise, the remaining conditional probability distributions and utility functions are as specified in Section 5. Employing equation (A.1), one can compute that $\operatorname{MEU}(\mathcal{I})=-4.4$

Next, one must calculate the MEU for the decision process represented by the influence diagram $\mathcal{I}_{H_{t} \rightarrow d_{t}}$. This is given by,

$$
\operatorname{MEU}\left(\mathcal{I}_{H_{t} \rightarrow d_{t}}\right)=\sum_{H_{t}} \max _{d_{t}}\left[\sum_{H_{t+1}} P\left(H_{t} \mid \boldsymbol{\nu}_{t}\right) P\left(H_{t+1} \mid H_{t}, d_{t}\right) U\left(H_{t+1}\right)+U\left(d_{t}\right)\right]
$$

Applying equation (A.2) and again taking $P\left(H_{t} \mid \boldsymbol{\nu}_{t}\right)=\{0.4,0.3,0.2,0.1\}$, one determines $\operatorname{MEU}\left(\mathcal{I}_{H_{t} \rightarrow d_{t}}\right)=1.015$.

Finally, the EVPI of observing $H_{t}$ prior to making the decision $d_{t}$, or the expected value of inspecting the structure, can be trivially calculated with equation (4) to be,

$$
\operatorname{EVPI}\left(d_{t} \mid H_{t}\right)=1.015--4.4=5.415
$$