# VALUATION-BASED SYSTEMS FOR BAYESIAN DECISION ANALYSIS 

PRAKASH P. SHENOY<br>The University of Kansas, Lawrence, Kansas<br>(Received June 1990; revision received May 1991; accepted May 1991)


#### Abstract

This paper proposes a new method for representing and solving Bayesian decison problems. The representation is called a valuation-based system and has some similarities to influence diagrams. However, unlike influence diagrams which emphasize conditional independence among random variables, valuation-based systems emphasize factorizations of joint probability distributions. Also, whereas influence diagram representation allows only conditional probabilities, valuationbased system representation allows all probabilities. The solution method is a hybrid of local computational methods for the computation of marginals of joint probability distributions and the local computational methods for discrete optimization problems. We briefly compare our representation and solution methods to those of influence diagrams.


The main goal of this paper is to propose a new method for representing and solving Bayesian decision problems. We propose a new representation of a decision problem called a valuation-based system. A graphical depiction of a valuation-based system is called a valuation network. Valuation networks are similar in some respects to influence diagrams. Like influence diagrams, valuation networks are a compact representation emphasizing qualitative features of decision problems. Also, like influence diagrams, valuation networks allow representation of decision problems without any preprocessing. However, there are some differences. Whereas influence diagrams emphasize conditional independence among random variables, valuation networks emphasize factorizations of joint probability distributions. Also, the representation method of influence diagrams allows only conditional probabilities. While conditional probabilities are readily available in pure causal models, they are not always readily available in other graphical models (see, for example, Darroch, Lauritzen and Speed 1980). The representation method of valuation-based systems is more general and allows direct representation of all probability models.

The solution method proposed is a hybrid of local computational methods for computations of the marginals of joint probability distributions and local
computational methods for discrete optimization. Local computational methods for computation of the marginals of joint probability distributions have been proposed by, e.g., Pearl (1988), Lauritzen and Spiegelhalter (1988), Shafer and Shenoy (1988, 1990), Jensen, Lauritzen and Oleson (1990), and Jensen, Olesen and Anderson (1990). Local computational methods for discrete optimization are also called nonserial dynamic programming (Bellman 1957, Bertele and Brioschi 1972). Viewed abstractly using the framework of valuation-based systems, these two local computational methods are actually quite similar. Shenoy and Shafer (1990) and Shenoy (1991b) show that the same three axioms justify the use of local computation in both cases.

Valuation-based systems are described in Shenoy (1989, 1991c). In valuation-based systems, we represent knowledge by functions called valuations. We draw inferences from such systems using two operations called combination and marginalization. Drawing inferences can be described simply as marginalizing all variables out of the joint valuation. The joint valuation is the result of combining all valuations. The framework of valuation-based systems is powerful enough to also include Dempster-Shafer theory of belief functions (Shenoy 1991c), Spohn's theory of epistemic beliefs (Shenoy 1991a, c),

[^0]
[^0]:    Subject classifications: Decision analysis, theory: representation, and solution using local computation. Dynamic programming, Markov, finite state: solution using local computation. Networks/graphs: representation for decision, optimization and probabilistic inference problems. Area of review: Decision Analysis, Bargaining and Negotiation.

possibility theory (Dubois and Prade 1990), propositional logic (Shenoy 1990a), and constraint satisfaction problems (Shenoy and Shafer 1988).

Traditional methods of representing problems in decision theory are payoff matrices and decision trees. The payoff matrix representation has its origins in the work of von Neumann and Morgenstern (1953) on normal form games and was made popular by Savage (1950). It is a convenient representation in problems where there is one decision to be made and one common uncertainty for all acts. In multistage decision problems, a payoff matrix representation requires the enumeration of possible strategies and the computation of the joint distribution of all random variables. Each of these two tasks can be computationally intractable due to combinatorial explosion.

A decision tree is a more flexible and graphic representation tool especially for multistage decision problems. Decision trees have their genesis in the work of von Neumann and Morgenstern on extensive form games. One distinct advantage of decision trees is that an optimal strategy can be identified using dynamic programming methods without enumerating all possible strategies (Zermelo 1913, Bellman 1957, Raiffa and Schlaifer 1961). Raiffa and Schlaifer call the dynamic programming method for solving decision trees "averaging-out-and-folding-back."

Although decision trees are more expressive and computationally more efficient than payoff matrices, decision trees have several drawbacks. First, since decision trees explicitly represent acts and events, the trees grow too fast in many problems. Thus, an $n$ stage decision problem with $m$ choices or events at each stage has at least $m^{n}$ endpoints.

Second, probabilities of events may not be available in the form that decision tree methodology requires. In such cases, it is necessary to compute these probabilities from the available probabilities using the laws of probability theory. This is a major drawback of decision trees. There should be a cleaner way of separating a representation of a problem from its solution. The former is hard to automate while the latter is easy. Decision trees mix these two tasks making automation difficult. The problem of finding marginals from a factored representation of the joint distribution has received much attention in the literature on uncertainty in artificial intelligence (e.g., Pearl 1988, Shafer and Shenoy 1988, 1990, Lauritzen and Spiegelhalter 1988, Jensen, Olesen and Andersen 1990, and Jensen, Lauritzen and Olesen 1990).

Third, the decision tree representation demands conditional probability distributions at each random variable node. This demand often necessitates division
operations (in the preprocessing of probabilities) that may be unnecessary. The uncessary divisions are compensated for by multiplications that neutralize the divisions. These unnecessary divisions and multiplications make the decision tree solution process inefficient.

Influence diagrams were initially proposed as an alternative to decision trees for represent decision problems (Miller et al. 1976, Howard and Matheson 1984). Subsequently, Olmsted (1983) and Shachter (1986) devised methods for solving influence diagrams directly (without having to convert them to decision trees). In the last decade, influence diagrams have become popular for representing and solving decision problems (Oliver and Smith 1990).

Influence diagrams do not share some of the drawbacks of decision trees mentioned above. First, since acts and events are not graphically depicted, influence diagrams do not grow as fast as decision trees. Second, users can input conditional probabilities directly in the form they are available without having to compute the posteriors. The computation of the posteriors is part of the process of solving influence diagrams (Olmsted 1983, Shachter 1986, Tatman 1986, Ezawa 1986, Tatman and Shachter 1990). The process of solving influence diagrams involves arc reversals and node removals. Although the process of solving influence diagrams is more complex than the process of solving decision trees, the process can easily be automated (Shachter 1988).

The representation method of influence diagrams allows only conditional probabilities. While conditional probabilities are readily available in pure causal models, they are not always available in other graphical models (see, e.g., Darroch, Lauritzen and Speed 1980, Wermuth and Lauritzen 1983, Edwards and Kreiner 1983, Kiiveri, Speed and Carlin 1984). In such cases, the probabilities have to be preprocessed before they can be represented in influence diagrams. The representation method of valuation-based systems is more general-all probability models can be represented directly without any preprocessing.

The arc reversal operation in influence diagrams involves unnecessary divisions. As in decision trees, these unnecessary operations are the result of influence diagram representation requirements that allow only conditional probabilities. The solution method for valuation-based systems described in this paper involves minimal division. If there is only one joint utility function (in unfactored form), then our method involves no divisions. This assumption of one joint utility function is similar to the assumption in influence diagrams that there is only one value node (see,

e.g., Shachter 1986). Also, if we have a factorization of the joint probability distributions into conditionals and the ordering of the variables is consistent in some sense with the information constraints, then again, our method involves no divisions. Finally, if the combination of valuations is associative, as, for example, it is if the joint utility function factors multiplicatively, then again no divisions are necessary. In general, if we want to take computational advantage of an additive factorization of the joint utility function, then divisions may be necessary.

An outline of this paper is as follows. In Section 1, we give a complete statement, decision tree representation, and decision tree solution of the oil wildcatter's problem (Raiffa 1968). We use the oil wildcatter's problem to illustrate all definitions in the paper. In Section 2, we describe valuation-based systems specifically designed for the representation and solution of Bayesian decision problems. In Section 3, we define combination and marginalization operations used for solving valuation-based systems. In Section 4, we describe the semantics of a valuation-based system representation, and the conditions under which such a representation is well defined. In Section 5, we describe a fusion algorithm for solving valuationbased systems using local computation. In Section 6, we compare valuation-based systems to influence diagrams. In Section 7, we make some concluding remarks. Finally, Section 8 contains a proof of the main theorem in the paper.

## 1. THE OIL WILDCATTER'S PROBLEM

The oil wildcatter's problem is reproduced with minor modifications from Raiffa. An oil wildcatter must decide either to drill $(d)$ or not drill $(\sim d)$. He is uncertain whether the hole is dry ( $d r$ ), wet (we) or soaking (so). Table I gives his monetary payoffs and his subjective probabilities of the various states. The cost of drilling is $\$ 70,000$. The net return associated with the $d$-we pair is $\$ 50,000$, which is interpreted as a return of $\$ 120,000$ less the $\$ 70,000$ cost of drilling. Similarly, the $\$ 200,000$ associated with the $d$-so pair

Table I
The Payoff Matrix for the Oil Wildcatter's Problem


Table II
Probabilities of Seismic Test Results Conditional on the Amount of Oil


is a net return (a return of $\$ 270,000$ less the $\$ 70,000$ cost of drilling).

