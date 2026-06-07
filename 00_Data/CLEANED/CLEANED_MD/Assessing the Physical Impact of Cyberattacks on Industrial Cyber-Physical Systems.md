# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Huang, Kaixing, Zhou, Chunjie, Tian, Glen, Yang, Shuang-Hua, \& Qin, Yuanqing
(2018)

Assessing the physical impact of cyber-attacks on industrial cyber-physical systems.
IEEE Transactions on Industrial Electronics, 65(10), pp. 8153-8162.
This file was downloaded from: https://eprints.qut.edu.au/223506/

## (c) Consult author(s) regarding copyright matters

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1109/TIE.2018.2798605

# Assessing the Physical Impact of Cyber-Attacks on Industrial Cyber-Physical Systems 

Kexing Huang, Chunjie Zhou, Yu-Chu Tian, Shuanghua Yang, Yuanqing


#### Abstract

Industrial Cyber-Physical systems (ICPSs) are widely applied in critical infrastructures such as chemical plants, water distribution networks, and power grid. However, they face various cyber-attacks, which may cause physical damage to these industrial facilities. Therefore, ensuring the security of ICPSs is of paramount importance. For this purpose, a new risk assessment method is presented in this paper to quantify the impact of cyberattacks on the physical system of ICPSs. It helps carry out appropriate attack mitigation measures. The method uses a Bayesian network to model the attack propagation process and infers the probabilities of sensors and actuators to be compromised. These probabilities are fed into a stochastic hybrid system (SHS) model to predict the evolution of the physical process being controlled. Then, the security risk is quantified by evaluating the system availability with the SHS model. The effectiveness of the proposed method is demonstrated with a case study on a hardware-in-the-loop simulation testbed.


Index Terms-Industrial Cyber-Physical system, security, risk assessment, Bayesian, stochastic hybrid system.

## I. INTRODUCTION

CYBER-Physical systems (CPSs) are a type of systems in which information and communication technologies are tightly integrated with physical processes. Industrial CPSs (ICPSs) [1] are CPSs in industrial environments. They are widely applied in critical infrastructures such as modern chemical plants, water distribution networks, and smart grid. Hiowever, ICPSs are vulnerable to external attacks due to the tight integration of cyber and physical parts [2]. Therefore, ensuring the security of ICPSs is an issue of great concern.

Security risk assessment (SRA) is a process to identify possible security threats and evaluate potential loss typically mesured by dollar values. It is used to guide attack mitigation actioons, and thus is critical to ICPS protection [3]. In general, SRA is either qualitative or quantitative. Quantitative methods are preferred here because they provide a more accurate reflection of system status, thus facilitating better allocation of safeguard resources. While many SRA methods have been proposed for ICPSs, most of them are directly adapted from IT domains. Focusing more on information security risk in the cyber layer, they neglect the risk of cyber-attacks on the physical system, referred to as cyber-to-physical (C2P) [4] risk in this paper. As cyber-attacks may result in severe safety incidents in ICPSs [2], assessing the C2P risk is highly demanded [5].

Efforts have been recently made to SRA in ICPSs with awareness of the physical world. For example, a cyber-security risk evaluation model is proposed for nuclear control systems [6]. It uses Bayesian networks (BNs) and event trees to quantify cyber-security risk and predict the malfunction
probability of the reactor protection system. In [7], a multimodel framework is formed from a combination of BNs, fault trees and event trees. It is used to compute the probability that a hazardous incident happens and evaluate the monetary loss caused by these incidents. The physical impact of false sequential logic attack on ICPSs is investigated in [8]. This type of attacks may cause equipment damage or facility destruction. A risk management framework is presented in [3] for ICPSs. It continuously monitors the system, quantifies the impact of cyber attacks, and carries out risk treatment operations.

In spite of these efforts, SRA in ICPSs is still challenging. Most previous studies on SRA in ICPSs have made simplified assumptions about the physical system. They have only focused on evaluation of cyber-layer network security [6], [7], [9]. On the other hand, the efforts that have addressed the physical layer generally abstract ICPSs as traditional feedback control systems and ignore cyber-physical interactions [3], [8]. Moreover, existing approaches do not support real-time evaluation of the impact of cyber-attacks on ICPSs.

This paper presents a new SRA method for dynamic evaluation of C2P risk in ICPSs. The method uses Bayesian network (BN) to model the attack propagation process in the cyber layer. This enables to estimate the probability of the components connecting with the physical process to be compromised. Employing these probabilities, a stochastic hybrid system (SHS) model is implemented to predict the evolution of the physical process. It is further used to evaluate its availability by computing the Mean-Time-To-Shut-Down (MTTSD). Then, the C2P risk is quantified based on the MTTSD metric. The contributions of this paper include:

1) BNs are integrated with an SHS model to analyze crossdomain attacks in ICPSs;
2) An unbiased minimum-variance state estimator is designed for estimation of the states of ICPS physical process under attack; and
3) A new security metric, MTTSD, is introduced to quantify the C2P risk in ICPSs.

This paper is organized as follows. Section II briefly introduces BNs and SHS modelling. Section III presents our risk assessment framework. Section IV describes BN-based attack modelling. Our C2P risk assessment method is presented in Section V presents the C2P risk assessment method. Experiments are carried out in Section VI to demonstrate the effectiveness of the presented method. Finally, Section VII concludes the paper.

## II. Preliminaries

## A. Bayesian Network

A BN is a directed acyclic graph, in which nodes represent variables and directed arcs imply the conditional dependencies between these variables [10]. The state of each node in a BN is only dependent on its parent nodes. It is described by a conditional probability table (CPT). Given a BN with a set of binary variables $\mathbf{Y}=\left\{Y_{1}, Y_{2}, \ldots, Y_{N}\right\}$, the joint probability distribution of $\mathbf{Y}$ is

$$
p(\mathbf{Y})=P\left(Y_{1}, Y_{2}, \ldots, Y_{N}\right)=\prod_{i=1}^{N} p\left(Y_{i} \mid \mathbf{p a}_{i}\right)
$$

