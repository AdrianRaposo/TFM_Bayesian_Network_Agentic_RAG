# Smooth, identifiable supermodels of discrete DAG models with latent variables 

ROBIN J. EVANS ${ }^{1}$ and THOMAS S. RICHARDSON ${ }^{2}$<br>${ }^{1}$ Department of Statistics, University of Oxford, 24-29 St Giles', Oxford, OX1 3LB, UK. E-mail: evans@stats.ox.ac.uk<br>${ }^{2}$ Department of Statistics, University of Washington, Box 354322, Seattle, WA 98195, USA.<br>E-mail: thomasr@u.washington.edu

We provide a parameterization of the discrete nested Markov model, which is a supermodel that approximates DAG models (Bayesian network models) with latent variables. Such models are widely used in causal inference and machine learning. We explicitly evaluate their dimension, show that they are curved exponential families of distributions, and fit them to data. The parameterization avoids the irregularities and unidentifiability of latent variable models. The parameters used are all fully identifiable and causallyinterpretable quantities.

Keywords: Bayesian network; DAG; nested Markov model; parameterization

## 1. Introduction

Directed acyclic graph (DAG) models, also known as Bayesian networks, are a widely used class of multivariate models in probabilistic reasoning, machine learning and causal inference (Bishop [1], Darwiche [2], Pearl [15]). The inclusion of latent variables within Bayesian network models can greatly increase their flexibility, and also account for unobserved confounding; however, latent variable models are typically non-regular, their dimension can be hard to calculate, and they generally do not have fully identifiable parameterizations. In this paper, we will present an alternative approach which overcomes these difficulties, and does not require any parametric assumptions to be made about the latent variables.

Example 1.1. Suppose we are interested in the relationship between family income during childhood $X$, an individual's education level $E$, their military service $M$, and their later income $Y$. We might propose the model shown in Figure 1(a), which includes a hidden variable $U$ representing motivation or intelligence. Let the four observed variables be binary, but make no assumption about $U$.

One can check using Pearl's d-separation criterion (Pearl [15]) that $M \Perp X \mid E$ under this model, in other words there is no relationship between military service and family income after controlling for level of education; this places two independent constraints on the variables' joint distribution $p(x, e, m, y)$ (one for each level of $E)$. In addition, let $q_{E Y}(e, y \mid x, m) \equiv p(e \mid$

![img-0.jpeg](img-0.jpeg)

Figure 1. (a) A directed acyclic graph with the latent variable $U$; (b) a (conditional) acyclic directed mixed graph (the Verma graph) representing the observed distribution in (a).
$x) \cdot p(y \mid x, m, e)$; then the quantity

$$
\begin{aligned}
q_{E Y}(y \mid x, m) & \equiv \sum_{e} q_{E Y}(e, y \mid x, m) \\
& =\sum_{e} p(e \mid x) \cdot p(y \mid x, m, e)
\end{aligned}
$$

does not depend upon $x$ (Robins [18]); a short proof of this is given in Appendix A. If the graph is interpreted causally, then $q_{E Y}(y \mid x, m)=p(y \mid \operatorname{do}(x, m))$, that is, the distribution of $Y$ in an experiment that externally sets $\{X=x, M=m\}$. Note that generally $q_{E Y}(y \mid x, m) \neq p(y \mid$ $x, m)$.

The restriction that (1) does not depend on $x$ corresponds to two further independent constraints on $p$, one for each level of $m$. The set of distributions that satisfy all four constraints is the nested Markov model associated with the graph(s) in Figure 1; the number of free parameters is $15-2-2=11$.

The distributions in the model all factorize as

$$
p(x, e, m, y)=p(x) \cdot p(m \mid e) \cdot q_{E Y}(e, y \mid x, m)
$$

and each of the three factors can be parameterized separately. The model can therefore be described using the following 11 free parameters:

$$
\begin{aligned}
& p(x=0), \quad p(m=0 \mid e), \quad q_{E Y}(e=0 \mid x) \\
& q_{E Y}(y=0 \mid m), \quad q_{E Y}(e=y=0 \mid x, m)
\end{aligned}
$$

If we interpret the model causally these are, respectively, the quantities

$$
\begin{aligned}
& P(X=0), \quad P(M=0 \mid \operatorname{do}(E=e)), \quad P(E=0 \mid \operatorname{do}(X=x)) \\
& P(Y=0 \mid \operatorname{do}(M=m)), \quad P(E=0, Y=0 \mid \operatorname{do}(X=x, M=m))
\end{aligned}
$$

The map from the set of positive probability distributions that satisfy the 4 constraints to these 11 parameters is smooth and bijective, and the parameters are fully identifiable. It follows that the model is a curved exponential family of distributions, and that it can be fitted using standard numerical methods.

An alternative modelling approach would be to include a latent variable $U$ explicitly in the model, but this leads to some parameters being unidentifiable. For example, with a binary $U$ the model implied by Figure 1(a) has 12 parameters. We know that the true marginal distribution has at most dimension 11, so at least one of these 12 parameters is unidentifiable. Even though the model is not identified, this latent variable model is still 'too small', in the sense that the model over the observed margin only has dimension 10, whereas dimension 11 can be obtained if $U$ is allowed to have more than two states. As $U$ is not observed, it is undesirable to make specific assumptions about $U$ 's state-space because one may unwittingly impose restrictions on the observable distribution. Further, latent variable models are not statistically regular, so standard statistical theory for likelihood ratio tests and asymptotic normality of parameter estimates does not apply (Mond et al. [13], Drton [5]).

# 1.1. Other work and this paper's contribution 

Models of conditional independence associated with margins of DAG models (we refer to these as 'ordinary Markov models') have been studied by Richardson and Spirtes [25]; see also Wermuth [30]. These models were parameterized and shown to be smooth by Evans and Richardson [10]. Other approaches using probit models (Silva and Ghahramani [24]) and cumulative distribution networks (Huang and Frey [12], Silva et al. [23]) are more parsimonious than ordinary Markov models, but impose additional constraints due to their parametric structure.

None of the models mentioned in the previous paragraph can account for constraints of the kind in (1), which were first identified by Robins [18] and separately by Verma and Pearl [29]. Such constraints are attractive because they allow finer distinctions between different causal models from purely observational data: for example, going by conditional independence alone the graph in Figure 1(b) is Markov equivalent to the DAGs in Figure 2, and these causal models are therefore indistinguishable without using other constraints; however the DAGs do not imply the Verma constraint (1), so under the nested Markov model one can distinguish between these models.

An algorithm for finding such constraints was given by Tian and Pearl [28], and developed into a fully nonparametric statistical model (the nested Markov model) by Richardson et al. [17]. In this paper, we provide a smooth, statistically regular and fully identifiable parameterization of the discrete version of nested Markov models. As a result, discrete nested Markov models are shown to be curved exponential families of distributions of known dimension. All the parameters we derive are interpretable as straightforward causal quantities. Evans [7] shows that the discrete nested Markov model that we describe here is the best possible algebraic approximation to DAG
![img-1.jpeg](img-1.jpeg)

Figure 2. DAGs that represent the same conditional independence model as Figure 1(b), but which do not imply the Verma constraint.

models with latent variables, in the sense that the models have the same dimension over the observed variables. An earlier review paper (Shpitser et al. [20]) mentions the parameterization given here, but no proofs are provided.

The conditional independence constraints we consider here include the constraints described in Tian and Pearl [28]. They are also a special case of the dormant independences. However, not all dormant independences lead to constraints on the observed distribution - some impose restrictions (solely) on intervention distributions; see Shpitser et al. [20]. A complete algorithm for generating dormant constraints is given in Shpitser and Pearl [21].

The remainder of the paper is organized as follows. In Section 2, we introduce Conditional Acyclic Directed Mixed Graphs, the class of graphs we use to represent our models; those models are formally introduced in Section 3. Some graphical theory is given in Section 4, before the main results in Section 5. Section 6 applies the method to data from a panel study.

# 2. Conditional acyclic directed mixed graphs 

A directed acyclic graph (DAG) contains vertices representing random variables, and edges (arrows) that imply some structure on the joint probability distribution. A DAG with latent vertices can be transformed into an acyclic directed mixed graph (ADMG) over just its observed vertices via an operation called latent projection (Pearl and Verma [14]). In the simplest case this just involves replacing latent variables with bidirected edges $(\leftrightarrow)$, as illustrated by the transformation from Figure 1(a) to (b); the transformed graph represents the marginal distribution over the observed random variables $X_{V}$.

For technical reasons, we work with a slightly larger class of graphs, called conditional acyclic directed mixed graphs (CADMGs). These have two sets of vertices, fixed $(W)$ and random $(V)$, and are used to represent the structure of a set of distributions for $X_{V}$ indexed by possible values of $X_{W}$.

Definition 2.1. A conditional acyclic directed mixed graph (CADMG) $\mathcal{G}$ is a quadruple $(V, W, \mathcal{E}, \mathcal{B})$. There are two disjoint sets of vertices: random, $V$, and fixed, $W$. The directed edges $\mathcal{E} \subseteq(V \cup W) \times V$ are ordered pairs of vertices; if $(a, b) \in \mathcal{E}$ we write $a \rightarrow b$. Loops $a \rightarrow a$ and directed cycles $a \rightarrow \cdots \rightarrow a$ are not allowed (hence 'acyclic'). The bidirected edges, $\mathcal{B}$, are unordered pairs of distinct random vertices, and if $\{a, b\} \in \mathcal{B}$ we write $a \leftrightarrow b$.

For convenience, throughout this paper we will only consider CADMGs in which for every fixed vertex $w$ there is at least one edge $w \rightarrow v$. (Note that it follows from the definition of a CADMG that $v$ will be random.)

These graphical concepts are most easily understood by example: see the CADMG in Figure 3. We depict random vertices with round nodes, and fixed vertices with square nodes. CADMGs are not generally simple graphs, because it is possible to have up to two edges between each pair of vertices in $V$ (one directed and one bidirected); see Figure 6 for two examples. CADMGs are a slight generalization of ADMGs (Richardson [16]), which correspond to the special case $W=\varnothing$. Note that no arrowheads can be adjacent to any fixed vertex: so neither $a \rightarrow w$ nor $a \leftrightarrow w$ is allowed for any $w \in W$. This reflects the fact that fixed vertices cannot depend on

![img-2.jpeg](img-2.jpeg)

Figure 3. A conditional acyclic directed mixed graph $\mathcal{L}$, with random vertices $V=\{2,3,4,5\}$ and fixed vertices $W=\{1\}$.
other variables, observed or unobserved, but that random vertices may depend upon fixed ones. Mathematically, fixed nodes play a similar role to the 'parameter nodes' used by Dawid [3].

We make use of the following standard familial terminology for directed graphs.
Definition 2.2. If $a \rightarrow b$, we say that $a$ is a parent of $b$, and $b$ a child of $a$. The set of parents of $b$ is denoted $\mathrm{pa}_{\mathcal{G}}(b)$. We say that $w$ is an ancestor of $v$ if either $v=w$ or there is a sequence of directed edges $w \rightarrow \cdots \rightarrow v$. The set of ancestors of $v$ is denoted $\operatorname{an}_{\mathcal{G}}(v)$. These definitions are applied disjunctively to sets of vertices so that, for example, $\operatorname{pa}_{\mathcal{G}}(A) \equiv \bigcup_{a \in A} \operatorname{pa}_{\mathcal{G}}(a)$. An ancestral set is one that contains all its own ancestors: $\operatorname{an}_{\mathcal{G}}(A)=A$.

