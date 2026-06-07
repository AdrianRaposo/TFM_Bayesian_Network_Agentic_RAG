# Belief Updating in Multiply Sectioned Bayesian Networks without Repeated Local Propagations 

Y. Xiang<br>Department of Computer Science<br>University of Regina<br>Regina, Saskatchewan<br>Canada S4S 0A2<br>yxiang@cs.uregina.ca


#### Abstract

Multiply sectioned Bayesian networks (MSBNs) provide a coherent and flexible formalism for representing uncertain knowledge in large domains. Global consistency among subnets in a MSBN is achieved by communication. When a subnet updates its belief with respect to an adjacent subnet, existing inference operations require repeated belief propagations (proportional to the number of linkages between the two subnets) within the receiving subnet, making communication less efficient. We redefine these operations such that two such propagations are sufficient. We prove that the new operations, while improving the efficiency, do not compromise the coherence.


A MSBN must be initialized before inference can take place. The initialization involves dedicated operations not shared by inference operations according to existing methods. We show that the new inference operations presented here unify inference and initialization. Hence the new operations are not only more efficient but also simpler. The new results are presented such that their connection with the common inference methods for single Bayesian networks is highlighted.
keywords: Bayesian networks, probabilistic reasoning, multi-agent inference, distributed inference, uncertain knowledge representation.

# 1 Introduction 

Bayesian networks (BNs) [14, 7] provide a coherent and effective framework for decision support systems that must function with uncertain knowledge. However, as the problem domains become larger and more complex, modeling a domain as a single BN and conducting inference in it becomes increasingly more difficult and expensive.

Multiply Sectioned Bayesian Networks (MSBNs) [24] provide one alternative to meet this challenge by relaxing the single BN paradigm. The framework allows a large domain to be modeled modularly and the inference to be performed distributively, while maintaining the coherence. The framework can be applied under the single agent paradigm [23] as well as the multi-agent paradigm [19]. It supports hierarchical model based diagnosis $[16,18]$ and modeling large systems with the object-oriented paradigm [10].

Several other frameworks for decomposition of probabilistic knowledge under a single agent paradigm has been proposed. Lam [11] proposed abstract network which replaces fragments of a BN by abstract arcs to improve inference efficiency. Geiger and Heckerman [4] presented similarity network and Bayesian multinet for representation of asymmetric independence relations. Kjaerulff [9] proposed nested junction trees to exploit independence relations induced by incoming messages of a cluster.

The focus of this paper is twofold. The first is on the inference computation in MSBNs. Evidence propagation among multiple subnets in a MSBN can be achieved by communication. During communication, each subnet exchanges belief twice with each adjacent subnet in a half-duplex fashion. According to existing inference operations [24, 18], each exchange requires repeated belief propagations in the receiving subnet. The repeated local propagation was viewed as the unavoidable price to trade communication bandwidth.

That view has proved to be limited by the new results to be presented below. In this work, we redefine these operations such that each exchange of belief requires only two belief propagations in the receiving subnet. We prove that the new operations, while improving the efficiency, do not compromise the coherence.

A MSBN needs to be initialized before evidential inference takes place. According to existing method [24], the initialization involves several operations that are not shared by inference computation. In this work, we show that the newly proposed inference operations unify inference and initialization. Therefore, the new operations not only are more efficient, but also are simpler. They allow faster run time computation as well as simplify the prototype implementation.

The second focus of this paper is on the unification of frameworks for inference in single BNs and in MSBNs. Inference in a BN can be performed effectively using its junction tree (JT) representation. Shafer [15] gives a unified presentation of Shafer-Shenoy, Lauritzen-Spiegelhalter [12] and HUGIN [8] methods.

The MSBN framework is an extension of these JT based inference methods with the HUGIN [8] method the most relevant. The theory of MSBNs and our new results can be better understood by following their connection with these methods. In our overview of MSBNs and presentation of the new results, we highlight such a connection.

We present the basic ideas underlying the MSBN framework in Section 2 with an emphasis on how they relate to JT based inference methods for BNs. A more formal review of the framework is given in Section 3. In Section 4, we establish the syntactic and semantic properties of linkage trees (the interface between subnets) which have not been treated formally before. In Section 5, we redefine the messages to be passed between subnets. The inference operations are redefined in Section 6 based on the new form of messages, and their coherence are proven. We discuss the efficience gain from the new operations in Section 7, and discuss the unification of inference and initialization in Section 8. About a dozen abbreviations frequently used in the paper are listed in Appendix.

# 2 Extending junction trees beyond single BNs 

In this section, we present intuitively the basic ideas behind the MSBN framework with an emphasis on how it relates to junction tree based inference methods for Bayesian networks (BNs). We assume that readers are familiar with the basics about representation of probabilistic knowledge using BNs and the common inference methods in BNs $[14,12,7,15]$.

A BN $S$ is a triplet $(N, D, P)$ where $N$ is a set of domain variables, $D$ is a DAG whose nodes are labeled by elements of $N$, and $P$ is a joint probability distribution (jpd) over $N . D$ encodes the assumption that each variable $x$ is independent of its nondescendants given its parents $\pi(x)$. This allows $P$ to be expressed as $P(N)=\prod_{x \in N} P(x \mid \pi(x))$. A BN can be used to model our uncertain knowledge about a domain, e.g., medical diagnosis [5], equipment trouble-shooting [6], financial forecasting [1], automated vehicles [3], etc.

Figure 1 (a) shows a digital circuit and the DAG of a BN that models the circuit is shown in (b). An example conditional probability distribution associated with the variable $f$ (output of a not gate) is given below:

![img-0.jpeg](img-0.jpeg)

Figure 1: (a) A digital circuit. (b) The DAG of a BN to model the circuit. (c) A JT of the BN.