where $\mathbf{p a}_{i}$ is the parent set of variable $Y_{i}$.
Quantitative risk assessment can be conducted through probabilistic risk analysis. BN is a useful probabilistic tool for risk assessment. When applied to SRA in computer networks, it is able to reason the causal dependencies between network states and, more importantly, calculate the occurrence probabilities of attacks. With these probabilities, the security risk $\mathcal{R}$ can be quantified by the following equation [11]:

$$
\mathcal{R}=\sum_{i=1}^{M} A_{i}^{V} \times p\left(A_{i}\right)
$$

where $\mathbf{A}=\left\{A_{1}, A_{2}, \ldots, A_{M}\right\}$ is the set of system assets (in terms of information, property, people, environment, etc.), $A_{i}^{V}$ is the value of $A_{i}$, and $p\left(A_{i}\right)$ is the probability of $A_{i}$ to be compromised.

## B. Stochastic Hybrid System Model

An SHS refers to a stochastic process defined on a hybrid state space involving both continuous and discrete states [12]. The continuous states of SHSs evolve continuously, typically according to a differential equation indexed by the discrete state or mode. The switching between the discrete states is triggered by stochastic events. An SHS is represented as

$$
\mathcal{S}=<\mathcal{Q}, \mathcal{X}, \text { Init }, \mathcal{F}, \mathcal{E}, \phi, \mu>
$$

where

- $\mathcal{Q}=\left\{q_{1}, q_{2}, \ldots\right\}$ is a finite set of discrete states.
- $\mathcal{X} \in \mathbb{R}^{n}$ is a set of continuous states.
- Init is the initial system states.
- $\mathcal{F}(\cdot, \cdot): \mathcal{Q} \times \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ is a family of vector fields that characterizes the dynamics of $\mathcal{X}$ in mode $q \in \mathcal{Q}$.
- $\mathcal{E}=\left\{e_{1}, e_{2}, \ldots\right\}$ is a finite set of stochastic events.
- $\phi=\left\{\phi_{q}^{e}: \mathcal{Q} \times \mathbb{R}^{n} \rightarrow \mathcal{Q} \times \mathbb{R}^{n}\right\}$ is a family of reset maps that describes how the transition changes system states.
- $\mu=\left\{\mu_{q}^{e}: \mathcal{Q} \times \mathbb{R}^{n} \rightarrow[0,+\infty)\right\}$ is a family of transitiontime distributions that defines when transitions happen.
The physical processes of an ICPS typically have continuous dynamics. An attack to the ICPS may cause the dynamics of the physical processes to change. Different attack scenarios drive the ICPS into different operation conditions. Hence, an ICPS under attack can be naturally considered as an SHS. This paper uses SHS models to characterize the coupling between the continuous system dynamics and discrete attack behaviours in ICPSs.


## III. PROPOSED RISK ASSESSMENT FRAMEWORK

This paper presents a concise risk assessment framework. As shown in Fig. 1, it is designed for assessing the physical impact caused by cyber-attacks on ICPSs. The framework uses a BN to model the dependencies between cyber components, system vulnerabilities, attack path and the likelihood of successful attacks. With the BN model, as well as realtime intrusion detection evidences [13], the probabilities of compromise for the sensors and actuators can be inferred. Using these probabilities as inputs, an SHS model is employed to predict the evolution of the physical process. Then, it further assesses the C2P risk of the ICPSs.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Proposed risk assessment framework.
In Fig. 1, $q_{0}$ represents the normal operation mode of the physical system. When a cyber-attack is launched, $q_{0}$ may transit into another hybrid state. In each hybrid state other than $q_{0}$, the MTTSD of the physical process is computed. It is used to quantify the immediate C2P risk.

## IV. Attack Propagation Modelling

This section presents the details of our BN modelling of the attack propagation process in the cyber layer of ICPSs.

## A. Structure of our Bayesian Network

In general, an attacker keeps exploiting system vulnerabilities for privilege escalation until the target is reached [14]. It is assumed that the goal of cyber-attacks against ICPSs is to disrupt the physical system by maliciously manipulating sensors and actuators [15], [16]. Therefore, the BN structure can be constructed with three types of nodes: VULnerability node, PRIvilege node and TARget node. The VUL nodes represents the vulnerabilities of cyber components that can be exploited by attackers. The PRI node represents the host privileges which attackers require for further operations. The TAR node describes the attacks on sensors or actuators for aimed damage to the physical system.

Moreover, it is assumed that a motivated attacker, who wants to penetrate deep into the ICPS network and manipulate the sensors or actuators, will not waste any time with unnecessary actions [17]. Therefore, when building the BN, we only consider the hosts and the associated vulnerabilities that can help the attacker move forward towards the target.

## B. Conditional Probability Tables

The tractability of CPT construction is generally referred to as the bottleneck of BN modeling. This is due to the large number of CPT parameters and complex dependencies between BN nodes [18]. The primary solution to this problem is the canonical gate, which reduces the number of CPT parameters significantly from the independence of causal influence assumption [18]. This paper adopts the logical $A N D$ gate and logic $O R$ gate [14] to alleviate the difficulty of specifying CPT parameters. A logic $A N D$ assumes that all the causes of $Y_{i}$ must be met to realize $Y_{i}$. This is expressed as:

