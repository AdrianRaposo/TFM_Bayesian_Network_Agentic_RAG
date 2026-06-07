![img-0.jpeg](img-0.jpeg)

# THE UNIVERSITY of EDINBURGH

Edinburgh Research Explorer

## **Possibilistic networks: MAP query and computational analysis**

### **Citation for published version:**

Benferhat, S, Tabia, K & Levray, A 2018, Possibilistic networks: MAP query and computational analysis. in *Proceedings of the 30th IEEE Int'l Conference on Tools with Artificial Intelligence (ICTAI'18)*, 2018. Institute of Electrical and Electronics Engineers, Volos, Greece, pp. 916-923, 30th International Conference on Tools with Artificial Intelligence, Volos, Greece, 5/11/18. https://doi.org/10.1109/ICTAI.2018.00142

### **Digital Object Identifier (DOI):**

10.1109/ICTAI.2018.00142

### **Link:**

Link to publication record in Edinburgh Research Explorer

### **Document Version:**

Peer reviewed version

### **Published In:**

Proceedings of the 30th IEEE Int'l Conference on Tools with Artificial Intelligence (ICTAI'18), 2018

### **General rights**

Copyright for the publications made accessible via the Edinburgh Research Explorer is retained by the author(s) and/or other copyright owners and it is a condition of accessing these publications that users recognise and abide by the legal requirements associated with these rights.

### **Take down policy**

The University of Edinburgh has made every reasonable effort to ensure that Edinburgh Research Explorer content complies with UK legislation. If you believe that the public display of this file breaches copyright, please contact openaccess@ed.ac.uk providing details, and we will remove access to the work immediately and investigate your claim.

![img-1.jpeg](img-1.jpeg)

# Possibilistic networks: MAP query and computational analysis 

Salem BENFERHAT, Karim TABIA<br>Centre de Recherche en Informatique de Lens (CRiL)<br>Lens, France<br>\{benferhat,levray,tabia\}@cril.fr

Amélie LEVRAY<br>University of Edinburgh<br>Edinburgh, Scotland<br>alevray@inf.ed.ac.uk


#### Abstract

Possibilistic networks are powerful graphical uncertainty representations based on possibility theory. This paper analyzes the computational complexity of querying min-based and product-based possibilistic networks. It particularly focuses on a very common kind of queries: computing maximum a posteriori explanation (MAP). The main result of the paper is to show that the decision problem of answering MAP queries in both min-based and product-based possibilistic networks is $N P$ complete. Such computational complexity results represent an advantage of possibilistic networks over probabilistic networks since MAP querying is $N P^{N P}$-complete in probabilistic Bayesian networks. We provide the proof based on reduction from the 3SAT decision problem to MAP querying possibilistic networks decision problem. As well as reductions that are useful for implementation of MAP queries using SAT solvers.


Index Terms-Complexity, Possibilistic networks, MAP inference

## I. INTRODUCTION

Probabilistic and possibilistic networks [11], [22], [27] are powerful tools to represent and reason with uncertain information. They allow a compact representation of uncertainty distributions using directed acyclic graphs and independence relations. Despite many similarities with probabilistic networks, possibilistic graphical models offer interesting additional advantages especially for modeling and reasoning with qualitative and incomplete uncertainty. As stressed in [19], some possibility theory particularities may offer interesting gains in inference algorithms. For example, in the ordinal possibilistic setting, there may be meaningful gains where the idempotence property of min and max operators benefit to inference algorithms. Also, recent works [9], [16], [23], [30] involves using possibilistic setting applied to web semantics. In this paper, we provide additional benefits for adopting such tools in terms of inferential computational complexity in the context of possibility theory frameworks ( [15], [18]). Possibility theory is a natural alternative uncertainty theory particularly appropriate when only the plausibility ordering between events is useful. In fact, there are two main definitions of possibility theories. The first one is called min-based possibility theory. In this setting, the unit interval $[0,1]$, used for assessing the uncertainty degrees of events, is viewed as an ordinal scale. Hence, only the minimum and maximum operators are used for defining uncertainty measures. This contrasts with the second definition of possibility theory, called
product-based possibility theory, where the unit interval is used in the general sense.

This paper focuses on one of the most important inference task in graphical models which is computing maximum a posteriori explanation (MAP). One of the major result of this paper is to show that querying possibilistic networks has a lower complexity than querying probabilistic networks. More precisely, we show that the decision problem associated with answering MAP queries in possibilistic networks is $N P$ complete. The proof is provided for both min-based and product-based networks and is built progressively. To show the hardness of the decision problem of MAP querying a possibilistic network, we focus on a special type of possibilistic networks called Binary and Boolean possibilistic networks. And we provide a reduction from 3SAT to MAP querying a Binary and Boolean possibilistic network. Finally, we provide reductions MAP querying a possibilistic network to two known $N P$-complete problems: SAT and weighted MaxSAT decision problems.

The rest of this paper is organized as follows: the first section recalls basic notions on possibilistic frameworks. Then, we discuss motivations and related works. The third section introduces the decision problems of MAP query in possibilistic networks and presents an overview of the solution to prove the complexity results of the decision problems considered in this paper. The remaining sections present different polynomialtime reductions used in this paper.

## II. BACKGROUND NOTIONS

This section provides a brief refresher on possibility theory (for more details see [18]) and possibilistic networks ( [2], [7], [20]). One of the basic elements in possibility theory is the notion of possibility distribution, denoted by $\pi$, which is a mapping from the universe of discourse $\Omega$ to the unit interval $[0,1]$. Especially, we consider a finite and discrete universe of discourse. By convention, for a given $\omega \in \Omega, \pi(\omega)=1$ means that $\omega$ is fully possible while $\pi(\omega)=0$ means that it is impossible for $\omega$ to be the real world. $\pi$ is said to be normalized if there is at least an element $\omega \in \Omega$ such that $\pi(\omega)=1$.

Given a possibility distribution $\pi$, one can define a possibility measure, defined for each event $\phi \subseteq \Omega$, by:

$$
\Pi(\phi)=\max \{\pi(\omega): \omega \in \Omega \text { and } \omega \in \phi\}
$$

