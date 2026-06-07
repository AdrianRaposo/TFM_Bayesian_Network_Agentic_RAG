# Dynamic Multiagent Probabilistic Inference 

Xiangdong An ${ }^{\mathrm{a}, *}$, Yang Xiang ${ }^{\mathrm{b}}$, Nick Cercone ${ }^{\mathrm{c}}$<br>${ }^{a}$ Faculty of Computer Science, Dalhousie University<br>Halifax, Nova Scotia B3H 1W5, Canada<br>${ }^{\mathrm{b}}$ Department of Computing and Information Science, University of Guelph<br>Guelph, Ontario N1G 2W1, Canada<br>${ }^{c}$ Department of Computer Science and Engineering, York University<br>Toronto, Ontario M3J 1P3, Canada


#### Abstract

Cooperative multiagent probabilistic inference can be applied in areas such as building surveillance and complex system diagnosis to reason about the states of the distributed uncertain domains. In the static cases, multiply sectioned Bayesian networks (MSBNs) have provided a solution when interactions within each agent are structured and those among agents are limited. However, in the dynamic cases, the agents' inference will not guarantee exact posterior probabilities if each agent evolves separately using a single agent dynamic Bayesian network (DBN). Nevertheless, due to the discount of the past, we may not have to use the whole history of a domain to reason about its current state. In this paper, we propose to reason about the state of a distributed dynamic domain period by period using an MSBN. To reduce the influence of the ignored history on the posterior probabilities to a minimum, we propose to observe as many observable variables as possible in the modeled history. Due to the limitations of the problem domains, it could be very costly to observe all observable variables. We present a distributed algorithm to compute all observable variables that are relevant to our concerns. Experimental results on the relationship between the computational complexity and the length of the represented history, and effectiveness of the approach are presented.


Key words: Multiagent uncertain reasoning, Reasoning in dynamic systems, (Dynamic) Bayesian networks, Agent privacy, Exact and approximate reasoning

## 1 Introduction

For cooperative multiagent systems, one of the tasks we need to study is how multiple agents can collectively reason about the state of the problem domain based

[^0]
[^0]:    * Corresponding author. Tel.:+1-902-420-5003; fax:+1-902-496-8101.

    Email address: xan@cs.da1.ca (Xiangdong An).

on their local knowledge, local observation (evidence), and limited communication with each other. This task is referred to by some authors as distributed interpretation [1], which arises in many areas such as inventory control, power network grids, equipment monitoring, smart house, cooperative design, battlefield assessment, and surveillance.

Multiply sectioned Bayesian networks (MSBNs) [2] provide a coherent framework for probabilistic reasoning in distributed interpretation systems with uncertainties, which have been applied in many areas such as medical diagnosis [3], equipment monitoring and diagnosis [4], and distributed network intrusion detection [5]. However, problem domains such as medical diagnosis and equipment monitoring and diagnosis are dynamic in general. MSBNs do not provide facilities to properly manage and absorb historical information in distributed dynamic domains [6]. Actually in distributed dynamic domains, if we allow the historical probabilistic messages from different subdomains to be passed over time separately, the dependencies among these separated messages would be lost. This indicates that, at least for probabilistic inference, the spatial distribution of multiagent systems conflicts with the temporal message passing requirement of dynamic domains. We have difficulty to perform probabilistic inference in dynamic multiagent systems ideally on all of the following aspects: exactness, distribution and effectiveness.

We cannot sacrifice the distribution since multiagent inference has to be done distributedly. We could make some tradeoffs between the ideallness and either the exactness or the effectiveness or both.

It has been widely recognized that the recent past is more relevant to the current state of domain than the distant past [7-9], which is called the discount of the past. In the probabilistic framework, weak influence means small effects on the posterior probabilities. In a stochastic world, the influence of the historical probabilistic knowledge would be weakened over distance (the length of influence chains), time and quantity (as many influences combine) [10,11]. In this paper, we propose to reason about the state of a dynamic multiagent domain based on its recent history, instead of its whole history. To reduce the impacts of the ignored history on the inference results, we propose to observe (gather information from) the modeled history as much as possible. In dynamic domains, some aspects of the remote past are referenced in the recent history. The more variables in the modeled history we observe, the less influence the ignored history would have on the posterior probabilities. Observing everything that is observable would reduce the impacts of the ignored remote past to a minimum. However, each observation would have a cost. It could be very expensive to observe everything. For example, although many medical laboratory tests may help improve the accuracy of a patient's diagnosis, the patient may not want to take all of them due to the cost and the potential side effects involved. To fully and efficiently take advantage of the information provided by the modeled history, we propose to observe all observable variables that are relevant to the concerned variables.

A suite of algorithms is presented to distributedly compute all observable variables that are relevant to the concerned variables, where agents' privacy is preserved. The correctness and the complexity of the set of algorithms is analyzed. To facilitate the understanding of the set of algorithms, a single agent version of the set of algorithms is presented before the multiagent version. An algorithm called BayesBall [12] was once presented to compute the requisite observations for a set of concerned variables in Bayesian networks (BNs). The requisite observations for a set $S$ of variables are those observed variables in the domain, which are relevant to the state of $S$. Bayes-Ball solves the same problem as our single agent version algorithm in the same computational complexity. Nevertheless, Bayes-Ball is different from our single agent version algorithm in that our method computes the requisite observations based on the explicit observable descendant information of nodes in the BNs. Observable descendant information can be reused once obtained. This makes our method cheaper in both time and space complexities when requisite observations for multiple sets of concerned variables need to be computed.

Experimental results on the relationship between the computational complexity and the length of the represented period, and the effectiveness of the approach are presented.

The rest of the paper is organized as follows. In Section 2, we review the related work. The necessary background knowledge is introduced in Section 3. In Section 4, the issues involved in the dynamic multiagent probabilistic inference and the proposed solution are presented. In Section 5, the set of algorithms for computing the observable relevant variables in MSBNs is presented and analyzed. Experimental results are provided in Section 6. In Section 7, the conclusion is made.

# 2 Related Work 

Both the Markov decision processes (MDPs) [13] and the partially observable Markov decision processes (POMDPs) [14] are probabilistic models for probabilistic reasoning and acting in stochastic systems. They have been extended and applied to probabilistic reasoning and acting in dynamic multiagent systems recently.

Extended from MDPs, the multiagent MDPs (MMDPs) [15] assume a full view of the global state by each agent, whereas the decentralized MDPs (Dec-MDPs) assume a different partial view of the global state by each agent [16]. In either MMDPs or Dec-MDPs, an agent can fully observe the state of the world in its view. In Dec-MDPs, agents may be allowed to communicate about their deterministic local states with costs. Though solving an MDP is P-complete, solving a Dec-MDP is NEXP-complete [16].

The decentralized POMDPs (Dec-POMDPs) [17], extended from POMDPs, are more related with our work than Dec-MDPs, where each agent only has an incomplete information about its subdomain. In Dec-POMDPs, though agents exe-

cute their local policies distributedly based on their local observations, planning is generally centralized [18]. Agents may be allowed to communicate about their observations to improve the policy computation. In Dec-POMDPs, no probabilistic messages are passed among agents. Hence, there does not exist the divided temporal probabilistic message passing problem. Solving a POMDP is EXP-complete (PSPACE-complete if the transitions are deterministic) [19], whereas solving a Dec-POMDP is NEXP-complete [16].

In POMDPs, the state is encoded in a single random variable, which is not efficient in modeling large state spaces with structures. Dynamic decision networks (DDNs) [20] have been proposed to model and solve sequential decision problems with large structured state spaces. DDNs were extended from dynamic Bayesian networks (DBNs) with decision nodes and utility nodes. Factored POMDPs [21] were proposed to represent large structured POMDPs compactly. In a factored POMDP, a DBN is used to compactly represent the transition models and observations models. In this paper, we investigate how to properly use MSBNs to compactly represent and reason about the states of the distributed partially observable dynamic domains.

In [22], an approximate inference method for DBNs, which we call Boyen-Koller (BK), was investigated. The method works on stochastic processes that are composed of weakly interacting subprocesses. In the method, the joint belief on the DBN interface is approximated by the product of marginals that correspond to respective individual subprocesses. Message passing over time is done approximately through these marginal products, whereas belief updating at each time instant is done exactly. It was shown that the approximation error remains bounded over time. Motivated by BK, a more aggressive DBN approximate inference approach, called Factored Frontier (FF), has been presented [23]. FF is very similar to BK algorithm, but instead of doing an exact belief updating at each time instant, it always works with the factored distributions.

Though the approximation error of BK is bounded over time, it is still unclear how tight the bound is [24]. The tightness of the bound is related with the strength of the interactions among subprocesses (agents). There is no guarantee on the boundness of approximation error from FF. It has been shown [24] both BK and FF are special cases of loopy belief propagation (LBP), which is not guaranteed to converge [25].

# 3 Background Knowledge 

### 3.1 Notations and Terminology

Let $X, Y$ and $Z$ be disjoint subsets of variables in $V$. We use the notation $I(X, Z, Y)_{P}$ to denote the conditional independence of $X$ and $Y$ given $Z$; thus,

$$
I(X, Z, Y)_{P} \text { iff } P(\mathbf{x} \mid \mathbf{y}, \mathbf{z})=P(\mathbf{x} \mid \mathbf{z})
$$

for any configuration $\mathbf{x}$ of $X$, and any configurations $\mathbf{y}$ and $\mathbf{z}$ of $Y$ and $Z$ such that $P(\mathbf{y}, \mathbf{z})>0$.

In a directed graph, when two arcs meet in a path, the shared node can be described as a node of tail-to-tail, head-to-tail or head-to-head.

Definition 1 Let $X, Y$ and $Z$ be disjoint subsets of nodes in a DAG G. A path $\rho$ between nodes $x \in X$ and $y \in Y$ is closed by $Z$ whenever one of the following two conditions is true: (1) there exists $z \in Z$ that is a node of either tail-to-tail or head-to-tail on $\rho$; (2) there exists a node $w$ that is a node of head-to-head on $\rho$ and neither $w$ nor any descendant of $w$ is in $Z$. If both conditions are false, then $\rho$ is rendered open by $Z$. Nodes $x$ and $y$ are d-separated by $Z$ if every path between $x$ and $y$ is closed by $Z ; X$ and $Y$ are d-separated by $Z$ iffor every $x \in X$ and $y \in Y$, $x$ and $y$ are d-separated by $Z$.

We use the notation $\langle X| Z| Y>_{G}$ to denote that $X$ and $Y$ are separated (dseparated) by $Z$ in graph $G$.

A dependency model $M$ over a set $U$ of variables is a model that can determine whether $I(X, Z, Y)_{M}$ is true, for all possible triplets of disjoint subsets $X, Y$ and $Z$. A probabilistic model, which is a complete specification of a joint probability distribution (JPD), is a dependency model.

A graph $G$ is an I-map of a dependency model $M$ over a set $V$ of variables, if there is a one-to-one correspondence between nodes in $G$ and variables in $V$ and for every disjoint subsets $X, Y$ and $Z$, we have $\langle X| Z| Y>_{G} \Rightarrow I(X, Z, Y)_{M}$. A graph is a minimal I-map if all edges in it are necessary for it to remain an I-map.

# 3.2 Bayesian Networks 

Definition 2 A Bayesian network (BN) is a triplet $(V, G, P)$, where $V$ is a set of variables, $G$ is a connected DAG, and there is a one-to-one correspondence between nodes in $G$ and variables in $V . P$ is a set of probability distributions: $P=\{P(v \mid \pi(v)) \mid v \in V\}$, where $\pi(v)$ denotes the set of parents of $v$ in $G . G$ is a minimal I-map of $P(V)$.

### 3.3 Dynamic Bayesian Networks

Definition 3 A dynamic Bayesian network (DBN) is a quadruplet

