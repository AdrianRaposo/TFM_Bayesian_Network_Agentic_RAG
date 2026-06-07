# Article 

## Computation of Kullback-Leibler Divergence in Bayesian Networks

Serafín Moral (1), Andrés Cano (2) and Manuel Gómez-Olmedo * *<br>check for updates<br>Citation: Moral, S.; Cano, A.; Gómez-Olmedo, M. Computation of Kullback-Leibler Divergence in Bayesian Networks. Entropy 2021, 23, 1122. https://doi.org/10.3390/ e23091122<br>Academic Editor: Raúl Alcaraz<br>Received: 29 July 2021<br>Accepted: 25 August 2021<br>Published: 28 August 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (1)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Computer Science and Artificial Intelligent Department, University of Granada, 18071 Granada, Spain; smc@decsai.ugr.es (S.M.); acu@decsai.ugr.es (A.C.)

* Correspondence: mgomez@decsai.ugr.es


#### Abstract

Kullback-Leibler divergence $K L(p, q)$ is the standard measure of error when we have a true probability distribution $p$ which is approximate with probability distribution $q$. Its efficient computation is essential in many tasks, as in approximate computation or as a measure of error when learning a probability. In high dimensional probabilities, as the ones associated with Bayesian networks, a direct computation can be unfeasible. This paper considers the case of efficiently computing the Kullback-Leibler divergence of two probability distributions, each one of them coming from a different Bayesian network, which might have different structures. The paper is based on an auxiliary deletion algorithm to compute the necessary marginal distributions, but using a cache of operations with potentials in order to reuse past computations whenever they are necessary. The algorithms are tested with Bayesian networks from the bnlearn repository. Computer code in Python is provided taking as basis pgmpy, a library for working with probabilistic graphical models.


Keywords: probabilistic graphical models; learning algorithms; Kullback-Leibler divergence

## 1. Introduction

When experimentally testing Bayesian network learning algorithms, in most of the cases, the performance is evaluated looking at structural differences between the graphs of the original Bayesian network and the learned one [1], as in the case of using the structural Hamming distance. This measure is used in recent contributions as [2-4]. A study and comparison of the different metrics used to measure the structural differences between two Bayesian networks can be found in [1].

However, in most cases the aim of learning a Bayesian network is to estimate a joint probability for the variables in the problem. In that situation the error of a learning procedure should be computed by measuring the difference between the probability associated with the learned network and the original joint probability distribution. Therefore, it can be useful to estimate a network that is less dense than the original one, but in which parameters can have a more accurate estimation. This is the case of the Naive Bayes classifier, which obtains very good results in classification problems, despite the fact that the structure is not the correct one. So, in this situation, structural graphical differences are not a good measure of performance.

The basic measure to determine the divergence between an estimated distribution and a true one is the so-called Kullback-Leibler divergence [5]. Some papers use this way of asserting the quality of a learning procedure as in [6-8]. A direct computation of the divergence is unfeasible if the number of variables is high. However, some basic decomposition properties [9] (Theorem 8.5) can be applied to reduce the cost of computation of the divergence. This is the basis of the procedure implemented in the Elvira system [10] which is the one used in [6]. Methods in $[7,8]$ are also based on the same basic decomposition. Kullback-Leibler divergence is not only meaningful for measuring divergence between a learned network and a true one, but also for other tasks, as for example the approximation of a Bayesian network by a simpler one [11-13] by removing some of the existing links.

The aim of this work is to improve existing methods for computing Kullback-Leibler divergence in Bayesian networks and to provide a basic algorithm for this task using Python and integrated into the pgmpy [14] environment. The algorithm implemented in the Elvira system [10] is based on carrying out a number of propagation computations in the original true network. The hypothesis underlying our approach is that there are a lot of computations that are repeated in these propagation algorithms, so what it is done is to determine which are the operations with potentials that are repeated and then storing the results in a cache of operations in order to allow reuse them. The experimental work will show that this is an effective method to improve the efficiency of algorithms, especially in large networks.

The paper is organized as follows: Section 2 is devoted to set the basic framework and to present fundamental results for the Kullback-Leibler divergence computation; Section 3 describes the method implemented in the Elvira system for computing Kullback-Leibler divergence; Section 4 is devoted to describing our proposal based on the cache of operations with potentials; Section 5 contains the experimental setting and the obtained results; finally the conclusions are shown in Section 6.

# 2. Kullback-Leibler Divergence 

Let $N$ be a Bayesian network defined on a set of variables $\mathbf{X}=\left\{X_{1} \ldots X_{n}\right\}$. The family of a variable $X_{i}$ in $\mathbf{X}$ is termed $f\left(X_{i}\right)=\left\{X_{i}\right\} \cup p a\left(X_{i}\right)$, where $p a\left(X_{i}\right)$ is the set of parents of $X_{i}$ in the directed acyclic graph (DAG) defined by $N . \mathbf{F}=\left\{f\left(X_{1}\right) \ldots f\left(X_{n}\right)\right\}$ denotes the complete set of families, one for each one of the variables. Sometimes simplified notations for families and parent sets will be used: $f_{i}$ (for $f\left(X_{i}\right)$ ) and $p a_{i}$ (for $p a\left(X_{i}\right)$ ), respectively. As a running example, assume a network with three variables, $X_{1}, X_{2}, X_{3}$ and the following structure: $X_{1} \rightarrow X_{2} \rightarrow X_{3}$ (see right part of Figure 1). Then the set of families for this network is given by $\left\{f_{1}, f_{2}, f_{3}\right\}$, where $f_{1}=\left\{X_{1}\right\}, f_{2}=\left\{X_{2}, X_{1}\right\}, f_{3}=\left\{X_{3}, X_{2}\right\}$.

$$
\begin{aligned}
& \overbrace{f^{A}\left(X_{1}\right)=\left\{X_{1}\right\}}^{N^{A}} \\
& f^{A}\left(X_{2}\right)=\left\{X_{1}, X_{2}\right\} \\
& f^{A}\left(X_{3}\right)=\left\{X_{1}, X_{3}\right\} \\
& f^{A}\left(X_{3}\right)=\left\{X_{2}, X_{3}\right\}
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian networks to compare.
A configuration or assignment of values to a set of variables $\mathbf{X},\left\{X_{1}=x_{1} \ldots X_{n}=x_{n}\right\}$, can be abbreviated with $\left(x_{1} \ldots x_{n}\right)$ and is denoted as $\mathbf{x}$. If the set of possible values for each variable in the previous example is $\{0,1\}$, then a configuration can be $\mathbf{x}=(0,0,1)$, representing the assignment $\left\{X_{1}=0, X_{2}=0, X_{3}=1\right\}$.

