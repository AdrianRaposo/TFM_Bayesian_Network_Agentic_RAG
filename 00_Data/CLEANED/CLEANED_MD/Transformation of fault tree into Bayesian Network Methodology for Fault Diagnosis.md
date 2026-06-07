# Transformation of Fault Trees into Bayesian Networks Methodology for Fault Diagnosis 

M. MEDKOUR*, L. KHOCHMANE**, A. BOUZAOUIT**, O. BENNIS***
*LRPCSI Laboratory, Mechanical department, Faculty of Technology, 20th August 1955 University, Skikda 21075, Algeria, E-mail: malakmedkour@yahoo.fr; m.medkour@univ-skikda.dz.
**LRPCSI Laboratory, University of Skikda, Algeria, E-mail: lakhdarkhochmane@yahoo.fr; bouzaouit21@gmail.com
***PRISME Laboratory of Research, IUT of Chartres, 28000, France, E-mail: ouafae.bennis@univ-orleans.fr
cross ${ }^{\text {ref }}$ http://dx.doi.org/10.5755/j01.mech.23.6.17281

## 1. Introduction

Faults detection and their diagnosis play an essential role in the industry. The search for signatures or fault indicators has as a purpose to characterize the operation of the system by identifying the type and origin of each of the failures. Indeed, they contribute, by a rapid and early detection, to saving points of availability and production to the capital invested in the production tool.

In the last decade, maintaining and diagnosing machines is an effective tool for early faults detection and continuous tracking of their evolution in time. Machine maintenance requires a good understanding of the phenomena related to the onset and development of faults. Detecting their occurrence at an early stage and following their evolution is of a great interest [1]. It is possible to distinguish three types of approach for surveillance, depending on the nature of the monitoring element: analytical model methods, data based methods, and knowledge based methods.

Fault diagnosis is considered as the problem of multi-classification after the fault data is detected. Various approaches developed for this purpose can be mainly divided into two categories. The first is mathematical modelbased, such as multinomial logistic regression and bayesian network (BN). The second is related to the artificial intelligence, (i.e. fuzzy classifier, artificial neural networks (ANN), SVM and ELM) [2].

The structure and relationship of components are complicated in rotary complex machines, and the graphical construction of (BN) can be tedious and difficult, a fault tree is considered to simplify determining causality between components. The construction of the Fault tree allows constructing a bayesian network for exploit the mass of existing data. Which means that any fault tree can be transformed into a corresponding bayesian network by creating a binary bayesian network node for each event in the fault tree? Moreover, in the context of transforming the fault tree into a bayesian network, several works have been carried out (more details on these transformation steps are given in reference) [3].

Bayesian network probabilistic graphical models have been widely used to solve various problems (for example diagnosis, failure prediction and risk analysis, classification) [4]. Modelling by using bayesian network is performed in two steps: the quantitative step (estimating the probability distribution tables) and the qualitative step (construction of the network or the graph).

The phase of the quantitative analysis in the construction of bayesian networks is considered a very difficult task in estimating the a prior marginal and conditional probabilities of each node of the network. A prior probability is based on the knowledge provided by expert of the process or obtained by learning methode or algorithm from an experimental or experience feedback database [5].

The priori information, the posterior information and the likelihood in bayesian probability theory are represented by probability distributions. The prior probabilities represent the distribution of knowledge or belief concerning a subject or a variable before any relevant evidence taken into account. A posterior probability is the conditional probability on collected data by a combination of a prior probability and likelihood via Bayes' theorem. The likelihood is a parameter function of a statistical model, reflecting the possibility of observing a variable when these parameters have a value [6]. On the other side, in fault tree method the probability of occurrence of the top event, intermediaries vents are governed by their basic events; the occurrence of the latter can be modeled by various statistical distributions (Exponential, Normal, Lognormal, Weibull, Gamma ...) [7].

