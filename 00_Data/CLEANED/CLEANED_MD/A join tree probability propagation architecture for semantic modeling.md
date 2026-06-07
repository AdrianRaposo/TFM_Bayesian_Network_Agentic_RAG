# A join tree probability propagation architecture for semantic modeling 

C. J. Butz $\cdot$ H. Yao $\cdot$ S. Hua

Received: 29 September 2006 / Revised: 19 November 2007 /
Accepted: 22 August 2008 / Published online: 25 September 2008
(C) The Author(s) 2008. This article is published with open access at Springerlink.com


#### Abstract

We propose the first join tree (JT) propagation architecture that labels the probability information passed between JT nodes in terms of conditional probability tables (CPTs) rather than potentials. By modeling the task of inference involving evidence, we can generate three work schedules that are more time-efficient for LAZY propagation. Our experimental results, involving five real-world or benchmark Bayesian networks (BNs), demonstrate a reasonable improvement over LAZY propagation. Our architecture also models inference not involving evidence. After the CPTs identified by our architecture have been physically constructed, we show that each JT node has a sound, local BN that preserves all conditional independencies of the original BN. Exploiting inference not involving evidence is used to develop an automated procedure for building multiply sectioned BNs. It also allows direct computation techniques to answer localized queries in local BNs, for which the empirical results on a real-world medical BN are promising. Screen shots of our implemented system demonstrate the improvements in semantic knowledge.


Keywords Bayesian networks $\cdot$ Join trees $\cdot$ Probabilistic inference $\cdot$
Conditional independence

## 1 Introduction

Bayesian networks (BNs) (Castillo et al. 1997; Cowell et al. 1999; Hájek et al. 1992; Jensen 1996; Neapolitan 1990; Pearl 1988; Xiang 2002) are a clear and concise

[^0]
[^0]:    C. J. Butz $(\boxtimes) \cdot$ H. Yao $\cdot$ S. Hua

    Department of Computer Science, University of Regina, Regina, S4S 0A2, Canada
    e-mail: butz@cs.uregina.ca
    H. Yao
    e-mail: yao2hong@cs.uregina.ca
    S. Hua
    e-mail: huash111@cs.uregina.ca

