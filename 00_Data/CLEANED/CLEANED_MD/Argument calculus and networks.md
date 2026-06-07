# Argument Calculus and Networks 

Adnan Y. Darwiche<br>Cognitive Systems Laboratory<br>Computer Science Department<br>University of California<br>Los Angeles, CA 90024<br>darwiche@cs.ucla.edu


#### Abstract

A major reason behind the success of probability calculus is that it possesses a number of valuable tools, which are based on the notion of probabilistic independence. In this paper, I identify a notion of logical independence that makes some of these tools available to a class of propositional databases, called argument databases. Specifically, I suggest a graphical representation of argument databases, called argument networks, which resemble Bayesian networks. I also suggest an algorithm for reasoning with argument networks, which resembles a basic algorithm for reasoning with Bayesian networks. Finally, I show that argument networks have several applications: Nonmonotonic reasoning, truth maintenance, and diagnosis.


## 1 INTRODUCTION

A major reason behind the success of probability calculus is that it possesses a number of valuable tools, which are based on the notion of probabilistic independence [Pearl, 1988]. In this paper, I identify an intuitive notion of logical independence that makes some of these tools available to a special class of propositional databases.
In particular, I identify in Section 2 a class of propositional databases, called argument databases, and study some of their properties. In Section 3, I identify a notion of logical independence with respect to argument databases and study its properties. In Section 4, I suggest a graphical representation of argument databases, called argument networks, which resemble Bayesian networks. And in Section 5, I suggest an algorithm for reasoning with argument networks, which resembles a basic algorithm for reasoning with Bayesian networks. Finally, I show in Section 6 that argument networks have several applications: Nonmonotonic reasoning, truth maintenance,
and diagnosis. Proofs, omitted due to space limitations, can be found in the full version of this paper.

## 2 ARGUMENT DATABASES

Logical independence, to be defined in Section 3, is based on three notions: argument databases, arguments, and conditional arguments, which are counterparts of probability distributions, probabilities, and conditional probabilities. This section explores these three notions in some detail.

Definition 1 Let $\mathcal{L}$ and $\mathcal{A}$ be two propositional languages over disjoint primitive propositions. An argument database $\Delta$ with respect to $(\mathcal{L}, \mathcal{A})$ is a set of sentences $\alpha \supset \phi$, where sentence $\alpha$ belongs to language $\mathcal{A}$, sentence $\phi$ belongs to language $\mathcal{L}$, and database $\Delta$ does not entail any invalid sentence in language $\mathcal{A} .{ }^{1}$

Example 1 Let $\mathcal{L}$ be a propositional language constructed from primitive propositions rain, sprinkler_on, wet_grass, and wet_shoes. Let $\mathcal{A}$ be another propositional language constructed from primitive propositions $a_{1}, \ldots, a_{6}$. The following is an argument database with respect to $(\mathcal{L}, \mathcal{A})$ :

$$
\begin{aligned}
& a_{1} \supset \text { rain } \\
& a_{2} \supset \text { sprinkler_on } \\
& a_{3} \supset \text { (rain } \supset \text { wet_grass) } \\
& a_{4} \supset \text { (sprinkler_on } \supset \text { wet_grass) } \\
& a_{5} \supset \text { wet_grass } \\
& a_{6} \supset \text { (wet_grass } \supset \text { wet_shoes). }
\end{aligned}
$$

### 2.1 Arguments

The same way that a probability distribution assigns a unique probability to each sentence, an argument database assigns a unique argument (up to logical equivalence) to every sentence:

[^0]
[^0]:    ${ }^{1}$ Any propositional database is an argument database with respect to some pair $(\mathcal{L}, \mathcal{A})$.

Definition 2 Let $\Delta$ be an argument database with respect to $(\mathcal{L}, \mathcal{A})$ and let $\phi$ be a sentence in $\mathcal{L}$. The argument for sentence $\phi$ with respect to database $\bar{\Delta}$, written $\bar{\Delta}(\phi)$, is the weakest sentence $\alpha$ in language $\mathcal{A}$ that together with database $\Delta$ entails sentence $\phi: \Delta \cup\{\alpha\} \models \phi .^{2}$

Any sentence in $\mathcal{A}$ that entails $\Delta(\phi)$ is called an argument for $\phi$. Recall that $\Delta(\phi)$ itself is the argument for $\phi$.

