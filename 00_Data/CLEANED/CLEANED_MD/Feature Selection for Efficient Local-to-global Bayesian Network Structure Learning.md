# Feature Selection for Efficient Local-to-Global Bayesian Network Structure Learning 

KUI YU, ZHAOLONG LING, Hefei University of Technology, China<br>LIN LIU, University of South Australia, Australia<br>HAO WANG, Hefei University of Technology, China<br>JIUYONG LI, University of South Australia, Australia

Local-to-global learning approach plays an essential role in Bayesian network (BN) structure learning. Existing local-toglobal learning algorithms first construct the skeleton of a DAG (directed acyclic graph) by learning the MB (Markov blanket) or PC (parents and children) of each variable in a data set, then orient edges in the skeleton. However, existing MB or PC learning methods are often computationally expensive especially with a large-sized BN, resulting in inefficient local-to-global learning algorithms. To tackle the problem, in this paper, we develop an efficient local-to-global learning approach using feature selection. Specifically, we first analyze the rationale of the well-known Minimum-Redundancy and Maximum-Relevance (MRMR) feature selection approach for learning a PC set of a variable. Based on the analysis, we propose an efficient F2SL (feature selection-based structure learning) approach to local-to-global BN structure learning. The F2SL approach first employs the MRMR approach to learn a DAG skeleton, then orients edges in the skeleton. Employing independence tests or score functions for orienting edges, we instantiate the F2SL approach into two new algorithms, F2SL-c (using independence tests) and F2SL-s (using score functions). Compared to the state-of-the-art local-to-global BN learning algorithms, the experiments validated that the proposed algorithms in this paper are more efficient and provide competitive structure learning quality than the compared algorithms.

Additional Key Words and Phrases: Bayesian network, Feature selection, Local-to-global structure learning, Markov blanket

## ACM Reference Format:

Kui Yu, Zhaolong Ling, Lin Liu, Hao Wang, and Jiuyong Li. 2018. Feature Selection for Efficient Local-to-Global Bayesian Network Structure Learning. Proc. ACM Meas. Anal. Comput. Syst. 37, 4, Article 111 (August 2018), 26 pages. https://doi.org/10.1145/1122445.1122456

## 1 INTRODUCTION

Learning Bayesian network (BN) from observational data is an important problem in data mining, playing an essential part in inferring conditional independence and causal relations between variables [1]. BN learning has had many applications in various areas such as bioinformatics [11], neuroscience [3], and information retrieval $[10]$.

Authors' addresses: Kui Yu, Zhaolong Ling, yukui@hfut.edu.cn, z_dragonl@163.com, School of Computer Science and Information Engineering, Hefei University of Technology, 485 Daxia Road, Shushan District, Hefei, 230601, China; Lin Liu, Lin.Liu@unisa.edu.au, UniSA STEM, University of South Australia, Mawson Lakes Blvd, Mawson Lakes, Adelaide, 5095, SA, Australia; Hao Wang, jsjxwangh@hfut.edu.cn, School of Computer Science and Information Engineering, Hefei University of Technology, 485 Daxia Road, Shushan District, Hefei, 230601, China; Jiuyong Li, Jiuyong.Li@unisa.edu.au, UniSA STEM, University of South Australia, Mawson Lakes Blvd, Mawson Lakes, Adelaide, 5095, SA, Australia.

