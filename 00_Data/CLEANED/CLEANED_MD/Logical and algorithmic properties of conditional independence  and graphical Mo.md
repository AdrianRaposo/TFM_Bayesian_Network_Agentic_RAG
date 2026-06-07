# LOGICAL AND ALGORITHMIC PROPERTIES OF CONDITIONAL INDEPENDENCE AND GRAPHICAL MODELS ${ }^{1}$ 

By Dan Geiger and Judea Pearl<br>Technion-Israel Institute of Technology and University of California, Los Angeles


#### Abstract

This article develops an axiomatic basis for the relationship between conditional independence and graphical models in statistical analysis. In particular, the following relationships are established: (1) every axiom for conditional independence is an axiom for graph separation, (2) every graph represents a consistent set of independence and dependence constraints, (3) all binary factorizations of strictly positive probability models can be encoded and determined in polynomial time using their correspondence to graph separation, (4) binary factorizations of non-strictly positive probability models can also be derived in polynomial time albeit less efficiently and (5) unconditional independence relative to normal models can be axiomatized with a finite set of axioms.


1. Introduction. A useful approach to multivariate statistical modeling is to first define the conditional independence constraints that are likely to hold in the domain, and then to restrict the analysis to probability functions that satisfy those constraints. An increasingly popular way of specifying independence constraints are graphical models, such as Markov networks and Bayesian networks, where the constraints are encoded through the topological properties of the corresponding graphs [Lauritzen (1982), Lauritzen and Spiegelhalter (1988), Pearl (1988) and Whittaker (1990)].

The key idea behind these specification schemes is to utilize the correspondence between separation in graphs and conditional independence in probability; each node represents a variable and each missing edge encodes some conditional independence constraint. More specifically, if a set of nodes $Z$ blocks all the paths between two nodes, then the corresponding two variables are asserted to be conditionally independent given the variables corresponding to $Z$.

The notions of graph separation and conditional independence, which at first glance seem to have little in common, share key properties which render graphs an effective language of specifying independence constraints. This

[^0]
[^0]:    Received July 1989; revised November 1992.
    ${ }^{1}$ Supported in part by NSF Grant IRI-8821444 while the first author was at UCLA. The revised version was prepared while the first author was at Northrop Research and Technology Center and completed at Technion.

    AMS 1991 subject classifications. Primary 60A05, 60J99, 60G60; secondary 62A15, 62H25.
    Key words and phrases. Conditional independence, Markov fields, Markov networks, graphical models.

article develops an axiomatic characterization of these properties, thus providing a theoretical basis for understanding the role of graphical models in statistical analysis.

The article is organized as follows. Section 2 provides preliminary definitions. Section 3 proves the existence of perfect probability models, that is, probability models that, given an arbitrary list of conditional independence statements, satisfy every statement on that list, every statement that logically follows from that list and none other. Using this result, Section 4 then shows that every axiom for conditional independence is an axiom for graph separation and that every graph represents a consistent set of independence and dependence constraints. In other words, graphs provide a "safe" language for encoding statistical associations; the set of conditional independencies and dependencies encoded by any graph is guaranteed to be realizable in some probability model.

Section 5 deals with special kinds of conditional independence relationships, those that permit the factorization of a probability model into a product of two functions. It is shown that graphs provide a parsimonious code (requiring polynomial space) for representing the entire set of binary factorizations that are realizable in strictly positive probability models. Graphs also facilitate a polynomial time algorithm for determining whether an arbitrary binary factorization logically follows from a given set of such factorizations.

The rest of the article provides a complete axiomatic characterization for special families of independence relationships. We first develop complete axiomatizations for saturated independence (Section 6) and marginal independence (Section 7) and then address the axiomatization of conditional independence in general (Section 8). Section 9 generalizes several results to qualitative independence, and Section 10 provides a tabulated summary of our results.
2. Preliminaries. Throughout this article, let $U$ be a finite set of distinct symbols $\left\{u_{1}, \ldots, u_{n}\right\}$, called attributes (or variable names). A domain mapping is a mapping that associates a set, $d\left(u_{i}\right)$, with each attribute $u_{i}$. This set is called the domain of $u_{i}$ and each of its elements is a value for $u_{i}$. An attribute combined with a domain is a variable. For example, the variable describing the age of a person will be characterized by the attribute age and may be assigned a domain such as $\{i \mid 0 \leq i \leq 120\}$ or \{infant, child, young adult, other adult\}. The distinction between attributes and variables allows us to associate several domains with the same variable name, as done in some of the following.

Definition. A probability model over a finite set of attributes $U=$ $\left\{u_{1}, \ldots, u_{n}\right\}$ is a pair $(d, P)$, where $d$ is a domain mapping that maps each $u_{i}$ to a finite domain $d\left(u_{i}\right)$, and $P: d\left(u_{1}\right) \times \cdots \times d\left(u_{n}\right) \rightarrow[0,1]$ is a probability distribution having the Cartesian product of these domains as its sample space. The class of probability models over $U$ is denoted by $\mathscr{P}$.

Unless stated otherwise, $U$ and its domain are assumed to be finite.
Definition. The expression $I(X, Y \mid Z)$ where $X, Y$ and $Z$ are disjoint subsets of $U$ is called an independence statement. Its negation $\neg I(X, Y \mid Z)$ is called a dependence statement. An independence or dependence statement is defined over $V \subseteq U$ if it mentions only attributes in $V$.

Definition. Let $(d, P)$ be a probability model over $U$. An independence statement $I(X, Y \mid Z)$ is said to hold for $(d, P)$ if for every value $\mathbf{X}, \mathbf{Y}$ and $\mathbf{Z}$ of $X, Y$ and $Z$, respectively,

$$
P(\mathbf{X}, \mathbf{Y}, \mathbf{Z}) \cdot P(\mathbf{Z})=P(\mathbf{X}, \mathbf{Z}) \cdot P(\mathbf{Y}, \mathbf{Z})
$$

Equivalently, $(d, P)$ is said to satisfy $I(X, Y \mid Z)$. Otherwise, $(d, P)$ is said to satisfy $\neg I(X, Y \mid Z)$.

Definition. When $I(X, Y \mid Z)$ holds for $(d, P)$, then $X$ and $Y$ are conditionally independent relative to $(d, P)$, and if $Z=\varnothing$, then $X$ and $Y$ are marginally independent relative to $(d, P)$.

Definition. A probability model over $U$ is strictly positive if every combination of $U$ 's values has a probability greater than 0 . The class of strictly positive probability models is denoted by $\mathscr{P}^{+}$.

Definition. A probability model over $U$ is binary if it assigns every attribute in $U$ a domain with only two values, say 0 and 1 . The class of binary probability models is denoted by $\mathscr{B}$.

Equations (2) through (6) list some properties of conditional independence. Variants of them were first introduced by Dawid (1979) and further studied by Spohn (1980), Pearl and Paz (1985), Pearl (1988) and Geiger (1990).

Trivial independence:

$$
I(X, \varnothing \mid Y)
$$

Symmetry:

$$
I(X, Y \mid Z) \Rightarrow I(Y, X \mid Z)
$$

Decomposition:

$$
I(X, Y \cup W \mid Z) \Rightarrow I(X, Y \mid Z)
$$

Weak contraction [the axiomatic theory of Pearl and Paz (1985) invoked a stronger version of this axiom which is not needed in the discussion of this article]:

$$
I(X \cup W, Y \mid Z), I(X, W \mid Z \cup Y) \Rightarrow I(X, Y \cup W \mid Z)
$$

Weak union:

$$
I(X, Y \cup W \mid Z) \Rightarrow I(X, Y \mid Z \cup W)
$$

Definition. An independence Horn clause is an implication of the form

$$
I\left(X_{1}, Y_{1} \mid Z_{1}\right), I\left(X_{2}, Y_{2} \mid Z_{2}\right), \ldots I\left(X_{k}, Y_{k} \mid Z_{k}\right) \Rightarrow I\left(X_{k+1}, Y_{k+1} \mid Z_{k+1}\right)
$$