$$
\begin{array}{ll}
P\left(f=0 \mid G_2=\text{normal}, e=0\right) = 0 & P\left(f=0 \mid G_2=\text{normal}, e=1\right) = 1.0 \\
P\left(f=0 \mid G_2=\text{faulty}, e=0\right) = 0.3 & P\left(f=0 \mid G_2=\text{faulty}, e=1\right) = 0.8
\end{array}
$$

Once observation on the domain is available, inference can be performed using the BN to estimate the states of unobserved variables. For example, we can compute the posterior probability $P(G_1 = \text{faulty} \mid a = 0, b = 1, f = 1)$ from the above BN. Well-known methods for computing such posteriors exactly include those by Lauritzen-Spiegelhalter [12], HUGIN [8] and Shafer-Shenoy [15]. These methods base their inference computation on a junction tree (JT) representation of the domain. For example, variables in the above BN can be organized into a JT of clusters in Figure 1 (c). During inference, message passing is performed first inward and then outward along the tree structure. After message passing, the posteriors for each variable can be obtained locally at any cluster that contains it. As explained by Shafer [15] (p64), the message passing can be equivalently controlled in an asynchronous fashion or a synchronous fashion initiated from a root cluster. In the HUGIN method (synchronous control), a single message passing from a cluster to

an adjacent cluster is called Absorption, the inward message passing along the entire JT is called CollectEvidence and outward passing is called DistributeEvidence.

As the problem domain becomes larger and more complex, modeling such a domain as a single BN and conducting inference in it becomes increasingly more difficult and expensive. The approach taken by multiply section Bayesian networks (MSBNs) is to explore modularity and distribution, two important factors that motivate distributed artificial intelligence (DAI) [2] and multi-agent systems [17]. The key issue then is how to determine the units for distribution such that the coherence of inference is not compromised by distribution. The junction tree representation of a single BN provides useful hints:

In a JT, each cluster consists of a subset of the domain variables. Each cluster acts as a unit/object in message passing during inference. Similarly, a MSBN partitions a large domain into a hypertree (that can be proven to be a JT) of some natural subdomains. Such subdomains become the units for distribution. Based on such a partition, the top level inference in the large domain, called CommunicateBelief (Section 6), can be performed similarly to what is performed in the JT of a single BN, namely, by an inward message passing through subdomains along the hypertree, called CollectBelief (Section 6), followed by an outward message passing, called DistributeBelief (Section 6). Note that these operations are named to correspond to the HUGIN operations.

We illustrate the idea using the above circuit example. We choose to use a digital circuit as no special domain knowledge is required. Readers should keep in mind that the example is an over-simplified one, and a MSBN is not needed in practice unless the domain is much larger than this example.

Suppose the circuit in Figure 1 (a) is organized into three components (shown as dotted boxes in Figure 2 (a)) which are spatially distributed. Hence $U_{i}(i=0,1,2)$ form a natural partition of the domain, where $U_{1}=\{a, b, c, g, h, i, G 5, G 6, G 7\}$ for example. The hypertree in this case is the hyperchain $U_{2}-U_{0}-U_{1}$.

We have seen that a MSBN partitions a large domain into a hypertree which is analogous to a JT of a single BN. This is the first level of application of the JT representation in MSBNs. On the other hand, a cluster (e.g., $\{a, b, g, G 5\}$ in Figure 1 (c)) in a JT has no internal structure (saving for a recent development [13]). The belief over a cluster is represented as a potential (non-normalized probability distribution) over all variables in the cluster. Since a subdomain in a large domain is itself large in general, representing it as a cluster is neither feasible nor necessary. Instead, a MSBN represents each subdomain as a Bayesian network called a subnet. For example, the circuit

![img-1.jpeg](img-1.jpeg)

Figure 2: (a) A digital circuit organized as three components. (b) The DAGs of three subnets of a MSBN. (c) JTs converted from the subnets.
in Figure 2 (a) can be represented by the three subnets in (b).
Since each subnet is itself a BN, inference within a subdomain can be performed in the same way as if the subnet is a normal BN. Hence in the MSBN framework, a subnet is converted into a JT and inference in it is performed by CollectEvidence and DistributeEvidence if only local observations in its subdomain are involved. For example, the three subnets in Figure 2 (b) are converted into the three JTs in (c) for local inference. This is the second level of application of the JT representation in MSBNs.

In a JT of a single BN, a message sent by a cluster $C$ to an adjacent cluster $C^{\prime}$ is a belief table over their intersection $C \cap C^{\prime}$, called sepset (which labels the link between the clusters). For example, the sepset between clusters $\{a, b, g, G 5\}$ and $\{a, b, e, G 1\}$ (Figure 1 (c)) is $\{a, b\}$. Like a cluster in a JT, a sepset has no internal structure (saving for a recent development [13]). In a large domain, the intersection of two subdomains, called a d-sepset, is also large in general. Hence, more compact representation of the d-sepset is desired. The MSBN framework represents each

d-sepset also as a JT, called a linkage tree, which allows a more efficient representation of the message passed between subdomains. This is the third level of application of the JT representation in MSBNs. Figure 3 expresses the three JTs as three boxes. Each band between a pair of boxes illustrates a d-sepset and is labeled accordingly. The d-sepset between $T_{0}$ and $T_{1}$ is represented as a linkage tree of two clusters, and that between $T_{0}$ and $T_{2}$ is represented as a trivial linkage tree of a single cluster.
![img-2.jpeg](img-2.jpeg)

Figure 3: Linkage trees for JTs of the circuit MSBN.
In a JT of a single BN, the inward/outward message passing are performed by a series of Absorptions, each of which passes a message over one sepset. In the MSBN framework, CollectBelief and DistributeBelief are performed by a series of message passings each of which is over one linkage tree and is called UpdateBelief (Section 6). A key result presented in this paper is a redesign of UpdateBelief for better conceptual clarity as well as computational efficiency.