Note that the definitions of parents, children and ancestors do not distinguish between random and fixed vertices. A random-ancestral set, $A^{\prime} \subseteq V$, is a set of random vertices such that $\operatorname{an}_{\mathcal{G}}\left(A^{\prime}\right) \subseteq A^{\prime} \cup W$; that is, all the random ancestors of $A^{\prime}$ are contained in $A^{\prime}$ itself.

A set of vertices $B$ is said to be sterile if it does not contain any of its children: equivalently $\operatorname{pa}_{\mathcal{G}}(B) \cap B=\varnothing$. The sterile subset of a set $C \subseteq V$ is sterile ${ }_{\mathcal{G}}(C) \equiv C \backslash \operatorname{pa}_{\mathcal{G}}(C)$ (sometimes called the set of 'sink nodes' in the induced subgraph on $C$ ).

Example 2.3. Consider the CADMG $\mathcal{L}$ in Figure 3. The set of parents of the vertex 3 is $\mathrm{pa}_{\mathcal{L}}(3)=\{2\}$, and the set of ancestors is $\operatorname{an}_{\mathcal{L}}(3)=\{1,2,3\}$; hence $\{1,2,3\}$ is ancestral, and $\{2,3\}$ is random-ancestral. The set $\{2,4,5\}$ is sterile, but $\{2,3,5\}$ is not.

Definition 2.4. A set of random vertices $B \subseteq V$ is bidirected-connected if for each $a, b \in B$ there is a sequence of edges $a \leftrightarrow \cdots \leftrightarrow b$ with all intermediate vertices in $B$. A maximal bidirectedconnected set is a district of the graph $\mathcal{G}$ (sometimes called a $c$-component). The set of districts is a partition of the random vertices of a graph; the district containing $v \in V$ is denoted $\operatorname{dis}_{\mathcal{G}}(v)$.

We draw bidirected edges in red, which makes it easy to identify districts as the maximal sets connected by red edges. In Figure 1(b) for example, there are three districts: $\{X\},\{M\}$, and $\{E, Y\}$. In Figure 3, there are two: $\{3\}$ and $\{2,4,5\}$.

# 2.1. Transformations 

We now introduce two operations that transform CADMGs by removing vertices: the first separates into districts and the second one forms ancestral subgraphs. We will use these transformations to define our Markov property (and thereby our statistical model) in Section 3.

![img-3.jpeg](img-3.jpeg)

Figure 4. Four reachable subgraphs of the graph in Figure 1(b). Graphs in (a), (b) and (c) correspond to factorization into the districts $\{X\},\{E, Y\}$ and $\{M\}$ respectively. Graph (d) corresponds to marginalizing the childless node $Y$.

Definition 2.5. Let $\mathcal{G}$ be a CADMG containing a district $D$. Define $\mathfrak{d}_{D}(\mathcal{G})$ to be the CADMG with: the set of random vertices $D$; the set of fixed vertices $\mathrm{pa}_{\mathcal{G}}(D) \backslash D$; the set of bidirected edges whose endpoints are both in $D$ in $\mathcal{G}$; the set of directed edges from $\mathcal{G}$ pointing to a vertex in $D$ (including directed edges between vertices in $D$ ).

Let $A$ be a random-ancestral set in $\mathcal{G}$. Define $\mathfrak{m}_{A}(\mathcal{G})$ to be the graph with the set of random vertices $A$, the set of fixed vertices $\mathrm{pa}_{\mathcal{G}}(A) \backslash A$, and all edges between these vertices that are in $\mathcal{G}$. Note that, since $A$ is random-ancestral, by definition the vertices in $\mathrm{pa}_{\mathcal{G}}(A) \backslash A$ are already fixed vertices in $\mathcal{G}$.

If a graph $\mathcal{G}^{\prime}$ can be obtained from $\mathcal{G}$ by iteratively applying operations of the form $\mathfrak{d}$ and $\mathfrak{m}$, we say that $\mathcal{G}^{\prime}$ is reachable from $\mathcal{G}$.

Note that if we start with a graph $\mathcal{G}$ in which all the fixed vertices $w \in W$ have at least one child, then this is also true of the graph obtained after applying either $\mathfrak{m}_{A}$ or $\mathfrak{d}_{D}$.

Example 2.6. The graph in Figure 1(b) contains the districts $\{X\},\{E, Y\}$ and $\{M\}$. The corresponding graphs $\mathfrak{d}_{D}(\mathcal{G})$ are given in Figure 4(a), (b) and (c), respectively. The sets $\{X, E, M\}$, $\{X, E\}$ and $\{X\}$ are ancestral in $\mathcal{G}$, and the graphs $\mathfrak{m}_{\{X\}}(\mathcal{G})$ and $\mathfrak{m}_{\{X, E, M\}}(\mathcal{G})$ are shown in Figure 4(a) and (d), respectively.

Example 2.7. The graph in Figure 3 contains the district $\{2,4,5\}$, and $\mathfrak{d}_{\{2,4,5\}}(\mathcal{L})$ gives us the graph in Figure 5(a). The sets $\{2,4\}$ and $\{4,5\}$ are both random-ancestral in $\mathfrak{d}_{\{2,4,5\}}(\mathcal{L})$, so we can apply either $\mathfrak{m}_{\{2,4\}}$ or $\mathfrak{m}_{\{4,5\}}$ to obtain the CADMGs in Figure 5(b) and (c), respectively.

As we will see in the next section, both of these graphical operations correspond to an operation on a probability distribution we associate with the graph: $\mathfrak{m}_{A}$ to marginalization, and $\mathfrak{d}_{D}$ to a factorization. The 'fixing' operation described in Richardson et al. [17] unifies and generalizes $\mathfrak{m}$ and $\mathfrak{d}$, but the statistical model we will describe is ultimately the same. For the purposes of defining a parameterization, it is more convenient to use the formulation given here.

It is important to note that sets may become districts or random ancestral sets after several iterations of $\mathfrak{m}$ and $\mathfrak{d}$. For example, $\{2,4\}$ is not random-ancestral in $\mathcal{L}$, but it is in

![img-4.jpeg](img-4.jpeg)

Figure 5. Three CADMGs reachable from the graph in Figure 3.
$\mathfrak{d}_{[2,4,5]}(\mathcal{L})$. Similarly, $\{4\}$ is not a district in $\mathfrak{d}_{[2,4,5]}(\mathcal{L})$, but it is in $\mathfrak{m}_{[2,4]}\left(\mathfrak{d}_{[2,4,5]}(\mathcal{L})\right)$; see Figure 5(b).

We now give a characterization of what reachable graphs look like.
Definition 2.8. Let $\mathcal{G}$ be a CADMG with random vertex set $V$. Given $C \subseteq V$ the graph $\mathcal{G}[C]$ is defined to be the CADMG with the set of random vertices $C$, fixed vertices $\mathrm{pa}_{\mathcal{G}}(C) \backslash C$, those bidirected edges in $\mathcal{G}$ with both endpoints in $C$, and those directed edges that are directed from $C \cup \mathrm{pa}_{\mathcal{G}}(C)$ to $C$.

In other words, $\mathcal{G}[C]$ is the subgraph containing precisely the edges whose arrowheads are all in $C$. For example, if $\mathcal{G}$ is the graph in Figure 1(b), then Figure 4(a)-(d) corresponds to $\mathcal{G}[\{X\}]$, $\mathcal{G}[\{E, Y\}], \mathcal{G}[\{M\}]$ and $\mathcal{G}[\{X, E, M\}]$, respectively.

Lemma 2.9. Suppose that the graph $\mathcal{G}^{\prime}$ is reachable from $\mathcal{G}$ and has set of random vertices $C$. Then $\mathcal{G}^{\prime}=\mathcal{G}[C]$.

Proof. Since we assume all fixed vertices have at least one child, then $\mathcal{G}=\mathcal{G}[V]$. In addition, it is clear from the definitions of $\mathfrak{d}$ and $\mathfrak{m}$ that precisely the edges and fixed vertices mentioned are preserved at each step.

In the rest of this paper, we will only refer to $\mathcal{G}[C]$ if $C$ is a reachable set, though Definition 2.8 in principle applies to any $C \subseteq V$. Unfortunately, there is generally no simple way of characterizing which sets $C$ correspond to reachable subgraphs without iteratively applying $\mathfrak{d}$ and $\mathfrak{m}$ as defined above. If a set $A$ is random-ancestral, then clearly $\mathcal{G}[A]$ is reachable just by applying $\mathfrak{m}$. Note that Richardson et al. [17] use a more general definition of reachable sets.

# 3. Nested Markov property 

Graphical models relate the structure of a graph to a collection of joint probability distributions over a set of random variables. We will work with the nested Markov property, which relates a (C)ADMG and each of its reachable subgraphs to a collection of probability distributions over random vertices, indexed by fixed vertices.

Suppose we are interested in random variables $X_{v}$ taking values in a finite discrete set $\mathfrak{X}_{v}$. For a set of vertices $C$, let $\mathfrak{X}_{C} \equiv \times_{v \in C} \mathfrak{X}_{v}$. A probability kernel for $V$ given $W$ (or simply a kernel) is a function $p_{V \mid W}: \mathfrak{X}_{V} \times \mathfrak{X}_{W} \rightarrow[0,1]$ such that for each $x_{W} \in \mathfrak{X}_{W}$,

$$
\sum_{x_{V} \in \mathfrak{X}_{V}} p_{V \mid W}\left(x_{V} \mid x_{W}\right)=1
$$

In other words, a kernel behaves like a conditional probability distribution for $X_{V}$ given $X_{W}$. We use the word 'kernel' to emphasize that some of the conditional distributions we obtain are not equal to the usual conditional distribution obtained from elementary definitions, but instead correspond to certain interventional quantities.

In what follows, $\dot{\cup}$ is used to denote a union of disjoint sets.

Definition 3.1. Let $p_{V \mid W}$ be a kernel, and let $A \dot{\cup} B \dot{\cup} C=V$. The marginal kernel over $A, B \mid$ $W$ is defined to be:

$$
p_{A B \mid W}\left(x_{A}, x_{B} \mid x_{W}\right) \equiv \sum_{x_{C}} p_{V \mid W}\left(x_{V} \mid x_{W}\right)
$$

It is easy to check that $p_{A B \mid W}$ is also a kernel. A (version of the) conditional kernel of $A \mid B, W$ is any kernel $p_{A \mid B W}$ satisfying

$$
p_{A \mid B W}\left(x_{A} \mid x_{B}, x_{W}\right) \cdot p_{B \mid W}\left(x_{B} \mid x_{W}\right) \equiv p_{A B \mid W}\left(x_{A}, x_{B} \mid x_{W}\right)
$$

This is uniquely defined precisely for $x_{B}, x_{W}$ such that $p_{B \mid W}\left(x_{B} \mid x_{W}\right)>0$.
Remark 3.2. Note that, for convenience, if some of the fixed variables $W^{*} \subseteq W$ in a kernel $p_{V \mid W}$ are entirely irrelevant, (i.e. if the functions $p_{V \mid W}\left(\cdot \mid \cdot, y_{W^{*}}\right)$ are identical for all $y_{W^{*}} \in \mathfrak{X}_{W^{*}}$ ) we will describe it interchangably as a kernel of $V$ given $W$, and as a kernel of $V$ given $W \backslash W^{*}$, since in this case these objects are isomorphic: $p_{V \mid W}=p_{V \mid W \backslash W^{*}}$.

We are now in a position to define the nested model. The definition is recursive, and works by reference to the model applied iteratively to smaller and smaller graphs. The model is introduced in Richardson et al. [17], and is based on the constraint finding algorithm of Tian and Pearl [28], which follows a similar recursive structure.