As we shall see later, the argument for a sentence is closely related to the ATMS label of the sentence [Reiter and de Kleer, 1987]. In particular, I will show in Section 6 that the prime implicants for the argument $\Delta(\phi)$ constitute the label for the sentence $\phi$.

Example 2 Consider Example 1. The argument for wet_grass, $\Delta($ wet_grass $)$, is $\left(a_{1} \wedge a_{3}\right) \vee\left(a_{2} \wedge a_{4}\right) \vee$ $a_{5}$. Moreover, each of $a_{1} \wedge a_{3}, a_{2} \wedge a_{4}$, and $a_{5}$ is an argument for wet_grass.

Properties of argument databases are similar to properties of probability distributions:

Theorem 1 An argument database $\Delta$ satisfies:

1. $\Delta($ true $) \equiv$ true,
2. $\Delta($ false $) \equiv$ false,
3. $\Delta(\phi \wedge \psi) \equiv \Delta(\phi) \wedge \Delta(\psi)$, and
4. $\Delta(\phi) \equiv \Delta(\psi)$ when $\phi \equiv \psi$.

Note how true and false in argument calculus play the roles of 1 and 0 in probability calculus.
Although the argument for a conjunction can be computed from the arguments for its conjuncts, the argument for a disjunction cannot be computed from the arguments for its disjuncts in general:

Theorem $2 \Delta(\phi) \vee \Delta(\psi) \models \Delta(\phi \vee \psi)$, but $\Delta(\phi \vee \psi) \not \equiv \Delta(\phi) \vee \Delta(\psi)$.

Example 3 Consider the argument database $\left\{a_{3} \supset\left(\right.\right.$ rain $\supset$ wet_grass $\left.)\right\}$. The argument for $\neg$ rain is false, the argument for wet_grass is false, but the argument for $\neg$ rain $\vee$ wet_grass is $a_{3}$.

The role that conjunction and disjunction play in argument calculus is dual to the role they play in probability calculus. In probability calculus, the probability of a disjunction can be computed from the probabilities of the disjuncts when the disjuncts are logically disjoint. However, to compute the probability of a conjunction one has to appeal to the notion of conditional probability unless the conjuncts

[^0]are independent. In argument calculus, however, the argument for a conjunction can be computed from the arguments for the conjuncts ${ }^{3}$, but to compute the argument for a disjunction one has to appeal to the notion of conditional argument unless the conjuncts are independent. Conditional arguments and independence shall be discussed next.

### 2.2 Conditional arguments

The obvious way to update the argument for $\psi$ after observing some sentence $\phi$ in $\mathcal{L}$ is to compute the argument for $\psi$ with respect to the extended database $\Delta \cup\{\phi\}$. This computation gives the argument for $\phi \supset \psi$ with respect to the database $\Delta$. But this argument includes the argument for $\neg \phi$, which should not count because $\phi$ has been observed. When the argument for $\neg \phi$ is subtracted from the argument for $\phi \supset \psi$, we get the conditional argument for $\psi$ given $\phi$.

Definition 3 The conditional argument for $\psi$ given $\phi$, written $\Delta(\psi \mid \phi)$, is

$$
\Delta(\psi \mid \phi) \stackrel{\text { def }}{=} \Delta(\phi \supset \psi) \wedge \neg \Delta(\neg \phi)
$$

Example 4 Consider the argument database $\left\{a_{1} \supset\right.$ rain $\}$. The argument for $\neg$ rain $\supset$ wet_grass is $a_{1}$, which is also the argument for $\neg$ rain. The conditional argument for wet_grass given $\neg$ rain is $a_{1} \wedge \neg a_{1} \equiv$ false. Therefore, although there is an argument for $\neg$ rain $\supset$ wet_grass, there is no argument for wet_grass given $\neg$ rain.

Although conditional arguments play a central role in defining logical independence, a related class of arguments, called sufficient arguments, plays a central role in computing arguments.

Definition 4 A sufficient argument for $\psi$ given $\phi$, written $\Delta(\phi \rightarrow \psi)$, is an argument that satisfies $\Delta(\psi \mid \phi) \models \Delta(\phi \rightarrow \psi) \models \Delta(\psi \supset \phi)$.
A sufficient argument for $\psi$ given $\phi$ is "sufficient" for computing the argument for $\phi \supset \psi$ once the argument for $\neg \phi$ is computed:

Theorem 3 (Disjunction Rule) $\Delta(\phi \supset \psi) \equiv$ $\Delta(\phi \rightarrow \psi) \vee \Delta(\neg \phi)$.