semantic modeling tool for managing uncertainty in complex domains. A BN consists of a directed acyclic graph (DAG) and a corresponding set of conditional probability tables (CPTs). The probabilistic conditional independencies (Wong et al. 2000) encoded in the DAG indicate that the product of the CPTs is a joint probability distribution (JPD). Although Cooper (1990) has shown that the complexity of exact inference in BNs is NP-hard, several approaches have been developed that apparently work quite well in practice. One approach, called multiply sectioned Bayesian networks (MSBNs) (Xiang 1996, 2002; Xiang and Jensen 1999; Xiang et al. 2006, 2000, 1993), performs inference in sections of a BN. A second approach, called direct computation (DC) (Dechter 1996; Li and D'Ambrosio 1994; Zhang 1998), answers queries directly in the original BN. Although we focus on a third approach called join tree propagation, in which inference is conducted in a join tree (JT) (Pearl 1988; Shafer 1996) constructed from the DAG of a BN, our work has practical applications in all three approaches.

Shafer emphasizes that JT probability propagation is central to the theory and practice of probabilistic expert systems (Shafer 1996). JT propagation passes information, in the form of potentials, between neighbouring nodes in a systematic fashion. Unlike a CPT, a potential (Hájek et al. 1992) is not clearly interpretable (Castillo et al. 1997) as the probability values forming the distribution may have no recognizable pattern or structure. In an elegant review of traditional JT propagation (Shafer 1996), it is explicitly written that while independencies play an important role in semantic modeling, they do not play a major role in JT propagation. We argue that they should.

By iterating between semantic modeling and computing the actual probability distributions in computer memory, the JT propagation algorithm suggested by Madsen and Jensen (1999), called LAZY propagation, is a significant advancement in the study of JT propagation. Unlike traditional approaches, LAZY propagation maintains structure in the form of a multiplicative factorization of the potentials at each JT node and each JT separator. Thereby, when a node is ready to send its messages to a neighbour, the structure is modeled to remove irrelevant potentials from the multiplicative factorization by exploiting barren variables (Shachter 1986) and independencies induced by evidence. Next, physical computation is performed on the relevant potentials. Performing semantic modeling before physical computation improves the efficiency of inference, as the experimental results presented in Madsen and Jensen (1999) explicitly demonstrate. With respect to the computational efficiency at the sending node, any remaining independencies, in the relevant potentials, are immaterial. On the contrary, by ignoring these independencies, LAZY propagation is not able to precisely articulate the probability information being passed from one node to another. Passing potentials not only hinders the identification of barren variables at the receiving node, but also blurs the exact probability information remaining at each JT node when propagation finishes. More importantly, iterating between semantic modeling and physical computation essentially guarantees that LAZY performs JT probability propagation more slowly than necessary.

In this study, we propose the first JT propagation architecture for modeling two tasks of inference, one involving evidence and the other not. Our architecture, itself, does not construct the actual probability distributions stored in computer memory. Instead, it labels the probability information to be propagated more precisely in terms of CPTs. The notions of parent-set and elder-set are introduced in order to

identify independencies that are not utilized in previous architectures. The identified independencies are very useful, since they allow us to maintain a CPT factorization after a variable is eliminated. When a JT node is ready to send its messages to a neighbour, it calls the IdentifyCPTMessages (ICM) algorithm to determine the CPT labels corresponding to the probability information to be sent to the neighbour, that is, without building the actual probability tables in computer memory. We prove the correctness of our architecture and also show that each JT node can identify its CPT labels in polynomial time. Screen shots of our implemented system demonstrate the improvements in semantic knowledge.

As discussed in Section 5, modeling the processing of evidence is beneficial as our architecture is able to identify relevant and irrelevant messages faster than it takes other propagation algorithms to construct the actual probability distributions in the memory. In a real-world BN for coronary heart disease (CHD) (Hájek et al. 1992), for instance, our architecture can identify all messages in the JT in less time than it takes to physically construct the distribution for one message. We make use of this semantic knowledge to generate three work schedules for LAZY propagation. Our first work schedule identifies irrelevant non-empty messages. This information is very useful, since LAZY's lack of semantic knowledge could force a receiving node to wait for the physical construction of a message that is irrelevant to its subsequent message computation. Our second work schedule indicates the empty messages to be propagated from non-leaf JT nodes. This has merit as LAZY could force a receiving node to wait for the identification of an empty message that will not even be constructed, let alone sent. Our third work schedule also helps LAZY finish sooner by pointing out those variables that can be eliminated at a non-leaf node before the node has received any messages. Thus, our three work schedules save time, which is the measure used to evaluate inference methods in Madsen and Jensen (1999). As reported in Tables 2, 3 and 4, our empirical results, involving processing the evidence in five real-world or benchmark BNs, are encouraging.

Our architecture is also useful for modeling inference not involving evidence. As shown in Section 6, after the CPTs identified by our architecture have been physically constructed, say, by either of the methods in Madsen and Jensen (1999); Zhang (1998), each JT node has a sound, local BN preserving all conditional independencies of the original BN involving variables in this node. These local BNs are useful to the MSBN and to the DC techniques. We show that our JT propagation architecture is instrumental in developing an automated procedure for constructing a MSBN from a given BN. This is a worthwhile result, since several problems with the manual construction of a MSBN from a BN have recently been acknowledged (Xiang et al. 2000). We also suggest a method for exploiting localized queries in DC techniques. Practical experience has demonstrated that queries tend to involve variables in close proximity within a BN (Xiang et al. 1993). Our approach allows DC to process localized queries in local BNs. As a result, the experimental results involving a realworld BN for CHD show promise.

This paper is organized as follows. Section 2 contains definitions. Our semantic architecture for JT probability propagation is given in Section 3. Complexity analysis and the correctness of our architecture are established in Section 4. In Section 5, we model the task of inference involving evidence and show its usefulness in practice. In Section 6, we show the practical benefits of modeling inference not involving evidence. The conclusion is given in Section 7.

# 2 Definitions 

Let $U=\left\{v_{1}, v_{2}, \ldots, v_{m}\right\}$ be a finite set of variables. Each variable $v_{i}$ has a finite domain, denoted $\operatorname{dom}\left(v_{i}\right)$, representing the values $v_{i}$ can assume. For a subset $X \subseteq U$, we write $\operatorname{dom}(X)$ for the Cartesian product of the domains of the individual variables in $X$. Each element $x \in \operatorname{dom}(X)$ is called a configuration of X .

Definition 1 A potential (Hájek et al. 1992) on $\operatorname{dom}(X)$ is a function $\phi$ on $\operatorname{dom}(X)$ such that $\phi(x) \geq 0$, for each configuration $x \in \operatorname{dom}(X)$, and at least one $\phi(x)$ is positive.

For example, five potentials $\phi(b), \phi(f, g), \phi(g, h), \phi(f)$ and $\phi(g)$ are illustrated in Fig. 1.

Definition 2 For variable $v_{i}$, a unity-potential $1\left(v_{i}\right)$ is a potential 1 assigning value 1.0 to each configuration of $v_{i}$. For a subset $X \subseteq U$, the unity-potential $1(X)$ is defined as the product of the unity-potentials $1\left(v_{i}\right), v_{i} \in X$.

For brevity, we refer to a potential as a probability distribution on $X$ rather than $\operatorname{dom}(X)$, and we call $X$, not $\operatorname{dom}(X)$, its domain (Shafer 1996). Also, for simplified notation, we may write a set $\left\{v_{1}, v_{2}, \ldots, v_{k}\right\}$ as $v_{1} v_{2} \cdots v_{k}$ and use $X Y$ to denote $X \cup Y$.

Definition 3 A $J P D$ (Shafer 1996) on $U$, denoted $p(U)$, is a potential on $U$ that sums to one.

Definition 4 Given $X \subset U$, a $C P T$ (Shafer 1996) for a variable $v \notin X$ is a distribution, denoted $p(v \mid X)$, satisfying the following condition: for each configuration $x \in \operatorname{dom}(X), \sum_{c \in \operatorname{dom}(v)} p(v=c \mid X=x)=1.0$.

For example, given binary variables $U=\{a, b, \ldots, k\}$, CPTs $p(a), p(b \mid a), p(c)$, $p(d \mid c), p(e \mid c), p(f \mid d, e), p(g \mid b, f), p(h \mid c), p(i \mid h), p(j \mid g, h, i)$ and $p(k \mid g)$ are depicted in Fig. 2. The missing conditional probabilities can be obtained by definition, for instance, $p(a=0)=0.504$ and $p(b=0 \mid a=0)=0.943$.

Definition 5 The label of a probability distribution is the heading appearing above the probability column.

For example, the five probability distributions in Fig. 1 can be more precisely labeled as $p(b), p(g \mid f), p(g, h), p(f)$ and $p(g)$, respectively.


Fig. 1 Five potentials $\phi(b), \phi(f, g), \phi(g, h), \phi(f)$ and $\phi(g)$


Fig. 2 CPTs $p(a), p(b \mid a), p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(g \mid b, f), p(h \mid c), p(i \mid h), p(j \mid g, h, i)$ and $p(k \mid g)$

Definition 6 Let $x, y$ and $z$ denote arbitrary configurations of pairwise disjoint subsets $X, Y, Z$ of $U$, respectively. We say $X$ and $Z$ are conditionally independent (Wong et al. 2000) given $Y$ under the JPD $p(U)$, denoted $I(X, Y, Z)$, if $p(X=$ $x \mid Y=y, Z=z)=p(X=x \mid Y=y)$, whenever $p(Y=y, Z=z)>0$. If $Y=\emptyset$, then we say $X$ and $Z$ are unconditionally independent. The independence $I(X, Y, Z)$ can be equivalently written as $p(X, Y, Z)=\frac{p(X, Y), p(Y, Z)}{p(Y)}$.

Definition 7 A Markov blanket (Pearl 1988) of a variable $v \in U$ is any subset of variables $X \subset U$ with $v \notin X$ such that the independence $I(v, X, U-X-v)$ holds in $p(U)$.

Definition 8 A $B N$ (Pearl 1988) on $U$ is a pair $(D, C) . D$ is a DAG on $U . C$ is a set of CPTs defined as: for each variable $v_{i} \in D$, there is a CPT for $v_{i}$ given its parents.

Note that, for each CPT in the BN, there is a corresponding CPT labe. The family of a variable in the DAG of a BN is the variable and its parents. We may use the terms BN and $D A G$ interchangeably, if no confusion arises.

Example 1 One real-world BN for CHD (Hájek et al. 1992) is shown in Fig. 3, where the CPTs are given in Fig. 2. For pedagogical reasons, we have made the following minor adjustments: edge $(a, f)$ has been removed; edges $(c, f)$ and $(g, i)$ have been replaced with edges $(c, d),(c, e),(d, f),(e, f)$ and $(g, j)$, respectively, where $d$ and $e$ are dummy variables.

Definition 9 A numbering $\prec$ of the variables in a DAG is called ancestral (Castillo et al. 1997), if the number corresponding to any variable $v_{i}$ is lower than the number corresponding to each of its children $v_{j}$, denoted $v_{i} \prec v_{j}$.

Definition 10 The moralization (Pearl 1988) of a DAG $D$ is the undirected graph obtained by making the family of each variable in $D$ complete.

Given pairwise disjoint subsets of variables $X, Y, Z$ in a DAG $D$, the independence $I(X, Y, Z)$ holds in $D$ (Lauritzen et al. 1990), if $Y$ separates $X$ and $Z$ in the moralization of $D^{\prime}$, where $D^{\prime}$ is the sub-DAG of $D$ restricted to the edges $\left(v_{i}, v_{j}\right)$ such that $v_{i}, v_{j}$ are in $X Y Z \cup \operatorname{An}(X Y Z)$, and where $\operatorname{An}(X Y Z)$ denotes the ancestors

Fig. 3 The coronary heart disease (CHD) BN (Hájek et al. 1992) in Example 1
![img-0.jpeg](img-0.jpeg)
of $X Y Z$ in $D$. The independencies encoded in $D$ indicate that the product of the CPTs in $C$ is a JPD. For instance, the independencies encoded in the DAG of Fig. 3 indicate that the product of the CPTs in Fig. 2 is a JPD on $U=\{a, b, c, d, \ldots, k\}$, namely, $p(U)=p(a) \cdot p(b \mid a) \cdot p(c) \cdot p(d \mid c) \cdot \ldots \cdot p(k \mid g)$.

Probabilistic inference, also known as query processing, means computing $p(X)$ or $p(X \mid E=e)$, where $X \cap E=\emptyset$ and $X, E \subseteq U$. The evidence in the latter query is that $E$ is instantiated to configuration $e$, while $X$ contains target variables. Barren variables can be exploited in inference (Shachter 1986).

Definition 11 A variable is barren (Madsen and Jensen 1999), if it is neither an evidence nor a target variable and either it has no descendants or (recursively) all its descendants are barren.

As discussed in Section 6, probabilistic inference can be conducted directly in an entire BN or in parts of a BN. It can also be conducted in a JT (Jensen et al. 1990; Lauritzen and Spiegelhalter 1988; Madsen and Jensen 1999; Shafer and Shenoy 1990).

Definition 12 A $J T$ (Pearl 1988; Shafer 1996) is a tree having sets of variables as nodes, with the property that any variable in two nodes is also in any node on the path between the two. The separator (Shafer 1996) $S$ between any two neighbouring nodes $N_{i}$ and $N_{j}$ is $S=N_{i} \cap N_{j}$. A JT node with only one neighbour is called a leaf (Shafer 1996); otherwise it is a non-leaf node.

Constructing a minimal JT is NP-complete (Yannakakis 1981). The reader is referred to (Becker and Geiger 2001; Kjaerulff 1990; Olesen and Madsen 2002) for discussions on constructing a JT from a BN. For example, one possible JT for the DAG in Fig. 3 is depicted in Fig. 4 (ignoring the messages for the moment). We label the nodes of this JT as $a b, b f g$, cdefgh, ghij and $g k$. The separators of this JT are $b$, $f g, g h$ and $g$.

Fig. 4 LAZY propagates potentials $\phi(b), \phi(f, g)$, $\phi(g, h), \phi(f)$ and $\phi(g)$
![img-1.jpeg](img-1.jpeg)

Although JT propagation can be performed serially, our discussion here is based on parallel computation (Kozlov and Singh 1999; Madsen and Jensen 1999; Shafer 1996). We provide a quick overview of the Shafer-Shenoy (SS) architecture for probability propagation in JTs (Shafer and Shenoy 1990; Shafer 1996). Each JT node $N$ has exactly one potential $\phi(N)$, which is defined by the product of the unitypotential $1(N)$ and all of the BN CPTs assigned to $N$. The SS architecture allocates two storage registers in each separator, one for a message sent in each direction. Each node sends messages to all its neighbours, according to the following two rules. First, each node waits to send its message to a particular neighbour until it has received messages from all its other neighbours. Second, when a node $N_{i}$ is ready to send its message to a particular neighbour $N_{j}$, it computes the message $\phi\left(N_{i} \cap N_{j}\right)$ by collecting all its messages from other neighbours, multiplying its potential $\phi\left(N_{i}\right)$ by these messages, and marginalizing the product to $N_{i} \cap N_{j}$.

The LAZY architecture, proposed by Madsen and Jensen (1999), is more sophisticated than the SS architecture, in that it maintains a multiplicative factorization of potentials at each JT node and each JT separator. Modelling structure in this manner leads to significant computational savings (Madsen and Jensen 1999). For ease of exposition, evidence will not be considered here, but later, in Section 5. When LAZY propagation terminates, the potentials at each JT node $N$ are a factorization of the marginal $p(N)$ of $p(U)$. Example 2 illustrates the messages passed in LAZY and the probability information that remains after propagation.

Example 2 Consider the CHD BN in Fig. 3 and one possible JT with assigned CPTs in Fig. 4. The distributions of the five potentials $\phi(b), \phi(f, g), \phi(g, h), \phi(f)$ and $\phi(g)$ in Fig. 4, passed in LAZY propagation, are illustrated in Fig. 1. After propagation the marginal distribution at each node is:

$$
\begin{aligned}
p(a, b) & =p(a) \cdot p(b \mid a) \\
p(b, f, g) & =p(g \mid b, f) \cdot \phi(b) \cdot \phi(f) \\
p(c, d, e, f, g, h) & =p(c) \cdot p(d \mid c) \cdot p(e \mid c) \cdot p(f \mid d, e) \cdot p(h \mid c) \cdot \phi(f, g) \\
p(g, h, i, j) & =p(i \mid h) \cdot p(j \mid g, h, i) \cdot \phi(g, h) \\
p(g, k) & =p(k \mid g) \cdot \phi(g)
\end{aligned}
$$

# 3 Modeling inference not involving evidence 

In this paper, we are interested in identifying the probability information passed during propagation and that which remains after propagation terminates. Although LAZY propagation can efficiently compute the five distributions in Fig. 1, it does not clearly articulate the semantics of the messages being propagated between JT nodes. For instance, it can be verified that the potential $\phi(f, g)$ in Fig. 1 is, in fact, the CPT $p(g \mid f)$ of $p(U)$. To address these problems, instead of developing yet another architecture for probabilistic inference, our architecture models probabilistic inference.

Our simple architecture identifies the probability information being passed between JT nodes. It uses five rules, given below, for filling the storage registers in the JT separators with CPT or unity-potential labels. The key to our architecture is the ICM algorithm used in Rule 4. Before starting JT propagation, each CPT label $p(v \mid X)$ in the original BN is assigned to exactly one JT node $N$, where $N$ contains the variables in $\{v\} \cup X$.

Rule 1. For every variable in every separator, allocate two empty storage registers, one for a label in each direction.
Rule 2. Fix an ancestral numbering $\prec$ of the variables in the BN.
Rule 3. Each node $N_{i}$ waits to identify its label(s) to a given neighbour until all of $N_{i}$ 's other neighbours have filled their storage registers to $N_{i}$.
Rule 4. When a node $N_{i}$ is able to send the label(s) to a neighbour $N_{j}$, it calls the ICM algorithm, passing its assigned CPT labels and all CPT labels received by the storage registers from its other neighbours to $N_{i}$, as well as the variables $N_{i}-N_{j}$ to be eliminated.
Rule 5. For each CPT label $p\left(v_{k} \mid P_{k}\right)$ returned by ICM, fill the storage register for variable $v_{k}$ from $N_{i}$ to $N_{j}$ with label $p\left(v_{k} \mid P_{k}\right)$. For any variable $v_{l}$ with a storage register from $N_{i}$ to $N_{j}$ still empty, fill the register with the unitypotential label $1\left(v_{l}\right)$.

We illustrate Rules 1-3 with the following example.
Example 3 Consider the JT with assigned BN CPTs in Fig. 5. By Rule 1, the separator $g h$ in Fig. 4, for instance, has four storage registers in Fig. 5, which initially are empty. For Rule 2, we fix the ancestral numbering as $a \prec b \prec \ldots \prec k$. According to Rule 3, node bfg, for example, can only send labels to node $a b$ after the message labels have been received by the storage registers from its other neighbours to bfg, namely, the storage registers from both nodes cdefgh and $g k$ to bfg. In other words, Rule 3 means leaf JT nodes are ready to identify their messages immediately.

The ICM algorithm is built upon the FindRelevantCPTs (FRC) and MaintainCPTLabels (MCL) algorithms.

Definition 13 Given a set $C$ of CPT labels and a variable $v_{i}$ to be eliminated, the FindRelevantCPTs (FRC) algorithm returns the set $C^{\prime}$ of CPT labels in $C$ involving $v_{i}$, where FRC first sorts the CPT labels in $C^{\prime}$ according to $\prec$ in Rule 2, say $C^{\prime}=$ $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$, where $v_{i} \prec v_{1} \prec \ldots \prec v_{k}$.

Fig. 5 Unlike Fig. 4, our architecture precisely articulates the probability information being passed between JT nodes
![img-2.jpeg](img-2.jpeg)

Example 4 Suppose FRC is called with $C=\{p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(h \mid c)\}$ and variable $d$ is to be eliminated. By $\prec$ in Example 3, FRC returns $C^{\prime}=\{p(d \mid c)$, $p(f \mid d, e)\}$ and not $C^{\prime}=\{p(f \mid d, e), p(d \mid c)\}$.

Definition 14 To eliminate $v_{i}$, suppose FRC returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots\right.$, $\left.p\left(v_{k} \mid P_{k}\right)\right\}$. Consider a variable $v_{j} \in v_{i} v_{1} \cdots v_{k}$. The parent-set of $v_{j}$ is $P_{j}$.