At a cost of $\$ 10,000$, the wildcatter could take seismic soundings which will help determine the geological structure at the site. The soundings will disclose whether the terrain below has no structure ( $n s$ )(that's bad), or an open structure (os) (that's so-so), or a closed structure (cs) (that's really hopeful). The experts have provided us with Table II which shows the probabilities of seismic test results conditional on the amount of oil.
![img-0.jpeg](img-0.jpeg)

Figure 1. The preprocessing of probabilities in the oil wildcatter's problem.

Figures 1 and 2 show a decision tree representation and solution of this problem. Note that even before the decision tree can be specified completely the conditional probabilities in the tree have to be computed from those specified in the problem, as in Figure 1. In Figure 1, the probability tree on the left is used to compute the joint probabilities, and the probability tree on the right is used to compute the marginals for test results and the conditional probabilities of the amount of oil given test results. As we will see later, all computations in the probability tree on the right are unnecessary.

Figure 2 shows the solution of the oil wildcatter's problem. The optimal strategy is to do a seismic test, not drill if the seismic test reveals no structure, and

![img-1.jpeg](img-1.jpeg)

Figure 2. A decision tree representation and solution of the oil wildcatter's problem.
drill if the seismic test reveals either open or closed structure. The expected profit associated with this strategy is $\$ 22,500$.

## 2. VALUATION-BASED SYSTEM REPRESENTATION

A valuation-based system representation of decision problems uses decision varibles, random variables, frames, payoff valuations, potentials, and precedence constraints. We will discuss each of these in detail. A graphical representation of these objects is called a valuation network. Figure 3 shows a valuation network for the oil wildcatter's problem.

### 2.1. Variables, Frames and Configurations

A decision node is represented as a variable. The possible values of a decision variable represent the acts available at that point. We use the symbol $\mathscr{O}_{D}$ for the set of possible values of decision variable $D$. We assume that the decision-maker has to pick one and only one of the elements of $\mathscr{O}_{D}$ as their decision. We call $\mathscr{O}_{D}$ the frame for $D$. Decision variables are represented in a valuation network by rectangular nodes.

In the oil wildcatter's problem, there are two decision nodes $D$ and $T$. The frame for $D$ has two acts: drill $(d)$, and not drill $(\sim d)$. The frame for $T$ also has
two elements: do a seismic test $(t)$, and not do a seismic test $(\sim t)$.
If $R$ is a random variable, we use the symbol $\mathscr{O}_{R}$ to denote its possible values. We assume that one and only one of the elements of $\mathscr{O}_{R}$ can be the true value of $R$. We call $\mathscr{O}_{R}$ the frame for $R$. Random variables are denoted in valuation networks by circular nodes.
In the oil wildcatter's problem, there are two random variables: amount of oil $(O)$ and seismic test results $(R)$. The frame for $O$ has three elements: dry ( $d r$ ), wet ( $w e$ ), and soaking ( $s o$ ). The frame for $R$ has four elements: no result ( $n r$ ), no structure ( $n s$ ), open structure (os), and closed structure (cs).
Let $\mathscr{R}_{D}$ denote the set of all decision variables, let $\mathscr{R}_{R}$ denote the set of all random variables, and let $\mathscr{R}=\mathscr{R}_{D} \cup \mathscr{R}_{R}$ denote the set of all variables. In this paper, we are concerned only with the case where $\mathscr{R}$ is finite. We also assume that all the variables in $\mathscr{R}$ have finite frames. We use upper-case Roman alphabets to denote variables.
We often deal with nonempty subsets of variables in $\mathscr{R}$. Given a nonempty subset $h$ of $\mathscr{R}$, let $\mathscr{O}_{h}$ denote the Cartesian product of $\mathscr{O}_{X}$ for $X$ in $h$, i.e., $\mathscr{O}_{h}=$ $\times\left\{\mathscr{O}_{X} \mid X \in h\right\}$. We can think of $\mathscr{O}_{h}$ as the set of possible values of the joint variable $h$. Accordingly, we call $\mathscr{O}_{h}$ the frame for $h$. Also, we refer to elements of $\mathscr{O}_{h}$ as configurations of $h$. We use this terminology even when $h$ consists of a single variable, say $X$. Thus, we refer to elements of $\mathscr{O}_{X}$ as configurations of $X$. We use lower case, boldface letters, such as $\mathbf{x}$ and $\mathbf{y}$, to denote configurations. Also, if $\mathbf{x}$ is a configuration of $g, \mathbf{y}$ is a configuration of $h$, and $g \cap h=\varnothing$, then $(\mathbf{x}, \mathbf{y})$ denotes a configuration of $g \cup h$.
It is convenient to extend this terminology to the case where the set of variables $h$ is empty. We adopt the convention that the frame for the empty set $\varnothing$ consists of a single configuration, and we use the symbol to name that configuration; $\mathscr{O}_{0}=\{\boldsymbol{\phi}\}$. To
![img-2.jpeg](img-2.jpeg)

Figure 3. A valuation network for the oil wildcatter's problem.

be consistent with this notation, we adopt the convention that if $\mathbf{x}$ is a configuration for $g$, then $(\mathbf{x}, \boldsymbol{\nabla})=\mathbf{x}$.

### 2.2. Valuations

Suppose that $h \subseteq \mathscr{L}$. A payoff valuation $\pi$ for $h$ is a function from $\mathscr{L}_{h}$ to $\mathbb{R}$, where $\mathbb{R}$ denotes the set of real numbers. The values of payoff valuations are consequences, for example, utilities, profit, and cost. If $h=$ $d \cup r$, where $d \subseteq \mathscr{L}_{D}$ and $r \subseteq \mathscr{L}_{R}, \mathbf{x} \in \mathscr{L}_{d}$, and $\mathbf{y} \in \mathscr{L}_{r}$, then $\pi(\mathbf{x}, \mathbf{y})$ denotes a partial payoff to the decision maker if the decision maker chooses configuration $\mathbf{x}$ and the true configuration of $r$ is $\mathbf{y}$. The exact meaning of a payoff valuation is given in Section 4. If $\pi$ is a payoff valuation for $h$ and $X \in h$, then we say that $\pi$ bears on $X$.

In a valuation network, a payoff valuation is represented by a diamond-shaped node. To permit the identification of all valuations that bear on a variable, we draw undirected edges between the payoff valuation node and all the variable nodes it bears on. In the oil wildcatter's problem, there are two payoff valuations $\pi$ and $\kappa$, as shown in Figure 3. Table III shows the details of these valuations.

Suppose that $h \subseteq \mathscr{L}$ such that $h \cap \mathscr{L}_{R} \neq \varnothing$. A potential $\rho$ for $h$ is a function from $\mathscr{L}_{h}$ to the unit interval $[0,1]$. The values of potentials are probabilities. The exact meaning of a potential is given in Section 4.

In a valuation network, a potential is represented by a triangular node. Again, to permit the identification of valuations that bear on a variable, we draw undirected edges between a potential node and all the variables nodes it bears on.

Suppose that $h \subseteq \mathscr{L}, R$ is a random variable in $h$, and $\rho$ is a potential for $h$. If all the values of $\rho$ represent conditional probabilities for $R$ given configurations of the variables in $h-\{R\}$, then we call $\rho$ a conditional potential for $R$ given $h-\{R\}$. In this case, $\rho$ satisfies
$\sum\left\{\rho(\mathbf{c}, \mathbf{r})\left|\mathbf{r} \in \mathscr{L}_{R}\right|=1\right.$ for all $\mathbf{c} \in \mathscr{L}_{h-\{R\}}$.

Table III
Payoff Valuations in the Oil Wildcatter's Problem


Table IV
Potentials in the Oil Wildcatter's Problem


${ }^{a}$ Only nonzero probability values of $\mu$ are shown.

In a valuation network, a conditional potential $\rho$ for $R$ given $h-\{R\}$ is represented by making the edge between the potential node $\rho$ and the variable node $R$ directed (pointed toward $R$ ). In the oil wildcatter's problem, there are two potentials $\rho$ and $\mu$, as shown in Figure 3. Table IV shows the details of these potentials. Note that $\mu$ is a conditional potential for $R$ given $\{T, O\}$, and $\rho$ is a conditional potential for $O$ given $\varnothing$.

In a valuation network, both variables and valuations are represented by nodes. To help the reader keep these objects separate, we use upper case Roman alphabets to label variables and lower case Greek alphabets to label valuations.

Let $\mathscr{L}_{D}$ denote the set of subsets of $\mathscr{L}$ for which payoff valuations exist in the valuation-based system. For simplicity of exposition, we assume that each decision variable in $\mathscr{L}_{D}$ is included in some element of $\mathscr{L}_{D}$, i.e.,
$\cup \mathscr{L}_{D} \supseteq \mathscr{L}_{D}$.
Let $\mathscr{L}_{R}$ denote the set of subsets of $\mathscr{L}$ for which potentials exist. We assume that each random variable is included in some element of $\mathscr{L}_{R}$, i.e.,
$\cup \mathscr{L}_{R} \supseteq \mathscr{L}_{R}$.
$\mathscr{L}=\mathscr{L}_{D} \cup \mathscr{L}_{R}$. From (2) and (3), it is clear that $\cup \mathscr{L}=\mathscr{L}$. Using the language of graph theory, the set $\mathscr{L}$ is called a hypergraph on $\mathscr{L}$, and each of its elements is called a hyperedge. We call $\mathscr{L}_{D}$ the payoff hypergraph and $\mathscr{L}_{R}$ the potential hypergraph.

### 2.3. Precedence Constraints

Besides acts, events, probabilities and payoffs, an important ingredient of problems in decision analysis

is information constraints. Some decisions have to be made before the observation of some uncertain events, and some decisions can be postponed until some events are observed. In the oil wildcatter's problem, for example, the amount of oil is revealed only after the ground is drilled or perhaps it is never revealed; the decision whether to drill or not may be postponed until the seismic test result is revealed.

If a decision-maker expects to be informed of the true value of random variable $R$ before they make a decision $D$, then we represent this situation by the binary relation $R \rightarrow D$ (read as $R$ precedes $D$ ). On the other hand, if a random variable $R$ is only revealed after a decision $D$ is made or perhaps never revealed, then we represent this situation by the binary relation $D \rightarrow R$. It is possible that in some problems, we may have precedence constraints between two decision nodes or between two random variable nodes. For example, if random variable $R_{2}$ is only revealed after random variable $R_{1}$ is revealed, we represent this by the relation $R_{1} \rightarrow R_{2}$.

In the oil wildcatter's problem, we have the precedence constraints $T \rightarrow R, R \rightarrow D, D \rightarrow O$. The seismic test result $(R)$ is only revealed after we make the decision to do a seismic test or not $(T)$. The decision to drill or not to drill $(D)$ is only made after observing the test results $(R)$. Finally, the amount of oil $(O)$ is only revealed if we make the decision to drill $(D)$. Obviously, these are not the only constraints. In the oil wildcatter's problem we also have, for example, $T \rightarrow O$. But such constraints can be deduced, and there is no reason to include all such constraints in the representation. On the other hand, the problem can incorrectly be overconstrained, permitting no solution. For example, if $T \rightarrow R$ and $R \rightarrow T$, then this will preclude a solution. Therefore, we do not permit such precedence constraints.

What restrictions do we need to impose on the precedence relation $\rightarrow$ ? We require four conditions. First, we require that the transitive closure of $\rightarrow$, denoted by $>$, is a partial order on $\mathscr{R}$. We call this first condition the partial order condition. Second, we require that this partial order $>$ is such that for any $D \in \mathscr{R}_{D}$ and any $R \in \mathscr{R}_{R}$, either $D>R$ or $R>D$. We call this second condition the perfect recall condition. (This terminology is borrowed from Kuhn (1953). In the influence diagram literature, this condition is called the "no-forgetting assumption" (Howard and Matheson 1984).) Third, if $R$ is a random variable such that there exists a conditional potential for $R$ given $h-R$, and if $D$ is a decision variable in $h$, then we require that $D>R$. Fourth, if $D$ is a decision variable and there exists a potential for $h$ such
that $D \in h$, then we require that $D>R$ for some random variable $R \in h$. We call the third and fourth conditions consistency conditions.

Before we explain the reasons for these three conditions, let us explain the terms transitive closure and partial ordering. The transitive closure of $\rightarrow$ is defined as:
i. $X>Y$ whenever $X \rightarrow Y$, and
ii. $X>Y$ whenever there exists a $Z \in \mathscr{R}$ such that $X>Z$ and $Z>Y$.

A binary relation $>$ is a partial order on $\mathscr{R}$ if it satisfies the following two properties:
i. (Irreflexive): $X>X$ for no $X \in \mathscr{R}$.
ii. (Transitive): $X>Y$ and $Y>Z$ imply $X>Z$.

The reason for the partial order requirement is obvious. The reason for the perfect recall condition is as follows. Given the meaning of the precedence relation $\rightarrow$, for any decision variable $D$ and any random variable $R$, either $R$ is known when decision $D$ has to be made, or not. This translates to either $R>D$ or $D>R$. Finally, the consistency conditions are dictated by the meaning of potentials. If the conditional probability distribution of random variable $R$ depends on the act chosen by the decision maker at node $D$, then it must be the case that $D>R$.

In summary, a valuation-based system representation of a decision problem consists of a finite set of decision variables $\mathscr{R}_{D}$, a finite set of random variables $\mathscr{R}_{R}$, a finite frame $\mathscr{R}_{X}$ for each variable $X$ in $\mathscr{R}_{D} \cup \mathscr{R}_{R}$, a finite collection of payoff valuations $\left\{\pi_{1}, \ldots, \pi_{m}\right\}$, a finite collection of potentials $\left\{\rho_{1}, \ldots, \rho_{n}\right\}$, and a precedence relation $\rightarrow$ on $\mathscr{R}_{D} \cup \mathscr{R}_{R}$. Thus, a valuationbased system (VBS) can be denoted formally by the 6 -tuple
$\left\{\mathscr{R}_{D}, \mathscr{R}_{R},\left\{\mathscr{W}_{X}\right\}_{X \in \mathscr{R}},\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\} \rightarrow\right\}$
representing decision variables, random variables, frames, payoff valuations, potentials, and the precedence relation, respectively.

## 3. COMBINATION AND MARGINALIZATION

In this section, we define two operations called combination and marginalization. We use these operations to solve valuation-based systems. Precise definitions require extensive notation that will test the patience of the reader. For relief, we use the oil wildcatter's problem to illustrate all definitions. First, we start with some notation we need to define combination and marginalization.

### 3.1. Projection of Configurations

Projection of configurations simply means dropping extra coordinates; if ( $w, x, y, z$ ) is a configuration of $\{W, X, Y, Z\}$, for example, then the projection of ( $w, x, y, z$ ) to $\{W, X\}$ is simply ( $w, x$ ), which is a configuration of $\{W, X\}$.

If $g$ and $h$ are sets of variables, $h \subseteq g$, and $\mathbf{x}$ is a configuration of $g$, then let $\mathbf{x}^{\downarrow h}$ denote the projection of $\mathbf{x}$ to $h$. The projection $\mathbf{x}^{\downarrow h}$ is always a configuration of $h$. If $h=\mathrm{g}$ and $\mathbf{x}$ is a configuration of $g$, then $\mathbf{x}^{\downarrow h}=\mathbf{x}$. If $h=\varnothing$, then $\mathbf{x}^{\downarrow h}=$ ・

### 3.2. Combination

The definition of combination depends on the type of valuations being combined. Suppose that $h$ and $g$ are subsets of $\mathscr{L}, \pi_{i}$ is a payoff valuation for $h$, and $\pi_{j}$ is a payoff valuation of $g$. Then the combination of $\pi_{i}$ and $\pi_{j}$, denoted by $\pi_{i} \otimes \pi_{j}$, is a payoff valuation for $h \cup g$ defined as
$\left(\pi_{i} \otimes \pi_{j}\right)(\mathbf{x})=\pi_{i}\left(\mathbf{x}^{\downarrow h}\right)+\pi_{j}\left(\mathbf{x}^{\downarrow g}\right)$
for all $\mathbf{x} \in \mathscr{H}_{h \cup g}$.
Suppose that $h$ and $g$ are subsets of $\mathscr{R}, \pi_{i}$ is a payoff valuation of $h$, and $\rho_{j}$ is a potential for $g$. Then the combination of $\pi_{i}$ and $\rho_{j}$, denoted by $\pi_{i} \otimes \rho_{j}$, is a payoff valuation for $h \cup g$ defined as
$\left(\pi_{i} \otimes \rho_{j}\right)(\mathbf{x})=\pi_{i}\left(\mathbf{x}^{\downarrow h}\right) \rho_{j}\left(\mathbf{x}^{\downarrow g}\right)$
for all $\mathbf{x} \in \mathscr{H}_{h \cup g}$. And the combination of $\rho_{j}$ and $\pi_{i}$, denoted by $\rho_{j} \otimes \pi_{i}$, is a payoff valuation for $h \cup g$ defined as
$\rho_{j} \otimes \pi_{i}=\pi_{i} \otimes \rho_{j}$.
Suppose that $h$ and $g$ are subsets of $\mathscr{R}, \rho_{i}$ is a potential for $h$, and $\rho_{j}$ is a potential for $g$. Then the combination of $\rho_{i}$ and $\rho_{j}$, denoted by $\rho_{i} \otimes \rho_{j}$, is a potential for $h \cup g$ defined as
$\left(\rho_{i} \otimes \rho_{j}\right)(\mathbf{x})=\rho_{i}\left(\mathbf{x}^{\downarrow h}\right) \rho_{j}\left(\mathbf{x}^{\downarrow g}\right)$
for all $\mathbf{x} \in \mathscr{H}_{h \cup g}$.
First, note that the combination of two payoff valuations is a payoff valuation, the combination of two potentials is a potential, and the combination of a payoff valuation and a potential is a payoff valuation. This is consistent with the units of the values of the valuations because values of potentials are probabilities, which are dimensionless quantities.

Second, note that a combination of two payoff valuations consists of pointwise addition. This assumes that the joint payoff function factors additively as in the oil wildcatter's problem. (If it factored multiplicatively, we would have defined this combi-
nation as pointwise multiplication.) Combination of two potentials consists of pointwise multiplication. Probability theory mandates this. Finally, combination of a payoff valuation and a potential consists of pointwise multiplication. This is one of the operations in computing expected payoffs. (The other operation, summation, is part of the definition of marginalization given below.)