$$
G=\left(\bigcup_{t=0} V_{t}, \bigcup_{t=0} E_{t}, \bigcup_{t=0} E_{t}^{\sim}, \bigcup_{t=0} P_{t}\right)
$$

Each $V_{t}$ is a set of nodes labeled by variables, which represents the dynamic domain at time instant $t(0 \leq t<k)$. Collectively, $V=\bigcup_{t=0}^{k} V_{t}$ represents the dynamic domain over $k$ instants. Each $E_{t}$ is a set of arcs among nodes in $V_{t}$, which represents

dependencies among domain variables at time $t$. Each $E_{t}^{\rightarrow}$ is a set of temporal arcs each of which is directed from a node in $V_{t-1}$ to a node in $V_{t}(0<t<k)$. The subset of $V_{t}(0 \leq t<k) F I_{t}=\left\{x \mid x \in V_{t} \& \exists y<x, y>\in E_{t+1}^{\rightarrow}\right\}$ is called the forward interface of $V_{t}$ where $\langle x, y\rangle$ is a temporal arc directed from $x$ to $y$. The subsets of $V_{t}(0<t<k) B I_{t}=I_{t} \cup\left\{z \mid z \in V_{t} \& \exists y\left(y \in I_{t} \& z \in \pi(y)\right)\right\}$ is called the backward interface of $V_{t}$, where $I_{t}=\left\{y \mid y \in V_{t} \& \exists x\left(<x, y>\in E_{t}^{\rightarrow}\right)\right\}$. Each $D_{t}=\left(V_{t} \cup F I_{t-1}, E_{t} \cup E_{t}^{\rightarrow}\right)$ or $\left(V_{t} \cup B I_{t+1}, E_{t} \cup E_{t+1}^{\rightarrow}\right)$ is a DAG and each $P_{t}$ is a set of probability distributions

$$
P_{t}= \begin{cases}P\left(V_{0}\right), & t=0 \\ P\left(V_{t} \mid F I_{t-1}\right) \text { or } P\left(B I_{t+1} \mid V_{t}\right), & t>0\end{cases}
$$

The pair $S_{t}=\left(D_{t}, P_{t}\right)$ is called a slice of the DBN.
Figure 1 shows the structure of a DBN of $n$ slices, where $V_{1}=\left\{a_{1}, b_{1}, c_{1}, d_{1}\right\}, E_{1}=$ $\left\{\left(a_{1}, b_{1}\right),\left(b_{1}, c_{1}\right),\left(b_{1}, d_{1}\right),\left(d_{1}, c_{1}\right)\right\}, E_{1}^{\rightarrow}=\left\{\left(a_{0}, b_{1}\right),\left(d_{0}, c_{1}\right)\right\}, F I_{1}=\left\{a_{1}, d_{1}\right\}$ and $B I_{1}=\left\{a_{1}, b_{1}, c_{1}, d_{1}\right\}$. The slice of DBN at time $t=1$ is $D_{1}=\left\{V_{1} \cup F I_{0}, E_{1} \cup E_{1}^{\rightarrow}\right\}$ where $F I_{0}=\left\{a_{0}, d_{0}\right\}$. Each slice of a DBN is a BN. At any time $t=j \leq n-1$, the slices $S_{0}, S_{1}, \ldots, S_{j-1}$ represent the domain history and $S_{j+1}, \ldots, S_{n-1}$ predict the future. Evidences may be entered into $S_{0}, \ldots, S_{j}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A simple sample dynamic Bayesian network.

# 3.4 Overview of MSBNs 

In an MSBN, a set of $n>1$ agents $A_{0}, A_{1}, \ldots, A_{n-1}$ populates a total universe $V$ of variables. Each $A_{i}$ has knowledge over a subdomain $V_{i} \subset V$ encoded as a Bayesian subnet $\left(V_{i}, G_{i}, P_{i}\right)$. The collection $\left\{G_{0}, G_{1}, \ldots, G_{n-1}\right\}$ of local DAGs encodes agents' knowledge of domain dependencies. Local DAGs of an MSBN should overlap and be organized into a hypertree.

Definition 4 Let $G=(V, E)$ be a connected graph sectioned into subgraphs $\left\{G_{i}=\left(V_{i}, E_{i}\right)\right\}$. Let these subgraphs be organized into a tree $\Psi$ where each node, called a hypernode, is labeled by $G_{i}$ and each link between $G_{i}$ and $G_{j}$, called a hyperlink, is labeled by the interface $V_{i} \cap V_{j}$ such that for each pair of nodes $G_{l}$ and $G_{m}, V_{l} \cap V_{m}$ is contained in each subgraph on the path between $G_{l}$ and $G_{m}$. The tree $\Psi$ is called a hypertree over $G$.

Each hyperlink serves as the information channel between agents connected and is referred to as an agent interface. We say all variables in agent interfaces are public or shared among agents involved, and all others are private. To allow efficient and exact inference, each hyperlink should render the subdomains connected conditionally independent. It has been shown that this implies the following structural condition [6].

Definition 5 Let $G$ be directed graph such that a hypertree over $G$ exists. A node $x$ contained in more than one subgraph with its parents $\pi(x)$ in $G$ is a d-sepnode if there exists a subgraph that contains $\pi(x)$. An interface $I$ is a d-sepset if every $x \in I$ is a d-sepnode.

Theorem 1 Let $\Psi$ be a hypertree over a directed graph $G=(V, E)$. For each hyperlink I which splits $\Psi$ into two subtrees over $U \subset V$ and $W \subset V$ respectively, $U \backslash I$ and $W \backslash I$ are d-separated by $I$ if and only if each hyperlink in $\Psi$ is a d-sepset.

The overall structure of an MSBN is a hypertree MSDAG.
Definition 6 A hypertree MSDAG $G=\bigcup_{i} G_{i}$, where each $G_{i}=\left(V_{i}, E_{i}\right)$ is a DAG, is a connected DAG such that there exist a hypertree over $G$ and each hyperlink is a d-sepset.

An MSBN is composed of a hypertree MSDAG and the corresponding numerical probability distributions.

Definition 7 An MSBN $M$ is a triplet $(V, G, P) . V=\bigcup_{i} V_{i}$ is the total universe where each $V_{i}$ is a set of variables, called a subdomain. $G=\bigcup_{i} G_{i}$ is a hypertree MSDAG where nodes of each subgraph $G_{i}$ are labeled by elements of $V_{i}$. Let $x$ be a variable and $\pi(x)$ be all parents of $x$ in $G$. For each $x$, exactly one of its occurrences (in a $G_{i}$ containing $\{x\} \cup \pi(x)$ ) is assigned $P(x \mid \pi(x))$, and each occurrence in other subgraphs is assigned a unit constant potential. $P=\prod_{i} P_{i}$ is the JPD where each $P_{i}$ is the product of the potentials associated with nodes in $G_{i}$. Each triplet $S_{i}=\left(V_{i}, G_{i}, P_{i}\right)$ is called a subnet of $M$. Two subnets $S_{i}$ and $S_{j}$ are said to be adjacent if $G_{i}$ and $G_{j}$ are adjacent in the hypertree.

# 4 Issues and Solution 

### 4.1 Dynamic MSBNs

We first look at how MSBNs can be extended and applied to dynamic multiagent probabilistic inference. We propose to use an MSBN to model one time instant of a dynamic multiagent domain. The MSBNs over all time instants are called a dynamic MSBN (dMSBN).

A dMSBN is defined as in Definition 8.

Definition 8 A dynamic MSBN is a quadruplet

$$
M=\left(\bigcup_{t=0} V_{t}, \bigcup_{t=0} E_{t}, \bigcup_{t=0} E_{t}^{\rightarrow}, \bigcup_{t=0} P_{t}\right)
$$

Each $V_{t}=\bigcup_{i} V_{t, i}(0 \leq i<n)$ is the total universe at time $t$, where $V_{t, i}$ is a set of variables, called subdomain $i$ at time $t$. Each $E_{t}=\bigcup_{i} E_{t, i}$ is a set of arcs among nodes in $V_{t}$, where $E_{t, i}$ is a set of arcs among nodes in $V_{t, i}$. Each $E_{t}^{\rightarrow}=\bigcup_{i} E_{t, i}^{\rightarrow}$ is a set of temporal arcs directed from nodes in $V_{t-1}$ to nodes in $V_{t}$, where $E_{t, i}^{\rightarrow}$ is the set of temporal arcs directed from nodes in $V_{t-1, i}$ to nodes in $V_{t, i}$. The subset of $V_{t, i}$

$$
F I_{t, i}=\left\{x \in V_{t, i} \mid(\exists y)\left(<x, y>\in E_{t+1, i}^{\rightarrow}\right)\right\}
$$

is called the forward interface of $V_{t, i}$, whereas $F I_{t}=\bigcup_{i} F I_{t, i}$ is called the forward interface of $V_{t}$. The subset of $V_{t, i}$

$$
\begin{array}{r}
B I_{t, i}=\left\{y \in V_{t, i} \mid(\exists x)\left(<x, y>\in E_{t, i}^{\rightarrow}\right)\right\} \cup\left\{z \in V_{t, i} \mid(\exists y)(z \in \pi(y) \&\right. \\
\left.(\exists x)\left(<x, y>\in E_{t, i}^{\rightarrow}\right)\right)\right\}
\end{array}
$$

is called the backward interface of $V_{t, i}$, whereas $B I_{t}=\bigcup_{i} B I_{t, i}$ is called the backward interface of $V_{t}$. Each $G_{t}=\left(V_{t} \cup F I_{t-1}, E_{t} \cup E_{t}^{\rightarrow}\right)$ is a MSDAG and each $P_{t}$ is a probability distribution

$$
P_{t}= \begin{cases}P\left(V_{0}\right), & t=0 \\ P\left(V_{t} \mid F I_{t-1}\right), & t>0\end{cases}
$$

The triplet $M_{t}=\left(V_{t} \cup F I_{t-1}, E_{t} \cup E_{t}^{\rightarrow}, P_{t}\right)$ is an MSBN, called a slice of the dynamic MSBN at time $t$.

Temporal dependencies in a dMSBN only happen within the same subdomains. Hence, there exists a DBN corresponding to each subdomain (agent), where the uncertain knowledge at each time instant is represented by a BN.

Let $D_{0}$ be the MSDAG over $\left(V_{0}, E_{0}\right)$. A (stationary) dynamic MSBN can be represented by a pair ( $S_{0}, S_{\rightarrow}$ ), where $S_{0}$ is an MSBN $\left(V_{0}, D_{0}, P_{0}\right)$ and $S_{\rightarrow}$ represents how the dynamic MSBN evolves over time. $S_{0}$ and $S_{\rightarrow}$ together define

$$
P\left(V_{t} \mid V_{t-1}\right)=P\left(V_{t} \mid F I_{t-1}\right)=\prod_{v \in V_{t}} P(v \mid \pi(v)), 0<t
$$

where $P(v \mid \pi(v))$ is defined by $P\left(V_{0}\right)$ for those $v \in V_{t}$ with $\pi(v) \subseteq V_{t}$, and by $S_{\rightarrow}$ for those with $\pi(v) \subseteq F I_{t-1}$.

For a forward or a backward interface in a dMSBN, we have Lemma 1.
Lemma 1 In a dMSBN, for a forward interface $F I_{t}$, we have $<V_{0: t}\left|F I_{t}\right| V_{t+1: T}>$; for a backward interface $B I_{t}$, we have $<V_{0: t-1}\left|B I_{t}\right| V_{t: T}>$.

That is, a forward or backward interface in a dMSBN separates the past from the future.

Proof: By definition of $F I_{t}$, any path $\rho$ between a node in the future $f$ and a node in the past $p$ should be via a node $n \in F I_{t}$. Since the node $f^{\prime} \in V_{t+1}$ that is adjacent to $n$ on $\rho$ should be a child of $n$, no matter how the node $p^{\prime} \in V_{t}$ that is adjacent to $n$ on $\rho$ is connected with $n, \rho$ should be closed by $n$. Hence, $F I_{t}$ d-separates $V_{0: t}$ and $V_{t+1: T}$.