Each independence statement on the left of the implication is called an antecedent and the one on the right is called the consequence. Independence Horn clauses may also have no consequence [as in (2)].

Definition. An independence Horn clause is instantiated if each of the $X_{i}$ 's, $Y_{i}$ 's and $Z_{i}$ 's is substituted with a specific subset of $U$ [e.g., $I\left(\left\{u_{1}, u_{2}\right\}, \varnothing \mid\left\{u_{3}, u_{4}\right\}\right)$ is an instance of trivial independence].

We use $\sigma$, possibly subscripted, to denote an independence statement, $\neg \sigma$ to denote the negation of $\sigma, \Sigma$ to denote a set of independence statements and $\mathscr{F}$ to denote a subset of $\mathscr{P}$ (i.e., a class of probability models over $U$ such as $\mathscr{B}$ or $\mathscr{P}^{+}$).

Definition. An independence Horn clause is sound relative to $\mathscr{F}$ iff for every instantiation of the clause, every probability model in $\mathscr{F}$ that satisfies the clause's antecedents also satisfies its consequence.

Definition. When an independence Horn clause is sound relative to $\mathscr{F}$, it is called an axiom relative to $\mathscr{F}$. An axiom relative to $\mathscr{P}$ is simply called an axiom.

For example, (7) is an axiom relative to $\mathscr{P}^{+}$but not relative to $\mathscr{P}$.
Intersection:

$$
I(X, Y \mid Z \cup W), I(X, W \mid Z \cup Y) \Rightarrow I(X, Y \cup W \mid Z)
$$

Definition. Given a set of axioms $\mathscr{A}$, an independence statement $\sigma$ is derivable from a set of statements $\Sigma$, denoted $\Sigma \vdash \sigma$, if there exists a derivation sequence $\sigma_{1}, \ldots, \sigma_{n}$ such that $\sigma_{n}=\sigma$ and for each $\sigma_{j}$, either (1) $\sigma_{j} \in \Sigma$ or (2) $\sigma_{j}$ is the consequence of some instantiated axiom in $\mathscr{A}$ for which every antecedent is in $\left\{\sigma_{1}, \ldots, \sigma_{j-1}\right\}$. The closure of $\Sigma$ is the set of derivable statements, $\{\sigma \mid \Sigma \vdash \sigma\}$, and is denoted by $\Sigma^{+}$.

For example, $I\left(u_{1}, u_{3} \mid \varnothing\right)$ is derivable from the set $\left\{I\left(\left\{u_{1} u_{3}\right\}, u_{2} \mid \varnothing\right)\right.$, $I\left(u_{1}, u_{3} \mid u_{2}\right)$ \} using axioms (2) through (6) via the derivation sequence $I\left(\left\{u_{1} u_{3}\right\}, u_{2} \mid \varnothing\right), I\left(u_{1}, u_{3} \mid u_{2}\right), I\left(u_{1},\left\{u_{2}, u_{3}\right\} \mid \varnothing\right), I\left(u_{1}, u_{3} \mid \varnothing\right)$. The third and fourth statements in this sequence are derived from the previous ones by weak contraction and decomposition, respectively. [For simplicity, throughout, $I\left(u_{i}, u_{j} \mid u_{k}\right)$ stands for $I\left(\left\{u_{i}\right\},\left\{u_{j}\right\} \mid\left\{u_{k}\right\}\right)$ ].

Definition. An independence statement $\sigma$ is entailed by a set of statements $\Sigma$ relative to a set of probability models $\mathscr{F}$, denoted $\Sigma \vDash \sigma$, if every probability model in $\mathscr{F}$ that satisfies $\Sigma$ satisfies $\sigma$ as well. The set of entailed statements, $\{\sigma \mid \Sigma \vDash \sigma\}$, is denoted by $\Sigma^{*}$, keeping $\mathscr{F}$ implicit.

Proposition 1. Let $\mathscr{A}$ be a set of axioms relative to $\mathscr{F}$. For every set $\Sigma$ of independence statements, we have $\Sigma^{+} \subseteq \Sigma^{*}$, where $\Sigma^{+}$is derived from $\Sigma$ using the axioms in $\mathscr{A}$, and $\Sigma^{*}$ is entailed relative to $\mathscr{F}$.

Proof. The proof follows by induction on the length of a derivation sequence of each $\sigma$ in $\Sigma^{+}$, using the fact that the axioms in $\mathscr{A}$ are sound relative to $\mathscr{F}$.

Equality of $\Sigma^{+}$and $\Sigma^{*}$ holds only if no axioms are "missing."
Definition. A set of axioms $\mathscr{A}$ is complete (relative to $\mathscr{F}$ ) if for every set $\Sigma$ of independence statements, $\Sigma^{*}=\Sigma^{+}$.

Proposition 2. A set of axioms $\mathscr{A}$ is complete (relative to $\mathscr{F}$ ) if and only if for every set of statements $\Sigma$ and every statement $\sigma \notin \Sigma^{+}$there exists a probability model $\left(d_{\sigma}, P_{\sigma}\right)$ in $\mathscr{F}$ that satisfies $\Sigma$ and does not satisfy $\sigma$.

Proof. The proof follows immediately from the definition of completeness and Proposition 1.

Next, we seek conditions under which, for every set $\Sigma$ of independence statements, there exists a probability model in a given class $\mathscr{F}$ that satisfies precisely the statements in $\Sigma^{*}$ and none other. Fagin (1982) spelled out such conditions and showed, in the context of database theory, that they imply the existence of an operator $\otimes$ that maps a set of probability models to a probability model, such that an independence statement holds in the latter if and only if it holds in every constituent of the former. The next section constructs such an operator.
3. Perfect probability models. The main result of this section is that, for any given set $\Sigma$ of independence statements, there exists a probability model in $\mathscr{F}$ that satisfies precisely $\Sigma^{*}$ and no other statements. (Fagin called models with this property "Armstrong models.") An immediate application of it, as we shall see, lies in determining whether a given set of independence and dependence statements is consistent.

Definition. Let $\Sigma$ be a set of independence statements. A probability model is perfect for $\Sigma$ (relative to $\mathscr{F}$ ) if it satisfies precisely the set of statements $\Sigma^{*}$ entailed by $\Sigma$ (relative to $\mathscr{F}$ ) and none other.

The key idea in showing the existence of perfect probability models rests with the notion of direct product defined below, which extends Fagin's definition (1982) from database relations to probability models.

Definition. The (binary) direct product for $\mathscr{F}$ is a mapping, $\otimes: \mathscr{F} \times \mathscr{F} \rightarrow$ $\mathscr{F}$, where $\mathscr{F}$ is a class of probability models over a finite set of attributes

$\left\{u_{1}, \ldots, u_{n}\right\}$, and $(d, P)=\left(d_{1}, P_{1}\right) \otimes\left(d_{2}, P_{2}\right)$ is defined as follows: Let $d_{1}\left(u_{i}\right)$ and $d_{2}\left(u_{i}\right)$ be the domains associated with $u_{i}$ in $\left(d_{1}, P_{1}\right)$ and in $\left(d_{2}, P_{2}\right)$, respectively. Let $a_{i}$ and $b_{i}$ be values drawn respectively from these domains. Set the domain of $u_{i}$ in $(d, P)$ to be the Cartesian product $d_{1}\left(u_{i}\right) \times d_{2}\left(u_{i}\right)$, and let

$$
P\left(a_{1} b_{1}, a_{2} b_{2}, \ldots, a_{n} b_{n}\right)=P_{1}\left(a_{1}, a_{2}, \ldots, a_{n}\right) \cdot P_{2}\left(b_{1}, b_{2}, \ldots, b_{n}\right)
$$

where $a_{i} b_{i}$ denotes a value of $u_{i}$ in $(d, P)$.
A notable property of $\otimes$ is the assignment of a new domain, $d_{1}\left(u_{i}\right) \times d_{2}\left(u_{i}\right)$, to each $u_{i}$. Thus $u_{i}$ is treated as an attribute rather than a variable with a fixed domain. We will show at the end of this section that if the domain of each attribute is fixed, then the existence of perfect models is not guaranteed.

