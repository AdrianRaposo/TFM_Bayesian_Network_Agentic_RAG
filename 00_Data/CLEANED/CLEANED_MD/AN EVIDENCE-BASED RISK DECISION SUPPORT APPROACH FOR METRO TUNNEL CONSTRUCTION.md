# AN EVIDENCE-BASED RISK DECISION SUPPORT APPROACH FOR METRO TUNNEL CONSTRUCTION 

Yifan GUO ${ }^{1}$, Junjie ZHENG ${ }^{1 *}$, Rongjun ZHANG ${ }^{1}$, Youbin YANG ${ }^{2}$<br>${ }^{1}$ School of Civil Engineering \& Mechanics, Huazhong University of Science and Technology, Wuhan, China<br>${ }^{2}$ China Railway Siyuan Survey and Design Group Co., LTD, Kunming, China

Received 26 May 2020; accepted 13 January 2022


#### Abstract

The risk-informed decision-making of metro tunnel project is often faced with the problem of inadequate utilization of available information. In order to address the epistemic uncertainty problem caused by insufficient utilization of information in decision-making, this paper proposes a risk decision support approach for metro tunnel construction based on Continuous Time Bayesian Network (CTBN) technique. CTBN can factor the state space of variables in tunnel projects and perform evidence-based reasoning, which enables the diverse information of expert opinions, project-specific parameters, historical data and engineering anomalies to be the evidence to support decision-making. A concise CTBN model development method based on Dynamic Fault Trees is presented to replace the cumbersome model learning process. The proposed approach can utilize multi-source information as evidence to provide multi-form decision support both in the pre-construction stage and construction stage of the tunnel construction project, and the results can support the decisions on judging the acceptability of the risk, developing response strategies for risk factors and diagnosing the causes of the hazardous event. A case study on the water leakage risk of tunnel construction in China is presented to illustrate the feasibility of the approach. The case study shows that the approach can assist in making informed decisions, so as to improve the engineering safety.


Keywords: Continuous Time Bayesian Network, evidence, risk-informed decision-making, tunnel construction, knowledge, multi-source information.

## Introduction

Over the past decades, urban metro construction projects have been increasing rapidly in China. Tunnel project is a complicated process with multiple working procedures, which means that practical tunnel project will inevitably face numerous uncertainties in the tunnel construction project. Uncertainties that may affect the safety of tunnel projects can be considered of aleatory uncertainty and epistemic uncertainty (Zio, 2009). Aleatory uncertainty is the natural randomness due to inherent variability of the analyzed system itself, and epistemic uncertainty is the imprecision due to lack of knowledge and information (Ferdous et al., 2013). As the existing of these uncertainties, tunnel projects are tend to impose various risks on all parties involved and on those not directly involved in the projects (Hu \& Huang, 2014). It is significant to make appropriate risk decisions on the risk management of tunnel construction projects. Previous researches on the uncertainty of risks mainly aimed to address single uncertain characteristics, for example, Fuzzy Theory was used
to address the imprecision or subjective fuzziness (Wang \& Chen, 2017), Evidence Theory was used to address the conflict between different information sources (Zhang et al., 2017), Random Field Theory was used to address the inherent random characteristics of geology (Wang et al., 2016), etc. However, previous works were limited because most of them only focused on addressing the uncertainties caused by the scarcity of risk-related information, but rarely considered how to fully utilize the diversity of riskrelated information to reduce uncertainties, and this may bring problems to the interpretability of decision results. In practical engineering, rich available information sources including historical data, expert opinions, project-specific parameters, and engineering anomalies can be collected in the pre-construction stage or construction stage of the tunnel construction project, and this information can be extracted as evidence to support risk-informed de-cision-making. Therefore, an evidence-based risk decision support approach which can fully utilize the diversity of

[^0]
[^0]:    *Corresponding author. E-mail: zhengjj@hust.edu.cn

information is developed to support the decision-making of tunnel construction project.

Continuous Time Bayesian Network (CTBN) model is a probabilistic graphical model which fuses Bayesian Networks with Markov Processes. CTBN can factor the state space of variables and perform evidence-based reasoning, which enables the utilization of risk-related information. In view of these advantages, the CTBN model is applied in the proposed risk decision support approach of tunnel construction project to address the epistemic uncertainty. The risk-related information is obtained through expert interview, project investigation, and historical data statistics in the pre-construction stage of the tunnel project and through safety patrol and construction monitoring in the construction stage of the tunnel project. Sturlaugson and Sheppard (2016) introduced various types of evidence of the CTBN model. The available information can be extracted as certain or uncertain evidence of the CTBN model to support the decision-making through explicit and tacit knowledge. Moreover, the traditional parameter learning and structure learning method of the CTBN model has high requirements for observation data (Nodelman et al., 2012), an approximate CTBN model development method based on Dynamic Fault Trees (DFTs) is proposed. DFTs define multi-form logic gates to model the failure modes of complex systems and can provide a reliable logical framework for the causality of the hazardous event and risk factors (Boudali et al., 2009), thus the DFT framework can be served as prior knowledge for CTBN structure learning.

Once the CTBN model is developed, multi-form analyses can be performed, aiming to provide safety guidance for the tunnel project in the pre-construction stage and construction stage. Specifically, the result of predictive analysis can help judge the acceptability of the hazardous event in tunnel construction project before it occurs and find the weak positions that need attention, if it is unacceptable, corresponding response strategies for the risk factors can be formulated according to the result of importance analysis. Moreover, when the hazardous event occurs, diagnostic analysis can help identify the most likely causes, and the repair strategies can be formulated accordingly. Špačková (2012) has pointed out that new information can reduce epistemic uncertainty. The CTBN model is developed not only to provide decision support in the pre-construction stage of the tunnel project based on prior information, but also to update the decision with the new information obtained in the construction stage of the tunnel project. Finally, an actual metro tunnel project in China is presented as a case study to demonstrate the feasibility of the developed risk decision support approach.

The remainder of the paper is organized as follows. In Section 1, a literature review of previous relevant researches is provided. In Section 2, fundamental theories are introduced, the method of establishing CTBN model is elucidated, and the risk decision support approach with step-by-step procedures is established. In Section 3, the
proposed approach is applied to the risk-informed deci-sion-making of a metro tunnel construction in China for case study. Finally, some further discussions and conclusions are presented.

## 1. Literature review

Multifarious risk analysis and assessment methods were invented and made prominent contributions to the risk management of complex projects. In previous studies, risk analysis and assessment methods such as Fault Tree Analysis, Event Tree Analysis, Analytic Hierarchy Process, and Exploratory Factor Analysis have been successfully applied in the tunnel projects (Hong et al., 2009; Qu et al., 2011; Hyun et al., 2015; Liu et al., 2018). By implement these methods to the tunnel projects, probabilities and impacts of risks, causes and consequences of undesired events, classification of risk factors, etc. can be acquired. The results of these methods can provide basis for risk control and improve the safety of tunnel projects. However, most of the traditional risk assessment and analysis methods analyzed problems from a single perspective and were unlikely to comprehensively characterize the risks of tunnel projects. Therefore, some more advanced models were proposed to address the risk decision problems of tunnel project under complex environment (Cárdenas et al., 2012; Sousa \& Einstein, 2012; Špačková et al., 2013a; Zhang et al., 2013; Gitinavard, 2019). These approaches were presented to expound how the risk analysis models were used to support risk decision-making in tunnel projects, but few of them provided complete decision-making steps.

In order to improve the risk cognition of tunnel projects, some studies developed risk prediction models, which had the abilities to predict the safety of the tunnel project, provide the risk criteria, and improve the design and construction parameters of the tunnel project (Cao et al., 2018; Li et al., 2019; Liu et al., 2019; Mohammadi \& Azad, 2021). The risk prediction models provided effective ways to identify the explicit and tacit knowledge from the raw risk-related information of tunnel projects. Appropriate risk prediction models can serve as a bridge between the tunnel project information and the professional knowledge. Unfortunately, most of these models were highly abstract and seldom fully consider the complex situation in practical engineering, thus, the results of these models can only provide basis for decision-making in practical engineering, but cannot be used directly for decision-making.

