# HIAL open science 

## Possibilistic Networks: Computational Analysis of MAP and MPE Inference

Amélie Levray, Salem Benferhat, Karim Tabia

## To cite this version:

Amélie Levray, Salem Benferhat, Karim Tabia. Possibilistic Networks: Computational Analysis of MAP and MPE Inference. International Journal on Artificial Intelligence Tools, 2020, 29 (03n04), pp.2060005. 10.1142/S0218213020600052 . hal-03662634

## HAL Id: hal-03662634 <br> https://hal.science/hal-03662634v1

Submitted on 31 May 2022

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Possibilistic networks: computational analysis of MAP and MPE inference <br> (Prepring version) 

Amélie Levray ${ }^{1}$, Salem Benferhat ${ }^{2}$, Karim Tabia ${ }^{2}$<br>${ }^{1}$ School of Informatics, University of Edinburgh, 10 Crichton St, Edinburgh, EH8 9AB, United Kingdom<br>${ }^{2}$ CRIL, Université d'Artois, CNRS UMR-8188, rue Jean Souvraz, Lens, 62300, France


#### Abstract

Possibilistic networks are powerful graphical uncertainty representations based on possibility theory. This paper analyzes the computational complexity of querying min-based and product-based possibilistic networks. It particularly focuses on very common kind of queries: computing maximum a posteriori explanation (MAP) and computing most plausible explanation (MPE). The main result of the paper is to show that the decision problem of answering these queries in both min-based and productbased possibilistic networks is $N P$-complete. Such computational complexity results represent an advantage of possibilistic networks over probabilistic networks since MAP querying is $N P^{P P}$-complete in probabilistic Bayesian networks. We provide the proof based on reductions from the 3SAT decision problem to querying possibilistic networks decision problem. We also provide reductions that are useful for the implementation of MAP and MPE queries using SAT solvers. For product-based possibilistic networks, we provide incremental proofs based on polynomial reductions from SAT and its weighted variant WMAXSAT decision problem.


## 1 Introduction

Beliefs graphical models, such as Bayesian networks [13], credal networks [12], or possibilistic networks [6] are powerful means to compactly represent uncertainty distributions using directed acyclic graphs and independence relationships. Despite many similarities with probabilistic networks, possibilistic graphical models offer interesting advantages especially for modeling and reasoning with qualitative and incomplete uncertainty. For example, in the ordinal possibilistic setting, there may be meaningful gains where the idempotence property of minimum and maximum operators benefit to inference algorithms, as stressed

in [21]. Also, recent works $[10,18,24,30]$ involve using possibilistic setting applied to web semantics. Thus, possibility theory $[17,20]$ is a natural alternative uncertainty theory particularly appropriate when only the plausibility ordering between events is useful. In fact, there are two main definitions of possibility theory. The first one is called min-based possibility theory. In this setting, the unit interval $[0,1]$, used for assessing the uncertainty degrees of events, is viewed as an ordinal scale. Hence, only the minimum and maximum operators are used for defining uncertainty measures. This contrasts with the second definition of possibility theory, called product-based possibility theory, where the unit interval is used in the general sense.

Inference in possibilistic networks has been extensively studied and many algorithms have emerged. On the other hand, while complexity results regarding inference in probabilistic networks are well-established [14-16], there is no such deep study for possibilistic networks. This paper aims at filling this gap. More precisely, in this paper, we provide additional benefits for adopting such tools in terms of inferential computational complexity in the context of possibility theory frameworks $[17,20]$.

Essentially, in graphical models there are three common types of queries: computing most probable (or plausible) explanation (MPE); computing a posteriori probability (or possibility) degrees ( $\operatorname{Pr}$ ); and computing the maximum a posteriori explanation (MAP). These tasks are known to be very hard in the probabilistic setting. Indeed, the decision problems associated to $M P E, \operatorname{Pr}, M A P$ are $N P$-complete, $P P$-complete and $N P^{P P}$-complete respectively (see $[14,16]$ for more details on complexity issues in Bayesian and credal networks).

This paper focuses most plausible explanation (MPE) and maximum a posteriori (MAP) in the context of min-based and product-based possibilistic networks. One of the major result of this paper is to show that querying possibilistic networks has a lower complexity than querying probabilistic networks. More precisely, we show that the decision problem associated with answering $M A P$ and $M P E$ queries in possibilistic networks is $N P$-complete. The proof is provided for both min-based and product-based networks and is built progressively. To show the hardness of the decision problem of MAP (resp. MPE) querying a possibilistic network, we focus on a special type of possibilistic networks called Binary and Boolean possibilistic networks. We provide a reduction from 3SAT to MAP (resp. MAP) querying a Binary and Boolean possibilistic network. Finally, we provide reductions from querying a possibilistic network to two well-known $N P$-complete problems: SAT and weighted MaxSAT decision problems.

The rest of this paper is organized as follows: Section 2 recalls basic notions on possibilistic frameworks. Section 3 discusses motivations and related work. Section 4 introduces the definition of MAP and MPE inference in possibilistic networks and give first results on the computational complexity of these inferences. Section 5 presents an overview of the solution to prove the complexity results of the decision problems considered in this paper. The remaining sections present different polynomial-time reductions used in this paper.

# 2 Background notions 

This section provides a brief refresher on possibility theory (for more details see [20]) and possibilistic networks ( $[2,8,22])$. One of the basic elements in possibility theory is the notion of a possibility distribution, denoted by $\pi$, which is a mapping from the universe of discourse $\Omega$ to the unit interval $[0,1]$. Especially, we consider a finite and discrete universe of discourse. By convention, for a given $\omega \in \Omega, \pi(\omega)=1$ means that $\omega$ is fully possible while $\pi(\omega)=0$ means that it is impossible for $\omega$ to be the real world. A possibility distribution $\pi$ is said to be normalized if there is at least an element $\omega \in \Omega$ such that $\pi(\omega)=1$.

Given a possibility distribution $\pi$, one can define a possibility measure, defined for each event $\phi \subseteq \Omega$, by:

$$
\Pi(\phi)=\max \{\pi(\omega): \omega \in \phi\}
$$

It expresses to what extent $\phi$ is coherent (compatible) with available information represented by $\pi$.

There are two interpretations of possibility degrees, either the product-based interpretation of the scale $[0,1]$ like in probability theory or the min-based interpretation which consider degrees on an ordinal scale. These two interpretations lead to two different ways to deal with possibility degrees. Indeed, updating degrees given a new evidence, namely conditioning, differs whether the interval $[0,1]$ is just used to rank-order events or not. We call min-based conditioning $\left.\right|_{m}[20,23]$ the operation defined by: given a possibility distribution $\pi$, and a new evidence $\phi \subseteq \Omega$ (with $\Pi(\phi)>0$ ) the conditional distribution $\pi\left(. \mid_{m} \phi\right)$ is obtained as follows:

$$
\pi\left(\omega_{i} \mid_{m} \phi\right)= \begin{cases}1 & \text { if } \pi\left(\omega_{i}\right)=\Pi(\phi) \text { and } \omega_{i} \in \phi \\ \pi\left(\omega_{i}\right) & \text { if } \pi\left(\omega_{i}\right)<\Pi(\phi) \text { and } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

The product-based conditioning, denoted by $\left.\right|_{*}$, is, as in the probabilistic setting, defined as follows:

$$
\pi\left(\omega_{i} \mid_{*} \phi\right)= \begin{cases}\frac{\pi\left(\omega_{i}\right)}{\Pi(\phi)} & \text { if } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

When there is no ambiguity, we simply write $\pi(\omega \mid \phi)$ to indifferently refer to $\pi\left(\omega \mid_{m} \phi\right)$ or $\pi\left(\omega \mid_{*} \phi\right)$.

The compact representation, in form of a graphical model, associated with a possibility distribution is known as possibilistic networks. As in Bayesian networks, a possibilistic network denoted $\mathcal{P N}=\left\langle G, \Theta>\right.$ is defined by two components:

- A graphical component $G$ : a directed acyclic graph (DAG) where each node represents a discrete variable (from the set of variables $V=\left\{X_{1}, . ., X_{n}\right\}$ ) and edges encode independence relations between variables.

- A numerical component $\Theta$ : a set of local normalized possibility distributions $\Theta_{i}=\pi_{\mathcal{P N}}\left(X_{i} \mid \operatorname{par}\left(X_{i}\right)\right)$ of each node $X_{i}$ given its parents $\operatorname{par}\left(X_{i}\right)$, where the normalized condition is defined by:

$$
\forall u_{i j} \in D_{\operatorname{par}\left(X_{i}\right)} \max _{x_{i} \in D_{X_{i}}} \pi_{\mathcal{P N}}\left(x_{i} \mid u_{i j}\right)=1
$$

The semantics associated with a possibilistic network is a joint possibility distribution obtained using a so-called chain rule. As there are two definitions of conditioning, there are also two definitions of chain rule that compute a joint distribution. We denote by $\mathcal{P N}_{m}$ (respectively $\mathcal{P N}_{*}$ ) a min-based (respectively a product-based) possibilistic network. The possibilistic chain rule for these networks is defined as:

$$
\begin{gathered}
\pi_{\mathcal{P N}_{m}}\left(X_{1}, . ., X_{n}\right)=\min _{i=1, . ., n} \pi_{\mathcal{P N}_{m}}\left(X_{i} \mid m \operatorname{par}\left(X_{i}\right)\right) \\
\text { and } \\
\pi_{\mathcal{P N}_{*}}\left(X_{1}, . ., X_{n}\right)=\prod_{i=1, . ., n} \pi_{\mathcal{P N}_{*}}\left(X_{i} \mid * \operatorname{par}\left(X_{i}\right)\right)
\end{gathered}
$$