The next lemma shows that the product form of (8) remains valid after marginalization.

Lemma 3. Let $\left(d_{1}, P_{1}\right),\left(d_{2}, P_{2}\right)$ and $(d, P)$ be probability models over $U$ as in (8). Then, for every subset $u_{1_{1}}, \ldots, u_{i_{l}}$ of $U$,

$$
P\left(a_{i_{1}} b_{i_{1}}, a_{i_{2}} b_{i_{2}}, \ldots, a_{i_{l}} b_{i_{l}}\right)=P_{1}\left(a_{i_{1}}, a_{i_{2}}, \ldots, a_{i_{l}}\right) \cdot P_{2}\left(b_{i_{1}}, b_{i_{2}}, \ldots, b_{i_{l}}\right)
$$

Proof. Assume without loss of generality that in (9), $i_{1}=1, i_{2}=2, \ldots$, $i_{l}=l$. (otherwise reorder $u_{1}, \ldots, u_{n}$ to meet this assumption.) When $l=n$ this equation is identical to (8). We proceed by descending induction. Assume (9) holds for $l=k \leq n$; then

$$
\begin{aligned}
& P\left(a_{1} b_{1}, \ldots, a_{k-1} b_{k-1}\right) \\
& =\sum_{x_{k}} P\left(a_{1} b_{1}, \ldots, a_{k-1} b_{k-1}, x_{k}\right) \\
& =\sum_{a_{k} \in d_{1}\left(u_{k}\right), b_{k} \in d_{2}\left(u_{k}\right)} P_{1}\left(a_{1}, \ldots, a_{k-1}, a_{k}\right) \cdot P_{2}\left(b_{1}, \ldots, b_{k-1}, b_{k}\right) \\
& =\left\{\sum_{a_{k} \in d_{1}\left(u_{k}\right)} P_{1}\left(a_{1}, \ldots, a_{k-1}, a_{k}\right)\right\} \cdot\left\{\sum_{b_{k} \in d_{2}\left(u_{k}\right)} P_{2}\left(b_{1}, \ldots, b_{k-1}, b_{k}\right)\right\} \\
& =P_{1}\left(a_{1}, \ldots, a_{k-1}\right) \cdot P_{2}\left(b_{1}, \ldots, b_{k-1}\right)
\end{aligned}
$$

The key property of $\otimes$ is given in the following lemma.
Lemma 4. Let $\left(d_{1}, P_{1}\right),\left(d_{2}, P_{2}\right)$ and $(d, P)$ be probability models over $U$ as in (8). Then, for any three disjoint subsets $X, Y$ and $Z$ of $U$,

$$
\begin{aligned}
& I(X, Y \mid Z) \text { holds for }(d, P) \text { iff } I(X, Y \mid Z) \\
& \text { holds for }\left(d_{1}, P_{1}\right) \text { and for }\left(d_{2}, P_{2}\right)
\end{aligned}
$$

Proof. Let $a_{x}, a_{y}, a_{z}$ be respective values of $X, Y, Z$ in $\left(d_{1}, P_{1}\right)$ and $b_{x}, b_{y}, b_{z}$ be respective values of $X, Y, Z$ in $\left(d_{2}, P_{2}\right)$.

The if part of (10) follows from

$$
\begin{aligned}
& P\left(a_{x} b_{x}\right) P\left(a_{x} b_{x}, a_{y} b_{y}, a_{z} b_{z}\right) \\
& \quad=P_{1}\left(a_{x}, a_{y}, a_{z}\right) \cdot P_{1}\left(a_{x}\right) \cdot P_{2}\left(b_{x}, b_{y}, b_{z}\right) \cdot P_{2}\left(b_{z}\right) \\
& \quad=P_{1}\left(a_{x}, a_{x}\right) \cdot P_{1}\left(a_{y}, a_{x}\right) \cdot P_{2}\left(b_{x}, b_{z}\right) \cdot P_{2}\left(b_{y}, b_{z}\right) \\
& \quad=P\left(a_{x} b_{x}, a_{z} b_{z}\right) \cdot P\left(a_{y} b_{y}, a_{z} b_{z}\right)
\end{aligned}
$$

(Note the implicit use of Lemma 3.)
The only if part of (10) follows from

$$
\begin{aligned}
& P_{1}\left(a_{x}, a_{y}, a_{z}\right) \cdot P_{1}\left(a_{x}\right) \cdot P_{2}\left(b_{x}, b_{y}, b_{z}\right) \cdot P_{2}\left(b_{z}\right) \\
& \quad=P\left(a_{x} b_{x}, a_{y} b_{y}, a_{z} b_{z}\right) \cdot P\left(a_{z} b_{z}\right) \\
& \quad=P\left(a_{x} b_{x}, a_{z} b_{z}\right) \cdot P\left(a_{y} b_{y}, a_{z} b_{z}\right) \\
& \quad=P_{1}\left(a_{x}, a_{z}\right) \cdot P_{1}\left(a_{y}, a_{z}\right) \cdot P_{2}\left(b_{x}, b_{z}\right) \cdot P_{2}\left(b_{y}, b_{z}\right)
\end{aligned}
$$

By summing once over $a_{x}$ and once over $b_{x}$, it is evident that $I(X, Y \mid Z)$ holds for $\left(d_{1}, P_{1}\right)$ and for $\left(d_{2}, P_{2}\right)$.

Next, we extend the direct product to be a mapping from families of probability models (rather than pairs) into probability models.

Theorem 5. There exists an operator $\otimes$ that any nonempty finite family $\left\{\left(d_{i}, P_{i}\right) \mid i=1, \ldots, n\right\}$ of probability models over a set of attributes $U$ into a probability model over $U$, such that if $\sigma$ is an independence statement, then $\sigma$ holds for $\otimes\left\{\left(d_{i}, P_{i}\right) \mid i=1, \ldots, n\right\}$ if and only if $\sigma$ holds for each $\left(d_{i}, P_{i}\right)$.

Proof. Since the binary direct product is commutative and associative, it can be extended to sets as follows:

$$
\left.\otimes\left\{\left(d_{i}, P_{i}\right) \mid i=1, \ldots, n\right\}=\left(\left(\left(\left(d_{1}, P_{1}\right) \otimes\left(d_{2}, P_{2}\right)\right) \otimes\left(d_{3}, P_{3}\right)\right) \otimes \cdots\left(d_{n}, P_{n}\right)\right)\right)
$$

Due to Lemma 4,
$\sigma$ holds for $\otimes\left\{\left(d_{i}, P_{i}\right) \mid i=1, \ldots, n\right\}$ iff $\sigma$ hold for every $\left(d_{i}, P_{i}\right)$,
as stated by the theorem.
Consequently, the existence of perfect probability models can be established [similar to (Fagin 1982)].

Corollary 6. For every set of independence statements $\Sigma$ over the attributes of $U$, there exists a probability model $(d, P)$ in $\mathscr{P}$ such that $(d, P)$ satisfies every statement in $\Sigma^{*}$ and none other, that is, $(d, P)$ is a perfect model relative to $\mathscr{P}$.

Proof. Let $(d, P)$ be $\otimes\left\{\left(d_{\sigma}, P_{\sigma}\right) \mid \sigma \notin \Sigma^{*}\right\}$, where $\left(d_{\sigma}, P_{\sigma}\right)$ is a probability model that satisfies $\Sigma^{*}$ but does not satisfy $\sigma$. By the definition of $\Sigma^{*}$, a probability model ( $d_{\sigma}, P_{\sigma}$ ) always exists except for the degenerated case where $\Sigma^{*}$ renders all variables mutually independent, in which case Corollary 6 holds trivially. (Also note that the set $\left\{\sigma \mid \sigma \notin \Sigma^{*}\right\}$ is finite because $U$ is finite.) Due to Theorem $5,(d, P)$ satisfies the statements in $\Sigma^{*}$ and none other because these are the only statements that hold for every $\left(d_{\sigma}, P_{\sigma}\right)$.