In recent years, the uncertainty of risks that may affect engineering safety has gradually become a research hot spot. Lack of data, simplification of model, imprecision of knowledge, and conflict between different information sources may lead to the uncertainty of risks. Therefore, many theories for addressing these uncertainties were developed. Among them, Fuzzy Theory was used to characterize the uncertainty caused by the lack of data and the imprecision of knowledge (Wang \& Chen, 2017; Mousavi

\& Gitinavard, 2019); Entropy-risk model was developed to quantify the parameter uncertainty and the model uncertainty (Xia et al., 2017); D-S Evidence Theory was presented to address the conflict between different information sources (Zhang et al., 2017); various forms of Bayesian networks were proposed to reduce the uncertainty by data fusion or model updating (Wu et al., 2015; Xie et al., 2021). It can be seen that in comparison with other theories, the advantage of Bayesian-based approaches in coping with uncertainties lies in its ability of model updating and information fusion.

Previous researches for addressing the uncertainty of risks in tunnel projects still existed some limitations, because the main concerns of them were addressing the uncertainty characteristics caused by the scarcity of information but rarely considered how to fully utilize the diversity of risk-related information. The CTBN model can factor the variables into three dimensions: initial state, state transition rate, and time, which enables the multi-source information obtained in the pre-construction stage and construction stage of the tunnel project to be the evidence of decision-making. Therefore, this paper innovatively utilizes CTBN technique to address the uncertainty of risks in tunnel projects through maximizing the benefit of riskrelated information. How to extract the information as evidence to support decision-making is also expounded. Moreover, a discussion on how to increase the certainty degree of uncertain evidence is provided to further reduce the uncertainty. A comparison of several main properties between this paper and some relevant literatures is shown in Table 1 to specify the merits of this study.

## 2. Methodologies

### 2.1. Bayesian Networks

Bayesian Networks is a directed acyclic graph (DAG) composed of a set of variables and directed edges, and each variable with all of their parents is attached by a con-
ditional probability table (Jensen \& Nielsen, 2007). A BN model can be defined as a binary: $B=\langle G, \Theta\rangle . G=\langle V$, $E>$ represents a directed acyclic graph, $V=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ represents a set of nodes, and $E$ represents directed edges between pairs of nodes. The node $x_{i}$ in the node set $V$ represents the $i$ th random variable, the directed edge denotes the association relationship between variables, and $P\left(x_{i}\right)$ represents the marginal probability distribution of $x_{i}$. The starting node of the directed edge is the parent node of the end node, and the parent node of the node $x_{i}$ is denoted as $P a\left(x_{i}\right) . \Theta$ represents the conditional probability distribution (CPD) corresponding to each node. According to the conditional independence assumptions contained in BNs, the CPD of the node $x_{i}$ can be denoted as $P\left(x_{i} \mid P a\left(x_{i}\right)\right)$. $P(V)$ represents the probability distribution over $V$, it is equivalent to $P\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, which means the joint probability distribution (JPD) over the node set $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$. Based on the chain rule, $P(V)$ can be written as Eqn (1):

$$
P(V)=P\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid P a\left(x_{i}\right)\right)
$$

### 2.2. Continuous Time Bayesian Networks

Continuous Time Bayesian Networks can explicitly describe dynamic characteristics of structured state space by temporal evolution of local variables, which enable users to obtain the state probability distribution of specific nodes over time (Gatti et al., 2012). CTBNs are first introduced by Nodelman et al. (2002) and a CTBN model can be defined as follows. $\boldsymbol{X}$ denotes a set of local variables $X_{1}, X_{2}, \ldots, X_{N}$, in which $X_{n}$ has a finite domain of values $\operatorname{Val}\left(X_{n}\right)=\left\{x_{1}(n), x_{2}(n), \ldots, x_{m}(n)\right\}$. A CTBN $\mathcal{N}$ over $\boldsymbol{X}$ is composed of a binary: $\mathcal{N}=\langle\mathcal{B}, \mathcal{G}\rangle$. The first component is an initial distribution $P_{X}^{0}$, designated as $\mathcal{B}$ over $\boldsymbol{X}$. The second component is a continuous transition model which is specified as: (1) A directed graph $\mathcal{G}$ whose nodes are $X_{1}$, $X_{2}, \ldots, X_{N}$, and $P a\left(X_{n}\right)$ denotes the parents of $X_{n}$; (2) A set of conditional intensity matrices (CIMs) $\boldsymbol{Q}_{X_{n}}^{\operatorname{Pat}\left(X_{n}\right)}$ as-

Table 1. Comparison of properties of some risk-informed decision support approaches for tunnel construction.


Notes: $\mathrm{U}^{\Delta}$ - Uncertain evidence; $\mathrm{C}^{\Delta}$ - Certain evidence; $\mathrm{P}^{*}$ - Predictive analysis; $\mathrm{D}^{*}$ - Diagnostic analysis; $\mathrm{I}^{*}$ - Importance analysis; $\mathrm{C}^{*}$ - Continuous time; $\mathrm{D}^{*}$ - Discrete time; $\mathrm{N}^{*}$ - Not considered; $\mathrm{A}^{*}$ - Aleatory uncertainty; $\mathrm{E}^{*}$ - Epistemic uncertainty.

sociated with each variable $X_{n} \in \boldsymbol{X}$ for all of the possible instantiations of $P a\left(X_{n}\right)$. If $X_{n}$ is given, one instantiation of its CIM $\boldsymbol{Q}_{X_{n}}^{P a\left(X_{n}\right)}$ can be presented as Eqn (2):

$$
\boldsymbol{Q}_{X_{n}}^{P a\left(X_{n}\right)}=\left[\begin{array}{cccc}
-q_{x_{1}(n)}^{P a\left(X_{n}\right)} & q_{x_{1} x_{2}(n)}^{P a\left(X_{n}\right)} & \cdots & q_{x_{1} x_{m}(n)}^{P a\left(X_{n}\right)} \\
q_{x_{2} x_{1}(n)}^{P a\left(X_{n}\right)} & -q_{x_{2}(n)}^{P a\left(X_{n}\right)} & \cdots & q_{x_{2} x_{m}(n)}^{P a\left(X_{n}\right)} \\
\vdots & \ddots & \vdots \\
q_{x_{m} x_{1}(n)}^{P a\left(X_{n}\right)} & q_{x_{m} x_{2}(n)}^{P a\left(X_{n}\right)} & \cdots & -q_{x_{m}(n)}^{P a\left(X_{n}\right)}
\end{array}\right]
$$

where $q_{x_{i} x_{j}(n)}^{P a\left(X_{n}\right)}$ denotes the transition intensity from state $q_{x_{i}(n)}^{P a\left(X_{n}\right)}$ to state $q_{x_{j}(n)}^{P a\left(X_{n}\right)}$, and $q_{x_{i}(n)}^{P a\left(X_{n}\right)}=\sum_{x_{j} \neq x_{i}} q_{x_{i} x_{j}(n)}^{P a\left(X_{n}\right)}$ can be interpreted as the instantaneous probability for leaving state $q_{x_{i}(n)}^{P a\left(X_{n}\right)}$ (Stella \& Amer, 2012).

As a CTBN can be seen as a factored Markov Process, formally similar to a BN, the joint intensity matrix (JIM) can be defined as Eqn (3):

$$
\boldsymbol{Q}_{N}=\prod_{n=1}^{N} \boldsymbol{Q}_{X_{n}}^{P a\left(X_{n}\right)}
$$

### 2.3. Formalism transformation from DFT into CTBN

Dynamic Fault Trees can provide a reliability modeling framework based on expert knowledge for the risk of tunnel construction. Some researchers have done previous works on the integration of DFTs/SFTs and CTBNs for reliability modeling (Cao, 2011; Perreault et al., 2015; Codetta-Raiteri \& Portinale, 2017; Forrester et al., 2019). However, these researches do not include the transformation relationship of all logic gates in DFTs to the CTBN model and a complete formalism transformation process. Therefore, this study complements and perfects the previous works, and a detailed transformation method from a DFT structure with all logic gates to the corresponding CTBN formalism is elaborated.