A partial configuration involving a subset of variables $\mathbf{Y} \subseteq \mathbf{X}$ is denoted as $\mathbf{y}$. If the set of variables is $f_{i}$ or $p a_{i}$, then the partial configuration will be denoted by $\mathbf{x}_{f_{i}}$ or $\mathbf{x}_{p a_{i}}$, respectively. In our example, if $f_{2}=\left\{X_{2}, X_{1}\right\}$ an example of partial configuration about these variables will be $\mathbf{x}_{f_{2}}=(0,0)$.

The set of configurations for variables $\mathbf{Y}$ is denoted by $\Omega_{\mathbf{Y}}$. If $\mathbf{x}$ is an assignment and $\mathbf{Y} \subseteq \mathbf{X}$, then the configuration $\mathbf{y}$ obtained by deleting the values of the variables in $\mathbf{X} \backslash \mathbf{Y}$ is denoted by $\mathbf{x}^{\cup \mathbf{Y}}$. If $\mathbf{x}_{f_{2}}=(0,0)$ is a partial configuration about variables $\left\{X_{2}, X_{1}\right\}$ and we consider $\mathbf{Y}=\left\{X_{2}\right\}$, then $\mathbf{x}_{f_{2}}^{\cup \mathbf{Y}}$ is the configuration obtained by removing the value of $X_{1}$, i.e., $(0)$.

If $\mathbf{w}$ and $\mathbf{z}$ are configurations for $\mathbf{W} \subseteq \mathbf{X}$ and $\mathbf{Z} \subseteq \mathbf{X}$ respectively, and $\mathbf{W} \cap \mathbf{Z}=\varnothing$, then $(\mathbf{w}, \mathbf{z})$ is a configuration for $\mathbf{W} \cup \mathbf{Z}$, and will be called the composition of $\mathbf{w}$ and $\mathbf{z}$. For example, if $\mathbf{w}$ is the configuration $(0)$ about variable $X_{1}$ and $\mathbf{y}$ is the configuration

$(0,1)$ defined on $X_{2}, X_{3}$, then its composition will be the configuration $(0,0,1)$ for variables $\left\{X_{1}, X_{2}, X_{3}\right\}$.

The conditional probability distribution for $X_{i}$ given its parents will be denoted as $\phi_{i}$ which is a potential defined on the set of variables $f\left(X_{i}\right)$. In general, a potential $\phi$ for variables $\mathbf{Y} \subseteq \mathbf{X}$ is a mapping defined on $\Omega_{\mathbf{Y}}$ into the set of real numbers: $\phi: \Omega_{\mathbf{Y}} \rightarrow \mathbb{R}$. The set of variables of potential $\phi$ will be denoted as $v(\phi)$. If $\boldsymbol{\Phi}$ is a set of potentials, $v(\boldsymbol{\Phi})$ will denote $\bigcup_{\phi \in \boldsymbol{\Phi}} v(\phi)$.

In our example, there are three potentials and $\boldsymbol{\Phi}=\left\{\phi_{1}\left(X_{1}\right), \phi_{2}\left(X_{2}, X_{1}\right), \phi_{3}\left(X_{3}, X_{2}\right)\right\}$ (that is, a probability distribution about $X_{1}$, and two conditional probability distributions: one for $X_{2}$ given $X_{1}$ and the other for $X_{3}$ given $X_{2}$, respectively).

There are three basic operations that can be performed on potentials:

- Multiplication. If $\phi, \phi^{\prime}$ are potentials, then their multiplication is the potential $\phi \cdot \phi^{\prime}$, with set of variables $v\left(\phi \cdot \phi^{\prime}\right)=v(\phi) \cup v\left(\phi^{\prime}\right)$ and obtained by pointwise multiplication:

$$
\phi \cdot \phi^{\prime}(\mathbf{y})=\phi\left(\mathbf{y}^{\downarrow v(\phi)}\right) \cdot \phi^{\prime}\left(\mathbf{y}^{\downarrow v\left(\phi^{\prime}\right)}\right)
$$

In our example, the combination of $\phi_{2}$ and $\phi_{3}$ will be the potential $\phi_{2} \cdot \phi_{3}$ defined on $\left\{X_{1}, X_{2}, X_{3}\right\}$ and given by $\phi_{2} \cdot \phi_{3}\left(x_{1}, x_{2}, x_{3}\right)=\phi_{2}\left(x_{2}, x_{1}\right) \cdot \phi_{3}\left(x_{3}, x_{2}\right)$.

- Marginalization. If $\phi$ is a potential defined for variables $\mathbf{Y}$ and $\mathbf{Z} \subseteq \mathbf{Y}$, then the marginalization of $\phi$ on $\mathbf{Z}$ is denoted by $\phi^{\downarrow \mathbf{Z}}$ and it is obtained by summing in the variables in $\mathbf{Y} \backslash \mathbf{Z}$ :

$$
\phi^{\downarrow \mathbf{Z}}(\mathbf{z})=\sum_{\mathbf{y}^{\downarrow \mathbf{Z}}=\mathbf{z}} \phi(\mathbf{y})
$$

When $\mathbf{Z}$ is equal to $\mathbf{Y}$ minus a variable $W$, then $\phi^{\downarrow \mathbf{Z}}$ will be called the result of removing $W$ in $\phi$ and also denoted as $\phi^{-W}$. In the example, a marginalization of $\phi_{3}$ is obtained by removing $X_{3}$ producing $\phi_{3}^{-X_{3}}$ defined on $X_{2}$ and given by $\phi_{3}^{-X_{3}}\left(x_{2}\right)=\phi_{3}\left(0, x_{2}\right)+$ $\phi_{3}\left(1, x_{2}\right)$. If $\phi_{3}\left(x_{3}, x_{2}\right)$ represents the conditional probability of $X_{3}=x_{3}$ given $X_{2}=x_{2}$, then it can be obtained that $\phi_{3}^{-X_{3}}\left(x_{2}\right)$ is always equal to $1\left(\forall x_{2} \in v\left(\phi_{3}\right)\right)$.

- Selection. If $\phi$ is a potential defined for variables $\mathbf{Y}$ and $\mathbf{z}$ is a configuration for variables $\mathbf{Z}$, then the selection of $\phi$ for this configuration $\mathbf{z}$ is the potential $\phi_{\mathbf{Z}=\mathbf{z}}$ defined on variables $\mathbf{W}=\mathbf{Y} \backslash \mathbf{Z}$ and given by

$$
\phi_{\mathbf{Z}=\mathbf{z}}(\mathbf{w})=\phi\left(\mathbf{w}, \mathbf{z}^{\downarrow \mathbf{Y}}\right)
$$