$$
p\left(Y_{i} \mid \mathbf{p a}_{i}\right)=\left\{\begin{array}{lr}
0, & \exists Y_{j} \in \mathbf{p a}_{i} \mid Y_{j}=0 \\
\prod_{j: Y_{j} \in \mathbf{p a}_{i}} p\left(Y_{j}\right), & \text { otherwise. }
\end{array}\right.
$$

A logic $O R$ only requires that at least one node in $\mathbf{p a}_{i}$ be satisfied. It follows that
$p\left(Y_{i} \mid \mathbf{p a}_{i}\right)=\left\{\begin{array}{ll}0, & \forall Y_{j} \in \mathbf{p a}_{i} \mid Y_{j}=0, \\ 1-\prod_{j: Y_{j} \in \mathbf{p a}_{i}}\left(1-p\left(Y_{j}\right)\right), & \text { otherwise. }\end{array}\right.$
Though the logic gates offer great help on building the CPTs, the probability of success that the attacker exploits a vulnerability has to be estimated. After that, all the CPT parameters can be computed using (4) and(5). In order to estimate the probability of a successful exploitation, the metrics provided by the Common Vulnerability Scoring System (CVSS) [19] are used in this paper.

CVSS has three groups of metrics: base, temporal and environmental. Specifically, only the exploitability subscore defined in the base group is considered since it evaluates the difficulty of exploiting a vulnerability. The exploitability subscore consists of access vector ( $S_{-} A V$ ), access complexity ( $S_{-} A C$ ) and authentication ( $S_{-} A U$ ). All the scores of $S_{-} A V, S_{-} A C$ and $S_{-} A U$ can be obtained from public vulnerability databases. Then, the probability of successful exploitation on a vulnerability is computed from the following equation [14]:

$$
p=2 \times S_{-} A V \times S_{-} A C \times S_{-} A U
$$

## C. Attack Prediction

After the BN model is developed, the conditional probabilities of the TAR nodes are inferred based on real-time attack information, which is usually provided by intrusion detection systems. A large number of intrusion detection approaches have been proposed for ICPSs, as summarized in a recent survey paper [13]. Given a set of attack evidence $\mathbf{E}=\left\{E_{1}, E_{2}, \ldots\right\}$, each $E_{i}$ indicates that the corresponding $i$ th BN node has been compromised by the attacker. Then, the

Bayes theorem is used to update the posterior probability of the TAR nodes $\mathbf{T}=\left\{T_{1}, T_{2}, \ldots\right\}$ :

$$
p\left(T_{i} \mid \mathbf{E}\right)=\frac{p\left(\mathbf{E} \mid T_{i}\right) \times p\left(T_{i}\right)}{p(\mathbf{E})}
$$

where $p\left(T_{i} \mid \mathbf{E}\right)$ is the conditional probability of $T_{i}$ given $\mathbf{E}$, and $p\left(\mathbf{E} \mid T_{i}\right)$ is the conditional probability of $\mathbf{E}$ given $T_{i}$. Also, with the inference capability of BNs, all the probabilities of each system asset to be compromised can be computed. Then, the cyber-security risk is quantified using (2), which is the most common SRA method for ICPSs in the literature.

## V. PHYSICAL IMPACT ASSESSMENT

This section employs an SHS model to analyze the system dynamics of ICPSs under attack. It further uses the SHS model to quantify the C2P risk by evaluating the system availability.

## A. System Description

The physical process being controlled is modelled as a multi-variable discrete-time linear time-invariant (LTI) system:

$$
\begin{aligned}
& \mathbf{x}_{k+1}=A \mathbf{x}_{k}+B \mathbf{u}_{k}+\mathbf{w}_{k} \\
& \mathbf{y}_{k}=C \mathbf{x}_{k}+\mathbf{v}_{k}
\end{aligned}
$$

where $\mathbf{x}_{k} \in \mathbb{R}^{n}$ represents current system states; $\mathbf{u}_{k} \in \mathbb{R}^{m}$ means control actions; $\mathbf{y}_{k} \in \mathbb{R}^{l}$ denotes sensor readings; $\mathbf{w}_{k} \in$ $\mathbb{R}^{n}$ and $\mathbf{v}_{k} \in \mathbb{R}^{l}$ are uncorrelated zero-mean Gaussian noises with known covariance matrices $W_{k}$ and $V_{k}$, respectively; and $A, B$ and $C$ are matrices representing the dynamics of the physical process.

## B. Stochastic Hybrid System Model

The attacker who aims to disrupt the physical process of an ICPS needs to manipulate the sensors or actuators to achieve aimed malicious goals. Thus, the physical system under attack can be described as

$$
\begin{aligned}
& \mathbf{x}_{k+1}=A \mathbf{x}_{k}+B\left(\mathbf{u}_{k}+\mathbf{d}_{k}^{u}\right)+\mathbf{w}_{k} \\
& \mathbf{y}_{k}=C \mathbf{x}_{k}+\mathbf{d}_{k}^{y}+\mathbf{v}_{k}
\end{aligned}
$$

where $\mathbf{d}_{k}^{u}$ and $\mathbf{d}_{k}^{y}$ are attacks on the actuators and sensors, respectively.

Without loss of generality, define an attack scenario in the physical layer of ICPSs as an running state of all sensors and actuators. As each sensor or actuator has two possible states: normal or compromised, the total number of attack scenarios is

$$
Q_{0}=\sum_{i=1}^{h} A_{h}^{i}=\sum_{i=1}^{h} \frac{(h)!}{(h-i)!}
$$

where $h=m+l$, and $h$ ! represents the factorial of $h$.
Let us denote each attack scenario as a discrete mode. Then, the physical process under attack can be characterized by an SHS model, and (9) changes to

$$
\begin{aligned}
& \mathbf{x}_{k+1}=A \mathbf{x}_{k}+B\left(\mathbf{u}_{k}+\mathbf{d}_{k}^{u, q_{k}}\right)+\mathbf{w}_{k} \\
& \mathbf{y}_{k}=C \mathbf{x}_{k}+\mathbf{d}_{k}^{y, q_{k}}+\mathbf{v}_{k}
\end{aligned}
$$

where $q_{k} \in\left\{q^{1}, q^{2}, \ldots, q^{Q}\right\}$ is current mode, and $\mathbf{d}_{k}^{u, q_{k}}, \mathbf{d}_{k}^{y, q_{k}}$ are additive attack signals on the actuators and sensors in mode

$q_{k}$, respectively. $Q$ is the total number of discrete modes, including both the normal mode and attack modes. Thus, $Q=\left(Q_{0}+1\right)$.

As explained in Section IV, a BN model is employed to predict the attack behaviours. Assume that at each time instant $k$, the current discrete mode is $q_{k}=q^{i}$. With the BN model, we can predict the next mode from a mode transition probability vector $\pi_{k}^{i}=\left[\pi_{k}^{i 1}, \pi_{k}^{i 2}, \ldots, \pi_{k}^{(Q)}\right]$, where $\pi_{k}^{i j}=p\left(q_{k+1}=q^{j} \mid q_{k}=q^{i}, k\right)$ and $\sum_{j=1}^{Q} \pi_{k}^{i j}=1$.

It is worth mentioning that the attack scenarios discussed in this section only take the sensors and actuators into consideration. The components in the cyber layer are not inckluded. Thus, the transition probability vector will change when more cyber components are compromised. Consequently, we need to generate new transition probability matrix, denoted as $\pi_{k}$, once the intrusion detection system raises new alarms.

Then, we need to characterize the times when discrete mode transition happens. As we have associated each discrete mode with an attack scenario in terms of the sensors and actuators, the discrete mode transition time is determined by the time interval between two consecutive attacks against the physical system of an ICPS, namely the sojourn time in a discrete mode. However, the attack intervals are unknown. It is suggested in [20] that the time needed for a successful vulnerability compromise follow an exponential distribution with a parameter $1 / \lambda$.

## C. State Estimation

In order to assess the availability of the physical system of an ICPS under attack, the system states need to be estimated in each discrete mode. Then, current operation condition is evaluated. As the compromised sensors or actuators may have random behaviours, i.e., attack signals are non-Gaussian and have unknown statistics, for each discrete mode, a robust state estimator needs to be designed whose estimation error is decoupled from attack signals.

Because $\mathbf{x}_{k}$ has arbitrary ordering, the state equation in(11) can be represented as follows when the system is within mode $q^{i}$ where part of the actuators are compromised

$$
\begin{aligned}
\mathbf{x}_{k+1} & =A^{q^{i}} \mathbf{x}_{k}+B^{q^{i}}\left(\mathbf{u}_{k}+\left[\begin{array}{ll}
\mathbf{0} & \mathbf{0} \\
\mathbf{0} & I
\end{array}\right]\left[\begin{array}{c}
\mathbf{0} \\
\mathbf{u}_{k}^{q^{i}}
\end{array}\right]\right)+\mathbf{w}_{k} \\
& =A^{q^{i}} \mathbf{x}_{k}+B^{q^{i}} \mathbf{u}_{k}+B_{a}^{q^{i}} \mathbf{u}_{k}^{q^{i}}+\mathbf{w}_{k}
\end{aligned}
$$

where $B_{a}^{q^{i}}=B^{q^{i}}\left[\begin{array}{l}\mathbf{0} \\ I\end{array}\right], A^{q^{i}}$ and $B^{q^{i}}$ are the reordered $A$ and $B$ in mode $q^{i}$, respectively, and $\mathbf{u}_{k}^{q^{i}} \in \mathbb{R}^{z_{i}}$ denotes the injected actuator signals in mode $q^{i}$.

When sensor attacks happen, part of the sensor readings are fake. So, we can discard these corrupted variables in the output equation of (11). Let $\mathbf{y}^{q^{i}}$ denote the uncorrupted sensor measurement variables in mode $q_{i}$. Then, we have

$$
\mathbf{y}_{k}^{q^{i}}=C^{q^{i}} \mathbf{x}_{k}+\mathbf{v}_{k}^{q^{i}}
$$

where $\mathbf{v}_{k}^{q^{i}}$ is the reduced measurement noise in mode $q^{i}$.
Accordingly, the SHS model changes to

$$
\begin{aligned}
\mathbf{x}_{k+1} & =A^{q^{i}} \mathbf{x}_{k}+B^{q^{i}} \mathbf{u}_{k}+B_{a}^{q^{i}} \mathbf{u}_{k}^{q^{i}}+\mathbf{w}_{k} \\
\mathbf{y}_{k}^{q^{i}} & =C^{q^{i}} \mathbf{x}_{k}+\mathbf{v}_{k}^{q^{i}}
\end{aligned}
$$

Before an individual observer is designed for each discrete mode, we need to make sure that system (14) is observable when $B_{a}^{q^{i}}=0$. This is satisfied by

$$
\operatorname{rank}\left(\left[\begin{array}{c}
C^{q^{i}} \\
C^{q^{i}} A^{q^{i}} \\
\vdots \\
C^{q^{i}}\left(A^{q^{i}}\right)^{n-1}
\end{array}\right]\right)=n
$$

In order to design a robust unbiased minimum-variance state estimator for the system formulated in (14), which is a discrete-time LTI system with unknown inputs, the filter proposed in [21] is adopted in this paper. It has the following form (superscript $q^{i}$ is omitted for better readability)

$$
\begin{aligned}
\hat{\mathbf{x}}_{k+1}= & A \hat{\mathbf{x}}_{k}+B \mathbf{u}_{k}+ \\
& L_{k+1}\left[\mathbf{y}_{k+1}-C A \hat{\mathbf{x}}_{k}-C B \mathbf{u}_{k}\right]
\end{aligned}
$$

where $\hat{\mathbf{x}}_{k}$ is the estimate of $\mathbf{x}_{k}$ and $L_{k+1}$ is a gain matrix parameter to be designed. The estimator is unbiased if

$$
\mathbb{E}\left(\hat{\mathbf{x}}_{k}-\mathbf{x}_{k}\right)=0
$$

Substituting (14a) and (16) into(17) gives

$$
\begin{aligned}
& \mathbb{E}\left[\left(A-L_{k+1} C A\right)\left(\hat{\mathbf{x}}_{k}-\mathbf{x}_{k}\right)+\left(L_{k+1} C B_{a}-B_{a}\right) \mathbf{u}_{k}^{a}\right. \\
& \left.+\left(L_{k+1} C-I\right) W_{k}+L_{k+1} V_{k+1}\right]=0
\end{aligned}
$$

For the condition in (18) to hold regardless of the actuator attack signals, $L_{k+1}$ should satisfy

$$
L_{k+1} C B_{a}-B_{a}=0
$$

Equation (19) has a solution if

$$
\operatorname{rank}\left(C B_{a}\right)=\operatorname{rank}\left(B_{a}\right)=z_{i}
$$

The solution to (19) is given by

$$
L_{k+1}=B_{a}\left(C B_{a}\right)^{+}+\Gamma_{k+1} \Psi
$$

where $\left(C B_{a}\right)^{+}=\left[\left(C B_{a}\right)^{T} C B_{a}\right]\left(C B_{a}\right)^{T}$ is the MoorePenrose psudo-inverse of $C B_{a}, \Psi=\Upsilon\left(I-C B_{a}\left(C B_{a}\right)^{+}\right)$, and $\Upsilon$ is any full row rank matrix with proper size. $\Gamma_{k+1}$ is a design parameter.

For minimum-variance estimation, we need to find $L_{k+1}$ that minimizes the trace of estimation error $P_{k+1}$ under constraint (19). $P_{k+1}$ can be written as

$$
\begin{aligned}
P_{k+1}= & \mathbb{E}\left[\left(\hat{\mathbf{x}}_{k+1}-\mathbf{x}_{k+1}\right)\left(\hat{\mathbf{x}}_{k+1}-\mathbf{x}_{k+1}\right)^{T}\right] \\
= & \left(I-L_{k+1} C\right)\left(A P_{k} A^{T}+W_{k}\right) \\
& \left(I-L_{k+1} C\right)^{T}+L_{k+1} V_{k+1} L_{k+1}^{T}
\end{aligned}
$$

Let

$$
\begin{aligned}
& P_{k+1 \mid k}=A P_{k} A^{T}+W_{k} \\
& K_{k+1}=C P_{k+1 \mid k} C^{T}+V_{k}
\end{aligned}
$$

Then, (22) is simplified to

$$
\begin{aligned}
P_{k+1}= & L_{k+1} K_{k+1} L_{k+1}^{T}-P_{k+1 \mid k} C^{T} L_{k+1}^{T} \\
& -L_{k+1} C P_{k+1 \mid k}+P_{k+1 \mid k}
\end{aligned}
$$

Substituting (21) into(24) and letting the derivative of the trace of $P_{k+1}$ equal to zero give

$$
\frac{\partial\left(\operatorname{tr}\left(P_{k+1}\right)\right)}{\partial L_{k+1}}=0
$$

The result of (25) is given by

$$
\Gamma_{k+1}=\begin{aligned}
& {\left[P_{k+1 \mid k}-C^{T} \Psi^{T}-B_{a}\left(C B_{a}\right)^{+} K_{k+1} \Psi^{T}\right] } \\
& {\left[\Psi K_{k+1} \Psi^{T}\right]^{-1}}
\end{aligned}
$$

Substituting (26) into (16) gives $L_{k+1}$ as

$$
\begin{aligned}
L_{k+1}= & B_{a}\left(C B_{a}\right)^{+}+\left[P_{k+1 \mid k}-C^{T} \Psi^{T}\right. \\
& \left.-B_{a}\left(C B_{a}\right)^{+} K_{k+1} \Psi^{T}\right]\left[\Psi K_{k+1} \Psi^{T}\right]^{-1} \Psi
\end{aligned}
$$

## D. C2P Risk Quantification

This section quantifies the physical impact of cyber-attacks, namely the aforementioned C2P risk $\mathcal{R}$. Equation (2) is the most general form for cyber layer security risk quantification in ICPSs. On the other hand, when evaluating the risk of physical layer, some metrics related to reliability, availability or dependability are widely used, e.g., the Mean-Time-ToFailure and Time-To-Shut-Down (TTSD). Since C2P risk is the operational risk caused by cyber-security issues, these two metrics should be integrated. In [22], an equation $\mathcal{R}=$ $P / T T S D$ is proposed to quantify C 2 P risk, where $P$ is the occurrence probability of attacks. However, this method is too simple to take into account consecutive attacksas well as the case that only performance degradation is resulted. Motivated by this preliminary work in C2P risk quantification, this paper extends the availability metric TTSD into MTTSD. MTTSD describes the expected amount of time that the attacker needs to drive the physical process into an undesirable state.

The MTTSD does not mean that the whole physical process will definitely shut down when the ICPS is under attack. The attacker may drive the physical process into a state with failures of some devices, defected output products or the degraded real-time performance. In these cases, MTTSD is still applicable as long as attacks drive the system into an undesired state and the administrators can distinguish these different states using the process variables $\mathrm{x}_{k}$.

Suppose the system is in mode $q^{i}$. The corrupted actuator signals are $\mathbf{u}^{a, q^{i}}=\left\{u_{1}^{a, q^{i}}, u_{2}^{a, q^{i}}, \ldots, u_{z_{i}}^{a, q^{i}}\right\}$. With the proposed state estimator, the TTSD can be obtained at time $k$ for mode $q^{i}$, denoted as $\mathcal{T}_{k}^{q^{i}}$, by means of numerical simulation. Within the time span $\left[k, k+\mathcal{T}_{k}^{q^{i}}\right]$, the attacker may launch another attack where the time interval between two consecutive attacks is described by an exponential distribution. Therefore, the effect of discrete mode switching on the TTSD should be taken into consideration. Suppose that the system enters mode $q^{i}$ at time $T_{i}$, and the next discrete mode is $q^{j}$. Then, the discrete mode transition probability vector $\pi_{k}^{i}=\left[\pi_{k}^{i 1}, \pi_{k}^{i 2}, \ldots, \pi_{k}^{i Q}\right]$ is the $i$ th row of $\pi_{k}$. When $\mathcal{T}_{k}^{q^{i}}<\left(T_{i}+\lambda-k\right)$, it means that a mode switching is expected to happen before the system enters an undesirable state. In this case, we need to predict the next discrete mode with $\pi_{k}^{i}$, compute the TTSD for each predicted mode, and then calculate the weighted sum as the current MTTSD. When $\mathcal{T}_{k}^{q^{i}}>\left(T_{i}+\lambda-k\right)$, which means that the physical process is expected to enter an undesirable
or failure state before next attack has taken place, the MTTSD is set to $\mathcal{T}_{k}^{q^{i}}$. Accordingly, MTTSD is given by

$$
\overline{\mathcal{T}_{k}^{q^{i}}}=\left\{\begin{array}{lr}
\mathcal{T}_{k}^{q^{i}}, & \text { if } T_{i}+\lambda-k>\mathcal{T}_{k}^{q^{i}} \\
T_{i}+\lambda-k+\sum_{m=1}^{Q} \pi_{k}^{i m} \mathcal{T}_{T_{i}+\lambda}^{q^{m}}, & \text { else }
\end{array}\right.
$$

After $\overline{\mathcal{T}_{k}^{q^{i}}}$ is computed, the following equation is proposed to quantify the real-time C 2 P risk

$$
\mathcal{R}_{k}=V_{T} \frac{\mathcal{T}_{\max }-\overline{\mathcal{T}_{k}^{q^{i}}}}{\mathcal{T}_{\max }}
$$

where $V_{T}$ is the monetary loss caused by operation state switching in the ICPS (e.g., abrupt shutdown, and system degradation), and $\mathcal{T}_{\text {max }}$ is the TTSD of the physical process when it is running without any attacks. Consequently, the shorter the MTTSD, the higher the C2P risk of the system.

## VI. CASE STUDIES

In order to evaluate the performance of our risk assessment method, this section implements and tests the proposed method on a hardware-in-the-loop (HIL) simulation testbed.

## A. Experiment Setup

A boiling water power plant (BWPP) described in [23] is investigated as an ICPS. Fig. 2 depicts the architecture of our HIL simulation testbed. The HIL testbed consists of two parts: the cyber part and the physical part. The physical part is simulated on an individual simulation host (SH). It includes the BWPP and sensors and actuators. Apart from the physical system, all other devices are real ones. This HIL testbed has the following components: 1) an administrator host (AH) and two PCs (C1 and C2) in the corporate network; 2) a human-machine-interface (HM) and a data server (DS) in the supervisory network; 3) three embedded controllers (N1, N2, and N3) in the control network; and 4) a water valve (WV), a fuel valve (FV), a steam valve (SV), two pressure sensors (P1 and P2), two water level sensors (L1 and L2) and a sensor for reading the generated electricity (GT) in the field area.

