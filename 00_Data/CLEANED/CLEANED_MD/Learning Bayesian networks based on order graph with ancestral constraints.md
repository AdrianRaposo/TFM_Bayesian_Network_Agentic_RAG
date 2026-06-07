# Learning Bayesian Networks based on Order Graph with Ancestral Constraints 

Zidong Wang*, Xiaoguang Gao, Xiangyuan Tan<br>School of Electronics and Information, Northwestern Polytechnical University, Xi'an, China<br>Yu Yang<br>China Electronics Technology Group Corp 10th Research Institute, Chengdu, China<br>Daqing Chen<br>School of Engineering, London South Bank University, London, UK


#### Abstract

We consider incorporating ancestral constraints into structure learning for Bayesian Networks (BNs) when executing an exact search based on order graph; this is thought to be impossible because ancestral constraints are non-decomposable. In order to adapt to the constraints, the node in an Order Graph (OG) is generalized as a series of directed acyclic graphs (DAGs). Then, we design a novel revenue function to breed out infeasible and suboptimal nodes to expedite the graph search. A breadth-first search algorithm is implemented in the new search space, verifying the validity and efficiency of the proposed framework. It has been demonstrated that, when the ancestral constraints are consistent with the ground-truth network or deviate from it, the new framework can navigate a path that leads to a global optimization in almost all cases with less time and space required for orders of magnitude than the state-of-the-art framework, such as EC-Tree.


Keywords: Bayesian Network, Structure Learning, Ancestral Constraints

## 1. Introduction

As a type of graphic model, Bayesian Networks (BNs) are powerful tools for solving uncertainty in various applications, such as classification, causal discovery, and intelligent decision-making $[1,2,3,4]$. A BN is composed of a structure and parameters, where the structure is the basis of the model. It

[^0]
[^0]:    *Corresponding author
    Email addresses: nwpu_wzd@mail.nwpu.edu.cn (Zidong Wang), cxg2012@nwpu.edu.cn (Xiaoguang Gao), tanxy2017@mail.nwpu.edu.cn (Xiangyuan Tan), youngiv@126.com (Yu Yang), chend@lsbu.ac.uk (Daqing Chen)

is necessary to identify the structure of a BN to use it for modeling a system. However, it is tough to build a BN model purely based on the experience and domain knowledge of human-beings/experts; thus, the structure is typically modeled from training data[5].

In this paper, we consider the task of incorporating expert knowledge when learning the BN structure from the training data. The prior knowledge of an expert can be extracted and generalized as beliefs of a causal relationship among variables; hence the knowledge contains topological ordering constraints and structural constraints. In general, structure constraints fall into ancestral constraints and edge constraints according to whether they are decomposable [6]. Li proposed a constraint-based hill-climbing approach to incorporate all these constraints[6]. Cussens considered integer linear programming(ILP) as constrained optimization and treated all constraints as cutting planes [7]. Parviainen analyzed the existence of ancestor relations in the order space [8]. Chen claimed that the Markov equivalence is not satisfied because the corresponding sets of consistent directed acyclic graphs (DAGs) are overlapping [9]. Therefore, he proposed a new search space: the Bayesian network graph (BNG), a space of DAGs, for learning structures with non-decomposable scores [10]. To process ancestral constraints, Chen not only projected them using specific edge constraints but also implemented them through a tree of equivalent class(EC-Tree) [11, 12]. They demonstrated that ILP requires orders-of-magnitude computational time than their methods.

In this paper, we intend to fill in the research gap that utilizing ancestral constraints is infeasible in the decomposable implicit state-space search graphs, such as order graph(OG)[13]. As the K2 algorithm [14] and the approaches based on the OG (dynamic programming and heuristic search) cannot enforce ancestral constraints through pruning specific nodes, the global optimum solution theoretically only exists in a structural space, such as BNG and EC-Tree. Unfortunately, the extreme complexity of the frameworks mentioned above restricts the scalability of the algorithm (no more than 20 variables, as mentioned in the paper). Hence, it is necessary to study how to impose ancestral constraints into OG, a more inclusive and effective space when learning BN structure. It is easy to impose ordering constraints into OG [15]. However, incorporating structural constraints is tough since the order cannot convert to the parent or ancestor relations. Although some researchers have suggested utilizing edge constraints[16], ancestral constraints are still difficult to process using decomposable scores due to their non-decomposable nature. Furthermore, the exact search based on OG quickly gets stuck in a local optimum if ancestral constraints are incorporated as the technique in handling edge constraints. So we prepare to extend the scope of OG to tackle this challenge.

The contributions of the study are: 1) We propose and develop a new search space, named ancestral constrained order graph (ACOG). Such a framework combines the advantages of OG and BNG. When conducting a candidate node, all the suboptimal structures are reserved. When expanding a sink, only the structure with the best parents is encoded. 2) ACOG does not require to decompose ancestral constraints into edge constraints or any other constraints.

Furthermore, the only rule to follow is that a candidate node should conform to all the relevant constraints when adding a new sink. 3) We introduce the methods for eliminating violated and suboptimal nodes in ACOG when ancestral constraints are incorporated. The efficiency of the exact search can be highly improved, and the learned result can escape from the local optimum solution as much as possible based on pruned ACOG.

We empirically evaluate the effectiveness of the proposed framework through a breadth-first search strategy. Furthermore, when the ancestral constraints are consistent with the ground-truth network or deviate from it, the new framework can navigate a path that leads to a global optimization in almost all cases. Moreover, the proposed framework can effectively reduce the space and time complexity of learning BN structure with ancestral constraints. To verify the robustness of the proposed framework, we conduct a comparative test when there are minor errors and fatal errors in prior knowledge.

This paper is organized as follows: In Section 2, we review the relevant works on Bayesian Network structure learning and order graph. In Section 3, we propose the basic structure of the ACOG. In Section 4, we first discuss the relevant concepts of violated nodes and introduce the regulations for pruning them based on ancestral constraints. Then, we theoretically analyze how to discard the suboptimal DAGs by a novel revenue function based on ancestral constraints. We also introduce a practical example to illustrate it. In Section 5 , we present the experiments to evaluate the proposed algorithms. Section 6 concludes the paper.

# 2. Preliminaries 

Structure learning for Bayesian Networks has been proved to be NP-hard [17]; specifically, it has been formalized as a highly non-convex optimization problem in search space. There are two general approaches for learning BN structure: approximate methods[18, 19, 20, 21] and exact methods. In recent years, the exact approaches have attracted considerable research attention. An exact approach attempts to separate the learning process into two phases: parent set identification and structure optimization[22]. The first phase's purpose is to determine all the feasible candidate parent sets and their scores for each variable. Most of the structure optimization methods assign a parent set to each variable, maximizing the score of the observed structure while avoiding cycles. There are numerous efficient algorithms for the second phase, such as dynamic programming (DP) [23, 24], linear and integer programming (ILP) [25, 7], and shortest-path heuristic [26, 27].

### 2.1. Parent Set Identification