Example 5 Consider the argument database $\left\{a_{7} \supset \neg\right.$ rain, $a_{3} \supset($ rain $\supset$ wet_grass $\left.)\right\}$. The argument for rain $\supset$ wet_grass is $a_{3} \vee a_{7}$ and the argument for wet_grass given rain is $a_{3} \wedge \neg a_{7}$. It follows that $a_{3}$ is a sufficient argument for wet_grass given rain. Therefore, disjoining $a_{3}$ with the argument for $\neg$ rain gives the argument for rain $\supset$ wet_grass.

[^1]
[^0]:    ${ }^{2}$ Sentence $\alpha$ is weaker than sentence $\beta$ if $\beta$ entails $\alpha$. The argument for a sentence is unique up to logical equivalence.

[^1]:    ${ }^{3}$ The equivalence $\Delta(\phi \wedge \psi) \equiv \Delta(\phi) \wedge \Delta(\psi)$ holds even when the conjuncts $\phi$ and $\psi$ are not logically disjoint. This is because logical conjunction is idempotent; that is, $\alpha \wedge \alpha \equiv \alpha$ for all $\alpha$, which is not true of numeric addition since $a+a \neq a$ in general.

![img-0.jpeg](img-0.jpeg)

Figure 1: ( $A$ stands for $\phi$ and $B$ stands for $\psi$ ). The change that occurs to the argument for $B$ as a result of observing A. From left to right, the above shaded areas are: the argument for $B$, the negative influence of $A$ on $B$, the positive influence of $A$ on $B$, and the conditional argument for $B$ given $A$.

## 3 INDEPENDENCE

The notion of logical independence is based on the relation between arguments and conditional arguments. Consider Figure 1, for example, which depicts the relation between the argument for $\psi$ and the conditional argument for $\psi$ given $\phi$. The two arguments are incomparable in general. The decrease in the argument for $\psi$ after observing $\phi$ is called the negative influence of $\phi$ on $\psi$. And the increase in the argument for $\psi$ after observing $\phi$ is called the positive influence of $\phi$ on $\psi$. The positive influence of $\phi$ on $\psi$ is the disjunction of all arguments for $\phi \supset \psi$ that are neither arguments for $\neg \phi$ nor arguments for $\psi$. And the negative influence of $\phi$ on $\psi$ is the disjunction of all arguments for $\psi$ that are also arguments for $\neg \phi$. More formally:

Definition 5 The positive influence of $\phi$ on $\psi$, written $\Delta(\phi \sim \sim \psi)$, is $\Delta(\phi \supset \psi) \wedge \neg \Delta(\neg \phi) \wedge \neg \Delta(\psi)$. The negative influence of $\phi$ on $\psi$ is $\Delta(\psi \wedge \neg \phi)$.

Example 6 Consider the argument database:

$$
\begin{aligned}
& a_{7} \supset \neg \text { rain } \\
& a_{5} \supset \text { wet_grass } \\
& a_{3} \supset(\text { rain } \supset \text { wet_grass })
\end{aligned}
$$

The negative influence of rain on wet_grass is $a_{5} \wedge a_{7}$ because this will be subtracted from the argument for wet_grass when rain is observed. The positive influence of rain on wet_grass is $a_{3} \wedge \neg a_{5} \wedge \neg a_{7}$ because this will be added to the argument for wet_grass when rain is observed.

When $\Delta(\phi \sim \sim \psi) \equiv$ false, we say that $\phi$ has no positive influence on $\psi$. And when $\Delta(\psi \wedge \neg \phi) \equiv$ false, we say that $\phi$ has no negative influence on $\psi$.

Below are two definitions of independence that are based on positive and negative influence. According to the first definition, a set of propositions $I$ is independent from another set $J$ precisely when no information about propositions $J$ has a positive influence on any information about propositions $I$. According to the second definition, $I$ is independent from $J$ precisely when no information about $J$ has a negative influence on any information about $I$.

Before I state the definitions formally, let me introduce some notation. The symbol $\hat{i}$ denotes a literal, $i$ or $\neg i$, where $i$ is a primitive proposition. The symbol $\hat{I}$ denotes a conjunction of literals $\hat{i}$, where $i$ belongs to $I$. And the symbol $\hat{I}$ denotes a disjunction of literals $\hat{i}$, where $i$ belongs to $I$.

