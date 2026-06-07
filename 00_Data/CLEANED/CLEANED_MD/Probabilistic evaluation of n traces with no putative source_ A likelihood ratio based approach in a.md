# Probabilistic evaluation of $n$ traces with no putative source: a likelihood ratio based approach in an investigative framework 

I. De March*, E. Sironi, F. Taroni<br>University of Lausanne, School of Criminal Justice, 1015 Lausanne-Dorigny, Switzerland


#### Abstract

Analysis of marks recovered from different crime scenes can be useful to detect a linkage between criminal cases, even though a putative source for the recovered traces is not available. This particular circumstance is often encountered in the early stage of investigations and thus, the evaluation of evidence association may provide useful information for the investigators. This association is evaluated here from a probabilistic point of view: a likelihood ratio based approach is suggested in order to quantify the strength of the evidence of trace association in the light of two mutually exclusive propositions, namely that the $n$ traces come from a common source or from an unspecified number of sources. To deal with this kind of problem, probabilistic graphical models are used, in form of Bayesian networks and object-oriented Bayesian networks, allowing users to intuitively handle with uncertainty related to the inferential problem.


Keywords: Evidence interpretation; Likelihood ratio; Bayesian networks; Objectoriented Bayesian networks; Case linkage.

## 1 Introduction

In forensic practice, scientists are frequently asked to deal with cases in which several traces of the same type are collected. These items of evidence can be found on a unique crime scene or in different locations related to distinct criminal activities. If the scientific comparative analysis performed on the recovered traces shows that there are some relevant similarities between them, and if the traces are considered relevant to the criminal activity, it can be assumed that a linkage may exist between the different cases because a unique perpetrator could be the source of the traces $[1,2]$.
Moreover, if any putative source that could be at the origin of traces is known, it is crucial to evaluate the strength of the potential link, due to the fact that this kind of information could