The structure $G$ of BN is a directly acyclic graph(DAG), which consists of random variables $\boldsymbol{V}=\left\{X_{1}, \cdots, X_{n}\right\}$ and arcs to their parent set. When learning the optimal BN structure from a dataset $\boldsymbol{D}$, the candidate parent sets for every variable and the corresponding score of them assess how well the model

fits the given data. As such, finding the best structure can be considered as a combinatorial optimization problem. The common criteria, such as BIC [28], $\mathrm{CH}[29]$ and BDeu [30] et. al, are all decomposable, meaning that the DAG score is the sum of its local scores for every variable.

$$
\operatorname{Score}(G \mid \boldsymbol{D})=\sum_{i=1}^{n} \operatorname{Score}\left(\left\langle X_{i}, P a\left(X_{i}\right)\right\rangle \mid \boldsymbol{D}\right)
$$

where $P a\left(X_{i}\right)$ represents a parent set of $X_{i}$. Usually, the score of the parent set is computed in sequential order, and the calculation complexity depends on the maximum in-degree, which is limited by the maximum size of parents.

In order to explain the underlying theory of the proposed approach more clearly, we adopt a specific mark of parent sets here. In a structure $G(\boldsymbol{V})$, where $\boldsymbol{V}$ is a set of variables in the graph, for any $X$ in $\boldsymbol{V}, P a(X \mid G)$ are the parents of $X$, and $D(X \mid G)$ are the descendants of $X$. The constraint sets are defined as follows.

Definition 1. (Edge constraints): $\mathcal{E}: \boldsymbol{V} \rightarrow P(\boldsymbol{V})$, where $P(\boldsymbol{V})$ is the power set of $\boldsymbol{V}$. For every $X \in \boldsymbol{V}, \mathcal{E}(X) \in P(\boldsymbol{V})$ is the required parent set of $X$, denoted as $\mathcal{E}(X) \rightarrow X$.

Definition 2. (Ancestral constraints): $\mathcal{A}: \boldsymbol{V} \rightarrow P(\boldsymbol{V})$, where $P(\boldsymbol{V})$ is the power set of $\boldsymbol{V}$. For every $X \in \boldsymbol{V}, \mathcal{A}(X) \in P(\boldsymbol{V})$ is the required ancestor set of $X$, denoted as $\mathcal{A}(X) \rightsquigarrow X . \mathcal{D}: \boldsymbol{V} \rightarrow P(\boldsymbol{V})$, where $P(\boldsymbol{V})$ is the power set of $\boldsymbol{V}$. For every $X \in \boldsymbol{V}, \mathcal{D}(X) \in P(\boldsymbol{V})$ is the required descendent set of $X$.

# 2.2. Structure Optimization 

For the sake of completeness, we briefly introduce OG and the exact search strategies below. OG is a Hasse diagram that contains all the subset of variables. The node in OG represents an ordering with the highest score, and the arc implies the lowest cost when adding a sink. Figure 1 shows an OG for the three variables.
![img-0.jpeg](img-0.jpeg)

Figure 1: OG for three variables.

In the step of the structure optimization, search strategies in OG, such as breadth-first search(DP) [23] and heuristic search(A*) [27], could find a global

optimum Bayesian Network easily. DP solves the structure learning problem by dividing it into sub-problems based on score decomposability. Let $\boldsymbol{U}$ be the domain variables. Assume that the variable $X$ is a sink in the optimal structure:

$$
\operatorname{Score}(\boldsymbol{U})=\max _{X \in \boldsymbol{U}}\{\operatorname{Score}(\boldsymbol{V} \backslash X)+\operatorname{BestScore}(X, \boldsymbol{U} \backslash X)\}
$$

where

$$
\operatorname{BestScore}(X, \boldsymbol{U} \backslash X)=\max _{P a(X) \subset \boldsymbol{U} \backslash X} \operatorname{Score}(X, P a(X))
$$

the remaining variables $\boldsymbol{U} \backslash X$ must form an optimal subnetwork, and $X$ can find its best parents set from $\boldsymbol{U} \backslash X$. Therefore, by comparing the cases in which every variable in $\boldsymbol{U}$ is a sink, the optimal structure can be obtained. With the guidance of the relation, the entire learning process can be divided into phases and starts with an empty network. In each phase, the algorithm adds a sink to every subnetwork obtained in the previous phase and generates more complex subnetworks. This process continues recursively until the complete network is observed.
$\mathrm{A}^{*}$ is a heuristic search strategy to find a shortest-path in OG. For every node $\boldsymbol{U}$ in a graph, evaluation function $\mathrm{f}(\boldsymbol{U})$ is applied to measure its quality, and node with lowest $\mathrm{f}(\boldsymbol{U})$ is expanded during the exploration of OG. So the entire search is guided towards the minimum $\mathrm{f}(\boldsymbol{U}) . \mathrm{f}(\boldsymbol{U})$ is defined as follows:

$$
\mathrm{f}(\boldsymbol{U})=\mathrm{g}(\boldsymbol{U})+\mathrm{h}(\boldsymbol{U})
$$

where $\mathrm{g}(\boldsymbol{U})$ is the past cost from the initial node to the current node, and $\mathrm{h}(\boldsymbol{U})$ is the estimate cost from the current node to the final node. In BN structure learning, the score of expanding a sink represent the path cost in each step. Thus, $\mathrm{g}(\boldsymbol{U})$ and $\mathrm{h}(\boldsymbol{U})$ can be fomulated as follows:

$$
\begin{gathered}
\mathrm{g}(\boldsymbol{U})=\mathrm{g}(\boldsymbol{U} \backslash X)+\operatorname{BestScore}(X, \boldsymbol{U} \backslash X) \\
\mathrm{h}(\boldsymbol{U})=\sum_{X \in \boldsymbol{V} \backslash \boldsymbol{U}} \operatorname{BestScore}(X, \boldsymbol{V} \backslash X)
\end{gathered}
$$

Because of the heuristic function's consistency, the search would converge to the global optimum solution with the minimum path cost. Furthermore, A* is proven to be a more efficient algorithm [27].

The rest of the paper focuses on resolving the problem of incorporating ancestral constraints into OG through exact search strategies.

# 3. Ancestral Constrained Order Graph 

Structure constraints are usually projected as edge constraints and ancestral constraints. The principle of incorporating edge constraints is as follows [16]. We assume that there is an edge constraint set $\mathcal{E}$. Then, two rules should be obeyed to check for the nodes in OG.

Table 1: Local scores of variables


Table 2: Order graph of variables


1. Let $\boldsymbol{U}$ be the set of variables at a node of the OG. If for some $X \in \boldsymbol{U}$, we have $\mathcal{E}(X) \not \subset \boldsymbol{U}$, then the node should be pruned.
2. When a variable $X$ is added to a node, the best parent set of $X$ should contain $\mathcal{E}(X)$.

