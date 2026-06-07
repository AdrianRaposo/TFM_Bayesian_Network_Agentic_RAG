# HAL open science 

## A dynamic Bayesian network approach for prognosis computations on discrete states systems

Josquin Foulliaron, Laurent Bouillaut, Patrice Aknin, Anne Barros

## To cite this version:

Josquin Foulliaron, Laurent Bouillaut, Patrice Aknin, Anne Barros. A dynamic Bayesian network approach for prognosis computations on discrete states systems. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability, 2017, 231 (5), pp. 516-533. 10.1177/1748006X17712661 . hal-01816417

## HAL Id: hal-01816417 <br> https://hal.science/hal-01816417v1

Submitted on 15 Jun 2018

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# A dynamic Bayesian network approach for prognosis computations on discrete states systems 

Journal name<br>000(00):1-13<br>©The Author(s) 2010<br>Reprints and permission:<br>sagepub.co.uk/journalsPermissions.nav<br>DOI:doi number<br>http://mms.sagepub.com

## J. Foulliaron*, L. Bouillaut <br> Universite Paris-Est, IFSTTAR, GRETTIA, F-93166 Noisy-le-Grand, France

## P.Aknin

SNCF- Innovation \& Research , 40 avenue des Terroirs de France, 75611 PARIS cedex 12, France

## A.Barros

RAMS Group, Norwegian University of Science and Technology S. P. Andersens veg 5, Valgrinda 2.308A 7491 Trondheim Norway


#### Abstract

The maintenance optimization of complex systems is a key question. One important objective is to be able to anticipate future maintenance actions required to optimize the logistic and future investments. That is why, over the past few years, the predictive maintenance approaches have been an expanding area of research. They rely on the concept of prognosis. Many papers have shown how Dynamic Bayesian Networks (DBN) can be relevant to represent multicomponent complex systems and carry out reliability studies. The Diagnosis \& maintenance group from IFSTTAR developed a model (VirMaLaB : Virtual Maintenance Laboratory) based on DBN in order to model a multicomponent system with its degradation dynamic and its diagnosis and maintenance processes. Its main purpose is to model a maintenance policy to be able to optimize the maintenance parameters due to the use of DBN. A discrete state space system is considered, periodically observable through a diagnosis process Such systems are common in railway or road infrastructures fields. This paper presents a prognosis algorithm whose purpose is to compute the Remaining useful life (RUL) of the system and update this estimation each time a new diagnosis is available. Then, a representation of this algorithm is given as a DBN in order to be next integrated into the VirMaLaB model to include the set of predictive maintenance policies. Inference computation questions on the considered DBN will be discussed. Finally, an application on simulated data will be presented.


[^0]
[^0]:    * Corresponding author; e-mail: josquin.foulliaron@ifsttar.fr

# Keywords 

Reliability, Prognosis algorithm, Discrete state space systems, Dynamic Bayesian Network, Inference, Degradation modelling

## 1. Introduction

For the last fifty years, systems in most industrial fields have increased their complexity. A failure can lead at best, to a poorer performance in some parts of the system, and at worst to a complete shut-down that can cause an important security risk. When a failure is detected, it is necessary to find its cause, to get new components to replace and then to repair the damaged part. All these operations make the system unavailable for quite a long time which costs money. In the specific case of a transport system like a railway, a failure on a train can stop the whole the train traffic. It has important consequences on the performance of the line. Moreover, the number of users is increasing and companies have to do with specific security norms. It thus makes necessary both to increase the availability of the material and to guarantee a high level of security keeping down maintenance costs. For this reason, optimizing the maintenance of complex systems has become a key issue. Currently, most companies use a compromise between systematic and corrective maintenance. Anyway, a maintenance action can be very costly specially if it has not been anticipated. Consequently, optimization of maintenance policies requires an anticipation of the future failure time which corresponds to a prognosis computation. The predictive maintenance is based on this principle and has been an expanding area of research since past few years (14)(9). The prognosis result could be subsequently used to optimize the maintenance and diagnosis schedule.
To describe the behaviour of a complex system and its diagnosis and maintenance process, we need a model that can represent a multicomponent system with potential dependency relationships between its components, the diagnosis devices, the maintenance actions and their influence on the degradation process of each component. In this paper, periodically observable multicomponent systems with discrete states are considered.

Probabilistic Graphical Models are mathematical objects that can model complex systems behaviour. Particularly, Dynamic Bayesian Networks (DBN) are powerful tools to represent complex systems evolving in time because of their simplicity and specially in their way of representing the causal relationships between system components (13)(15).
It is usually assumed that a DBN has the Markov property that makes possible to simplify its complexity and thereby the complexity of the computations. But the Markov property implies that the sojourn time in each state is exponentially distributed (or geometrically distributed in the discrete case). In practice, systems behaviours are usually different and it was proved that considering exponential laws for sojourn times implies losing a lot of information about the degradation process. It thus leads to poor estimations concerning the future state of the system and consequently inadequate optimization of maintenance parameters.(1). To address this problem, Donat et al. (6) developed the Graphical Duration Model (GDM) that is a modification of duration variables from (13). It brings the possibility to use any discrete distribution for sojourn times associated to each state.
In (8), Foulliaron et al. proposed an extension of GDM in order to improve the degradation modelling. This new degradation model can consider some existing degradation modes and can adapt the degradation modelling to a mode change.
The Diagnosis \& Maintenance group from IFSTTAR developed a graphical model called VirMaLab (Virtual Maintenance Laboratory) based on DBN and GDM to describe the degradation dynamic of a system and its Diagnosis/Maintenance process.(2). It can be used to optimize the maintenance parameters according to multiple constraints, (reliability rate, costs, ..)
Some studies like (16) used a DBN to perform prognosis computation but the RUL was never represented as a specific node in a DBN.

The aim of this paper is to present a prognosis algorithm and its representation in order to integrate it into an extended VirMaLaB model that could represent a multicomponent system and every kind of maintenance policy and particularly the set of predictive maintenance strategies based on prognosis computations. This methodology apply on discrete state space systems that can be periodically observable through a diagnosis process. Such systems are common for example in railway or road infrastructures fields. Its particularity is to consider the degradation process from a "sojourn time" point of view. It proposes a prognosis algorithm based on this vision and presents its representation as a Dynamic Bayesian network in order to be next included in the VirMaLab approach. It is divided into two parts:

In the first part, we will present the framework from where we will start. The most commonly used maintenance policies and main approaches for prognosis will be first reviewed. Then, the context and the point of view used to model the degradation process will be explained. At last, the mathematical formalism (Dynamic Bayesian networks, Graphical Duration Model and its extension) used to build the VirMaLab model will be presented.
The second part will focuses on the contribution of this paper. It will be divided into three sections. The first one will present a prognosis algorithm based on GDM and its extension whose purpose is to compute and update a RUL estimation each time a new diagnosis of the system is available. Some explanati ons and illustrations will be added to make easier the understanding of how it works. In a second section, a representation of the prognosis algorithm as a DBN will be given. The third section will discuss the different inference methods that could be used on this DBN. Because of the complexity of the graph and the size of some nodes, a specific inference algorithm will be proposed to perform exact inference computation on the prognosis part of the DBN. The last section will present an application case, on simulated data, to illustrate how the methodology could be used in practice.
Finally, remaining difficulties concerning the complexity of computations and the main existing perspectives will be discussed.

# List of acronyms 

BN : Bayesian network
DBN : Dynamic Bayesian network
CPT : Conditional probability table
GDM : Graphical duration model
STD : Sojourn time distribution
CSTD : Conditional sojourn time distribution
$X^{(t)}$ : Stochastic process representing the state of the considered system
$S^{(t)}$ : Stochastic process representing the remaining sojourn time for the system to be on current state.
$\Psi_{x / y}$ : Conditional sojourn time distribution on state x knowing state y
$x_{F}$ : Failure state
$T_{S}$ : Maximal possible sojourn time among all states
$T_{E C S}^{(t)}$ : Time elapsed on the current state at time t
$T_{R C S}^{(t)}$ : Estimation of the remaining time on the current state at time t
$R^{(t)}$ : Sum of all sojourn times until the last state before the failure $\Delta t$ : Constant time interval between diagnoses
$\Psi[a, b]$ : Normalized restriction of the function $\Psi$ on interval [a,b]
$R U L$ : Remaining useful life.

# 2. Starting framework 

### 2.1. To a predictive maintenance approach

This part gives an overview of the most used maintenance policies, and try to explain why the predictive maintenance can be very useful to optimize the maintenance schedule.