By definition of $B I_{t}$, any path $\rho$ between a node in the future $f$ and a node in the past $p$ should be via a node $n \in B I_{t}$. Node $n$ should be the child of a node $p^{\prime} \in V_{t-1}$ that is adjacent to $n$ on $\rho$. If the node $f^{\prime} \in V_{t}$ that is adjacent to $n$ on $\rho$ is a child of $n, \rho$ is closed by $n$; otherwise, $f^{\prime} \in B I_{t}$. Then, no matter how the node $f^{\prime \prime} \in V_{t: T}$ that is adjacent to $f^{\prime}$ on $\rho$ is connected with $f^{\prime}, f^{\prime}$ should block $\rho$. Hence, $B I_{t}$ d-separates $V_{0, t-1}$ and $V_{t: T}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. A dynamic MSBN extended from an MSBN: (a) An MSBN over two subdomains $G_{0}$ and $G_{1}$; (b) The first two slices of the dynamic MSBN.

Figure 2 shows a two agent MSBN extended over a distributed dynamic domain. The structure of a slice of the dynamic MSBN is shown as in (a), and the first two consecutive slices of the dynamic MSBN are shown as in (b), where each dotted box represents a subdomain. A DBN is formed in each subdomain. The temporal dependencies are signified by the $\operatorname{arcs}\left(a_{0}, a_{1}\right)$ and $\left(g_{0}, g_{1}\right)$ respectively as shown in (b). Either the forward interface $F I_{0}=\left\{a_{0}, g_{0}\right\}$ or the backward interface $B I_{1}=\left\{a_{1}, c_{1}, g_{1}, d_{1}, f_{1}\right\}$ separates the two parts it connects.

Therefore, we can construct a model to represent the distributed uncertain knowledge in a dynamic multiagent system. Next, we discuss the difficulties we face when using dMSBNs to perform inference.

# 4.2 Issues 

### 4.2.1 Decomposition Issue

The decomposition issue exists in DBNs. However, it becomes a fatal problem for probabilistic reasoning using dynamic MSBNs.

In DBNs, between any two consecutive slices, there exists an interface - a forward interface or a backward interface - that d-separates the two slices. For messages to be properly passed forward via such interfaces, the elimination should be done by eliminating nodes in the previous slice (except interface nodes) first. A junction tree (JT) obtained based on such triangulation would make interfaces complete (when forward or backward interfaces are optimal) [26]. This makes the size of the slice interface the lower bound of computational complexity of reasoning using DBNs.

This problem becomes fatal for dynamic MSBNs since it requires that all messages passed from the preceding slice to the current slice be in the form of a single JPD. This not only makes the reasoning using dMSBNs expensive, but also results in the difficulty of the distribution of multiagent inference.

# 4.2.2 Distribution Issue 

Ideally, we would like each agent to be able to maintain its own belief on its own subdomain and all agents to be able to benefit from each others' knowledge up to the relevant history. However, agents have difficulty to propagate their beliefs from one time instant to next time instant individually. The message passing separately in each subdomain would constitute loopy belief propagation. The slice interfaces at each subdomain and agent interfaces at each time instant won't d-separate the corresponding instants or subdomains.

For example, in the MSBN as shown in Figure 2 (a), the agent interface $\left\{d_{0}, e_{0}\right\}$ separates the two subdomains $G_{0}$ and $G_{1}$ it connects. Once the MSBN evolves, the corresponding interface at each new instant won't separate the corresponding subdomains any more. For example, in Figure 2 (b), the interface $\left\{d_{1}, e_{1}\right\}$ at instant 1 does not separate the two subdomains it connects because of the paths $<a_{0}, a_{1}>$ and $<g_{0}, g_{1}>$. For similar reasons, slice interfaces in each subdomain do not separate the two consecutive instants of the subdomain.

### 4.3 Local Inference

The two issues discussed above strongly imply that exact multiagent probabilistic reasoning over unbounded time periods could not be achieved by maintaining agents' belief over a finite time.

In this paper, we propose to model a dynamic multiagent domain over a period of time into an MSBN, and then reason about the state of the domain period by period exactly. For each new period, the initial prior belief of the domain is assumed. For example, the dynamic MSBN over time instants 0 and 1 as shown in Figure 2 (b) is actually an MSBN over a period of two time instants. The corresponding subdomains are $G_{0}^{\prime}$ and $G_{1}^{\prime}$ respectively. The interface between the two subdomains is $\left\{d_{0}, e_{0}, d_{1}, e_{1}\right\}$, which is the union of the corresponding agent interfaces over all instants of the period. The period could be much longer. The two consecutive

periods could overlap on some instants. Using the MSBN, the state of domain could be reasoned about period by period exactly.

Within each period, a message does not have to be passed instant by instant. There are no conflicts between the distribution of multiagent systems and the centralization of temporal message passing. The extended agent interfaces separate the two subdomains they connect. The remote historical knowledge is ignored. However, the influence of the probabilistic knowledge would become weakened over distance, time and quantity. More recent history contains more relevant information about the current state of a domain. The history of a reasonable length could contain sufficient relevant information for reasoning about the state of the domain.

In particular, by a denser observation of the modeled history, the influence of the ignored history would be reduced. We propose to observe all relevant observable variables in the modeled period to reduce the influence. A notion called the graphical observable Markov boundary (GOMB) is proposed to capture all relevant and observable variables regarding the state of a set of concerned variables.

# 5 Graphical Observable Markov Boundaries 

In this section, we define and discuss how to compute the GOMB of a set of variables in an MSBN.

### 5.1 Markov Boundaries

Due to limitation of domains, not all variables are observable. Due to limitation of bandwidth, it may be very costly to observe all observable variables. It would be ideal if we could find and only observe the relevant observable variables. The concept of Markov boundary gives us a hint.

Definition 9 [27] Let $M$ be a dependency model over a set $V$ of variables. Let $v$ be a variable such that $v \in V$. A Markov blanket $L(v)$ of $v$ is any subset $S \subset V$ of variables for which

$$
I(\{v\}, S, V \backslash S \backslash\{v\})_{M} \text { and } v \notin S
$$

A Markov blanket is called a Markov boundary $B(v)$ of $v$ if it is a minimal Markov blanket of $v$.

That is, a Markov boundary of a variable provides us with a set of variables that is relevant to the state of the variable. ${ }^{1}$

Nevertheless, finding a Markov boundary of a variable in a probability distribution may not be tractable, since the verification of conditional independencies in

[^0]
[^0]:    ${ }^{1}$ In a not strictly positive probability distribution, the Markov boundary of a variable may not be unique [28].

probabilistic models is generally infeasible. Also, in probabilistic graphical models, the graphical structures may not capture all conditional independencies in the corresponding probabilistic models. For a node in a graphical model, the union of its parents, its children and the parents of its children is generally not a Markov boundary of the node because a node may have different neighbors in different minimal I-map DAGs [27]. In particular, the concepts of Markov blanket and Markov boundary are defined only for a single variable without the observabilities of their members considered.

On the other hand, when we do inference with graphical models, we generally only take advantage of the independencies expressed by the graphical structures. In particular, conditional independencies in Bayesian network structures can be identified in polynomial time [27]. We would revise the definition of Markov boundary based on d-separation in graphical structures. The revised Markov boundary of a variable can be efficiently and uniquely obtained, which we call the graphical Markov boundary (GMB) of the corresponding variable. We then further extend it to a set of variables, and eventually introduce the graphical observable Markov boundary (GOMB) of a set of variables, which only include observable variables.

# 5.2 Graphical Markov Boundaries 

### 5.2.1 Graphical Markov Boundaries of a Single Node

Definition 10 emphasizes that we are interested in the Markov blanket and the Markov boundary defined based on d-separations on $G$, instead of independencies in $P$.

Definition 10 Let $N=(V, G, P)$ be a $B N$ where $D A G G$ is a minimal I-map of $P$. Let $v$ be a variable such that $v \in V$. A graphical Markov blanket $L(v)$ of $v$ is any subset $S \subset V$ of variables for which

$$
<\{v\} \mid S \mid V \backslash S \backslash\{v\}>_{G} \text { and } v \notin S
$$

A graphical Markov blanket is called the graphical Markov boundary $B(v)$ of $v$ if it is a minimal graphical Markov blanket of $v$.

For the graphical Markov boundary (GMB), we have Proposition 1.
Proposition 1 For a node $v$ in a $B N N=(V, G, P)$, the union $A$ of $v$ 's parents, $v$ 's children and the parents of $v$ 's children forms a graphical Markov blanket $L(v)$ of $v$ in $N$. The graphical Markov blanket is a graphical Markov boundary $B(v)$ of $v$. The graphical Markov boundary is unique.

Proof: Straightforward.

# 5.2.2 Graphical Markov Boundaries of a Set of Nodes 

Since most times we are interested in the state of a set of variables, we further extend the two concepts to a set of variables.

Definition 11 Let $N=(V, G, P)$ be a BN. Let $R$ be a set of variables such that $R \subset V$ and $R \neq \emptyset$. A graphical Markov blanket $L(R)$ of $R$ is any subset $S \subset V$ of variables for which

$$
<R|S| V \backslash R \backslash S>_{G} \text { and } R \cap S=\emptyset
$$

A graphical Markov blanket $L(R)$ is called the graphical Markov boundary $B(R)$ of $R$ if it is a minimal graphical Markov blanket of $R$.

To facilitate the description of their members, we first define the parents and children of a set of variables.

Definition 12 Let $N=(V, G, P)$ be a BN. Let $R$ be a set of variables such that $R \subset V$ and $R \neq \emptyset$. We say any node in $V \backslash R$ that is a parent of a node in $R$ is a parent of $R$, and any node in $V \backslash R$ that is a child of a node in $R$ is a child of $R$.

We have Proposition 2 regarding the members of GMB of a set of variables.
Proposition 2 Let $N=(V, G, P)$ be a BN. Let $R$ be a set of variables such that $R \subset V$ and $R \neq \emptyset$. The union $A$ of $R$ 's parents, $R$ 's children and the parents of $R$ 's children forms a graphical Markov blanket $B(R)$ of $R$ in the BN. The graphical Markov blanket $L(R)$ of $R$ is the graphical Markov boundary $B(R)$ of $R$. The graphical Markov boundary is unique.

Proof: Straightforward as the proof for Proposition 1.
Graphical Markov boundaries can only be used for relevant observation in fully observable problem domains. In partially observable problem domains, members of a GMB may not be observable.

### 5.3 Graphical Observable Markov Boundaries

In this subsection, we introduce the graphical observable Markov boundary (GOMB) of a set $S$ of variables to capture all observable relevant variables regarding the state of $S$.

### 5.3.1 Definition

In the following definition, we use $\Omega_{\text {obs }}(X)$ to denote all observable variables in a set $X$.

Definition 13 Let $N=(V, G, P)$ be a $B N$ where $G$ is a minimal I-map of $P$. Let $R$

be a set of unobservable variables such that $R \subset V$. The GOMB $B(R)$ of $R$ is a minimal subset $S(\subset V)$ of observable variables such that

$$
<R|S| \Omega_{o b s}((V \backslash S) \backslash R)>_{G}
$$

In the following discussion, we may also call the graphical Markov boundaries defined by Definitions 10 and 11 the immediate graphical Markov boundary. Regarding GOMB, we have Proposition 3.

Proposition 3 For a set $R$ of unobservable nodes in a BN $N=(V, G, P)$, its GOMB $B$ always exists and is unique. Given $B, R$ is independent of all observable nodes in $V \backslash B$, but may not be independent of all other nodes in $V \backslash B \backslash R$.