Third, note that combination is commutative. Also, the combination for payoff valuations is associative. Thus, if $\left\{\pi_{1}, \ldots, \pi_{k}\right\}$ is a set of payoff valuations, we write $\otimes\left\{\pi_{1}, \ldots, \pi_{k}\right\}$ to mean the combination of valuations in $\left\{\pi_{1}, \ldots, \pi_{k}\right\}$ in some sequence. Similarly, the combination of potentials is associative, and if $\left\{\rho_{1}, \ldots, \rho_{k}\right\}$ is a set of potentials, we write $\otimes\left\{\rho_{1} \ldots, \rho_{k}\right\}$ to mean the combination of potentials in $\left\{\rho_{1}, \ldots, \rho_{k}\right\}$ in some sequence. In general, the combination for a mixture of payoff valuations and potentials is not associative, e.g., $\left(\rho_{1} \otimes \pi_{1}\right) \otimes \pi_{2} \neq$ $\rho_{1} \otimes\left(\pi_{1} \otimes \pi_{2}\right)$. In such cases, what sequence should we use? We define combination such that the payoff valuations are combined before combining the potentials. Formally, suppose that $\pi_{1}, \ldots, \pi_{k}$ are payoff valuations, and $\rho_{1}, \ldots, \rho_{j}$ are potentials. Then let $\otimes\left\{\pi_{1}, \ldots, \pi_{k}, \rho_{1}, \ldots, \rho_{j}\right\}$ denote $\left(\otimes\left\{\pi_{1}, \ldots, \pi_{k}\right\}\right) \otimes$ $\left(\otimes\left\{\rho_{1}, \ldots, \rho_{j}\right\}\right)$. Finally, note that if we have only one payoff valuation and several potentials, then combination is associative. We can assume that we have only one payoff valuation by combining all payoff valuations before we combine the potentials.

Tables V and VI illustrate the combination operation using valuations from the oil wildcatter's problem.

### 3.3. Vacuous Potentials

Suppose that $\rho$ is a potential for $g$. We say that $\rho$ is vacuous if $\rho(\mathbf{r})=1$ for all $\mathbf{r} \in \mathscr{H}_{g}$. It follows from the definition of combination, that if $\mu$ is a potential for $g$ and $\rho$ is a vacuous potential for $g$, then $\rho \otimes \mu=\mu$.

### 3.4. Marginalization

Suppose that $h$ and $g$ are subsets of variables, and $g$ is a subset of $h$. Marginalization is an operation when we reduce a valuation for $h$ to a valuation for $g$ by eliminating variables in $h-g$. Unlike combination, the definition of marginalization does not depend on the type of valuation being marginalized. But the definition of marginalization depends on the type of variables being eliminated. If the variable being eliminated is random, marginalization is achieved by summing the valuation over the frame of the eliminated variable. In this case, the valuation being marginalized may be either a payoff valuation or a potential. If the -

Table V
Combination of Payoff Valuations $\pi$ and $\kappa$, and Potentials $\rho$ and $\mu$


variable being eliminated is a decision variable, marginalization is achieved by maximization (or minimization depending on the nature of the values of the payoff valuations) over the frame of the eliminated variable. In this case, the valuation being marginalized must be a payoff valuation. A formal definition of marginalization is as follows.

Suppose that $h$ is a subset of $\mathscr{L}$ containing random variable $R$, and $\alpha$ is a valuation for $h$. The marginal of $\alpha$ for $h-\{R\}$, denoted by $\alpha^{\lfloor(h-\{R\})}$, is a valuation for $h-\{R\}$ defined as
$\alpha^{\lfloor(h-\{R\})}(\mathbf{c})=\sum\left\{\alpha(\mathbf{c}, \mathbf{r}) \mid \mathbf{r} \in \mathscr{H}_{R}\right\}$
for all $\mathbf{c} \in \mathscr{H}_{h-\{R\}}$.
Suppose that $h$ is a subset of $\mathscr{L}$ containing decision variable $D$, and $\alpha$ is a payoff valuation for $h$. The marginal of $\alpha$ for $h-\{D\}$, denoted by $\alpha^{\lfloor(h-\{D)\}$, is a valuation for $h-\{D\}$ ) defined as
$\alpha^{\lfloor(h-\{D\}\{c)}=\operatorname{MAX}\left\{\alpha(\mathbf{c}, \mathbf{d}) \mid \mathbf{d} \in \mathscr{H}_{D}\right\}}$
for all $\mathbf{c} \in \mathscr{H}_{h-\{D\}}$.

Some observations: If $\alpha$ is a payoff valuation, then (8) corresponds to the second operation in "averaging out" a random variable. (The first operation is included in the combination operation.) On the other hand, if $\alpha$ is a potential, then (8) simply represents the familiar marginalization operation in probability theory. Table VI shows an example of marginalizing a random variable.

Condition 9 assumes that the nature of the values of a payoff valuation is such that the decision-maker's objective is to maximize it. This is true if the payoff values represent utility, profits, probability of success, etc. On the other hand, in some problems, the decision-maker may wish to minimize the payoff values, when they represent disutility, cost, probability of failure, etc. In this case, we need to substitute MIN for MAX in (9). Condition 9 corresponds to "foldingback." Table VII shows an example of marginalizing a decision variable.

We now state three lemmas regarding the marginalization operation. Lemma 1 states that in marginalizing two decision variables out of a valuation, the order in which the variables are eliminated does not affect the final result. Lemma 2 states a similar result for marginalizing two random variables out of a valuation. Lemma 3 states that in marginalizing a decision variable and a random variable out of a valuation, the order in which the two variables are eliminated may make a difference.

Lemma 1. Suppose that $h$ is a subset of $\mathscr{L}$ containing decision variables $D_{1}$ and $D_{2}$, and $\alpha$ is a payoff valuation for $h$. Then
$\left(\alpha^{\left.\left.\left.\left.\left.\left.D_{1}\right D_{1}\right]\right)\right\}\right\|(h-\left.\left.D_{1}, D_{2}\right]\right)}(\mathbf{c})=\left(\alpha^{\left.\left.\left.\left.\left.\left.D_{2}\right D_{2}\right]\right)\right\}\right\| h-\left.\left.D_{1}, D_{2}\right]\right)}(\mathbf{c})\right.\right.$
for all $\mathbf{c} \in \mathscr{H}_{h-\left\{D_{1}, D_{2}\right\}}$.
Proof. The proof follows trivially from the definition of marginalization.

Lemma 2. Suppose that $h$ is a subset of $\mathscr{L}$ containing random variables $R_{1}$ and $R_{2}$. and $\alpha$ is a valuation for h. Then
$\left(\alpha^{\left.\left.\left.\left.\left.\left.\left.\left.\left.D_{1}\right D_{1}\right]\right)\right\}\right\| h-\left.\left.R_{1}, R_{2}\right]\right)}(\mathbf{c})=\left(\alpha^{\left.\left.\left.\left.\left.\left.\left.\left.\left.D_{2}\right D_{2}\right]\right)\right\}\right\| h-\left.\left.R_{1}, R_{2}\right]\right)}(\mathbf{c})\right.\right.\right.\right.\right.$
for all $\mathbf{c} \in \mathscr{H}_{h-\left\{R_{1}, R_{2}\right\}}$.
Proof. The proof follows trivially from the definition of marginalization.

Lemma 3. Suppose that $h$ is a subset of $\mathscr{L}$ containing decision variable $D$ and random variable $R$, and $\alpha$ is

Table VI
Computation of $(\pi \otimes \kappa) \otimes \rho \otimes \mu$ and $((\pi \otimes \kappa) \otimes \rho \otimes \mu)^{\downarrow[T, R, D]}$


Table VII
Computation of $\tau^{\downarrow[T, R]}, \Psi_{D}, \tau^{\downarrow[T]}, \tau^{\downarrow 2}$, and $\Psi_{T}{ }^{a}$


${ }^{a} \tau$ denotes the joint valuation $(\pi \otimes \kappa) \otimes \rho \otimes \mu$.
a payoff valuation of $h$. Then
$\left(\alpha^{\downarrow(h-\{D\})}\right)^{\downarrow(h-\{R, D\})}(\mathbf{c}) \geqslant \alpha^{\downarrow(h-\{R\})} \downarrow(h-\{R, D\})(\mathbf{c})$
for all $\mathbf{c} \in \mathscr{H}_{h-\{R, D\}}$.
Proof. The proof follows trivially from the definition of marginalization.

It is clear from Lemma 3, that in marginalizing more than one variable, the order of elimination of
the variables may make a difference. As we will see shortly, we need to marginalize all variables out of the joint valuation. What sequence should we use? This is where the precedence constraints come into play. We define marginalization such that variable $Y$ is marginalized before $X$ whenever $X>Y$.

Suppose $h$ and $g$ are nonempty subsets of $\mathscr{L}$ such that $g$ is a proper subset of $h, \alpha$ is a valuation for $h$, and $>$ is a partial order on $\mathscr{L}$ satisfying the perfect recall condition. The marginal of $\alpha$ for $g$ with respect

