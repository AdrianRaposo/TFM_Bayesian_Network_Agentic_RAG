# A Novel Social Network Group Decision-Making Method in a Quantum Framework 

Mei Cai ${ }^{1,2} \odot$ ・Xinglian Jian ${ }^{2} \cdot$ YuanYuan Hong ${ }^{2} \cdot$ Jingmei Xiao ${ }^{2} \cdot$ Yu Gao ${ }^{2} \cdot$ Suqiong Hu ${ }^{1,2}$<br>Received: 19 September 2022 / Accepted: 21 October 2022<br>© The Author(s) 2022


#### Abstract

Social networks (SNs) have become popular as a medium for disseminating information and connecting like-minded people. They play a central role in decision-making by correlating the behaviors and preferences of connected agents. However, it is difficult to identify social influence effects in decision-making. In this article, we propose a framework of how to describe the uncertain nature of the social network group decision-making (SN-GDM) process. Social networks analysis (SNA) and quantum probability theory (QPT) are combined to construct a decision framework considering superposition and interference effects in SN-GDM scenarios. For the first time, we divide interference effects into symmetry and asymmetry. We construct an influence diagram, which is a quantum-like Bayesian network (QLBN), to model group decisions with interactions. We identify symmetry interference terms from Shapley value and asymmetry interference terms from trust value, respectively. The probability of an alternative is calculated through quantum probability theory in our influence diagram. The combination of QLBN model and social network could gain an understanding of how the group preferences evolve within SN-GDM scenarios, and provide new insights into SNA. Finally, an overall comparative analysis is performed with traditional SNA and other quantum decision models.


Keywords Social network group decision-making (SN-GDM) $\cdot$ Quantum-like Bayesian network (QLBN) $\cdot$ Influence diagram $\cdot$ Social networks analysis (SNA)

## Abbreviations

SN-GDM Social network group decision-making
SN Social network
SNs Social network
SNA Social networks analysis
QPT Quantum probability theory
QLBN Quantum-like Bayesian network
GDM Group decision-making

[^0]DM Decision-maker
DMs Decision-makers

## 1 Introduction

People live in large social contexts, such as schools, workplaces, neighborhoods, and online communities. In addition, they form smaller groups in which they experience a higher level of communication than the rest of the social context Stadtfeld, Takács, and Vörös [1]. Social networks (SNs) like WeChat, and Facebook, play a central role in the transactions and decision-making of individuals by correlating the behaviors and preferences of connected agents [2]. Agents' interaction in a social environment can be expressed as a pattern or rule based on relationships. Because of the increasing availability of data that allows one to infer such interactions, the study of group decision-making (GDM) on SNs is of both theoretical and practical importance [3]. Social network (SN) has become an important element in GDM, which leads to social network group decision-making (SN-GDM)


[^0]:    Mei Cai
    sanmoon_1980@163.com
    Suqiong Hu
    hu_suqiong@126.com
    1 Collaborative Innovation Center on Forecast and Evaluation of Meteorological Disasters (CIC-FEMD), Nanjing University of Information Science and Technology, Nanjing 210044, China
    2 Research Center of Risk Management and Emergency Decision Making, School of Management Science and Engineering, Nanjing University of Information Science and Technology, Nanjing 210044, China

problems. There are two important problems in SN-GDM. Those two problems are how to handle interactions between groups, and how to eliminate cognitive efforts of the decision-makers (DMs) in inter-linkage [4]. We hope to study the decision-making problem closer to the actual situation. Decision-making in an SN is such a situation.

Social network analysis (SNA) focuses on DMs' relationships and the relationship model, which is conceptually different from traditional statistical analysis and data processing methods. The application of SNA can help to improve the quality of GDM and have gradually become an important factor affecting GDM [5].

In decision theory and cognitive sciences, classical cognitive models of judgment rely on Bayesian probabilities. Yet, various empirical results have threatened the predictive and explanatory power of these classical models [6]. In the Bayesian model, we need to quantify two main types of uncertainty [7], aleatory uncertainty and epistemic uncertainty. To better manage epistemic uncertainties, we need to collect enough data based on historical events. While the decision environment in SNA cannot provide sufficient data. We need a new way to portray epistemic uncertainty in the SN-GDM scenario.

The decision-making model based on classical logic cannot well explain the irrational phenomenon in human decision-making behavior. As early as 1992, Tversky and Shafir [8] observed experimentally that human actual decision-making data violated the classical probability theorem. Especially, one of the important laws of classical probability theorem is total probability. Some empirical evidence, such as the two-stage gambling paradigm [9], the prisoner dilemma game [9], and the categorization-decision task [10] have shown the irrational behavior that cannot be explained by classical probability theorem. An interference effect is a violation of the law of total probability. As more and more empirical evidence for interference effects in decision-making paradigms appears, researchers shifted their perspective to quantum probability theory [11].

According to cognitive scientists, persons' beliefs are in a superposition state [12]. This superposition of beliefs will result in the occurrence of quantum interference effects. Quantum interference effects can be seen as waves that crash between each other, leading to waves (beliefs) that are destroyed (destructive interference) and waves that can be reinforced (constructive interference) [13]. Just like the behavior of microparticles, the cognitive and decision-making behavior of people is easily influenced by the situation which is very analogous to the mechanism of the particle in physical systems [14]. That maybe a reasonable explanation of how one person's choice interferes with another person's choice. With the increasing impact of SNs on people's everyday lives, the interference effect cannot be ignored. The interaction (feedback) mechanism in consensus reaching process (CRP) is effective to improve the consensus level [15-17].

Given the prevalence of technological paradigms, the generation of large-scale GDM (LSGDM) framework that takes into account these characteristics has grown exponentially and becomes an important direction in decision science [18]. How to improve the effectiveness of CRP in LSGDM situations become a key issue [19, 20]. Some studies Chen et al. [18], Chen et al. [19], Rodriguez et al. [20], Rodríguez, Labella et al. [21], Garcia-Zamora et al. [22], Jian et al. [23] provide the collective opinion generation framework from different aspect. Quantum probability theory opens the door to addressing LSGDM problems in a totally new light. Interference effects is new form of CRP and helps the group reach a consensus quickly.

How to measure the interference effects among them, and how to construct an SN-GDM method in a quantum framework which can flexibly simulate these interference effect still remain unsolved. At present, it is necessary to bridge the gap between SNA and quantum decision-making. To address the above challenges, we combine quantum probability theory (QPT) and SNA into SN-GDM and propose a quantum-like Bayesian network for superposition and interference effects in SN-GDM scenarios. Use the abundant data from SN and the relatively complete theory of quantum probability to provide an effective auxiliary tool for decision-making problems under complex and uncertain scenarios. The proposed quantum-like Bayesian network is a mathematical model of human behavior derived from principles abstracted and extrapolated from quantum probability theory. The highlights of this paper can be summarized as follows:

- Combine SNA and QPT in GDM.
- Analyze SN-GDM mechanism with an influence diagram.
- Quantify superposition and interference effects in SNGDM scenario.
- Divide interference effects into symmetry and asymmetry.

The paper is organized as follows. Section 2 reviews the concept of SN-GDM, and QPT in decision-making. Section 3 constructs an influence diagram which is a quantumlike Bayesian network and a decision framework based on this influence diagram is developed. In Sect. 4, we develop a model to derive the interference term from an SN which is the key parameter in the influence diagram. In Sect. 5, numerical examples are provided and a comparison with other methods is presented to show the advantages of our method. Finally, the paper is summarized, and the future research prospects are put forward in Sect. 6.

## 2 Preliminary

In this Section, we review the concept of SN-GDM, and QPT in decision-making.

### 2.1 Decision Problem in Social Networks

A social network allows information exchange and communication, and provides social relationships among DMs [24]. Because of DMs' interactions, DMs with more experience and prestige will influence other DMs in the SN [25]. SNA studies the relationships between social entities like members in a group, corporations, or nations. Social interactions are modeled through the use of network structures or graphs, in which agents are represented by nodes, and their relationships are represented by arcs between those nodes [26]. Three important network concepts are proposed: graph-theoretic, algebraic, and sociometric [27].

In SN-GDM, an SN is essentially represented as a graph $G=\{V, E\}$, where $V$ is the set of nodes and $E$ is the set of edges. Nodes represent DMs $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$ and edge $\left(D_{i}, D_{j}\right) \in E$ presents social influence from $D_{i}$ to $D_{j}$. Social influence is a relationship established between two DMs. one DM can affect the other one's opinion and influence his/her decision. To represent social influence, a fuzzy adjacent matrix $X=\left(x_{i j}\right)_{\text {gorm }}$ is used with $x_{i j} \in[0,1]$.

One problem in traditional GDM that needs to be addressed is the determination of agents' weights. Because all agents have complex interactions with each other, the decision environment is quite different from traditional ones. In an SN, DMs' positive (negative) interaction based on a trust relationship will also produce a corresponding synergy (redundancy) effect on the final decision result. There are synergy and redundancy effects among SN members. Synergy effect is a strengthening effect, while redundancy is a weakening effect. Commonly, a weight is assigned to an agent to reflect the individual importance in GDM. However, the importance of an agent not only depends on himself but also on his interactions with others. Grabisch and Labreuche [28] and Grabisch [29] studied the problem of how a criterion's importance changes when added to some coalitions and introduced k-order fuzzy measures to freely trade-off the interaction representation in a much better framework for decision-making. Cai et al. [24] used the modified Shapley importance index to describe the marginal contribution of agents in GDM.

Trust is a representative relationship in SNs. When the strength of a relationship is related to the concept of 'trust', the network is referred to as a trust network [30]. For example, WeChat, as a trust network, shows that users accept advice that comes from individuals they trust.
Recent studies have indicated that trust and distrust are two distinct but coexisting concepts [31].

Definition 1 [32]. Trust value $(t, d)$ is an element of $[0,1]^{2}$, where $t$ is called the degree of trust, and $d$ is the degree of distrust.

A trust score space $\mathcal{B L}=\left([0,1]^{2}, \leq_{t}, \leq_{k}, \neg\right)$ consists of the set $[0,1]^{2}$ of trust scores $\left(t_{i}, d_{i}\right)$, a trust ordering $\leq_{t}$, a knowledge ordering $\leq_{k}$, and a negation $\neg$ defined by:
$\left(t_{1}, d_{1}\right) \leq_{t}\left(t_{2}, d_{2}\right)$ iff $t_{1} \leq t_{2}$ and $d_{1} \geq d_{2}$;
$\left(t_{1}, d_{1}\right) \leq_{k}\left(t_{2}, d_{2}\right)$ iff $t_{1} \leq t_{2}$ and $d_{1} \leq d_{2}$;
$\neg\left(t_{1}, d_{1}\right)=\left(d_{1}, t_{1}\right)^{\prime}$.
Wu, Chiclana and Herrera-Viedma [27] provided two functions (1) and (2) to define the trust score and knowledge deficit.
$T S(t, d)=t-d$,
$K D(t, d)=|1-t-d|$.
Implicit trust plays a significant role in the overall dynamics of SNs. A fuzzy relation is defined as a mapping $R: Y \times Y \rightarrow[0,1]$, where $\mu_{R}\left(y_{i}, y_{j}\right)$ denotes the degree of membership of the relationship between the pair of actors $\left(y_{i}, y_{j}\right)$. Zadeh, Abbasov and Shahbazova [33] use m-ary fuzzy relations to describe an adjacency matrix. Such relations represent social relationships among $m$ individuals when a group of $m$ individuals is considered:

$$
\begin{aligned}
& \mu\left(y_{1}, y_{2}, \ldots, y_{m}\right) \\
& \quad=\left\{\begin{array}{l}
1, \text { if } y_{1}, y_{2}, \ldots, y_{m} \text { are related to each other. } \\
(0,1), \text { if } y_{1}, y_{2}, \ldots, y_{m} \text { are related to each other to same extent. } \\
0, \text { if } y_{1}, y_{2}, \ldots, y_{m} \text { are not related to each other. }
\end{array}\right.
\end{aligned}
$$

Genç et al. [34] presented the relations in the form of linguistic variables. Other semi-fuzzy forms have also been proposed to present the relations. However, interaction among agents in an SN is an abstract concept. To quantify this concept, we need to deeply analyze the decision-making mechanism in an SN.

### 2.2 Quantum Probability Theory

In all aspects of our life, whether natural science or social science, we are faced with all kinds of uncertainty. Uncertainty is modeled by possibility measures, such as fuzzy measure, imprecise probability, belief function and quantum probability. In classical probability theory, events are contained in sample space $\Omega$, while events in QPT

![img-0.jpeg](img-0.jpeg)

Fig. 1 An example of quantum probability in two dimensions
![img-1.jpeg](img-1.jpeg)

Fig. 2 Path selection of decision state transition
are regarded as subspaces of the Hilbert space [35]. If an event has two basic states $\Omega=\left\{E_{1}, E_{2}\right\}$, then the Hilbert space is spanned by a set of orthonormal basis vectors: $|\psi\rangle=\varphi_{1} \exp \left(i \theta_{1}\right)\left|E_{1}\right\rangle+\varphi_{2} \exp \left(i \theta_{2}\right)\left|E_{2}\right\rangle$, where $\left|E_{1}\right\rangle=(1,0)$, $\left|E_{2}\right\rangle=(0,1)$. This situation is shown in Fig. 1.

According to Born's rule [36], the squared value of probability amplitude can be interpreted as classical probability [37]. So, the conversion relationship between probability amplitude and classical probability is
$P\left(E_{1}\right)=\left|\varphi_{1} \exp \left(i \theta_{1}\right)\right|^{2}=\varphi_{1}^{2}, P\left(E_{2}\right)=\left|\varphi_{2} \exp \left(i \theta_{2}\right)\right|^{2}=\varphi_{2}^{2}$,
where $P\left(E_{i}\right)$ is the classical probability of state $E_{i}$.
Busemeyer, Wang, and Lambert-Mogiliansky [10] firstly proposed an experimental study of the decision process by comparing Markov and quantum models. Through using conditional probabilities, the probability of a state can be computed by making the product of the individual probabilities for each transition from one state to another. The probability of transiting from state A , followed by state B and ending in state C (Fig. 2a), that is, $\operatorname{Pr}(A \rightarrow B \rightarrow C)$, is given by:
$\operatorname{Pr}(A \rightarrow B \rightarrow C)=\operatorname{Pr}(A) \cdot \operatorname{Pr}(B \mid A) \cdot \operatorname{Pr}(C \mid B)$.
We cannot distinguish which paths were taken to reach the final state. Moreira and Wichert [12] used the concept of an indistinguishable path to describe this situation. If there are two paths from A to D , such as $\mathrm{A} \rightarrow \mathrm{B} \rightarrow \mathrm{D}$ and $\mathrm{A} \rightarrow \mathrm{C} \rightarrow \mathrm{D}$, the classical probability $\operatorname{Pr}(A \rightarrow D)$ is given by:
$\operatorname{Pr}(A \rightarrow D)=\operatorname{Pr}(A) \cdot \operatorname{Pr}(B \mid A) \cdot \operatorname{Pr}(D \mid B)+\operatorname{Pr}(A) \cdot \operatorname{Pr}(C \mid A) \cdot \operatorname{Pr}(D \mid C)$.
Quantum probability theory does not recognize the single path trajectory principle in traditional Markov chain and holds that the path is not observed. The superposition of path trajectories influenced the final state. The amplitude of transition from the initial state to the final state adopts multiple indistinguishable paths (Fig. 2b), is given as:

$$
\begin{aligned}
\operatorname{Pr}(A \rightarrow D)= & \left|\psi_{A} \cdot \psi_{B \mid A} \cdot \psi_{D \mid B}+\psi_{A} \cdot \psi_{C \mid A} \cdot \psi_{D \mid C}\right|^{2} \\
= & \left|\psi_{A} \cdot \psi_{B \mid A} \cdot \psi_{D \mid B}\right|^{2}+\left|\psi_{A} \cdot \psi_{C \mid A} \cdot \psi_{D \mid C}\right|^{2} \\
& +2 \cdot\left|\psi_{A} \cdot \psi_{B \mid A} \cdot \psi_{D \mid B}\right| \cdot\left|\psi_{A} \cdot \psi_{C \mid A} \cdot \psi_{D \mid C}\right| \cos \theta
\end{aligned}
$$

The term $\cos \theta$ corresponds to a quantum interference term that does not exist in classical probability theory. The term $\cos \theta$ in QPT is the main difference from the classical probability.

## 3 Influence Diagram: A Quantum-like Bayesian Network

To accurately imitate the mechanism of SN-GDM, we design an influence diagram which is a quantum-like Bayesian network combining SN and Bayesian Network to reflect superposition and interference effects. Furthermore, a decision framework based on this influence diagram is developed.

### 3.1 Problem Description

DMs give their preferences on alternatives which can be transformed into a probability distribution of alternatives being selected. The more the DMs prefer an alternative, the greater the probability of the alternative is selected. Finally, the ranking of all alternatives is sorted according to the probability of alternative. Then, the decision-making process can be illustrated in Fig. 3 as an influence diagram. In the process of GDM, the change of a single DM's preference may cause changes of multiple DM's preferences, which can ultimately lead to a greatly change of group preference.

We focus on the superposition effect and interference effect in SN-GDM problem in this paper. First, due to the

![img-2.jpeg](img-2.jpeg)

Fig. 3 An example of influence diagram for a SN-GDM problem
vagueness of the inherently subjective instinct of human thinking, it may be appropriate and sufficient to assess the preference information in a qualitative form rather than a quantitative form. 'Quantum superposition' is the expression of the fact that the DMs have not 'made up their mind' until they get more information. Here, we assume members' opinions in an SN may be a factor influencing their preference and help he/she make a decision. We apply the superposition effect to describe the uncertain state of his/her initial preference. Then, agents' interaction in the social environment which is described as interference effects in a quantum-like decision model can never be obtained in a classical setting. Because of interference effects, the group reaches a consensus and everyone updates his/her preference. Now we give the details from the following two aspects.

### 3.1.1 Superposition Effect

The beliefs of DMs are in a superposition state. There are two basic states of decision maker's preference over alternative $A$ :
(1) State $E_{1}$ : select $A$ (denoted as $\left|E_{1}\right\rangle$ ),
(2) State $E_{2}$ : not select $A$ (denoted as $\left|E_{2}\right\rangle$ ), where $\left|E_{1}\right\rangle=(1,0),\left|E_{2}\right\rangle=(0,1)$.

A decision maker's preference can be represented by the superposition of these two basic states:
$\left|\psi\right\rangle=\varphi_{1} \exp \left(i \theta_{1}\right)\left|E_{1}\right\rangle+\varphi_{2} \exp \left(i \theta_{2}\right)\left|E_{2}\right\rangle$,
where $\varphi_{1}$ and $\varphi_{2}$ are called the probability amplitudes corresponding to states $\left|E_{1}\right\rangle$ and $\left|E_{2}\right\rangle$, respectively. $\left(\varphi_{1}\right)^{2},\left(\varphi_{2}\right)^{2} \in[0,1]$ and $\left(\varphi_{1}\right)^{2}+\left(\varphi_{2}\right)^{2}=1$. The term $e^{i \theta}$ depicts the phase of the amplitude.

### 3.1.2 Interference Effect

DMs preferences over an alternative is a superposition of all possible paths. In the decision situation described in Fig. 2b, the global preference of $A_{j}$ is presented in the form of probability to represent the chance of $A_{j}$ being selected, which is calculated by:

$$
\begin{aligned}
P\left(A_{j}\right)= & \left|\sqrt{P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right)} \exp \left(i \theta_{1}\right)+\sqrt{P\left(D_{2}\right) P\left(A_{2} \mid D_{2}\right)} \exp \left(i \theta_{2}\right)\right|^{2} \\
= & \left(\sqrt{P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right)} \exp \left(i \theta_{1}\right)+\sqrt{P\left(D_{2}\right) P\left(A_{2} \mid D_{2}\right)} \exp \left(i \theta_{2}\right)\right) \\
& \left(\sqrt{P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right)} \exp \left(-i \theta_{1}\right)+\sqrt{P\left(D_{2}\right) P\left(A_{2} \mid D_{2}\right)} \exp \left(-i \theta_{2}\right)\right) \\
= & P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right)+P\left(D_{2}\right) P\left(A_{2} \mid D_{2}\right) \\
& +\sqrt{P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right) \sqrt{P\left(D_{2}\right) P\left(A_{1} \mid D_{2}\right)}} \exp \left(i \theta_{1}-i \theta_{2}\right) \\
& +\sqrt{P\left(D_{1}\right) P\left(A_{1} \mid D_{1}\right) \sqrt{P\left(D_{2}\right) P\left(A_{2} \mid D_{2}\right)}} \exp \left(i \theta_{2}-i \theta_{1}\right) .
\end{aligned}
$$