First, some definitions need to be made. It is defined that state 0 denotes a working state and state 1 denotes a failure state. For a given variable $X_{n}$ in the CTBN model whose parent node is denoted as $P a\left(X_{n}\right)$, the conditional failure rate of $X_{n}$ is denoted as $\lambda_{X_{n}}^{P a\left(X_{n}\right)}$, and the conditional repair rate is denoted as $\mu_{X_{n}}^{P a\left(X_{n}\right)}$. If the variable is considered non-reparable, the repair rate will be set to 0 .

The CIM of $X_{n}$ can be expressed as Eqn (4):

$$
\begin{aligned}
& \text { State } 0 \\
& \boldsymbol{Q}_{X_{n}}^{P a\left(X_{n}\right)}=0 \\
& 0\left[\begin{array}{cc}
-\lambda_{X_{n}}^{P a\left(X_{n}\right)} & \lambda_{X_{n}}^{P a\left(X_{n}\right)} \\
\mu_{X_{n}}^{P a\left(X_{n}\right)} & -\mu_{X_{n}}^{P a\left(X_{n}\right)}
\end{array}\right] .
\end{aligned}
$$

The state distribution over $X_{n}$ at time $t, \boldsymbol{P}_{X_{n}}(t)$, can be calculated by Eqn (5):

$$
\boldsymbol{P}_{X_{n}}(t)=\boldsymbol{P}_{X_{n}}^{0} \exp \left[\boldsymbol{Q}_{X_{n}}^{P a\left(X_{n}\right)} \cdot t\right]
$$

The repair strategy is usually formulated after the hazardous event is diagnosed in practical tunnel projects, therefore, the variables are considered non-reparable in
the calculation of failure probability, and $\boldsymbol{P}_{X_{n}}^{0}$ is defined as:

$$
\begin{aligned}
& \text { State } 01 \\
& \boldsymbol{P}_{X_{n}}^{0}=\left[\begin{array}{ll}
1 & 0
\end{array}\right]
\end{aligned}
$$

With above definitions, the failure probability of $X_{n}$ at time $t$ can be calculated by Eqn (7):

$$
F_{X_{n}}(t)=1-\exp \left[-\lambda_{X_{n}}^{P a\left(X_{n}\right)} \cdot t\right]
$$

The variable repair process is similar. If $X_{n}$ is in a failure state and the initial time of repair process is denoted as $s, \boldsymbol{P}_{X_{n}}^{s}$ can be expressed as:

$$
\begin{array}{cc}
\text { State } & 0 \\
\boldsymbol{P}_{X_{n}}^{s} & =\left[\begin{array}{ll}
0 & 1
\end{array}\right]
\end{array}
$$

The repair probability for the transition of $X_{n}$ back to a non-failing state at time $t$ can be calculated by Eqn (9):

$$
R_{X_{n}}(t)=1-\exp \left[-\mu_{X_{n}}^{P a\left(X_{n}\right)} \cdot(t-s)\right]
$$

In a CTBN model, each node is assigned with a corresponding CIM and an initial distribution. The core for developing a CTBN model is to determine the CIMs representing the relationships among nodes. Logic gates expressing failure modes in DFTs can provide prior knowledge to the relationships among nodes. In the following part, six common logic gates are taken as examples to illustrate how DFTs can be converted into CTBN formalisms.

The correspondence between an AND gate and the CTBN representation is shown in Figure 1, and the CIMs of the nodes are listed in Tables 2-4. For node $A$ and node $B$, the expected time of transitioning from state 0 to state 1 are $1 / \lambda_{A}$ and $1 / \lambda_{B}$, and the expected time of transitioning back from state 1 to state 0 are $1 / \mu_{A}$ and $1 / \mu_{B}$ (if the component is non-reparable, then the expected time of transitioning is $1 / 0$ which means infinity). For node $C$, only when both of node $A$ and node $B$ are in state 1 , the transitioning of node $C$ from state 0 to state 1 will occur.

Table 2. CIM of node $A$


Table 3. CIM of node $B$


Table 4. CIM of node $C$


The correspondence between an OR gate and the CTBN representation is shown in Figure 2. The CIMs of node $A$ and node $B$ are the same as in Tables $2-3$, and the CIM of node $C$ is listed in Table 5. For node $C$ in the OR gate, as long as any input node is in state 1 , the transitioning of node $C$ from state 0 to state 1 will occur at once.

How a PAND gate can be converted into the corresponding CTBN representation is exhibited in Figure 3. For a PAND gate with two inputs, this paper defines the latter input node $B$ has a working state and two failure states: state 0 indicates a working state, state 1 indicates that node $A$ is in a failure state when node $B$ fails and state $1^{*}$ indicates that node $A$ is in a working state when node $B$ fails. Only when node $B$ is in state 1 , the state transitioning of node $C$ from state 0 to state 1 will occur. The CIM of node $A$ is the same as in Table 2, and the CIMs of node $B$ and node $C$ are listed in Tables 6-7.

The mapping model from a SEQ gate into its corresponding CTBN representation is demonstrated in Figure 4. The failure of node $A$ is like a trigger to boot up the state transitions of node $B$ (Codetta-Raiteri, 2005). For node $C$, only when node $A$ and node $B$ are both in state 1 , the transitioning from state 0 to state 1 will occur. The CIM of node $A$ is the same as in Table 2, and the CIMs of node $B$ and node $C$ are listed in Tables 8-9.

Table 5. CIM of node $C$


Table 6. CIM of node $B$


Table 7. CIM of node $C$


Table 8. CIM of node $B$


Table 9. CIM of node $C$


Figure 5 provides a mapping model from a FDEP gate into its CTBN representation. The transformation logic of the trigger event node $T$ is just like that in static gates. As for the dependent events, when node $T$ is in state 1 , node $A$ and $B$ will be forced to transition to state 1 immediately. The CIMs of node $T$, node $A$ and node $B$ are shown in Tables $10-12$.

As for SPARE gates, this paper cites a WSP gate as an instance for illustrating the transformation rules. The WSP gate and its corresponding CTBN representation are shown in Figure 6. Node $P$ denotes the primary event which is initially in a working state. Node $S$ denotes the

![img-0.jpeg](img-0.jpeg)

Figure 1. AND gate and its corresponding CTBN representation

![img-1.jpeg](img-1.jpeg)

Figure 2. OR gate and its corresponding CTBN representation

![img-2.jpeg](img-2.jpeg)

Figure 3. PAND gate and its corresponding CTBN representation

![img-3.jpeg](img-3.jpeg)

Figure 4. SEQ gate and its corresponding CTBN representation

![img-4.jpeg](img-4.jpeg)

Figure 5. FDEP gate and its corresponding CTBN representation

![img-5.jpeg](img-5.jpeg)

Figure 6. WSP gate and its corresponding CTBN representation

spare event which is initially in a dormant state with a dormant factor $\alpha$, when node $P$ fails while node $S$ has not failed, node $P$ will transition to a working state immediately. The transitioning of node $C$ from state 0 to state 1 will occur when both of the primary event and spare event are in a failure state. The CIMs of node $P$, node $S$ and node $C$ are shown in Tables 13-15 respectively. The transformation rules of CSP gate and HSP gate are similar, which will not be reiterated here.

Table 10. CIM of node $T$


Table 11. CIM of node $A$


Table 12. CIM of node $B$


Table 13. CIM of node $P$


Table 14. CIM of node $S$


Table 15. CIM of node $C$


### 2.4. Development of an evidence-based risk decision support approach

In tunnel construction projects, decision makers mainly need to make decision on risks in the pre-construction stage and construction stage. The available information obtained in the pre-construction stage and construction stage of the tunnel project can be extracted as the evidence of the CTBN model to assist in making sensible risk decisions. The flow chart of the entire implementation process
is shown in Figure 7. The specific steps of risk-informed decision-making in the pre-construction stage and construction stage of the tunnel project are elaborated respectively.

### 2.4.1. Risk-informed decision-making in the pre-construction stage of the tunnel project