The probability model $\otimes\left\{\left(d_{i}, P_{i}\right) \mid i=1, \ldots, n\right\}$ is strictly positive whenever each $\left(d_{i}, P_{i}\right)$ is strictly positive. Consequently, we obtain the following result.

Corollary 7. For every set of independence statements $\Sigma$, there exists a strictly positive probability model $(d, P)$ such that $(d, P)$ satisfies every statement in $\Sigma^{*}$ (relative to $\mathscr{P}^{+}$) and none other, that is, $(d, P)$ is a perfect model relative to $\mathscr{P}^{+}$.

The existence of a perfect model implies that any algorithm that determines whether a given statement is entailed by $\Sigma$ can also determine whether a disjunction of statements in entailed by $\Sigma$. For example, to show that

$$
\left\{I\left(u_{1}, u_{2} \mid \varnothing\right), I\left(u_{1}, u_{2} \mid u_{3}\right)\right\} \not \equiv I\left(u_{1}, u_{3} \mid \varnothing\right) \vee I\left(u_{2}, u_{3} \mid \varnothing\right)
$$

we will see that one must merely check that each disjunct is not entailed by itself.

To refute the first disjunct, construct a probability model ( $d_{1}, P_{1}$ ) in which $u_{1}$ and $u_{2}$ are two independent binary variables and $u_{1}$ equals $u_{3}$. This probability model satisfies the antecedents but does not satisfy the first disjunct. To refute the second disjunct, construct a probability model ( $d_{2}, P_{2}$ ) in which $u_{1}$ and $u_{2}$ are two independent binary variables and $u_{2}$ equals $u_{3}$; it satisfies the antecedents but not the second disjunct. The probability model $\left(d_{1}, P_{1}\right) \otimes\left(d_{2}, P_{2}\right)$ satisfies the antecedents but does not satisfy the disjunction. Hence, the disjunction is not entailed by the antecedents.

Notably, if we fix the domain of $u_{3}$ to be binary, the antecedents of (11) do entail the disjunctive consequence [Pearl (1988), pp. 129 and 137]; the construction of $\left(d_{1}, P_{1}\right) \otimes\left(d_{2}, P_{2}\right)$ fails because $\otimes$ assigns a domain of size 4 to $u_{3}$. Consequently, we obtain the following result.

Corollary 8. There exists a set of independence statements $\Sigma$ for which no binary probability model is perfect.

Proof. Let $\Sigma=\left\{I\left(u_{1}, u_{2} \mid \varnothing\right), I\left(u_{1}, u_{2} \mid u_{3}\right)\right\}$. Every binary probability model that satisfies $\Sigma$ satisfies either $I\left(u_{1}, u_{3} \mid \varnothing\right)$ or $I\left(u_{2}, u_{3} \mid \varnothing\right)$. However, neither statement in itself is entailed by $\Sigma$ (relative to $\mathscr{B}$ ) and therefore none is in $\Sigma^{*}$.

Another application of Theorem 5 is facilitating tests for consistency.
Definition. A set of independence statements $\Sigma_{n}$ and a set of negated independence statements (i.e., dependence statements) $\Sigma_{n}$ is consistent if there

exists a probability model that satisfies $\Sigma_{p} \cup \Sigma_{n}$. The task of deciding whether a set of independence and dependence statements is consistent is called the consistency problem. The task of determining whether a set of independence statements entails an independence statement is called the implication problem.