The above formula can be transformed into:

$$
\begin{aligned}
P\left(A_{j}\right)= & P\left(D_{1}\right) P\left(A_{j} \mid D_{1}\right)+P\left(D_{2}\right) P\left(A_{j} \mid D_{2}\right) \\
& +2 \sqrt{P\left(D_{1}\right) P\left(A_{j} \mid D_{1}\right)} \sqrt{P\left(D_{2}\right) P\left(A_{j} \mid D_{2}\right)} \cos \beta_{12}
\end{aligned}
$$

where $\beta_{12}=\theta_{1}-\theta_{2}$ denotes the phase difference between $D_{1}$ and $D_{2}$, and $\cos \beta_{12}=\cos \left(\theta_{1}-\theta_{2}\right)=\exp \left(i\left(\theta_{1}-\theta_{2}\right)\right)+\exp \left(i\left(\theta_{2}-\theta_{1}\right)\right) / 2$. $\cos \beta_{12}>0$ means there is a positive interference between $D_{1}$ and $D_{2}, \cos \beta_{12}<0$ means there is a negative interference between $D_{1}$ and $D_{2}$ and $\cos \beta_{12}=0$ means no interference happens between $D_{1}$ and $D_{2}$.

This paper will (1) describe decision maker's preference uncertainty by superposition of beliefs. (2) predict the probability distributions of alternatives by modeling uncertainty through quantum interference in decision-making process considering agents' interaction in a SN, (3) identify group decisions and understand the evolution of the GDM process.

### 3.2 Influence Diagram Description

An influence diagram is defined as a compact graphical representation of a decision scenario, in which each node means a decision maker (DM) and each edge means a conditional dependence.

An influence diagram can be divided into three parts:

1. The first part describes the initial preferences of DMs over alternatives. $x_{i j} \in X_{i}$ is the $D_{i}$ 's preference over alternative $A_{j}$.
2. The core part is an SN, which is a (directed or undirected) graph $G=(V, E)$, described by the set of vertices $V$ and set of edgesE. $D_{1}, \ldots, D_{n} \in V$ represent DMs, and the edge $e_{i j} \in E$ between the nodes represents the influence between DM $D_{i}$ and $D_{j}$.
3. The third part is composed of alternatives. Alternative node is associated to a utility function which is the fusion preference of all decision makers.

The nodes in the first part are connected with the nodes in the core part by directed edges. An individual preference vector $\left|P\left(A_{j} \mid D_{i}\right)\right|_{1 \text { von }}$ transformed from initial preferences $x_{i j}$ is assigned to $D_{i} . P\left(A_{j} \mid D_{i}\right)$ is the conditional probability of alternative. The probability amplitude of $P\left(A_{j} \mid D M_{i}\right)$ is propagated and influenced the probabilities of the remaining nodes. That is, every assignment of every node of the Bayesian Network propagates throughout the network until they reach the node representing the query variable. Alternative node is associated to the joint probability which is the
fusion preference of all decision makers. We rank alternatives according to the joint probability.

Cercel and Trausan-Matu [38] defined social influence as the power of individual $A$ in a SN on $B$. Yager [39] discussed the influence of an SN in two situations, which are symmetry and asymmetry; and primarily constructed an undirected graph to represent an SN. The extent to which $A$ affects $B$ is not necessarily the same as that to which $B$ affects $A$ [40]. It is even possible that the influence of A on B is positive, while the influence of B on A is negative. Trust is a asymmetric relationship in SN [30]. The trust relationship between $D_{i}$ and $D_{i}$ is not equal. It is common for one side to trust the other side slightly more or less. Hence, trust is directed and asymmetric. According to the structure of SNs, we can classify the influence diagram into a symmetry diagram and an asymmetry one. Our model will discuss these two situations.

Edges among DM nodes represent influences among them with the value $I\left(D_{i}, D_{i}\right)$. The subgraph which is only composed of DM node $D_{i}$ in an SN can be a directed or undirected graph. If we view the interaction from $D_{i}$ to $D_{j}$ equals to the interaction from $D M_{i}$ to $D M_{i}$, then nodes are connected with dotted undirected line and the SN is an undirected graph. Otherwise, nodes are connected with a dotted directed line and the SN is a directed graph.

In an Influence diagram, the utility function of an alternative node is presented as the probability of the alternative $A_{j}$. As the decision-making process begins, one agent expresses the preference in a level of uncertainty, and produces different waves, causing interference effects. Finally, we obtain $P\left(A_{j}\right)$ and rank alternatives according to $P\left(A_{j}\right)$.

Nodes in "influence diagram" are associated with random variables which are a set of quantum systems $v_{1}, \ldots, v_{n} \in V$, each of them associated with a Hilbert space with a specific dimension. Consequently, all values contained in the conditional probability tables of the random variables are complex numbers. In the quantum framework, the probability of alternatives can be obtained by considering the interference effect between two DMs. Interference effect in quantum decisionmaking can be explained and measured by the influence of group members. The final state $P\left(A_{i}\right)$ is described as function (10) containing an interference term:
$P\left(A_{j}\right)=\sum_{i=1}^{s}\left|\psi_{I_{j}} \cdot \psi_{D_{i} \mid I_{j}} \cdot \psi_{A_{j} \mid D_{i}}\right|^{2}+$ interference.

### 3.3 A framework of SN-GDM According to Influence Diagram

Due to the complexity of SN-GDM, the following parameters are defined to describe it:

1. $D=\left\{D_{1}, D_{2}, \ldots, D_{n}\right\}$ is the set of DMs, where $D_{i}$ is the $i$-th DM.
2. $A=\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$ is the set of alternatives, where $A_{j}$ denotes the $j$-th alternative.
3. $X_{i}=\left(x_{i j}\right)_{m}$ is the individual preference vector, where $x_{i j} \in \mathbb{R}^{+}$is the evaluation of $D_{i}$ concerning alternative $A_{i} . X=\left(x_{i j}\right)_{n \times m}$ is the individual preference matrix.

In an ''influence diagram', we divide the GDM into three phases: the initial phase, the inference phase, and the selection phase. DMs express their initial preferences before GDM. In the initial phase, the preference matrix is transformed into a quantum probability matric. In the inference phase, SN analysis is utilized to obtain the interaction and we build a connection between the concept of interaction in an SN and interference term in QPT. In the selection phase, the probability of $A_{j}$ is updated based on the quantum probability matrix and we obtain the global preference of $A_{j}$ in this SN. The details of these three phases are as follows:

### 3.3.1 Initial Phase

The preference matrix $X$ is transformed into the quantum probability matrix for the quantum probability calculation. We assume that the more the DM prefers the alternative, the greater the probability that the alternative will be selected. So, the preference matrix can reflect the probability of the selected situation. The preference matrix $X=\left(x_{i j}\right)_{n \times m}$ should be transformed to quantum probability matrix $Q=\left(q_{i j} \exp \left(i \theta_{i j}\right)\right)_{n \times m}$ for the preference aggregation in GDM. First, we normalize preference $x_{i j}$ by function (11):
$x_{i j}^{\prime}=\frac{x_{i j}}{\sum_{i} x_{i j}}$,
where $x_{i j}^{\prime}$ satisfies $\sum_{i=1}^{n} x_{i j}^{\prime}=1$ and $0 \leq x_{i j}^{\prime} \leq 1$. Then we transform classical probability into quantum probability. The quantum probability matrix is $Q=\left(q_{i j} \exp \left(i \theta_{i j}\right)\right)_{n \times m}$, where $q_{i j}=\sqrt{x_{i j}^{\prime}} \cdot q_{i j} \exp \left(i \theta_{i j}\right)$ describes the amplitude of the wave, and the term $\theta_{i j}$ represents the phase of the amplitude. Our GDM processes based on quantum probability will be expanded based on this matrix.

### 3.3.2 Interference Phase

In this phase, we need to quantify the agents' interaction in an SN. We cannot observe the interference process in the consensus reaching process. Through SNA, we obtain interaction information and find out the measurement of interference effect.

### 3.3.3 Selection Phase

We update the probability of alternative after considering the inference effect based on QPT, and obtain the rank of alternatives according to the probability of alternative.

## 4 The Quantum Interference Measure

In this section, we identify a key parameter in QPT-interference term, with the help of SNA technology. We innovatively divide interference effects into two types: symmetric and asymmetric, corresponding to SNs with different contexts.

### 4.1 Derive the Interference Term from an SN

In an SN, during their interactions, DMs with more experience and knowledge may influence other decision makers [25]. In short, SN members are more likely to interfere with each other because of a strong connection. SNA supplies much information from a realistic scenario. And it is reasonable to use SN to drive the interference term in quantum mechanics. The interference term in an SN would be a powerful tool to remedy the gap between the abstract concept in quantum mechanics and realistic decision scenarios. Many references [24, 41-44] show the social influence between DMs in an SN and measure it by interaction index through SNA. For example, we can see that the social context similarity between two unknown decision makers can influence the social interactions [45]. Based on this property, we can estimate an interaction index based on the social context similarity between decision makers. Wu et al. [43] proposed a trust-based consensus model of SN-GDM for visual interaction. Xu et al. [5] identify types of relationships between DMs and construct uncertainty optimization models to calculate trust value between DMs. The process of how to obtain reliable interaction parameters from developed SNs is also described in these references in great detail.

Now, we give the definition of interference term in an SN.
Definition 1. The interference term driven from an SN is defined as $I\left(D_{i}, D_{l}\right)$, which is the measure of interference effect between $D_{i}$ and $D_{l}$. In an SN, it can be described by an undirected graph, when $I\left(D_{i}, D_{l}\right)=I\left(D_{l}, D_{s}\right)$, we name this kind of interference as symmetrical interference. Otherwise, we name this kind of interference as asymmetrical interference, when $I\left(D_{i}, D_{l}\right) \neq I\left(D_{l}, D_{s}\right)$.

Edges among DM nodes represent interference among them with the value $I\left(D_{i}, D_{l}\right)$. If interference is symmetrical, then nodes are connected with dotted undirected line and the SN is an undirected graph. Otherwise, nodes are connected with dotted directed line and the SN is a directed graph. Our model will discuss these two situations by SNA.

The phase difference measured by $\cos \left(\theta_{i}-\theta_{l}\right)$ is a critical parameter in QPT. Since the range of the interaction index is consistent with the value range of $\cos \left(\theta_{i}-\theta_{l}\right)$, and this study measures the interference value between DMs by interference term, it is reasonable to apply the interaction index to replace the cosine of the phase difference between DMs. So we define $\cos \left(\theta_{i}-\theta_{l}\right)$ as:
$\cos \left(\theta_{i}-\theta_{l}\right)=I\left(D_{i}, D_{l}\right)$.
There are three situations:
i. If there is no interference between $D_{i}$ and $D_{l}$, then $I\left(D_{i}, D_{l}\right)=0 \Longleftrightarrow_{\left(\theta_{i}-\theta_{l}\right)=\pi / 2 \text { and } 3 \pi / 2 \Rightarrow} \cos \left(\theta_{i}-\theta_{l}\right)=0 ;$
ii. If there is a positive interference between $D_{i}$ and $D_{l}$, then $I\left(D_{i}, D_{l}\right)>0 \Longleftrightarrow\left(\theta_{i}-\theta_{l}\right) \in[0, \pi / 2) \operatorname{and}(3 \pi / 2,2 \pi]$ $\Rightarrow \cos \left(\theta_{i}-\theta_{l}\right)>0$
iii. If there is a negative interference between $D_{i}$ and $D_{l}$, then $I\left(D_{i}, D_{l}\right)<0 \Longleftrightarrow\left(\theta_{i}-\theta_{l}\right) \in(\pi / 2,3 \pi / 2) \Rightarrow \cos \left(\theta_{i}-\theta_{l}\right)<0$.

### 4.2 Symmetric Interference from Shapley Value and Interaction Index

In this subsection, we introduce the interaction index of elements $i$ and $j$ [46] to quantify the symmetry interference term in an SN. Interaction index is a fuzzy measure which can well reflect complementariness, redundancy, or independence between elements. A fuzzy measure $\mu(\cdot)$ is a capacity with the interpretation that the value $\mu(\mathrm{A})$ of a crisp subset $A \subseteq \Omega$ is the subjective evaluation expressing. $\mu(\cdot)$ reflects the degree of matching of the observed $A$ with some intended target.

Definition 2 [47]. A fuzzy measure on finite set $N=\{1,2, \ldots, n\}$ is a set function $\mu: \mathcal{P}(N) \rightarrow[0,1]$ satisfying:

$$
\mu(\varnothing)=0, \mu(N)=1
$$