Example 5 To eliminate $c$, suppose FRC returns $\{p(c), p(e \mid c), p(f \mid c, e), p(h \mid c)\}$. The parent-sets of variables $c, e, f$ and $h$ are $\}\},\{c\},\{c, e\}$ and $\{c\}$, respectively.

Definition 15 Suppose FRC returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$ for eliminating variable $v_{i}$. We call $C_{i}=\left\{v_{1}, \ldots, v_{k}\right\}$ the child-set of $v_{i}$, where $v_{1} \prec \ldots \prec v_{k}$ in Rule 2 .

Example 6 To eliminate $c$, suppose FRC returns $\{p(c), p(d \mid c), p(e \mid c), p(h \mid c)\}$. Besides $p(c)$, variable $c$ appears in the CPT labels for $\{h, d, e\}$. By $\prec$ in Example 3, $e \prec h$, while $d \prec e$. By definition, the child-set of $v_{i}=c$ is $C_{i}=\left\{v_{1}=d, v_{2}=e, v_{3}=h\right\}$.

To eliminate $v_{i}$, given that FRC returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$, those CPT labels $p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)$ of the variables $v_{j} \in C_{i}$ are modified. While variable $v_{i}$ is deleted from $P_{j}$, only certain variables preceding $v_{j}$ in $\prec$ of Rule 2 may be added to $P_{j}$.

Definition 16 To eliminate $v_{i}$, suppose FRC returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid\right.\right.$ $\left.\left.P_{k}\right)\right\}$. Consider a variable $v_{j} \in v_{i} v_{1} \cdots v_{k}$. The family-set, denoted $F_{j}$, of $v_{j}$ is $v_{j} P_{j}$.

Example 7 To eliminate $c$, suppose FRC returns $\{p(c), p(e \mid c), p(f \mid c, e), p(h \mid c)\}$. The family-sets of variables $c, e, f$ and $h$ are $\{c\},\{c, e\},\{c, e, f\}$ and $\{c, h\}$, respectively.

Definition 17 Given a set of CPT labels $\left\{p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{m} \mid P_{m}\right)\right\}$, the directed graph defined by these CPT labels, called the CPT-graph, has variables $F_{1} \cdots F_{m}$, and a directed edge from each variable in $P_{k}$ to $v_{k}, k=1, \ldots, m$.

Fig. 6 The CPT-graph defined by the CPT labels in Example 8
![img-3.jpeg](img-3.jpeg)

Example 8 Consider the set of CPT labels $\{p(a), p(c \mid a), p(d), p(e \mid b), p(g \mid d), p(h)$, $p(j \mid c, d, e), p(k \mid c, d, e, h, j), p(l \mid c, d, e, h, i, j, k), p(m \mid j)\}$. The CPT-graph is shown in Fig. 6. Note that variables $b$ and $i$ do not have CPT labels in the given set.

Definition 18 To eliminate $v_{i}$, suppose FRC returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid\right.\right.$ $\left.P_{k}\right)\right\}$. The child-set $C_{i}=\left\{v_{1}, \ldots, v_{k}\right\}$ is defined by $\prec$ in Rule 2. For each variable $v_{j} \in C_{i}$, the elder-set $E_{j}$ is defined as $E_{1}=F_{i}-v_{i}, E_{2}=\left(E_{1} F_{1}\right)-v_{i}, E_{3}=\left(E_{2} F_{2}\right)-$ $v_{i}, \ldots, E_{k}=\left(E_{k-1} F_{k-1}\right)-v_{i}$.

For simplified notation, we will write $\left(E_{j} F_{j}\right)-v_{i}$ as $E_{j} F_{j}-v_{i}$. Definition 18 says that the elder-set $E_{j}$ of variable $v_{j}$ in $C_{i}$ is $F_{i}$ together with the family-sets of the variables in $C_{i}$ preceding $v_{j}$, with $v_{i}$ subsequently removed.

Example 9 Consider the set of CPT labels $\{p(a), p(c \mid a), p(d), p(e \mid b), p(f \mid c, d)$, $p(g \mid d), p(h), p(j \mid e, f), \quad p(k \mid d, f, h), p(l \mid f, i), p(m \mid j)\}$. The CPT-graph defined by these CPT labels is shown in Fig. 7. Let us assume that $\prec$ in Rule 2 orders this subset of variables in alphabetical order. Consider eliminating variable $v_{i}=f$. The call to FRC returns $\{p(f \mid c, d), p(j \mid e, f), p(k \mid d, f, h), p(l \mid f, i)\}$. With respect to $\prec$ in Rule 2, the elder-set of each variable in the child-set $C_{i}=\left\{v_{1}=j, v_{2}=k, v_{3}=l\right\}$ is $E_{1}=\{c, d\}, E_{2}=\{c, d, e, j\}$ and $E_{3}=\{c, d, e, h, j, k\}$, as depicted in Fig. 7.

Fig. 7 With respect to variable $v_{i}=f$, illustrating the elder-set $E_{1}, E_{2}$ and $E_{3}$ for each variable in the child-set $C_{i}=\left\{v_{1}=j, v_{2}=k, v_{3}=l\right\}$ in Example 9. Note that one Markov blanket of $f$ is $E_{3} F_{3}$
![img-4.jpeg](img-4.jpeg)

The MCL algorithm now can be introduced.

```
Algorithm \(1 \mathrm{MCL}\left(C^{\prime}\right)\)
Input: \(C^{\prime}=\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}\) from FRC for eliminating \(v_{i}\)
Output: the modified CPT labels for all \(k\) variables \(v_{j}\) in \(C_{i}=\left\{v_{1}, \ldots, v_{k}\right\}\)
begin
Determine the elder-set \(E_{j}\) and parent-set \(P_{j}\) for all \(k\) variables \(v_{j} \in C_{i}\)
for \(j=k, \ldots, 1\)
    \(P_{j}=\left(E_{j} P_{j}\right)-v_{i}\)
return \(\left(\left\{p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}\right)\)
end
```

For simplified notation, we will write $\left(E_{j} P_{j}\right)-v_{i}$ as $E_{j} P_{j}-v_{i}$.

Example 10 To eliminate variable $v_{i}=f$, suppose the set of CPT labels obtained by FRC in Example 9 is passed to MCL. For $\prec$ in Example 9, consider variable $v_{3}=l$. By definition, $E_{3}=\{c, d, e, h, j, k\}$ and $P_{3}=\{f, i\}$. Then $p(l \mid f, i)$ is adjusted to $p(l \mid c, d, e, h, i, j, k)$, as $E_{3} P_{3}-v_{i}$ is $\{c, d, e, h, i, j, k\}$. Similarly, $p(k \mid d, f, h)$ is changed to $p(k \mid c, d, e, h, j)$, and $p(j \mid e, f)$ is modified to $p(j \mid c, d, e)$. By Definition 17, the CPTgraph defined by the CPT labels remaining after the elimination of variable $f$ is shown in Fig. 6.