In this expression $\left(\mathbf{w}, \mathbf{z}^{\downarrow \mathbf{Y}}\right)$ is the composition of configurations $\mathbf{w}$ and $\mathbf{z}^{\downarrow \mathbf{Y}}$ which is a configuration for variables $v(\phi)$. Going back to the example, assume that we want to perform the selection of $\phi_{3}$ to configuration $\mathbf{z}=(0,1)$ for variables $\left\{X_{1}, X_{2}\right\}$, then $\phi_{3 \mathbf{Z}=\mathbf{z}}$ will be a potential defined for variables $\left\{X_{2}, X_{3}\right\} \backslash\left\{X_{1}, X_{2}\right\}=\left\{X_{3}\right\}$ given by $\phi_{3 \mathbf{Z}=\mathbf{z}}\left(x_{3}\right)=\phi_{3}\left(x_{3}, 1\right)$, as we are reducing $\phi_{3}\left(X_{3}, X_{2}\right)$ to a configuration $\mathbf{z}$ in which $X_{2}=1$.
The family of all the conditional distributions is denoted as $\boldsymbol{\Phi}=\left\{\phi_{1}, \ldots, \phi_{n}\right\}$. It is well known that given $N$ the joint probability distribution of the variables in $N, p$, is a potential that decomposes as the product of the potentials included in $\boldsymbol{\Phi}$ :

$$
p=\prod_{\phi_{i} \in \boldsymbol{\Phi}} \phi_{i}
$$

Considering the example, $\boldsymbol{\Phi}=\left\{\phi_{1}, \phi_{2}, \phi_{3}\right\}$ and $p=\phi_{1} \cdot \phi_{2} \cdot \phi_{3}$. The marginal distribution of $p$ for a set of variables $\mathbf{Y} \subseteq \mathbf{X}$ is equal to $p^{\downarrow \mathbf{Y}}$. When $\mathbf{Y}$ contains only one variable $X_{i}$, then to simplify the notation, $p^{\downarrow \mathbf{Y}}$ will be denoted as $p_{i}$. Sometimes it will be needed to make reference to the Bayesian network containing a potential or family. In these cases we will use a superscript. For example, $f^{A}\left(X_{i}\right)$ and $p a^{A}\left(X_{i}\right)$ refer to the family and parents set of $X_{i}$ in a Bayesian network $N^{A}$ respectively.

The aim of this paper is to compute the Kullback-Leibler divergence (termed $K L$ ) between the joint probability distributions, $p^{A}$ and $p^{B}$, of two different Bayesian networks $N^{A}$ and $N^{B}$ defined on the same set of variables $\mathbf{X}$ but possibly having different structures. This divergence, denoted as $K L\left(N^{A}, N^{B}\right)$ can be computed considering the probabilities for each configuration $\mathbf{x}$ in both distributions as follows:

$$
K L\left(N^{A}, N^{B}\right)=\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(\frac{p^{A}(\mathbf{x})}{p^{B}(\mathbf{x})}\right)
$$

However, the computation of the joint probability distribution may be unfeasible for complex models as the number of configurations $\mathbf{x}$ is exponential in the number of variables. If $p, q$ are probability distributions on $\mathbf{X}$ then the expected log likelihood ( $L L$ ) of $q$ with respect to $p$ is:

$$
L L(p, q)=\sum_{\mathbf{x}} p(\mathbf{x}) \log (q(\mathbf{x}))
$$

then, from Equation (2) it is immediate that:

$$
\begin{array}{r}
K L\left(N^{A}, N^{B}\right)=\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(p^{A}(\mathbf{x})\right)-\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(p^{B}(\mathbf{x})\right)= \\
L L\left(p^{A}, p^{A}\right)-L L\left(p^{A}, p^{B}\right)=L L\left(N^{A}, N^{A}\right)-L L\left(N^{A}, N^{B}\right)
\end{array}
$$

The probability distribution $p^{B}$ can be decomposed as well as considered in Equation (1). Therefore, the term $L L\left(N^{A}, N^{B}\right)$ in Equation (3) can be obtained as follows considering the families of variables in $N^{B}$ and their corresponding configurations, $\mathbf{x}^{\downarrow f_{i}^{B}}$ :

$$
\begin{array}{r}
L L\left(N^{A}, N^{B}\right)=\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(p^{B}(\mathbf{x})\right)=\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(\prod_{X_{i} \in \mathbf{X}} \phi_{i}^{B}\left(\mathbf{x}^{\downarrow f_{i}^{B}}\right)\right)= \\
\sum_{\mathbf{x}} p^{A}(\mathbf{x}) \sum_{X_{i} \in \mathbf{X}} \log \left(\phi_{i}^{B}\left(\mathbf{x}^{\downarrow f_{i}^{B}}\right)\right)
\end{array}
$$

Interchanging additions and reorganizing the terms in Equation (4):

$$
\begin{array}{r}
L L\left(N^{A}, N^{B}\right)=\sum_{X_{i} \in \mathbf{X}} \sum_{\mathbf{x}} p^{A}(\mathbf{x}) \log \left(\phi_{i}^{B}\left(\mathbf{x}^{\downarrow f_{i}^{B}}\right)\right)= \\
\sum_{X_{i} \in \mathbf{X}} \sum_{\mathbf{x}_{f_{i}^{B}}} \log \left(\phi_{i}^{B}\left(\mathbf{x}_{f_{i}^{B}}\right)\right)\left(\sum_{\mathbf{x}^{\downarrow f_{i}^{B}}=\mathbf{x}_{f_{i}^{B}}} p^{A}(\mathbf{x})\right)= \\
\sum_{X_{i} \in \mathbf{X}} \sum_{\mathbf{x}_{f_{i}^{B}}} \log \left(\phi_{i}^{B}\left(\mathbf{x}_{f_{i}^{B}}\right)\right)\left(p^{A}\right)^{\downarrow f_{i}^{B}}\left(\mathbf{x}_{f_{i}^{B}}\right)
\end{array}
$$

Equation (5) implies a decomposition of the term $L L\left(N^{A}, N^{B}\right)$ and, as a consequence of $K L\left(N^{A}, N^{B}\right)$ computation as well. Observe that $\phi_{i}^{B}\left(\mathbf{x}_{f_{i}^{B}}\right)$ is the value of the potential $\phi_{i}^{B}$ for a configuration $\mathbf{x}_{f_{i}^{B}}$ and can be obtained directly from the potential $\phi_{i}^{B}$ of the Bayesian network $N^{B}$. The main difficulty in Equation (5) consists of the computation of $\left(p^{A}\right)^{\downarrow f_{i}^{B}}\left(\mathbf{x}_{f_{i}^{B}}\right)$ values, as it is necessary to compute the marginal probability distribution for variables in $f_{i}^{B}$, the family of $X_{i}$ in Bayesian network $N^{B}$, but using the joint probability distribution $p^{A}$ associated with the Bayesian network $N^{A}$.