# 3 Overview of the MSBN framework 

In this section, we present briefly the formal theory of the MSBN framework. A MSBN $M$ is a collection of Bayesian subnets that together defines a BN. $M$ represents probabilistic dependence of a total universe partitioned into multiple subdomains each of which is represented by a subnet. The partition should satisfy certain conditions to permit coherent distributed inference. One condition requires that nodes shared by two subnets form a $d$-sepset, as defined below.

Let $G_{i}=\left(N_{i}, E_{i}\right)(i=0,1)$ be two graphs. The graph $G=\left(N_{0} \cup N_{1}, E_{0} \cup E_{1}\right)$ is referred to as the union of $G_{0}$ and $G_{1}$, denoted by $G=G_{0} \sqcup G_{1}$.

Definition 1 Let $D_{i}=\left(N_{i}, E_{i}\right)(i=0,1)$ be two DAGs such that $D=D_{0} \sqcup D_{1}$ is a DAG. The intersection $I=N_{0} \cap N_{1}$ is a d-sepset between $D_{0}$ and $D_{1}$ if for every $x \in I$ with its parents $\pi$ in $D$, either $\pi \subseteq N_{0}$ or $\pi \subseteq N_{1}$. Each $x \in I$ is called a d-sepnode.

For example, in Figure 2 (b) the intersection $\{a, b, c\}$ between $D_{0}$ and $D_{1}$ is a d-sepset, so is $\{j, k\}$ between $D_{0}$ and $D_{2}$. A d-sepset is a sufficient information channel for passing all relevant

evidence from one subnet to another. Formally, a pair of subnets are conditionally independent given their d-sepset.

Just as the structure of a BN is a DAG, the structure of a MSBN is a multiply sectioned DAG (MSDAG) with a hypertree organization:

Definition 2 A hypertree MSDAG $\mathcal{D}=\bigsqcup_{i} D_{i}$, where each $D_{i}$ is a connected $D A G$, is a connected DAG constructible by the following procedure:

Start with an empty graph (no node). Recursively add a $D A G D_{k}$, called a hypernode, to the existing MSDAG $\bigsqcup_{i=0}^{k-1} D_{i}$ subject to the constraints:
[d-sepset] For each $D_{j}(j<k)$, $I_{j k}=N_{j} \cap N_{k}$ is a d-sepset when only $D_{j}$ and $D_{k}$ are considered. [local covering] There exists $D_{i}(i<k)$ such that, for each $D_{j}(j<k ; j \neq i)$, we have $I_{j k} \subseteq N_{i}$. For an arbitrarily chosen such $D_{i}, I_{i k}$ is the hyperlink between $D_{i}$ and $D_{k}$ which are said to be adjacent.

It can be proven [21] that if each hypernode $D_{k}$ of a hypertree MSDAG is replaced by the cluster $N_{k}$ and each hyperlink between $D_{j}$ and $D_{k}$ is replaced by the d-sepset $I_{j k}$, then the resultant is a JT. The DAGs in Figure 2 (b) is organized into the trivial hypertree MSDAG in Figure 4 (a) where each hypernode is labeled by a DAG and each hyperlink is labeled by a d-sepset. Figure 4 (b) depicts a more general hypertree MSDAG. A hyperlink is a sufficient information channel for passing all relevant evidence from one side of hyperlink to the other. Formally, given a hyperlink, the two subtrees connected through the link are conditionally independent.
![img-3.jpeg](img-3.jpeg)

Figure 4: (a) The hypertree MSDAG of the circuit MSBN. (b) A MSDAG of a more general topology.

In a MSDAG, a non-d-sepnode occurs only once, and a d-sepnode has multiple occurrences one at each DAG involved. For each d-sepnode, at least one occurrence in one DAG has all its parents in the entire MSDAG, which is ensured by the d-sepset condition. A MSBN is defined as follows:

Definition 3 A MSBN $M$ is a triplet $M=(\mathcal{N}, \mathcal{D}, \mathcal{P}) . \mathcal{N}=\bigcup_{i} N_{i}$ is the total universe where each $N_{i}$ is a set of variables. $\mathcal{D}=\bigsqcup_{i} D_{i}$ (a hypertree MSDAG) is the structure where nodes of

each $D A G D_{i}$ are labeled by elements of $N_{i}$. For each $x \in \mathcal{N}$, its occurence with the most parents (breaking ties arbitrarily) $\pi(x)$ is associated with a probability distribution $P(x \mid \pi(x))$, and each other occurrence is associated with a constant (trivial) distribution. $\mathcal{P}=\prod_{i} P_{D_{i}}\left(N_{i}\right)$ is the jpd, where $P_{D_{i}}\left(N_{i}\right)=\prod_{x \in N_{i}} P(x \mid \pi(x))$ is a local distribution over $N_{i}$. Each triplet $S_{i}=\left(N_{i}, D_{i}, P_{D_{i}}\left(N_{i}\right)\right)$ is called a subnet of $M . S_{i}$ and $S_{j}$ are adjacent if $D_{i}$ and $D_{j}$ are adjacent.

Inference in a MSBN can be performed more effectively on a compiled representation, called linked junction forest (LJF) of belief universes (LJFBU). Each $D_{i}$ is converted into a junction tree (JT) [7] $T_{i}$ over $N_{i}$. A junction tree $T$ over $N$ is a tree whose nodes are labeled by subsets (clusters) of $N$ such that the intersection of any two clusters is contained in every cluster between them. Each link in $T$ is labeled by the intersection (sepset) of the end clusters. $D_{i}$ is converted into $T_{i}$ by moralization and triangulation. How to perform these operations is presented in [24] and is improved in [22]. The JTs obtained from DAGs in Figure 2 (b) are shown in (c).