to the partial order $>$, denoted by $\alpha^{\downarrow g}$, is a valuation for $g$ defined as
$\alpha^{\downarrow g}=\left(\left(\left(\alpha^{\left.\left.\downarrow h-\left|X_{1}\right|\right)\right)^{\left.\downarrow\left(h-\left|X_{1}, X_{2}\right|\right)}\right) \ldots . .\right)^{\left.\downarrow\left(h-\left|X_{1}, X_{2}, \ldots, X_{k}\right|\right.}\right.\right.$,
where $h-g=\left\{X_{1}, \ldots, X_{k}\right\}$, and $X_{1} X_{2} \ldots X_{k}$ is a sequence of variables in $h-g$ such that with respect to the partial order $>, X_{1}$ is a minimal element of $h-g, X_{2}$ is a minimal element of $h-g-\left|X_{1}\right|$, etc.

The marginalization sequence $X_{1} X_{2} \ldots X_{k}$ may not be unique because $>$ is only a partial order. But, since $>$ satisfies the perfect recall condition, it is clear from Lemmas 1 and 2, that the definition of $\alpha^{\downarrow g}$ in (10) is well defined.

### 3.5. Solution for a Variable

As we will see shortly, the main objective in solving a decision problem is computing an optimal strategy. Computing an optimal strategy is a matter of bookkeeping. Each time we eliminate a decision variable from a payoff valuation using maximization, we store a table of optimal values of the decision variables where the maximums are achieved. We can think of this table as a function. We call this function "a solution" for the decision variable. Formally, we define a solution as follows.

Suppose $h$ is a subset of variables such that decision variable $D \in h$, and $\pi$ is payoff valuation for $h$. A function $\Psi_{D}: \mathscr{H}_{h-|D|} \rightarrow \mathscr{H}_{D}$ is called a solution for $D$ (with respect to $\pi$ ) if
$\pi^{\downarrow(h-|D|)}(\mathbf{c})=\pi\left(\mathbf{c}, \Psi_{D}(\mathbf{c})\right)$
for all $\mathbf{c} \in \mathscr{H}_{h-|D|}$.
Table VII shows the solution for $D$ with respect to $((\pi \otimes \kappa) \otimes \rho \otimes \mu)^{\downarrow(T, R, D)}$, and the solution for $T$ with respect to $((\pi \otimes \kappa) \otimes \rho \otimes \mu)^{\downarrow(T)}$ in the oil wildcatter's problem.

### 3.6. Strategy

The main task in a decision problem is to compute an optimal strategy. What constitutes a strategy? Intuitively, a strategy is a choice of an act for each decision variable $D$ as a function of configurations of random variables $R$ such that $R>D$. Let $\operatorname{Pr}(D)=$ $\left\{R \in \mathscr{R}_{R} \mid R>D\right\}$. We call $\operatorname{Pr}(D)$ the predecessors of $D$. Thus, a strategy $\sigma$ is a collection of functions $\left\{\xi_{D}\right\}_{D \in \mathscr{R}_{D}}$ where $\xi_{D}: \mathscr{H}_{\operatorname{Pr}(D)} \rightarrow \mathscr{H}_{D}$.

Suppose that $\sigma=\left\{\xi_{D}\right\}_{D \in \mathscr{R}_{D}}$ is a strategy, and $\mathbf{y}$ is a configuration of $\mathscr{R}_{R}$. Then $\sigma$ and $\mathbf{y}$ together determine a unique configuration of $\mathscr{R}_{D}$. Let $\mathbf{a}_{\sigma, \mathbf{y}}$ denote this unique configuration of $\mathscr{R}_{D}$. By definition
$\mathbf{a}_{S, \mathbf{y}}^{\downarrow(D)}=\xi_{D}\left(\mathbf{y}^{\downarrow \operatorname{Pr}(D)}\right) \quad$ for all $D \in \mathscr{R}_{D}$.

In the next section, we will formally define the decision problem. Before we can do this, we will have to explain the semantics of a VBS representation.

## 4. WELL DEFINED VBS REPRESENTATIONS AND SEMANTICS

In this section, we describe when a VBS representation of a decision problem is well defined. We also describe the semantics of a well defined VBS representation. Suppose that
$\Delta=\left\{\mathscr{R}_{D}, \mathscr{R}_{R},\left\{\mathscr{H}_{X}\right\}_{X \in \mathscr{X}},\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\}, \rightarrow\right\}$
is a VBS representation of a decision problem. How can we tell if $\Delta$ is well defined? And, assuming that $\Delta$ is well defined, what does $\Delta$ mean? We will answer these two related questions in terms of a canonical decision problem.

### 4.1. Canonical Decision Problem

A canonical decision problem $\Delta_{C}$ consists of a single decision variable $D$ with a finite frame $\mathscr{H}_{D}$, a single random variable $R$ with a finite frame $\mathscr{H}_{R}$, a single payoff valuation $\pi$ for $\{D, R\}$, a single conditional potential $\rho$ for $R$ given $\{D\}$, and a precedence relation $\rightarrow$ defined by $D \rightarrow R$. Figure 4 shows a valuation network and a decision tree representation of the canonical decision problem.

The meaning of the canonical decision problem is as follows. The elements of $\mathscr{H}_{D}$ are acts, and the elements of $\mathscr{H}_{R}$ are states of nature. The conditional potential $\rho$ is a family of probability distributions for $R$, one for each act $\mathbf{d} \in \mathscr{H}_{D}$. In other words, the probability distribution of random variable $R$ is conditioned on the act $\mathbf{d}$ chosen by the decision maker. The probability $\rho(\mathbf{d}, \mathbf{r})$ can be interpreted as the conditional probability of $R=\mathbf{r}$ given that $D=\mathbf{d}$. Using
![img-3.jpeg](img-3.jpeg)

Figure 4. A VBS and a decision tree representation of the canonical decision problem.

our marginalization notation, (1) for a conditional potential can be written as
$\rho^{\| D \mid}$ is the vacuous potential for $D$, i.e., $\rho^{\| D \mid}(\mathbf{d})=1$

$$
\text { for all } \mathbf{d} \in \mathscr{O}_{D}
$$

The payoff valuation $\pi$ is a conditional payoff func-tion-if the decision maker chooses act $\mathbf{d}$ and the state of nature $\mathbf{r}$ prevails, then the payoff to the decision maker is $\pi(\mathbf{d}, \mathbf{r})$. The precedence relation $\rightarrow$ states that the true state of nature is revealed to the decision maker only after the decision maker has chosen an act.

Solving a canonical decision problem using the criterion of maximizing expected payoff is easy. The expected payoff associated with act $\mathbf{d}$ is
$\sum\left\{(\pi \otimes \rho)(\mathbf{d}, \mathbf{r}) \mid \mathbf{r} \in \mathscr{O}_{R}\right\}=(\pi \otimes \rho)^{\| D \mid}(\mathbf{d})$.
The maximum expected payoff (associated with an optimal act, say $\mathbf{d}^{*}$ ) is

$$
\begin{aligned}
& \operatorname{MAX}\left\{(\pi \otimes \rho)^{\| D \mid}(\mathbf{d}) \mid \mathbf{d} \in \mathscr{O}_{D}\right\} \\
& \quad=\left((\pi \otimes \rho)^{\| D \mid}\right)^{\| \varnothing}(\bullet)=(\pi \otimes \rho)^{\| \varnothing}(\bullet)
\end{aligned}
$$

Finally, act $\mathbf{d}^{*}$ is optimal if and only if
$(\pi \otimes \rho)^{\| D \mid}\left(\mathbf{d}^{*}\right)=(\pi \otimes \rho)^{\| \varnothing}(\bullet)$.
Consider the decision problem
$\Delta=\left\{\mathscr{P}_{D}, \mathscr{P}_{R},\left\{\mathscr{O}_{X}\right\}_{X \in \mathscr{P}},\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\}, \rightarrow\right\}$.
We will explain the meaning of $\Delta$ by reducing it to an equivalent canonical decision problem $\Delta_{C}=$ $\{\{D\},\{R\},\left\{\mathscr{O}_{D}, \mathscr{O}_{R}\right\},\{\pi\},\{\rho\}, \rightarrow\}$. To define $\Delta_{C}$, we need to define $\mathscr{O}_{D}, \mathscr{O}_{D}, \pi$, and $\rho$. Define $\mathscr{O}_{D}$ such that for each distinct strategy $\sigma$ of $\Delta$, there is a corresponding act $\mathbf{d}_{\sigma}$ in $\mathscr{O}_{D}$. Define $\mathscr{O}_{R}$ such that for each distinct configuration $\mathbf{y}$ of $\mathscr{P}_{R}$ in $\Delta$, there is a corresponding configuration $\mathbf{r}_{\mathbf{y}}$ in $\mathscr{O}_{R}$.

Before we define payoff valuation $\pi$ for $\{D, R\}$, we need some notation. Consider the joint payoff valuation $\pi_{1} \otimes \ldots \otimes \pi_{m}$ in $\Delta$. By (2), the domain of this valuation includes all of $\mathscr{O}_{D}$. Typically, the domain of this valuation will also include some (or all) random variables. Let $p$ denote the subset of random variables included in the domain of the joint payoff valuation, i.e., $p \subseteq \mathscr{P}_{R}$ such that $\pi_{1} \otimes \ldots \otimes \pi_{m}$ is a payoff valuation for $\mathscr{O}_{D} \cup p$. Define payoff valuation $\pi$ for $\{D, R\}$ such that
$\pi\left(\mathbf{d}_{\sigma}, \mathbf{r}_{\mathbf{y}}\right)=\left(\pi_{1} \otimes \ldots \otimes \pi_{m}\right)\left(\mathbf{a}_{\sigma, \mathbf{y}}, \mathbf{y}^{\mid \rho}\right)$
for all strategy $\sigma$ of $\Delta$, and for all configurations $\mathbf{y} \in$ $\mathscr{O}_{\mathscr{P}_{R}}$. Remember that $\mathbf{a}_{\sigma, \mathbf{y}}$ is the unique configuration of $\mathscr{P}_{D}$ determined by $\sigma$ and $\mathbf{y}$.

Consider the joint potential $\rho_{1} \otimes \ldots \otimes \rho_{n}$. By (3), this potential includes all random variables in its domain. Let $q$ denote the subset of decision variables included in the domain of the joint potential, i.e., $q \subseteq \mathscr{P}_{D}$ such that $\rho_{1} \otimes \ldots \otimes \rho_{n}$ is a potential for $q \cup \mathscr{P}_{R}$. Note that $q$ could be empty. Define potential $\rho$ for $\{D, R\}$ such that
$\rho\left(\mathbf{d}_{\sigma}, \mathbf{r}_{\mathbf{y}}\right)=\left(\rho_{1} \otimes \ldots \otimes \rho_{n}\right)\left(\mathbf{a}_{\sigma, \mathbf{y}}^{\mid \rho}, \mathbf{y}\right)$
for all strategy $\sigma$, and for all configurations $\mathbf{y} \in \mathscr{O}_{\mathscr{P}_{R}}$; $\Delta_{C}$, as defined above in (13) and (14), is a canonical decision problem only if $\rho$, defined in (14), is a conditional potential satisfying condition (1). This motivates the following definition: $\Delta$ is a well defined VBS representation of a decision problem if and only if
$\sum\left\{\left(\rho_{1} \otimes \ldots \otimes \rho_{n}\right)(\mathbf{x}, \mathbf{y}) \mid \mathbf{y} \in \mathscr{O}_{\mathscr{P}_{R}}\right\}=1$
for every $\mathbf{x} \in \mathscr{O}_{\sigma}$, or equivalently, if and only if $\left(\rho_{1} \otimes \ldots \otimes \rho_{n}\right)^{\mid \rho}$ is the vacuous potential for $q$. We are assuming, of course, that (1) for conditional potentials, (2) for the payoff hypergraph $\mathscr{P}_{D}$, (3) for the potential hypergraph $\mathscr{P}_{R}$, and the four conditions for the precedence relation $\rightarrow$, are true.

In summary, a VBS representation $\Delta$ of a decision problem is well defined if: 1) for conditional potentials, 2) for the payoff hypergraph, 3) for the potential hypergraph, the four conditions for the precedence relation, and (15) for the potentials, are all satisfied. Furthermore, in a well defined VBS representation $\Delta$ of a decision problem, the payoff valuations $\left\{\pi_{1}, \ldots, \pi_{m}\right\}$ represent the factors of a joint payoff function $\pi$, and the potentials $\left\{\rho_{1}, \ldots, \rho_{n}\right\}$ represent the factors of a family of probability distributions $\rho$.

It is easy to verify that the VBS representation of the oil wildcatter's problem described in Section 2 is well defined. Note that the domain of the joint potential $\rho \otimes \mu$ (shown in Table V) is $\{T, R, O\}$. Since $T$ is the only decision variable in this set, because $T$ has no predecessors, and the frame for $T$ has two configurations, there are exactly two distinct strategy components $\xi_{T}$. Thus, $\rho \otimes \mu$ represents a family of two distinct joint distributions for $\{R, O\}$, one conditioned on the decision to perform a seismic test $\left(\xi_{T}(\boldsymbol{\theta})=t\right)$ and another conditioned on the decision to not perform a seismic test $\left(\xi_{T}(\boldsymbol{\theta})=\sim t\right)$.