The corporate network of the ICPS is directly connected with the Internet. The supervisory network is isolated from the the corporate network by a firewall (F1) and only AH has the privilege to access the supervisory network. Another firewall (F2) exists between the supervisory network and the control network. Both HM and DS can cross F2 to access the controllers. The devices in the supervisory layer communicate with each other through industrial Ethernet using the Modbus TCP protocol. The gateway (GW) between the supervisory network and the control network is responsible for protocol conversion. The controllers communicate with the SH via an agent node (AN), which is attached to the CAN bus of the control network. As shown in Fig. 2, the dashed lines represent the connections between the controllers and the sensors and actuators. All these connections are actually implemented by software on the SH.

There are three states to be controlled in the BWPP: drum pressure $x_{1}\left(k g / \mathrm{cm}^{2}\right)$, electric output $x_{2}(M W)$ and fluid

![img-1.jpeg](img-1.jpeg)

Fig. 2. Structure of the boiling water power plant.
density $x_{3}\left(\mathrm{~kg} / \mathrm{cm}^{3}\right)$. Let $u_{1}, u_{2}, u_{3}$ denote fuel, steam and water valve positions, respectively. Use $y_{1}, y_{2}, y_{3}, y_{4}$, and $y_{5}$ to represent the sensor readings of P1, P2, GT, L1 and L2, respectively. When the system is in the steady state, $\bar{u}_{1}=0.34$, $\bar{u}_{2}=0.69, \bar{u}_{3}=0.433, \bar{x}_{1}=108, \bar{x}_{2}=66.65$ and $\bar{x}_{3}=428$. The scheduling period is 100 ms . The possible range for the valves is $[0,1]$. When the drum pressure $x_{1}>250 \mathrm{~kg} / \mathrm{cm}^{2}$, the tank will explode immediately. The process dynamics is given by