For all $A, B \in \mathcal{P}(N)$ with $A \subseteq B, \mu(A) \leq \mu(B)$,
where $\mathcal{P}(N)$ is the power set of $N$.
When measuring the importance of element $D_{i}$, $\mu=(\mu(1), \mu(2), \ldots, \mu(n))^{T}$ represents the vector of fuzzy measure on the set of DMs, where $\mu_{i}$ is the weight
information of DM $D_{i}$, and $0 \leq \mu(i) \leq 1$. The importance $\mu(i)$ is determined based on its roles in various coalitions containing $i$, compared with coalitions not containing $i$. We evaluate the importance of every element in $N$ by using an analogy with multi-person game theory. From a multiperson game theory perspective, the pair $(N, \mu)$ is a game in characteristic function form, $N$ is the set of players, and $\mu$ is the characteristic function. We assume players $i$ and $j$ are symmetric, which means $\mu(S \cup\{i\})=\mu(S \cup\{j\})$ for $S \subset N-\{i, j\}$. The importance of element $i$ is a weighted arithmetic mean of the contribution of $i$ with respect to any subset $S$ not containing $i$. Shapley [48] proposed a definition of importance index, based on a set of reasonable axioms (see also [49]).

Definition 3. Let $\mu$ be a fuzzy measure on $N$. The Shapley value of an element $i \in N$ is given by:
$I_{\{i\}}(\mu, N)=\sum_{S \subseteq N \backslash\{i\}}(n-s-1)!s!/ n!(\mu(S \cup i)-\mu(S)), i \in N$,
where $s$ and $n$, respectively, denote the cardinalities of $S$ and $N$.

The interaction index reflects the weighted average value of the marginal contribution of set $S \subset N$ in all coalitions. Besides, the interaction index is a favorable description of the interaction among DMs in GDM, and it is a superior supplement to the Shapley value. The interaction index between DMs is derived from their weights, which can reflect the actual relationship between DMs to a certain extent. Grabisch [29] proposed the concept of k-order additive fuzzy measure for all $S$ where $I_{k}=0$, if $|S|>k$. When $k=2$, we obtain a special function (14) to define the interaction index of two elements $i$ and $l[46]$.

$$
\begin{aligned}
I_{\{i, l\}}= & \sum_{S \subseteq N \backslash\{i, l\}}(n-s-2)!s!/(n-1)!\left(\mu(S \cup\{i, l\})\right. \\
& -\mu(S \cup\{i\})-\mu(S \cup\{l\})+\mu(S)), i, l \in N
\end{aligned}
$$

$I\left(D_{i}, D_{l}\right)=I_{\{i, l\}}$ is the value of edge $e_{i, l}$. There are three situations which correspond to $\cos \left(\theta_{i}-\theta_{l}\right)$, where $\left(\theta_{i}-\theta_{l}\right) \in[0,2 \pi]$ :
i. If there is no interference between $D_{i}$ and $D_{l}$, then $\mu(\mathrm{i} l)=\mu(i)+\mu(l) \Longleftrightarrow\left(\theta_{i}-\theta_{l}\right)=\pi / 2 \text { and } 3 \pi / 2 \Rightarrow$ $\cos \left(\theta_{i}-\theta_{l}\right)=0$
ii. If there is positive interference between $D_{i}$ and $D_{l}$, then $\mu(i l)>\mu(i)+\mu(l) \Longleftrightarrow\left(\theta_{i}-\theta_{l}\right) \in[0, \pi / 2) \operatorname{and}(3 \pi / 2,2 \pi]$ $\Rightarrow \cos \left(\theta_{i}-\theta_{l}\right)>0$

iii. If there is negative interference between $D_{i}$ and $D_{j}$, then $\mu(i l)<\mu(i)+\mu(l) \Longleftrightarrow\left(\theta_{i}-\theta_{j}\right) \in(\pi / 2,3 \pi / 2) \Rightarrow$ $\cos \left(\theta_{i}-\theta_{j}\right)<0$.

### 4.3 Asymmetric Interference from Trust Value

In this subsection, we introduce trust score to quantify asymmetry interference in an SN. A tuple of the type $\lambda=\left(t_{i l}, d_{i l}\right)$ where $t_{i l}, d_{i l} \in[0,1]$, in which the first component $t_{i l}$ is the strength of trust, and the second component $d_{i l}$ is the strength of distrust. The set of trust function (TFs) will be denoted by $\Lambda=\{\lambda=(t, d) \mid t, d \in[0,1]\} \equiv[0,1]^{2}$. The trust score $t s_{i l}$ is in $[0,1]$ and represented as [50]:
$t s_{i l}=t_{i l}-d_{i l}$.
We construct relation between trust score and inference term and define:
$I\left(D_{i}, D_{l}\right)=t s_{i l}$.
The trust relationship between A and B is not equal. It is common for one side to trust the other side slightly more or less. Hence, the trust relationship of DMs is directed and asymmetric. Here, $t s_{i l} \neq t s_{l i} \Rightarrow I\left(D_{i}, D_{l}\right) \neq I\left(D_{l}, D_{i}\right)$, and the SN is a directed graph.

### 4.4 Calculation of the Probability Value of Alternative Nodes in an Influence Diagram

As mentioned in Sect. 4.1, there are two situations of interference effect:
(1) Symmetrical interference: We can substitute the interference term to the interaction index, i.e., Shapley interaction index $I_{\left\{i, i^{\prime}\right\}}$, it can be written by:
$P\left(A_{j}\right)=\sigma_{1}\left(\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+2 \sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} I_{\left\{i, i^{\prime}\right\}}\right)$,
where $\sigma_{1}=1 / \sum_{i=1}^{m}\left(\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+2 \sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} I_{\left\{i, i^{\prime}\right\}}\right)$ is a normalization factor.
(2) Asymmetrical interference: We use the trust score to replace the intervention term, it can be written by:
$P\left(A_{j}\right)=\sigma_{2}\left(\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+\sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} t s_{i \vec{r}}+\sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} t s_{\vec{r} i}\right)$.

Table 1 The trust score $t s_{i l}$ of DMs in an SN


where $\sigma_{2}=1 / \sum_{j=1}^{m}\left(\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+\sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} t s_{i \vec{r}}+\sum_{i=1}^{n-1} \sum_{\vec{r}= i+1}^{n} q_{i j} q_{i^{\prime} j} t s_{\vec{r} i}\right)$
is a normalization factor.
Finally, we can rank the alternatives by $P\left(A_{j}\right)$ according to the following relation:
$P\left(A_{j}\right)=P\left(A_{j^{\prime}}\right) \Rightarrow A_{j} \sim A_{j^{\prime}}$,
$P\left(A_{j}\right)>P\left(A_{j^{\prime}}\right) \Rightarrow A_{j}>A_{j^{\prime}}$.
And obtain the final preference of $A$.

## 5 Comparison and Analysis

First, we introduce two numerical examples. In the following two examples, we used the proposed method to choose the better alternative in SNs with symmetric interference and asymmetric interference, respectively. Then, we solve the same problem with Choquet integral as an aggregation operator for obtaining group preference. Finally, we analyze the difference of several QPT methods.

### 5.1 Numerical Examples

In the following two examples, we used the proposed method to choose the better alternative in SNs with symmetric interference and asymmetric interference, respectively. First, we design an example of asymmetrical interference in SN. In interference phase, we obtain trust scores through observing their behaviors in an SN (see Table 1).