The method of fault tree is widely used in the field of the reliability. It offers a framework privileged to the deductive and inductive analysis by means of a tree structure of logical gates [8].

The procedure that uses fault trees for diagnosis purposes is abductive, focusing first on adverse events and then identifying their causes. A fault tree is established as a logical diagram and has the undesirable event at the top. The immediate causes that produce this event are then hierarchized using logical symbols "AND" and "OR". To perform a correct diagnosis from the fault trees, these must largely represent all the causal relationships of the system, capable of explaining all possible fault scenarios.

In FT Analysis, the analysis is realized in two steps: a quantitative step in which, on the basis of the probabilities assigned to the failure events of the basic components, the probability of occurrence of the top event (and of any internal event corresponding to a logical subsystem) is calculated; a qualitative step in which the logical expression of the top event is derived in terms of prime applicants (the minimal cut-sets) [3].

Works on bayesian network and system safety have recently been developed by [3] in 2005; explaining how the fault tree can be achieved using bayesian network static. Moreover, works which concern applications to reliability are numerous; [9] in 2003, [10] in 2006 provide also

the use of bayesian network for modelling purpose of the cause-and-effect relationships between the degradation, the causes and consequences, and calculation, alike, of the reliability of complex mechanical systems. Bayesian networks can also take a dynamic dimension, [11] describes the representation of dynamic fault trees by dynamic bayesian networks.

The advantage of probabilistic graphical models is interesting graphical representation of models, easy to understand and analyze. In addition, the probabilistic failure analysis evaluates the probability of failure of a complex system that its weak points can be identified.

Bayesian network are increasingly used in various fields and applications such as operating safety, risk analysis, maintenance, as well as finance [4], and the field of image processing [12].

Bayesian network and fault tree have a probabilistic aspect. The main objective of the present work is to show the strong contribution of these tools in the field of fault diagnosis and enhance the knowledge in the area of ensuring reliability and maintaining of mechanical systems among simulated scenarios.

## 2. Methodology of work

The main purpose of this works is to give a methodological approach based on the transformation method of fault tree into bayesian network to model a complex system. This work is divided into:

- Qualitative exploitation of events for the fault tree representation.
- Define the undesired event to be analyzed; explicitly shows all the different relationships that are necessary to result in the top event.
- Exploits the existing data (historical data base) of the system under study, to quantify the failures probability.
- Estimate the failures probability of events by using Weibull model (failure probabilities of events are normalized to become prior failure probabilities).
- Deriving the graphical structure of the bayesian network via transforming the Fault Tree into bayesian network according to the proposed methodology.
In order to diagnose industrial system and evaluate their reliability, in the absence of analytical model, it is possible to carefully analyze the history of their behavior over time. At the end of this study, a fault diagnosis of strategic motor pump at the Annaba ARCOLOR-METAL (Algeria) is presented.


### 2.1. Bayesian network

A Bayesian network is a probabilistic graphical model that represents a set of random variables represented by nodes, bounded by oriented arcs and accompanied by their conditional independencies. In a formal way, a Bayesian network is defined by [13]:

- Its graphical component represented by a graphe $G$ directed acyclic (DAG) comprising nodes $X$, and arcs $E, G=(X, E)$.
- Its quantitative component $X$ represented by probability tables (PT) for parent nodes and conditional probability tables (CPT) for descendant's nodes, arcs $X=\left\{X_{i}\right\}=\left\{P\left(X_{i} /\right.\right.$ parents $\left.\left(X_{i}\right)\right)\right\}$.
- A set of random variables associated with nodes, arcs $X=\left\{X_{1}, X_{2}, . . X_{n}\right\}$, and the joint distribution function $\operatorname{arcs} P(X)$ consisting of:

$$
p\left(X_{1}, X_{2}, \ldots ., X_{n}\right)=\prod_{i=1}^{n} p\left(X_{i} / C\left(X_{i}\right)\right)
$$