Lemma 1 According to our architecture, let $C^{\prime \prime}=\left\{p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$ be the set of CPT labels returned by the MCL algorithm. Then the CPT-graph defined by $C^{\prime \prime}$ is a DAG.

Proof For any BN CPT $p\left(v_{j} \mid P_{j}\right)$, by Rule $2, v \prec v_{j}$, where $v \in P_{j}$. Moreover, by the definition of elder-set, $v \prec v_{j}$, where $v \in E_{j}$. Since the parent set $P_{j}$ of $v_{j}$ is modified as $P_{j} E_{j}-v_{i}$, for any CPT label $p\left(v_{j} \mid P_{j}\right)$ returned by the MCL algorithm, it is still the case that $v \prec v_{j}$, where $v \in P_{j}$. Therefore, the CPT-graph defined by $C^{\prime \prime}$ is acyclic, namely, it is a DAG.

We now present the ICM algorithm.

```
Algorithm \(2 \operatorname{ICM}(C, X)\)
Input: a set \(C\) of CPT labels,
    the set \(X\) of variables to be eliminated from \(C\)
Output: the set \(C\) of CPT labels sent from a node to a neighbour
begin
for each variable \(v\) in \(X\)
\(\{\)
    \(C^{\prime}=F R C(C, v)\)
    \(C^{\prime \prime}=M C L\left(C^{\prime}\right)\)
    \(C=\left(C-C^{\prime}\right) \cup C^{\prime \prime}\)
\(\}\)
return \((C)\)
end
```

We use two examples to illustrate the subtle points of all five rules in our architecture.

Example 11 Let us demonstrate how our architecture determines the CPT labels $p(g)$ and $p(h \mid g)$ in the storage registers for $g$ and $h$ from cdefgh to ghij, shown in Fig. 5. By Rule 2, we use $\prec$ in Example 3. By Rule 4, cdefgh has collected the CPT label $p(g \mid f)$ in the storage register of $g$ from bfg to cdefgh, but not $1(f)$ as this is not a CPT label, and calls ICM with $C=\{p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(g \mid f), p(h \mid c)\}$ and $X=\{c, d, e, f\}$. For pedagogical purposes, let us eliminate the variables in the order $d, c, e, f$. ICM calls FRC, passing it $C$ and variable $d$. FRC returns $\{p(d \mid c), p(f \mid d, e)\}$, which ICM initially assigns to $C^{\prime}$ and subsequently passes to MCL. Here $v_{i}=d, C_{i}=\left\{v_{1}=f\right\}, P_{1}=\{d, e\}$ and $E_{1}=\{c\}$. As $E_{1} P_{1}-v_{i}$ is $\{c, e\}$, MCL returns $\{p(f \mid c, e)\}$, which ICM assigns to $C^{\prime \prime}$. Next, the set $C$ of CPT labels under consideration in ICM is adjusted to be $C=\{p(c), p(e \mid c), p(f \mid c, e), p(g \mid f), p(h \mid c)\}$. For variable $c$, the call to FRC results in $C^{\prime}=\{p(c), p(e \mid c), p(f \mid c, e), p(h \mid c)\}$. To eliminate $v_{i}=c$, the elder-set of each variable in the child-set $C_{i}=\left\{v_{1}=\right.$ $\left.e, v_{2}=f, v_{3}=h\right\}$ is $E_{1}=\{ \}, E_{2}=\{e\}$ and $E_{3}=\{e, f\}$. Moreover, the parent-set of each variable in the child-set is $P_{1}=\{c\}, P_{2}=\{c, e\}$ and $P_{3}=\{c\}$. In MCL, then $p(h \mid c)$ is adjusted to $p(h \mid e, f)$, as $E_{3} P_{3}-v_{i}$ is $\{e, f\}$. Similarly, $p(f \mid c, e)$ is changed to $p(f \mid e)$ and $p(e \mid c)$ is modified to $p(e)$. Therefore, MCL returns the set $\{p(e), p(f \mid e), p(h \mid e, f)\}$ of CPT labels, which ICM assigns to $C^{\prime \prime}$. Then $C$ is updated to be $C=\{p(e), p(f \mid e), p(g \mid f), p(h \mid e, f)\}$. After eliminating variable $e$, the set of labels under consideration is modified to $C=\{p(f), p(g \mid f), p(h \mid f)\}$. Moreover, after considering the last variable $f$, the set of labels under consideration is $C=$ $\{p(g), p(h \mid g)\}$. ICM returns $C$ to cdefgh. By Rule 5, cdefgh places the CPT labels $p(g)$ and $p(h \mid g)$ in the storage registers of $g$ and $h$ from cdefgh to ghij, respectively.

Example 12 Now let us show how our architecture determines the labels $p(f)$ and $1(g)$ in the storage registers for $f$ and $g$ from cdefgh to bfg, shown in Fig. 5. By Rule 2, we use $\prec$ in Example 3. By Rule 4, cdefgh does not collect the unitypotential labels $1(g)$ and $1(h)$ in the storage registers of $g$ and $h$ from ghij and calls ICM with $C=\{p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(h \mid c)\}$ and $X=\{c, d, e, h\}$. For simplicity, let us eliminate the variables in the order $d, c, e, h$. Similar to Example 11, the set of CPT labels under consideration, after the elimination of variables $c, d, e$, is $C=\{p(f), p(h \mid f)\}$. After eliminating the last variable $h$, the set of labels under consideration is $C=\{p(f)\}$. ICM returns $C$ to cdefgh. By Rule 5, cdefgh places the CPT label $p(f)$ in the storage register of $f$ from cdefgh to $b f g$ and places the unitypotential label $1(g)$ in the empty storage register for variable $g$ from cdefgh to bfg.

All of the identified CPT messages for Fig. 5 are illustrated in Fig. 8, which is a screen shot of our implemented system. For simplified discussion, we will henceforth speak of messages passed between JT nodes with the separators understood.

Fig. 8 Identification of the CPT messages in Fig. 5


Example 13 Let us review Example 11 in terms of equations:

$$
\begin{aligned}
\sum_{c, d, e, f} & p(c) \cdot p(d|c) \cdot p(e|c) \cdot p(f|d, e) \cdot p(g|f) \cdot p(h|c) \\
& =\sum_{f} p(g|f) \cdot \sum_{e} \sum_{c} p(c) \cdot p(e|c) \cdot p(h|c) \cdot \sum_{d} p(d|c) \cdot p(f|d, e) \\
& =\sum_{f} p(g|f) \cdot \sum_{e} \sum_{c} p(c) \cdot p(e|c) \cdot p(h|c) \cdot p(f|c, e) \\
& =\sum_{f} p(g|f) \cdot \sum_{e} p(e) \cdot p(f|e) \cdot p(h|e, f) \\
& =\sum_{f} p(g|f) \cdot p(f) \cdot p(h|f) \\
& =p(g) \cdot p(h|g)
\end{aligned}
$$

The derivation of $p(g)$ and $p(h \mid g)$ is not correct without independencies. For instance, the independencies $I(d, c, e)$ and $I(f, d e, c)$ are necessary when moving from (2) to (3). In fact, without the unconditional independence $I(b, \emptyset, f)$, the message $p(g \mid f)$, from $b f g$ to $c d e f g h$, used in (1), is not correct either:

$$
\sum_{b} p(b) \cdot p(g \mid b, f)=\sum_{b} p(b) \cdot \frac{p(b, f, g)}{p(b, f)}=\sum_{b} p(b) \cdot \frac{p(b, f, g)}{p(b) \cdot p(f)}=p(g \mid f)
$$

Thus, the importance of showing that we can identify these independencies and utilize them, as shown above, is made obvious.

# 4 Complexity and correctness 

Here we establish the time complexity of the ICM algorithm and the correctness of our architecture for modeling inference not involving evidence.

Lemma 2 Let $n$ be the number of CPT labels in $C^{\prime}$ given as input to the MCL algorithm for eliminating variable $v_{i}$. The time complexity of MCL is $O(n)$.

Proof Let $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{n-1} \mid P_{n-1}\right)\right\}$ be the input set $C^{\prime}$ of CPT labels given to MCL. The elder-sets $E_{1}, \ldots, E_{n-1}$ and parent-sets $P_{1}, \ldots, P_{n-1}$ can be obtained in one pass over $C^{\prime}$. Given that $C^{\prime}$ has $n$ labels, the time complexity to determine the required parent-sets and elder-sets is $O(n)$. Similarly, for each label in $\left\{p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{n-1} \mid P_{n-1}\right)\right\}$, the parent-set is modified exactly once. Hence, this for-loop executes $n-1$ times. Therefore, the time complexity of MCL is $O(n)$.

Our main complexity result, given in Theorem 1, is that the CPT labels sent from a JT node can be identified in polynomial time.

Theorem 1 In the input to the ICM algorithm, let $n$ be the number of CPT labels in $C$, and let $X$ be the set of variables to be eliminated. The time complexity of ICM is $O\left(n^{2}\right.$ $\log n)$.

Proof As the number of CPT labels in $C$ is $n$, the maximum number of variables to be eliminated in $X$ is $n$. The loop body is executed $n$ times, once for each variable in $X$. Recall that the loop body calls the FRC and MCL algorithms. Clearly, FRC takes $O(n)$ time to find those CPT labels involving $v_{i}$. According to $\prec$ in Rule 2, these CPT labels can be sorted using the merge sort algorithm in $O(n \log n)$ time (Cormen et al. 2001). Thus, FRC has time complexity $O(n \log n)$. By Lemma 2, MCL has time complexity $O(n)$. Thus, the loop body takes $O(n \log n)$ time. Therefore, the time complexity of the ICM algorithm is $O\left(n^{2} \log n\right)$.

We now turn to the correctness of our architecture. The next result shows that certain independencies involving elder-sets hold in any BN.

Lemma 3 Let $(D, C)$ be a $B N$ defining a $J P D p(U)$. Given the set $C$ of CPT labels and any variable $v_{i} \in D$, the FRC algorithm returns $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$, where the variables in the child-set $C_{i}=\left\{v_{1}, \ldots, v_{k}\right\}$ are written according to $\prec$ in Rule 2. For each $v_{j} \in C_{i}$ with elder-set $E_{j}$, the independencies $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ and $I\left(v_{j}, P_{j}, E_{j}\right)$ hold in the $J P D p(U)$.

Proof Observe that the parents, children, and family of any variable $v$ in $D$ are precisely the parent-set, child-set and family-set of $v$, which are defined by $C^{\prime}$, respectively. Let us first show that $I\left(v_{j}, P_{j}, E_{j}\right)$ holds for $j=1, \ldots, k$. Pearl (1988) has shown that $I\left(v, P_{v}, N_{v}\right)$ holds for every variable $v$ in a BN, where $N_{v}$ denotes the set of all non-descendants of $v$ in $D$. By definition, no variable in the elder-set $E_{j}$ can be a descendant of $v_{j}$ in $D$. Thereby, $E_{j} \subseteq N_{j}$. By the decomposition axiom of probabilistic independence (Pearl 1988; Wong et al. 2000), the JPD $p(U)$ satisfying $I\left(v_{j}, P_{j}, N_{j}\right)$ logically implies that $p(U)$ satisfies $I\left(v_{j}, P_{j}, E_{j}\right)$.

We now show that $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ holds, for $j=1, \ldots, k$. According to the method in Section 2 for testing independencies, we write $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ as $I\left(v_{i}, E_{j}, P_{j}-v_{i}-E_{j}\right)$ and determine the ancestral set of the variables in $I\left(v_{i}, E_{j}, P_{j}-v_{i}-E_{j}\right)$ as $A n\left(v_{i}\right) \cup A n\left(E_{j}\right) \cup A n\left(P_{j}-v_{i}-E_{j}\right)$, which is the same as $A n\left(E_{j} P_{j}\right)$, since $v_{i} \in P_{j}$. Note that $v_{j}$, and any child of $v_{i}$ in $D$ succeeding $v_{j}$ in $\prec$ of Rule 2, are not members in the set $A n\left(E_{j} P_{j}\right)$. Hence, in the constructed sub-DAG $D^{\prime}$ of DAG $D$ onto $A n\left(E_{j} P_{j}\right)$, the only directed edges involving $v_{i}$ are those from each variable in $P_{i}$ to $v_{i}$ and from $v_{i}$ to every child preceding $v_{j}$. By Corollary 6 in Pearl (1988), $E_{j}$ is a Markov blanket of $v_{i}$ in $D^{\prime}$. By definition, $I\left(v_{i}, E_{j}, U-E_{j}-v_{i}\right)$ holds in $p(U)$. By the decomposition axiom, $p(U)$ satisfies $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$.

Let us first focus on the elimination of just one variable. We can maintain a CPT factorization after $v_{i} \in X$ is eliminated, provided that the corresponding elder-set independencies are satisfied by the JPD $p(U)$. Note that, as done previously, we write $\left(E_{j} P_{j}\right)-v_{i},\left(E_{j} F_{k}\right)-v_{i}$ and $\left(E_{j} F_{j}\right)-v_{i} v_{j}$ more simply as $E_{j} P_{j}-v_{i}, E_{j} F_{k}-v_{i}$ and $E_{j} F_{j}-v_{i} v_{j}$, respectively.

Lemma 4 Given the output $\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$ of FRC to eliminate variable $v_{i}$ in our architecture. By Rule $2, v_{1} \prec \ldots \prec v_{k}$ in the child-set $C_{i}=$ $\left\{v_{1}, \ldots, v_{k}\right\}$ of $v_{i}$. For each variable $v_{j} \in C_{i}$ with elder-set $E_{j}$, if the independencies $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ and $I\left(v_{j}, P_{j}, E_{j}\right)$ hold in the $\operatorname{JPD} p(U)$, then

$$
\sum_{v_{i}} p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k} \mid P_{k}\right)=\prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
$$

Proof We first show, by mathematical induction on the number $k$ of variables in $C_{i}$, that the product of these relevant CPTs can be rewritten as follows:

$$
p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k} \mid P_{k}\right)=p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \cdot \prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
$$

(Basic step: $j=1$ ). By definition, $E_{1}=P_{i}$. Thus, $p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right)=p\left(v_{i} \mid E_{1}\right)$. $p\left(v_{1} \mid P_{1}\right)$. By definition,

$$
p\left(v_{i} \mid E_{1}\right) \cdot p\left(v_{1} \mid P_{1}\right)=\frac{p\left(v_{i} E_{1}\right)}{p\left(E_{1}\right)} \cdot \frac{p\left(v_{1} P_{1}\right)}{p\left(P_{1}\right)}
$$

When $j=1$, by assumption, $I\left(v_{i}, E_{1}, P_{1}-v_{i}\right)$ and $I\left(v_{1}, P_{1}, E_{1}\right)$ hold. We can apply these independencies consecutively by multiplying the numerator and denominator of the right side of Eq. 4 by $p\left(E_{1} P_{1}-v_{i}\right)$, namely,

$$
\begin{aligned}
\frac{p\left(v_{i} E_{1}\right)}{p\left(E_{1}\right)} \cdot \frac{p\left(v_{1} P_{1}\right)}{p\left(P_{1}\right)} & =\frac{p\left(v_{i} E_{1}\right) \cdot p\left(E_{1} P_{1}-v_{i}\right)}{p\left(E_{1}\right) \cdot p\left(E_{1} P_{1}-v_{i}\right)} \cdot \frac{p\left(v_{1} P_{1}\right)}{p\left(P_{1}\right)} \\
& =\frac{p\left(E_{1} P_{1}\right)}{p\left(E_{1} P_{1}-v_{i}\right)} \cdot \frac{p\left(v_{1} P_{1}\right)}{p\left(P_{1}\right)} \\
& =\frac{p\left(v_{1} P_{1} E_{1}\right)}{p\left(E_{1} P_{1}-v_{i}\right)}
\end{aligned}
$$