Definition 3.3. Let $\mathcal{G}$ be a CADMG and $p_{V \mid W}$ a probability kernel. Say that $p_{V \mid W}$ recursively factorizes according to $\mathcal{G}$, and write $p_{V \mid W} \in \mathcal{M}_{r f}(\mathcal{G})$ if either $|V|=1$, or both:

(i) if $\mathcal{G}$ has districts $D_{1}, \ldots, D_{k}, k \geq 1$, then

$$
p_{V \mid W}\left(x_{V} \mid x_{W}\right)=\prod_{i} r_{i}\left(x_{D_{i}} \mid x_{\operatorname{pa}\left(D_{i}\right) \backslash D_{i}}\right)
$$

and where, if $k \geq 2$, each $r_{i}$ recursively factorizes according to $\mathcal{G}\left[D_{i}\right]=\mathfrak{d}_{D_{i}}(\mathcal{G})$; and
(ii) for each ancestral set $A$ with $V \backslash A \neq \varnothing$, the marginal distribution

$$
p_{A \cap V \mid W}\left(x_{A \cap V} \mid x_{W}\right)=\sum_{x_{V \backslash A}} p_{V \mid W}\left(x_{V} \mid x_{W}\right)
$$

does not depend upon $x_{W \backslash A}$ (so we denote it by $p_{A \cap V \mid A \cap W}$ in line with Remark 3.2), and this recursively factorizes according to $\mathcal{G}[V \cap A]=\mathfrak{m}_{V \cap A}(\mathcal{G})$.

Given a graph $\mathcal{G}$, we shall refer to $\mathcal{M}_{r f}(\mathcal{G})$ as the nested model associated with $\mathcal{G}$, and say that distributions in that set satisfy the nested Markov property with respect to $\mathcal{G}$. There are other, equivalent definitions: see Richardson et al. [17].

Remark 3.4. It is important to note that, in terms of the factors $r_{i}$ whose existence is implied by condition (i), the definition of recursive factorization 'starts from scratch' each time we perform the recursion. For example, we make no claim (yet) about the connection between a factor $r_{i}$ obtained from (i) and any such factors which arise after first applying (ii) and then later (i): see Example 3.5.