# 3. Computation with Propagation Algorithms 

In this section we introduce the category of inference algorithms based on deletion of variables and then we show how these algorithms can be applied to compute the Kullback-Leibler divergence using Equation (5).

### 3.1. Variable Elimination Algorithms

To compute $\left(p^{A}\right)^{\downarrow f_{i}^{B}}$ we consider $\boldsymbol{\Phi}^{A}$ the set of potentials associated to network $N^{A}$ : the multiplication of all the potentials in $\boldsymbol{\Phi}^{A}$ is equal to $p^{A}$. Deletion algorithms [15,16], can be applied to $\boldsymbol{\Phi}^{A}$ to determine the required marginalizations. The basic step of these algorithms is the deletion of a variable from a set $\boldsymbol{\Phi}^{A}$ :

- Variable Deletion. If $\boldsymbol{\Phi}$ is a set of potentials, the deletion of $X_{i}$ consists of the following operations:
- Compute $\boldsymbol{\Phi}_{i}=\left\{\phi: X_{i} \in v(\phi)\right\}$, i.e., the set of potentials containing variable $X_{i}$.
- Compute $\phi^{-i}=\left(\prod_{\phi \in \boldsymbol{\Phi}_{i}} \phi\right)^{-X_{i}}$, i.e., combine all the potentials in $\boldsymbol{\Phi}_{i}$ and remove variable $X_{i}$ by marginalization.
- Update $\boldsymbol{\Phi} \leftarrow\left(\boldsymbol{\Phi} \backslash \boldsymbol{\Phi}_{i}\right) \cup\left\{\phi^{-i}\right\}$, i.e., remove from $\boldsymbol{\Phi}$ the potentials containing $X_{i}$ and add the new potential $\phi^{-i}$ which does not contain $X_{i}$.
The main property of the deletion step is the following: starting with $\prod_{\phi \in \boldsymbol{\Phi}} \phi=q$, then after the deletion of $X_{i}$ from $\boldsymbol{\Phi}, \prod_{\phi \in \boldsymbol{\Phi}} \phi=q^{-X_{i}}$. It is easy to see that the deletion of a variable $X_{i}$ can be computed just operating with the elements of $\boldsymbol{\Phi}$ defined on $X_{i}$.

If $\boldsymbol{\Phi}$ is the initial set of potentials of a network $N$, then $p=\prod_{\phi \in \boldsymbol{\Phi}} \phi$. In order to compute the marginalization of $p$ on a set of variables $\mathbf{Y} \subseteq \mathbf{X}$, the deletion procedure should be repeated for each variable $X_{i}$ in $\mathbf{X} \backslash \mathbf{Y}$. If the marginal probability distribution for variable $X_{k}$ is to be calculated, any variable in $\mathbf{X}$ different from $X_{k}$ should be deleted. The order of variable deletion is not meaningful for the final result, but the efficiency may depend on it.

When there are observed variables, $\mathbf{Z}=\mathbf{z}$, then a previous step of selection should be carried out: any potential $\phi \in \boldsymbol{\Phi}$ is transformed into $\phi_{\mathbf{Z}=\mathbf{z}}$. This step will be called evidence restriction. After it $q$, the product of the potentials in $\boldsymbol{\Phi}$ is defined for variables in $\mathbf{Y}=\mathbf{X} \backslash \mathbf{Z}$ and its value is $q(\mathbf{y})=p(\mathbf{y}, \mathbf{z})$, i.e., the joint probability of obtaining this value and the observations. If a deletion of variables in $\mathbf{W}$ is carried out, then the product of the potentials in $\boldsymbol{\Phi}$ is the potential defined for variables $\mathbf{Y}=(\mathbf{X} \backslash \mathbf{Z}) \backslash \mathbf{W}$, and satisfies $q(\mathbf{y})=p^{\downarrow \mathbf{Y} \cup \mathbf{Z}}(\mathbf{y}, \mathbf{z})$.

When we have observations and we want to compute the marginal on a variable $X_{i}$, it is well known that not all the initial potentials in $\boldsymbol{\Phi}$ are relevant. A previous pruning step can be done using the Bayes-ball algorithm [17] in order to remove the irrelevant potentials from $\boldsymbol{\Phi}$ before restricting to the observations and carrying out the deletion of variables.

### 3.2. Computation of Kullback-Leibler Divergence Using Deletion Algorithms

Our first alternative to compute $L L\left(N^{A}, N^{B}\right)$ is based on using a simple deletion algorithm to compute the values $\left(p^{A}\right)^{\downarrow f_{i}^{B}}\left(\mathbf{x}_{f_{i}^{B}}\right)$ in Equation (5). The basic steps are:

- Given a specific variable $X_{i}$, we have that $f_{i}^{B}=\left\{X_{i}\right\} \cup p a_{i}^{B}$. Then for each possible configuration $\mathbf{x}_{p a_{i}^{B}}$ of the parent variables, we include the observation $p a_{i}^{B}=\mathbf{x}_{p a_{i}^{B}}$ and we apply a selection operation to the list of potentials associated with Bayesian network $N^{A}$ by means of evidence restriction. We also apply a pruning of irrelevant variables using the Bayes-ball algorithm.
- Then all the variables are deleted except the target variable $X_{i}$. The potentials in $\boldsymbol{\Phi}$ will be all defined for variable $X_{i}$ and their product will be a potential $q$ defined for variable $X_{i}$ such that $q\left(x_{i}\right)=\left(p^{A}\right)^{\downarrow f_{i}^{B}}\left(x_{i}, \mathbf{x}_{p a_{i}^{B}}\right)$.
- The deletion algorithm is repeated for each variable $X_{i}$ and each configuration of the parent variables $\mathbf{x}_{p a_{i}^{B}}$ in Bayesian network $N^{B}$. So, the number of executions of the

propagation algorithm in Bayesian network $N^{A}$ is equal to $\sum_{i=1}^{n} \prod_{X_{i} \in p a^{B}\left(X_{i}\right)} n_{j}$, where $n_{j}$ is the number of possible values of $X_{j}$. This is immediate taking into account that $\prod_{X_{j} \in p a^{B}\left(X_{i}\right)} n_{j}$ is the number of possible configurations $\mathbf{x}_{p a^{B}\left(X_{i}\right)}$ of variables in $p a^{B}\left(X_{i}\right)$.
Though this method can take advantage of propagation algorithms to compute marginals in a Bayesian network, and it avoids a brute force computation associated with the use of Equation (2), it is quite time consuming when the structure of the involved Bayesian network is complex.

Algorithm 1 details the basic steps of the initial proposal for computing the KullbackLeibler divergence. This algorithm is the one used in [8,10]. Observe that this algorithm computes $L L\left(N^{A}, N^{B}\right)$. It allows the computation of the $K L$ divergence by using Equation (3).