$$
\begin{gathered}
A=\left[\begin{array}{ccc}
0.9998 & 0 & 0 \\
0.0069 & 0.9900 & 0 \\
-0.0007 & 0 & 1
\end{array}\right] \\
B=\left[\begin{array}{ccc}
0.0900 & -0.0349 & -0.0150 \\
0.0003 & 1.4083 & -0.0001 \\
0 & -0.1398 & 0.1659
\end{array}\right] \\
C=\left[\begin{array}{ccc}
1 & 0 & 0 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
0.0063 & 0 & 0.0047 \\
0.0063 & 0 & 0.0047
\end{array}\right] \\
\mathbf{w}_{k} \sim \mathcal{N}\left(0,0.05^{2}\right), \mathbf{v}_{k} \sim \mathcal{N}\left(0,0.05^{2}\right)
\end{gathered}
$$

The controller has a proportional-integral control strategy:

$$
\begin{aligned}
& u_{1, k+1}=0.0485 \Delta \hat{x}_{1, k}+0.0012 \sum \Delta \hat{x}_{1}+ \\
& 1.2091 \Delta \hat{x}_{3, k}+0.0486 \sum \Delta \hat{x}_{3}+\overline{u_{1}} \\
& u_{2, k+1}=0.0197 \Delta \hat{x}_{2, k}+0.0045 \sum \Delta \hat{x}_{2}+\overline{u_{2}} \\
& u_{3, k+1}=7.2548 \Delta \hat{x}_{3, k}+0.2914 \sum \Delta \hat{x}_{3}+\overline{u_{3}}
\end{aligned}
$$

