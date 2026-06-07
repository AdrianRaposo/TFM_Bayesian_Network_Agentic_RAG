# HAL open science 

## A complexity analysis of MPE inference in possibilistic networks

Salem Benferhat, Amélie Levray, Karim Tabia

## To cite this version:

Salem Benferhat, Amélie Levray, Karim Tabia. A complexity analysis of MPE inference in possibilistic networks. IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), 2019, New Orleans,, Unknown Region. pp.1-6, 10.1109/FUZZ-IEEE.2019.8858977 . hal-03299694

## HAL Id: hal-03299694 <br> https://univ-artois.hal.science/hal-03299694v1

Submitted on 23 Jun 2022

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# A complexity analysis of MPE inference in possibilistic networks <br> (Preprint version) 

Salem BENFERHAT, Karim TABIA<br>Centre de Recherche en Informatique de Lens (CRIL)<br>Lens, France<br>\{benferhat,tabia\}@cril.fr

Amélie LEVRAY<br>University of Edinburgh<br>Edinburgh, Scotland<br>alevray@inf.ed.ac.uk


#### Abstract

Reasoning with uncertainty in graphical models often implies great computational cost. For example, computing the most probable explanation in Bayesian networks is known to be $N P^{P P}$-complete. Possibilistic networks represent an alternative powerful representation for uncertain information. This paper aims at showing that the computation complexity of MPE inference tasks in possibilistic networks are $N P$-complete. To that end, we provide full reduction and proof for MPE querying minbased and product-based possibilistic networks. More precisely, we provide incremental proofs based on reductions to and from three well-known $N P$-complete problems: SAT, 3SAT and Weighted MaxSAT decision problems.


Index Terms-Complexity, Possibilistic networks, MAP inference, MPE inference

## I. INTRODUCTION

Beliefs graphical models, such as Bayesian networks [6], credal networks [5], or possibilistic networks [3] are powerful means of compactly represent uncertainty using directed acyclic graphs and independence relationships. Typically, possibilistic networks are seen as counterparts of Bayesian networks based on possibility theory [10], where possibility degrees are more suited for handling imperfect, qualitative and partial information.

Inference in such graphical models has been extensively studied and many algorithms have emerged. On the other hand, while complexity results regarding inference in probabilistic networks are well-established [7]-[9], there is no such deep study for possibilistic networks. This paper aims at filling this gap.

Essentially, in graphical models there are three common types of queries: computing most probable (or plausible) explanation (MPE); computing a posteriori probability (or possibility) degrees ( $P r$ ); and computing the maximum a posteriori explanation (MAP). These tasks are known to be very hard in the probabilistic setting. Indeed, the decision problems associated to $M P E, P r, M A P$ are $N P$-complete, $P P$-complete and $N P^{P P}$-complete respectively (see [7], [9] for more details on complexity issues in Bayesian and credal networks). In this paper, we focus on possibility theory where we consider two interpretations of possibility theory, minbased possibility theory and product-based possibility theory [11].

In [2], the authors analysed the computational complexity of MAP queries in min-based and product-based possibilistic

Amélie LEVRAY<br>University of Edinburgh<br>Edinburgh, Scotland<br>alevray@inf.ed.ac.uk

networks. They showed that the decision problem behind MAP querying is $N P$-complete for both min-based and productbased possibilistic networks. Regarding MAP querying a product-based possibilistic network, only the proof of $N P$ hardness has been provided. The first part of this paper provides the proof of $N P$-completeness theorem, stated in [2], of MAP querying a product-based possibilistic network. In the second part of the paper, we address the complete analysis of the decision problems associated with the most plausible explanation (MPE) task in both min-based and product-based possibilistic networks, show using a reduction to the SAT decision problem, that it is $N P$-complete. Such computational complexity outcomes favour possibility theory as an efficient alternative for reasoning with uncertainty (some results on learning possibilistic parameters over probabilistic ones can be found in [13]).

The paper is outlined as follows. In section II, we briefly recall notions on possibility theory, as well as give motivations. The third section investigates general properties on inference tasks in possibilistic networks. In particular, we provide the proof that the decision problem based on conditioning operator is the same as the one based on conjunction operator when computing MAP queries. Hence, we no longer need conditioning rule in the computation of MAP queries. The fourth section addresses the $N P$-completeness result of MAP inference in product-based possibilistic networks. In the fifth section, we establish the complexity of MPE inference. This is done by showing a reduction from 3SAT to MPE querying a binary and boolean possibilistic networks, and conversely with a reduction from $M P E$ in a possibilistic network to a SAT problem.