```
Algorithm 1 Computation of \(L L\) using an evidence propagation algorithm
    function \(\operatorname{LL}\left(N^{A}, N^{B}\right)\)
        sum \(\leftarrow 0.0 \quad \triangleright\) sets initial value to sum
        for each \(X_{i}\) in \(N^{B}\) do
            for each \(\mathbf{x}_{p a_{i}^{B}}\) do \(\triangleright\) configuration of \(X_{i}\) parents
            Let \(\boldsymbol{\Phi}^{\prime}\) the set of relevant potentials from \(\boldsymbol{\Phi} \quad \triangleright\) Applying Bayes-ball
            Restrict the potentials in \(\boldsymbol{\Phi}^{\prime}\) to evidence \(p a_{i}^{B}=\mathbf{x}_{p a_{i}^{B}}\)
            Delete in \(\boldsymbol{\Phi}^{\prime}\) all the variables in \(\mathcal{v}(\boldsymbol{\Phi}) \backslash\left\{X_{i}\right\}\)
            Let \(q\) the product of all the potential in \(\boldsymbol{\Phi}^{\prime}\)
            for each \(x_{i}\) in \(\Omega_{X_{i}}\) do
                sum \(\leftarrow \operatorname{sum}+q\left(x_{i}\right) \log \left(\phi_{i}^{B}\left(x_{i}, \mathbf{x}_{p a_{i}^{B}}\right)\right)\)
            end for
            end for
        end for
        end for
    return sum
end function
```

As an example, let us suppose we wish to compute the $K L$ divergence between two Bayesian networks $N^{A}$ and $N^{B}$ defined on $\mathbf{X}=\left\{X_{1}, X_{2}, X_{3}\right\}$ (see Figure 1). Let us assume $N^{A}$ is the reference model. The families of variables in both models are presented in Figure 1. We have to compute $L L\left(N^{A}, N^{A}\right)$ and $L L\left(N^{A}, N^{B}\right)$. To compute $L L\left(N^{A}, N^{B}\right)$ Algorithm 1 is applied. Initially, $\boldsymbol{\Phi}=\left\{\phi_{1}^{A}, \phi_{2}^{A}, \phi_{3}^{A}\right\}$ where $\phi_{i}^{A}$ is defined for variables $f^{A}\left(X_{i}\right)$. The algorithm works as follows:

- The parent set for $X_{1}$ is empty. The set of relevant potentials in network $N^{A}$ to compute the marginal for $X_{1}$ is given by $\boldsymbol{\Phi}^{\prime}=\left\{\phi_{1}^{A}\right\}$, which is the desired marginal $q$.
- The parents set for $X_{2}$ in $N^{B}$ is $\left\{X_{1}\right\}$. So, for each value $X_{1}=x_{1}$ we have to introduce this evidence in network $N^{A}$ and compute the marginal on $X_{2}$. The set relevant potentials is $\boldsymbol{\Phi}^{\prime}=\left\{\phi_{1}^{A}, \phi_{2}^{A}\right\}$. These potentials are reduced by selection on configuration $X_{1}=x_{1}$. If we call $\phi_{4}, \phi_{5}$ the results of reducing $\phi_{1}^{A}, \phi_{2}^{A}$, respectively, then $\phi_{4}$ is a potential defined for the empty set of variables and determined by its value $\phi_{4}()$ for the empty configuration. $\phi_{5}$ is a potential defined for variable $X_{2}$. The desired marginal $q$ is the multiplication of these potentials: $q\left(x_{2}\right)=\phi_{4}() \cdot \phi_{5}\left(x_{2}\right)$.
- The parents set for $X_{3}$ in $N^{B}$ is $\left\{X_{2}\right\}$. So, for each value $X_{2}=x_{2}$ we have to introduce this evidence in network $N^{A}$ and compute the marginal on $X_{3}$. In this case, all the potentials are relevant $\boldsymbol{\Phi}^{\prime}=\left\{\phi_{1}^{A}, \phi_{2}^{A}, \phi_{3}^{A}\right\}$. The first step introduces the evidence $X_{2}=x_{2}$ in all the potentials containing this variable. Only $\phi_{2}^{A}$ contains $X_{2}$; therefore the selection $\phi_{2}^{A}{ }_{X_{2}=x_{2}}$ is a potential defined on variable $X_{1}$ which we will denote as $\phi_{6}$. So, after that $\boldsymbol{\Phi}^{\prime}=\left\{\phi_{1}^{A},, \phi_{3}^{A}, \phi_{6}\right\}$. To compute the marginal on $X_{3}$, we have to delete variable $X_{1}$. As all the potentials in $\boldsymbol{\Phi}^{\prime}$ contains this variable they must be combined for removing $X_{1}$ afterwards, i.e., computing $\left(\phi_{1}^{A} \cdot \phi_{3}^{A} \cdot \phi_{6}\right)^{-X_{1}}$. After this operation, this will be the only potential in $\boldsymbol{\Phi}^{\prime}$ and it is the desired marginal $q$.

# 4. Inference with Operations Cache 

The approach proposed in this paper is based on the following fact: the computation of $K L$ divergence using Equations (3) and (5) requires us to obtain the following families of marginal distributions:

- $\left(p^{A}\right)^{\downarrow f_{i}^{B}}$, for each $X_{i}$ in $N^{B}$, for computing $L L\left(N^{A}, N^{B}\right)$
- $\left(p^{A}\right)^{\downarrow f_{i}^{A}}$, for each $X_{i}$ in $N^{A}$, for obtaining $L L\left(N^{A}, N^{A}\right)$

We have designed a procedure to compute each one of the required marginals $\left(p^{A}\right)^{\downarrow \mathbf{Y}}$ for each $\mathbf{Y} \in\left\{f_{i}^{A}: X_{i} \in N^{A}\right\} \cup\left\{f_{i}^{B}: X_{i} \in N^{B}\right\}$. Marginals are computed by deleting the variables not in $\mathbf{Y}$. The procedure uses a cache of computations which can be reused in the different marginalizations in order to avoid repeated computations.

We have implemented a general procedure to calculate the marginal for a family $\mathcal{Y}$ of subsets $\mathbf{Y}$ of $\mathbf{X}$ in a Bayesian network $N$. In our case the family $\mathcal{Y}$ is $\left(p^{A}\right)^{\downarrow \mathbf{Y}}$ for each $\mathbf{Y} \in\left\{f_{i}^{A}: X_{i} \in N^{A}\right\} \cup\left\{f_{i}^{B}: X_{i} \in N^{B}\right\}$ and the Bayesian network is $N^{A}$. A previous step consists of determining the relevant potentials for computing the marginal on a subset $\mathbf{Y}$, as not all the initial potentials are necessary. If $\boldsymbol{\Phi}$ is the list of potentials, then a conditional probability potential $\phi_{i}$ for variable $X_{i}$ is relevant for $\mathbf{Y}$ when $X_{i}$ is an ascendant for some of the variables in $\mathbf{Y}$. This is a consequence of known relevance properties in Bayesian networks [17]. Let us call $\boldsymbol{\Phi}_{\mathbf{Y}}$ the family of relevant potentials for subset $\mathbf{Y}$.