[^0](C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    *Corresponding author: ilaria.demarch@unil.ch

allow investigators to treat the cases as a series. Therefore, this work aims to investigate an inferential model to deal with such an investigative framework. A similar analysis was performed by Taroni et al. [3] in a scenario considering two items of evidence recovered in two locations. Here, the goal is to extend the reasoning to a scenario involving $n$ traces recovered on $n$ different crime scenes. The likelihood ratio (LR) will be used as a measure of the degree to which the evidence (in this case, the observed similarities between traces) is capable of discriminating between two competing propositions, i.e. the traces come from the same (unknown) source or from at least two different sources. Graphical models are developed in order to qualitatively and quantitatively describe the problem of interest. The advantages of the probabilistic graphical environment will be discussed, putting forward its flexibility and dynamism. This work's objective is to support a probabilistic use of investigative information in order to provide a structured approach to assess scientific elements issued from crime scene investigations for intelligence purposes.
The paper is structured as follows: Section 2 describes the scenario of interest and the questions related to the management of uncertainty in our investigative setting. In Section 3 graphical models, such as Bayesian networks and object-oriented Bayesian networks, are used to represent the proposed scenario and investigate the dependencies between the variables of interest. Section 4 presents the development of the likelihood ratio formula considering the two propositions previously defined. Finally Section 5 illustrates a practical example with a fixed number of traces; the adjustment of the formula and the graphical models will be described.

# 2 Scenario 

A forensic scientist is asked to deal with $n$ traces recovered at $n$ separate crime scenes. All the traces are of the same kind, and each trace is characterized by a single discrete attribute $A$. For sake of illustration, consider $n$ shoe marks found on $n$ crime scenes, characterized by their general pattern only, or $n$ blood stains defined by their genetic DNA profile. Assume the traces have the same degree of quality, and according to the scientific comparative analysis, they present a relevant amount of similarities, so that it cannot be excluded that they share a common origin. Finally, no suspect who could be at the origin of the traces is known. Because of the absence of a suspect, the problem is treated under an investigative point of view, and the main (source level) propositions of interest can be whether or not the recovered traces come from the same source.

## 3 Graphical models

The recovered items of evidence should be evaluated in order to support investigators in their inquiry. Should the investigators focus on a unique perpetrator (source) of the recovered material or are more than one source involved in the cases? In order to perform
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

the evaluation correctly, a graphical representation of the relevant variables for the problem of interest may prove to be particularly convenient. Bayesian networks and object-oriented Bayesian networks are probabilistic graphical models that have been used for decades to study forensic problems $[4,5]$, and they are therefore used to analyze the proposed scenario.

# 3.1 Bayesian networks 

Bayesian networks (BN) are probabilistic graphical tools based on elements of graph and probability theory $[6,5]$ that allow one to deal with uncertainty in a coherent and rigorous manner. BNs are directed acyclic graphs (DAG) composed by a set of variables, represented by nodes, that model the entities of interest for the problem. The probabilistic relationships between two nodes are represented by directed edges (arrows). A conditional probability table is associated with each node, and shows the probabilities of the different states of the node conditioned by the states of its parent nodes, i.e. the nodes on which they directly depend. More formally, a BN illustrates the representation of the joint probability distribution for all the variables of the structured model. Moreover, because a BN is a complete model for all the variables of interest and their relationships, it can be used to answer probabilistic queries about them. For example, the network can be used to obtain updated knowledge of the states of a subset of variables when other variables are observed; this aspect is called probabilistic inference.
In the similar but simpler scenario treated in [3], the authors developed a Bayesian network for a case where $n=2$ traces were involved; the qualitative part of the Bayesian network was described by node $H$, accounting for the propositions of interest, nodes $S_{1}$ and $S_{2}$, considering the type ( $A$ or $\bar{A}$ ) of the true source of the first and second trace respectively, and nodes $E_{1}$ and $E_{2}$, representing the features of the first and second trace.
In this work, the network is extended to cases involving $n>2$ traces, and new nodes have been introduced in order to take the increased complexity of the scenario into account.
The developed network is shown in Figure 1, and Table 1 shows a summary of the different nodes and their definitions.
Here, node $H$ represents again the two propositions of interest. Its states are $H_{1}$ and $H_{2}$, formally defined as:

- $H_{1}$ : The $n$ traces come from the same source;
- $H_{2}$ : The $n$ traces come from at least two different sources,
where the number of possible different sources is not specified.
Node $K$ depends directly on node $H$. It represents the number of possible sources at the origin of the $n$ traces, and its states are all the numbers from 1 to $n$. If proposition $H_{1}$ is true, only one source is at the origin of the traces, so $\operatorname{Pr}\left(K=1 \mid H_{1}\right)=1$ and $\operatorname{Pr}\left(K \neq 1 \mid H_{1}\right)=0$. If $H_{2}$ is true, $\operatorname{Pr}\left(K=1 \mid H_{2}\right)=0$ and $\operatorname{Pr}\left(K=k \mid H_{2}\right)$, with $k=2 \ldots n$, represents the probability that exactly $k$ sources are involved knowing that the traces come
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-0.jpeg](img-0.jpeg)

Figure 1: Bayesian network for a scenario in which $n$ traces are found. New nodes have been introduced with respect to the network developed in [3], in particular the node $K$, accounting for the number of possible different sources, nodes $D_{i-1 \rightarrow i}$ that consider the dependency between the true sources of $(i-1)$ th and $i$ th traces, and the constraint node $C$ that allows the network to consider only the logically possible configurations.
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Table 1: Table representing the names of different nodes (1st column) of the Bayesian network (Figure 1), their definition (2nd column) and their states (3rd column).


