# Article 

## Bayesian Network Model Averaging Classifiers by Subbagging

Shouta Sugahara ${ }^{1, * *}$, Itsuki Aomi ${ }^{2 *}$ and Maomi Ueno ${ }^{1 *}$


#### Abstract

check for updates Citation: Sugahara, S.; Aomi, I.; Ueno, M. Bayesian Network Model Averaging Classifiers by Subbagging. Entropy 2022, 24, 743. https:// doi.org/10.3390/e24050743


Academic Editors: Andrea Prati, Luis Javier García Villalba and Vincent A. Cicirello

Received: 10 April 2022
Accepted: 19 May 2022
Published: 23 May 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Graduate School of Informatics and Engineering, The University of Electro-Communications, 1-5-1, Chofugaoka, Chofu-shi 182-8585, Japan; ueno@ai.lab.uec.ac.jp
2 Sansan Inc., Tokyo 150-0001, Japan; aomi@sansan.com

* Correspondence: sugahara@ai.lab.uec.ac.jp

Abstract: When applied to classification problems, Bayesian networks are often used to infer a class variable when given feature variables. Earlier reports have described that the classification accuracy of Bayesian network structures achieved by maximizing the marginal likelihood (ML) is lower than that achieved by maximizing the conditional log likelihood (CLL) of a class variable given the feature variables. Nevertheless, because ML has asymptotic consistency, the performance of Bayesian network structures achieved by maximizing ML is not necessarily worse than that achieved by maximizing CLL for large data. However, the error of learning structures by maximizing the ML becomes much larger for small sample sizes. That large error degrades the classification accuracy. As a method to resolve this shortcoming, model averaging has been proposed to marginalize the class variable posterior over all structures. However, the posterior standard error of each structure in the model averaging becomes large as the sample size becomes small; it subsequently degrades the classification accuracy. The main idea of this study is to improve the classification accuracy using subbagging, which is modified bagging using random sampling without replacement, to reduce the posterior standard error of each structure in model averaging. Moreover, to guarantee asymptotic consistency, we use the $K$-best method with the ML score. The experimentally obtained results demonstrate that our proposed method provides more accurate classification than earlier BNC methods and the other state-of-the-art ensemble methods do.

Keywords: Bayesian networks; classification; model averaging; structure learning

## 1. Introduction

A Bayesian network is a graphical model that represents probabilistic relations among random variables as a directed acyclic graph (DAG). The Bayesian network provides a good approximation of a joint probability distribution because it decomposes the distribution exactly into a product of the conditional probabilities for each variable when the probability distribution has a DAG structure, depicted in Figure 1.

Bayesian network structures are generally unknown. For that reason, they must be estimated from observed data. This estimation problem is called Learning Bayesian networks. The most common learning approach is a score-based approach, which seeks the best structure that maximizes a score function. The most widely used score is the marginal likelihood for finding a maximum a posteriori structure [1,2]. The marginal likelihood (ML) score based on the Dirichlet prior ensuring likelihood equivalence is called Bayesian Dirichlet equivalence [2]. Given no prior knowledge, the Bayesian Dirichlet equivalence uniform (BDeu), as proposed by Buntine [1], is often used. These scores require an equivalent sample size (ESS), which is the value of a user-determined free parameter. As demonstrated in recent studies, ESS plays an important role in resulting network structure estimated using BDeu [3-6]. However, this approach has an associated NP-hard problem [7]: the number of structure searches increases exponentially with the number of variables.

![img-0.jpeg](img-0.jpeg)

Figure 1. Example of a Bayesian network.
Bayesian network classifiers (BNC), which are special cases of Bayesian networks designed for classification problems, have yielded good results in real-world applications, such as facial recognition [8] and medical data analysis [9]. The most common score for BNC structures is conditional log likelihood (CLL) of the class variable given all the feature variables [10,11,12]. Friedman et al. [10] claimed that the structure maximizing CLL, called a discriminative model, provides a more accurate classification than that maximizing the ML. The reason is that the CLL reflects only the class variable posterior, whereas the ML reflects the posteriors of all the variables.

Nevertheless, ML is known to have asymptotic consistency, which guarantees that the structure which maximizes the ML converges to the true structure when the sample size is sufficiently large. Therefore, Sugahara et al. [13], Sugahara and Ueno [14] demonstrated experimentally that the BNC performance achieved by maximizing the ML is not necessarily worse than that achieved by maximizing CLL for large data. Unfortunately, their experiments also demonstrated that the classification accuracy of the structure maximizing the ML rapidly worsens as the sample size becomes small. They explained the reason: the class variable tends to have numerous parents when the sample size is small. Therefore, the conditional probability parameter estimation of the class variable becomes unstable because the number of parent configurations becomes large. Then the sample size for learning a parameter becomes sparse. This analysis suggests that exact learning BNC by maximizing the ML to have no parents of the class variable might improve the classification accuracy. Consequently, they proposed exact learning augmented naive Bayes classifier (ANB), in which the class variable has no parent and in which all feature variables have the class variable as a parent. Additionally, they demonstrated the effectiveness of their method empirically.

The salient reason for difficulties with this method is that the error of learning structures becomes large when the sample size becomes small. Model averaging, which marginalizes the class variable posterior over all structures, has been regarded as a method to alleviate this shortcoming [15,16,17,18]. However, the model averaging approach confronts the difficulty that the number of structures increases super-exponentially for the network size. Therefore, averaging all structures with numerous variables is computationally infeasible. The most common approach to this difficulty is the $K$-best method [19,20,21,22,23,24,25], which considers only the $K$-best scoring structures.