The set of usually used maintenance policies can be divided in two categories : corrective maintenance and preventive maintenance (17). Principe of corrective maintenance is to repair a component when a failure occurs. In this case, a complete repair of the component (curative maintenance), or a minimal temporarily repair (palliative maintenance) can be performed.
These approaches can be used if broken components could be easily replaced and the failure state can be reached without causing risks of security or big costs. In other situations, preventive maintenance is used, consisting in preventing failures by acting before their apparitions. In this category, three approaches exist: systematic maintenance, condition based maintenance (CBM) and predictive maintenance.
Systematic maintenance is defined by a planning of replacement of components. In this approach, we don't try to know in what level of degradation we are, components are replaced at planned instant whatever state they are in. So, the main question is to choose the best instants to guarantee a tolerable level of safety keeping reasonable costs and avoiding useless repairs on good health components. The advantage of this maintenance policy is to be able to handle the maintenance requirement.
Condition based maintenance is based on a monitoring of the system, providing a diagnosis of the operating state through some indicators on which threshold will be defined. This approach requires to get a diagnosis of the system state. In this case, the question is to optimize the inspection frequency and the chosen threshold (18). The interest is to have "just in time" maintenance actions. However, it leads to unanticipated maintenance.
The predictive maintenance is attempting to integrate both advantage of systematic and condition-based maintenance. Its principle is to adapt maintenance actions according to a computed estimation of the future failure time of the system.
In this case, it is possible to optimize the logistics by anticipating the maintenance requirement. This kind of maintenance policy can be the best one, if it is correctly optimized.

The projection of the future health state of the system relies on the concept of prognosis. There are many ways in the literature to define what a prognosis computation is (11).
In this paper, we will consider the classical definition: The prognosis is the computation of a duration called the remaining useful life (RUL). It is defined as the remaining time before the system reaches a state that is considered to be intolerable. It can be the failure state or another state that is close to it. To perform a prognosis computation, modelling the dynamics of the considered system is required. Many different approaches are commonly used. They can be classified into three groups (3).

- Models based approach : is interesting when an analytic expression (like differential equation, or dynamical systems) modelling the degradation process of the system is available. This kind of equations is frequently obtained from mechanical laws.
- Data based approach : consists in using monitoring data to predict the future behaviour using statistical methods (linear regression, time series models,..). In this approach no comprehension about why the system evolves as observed is needed. A global trend about the health state evolution is just extracted from collected observations and the methodology computes projections from this trend.
- Reliability approach : consists in using feedback, expert opinion, return on operating experience, to estimate the probability laws of possible events. Data are collected to learn a degradation model using probabilistic graphical models (Bayesian

network, Petri nets, neuronal networks..) or stochastic processes (Gamma process, Poisson process,..). In the next section, the context of the study and the considered degradation modelling will be introduced.

### 2.2 Context and degradation model

In our framework, no mechanical degradation model and no continuous monitoring devices are available. The system is just periodically observable through a diagnosis process. So, an hybrid approach based both on reliability and data will be developed. In this part, we are at the component scale. The state of a component is represented with a stochastic process with discrete state space and discrete time denoted $X^{(t)}$ where state 1 is the new state, and $x_{F}$ is the failure state. So $t \in \mathbb{N}$ and $X^{(t)} \in\left\{1, . ., x_{F}\right\}$. This state is considered to be hidden and can only be known at some instant through a diagnosis device when this one is available. The diagnosis result could have some confusion rate.
It is assumed that $X^{(t)}$ is an increasing monotone process. From a state, it is only possible to stay on it or go to a more advanced degradation state. $\forall t, X^{(t+1)} \geq X^{(t)}$. It is assumed that there is no auto repair, and the failure state is absorbent. It can only be left with a corrective maintenance action. In this context, the RUL computed at time $t$ for prognosis is a random variable formally defined as :

$$
R U L^{(t)}=\inf _{T, T>t}\left\{X^{(T)}=x_{F}\right\}-t
$$

A visual description of the RUL is presented on figure 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. RUL illustration in the presented context

Unlike most models in reliability, we don't try to get a function that describes the evolution of $X^{(t)}$ in function of $t$, but we consider the opposite point of view that is based on sojourn time distribution (STD) of each degradation state. The sojourn time distribution on state x is a finite discrete probability function denoted $\Psi_{x}$ and defined on the set of discrete values $\left\{1,2,3, . ., T_{S}\right\}$ where $T_{S}$ is denoted as the maximal possible sojourn time among all states. The active sojourn time is a random variable denoted S. The active sojourn time on state x is denoted $S_{x}$. This approach is illustrated in Figure 2.

Whereas classical models in reliability use stochastic processes (like Gamma process, Wiener process) with two or three parameters, this discrete "sojourn time" approach requires a large amount of parameters that are not always easy to learn, but the main advantage is that no assumption is required concerning the degradation dynamic modelling and its stochastic properties. Moreover, it perfectly match mixtures without needing to know if this mixture exists and to estimate its number of components.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Sojourn time based degradation model

The STD for each state is learnt with the maximum likelihood method. In the discrete case of our framework, by denoting $\Psi_{x}$ as the STD on state x , applying this method leads to the following formula :

$$
\Psi_{x}(k)=p\left(S_{x}=k\right)=\frac{N_{x, k}}{|D|}
$$

where $|D|$ is the number of observations in the database and $N_{x, k}$ the number of observations that contain a sojourn time equal to k on state x . So, the desired probabilities can be directly deduced from the frequencies histogram associated to the observation database. In the case of an incomplete database, an EM algorithm could be used to get those probabilities (5). So the degradation model, is the set of discrete distributions $\left\{\Psi_{1}, . ., \Psi_{x_{F}}\right\}$ where

$$
\forall x, \sum_{k=1}^{T_{S}} \Psi_{x}(k)=1
$$

# 2.3. Extension with conditional sojourn times distributions 

This section briefly presents an extended degradation model using the concept of conditional sojourn time distribution (CSTD). This extension will be explained in detail in another paper that will be very soon submitted to "Journal of risk and Reliability". The main idea is to consider that STDs associated to the different degradation states are not independent. So, conditional sojourn time distributions are used. It is considered that the system can be in many different degradation modes (or dynamic). The STD in each state is in this case a mixture model with $n_{M}$ components where $n_{M}$ is the number of considered degradation modes. For a given state x , the component of its mixture is a CSTD describing the sojourn time in state x knowing the system is in a specific mode. The CSTD in state x knowing the mode $m_{j}$ is denoted $\Psi_{x / m_{j}}$ where $m_{j}$ is the j-th considered mode $\left(j \in\left\{1, . ., n_{M}\right\}\right)$. The mixture model is learnt with a EM algorithm. The number of modes can be chosen with a BIC or a AIC criterion. So a global SJD in a state x as a mixture of CSTD defined as following :

$$
\Psi_{x}=\sum_{j=1}^{n_{M}} w_{j} \Psi_{x / m_{j}}
$$

where $w_{j}$ are the weights of the mixture components. An example of STD with two degradation modes is shown on figure 3 .

![img-2.jpeg](img-2.jpeg)

Fig. 3. Example of SJD on a given state $x$ for a system with 2 degradation modes

The objective is then to follow the effect of a degradation mode over all states by considering CSTD in a state knowing the system was on a degradation mode in the previous state. At each time, the most likely mode is estimated. STD in futur states can be changed when a mode change is detected by using adequate CSTD. This modified GDM using CSTD is denoted GDM-CSTD. The interest of this extended degradation model is to consider system that have many degradation modes. Let consider a system with many subcomponents. Let assume that the diagnosis of the state can only be performed at the scale of the system. In this case the global visible degradation at the system scale is function of the different hidden degradation processes of all subcomponents. This is an exemple of situation involving many degradation modes. The sojourn time distributions of the observed system will contain many degradation modes associated to the hidden degradations of each subcomponent. Another interesting cases for this this model is when the available observation database mixes many observations from systems under different operating conditions involving many degradation dynamics.

Next section presents the mathematical objects that have been used to represent the degradation model that have just been presented and its extension.

# 2.4. From Bayesian network to Dynamic Bayesian network 

Bayesian networks (BNs) are directed acyclic graphs in which each node represents a random variable (10). An arrow from a node $X_{i}$ to another one $X_{j}$ represents a dependency relationship between the random variables $X_{i}$ and $X_{j}$ (an influence of $X_{i}$ on $X_{j}$ ).
The parameter of each node is the conditional probability table (CPT) of its variable given the variables of the parent nodes. A CPT mathematically corresponds to a multidimensional array also called "potential".
An example of BN is shown in Figure 4. The graph of the BN supposes some conditional independence relationships between some sets of variable (Their existence is linked to the d-separation property in the graph, see (10) or (15) for more details). It leads to the main property of the BN. The joint law of all random variables can be factorized as the product of local CPTs. If we denote $p a\left(X_{i}\right)$ as the set of parents nodes of node $X_{i}$. we have the general formula :