It expresses to what extent $\phi$ is coherent (compatible) with available information represented by $\pi$.

There are two interpretations of possibility degrees, either the product-based interpretation of the scale $[0,1]$ like in probability theory or the min-based interpretation which consider degrees on an ordinal scale. These two interpretations lead to two different ways to deal with possibility degrees. Indeed, updating degrees given a new evidence, namely conditioning, differs whether the interval $[0,1]$ is just used to rank-order events or not. We call min-based conditioning $\left.\right|_{m}$ [18], [21] the operation defined by: given a possibility distribution $\pi$, and a new evidence $\phi \subseteq \Omega$ (with $\Pi(\phi)>0$ ) the conditional distribution $\pi(. |_{m} \phi)$ is obtained as follows:

$$
\pi\left(\omega_{i} \mid_{m} \phi\right)= \begin{cases}1 & \text { if } \pi\left(\omega_{i}\right)=\Pi(\phi) \text { and } \omega_{i} \in \phi \\ \pi\left(\omega_{i}\right) & \text { if } \pi\left(\omega_{i}\right)<\Pi(\phi) \text { and } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

The product-based conditioning, denoted by $\left.\right|_{*}$, is, as in the probabilistic setting, defined as follows:

$$
\pi\left(\omega_{i} \mid_{*} \phi\right)= \begin{cases}\frac{\pi\left(\omega_{i}\right)}{\Pi(\phi)} & \text { if } \omega_{i} \in \phi \\ 0 & \text { otherwise }\end{cases}
$$

When there is no ambiguity, we simply write $\pi(\omega \mid \phi)$ to indifferently refer to $\pi\left(\omega \mid_{m} \phi\right)$ or $\pi\left(\omega \mid_{*} \phi\right)$.

The compact representation, in form of a graphical model, associated with a possibility distribution is known as possibilistic networks. As in Bayesian networks, a possibilistic network denoted $\mathcal{P N}=<G, \Theta>$ is defined by two components:

- A graphical component $G$ : a directed acyclic graph (DAG) where each node represents a discrete variable (from the set of variables $V=\left\{X_{1}, . ., X_{n}\right\}$ ) and edges encode independence relations between variables.
- A numerical component $\Theta$ : a set of local normalized possibility distributions $\Theta_{i}=\pi_{\mathcal{P N}}\left(X_{i} \mid \operatorname{par}\left(X_{i}\right)\right)$ of each node $X_{i}$ given its parents $\operatorname{par}\left(X_{i}\right)$, where the normalized condition is defined by:

$$
\forall u_{i j} \in D_{\operatorname{par}\left(X_{i}\right)} \max _{x_{i} \in D_{X_{i}}} \pi_{\mathcal{P N}}\left(x_{i} \mid u_{i j}\right)=1
$$

The semantics associated with a possibilistic network is a joint possibility distribution obtained using a so-called chain rule. As there are two definitions of conditioning, there are also two definitions of chain rule that compute a joint distribution. We denote by $\mathcal{P N}_{m}$ (respectively $\mathcal{P N}_{*}$ ) a min-based (respectively a product-based) possibilistic network. The possibilistic chain rule for these networks is defined as:

$$
\pi_{\mathcal{P N}_{\otimes}}\left(X_{1}, . ., X_{n}\right)=\otimes_{i=1, . ., n} \pi_{\mathcal{P N}_{\otimes}}\left(X_{i} \mid{ }_{\otimes} \operatorname{par}\left(X_{i}\right)\right)
$$

where $\otimes=m$ in min-based possibilistic setting and $\otimes=*$ in product-based possibilistic setting.

Example 1. Figure 1 is an example of a possibilistic network on the set of boolean variables $V=\{A, B, C, D\}$.

Again, when there is no ambiguity, we simply write $\mathcal{P N}$ to indifferently refer to $\mathcal{P N}_{m}$ or $\mathcal{P N}_{*}$.
![img-2.jpeg](img-2.jpeg)

Fig. 1. Example of a possibilistic network $\mathcal{P N}$ over four boolean variables.

## III. Related Works and MOTIVATIONS

Possibilistic graphical models offer some advantages over probabilistic ones especially for modeling and reasoning with qualitative and incomplete uncertainty. Moreover, possibilistic graphical models also offer nice features regarding practical and computational aspects. This section illustrates two examples of features when it comes to modeling complex problems.

## A. Probability underflow/undistinguishable likelihoods

In many real-world problems (eg. forecasting [28], simulation of physical [1] or biological systems [8], [24], etc.) there is need to model a sequential or more generally a dynamic system with many variables over a long period of time. Inference typically consists in computing the likelihood of an outcome or any event of interest given an input. The problem then is that drawing inferences for a long sequence leads inevitably to what is called probability underflow problem due to propagating a long series of small probabilities (indeed, the computer representation of numbers does not allow to represent extremely small probabilities and rounds them to zero). As a consequence, two events with relatively different likelihoods will be associated to equal likelihoods. Of course, an alternative and very common approach is to use log likelihood values rather than computing likelihood itself but then over long sequences one can encounter the overflow problem. Possibilistic propagation thanks to the use of idempotent operators will not encounter such a problem.

## B. High computational complexity

Inference in probabilistic models is a hard task in the general case. In particular, the decision problem associated with $M A P$ is $N P^{P P}$-complete (see [12], [14] for more details on complexity issues in Bayesian and credal networks). As said in the introduction, it is important to note that while the complexity results regarding inference in probabilistic networks are wellestablished [13], there is, to the best of our knowledge, no systematic study of such issues for possibilistic networks (except a study of complexity in possibilistic influence diagrams [20]). Some probabilistic network inference algorithms have already been adapted from the probabilistic setting and seem to show the same complexity. Among the first works on inference