Definition 6 An argument database $\Delta$ finds propositions $I$ +independent from propositions $J$, written $+I n d_{\Delta}(I, J)$, precisely when no $\hat{J}$ has a positive influence on any $\hat{I}$. And $\Delta$ finds propositions $I$ -independent from $J$, written $-I n d_{\Delta}(I, J)$, precisely when no $\hat{J}$ has a negative influence on any $\hat{I}$.

Corollary $1+\operatorname{Ind}_{\Delta}(I, J)$ iff $\Delta(\hat{I} \mid \hat{J}) \models \Delta(\hat{I})$ and $-\operatorname{Ind}_{\Delta}(I, J)$ iff $\Delta(\hat{I}) \models \Delta(\hat{I} \mid \hat{J})$.

Example 7 Consider Example 1. sprinkler_on is +independent of rain, but is -dependent on rain. Moreover, wet_shoes is +dependent on rain.

From here on, I will discuss +independence only.
There is also a notion of conditional +independence in argument calculus. It can be defined in terms of conditional influence, but the following is a simpler definition in terms of conditional arguments.

Definition 7 An argument database $\Delta$ finds propositions $I$ +independent from $J$ given $K$, written $+\operatorname{Ind}_{\Delta}(I, \hat{K}, \hat{J})$, precisely when

$$
\Delta(\hat{I} \mid \hat{K} \wedge \hat{J}) \models \Delta(\hat{I} \mid \hat{K})
$$

Example 8 In Example 1, wet_shoes is +independent of rain given wet_grass.

There are several characterizations of conditional +independence in terms of arguments, conditional arguments, and sufficient arguments. Following is one of these characterizations.

Theorem $4+$ Ind $_{\Delta}(I, K, J)$ iff

$$
\Delta(\hat{K} \supset \hat{I} \vee \hat{J}) \equiv \Delta(\hat{K} \supset \hat{I}) \vee \Delta(\hat{K} \supset \hat{J})
$$

Of most importance among the properties of conditional +independence are the graphoid axioms [Pearl, 1988]:

Theorem 5 Conditional +independence satisfies the following properties:
(a) $+$ Ind $_{\Delta}(I, K, J)$ iff $+$ Ind $_{\Delta}(J, K, I)$, and
(b) $+$ Ind $_{\Delta}(I, K, J)$ and $+$ Ind $_{\Delta}(L, K \cup I, J)$ iff $+$ Ind $_{\Delta}(I \cup L, K, J)$.

## 4 ARGUMENT NETWORKS

An argument network is a graphical representation of an argument database. Figure 2 depicts an argument network, which represents the database of Example 1. Figure 3 depicts another argument network.
An argument network has two components: a directed acyclic graph and a set of tables. Every node in an argument network has a table associated with it. The table has two columns, each corresponding to a state of the associated node. The table also has a number of rows, each corresponding to a state of the node's parents. A table entry at row $\phi$ and column $\psi$ is an argument for $\phi \supset \psi$. For example, the top left entry of the table associated with Node wet_grass, $a_{3} \vee a_{4} \vee a_{5}$, is an argument for rain $\wedge$ sprinkler_on $\supset$ wet_grass.
Following is the formal definition of an argument network in which the symbol $i \circ$ denotes the parents of node $i$.

Definition 8 An argument network is a tuple $(\mathcal{L}, \mathcal{A}, \mathcal{G}, \mathcal{Q})$, where

1. $\mathcal{L}$ and $\mathcal{A}$ are propositional languages over disjoint primitive propositions,
2. $\mathcal{G}$ is a directed acyclic graph over the primitive propositions of language $\mathcal{L}$, and
3. $\mathcal{Q}$ maps each pair $(\hat{i \circ}, \hat{i})$, where $i$ is a node in $\mathcal{G}$, into an argument in $\mathcal{A}$ such that $\mathcal{Q}(\hat{i \circ}, i) \wedge$ $\mathcal{Q}(\hat{\imath \circ}, \neg i) \equiv$ false.

Definition 9 The database corresponding to argument network $(\mathcal{L}, \mathcal{A}, \mathcal{G}, \mathcal{Q})$ is

$$
\{\mathcal{Q}(\hat{\imath \circ}, \hat{\imath}) \supset(\hat{\imath \circ} \supset \hat{\imath}) \mid i \text { is a node in } \mathcal{G}\}
$$

An argument network graphically explicates many of the independences in its corresponding database. The following two theorems elaborate on this and other features.

Theorem 6 Let $(\mathcal{L}, \mathcal{A}, \mathcal{G}, \mathcal{Q})$ be an argument network and let $\Delta$ be its corresponding database. Then