from at least two different sources. This probability depends on the different configurations in which many sources can be at the origin of the $n$ traces. According to the considered scenario, all the potential sources, being unknown, are indistinguishable from one another. On the contrary, no assumption has been made on the crime scenes, which means that non-scientific information could exist, allowing one to model a probability distribution which considers the prior belief "two or more crime scenes are more related than others", which is the initial belief that the same source is at the origin of traces collected on two or more particular crime scenes. According to this consideration, all the crime scenes can be considered distinguishable and, for the sake of simplicity, they will be treated as equiprobable in this work. The number of ways in which the $n$ traces can come from exactly $k$ sources corresponds to the Stirling number of the second kind $\left\{\begin{array}{l}n \\ k\end{array}\right\}[7,8]$ which represents the number of ways in which a $n$-elements group can be partitioned in exactly $k$ subsets. The total number of ways in which $n$ traces can come from 2 to $n$ sources is $B_{n}-1$, where $B_{n}$ represents the $n$th Bell number ${ }^{1}[7,8] . \operatorname{Pr}\left(K=k \mid H_{2}\right)$ can therefore be written as $\operatorname{Pr}\left(K=k \mid H_{2}\right)=\left\{\begin{array}{l}n \\ k\end{array}\right\} / B_{n}-1$. The conditional probability table for node $K$ is shown in Table 2 .
Following the nodes' definitions presented in [3], the type of each trace recovered and of its true source are represented by nodes $E_{i}$ and $S_{i}(i=1 \ldots n)$ respectively. The states of these nodes are $A$ and $\bar{A}$, with $A$ being the considered discrete attribute (for example a given DNA profile). It is important to stress that the numbering of the traces ( 1 to $n$ ) and of their actual sources ( 1 to $n$ ) is not related to information issued from investigations (for example, the order of recovery). Numbers 1 to $n$ are only useful to label the traces, not to order them.

[^0](C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    ${ }^{1}$ The Stirling number of the second kind $\left\{\begin{array}{l}n \\ k\end{array}\right\}$ indicates the number of partitions of an $n$-elements set into $k$ non-empty subsets. It can be calculated using its explicit formula $\left\{\begin{array}{l}n \\ k\end{array}\right\}=\frac{1}{k!} \sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j} j^{n}$. The Bell number counts the number of partitions of an $n$-elements set, regardless the number of subsets. Bell number can be obtained as $\sum_{k=0}^{n}\left\{\begin{array}{l}n \\ k\end{array}\right\}$

Table 2: Conditional probability table for node $K$.


Each node $E_{i}(i=1 \ldots n)$ is dependent by the respective node $S_{i}$, and, since it is sensible to accept the assumption that if a source is of type $A$ then the trace recovered on the crime scene will be of the same type and assuming that no laboratory or manipulation errors occurred, $\operatorname{Pr}\left(E_{i}=A \mid S_{i}=A\right)=1$ and $\operatorname{Pr}\left(E_{i}=\bar{A} \mid S_{i}=A\right)=0$. Given the fact that the presence of at least one source at the origin of the traces recovered is certain, the first node of type $S\left(S_{1}\right)$ does not depend upon any other node. $\operatorname{Pr}\left(S_{1}=A\right)$ corresponds to the probability that a source of the relevant population is of type $A$, which can be written as $\gamma_{A}$. The conditional probability table for node $S_{1}$ is shown in Table 3.

Table 3: Conditional probability table for node $S_{1} . \gamma_{A}$ represents the probability that a source from the relevant population is of type $A$.


For a generic node $S_{i}$ with $i \neq 1$, the construction of the conditional probability table must consider if the $i$ th source is dependent (i.e. it is the same source) from one of the previous sources, represented by nodes $S_{i-1} \ldots S_{1}$. As stressed before, the fact of numbering the traces does not have any theoretical meaning, so it can be considered that all nodes $S_{i}$ representing the same source can be placed one after another. In this way, a generic node $S_{i}$ depends only on node $S_{i-1}$ and no more on nodes $S_{i-2} \ldots S_{1} . n-1$ nodes $D_{i-1 \rightarrow i}$ consider the a priori probability that the $(i-1)$ th and the $i$ th trace share a common source. The states of these nodes are defined by the symbols $\mid$ and $\circ$, the former meaning that the sources of the $(i-1)$ th and $i$ th traces are the same, and the latter that the two sources are different. Note that investigative information such as modus operandi or eyewitness evidence could play an important role in such probability assignments. Nevertheless, in the present work, the two states are considered equiprobable.
Information from nodes $D_{i-1 \rightarrow i}$ and from node $K$, representing the number of potential
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