Proof: The GOMB $B$ of $R$ always exists because $I(R, S, \emptyset)$ guarantees that the set $S=\Omega_{o b s}(V)$ satisfies Equation (7).
![img-2.jpeg](img-2.jpeg)

Fig. 3. A path between $R$ and $o$ is not closed by $B_{b} \backslash\{o\}$, where the white nodes are observable and the black nodes are unobservable: (a) No observable head-to-tail or tail-tail nodes on the path are in $B_{b}$. (b) There do not exist any unobservable head-to-head nodes on the path. (c) Any observable head-to-head nodes should be in $B_{b}$.

We prove the uniqueness by contradiction. Suppose there exist at least two GOMBs $B_{a}$ and $B_{b}$ for $R$ such that $B_{a} \neq B_{b}$, and $\left|B_{a}\right| \leq\left|B_{b}\right|$. Hence, there exists at least one observable node $o \in B_{b}$ such that $o \notin B_{a}$. That is, $R$ should be d-separated from $o$ by $B_{a}$ but not by $B_{b} \backslash\{o\}$. Therefore, there should be a path between a node in $R$ and $o$ not closed by $B_{b} \backslash\{o\}$. As shown in Figure 3, since the path is not closed by $B_{b} \backslash\{o\}$, no head-to-tail or tail-to-tail nodes on the path are in $B_{b} \backslash\{o\}$ or $B_{b}$. There also should not exist any head-to-head node $f$ on the path that is not in $B_{b} \backslash\{o\}$ since otherwise the path is closed by $f$. If there is any head-to-head node on the path that is in $B_{b} \backslash\{o\}, o$ won't be d-separated from $R$ by $B_{b}$ since we have known there does not exist any head-to-tail or tail-to-tail node on the path that is in $B_{b} \backslash\{o\}$. Hence, there should not exist any head-to-head node on the path. Since $B_{a}$ d-separates $o$ from $R$, there should exist an observable node $g$ on the path that is in $B_{a}$, but not in $B_{b}$. Nevertheless, the observable node $g$ won't be d-separated from $R$ by $B_{b}$. This is in contradiction with the assumption that $<R \mid B_{b} \mid \Omega_{o b s}\left(V \backslash B_{b} \backslash R\right)>_{G}$ holds.

Since $R$ contains no observable nodes, from Equation 7 and the assumption that $G$ is a minimal I-map of $P$, we have $\langle R| B\left|\Omega_{o b s}(V \backslash B)\right\rangle_{G} \Rightarrow I\left(R, B, \Omega_{o b s}(V \backslash B)\right)_{P}$. However, $I(R, B, V \backslash B \backslash R)_{P}$ may not hold. For example, in the BN as shown in Figure 4 (a), given the GOMB of node $a B(a)=\{d\}$, node $a$ is independent of

node $b$, but not independent of node $c$.

# 5.3.2 Computation Illustration 

By computing the GOMB $B(a)$ of $a$ in Figure 4 (b), we illustrate how to compute the GOMB of a node in a BN. We then present a set of general algorithms for this computation.
![img-3.jpeg](img-3.jpeg)

Fig. 4. (a) Given the GOMB $B(a)=\{d\}$ of node $a$, $a$ may not be independent of all other nodes; (b) The computation of the GOMB of node $a$ in a BN. The white nodes are observable and the black nodes are unobservable. (c) The division of a domain $V$ by the graphical observable Markov boundary $B$ of a set $R$ of nodes.

In the BN as shown in Figure 4 (b), we first check the immediate graphical Markov boundary of $a$. Its observable child $u$ and its observable parent $i$ would be members of $B(a)$. Hence, $B(a)=\{i, u\}$. Since paths to node $a$ via unobservable parent $j$ or unobservable children $b$ and $n$ are still open, we put them in a set $T$ (initially $T=\emptyset$ ) for further processing later. Hence, $T=\{j, b, n\}$. The processing of the parents of a child node $\alpha$ of node $a$ depends on whether $\alpha$ or any of its descendants is observable.
(1) If $\alpha$ is observable (e.g. $u$ ), we process the other of its parents $(s, d)$ immediately. Since node $a$ is a processed parent of $u$, we need mark $a$ to prevent it form being processed repeatedly. Actually this is the case for all nodes put in $B(a)$ or $T$. We mark and put observable $s$ in $B(a)$ and unobservable $d$ in $T$. Hence, $B(a)=\{i, u, s\}$ and $T=\{j, b, n, d\}$. We process parents of observable child $u$ of node $a$ immediately because $u$ would be put in $B(a)$ (instead of $T$ ), which would not be further processed.
(2) If $\alpha$ is unobservable but has observable descendants (e.g. $n$ ), it should be put in $T$. Both its parents and children should be further examined.
(3) If neither $\alpha$ nor any of its descendants are observable (e.g. $b$ ), its parents and descendants need not be further processed. For example, the other parents $(d, e, g)$ of $b$ need not be examined. This is because the path from node $d, e$ or $g$ to $a$ via $b$ is closed by the absence of $b$ and any of its descendants from $B(a)$ (they are unobservable). It should be noted that, although $g$ is not examined because of $b$, it

would be examined and put in $B(a)$ as a child of $j$. This is because otherwise one other path to node $a$ via $g$ would be open.

By similarly further processing nodes in $T$ until $T$ becomes $\emptyset$, we should have the final graphical observable Markov boundary $B(a)=\{i, u, s, g, h, m, p\}$.

# 5.3.3 Division of Domain 

We say the graphical observable Markov boundary $B$ of a set $R$ of nodes separates the whole domain $V$ into 3 parts as shown in Figure 4 (c): the nodes in $B$ (the area in brick pattern), the set $X(\supseteq R$, the grey shaded area) of nodes inside $B$, and the set $O(O=(V \backslash B) \backslash X)$ of nodes outside $B$. The set $X$ of nodes inside $B$ contains all nodes in $R$, and a set $K$ of unobservable nodes which are not d-separated from $R$ by $B$. In the example above, $B(a)=\{i, u, s, g, h, m, p\}, X(a)=\{j, b, n, d, a, c, z\}$, and $O(a)=\{r, q, t, v, k, e, f\}$. Given $B, R$ is independent of $O$, observable or not, but $X$ may not necessarily be independent of $O$. For example, in the BN as shown in Figure 4 (b), given $B(a)$, node $a$ is independent of all nodes in $O(a)$. However, $b \in X(a)$ is not independent of $O(a)$ because at least node $b$ has a direct path with node $e$.

### 5.3.4 Algorithms for Computing the Observable Descendants

In the computation of GOMBs, we need to know if an unobservable node has any observable descendants. The information can be obtained by a recursive process which recursively checks descendants of an unobservable node until an observable descendant is discovered or all descendants are checked. This process is presented as Algorithms 1 and 2.

In the two algorithms, we associate each node $v$ in a BN $N$ with a variable $O_{v}$. If $v$ or any of its descendants is observable in $N, O_{v}=1$; otherwise $O_{v}=0$. Initially we set $O_{v}=-1$. We say the observability of $v$ or its descendants is unknown if $O_{v}=-1$. If a node $v$ is unobservable, we need check the observabilities of its descendants to determine the value of $O_{v}$.

Algorithm 1 initializes $O_{v}=1$ for each observable node $v$ and $O_{v}=-1$ for each unobservable node $v$. Then Algorithm 2 is called on each node $v$ where $O_{v}=-1$. Algorithm 2 is a recursive algorithm which determines if an unobservable node $v$ has any observable descendants. It does so by searching all possible descendant branches. It backtracks from a node $y$ with determined $O_{y}$ or a leaf node. When it returns, any node $x$ visited should have a determined $O_{x}$. In this algorithm, " $\vee$ " on line 4 is a boolean "or" operator.

Note this algorithm won't return even when $O_{v}=1$ is determined from one of its descendant branch. Since we want $O_{v}$ of each node $v$ in the BN, checkOD, once called, would return only after all descendant branches have been properly

searched. Hence, Algorithm 2 will be called on a node in the BN at most once. The complexity of the computation is $O(|V|)$ in the number $|V|$ of nodes in the BN.

# Algorithm 1 (computeOD) 

Input: a BN $N=(V, G, P)$.
Output: the BN $N$ where $O_{v}$ of each node $v$ in $N$ is known.
begin
1 for each node $v$ in $N$, do
2 if $v$ is observable, set $O_{v}=1$;
3 otherwise set $O_{v}=-1$;
4 for each node $v$ where $O_{v}=-1$, do
5 call checkOD $(N, v)$;
end

## Algorithm 2 (checkOD)

Procedure checkOD $(N, v)$
Input: a BN $N=(V, G, P)$ and a node $v$.
Output: Any node $x$ visited before its return has a known $O_{x}$.
begin
1 set $O_{v}=0$;
2 for each child $y$ of $v$, do
3 if $O_{y}=-1$, set $O_{y}=\operatorname{checkOD}(N, y)$;
$4 \quad O_{v}=O_{v} \vee O_{y}$
5 return $O_{v}$;
end

### 5.3.5 Algorithms for Computing GOMBs in BNs

Once we know if each unobservable node has any observable descendants, we can compute the GOMB $B$ of a set $R$ of nodes in a BN. Since nodes in $R$ are concerned, they will for sure not be in their GOMB $B$. Summarized from the computation illustration of GOMB above, the other nodes are processed as follows ( $T$ is initialized with $R$ ):
(1) For a parent node $p$ of any nodes in $T$ : if observable, put it into $B$; otherwise put it into $T$ for further processing.
(2) For an observable child node $c$ of any nodes in $T$ : put it into $B$, and for each $g$ of its parents, put it into $B$ if observable or put it into $T$ for further processing otherwise.
(3) For an unobservable child node $c$ of any nodes in $T$ : if it has observable descendants, put it into $T$ for further processing.
(4) For an unobservable child node $c$ of any nodes in $T$ : if it has no observable descendants, nothing needs to be done from this node.

All nodes put into $B$ or $T$ should be marked so that they won't be further processed a second time. Since the number of nodes in a BN is limited, $T$ will become $\emptyset$.

When $T$ is $\emptyset$, the nodes in $B$ form the GOMB of $R$. We present the idea into Algorithm 3, where "elif" represents "else if".

In Algorithm 3, lines 7, 8, 9 and 10 correspond to situation 1. Lines 11, 12 and 13 correspond to part of situation 2. Lines $14,15,16$ and 17 correspond to the other part of situation 2. Lines 18 and 19 correspond to situation 3 . Lines 5 and 6 ensure $T$ will eventually become $\emptyset$. Lines $4,8,13,15$ and 19 mark visited nodes so that they won't be processed a second time. Since nothing needs to be done for situation 4 , no lines of code correspond to it.

Algorithm 3 (ComputeGOMBinBN) Let $R$ be a set of unobservable nodes in a $B N N=(V, G, P)$. The GOMB $B(R)$ of $R$ in $N$ is returned.

```
1 set B = \emptyset, T = R;
2}\mathrm{ for each node v\in V, do
3 associate v with a variable b
4 if v\in R, set bv=1; else set bv=0;
5 while T\neq\emptyset, do
6}\mathrm{ pick v\in T and set T=T\backslash\{v\}
7 for each parent pof v where bp=0, do
8 setbp=1;
9 if p is observable, set B=B\cup\{p\}
10 else, set T=T\mp@subsup{\cup}{}{p}\mathrm{ ;
11 for each child cof v where bc=0, do
12 if c is observable, do
13 setbc=1, and B=B\mp@subsup{\cup}{}{c}\mathrm{ ;
14 for each parent gof c wherebg=0, do
15 setbg=1;
16 if g is observable, set B=B\mp@subsup{\cup}{}{g}\mathrm{ ;
17 else, set T=T\mp@subsup{\cup}{}{g}\mathrm{ ;
18 elif any descendant of c is observable, do
19 setbc=1 and T=T\mp@subsup{\cup}{}{c}\mathrm{ ;
```