where $\Delta \hat{x}_{1, k}=\overline{x_{1}}-\hat{x}_{1, k}$ and $\sum \Delta \hat{x}_{1}=\sum_{i=1}^{k} \Delta \hat{x}_{1, k}$.

The BWPP ICPS has some vulnerabilities, which are summarized in Table I. In Table I, the "Exploitability" column is the vulnerability exploitation probability computed from (6). The parameter $\lambda$ column is the expected amount of time that the attacker needs to exploit the vulnerability [20]. A typical value of $\lambda$ is several minutes. The database of Common Vulnerabilities and Exposures (CVE) provides detailed information about all these vulnerabilities except the vulnerability $\mathcal{V}_{6} . \mathcal{V}_{6}$ is a Modbus vulnerability that Modbus protocol lacks authentication and encryption mechanisms. It allows attackers to easily send forged Modbus messages. This vulnerability is common in ICPSs due to the wide use of Modbus protocol in industrial equipments.

Given the vulnerabilities listed in Table I, we construct a hypothetic cyber-attack process involving the following steps:

1. At the 20th minute, the attacker attacks AH by exploiting $\mathcal{V}_{1}$. This is a remote code execution vulnerability found in SIMATIC WinCC, an industrial monitoring software designed by Siemens. The exploitability of $\mathcal{V}_{1}$ is 1 , meaning that a beginner attacker can easily exploit it;
2. At the 52 nd minute, the attacker gains the privilege to manipulate the WinCC server installed on AH;
3. At the 56th minute, the attacker performs a man-in-themiddle (MITM) attack between the HM and GW by exploiting the Modbus protocol vulnerability;
4. At the 68th minute, the attacker successfully acts as the HM to send forged Modbus commands to N1, N2 and N3. Meanwhile, the attacker could also send previously recorded packets to HM;
5. At the 104th minute, the attacker exploits the vulnerability $\mathcal{V}_{7}$ to launch a DoS attack on P1 by injecting false structured query language (SQL) statements;
6. At the 120th minute, the attacker modifies the control variable $u_{1}$ of FV; and
7. At the 128th minute, the attacker modifies the control variable $u_{2}$ of SV.