These rules ensure that the constraints are consistent with nodes in OG; thus, the structure in the final layer maximizes the score. With the guidance of Rule 1, several violated nodes are discarded, and therefore the time and space cost is effectively reduced. For example, if the number of edge constraints is $m$, the space complexity can be reduced from $O\left(C_{n}^{\frac{1}{2}}\right)$ to $O\left(m C_{n-m}^{\frac{n}{2}-1}\right)$. Rule 2 restricts the candidate parent set, whose time complexity is $O(1)$. Therefore, OG can be efficiently simplified under edge constraints. However, the approach is not suitable for optimization with ancestral constraints. For example, Table 1 shows the variables with their local scores; assume that there is an ancestral constraint $X \rightsquigarrow Z$.

All the other scores that are not listed are -Inf. According to the above rules, Table 2 shows the process of searching the optimal structure. $Y \rightarrow X \rightarrow Z$ is the optimal structure under the constraints. However, there is another structure $X \rightarrow Y \rightarrow Z$, with a higher score of -22 that satisfies the constraints. The cause of the mistake is that the structure $X \rightarrow Y$ is discarded at node $\{X, Y\}$, which is permitted in the exact search. When incorporating ancestral constraints, it is essential to solving the conflict between decomposable scores and nondecomposable constraints [12]. Therefore, it is not appropriate to expand the subnetworks to a global optimum BN structure by adding sinks. The BNG and

EC-Tree [10, 12] can feasibly address this problem. However, the number of nodes in the frameworks mentioned above is vast, which could pose a restriction on the scalability when increasing the size of variables in the learning problem. Therefore, we introduce a new search graph called Ancestral constrained Order Graph (ACOG), that stores reasonable DAGs at its nodes. Figure 2 shows a simple ACOG with three variables.
![img-1.jpeg](img-1.jpeg)

Figure 2: ACOG for three variables
A node $\mathcal{G}(\boldsymbol{U})$ in the graph is formulated as

$$
\begin{aligned}
& \mathcal{G}(\boldsymbol{U})=\bigcup_{\forall X \in \boldsymbol{U} ; \boldsymbol{T}=\boldsymbol{U} \backslash X} \mathcal{G}(X \mid \boldsymbol{T}) \\
& \mathcal{G}(X \mid \boldsymbol{T})=\bigcup_{\forall G(\boldsymbol{T}) \in \mathcal{G}(\boldsymbol{T})} \operatorname{Best}(X, G(\boldsymbol{T})) \\
& \operatorname{Best}(X, G(\boldsymbol{T}))=G(\boldsymbol{T}) \bigcup G\left(X, \underset{P a(X) \subseteq \boldsymbol{T}}{\arg \max }(\operatorname{Score}(X, P a(X)))\right)
\end{aligned}
$$

$\operatorname{Best}(X, G)$ denotes the best structure based on $G$ with a sink $X . G(\boldsymbol{T})$ is a DAG of $\boldsymbol{T}$, and $G(X, P a(X))$ is a DAG for $X$ with the parent set $P a(X)$. Note that if a sink is a constrained descendant variable, the best parent set must conclude at least one of the specific ancestor and its descendants. Otherwise, the optimal parent set will be taken in the same way as OG. It is easy to conclude some features of ACOG:

1. The scope of ACOG is higher than OG. OG's node encodes the best DAG (or its equivalent structure) of the current variables, whereas ACOG's node encodes a series of DAGs that consist of all the subsets with a corresponding sink. ACOG reserves many partial suboptimal structures that potentially compose the final optimal DAG due to ancestral constraints. Thus, the proposed framework is more likely to lead to global optimization.
2. The scope of ACOG is lower than EC-Tree. When adding a sink to a DAG, only the best parent set is considered instead of all parent sets. Theoretically, the exact search is difficult to reach a global optimum solution based on ACOG because the framework is simplified. However, it is usually inconsiderable to reserve too many suboptimal parent sets, which cost massive

memory, especially when the ancestral constraints are consistent with the ground-truth network.

The nodes in the ACOG only store the best structures of the related nodes in the previous layer. However, it is still computationally inefficient and timeconsuming to search in the ACOG due in no small number of DAGs in the previous layer. In fact there are numerous violated and suboptimal structures in the ACOG with ancestral constraints. Moreover, we would discuss the condition in detail in the next section.

# 4. Simplifying the ACOG under ancestral constraints 

ACOG can be efficiently simplified under the ancestral constraints by discarding the violated and suboptimal structures. We detect the pruning rules next.

### 4.1. Pruning violated structures in $A C O G$

The purpose of introducing the ACOG is to incorporate ancestral constraints; thus, the necessary precondition for doing so is that DAGs at the nodes of the ACOG should be consistent with the constraints. Some nodes that violate the constraints need to be discarded. The definition of violation is as follows. Let $\mathcal{G}(\boldsymbol{U})$ be a node in an ACOG, and $\boldsymbol{U}$ be the set of domain variables in $\mathcal{G}(\boldsymbol{U})$.

Definition 3. (Violated node): If for every $X \in \boldsymbol{U}$, we have $\mathcal{A}(X) \subseteq \boldsymbol{U}$, then the node $\mathcal{G}(\boldsymbol{U})$ comforms to the constraints; otherwise $\mathcal{G}(\boldsymbol{U})$ is a violated node.

Definition 4. (Violated DAG): If in a DAG $G$, for every $X \in \boldsymbol{U}, \operatorname{Pa}(X \mid G)$ satisfies the conditions :
i) $\operatorname{Pa}(X \mid G) \subseteq \boldsymbol{U}$;
ii) for every $Y \in \mathcal{A}(X), \operatorname{Pa}(X \mid G) \bigcap D(Y \mid G) \neq \varnothing$;
then $G$ comform to the constraints; otherwise $G$ is a violated DAG.
Definitions 3 and 4 guide the pruning violated structures. If a node dissatisfies the ancestral constraints or contains violated partial DAGs, these structures should be pruned from ACOG. Although the candidate DAGs in ACOG are fewer than those in EC-Tree apparently, the size of nodes is still excessively large compared to that in OG. For example, if $\boldsymbol{U}=\left\{X_{1}, X_{2}, \cdots, X_{12}\right\}$ and $\mathcal{A}\left(X_{2}\right)=X_{1}$, there are several DAGs at initial layer nodes. However, the number of DAGs at node $\mathcal{G}\left(\boldsymbol{U} \backslash X_{1}\right)$ is enormous since it accumulates through all the structures from the entire ACOG except $\mathcal{G}(\boldsymbol{U})$. In order to resolve this issue, a novel method is proposed for pruning suboptimal structures in ACOG so that space complexity could be further reduced.

# 4.2. Pruning suboptimal structures in ACOG 

After the violated nodes and DAGs have been discarded, most of the DAGs at the remaining nodes are still suboptimal. When lacking the expert knowledge, the DAG with the highest score at each node should be reserved according to the principle of the exact strategies. All the DAGs at every node should be encoded in theory under ancestral constraints, but most suboptimal structures can still be pruned based on the following theorems. For consistency, let $\boldsymbol{U}$ denote the set of variables of $\mathcal{G}(\boldsymbol{U})$. In the following discussion, we assume that all the structures in ACOG conform to the constraints.