sources, are combined into node $C$. Node $C$ is a constraint node [9] ${ }^{2}$ having two states, on and off, that has been introduced in order to allow the network to separate the $n$ nodes representing the true sources into $k$ groups, $k$ clearly being one of the states of node $K$. Node $C$ is conditioned by node $K$ and by all nodes $D_{i-1 \rightarrow i}$, and for a given number of traces $n$ it can be built as follows: given $k$ possible sources, a probability value of 1 to the state called on must be assigned to one of the sequences of $\mid$ and $\circ$ (states of nodes $\left.D_{1 \rightarrow 2} \ldots D_{n-1 \rightarrow n}\right)$ including exactly $k-1 \circ$. Note that any of the sequences respecting this rule can be valid: in fact, they all represent a situation involving exactly $k$ sources. The difference between the sequences lies in the size of the groups, i.e. in the number of traces coming from each source. Being this parameter not considered in this work, all the sequences can be considered equivalent ${ }^{3}$.
Given $k$ sources, there will be only $k-1$ nodes $S_{i}$ that will be independent from node $S_{i-1}$. This corresponds to a separation of the potential sources at the origin of traces in exactly $k$ groups.
Node $C$ has to be instantiated to its state on when using the Bayesian network. This has to be done in order to avoid the separation of nodes $S_{i}$ into a number of groups not coherent with the number of true sources fixed by node $K$. An example of the conditional probability table for node $C$ for a case of $n=4$ traces is presented in Table 4, and the conditional probability table for nodes $S_{i}$ is shown in Table 5.
This BN can be seen as a composition of two blocks: the first block consists of nodes $K, D$ and $C$ and focuses on how different sources can be at the origin of the traces; it is specific to every different $n$. The second block is formed by all couples of nodes $S_{i}$ and $E_{i}$ and considers the type of the recovered traces. According to this, the use of object-oriented Bayesian networks is very reasonable in our case.

# 3.2 Object-oriented Bayesian networks 

An object-oriented Bayesian network (OOBN) [10] can be seen as a hierarchically ordered BN. OOBNs are composed of a master network that includes instance nodes along with nodes as defined in the previous section. Instance nodes represent themselves a network fragment on a lower hierarchical level, and can be connected by using so-called input and output nodes, which allow the network to propagate the belief through different hierarchical levels. Instance nodes can be reused multiple times in the same master network, so OOBNs are particularly useful when dealing with problems that present a modular structure. With