The first step is risk-related information survey. Nielsen (2004) pointed out that the most common risk management problem in project construction stage is insufficient risk identification. In order to achieve a well-supported risk identification, collecting preliminary risk-related information becomes a particularly important step as it helps in identifying the most common accidents, determining the causes of incidents and developing better safety systems and culture (Ayhan \& Tokdemir, 2019). There are three sources of risk-related information needed in the pre-construction stage of the tunnel project, i.e., historical data, project-specific parameters and expert opinions. Historical data mainly encompasses tunnel accident records, standards, safety guidelines, related researches, and previous similar projects (Sherehiy \& Karwowski, 2006). Project-specific parameters mainly include engineering characteristics, engineering hydrogeological conditions, construction techniques, circumjacent environment, quality of project participants, design parameters, and schedule, etc. In practice, historical data on tunnel projects are often scarce or not conveniently accessible, thus interview with professionals becomes an alternative source to obtain risk-related information (Cárdenas et al., 2012). Expert opinions mainly include the experts' perception of the tunnel project risks.

The second step is risk identification. This step is a kind of descriptive analysis which lays the basis for the risk analysis process, and sufficient risk identification ensures the effectiveness of the whole risk management (Tchankova, 2002). In this step, the explicit and tacit knowledge of tunnel project is identified from the raw risk-related information. The explicit knowledge of tunnel construction is rational knowledge, which is related to theoretical aspects, while the tacit knowledge is empirical knowledge, which is related to practical aspects (Hadikusumo \& Rowlinson, 2004). The risk-related knowledge can assist in identifying the possible hazardous events and the associated risk factors in tunnel construction, revealing their relationships, estimating their failure rate and other parameters needed. Specifically, Hazardous events, risk factors and risk mechanism that are prone to occur in tunnel construction can be identified from the historical data, and the historical data can also provide a basis for the expert estimation of failure rate. By comparing the project-specific parameters with the historical data, the possible hazardous event and its risk factors in the specific project can be derived, the construction duration can also be identified from the project-specific parameters. The function of the expert opinions is to supplement the risk factors and risk mechanism and estimate the parameters required to develop the CTBN model. Then the evidence

![img-6.jpeg](img-6.jpeg)

Figure 7. Flow chart of the proposed dynamic risk decision support approach for metro tunnel construction

For developing the CTBN model can be extracted from the risk-related knowledge. In particular, hazardous events, risk factors, and risk mechanisms identified from the combination of historical data, project-specific parameters, and expert opinions are extracted as the evidence for developing the structure of the CTBN model; the failure rate of risk factors identified from the expert opinions is extracted as the evidence of state transition rate of nodes in the CTBN model; the state of risk factors and the hazardous event identified from the project-specific parameters are extracted as the evidence of initial state of nodes in the CTBN model; the construction duration identified from the project-specific parameters is extracted as the evidence of time interval. The detailed evidence use and evidence-based decision-making are shown in the following steps.

The third step is DFT structure construction, which aims to structure the identified hazardous event and its risk factors in the form of DFT. The procedures for establishing DFT structure mainly include: first, determining the analysis scope, objective and basic assumptions; second, defining the hazardous event as the top event and defining the risk factors as the intermediate events and basic events; third, exploring all possible causes of the event layer by layer from top to bottom until the basic events at the bottom level and expressing the relationships among events by logic gates; and finally, performing standardization and simplification to finalize the generated DFT structure.

The fourth step is CTBN model development. In the fourth step, an evidence-based CTBN model is developed to support the decision-making. Firstly, two basic assumptions need to be clarified: The first assumption is that the tunnel construction process is approximately considered as a stationary process, the failure rate of all risk factors is constant and independent of time, the probability of occurrence of each risk factor can be considered to obey the negative exponential distribution; The second assumption is that in the pre-construction stage, all risk factors and the hazardous event are in a non-occurrence state, the initial state of all nodes in the CTBN model can be defined as in state 0. And then, in order to establish a CTBN model, structure learning and parameter learning need to be conducted. Structure learning aims to form an appropriate directed graph with nodes and directed edges, and assemble the corresponding CIM for each node. Instead of the traditional structure learning method, the proposed approach uses DFTs as evidence to develop the CTBN model. Events in DFTs correspond to nodes in CTBNs, and logic gates connecting events are represented by directed edges and CIMs attached to nodes in CTBNs. The transformation rules from the DFT structure into the CTBN formalism have been illustrated previously. Parameter learning aims to parameterize the generated CTBN structure, which need to determine the conditional transition intensity between states of each node. In the pre-construction stage, the repair rate of each root node is set to 0. The remaining task is to estimate the failure rate of each root node.

Many tools have been developed for estimating the failure rate of tunnel construction, and the sources can be broadly classified into three types: reliability analysis, statistical method and expert judgment. The reliability analysis of tunnel construction is usually a complex task since the reliability of both the final tunnel and each of the interim states need to be analyzed, and it has a disadvantage that uncertainties resulting from human and

organizational factors cannot be included in reliability analysis (Blockley, 1999). The statistical method based on data interprets the failure rate as a relative frequency (Aven, 2011). However, failures in tunnel projects are rare events that cannot be easily captured. The study shows a huge spread of failure rate estimation caused by different statistical samples, and suggests that statistical methods can only serve as a basis orientation for expert estimation (Špačková et al., 2013b). Thus, expert judgement is selected for failure rate estimation in the proposed approach.

Expert judgment is a concise way to estimate failure rate when lack of sufficient data support (Choi et al., 2004). On the one hand, expert judgement can be applied to bridge the gap between hard technical evidence and mathematical rules, on the other hand, it can also make up for unknown characteristics of a technical system (Cooke \& Goossens, 2004). However, expert judgement exists an apparent weakness since it is uncertain evidence, the certainty of it is subjectively influenced by expert individuals, which may lead to biases. The following two measures can be utilized to mitigate these biases:
(1) The accuracy of expert judgement depends to a large extent on the degree of risk perception. A comprehensive information survey and knowledge elicitation process can increase the judgement beliefs of expert, which has been clarified in the second step. The increase of expert judgment belief is helpful to reduce subjective biases, and the factored state space in CTBN model can reduce the burden of expert judgement.
(2) The expert investigation is conducted via questionnaires distributed to expert individuals. Eskesen et al. (2004) classified the frequency interval and its corresponding language description. Experts can use this as a reference and combine their knowledge to estimate the failure rate. Different expert individuals may involve in different risk attitudes and different judgment abilities on different events. Hence, expert judgement credibility index is introduced to distinguish the reliability of data from interviews with individuals (Zhang et al., 2014a). The expert judgement credibility index (denoted by $\omega$ ) is determined by the expert judgment ability (denoted by $\eta$ ) and the expert confidence index (denoted by $\theta$ ). The expert judgment ability of each expert individual is determined by the expert's educational level, length of employment and job position, and reflects the authority of expert. Table 16 lists the expert judgment ability level and the associated expert weight coefficient. The expert confidence index reflects the subjective confidence of each expert individual in his or her own judgements and can be measured in ten levels from 0.1 to 1.0. The expert judgement credibility index $\omega$ can be calculated by Eqn (10):

$$
\omega=\eta \cdot \theta
$$

If the number of experts is $m$, by using the weighted average method, the estimated failure rate of the root node $X_{n}$ can be calculated by Eqn (11):

$$
\lambda_{X_{n}}=\frac{\sum_{j=1}^{m} \omega_{j} \cdot \lambda_{X_{n}}^{j}}{\sum_{j=1}^{m} \omega_{j}}
$$

where $\lambda_{X_{n}}$ denotes the weighted average of $m$ experts' estimates of failure rate; $\lambda_{X_{n}}^{j}$ denotes the $j$-th expert's estimates of failure rate.

Table 16. Classification of expert judgment ability level and setting of corresponding weights (Zhang et al., 2014a).


Some other main possible expert judgement biases and measures of minimizing biases are listed by Hallowell and Gambatese (2009). The failure rate of nodes can be estimated with relatively accuracy by applying these measures in accordance with specific conditions.