### 4.2.1. Principle for elimination

Consider a special condition:
Theorem 1. If for all $X \in \boldsymbol{U}, \mathcal{D}(X) \subseteq \boldsymbol{U}$ is true, then all the DAGs in $\mathcal{G}(\boldsymbol{U})$ can be pruned except those DAGs with the highest score.

Proof. Suppose that $\mathcal{G}\left(\boldsymbol{U}_{1}\right)$ satisfies the condition being a node in the ACOG, and $\mathcal{G}\left(\boldsymbol{U}_{2}\right)$ is a descendant of $\mathcal{G}\left(\boldsymbol{U}_{1}\right)$. Consider a sink variable $X$ is added to $\mathcal{G}\left(\boldsymbol{U}_{2}\right)$ : If $\mathcal{A}(X)=\varnothing$, for all $G \in \mathcal{G}\left(\boldsymbol{U}_{1}\right)$, the best parents of $X$ in $G$ are constant because the candidate parent set of $X$ is always $\boldsymbol{U}_{1} \cap \boldsymbol{U}_{2}$. If $\mathcal{A}(X) \neq \varnothing$, then $\mathcal{A}(X) \subset \boldsymbol{U}_{2} / \boldsymbol{U}_{1}$ holds. If the above conclusion is false, then $\mathcal{A}(X) \subset \boldsymbol{U}_{1}$ and $\mathcal{D}(\mathcal{A}(X)) \subseteq \boldsymbol{U}_{1}$; thus, we deduce $X \in \boldsymbol{U}_{1}$, which violates the assumption. Therefore, for all $G \in \mathcal{G}\left(\boldsymbol{U}_{1}\right)$, the best parents of $X$ in $G$ are constant because the required parents are from $\boldsymbol{U}_{2} \backslash \boldsymbol{U}_{1}$. The differences between DAGs in $\mathcal{G}\left(\boldsymbol{U}_{1}\right)$ are useless in choosing the optimal structures, and thus only DAGs with the highest score should be reserved.

Virtually, the property that ancestors with requires descendants are present in the same set is called 'all-satisfied' node. Such a node is tractable. However, most nodes of ACOG which waste too much vague memory are 'partiallysatisfied'. For a 'partially-satisfied' node $\mathcal{G}(\boldsymbol{U})$, it is necessary to construct the hypothetic 'all-satisfied' structure for pruning according to theorem1. We now introduce $I F(\boldsymbol{U})$, which is an unstable factor of node $\mathcal{G}(\boldsymbol{U})$ such that $I F(\boldsymbol{U})=\mathcal{D}(\boldsymbol{U}) \backslash(\mathcal{D}(\boldsymbol{U}) \cap \boldsymbol{U}) . I F(\boldsymbol{U})$ consider some required but absent descendants in advance. It is no longer suitable to reserve the DAG with the highest score in new structures obviously; thus, another problem is how to prune the useless DAGs at nodes. We now introduce a method of discarding suboptimal structures with invalid constraints.

Definition 5. (Invaild constraints): For $X \in I F(\boldsymbol{U})$ and all $Y \in \mathcal{A}(X) \cap \boldsymbol{U}$, the revenue function $\mathcal{F}_{G}(X, Y)$ for a certain $G$ of $\mathcal{G}(\boldsymbol{U})$ is defined as

$$
\begin{aligned}
\mathcal{F}_{G}(X, Y)= & \max _{P a_{1}, s, t, \forall \alpha \in P a_{1}, \alpha \in \phi_{1}(Y, G)} \operatorname{Score}\left(X, P a_{1}\right)- \\
& \max _{P a_{2}, s . t . \exists \alpha \in P a_{2}, \alpha \in \phi_{2}(Y, G)} \operatorname{Score}\left(X, P a_{2}\right) \\
& \phi_{1}(Y, G)=\boldsymbol{U} \backslash\{Y \cup D(Y \mid G)\} \\
& \phi_{2}(Y, G)=Y \cup D(Y \mid G)
\end{aligned}
$$

If $\mathcal{F}_{G}(X, Y)<0$, the constraint $Y \rightsquigarrow X$ is invalid in $G$. If $\mathcal{F}_{G}(X, Y) \geq 0$, the constraint is valid.

Definetion 5 provides a useful guidance to the pruning process of suboptimal structures. Using the revenue function $\mathcal{F}_{G}(X, Y)$, a set of certain rules is discussed below regarding the elimination of suboptimal structures in the ACOG.

Theorem 2. Assume that $G_{1}$ and $G_{2}$ are two DAGs in $\mathcal{G}(\boldsymbol{U})$ satisfying $\operatorname{Score}\left(G_{1}\right)>$ $\operatorname{Score}\left(G_{2}\right)$, and $\operatorname{IF}(\boldsymbol{U})=Y, \mathcal{A}(Y)=\{X\}$ is the single ancestral constraint in $\boldsymbol{U}$.
i). If the constraint $X \rightsquigarrow Y$ in $G_{1}$ and $G_{2}$ is invalid, the DAGs with the highest score should be retained.
ii). If the constraint $X \rightsquigarrow Y$ in $G_{1}$ and $G_{2}$ is valid and $D\left(X \mid G_{2}\right) \subseteq D\left(X \mid G_{1}\right)$, then $G_{2}$ can be pruned.

Proof. We construct a "all-satisfied" structure for $\mathcal{G}(\boldsymbol{U})$ and examine the value of $\mathcal{F}_{G}(X, Y)$.
ii). is obviously true. If $Y \in \boldsymbol{U}$, we only retain the best structure in $\mathcal{G}(\boldsymbol{U})$ according to Theorem 1. If $Y \notin \boldsymbol{U}$ and $D\left(X \mid G_{2}\right) \subseteq D\left(X \mid G_{1}\right)$, the candidate constraint parent variables for $X$ in $G_{1}$ are always more than those in $G_{2}$. If $\operatorname{Score}\left(G_{1}\right)>\operatorname{Score}\left(G_{2}\right)$, conclusion holds in all subsequent nodes with respect to $\boldsymbol{U}$ in the ACOG. The pruning rule is suitable for both $\mathcal{F}(X, Y, G)>0$ and $\mathcal{F}(X, Y, G)<0$.
i). is proved as follows. Generally, if the best parent set is $P \cup Q(P \notin U, Q \in$ $X \cup D(X \mid G))$. regardless of whether $P \in \mathcal{A}(Y)$, the discussion should be on node $\mathcal{G}(U \cup P)$. Therefore, we are only concerned with the case in which $Q$ is the best parent. We construct the "all-satisfied " $\mathcal{G}(\boldsymbol{U} \cup Y)$, where $Y$ is a sink. The best parent set of $Y$ must contain a variable $\alpha \in X \cup D\left(X \mid G_{i}\right)(i=1,2)$. When considering the revenue function, the formula (3) holds:

$$
\begin{aligned}
\max _{P \alpha \subset \boldsymbol{U}} \operatorname{Score}(Y, P a)= & \max \left(\max _{P a_{1}, s, t, \forall \alpha \in P a_{1}, \alpha \in \phi_{1}(X, G)} \operatorname{Score}\left(Y, P a_{1}\right)\right. \\
& \left.\max _{P a_{2}, s . t . \exists \alpha \in P a_{2}, \alpha \in \phi_{2}(X, G)} \operatorname{Score}\left(Y, P a_{2}\right)\right)
\end{aligned}
$$

If $\mathcal{F}_{G}(X, Y)<0$ in both $G_{1}$ and $G_{2}$, then:

$$
\begin{aligned}
\max _{P \alpha \subset \boldsymbol{U}} \operatorname{Score}(Y, P a) & =\max _{P a_{2}, s . t . \exists \alpha \in P a_{2}, \alpha \in \phi_{2}\left(X, G_{1}\right)} \operatorname{Score}\left(Y, P a_{2}\right) \\
& =\max _{P a_{2}, s . t . \exists \alpha \in P a_{2}, \alpha \in \phi_{2}\left(X, G_{2}\right)} \operatorname{Score}\left(Y, P a_{2}\right)
\end{aligned}
$$

For all the subsequent nodes $\mathcal{G}(\boldsymbol{U} \cup \boldsymbol{S})$ satisfying $Y \in \boldsymbol{S}$, the difference between arbitrary two DAGs $G_{1}(\boldsymbol{U} \cup \boldsymbol{S})$ and $G_{2}(\boldsymbol{U} \cup \boldsymbol{S})$ in $\mathcal{G}(\boldsymbol{U} \cup \boldsymbol{S})$ is is the best parent set restricted by the ancestral constraints of $Y$ in $G_{1}(\boldsymbol{U} \cup \boldsymbol{S}), G_{2}(\boldsymbol{U} \cup \boldsymbol{S})$. However, if $Q \in \boldsymbol{S}, Q$ is a constant and $\operatorname{Score}\left(G_{1}(\boldsymbol{U} \cup \boldsymbol{S})\right)>\operatorname{Score}\left(G_{2}(\boldsymbol{U} \cup S)\right)$. If $Q \in \boldsymbol{U}$, Eq. (4) suggests that $Q$ is still the same in the two new DAGs, and $\operatorname{Score}\left(G_{1}(\boldsymbol{U} \cup S)\right)>\operatorname{Score}\left(G_{2}(\boldsymbol{U} \cup \boldsymbol{S})\right)$ always holds true. Therefore, only $G_{1}$, whose score is the highest, should be retained. The correctness of conclusion on $\mathcal{G}(\boldsymbol{U} \cup P)$ can be proved similarly if the best parent set is $P \cup Q$.

We can demonstrate the pruning rules under invalid constraints by the example shown in Figure 3. Assume $\boldsymbol{U}=\{P, A, B, C\}, \boldsymbol{S}=\{D, E, F\}$ and ancestral
![img-2.jpeg](img-2.jpeg)

Figure 3: Example of $\mathcal{F}_{G}(X, Y)$
constraint $\mathcal{D}(B)=F . G_{1}$ and $G_{2}$ are DAGs in node $\mathcal{G}(\boldsymbol{U})$ with $\operatorname{Score}\left(G_{1}\right)>$ $\operatorname{Score}\left(G_{2}\right)$. If $\mathcal{F}_{G_{i}}(B, F)(i=1,2)$ is false, the best parent set of $F$ contains at least one of $\{B, C\}$ (here, we assume that $C$ is selected). As a descendant of $B$ in $G_{2}, A$ would not appear in the best parent set without $C$. Further we consider nodes $\mathcal{G}(\boldsymbol{U} \cup \boldsymbol{S})$, where $F$ is a sink. Without loss of generality, consider variables $D\left(B \mid G_{i}\right)(i=1,2)$ (such as $E)$, whereas others are $\boldsymbol{S} \backslash D\left(B \mid G_{i}\right)(i=1,2)$ (such as $D)$. If we add $F$ to the two new DAGs, the required parent could be $C$ or $E$ but can not be $A$. Therefore, the best parent sets for the two new structures are the same; this indicates that $G_{2}$, whose score is always lower than that of $G_{1}$, can be pruned, regardless of the added sink. Actually, if there exists a best path $A \rightarrow X \rightarrow F$, the optimal DAG that contains such a path is reserved in node $\boldsymbol{U}=\{P, A, B, X\}$. However, if $\mathcal{F}_{G_{i}}(B, F)(i=1,2)$ is true, $G_{2}$ cannot be pruned because $\operatorname{Score}\left(G_{1}\right)+\operatorname{Score}(F, C)<\operatorname{Score}\left(G_{2}\right)+\operatorname{Score}(F, A)$ may hold.

# 4.2.2. Algorithm for elimination 

Similarly, considering multiple ancestral constraints, we have the following conclusion: assume that $G_{1}$ and $G_{2}$ are two DAGs in $\mathcal{G}(\boldsymbol{U})$ with $\operatorname{Score}\left(G_{1}\right)>$ $\operatorname{Score}\left(G_{2}\right)$ and $|I F(\boldsymbol{U})|>1$. i) If for all $Y \in I F(\boldsymbol{U})$, the constraint $\mathcal{A}(Y) \rightsquigarrow Y$ is invalid in $G_{1}$ and $G_{2}$, then the DAGs with the highest score should be retained. ii) If for some $\boldsymbol{Q} \subseteq I F(\boldsymbol{U})$, for all $Y \in \boldsymbol{Q}$, the constraint $\mathcal{A}(Y) \rightsquigarrow Y$ is valid and $D\left(\mathcal{A}(Y) \mid G_{2}\right) \subseteq D\left(\mathcal{A}(Y) \mid G_{1}\right)$, then $G_{2}$ can be pruned. A summary is provided below on the general approach for pruning suboptimal DAGs of $\mathcal{G}(\boldsymbol{U})$ in ACOG: Firstly, we set a revenue list for all instable factors in $\mathcal{G}(\boldsymbol{U})$ as follows:


```
Algorithm 1 ACOG with Ancestral Constraints
    Initialize PreLayer \(\leftarrow \varnothing\).
    for Layer \(=1\) to \(n\) do
        for each node \(\mathcal{G}(U)\) in the PreLayer do
            for \(X \in \boldsymbol{V} \backslash \boldsymbol{U}\) and \(\boldsymbol{U} \cup X\) isn't violated do
                NowLayer \([U \cup X]\).visited \(=\) NowLayer \([U \cup X]\).visited \(\cup X\)
                for \(G(\boldsymbol{U}) \in \mathcal{G}(\boldsymbol{U})\) do
                    \(G(\boldsymbol{U} \cup X)=\operatorname{BestStructure}(G(\boldsymbol{U}), X, \mathcal{A}(X))\)
                    NowLayer \([U \cup X]\).str \(=\) NowLayer \([U \cup X] . s t r \cup G(\boldsymbol{U} \cup X)\)
            end for
            end for
    end for
    if NowLayer \([U \cup X]\).visited \(=U \cup X\) then
        if \(\boldsymbol{U} \cup X\) is all-satisfied then
            NowLayer \([U \cup X]\).str \(=\max (\) NowLayer \([U \cup X] . s t r)\)
        else
            \(M(\mathcal{G}(\boldsymbol{U} \cup X))=\operatorname{SetRevMat}(\) NowLayer \([U \cup X] . s t r, I F(\boldsymbol{U} \cup X))\)
            Group \(M(\mathcal{G}(\boldsymbol{U} \cup X))\) with same values of row into groups \((\boldsymbol{U} \cup X)\)
            NowLayer \([U \cup X] . s t r=\varnothing\)
            for Gro \(\in \operatorname{groups}(\boldsymbol{U} \cup X)\) do
                Gro \(=\) CutInvalid \((\) Gro)
                NowLayer \([U \cup X]\).str \(=\) NowLayer \([U \cup X] . s t r \cup\) Gro
            end for
            end if
    end if
    PreLayer \(\leftarrow\) NowLayer, NowLayer \(\leftarrow \varnothing\)
    end for
```

where 1 indicates $\mathcal{F}_{G}(\mathcal{A}(I F(\boldsymbol{U})), I F(\boldsymbol{U})) \geq 0$, whereas 0 implies $\mathcal{F}_{G}(\mathcal{A}(I F(\boldsymbol{U}))$ with $\left.I F(\boldsymbol{U})\right)<0$. Secondly, we divide the DAGs into different groups and ensure that the values of $\left.I F(\boldsymbol{U})_{i}(i=1: m)\right.$ are the same in each rows. Finally, we remove all suboptimal DAGs in every group and store the retained DAGs for the next stage.

The pseudocode of the entire pruning procedure for violated and suboptimal structures in ACOG is described as Algorithm 1.

So far, in the previous sections, we have discussed in detail our proposed approaches for pruning violated nodes and DAGs and suboptimal DAGs with the relevant principles and the proof. These approaches can prevent the computational time cost from increasing exponentially when the number of variables increases since many violated nodes can be removed. In the next section, some practical experiments are given to demonstrate the effectiveness of the benefits of the proposed approaches.

# 5. Experiments 

In this section, we first discuss the necessity of incorporating weak expert knowledge in a qualitative form; then evaluate the performance of the proposed framework under ancestral constraints in a quantitative form. As mentioned in Section 1, learning BN structure can be divided into two phases: Parent Identification and Structure Optimization. Either exact search strategies based on ACOG, OG, and EC-Tree or other approximate methods are all related to phase two. In phase one, the BIC scores have been pre-computed based on independence selection ordering without restriction on the in-degree of parent variables(BIC*)[31, 32]. For a small-scale network, parent sets are identified with a 1 s time limit, and 10 s on middle-scale networks ${ }^{1}$. For the sake of fairness, the computational cost of phase one is not considered in the comparison. ACOG is implemented in R language and run on an Intel Pentium G4560 CPU with a 12 GB memory limit. We apply memory-efficient dynamic programming (MEDP) [34] to search the exact solution based on proposed framework ${ }^{2}$.

The independent variables in the simulations included the number of variables ( n ), the number of observations from the ground-truth network ( m ), the constraint rate (p) and the error constraint rate (wp):

- $\boldsymbol{n}$ : We chose a random sub-network of a given size from four standard BN benchmarks: Insurance, Alarm, Hailfinder, and Hepar2 ${ }^{3}$.
- $\boldsymbol{m}$ :The training dataset was generated from the above sub-networks.
- $\boldsymbol{p}$ : The $\mathrm{p} \%$ of constraints that represent directed paths in the groundtruth network have been generalized and utilized in the BN structure learning. For each test instance, we used part of the constraints with a certain probability ranging from 0 to 1 . Notably, the number of paths presented in the network has limited the maximum size of constraints, and the negative constraints have not been taken into account.
- $\boldsymbol{w} \boldsymbol{p}$ : A percentage of fatal constraints: $\mathrm{wp} \%$ of constraints have declared that the path does not exist in the ground-truth network.

The comparison was based on the following criteria, and we chose the different criteria according to candidate algorithms and the propose of experiments.

- $t$ : Time recorded the running time of the algorithm.

[^0]
[^0]:    ${ }^{1}$ As literature[33], we judge the scale of networks according to the number of variables: a small network with $n<20$, a middle network with $20 \leq n<50$, and a large network with $n \geq 50$.
    ${ }^{2}$ Although A* search is known to be faster than DP, the reason DP is applied is that some nodes which are suboptimal without ancestral constraints but are part of the optimal graph with ancestral constraints in ACOG may not be traversed to based on A* search, while DP always takes all nodes into account.
    ${ }^{3}$ https://www.bnlearn.com/bnrepository/

- Score: Score estimated the accuracy of the learned network. When discussing the influence of the constraint rate, we used the score of learned structure based on EC-Tree as the benchmark and recorded the deviation rate in other algorithms. In addition to other situations, the actual score value was reserved.
- Nodes: The maximum number of nodes considered for a comparison between the exact graph search strategies. The fewer nodes to be expanded, the less the memory cost.
- Constraint Satisfaction Rate (CSR): It should note that the learned network based on exact methods always satisfied all the ancestral constraints, whereas approximate heuristic search ignored some constraints. So the constraint satisfaction rate, an index of required paths presented in observed DAG, should be considered besides.
- Structural Hamming Distance (SHD): SHD measured the distance between the learned structure and target structure. A higher SHD value indicated that the result deviated from the ground-truth network further.


# 5.1. Qualitative analysis of ACOG under ancestral constraints 