where $P\left(X_{i}\right)$ is the set of causes (parents) of $X_{i}$ on the graphe $G$.

BN used Bayes theorem to update the prior belief of variables given observations of other variables. For tow event $X_{i}$ and $X_{2}$, provided that arcs $P\left(X_{2}\right) \neq 0$ consisting the relationship of joints probability to conditional and marginal probability are written as:

$$
p\left(X_{1} / X_{2}\right)=\frac{P\left(X_{1}\right) P\left(X_{2} / X_{1}\right)}{P\left(X_{2}\right)}
$$

with $p\left(X_{1}\right)$ is Priori probability (or marginal, or occurrence probability) of event $X$, it is prior in the sense that it does not take into account any information about $X_{2}$, $p\left(X_{2}\right)$ is Marginal probabilities of event $X_{2}, p\left(X_{1} / X_{2}\right)$ is Posterior probability (or conditional probability) of $X_{1}$ knowing $X_{2}, p\left(X_{2} / X_{1}\right)$ is Likelihood function (or conditional probability) of $X_{2}$ knowing $X_{1}$.

The marginal distribution of $p\left(X_{2}\right)$ is computed by:

$$
p\left(X_{2}\right)=p\left(X_{2} / X_{1}\right) p\left(X_{2}\right)+p\left(X_{2} / \bar{X}_{1}\right) p\left(\bar{X}_{1}\right)
$$

2.2. Transformation of fault tree into bayesian network methodology

Currently, modern machines and installations are becoming more complex and their failures can have severe consequences on production, at the same time; the graphical construction of bayesian network can be tedious and difficult. We can then simplify based on fault tree to determine causality between components. Fault tree construction allows building a bayesians network. This step allows deriving the graphical structure of the bayesian network that represents the causal relationship between the different events of the system under study and exploits the mass of existing data.

Building bayesian network from the fault tree is to transform the graphical representation of the fault tree into bayesian network. Events and logic Gates (AND, OR) are the basic elements for the fault tree. However, the bayesian network use as basic elements nodes that representing events and arcs that model the dependences between events and relations causes - effect.

There are several transformation methods of fault tree into bayesian network that consist to transforming the logical gates to nodes on the network, this methodes incre-

ase the nodes number and make complicated calculation. For this, the adopted method in this works consists to transform the different kinds of events of the fault tree to
nodes in the associated bayesian networks, and the logic gates (AND, OR) not participating in the form of the graphical structure of the networks $[3,6]$.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Graphical and digital transformation of Fault tree into Bayesians network

Next, the construction of a bayesian network from a fault tree lies in the estimation (quantification) of probabilities, it consists in this step to assign probabilities of occurrence of basic events (primaries) of fault tree to node roots as probabilities a priori, but in case of induced events (intermediate) and final events (dreaded) associated probabilities will be estimated on the basis of calculation of conditional probabilities. In addition, in the subject of the transformation of fault tree into bayesian network multiple works have-been performed (more details on this transformation steps shown in reference [3, 6]), the transformation algorithm of fault tree into bayesians network is displayed in Fig. 1.

## 3. Functional analysis of the motor-pump and application result

### 3.1. Description and system modeling

Modeling by using BN is performed in two steps:

- Qualitative analysis of failures: construction of the network or the graph.
- Quantitative analysis of failures: deriving or estimating the probability distribution tables.
Qualitative step allows deriving the graphical structure of the bayesian network that represents the causal relations ship between the different events in the motor pump G18A.

As part of preventive maintenance, the motorpump G18A plays a strategic role in the cooling of the iron rods getting out from the electric oven; its failures influence directly the continuity of service.

After the functional decomposition of defects which affect the proper functioning of the motor pump (qualitative phase), the failure modes are classified into three main types (M: Mechanical, E: Electric, H: Hydraulic), this qualitative analysis allows identifying failure modes and construction fault tree as shown in Fig (1), by transforming the fault tree into bayesian network. Each variable corresponds to a node. Model of Cause-effect and
its generic structure are shown in Fig (2), and it is split into three levels:

- Top Event (S) is the motor-pump is in field state (undesired event).
- Basic undesirable events are (H111, H112, H113. H114, H21, H22, H23, H24, E41 E42, E11, M11, M12, M221, M222, M51, M52).
- Intermediate events are the remaining nodes (consequences).
The hypothesis used in our modeling concerns quantitative analysis of fault tree analysis is to assume that components corresponding to basic events follow adjusted Weibull law. This means that:
$t=t_{2}, \ldots t_{N} ;$ Times between failures following Weibull model, and the probability of having component $(X)$ faulty at time t (alternatively the probability of occurrence of the basic event $X=$ faulty) is :

$$
P(X=f a u l t y, \mathrm{t})=F(t)=1-\exp \left[-\left(\frac{t}{\eta}\right)^{\beta}\right]
$$

Where: $t$ represent time between failures.
The shape parameter $\beta$ and the scale parameter, $\eta$, of the Weibull pdf are obtained by maximizing the following log-verisimilitude:

$$
L\left(t_{1}, \beta, \eta\right)=\ln \left\{\prod_{i, j} \frac{\beta}{\eta}\left(\frac{t_{i}}{\eta}\right)^{\beta-1} \exp \left[-\left(\frac{t_{i}}{\eta}\right)^{\beta}\right]\right\}
$$

3.2. Inference and conditional probabilities

Bayesian inference is the process or the logic to calculate or revise the probability of belief (hypostasis).

After describing the bayesian network, which will be used in the follow-up diagnosis of the motor pump, the failure probabilities of components are normalized to become prior failure probabilities and reported in Table1.

When the BN structure is defined, the probabilities are assigned (prior probabilities for the root nodes from Eq. (4), and conditional probabilities tables "CPTs" for their child node are given according to the gate types), the bayesian inference can then be conducted. It allows the computation of the marginal probability of a node (compo-
nent or event) by taking into account the interactions between the nodes of the network.

The estimation of the Weibull parameters with the MATLAB function "wblfit" gives $\beta=3.21$ and $\eta=2681.22$.
![img-1.jpeg](img-1.jpeg)

Fig 2 Qualitative analysis by fault tree for the motor-pump system
![img-2.jpeg](img-2.jpeg)

Fig. 3 Bayesian network of the motor-pump used in fault diagnosis

Events and their priors and posteriors probability


The model for characterizing the defects of the motor pump according to the principle of total probability theorem and bays law is given by:

$$
\begin{aligned}
& P(S)=P(M \cup E \cup H) \\
& P(S, M, E, H)=P(S / M, E, H) P(M, E, H)
\end{aligned}
$$

$$
\begin{aligned}
& P(M / S)=\frac{P(S / M) P(M)}{P(S)} \\
& P(H / S)=\frac{P(S / H) P(H)}{P(S)} \\
& P(E / S)=\frac{P(S / E) P(E)}{P(S)}
\end{aligned}
$$

We start by building a probability space on the initiative knowledge, and we will see how beliefs vary.

Subsystems probabilities of failures are normalized to become prior probabilities and tow modalities will be kept:

- Presence of defects (T : true)
- Absence of defects (F: false)

Different questions arise: example, what is the probability that the motor-pump still works knowing that there is a mechanical fault?

Table 2
Conditional probabilities of variables $M, E, H$, express the knowledge that the presence of different defaults in the motor-pump


The achieved calculations from the equations (7), (8), (9) and (10) are presented in Fig. 4.

We proceed firstly, that the inference makes it possible to propagate any probability instantiated or a priori on the belief of the other nodes. A new table of beliefs (probabilities) is obtained on each node, a kind of new state of the premises. In reality a model of probabilistic behavior is realized by the bayesian networks on the mo-tor-pump.
![img-3.jpeg](img-3.jpeg)