The probability of state $A_{j}$ is calculated with function (18).
$P(A)=0.282, P(B)=0.252, P(C)=0.186, P(D)=0.280$.
Rank of alternatives is $A>D>B>C$
The probabilities of alternatives have not changed. Because $\left(t s_{i l}{ }^{\prime}+t s_{i^{\prime} i}\right) / 2$ equals to $I_{\left\{i, i^{\prime}\right\}}$ in Table 3. We can find:

$$
\begin{aligned}
& P\left(A_{j}\right)=\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+\sum_{i=1}^{n-1} \sum_{\ell=i+1}^{n} q_{i j} q_{\ell j} i s_{i \ell}+\sum_{i=1}^{n-1} \sum_{\ell=i+1}^{n} q_{i j} q_{\ell j} i s_{\ell i} \\
& =\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+\sum_{i=1}^{n-1} \sum_{\ell=i+1}^{n} q_{i j} q_{\ell j}\left(i s_{i \ell}+i s_{\ell i}\right)=\sum_{i=1}^{n}\left|q_{i j}\right|^{2}+2 \sum_{i=1}^{n-1} \sum_{\ell=i+1}^{n} q_{i j} q_{\ell j} I_{\{i, \ell\}}
\end{aligned}
$$

So symmetrical interference diagram can be viewed as a degraded form of an asymmetrical interference diagram. The asymmetrical interference diagram can solve more complex situations. However, most interference effects studies integrated quantum probability theory assume influence relationship is symmetric and does not distinguish between directions. So, function (18) is the common presentation of influence effects. Our study distinguishes symmetric and asymmetric influence effects which are more consistent with the character of social influence.

Then we give a numerical example of symmetrical interference in SN. There is a small SN with 5 DMs $D=\left\{D_{1}, D_{2}, \cdots, D_{5}\right\}$. They are asked to give the preferences of four alternatives $\{A, B, C, D\}$, as shown in Table 2 below.

### 5.1.1 Initial Phase

The preference matrix $X=\left(x_{i j}\right)_{n \times m}$ is transformed into quantum probability with function (11) (see Table 3). The unobserved quantum preference matrix is $Q=\left(q_{i j} \exp \left(i \theta_{i j}\right)\right)_{n \times m}$, where $q_{i j}=\sqrt{x_{i j}}$.

In a quantum probability matrix, it is defined as follows:

Table 3 Preference matrices for alternatives


### 5.1.3 Selection Phase

Influence diagram is used to infer the utility value $P\left(A_{j}\right)$ of each alternative. The probability of state $A_{j}$ is calculated with function (17).
$P(A)=0.282, P(B)=0.252, P(C)=0.186, P(D)=0.280$.
Rank of alternatives is $A>D>B>C$.

### 5.2 Comparison of Aggregation Model

In a BN, there are $n$ paths from the initial state to alternative node $A_{j}$, which are $I\left(A_{j}\right) \rightarrow D_{i} \rightarrow P\left(A_{j}\right), \quad i=1,2 \ldots, n$. We can calculate $P\left(A_{j} \mid D_{i}\right)$ for each path and utilize a proper aggregation operator $f$ to obtain the utility of alternative node $A_{j}$. Considering the interaction among agents in an SN , the above ideas will miss important information. The interaction of the group is manifested in a way of sound or silent communication. Although there is no mandatory change in other people's opinions, this communication has imperceptibly affected other people's preferences, and finally
$Q=\left[\begin{array}{l}0.480 \exp \left(i \theta_{11}\right) \mid 0.447 \exp \left(i \theta_{21}\right) 0.471 \exp \left(i \theta_{31}\right) 0.530 \exp \left(i \theta_{41}\right) 0.557 \exp \left(i \theta_{51}\right) \\ 0.555 \exp \left(i \theta_{12}\right) \mid 0.447 \exp \left(i \theta_{22}\right) 0.471 \exp \left(i \theta_{32}\right) 0.500 \exp \left(i \theta_{42}\right) 0.525 \exp \left(i \theta_{52}\right) \\ 0.519 \exp \left(i \theta_{13}\right) \mid 0.516 \exp \left(i \theta_{23}\right) 0.544 \exp \left(i \theta_{33}\right) 0.433 \exp \left(i \theta_{43}\right) 0.491 \exp \left(i \theta_{53}\right) \\ 0.439 \exp \left(i \theta_{14}\right) \mid 0.578 \exp \left(i \theta_{24}\right) 0.509 \exp \left(i \theta_{34}\right) 0.530 \exp \left(i \theta_{44}\right) 0.415 \exp \left(i \theta_{54}\right)\end{array}\right]$.

### 5.1.2 Interference Phase

Suppose an SN is described by an undirected graph, and obtain interaction indices through observing their behaviors in an SN (see Table 4).

Table 2 Preference matrices for alternatives


affected the results of GDM. It is not easy to find such aggregation operator $f$.

SNA in SNs has important social significance and application value [40]. SNs are integrated into the influence diagram described in Sect. 3.2. This integration is a key innovation of our method. In this section, we will discuss some

Table 4 The interaction index of DMs in an SN


methods related to SNA to describe interference effects in SN-GDM scenario.

GDM proposes to represent preferences of DMs on set A of alternatives by an overall value function $U: X \rightarrow R . U$ is the aggregation operator for obtaining group preference. We aggregate individuals' preferences to obtain utility value of alternative, which is defined as $U\left(A_{j}\right)=f\left(U\left(A_{j} \mid D_{1}\right), U\left(A_{j} \mid D_{2}\right), \ldots, U\left(A_{j} \mid D_{n}\right)\right)$, where $f$ is an aggregation operator. The additive model is very popular for aggregation of individual preferences. Given the numerical example in Sect. 5.1, if we do not consider the interference effect and suppose everyone is the same important. We cannot distinguish between good and bad alternatives. However, many extension models have been proposed considering the interaction among DMs in an SN.

Cai et al. [24] classify the interaction among DMs into synergy and redundancy effects. A final ranking of alternatives should reflect synergy and redundancy effects by enhancing or weakening the scores of alternatives. Traditional GDM contains two main procedures: the consensus reaching process (CRP) and the selection of acceptable alternatives [25]. The CRP is the forerunner of selection and is responsible for the input and fusion of multiple opinion sources. Therefore, the interference effect is considered to generate an opinion adjustment model for experts to improve the consensus level of the group. The Choquet integral which is in the form of Möbius representation can also be applied in modeling the interference effect and reducing the impact from synergy and redundancy between DMs.

The Choquet integral is represented as follows:
$C_{\mu}(x)=\sum_{i \in N} a(i) x_{i}+\sum_{\left[i, j\right] \in N} a(i j)\left(x_{i} \bigwedge x_{j}\right)$,
where $a(S)=\sum_{T \subseteq S}(-1)^{|S|-|T|} \mu(T)$.
We assign everyone with equal importance, that is $\mu(i)=0.2, i=1,2, \cdots, 5$, and the preference matrices for alternatives is in Table 2. Set $a\left(i i^{t}\right)=I_{\left[i, i^{t}\right]}$, we obtain the global preference with function (19):