Each cluster and each sepset in a JT is associated with a belief table: a non-normalized (hence equivalent) probability distribution. How to assign these tables will be detailed in Section 8. A belief table $B_{T_{i}}\left(N_{i}\right)$ associated with a JT $T_{i}$ is defined below.

Definition 4 Let $T$ be a $J T$ over a set $N$ of variables. The belief table of $T$, denoted by $B_{T}(N)$, is defined as $B_{T}(N)=\prod_{C} B_{C}(C) / \prod_{S} B_{S}(S)$ where each $C$ is a cluster with the belief table $B_{C}(C)$ and each $S$ is a sepset with the belief table $B_{S}(S)$.

A triplet $\mathcal{T}_{i}=\left(N_{i}, T_{i}, B_{T_{i}}\left(N_{i}\right)\right)$ is called a junction tree of belief universes (JTBU) [7]. We shall sometimes refer to a JTBU as simply a JT if no confusion may arise. Proposition 5 states the semantics of a JTBU from one perspective and is needed later. Let $P(N)$ be a probability distribution over $N$ and $T$ be a JT over $N . T$ is an $I$-map of $P$ if for any disjoint subsets $X, Y$, $Z$ of $N$, that $X$ and $Y$ are independent given $Z$ according to $P$ implies that clusters containing $X$ and $Y$ are separated in $T$ by sepsets contained in $Z$. See [14] for a general discussion on I-maps and [20] for JTs as I-maps.

Proposition 5 Let $P(N)$ be a probability distribution over $N$. Let a JT T over $N$ be an I-map of $P$. Then $B_{T}(N)$ is equivalent to $P(N)$ if for each cluster and each sepset in $T$, the corresponding belief table is equivalent to the marginalization of $P(N)$ over the corresponding subset of variables.

A LJFBU has the same hypertree organization as its deriving MSBN. Each hypernode is a JTBU converted from its deriving subnet. Each hyperlink includes a linkage tree converted from its

deriving d-sepset. Here we give a definition equivalent to (but computationally less efficient than) that in [19]. The proof of equivalence is trivial.

Definition 6 Let $I$ be the d-sepset between JTs $T_{a}$ and $T_{b}$ in a LJF. A linkage tree $L$ of $T_{a}$ with respect to $T_{b}$ is constructed as follows:

Initialize $L$ to $T_{a}$. Repeat the following on clusters of $L$ until no variable can be removed:
(1) Remove a variable $x \notin I$ if $x$ is contained in a single cluster $C$.
(2) If $C$ becomes a subset of an adjacent cluster $D$ after (1), union $C$ into $D$.

Each cluster $l$ in $L$ is a linkage. Define a cluster in $T_{a}$ that contains $l$ as its linkage host and break ties arbitrarily.

For the circuit MSBN, the linkage trees $L_{1}$ between $T_{0}$ and $T_{1}$ and $L_{2}$ between $T_{0}$ and $T_{2}$ are shown in Figure 5. The thick grey links illustrate how each linkage relates to its two linkage hosts.
![img-4.jpeg](img-4.jpeg)

Figure 5: Linked junction forest for the circuit MSBN.
A triplet $\mathcal{L}_{i}=\left(I, L, B_{L}(I)\right)$ is called a linkage tree of belief universes (LTBU), where $B_{L}(I)$ is a belief table associated with $L$. How to assign belief tables for clusters and sepsets of a LTBU is detailed in Sections 4 and 8.

A common question on MSBN is whether the JTs in a linked junction forest can be merged into a single JT by simply adding links between clusters in different JTs. The JTs can certainly be constructed such that they can be merged. However, this implies that each d-sepset will be represented as a single unit/cluster (without explicit internal structure). The consequence is that clusters of each JT will be larger and the inference computation will be more expensive.

When a d-sepset is represented as a LTBU, such as $L_{1}$ in Figure 5, it allows more compact representation of belief over the d-sepset, smaller clusters of JTs being linked, and more efficient inference. On the other hand, the JTs so constructed cannot be merged into a single JT. For example, $T_{i}(i=0,1,2)$ in Figure 5 cannot be merged into one JT by adding links between clusters in different JTs.

More discussion on $\mathcal{L}_{i}$ follows in Section 4. A LJFBU is then defined as:

Definition 7 Let $M$ be a MSBN. A LJFBU $F$ derived from $M$ is a triplet $F=\left(\mathcal{T}, \mathcal{L}, \mathcal{P}^{\prime}\right) . \mathcal{T}$ is a set of JTBUs each of which is derived from a subnet in $M$. The JTBUs are organized into a hypertree isomorphic to the hypertree MSDAG of $M . \mathcal{L}$ is a set of LTBUs each of which is derived from a pair of adjacent JTBUs in the hypertree. $\mathcal{P}^{\prime}=\prod_{i} P_{T_{i}}\left(N_{i}\right) / \prod_{k} P_{L_{k}}\left(I_{k}\right)$ is the joint system belief (JSB), where each $P_{T_{i}}\left(N_{i}\right)$ is the belief table of a JTBU and each $P_{L_{k}}\left(I_{k}\right)$ is the belief table of a LTBU.

The structure of a LJFBU is a LJF consisting of its JTs and linkage trees. In Section 8, we will detail how to assign belief tables such that the JSB of a LJFBU is equivalent to the jpd of its deriving MSBN.

# 4 Properties of linkage trees 

In this section, we formally establish the syntactic and semantic properties of linkage trees.
A linkage tree is an alternative representation of the d-sepset. The procedure in Definition 6 may not be able to remove all the non-d-sepnodes and in that case a linkage tree is undefined. The condition under which a linkage tree is well defined and how to satisfy that condition are presented in [22]. Here, we assume that a linkage tree is well defined when the procedure in Definition 6 terminates.