By definition,

$$
\begin{aligned}
\frac{p\left(v_{1} P_{1} E_{1}\right)}{p\left(E_{1} P_{1}-v_{i}\right)} & =\frac{p\left(E_{1} F_{1}\right)}{p\left(E_{1} F_{1}-v_{i} v_{1}\right)} \\
& =p\left(v_{i} v_{1} \mid E_{1} F_{1}-v_{i} v_{1}\right)
\end{aligned}
$$

By the product rule (Xiang 2002) of probability, which states that $p(X, Y \mid Z)=$ $p(X \mid Y, Z) \cdot p(Y \mid Z)$ for pairwise disjoint subsets $X, Y$ and $Z$, Eq. 6 is expressed as:

$$
\begin{aligned}
p\left(v_{i} v_{1} \mid E_{1} F_{1}-v_{i} v_{1}\right) & =p\left(v_{i} \mid E_{1} F_{1}-v_{i}\right) \cdot p\left(v_{1} \mid E_{1} F_{1}-v_{i} v_{1}\right) \\
& =p\left(v_{i} \mid E_{1} F_{1}-v_{i}\right) \cdot p\left(v_{1} \mid E_{1} P_{1}-v_{i}\right)
\end{aligned}
$$

By (4)-(7),

$$
p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right)=p\left(v_{i} \mid E_{1} F_{1}-v_{i}\right) \cdot p\left(v_{1} \mid E_{1} P_{1}-v_{i}\right)
$$

(Inductive hypothesis: $j=k-1, k \geq 2$ ). Suppose

$$
p\left(v_{i} \mid P_{i}\right) p\left(v_{1} \mid P_{1}\right) \cdots p\left(v_{k-1} \mid P_{k-1}\right)=p\left(v_{i} \mid E_{k-1} F_{k-1}-v_{i}\right) \prod_{j=1}^{k-1} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
$$

(Inductive step: $j=k$ ). Consider the following product

$$
p\left(v_{i} \mid P_{i}\right) p\left(v_{1} \mid P_{1}\right) \ldots p\left(v_{k} \mid P_{k}\right)=p\left(v_{i} \mid P_{i}\right) p\left(v_{1} \mid P_{1}\right) \ldots p\left(v_{k-1} \mid P_{k-1}\right) p\left(v_{k} \mid P_{k}\right)
$$

By the inductive hypothesis,

$$
\begin{aligned}
& \left(p\left(v_{i} \mid P_{i}\right) p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k-1} \mid P_{k-1}\right)\right) \cdot p\left(v_{k} \mid P_{k}\right) \\
& \quad=\left(p\left(v_{i} \mid E_{k-1} F_{k-1}-v_{i}\right) \prod_{j=1}^{k-1} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)\right) \cdot p\left(v_{k} \mid P_{k}\right) \\
& \quad=p\left(v_{i} \mid E_{k-1} F_{k-1}-v_{i}\right) \cdot p\left(v_{k} \mid P_{k}\right) \cdot \prod_{j=1}^{k-1} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
\end{aligned}
$$

Since $E_{k}=E_{k-1} F_{k-1}-v_{i},(10)$ can be rewritten as

$$
p\left(v_{i} \mid P_{i}\right) p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k} \mid P_{k}\right)=p\left(v_{i} \mid E_{k}\right) p\left(v_{k} \mid P_{k}\right) \prod_{j=1}^{k-1} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
$$

It can easily be shown that

$$
p\left(v_{i} \mid E_{k}\right) \cdot p\left(v_{k} \mid P_{k}\right)=p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \cdot p\left(v_{k} \mid E_{k} P_{k}-v_{i}\right)
$$

by following (4)-(7) replacing $j=1$ with $j=k$. Substituting (12) into (11), the desired result follows:

$$
\begin{aligned}
& p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k} \mid P_{k}\right) \\
& \quad=p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \cdot p\left(v_{k} \mid E_{k} P_{k}-v_{i}\right) \cdot \prod_{j=1}^{k-1} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right) \\
& \quad=p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \cdot \prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
\end{aligned}
$$

Having rewritten the factorization of the relevant CPTs, we now consider the elimination of variable $v_{i}$ as follows:

$$
\begin{aligned}
& \sum_{v_{i}} p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \cdot \prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right) \\
& \quad=\prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right) \cdot \sum_{v_{i}} p\left(v_{i} \mid E_{k} F_{k}-v_{i}\right) \\
& \quad=\prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right) \cdot 1.0 \\
& \quad=\prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
\end{aligned}
$$

By (13) and (14), we obtain the desired result

$$
\sum_{v_{i}} p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{1} \mid P_{1}\right) \cdot \ldots \cdot p\left(v_{k} \mid P_{k}\right)=\prod_{j=1}^{k} p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)
$$

Equation (15) explicitly demonstrates the form of the factorization in terms of CPTs after variable $v_{i}$ is eliminated. Hence, the right-side of (15) is used in the MCL algorithm to adjust the label of the CPT for each variable in $v_{i}$ 's child-set. That is, $\prod_{j=1}^{k}$ corresponds to the for-loop construct running from $j=k, \ldots, 1$, while $p\left(v_{j} \mid E_{j} P_{j}-v_{i}\right)$ corresponds to the statement $P_{j}=E_{j} P_{j}-v_{i}$ for one iteration of the for-loop.

Example 14 Recall eliminating variable $d$ in (2). By Example 11, $v_{i}=d, C_{i}=\left\{v_{1}=\right.$ $f\}, P_{1}=\{d, e\}$ and $E_{1}=\{c\}$. By Lemma $3, I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ and $I\left(v_{j}, P_{j}, E_{j}\right)$ hold, namely, $I(d, c, e)$ and $I(f, d e, c)$. By Lemma $4, \sum_{d} p(d \mid c) \cdot p(f \mid d, e)$ is equal to $p(f \mid c, e)$, as shown in (3).

We now establish the correctness of our architecture by showing that our messages are equivalent to those of the SS architecture (Shafer and Shenoy 1990; Shafer 1996). Since their architecture computes the probability distributions stored in computer

memory, while our architecture determines labels, let us assume that the label in each storage register of our architecture is replaced with its corresponding probability distribution.

Theorem 2 Given a BN D and a JT for D. Apply our architecture and also the SS architecture. For any two neighbouring JT nodes $N_{i}$ and $N_{j}$, the product of the distributions in the storage registers from $N_{i}$ to $N_{j}$ in our architecture is the message in the storage register from $N_{i}$ to $N_{j}$ in the SS architecture.

Proof When a JT node $N_{i}$ receives a message from a neighbour $N_{j}$, it is also receiving, indirectly, information from the nodes on the other side of $N_{j}$ (Shafer 1996). Thus, without a loss of generality, let the JT for $D$ consist of two nodes, $N_{1}$ and $N_{2}$. Consider the message from $N_{2}$ to $N_{1}$. Let $Z$ be those variables $v_{m}$ of $N_{2}$ such that the BN CPT $p\left(v_{m} \mid P_{m}\right)$ is assigned to $N_{2}$. The variables to be eliminated are $X=N_{2}-N_{1}$. Let $Y=N_{2}-(X Z)$. Following the discussion in Section 2, the SS message $\phi\left(N_{2} \cap N_{1}\right)$ from $N_{2}$ to $N_{1}$ is:

$$
\begin{aligned}
\phi\left(N_{2} \cap N_{1}\right) & =\sum_{X} \phi\left(N_{2}\right) \\
& =\sum_{X} 1\left(N_{2}\right) \cdot \prod_{v_{m} \in Z} p\left(v_{m} \mid P_{m}\right) \\
& =\sum_{X} 1(Y) \cdot 1(X Z) \cdot \prod_{v_{m} \in Z} p\left(v_{m} \mid P_{m}\right) \\
& =1(Y) \cdot \sum_{X} \prod_{v_{m} \in Z} p\left(v_{m} \mid P_{m}\right)
\end{aligned}
$$

Consider the first variable $v_{i}$ of $X$ eliminated from $\prod_{v_{m} \in Z} p\left(v_{m} \mid P_{m}\right)$. By Lemma 3, for each $v_{j} \in C_{i}$, the independencies $I\left(v_{i}, E_{j}, P_{j}-v_{i}\right)$ and $I\left(v_{j}, P_{j}, E_{j}\right)$ hold in $p(U)$. By Lemma 4, the exact form of the CPTs is known after the elimination of $v_{i}$. By (Shafer 1996), the product of all remaining probability tables in the entire JT is the marginal distribution $p\left(U-v_{i}\right)$ of the original joint distribution $p(U)$. Let us more carefully examine the remaining CPTs in the entire JT. First, each variable in $U-v_{i}$ has exactly one CPT. It follows from Lemma 1 that the CPT-graph defined by all CPT labels remaining in the JT is a DAG. Therefore, the CPTs for the remaining variables $U-v_{i}$ are a BN defining the marginal distribution $p\left(U-v_{i}\right)$ of the original JPD $p(U)$. By the definition of probabilistic conditional independence, an independence holding in the marginal $p\left(U-v_{i}\right)$ necessarily means that it holds in the joint distribution $p(U)$. Thereby, we can recursively apply Lemmas 1, 3 and 4 to eliminate the other variables in $X$. The CPTs remaining from the marginalization of $X$ from $\prod_{v_{m} \in Z} p\left(v_{m} \mid P_{m}\right)$ are exactly the distributions of the CPT labels output by the ICM algorithm when called by $N_{2}$ to eliminate $X$ from $C=\left\{p\left(v_{m} \mid P_{m}\right) \mid v_{m} \in Z\right\}$. In our architecture, the storage registers from $N_{2}$ to $N_{1}$ for those variables in $Y$ are still empty. Filling these empty storage registers with unity-potentials $1\left(v_{l}\right)$, $v_{l} \in Y$, follows directly from the definition of the unity-potential $1(Y)$. Therefore, the product of the distributions in the storage registers from $N_{2}$ to $N_{1}$ in our architecture is the message in the storage register from $N_{2}$ to $N_{1}$ in the SS architecture.

Example 15 It can be verified that the identified CPTs shown in Fig. 5 are correct. In particular, the SS message $\phi(f, g)$ from $c d e f g h$ to $b f g$ is $p(f) \cdot 1(g)$.

Corollary 1 The marginal distribution $p(N)$ for any JT node $N$ can be computed by collecting all CPTs sent to $N$ by N's neighbours and multiplying them with those CPTs assigned to $N$.

# 5 Modeling inference involving evidence 

Pearl (1988) emphasizes the importance of structure by opening his chapter on Markov and BNs with the following quote:

Probability is not really about numbers; it is about the structure of reasoning.

- G. Shafer

In this section, we extend our architecture to model the processing of evidence and show that it can still identify CPT messages. Modeling the processing of evidence is faster than the physical computation needed for evidence processing. By allowing our architecture to take full responsibility for modeling structure, we empirically demonstrate that LAZY can finish its work sooner.