in possibilistic graphical models we mention [17] dealing with inference in hypergraphs. Most of the works are more or less direct adaptations of probabilistic networks inference algorithms. For examples, a possibilistic elimination variable algorithm can be found in [5] in the context of possibilistic network classifiers. In [7], a possibilistic counterpart of teh wel-known Message passing algorithm is proposed. A direct adaptation of the Junction tree algorithm in the possibilistic setting is presented in [6]. Possibilistic networks could also be used to approximate inference models of some imprecise probabilistic models. For instance, in [3], an approach based on probability-possibility transformations is proposed to perform approximate MAP inference in credal networks where MAP inference is very hard [13]. Clearly, modeling and reasoning with complex problems involving many variables will not be tractable unless strong assumption are made regarding the structure of the network. One of the main results of this paper is to show that querying possibilistic networks has a lower complexity than querying probabilistic ones making the former more appropriate for modeling and reasoning with complex problems.

## IV. MAP INFERENCE IN POSSIBILISTIC NETWORKS

MAP queries require searching for the most plausible instantiation of query variables $Q$ given an evidence $e$ (an instantiation of a set of variables $E$ ). In this paper, we show that the computational complexity of MAP querying a possibilistic network is $N P$-complete.

## A. Definition of a MAP query

Let $\mathcal{P N}$ be a possibilistic network over the set of variables $V, Q \subset V$ be a set of query variables and $E \subset V$ be a set of evidence variables with $Q \cap E=\emptyset$. Then, given an evidence $E=e$, the aim is to compute the most plausible instantiation $q$ of $Q$ given the evidence $e$. More formally, MAP queries aim to compute

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)
$$

Using the maximum property of possibility measures allows us to rewrite Equation (5) as follows:

Proposition 1. Given a possibilistic network $\mathcal{P N}, Q$ the set of query variables and an evidence $e$ (an instantiation of variables $E$ ), we have:

$$
\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \mid e)\right)=\operatorname{argmax}_{q \in D_{Q}}\left(\Pi_{\mathcal{P N}}(q \wedge e)\right)
$$

for both min-based and product-based conditioning rule.

## B. Decision problem associated with a MAP query

We now formally define the decision problem associated with a MAP query in min-based possibilistic networks, denoted $\pi_{m}$-D-MAP, and in product-based possibilistic networks, denoted $\pi_{*}$-D-MAP. They are given in the following definition where we substitute $\otimes$ by $m$ when considering minbased possibilistic setting and by $*$ when considering productbased possibilistic setting:

Definition 1. By $\pi_{\otimes}$-D-MAP( $\mathcal{P N}_{\otimes}, Q, e, t)$ we denote the decision problem associated with MAP querying possibilistic networks that we define by:
Input:

- $\mathcal{P N}_{\otimes}$ : a possibilistic network (min-based or productbased)
- $e$ (evidence): an instantiation of a set of variables $E$
- $Q$ (query): a set of variables with $Q \cap E=\emptyset$
- $t$ : a real number in $[0,1]$.

Question: Is there an instantiation $q$ of non observed variables $Q$ such that $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq t ?$

## V. OVERVIEW OF THE SOLUTION

We will show that MAP inference in possibilistic networks is $N P$-complete. We will provide polynomial-time reductions from some known $N P$-complete problems to our MAP decision problems and conversely.

## A. Background on satisfiability problems

Let us first recall the basic notions of boolean satisfiability where we only consider formulas that are in conjunctive normal form (this is enough for the purpose of this paper). Let us consider a set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. We denote by $x_{i}$ ( $\neg x_{i}$ respectively) the positive literal (the negative literal respectively) of variable $X_{i}$. A clause $C$ is a disjunction of literals (or a single literal). For instance a clause $C$ would be: $x_{1} \vee \neg x_{2}$. A CNF formula $\Psi$ is a conjunction of clauses (e.g. $C_{1} \wedge C_{2}$ ). In particular, a 3 CNF is a formula in a conjunctive normal form for which each clause is a disjunction of at most 3 literals.

A CNF formula $\Psi$ is said to be satisfiable (or consistent) if there exists an assignment of all the variables (that we also call an interpretation) that renders $\Psi$ true. Now, we define the boolean satisfiability decision problem CNF-SAT (specified for conjunctive normal form formulas), denoted simply by D$\mathbf{S A T}$, as follows:

Definition 2. By D-SAT $(\Psi)$ we denote the decision problem associated to determining if there exists an assignment that satisfies $\Psi$. It is defined by:
Input: $\Psi$ a formula in a conjunctive normal form
Question: Is $\Psi$ satisfiable?
The D-3SAT decision problem is defined as:
Definition 3. By D-3SAT $(\Psi)$ we denote the decision problem defined by:
Input: $\Psi$ a 3CNF formula
Question: Is $\Psi$ satisfiable?
Example 2. Let us consider the set of variables $V=$ $\left\{X_{1}, X_{2}, X_{3}, X_{4}\right\}$ and the following 3CNF $\Psi$ over $V$ :

$$
\begin{aligned}
& \left(x_{1} \vee \neg x_{2} \vee x_{3}\right) \wedge \\
& \left(\neg x_{3} \vee \neg x_{2} \vee x_{4}\right)
\end{aligned}
$$

$\Psi$ is satisfiable. Indeed the assignment (or interpretation) $\omega=$ $x_{1}, x_{2}, \neg x_{3}, \neg x_{4}$ satisfies all clauses. Hence, the answer to the decision problem D-SAT $(\Psi)$ is "yes".

The last problem that we will refer to in this paper is the weighted MaxSAT problem. This problem generalizes the SAT problem: given a formula with non-negative integer weights on each clause, find an assignment of variables that maximizes the sum of the weights of the satisfied clauses. More precisely, we define its associated decision problem as follows:

Definition 4. By D-WMaxSAT $(\Psi, k)$ we denote the decision problem defined by:
Inputs:

- $\Psi$ : a weighted CNF formula over $V=\left\{X_{1}, \ldots, X_{n}\right\}$ simply represented by

$$
\Psi=\left\{\begin{array}{c}
\left(C_{1}, \alpha_{1}\right) \\
\left(C_{2}, \alpha_{2}\right) \\
\ldots \\
\left(C_{m}, \alpha_{m}\right)
\end{array}\right\}
$$

where $C_{i}^{\prime} s$ are clauses and $\alpha_{i}^{\prime} s$ are positive integers.

- $k$ : a positive integer

Question: Is there an instantiation of variables $V$ such that the sum of weights of satisfied clauses in $\Psi$ is greater or equal to $k$ ?