where $\Pi$ is the product operator.
Example 1 Figure 1 is an example of a possibilistic network on the set of boolean variables $V=\{A, B, C, D\}$. The domains of each variable $X$ of $V$ is simply represented by the two values $x$ and $\neg x$.
![img-0.jpeg](img-0.jpeg)

Figure 1: Example of a possibilistic network $\mathcal{P N}$ over four boolean variables.

Again, when there is no ambiguity, we simply write $\mathcal{P N}$ to indifferently refer to $\mathcal{P N}_{m}$ or $\mathcal{P N}_{*}$.

# 3 Related works and motivations 

Possibilistic graphical models offer some advantages over probabilistic ones especially for modeling and reasoning with qualitative and incomplete uncertainty. Moreover, possibilistic graphical models also offer nice features regarding practical and computational aspects. This section illustrates two examples of features when it comes to modeling complex problems.

### 3.1 Probability underflow/undistinguishable likelihoods

In many real-world problems (eg. forecasting [28], simulation of physical [1] or biological systems $[9,25]$, etc.) there is need to model a sequential or more generally a dynamic system with many variables over a long period of time. Inference typically consists in computing the likelihood of an outcome or any event of interest given an input. The problem then is that drawing inferences for a long sequence leads inevitably to what is called probability underflow problem due to propagating a long series of small probabilities (indeed, the computer representation of numbers does not allow to represent extremely small probabilities and rounds them to zero). As a consequence, two events with relatively different likelihoods will be associated to equal likelihoods. Of course, an alternative and very common approach is to use log likelihood values rather than computing likelihood itself but then over long sequences one can encounter the overflow problem. Possibilistic propagation thanks to the use of idempotent operators will not encounter such a problem.

### 3.2 High computational complexity

Inference in probabilistic models is a hard task in the general case. In particular, the decision problem associated with $M A P$ is $N P^{P P}$-complete (see $[14,16]$ for more details on complexity issues in Bayesian and credal networks). As said in the introduction, it is important to note that while the complexity results regarding inference in probabilistic networks are well-established [15], there is, to the best of our knowledge, no systematic study of such issues for possibilistic networks (except a study of complexity in possibilistic influence diagrams [22]). Some probabilistic network inference algorithms have already been adapted from the probabilistic setting and seem to show the same complexity. Among the first works on inference in possibilistic graphical models we mention [19] dealing with inference in hypergraphs. Most of the works are more or less direct adaptations of probabilistic networks inference algorithms. For example, a possibilistic elimination variable algorithm can be found in [5] in the context of possibilistic network classifiers. In [8], a possibilistic counterpart of the well-known Message passing algorithm is proposed. A direct adaptation of the Junction tree algorithm in the possibilistic setting is presented in [7]. Possibilistic networks could also be used to approximate inference models of some imprecise probabilistic models. For instance, in [3], an approach based on probability-possibility transformations is proposed to perform approximate

$M A P$ inference in credal networks where $M A P$ inference is very hard [15]. Clearly, modeling and reasoning with complex problems involving many variables will not be tractable unless strong assumption are made regarding the structure of the network. One of the main results of this paper is to show that querying possibilistic networks has a lower complexity than querying probabilistic ones making the former more appropriate for modeling and reasoning with complex problems.

# 4 Inference in possibilistic networks 

In this paper, we investigate two of the most common types of queries when reasoning with graphical models, that are MAP inference and MPE inference. MAP queries require searching for the most plausible instantiation of query variables $Q$ given an evidence $e$ (an instantiation of a set of variables $E$ ). While $M P E$ queries search for the most plausible explanation of an evidence $e$. More formally,
$M A P$ query: Let $\mathcal{P N}$ be a possibilistic network over the set of variables $V$, $Q \subset V$ be a set of query variables and $E \subset V$ be a set of evidence variables with $Q \cap E=\emptyset$. Then, given an evidence $E=e$, the aim is to compute the most plausible instantiation $q$ of $Q$ given the evidence $e$. More formally, MAP queries aim to compute

$$
\underset{q \in D_{Q}}{\operatorname{argmax}}\left(\Pi_{\mathcal{P N}}\left(q \mid_{\otimes} e\right)\right)
$$

where $\left.\right|_{\otimes}$ is either min-based or product-based conditioning.
$M P E$ query: Let $\mathcal{P N}$ be a possibilistic network over the set of variables $V$, $E \subset V$ be a set of evidence variables. We denote $X$ the set of remaining variables $(X=V \backslash E)$. Then, given an evidence $E=e, M P E$ query compute the most plausible instantiation $x$ of $X$ compatible with the evidence $e$. Namely ${ }^{1}$ :

$$
\underset{x \in X}{\operatorname{argmax}}\left(\Pi_{\mathcal{P N}}(x, e)\right)
$$

In the case of a MAP query, the problem can be reduced to finding the most plausible assignment of query variables $Q$ compatible with the evidence $e$. More precisely, using the maximum property of possibility measures allows us to rewrite Equation (5) as follows:

$$
\underset{q \in D_{Q}}{\operatorname{argmax}}\left(\Pi_{\mathcal{P N}}(q, e)\right)
$$

This is formally stated in the following proposition.

[^0]
[^0]:    ${ }^{1}$ Note that $\Pi_{\mathcal{P N}}(x, e)$ is the possibility degree of the conjunction of $x$ and $e$, especially since $X \cap E=\emptyset$. Another notation commonly used is $\Pi_{\mathcal{P N}}(x \wedge e)$.

Proposition 1 Given a possibilistic network $\mathcal{P N}, Q$ the set of query variables and an evidence $e$ (an instantiation of variables $E$ ), we have:

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)=\underset{q \in D_{Q}}{\operatorname{argmax}}\left(\Pi_{\mathcal{P N}}(q, e)\right)
$$

for both min-based and product-based conditioning rule.

# Proof 1 

- Let us start with the min-based conditioning. Given a possibilistic network $\mathcal{P N}_{m}$ over $V$ and let $Q$ and $E$ be two subsets of $V$ (s.t. $Q \cap E=\emptyset$ ). Then, computing $\operatorname{argmax}_{q \in D_{Q}}(\Pi(q \mid e))$ is equivalent to searching the instantiation $q$ such that $\Pi(q \mid e)=1$. By definition of the min-based conditioning, $\Pi(q \mid e)=1$ if $\Pi(q, e)=\Pi(e)$. Assume that $\operatorname{argmax}_{q \in D_{Q}}(\Pi(q, e))$ is $q^{\prime}$ then since $\Pi(e)=\max _{\omega \vDash e} \pi(\omega)$ or said otherwise $\Pi(e)=\max _{q \in D_{Q}} \Pi(q, e)$ which is given by $\Pi\left(q^{\prime}, e\right)$.
- Let us now consider product-based conditioning. In the same way, since the possibilistic network $\mathcal{P N}_{*}$ is normalised then $\forall e \in E, \operatorname{argmax}_{q \in D_{Q}}(\Pi(q \mid e))$ is equivalent to searching the instantiation $q$ such that $\Pi(q \mid e)=1$. Which, by definition, is given by $\Pi(q \mid e)=\frac{\Pi(q, e)}{\Pi(e)}$, therefore, $\Pi(q \mid e)=1$ if $\Pi(q, e)=\Pi(e)$. From there, assume that $\operatorname{argmax}_{q \in D_{Q}}(\Pi(q, e))$ is $q^{\prime}$ then since $\Pi(e)=\max _{\omega \vDash e} \pi(\omega)=\Pi\left(q^{\prime}, e\right)$. Thus, $\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)=$ $\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q, e)\right)$.

Given this equivalence, we can focus only on the MAP problem redefined by Equation (7).

## 5 Overview of the solution

In order to analyse the computational complexity of inference in possibilistic networks, we provide first in this section, a reminder of the notions of boolean satisfiability decision problems and a description of the different steps we will take, to prove that MAP inference (resp. MPE inference) is $N P$-complete in possibilistic networks. In particular, the analysis breaks down into showing the hardness and the completeness of the decision problems associated to MAP and MPE queries. Let us first denote each of these decision problems. More precisely ${ }^{2}$,

- We denote by $\pi_{\otimes}$-D-MAP $\left(\mathcal{P N}_{\otimes}, Q, e, t\right)$ the decision problem associated to a MAP query in a possibilistic network (i.e. $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ in product-based possibilistic networks and $\pi_{m}$-D-MAP $\left(\mathcal{P N}_{m}, Q, e, t\right)$ in min-based possibilistic networks)

[^0]
[^0]:    ${ }^{2}$ these decision problems will be formally defined in relevant sections

- We denote by $\pi_{\otimes}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{\otimes}, e, t\right)$ the decision problem associated to a $M P E$ query in a possibilistic network (i.e. $\pi_{*}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{*}, e, t\right)$ in product-based possibilistic networks and $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ in minbased possibilistic networks)

We will also refer to a special case of possibilistic networks that only involve boolean variables and binary possibility degrees 0 or 1 (namely, each conditional event is either fully possible or fully impossible). We call this type of networks Boolean and Binary possibilistic networks, denoted by B\&B possibilistic networks. A joint B\&B possibility distribution is therefore a particular case of a general possibility distribution which is defined over $\{0,1\}$ rather than over then whole unit interval $[0,1]$. Thus it keeps the same properties and the same definition of computations of conditioning and chain rules. The following introduces notations associated with MAP and MPE decision problems defined for B\&B possibilistic networks:

- We denote by $\mathbf{B} \& \mathbf{B}_{\otimes}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{\otimes}}, Q, e\right)$ the decision problem associated to MAP querying a binary and boolean possibilistic network.
- In the same way, we denote by $\mathbf{B} \& \mathbf{B}_{\otimes}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{B \& B_{\otimes}}, e\right)$ the decision problem associated to $M P E$ querying a binary and boolean possibilistic network.

We recall that the operator $\otimes$ can be either the min or product operation.
To show hardness and completeness of MAP and MPE queries, we will provide polynomial-time reductions from some known $N P$-complete problems to our MAP decision problems (resp. MPE decision problems) and conversely.

# 5.1 Background on satisfiability problems 

Let us first recall the basic notions of boolean satisfiability where we only consider formulas that are in conjunctive normal form (this is enough for the purpose of this paper). Let us consider a set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. We denote by $x_{i}$ ( $\neg x_{i}$ respectively) the positive literal (the negative literal respectively) of variable $X_{i}$. A clause $C$ is a disjunction of literals (or a single literal). For instance a clause $C$ would be: $x_{1} \vee \neg x_{2}$.

Definition 1 We define a CNF (Conjunctive Normal Form) formula $\Psi$ as a conjunction of clauses.

An example of a CNF formula is $\left(x_{1} \vee \neg x_{2}\right) \wedge\left(x_{3} \vee \neg x_{2}\right)$. In particular, a 3 CNF is a formula in a conjunctive normal form for which each clause is a disjunction of at most 3 literals.

A CNF formula $\Psi$ is said to be satisfiable (or consistent) if there exists an assignment of all the variables (that we also call an interpretation) that renders $\Psi$ true. Now, we define the boolean satisfiability decision problem CNF-SAT (specified for conjunctive normal form formulas), denoted simply by D-SAT, as follows:

Definition 2 By D-SAT $(\Psi)$ we denote the decision problem associated to determining if there exists an assignment that satisfies $\Psi$. It is defined by:
Input: The input is a formula $\Psi$ given in a conjunctive normal form
Question: The question is whether the formula $\Psi$ satisfiable or not?
The D-3SAT decision problem is defined as:
Definition 3 By D-3SAT $(\Psi)$ we denote the decision problem defined by:
Input: The input is a 3CNF formula, denoted by $\Psi$
Question: The question is whether the formula $\Psi$ satisfiable or not?
Example 2 Let us consider the set of variables $V=\left\{X_{1}, X_{2}, X_{3}, X_{4}\right\}$ and the following $3 C N F \Psi$ over $V$ :

$$
\begin{aligned}
& \left(x_{1} \vee \neg x_{2} \vee x_{3}\right) \wedge \\
& \left(\neg x_{3} \vee \neg x_{2} \vee x_{4}\right)
\end{aligned}
$$

One can check that $\Psi$ is satisfiable. Indeed the assignment (or interpretation) $\omega=x_{1}, x_{2}, \neg x_{3}, \neg x_{4}$ satisfies all clauses. Hence, the answer to the decision problem D-SAT $(\Psi)$ is "yes".

The last problem that we will refer to in this paper is the weighted MaxSAT problem. This problem generalizes the SAT problem: given a formula with non-negative integer weights on each clause, find an assignment of variables that maximizes the sum of the weights of the satisfied clauses. More precisely, we define its associated decision problem as follow:

Definition 4 By D-WMaxSAT $(\Psi, k)$ we denote the decision problem defined by:
Inputs: The input of this problem is composed of two elements :

- $\Psi$ : a weighted CNF formula over $V=\left\{X_{1}, \ldots, X_{n}\right\}$ simply represented by

$$
\Psi=\left\{\begin{array}{c}
\left(C_{1}, \alpha_{1}\right) \\
\left(C_{2}, \alpha_{2}\right) \\
\cdots \\
\left(C_{m}, \alpha_{m}\right)
\end{array}\right\}
$$

where $C_{i}^{\prime} s$ are clauses and $\alpha_{i}^{\prime} s$ are positive integers.

- k: a positive integer

Question: Is there an instantiation of variables $V$ such that the sum of weights of satisfied clauses in $\Psi$ is greater or equal to $k$ ?

Example 3 Let us consider the following weighted CNF formula $\Psi$ over $V=$ $\left\{X_{1}, X_{2}, X_{3}, X_{4}\right\}$ :

$$
\Psi=\left\{\begin{array}{c}
\left(x_{1} \vee \neg x_{2}, 4\right) \\
\left(\neg x_{1} \vee x_{2}, 6\right) \\
\left(\neg x_{3} \vee \neg x_{2} \vee x_{4}, 5\right) \\
\left(x_{5} \vee x_{4} \vee \neg x_{1}, 2\right)
\end{array}\right\}
$$

Let $k=10$. The instantiation of the variables $V$ (or interpretation) $\omega=$ $x_{1}, \neg x_{2}, x_{3}, x_{4}$ satisfies all clauses except $\left(\neg x_{1} \vee x_{2}, 6\right)$. Hence $\sum\left\{\alpha_{i}:\left(C_{i}, \alpha_{i}\right) \in\right.$ $\Psi$ s.t $\left.\omega \models C_{i}\right\}=11 \geq 10$ where $\models$ denotes the propositional logic satisfaction relation. Therefore, the answer to the decision problem D-WMaxSAT $(\Psi, 10)$ is "yes".

# 5.2 Description of the solution 

The following sections provide the proof of the $N P$-completeness of $\pi_{\otimes}$-D-MAP and $\pi_{\otimes}$-D-MPE decision problems. This is done following these steps:

- We first show the $N P$-hardness of $\pi_{m}$-D-MAP and $\pi_{*}$-D-MAP. We will provide a reduction from the D-3SAT decision problem to both $\pi_{m}$-DMAP and $\pi_{*}$-D-MAP decision problems. In this reduction, we use the restricted version, B\&B possibilistic networks, and we will provide intermediary results and the reductions from the D-3SAT decision problem to $\mathbf{B} \& \mathbf{B}_{\otimes}$-D-MAP decision problem.
- We provide a reduction of the $\pi_{m}$-D-MAP decision problem, defined for min-based possibilistic networks, to the D-SAT decision problem (for completeness in min-based possibilistic networks).
- We provide the completeness of the proof by reducing the $\pi_{*}$-D-MAP decision problem, defined for product-based possibilistic networks, to the D-WMaxSAT decision problem.

This concludes the proof for MAP querying possibilistic networks. To tackle the MPE querying of possibilistic networks, we will follow the same steps:

- We show the $N P$-hardness of $\pi_{m}$-D-MPE and $\pi_{*}$-D-MPE with a reduction from the D-3SAT decision problem to $\mathbf{B} \& \mathbf{B}_{\otimes}$-D-MPE decision problem.
- We provide a reduction of the $\pi_{m}$-D-MPE decision problem, defined for min-based possibilistic networks, to the D-SAT decision problem (for completeness in min-based possibilistic networks).
- Lastly, we will focus on reducing the $\pi_{*}$-D-MPE decision problem, defined for product-based possibilistic networks, to the D-WMaxSAT decision problem (for completeness in product-based possibilistic networks).


## 6 Analysis of MAP querying a possibilistic network

In this section, we focus on proving that the decision problem behind MAP inference in possibilistic networks is $N P$-complete. First, we propose, in Subsection 6.1, to reduce the 3SAT decision problem to MAP querying B\&B possibilistic

networks. This shows that the decision problem behind MAP is $N P$-hard. By proving, in Subsections 6.2 and 6.3, that the decision problem associated to MAP inference is also in $N P$, hence we prove that MAP inference is $N P$-complete.

# 6.1 From 3SAT to MAP querying over B\&B possibilistic networks 

In this context, we are faced to only consider two kinds of queries: given $e$ an instantiation of evidence variables $E$, is there an instantiation $q$ of query variables $Q$ such that $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 0$ or such that $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 1$ with $\otimes=m$ for min-based possibilistic setting or $\otimes=*$ for product-based possibilistic setting. The inequality $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 0$ is trivially satisfied since any instantiation $q$ of $Q$ is a solution to the query.

Hence, we will only focus on analyzing the computational complexity of the decision problems $\pi_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{m}}, Q, e, 1\right)$ and $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{*}}, Q, e, 1\right)$.

Example 4 We illustrate the decision problem $\pi$-D-MAP $\left(\mathcal{P N}_{B \& B}, Q, e, 1\right)$ on the B\&B possibilistic network of Figure 2 over the boolean variables $V=\{A, B, C\}$.
![img-1.jpeg](img-1.jpeg)

Figure 2: Example of a B\&B possibilistic network.
Let $Q=\{B\}$ be the set of query variables and $E=\{C\}$ be the set of evidence variables. Assume that $e=c$, then one can check that the answer to the question: is there an instantiation $q$ of $B$ such that $\Pi_{\mathcal{P N}_{B \& B}}(q \wedge c)=1$ ? is "yes". Indeed, we have $\Pi_{\mathcal{P N}_{B \& B}}(b c)=1$ and this is valid independently if we consider the min-based chain rule or the product-based chain rule.

### 6.1.1 Equivalence of the MAP decision problem in min-based B\&B possibilistic networks and product-based B\&B possibilistic networks