The fifth step is risk analysis based on CTBN model inference. The inference with the CTBN model is performed with a powerful software package called CTBN-RLE in Rversion developed by Shelton's team (Shelton et al., 2010). This software provides libraries and programs for the algorithms developed for CTBNs, and the library supplies classes for storing and scanning multivariate trajectories. So, the initial distribution and conditional intensity matrices of a CTBN can be represented. CTBN-RLE can implement exact inference and sampling approximate inference based on evidence, and among the multifarious forms of inferences, querying the marginal distribution of a variable at a particular time enables the users to obtain the failure probability of an event in a time interval. Cao (2011) has validated the correctness of the CTBN modeling technique. The following equations and descriptions will help the users determine the input parameters of the CTBN model for various forms of analysis.

In the pre-construction stage of the tunnel project, by inputting the built CTBN model into the CTBN-RLE software and querying the marginal distribution of the nodes, predictive analysis and importance analysis can be implemented to support the decision-making.

Predictive analysis aims to judge the acceptability of the hazardous event and find the weak positions by predicting the occurrence probability of it and its critical subevents. According to basic assumption, the initial state of each node in the CTBN model is set to 0 , the time interval is set to $T$, the CIMs of the root nodes are filled in based on the failure rates estimated by expert judgement, and the CIMs of the intermediate nodes and leaf node are filled in with the transformation rule of the logic gates. The leaf node is denoted as $X_{H E}$. Then the probability of $X_{H E}$ transitioning to state 1 within the time interval $T$ can be queried by CTBN modeling method. The probability of $X_{H E}$ transitioning to state 1 indicates the occurrence probability of the hazardous event. In the same way, the occurrence probability of a specific sub-event can be calculated. The calculation results are called the prior probabilities of the hazardous event and its sub-events.

Importance analysis aims to sequence the importance of each risk factor to the hazardous event and judge the acceptability of the impact of each risk factor on the tunnel performance. If the impact of the risk factor on the hazardous event is unacceptable, it will threaten the safety of the tunnel project and handling of it may prolong the construction duration and increase the cost. In comparison with the CTBN model developed for predictive analysis, the hypothetical scenario that setting the initial state of the node $X_{n}$ to state 1 is served as evidence to calculate the conditional probability $P\left(X_{H E}(T)=1 \mid X_{n}(T)=1\right)$, and the hypothetical scenario that setting the failure rate of $X_{n}$ (denoted as $\lambda_{X n}$ ) to 0 is served as evidence to calculate the conditional probability $P\left(X_{H E}(T)=1 \mid X_{n}(T)=\right.$ 0 ). Importance analysis is conducive to improve the reliability of the system effectively, optimize design methods for system, or find out the causes of system failure. The importance analysis in the proposed approach is carried out in three layers:
(1) In the first layer, effort need to be made to distinguish whether a risk factor is in a critical state in the system. If the occurrence of a risk factor $X_{n}$ directly leads to the occurrence of the hazardous event $X_{H E}, X_{n}$ is considered to be in a critical state, which can be expressed as Eqn (12):

$$
P\left(X_{H E}(T)=1 \mid X_{n}(T)=1\right)=1
$$

Conversely, if the occurrence of $X_{n}$ cannot directly lead to the occurrence of $X_{H E}, X_{n}$ is considered to be in a non-critical state which can be expressed as:

$$
P\left(X_{H E}(T)=1\right)<P\left(X_{H E}(T)=1 \mid X_{n}(T)=1\right)<1
$$

Obviously, risk factors in a critical state need to be paid top priority attention in tunnel construction, whereas risk factors in a non-critical state will enter into the next layer.
(2) In the second layer, the importance of risk factors is judged from the sensitivity perspective and Birnbaum's Measure is utilized to analyze the Probability Importance of risk factors (Andrews \& Beeson, 2003).

The Probability Importance is defined as the probability change degree of the hazardous event when only a risk factor $X_{n}$ is set to failure state. The Probability Importance index of $X_{n}$, denoted as $I^{P}\left(X_{n}(T)\right)$, can be calculated by Eqn (14):

$$
\begin{aligned}
& I^{P}\left(X_{n}(T)\right)=\frac{\partial P\left(X_{H E}(T)\right)}{\partial P\left(X_{n}(T)\right)}=P\left(X_{H E}(T)=\right. \\
& 1\left|X_{n}(T)=1\right)-P\left(X_{H E}(T)=1 \mid X_{n}(T)=0\right)
\end{aligned}
$$

where $P\left(X_{H E}(T)=1 \mid X_{n}(T)=1\right)$ denotes the conditional probability that $X_{H E}$ transitions to state 1 when $X_{n}$ is initially in state $1 ; P\left(X_{H E}(T)=1 \mid X_{n}(T)=0\right)$ denotes the conditional probability that $X_{H E}$ transitions to state 1 when $X_{n}$ is known to be in state 0 . The higher Probability Importance index of $X_{n}$ is, the more sensitive $X_{n}$ is.
(3) The Probability Importance cannot reflect the difficulty of reducing the probability of risk factors. Thus, the non-critical risk factors are input into the third layer and the Criticality Importance is calculated. The Criticality Importance is defined as the change degree of probability change rate of the hazardous event caused by the change of probability change rate of a risk factor $X_{n}$ (Beeson \& Andrews, 2003). The Criticality Importance index of $X_{n}$, denoted as $I^{C}\left(X_{n}(T)\right)$, can be calculated by Eqn (15):

$$
\begin{aligned}
& I^{C}\left(X_{n}(T)\right)=I^{P}\left(X_{n}(T)\right) \cdot \frac{P\left(X_{n}(T)\right)}{P\left(X_{H E}(T)\right)}= \\
& \frac{\partial P\left(X_{H E}(T)\right)}{\partial P\left(X_{n}(T)\right)} \cdot \frac{P\left(X_{n}(T)\right)}{P\left(X_{H E}(T)\right)}= \\
& {\left[P\left(X_{H E}(T)=1 \mid X_{n}(T)=1\right)-P\left(X_{H E}(T)=\right.\right.} \\
& \left.\left.1 \mid X_{n}(T)=0\right)\right] \cdot \frac{P\left(X_{n}(T)=1\right)}{P\left(X_{H E}(T)=1\right)}
\end{aligned}
$$

where $P\left(X_{n}(T)=1\right)$ denotes the probability of $X_{n}$ transitioning to state 1 . The Criticality Importance can measure the importance of risk factors from both the sensitivity perspective and the probability perspective. In this manner, a less reliable risk factor with a higher Criticality Importance index is more critical and needs more attention (Espiritu et al., 2007).
The compound influences of multiple risk factors on the safety of the hazardous event can be evaluated in the same way.

The final step of decision-making in the pre-construction stage of the metro tunnel project is to make an evidence-based risk decision based on the analysis results of the previous step. The decision-making is mainly composed of risk assessment and risk response. Decision makers need to perform risk assessment on whether the safety of the hazardous event is acceptable. This procedure is implemented through comparing the occurrence probability of the hazardous event with the risk acceptance criterion. If there is no clear risk acceptance criterion for the hazardous event, decision makers need to combine their risk perceptions with the possible consequences and safety

objectives to develop the risk acceptable range. If the assessment result is within an acceptable range, the existing scheme is considered capable of meeting the requirement, and the attitude is to retain or ignore the risk; whereas if the assessment result is non-acceptable, the construction process monitoring and safety patrol need to be strengthened and an appropriate risk response strategy need to be adopted. Common risk responses to unacceptable risks mainly include risk avoidance, risk transfer and risk mitigation. Risk avoidance is to bypass risks by changing the project plan, risk transfer is the transfer of risk to a third party, and risk mitigation aims to reduce risk exposure by reducing the probability or impact of the hazardous event to an acceptable range. Moreover, the results of importance analysis can assist decision makers in determining the monitoring priority of risk factors and optimizing the risk warning in tunnel construction.

### 2.4.2. Risk-informed decision-making in the construction stage of the tunnel project