Proposition 8 shows that a linkage tree is a JT:
Proposition 8 A linkage tree constructed according to Definition 6 is a junction tree.
Proof:
After removal of a variable contained in a single cluster $C$ of a JT, the resultant graph is still a JT. If such removal renders $C$ a subset of an adjacent cluster $D$, then union of $C$ into $D$ neither changes any sepset between $C$ and its neighbor clusters (other than $D$ ), nor changes any sepset between $D$ and its neighbor clusters (other than $C$ ). Hence the graph obtained after steps (1) and (2) is a JT.

Furthermore, the linkage tree preserves the I-mapness as shown in Proposition 9:
Proposition 9 Let $L$ be a linkage tree between a pair of JTs in a LJF and I be the d-sepset. Then $L$ is an I-map over I with respect to the distribution of either JT.

Proof:
Let $T$ be one of the JTs. We show that the graphical separation between variables in $I$ portrayed by $T$ is unchanged during construction of $L$ from $T$.

In step (1) of Definition 6, the removal of $x$ is irrelevant to the graphical separation among elements of $I$.

In step (2), union of $C$ into $D$ still leaves $C$ contained in a cluster. Thus removal (union) of $C$ does not alter the graphical separation among elements of $I$.

Definition 7 does not specify how a belief table for a linkage tree is defined. It is defined as follows:

Definition 10 Let $\left(N, T, B_{T}(N)\right)$ be a $J T B U$ and $I \subset N$ be its d-sepset with another JTBU. Let $L$ be a linkage tree over $I$ obtained from $T$. For each linkage $l$ in $L$ of host $C$ in $T$, define its belief table $B_{l}(l)=\sum_{C \backslash l} B_{C}(C)$. For each sepset $q$ in $L$, define its belief table $B_{q}(q)=\sum_{l \backslash q} B_{l}(l)$, where $l$ is any one of the two linkages whose sepset is $q$. Then the belief table of $L$ is $B_{L}(I)=\prod_{l} B_{l}(l) / \prod_{q} B_{q}(q)$.

For example, the belief of $L_{1}$ in Figure 5 can be defined from belief tables in $T_{1}$. For linkage $\{b, c\}$, its belief table is obtained from the belief table of its host cluster $\left\{b, c, h, G_{6}\right\}$ through marginalization. For linkage $\{a, b\}$, its belief table is obtained from that of $\left\{a, b, g, G_{5}\right\}$.

The semantics of a LTBU is established by Proposition 11. A JTBU is internally consistent if $\sum_{C \backslash S} B_{C}(C), \sum_{Q \backslash S} B_{Q}(Q)$ and $B_{S}(S)$ are equivalent for every adjacent clusters $C$ and $Q$ with sepset $S$.

Proposition 11 Let $\left(N, T, B_{T}(N)\right)$ be an internally consistent JTBU and $\left(I, L, B_{L}(I)\right)$ be a LTBU obtained from $\left(N, T, B_{T}(N)\right)$. Then $B_{L}(I)$ is a marginalization of $B_{T}(N)$.

Proof:
By Proposition 8, $L$ is a JT. By Proposition 9, $L$ is an I-map over $I$. From Proposition 5, the result follows.

# 5 Extending linkage belief 

In this section, we extend the linkage belief defined in Definition 10 such that more efficient belief propagation (than the existing methods) between JTBUs can be supported. The extended belief for each linkage is a combination of the original linkage belief with the belief of a sepset in the linkage tree. First, we introduce the peer sepset of a linkage used to signify which sepset belief should be combined with which linkage belief:

Definition 12 Let $L$ be a linkage tree between a pair of JTs in a LJF. Convert $L$ into a rooted tree by select a node $l$ arbitrarily as the root and direct links away from it. For each node $l^{\prime} \neq l$ in $L$, assign its sepset with its parent node as the peer sepset of $l^{\prime}$.

For example, in Figure 5, there are two linkages in $L_{1}$. If we select linkage $\{a, b\}$ as the root, then $\{a, b\}$ has no peer assigned to it, and the sepset $\{b\}$ becomes the peer of linkage $\{b, c\}$. We extend the linkage belief from Definition 10 as follows:

Definition 13 Let $L$ be a linkage tree with linkage and sepset belief defined as Definition 10, and linkage peers defined as Definition 12. For each node $l$ in $L$ with peer $q$, the extended linkage belief is $B_{l}^{*}(l)=B_{l}(l) / B_{q}(q)$, and for the node $l$ without peer, define $B_{l}^{*}(l)=B_{l}(l)$.

As an example, consider $L_{1}$ in Figure 5 using the above peer assignment. The extended belief for linkage $\{b, c\}$ will be $B_{\{b, c\}}(b, c) / B_{\{b\}}(b)$, and the extended belief for linkage $\{a, b\}$ will be $B_{\{a, b\}}(a, b)$.

The semantics of extended linkage belief is shown in Proposition 14. The proof is trivial.

Proposition 14 Let $L$ be a linkage tree. Then $B_{L}(I)$, as defined in Definition 10, can be expressed in terms of extended linkage belief as $B_{L}(I)=\prod_{l} B_{l}^{*}(l)$, where each $l$ is a linkage in $L$.

The linkage belief by Definition 10 is equivalent to the HUGIN belief representation. In this representation, the belief on each sepset is repeated in the linkage belief tables. During evidence propagation between JTBUs, we have to remove this redundant information, which is a main contributing factor that causes the complication of existing inference operations for MSBNs. The extended linkage belief removes this redundancy before propagation. Hence it is similar to the Shafer-Shenoy belief representation (although no link buffer storage is used as S-S scheme does). We shall see that by using extended linkage belief tables as messages between JTBUs during inference, belief propagation between JTBUs can be performed more efficiently than the existing methods. We assume explicit storage of extended linkage belief $B_{l}^{*}(l)$, while $B_{l}(l)$ will only be used as a conceptual object in our analysis.