## B. Implementation of the Proposed Method

1) BN Model: When building the BN, we only consider the hosts and the associated vulnerabilities that help the attacker move towards the aimed target. Thus, hosts C 1 and C 2 are excluded because they have no privilege to access the supervisory network. Also, the vulnerability $\mathcal{V}_{3}$ is not considered since it only causes information leakage. The constructed BN is shown in Fig. 3. In this figure, $\mathcal{G}$ represents the TAR node (sensors or actuators), $\mathcal{V}$ indicates the VUL node, and $\mathcal{P}$ denotes the PRI node. It is assumed that the vulnerabilities of a host have a relationship of Logic OR, i.e., they are independent of each other. The PRI nodes and the VUL nodes have the relationship of Logic AND, implying that to compromise a host $h$, the attacker must gain the privilege of another host communicating with $h$ and make use of at least one vulnerability of $h$ at the same time. Under this condition, all CPTs can be computed by using the CVSS metrics [19].
2) SHS Model: After the BN is built and the CPT parameters are specified, real-time discrete mode transition matrix $\pi_{k}$ is generated from online intrusion detection evidence. For

TABLE I
VULNERABILITY INFORMATION


![img-2.jpeg](img-2.jpeg)

Fig. 3. Bayesian network for the BWPP.
instance, an evidence set $\mathbf{E}=\left\{\mathcal{V}_{1}, \mathcal{P}_{A H}, \mathcal{V}_{6}, \mathcal{P}_{H M}\right\}$ means that the vulnerability $\mathcal{V}_{1}$ and $\mathcal{V}_{6}$ have been exploited and the host AH and HM have been compromised. Then, the Bayes theorem(7) is employed to infer the probabilities of the sensors or actuators to be compromised. It is further used to construct the full mode transition probability matrix $\pi_{k}$.

With reference to the attack steps described in Section VI-A, Fig. 4 gives a simple illustration of the mode transition process of the BWPP under attack. As there are too many possible hybrid modes, Fig. 4 gives only a small part of all possible modes. In Fig. 4, $q^{0}$ represents the normal operation mode, $q^{1}$ represents the hybrid mode where $y_{1}$ is under attack, $q^{2}$ represents the mode where both $y_{1}$ and $u_{1}$ are compromised, and $q^{3}$ denotes the mode where $y_{1}, u_{1}$ and $u_{2}$ are corrupted.
![img-3.jpeg](img-3.jpeg)

Fig. 4. A Simple illustration of the SHS model.

In each of the hybrid modes other than $q_{0}$, the MTTSD of the physical process is computed. Then, the immediate C2P risk is quantified. Let us take mode $q^{2}$ as an example. In this mode, both FV and P1 have been compromised. Then, the matrices $A^{q^{1}}, B^{q^{1}}, B_{a}^{q^{1}}$ and $C^{q^{1}}$ defined in the state space
function(14) of the BWPP process in mode $q^{2}$ are given by

$$
\begin{aligned}
A^{q^{2}} & =\left[\begin{array}{ccc}
0.9998 & 0 & 0 \\
0.0069 & 0.9900 & 0 \\
-0.0007 & 0 & 1
\end{array}\right] \\
B^{q^{2}} & =\left[\begin{array}{ccc}
0.0900 & -0.0349 & -0.0150 \\
0.0003 & 1.4083 & -0.0001 \\
0 & -0.1398 & 0.1659
\end{array}\right] \\
B_{a}^{q^{2}} & =\left[\begin{array}{cc}
1 & -1 \\
0 & 0 \\
0 & 1
\end{array}\right] \\
C^{q^{2}} & =\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0.0063 & 0 & 0.0047 \\
0.0063 & 0 & 0.0047
\end{array}\right]
\end{aligned}
$$

After that, As the constraints (15) and(19) are satisfied in mode $q^{2}$, the unbiased state estimator (16) is developed. For mode $q^{2}$, it is given by

$$
L^{q^{2}}=\left[\begin{array}{cccccc}
4.5024 & -3.5024 & 0.0064 & -0.1449 & 0.1449 \\
0.0484 & -0.0484 & 0.1220 & -0.0676 & 0.0676 \\
-2.033 & 0.6926 & 0.1769 & 110.4252 & 102.34
\end{array}\right]
$$

Next, from the developed state estimator, the TTSDs for mode $q^{2}$ and all possible next modes are obtained. By using (28), the MTTSD for mode $q^{2}$ at the time instant $k=120$ minute is calculated. it is $\overline{T_{b}^{q^{2}}}=30.08$ minutes. Finally, the C2P risk is quantified from (29).

## C. Result Analysis

Three experiments are carried out to predict the probabilities of different attack scenarios. In the experiments, the the states of the physical process when it is under attack are estimated. Then, the real-time C2P risk is quantified.

1) Experiment 1 - Attack Probability Prediction: In the first experiment, the probabilities of the sensors and actuators to be compromised are predicted. For brevity, it is assumed that the two redundant sensors L2 and P2, and the sensor GT are invulnerable. From the constructed BN and real-time intrusion detection evidence, the probability $p_{c}$ of compromise for the other five sensors and actuators can be inferred.

Fig. 5 shows $p_{c}$ for WV, FV, SV, P1 and L1 when the ICPS is under attack. The attack steps have been described previously in Section VI-A. It is seen from Fig. 5 that $p_{c}$ increases as the cyber-attack goes deeper in the ICPS network. Each attack step tends to produce a step change in $p_{c}$. When a