Though each node is processed at most once, its neighbors may be checked for their membership of $B$ or $T$. Therefore, the GOMB of a set of nodes in a BN can be returned in a time of $O(|V|+|E|)$, where $|V|$ is the number of nodes in the BN, and $|E|$ is the number of arcs in the BN. Regarding Algorithm 3, we have Proposition 4.

Proposition 4 Let $R$ be a set of unobservable nodes in a BN $N$. Let $B$ be the set of nodes returned by Algorithm 3. Then $B$ is the GOMB of $R$ in $N$.

Proof: Initially $T=R$. Whenever a node is removed from $T$, the members of its immediate graphical Markov boundary, not processed before, are processed depending on the situations they belong to.

Once $T$ becomes $\emptyset$, all paths from any nodes in $R$ to any observable nodes in $V \backslash R \backslash B$ should have been closed by nodes in $B$. Suppose there exists a path $\rho$ between a node $r \in R$ and an observable node $x \in V \backslash R \backslash B$ not closed by $B$. That is, on the path there exist no observable head-to-tail or tail-to-tail nodes that are in $B$, there exist no unobservable head-to-head nodes, and if there exist any observable head-to-head nodes, they should be in $B$. We consider it for different cases: (1) if there exist no observable head-to-head nodes on that path, then all nodes on the path should be of head-to-tail or tail-to-tail. If any of them are observable, as shown in Figure 5 (a), at least one of them should be reached by $r$ and put in $B$ via lines 7, 8, 9 and 10; and/or lines $11,12,13,14,15,16$ and 17; and /or lines 18 and 19. This is in contradiction with the assumption that the path is not closed. If none of them is observable, $x$ should be reached by $r$ and put in $B$. This is in contradiction with the assumption that $x \in V \backslash R \backslash B$. (2) if there exist any observable head-to-head nodes that are in $B$, as shown in Figure 5 (b), from these head-to-head nodes, $x$ should be reached and put in $B$ via lines $7,8,9$ and 10; and/or lines $11,12,13,14,15$, 16 and 17; and /or lines 18 and 19 because no observable head-to-tail or tail-to-tail nodes on the path will be in $B$. This is in contradiction with the assumption that $x \in V \backslash R \backslash B$. Hence, all paths from any observable nodes in $V \backslash R$ to $R$ should have been closed.
![img-4.jpeg](img-4.jpeg)

Fig. 5. (a) There should not exist any observable head-to-tail or tail-tail nodes between $r$ and $x$; (b) If any head-to-head node is in $B, x$ can also be reached by $r$; (c) Paths separated by $b$ are also separated by some other ways. The white nodes are observable and the black nodes are unobservable.

Next we show $B$ is minimal to satisfy $<R|B| \Omega_{o b s}(V \backslash B \backslash R)>_{G}$. Suppose there exists a node $b \in B$ that could be removed, i.e. $<R|(B \backslash\{b\})| \Omega_{o b s}(V \backslash B \backslash R) \cup$ $\{b\}>_{G}$ holds. Therefore, $<R \mid(B \backslash\{b\}) \mid b>_{G}$ holds, and all paths between $R$ and $b$ should be closed by some nodes in $B$ other than $b$. As shown in Figure 5 (c), these paths can be closed either by an unobservable head-to-head node $c$, or by a head-to-tail or tail-to-tail node $p \in B \backslash\{b\}$ on the path. However, if that is the case, $b$ cannot be reached by $r$ from these paths via lines $7,8,9$ and 10; and/or lines 11, $12,13,14,15,16$ and 17; and /or lines 18 and 19 and hence $b$ should have never been in $B$.

# 5.4 Multiagent Cooperative Computation of GOMBs 

In this subsection, we provide a set of algorithms for distributed computation of GOMBs in MSBNs.

# 5.4.1 GOMB in MSBNs 

The GOMB of a set of nodes in an MSBN could appear across all Bayesian subnets. For example, in the MSBN as shown in Figure 6, the members of GOMB of $f_{0} \in G_{1}$ could appear in both $G_{0}$ and $G_{1}$. Its immediate GMB is $\left\{d_{0}, g_{0}\right\}$. If we assume $d_{0}$ is unobservable, $\left\{d_{0}, g_{0}\right\}$ is not a GOMB. We therefore need to further consider the immediate GMB of $d_{0}$. If $c_{0}, b_{0}, a_{0}$, and $e_{0}$ are all observable, the GOMB of $f_{0}$ should be $\left\{g_{0}, c_{0}, b_{0}, a_{0}, e_{0}\right\}$. If we further assume $a_{0}, a_{1}, c_{1}$ and $d_{1}$ are all unobservable, the computation would return back to $G_{1}$ and the GOMB of $f_{0}$ would further include $f_{1}$ and $g_{1}$. Hence, the computation of the GOMB of a set of nodes in an MSBN could occur in a subnet many times.
![img-5.jpeg](img-5.jpeg)

Fig. 6. A trivial MSBN over two subdomains $G_{0}$ and $G_{1}$.
In the following 3 Subsubsections, we propose a suite of algorithms to compute the GOMB $B(R)$ of a set $R$ of nodes in an MSBN $M$ of $n$ subnets. Let $N_{i}(0 \leq i<n)$ be the $n$ subnets over subdomains $V_{i}(0 \leq i<n)$, respectively. Let $A_{i}(0 \leq i<n)$ be the corresponding agents on $V_{i}(0 \leq i<n)$. For each adjacent agent $A_{k}$ of $A_{0}$, we denote $V_{k} \cap V_{0}$ by $I_{k}$.

### 5.4.2 Cooperative Computation of the Observable Descendants

We first compute the observable descendants information distributedly. Algorithm 4 is started by the system coordinator to activate the computation. It first makes some initialization by calling Algorithm 5 (line 1), where each unobservable node is assigned a value "-1", which indicates that it is still unknown if the corresponding node has any observable descendants or not. Then it calls Algorithm 6 (line 4) on each of such nodes to figure out the answer.

Algorithm 4 (multiComputeOD) An MSBN $M$ of $n$ subnets is populated by multiple agents with one at each subnet. The system coordinator does the following:
1 call multiInitialOD;
2 for each agent $A_{i}(i=0,1, \ldots, n-1)$, do
3 for each node $v$ in $V_{i}$ where $O_{v}=-1$, do
$4 \quad O_{v}=\operatorname{localOD}\left(A_{i}, v\right)$;

In an MSBN, we call a node a global leaf node if it does not have any children in any subnet DAGs. Algorithm 6 recursively checks all descendants (could be in

adjacent subnets) of an unobservable node $v$ to figure out if $v$ has any observable descendants. For computational efficiency, the backtracking happens only when either observable nodes or global leaf nodes have been reached. A node needs to call localOD at most once to figure out if it has any observable descendants. Hence, the computational complexity is $O(m n)$, where $n$ is the number of subnets in the corresponding MSBN, and $m$ is the maximum number of nodes a subnet can have. For Algorithms 4, 5 and 6, we have Proposition 5.

Algorithm 5 (multiInitialOD) Each agent $A_{i}(i=0,1, \ldots, n-1)$ does the following:
1 for each node $v$ in $V_{i}$, do
2 if $v$ is observable, set $O_{v}=1$;
3 otherwise, set $O_{v}=-1$;

Algorithm $6\left(\operatorname{localOD}\left(A_{k 0}, v\right)\right)$ Let $A_{k 0}$ be an agent with a local subnet $N_{k 0}$. A caller is either an adjacent agent $A_{s}$ or the system coordinator. When $A_{k 0}$ is called by caller on $v$, it does the following:
1 if $O_{v}=-1$, set $O_{v}=0$; else return $O_{v}$;
2 for each child $c$ of $v$, do
3 if $O_{c}=-1$, do
4 if $c$ is a shared local leaf node in $N_{k 0}$, do
5 for each adjacent $A_{j}$ containing $c$, except $A_{s}$, do
$6 \quad$ pass descendant info on $V_{k 0} \cap I_{j}$ to $A_{j}$;
$7 \quad O_{c}=\operatorname{localOD}\left(A_{j}, c\right)$;
$8 \quad O_{v}=O_{v} \vee O_{c}$;
$9 \quad$ else $O_{c}=\operatorname{localOD}\left(A_{k 0}, c\right)$;
$10 \quad O_{v}=O_{v} \vee O_{c}$;

Proposition 5 Algorithms 4, 5 and 6 determine $O_{a}$ for each node a in an MSBN. All messages passed among agents are through public nodes.

Proof: We have shown that Algorithms 1 and 2 can figure out such information for every node in a single agent BN. Algorithms 4, 5 and 6 modify Algorithms 1 and 2 by adding some multiagent cooperation mechanisms. Hence, it is sufficient if we can show such mechanisms work when computation is across different subdomains.

Algorithm 5 initializes every node in every subnet when called by Algorithm 4. Then Algorithm 6 is called by Algorithm 4 on each agent to figure out the observable descendant information for every node in the respective subdomain. Since an agent can only be activated by the system coordinator or a caller agent, the computation is performed agent by agent. That is, at one time, there is only one active agent.

In Algorithm 6, line 1 ensures that the required information will be returned properly if it has been available. Lines $4,5,6,7$ and 8 process cooperation operations

with adjacent agents. For a shared local leaf node $c$, the computation would be extended to the corresponding adjacent agents. In the corresponding agents, $O_{c}$ could have been available. If so, it is immediately returned by line 1 . All the observable descendant information on shared nodes is passed to the adjacent agents (line 6) because the observable descendant information may have been available for some of these nodes and could be required by the corresponding adjacent agents. Line 8 absorbs the observable descendant information obtained from the corresponding adjacent agents by boolean "or" ( $V$ ) operation.

# 5.4.3 Cooperative Computation of GOMBs 

Based on the observable descendant information obtained by Algorithms 4, 5 and 6, we can compute the GOMB $B(R)$ of a set $R$ of nodes in an MSBN $M$ distributedly.

In a distributed problem domain, a variable could be logically shared by different agents, but the entity represented by the variable can only physically locate in one subdomain. We call the subdomain where an entity physically exists the host subdomain of the entity and the corresponding agent its host agent. We assume a variable can only be observed by its host agent. Therefore, each agent $A_{i}$ should keep the part $B_{i}(R)$ of $B(R)$ it can observe, called the partial graphical observable Markov boundary (PGOMB) of $R$ in the corresponding subdomain, for observation.

We present a suite of algorithms to cooperatively compute GOMB in an MSBN. The system coordinator activates the computation by executing Algorithm 7, which first distributes $R$ to the corresponding agents and then call each involved agent to do some initialization by running Algorithm 8 (lines 1, 2, and 3). After that, the cooperative computation of $B(R)$ is performed by running Algorithm 9 (line 4).

Algorithm 7 (ComputeMB) An MSBN $M$ of $n$ subnets is populated by multiple agents with one at each subnet. Let $R$ be a set of nodes in $M$. The system coordinator does the following for multiple agents to figure out the GOMB $B(R)$ of $R$, which is the union of $B_{i}(R)(0 \leq i<n)$, in $M$.
1 for each agent $A_{i}$, do
2 send $R \cap V_{i}$ to $A_{i}$;
3 call $A_{i}$ to run InitializeMB;
4 call ExpandMB;

By Algorithm 8, each agent receives a set $T_{i}$ of the corresponding concerned nodes from the system coordinator for the cooperative computation of the GOMB $B(R)$ (line 1) and makes some initialization (lines 2, 3 and 4). Lines 2 and 3 associate each node $v$ with a variable $b_{v}$. If $b_{v}=1$, the node $v$ should have been processed. Since a DAG is generally multiply connected, such a marking is necessary to prevent infinite loops. Line 4 initializes the corresponding PGOMB in each subdomain.