# 6 Inference operations 

In this section, we redefine inference operations in $[24,19]$ based on extended linkage belief. First, we redefine the operation AbsorbThroughLinkage. The effect of the operation is to propagate belief from one linkage host to the other.

Operation 15 (AbsorbThroughLinkage) Let $l$ be a linkage in a linkage tree $L$ between JTBUs $\mathcal{T}_{a}$ and $\mathcal{T}_{b}$. Let $C_{a}$ and $C_{b}$ be the corresponding linkage host of $l$ in $T_{a}$ and $T_{b}$. Let $B_{l}^{*}(l)$ be the

extended linkage belief associated with $l$, and $B_{C_{b}}^{*}(l)$ be the extended linkage belief on $l$ defined in $C_{b}$.

When AbsorbThroughLinkage is called on $C_{a}$ to absorb from $C_{b}$ through l, perform the following:
(1) Updating host belief: $B_{C_{a}}^{\prime}\left(C_{a}\right)=B_{C_{a}}\left(C_{a}\right) * B_{C_{b}}^{*}(l) / B_{l}^{*}(l)$.
(2) Updating linkage belief: $B_{l}^{*^{\prime}}(l)=B_{C_{b}}^{*}(l)$.

Due to the use of extended linkage belief, the normal concept of consistency as used in [24] does not apply any more. We extend it to define the concept of e-consistency:

Definition 16 Let $l$ be a linkage between JTBUs $\mathcal{T}_{a}$ and $\mathcal{T}_{b}$. Let $C_{a}$ be the linkage host of $l$ in $T_{a}$. $C_{a}$ and $l$ are said to be e-consistent if $\sum_{C_{a} \backslash l} B_{C_{a}}\left(C_{a}\right)=B_{l}(l)$.

Note that $B_{l}(l)$ is not the belief table associated with $l$. Instead, $B_{l}^{*}(l)$ is. We show several properties of AbsorbThroughLinkage:

Proposition 17 After AbsorbThroughLinkage is performed, the following hold:
(1) The joint system belief is invariant.
(2) $C_{b}$ and $l$ are e-consistent.
(3) If $C_{a}$ and $l$ were e-consistent before AbsorbThroughLinkage is performed, then $C_{a}$ and $l$ are also e-consistent after.

Proof:
(1) Denote the JSB by $B_{F}(\mathcal{N})$. After AbsorbThroughLinkage, the new JSB is

$$
\begin{aligned}
B_{F}^{\prime}(\mathcal{N}) & =B_{F}(\mathcal{N}) *\left[B_{C_{a}}^{\prime}\left(C_{a}\right) / B_{C_{a}}\left(C_{a}\right)\right] /\left[B_{l}^{*^{\prime}}(l) / B_{l}^{*}(l)\right] \\
& =B_{F}(\mathcal{N}) * B_{C_{a}}^{\prime}\left(C_{a}\right) * B_{l}^{*}(l) /\left[B_{C_{a}}\left(C_{a}\right) * B_{l}^{*^{\prime}}(l)\right] \\
& =B_{F}(\mathcal{N}) *\frac{\left[B_{C_{a}}\left(C_{a}\right) * B_{C_{b}}^{*}(l) / B_{l}^{*}(l)\right] * B_{l}^{*}(l)}{B_{C_{a}}\left(C_{a}\right) * B_{C_{b}}^{*}(l)}=B_{F}(\mathcal{N})
\end{aligned}
$$

(2) This is true from the definition of AbsorbThroughLinkage.
(3) After the operation, we have

$$
\begin{aligned}
\sum_{C_{a} \backslash l} B_{C_{a}}^{\prime}\left(C_{a}\right) & =\sum_{C_{a} \backslash l} B_{C_{a}}\left(C_{a}\right) * B_{C_{b}}^{*}(l) / B_{l}^{*}(l) \quad \text { (def. of AbsorbThroughLinkage) } \\
& =\left[B_{C_{b}}^{*}(l) / B_{l}^{*}(l)\right] * \sum_{C_{a} \backslash l} B_{C_{a}}\left(C_{a}\right) \quad \text { (Proposition 4.1 [7]) } \\
& =\left[B_{C_{b}}^{*}(l) / B_{l}^{*}(l)\right] * B_{l}(l) \quad \text { (e-consistency assumption) }
\end{aligned}
$$