### 4.2. The Decision Problem

Suppose that
$\Delta=\left\{\mathscr{P}_{D}, \mathscr{P}_{R},\left\{\mathscr{O}_{X}\right\}_{X \in \mathscr{P}},\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\}, \rightarrow\right\}$
is a well defined decision problem. Let $\Delta_{C}=\{\{D\}$, $\{R\},\left\{\mathscr{O}_{D}, \mathscr{O}_{R}\right\},\{\pi\},\{\rho\}, \rightarrow\}$ represent an equivalent

canonical decision problem. In the canonical decision problem $\Delta_{C}$, the two computations that are of interest are the computation of the maximum expected value $(\pi \otimes \rho)^{1 / 0}(\bullet)$, and the computation of an optimal act $\mathbf{d}_{\sigma^{*}}$ such that $(\pi \otimes \rho)^{1 / 0}\left(\mathbf{d}_{\sigma^{*}}\right)=$ $(\pi \otimes \rho)^{1 / 0}(\bullet)$. Since we know the mapping between $\Delta$ and $\Delta_{C}$, we can now formally define the questions posed in a decision problem $\Delta$. There are two computations of interest.

First, we would like to compute the maximum expected value of the payoffs. The maximum expected payoff is given by $\left(\otimes\left(\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{1 / 0}(\boldsymbol{)})$.

Second, we would like to compute an optimal strategy $\sigma^{*}$ that gives the maximum expected value $\left(\otimes\left(\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n} \mid\right)^{1 / 0}(\boldsymbol{)}\right)$. A strategy $\sigma^{*}$ of $\Delta$ is optimal if
$(\pi \otimes \rho)^{1 / 0}\left(\mathbf{d}_{\sigma^{*}}\right)=\left(\otimes\left(\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{1 / 0}(\boldsymbol{)})$,
where $\pi, \rho$, and $D$ refer to the equivalent canonical decision problem $\Delta_{C}$.

The computation of an optimal strategy in the oil wildcatter's problem is shown in Table VII. The maximum expected value is $\$ 22,500$. An optimal strategy can be constructed from the information in $\Psi_{T}$ and $\Psi_{D}$ as follows. From $\Psi_{T}$, it can be seen that the oil wildcatter should do the seismic test $(t)$. From $\Psi_{D}$, it can be seen that if the test result is $n s$, then the optimal decision is not to drill $(\sim d)$. However, if the test result is either $o s$ or $c s$, then the optimal decision is to drill $(d)$. Note that the solution of VBS involves no divisions. Thus, the computation of the conditional distribution of $O$ given $R$ (during the preprocessing of probabilities) in the decision tree methodology is unnecessary.

## 5. A FUSION ALGORITHM FOR SOLVING VBS USING LOCAL COMPUTATION

In this section, we describe a method for solving VBS using local computation. The solution for the oil wildcatter's problem shown in Tables V, VI, and VII involves combination on the space $\mathscr{E}_{\mathscr{E}}$. While this is possible for small problems, it is computationally not feasible for problems with many variables. Given the structure of the oil wildcatter's problem, it is not possible to avoid the combination operation on the space of all four variables, $T, R, D$, and $O$. However, in some problems, it may be possible to avoid such global computations.

The basic idea of the method is to successively delete all variables from the VBS. The sequence in which variables are deleted must respect the precedence con-
straints in the sense that if $X>Y$, then $Y$ must be deleted from $X$. Since $>$ is only a partial order, a problem may allow several deletion sequences. Any allowable deletion sequence may be used. All allowable deletion sequences lead to the same answers. However, different deletion sequences may involve different computational costs. We will comment on good deletion sequences at the end of this section.

When we delete a variable, we have to do a "fusion" operation on valuations that bear on the variable. Before we describe the fusion operation, we need to define a division operation for potentials.

Division. Suppose that $\alpha$ is a potential for $g$, and $h \subseteq$ $g$. Then we define $\alpha / \alpha^{\mathrm{i} h}$, called $\alpha$ divided by $\alpha^{\mathrm{i} h}$, to be a potential for $g$ defined as
$\left(\alpha / \alpha^{\mathrm{i} h}\right)(\mathbf{r})=\alpha(\mathbf{r}) / \alpha^{\mathrm{i} h}\left(\mathbf{r}^{\mathrm{i} h}\right)$
for all $\mathbf{r} \in \mathscr{E}_{g}$. If $\alpha(\mathbf{r})=\alpha^{\mathrm{i} h}\left(\mathbf{r}^{\mathrm{i} h}\right)=0$, then we consider $\left(\alpha / \alpha^{\mathrm{i} h}\right)(\mathbf{r})=0$. In all other respects, the right-hand side of (16) should be interpreted as the usual division of two real numbers. Since $\alpha^{\mathrm{i} h}\left(\mathbf{r}^{\mathrm{i} h}\right) \geqslant \alpha(\mathbf{r})$ for all $\mathbf{r} \in \mathscr{E}_{g}$, $\alpha / \alpha^{\mathrm{i} h}$ is a well defined potential. If $\alpha$ is a potential for $g$ such that $\alpha^{\mathrm{i} h}$ is a vacuous potential for $h$, then $\alpha / \alpha^{\mathrm{i} h}=\alpha$. For example, if $\alpha$ is a conditional potential for $R$ given $g-|R|$, then it follows from the definition of a conditional potential that $\alpha^{\mathrm{i}(g-|R|)}$ is a vacuous potential. Thus, if $\alpha$ is a conditional potential for $R$ given $g-|R|$, then $\alpha / \alpha^{\mathrm{i}(g-|R|)}=\alpha$.

Fusion. The fusion operation depends on the type of variable being eliminated and the nature of valuations that bear on the variable. Consider a set of valuations consisting of $j$ payoff valuations $\pi_{1}, \ldots, \pi_{j}$ and $k$ potentials $\rho_{1}, \ldots, \rho_{k}$. Suppose that $\pi_{i}$ is a payoff valuation of $h_{i}$, and $\rho_{i}$ is a potential for $g_{i}$. Let $\operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ denote the collection of valuations after fusing the valuations in the set $\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ with respect to variable $X$.

Case 1. Suppose that $D$ is a decision variable, and none of the potentials bear on $D$. Then $\operatorname{Fus}_{D}\left\{\pi_{1}, \ldots\right.$, $\left.\pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ is a collection of valuations defined as

$$
\begin{aligned}
& \operatorname{Fus}_{D}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\} \\
& \quad=\left\{\pi^{\mathrm{i}(h-|D|}\right\} \cup\left\{\pi_{i} \mid D \notin h_{i}\right\} \cup\left\{\rho_{1}, \ldots, \rho_{k}\right\}
\end{aligned}
$$

where $\pi=\otimes\left\{\pi_{i} \mid D \in h_{i}\right\}$, and $h=\cup\left\{h_{i} \mid D \in h_{i}\right\}$.
In this case, after fusion, the set of valuations is changed as follows. All payoff valuations that bear on $D$ are combined, and the resulting payoff valuation is marginalized such that $D$ is eliminated from its domain. The payoff valuations that do not bear on $D$, and all potentials, remain unchanged.

Case 2. Suppose that $R$ is a random variable, and none of the $j$ payoff valuations bear on $R$. In this case, $\operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ is defined as

$$
\begin{aligned}
& \operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\} \\
& \quad=\left\{\pi_{1}, \ldots, \pi_{j}\right\} \cup\left\{\rho_{i} \mid R \notin g_{i}\right\} \cup\left\{\rho^{\lfloor(g-\{R]\rangle}\right\}
\end{aligned}
$$

where $\rho=\otimes\left\{\rho_{i} \mid R \in g_{i}\right\}$, and $g=\cup\left\{g_{i} \mid R \in g_{i}\right\}$.
In this case, after fusion, the set of valuations is changed as follows. The payoff valuations remain unchanged (since they do not bear on $R$ ). The potentials that do not bear on $R$ remain unchanged. The potentials that bear on $R$ are combined and the resulting potential is marginalized such that $R$ is eliminated from its domain.

Case 3. Suppose that $R$ is a random variable, and all $j$ payoff valuations bear on $R$. In this case, $\operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ is defined as

$$
\begin{aligned}
& \operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\} \\
& \quad=\left\{(\pi \otimes \rho)^{\left\lfloor(h \cup g)-\{R\}\right\rangle}\right\} \cup\left\{\rho_{i} \mid R \notin g_{i}\right\}
\end{aligned}
$$

where

$$
\begin{aligned}
\pi & =\otimes\left\{\pi_{i} \mid R \in h_{i}\right\}=\otimes\left\{\pi_{1}, \ldots, \pi_{j}\right\} \\
\rho & =\otimes\left\{\rho_{i} \mid R \in g_{i}\right\}, h=\cup\left\{h_{i} \mid R \in h_{i}\right\}
\end{aligned}
$$

and

$$
g=\cup\left\{g_{i} \mid R \in g_{i}\right\}
$$

In this case, after fusion, the set of valuations is changed as follows. All payoff valuations and those potentials that depend on $R$ are combined, and the resulting payoff valuation is marginalized such that $R$ is eliminated from its domain. The potentials that do not bear on $R$ remain unchanged.

Case 4. Suppose that $R$ is a random variable, there is a payoff valuation that bears on $R$, and there is a payoff valuation that does not bear on $R$. In this case, $\operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\}$ is defined as