## B. Description of the solution

The following section provide the proof of the $N P$ completeness of $\pi_{m}$-D-MAP and $\pi_{*}$-D-MAP decision problems. We then give tranformations of MAP decision problems in possibilistic networks in order to use SAT solver. The next sections follow these three steps:

- We first show the $N P$-hardness of $\pi_{m}$-D-MAP and $\pi_{*}$ D-MAP. This is done by providing a reduction from the D-3SAT decision problem to both $\pi_{m}$-D-MAP and $\pi_{*}$ D-MAP decision problems. In this reduction, we use a restricted version of possibilistic networks that only involve boolean variables and binary possibility degrees 0 or 1 (namely, each conditional event is either fully possible or fully impossible). We call this type of networks Boolean and Binary possibilistic networks denoted by B\&B possibilistic networks.
- We provide a reduction of the $\pi_{m}$-D-MAP decision problem, defined for min-based possibilistic networks, to the D-SAT decision problem.
- The last section focuses reducing the $\pi_{*}$-D-MAP decision problem, defined for product-based possibilistic networks, to the D-WMaxSAT decision problem.
In particular, we highlight the results of the min-based possibilistic setting.


## VI. From 3SAT to MAP QUERYING OVER B\&B POSSIBILISTIC NETWORKS

As described in the overview of the solution, we propose to first reduce the 3SAT decision problem to MAP querying Boolean and Binary possibilistic networks.

In this context, we are faced to only consider two kinds of queries: given $e$ an instantiation of evidence variables $E$, is there an instantiation $q$ of query variables $Q$ such that $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 0$ or such that $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 1$ with $\otimes=m$ for min-based possibilistic setting or $\otimes=*$ for productbased possibilistic setting. The inequality $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 0$ is trivially satisfied since any instantiation $q$ of $Q$ is a solution to the query.

Hence, we will only focus on analyzing the computational complexity of the decision problems $\pi_{m}$-D$\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{m}}, Q, e, 1\right)$ and $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{B \& B_{*}}, Q, e, 1\right)$.
A. Equivalence of the MAP decision problem in min-based $B \& B$ possibilistic networks and product-based $B \& B$ possibilistic networks

Given the definition of a B\&B possibilistic network, the following proposition states that the decision problems $\pi_{*}$-D$\mathbf{M A P}\left(\mathcal{P N}_{B \& B_{m}}, Q, e, 1\right)$ and $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{B \& B_{*}}, Q, e, 1\right)$ are equivalent.
Proposition 2. Let $e$ be an instantiation of evidence variables and $Q$ be a subset of query variables. Let $\mathcal{P N}_{B \& B_{m}}$ and $\mathcal{P N}_{B \& B_{*}}$ be two $B \& B$ possibilistic networks such that $\forall X_{i}, \forall \mu$ an instance of parents of $X_{i}$, $\pi_{\mathcal{P N}_{B \& B_{m}}}\left(X_{i} \mid \mu\right)=\pi_{\mathcal{P N}_{B \& B_{*}}}\left(X_{i} \mid \mu\right)$. Then the answer to $\pi_{m}$ D-MAP $\left(\mathcal{P N}_{B \& B_{m}}, Q, e, 1\right)$ is "yes" if and only if the answer to $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{B \& B_{*}}, Q, e, 1\right)$ is "yes".

Proposition 2 means that the answer to a MAP query in a B\&B possibilistic network does not depend on whether we consider the min-based version of B\&B possibilistic networks or the product-based version one. This is due to the fact that operators $*$ and min applied to possibility degrees 0 and 1 lead to same results. More precisely,
Proposition 3. Let $\mathcal{P N}_{B \& B_{m}}$ and $\mathcal{P N}_{B \& B_{*}}$ be two $B \& B$ possibilistic networks such that $\forall X_{i}, \forall \mu$ an instance of parents of $X_{i}, \pi_{\mathcal{P N}_{B \& B_{m}}}\left(X_{i} \mid \mu\right)=\pi_{\mathcal{P N}_{B \& B_{*}}}\left(X_{i} \mid \mu\right)$. Then we have:

$$
\forall \omega \in \Omega, \pi_{\mathcal{P N}_{B \& B_{m}}}(\omega)=\pi_{\mathcal{P N}_{B \& B_{*}}}(\omega)
$$

The proof of Proposition 3 is immediate and follows from the fact that if $a$ and $b$ are either equal to 0 or 1 then $\min (a, b)=$ $a * b$.

## B. Reduction from 3SAT problem to B\&B-D-MAP problem

Now we can tackle the reduction from 3SAT to querying B\&B possibilistic networks. Since we showed that MAP querying B\&B possibilistic networks is the same in minbased or in product-based B\&B possibilistic networks, we only consider in this section the decision problem in the minbased possibilistic setting, denoted by $\mathbf{B \& B}_{m}$-D-MAP. Since $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e) \geq 1$ is trivially equivalent to $\Pi_{\mathcal{P N}_{\otimes}}(q \wedge e)=1$ there is no need to specify the threshold $t$. Then we get:
Definition 5. By B\&B ${ }_{m}$-D-MAP $\left(\mathcal{P N}_{B \& B_{m}}, Q, e\right)$ we denote the decision problem associated with MAP querying a minbased Boolean and Binary possibilistic network that we define by:
Inputs:

- $\mathcal{P N}_{B \& B_{m}}$ : a min-based binary and boolean possibilistic network over $V=\left\{X_{1}, \ldots, X_{n}\right\}$

- $e$ (evidence): an instantiation of a set of observation variables $E$
- $Q$ (query): a set of query variables with $Q \cap E=\emptyset$
Question: Is there an instantiation $q$ of variables $Q$ such that $\prod_{\mathcal{P N}_{B \in B_{m}}}(q \wedge e)=1$ ?

We first provide the B\&B possibilistic network associated with a 3CNF formula $\Psi$. This reduction takes inspiration from the probabilistic reduction provided in [10] and used to prove the fact that probabilistic inference in belief networks is $N P$ hard. More precisely, the B\&B possibilistic network associated with a 3CNF is given by the following definition.
Definition 6. Let $\Psi=C_{1} \wedge C_{2} \wedge \ldots \wedge C_{m}$ be a 3CNF formula. Let $V=\left\{X_{1}, \ldots, X_{n}\right\}$ be the set of propositional variables appearing in $\Psi$. The $B \& B$ possibilistic network associated with $\Psi$, denoted by $\mathcal{P N}_{\Psi}$ is defined as follows:

1) Modeling the propositional variables: For each propositional symbol $X_{i}$ appearing in $\Psi$, we create a rooted boolean node variable, also and simply denoted by $X_{i}$, in the graph (with two values $x_{i}$ and $\neg x_{i}$ ). Each rooted variable $X_{i}$ is associated with a local binary possibility distribution defined by: $\pi_{\mathcal{P N}_{\Psi}}\left(x_{i}\right)=1$ and $\pi_{\mathcal{P N}_{\Psi}}\left(\neg x_{i}\right)=1$.
2) Modeling the satisfaction of a clause $C_{j}$ : For each clause $C_{j}$ of $\Psi$, we create a conditional node variable, again simply denoted $C_{j} . C_{j}$ is a boolean variable, its two values are denoted by $c_{j}$ and $\neg c_{j}$. Parents of $C_{j}$ are the rooted variables $X_{i}$ that are involved in $C_{j}$. Each conditional node variable $C_{j}$ is associated with a conditional possibility distribution given by: $\forall u_{j k}$ an instance of parents of $C_{j}$.

$$
\begin{gathered}
\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{j k}\right)= \begin{cases}1, & \text { if } u_{j k} \models C_{j} \\
0, & \text { otherwise }\end{cases} \\
\pi_{\mathcal{P N}_{\Psi}}\left(\neg c_{j} \mid u_{j k}\right)= \begin{cases}0, & \text { if } u_{j k} \models C_{j} \\
1, & \text { otherwise }\end{cases}
\end{gathered}
$$

where $u_{j k}$ is an instantiation of the parents of $C_{j}$, namely the instantiation of variables $X_{i}$ involved in $C_{j}$ and $u_{k} \models C_{j}$ means that the instantiation $u_{k}$ satisfies the clause $C_{j}$.
3) Modeling the satisfaction of the 3CNF formula $\Psi$ : Lastly, we add a single boolean node denoted by $E_{\Psi}$, which represents the satisfiability of the overall formula $\Psi$. Its values are denoted by $e_{\Psi}$ and $\neg e_{\Psi}$. It has all nodes $C_{j}^{\prime} s$ as parents. The conditional possibility distributions associated with $E_{\Psi}$ are as follow:

$$
\begin{gathered}
\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid C_{1} \wedge . . \wedge C_{m}\right)= \begin{cases}1, & \text { if } \forall C_{j}, C_{j}=c_{j} \\
0, & \text { otherwise } \\
& \left(\exists j \in\{1 . . m\}\right. \text { s.t. } \left.C_{j}=\neg c_{j}\right)\end{cases} \\
\pi_{\mathcal{P N}_{\Psi}}\left(\neg e_{\Psi} \mid C_{1} \wedge . . \wedge C_{m}\right)= \begin{cases}0, & \text { if } \forall C_{j}, C_{j}=c_{j} \\
1, & \text { otherwise }\end{cases}
\end{gathered}
$$

The reduction (from 3SAT clauses to a B\&B possibilistic network) given by Definition 6 is done in polynomial time. Its
space complexity is also polynomial with respect to the size of the formula.

Example 3. Let us consider the 3CNF $\Psi$ of Example 2.
Following Definition 6, the B\&B possibilistic network $\mathcal{P N}_{\Psi}$, associated with $\Psi$, consists of three levels of nodes. The first level of nodes represents the set of variables. In this example we have the first level containing the nodes $X_{1}, X_{2}, X_{3}$ and $X_{4}$ as depicted in Figure 2.
![img-3.jpeg](img-3.jpeg)

Fig. 2. First level of nodes in $\mathcal{P N}_{\Psi}$.
The second level of nodes has 2 nodes $C_{1}$ and $C_{2}$ with local distributions as illustrated in Figure 3. Note that in local distributions of Figures 3 and 4 we describe by _ _ _ the remaining instantiations of $\operatorname{par}\left(C_{j}\right)$ and $\operatorname{par}\left(E_{\Psi}\right)$.
![img-4.jpeg](img-4.jpeg)

Fig. 3. First two levels of nodes $X_{i}$ and $C_{j}$ in $\mathcal{P N}_{\Psi}$.
By adding the last node $E_{\Psi}$ representing the 3CNF formula, we obtain the final binary possibilistic network, given in Figure 4.
![img-5.jpeg](img-5.jpeg)

Fig. 4. B\&B possibilistic network $\mathcal{P N}_{\Psi}$ obtained from the 3CNF formula $\Psi$ given in Example 2.

Theorem 1 provides the reduction from the decision problem $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ into $\mathbf{B} \boldsymbol{\mathbf { B }}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi}, Q, e\right)$. The input $e$ is let to $e_{\Psi}$ while $Q$ is set to the remaining variables in $\mathcal{P N}_{\Psi}$ (namely, $\left(\left\{X_{1}, \ldots, X_{n}\right\} \cup\left\{C_{1}, \ldots, C_{m}\right\}\right) \backslash\left\{E_{\Psi}\right\}$ ). More formally:

Theorem 1. Let $\Psi$ be a 3CNF formula. Let $\mathcal{P N}_{\Psi}$ be the $B \& B$ possibilistic network given by Definition 6. Let $V_{\mathcal{P N}_{\Psi}}$ be the set of variables in $\mathcal{P N}_{\Psi}$, namely $\left\{X_{1}, \ldots, X_{n}\right\} \cup\left\{C_{1}, \ldots, C_{m}\right\} \cup$ $\left\{E_{\Psi}\right\}$. Then, $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ answer is "yes" if and only if the $\mathbf{B} \boldsymbol{\mathbf { B }}_{m}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ answers "yes" where $\mathbf{D}-\mathbf{3 S A T}$ is given in Definition 3 and $\mathbf{B} \boldsymbol{\mathbf { B }}_{m}-\mathbf{D}-\mathbf{M A P}$ is given by Definition 5.