Algorithm 8 (InitializeMB) Let $A_{i}$ be the agent over a subnet $N_{i}=\left(V_{i}, G_{i}, P i\right)$. When called by the system coordinator, it does the following:
1 receive $T_{i}=R \cap V_{i}$;
2 for each node $v$ in $V_{i}$, do
3 if $v \in R$, set $b_{v}=1$; else, set $b_{v}=0$;
4 set $B_{i}=\emptyset, Q_{i}=\emptyset$;

Algorithm 9 (ExpandMB) Let $Q_{k}(k=0,1, \ldots, n-1)$ be the set of unobservable nodes collected by agent $A_{k}(k=0,1, \ldots, n-1)$ for extended computation of GOMB. The system coordinator does the following:
1 for each agent $A_{i}$, do
2 if $T_{i}=\emptyset$, continue;
3 call $A_{i}$ to run ComputePMB;
4 for each agent $A_{i}$, do
5 call $A_{i}$ to run collectNodes;
6 if all $Q_{i}$ 's $(0 \leq i<n)$ are $\emptyset$ 's, return;
7 else, set $T_{i}^{\prime} s=Q_{i}^{\prime} s$, restart the algorithm;

Algorithm 9 calls Algorithm 10 to compute the PGOMB of $R$ in each corresponding subnet (lines 1,2 and 3 ). This is called one pass of the computation of the GOMB $B(R)$. Several passes may be needed to reach the final GOMB $B(R)$. A pass of computation of PGOMB by Algorithm 10 could be extended across different subnets. Agent $A_{i}(0 \leq i<n)$ uses $Q_{i}(0 \leq i<n)$ to receive the shared unobservable nodes from the adjacent agents when extension happens. ${ }^{2}$ In Algorithm 9, Algorithm 11 is called by each agent to collect such nodes from the the corresponding agents (lines 4 and 5). Then all $Q_{i}$ 's are checked (lines 4 and 5). If all $Q_{i}$ 's are $\emptyset$ 's, the computation is finished; otherwise, a new pass of computation has to be started in the corresponding agents.

Algorithm 10, which is very similar to Algorithm 3 except for some mechanisms for message passing among agents, performs one pass of the computation of the PGOMB $B(R)$ in a subnet. The set $H_{k 0}$ contains all unobservable nodes assigned initially and reached in computation (lines 1, 8, 16, and 19). The public nodes in $H_{k 0}$ are passed to the corresponding adjacent agents for extending the computation of $B(R)$ in other subnets (lines 20 and 21). The Algorithm 10 computes the PGOMB in an iterative way. A recursive version can recursively check the immediate GMB of each of $T_{k 0}$ members.

Algorithm 11 collects unobservable public nodes from the adjacent agents for the extended computation of the GOMB $B(R)$. Since this may not be the first pass of computation, all nodes evaluated (and hence marked) by $A_{i}$ are removed from $X$ (line 4). The set $Q_{k 0}$ are set to be $\emptyset$ in the beginning (line 1). If it remains $\emptyset$ after

[^0]
[^0]:    ${ }^{2} Q_{i}(0 \leq i<n)$ is initialized at line 4 of Algorithm 8 .

the collection, no computation is necessary in subnet $N_{k 0}$ at this time.
Algorithm 10 (ComputePMB) Let $T_{k 0}$ be a set of unobservable nodes in $N_{k 0}$. Let $H_{k 0}$ be the set used to collect the corresponding unobservable nodes involved in the pass of computation. Denote the adjacent agent of $A_{k 0}$ by $A_{k 1}, A_{k 2}, \ldots, A_{k m}$. When called by the system coordinator, the agent $A_{k 0}$ does the following to figure out the GOMB members in $V_{k 0}$ corresponding to $T_{k 0}$ :
1 set $H_{k 0}=T_{k 0}$
2 while $T_{k 0} \neq \emptyset$, do
3 pick $v \in T_{k 0}$ and set $T_{k 0}=T_{k 0} \backslash\{v\}$;
4 for each parent $p$ of $v$ where $b_{p}=0$, do
5 set $b_{p}=1$;
6 if $p$ is observable, set $B_{k 0}=B_{k 0} \cup\{p\}$;
7 else, do
$8 \quad$ set $T_{k 0}=T_{k 0} \cup\{p\}, H_{k 0}=H_{k 0} \cup\{p\}$;
$9 \quad$ for each child $c$ of $v$ where $b_{c}=0$, do
10 if $c$ is observable, do
11 set $b_{c}=1$, and $B_{k 0}=B_{k 0} \cup\{c\}$;
12 for each parent $g$ of $c$ where $b_{g}=0$, do
13 set $b_{g}=1$;
14 if $g$ is observable, set $B_{k 0}=B_{k 0} \cup\{g\}$;
15 else, do
16 set $T_{k 0}=T_{k 0} \cup\{g\}, H_{k 0}=H_{k 0} \cup\{g\}$;
17 elif any descendant of $c$ is observable, do
18 set $b_{c}=1$;
19 set $T_{k 0}=T_{k 0} \cup\{c\}, H_{k 0}=H_{k 0} \cup\{c\}$;
20 for each adjacent agent $A_{j}(j=k 1, k 2, \ldots, k m)$ of $A_{k 0}$, do
21 pass $H_{k 0} \cap I_{j}$ to $A_{j}$ over $I_{j}$;
Algorithm 11 (collectNodes) Let $A_{k 0}$ be an agent over a subnet $N_{k 0}$. Denote the adjacent agents of $A_{k 0}$ by $A_{k 1}, A_{k 2}, \ldots, A_{k m}$. When called by the system coordinator, $A_{k 0}$ does the following:
1 set $Q_{k 0}=\emptyset$;
2 for each adjacent agent $A_{j}(j=k 1, k 2, \ldots, k m)$ of $A_{k 0}$, do
3 receive a set $X$ of nodes over $I_{j}$ from $A_{j}$;
4 remove any nodes marked by $A_{k 0}$ from $X$;
$5 \quad$ set $Q_{k 0}=Q_{k 0} \cup X$;

Since the computation of $B(R)$ will finish when all nodes are visited, the computational complexity of the suite of algorithms is $O(n+m)$, where $n$ is the number of nodes in the MSBN, and $m$ is the number of arcs in the MSBN. For the suite of algorithms, we have Proposition 6.

Proposition 6 Algorithms 7, 8, 9, 10 and 11 compute and return the GOMB $B(R)$

of a set $R$ of nodes in an MSBN. All messages passed among agents are through public nodes.

Proof: The set of algorithms is different from Algorithm 3 in that they need to process message passing among agents for extended computation of the GOMB $B(R)$. To reach $B(R)$, several passes of computation could occur in one subdomain. Since we have proved the Algorithm 3 for single agent case in Proposition 4, we here need to show that the message passing and multiple passes of computation are properly done.

Only public unobservable nodes collected in the computation in a subnet could be involved in the extended computation in the adjacent agents. Such nodes are passed to the corresponding agents over their interfaces (lines 20 and 21 of ComputePMB). If any of them are already evaluated in the corresponding agents, they will be removed from the extended computation (line 4 of collectNodes). Hence, the number of nodes in a subnet that need to be evaluated will become less and less until none. The computation in each subnet will be eventually finished (line 6 of ExpandMB).

# 5.4.4 Cooperative Distribution of GOMB 

Until now, all nodes that belong to $B(R)$ should have been reached. However, they may not have been properly distributed to PGOMB $B_{i}(R)(0 \leq i<n)$.
![img-6.jpeg](img-6.jpeg)

Fig. 7. The GOMB of a set of nodes in an MSBN may not be properly distributed. (a) The 4 subnets of an MSBN. (b) The hypertree MSDAG over the DAGs in (a). The white nodes are observable and the black nodes are unobservable.

Figure 7 shows a trivial MSBN of 4 subnets $G_{0}, G_{1}, G_{2}$ and $G_{3}$, where each dotted box represent one subnet. The white nodes are observable and the black nodes are unobservable. We assume the 4 subnets are controlled by 4 agents $A_{0}, A_{1}, A_{2}$ and $A_{3}$ respectively. Suppose $A_{0}, A_{1}, A_{2}$ and $A_{3}$ are the host agents of $\{a, b, z\}$, $\{c, v, x\},\{e, f, y\}$ and $\{d, u\}$, respectively. Assume that we compute the GOMB of node $c$ in the MSBN. Since $c$ is a private node in $G_{1}$, in the first pass, only agent $A_{1}$ run ComputePMB on $G_{1}$. All other agents do not join the pass of computation. After the first pass of the computation, we get $B_{1}=\{x, u, v, y\}$, and $H_{1}=\{z, c\}$. Then the public node $z$ in $H_{1}$ is passed to the corresponding adjacent agent $A_{0}$.

$A_{0}$ uses $Q_{0}$ to hold $z$. Since $Q_{0}=\{z\}$ is not empty, ExpandMB is restarted. We get $B_{0}=\{b, x\}$, and $H_{0}=\{z, a\}$ in $G_{0}$ in the second pass of the computation. Then the public node $z$ in $H_{0}$ is passed back to the corresponding adjacent agent $A_{1}$. However, $Q_{1}$ will become $\emptyset$ since $A_{1}$ has evaluated and marked node $z$. Hence, $Q_{0}, Q_{1}, Q_{2}$ and $Q_{3}$ are all empty at this time and ComputeMB finishes. Though all members of $B(c)$ have been identified in the MSBN, they may not have been distributed to the proper $B_{i}(c)^{\prime} s$ properly. For example, $y$ and $u$ can only be observed by $A_{2}$ and $A_{3}$ respectively, but both $B_{2}(c)$ and $B_{3}(c)$ are empty. Hence, we need properly distribute the available GOMB members to the corresponding host agents.

We present a set of 3 algorithms to properly distribute GOMB $B(R)$ to PGOMB $B_{i}(R)^{\prime} s(0 \leq i<n)$. Algorithm 12 is called to start the set of algorithms, where CollectMB and DistributeMB are called one after another by an arbitrary agent. Both CollectMB and DistributeMB are recursive algorithms, which recursively collect or distribute related GOMB members from or to the corresponding agents, through agents' interfaces.

Algorithm 12 (UnifyMarkovBoundary) Let $M$ be an MSBN of $n$ subnets. The system coordinator selects an arbitrary agent $A_{r}$ to run CollectMB in $G_{r}$. After it finishes, $A_{r}$ runs DistributeMB in $G_{r}$. Finally, each agent $A_{i}$ removes nodes it cannot observe from $B_{i}(0 \leq i<n)$.

Algorithm 13 (CollectMB) Let $A_{k 0}$ be an agent over the subnet $N_{k 0}$ of an MSBN $M$. A caller can be the system coordinator or an agent $A_{s}$. Denote the additional adjacent agents of $A_{k 0}$ by $A_{k 1}, A_{k 2}, \ldots, A_{k m}$. Agent $A_{k 0}$ does the following when called by a caller:
for each agent $A_{i}(i=k 1, k 2, \ldots, k m)$, do
call $A_{i}$ to run CollectMB;
receive a set $X=B_{i} \cap I_{i}$ of nodes over $I_{i}$;
set $B_{k 0}=B_{k 0} \cup X$;
if caller is an agent $A_{s}$, do
send $A_{s}$ the GOMB members $B_{k 0} \cap I_{s}$ over $I_{s}$;

For the set of 3 algorithms for PGOMB distribution, we have Proposition 7.
Proposition 7 Let $N_{i}=\left(V_{i}, G_{i}, P_{i}\right)(0 \leq i<0)$ be the subnets of an MSBN $M$. Let $R$ be a set of unobservable nodes in $M$. Let $B(R)$ be the union of all the GOMB members reached by Algorithms 7, 8, 9, 10 and 11. Algorithms 12, 13 and 14 properly distribute the members of the GOMB $B(R)$ to the corresponding PGOMB $B_{i}(R)(0 \leq i<n)$. All messages passed among agents are through public nodes.