$$
\begin{aligned}
& \operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\} \\
& \quad=\left\{\pi_{i} \mid R \notin h_{i}\right\} \cup\left\{\left[\pi \otimes\left(\rho / \rho^{\left\lfloor(g-\{R\}\right\rangle}\right)\right]^{\left\lfloor(h \cup g)-\{R\}\right\rangle}\right\} \\
& \cup\left\{\rho_{i} \mid R \notin g_{i}\right\} \cup\left\{\rho^{\left\lfloor(g-\{R\}\right\rangle}\right\},
\end{aligned}
$$

where

$$
\begin{aligned}
\pi & =\otimes\left\{\pi_{i} \mid R \in h_{i}\right\}, \rho=\otimes\left\{\rho_{i} \mid R \in g_{i}\right\} \\
h & =\cup\left\{h_{i} \mid R \in h_{i}\right\}
\end{aligned}
$$

and
$g \cup\left\{g_{i} \mid R \in g_{i}\right\}$.

In this case, after fusion, the set of valuations is changed as follows. The payoff valuations that do not bear on $R$, and the potentials that do not bear on $R$, remain unchanged. A new potential, $\rho^{\left\lfloor(g-\{R\}\right\rangle}$, is created. Finally, we combine all potentials that bear on $R$, divide the resulting potential by the new potential that was created, combine the resulting potential with the payoff valuations that bear on $R$, and marginalize the resulting payoff valuation such that $R$ is eliminated from its domain.

In Markov decision processes, it is often the case that the new potential created in Case 4 is vacuous. If $\rho^{\left\lfloor(g-\{R\}\right\rangle}$ is a vacuous potential for $g-\{R\}$, then (20) can be simplified as

$$
\begin{aligned}
& \operatorname{Fus}_{R}\left\{\pi_{1}, \ldots, \pi_{j}, \rho_{1}, \ldots, \rho_{k}\right\} \\
& \quad=\left\{\pi_{i} \mid R \notin h_{i}\right\} \cup\left\{(\pi \otimes \rho)^{\left\lfloor(h \cup g)-\{R\}\right\rangle}\right\} \\
& \quad \cup\left\{\rho_{i} \mid R \notin g_{i}\right\}
\end{aligned}
$$

where

$$
\begin{aligned}
\pi & =\otimes\left\{\pi_{i} \mid R \in h_{i}\right\}, \rho=\otimes\left\{\rho_{i} \mid R \in g_{i}\right\} \\
h & =\cup\left\{h_{i} \mid R \in h_{i}\right\}
\end{aligned}
$$

and
$g=\cup\left\{g_{i} \mid R \in g_{i}\right\}$.
We are now ready to state the main theorem.
Theorem 1. Suppose that

$$
\begin{aligned}
\Delta= & \left\{\mathscr{L}_{D}, \mathscr{L}_{R},\left\{\mathscr{L}_{X}\right\}_{X \in \mathscr{L}}\right. \\
& \left.\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\}, \rightarrow\right\}
\end{aligned}
$$

is a well defined decision problem. Suppose that $X_{1} X_{2} \ldots X_{k}$ is a sequence of variables in $\mathscr{L}=$ $\mathscr{L}_{D} \cup \mathscr{L}_{R}$ such that with respect to the partial order $>$, $X_{1}$ is a minimal element of $\mathscr{L}, X_{2}$ is a minimal element of $\mathscr{L}-\left\{X_{1}\right\}$, etc. Then $\left\{\left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}\right.\right.\right.$, $\left.\left.\rho_{1}, \ldots, \rho_{n}\right\}\right\}^{\left\lfloor 20\right\rfloor}=\operatorname{Fus}_{X_{2}}\left\{\ldots \operatorname{Fus}_{X_{2}}\left\{\operatorname{Fus}_{X_{1}}\left\{\pi_{1}, \ldots, \pi_{m}\right.\right.\right.$, $\left.\left.\rho_{1}, \ldots, \rho_{n}\right\}\right\}\right\}$.

Let us illustrate the statement of Theorem 1 for the oil wildcatter's problem. In this problem, we have payoff valuation $\kappa$ for $\{T\}$, payoff valuation $\pi$ for $\{D, O\}$, potential $\rho$ for $\{O\}$, and potential $\mu$ for $\{T, R, O\}$. Also, as per the precedence constraints, $T>R>D>O$. First, it is easy to see that after fusing with respect to $O$ (using (20)), the set of valuations is
$\left\{\kappa,\left(\pi \otimes\left((\rho \otimes \mu) /(\rho \otimes \mu)^{\left\lfloor(T, R]\right\rangle}\right)\right)^{\left\lfloor[T, R, D]\right.},(\rho \otimes \mu)^{\left\lfloor[T, R]\right\rangle}\right\}$.
Second, after fusing with respect to $D$ (using (17)), the set of valuations is
$\left\{\kappa,\left(\pi \otimes\left((\rho \otimes \mu) /(\rho \otimes \mu)^{\left\lfloor(T, R]\right\rangle}\right)\right)^{\left\lfloor[T, R]\right.},(\rho \otimes \mu)^{\left\lfloor[T, R]\right\rangle}\right\}$.

Third, after fusing with respect to $R$ (using (21)) since $(\rho \otimes \mu)^{\downarrow[T]}$ is a vacuous valuation), the set of valuations is
$\left\{\kappa,\left((\pi \otimes((\rho \otimes \mu) /(\rho \otimes \mu)^{\downarrow[T, R]})\right)^{\downarrow[T, R} \otimes(\rho \otimes \mu)^{\downarrow[T, R]}\right)^{\downarrow[T]}\right\}$.
Note that the second payoff valuation
$\left((\pi \otimes((\rho \otimes \mu) /(\rho \otimes \mu)^{\downarrow[T, R]})\right)^{\downarrow[T, R]} \otimes(\rho \otimes \mu)^{\downarrow[T, R]}\right)^{\downarrow[T]}$
simplifies to
$\left((\pi \otimes(\rho \otimes \mu))^{\downarrow[T, R]}\right)^{\downarrow[T]}=(\pi \otimes \rho \otimes \mu)^{\downarrow[T]}$.
Finally, after fusing with respect to $T$ (using (17)), the set of valuation reduces to the singleton set
$\left\{(\kappa \otimes(\pi \otimes \rho \otimes \mu)^{\downarrow[T]}\right)^{\downarrow \varnothing}\{ }$.
As per Theorem 1,
$((\kappa \otimes \pi) \otimes \rho \otimes \mu)^{\downarrow \varnothing}=(\kappa \otimes(\pi \otimes \rho \otimes \mu)^{\downarrow[T]})^{\downarrow \varnothing}$.
In the oil wildcatter's example, notice that the division in the first fusion operation is neutralized by the multiplication in the third fusion operation. A natural question that arises is: Can the division in (20) always be avoided? One way to avoid the division in (20) is to avoid circumstances where (20) applies. One way to avoid the circumstance where (20) applies is to make sure we have only one payoff valuation. If there is only one payoff valuation in the valuationbased system, then whenever we fuse valuations with respect to a random variable, either Case 2 or 3 will apply, never Case 4. If we have more than one payoff valuation, then we can always combine these to get one valuation before we start the fusion algorithm. Of course, this means that we will be unable to take advantage of a factorization of the joint utility function. In the oil wildcatter's problem, if we combine $\kappa$ and $\pi$ before we start the fusion algorithm, then the computations in the fusion algorithm are exactly the same as the computations in solving the problem globally (as was done in Section 4).

Another way to avoid divisions is to have a factorization of the joint probability distributions such that the added potential is always vacuous. (In this case, we can always use (21) instead of (20) and avoid divisions.) The added potential is always vacuous if we have only a conditional potential for each random variable such that the variables on which the probabilities are conditioned always precede the random variable. This typically happens in Markov decision problems. An example of such a problem follows.

### 5.1. A Finite Markov Decision Problem

Consider a valuation-based system as shown in Figure 5. There are three random variables, $R_{1}, R_{2}$,
![img-4.jpeg](img-4.jpeg)

Figure 5. A finite Markov decision problem.
and $R_{3}$, and two decision variables, $D_{1}$, and $D_{2}$. The information constraints are as follows. The decision maker first chooses an act from $\mathscr{H}_{D_{i}}$, then from $\mathscr{H}_{D_{2}}$. When the decision maker has to choose an act from frame $\mathscr{H}_{D_{i}}$, she knows only the true value of all random variables in the set $\left\{R_{j} \mid j \leqslant i\right\}$. The probability distribution of $R_{i}$ only depends on $R_{j-1}$ and $D_{j-1}$. Thus, we are given a conditional potential $\rho_{1}$ for $R_{1}$ given $\varnothing$ representing the prior probability of $R_{1}$, a conditional potential $\rho_{2}$ for $R_{2}$ given $\left\{R_{1}, D_{1}\right\}$, and a conditional potential $\rho_{3}$ for $R_{3}$ given $\left\{R_{2}, D_{2}\right\}$. Finally, the joint payoff function factorizes additively into three factors $\pi_{1}$ for $\left\{R_{1}, D_{1}\right\}, \pi_{2}$ for $\left\{R_{2}, D_{2}\right\}$, and $\pi_{3}$ for $\left\{R_{3}\right\}$.

Figure 6 shows the solution of the Markov decision problem using the fusion algorithm. The first valuation network in the figure shows the result after deletion of random varible $R_{3}$ and the resulting fusion. Note that since $\rho_{3}$ is a conditional potential for $R_{3}$ given $R_{2}$ and $D_{2}$, by definition of a conditional potential, $\rho^{\left\llbracket R_{2}, D_{2}\right\}}$ is a vacuous potential. Therefore, (21) applies. The second valuation network shows the result after deletion of decision node $D_{2}$ and the resulting fusion using (17). Step 3 is similar to Step 1, and Step 4 is similar to Step 2. Finally, Step 5 is similar to Step 1. Note that the fusion method for solving this problem involves no divisions.

In general, if we wish to take advantage of an additive factorization of the joint payoff valuation, and if we have arbitrary potentials, then divisions may be inescapable. The following example demonstrates this.

Consider a valuation-based system as shown in Figure 7 with two random variables, $R_{1}$ and $R_{2}$, and one decision variable $D$. We are given one potential $\rho$ for $\left\{R_{1}, R_{2}\right\}$ representing the joint probability distribution for $\left\{R_{1}, R_{2}\right\}$. The joint payoff valuation factors additively into two payoff valuations, $\pi_{1}$ for $\left\{R_{1}\right\}$, and $\pi_{2}$ for $\left\{D, R_{2}\right\}$. The precedence constraints are: $R_{1} \rightarrow$ $D \rightarrow R_{2}$. Figure 7 shows the details of the valuations and the valuation network representation. A global solution of this problem involves computing
$\left(\left(\left(\left(\pi_{1} \otimes \pi_{2}\right) \otimes \rho\right)^{\downarrow\left[R_{1}, D\right]}\right)^{\downarrow\left[R_{1}\right]}\right)^{\downarrow \varnothing}$

![img-5.jpeg](img-5.jpeg)

Figure 6. The fusion algorithm for the VBS in Figure 5.
which, of course, involves no divisions. If we, however, apply the fusion algorithm to the set of valuations $\left\{\pi_{1}, \pi_{2}, \rho\right\}$, then after deletion of all three variables, the valuation in the resulting singleton set is
$\left(\left[\pi_{1} \otimes\left[\pi_{2} \otimes\left(\rho / \rho^{\left.\left.\right|^{R_{1}}\right]}\right]\right]^{\left.\left.\right|^{R_{1}}\right] \otimes \rho^{\left.\left.\right|^{R_{1}}\right]}\right)^{\left.\right|^{2}}\right)$.
Note that since combination is not associative, the division in this computation is unavoidable, i.e.,

$$
\begin{aligned}
& \left(\left[\pi_{1} \otimes\left[\pi_{2} \otimes\left(\rho / \rho^{\left.\left.\right|^{R_{1}}\right]}\right]\right]^{\left.\left.\right|^{R_{1}}\right] \otimes \rho^{\left.\left.\right|^{R_{1}}\right]}\right)^{\left.\right|^{2}}\right) \\
& \quad \neq\left(\pi_{1} \otimes\left[\pi_{2} \otimes \rho\right]^{\left.\left.\right|^{R_{1}}\right]}\right)^{\left.\right|^{2}}
\end{aligned}
$$

The fusion operations in (17), (18), (19), and (21), say with respect to $X$, can simply be redescribed as
$\operatorname{Fus}_{X}\left\{\alpha_{1}, \ldots, \alpha_{h}\right\}=\left\{\alpha^{\left.\right\|^{(h-1 X)}}\right\} \cup\left\{\alpha_{i} \mid X \notin h_{i}\right\}$,
where $\alpha=\otimes\left\{\alpha_{i} \mid X \in h_{i}\right\}$ and $h=\cup\left\{h_{i} \mid X \in h_{i}\right\}$. In words, after fusion the set of valuations is changed as follows. All valuations that bear on $X$ are combined, and the resulting valuation is marginalized such that
$X$ is eliminated from its domain. The valuations that do not bear on $X$ remain unchanged.

The fusion operation in (20) is the only one that involves division and is designed especially to take care of the nonassociativity of the combination operation (see the proof of Theorem 1 in Section 8). One implication is that if the combination is associative, then the fusion operation can be simplified as in (22) and no divisions are necessary (see Shenoy 1990b for a proof of this assertion). The combination operation is associative if, for example, the utility function in a decision problem factorizes multiplicatively. In this case, for computational purposes, it is not necessary to distinguish between payoff valuations and potentials.

### 5.2. Deletion Sequences

Since $>$ is only a partial order, in general, we may have many sequences of variables that satisfy the condition stated in Theorem 1. (We call such sequences deletion sequences.) If so, which deletion sequence should one use? First, note that all deletion sequences lead to the same final result. This is implied in the statement of the theorem. Second, different deletion sequences may involve different computational efforts. For example, consider the VBS shown in Figure 8. In this example, deletion sequence $R_{2} R_{1} D$ involves less computational effort than $R_{1} R_{2} D$ as the former involves combinations on the frame of only two variables, whereas the latter involves combinations on the frame of all three variables. Finding an optimal deletion sequence is a secondary optimization problem that has been shown to be NP-complete (Arnborg, Corneil and Proskurowski 1987). However, there are several heuristics for finding good deletion sequences (Kong 1986, Mellouli 1987, Zhang 1988).
![img-6.jpeg](img-6.jpeg)

Figure 7. A decision problem requiring divisions in the fusion algorithm.

![img-7.jpeg](img-7.jpeg)

Figure 8. A VBS with two deletion sequences, $\mathrm{R}_{2} \mathrm{R}_{1} \mathrm{D}$ and $\mathrm{R}_{1} \mathrm{R}_{2} \mathrm{D}$.

One such heuristic is called one-step-look-ahead (Kong). This heuristic tells us which variable to delete next from among those that qualify. As per this heuristic, the variable that should be deleted next is one that leads to combination over the smallest frame. For example, in the VBS of Figure 8, two variables qualify for the first deletion, $R_{1}$ and $R_{2}$. This heuristic would pick $R_{2}$ over $R_{1}$ because deletion of $R_{1}$ involves combination over the frame of $\left\{D, R_{1}, R_{2}\right\}$, whereas deletion of $R_{2}$ only involves combination over the frame of $\left\{R_{1}, R_{2}\right\}$. Thus, this heuristic would choose deletion sequence $R_{2} R_{1} D$.