$$
P\left(X_{1}, X_{2}, . ., X_{n}\right)=\prod_{i=i}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Example of 4 nodes BN

Dynamic Bayesian Networks are an extension of BN adding the time dimension (13). Random variables are not static but stochastic processes. They evolve over time. In our framework, we only use discrete random variables with discrete time. DBNs are like BNs with temporal dependency.
Usually, to simplify the model, the first order Markov property is assumed in the stochastic process. It means that the states of all random variables at time $t$ only depend on states at the previous time. In other words, in the graph, the dependence arrows from a node in slice $t$ only go to nodes in the same slice or to other nodes in slice $t+1$. It is assumed that the graph is homogeneous(conditional probabilities of $X^{(t)} \mid X^{(t-1)}$ don't depend on $t$ ).
From this assumption, it is just necessary to formally define a first order DBN like this : (denoted 2-DBN for 2 time slice DBN)
-A static $B N_{1}$ at initial time :

$$
P\left(X_{1}^{(1)}, X_{2}^{(1)}, . ., X_{n}^{(1)}\right)=\prod_{k=1}^{n} P\left(X_{k}^{(1)} \mid p a\left(X_{k}^{(1)}\right)\right)
$$

-A transition model $B N_{\rightarrow}$ :

$$
P\left(X_{1}^{(t)}, X_{2}^{(t)}, . ., X_{n}^{(t)} \mid X_{1}^{(t-1)}, X_{2}^{(t-1)}, . ., X_{n}^{(t-1)}\right)=\prod_{k=1}^{n} P\left(X_{k}^{(t)} \mid p a\left(X_{k}^{(t)}\right)\right)
$$

where $p a\left(X_{k}\right)$ is the set of parent nodes of $X_{k}$.
Figure 5 is an example of a complete representation of a first order DBN. It contains the initial and the transition model. Dotted arrows correspond to time dependencies.
The main advantage of this representation is that both qualitative and quantitative nodes can be mixed in a same model
![img-4.jpeg](img-4.jpeg)

Fig. 5. Example of 1-DBN with 4 variables $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$

and represent many causality relationships. Most of the DBN used have nodes with discrete space states. There are thus many parameters for each nodes to learn in order to build the model. Moreover, if nodes have large domains and have many parents, the size of potentials can be very large, and then computations could be very heavy.

In its "standard" approach, DBN induces a Markovian behaviour for each state, inducing geometrically distributed sojourn times. To overcome this limitation and keep the "sojourn time" point of view mentioned previously, a particular graphical model was proposed and will be reviewed in the next section.

# 2.5. Graphical Duration Models 

Graphical Duration Model (6) is a specific Dynamic Bayesian network in which each considered variable $X^{(t)}$ has its own duration variable denoted $S^{(t)}$ that controls its sojourn time . $S^{(t)}$ represents the remaining time at time $t$ before the next transition of $X$. The probability of $X^{(t+1)}$ is conditioned by $X^{(t)}$ and $S^{(t)}$. At each time step, the value of $S^{(t)}$ decreases by one unit. When the value of $S^{(t)}$ is different from one, the state of $X^{(t)}$ is blocked. If $S^{(t)}$ is equal to $1, X^{(t)}$ is free to go to the next state, and the new value for $S^{(t+1)}$ is chosen according to the sojourn time distribution associated with the new state $X^{(t+1)}$.
The CPT of node $S$ is a $\mathrm{n}^{*} T_{S}$ potential where n is the number of possible states for $\mathrm{X} . T_{S}$ is the maximal possible sojourn time among all states of X . The CPT of $X$ and $S$ are defined as below ${ }^{1}$ :

$$
\begin{gathered}
S^{(t+1)}= \begin{cases}S^{(t)}-1 & \text { if } S^{(t)} \neq 1 \\
\sim \Psi_{X^{(t+1)}} & \text { if } S^{(t)}=1\end{cases} \\
X^{(t+1)}= \begin{cases}X^{(t)}+1 & \text { if } S^{(t)}=1 \\
X^{(t)} & \text { otherwise }\end{cases}
\end{gathered}
$$

where $\Psi_{x}$ is the STD for state x. A representation of GDM is shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Fig. 6. DBN reprentation of GDM
If we want to use the conditional sojourn time distributions (CSTD) improvement mentioned in part 3.5, it is necessary to add one node denoted $C_{1}^{(t)}$ to the graphical duration model. $C_{1}^{(t)}$ represents the active mode at time $t$ and is defined so that :

$$
C_{1}^{(t+1)}= \begin{cases}C_{1}^{(t)} & \text { if } S^{(t)} \neq 1 \\ \underset{k}{\arg \max }\left(P\left(\text { mode }=k \mid S^{(t+1)}\right)\right) & \text { if } S^{(t)}=1\end{cases}
$$

The probability $P($ mode $=k \mid S^{(t+1)}))$ is are a posteriori probabilities deduced from the mixture models learnt with the EM algorithm. More explanations can be found in (8). Figure 7 illustrates the graphical duration model with its extension integrating the CSTD. Some texts describe the dependencies represented by arrows. To sum-up, this model gives the

[^0]
[^0]:    ${ }^{1}$ Notation $S \sim \Psi$ means that the quantity S follows the distribution $\Psi$

![img-6.jpeg](img-6.jpeg)

Fig. 7. GDM extended to conditional sojourn time distribution
possibility to better model the degradation process without the drawback of a geometric law on sojourn time. $S^{(t)}$ can follow any discrete probability distribution. In this case, $X^{(t)}$ is said to be a semi-markovian process. It can consider many degradation nodes, due to node $C_{1}$ and can adapt the considered STDs to a mode change.

# 2.6. The VirMaLab model 

The VirMaLab (Virtual Maintenance Laboratory) approach aims to develop a support decision tool for optimization of maintenance parameters of complex systems (2). It is a multicomponent scale development of the degradation model described before, including the modelling of diagnosis devices and maintenance actions.
The model is split into three connected modules. The degradation process, the maintenance modelling, and the evaluation module. In the degradation process module, the real state of the system is hidden. The diagnosis nodes in the maintenance module provide an estimation of the real hidden state of the system. A non identity matrix as the CPT of the diagnosis node makes possible to model the risk of error committed by the diagnosis device modelling its false alarm rates, non detection rates and mismatch rates. The diagnosis result will determine the next maintenance decision. It will modify the real hidden state of the system. Utility nodes can be used to associate costs to some maintenance or diagnosis actions to make possible to perform cost-based optimization of maintenance parameters. The interest of the VirMaLaB model is to be able to evaluate and compare some given maintenance policies, by providing probabilistic information and reliability indicators in function of parameters, in order to optimize the maintenance strategy.
Figure 8 below represents the VirMaLab model and its three main modules. For the moment, the possible maintenance policies that can be represented with VirMaLaB are corrective, systematic and condition based maintenance. To be able to model the predictive maintenance policies based on prognosis, a prognosis algorithm has to be established and then represented as a DBN in order to be integrated into the VirMalaB model. The next part will deal with this task.

## 3. The prognosis algorithm

The following developments are the first step of a global methodology that aims to represent the decision process of a maintenance team of a company that would use a predictive maintenance policy. The prognosis algorithm, its representation

![img-7.jpeg](img-7.jpeg)

Fig. 8. VirMaLab model:
and the inference algorithms are useful only in the perspective of connecting next the RUL estimation to a maintenance action to be able to evaluate the global predictive maintenance policy.

# 3.1. Algorithm 

a) Formal definitions :

The aim of this prognosis algorithm is to compute a first estimation of the RUL $\left(R U L^{(0)}\right)$ and then to update and improve this estimation each time a new diagnosis is available. This version is based on a degradation process modelling by GDM. Before introducing the algorithm, some intermediate variables need to be detailed. Let us define :