In the base case $V=\{v\}$ the definition places no restriction on the distribution of $X_{v}$ given $X_{W}$ (recall that, by assumption, all fixed vertices have at least one random child). The observed distribution obtained from a directed acyclic graph model with latent variables will satisfy conditions (i) and (ii) with respect to the ADMG that is the latent projection of that DAG (Tian and Pearl [27,28]). The models defined by the Markov properties for ADMGs introduced by Richardson [16] and parameterized by Evans and Richardson [9,10] can be defined by replacing (i) with the weaker requirement:
(i') $\mathcal{G}$ has districts $D_{1}, \ldots, D_{k}, k \geq 1$, and $p_{V \mid W}=\prod_{i} r_{i}$ where each $r_{i}$ is a kernel for $D_{i}$ given $\mathrm{pa}_{\mathcal{G}}\left(D_{i}\right) \backslash D_{i}$.
In other words, although the distribution must satisfy the ancestrality condition (ii) and then factorize, no further conditions are imposed on those factors: they are not required to obey any additional constraints implied by the graph $\mathcal{G}\left[D_{i}\right]$. This leads to a model defined entirely by conditional independence relations on the original joint distribution $p_{V \mid W}$.

As a consequence of this, the m-separation criterion for ordinary Markov models (as well as the other Markov properties described by Richardson [16]) can be applied correctly to the initial ADMG $\mathcal{G}$ to derive conditional independences in $p\left(x_{V}\right)$; however, applied solely to $\mathcal{G}$, this does not completely describe the nested model.

Example 3.5. Consider the CADMG in Figure 1(b). Criterion (i) of recursive factorization requires that

$$
p(x, e, m, y)=r_{X}(x) \cdot r_{E Y}(e, y \mid x, m) \cdot r_{M}(m \mid e)
$$

for distributions $r_{X}, r_{E Y}$ and $r_{M}$ which recursively factorize according to the graphs in Figure 4(a), (b) and (c), respectively.

On the other hand, if we apply condition (ii) to the childless node $Y$ we see that the margin $p(x, e, m)$ must satisfy recursive factorization with respect to the DAG in Figure 4(d), so

$$
p(x, m, e)=\tilde{r}_{X}(x) \cdot \tilde{r}_{E}(e \mid x) \cdot \tilde{r}_{M}(m \mid e)
$$

for some kernels $\tilde{r}_{X}, \tilde{r}_{M}$ and $\tilde{r}_{E}$. This factorization implies the conditional independence $X \Perp M \mid E$, which can also be deduced using m-separation. We add a tilde to the kernels to emphasise that the definition starts afresh at each iteration, and makes no claim of any relationship between this factorization and the factorization of $p=r_{X} r_{E Y} r_{M}$. However, it is not hard to verify that in this case

$$
\begin{aligned}
r_{X}(x) & =\tilde{r}_{X}(x)=p(x) \\
r_{M}(m \mid e) & =\tilde{r}_{M}(m \mid e)=p(m \mid e) \\
\sum_{y} r_{E Y}(e, y \mid x, m) & =\tilde{r}_{E}(e \mid x)=p(e \mid x)
\end{aligned}
$$

In fact, it will follow from Theorem 5.4 that, in general, kernels such as $r_{X}$ and $\tilde{r}_{X}$ that have the same random vertex set but are derived in different ways are equal under the model. Note that

$$
\begin{aligned}
r_{E Y}(e, y \mid x, m) & =p(e \mid x) \cdot p(y \mid x, m, e) \\
& \neq p(e \mid x, m) \cdot p(y \mid x, m, e) \\
& =p(e, y \mid x, m)
\end{aligned}
$$

and so $r_{E Y}$ is not the usual conditional distribution of $E, Y$ given $X, M$.

# 3.1. Properties of the recursive kernels 

Here we show that the kernels $r_{i}$ from (2) in Definition 3.3 are products of conditional distributions derived from $p_{V \mid W}$ at the current level of the recursion, and that they are uniquely defined up to versions of those conditional distributions.

A topological ordering of the random vertices of a CADMG is a total ordering $<$ on $V$ such that every vertex precedes its children. We denote by $\operatorname{pre}_{<}(v)$ the set of (random) vertices which precede $v$ under $<$.

The following proposition shows that the factors in the definition of recursive factorization are unique up to versions of conditional distributions.

Proposition 3.6. Let $\mathcal{G}$ be a CADMG with districts $D_{1}, \ldots, D_{k}$, and let $<$ be any topological ordering of $V$. Let $p_{V \mid W}=\prod_{i} r_{i}$, where each $r_{i}$ recursively factorizes with respect to $\mathcal{G}\left[D_{i}\right]$. Then

$$
r_{i}\left(x_{D_{i}} \mid x_{\mathrm{pa}_{\mathcal{G}}\left(D_{i}\right) \backslash D_{i}}\right)=\prod_{v \in D_{i}} p_{v \mid \operatorname{pre}_{<}(v) \cup W}\left(x_{v} \mid x_{\operatorname{pre}_{<}(v)}, x_{W}\right)
$$

where $p_{v \mid \operatorname{pre}_{<}(v) \cup W}$ is any $p_{V \mid W}$-version of the conditional distribution of $X_{v} \mid X_{\operatorname{pre}_{<}(v)}, X_{W}$.

Remark 3.7. The equation in (3) is an instance of the $g$-formula of Robins [18]. The result also appears as Corollary 1 in Tian [26], Section 4.3, in the case of latent variable models.

Proof. For the purposes of induction, we generalize the result slightly to allow $D_{i}$ to be collections of several districts. Let $E_{i} \equiv \mathrm{pa}_{\mathcal{G}}\left(D_{i}\right) \backslash D_{i}$. We proceed by induction on $|V|$ : if $|V| \leq 1$ there is nothing to show. Otherwise, let $t \in D_{k}$ be the last vertex in the ordering $<$, so that $x_{t}$ only appears as a variable in the factor $r_{k}$. Then

$$
\begin{aligned}
p_{V \backslash\{t\}|W}\left(x_{V \backslash\{t\}} \mid x_{W}\right) & \equiv \sum_{x_{t}} p_{V \mid W}\left(x_{V} \mid x_{W}\right) \\
& =\sum_{x_{t}} \prod_{i=1}^{k} r_{i}\left(x_{D_{i}} \mid x_{E_{i}}\right) \\
& =\left(\sum_{x_{t}} r_{k}\left(x_{D_{k}} \mid x_{E_{k}}\right)\right) \prod_{i=1}^{k-1} r_{i}\left(x_{D_{i}} \mid x_{E_{i}}\right) \\
& =\tilde{r}_{k}\left(x_{D_{k} \backslash\{t\}} \mid x_{E_{k}}\right) \prod_{i=1}^{k-1} r_{i}\left(x_{D_{i}} \mid x_{E_{i}}\right)
\end{aligned}
$$

where, by property 1 of recursive factorization, the kernel $\tilde{r}_{k}$ recursively factorizes with respect to the graph $\mathcal{G}\left[D_{k} \backslash\{t\}\right]$. Similarly, all the factors $r_{i}$ for $i=1, \ldots, k-1$ recursively factorize with respect to $\mathcal{G}\left[D_{i}\right]$, so by the induction hypothesis each such $r_{i}$ is of the required form (3), and

$$
\tilde{r}_{k}\left(x_{D_{k} \backslash\{t\}} \mid x_{E_{k}}\right)=\prod_{v \in D_{k} \backslash\{t\}} p_{v \mid \operatorname{pre}_{<}(v) \cup W}\left(x_{v} \mid x_{\operatorname{pre}_{<}(v)}, x_{W}\right)
$$

But then

$$
\prod_{i} r_{i}=p_{V \mid W}=p_{t \mid W, V \backslash\{t\}} \cdot p_{V \backslash\{t\}|W}=p_{t \mid W, V \backslash\{t\}} \cdot \tilde{r}_{k} \cdot \prod_{i=1}^{k-1} r_{i}
$$

therefore whenever $p_{V \backslash\{t\}|W}>0$

$$
r_{k}\left(x_{D_{k}} \mid x_{E_{k}}, x_{W}\right)=p_{t \mid W, V \backslash\{t\}}\left(x_{t} \mid x_{W}, x_{V \backslash\{t\}}\right) \cdot \tilde{r}_{k}
$$

Hence $p_{t \mid W, V \backslash\{t\}}$ satisfies (4) if and only if it is a version of the relevant conditional distribution, as required.

The next result shows that the positivity of $p_{V \mid W}$ is preserved in any derived kernels.
Lemma 3.8. Let $p_{V \mid W}\left(x_{V} \mid x_{W}\right)$ be a probability distribution, $<$ some total ordering on $V$, and let $A \subseteq V$ and $B \equiv W \cup \operatorname{pre}_{<}(A) \backslash A$. Define

$$
r_{A \mid B}\left(x_{A} \mid x_{B}\right) \equiv \prod_{v \in A} p_{v \mid \operatorname{pre}_{<}(v), W}\left(x_{v} \mid x_{\operatorname{pre}_{<}(v)}, x_{W}\right)
$$

for some versions $p_{v \mid \operatorname{pre}_{<}(v), W}$ of the conditional distributions of $X_{v} \mid X_{W}, X_{\operatorname{pre}_{<}(v)}$.

Then:
(a) $r_{A \mid B}$ is a kernel for $X_{A} \mid X_{B}$;
(b) for any $T \subseteq V, x_{T} \in \mathfrak{X}_{T}$ and $x_{W} \in \mathfrak{X}_{W}$, if $p_{T \mid W}\left(x_{T} \mid x_{W}\right)>0$ then

$$
r_{T \cap A \mid B}\left(x_{T \cap A} \mid x_{B}\right) \equiv \sum_{y_{A \backslash T}} r_{A \mid B}\left(y_{A \backslash T}, x_{T \cap A} \mid x_{B}\right)>0
$$

and all versions of $r_{T \cap A \mid B}\left(x_{T \cap A} \mid x_{B}\right)$ are the same;
(c) if $p_{T \mid W}\left(x_{T} \mid x_{W}\right)=0$ then there exists $t \in T$ such that (every version of)

$$
p_{t \mid \operatorname{pre}_{<}(t), W}\left(x_{t} \mid x_{\operatorname{pre}_{<}(t)}, x_{W}\right)=0
$$

Proof. (a) Clearly $r_{A \mid B} \geq 0$ since it is a product of conditional distributions, which are themselves non-negative. In addition, by summing the expression above in reverse order of $<$ it is easy to see that $\sum_{x_{A}} r_{A \mid B}\left(x_{A} \mid x_{B}\right)=1$ for any $x_{B} \in \mathfrak{X}_{B}$. Hence, $r_{A \mid B}$ is a kernel.

For (b), note that if $p_{T \mid W}\left(x_{T} \mid x_{W}\right)>0$, then there exists some $x_{V \backslash T} \in \mathfrak{X}_{V \backslash T}$ such that $p_{V \mid W}\left(x_{V} \mid x_{W}\right)>0$. Then

$$
\begin{aligned}
p_{V \mid W}\left(x_{V} \mid x_{W}\right) & =\prod_{v \in V} p_{v \mid \operatorname{pre}_{<}(v), W}\left(x_{v} \mid x_{\operatorname{pre}_{<}(v)}, x_{W}\right) \\
& =r_{A \mid B}\left(x_{A} \mid x_{B}\right) \prod_{v \in V \backslash A} p_{v \mid \operatorname{pre}_{<}(v), W}\left(x_{v} \mid x_{\operatorname{pre}_{<}(v)}, x_{W}\right)
\end{aligned}
$$

so if the left-hand side is positive then so is $r_{A \mid B}\left(x_{A} \mid x_{B}\right)>0$. Since all the events in this expression have positive $p_{V \mid W}$ probability, all versions of each conditional probability are equal.

Lastly, if $p_{T \mid W}\left(x_{T} \mid x_{W}\right)=0$ then clearly some factor of

$$
0=p_{T \mid W}\left(x_{T} \mid x_{W}\right)=\prod_{t \in T} p_{t \mid \operatorname{pre}_{<}(t), W}\left(x_{t} \mid x_{\operatorname{pre}_{<}(t)}, x_{W}\right)
$$

is also zero. Pick the $<$-minimal $t$ such that this holds, so that $p_{\operatorname{pre}_{<}(t) \mid W}\left(x_{\operatorname{pre}_{<}(t)} \mid x_{W}\right)>0$. Then (c) holds.

A corollary of this lemma is the following.
Corollary 3.9. Let $p_{V \mid W} \in \mathcal{M}_{r f}(\mathcal{G})$ be a strictly positive kernel. Then any kernel derived from $p_{V \mid W}$ by repeated applications of Definition 3.3 (using $\mathcal{G}$ ) is uniquely defined.

Proof. Clearly applying (ii) is always unique, since it only involves summing. By Proposition 3.6, application of (i) is a factorization into univariate conditional distributions, each of which is uniquely defined when the joint distribution is positive. In addition, by Lemma 3.8 each such conditional distribution is also strictly positive, so following the recursion with each unique factor gives the result.

# 4. Intrinsic sets and partitions 

In this section, we provide the necessary theory to link the graphical notions of Section 3 to the parameterization in Section 5. The parameterization uses factorizations of the distribution into pieces that correspond to special subsets of vertices in the graph; these subsets are themselves derived from the idea of the 'reachable' sets already introduced.

Definition 4.1. Let $\mathcal{G}$ be a CADMG. A non-empty set $S$ of random vertices is intrinsic if it is bidirected-connected and the graph $\mathcal{G}[S]$ is reachable from $\mathcal{G}$.

For each intrinsic set $S$, define the associated recursive head by $\operatorname{rh}_{\mathcal{G}}(S)=\operatorname{sterile}_{\mathcal{G}}(S)$; that is, it is the set of sink nodes in the induced subgraph over $S$. The set of recursive heads is denoted by $\mathcal{H}(\mathcal{G})$, or simply $\mathcal{H} .{ }^{1}$

The tail associated with a recursive head $H$ (and the relevant intrinsic set $S$ ) is $T(H) \equiv$ $\mathrm{pa}_{\mathcal{G}}(S)$. We will denote a tail by $T$ if it is unambiguous which recursive head it is derived from.

Intrinsic sets are central to the nested Markov property as they are the sets of variables over which the kernels $r_{i}$ in Definition 3.3 specify distributions. Intrinsic sets do not appear to be easily characterized in terms of the presence of a path in the original graph; Definition 4.1 implicitly considers a sequence of graphs generated via repeated applications of the two operations $\mathfrak{d}$ and $\mathfrak{m}$. The set of intrinsic sets may be found in polynomial time; see Shpitser et al. [22].

Example 4.2. For the graph $\mathcal{L}$ in Figure 3, $\{2,4,5\}$ and $\{3\}$ are districts and therefore intrinsic sets. The graph $\mathcal{L}[\{2,4,5\}]$ is shown in Figure 5(a); applying m appropriately to randomancestral sets yields all the other intrinsic sets: $\{2,5\},\{4,5\},\{2\},\{4\}$ and $\{5\}$. Each recursive head is equal to the associated intrinsic set.

Definition 4.3. Let $B \subseteq V$ be a set of random vertices in $\mathcal{G}$. Suppose we alternately marginalize vertices that are not ancestors of $B$, and remove those which are not in the same district as some element of $B$ :

$$
\mathcal{G} \mapsto \mathfrak{m}_{\operatorname{an}_{\mathcal{G}}(B)}(\mathcal{G}), \quad \mathcal{G} \mapsto \mathfrak{d}_{\operatorname{dis}_{\mathcal{G}}(B)}(\mathcal{G})
$$

If these two operations change anything at all then they reduce the size of the set of random vertices; consequently repeatedly applying both these operations successively will eventually reach some stable point, which is a graph whose set of random vertices we denote by $I_{\mathcal{G}}(B)$. Note that at each step of (5) the random vertices in the resulting graph always include $B$, so $B \subseteq I_{\mathcal{G}}(B)$.

If $I_{\mathcal{G}}(B)$ is bidirected-connected, then it is an intrinsic set by definition, and we call $I_{\mathcal{G}}(B)$ the intrinsic closure of $B$.

[^0]
[^0]:    ${ }^{1}$ Note that the definition of a recursive head differs from the head used in Evans and Richardson [10] for ADMGs. We will see in Example 4.12 that $\{E, Y\}$ is a recursive head in the graph in Figure 1(b), but one can check that it is not a head in the Evans and Richardson [10] sense.

![img-5.jpeg](img-5.jpeg)

Figure 6. (a) $\mathrm{A}(\mathrm{C}) \mathrm{ADMG} \mathcal{G}$ and (b) $\mathcal{G}_{1} \equiv \mathfrak{d}_{\operatorname{dis}(Y)}(\mathcal{G})$.

Proposition 4.4. If $\mathcal{G}^{\prime}=\mathcal{G}[C]$ is reachable from $\mathcal{G}$ for some set $C \supseteq B$, then

$$
\mathfrak{m}_{\mathfrak{a n}_{\mathcal{G}^{\prime}}(B)}\left(\mathcal{G}^{\prime}\right) \subseteq \mathfrak{m}_{\mathfrak{a n}_{\mathcal{G}}(B)}(\mathcal{G}), \quad \mathfrak{d}_{\operatorname{dis}_{\mathcal{G}^{\prime}}(B)}\left(\mathcal{G}^{\prime}\right) \subseteq \mathfrak{d}_{\operatorname{dis}_{\mathcal{G}}(B)}(\mathcal{G})
$$

Note that here and in what follows we use $\subseteq$ as a subgraph relation when applied to graphs.
Proof. From Lemma 2.9, $\mathcal{G}^{\prime}=\mathcal{G}[C]$; We have $\mathfrak{m}_{\mathfrak{a n}_{\mathcal{G}^{\prime}}(B)}\left(\mathcal{G}^{\prime}\right)=\mathcal{G}\left[\mathfrak{a n}_{\mathcal{G}^{\prime}}(B)\right]$ and $\mathfrak{m}_{\mathfrak{a n}_{\mathcal{G}}(B)}(\mathcal{G})=$ $\mathcal{G}\left[\mathfrak{a n}_{\mathcal{G}}(B)\right]$. Any ancestor of $B$ in the subgraph $\mathcal{G}^{\prime}=\mathcal{G}[C]$ must be also be an ancestor in $\mathcal{G}$, so clearly $\mathcal{G}\left[\mathfrak{a n}_{\mathcal{G}^{\prime}}(B)\right] \subseteq \mathcal{G}\left[\mathfrak{a n}_{\mathcal{G}}(B)\right]$. A similar argument holds for $\mathfrak{d}$.

Both of the operators in (5) are idempotent; in addition, since the sets an $(B)$ and $\operatorname{dis}(B)$ only get smaller through repeated iterations, it follows from Proposition 4.4 that the stable point does not depend upon which operation is applied first. Hence, $I_{\mathcal{G}}(B)$ is well-defined.

Example 4.5. Let $\mathcal{G}$ be the graph in Figure 6(a) and consider the intrinsic closure of the bidirected-connected set $\{Y\}$. The graph $\mathfrak{m}_{\text {an }(Y)}(\mathcal{G})$ is just $\mathcal{G}$, since everything is an ancestor of $Y$. However $\mathcal{G}_{1} \equiv \mathfrak{d}_{\operatorname{dis}(Y)}(\mathcal{G})$ gives the graph $\mathcal{G}[\{X, Y\}]$ shown in Figure 6(b) in which $Z$ is fixed, but the edges are all unchanged. It then becomes clear that repeatedly applying $\mathfrak{m}$ and $\mathfrak{d}$ will not result in any further changes to the graph. Hence, the intrinsic closure is just the set of random vertices in this graph: $I_{\mathcal{G}}(\{Y\})=\{X, Y\}$.

On the other hand, consider the graph $\mathcal{L}$ in Figure 3 and the intrinsic closure of the set $\{4,5\}$. Again $\mathfrak{m}_{\text {an }(\{4,5\})}(\mathcal{L})=\mathcal{L}$, and then $\mathfrak{d}_{\operatorname{dis}(\{4,5\})}(\mathcal{L})$ gives the graph in Figure 5(a). Applying $\mathfrak{m}_{\text {an }(\{4,5\})}(\cdot)$ to this graph yields the graph in Figure 5(c), whose only random vertices are $\{4,5\}$. Hence, the procedure terminates and, since it forms a district in this graph, $\{4,5\}$ is an intrinsic set and its own intrinsic closure.

One consequence of the next result is that, as we would hope, every intrinsic set is its own intrinsic closure.

Lemma 4.6. Let $S$ be an intrinsic set with recursive head $H$ in a graph $\mathcal{G}$. Then for any set $A$ such that $H \subseteq A \subseteq S$ we have $I_{\mathcal{G}}(A)=S$.

Proof. By the definition of $H$, every vertex in $S$ is either in $H$ or is a parent of some other element of $S$. Since $S$ is bidirected-connected, the operations $\mathfrak{d}_{A}, \mathfrak{m}_{A}$ therefore cannot remove any element of $S$ without also having removed an element of $H$, but this is not allowed since $H \subseteq A$. Hence, no element of $S$ is ever removed, and $I_{\mathcal{G}}(A) \supseteq S$.

Suppose that $I_{\mathcal{G}}(A) \supset S$ and so $B \equiv I_{\mathcal{G}}(A) \backslash S$ is non-empty. Every element of $B$ is an ancestor of some other entry in $I_{\mathcal{G}}(A)$. In addition, every element of $I_{\mathcal{G}}(A)$ is connected to $A \subseteq S$ by sequences of bidirected edges through $I_{\mathcal{G}}(A)$, so $I_{\mathcal{G}}(A)$ is, like $S$, a bidirected-connected set. Thus, we cannot remove any element of $B$ via operations of the form $\mathfrak{m}, \mathfrak{d}$ without first removing some element of $A \subseteq S$. If $B$ is non-empty, then this implies $S$ is not reachable, which contradicts the assumption that $S$ is intrinsic.

Note that a corollary of this result is that recursive heads are in one-to-one correspondence with intrinsic sets: two distinct intrinsic sets may not have the same recursive head.

Proposition 4.7. If $B$ is a bidirected-connected set with intrinsic closure $I_{\mathcal{G}}(B)$, then the recursive head $H$ associated with the intrinsic set $I_{\mathcal{G}}(B)$ satisfies $H \subseteq B$.

Proof. By definition of intrinsic closure, every vertex $v$ in $I_{\mathcal{G}}(B)$ is an ancestor of $B$ in $\mathcal{G}\left[I_{\mathcal{G}}(B)\right]$. If $v \notin B$, then $v \notin \operatorname{sterile}_{\mathcal{G}}\left(I_{\mathcal{G}}(B)\right)$, hence $v \notin H$.

Lemma 4.8. Every singleton $\{v\}$ for $v \in V$ is a recursive head.
Proof. Take the intrinsic closure $I_{\mathcal{G}}(\{v\})$ of $v$. Every element of $I_{\mathcal{G}}(\{v\})$ other than $v$ is a parent of some other element of $I_{\mathcal{G}}(\{v\})$ by definition; therefore $\{v\}$ is the sterile set, and a recursive head.

Lemma 4.9. Let $\mathcal{G}$ be a CADMG, and $\mathcal{G}^{\prime}$ be a CADMG with random vertices $V^{\prime}$, reachable from $\mathcal{G}$. Then the intrinsic sets of $\mathcal{G}^{\prime}$ are precisely the intrinsic sets of $\mathcal{G}$ that are contained in $V^{\prime}$, and their associated recursive heads and tails are the same.

Proof. Since $\mathcal{G}^{\prime}=\mathcal{G}\left[V^{\prime}\right]$ is reachable from $\mathcal{G}$, any intrinsic set in $\mathcal{G}^{\prime}$ is also an intrinsic set in $\mathcal{G}$. For the converse, suppose that $D \subseteq V^{\prime}$ is an intrinsic set in $\mathcal{G}$. Take the intrinsic closure of $D$ in $\mathcal{G}^{\prime}$, say $C$; if $C=D$ then we are done.

Suppose not, so that $C \backslash D$ is non-empty. This occurs precisely when $C$ is bidirected-connected in $\mathcal{G}^{\prime}$, and every vertex in $C \backslash D$ is an ancestor in $\mathcal{G}^{\prime}$ of some other vertex in $C$. But if this is true in $\mathcal{G}^{\prime}$, then it must also be true in $\mathcal{G}$, which contains any edges that $\mathcal{G}^{\prime}$ does; thus the intrinsic closure of $D$ in $\mathcal{G}$ is a strict superset of $D$. This contradicts the assumption that $D$ is intrinsic in $\mathcal{G}$.

By Lemma 2.9 the recursive heads and tails associated with each intrinsic set are unchanged, since the parent sets of each random vertex are preserved.

Corollary 4.10. Let $\mathcal{G}$ be a CADMG containing random-ancestral sets $A_{1}, A_{2}$. If $H \in \mathcal{H}\left(\mathcal{G}\left[A_{1}\right]\right)$ and $H \in \mathcal{H}\left(\mathcal{G}\left[A_{2}\right]\right)$, then $H \in \mathcal{H}\left(\mathcal{G}\left[A_{1} \cap A_{2}\right]\right)$.

Proof. If $A_{1}$ and $A_{2}$ are random-ancestral, then so is $A_{1} \cap A_{2}$, so the graph $\mathcal{G}\left[A_{1} \cap A_{2}\right]$ is reachable from $\mathcal{G}$. The result follows from Lemma 4.9.

# 4.1. Partitions 

We follow the approach of Evans and Richardson [10] by defining partitions of sets via appropriate collections of subsets. Define a partial ordering $\prec$ on recursive heads by $H_{1} \prec H_{2}$ whenever $I_{\mathcal{G}}\left(H_{1}\right) \subset I_{\mathcal{G}}\left(H_{2}\right)$.

Definition 4.11. Define a function $\Phi_{\mathcal{G}}$ on sets of random vertices $C \subseteq V$ that 'picks out' the set of $\prec$-maximal recursive heads $H \in \mathcal{H}(\mathcal{G})$ that are subsets of $C$. That is,

$$
\Phi_{\mathcal{G}}(C) \equiv\left\{H \in \mathcal{H} \mid H \subseteq C \text { and } H \nprec H^{\prime} \text { for all other } H^{\prime} \subseteq C, H^{\prime} \in \mathcal{H}\right\}
$$

Define

$$
\psi_{\mathcal{G}}(C) \equiv C \backslash \bigcup_{D \in \Phi_{\mathcal{G}}(C)} D
$$

Now recursively define a function $\llbracket \cdot \rrbracket_{\mathcal{G}}$ that partitions subsets of $V$ : define $\llbracket \varnothing \rrbracket_{\mathcal{G}}=\varnothing$, and

$$
\llbracket W \rrbracket_{\mathcal{G}} \equiv \Phi_{\mathcal{G}}(W) \cup \llbracket \psi_{\mathcal{G}}(W) \rrbracket_{\mathcal{G}}
$$

For full details, including a proof that this definition does indeed define a partition, see the Appendix B.

Example 4.12. The recursive heads of the graph in Figure 1(b) are $\{X\},\{E\},\{M\},\{Y\},\{E, Y\}$, and the ordering requires that $\{E\}$ and $\{Y\}$ precede $\{E, Y\}$. Hence, for example

$$
\begin{aligned}
\llbracket\{X, E, Y\} \rrbracket_{\mathcal{G}} & =\{\{X\},\{E, Y\}\} \\
\llbracket\{M, Y\} \rrbracket_{\mathcal{G}} & =\{\{M\},\{Y\}\}
\end{aligned}
$$

The partitioning function $[\cdot]_{\mathcal{G}}$ in Evans and Richardson [10] made use of 'heads' rather than 'recursive heads', and therefore the partition obtained differs from the one here. For example, applied to the same graph as above,

$$
[\{X, E, Y\}]_{\mathcal{G}}=\{\{X\},\{E\},\{Y\}\}
$$

Lemma 4.13. If $\mathcal{G}^{\prime}=\mathcal{G}[D]$ is reachable from $\mathcal{G}$ then $\llbracket C \rrbracket_{\mathcal{G}^{\prime}}=\llbracket C \rrbracket_{\mathcal{G}}$ for every $C \subseteq D$.
Proof. By Lemma 4.9, the intrinsic sets of $\mathcal{G}^{\prime}=\mathcal{G}[D]$ are precisely the intrinsic sets of $\mathcal{G}$ that are subsets of $D$, with the same associated recursive heads. Hence the result follows from the definition of $\prec$.

Lemma 4.14. If $\mathcal{G}$ is such that $V=D_{1} \dot{\cup} D_{2}$ for sets $D_{1}, D_{2}$ not connected by bidirected edges, then

$$
\llbracket C \rrbracket_{\mathcal{G}}=\llbracket C \cap D_{1} \rrbracket_{\mathcal{G}} \cup \llbracket C \cap D_{2} \rrbracket_{\mathcal{G}}
$$

Proof. Since every intrinsic set (and therefore recursive head) is a subset of either $D_{1}$ or $D_{2}$, the result follows from Propositions B. 4 and B. 5 in the Appendix.

# 5. Parameterization 

We are now in a position to introduce the parameterization. Recall that $T$ denotes the tail associated with a recursive head $H$. We will present the parameterization for binary variables only, that is, those with state-space $\mathfrak{X}_{v} \equiv\{0,1\}$, each $v \in V \dot{\cup} W$; the extension to non-binary discrete variables is conceptually simple but notationally cumbersome. Appendix C contains notes on the general case.

Definition 5.1. Let $\mathcal{G}$ be a CADMG with random vertices $V$ and fixed vertices $W$. We say that $p_{V \mid W}$ is parameterized according to $\mathcal{G}$, and write $p_{V \mid W} \in \mathcal{M}_{p}(\mathcal{G})$, if it can be written in the form:

$$
p_{V \mid W}\left(x_{V} \mid x_{W}\right)=\sum_{C: O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right), \quad x_{V W} \in \mathfrak{X}_{V W}
$$

where we define $O \equiv O\left(x_{V}\right) \equiv\left\{v \in V \mid x_{v}=0\right\}$. Here $q_{H}\left(x_{T}\right) \in \mathbb{R}$ for each $H \in \mathcal{H}, x_{T} \in \mathfrak{X}_{T}$, and $T \equiv T(H)$ is the tail associated with the recursive head $H$.

Note that if $C=\varnothing$ then the product is empty, which we define to be equal to 1 . It will be shown in Section 5.3 that if $p_{V \mid W}$ is of the above form then $q_{H}\left(x_{T}\right) \in[0,1]$ for all $H$ and $x_{T}$, or can be chosen to be so. In fact, if the graph is interpreted causally, then each $q_{H}\left(x_{T}\right)$ is the same as $p_{H \mid T}\left(0_{H} \mid x_{T \backslash \bar{T}}, \operatorname{do}\left(x_{\bar{T}}\right)\right)$, where $\bar{T}$ is a suitable subset of $T$ (see Theorem 5.5), and $0_{H}$ denotes $\bigcup_{h \in H}\left\{X_{h}=0\right\}$.

### 5.1. Comparison to other graphical parameterizations

It is worth remarking on some special cases of the parameterization: if $\mathcal{G}$ is a DAG then each $H$ is a singleton $\{h\}$, and (6) is just the familiar parameterization in terms of conditional probability tables using corner-point identifiability constraints: $q_{H}\left(x_{T}\right)=p_{h \mid \mathrm{pa}(h)}\left(0_{h} \mid x_{\mathrm{pa}(h)}\right)$. If $\mathcal{G}$ has only bidirected edges, then $T=\varnothing$, and (6) reduces to the parameterization given in Drton and Richardson [6]. If $\mathcal{G}$ has a chain graph structure, that is, the districts can be ordered so that $v \rightarrow w$ only if $v$ 's district is strictly before $w$ 's, then the parameterization reduces to that given in Drton [4].

A comparison with the parameterization of Evans and Richardson [10] is more subtle. Since the ordinary Markov models in that paper only use the weaker requirement ( $\mathrm{i}^{\prime}$ ) (see Section 3) we would expect that they generally have a larger dimension than the nested model for the same graph, and therefore use a different parameterization. If the models are the same, and if each intrinsic set can be obtained from a single marginalization step followed by factorization, then the 'ordinary' heads and tails will be the same as the recursive heads and tails, and hence the parameterization will be identical.

![img-6.jpeg](img-6.jpeg)

Figure 7. An ADMG whose nested and ordinary Markov models are the same, but for which the parameterizations of Evans and Richardson [10] and this paper are distinct.

However, even if the ordinary and nested models are the same, the parameterizations can be different. Consider the graph in Figure 7 (a modified version of $\mathcal{L}$ ). In this case, the ordinary and nested models are the same and both represent the distributions for which $X_{5} \perp X_{3} \mid X_{2}$ and $X_{4} \perp X_{2} \mid X_{3}$; this is the same as the corresponding maximal ancestral graph model. Since the set $[2,4,5]$ is a recursive head the nested parameterization includes the quantity $q_{245}\left(x_{3}\right)=P\left(X_{2}=\right.$ $\left.X_{4}=X_{5}=0 \mid \operatorname{do}\left(x_{3}\right)\right)$ (see Theorem 5.5), whereas the ordinary parameterization does not have such a head, and uses only ordinary conditional probabilities such as $P\left(X_{4}=0, X_{5}=0 \mid x_{2}, x_{3}\right)$.

In general, the number of parameters in the nested model is no greater than the number in the ordinary Markov model, though this number can be quite large even for sparse graphs if the districts are large. The number of parameters for a particular district will be at least quadratic in the district size, this most parsimonious case occurring if the district is a single chain. The number of parameters may grow exponentially in the number of vertices, even for models with only a linear number of edges: for example, if we have a 'star' graph with all bidirected edges (this is equivalent to a star-shaped DAG with all edges pointing to the central node). Such large models are potentially undesirable, and methods to reduce the parameter count are suggested by Shpitser et al. [19].

# 5.2. Main results 

We will show that distributions are parameterized according to $\mathcal{G}$ precisely when they recursively factorize according to $\mathcal{G}$, so that in fact $\mathcal{M}_{r f}(\mathcal{G})=\mathcal{M}_{p}(\mathcal{G})$. In particular, a distribution of the form (6) satisfies properties (i) and (ii) of the recursive factorization. This is shown by the next two lemmas.

Lemma 5.2. Let $\mathcal{G}$ be a CADMG with random vertices $V=D_{1} \dot{\cup} \cdots \dot{U} D_{l}$, such that for $i \neq j$ there is no bidirected edge in $\mathcal{G}$ from a vertex in $D_{i}$ to a vertex in $D_{j}$. Then for all $x_{V W} \in \mathfrak{X}_{V W}$ and $O \equiv O\left(x_{V}\right)$,

$$
\sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)=\prod_{i=1}^{l} \sum_{O_{i} \subseteq C \subseteq D_{i}}(-1)^{|C \backslash O_{i}|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
$$

where $O_{i}=O \cap D_{i}$.

Proof. We prove the result for $l=2$, from which the general result follows by induction. From Lemma 4.14,

$$
\prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)=\prod_{H \in \llbracket C \cap D_{1} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \times \prod_{H \in \llbracket C \cap D_{2} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
$$

In addition, if $C_{i}=C \cap D_{i}$, then $C \backslash O=\left(C_{1} \backslash O_{1}\right) \cup\left(C_{2} \backslash O_{2}\right)$ and this is the union of two disjoint sets, so $|C \backslash O|=\left|C_{1} \backslash O_{1}\right|+\left|C_{2} \backslash O_{2}\right|$. Hence,

$$
\begin{aligned}
& \sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& =\sum_{O \subseteq C \subseteq D_{1} \cup D_{2}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \cap D_{1} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \prod_{H \in \llbracket C \cap D_{2} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& =\sum_{O_{1} \subseteq C_{1} \subseteq D_{1}}(-1)^{\left|C_{1} \backslash O_{1}\right|} \prod_{H \in \llbracket C_{1} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& \quad \times \sum_{O_{2} \subseteq C_{2} \subseteq D_{2}}(-1)^{\left|C_{2} \backslash O_{2}\right|} \prod_{H \in \llbracket C_{2} \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

Lemma 5.3. Let $\mathcal{G}$ be a CADMG with a random vertex $v$. Then for all $x_{V W} \in \mathfrak{X}_{V W}$ and $O \equiv$ $O\left(x_{V}\right)$,

$$
\begin{aligned}
& \sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& \quad=\sum_{O \subseteq C \subseteq V \backslash\{v\}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)-\sum_{O \cup\{v\} \subseteq C \subseteq V}(-1)^{|C \backslash(O \cup\{v\})|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

Proof. Separating the sum into those subsets $C$ that contain $v$ and those which do not gives

$$
\begin{aligned}
& \sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& \quad=\sum_{O \subseteq C \subseteq V \backslash\{v\}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)+\sum_{O \cup\{v\} \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

which is seen to be the same as the given expression by including a factor of -1 inside and outside the second sum.

We now move to the main result of the paper.
Theorem 5.4. The kernel $p_{V \mid W}$ recursively factorizes according to $\mathcal{G}$ if and only if it is parameterized according to $\mathcal{G}$.

Proof. Throughout the proof, we will write the partitions of vertices in a CADMG as $\llbracket \cdot \rrbracket_{\mathcal{G}}$ regardless of which graph we are dealing with; since all the graphs we consider are reachable from $\mathcal{G}$, this is justified by Lemma 4.13.

We proceed by induction on the size of $V$. If $V=\{v\}$ then recursive factorization is by definition, so the condition holds for any distribution. On the other hand, parameterization entails

$$
p_{v \mid W}\left(0_{v} \mid x_{W}\right)=q_{v}\left(x_{\mathrm{pa}(v)}\right), \quad p_{v \mid W}\left(1_{v} \mid x_{W}\right)=1-q_{v}\left(x_{\mathrm{pa}(v)}\right)
$$

which follows from setting $q_{v}\left(x_{\mathrm{pa}(v)}\right)=p_{v \mid W}\left(0_{v} \mid x_{W}\right)$ and the fact that $p_{v \mid W}\left(0_{v} \mid x_{W}\right)+$ $p_{v \mid W}\left(1_{v} \mid x_{W}\right)=1$ because $p_{v \mid W}$ is a probability distribution; hence parameterization also holds for any distribution with one random variable.
$(\Leftarrow)$ Now consider a general $V$ and suppose $p_{V \mid W}$ is parameterized according to $\mathcal{G}$. If $\mathcal{G}$ has multiple districts then, by Lemma 5.2, the kernel factorizes into pieces which are parameterized according to $\mathcal{G}\left[D_{i}\right]$, and so by the induction hypothesis recursively factorize according to $\mathcal{G}\left[D_{i}\right]$.

Otherwise take any $a \in \operatorname{sterile}_{\mathcal{G}}(V)$, and consider a specific $x_{W, V \backslash\{a\}} \in \mathfrak{X}_{W, V \backslash\{a\}}$; let $O=\{v \in$ $\left.V \backslash\{a\} \mid x_{v}=0\right\}$, so then

$$
\begin{aligned}
\sum_{x_{a}} p\left(x_{V} \mid x_{W}\right)= & p\left(x_{V \backslash a}, 0_{a} \mid x_{W}\right)+p\left(x_{V \backslash a}, 1_{a} \mid x_{W}\right) \\
= & \sum_{O \cup\{a\} \subseteq C \subseteq V}(-1)^{|C| \cdot(O \cup\{a\})|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& +\sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
= & \sum_{O \subseteq C \subseteq V \backslash\{a\}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

by Lemma 5.3. By the induction hypothesis, this last expression recursively factorizes according to $\mathcal{G}[V \backslash\{a\}]=\mathfrak{m}_{V \backslash a}(\mathcal{G})$, and this extends easily to any random-ancestral margin $V \backslash B$ by sequentially marginalizing the variables in $B$. Hence, $p_{V \mid W}$ obeys properties (i) and (ii) of recursive factorization, and therefore recursively factorizes according to $\mathcal{G}$.
$(\Rightarrow)$ Conversely, suppose that $p_{V \mid W}$ recursively factorizes according to $\mathcal{G}$. In this direction, we will strengthen the induction hypothesis slightly and show that if $p_{V \mid W}$ recursively factorizes according to $\mathcal{G}$ then $p_{V \mid W}$ is parameterized according to $\mathcal{G}$, and that for each parameter $q_{H}\left(x_{T}\right)$, either: $p_{T \backslash W \mid W}\left(x_{T \backslash W} \mid x_{T \cap W}, y_{W \backslash T}\right)>0$ for some $y_{W \backslash T}$, in which case $q_{H}\left(x_{T}\right)$ is uniquely recoverable from $p_{V \mid W}$; or $p_{T \backslash W \mid W}\left(x_{T \backslash W} \mid x_{T \cap W}, y_{W \backslash T}\right)=0$ for all $y_{W \backslash T}$, in which case $q_{H}\left(x_{T}\right)$ can take any value. For the base case with $|V|=1$, the result follows from the derivation of (7).

If $\mathcal{G}$ has multiple districts then, by definition, $p_{V \mid W}$ factorizes into pieces which themselves recursively factorize according to the district subgraphs $\mathcal{G}\left[D_{i}\right]$, and by the induction hypothesis each factor is parameterized according to $\mathcal{G}\left[D_{i}\right]$. Applying Lemma 5.2 it follows that $p_{V \mid W}$ is parameterized according to $\mathcal{G}$, and no parameters are shared between these factors by Lemma 4.14.

For uniqueness of $q_{H}\left(x_{T}\right)$, note that this parameter only appears in the expansion for probabilities $p_{V \mid W}\left(x_{V} \mid x_{W}\right)$ (i.e., those indexed by the same values $x_{T}$ ). If $p_{T \backslash W \mid W}\left(x_{T \backslash W} \mid x_{W}\right)>0$,

then the factorization of $p_{V \mid W}$ is unique for these values by Proposition 3.6, and each factor is also positive for those values of $x_{T}$ by Lemma 3.8 ; thus $q_{H}\left(x_{T}\right)$ is uniquely recoverable from that factor by the strengthened induction hypothesis.

If $p_{T \backslash W \mid W}\left(x_{T \backslash W} \mid x_{W}\right)=0$, then by Lemma 3.8 there is some $t \in T \backslash W$ and $x_{V \backslash T}$ such that every version of $p_{t \mid \operatorname{pre}_{w}(t), W}\left(x_{t} \mid x_{\operatorname{pre}_{w}(t)}, x_{W}\right)=0$. We split into two cases: either $t$ is in the same district as $H$, or not; let $D_{1}$ be the district containing $H$, and the associated kernel $r_{1}$. If $t$ is in $D_{1}$, then it follows from Proposition 3.6 that $r_{1}\left(x_{T \cap D_{1}} \mid x_{T \backslash D_{1}}\right)=0$, and so by the induction hypothesis applied to $\mathcal{G}\left[D_{1}\right]$ we get that $q_{H}\left(x_{T}\right)$ can take any value. Otherwise if $t$ is in a different district (say $D_{2}$ ), then it follows from Proposition 3.6 that $r_{2}\left(x_{T \cap D_{2}} \mid x_{\operatorname{pa}\left(D_{2}\right) \backslash D_{2}}\right)=0$; so clearly whatever the value of any other factor, including $r_{1}$, the product will always be zero.

Now suppose $\mathcal{G}$ has a single district $V$; it follows from the definitions that $V$ is intrinsic with recursive head $H^{*}=\operatorname{sterile}_{\mathcal{G}}(V)$ and tail $T^{*}=(V \cup W) \backslash H^{*}$. For any vertex $h \in H^{*}$ the set $V \backslash\{h\}$ is random-ancestral, so the margin $p_{V \backslash h \mid W}$ recursively factorizes with respect to $\mathcal{G}[V \backslash\{h\}]$, and therefore (by the induction hypothesis) is also parameterized according to $\mathcal{G}[V \backslash\{h\}]$. Every recursive head $H$ other than $H^{*}$ is found in at least one random-ancestral margin $V \backslash\{h\}$ of $\mathcal{G}$, so applying the induction hypothesis to $\mathcal{G}[V \backslash\{h\}]$ we obtain either a well defined parameter, or determine that its value is irrelevant.

If two or more random-ancestral margins contain the recursive head $H$, note that by Corollary 4.10 there is a 'smallest' such margin $p_{\operatorname{an}(H) \backslash W \mid W}$ containing $H$; all other random-ancestral margins contain this margin, and therefore by the induction hypothesis they will agree either on a value for $q_{H}\left(x_{T}\right)$ or agree that it is arbitrary. So for every random-ancestral set $A \subsetneq V$ the margin $\mathcal{G}[A]$ is parameterized according to $p_{A \mid W}$ and any parameters that two or more of these margins jointly use either are consistent, or can be chosen to be consistent.

The only recursive head not found in a random-ancestral margin is $H^{*}$, so the only parameter yet to be defined is $q_{H^{*}}\left(x_{T^{*}}\right)$. We define this to be any version of $p_{H^{*} \mid T^{*}}\left(0_{H^{*}} \mid x_{T^{*}}\right)$; this is well defined if $p\left(x_{T^{*} \backslash W} \mid x_{T^{*} \cap W}\right)>0$, and arbitrary otherwise. Then

$$
p_{V \mid W}\left(0_{H^{*}}, x_{V \backslash H^{*}} \mid x_{W}\right)=q_{H^{*}}\left(x_{T^{*}}\right) \cdot p\left(x_{V \backslash H^{*}} \mid x_{W}\right)
$$

Since $V \backslash H^{*}$ is a random-ancestral margin of $\mathcal{G}$, it follows that $p\left(x_{V \backslash H^{*}} \mid x_{W}\right)$ is parameterized according to $\mathcal{G}\left[V \backslash H^{*}\right]$, and so

$$
\begin{aligned}
p_{V \mid W}\left(0_{H^{*}}, x_{V \backslash H^{*}} \mid x_{W}\right) & =p\left(0_{H^{*}} \mid x_{V \backslash H^{*}}, x_{W}\right) \cdot \prod_{O \subseteq C \subseteq V \backslash H^{*}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& =\prod_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

This gives the required result if $x_{h}=0$ for all $h \in H^{*}$. On the other hand, if $x_{h}=1_{h}$ for some $h \in H^{*}$, then using a second induction on the number of zeros in $x_{H^{*}}$ we have

$$
\begin{aligned}
& p\left(x_{V \backslash h}, 1_{h} \mid x_{W}\right) \\
& =p\left(x_{V \backslash h} \mid x_{W}\right)-p\left(x_{V \backslash h}, 0_{h} \mid x_{W}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{O \subseteq C \subseteq V \backslash\{h\}}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)-\sum_{O \cup\{h\} \subseteq C \subseteq V}(-1)^{|C \backslash(O \cup\{h\})|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right) \\
& =\sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(x_{T}\right)
\end{aligned}
$$

using Lemma 5.3. Hence, every probability $p_{V \mid W}\left(x_{V} \mid x_{W}\right)$ is of the required form.

# 5.3. Model smoothness 

For some ADMGs $\mathcal{G}$, the parameters $q_{H}\left(x_{T}\right)$ are just (versions of) the ordinary conditional probabilities $P\left(X_{H}=0 \mid X_{T}=x_{T}\right)$, and hence the alternating sum is similar to the Möbius form of the parameterization studied in Evans and Richardson [10] in the context of 'ordinary' Markov models. However, we have already seen that not all of the parameters can be interpreted this way; recall the example in Section 3 for Figure 1(b). In this case, as noted in Example 3.5, $q_{E Y}(x, m)=r_{E Y}(0,0 \mid x, m)$ is not an ordinary conditional probability, but if the graph is interpreted causally then it is the conditional probability of $\{E=Y=0\}$ after intervening to fix $\{X=x, M=m\}$

$$
\begin{aligned}
q_{E Y}(x, m) & =p_{E \mid X}(0 \mid x) \cdot p_{Y \mid X M E}(0 \mid x, m, 0) \\
& =P(Y=E=0 \mid \operatorname{do}(X=x, M=m))
\end{aligned}
$$

By the requirement that the graph is 'interpreted causally' we mean that it is the latent projection of a causal DAG in the sense of Pearl [15], Definition 1.3.1. This result holds more generally.

Theorem 5.5. If $p_{V \mid W}$ is strictly positive and recursively factorizes according to some CADMG $\mathcal{G}$, then all the parameters $q_{H}\left(x_{T}\right)$ are unique and can be smoothly recovered from $p_{V \mid W}$ (i.e., there is an infinitely differentiable function from $p_{V \mid W}$ to the $q_{H}\left(x_{T}\right)$ ).

In addition, if the graph is interpreted causally, then

$$
q_{H}\left(x_{T}\right)=P\left(X_{H}=0_{H} \mid X_{T \backslash \bar{T}}=x_{T \backslash \bar{T}}, \operatorname{do}\left(X_{\bar{T}}=x_{\bar{T}}\right)\right)
$$

where $\bar{T} \equiv T \backslash S=\mathrm{pa}_{\mathcal{G}}(S) \backslash S$ is the subset of $T$ that does not intersect $S$.
Proof. The first claim follows directly from the proof of Theorem 5.4, since the operations involved are just summations and divisions by positive quantities; the fact that $p_{V \mid W}$ is strictly positive ensures that each parameter is always uniquely defined rather than being arbitrary.

For the second part: recall that the steps (i) and (ii) in Definition 3.3 correspond to the algorithm in Tian and Pearl [27], so it follows from that paper that the conditional distribution obtained when we reach a particular intrinsic set $S$ is $p_{V}\left(x_{S} \mid \operatorname{do}\left(x_{\mathrm{pa}(S) \backslash S}\right)\right)$. Then calculating $q_{H}\left(x_{T}\right)$ just gives $p_{V}\left(0_{H} \mid x_{S \backslash H}, \operatorname{do}\left(x_{\mathrm{pa}(S) \backslash S}\right)\right)$, and hence the result.

We remark that if the distribution is not strictly positive then it follows from the ' $\Rightarrow$ ' part of the proof of Theorem 5.4 that the parameters $q_{H}\left(x_{T}\right)$ are uniquely defined if and only if

$p\left(x_{V \cap T} \mid x_{W \cap T}, y_{W \backslash T}\right)>0$ for some $y_{W \backslash T}$. In the case that $W=\varnothing$ and $\mathcal{G}$ is an ADMG, this reduces to $q_{H}\left(x_{T}\right)$ being uniquely defined if and only if $p\left(x_{T}\right)>0$.

We now return to the generality of a finite discrete state-space $\mathfrak{X}_{v}$ for each $X_{v}$. Let $\tilde{\mathfrak{X}}_{v}$ be the same set with some arbitrary entry removed (so that $\left|\tilde{\mathfrak{X}}_{v}\right|=\left|\mathfrak{X}_{v}\right|-1$ ). Then for any set $C$ let $\tilde{\mathfrak{X}}_{C} \equiv \times_{v \in C} \tilde{\mathfrak{X}}_{v}$. See Appendix C for explicit definitions of the parameters in this case.

Corollary 5.6. The set of strictly positive distributions obeying the recursive factorization property with respect to a CADMG $\mathcal{G}$ is a curved exponential family of dimension

$$
d(\mathcal{G})=\sum_{H \in \mathcal{H}(\mathcal{G})}\left|\tilde{\mathfrak{X}}_{H}\right| \cdot\left|\mathfrak{X}_{T}\right|
$$

Proof. Theorem 5.5 shows that there is a smooth (infinitely differentiable) map from positive distributions obeying the recursive factorization to the model parameters; it is clear from the form of the parameterization that the map from parameters to the probabilities is also smooth. The result follows by the same argument as Theorem 6.5 of Evans and Richardson [10].

This result allows us to invoke standard statistical theory within this class of models. For example, if $\mathcal{G}^{\prime}$ is a subgraph of $\mathcal{G}$, then we can perform a hypothesis test of $H_{0}: p_{V \mid W} \in \mathcal{M}_{r f}\left(\mathcal{G}^{\prime}\right)$ versus $H_{1}: p_{V \mid W} \in \mathcal{M}_{r f}(\mathcal{G})$ by comparing the likelihood ratio statistic to a $\chi_{k}^{2}$ distribution, where $k=d(\mathcal{G})-d\left(\mathcal{G}^{\prime}\right)$.

Fitting these models is relatively straightforward given the explicit maps between parameters and probabilities. Maximum likelihood estimation can be performed using the same method as in Evans and Richardson [8]. The parameters $q_{H}\left(x_{T}\right)$ are clearly variation dependent, which can cause algorithmic complications and interpretability problems. A (generally variation dependent) log-linear parameterization of the kind given in Evans and Richardson [9] can relatively easily be adapted to nested models; see also Shpitser et al. [19].

# 6. Examples 

The Wisconsin Longitudinal Study (Hauser et al. [11]) is a panel study of over 10000 people who graduated from Wisconsin High Schools in 1957. We consider males who, when asked in 1975, had either been drafted or had not served in the military at all; after removing missing data this left 1676 respondents. We wish to know whether, after controlling for family income and education, being drafted had a significant effect on future earnings.

The variables measured were:

- $X$, an indicator of whether family income in 1957 was above $\$ 5 \mathrm{k}$;
- $Y$, an indicator of whether the respondent's income in 1992 was above $\$ 37 \mathrm{k}$;
- $M$, an indicator of whether the respondent was drafted into the military;
- $E$, an indicator of whether the respondent had education beyond high school.

Dichotomizations for $X, Y$ and $E$ were chosen to be close to the median values of the original variables. The data are shown in Table 1; in each case the value 1 corresponds to the statement

Table 1. Data from the Wisconsin Longitudinal Study




above being true, 0 otherwise. One possible model is that future income is unrelated to family income at the time of graduation after controlling for military service and level of education. This suggests the graph in Figure 8(a), where the directed edge from $X$ to $Y$ is not present. We can fit this model using the parameterization and an algorithm based on the one given by Evans and Richardson [8]; the resulting fit has a deviance of 31.3 on 2 degrees of freedom, strongly suggesting that the model should be rejected. Unsurprisingly, the graph in Figure 1(b) is also rejected for these data.

On the other hand the model shown in Figure 8(b) has a deviance of 5.57 on 6 degrees of freedom, which indicates a good fit. Note that this implies that there is no evidence of a significant effect of being drafted on future income, even though marginally there is a strong negative correlation. Models obtained by removing any additional edges are strongly rejected. Under this model, the probability of having a high income in 1992 is estimated as 0.50 (standard error 0.018 ) if the family had high income, and $0.36(0.016)$ if not.

In other words, we estimate

$$
P(Y=1 \mid \operatorname{do}(X=1))=0.50, \quad P(Y=1 \mid \operatorname{do}(X=0))=0.36
$$

indicating a strong causal effect.
![img-7.jpeg](img-7.jpeg)

Figure 8. Two models for the Wisconsin miltary service data. (a) A proposed but rejected model; (b) a well-fitting model. See text for discussion.

# Appendix A: Proof of the Verma constraint 

Note that

$$
\begin{aligned}
\sum_{e} p(e \mid x) \cdot p(y \mid x, m, e) & =\sum_{e} \frac{p(x, m, e, y)}{p(x) \cdot p(m \mid x, e)} \\
& =\sum_{e} \frac{\sum_{u} p(u, x, m, e, y)}{p(x) \cdot p(m \mid x, e)}
\end{aligned}
$$

by elementary laws of conditional probability. Applying the usual factorization of the DAG in Figure 1(a), we obtain

$$
=\sum_{e} \frac{\sum_{u} p(u) \cdot p(x) \cdot p(e \mid x, u) \cdot p(m \mid e) \cdot p(y \mid m, u)}{p(x) \cdot p(m \mid x, e)}
$$

noting that $M \Perp X \mid E$, and cancelling, gives

$$
\begin{aligned}
& =\sum_{e, u} p(u) \cdot p(e \mid x, u) \cdot p(y \mid m, u) \\
& =\sum_{u} p(u) \cdot p(y \mid m, u)
\end{aligned}
$$

which does not depend upon $x$.

## Appendix B: Partitions

Let $V$ be an arbitrary finite set, and let $\mathcal{H}$ be an arbitrary collection of non-empty subsets of $V$, with the restriction that $\{v\} \in \mathcal{H}$ for all $v \in V$ (i.e. all singletons are in $\mathcal{H}$ ). A partial ordering $\prec$ on the elements of $\mathcal{H}$ will be said to be partition suitable if for any $H_{1}, H_{2} \in \mathcal{H}$ with $H_{1} \cap H_{2} \neq \varnothing$, there exists $H^{*} \in \mathcal{H}$ such that $H^{*} \subseteq H_{1} \cup H_{2}$ and $H_{i} \preceq H^{*}$ for each $i=1,2$. (Here $H_{1} \preceq H_{2}$ means $H_{1} \prec H_{2}$ or $H_{1}=H_{2}$.)

Define a function $\Phi$ on subsets of $V$ such that $\Phi(W)$ 'picks out' the set of $\prec$-maximal elements of $\mathcal{H}$ that are subsets of $W$. That is,

$$
\Phi(W) \equiv\left\{H \in \mathcal{H} \mid H \subseteq W \text { and } H \nprec H^{\prime} \text { for all other } H^{\prime} \subseteq W\right\}
$$

Define $\psi(W)$ to be the set of vertices not in any set in $\Phi(W)$, that is:

$$
\psi(W) \equiv W \backslash \bigcup_{C \in \Phi(W)} C
$$

Now recursively define a function $[\cdot]$ that partitions subsets of $V$ : define $[\varnothing]=\varnothing$, and

$$
[W] \equiv \Phi(W) \cup[\psi(W)]
$$

It is clear that $\bigcup_{A \in[W]} A=W$.
The next proposition shows that $[W]$ is indeed a partition of $W$.
Proposition B.1. If $H_{1}, H_{2} \in \Phi(W)$ with $H_{1} \neq H_{2}$ then $H_{1} \cap H_{2}=\varnothing$.
Proof. Suppose $H_{1} \cap H_{2} \neq \varnothing$. Then by partition suitability, there exists $H^{*} \subseteq H_{1} \cup H_{2}$ with $H^{*} \succeq H_{1}, H_{2}$, and in particular $H^{*} \succ H_{i}$ for at least one of $i=1,2$. Hence at least one of the $H_{i}$ is not maximal in $W$.

Proposition B.2. If $A \subseteq W_{1} \subseteq W_{2}$, and $A \in \Phi\left(W_{2}\right)$ then $A \in \Phi\left(W_{1}\right)$.
Proof. If $A$ is maximal amongst elements of $\mathcal{H}$ that are subsets of $W_{2}$, then it is certainly still maximal amongst those that are subsets of $W_{1}$, since there are fewer such sets.

Proposition B.3. If $C \in[W]$, then $[W]=\{C\} \cup[W \backslash C]$.
Proof. We proceed by induction on the size of $W$. If $[W]=\{C\}$, including any case in which $|W|=1$, the result is trivial.

If $C$ is not maximal with respect to $\prec$ among subsets of $W$, then $\Phi(W)=\Phi(W \backslash C)$, and so

$$
\begin{aligned}
{[W] } & =\Phi(W) \cup[\psi(W)] \\
& =\Phi(W \backslash C) \cup[\psi(W)]
\end{aligned}
$$

and the problem reduces to showing that $[\psi(W)]=\{C\} \cup[\psi(W \backslash C)]$, which follows from the induction hypothesis. Thus, suppose $C \in \Phi(W)$.

Now by Proposition B.2, $\Phi(W \backslash C) \cup\{C\} \supseteq \Phi(W)$, and if equality holds we are done. Otherwise let $C_{1}, \ldots, C_{k}$ be the sets in $\Phi(W \backslash C)$ but not in $\Phi(W)$. These sets are maximal in $W \backslash C$, so they are in $\Phi(\psi(W))$ by Proposition B.2, since by hypothesis, $\psi(W) \subseteq W \backslash C$. Then the problem reduces to showing that

$$
[\psi(W)]=\left\{C_{1}, \ldots, C_{k}\right\} \cup\left[\psi(W) \backslash\left(C_{1} \cup \cdots \cup C_{k}\right)\right]
$$

which follows from repeated application of the induction hypothesis.
Proposition B.4. Let $D_{1}, \ldots, D_{k}$ be a partition of $V$, and suppose that each $H \in \mathcal{H}$ is contained within some $D_{i}$. Let $\prec$ be a partition-suitable partial ordering. Then

$$
[W]=\bigcup_{i=1}^{k}\left[W \cap D_{i}\right]
$$

Proof. We prove the case $k=2$, from which the general result follows by repeated applications. We proceed by induction on the size of $W$. If either $W \cap D_{1}$ or $W \cap D_{2}$ are empty, then the result is trivial. By definitions

$$
[W]=\Phi(W) \cup[\psi(W)]
$$

$\psi(W)$ is strictly smaller than $W$, so by the induction hypothesis

$$
[W]=\Phi(W) \cup\left[\psi(W) \cap D_{1}\right] \cup\left[\psi(W) \cap D_{2}\right]
$$

From the condition on $\mathcal{H}$ we can write $\Phi(W)=\mathcal{C}_{1} \cup \mathcal{C}_{2}$ where each $H \in \mathcal{C}_{i}$ is a subset of $D_{i}$; since the elements of $\mathcal{C}_{i}$ are maximal with respect to $\prec$ in $W$, they are also maximal in $W \cap D_{i}$. Hence $\mathcal{C}_{i} \subseteq \Phi\left(W \cap D_{i}\right)$, and then applying Proposition B. 3 repeatedly gives

$$
\mathcal{C}_{i} \cup\left[\psi(W) \cap D_{i}\right]=\left[W \cap D_{i}\right]
$$

because $\left(\psi(W) \cap D_{i}\right) \cup \bigcup \mathcal{C}_{i}=W \cap D_{i}$. Hence the result.

# B.1. Partition suitability of recursive head ordering 

The next result, together with Proposition B.1, shows that the function $\llbracket \cdot \rrbracket_{\mathcal{G}}$, from Definition 4.11, is indeed a partition.

Proposition B.5. $\prec$ is partition suitable for $\mathcal{H}(\mathcal{G})$.
Proof. Lemma 4.8 shows that $\mathcal{H}$ contains the singleton vertices. Now suppose we have two recursive heads $H_{1}, H_{2}$ with $H_{1} \cap H_{2} \neq \varnothing$. Let the associated intrinsic sets be $S_{1}, S_{2}$. Since $S_{1}, S_{2}$ are bidirected connected sets and they share a common element, $S_{1} \cup S_{2}$ is also bidirectedconnected. Let $S^{*}$ be the intrinsic closure of $S_{1} \cup S_{2}$, with recursive head $H^{*}$. Then $S^{*}$ contains both $S_{1}$ and $S_{2}$, and therefore $H^{*} \succeq H_{1}, H_{2}$.

By Proposition 4.7, $H^{*}=\operatorname{sterile}_{\mathcal{G}}\left(S^{*}\right) \subseteq S_{1} \cup S_{2}$; by definition of a recursive head, any $v \in S_{1}$ is either in $H_{1}$ or is a parent of some other element of $S_{1}$ (and the same for $S_{2}$ ). Hence $H^{*} \subseteq$ $H_{1} \cup H_{2}$.

## Appendix C: General discrete state-space

Lemmas 5.2 and 5.3 and Theorem 5.4 are stated and proved for binary variables to avoid cumbersome notation; here we provide some notes on how one would adapt them to the general case.

Suppose that $\mathfrak{X}_{V W}$ is possibly non-binary. For each $v \in V$ pick an arbitrary element $k_{v} \in \mathfrak{X}_{v}$ to be a corner-point. Let $\tilde{\mathfrak{X}}_{v} \equiv \mathfrak{X}_{v} \backslash\left\{k_{v}\right\}$ and $\tilde{\mathfrak{X}}_{C} \equiv \times_{v \in C} \tilde{\mathfrak{X}}_{v}$. In the binary case we took $k_{v}=1$, so that $\tilde{\mathfrak{X}}_{v}=\{0\}$ for each $v$.

The parameters then become $q_{H}\left(x_{H} \mid x_{T}\right)$ for $H \in \mathcal{H}(\mathcal{G}), x_{H} \in \tilde{\mathfrak{X}}_{H}$ and $x_{T} \in \mathfrak{X}_{T}$. The parameterization in (6) becomes:

$$
p_{V \mid W}\left(x_{V} \mid x_{W}\right)=\sum_{O \subseteq C \subseteq V}(-1)^{|C \backslash O|} \sum_{y_{C} \in \tilde{\mathfrak{X}}_{C}: y_{O}=x_{O}} \prod_{H \in \llbracket C \rrbracket_{\mathcal{G}}} q_{H}\left(y_{H} \mid x_{T}\right)
$$

where $O \equiv O\left(x_{V}\right)=\left\{v \mid x_{v} \in \tilde{\mathfrak{X}}_{v}\right\}$. Note that, in the binary case, the inner sum only ever has one term.

Lemma 5.2 goes through as before by splitting the inner sum up as

$$
\sum_{y_{C} \in \tilde{\mathfrak{X}}_{C}: y_{O}=x_{O}}=\sum_{y_{C_{1}} \in \tilde{\mathfrak{X}}_{C_{1}}: y_{O_{1}}=x_{O_{1}}} \sum_{y_{C_{2}} \in \tilde{\mathfrak{X}}_{C_{2}}: y_{O_{2}}=x_{O_{2}}}
$$

The proof of Theorem 5.4 is also the same, except that instead of $x_{h}=0$ and $x_{h}=1$ the important cases become $x_{h} \in \tilde{\mathfrak{X}}_{h}$ and $x_{h}=k_{h}$.

# Acknowledgements 

This research uses data from the Wisconsin Longitudinal Study (WLS) of the University of Wisconsin-Madison, which is supported principally by the National Institute on Aging. Evans was funded by EPSRC grant EP/N020294/1, and Richardson by U.S. National Institutes of Health grant R01 AI032475 and U.S. Office of Naval Research grant N00014-15-1-2672. The research was also supported by a SQuaRE grant from the American Institute of Mathematics. We thank two anonymous reviewers and an associate editor for suggesting several improvements to the paper.