sensor or actuator is compromised, the corresponding $p_{c}=1$. From the predicted real-time $p_{c}$, the most important assets in an urgent need of protection can identified.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Predicted attack probability.
2) Experiment 2 - State Estimation: As explained in Section VI-B, the constraints in (15) and(19) are satisfied in mode $q^{2}$ and an unbiased state estimator(36) has been for this hybrid mode. This allows real-time state estimation for mode $q^{2}$ in this experiment. As $x_{1}$ is the most important system state of the BWPP, its changes are observed when the physical process is under attack. It is assumed that the physical system is running in the steady state before the attacker modifies $u_{1}$ to $1.05 u_{1}$ at the 120th minute. The state estimation result is shown in Fig. 6.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Normal, affected and estimated $x_{1}$.
The green curve in Fig. 6 depicts the evolution of $x_{1}$ when the physical process is affected by the attack. It is seen from this figure that $x_{1}$ deviates from the normal due to the attack at the 120th minute. The tank will explode when $x_{1}$ becomes bigger than $250 \mathrm{~kg} / \mathrm{cm}^{2}$ at the 218 th minute. The orange curve in Fig. 6 is the estimate of $x_{1}$. It is seen from te figure that the estimate $\hat{x}_{1}$ traces $x_{1}$ closely even when cyber-attack is in progress.
3) Experiment 3 - C2P Risk Assessment: The third experiment is to compute the real-time C2P risk. As described in Section VI-A, there are seven attack steps altogether. The
system states can be estimated in an unbiased minimumvariance sense in the first six steps because the constraints in (15) and(19) are satisfied. Thus, the real-time C2P risk value is estimated for the first six steps. For the seventh step, the C2P risk reaches its maximum. In this experiment, $V_{T}$ is set to 10,000 dollars. As the BWPP responds quickly to control commands [23], a small modification on $\mathbf{u}_{k}$ can bring the BWPP to a failure state in a short period of time, typically in tens of minutes. Therefore, $\mathcal{T}_{\text {max }}$ has a small value. It is set as $\mathcal{T}_{\max }=320$ minute.

Fig. 7 presents the real-time C2P risk of the BWPP ICPS under attack. As shown in Fig. 7, the ICPS has a low risk level when the first attack takes place in the corporate network at the 20th minute. Later, when the attacker reaches the supervisory network, $\mathcal{R}$ increases dramatically (see the 68th minute). Then, the risk level goes much higher when the sensors or actuators are attacked at the 104th minute. When both $u_{1}$ and $u_{2}$ are compromised, the physical process is unobservable and $\mathcal{R}$ increases to its maximum, implying that the boiler-turbine is likely to explode immediately.
![img-6.jpeg](img-6.jpeg)

Fig. 7. C2P risk.

## D. Further Discussions

From different perspectives, the three experiments conducted above shows the effectiveness of our SRA method for ICPSs. The first experiment demonstrates that the proposed BN model reflects the security status of system components. The second one shows that our state estimator can robustly estimate system states when the sensors and actuators are partially compromised. The third experiment presents the C2P risk curve, which describes the real-time risk level of the physical system.
creftab: Comparison of SRA Methods for ICPSs compares our method with with existing ones. It is seen from Table II that our risk assessment method provides a comprehensive way to quantify the real-time security risk of ICPSs under attack. In particular, only our method has taken C2P attacks into consideration. In contrast to previous studies which focus only on the attacks in the cyber layer or the physical layer, our method combines BN with an SHS model to assess the C2P risk through analysis of cross-domain attacks in ICPSs.

TABLE II
COMPARISONS OF SRA METHODS FOR ICPSs.


For the cyber layer of ICPSs, a BN model of the attack propagation process is developed to infer the probability of attacks penetrating into the physical layer. BN is a mature probabilistic tool with widespread use for risk analysis in real computer networks. As the cyber part of ICPSs is also a computer network, BN can be easily adapted to real-world ICPSs. Moreover, with consideration of the difficulty of BN modelling in large-scale ICPSs, the traditional BN model is extended with AND/OR gates. Furthermore, when realtime probabilistic inference is performed with BN, some nonrelevant nodes can be trimmed. For example, if a parent node of an OR gate is realized, other parent nodes are no longer relevant and thus can be trimmed. Trimming operations greatly reduce the combinatorial explosion.

As for the physical layer, an SHS model is used to describe the operation mode of the physical process. In each mode, the C2P risk is quantified by means of a robust state estimator, which is designed on the basis of the widely used Kalman filter. As there are too many hybrid modes in general for a complex ICPS, many such modes can be removed by assuming that an attacker has limited energy. In other words, the attacker cannot compromise many devices simultaneously or attack a device currently unreachable. In this way, many infeasible modes are removed, thus reducing the computational complexity of our method.

## VII. CONCLUSION

A new risk assessment method has been presented in this paper to quantitatively evaluate the physical impact of cyber-attacks on ICPSs. It uses a BN to describe the attack propagation process in the cyber layer. With the probabilities of the sensor and actuators being compromised as inoputs, an SHS model in designed to predict the behaviours of the physical process. By computing the MTTSD metric after robustly estimating the process states, the system availability is evaluated and the real-time C2P risk is obtained.

Existing SRA methods for ICPSs consider either the cyber layer or the physical layer. In comparison, our method combines both layers, thus providing a cyber-physical-integrated way to quantify the impact of cyber-attacks on ICPSs. With our method, the prediction of the likelihood of different attack scenarios becomes possible. This helps 1) identify the assets in most urgent need of protection, 2) estimate system states without any prior knowledge about attack patterns, and 3) assess real-time system risk level.

There are a few aspects worth investigating in future work. Our method has dealt with ICPSs with linear dynamics. While
a large number of industrial processes are linear or can be linearized, there are highly nonlinear industrial processes that cannot be handled through linearization. How to design state estimator for nonline ICPSs is a direction for future work. In addition, our method in this paper has assumed that cyber-attacks will drive the physical process of an ICPSs to an undesirable state. However, some ICPSs are resilient to certain types of cyber-attacks. They are able to recover to the steady state in a short period of time after an attack. How to integrate our method with other steady state availability analysis methods to handle this scenario is an interesting topic of research in the future.