- $t_{c o}$ : Time of current observation (last diagnosis time)
$-t_{p o}:$ Time of previous observation
- $x^{\left(t_{c o}\right)}=x_{c o}$ : State observed at time $t_{c o}\left(x \in\left\{1,2, \ldots, x_{F}\right\}\right)$.
- $x^{\left(t_{p o}\right)}$ : State observed at time $t_{p o}$
- $T_{E C S}^{\left(t_{c o}\right)}$ : Time elapsed at current state $x_{c o}$ until time $t_{c o}$
- $T_{R C S}^{\left(t_{c o}\right)}$ : Remaining time in the current state after $t_{c o}$
- $S_{x}^{(t)}$ : Estimation of the total sojourn time in state $x$ computed at time $t$
$-\Delta t$ : Time between the current observation and the last one $\left(t_{c o}-t_{p o}\right)$
- $R^{(t)}$ : Sum of all SJ in next states until the last state before failure.

Some of the previous variables are illustrated in Figure 9.

- $\Psi_{x}$ is the STD on state $x$ that represents the discrete conditional probability $p(S \mid X=x)$.
- $\alpha_{j}^{\max }$ is the maximal possible value for sojourning in state $j$. In other words: $\alpha_{j}^{\max }=\sup \left\{k, P\left(S^{(t)}=k \mid X^{(t)}=j\right)>0\right\}$
- $U[a, b]$ corresponds to the uniform distribution in [a,b] interval
- Time ( 0 ) is the algorithm starting instant.
- $S_{j}$ compatible means compatible with the last current observation.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Illustration of the main variables considered for the proposed prognosis algorithm

Notation $A \sim \Psi_{x}([a, b])$ means that the value for A is randomly drawn according to a new density denoted $\Psi^{\prime}$ that is a normalization of $\Psi$ in interval $[a, b]$. So it is defined as : $\forall x_{i} \in[a, b], \Psi^{\prime}\left(x_{i}\right)=\frac{\Psi\left(x_{i}\right)}{\sum_{x_{i} \in[a, b]} \Psi\left(x_{i}\right)}$

In this algorithm, elementary time unit was considered. It is assumed that, if the system is observed precisely at a transition time, the visible state is that after the transition and that minimal sojourn time on a state is one time unit. The abbreviation SJ is used for "sojourn time". All steps of the prognosis computation (initialization and update of the RUL) are detailed in algorithm 1. We can note that all random sampling in the algorithm can be replaced by choosing the average of the considered distribution. It has the advantage of reducing the risk of error on the prognosis.

# b) Interpretations and discussion : 

For each degradation state, during the initialization phase, a sojourn time is randomly drawn ( $S_{j}^{(0)}$ is assigned for each state $j$ ). By summing these estimations, $R^{(0)}$ is computed. $T_{R C S}^{(0)}$ is chosen with a random sampling in a specific interval taking into account the information from $T_{E C S}^{(0)}$. Then, a first estimation of the RUL is computed. At each new available observation, the RUL is re-estimated by updating intermediate variables $T_{E C S}$ and $T_{R C S}$. This update depends on the compatibility between the new observation and the last computed estimations. If a transition is observed, that isn't compatible with the previous estimations, the missed intermediate transition time is rebuilt using the STD associated to the previous state. If a lot of degradation states have been missed between two diagnosis, the real sojourn time of each intermediate state is very small so, the new $T_{E C S}$ value is estimated with a uniform sampling. Then, the RUL is obtained by adding $T_{R C S}^{(t)}$ and $R^{(t)}$. Some of those update processes are illustrated in Figures 10 and 11.

By denoting $O_{n}$ as the n-th diagnosis and $S_{j}^{\left(t_{O_{n}}\right)}=T_{E C S}^{\left(t_{O_{n}}\right)}+T_{R C S}^{\left(t_{O_{n}}\right)}$ as the sojourn time estimation on state j updated at the n-th observation, the following formula can be obtained from the algorithm :

$$
R U L^{\left(t_{O_{n}}\right)}=S_{j}^{\left(t_{O_{n}}\right)}+\sum_{j=x^{\left(t_{O_{n}}\right)}+1}^{x_{n}-1} S_{j}^{(0)}-(n-1) \Delta t
$$

So, the error committed in the RUL computation depends on the error committed in each initial sojourn time estimation $S_{j}^{(t)}$ and those associated to the last observed state. These estimations are updated and improved at each diagnosis time.

# Algorithm 1 Prognosis algorithm 

## Initialization:

1: $\forall i=1 . . x_{F}-1, S_{i}^{(0)} \sim \Psi_{i}$ (Initial random sampling of sojourn times)
2: $R^{(0)}=\sum_{j=x^{(0)}+1}^{x_{F}-1} S_{j}^{(0)}$
3: $T_{E C S}^{(0)}$ initialized by the user depending the past of the component
4: $T_{R C S}^{(0)} \sim \Psi_{x^{(0)}}\left(\left[T_{E C S}^{(0)}+1, \alpha^{M A X}\right]-T_{E C S}^{(0)}\right.$
5: $R U L^{(0)}=T_{R C S}^{(0)}+R^{(0)}$
Update: Let $x^{\left(t_{c o}\right)}$ be a new available diagnosis result :
1: if $\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}=\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}$ (case where no transition is observed) then
2: $\quad T_{E C S}^{\left(t_{c o}\right)}=T_{E C S}^{\left(t_{p o}\right)}+\Delta t$
3: if $\left(T_{R C S}^{\left(t_{p o}\right)}>\Delta t\right)$ (case where the previous estimation is compatible) then
4: $\quad T_{R C S}^{\left(t_{c o}\right)}=T_{R C S}^{\left(t_{p o}\right)}-\Delta t$
5: else
6: $\quad T_{R C S}^{\left(t_{c o}\right)}=\Psi_{x^{\left(t_{c o}\right)}}\left[T_{E C S}^{\left(t_{c o}\right)}+1, \alpha^{M A X}\right]-T_{E C S}^{\left(t_{c o}\right)}$
7: end if
8: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}$
9: else if $\left(\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}-\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}=\mathbf{1}\right)$ (if a transition is observed) then
10: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}-S_{x^{\left(t_{c o}\right)}^{(0)}}$
11: if $\left(T_{R C S}^{\left(t_{p o}\right)} \leq \Delta t\right)$ (if the previous estimation of $T_{R C S}$ is compatible) then
12: $\quad T_{E C S}^{\left(t_{c o}\right)}=\Delta t-T_{R C S}^{\left(t_{p o}\right)}$
13: else
14: $\quad T_{E C S}^{\left(t_{c o}\right)}=\Delta t-\Psi_{x^{\left(t_{p o}\right)}}\left[T_{E C S}^{\left(t_{p o}\right)}+1, T_{E C S}^{\left(t_{p o}\right)}+\Delta t\right]+T_{E C S}^{\left(t_{p o}\right)}$
15: end if
16: if $R^{\left(t_{c o}\right)}-R^{\left(t_{p o}\right)}>T_{E C S}^{\left(t_{c o}\right)}$ (if the initial SJ sampling is compatible) then
17: $\quad T_{R C S}^{\left(t_{c o}\right)}=R^{\left(t_{c o}\right)}-R^{\left(t_{p o}\right)}-T_{E C S}^{\left(t_{c o}\right)}$
18: else
19: $\quad T_{R C S}^{\left(t_{c o}\right)}=\Psi_{x^{\left(t_{c o}\right)}}\left[T_{E C S}^{\left(t_{c o}\right)}+1, \alpha^{M A X}\right]-T_{E C S}^{\left(t_{c o}\right)}$
20: end if
21: else if If $k=\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}-\mathbf{x}^{\left(\mathbf{t}_{\mathbf{p o}}\right)}>\mathbf{1}$ (if many transitions are observed) then
22: $\quad T_{E C S}^{\left(t_{c o}\right)} \sim U[0, \Delta t-k]$
23: $\quad T_{R C S}^{\left(t_{c o}\right)}=\Psi_{x^{\left(t_{c o}\right)}}\left[T_{E C S}^{\left(t_{c o}\right)}+1, \alpha_{x^{\left(t_{c o}\right)}}^{M A X}\right]-T_{E C S}^{\left(t_{c o}\right)}$
24: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}-\sum_{j=x^{\left(t_{p o}\right)}+1}^{x^{\left(t_{c o}\right)}} S_{j}$
25: end if
26: At last $R U L^{\left(t_{c o}\right)}=T_{R C S}^{\left(t_{c o}\right)}+R^{\left(t_{c o}\right)}$
27: $\forall t \in] t_{c o}, t_{f o}\left[\quad R U L^{(t)}=R U L^{\left(t_{c o}\right)}-\left(t-t_{c o}\right)\right.$ where $f o$ is the future observation.

![img-9.jpeg](img-9.jpeg)

Fig. 10. $T_{E C S}$ extending in the case where $x_{c o}=x_{p o}$
![img-10.jpeg](img-10.jpeg)

Fig. 11. Update process in some cases

The quality of the RUL computations depends on the initial sojourn time sampling and the variance of the sojourn time distributions, Consequently, one important question is to find a way to reduce the variance of the considered STDs. The purpose of the extended GDM is to limit this problem. The next section describes a modification of algorithm 1 to be adapted to the extended GDM-CSTD degradation model.

# c) Extension to conditional sojourn time : 

The use of the extended GDM using CSTD requires adapting the prognosis algorithm. In this case, the prognosis algorithm is modified as follows :

## Initialization :

- According to the original random sampling for sojourn time in state 1, the most likely mode is determined using the conditional a posteriori probabilities (mode given the sojourn time). Then, future sojourn times are chosen according to the conditional distribution associated with this mode. So $R^{(0)}$ and $T_{R C S}^{(0)}$ computations are modified.

# Update: 

Each time $T_{E C S}$ is updated, the most likely active mode is evaluated according to the new value of $T_{E C S}$ as sojourn time. If the new mode is different, then the new value of $T_{R C S}$ is chosen according to the conditional distribution associated with this new mode. $R^{(t)}$, that is the sum of all sojourn times in future states until failure state, is completely re-estimated, by performing a new drawing for all sojourn time, according to the new conditional sojourn time distributions associated with the new detected mode.

All these modifications lead to the algorithm 2 that can be found in appendix. $m^{(c o)}$ is denoted as the active mode at time co. Notation $\Psi(x)$ is the value of the STD at $\mathrm{x} . \Psi(x) / m^{(c o)}$ is the CSTD in state $x$ given the active mode $m^{(c o)}$. The main objective of CSTD is to get a more precise modelling of the degradation process considering smaller variance distributions with. This prognosis algorithm needs now to be represented as a DBN.

### 3.2. Representation of the prognosis algorithm as a DBN

This part introduces graphical representation of the prognosis algorithm presented in section 3.1 as a DBN in order to introduce it into the global VirMaLab DBN as a prognosis module.
An intuitive way to proceed is to define a node for each intermediate variable defined in the prognosis algorithm.

So, variables $T_{E C S}$ and $T_{R C S}$ are represented and some other have to be added.

- $D^{(t)}$ is the result given by the diagnosis device when it is enabled.
- Act ${ }^{(t)}$ is a binary node set on one if the diagnosis device is enabled
- $\delta^{(t)}$ : In the case of one transition, it determines how many states have been skipped.
- $C_{1}^{(t)}$ and $C_{2}^{(t)}$ : represent respectively the current active mode in the degradation module and in the prognosis module.

We remind that the purpose of the nodes that are in the hidden degradation model.

- $X^{(t)}$ is the hidden state of the system
- $S^{(t)}$ is the sojourn time variable associated to $X^{t}$ ( from GDM)

Each relationship dependency is represented by an arrow in the graph. The purpose of node $\Delta t$ is to represent the conditional structure "if then" in the algorithm. The presence of $C_{2}^{(t)}$ node is due to the use of conditional sojourn time distributions because the choice of the degradation mode influences the computations of three variables in the prognosis computation $\left(T_{R C S}^{(t)}, T_{S E C}^{(t)}\right.$ and $\left.R^{(t)}\right)$.
The set of nodes is split into three groups:

- Orange nodes are linked to the hidden degradation model. (The original GDM model)
- Blue nodes represent the variables used in the prognosis algorithm.
- Purple nodes are linked to the use of CSTD.

The prognosis part of the DBN is a graphical representation of the computing process of the prognosis algorithm described in part 3.1. The interest of this DBN is to be able to perform inference computations to get out new informations from the model. Figure 12 gives a representation of the prognosis algorithm as a specific DBN and its link with the extended degradation module from the VirMalaB model. The prognosis DBN for algorithm 1 is the same without purple nodes). The properties of the prognosis DBN presented above are studied.
$N_{S}, T_{S}$ and $N_{M}$ : denote respectively the number of state of the modelled system, the maximal value for sojourn time in all states and the number of considered degradation modes.