It is important to realize that the processing of evidence $E=e$ can be viewed as computing marginal distributions (Schmidt and Shenoy 1998; Shafer 1996; Xu 1995). For each JT node $N$, compute the marginal $p(N E)$, from whence $p(N-E, E=e)$ can be obtained. The desired distribution $p(N-E \mid E=e)$ can then be determined via normalization.

Rules 6 and 7 extend our architecture to model the processing of evidence.
Rule 6. Given evidence $E=e$. For each node $N$ in the JT, set $N=N \cup E$. On this augmented JT, apply Rules 1-5 of our architecture for modeling inference not involving evidence.
Rule 7. For each evidence variable $v \in E$, change each occurrence of $v$ in an assigned or propagated CPT label from $v$ to $v=\varepsilon$, where $\varepsilon$ is the observed value of $v$.

We now show the correctness of our architecture for modeling inference involving evidence.

Theorem 3 Given a BN D, a JT for D, and observed evidence $E=e$. After applying our architecture, extended by Rules 6 and 7 for modeling inference involving evidence, the probability information at each JT node $N$ defines $p(N-E, E=e)$.

Proof Apply Rule 6. By Corollary 1, the probability information at each node $N$ is $p(N E)$. By selecting those configurations agreeing with $E=e$ in Rule 7, the probability information at each node is $p(N-E, E=e)$.

Example 16 Consider evidence $b=0$ in the real-world BN for CHD in Fig. 3. With respect to the CHD JT in Fig. 5, the CPT messages to be propagated are depicted in Fig. 9.

The next example involves three evidence variables.

Example 17 Consider the JT with assigned BN CPTs in Fig. 10 (top). Given evidence $a=0, c=0, f=0$, the LAZY potentials propagated towards node $d e$ are shown (Madsen and Jensen 1999). In comparison, all CPT labels identified by our architecture are depicted in Fig. 10 (bottom).

We can identify the labels of the messages faster than the probability distributions themselves can be built in computer memory.

Example 18 Given evidence $b=0$ in Example 16, constructing the distribution $p(b=0)$ in memory for the message from node $a b$ to bfg required 1.813 ms . Identifying all CPT messages in Fig. 9 required only 0.954 ms .

Although semantic modeling can be done significantly faster than physical computation, the LAZY architecture applies these two tasks iteratively. The consequence, as the next two examples show, is that semantic modeling must wait while the physical computation catches-up.

Example 19 Madsen and Jensen (1999) Consider the BN (left) and JT with assigned CPTs (right) in Fig. 11. Suppose evidence $d=0$ is collected. Before node $b c d e f$ can send its messages to node $e f g$, it must first wait for the message $\phi(b, c)$ to be physically constructed at node $a b c$ as:

$$
\phi(b, c)=\sum_{a} p(a) \cdot p(b \mid a) \cdot p(c \mid a)
$$

Upon receiving distribution $\phi(b, c)$ at node $b c d e f$, LAZY exploits the independence $I(b c, d, e f)$ induced by the evidence $d=0$ to identify that $\phi(b, c)$ is irrelevant to the computation for the messages to be sent from $b c d e f$ to $e f g$.

Fig. 9 Recall the real-world BN for CHD in Fig. 3 and the JT in Fig. 5. Given evidence $b=0$, the propagated CPT labels are shown here


Fig. 10 Madsen and Jensen (1999) A JT with assigned BN CPTs (top). Given evidence $a=0, c=0, f=0$, this shows the LAZY potentials propagated towards node $d e$. In contrast to Fig. 10 (top), this screen shot shows all identified CPT labels given evidence $a=0, c=0, f=0$ (bottom)
![img-5.jpeg](img-5.jpeg)

# CPT Message Identification 


In the exploitation of independencies induced by evidence, Example 19 explicitly demonstrates that LAZY forces node bcdef to wait for the construction of the irrelevant message $\phi(b, c)$.

Fig. 11 Madsen and Jensen (1999) A BN (left) and a JT with assigned CPTs (right). LAZY exploits the independence $I(b c, d, e f)$ induced by evidence $d=0$ only after the irrelevant potential $\phi(b, c)$ has been physically constructed at $a b c$ and sent to bcdef
![img-6.jpeg](img-6.jpeg)
$\{p(d \mid b, c), p(e \mid d), p(f \mid d)\}$
![img-7.jpeg](img-7.jpeg)
$\{p(\mathrm{~g} \mid \mathrm{e}, \mathrm{f})\}$

Example 20 Madsen and Jensen (1999) Consider the BN (left) and JT with assigned CPTs (right) in Fig. 12. Before node $a c d e$ can send its messages to node $e f$, it must first wait for the message $\phi(c, d \mid a)$ to be constructed in computer memory at node $a b c d$ as:

$$
\phi(c, d \mid a)=\sum_{b} p(b \mid a) \cdot p(c \mid a, b) \cdot p(d \mid a, b)
$$

Upon receiving distribution $\phi(c, d \mid a)$ at $a c d e$, LAZY exploits barren variables $c$ and $d$ to identify that $\phi(c, d \mid a)$ is irrelevant to the computation for the messages to be sent from $a c d e$ to $e f$.

In the exploitation of barren variables, Example 20 explicitly demonstrates that LAZY forces node acde to wait for the physical construction of the irrelevant message $\phi(c, d \mid a)$. These unnecessary delays in Examples 19 and 20 are inherently built into the main philosophy of LAZY propagation (Madsen and Jensen 1999):

The bulk of LAZY propagation is to maintain a multiplicative [factorization of the CPTs] and to postpone combination of [CPTs]. This gives opportunities for exploiting barren variables . . . during inference. . . . Thereby, when a message is to be computed only the required [CPTs] are combined.

The notion of a barren variable, however, is relative. For instance, in Example 20, variables $c$ and $d$ are not barren at the sending node $a b c d$, but are barren at the receiving node acde. Thus, the interweaving of modeling structure and physical computation underlay these unnecessary delays.

We advocate the uncoupling of these two independent tasks. More specifically, we argue that modeling structure and computation of the actual probability distributions in computer memory should be performed separately. As our architecture can model structure faster than the physical computation can be performed, it can scout the structure in the JT and organize the collected information in three kinds of work schedules.

Our first work schedule pertains to non-empty messages that are irrelevant to subsequent message computation at the receiving node, as evident in Examples 19 and 20. More specifically, for three distinct nodes $N_{i}, N_{j}$ and $N_{k}$ such that $N_{i}$ and $N_{j}$ are neighbours, as are $N_{j}$ and $N_{k}$, our first work schedule indicates that the messages from $N_{i}$ to $N_{j}$ are irrelevant in the physical construction of the messages to be sent from $N_{j}$ to $N_{k}$.

Fig. 12 Madsen and Jensen (1999) A BN (left) and a JT with assigned CPTs (right). LAZY exploits barren variables $c$ and $d$ only after the irrelevant potential $\phi(c, d \mid a)$ has been physically constructed at $a b c d$ and sent to acde
![img-8.jpeg](img-8.jpeg)

Fig. 13 Given evidence $d=0$ in Example 19, our architecture can identify the irrelevant message from $a b c$ to $b c d e f$

## Irrelevant CPT Identification

![img-9.jpeg](img-9.jpeg)

Example 21 Given evidence $d=0$ in Example 19, the work schedule in Fig. 13 indicates that the messages from node $a b c$ are irrelevant to node $b c d e f$ in the physical construction of the messages to be sent from bcdef to node efg. Now reconsider Example 20. The work schedule in Fig. 14 indicates that the messages from node $a b c d$ are irrelevant to node $a c d e$ in the physical construction of the messages to be sent from acde to node ef.

Our second work schedule indicates that an empty message will be propagated from a non-leaf node to a neighbour. (As LAZY could begin physical computation at the leaf JT nodes, we focus on the non-leaf JT nodes.) For instance, given evidence $b=0$ in the extended CHD BN and JT with assigned CPTs in Fig. 15, the work schedule in Fig. 16 indicates that bfg will send $a b$ an empty message. Our second work schedule saves LAZY time.

Example 22 Recall the extended CHD BN and JT in Fig. 15. Given evidence $b=0$, LAZY determines that $b f g$ will send $a b$ an empty message only after $b f g$ receives the probability distributions $\phi(f)$ from cdefgh. Physically constructing $\phi(f)$ involves eliminating the four variables $c, d, e, h$ from the five potentials $p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(h \mid c)$. In less time than is required for this physical computation, our architecture has generated the work schedule in Fig. 16. Without waiting for LAZY to eventually consider $b f g$, node $a b$ can immediately send its messages $\{p(a \mid b=0), p(b=0)\}$ to node $a l$, which, in turn, can send its respective messages $\{p(b=0), p(l \mid b=0)\}$ to node $l m$.

Last, but not least, our architecture can generate another type of beneficial work schedule. This third work schedule indicates the variables that can be eliminated at a non-leaf node with respect to the messages for a particular neighbour, before the sending node has received any messages. Given evidence $b=0$ in the CHD JT of Fig. 5, the work schedule in Fig. 17 indicates that, for instance, non-leaf node cdefgh

Fig. 14 For Example 20, our architecture can identify the irrelevant message from $a b c d$ to acde

## Irrelevant CPT Identification

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

Fig. 15 An extended CHD BN (left) and a JT with assigned CPTs (right). Given evidence $b=0$, LAZY forces node $a b$ to wait for the identification of an irrelevant empty message from $b f g$
can immediately eliminate variables $c, d, e$ in its construction of the message to ghij. Assisting LAZY to eliminate variables early saves time, as the next example clearly demonstrates.

Example 23 Given evidence $b=0$ in the CHD JT of Fig. 5, consider the message from cdefgh to ghij. LAZY waits to eliminate variables $c, d, e, f$ at cdefgh until cdefgh receives its messages $\left\{\phi(b=0), \phi_{b=0}(f, g)\right\}$ from bfg, which, in turn, has to wait for message $\phi(b=0)$ from $a b$. Thus, LAZY computes the message from cdefgh to ghij as:

$$
\sum_{c d e f} p(c) \cdot p(d \mid c) \cdot p(e \mid c) \cdot p(f \mid d, e) \cdot p(h \mid c) \cdot \phi(b=0) \cdot \phi_{b=0}(f, g)
$$

In contrast, the work schedule of Fig. 17 allows LAZY to immediately eliminate variables $c, d, e$ as:

$$
\phi(f, h)=\sum_{c, d, e} p(c) \cdot p(d \mid c) \cdot p(e \mid c) \cdot p(f \mid d, e) \cdot p(h \mid c)
$$

The benefit is that when the LAZY messages $\left\{\phi(b=0), \phi_{b=0}(f, g)\right\}$ from bfg are received, only variable $f$ remains to be eliminated. That is to say, LAZY's (18) is simplified to

$$
\sum_{f} \phi(f, h) \cdot \phi(b=0) \cdot \phi_{b=0}(f, g)
$$

In our CHD example, LAZY will eliminate $c, d, e$ twice at node cdefgh, once for each message to $b f g$ and ghij. This duplication of effort is a well-known undesirable

Fig. 16 Our architecture can identify all empty messages sent by non-leaf nodes given evidence $b=0$ in the extended CHD JT of Fig. 15 (right)

## Empty Message Identification