[^0](C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    ${ }^{2}$ As stated in [9], it is possible to face a situation where a group of variables not directly dependent on each other cannot assume simultaneously a certain configuration of their states. This constraint can be modeled by using a constraint variable, which states reflect the legal and illegal configurations respectively. The constraint is enforced by instantiating the variable to the state that represents the allowed configurations.
    ${ }^{3}$ For example, in the case of $n=4$ traces and $k=2$ sources the allowed sequences are $\|\circ, \mid \circ \mid$ and $\circ\|$. In the first and third case, three traces come from a same source and one from the other, whilst in the second case two traces come from one source and two traces from another. The size of the group of traces sharing a common source changes, but always the same number of sources (in this case 2) is involved.

Published in final edited form as: Forensic Sci Int. 266 (2016) 527-533.
https://doi.org/10.1016/j.forsciint.2016.07.015

Table 4: Example of the conditional probability table for node $C$ for the case $n=4$ traces. In this case, given $n=4$ a probability of 1 to the state on is assigned to sequences $|\mid|$ for $k=1,|\mid \circ$ for $k=2, \mid \circ \circ$ for $k=3$ and $\circ \circ \circ$ for $k=4$.


Table 5: Conditional probability table for nodes $S_{i}$. Given that node $C$ must be instantiated to its state on, only this part of the table is represented here.


(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

respect to the BN, the OOBN has many structural and practical advantages, in particular it facilitates hierarchical construction, utilizing small modular networks (network fragments) as building blocks. The use of object-oriented Bayesian networks is largely attested in forensic science [5], in particular in problems dealing with DNA evidence [e.g., 11, 12, 13]. In the present scenario, it is possible to define a first instance node ( $n$ traces), representing a network's fragment composed by nodes $K, D_{i-1 \rightarrow i}$ and $C$ (see Figure 2a), which is specific to the number of traces $n$. Another instance node (Trace $i$ ) represents the part of the network composed by couples of nodes $S_{i}$ and $E_{i}$ (see Figure 2b), and a third instance node (Trace 1) which, similarly to the previous one, is composed by nodes $S_{1}$ and $E_{1}$ (see Figure 2c). The latter is necessary because probabilities on states of node $S_{1}$ do not depend upon any other variable.
It is possible to reconstruct the original Bayesian network by using the composition of these three instance nodes (Figure 3).
![img-1.jpeg](img-1.jpeg)
(a) Network's fragment represented by instance node $n$ traces.
![img-2.jpeg](img-2.jpeg)
(b) Network's fragment represented by instance node Trace $i$.
![img-3.jpeg](img-3.jpeg)
(c) Network's fragment represented by instance node Trace 1.

Figure 2: Bayesian network's fragments corresponding to the three instance nodes used to construct the object-oriented Bayesian network for the model. Input nodes are represented by gray dotted contoured circles, whilst output nodes are represented by gray contoured circles.

Irrespectively to the number of traces, the proper OOBN can be constructed combining the
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-4.jpeg](img-4.jpeg)

Figure 3: Structure of the object-oriented Bayesian network for $n$ traces. Instance nodes are represented by squares. Node $C$, defined inside the instance node $n$ traces, appears also in the master network. In this way, all nodes that must be instantiated when running the network are present on the master network.
three instance nodes previously defined.

# 4 Likelihood ratio formula 

In order to obtain a verification of the results obtained through graphical models, it is possible to develop an analytical formula for the likelihood ratio. It is important to stress that both the graphical models and the formula are based on the same assumptions. For this reason, the formula can be considered as a validation of the numerical results issued from the graphical models.
Remind that the hypothesis of interest are:

- $H_{1}$ : The $n$ traces come from the same source;
- $H_{2}$ : The $n$ traces come from at least two different sources,
where the number of possible different sources is not specified.
The likelihood ratio can therefore be written as:

$$
L R=\frac{\operatorname{Pr}\left(E_{1}=A, E_{2}=A, \ldots, E_{n}=A \mid H_{1}\right)}{\operatorname{Pr}\left(E_{1}=A, E_{2}=A, \ldots, E_{n}=A \mid H_{2}\right)}=\frac{\operatorname{Pr}\left(E \mid H_{1}\right)}{\operatorname{Pr}\left(E \mid H_{2}\right)}
$$

(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

where $E$ represents the event that all traces $E_{i}$, with $i=1 \ldots n$, share the same discrete characteristic $A$. In the following sections, the numerator and the denominator of the likelihood ratio will be studied separately.

# 4.1 Numerator 

The likelihood ratio's numerator, $\operatorname{Pr}\left(E \mid H_{1}\right)$ can be developed further by introducing a new variable $S$, that considers the type of the sources at the origin of the $n$ traces. The event $S=A$ corresponds to all the sources involved being of type $A$, and $S=\bar{A}$ is the event that at least one of the sources involved is not of type $A$. Obviously, given $H_{1}$ only one source is involved.
Therefore, the numerator can be extended as follows:

$$
\operatorname{Pr}\left(E \mid H_{1}\right)=\underbrace{\operatorname{Pr}\left(E \mid S=A, H_{1}\right)}_{1} \underbrace{\operatorname{Pr}\left(S=A \mid H_{1}\right)}_{\gamma_{A}}+\underbrace{\operatorname{Pr}\left(E \mid S=\bar{A}, H_{1}\right)}_{0} \operatorname{Pr}\left(S=\bar{A} \mid H_{1}\right)=\gamma_{A}
$$

In fact, under the proposition that the $n$ traces come from the same source, the probability of observing this kind of evidence knowing that the true source is of type $A$ is 1 , and the probability to observe the same traces knowing that their true source is of type $\bar{A}$ is 0 . The factor $\operatorname{Pr}\left(S=A \mid H_{1}\right)$ is equal to $\gamma_{A}$, which is again the probability that a source from the relevant population is of type $A[3]$.

### 4.2 Denominator

Similarly, the denominator can be written as

$$
\begin{aligned}
\operatorname{Pr}\left(E \mid H_{2}\right) & =\underbrace{\operatorname{Pr}\left(E \mid S=A, H_{2}\right)}_{1} \operatorname{Pr}\left(S=A \mid H_{2}\right)+\underbrace{\operatorname{Pr}\left(E \mid S=\bar{A}, H_{2}\right)}_{0} \operatorname{Pr}\left(S=\bar{A} \mid H_{2}\right) \\
& =\operatorname{Pr}\left(S=A \mid H_{2}\right)
\end{aligned}
$$

The probability that the sources at the origin of the traces are all of type $A$, knowing that the traces come from different sources, i.e. $\operatorname{Pr}\left(S=A \mid H_{2}\right)$, depends on the number of sources involved. The number of sources potentially at the origin of traces can vary between 1 and $n$, therefore
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

$$
\begin{aligned}
\operatorname{Pr}\left(S=A \mid H_{2}\right)= & \sum_{k=1}^{n} \operatorname{Pr}\left(S=A \mid K=k, H_{2}\right) \operatorname{Pr}\left(K=k \mid H_{2}\right) \\
= & \operatorname{Pr}\left(S=A \mid K=1, H_{2}\right) \underbrace{\operatorname{Pr}\left(K=1 \mid H_{2}\right)}_{0} \\
& \quad+\sum_{k=2}^{n} \operatorname{Pr}\left(S=A \mid K=k, H_{2}\right) \operatorname{Pr}\left(K=k \mid H_{2}\right)
\end{aligned}
$$

$\operatorname{Pr}\left(S=A \mid K=k, H_{2}\right)$ denotes the probability that all the sources are of the same type $A$ knowing that exactly $k$ sources are involved. If the $k$ sources are assumed to be independent to each other, this term is equal to $\gamma_{A}{ }^{k}$.
$\operatorname{Pr}\left(K=k \mid H_{2}\right)$ represents the probability that exactly $k$ sources are involved knowing that the traces come from different sources.
As explained in Section 3, this probability depends on the number of different configurations in which $k$ sources can be at the origin of $n$ traces. $\operatorname{Pr}\left(K=k \mid H_{2}\right)$ can therefore be written as $\operatorname{Pr}\left(K=k \mid H_{2}\right)=\left\{\begin{array}{l}n \\ k\end{array}\right\} / B_{n}-1$. Equation 1 becomes then:

$$
\sum_{k=2}^{n} \operatorname{Pr}\left(S=A \mid K=k, H_{2}\right) \operatorname{Pr}\left(K=k \mid H_{2}\right)=\sum_{k=2}^{n} \gamma_{A}^{k} \frac{\left\{\begin{array}{l}
n \\
k
\end{array}\right\}}{B_{n}-1}
$$

and the likelihood ratio's formula for the scenario considered is finally:

$$
L R=\frac{\gamma_{A}}{\frac{1}{B_{n}-1} \sum_{k=2}^{n}\left\{\begin{array}{l}
n \\
k
\end{array}\right\} \gamma_{A}^{k}}
$$

# 5 Model application 

In order to illustrate how the $n$ traces model works, a case involving $n=4$ traces will be described.
Assuming a probability $\gamma_{A}=0.2$, the proper BN and OOBN are shown in Figure 4.
The same result can be obtained by using equation (2), that can be written as:

$$
\begin{aligned}
L R & =\frac{0.2}{\frac{1}{B_{4}-1} \sum_{k=2}^{4}\left\{\begin{array}{l}
4 \\
k
\end{array}\right\} 0.2^{k}} \\
& =\frac{0.2}{\frac{1}{14}\left[7 \cdot 0.2^{2}+6 \cdot 0.2^{3}+1 \cdot 0.2^{4}\right]} \\
& =\frac{0.2}{0.0235} \\
& =8.5
\end{aligned}
$$

(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-5.jpeg](img-5.jpeg)

Figure 4: Bayesian networks (top) and object-oriented Bayesian networks (bottom) for $n=4$ traces. On the left, node $H$ is instantiated to its state $H_{1}$, and probability associated to state $A$ of node $E$ corresponds to the likelihood ratio's numerator. On the right, node $H$ is instantiated to its state $H_{2}$, and so variable $E$ 's state $A$ corresponds to likelihood ratio's denominator.
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Simulations conducted using a number of traces varying between two and ten with a fixed value of $\gamma_{A}$ show that results obtained with the formula 2 coincide with those obtained when using Bayesian networks and object-oriented Bayesian networks. Furthermore, results obtained in [3] coincide with those obtained when using this model in the particular case of $n=2$ traces.
In Figure 5, the LR as a function of probability $\gamma_{A}$ is represented in correspondence of an increasing number of traces.
![img-6.jpeg](img-6.jpeg)

Figure 5: Logarithm of likelihood ratio as a function of probability $\gamma_{A}$ for $n=2,4,6,8$ and 10 traces

As expected, the LR decreases as values of $\gamma_{A}$ increase regardless of the number of traces recovered, but it always supports the proposition $H_{1}$.
It can also be observed that the number of traces plays a minor role when probability $\gamma_{A}$ is high (i.e. when the considered characteristic $A$ is common in the relevant population), whilst, for lower values of $\gamma_{A}$, the number of traces has a strong impact on the LR's magnitude.
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

# 6 Discussion and conclusions 

The evaluation of a comparative analysis of multiple pieces of evidence can be of high interest from a forensic point of view, even though a putative source of the traces is not available, notably in investigative settings. For example, this kind of approach can allow the forensic scientist to provide some case linkage, which can be extremely helpful in both an investigative and an evaluative framework [14]. Taroni et al. [3] already discussed the problem in the case of two items of evidence, for both discrete and continuous trace characteristics. Through this paper, the inferential model was extended in order to consider a number of items of evidence possessing discrete attributes greater than two $(n>2)$. Developments were performed based on graphical models, namely Bayesian networks and object-oriented Bayesian networks. Additionally, an analytical formula for the LR was developed, in order to verify the results issued from the graphical models.
Though the LR is usually applied to evaluate the weight of an item of evidence given two competing propositions involving a putative source, its use in investigative frameworks is widely attested [see, e.g. 15]. The current work further supports the use of LR as a powerful statistical tool that can provide relevant information also in an early stage of the investigations process.
The study shows that, besides the mathematical equations, the use of Bayesian networks allows one to structure the inferential problem of interest in a rigorous manner by expressing dependencies between the variables involved in the problem. Therefore, this probabilistic tool facilitates the handling of uncertainty related to the problem in a logical and coherent way, which does not request any particular expertise in statistics or mathematics. This is a great advantage for the forensic practitioners and experts, since they could focus on the evaluation procedure rather than on mathematical computation. The flexible nature of Bayesian networks is highlighted when dealing with multiple items of evidence. The model is extended taking advantage of repetitive sub-structures; in this respect, OOBN is adapted in a particular way.
These results have to undoubtedly be interpreted in the light of the assumptions only. In particular, one should not consider circumstantial and investigative information in the model, even though it could provide substantial elements to interpret the case more accurately. A further development of the model investigating the influence of non scientific elements such as the modus operandi or location of the traces on the crime scenes can therefore be envisaged.
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/