Given the definition of a B\&B possibilistic network, the following proposition states that the decision problems $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{m}}, Q, e, 1\right)$ and $\pi_{*}-\mathbf{D}-$ $\operatorname{MAP}\left(\mathcal{P N}_{B \& B_{*}}, Q, e, 1\right)$ are equivalent.

Proposition 2 Let e be an instantiation of evidence variables and $Q$ be a subset of query variables. Let $\mathcal{P N}_{B \& B_{m}}$ and $\mathcal{P N}_{B \& B_{*}}$ be two $B \& B$ possibilistic networks such that $\forall X_{i}, \forall \mu$ an instance of parents of $X_{i}, \pi_{\mathcal{P N}_{B \& B_{m}}}\left(X_{i} \mid \mu\right)=$

$\pi_{\mathcal{P N}_{B \varkappa B \kappa}}\left(X_{i} \mid \mu\right)$. Then the answer to $\pi_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \varkappa B_{m}}, Q, e, 1\right)$ is "yes" if and only if the answer to $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{B \varkappa B_{*}}, Q, e, 1\right)$ is "yes".

Proposition 2 means that the answer to a MAP query in a B\&B possibilistic network does not depend on whether we consider the min-based version of B\&B possibilistic networks or the product-based version one. The proof of Proposition 2 is immediate. It is based on the fact that operators $*$ and min when only applied to possibility degrees 0 and 1 lead to same results. Hence, when only considering binary degrees $\{0,1\}$, then joint distributions associated with $\mathcal{P N}_{m}$ and $\mathcal{P N}_{*}$ are equals. Namely:

Proposition 3 Let $\mathcal{P N}_{B \varkappa B_{m}}$ and $\mathcal{P N}_{B \varkappa B_{*}}$ be two $B \mathcal{B} B$ possibilistic networks such that $\forall X_{i}, \forall \mu$ an instance of parents of $X_{i}, \pi_{\mathcal{P N}_{B \varkappa B_{m}}}\left(X_{i} \mid \mu\right)=\pi_{\mathcal{P N}_{B \varkappa B_{*}}}\left(X_{i} \mid \mu\right)$. Then we have:

$$
\forall \omega \in \Omega, \pi_{\mathcal{P N}_{B \varkappa B_{m}}}(\omega)=\pi_{\mathcal{P N}_{B \varkappa B_{*}}}(\omega)
$$

The proof of Proposition 3 is immediate and follows from the fact that if $a$ and $b$ are either equal to 0 or 1 then $\min (a, b)=a * b$. Hence, the application of min-based chain rule or product-based chain rule leads to same result.

# 6.1.2 Definition of the B\&B possibilistic network associated to a 3CNF 

Now we can tackle the reduction from 3SAT to querying B\&B possibilistic networks. Since we showed that MAP querying B\&B possibilistic networks is the same in min-based or in product-based B\&B possibilistic networks, we can consider in this section the decision problem in the general case, denoted by B\&B-D-MAP. Since $\Pi_{\mathcal{P N}}(q \wedge e) \geq 1$ is trivially equivalent to $\Pi_{\mathcal{P N}}(q \wedge e)=1$ there is no need to specify the threshold $t$. Then we get:

Definition 5 By B\&B-D-MAP $\left(\mathcal{P N}_{B \varkappa B}, Q, e\right)$ we denote the decision problem associated with MAP querying a B $\mathcal{B} B$ possibilistic network that we define by:
Inputs: The input of this decision problem has three components :

- $\mathcal{P N}_{B \varkappa B}$ : a $B \mathcal{B} B$ possibilistic network over $V=\left\{X_{1}, \ldots, X_{n}\right\}$
- e (evidence): an instantiation of a set of observation variables $E$
- $Q$ (query): a set of query variables with $Q \cap E=\emptyset$

Question: The question addressed in this decision problem is : is there an instantiation $q$ of variables $Q$ such that $\Pi_{\mathcal{P N}_{B \varkappa B}}(q \wedge e)=1$ ?

We first provide the B\&B possibilistic network associated with a 3CNF formula $\Psi$. This reduction takes inspiration from the probabilistic reduction provided in [11] and used to prove the fact that probabilistic inference in belief networks is $N P$-hard. More precisely, the B\&B possibilistic network associated with a 3CNF is given by the following definition.

Definition 6 Let $\Psi=C_{1} \wedge C_{2} \wedge \ldots \wedge C_{m}$ be a 3CNF formula. Let $V=$ $\left\{X_{1}, \ldots, X_{n}\right\}$ be the set of propositional variables appearing in $\Psi$. The $B \mathcal{B} B$ possibilistic network associated with $\Psi$, denoted by $\mathcal{P N}_{\Psi}$ is defined as follows:

1. Representing propositional variables: For each propositional symbol $X_{i}$ appearing in $\Psi$, we create a rooted boolean node variable, also and simply denoted by $X_{i}$, in the graph (with two values $x_{i}$ and $\neg x_{i}$ ). Each rooted variable $X_{i}$ is associated with a local uniform binary possibility distribution defined by: $\pi_{\mathcal{P N}_{\Psi}}\left(x_{i}\right)=1$ and $\pi_{\mathcal{P N}_{\Psi}}\left(\neg x_{i}\right)=1$.
2. Modeling the satisfaction of a clause $C_{j}$ : For each clause $C_{j}$ of $\Psi$, we create a conditional node variable, again simply denoted $C_{j} . C_{j}$ is a boolean variable, its two values are denoted by $c_{j}$ and $\neg c_{j}$. Parents of $C_{j}$ are the rooted variables $X_{i}$ that are involved in $C_{j}$. Each conditional node variable $C_{j}$ is associated with a conditional possibility distribution given by: $\forall u_{j k}$ an instance of parents of $C_{j}$ :

$$
\begin{gathered}
\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{j k}\right)=\left\{\begin{array}{ll}
1, & \text { if } u_{j k} \models C_{j} \\
0, & \text { otherwise. }
\end{array}\right. \\
\pi_{\mathcal{P N}_{\Psi}}\left(\neg c_{j} \mid u_{j k}\right)=\left\{\begin{array}{ll}
0, & \text { if } u_{j k} \models C_{j} \\
1, & \text { otherwise. }
\end{array}\right.
\end{gathered}
$$

where $u_{j k}$ is an instantiation of the parents of $C_{j}$, namely the instantiation of variables $X_{i}$ involved in $C_{j}$ and $u_{k} \models C_{j}$ means that the instantiation $u_{k}$ satisfies the clause $C_{j}$.
3. Modeling the satisfaction of the 3CNF formula $\Psi$ : Lastly, we add a single boolean node denoted by $E_{\Psi}$, which represents the satisfiability of the overall formula $\Psi$. Its values are denoted by $e_{\Psi}$ and $\neg e_{\Psi}$. It has all nodes $C_{j}^{\prime}$ s as parents. The conditional possibility distributions associated with $E_{\Psi}$ are as follow:

$$
\begin{gathered}
\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid C_{1} \wedge . . \wedge C_{m}\right)=\left\{\begin{array}{ll}
1, & \text { if } \forall C_{j}, C_{j}=c_{j} \\
0, & \text { otherwise }\left(\exists j \in\{1 . . m\} \text { s.t. } C_{j}=\neg c_{j}\right)
\end{array}\right. \\
\pi_{\mathcal{P N}_{\Psi}}\left(\neg e_{\Psi} \mid C_{1} \wedge . . \wedge C_{m}\right)=\left\{\begin{array}{ll}
0, & \text { if } \forall C_{j}, C_{j}=c_{j} \\
1, & \text { otherwise }
\end{array}\right.
\end{gathered}
$$

The reduction (from 3SAT clauses to a B\&B possibilistic network) given by Definition 6 is done in polynomial time. Its space complexity is also polynomial with respect to the size of the formula.

Example 5 Let us consider the 3CNF $\Psi$ of Example 2.
Following Definition 6, the $B \mathcal{B} B$ possibilistic network $\mathcal{P N}_{\Psi}$, associated with $\Psi$, consists of three levels of nodes. The first level of nodes represents the set of variables. In this example we have the first level containing the nodes $X_{1}, X_{2}, X_{3}$ and $X_{4}$ as depicted in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3: First level of nodes in $\mathcal{P N}_{\Psi}$.
![img-3.jpeg](img-3.jpeg)

Figure 4: First two levels of nodes $X_{i}$ and $C_{j}$ in $\mathcal{P N}_{\Psi}$.

The second level of nodes has 2 nodes $C_{1}$ and $C_{2}$ with local distributions as illustrated in Figure 4. Note that in local distributions of Figures 4 and 5 we denote by _ _ the remaining instantiations of $\operatorname{par}\left(C_{j}\right)$ and $\operatorname{par}\left(E_{\Psi}\right)$.

By adding the last node $E_{\Psi}$ representing the 3CNF formula, we obtain the final binary possibilistic network, given in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5: B\&B possibilistic network $\mathcal{P N}_{\Psi}$ obtained from the 3CNF formula $\Psi$ given in Example 2.

# 6.1.3 Reduction from 3SAT problem to B\&B-D-MAP problem 

Theorem 1 provides the reduction from the decision problem $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ into $\mathbf{B} \& \mathbf{B}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi}, Q, e\right)$. The input $e$ is let to $e_{\Psi}$ while $Q$ is set to the remaining variables in $\mathcal{P N}_{\Psi}$ (namely, $\left.\left(\left\{X_{1}, \ldots, X_{n}\right\} \cup\left\{C_{1}, \ldots, C_{m}\right\}\right) \backslash\left\{E_{\Psi}\right\}\right)$. More formally:

Theorem 1 Let $\Psi$ be a 3CNF formula. Let $\mathcal{P N}_{\Psi}$ be the B\&B possibilistic network given by Definition 6. Let $V_{\mathcal{P N}_{\Psi}}$ be the set of variables in $\mathcal{P N}_{\Psi}$, namely $\left\{X_{1}, \ldots, X_{n}\right\} \cup\left\{C_{1}, \ldots, C_{m}\right\} \cup\left\{E_{\Psi}\right\}$. Then, $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ answer is "yes" if and only if the $\mathbf{B} \& \mathbf{B}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ answers "yes" where D-3SAT is given in Definition 3 and $\mathbf{B} \& \mathbf{B}_{m}-\mathbf{D}-\mathbf{M A P}$ is given by Definition 5 .

## Proof 2

* Let us assume that the answer to D-3SAT $(\Psi)$ is "yes". It means that there exists an interpretation or an instantiation of the variables $\left\{X_{1}, \ldots, X_{n}\right\}$, denote by $\omega^{*}$, that satisfies all the clauses in $\Psi$. If $\omega$ is an interpretation and $X$ is a variable then we simply denote by $\omega[X]$ the instance of $X$ present in $\omega$.

Let us construct an interpretation, denoted $\omega_{\mathcal{P N}_{\Psi}}$, of $V_{\mathcal{P N}_{\Psi}}$ such that $\omega_{\mathcal{P N}_{\Psi}} \mid=$ $e_{\Psi}$ and $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=1$. For the variable $E_{\Psi}$, we let $\omega_{\mathcal{P N}_{\Psi}}\left[E_{\Psi}\right]=e_{\Psi}$. For variables $X_{i} \in\left\{X_{1}, \ldots, X_{n}\right\}$ we let $\omega_{\mathcal{P N}_{\Psi}}\left[X_{i}\right]=\omega^{*}\left[X_{i}\right]$. For variables $C_{j} \in\left\{C_{1}, \ldots, C_{m}\right\}$ we simply let $\omega_{\mathcal{P N}_{\Psi}}\left[C_{j}\right]=c_{j}$. Now, let us show that indeed $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=1$

Recall that for all variables $X_{i}$ in $\mathcal{P N}_{\Psi}$, we have $\pi_{\mathcal{P N}_{\Psi}}\left(X_{i}\right)=1$. Since $\omega^{*}$ satisfies all clauses, then for all variables $C_{j}$ in $\mathcal{P N}_{\Psi}$ (namely, the set of nodes representing the clauses), we have $\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{j k}\right)=1$ where $\omega^{*} \mid=u_{j k}$. Lastly, the variable $E_{\Psi}=e_{\Psi}$ when all $C_{j}^{\prime} s$ are set to $c_{j}^{\prime} s$ respectively have a possibility degree of $1\left(\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid c_{1} \wedge \ldots \wedge c_{m}\right)=1\right)$.