## Proof.

* Let us assume that the answer to $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ is "yes". It means that there exists an interpretation or an instantiation of the variables $\left\{X_{1}, \ldots, X_{n}\right\}$, that we denote $\omega^{*}$, that satisfies all the clauses in $\Psi$. If $\omega$ is an interpretation and $X$ is a variable then we simply denote by $\omega[X]$ the instance of $X$ present in $\omega$.

Let us construct an interpretation, denoted $\omega_{\mathcal{P N}_{\Psi}}$, of $V_{\mathcal{P N}_{\Psi}}$ such that $\omega_{\mathcal{P N}_{\Psi}} \models e_{\Psi}$ and $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=1$. For the variable $E_{\Psi}$, we let $\omega_{\mathcal{P N}_{\Psi}}\left[E_{\Psi}\right]=e_{\Psi}$. For variables $X_{i} \in\left\{X_{1}, \ldots, X_{n}\right\}$ we let $\omega_{\mathcal{P N}_{\Psi}}\left[X_{i}\right]=\omega^{*}\left[X_{i}\right]$. For variables $C_{j} \in\left\{C_{1}, \ldots, C_{m}\right\}$ we simply let $\omega_{\mathcal{P N}_{\Psi}}\left[C_{j}\right]=c_{j}$. Now, let us show that indeed $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=1$.

Recall that for all variables $X_{i}$ in $\mathcal{P N}_{\Psi}$, we have $\pi_{\mathcal{P N}_{\Psi}}\left(X_{i}\right)=1$. Since $\omega^{*}$ satisfies all clauses, then for all variables $C_{j}$ in $\mathcal{P N}_{\Psi}$ (namely, the set of nodes representing the clauses), we have $\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{j k}\right)=1$ where $\omega^{*} \models u_{j k}$. Lastly, the variable $E_{\Psi}=e_{\Psi}$ when all $C_{j}^{\prime} s$ are set to $c_{j}^{\prime} s$ respectively have a possibility degree of $1\left(\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid c_{1} \wedge \ldots \wedge c_{m}\right)=1\right)$.

Therefore, using the min-based chain rule, we have

$$
\begin{aligned}
\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)= & \min \left\{\pi_{\mathcal{P N}_{\Psi}}\left(e_{\Psi} \mid c_{1} \wedge \ldots \wedge c_{m}\right),\right. \\
& \min _{\left\{=1, \ldots, m, \omega_{\mathcal{P N}_{\Psi}} \mid=u_{c_{j}} \pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{c_{j}}\right)\right.} \\
& \left.\left.\min _{i=1, \ldots, n, \omega_{\mathcal{P N}_{\Psi}} \models X_{i}} \pi_{\mathcal{P N}_{\Psi}}\left(X_{i}\right)\right)\right\} \\
= & 1
\end{aligned}
$$

where $u_{c_{j}}$ is the instance parents of $C_{j}$ such that $\omega_{\mathcal{P N}_{\Psi}} \models u_{c_{j}}$. Therefore, defining $q$ as the instantiation of $Q$ satisfied by $\omega_{\mathcal{P N}_{\Psi}}$ we have $\Pi_{\mathcal{P N}_{\Psi}}\left(q \wedge e_{\Psi}\right)=1$, hence $\mathbf{B} \boldsymbol{\mathbf { B }}_{m}-\mathbf{D}-$ $\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ is "yes".

* Let us assume that the answer to $\mathbf{D}-\mathbf{3 S A T}(\Psi)$ is "no". Hence, whatever the considered interpretation $\omega_{\mathcal{P N}_{\Psi}}$ where $\omega_{\mathcal{P N}_{\Psi}} \models e_{\Psi}$ there exists at least $C_{j}$ such that $\pi_{\mathcal{P N}_{\Psi}}\left(c_{j} \mid u_{c_{j}}\right)=$ 0 with $\omega_{\mathcal{P N}_{\Psi}} \models u_{c_{j}}$. Hence, $\pi_{\mathcal{P N}_{\Psi}}\left(\omega_{\mathcal{P N}_{\Psi}}\right)=0$. So using the min operator of the chain rule, we obtain that $\Pi_{\mathcal{P N}_{\Psi}}\left(q \wedge e_{\Psi}\right)=0$ for all instantiation $q$ of $Q$. Hence, $\mathbf{B} \boldsymbol{\mathbf { B }}_{m}-$ $\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\Psi},\left(V_{\mathcal{P N}_{\Psi}} \backslash\left\{E_{\Psi}\right\}\right), e_{\Psi}\right)$ is "no".

This proof can be easily extended to multi-valued variables and non-binary domains. Hence, the following corollary:

Corollary 1. Let $\mathcal{P N}_{\otimes}$ be a possibilistic network, $Q$ be a subset of variables, $e$ be an instantiation of evidence variables $E$ (with $E \cap Q=\emptyset$ ) and let $t$ be a real value in $] 0,1]$ with
$\otimes=m$ or $\otimes=*$. Then $\pi_{\otimes}-\mathbf{D}-\mathbf{M A P}\left(\mathcal{P N}_{\otimes}, Q, e, t\right)$ is $N P$ complete.

In particular, the Membership part of the $\pi_{\otimes}$-D-MAP is: Given an instance $q$, it is easy to check if $\Pi(q \wedge e) \geq t$. Indeed, $x=(q, e)$ is a complete instantiation of the network variables, hence the possibility degree $\Pi(q \wedge e)$ is computed in polynomial time (more precisely, in linear time) in the size of the network (number of variables) using the chain rule.

By this reduction we have shown that $M A P$ querying possibilistic network is $N P$-hard. In addition to this proof, we provide converse transformations which are useful for implementation issues of MAP queries in possibilistic networks using SAT solvers.

## VII. FROM QUERYING min-BASED POSSIBILISTIC NETWORKS TO SAT

In this section, we no longer restrict ourselves to binary possibility distributions. Namely, (conditional) possibility degrees can take any value in the unit interval $[0,1]$. However, for the sake of simplicity, we still only consider boolean variables. This is not a restriction and the proof can be adapted by encoding a non-boolean variable by a set of boolean variables. We propose to reduce the decision problem $\pi_{m}$-D-MAP to the decision problem D-SAT.