Another point of difficulty is that the posterior standard error of each structure in the model averaging becomes large for a small sample size; it then decreases the classification accuracy. As methods to reduce the posterior standard error, resampling methods such as the adaboost (adaptive boosting) [26], bagging (bootstrap aggregating) [27], and subbagging (subsampling aggregating) [28] are known. In addition, Jing et al. [29] proposed ensemble class variable prediction using adaboost. That study demonstrated its effectiveness empirically. However, this method tends to cause overfitting for small data because adaboost tends to be sensitive to noisy data [30]. Later, Rohekar et al. [31] proposed B-RAI, a model averaging method with bagging, based on the RAI algorithm [32], which learns a structure by recursively conducting conditional independence (CI) tests, edge direction, and structure decomposition into smaller substructures. The B-RAI increases the number of models for model averaging using multiple bootstrapped datasets. However, B-RAI is

inapplicable for bagging to the posterior of the structures. Therefore, the posterior standard error of the structures is not expected to decrease. In addition, the CI tests of the B-RAI are not guaranteed to have asymptotic consistency. Although B-RAI reduces the computational costs, it degrades the classification accuracy for large data.

The main idea of this study is to improve the classification accuracy using the subbagging to reduce the posterior standard error of structures in model averaging. Moreover, to guarantee asymptotic consistency, we use the $K$-best method with the ML score. The proposed method, which we call Subbagging $K$-best method (SubbKB), is expected to present the following benefits: (1) Because the SubbKB has an asymptotic consistency for the true class variable classification, the class variable posterior converges to the true value when the sample size becomes sufficiently large; (2) even for small data, subbagging reduces the posterior standard error of each structure in the $K$-best structures and improves the classification accuracy. For this study, we conducted experiments to compare the respective classification performances of our method and earlier methods. Results of those experiments demonstrate that SubbKB provides more accurate classification than the earlier BNC methods do. Furthermore, our experiments compare SubbKB and the other state-of-the-art ensemble methods. Results indicate that SubbKB outperforms the state-of-the-art ensemble methods.

This paper is organized as follows. In Section 2 we review Bayesian networks and BNCs. In Section 3 we review model averaging of BNCs. In Section 4 we describe SubbKB and prove that SubbKB asymptotically estimates a true conditional probability. In Section 5 we describe in detail the experimental setup and results. Finally, we conclude in Section 6.

# 2. Bayesian Network Classifier 

### 2.1. Bayesian Network

Letting $\left\{X_{0}, X_{1}, \cdots, X_{n}\right\}$ be a set of $n+1$ discrete variables, then $X_{i},(i=0, \cdots, n)$ can take values in the set of states $\left\{1, \cdots, r_{i}\right\}$. One can write $X_{i}=k$ when observing that an $X_{i}$ is state $k$. According to the Bayesian network structure $G$, the joint probability distribution is $P\left(X_{0}, X_{1}, \cdots, X_{n}\right)=\prod_{i=0}^{n} P\left(X_{i} \mid \Pi_{i}, G\right)$, where $\Pi_{i}$ is the parent variable set of $X_{i}$. Letting $\theta_{i j k}$ be a conditional probability parameter of $X_{i}=k$ when the $j$-th instance of the parents of $X_{i}$ is observed (we write $\Pi_{i}=j$ ), we define $\Theta=\left\{\theta_{i j k}\right\}(i=0, \cdots, n ; j=$ $1, \cdots, q_{i} ; k=1, \cdots, r_{i}$ ). A Bayesian network is a pair $B=(G, \Theta)$.

The Bayesian network (BN) structure represents conditional independence assertions in the probability distribution by $d$-separation. First, we define collider, for which we need to define the d-separation. Letting path denote a sequence of adjacent variables, the collider is defined as shown below.

Definition 1. Assuming a structure $G=(\mathbf{V}, \mathbf{E})$, a variable $Z \in \mathbf{V}$ on a path $\rho$ is a collider if and only if there exist two distinct incoming edges into $Z$ from non-adjacent variables.

We then define d-separation as explained below.
Definition 2. Assuming we have a structure $G=(\mathbf{V}, \mathbf{E}), X, Y \in \mathbf{V}$, and $\mathbf{Z} \subseteq \mathbf{V} \backslash\{X, Y\}$, the two variables $X$ and $Y$ are d-separated, given $\mathbf{Z}$ in $G$, if and only if every path $\rho$ between $X$ and $Y$ satisfies either of the following two conditions:

- $\quad \mathbf{Z}$ includes a non-collider on $\rho$.
- There is a collider $Z$ on $\rho$, and $\mathbf{Z}$ does not include $Z$ or its descendants.

We denote the d-separation between $X$ and $Y$ given $\mathbf{Z}$ in the structure $G$ as $D \operatorname{sep}_{G}(X, Y \mid \mathbf{Z})$. Two variables are d-connected if they are not d-separated.

Let $I(X, Y \mid \mathbf{Z})$ denote that $X$ and $Y$ are conditionally independent given $\mathbf{Z}$ in the true joint probability distribution. A BN structure $G$ is an independence map (I-map) if all d-separations in $G$ are entailed by conditional independence in the true probability distribution.