Therefore, using the min-based chain rule, we have

$$
\begin{aligned}
\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)= & \min \left\{\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid c_{1} \wedge \ldots \wedge c_{m}\right)\right. \\
& \left.\min _{j=1, \ldots, m, \omega_{\mathcal{P N}_{\Psi}} \mid=u_{c_{j}}} \pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{c_{j}}\right)\right. \\
& \left.\left.\min _{i=1, \ldots, n, \omega_{\mathcal{P N}_{\Psi}} \mid=X_{i}} \pi_{\mathcal{P N}_{\Psi}}\left(X_{i}\right)\right)\right\} \\
= & 1
\end{aligned}
$$

where $u_{c_{j}}$ is the instance parents of $C_{j}$ such that $\omega_{\mathcal{P N}_{\Psi}} \mid=u_{c_{j}}$. Therefore, defining $q$ as the instantiation of $Q$ satisfied by $\omega_{\mathcal{P N}_{\Psi}}$ we have $\Pi_{\mathcal{P N}_{\Psi}}\left(q \wedge e_{\Psi}\right)=1$, hence $\mathbf{B} \& \mathbf{B}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ is "yes".

* Let us assume that the answer to D-3SAT $(\Psi)$ is "no". Hence, whatever the considered interpretation $\omega_{\mathcal{P N}_{\Psi}}$ where $\omega_{\mathcal{P N}_{\Psi}} \mid=e_{\Psi}$ there exists at least $C_{j}$ such that $\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{c_{j}}\right)=0$ with $\omega_{\mathcal{P N}_{\Psi}} \mid=u_{c_{j}}$. Hence, $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=0$. So using the min operator of the chain rule, we obtain that $\Pi_{\mathcal{P N}_{\Psi}}\left(q \wedge e_{\Psi}\right)=0$ for all instantiation $q$ of $Q$. Hence, $\mathbf{B} \& \mathbf{B}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ is "no".

By this reduction we have shown that MAP querying possibilistic network is $N P$-hard. In addition to this proof, we provide the completeness of $\pi_{m}$ -D-MAP and $\pi_{*}$-D-MAP. One can either show their membership to $N P$ or provide reductions from $\pi_{m}$-D-MAP and $\pi_{*}$-D-MAP to SAT and WMAXSAT decision problems. In the following, we adopt the second option. Indeed, the proposed reductions can be used as useful transformations for implementation of MAP queries in possibilistic networks using SAT solvers.

# 6.2 From MAP querying min-based possibilistic networks to SAT 

In this subsection, we no longer restrict ourselves to binary possibility distributions. Namely, (conditional) possibility degrees can take any value in the unit interval $[0,1]$. However, for the sake of simplicity, we still only consider boolean variables. This is not a restriction and the proof can be adapted by encoding a non-boolean variable by a set of boolean variables. We propose to reduce the decision problem $\pi_{m}$-D-MAP to the decision problem D-SAT.

We now formally define the decision problem associated with a MAP query in min-based possibilistic networks, denoted $\pi_{m}$-D-MAP. It is given by the following:

Definition 7 By $\pi_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{m}, Q, e, t\right)$ we denote the decision problem associated with MAP querying min-based possibilistic networks that we define by:
Input: The input of this decision problem is composed of four elements :

- $\mathcal{P N}_{m}$ : a min-based possibilistic network
- e (evidence): an instantiation of a set of variables $E$
- $Q$ (query): a set of variables with $Q \cap E=\emptyset$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $q$ of non observed variables $Q$ such that $\overline{\Pi_{\mathcal{P N}_{m}}(q \wedge e)} \geq t$ ?

### 6.2.1 Definition of a CNF formula associated with a min-based possibilistic network

We now define the transformation of a min-based possibilistic network $\mathcal{P N}_{m}$ into a CNF formula, denoted $\Psi_{\mathcal{P N}_{m}, Q, e, t}$. The following gives the definition of the CNF formula associated with the network $\mathcal{P N}_{m}$, the set $Q$, the evidence $e$ (an instantiation of the variables $E$ ) and the positive real number $t$ in $\Psi_{\mathcal{P N}_{m}, Q, e, t}$.

Definition 8 Let $\mathcal{P N}_{m}$ be a min-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $Q$ be a subset of $V, e=e_{1}, \ldots, e_{l}$ be

an instantiation of evidence variables $E$ (with $Q \cap E=\emptyset$ ) and let $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ over the same set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$, is given by:

$$
\begin{aligned}
\Psi_{\mathcal{P N}_{m}, Q, e, t} & =\left\{\left(\neg x_{i} \vee \neg u_{i j}\right): \pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t\right\} \\
& \cup\left\{\mathbf{e}_{\mathbf{k}}: \mathbf{k}=\mathbf{1}, \ldots, \mathbf{l}\right\}
\end{aligned}
$$

Clearly, this reduction is done in polynomial time (and space) with respect to the size of $\mathcal{P N}_{m}$.

Example 6 Let us consider the possibilistic network $\mathcal{P N}_{m}$ of Figure 1 over the set of variables $V=\{A, B, C, D\}$. Let $E=\{D\}$ be the set of evidence with $e=\{D=d\}$ be an instantiation of $E, Q=\{B, C\}$ be the set of query variables and $t=.5$. Then the CNF $\Psi_{\mathcal{P N}_{m,\{B, C\}, d, .5}}$ given by the transformation of Definition 8 is:

$$
\Psi_{\mathcal{P N}_{m},\{B, C\}, d, .5}=\left\{\begin{array}{c}
(c \vee b) \wedge \\
(d \vee \neg b) \wedge \\
(\neg d \vee b) \wedge \\
(\neg b \vee \neg a) \wedge \\
d
\end{array}\right\}
$$

# 6.2.2 Reduction from a min-based possibilistic network into a CNF 

The following theorem states that $\pi_{m}$-D-MAP can be reduced to D-SAT.
Theorem 2 Let $\mathcal{P N}_{m}$ be a min-based possibilistic network, $Q$ be a subset of query variables, e be an instantiation of evidence variables $E$ and $t$ be a real number in $(0,1]$. Let $\Psi_{P N_{m}, Q, e, t}$ be the CNF formula given by Definition 8. Then, $\pi_{m}$-D-MAP $\left(\mathcal{P N}_{m}, Q, e, t\right)$ answers "yes" if and only if D-SAT $\left(\Psi_{\mathcal{P N}_{m}, Q, e, t}\right)$ answers "yes" where $\pi_{m}$-D-MAP is given by Definition 7 and D-SAT is given by Definition 2.