Fig. 17 Given evidence $b=0$ in the CHD JT of Fig. 5, our architecture identifies those variables that can be eliminated at non-leaf nodes before any messages are received


property in JT propagation (Shafer 1996). Utilizing our third work schedule, such as in Fig. 17, to remove this duplication remains for future work.

We conclude this section by providing some empirical results illustrating the usefulness of our JT architecture. In particular, we provide the time taken for LAZY propagation and the time saved by allowing our architecture to guide LAZY. The source code for LAZY propagation was obtained from (Consortium 2002), as was the code for generating a JT from a BN. Table 1 describes five real-world or benchmark BNs and their corresponding JTs used in the experiments.

We first measure the time cost of performing inference not involving evidence. Table 2 shows the time taken for : (i) LAZY propagation by itself, (ii) LAZY propagation guided by our architecture, (iii) time saved by using our approach, and (iv) time saved as a percentage. All propagation was timed in seconds using a SGI R12000 processor. Note that our architecture lowered the time taken for propagation in all five real-world or benchmark BNs. The time percentage saved ranged from $11.76 \%$ to $69.26 \%$ with an average percentage of $37.02 \%$.

Next, we measure the time cost of performing inference involving evidence. As shown in Tables 3 and 4, approximately nine percent and eighteen percent of the variables in each BN are randomly instantiated as evidence variables, respectively. Note that once again our architecture lowered the time taken for propagation in all five real-world or benchmark BNs. In Table 3, the time percentage saved ranged from $0.42 \%$ to $15.48 \%$ with an average percentage of $6.42 \%$. In Table 4,

Table 1 Five real-world or benchmark BNs used in our experiments


Table 2 Experimental results on five BNs not involving evidence


the time percentage saved ranged from $1.86 \%$ to $14.89 \%$ with an average percentage of $6.12 \%$.

It is worth mentioning that our architecture is more useful with fewer evidence variables. One reason for this is that the cost of physical computation is lowered with collected evidence, since the probability tables to be propagated are much smaller. For instance, LAZY takes over 882 s to perform propagation not involving evidence on the Mildew BN, yet only takes about 15 s to perform propagation if 6 variables are instantiated as evidence variables. Therefore, LAZY needs more help in the case of processing no or fewer evidence variables and this is precisely when our architecture is most beneficial.

# 6 Local BNs and practical applications 

After applying our architecture, as described in Section 3, to identify the probability information being passed in a JT, let us apply either method from (Madsen and Jensen 1999; Zhang 1998) to physically construct the identified CPT messages. That is, we assume that the label in each storage register of our architecture is replaced with its corresponding probability distributions. Unlike all previous JT architectures (Jensen et al. 1990; Lauritzen and Spiegelhalter 1988; Madsen and Jensen 1999; Shafer and Shenoy 1990), in our architecture, after propagation not involving evidence, each JT node $N$ has a sound, local BN preserving all conditional independencies of the original BN involving variables in $N$. Practical applications of local BNs include an automated modeling procedure for MSBNs and a method for exploiting localized queries in DC techniques.

Table 3 Experimental results on five BNs with 9\% of the variables randomly instantiated as evidence variables


Table 4 Experimental results on five BNs with $18 \%$ of the variables randomly instantiated as evidence variables


Lemma 5 Given a BN D and a JT for D, apply Rules 1-5 in our architecture. For any JT node $N$, the CPTs assigned to $N$, together with all CPTs sent to $N$ from N's neighbours, define a local $B N D_{N}$.

Proof As previously mentioned, when a JT node $N_{i}$ receives a message from a neighbour $N_{j}$, it is also receiving, indirectly, information from the nodes on the other side of $N_{j}$ (Shafer 1996). Thus, without a loss of generality, let the JT for $D$ consist of two nodes, $N_{1}$ and $N_{2}$. We only need focus on variables in the separator $N_{1} \cap N_{2}$. Consider a variable $v_{m}$ in $N_{1} \cap N_{2}$ such that the BN CPT $p\left(v_{m} \mid P_{m}\right)$ is assigned to $N_{1}$. Thus, $v_{m}$ is without a CPT label with respect to $N_{2}$. In $N_{1}$ 's call to ICM for its messages to $N_{2}$, variable $v_{m}$ is not in $X=N_{1}-N_{2}$, the set of variables to be eliminated, Thus, ICM will return a CPT label for $v_{m}$ to $N_{1}$. By Rule 5, $N_{1}$ will place this CPT label in the empty storage register for $v_{m}$ from $N_{1}$ to $N_{2}$. Therefore, after propagation, variable $v_{m}$ has a CPT label at node $N_{2}$. Conversely, consider $N_{2}$ 's call of ICM for its messages to $N_{1}$. Since the BN CPT $p\left(v_{m} \mid P_{m}\right)$ is assigned to $N_{1}$, there is no CPT label for $v_{m}$ passed to ICM. Thus, ICM does not return a CPT label for $v_{m}$ to $N_{2}$. By Rule $5, N_{2}$ fills the empty storage register of $v_{m}$ from $N_{2}$ to $N_{1}$ with the unity-potential label $1\left(v_{m}\right)$. Therefore, after propagation, both $N_{1}$ and $N_{2}$ have precisely one CPT label for $v_{m}$. Moreover, for each node, it follows from Lemma 1 that the CPT-graph defined by the assigned CPTs and the message CPTs is a DAG. By definition, each JT node $N$ has a local $\mathrm{BN} D_{N}$.

Example 24 Recall the JT with assigned CPTs in Fig. 5. Each JT node has a local BN after propagation not involving evidence, as depicted by a screen shot of our implemented system in Fig. 18.

Theorem 4 Given Lemma 5. If an independence $I(X, Y, Z)$ holds in a local $B N D_{N}$ for a JT node $N$, then $I(X, Y, Z)$ holds in the original $B N D$.

Proof We will show the claim by removing variables in the JT towards the node $N$. Let $v_{i}$ be the first variable eliminated in the JT for $D$. After calling MCL, let $D^{\prime}$ be the CPT-graph defined by the CPTs remaining at this node, together with the CPTs assigned to all other nodes. It follows from Lemma 1 that $D^{\prime}$ is a DAG. We now establish that $I(X, Y, Z)$ holding in $D^{\prime}$ implies that $I(X, Y, Z)$ holds in $D$. Note that since $v_{i}$ is eliminated, $v_{i} \notin X Y Z$. By contraposition, suppose $I(X, Y, Z)$ does not hold in $D$. By the method for testing independencies in Section 2, let $D_{m}$ be the moralization of the sub-DAG of $D$ onto $X Y Z \cup \operatorname{An}(X Y Z)$. There are two cases

Fig. 18 Local BNs after propagation not involving evidence for the CHD BN
![img-12.jpeg](img-12.jpeg)
to consider. Suppose $v_{i} \notin \operatorname{An}(X Y Z)$. In this case, $I(X, Y, Z)$ does not hold in $D^{\prime}$ as $D_{m}$ is also the moralization of the sub-DAG of $D^{\prime}$ onto $X Y Z \cup \operatorname{An}(X Y Z)$. Now, suppose $v_{i} \in \operatorname{An}(X Y Z)$. Let $D_{m}^{\prime}$ be the moralization of the sub-DAG of $D^{\prime}$ onto $X Y Z \cup \operatorname{An}(X Y Z)$. By assumption, there is an undirected path in $D_{m}$ from $X$ to $Z$, which does not involve $Y$. If this path does not involve $v_{i}$, this same path must exist in $D_{m}^{\prime}$ as the MCL algorithm only removes those edges involving $v_{i}$. Otherwise, as $v_{i} \notin X Y Z$, this path must include edges $\left(v, v_{i}\right)$ and $\left(v_{i}, v^{\prime}\right)$, where $v, v^{\prime} \in P_{i} C_{i}$. Since the moralization process will add an undirected edge between every pair of variables in $P_{i}$, and since the MCL algorithm will add a directed edge from every variable in $P_{i}$ to every variable in $C_{i}$ and also from every variable $v_{j}$ in $C_{i}$ to every other variable $v_{k}$ in $C_{i}$ such that $v_{j} \prec v_{k}$ in Rule 2, it is necessarily the case that $\left(v, v^{\prime}\right)$ is an undirected edge in the moralization $D_{m}^{\prime}$ of $D^{\prime}$. As there is an undirected path in $D_{m}^{\prime}$ from $X$ to $Z$ not involving $Y$, by definition, $I(X, Y, Z)$ does not hold in $D^{\prime}$. Thus, every independence $I(X, Y, Z)$ encoded in $D^{\prime}$ is encoded in the original BN $D$. Therefore, by recursively eliminating all variables $v \notin N$, all conditional independencies encoded in $D_{N}$ are also encoded in $D$.

Example 25 In Fig. 18, it is particularly illuminating that our architecture correctly models $I(g, c, h)$, the conditional independence of $g$ and $h$ given $c$, in the local BN for $c d e f g h$, yet at the same time correctly models $I(g, h, i)$, the conditional independence of $g$ and $i$ given $h$, in the local BN for $g h i j$.

Although unconditional independencies of the original BN might not be saved in the local BNs, Theorem 5 shows that conditional independencies are.

Theorem 5 Given Lemma 5. If an independence $I(X, Y, Z)$ holds in the original $B N$ $D$, where $Y \neq \emptyset$ and $X Y Z$ is a subset of a JT node $N$, then $I(X, Y, Z)$ holds in the local $B N D_{N}$.