## II. A REFRESHER ON POSSIBILITY THEORY AND POSSIBILISTIC NETWORKS

In this section, we give a short reminder of the basic notions associated to possibility theory [11] and its associated graphical models named possibilistic networks [1], [4], [12]. A possibility distribution, denoted by $\pi$, is a mapping from the set of possible worlds $\Omega$ to the unit interval $[0,1]$. Note that we consider a finite and discrete set. For a given interpretation $\omega \in \Omega, \pi(\omega)=1$ is interpreted as fully possible. $\pi(\omega)=0$ is interpreted as impossible. $\pi$ is said to be normalised if there is at least an element $\omega \in \Omega$ that is fully possible (i.e. such

that $\pi(\omega)=1$ ).
There are two understandings of the scale $[0,1]$ of possibility degrees, either the product-based interpretation as in probability theory or the min-based interpretation which considers degrees on an ordinal scale. These two interpretations lead to two different conditioning rules when dealing with new evidence. We call min-based conditioning $\left.\right|_{m}$ the operation leading to $\pi\left(.|{ }_{m} \phi\right)$ given by [11], [14]:

$$
\pi\left(\omega_{i}\right|_{m} \phi)= \begin{cases}1 & \text { if } \pi\left(\omega_{i}\right)=\Pi(\phi) \text { and } \omega_{i} \in \phi \\ \pi\left(\omega_{i}\right) & \text { if } \pi\left(\omega_{i}\right)<\Pi(\phi) \text { and } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

The product-based conditioning, denoted by $\left.\right|_{*}$, is, as in the probabilistic setting, defined as follows:

$$
\pi\left(\omega_{i} \mid * \phi\right)= \begin{cases}\frac{\pi\left(\omega_{i}\right)}{\Pi(\phi)} & \text { if } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

A possibilistic network denoted $\mathcal{P N} \mathcal{N}=<G, \Theta>$ is specified by two components:

- A graphical component $G$ : a directed acyclic graph (DAG) where each node represents a discrete variable and edges encode independence relations between variables.
- A numerical component $\Theta$ : a set of local normalised possibility distributions $\Theta_{i}=\pi_{\mathcal{P N}}\left(X_{i} \mid \operatorname{par}\left(X_{i}\right)\right)$ of each node $X_{i}$ given its parents $\operatorname{par}\left(X_{i}\right)$.
The joint possibility distribution is factorised using a chain rule, defined as:

$$
\pi_{\mathcal{P N}_{\otimes}}\left(X_{1}, . ., X_{n}\right)=\otimes_{i=1, . ., n} \pi_{\mathcal{P N}_{\otimes}}\left(X_{i} \mid \otimes \operatorname{par}\left(X_{i}\right)\right)
$$

where $\otimes=m$ in min-based possibilistic setting and $\otimes=*$ in product-based possibilistic setting.

It is well-known that inference in probabilistic models is a hard task in the general case. In particular, the decision problem associated with MAP in Bayesian networks is $N P^{P P}$ complete [7]. The next sections address the same complexity issues on product-based possibilistic networks as well as the computational complexity of MPE inference.

The complexity of MAP querying a min-based possibilistic network has already been discussed in [2] and it has been shown that MAP inference in this context is $N P$-complete.

But first, we recall the definition of inference tasks in possibilistic networks.

## III. INFERENCE IN POSSIBILISTIC NETWORKS

In this paper, we investigate two of the most common types of queries when reasoning with graphical models, that are MAP inference and MPE inference. MAP queries require searching for the most plausible instantiation of query variables $Q$ given an evidence $e$ (an instantiation of a set of variables $E$ ). While MPE queries search for the most plausible explanation of an evidence $e$. More formally,

MAP query: Let $\mathcal{P N}$ be a possibilistic network over the set of variables $V, Q \subset V$ be a set of query variables and $E \subset V$ be a set of evidence variables with $Q \cap E=\emptyset$. Then, given an evidence $E=e$, the aim is to compute the most plausible instantiation $q$ of $Q$ given the evidence $e$.

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)
$$

$M P E$ query: Let $\mathcal{P N}$ be a possibilistic network over the set of variables $V, E \subset V$ be a set of evidence variables. We denote $X$ the set of remaining variables $(X=V \backslash E)$. Then, given an evidence $E=e, M P E$ query compute the most plausible instantiation $x$ of $X$ compatible with the evidence $e$. Stated otherwise by:

$$
\operatorname{argmax}_{x \in X}\left(\Pi_{\mathcal{P N}}(x, e)\right)
$$

Note that $\Pi_{\mathcal{P N}}(x, e)$ is the possibility degree of the conjunction of $x$ and $e$, especially since $X \cap E=\emptyset$. Another notation commonly used is $\Pi_{\mathcal{P N}}(x \wedge e)$.

In [2], it is stated that in the case of a MAP query, the problem can be reduced to finding the most plausible assignment of query variables $Q$ compatible with the evidence $e$. More precisely, it can be rewritten as:

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q, e)\right)
$$

Namely, given a possibilistic network $\mathcal{P N}, Q$ the set of query variables and an evidence $e$ (an instantiation of variables $E$ ), we have:

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)=\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q, e)\right)
$$

Simply put, the conditioning rule of possibility theory is not required to compute the maximum a posteriori assignment. In this section, we provide the full proof of Equation (7) of the above statement, stated in [2].

- Let us start with the min-based conditioning. Given a possibilistic network $\mathcal{P N}_{m}$ over $V$ and let $Q$ and $E$ be two subsets of $V$ (s.t. $Q \cap E=\emptyset$ ). Then, computing $\operatorname{argmax}_{q \in D_{Q}}\left(\Pi(q \mid e)\right)$ is equivalent to searching the instantiation $q$ such that $\Pi(q \mid e)=1$. By definition of the min-based conditioning, $\Pi(q \mid e)=1$ if $\Pi(q, e)=\Pi(e)$. Assume that $\operatorname{argmax}_{q \in D_{Q}}(\Pi(q, e))$ is $q^{\prime}$ then since $\Pi(e)=\max _{\omega \vDash e} \pi(\omega)$ or said otherwise $\Pi(e)=\max _{q \in D_{Q}} \Pi(q, e)$ which is given by $\Pi\left(q^{\prime}, e\right)$.
- Let us now consider product-based conditioning. In the same way, since the possibilistic network $\mathcal{P N}_{*}$ is normalised then $\forall e \in E, \operatorname{argmax}_{q \in D_{Q}}\left(\Pi(q \mid e)\right)$ is equivalent to searching the instantiation $q$ such that $\Pi(q \mid e)=1$. Which, by definition, is given by $\Pi(q \mid e)=$ $\frac{\Pi(q, e)}{\Pi(e)}$, therefore, $\Pi(q \mid e)=1$ if $\Pi(q, e)=\Pi(e)$. From there, assume that $\operatorname{argmax}_{q \in D_{Q}}(\Pi(q, e))$ is $q^{\prime}$ then since $\Pi(e)=\max _{\omega \vDash e} \pi(\omega)=\Pi\left(q^{\prime}, e\right)$. Thus, $\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)=\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q, e)\right)$.
Given this equivalence, we can focus only on the MAP problem redefined by Equation (6).

## IV. MAP QUERYING PRODUCT-BASED POSSIBILISTIC

NETWORKS

In [2] a computational complexity analysis of $M A P$ queries in min-based and product-based possibilistic networks is provided. In particular, it is stated that the decision problem behind $M A P$ querying is $N P$-complete for product-based possibilistic networks. The full proof of $N P$-hardness has been provided. This section provides the proof of $N P$-completeness theorem, stated in [2], of $M A P$ querying a product-based possibilistic network. Let us first give a brief refresher on decision problems associated with $M A P$ querying productbased possibilistic networks.

## A. Definition of the decision problems

Let us recall the definition of the decision problem associated with a $M A P$ query in product-based possibilistic networks, denoted $\pi_{*}$-D-MAP.

Definition 1. By $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ we denote the decision problem associated with $M A P$ querying possibilistic networks that we define by:
Input:

- $\mathcal{P N}_{*}:$ a product-based possibilistic network
- $e$ (evidence): an instantiation of a set of variables $E$
- $Q$ (query): a set of variables with $Q \cap E=\emptyset$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $q$ of non observed variables $Q$ such that $\Pi_{\mathcal{P N}_{0}}(q, e) \geq t$ ?

As said before, the decision problem we refer to in this reduction is the weighted MaxSAT problem. It is defined as follows:

Definition 2. By D-WMaxSAT $(\Psi, k)$ we denote the decision problem specified by:
Input:

- $\Psi$ : a weighted CNF formula over boolean variables $V=$ $\left\{X_{1}, \ldots, X_{n}\right\}$ simply represented by

$$
\Psi=\left\{\begin{array}{c}
\left(C_{1}, \alpha_{1}\right) \\
\left(C_{2}, \alpha_{2}\right) \\
\cdots \\
\left(C_{m}, \alpha_{m}\right)
\end{array}\right\}
$$

where $C_{i}^{t} *$ are clauses and $\alpha_{i}^{t} *$ are positive integers.

- $k$ : a positive integer

Question: Is there an instantiation of variables $V$ such that the sum of weights of satisfied clauses in $\Psi$ is greater or equal to $k$ ?
B. From querying product-based possibilistic networks to WMaxSAT

1) Definition of a weighted CNF formula associated to a product-based possibilistic network: In what follows, we will reuse the same weighted CNF formula associated to a productbased possibilistic network and defined in [2].

Definition 3. Let $\mathcal{P N}_{*}$ be a product-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$.

Let $Q$ be a subset of $V, e=e_{1}, \ldots, e_{l}$ be an instantiation of evidence variables $E$ (with $Q \cap E=\emptyset$ ) and $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is defined by: $\Psi_{R} \cup \Psi_{0} \cup \Psi_{e}$ where

$$
\begin{aligned}
& \Psi_{R}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=2^{-\alpha_{i}}\right\} \\
& \Psi_{0}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, M\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=0\right\} \\
& \Psi_{e}=\left\{\left(e_{k}, M\right): k=1, \ldots, l\right\}
\end{aligned}
$$

where $M>\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$.
Example 1 illustrates Definition 3.
Example 1. Let us consider the product-based possibilistic network $\mathcal{P N}_{*}$ of Figure 1. Let $Q=\{B\}$ be a subset of $V$, let $e=\neg e$ be an instantiation of evidence variables $E=\{C\}$ and let $t=2^{-2}$ be the threshold.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of a product-based possibilistic network $\mathcal{P N}_{*}$ over $A, B$ and $C$.

Let $M=30$. Then following Definition 3, the weighted CNF formula $\Psi_{\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}}$ is

$$
\Psi_{\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}}=\left\{\begin{array}{c}
(a, 4) \\
(\neg b, 8) \\
\left(\neg c \vee \neg a \vee \neg b, 7\right) \\
(c \vee \neg a \vee b, 2) \\
\left(\neg c \vee a \vee b, 30\right) \\
\left(\neg c \vee a \vee \neg b, 30\right) \\
\left(\neg c, 30\right)
\end{array}\right\} \Psi_{R}
$$

2) Reduction from a product-based possibilistic network to a weighted CNF formula: Theorem 1, given in [2], provides the result that the decision problem $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ can be reduced into D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$.
Theorem 1. [2] Let $\mathcal{P N}_{*}$ be a product-based possibilistic network. Let $Q$ be a subset of $V$, e be an instantiation of variables $E$ and $t$ be a threshold. Let $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ be the CNF formula given by Definition 3. Then, $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ answers "yes" if and only if D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\right.$ $\log _{2} t+M *(Z+|E|))$ answers "yes" where $\pi_{*}$-D-MAP is given by Definition 4 and D-WMaxSAT is given by Definition 2.

In this section, we provide the full proof of Theorem 1 and illustrate it with examples.

Proof. Let us first define the parameters of the WMaxSAT decision problem, D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$. Namely,

- $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is the weighted CNF formula given by Definition 3 .
- $k$ is the threshold for the problem and it is given by:

$$
k=X+\log _{2} t+M *\left(\left(\sum \Pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i}\right)=0\right)+1\right)
$$

where $M$ is defined in Definition 3. And $X$ is given by the sum of weights in $\Psi_{R}: X=\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in\right.$ $\left.\Psi_{R}\right\}$
The second part of the proof consists in showing that the two decision problems as defined are equivalent. Let the query associated to D-WMaxSAT be: Does DWMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\log _{2} t+M *(Z+1)\right)$ answer "yes"? More precisely, is there an instantiation of all variables that satisfies a subset of clauses in $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ having the sum of the degrees of the satisfied clauses greater or equal to $k$ ?
Recall that $\pi_{*}$-D-MAP decision problem is: Given an instantiation $e$ of evidence variables, is there an instantiation $q$ of query variables $Q$ such that $\Pi(q, e) \geq t$ ?
For the sake of clarity, in this proof we simply write $\Psi$ instead of $\Psi_{\mathcal{P N}_{*}, Q, e, t}$.
* Assume that D-WMaxSAT $(\Psi, k)$ answers "yes". This means that there exists a subset $A \subseteq \Psi$ such that:

- $\left\{\left(\phi_{i}, \alpha_{i}\right) \in A\right\}$ is consistent and
- $\sum_{\left\{\phi_{i}, \alpha_{i}\right\} \in A} \alpha_{i} \geq k$

Note that we can state that $\left\{\left(e_{k}, M\right): k=1, \ldots, l\right\}$ is included in $A$. Indeed, if some $\left(\phi_{i}, M\right)$ of $\Psi$ is not in $A$ then $\sum_{\left\{\phi_{i}, \alpha_{i}\right\} \in A}$ cannot be greater than $M *(Z+|E|)$. Let us denote by $A^{*}=A \backslash\left\{\left(\phi_{i}, M\right):\left(\phi_{i}, M\right) \in A\right\}$ then we can also state that:

- $\left\{\left(\phi_{i}, \alpha_{i}\right) \in A^{*}\right\}$ is consistent,
- $\sum_{\left\{\phi_{i}, \alpha_{i}\right\} \in A^{*}} \alpha_{i} \geq X+\log _{2} t$

Let $\omega$ be a model of $\left\{\phi_{i}:\left(\phi_{i}, \alpha_{i}\right) \in A\right\}$ and $\left\{\phi_{i}:\left(\phi_{i}, \alpha_{i}\right) \in\right.$ $\left.A^{*}\right\}$. Since $X=\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi\right.$ and $\left.\alpha_{i} \neq M\right\}$. Then the latter equation implies that:

$$
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \notin A^{*}\right\} \leq-\log _{2} t
$$

This can be rewritten as:

$$
\sum_{\omega \alpha_{i}}\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} \leq-\log _{2} t
$$

It is enough now to consider the following immediate simplified inequalities to get the desirable result.

$$
\begin{aligned}
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} & \leq-\log _{2} t \\
-\sum\left\{\log _{2} 2^{-\alpha_{i}}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} & \leq-\log _{2} t \\
-\log _{2}\left(\left(*\left\{2^{-\alpha_{i}}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\}\right)\right. & \leq-\log _{2} t \\
-\log _{2}\left(\left(*\left\{2^{-\alpha_{i}}: \omega \nvdash \neg x_{i} \vee \neg u_{i j}\right\}\right)\right. & \leq-\log _{2} t \\
-\log _{2}\left(\left(*\left\{2^{-\alpha_{i}}: \omega \vDash x_{i} \wedge u_{i j}\right\}\right)\right. & \leq-\log _{2} t \\
-\log _{2} \pi_{\mathcal{P N}_{*}}(\omega) & \leq-\log _{2} t \\
\pi_{\mathcal{P N}_{*}}(\omega) & \geq t
\end{aligned}
$$

with $\omega \vDash e$. Hence the answer to $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ is also "yes" by taking $q$ such that $\omega \models q$.

* Assume that D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$ answers "no". Then, for all consistent subset of clauses $A$ that include $\Psi_{0}$ and $\Psi_{e}$ we have

$$
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in A\right\}<k
$$

Let us consider such a subset $A_{*}$. Let $\omega$ be a model of $A^{*}$, then following the same previous steps we have:

$$
\begin{aligned}
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A_{*} s . t \omega \nvdash \phi_{i}\right\} & >-\log _{2} t \\
-\log _{2}\left(\left(*\left\{2^{-\alpha_{i}}: \omega \nvdash \neg x_{i} \vee \neg u_{i j}\right\}\right)\right. & >-\log _{2} t \\
-\log _{2}\left(\left(*\left\{2^{-\alpha_{i}}: \omega \vDash x_{i} \wedge u_{i j}\right\}\right)\right. & >-\log _{2} t \\
-\log _{2} \pi_{\mathcal{P N}_{*}}(\omega) & >-\log _{2} t \\
\pi_{\mathcal{P N}_{*}}(\omega) & <t
\end{aligned}
$$

with $\omega \vDash e$. Hence the answer to $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ is also "no".

Example 2. Let $Q=\{B\}$ and $E=\{C\}$ be the set of query variables and evidence variables respectively. Let us consider the evidence $e=\neg e$. Let $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ be the weighted CNF formula associated to $\mathcal{P N}_{*}$ given by Definition 3. The MAP query over $\mathcal{P N}_{*}$ is: Is there an instantiation $q$ of the variables $Q$ such that $\Pi_{\mathcal{P N}_{*}}(q, e) \geq 2^{-2}$. Hence, the corresponding problem D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$ is given by: Is there an instantiation of the variables such that the sum of the degrees of the satisfied clauses is greater or equal to $k$ ?
Let us set the values of the variables $X, M$ and $Z: X=21$, $M=30$, and $Z=2$. Then, $k=X+\log _{2} t+30 *(Z+1)=109$. Given this configuration, D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*},(B), \neg c, 2^{-2}}, 109\right)$ answers "yes". Indeed, it is enough to consider $A$ such that