## Proof 3

* Assume that $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ is satisfiable. This means that there exists an instantiation of all variables, denoted by $\omega^{*}$, that satisfies all clauses of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ including $e=e_{1}, \ldots, e_{l}$. Recall that by construction of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$, if $\left(\neg x_{i} \vee \neg u_{i j}\right) \in$ $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ then we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$. So if $\omega^{*}$ satisfies all clauses in $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ then $\omega^{*}$ falsifies each of the formulas in $\left\{\left(x_{i} \wedge u_{i j}\right):\left(\neg x_{i} \vee \neg u_{i j}\right) \in\right.$ $\left.\Psi_{\mathcal{P N}_{m}, Q, e, t}\right\}$. This means that all conditionals $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)$ used in chain rule for defining $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right)$ have a possibility degree greater or equal to t.Hence, their minimal is also greater or equal to $t$. Therefore, using the min-based chain rule we get $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t$.

Denoting now $q=\omega^{*}[Q]$ the instantiation of the variables $Q$ such that $\omega^{*} \vDash q$, we have $\Pi_{\mathcal{P N}_{m}}(q \wedge e) \geq t$ since $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t, \omega^{*} \models q$ and $\omega^{*} \vDash e$. Hence the answer to $\pi_{m}$-D-MAP $\left(\mathcal{P N}_{m}, Q, e, t\right)$ is also "yes".

* Assume that $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ is unsatisfiable. Then for all instantiation of variables $\omega$ such that $\omega \models e\left(=e_{1} \wedge . . \wedge e_{l}\right)$, there exists at least a clause $C_{i}=\neg x_{i} \vee \neg u_{i j}$ that is falsified by $\omega$ (and hence $\omega \models x_{i} \wedge u_{i j}$ ). Now by construction of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$, we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$, so using the min-based chain rule we have $\forall \omega \models e$, $\pi_{\mathcal{P N}_{m}}(\omega)<t$ and therefore $\forall q \in D_{Q}, \Pi_{\mathcal{P N}_{m}}(q \wedge e)<t$.

We illustrate the above theorem and its proof with an example using a MAP query.

Example 7 Let us consider the CNF formula $\Psi_{\mathcal{P N}_{m},\{B, C\}, d, .5}$, of Example 6, corresponding to the MAP query:

Is there an instantiation $q$ of query variables $\{B, C\}$ such that $\Pi_{\mathcal{P N}_{m}}(q \wedge$ $e) \geq .5$ ?

Namely, the decision problem is $\pi_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{m},\{B, C\}, d, .5\right)$. There exist two models $\neg$ abcd and $\neg a b \neg c d$. Hence, the answer to $\mathbf{D}-\mathbf{S A T}\left(\Psi_{\mathcal{P N}_{m}, Q, e, t}\right)$ is "yes". Lastly, using the min-based chain rule on the possibilistic network of Figure 1, we get $\pi(\neg a b c d)=.6$; hence $\Pi_{\mathcal{P N}_{m}}(b c d)=.6$ which is higher or equal than .5. So the answer to $\pi_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{m},\{B, C\}, d, .5\right)$ is "yes".

This proves that MAP querying a min-based possibilistic network is $N P$ complete. We now tackle the product-based possibilistic setting by providing a reduction from the decision problem $\pi_{*}$-D-MAP to the decision problem D-WMaxSAT, given by Definition 4.

# 6.3 From MAP querying product-based possibilistic networks to WMaxSAT 

In this section, we will consider that the possibility degrees in the possibilistic networks are of the form $2^{-\alpha_{i}}$ (plus 0 and 1 ) where $\alpha_{i}$ 's are positive integers. Having uncertainty degrees of the form $2^{-\alpha_{i}}$ will allow us to easily reduce $\mathcal{P N}_{*}$ to WMaxSAT given the fact that the weights used in WMaxSAT are integers (it is enough to use $-\log _{2}\left(2^{-\alpha_{i}}\right)$ to get positive integers). This assumption is done again for the sake of clarity but the proof can be generalized to other real numbers between 0 and 1 . Note that $\alpha_{i}$ may represent a degree of surprise used in Spohn's ordinal conditional function [29].

Before giving the definition of the transformation, we formally define the decision problem associated to MAP querying a product-based possibilistic network $\pi_{*}$-D-MAP.

Definition 9 By $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ we denote the decision problem associated with MAP querying product-based possibilistic networks that we define by:
Input: The input of this decision problem is composed of four elements :

- $\mathcal{P N}_{*}$ : a product-based possibilistic network
- e (evidence): an instantiation of a set of variables $E$

- $Q$ (query): a set of variables with $Q \cap E=\emptyset$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $q$ of non observed variables $Q$ such that $\prod_{\mathcal{P N}_{*}}(q \wedge e) \geq t ?$

# 6.3.1 Definition of a weighted CNF formula associated to a productbased possibilistic network 

In the following definition, we give the weighted CNF formula associated with a $M \mathcal{M}$ query in product-based possibilistic networks. More precisely, it takes into account the evidence $e=e_{1}, \ldots, e_{l}$ of the set of variables $E$ (of size $|E|=l$ ), the set of query variables $Q$ and the threshold $t$ to produce the associated weighted CNF formula.
Definition 10 Let $\mathcal{P N}_{*}$ be a product-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $Q$ be a subset of $V, e=e_{1}, \ldots, e_{l}$ be an instantiation of evidence variables $E$ (with $Q \cap E=\emptyset$ ) and $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is defined by: $\Psi_{R} \cup \Psi_{0} \cup \Psi_{e}$ where

$$
\begin{aligned}
& \Psi_{R}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=2^{-\alpha_{i}}\right\} \\
& \Psi_{0}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, M\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=0\right\} \\
& \Psi_{e}=\left\{\left(e_{k}, M\right): k=1, \ldots, l\right\}
\end{aligned}
$$

where $M$ is a positive number such that $M>\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$.
$\Psi_{R}$ represents the clauses in $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ such that have possibility degrees of the form $2^{-\alpha_{i}} . \Psi_{0}$ represents the clauses for which the possibility degrees in $\mathcal{P N}_{*}$ are 0 . The information $\Psi_{e}$ represents the clauses added to enforce the evidence. Intuitively, the integer weight $M$ is used for fully certain pieces of information. Besides, $\Psi_{0} \wedge \Psi_{e}$ is of course assumed to be consistent (this reflects the very reasonable assumption that the evidence is somewhat possible).

For the following, we will also denote by $X=\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$ the sum of weights in $\Psi_{R}$.

Example 8 illustrates Definition 10.
Example 8 Let us consider the product-based possibilistic network $\mathcal{P N}_{*}$ of Figure 6. Let $Q=\{B\}$ be a subset of $V$, let $e=\neg c$ be an instantiation of evidence variables $E=\{C\}$ and let $t=2^{-2}$ be the threshold.

Let $M=30$. Then following Definition 10, the weighted CNF formula $\Psi_{\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}}$ is

$$
\Psi_{\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}}=\left\{\begin{array}{c}
(a, 4) \\
(\neg b, 8) \\
(\neg c \vee \neg a \vee \neg b, 7) \\
(c \vee \neg a \vee b, 2) \\
(\neg c \vee a \vee b, 30) \\
(\neg c \vee a \vee \neg b, 30) \\
(\neg c, 30)
\end{array}\right\} \Psi_{R} \Psi_{R}
$$

![img-5.jpeg](img-5.jpeg)

Figure 6: Example of a product-based possibilistic network $\mathcal{P N}_{*}$ over $A, B$ and $C$.

# 6.3.2 Reduction from a product-based possibilistic network to a weighted CNF formula 

Theorem 3 provides the reduction from the decision problem $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{*}, Q, e, t\right)$ into D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$. We will denote by $Z$ the number of possibility degrees, $\pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)$ in $\mathcal{P N}_{*}$ that are equal to 0 (namely, $Z$ is the number of clauses in $\Psi_{0}$ ).

The input $k$ is let to $X+\log _{2} t+M *(Z+|E|)$ while $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is the weighted CNF formula given associated to $\mathcal{P N}_{*}$ given by Definition 10 (we also assume for only sake of simplicity that $t$ is of the form $2^{-\alpha}$ with $\alpha$ an integer). More formally:

Theorem 3 Let $\mathcal{P N}_{*}$ be a product-based possibilistic network. Let $Q$ be a subset of $V$, e be an instantiation of variables $E$ and $t$ be a threshold. Let $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ be the CNF formula given by Definition 10. Then, $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ answers "yes" if and only if D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\log _{2} t+M *(Z+|E|)\right)$ answers "yes" where $\pi_{*}$-D-MAP is given by Definition 7 and D-WMaxSAT is given by Definition 4.

Proof 4 Let us first recall the parameters of the WMaxSAT decision problem, D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$. Namely,

- $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is the weighted CNF formula given by Definition 10.
- $k$ is the threshold for the problem and it is given by:

$$
k=X+\log _{2} t+M *\left(\left(\sum \Pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i}\right)=0\right)+1\right)
$$

where $M$ is defined in Definition 10. The value of $X$ is defined by the sum of weights in $\Psi_{R}: X=\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$.
Recall that $\pi_{*}$-D-MAP decision problem is: Given an instantiation e of evidence variables, is there an instantiation $q$ of query variables $Q$ such that $\Pi(q, e) \geq t ?$