$$
\begin{aligned}
& C_{\mu}(A)=6.93 \\
& C_{\mu}(B)=6.68 \\
& C_{\mu}(C)=5.73 \\
& C_{\mu}(D)=7.8
\end{aligned}
$$

Table 5 The comparison of aggregation mode


Rank of alternatives is $D>A>B>C$.
The result obtained from [24] is a little different from the one by our proposed quantum-like Bayesian network. The comparison of aggregation mode is in Table 5.

We can explain from three aspects:
(1) Weight determination of DMs: In a GDM problem, the weight determination of DMs is always difficult to solve. It inevitably increases subjectivity when we assign weight to everyone and has a great impact on the evaluation results. When we use function (19), we assign $\mu(i)=0.2$. While in our proposed method, we needn't assign weight to every DM. So the rank maybe different because of subjectivity in the weight determining process.
(2) Coexistence of superposition and interference effects: Superposition and interference effects can be reflected through QPT, while superposition effects cannot be reflected through Choquet integral. The numerical example in Sect. 5.1 considers interference effects in SN-GDM but ignores superposition effects. That may be another reason for the different result. There are many studies applied fuzzy sets or linguistic variables to reflect DMs uncertainty and achieve some good results. However, it is very complicated to combine fuzzy sets or linguistic variables with Choquet integrals to deal with these two effects together.
(3) More objective judgment on interference effect: Although some SNA methods [43, 51, 52] use trust relationship to replace interference effects, they are suspected of being "too subjective". Quantum decision-making can make up for these defects and better explain people's decision-making behavior under uncertainty or contradiction. Research shows that when the decision-making path is unknown, human behavior results will violate the certainty principle in classical probability and the total probability theorem [53]. Quantum logic has greater flexibility and randomness, and has more advantages in describing people's uncertain belief states, which is more conducive to explaining the trust relationship between people.

### 5.3 Comparison with Other QPT Methods

In recent years, scholars began to use the interference effect in QPT to solve the GDM problem, but the relevant research is insufficient. How to scientifically calculate the interference term's value between DMs is still a troublesome issue to be solved. Table 6 shows the comparison for solving interference values between the previous methods and the proposed method.

In Table 6, we compare the existing methods considering interference effects in GDM problems from four aspects: basic principle, number of DMs, advantages, and limitations of parameters determination. The similarity heuristic

Table 6 The comparison between existing QPT methods and the proposed method


developed by Moreira and Wichert [54] is highly subjective. The approach presented by He et al. [35] has advantages in evaluating the reliability of decision-making results, but it is only suitable for the situation of two DMs and cannot obtain the precise interference value. Besides, although the methods proposed by Huang, Yang and Jiang [55] and She, Han and Liu [14] make up for the shortcomings of the first two methods to some extent, they do not establish a direct connection between the DM's weight and the interference effect. It can be seen that the proposed model can be applied to the situation where multiple DMs participate in decisionmaking, but it needs the support of other techniques.

## 6 Conclusion

One of the main arguments for a quantum approach to cognitive phenomena is the existence of interference effects in higher cognitive processes such as perception, decisionmaking, and reasoning. Therefore, the traditional probability model cannot accurately simulate people's decision-making behavior. Compared with classical probability, quantum logic has greater flexibility and randomness. QuantumBayesian network and quantum-like Bayesian network realize the prediction of human decision-making behavior from psychological experiments to real application scenarios. The proposed model demonstrates the possible interference phenomena of entanglement of different choices and can also be extended to social selection-based joint and other statistical analysis and prediction tools. It also realizes the combination of abstract mathematical principles and behavioral decision-making models. The contributions of this paper are as follows:

1. By expanding the research methods of decision-making problems, introducing the principle of quantum probability to describe and explain human cognition and decision-making behavior, we can solve the modeling problem of GDM behavior in complex situations, and provide a novel and complete mathematical theoretical framework for improving cognition and decision-making theory. We design an influence diagram which combines SN and Bayesian network and realize the combination of SNA and QPT. Our influence diagram only needs partial information of a black box to complete reasoning. On the other hand, compared with traditional bidirectional feedback mechanism in CRP, our proposed method does not need a moderator to help DMs interact and feedback, and it is applicable to the situation where the initial consensus level is relatively low, in which it is difficult to find a 'central opinion' to represent all individual opinions.
2. Quantum-Bayesian holds a subjective Bayesian or personal view of quantum probability. The Born's rule of quantum theory is also an empirically motivated norm of rationality that a wise DM should follow. Rational decision makers assigned the same initial quantum state may come to differ in their subsequent state. Superposition and interference effects in quantum theory highly attach to human cognitive process. Quantum-Bayesian can explain some irrational decision behavior.
3. Although interference effects are often mentioned in psychology, the best explanation for these effects is not universally acknowledged. We divide interference effects into symmetry and asymmetry and map them to SNs with different structures. We modify the common form of conditional probability in QPT in functions (17) and (18). This modification is a great attempt of this paper.

The increasing availability of data allows one to infer interference effects in a group which is of both theoretical and practical importance. SNA supplies much information from a realistic scenario. However, our approach has

limitations. Because of people's different understanding of social influence, it is likely to cause deviation to the decision results. And people's understanding of social influence has not reached a consensus so far. Further research is needed to obtain more objective decision-making results.

On the other hand, interference effects are dynamic. In our study, interference effects are not dynamic which is the main limitation. In an SN-GDM environment, inconsistencies in consensus are inevitable. However, interference effects can improve the consensus level of the group. The CRP is a dynamic process. How to determine the dynamic change of the term $\cos \theta$ in line with actual decision-making remains to be studied. Future research can also consider how to solve the challenges, such as: opinion polarization, scalability, noncooperative behaviors, supervision, the uncertainty of information and support systems to deal with large numbers of experts in LSGDM in a quantum framework. We also can turn the SN in this paper into a community or organization, build a quantum cognitive framework, and use the decision-making method based on quantum Bayesian network to solve the decision-making problem. SNA still needs the support of information technology to extract and quantify the relationship information between SN members.

Author Contributions MC conceptualization, methodology, writingoriginal draft. XJ writing-review and editing. JX writing-review and editing. YG collection and revision of relevant literature.

Funding This work was funded by National Natural Science Foundation of China (NSFC) (71871121), Future Network Scientific Research Fund Project (FNSRFP-2021-YB-19). Postgraduate Research \& Practice Innovation Program of Jiangsu Province (KYCX22_1248). Project of the Meteorological Industry Research Center (sk20210032).

Availability of Data and Materials My manuscription has no associated data.

## Declarations

Conflict of Interest The authors declare that they have no conflict of interest.

Ethical Approval and Consent to Participate Articles do not rely on clinical trials.

Consent for Publication The authors declare the consent for publication.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