Practical tunnel projects often involve numerous uncertainties. The uncertainty associated with imperfect prediction and estimation is caused by the simplification of models and lack of prior information and knowledge (Ang \& Tang, 2007). The uncertainty can be decreased by acquiring new information from tunnel construction site as certain evidence. Owing to the existence of the uncertainty, it is necessary to update the decision-making when new evidence supporting the decision is obtained in the construction stage.

Once the tunnel construction begins, new information can be collected from the monitoring data and on-site safety patrol observations. The main objects of monitoring and observation are composed of geology conditions, tunnel project itself and circumjacent environment. By comparing this information with the predicted tunnel construction performance, anomalies of risk factors can be identified. The certain evidence of nodes in CTBN model can be extracted from the identified anomalies.

If a risk factor $X_{n}$ is observed to be in a failure state at the time point $s$, then the predictive analysis can be updated and the inputs of the CTBN model is updated as follows: The initial time is updated to $s$, the initial state of $X_{n}$ is updated to state 1 , the time interval is updated to $[s, T]$, and other parameters of the CTBN model remain unchanged from the inputs in the pre-construction stage. Then the updated occurrence probability of the hazardous event can be expressed by Eqn (16):

$$
\begin{aligned}
& P\left(X_{n}(s, T)=1\right)=1 \\
& P\left(X_{H E}(s, T)=1\right)=P\left(X_{H E}(s, T)=\right. \\
& 1 \mid X_{n}(s, T)=1) \cdot P\left(X_{n}(s, T)=1\right)
\end{aligned}
$$

where $P\left(X_{H E}(s, T)=1 \mid X_{n}(s, T)=1\right)$ denotes the conditional probability that $X_{H E}$ transitions to state 1 within the time interval $[s, T]$ when $X_{n}$ is initially in state 1 ; Finally, with the updated prediction result of the occurrence prob-
ability of the hazardous event, the decision-making can be updated.

Once the occurrence of the hazardous event is found in the tunnel construction process, the decision-making will focus on the diagnosis of accident causes and the development of repair strategies. The information of the occurrence of the hazardous event and its sub-events can be obtained from the accident detection, and this information is extracted as certain evidence to update the node state and time interval of the CTBN model for diagnostic analysis.

Diagnostic analysis aims to find out the most likely causes when the hazardous event occurs. It requires obtaining the posterior probability of risk factors that may lead to the hazardous event. Assume that the hazardous event is found to have occurred at the time point $s$, then the posterior probability of the risk factor $X_{n}$ transitioning to state 1 within the time interval $[0, s]$, which is denoted as $P\left(X_{n}(s)=1 \mid X_{H E}(s)=1\right)$, can be calculated by Eqn (17):

$$
\begin{aligned}
& P\left(X_{n}(s)=1 \mid X_{H E}(s)=1\right)= \\
& \frac{P\left(X_{H E}(s)=1 \mid X_{n}(s)=1\right) \times P\left(X_{n}(s)=1\right)}{P\left(X_{H E}(s)=1\right)}
\end{aligned}
$$

where $P\left(X_{n}(s)=1\right)$ denotes the prior probability of $X_{n}$ within the time interval $[0, s] ; P\left(X_{H E}(s)=1\right)$ denotes the prior probability of $X_{H E}$ within the time interval $[0, s]$. The larger the posterior probability of $X_{n}$, the more likely $X_{n}$ is the direct cause of $X_{H E}$. Furthermore, if an intermediate node in the CTBN model is confirmed to be in a failure state, the posterior probability of the risk factors of the corresponding sub-events can also be calculated to narrow the scope of fault diagnosis.

Via diagnostic analysis all suspected risk factors can be identified, and by combining the possible risk factors in the order of posterior probability with the information obtained from the accident detection, experts can ultimately determine the cause of the hazardous event. On this basis, experts can estimate the repair probability of the risk factors that lead to the occurrence of the hazardous event and develop an optimal repair strategy, which will not be detailed here.

## 3. Case study

The shield method for tunnel construction has the advantages of safety and efficiency, and is widely applied in urban metro tunnel construction in China. In areas rich in groundwater, most tunnel lines are excavated below groundwater. Owing to the complicacy of circumjacent environment and construction process, the phenomenon of tunnel water leakage in different degrees is prone to be found. In consideration of the universality and perniciousness of tunnel water leakage, it is of great significance to make decision on the leakage risk during tunnel construction. A metro tunnel project in southwest of China is selected as a case to illustrate how the proposed decision support approach is applied to the risk of tunnel water leakage.

### 3.1. Project profile

The selected tunnel project locates in an old urban area and is adjacent to dense surface buildings. An earth pressure balance shield machine with a cutter head diameter of 6.43 m is used for soil excavation. Reinforced concrete segments with an external diameter of 6.2 m , an internal diameter of 5.5 m and a width of 1.2 m are adopted for tunnel lining. Each lining ring is composed of 6 pieces of segments, and the staggered joint assembly pattern is adopted in the project.

The profile of the hydrogeology conditions along the tunnel axis is shown in Figure 8, and the permeability coefficient of each soil layer is shown in Table 17. The total length of the tunnel is 1066 m , the buried depth of the tunnel is $15.60-25.40 \mathrm{~m}$, and the soil layers where the tunnel passes through are mainly the silty clay layer, silt layer and silty sand layer. The groundwater level is $2.2-5 \mathrm{~m}$ below the ground surface. The aquifers have the characteristics of high water content, strong water permeability, hydraulically connected and confined. These characteristics may have great impact on the construction safety. Thus, the waterproofing works should be well done during the tunnel construction process. The engineering investigation report shows the silty sand layer is the aquifer that the tunnel mainly passes through. The mileage DK0+835.40$\mathrm{DK} 1+564.80$ has a relatively high risk of tunnel water leakage, so it is selected as the research object.

Table 17. Permeability coefficient of soil layers


### 3.2. Development of the decision support model

Although more and more attention has been paid to the metro waterproofing works, the current situation is still not optimistic. A risk screening team is involved in the identification of the water leakage risk of the project. First, risk-related information is collected to identify the risk mechanism of the tunnel water leakage. Zhang et al. (2014b) evaluated the water leakage risk of the rivercrossing tunnel from the aspects of geology, design, construction and management by empirical method. Xie et al. (2021) calculated the leakage probability of longitudinal joint of the segments by Monte Carlo method. Wu et al. (2014) introduced the leaking behaviour of the tunnel under Huangpu River and discussed the factors influencing tunnel water tightness. According to the statistics of on-site inspection of shield tunnels in Shanghai, $87 \%$ of tunnel leakage occurs through the segmental joints, $8 \%$ occurs through the grouting holes, $3 \%$ occurs through the grouting holes and $2 \%$ occurs through other locations (Zhang et al., 2015). Such studies can effectively increase the cognition of tunnel leakage risk and help to extract the explicit knowledge and tacit knowledge from the riskrelated information.

Through preliminary analysis of the information of previous studies, accident records and expert opinions, four water leakage locations can be identified: (1) shield tail sealing; (2) segment joint; (3) segment surface; (4) bolt and grouting holes. The shield tail sealing device relies on the combined action of wire brush and grease to prevent grouting slurry and water from entering the tunnel. Since the grouting material has a certain degree of impermeability after solidification, the grouting layer behind the segment lining can effectively reduce the possibility of tunnel water leakage and becomes the first defense line of the tunnel waterproofing system. As the segments are made of high-strength reinforced concrete with impermeability grade of P12, and self-adhesive rubber sheet is installed at the corners of each segment, the self-waterproofing performance of segment can be considered warrantable.
![img-7.jpeg](img-7.jpeg)

Figure 8. Longitudinal profile of the tunnel hydrogeology condition

Segment joints are commonly labeled as the weakest points against infiltration of groundwater (Wu et al., 2014), hence two defense lines are adopted for waterproofing of segment joints in this project. The first defense line is the ethylene propylene diene monomer (EPDM) rubber elastic gasket set in the gasket groove, which can achieve the waterproofing function when under compressed state. The second defense line is to set caulking groove inside the segment joint and use polysulfide sealant as caulking material. The bolt and grouting holes are sealed by water swelling rubber washers to achieve the waterproofing effect. The bolt holes are plugged with M15 polymer cement mortar and the grouting holes are plugged with
screw plug. Some typical waterproofing measures adopted in the project are depicted in Figure 9.