Let us now show that the two decision problems $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{*}, Q, e, t\right)$ and $\mathbf{D}$-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\log _{2} t+M *(Z+|E|)\right)$ are equivalent. Let the query associated to D-WMaxSAT be: Does D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\right.$ $\log _{2} t+M *(Z+1))$ answer "yes"? More precisely, is there an instantiation of all variables that satisfies a subset of clauses in $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ having the sum of the degrees of the satisfied clauses greater or equal to $k$ ?

For the sake of clarity, in this proof, we simply write $\Psi$ instead of $\Psi_{\mathcal{P N}_{*}, Q, e, t}$. * Assume that D-WMaxSAT $(\Psi, k)$ answers "yes". This means that there exists a subset $A \subseteq \Psi$ such that:

- $\left\{\left(\phi_{i}, \alpha_{i}\right) \in A\right\}$ is consistent and
- $\sum_{\left(\phi_{i}, \alpha_{i}\right) \in A} \alpha_{i} \geq k$

Note that we can state that $\left\{\left(e_{k}, M\right): k=1, \ldots, l\right\}$ is included in $A$. Indeed, if some $\left(\phi_{i}, M\right)$ of $\Psi$ is not in $A$ then $\left(\sum_{\left(\phi_{i}, \alpha_{i}\right) \in A} \alpha_{i}\right)$ cannot be greater than $M *(Z+|E|)$. Let us denote by $A^{*}=A \backslash\left\{\left(\phi_{i}, M\right):\left(\phi_{i}, M\right) \in A\right\}$ then we can also state that:

- $\left\{\left(\phi_{i}, \alpha_{i}\right) \in A^{*}\right\}$ is consistent,
- $\sum_{\left(\phi_{i}, \alpha_{i}\right) \in A^{*}} \alpha_{i} \geq X+\log _{2} t$

Let $\omega$ be a model of $\left\{\phi_{i}:\left(\phi_{i}, \alpha_{i}\right) \in A\right\}$ and $\left\{\phi_{i}:\left(\phi_{i}, \alpha_{i}\right) \in A^{*}\right\}$. Since $X=$ $\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi\right.$ and $\left.\alpha_{i} \neq M\right\}$. Then the latter equation implies that:

$$
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \notin A^{*}\right\} \leq-\log _{2} t
$$

This can be rewritten as:

$$
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} \leq-\log _{2} t
$$

It is enough now to consider the following immediate simplified inequalities to get the desirable result.

$$
\begin{array}{rll}
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} & \leq-\log _{2} t \\
-\sum\left\{\log _{2} 2^{-\alpha_{i}}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\} & \leq-\log _{2} t \\
-\log _{2}\left(\ast\left\{2^{-\alpha_{i}}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A, \omega \nvdash \phi_{i}\right\}\right) & \leq-\log _{2} t \\
-\log _{2}\left(\ast\left\{2^{-\alpha_{i}}: \omega \nvdash \neg x_{i} \vee \neg u_{i j}\right\}\right) & \leq-\log _{2} t \\
-\log _{2}\left(\ast\left\{2^{-\alpha_{i}}: \omega \vDash x_{i} \wedge u_{i j}\right\}\right) & \leq-\log _{2} t \\
-\log _{2} \pi_{\mathcal{P N}_{*}}(\omega) & \leq-\log _{2} t \\
\pi_{\mathcal{P N}_{*}}(\omega) & \geq t
\end{array}
$$

with $\omega \vDash e$. Hence the answer to $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{*}, Q, e, t\right)$ is also "yes" by taking $q$ such that $\omega \models q$.

* Assume that D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$ answers "no". Then, for all consistent subset of clauses $A$ that include $\Psi_{0}$ and $\Psi_{e}$ we have

$$
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in A\right\}<k
$$

Let us consider such a subset $A_{*}$. Let $\omega$ be a model of $A^{*}$, then following the same previous steps we have:

$$
\begin{aligned}
\sum\left\{\alpha_{i}:\left(\phi_{i}, \alpha_{i}\right) \in \Psi \backslash A_{*} \text { s.t } \omega \nvdash \phi_{i}\right\} & >-\log _{2} t \\
-\log _{2}\left(*\left\{2^{-\alpha_{i}}: \omega \nvdash \neg x_{i} \vee \neg u_{i j}\right\}\right) & >-\log _{2} t \\
-\log _{2}\left(*\left\{2^{-\alpha_{i}}: \omega \vDash x_{i} \wedge u_{i j}\right\}\right) & >-\log _{2} t \\
-\log _{2} \pi_{\mathcal{P N}_{*}}(\omega) & >-\log _{2} t \\
\pi_{\mathcal{P N}_{*}}(\omega) & <t
\end{aligned}
$$

with $\omega \vDash e$. Hence the answer to $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{*}, Q, e, t\right)$ is also "no".
The next example illustrates Theorem 3.
Example 9 Let us continue Example 8. Let $Q=\{B\}$ and $E=\{C\}$ be the set of query variables and evidence variables respectively. Let us consider the evidence $e=\neg c$. Let $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ be the weighted CNF formula associated to $\mathcal{P N}_{*}$ given by Definition 10. The MAP query over $\mathcal{P N}_{*}$ is:

Is there an instantiation $q$ of the variables $Q$ such that $\Pi_{\mathcal{P N}_{*}}(q, e) \geq$ $2^{-2}$ ?

Hence, the corresponding problem D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$ is given by:
Is there an instantiation of the variables such that the sum of the degrees of the satisfied clauses is greater or equal to $k$ ?

Let us set the values of the variables $X, M$ and $Z: X=21, M=30$, and $Z=2$. Then, $k=X+\log _{2} t+30 *(Z+1)=109$. Given this configuration, D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*},(B), \neg c, 2^{-2}}, 109\right)$ answers "yes". Indeed, it is enough to consider $A$ such that

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

The sum of the weights in $A$ is equal to 109. A model of formulas in $A$ can be $a \neg b \neg c$ for which using the product-based chain rule has a possibility degree of $\Pi_{\mathcal{P N}_{*}}(a \neg b c)=2^{-2}$. Hence, $\pi_{*}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{*},\{B\}, \neg c, 2^{-2}\right)$ answers "yes" as well.

In this section, we have shown that the complexity of MAP inference in possibilistic networks is $N P$-complete. We have also provided the transformations that encode a possibilistic network into a satisfiability problem in order to use the power of SAT solvers. These results are significant as it overrides the complexity for the same queries in Bayesian networks. In the next section, we provide, following the same hypothesis the proof of hardness and completeness for $M P E$ query in possibilistic networks.

# 7 Analysis of MPE querying a possibilistic network 

This section briefly focuses on MPE query in possibilistic networks where we will follow the same steps as for showing the computational complexity of MAP querying.

### 7.1 From 3SAT to MPE querying over B\&B possibilistic networks

In the previous section, we have shown that MAP querying a min-based B\&B possibilistic network and MAP querying a product-based B\&B possibilistic network give the same result. This results is also valid for a MPE query as shown below.

Proposition 4 Let $e$ be an instantiation of evidence variables. Let $\mathcal{P N}_{B \& B_{m}}$ and $\mathcal{P N}_{B \& B_{*}}$ be two $B \mathcal{B} B$ possibilistic networks such that $\forall X_{i}, \forall \mu$ an instance of parents of $X_{i}, \pi_{\mathcal{P N}_{B \& B_{m}}}\left(X_{i} \mid \mu\right)=\pi_{\mathcal{P N}_{B \& B_{*}}}\left(X_{i} \mid \mu\right)$. Then the answer to $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{B \& B_{m}}, e, 1\right)$ is "yes" if and only if the answer to $\pi_{*}-\mathbf{D}-$ $\operatorname{MPE}\left(\mathcal{P N}_{B \& B_{*}}, e, 1\right)$ is "yes".

Proof 5 Assume that $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{B \& B_{m}}, e, 1\right)$ is "yes". This means that there exists an interpretation $\omega$ such that $\pi_{m}(\omega)=1$ and for all conditionals, involved in the computation of $\pi_{m}(\omega), \pi_{m}\left(x_{i} \mid \operatorname{par}\left(x_{i}\right)\right)=1$. By definition of $\mathcal{P N}_{B \& B_{*}}$, we have $\pi_{*}\left(x_{i} \mid \operatorname{par}\left(x_{i}\right)\right)=1$ and using the product-based chain rule, we obtain that $\pi_{*}(\omega)=1$ so $\pi_{*}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{B \& B_{*}}, e, 1\right)$ is "yes". The same reasoning can be used to prove the 'only if' condition.

### 7.1.1 Reduction from 3SAT problem to B\&B-D-MPE problem

In the previous sections, we gave the transformation definition of a 3CNF to a B\&B possibilistic network in the context of a MAP query. In the following, we provide the same definition for a MPE query. We first formally define the B\&B-D-MPE problem.

Definition 11 By B\&B-D-MPE $\left(\mathcal{P N}_{B \& B}, e\right)$ we denote the decision problem associated with MPE querying a Boolean and Binary possibilistic network that we define by:
Input: The input of this decision problem is composed of two elements :

- $\mathcal{P N}_{B \& B_{m}}$ : a B $\mathcal{B} B$ possibilistic network over $V=\left\{X_{1}, \ldots, X_{n}\right\}$ (min-based or product-based)
- e (evidence): an instantiation of a set of observation variables $E$

Question: Is there an instantiation $x$ of variables $X$ such that $\Pi_{\mathcal{P N}_{B \& B}}(x, e)=$ 1 ?