To qualitatively analyze the superiority of incorporating ancestral constraints, we have compared ACOG against other mainstream methods for BN structure learning without constraints, including constraint-based algorithm PC, scorebased algorithm HC, hybrid algorithm MMHC, and exact search algorithm based on OG. All of PC, HC, MMHC were approximate methods. The approximate algorithms have been implemented in R language (https://cran.rproject.org/web/packages/bnlearn/). SHD and Score were adopted as the criteria of accuracy. We simulated the subnetworks from three benchmark networks with $n \in[10,20]$ and $m \in\{1000,5000\}$. Figures 4 and 5 display the performance of the five algorithms considered.

In Figure 4, HC always resulted in a high SHD as a score-based algorithm is driven by some heuristic strategies focusing on the fitness of the edges and the training data. As a result, the judgment on the orientation of edges heavily depended on the dataset, which has caused a deviation from the target network. On the contrary, PC carried out conditional independent tests on the variables, then identified the v-structure and equivalent classes to learn an optimal BN structure. PC has focused on exploring the distribution of training data with respect to the causal relationships between the variables. Thus, the result learned by constrained-based algorithms got closer to the target network. Moreover, the performance of the hybrid algorithm MMHC was between HC and PC. The exact methods, OG and ACOG, can find a global optimum solution with a low SHD. Furthermore, ACOG projected the prior knowledge and attempted to make a trade-off between the training data and the real network structure. As a result, the learned network of ACOG was always the closest to the ground-truth network in almost all conditions. The comparison of SHD conformed to the conclusion that $H C>M M H C>P C \approx O G>A C O G$, and

![img-3.jpeg](img-3.jpeg)

Figure 4: SHD comparison with different algorithms
has demonstrated the efficiency and the necessity of enforcing the qualitative prior knowledge.

Figure 5 showed the scoring trends with the variation of the benchmark networks and the datasets, and we can find that the gap between different algorithms was insignificant. Especially in Hepar2, a sparse network, all the algorithms behaved almost the same regardless of the size of the datasets. OG always resulted in the highest score compared to the approximate approaches HC, MMHC, and PC. Incorporating ancestral constraints did not promote a structure with a higher score; On the contrary, the learned network obtained a worse evaluation in many conditions. It was hard to guarantee that the ground-truth network entirely could fall into the global optimum solution with the given training data, and a real path did not always acquire a high score, although the training data was generated from the standard network. Thus, the score generally decreased after incorporating ancestral constraints compared to the original exact algorithm. All the subfigures in Figure 5 also indicated that the score deviation was usually small when the ancestral constraints were sampled from the ground-truth network without wrong prior knowledge. In such a condition, ACOG performed better than the approximate methods such as MMHC and PC.

Additionally, figure 6 showed a comparison of the number of nodes for each

![img-4.jpeg](img-4.jpeg)

Figure 5: Score comparison with different algorithms
layer in ACOG and OG. The line in red in the figure $(p=0)$ indicated the scale of OG at different stages without ancestral constraints, and other lines gave the scale of ACOG with different numbers of constraints. It can be seen that the trend of the nodes in each layer was the same as the variation of the total expanded nodes, and ACOG with ancestral constraints always cost less memory than OG. This validated the necessity and efficiency of incorporating ancestral constraints.

# 5.2. Quantitative analysis of ACOG under ancestral constraints 

To evaluate the effectiveness of the proposed framework under ancestral constraints in a quantitative form, we compared it with EC-Tree[12], which was a state-of-the-art framework. Notably, the exact search strategies always reached the global optimum in EC-Tree despite imposing ancestral constraints. We also compared ACOG against an efficient constraint-based heuristic strategy (MINOBSx)[6]. MINOBSx, an approximate method, intended to find an optimal network under the conditions that satisfied the ancestral constraints as much as possible. The result on the same dataset was highly associated with

[^0]
[^0]:    ${ }^{4}$ https://github.com/acliuw/MINOBS-anc

![img-5.jpeg](img-5.jpeg)

Figure 6: Nodes in different layers of ACOG when incorporating ancestral constraints
the initial network in approximate search. Without loss of generality, the mean values of criteria in 10 experiments were adopted when executing MINOBSx.

# 5.2.1. Efficiency and Accuracy of ACOG 

We varied the number of variables $n \in\{10,12,14\}$ and the size of dataset $m \in\{1000,5000\}$ in the benchmark networks. Table 3 showed the comparison of the three small-scale networks with the constraints completely generalized from the ground-truth network.

The performance of ACOG and EC-Tree was compared. In terms of accuracy, the score gap between ACOG and EC-Tree was $0 \%$ in all the 24 cases, which indicated that ACOG always conducted an optimal global search. As for efficiency, the time consumption in $24 / 24^{5}$ results based on ACOG was lower than those based on EC-Tree. It has also been observed that: 1). The relationship between the constraint rate and time consumption. The cost of ACOG and EC-Tree both decreased with the increase of the constraint rate. 2). The relationship between the number of variables and time consumption. With the scale of the learning problem becoming large, the growth was more rapid in EC-Tree, whereas it was slow in ACOG. For example, if $\mathrm{m}=5000$ and $\mathrm{p}=$ 0.1 , the cost of EC-Tree was $1,75,227$ times of those of ACOG, respectively, when the number of variables was 10,12 , and 14 . In terms of memory consumption, the expanded nodes of EC-Tree were less than ACOG when the number of variables was small because A* search was implemented in EC-Tree, whereas MEDP in ACOG. However, the complexity of EC-Tree dramatically grew, even though the number of variables slightly increased. If $\mathrm{m}=1000$ and $\mathrm{p}=0.2$, the expanded nodes ratio was $0.27,0.9$ and 4.87 between EC-Tree and ACOG when $\mathrm{n}=10,12$ and 14 , respectively. The experiments asserted a higher efficiency of ACOG compared to EC-Tree without loss of accuracy when incorporating

[^0]
[^0]:    ${ }^{5} \mathrm{x} / \mathrm{x}$ in the whole section represents that the experiment sets satisfied the following conclusion / the total experiment sets.

Table 3: Results comparisons in three small-scale networks for different algorithms when wp $=0$


ancestral constraints.
Now consider the performance of ACOG and MINOBSx. It was easy to find that ACOG always consumed less time than MINOBSx in 22/24 simulation conditions. When imposing ancestral constraints, 14/24 results based on MINOBSx were deviated from the best solution and got stuck in local optimum. Furthermore, the maximum deviation rate was $6.67 \%$. More detailed comparisons have revealed: 1). The relationship between time consumption and the number of variables. When the learning problem was simple, traversing the whole search space was much easier than optimizing through a heuristic strategy. So the time consumption of ACOG was lower than MINOBSx when $\mathrm{n}=10$ and 12. Nevertheless, the growth of MINOBSx tended to be smoother, with the scale of the network becoming large. When the number of variables varied from 10 to 12 and 12 to 14 (assume that $\mathrm{m}=5000, \mathrm{p}=0.1$ ), the time consumption increased by two times and two times of MINOBSx, whereas two times and ten times of ACOG. Moreover, this trend was more apparent in medium-scale networks. 2). The relationship between the time consumption and constraint rate. Different from the trends of EC-Tree and ACOG, it was a more general case that the cost of MINOBSx did not increase even more constraints provided. Additionally,

MINOBSx can utilize most of the ancestral constraints: 17/24 results satisfied all constraints, and CSR in 23/24 results was no more than $3 \%$.

# 5.2.2. Robustness of ACOG 

We also empirically evaluated the robustness of ACOG when there were minor errors and fatal errors in ancestral constraints. Table 4 and Table 5 showed the performance of the three approaches when ancestral constraints violated the ground-truth network. Because of the inappropriate domain knowledge, there was no feasible solution in $7 / 24$ results when $\mathrm{wp}=0.2$ and $10 / 24$ results when $\mathrm{wp}=0.5$ based on EC-Tree and ACOG.

Table 4: Results comparisons in three small-scale networks for different algorithms when wp $=0.2$ ( $\backslash$ indicate that there is no feasible solution)