Fig. 4 Bayesian network of the motor-pump
Fig. 4 shows the inference permit to obtain a new table of beliefs on each node.

The high probabilities of failures of the motorpump (Top event) are in the order of $18.9 \%$.

The probabilities of failures of the motor-pump respectively mechanical, electrical and hydraulic knowing that there is a malfunction in the motor-pump equal to 99.4, 98.3 and $83 \%$; these allow us to update the beliefs to priori probability.

### 3.3. Fault diagnosis

According to the values of the posterior probability in Table 1, the presence of defects in the motor-pump is mainly caused by event M51.which summarizes the out of balance (M51) defect is the most likely source to stop the motor-pump.

The objective of this application is to make a diagnosis on the out of balance defect of the motor-pump (we will be interested on the presence or absence of the defect of bending rotor).

The diagnosis in this application consists to computing probabilities of new observations described in the
following scenarios.
Scenarios 1: this scenario is related to the system's nominal operating condition. In this step, given the fact that there is no observed fault on the motor pump, the joint probability is equal to one. The BN corresponding to this scenario is given in Fig. 5.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Scenario 1: nominal operating condition
Fig. 5 Shows that the probability of occurrence of the top event $P$ (motor-pump failed state) $=P(S)=0.189$, which are worth $18.9 \%$ and that the bending rotor, the break of vanes and the Out of balance remain in their respective nominal case (presence state defect),( with probabilities equal to $99.4,91.5$ and $9.03 \%$ respectively. These probabilities are quantitatively unacceptable, also since the machine is strategic and in order to optimize the operation security, it is mandatory to seek for identification of the faults' root causes of the system to better plan the maintenance actions and to identify the preventive solutions to minimize this percentage.

The high probability $99.4 \%$ means that the bending rotor (M51) is the most likely event to stop the motor-pump and should be treated as a priority.

Scenario 2: (Absence of fault on the out of balance) one tends then to believe that the presence of the out

of balance could have been caused by a fault on the bending rotor or break of vanes and this scenario will lead to:
![img-5.jpeg](img-5.jpeg)
(a) Absence a fault on the bending rotor
![img-6.jpeg](img-6.jpeg)
(b) Absence a fault on the break of vanes

Fig. 6 Scenario 2: Absence a fault on the out of balance

- We suppose that the fault on the bending rotor $(P(S=$ false $)=1)$. With a probability value of $P(S=$ true $[\mathrm{M} 51=$ false $)=0.022)$.

Fig. 6, a illustrates the probability of the event $P(M 5=$ false/ $M 51=$ true $)=8.50 \%$.

- We suppose that the fault on the bending rotor and break of vanes $(P(S=$ false $)=1)$. With a probability value of $P(S=$ true $[M 51=$ false, $M 52=$ false $)=0.012)$.

Fig. 6, b illustrates the probability of the event $P(M 5=$ false/ $M 51=$ true, M52=true $)=0 \%$.

According to this scenario the probability of occurrence of the top event $P$ (motor-pump failed state) $(P(S)$ is equal to 0.012$)$. The result justifies the decrease in the probability value (from 18 to $1.2 \%$ ) that the out of balance would be the cause of the unreliability of the motor pump, and this result is practically more credible giving the number of elements and components that are participated in its function and which can produce this faulty situation (motor-pump failed state).

To improve the results analysis, uncertainties on the parameters " $\beta$ " and " $\eta$ " have been taken into account. The associated $95 \%$ confidence intervals for $\beta$ and $\eta$ obtained using the Matlab function "wblfit" are [2.3984, 4.3015] and [2356.4, 3050.8], respectively. We considered five values, uniformly generated, for each parameter:
$\left[\beta_{1}, \beta_{2}, \beta_{3}, \beta_{4}, \beta_{5}\right]=[2.398,2.874,3.349,3.825,4.301]$; $\left[\eta_{1}, \eta_{2}, \eta_{3}, \eta_{4}, \eta_{5}\right]=[2356.42,2530,2703.58,2877.17$, 3050.75].

The results obtained for both scenarios 1 and 2 are summarized in Table 3, 4 and 5 respectively.

Table3
Posterior probability of the top event for the first scenario with uncertainty on $\beta$ and $\eta$


Table4
Posterior probability of the top event for the absence a fault on the bending rotor with uncertainty on $\beta$ and $\eta$


Table5
Posterior probability of the top event for the absence a fault on the break of vanes with uncertainty on $\beta$ and $\eta$


We should notice that bending rotor $(M 51)$ is still the most likely event to stop the motor-pump for each couple $(\beta, \eta)$.

In order to characterize the uncertainty related to the posterior probabilities, we give hereafter the mean $(\mu)$ and the standard deviation $(\sigma)$ for each scenario.

- Scenario 1: $\mu=0.1808, \sigma=0.0474$.
- Scenario 2 (a): $\mu=0.0221, \sigma=0.0157$.
- Scenario 2 (b): $\mu=0.0068, \sigma=0.0041$.


## 4. Conclusion

This paper presents the application of bayesians networks and fault tree to diagnose motor- pump defects.

The construction of the graphical model of the motor-pump (variable identification and their modes, causal relationship, quantification of probabilities, etc.) was performed according to historical data.

According to the fault tree results and the values of conditional probability, the presence of defects in the motor-pump are mainly caused by the event M51, which indicates that the defect of unbalance (M5) is the most likely source to stop the motor-pump.

Fault tree method allows thanks to its qualitative and quantitative aspects, an event scenario leading to top undesirable events (motor-pump failed state). For diagnosis or to model multi-state variable system, bayesian network is well adapted.

Bayesian inferences permit to calculate the joint posterior probability of the different variables which can overcome the limitations of fault tree regarding the diagnosis.

According to the scenarios modeled in this work the probability of occurrence of the top event $P$ (motorpump failed state) $=P(S)=1.2 \%$. This result is practically credible giving the number of elements and components that participate in its function and which can produce this faulty situation (motor-pump failed state).

The Analysis of the obtained results by the methodology of converting the fault tree into bayesian networks allowed to identify the undesirable and critical components, and contributed in using the targeted preventive maintenance in order to increase the system's reliability and availability. Thus, in order to optimize the availability of this motor pump rigorous monitoring of its behavior and an effective supervision must be carried out.

## TRANSFORMATION OF FAULT TREE INTO BAYESIAN NETWORK METHODOLOGY FOR FAULT DIAGNOSIS

## Summary

In this article, we have shown an application of a decision support tool which is the FTBN. The combination of bayesian network (BN) with fault tree (FT) is an interesting approach to diagnose mechanical systems. Bayesian networks provide robust probabilistic methods of reasoning under uncertainty, widely used in the field of reliability and fault diagnosis. Fault tree is a method of deductive analysis based on the realization of an arborescence used to identify combinations of failures. Since both tools have a probabilistic aspect, the main purpose of this work is to give a methodological approach based on the transformation method of fault tree into bayesian network to model a mechanical system, more specifically the fault diagnosis.

Fault tree construction allows building a bayesians network. Deriving the graphical structure of the bayesian network will represent the causal relationship between the different events, and exploits the mass of existing data (experience feedback database) of the system under study.

In this paper a methodology approach is used to conduct quantification of conditionals probabilities of this network, and performed a diagnosis on the out of balance trough modeled scenarios. The proposed methodology in our paper is centred on the presence or absence of the out of balance of the motor-pump. Knowing that the source of this unbalance is caused by tows essentially events in the
fault tree: bending rotor and break of vanes. This statement remains valid when uncertainties are taken into account.

Keywords: bayesians network; fault tree; Probability; inference; modeling; diagnosis; maintenance.

Received December 17, 2016
Accepted December 07, 2017