![img-11.jpeg](img-11.jpeg)

Fig. 12. The extended prognosis algorithm as a DBN

The size of the range of node X is denoted $|X|$. Thus:
$\left|X^{(t)}\right|=\left|D^{(t)}\right|=\left|\delta^{(t)}\right|=N_{S}$.
$\left|C_{1}^{(t)}\right|=\left|C_{2}^{(t)}\right|=N_{M}$.
$|S|=\left|T_{E C S}\right|=\left|T_{R C S}\right|=T_{S}$
$\left|R U L\right|=\left|R^{(t)}\right|=\left(N_{S}-1\right) T_{S}$

The set of nodes can be divided into two groups. The nodes that have a small domain $\left(X, A c t^{(t)}, D^{(t)}, \delta^{(t)}\right)$ and those which have a large domain $\left(S, T_{E C S}, T_{R C S}, R, R U L\right)$.
Moreover, the transition laws in nodes are deterministic or semi-deterministic. By using an inference algorithm, this model can compute the future distributions of the RUL and provide a confidence interval associated to with RUL computations.

Given $t$ : the time of the last diagnosis, $\alpha$ : the RUL computed at time $\mathrm{t}, x_{F}$, the failure state and $\left\{d_{1}, d_{2}, \ldots d_{n}\right\}$ : the set of all previous diagnosis results: according to this model, the probability for the error associated with the RUL computation to be inferior to $\epsilon$ is :

$$
p\left(\operatorname{Err}^{(t)}<\epsilon\right)=\sum_{|k|<\epsilon} p\left(X^{(t+\alpha+k)}=x_{F}, X^{(t+\alpha+k-1)} \neq x_{F} \mid R U L^{(t)}=\alpha, D^{(1)}=d_{1}, D^{(2)}=d_{2}, . ., D^{(t)}=d_{n}\right)
$$

With the conditional probability relationship induced by the graph, $X^{(t+\alpha+k)}, X^{(t+\alpha+k-1)}$ is independent from $R U L^{t}$ given $\left(D_{1}, . . D_{t}\right)$ so, this probability is equal to

$$
p\left(\operatorname{Err}_{t}<\epsilon\right)=\sum_{|k|<\epsilon} p\left(X^{(t+\alpha+k)}=x_{F}, X^{(t+\alpha+k-1)} \neq x_{F} \mid D^{(1)}=d_{1}, D^{(2)}=d_{2}, . ., D^{(n)}=d_{n}\right)
$$

We then face to a prediction problem. If we consider a set of random values following a given probability distribution, the mathematical expectancy has the property to minimize the total of the distances squared. In other words, it minimizes the risk of error. The use of the variant method in the prognosis algorithm, leads to a RUL estimation that minimizes the risk of error.
In section 3, the inference process that is used to compute this probability will be detailed.

# 3.3. Inference process and algorithm for computations 

Inference is a computation process that aims to get a probability of type $P\left(X_{r} \mid X_{o}\right)$ where $X_{o)}$ is the set of the observed variables, and $X_{r}$ is called the request.
Two different approaches are commonly used to perform inference computations in a DBN (13) :

- Exact inference.
- Approximate inference