Our algorithm assumes that the subsets in $\mathcal{Y}$ are numbered from 1 to $K:\left\{\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{K}\right\}$. The algorithm first carries out the deletion algorithm symbolically, without actually doing numerical computations, in order to determine which of them can be reused. A symbolic combination of $\phi$ and $\phi^{\prime}$ consists of determining a potential $\phi \cdot \phi^{\prime}$ defined for variables $v(\phi) \cup v\left(\phi^{\prime}\right)$ but without computing its numerical values (only the scope of the resulting potential is actually computed). This procedure is analogously done in the case of marginalization.

In fact, two repositories are employed: one for potentials $\left(R_{\Phi}\right)$ and another for operations $\left(R_{O}\right)$. The entry for each potential in $R_{\Phi}$ contains a value acting as its identifier (id); the potential itself; the identifier of the last operation for which this potential was required (this is denoted as potential time). Initially, $R_{\Phi}$ contains the potentials in $\Phi$ assigning time $=0$ to all of them. When a potential is no longer required, then it is removed from $R_{\Phi}$ in order to alleviate memory space requirements. The potentials representing the required marginals (the results of the queries) are set with time $=-1$ in order to avoid their deletion.

The repository $R_{O}$ contains an entry for each operation (combination or marginalization) with potentials performed during the running of the algorithm in order to compute the required marginals. This allows that if an operation is needed in the future, its result can be retrieved from $R_{O}$ preventing repeated computations. Initially $R_{O}$ will be empty. At the end of the analysis, it will include the description of the elementary operations carried out throughout the evaluation of all the queries. Two kinds of operations will be stored in $R_{O}$ :

- combination of two potentials $\phi_{1}$ and $\phi_{2}$ producing a new one as result, $\phi_{r}$.
- marginalization of a potential $\phi_{1}$, in order to sum-out a variable and obtaining $\phi_{r}$ as result.

The operation description will be stored as registers (id, type, $\phi_{1}, \phi_{2}, \phi_{r}$ ) with the following information:

- A unique identifier for the operation (id; an integer).
- The type of operation (type): marginalization or combination.
- Identifiers of the potentials involved as operands and result (identifiers allow to retrieve potentials from $R_{\Phi}$ ). If the operation is a marginalization, then $\phi_{2}$ will identify the index of the variable to remove.
The computation of a marginal for a set $\mathbf{Y}$ will also require a deletion order of variables in some cases. This order is always obtained with a fixed triangulation heuristic min weight [18]. However, the procedure described here does not depend on this heuristic and any one of them could be used.

Algorithm 2 depicts the basic structure of the procedure. The result is $L R$, an ordered list of $K$ potentials containing the required marginals for $\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{K}$. The algorithm is divided into two main parts.

In the first part (lines 2-26), the operations are planned (using symbolic propagation) and detecting repeated operations. It is assumed that there are two basic functions $\operatorname{SCOMBINE}\left(\phi_{1}, \phi_{2}\right)$ and $\operatorname{SMAR} \operatorname{GINALIZE}(\phi, i)$, representing the symbolic operations: $\operatorname{SCOMBINE}\left(\phi_{1}, \phi_{2}\right)$ will create a new potential $\phi_{r}$ with $v\left(\phi_{r}\right)=v\left(\phi_{1}\right) \cup v\left(\phi_{2}\right)$ and $\operatorname{SMAR} \operatorname{GINALIZE}(\phi, i)$ producing another potential $\phi_{r}$ with $v\left(\phi_{r}\right)=v(\phi) \backslash\left\{X_{i}\right\}$.

We will also consider that there are two conditional versions of these operations: if the operation already exists, only the time is updated, and if it does not exist it is symbolically carried out and added to the repository of operations. The conditional combination will be CONDSCOMBINE $\left(\phi_{1}, \phi_{2}, t\right)$ and the conditional marginalization will be CONDSMARGINALIZE $(\phi, i)$ and are depicted in Algorithms 3 and 4, respectively. It is assumed that both repositories are global variables for all the procedures. The potentials representing the required marginals are never deleted. For that, a time equal to -1 is assigned: if time $=-1$, then the potential should not be removed and then this time is never updated. We will assume the function $\operatorname{UPdatETIME}(\phi, t)$ which does nothing if the time of $\phi$ is equal to -1 , and updates the time of $\phi$ to $t$ otherwise in repository $R_{\Phi}$.

Observe that the first part of Algorithm 2 (lines 2-26) just determines the necessary operations for the deletion algorithm for for all the marginals, while the second part (lines 27-32) carries out the numerical computations in the order that was established in the first part. After each operation, the potentials that are no longer necessary are removed from $R_{\Phi}$ and their memory is deallocated. We will assume a function $\operatorname{DELETEIF}(\phi, t)$ doing this (remove from $R_{\Phi}$ if time of $\phi$ is equal to $t$ ).

As mentioned above, the analysis of the operation sequence will be carried out using symbolic operations and taking into account the scopes of potentials but without numerical computations. This allows an efficient analysis. The result of the analysis will be used as an operation planning for the posterior numerical computation.

Assume the same example considered in previous sections for the networks in Figure 1. The marginals to compute on $N^{A}$ (as reference model) will correspond to families $f^{A}\left(X_{1}\right)=\left\{X_{1}\right\}, f^{A}\left(X_{2}\right)=\left\{X_{1}, X_{2}\right\}, f^{A}\left(X_{3}\right)=\left\{X_{1}, X_{3}\right\}$ and $f^{B}\left(X_{3}\right)=\left\{X_{2}, X_{3}\right\}$ (observe that $\left.f^{A}\left(X_{1}\right)=f^{B}\left(X_{1}\right), \quad\right.$ and $\left.f^{A}\left(X_{2}\right)=f^{B}\left(X_{2}\right)\right)$. Therefore, in this case $\mathcal{Y}=\left\{\left\{X_{1}\right\},\left\{X_{1}, X_{2}\right\},\left\{X_{1}, X_{3}\right\},\left\{X_{2}, X_{3}\right\}\right\}$.