As for MAP inference, we build a B\&B possibilistic network from a 3CNF. Definition 6 given for the MAP inference in the previous section can be reused to transform the 3CNF into a B\&B possibilistic network. Indeed, the difference between MAP and MPE inference in B\&B possibilistic network lies in the presence of a subset of query variables. The set of variables $Q$ is not used in the definition of the transformation.

Theorem 4 provides the reduction from the decision problem D-3SAT( $\Psi$ ) into B\&B-D-MPE $\left(\mathcal{P N}_{\Psi}, e\right)$ where the input $e$ is let to $e_{\Psi}$. More formally:

Theorem 4 Let $\Psi$ be a 3CNF formula. Let $\mathcal{P N}_{\Psi}$ be the B $\mathcal{B B}$ possibilistic network given by Definition 6. Let $V_{\mathcal{P N}_{\Psi}}$ be the set of variables in $\mathcal{P N}_{\Psi}$, namely $\left\{X_{1}, \ldots, X_{n}\right\} \cup\left\{C_{1}, \ldots, C_{m}\right\} \cup\left\{E_{\Psi}\right\}$. Then, D-3SAT $(\Psi)$ answer is "yes" if and only if the B\&B-D-MPE $\left(\mathcal{P N}_{\Psi}, e_{\Psi}\right)$ answers "yes" where D-3SAT is given in Definition 3 and B\&B-D-MPE is given by Definition 11.

The proof of Theorem 4 is the same as the proof of Theorem 1. It is even shorter as we don't have to restrict the model instantiation to the variables in $Q$.

Note that it is clear that $M A P$ is a generalization of $M P E$ where, in $M P E$, $Q$ is set to the remaining variables not used in $E$. This explains why it is easier in this second part to prove that MPE queries in possibilistic networks are $N P$-complete.

# 7.2 From MPE querying a min-based possibilistic network to SAT 

The decision problem associated with a MPE query in min-based possibilistic networks, denoted $\pi_{m}$-D-MPE is defined by:

Definition 12 We denote $\pi_{m}$-D-MPE $\left(\mathcal{P N}_{m}, e, t\right)$ the decision problem associated with MPE querying a min-based possibilistic network. It is defined by: Input: The input of this decision problem is composed of three elements :

- $\mathcal{P N}_{m}$ : a min-based possibilistic network
- e (evidence): an instantiation of a set of variables $E$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $x$ of the variables $X$ such that $\Pi_{\mathcal{P N}_{m}}(x, e) \geq$ $t$ ?

The definition of $\Psi_{\mathcal{P N}_{m}, e, t}$, the CNF formula associated to a min-based possibilistic network for the MPE query with evidence $e$ and threshold $t$ is given by $\Psi_{\mathcal{P N}_{m}, \emptyset, e, t}^{\prime}$ where $\Psi^{\prime}$ is given by definition 8 .

The following theorem states that $\pi_{m}$-D-MPE can be reduced to D-SAT.

Theorem 5 Let $\mathcal{P N}_{m}$ be a min-based possibilistic network, e be an instantiation of evidence variables $E$ and $t$ be a real number in $(0,1]$. Let $\Psi_{P N_{m}, e, t}$ be the CNF formula given by Definition 8 with $Q=\emptyset$. Then, $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ says "yes" if and only if $\mathbf{D}-\mathbf{S A T}\left(\Psi_{\mathcal{P N}_{m}, e, t}\right)$ says "yes" where $\pi_{m}-\mathbf{D}-\mathbf{M P E}$ is given by Definition 12 and D-SAT is given by Definition 2.

Proof 6 We need to prove that when $\Psi_{\mathcal{P N}_{m}, e, t}$ is satisfiable then $\Pi_{\mathcal{P N}_{m}}(x, e) \geq$ $t$ and that when $\Psi_{\mathcal{P N}_{m}, e, t}$ is unsatisfiable then $\Pi_{\mathcal{P N}_{m}}(x, e)<t$ for all assignments of all variables compatible with $e$.

- Assume that $\Psi_{\mathcal{P N}_{m}, e, t}$ is satisfiable. This means that there exists an instantiation of all variables, denoted by $\omega^{*}$, that satisfies all clauses of $\Psi_{\mathcal{P N}_{m}, e, t}$ including $e=e_{1}, \ldots, e_{l}$. Then we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$ by construction of $\Psi_{\mathcal{P N}_{m}, e, t}$. So if $\omega^{*}$ satisfies all clauses in $\Psi_{\mathcal{P N}_{m}, e, t}$ then $\omega^{*}$ falsifies each of the formulas in $\left\{\left(x_{i} \wedge u_{i j}\right):\left(\neg x_{i} \vee \neg u_{i j}\right) \in \Psi_{\mathcal{P N}_{m}, e, t}\right\}$. Thus, all conditionals $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)$ applied in chain rule to compute $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right)$ have a possibility degree greater or equal to $t$. Therefore, $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t$. Hence the answer to $\pi_{m}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{m}, e, t\right)$ is also "yes".
- Assume that $\Psi_{\mathcal{P N}_{m}, e, t}$ is unsatisfiable. Then for all instantiation of variables $\omega$ such that $\omega \models e\left(=e_{1} \wedge . . \wedge e_{l}\right)$, there exists at least a clause $C_{i}=\neg x_{i} \vee \neg u_{i j}$ that is falsified by $\omega$ (and hence $\omega \models x_{i} \wedge u_{i j}$ ). Again by construction of $\Psi_{\mathcal{P N}_{m}, e, t}$, we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$, so using the min-based chain rule we have $\forall \omega \models e, \pi_{\mathcal{P N}_{m}}(\omega)<t$. Hence $\pi_{m}-\mathbf{D}-$ $\operatorname{MPE}\left(\mathcal{P N}_{m}, e, t\right)$ is also "no".


# 7.3 From MPE querying a product-based possibilistic network to WMaxSAT 

The decision problem associated with a MPE query in product-based possibilistic networks, denoted $\pi_{*}$-D-MPE is defined by:

Definition 13 We denote $\pi_{*}$-D-MPE( $\left.\mathcal{P N}_{*}, e, t\right)$ the decision problem associated with MPE querying a product-based possibilistic network. It is defined by: Input: The input of this decision problem is composed of three elements :

- $\mathcal{P N}_{*}$ : a product-based possibilistic network
- e (evidence): an instantiation of a set of variables $E$
- $t$ : a real number in $(0,1]$.

Question: Is there an instantiation $x$ of the variables $X$ such that $\Pi_{\mathcal{P N}_{*}}(x, e) \geq$ $t$ ?

The definition of $\Psi_{\mathcal{P N}_{*}, e, t}$, the CNF formula associated to a product-based possibilistic network for the MPE query with evidence $e$ and threshold $t$ is given by $\Psi_{\mathcal{P N}_{*}, \emptyset, e, t}^{\prime}$ where $\Psi^{\prime}$ is given by definition 10 .

Theorem 6 provides the reduction from the decision problem $\pi_{*}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{*}, e, t\right)$ into D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, e, t}, k\right)$. We denote (in the same way as for the MAP analysis) by $Z$ the number of possibility degrees, $\pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)$ in $\mathcal{P N}_{*}$ that are equal to 0 .

The input $k$ is let to $X+\log _{2} t+M *(Z+|E|)$ while $\Psi_{\mathcal{P N}_{*}, e, t}$ is the weighted CNF formula given associated to $\mathcal{P N}_{*}$ given by Definition 10 where $Q$ is let to the empty set. More formally:

Theorem 6 Let $\mathcal{P N}_{*}$ be a product-based possibilistic network. Let e be an instantiation of variables $E$ and $t$ be a threshold. Let $\Psi_{\mathcal{P N}_{*}, e, t}$ be the CNF formula given by Definition 10. Then, $\pi_{*}-\mathbf{D}-\mathbf{M P E}\left(\mathcal{P N}_{*}, e, t\right)$ answers "yes" if and only if D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, e, t}, X+\log _{2} t+M *(Z+|E|)\right)$ answers "yes" where $\pi_{*}$-D-MPE is given by Definition 7 and D-WMaxSAT is given by Definition 4 .

The proof follows the same reasoning as the proof of Theorem 3.
To summarise Theorems 4,5 and 6 show that the decision problem associated with $M P E$ inference is $N P$-complete for both min-based and product-based possibilistic networks.

# 8 Conclusions 

As stressed out in the motivations, inference in probabilistic models is a hard task in the general case. Indeed, computing MAP queries in Bayesian networks is $N P^{P P}$-complete [16, 27]. This paper provided complexity results for possibilistic networks where MAP inference queries are shown to be $N P$-complete. Especially, these results are valid in both min-based and product-based possibilistic networks. The other main result of this paper is that the complexity of $M P E$ inference is also $N P$-complete. These results proved that possibilistic networks offer interesting advantages for reasoning with uncertain information.

A future work concerns the computational complexity analysis of MAP queries in interval-based possibilistic networks. We believe that our results on MAP queries will still hold in the interval-based possibilistic setting. Since in intervalbased possibilistic logic the complexity of conditioning is the same as the complexity of conditioning a standard possibilistic knowledge base. Among other future works, we also argue that the nice complexity results of possibilistic networks shown in this paper can really benefit for inference in probabilistic credal networks where these latter can be approximated by possibilistic networks by means of imprecise probability-possibility transformations [4, 26].

## 9 Acknowledgments

This work benefited from the support of the project AniAge MSCA-RISE Marie Sklodowska-Curie Research and Innovation Staff Exchange (RISE).