Approximate inference consists in using a Monte-Carlo simulation. In this case many trajectories are simulated with the DBN, and the frequency of trajectories corresponding to the inference request converge to the desired probability. The drawback is that many simulations are needed to hope to get accurate an estimation of the desired probability.
The exact methods lays on algebraic computations on CPTs of the nodes. In this paper we focus on the elimination variable algorithm(4) . Let remember that in a first order DBN, the left interface ( $I^{-}$) is defined as the set of nodes that have at least one child in the next time slice. The interface algorithm from (13) is an improvement of the elimination variable algorithm using the Markov property in a DBN. It rely on the following proposition.
All of the nodes at time $t+1$ are independent from all the past given the left interface. So to get the joint law at slice $t+1$ is just needed the joint law of the left interface at time $t$. In our case, prediction computation are requested (that is to say of type : $p\left(X^{(t+\Delta t)} \mid X^{(t)}\right)$ so, a forward process is used to compute the desired probability (ie nodes on slice $t-1$ are eliminated before nodes from slice $t)$. But this algorithm requires to stock the left interface for each iteration slice update.
In the prognosis DBN presented in figure 12, the left interface contains 8 nodes.

$$
I^{-}=\left(X^{(t)}, S^{(t)}, C_{1}^{(t)}, D^{(t)}, T_{E C S}^{(t)}, C_{2}^{(t)}, T_{R C S}^{(t)}, R^{(t)}\right)
$$

Because all of these nodes represent quantitative values, the size of each potential is large, and the order of magnitude of the potential product of the joint law of the left interface is

$$
\left|I^{-}\right|=N_{M}^{2} N_{S}^{2} T_{S}^{4}
$$

The classical update of the left interface requires computing $p\left(I^{-(t)}\right) \times p\left(I^{-(t+1)}\right)$. This implies stocking temporarily in the RAM memory a potential with a size at an order of magnitude of $\left(N_{M}^{2} N_{S}^{2} T_{S}^{4}\right)^{2}=N_{M}^{4} N_{S}^{6} T_{S}^{8}$.
So, we need to find a way to avoid stocking the complete left interface. We will propose a specific algorithm adapted to the prognosis DBN. It is a modification of the interface algorithm that aims to perform a slice update without stocking all the

left interface.
The principle is to conduct the forward process by using conditional independence relationships and to compute some specific conditional probability to avoid the computation of a large product. The left interface is split into three groups:

- group 1 : $\left(X^{(t)}, S^{(t)}, C_{1}^{(t)}\right)$
- group 2 : $\left(D^{(t)}, C_{2}^{(t)}, T_{E C S}^{(t)}, T_{R C S}^{(t)}\right)$
- group 3 : $\left(D^{(t)}, R^{(t)}, C_{2}^{(t)}\right)$

The general inference process is detailed in algorithms 3 and 4 in appendix. Its goal is to compute the joint law of the three groups then to update them from slice $t$ to slice $t+1$. It computes the distribution of $R U L^{(t)}$ too. The notation $n(X)$ means that the CPT (the potential) of node X is considered. The $\rightarrow$ symbol means that a marginalization operation or a division by a subset of variables has been used to determine the probability on the right side.
The largest potential now has an order of magnitude of : $T_{S}^{3} N_{S}^{3} N_{S}^{2}$

# Error computation 

As mentioned in the previous section, the error computation is a conditional probability with the form

$$
p\left(X^{(t+h)}, X^{(t+h-1)} \mid D^{(1)}=d_{1}, D^{(2)}=d_{2}, . ., D^{(n)}=d_{n}\right)
$$

In the inference process detailed in algorithm 3 and 4, the conditional information can be directly introduced in the forward step. Because, in this version of the model, the RUL has not been connected yet to the maintenance nodes, the error computation only requires an inference on the set of group 1 nodes. So, algorithm 2 only shows the modified inference update process for group 1

```
Algorithm 2 Inference Modification on group 1 for introducing conditionning with \(D_{t}\)
```

We suppose that we have $P\left(X^{(t)}, S^{(t)}, C_{1}^{(t)} \mid D^{(1)}=d_{1}, . . D^{(t-1)}=d_{t-1}\right)$ and we want to compute $P=$ $p\left(X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)} \mid D^{(1)}=d_{1}, . ., D^{(t)}=d_{t}\right)$

1: $P\left(X^{(t)}, S^{(t)}, C_{1}^{(t)} \mid D^{(1)}=d_{1}, . ., D^{(t-1)}=d_{t-1}\right) \times n\left(X^{(t+1)}\right) \times n\left(S^{(t+1)}\right) \times n\left(C_{1}^{(t+1)}\right)$ $\rightarrow$ $p\left(X^{(t)}, X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)} \mid D^{(1)}=d_{1}, . ., D^{(t-1)}=d_{t-1}\right)$
2: $p\left(X^{(t)}, X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)} \mid D^{(1)}=d_{1}, . . D^{(t-1)}=d_{t-1}\right) \times p\left(D^{(t)} \mid X^{(t)} \mid D^{(1)}, . . D^{(t-1)}\right)$ $\rightarrow$ $p\left(X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)}, D^{(t)} \mid D^{(1)}=d_{1}, . . D^{(t-1)}=d_{t-1}\right)$
Let be $\mathrm{M}(:, ;, ;$,$) the potential for p\left(X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)}, D^{(t)} \mid D^{(1)}=d_{1}, . ., D^{(t-1)}=d_{t-1}\right)$
If the conditioning is $D^{(t)}=d$ then we consider $P=M(:,:, d)$ and $P \rightarrow \frac{P}{p\left(D^{(1)}=d_{t} ; D^{(1)}=d_{1}, . ., D^{(t-1)}=d_{t-1}\right)}$ then we have $P=p\left(X^{(t+1)}, S^{(t+1)}, C_{1}^{(t+1)} \mid D^{(1)}=d_{1}, . ., D^{(t)}=d_{t}\right)$

Algorithms 3 and 4 in use the conditional independence relationships induced by the graph to decrease the complexity of the update part of inference computation. But the main problem in terms of complexity concerns the update of node $T_{E C S}$ and $T_{R C S}$, because of the size of their potentials and the high number of parents. It is the drawback of using a discrete approach. In the analytic approach, analytic expressions are hard to determine, and in most cases, the obtained integrals are not directly computable and need to be approximated using numeric methods, whereas discrete expressions are easy to write and are a sequence of additions and products on potentials but the size of computation is very large because of the high number of numerical values we consider for each node. For this reason, with a computer with 8 Go RAM, $T_{S}$ value is limited to 70 to avoid RAM overloading.

# 4. Application 

## Context

The aim of this section, is to use the prognosis algorithm and its representation to produce some prognostic results, and compute an associated confidence interval. In this section, we work on simulated databases. To show the interest of conditional sojourn time distributions, data are simulated with a mixture of two degradation modes. A four discrete states system is considered. It is supposed to be periodically observable. The sojourn time distributions for each state are a mixture of two Weibull distributions with the following parameters.

- state 1 :
mode $1: W(\alpha=15, \beta=2)$ mode $2: W(\alpha=33, \beta=6)$
- state 2 :
mode $1: W(\alpha=10, \beta=6)$ mode $2: W(\alpha=25, \beta=9)$
- state 3 :
mode $1: W(\alpha=5, \beta=6)$ mode $2: W(\alpha=15, \beta=15)$
Each degradation mode has the same weight $(0.5,0.5)$. From the previous sojourn time distributions, a discrete database was simulated. The interval between two diagnosis was set as 5 time units. The generated database contained 10000 observation sequences with 500 in each mode.


## Learning

About the first state, the parameters of the mixing model were learnt using the EM algorithm (5). Then, the most likely mode was associated with each observation of the database using the a posteriori probabilities. And the CSTD for future states were learnt using the maximum likelihood method on subsets of observations associated with each mode. Because we are in a discrete case, the probability of a sojourn time is its frequency of appearance in the simulated database. The STD are shown in Figure 13.

## Test of the prognosis algorithm

![img-12.jpeg](img-12.jpeg)

Fig. 13. STD learnt with EM algorithm and Max likelihood method (MLM)


Table 1. Prognosis result on Obs 1


Table 2. Prognosis result on Obs 2

Two observation sequences were chosen from the simulated database. The first observation was generated with the first degradation mode (mode 1) and the second one with mode 2. The prognosis algorithm was launched from these observation sequence. It computed a RUL estimation at each available diagnosis. The variant method of the algorithm was used, so the sojourn times are drawn taking the average value of the STDs. The real RUL was deduced from the real failure time that was given because the real hidden sojourn times that had been used to build the observation sequences are known. The RUL estimated with the prognosis algorithm using the conditional STD (Conditional RUL) was computed and compared with the results of the RUL computed by applying the prognosis algorithm with the original GDM (with independent STD). Numerical results produced with the prognosis algorithm are shown in tables 1 and 2. Then, the results are plotted for comparison on figure 14. As expected, the predictions were logically better using the conditional STD, than using the global independent STD. The real active mode was detected after the first transition, so the predictions with CSTD were better. The intermediate sojourn times for each state could then be updated, only when a transition was detected, or due to a sojourn time extension.
![img-13.jpeg](img-13.jpeg)
(a) Prognosis on the first obs sequence
![img-14.jpeg](img-14.jpeg)
(b) Prognosis on the second obs sequence

Fig. 14. Prognosis results on two observation sequences

A confidence interval was computed on the computed RUL at times $10,15,20$ from the first observation sequence using the inference algorithm. The results are shown in Figure 15. The transition at time 15 to state 2 provides new information on sojourn time and the risk of error logically decreases.

To have a more complete view of the behaviour of the prognosis algorithm, the computations are now performed on the
![img-15.jpeg](img-15.jpeg)

Fig. 15. RUL distribution evolution

1000 observation sequences from the simulated database. Figure 16 compares the evolution of the committed error for trajectories generated with mode 1 and those generated with mode 2 .