Definition 3. Assuming a structure $G=(\mathbf{V}, \mathbf{E}), X, Y \in \mathbf{V}$, and $\mathbf{Z} \subseteq \mathbf{V} \backslash\{X, Y\}$, then $G$ is an I-map if the following proposition holds:

$$
\forall X, Y \in \mathbf{V}, \forall \mathbf{Z} \subseteq \mathbf{V} \backslash\{X, Y\}, D \operatorname{sep}_{G}(X, Y \mid \mathbf{Z}) \Rightarrow I(X, Y \mid \mathbf{Z})
$$

Probability distributions represented by an I-map converge to the true probability distribution when the sample size becomes sufficiently large.

For an earlier study, Buntine [1] assumed the Dirichlet prior and used an expected a posteriori (EAP) estimator $\hat{\theta}_{i j k}=\left(\alpha_{i j k}+N_{i j k}\right) /\left(\alpha_{i j}+N_{i j}\right)$. In that equation, $N_{i j k}$ represents the number of samples of $X_{i}=k$ when $\Pi_{i}=j, N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$. Additionally, $\alpha_{i j k}$ denotes the hyperparameters of the Dirichlet prior distributions ( $\alpha_{i j k}$ as a pseudo-sample corresponding to $N_{i j k}$ ); $\alpha_{i j}=\sum_{k=1}^{r_{i}} \alpha_{i j k}$.

The first learning task of the Bayesian network is to seek a structure $G$ that optimizes a given score. Let $D=\left\{\mathbf{u}^{1}, \cdots, \mathbf{u}^{d}, \cdots, \mathbf{u}^{N}\right\}$ be training dataset. In addition, let each $\mathbf{u}^{d}$ be a tuple of the form $\left\langle x_{0}^{d}, x_{1}^{d}, \cdots, x_{n}^{d}\right\rangle$. The most popular marginal likelihood (ML) score, $P(D \mid G)$, of the Bayesian network finds the maximum a posteriori (MAP) structure $G^{*}$ when we assume a uniform prior $P(G)$ over structures, as presented below.

$$
G^{*}=\underset{G}{\arg \max } P(G \mid D)=\underset{G}{\arg \max } \frac{P(D \mid G) P(G)}{P(D)}=\underset{G}{\arg \max } P(D \mid G)
$$

The ML has an asymptotic consistency [33], i.e., the structure which maximizes ML converges to the true structure when the sample is large. In addition, the Dirichlet prior is known as a distribution that ensures likelihood equivalence. This score is known as Bayesian Dirichlet equivalence [2]. Given no prior knowledge, the Bayesian Dirichlet equivalence uniform (BDeu), as proposed earlier by Buntine [1], is often used. The BDeu score is represented as:

$$
P(D \mid G)=\prod_{i=0}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\frac{\alpha}{q_{i}}\right)}{\Gamma\left(\frac{\alpha}{q_{i}}+N_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(\frac{\alpha}{r_{i} q_{i}}+N_{i j k}\right)}{\Gamma\left(\frac{\alpha}{r_{i} q_{i}}\right)}
$$

where $\alpha$ denotes a hyperparameter. Earlier studies [5,6,34,35] have demonstrated that learning structures are highly sensitive to $\alpha$. Those studies demonstrated $\alpha=1.0$ as the best method to mitigate the influence of $\alpha$ for parameter estimation.

# 2.2. Bayesian Network Classifiers 

A Bayesian network classifier (BNC) can be interpreted as a Bayesian network for which $X_{0}$ is the class variable and for which $X_{1}, \cdots, X_{n}$ are feature variables. Given an instance $\mathbf{x}=\left\langle x_{1}, \cdots, x_{n}\right\rangle$ for feature variables $X_{1}, \ldots, X_{n}$, BNC $B$ predicts the class variable's value by maximizing the posterior as $\hat{c}=\operatorname{argmax}_{c \in\{1, \cdots, r_{0}\}} P(c \mid \mathbf{x}, B)$.

However, Friedman et al. [10] reported the BNC maximizing ML as unable to optimize the classification performance. They proposed the sole use of the conditional log likelihood (CLL) of the class variable given the feature variables instead of the log likelihood for learning BNC structures.

Unfortunately, no closed-form formula exists for optimal parameter estimates to maximize CLL. Therefore, for each structure candidate, learning the network structure maximizing CLL requires the use of some search methods such as gradient descent over the space of parameters. For that reason, the exact learning of network structures by maximizing CLL is computationally infeasible.

As a simple means of resolving this difficulty, Friedman et al. [10] proposed the treeaugmented naive Bayes (TAN) classifier, for which the class variable has no parent and for which each feature variable has a class variable and at most one other feature variable as a parent variable.

In addition, Carvalho et al. [12,36] proposed an approximated conditional log likelihood (aCLL) score, which is both decomposable and computationally efficient. Let-

ting $G_{A N B}$ be an ANB structure, we define $\Pi_{i}^{*}=\Pi_{i} \backslash\left\{X_{0}\right\}$ based on $G_{A N B}$. Additionally, we let $N_{i j c k}$ be the number of samples of $X_{i}=k$ when $X_{0}=c$ and $\Pi_{i}^{*}=j$ $\left(i=1, \cdots, n ; j=1, \cdots, q_{i}^{*} ; c=1, \cdots, r_{0} ; k=1, \cdots, r_{i}\right)$. Moreover, we let $N^{\prime}>0$ represent the number of pseudo-counts. Under several assumptions, aCLL can be represented as:

$$
a C L L\left(G_{A N B} \mid D\right) \propto \sum_{i=1}^{n} \sum_{j=1}^{q_{i}^{*}} \sum_{k=1}^{r_{i}} \sum_{c=1}^{r_{0}}\left(N_{i j c k}+\beta \sum_{c^{\prime}=1}^{r_{0}} N_{i j c^{\prime} k}\right) \log \frac{N_{i j+c k}}{N_{i j+c}}
$$

where

$$
\begin{gathered}
N_{i j+c k}=\left\{\begin{array}{l}
N_{i j c k}+\beta \sum_{c=1}^{r_{0}} N_{i j c^{\prime} k} \text { if } N_{i j c k}+\beta \sum_{c^{\prime}=1}^{r_{0}} N_{i j c^{\prime} k} \geq N^{\prime} \\
N^{\prime} \quad \text { otherwise, }
\end{array}\right. \\
N_{i j+c}=\sum_{k=1}^{r_{i}} N_{i j+c k}
\end{gathered}
$$

The value of $\beta$ is found using Monte Carlo method to approximate CLL. When the value of $\beta$ is optimal, then aCLL is a minimum-variance unbiased approximation of CLL. A report of an earlier study described that the classifier maximizing the approximated CLL provides a better performance than that maximizing the approximated ML.

Unfortunately, they stated no reason for why CLL outperformed ML. Differences of performance between ML and CLL in earlier studies might depend on the learning algorithms which were employed because they used not exact but approximate learning algorithms. Therefore, Sugahara et al. [13], Sugahara and Ueno [14] demonstrated by experimentation that the BNC performance achieved by maximizing the ML is not necessarily worse than that achieved by maximizing CLL for large data, although both performances may depend on the nature of the dataset. However, the classification accuracy of the structure maximizing the ML becomes rapidly worse as the sample size becomes small.

# 3. Model Averaging of Bayesian Network Classifiers 

The less accurate classification of BNCs for small data results from learning structure errors. As a method to alleviate this shortcoming, model averaging, which marginalizes the class variable posterior over all structures, is reportedly effective [15,16,17,18]. Using model averaging, the class variable's value $c$ is estimated as:

$$
\begin{aligned}
\tilde{c} & =\underset{c \in\left\{1, \cdots, r_{0}\right\}}{\arg \max } P(c \mid \mathbf{x}, D) \\
& =\underset{c \in\left\{1, \cdots, r_{0}\right\}}{\arg \max } \sum_{G \in \mathcal{G}} P(G \mid D) P(c \mid \mathbf{x}, G, D) \\
& =\underset{c \in\left\{1, \cdots, r_{0}\right\}}{\arg \max } \sum_{G \in \mathcal{G}} P(D \mid G) P(c \mid \mathbf{x}, G, D)
\end{aligned}
$$

where $\mathcal{G}$ is a set of all structures. However, the number of structures increases superexponentially for the network size. Therefore, averaging all the structures with numerous variables is computationally infeasible. The most commonly used approach to resolve this problem is a $K$-best structures method [19,21,22,23,24,25], which considers only the $K$-best scoring structures. However, the $K$-best structures method finds the best $K$ individual structures included in Markov equivalence classes, where the structures within each class represent the same set of conditional independence assertions and determine the same statistical model. To address the difficulty, Chen and Tian [20] proposed the $K$-best EC method, which can be used to ascertain the $K$ best equivalence classes directly. These methods have asymptotic consistency if they use an exact learning algorithm. Using the $K$-best scoring structures, $\left\{G^{k}\right\}_{k=1}^{K}$, the class variable posterior can be approximated as:

$$
P\left(X_{0} \mid \mathbf{x}, D\right) \approx \sum_{k=1}^{K} \frac{P\left(D \mid G^{k}\right)}{\sum_{k^{\prime}=1}^{K} P\left(D \mid G^{k^{\prime}}\right)} P\left(X_{0} \mid \mathbf{x}, G^{k}, D\right)
$$

The posterior standard error of each structure in the model averaging becomes large as the sample size becomes small; as it does so, it decreases the classification accuracy. However, resampling methods such as adaboost [26] and bagging [27] are known to reduce the standard error of estimation. Actually, Jing et al. [29] proposed the $b A N_{\text {mix }}$ boosting method, which predicts the class variable using adaboost. Nevertheless, this method is not a model averaging method. It tends to cause overfitting for small data because adaboost tends to be sensitive to noisy data [30].

Rohekar et al. [31] proposed a model averaging method named B-RAI, based on the RAI algorithm [32]. The method learns the structure by sequential application of conditional independence (CI) tests, edge direction and structure decomposition into smaller substructures. This sequence of operations is performed recursively for each substructure, along with increasing order of the CI tests. At each level of recursion, the current structure is first refined by removing edges between variables that are independently conditioned on a set of size $n_{z}$, with subsequent directing of the edges. Then, the structure is decomposed into ancestors and descendant groups. Each group is autonomous: it includes the parents of its members [32]. Furthermore, each autonomous group from the $n_{z}$-th recursion level is partitioned independently, resulting in a new level of $n_{z}+1$. Each such structure (a substructure over the autonomous set) is partitioned progressively (in a recursive manner) until a termination condition is satisfied (independence tests with condition set size $n_{z}$ cannot be performed), at which point the resulting structure (a substructure) at that level is returned to its parent (the previous recursive call). Similarly, each group in its turn, at each recursion level, gathers back the structures (substructures) from the recursion level that followed it; it then returns itself to the recursion level that precedes it until the highest recursion level $n_{z}=0$ is reached and the final structure is fully constructed. Consequently, RAI constructs a tree in which each node represents a substructure and for which the level of the node corresponds to the maximal order of conditional independence that is encoded in the structure. Based on the RAI algorithm, B-RAI constructs a structure tree from which structures can be sampled. In essence, it replaces each node in the execution tree of the RAI with a bootstrap node. In the bootstrap node, for each autonomous group, $s$ datasets are sampled with replacement from training data $D$. They calculate $\log [P(D \mid G)]$ for each leaf node in the tree ( $G$ is the structure in the leaf) using the BDeu score. For each autonomous group, given $s$ sampled structures and their scores returned from $s$ recursive calls, the B-RAI samples one of the $s$ results proportionally to their (log) score. Finally, the sampled structures are merged. The sum of scores of all autonomous sets is the score of the merged structure.

However, B-RAI does not apply bagging to the posterior of the structures. Therefore, the posterior standard error of each structure is not expected to decrease. In addition, the B-RAI is not guaranteed to have asymptotic consistency. This lack of consistency engenders the reduction of the computational costs, but degradation of the classification accuracy.

# 4. Proposed Method 

This section presents the proposed method, SubbKB, which improves the classification accuracy using resampling methods to reduce the posterior standard error of each structure in model averaging. As described in Section 3, the existing resampling methods are not expected to reduce the posterior standard error of each structure in model averaging sufficiently. A simple method to resolve this difficulty might be a bagging using random sampling with replacement. However, sampling with replacement might increase the standard error of estimation as the sample size becomes small because of duplicated sampling [37]. To avoid this difficulty, we use subbagging [28], which is modified bagging using random sampling without replacement.

Consequently, SubbKB includes the following four steps: (1) Sample $T$ datasets $\left\{D_{t}\right\}_{t=1}^{T}$ without replacement from training data $D$, where $\left|D_{t}\right|=\delta|D|,(0<\delta<1)$; (2) Learn the $K$-best BDeu scoring structures $\left\{G_{t}^{k}\right\}_{k=1}^{K}$, representing the $K$-best equivalence classes for each dataset $D_{t}$; (3) Compute the $T$ class variable posteriors using each dataset

$D_{t}$ and each set of $K$-best structures to model averaging; (4) By averaging the computed $T$ class variable posteriors, the resulting conditional probability of the class variable given the feature variables is estimated as:

$$
P\left(X_{0} \mid \mathbf{x}, D\right) \approx \frac{1}{T} \sum_{t=1}^{T} \sum_{k=1}^{K} \frac{P\left(D_{t} \mid G_{t}^{k}\right)}{\sum_{k^{\prime}=1}^{K} P\left(D_{t} \mid G_{t}^{k^{\prime}}\right)} P\left(X_{0} \mid \mathbf{x}, G_{t}^{k}, D_{t}\right)
$$

The following theorem about SubbKB can be proved.
Theorem 1. The SubbKB asymptotically estimates the true conditional probability of the class variable given the feature variables.

Proof. From the asymptotic consistency of BDeu [38], the highest BDeu scoring structure converges asymptotically to the I-map with the fewest parameters denoted by $G^{*}$. Moreover, the ratio $P\left(D_{t} \mid G^{*}\right) / \sum_{k=1}^{K} P\left(D_{t} \mid G_{t}^{k}\right)$ asymptotically approaches 1.0. Therefore, Equation (1) converges asymptotically to

$$
\frac{1}{T} \sum_{t=1}^{T} P\left(X_{0} \mid \mathbf{x}, G^{*}, D_{t}\right)
$$

It is guaranteed that $P\left(X_{0} \mid \mathbf{x}, G^{*}, D_{t}\right)$ converges asymptotically to the true conditional probability of the class variable given the feature variables denoted by $P^{*}\left(X_{0} \mid \mathbf{x}\right)$. Consequently, formula (2) converges asymptotically to $P^{*}\left(X_{0} \mid \mathbf{x}\right)$, i.e., SubbKB asymptotically estimates $P^{*}\left(X_{0} \mid \mathbf{x}\right)$.

The SubbKB is expected to provide the following benefits: (1) From Theorem 1, SubbKB asymptotically estimates the true conditional probability of the class variable given the feature variables; (2) For small data, subbagging reduces the posterior standard error of each structure learned using the $K$-best EC method and improves the classification accuracy. The next section explains experiments conducted to compare the respective classification performances of SubbKB and earlier methods.

# 5. Experiments 

This section presents experiments comparing SubbKB and other existing methods.

### 5.1. Comparison of the SubbKB and Other Learning BNC Methods

First, we compare the classification accuracy of the following 14 methods:

- NB: Naive Bayes;
- TAN [10]: Tree-augmented naive Bayes;
- aCLL-TAN [12]: Exact learning TAN method by maximizing aCLL;
- EBN: Exact learning Bayesian network method by maximizing BDeu;
- EANB: Exact learning ANB method by maximizing BDeu;
- $b A N_{\text {mix }}$ [29]: Ensemble method using adaboost, which starts with naive Bayes and greedily augments the current structure at iteration $j$ with the $j$-th edge having the highest conditional mutual information;
- Adaboost(EBN): Ensemble method of 10 structures learned using adaboost to $E B N$;
- B-RAI [31]: Model averaging method over 100 structures sampled using B-RAI with $s=3$;
- Bagging(EBN): Ensemble method of 10 structures learned using bagging to $E B N$;
- Bagging(EANB): Ensemble method of 10 structures learned using bagging to EANB;
- KB10 [20]: K-best EC method using the BDeu score with $K=10$;
- KB10(EANB): K-best EC method under ANB constraints using the BDeu score with $K=10$;
- KB20 [20]: K-best EC method using the BDeu score with $K=20$;
- KB50 [20]: K-best EC method using the BDeu score with $K=50$;

- KB100 [20]: K-best EC method using the BDeu score with $K=100$;
- SubbKB10: SubbKB with $K=10$ and $T=10$;
- SubbKB10(MDL): the modified SubbKB10 to use MDL score.

Here, the classification accuracy represents the average percentage correct among all classifications from ten-fold cross validation. Although determination of hyperparameter $\alpha$ of BDeu is difficult, we used $\alpha=1.0$, which allows the data to reflect the estimated parameters to the greatest degree possible [5,6,34,35]. Note that $\alpha=1.0$ is not guaranteed to provide optimal classification. We also used EAP estimators with $\alpha_{i j k}=1 /\left(r_{i} q_{i}\right)$ as conditional probability parameters of the respective classifiers. Using SubbKB10, Bagging(EBN), and $\operatorname{Bagging}(E A N B)$, the size of the sampled data is $90 \%$ of the training data. Our experiments were conducted entirely using a computational environment, as shown in Table 1. We used 26 classification benchmark datasets from the UCI repository, as shown in Table 2. Continuous variables were discretized into two bins using the median value as cut-off. Furthermore, data with missing values were removed from the datasets. Table 2 also presents the entropy of the class variable, $H\left(X_{0}\right)$, for each dataset. For the discussion presented in this section, we define small datasets as datasets with less than 1000 sample size. In addition, we define large datasets as datasets with 1000 and more sample size. Throughout our experiments, we employ the ten-fold cross validation to evaluate methods.

Table 1. Computational environment.


Table 2. Datasets for the experiments.


Table 3 presents the classification accuracies of each method. The values shown in bold in Table 3 represent the best classification accuracies for each dataset. Moreover, we highlight the results obtained by the SubbKB10 using a blue color. To confirm significance of the differences that arise when using SubbKB10 and other methods, we applied the Hommel test [39], which is a non-parametric post hoc test used as a standard in machine learning studies [40]. Table 4 presents the $p$-values obtained using Hommel tests. From Table 3, results show that, among the methods explained above, the SubbKB10 yields the best average accuracy. Moreover, from Table 4, SubbKB10 outperforms all the model selection methods at the $p<0.10$ significance level. Particularly $N B, T A N$, and $a C L L-T A N$ provide lower classification accuracy than the SubbKB10 does for the No. 1, No. 20, and No. 24 datasets. The reason is that those methods have a small upper bound of maximum number of parents. Such a small upper bound is known to cause poor representational power of the structure [41]. The classification accuracy of $E B N$ is the same as, or almost identical to, that of SubbKB10 for large datasets such as No. 20, No. 23, No. 25, and No. 26 datasets because both methods have asymptotic consistency. However, the classification accuracy of SubbKB10 is equal to or greater than that of $E B N$ for small datasets from No. 1 to No. 15. As described previously, the classification accuracy of $E B N$ is worse than that of the model averaging methods because the error of learning structure by $E B N$ becomes large as the sample size becomes small.

For almost small datasets such as datasets from No. 6 to No. 9 and from No. 11 to No. 13, SubbKB10 provides higher classification accuracy than EANB does because the error of learning ANB structures becomes large. However, for the No. 4 and No. 5 datasets, the classification accuracy of $E A N B$ is much higher than that obtained using SubbKB10. To analyze this phenomenon, we investigate the average number of the class variable's parents in the structures learned by $E B N$ and that by SubbKB10. The results displayed in Table 5 highlight that the average number of the class variable's parents in the structures learned by $E B N$ and that by SubbKB10 tends to be large in the No. 4 and No. 5 datasets. Consequently, estimation of the conditional probability parameters of the class variable becomes unstable because the number of parent configurations becomes large. Then the sample size for learning a parameter becomes sparse. Actually, the ANB constraint prevents numerous parents of the class variable. Moreover, it improves the classification accuracy.

The SubbKB10 outperforms $b A N_{\text {mix }}$, Adaboost(EBN), B-RAI, Bagging(EBN), KB10, KB20, and $K B 50$ at the $p<0.10$ significance level. Actually, $b A N_{\text {mix }}$ provides much lower accuracy than SubbKB10 does for the No. 1, No. 20, and No. 24 datasets because it has a small upper bound of a maximum number of parents, similar to $N B, T A N$, and $a C L L-T A N$. For almost all large datasets, the classification accuracy of SubbKB10 is higher than that of B-RAI because SubbKB10 has an asymptotic consistency, whereas B-RAI does not. The SubbKB10 provides higher classification accuracy than Adaboost $(E B N)$ does for small datasets, such as No. 5 and No. 10 datasets, because Adaboost $(E B N)$ tends to cause overfitting, as described in section 3. The classification accuracy of Bagging $(E B N)$ is much worse than that of SubbKB10 in the No. 5 dataset because the error of learning structures using each sampled data becomes large as the sample size becomes small. The SubbKB10 alleviates this difficulty somewhat using model averaging for sampled data.

The $K$-best EC method using the BDeu score provides higher average classification accuracy as $K$ increases, as shown by $E B N, K B 10, K B 20, K B 50$, and $K B 100$. Although the difference between SubbKB10 and KB100 is not statistically significant, SubbKB10 provides higher average classification accuracy than KB100 does. Moreover, we compare the classification accuracy of SubbKB10 and the K-best EC methods using 1/100-sized subsamples from MAGICGT (No. 26 of datasets) to confirm the robustness of SubbKB10. The results presented in Table 6 show that SubbKB10 provides higher classification accuracy than the other $K$-best EC methods do.

Table 3. Classification accuracies of each BNC.


Table 4. The $p$-values of each BNC.


Table 5. Average numbers of the class variable's parents in the structures of the $E B N$ and those of the SubbKB10.


Table 6. Classification accuracies of $K$-best EC methods and SubbKB10 for 1/100-sized subsamples from MAGICGT.


Although EANB provides higher average classification accuracy than EBN does, Bagging(EBN) and KB10 provides higher average accuracy than Bagging(EANB) and KB10(EANB) do, respectively. These results imply that the ANB constraint might not work effectively in model averaging because it decreases the diversity of the models; all the ANB structures necessarily have the edges between the class variable and all the feature variables. To confirm the diversity of ANB structures in model averaging, we compare the structural hamming distance (SHD) [42] of structures in each model averaging method. Table 7 presents the average SHDs between all two structures in each model averaging method. Results show that the average SHDs of Bagging(EBN) and KB10 are higher than those of Bagging(EANB) and KB10(EANB). That is, model averaging with ANB constraint has less diverse structures than that without ANB constraint does. Moreover, SubbKB10 provides the highest average SHD among all the compared methods because the combination of $K$-best method and subbagging diversifies structures in the model averaging. SubbKB10 provides higher average classification accuracy than SubbKB10(MDL) does. However, the

difference between both methods is not statistically significant because the MDL score asymptotically converges to minus $\log$ BDeu score.

SubbKB10 provides the highest accuracy among all the methods for the No. 22 dataset, which has the most entropy for the class variable among all the datasets. From Theorem 1, SubbKB10 asymptotically estimates the true conditional probability of the class variable given the feature variables. Therefore, SubbKB10 guarantees to provide high classification accuracy when the sample size is sufficiently large regardless of the distribution of the dataset.

Table 7. Average SHDs of model averaging BNCs.


Next, to demonstrate the advantages of using SubbKB10 for small data, we compare the posterior standard error of the structures learned using SubbKB10 with that learned by KB100. We estimate the posterior standard error of structures learned by the KB100 as explained below.

1. Generate 10 random structures $\left\{G_{m}\right\}_{m=1}^{10}$;
2. Sample 10 datasets, $\left\{\widetilde{D}_{i}\right\}_{i=1}^{10}$, with replacement from the training dataset $D$, where $\left|\widetilde{D}_{i}\right|=|D|$
3. Compute the posteriors $P\left(G_{m} \mid \widetilde{D}_{i}\right) \approx P\left(\widetilde{D}_{i} \mid G_{m}\right) / \sum_{m^{\prime}=1}^{10} P\left(\widetilde{D}_{i} \mid G_{m^{\prime}}\right),(m=$ $1, \cdots, 10 ; i=1, \cdots, 10)$
4. Estimate the standard error of the posteriors $P\left(G_{m} \mid D\right),(m=1, \cdots, 10)$ as:

$$
\sqrt{\frac{1}{10(10-1)} \sum_{i=1}^{10}\left\{P\left(G_{m} \mid \widetilde{D}_{i}\right)-\frac{1}{10} \sum_{j=1}^{10} P\left(G_{m} \mid \widetilde{D}_{j}\right)\right\}^{2}}
$$

We estimate the posterior standard error of structures learned using SubbKB10 as presented below.

1. Generate 10 random structures $\left\{G_{m}\right\}_{m=1}^{10}$;
2. Sample 10 datasets, $\left\{\widetilde{D}_{t i}\right\}_{i=1}^{10}$, with replacement from each bootstrapped dataset $D_{t}$, where $\left|\widetilde{D}_{t i}\right|=\left|D_{t}\right|$;

3. Compute the posteriors $P\left(G_{m} \mid \widetilde{D}_{i}\right) \approx \frac{1}{T} \sum_{t=1}^{T}\left[P\left(\widetilde{D}_{i t} \mid G_{m}\right) / \sum_{m^{\prime}=1}^{10} P\left(\widetilde{D}_{i t} \mid G_{m^{\prime}}\right)\right],(m=$ $1, \cdots, 10 ; i=1, \cdots, 10)$;
4. Estimate the standard error of each of the posteriors $P\left(G_{m} \mid D\right),(m=1, \cdots, 10)$ using formula (3).
Average posterior standard errors over 10 structures $\left\{G_{m}\right\}_{m=1}^{10}$ of the SubbKB10 and those of the KB100 are presented in "APSES" of Table 8. Significance can be assessed from values obtained using the Wilcoxon signed-rank test. The $p$-values of the test are presented at the bottom of Table 8. Moreover, Table 8 presents the classification accuracies of the KB100 and the SubbKB10. The results demonstrate that the APSES of SubbKB10 is significantly lower than that of the KB100. Moreover, we investigate the relation between the APSES and the training data sample size. The APSES values of SubbKB10 and KB100 for the sample size are plotted in Figure 2. As presented in Figure 2, the APSESs of KB100 are large for small sample size. As the sample size becomes large, the APSES of KB100 becomes small and closes to that of SubbKB10. On the other hand, the APSESs of SubbKB10 are constantly small independently of the sample size. As presented particularly in Table 8, SubbKB10 provides higher classification accuracy than KB100 does when the APSES of SubbKB10 is lower than that of the KB100, such as that of No. 2, No. 6, and No. 9 datasets. Consequently, SubbKB10 reduces the posterior standard error of the structures. It therefore improves the classification accuracy.

Table 8. (1) Average posterior standard errors of structures (APSES) of the KB100 and those of the SubbKB10 and (2) classification accuracies of KB100 and the SubbKB10.

small | 5800 | 10 | 0.0600 | 0.0600 | 0.9693 | 0.9693  |

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Average posterior standard errors of structures (APSES) of the *KB100* and those of *SubbKB10*.

### 5.2. Comparison of SubbKB10 and State-of-the-Art Ensemble Methods

This subsection presents a comparison of the classification accuracies of SubbKB10 with *K* = 10, *T* = 10 and state-of-the-art ensemble methods, i.e., XGBoost [23], CatBoost [43], and LightGBM [44]. Experimental setup and evaluation methods are the same as those of the previous subsection. We determine the ESS α ∈ {1, 4, 16, 64, 256, 1024} in *SubbKB10* using ten-fold cross validation to obtain the highest classification accuracy. The six ESS values of α are determined according to Heckerman et al. [2]. To assess the significance of differences of *SubbKB10* from the other ensemble methods, we applied multiple Hommel tests [39]. Table 9 presents the classification accuracy and *p*-values obtained using Hommel tests. Results show that the differences between *SubbKB10* and any other ensemble methods are not statistically significant at the *p* < 0.10 level. However, *SubbKB10* provides higher average accuracy than XGBoost, CatBoost, and LightGBM do. CatBoost and LightGBM provides much worse accuracies than the other methods do for the No. 3 and No. 2 datasets, respectively. On the other hand, *SubbKB10* avoids to provide much worse accuracy than the other methods for small data because subbagging in *SubbKB10* improves the accuracy for small data, as previously demonstrated. Moreover, *SubbKB10* provides much higher accuracy than the other methods even for large data, the No. 24 dataset. The reason is that *SubbKB10* asymptotically estimates the true conditional probability of the class variable given the feature variables from Theorem 1. This property is also highly useful for developing AI systems based on decision theory because such systems require accurate probability estimations to calculate expected utility and loss [45,46].

Table 9. Classification accuracies of XGBoost, CatBoost, LightGBM, and SubbKB10.


# 6. Conclusions

This paper described our proposed subbagging of $K$-best EC to reduce the posterior standard error of each structure in model averaging. The class variable posterior of SubbKB converges to the true value when the sample size becomes sufficiently large because SubbKB has asymptotic consistency for true class variable classification. In addition, even for small data, SubbKB reduces the posterior standard error of each structure in the $K$-best structures and thereby improves the classification accuracy. Our experiments demonstrated that SubbKB provided more accurate classification than the $K$-best EC method and the other state-of-the-art ensemble methods did.

The SubbKB cannot learn large size of networks because of its large computational cost. We plan on exploring the following in future work:

- Steck and Jaakkola [47] proposed a conditional independence test with an asymptotic consistency, a Bayes factor with BDeu; Moreover, Abellán et al. [48], Natori et al. [49,50] proposed constraint-based learning methods using a Bayes factor, which can learn large size of networks. We will apply the constraint-based learning methods using a Bayes factor to SubbKB so as to handle much larger number of variables in our method;
- Liao et al. [25] proposed a novel approach to model averaging Bayesian networks using a Bayes factor. Their approach is significantly more efficient and scales to much larger Bayesian networks than existing approaches. We expect to employ their method to address much larger number of variables in our method.
- Isozaki et al. [51,52], Isozaki and Ueno [53] proposed an effective learning Bayesian network method by adjusting the hyperparameter for small data. We expect to employ their method instead of the BDeu to improve the classification accuracy for small data.

Author Contributions: Conceptualization, methodology, I.A. and M.U.; validation, S.S., I.A. and M.U.; writing-original draft preparation, S.S.; writing-review and editing, M.U.; funding acquisition, M.U. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by JSPS KAKENHI Grant Numbers JP19H05663 and JP19K21751.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Acknowledgments: Parts of this research were reported in an earlier conference paper published by Sugahara et al. [54]. One major change is the addition of a theorem that proves that the class variable posterior of the proposed method converges to the true value when the sample size is sufficiently large. A second major revision is the addition of experiments comparing the proposed method with state-of-the-art ensemble methods. A third major improvement is the addition of detailed discussions and analysis for the diversity of structures in each model averaging method. We demonstrated that model averaging with ANB constraint has less diverse structures than that without ANB constraint does.

Conflicts of Interest: The authors declare that they have no conflict of interest. The funders had no role in the design of the study, in the collection, analyses, or interpretation of data, in the writing of the manuscript, or in the decision to publish the results.

# Abbreviations 

The following abbreviations are used in this manuscript:
DAG directed acyclic graph
ML marginal likelihood
BDeu Bayesian Dirichlet equivalence uniform
ESS equivalent sample size
BNC Bayesian network classifier
CLL conditional log likelihood
ANB augmented naive Bayes classifier
aCLL approximated conditional log likelihood
SubbKB Subbagging K-best