Initially, the potentials repository $R_{\Phi}$ contains the potentials of $N^{A}$ (a conditional probability for each variable given its parents): $\phi_{1}^{A}\left(X_{1}\right), \phi_{2}^{A}\left(X_{2}, X_{1}\right)$, and $\phi_{3}^{A}\left(X_{3}, X_{1}\right)$ with time 0 . We indicate the variables involved in each potential. The operations repository, $R_{O}$, will be empty. Table 1 contains the initial repositories. Notice that the superscript $A$ has been omitted in order to simplify the notation.

Table 1. Initial state for $R_{\Phi}$ (left part) and $R_{O}$ (right part).


```
Algorithm 2 Computation of marginals of \(p\) for subsets \(\mathbf{Y} \in \mathcal{Y}\)
    function \(\operatorname{MARGINAL}(N, \mathcal{Y})\)
        \(t \leftarrow 1\)
        for each \(k=1, \ldots, K\) do
            Let \(\mathbf{Y}\) the subset \(\mathbf{Y}_{k}\) in \(\mathcal{Y}\)
            Let \(\boldsymbol{\Phi}_{\mathbf{Y}}\) the family of potentials from \(\boldsymbol{\Phi}\) relevant to subset \(\mathbf{Y}\)
            for \(X_{i} \in v\left(\boldsymbol{\Phi}_{\mathbf{Y}}\right) \backslash \mathbf{Y}\) do \(\triangleright\) determine operations for the query
                Let \(\boldsymbol{\Phi}_{i}=\left\{\phi \in \boldsymbol{\Phi}_{\mathbf{Y}}: X_{i} \in v(\phi)\right\}\)
                Assume \(\boldsymbol{\Phi}_{i}=\left\{\phi_{1}, \ldots, \phi_{L}\right\}\)
                \(\psi=\phi_{1}\)
                for \(l=2, \ldots, L\) do
                    \(\psi \leftarrow \operatorname{CONDSCOMBINE}\left(\psi, \phi_{l}, t\right)\)
                    \(t \leftarrow t+1\)
                end for
                \(\psi \leftarrow \operatorname{CONDSMargINALIZE}(\psi, i, t)\)
                \(t \leftarrow t+1\)
                \(\boldsymbol{\Phi}_{\mathbf{Y}} \leftarrow\left(\boldsymbol{\Phi}_{\mathbf{Y}} \backslash \boldsymbol{\Phi}_{i}\right) \cup\{\psi\}\)
            end for
            Assume \(\boldsymbol{\Phi}_{\mathbf{Y}}=\left\{\phi_{1}, \ldots, \phi_{J}\right\} \quad \triangleright\) compute joint distribution
            \(\psi_{k} \leftarrow \phi_{1}\)
            for \(j=2, \ldots, J\) do
                \(\psi_{k} \leftarrow \operatorname{CONDSCOMBINE}\left(\psi_{k}, \phi_{j}, t\right)\)
                \(t \leftarrow t+1\)
            end for
            Append \(\psi_{k}\) to \(L R\)
            Set time of \(\psi_{k}\) to -1
        end for
        \(T \leftarrow t-1\)
        for each \(t=1, \ldots, T\) do \(\triangleright\) start numerical computation using operations planning
            Select register with time \(t\) from \(R_{\mathrm{O}}:\left(t, \text { type, } \phi_{1}, \phi_{2}, \phi_{r}\right)\)
            Compute numerical values of \(\phi_{r} \quad \triangleright\) Actual computation
            \(\operatorname{DELETEIF}\left(\phi_{1}, t\right), \operatorname{DELETEIF}\left(\phi_{2}, t\right), \operatorname{DELETEIF}\left(\phi_{r}, t\right)\)
        end for
        return \(L R\)
    end function
```

Algorithm 3 Conditional symbolic combination

```
function \(\operatorname{CONDSCOMBINE}\left(\phi_{1}, \phi_{2}, t\right)\)
    if register \(\left(i d, \operatorname{comb}, \phi_{1}, \phi_{2}, \phi_{r}\right)\) is in \(R_{\mathrm{O}}\) then
        \(\operatorname{UpdateTIME}\left(\phi_{1}, t\right), \operatorname{UpdateTIME}\left(\phi_{2}, t\right), \operatorname{UpdateTIME}\left(\phi_{r}, t\right)\)
    else
        \(\phi_{r}=\operatorname{SCOMBINE}\left(\phi_{1}, \phi_{2}\right)\)
        Add register \(\left(i d, \operatorname{comb}, \phi_{1}, \phi_{2}, \phi_{r}\right)\) to \(R_{\mathrm{O}}\) with \(i d\) as identifier
        \(\operatorname{UpdateTIME}\left(\phi_{1}, t\right), \operatorname{UpdateTIME}\left(\phi_{2}, t\right)\)
        Add \(\phi_{r}\) to \(R_{\phi}\) with time \(=t\)
        end if
        return \(\phi_{r}\)
    end function
```

```
Algorithm 4 Conditional symbolic marginalization
    function CONDSMARGINALIZE \((\phi, i, t)\)
        if register \(\left(i d, \operatorname{marg}, \phi, i, \phi_{r}\right)\) is in \(R_{O}\) then
            \(\operatorname{UpdateTime}(\phi, t), \operatorname{UpdateTime}\left(\phi_{r}, t\right)\)
        else
            \(\phi_{r}=\operatorname{SMAR} \operatorname{an} \operatorname{an} \operatorname{al} \operatorname{le}(\phi, i)\)
            Add register \(\left(i d, \operatorname{marg}, \phi, i, \phi_{r}\right)\) to \(R_{O}\) with \(i d\) as identifier
            \(\operatorname{UpdateTime}(\phi, t)\)
            Add \(\phi_{r}\) to \(R_{\phi}\) with \(t\) as time
        end if
        return \(\phi_{r}\)
    end function
```

The first marginal to compute is for $\mathbf{Y}=\left\{X_{1}\right\}$. In this case, the set of relevant potentials is $\boldsymbol{\Phi}_{\mathbf{Y}}=\left\{\phi_{1}\right\}$ and there are not operations to carry out. Therefore the first marginal is $\Psi_{1}=\phi_{1}$ which is appended to $L R$.

The second marginal to be computed is for $\mathbf{Y}=\left\{X_{1}, X_{2}\right\}$. In this case, the relevant potentials are $\boldsymbol{\Phi}_{\mathbf{Y}}=\left\{\phi_{1}, \phi_{2}\right\}$ and there are no variables to remove, but it is necessary to carry out the symbolic combination of $\phi_{1}$ and $\phi_{2}$ in order to compute $\Psi_{2}$ (lines 19-23 of Algorithm 2). If we call $\phi_{4}$ the result, then the repositories after this operation will be as shown in Table 2.

Table 2. Repositories after $k=2$.