$$
A=\left\{\begin{array}{c}
(a, 4) \\
(\neg b, 8) \\
(\neg c \vee \neg a \vee \neg b, 7) \\
(\neg c \vee a \vee b, 30) \\
(\neg c \vee a \vee \neg b, 30) \\
(\neg c, 30)
\end{array}\right\}
$$

The sum of the weights in $A$ is equal to 109. A model of formulas in $A$ can be $a \neg b \neg c$ for which using the productbased chain rule has a possibility degree of $\Pi_{\mathcal{P N}_{*}}(a \neg b c)=$ $2^{-2}$. Hence, $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}\right)$ answers "yes" as well.

## C. Complexity of MPE inference

In this subsection, we analyse the complexity of MPE inference in product-based possibilistic networks. As we have mentioned in the definition of the query, we search for the assignment of all variables compatible with the evidence. Which means that the only difference with a MAP query as redefined in Equation (6) is that instead of a subset of variables we use all of them.

Based on what has just been proven for MAP inference, we argue that by choosing a set of query variables corresponding to the remaining variables $V \backslash E$, the complexity results follows from Theorem 1. This is formally stated in the following proposition.

Proposition 1. $\pi_{*}$-D-MPE is NP-complete.

We provide a more rigorous proof for MPE inference in min-based possibilistic networks in the next section.

## V. COMPLEXITY ANALYSIS OF MPE INFERENCE IN min-BASED POSSIBILISTIC NETWORKS

This section focuses on MPE query in min-based possibilistic networks. Contrary to MAP inference, where the complexity analysis have shown that MAP inference in possibilistic networks costs less than in Bayesian networks; Here we show that MPE querying a possibilistic network is $N P$-complete as in Bayesian networks.

Basically, to prove that $\pi_{m}$-D-MPE is $N P$-complete, we follow the same steps as in the analysis of MAP in min-based possibilistic networks given in [2]. More precisely,

- we first show the $N P$-hardness of $\pi_{m}$-D-MPE by providing a reduction from the D-3SAT decision problem to $\pi_{m}$-D-MPE decision problem. In particular, in this reduction we build a special possibilistic network that only takes into account boolean variables and binary values. This network is called a binary and boolean possibilistic network (see [2] for more details).
- we provide a reduction of the $\pi_{m}$-D-MPE decision problem, defined for min-based possibilistic networks, to the D-SAT decision problem.


## A. Definition of the decision problems

We first formally define the decision problem associated with a MPE query in min-based possibilistic networks, denoted $\pi_{m}$-D-MPE as well as the decision problem associated with querying a B\&B possibilistic network.
Definition 4. We denote $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ the decision problem associated with MPE querying a min-based possibilistic network. It is defined by:
Input:

- $\mathcal{P N}_{m}$ : a min-based possibilistic network
- $e$ (evidence): an instantiation of a set of variables $E$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $x$ of the variables $X$ such that $\Pi_{\mathcal{P N}_{m}}(x, e) \geq t ?$

Definition 5 considers a particular case of Definition 4 where degrees are either 0 or 1 (hence no need to explicitly specify $t$ ).
Definition 5. By $\mathbf{B \& B}_{m}$-D-MPE( $\left.\mathcal{P N}_{B \& B_{m}}, e\right)$ we denote the decision problem associated with MPE querying a min-based Boolean and Binary possibilistic network that we define by: Input:

- $\mathcal{P N}_{B \& B_{m}}$ : a min-based binary and boolean possibilistic network over $V=\left\{X_{1}, \ldots, X_{n}\right\}$
- $e$ (evidence): an instantiation of a set of observation variables $E$
Question: Is there an instantiation $x$ of variables $X$ such that $\Pi_{\mathcal{P N}_{B \& B_{m}}}(x, e)=1 ?$