Proof: In a hypertree MSDAG, any nodes shared by two hypernodes $B$ and $C$ also

Algorithm 14 (DistributeMB) Let $A_{k 0}$ be an agent over the subnet $N_{k 0}$ of an MSBN M. A caller can be the system coordinator or an agent $A_{s}$. Denote the additional adjacent agents of $A_{k 0}$ by $A_{k 1}, A_{k 2}, \ldots, A_{k m}$. Agent $A_{k 0}$ does the following when called by a caller:
if caller is an agent $A_{s}$, do
receive a set $X$ of GOMB members over $I_{s}$ from $A_{s}$;
add $X$ to $B_{k 0}$;
for each agent $A_{i}(i=k 1, k 2, \ldots, k m)$, do
send $B_{k 0} \cap I_{i}$ to $B_{i}$ of $A_{i}$ over $I_{i}$;
call $A_{i}$ to run DistributeMB;
appear in every hypernode on the path between them. By recursive collection, the shared $B(R)$ members between a some agent $A_{x}$ and agent $A_{r}$ will be collected from $A_{x}$ to agent $A_{r}$ and any agents on the path between them. By recursive distribution, the shared $B(R)$ members between agent $A_{r}$ and a some agent $A_{x}$ will be distributed from $A_{r}$ to $A_{x}$ and any agents on the path between them. Hence, by recursive collection and distribution, a shared node $u \in B(R)$ should have reached every $B_{i}(R)$ where $u \in V_{i}$.

After all nodes for which $A_{i}(0 \leq i<n)$ is not a host agent are removed from $B_{i}(R)(0 \leq i<n)$, we have a set of PGOMBs that can be observed properly by each agent.

By applying Algorithms 12, 13 and 14 to the above example, we have $B_{0}=\{b\}$, $B_{1}=\{v, x\}, B_{2}=\{y\}$, and $B_{3}=\{u\}$.

Since both CollectMB and DistributeMB are called once at each subnet, and at each call, only a finite number of intersection operations are made, the computation should finish in $O(m n)$ time, where $n$ is the number of agents in the corresponding MSBN, and $m$ is the maximum number of neighbors an agent can have in the hypertree.

# 6 Experiments 

In this section, we show the effectiveness of the proposed dynamic multiagent probabilistic inference method on the simulated sequential digital circuits. We also give the relationship between the computational complexity and the length of the represented period.

### 6.1 The Sequential Digital Circuits

In sequential digital circuits, some devices may become faulty in the run time. We use the proposed dynamic multiagent inference method to detect such faulty

devices.

The synchronous sequential digital circuit as shown in Figure 8 is composed of 5 components. It has a total of 62 devices including 20 inverters, 21 and gates, 13 or gates, 1 xor gate, 3 D flip-flops, and 4 J-K flip-flops. Each component can be associated with a computational agent responsible for monitoring and troubleshooting the component. The agents can acquire local observations from sensors and reason about the values of unobservable variables within the component. Components are interfaced with each other, and observations obtained by one agent could be valuable to another agent. When modeling these components, one agent should have some variables shared with some other agents.
![img-7.jpeg](img-7.jpeg)

Fig. 8. A synchronous sequential digital circuit. Each dashed box represents one component.

# 6.2 The MSBN Model 

We monitor and diagnose the simulated circuit with a five agent MSBN over a period of four time instants (clocks). Figures 9 and 10 shows the two Bayesian subnets corresponding to component 0 and 1 , respectively, where each variable is labeled by its variable name followed by the variable's index (which readers may ignore). Each variable name is composed of a string indicating the corresponding

device or signal and a digit indicating the respective time instant. For example, in Figure 9, $f 4 \_3$ denotes the state of J-K flip flop $f 4$ in subdomain $U_{0}$ at relative time instant 3. The five Bayesian subnets of the MSBN are organized into a hypertree as shown in Figure 11.
![img-8.jpeg](img-8.jpeg)

Fig. 9. The subnet $G_{0}$ for component $U_{0}$.
![img-9.jpeg](img-9.jpeg)

Fig. 10. The subnet $G_{1}$ for component $U_{1}$.
In addition to the dependency structures, we have the following prior beliefs on representational parameters. The state of a device (flip-flops or logic gates) at a time instant is represented by a boolean variable and is either normal or abnormal. A device could become faulty (abnormal) at a probability of $1 \%$. If a device is normal at time $t=i$, it may become abnormal at $t=i+1$ with a probability of $1 \%$. If it is abnormal at time $t=i$, it will stay abnormal. A faulty device may produce correct output(s): a faulty not gate outputs correctly with a probability of

$50 \%$; a faulty and gate outputs correctly with a probability of $20 \%$; a faulty or gate outputs correctly with a probability of $70 \%$; a faulty xor gate outputs correctly with a probability of $30 \%$; and either outputs $(Q, \bar{Q})$ of a faulty flip-flop could be correct with a probability of $30 \%$.
![img-10.jpeg](img-10.jpeg)

Fig. 11. The hypertree MSDAG of the five agent MSBN.
We assume that the state of a device is not observable. We also assume that the observation of an input or output has a cost. Therefore, observing all inputs and outputs is not an option. To make the situation more challenging, we assume that not all inputs or outputs of a device are observable.

# 6.3 Lower Bound on the Length of the Modeled Period 

To detect the problems of a flip-flop in a sequential digital circuit, we need to model at least two instants so that we have the chance to observe the outputs of the flipflop. When many flip-flops are chained together and signals between them are not observable, the length of the modeled period is lower bounded by one more than the number of flip-flops such connected. For example, as shown in Figure 12, a sequence of $n$ J-K flip-flops are connected one after another, where each irregular box represents a combinational circuit receiving outputs from the preceding flip-flop and providing inputs to the posterior flip-flop except the first one only providing inputs to flip-flop $j k_{0}$ and the last one only receiving outputs from flip-flop $j k_{n-1}$. If we can only observe the variables in irregular boxes $I$ and $O_{n-1}$, we may need to model the domain over a period of at least $n+1$ instants to properly reason about the state of the domain. This is because the output $O_{n-1}$ won't be affected by the possibly problematic outputs from flip-flop J-K $j k_{0}$ within $n$ instants. That is, there exists a delay between the time when the problem happens and the time when the affected outputs are observed.
![img-11.jpeg](img-11.jpeg)

Fig. 12. A sequence of J-K flip-flops.

Therefore, the number of flip-flops that are chained together and the observability of variables between them could tell us the minimal period we need to model.

For the digital circuit as shown in Figure 8, a period of at least three instants needs to be modeled to reason about the state of the domain because the longest sequences of flip-flops where variables between them are unobservable are the sequences of two flip-flops. However, a modeled period of three instants may not give us very confident inference results for this problem domain. We show this by randomly picking and observing a period of three consecutive instants of the problem domain, where flip-flop $f_{2}$ is assumed to be faulty. Figure 8 shows all input signals and some of output signals over a period of four instants. The outputs provided here are those that could be affected by the outputs of faulty $f_{2}$ and cannot be properly predicted based on given inputs. The signal values are provided as strings of four digits. For example, "0101" beside $i_{7}$ indicates that $i_{7}$ takes values ' 0 ', ' 1 ', ' 0 ' and ' 1 ' chronologically in the period. We test on the first 3 instants.

We assume one input ( $k_{2}$ ) and all outputs ( $q_{2}, k_{5}$ ) of the faulty J-K flip-flop $f_{2}$ are unobservable. In particular, its outputs are direct or indirect inputs of another J-K flip-flop $f_{5}$, whose inputs are not observable. However, one of $f_{5}$ 's outputs $p_{5}$ is observable, and its other output $q_{5}$ is an input of an and gate $a_{i}$, whose output $e_{a}$ is observable. We underline all observable variables in Figure 8.

For a model over a period of three instants, we have the graphical observable Markov boundary $B\left(R_{0}^{3}\right)$ of $R_{0}^{3}=\left\{f_{20}, f_{21}, f_{22}\right\}$ :

$$
\begin{aligned}
& B\left(R_{0}^{3}\right)=\left\{i_{70}, i_{71}, i_{72}, i_{80}, i_{81}, i_{82}, j_{20}, q_{30}, q_{31}, q_{32}, i_{g 0}, i_{g 1}, i_{g 2}, e_{60}, e_{61}, e_{62}, i_{h 0}\right. \\
& \left.\quad i_{h 1}, i_{h 2}, i_{d 0}, i_{d 1}, i_{e 0}, i_{e 1}, i_{f 0}, i_{f 1}, i_{n 0}, i_{n 1}, p_{50}, p_{51}, p_{52}, e_{a 0}, e_{a 1}, e_{a 2}, i_{o 0}, i_{o 1}, i_{o 2}\right\}
\end{aligned}
$$

For simplicity, we do not differentiate host agents here. The graphical observable Markov boundary contains 36 variables. It is interesting that not all observable direct inputs of J-K flip-flop $f_{2}$ are contained in $B\left(R_{0}^{3}\right)$. Only $j_{20}$ at the first instant ( 0 ) are contained in $B\left(R_{0}^{3}\right)$. This is because the inputs to $f_{2}$ at instant 2 have not gone through $f_{2}$, and no any effects have been produced. Although the inputs to $f_{2}$ at instant 1 have gone through $f_{2}$, the effects of $f_{2}$ 's outputs won't be observed at $e_{a}$ or $p_{5}$ at instant 2 before these outputs go through another J-K flip-flop $f_{5}$ (i.e. any information resulted from inputs to $f_{2}$ at instant 1 are currently contained somewhere between the two J-K flip-flops, where no variables are observable). Also, although $i_{n 0}$ and $i_{n 1}$ are contained in $B\left(R_{0}^{3}\right), i_{n 2}$ and $i_{n 3}$ are not. This is because no effects of $i_{n 2}$ and $i_{n 3}$ would be observed at $e_{a}$ or $p_{5}$ within the period.

By inference based on the observation of $B\left(R_{0}^{3}\right)$ and communication among agents, J-K flip-flop $f_{2}$ is believed to be faulty with a belief of $72.65 \%$. All other devices in component $C_{2}$ are believed to be normal with beliefs over $96 \%$ except or gate $o_{6}$ $77.86 \%$. All devices in components $C_{0}, C_{1}$ and $C_{3}$ are believed to be normal with beliefs over $96.06 \%$. All devices in component $C_{4}$ are believed to be normal with beliefs over $96.06 \%$ except flip-flop $f_{5} 89.81 \%$. Though the inference indicates that

$f_{2}$ could be faulty, we may not be very confident about the result since the posterior $(72.65 \%)$ is not very positive.

# 6.4 More Than Minimal Instants 

When we monitor the circuit as shown in Figure 8 over periods of four instants, we may get better results. Based on the similar assumptions as the example above, we have the graphical observable Markov boundary $B\left(R_{0}^{4}\right)$ of $R_{0}^{4}=\left\{f_{20}, f_{21}, f_{22}, f_{23}\right\}$ :

$$
\begin{gathered}
B\left(R_{0}^{4}\right)=\left\{i_{70}, i_{71}, i_{72}, i_{73}, i_{80}, i_{81}, i_{82}, i_{83}, j_{20}, j_{21}, q_{30}, q_{31}, q_{32}, q_{33}, i_{g 0}, i_{g 1}, i_{g 2}\right. \\
i_{g 3}, e_{60}, e_{61}, e_{62}, e_{63}, i_{h 0}, i_{h 1}, i_{h 2}, i_{h 3}, i_{d 0}, i_{d 1}, i_{d 2}, i_{e 0}, i_{e 1}, i_{e 2}, i_{f 0}, i_{f 1}, i_{f 2}, i_{n 0} \\
\left.i_{n 1}, i_{n 2}, p_{50}, p_{51}, p_{52}, p_{53}, e_{a 0}, e_{a 1}, e_{a 2}, e_{a 3}, i_{o 0}, i_{o 1}, i_{o 2}, i_{o 3}\right\}
\end{gathered}
$$