Proof Let $v_{i} \in U$ be the first variable eliminated by our architecture. Suppose FRC returns the set of CPT labels $C^{\prime}=\left\{p\left(v_{i} \mid P_{i}\right), p\left(v_{1} \mid P_{1}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$. By $\prec$ in Rule 2, the child-set of $v_{i}$ is $C_{i}=\left\{v_{1}, \ldots, v_{k}\right\}$. The set of all variables appearing in any label of $C^{\prime}$ is $E_{k} F_{k}$. Clearly, the CPT-graph $D^{\prime}$ defined by $C^{\prime}$ is a DAG. By Corollary 6

in Pearl (1988), variable $v_{i}$ is independent of all other variables in $U$ given $E_{k} F_{k}-v_{i}$. Thus, we only need to show that any conditional independence $I(X, Y, Z)$ holding in $D^{\prime}$ with $v_{i} \notin X Y Z$ is preserved in $D^{\prime \prime}$, where $D^{\prime \prime}$ is the CPT-graph defined by the set $C^{\prime \prime}$ of CPT labels output by MCL given $C^{\prime}$ as input. By Lemma 1, $D^{\prime \prime}$ is a DAG. By contraposition, suppose a conditional independence $I(X, Y, Z)$ does not hold in $D^{\prime \prime}$. According to the method for testing independencies in Section 2, let $D_{m}^{\prime}$ be the moralization of the sub-DAG of $D^{\prime}$ onto $X Y Z \cup \operatorname{An}(X Y Z)$. There are two cases to consider. Suppose $v_{i} \notin \operatorname{An}(X Y Z)$. In this case, $I(X, Y, Z)$ does not hold in $D^{\prime}$ as $D_{m}^{\prime}$ is also the moralization of the sub-DAG of $D^{\prime \prime}$ onto $X Y Z \cup$ $\operatorname{An}(X Y Z)$. Now, suppose $v_{i} \in \operatorname{An}(X Y Z)$. By definition, the moralization process makes families complete. Observe that the family of each variable $v_{m}$ in $D^{\prime}$ is, by definition, the family-set of $v_{m}$ in the CPT label $p\left(v_{m} \mid P_{m}\right)$ of $C^{\prime}$. For every variable $v_{m}$ in the sub-DAG of $D^{\prime}$ onto $X Y Z \cup \operatorname{An}(X Y Z), v_{i}$ is a member of the family-set $F_{m}$. Therefore, there is an edge $\left(v_{i}, v\right)$ in $D_{m}^{\prime}$ between $v_{i}$ and every other variable $v$ in $D_{m}^{\prime}$. Then, in particular, there is a path $\left(x, v_{i}\right),\left(v_{i}, z\right)$ from every variable $x \in X$ to every variable $z \in Z$. Since $v_{i} \notin Y$, by definition, $I(X, Y, Z)$ does not hold in $D^{\prime}$. Hence, all conditional independencies on $U-v_{i}$ are kept. Therefore, by recursively eliminating all variables $v \notin N$, all conditional independencies on $N$ are kept. That is, by Lemma 5, all conditional independencies $I(X, Y, Z)$ with $X Y Z \subseteq N$ are preserved in the local $\mathrm{BN} D_{N}$.

Example 26 Recall the CPT-graphs in Figs. 7 and 6 defined by the CPT labels before and after the elimination of variable $v_{i}=f$, respectively, where $C_{i}=\left\{v_{1}=j, v_{2}=\right.$ $\left.k, v_{3}=l\right\}$. It may seem as though some conditional independencies are lost due to the additional directed edges like $(c, l),(e, l)$ and $(j, l)$, where $c \in P_{i}, e \in P_{1}$ and $j, l \in C_{i}$. On the contrary, although $I(c, e j k h i, l), I(e, b c d h j k, l)$ and $I(j, c d e, l)$ do not hold in Fig. 6, these independencies do not hold in Fig. 7 either. Some unconditional independencies were lost, however, such as $I(b e, \emptyset, k l)$.

Our first practical application of local BNs concerns MSBNs (Xiang 1996, 2002; Xiang and Jensen 1999; Xiang et al. 2006, 2000, 1993), which are formally defined as follows.

Definition 19 A MSBN is a finite set $\left\{B_{1}, B_{2}, \ldots, B_{n}\right\}$ of BNs satisfying the following condition: $N_{1}, N_{2}, \ldots, N_{n}$ can be organized as a join tee, where $N_{i}$ is the set of variables in the local $\mathrm{BN} B_{i}, i=1,2, \ldots, n$.

Before any inference takes place, a given BN needs first be modeled as a MSBN. Several problems, however, with the manual construction of a MSBN from a BN have recently been acknowledged (Xiang et al. 2000). We resolve this modeling problem as follows.

Recently, Olesen and Madsen (2002) gave a simple method for constructing a special JT based on the maximal prime decomposition (MPD) of a BN. One desirable property of a MPD JT is that the JT nodes are unique for a given BN. We favour MPD JTs over conventional JTs, since they facilitate inference in the LAZY architecture while still only requiring polynomial time for construction (Olesen and Madsen 2002). For example, given the CHD BN in Fig. 3, the JT shown in Fig. 5 is the unique MPD JT.

We now propose Algorithm 3 to introduce an automated procedure for constructing a MSBN from a given BN.

```
Algorithm 3 Construct-MSBN \((D)\)
Input: A BN \(D\).
Output: A MSBN \(\left\{B_{1}, B_{2}, \ldots, B_{n}\right\}\).
begin
1. Construct a MPD JT with nodes \(\left\{N_{1}, N_{2}, \ldots, N_{n}\right\}\) for the BN \(D\).
2. Assign the CPTs of the BN \(D\) to the MPD JT nodes \(N_{1}, N_{2}, \ldots, N_{n}\) as usual.
3. Apply our architecture to label the messages to be propagated during JT
    propagation.
4. Compute the distributions of the identified CPTs in Step 3 using any of the
    available inference algorithms.
5. Define the local BN \(B_{i}\) for each \(N_{i}\) to be the CPTs assigned
    and passed to \(N_{i}\).
6. Return the MSBN \(\left\{B_{1}, B_{2}, \ldots, B_{n}\right\}\).
```

Example 27 We illustrate Algorithm 3 using the real-world CHD BN in Fig. 3. The MPD JT with assigned BN CPTs is shown in Fig. 5. The CPTs identified by our architecture are listed in Fig. 8. Apply any probabilistic inference algorithm to physically construct these CPTs. By definition, Fig. 18 is a MSBN for the CHD BN.

We now establish the correctness of Algorithm 3.
Lemma 6 Given as input a $B N D$, the output $\left\{B_{1}, B_{2}, \ldots, B_{n}\right\}$ of Algorithm 3 is a MSBN.

Proof The claim holds immediately by Lemma 5.

It is worth emphasizing that the local BNs have been shown in Theorems 4 and 5 to possess two favourable features, namely, the local BNs are sound and they preserve all conditional independencies of the original BN onto the context of the variables in each JT node. Note that recursive conditioning (Allen and Darwiche 2003) can also be used to build the CPTs in step 4 of Algorithm 3. Recursive conditioning was recently introduced as the first any-space algorithm for exact inference in BNs. Recursive conditioning finds an optimal cache factor to store the probability distributions under different memory constraints. The experimental results in Allen and Darwiche (2003) show that the memory requirements for inference in many large real-world BNs can be significantly reduced by recursive conditioning. Therefore, recursive conditioning allows for performing exact inference in the situations previously considered impractical (Allen and Darwiche 2003).

The significance of our suggestion is not aimed at an improvement in MSBN computational efficiency. Instead, an automated procedure for the semantic modeling of MSBNs overcomes the recently acknowledged problems with manually constructing MSBNs (Xiang et al. 2000).

Our second practical application of local BNs concerns $D C$ (Dechter 1996; Li and D'Ambrosio 1994; Zhang 1998). MSBNs are well established in the probabilistic

Table 5 The computation needed in DC to process five localized queries in the original CHD BN in Fig. 3 versus the local BNs in Fig. 18


reasoning community due, in large part, to the presence of localized queries (Xiang 1996, 2002; Xiang and Jensen 1999). That is, practical experience has previously demonstrated that queries tend to involve variables in close proximity within the BN (Xiang et al. 1993). We conclude our discussion by showing how our semantic architecture allows DC to exploit localized queries.

DC is usually better than JT propagation, if one only is interested in updating a small set of non-evidence variables (Madsen and Jensen 1999), where small is shown empirically to be twenty or fewer variables in Zhang (1998). However, DC processes every query using the original BN. Therefore, it is not exploiting localized queries.

Our semantic architecture models the original BN as a set of local BNs, once the actual probability distributions corresponding to the identified CPT labels have been constructed in computer memory. Hence, DC techniques can process localized queries in local BNs. The following empirical evaluation is styled after the one reported by Schmidt and Shenoy (1998).

Example 28 We suggest that the CHD BN in Fig. 3 be represented as the smaller local BNs in Fig. 18, after the physical construction of CPTs $p(b), p(f), p(g), p(g \mid f)$ and $p(h \mid g)$. Table 5 shows the work needed by DC to answer five localized queries using the original CHD BN of Fig. 3 in comparison to using the local BNs of Fig. 18.

While it is acknowledged that our suggestion here is beneficial only for localized queries, practical experience with BNs, such as in neuromuscular diagnosis (Xiang et al. 1993), has long established that localized queries are a reality.

# 7 Conclusion 

Unlike all previous JT architectures (Jensen et al. 1990; Lauritzen and Spiegelhalter 1988; Madsen and Jensen 1999; Shafer and Shenoy 1990), we have proposed the first architecture to precisely model the processing of evidence in terms of CPTs. The key advantage is that we can identify the labels of the messages significantly faster than the probability distributions themselves can be built in computer memory. For instance, in the medical BN for CHD, our architecture can identify all messages to be propagated in the JT in less time than it takes to physically construct one message (see Example 18). We can assist LAZY propagation (Madsen and Jensen 1999), which interlaces semantic modeling with physical computation, by uncoupling these two independent tasks. Treating semantic modeling and physical computation as being dependent practically ensures that LAZY will perform probability propagation unnecessarily slowly. When exploiting barren variables and independencies induced

by evidence, Examples 19 and 20 explicitly demonstrate that LAZY forced a node to wait for the physical construction of a non-empty message that was irrelevant to its subsequent message computation. These irrelevant non-empty messages are identified by our first work schedule, as depicted in Figs. 13 and 14. Another advantage of allowing semantic modeling to scout the structure in the JT is our second work schedule, which presents the empty messages propagated from non-leaf JT nodes, such as shown in Fig. 16. This second work schedule is beneficial as was demonstrated in Example 22, where LAZY forced a receiving node to wait for the identification of an empty message that would be neither constructed nor sent. Finally, to send a message from one node to a neighbour, LAZY does not eliminate any variables at the sending node until all messages have been received from its other neighbours (see Example 23). Our third work schedule lists those variables that can be eliminated before any messages are received, as the screen shot in Fig. 17 indicates. Besides the real-world BN for CHD, we also evaluated our architecture on four benchmark BNs, called Alarm, Insurance, Hailfinder and Mildew. The experimental results reported in Tables 2, 3 and 4 are very encouraging. The important point, with respect to JT probability propagation, is that our architecture can assist LAZY by saving time, which is the measure used to compare inference methods in Madsen and Jensen (1999).

Even when modeling inference not involving evidence, our architecture still is useful to the MSBN technique and to the DC techniques. We have shown that our JT propagation architecture is instrumental in developing an automated procedure for constructing a MSBN from a given BN. This is a worthwhile result, since several problems with the manual construction of a MSBN from a BN have recently been acknowledged (Xiang et al. 2000). We also have suggested a method for exploiting localized queries in DC techniques. Practical experience, such as that gained from neuromuscular diagnosis (Xiang et al. 1993), has demonstrated that queries tend to involve variables in close proximity within a BN. Our approach allows DC to process localized queries in local BNs. The experimental results in Table 5 involving a realworld BN for CHD show promise.

In his eloquent review of three traditional JT architectures (Jensen et al. 1990; Lauritzen and Spiegelhalter 1988; Shafer and Shenoy 1990), Shafer (1996) writes that the notion of probabilistic conditional independence (Wong et al. 2000) does not play a major role in inference. More recently, the LAZY architecture has demonstrated a remarkable improvement in efficiency over the traditional methods by actively exploiting independencies to remove irrelevant potentials before variable elimination. However, LAZY propagation does not utilize the independencies holding in the relevant potentials. In our architecture, we introduce the notions of parent-set and elder-set in order to take advantage of these valuable independencies. Based on this exploitation of independency information, we believe that the computationally efficient LAZY method, and the semantically rich architecture proposed here, serve as complementary examples of second-generation JT probability propagation architectures.

Acknowledgements This research is supported by NSERC Discovery Grant 238880. The authors would like to thank F.V. Jensen, Q. Hu, H. Geng, C.A. Maguire and anonymous reviewers, for insightful suggestions.

Open Access This article is distributed under the terms of the Creative Commons Attribution Noncommercial License which permits any noncommercial use, distribution, and reproduction in any medium, provided the original author(s) and source are credited.