The following algorithm determines whether or not $\Sigma_{p} \cup \Sigma_{n}$ is consistent: For every member $\neg \sigma$ of $\Sigma_{n}$, determine whether $\Sigma_{p} \equiv \sigma$. If the answer is negative for all members of $\Sigma_{n}$, then $\Sigma_{p} \cup \Sigma_{n}$ is consistent; otherwise it is not consistent [(Geiger, Paz and Pearl (1991)].

This algorithm works when the following two conditions are met: (1) we can efficiently check whether or not $\Sigma \equiv \sigma$ and (2) entailment is taken with respect to a class of probability models that has perfect models (i.e., $\mathscr{P}^{+}$but not $\mathscr{B}$ ). In Section 5 we examine a class of independence statements, called saturated, for which these conditions are met.

The correctness of the algorithm stems from the fact that if the negation of each member $\neg \sigma$ of $\Sigma_{n}$ is not entailed by $\Sigma_{p}$, that is, each member of $\Sigma_{n}$ is individually consistent with $\Sigma_{p}$, then there exists a probability model $\left(d_{\sigma}, P_{\sigma}\right)$ that satisfies $\Sigma_{p}$ and does not satisfy $\sigma$. The probability model $(d, P)=$ $\otimes\left\{\left(d_{\sigma}, P_{\sigma}\right) \mid \neg \sigma \in \Sigma_{n}\right\}$ satisfies every statement in $\Sigma_{p} \cup \Sigma_{n}$, and therefore the algorithm's decision that the two sets are consistent is correct. In the other direction, namely, when the algorithm detects an inconsistent member of $\Sigma_{n}$, then the decision is obviously correct.
4. Graphs and independence. The use of graphs for representing probability distributions is well documented in the statistical literature [Whittaker (1990) and reference therein]. The basis of these representation schemes is the similarity between separation in graphs and conditional independence in probability. We will show that these two concepts are related in a stronger sense than was previously known; we will show that every axiom for conditional independence must also be an axiom for graph separation, and that the set of separation-connection conditions embodied in any graph always corresponds to a consistent set of independence-dependence statements in probability.

Definition. An undirected graph is a pair $(U, E)$, where $U$ is a finite set of attributes, called nodes, and $E$ is a set of unordered pairs of distinct nodes, called edges. When $\left(u_{1}, u_{2}\right)$ is an edge, $u_{1}$ and $u_{2}$ are directly connected. A path between two nodes is a sequence of nodes for which every pair of adjacent nodes is directly connected and no node appears twice.

Definition. Let $X, Y$ and $Z$ be disjoint subsets of nodes in a graph $G=(U, E)$. A separation statement $J(X, Y \mid Z)$ is said to hold for $G$ if every path between a node in $X$ and a node in $Y$ includes a node in $Z$. Equivalently, we say that $G$ satisfies $J(X, Y \mid Z)$ or $X$ and $Y$ are separated by $Z$ in $G$.

Connection (negated separation) statements, separation Horn clauses and separation Horn axioms for a set of graphs are defined analogously to the corresponding concepts of independence defined in Section 2.

It is easy to see that axioms (2) through (7) remain sound when $I$ is replaced with $J$; that is, whenever the antecedent of one of these axioms holds in some graph, its consequence holds as well. For example, if $X$ and $Y \cup W$ are separated by $Z$ in some graph $G$, then $X$ and $Y$ are also separated by $Z \cup W$ as dictated by the weak-union axiom (6). This correspondence between independence and graph separation is not a coincidence; we show next that every axiom of conditional independence is an axiom for separation. The converse does not hold [Pearl (1988)]. A preliminary definition and a lemma are needed.

Definition. Let $(d, P)$ be a probability model over a finite set of attributes $U$, and let $G$ be a graph whose nodes are the elements of $U$ (i.e., each node is associated with an attribute). Then $G$ is said to be a Markov network of $(d, P)$ if for every three disjoint subsets $X, Y$ and $Z$ of $U$,

$$
J(X, Y \mid Z) \text { holds for } G \text { implies that } I(X, Y \mid Z) \text { holds for }(d, P)
$$

For example, a language in which the probability of the $i$ th letter is determined solely by the $(i-1)$ th letter via $P\left(l_{i} \mid l_{i-1}\right)$ can be represented by the Markov network of Figure 1. This graph shows, for example, that $l_{1}$ and $l_{3}$ are conditionally independent given $l_{2}$, since $l_{2}$ separates $l_{1}$ and $l_{3}$. Note that this independence statement holds regardless of the domain associated with each $l_{i}$ (i.e., the alphabet of the language need not be specified). Markov networks are discussed in Darroch, Lauritzen and Speed (1980) and Lauritzen (1982).

A variant of the next lemma was independently derived by Frydenberg (1990).

Lemma 9. Let $G$ be an undirected graph with $U$ as its set of nodes. Let $X, Y$ and $Z$ be disjoint subsets of $U$ such that $X$ and $Y$ are not separated by $Z$. Then there exists a strictly positive probability model $(d, P)$ over a set of attributes $U$, such that $G$ is a Markov network of $(d, P)$ and $I(X, Y \mid Z)$ does not hold for $(d, P)$.

Proof. Since $X$ and $Y$ are not separated by $Z$, there exists a path $r_{1}, r_{2}, \ldots, r_{l}$ which contain no nodes of $Z$ and which connects a node $r_{1}$ in $X$ to a node $r_{l}$ in $Y$. Let every node $r_{i}$ be associated with a binary variable $v_{i}$ and

$$
l_{1}-\left(l_{2}-\left(l_{3}\right)-\left(l_{4}\right)-\left(l_{5}\right.\right.
$$

Fig. 1. A five-node chain.

every node not on the path be associated with a binary variable $s_{i}$. A probability model $(d, P)$ where

$$
P\left(v_{1}, \ldots, v_{l}, s_{1}, \ldots\right)=(1 / 2) \cdot \prod_{i=1}^{l-1} f\left(v_{i}, v_{i+1}\right) \cdot \prod_{i} g\left(s_{i}\right)
$$

$g\left(s_{i}\right)=1 / 2$, and

$$
f\left(v_{i}, v_{i+1}\right)= \begin{cases}1 / 2, & \text { if } v_{i}=0, v_{i+1}=0 \\ 1 / 2, & \text { if } v_{i}=0, v_{i+1}=1 \\ 1 / 4, & \text { if } v_{i}=1, v_{i+1}=0 \\ 3 / 4, & \text { if } v_{i}=1, v_{i+1}=1\end{cases}
$$

satisfies the requirements; $I\left(v_{1}, v_{l} \mid Z\right)$ does not hold and if $J\left(X^{\prime}, Y^{\prime} \mid Z^{\prime}\right)$ holds, $I\left(X^{\prime}, Y^{\prime} \mid Z^{\prime}\right)$ holds as well.

Theorem 10. Every independence Horn clause $\sigma_{1}, \sigma_{2}, \ldots, \sigma_{n} \Rightarrow \sigma$ that is an axiom for independence relative to $\mathscr{P}^{+}$is also an axiom for separation, where each $\sigma_{i}$ is interpreted as a separation statement.

Proof. Suppose by contradiction that there exists a graph that satisfies $\Sigma=\left\{\sigma_{1}, \ldots, \sigma_{n}\right\}$ and does not satisfy $\sigma$. Then by Lemma 9 there exists a strictly positive probability model that satisfies $\Sigma$ and does not satisfy $\sigma$. Thus $\sigma_{1}, \sigma_{2}, \ldots, \sigma_{n} \Rightarrow \sigma$ is not sound relative to $\mathscr{P}^{+}$.

Consequently, in particular, axioms (2) through (7) as well as those discussed by Studeny (1992) are axioms for separation. A complete list of axioms for separation was found by Pearl and Paz (1985).

Each graph can be thought of as a specification language for independence and dependence statements; whenever a separation condition holds in the graph, the corresponding independence statement is asserted, and whenever a connection condition holds in the graph, the corresponding dependence statement is asserted. We will show next that, in any graph, the two sets of statements are always consistent. This result justifies the use of undirected graphs as a general language for encoding intricate patterns of statistical associations. Similar results hold for directed acyclic graphs [Geiger and Pearl (1988)].

Theorem 11. For every graph $G$ with $U$ as its nodes, there exists a strictly positive probability model $(d, P)$ over $U$, such that for every three disjoint sets $X, Y$ and $Z$ of $U$,

$$
J(X, Y \mid Z) \text { holds for } G \text { if and only if } I(X, Y \mid Z) \text { holds for }(d, P)
$$

Proof. Let $\Sigma$ be the set of separation statements that hold in $G$. For every statement $\sigma \notin \Sigma$, there exists a probability model ( $d_{\sigma}, P_{\sigma}$ ) that satisfies $\Sigma$ and does not satisfy $\sigma$ where $\Sigma$ and $\sigma$ are interpreted as independence statements

(Lemma 9). Let $(d, P)$ be $\otimes\left\{\left(d_{\sigma}, P_{\sigma}\right) \mid \sigma \notin \Sigma\right\}$. (The set $\{\sigma \mid \sigma \neg \in \Sigma\}$ if finite because $U$ is finite.) Due to Theorem $5,(d, P)$ satisfies precisely the statements in $\Sigma$ and none other.

Note, however, that $\otimes$ assigns to each attribute in $U$ an arbitrary domain size. We conjecture that this arbitrariness is not needed.

Conjecture 1. For every graph $G$ with $u_{1}, \ldots, u_{n}$ as its nodes and for every $n$ integers $k_{1}, \ldots, k_{n}$ all greater than 2 , there exists a strictly positive probability model $(d, P)$ over $U$, such that (1) $\left|d\left(u_{i}\right)\right|=k_{i}$ and (2) for every three disjoint sets $X, Y$ and $Z$ of $U$,
$J(X, Y \mid Z)$ holds for $G$ if and only if $I(X, Y \mid Z)$ holds for $(d, P)$.
5. Graphs and binary factorizations. The relationship between graph separation and conditional independence is even stronger than that shown so far if we restrict ourselves to strictly positive probability models and to saturated statements.

Definition. An independence statement $I(X, Y \mid Z)$ or a separation statement $J(X, Y \mid Z)$ is saturated if $X \cup Y \cup Z=U$, where $U$ is the finite set of attributes of interest.

In the following discussion we show that saturated independence statements (relative to $\mathscr{P}^{+}$) and saturated separation statements satisfy precisely the same axioms. This correspondence provides us with an efficient algorithm to deterine all saturated independence statements entailed (relative to $\mathscr{P}^{+}$) by a given set of such statements.

Moreover, each statement $I(X, Y \mid Z)$ holds for a probability model $(d, P)$ if and only if $(d, P)$ has a binary factorization, namely,

$$
P(X, Y, Z)=f(X, Y) \cdot g(Y, Z)
$$

where $g$ and $f$ are any functions [Lauritzen (1982)]. Consequently, the proposed algorithm provides an efficient way to determine all binary factorizations entailed (relative to $\mathscr{P}^{+}$) by a given set of binary factorizations. [The terms saturated independence and binary factorizations are borrowed, respectively, from Lee and Buehler (1986) and Malvestuto (1992)].

We use the following theorem of Pearl and Paz (1985) which generalizes a result by Lauritzen (1982).

Theorem 12. Let $\Sigma$ be a set of independence statements over a finite set of attributes $U$, and let $\Sigma^{+}$be the closure of $\Sigma$ with respect to trivial independence, symmetry, decomposition, intersection and weak union. Let $G_{0}$ be the graph having $U$ as its nodes and an edge between $x$ and $y$ if and only if

$I(\{x\},\{y\} \mid U \backslash\{x, y\}) \in \Sigma^{+}$. Then (1) for every three disjoint subsets $X, Y$ and $Z$ of $U$,

$$
J(X, Y \mid Z) \text { holds for } G_{0} \text { implies that } I(X, Y \mid Z) \in \Sigma^{+}
$$

and (2) if any edge is removed from $G_{0}$ property 1 ceases to hold.
Next, we strengthen Theorem 12 when $\Sigma$ consists of saturated independence statements.

Theorem 13. Let $\Sigma$ be a set of saturated independence statements over a finite set of attributes $U$, and let $\Sigma^{+}$be the closure of $\Sigma$ with respect to saturated trivial independence [i.e., all statements of the form $I(X, \varnothing \mid Z)$ where $X \cup Z=U]$, symmetry, intersection and weak union. Let $G_{0}$ be the graph defined in Theorem 12. Then for every three disjoint subsets $X, Y$ and $Z$ of $U$, such that $X \cup Y \cup Z=U$,

$$
J(X, Y \mid Z) \text { holds for } G_{0} \text { iff } I(X, Y \mid Z) \in \Sigma^{+}
$$

Proof. The key point to notice is that $I(X, Y \mid Z) \in \Sigma^{+}$if and only if $I(\{x\},\{y\} \mid Z \cup(X \backslash\{x\}) \cup(Y \backslash\{y\}))$ is in $\Sigma^{+}$for every $x \in X$ and $y \in Y$. Each of these independence statements is derivable from $I(X, Y \mid Z)$ by an application of weak union followed by symmetry, weak union and finally followed by symmetry. The statement $I(X, Y \mid Z)$ is derivable by repeated applications of intersection and symmetry. The same equivalence holds when $I$ is replaced by $J$ because separation satisfies the three axioms we have used in the preceding argument. Consequently, $J(X, Y \mid Z)$ holds for $G_{0}$ iff $J(\{x\},\{y\} \mid Z \cup(X \backslash\{x\}) \cup$ $(Y \backslash\{y\}))$ holds for $G_{0}$ for every $x \in X$ and $y \in Y$. By the definition of $G_{0}$, the latter set of statements holds if and only if $I(\{x\},\{y\} \mid Z \cup(X \backslash\{x\}) \cup(Y \backslash\{y\}))$ is in $\Sigma^{+}$for every $x \in X$ and $y \in Y$. In addition, these statements are in $\Sigma^{+}$ iff $I(X, Y \mid Z) \in \Sigma^{+}$. An additional minor observation is that each trivial independence statement holds in every graph $(U, E)$ in particular in $G_{0}$.

Similarly, we obtain the following result.
Theorem 14 (Completeness relative to $\mathscr{P}^{+}$). Let $\Sigma$ be a set of saturated independence statements, and let $\Sigma^{+}$be the closure of $\Sigma$ with respect to saturated trivial independence, symmetry, intersection and weak union. Then, for every $\sigma \notin \Sigma^{+}$, there exists a strictly positive probability model $\left(d_{\sigma}, P_{\sigma}\right)$ over $U$, where $U$ is the set of attributes that appears in $\Sigma$, that satisfies $\Sigma^{+}$and does not satisfy $\sigma$.

Proof. By Theorem 13 there exists a graph $G_{0}$ that satisfies $\Sigma^{+}$and no other independence statement. By Lemma 9 there exists a strictly positive probability model $\left(d_{\sigma}, P_{\sigma}\right)$ that satisfies the statements that hold in $G_{0}$ and does not satisfy $\sigma$. Thus $\left(d_{\sigma}, P_{\sigma}\right)$ satisfies the requirement of the theorem.

Theorems 13 and 14 together show that saturated independence statements and saturated separation statements share precisely the same axioms (relative to $\mathscr{P}^{+}$). This equivalence permits us to compute the set of all saturated independence statements entailed relative to $\mathscr{P}^{+}$by a given set of saturated statements, using a purely graph-theoretic approach.

The algorithm is simple: Given a set of saturated independence statements $\Sigma$ over $U$, construct the graph $G_{0}=(U, E)$ as follows.

Step 1. Replace each given statement $I(X, Y \mid Z)$ with a set of independence statements $\{I(\{x\},\{y\} \mid Z \cup(X \backslash\{x\}) \cup(Y \backslash\{y\})) \mid x \in X, y \in Y\}$.

Step 2. Introduce an edge between $x$ and $y$ if $I(\{x\},\{y\} \mid Z \cup(X \backslash\{x\}) \cup(Y \backslash$ $\{y\}))$ is not among the statements generated in Step 1.

Step 3. Output $I\left(X^{\prime}, Y^{\prime} \mid Z^{\prime}\right) \in \Sigma^{+}$if $J\left(X^{\prime}, Y^{\prime} \mid Z^{\prime}\right)$ holds in the graph produced in Step 2. Otherwise output $I\left(X^{\prime}, Y^{\prime} \mid Z^{\prime}\right) \notin \Sigma^{+}$.

The algorithm requires $O\left(|\Sigma| \cdot n^{2}\right)$ steps to construct $G_{0}$ where $n$ is the number of attributes because it scans each statement of the input once and each statement may require checking $n^{2}$ pairs of attributes. Once $G_{0}$ is constructed, it permits us to check whether a specific saturated statement $\sigma=I(X, Y \mid Z)$ is entailed (relative to $\mathscr{P}^{+}$) by $\Sigma$ in only $O(n)$ steps-the time needed to check whether $Z$ separates $X$ and $Y$ in $G_{0}$.

This method allows us to represent in polynomial space (in the number of attributes) the entire set of binary factorizations entailed (relative to $\mathscr{P}^{+}$) by a given set of binary factorizations and to determine, in polynomial time, whether or not a specific binary factorization is in this set. We will see next that a similar implication algorithm, albeit less efficient, can be developed without the assumption of strict positiveness.
6. Saturated independence. The next completeness theorem is the analog of Theorem 14 with weak contraction replacing intersection. This change is needed because intersection is sound relative to $\mathscr{P}^{+}$but not relative to $\mathscr{P}$.

Theorem 15 (Completeness relative to $\mathscr{P}$ ). Let $\Sigma$ be a set of saturated independence statements over a finite set of attributes $U$, and let $\Sigma^{+}$be the closure of $\Sigma$ with respect to saturated trivial independence, symmetry, weak contraction and weak union. Then, for every $\sigma \notin \Sigma^{+}$, there exists a probability model ( $d_{\sigma}, P_{\sigma}$ ) that satisfies $\Sigma^{+}$and does not satisfy $\sigma$.

Proof. Let $\sigma=I(X, Y \mid Z)$ be a saturated statement not in $\Sigma^{+}$where $X \cup Y \cup Z=U$. At first we assume that $\sigma$ is maximal, that is, for all sets $X^{\prime} X^{\prime \prime}$ and $Y^{\prime} Y^{\prime \prime}$ partitioning $X$ and $Y$, respectively, the statement $I\left(X^{\prime}, Y^{\prime} \mid Z X^{\prime \prime} Y^{\prime \prime}\right)$ is in $\Sigma^{+}$. (In this proof $A B$ stands for $A \cup B$.) At the end of the proof we relax this assumption.

Let each attribute in $U$ be associated with a binary domain $\{0,1\}$. Denote all attributes in $X$ by $x_{1}, x_{2}, \ldots, x_{l}$, those in $Y$ by $y_{1}, y_{2}, \ldots, y_{m}$ and those in $Z$

by $z_{1}, z_{2}, \ldots, z_{k}$. The probability model $\left(d_{\sigma}, P_{\sigma}\right)$ is defined as follows:
$P_{\sigma}(X, Y, Z)=\prod_{z_{i} \in Z} f\left(z_{i}\right) \cdot\left\{\begin{array}{ll}1 / 2, & \text { if all attributes in } X \cup Y \text { are assigned } 0, \\ 1 / 2, & \text { if all attributes in } X \cup Y \text { are assigned } 1, \\ 0, & \text { otherwise, }\end{array}\right.$
where $f\left(z_{i}\right)=1 / 2$.
This probability model does not satisfy $\sigma$ because $P_{\sigma}(X=0, Y=1, Z=0)$ is 0 , while $P_{\sigma}(X=0, Z=0)$ and $P_{\sigma}(Y=1, Z=0)$ are not.

It remains to show that every saturated statement in $\Sigma^{+}$holds for $\left(d_{\sigma}, P_{\sigma}\right)$, or equivalently that every saturated statement either holds for $\left(d_{\sigma}, P_{\sigma}\right)$ or does not belong to $\Sigma^{+}$. Any saturated statement $\gamma$ can be written as $I\left(X_{1} Y_{1} Z_{1}, X_{3} Y_{3} Z_{3} \mid X_{2} Y_{2} Z_{2}\right)$, where $X=X_{1} X_{2} X_{3}, Y=Y_{1} Y_{2} Y_{3}$ and $Z=Z_{1} Z_{2} Z_{3}$ and the $X_{i}$ 's, $Y_{i}$ 's and $Z_{i}$ 's are all disjoint. If $X_{2} Y_{2} \neq \varnothing$, then $\gamma$ holds for $\left(d_{\sigma}, P_{\sigma}\right)$ because every instance of $X_{1} Y_{1} Z_{1}$ and of $X_{3} Y_{3} Z_{3}$ that is consistent with the values of $X_{2} Y_{2}$ has the same probability of occurring, namely, $1 / 2^{\left|Z_{1}\right|} \cdot 1 / 2^{\left|Z_{2}\right|}$. If $X_{1} Y_{1}=\varnothing$, then, again, $\gamma$ holds for $\left(d_{\sigma}, P_{\sigma}\right)$ because $Z_{1}$ is marginally and conditionally independent of any other set of attributes of $P_{\sigma}$. (Symmetrically when $X_{3} Y_{3}=\varnothing$.) Otherwise, $\gamma$ is of the form $I\left(X_{1} Y_{1} Z_{1}, X_{3} Y_{3} Z_{3} \mid Z_{2}\right)$, where $X_{1} Y_{1} \neq \varnothing$ and $X_{3} Y_{3} \neq \varnothing$. We continue by contradiction and show that in this case $\gamma$ does not belong to $\Sigma^{+}$.

Assume, by contradiction, that the statement $I\left(X_{1} Y_{1} Z_{1}, X_{3} Y_{3} Z_{3} \mid Z_{2}\right)$ is in $\Sigma^{+}$. Then $I\left(X_{1} Y_{1}, X_{3} Y_{3} \mid Z\right)$ is in $\Sigma^{+}$as well because it can be derived by weak union and symmetry. To reach a contradiction, we show that the latter statement implies that $\sigma$ must be in $\Sigma^{+}$, contradicting our selection of $\sigma$. The proof uses weak contraction and symmetry to derive $I\left(X_{1} X_{3}, Y_{1} Y_{3} \mid Z\right)$ (i.e., $\sigma$ ) from $I\left(X_{1} Y_{1}, X_{3} Y_{3} \mid Z\right)$ by "joining" the $X$ 's and the $Y$ 's. The following is a derivation of $\sigma$.

First, $I\left(X_{1}, Y_{1} \mid Z X_{3} Y_{3}\right)$ is in $\Sigma^{+}$because $I(X, Y \mid Z)$ is maximal. Due to weak contraction,

$$
I\left(X_{1} Y_{1}, X_{3} Y_{3} \mid Z\right), I\left(X_{1}, Y_{1} \mid Z X_{3} Y_{3}\right) \Rightarrow I\left(X_{1}, Y_{1} X_{3} Y_{3} \mid Z\right)
$$

we conclude that $I\left(X_{1}, Y X_{3} \mid Z\right) \in \Sigma^{+}$. Due to symmetry, we conclude $I\left(Y X_{3}, X_{1} \mid Z\right) \in \Sigma^{+}$as well. $I\left(X_{3}, Y \mid Z X_{1}\right) \in \Sigma^{+}$because $\sigma$ is maximal. Therefore, by symmetry, $I\left(Y, X_{3} \mid Z X_{1}\right)$ is also in $\Sigma^{+}$. Using weak contraction, we obtain

$$
I\left(Y X_{3}, X_{1} \mid Z\right), I\left(Y, X_{3} \mid Z X_{1}\right) \Rightarrow I\left(Y, X_{1} X_{3} \mid Z\right)
$$

Thus $I(Y, X \mid Z) \in \Sigma^{+}$, and, by symmetry, $I(X, Y \mid Z) \in \Sigma^{+}$, a contradiction. (Note that if some sets out of $X_{1}, X_{3}, Y_{1}$ and $Y_{3}$ are empty, the derivation just described remains valid.)

If $\sigma=I(X, Y \mid Z)$ is not maximal, then either $I(X \backslash\{x\}, Y \mid Z \cup\{x\}) \notin \Sigma^{+}$for some $x \in X$ or $I(X, Y \backslash\{y\} \mid Z \cup\{y\}) \notin \Sigma^{+}$for some $y \in Y$. Without loss of generality assume the first statement is not in $\Sigma^{+}$. If this statement is maximal, denote it $\sigma^{\prime}$. Otherwise, repeat the process of augmenting $Z$ with additional elements from $X$ and $Y$. When this process can no longer continue, we denote the resulting statement $\sigma^{\prime}=I(R, S \mid T)$. Clearly, $\sigma^{\prime}$ is maximal; it is

not in $\Sigma^{+}$and for all sets $R^{\prime} R^{\prime \prime}$ and $S^{\prime} S^{\prime \prime}$ partitioning $S$ and $T$, respectively, the statement $I\left(R^{\prime}, S^{\prime} \mid T R^{\prime \prime} S^{\prime \prime}\right)$ is in $\Sigma^{+}$.

For a maximal statement $\sigma^{\prime}$, we have shown how to construct a probability model ( $d_{\sigma^{\prime}}, P_{\sigma^{\prime}}$ ) that satisfies $\Sigma$ and does not satisfy $\sigma^{\prime}$. Due to symmetry and weak union, which hold for all probability models, any probability model that does not satisfy $\sigma^{\prime}$, does not satisfy $\sigma$ as well. In particular, $\left(d_{\sigma}, P_{\sigma^{\prime}}\right)$ does not satisfy $\sigma$ while satisfying $\Sigma^{+}$, as required by the theorem.

The probability model ( $d_{\sigma}, P_{\sigma}$ ) constructed previously has an additional property; each combination of values for $X \cup Y \cup Z$ has either zero probability or a constant probability of $1 / 2^{|Z|+1}$. Thus the probability model ( $d_{\sigma}, P_{\sigma}$ ) can be viewed as a database, categorically distinguishing between possible and impossible value combinations. Consequently, the proof of Theorem 15 shows that the previously mentioned axioms are also complete for MVD statements of relational databases [Fagin (1978)]. Indeed, the only difference between our axioms and the ones governing MVD's is that the latter allow overlapping sets $X, Y$ and $Z$ in $I(X, Y \mid Z)$ whereas we do not [Beeri, Fagin and Howard (1977)]. This equivalence permits the employment of a polynomial implication algorithm devised for MVDs [Beeri (1980)] to determine whether a saturated statement is entailed by a set of saturated statements, just as the equivalence between graph separation and conditional independence (relative to $\mathscr{P}^{+}$) provided us with an implication algorithm in the previous section.

Malvestuto (1992) has independently observed this equivalence and used it to produce an indirect proof of Theorem 15 by showing that MVD and saturated independence statements must satisfy the same set of axioms.

The complexity of the implication algorithm for saturated statements relative to $\mathscr{P}$ [Beeri (1980)] differs from that needed relative to $\mathscr{P}^{+}$; the former requires $O\left(|\Sigma| \cdot n^{2}\right)$ operations to decide $\Sigma \vDash \sigma$ for each $\sigma$, while the latter requires only $O(n)$ operations, regardless of $|\Sigma|$. These savings are achieved at the cost of investing $O\left(|\Sigma| \cdot n^{2}\right)$ steps in constructing a graphical representation of the closure of $\Sigma$ (relative to $\mathscr{P}^{+}$), but this cost is encountered only once. This difference in complexity can be significant since, in principle, $|\Sigma|$ can be exponential in $n$.
7. Marginal independence. This section summarizes two completeness results for statements of the form $I(X, Y \mid \varnothing)$ (marginal statements).

Theorem 16 (Completeness). Let $\Sigma$ be a set of marginal statements, and let $\Sigma^{+}$be the closure of $\Sigma$ with respect to axioms (12) through (15). Then for every marginal statement $\sigma=I(X, Y \mid \varnothing)$ not in $\Sigma^{+}$, there exists a binary probability model ( $d_{\sigma}, P_{\sigma}$ ) that satisfies $\Sigma^{+}$and does not satisfy $\sigma$.

Marginal trivial independence:

$$
I(X, \varnothing \mid \varnothing)
$$

Marginal symmetry:

$$
I(X, Y \mid \varnothing) \Rightarrow I(Y, X \mid \varnothing)
$$

Marginal decomposition:

$$
I(X, Y \cup W \mid \varnothing) \Rightarrow I(X, Y \mid \varnothing)
$$

Marginal mixing:

$$
I(X, Y \mid \varnothing), I(X \cup Y, W \mid \varnothing) \Rightarrow I(X, Y \cup W \mid \varnothing)
$$

The proof of Theorem 16 uses the same technique as that of Theorem 15. It can be found in Geiger, Paz and Pearl (1991), together with an $O\left(|\Sigma| \cdot n^{2}\right)$ implication algorithm that is based on these axioms. The implication algorithm and the axiomatization hold relative to $\mathscr{B}$ and $\mathscr{P}$.

Definition. A Gaussian model over a finite set of attributes $U=$ $\left\{u_{1}, \ldots, u_{n}\right\}$ is a pair $(d, P)$, where $d$ is a domain mapping that maps each $u_{i}$ to $(-\infty,+\infty)$, and $P: d\left(u_{1}\right) \times \cdots \times d\left(u_{n}\right) \rightarrow[0,1]$ is a multivariate Gaussian probability distribution. (For the sake of brevity, we will not define multivariate Gaussian probability distributions.) The class of Gaussian models is denoted by $\mathscr{N}$.

Gaussian models share stronger properties for marginal independence than the ones listed previously; in particular, it is well known that Gaussian models satisfy the following additional property:

Marginal composition:

$$
I(X, Y \mid \varnothing), I(X, W \mid \varnothing) \Rightarrow I(X, Y \cup W \mid \varnothing)
$$

Theorem 17 shows that marginal composition is the only axiom that was "missing" relative to Gaussian models.

Theorem 17 (Completeness). Let $\Sigma$ be a set of marginal statements, and let $\Sigma^{+}$be the closure with respect to marginal trivial independence, marginal symmetry, marginal decomposition and marginal composition. Then there exists a Gaussian model that satisfies all statements in $\Sigma^{+}$and none other.

Proof. Let $U=u_{1}, \ldots, u_{n}$ be the attributes of interest. Let $P$ be a zero-mean multivariate normal distribution, with the following covariance matrix:

$$
\Gamma=\left(\rho_{i, j}\right) \quad \text { where } \rho_{i, j}= \begin{cases}0, & \text { if } \exists I(X, Y \mid \varnothing) \in \Sigma \text { s.t. } u_{i} \in X, u_{j} \in Y \\ \rho, & \text { otherwise }\end{cases}
$$

where $\rho^{2} \ll 1$. Simple algebra shows that this matrix is positive definite.
We need to show that $P$ satisfies $\Sigma^{+}$and no other marginal statement or, equivalently, that $I(X, Y \mid \varnothing) \in \Sigma$ if and only if $I(X, Y \mid \varnothing)$ holds for $P$. This is

proven by the following chain of relationships:

$$
\begin{aligned}
& I(X, Y \mid \varnothing) \in \Sigma^{+} \text {iff } \forall u_{i} \in X, u_{j} \in Y, I\left(u_{i}, u_{j} \mid \varnothing\right) \in \Sigma^{+} \text {iff } \\
& \forall u_{i} \in X, u_{j} \in Y, \rho_{i, j}=0 \text { iff } \forall u_{i} \in X, u_{j} \in Y, I\left(u_{i}, u_{j} \mid \varnothing\right) \\
& \text { holds for } P \text { iff } I(X, Y \mid \varnothing) \text { holds for } P .
\end{aligned}
$$

The first and last equivalences hold due to marginal decomposition and composition, making any statement $I(X, Y \mid \varnothing)$ completely determined by statements on singletons. The second equivalence holds by the construction of $\Gamma$ and the third equivalence is a property of normal distributions.

The construction of the matrix $\Gamma$ requires $O\left(|\Sigma| \cdot n^{2}\right)$ steps, where $n$ is the number of attributes appearing in statements of $\Sigma$. Testing whether a marginal statement $I(X, Y \mid \varnothing)$ is entailed (relative to Gaussian models) by a set of marginal statements amounts to checking that $\rho_{i, j}=0$ for every $u_{i} \in X$ and $u_{j} \in Y$, which requires on the order of $n^{2}$ steps.
8. Nonaxiomatizability of conditional independence. The previous two sections provide finite sets of Horn axioms for marginal and saturated independence statements. These axiom sets remain fixed when the size of $U$ increases because our proofs depend only on the finiteness of $|U|$ but not on its actual size. Unfortunately, analogous results for independence statements (without restrictions) cannot be obtained.

Theorem 18 [Studeny (1992)]. There exists no finite set of Horn axioms for independence statements (relative to $\mathscr{P}$ ) that is complete for every finite $|U|$.

Studeny proved the preceding theorem by presenting an infinite set of Horn axioms for conditional independence that is not implied by any finite set of such axioms.

The nonexistence of a complete set of axioms does not exclude the possibility of an efficient implication algorithm for conditional independence; Sagiv and Walecka (1982) provide an example of a class of sentences, called Z-EMVD, which admits an efficient polynomial implication algorithm but for which there exists no finite set of axioms. Nevertheless, we make the following conjecture.

Conjecture 2. The task of determining whether an independence statement is entailed (in $\mathscr{P}$ ) by a set of independence statements requires at least exponential time.

Moreover, the preceding task might even be undecidable; that is, there might exist no algorithm for deciding entailment of conditional independence. For related problems, consult Fagin and Vardi (1986).

9. Qualitative independence. Similar to conditional independence, we can define a qualitative independence statement $\hat{I}(X, Y \mid Z)$ by saying that $\hat{I}(X, Y \mid Z)$ holds for $P$ if

$$
P(\mathbf{X}, \mathbf{Y}, \mathbf{Z})>0 \text { and } P(\mathbf{Z})>0 \quad \text { iff } P(\mathbf{X}, \mathbf{Z})>0 \text { and } P(\mathbf{Y}, \mathbf{Z})>0
$$

for every respective value of $\mathbf{X}, \mathbf{Y}$ and $\mathbf{Z}$.
This definition is identical to that of EMVD in database theory and is also discussed by Shafer, Shenoy and Mellouli (1988). Theorems 5, 14 and 15 hold when $I$ is replaced with $\hat{I}$. For details consult Geiger (1990).
10. Summary. Table 1 summarizes properties of classes of probability models versus classes of independence statements. A question mark means that the problem remains open as of the writing of this article. The symbol $\mathscr{N}$ denotes the class of normal models and $\mathscr{B}$ probability models over binary variables.

Some properties of Gaussian models are listed in Table 1 which have not been proven in this article. The axioms for saturated independence (relative to $\mathscr{N}$ ) consist of trivial independence, symmetry, weak union and intersection [Geiger (1990)]. The fact that perfect Gaussian models do not exist for some sets of statements can be proven in the same way as in Corollary 8 (with the same $\Sigma$ selected). The nonexistence of a finite set of Horn axioms can be proven in the same way as in Theorem 18.

In addition, we have shown a strong relationship between graph separation and conditional independence. In particular, every undirected graph represents a consistent set of independence and dependence statements (Theorem 11), every axiom for conditional independence is also an axiom for graph separation (Theorem 10) and saturated separation and saturated independence (relative

Table 1
Properties of conditional independence


to $\mathscr{P}^{+}$) share the same axiomatic structure (Theorems 13 and 14). Analogous correspondence exists between separation in directed acyclic graphs ( $d$-separation) and conditional independence. See Geiger and Pearl (1988) and Verma (1986) for details.

Acknowledgments. Our notation and definitions were influenced by Beeri, Fagin and Howard (1977) and Fagin (1976). We are indebted to Ron Fagin for pointing out the usefulness of the notion of Armstrong models. We thank Azaria Paz for his help in proving Theorem 13 by referring us to Paz (1987), and to Norman Dalkey and Thomas Verma for many useful discussions. We also thank Glenn Shafer and several reviewers for suggesting numerous improvements on earlier drafts.