For mode 1 trajectories, i.e. faster degradation scenarios, we can observe the same global behaviour of the RUL estimation algorithm. Nevertheless, this case also illustrates the drawback of the proposed approach that might be improved in further works. Globally, 34 of the 500 trajectories in mode 1 have at least one sojourn time in the intersection range of two modes, inducing a wrong estimation of the most probable degradation mode, such a way that the adaptation ability of the algorithm, cannot process in these cases and the RUL estimation is absolutely unusable.
![img-16.jpeg](img-16.jpeg)

Fig. 16. Error comparison depending on the mode :

# 4.1. Conclusion and perspective 

In this paper, the formalism of Probabilistic Graphical Models was investigated to perform prognosis computations for systems with discrete and finite states space. This approach is based on a semi-Markovian degradation model called "Graphical duration model" in order to be not dependent of the assumption of geometrical distributed STDs implied by the use

of a classical markovian approach. Then, a prognosis algorithm and its representation as a DBN have been introduced. Based on the current observed state, this algorithm computes the system RUL estimation and updates it each time a new observation of the system state is available. It's main advantage is that the RUL computations are very fast and can be easily implemented in a prognosis software. The representation of this algorithm as a DBN makes possible to compute confidence intervals around the RUL estimations. Because of the complexity of the DBN representing the prognosis algorithm, a specific inference algorithm was proposed requiring the use sojourn time distributions with a size inferior to 70 time units. The quality of the prognosis computation depends on the variance of these sojourn time distributions. One possible way to reduce this variance was to use the notion of Conditional Sojourn Time Distributions that take into account the fact that a failure process can be induced by several degradation dynamics. Through some simulations from a case study, the significant improvement of the RUL estimation by the MGD-CSTD approach was underlined. Nevertheless, some convergence problems can remain, particularly for cases with very fast degradation and for case where real sojourn time are at the intersection of two CSTDs from different modes.
The next step consists in integrating the prognosis module to the global VirmaLab model in order to represent global maintenance strategies based on prognosis. It could again increase the size of the interface of the model and particularly the future connexion between the RUL and the maintenance action nodes. One way we are working on to reduce the exact inference algorithm complexity is to use a sparse structure in the programming to take into account the fact that most of the potentials in the RBD are sparse or semi-sparse. Another way is to slightly modify the prognosis algorithm to delete some dependencies between some variables. For example, if the random samplings are replaced by the choice of the average, the compatibility tests in the algorithm become useless. It leads to the suppression of the arrow between $T_{R C S}^{(t-1)}$ and $T_{E C S}^{(t)}$ that reduce by a factor $T_{S}$ the complexity of the inference process. It is also possible to use approximate inference methods based on Monte-Carlo simulations.
The final VirmalaB model could be used to optimize every kind of maintenance policy and, particularly, the predictive maintenance strategies.

# Acknowledgement 

This work is a part of the project DIADEM ANR -13 -TDMO -04, supported by the French National Agency for Research (ANR), in partnership with University of Technology of Troye, Faiveley Transport, Keolis Rennes and University of technology of Compiegne.

# Appendix 

Algorithm 3 Specific inference algorithm adapted to the prognosis DBN : part 1 : Initialization

## Initial slice $\mathbf{t = 0}$ :

1: $n\left(X^{(0)}\right) \times n\left(S^{(0)}\right) \times n\left(C_{1}^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{X}^{(\mathbf{0})}, \mathbf{S}^{(\mathbf{0})}, \mathbf{C}_{1}^{(\mathbf{0})}\right)$ (group 1)
2: $n\left(X^{(0)}\right) \times n\left(A c t^{(0)}\right) \times n\left(D^{(0)}\right) \times n\left(\delta^{(0)}\right) \rightarrow p\left(X^{(0)}, D^{(0)}, \delta^{(0)}\right)$
3: $p\left(X^{(0)}, S^{(0)}, C_{1}^{(0)}, D^{(0)}, \delta^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{D}^{(\mathbf{0})}, \delta^{(\mathbf{0})}\right)$
4: $p\left(X^{(0)}, S^{(0)}, C_{1}^{(0)}, D^{(0)}, \delta^{(0)}\right) \rightarrow p\left(D^{(0)}, X^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{D}^{(\mathbf{0})} \mid \mathbf{X}^{(\mathbf{0})}\right)$
5: $\mathbf{p}\left(\mathbf{D}^{(\mathbf{0})}, \delta^{(\mathbf{0})}\right) \times n\left(T_{E C S}^{(0)}\right) \times n\left(C_{2}^{(0)}\right) \times n\left(T_{R C S}^{(0)}\right) \rightarrow p\left(D^{(0)}, \delta^{(0)}, T_{E C S}^{(0)}, C_{2}^{(0)}, T_{R C S}^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{D}^{(\mathbf{0})}, \mathbf{T}_{\mathbf{E C S}}^{(\mathbf{0})}, \mathbf{C}_{2}^{(\mathbf{0})}, \mathbf{T}_{\mathbf{R C S}}^{(\mathbf{0})}\right)$ (group 2)
6: $p\left(D^{(0)}, \delta^{(0)}, T_{E C S}^{(0)}, C_{2}^{(0)}, T_{R C S}^{(0)}\right) \rightarrow p\left(D^{(0)}, \delta^{(0)}, C_{2}^{(0)}\right)$
7: $p\left(D^{(0)}, \delta^{(0)}, T_{E C S}^{(0)}, C_{2}^{(0)}, T_{R C S}^{(0)}\right) \rightarrow p\left(T_{R C S}^{(0)} \mid D^{(0)}, \delta^{(0)}, C_{2}^{(0)}\right)$
8: $p\left(D^{(0)}, \delta^{(0)}, C_{2}^{(0)}\right) \times n\left(R^{(0)}\right) \times p\left(T_{R C S}^{(0)} \mid D^{(0)}, \delta^{(0)}, C_{2}^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{D}^{(\mathbf{0})}, \mathbf{C}_{2}^{(\mathbf{0})}, \mathbf{R}^{(\mathbf{0})}\right)$ (group 3) and $p\left(T_{R C S}^{(0)}, R^{(0)}\right)$
9: $p\left(T_{R C S}^{(0)}, R^{(0)}\right) \times n\left(R U L^{(0)}\right) \rightarrow \mathbf{p}\left(\mathbf{R U L}^{(\mathbf{0})}\right)$