## A. Definition of a CNF formula associated with a min-based possibilistic network

In this subsection, we define the transformation of a minbased possibilistic network $\mathcal{P N}_{m}$ into a CNF formula, denoted $\Psi_{\mathcal{P N}_{m}, Q, e, t}$. The following gives the definition of the CNF formula associated with the network $\mathcal{P N}_{m}$, the set $Q$, the evidence $e$ (an instantiation of the variables $E$ ) and the real number $t$ in $\Psi_{\mathcal{P N}_{m}, Q, e, t}$.

Definition 7. Let $\mathcal{P N}_{m}$ be a min-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $Q$ be a subset of $V, e=e_{1}, \ldots, e_{l}$ be an instantiation of evidence variables $E$ (with $Q \cap E=\emptyset$ ) and let $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ over the same set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$, is given by:

$$
\begin{aligned}
\Psi_{\mathcal{P N}_{m}, Q, e, t} & =\left\{\left(\neg x_{i} \vee \neg u_{i j}\right): \pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<\mathbf{t}\right\} \\
& \cup\left\{\mathbf{e}_{\mathbf{k}}: \mathbf{k}=\mathbf{1}, \ldots, \mathbf{l}\right\}
\end{aligned}
$$

Clearly, this reduction is done in polynomial time (and space) with respect to the size of $\mathcal{P N}_{m}$.

Example 4. Let us consider the possibilistic network $\mathcal{P N}_{m}$ of Figure 1 over the set of variables $V=\{A, B, C, D\}$. Let $E=\{D\}$ be the set of evidence with $e=\{D=d\}$ be an instantiation of $E, Q=\{B, C\}$ be the set of query variables and $t=.5$. Then the CNF $\Psi_{\mathcal{P N}_{m,\{B, C\}, d, .5}}$ given by the transformation of Definition 7 is:

$$
\Psi_{\mathcal{P N}_{m},\{B, C\}, d, .5}=\begin{gathered}
(c \vee b) \wedge \\
(d \vee \neg b) \wedge \\
(\neg d \vee b) \wedge \\
(\neg b \vee \neg a) \wedge \\
d
\end{gathered}
$$

B. Reduction from a min-based possibilistic network into a CNF

The following theorem states that $\pi_{m}$-D-MAP can be reduced to D-SAT.

Theorem 2. Let $\mathcal{P N}_{m}$ be a min-based possibilistic network, $Q$ be a subset of query variables, $e$ be an instantiation of evidence variables $E$ and $t$ be a real number in $[0,1]$. Let $\Psi_{P N_{m}, Q, e, t}$ be the CNF formula given by Definition 7. Then, $\pi_{m}$-D-MAP( $\left.\mathcal{P N}_{m}, Q, e, t\right)$ says "yes" if and only if D$\mathbf{S A T}\left(\Psi_{\mathcal{P N}_{m}, Q, e, t}\right)$ says "yes" where $\pi_{m}$-D-MAP is given by Definition 1 and D-SAT is given by Definition 2.

## Proof.

$\star$ Assume that $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ is satisfiable. This means that there exists an instantiation of all variables, denoted by $\omega^{*}$, that satisfies all clauses of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ including $e=e_{1}, \ldots, e_{l}$. Recall that by construction of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$, if $\left(\neg x_{i} \vee \neg u_{i j}\right) \in$ $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ then we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$. So if $\omega^{*}$ satisfies all clauses in $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ then $\omega^{*}$ falsifies each of the formulas in $\left\{\left(x_{i} \wedge u_{i j}\right):\left(\neg x_{i} \vee \neg u_{i j}\right) \in \Psi_{\mathcal{P N}_{m}, Q, e, t}\right\}$. This means that all conditionals $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)$ used in chain rule for defining $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right)$ have a possibility degree greater or equal to $t$. Therefore, $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t$.

Denoting now $q=\omega^{*} Q$ the instantiation of the variables $Q$ such that $\omega^{*} \vDash q$, we have $\Pi_{\mathcal{P N}_{m}}(q \wedge e) \geq t$ since $\pi_{\mathcal{P N}_{m}}\left(\omega^{*}\right) \geq t, \omega^{*}=q$ and $\omega^{*} \vDash e$. Hence the answer to $\pi_{m}$-D-MAP( $\left.\mathcal{P N}_{m}, Q, e, t\right)$ is also "yes".

* Assume that $\Psi_{\mathcal{P N}_{m}, Q, e, t}$ is unsatisfiable. Then for all instantiation of variables $\omega$ such that $\omega=e\left(=e_{1} \wedge . . \wedge e_{l}\right)$, there exists at least a clause $C_{i}=\neg x_{i} \vee \neg u_{i j}$ that is falsified by $\omega$ (and hence $\omega \models x_{i} \wedge u_{i j}$ ). And by construction of $\Psi_{\mathcal{P N}_{m}, Q, e, t}$, we have $\pi_{\mathcal{P N}_{m}}\left(x_{i} \mid u_{i j}\right)<t$, so using the min-based chain rule we have $\forall \omega \models e, \pi_{\mathcal{P N}_{m}}(\omega)<t$ and therefore $\forall q \in D_{Q}$, $\Pi_{\mathcal{P N}_{m}}(q \wedge e)<t$.

We illustrate the above theorem and its proof with an example using a MAP query.

Example 5. Let us consider the CNF formula $\Psi_{\mathcal{P N}_{m},\{B, C\}, d, .5}$, of Example 4, corresponding to the MAP query: Is there an instantiation $q$ of query variables $\{B, C\}$ such that $\Pi_{\mathcal{P N}_{m}}(q \wedge e) \geq .5$ ? Namely, the decision problem is $\pi_{m}$-D-MAP( $\left.\mathcal{P N}_{m},\{B, C\}, d, .5\right)$. There exist two models $\neg$ abcd and $\neg a b \neg c d$. Hence, the answer to D-SAT $\left(\Psi_{\mathcal{P N}_{m}, Q, e, t}\right)$ is "yes". And by using the minbased chain rule on the possibilistic network of Figure 1, we get $\pi(\neg a b c d)=.6$ hence $\Pi_{\mathcal{P N}_{m}}(b c d)=.6$ which is higher or equal than .5. So the answer to $\pi_{m}$-D$\mathbf{M A P}\left(\mathcal{P N}_{m},\{B, C\}, d, .5\right)$ is "yes".