$$
\begin{aligned}
& =\left\{\begin{array}{cc}
\frac{B_{C_{b}}(l) / B_{q}(q)}{B_{l}(l) / B_{q}(q)} * B_{l}(l) & {[\text { if } l \text { has peer } q]} \\
\frac{B_{C_{b}}(l)}{B_{l}(l)} * B_{l}(l) & {[\text { otherwise }]}
\end{array} \quad\right. \text { (def. of extended linkage belief) } \\
& =B_{C_{b}}(l)=B_{l}^{\prime}(l)
\end{aligned}
$$

As shown by Jensen et al., the operations CollectEvidence and DistributeEvidence [8] bring a JTBU internally consistent. As they are called by several operations defined below, we combine the two into a single operation UnifyBelief as in [24] for simplicity.

Operation 18 (UnifyBelief[24]) Let $T$ be a JTBU and $C$ be any cluster in $T$. When UnifyBelief is called on $T$, initiate CollectEvidence [8] at $C$ followed by DistributeEvidence [8] from $C$.

The operation UpdateBelief propagates belief from a JTBU to another adjacent JTBU through multiple linkages (a hyperlink) between them. In the HUGIN method for inference in a JT of a single BN, evidence is propagated from a cluster to an adjacent one through a sepset by an operation called Absorption [7]. UpdateBelief is analogous to Absorption but the sender and the receiver are JTBUs, and the channel is a d-sepset/hyperlink.

Operation 19 (UpdateBelief) Let $T_{a}$ and $T_{b}$ be adjacent JTBUs, and $L$ be the linkage tree between them. When UpdateBelief is called on $T_{a}$ relative to $T_{b}$, perform the following:
(1) For each linkage $l$ in $L$, call the host of $l$ in $T_{a}$ to perform AbsorbThroughLinkage.
(2) Perform UnifyBelief at $T_{a}$.

The effects of UpdateBelief are shown in the following proposition. The consistency between a linkage tree and one of its deriving JTBU is defined in the normal way.

Proposition 20 Let $T_{a}$ and $T_{b}$ be locally consistent JTBUs of a LJFBU F. After UpdateBelief is performed in $T_{a}$ relative to $T_{b}$, the following hold:
(1) $T_{a}$ is internally consistent.
(2) The joint system belief of $F$ is invariant.
(3) $L$ is consistent with $T_{b}$.
(4) If $T_{a}$ and $L$ were consistent before UpdateBelief, they are also consistent after.

Proof:
(1) This holds due to UnifyBelief at the end of UpdateBelief.

(2) It holds since neither AbsorbThroughLinkage nor UnifyBelief changes the joint system belief.
(3) It is implied by Propositions 14 and 17 (2).
(4) It follows from Propositions 14 and 17 (3).

CollectBelief recursively propagates belief inwards (from leaves towards an initiating JTBU) on the hypertree of a LJFBU. Just as UpdateBelief is analogous to Absorption at a higher abstraction level, CollectBelief is analogous to CollectEvidence in the HUGIN method but at the hypertree level.

Operation 21 (CollectBelief) Let $T$ be a JTBU. Let caller by an adjacent JTBU or the LJFBU. When caller calls $T$ to CollectBelief, $T$ performs the following:
(1) If $T$ has no neighbor except caller, it performs UnifyBelief and return.
(2) Otherwise, for each adjacent JTBU $Y$ except caller, call CollectBelief in $Y$. After $Y$ finishes, $T$ performs UpdateBelief relative to $Y$.

Note that $Y$ is always internally consistent when $T$ performs UpdateBelief relative to $Y$ due to UnifyBelief in step (1) and in UpdateBelief.

DistributeBelief recursively propagates belief outwards (from an initiating JTBU towards leaves) on the hypertree of a LJFBU. DistributeBelief is analogous to DistributeEvidence in the HUGIN method but at the hypertree level.

Operation 22 (DistributeBelief) Let $T$ be a JTBU. Let caller by an adjacent JTBU or the LJFBU. When caller calls $T$ to DistributeBelief, $T$ performs the following:
(1) If caller is a JTBU, performs UpdateBelief relative to caller.
(2) For each adjacent JTBU $Y$ except caller, call DistributeBelief in $Y$.

CommunicateBelief combines the previous two operations to bring a LJFBU into consistency. CommunicateBelief is analogous to UnifyBelief (at the JTBU level) but at the LJFBU/hypertree level.

Operation 23 (CommunicateBelief) When CommunicateBelief is initiated at an LJFBU, CollectBelief is called at any JTBU T, followed by a call of DistributeBelief at $T$.

CommunicateBelief brings a LJFBU into global consistency as defined below. It is shown in Theorem 25.

Definition 24 A LJFBU $F$ is globally consistent if each JTBU is internally consistent and each linkage tree is consistent with each of the two corresponding JTBUs.

Theorem 25 After CommunicateBelief in a LJFBU F, F is globally consistent.

Proof:
Let $Y$ be any JTBU in $F$ other than $T$ as referred in Operation 23. Let $Y^{\prime}$ be the adjacent JTBU of $Y$ on the path between $Y$ and $T$ in the hypertree. Let $L$ be the linkage tree between $Y^{\prime}$ and $Y$. See Figure 6 for illustration.
![img-5.jpeg](img-5.jpeg)

Figure 6: Illustration of proof for Theorem 25.
After CollectBelief at $T$, each JTBU $Y$ is internally consistent (due to Proposition 20 (1)), and is consistent with $L$ (due to Proposition 20 (3)).

After DistributeBelief at $T$, each JTBU $Y^{\prime}$ is internally consistent (due to Proposition 20 (1)), is consistent with $L$ (due to Proposition 20 (3)), and the corresponding JTBU $Y$ is also consistent with $L$ (due to Proposition 20 (4)).

As discussed in [19], CommunicateBelief is performed once for a while after evidence has been entered into different JTBUs. The operation ensures that local belief at each JTBU is consistent with evidence accumulated in the entire LJFBU.

# 7 Efficiency gain from new operations 

What efficiency gain do the new operations provide?
According to the definition of CommunicateBelief, UpdateBelief is performed twice for each hyperlink of the LJFBU, and consumes a major portion of the communication computation. In the original version of UpdateBelief [24], a local belief propagation (DistributeEvidence) is performed in the receiving JTBU after each AbsorbThroughLinkage ${ }^{1}$. Hence as many propagations as the number $|L|$ of linkages in the linkage tree $L$ are performed for each execution of UpdateBelief.

The UpdateBelief defined in Operation 19 performs UnifyBelief once (two local propagations) no matter how many linkages are contained in the linkage tree. It improves the efficiency by a

[^0]
[^0]:    ${ }^{1}$ UnifyBelief consists of two local propagations and DistributeEvidence is one of them.

factor of $|L| / 2$ relative to the original UpdateBelief [24]. The savings in computation are significant when each JTBU is large.

Alternative improvement over the original UpdateBelief has been proposed in [18]. There $|L|-1$ propagations are first performed each of which is along a chain in the JTBU, and a DistributeEvidence is performed at the end. The control of the first $|L|-1$ propagations, however, is more sophisticated in that each chain is terminated by a different pair of clusters.

The UnifyBelief performed in the new UpdateBelief can be improved similarly: The first propagation (CollectEvidence) in UnifyBelief can be restricted to the subgraph of the JTBU that terminates at linkage hosts. The second propagation (DistributeEvidence) is the same. The amount of computation in the first propagation will be less than or equal to that in the first $|L|-1$ propagations in the alternative UpdateBelief, and the control needed is simpler than the alternative. The less amount of computation can be seen by observing that the $|L|-1$ propagations may repeat over certain sepsets in the JTBU. But the improved new UpdateBelief does not. The amount of computation of the two versions become equal if and only if the subgraph terminated by linkage hosts is a chain. Therefore, the new UpdateBelief with such modification will be superior (with respect to efficiency and simplicity in control) than that in [18].

# 8 Belief initialization 

Before inference can be performed in a LJFBU, its belief tables need to be set up such that marginal probabilities of each variable $x$ can be computed locally in any cluster of any JTBU that contains $x$. In other words, the joint system belief (JSB) of the LJFBU should be assigned equivalently to the jpd of its deriving MSBN and the LJFBU should be made globally consistent.

Definition 7 did not detail how belief tables for clusters/sepsets in the JTBUs and LTBUs are initially assigned. We present the assignment here:

The beliefs for clusters of JTBUs are assigned in the same way as common methods of inference in JTs of single BNs: For each subnet $S_{i}$, assign the probability table of each node $x$ to a unique cluster $C$ in $T_{i}$ such that $C$ contains $x$ and its parents in $S_{i}$. Then the belief table of each cluster is the product of all tables assigned to it. Each sepset in a JTBU is assigned a constant table. For each LTBU, all clusters and sepsets are assigned constant tables of proper dimensions. Then from Definitions 3 and 7 , it is trivial to show the following:

Proposition 26 The JSB defined in Definition 7 is equivalent to the jpd defined in Definition 3.

Next, we consider the issue of consistence. Clearly the LJFBU, with its JSB assigned as above, is not globally consistent. The process of rendering the LJFBU globally consistent is called initialization.

In the early work on MSBNs [24], initialization is achieved by a special operation BeliefInitialization. It in turn is supported by some special operations not shared by inference computation (e.g., NonRedundancyAbsorption and ExchangeBelief). These operations dedicated to initialization complicates the theory of MSBNs as well as the practical implementation.

We note that Theorem 25 does not assume any previous state of consistency in $F$ (compare with Theorem 14 in [19]). Therefore, it can be used both for inference as well as for initialization. In other words, after belief tables are assigned, initialization can be completed by performing CommunicateBelief. A separate set of initialization operations is thus no longer needed. We summarize this in the following corollary:

Corollary 27 CommunicateBelief (Operation 23) performed in a LJFBU before any evidence is entered is equivalent to the operation BeliefInitialization as defined in [24].

# 9 Conclusion 

MSBNs allow effective local inference by representing each subnet as a JTBU and by representing the d-sepset between a pair of subnets as a linkage tree. Given a linkage tree with $|L|$ linkages, previous inference operations require $|L|$ belief propagation in order to propagate new evidence from one JTBU to an adjacent one. Hence communication among subnets is slowed down by the use of multiple linkages. A separate set of operations different from that for inference was also used to initialize a MSBN before inference can take place. These operations complicate the theory of MSBNs and hinders its practical application.

In this paper, we redefined operations for inference in MSBNs. Using the new operations, two local propagations are sufficient for propagating evidence from one JTBU to an adjacent one no matter how many linkages there are between the two JTBUs. Thus they improve the efficiency of communication by a factor of $|L| / 2$. The computational savings are particularly significant when each subnet in the MSBN is large.

In our presentation, we have emphasized the connection between the MSBN/LJFBU representation and the standard JT representation of single BNs. At the top level, a MSBN partitions a large domain into a hypertree (a JT) of subdomains. At the next level, each subdomain is represented as a JT for local inference computation. At the intersubdomain level, each d-sepset is represented

as a linkage tree (a JT). These representations are crucial in order to perform inference in a large domain distributively, coherently, and effectively.

It has long been a puzzle to us why inference as well as initialization in JTs of single BNs can be performed using the same set of operations (CollectEvidence and DistributeEvidence) but two different sets of operations are needed for inference and initialization in MSBN/LJFBU. The new operations presented unify operations for inference and those for initialization, which simplifies the theory of MSBNs and facilitates practical implementation. These operations have been implemented in WEBWEAVR-III (freely available at "http://cs.uregina.ca/ yxiang/ww3/index.html") and tested experimentally.

The new set of operations presented in the paper is directly suited for inference in MSBNs under the multi-agent paradigm. By replacing the operation CommunicateBelief with the operation ShiftAttention as defined in [24], the modified set will be suited for inference in MSBNs under the single-agent paradigm. All the benefits as indicated above will still apply.

# Acknowledgements 

This work is supported by the Research Grant OGP0155425 from the Natural Sciences and Engineering Research Council (NSERC) of Canada. Partial writing was completed while the author was visiting Aalborg University, Denmark.

# Appendix: Frequently used abbreviations 

BN: Bayesian network
DAG: directed acyclic graph
jpd: joint probability distribution
JSB: joint system belief
JT: junction tree
JTBU: junction tree of belief universes
LJF: linked junction forest
LJFBU: linked junction forest of belief universes
LTBU: linkage tree of belief universes
MSBN: multiply sectioned Bayesian network
MSDAG: multiply sectioned DAG