The risk-related knowledge of the hazardous event, risk mechanism and risk factors identified from the previous step is extracted as evidence of events and logic gates in the DFT structure. Specifically, the hazardous event is represented by top event, its sub-events and risk factors are represented by intermediate events and basic events, and the relationships among these events are represented by logic gates. The water leakage of tunnel is defined as the top event of DFT, and a DFT structure with 15 intermediate events and 32 basic events is established and shown in Figure 10, and the descriptions of the events are depicted in Table 18.
![img-8.jpeg](img-8.jpeg)

Figure 9. Typical waterproofing measures adopted in the selected tunnel project
![img-9.jpeg](img-9.jpeg)

Figure 10. DFT structure diagram for water leakage of tunnel

Table 18. Descriptions of the events in DFT model


And then the equivalent CTBN framework can be developed in accordance with the transformation rules. The CTBN representation of tunnel water leakage is shown in Figure 11, and all nodes of the CTBN model are assigned with the corresponding CIMs.

The failure rate of root nodes in the CTBN model is estimated by experts as evidence. Questionnaires are distributed to 24 tunnel experts, and 20 of which are returned. Among the 20 questionnaires, 2 are from experts at level I, 4 are from experts at level II, 8 are from experts at level III, and 6 are from experts at level IV. In order to standardize the risk analysis method, the unit of failure rate is defined as one day, the minimum failure rate is set to be $1.0 \mathrm{E}-5$ per day, and two significant digits are retained for all statistical results. The planned construction duration of the selected region is roughly estimated by experts as 130 days. The failure rate of each root node is estimated by experts on the basis of the prior information and their expertise, and the failure rate estimations from 20 experts are weighted by expert judgement credibility index. The final results of the failure rate estimations are shown in Table 19.


### 3.3. Risk analysis and decision-making in the pre-construction stage

Predictive analysis and importance analysis are performed in the pre-construction stage of the tunnel project to assist decision makers in judging the acceptability of tunnel water leakage risk and taking corresponding risk responses.

As the inputs of the CTBN model for predictive analysis, the failure rates estimated by experts are the sources of the root nodes' CIMs, and the CIMs of intermediate nodes and leaf node can be inferred according to the transformation rules, and according to the basic assumption for predictive analysis, the initial state of all nodes is set to state 0 . The initial state of the nodes and the CIMs attached to the nodes are filled into the CTBN-RLE, and the failure probability of the nodes in the planned construction duration can be queried with the built-in default inference algorithm. In order to make the CTBN model computable, a large number, i.e., 1E10, is used to substitute all $\infty$ in CIMs. Within the outputs of the CTBN model, the state distribution of the leaf node and several critical intermediate nodes when the time is 130 days are queried.

![img-10.jpeg](img-10.jpeg)

Figure 11. Equivalent CTBN model for water leakage of tunnel
Table 19. Failure rate estimations of root nodes


It turns out that the occurrence probability of tunnel water leakage is $9.11 \%$ within the construction duration. The prior probabilities of the leaf node and some selected intermediate nodes are shown in Figure 12.

The importance analysis based on hypothetical scenarios is performed as follows: Through changing the initial state and the CIMs of the root nodes input into the CTBN model, the conditional probabilities $P\left(X_{H E}(T)=\right.$ $\left.1 \mid X_{n}(T)=1\right)$ and $P\left(X_{H E}(T)=1 \mid X_{n}(T)=0\right)$ of each root node can be calculated, and then three levels of importance analysis can be implemented. In the first layer, $X_{1}$ to $X_{8}$ are distinguished in a critical state according to Eqn (12), and the other 24 non-critical risk factors are input into the next layer. In the second layer, the Probability Importance of $X_{9}$ to $X_{32}$ is calculated by using Eqn (14) and the result is shown in Figure 13. Then, $X_{9}$ to $X_{32}$ are input into
![img-11.jpeg](img-11.jpeg)

Figure 12. Prior probabilities of leaf node and critical intermediate nodes (probability grade in red indicates very likely, probability grade in orange indicates likely, probability grade in light blue indicates possible, probability grade in light green indicates unlikely)

the third layer to compare their Criticality Importance respectively by using Eqn (15), and the result is shown in Figure 14.

In this project, decision makers define the following acceptance criterion: the probability grade of very likely and likely is non-acceptable, indicating that additional risk responses should be taken; whereas the probability of possible and unlikely is acceptable, suggesting that the existing waterproofing measures can satisfy the safety objective. By comparing the risk criterion with the predictive analysis result, the decision makers conclude that the tunnel water leakage risk is within an acceptable range. Furthermore, it is found that the probability of water leakage is higher at the segment joints and grouting and bolt holes among the four water leakage locations, hence more attention should be paid to these weak positions. Among the several main waterproofing measures, both the sealing gasket waterproofing and caulking waterproofing tend to show relatively high probability of failure, however, the co-work of them can effectively reduce the probability of joint leakage. Therefore, it is necessary to set two defense lines at the joint in this project. Due to the complicacy of the external environment around the tun-
nel, it is difficult to guarantee the waterproofing effect of grouting outside the segment lining, and consequently the grouting layer can only function as a preliminary defense line of the tunnel waterproofing system.

The contribution of risk factors to the tunnel water leakage risk can be measured by the results of importance analysis. Risk factors $X_{1}$ to $X_{8}$ related to the shield tail sealing should be strictly eliminated since they can directly lead to the occurrence of water leakage risk. The failure rates of $X_{1}$ to $X_{8}$ are limited to very low values, which are considered to meet the requirements. Risk factors $X_{11}$ to $X_{18}$ related to the segment surface as well as the grouting and bolt holes are the most sensitive non-critical risk factors, and reducing the probability of these risk factors can significantly decrease the probability of water leakage risk. The result of the third layer indicates that guaranteeing the grouting effect and amount and improving the construction quality of segment joints and holes are two priority ways to mitigate the risk of tunnel water leakage. In general, the waterproofing measures taken in the tunnel project is consistent with the risk design principle and can be considered reasonable.
![img-12.jpeg](img-12.jpeg)

Figure 13. Sequencing results of Probability Importance of nodes $X_{9}$ to $X_{32}$
![img-13.jpeg](img-13.jpeg)

Figure 14. Sequencing results of Criticality Importance of nodes $X_{9}$ to $X_{32}$

### 3.4. Risk monitoring and decision updating in the construction stage

New information from the tunnel construction process can reduce the epistemic uncertainty of tunnel water leakage risk, therefore, the anomalies identified from this information are used as certain evidence to support updating the node state. Amongst all the monitoring measurement items, lining deformation, groundwater level and grouting effect are the items with high correlation to the water leakage. Whilst amongst all the safety patrol items, location and mode of water leakage, condition of segment surface cracks, quality of segment installation, personnel operation, sealing of segment joints, and sealing of grouting and bolt holes are the items with emphases. Several typical observations from the safety patrol on construction site are shown in Figure 15. During a safety patrol when the tunnel construction was up to 30 days, the problem of unqualified calking waterproofing was found, which can be regarded as the occurrence of node $D_{2}$. If this problem is not addressed properly, the CTBN model can be updated as follows: In comparison with the inputs of the CTBN model for predictive analysis in the pre-construction stage, the initial state of the node $D_{2}$ is updated to state 1 , and according to the remaining construction duration, the time interval is updated to 100 days, other inputs of the CTBN model remain the same as the predictive analysis in the pre-construction stage. The updated outputs of the CTBN model can be queried and the comparison of the prior probabilities and the updated probabilities of the nodes is shown in Figure 16. It can be seen that the updated occurrence probability of tunnel water leakage is $17.87 \%$, which falls into the probability grade of likely. The updated predictive results indicate that the decision should be updated to non-acceptable and countermeasures need to be implemented. Thus, some improvement suggestions on caulking construction quality were put forward to the on-site workers and the supervision was strengthened.