The graphical observable Markov boundary contains 50 variables. Just like in $B\left(R_{0}^{3}\right)$, not all observable direct inputs of J-K flip-flop $f_{2}$ over the period are contained in $B\left(R_{0}^{4}\right)$. Only $j_{20}$ and $j_{21}$ at first two instants ( 0 and 1 ) are contained in $B\left(R_{0}^{4}\right)$. This is because the inputs to $f_{2}$ at instant 3 have not gone through $f_{2}$, and no effects could be observed. Although the inputs to $f_{2}$ at instant 2 have gone through $f_{2}$, the effects of $f_{2}$ 's outputs have not been observed at $e_{a}$ or $p_{5}$ before they go through another J-K flip-flop $f_{5}$ (i.e. any information resulted from inputs to $f_{2}$ at instant 2 are contained somewhere between the two J-K flip-flops, where no variables are observable). Also though $i_{n 0}, i_{n 1}$, and $i_{n 2}$ are contained in $B\left(R_{0}^{4}\right)$, but $i_{n 3}$ are not. This is because no effects of $i_{n 3}$ would be observed at $e_{a}$ or $p_{5}$ within the period.

After $B\left(R_{0}^{4}\right)$ are observed and agents communicate with each other, the inference indicates that $f_{2}$ could be faulty with a belief of $84.21 \%\left(f_{23}\right)$. All other devices in component $C_{2}$ are believed to be normal with beliefs over $94 \%$. All devices in components $C_{0}, C_{1}$ and $C_{3}$ are believed to be normal with beliefs over $96 \%$. All devices in component $C_{4}$ are believed to be normal with beliefs over $93.95 \%$. The inference results are significantly improved with one more instant modeled. This example also indicates that the potential improvement space will become less and less over more and more instants. This, from another perspective, shows a long history may not be so necessary in reasoning about the state of a dynamic domain.

### 6.5 Multiple Faults

To make the situation more complex, we next assume, besides J-K flip-flop $f_{2}$ in component $C_{2}$, J-K flip-flop $f_{4}$ in component $C_{0}$ is also abnormal. We randomly pick six consecutive instants as shown in Figure 13, where input signals, and those output signals that could be affected by the outputs of $f_{2}$ and $f_{4}$ are provided and presented as strings of six digits. The six instants will be divided into two consecutive periods each of which contains 4 instants. The two periods overlap over two instants. In Figure 13, the observable variables are underlined.

![img-12.jpeg](img-12.jpeg)

Fig. 13. The signal values of a sequential digital circuit over 6 instants.
The graphical observable Markov boundary $B\left(R_{1}^{4}\right)$ of $R_{1}=\left\{f_{40}, f_{41}, f_{42}, f_{43}\right\}$ is as shown as follows, and $B\left(R_{0}^{4}\right)$ is the same as given in Subsection 6.4. There are a total of 33 variables in $B\left(R_{1}^{4}\right)$.

$$
\begin{aligned}
B\left(R_{1}^{4}\right)=\{ & i_{i 0}, i_{i 1}, i_{i 2}, i_{i 3}, i_{j 0}, i_{j 1}, i_{j 2}, i_{j 3}, e_{80}, e_{81}, e_{82}, e_{83}, e_{70}, e_{71}, e_{72}, e_{73}, p_{40} \\
& \left.p_{41}, p_{42}, p_{43}, i_{20}, i_{21}, i_{22}, p_{40}, p_{41}, p_{42}, p_{43}, i_{30}, i_{31}, i_{32}, i_{40}, i_{41}, i_{42}\right\}
\end{aligned}
$$

Based on the observation of both $B\left(R_{0}^{4}\right)$ and $B\left(R_{1}^{4}\right)$ in the first period and communication among agents, the inference indicates that J-K flip-flop $f_{2}$ is believed to be faulty with a belief over $94.89 \%$. This belief is higher than the one obtained in Subsection 6.4. This is because stronger evidence, that indicates $f_{2}$ could be faulty, appears in $B\left(R_{0}^{4}\right)$ in this period (after observing $B\left(R_{0}^{4}\right),\left(R_{1}^{4}\right)$ is irrelevant to the state of $f_{2}$ ). The strength of the evidence we observe could be different from period to period for the same problem. When a system is monitored period by period, the system problems could be detected in different periods. Once a device is believed to be faulty in some period, the device should be fixed or replaced (though it may not be indicated to be faulty at some other periods).

In component $C_{2}$, all other devices are believed to be normal with beliefs over $96.06 \%$ except or gate $o_{6}$ with a belief over $94.30 \%$ in the first period.

The problem in J-K flip-flop $f_{4}$, however, is not properly detected in this period, which is believed to be abnormal with a belief of $16.21 \%$. All other devices in components $C_{0}$ are believed to be normal with beliefs over $96.06 \%$. All devices in component $C_{1}$ are believed to be normal with beliefs over $96.06 \%$ except inverter $n_{1}$ with a belief of $66.74 \%$, and gate $a_{n}$ with a belief of $45.79 \%$. That is, the system seems to attribute inconsistencies observed to $n_{1}$ and $a_{n}$ instead of $f_{4}$. Anyway, neither belief is high enough to conclude that either $n_{1}$ or $a_{n}$ or both are abnormal. All devices in component $C_{3}$ and $C_{4}$ are believed to be normal with beliefs over $96.06 \%$ except exclusive or gate $x_{0}$ with a belief of $93.48 \%$ and J-K flip-flop $f_{5}$ with a belief of $95.65 \%$.

Next, we continue to monitor the circuit over a new period of 4 instants, which has two instants overlapped with the previous one. The inference based on the observation of both $B\left(R_{0}^{4}\right)$ and $B\left(R_{1}^{4}\right)$ and communication among agents indicates that J-K flip-flop $f_{2}$ is believed to be faulty with a belief of $47.25 \%$. This is because that confusing evidence is observed in this period corresponding to the problem in $f_{2}$. Nevertheless, J-K flip-flop $f_{4}$ is believed to be faulty with a belief of $84.54 \%$. All other devices in component $C_{0}$ are believed to be normal with beliefs over $96.06 \%$ except and gate $a_{d}$ with a belief over $86.74 \%$. All devices in component $C_{1}$ are believed to be normal with beliefs over $95.64 \%$ except and gate $a_{2}$ with a belief of $86.71 \%$, inverter $n_{3} 91.69 \%$, and inverter $n_{1} 82.98 \%$. All other devices in component $C_{2}$ are believed to be normal with beliefs over $96.06 \%$ except or gate $o_{6}$ with a belief of $86.28 \%$. All devices in components $C_{3}$ are believed to be normal with beliefs over $95.99 \%$. All devices in components $C_{4}$ are believed to be normal with beliefs over $96.06 \%$ except exclusive or gate $x_{0} 85.00 \%$, and flip-flop $f_{5} 73.14 \%$. This time, we are confident that $f_{4}$ is faulty.

In the two consecutive periods, the posterior belief over the same entity may fluctuate significantly. For example, in the first period, $f_{2}$ is believed to be faulty with a belief over $94.89 \%$ and $f_{4} 16.21 \%$, and in the next period, $f_{2}$ is believed to be faulty with a belief of $47.25 \%$ and $f_{4} 84.54 \%$. The fluctuation is considered rational, which is caused by the variation in the strength of the evidence observed corresponding to the problems in the two devices in the two periods. In the first period, the observed evidence strongly indicates that $f_{2}$ is faulty and weakly indicates $f_{4}$ is faulty, and in the second period, the observed evidence strongly indicates that $f_{4}$ is faulty but weakly indicates that $f_{2}$ is faulty.

With dynamic systems being monitored period by period, the problems in the systems would be detected whenever proper evidence appears.

# 6.6 Complexity Growth 

In general, the longer the period of a dynamic domain we can model, the better the inference results we can reach would be. However, the period of a dynamic domain we can model into an MSBN should be limited by the computational complex-

ity. The computational complexity of inference using MSBNs is dominated by the largest clique size in the corresponding LJFs. In this subsection, we experimentally show the relationship between the computational complexity and the length of the modeled period of a dynamic domain.

The experiment is done on 3 different sequential digital circuits with different levels of complexity. Each circuit is divided into five components, and is modeled with a 5 agent MSBN over a range of periods. Depending on the circuit complexity, the period modeled could be up to 10 instant long. Beside the sequential digital circuit as shown in Figure 8, the other two sequential digital circuits are as shown in Figures 14 and 15, respectively.
![img-13.jpeg](img-13.jpeg)

Fig. 14. A simple sequential digital circuit of five components.
The circuit as shown in Figure 14 has the simplest topological structure. The interfaces between any two adjacent components are as shown in Table 1. When modeled into an MSBN, a new set of the corresponding interface variables will be added to the corresponding interfaces for each new instant added.

The sequential digital circuit as shown in Figure 15 has a more complex topological structure. The interfaces between any two components are as shown in Table 1. Compared to the two sequential digital circuits, the one as shown in Figure 8 has the most devices and signals.

![img-14.jpeg](img-14.jpeg)

Fig. 15. A more complex sequential digital circuit of five components.

Table 1
Interfaces of the circuits in Figure 14 and 15.


For the digital circuit as shown in Figure 8, we produce 4 MSBNs corresponding to the modeled periods from length 2 to length 5 . For the digital circuit as shown in Figure 14, we produce 9 MSBNs corresponding to the modeled periods from length 2 to length 10. For the digital circuit as shown in Figure 15, we produce 4 MSBNs corresponding to the modeled periods from length 2 to length 5 .

Since the computational complexity of the inference using MSBNs is dominated by the size of the largest cliques in the corresponding LJFs (linked junction forests), we show how the size of the largest cliques grows over the length of the represented period. Tables 2, 3 and 4 show the respective experimental results on different circuits.

Table 2
Maximum clique size vs the length of the modeled period for the circuit in Figure 8.


Table 3
Maximum clique size vs the length of the modeled period for the circuit in Figure 14.


Table 4
Maximum clique size vs the length of the modeled period for the circuit in Figure 15.


From the Tables 2, 3 and 4, the size of the largest cliques and the number of cliques in the corresponding linked junction forests grow linearly in the number of instants modeled. For example, in the column "Size of the largest clique" of Table 2, the difference between any two consecutive numbers are approximately the same (5). Note the size of the largest cliques is not only affected by the complexity and the size of the circuits, but is also affected by how you model the circuits (e.g. the choices of interface variables and the interface size, etc.).

# 7 Conclusion 

In dynamic multiagent domains, individual agents generally cannot evolve separately using DBNs because the temporal probabilistic messages from different subdomains are dependent of each other. This results in the decomposition issue and the distribution issue, which make it hard for the dynamic multiagent probabilistic inference to be performed both exactly and effectively. Nevertheless, in dynamic systems, the influence from the past could be weakened very quickly. We propose to represent and reason about the state of a dynamic multiagent domain period by period. By denser and relevant observation, the influence of the ignored history on the inference is reduced to a minimum. For relevant observation, we introduce graphical observable Markov boundary (GOMB) to capture all relevant observable variables. GOMB may also help us locate the relevant agents in the inference. For example, as shown in Subsection 6.4, the GOMB members in $B\left(R_{0}^{4}\right)$ (corresponding to flip-flop $f_{2}$ in the circuit as shown in Figure 8) only appear in subdomain $C_{2}, C_{3}$ and $C_{4}$. Hence, it is possible that, after proper initial processing, the 5 agent MSBN can be simplified to a 3 agent MSBN for cheaper inference.

Experiments show that the proposed method can successfully work on the simulated cases. The size of the largest cliques in the corresponding LJFs grows linearly in the length of the represented period. Hence, the period length affects the computational complexity in an exponential way. The length of the modeled period cannot be too long.

In the future, more experiments on more problem domains will be performed to further investigate the proposed approach.