1. $\Delta$ is an argument database,
2. the argument $\mathcal{Q}(\hat{\imath \circ}, \hat{\imath})$ is a sufficient argument for $\hat{\imath}$ given $\hat{\imath \circ}$, and
3. any node in $\mathcal{G}$ is +independent from its nondescendents given its parents.

The first result above says that the database corresponding to an argument network does not entail any invalid; sentence in the language $\mathcal{A}$. The second result says that $\mathcal{Q}(\hat{\imath \circ}, \hat{\imath})$ is entailed by the conditional argument $\Delta(\hat{\imath} \mid \hat{\imath \circ})$ and entails the argument $\Delta(\hat{\imath \circ} \supset \hat{\imath})$. The third result is most interesting because it shows that some independences, which are part of the definition of a Bayesian network, are properties of an argument network. Together with Theorem 5 , this result leads to the following consequential theorem.

Theorem 7 Let $(\mathcal{L}, \mathcal{A}, \mathcal{G}, \mathcal{Q})$ be an argument network and let $I, J, K$ be disjoint sets of nodes in $\mathcal{G}$. If $K d$-separates $I$ from $J$, then $+$ Ind $_{\Delta}(I, K, J)$.

The criterion of $d$-separation is a topological test that is not defined here, but can be found elsewhere [Pearl, 1988].

## 5 COMPUTING ARGUMENTS

A basic algorithm for computing probabilities in Bayesian networks is the well known polytree algorithm [Pearl, 1988; Peot and Shachter, 1991]. Although this algorithm applies to singly connected networks, ${ }^{4}$ it can be extended to multiply connected networks [Horvitz et al., 1989; Pearl, 1988; Suermondt and Cooper, 1988; Peot and Shachter, 1991]. In this section, I present a similar algorithm for computing arguments in singly connected networks, which can be extended to compute arguments in multiply connected networks [Darwiche, 1992].
Given an observation $\delta$, the algorithm computes the argument $\Delta(\delta \supset \hat{\imath})$ for each literal $\hat{\imath}$. From such arguments, one computes the argument for the negated observation $\neg \delta$ using $\Delta(\neg \delta) \equiv \Delta(\delta \supset i) \wedge \Delta(\delta \supset \neg i)$. Then one computes the conditional argument for $\hat{\imath}$ given $\delta$ using $\Delta(\hat{\imath} \mid \delta) \equiv \Delta(\delta \supset \hat{\imath}) \wedge \neg \Delta(\neg \delta)$. In the following theorem, which states the algorithm, the symbol ioj denotes the parents of node $i$ except parent $j$, io denotes the children of node $i$, and $i o j$ denotes the children of node $i$ except child $j$

Theorem 8 Let $(\mathcal{L}, \mathcal{A}, \mathcal{G}, \mathcal{Q})$ be an argument network and let $\Delta$ be its corresponding database. Let $\delta$ be a state of some leaf nodes in $\mathcal{G}$, where each node has only one parent. If $i$ is a non-observed node in $\mathcal{G}$, then $\Delta(\delta \supset \hat{\imath})$ equals $\pi_{i}(\hat{\imath}) \vee \lambda_{i}(\hat{\imath})$, where

$$
\pi_{i}(\hat{\imath}) \stackrel{\text { def }}{=} \bigwedge_{\hat{\imath} \circ} \mathcal{Q}(\hat{\imath \circ}, \hat{\imath}) \vee \bigvee_{\hat{\imath} \circ \mid \equiv j} \pi_{j, i}(\neg \hat{j})
$$

[^0]
[^0]:    ${ }^{4} \mathrm{~A}$ singly connected network has only one undirected path between any two nodes.

![img-1.jpeg](img-1.jpeg)

Figure 2: An argument network. The symbols $R, S, W G$, and $W S$ stand for rain, sprinkler_on, wet_grass, and wet_shoes, respectively.