For the sake of clarity, we focused on detailing the minbased possibilistic setting reduction. Therefore, the next section only gives the definition of the reduction and the main result stating the equivalence of the result of the two decision problems given the right parameters.

## VIII. FROM QUERYING PRODUCT-BASED POSSIBILISTIC NETWORKS TO WMAXSAT

This section tackles the product-based setting by providing a reduction from the decision problem $\pi_{*}$-D-MAP, given by Definition 1 to the decision problem D-WMaxSAT, given by Definition 4. In this section, we will consider that the possibility degrees in the possibilistic network are of the form $2^{-\alpha_{i}}$ (plus 0 and 1) where $\alpha_{i}$ is a positive integer. Having uncertainty degrees of the form $2^{-\alpha_{i}}$ will allow us to easily reduce $\mathcal{P N}_{*}$ to WMaxSAT given the fact that the weights used in WMaxSAT are integers (it is enough to use $-\log _{2}\left(2^{-\alpha_{i}}\right)$ to get positive integers). This assumption is done again for the sake of clarity but the proof can be generalized to other real numbers between 0 and 1 . Note that $\alpha_{i}$ may represent a degree of surprise used in Spohn's ordinal conditional function [29].
A. Definition of a weighted CNF formula associated to a product-based possibilistic network

In the following definition, we give the weighted CNF formula associated with a MAP query in product-based possibilistic networks. More precisely, it takes into account the evidence $e=e_{1}, \ldots, e_{l}$ of the set of variables $E$ (of size $|E|=l$ ), the set of query variables $Q$ and the threshold $t$ to produce the associated weighted CNF formula.

Definition 8. Let $\mathcal{P N}_{*}$ be a product-based possibilistic network over the set of boolean variables $V=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $Q$ be a subset of $V, e=e_{1}, \ldots, e_{l}$ be an instantiation of evidence variables $E$ (with $Q \cap E=\emptyset$ ) and $t$ be a threshold. Then $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is defined by: $\Psi_{R} \cup \Psi_{0} \cup \Psi_{e}$ where

$$
\begin{aligned}
& \Psi_{R}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=2^{-\alpha_{i}}\right\} \\
& \Psi_{0}=\left\{\left(\neg x_{i} \vee \neg u_{i j}, M\right): \pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)=0\right\} \\
& \Psi_{e}=\left\{\left(e_{k}, M\right): k=1, \ldots, l\right\}
\end{aligned}
$$

where $M>\sum\left\{\alpha_{i}:\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$.
$\Psi_{R}$ represents the clauses in $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ such that have possibility degrees of the form $2^{-\alpha_{i}} . \Psi_{0}$ represents the clauses for which the possibility degrees in $\mathcal{P N}_{*}$ are 0 . And $\Psi_{e}$ represents the clauses added to enforce the evidence. Intuitively, the integer weight $M$ is used for fully certain pieces of information. Besides, $\Psi_{0} \wedge \Psi_{e}$ is of course assumed to be consistent (this reflects the very reasonable assumption that the evidence is somewhat possible).

For the following, we will also denote by $X=\sum\left\{\alpha_{i}\right.$ : $\left.\left(\neg x_{i} \vee \neg u_{i j}, \alpha_{i}\right) \in \Psi_{R}\right\}$ the sum of weights in $\Psi_{R}$.
B. Reduction from a product-based possibilistic network to a weighted CNF formula

Theorem 3 provides the reduction from the decision problem $\pi_{*}$-D-MAP $\left(\mathcal{P N}_{*}, Q, e, t\right)$ into D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, k\right)$. We will denote by $Z$ the number of possibility degrees, $\pi_{\mathcal{P N}_{*}}\left(x_{i} \mid u_{i j}\right)$ in $\mathcal{P N}_{*}$ that are equal to 0 (namely, $Z$ is the number of clauses in $\Psi_{0}$ ).

The input $k$ is let to $X+\log _{2} t+M *(Z+|E|)$ while $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ is the weighted CNF formula given associated to $\mathcal{P N}_{*}$ given by Definition 8 (we also assume for only sake of

simplicity that $t$ is of the form $2^{-\alpha}$ with $\alpha$ an integer). More formally:

Theorem 3. Let $\mathcal{P N}_{*}$ be a product-based possibilistic network. Let $Q$ be a subset of $V$, $e$ be an instantiation of variables $E$ and $t$ be a threshold. Let $\Psi_{\mathcal{P N}_{*}, Q, e, t}$ be the CNF formula given by Definition 8. Then, $\pi_{*}$-D-MAP( $\mathcal{P N}_{*}, Q, e, t)$ answers "yes" if and only if D-WMaxSAT $\left(\Psi_{\mathcal{P N}_{*}, Q, e, t}, X+\log _{2} t+\right.$ $M *(Z+|E|))$ answers "yes" where $\pi_{*}$-D-MAP is given by Definition 1 and D-WMaxSAT is given by Definition 4.

## IX. CONCLUSIONS

As stressed out in the motivations, inference in probabilistic models is a hard task in the general case. Indeed, computing $M A P$ queries in Bayesian networks is $N P^{P P}$-complete [14], [26]. This paper provided crucial complexity results for possibilistic networks where $M A P$ inference queries are shown to be $N P$-complete. Especially, these results are valid in both min-based and product-based possibilistic networks.

A future work concerns the computational complexity analysis of $M A P$ queries in interval-based possibilistic networks. We believe that our results on $M A P$ queries will still hold in the interval-based possibilistic setting. Since in intervalbased possibilistic logic the complexity of conditioning is the same as the complexity of conditioning a standard possibilistic knowledge base.

Among other future works, we also argue that the nice complexity results of possibilistic networks shown in this paper can really benefit for inference in probabilistic credal networks where these latter can be approximated by possibilistic networks by means of imprecise probability-possibility transformations [4], [25].