In [2], the authors gave the reasons why we can afford to only consider the case $\Pi_{\mathcal{P N}_{B \& B_{m}}}(x, e)=1$.

Let us now recall the boolean satisfiability decision problem denoted D-SAT.

Definition 6. By D-SAT $(\Psi)$ we denote the decision problem associated to determining if there exists an assignment $\omega$ that satisfies $\Psi$. It is defined by:
Input: $\Psi$ a formula in a conjunctive normal form
Question: Is $\Psi$ satisfiable?
A restricted version of the SAT problem involves a 3CNF and is called D-3SAT decision problem. A 3CNF is a formula in a conjunctive normal form for which each clause is a disjunction of at most 3 literals. Thus,

Definition 7. By D-3SAT $(\Psi)$ we denote the decision problem defined by:
Input: $\Psi$ a 3CNF formula
Question: Is $\Psi$ satisfiable?
B. From 3SAT to MPE querying over B\&B possibilistic networks

As in [2], we build a B\&B possibilistic network from a 3CNF. The definition of this reduction is recalled by Definition 8. For more details, the reader can refer to [2].

Definition 8. Let $\Psi=C_{1} \wedge C_{2} \wedge \ldots \wedge C_{m}$ be a 3CNF formula. Let $V=\left\{X_{1}, \ldots, X_{n}\right\}$ be the set of propositional variables appearing in $\Psi$. The B\&B possibilistic network associated with $\Psi$, denoted by $\mathcal{P N}_{\Psi}$ is defined as follows:

1) For each propositional symbol $X_{i}$ appearing in $\Psi$, we add a boolean node variable in the graph. Each variable $X_{i}$ is associated with a possibility distribution given by: $\pi_{\mathcal{P N}_{\Psi}}\left(x_{i}\right)=1$ and $\pi_{\mathcal{P N}_{\Psi}}\left(\neg x_{i}\right)=1$.
2) For each clause $C_{j}$ of $\Psi$, we add a conditional node variable, $C_{j}$. Parents of $C_{j}$ are the rooted variables $X_{i}$ that are involved in $C_{j}$. Each $C_{j}$ is associated with a conditional possibility distribution given by: $\forall u_{j k}$ an instance of parents of $C_{j}$ that models the satisfiability of the clause.
3) Lastly, we add a single boolean node, $E_{\Psi}$, which represents the satisfiability of the overall formula $\Psi$. It has all nodes $C_{j}^{\prime} s$ as parents. Intuitively, $E_{\Psi}$ is set to true if all clauses are satisfied.

Theorem 2 provides the reduction from the decision problem $\mathbf{D}-\mathbf{S S A T}(\Psi)$ into $\mathbf{B \& B}_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{\Psi}, e\right)$ where the input $e$ is let to $e_{\Psi}$. More formally:

Theorem 2. Let $\Psi$ be a 3CNF formula. Let $\mathcal{P N}_{\Psi}$ be the $B \& B$ possibilistic network given by Definition 8. Let $V_{\mathcal{P N}_{\Psi}}$ be the set of variables in $\mathcal{P N}_{\Psi}$, namely $\left\{X_{1}, \ldots, X_{n}\right\} \cup$ $\left\{C_{1}, \ldots, C_{m}\right\} \cup\left\{E_{\Psi}\right\}$. Then, D-3SAT $(\Psi)$ answer is "yes" if and only if the $\mathbf{B \& B}_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{\Psi}, e_{\Psi}\right)$ answers "yes" where D-3SAT is given in Definition 7 and $\mathbf{B \& B}_{m}$-D-MPE is given by Definition 5.

## C. From querying min-based possibilistic networks to SAT

In this section, we no longer restrict ourselves to binary possibility distributions. Namely, (conditional) possibility degrees can take any value in the unit interval $[0,1]$. However, for the sake of simplicity, we still only consider boolean variables. This is not a restriction and the proof can be adapted by encoding a non-boolean variable by a set of boolean variables. We propose to reduce the decision problem $\pi_{m}$-D-MPE to the decision problem D-SAT.

The following gives the definition of the CNF formula associated with the network a MPE query, denoted by $\Psi_{\mathcal{P N}_{m}, e, t}$.

Definition 9. Let $\mathcal{P N}_{m}$ be a min-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $e=$ $e_{1}, \ldots, e_{l}$ be an instantiation of evidence variables $E$ and let $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{m}, e, t}$ over the set of variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$, is given by:

$$
\begin{aligned}
\Psi_{\mathcal{P N}_{m}, e, t} & =\left\{\left(\neg x_{i} \vee \neg u_{i j}\right): \pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<\mathbf{t}\right\} \\
& \cup\left\{\mathbf{e}_{\mathbf{k}}: \mathbf{k}=\mathbf{1}, \ldots, \mathbf{l}\right\}
\end{aligned}
$$

This reduction is done in polynomial time (and space) with respect to the size of $\mathcal{P N}_{m}$.

The following theorem states that $\pi_{m}$-D-MPE can be reduced to D-SAT.

Theorem 3. Let $\mathcal{P N}_{m}$ be a min-based possibilistic network, $e$ be an instantiation of evidence variables $E$ and $t$ be a real number in $(0,1]$. Let $\Psi_{\mathcal{P N}_{m}, e, t}$ be the CNF formula given by Definition 9. Then, $\pi_{m}$-D-MPE( $\left.\mathcal{P N}_{m}, e, t\right)$ says "yes" if and only if D-SAT $\left(\Psi_{\mathcal{P N}_{m}, e, t}\right)$ says "yes" where $\pi_{m}$-D-MPE is given by Definition 4 and D-SAT is given by Definition 6.
Proof. The proof is similar to the one provided in [2] for analyzing the complexity of map-querying possibilistic networks. We need to prove that when $\Psi_{\mathcal{P N}_{m}, e, t}$ is satisfiable then $\Pi_{\mathcal{P N}_{m}}(x, e) \geq t$ and that when $\Psi_{\mathcal{P N}_{m}, e, t}$ is unsatisfiable then $\Pi_{\mathcal{P N}_{m}}(x, e)<t$ for all assignments of all variables compatible with $e$.

- Assume that $\Psi_{\mathcal{P N}_{m}, e, t}$ is satisfiable. This means that there exists an instantiation of all variables, denoted by $\omega^{*}$, that satisfies all clauses of $\Psi_{\mathcal{P N}_{m}, e, t}$ including $e=e_{1}, \ldots, e_{l}$. Then we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$ by construction of $\Psi_{\mathcal{P N}_{m}, e, t}$. So if $\omega^{*}$ satisfies all clauses in $\Psi_{\mathcal{P N}_{m}, e, t}$ then $\omega^{*}$ falsifies each of the formulas in $\left\{\left(x_{i} \wedge u_{i j}\right):\left(\neg x_{i} \vee \neg u_{i j}\right) \in \Psi_{\mathcal{P N}_{m}, e, t}\right\}$. Thus, all conditionals $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)$ applied in chain rule to compute $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right)$ have a possibility degree greater or equal to $t$. Therefore, $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t$. Hence the answer to $\pi_{m}$ $\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ is also "yes".
- Assume that $\Psi_{\mathcal{P N}_{m}, e, t}$ is unsatisfiable. Then for all instantiation of variables $\omega$ such that $\omega \models e\left(=e_{1} \wedge \ldots \wedge e_{l}\right)$, there exists at least a clause $C_{i}=\neg x_{i} \vee \neg u_{i j}$ that is falsified by $\omega$ (and hence $\omega \models x_{i} \wedge u_{i j}$ ). And by construction of $\Psi_{\mathcal{P N}_{m}, e, t}$, we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$, so using the min-based chain rule we have $\forall \omega \models e$,
$\pi_{\mathcal{P N}_{m}}(\omega)<t$. Hence $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ is also "no".

To summarise Proposition 1 together with Theorems 2 and 3 show that the decision problem associated with MPE inference is $N P$-complete for both min-based and productbased possibilistic networks.

## VI. CONCLUSIONS

This paper dealt with the computational complexity of inference in possibilistic networks. The main results shown in this work proved that possibilistic networks offer interesting advantages for reasoning with uncertain information. These results have an impact on the complexity of reasoning in the interval-based possibilistic setting. A future work concerns the computation of the a posteriori possibility degree of an event in both min-based and product-based possibilistic networks.

## VII. ACKNOWLEDGEMENTS

This work is supported by the european project H2020 Marie Sklodowska-Curie Actions (MSCA) research and Innovation Staff Exchange (RISE): AniAge (High Dimensional Heterogeneous Data based Animation Techniques for Southeast Asian Intangible Cultural Heritage).