$$
\begin{aligned}
& \lambda_{i}(\hat{i}) \stackrel{\text { def }}{=} \bigvee_{k \in i \circ} \lambda_{k . i}(\hat{i}), \\
& \pi_{j . i}(\hat{j}) \stackrel{\text { def }}{=} \pi_{j}(\hat{j}) \vee \bigvee_{k \in j \circ i} \lambda_{k . j}(\hat{j}), \\
& \lambda_{k . i}(\hat{i}) \stackrel{\text { def }}{=} \mathcal{Q}(\neg \hat{i}, \neg \hat{k}), \text { if } \delta \models \hat{k} ; \text { and } \\
& \bigwedge_{\hat{k}} \lambda_{k}(\neg \hat{k}) \vee \bigwedge_{k \circ i} \mathcal{Q}(\hat{k \circ i} \wedge \neg \hat{i}, \neg \hat{k}) \vee \bigvee_{k \circ i \models \hat{j}} \pi_{j . k}(\neg \hat{j}),
\end{aligned}
$$

otherwise.
The polytree algorithm is usually explained in terms of a message-passing paradigm in which the pair $\left\langle\pi_{j . i}(j), \pi_{j . i}(\neg j)\right\rangle$ is called the message from node $j$ to its child $i$ and the pair $\left\langle\lambda_{k . i}(i), \lambda_{k . i}(\neg i)\right\rangle$ is called the message from node $k$ to its parent $i$. The computation of the algorithm is then a sequence of message exchanges between nodes in which each node receives and sends one message to each neighbor. Therefore, the number of messages exchanged during the computation is twice the number of arcs in the network, which, for singly connected networks, is one less than the number of nodes.

Beyond its message-passing behavior, the polytree algorithm is well known for its time complexity. Theorem 9 below shows a similar time complexity for the algorithm of Theorem 8, assuming that constructing a disjunction (or conjunction) of $l$ elements requires $l$ units of space and $l$ units of time.

Theorem 9 A non-observed node with $n>0$ parents and $m>0$ children consumes $(n+2) 2^{n+1}+2 m$ space units and a similar number of time units when it sends a child message, and consumes $(n+1) 2^{n+1}+$ $4(m+2)$ space units and a similar number of time units when it sends a parent message.

The theorem shows that the time and space consumed by the algorithm is manageable if the number of parents per node is small. In particular, when
there is one parent per node (the network is a tree), the time of the algorithm and the size of all arguments constructed are linear in both the number of nodes in the network and the number of children per node.

## 6 APPLICATIONS OF ARGUMENT NETWORKS

In this section, I discuss three applications of argument networks: Nonmonotonic reasoning, truth maintenance, and diagnosis. In nonmonotonic reasoning, I show how to compute what needs to be retracted from a database in order to resolve a conflict with an observation. In truth maintenance, I show how to compute the label of a sentence [Reiter and de Kleer, 1987] from its argument. And in diagnosis, I show how to compute the kernel diagnoses [de Kleer et al., 1992] of an observation from the argument for the negated observation.

All three applications are isomorphic at some level of abstraction. Moreover, in all of them, we end up expressing some argument in its prime implicant form. Following is a review of the notion of a prime implicant and the connected notion of a prime implicate.

Definition 10 A conjunctive clause is a conjunction of literals. An implicant for sentence $\psi$ is a satisfiable conjunctive clause that entails $\psi . A$ prime implicant for $\psi$ is a weakest implicant for $\psi$. A disjunctive clause is a disjunction of literals. An implicate of sentence $\psi$ is an invalid disjunctive clause that is entailed by $\psi$. A prime implicate of $\psi$ is a strongest implicate of $\psi$.

### 6.1 Nonmonotonic reasoning

When our beliefs are represented by a propositional database, we are often interested in answering two

![img-2.jpeg](img-2.jpeg)

Figure 3: An argument network representing the circuit on the right corner. This network assumes a particular fault model of digital gates: If a gate is OK, it produces the right output; but if the gate is not OK, it may or may not produce the right output.
types of questions. First, does sentence $\phi$ follow from the database? And second, if $\phi$ follows from the database, and if we observe $\neg \phi$, then what should be removed from the database such that the conflict is resolved? Both of these questions can be answered by appealing to the notion of an argument.
In particular, suppose that we have a database $\Gamma=$ $\left\{\phi_{1}, \ldots, \phi_{n}\right\}$ that is constructed from language $\mathcal{L}$. To answer the above questions, we introduce a primitive proposition $a_{i}$ to represent the identity of each sentence $\phi_{i}$ in the database - the argument language $\mathcal{A}$ is constructed from these primitive propositions. We then construct the argument database $\Delta=\left\{a_{1} \supset \phi_{1}, \ldots, a_{n} \supset \phi_{n}\right\}$. For example, the database