[^0]
[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    (c) 2018 Association for Computing Machinery.
    2476-1249/2018/8-ART111 $\$ 15.00$
    https://doi.org/10.1145/1122445.1122456

![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of a MB in a lung-cancer Bayesian network

The structure of a BN is represented by a DAG (directed acyclic graph) where nodes of the DAG represent the variables and edges represent dependence between variables. When there is an edge $X \rightarrow Y, X$ is known as a parent of $Y$ and $Y$ is a child of $X$. In general, learning a DAG over a large number of variables is computationally intractable [7, 31]. To alleviate the computational complexity, the local-to-global approach was proposed to reduce the DAG search space [12, 24, 37]. Instead of searching the entire DAG space over all the variables simultaneously, the local-to-global approach first finds the Markov blanket (MB) or parents and children (PC) of each variable (without distinguishing parents from children), then uses the learnt MB (or PC) set of each variable to construct the DAG skeleton, and finally orients edges in the skeleton. An MB of a node in a BN consists of the parents, children, and spouses (i.e. other parents of the node's children) of the node in a BN. Figure 1 gives an example of a MB in the BN of lung cancer [16]. The MB of Lung cancer consists of Smoking and Gentics (parents), Coughing and Fatigue (children), and Allergy (spouse).

The current MB learning methods are mainly categorized into two types: simultaneous MB learning and divide-and conquer MB learning. However, these methods are either inefficient or ineffective. Given a variable of interest, simultaneous MB learning algorithms learn the MB of the variable simultaneously without distinguishing PC from spouses and are not capable of constructing high quality DAG skeletons especially when a data set has a small number of data samples with high-dimensionality, but they are computationally efficient. Divide-and conquer methods first employ a Parent-Child (PC) learning algorithm to learn the PC set of the variable, then find the spouses of the variable. They are effective for DAG skeleton construction, but they are not computationally efficient when the size of PC is large. This implies that existing local-to-global BN structure learning algorithms are either inefficient or ineffective depending on which type of MB or PC learning methods are used.

Feature selection aims to select a subset of features with regard to a class variable of interest from the original set of features, and it is an essential preprocessing step for model building or data understanding in data analytics [4]. Existing feature selection methods can be broadly categorized into filtering, wrapper, and embedded methods [21, 38]. Filter methods are classifier independent, and the other two types of methods are classifier dependent.

Filtering feature selection methods have been attracting major attention, due to their fast processing speed and independence of prediction models. Studies have shown that under certain assumptions, the MB of a class variable is the optimal feature set for supervised machine learning tasks, while existing filtering feature selection methods attempt to find an approximate MB (e.g. PC) of a class variable [34]. A question is whether we can make use of efficient filtering feature selection methods to learn the MB/PC set of each variable in a dataset to significantly improve computational efficiency of BN structure learning. To investigate this question, in this paper, we first establish the theoretical link of filtering feature selection methods with local BN structure learning

(i.e., MB/PC learning) and then propose an efficient F2SL (Feature Selection-based Structure Learning) approach to speeding up local-to-global BN structure learning. Our contributions can be summarized as follows.

- We employ a well-known mutual information-based feature selection approach, called Min-Redundancy and Maximum-Relevance (MRMR) [4], to find parents and children for speeding up structure learning. To answer why the MRMR approach is able to learn the PC of a variable of interest, we first analyze the relationship of the objective function of MRMR and MB learning. Then we analyze the output of MRMR related to the MB. And finally we discuss the instantiation of MRMR for PC learning.
- Based on the analysis above, we propose the F2SL approach to local-to-global BN structure learning. F2SL employs the MRMR approach to learn the PC of each variable in a data set, then constructs the DAG skeleton, and finally it orients edges in the skeleton. Using independence tests or score functions for orienting edges, F2SL is instantiated to two algorithms, F2SL-c (using independence tests) and F2SL-s (using score functions).
- We conduct extensive experiments to validate F2SL-c and F2SL-s against the five representative local-toglobal BN learning algorithms. The experiments results show that the proposed algorithms are significantly faster and also achieve better structure learning quality than the five rivals.
The paper is organized as follows. Section 2 reviews the related work, and Section 3 gives notations and definitions. Section 4 presents an analysis in theory, while Section 5 proposes the new algorithms. Section 6 describes and discusses the experiments and Section 7 concludes the paper.


# 2 RELATED WORK 

In the past decades, learning BN structures has been an important task in data mining and machine learning [17, 20]. There are two main types of structure learning methods: score-based and constraint-based methods [15, 43]. Score-based algorithms use a scoring function to perform a global structure learning over a search space of possible DAGs over all the variables in a data set [6, 9]. Constraint-based methods employ independence tests to first estimate whether there is an edge between two variables and then orient edge directions [5, 8]. Existing BN learning approaches formulated the BN structure learning problem as a traditional combinatorial optimization problem and depend on various local heuristics for enforcing the acyclicity constraint.

To avoid the combinatorial constraint, Zheng et al. [45] have formulated the BN structure learning problem as a continuous optimization problem instead of the traditional combinatorial optimization problem. Some recent studies have leveraged the idea in [45] to learn BN structures using deep neutral networks. Yu et al. [41] have designed a BN structure learning algorithm using graph neural networks and Zhang et al. [44] have proposed a variational autoencoder-based method for learning BN structures.

Since the search space of DAGs is combinatorial and exponential with the number of variables, existing global BN structure learning methods are often computationally infeasible when the number of variables is large. Then to improve efficiency of BN structure learning, local-to-global BN structure learning methods were proposed which contain two steps: skeleton learning and edge orientation. In the skeleton learning step, the local-to-global approach first learns the MB or PC of each variable in a dataset independently, then constructs the DAG skeleton (i.e. the undirected graph) using the learnt MB or PC sets. Through learning each variable's MB or PC locally, the local-to-global approach significantly reduces the potential DAG search space, and thus can be scalable to thousands of variables. In the edge orientation step, edges are oriented in the skeleton using independence tests or score functions.

How to efficiently learn the MB or PC of a variable for skeleton learning is the key to existing local-to-global BN learning algorithms. To learn skeletons, many MB and PC learning algorithm have been proposed and they fall in two types: constraint-based methods and score-based approaches. Constraint-based MB learning algorithms employ independence tests and are mainly divided into two types: simultaneous learning approach and

divide-and conquer approach. The representative algorithms of the former type include GSMB [24], IAMB [36], and Inter-IAMB [36], while the representative algorithms of the latter type are HITON-MB [1, 2], MMMB [35], PCMB [29], STMB [13], and BAMB [23]. PC-simple [22], MMPC [35] and HITON-PC [2] are the three widely used algorithms for learning PC of a variable using independence tests. Score-based MB (or PC) learning methods use a score function to learn MB or PC, and mainly includes the SLL (Score-based Local Learning) [26] and $S^{2}$ TMB (Score-based Simultaneous MB) algorithms [14].

Based on these MB or PC learning algorithms, several local-to-global structure learning methods were proposed. The GSBN [24] algorithm employs the GSMB algorithm for learning skeleton and orients edge using independence tests. SLL+C [26] uses the SLL algorithm to learn the MB of each variable and employs independence tests for orienting edges while SLL+G [26] uses score-based methods for edge orientations. MMHC [37] uses MMPC for learning skeletons and employs a score function and hill-climbing search strategy for orienting edges. Thus both SLL+C and MMHC belong to a hybrid local-to-global approach. Gao et al. [12] recently proposed a novel GGSL (Graph Growing Structure Learning) algorithm for local-to-global structure learning. Instead of finding the MB of each variable in advance, GGSL first randomly selects a variable and learns the local structure around the variable using the $S^{2} T M B$ algorithm, then iteratively applies the local learning procedure to the variable's neighbors for gradually expanding the learned local BN structure until a global BN structure is achieved.

Existing MB or PC learning algorithms have the following main drawbacks. GSMB and IAMB are efficient, but the number of samples required by them grows exponentially with the size of the MB of the target variable, since they use the entire set of variables selected currently as conditioning sets for independence tests. HITONMB, MMMB, PCMB, STMB, and BAMB mitigate the problem of the large sample requirement by performing an exhaustive subset search within the variables selected currently, but the search is computationally expensive when the size of the currently selected variables becomes large. The computational cost of SLL and $S^{2}$ TMB is determined by BN structure learning algorithms, since at each iteration SLL and $S^{2}$ TMB need to use a BN structure learning algorithm to learn a local BN structure (involving all variables selected currently) around a variable. Due to the computational complexity of existing BN structure learning algorithms, they face the scalability issues when the size of the local BN structure becomes large. To improve the MB learning efficiency, Pellet et al. [28] proposed the TC (Total Conditioning) algorithm for learning BN structures from Gaussian data. The TC algorithm employs a regression-based feature-selection method to learn DAG skeletons and then uses independence tests to orient edges.

In the past decade, researchers have proposed many methods for distinguishing causes from effects purely from observational data in the two-variable case [42]. These methods are mainly divided into two types: methods based on additive noise models [18,32] and methods based on information geometric causal inference [19]. The focus of this paper is on learning a complete BN structure containing all variables in a problem of interest. For readers who are interested in the research on distinguishing causes from effects in the two-variable case, more references can be found in the recent survey proposed by Mooij et al [25].

In this paper, we focus on address the computational problem of existing MB or PC learning algorithms and focus on learning BN structures from discrete data with multivariate random variables.

# 3 NOTATIONS AND DEFINITIONS 

### 3.1 Bayesian network and Markov blanket

In this section, we will introduce some basic definitions. Let $P$ be the joint probability distribution represented by a DAG $G$ over a set of random variables $V=\left\{V_{1}, \cdots, V_{M}\right\}$. We use $V_{i} \Perp V_{j} \mid S$ to denote that $V_{i}$ and $V_{j}$ are conditionally independent given $S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$, and $V_{i} \Perp V_{j} \mid S$ to represent that $V_{i}$ and $V_{j}$ are conditionally dependent given $S$. The definition of conditional independence (and dependence) is given as follows.

Definition 1 (Conditional independence). Given two distinct variables $V_{i}, V_{j} \in V$ are said to be conditionally independent given a subset of variables $S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$ (i.e., $V_{i} \Perp V_{j} \mid S$ ), if and only if $P\left(V_{i}, V_{j} \mid S\right)=P\left(V_{i} \mid S\right) P\left(V_{j} \mid S\right)$. Otherwise, $V_{i}$ and $V_{j}$ are conditionally dependent given $S$, i.e., $V_{i} \Perp V_{j} \mid S$.

The symbols $p a\left(V_{i}\right), c h\left(V_{i}\right)$, and $s p\left(V_{i}\right)$ denote the sets of parents, children, and spouses of $V_{i}$, respectively. We call the triplet $\langle V, G, P\rangle$ a Bayesian network $\langle B N\rangle$ if $\langle V, G, P\rangle$ satisfies the Markov condition: every variable is independent of any subset of its non-descendant variables given its parents in $G$ [27]. In a BN $\langle V, G, P\rangle$, by the Markov condition, the joint probability $P$ can be decomposed into the product of conditional probabilities as

$$
P\left(V_{1}, V_{2}, \cdots, V_{M}\right)=\prod_{i=1}^{M} P\left(V_{i} \mid p a\left(V_{i}\right)\right)
$$

Definition 2 (D-SEPARATION [27]). In a DAGG, a path $\pi$ is said to be d-separated (or blocked) by a set of vertices $S \subset V$ if and only if (1) $\pi$ contains a chain $V_{i} \rightarrow V_{k} \rightarrow V_{j}$ or a fork $V_{i} \leftarrow V_{k} \leftarrow V_{j}$ such that the middle vertex $V_{k}$ is in $S$, or (2) $\pi$ contains an inverted fork (or collider) $V_{i} \rightarrow V_{k} \leftarrow V_{j}$ such that the middle vertex $V_{k}$ is not in $S$ and such that no descendant of $V_{k}$ is in $S$.

A set $S$ is said to d-separate $V_{i}$ from $V_{j}$ if and only if $S$ blocks every path from a vertex in $V_{i}$ to a vertex in $V_{j}$.
Definition 3 (Faithfulness). [33] Given a $B N\langle V, G, P\rangle, P$ is faithful to $G$ if $\forall V_{i}, V_{j} \in V, \exists S \subseteq V \backslash\left\{V_{i}, V_{j}\right\}$ $d$-separates $V_{i}$ and $V_{j}$ in $G$ if $V_{i} \Perp V_{j} \mid S$ holds in $P$.

The faithfulness assumption establishes a relation between a probability distribution $P$ and its underlying DAG $G$. In a BN, the faithfulness assumption implies that two variables $V_{i}, V_{j} \in V$ that are d-separated with each other by a subset $S \subseteq F \backslash\left\{F_{i}, F_{j}\right\}$ in $G$ are conditionally independent conditioning on $S$ in $P$. Under the assumption, we can use conditional independence tests, instead of d-separation, to find all dependencies or independencies entailed with a Bayesian network.

Definition 4 (MARKOV BLANKET). [27] Under the faithfulness assumption, the MB of a variable $V_{i}$ in $G$, noted as $M B\left(V_{i}\right)$, is unique and consists of parents, children and spouses of $V_{i}$.

In the following, Lemma 1 states the dependencies between a variable and its parents (or children). Lemma 2 denotes the independence/dependence relations of a variable and its spouses.

Lemma 1. [33] Under the faithfulness assumption, for $V_{j} \in V$ and $V_{i} \in V$, there is an edge between $V_{j}$ and $V_{i}$ if and only if $V_{j} \Perp V_{i} \mid S$, for all $S \subseteq V \backslash\left\{V_{j}, V_{i}\right\}$.

Lemma 1 indicates that if $V_{j}$ is a parent or a child of $V_{i}, V_{j}$ and $V_{i}$ are conditionally dependent given any subset $S$ of $V \backslash\left\{X, V_{i}\right\}$.

Lemma 2. [33] In a Bayesian network, assuming that $V_{i}$ is adjacent to $V_{k}, V_{j}$ is adjacent to $V_{k}$, and $V_{i}$ is not adjacent to $V_{j}$ (e.g. $V_{i} \rightarrow V_{k} \leftarrow V_{j}$ ), if $\forall S \subseteq V \backslash\left\{V_{i}, V_{k}, V_{j}\right\}, V_{i} \Perp V_{j} \mid S$ and $V_{i} \Perp V_{j} \mid S \cup\left\{V_{k}\right\}$ hold, then $V_{j}$ is a spouse of $V_{i}$.

Lemma 2 states that if $V_{j}$ is a spouse of $V_{i}, V_{j}$ and $V_{i}$ are independent conditioning on a subset $S$ excluding their common child, but they are dependent conditioning on $S$ including their common child.

# 3.2 Mutual information and conditional independence 

Given variable $X$, the entropy of $X$ is defined as

$$
H(X)=-\Sigma_{x} P(x) \log P(x)
$$

The entropy of $X$ after observing values of another variable $Y$ is defined as

$$
H(X \mid Y)=-\Sigma_{y} P(y) \Sigma_{x} P(x \mid y) \log P(x \mid y)
$$

In Eq.(2) and Eq.(3), $P(x)$ is the prior probability of $X=x$ (i.e. the value $x$ that $X$ takes), and $P(x \mid y)$ is the posterior probability of $X=x$ given $Y=y$. In order to calculate Eq.(2) we need the estimated distributions $P(x)$ and $P(x \mid y)$. For a discrete dataset with $N$ independently and identically distributed samples, we estimate the probability of $P(X=x)$ using maximum likelihood, i.e. the frequency of $X=x$ occurring in the dataset divided by the total number of data samples (i.e. $N$ ) of the dataset. The posterior probability $P(x \mid y)$ is calculated by the frequency of $X=x$ occurring given that $Y=y$ holds in the dataset divided by the total number of data samples $N$.

According to Eq.(2) and Eq.(3), the mutual information between $X$ and $Y$, denoted as $I(X, Y)$, is defined as

$$
\begin{aligned}
I(X ; Y) & =H(X)-H(X \mid Y) \\
& =\Sigma_{x, y} P(x, y) \log \frac{P(x, y)}{P(x) P(y)}
\end{aligned}
$$

From Eq. (4), the conditional mutual information between $X$ and $Y$ given another variable $Z$ is defined as:

$$
\begin{aligned}
I(X ; Y \mid Z) & =H(X \mid Z)-H(X \mid Y Z) \\
& =\Sigma_{z \in Z} P(z) \Sigma_{x \in X, y \in Y} P(x, y \mid z) \log \frac{P(x, y \mid z)}{P(x \mid z) P(y \mid z)}
\end{aligned}
$$

In Eq.(4) and Eq.(5), $\mathrm{i} I(X ; Y)=0$ if $X$ and $Y$ is independent (i.e., $P(X, Y)=P(X) P(Y)), I(X ; Y)=0$ and $I(X ; Y \mid Z)=0$ if $X$ and $Y$ is conditionally independent given $Z$.

# 4 MRMR FEATURE SELECTION \& MB LEARNING 

Given a data set $D$ consisting of a variable set $V$ and the class attribute $C \in V$, in this section, we will analyze the output of the MRMR feature selection approach with relation to the MB of $C$.

### 4.1 Objective functions of MRMR and MB learning

Objective function of MB learning. Under the faithfulness assumption, $M B(C)$ is the optimal feature set for the classification problem with $C$ as the class variable, and $M B(C)$ satisfies the following property [39].

Theorem 1. $\forall S \subset V \backslash C, I(C ; M B(C)) \geq I(C ; S)$.
In Theorem 1, except for $S=M B(C)$, if $S$ is a superset of $M B(C), I(C ; M B(C))=I(C ; S)$ also holds. In [39], the authors do not consider this case. This case means that although by the property of the $\mathrm{MB}, C$ is conditionally independent of the remaining variables $S$ conditioning on $M B(C)$ (i.e., $\forall S \subseteq F \backslash M B(C), P(C \mid S, M B(C))=$ $P(C \mid M B(C)) ; C$ and $S$ also conditionally independent conditioning on a superset of $M B(C)$, i.e., $\forall S, S^{\prime} \subset F \backslash$ $M B(C), P\left(C \mid S, M B(C) \cup S^{\prime}\right)=P(C \mid M B(C) \cup S^{\prime})$. Then Theorem 1 indicates that learning $M B(C)$ is equivalent to finding a subset $S \subseteq V \backslash C$ that maximizes $I(S ; C)$ and $M B(C)$ is the minimal and optimal set of $S$, since adding features to the $M B(C)$ set does not increase the mutual information to $C$. Although the issue of the superset exists in Theorem 1, it does not put any impact on existing algorithms for learning $M B(C)$ or $P C(C)$. Since the MB property $\forall S \subseteq F \backslash M B(C), P(C \mid S, M B(C))=P(C \mid M B(C)))$ holds, these algorithms can use this property to remove redundant features in the learnt MB and are able to identify the minimal MB of $C$ (i.e., parents, children, and spouses of $C$ ). In addition, if we assume that all conditional independence tests are reliable and the faithfulness assumption holds, existing MB learning algorithms achieve a correct MB of a target variable in theory.

However, in Theorem 1, it is a challenging combinatorial optimization problem for identifying $M B(C)$ from $F$. Therefore, almost all MB learning methods have adopted a greedy strategy by considering features one by one to find $S^{*}$. Specifically, at each iteration, given the currently selected set of features, $S$, they choose the feature $X$ in $V \backslash(S \cup\{C\})$ that maximizes $I((S \cup\{X\}) ; C)$. Since $I((S \cup X) ; C)=I(S ; C)+I(X ; C \mid S)$ holds and at each iteration $I(S ; C)$ is the same for each variable $X$, this greedy strategy can be formulated as Eq.(6) as follows.

$$
X^{*}=\underset{X \in V \backslash\left(S \cup\{C\}\right)}{\arg \max } I(X ; C \mid S)
$$

To solve Eq.(6), there are two types of MB learning methods. One is to calculate $I(X ; C \mid S)$ in Eq.(6) using the entire set $S$ of features currently selected, i.e., all the features in $S$, such as GSMB [24] and IAMB [36], while the other is to calculate $I(X ; C \mid S)$ using all possible subsets of $S$, such as HITON-MB [2] and MMMB [35]. When the size of $S$ increases, it will be impractical for the first type of methods to compute $I(X ; C \mid S)$ because the computation demands a large number of training samples while it will be computationally intractable for the second type of methods since the number of subsets of $S$ will be exponential to the number of features in $S$.

Objective function of MRMR. To tackle these problems, since $I(X ; S ; C)=I(X ; S)-I(X ; S \mid C)=I(X ; C)-$ $I(X ; C \mid S)$ holds, MRMR decomposes Eq.(6) into Eq.(7) as follows.

$$
X^{*}=\underset{X \in V \backslash S}{\arg \max }\{I(X ; C)-I(X ; S)+I(X ; S \mid C)\}
$$

In Eq.(7), $I(X ; C)$ represents the relevancy of $X$ to $C, I(X ; S)$ denotes the redundancy of $X$ with respect to $S$, and $I(X ; S \mid C)$ indicates the class-conditional relevance, which considers the situation where a feature $X$ provides more predictive information by jointly with other features (i.e., those in $S$ ) than by itself with respect to $C$.

When the size of $S$ becomes large, if we direct compute $I(X ; S)$ and $I(X ; S \mid C)$ in Eq.(7), on the one hand, it will result in computationally expensive; on the other hand, the big size of $S$ will lead to the large sample requirement to guarantee the reliable results of computing $I(X ; S)$ and $I(X ; S \mid C)$.

To reduce high-order mutual information computations to low-order mutual information calculations, we require highly restrictive assumptions made on the dependence/independence between features. To deal with the class-conditional relevance term $I(X ; S \mid C)$, Assumption 1 is the assumption by a naive Bayes classifier and it assumes that the features in $V \backslash C$ are pairwise independent conditioning on $C$. By Assumption 1, we get $I(X ; S \mid C)=0$ and the term $\{I(X ; C)-I(X ; S)+I(X ; S \mid C)\}$ in Eq.(7) is rewritten as $\{I(X ; C)-I(X ; S)\}$. This assumption makes MRMR only interested in which variables has an edge with $C$, i.e., parents and children of $C$.

Assumption 1. $\forall V_{i}, V_{j} \in V$ and $i \neq j, V_{i}$ and $V_{j}$ are assumed to be conditionally independent given the class attribute $C$, that is, $P\left(V_{i}, V_{j} \mid C\right)=P\left(V_{i} \mid C\right) P\left(V_{j} \mid C\right)$.

To tackle the redundancy term $I(X ; S)$, Assumption 2 assumes the selected features in $S$ are conditionally independent with each other conditioning on a feature $X$ in $V \backslash S$ (i.e. conditioning on a currently unselected feature). By the chain rule, $H(S \mid X)=\sum_{i=1}^{|S|} H\left(V_{i} \mid V_{i-1}, \cdots, V_{1}, X\right)$ holds. Under Assumption 2, we have $I(X ; S)=$ $H(S)-\sum_{i=1}^{|S|} H\left(V_{i}\right)+\sum_{i=1}^{|S|} I\left(V_{i} ; X\right)$. Since at each iteration $H(S)-\sum_{i=1}^{|S|} H\left(V_{i}\right)$ is the same for all unselected features in $V \backslash S$ and thus removing them will have no effect on the choice of features, the term $I(X ; S)$ in Eq.(7) is rewritten as $\sum_{i=1}^{|S|} I\left(V_{i} ; X\right)\}$ with the pairwise mutual information between a currently unselected feature $X$ and a feature $V_{i}$ in $S$ without conditioning on other features.

Assumption 2. The selected features in $S$ are conditionally independent given an unselected feature $X \in V \backslash S$ , that is, $P(S \mid X)=\prod_{i=1}^{|S|} P\left(V_{i} \mid X\right)$ where $V_{i} \in S$.

Under Assumptions 1 and 2, we reformulate Eq.(7) as Eq.(8), i.e., the MRMR objective function. The MRMR approach reduces Eq.(6) to a linear combination of low-order mutual information terms. To select relevant features with regard to $C$, at each iteration, Eq.(8) selects the feature $X^{*}$ that has the maximum relevancy with $C$ and the minimum redundancy with the features in $S$.

$$
X^{*}=\underset{X \in V \backslash S}{\arg \max }\left\{I(X ; C)-\sum_{i=1}^{|S|} I\left(V_{i} ; X\right)\right\}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Three-way variable interactions in a BN. (a) $X$ and $Y$ are each a parent or a child of $C$; (b) both $X$ and $Y$ are parents of $C$; (c) $X$ is a common child of $C$ and $Y$ while $Y$ is a spouse of $C$; and (d) $Y$ is a non-child descendant or a non-parent ancestor of $C$.

# 4.2 Output of the MRMR approach and the MB of $C$ 

Here we will link the objective function of MRMR to the learning of the MB of C. From Eq.(8), we can see that Eq.(8) only considers three variables, $C$, the variable in $S$, and the variable outside $S$. Figure 2 shows the three-way variable interactions in a BN. Using these interactions in Figure 2 and the relationship of mutual information and conditional independence discussed in Section 3.2, the output of MRMR based on Eq.(8) is analyzed as follows.

- All parents and children of $C$ enter the ouput of MRMR. In Figures 2 (a) and (b), $X$ and $Y$ are each a parent or a child of $C$. No matter whether $X$ or $Y$ enters $S$ or not (i.e., whether $X$ or $Y$ is selected by MRMR or not in the current iteration), by $I(C ;(X, Y))=I(C ; X)+I(C ; Y \mid X)$, both $I(C ;(X, Y))>I(C ; X)$ and $I(C ;(X, Y))>I(C ; Y)$ hold. In Figure 2 (a), $I(X ; Y \mid C)=0$. By $I(X ; Y ; C)=I(X ; C)-I(X ; C \mid Y)=I(Y ; C)-$ $I(Y ; C \mid X)=I(X ; Y)-I(X ; Y \mid C)$, we get $I(C ; Y)-I(X ; Y)=I(C ; Y)-I(C ; Y)+I(C ; Y \mid X)-I(X ; Y \mid C)=I(C ; Y \mid X)$. Thus $I(C ; Y)-I(X ; Y)>0$ holds in Figure 2 (a). Similarly, $I(C ; X)-I(X ; Y)>0$. In Figure 2 (b), $I(C ; Y)-$ $I(X ; Y)=I(C ; Y)>0$ and $I(C ; X)-I(X ; Y)>0$. Using Eq.(8), MRMR selects all parents and children of $C$ in its output.
- Spouses of $C$ do not enter the ouput of MRMR. In Figure 2 (c), $Y$ is a spouse of $C$ with regard to $X$. By Lemma $1, I(C ; Y)=0$ and $I(X ; C)>0$. Thus $I(C ; X)>I(C ; Y)$ and $X$ will be added to $S$ prior to $Y$. Meanwhile, since $I(C ;(X, Y))=I(C ; X)+I(C ; Y \mid X)$ and $C \Perp Y \mid X$ according to Lemma 2, we get that $I(C ;(X, Y))>I(C ; X)$. This illustrates that a child of $C$ (e.g., $X$ ) provides more predictive information of $C$ jointly with $X$ 's another parent, i.e., the spouse of $C$ which shares the same child as $C$ (e.g., $Y$ ) than by itself. Using Eq.(8), assuming that currently $X$ is added to $S$ before $Y$ due to $X$ is a child of $C$, when adding $Y$ to $S, I(C ; Y)-I(X ; Y)<0$ hold. Then using Eq.(8) MRMR do not include spouses of $C$ in its ouput.
- Non-parent ancestors and non-child descendants of $C$ do not enter the output of MRMR. As shown in Figure 2 (d), for a non-parent ancestor or a non-child descendant $Y$ of $C$ and a parent or a child $X$ of $C$ on the path from $Y$ to $C$, since $I(C ; Y \mid X)=0$ (i.e., $C \Perp Y \mid X)$ and $I(C ; X \mid Y)>0$ (i.e., $X \Perp C \mid Y)$, by $I(C ; X)-I(C ; X \mid Y)=I(C ; Y)-I(C ; Y \mid X), I(C ; X)>I(C ; Y)$ holds. Then $X$ will be added to $S$ first. When $X$ is added to $S$, does $\{X, Y\}$ provide more prediction information than $\{X\}$? By $I(C ;(X, Y))=$ $I(C ; X)+I(C ; Y \mid X)$, we get $I(C ;(X, Y))=I(C ; X)$, thus given $X, Y$ does not provide any information about $C$. As $X$ is added to $S$, we get $I(C ; Y)-I(X ; Y)=I(C ; Y)-I(C ; Y)+I(C ; Y \mid X)-I(X ; Y \mid C)=-I(X ; Y \mid C)<0$. Then $Y$ cannot be added to the output of MRMR.

In summary, for a non-parent ancestor or a non-child descendant $Y$, the parent(s) or child(ren) of $C$ on the path(s) from $Y$ to $C$ always has (have) larger mutual information with $C$, so the parent(s) or child(ren) will be added first, and once added, it is impossible for $Y$ to be added because $Y$ is independent $C$ given the parent(s) or child(ren).
However, when the sample size is small or noise data samples exist, non-parent ancestors or non-child descendants of $C$ may be added to $S$ prior to parents and children of $C$. The MRMR approach has a strong capability to mitigate problems caused by noise or small-sized data samples, since it calculates pairwise mutual information between features without conditioning on other features.
In summary, from the analysis above, we can see that the output of MRMR, i.e., the feature selection based on Eq.(8) prefers parents and children of $C$.

# 4.3 Instantiation of the MRMR approach 

There are two well-known algorithms which instantiate the MRMR approach, the mRMR (max-Relevance and Min-Redundancy) [30] and FCBF (Fast Correlation Based Filter) algorithms [40]. The mRMR algorithm needs to specify the number of PC of a target variable in advance. In fact, we do not always have the prior knowledge and thus it is not an easy task to determine a suitable value for the parameter. In contrast, FCBF does not need to specify such a parameter. So in our proposed algorithm (details in Section 5) we will employ FCBF to learn the PC of each variable. FCBF has two steps, the forward step (max-relevance) and backward step (min-redundancy).

- Forward step: FCBF selects a subset of features $S$ that $\forall X \in S, I(C ; X)>0$, then sorts the features in $S$ by their mutual information with $C$ in descending order. At this step, users always use a user-defined threshold $\delta(\delta>0)$ to control the size of $S$ satisfying $I(C ; X) \geq \delta(X \in S)$ instead of $I(C ; X)=0$.
- Backward step: beginning with the first feature $X \in S$, if $\exists Y \in S \backslash\{X\}$ such that $I(X ; Y)>I(X ; C)$, then $Y$ is removed from $S$ as a redundant feature to $X$. The FCBF algorithm is terminated until the last feature in $S$ is checked.
At the forward step, FCBF only selects features that are relevant to $C$, that is, the candidate PC of $C$. If feature $X$ is a parent or a child of $C$ and $\delta=0, I(C ; X)>\delta$ should hold. Thus, at the forward step of FCBF, if using $\delta=0$, all parents and children of $C$ enter $S$. If using $\delta>0, S$ may include a subset of parents and children of $C$. At the backward step of FCBF, for $X \in S, Y \in S$, according to the results in Section 4.2, we have the following analysis.

First, if $X$ and $Y$ are each a parent or a child of $C$ (e.g., $X$ and $Y$ in Figures 2 (a) and (b)), $I(X ; C)>I(X ; Y)$ and $I(Y ; C)>I(X ; Y)$ hold. Thus both $X$ and $Y$ cannot be used to remove each other from $S$ at the backward step of FCBF.

Second, if $Y$ is a spouse of $C$, i.e., both $Y$ and $C$ are parents of $X$ (e.g., $Y$ in Figure 2 (c)), then $I(C ; X)>I(C ; Y)$ holds and $X$ is put before $Y$ in $S$. Since $I(C ; Y)<I(X ; Y)$, then $Y$ is removed from $S$ at the backward step of FCBF.

Third, if $Y$ is an ancestor or a descendant of $C$ (e.g., $Y$ in Figure 2 (d)), $I(C ; X)>I(C ; Y)$ and $I(C ; Y)<I(X ; Y)$ hold. Since $X$ is put before $Y$ in $S, Y$ is removed from $S$.

Thus in theory FCBF prefers parents and children of $C$. At the forward step of FCBF, FCBF can use $\delta$ to control the size of $S$, but users do not need to specify the number of selected features in advance.

## 5 THE PROPOSED ALGORITHMS

Based on the analysis in Section 4 of the MRMR approach and the commonly used algorithms instantiated from MRMR, we can see that the MRMR approach can speed up computing the PC of a variable by decomposing $I(X ; C \mid S)$ into a linear combination of low-order mutual information terms. In the section, by employing the FCBF algorithm for PC learning, we propose the F2SL approach to local-to-global BN structure learning with the following three steps.

- Step 1: Learn the PC (parents and children) set of each variable in $V$ using FCBF;

```
- Step 2: Construct the DAG skeleton by combining all individual variablesq̣́ PC sets;
- Step 3: Orient edges in the skeleton obtained at Step 2.
At Step 2, F2SL constructs the DAG skeleton (i.e., undirected graph) by combining all the PC sets of individual
variables learnt at Step 1 using the symmetry constraint. The symmetry constraint in a BN means that if there is
an edge between \(V_{i}\) and \(V_{j}\), the PC set of \(V_{i}\) should contain \(V_{j}\) and the PC set of \(V_{j}\) also should contain \(V_{i}\). At Step
3, F2SL uses either score functions or conditional independence tests to orient edges in the skeleton obtained at
Step 2 .
```

At Step 3, using score functions or independence tests to orient edges, we instantiate the F2SL approach into two algorithms, F2SL-s and F2SL-c, respectively.

# 5.1 The F2SL-s algorithm 

The F2SL-s algorithm is shown in Algorithm 1. It first learns the PC set of each variable in $V$ using FCBF, then constructs the DAG skeleton using the learnt PC sets. Finally it orients edges in the DAG skeleton using a score function and a hill climbing greedy search algorithm, which is the same as MMHC for edge orientation. Thus the key difference between F2SL-s and MMHC is that F2SL-s uses FCBF to learn a DAG skeleton while MMHC employs the MMPC algorithm [35].

## 5.2 F2SL-c algorithm

Different from F2SL-s, the F2SL-c algorithm (Algorithm 2) employs independence tests for edge orientation at Step 3. Identifying all v-structures in the DAG skeleton is the first and key step to orient edges using independence tests. Thus, for a local structure of three variables, such as $A-C-D$, by Lemma 2 of the independence/ dependence relations of a variable (e.g., $A$ and $D$ ) and its spouses in Section 3, to determine whether it is a vstructure or not, we need to know the separation set that makes $A$ and $D$ conditionally independent. For example, Figure 3 gives all possible DAGs corresponding to the skeleton $A-C-D$. In Figure 3 (a), all three DAGs have the same independence/dependence of $A, C$, and $D$, i.e., $A \Perp D$ and $A \Perp D \mid C$. The DAG in Figure 3 (b) satisfies $A \Perp D$ and $A \Perp D \mid C$, thus it is a v-structure and the separate set of $A$ and $D$ is an empty set.

The separation sets are learned simultaneously with the DAG skeleton using existing MB and PC (ParentChild) leaning algorithms, however, they have to be learned separately using the MRMR approach based on Eq.(8). Since MRMR calculates pairwise mutual information between features without conditioning on other features, it cannot output the separation set of each pair of features. This is a caveat of the fast MRMR approach. To tackle this problem, we propose the FindVstructure algorithm (Algorithm 3) to learn separation sets in order to identifies v-structures in a skeleton.

Then based on the FindVstructure algorithm, the F2SL-c algorithm is described in Algorithm 2. Before introducing the FindVstructure algorithm, let us have a look at the different situations/types of separation sets of two variables in a DAG skeleton.

- Situation 1: the separation set is an empty set. In Figure 3 (a), $A$ and $D$ are dependent but become independent given $C$, and $A-C-D$ is a not v-structure. However, in Figure 3 (b), $A$ and $D$ are independent

```
Algorithm 2: The F2SL-c Algorithm
    Input: \(D\) : dataset
    Output: A (partially) DAG
    Learn PC of each variable in \(V\) using FCBF;
    Construct the DAG skeleton based on Step 1;
    Identify all v-structures in the skeleton using FindVstructure;
    Orient the remaining edges using the Meek rules;
    Output a (partially) DAG.
```

![img-2.jpeg](img-2.jpeg)

Fig. 3. Independence/dependence of $A, C$, and $D$ and $v$-structure
![img-3.jpeg](img-3.jpeg)

Fig. 4. Separation set of $A$ and $D$
but dependent given $C$, and $A-C-D$ is a v-structure. In this case, the separation set of $A$ and $D$ is an empty set.

- Situation 2: the separation set is a subset of the PC set of $A$ or $D$. In Figure 4 (a), $A, C$ and $D$ do not form a v-structure. Thus $A \Perp D \mid C$ and $A \Perp D \mid C, E$ hold. In Figure 4 (b), $A, C$ and $D$ form a v-structure, then $A \Perp D \mid E$ and $A \Perp D \mid C, E$. In this case, both $E$ and $C$ are the common PC of $A$ and $B$. In Figure 4 (c), $A \Perp D \mid E$ and $A \Perp D \mid G$. In this case, $E \in P C(D)$ and $G \in P C(A)$. In Figure 4 (c), the separation set of $A$ and $D$ is a subset of the PC set of $A$ or $D$.
From the above discussions, we see that for a local structure $A-C-D$, a separation set of $A$ and $D$ in a DAG skeleton will be a subset of the PC set of $A$ or $D$. Thus we do not need to search for the separation set for $A$ and $D$ from the union of the PC sets of $A$ and $D$. With these observations we propose the FindVstructure algorithm (Algorithm 3) to find separation sets and to determine v-structures. For a skeleton $A-C-D$ in a DAG skeleton, instead of searching for the separation set for $A$ and $D$ from the union of the PC sets of $A$ and $D$, FindVstructure divides this search into the following three steps.
- Step 1 (Lines 3-5). If $A \Perp D \mid C$ holds, $A-C-D$ is not a v-structure. Otherwise, go to Step 2.
- Step 2 (Lines 6-9). If $A \Perp D$ and $A \Perp D \mid C$ hold, $A-C-D$ is oriented as a v-structure. Otherwise, go to Step 3.
- Step 3 (Lines 10-12). Assume $P C(A)$ is the PC set of $A$, Step 3 tests all subsets of $P C(A)$ (or $P C(D)$ ) excluding $C$. Once finding a subset $S$ that makes both $A \Perp D \mid S$ and $A \Perp D \mid S \cup\{C\}$ hold, $A-C-D$ is oriented as a v-structure. Otherwise, Step 3 continues until all subsets within $P C(A)$ are checked.

```
Input: Skeleton-DAG
Output: Vstructure-DAG
for any local structure \(A-C-D\) in Skeleton-DAG do
    if \(A \Perp D \mid C\) then
        continue;
    end
    if \(A \Perp D\) and \(A \Perp D \mid C\) then
        Orient \(A-C-D\) as \(A \rightarrow C \leftarrow D\);
        continue;
    end
    if \(2 S \subseteq P C_{\Delta}\left(\right.\) or \(\left.P C_{D}\right) \mid\{C\}\) such that \(A \Perp D \mid S\) and \(A \Perp D \mid S \cup\{C\}\) then
            Orient \(A-C-D\) as \(A \rightarrow C \leftarrow D\);
    end
end
```


# 6 EXPERIMENTS 

In this section, we will systematically evaluate the F2SL-s and F2SL-c algorithms. In Section 6.1, we describe the datasets, comparison methods, and evaluation metrics in the experiments. In Section 6.2, we report the results of F2SL-s and F2SL-c with the five representative local-to-global BN structure learning algorithms, and in Section 6.3, we analyze why F2SL-s and F2SL-c are better than the five rivals.

### 6.1 Experiment setting

To evaluate the F2SL-s and F2SL-c algorithms ${ }^{1}$, we use two groups of data generated from the six benchmark BNs as shown in Table $1^{2}$. One group includes 10 data sets each with 500 data instances, and the other group also contains 10 data sets each with 1,000 data instances.

All experiments were conducted on a computer with Intel(R) i7-8700, 3.2GHz CPU, and 16GB memory. The significance level for independence tests is set to 0.01 . In all Tables in Section 6, the symbol "-" denotes that an algorithm does not produce results when the running time of the algorithm exceeded 48 hours. We compare the F2SL-s and F2SL-c algorithms against the following five representative local-to-global BN structure learning algorithms:

- GSBN [24]. The GSBN algorithm first uses the GSMB algorithm to learning the MB of each variable for constructing the skeleton of a BN, then employs conditional independence tests to orient edges.
- MMHC [37]. The MMHC algorithm first employs the MMPC algorithm to learning the PC of each variable for constructing the skeleton of a BN, then uses a score function and a hill climbing greedy search method to orient edges ${ }^{3}$.
- MMHC-c. The MMHC-c algorithm is proposed by us. Compared to MMHC, MMHC-c uses MMPC to learn a DAG skeleton, then it uses conditional independence tests to orient edges.
- SLL+C/G [26]. The SLL+C and SLL+G algorithms learn the MB of each variable using a score-based MB learning algorithm, then SLL+C uses conditional independence tests to orient edges while SLL+G employs score functions to orient edges. ${ }^{4}$
- GGSL [12]. The GGSL algorithm starts to learn a local BN structure of a randomly selected variable using a score-based MB algorithm, then gradually expands the learnt structure until the entire structure is learnt.

[^0]
[^0]:    ${ }^{1}$ The source codes of F2SL-x/c are available a thttps://github.com/kuiy/CausalLearner
    ${ }^{2}$ The data sets are available at http : / /pages.mtu.edu/ Ilebrown/supplements/mmhc_paper/mmhc_index.html
    ${ }^{3}$ The source codes of MMHC are available at http://mensxmachina.org/en/software/probabilistic-graphical-model-toolbox
    ${ }^{4}$ The source codes of SLL+C/G are available at https://www.cs.helsinki.fi/u/tzniinim/uai2012

Table 1. Summary of benchmark BNs


- NOTEARS [45]. The NOTEARS algorithm learns a global BN structure using continuous optimization and score functions.
- DAG-GNN [41]. The DAG-GNN algorithm learns a global BN structure using graph neural networks.

Using the two groups of data sets, in addition to running time (in seconds), we evaluate our algorithms in structure learning quality against the eight rivals from two aspects, structure errors and structure correctness. The metrics of structural errors (i.e. number of extraneous edges) are described below.

- SHD (Structural Hamming Distance): the sum of the values of Miss, Extra, and Reverse as follows.
- Miss: the number of missing edges in the network structure learnt by the algorithm against the true network structure.
- Extra: the number of extra edges in the learnt BN.
- Reverse: the number of edges with wrong directions according to the true structure.

The metrics of structural correctness (i.e., number of correctly oriented edges) are Ar_Precision, Ar_Recall, and F1 described as follows.

- Ar_Recall $=\frac{\text { *correctly predicted arrowheads }}{\text { *predicted arrowheads }}$

The number of correctly predicted arrowheads in the output divided by the number of edges in the output of an algorithm.

- Ar_Precision $=\frac{\text { *correctly predicted arrowheads }}{\text { *true arrowheads }}$

The number of correctly predicted arrowheads in the output divided by the number of true arrowheads in a test DAG.

- Ar_F1. F1 $=2 *$ (Ar_Precision * Ar_Recall)/(Ar_Precision + Ar_Recall). Compared to SHD, Ar_F1 not only considers extraneous edges, but also correct edges.
In the experiments, for an algorithm, we report the average results of these metrics over the ten data sets in each group.


# 6.2 Results of Bayesian network structure learning 

In this section, we will report the experimental results of F2SL-c and F2SL-s vs. the eight rivals in terms of time efficiency and quality of learned structures, respectively.

1. Time efficiency. The last columns in Tables 2 and 3 show that F2SL-c and F2SL-s are significantly faster than GSBN, MMHC, SLL+C, SLL+G, MMHC-C, GGSL, NOTEARS, and DAG-GNN in both groups of datasets. GGSL, SLL+C, NOTEARS, DAG-GNN, and SLL+G are not scalable to a large size of a BN network. Based on the normalized running time results shown in Table 5, F2SL-s is up to 15, 15, 50800, 32408, 58065 times faster than GSBN, MMHC, SLL+C, SLL+G, and GGSL, respectively. Figures 5 and 6 show that the running time of GSBN and MMHC increases with the size of BNs networks while F2SL-c and F2SL-s are much more scalable.
2. Structure errors. Tables 2 to 3 show the BN quality by SHD of F2SL-c and F2SL-s against the eight rivals.
(1) F2SL-c and F2SL-s against GSBN. We can see that for both groups of datasets (with 500 and 1000 samples respectively), F2SL-c and F2SL-s are inferior to GSBN on the Hailfinder, Munin, and Link networks, since the

Table 2. Summaries of wrongly learnt edges and time efficiency for the data sets of Group 1(size=500)


Table 3. Summaries of wrongly learnt edges and time efficiency for the data sets of Group 2 (size $=1,000$ )


Table 4. Comparison of correctly learnt edge directions


![img-4.jpeg](img-4.jpeg)

Fig. 5. Running time with varying variables using sample size 500 (each point denotes running time of an algorithm on a BN in Table 1)
![img-5.jpeg](img-5.jpeg)

Fig. 6. Running time with varying variables using sample size 1000 (each point denotes running time of an algorithm on a BN in Table 1)
values of both Extra and Reverse of GSBN are much smaller than those of F2SL-c and F2SL-s. GSBN employs the GSMB algorithm to find the MB of each feature for constructing the DAG skeleton. Since GSMB uses the entire feature subset currently selected for computing Eq.(6), the number of data samples required by GSMB is exponential to the size of the MB. In Hailfinder, Munin, and Link networks, for both groups of datasets, the size of the MB of each feature selected by GSMB is much small. As a result, GSBN misses many true edges (i.e. has higher Miss values), but smaller Extra and Reverse of GSBN than F2SL-c and F2SL-s make it overall SHD lower than F2SL-c and F2SL-s.
(2) F2SL-c and F2SL-s against MMHC and MMHC-c. Using both groups of datasets, we have the following observations. F2SL algorithms learned a DAG skeleton better than MMHC. Both F2SL-c and MMHC-c have the same orientation process and the difference in their performance lies in learning skeletons. The BN structures learnt by MMHC-c have much more extra edges than those learnt by F2SL-c, but have slightly less missing edges than the BN structures learnt by F2SL-c. This indicates that F2SL finds more accurate skeletons than MMHC. Edge orientation in F2SL-c (by a conditional independence test) is better than edge orientation in MMHC (by

a score function). The edge orientation by a scoring function greedily deletes edges during edge orientation, and the deletion reducers the performance of BN learning since this edge deletion procedure not only deletes wrong edges, but may also remove correct edges. MMHC and F2SL-s employ the same orientation strategy. The skeleton learnt by F2SL is better than that learnt by MMHC as we discussed above, but after edge orientations, the performance of MMHC and F2SL-s are similar and the reduced performance of F2SL-s is due to edge deletion. To confirm this, we compare F2SL-c, which does not delete edges in the orientation process, with MMHC. On the Mildew, Hailfinder, Munin, and Gene networks, F2SL-c achieves better SHD than MMHC, and this confirms that deleting edges hurts the overall performance. Pigs is a special data set for MMHC which achieve 0 missing edges ( $100 \%$ recall rate as shown in Table 6 in Section 6.3). Such an exceptional performance does not repeat in other data sets.
(3) F2SL-c and F2SL-s against SLL+C/G. Both SLL+C and SLL+G only produce the results on the Mildew and Hailfinder networks due to expensively computational costs. We can see that the SHD values of both SLL+C and SLL+G are very close to those of F2SL-c and F2SL-s, but SLL+C and SLL+G are very computationally expensive.
(4) F2SL-c and F2SL-s against NOTEARS and DAG-GNN. From Tables 2 to 3, we can see that NOTEARS and DAG-GNN are computationally expensive and are not scalable to large and/or high dimensional data sets, thus they do not produce the results on the Pigs, Link and Gene networks. NOTEARS and DAG-GNN often achieve a smaller number of missing edges but a much larger number of extra edges than F2SL-c and F2SL-s. In small BN networks, the SHD values of DAG-GNN are competitive with those of F2SL-c and F2SL-s.
3. Structural correctness. Table 4 reports the BN structure quality by Ar_Recall, Ar_Precision, and Ar_F1 of F2SL-c and F2SL-s and their rivals. Although on the Hailfinder, Munin, and Link networks, GSBN achieves less structure errors than F2SL-c and F2SL-s in terms of $S H D$, it is inferior to F2SL-c/s on Ar_F1 with both groups of data as shown in Table 4. As discussed above, GSMB employed by GSBN finds much samller sized MBs than FCBF used by F2SL-c and F2SL-s, and thus GSMB has missed more true edges than F2SL-c and F2SL-s, and GSBN achieves much lower value of Ar_Recall than F2SL-c and F2SL-s.

F2SL-c and F2SL-s are better than its eight rivals on all networks except for the Pigs network. F2SL-c and F2SLs learn more correct edges than its eight rivals. From Tables 2 and 3, F2SL-s and MMHC are very competitive in terms of Miss, thus they are comparable on Ar_F1 as shown in Table 4. The Pigs network is a very special for MMHC which achieves $100 \%$ recall (as shown in Table 6).

From Table 4, we can see that F2SL-c and F2SL-s achieves larger Recall than NOTEARS and DAG-GNN (except for the Mildew network using 500 samples), although NOTEARS and DAG-GNN get smaller Miss than F2SL-c and F2SL-s (as shown in Tables 2 and 3). This is because NOTEARS and DAG-GNN have large orientation errors. Overall, F2SL-s and F2SL-s achieve better Ar_F1 than NOTEARS and DAG-GNN.
4. Simultaneous comparison of time efficiency and structure quality. In BN structure learning, an algorithm may be chosen to sacrifice structure learning quality for computational efficiency, while another algorithm may be chosen to sacrifice time efficiency for structure learning quality. Therefore it is interesting to compare two algorithms in terms of both time efficiency and quality of structure learning at the same time.

For this comparison, we normalize SHD, Ar_F1, and running time reported in Tables 2 to 4. Normalized SHD (or Ar_F1 or running time) is the value of SHD (or Ar_F1 or running time) of an algorithm for a particular sample size and network divided by the SHD (or Ar_F1 or running time) of F2SL-s on the same sample size and network. The normalized results are shown in Table 5. A normalized SHD or running time greater than one implies that the algorithm is worse or slower than F2SL-s on the same learning task, while a normalized Ar_F1 smaller than one implies that the algorithm is worse than F2SL-s on the same learning task.

Using the normalized results in Table 5, we explore the trade-off between structure quality (i.e. SHD or Ar_F1) and time efficiency of each algorithm. Figure 7 shows the logarithm of the normalized time versus the logarithm of the normalized SHD for the two groups of datasets with sample sizes 500 and 1000 respectively, and Figure 8 illustrates the logarithm of the normalized time vs. the normalized $\mathrm{Ar}_{-} \mathrm{F} 1$ for the two groups of datasets with

![img-6.jpeg](img-6.jpeg)

Fig. 7. Normalized Time vs. Normalized SHD with 500 (left) and 1000 (right) data samples
sample sizes 500 and 1000 respectively. Each point in Figures 7 and 8 denotes the performance in terms of the two metrics of a given algorithm on learning one of the six BN networks. Since we are using normalized measures with respect to the measures of F2SL-s, the performance measures of F2SL-s always fall on point $(1,1)$ and thus are not indicated in the figures.

We can see that in Figure 7, there are no algorithms (except for F2SL-c) fall in the grey area, indicating that no algorithms outperform F2SL-s in terms of both running time and SHD. In terms of SHD, F2SL-s and F2SL-c are very competitive with the other algorithms in most cases while no algorithms are faster than F2SL-s and F2SL-c.

Figure 8 illustrates that no algorithms (except for F2SL-c) fall in the grey area, indicating that no algorithms are better than F2SL-s in terms of both running time and Ar_F1, except for F2SL-c. GGSL is better than F2SL-s only in one case in the left figure of Figure 8 and SLL+C is superior to F2SL-s in one case in the right figure of Figure 8. Except for the two cases, no other algorithms outperform F2SL-s and F2SL-c.

In summary, in terms of time efficiency, F2SL-c and F2SL-s are significantly faster than GSMB, MMHC, GGSL, SLL+C, SLL+G, NOTEARS and DAG-GNN. Both of them achieve competitive performance against their eight rivals in terms of the metrics of structural errors. In terms of the metrics of structural correctness, F2SL-c and F2SL-s are better than their five rivals. In the following, we will analyze why F2SL-c and F2SL-s are better than these rivals.

# 6.3 Why the proposed algorithms are better? 

The efficiency and quality of MB or PC learning for each feature are the key to local-to-global BN learning algorithms. Among F2SL-c, F2SL-s and their five rivals, GSBN employs the GSMB algorithm for learning the MB (not the PC) of each feature to constructing skeletons, whereas MMHC, SLL+C, SLL+G, GGSL, F2SL-c, and F2SL-s learn the PC set of each feature for constructing the skeletons. GSBN employs a different method to learn the skeleton of a BN from MMHC, SLL+C, SLL+G, GGSL, F2SL-c, and F2SL-s. In this section, we evaluate the performance of the PC learning algorithms used by F2SL-c, F2SL-s, MMHC, SLL+C, SLL+G, and GGSL to find out why F2SL-c and F2SL-s are better. For the evaluation of the performance of the PC learning algorithms, we use precision and recall as described below (and for time efficiency evaluation, we use running time).

- Precision. The number of true positives in the output of a PC learning algorithm (i.e. the number of variables in the output belonging to the true PC of a target variable) divided by the total number of variables in the output.
- Recall. The number of true positives in the output divided by the size of the true PC set of a variable.

Table 5. Comparison of structure learning methods on different groups of data sets in terms of normalized metrics ( $\downarrow$ means the smaller, the better while $\uparrow$ denotes that the bigger, the better)


![img-7.jpeg](img-7.jpeg)

Fig. 8. Normalized Time vs. Normalized Ar_F1 with 500 (left) and 1000 (right) data samples

- F1. $F 1=2 *($ precision $*$ recall $) /($ precision + recall $)$.

Proc. ACM Meas. Anal. Comput. Syst., Vol. 37, No. 4, Article 111. Publication date: August 2018.

6.3.1 FCBF versus standard PC learning algorithm. As described in Section 5, F2SL-c and F2SL-s employ the FCBF algorithm to learn the PC of each variable for skeleton construction, and MMHC uses the MMPC algorithm [35] to find PC of each variable. SLL+C/G and GGSL employ SLL-PC and $S^{2}$ TMB-PC to learn the PC of each variable in a data set for skeleton construction. In this section, in addition to MMPC, SLL-PC, and $S^{2}$ TMB-PC, we do a comprehensive comparison of FCBF with another two widely used PC learning algorithms, HITON-PC [2] and PC-simple [22] to investigate why F2SL-c and F2SL-s are better than MMHC, SLL+C, SLL+G, and GGSL.

Table 6 shows the PC learning quality and running time of the PC learning algorithms. Table 7 gives the normalized running time and F1. Normalized F1 or running time is the value of F1 or running time of an algorithm for a particular sample size and network divided by the F1 or running time of F2SL-s on the same sample size and network. In Table 7, a normalized running time greater than one indicates that an algorithm is slower than FCBF, while a normalized F1 smaller than one implies that an algorithm is worse than FCBF.

From Tables 6 and 7, we can see that FCBF is significantly faster than the other PC methods on both groups of data sets. This explains why F2SL-c and F2SL-s are much more efficient than the other five BN structure learning algorithms. SLL-PC and $S^{2}$ TMB-PC are so computationally expensive, and this explains why SLL+C, SLL+G, and GGSL are not scalable to large-sized networks.

In PC learning quality, in terms of F1, FCBF is better than MMPC, HITON-PC, SLL-PC and $S^{2}$ TMB-PC on almost all networks. FCBF achieves almost the same F1 value as PC-simple on the Hilfinder, Pigs, and Gene networks, but it is significantly better than PC-simple on the remaining networks. In terms of recall, FCBF is very competitive with its rivals while it achieves better precision than these rivals, except for SLL-PC and $S^{2}$ TMBPC on the Mildew network. However, SLL-PC and $S^{2}$ TMB-PC are significantly worse than FCBF in terms of recall. Thus on average F2SL-c and F2SL-s are better than SLL+C, SLL+G, and GGSL. On the Hilfinder network, FCBF, SLL-PC, and $S^{2}$ TMB-PC are very comparable, thus F2SL-c and F2SL-s are competitive with SLL+C, SLL+G, and GGSL.

For FCBF and MMPC, MMPC calculates the high order mutual information between $X$ and $C$ conditioning on a subset of the already selected features $S$. In the worst case, MMPC needs to explore all possible subsets of $S$. When the size of PC sets becomes large, MMPC will be very computationally expensive and require large data samples for reliable independence tests. A large size of PC sets and/or small-sized data samples will make MMPC impractical in many real-world applications. Just as we discussed in Section 4, FCBF can deal with small and/or high dimensional datasets, since FCBF computes the pairwise mutual information between $X$ and $C$ without conditioning on other features.

Table 6 has shown that FCBF achieves higher precision rate than and almost the same recall rate as MMPC although FCBF only uses pairwise mutual information to learn an approximate PC set of a variable. When the size of a PC set is large (e.g. in Munin) or a BN network has a large number of variables (e.g. in Gene), FCBF is much better than MMPC on both recall and precision measures. In Tables 2 and 3 in Section 6.2, we observed that a higher recall achieved by MMPC does not transfer to smaller missing edges in BN structures learnt by MMHC in comparison with F2SL-c. FCBF achieves higher precision than MMPC. This means that the output of MMPC contains more false PCs than FCBF and hence the BN structures learnt by MMHC and MMHC-c should have more extra edges than those learnt by F2SL-c. But MMHC achieves a competitive number of extra edges with F2SL-c (except for the Gene network) due to edge deletion at the edge orientation step, while the BN structures learnt by MMHC-c have more extra edges and less missing edges than those learnt by F2SL-c on all networks except for the Mildew network due to non-edge deletion. In summary, for local-to-global structure learning, regardless of which method, score-based or constraint-based method, is used for edge orientations, it is crucial to find a correct DAG skeleton.
6.3.2 Experimental analysis of the threshold $\delta$ for FCBF. Although FCBF does not require users to specify the number of selected features before learning, it needs a user-specified parameter $\delta$ to control the number of

Table 6. Comparison of FCBF with four PC learning algorithms


Table 7. Comparison of PC learning methods with different groups of data sets in terms of normalized metrics ( $\downarrow$ means the smaller, the better while $\uparrow$ denotes that the bigger, the better)


candidate parents and children of a variable of interest at the forward step of FCBF as described in Section 4.3.

Proc. ACM Meas. Anal. Comput. Syst., Vol. 37, No. 4, Article 111. Publication date: August 2018.

![img-8.jpeg](img-8.jpeg)

Fig. 9. F1 of FCBF on the six BNs when varying the value of $\delta$ from 0 to 0.1 with different groups of data sets. The red line denotes $\delta=0.05$.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Precision of FCBF on the six BNs when varying the value of $\delta$ from 0 to 0.1 with different groups of data sets. The red line denotes $\delta=0.05$.

A large $\delta$ makes FCBF remove false positives as well as true positives. A small $\delta$ leads FCBF to find more true positives and more false positives as well.

To choose an optimal value of $\delta$ for FCBF, we have investigated the F1, recall, and precision of FCBF using different $\delta$ value from 0 to 0.1 with the six BNs in Table 1. In Figure 9, we can see that when $\delta$ is small, FCBF gets a low value of F1. As $\delta$ increases, the value of F1 gradually becomes high and stable. The explanation is that when $\delta$ is small, as shown in Figure 10, many false positives will enter the final output of FCBF, this reduces the precision of FCBF. However, Figure 11 illustrates that the value of $\delta$ does not have much impact on the true PC entering the output of FCBF, since parents and children of a variable should have a strong dependency relationship with the variable and they are less likely be discarded even when $\delta$ becomes big. As $\delta$ increases, some true positives will be discarded. Using the six BNs, we can see that when $\delta$ is up to 0.05 , FCBF is stable and almost gets the highest F1, and thus in all the experiments in Section 6, we choose 0.05 as the value of $\delta$ for FCBF.

# 7 CONCLUSION 

In this paper, we link feature selection methods to BN structure learning to improve computational efficiency, and propose the F2SL framework for BN structure learning by using the FCBF algorithm. By instantiating the F2SL

![img-10.jpeg](img-10.jpeg)

Fig. 11. Recall of FCBF on the six BNs when varying the value of $\delta$ from 0 to 0.1 with different groups of data sets. The red line denotes $\delta=0.05$.
framework, we propose two efficient local-to-global structure learning algorithms, F2SL-c and F2SL-s. Using six benchmark BNs, the experimental results have shown that F2SL-c and F2SL-s significantly improve computational efficiency of BN structure learning compared to the eight state-of-the-art BN structure learning algorithms and both also achieve competitive structure learning quality with the eight rivals.

# ACKNOWLEDGMENTS 

This work is partially supported by the National Key Research and Development Program of China (under grant 2020AAA0106100), National Natural Science Foundation of China (under Grant 61876206), and Open Project Foundation of Intelligent Information Processing Key Laboratory of Shanxi Province (under grant CICIP2020003).