When the error rate was $20 \%$, ACOG still navigated a path leading to global optimum in 13/17 results. Furthermore, the maximum score deviation rate in the four negative examples was no more than $0.6 \%$, which was a tiny error. It can be interpreted as when constraints were consistent with the groundtruth network or slightly violated; there was a tiny difference between the best structure learned with and without constraints. If we expanded the search space, ACOG still can observe the optimal BN structure. The trends of time consumption in ACOG and EC-Tree were same as the condition when $\mathrm{wp}=$

Table 5: Results comparisons in three small-scale networks for different algorithms when wp $=0.5$ ( $\backslash$ indicate that there is no feasible solution)


0 , which has demonstrated that the total provided constraint, instead of the correct constraints, would affect efficiency.

Next, we compared ACOG with MINOBSx. In 15/17 conditions, ACOG produced a better solution, and the maximum score deviation rate of MINOBSx was $6.17 \%$, which was much more significant than $0.6 \%$ in ACOG. As observed, MINOBSx can always find a solution even there were mirror errors in prior knowledge. 9/17 results based on MINOBSx satisfied all the constraints, and the maximum deviation of CSR was no more than $10 \%$ in $6 / 8$ negative examples. It was interesting that when $n=10, m=1000$, and $p=0.5$, the structure learned by MINOBSx made higher quality than that observed by ECTree. Because MINOBSx ignored some ancestral constraints that indicated the incredibly wrong domain knowledge with a terrible score. However, EC-Tree and ACOG always satisfied all the constraints, which caused a worse result.

When the error rate was $50 \%$, the accuracy of ACOG and MINOBSx had relatively large fluctuations because of the more inappropriate ancestral constraints. In $6 / 14$ conditions, ACOG searched a global optimum solution, and the maximum score deviation rate was $3.22 \%$. MINOBSx only observed $1 / 14$ best structure with a maximum deviation rate up to $7.39 \%$. In the $13 / 14$ ex-

periment sets, ACOG performed better than MINOBSx in terms of time cost. It was worth mentioning that when wp increased, the CSR has dropped significantly. Especially the CSR in 13/24 results has reduced to below $90 \%$ if $w p=0.5$.

# 5.2.3. Scability of ACOG 

Table 6 showed the comparison in the medium-scale network where $n=$ $\{20,24\}$ and $m=\{1000,5000\}$. The memory of EC-Tree was overflowing because of the numerous expanded nodes. As such, the result of experiments based on EC-Tree was not available; we recorded the actual score of the learned structure instead of the deviation from the global optimum solution.

Table 6: Results comparisons in three small-scale networks for different algorithms when the data size is 5000 ( $\backslash$ indicate that there is no feasible solution)


The score of ACOG in 13/14 experiment sets was higher, and the only exception was because MINOBSx satisfied $75 \%$ of constraints. Similarly, there were some detailed comparisons: 1). The conclusion on the relationship between the constraint rate and time consumption in the small-scale network was still applicable in a medium-scale network. If $p<0.5$, ACOG spent more time than MINOBSx in $8 / 8$ conditions. And if $p \geq 0.5$, the time consumption of ACOG was less in all $6 / 6$ experiment sets. 2). Generally, with the increase of the size of variables, the growth of ACOG's time cost was still faster than that of MINOBSx's. So it was obvious MINOBSx can handle more complex problems that ACOG cannot.

We tested the scalability of ACOG in more complex conditions where some subnetworks with $n=\{30,32\}$ were generated from Hailfinder with the default

![img-6.jpeg](img-6.jpeg)

Figure 7: The comparison in Hailfinder_30
setting of the parameters as $m=15000, p=0.25$, and $w p=0$. Figures 7 and 8 showed a comparison between ACOG and MINOBSx when the number of variables increased. ACOG can incorporate ancestral constraints in a more reasonable way that the quality of the learned network was quite higher. The median score based on ACOG was about $1.11 \%$ and $0.71 \%$ higher than that based on MINOBSx, and the structure in ACOG was closer to the ground-truth network with an average Hamming distance below 20, whereas it was beyond 30 in MINOBSx. Moreover, ACOG's score gap between the maxima and the minima was $0.56 \%$ and $0.14 \%$, whereas it was $3.17 \%$ and $1.62 \%$ for MINOBSx in Hailfinder_30 and Hailfinder_32, and these results have demonstrated the stability of ACOG. Similarly, the hamming distance gap of ACOG had ten arcs and seven arcs less than those of MINOBSx. However, MINOBSx was orders-of-magnitude faster than ACOG, as the time complexity of exact methods was up to $O\left(2^{n}\right)$. ACOG spent about 6000s and 24000s in Halifinder_30 and Hailfinder_32, and MINOBSx can find the solution within 1000s. Note that the results of ACOG still satisfied all the ancestral constraints, while CRS of MINOBSx significantly fluctuated and depended on the quality of constraints.

In summary, when considering a BN model for tackling a complex problem in the real world, if the most crucial requirement for the model is to integrate all the prior expert knowledge, then only ACOG can be applied. If a modeler is

![img-7.jpeg](img-7.jpeg)

Figure 8: The comparison in Hailfinder_32
more concerned with the accuracy of the model, ACOG would be preferred to MINOBSx. If the BN structure should be modeled in a limited time, MINOBSx might be the right choice. ACOG cannot project expert knowledge in more complex networks when the number of variables is beyond 35 due to insufficient memory. In theory, the time cost was about 53 hours in such a condition.

Overall, the main advantage of MINOBSx was that it could solve the largescale problem, and the main advantage of EC-Tree was that it always can find the global optimum solution under the ancestral constraints. The proposed ACOG was a trade-off between accuracy and efficiency. As shown in the simulation results, the ACOG framework has always performed as good as EC-Tree when the ancestral constraints were generalized from the ground-truth network completely. Besides, even if there were some violated constraints, ACOG was still able to find a path leading to a global optimization in most cases. Furthermore, the time and space cost of ACOG's was lower than EC-Tree. However, ACOG still cannot be applied to large-scale networks with ancestral constraints, as almost all the other frameworks.

# 6. Conclusion 

We propose a new framework ACOG to learn optimal BN structure. ACOG extends the search scope of OG and can escape from local optimum when imposing ancestral constraints. ACOG prunes violated structures to reduce storage requirements. We have used a "full-satisfied" structure to facilitate the pruning process and employed a simple revenue function to discard suboptimal structures. The pruning rules have been proven in a solid and valid way. Experiments have demonstrated the ACOG can guide an optimal global search even there are some errors in prior knowledge with less time and space consumption compared to EC-Tree. Also, ACOG is more accurate and stable than MINOBSx when utilizing ancestral constraints in terms of the middle-scale networks.

As Yuan and Malone reported on the experimental results with up to 26 variables [27], learning optimal BN structure based on exact search frameworks cannot be applied to large-scale problems. Because many violated nodes are discarded when incorporating ancestral constraints, ACOG slightly enhances the scalability. However, the improvement is not enough to produce a significant qualitative change. When tackling some complex problems, the approximate method, such as MINOBSx, would be a more appropriate choice.

Our further works include studying how to incorporate negative ancestral constraints into order graph. Moreover, the properties of the positive revenue function should also be investigated.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (61573285).