$$
\Gamma=\begin{aligned}
& \text { rain } \\
& \text { sprinkler_on } \\
& \text { rain } \supset \text { wet_grass } \\
& \text { sprinkler_on } \supset \text { wet_grass } \\
& \text { wet_grass } \\
& \text { wet_grass } \supset \text { wet_shoes. }
\end{aligned}
$$

gets represented by the argument database:

$$
\Delta=\begin{aligned}
& a_{1} \supset \text { rain } \\
& a_{2} \supset \text { sprinkler_on } \\
& a_{3} \supset \text { rain } \supset \text { wet_grass } \\
& a_{4} \supset \text { sprinkler_on } \supset \text { wet_grass } \\
& a_{5} \supset \text { wet_grass } \\
& a_{6} \supset \text { wet_grass } \supset \text { wet_shoes. }
\end{aligned}
$$

The argument network of this database was given in Figure 2.
The database $\Gamma$ entails some sentence $\phi$ precisely when $\Delta \cup\left\{a_{1} \wedge \ldots \wedge a_{n}\right\} \models \phi$. And this holds precisely
when $a_{1} \wedge \ldots \wedge a_{n}$ entails the argument $\Delta(\phi)$, which can be tested in time proportional to the size of the argument $\Delta(\phi)$.
When the observation $\phi$ is inconsistent with the database $\Gamma$, one is usually interested in retracting a set of sentences from the database $\Gamma$ to make it consistent with the observation $\phi$. There is often more than one set of sentences that can achieve this, and the prime implicants for the negated argument $\neg \Delta(\neg \phi)$ characterize all of them. In particular, the negative literals of a prime implicant for $\neg \Delta(\neg \phi)$ correspond to a minimal set of sentences that must be retracted, and its positive literals correspond to a minimal set of sentences that must not be retracted, in order for the database $\Gamma$ to become consistent with the observation $\phi$.

Example 9 Consider the database $\Gamma$ above and its corresponding argument database $\Delta$. We want to know whether $\Gamma$ entails wet_grass. We can answer this question by answering another question: Does $\Delta \cup\left\{a_{1}, \ldots, a_{6}\right\}$ entail wet_grass? To answer this question, we compute the argument for wet_grass and test whether $a_{1} \wedge \ldots \wedge a_{6}$ entails it. The argument for wet_grass was computed in Example 2 to be $\left(a_{1} \wedge a_{3}\right) \vee$ $\left(a_{2} \wedge a_{4}\right) \vee a_{5}$. This argument is entailed by $a_{1} \wedge \ldots \wedge a_{6}$. Therefore, $\Gamma$ entails wet_grass. Now, suppose that we observe $\neg$ wet_grass, which contradicts the database $\Gamma$. What should be retracted from $\Gamma$ to resolve this contradiction? To answer this question, we compute the prime implicants for $\neg \Delta(\neg$ wet_grass $)$, which turn

out to be:

$$
\begin{aligned}
& \neg a_{1} \wedge \neg a_{2} \wedge \neg a_{5} \\
& \neg a_{1} \wedge \neg a_{4} \wedge \neg a_{5} \\
& \neg a_{3} \wedge \neg a_{2} \wedge \neg a_{5} \\
& \neg a_{3} \wedge \neg a_{4} \wedge \neg a_{5}
\end{aligned}
$$

Each one of these implicants characterize a minimal set of sentences that must be retracted from $\Gamma$ in order to resolve the conflict with the given observation. For example, the first implicant says that if we remove rain, sprinkler_on and wet_grass from $\Gamma$, then $\neg$ wet_grass will no longer be inconsistent with the resulting $\Gamma$ :

$$
\begin{aligned}
& \text { rain } \supset \text { wet_grass } \\
& \text { sprinkler_on } \supset \text { wet_grass } \\
& \text { wet_grass } \supset \text { wet_shoes. }
\end{aligned}
$$

The fourth implicant, however, says that if we remove rain $\supset$ wet_grass, sprinkler_on $\supset$ wet_grass, and wet_grass from $\Gamma$, then $\neg$ wet_grass will no longer be inconsistent with the resulting $\Gamma$ :

$$
\begin{aligned}
& \text { rain } \\
& \text { sprinkler_on } \\
& \text { wet_grass } \supset \text { wet_shoes. }
\end{aligned}
$$

And so on.

### 6.2 Truth maintenance

The basic task of an assumption-based truth maintenance system, also called a clause management system (CMS) [Reiter and de Kleer, 1987], is to compute labels of sentences. Roughly speaking, the label for a sentence is a set of "minimal" arguments for that sentence. More formally, we have the following definitions [Reiter and de Kleer, 1987]:

Definition 11 A minimal support for sentence $\phi$ with respect to database $\Delta$ is a prime implicate of $\Delta \cup\{\neg \phi\}$ that is not an implicate of $\Delta$.

Definition 12 The $\mathcal{A}$-label of sentence $\phi$ with respect to database $\Delta$ is the set of all conjunctive clauses $\alpha$ such that $\alpha$ belongs to language $\mathcal{A}$ and $\neg \alpha$ is a minimal supports for $\phi$ with respect to $\Delta$.

The relation between the $\mathcal{A}$-label of a sentence and its argument is a corollary of the following theorem.

Theorem 10 Let $\Delta$ be an argument database with respect to $(\mathcal{L}, \mathcal{A})$. The sentence $\alpha$ is a prime implicant for $\Delta(A)$ precisely when $\alpha$ belongs to language $\mathcal{A}$ and $\neg \alpha$ is a minimal support for sentence $\phi$ with respect to database $\Delta$.

As the following corollary shows, the $\mathcal{A}$-label of a sentence is simply its argument put in a prime implicant form.

Corollary 2 Let $\Delta$ be an argument database with respect to $(\mathcal{L}, \mathcal{A})$. The $\mathcal{A}$-label of sentence $\phi$ with respect to database $\Delta$ is the set of prime implicants for argument $\Delta(A)$.

Example 10 Consider the argument database represented by the argument network in Figure 3:


The argument for the sentence $\neg A \wedge B \wedge C \supset F$ is $(O K(X) \vee O K(Y)) \wedge O K(Z)$. The prime implicants of this argument are $O K(X) \wedge O K(Z)$ and $O K(Y) \wedge O K(Z)$, each of which is an argument for $\neg A \wedge B \wedge C \supset F$. Moreover, by Corollary 2, these prime implicants constitute the label for the sentence $\neg A \wedge B \wedge C \supset F$.

### 6.3 Diagnosis

The basic task of a kernel-diagnosis system is to compute the kernel diagnoses of an observation with respect to some database. Roughly speaking, a kernel diagnosis of an observation is a "strongest" possible consequence of the observation. More formally, we have the following definition [de Kleer et al., 1992]:

Definition 13 The $\mathcal{A}$-kernel diagnoses of sentence $\phi$ with respect to database $\Delta$ are the prime implicants for the conjunction of all the prime implicates (that belong to language $\mathcal{A}$ ) of database $\Delta \cup\{\phi\}$.

The relation between kernel diagnoses and arguments is a corollary of the following theorem.

Theorem 11 The conjunction of all the prime implicates of database $\Delta$ that belong to language $\mathcal{A}$ is equivalent to the strongest sentence that belongs to language $\mathcal{A}$ and is entailed by database $\Delta$.

Corollary 3 Let $\Delta$ be an argument database with respect to $(\mathcal{L}, \mathcal{A})$. The $\mathcal{A}$-kernel diagnoses of sentence $\phi$ with respect to database $\Delta$ are the prime implicants for the negated argument $\neg \Delta(\neg \phi)$.

Example 11 Consider the database in Example 10. And suppose we observe $\neg A \wedge B \wedge C \wedge \neg F$, which is unexpected given that all gates are OK. Suppose further that we want to compute the kernel diagnoses of this observation. According to Corollary 3, we must first compute the argument for the negated observation. The negated observation in this case is $\neg A \wedge B \wedge C \supset F$, and its argument was computed in Example 10: $(O K(X) \vee O K(Y)) \wedge O K(Z)$. Negating this argument, we get $(\neg O K(X) \wedge \neg O K(Y)) \vee$ $\neg O K(Z)$. The prime implicants of this sentence are $\neg O K(X) \wedge \neg O K(Y)$ and $\neg O K(Z)$. That is, either gates $X$ and $Y$ are not OK, or that gate $Z$ is not OK. Each of these is a kernel diagnoses of the observation $\neg A \wedge B \wedge C \wedge \neg F$.

# CONCLUSION 

In this paper, I have identified a logical notion of independence that resembles probabilistic independence. I have also presented independence-based tools to represent and reason with a class of propositional databases that has several applications. The suggested tools have successful counterparts in the probabilistic literature.

## ACKNOWLEDGEMENT

This work was supported in part by grants from the Air Force Office in Scientific Research, AFOSR 900136 , and the National Science Foundation, IRI9200918 .