Consider the VBS in Figure 9. This VBS is essentially the same as the VBS of Figure 8 except that the precedence constraint $R_{2} \rightarrow R_{1}$ has been added (say $R_{1}$ is only observed after $R_{2}$ is observed). In this VBS, the partial order $>$ only allows deletion sequence $R_{1} R_{2} D$. It is clear from Lemma 2, however, that we would get the same answer if we had dropped the constraint $R_{2}>R_{1}$ from the partial order $>$. One advantage of dropping this constraint is that we can solve the problem more efficiently. Let $>^{\prime}$ denote the order obtained from $>$ by dropping pairs of the type $R_{i}>R_{j}$ and by dropping pairs of the type $D_{i}>D_{j}$, where $R_{i}, R_{j}$ are random variables and $D_{i}, D_{j}$ are decision variables. From Lemmas 1 and 2, it is clear that we can substitute $>$ ' for $>$ in the statement of Theorem 1 and the theorem remains valid.
![img-8.jpeg](img-8.jpeg)

Figure 9. The solution of this VBS can be found more efficiently by dropping the pair $\mathrm{R}_{2}>\mathrm{R}_{1}$ from the partial order $>$.

## 6. COMPARISON WITH INFLUENCE DIAGRAMS

In this section, we briefly compare our VBS representation and solution of decision problems with the influence diagram representation and solution. We assume that the reader is familiar with the influence diagram representation and solution methodology (Olmsted 1983, Howard and Matheson 1984, Shachter 1986, Tatman 1986, Ezawa 1986, Howard 1990, Tatman and Shachter 1990).

An influence diagram representation of a decision problem consists of decision nodes, random variable nodes, subvalue nodes, supervalue nodes, directed edges, a conditional potential for each random variable node, and a payoff valuation for each subvalue node. Figure 10 shows an influence diagram representation of the oil wildcatter's problem.

In influence diagrams, decision variables are shown as rectangular nodes, random variables are shown as circular nodes, and payoff valuations are shown as diamond-shaped nodes.

In influence diagrams, potentials are not depicted explicitly. It is implicit that each random variable node has a conditional potential given its direct predecessors. (Node $X$ is a direct precedessor of node $Y$ if there is a directed edge $(X, Y)$ in the diagram.) For example, the influence diagram for the oil wildcatter's problem shown in Figure 10 assumes a conditional potential for $O$ given $\varnothing$, and a conditional potential for $R$ given $\{T, O\}$. One advantage of this representation is that all conditional independences among random variables can easily be read from an influence diagram (Pearl, Geiger and Verma 1990). VBSs, on the other hand, emphasize factorizations of the joint probability distributions. Although factorizations have not been as well studied as conditional independences, the two are equivalent. For example, it is well known from probability theory that random variables $X$ and $Y$ are independent with respect to joint probability $P$ if and only if $P=Q \otimes R$, where $Q$ is a potential for $\{X\}$, and $R$ is a potential for $\{Y\}$ (e.g., see Pearl, p. 83).

Payoff valuations are shown explicitly in influence diagrams as subvalue nodes. The directed edges that point to subvalue nodes indicate the domain of the payoff valuations. The direction of these edges have no special significance. In the influence diagram for the oil wildcatter's problem, there are two subvalue nodes corresponding to payoff valuations $\pi$ for $\{D, O\}$ and $\kappa$ for $\{T\}$. In the influence diagram representation of the oil wildcatter's problem, there is a third value node $\tau$ connected to $\pi$ and $\kappa ; \tau$ represents the combination $\pi \otimes \kappa$ and is called a supervalue node. In

![img-9.jpeg](img-9.jpeg)

Figure 10. An influence diagram representation of the oil wildcatter's problem.
valuation networks, combination is implicit and is not shown explicitly.

In influence diagrams, information constraints are encoded in the form of directed edges pointing to decision nodes. The semantics of these directed edges are as follows. For any decision node $D$ and any random variable node $R$, the true value of $R$ is known to the decision maker at the point in time when they have to choose an act from the frame $D$ if and only if there is a directed edge in the diagram from $R$ to $D$. In the influence diagram representation of the oil wildcatter's problem, there are no directed edges pointing to $T$. This implies that nothing is known when the decision whether to perform a seismic test or not is made. Also, there are two directed edges $(T, D)$ and $(R, D)$. This means that at the point in time when the decision whether to drill or not has to be made, the oil wildcatter's knows the decision regarding performance of the seismic test and also knows the test results, but not the amount of oil. The oil wildcatter does not know the amount of oil (at the time the decision to drill is made) because there is no directed edge $(O, D)$ in the diagram.

Given an influence diagram representation, the translation to a VBS representation is clear. This means that the fusion algorithm described in Section 5 can be applied also to influence diagrams. On the other hand, if we have a well defined VBS representation such that all potentials are conditional potentials, then the translation to an influence diagram representation is also clear. However, if we have a VBS representation with potentials that are not conditional potentials, then there is no direct equivalent influence diagram representation. (By direct, we mean without any preprocessing.) For example, Figure 11 shows a valuation-based system with two random variables and one decision variable. The potential $\rho$ for $\left\{R_{1}, R_{2}\right\}$ is the joint probability distribution of
$R_{1}$ and $R_{2}$. The joint utility function factors multiplicatively into two factors, $\pi_{1}$ for $\left\{D, R_{1}\right\}$ and $\pi_{2}$ for $\left\{R_{1}, R_{2}\right\}$. There is no direct influence diagram representation of this problem. An influence diagram representation of this problem involves, for example, the computation of the marginal of $R_{1}, \rho^{\left\lfloor R_{1}\right.}$, and the computation of the conditional of $R_{2}$ given $\left\{R_{1}\right\}, \rho / \rho^{\left\lfloor R_{2}\right.}$. Note that these computations are unnecessary for an efficient solution of the problem given by $\left(\left\lfloor\pi_{1} \otimes\left(\pi_{2} \otimes \rho\right)^{\left\lfloor R_{1}\right\rfloor^{\left\lfloor D\right.}}\right)^{\left\lfloor 0\right\rfloor}\right.$

### 6.1. Solving Influence Diagrams

Here we only compare the arc reversal method for solving influence diagrams with the fusion algorithm for solving VBSs. We refer the reader to Olmsted, (1983), Shachter (1986), Ezawa (1986), Tatman (1986), and Tatman and Shachter (1990) for details about the arc reversal method.

Assume that each random variable node has a conditional potential stored at its location, and assume that each subvalue node has a payoff valuation stored at its location. These valuations get modified in the solution process. The process of solving influence diagrams involves arc reversals and node removals. Nodes are successively removed until only one value node remains.

Removal of a random variable node involves averaging the payoff valuations that depend on the random variable node using the potential stored at the random variable node. Compared to VBSs, this operation corresponds to fusing the valuations that bear on the random variable node.

Removal of a decision node involves first combining the payoff valuations that depend on the decision node and then maximizing the resulting payoff valuation over the frame of the decision node. The resulting valuation is stored at a value node. Compared to VBSs, this operation corresponds to fusing the payoff valuations that bear on the decision node.
![img-10.jpeg](img-10.jpeg)

Figure 11. A VBS that has no direct influence diagram representation (left); an equivalent influence diagram representation after preprocessing (right).

Removal of value nodes corresponds to combining the valuations stored at the value nodes and storing the result at another value node.

As in VBSs, the sequence of removals of random variable nodes and decision nodes must respect the precedence constraints expressed by the directed edges pointing to decision nodes. Also, a random variable node can be removed only if it is not a predecessor for any other random variable nodes in the diagram. If a random variable node is a predecessor for other random variable nodes, then these arcs have to be reversed before the random variable node can be removed.

In VBSs, the fusion algorithm combines all valuations that contain the variable being marginalized. In influence diagrams, this condition is achieved by arc reversals. Arc reversals ensure that all valuations containing the node being removed are combined prior to removing the node. However, the arc reversal operation also involves unnecessary divisions and multiplications to ensure that the resulting potentials at all random variable nodes are conditional potentials. It is this aspect of the arc reversal operation that makes the influence diagram solution less computationally efficient than the solution method of VBSs.

If we disregard the unnecessary divisions and multiplications, the solution method of influence diagrams is as efficient as that of VBSs. The computational efficiency of the influence diagram solution method depends on the node removal sequence. The computational efficiency of the VBS solution method also depends on the deletion sequence. If the same sequence is used in both cases, we get approximately the same computational efficiency. In Section 5, we described the one-step-look-ahead heuristic due to Kong for picking the sequence of variables. In the case of influence diagrams, Olmsted, and Ezawa describe some heuristics for selecting the sequence of node removals.

## 7. CONCLUSIONS

The main objective of this paper is to propose a new method to represent and solve decision problems. The VBS representation and solution described here is a hybrid of valuation-based systems for probability propagation (Shenoy 1991c) and valuation-based systems for optimization (Shenoy 1991b).

There are several advantages of the VBS representation and solution of decision problems. First, like influence diagrams, a valuation network representation is compact when compared to decision trees. A valuation network graphically depicts the qualitative
structure of the decision problem and de-emphasizes the quantitative details of the problem. However, both VBSs and influence diagrams are appropriate only for symmetric decision problems. For asymmetric decision problems, decision tree representation is more flexible.

Second, like influence diagrams, the VBS representation separates the formulation of the problem from its solution.

Third, in symmetric decision problems, the solution procedure of VBSs is more efficient than that of decision trees. This assumes that the computational procedure of decision trees includes the preprocessing of probabilities. The solution procedure of decision trees includes unnecessary divisions. The unnecessary divisions take place during preprocessing of probabilities.

Fourth, the VBS representation is more powerful than influence diagram representation. Whereas influence diagram representation is only capable of directly representing conditional potentials, VBS representation is capable of directly representing arbitrary potentials.

Fifth, the solution method of VBSs involves minimal divisions. In comparison, the influence diagram solution method involves unnecessary divisions (in every arc reversal operation). These unnecessary divisions are the same as those in the decision tree solution process. In influence diagrams, these unnecessary operations are performed for semantical considerations. The influence diagram solution process has the property that the diagram resulting from the deletion of a random variable node is again an influence diagram. This means that the resulting potentials in the reduced influence diagram are conditional potentials. It is this demand for conditional potentials at each stage that results in the unnecessary divisions and multiplications.

Sixth, the semantics of VBSs are different from the semantics of influence diagrams. Whereas influence diagrams are based on the semantics of conditional independence, VBSs are based on the semantics of factorization.

Seventh, if a decision problem has no random variables, it reduces to an optimization problem. And, the solution technique of VBSs reduces to dynamic programming (Shenoy 1991b).

Eighth, in cases where a decision problem has no decision variables, we may be interested in finding marginals of the joint distribution for each random variable. In such problems, the solution technique described in this paper reduces to the technique for finding marginals (Shenoy 1991c). This technique also

can revise marginals in light of new observations. We represent each new observation by a potential and then use the fusion algorithm to compute the desired marginals.

### 7.1. Limitations of VBSs

Like influence diagrams, VBSs are appropriate only if the decision problem is symmetric or almost symmetric. In asymmetric decision problems, decision tree representation is more flexible than VBSs and influence diagrams, and decision tree solutions may be more efficient than VBSs and influence diagrams. This is because, like influence diagrams, VBSs make an asymmetric decision problem symmetric by adding dummy acts and events, and in the process enlarge the space of the problem.

In problems with many variables, like the solution procedure of influence diagrams, the fusion algorithm is tractable only if the space on which combinations are performed stay small. The space on which combinations are performed depends on the sizes of the valuations and also on the precedence constraints. We need strong independence conditions to keep the sizes of the potentials small. We also need strong assumptions on the utility function to decompose it into small payoff valuations. In the worst case, of course, solving a decision problem is NP-hard (Cooper 1987).

## 8. PROOFS

In this section we give a proof for Theorem 1. First we state and prove a lemma needed to prove Theorem 1.

Lemma 4. Suppose that

$$
\begin{aligned}
\Delta= & \left\{\mathscr{L}_{D}, \mathscr{L}_{R},\left\{\mathscr{L}_{X}\right\}_{X \in \mathscr{L}}\right. \\
& \left.\left\{\pi_{1}, \ldots, \pi_{m}\right\},\left\{\rho_{1}, \ldots, \rho_{n}\right\}, \rightarrow\right\}
\end{aligned}
$$