Algorithm 4 Specific inference algorithm adapted to the prognosis DBN : part 2 : update from slice t to slice $\mathrm{t}+1$
1: $p\left(X^{(t)}, S^{(t)}, C_{1}^{(t)}\right) \times n\left(X^{(t+1)}\right) \times n\left(S^{(t+1)}\right) \rightarrow p\left(X^{(t)}, C_{1}^{(t)}, X^{(t+1)}, S^{(t+1)}\right)$
2: $p\left(X^{(t)}, C_{1}^{(t)}, X^{(t+1)}, S^{(t+1)}\right) \times n\left(C_{1}^{(t+1)}\right) \rightarrow \mathbf{p}\left(\mathbf{X}^{(\mathbf{t}+\mathbf{1})}, \mathbf{S}^{(\mathbf{t}+\mathbf{1})}, \mathbf{C}_{1}^{(\mathbf{t}+\mathbf{1})}\right)$
(New group 1) and $p\left(X^{(t)}, X^{(t+1)}\right)$
3: $p\left(X^{(t)}, X^{(t+1)}\right) \times \mathbf{p}\left(\mathbf{D}^{(\mathbf{t})} \mid \mathbf{X}^{(\mathbf{t})}\right) \times n\left(A c t^{(t+1)}\right) \times n\left(D^{(t+1)}\right) \rightarrow p\left(D^{(t+1)} \mid D^{(t)}\right)$ and $p\left(D^{(t+1)}, X^{(t+1)}\right)$
4: $X=\mathbf{p}($ group 2$)$
5: $X \times p\left(D^{(t+1)} \mid D^{(t)}\right) \times n\left(\delta^{(t+1)}\right) \rightarrow p\left(X, D^{(t+1)}, \delta^{(t+1)}\right)$
6: $p\left(X, D^{(t+1)}, \delta^{(t+1)}\right) \times n\left(T_{E C S}^{(t+1)}\right) \times n\left(C_{2}^{(t+1)}\right) \rightarrow \mathbf{p}\left(\mathbf{X}, \mathbf{D}^{(\mathbf{t}+\mathbf{1})}, \delta^{(\mathbf{t}+\mathbf{1})}, \mathbf{T}_{\mathbf{E C S}}^{(\mathbf{t}+\mathbf{1})}, \mathbf{C}_{2}^{(\mathbf{t}+\mathbf{1})}\right)$
7: $p\left(X, D^{(t+1)}, \delta^{(t+1)}, T_{E C S}^{(t+1)}, C_{2}^{(t+1)}\right) \rightarrow p\left(T_{R C S}^{(t)}, D^{(t+1)}, \delta^{(t+1)}, T_{E C S}^{(t+1)}, C_{2}^{(t+1)}\right)$
8: $p\left(T_{R C S}^{(t)}, D^{(t+1)}, \delta^{(t+1)}, T_{E C S}^{(t+1)}, C_{2}^{(t+1)}\right) \times n\left(T_{R C S}^{(t+1)}\right) \rightarrow p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}, T_{R C S}^{(t+1)}\right) \quad$ and $\mathbf{p}\left(\mathbf{D}^{(\mathbf{t}+\mathbf{1})}, \mathbf{T}_{\mathbf{E C S}}^{(\mathbf{t}+\mathbf{1})}, \mathbf{C}_{2}^{(\mathbf{t}+\mathbf{1})}, \mathbf{T}_{\mathbf{R C S}}^{(\mathbf{t}+\mathbf{1})}\right)($ New group 2)
9: $p\left(D^{(t+1)}, \delta^{(t+1)}, C_{1}^{(t+1)}, T_{R C S}^{(t+1)}\right) \rightarrow p\left(T_{R C S}^{(t+1)} \mid D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}\right)$
10: $\mathbf{p}\left(\mathbf{X}, \mathbf{D}^{(\mathbf{t}+\mathbf{1})}, \delta^{(\mathbf{t}+\mathbf{1})}, \mathbf{T}_{\mathbf{E C S}}^{(\mathbf{t}+\mathbf{1})}, \mathbf{C}_{2}^{(\mathbf{t}+\mathbf{1})}\right) \rightarrow p\left(D^{(t)}, C_{2}^{(t)}, D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}\right) \rightarrow p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)} \mid D^{(t)}, C_{2}^{(t)}\right)$
11: $\mathbf{Y}=\mathbf{n}($ group 3$)$
12: $Y \times p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)} \mid D^{(t)}, C_{2}^{(t)}\right) \rightarrow p\left(C_{2}^{(t)}, R^{(t)}, D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}\right)$
13: $p\left(C_{2}^{(t)}, R^{(t)}, D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}\right) \times n\left(R^{(t+1)}\right) \rightarrow p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}, R^{(t+1)}\right)$
14: $p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}, R^{(t+1)}\right) \rightarrow \mathbf{p}\left(\mathbf{D}^{(\mathbf{t}+\mathbf{1})}, \mathbf{C}_{2}^{(\mathbf{t}+\mathbf{1})}, \mathbf{R}^{(\mathbf{t}+\mathbf{1})}\right)($ New group 3)
15: $p\left(D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}, R^{(t+1)}\right) \times p\left(T_{R C S}^{(t+1)} \mid D^{(t+1)}, \delta^{(t+1)}, C_{2}^{(t+1)}\right) \rightarrow p\left(T_{R C S}^{(t+1)}, R^{(t+1)}\right)$
16: $p\left(T_{R C S}^{(t+1)}, R^{(t+1)}\right) \times n\left(R U L^{(t+1)} \rightarrow \mathbf{p}\left(\mathbf{R U L}^{(\mathbf{t}+\mathbf{1})}\right)\right.$

# Algorithm 5 Extended version of the prognosis algorithm using CSTD 

## Initialization:

1: $S_{1}^{(0)} \sim \Psi_{1}$
2: for i=2 ... $x_{F}-1$ do
3: $\quad m=\underset{k}{\arg \max }\left(\Psi_{i-1 / k}\left(S_{i-1}^{(0)}\right)\right)$
4: $\quad S_{i}^{(0)} \sim \Psi_{i / m}$
5: end for
6: $m^{(p o)}=m$
7: $R^{(0)}=\sum_{j=x^{(0)}+1}^{x_{F}-1} S_{j}^{(0)}$
8: $T_{E C S}^{(0)}$ initialized by the user depending the past of the component
9: $T_{R C S}^{(0)} \sim \Psi_{x^{(0)} / m}\left(\left[T_{E C S}^{(0)}+1, \alpha^{M A X}\right]-T_{E C S}^{(0)}\right.$
10: $R U L^{(0)}=T_{R C S}^{(0)}+R^{(0)}$

Update: Let $x^{(t_{c o})}$ be a new available diagnosis result :
1: if $\mathbf{x}^{\left(\mathbf{k}_{\mathbf{p o}}\right)}=\mathbf{x}^{\left(\mathbf{k}_{\mathbf{p o}}\right)}$ (case where no transition is observed) then
2: $\quad T_{E C S}^{\left(t_{c o}\right)}=T_{E C S}^{\left(t_{p o}\right)}+\Delta t$
3: $\quad m^{(c o)}=\underset{k}{\arg \max }\left(\Psi_{x^{(c o)} / k}\left(T_{E C S}^{(c o)}\right)\right)$
4: $\quad$ if $\left(T_{R C S}^{\left(t_{p o}\right)}>\Delta t\right)$ (case where the previous estimation is compatible) then
5: $\quad T_{R C S}^{\left(t_{c o}\right)}=T_{R C S}^{\left(t_{p o}\right)}-\Delta t$
6: else
7: $\quad T_{R C S}^{\left(t_{c o}\right)}=\Psi_{x^{\left(t_{c o}\right)} / m^{(c o)}\left[T_{E C S}^{\left(t_{c o}\right)}+1, \alpha^{M A X}\right]-T_{E C S}^{\left(t_{c o}\right)}$
8: end if
9: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}$
10: else if $\left(\mathbf{x}^{\left(\mathbf{k}_{\mathbf{p o}}\right)}-\mathbf{x}^{\left(\mathbf{k}_{\mathbf{p o}}\right)}=\mathbf{1}\right)$ (if a transition is observed) then
11: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}-S_{x}^{\left(0\right)}$

12: if $\left(T_{R C S}^{\left(t_{p o}\right)} \leq \Delta t\right)$ then
13: $\quad T_{E C S}^{\left(t_{c o}\right)}=\Delta t-T_{R C S}^{\left(t_{p o}\right)}$
14: else
15: $\quad T_{E C S}^{\left(t_{c o}\right)}=\Delta t-\Psi_{x^{\left(t_{p o}\right)} / m^{(p o)}\left[T_{E C S}^{\left(t_{p o}\right)}+1, T_{E C S}^{\left(t_{p o}\right)}+\Delta t\right]+T_{E C S}^{\left(t_{p o}\right)}$
16: end if
17:
18: $\quad m^{(c o)}=\underset{k}{\arg \max }\left(\Psi_{x^{(p o)} / k}\left(T_{E C S}^{(p o)}+\Delta t-T_{E C S}^{(c o)}\right)\right)$
19: if $R^{\left(t_{c o}\right)}-R^{\left(t_{p o}\right)}>T_{E C S}^{\left(t_{c o}\right)}$ then
20: $\quad T_{R C S}^{\left(t_{c o}\right)}=R^{\left(t_{c o}\right)}-R^{\left(t_{p o}\right)}-T_{E C S}^{\left(t_{c o}\right)}$
21: else
22: $\quad T_{R C S}^{\left(t_{c o}\right)}=\Psi_{x^{\left(t_{c o}\right)} / m^{(c o)}\left[T_{E C S}^{\left(t_{c o}\right)}+1, \alpha^{M A X}\right]-T_{E C S}^{\left(t_{c o}\right)}$
23: end if
24: end if
25: if $m^{(c o)}=m^{(p o)}$ then
26: $\quad R^{\left(t_{c o}\right)}=R^{\left(t_{p o}\right)}-\sum_{j=x^{\left(t_{p o}\right)}+1}^{x^{\left(t_{c o}\right)}} S_{j}$
27: else
28: $\quad \forall j \in\left[x^{(c o)}+1, x_{F}-1\right], S_{j} \sim \Psi_{j / m^{(c o)}}$
29: $\quad R^{\left(t_{c o}\right)}=\sum_{j=x^{(c o)}+1}^{x_{F}-1} S_{j}$
30: end if
31: $m^{(p o)}=m^{(c o)}$
32: At last $R U L^{\left(t_{c o}\right)}=T_{R C S}^{\left(t_{c o}\right)}+R^{\left(t_{c o}\right)}$
33: $\forall t \in] t_{c o}, t_{f o}\left[\quad R U L^{\left(t_{p o}\right)}=R U L^{\left(t_{c o}\right)}-\left(t-t_{c o}\right)\right.$ where $f o$ is the future observation.