The third marginal to compute is for set $\mathbf{Y}=\left\{X_{1}, X_{3}\right\}$. Now, the relevant potentials are $\boldsymbol{\Phi}_{\mathbf{Y}}=\left\{\phi_{1}, \phi_{3}\right\}$. The situation is analogous to the computation of the previous marginal, with the difference that now the symbolic combination to carry out is $\phi_{1} \cdot \phi_{3}$. The repositories status after $k=3$ is shown in Table 3. We have that the third desired marginal is $\psi_{3}=\phi_{5}$.

Table 3. Repositories after $k=3$.


Finally, for $k=4$ we have to compute the marginal for $\mathbf{Y}=\left\{X_{2}, X_{3}\right\}$. The relevant potentials are now $\boldsymbol{\Phi}_{\mathbf{Y}}=\left\{\phi_{1}, \phi_{2}, \phi_{3}\right\}$. Variable $X_{1}$ has to be deleted from this set of potentials. As all the potentials contain this variable, as a first step it is necessary to combine all of them, and afterwards to remove $X_{1}$ by marginalizing on $\left\{X_{2}, X_{3}\right\}$. Assume that the order of the symbolic operations is: first combine $\phi_{1}$ and $\phi_{2}$ and then its result is combined with $\phi_{3}$; then this result is marginalized by removing $X_{1}$. Then the repositories after $k=4$ are as presented in Table 4. The combination of $\phi_{1}$ and $\phi_{2}$ was previously carried out for $k=2$ and therefore its result can be retrieved without new computations.

Table 4. Repositories after $k=4$.


After that, the numerical part of operations in Table 4 are carried out in the same order in which they are described in that table. In this process, after doing an operation with an identifier (id) equal to $t$, the potentials with time equal to $t$ are removed from the $R_{\Phi}$ table. For example, in this case, potentials $\phi_{2}$ and $\phi_{3}$ can be removed from $R_{\Phi}$ after doing operation with $i d=4$ and potential $\phi_{6}$ can be removed after operation with $i d=5$, leaving only in $R_{\Phi}$ the potentials containing the desired marginal potentials needed to compute the $K L$ divergence between both networks (potentials with time $=-1$ ).

# 5. Experiments 

In order to compare the computation approaches presented in the paper the experimentation uses a set of Bayesian networks available in the bnlearn [19] repository (https://www.bnlearn.com/bnrepository/, accessed on 24 August 2021). This library provides all the functions required for the process described below. Given a certain Bayesian network as defined in the repository:

- A dataset is generated using the $r b n$ function. As explained in the library documentation, this function simulates random samples from a Bayesian network, using forward/backward sampling.
- The dataset is used for learning a Bayesian network. For this step, the tabu function is employed using the default setting (a dataset as unique argument). It is one of the structural learning methods available on bnlearn. Since the learned model could have unoriented links, the cextend function is required, which results in a Bayesian network consistent with the model passed as argument. Any other different learning algorithm could have been used, since the goal is to have an alternative Bayesian network that will be used later to calculate the Kullback-Leibler divergence with the methods described in Algorithms 1 and 2.

For each network, the Kullback-Leibler divergence is computed with the procedures presented using evidence propagation (see Algorithm 1) and using operations cache (described in Algorithm 2). The main purpose of the experiment is to get an estimation of the computation times required for both approaches. The obtained results are included in Table 5. It contains the following information:

- Network name.
- Number of nodes.
- Number of arcs.
- Number of parameters required for quantifying the uncertainty of the network.
- time1: Runtime using the algorithm without cache (Algorithm 1).
- time2: Runtime using the algorithm with cache (Algorithm 2).
- ops: Number of elementary operations stored in the operations repository $R_{O}$ to compute all the necessary distributions for the calculation using Algorithm 2.
- rep: Number of operations that are repeated and that, thanks to the use of $R_{O}$ and $R_{\Phi}$, will be executed only once.
- del: Number of factors that were removed from the $R_{\Phi}$ with the consequent release of memory space for future calculations.

The experiments have been run in a desktop computer with an Intel(R) Xeon(R) Gold 6230 CPU working at 3.60 GHz ( 80 cores). It has 312 Gb of RAM memory. The operating system is Linux Fedora Core 34.

Table 5. Runtimes for KL computation without cache (time1) and with cache (time2).


It is observed that the calculation with the second method always offers shorter runtimes than the first one. The shortest runtimes are presented in the table with bold style. It is noteworthy that the case of three networks in which the method based on the use of evidence cannot be completed because the available memory capacity is exceeded: water, mildew, and barley. Moreover, the computational overhead required to manage operations and factor repositories is beneficial as it avoids the repetition of a significant number of operations and enables unnecessary potentials to be released, especially in the most complex networks.

# 6. Conclusions 

Computing the KL divergence between the joint probabilities associated with two Bayesian networks is an important task that is relevant for many problems, for example assessing the accuracy of Bayesian network learning algorithms. However, in general, it is not possible to find this function implemented in software packages for probabilistic graphical models. In this paper, we provide an algorithm that uses local computation to calculate the KL divergence between two Bayesian networks. The algorithm is based in a procedure with two stages. The first one plans the operations determining the repeated operations and the times in which potentials are no longer necessary, while the second one carries out the numerical operations, taking care to reuse the results of repeated operations instead of repeating them and deallocating the memory space associated with useless potentials. Experiments show that this strategy saves time and space, especially in complex networks.

The functions have been implemented in Python taking as basis pgmpy software package and are available in the github repository: https://github.com/mgomez-olmedo/ KL-pgmpy, accessed on 24 August 2021. The README file of the project offers details about the implementation and the methods available for reproducing the experiments.

In the future, we plan to further improve the efficiency of the algorithms. The main line will be to invest more time in the planning stage looking for deletion orderings minimizing the total number of operations or optimizing the order of combinations, when several potentials have to be multiplied.

Author Contributions: Conceptualization, S.M., A.C. and M.G.-O.; methodology, S.M., A.C. and M.G.-O.; software, S.M., A.C. and M.G.-O.; validation, S.M., A.C. and M.G.-O.; formal analysis, S.M., A.C. and M.G.-O.; investigation, S.M., A.C. and M.G.-O.; writing-original draft preparation, S.M., A.C. and M.G.-O.; visualization, S.M., A.C. and M.G.-O.; supervision, S.M., A.C. and M.G.-O.; funding acquisition, S.M., A.C. and M.G.-O. All authors have read and agreed to the published version of the manuscript.
Funding: This research was jointly supported by the Spanish Ministry of Education and Science under project PID2019-106758GB-C31 and the European Regional Development Fund (FEDER).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: We are very grateful to the anonymous reviewers for their valuable comments and suggestions that have contributed to the improvement of the paper.
Conflicts of Interest: The authors declare no conflict of interest.