is a well defined decision problem. Suppose that $X$ is a minimal variable in $\mathscr{L}=\mathscr{L}_{D} \cup \mathscr{L}_{R}$ with respect to the partial order $>$, where $>$ is the transitive closure of $\rightarrow$. Then

$$
\begin{aligned}
& \left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\{\mathscr{L}-\{X\}\right\}} \\
& \quad=\otimes \operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\} .
\end{aligned}
$$

Proof. We prove this result in four mutually exclusive and exhaustive cases, each corresponding to the definition of the fusion operation in (17), (18), (19) and (20), respectively. Suppose that $\pi_{i}$ is a payoff valuation for $h_{i}$ and $\rho_{i}$ is a potential for $g_{i}$.

Case 1. Suppose that $X$ is a decision variable. In this case, there cannot be a potential in the VBS $\Delta$ that bears on $X$ because if there were one, then, since $\Delta$ is well defined, by the consistency conditions for the precedence relation $\rightarrow, X$ cannot be a minimal variable. This would contradict the hypothesis that $X$ is minimal. Without loss of generality, assume that $\pi_{1}$, $\ldots, \pi_{k}$ are the only payoff valuations that bear on $X$. Let $\pi=\pi_{1} \otimes \ldots \otimes \pi_{k}$, let $h=h_{1} \cup \ldots \cup h_{k}$, and let $\mathbf{c} \in \mathscr{H}_{\mathscr{L}-\{X\}}$. Then

$$
\begin{aligned}
& \left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\{\mathscr{L}-\{X\}\right.}(\mathbf{c}) \\
& =\operatorname{Max}\left\{\left[\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}, \mathbf{x}\right)+\ldots+\pi_{k}\left(\mathbf{c}^{\left.\right\}^{h_{k}}, \mathbf{x}\right)\right.\right. \\
& \left.\left.+\pi_{k+1}\left(\mathbf{c}^{\left.\right\}^{h_{k+1}}\right)+\ldots+\pi_{n}\left(\mathbf{c}^{\left.\right\}^{h_{n}}\right)\right]\right] \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& =\operatorname{Max}\left\{\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}, \mathbf{x}\right)+\ldots+\pi_{h}\left(\mathbf{c}^{\left.\right\}^{h_{h}}, \mathbf{x}\right)\right. \\
& \cdot \pi_{k+1}\left(\mathbf{c}^{\left.\right\}^{h_{k+1}}+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right\}\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right] \\
& =\left[\operatorname{Max}\left\{\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}, \mathbf{x}\right)+\ldots+\pi_{k}\left(\mathbf{c}^{\left.\right\}^{h_{k}}, \mathbf{x}\right)\right)\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right. \\
& +\pi_{k+1}\left(\mathbf{c}^{\left.\right\}^{h_{k+1}}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right] \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right] \\
& =\left[\pi^{\left.\right\}^{h-\{X\}}\left(\mathbf{c}^{\left.\right\}^{h}}\right)+\pi_{k+1}\left(\mathbf{c}^{\left.\right\}^{h_{k+1}}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right] \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right] \\
& =\otimes \operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}(\mathbf{c})
\end{aligned}
$$

Case 2. Suppose that $X$ is a random variable, and none of the $m$ payoff valuations bear on $X$. Without loss of generality, assume that $\rho_{1}, \ldots, \rho_{k}$ are the only potentials that bear on $X$. Let $\rho=\rho_{1} \otimes \ldots \otimes \rho_{k}$, let $g=g_{1} \cup \ldots \cup g_{k}$, and let $\mathbf{c} \in \mathscr{H}_{\mathscr{L}-\{X\}}$. Then

$$
\begin{aligned}
& \left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\{\mathscr{L}-\{X\}\right.}(\mathbf{c}) \\
& =\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right]\right. \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left.\right\}^{h_{k}}, \mathbf{x}\right) \rho_{k+1}\left(\mathbf{c}^{\left.\right\}^{h_{k+1}}\right)\right. \\
& \left.\ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& =\left[\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right]\left[\rho_{k+1}\left(\mathbf{c}^{\left.\right\}^{g_{k+1}}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right)\right] \\
& \cdot\left[\sum\left\{\left(\rho_{1}\left(\mathbf{c}^{\left.\right\}^{g_{1}}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left.\right\}^{g_{k}}, \mathbf{x}\right)\right| \mathbf{x} \in \mathscr{H}_{X}\right\}\right] \\
& =\left[\pi_{1}\left(\mathbf{c}^{\left.\right\}^{h_{1}}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left.\right\}^{h_{m}}\right)\right]\left[\rho_{k+1}\left(\mathbf{c}^{\left.\right\}^{g_{k+1}}\right)\right. \\
& \left.\ldots \rho_{n}\left(\mathbf{c}^{\left.\right\}^{g_{n}}\right) \rho^{\left.\right\}^{g-\{X\}}\left(\mathbf{c}^{\left.\right\}^{g}}\right)\right] \\
& =\otimes \operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}(\mathbf{c})
\end{aligned}
$$

Case 3. Suppose that $X$ is a random variable, and all of the $m$ payoff valuations bear on $X$. Without loss of

generality, assume that $\rho_{1}, \ldots, \rho_{k}$ are the only potentials that bear on $X$. Let $\pi=\pi_{1} \otimes \ldots \otimes \pi_{m}$, let $h=h \cup \ldots \cup h_{m}$, let $\rho=\rho_{1} \otimes \ldots \otimes \rho_{k}$, let $g=g_{1} \cup \ldots \cup g_{k}$, and let $\mathbf{c} \in \mathscr{H}_{\mathscr{L}-[X]}$. Then

$$
\begin{aligned}
& \left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\lfloor(\mathscr{L}-[X]\right)}\{\mathbf{c}\} \\
& =\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}, \mathbf{x}\right)\right]\right. \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right) \rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right)\right. \\
& \left.\ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& =\left[\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}, \mathbf{x}\right)\right]\right.\right. \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right] \\
& \cdot\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right)\right] \\
& =\left[(\pi \otimes \rho)^{\left\lfloor\left(\left\lfloor h \cup g\right)\right.\right.}-\left\lfloor X\right\rceil\left(\mathbf{c}^{\left\lfloor\left\lfloor h \cup g\right)\right.}\right)\right]\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor h_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right)\right] \\
& =\otimes \operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}(\mathbf{c})
\end{aligned}
$$

Case 4. Suppose that $X$ is a random variable, and some payoff valuations bear on $X$. Without loss of generality, assume that $\pi_{1}, \ldots, \pi_{j}$ are the only payoff valuations that bear on $X$, and $\rho_{1}, \ldots, \rho_{k}$ are the only potentials that bear on $X$. Let $\pi=$ $\pi_{1} \otimes \ldots \otimes \pi_{j}$, let $h=h_{1} \cup \ldots \cup h_{j}$, let $\rho=$ $\rho_{1} \otimes \ldots \otimes \rho_{k}$, let $g=g_{1} \cup \ldots \cup g_{k}$, and let $\mathbf{c} \in \mathscr{H}_{\mathscr{L}_{-[X]}}$. Then

$$
\begin{aligned}
& \left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\lfloor(\mathscr{L}-[X]\right)}(\mathbf{c}) \\
& =\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{j}\left(\mathbf{c}^{\left\lfloor h_{j}\right.}, \mathbf{x}\right)+\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)\right.\right. \\
& +\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right] \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right. \\
& \cdot \rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& =\left[\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{j}\left(\mathbf{c}^{\left\lfloor h_{j}\right.}, \mathbf{x}\right)+\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)\right.\right. \\
& +\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right] \\
& \cdot\left[\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right] \\
& \cdot\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right)\right] \\
& =\left[\sum\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{j}\left(\mathbf{c}^{\left\lfloor h_{j}\right.}, \mathbf{x}\right)\right.\right. \\
& +\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right] \\
& \cdot\left[\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right] \\
& \cdot\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right) \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& =\left[\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{j}\left(\mathbf{c}^{\left\lfloor h_{j}\right.}, \mathbf{x}\right)\right]\right.\right. \\
& \cdot\left[\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& \left.+\left[\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right]\right.\right.
\end{aligned}
$$

$$
\begin{aligned}
& \cdot\left[\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{g-|X|}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right] \\
& \cdot\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right) \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& =\left[\sum\left\{\left[\pi_{1}\left(\mathbf{c}^{\left\lfloor h_{1}\right.}, \mathbf{x}\right)+\ldots+\pi_{j}\left(\mathbf{c}^{\left\lfloor h_{j}\right.}, \mathbf{x}\right)\right]\right.\right. \\
& \cdot\left[\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right| \\
& +\sum\left\{\left[\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right]\right. \\
& \cdot\left[\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& \left.\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right]\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right) \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& =\left[\left[\pi \otimes\left(\rho / \rho^{\left\lfloor g-|X|\right.}\right)\right]^{\left\lfloor\left\lfloor h \cup g\right)\right.}-\left\lfloor X\right\rceil\left(\mathbf{c}^{\left\lfloor\left\lfloor h \cup g\right.}\right)\right.\right. \\
& +\left[\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right] \\
& {\left[\sum\left\{\left(\rho_{1}\left(\mathbf{c}^{\left\lfloor g_{1}\right.}, \mathbf{x}\right) \ldots \rho_{k}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}, \mathbf{x}\right)\right) / \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right]\left|\mathbf{x} \in \mathscr{H}_{X}\right|\right] \mid} \\
& \cdot\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{n}\right.}\right) \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right] \\
& =\left[\left[\pi \otimes\left(\rho / \rho^{\left\lfloor\left\lfloor g-|X|\right.}\right)\right]^{\left\lfloor\left\lfloor h \cup g\right)\right.}-\left\lfloor X\right\rceil\left(\mathbf{c}^{\left\lfloor\left\lfloor h \cup g\right.}\right)\right.}\right)+\left[\pi_{j+1}\left(\mathbf{c}^{\left\lfloor h_{j+1}\right.}\right)\right. \\
& \left.+\ldots+\pi_{m}\left(\mathbf{c}^{\left\lfloor h_{m}\right.}\right)\right]\left[\left[\rho_{k+1}\left(\mathbf{c}^{\left\lfloor g_{k+1}\right.}\right) \ldots \rho_{n}\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right) \rho^{\left\lfloor g-|X|\left(\mathbf{c}^{\left\lfloor g_{k}\right.}\right)\right.}\right]\right] \\
& =\otimes \operatorname{Fus}_{X}\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}(\mathbf{c})
\end{aligned}
$$

We have now shown the result for all four mutually exclusive and exhaustive cases. Therefore the result follows.

Proof of Theorem 1. By definition, $\left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}\right.\right.$, $\left.\left.\rho_{1}, \ldots, \pi_{n}\right\}\right\}^{\left\lfloor 2 \mid\right.}$ is obtained by sequentially marginalizing a minimal variable. A proof of this theorem is obtained by repeatedly applying the result of Lemma 4. At each step, we delete a minimal variable and fuse the set of all valuations with respect to the minimal variable. It is easy to see that after deletion and fusion, the resulting VBS is well defined. Using Lemma 4, after fusion with respect to $X_{1}$, the combination of all valuations in the resulting VBS is equal to $\left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\lfloor\left\lfloor g_{1}\right.}\left\lvert\, \rho_{1}\right\rvert\,}$. Again, using Lemma 4, after fusion with respect to $X_{2}$, the combination of all valuations in the resulting VBS is equal to $\left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\lfloor\left\lfloor g_{1}\right.}\left\lvert\, \rho_{1}\right\rvert\,}{ }^{\left\lvert\, \rho_{2}\right.}$. And so on. When all the variables have been deleted there will be a single valuation left. Using Lemma 4, this valuation will be $\left(\otimes\left\{\pi_{1}, \ldots, \pi_{m}, \rho_{1}, \ldots, \rho_{n}\right\}\right)^{\left\lfloor 2 \mid\right.}$.

## ACKNOWLEDGMENT

This work was supported in part by the National Science Foundation under grant IRI-8902444. I am grateful for comments from and conversations with Alice Agogino, Dan Geiger, Steffen Lauritzen, Pierre Ndilikilikesha, Anthony Neugebauer, Geoff Schemmel, Leen-Kiat Soh, Glenn Shafer, Philippe

Smets, Po-Lung Yu, and Lianwen Zhang. This paper has also profited from the comments of two anonymous referees, and the comments of the area editor, Peter Farquhar.