Theoretically, many anomalies can be treated as the evidence for risk updating. However, in practical engineering, the state of some risk factors cannot be directly observed, which need to be speculated by experts through
![img-14.jpeg](img-14.jpeg)

Figure 16. Comparison of prior probabilities and updated probabilities of nodes
indirect information, and some subtle anomalies in the construction process are often not received enough attention so that they are not fed back to experts. These reasons make it difficult to extract the evidence for updating the CTBN model.

### 3.5. Accident diagnosis and response

In the analysis section of the tunnel project, the water leakage problem was witnessed 46 days after the construction started and was not solved promptly. Through the field inspection, it is found that the leakage occurred at the segment joint, as shown in Figure 17. In this case, the diagnostic analysis should be performed to assist experts to speculate the causes of the hazardous event. According to the information regarding the location of the water leakage and the failure mode of waterproofing measures, the field experts infer that grouting waterproofing, sealing gasket waterproofing and caulking waterproofing enter into a failure state, and thus only the risk factors related to these waterproofing measures are considered for simplicity.

Based on Eqn (16), certain evidences $B_{4}(46)=1$, $D_{1}(46)=1$ and $D_{2}(46)=1$ are used to calculate the posterior probabilities of risk factors in these three sub-events
![img-15.jpeg](img-15.jpeg)

Figure 15. Some observations from the on-site safety patrol: a - Joint sealing; b - Personnel operation specification; c - Segment intactness

![img-16.jpeg](img-16.jpeg)

Figure 17. Observed leakage at the segment joint
respectively. The results are shown in Figure 18. It can be seen that the most probable reason of grouting waterproofing failure is poor grouting quality (with a $93.09 \%$ chance), the most probable reason of sealing gasket waterproofing failure is excessive deformation or relative displacement of segments (with a $80.05 \%$ chance), and the most probable reason of caulking waterproofing failure is excessive deformation of caulking groove or caulking groove damaged (with a $63.90 \%$ chance). The results can provide support for the diagnosis of accident site. After comparing the calculated results with the actual on-site diagnosis, experts in the field can finally confirm the causes of the occurrence of the hazardous event and formulate the following repair strategy: drilling a hole at the joint where the leakage occurs, inserting a slender plastic pipe to drain off the leakage water, and inserting another pipe and grouting outward through it. When it is confirmed that there is no more water leakage, cut off the grouting pipe and caulk the joint again. This repair strategy actually aims at the repair of risk factor $X_{10}$, which maintains as the main
cause of the water leakage. Since the expected repair time is far less than one day, it can be almost ascertained from Eqn (9) that the fault can be repaired (the analysis details are omitted). The actual result demonstrates that the application of repair strategy proposed for the water leakage is effective. The treatment measures adopted in the project successfully prevent the groundwater from continuing to leak into the tunnel and avoid the occurrence of more serious accidents.

In addition, by comparing the results of the diagnostic analysis in Figure 18 with the results of the critical importance analysis in Figure 14, it can be seen that $X_{10}, X_{22}$ and $X_{29}$ are not only the key factors of accident prevention, but also the most likely causes after the occurrence of the hazardous event. Therefore, whether it is prevention in the pre-accident stage or diagnosis in the post-accident stage, $X_{10}, X_{22}$, and $X_{29}$ are the factors that need priority attention.

## Conclusions

The risk-informed decision of metro tunnel project in complicated environment inevitably faces uncertainty problems. In order to fill the research gap that previous researches only focused on the epistemic uncertainty characteristics caused by the scarcity of risk-related information but ignored the fully utilization of the diversity of riskrelated information, this paper presents an evidence-based risk decision support approach for tunnel construction project. This study aims to reduce the epistemic uncertainty of risks by providing the evidence for decision-making. The CTBN model can perform evidence-based reasoning, thus a CTBN-based risk decision support framework is developed for the tunnel project. The proposed approach enables multi-dimensional information to be used as evidence to support decision-making through the state space decomposition of risks in tunnel construction project with
![img-17.jpeg](img-17.jpeg)

Figure 18. Diagnostic analysis results of tunnel water leakage: $\mathrm{a}-P\left(X_{n}(46) \mid B_{4}(46)=1\right) ; \mathrm{b}-P\left(X_{n}(46) \mid D_{1}(46)=1\right) ; \mathrm{c}-P\left(X_{n}(46) \mid D_{2}(46)=1\right)$

the CTBN model. Moreover, how to identify risk-related information as implicit or tacit knowledge and how to extract this knowledge as certain and uncertain evidence to support decision-making are demonstrated. Specifically, in the pre-construction stage of the tunnel project, the information of expert opinions, project-specific parameters and historical data are fused into CTBN model as evidence to perform predictive analysis and importance analysis, and the results can assist the decision on judging the acceptability of the hazardous event and formulating response strategies for risk factors; in the construction stage of the tunnel project, certain evidence extracted from engineering anomalies can update the predictive analysis, and the diagnostic analysis can be performed with the certain evidence extracted from the accident detection information to help find out the causes of the hazardous event. It can be found that with the progress of the tunnel project, new evidence integrated into the CTBN model can reduce the epistemic uncertainty of decision-making. The case study on tunnel water leakage risk illustrates the applicability of the proposed approach in risk-informed decision-making. Further, by using the same steps, the proposed decision support approach is also applicable to other types of risks in tunnel projects, so it has wide application prospect.

In terms of management, this paper presents a novel approach which gives a deep insight into the risk decisionmaking field. The integration of multi-source evidence and improving the certainty of uncertain evidence are the key to reduce the biases of risk decision-making. The proposed approach improves the utilization efficiency of risk-related information and promotes the circulation of information among project participants. In conclusion, the proposed decision support approach improves the safety of tunnelling project and is conducive to risk management.

Several main conclusions are drawn as follows:
(1) CTBN model is an efficient framework to integrate multi-source information as evidence and can perform evidence-based reasoning, the results of which can increase the risk cognition and provide informed decision support for tunnel projects.
(2) A concise CTBN model establishment method based on DFT technique is presented to replace the traditional model learning process with high data requirement.
(3) The application of the approach in tunnel water leakage risk reveals that the weak position of waterproofing is segment joint, risk factors related to human errors are the main causes of tunnel leakage.
There still exist some limitations in the proposed risk decision support approach that may hinder its wide application. This study assumes that all risk factors obey exponential distribution, and the failure rate is independent of time, which is only applicable to the case that the risk factors of the hazardous event are stable. The proposed approach can only reduce the uncertainty of part of the
parameters in the decision support model, while the parameter of failure rate based on expert judgement cannot be updated. The future work will focus on further improving the certainty of uncertainty evidence based on the information obtained from tunnel construction process and addressing the decision support when tunnel construction risk changes greatly.

## Notations

## Abbreviations

DFT - Dynamic fault tree;
CTBN - Continuous Time Bayesian Network;
FTA - Fault Tree Analysis;
BN - Bayesian Network;
DAG - Directed acyclic graph;
CPD - Conditional probability distribution;
JPD - Joint probability distribution;
CIM - Conditional intensity matrix;
JIM - Joint intensity matrix;
EPDM - Ethylene propylene diene monomer.

## Acknowledgements

First and foremost, I would like to show my deepest gratitude to my supervisor, Prof. Zheng Junjie, a respectable, responsible and resourceful scholar, who has provided me with valuable guidance in every stage of the writing of this paper. I would also like to thank Prof. Zhang Rongjun who have helped me to develop the fundamental and essential academic competence. I shall extend my thanks to Mr. Yang for all his kindness and help.

## Funding

This work was supported by the under Grant [No. 2016YFC0800200].

## Author contributions

Yifan Guo and Rongjun Zhang conceived the study and were responsible for the design and development of the decision support approach. Junjie Zheng and Youbin Yang were responsible for data collection and analysis. Yifan Guo wrote the first draft of the article.

## Disclosure statement

No conflict of interest exits in the submission of this manuscript, and manuscript is approved by all authors for publication. I would like to declare on behalf of my coauthors that the work described was original research that has not been published previously, and not under consideration for publication elsewhere, in whole or in part.
